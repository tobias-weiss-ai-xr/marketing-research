---
title: 'ActiveMem: Dynamic Latent Memory Trees for Long-Horizon Agents'
url: https://arxiv.org/abs/2609.33244
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Song-Li Wu
- Jingyi Wang
- Zhaocheng Du
- Weinan Gan
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.33244
pages: 20
chars: 91695
fetched_at: '2026-11-08T13:34:41+00:00'
kb_version: 1
---

# ActiveMem: Dynamic Latent Memory Trees for Long-Horizon Agents

ActiveMem: Dynamic Latent Memory Trees for Long-Horizon Agents
Song-Li Wu1∗, Jingyi Wang1∗, Zhaocheng Du†2, Weinan Gan2
1Tsinghua University,2Huawei Noah’s Ark Lab
Abstract
LargeLanguageModel(LLM)agentsincreasinglyrelyonex-
ternalmemorytosupportlong-horizonreasoninganddecision
making.Existingmemorysystemstypicallyretrievehistorical
trajectories or summaries as independent context fragments,
overlooking the procedural dependencies underlying multi-
step execution. As memory scales, such flat retrieval intro-
ducescontextfragmentationandcross-taskinterference,lead-
ingtostructurallyinconsistentreasoningtrajectories.Wepro-
pose ActiveMem, a hierarchical memory framework that re-
cursivelyorganizesagentexperiencesintodependency-aware
latent execution trees. ActiveMem abstracts trajectories into
reusable subtask nodes while explicitly preserving execution
transitions, enabling coherent reasoning-path retrieval con-
ditioned on the current execution state. To support contin-
ual adaptation, ActiveMem further learns dynamic memory
expansion, retrieval, and pruning policies through reinforce-
mentlearning.Experimentsacrossvariousagentbenchmarks
demonstratethatActiveMemconsistentlyimprovestaskcom-
pletion, reasoning stability, and memory efficiency over ex-
isting memory-based agents. Moreover, ActiveMem enables
compact open-weight models to achieve competitive perfor-
mance with substantially larger proprietary systems.
1 Introduction
Large Language Model (LLM) agents are increasingly ex-
pectedtosolvelong-horizontasksthatrequirepersistentrea-
soning, adaptive planning, and multi-step interaction with
dynamic environments (Xu and Yan 2026; Hu et al. 2025b;
Wuetal.2026b).Unlikestaticlanguagegeneration,success-
ful agent execution depends on maintaining coherent pro-
cedural states across extended decision trajectories, where
earlyactionsdirectlyinfluencesubsequentreasoningandex-
ecution outcomes (Chu et al. 2026; Erdogan et al. 2026; Wu
et al. 2026d). To support such long-term decision making,
recent agent frameworks increasingly incorporate external
memorymechanismsthataccumulateandretrievehistorical
experiences (Zhou et al. 2025b; Zhang, Fu, and Yan 2026).
Despiterecentprogress,existingmemorysystemsprimar-
ilyretrievepastexperiencesastrajectoryfragments,summa-
rized histories, or semantically similar contexts (Yao et al.
2022b; Wu et al. 2026a; Wang et al. 2026; Wu et al. 2026g),
often overlooking the procedural dependencies underlying
long-horizon execution. However, agent behaviors are in-
herently structured, where interdependent subtasks follow
∗These authors contributed equally.
†Corresponding author.
Copyright©2027, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
causally constrained execution transitions rather than iso-
lated action sequences. As illustrated in Fig. 1, retrieving
memories from such flat memory structures can introduce
contextfragmentationandcross-taskinterference,leadingto
workflow mismatch and inconsistent reasoning trajectories.
For example, the agent may retrieve functionally relevant
yet sequentially incompatible actions from unrelated tasks
(e.g., hotel-booking procedures during flight booking). As
memory scales over extended interaction histories, these in-
consistenciesincreasinglydestabilizereasoninganddegrade
execution coherence.
A key challenge therefore lies not only in storing his-
torical experiences, but in organizing and retrieving them
in a manner consistent with procedural execution structure.
Long-horizontasksnaturallyexhibithierarchicaldecomposi-
tion:high-levelgoalsareprogressivelyresolvedintoreusable
subtasks, while successful execution depends on preserv-
ing dependency relationships between intermediate reason-
ing states. This suggests that effective agent memory should
support both structured abstraction and dependency-aware
retrieval, rather than treating historical trajectories as inde-
pendent reusable contexts.
Motivated by this observation, we proposeActiveMem,
a hierarchical memory framework for long-horizon LLM
agents. ActiveMem organizes agent experiences into aLa-
tent Memory Tree, where nodes encode reusable subtask-
level reasoning abstractions and edges capture their execu-
tiondependencies.Thisstructureenablestheagenttoretrieve
coherent reasoning paths aligned with the current execution
stagewhilesuppressinginterferencefromirrelevantprocedu-
ral branches. Rather than directly retrieving isolated histori-
caltrajectories,ActiveMemretrievesdependency-consistent
executionpathsthatpreservehigh-levelproceduralstructure
duringdownstreamreasoning.AsshowninFig.1(b),ourAc-
tiveMem uses structured memory to preserve causal chains
and enforce task isolation, retrieving only domain-relevant
steps and enabling correct, end-to-end execution.
Beyond structured memory representation, ActiveMem
further models memory evolution as an adaptive decision-
making process. Specifically, the framework dynamically
expands, refines, compresses, and prunes the hierarchical
memorytopologyaccordingtotheagent’songoingreasoning
stateandlong-horizontaskfeedback.Duringinteraction,Ac-
tiveMem selectively activates dependency-consistent mem-
arXiv:2609.33244v2  [cs.AI]  19 Oct 2026

      User:  Found Paris flight transfer in Barcelona <€200,
add 23kg bag, Veg. Meal, Email tix to work.
Direct Paris
Flight <€200
Order a
meal for wife
Check Paris
weather
Paris Hotel
Veg. Breakfast
Paris Opera Tix
<$800,Email Tix
Flat Memory Pool
Retrieval
sim 0.87
sim 0.31
sim 0.28
sim 0.80
sim 0. 75
Concatenated Context
Problem 2: Cross-Task Leakage
Select
Room
Fill
Dates
Add
Breakfast
Search
Filghts
Add
Bag
Email
Ticket
Retrieved workflow (Hotel)
Correct workflow (Filght)
bindly applied
steps from hotel ≠ flight workflow
Policy
Problem 1: Context Fragmentation
trip.com
FLR ORY
Nonstop
Agent Action(Direct Flight) Agent Action(Transfer Flight )
trip.com
FLR ORY
Nonstop
FLR ORY
6h in Barcelona
      User:  Found Paris flight transfer in Barcelona <€200,
add 23kg bag, Veg. Meal, Email tix to work.
Structured Memory Pool
Flight
TransferNonstop
WeatherHotel Opera Meal
User
other domains
Structured Context
Task Isoluation
Hotel steps filtered
 Opera steps filtered
1. Search Paris via Barcelona
2. Select layover flight
3. Add 23kg bag + meal
4. Book & email ticket
Preserve Causal Chains
trip.com
FLR ORY
Nonstop
FLR ORY
6h in Barcelona
Takeout Dine-in
Filght Domain Only:
(a) Flat Memory (b) ActiveMem
Figure 1: Comparison between Flat Memory and ActiveMem. (a) Flat memory methods retrieve disparate context fragments
and mixed workflows from a flat pool based on simple similarity, leading to context fragmentation and cross-task leakage (e.g.,
blindly applying hotel booking steps to a flight workflow). (b) ActiveMem organizes context using a structured memory pool
with a tree hierarchy. It enforces task isolation to filter out irrelevant domains and preserves causal chains mapping to the
HTML/UI, enabling the agent to accurately plan domain-specific steps and execute the correct transfer flight action.
ory paths to support current reasoning, while reinforcement
learning continuously optimizes memory organization poli-
cies through trajectory-level rewards. This design enables
the agent to progressively form compact and reusable long-
termmemoryabstractionswhilekeepingthebackboneLLM
frozen.
We evaluate ActiveMem across various long-horizon rea-
soningandagentbenchmarksspanninginteractiveplanning,
webnavigation,andmulti-stepdecisionmaking.Experimen-
tal results show that ActiveMem consistently improves rea-
soning stability and task completion over existing memory-
based agents while substantially reducing active context us-
age. Further analysis demonstrates that explicitly modeling
procedural dependencies enables more robust memory re-
trievalandstrongergeneralizationacrossheterogeneoustask
environments.
2 Related Works
2.1 Large Language Model Agents
RecentadvancementshaveelevatedLargeLanguageModels
(LLMs)toautonomousfoundationagentscapableofcontin-
uous perception, reasoning, and tool manipulation (Xi et al.
2025a). Despite their rapid deployment across complex do-
mains (Luo et al. 2025; Liu et al. 2025a), achieving robust
long-horizon reliability remains a primary bottleneck due
to compounding errors and finite context windows (Zhang
et al. 2025b; Wu et al. 2025, 2026c). Consequently, explicit
memory management has emerged as an indispensable in-
frastructure (Lu et al. 2025; Wu et al. 2023). While current
frameworksemploysummarization,reflection,orconsolida-
tion to extend context capacity (Zheng et al. 2025a; Xi et al.
2025b; Wu et al. 2026f), they predominantly flatten multi-
step interactions into unstructured formats. This structural
oversimplification completely fails to preserve causal de-
pendencies,underscoringthecriticalneedtoovercomesuch
representationalbottlenecksforsustained,complexproblem-
solving.
2.2 Memory Agent
External memory is essential for long-horizon LLM agents
operating beyond limited context windows. Existing ap-
proaches typically either accumulate raw interaction trajec-
tories (Yao et al. 2022b; Wu et al. 2026a,e), which preserve
execution details but suffer from context saturation and re-
trieval noise, or compress experiences through summariza-
tion (Zhou et al. 2025b), improving efficiency at the cost of
procedural information loss. More broadly, episodic mem-
ory systems (Wang et al. 2023; Packer et al. 2023) generally
organize experiences as flat sequences or isolated memory
unitsindexedbysemanticsimilarity.Flatmemoryparadigms
largelyoverlookthestructuraldependenciesunderlyinglong-

horizon execution. As complex agent behaviors consist of
interdependent subtasks with causally constrained transi-
tions, retrieving isolated experiences often entangles high-
level planning with incompatible execution details, leading
to cross-task interference and inconsistent reasoning.
3 Method
3.1 Overview and Problem Formulation
We formulate agent interaction as a sequential decision-
making process. Given a task instructionx, a frozen LLM
πθ interactswithanenvironmentEoverTsteps,producinga
trajectoryτ= (s 0, a0, . . . , sT ). At any stept, the historical
trajectory prefixτ <t is condensed into a dynamic Hierar-
chical Latent Memory Tree (HLMT), denoted asTt, to pre-
ventcontextoverflow.Thememorystateevolvesdynamically
through a discrete update function composed of immediate
topological actions and periodic reward-based maintenance:
Tt = TreeUpdate(Tt−1, atree t−1).(1)
Given the current statest, the framework retrieves a rel-
evant memory pathP t =f retrieve(st,T t). A standalone
lightweightcontrollerW ϕprocessesP talongsidethecurrent
observation contexth t =f enc(st;π θ), wheref enc extracts
the last-token hidden state from the frozen LLM, to produce
a shared representationu t. This representation routes into
two heads: generating a latent memory prefixmt to condi-
tion the frozen LLM, and predicting a tree actionatree t to
manage memory topology.
WeoptimizethesharedparametersϕviaGRPO(Guoetal.
2025). Although the latent head does not output discrete ac-
tions, the injected prefixmt(ϕ)alters the hidden activations
ofthefrozenLLM,therebyimplicitlydefininganewparam-
eterized policy over action tokens. Thus, the latent head is
updated by optimizing this memory-conditioned policy:
πθ,ϕ(at |s t) =π θ(at |s t, mt(ϕ)).(2)
Our goal is to find parametersϕthat maximize the ex-
pected trajectory return:
max
ϕ
Ex∼D,τ∼π θ,ϕ

R(τ)

