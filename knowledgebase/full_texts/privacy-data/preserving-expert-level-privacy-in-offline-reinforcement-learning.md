---
title: Preserving Expert-Level Privacy in Offline Reinforcement Learning
url: https://arxiv.org/abs/2411.13598
category: privacy-data
subcategory: theory
date: 2024-11
venue: arXiv (Cornell University)
authors:
- Navodita Sharma
- Vishnu Vinod
- Abhradeep Thakurta
source: arxiv
pdf_url: https://arxiv.org/pdf/2411.13598
pages: 23
chars: 71897
fetched_at: '2026-11-08T12:57:32+00:00'
kb_version: 1
---

# Preserving Expert-Level Privacy in Offline Reinforcement Learning

Published in Transactions on Machine Learning Research (10/2025)
Preserving Expert-Level Privacy in Offline Reinforcement
Learning
Navodita Sharma* navoditasharma@google.com
Google DeepMind
Vishnu Vinod* vishnuvinod2001@gmail.com
CeRAI, IIT Madras
Abhradeep Thakurtaathakurta@google.com
Google DeepMind
Alekh Agarwalalekhagarwal@google.com
Google Research
Borja Balle bballe@google.com
Google DeepMind
Christoph Dann chrisdann@google.com
Google Research
Aravindan Raghuveeraraghuveer@google.com
Google DeepMind
Reviewed on OpenReview:https: // openreview. net/ forum? id= 2bj0eVgCdO
Abstract
The offline reinforcement learning (RL) problem aims to learn an optimal policy from his-
torical data collected by one or more behavioural policies (experts) by interacting with an
environment. However, the individual experts may be privacy-sensitive in that the learnt
policy may retain information about their precise choices. In some domains like personalized
retrieval, advertising and healthcare, the expert choices are considered sensitive data. To
provably protect the privacy of such experts, we propose a novel consensus-based expert-
level differentially private offline RL training approach compatible with any existing offline
RL algorithm. We prove rigorous differential privacy guarantees, while maintaining strong
empirical performance. Unlike existing work in differentially private RL, we supplement
the theory with proof-of-concept experiments on classic RL environments featuring large
continuous state spaces, demonstrating substantial improvements over a natural baseline
across multiple tasks.
1 INTRODUCTION
Leveraging existing offline datasets to learn high-quality decision policies via offline Reinforcement Learning
(RL) is a critical requirement in many settings ranging from robotics (Fu et al., 2020; Levine et al., 2020)
and recommendation systems (Bottou et al., 2013; Ie et al., 2019; Cai et al., 2017) to healthcare applica-
tions (Oberst & Sontag, 2019; Tang et al., 2022). Correspondingly, there is now a rich literature on effective
techniques (Fujimoto et al., 2019b; Kumar et al., 2019; 2020; Cheng et al., 2022) for learning from such offline
datasets, collected using one or morebehavioural policies. An often overlooked aspect of this literature is,
*These authors contributed equally.
1
arXiv:2411.13598v2  [cs.CR]  23 Nov 2025

Published in Transactions on Machine Learning Research (10/2025)
stable preﬁx unstable tail
ADR
DΠ stable
DΠ unst
SGD
DP-SGD
Oﬄine RL
Algorithm
πprivate
Expert Set
Π
input trajectory
1
Figure 1: Training pipeline for Expert-level Differentially Private Offline RL given an expert setΠ =
{π1,π 2,...,π m}and input trajectories logged into an offline datasetDΠ.A DR (Algorithm 2) splits input
trajectories and adds stable prefixes toDΠ stable discarding the rest toD Π unst. These are used to train any
off-the-shelf offline RL algorithm (see Algorithm 3) and learn an expert-level differentially policyπprivate.
however, that in privacy sensitive domains such as personalized retrieval, advertising, and healthcare, the
behavioural policies might reveal private information about the preferences or strategies used by the corre-
sponding experts (users, advertisers, health care providers etc.) whose decisions underlie the offline data.
In such scenarios, we ideally seek to uncover the broadly beneficial strategies employed in making decisions
by a large cohort of experts whose demonstrations the offline data is collected with, while not leaking the
private information of any given expert. We call this novel settingoffline RL with expert-level privacy, and
design algorithms with strong privacy guarantees for it.
There has been a growing interest in differentially private RL, both in online (Wang & Hegde, 2019; Qiao
& Wang, 2023a; Zhou, 2022; Liao et al., 2023) and offline (Qiao & Wang, 2023b) settings. The offline RL
literature, which is most relevant to this work, primarily focuses on protecting privacy at thetrajectory-
level. However, when each expert contributes multiple trajectories to the demonstration dataset, private
information can still be leaked under trajectory-level differential privacy. Protecting the privacy of an expert
in this scenario requires significantly more careful techniques. Secondly, the prior works mostly focus on
tabularorlinearsettings(Qiao&Wang,2023a;b;Zhou,2022), wheretheofflineRLproblemcanbeeffectively
solved using count or linear regression based techniques, and is hence amenable to existing techniques for
privatizing counts or linear regression models. In contrast, we make no assumptions on the size of the state
space, the parameterization of the learned policy or the policy underlying expert demonstrations. For a more
detailed discussion of related work, we refer the reader to Section 2.
Contributions:With this context, our paper makes the following contributions:
•We identify and formalize the problem of offline RL with expert-level privacy and motivate it with
practical examples. We also explain the inadequacy of prior algorithms in this setting.
•We providepractical algorithmsfor offline RL with strong expert-level privacy guarantees. In con-
trast with prior approaches which use noisy statistics of the data in offline RL (Qiao & Wang, 2023b)
or rely on very strict assumptions like tabular settings or linear function approximators (Wang &
Hegde, 2019), limiting real-world applicability, we remove these constraints, supporting any gradient-
based offline RL algorithm with general function approximators and continuous state spaces.
•DP-SGD (Abadi et al., 2016) is the go-to method today for privately training gradient-based general
function approximators. We adapt DP-SGD for expert-level privacy as a natural baseline in our
problem setting. Our algorithm identifies a subset of the data which can be used in learning without
any added noise, and significantly improves upon the DP-SGD baseline since itselectively adds noise
to gradients only where it is needed, unlike DP-SGD which uniformly noises all gradient updates.
We evaluate our algorithm on standard RL benchmarks, and discuss the results in Section 6.
2

Published in Transactions on Machine Learning Research (10/2025)
Our Algorithm:Our algorithm proceeds in two stages; see Figure 1. The first is a data filtering stage
that produces a set of trajectory prefixes (denotedDΠ stable), using a variant of the Sparse Vector Technique
(SVT) for privacy accounting (Dwork & Roth, 2014), that can be used in training without any further noise
addition, in a privacy-preserving manner. The intuition is that members of this set are likely to occur across
many experts, and hence using it in training does not violate the privacy of an individual expert. The
second stage involves selectively running DP-Stochastic Gradient Descent (DP-SGD)1 (Song et al., 2013;
Bassily et al., 2014; Abadi et al., 2016), adapted for expert-level privacy on the remainder of the trajectories,
DΠ\D Π stable. Our empirical results strongly show that combining both stages of the algorithm described
above, performs better than either of them individually. The only assumption we make on the underlying
offline RL algorithm is that it is gradient-based, so that we can use DP-SGD to privatize its updates.
Motivation:We motivate our problem setting using the case of financial portfolio management. Different
fund managers employ proprietary and privacy-sensitive investment strategies that guide their trading de-
cisions. In such a setting, treating the algorithms used by individual fund managers as expert policies and
learning an expert-level private investment strategy (policy) using offline RL will be beneficial as a starting
strategy for new investors and other parties that do not have specialized investment strategies.
Alternatively, inthecaseofpoliticalcampaignoptimizationinamulti-partydemocracy, largepoliticalparties
may use proprietary algorithms to maximize their reach, whereas independent candidates, often lacking the
same resources, are placed at a disadvantage. Access to a privately learnt aggregate campaigning strategy
will allow such players to compete on a somewhat equal footing, allowing voters greater effective choice.
At a high-level, our setting is similar to the ‘warm-start’ problem in optimization (Sambharya et al., 2024),
translated to an offline RL setting where data is privacy-sensitive and cannot be directly trained on.
Note on Experts:Throughout the paper, we use the term “expert” to refer to RL agents, policies, or
algorithms used in various real-world settings. They do not refer tohuman expertslike doctors, trading
agents etc. We learn an expert-level DP policy, from the offline trajectories logged by such agents interacting
with the environment like behavioural policies in offline RL (Levine et al., 2020; Prudencio et al., 2023).
2 RELATED WORK
Comparison to Prior Work on Private Offline RL:There have been recent works exploring the
intersection of differential privacy (DP) and reinforcement learning (RL) (Wang & Hegde, 2019; Qiao &
Wang, 2023a;b; Zhou, 2022; Liao et al., 2023). Qiao & Wang (2023a;b); Zhou (2022); Wang & Hegde (2019)
explore the problem either in the tabular setting or in the linear function approximation setting. In either of
the cases there is a sufficient statistic (like discrete state-action visit counts or feature covariances to privatize
sensitive data) which if privatized, would suffice to privatize the whole algorithm. Specifically, Wang & Hegde
(2019) explores the use of differential privacy (DP) in continuous spaces to only protect the value function
approximator. Liao et al. (2023) explores RL with linear function approximation under local differential
privacy guarantee, a stronger notion of privacy where users contributing data do not trust the central
aggregator. Meanwhile, Qiao & Wang (2023a;b); Vietri et al. (2020) work with tabular MDP settings
and discrete state-action spaces, often utilizing some form of state-action visit counts to privatize sensitive
data. In our work, we extend existing approaches beyond the state-space and linear function approximator
constraints and propose a general algorithm which can be used withcontinuous state spaces, and with general
functional approximation for RL tasks.
To the best of our knowledge, expert-level DP has not been dealt with in the context of RL so far. Prior works
often limit themselves to exploring trajectory-level privacy, which has finer granularity of privacy protection
which makes the setting arguably “easier". In this work, we adopt an expert-level notion of neighbourhood
when a large number of behavioural policies (or experts) are used for data collection. We further note that
expert-level privacy differs from existing privacy notions like Joint DP (Chowdhury & Zhou, 2022), or other
notions which aim to protect the transitions and rewards of the MDP.
1DP-SGD is to an SGD based approach where gradients coming from individual experts are clipped, and appropriate
Gaussian noise is added to ensure DP.
3

