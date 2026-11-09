---
title: Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems
url: https://arxiv.org/abs/2607.27443
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Xu Zheng
- Zhuomin Chen
- Chaohao Lin
- Hua Wei
- Haifeng Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.27443
pages: 29
chars: 97369
fetched_at: '2026-11-08T13:34:04+00:00'
kb_version: 1
---

# Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems

Leveraging Trajectory Graphs for Pre-Execution
Error Diagnosis in Agentic LLM Systems
Xu Zheng1 Zhuomin Chen1 Chaohao Lin1 Hua Wei2
Haifeng Chen3 Wei Cheng3 Dongsheng Luo4∗
1Florida International University, Miami, FL, USA
2Arizona State University, Tempe, AZ, USA
3NEC Laboratories America, Princeton, NJ, USA
4Singapore Management University, Singapore
Abstract
Large Language Model (LLM)-based agents have demonstrated exceptional per-
formance across a wide range of complex interactive tasks. However, they often
struggle with long-horizon interactive tasks common in domains, such as embodied
AI. The complexity and vast action spaces in these settings lead to compounding
errors, where a single suboptimal action can derail an entire trajectory, causing
the agent to exhaust its limited step budget on inefficient or unrecoverable paths.
To overcome this without costly fine-tuning, we draw inspiration from software
debugging, where execution logs are analyzed to preemptively catch errors. We
proposeTrajectory Graph Copilot, a novel framework that acts as a “copilot” for
LLM agents by diagnosing potential action errors before they are executed. At its
core,Graph Debuggermodels historical trajectories as a probabilistic graph and
uses a Graph Neural Network to identify sequential action patterns that frequently
lead to failure. Functioning as a proactive diagnostic sandbox, our method provides
early warnings on potentially flawed actions, prompting the agent to self-correct.
This pre-action error diagnosis prevents costly mistakes, significantly enhancing
the agent’s ability to complete long-horizon tasks successfully. The extensive
experiments on four benchmarks with three LLM agents demonstrate a 14.69%
pass ratio improvement on average.
1 Introduction
Large Language Models (LLMs), such as ChatGPT [33], Gemini [45], and Llama [47], possess a
remarkable capacity language comprehension and generation. When equipped with tools [68, 57],
these LLMs become powerful agents capable of extraordinary performance in complex applications
such as coding [13, 38, 76], scientific reasoning [52], and embodied artificial intelligence (Embodied
AI) [37, 41, 30]. These tasks often require agents to plan and execute long sequences of actions while
interacting with an environment [24, 64, 22, 67].
Despite their powerful reasoning capabilities, LLM agents often falter in complex and unfamiliar en-
vironments due to compounding errors [48, 63]. Prevailing strategies attempt to mitigate this through
post-hoc learning, using methods like environmental data exploration [60, 63, 42] or refinement learn-
ing [64, 75, 49]. However, these approaches share a fundamental limitation. By learning primarily
from the final outcomes of entire trajectories, they struggle to pinpoint the specific, step-level actions
that lead to failure. A reward for a trajectory provides a much weaker learning signal than feedback
explaining why a particular action was incorrect (e.g., targeting a non-existent object or performing
∗Corresponding author. This work was primarily conducted while he was at Florida International University.
Preprint.
arXiv:2607.27443v1  [cs.AI]  29 Jul 2026

an invalid sequence). Without this granular, causal feedback, agents learn inefficiently from sparse
signals and are prone to repeating similar mistakes.
To address this gap, we shift the paradigm from post-hoc trajectory analysis to proactive, step-level
error diagnosis. We draw inspiration from software debugging. When a program fails, a developer
uses a debugger to trace the execution, inspect the context, and pinpoint the exact line of code that
caused the error. This pre-action, fine-grained analysis is far more effective than simply observing
that the program crashed. This inspires our framework,Trajectory Graph Copilot, which incorporates
a graph-based diagnostic module,Graph Debugger. It acts as a “debugger” for the LLM agent,
analyzing its intended action in the context of the recent past to flag potential errors before they are
executed. This allows the agent to find potential errors early, preventing the accumulation of costly
mistakes that would otherwise doom the entire task.
By framing agent execution within the Partially Observable Markov Decision Process (POMDP)
paradigm [64, 49], our method ❶ transforms historical trajectories into a probabilistic graph. This
structure encodes domain knowledge by capturing the underlying relationships between actions and
observations [3, 17]. In our formulation, nodes represent actions and edges encode observations,
which can be viewed as an adaptation of the classical state–transition diagram. Unlike the traditional
methods, such as the retrieval-based methods [80], our graph-based approach offers two key advan-
tages: it ❷ provides higher performanceand ❸ requires fewer samplesto achieve the same level
error detection rate. We detail these insights in Section 4. Furthermore, instead of directly suggesting
correct actions,Graph Debuggercan ❹ serve as a diagnosis sandbox for the LLM-Agent decision
making. By providing only potential error warnings, our method encourages LLM agents to rely on
their own reasoning. This minimizes the bias introduced by fine-tuning on a fixed dataset, ultimately
leading to better generalization on new tasks.
To empirically verify the effectiveness of our framework, we conduct experiments on four benchmarks,
including embodied AI environments and planning tasks. We begin by collecting trajectory datasets
and annotating actions with corresponding labels, followed by conducting detection experiments
on them. Compared with traditional text classification and LLM-based methods,Graph Debugger
demonstrates a consistent advantage in step-level error detection. Moreover, we applyGraph
Debuggeras a diagnosis sandbox to provide error feedback in advance. By leveraging In-Context
Learning (ICL) with feedback information, our method enhances LLM agents’ pass ratio by 14.69%
on average, outperforming baselines. In summary, the contributions are as follows:
★ We introduce,Graph Debugger, a novel method based on a probabilistic graph model, to address
the challenge of step-level action error detection in LLM agents.
★ Our framework,Trajectory Graph Copilot, integrates this error detection module as a distinct
entity. By serving as a graph-based diagnostic module for LLM agents, our approach enhances
their performance by providing real-time error warnings.
★ Experiments conducted across multiple environments and LLM agents confirm the superiority of
Graph Debuggerin error detection and validate the effectiveness of the overall framework.
2 Preliminaries
Long-Horizon Tasks as POMDPs.Following prior work, we model an LLM agent’s interaction
in a long-horizon task as a POMDP [ 4, 49, 42, 64]. A POMDP is defined by the tuple M=
(G,S,A,J,R,O, γ) , where G is the goal space, S is the state space, A is the action space, J:
S × A → Sis the state-transition function, R:S × A × G →Ris the reward function, O is the
observation space, and γ is the discount factor. In the text-based environments considered by this
work, the spacesG,A, andOare subsets of natural language.
Graphical Models for Sequential Decision Making.A Markov Decision Process can be concep-
tually viewed as a Probabilistic Graphical Model (PGM), where nodes represent states and edges
represent transitions. This graphical perspective highlights the sequential dependencies inherent in
agent trajectories. However, in a POMDP, the true state is latent, and the belief state (a probability
distribution over states) is often high-dimensional and intractable to model explicitly, especially with
language-based observations. Directly constructing and reasoning over a formal state-based PGM
is therefore impractical. This motivates our work to develop a different, more practical graphical
representation learned directly from trajectory data to diagnose action errors.
2

Problem Formulation: Step-Level Error Diagnosis.Given a particular goal g∈ G, an LLM agent
generates a trajectory history of alternating observations and actions, (o0, a0, . . . , ot−1, at−1, ot).
Before executing the next proposed action at, our goal is to determine if this action is productive
or a potential error. To formalize what constitutes a “good” action, we move beyond simple binary
success/failure signals. Inspired by the benchmark AgentBoard [5], where the task is decomposed into
subgoals, we conceptualize complex tasks as requiring the completion of several ordered milestones.
For example, in AlfWorld, the task “clean a plate and put it on countertop” involves a sequence of
milestones, including collecting the plate, cleaning it, and placing it correctly. The quality of an
action can therefore be evaluated based on the progress it makes toward the next milestone. Figure 1
illustrates this concept by comparing an ideal Expert Trajectory, which progresses smoothly through
milestone states, with an Agent Trajectory, which may deviate and follow a less optimal path.
To create an informative label space Y={1, ..., C}, we define a set of fine-grained error categories
that capture common failure modes in long-horizon tasks. These categories are not only inspired
by task planning principles, using milestones to identify errors likePrecondition Not Met (P .M.)or
Condition Met, Action Not Taken (C.M.), but also include general procedural errors such asRepeated
Action (R.A.)andIllegal Action (I.A.). This multi-faceted approach provides a rich, step-level
diagnostic signal. The complete set of six error definitions is detailed in Appendix C.1. Our objective
is to learn a diagnostic function f that maps a trajectory history to a label for thecurrentproposed
action: f: (o 0, a0, . . . , ot, at)7→y t,wherey t ∈ Y. This provides granular, step-level feedback
that is far more informative than a sparse, trajectory-level reward.
3Trajectory Graph Copilot
In this section, we introduce a novel framework,Trajectory Graph Copilotfor LLM agents, which
includes a graph-based error diagnosis module,Graph Debugger. Initially, we transform text trajec-
tories into graphs from the perspective of PGM. Subsequently, we adopt the idea of TextGCN [69]
Figure 1: A conceptual diagram of a
POMDP illustrating our error diagnosis
task. An expert follows an optimal tra-
jectory from the Initial State (b0) to the
Goal State (b4) by progressing through
Milestone States (b6, b3). In contrast, the
agent’s trajectory is suboptimal.
to regard the action error diagnosis as a node classification
task. Finally, we applyGraph Debuggeras a diagnosis
sandbox in LLM agents for step-level action debugging
and providing feedback for decision making. The overall
framework is shown in Figure 2.
3.1 Graph Construction
Building an accurate graph based on PGM presents two
challenges: representing the dependency between states
and actions, and accurately representing states in the graph.
From Section 2, the LLM agents’ trajectories can be ex-
pressed as paths in a state transition graph. However,
representing actions as edges duplicates the graph struc-
ture, reducing the overall information content, since dif-
ferent states may share the same action. To better extract
the dependency between states and actions, a heteroge-
neous graph [43], where the nodes V comprise both states
B and actions A, offers a more effective and structured
representation. The heterogeneous graph enables node
reduction by merging states with highly similar neigh-
bors into a supernode, yielding a more generalized repre-
sentation. However, due to the partial observation, it is
hard to estimate the state in the graph. To address this
issue, we consider using observations instead of states.
In a POMDP, observations follow the conditional proba-
bility p(o|s). Given the observation posterior probability
q(o) and p(o|s), the state distribution can be inferred by
p(s)∝ P o p(o|s)q(o)/ P s′ p(o|s′). Therefore, states are learned as implicit knowledge through observations. However, given that the observation results are
in natural language and cannot be easily discretized, we integrate them as attributes within the edges
to form an action-centric graph.
3