.(3)
To implement this formulation, we propose ActiveMem.
Ourdesignexplicitlydepartsfrompriormemory-augmented
agentsinthreefundamentalaspects:(1)utilizingcontinuous
latentmemoryinsteadofrawtextualchunks;(2)activelyop-
timizing memory topology rather than passively appending
history; and (3) jointly optimizing reasoning adaptation and
memory structures via reinforcement learning.
3.2 Hierarchical Latent Memory Tree (HLMT)
HLMT organizes history into a directed tree topologyTt.
Eachnodeisdefinedasatuplen i = (ei, pa(i), ch(i)).Here,
ei ∈R d is a node embedding representing a compressed la-
tent summary of historical states produced by the controller,
whilepa(i)andch(i)denote the parent node pointer and
the set of child nodes, respectively. While graph structures
supportbroadassociativesearch,atreeframeworkexplicitly
models semantic hierarchy. Upper nodes capture coarse task
Algorithm 1: ActiveMem Forward Pipeline
Require:Initial states 0, frozen LLMπ θ, learnable con-
trollerW ϕ.
Ensure:Updated memory treeT T and optimized parame-
tersϕ.
1:Initialize:T 0 with a virtual root nodenr.
2:fort= 1, . . . , Tdo
3:h t ←f enc(st;π θ)
4:P t ←f retrieve(st,T t−1)
5: ¯pt ← 1 |Pt| P ni∈Pt ei
6:u t ←MLP shared([ht; ¯pt])
7:m t ←W latentut
8:a tree t ∼Softmax(W treeut)
9:a t ∼π θ,ϕ(· |st, mt)
10:s t+1, rt ← E(st, at)
11:T t ←TreeUpdateImmediate(T t−1, atree t ,u t,P t)
12:end for
13:T T ←TreeMaintenance(T T )
14:ϕ←OptimizeParameters({s t, at, rt}T t=1, ϕ)
semantics, whereas lower nodes preserve fine-grained exe-
cutiondetails.Consequently,theretrievaloperationprogres-
sivelynarrowsthesearchspace,enablingefficientcoarse-to-
fine reasoning. Att= 0, the tree is initialized with a virtual
root noden r, serving solely to initialize traversal. It does
not encode task-specific semantics and resets at the episode
boundary. Usingh t as the query, we perform a recursive
greedy traversal. At depthk, we select the child maximizing
cosine similarity:
nk+1 = arg max n∈ch(k)
ht ·e n
∥ht∥∥en∥ .(4)
The traversal terminates at stepdwhen the maximum
similarity falls below a thresholdτstop. If no child satisfies
thecriterion,thepathconsistsonlyoftheroot.Theresulting
pathP t = (n 1, . . . , nd)represents the activated historical
branch.
3.3 Dual-Head Memory Controller
TheindependentcontrollerW ϕ processesthestructuredhis-
tory.First,theretrievedpathP t isaggregatedviameanpool-
ing: ¯pt = 1 |Pt| P ni∈Pt ei. Because the tree traversal inher-
ently preserves explicit semantic hierarchy, the path order
is implicitly encoded by the traversal depth, making mean
pooling highly effective. The shared representation is then
computed via a 2-layer MLP:ut = MLPshared([ht; ¯pt]).
Latent Injection Head.To condition the generation pro-
cess without the heavy overhead of layer-wise modifica-
tions, the latent head generates a dynamic continuous prefix
mt =W latentut ∈R lp×dmodel. Instead of intervening at ev-
ery transformer layer, this latent prefix is directly prepended
to the input embeddings of the current observation. By act-
ing as a dynamic soft prompt,m t effectively guides the
frozen LLM’s reasoning. During RL optimization, although
theLLMparametersθarestrictlyfrozen,gradientsfromthe
RLobjectivearebackpropagatedthroughtheLLM’scompu-

tationalgraphdowntotheinputlayer,allowingthecontroller
parametersϕto be updated end-to-end.
Tree Action Head.Concurrently, the tree head predicts a
probabilitydistributionoverdiscretetopologicaloperations:
πtree(· |ut) = Softmax(W treeut). At each step, a discrete
actiona tree t ∼π tree is sampled. To manage the memory
structureefficientlywithoutoverwhelmingthecontroller,we
decouple the topology optimization into high-frequency se-
mantic updates (Immediate Execution) and low-frequency
utility-based pruning (Deferred Execution).
Immediate Execution (TreeUpdateImmediate).
During stept, the memory topology is dynamically updated
online based on the sampled tree actionatree t . Specifically,
if the action dictates an insertion (atree t =insert), a new
nodee new =W insut is attached as a child to the retrieved
leafn d to explicitly preserve the temporal hierarchy.
Conversely, if an update is triggered (atree t =update), the
existing leaf node is refined via a learned gating mechanism
α=σ(W gateut), which updates its representation as
ed ←(1−α)e d +αW updut. To prevent catastrophic rep-
resentational collapse during continuous RL optimization,
all newly inserted or updated embeddings are explicitly
constrained viaL2 normalization.
Deferred Execution (TreeMaintenance).At the
episode endT, we perform periodic structural maintenance
to ensure memory efficiency and reliability based on en-
vironmental feedback. We first calculate the episodic re-
turnsS(n i)for all activated nodes, averaging the returns
for nodes with multiple activations within the same episode
to prevent over-crediting high-frequency loops. These util-
ities are then smoothed using an exponential moving av-
erage:S EMA(ni)←(1−β)S EMA(ni) +βS(n i). Based
onthesesmoothedstatistics,wepruneobsoletenodeswhose
SEMA(ni)fallsbelowathresholdτ del,reassigningtheirchil-
drench(i)directlytotheparentpa(i)tomaintaintopological
connectivity. Finally, to further reduce computational over-
head,anysiblingnodesexhibitinghighrepresentationalsim-
ilarity (sim(ei,e j)> τmerge) are fused together via average
pooling.
3.4 Training Recipe
We optimize the shared parametersϕvia Group Relative
Policy Optimization (GRPO), eliminating the need for a
memory-intensive critic model. For a given reasoning task,
we sample a group of trajectoriesGfrom the current pol-
icy. To address the sparsity of final rewards in long-horizon
interactions, we enhance the GRPO framework with veri-
fiable process supervision. Thus, the episodic utilityS(ni)
for a memory node incorporates both fine-grained verifiable
step rewards and the final return:S(ni) = PT k=ti γk−ti rk. Instead of relying on a learned baseline, the hierarchical ad-
vantageA i evaluates structural contribution by normalizing
returns within the sampled group:
Ai =λ g
 S(ni)−µ G(S)
σG(S) +ϵ 0

+λ l (S(ni)−S(pa(i)))(5)
whereµ G(S)andσ G(S)are the mean and standard devi-
ation of utilities across the groupG. The global advantage
encouragestask-levelusefulnessrelativetoalternativegroup
rollouts, while the local advantage preserves relative node
specialization.
The parametersϕare updated using a joint GRPO surro-
gate objective:
L(ϕ) =L latent GRPO(ϕ) +λL tree GRPO(ϕ)(6)
where the latent objective updates the memory-conditioned
policy using the group-normalized environment advantage
Aenv t andaKullback-Leibler(KL)divergencepenaltytopre-
vent policy collapse:
Llatent GRPO(ϕ) =−E τ∈G,t [min(ρenv t (ϕ)Aenv t ,
clip (ρenv t (ϕ),1−ϵ,1 +ϵ)A env t )−βD KL (πθ,ϕ∥πref )]
(7)
with the probability ratioρenv t (ϕ) = πθ,ϕ(at|st) πθ,ϕold (at|st). The tree
objectiveL tree GRPO(ϕ)follows an identical clipped formula-
tion, replacingρ env t with the tree action ratio and utilizing
the hierarchical group advantageA i. Because both heads
optimize complementary objectives on a shared representa-
tion, gradients are jointly accumulated. We did not observe
training instability.
4 Experiments
4.1 Experimental Setup
EvaluationandBenchmarks.Tocomprehensivelyevalu-
ate the generalizability of our method, we follow the experi-
mental setup of Zhang, Fu, and Yan (2026) and benchmark
across nine datasets spanning five core domains. Specifi-
cally,theseincludewebsearch(TriviaQA(Joshietal.2017),
PopQA (Mallen et al. 2023) and FEVER (Zhang, Fu, and
Yan 2026)), embodied action (ALFWorld (Shridhar et al.
2020)and ScienceWorld(Zhang, Fu,and Yan2026)),math-
ematicalreasoning(GSM8K(Cobbeetal.2021)andMATH
(Hendrycks et al. 2021)), scientific reasoning (GPQA (Rein
etal.2023)),andcodegeneration(KodCode(Xuetal.2025b)
and BigCodeBench (Jain et al. 2025)).
Baselines.We evaluate ActiveMem against twelve base-
linesacrossfourcategories:(I)Prompt-basedmethods,in-
cluding the Vanilla model and CoT (Wei et al. 2022); (II)
Parametric memory, which incorporates experiences di-
rectly into model weights via SFT, GRPO, REINFORCE
(Williams 1992), REINFORCE++ (Hu et al. 2025a), and
Agent-FLAN(Chenetal.2024);(III)Retrieval-basedmem-
ory, which utilizes external databases for sequential expe-
rience storage, represented by MemoryBank (Zhong et al.
2024),ExpeL(Zhaoetal.2024),andAgentWorkflowMem-
ory (AWM) (Wang et al. 2024); and (IV)Latent computa-
tion, which employs latent tokens as experience carriers,
such as SoftCoT (Xu et al. 2025a), Co-processor (Liu et al.
2024) and MemGen (Zhang, Fu, and Yan 2026).
Implementation Details.We employ several LLM back-
bones of varying scales, including Qwen-2.5-1.5B (Yang
et al. 2024a), SmolLM3-3B (HuggingFace 2025), and
Qwen3-8B(Yangetal.2025).Thelengthofthelatentmem-
ory sequenceKis chosen from{2,4,8}. ActiveMem does

Table1:ResultsonSmolLM3-3BandQwen3-8B.Allvaluesrepresenttheperformancemetricforeachtask(e.g.,accuracy%).
We highlight the best and second best results.
Backbone Method ALFWorld TriviaQA PopQA KodCode BigCodeBench GPQA GSM8K MATH
SmolLM3-3B
Vanilla 18.96 10.47 8.23 37.05 35.96 9.35 47.63 16.22
CoT 17.60 12.88 9.95 38.45 39.42 20.70 58.91 56.33
SFT 32.36 55.25 37.22 59.25 40.79 19.70 63.48 45.65
GRPO 55.35 65.88 45.16 68.48 72.44 22.73 80.03 61.23
REINFORCE 53.13 63.20 46.81 65.53 67.14 23.44 82.03 58.75
REINFORCE++ 53.95 63.20 44.10 65.90 68.80 22.73 81.50 59.89
Agent-FLAN 34.00 56.70 39.50 56.80 37.20 17.80 59.60 36.84
ExpeL 36.18 46.20 28.16 51.14 40.22 15.15 56.23 38.11
MemoryBank 32.80 43.30 25.81 44.50 31.80 10.20 58.30 43.53
AWM 40.50 49.80 29.60 - - - - -
SoftCoT 35.03 50.38 34.90 59.20 39.10 17.22 56.34 44.62
Co-processor 38.36 53.28 38.96 56.25 45.40 20.10 57.60 38.81
MemGenSFT 50.60 68.13 42.34 62.65 42.99 26.75 70.42 57.44
MemGenGRPO 63.60 79.30 58.60 72.85 74.24 25.20 83.47 63.65
ActiveMemSFT 64.35 80.42 61.82 74.89 78.31 31.52 85.76 64.97
ActiveMemGRPO 73.26 86.14 71.30 84.02 92.26 36.83 90.36 80.62
Qwen3-8B
Vanilla 58.93 52.18 34.13 49.10 33.33 38.18 89.48 79.82
CoT 57.10 53.80 33.20 51.25 35.59 35.15 87.67 78.24
SFT 83.59 74.55 51.12 64.75 41.33 40.33 90.76 81.35
GRPO 85.60 76.15 58.90 73.35 70.24 39.54 92.30 83.54
REINFORCE 82.10 75.22 57.96 72.11 70.20 37.12 91.25 83.27
REINFORCE++ 84.80 75.90 58.30 72.90 71.88 37.68 91.90 85.24
Agent-FLAN 80.32 70.32 50.08 62.99 43.40 39.50 87.60 80.05
ExpeL 78.97 65.54 40.33 57.20 34.23 35.15 86.20 77.40
MemoryBank 70.41 60.56 41.60 56.39 40.61 35.66 90.35 80.35
AWM 80.33 69.30 43.69 - - - - -
SoftCoT 75.60 59.42 39.42 63.28 38.27 39.60 86.30 76.23
Co-processor 73.28 61.42 45.55 64.90 42.19 39.15 76.23 79.20
MemGenSFT 85.82 77.22 54.65 66.15 40.35 43.23 91.25 83.30
MemGenGRPO 90.60 80.65 62.30 76.16 75.56 40.24 93.20 88.24
ActiveMemSFT 90.73 82.31 66.27 79.37 77.84 47.83 93.92 89.38
ActiveMemGRPO 95.57 87.46 73.20 83.42 84.39 54.49 94.81 92.76
not rely on a specific optimization algorithm, so we imple-
ment two variants:ActiveMemSFT, trained with supervised
fine-tuningoninteractiontrajectories,andActiveMem GRPO,
further optimized using reinforcement learning with task
rewards. Comprehensive details on these variants, training
setups, and hyperparameter configurations are provided in
Appendix.
4.2 Main Results
To comprehensively validate the effectiveness of our ap-
proach, we evaluate ActiveMem across a diverse suite of
benchmarks.AsshowninTable1,ActiveMemachievessub-
stantialperformancegainsacrossalldomains,demonstrating
that our method is highly effective not only in long-horizon
interactive environments but also yields state-of-the-art re-
sults on static and short-horizon reasoning tasks. It success-
fully overcomes the limitations of passive retrieval meth-
ods (which bottleneck on reasoning tasks) and static para-
metric finetuning (which struggle with dynamic knowledge
application). By introducing a decoupled memory policy
(πϕ) trained via GRPO, ActiveMem dynamically manages
a latent memory tree—handling task anchoring, branching,
and utility-driven pruning—while keeping the LLM back-
bone frozen. Beyond absolute performance gains, Active-
Mem demonstrates a remarkable cross-scale leapfrogging
capability. By structuring context management through hi-
erarchical memory trees, our framework effectively com-
pensates for the limited internalized knowledge capacity of
smaller models.
4.3 Generalization Experiments
To rigorously assess cross-domain transferability, we train
models on a single source dataset and evaluate them across
structurally divergent environments, such as ScienceWorld
andFEVER(Figure2).Standardbaselines(e.g.,SFT,Mem-
oryBank) exhibit severe domain overfitting, as they are in-
herently bottlenecked by surface-level semantic matching
and tend to memorize dataset-specific interaction trajecto-
ries. Even advanced generative memory methods like Mem-
Gen yield only marginal gains when faced with signifi-
cant domain shifts. In contrast, ActiveMem intrinsically by-
passes this limitation. By abstracting raw trajectories into
dependency-aware latent nodes, our framework captures the
underlying procedural logic rather than domain-specific vo-
cabulary.Whethertransferringfromthealgorithmiclogicof
KodCode to the deductive reasoning of MATH, or transi-