Published in Transactions on Machine Learning Research (10/2025)
Background on DP-SGD and Sparse-Vector Technique:DP-SGD first introduced in Song et al.
(2013); Bassily et al. (2014), and adapted for deep learning by Abadi et al. (2016), proposed gradient noise
injection to guarantee differentially private model training. Several variants of DP-SGD have been proposed
such as McMahan et al. (2017), which allows user-level DP training in federated learning scenarios and
Kairouz et al. (2021) a private variant of the Follow-The-Regularized-Leader (DP-FTRL) algorithm that
compares favourably with amplified DP-SGD (Abadi et al., 2016; Balle et al., 2018).
The Sparse-Vector Technique (Roth & Roughgarden, 2010; Hardt & Rothblum, 2010; Dwork & Roth, 2014),
developed over a sequence of works, allows one to carefully track the privacy budget across queries, and
provide tighter data-dependent privacy guarantees as opposed to vanilla composition (Dwork & Roth, 2014).
At a high-level, the idea is to identify “stable queries”, which have low local sensitivity and do not change
their answers when moving to a neighboring dataset. Such queries can be answered without paying any
additional privacy cost. In Algorithm 2, we use a modification of this idea to output parts of the expert
trajectories that are “stable” without incurring any additional privacy cost (inε).
Relationship with Offline RL Literature:Our approach is agnostic to the underlying offline RL algo-
rithm used and can be combined with any off-the-shelf model-based (Kidambi et al., 2020; Yu et al., 2020;
2021) or model-free (Kumar et al., 2019; 2020; Cheng et al., 2022) offline RL algorithms which use gradient
updates to learn an optimal policy. We focus on model-free approaches in our experiments.
3 PRELIMINARIES
3.1 Offline RL
Offline RL (Levine et al., 2020; Prudencio et al., 2023) is a data-driven approach to RL that aims to
circumvent the prohibitive cost of interactive data collection in many real-world scenarios. Under this
paradigm, a static dataset collected by some (possibly sub-optimal) behaviour policyπβ is used to learn a
policyπwithout any interaction with the environment.
Let the environment be modeled by a Markov Decision Process (MDP)M=⟨S,A,r,P,ρ,γ⟩, whereSis the
state space,Ais the action space,r:S×A→Ris the reward function,P:S×A→∆(S)is the transition
kernel (∆(X)is the set of all probability distributions overX),ρ∈∆(S)is the initial state distribution and
γ∈[0,1]is the discount factor.
Definition 3.1(Offline RL).Given an environment represented by the MDPM=⟨S,A,r,P,ρ,γ⟩defined
above and a datasetD={(s i,ai,ri,s′ i)i}n i=1 generated with(si,ai)∼µfor some state-action distribution
µ,r i =r(s i,ai)ands ′ i∼P(·|s i,ai), the objective is to find an optimal policyπ∗ :S→∆(A), defined as
π∗ = arg max
π
Eπ s1∼ρ[Rτ]
, whereR τ = ∑|τ| t=1γtrt is the discounted return of trajectoryτ, generated fromπandMas:s 1 ∼ρ,
at∼π(.|s t),r t =r(s t,at)ands t+1∼P(.|s t,at)fort≥1upto|τ|timesteps.
A key concern in offline RL is that the state-action distribution encountered in the offline data to learn a
policyπmight significantly differ from that encountered upon actually executingπin the MDP. There is
a host of existing offline RL methods that address this challenge in different ways (Kumar et al., 2019;
Fujimoto et al., 2019b; Kumar et al., 2020; Cheng et al., 2022). We use BCQ (Fujimoto et al., 2019b) and
CQL (Kumar et al., 2020) as our offline RL methods due to their strong performance across a variety of
tasks in prior evaluations and popularity in existing offline RL literature..
We consider a scenario where the dataset contains demonstrations collected from a number of different
behavioural policies or experts with varying degrees of optimality. We denote the set of behaviour policies
byΠ ={π 1,...,π m}. Imposing the constrain of expert-level privacy can conflict with the rewards attainable
by the learned policy. For example, if most experts are similar but a single, high-reward expert diverges from
them, an inherent tradeoff arises between expert-level privacy and utility. We only consider the privatization
of the expert policies (the chosen actions). Thus, information about the environmnent dynamics such as the
transition kernel and reward function are not protected under our proposed algorithm.
4

Published in Transactions on Machine Learning Research (10/2025)
3.2 Differential Privacy
Differential privacy (DP) (Dwork et al., 2006; Dwork & Roth, 2014) quantifies the loss of privacy associated
with data release from any statistical database. Informally, a procedure satisfies DP if the distribution of
its outputs on two datasets which differ only in one record is very similar. We use approximate-DP (or
(ε,δ)-DP) throughout our work. This notion is formally defined below.
Definition 3.2((ε,δ)-DP).For positive real numbersε>0and0≤δ≤1, an algorithmAis(ε,δ)-DP iff,
for any two neighbouring datasetsD,D′∈D∗ (Dis the space of all data records), andS⊂Range(A):
Pr(A(D)∈S)≤e εPr(A(D′)∈S) +δ(1)
whereRange(A)is the set of all possible outputs ofA.
Definition 3.2 guarantees that the probability of seeing a specific output on any two neighbouring datasets
can differ at most by a factor ofeε, with a relaxation ofδ. In most ML applications reasonable privacy
guarantees haveε≤10andδ≤ 1 n (Ponomareva et al., 2023), wherenis the cardinality of the dataset.
One can instantiate Definition 3.2 with different of neighbourhood relations. Definition 3.3 describes our
setting ofexpert-level privacyand the more commonly studiedtrajectory-level privacy.
Definition 3.3(Expert- and Trajectory-level privacy).LetDbe the domain of all valid trajectories possible
in the underlying MDP. LetDΠ∈D∗ be a data set of trajectories generated by a set of expertsΠ.DΠ,D Π′ ∈
D∗ areexpert-level neighboursif the set of experts|Π∆Π′|= 1, where∆is the set difference. Alternatively,
ifD,D ′∈D∗ are sets of trajectories and|D∆D′|= 1, thenDandD ′ aretrajectory-level neighbours.
We note that the key difference between expert and trajectory level privacy notions, as defined above is that
removing an expertπcan remove up to|D π|trajectories from the overall dataset, whereDπ is the set of
trajectories contributed byπ. This is a much larger change than allowed in trajectory-level privacy, and
a naïve treatment would result in paying an additional cost due to group privacy (Dwork & Roth, 2014),
scaling linearly in the number of trajectories each expert contributes. At the same time, as we argue below,
via a set of settings, expert-level privacy is often a critically required notion of privacy protection.
3.3 Problem Setup
Dataset.LetΠdenote a set ofmprivacy-sensitive policies, corresponding tomexperts,Π ={π 1,...,π m}.
DΠ =D π1∪···∪D πm is the aggregated dataset generated by the interaction of themexperts with the
environment. EachDπi is a set ofNtrajectoriesτ= (s 1,a 2,s 2,a 2,...,s L,aL,sL+1)of lengthLobtained by
logging the interactions of policyπi with the MDPM=⟨S,A,r,P,ρ 0,γ⟩, wheres 1∼ρ 0,a h∼π i(·|sh)and
sh+1∼P(·|s h,ah). We denote by|τ|the length of the trajectory as the number of full state-action pairs it
consists of. Further, we useτh:h′ = (sh,ah,...s h′,ah′,sh′+1), whereh≤h ′, to denote the sub-trajectory of
τstarting from theh-th timestep until theh′-th, including the trailing next statesh′+1.
Note on Trajectory Notation:As in Definition 3.1, trajectories are classically defined as a series of
(s,a,r,s ′)tuples, where the next states′ of one transition is the statesof the next transition. Since the
rewards associated with transitions are not used in the privacy analysis or in the filtering stage of our
algorithm, we simplify the classical notation for our analysis and proofs as described above.
Goal.The goal is to learn a policy using an offline RL algorithm with expert-level DP guarantees onDΠ,
thus ensuring that the policy learnt in this manner is not much different from a policy learnt usingDΠ′ .
We make the following mild assumptions in the design of our solution.
Assumption 3.4.The action spaceAis discrete.
This is a fairly mild assumption satisfied in many offline RL settings. This arises while identifying stable
trajectory prefixes for our algorithm, and we leave an extension to continuous action spaces to future work.
Assumption 3.5.We can query the sensitive expert policies, i.e., evaluateπi(a|s)for a giveni,sanda.
5