Figure 2: Overall pipeline ofTrajectory Graph Copilot. We first collect the trajectories. We then use
theGraph Debuggerto predict the action error labels, which includes converting trajectories into a
PGM-based graph and utilizing the GNN-based detector. Finally, our framework provides external
information for agent decision-making.
During implementation, to obtain a robust representation of nodes, we utilize a natural language
processing tool, NLTK [2], to finish some regular preprocessing, such as removing meaningless
words/numbers. We then deduplicate actions to form a set of unique nodes and construct the PGM-
based graph by linking them according to their order in the trajectories. Finally, we reform the
state-transition diagram as an action-centric graphG= (V,E), whereV ⊆ AandE ⊆ O.
3.2 Potential Error Diagnosis
To achieve a step-level action error detection, we adopt the TextGCN [69] to regard trajectories as
sentences. We use the pretrained Bert [9] model to initialize action and observation embeddings. By
linking the trajectory nodes with action nodes, the error probe task is converted into a trajectory node
classification task. Formally, the complete graph adjacency matrixAis defined as:
Aij =
( 1v i, vj ∈ A,and[vi, o, vj]∈ξ
1v i ∈ A,andvj ∈ T
0otherwise
,(1)
where [vi, o, vj] is a subsequence of a trajectory ξ, T is the set of trajectories and o is an observation.
For edge attribution, we collect all the observations {o, o∈[a i, o, aj]} linking the same action pair
and get the average of the Bert embedding. The rest of the nodes and edges are set up with all zeros.
For potential error detection, we implement the detection mechanism outlined in the pipeline through
a Graph Neural Network (GNN) architecture. Given a trajectory ξ, our goal is to train a mapping
function f that probes if there is a potential error. This corresponds to the operation of the GNN
detector across K rounds of message passing. Each GNN layer performs one round of message
passing, defined by the following update rule:
a(l) v =AGG (l)

h(l−1) u :u∈ N(v)  ,
h(l) v =COMBINE (l)

h(l−1) v , a(l) v

,
where a(l) v denotes the aggregated message at l-th layer, h(l) v the feature vector of node v, and N(v)
its set of neighbors. The AGG(l) is a function that aggregates information from neighboring nodes,
while COMBINE(l) updates the node representations, following the definition in previous work [65].
After K rounds of updating, this process yields the final node embeddings H. For the error detection,
4

we apply a softmax function to the final embeddings to obtain probabilities, Z=softmax(H) . The
GNN model is trained by minimizing the cross-entropy loss on the labeled trajectories:
L=−
X
t∈T
X
ℓ∈Y
Ytℓ lnZ tℓ,(2)
where T represents the train set of trajectories and Y is the label space. During testing, we inject the
trajectory node into the existing graph constructed by the training set. To address potential issues
where an action, observation, or task falls outside the defined scope, we use embeddings to search
for and retrieve the corresponding trajectory path from the existing graph. We provide the detailed
information in Appendix C.6.
3.3 In-Context Learning Feedback
To fully leverage the corrective signals provided by our external feedback module, we design a
mechanism that integrates these signals into the agent’s reasoning loop through ICL [ 26, 78, 81].
Rather than fine-tuning the underlying language model, our approach dynamically adapts the agent’s
behavior during inference by augmenting the prompt with structured feedback information. The
detailed implementation is available in Appendix C.1.
Without feedback, the agent’s generative behavior is modeled by the conditional distribution
Pagent(Ai+1|(O0, A0, ...Oi, Ai)). With the environment copilot feedback, it first evaluates the
Ai+1 initialized by the agent and generates the feedback signal Yi, where the signal space is defined
in Section 2. If Yi indicate there is potential error, then the agent should regenerate A′ i+1 according to
the revised conditional distribution Pagent(A′ i+1|(O0, A0, ...Oi, Ai), Ai+1, Yi). The revised condi-
tional distribution can be viewed as the agent’s posterior over actions. In practice, ICL operationalizes
this posterior update by conditioning the model on explicit feedback text in the prompt.
4 Theoretical Analysis
One goal of this work is to detect the potential error based on the trajectory. A straightforward
approach is to directly retrieve historical trajectories to determine if the current action is erroneous. A
key challenge is managing the rapidly growing size of the trajectories as the number of interactions
with the environment increases. Alternatively, because the action and observation modalities are
consistent, the problem of error detection can be formulated as a text sequence classification task.
Prior works [44, 23] have explored sequence-based modeling approaches for the task, such as Bert-
based detectors [9]. Despite the promise, the structured information hidden in the trajectories is
not well-explored. Drawing inspiration from PGM, we formulate the action error probe task as a
node classification on a converted graph. Building upon this foundation, we show that graph-based
methods have a lower Bayes risk and sample complexity than sequence-based methods under the
same generalization error.
To better serve theory analysis, we reorganize the trajectory as a tupleX= (τ, G,O 1:k,A 1:k), where
G is the task, τ is the trajectory identifier, Oi, Ai are the i-th observation and action for i= 1, ...k,
and k is the number of action/observation in trajectory. The decision target is the ground truth class
Y∈ Y of the final action. We consider a class of baselines, theempirical sequence-based(ESB)
method, which captures the critical characteristics of existing approaches. The classical ESB method,
such as a fine-tuned Bert classification model, contains two modules, a sequence representation
mapping U= Φ seq(X)∈ U ⊆Rdseq and a classifier hseq :U → Y. In this work, the graph
representation is S= Φ g(X)∈ S ⊆Rdg obtained byprobabilistic graph-based(PGB) approach,
where S is chosen to be the Markov blanket [35] of Y in the graph induced by the connectivity rules.
Similarly, a classifier hg is learned from (S, Y)pairs. To better compare ESB and PGB, we first
make two conventional assumptions as follows.
Assumption 4.1(Conditional Sufficiency).There exists a representation S= MB G(Y) (the
Markov blanket ofYunder the graph construction) such thatY⊥ ⊥X\S

 S.
This assumption indicates that the label of an action is determined in limited steps and dependent on
other steps, which is aligned with the Markov decision process. In the Appendix C.1, we provide an
example to illustrate why this assumption holds. In Section 2, we follow the assumption to use the
milestone states to refer to the action labels.
5

Table 1: Action error detection results(%), the metric is the accuracy( ↑). GPT4o. is short for
GPT4o-mini. The best performances are inbold, and the second-best method is underlined .
AlfWorld TextWorld ScienceWorld TravelPlanner
Method GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3
Text Classification
TF-IDF 58.04 66.98 63.75 63.68 49.82 42.09 81.02 80.66 80.52 93.3565.23 65.22
Bert 53.09 62.07 55.85 64.17 54.12 49.44 83.51 80.48 78.72 92.14 65.76 64.63
Retrieve
MiniLM 39.33 46.74 49.74 59.37 43.55 42.37 73.87 76.57 73.76 90.20 60.56 58.79
E5 44.82 57.51 53.14 57.05 27.24 52.54 76.59 74.48 72.98 90.88 58.22 59.23
GTR 48.10 58.41 54.00 60.20 30.47 53.67 76.17 74.74 74.00 90.09 59.77 59.30
RAG
GPT4o 55.18 62.73 60.38 52.74 49.1069.2172.15 74.21 68.76 79.87 56.82 55.72
Gemma3 55.74 64.43 59.95 61.69 51.25 60.17 77.11 80.75 76.59 34.95 39.81 39.28
Qwen2.5 50.04 57.56 55.32 43.12 35.84 51.69 67.94 71.05 66.30 24.25 31.22 31.29
LLM Zero-Shot
GPT4o 32.12 30.13 32.06 45.77 42.29 48.31 33.33 35.30 31.45 4.21 8.68 8.03
Gemma3 31.04 28.92 33.81 48.26 34.59 44.35 18.81 34.42 20.30 2.42 4.48 4.03
Qwen2.5 16.46 20.24 16.75 39.64 27.78 31.64 19.76 19.79 20.83 2.25 10.86 11.46
LLM One-Shot
GPT4o 22.34 21.81 28.22 51.41 37.46 55.65 13.49 13.43 11.03 4.32 8.89 7.96
Gemma3 27.30 20.99 32.39 42.45 32.62 37.85 9.78 21.52 14.31 2.55 4.46 4.19
Qwen2.5 17.12 17.59 17.05 40.30 33.15 38.98 31.12 17.96 21.44 2.58 11.19 11.55
LLM Three-Shot
GPT4o 29.13 20.65 33.51 50.41 35.13 49.72 15.85 15.03 11.77 3.46 2.48 4.42
Gemma3 30.21 26.29 27.26 38.47 34.77 33.33 29.23 50.91 20.83 2.27 5.59 8.73
Qwen2.5 16.33 19.29 16.59 44.28 26.70 37.85 28.54 31.97 22.63 0.95 5.50 5.57
Ours 63.98 69.89 66.85 67.00 62.19 66.67 87.84 84.57 83.39 92.75 67.43 68.15
Theorem 4.2(Bayes Risk Ordering and Sample Complexity).For any measurable classifier h
and representation Φ, define the risk as R(h◦Φ) :=P(h(Φ(X))̸=Y) , and let R∗(·) denote the
corresponding Bayes (irreducible) risk. Among all representations, the sufficient statisticS is optimal:
its Bayes risk equals that of the full inputX. For any other representationU= Φ(X), we have
R∗(S)≤R ∗(U),(3)
where the inequality is strict whenever I(Y;S)> I(Y;U) . This ordering of risks translates directly
to sample complexity: to achieve classification error ϵ under the same error tolerance, the graph and
sequential representations requirem g andm seq samples, respectively, satisfyingm g < mseq.
The theorem demonstrates that the graph-based method has a lower Bayes risk and could achieve
superior performance compared to the ESB method under identical conditions. The detailed proof is
provided in Appendix B.
5 Experiments
To verify the effectiveness of our framework, we conduct empirical studies on two perspectives: error
detection and feedback evaluation. We first collect and build datasets on four environments, and then
we compare the performance on our framework and baselines.
Datasets & Benchmarks.Four environments are used for dataset construction, including Alf-
World [41], TextWorld [8, 14], ScienceWorld [ 52], and TravelPlanner [ 62]. These benchmarks
evaluate long-term reasoning by requiring agents to interact with the environment, gather information,
and make decisions. For instance, ScienceWorld evaluates an agent’s ability to programmatically
solve problems using scientific knowledge, while TravelPlanner tests its capacity to use tools for
information gathering and planning under user constraints. We follow the React [71] to implement a
vanilla agent for the data collection and experiments. In AlfWorld, we follow Agentboard to split
the train, validation, and test tasks. In TextWorld and ScienceWorld, we use the first 10 variants
as training and validation tasks, and 5 variants as test tasks. In TravelPlanner, we select 100 tasks
for each difficult level as test tasks and reserve the others for training and validation tasks. To
remove the bias of LLMs, we use GPT4o-mini [34], Qwen2.5-14B (Qwen2.5) [66], and Gemma3-
27B (Gemma3) [46] for all four environments. For the step-level annotation, we first employ LLM
models to generate the label, and then a rule-based script is used to select and filter. The detailed
dataset information is available in Appendix C.2.
6

Evaluation Metrics.For error detection, we use the classical metric, accuracy, to measure the
performance. In the feedback evaluation, we report two metrics: Pass Ratio (PR) and Ground
Ratio (GR). PR is used to evaluate whether an agent has successfully completed a given task, and GR
is a metric that assesses the validity of an agent’s action within a given environment state, serving
as an indicator of its grounding and understanding. In TravelPlanner, the PR indicates whether the
agents give the final plan. In practice, we are primarily concerned with the PR. We mainly provide
the analysis of GR in the Appendix.
Baselines.Our baselines contain three categories of approaches. The conventional methods include
TF-IDF [39] and fine-tuned Bert methods [9], which are represent the text classification approaches.
We use TF-IDF to extract the feature and logistic regression to predict the error probability. We also
use retrieval-based [10] and Retrieval-Augmented Generation (RAG) [20] methods as representative
approaches for incorporating external databases. In retrieval-based methods, we use embedding to
find the most similar trajectory. We use three language models to obtain the embeddings, including
ALL-MiniLM-L6-v2 (MiniLM) [53], E5-Large (E5) [50], and GTR-T5-Large (GTR) [32]. For RAG,
we select the five most similar trajectories as candidates and use LLMs to generate the answer. We
use the GTR as the embedding model to measure the similarity. Furthermore, we consider the LLM-
as-a-judge [79] methods as the LLM-based methods, including three settings: zero-shot, one-shot,
and three-shot. To avoid the model bias, we use three LLM models for RAG and LLM-as-judge:
GPT4o [12], Qwen2.5-14B (Qwen2.5), and Gemma3-27B (Gemma3).
5.1 Error Probe Performance Analysis
Detection Results.In Table 1, we report the results across four benchmark datasets. Overall, our
method mostly outperforms baselines. Specifically, the graph-based detection approach achieves
over a 5% improvement compared to text classification methods on average. The advantage is most
striking in the AlfWorld environment, where the agent is built with GPT4o-mini, and our method
achieves a 10.23% increase over the second-best approach. This observation aligns with our analysis
that graph-based methods require lower data complexity than sequence-based approaches, making
them more effective in handling sparse or noisy trajectories.
We also observe interesting differences across RAG methods. In the first three environments, RAG
methods outperform standard retrieval approaches, whereas in TravelPlanner, the opposite holds. We
attribute this reversal to the much longer observation sequences in TravelPlanner, which may dilute
the benefits of RAG and make simple retrieval more effective. Meanwhile, LLM-as-judge methods
consistently perform poorly. We believe this is due to the inherent difficulty of the tasks, which demand
strong logical reasoning skills beyond the capabilities of current judgment-style approaches. Finally,
Table 2: Statistical significance analysis of action
error detection (Micro F1) on TextWorld.The best
performances are inbold, and the second-best
method is underlined.
Method GPT4o. Qwen2.5 Gemma3
Text Classification
TF-IDF 0.6365±0.00160.4996 ±0.00410.4045±0.0160
Bert 0.6368 ±0.00970.4996 ±0.05010.4345±0.0493
Retrieval
GTR 0.5322±0.00730.3018±0.00090.5322±0.0073
RAG
Gemma3 0.6232±0.00300.5183±0.00660.6124 ±0.0072
LLM Zero-Shot
Gemma3 0.4732±0.00300.3427±0.00290.4492±0.0000
LLM One-Shot
Gemma3 0.3755±0.07550.2620±0.07410.3090±0.0554
LLM Three-Shot
Gemma3 0.1158±0.04570.3194±0.05050.1876±0.0907
Ours 0.6872±0.0091 0.5810±0.0133 0.6316±0.0229
we find no consistent trend between one-shot
and three-shot settings. Surprisingly, in most
cases, the zero-shot setting achieves better per-
formance than either, likely because additional
samples introduce bias that hinders the reason-
ing ability of the LLMs. These findings further
highlight the robustness of our graph-based de-
tection approach across different environments
and prompting strategies.
Statistical Significance Analysis.To further
evaluate the robustness of error detection perfor-
mance, we conduct the statistical significance
analysis on the TextWorld benchmark with three
LLMs. We use Gemma3 for the LLM zero-shot,
one-shot, and three-shot methods. As shown in
Table 2, our method consistently outperforms
the baselines, demonstrating the advantage of
the action-centric graph. We further provide
macro F1 results in Appendix D.2.
7

Figure 3: The pass ratio (%) results across four benchmarks and three LLM agents. Ours consistently
outperforms other baselines.
5.2 Feedback Evaluation Results
Main Results.To evaluate the effectiveness ofTrajectory Graph Copilot, we conduct feedback
evaluation experiments. We compare against four baselines: TF-IDF, GTR, Gemma3, and GPT4o,
representing text-classification, retrieval-based, RAG-based, and LLM-as-judge (zero-shot) categories,
respectively. The detailed experimental setup is provided in Appendix C.4. We report the average
results on four benchmarks and three LLM agents in Figure 3. As the results show, both our
method and baselines outperform the vanilla results in most cases, demonstrating that the mechanism,
Table 3: Performance comparison (Pass Ra-
tio(%)) of different methods with two open-source
LLMs.The best performances are inbold.
ReAct Reflexion Ours
Qwen2.5 62.50 60.0065.00
Gemma3 70.00 67.5075.00
feedback in the interaction consistently en-
hances agent performance across different detec-
tion strategies. Among these methods,Trajec-
tory Graph Copilotachieves the strongest perfor-
mance on average, which outperforms baselines
on all four benchmarks. On average, our method
improves the vanilla by 14.69%. Interestingly,
even for RAG and LLM-as-judge, which show
weaker detection accuracy, the agents still ben-
efit from performance gains. For example, in
ScienceWorld, LLM-as-Judge methods have a poor detection ratio but still boost the agents. A
possible explanation is that LLMs may not always follow instructions precisely, leading to incorrect
prediction labels; however, they still provide useful analysis that guides the agents. For the detailed
results and analysis of GR, we provide in Appendix D.3.
Comparison with Deliberate Prompting-based LLM agents.To further illustrate the effectiveness
of ours, we conduct the comparison experiments with ReAct [ 71] and Reflexion [ 40], which are
famous prompting-based LLM agents. We use the TextWorld benchmark with two open-source LLMs.
Table 4: Graph construction ablation study on detection. The Dir.
and Undir. are short for directed graph and undirected graph.
AlfWorld ScienceWorld
Graph GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3 Avg.
Onehot
Dir.64.2269.38 65.60 85.95 81.99 81.02 74.69
Undir. 62.44 67.83 65.63 82.21 82.17 81.71 73.67
Bert
Dir. 63.98 69.89 66.85 87.8484.57 83.39 76.09
Undir. 63.0570.18 67.2284.3285.68 83.7275.70
As shown in Table 3, our method
outperforms both baselines. This
is primarily because ReAct and
Reflexion rely heavily on the in-
herent reasoning capabilities of
the LLM, which can lead to error
accumulation and degraded per-
formance, especially when the
underlying model is not suffi-
ciently large, and no external
feedback signals are available.
5.3 Ablation Study
Graph Construction.To examine the graph’s variance, we conducted ablation studies on another
three settings, exploring combinations of two node features, Bert embedding or one-hot embedding
as attribution, and two edge types, directed and undirected edges. As shown in Table 4, our results
indicate that the performance of undirected graphs is slightly inferior to that of directed graphs.
The key reason is that POMDP dependencies are inherently directional, and representing them with
undirected graphs introduces noise, leading to a slight performance decline. Additionally, using
8

Figure 4: The ablation study of pass ratio (%) on maximum attempt times and confidence threshold.
one-hot encoding as a feature yields poorer performance compared to using Bert, demonstrating that
text information is useful in the detection tasks.
Feedback Integration.To explore the insight of the integration mechanisms, we evaluate four
types of integration mechanisms: (1) incorporating feedback in the user prompt, (2) including
feedback in the user prompt without label explanations, (3) adding feedback in the system prompt,
and (4) appending feedback to the trajectory history. We conduct these experiments in the TextWorld
environment with two open-source LLMs. As the results shown in Table 5, Gemma3 is more robust
than Qwen2.5 across different feedback integration strategies. When feedback is incorporated into
the user prompt, it yields greater improvements than other configurations, even after integration with
the system prompt.
Table 5: Ablation study results (PR) of feedback
integration mechanisms on TextWorld. In the ta-
ble, “exp.” is short for “explanations”. The best
performances are inbold.
Method Qwen2.5 Gemma3
in trajectories 57.50 70.00
in system 60.0075.00
in user65.00 75.00
in user w/o exp. 62.50 72.50
Hyperparameter Study of Feedback.Fur-
thermore, we conduct ablation studies to an-
alyze the impact of different settings ofTra-
jectory Graph Copiloton the TextWorld and
ScienceWorld benchmarks using Qwen2.5 and
Gemma3. Specifically, we analyze two key fac-
tors: the maximum number of attempts and the
choice of confidence threshold, as detailed in
Appendix C.4. As illustrated in Figure 4, PR
performance improves as the number of attempts
increases, then decreases, before eventually sta-
bilizing. This behavior is intuitive; additional
attempts raise the likelihood of producing valid
and reasonable actions, thereby reducing the probability of failure at each step. However, we also
observe a decline in GR, consistent with the findings in Section 5.2. In contrast, the confidence
threshold has only a marginal effect on overall performance. We attribute this to the strength of the
detection module, where the threshold plays a minor role, when detection is highly accurate and
robust, as relatively few false alarms or misclassifications propagate to the next stage. If detection
were less reliable, the choice of threshold would likely have a much greater impact. Interestingly, we
also find that setting a higher confidence threshold slightly improves GR performance. Additional
quantitative results supporting these observations are provided in Appendix D.4.
6 Conclusion
In this paper, we proposeGraph Debugger, a novel PGM-based graph detection method for step-level
diagnosis of agent action decisions. Compared with traditional approaches and LLM-based methods
such as text classification, RAG, or LLM-as-judge,Graph Debuggerachieves lower error rates while
requiring fewer samples. Beyond the detection module itself, we further introduceTrajectory Graph
Copilot, a flexible pipeline that integrates the detection module as an independent sandbox to provide
actionable feedback on agent behaviors. We conduct extensive experiments on four benchmarks and
three LLM-based agents to validate the effectiveness of our approach. The experiments and findings
highlight not only the effectiveness ofGraph Debuggerin detecting errors but also its potential as a
general framework for improving decision-making in LLM agents. We believe this work can inspire
more reliable performance-enhancement strategies for agent-based systems.
Limitation.This work requires collecting a dataset, which can be time-consuming for tasks with
limited historical trajectory data. Although continuously updating the trajectory pool and action-
9

centric graph could further improve agent performance, we do not explore this aspect in the current
paper due to space constraints. We leave it as a direction for future work.
Broader Impact.This work introduces a method for improving the performance of existing LLM
agents, formalized as a plug-in module that integrates seamlessly with existing agent frameworks.
We believe this work contributes positively to the broader goal of building more capable and reliable
AI systems, with potential benefits across a range of real-world applications.
References
[1] Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Michal Podstawski, Lukas
Gianinazzi, Joanna Gajda, Tomasz Lehmann, Hubert Niewiadomski, Piotr Nyczyk, et al. Graph
of thoughts: Solving elaborate problems with large language models. InProceedings of the
AAAI conference on artificial intelligence, volume 38, pages 17682–17690, 2024.
[2] Steven Bird, Edward Loper, and Ewan Klein.Natural language processing with Python.
O’Reilly Media, Inc., 2009.
[3] Christopher M Bishop and Nasser M Nasrabadi.Pattern recognition and machine learning,
volume 4. Springer, 2006.
[4] Thomas Carta, Clément Romac, Thomas Wolf, Sylvain Lamprier, Olivier Sigaud, and Pierre-
Yves Oudeyer. Grounding large language models in interactive environments with online
reinforcement learning. In Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara En-
gelhardt, Sivan Sabato, and Jonathan Scarlett, editors,Proceedings of the 40th International
Conference on Machine Learning, volume 202 ofProceedings of Machine Learning Research,
pages 3676–3713. PMLR, 23–29 Jul 2023.
[5] Ma Chang, Junlei Zhang, Zhihao Zhu, Cheng Yang, Yujiu Yang, Yaohui Jin, Zhenzhong Lan,
Lingpeng Kong, and Junxian He. Agentboard: An analytical evaluation board of multi-turn llm
agents.Advances in neural information processing systems, 37:74325–74362, 2024.
[6] Baian Chen, Chang Shu, Ehsan Shareghi, Nigel Collier, Karthik Narasimhan, and Shunyu Yao.
Fireact: Toward language agent fine-tuning.arXiv preprint arXiv:2310.05915, 2023.
[7] Yaran Chen, Wenbo Cui, Yuanwen Chen, Mining Tan, Xinyao Zhang, Dongbin Zhao, and
He Wang. Robogpt: an intelligent agent of making embodied long-term decisions for daily
instruction tasks.arXiv preprint arXiv:2311.15649, 2023.
[8] Marc-Alexandre Côté, Ákos Kádár, Xingdi Yuan, Ben Kybartas, Tavian Barnes, Emery Fine,
James Moore, Ruo Yu Tao, Matthew Hausknecht, Layla El Asri, Mahmoud Adada, Wendy
Tay, and Adam Trischler. Textworld: A learning environment for text-based games.CoRR,
abs/1806.11532, 2018.
[9] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep
bidirectional transformers for language understanding. InProceedings of the 2019 Conference
of the North American Chapter of the Association for Computational Linguistics: Human
Language Technologies, pages 4171–4186. Association for Computational Linguistics, 2019.
[10] Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Mingwei Chang. Retrieval
augmented language model pre-training. InInternational conference on machine learning,
pages 3929–3938. PMLR, 2020.
[11] Shibo Hao, Yi Gu, Haodi Ma, Joshua Jiahua Hong, Zhen Wang, Daisy Zhe Wang, and Zhit-
ing Hu. Reasoning with language model is planning with world model.arXiv preprint
arXiv:2305.14992, 2023.
[12] Aaron Hurst, Adam Lerer, Adam P. Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark,
AJ Ostrow, Akila Welihinda, et al. Gpt-4o system card, 2024.
[13] Md Ashraful Islam, Mohammed Eunus Ali, and Md Rizwan Parvez. Mapcoder: Multi-agent
code generation for competitive problem solving.arXiv preprint arXiv:2405.11403, 2024.
10

[14] Peter A. Jansen and Marc-Alexandre Côté. Textworldexpress: Simulating text games at one
million steps per second.arXiv, 2022.
[15] Tomoyuki Kagaya, Thong Jing Yuan, Yuxuan Lou, Jayashree Karlekar, Sugiri Pranata, Akira
Kinose, Koki Oguri, Felix Wick, and Yang You. Rap: Retrieval-augmented planning with
contextual memory for multimodal llm agents.arXiv preprint arXiv:2402.03610, 2024.
[16] Thomas N. Kipf and Max Welling. Semi-supervised classification with graph convolutional
networks. InInternational Conference on Learning Representations, 2017.
[17] Daphane Koller.Probabilistic Graphical Models: Principles and Techniques. The MIT Press,
2009.
[18] Yunshi Lan, Gaole He, Jinhao Jiang, Jing Jiang, Wayne Xin Zhao, and Ji-Rong Wen. Complex
knowledge base question answering: A survey.IEEE Transactions on Knowledge and Data
Engineering, 35(11):11196–11215, 2022.
[19] Seungjae Lee, Jigang Kim, Inkyu Jang, and H Jin Kim. Dhrl: A graph-based approach for
long-horizon and sparse hierarchical reinforcement learning.Advances in Neural Information
Processing Systems, 35:13668–13678, 2022.
[20] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman
Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. Retrieval-augmented
generation for knowledge-intensive nlp tasks.Advances in neural information processing
systems, 33:9459–9474, 2020.
[21] Kun Li, Tianhua Zhang, Xixin Wu, Hongyin Luo, James Glass, and Helen Meng. Decoding on
graphs: Faithful and sound reasoning on knowledge graphs through generation of well-formed
chains.arXiv preprint arXiv:2410.18415, 2024.
[22] Manling Li, Shiyu Zhao, Qineng Wang, Kangrui Wang, Yu Zhou, Sanjana Srivastava, Cem
Gokmen, Tony Lee, Erran Li Li, Ruohan Zhang, et al. Embodied agent interface: Benchmarking
llms for embodied decision making.Advances in Neural Information Processing Systems,
37:100428–100534, 2024.
[23] Qian Li, Hao Peng, Jianxin Li, Congying Xia, Renyu Yang, Lichao Sun, Philip S Yu, and Lifang
He. A survey on text classification: From traditional to deep learning.ACM Transactions on
Intelligent Systems and Technology (TIST), 13(2):1–41, 2022.
[24] Shuang Li, Xavier Puig, Chris Paxton, Yilun Du, Clinton Wang, Linxi Fan, Tao Chen, De-An
Huang, Ekin Akyürek, Anima Anandkumar, et al. Pre-trained language models for interactive
decision-making.Advances in Neural Information Processing Systems, 35:31199–31212, 2022.
[25] Zichao Li, Zong Ke, and Puning Zhao. Injecting structured knowledge into llms via graph
neural networks. InProceedings of the 1st Joint Workshop on Large Language Models and
Structure Modeling (XLLM 2025), pages 16–25, 2025.
[26] Barys Liskavets, Maxim Ushakov, Shuvendu Roy, Mark Klibanov, Ali Etemad, and Shane K
Luke. Prompt compression with context-aware sentence encoding for fast and improved llm
inference. InProceedings of the AAAI Conference on Artificial Intelligence, volume 39, pages
24595–24604, 2025.
[27] Laura Londoño, Juana Valeria Hurtado, Nora Hertz, Philipp Kellmeyer, Silja V oeneky, and
Abhinav Valada. Fairness and bias in robot learning.Proceedings of the IEEE, 112(4):305–330,
2024.
[28] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. InInternational
Conference on Learning Representations, 2019.
[29] Linhao Luo, Zicheng Zhao, Gholamreza Haffari, Yuan-Fang Li, Chen Gong, and Shirui Pan.
Graph-constrained reasoning: Faithful reasoning on knowledge graphs with large language
models.arXiv preprint arXiv:2410.13080, 2024.
11

[30] Yueen Ma, Zixing Song, Yuzheng Zhuang, Jianye Hao, and Irwin King. A survey on vision-
language-action models for embodied ai.arXiv preprint arXiv:2405.14093, 2024.
[31] Costas Mavromatis and George Karypis. Gnn-rag: Graph neural retrieval for efficient large lan-
guage model reasoning on knowledge graphs. InFindings of the Association for Computational
Linguistics: ACL 2025, pages 16682–16699, 2025.
[32] Jianmo Ni, Chen Qu, Jing Lu, Zhuyun Dai, Gustavo Hernandez Abrego, Ji Ma, Vincent Zhao,
Yi Luan, Keith Hall, Ming-Wei Chang, et al. Large dual encoders are generalizable retrievers.
InProceedings of the 2022 Conference on Empirical Methods in Natural Language Processing,
pages 9844–9855, 2022.
[33] OpenAI. Chatgpt. 2022.
[34] OpenAI. Gpt-4o mini: advancing cost-efficient intelligence. https://openai.com/
index/gpt-4o-mini-advancing-cost\-efficient-intelligence/ , 2024.
Accessed: July 31, 2026.
[35] Judea Pearl. Graphical models for probabilistic and causal reasoning.Quantified representation
of uncertainty and imprecision, pages 367–389, 1998.
[36] Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo, Haizhou Shi, Chuntao Hong, Yan Zhang,
and Siliang Tang. Graph retrieval-augmented generation: A survey.arXiv preprint
arXiv:2408.08921, 2024.
[37] Xavier Puig, Kevin Ra, Marko Boben, Jiaman Li, Tingwu Wang, Sanja Fidler, and Antonio
Torralba. Virtualhome: Simulating household activities via programs. InProceedings of the
IEEE conference on computer vision and pattern recognition, pages 8494–8502, 2018.
[38] Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize
Chen, Yusheng Su, Xin Cong, et al. Chatdev: Communicative agents for software development.
arXiv preprint arXiv:2307.07924, 2023.
[39] Gerard Salton and Christopher Buckley. Term-weighting approaches in automatic text retrieval.
Information processing & management, 24(5):513–523, 1988.
[40] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflex-
ion: language agents with verbal reinforcement learning. In A. Oh, T. Naumann, A. Globerson,
K. Saenko, M. Hardt, and S. Levine, editors,Advances in Neural Information Processing
Systems, volume 36, pages 8634–8652. Curran Associates, Inc., 2023.
[41] Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, and
Matthew Hausknecht. Alfworld: Aligning text and embodied environments for interactive
learning.arXiv preprint arXiv:2010.03768, 2020.
[42] Yifan Song, Da Yin, Xiang Yue, Jie Huang, Sujian Li, and Bill Yuchen Lin. Trial and error:
Exploration-based trajectory optimization for llm agents.arXiv preprint arXiv:2403.02502,
2024.
[43] Richard S Sutton, Andrew G Barto, et al.Reinforcement learning: An introduction, volume 1.
MIT press Cambridge, 1998.
[44] Kamal Taha, Paul D Yoo, Chan Yeun, Dirar Homouz, and Aya Taha. A comprehensive survey
of text classification techniques and their research applications: Observational and experimental
insights.Computer Science Review, 54:100664, 2024.
[45] Gemini Team, Petko Georgiev, Ving Ian Lei, Ryan Burnell, Libin Bai, Anmol Gulati, Garrett
Tanzer, Damien Vincent, Zhufeng Pan, Shibo Wang, et al. Gemini 1.5: Unlocking multimodal
understanding across millions of tokens of context.arXiv preprint arXiv:2403.05530, 2024.
[46] Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya Pathak, et al. Gemma 3 technical
report.arXiv preprint arXiv:2503.19786, 2025.
12

[47] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timo-
thée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open
and efficient foundation language models.arXiv preprint arXiv:2302.13971, 2023.
[48] Hanlin Wang, Chak Tou Leong, Jian Wang, and Wenjie Li. E2cl: exploration-based error
correction learning for embodied agents.arXiv preprint arXiv:2409.03256, 2024.
[49] Hanlin Wang, Jian Wang, Chak Tou Leong, and Wenjie Li. Steca: Step-level trajectory
calibration for llm agent learning.arXiv preprint arXiv:2502.14276, 2025.
[50] Liang Wang, Nan Yang, Xiaolong Huang, Binxing Jiao, Linjun Yang, Daxin Jiang, Rangan
Majumder, and Furu Wei. Text embeddings by weakly-supervised contrastive pre-training.
arXiv preprint arXiv:2212.03533, 2022.
[51] Peiyi Wang, Lei Li, Zhihong Shao, RX Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang
Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations.arXiv
preprint arXiv:2312.08935, 2023.
[52] Ruoyao Wang, Peter Jansen, Marc-Alexandre Côté, and Prithviraj Ammanabrolu. Scienceworld:
Is your agent smarter than a 5th grader?arXiv preprint arXiv:2203.07540, 2022.
[53] Wenhui Wang, Hangbo Bao, Shaohan Huang, Li Dong, and Furu Wei. MiniLMv2: Multi-head
self-attention relation distillation for compressing pretrained transformers. InFindings of the
Association for Computational Linguistics: ACL-IJCNLP 2021, pages 2140–2151, Online,
August 2021. Association for Computational Linguistics.
[54] Xinyi Wang, Alfonso Amayuelas, Kexun Zhang, Liangming Pan, Wenhu Chen, and
William Yang Wang. Understanding reasoning ability of language models from the perspective
of reasoning paths aggregation.arXiv preprint arXiv:2402.03268, 2024.
[55] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha
Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language
models.arXiv preprint arXiv:2203.11171, 2022.
[56] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le,
Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models.
Advances in neural information processing systems, 35:24824–24837, 2022.
[57] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun
Zhang, Shaokun Zhang, Jiale Liu, et al. Autogen: Enabling next-gen llm applications via
multi-agent conversations. InFirst Conference on Language Modeling, 2024.
[58] Xixi Wu, Yifei Shen, Caihua Shan, Kaitao Song, Siwei Wang, Bohang Zhang, Jiarui Feng,
Hong Cheng, Wei Chen, Yun Xiong, et al. Can graph learning improve planning in llm-based
agents?Advances in Neural Information Processing Systems, 37:5338–5383, 2024.
[59] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang,
Junzhe Wang, Senjie Jin, Enyu Zhou, et al. The rise and potential of large language model
based agents: A survey.Science China Information Sciences, 68(2):121101, 2025.
[60] Jiannan Xiang, Tianhua Tao, Yi Gu, Tianmin Shu, Zirui Wang, Zichao Yang, and Zhiting
Hu. Language models meet world models: Embodied experiences enhance language models.
Advances in neural information processing systems, 36:75392–75412, 2023.
[61] Yuchen Xiao, Yanchao Sun, Mengda Xu, Udari Madhushani, Jared Vann, Deepeka Garg, and
Sumitra Ganesh. O3d: Offline data-driven discovery and distillation for sequential decision-
making with large language models.arXiv preprint arXiv:2310.14403, 2023.
[62] Jian Xie, Kai Zhang, Jiangjie Chen, Tinghui Zhu, Renze Lou, Yuandong Tian, Yanghua Xiao,
and Yu Su. Travelplanner: A benchmark for real-world planning with language agents. In
Forty-first International Conference on Machine Learning, 2024.
[63] Jian Xie, Kexun Zhang, Jiangjie Chen, Siyu Yuan, Kai Zhang, Yikai Zhang, Lei Li, and Yanghua
Xiao. Revealing the barriers of language agents in planning.arXiv preprint arXiv:2410.12409,
2024.
13

[64] Weimin Xiong, Yifan Song, Xiutian Zhao, Wenhao Wu, Xun Wang, Ke Wang, Cheng Li, Wei
Peng, and Sujian Li. Watch every step! llm agent learning via iterative step-level process
refinement.arXiv preprint arXiv:2406.11176, 2024.
[65] Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. How powerful are graph neural
networks? InInternational Conference on Learning Representations, 2019.
[66] An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, et al. Qwen2.5 technical report.
arXiv:2412.15115 [cs.CL], 2024.
[67] Rui Yang, Hanyang Chen, Junyu Zhang, Mark Zhao, Cheng Qian, Kangrui Wang, Qineng Wang,
Teja Venkat Koripella, Marziyeh Movahedi, Manling Li, et al. Embodiedbench: Comprehensive
benchmarking multi-modal large language models for vision-driven embodied agents.arXiv
preprint arXiv:2502.09560, 2025.
[68] Rui Yang, Lin Song, Yanwei Li, Sijie Zhao, Yixiao Ge, Xiu Li, and Ying Shan. Gpt4tools:
Teaching large language model to use tools via self-instruction.Advances in Neural Information
Processing Systems, 36:71995–72007, 2023.
[69] Liang Yao, Chengsheng Mao, and Yuan Luo. Graph convolutional networks for text classi-
fication. InProceedings of the AAAI conference on artificial intelligence, volume 33, pages
7370–7377, 2019.
[70] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik
Narasimhan. Tree of thoughts: Deliberate problem solving with large language models.Ad-
vances in neural information processing systems, 36:11809–11822, 2023.
[71] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan
Cao. React: Synergizing reasoning and acting in language models. InInternational Conference
on Learning Representations (ICLR), 2023.
[72] Xi Ye, Semih Yavuz, Kazuma Hashimoto, Yingbo Zhou, and Caiming Xiong. Rng-kbqa:
Generation augmented iterative ranking for knowledge base question answering.arXiv preprint
arXiv:2109.08678, 2021.
[73] Da Yin, Faeze Brahman, Abhilasha Ravichander, Khyathi Chandu, Kai-Wei Chang, Yejin Choi,
and Bill Yuchen Lin. Agent lumos: Unified and modular training for open-source language
agents.arXiv preprint arXiv:2311.05657, 2023.
[74] Che Rin Yu, Daewon Chae, Dabin Seo, Sangwon Lee, Hyeongwoo Im, and Jinkyu Kim.
Scene graph-guided proactive replanning for failure-resilient embodied agent.arXiv preprint
arXiv:2508.11286, 2025.
[75] Siyu Yuan, Zehui Chen, Zhiheng Xi, Junjie Ye, Zhengyin Du, and Jiecao Chen. Agent-r: Train-
ing language model agents to reflect via iterative self-training.arXiv preprint arXiv:2501.11425,
2025.
[76] Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, and Zhi Jin. Codeagent: Enhancing code generation
with tool-integrated agent systems for real-world repo-level coding challenges.arXiv preprint
arXiv:2401.07339, 2024.
[77] Qixuan Zhang, Xinyi Weng, Guangyou Zhou, Yi Zhang, and Jimmy Xiangji Huang. Arl: An
adaptive reinforcement learning framework for complex question answering over knowledge
base.Information Processing & Management, 59(3):102933, 2022.
[78] Yiming Zhang, Shi Feng, and Chenhao Tan. Active example selection for in-context learning.
InProceedings of the 2022 Conference on Empirical Methods in Natural Language Processing,
pages 9134–9148, 2022.
[79] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and
chatbot arena.Advances in neural information processing systems, 36:46595–46623, 2023.
14

[80] Ruiwen Zhou, Yingxuan Yang, Muning Wen, Ying Wen, Wenhao Wang, Chunling Xi, Guoqiang
Xu, Yong Yu, and Weinan Zhang. Trad: Enhancing llm agents with step-wise thought retrieval
and aligned decision. InProceedings of the 47th International ACM SIGIR Conference on
Research and Development in Information Retrieval, pages 3–13, 2024.
[81] Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan,
and Jimmy Ba. Large language models are human-level prompt engineers. InThe eleventh
international conference on learning representations.
[82] Yuchen Zhuang, Xiang Chen, Tong Yu, Saayan Mitra, Victor Bursztyn, Ryan A Rossi, Somdeb
Sarkhel, and Chao Zhang. Toolchain*: Efficient action space navigation in large language
models with a* search.arXiv preprint arXiv:2310.13227, 2023.
15

A Related Work
LLM Agents.Empowered by LLMs, agents have experienced rapid growth and demonstrated
remarkable performance across a wide range of tasks, including goal reasoning and action execu-
tion [59].For instance, LLMs have empowered embodied agents [ 7] with perception, interaction,
and planning skills for versatile operation in virtual and physical environments [ 27]. To address
the long-horizon interaction tasks, existing methods can be divided into two categories: fine-tuning-
based and fine-tuning-free methods. To obtain a refined language model agent, fine-tuning-based
methods [49, 64, 48, 42, 51] enhance decision-making capabilities by tuning LLMs from expert
demonstrations or exploration [6, 73, 60, 42]. Another line of work incroporates external tools/models
to gain improvements, such as structure search [70, 1, 11, 82] and retrieval [61, 15, 80]. These meth-
ods typically guide LLM agents by incorporating external knowledge. For instance, structure search
offers feedback from the environment [60], while retrieval selects optimal actions by comparing them
to offline successful trajectories [15].
Graph in LLM Reasoning.To enhance the reasoning capacity of LLM, recent works [70, 1, 55], such
as chain-of-thoughts [56], are proposed. These methods essentially decompose the LLM’s reasoning
into nodes and edges, where nodes represent entities and edges represent thought processes [ 1],
thereby modeling interactive relationships. Leveraging these relationships can enhance the LLM’s
reasoning capabilities. Alternatively, explicit graph structures like knowledge graphs [31] can serve
as external knowledge bases to guide reasoning, such as GraphRAG [36, 29, 21], Knowledge Graph
Question Answering (KGQA) [18, 72, 77]. In [ 54], the authors propose that the reasoning ability
of the language model can be seen as an aggregation of the numerous indirect reasoning paths
encountered during pretraining. Moreover, integrating graph structures with LLMs can enhance their
reasoning abilities. For instance, [ 25] embeds knowledge graph representations directly into LLM
tokens as graph semantics, enabling the model to incorporate structural information without relying
on prompt engineering or extensive fine-tuning. Furthermore, graphs are increasingly used to ground
LLM reasoning in actionable plans and environments. For instance, graphs can structure high-level
subgoals [19], represent physical scenes for failure recovery [74], or facilitate graph-based learning
to improve the planning robustness of LLM agents [58].
B Proofs of Theorem 4.2
Proof.We prove the proof of Theorem 4.2 in several steps.
(1) Sufficiency.Assumption 4.1 states exactly that S d-separates Y from the rest of the observed
variables, i.e. Y⊥ ⊥X\S|S . This is equivalent to the conditional probability factorization
P(Y|X) =P(Y|S). HenceSis a sufficient statistic forYrelative toX.
(2) Bayes risk equality.Given the full inputX, the Bayes classifier and its risk are:
h∗ X (x) = arg max c∈{1,...,C} P(Y=c|X=x),andR ∗(X) =E  1{h∗ X (X)̸=Y}  .
BecauseP(Y|X) =P(Y|S), the Bayes posterior and classifier can be written usingSonly:
h∗ X (x) = arg max c P(Y=c|S= Φ g(x))≡h ∗ S(Φg(x)).
Therefore R∗(X) =R ∗(S): no additional reduction in Bayes risk is possible by observing X instead
ofS.
(3) Information-theoretic ordering.For any representation U= Φ(X) , consider the Markov chain
Y→X→U . By the data processing inequality,I(Y;U)≤I(Y;X) . Because S is a (deterministic)
function ofXand suffices forY, we also haveI(Y;S) =I(Y;X). HenceI(Y;U)≤I(Y;S).
A standard information-theoretic lower bound relates classification error to the remaining uncertainty
H(Y)−I(Y;U) . Therefore a representation with strictly larger mutual information with Y yields a
strictly smaller lower bound on achievable error; hence if I(Y;S)> I(Y;U) then R∗(S)< R∗(U).
16

(4) Information-Theoretic Sample Complexity.We now derive the lower bound on the number
of samples m required to achieve an expected classification error ϵ. Let the true class label Y∈
{1, . . . , C}be uniformly distributed, such that the initial entropy is H(Y) = logC . Let ˆY be the
predicted label derived from a dataset ofmindependent samplesS m ={X 1, . . . , Xm}.
By Fano’s Inequality, the conditional entropy of the true label given the prediction is bounded by the
probability of errorϵ=P( ˆY̸=Y):
H(Y| ˆY)≤H(ϵ) +ϵlog(C−1)
To simplify the bound, we upper-bound the binary entropy H(ϵ)≤1 (assuming logarithms are
base-2) andlog(C−1)<logC, yielding:
H(Y| ˆY)<1 +ϵlogC
Since the prediction ˆY is a function of the data Sm, they form a Markov chain Y→S m → ˆY . By
the Data Processing Inequality, H(Y|S m)≤H(Y| ˆY) . Furthermore, by the definition of mutual
information, H(Y|S m) =H(Y)−I(Y;S m) = logC−I(Y;S m). Substituting these into the
relaxed Fano bound gives:
logC−I(Y;S m)<1 +ϵlogC
Rearranging to isolate the mutual information:
I(Y;S m)>(1−ϵ) logC−1
Assuming the m samples are drawn independently, the total information gained about Y from Sm is
bounded by m times the information gained from a single representation X, such that I(Y;S m)≤
mI(Y;X). Substituting this upper bound yields:
m·I(Y;X)>(1−ϵ) logC−1
m≳ (1−ϵ) logC−1 I(Y;X)
Having established this general lower bound, we substitute the representations from Section 4 to
obtain the sample complexity for the respective models:
mg ∝ (1−ϵ) logC−1 I(Y;S) , m seq ∝ (1−ϵ) logC−1 I(Y;U)
From paragraph (3), we established that I(Y;S)≥I(Y;U) . Because the mutual information term
resides in the denominator, a larger information capacity requires fewer samples to achieve the same
error threshold ϵ. It directly follows that mg ≤m seq, with strict inequality if I(Y;S)< I(Y;U) .
This completes the proof.
C Detailed Implementation
C.1 Error Definition
As described in Section 2, we utilize the milestone state definition to detect the errors, which is based
on the previous actions and goals. Besides, we also consider the repeated action as an error. In this
work, we define the error using the following categories:
• No Error (N.E.): The current action goes directly towards the next milestone state.
• Illegal Action (I.A.): The current action is not a valid action for the current environment.
• Repeated Action (R.A.): The current action has been done in the trajectory, and the results are the
same.
• Incorrect Target (I.T.): The current action causes the agent to grab a wrong object or move to a
wrong destination.
17

Table 6: Action error statistic information of datasets.
Train and Validate Test
Agent N.E. I.A. I.T. R.A. P.M. C.M. N.E. I.A. I.T. R.A. P.M. C.M.
AlfWorld
GPT4o-mini 746 4410 410 51 403 2187 245 1546 126 14 179 771
Qwen2.5 804 5612 544 552 2825 1105 268 1838 171 173 1082 351
Gemma3 804 2186 583 237 3334 1120 268 932 213 96 1150 367
TextWorld
GPT4o-mini 240 181 81 70 549 63 80 76 35 32 343 37
Qwen2.5 240 298 67 88 214 60 80 218 46 42 142 30
Gemma3 240 146 57 50 244 49 80 26 43 23 151 31
ScienceWorld
GPT4o-mini 601 4943 57 72 369 186 288 2924 13 21 306 57
Qwen2.5 600 4332 23 59 383 54 288 1778 12 11 149 11
Gemma3 600 3399 37 263 65 60 288 1953 8 127 21 42
TravelPlanner
GPT4o-mini 12441 507 41 394 41 12 4210 177 24 127 3 0
Qwen2.5 9362 3731 143 502 37 18 2826 1181 57 220 14 10
Gemma3 9341 3734 140 547 35 20 2821 1174 61 216 13 10
• Precondition Not Met (P.M.): The current action is valid, but it can only be executed when the
agent has finished a specific action.
• Condition Met, Action Not Taken (C.M.): The current action is a valid action, but not necessary for
the next milestone state or goal.
Notably, these error definitions are not specific to any particular environment. As a result, they do not
include environment-related errors, such as tool misuse, which makes them easy to extend to other
environments.
To further illustrate the error space, we provide an example. Given a task such as “clean a plate and
put it on the countertop”, the key states include: (1) a plate is found, (2) the plate is cleaned, and
(3) the plate is placed on the countertop. Suppose the action-only trajectory is “go to desk, go to
basin, pick up plate 1, clean plate 1, go to desk 1.” In this trajectory, the label for “go to desk 1” is
“Condition Met, Action Not Taken.” Making this prediction only requires tracing back to the action
“clean plate 1”, because after that action, the plate becomes clean. This example demonstrates how
the error space is defined and why the Markov blanket assumption is reasonable.
Table 7: Action and trajectory statistic information of datasets. GPT4o. is short for GPT4o-mini.
(Sub) Trajectory Action
Agent train validate test train validate test
AlfWorld
GPT4o. 7386 821 2881 74127 8286 28704
Qwen2.5 10297 1145 3883 63522 7288 25020
Gemma3 7437 827 3026 41432 4817 16352
TextWorld
GPT4o. 1065 119 603 9760 1057 4706
Qwen2.5 870 97 558 10286 1161 5923
Gemma3 707 79 354 7131 721 4174
ScienceWorld
GPT4o. 5605 623 3609 30415 3506 16497
Qwen2.5 4905 546 2249 17557 1818 5277
Gemma3 3981 443 2439 17713 1953 7659
TravelPlanner
GPT4o. 12055 1340 4541 82691 9201 31017
Qwen2.5 12413 1380 4308 72468 7996 23604
Gemma3 12435 1382 4295 72260 8079 23547
18

C.2 Dataset Construction
To build the datasets, we use three LLMs for each environment. For AlfWorld, TextWorld, and
ScienceWorld, we use GPT4o-mini [34], Qwen2.5 [66], and Gemma3 [46] to construct the Agent.
We first run the training tasks to collect agent trajectories and obtain the expert/golden trajectories
from the environments. Each full trajectory will be divided into several subtrajectories by the
sequence of actions. Notably, the expert/golden trajectories indicate successful trajectories, which
can be obtained by random sampling or provided by benchmarks. We then utilize an LLM to analyze
the trajectory to generate initial labels. Finally, we use a rule-based script to filter and remap labels.
The Gemma3 was used for the initialization labels. For the detailed prompts, we provide them
at the end of the Appendix. Then we filter and map the label manually. For AlfWorld, we use
the AgentBoard dataset, with 402 tasks for training and validation, and 134 tasks for testing. The
TextWorld environment comprises eight subsets; for each, we use 10 variants for training/validation
and 5 variants for testing. Similarly, ScienceWorld has 30 subsets, with the first 10 variants used
for training/validation and the subsequent 5 variants for testing. For all three of these environments,
expert trajectories serve as “No Error” samples. The TravelPlanner dataset contains three levels of
tasks (easy, normal, and hard), with 880 tasks for training/validation and 300 tasks for testing (100
for each level). The detailed statistics information is available in Table 7 and 6. All data and code
will be released once the paper is accepted.
C.3 Agent Implementation
In this paper, we follow the AgentBoard [ 5] to build interactive agents for AlfWorld, TextWorld,
and ScienceWorld. Each task is capped at 50 steps. At every step, we supply the LLM with the full
history of observations and actions to support decision-making, along with a short demonstration
included in the prompt to improve performance. For AlfWorld and TextWorld, we also provide the
list of available action options derived from the environment. In ScienceWorld, however, the action
space is prohibitively large, so we instead provide an action template. For TravelPlanner, we adopt the
two-stage methods from open-source implementation2. The detailed prompts used in our experiments
are provided at the end of the Appendix.
C.4Trajectory Graph CopilotImplementation
In this paper, we implementTrajectory Graph Copilotusing in-context learning with carefully
designed prompts. At each step, the agent is allowed up to three attempts to satisfy the criteria defined
inGraph Debugger. If a step fails, we provide additional feedback to guide the regeneration of actions,
including the error type, its definition, and representative failure examples. In our experiments, we
include three failure examples by default to ensure sufficient guidance while maintaining prompt
efficiency. To reduce false positives, we apply a confidence threshold of 0.6 to filter out unreliable
detection results. For the baseline methods, we adopt the same three-attempt strategy for a fair
comparison. However, since methods such as retrieval-based approaches and LLM-as-a-judge do not
produce explicit confidence scores, this threshold cannot be applied to them. Within this iterative
feedback loop, we incorporate potential error information directly into the prompt to enable more
informed decision-making and refinement.
The detailed prompt templates are provided at the end of the Appendix, with redundant components
omitted where they overlap with the agent implementation described earlier. This design ensures both
reproducibility and clarity while avoiding unnecessary repetition.
C.5 Detection Implementation
In this paper, we employ a three-layer GCN [16] with edge attributions as the graph-based detector,
with hidden dimensions of [768, 512, 6]. We use AdamW [28] as the optimizer, with a learning rate
of 1e-3 and a weight decay of 5e-5. The TF-IDF baseline is implemented using scikit-learn 3 with
default hyperparameters. For Bert, we fine-tune the model using AdamW with a learning rate of 5e-5.
For the retrieval-based and RAG methods, we use the training set as the retrieval database to ensure a
2https://github.com/OSU-NLP-Group/TravelPlanner
3https://github.com/scikit-learn/scikit-learn
19

consistent and fair comparison across methods. Additionally, for both the RAG and LLM-as-a-Judge
approaches, we provide the full prompt templates at the end of the Appendix.
Overall, we keep the training settings and hyperparameters consistent across different methods
whenever applicable, in order to ensure a fair and controlled evaluation of performance differences.
C.6 Test-Time Graph Injection and Inference
During the testing phase or when applyingGraph Debuggeras a real-time diagnosis sandbox for
LLM agents, the framework operates in an inductive setting to evaluate previously unseen trajectories.
To ensure consistency between the training and inference phases, we dynamically integrate novel test
trajectories into the pre-established action-centric graph without retraining the GNN detector.
Let G= (V,E) denote the graph constructed from the training set, where the node setV encompasses
the unique actions and the training trajectories.
Given a novel test trajectoryξtest /∈ Tgenerated by the agent, we first utilize NLTK and the pretrained
Bert model to process and initialize the representations of its constituent actions and observations. To
embed ξtest, we perform a dynamic graph injection operation by introducing a new trajectory node
vtest. The augmented node set is defined as V ′ =V ∪ {vtest}.The topological relationships for vtest are
established by linking it to its corresponding action nodes vi ∈ A, following the exact same heuristic
defined in Equation 1. If the new trajectory contains previously unseen actions, they are initialized
and added toA. The augmented adjacency matrixA ′ is formally updated as:
A′ij=
( 1ifAij= 1in the training graph
1v i ∈ A,andvj =v test,wherev i ∈ξ test
0otherwise
(4)
Once the augmented graph and A′ are constructed, we apply our trained GNN detector to perform K
rounds of message passing. For computational efficiency during step-level action debugging, this
message passing can be localized to the K-hop neighborhood of vtest. The representation of the test
trajectory, h(K) test , is aggregated inductively from its constituent actions. Finally, we apply the softmax
function to obtain the error probability vector Ztest =softmax(h (K) test ), which provides immediate
feedback for the agent’s subsequent decision-making.
C.7 Compute Resources Used
The experiments in this paper involve both open-source LLMs (Qwen2.5-14B, Gemma3-27B) and
commercial LLMs (GPT-4o, GPT-4o-mini). For the commercial models, inference is performed via
the Azure OpenAI Service API, called from standard Linux machines using CPU-only execution,
with no dependency on local GPU availability.
All open-source LLMs are deployed locally and served on a single NVIDIA A100 GPU (80GB
VRAM) at a time, ensuring consistent and reproducible runtime characteristics across model families.
Each model is loaded and evaluated independently to isolate performance measurements and avoid
cross-model interference. The full hardware platform consists of a Linux system equipped with
eight NVIDIA A100 GPUs, running CUDA 12.8, Python 3.10, and PyTorch 2.6.0, providing ample
capacity for iterative experimentation and parallel development workflows.
D Extensive Results
D.1 Quality of Datasets
To verify the quality of the dataset, we conduct experimental validation in this section. While
human-based evaluation provides the most reliable form of quality assessment, the sheer volume of
trajectories makes it impractical for large-scale applications. To address this limitation, we employ
two different LLMs for automatic annotation and introduce a cross-evaluation strategy to improve
label quality and robustness.
Specifically, we use a larger and independent foundation model, GPT-OSS-120B, to re-annotate
the ScienceWorld trajectories that were originally generated by Qwen2.5 and Gemma3. In total,
20

Table 8: Quality and robustness analysis of dataset on ScienceWorld. The trajectories are generated by
Qwen2.5 and Gemma3. The annotations are generated by GPT-OSS-120B(GPT-OSS) and Gemma3.
Qwen2.5 Trajectory Gemma3 Trajectory
Annotation Gemma3 GPT-OSS Gemma3 GPT-OSS
No Error(N.E.) 20.49% 16.57% 12.62% 13.02%
Illegal Action(I.A.) 68.10% 68.67% 77.22% 76.82%
Repeated Action(R.A.) 8.00% 7.64% 8.16% 8.09%
Incorrect Target(I.T.) 0.59% 0.59% 0.38% 0.69%
Precondition Not Met(P.M.) 0.78% 0.86% 0.74% 0.48%
Condition Met, Action Not Taken(C.M.) 2.04% 5.07% 0.87% 0.91%
this process covers 11,762 actions annotated with Gemma3. We then compare the resulting class
distribution with that produced by our primary annotation model. As shown in Table 8, the distribution
of error labels remains highly consistent across different models. We further calculate Cohen’s Kappa
κ as the agreement metric. For Qwen2.5 and Gemma3, we have the results 0.8817 and 0.8907. This
consistency suggests that our annotation pipeline is robust and not overly sensitive to the biases or
noise introduced by any single model. Furthermore, it provides empirical evidence that our dataset
maintains stable labeling characteristics even under model variation, supporting its reliability for
downstream evaluation and training.
D.2 Error Detection
In Section 5.1, we provide the detection results across four benchmarks. To facilitate a more
comprehensive comparison of performance across each benchmark and LLM backbone, we present
results in Table 9. We observe that our method consistently outperforms all baselines across all four
benchmarks and three LLM Agents, demonstrating the broad effectiveness and generalizability of
our approach.
Table 9: Extended action error detection marginal average results(%), the metric is the average
accuracy(↑). GPT4o. is short for GPT4o-mini. The best performances are inbold, and the second-
best method is underlined.
Method AlfWorld TextWorld ScienceWorld TravelPlanner GPT4o. Qwen2.5 Gemma3
Text Classification
TF-IDF 62.92 51.86 80.73 74.60 74.02 65.67 62.90
Bert 57.00 55.91 80.90 74.18 73.23 65.61 62.16
Retrieval
MiniLM 45.27 48.43 74.73 69.85 65.69 56.86 56.17
E5 51.82 45.61 74.68 69.44 67.34 54.36 59.47
GTR 53.50 48.11 74.97 69.72 68.64 55.85 60.24
RAG
GPT4o 59.43 57.02 71.71 64.14 64.99 60.72 63.52
Gemma3 60.04 57.70 78.15 38.01 57.37 59.06 59.00
Qwen2.5 54.31 43.55 68.43 28.92 46.34 48.92 51.15
LLM Zero-Shot
GPT4o 31.44 45.46 33.36 6.97 28.86 29.10 29.96
Gemma3 31.26 42.40 24.51 3.64 25.13 25.60 25.62
Qwen2.5 17.82 33.02 20.13 8.19 19.53 19.67 20.17
LLM One-Shot
GPT4o 24.12 48.17 12.65 7.06 22.89 20.40 25.72
Gemma3 26.89 37.64 15.20 3.73 20.52 19.90 22.19
Qwen2.5 17.25 37.48 23.51 8.44 22.78 19.97 22.26
LLM Three-Shot
GPT4o 27.76 45.09 14.22 3.45 24.71 18.32 24.86
Gemma3 27.92 35.52 33.66 5.53 25.05 29.39 22.54
Qwen2.5 17.40 36.28 27.71 4.01 22.53 20.87 20.66
Ours 66.91 65.29 85.27 76.11 77.89 71.02 71.27
21

Extensive Statistical Significance Analysis.To further assess the robustness of the detection
methods under varying conditions, we repeat the experiments five times and report the mean results
with error bars on TextWorld, which serves as a representative benchmark for this analysis. As shown
in Table 10, our method consistently outperforms all baselines across runs, with a small variance,
confirming the stability of our approach and its alignment with our theoretical analysis.
Table 10: Statistical significance analysis of action error detection on TextWorld.The best perfor-
mances are inbold, and the second-best method is underlined .
Accuracy/Micro F1 Macro F1
Method GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3
Text Classification
TF-IDF 0.6365±0.00160.4996 ±0.00410.4045±0.01600.3399±0.00930.2712±0.00420.2256±0.0074
Bert 0.6368 ±0.00970.4996 ±0.05010.4345±0.04930.4177±0.01200.3897±0.03800.3711±0.0283
Retrieve
GTR 0.5322±0.00730.3018±0.00090.5322±0.00730.4257±0.00410.2472±0.00560.4257±0.0041
RAG
Gemma3 0.6232±0.00300.5183±0.00660.6124 ±0.00720.4217±0.00520.4649±0.00360.4952±0.0052
LLM Zero-Shot
Gemma3 0.4732±0.00300.3427±0.00290.4492±0.00000.2522±0.00000.2462±0.00090.2680±0.0000
LLM One-Shot
Gemma3 0.3755±0.07550.2620±0.07410.3090±0.05540.2157±0.04080.1824±0.06060.1799±0.0442
LLM Three-Shot
Gemma3 0.1158±0.04570.3194±0.05050.1876±0.09070.0994±0.04410.1932±0.06120.1474±0.0694
Ours 0.6872±0.0091 0.5810±0.0133 0.6316±0.0229 0.4226±0.0160 0.4298±0.0063 0.5283±0.0199
D.3 Feedback Evaluation
Detailed Results.In Section 5.1, we provide the average results across four benchmarks and three
LLM agents; in this subsection, we present a more granular breakdown. As the PR results in Table 11
show, our method achieves 7 best and 4 second-best results across all configurations, demonstrating
the consistent advantage ofTrajectory Graph Copilot. Furthermore, in most cases our method
outperforms the vanilla baseline, confirming that incorporating feedback information effectively
boosts the agent’s task completion performance.
Table 11: Action error feedback evaluation results. The metric is PR( ↑). GPT4o. is short for
GPT4o-mini. The best performances are inbold, and the second-best method is underlined .
AlfWorld TextWorld ScienceWorld TravelPlanner
Method GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3
Vanilla 18.66 40.30 6.72 45.00 65.00 65.00 77.26 75.69 86.81 79.33 54.67 55.00
Text Classification
+TF-IDF 22.22 31.34 12.69 65.0057.50 65.00 71.03 77.93 86.39 80.67 60.67 97.00
Retrieve
+GTR 15.67 32.09 8.96 37.5072.5067.50 67.32 79.86 83.33 80.00 59.33 95.33
RAG
+Gemma3 20.71 37.31 2.99 50.0072.5070.00 70.0886.1187.50 82.6759.67 96.33
LLM Zero-Shot
+GPT4o 18.66 33.5817.1652.50 65.00 72.5071.35 80.41 85.42 80.67 57.33 92.67
+Ours 26.12 44.78 12.69 46.51 65.00 75.00 94.44 82.64 94.44 80.67 67.67 97.00
Grounding Ratio Analysis.Regarding the GR, as shown in Table 12, our method achieves the
second-best GR overall. It is important to note that GR only indicates whether an action lies within
the valid action space, but does not guarantee its correctness. Compared to the vanilla baseline,
all methods exhibit varying GRs, suggesting that the feedback mechanism encourages the agent to
explore alternative actions rather than converging on familiar ones. Moreover, GR is jointly influenced
by task characteristics and the reasoning ability of the underlying LLM. For instance, in TextWorld,
the action space contains many variants, making it inherently harder to generate grounded actions
even with feedback; in contrast, TravelPlanner features a more constrained action space, leading to
improved GR under feedback. We also observe model-dependent behavior: for GPT4o-mini and
22

Qwen2.5-14B, the GR is lower than the vanilla baseline, whereas Gemma3-27B shows the opposite
trend, suggesting that stronger reasoning capabilities allow the model to better leverage feedback
for grounded action generation. Importantly, a brute-force guessing strategy would typically yield
a similar PR but a lower GR compared to the baseline; however, we do not observe this pattern in
our results, confirming that the feedback mechanism does not reduce to random guessing. To further
confirm the statistical significance of these findings, we repeat the experiments five times and report
results with error bars in Table 10, where our method consistently outperforms all baselines with low
variance.
Another notable observation is that GR does not directly correlate with PR. For instance, in TextWorld,
although the GR of all methods falls below the vanilla baseline, the PR still improves. This is expected,
as the feedback mechanism does not directly modify the LLM’s parameters or decoding behavior, but
instead encourages the generation of more diverse candidate actions, even when some contain errors.
This diversity ultimately benefits task progress, decoupling PR gains from GR, and highlighting that
grounding accuracy alone is insufficient as a proxy for overall agent performance.
Table 12: Action error feedback evaluation results. The metric is GR( ↑). GPT4o. is short for
GPT4o-mini. The best performances are inbold, and the second-best method is underlined .
AlfWorld TextWorld ScienceWorld TravelPlanner
Method GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3 GPT4o. Qwen2.5 Gemma3
Vanilla 73.8768.0262.4995.66 86.79 91.07 77.3549.62 70.22 97.71 74.14 74.20
Text Classification
+TF-IDF 74.22 58.12 63.04 53.33 46.07 48.02 71.0358.69 75.0397.83 75.58 99.58
Retrieve
+GTR 74.73 54.89 64.66 58.11 43.84 52.58 67.32 55.42 72.16 97.73 76.48 99.21
RAG
+Gemma3 75.78 61.8891.1957.35 44.24 52.33 70.08 57.58 71.41 97.83 76.04 99.53
LLM Zero-Shot
+GPT4o75.8457.55 65.88 55.20 46.57 52.82 71.35 52.12 74.12 97.76 75.36 98.52
+Ours 71.19 62.33 66.97 67.89 62.78 89.79 69.09 57.26 73.55 98.07 81.23 99.81
Detailed Results of Deliberate Prompting-based LLM agents.We further provide the PR and
GR in Table 13. As mentioned in Section 5.2, our method mitigates these limitations, which highly
rely on reasoning capabilities of the LLM, by incorporating structured external feedback, allowing
the model to self-correct more reliably without depending solely on its parametric knowledge. As a
result, our approach remains robust even when applied to smaller backbone models.
Table 13: Comparison between ours and modern prompts on TextWorld. The best performances are
inbold.
Pass Ratio(%) Ground Ratio(%)
Method Qwen2.5 Gemma3 Qwen2.5 Gemma3
ReAct 62.50 70.00 69.86 86.60
Reflexion 60.00 67.5071.1879.60
Ours 65.00 75.00 62.78 89.78
Table 14: Statistical significance analysis of error feedback on TextWorld.The best performances are
inbold.
Pass Ratio(%) Ground Ratio(%)
Method Qwen2.5 Gemma3 Qwen2.5 Gemma3
Vanilla 65.00±6.5270.50±5.5088.77±2.9891.49±3.42
Text Classification
+TF-IDF 61.50±3.3567.50±7.0740.49±2.3546.81±1.51
Retrieve
+GTR 67.50±6.1273.50±6.7541.16±1.7351.52±1.13
RAG
+Gemma369.50±3.7171.94±5.3640.81±0.8252.66±1.42
+Ours 64.00±1.22 76.00±3.74 73.61±6.74 87.15±4.78
23

Statistical Significance Analysis.To conduct the variance analysis, we perform experiments
reporting error bars for feedback-improvement evaluations on the TextWorld environment. We repeat
each experiment five times and report the mean and standard deviation. The results are presented
in Table 14. As the results demonstrate, our method achieves robust and stable performance across
all runs, with low variance pass ratio consistently aligned with the findings reported in previous
experiments. This confirms that our method is not sensitive to random initialization or stochastic
variation, further validating the reliability of our reported results.
D.4 Ablation Study
Graph Building.In Section 5.3, we provide an analysis of two types of graphs and node embed-
ding initialization. In this section, we further analyze the distinction between action-centric and
observation-centric graph designs. As shown in Table 15, in ALFWorld, when modeling actions as
nodes, the resulting graph scale is smaller than when using observations as nodes. However, even
with Qwen2.5-14B, the number of unique actions exceeds that of observations, while the number
of edges remains smaller. This suggests that an action-centric graph yields a more compact yet
informative structure.
From the perspective of graph construction, the observation space is significantly larger than the
action space. Treating observations as nodes would therefore greatly increase the graph size and
complexity, imposing additional computational overhead and making it harder for the model to
efficiently capture task-relevant relationships. Using observations as nodes and actions as edges
tends to produce a much sparser graph, which may limit the model’s ability to learn meaningful
representations. In contrast, our design, where actions serve as nodes, encourages denser connectivity
and richer structural information, enabling the model to better capture the sequential and relational
nature of agent decision-making.
Table 15: The number of nodes/edges between action-centric/observation-centric graphs of the
AlfWorld environment.
GPT4o-mini Qwen2.5-14B Gemma3-27B
node(action)/edge(observation) 682/2,900 1,825/3,868 623/1,983
node(observation)/edge(action) 1,154/5,938 910/4,404 834/4,064
Detailed Results of Prompt Ablation Study.We provide the detailed results of the feedback
integration of PR and GR in Table 16.
Table 16: Ablation study of feedback integration mechanisms on TextWorld. In the table, “exp.” is
short for “explanations”. The best performances are inbold.
Pass Ratio(%) Ground Ratio(%)
Method Qwen2.5 Gemma3 Qwen2.5 Gemma3
in trajectories 57.50 70.00 52.49 86.69
in system 60.0075.0057.41 88.10
in user 65.00 75.00 62.78 89.79
in user w/o exp. 62.50 72.5071.2484.79
Detailed Hyperparameter Study of Feedback.In Section 5.3, we examine the impact of two key
hyperparameters inTrajectory Graph Copilot: the maximum number of attempts and the confidence
threshold. We provide the detailed results in Table 17. In this section, we further investigate the role
of error samples in enhancing performance. Table 18 summarizes the results under two settings: with
and without error samples. Our findings show that, without error samples, increasing the number of
attempts leads to consistent improvements in PR performance, while GR remains largely unchanged.
When error samples are included, PR performance also improves; however, adding more samples
does not yield further gains and, in fact, leads to a decline in GR. This suggests a trade-off: while
error samples provide useful information for correction, an excessive number of them may introduce
noise or bias, ultimately hindering generalization.
24

Table 17: Ablation study on confidence threshold and maximum attempts of feedback evaluation.
TextWorld(PR)ScienceWorld(PR)TextWorld(GR)ScienceWorld(GR)
Hyperparameter Qwen2.5 Gemma3 Qwen2.5 Gemma3 Qwen2.5 Gemma3 Qwen2.5 Gemma3
Vanilla 65.00 65.00 75.69 86.81 86.79 91.07 49.62 70.22
Threshold-0.6
+ 1 Attempts 65.00 65.00 75.69 86.81 86.79 91.07 49.62 70.22
+ 2 Attempts 67.50 72.50 96.81 94.44 65.05 93.09 60.59 71.67
+ 3 Attempts 65.00 75.00 82.64 94.44 62.78 89.79 57.26 73.55
+ 5 Attempts 62.50 70.00 82.64 95.92 58.02 90.56 57.51 73.71
+ 7 Attempts 70.00 72.50 86.11 93.75 64.71 91.71 59.91 73.47
3 Attempts
+ Threshold-0.20 62.50 67.50 77.78 96.53 60.10 90.80 56.59 75.32
+ Threshold-0.35 65.00 75.00 88.36 96.53 58.16 92.46 57.91 72.91
+ Threshold-0.50 62.50 77.50 87.50 93.06 55.16 92.20 58.82 73.36
+ Threshold-0.65 57.50 75.00 86.11 94.44 58.31 89.11 61.28 74.72
+ Threshold-0.80 65.00 72.50 88.19 86.11 63.36 92.43 58.74 74.91
Table 18: Ablation study on error samples of feedback evaluation.
TextWorld(PR)ScienceWorld(PR)TextWorld(GR)ScienceWorld(GR)
Hyperparameter Qwen2.5 Gemma3 Qwen2.5 Gemma3 Qwen2.5 Gemma3 Qwen2.5 Gemma3
Vanilla 65.00 65.00 75.69 86.81 86.79 91.07 49.62 70.22
Zero-Shot + Threshold-0.6
+ 2 Attempts 60.00 72.50 88.19 93.06 71.07 90.50 66.28 72.51
+ 3 Attempts 50.00 77.50 87.50 94.44 69.20 89.28 63.64 73.86
+ 5 Attempts 50.00 70.00 91.67 91.67 67.97 92.16 66.28 74.49
3 Attempts + Threshold-0.6
+ One Shot 60.00 72.50 94.44 97.22 71.19 88.55 65.87 74.20
+ Three Shots 65.00 75.00 82.64 94.44 62.78 89.79 57.26 73.55
+ Five Shots 65.00 77.50 82.64 93.06 55.82 92.01 56.21 73.29
Noise Injection.To evaluate the robustness of our method, we conduct ablation experiments on the
feedback component under varying levels of input perturbation. Specifically, we inject random noise
into the detection results at noise intensities of 0.0, 0.2, 0.4, 0.6, 0.8. The results are presented in
Figure 5. As the noise intensity increases, the model’s performance gradually decreases, which is
expected given that higher noise levels corrupt the quality of the feedback signal. Nevertheless, our
method maintains competitive performance at moderate noise levels, demonstrating that it is not
overly sensitive to minor perturbations in the feedback. This highlights the resilience of our approach
and suggests that it can generalize well even when the feedback source is imperfect or noisy.
Figure 5: The pass ratio (%) and ground ratio (%) results on random noise injection.
D.5 Prompts
In this subsection, we provide the prompts used in experiments.
LLM Prompt for AlfWorld, TextWorld, ScienceWorld Action Error Label
"""
You are a top-level expert AI agent trajectory analyst. Your
primary task is to analyze the ’CURRENT STEP’ of an agent’s
trajectory and identify the single most likely error.
25

**Crucial Constraint **: The agent is unfamiliar with the
environment, so it might take some time to explore and find
destinations and objects. Therefore, its actions should be judged
based on the **Overall Task Goal **, not by strictly following
the expert plan. The expert plan is only a reference for a possible
successful path. You can know how much the agent has inferred the
environment from the observation and extract the best possible
action from the observation.
**Output Format **: Your entire response MUST be a single, valid JSON
object. Do not include any text, explanations, or markdown
formatting before or after the JSON object.
The JSON object must contain exactly three keys:
- "has_error": (boolean) true if there is an error(No Error is not
an error), otherwise false.
- "error_type": (string) One of the specified error types below.
- "analysis": (string) A concise, one-sentence explanation for the
error.For example, for a "Precondition Not Met" error, a good
analysis would be "The agent tried to place an object that it was
not holding in its inventory."
**Types**:
- "No Error": The action is logical and contributes to the task
goal.
- "Precondition Not Met": The action is valid but cannot be gain
progress because a necessary prior condition is not met (e.g.,
trying to ’put’ an object that is not currently held).
- "Condition Met, Action Not Taken": A critical step was available,
necessary to progress and the agent already observed the condition,
but the agent performed an irrelevant or less optimal action
instead (e.g., finding the target object but not picking it up).
- "Incorrect Target": The action is performed on the wrong object or
at the wrong location (e.g., picking up a ’cloth’ instead of the
required ’soapbottle’).
- "Repeated Action": The action is part of a sequence that was
already performed and without any progress.
--- CONTEXT ---
1. **Overall Task Goal **:
"{task_goal}"
2. **Expert’s Suggested Plan (for reference only, may be flawed) **:
{expert_plan}
3. **Trajectory History (Recent Steps) **:
{trajectory_history}
4. **CURRENT STEP TO ANALYZE **:
- Action: "{current_action}"
--- YOUR RESPONSE (JSON ONLY) ---
"""
LLM Prompt for TravelPlanner Action Error Label
prompt = f"""Please analyze the following action in a travel
planning trajectory and classify it into one of these error
categories. Before giving a conclusion, please read the Agent
thought(indicate the next step) and observation, reason the
state of the agent. In general, the action should be consistent
with the thought.
ERROR CATEGORIES:
1. No error: There is no error during the trajectory
2. Illegal Action: The action is not a valid action
3. Repeated Action: The action has been done in the trajectory, and
there is nothing updated. It is not necessary.
26

4. Incorrect Target: The action is not aligned with the goal, for
example the thought would go to place A, but the action searches
place B.
5. Precondition Not Met: The action is valid, but it can’t be done
right now, because some condition is not met. For example, the
current information does not contain the hotel information, so it
is not a good time to make final plan. Or the current information
does not have a valid plan due to the constraints, such as money.
6. Precondition Met, Action Not Taken: The information needed is
collected. The agent can have a valid plan according to the
information, but it did not make the final plan immediately.
TASK DESCRIPTION:
{current_step.get(’task_description’, ’N/A’)}
TRAJECTORY CONTEXT:
{context_str}
CURRENT STEP TO ANALYZE:
Agent Thought: {current_step.get(’thought’, ’N/A’)}
Action: {current_step.get(’action’, ’N/A’)}
Based on the context and current step, return strict JSON with
two keys: label and reason. The label must be exactly one of the
categories above (e.g., "No error", "Illegal Action", etc.). The
reason should be a brief phrase explaining why.
Attention: Only the raw json."""
Agent Prompt for AlfWorld environment
messages = [{
"role": "system",
"content": f"""You are an agent in a text-based ALFWorld environment,
performing a household task.\n
For each step, generate one action based on the task description,
action Options, current observation, and the plan.\n
Please think about the environmental state from the historical
trajectories before you give the answer.\n
Do not generate other text except the action itself.
One action per step.\n
The action output format must be ##Action: XXX ##,
where XXX is the action.\n\n
Example:\n> Observation: You are in the middle of a room.
Looking quickly around you, you see a bathtubbasin 1, a cabinet 2,
a cabinet 1, a countertop 1, a garbagecan 1, a handtowelholder 1,
a sinkbasin 1, a toilet 1, a toiletpaperhanger 1, and
a towelholder 1.\n
Your task is to: put a toiletpaper in toiletpaperhanger.\n
> Action: go to toiletpaperhanger 1\n
> Observation: On the toiletpaperhanger 1, you see nothing.\n
> Action: go to toilet 1\n> Observation: On the toilet 1, you see a
soapbottle 1, and a toiletpaper 1.\n
> Action: take toiletpaper 1 from toilet 1\n> Observation: You pick
up the toiletpaper 1 from the toilet 1.\n
> Action: go to toiletpaperhanger 1\n> Observation: On the
toiletpaperhanger 1, you see nothing.\n
> Action: put toiletpaper 1 in/on toiletpaperhanger 1\n"""},
{"role": "user",
"content": f"""
> Task Description: {task_description}
> Action Options: {’,’.join(action_lists)}
> Trajectory History: {’ ’.join(history)}
> Action:"""} ]
27

Agent Prompt for TextWorld environment
messages = [{
"role": "system",
"content": f"""You are an agent in a text-based TextWorld
environment, performing a task.\n
For each step, generate one action based on the task description,
action Options, current observation, and the plan.\n
Please think the environment state from the history trajectories
before you give the answer.\n
Do not generate other text except the action itself. One action
per step.\n
The action output format must be ##Action: XXX ##, where XXX is the
action.\n\n
Example:\n
> Observation: You are in a room. You see a coin, a table,
and a door to the north (open).\n
Your task is to: find and collect a coin.\n
> Action: look\n
> Observation: You see a coin.\n
> Action: take coin\n
> Observation: You take the coin.\n"""},
{"role": "user",
"content": f"""
> Task Description: {task_description}
> Action Options: {’,’.join(action_list)}
> Trajectory History: {’ ’.join(history)}
> Action:""" }]
Agent Prompt for ScienceWorld environment
messages = [ {
role="system",
content=( "You are an agent in a text-based ScienceWorld
environment, performing a task.\n"
"For each step, generate one action based on the task description,
action Options, current observation, and the plan.\n"
"Please think the environment state from the history trajectories
before you give the answer.\n"
"Possible Available Actions contains the OBJ, which can be replace
by object in environment.\n"
"Do not generate other text except the action itself. One action
per step.\n"
"The action output format must be ##Action: XXX ##, where XXX is
the action.\n\n"
"Example:\n
> Observation: This room is called the hallway. In it, you see: a
picture, a substance called air, the agent.\n"
"You also see: doors to other rooms.\nYour task is to: boil water.\n
> Action: look around\n
> Observation: The door is already open.\n
> Action: open door to kitchen\n" ) },
{ role="user",
content=(
f"> Task Description: {task_description}\n"
f"> Action Options: {’,’.join(action_lists)}\n"
f"> Trajectory History: {’ ’.join(history)}\n"
f"> Action:\n" ) } ]
28

LLM Prompt with the Error Feedback
feedback_section = f"\n\nIMPORTANT: We have analyzed
your last time action {action} for the same trajectory and provided
this feedback: {gnn_feedback}\n Do not generate the same action,
{action}, again.\n"
messages = [{...},
{"role": "user",
"content": f"""
> Task Description: {task_description}
> Action Options: {’,’.join(action_lists)}
> Trajectory History: {’ ’.join(history)}
> Action:
{feedback_section} """}]
LLM-as-Judge prompt for Error Detection
prompt = """You are a helpful assistant for classifying
agent actions.Please give the label for the following
input. Here are labels:\n
- No Error: The action is logical and contributes to the task
goal.
- Illegal Action: The action performed an illegal action or has
no effect.
- Precondition Not Met: The action is valid but cannot be gain
progress because a necessary prior condition is not met (e.g.,
trying to ’put’ an object that is not currently held).
- Condition Met, Action Not Taken: A critical step was available,
necessary to progress and the agent already observed the condition,
but the agent performed an irrelevant or less optimal action
instead (e.g., finding the target object but not picking it up).
- Incorrect Target: The action is performed on the wrong object or
at the wrong location (e.g., picking up a ’cloth’ instead of the
required ’soapbottle’).
- Repeated Action: The action is part of a sequence that was
already performed and without any progress.\n """
for shot in shots:
prompt += f"Example:\nInput: {shot[’input’]}\n
Label: {shot[’label’]}\n\n"
prompt += f"Input: {input_text}\nLabel:"
RAG prompt for Error Detection
prompt = "You are a classifier. Given the following examples,
predict the label for the new sample.\n"
for idx, (txt, lbl) in enumerate(retrieved):
prompt += f"Example {idx+1}:\nText: {txt}\nLabel: {lbl}\n"
prompt += f"\nNow,classify this sample:\nText: {X_test[i]}\nLabel: "
29