Table2:AblationStudyonQwen3-8B.WeevaluatethecontributionofeachmajorcomponentinActiveMem.Allvaluesdenote
task performance (%).
Method ALFWorld TriviaQA PopQA KodCode BigCodeBench GPQA GSM8K MATH
ActiveMemGRPO 95.57 87.46 73.20 83.42 84.39 54.49 94.81 92.76
w/o Tree Action Head 89.88 81.93 67.80 80.95 79.46 48.53 86.41 89.83
w/o Merge/Delete 93.11 84.24 71.24 81.54 83.64 52.13 88.02 87.11
w/o Hierarchical Advantage 90.74 83.25 69.93 82.46 81.35 50.98 86.74 90.86
w/o Latent Injection 88.96 81.67 66.81 81.92 78.44 51.76 85.98 87.35
w/o HLMT 83.25 78.64 58.92 73.41 69.88 44.53 82.47 86.39
Table 3: Quantitative comparison of models on multi-objective, multi-hop QA tasks. Arrows indicate the optimal direction for
each metric. Underlined entries denote catastrophic model collapse (i.e., extremely low performance). Variants marked with
(truncate)adopt ActiveMem’s prompt and rollout pipeline with context truncation. Variants labeled with(A-MEM)employ the
prompt, rollout pipeline, and the external memory module from ActiveMem (Xu et al. 2026).ActiveMem-QArefers to our
proposed ActiveMem optimized specifically on the 2-objective QA.
Model 2-Objective 8-Objective 16-Objective
EM↑F1↑Peak (×10 2)↓Time (s)↓EM↑F1↑Peak (×10 2)↓Time (s)↓EM↑F1↑Peak (×10 2)↓Time (s)↓
Qwen2.5-14B-Inst 0.732 0.902 15.6±0.19 5.49±0.16 1.55 1.87 44.7±0.37 16.2±0.27 0.567 0.703 38.4±0.71 29.7±0.75
Qwen2.5-7B-Inst 0.268 0.366 19.6±0.33 4.60±0.08 0.87 1.10 49.5±0.40 13.9±0.18 0.165 0.213 43.3±0.62 15.5±0.23
Qwen2.5-7B-Inst (A-MEM) 0.286 0.371 14.1±0.10 24.6±0.51 1.13 1.43 18.6±0.10 53.7±1.26 0.730 0.961 18.8±0.14 91.2±2.44
Qwen2.5-7B-Inst (truncate) 0.262 0.336 8.28±0.06 5.89±0.16 0.97 1.23 11.8±0.10 11.9±0.20 0.396 0.497 13.3±0.16 22.1±0.60
Search-R1 0.452 0.531 13.0±0.08 4.09±0.23 0.064 0.08 24.7±0.19 4.25±0.16 0.009 0.011 20.9±0.03 4.75±0.18
DeepResearcher 0.536 0.650 22.0±0.434.01±0.070.73 0.90 51.8±0.35 11.3±0.14 0.071 0.106 48.9±0.66 15.8±0.19
MEM1-QA 0.709 0.8386.40±0.026.49±0.07 1.87 2.318.01±0.06 8.68±0.121.97 2.3910.4±0.09 8.70±0.12
ActiveMem-QA0.753 0.9256.68±0.04 6.84±0.052.39 2.848.83±0.04 9.13±0.102.83 3.5811.5±0.04 9.32±0.08
0 10 20 30 40 50 60 70 80
ALFWorld
TriviaQA
ScienceWorld
FEVER
Trained on ALFWorld
0 10 20 30 40 50 60 70 80
Trained on TriviaQA
Vanilla SFT MemoryBank MemGen ActiveMem
Figure 2: Generalization study of ActiveMem. We train Ac-
tiveMemSFTonasingledataset(eitherALFWorldorTrivi-
aQA) and evaluate it across four diverse datasets: TriviaQA,
ALFWorld, ScienceWorld, and FEVER.
tioningfromembodiednavigationinALFWorldtoevidence
retrieval in FEVER, ActiveMem seamlessly generalizes its
learned topological operations (e.g., temporal branching,
utility-driven pruning). This robust transferability demon-
stratesthatourdecoupledmemorycontroller(π ϕ),optimized
via GRPO, successfully internalizes a universal cognitive
strategy for long-horizon context management, effectively
preventing catastrophic performance degradation in unseen
environments (Figure 5).
4.4 Ablation Study
We conduct ablation experiments on the Qwen3-8B back-
bone to evaluate the individual contribution of each core
component in ActiveMem. As shown in Table 2, remov-
ing any module consistently degrades performance across
0 10 20 30 40 50 60 70
GSM8K
KodCode
GPQA
MATH
Trained on GSM8K
0 10 20 30 40 50 60 70
GSM8K
KodCode
GPQA
MATH
Trained on KodCode
Vanilla SFT MemoryBank MemGen ActiveMem
Figure 3: The generalization study. We train ActiveMem on
GSM8K or KodCode and evaluate it on all four datasets.
all domains. This validates that our gains are not driven by
a single heuristic, but rather by the deeply integrated syn-
ergy of hierarchical memory organization, adaptive topol-
ogyevolution,latentreasoningmodulation,andhierarchical
reinforcement optimization. Among all variants, removing
the Hierarchical Latent Memory Tree (w/o HLMT) triggers
the most catastrophic performance collapse across nearly all
benchmarks, with GPQA plunging from 54.49% to 44.53%
and BigCodeBench from 84.39% to 69.88%. This confirms
that hierarchical structural organization is the indispensable
foundation of ActiveMem, enabling scalable retrieval and
progressive abstraction that fundamentally avoids the con-
textfragmentationinherentinflatmemorystorage.Disabling
latent memory injection (w/o Latent Injection) also signifi-

1 2 3 4 6 8 16
Number of Objectives
0
1000
2000
3000
4000
5000Peak Token Count
0.0
0.5
1.0
1.5
2.0
Exact Match Count
ActiveMem (Exact Match)
Qwen2.5-7B-Instruct (A-Mem) (Exact Match)
Qwen2.5-7B-Instruct (Exact Match)
Qwen2.5-14B-Instruct (Exact Match)
Search-R1-7B (Exact Match)
DeepResearcher-7B (Exact Match)
MEM1-7B (Exact Match)
ActiveMem (Peak T oken)
Qwen2.5-7B-Instruct (A-Mem) (Peak T oken)
Qwen2.5-7B-Instruct (Peak T oken)
Qwen2.5-14B-Instruct (Peak T oken)
Search-R1-7B (Peak T oken)
DeepResearcher-7B (Peak T oken)
MEM1-7B (Peak T oken)
Figure4:Scalingtrajectoriesoftaskperformanceandmemoryefficiencyasafunctionoftaskcomplexity(numberofobjectives).
ActiveMem (trained on the 2-objective QA dataset) consistently outperforms all baselines while maintaining a nearly constant
memory footprint. Note that the apparent plateau in peak token usage for baseline models at 16 objectives is an artifact of
catastrophic model collapse (e.g., premature trajectory termination), rather than an indication of sustained efficiency.
cantlyimpairsreasoningcapabilities.Thisdemonstratesthat
merely selecting the correct historical path is insufficient;
the retrieved memories must continuously and fundamen-
tally steer the model’s internal hidden-state dynamics to ef-
fectivelyinfluenceautoregressivedecoding.Similarly,omit-
tingthehierarchicaladvantagemechanism(w/oHierarchical
Advantage)consistentlyharmsperformance,echoingourhy-
pothesis that sparse, trajectory-level final rewards alone are
inadequate for stable memory evolution. Hierarchical credit
assignment is crucial for providing fine-grained optimiza-
tion signals to intermediate tree nodes. Finally, restricting
the model’s ability to edit memory topology (w/o Tree Ac-
tionHead)leadstosubstantialdegradation,indicatingthata
statichierarchycannotcontinuallyadapttounfoldingreason-
ingpatterns.Removingonlythemergeanddeleteoperations
(w/o Merge/Delete) results in relatively smaller but strictly
consistent declines. This is theoretically sound, as these op-
erations primarily target long-term computational efficiency
rather than immediate reasoning execution. Nonetheless,
their absence still hurts overall accuracy, underscoring that
proactive redundancy consolidation and low-utility pruning
areessentialforpreventingnoiseaccumulationoverextended
interaction horizons.
4.5 Efficiency Analysis
ActiveMem excels at managing long-horizon interactions
through structured memory evolution. To evaluate this ca-
pability, we extend QA into multi-objective tasks that re-
quire progressively longer reasoning trajectories and sus-
tained memory consistency. As shown in Table 7, Active-
Mem surpasses 7B baselines on 2-objective tasks while
using substantially fewer tokens and lower inference cost.
Moreimportantly,itsadvantagegrowsconsistentlywithtask
complexity.Across3–16objectives(Figure4),conventional
methods exhibit near-linear growth in Peak Token Usage,
whereas ActiveMem maintains a lower memory footprint,
demonstratingsubstantiallybetterscalabilityunderextended
reasoning horizons. This efficiency further translates into
strong cross-scale generalization: although initially trailing
the larger Qwen2.5-14B-Instruct on shorter tasks, Active-
Mem becomes increasingly robust as task horizons expand
and eventually surpasses the 14B model. On the challeng-
ing 16-objective benchmark, ActiveMem achieves superior
performance while using only 27.1% of the peak tokens and
29.3%oftheinferencetimeofthe14Bbaseline,substantially
reducingbothGPUmemoryconsumptionandcomputational
overhead for complex multi-step reasoning.
5 Conclusion
We propose ActiveMem, a hierarchical memory framework
that addresses context fragmentation and cross-task interfer-
ence, in long-horizon LLM agents by organizing interaction
histories into dynamically evolving latent memory trees. In-
steadofrelyingonflatmemorybuffers,ActiveMememploys
anRL-optimizeddecoupledcontrollertojointlylearnhierar-
chicalmemoryorganization,topology-awareretrieval,latent
reasoninginjection,andadaptivememorymaintenance.Ex-
tensive experiments demonstrate consistent state-of-the-art
performancewithsubstantiallyimprovedmemoryefficiency.