Published in Transactions on Machine Learning Research (10/2025)
Similar assumptions are reasonable to make in setups involving learning a student model from an ensemble
of privacy-sensitive teacher models, where access to the teacher models are assumed (e.g. Papernot et al.
(2017)). The privacy-sensitive experts in our setting are analogous to these privacy-sensitive teacher models.
Again, query access only comes up in computing the stability of the trajectory prefix, and can likely be
relaxed to using behavior-cloned versions of the experts with a slightly worse utility bound.
Assumption 3.6.LetΠ s be the class of expert policies considered by our algorithm. Hence,Π⊆Πs. We
assume aminimum action probability(pmin), defined as,pmin≤min π∈Πs infs∈S mina∈Aπ(a|s)
This value is used in the data filtering stage (first stage) of our algorithm. Note that we can always take
pmin = 0. However, our algorithm is more meaningful whenpmin >0. Examples of common policy classes
withp min >0includeε-greedy policies and softmax policies with bounded parameters.
Existing work in DP-RL relies on strict assumptions like tabular settings or linear function approximation,
limiting real-world applicability. Our approach removes these constraints and extends to any state-of-the-art
gradient-based offline RL algorithm with general function approximators and continuous state spaces.
4 ALGORITHM
For a given trajectory prefixτ, we define the total probability ofτbeing generated by all the experts as:
countτ(Π) =∑m i=1 [∏Lτ j=1πi(aj|sj) ] 2, whereLτ =|τ|, is the length of trajectoryτ. Algorithm 1 deemsτ
stable ifcountτ(π)exceeds a carefully chosen threshold, implying that enough experts are likely to generate
τ. These stable prefixes may be used in training an offline RL algorithm without any noise addition. We
need Assumption 3.4 for this step. Given a trajectory, the count function gives the sum of probabilities of
each expert traversing it. We usecountτ(Π)to check if enough experts can generate this trajectory.
Algorithm 1PrefixQuery (APQ): Tests if count of experts expected to execute a trajectory is large enough
Require:Expert policiesΠ, trajectoryτ= (s 1,a 1,s 2,a 2,...), stability threshold ˆθ,ε
1:Compute expected experts:count τ(Π)← ∑ π∈Π ∏|τ| j=1π(aj|sj)
2:ifcount τ(Π) +Lap( 4 ε)> ˆθthen return⊤
3:else return⊥
Algorithm 2 uses Algorithm 1 as a subroutine, traversing up toTtrajectories to find stable prefixes. The
datasetD Π stable returned by Algorithm 2 is composed of these stable trajectory prefixes. The discarded tails
of each trajectory (including several full trajectories that were discarded) are collected in another dataset:
DΠ unst ={τ k+1:|τ| ifτ 1:k∈D Π stable fork≥1orτ, τ:D Π}
Consider any parameterized gradient-based offline RL algorithmHϕ, whereϕdenotes the parameters. Train-
ing this algorithm consists of using(s,a,r,s′)tuples collected in the offline dataset to update the parameters
(by splitting the trajectories into into individual transitions). Having split the dataset into stable and un-
stable trajectories, we can now leverage the stability ofDΠ stable to accumulate the gradient updates ofHϕ on
transitions drawn from this dataset without any noise addition. The full algorithm, detailing the training
using a mix of noisy gradient updates for transitions fromDΠ unst and noiseless gradient updates for transitions
fromD Π stable is given in Algorithm 3.
The sampling probabilitypcontrols the expected fraction of batches sampled from the unstable dataset
DΠ unst. The DP-SGD updates of the form DP-SGD(ϕn,B,ε 2,δ 2,N) in Algorithm 3 refer to noisy gradient
updates with additive noise scaled as to ensure(ε2,δ 2)expert-level DP. To do so we add the modifications
to the standard DP-SGD algorithm (Abadi et al., 2016):
•During gradient updates, we ensure that an expert contributesat most one transitionto a batch.
2The full probability of being generated by the given set of experts, is actually proportional to the count function multiplied
by the state-transition probabilities (which do not change for neighbouring experts).
6

Published in Transactions on Machine Learning Research (10/2025)
Algorithm 2DataRelease (ADR): Releasing public dataset after privatisation
Require:Expert datasetD Π, expert policiesΠ,ε 1,δ 1, min action-selection probabilityp min, unstable
query cutoffT≤N·m
1:L←max
τ∈D Π
|τ|
2:ε ′← ε1√
32Tlog(2/δ 1)
, δ ′← δ1 (2TL)
3:c min← eε′ (eε′−1), θ← cmin pmin , D Π stable←{}
4:ReshuffleD Π
5:forc= 1,...,Tdo
6:τ←next trajectory fromD Π
7: ˆθ←θ+ 4 ε′ log(1/δ′) +Lap( 2 ε′ )
8:fori= 1toLdo
9:r←A PQ (Π,τ 1:i, ˆθ,ε′)
10:ifr=⊤andi=|τ|thenD Π stable←D Π stable∪{τ 1:i}
11:else ifr=⊥then
12:ifi>1thenD Π stable←D Π stable∪{τ 1:i−1}
13:break
14:returnD Π stable
•To account for privacy amplification while sampling batches from the dataset, we use the use the
fraction of experts from which we sample. Hence, the subsampling coefficientqfor DP-SGD analysis
isq=p· |B| m , wheremis the number of experts.
We detail the modified expert-level DP-SGD, used as a baseline in Section 6, in Appendix B. See Section 5
for the privacy analysis for the overall pipeline combining Algorithms 2 and 3.
Algorithm 3Selective DP-SGD for Offline RL
Require:Stable datasetD Π stable, Unstable datasetD Π unst, Sampling probabilityp, Gradient-based offline
RL algorithmHϕ,ε 2,δ 2,Ntraining steps,Bbatch size
1:Initializeϕ 0
2:forn= 1toNdo
3:b∼Bernoulli(p)
4:ifb= 1thenϕ n+1←DP-SGD(ϕ n,B,ε 2,δ 2,N), where we sample batchB∼D Π unst
5:else ifb= 0thenϕ n+1←SGD(ϕ n,B), where we sample batchB∼D Π stable
6:returnH ϕN
Relationship with User-level DP:The relationship between trajectory-level and expert-level DP is
analogous to the notions of example-level and user-level privacy in existing DP literature (Lévy et al., 2021;
Zhou et al., 2022; Zhao et al., 2024). However, we retain naming conventions from existing RL literature.
We note that the expert-level DP-SGD (discussed above and in Appendix B) update step in Line 6 of
Algorithm 3 is compatible with other user-level DP algorithms that can be used for training on the unstable
data instead. Most practical approaches for achieving user-level DP are based on clipping user-level gradients
to bound user contributions (Lévy et al., 2021; Bassily & Sun, 2023; Liu & Asi, 2024; De et al., 2022). These
approaches have been empirically tested to be successful on large scale datasets (Charles et al., 2024). Other
approaches for achieving user-level DP are mostly theoretical in nature and come with restrictions (such
as on the function class) that limit their practical usage. The baseline used for comparison in our paper
(described in Appendix B) is a representative of this class of approaches, and a natural way to tackle our
problem statement in such a way that we generalize to any function approximators and continuous, high-
dimensional state spaces. We demonstrate that our method outperforms this baseline by identifying a subset
of the data where noisy training is not required, before running the same baseline on the rest of the data.
7

Published in Transactions on Machine Learning Research (10/2025)
Sub-Optimality Guarantees for the Learned Policy:While we show in the following section that
the Algorithm 3 provides expert-level privacy, we do not provide explicit bounds on the suboptimality of
the returned policy. Typical offline RL literature shows that using pessimistic approaches, the learned
policy is competitive with any other policy whose state-action distribution is well-covered by the offline data
distribution (Xie et al., 2021; Cheng et al., 2022). However, our training distribution undergoes two changes
from thea priorioffline data distribution. First is that the stable prefixes might be distributionally rather
different from the entire state-action distribution, and potentially emphasize the states and actions near
the start of a trajectory, as shorter prefixes are more likely to be stable. Second, the gradient clipping in
DP-SGD adds an additional bias. Understanding the effect of latter with arbitrary function approximation
is beyond the scope of this paper. We do, however, study the effects of distributional biases from adding
varying amounts of the stable prefixes in our experiments, and find that they are typically very beneficial,
particularly in tasks where the optimal behaviour does not change significantly over time.
5 PRIVACY ANALYSIS
We note that all the trajectories may be of various lengths. However, as we shall see in the analysis, the
privacy cost in theδparameter scales linearly with the length of the trajectory, i.e.,δ1∝Lδ ′ (Line 2 in
Algorithm 2), whereδ′ is the per-timestep cost andδ1 is the full cost of the trajectory. By settingLto
be the maximum length across all trajectories, we carry out a worst-case analysis of the privacy leakage.
For a fixed per-timestep privacy budget, we overestimate the total privacy cost by safely considering the
worst-case (maximum) trajectory lengths. In other words, for the benefit of the analysis, we assume that all
trajectories have the same (maximal) lengthL=max
τ∈D Π
|τ|.
Algorithm 2 can be thought of asTiterations of a combination of two algorithmsA1 andA 2:
•A 1 samples a random expertπ∼Unif(Π)and a trajectoryτ∼D π and converts it into|τ|queries,
Qτ ={count τ1(.),...,count τ|τ| (.)}, whereτi =τ 1:i is ani-length prefix of the trajectoryτ.
•A 2 isinvokedonΠandthequerysetQ τ, runninganiterationoftheSparse-VectorTechnique(Dwork
& Roth, 2014) (SVT).A2 treatsΠas the privacy-sensitive database,Qτ as the query sequence, and
ˆθas the threshold for SVT.A 2(Π,Qτ)outputsr∈{⊤,⊥} k+1 such thatr[i] =⊤∀i≤kand
r[k+ 1] =⊥, wherek≤Lis the length of the stable prefix. Note thatr[i] =A PQ (Π,τ 1:i, ˆθ,ε′).
•A 1, upon receivingr, releases the prefixτ1:k = (s1,a 1,...,s k,ak,sk+1).
For a fixed stream of queriesQτ, AlgorithmA 2 is(ε′,0)-DP since it just invokes one round of the Sparse
Vector Algorithm (Dwork & Roth (2014)). Note that the trajectories are just used for creating the queries
for SVT, and the set of expert policiesΠis the privacy database. For a given trajectoryτ,A2 identifies the
longest prefix which is stable, or in other words, has enough experts which are likely to sample this prefix.
Note that, the privacy costε′ for identifying this prefix is independent of the length of the trajectory.
However,Qτ itself is a function of the set of expertsΠ. Despite this, in the following analysis, we show that
A=A 1◦A 2 is also differentially private (due to the carefully chosen threshold in Algorithm 2 Line 6). We
then compose the privacy guarantees overTtrajectories, sinceADR is simplyAappliedTtimes.
We now state two key lemmas for proving thatAis differentially private. For a given trajectory prefixτk of
lengthk, letE τ denote the event thatA1 samples any trajectoryτ′ containingτ k as a prefix, i.e.,τ′ 1:k =τ k.
Lemma 5.1.For a trajectory prefixτk, and neighbouring expert setsΠ,Π′, ifcountτk(Π)≥c min then,
Pr(Eτk|Π)≤e ε′ Pr(Eτk|Π′)(2)
wherec min andε′ are as defined in Algorithm 2.
If the probability of seeing a trajectory prefixτk across all experts is large enough, then the probability that
A1 samples any trajectory with prefixτk is stable when one expert changes. See Appendix A for proof.
8

Published in Transactions on Machine Learning Research (10/2025)
Lemma 5.2.For any trajectory prefixτk, and expert setΠsuch thatcount τk(Π)<θthe following holds:
Pr(APQ (Π,τk, ˆθ,ε′) =⊤)<δ ′ (3)
whereε′,δ′,θ, ˆθare as defined in Algorithm 2.
Informally, if the total probability of seeing a trajectory prefixτk across all experts isnotlarge enough, then
the probability that it is labelled as stable by Algorithm 1 is less thanδ′. See Appendix A for proof.
Theorem 5.3.Under Assumption 3.4,Ais(2ε ′, δ1 2T )-DP, whereε′,δ 1 are defined in Algorithm 2.
Proof Sketch:The main result used to prove this theorem is the following:
Pr(A(Π) =τ)≤e 2ε′ Pr(A(Π′) =τ) + Pr(E τ|Π)·δ ′ (4)
which is obtained from Lemma 5.4 that we give below.
LetTdenote the set of all possible trajectory prefixes usingS,A. To prove thatAis(2ε ′,δ 1/(2T))-
differentially private, we need to prove the following for any pair of neighbouringΠ,Π′⊆Π pmin:
∑
τ∈T
max{Pr(A(Π) =τ)−e 2ε′ Pr(A(Π′) =τ),0}≤ δ1
2T.
The above can be proved using equation 4, and we defer the full proof to Appendix A.
The following lemma gives the key result used to prove Theorem 5.3.
Lemma 5.4.For a trajectory prefixτk and neighboring expert setsΠ,Π′, ifcountτk(Π)<c min then,
Pr(A(Π) =τ k)<Pr(E τk|Π)·δ ′.(5)
Ifcount τk(Π)≥c min then,
Pr(A(Π) =τ k)≤e 2ε′ Pr(A(Π′) =τ k) + Pr(Eτk|Π)·δ ′ (6)
Proof Sketch:The proof of this lemma follows from Lemmas 5.1 and 5.2. Letr=⊤···⊤⊥∈{⊤,⊥} k+1 and
γ(L) =⊤ L. Whenk<Lwe have
Pr(A(Π) =τ k) =
∑
a∈A
[Pr(A2(Π,Qτk·a) =r) Pr(Eτk·a|Π)]
whereτ k·adenotes the trajectory prefixτ k followed by actiona. And whenk=L,
Pr(A(Π) =τ k) = Pr(A2(Π,Qτ k) =γ (L)) Pr(Eτk|Π)
Consider the casek=L. Ifcount τk(Π)is small enough, thenPr(A 2(Π,Qτ k) =γ (L))is less thanδ ′
(Lemma 5.2) and we get equation 5. On the other hand, ifcountτk(Π)is greater thanc min, thenPr(Eτk|Π)
is bounded by Lemma 5.1. Using thatA2 is alwaysε′-DP when the queries are fixed we get equation 6.
The case ofk<Lis less straightforward, but can also be analyzed by considering two cases for eacha∈A,
countτk·a(Π)≥c min orcount τk·a(Π)<c min. See Appendix A for the full proof.
Theorem 5.5.Under Assumption 3.4, Algorithm 2 is(ε1,δ 1)-DP.
Proof.Algorithm 2 executesAwith(ε 1/
√
8Tlog(2/δ 1),δ 1/(2T))-DP (see Theorem 5.3),Ttimes. Using
advanced composition (Corollary 3.21 in Dwork & Roth (2014)) we get that Algorithm 2 is(ε1,δ 1)-DP.
Using all the above, we derive the following expert-level privacy guarantee for the overall training pipeline.
9

Published in Transactions on Machine Learning Research (10/2025)
Theorem 5.6.Algorithm3is(ε,δ)-DP, where:
ε=ε 1 +ε 2 andδ=δ 1 +δ 2 (7)
Proof.Follows from sequential composition of DP guarantees for the release ofDΠ stable and DP-SGD training
on samples fromDΠ unst.
Note on Novelty:We present a novel, useful and non-trivial extension of the Sparse Vector Technique
(SVT) to preserve expert-level DP in Offline RL. The stream of queries in vanilla SVT, (Algorithm 1, Section
3.6, Dwork & Roth (2014)), is not dependent on the private database. However, in our setup, the stream of
queries is a function of the set of the experts (which is the private database to be protected), and directly
applying SVT does not ensure privacy. However, we show that despite the query stream being a function of
the private database, SVT can work if the threshold (line 6 in Algorithm 2) is chosen in a certain way. We
use the probability distribution of the query stream derived from the experts’ policies to prove this.
6 EXPERIMENTS
Ensuring reasonable privacy requires significant hyperparameter tuning and a large number of data points,
often impacting performance adversely3. Intuitively, with the demand for expert-level privacy in our setting,
we risk severe degradation of utility since each “record” (each expert’s data) forms a much larger fraction of
the overall dataset. We recover most of this performance loss, significantly outperforming DP-SGD.
Dataset Generation:We train3000experts each on the Cartpole, Acrobot, LunarLander and HIV Treat-
ment environments. Cartpole, Acrobot and LunarLander are from the Gymnasium package (Towers et al.,
2023). The HIV Treatment simulator is based on the implementation by Geramifard et al. (2015) of the
model described in Ernst et al. (2006). Experts are trained on variations of the default environment, created
by modifying the values of key parameters (e.g. gravity in LunarLander environment). The trained experts
are then used to generate demonstrations on a default setting of the environment, collectively forming the
aggregated dataset for offline RL. This training methodology ensures that the experts show varied (often
sub-optimal) behaviours on the default environment. As shown in Figure 2, the experts’ return-histograms
indicate that the mix of experts we create shows significant diversity in the policies learnt. Further details
regarding the environment settings used to train the expert policies are available in Appendix B.
Figure 2: Expert return histograms, with Kernel Density Estimation, for experts trained on heterogeneous
(left to right) LunarLander, Acrobot, CartPole and HIV Treatment environments. We use experts with wide
ranges of performance on the test environment. Return values for HIV treatment normalised by106.
Training Setup:Our algorithm allows us to use any off-the-shelf gradient-based offline RL algorithm,
and we demonstrate this by experimenting with Conservative Q-Learning (CQL) (Kumar et al., 2020) and
Batch Constrained Deep Q-Learning (BCQ) (Fujimoto et al., 2019b). More specifically, we use the DQN
(Deep Q-Network) version of CQL, and the discrete-action version of BCQ (Fujimoto et al., 2019a), since
we operate under the assumption of discrete action spaces. To represent each of the Q-value functions in
both the algorithms and the generative model in BCQ, we use a neural network with 2 hidden layers of 256
units each. During training, we perform a grid search to find the optimal set of hyper-parameters (learning
rate, batch size, sampling probabilityp, DP-SGD noise) for each environment; see Appendix B.
3In supervised learning, for example, the accuracy on ImageNet training can go from>75%to∼47.9%in the private
case (Kurakin et al., 2022), under example-level privacy.
10

Published in Transactions on Machine Learning Research (10/2025)
The maximum trajectory length is fixed to 200 for Acrobot and CartPole in the collected demonstrations.
While evaluating the final learned policy, the maximum episode length is again set as 200 for Acrobot, we
increase this to 1000 for Cartpole for increased difficulty in an otherwise “simple” environment. We allow
all DP-SGD training runs to progress until the privacy budget is used up completely.
Baselines:We compare our method against DP-SGD adapted for expert-level privacy. A brief discussion
of the changes we made are presented in Section 4. A full discussion, along with analysis, is presented in
Appendix B. We keep the underlying RL algorithm same for fair comparison. In the absence of prior methods
for the expert-level privacy setting, we limit our empirical studies to this naive baseline. We also train a
non-private policy over the whole dataset using vanilla CQL/BCQ (ignoring privacy concerns). This serves
as an empirical upper-bound on the performance achievable under privacy constraints. In our experiments,
we report episodic returns, normalized to lie between 0 (random policy) and 1 (optimal policy) averaged
over 10 evaluation runs at the end of training, as a fraction of the return of the non-private baseline.
6.1 Results
Figure 3: Performance of our method and DP-SGD for different values ofεwithδ= 1/m, wheremis the
number of experts. We report the episodic return, normalized between0(random policy) and1(optimal
policy) averaged over10evaluation runs (with95%confidence intervals) at the end of training, as a fraction
of the non-private baseline. Our method consistently outperforms DP-SGD, especially in the highεregions.
We observe empirically that our algorithm, which leverages expert consensus to select stable trajectory
prefixes prior to offline RL training, shows superior performance to merely using an adapted expert-level
DP-SGD algorithm. Figure 3 compares the performance of our method with DP-SGD across different values
ofε. All the results are averaged over 3 runs and95%confidence intervals are also reported. Our method is
able to recover much of the performance loss due to DP-SGD, especially in the highε-regions.
We experiment withε <5too, but for such lowε, Algorithm 2 yields very little stable data, which does
not meaningfully influence training. Thus, the model primarily learns from the unstable data. Thus, setting
ε1 = 0andε 2 =εis optimal as we minimize the noise injected by the DP-SGD training. This is in contrast
to the observations for higherεvalues where we takeε1 = 3ε 4,ε 2 = ε 4 for LunarLander and CartPole. For
Acrobot and HIVTreatment, we setε1 =ε,ε 2 = 0, that is, we only train onDΠ stable. Similarly, we splitδas
δ1 = 9δ 10,δ 2 = δ 10. These results for lowεare presented in Table 2.
We also note the optimal settings of sampling probabilities in Table 1. Interestingly, for Acrobot (with CQL
and BCQ) and HIV Treatment (with CQL) environments, justDΠ stable suffices to get the optimal performance
in highε-region and we did not need to pay any privacy cost of DP-SGD during model training. We also
report the variation of performance with various mixes of the two datasets (by varyingp) in Table 2.
We also evaluate the effect of varying the number of experts on the performance of our algorithm relative to
DP-SGD, in figure 4, on the Acrobot environment. Asmincreases, the likelihood thatcountτ(Π)exceeds
11