References
Anthropic. 2025. Introducing Claude 4.
Chen, Z.; Liu, K.; Wang, Q.; Zhang, W.; Liu, J.; Lin, D.;
Chen, K.; and Zhao, F. 2024. Agent-flan: Designing data
and methods of effective agent tuning for large language
models. InFindings of the Association for Computational
Linguistics: ACL 2024, 9354–9366.
Chu, Z.; Wang, X.; Hong, J.; Fan, H.; Huang, Y.; Yang,
Y.; Xu, G.; Zhao, C.; Xiang, C.; Hu, S.; et al. 2026. Red-
searcher: A scalable and cost-efficient framework for long-
horizon search agents.arXiv preprint arXiv:2602.14234.
Cobbe, K.; Kosaraju, V.; Bavarian, M.; Chen, M.; Jun, H.;
Kaiser, L.; Plappert, M.; Tworek, J.; Hilton, J.; Nakano, R.;
et al. 2021. Training verifiers to solve math word problems.
arXiv preprint arXiv:2110.14168.
Douze, M.; Guzhva, A.; Deng, C.; Johnson, J.; Szilvasy, G.;
Mazaré,P.-E.;Lomeli,M.;Hosseini,L.;andJégou,H.2025.
The faiss library.IEEE Transactions on Big Data.
Erdogan,L.E.;Lee,N.;Kim,S.;Moon,S.;Furuta,H.;Anu-
manchipalli, G.; Keutzer, K.; and Gholami, A. 2026. Plan-
and-Act: Improving Planning of Agents for Long-Horizon
Tasks. InForty-second International Conference on Ma-
chine Learning.
Gao, J.; Fu, W.; Xie, M.; Xu, S.; He, C.; Mei, Z.; Zhu,
B.; and Wu, Y. 2025. Beyond ten turns: Unlocking long-
horizon agentic search with large-scale asynchronous rl.
arXiv preprint arXiv:2508.07976.
Guo, D.; Yang, D.; Zhang, H.; Song, J.; Wang, P.; Zhu, Q.;
Xu, R.; Zhang, R.; Ma, S.; Bi, X.; et al. 2025. Deepseek-r1:
Incentivizing reasoning capability in llms via reinforcement
learning.arXiv preprint arXiv:2501.12948.
Hendrycks, D.; Burns, C.; Kadavath, S.; Arora, A.; Basart,
S.; Tang, E.; Song, D.; and Steinhardt, J. 2021. Measuring
mathematical problem solving with the math dataset.arXiv
preprint arXiv:2103.03874.
Hu,J.;Liu,J.K.;Xu,H.;andShen,W.2025a. Reinforce++:
An efficient rlhf algorithm with robustness to both prompt
and reward models.arXiv preprint arXiv:2501.03262, 1(3):
5.
Hu, M.; Chen, T.; Chen, Q.; Mu, Y.; Shao, W.; and Luo,
P. 2025b. Hiagent: Hierarchical working memory manage-
mentforsolvinglong-horizonagenttaskswithlargelanguage
model. InProceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long
Papers), 32779–32798.
HuggingFace. 2025. SmolLM3: Smol, Multilingual, Long-
Context Reasoner.
Jain, N.; Gu, A.; Li, W.-D.; Yan, F.; Zhang, T.; Wang,
S.; Solar-Lezama, A.; Sen, K.; and Stoica, I. 2025. Live-
codebench: Holistic and contamination free evaluation of
largelanguagemodelsforcode. InInternationalConference
on Learning Representations, volume 2025, 58791–58831.
Jin, B.; Zeng, H.; Yue, Z.; Yoon, J.; Arik, S.; Wang, D.;
Zamani, H.; and Han, J. 2025. Search-r1: Training llms
to reason and leverage search engines with reinforcement
learning.arXiv preprint arXiv:2503.09516.
Joshi, M.; Choi, E.; Weld, D. S.; and Zettlemoyer, L. 2017.
Triviaqa:Alargescaledistantlysupervisedchallengedataset
for reading comprehension. InProceedings of the 55th An-
nual Meeting of the Association for Computational Linguis-
tics (Volume 1: Long Papers), 1601–1611.
Karpukhin,V.;Oguz,B.;Min,S.;Lewis,P.;Wu,L.;Edunov,
S.; Chen, D.; and Yih, W.-t. 2020. Dense passage retrieval
for open-domain question answering. InProceedings of the
2020 conference on empirical methods in natural language
processing (EMNLP), 6769–6781.
Kwon, W.; Li, Z.; Zhuang, S.; Sheng, Y.; Zheng, L.; Yu,
C.H.;Gonzalez,J.;Zhang,H.;andStoica,I.2023. Efficient
memorymanagementforlargelanguagemodelservingwith
pagedattention. InProceedings of the 29th symposium on
operating systems principles, 611–626.
Li, K.; Zhang, Z.; Yin, H.; Zhang, L.; Ou, L.; Wu, J.; Yin,
W.; Li, B.; Tao, Z.; Wang, X.; et al. 2025. Websailor: Navi-
gating super-human reasoning for web agent.arXiv preprint
arXiv:2507.02592.
Li,X.;Jin,J.;Dong,G.;Qian,H.;Wu,Y.;Wen,J.-R.;Zhu,Y.;
andDou,Z.2026. Webthinker:Empoweringlargereasoning
models with deep research capability.Advances in Neural
Information Processing Systems, 38: 120091–120131.
Liu, B.; Li, X.; Zhang, J.; Wang, J.; He, T.; Hong, S.; Liu,
H.; Zhang, S.; Song, K.; Zhu, K.; et al. 2025a. Advances
and challenges in foundation agents: From brain-inspired
intelligence to evolutionary, collaborative, and safe systems.
arXiv preprint arXiv:2504.01990.
Liu, J.; Li, Y.; Zhang, C.; Li, J.; Chen, A.; Ji, K.; Cheng,
W.; Wu, Z.; Du, C.; Xu, Q.; et al. 2025b. Webexplorer:
Explore and evolve for training long-horizon web agents.
arXiv preprint arXiv:2509.06501.
Liu,L.;Pfeiffer,J.;Wu,J.;Xie,J.;andSzlam,A.2024.Delib-
erationinlatentspaceviadifferentiablecacheaugmentation.
arXiv preprint arXiv:2412.17747.
Lu, M.; Sun, W.; Du, W.; Ling, Z.; Yao, X.; Liu, K.; and
Chen, J. 2025. Scaling llm multi-turn rl with end-to-end
summarization-based context management.arXiv preprint
arXiv:2510.06727.
Luo,J.;Zhang,W.;Yuan,Y.;Zhao,Y.;Yang,J.;Gu,Y.;Wu,
B.;Chen,B.;Qiao,Z.;Long,Q.;etal.2025. Largelanguage
model agent: A survey on methodology, applications and
challenges.arXiv preprint arXiv:2503.21460.
Mallen, A.; Asai, A.; Zhong, V.; Das, R.; Khashabi, D.;
andHajishirzi,H.2023. Whennottotrustlanguagemodels:
Investigatingeffectivenessofparametricandnon-parametric
memories. InProceedings of the 61st annual meeting of the
association for computational linguistics (volume 1: Long
papers), 9802–9822.
Mialon,G.;Fourrier,C.;Wolf,T.;LeCun,Y.;andScialom,T.
2024. Gaia: a benchmark for general ai assistants. InInter-
national Conference on Learning Representations, volume
2024, 9025–9049.
OpenAI. 2025a. Deep Research System Card.
OpenAI. 2025b. Introducing OpenAI o3 and o4-mini.

Packer, C.; Fang, V.; Patil, S.; Lin, K.; Wooders, S.; and
Gonzalez, J. 2023. MemGPT: towards LLMs as operating
systems.
Rein, D.; Hou, B. L.; Stickland, A. C.; Petty, J.; Pang, R. Y.;
Dirani, J.; Michael, J.; and Bowman, S. R. 2023. Gpqa: A
graduate-levelgoogle-proofq&abenchmark.arXivpreprint
arXiv:2311.12022.
Serper.2025.SerperAPI:FastandAffordableGoogleSearch
API. https://serper.dev/. Accessed: 2025-05-15.
Sheng,G.;Zhang,C.;Ye,Z.;Wu,X.;Zhang,W.;Zhang,R.;
Peng, Y.; Lin, H.; and Wu, C. 2025. Hybridflow: A flexible
andefficientrlhfframework. InProceedingsoftheTwentieth
European Conference on Computer Systems, 1279–1297.
Shi, W.; Tan, H.; Kuang, C.; Li, X.; Ren, X.; Zhang, C.;
Chen, H.; Wang, Y.; Shang, L.; Yu, F.; et al. 2025. Pangu
deepdiver: Adaptive search intensity scaling via open-web
reinforcement learning.arXiv e-prints, arXiv–2505.
Shridhar, M.; Yuan, X.; Côté, M.-A.; Bisk, Y.; Trischler, A.;
and Hausknecht, M. 2020. Alfworld: Aligning text and em-
bodiedenvironmentsforinteractivelearning.arXivpreprint
arXiv:2010.03768.
Team, D. ???? Introducing deepseek-v3. 1: our first step
towardtheagentera!,2025.URLhttps://api-docs.deepseek.
com/news/news250821.
Team, K.; Bai, Y.; Bao, Y.; Charles, Y.; Chen, C.; Chen, G.;
Chen,H.;Chen,H.;Chen,J.;Chen,N.;etal.2025a.Kimik2:
Openagenticintelligence.arXivpreprintarXiv:2507.20534.
Team, M. A.; et al. 2025b. Mirothinker: An open-source
agentic model series trained for deep research and complex,
long-horizon problem solving.
Team, O. 2025. Openpangu deepdiver-v2: Multi-
agent learning for deep information seeking, 2025.
URL https://ai. gitcode. com/ascend-tribe/openPangu-
Embedded-7B-DeepDiver.
Wang, G.; Xie, Y.; Jiang, Y.; Mandlekar, A.; Xiao, C.; Zhu,
Y.; Fan, L.; and Anandkumar, A. 2023. Voyager: An open-
ended embodied agent with large language models.arXiv
preprint arXiv:2305.16291.
Wang,J.;Zhu,L.;Weng,T.;Wu,S.-L.;Tan,H.;Chen,J.;Tao,
C.;Bai,H.;Hou,L.;Shang,L.;etal.2026. GRPO-VPS:En-
hancingGroup RelativePolicy OptimizationwithVerifiable
ProcessSupervisionforEffectiveReasoning.arXivpreprint
arXiv:2604.20659.
Wang, L.; Yang, N.; Huang, X.; Jiao, B.; Yang, L.; Jiang,
D.; Majumder, R.; and Wei, F. 2022. Text embeddings by
weakly-supervised contrastive pre-training.arXiv preprint
arXiv:2212.03533.
Wang,Z.Z.;Mao,J.;Fried,D.;andNeubig,G.2024. Agent
workflow memory.arXiv preprint arXiv:2409.07429.
Wei, J.; Sun, Z.; Papay, S.; McKinney, S.; Han, J.; Fulford,
I.; Chung, H. W.; Passos, A. T.; Fedus, W.; and Glaese, A.
2025. Browsecomp:Asimpleyetchallengingbenchmarkfor
browsing agents.arXiv preprint arXiv:2504.12516.
Wei,J.;Wang,X.;Schuurmans,D.;Bosma,M.;Xia,F.;Chi,
E.;Le,Q.V.;Zhou,D.;etal.2022.Chain-of-thoughtprompt-
ing elicits reasoning in large language models.Advances in
neural information processing systems, 35: 24824–24837.
Williams,R.J.1992.Simplestatisticalgradient-followingal-
gorithms for connectionist reinforcement learning.Machine
learning, 8(3): 229–256.
Wong, R.; Wang, J.; Zhao, J.; Chen, L.; Gao, Y.; Zhang,
L.; Zhou, X.; Wang, Z.; Xiang, K.; Zhang, G.; et al.
2025. Widesearch: Benchmarking agentic broad info-
seeking.arXiv preprint arXiv:2508.07999.
Wu, J.; Li, B.; Fang, R.; Yin, W.; Zhang, L.; Wang, Z.;
Tao, Z.; Zhang, D.-C.; Xi, Z.; Tang, R.; et al. 2026a. Web-
dancer: Towards autonomous information seeking agency.
Advances in Neural Information Processing Systems, 38:
120957–120985.
Wu, J.; Zhu, J.; Liu, Y.; Xu, M.; and Jin, Y. 2025. Agentic
reasoning: A streamlined framework for enhancing llm rea-
soningwithagentictools. InProceedingsofthe63rdAnnual
Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), 28489–28503.
Wu, S.-L.; Du, L.; Yang, J.-Q.; Wang, Y.-A.; Zhan, D.-C.;
Zhao, S.; and Sun, Z.-X. 2023. Re-sort: Removing spurious
correlation in multilevel interaction for ctr prediction.arXiv
preprint arXiv:2309.14891.
Wu, S.-L.; Du, Z.; Gan, W.; Wang, J.; and Wang, X. 2026b.
From ID to LLM: Rethinking Representation Learning for
Recommendation. InProceedings of the 64th Annual Meet-
ingoftheAssociationforComputationalLinguistics(Volume
1: Long Papers), 3893–3905.
Wu,S.-L.;Du,Z.;Jia,Q.;andDong,Z.2026c. REACTION:
Parameter-Efficient Learning for Recommendation. InPro-
ceedings of the AAAI Conference on Artificial Intelligence,
volume 40, 15977–15985.
Wu, S.-L.; Du, Z.; Wang, X.; and Wang, J. 2026d. CaPEdit:
Capability-PreservingLifelongKnowledgeEditingForLan-
guage Models. InFindings of the Association for Computa-
tional Linguistics: ACL 2026, 15710–15752.
Wu, S.-L.; Gan, W.; Du, Z.; Wang, X.; and Wang, J.
2026e. FineSID: Scalable and Efficient Semantic Identifier
Learning for Generative Recommendation.arXiv preprint
arXiv:2609.36670.
Wu, S.-L.; Wang, J.; Du, Z.; Gan, W.; and Liu, W. 2026f.
CodeSkill: Latent Skill Abstraction for Long-Horizon Code
Agents.arXiv preprint arXiv:2609.33243.
Wu, S.-L.; Wang, X.; Du, Z.; Gan, W.; and Wang, J.
2026g. FairDiff: Mitigating the Self-Reinforcing Matthew
Effect in Diffusion Recommender Models.arXiv preprint
arXiv:2609.36671.
Xi,Z.;Chen,W.;Guo,X.;He,W.;Ding,Y.;Hong,B.;Zhang,
M.; Wang, J.; Jin, S.; Zhou, E.; et al. 2025a. The rise and
potential of large language model based agents: A survey.
Science China Information Sciences, 68(2): 121101.
Xi, Z.; Huang, J.; Liao, C.; Huang, B.; Guo, H.; Liu,
J.; Zheng, R.; Ye, J.; Zhang, J.; Chen, W.; et al. 2025b.
Agentgym-rl: Training llm agents for long-horizon decision
making through multi-turn reinforcement learning.arXiv
preprint arXiv:2509.08755.
Xu, R.; and Yan, Y. 2026. Agent skills for large language
models: Architecture, acquisition, security, and the path for-
ward.arXiv preprint arXiv:2602.12430.

Xu, W.; Liang, Z.; Mei, K.; Gao, H.; Tan, J.; and Zhang, Y.
2026. A-mem:Agenticmemoryforllmagents.Advancesin
Neural Information Processing Systems, 38: 17577–17604.
Xu, Y.; Guo, X.; Zeng, Z.; and Miao, C. 2025a. Softcot++:
Test-timescalingwithsoftchain-of-thoughtreasoning.arXiv
preprint arXiv:2505.11484.
Xu,Z.;Liu,Y.;Yin,Y.;Zhou,M.;andPoovendran,R.2025b.
Kodcode: A diverse, challenging, and verifiable synthetic
dataset for coding. InFindings of the Association for Com-
putational Linguistics: ACL 2025, 6980–7008.
Yang,A.;Li,A.;Yang,B.;Zhang,B.;Hui,B.;Zheng,B.;Yu,
B.;Gao,C.;Huang,C.;Lv,C.;etal.2025. Qwen3technical
report.arXiv preprint arXiv:2505.09388.
Yang, A.; Yang, B.; Zhang, B.; Hui, B.; Zheng, B.; Yu, B.;
Li, C.; Liu, D.; Huang, F.; Wei, H.; et al. 2024a. Qwen2.5
Technical Report. InarXiv preprint arXiv:2412.15115.
Yao, S.; Chen, H.; Yang, J.; and Narasimhan, K. 2022a.
Webshop: Towards scalable real-world web interaction with
grounded language agents.Advances in Neural Information
Processing Systems, 35: 20744–20757.
Yao,S.;Zhao,J.;Yu,D.;Shafran,I.;Narasimhan,K.R.;and
Cao, Y. 2022b. ReAct: Synergizing Reasoning and Acting
in Language Models. InNeurIPS 2022 Foundation Models
for Decision Making Workshop.
Ye, R.; Zhang, Z.; Li, K.; Yin, H.; Tao, Z.; Zhao, Y.; Su, L.;
Zhang,L.;Qiao,Z.;Wang,X.;etal.2026. AgentFold:Long-
HorizonWebAgentswithProactiveContextFolding. InThe
FourteenthInternationalConferenceonLearningRepresen-
tations.
Zeng, A.; Lv, X.; Zheng, Q.; Hou, Z.; Chen, B.; Xie, C.;
Wang, C.; Yin, D.; Zeng, H.; Zhang, J.; et al. 2025. Glm-
4.5:Agentic,reasoning,andcoding(arc)foundationmodels.
arXiv preprint arXiv:2508.06471.
Zhang, G.; Fu, M.; and Yan, S. 2026. Memgen: Weaving
generative latent memory for self-evolving agents.
Zhang,J.;Zhu,Y.;Sun,M.;Luo,Y.;Qiao,S.;Du,L.;Zheng,
D.; Chen, H.; and Zhang, N. 2025a. Lightthinker: Thinking
step-by-step compression. InProceedings of the 2025 Con-
ferenceonEmpiricalMethodsinNaturalLanguageProcess-
ing, 13318–13339.
Zhang,W.;Li,Y.;Bei,Y.;Luo,J.;Wan,G.;Yang,L.;Xie,C.;
Yang, Y.; Huang, W.-C.; Miao, C.; et al. 2025b. From web
search towards agentic deep research: Incentivizing search
with reasoning agents.arXiv preprint arXiv:2506.18959.
Zhao,A.;Huang,D.;Xu,Q.;Lin,M.;Liu,Y.-J.;andHuang,
G.2024. Expel:Llmagentsareexperientiallearners. InPro-
ceedings of the AAAI Conference on Artificial Intelligence,
volume 38, 19632–19642.
Zhao, Y.; Huang, J.; Hu, J.; Wang, X.; Mao, Y.; Zhang, D.;
Jiang, Z.; Wu, Z.; Ai, B.; Wang, A.; et al. 2025. Swift: a
scalable lightweight infrastructure for fine-tuning. InPro-
ceedings of the AAAI Conference on Artificial Intelligence,
volume 39, 29733–29735.
Zheng, T.; Tam, K. K.-W.; Nguyen, N. H.-N. K.; Xu, B.;
Wang, Z.; Cheng, J.; Tsang, H. T.; Wang, W.; Bai, J.; Fang,
T.; et al. 2025a. Newtonbench: Benchmarking generaliz-
able scientific law discovery in llm agents.arXiv preprint
arXiv:2510.07172.
Zheng,Y.;Fu,D.;Hu,X.;Cai,X.;Ye,L.;Lu,P.;andLiu,P.
2025b. Deepresearcher:Scalingdeepresearchviareinforce-
ment learning in real-world environments. InProceedings
of the 2025 Conference on Empirical Methods in Natural
Language Processing, 414–431.
Zhong, W.; Guo, L.; Gao, Q.; Ye, H.; and Wang, Y. 2024.
Memorybank: Enhancing large language models with long-
term memory. InProceedings of the AAAI conference on
artificial intelligence, volume 38, 19724–19731.
Zhou, P.; Leon, B.; Ying, X.; Zhang, C.; Shao, Y.;
Ye, Q.; Chong, D.; Jin, Z.; Xie, C.; Cao, M.; et al.
2025a. Browsecomp-zh: Benchmarking web browsing abil-
ity of large language models in chinese.arXiv preprint
arXiv:2504.19314.
Zhou, Z.; Qu, A.; Wu, Z.; Kim, S.; Prakash, A.; Rus, D.;
Zhao, J.; Low, B. K. H.; and Liang, P. P. 2025b. Mem1:
Learning to synergize memory and reasoning for efficient
long-horizon agents.arXiv preprint arXiv:2506.15841.
6 Details
6.1 Computing Resources and Training Details
All training procedures for ActiveMem are executed on a
computing cluster equipped with four NVIDIA H100 or
H200 GPUs. We implement our reinforcement learning
(RL) pipeline utilizing the veRL framework (Sheng et al.
2025),whileSupervisedFine-Tuning(SFT)isconductedvia
Swift (Zhao et al. 2025). During RL optimization, both the
rolloutdatabatchsizeandthemini-batchsizeareconfigured
to 64. We employ learning rates of10−6 for the actor net-
work and10−5 for the critic network, incorporating a linear
warmup schedule over the initial 50 steps. The generation
temperature is fixed at 1.0 during training to facilitate tra-
jectory exploration, and drastically reduced to 0.01 during
evaluation to ensure near-deterministic decoding. All evalu-
ationsareperformedonasingleNVIDIAH200GPU,where
modelsaredeployedasanAPIservicepoweredbythevLLM
engine (Kwon et al. 2023), explicitly leveraging automatic
prefix caching to maximize inference throughput.
6.2 RAG Configuration
For the local Retrieval-Augmented Generation (RAG)
pipeline, we deploy Faiss-GPU (Douze et al. 2025) cou-
pled with an E5-Base embedding model (Wang et al. 2022)
to index a standard Wikipedia 2018 dump (Karpukhin et al.
2020).Toensureequitablecomparisonswithbaselinemeth-
ods,theretrievaldepthisstrictlylimitedtothetop-3passages
perquery.Fordynamiconlinesearches,weleveragetheSer-
per API (Serper 2025) to execute Google queries, returning
structured metadata including titles, URLs, and contextual
snippets. The agent is consistently supplied with the top-10
searchresultsasexternalcontext.Notably,tostrictlyevaluate
snippet-level reasoning and filter out noisy HTML parsing,
weintentionallyrestricttheagent’sobservationspacetothese
searchresults,omittingtheretrievaloffullwebpagecontent.

6.3 Prompt
Prompt 6.1: Multi-Objective Task (QA)
You will answer multiple complex questions using itera-
tive reasoning, summarization, and web search.
Ateachstep,youwillseethequestions,acumulativesum-
mary of relevant information, the current search query,
and search results (except in the first step, where only the
questions are provided).
Your task is to:
1. Perform reasoning and update a cumulative, concise
summary within <think> ... </think>. This acts as persis-
tent memory and must include all essential information
from previous <think> and <information> tags.
2. Then choose one of the following actions:
-Ifanyquestionremainsunanswered,issueasinglequery
for one question inside <search> ... </search>. The query
shouldconsistofkeywordsorashortphrase.Onlysearch
one question at a time.
- If all questions are answered, provide the final an-
swers—separated by semicolons—within <answer> an-
swer1; answer2; ... </answer>. The answers must be con-
cise,containonlyessentialwords,andavoidanyexplana-
tions.
Important:
- Always follow this structure after <information> or
the initial questions: <think> ... </think><search> ...
</search> or <think> ... </think><answer> ... </answer>.
- Do not search multiple queries or questions simultane-
ously. Answer the following questions:[QUESTIONS]
Prompt 6.2: Single-Objective Task (QA)
Youwillansweracomplexquestionthroughiterativerea-
soning, summarization, and web searches.
At each step, you can see the question, previous sum-
mary in <think> ... </think>, search query in <search> ...
</search>,andthereturnedinformationin<information>
... </information> (except the first step where you will be
given only the question). Then, you should:
1. Conduct reasoning, and then update a concise, cumu-
lativesummarywithessentialinformationinside<think>
</think>. This is your persistent memory and should in-
clude all important information from previous <think>
</think> and <information> </information> (i.e. infor-
mationandanswersalreadyfoundforquestions).2.Then
choose one:
-Issueaquery(i.e.,keywords/phrasesforsearch)inside
<search> </search> (you may search repeatedly until the
answerisclear).Thisquerywillbeusedtoconductsearch
andreturntheresultsin<information>results</informa-
tion>
- Provide the final concise answer (no explanations) if no
additional information is needed inside <answer> </an-
swer>. The answer should be concise and only contain
the words necessary to answer the question.
After <information> </information> (or question at
the beginning), you should always follow the order:
<think> ... </think><search> ... </search> or <think> ...
</think><answer>...</answer>.Question:[QUESTION]
Prompt 6.3: Single-Objective Task (WebShop)
You are browsing an online shop. Your goal is to find
a product that matches the given description. You will
interact with the site step-by-step. Each step gives you a
<state>...</state> representing the current webpage. You
mustdecidewhatactiontotakenextuntilyouidentifythe
correct product.
Available actions (shown in the <state> tag) depend on
the page:
- On the search page: search[<keywords>]
-Onsearchresultpages:click[<itemurl>]toviewaprod-
uct, or click[next >] to go to the next results page
- On product pages: click[description], click[features],
click[color], click[size], click[buy now]
- To return to search: click[back to search]
Example goal: "Find a gingko light and 20x20 pil-
low cover that is hand painted." Example first action:
<answer>search[gingko light 20x20 pillow cover hand
painted]</answer> Only respond with valid actions for-
matted as: search[...], click[...], etc.
After you navigate and find the product that best fits the
user goal, you should click[buy now] to buy the product
attheproductpagewhenthebuynowbuttonisavailable.
Product Description: [PRODUCT DESCRIPTION]
6.4 WebShop Training Details
To adapt ActiveMem for the WebShop environment, we
strictly maintain the core rollout pipeline and policy opti-

mization mechanisms utilized in the QA tasks. However, we
introducetwonecessarytask-specificmodifications.First,we
employ a domain-tailored prompt template (see Prompt 6.3)
that preserves the fundamental principles of memory con-
solidation while seamlessly integrating WebShop-specific
navigation instructions. Second, unlike the QA setup which
reliesonExactMatch(EM)scores,wedirectlyleverageWeb-
Shop’s native, state-dependent reward function to derive the
reinforcement signal during training. For dataset partition-
ing, we adhere strictly to the standard protocol established
in the original benchmark (Yao et al. 2022a): the first 1,000
instances are reserved for testing, the subsequent 500 for
validation, and the remainder constitute the training set.
6.5 Implementation Details
6.6 Trajectory Construction Across Benchmarks
Although several evaluation benchmarks (e.g., TriviaQA,
PopQA, GSM8K, GPQA, MATH, KodCode, and Big-
CodeBench) are not interactive environments, ActiveMem
adopts a unified trajectory formulation for both agentic and
reasoning tasks. Specifically, each sample is treated as a
sequential reasoning process, where autoregressive decod-
ing naturally produces a trajectory of intermediate reason-
ing states. At each decoding step, the current hidden repre-
sentation is regarded as the execution state, and the gener-
ated reasoning history forms the trajectory prefix used for
memoryretrievalandupdate.TheHierarchicalLatentMem-
ory Tree (HLMT) incrementally stores latent abstractions of
theseintermediatestates,enablinglaterreasoningstepstore-
trieve dependency-consistent reasoning paths instead of iso-
lated memory fragments. For embodied environments such
as ALFWorld, trajectory states correspond to environment
observations and actions, while for reasoning benchmarks
they correspond to intermediate reasoning transitions dur-
ing chain-of-thought generation. During training, memory
evolution is optimized using the same task-level supervision
(SFT) or trajectory-level reinforcement signal (RL) as the
underlyingbackbone,makingthememoryoptimizationpro-
tocol consistent across both interactive agent environments
and non-interactive reasoning benchmarks.
Implementation Details on ThresholdsRather than re-
lying on rigid hyperparameter tuning, ActiveMem employs
thresholds primarily as feasible region constraints (action
masking) for the RL policy. In our experiments, similarity-
basedthresholds(τ stopandτ merge)areempiricallyinitialized
to[0.5]and[0.9],respectively.Fortopologymaintenance,we
adoptadynamicpercentile-basedapproachforτ del,pruning
thelowest[5%]ofutility-scoringnodesperepisodetoensure
scale-invariant stability across diverse tasks.
Forabalancedtreewithbranchingfactorbandtotalhistor-
ical interactionsN, the retrieval depth bounds the retrieval
complexity toO(blog b N), drastically reducing theO(N)
burden of flat memory. The overall spatial memory com-
plexity remainsO(N). The external controller introduces
minimal overhead (O(dmodel ×d hidden)), while the latent
injection introduces a fixed attention complexity overhead
linearlyproportionaltotheprefixlengthL.Thecontrolleris
parameterized as a 512-dimensional MLP.
Metrics
Exact match.In QA tasks, we use exact match (EM) as
both the verifiable reward for the RL pipeline and the eval-
uation metric for the final output. The final response is ex-
tracted from between <answer> and </answer>. In multi-
objective settings, the response should contain answers to
each question separated by semicolons. If the XML tags
are mismatched, or if the number of provided answers does
notcorrespondtothenumberofquestions,ascoreof0isas-
signed.Otherwise,1pointiscreditedforeachcorrectanswer.
During RL training, we do not provide any other intermedi-
ate rewards or format penalties, as we find that such manual
interventionscaninterferewiththeagent’slearningprocess.
F1 score.The F1 score computes the harmonic mean be-
tweentheprecisionpandrecallr.Inthecaseofstringmatch-
ing,wesplitboththepredictedanswerandthegroundtruth.
For example, if the ground truth is “United States of Amer-
ica”, it is split into a list with lower-case words: “united”,
“states”, “of”, “america”. The same works for the predicted
answer. Then, denote the number of common words asc.
Further denote the number of words in the predicted answer
asland the number of words in the ground truth asg. Then,
precisionis calculatedasp:=c/landrecalliscalculated as
r:=c/g. The F1 score is finally computed as
F1:= 2× p×r p+r .
Ifmultiplegroundtruthsarepresent,themaximumofallF1
scoresischosen.Formulti-objectivetasks,thefinalF1isthe
sum of the F1 scores for each sub-question.
Peak token usage.Peak token usage is calculated as the
maximum number of tokens (using GPT-4o-mini tokenizer)
in any single sequence throughout the agent’s entire trajec-
tory. For fair comparison in our experiments, the system
prompt is excluded when computing this sequence length.
The peak token usage serves as a proxy for the inference-
time memory requirement.
Inference time.Inference time for each trajectory is
recorded as the total elapsed time required to generate the
complete output trajectory. For all experiments, these mea-
surements are conducted on a single H200 GPU, operating
with10concurrentthreads.ThevLLMinferenceframework
isutilized,withitsautomaticprefixcachingfeatureenabled.
Dependency length.Following (Zhang et al. 2025a), the
dependencymetricisdefinedasthetotalnumberofhistorical
tokens on which each generated token effectively depends.
LetTdenote the total number of interaction steps. For each
stepi∈[T], letn (i) p be the number of prefix tokens andn(i) o
be the number of output tokens generated. The dependency
metric is then calculated as
Dependency:=
X
i∈[T]