Published in Transactions on Machine Learning Research (10/2025)
Environment CQL BCQ
ε= 5ε= 7.5ε= 10ε= 5ε= 7.5ε= 10
LunarLander1.0 0.8 0.8 1.0 0.5 0.5
Acrobot0.0 0.0 0.0 0.0 0.0 0.0
CartPole1.0 0.9 0.8 1.0 0.5 0.5
HIV Treatment1.0 0.0 0.0 1.0 0.9 0.9
Table 1: Best choices for probability of sampling fromDΠ unstable ie.pfor Algorithm 3 on test environments
Environment CQL BCQ
p= 0.0p= 0.8p= 1.0p= 0.0p= 0.5p= 1.0
LunarLanderinf0.75 0.67inf0.57 0.54
CartPole 0.67 1.03 0.92 0.31 0.99 0.67
Environmentε ε 1 = 3 4 ε ε 1 = 0
Acrobot (BCQ) 2.5 0.74 0.95
Cartpole (BCQ) 2.5 0.28 0.58
Cartpole (BCQ) 5.0 0.56 0.60
Table 2: We perform ablation studies with low, intermediate and high sampling probabilitiespfrom the
unstable datasetD Π unst, atε= 10.inf(infeasible) denotes that the stable datasetD Π stable was empty, and
training was infeasible. We also vary the allocation ofεin the low-privacy regime (ε≤5) and report utility.
the noisy threshold ˆθalso increases, and with it the number and length of trajectory prefixes in the stable
datasetD Π stable. Thus, performance scales with the number of experts. Conversely, for very low values ofm,
the stable dataset is empty and our algorithm defaults towards the baseline.
Figure 4: Performance of our method and DP-SGD
form= 1000,2000and3000experts, on the Acrobot
environment withε= 10.0and CQL as the underlying
offline RL algorithm. We observe increasing improve-
ments of our method over DP-SGD asmincreases.
Note on Implementation:In the implementa-
tion of both our method and DP-SGD, we create
batches by by shuffling datasets of individual ex-
perts and randomly interleaving them such that
each batch has at most one data point from each
expert. This differs slightly from the poisson sam-
pling based accounting in our privacy analysis. This
gap between analysis and implementation in our
work corresponds to the gap between privacy am-
plification by subsampling and shuffling. A promis-
ing line of work (Erlingsson et al., 2019; Feldman
et al., 2021) aims to derive comparable theoretical
amplification guarantees via shuffling. Empirically,
however, the gap in utility is expected to be mini-
mal (Ponomareva et al., 2023).
We use the PLD accountant from the
dp-accountinglibrary to account for the pri-
vacy loss in DP-SGD training.
7 CONCLUSION
In this work, we initiate the study of offline RL with expert-level privacy. We describe the novel challenges of
the setting, and provide theoretically sound algorithms which are evaluated in proof-of-concept evaluation.
In future work, we would like to relax Assumptions 3.4-3.6, by replacing the queries to the experts with
behaviour cloned versions and extending our trajectory prefix selection paradigm to continuous action spaces
(for e.g using kernel density estimation). Understanding the utility implications of Algorithm 3, despite the
influence of our privatization scheme on the training distribution is another important avenue for future work.
Further, privacy auditing in the reinforcement learning setting is another important open research problem
orthogonal to our work. Finally, while our empirical evaluation convincingly establishes the promise of this
approach, we leave a larger evaluation across diverse and larger-scale RL benchmarks for future studies.
12

Published in Transactions on Machine Learning Research (10/2025)
Acknowledgements
The authors thank Krishna Pillutla and Balaraman Ravindran for fruitful discussions and helpful comments.
We also thank the TMLR reviewers for their helpful feedback. This research was supported in part by the
Post-Baccalaureate Fellowship at the Centre for Responsible AI, IIT Madras.
References
Martin Abadi, Andy Chu, Ian Goodfellow, H. Brendan McMahan, Ilya Mironov, Kunal Talwar, and Li Zhang.
Deep Learning with Differential Privacy. InProceedings of the 2016 ACM SIGSAC Conference on Computer and
Communications Security, CCS’16. ACM, 2016.
BorjaBalle, GillesBarthe, andMarcoGaboardi. PrivacyAmplificationbySubsampling: TightAnalysesviaCouplings
and Divergences. InAdvances in Neural Information Processing Systems (NeurIPS), volume 31, 2018.
Raef Bassily and Ziteng Sun. User-level Private Stochastic Convex Optimization with Optimal Rates. InInternational
Conference on Machine Learning (ICML), 2023.
Raef Bassily, Adam Smith, and Abhradeep Thakurta. Private Empirical Risk Minimization: Efficient Algorithms and
Tight Error Bounds. InProceedings of the 55th IEEE Annual Symposium on Foundations of Computer Science
(FOCS), pp. 464–473, 2014. ISBN 9781479965175.
Léon Bottou, Jonas Peters, Joaquin Quiñonero-Candela, Denis X Charles, D Max Chickering, Elon Portugaly, Di-
pankar Ray, Patrice Simard, and Ed Snelson. Counterfactual reasoning and learning systems: The example of
computational advertising.Journal of Machine Learning Research, 14(11), 2013.
Han Cai, Kan Ren, Weinan Zhang, Kleanthis Malialis, Jun Wang, Yong Yu, and Defeng Guo. Real-time bidding by
reinforcement learning in display advertising. InProceedings of the tenth ACM international conference on web
search and data mining, pp. 661–670, 2017.
Zachary Charles, Arun Ganesh, Ryan McKenna, H. Brendan McMahan, Nicole Mitchell, Krishna Pillutla, and Keith
Rush. Fine-Tuning Large Language Models with User-Level Differential Privacy.arXiv Preprint, 2024.
Ching-An Cheng, Tengyang Xie, Nan Jiang, and Alekh Agarwal. Adversarially trained actor critic for offline rein-
forcement learning. InInternational Conference on Machine Learning, pp. 3852–3878. PMLR, 2022.
Sayak Ray Chowdhury and Xingyu Zhou. Differentially Private Regret Minimization in Episodic Markov Decision
Processes. InThirty-Sixth AAAI Conference on Artificial Intelligence, pp. 6375–6383. AAAI Press, 2022.
Soham De, Leonard Berrada, Jamie Hayes, Samuel L. Smith, and Borja Balle. Unlocking High-Accuracy Differentially
Private Image Classification through Scale.arXiv Preprint, 2022.
Cynthia Dwork and Aaron Roth. The Algorithmic Foundations of Differential Privacy.Foundations and Trends®in
Theoretical Computer Science, 9(3–4):211–407, 2014. ISSN 1551-305X. doi: 10.1561/0400000042.
Cynthia Dwork, Frank McSherry, Kobbi Nissim, and Adam Smith. Calibrating Noise to Sensitivity in Private Data
Analysis. InProc. of Theory of Cryptography Conference (TCC), 2006.
Úlfar Erlingsson, Vitaly Feldman, Ilya Mironov, Ananth Raghunathan, Kunal Talwar, and Abhradeep Thakurta.
Amplification by Shuffling: From Local to Central Differential Privacy via Anonymity. InProceedings of the
Thirtieth Annual ACM-SIAM Symposium on Discrete Algorithms (SODA), pp. 2468–2479. SIAM, 2019.
Damien Ernst, Guy-Bart Stan, Jorge Goncalves, and Louis Wehenkel. Clinical Data Based Optimal STI Strategies for
HIV: A Reinforcement Learning Approach. InProceedings of the 45th IEEE Conference on Decision and Control,
pp. 667–672. IEEE, 2006.
Vitaly Feldman, Audra McMillan, and Kunal Talwar. Hiding Among the Clones: A Simple and Nearly Optimal
Analysis of Privacy Amplification by Shuffling. In62nd IEEE Annual Symposium on Foundations of Computer
Science (FOCS), pp. 954–964. IEEE, 2021.
Justin Fu, Aviral Kumar, Ofir Nachum, G. Tucker, and Sergey Levine. D4RL: Datasets for Deep Data-Driven
Reinforcement Learning.arXiv Preprint, abs/2004.07219, 2020.
13

Published in Transactions on Machine Learning Research (10/2025)
Scott Fujimoto, Edoardo Conti, Mohammad Ghavamzadeh, and Joelle Pineau. Benchmarking Batch Deep Reinforce-
ment Learning Algorithms.arXiv Preprint, 2019a.
Scott Fujimoto, David Meger, and Doina Precup. Off-Policy Deep Reinforcement Learning without Exploration.
In Kamalika Chaudhuri and Ruslan Salakhutdinov (eds.),Proceedings of the 36th International Conference on
Machine Learning, volume 97 ofProceedings of Machine Learning Research, pp. 2052–2062. PMLR, 2019b.
Alborz Geramifard, Christoph Dann, Robert H Klein, William Dabney, and Jonathan P How. RLPy: A Value-
Function-Based Reinforcement Learning Framework for Education and Research.Journal of Machine Learning
Research (JMLR), 16(1):1573–1578, 2015.
Moritz Hardt and Guy N Rothblum. A multiplicative weights mechanism for privacy-preserving data analysis. In
2010 IEEE 51st annual symposium on foundations of computer science, pp. 61–70. IEEE, 2010.
Eugene Ie, Vihan Jain, Jing Wang, Sanmit Narvekar, Ritesh Agarwal, Rui Wu, Heng-Tze Cheng, Morgane Lustman,
Vince Gatto, Paul Covington, et al. Reinforcement learning for slate-based recommender systems: A tractable
decomposition and practical methodology.arXiv preprint, 2019.
Peter Kairouz, Brendan Mcmahan, Shuang Song, Om Thakkar, Abhradeep Thakurta, and Zheng Xu. Practical and
Private (Deep) Learning Without Sampling or Shuffling. InProceedings of the 38th International Conference on
Machine Learning, pp. 5213–5225. PMLR, 2021.
Rahul Kidambi, Aravind Rajeswaran, Praneeth Netrapalli, and Thorsten Joachims. MOReL: Model-Based Offline
Reinforcement Learning. InAdvances in Neural Information Processing Systems (NeurIPS), volume 33, pp. 21810–
21823, 2020.
Aviral Kumar, Justin Fu, Matthew Soh, George Tucker, and Sergey Levine. Stabilizing off-policy q-learning via
bootstrapping error reduction. InAdvances in Neural Information Processing Systems (NeurIPS), volume 32,
2019.
Aviral Kumar, Aurick Zhou, G. Tucker, and Sergey Levine. Conservative q-learning for offline reinforcement learning.
arXiv Preprint, abs/2006.04779, 2020.
AlexeyKurakin, SteveChien, ShuangSong, RoxanaGeambasu, A.Terzis, andAbhradeepThakurta. TowardTraining
at ImageNet Scale with Differential Privacy.arXiv Preprint, abs/2201.12328, 2022.
Sergey Levine, Aviral Kumar, G. Tucker, and Justin Fu. Offline Reinforcement Learning: Tutorial, Review, and
Perspectives on Open Problems.arXiv Preprint, abs/2005.01643, 2020.
Daniel Lévy, Ziteng Sun, Kareem Amin, Satyen Kale, Alex Kulesza, Mehryar Mohri, and Ananda Theertha Suresh.
Learning with User-Level Privacy.arXiv Preprint, abs/2102.11845, 2021.
Chonghua Liao, Jiafan He, and Quanquan Gu. Locally Differentially Private Reinforcement Learning for Linear
Mixture Markov Decision Processes. InProceedings of The 14th Asian Conference on Machine Learning, volume
189 ofProceedings of Machine Learning Research, pp. 627–642. PMLR, 2023.
Daogao Liu and Hilal Asi. User-level Differentially Private Stochastic Convex Optimization: Efficient Algorithms
with Optimal Rates. InInternational Conference on Artificial Intelligence and Statistics (AISTATS), 2024.
H. B. McMahan, Daniel Ramage, Kunal Talwar, and Li Zhang. Learning differentially private recurrent language
models. InInternational Conference on Learning Representations, 2017.
Michael Oberst and David Sontag. Counterfactual off-policy evaluation with gumbel-max structural causal models.
InInternational Conference on Machine Learning, pp. 4881–4890. PMLR, 2019.
Nicolas Papernot, Martín Abadi, Úlfar Erlingsson, Ian J. Goodfellow, and Kunal Talwar. Semi-supervised Knowledge
Transfer for Deep Learning from Private Training Data. In5th International Conference on Learning Representa-
tions (ICLR), 2017.
Natalia Ponomareva, Hussein Hazimeh, Alex Kurakin, Zheng Xu, Carson Denison, H. Brendan McMahan, Sergei
Vassilvitskii, Steve Chien, and Abhradeep Guha Thakurta. How to DP-fy ML: A Practical Guide to Machine
Learning with Differential Privacy.Journal of Artificial Intelligence Research, 77:1113–1201, 2023. ISSN 1076-
9757.
14

Published in Transactions on Machine Learning Research (10/2025)
Rafael Figueiredo Prudencio, Marcos R. O. A. Maximo, and Esther Luna Colombini. A Survey on Offline Reinforce-
ment Learning: Taxonomy, Review, and Open Problems.IEEE Transactions on Neural Networks and Learning
Systems, 2023. ISSN 2162-2388.
Dan Qiao and Yu-Xiang Wang. Near-Optimal Differentially Private Reinforcement Learning. InInternational Con-
ference on Artificial Intelligence and Statistics (AISTATS), pp. 9914–9940. PMLR, 2023a.
Dan Qiao and Yu-Xiang Wang. Offline Reinforcement Learning with Differential Privacy. InAdvances in Neural
Information Processing Systems (NeurIPS), 2023b.
Aaron Roth and Tim Roughgarden. Interactive privacy via the median mechanism. InProceedings of the Forty-Second
ACM Symposium on Theory of Computing (STOC), pp. 765–774, 2010.
Rajiv Sambharya, Georgina Hall, Brandon Amos, and Bartolomeo Stellato. Learning to warm-start fixed-point
optimization algorithms.J. Mach. Learn. Res., 25:166:1–166:46, 2024.
Shuang Song, Kamalika Chaudhuri, and Anand D. Sarwate. Stochastic gradient descent with differentially private
updates. In2013 IEEE Global Conference on Signal and Information Processing, GlobalSIP 2013 - Proceedings,
pp. 245–248, 2013. ISBN 9781479902484.
Shengpu Tang, Maggie Makar, Michael Sjoding, Finale Doshi-Velez, and Jenna Wiens. Leveraging factored action
spaces for efficient offline reinforcement learning in healthcare.Advances in Neural Information Processing Systems,
35:34272–34286, 2022.
Mark Towers, Jordan K. Terry, Ariel Kwiatkowski, John U. Balis, Gianluca de Cola, Tristan Deleu, Manuel Goulão,
Andreas Kallinteris, Arjun KG, Markus Krimmel, Rodrigo Perez-Vicente, Andrea Pierré, Sander Schulhoff, Jun Jet
Tai, Andrew Tan Jin Shen, and Omar G. Younis. Gymnasium, 2023.
Giuseppe Vietri, Borja Balle, Akshay Krishnamurthy, and Steven Wu. Private Reinforcement Learning with PAC
and Regret Guarantees. InInternational Conference on Machine Learning, pp. 9754–9764. PMLR, 2020.
Baoxiang Wang and Nidhi Hegde. Privacy-Preserving Q-Learning with Functional Noise in Continuous Spaces. In
Advances in Neural Information Processing Systems (NeurIPS), volume 32, 2019.
Tengyang Xie, Ching-An Cheng, Nan Jiang, Paul Mineiro, and Alekh Agarwal. Bellman-consistent pessimism for
offline reinforcement learning.Advances in neural information processing systems, 34:6683–6694, 2021.
Tianhe Yu, Garrett Thomas, Lantao Yu, Stefano Ermon, James Y Zou, Sergey Levine, Chelsea Finn, and Tengyu
Ma. Mopo: Model-based offline policy optimization.Advances in Neural Information Processing Systems, 33:
14129–14142, 2020.
Tianhe Yu, Aviral Kumar, Rafael Rafailov, Aravind Rajeswaran, Sergey Levine, and Chelsea Finn. Combo: Conser-
vative offline model-based policy optimization.Advances in neural information processing systems, 34:28954–28967,
2021.
Puning Zhao, Lifeng Lai, Li Shen, Qingming Li, Jiafei Wu, and Zhe Liu. A Huber Loss Minimization Approach to
Mean Estimation under User-level Differential Privacy. InNeurIPS, 2024.
Mingxun Zhou, Tianhao Wang, T.-H. Hubert Chan, Giulia Fanti, and Elaine Shi. Locally Differentially Private
Sparse Vector Aggregation. InIEEE Symposium on Security and Privacy, 2022.
Xingyu Zhou. Differentially private reinforcement learning with linear function approximation.Proceedings of the
ACM on Measurement and Analysis of Computing Systems, 6(1):1–27, 2022.
15

Published in Transactions on Machine Learning Research (10/2025)
A Theorem Proofs
A.1 Proof of Lemma 5.1
Lemma 5.1.For a trajectory prefixτk, and neighbouring expert setsΠ,Π′, ifcountτk(Π)≥c min then,
Pr(Eτk|Π)≤e ε′ Pr(Eτk|Π′)(2)
wherec min andε′ are as defined in Algorithm 2.
Proof.RecallE τk is the event a trajectory with prefixτk is generated. Assumingτk =s 1,a 1,s 2,...,a k,sk+1,
the probability that a fixed expertπgenerates such a prefix when interacting with the MDP is
ρ0(s1)
(
Πk j=1π(aj|sj)P(sj+1|sj,aj) ) . Since the expert is chosen uniformly at random, we have:
Pr(Eτk|Π) = 1 m
m∑
i=1
[
ρ0(s1)
(
Πk j=1πi(aj|sj)P(sj+1|sj,aj) )] (8)
= 1 mρ0(s1) ( Πk j=1P(sj+1|sj,aj) ) m∑ i=1 ( Πk j=1πi(aj|sj) ) (9)
= 1 mρ0(s1) ( Πk j=1P(sj+1|sj,aj) ) countτk(Π).(10)
Similarly,
Pr(Eτk|Π′) = 1 m′ρ0(s1) ( Πk j=1P(sj+1|sj,aj) ) countτk(Π′).(11)
Wherem′ =|Π′|. Since|Π∆Π′|= 1,
|countτk(Π)−count τk(Π′)|≤1and|m−m ′|= 1.(12)
This gives us the following,
Pr(Eτk|Π)
Pr(Eτk|Π′) = countτk(Π)×m ′ countτk(Π′)×m (13)
≤max
(countτk(Π)(m+ 1)
(countτk(Π) + 1)m,countτk(Π)(m−1) (countτk(Π)−1)m ,m+ 1 m ,m−1 m ) (14)
= max
(countτk(Π)(m−1)
(countτk(Π)−1)m ,m+ 1 m ) .(15)
Note that, sincem+ 1>count τk(Π),
m+ 1
m < countτk(Π) countτk(Π)−1 (16)
max
(countτk(Π)(m−1)
(countτk(Π)−1)m ,m+ 1 m ) < countτk(Π) countτk(Π)−1 .(17)
This allows us to bound the ratio of probabilities ofEτk forΠandΠ ′ as
Pr(Eτk|Π)
Pr(Eτk|Π′) < countτk(Π) countτk(Π)−1 ≤e ε′ ,(18)
where the last inequality usescountτ(Π)≥c min =e ε′ /(eε′ −1).
16