2n(i) o +n (i) p

×n (i) o
2 .
At a high level, this metric quantifies the cumulative com-
putational cost associated with the generation of an output

trajectory. It is important to note that in MEM1, prefix to-
kensfrompreviousstepsareconsolidatedintoanewinternal
state,ratherthanbeingcontinuouslyaccumulated.Inourex-
periments, we ignore the tokens in the system prompt when
calculating the dependency metric.
6.7 Training Dataset Setup
Weadopttheofficialtrainingsplitsforallbenchmarkdatasets
except PopQA, which lacks a dedicated training partition.
Allutilizeddatasetsprovideessentialsupervisionsignalsfor
modeltraining.SincePopQAcontainsnoofficialtrainingset,
we directly evaluate on its test split to examine cross-dataset
generalization,usingthemodelpre-trainedonTriviaQAdue
to its high conceptual relevance to PopQA.
6.8 Parameter Configurations
Parameter configurations are shown in Table 4.
Table4:HyperparametersusedinthetrainingofActiveMem.
Settings Hyperparameters
Training (SFT)
train_batch_size= 4
learning_rate= 1e-5
epochs= 2
warmup_ratio= 0.1
optim=adamw_torch
schedular=cosine
Training (GRPO)
rollout_batch_size= 8
train_batch_size= 8
epochs= 2
beta= 0.4
num_iterations= 1
learning_rate= 1e-5
warmup_ratio= 0.1
optim=adamw_torch
schedular=cosine
LoRA
r= 16
lora_alpha= 32
target_modules= [q_proj,v_proj]
lora_dropout= 0.1
bias=none
task_type=CAUSAL_LM
Optimization
adam_offload
flash_attn
deepspeed_enable_sleep
6.9 Baselines
Search-R1.Search-R1 (Jin et al. 2025) is a reinforcement
learning framework that integrates large language models
with real-time search engines for interleaved reasoning and
retrieval. It models the search engine as part of the RL en-
vironment and supports multi-turn query generation trig-
gered by special tokens during step-by-step reasoning. To
stabilize training, it applies loss masking to retrieved to-
kens and optimizes the policy using outcome-based rewards
withoutcomplexprocesssupervision.CompatiblewithPPO
andGRPO,itoutperformsstandardRAGandtool-usemeth-
ods on multiple question-answering benchmarks. This ap-
proachenablesLLMstolearneffectivesearchandreasoning
strategies purely from final outcome feedback. The model is
trainedonthe1-objectivetaskwiththesamedataset.Search-
R1 also uses exact match as its reward function.
Deep Researcher.DeepResearcher (Zheng et al. 2025b)
is the first end-to-end reinforcement learning framework for
training LLM research agents in real-world web environ-
ments. It replaces static RAG corpora with live, noisy web
searchandusesamulti-agentbrowsingarchitecturetoextract
information from diverse webpage structures. Trained with
GRPO and outcome-based F1 rewards, it learns emergent
behaviors including planning, cross-validation, reflection,
and honest uncertainty expression. Experiments on seven
open-domainQAbenchmarksshowlargegainsoverprompt-
based and RAG-based RL baselines, especially in out-of-
distribution generalization. It resolves real-world challenges
such as API limits, anti-crawling, and high-concurrency re-
questsviadistributedclustersandcachingmechanisms.The
model is trained on 1-objective task with a curated set from
variousQAdatasetsincludingHotPotQAandNaturalQues-
tions. Deep Researcher adopts the F1 score as the reward
function.
MEM1.MEM1 (Zhou et al. 2025b) is an end-to-end rein-
forcement learning framework that enables LLM agents to
maintainconstantmemoryusageduringlong-horizonmulti-
turn tasks. It learns to iteratively update a compact internal
state that unifies memory consolidation and reasoning, dis-
carding irrelevant historical context after each step. To sup-
port training, it constructs scalable multi-objective environ-
mentsbycomposingstandardQAdatasetsintolong-horizon
tasks. Trained via PPO with masked trajectory optimiza-
tionforstablepolicylearning,itdeliversstrongperformance
while drastically reducing memory cost and inference time
across QA and web navigation tasks. It also generalizes to
longer horizons unseen during training and exhibits emer-
gentbehaviorsincludingparallelmemorymanagement,self-
verification, and adaptive search planning. MEM1 is trained
exclusively on 2-objective tasks.
6.10 Why GRPO Instead of PPO?
WeadoptGroupRelativePolicyOptimization(GRPO)rather
than standard Proximal Policy Optimization (PPO) primar-
ily for its exceptional memory and computational efficiency.
Standard PPO requires maintaining a Critic (Value) model
ofcomparablesizetothepolicy,imposingprohibitivemem-
oryoverheadsforlong-horizonagents.Bysamplingagroup
of trajectories for a single prompt and computing rela-
tive advantages within the group, GRPO entirely elimi-
nates the need for a value network, which perfectly comple-
mentsourframework’semphasisonalightweightcontroller
and highly efficient context management. Furthermore, this
group-contrastive formulation naturally mitigates the noto-
rious credit assignment problem in extended sequences, es-
tablishing an ideal algorithmic scaffold for integrating fine-
grained, verifiable process supervision directly at interme-
diate trajectory nodes. Finally, because reward signals in
multi-steptreeretrievalareinherentlysparse,GRPO’sinter-
nal group normalization mechanism effectively controls the
high variance of long-trajectory returns. This stabilization
ensures that the discrete topological updates to the memory

tree—suchasnodeinsertions,merges,anddeletions—evolve
smoothly and coherently throughout the extended reasoning
process.
7 More Experiments
7.1 Results on Qwen2.5-1.5B
Results are shown in Table 5.
7.2 generalization study
Results are shown in Figure 5.
7.3 Continual Learning Result
The results in Table 6 indicate three main findings. These
findingssuggestthatActiveMemprovidesamorestableand
transferable mechanism for continual learning.
7.4 More Efficiency Analysis
Results are shown in Table 7.
7.5 Results on Single-Objective Multi-Hop Tasks
Although ActiveMem is primarily engineered for extremely
long-horizonautonomy,ourtrainingparadigmdemonstrates
profound zero-shot transferability to standard multi-hop
tasks.Specifically,ityieldssuperiortaskperformanceandre-
markably higher computational efficiency without requiring
any explicit training on single-objective benchmarks. This
highlights the robustness of our memory representations, as
eventhesestandardsingle-objectivetasksinherentlydemand
complex,multi-turninteractiontrajectoriestoachieveasuc-
cessful resolution.
Long-Horizon Web Navigation on WebShopBeyond
multi-hop QA, we extend our evaluation to complex web
navigation using the WebShop environment (detailed in
App. 6.4) to assess ActiveMem’s proficiency in manag-
ing dynamic, long-horizon interactions. As reported in Ta-
ble 8, ActiveMem establishes a new state-of-the-art among
open-source agents, consistently outperforming compara-
ble baselines such as Agent-Flan, Agent-R, and AgentLM.
Mostremarkably,ActiveMemachievesthissuperioritywhile
demonstratingprofoundcomputationalefficiency.Compared
to the strongest baseline (AgentLM), ActiveMem yields a
2.8×reduction in Peak Token Usage, a1.9×improvement
inContextDependency,anda1.5×accelerationinInference
Time. Furthermore, ActiveMem exhibits exceptional cross-
scale capabilities by decisively surpassing AgentLM-13B, a
model with double the parameter count. Strikingly, our em-
piricalresultsrevealthatthecompactActiveMemframework
outperforms even OpenAI’s proprietary GPT-4o, maintain-
ing its competitive edge even when GPT-4o is heavily aug-
mentedwithourtruncationtemplatesorA-MEMtechniques.
Single-Objective QA on WikipediaTable 9 details the
performance and efficiency of agents on single-objective
Wikipedia QA (Jin et al. 2025), where models iteratively
issue retrieval requests via a RAG pipeline. Crucially,
we deploy the exact ActiveMem checkpoint trained exclu-
sively on the 2-objective setup, rigorously testing its out-
of-distribution transferability to single-objective environ-
ments. Overall, ActiveMem demonstrates absolute superior-
ity across all three efficiency metrics, while simultaneously
securing the highest Exact Match (EM) score and achieving
anF1scorecompetitivewiththeparameter-heavyQwen2.5-
14B-Instruct.Thisprofounddualadvantageisfundamentally
driven by ActiveMem’s core mechanism: it actively consol-
idates historical interactions into a highly compact internal
state,therebydrasticallyminimizingcontexttokenoverhead.
Furthermore, empirical results reveal a severe performance
drop when relying solely on Supervised Fine-Tuning (SFT),
definitivelyunderscoringthenecessityofourRL-drivenop-
timization for robust memory management.
Search Agent
Implementation DetailsOur ActiveMem framework is
built upon the Qwen3-30B-A3B-Instruct-2507 architecture
(Yang et al. 2025). This model features 30B total parame-
ters, utilizing an Mixture-of-Experts (MoE) approach that
activates 3B parameters during inference. To maintain com-
putational efficiency and prevent infinite loops, we impose a
hard constraint of 100 maximum tool calls per task; any tra-
jectoryexceedingthisthresholdisautomaticallyterminated.
Benchmarks.Regarding evaluation, we consider three
information-seeking benchmarks—BrowseComp (Wei et al.
2025), BrowseComp-ZH (Zhou et al. 2025a), and
WideSearch-en (Wong et al. 2025)—alongside the text-only
subset of the general agent benchmark GAIA (Mialon et al.
2024).WhileBrowseCompanditsChinesevariantprimarily
assess the agent’s precision in locating elusive information,
WideSearch emphasizes the capacity for expansive explo-
ration,forwhichwereporttheItem-F1metric.GAIAserves
to evaluate broader functional capabilities. To mitigate vari-
ance in smaller datasets, we report the average performance
acrossthreeindependenttrialsforanybenchmarkcontaining
fewer than 200 samples.
Baselines.We conduct a comprehensive comparison be-
tween our ActiveMem-30B-A3B and a wide array of repre-
sentativeopen-sourceagents,includingWebThinker(Lietal.
2026), WebDancer (Wu et al. 2026a), WebSailor (Li et al.
2025),ASearcher(Gaoetal.2025),MiroThinker(Teametal.
2025b),WebExplorer(Liuetal.2025b),DeepDive(Shietal.
2025),DeepDiver-V2(Team2025),Kimi-K2-Instruct(Team
et al. 2025a), GLM-4.5 (Zeng et al. 2025), and DeepSeek-
V3.1 (Team). To provide a broader context for performance,
wealsoincludeseveralstate-of-the-artproprietarymodelsas
reference points, such as Claude-4-Sonnet/Opus (Anthropic
2025), OpenAI-o4-mini/o3 (OpenAI 2025b), and OpenAI
DeepResearch(OpenAI2025a).Theresultsreportedherein
are aggregated from a combination of primary experiments,
official technical reports, and public leaderboards.
Results.Results are shown in Table 10.