Published in Transactions on Machine Learning Research (10/2025)
A.2 Proof of Lemma 5.2
Lemma 5.2.For any trajectory prefixτk, and expert setΠsuch thatcount τk(Π)<θthe following holds:
Pr(APQ (Π,τk, ˆθ,ε′) =⊤)<δ ′ (3)
whereε′,δ′,θ, ˆθare as defined in Algorithm 2.
Proof.
Pr(APQ (Π,τ, ˆθ,ε′) =⊤) = Pr [countτk(Π) +Lap(4/ε′)>θ+ (4/ε ′) log(1/δ′) +Lap(2/ε′)](19)
<Pr [θ+Lap(4/ε ′)>θ+ (4/ε ′) log(1/δ′) +Lap(2/ε′)](20)
= Pr [Lap(4/ε′)>(4/ε ′) log(1/δ′) +Lap(2/ε′)](21)
Consideru∼Lap(4/ε ′)andv∼Lap(2/ε ′). For a fixedv, we have,
Pr [u≥(4/ε ′) log(1/δ′) +v]≤ δ′
2e−v(ε′/4) (22)
Using the Laplace tail bound, we account for the randomness ofvfrom equation 21, equation 22 and the
probability density function of the Laplace distribution, we have,
Pr [Lap(4/ε′)>(4/ε ′) log(1/δ′) +Lap(2/ε′)]≤
∫ ∞
−∞
(δ′
2e−v(ε′/4)× ε′ 4e−|v|(ε′/2) ) dv(23)
<δ′ (24)
This gives the statement of the lemma.
A.3 Proof of Lemma 5.4
Lemma 5.4.For a trajectory prefixτk and neighboring expert setsΠ,Π′, ifcountτk(Π)<c min then,
Pr(A(Π) =τ k)<Pr(E τk|Π)·δ ′.(5)
Ifcount τk(Π)≥c min then,
Pr(A(Π) =τ k)≤e 2ε′ Pr(A(Π′) =τ k) + Pr(Eτk|Π)·δ ′ (6)
Proof.We split this proof across 3 lemmas. Lemma A.1 proves this bound for the casecountτk(Π)< cmin
andk<L. Lemma A.2 handles the casecount τk(Π)≥c min andk<L. Finally, Lemma A.3 proves this for
k=L. Combining these 3 gives the statement of Lemma 5.4.
Lemma A.1.For any trajectory prefixτk,k<L, and neighboring expert setsΠ,Π′⊆Π pmin, ifcountτk(Π)<
cmin then,
Pr(A(Π) =τ k)<Pr(E τk|Π)·δ ′
whereδ′ is as defined in Algorithm 2.
Proof.Letr=⊤···⊤⊥∈{⊤,⊥} k+1
Pr(A(Π) =τ k) =
∑
a∈A
[Pr(A2(Π,Qτk·a) =r) Pr(Eτk·a|Π)](25)
whereτ k·adenotes the trajectory prefixτ k followed by actiona.
17

Published in Transactions on Machine Learning Research (10/2025)
A2 runs the Sparse Vector Algorithm using the the query sequenceQτk·a to output a sequence of the form
⊤···⊤⊥. Here, each⊤or⊥is an output ofA PQ (Algorithm 1). The probability thatA 2 outputs the
sequencercan be upper-bounded by the probability of getting⊤on thek th call toAPQ. Formally,
Pr(A2(Π,Qτk·a) =r)≤Pr(A PQ (Π,τk, ˆθ,ε′) =⊤)(26)
∀a, Usingcountτ(Π)<c min <θ, (sinceθ=c min/pmin), Lemma 5.2, and equation 26,
Pr(A2(Π,Qτk·a) =r)≤δ ′ (27)
Combining equation 25 and equation 27, we get,
Pr(A(Π) =τ k)<δ ′∑
a∈A
Pr(Eτk·a|Π) =δ′ Pr(Eτk|Π)(28)
Lemma A.2.For any trajectory prefixτ k = (s 1,a 1,...,s k,ak,sk+1),k < L, and neighboring expert sets
Π,Π′⊆Π pmin, ifcountτk(Π)≥c min then,
Pr(A(Π) =τ k)≤e 2ε′ Pr(A(Π′) =τ k) + Pr(Eτk|Π)δ′
whereε′,δ′ are as defined in Algorithm 2.
Proof.Letr=⊤···⊤⊥∈{⊤,⊥} k+1.
Pr(A(Π) =τ) =
∑
a∈A
[
Pr(A2(Π,Qτ·a) =r k+1) Pr(Eτ·a|Π) ] (29)
LetA′ ={a:a∈A,count τk·a(Π)≥c min},A′′ =A\A ′.
∀a∈A ′′,
countτk·a(Π) =
m∑
i=1
[(Πk j=1πi(aj|sj))×π i(a|sk+1)]≥p min×
m∑
i=1
[Πk j=1πi(aj|sj)] =p min×countτk(Π)(30)
pmin×countτk(Π)≤count τk·a(Π)<c min (31)
⇒count τk(Π)< cmin pmin =θ(32)
The output ofA2 is the output of a sequence of calls toAPQ (Algorithm 1). The probability thatA2 outputs
the sequencercan be upper-bounded by the probability of getting⊤on thek th call toA PQ. Using this
fact along with equation 32 and Lemma 5.2, we can say,
Pr(A2(Π,Qτk·a) =r)≤Pr(A PQ (Π,τk, ˆθ,ε′) =⊤)<δ ′ (33)
18

Published in Transactions on Machine Learning Research (10/2025)
Pr(A(Π) =τ k) =
∑
a∈A
[Pr(A2(Π,Qτk·a) =r) Pr(Eτk·a|Π)](34)
=
∑
a∈A′
[Pr(A2(Π,Qτk·a) =r) Pr(Eτk·a|Π)]
+
∑
a∈A′′
[Pr(A2(Π,Qτk·a) =r) Pr(Eτk·a|Π)](35)
=
∑
a∈A′
[Pr(A2(Π,Qτk·a) =r) Pr(Eτk·a|Π)]
+δ′ ∑
a∈A′′
Pr(Eτk·a|Π)[Using equation 33] (36)
≤e 2ε′ ∑
a∈A′
[Pr(A2(Π′,Qτk·a) =r) Pr(Eτk·a|Π′)]
+δ′ Pr(Eτk|Π)[Using:A 2 is(ε′,0)-DP and Lemma 5.1] (37)
≤e 2ε′∑
a∈A
[Pr(A2(Π′,Qτk·a) =r) Pr(Eτk·a|Π′)] +δ′ Pr(Eτk|Π)(38)
Pr(A(Π) =τ k)≤e 2ε′ Pr(A(Π′) =τ k) + Pr(Eτk|Π)δ′ (39)
Lemma A.3.For any trajectory prefixτ L, whereLis the maximum length of a trajectory, and a pair of
neighboring expert setsΠ,Π′⊆Π pmin, ifcountτL(Π)<c min then,
Pr(A(Π) =τ L)<Pr(E τL|Π)·δ ′.(40)
Ifcount τL(Π)≥c min then,
Pr(A(Π) =τ L)≤e 2ε′ Pr(A(Π′) =τ L)(41)
Proof.Letγ (L) =⊤ L.
Pr(A(Π) =τ L) = Pr(A2(Π,Qτ L) =γ (L)) Pr(EτL|Π)(42)
Ifcount τL(Π)≥c min, then using the fact thatA2 is(ε′,0)-DP and Lemma 5.1, we can say that,
Pr(A(Π) =τ L)≤e 2ε′ Pr(A(Π′) =τ L)(43)
Recall that the output ofA2 is the output of a sequence of calls toAPQ (Algorithm 1). The probability that
A2 outputs the sequencercan be upper-bounded by the probability of getting⊤on theL th call toAPQ.
Formally,
Pr(A2(Π,QτL) =γ (L))≤Pr(A PQ (Π,τL, ˆθ,ε′) =⊤)(44)
Ifcount τL(Π)<c min, then usingcountτ(Π)<c min <c min/pmin =θ, equation 44 and Lemma 5.2, we get,
Pr(A2(Π,QτL) =γ (L))≤Pr(A PQ (Π,τL, ˆθ,ε′) =⊤)<δ ′ (45)
Pr(A(Π) =τ L)≤Pr(E τL|Π)δ′ [Fromequation42](46)
Combining 43 and 46, we get the statement of the lemma.
19

Published in Transactions on Machine Learning Research (10/2025)
A.4 Proof of Theorem 5.3
Theorem 5.3.Under Assumption 3.4,Ais(2ε ′, δ1 2T )-DP, whereε′,δ 1 are defined in Algorithm 2.
Proof.LetTdenote the set of all possible trajectory prefixes usingS,A. From Lemma 5.4, we have,∀τ∈T,
and all pairs of neighboring sets of expertsΠ,Π′⊆Π pmin,
Pr(A(Π) =τ)≤e 2ε′ Pr(A(Π′) =τ) + Pr(E τ|Π)·δ ′ (47)
whereδ′ =δ 1/(2LT).
To prove thatAis(2ε ′,δ 1/(2T))-differentially private, we need to prove the following for any pair of
neighbouringΠ,Π ′⊆Π pmin:
∑
τ∈T
max{Pr(A(Π) =τ)−e 2ε′ Pr(A(Π′) =τ),0}≤ δ1
2T (48)
Note that, for any fixedk, ∑
τ∈{τ:τ∈T,|τ|=k}
Pr(Eτ|Π) = 1(49)
where|τ|denotes the length of the trajectory prefixτ.
∑
τ∈T
Pr(Eτ|Π) =
L∑
k=1

 ∑
τ∈{τ:τ∈T,|τ|=k}
Pr(Eτ|Π)

 =L(50)
whereLis the length of a full trajectory. From equation 47, we have,
∑
τ∈T
max{Pr(A(Π) =τ)−e 2ε′ Pr(A(Π′) =τ),0}≤ ∑
τ∈T
Pr(Eτ|Π)δ′ =Lδ′ = δ1 2T (51)
This proves Eqn 48, and hence the statement of the theorem.
B EXPERIMENTAL DETAILS
B.1 Dataset Generation
We setpmin = 0.02for all the environments.
LunarLander:Among the various variable which govern the dynamics of this environment, we chose to
modify gravity (default = 9.8), wind power (default = 0.0) and turbulence (default = 0.0) to train different
experts. We modified gravity over 10 equally spaced values from 9.0 to 11.0, wind power over 10 equally
spaced values between 0.0 to 5.0, and similarly turbulence over 10 equally spaced values from 0.0 to 0.5,
to generate 1000 environment settings. For each of these environment settings, we trained agents using the
PPO algorithm for1e6updates along with hyperparameter tuning of learning rate and batch size. Each
agent is a neural network with hidden-layers of sizes (512, 256, 64). For each environment setting, we chose
the top 3 agents that performed the best onthe corresponding environment, to form our 3000 experts.
CartPole:For CartPole, we chose to vary gravity, the magnitude of the force exerted when the cart is
pushed and the mass of the cart. The default values of gravity, force magnitude and mass of the cart are
9.8, 10.0 and 1.0 respectively. We varied each control over 10 equally spaced values over a fixed range. For
gravity, we fixed this range as (8.75, 11.0), for force magnitude as (9.0, 11.25) and for mass of the cart as
(0.8, 1.25). Similar to above, for each of these 1000 environment settings, we trained agents using the PPO
20

Published in Transactions on Machine Learning Research (10/2025)
π1
π2
π3
πm
Π
Expert Set
Env 1
Env 2
Env 3
Env m
Train
Train
Train
Train
...... ...... ...... ......Test
Environment
Dπ1
Dπ2
Dπ3
Dπm
DΠ
Oﬄine Dataset
1
Figure 5: Outline of Data Generation scheme; We train experts on multiple environments as described below.
algorithm for1e6updates while tuning the learning rate and batch size. Each agent is a neural network with
hidden-layers of sizes (512, 256, 64). We chose the top 3 agents from each setting to form our 3000 experts.
Acrobot:For this environment, we varied the lengths of the 2 connected links and their masses. The default
values of all these parameters is 1.0. We assign the same length to both the links in each setting. We vary
this length, the mass of link 1 and the mass of link 2 over 10 equally spaced values across fixed ranges for
each. We fix these ranges as (0.8, 1.2) for the length of the links, (0.9, 1.1) for the mass of link 1 and (0.9,
1.1) for the mass of link 2. The combination of these gives us 1000 environment settings. Again, we trained
agents using PPO for1e6updates over multiple learning rates and batch sizes and picked the top 3 agents
from each setting to form our 3000 experts. Each agent is a neural network with hidden-layers of sizes (512,
256, 64).
HIV Treatment:In this domain, the 6-dimensional continuous state represents the concentrations of
various cells and viruses. The actions correspond to the dosages of two drugs. The reward is a function
of the health outcomes of the patient, and it also penalises the side-effects due to the quantity of drugs
prescribed. Hence, the default reward function has 2 penalty terms, a penalty of 20000 on the dosage of
drug 1, and a penalty of 2000 on the dosage of drug 2 (Ernst et al., 2006). In the default setting of the
environment, we assume that the treatment at each steps is applied for 20 days and that there are 50 time
steps in an episode. To train experts, we vary the penalty on drug 1 over 50 equally spaced values from
18750 to 21250, and the penalty on drug 2 over 20 equally spaced values from 1850 to 2150. Another
variation that we introduce is whether the efficacy of the administered drug is noisy or not. So we either add
no noise to the drug efficacy, or we add gaussian noise with standard deviation 0.01. All these modifications
give us 2000 different environment settings. We trained agents using PPO for2e6updates on each of the
environment settings and over multiple learning rates and batch sizes. Each agent is represented by a
neural network with a single hidden layer of size 512. We then picked the top agents from each of the 2000
environment settings to create experts. We picked 1000 more top-performing agents from the 2nd best
agents of all the environment settings to get 3000 experts in total.
Once we have chosen 3000 experts for any of the above environments, we modify each expert’s policy so
that for each state, the action with the highest probability gets(1−(|A|−1)·pmin)probability (where|A|
denotes the total number of actions), whereas all the other actions getpmin probability of being executed.
We then use these modified experts to sample 20 trajectories each from the default environment to form our
offline dataset.
21

Published in Transactions on Machine Learning Research (10/2025)
B.2 Expert-Level DP-SGD
We adapted DP-SGD to the expert-level privacy setting to form the baseline that we compare against. To
achieve this, during gradient updates, we ensure that an expert contributes at most one transition to a batch.
To construct a batch of sizeb, we randomly samplebexperts from the totalmexperts, and then pick a
transition from each selected expert. This is analogous to DP-SGD training on a dataset of sizem. For
privacy accounting, we use PLD accountant from thetensorflow_privacylibrary.
Algorithm 4Expert-Level DP-SGD (outline)
Require:Model Parametersϕ, Expert DatasetsD Π, Expert PoliciesΠ, Loss functionL(ϕ) =
1
b
∑b
i=1L(ϕ,xi), Learning Rateη, Batch sizeb, Noise parameterσ, Clipping thresholdC, Training
stepsN
1:Initializeϕ 0 randomly
2:fort= 1,...,N−1do
3:Sample subset of expertsBfromΠwith subsampling probability b m
4:For eachπ i∈Bsample transitionx= (s,a,r,s ′)fromD πi to form a batch of transitionsBtrans
5:For eachx i∈B trans compute gradientsgi(ϕt)←∇ ϕtL(ϕt,xi)
6:Scale gradients to fit clipping threshold¯g i(ϕt)←g i(ϕt)/max
(
1,∥gi(ϕt)∥2 C
)
7:Add gaussian noise to gradients˜g t← 1 b
(∑b
i=1 ¯gi(ϕt) +N(0,σ 2C2I) )
8:Update model parametersϕ t+1←ϕ t−η·˜gt
9:returnϕ T
Algorithm 4 describes a general outline for expert-level DP-SGD which we use as a baseline to compare our
method against. The loss function here corresponds to the offline RL algorithm.
In our method, Algorithm 4 is incorporated in the training scheme in Algorithm 3 (lines 5 and 6) in the
main paper. At each training step, with probabilityp, we execute lines 3-8 in Algorithm 4 to train on a
batch of transitions. Otherwise, we sample a batch of transitions fromDΠ stable and perform a normal SGD
update (this has no privacy cost). The privacy analysis for Algorithm 3 proceeds in a manner similar to that
in standard DP-SGD (Abadi et al., 2016) with the exception of the subsampling probability which must be
modified to beq=p· b m (in the analysis only) to account for the randomness in picking the unstable dataset
for sampling.
B.3 Hyperparameter Tuning
For all the environments, we assume thatpmin = 0.02. For LunarLander, CartPole and HIVTreatment,
forε= 5, we setε 1 = 0,ε 2 =ε,δ 1 = 0,δ 2 =δand resort to pure expert-level DP-SGD training since
the privacy budget is not enough to get meaningful stable trajectories for training. For Acrobot, we set
ε1 =ε,ε 2 = 0,δ 1 =δ,δ 2 = 0. For all other cases, we setε1 = 3ε 4,ε 2 = ε 4,δ 1 = 9δ 10,δ 2 = δ 10.
We use Conservative Q-Learning (CQL) (Kumar et al., 2020) and Discrete Batch-Constrained Deep Q-
Learning (BCQ) (Fujimoto et al., 2019a) for training on the offline data. For Lunar Lander, Acrobot and
CartPole, we fix all neural network hidden layer sizes to (256, 256). For HIV Treatment, we use a neural
network of one hidden layer of size 512 to represent the Q-function. For DP-SGD updates, we clip all
gradient norms to 1.0. For Acrobot, forε=10, 7.5, 5, we setT(defined in Algorithm 2) equal to 25, 20, 20
respectively. For LunarLander, forε=10, 7.5, we setTequal to 100 and 62 respectively. For CartPole, for
ε=10, 7.5, we setTequal to 25 and 20 respectively. We useT= 50for HIVTreatment.
We tune the following hyperparameters for our method: learning rateη, batch sizeb, probability of sampling
fromD Π unst during training (p), and DP-SGD noise multiplier (s) which is the standard deviation of the
gaussian noise applied to the gradients divided by the clipping threshold. We perform a grid search over all
hyper-parameters. The search spaces for different hyperparameters are as follows:η- [0.0001, 0.0005, 0.001,
0.005, 0.01],b- [64, 128, 256],p- [0.9, 0.8, 0.5, 0.0], ands- [10.0, 20.0, 30.0, 40.0, 50.0, 80.0]. For each
22

Published in Transactions on Machine Learning Research (10/2025)
configuration of hyperparameters, we let the model train for as long as possible with the given value ofε2.
We report the average episodic return obtained over 10 evaluation runs spaced over the last 10000 steps of
training. The best hyper-parameter configurations for each setting are given in Table 3.
Table 3: Best hyper-parameter settings across different environments, offline-RL algorithms andεvalues.
Environmentε CQL BCQ
η b p s η b p s
Acrobot
5 0.001 128 0.0 - 0.01 256 0.0 -
7.5 0.001 128 0.0 - 0.01 256 0.0 -
10 0.0005 128 0.0 - 0.01 256 0.0 -
LunarLander
5 0.0005 256 1.0 80 0.005 64 1.0 10
7.5 0.005 64 0.8 20 0.001 128 0.5 50
10 0.0005 64 0.8 40 0.005 128 0.5 20
CartPole
5 0.005 256 1.0 20 0.005 128 1.0 10
7.5 0.001 128 0.9 50 0.01 128 0.5 20
10 0.0001 128 0.8 80 0.001 128 0.5 40
HIVTreatment
5.0 0.01 256 1.0 10 0.005 128 1.0 20
7.5 0.0001 64 0.0 - 0.005 64 0.9 20
10 0.0001 64 0.0 - 0.005 64 0.9 20
23