Table 5: Results on Qwen2.5-1.5B. All values represent the performance metric for each task (e.g., accuracy %). We highlight
the best and second best results.
Method ALFWorld TrivialQA PopQA KodCode BigCodeBench GPQA GSM8K MATH
Vanilla 22.54 32.10 16.08 24.55 40.35 11.62 39.51 36.63
CoT 18.30 28.67 18.39 32.32 38.59 15.67 56.79 45.22
SFT 36.57 63.84 39.20 55.83 37.72 11.11 54.83 38.84
GRPO 43.55 68.21 43.15 62.11 70.34 15.65 68.10 47.42
REINFORCE 43.25 66.50 41.87 60.20 67.80 12.50 67.40 46.89
REINFORCE++ 43.66 66.90 44.69 63.33 69.50 13.80 69.04 47.33
Agent-FLAN 35.80 64.28 38.90 56.21 43.83 9.35 53.02 29.82
ExpeL 28.96 25.20 20.20 31.15 39.78 8.12 45.12 38.12
MemoryBank 27.89 38.14 22.78 37.93 35.87 13.87 47.88 30.47
AWM 30.42 55.69 32.54 - - - - -
SoftCoT 33.07 62.22 38.78 55.13 36.10 9.31 54.50 38.55
Co-processor 35.66 64.78 40.12 56.65 38.10 12.12 57.12 37.40
MemGenSFT 40.30 65.02 41.28 58.16 42.47 18.28 58.15 47.12
MemGenGRPO 54.27 73.42 49.28 65.43 72.81 18.18 73.39 53.36
ActiveMemSFT 55.12 75.28 52.71 67.35 75.02 19.41 70.35 56.52
ActiveMemGRPO 74.82 86.51 61.94 78.29 87.14 30.09 86.02 69.16
8 Details of ActiveMem
8.1 Online Interaction Pipeline
To stabilize autoregressive reasoning under dynamically
evolving memory structures, ActiveMem decouples online
retrieval from asynchronous topology evolution. During au-
toregressivedecoding,allretrievaloperationsareperformed
overatemporallyfrozensnapshotoftheHierarchicalLatent
Memory TreeT. At each decoding step, the current hidden
stateretrievesamemorypaththroughhierarchicaltop-down
traversal,afterwhichthelatentinjectionheadproducescom-
pact memory residuals that modulate the frozen backbone
policy. Meanwhile, the tree action head predicts topology
operations online during interaction. Instead of immediately
modifyingthememorystructure,thepredictedoperationsare
cached throughout the trajectory rollout. After the environ-
ment interaction terminates, the cached operations are asyn-
chronouslycommittedtothepersistentmemorytree.Specif-
ically,insertionandupdateactionsareappliedusingthecol-
lected hidden-state representations, while merge and delete
operations are executed periodically to maintain structural
compactness.Thisdecoupledexecutionstrategypreventsre-
trieval inconsistency caused by concurrent topology muta-
tions during autoregressive decoding while enabling contin-
ual memory evolution across long-horizon interactions.
8.2 Latent Injection Implementation
The latent injection head operates entirely in hidden space
without expanding the textual context window. Given the
shared latent representationu t,j, the controller predicts a
compact latent residual:
mt,j =W latentut,j.(8)
TheresidualisinjectedintointermediateTransformerlay-
ers as a learnable memory prefix. Specifically, for selected
attentionlayers,thelatentmemoryvectorisprependedtothe
key-value cache of the current decoding step:
eK= [m t,j;K], eV= [m t,j;V].(9)
The frozen backbone policy subsequently performs self-
attention over the augmented hidden-state space:
Attn(Q, eK, eV).(10)
To preserve the general reasoning capability of the pre-
trained backbone, only the lightweight LoRA parameters
associated with the memory controller are optimized dur-
ing training. The backbone LLM parameters remain frozen
throughout all experiments.
8.3 Hierarchical Credit Assignment
ActiveMem estimates node utility using trajectory-level
downstreamoutcomes.Foreachmemorynoden i,wemain-
tain an exponential moving estimate of its success probabil-
ity:
S(ni)←(1−η)S(n i) +ηR(τ),(11)
whereR(τ)denotes the environment reward of trajectories
that activate nodeni during retrieval.
Theglobaladvantageevaluateswhetheranodecontributes
moreeffectivelythantheaveragememoryabstractionacross
the entire tree:
Aglobal i =S(n i)− 1 |T | X nj ∈T S(nj).(12)
Meanwhile, the local advantage measures relative im-
provement over the parent abstraction:
Alocal i =S(n i)−S(n f (i)).(13)

0 10 20 30 40 50 60 70
GSM8K
KodCode
GPQA
MATH
Trained on GSM8K
0 10 20 30 40 50 60 70
GSM8K
KodCode
GPQA
MATH
Trained on KodCode
Vanilla SFT MemoryBank MemGen ActiveMem
Figure 5: The generalization study. We train ActiveMem on GSM8K or KodCode and evaluate it on all four datasets
Thefinalhierarchicaladvantagecombinesbothobjectives:
Ai =λ gAglobal i +λ lAlocal i .(14)
To stabilize long-horizon optimization, depth-aware dis-
counting is further applied:
eAi =γ di Ai,(15)
whered i denotes the depth of nodeni in the hierarchy. This
mechanism encourages globally useful abstractions while
preserving fine-grained specialization within local memory
branches.
9 Complexity Analysis
Assume the hierarchicalmemory tree has depthDand aver-
agebranchingfactorB.Unlikeflatretrievalmechanismsthat
requireexhaustivesimilaritysearchoverallmemoryentries,
ActiveMemperformsrecursivetop-downtraversaloverlocal
child sets.
At each traversal step, retrieval computes similarity only
among the current node’s children, leading to retrieval com-
plexity:
O(DB).(16)
Underboundedbranchingassumptions,theretrievalcom-
plexity grows approximately logarithmically with the total
number of memory nodes:
D≈log B |T |.(17)
Therefore, ActiveMem scales substantially more effi-
cientlythanflatmemoryretrievalmethodswhosecomplexity
grows linearly with memory size:
O(|T |).(18)
Meanwhile, topology evolution operations are executed
asynchronously after trajectory completion and therefore do
not introduce additional decoding-time overhead.
10 Theoretical Insights into ActiveMem
In this section, we establish a rigorous mathematical foun-
dation for ActiveMem. By bridging structured memory re-
trievalwithinformationtheory,metricspacecoveringunder
dynamic adaptation, and policy gradient variance analysis,
weformallyprovethearchitecturaladvantagesoftopological
reasoning trees over flat, sequential memory buffers.
10.1 Formal Definitions and Causal Graph
Alignment
Letthemulti-turnagentinteractionenvironmentbemodeled
asaStructuralCausalModel(SCM).WedefineZ H ∈ ZH as
the abstract latent vector representing high-level task intent
(e.g., domain-specific planning goals), andZL ∈ ZL as the
low-level trajectory execution details (e.g., instance-specific
actionsandobservations).Thegenerateddownstreamaction
at any decoding token step is denoted byY.
Definition 10.1(Flat Memory).A flat memory poolMf lat
is defined as an uncompressed, concatenated sequence of

Table6:ContinuallearningresultsofQwen2.5-1.5B-Instruct
across four reasoning and programming datasets (AQuA,
GPQA, GSM8K, KodCode). The model is sequentially
trained on each dataset (AQuA→GPQA→GSM8K→
KodCode), and after each training stage, evaluation is con-
ducted on all four benchmarks.
Trained On Method AQuA GPQA GSM8K KodCode Vanilla 41.34 11.62 39.51 24.55
AQuA
SFT 42.52 16.67 42.10 18.20
ExpeL 41.73 12.67 40.16 16.30
MemGen 43.31 19.70 39.80 19.55
ActiveMem47.10 22.51 51.28 24.38
GPQA
SFT 38.55 17.17 45.74 18.50
ExpeL 37.24 14.35 42.67 15.20
MemGen 39.85 20.72 47.96 28.80
ActiveMem43.82 28.48 58.93 34.13
GSM8K
SFT 33.46 13.13 52.31 19.45
ExpeL 34.89 12.42 48.78 13.65
MemGen 38.43 21.72 55.67 19.75
ActiveMem44.28 26.84 63.28 25.15
KodCode
SFT 28.61 2.53 24.14 54.10
ExpeL 27.14 6.23 31.44 48.35
MemGen 40.34 20.09 53.72 52.95
ActiveMem46.86 24.51 61.20 68.44
historical random vectors accumulated overTinteraction
steps:M f lat={(Z (i) H , Z(i) L )}T i=1.
Definition10.2(LatentMemoryTree).Alatentmemorytree
is a directed acyclic graphMtree = (V,E)embedded in a
semanticallystructuredmetricspace(X, d).Theretrievalop-
eratorR(q)actively extracts a coherent, dependency-aware
topological pathP ⊂ Vmapped to the current execution
state.
Definition 10.3(Irrelevant Confounders).LetZ irr L ⊂ ZL
denote the subset of historical execution details that are
causally independent of the current intentZcurr H but reside
within the memory pool. They act as spurious confounders
and cross-task interference sources if explicitly attended to
during autoregressive decoding.
To ensure that the causal graph accurately reflects the
structural task isolation properties claimed by ActiveMem,
we introduce the following structural assumption:
Assumption 10.4(Topological Domain Isolation).If two
subtasks belong to distinct procedural domains (e.g., flight
booking workflows vs. hotel booking rules), their corre-
sponding node pathsP1,P 2 ⊂ Vare topologically disjoint
except at the hierarchical domain rootv0. In the underlying
structural causal model, this disjoint topology enforces that
theirrelevantexecutiondetailsZ irr L ofaninactivebranchare
d-separatedfromtheactiveintentZ curr H giventhepath-level
memory contextMtree.
10.2 Information Entanglement and Causal
Decoupling
Proposition 10.5(Causal Decoupling via Tree Retrieval).
Under the assumption of structural d-separation in the rea-
soningtree(Assumption10.4),path-basedactivationstrictly
reduces the expected mutual information between irrelevant
historical confounders and the current execution action to
zero,eliminatingcross-taskleakageinherentinflatretrieval:
E

I(Z irr L ;Y| Mtree)  = 0≪E  I(Z irr L ;Y| Mf lat)  .
Proof.Bythecoredefinitionofconditionalmutualinforma-
tion, the informational entanglement can be quantified via
the Kullback-Leibler (KL) divergence between the joint and
marginal conditional distributions:
I(Z irr L ;Y| M)(19)
=E Z,Y,M

log P(Z irr L , Y| M) P(Z irr L | M)P(Y| M)  (20)
=H(Y| M)− H(Y|Z irr L ,M)(21)
For a flat memory poolMf lat, the unrestricted token-
level attention mechanism operates globally over the joint
union S(Z (i) H , Z(i) L ). In the system SCM, conditioning on
the un-isolated flat bufferM f latopens a backdoor col-
lider path:Z irr L → Mf lat←Z curr H →Y. Consequently,
conditioning onZ irr L alters the action generation distribu-
tion, meaningP(Y|Z irr L ,M f lat)̸=P(Y| M f lat). This
yields a strictly positive mutual information due to informa-
tion leakage:H(Y|Z irr L ,M f lat)<H(Y| M f lat) =⇒
I(Z irr L ;Y| Mf lat)>0.
Conversely,ActiveMem’streeretrievaloperatorR(q)ex-
tracts an isolated path contextMtree =P(l ∗ t ). According
to Assumption 10.4, the topological branching ensures the
causal Markov condition holds, rendering distinct subtrees
mutually d-separated. Given the retrieved path aligned with
Z curr H , the irrelevant variablesZirr L situated in unselected
structural branches are conditionally independent ofY:
Z irr L ⊥ ⊥Y| Mtree (22)
This conditional independence directly factorizes the joint
conditional probability distribution:
P(Z irr L , Y| Mtree)(23)
=P(Z irr L | Mtree)P(Y| Mtree)(24)
Substituting Equation (24) into the logarithmic term of the
KL divergence in Equation (20) yields:
I(Z irr L ;Y| Mtree) =E[log(1)] = 0(25)
Therefore,E[I(Z irr L ;Y| M tree)]<E[I(Z irr L ;Y|
Mf lat)], demonstrating complete causal decoupling of ir-
relevant task contexts.
10.3 Topological Growth and Bounded Dynamic
Complexity
To resolve the reproducibility concern regarding memory
capacity controls, we evaluate the tree complexity not as
a static expansion, but as a dynamic birth-death resource
process governed by ActiveMem’s joint optimization loop
(incorporating node insertion, merging, and pruning).
Proposition 10.6(Bounded Dynamic Tree Size).Let the
agent task domain be a compact metric space(X, d)with
bounded Lebesgue measureµ(X) = 1. Under a semantic

Table 7: Quantitative comparison of models on multi-objective, multi-hop QA tasks. Arrows indicate the optimal direction for
each metric. Underlined entries denote catastrophic model collapse (i.e., extremely low performance). Variants marked with
(truncate)adopt ActiveMem’s prompt and rollout pipeline with context truncation. Variants labeled with(A-MEM)employ the
prompt, rollout pipeline, and the external memory module from ActiveMem (Xu et al. 2026).ActiveMem-QArefers to our
proposed ActiveMem optimized specifically on the 2-objective QA.
Model 2-Objective 8-Objective 16-Objective
EM↑F1↑Peak (×10 2)↓Time (s)↓EM↑F1↑Peak (×10 2)↓Time (s)↓EM↑F1↑Peak (×10 2)↓Time (s)↓
Qwen2.5-14B-Inst 0.732 0.902 15.6±0.19 5.49±0.16 1.55 1.87 44.7±0.37 16.2±0.27 0.567 0.703 38.4±0.71 29.7±0.75
Qwen2.5-7B-Inst 0.268 0.366 19.6±0.33 4.60±0.08 0.87 1.10 49.5±0.40 13.9±0.18 0.165 0.213 43.3±0.62 15.5±0.23
Qwen2.5-7B-Inst (A-MEM) 0.286 0.371 14.1±0.10 24.6±0.51 1.13 1.43 18.6±0.10 53.7±1.26 0.730 0.961 18.8±0.14 91.2±2.44
Qwen2.5-7B-Inst (truncate) 0.262 0.336 8.28±0.06 5.89±0.16 0.97 1.23 11.8±0.10 11.9±0.20 0.396 0.497 13.3±0.16 22.1±0.60
Search-R1 0.452 0.531 13.0±0.08 4.09±0.23 0.064 0.08 24.7±0.19 4.25±0.16 0.009 0.011 20.9±0.03 4.75±0.18
DeepResearcher 0.536 0.650 22.0±0.434.01±0.070.73 0.90 51.8±0.35 11.3±0.14 0.071 0.106 48.9±0.66 15.8±0.19
MEM1-QA 0.709 0.8386.40±0.026.49±0.07 1.87 2.318.01±0.06 8.68±0.121.97 2.3910.4±0.09 8.70±0.12
ActiveMem-QA0.753 0.9256.68±0.04 6.84±0.052.39 2.848.83±0.04 9.13±0.102.83 3.5811.5±0.04 9.32±0.08
Table 8: Quantitative evaluation on the WebShop navigation benchmark. Inference latency for proprietary GPT models is
excludedtoensureequitablecomparison,asAPI-dependentmetricsarenotdirectlycomparabletolocalexecution.Performance
scores for Agent-R are sourced directly from the original publication due to the unavailability of its model weights. The-
WebShopsuffix designates model variants explicitly fine-tuned on the WebShop domain.
Model Avg Final Reward↑Peak Token (×10 3)↓Dependency (×10 6)↓Inference Time Per Traj (s)↓
GPT-4o 25.485.30±1.23 3.99±1.16N/A
GPT-4o (truncate) 13.820.99±0.99 0.81±0.23N/A
GPT-4o (A-MEM) 24.501.84±0.06 0.31±0.11N/A
Qwen2.5-7B-Instruct 18.425.64±1.34 3.38±0.89 12.31±1.82
Qwen2.5-14B-Instruct 12.345.44±0.92 3.30±0.61 18.17±2.32
Agent-FLAN-7B 40.353.37±1.12 2.18±1.62 9.95±6.19
Agent-R-8B 63.91 N/A N/A N/A
AgentLM-7B 63.602.24±0.40 0.28±0.07 3.91±1.07
AgentLM-13B 70.802.36±0.46 0.30±0.08 5.23±1.59
MEM1-WebShop 70.870.81±0.100.15±0.16 2.61±0.48
ActiveMem-WebShop 76.240.86±0.070.09±0.11 2.46±0.34
anchoringthresholdτ,anoptimisticutilitythresholdϵ 0,and
a policy-driven branch pruning rateρ∈(0,1), the expected
number of active nodesE[|VN |]generated over an infinite
task streamN→ ∞is strictly upper-bounded by a finite
constant:
lim
N→∞
E[|VN |]≤ 1 (1−ρ)cτ D ∈ O(1)
whereDis the intrinsic dimensionality of the latent reason-
ing space, andc >0is a geometric volume coefficient.
Proof.Let any newly instantiated memory nodevnew cover
a local semantic neighborhood parameterized as aτ-ball
Bτ ⊂ Xwith measureµ(B τ ) =cτ D >0. ActiveMem
triggers a node insertion action at steptif and only if the
incoming reasoning state hidden vectorhst falls outside the
union of all existingτ-balls. LetU t denote the uncovered
measure of the metric space after executingttasks. The
intrinsicbranchingprobabilityis preciselyequivalent tothis
remaining uncovered region:p(t) branch =U t−1.
When an insertion occurs, the expected uncovered space
decreases proportionally:E[U t |U t−1] =U t−1(1−cτ D).
Solvingthisrecurrencerelationfromtheboundaryinitializa-
tionU 0 = 1gives the expected insertion probability at task
stept:E[p (t) branch] = (1−cτ D)t−1. Concurrently, after each trajectory rollout sequence, Ac-
tiveMemdynamicallyevaluatesnodeutilityviascore(n i) =
βri + (1−β)f i.Nodesthataccumulatelow-utilityareelim-
inated asynchronously via PruneNodes(G, δ, nmin), while
redundant subtrees are consolidated via semantic merging.
Lettheexpectedfractionofnodesprunedorconsolidatedper
taskiterationbeparameterizedasastationarypolicyoutflow
rateρ∈(0,1).Theexpectationoftheactivenodepopulation
pool satisfies the regularized dynamic balance equation:
E[|Vt|] =E[|V t−1|] +E[p (t) branch]−ρE[|V t−1|](26)
= (1−ρ)E[|V t−1|] + (1−cτ D)t−1 (27)
Solvingthisdynamicrecurrencerelationexplicitlyacrossthe
continuous task horizon yields:
E[|VN |] =
NX
t=1
(1−ρ) N−t (1−cτ D)t−1 (28)
Taking the infinite limit asN→ ∞, the summation con-

Table 9: Performance comparison across diverse environments on single-objective tasks. Arrows denote the optimal direction
for each metric. The(SFT)notation indicates variants trained via Supervised Fine-Tuning while adopting ActiveMem’s prompt
templates and rollout pipeline. Notably, baseline models undergo task-specific optimization for their respective domains:
DeepResearcher is exclusively tailored for the Online Web-QA task targeting the F1 score, whereas Search-R1 is specifically
optimized for the Wiki-RAG task using Exact Match (EM) as the training signal.
Environment SystemEM↑F1↑Peak Token (×10 2)↓Dependency (×10 5)↓Inference Time↓
Wiki RAG
Qwen2.5-7B-Inst (truncate) 0.287 0.3826.28±0.05 1.65±0.04 2.26±0.04
Qwen2.5-7B-Inst (A-MEM) 0.246 0.3738.47±0.12 0.92±0.03 11.2±0.40
Qwen2.5-7B-Inst 0.269 0.3909.32±0.19 1.17±0.04 2.31±0.04
Qwen2.5-14B-Inst 0.422 0.5348.89±0.21 2.22±0.10 6.73±0.24
Search-R1 0.445 0.51611.0±0.25 1.50±0.052.23±0.14
DeepResearcher 0.419 0.50313.3±0.34 7.04±0.33 3.86±0.09
MEM1-QA (SFT) 0.302 0.3586.54±0.05 3.30±0.13 4.84±0.21
MEM1-QA 0.405 0.4715.63±0.030.76±0.02 3.79±0.07
ActiveMem (SFT)0.462 0.5636.83±0.04 2.03±0.05 4.73±0.25
ActiveMem 0.498 0.6085.96±0.020.52±0.013.52±0.05
Online Web-QA
Qwen2.5-7B-Inst 0.334 0.4518.37±0.18 1.39±0.06 2.20±0.04
DeepResearcher 0.372 0.49210.27±0.19 2.86±0.14 2.87±0.06
MEM1-QA 0.397 0.4855.79±0.060.44±0.02 1.84±0.03
ActiveMem-QA 0.421 0.5095.94±0.040.31±0.03 1.66±0.02
verges to a steady-state geometric series boundary:
lim
N→∞
E[|VN |] =
∞X
t=1
(1−ρ) t−1(1−cτ D)t−1 (29)
= 1 1−(1−ρ)(1−cτ D) ≤ 1 (1−ρ)cτ D (30)
Since the thresholdsτ >0andρ >0are fixed, the upper
boundinEquation(30)isafiniteconstantindependentofN.
This mathematically guarantees that the memory tree layout
maintains sublinear, bounded growthO(1)⊂o(N)under
lifelong deployment.
10.4 Variance Reduction in Policy Optimization
Proposition 10.7(Credit Assignment Stabilization).Let
∇J(ϕ)bethepolicygradientestimatorusedtotrainActive-
Mem’s controller. Freezing the autoregressive LLM policy
πθ and restricting the trainable MDP optimization horizon
fromthefine-grainedtokenlevel(T token)tothemacroscopic
memorytreedepth(T mem)reducesthevarianceoftheGRPO
estimator quadratically:
Var[∇Jmem(ϕ)]≤
 Tmem
Ttoken
2
Var[∇Jtoken(ϕ)]
Proof.Consider a standard policy gradient estimatorˆg=PH
t=1 ∇ϕ logπ(a t |s t) ˆAtoveranarbitraryoperationalhori- zon lengthH. Let the score function variance be bounded
byE[∥∇ ϕ logπ∥ 2]≤σ 2 and the estimated advantages be
boundedsuchthat| ˆAt| ≤Amax.Usingthelawoftotalvari-
ance alongside the Cauchy-Schwarz inequality, the norm of
thetotalestimatorvariancecanbeupper-boundedasfollows:
Var[ˆg] =E

∥ˆg−E[ˆg]∥2 (31)
≤E


 HX
t=1
∥∇ϕ logπ(a t |s t)∥ |ˆAt|
!2
 (32)
≤E
" HX
t=1
12
!  HX
t=1
∥∇ϕ logπ(a t |s t)∥2 ˆA2 t
!#
(33)
=H·
HX
t=1
E
h
∥∇ϕ logπ∥ 2 ˆA2 t
i
(34)
≤H·H·σ 2A2 max =O(H 2)(35)
In a flat, end-to-end token-level reinforcement learning
paradigm, the policy gradient must propagate back through
the massive vocabulary generation spaceAtoken, yielding
aneffectiveoptimizationhorizonH=T token.Theresulting
variance upper bound scales quadratically with token count
asO(T 2 token).
In ActiveMem, the massive backbone LLMπθ is kept
strictly frozen. Autoregressive token generation steps are
treatedaspartofthestochasticenvironmenttransitionsfrom
the perspective of the controller. The trainable controller
policyπ ϕ onlyemitsdiscretetopologyevolutionandrouting
path actions withinAmem. Consequently, the optimization
MDP is compressed topologically to the maximum depth of
the reasoning path, meaning the effective horizon matches
the tree depth:H=T mem. SubstitutingT mem into Equa-
tion(35)yieldsanisolatedvarianceboundofO(T 2 mem).The
varianceboundratioisthereforemathematicallyconstrained
by:
Var[∇Jmem(ϕ)]
Var[∇Jtoken(ϕ)] ≈ T 2 mem T 2 token =  Tmem Ttoken 2 (36)

Table 10: Main results. ActiveMem-30B-A3B achieves remarkable performance, surpassing open-source agents with much
larger model size such as AgentFold-30B-A3B, DeepSeek-V3.1-671B-A37B and matching proprietary agents such as OpenAI-
o4-mini, indicating the potential of this new paradigm.
Agent BrowseComp BrowseComp-ZH WideSearch GAIA
Proprietary Agents
Claude-4-Sonnet(Anthropic 2025) 14.7 22.5 62.0 68.3
Claude-4-Opus(Anthropic 2025) 18.8 37.4 - -
OpenAI-o4-mini(OpenAI 2025b) 28.3 44.3 - -
OpenAI-o3(OpenAI 2025b) 49.7 58.1 60.0 70.5
OpenAI Deep Research(OpenAI 2025a) 51.5 42.9 - 67.4
Open-Source Agents
WebThinker-32B(Li et al. 2026) 2.8 7.3 - 48.5
WebDancer-32B(Wu et al. 2026a) 3.8 18.0 - 51.5
WebSailor-32B(Li et al. 2025) 10.5 25.5 - 53.2
WebSailor-72B(Li et al. 2025) 12.0 30.1 - 55.4
ASearcher-Web-32B(Gao et al. 2025) 5.2 15.6 - 52.8
MiroThinker-32B-DPO-v0.2(Team et al. 2025b) 13.0 17.0 - 64.1
WebExplorer-8B(Liu et al. 2025b) 15.7 32.0 - 50.0
DeepDive-32B(Shi et al. 2025) 14.8 25.6 - -
DeepDiver-V2-38B (Team 2025) 13.4 34.6 - -
Kimi-K2-Instruct-1T(Team et al. 2025a) 14.1 28.8 59.9 57.3
GLM-4.5-355B-A32B(Zeng et al. 2025) 26.4 37.5 - 66.0
DeepSeek-V3.1-671B-A37B(Team) 30.0 49.2 - 63.1
AgentFold-30B-A3B (Ye et al. 2026) 36.2 47.3 62.1 67.0
ActiveMem 43.6 56.1 73.5 72.8
Given that the structural reasoning tree depth is orders
of magnitude smaller than the full sequence token length
(Tmem ≪T token), ActiveMem guarantees a quadratic vari-
ance reduction. This formal stabilization ensures highly ef-
ficient credit assignment under sparse long-horizon task re-
wards, explaining the massive convergence gains observed
empirically.
