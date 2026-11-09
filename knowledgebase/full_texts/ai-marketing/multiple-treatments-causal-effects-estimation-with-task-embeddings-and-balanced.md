---
title: Multiple Treatments Causal Effects Estimation with Task Embeddings and Balanced Representation
  Learning
url: https://arxiv.org/abs/2511.09814
category: ai-marketing
subcategory: empirical
date: 2025-11
venue: ''
authors:
- Yuki Murakami
- Takumi Hattori
- Kohsuke Kubota
source: arxiv
pdf_url: https://arxiv.org/pdf/2511.09814
pages: 33
chars: 60807
fetched_at: '2026-11-08T13:15:06+00:00'
kb_version: 1
---

# Multiple Treatments Causal Effects Estimation with Task Embeddings and Balanced Representation Learning

Multiple Treatments Causal Effects Estimation
with Task Embeddings and Balanced
Representation Learning
Yuki Murakami1, Takumi Hattori1 and Kohsuke Kubota1*
1NTT DOCOMO, INC.
Abstract
The simultaneous application of multiple treatments is increasingly common in many
fields, such as healthcare and marketing. In such scenarios, it is important to estimate
the single treatment effects and the interaction treatment effects that arise from treatment
combinations. Previous studies have proposed using independent outcome networks with
subnetworks for interactions, or combining task embedding networks that capture treat-
ment similarity with variational autoencoders. However, these methods suffer from the
lack of parameter sharing among related treatments, or the estimation of unnecessary la-
tent variables reduces the accuracy of causal effect estimation. To address these issues,
we propose a novel deep learning framework that incorporates a task embedding network
and a representation learning network with the balancing penalty. The task embedding
network enables parameter sharing across related treatment patterns because it encodes
elements common to single effects and contributions specific to interaction effects. The
representation learning network with the balancing penalty learns representations non-
parametrically from observed covariates while reducing distances in representation dis-
tributions across different treatment patterns. This process mitigates selection bias and
avoids model misspecification. Simulation studies demonstrate that the proposed method
*Corresponding author.
1
arXiv:2511.09814v1  [stat.ME]  12 Nov 2025

outperforms existing baselines, and application to real-world marketing datasets confirms
the practical implications and utility of our framework.
Key words: Causal Inference; Multiple Treatments; Interaction Effect; Deep Neural Net-
works; Task Embedding Network; Balanced Representation Learning
1 INTRODUCTION
Estimating the single and interaction effects of multiple, simultaneously applied treat-
ments is a critical challenge in many fields, such as healthcare and marketing. For ex-
ample, combination drug therapies can lead to complex interactions and unforeseen side
effects that are not apparent from studying each drug in isolation (Gradman et al., 2010;
Webster, 2016; Mokhtari et al., 2017). Similarly, since the total impact of concurrent
marketing promotions often exceeds the simple sum of their single effects, accounting
for these interactions is crucial for optimizing marketing strategy (Danaher et al., 2008;
Lemon and Nowlis, 2002; Lesscher et al., 2021; Naik and Raman, 2003). These situations
demonstrate a critical need for robust analytical frameworks that can precisely estimate
both single and interaction treatment effects to guide effective decision-making.
Whereas existing methods have been proposed to estimate causal effects under multi-
ple treatments, they suffer from critical structural limitations that degrade their perfor-
mance. For example, Neural Counterfactual Relation Estimation (NCoRE) (Parbhoo
et al., 2021) addresses treatment interaction by using separate outcome prediction net-
works for each treatment and additional interaction subnetworks that are activated only
when multiple treatments are applied simultaneously. However, this reliance on separate
networks prevents parameter sharing across similar treatments, which leads to unstable
estimates, especially when samples for specific treatment patterns are limited. Similarly,
Task Embedding–based Causal Effect Variational Autoencoder (TECE-V AE) (Saini et al.,
2019), which combines a treatment similarity–aware task embedding network with a vari-
ational autoencoder, assumes the existence of latent covariates and treats observed ones
2

as proxies. This approach, in turn, introduces a susceptibility to model misspecification,
because its forced estimation of latent variables can be detrimental when observed co-
variates are sufficient. Therefore, the structural constraints of existing methods limit their
ability to provide accurate and robust estimates of both single and interaction treatment
effects.
In this study, we propose a novel deep learning framework called Causal Inference
for Single and Interaction treatment effects Network (CISI-Net). CISI-Net integrates two
core components: a task embedding network designed to capture treatment similarity
and a representation learning network for mitigating selection bias. First, the task em-
bedding network learns to assign similar embedding vectors to similar treatments, and it
places treatment patterns with similar causal effects closer in the embedding space. This
structure enables the embedding vectors to encode components common to single effects
and contributions specific to interaction effects. This alignment allows parameter sharing
across related treatment patterns, which both reduces the need for independent networks
per treatment pattern and improves the stability and accuracy of causal effect estimation
by distinguishing components common to single effects from those specific to interaction
effects. Second, the representation learning network with the balancing penalty learns
representations nonparametrically from the observed covariates while adjusting the rep-
resentation distributions to be aligned across different treatment patterns, which mitigates
selection bias. Unlike TECE-V AE, this data-driven flexibility removes the coercion to
infer latent covariates, and thus reduces the risk of accuracy degradation caused by model
misspecification.
To assess the effectiveness of the proposed framework, we conducted extensive eval-
uations using both three simulations and two real-world datasets. In three simulation
datasets, our method consistently outperformed all baseline approaches in estimating both
single and interaction treatment effects. Our real-world case study based on multiple mar-
keting promotion datasets further demonstrates the practical implications and utility of our
framework.
3

2 RELA TED WORK
This section reviews the main contributions and limitations of the deep learning–based
methods for causal effect estimation. These methods can broadly be categorized into
two groups. The first group consists of methods developed for single-treatment settings,
which primarily aim to estimate the causal effect of one treatment applied in isolation.
These methods can be adapted to multiple-treatment settings by treating each treatment
pattern as a distinct treatment and are commonly used as baselines in multiple-treatment
research (Parbhoo et al., 2021; Saini et al., 2019). The second group consists of methods
developed for multiple-treatment settings. These methods include approaches that extend
single-treatment methods for multiple treatments or are specifically designed to handle
multiple treatments.
Existing methods in the first group, designed for single-treatment settings (Alaa and
van der Schaar, 2018; Johansson et al., 2016; K ¨unzel et al., 2019; Lopez and Gutman,
2017; Shi et al., 2019; Yang et al., 2024; Zhu et al., 2023), are by their very nature
unable to model the interaction effects that arise from the joint application of multiple
treatments. For example, Treatment-Agnostic Representation Network (TARNet) (Shalit
et al., 2017) learns a shared representation that is independent of treatment and uses it to
predict counterfactual outcomes. Counterfactual Regression (CFR) (Shalit et al., 2017)
extends TARNet by introducing a balancing penalty based on Integral Probability Met-
rics (IPM) (Sriperumbudur et al., 2010), which aligns the representation distributions of
the treated and control groups to mitigate selection bias. Although these approaches are
effective for estimating single treatment effects, they are fundamentally limited by their
core assumption of treatment isolation, which makes them incapable of modeling interac-
tions.
In the second group, existing methods for multiple treatments (Mondal et al., 2022;
Parbhoo et al., 2021; Saini et al., 2019; Tsuboi et al., 2024) face two major limitations.
The first limitation is a structural inability to share parameters across related treatments,
4

which leads to unstable estimation under data sparsity caused by the limited number of
samples for specific treatment patterns. The extensions of single-treatment methods can
model interaction effects by assigning independent outcome prediction networks to each
treatment pattern (Parbhoo et al., 2021; Saini et al., 2019). NCoRE introduces interaction
subnetworks that are activated only when multiple treatments are applied simultaneously,
which enables explicit modeling of interaction treatment effects. These methods depend
on having sufficient samples for each treatment pattern because each network is updated
only with samples corresponding to its treatment pattern. Since users who receive mul-
tiple treatments are typically rare (Chu et al., 2022), networks corresponding to infre-
quent treatment patterns remain poorly trained. In addition, because outcome prediction
networks and interaction subnetworks are constructed independently without parameter
sharing across treatments, these methods cannot use similarities among treatments, which
further increases instability in estimation.
The second limitation is a susceptibility to model misspecification. Although TECE-
V AE addresses the first limitation by combining a treatment similarity-aware task embed-
ding network with a V AE, it relies on a V AE that assumes the presence of latent covari-
ates. This method assumes the presence of latent covariates, which are a subset or the
entirety of the true covariates that remain unobserved by the analyst, and treats observed
covariates as proxies for these latent covariates. Even when true covariates are observed,
the model still infers latent covariates, which increases the risk of misspecification and
degrades estimation performance. Such strong assumptions about latent variables can re-
duce robustness and limit the practical applicability of this method in real-world settings.
Our CISI-Net addresses these limitations through two core components. First, the task
embedding network captures treatment similarities by mapping related treatment patterns
to proximal points in an embedding space. This network offers two key advantages over
existing methods. Because it provides a mechanism to disentangle single effects from
interaction effects, it enables the explicit modeling of interaction treatment effects that
single-treatment methods cannot capture. Furthermore, by bringing similar treatments
5

closer together, it facilitates parameter sharing across different treatment patterns, which
improves estimation stability and removes the need for separate networks for each com-
bination. Second, the representation learning network with the balancing penalty directly
learns balanced representations from observed covariates to mitigate selection bias. Cru-
cially, because this data-driven approach does not rely on the rigid latent-covariate as-
sumptions of models like TECE-V AE, this design minimizes the risk of accuracy degra-
dation from model misspecification.
3 CAUSAL INFERENCE UNDER MULTIPLE TREA TMENTS
We formulate the causal inference problem under multiple treatments within the potential
outcomes framework (Rubin, 2005). The goal is to estimate the single and interaction
treatment effects of multiple binary treatments on a continuous outcome using observed
covariates. We considerNindependent units, indexed byi= 1,...,N. For each unit
i, we observe a covariate vectorx i∈R d drawn from the covariate spaceX. There are
Kbinary treatments. For each uniti, let the random variableT i denote the treatment
assignment. Its realization,t i∈{0,1} K, is the vector representing the specific treatment
the unit actually received. Under any possible treatment vectort∈{0,1} K, the potential
outcome for unitiis a scalar valueY i(t)∈R, which represents the outcome that would
have been observed had unitireceived treatmentt. In practice, we only observe one of
these potential outcomes for each unit. The observed outcome is denoted byY i, and the
specific realized outcome is denoted byy i. Therefore, for each uniti, the observed data
consists of the triplet(x i,t i,y i).
To identify causal effects of interest from the observed data, we adopt the following
three assumptions commonly used in observational studies (Imbens and Rubin, 2015).
Assumption 1. (Stable Unit Treatment Value Assumption)(1) no interference, mean-
ing that the outcome of one unit is unaffected by the treatment assignments of other units;
and (2) consistency of treatment, meaning that the potential outcomes correspond to well-
defined and unique treatments (i.e.,Y i =Y i(Ti)).
6

Assumption 2. (Ignorability.)For any treatment pattern, the potential outcome is
independent of the assigned treatmentTgiven the observed covariatesX. Formally, for
allt,
Y(t)⊥T|X
Assumption 3. (Overlap.)Every unit has a non-zero probability of receiving any
treatment pattern given its observed covariates. Formally, for alltandx,
0<P(T=t|X=x)<1
Our estimands of interest, the average single effect (ASE) and the average interaction
effect (AIE), are defined using the conditional expected potential outcomeµ(x,t)given
by
µ(x,t) :=E[Y(t)|X=x
]
.(1)
Under Assumptions 1-3, this quantity is identified from observed data. This key result is
summarized as follows.
Proposition 1.Under Assumptions 1-3, the conditional average potential outcomeµ(x,t)
is identified and is equal to the conditional expectation of the observed outcome as fol-
lows:
µ(x,t) =E[Y|X=x,T=t].(2)
We now formally define our estimands of interest. First, the ASE for treatmentkis
the average effect of applying only treatmentkcompared to no treatment. Lett +k be the
one-hot vector for treatmentk. The ASE is defined as
τASE(k) :=E X [µ(x,t +k)−µ(x,0)].(3)
The ASE is mathematically equivalent to the average combination effect (Egami and Imai,
2019) under the special case where the treatment vector is one-hot, meaning that only
7

a single treatment is applied. The ASE captures the causal effect of applying a single
treatment.
Second, the AIE quantifies the interaction effect for a combination of treatments
S(whereS∈{S ′⊆{1,...,K}||S ′|≥2}) as follows:
τAIE(S) :=E X

∑
Q⊆S
(−1)|S|−|Q|µ ( x,t (+Q) )

,(4)
wheret (+Q) is the treatment vector that sets the components indexed byQto one and all
remaining components to zero. For example, whenK= 2andS={1,2},τ AIE({1,2}) =
Ex[µ(x,(1,1))−µ(x,(1,0))−µ(x,(0,1)) +µ(x,(0,0))].τ AIE({1,2})quantifies how
much the treatment effect oft= (1,1)differs from what would be expected if the treat-
ment effects of(1,0)and(0,1)were simply additive. The AIE represents the interaction
treatment effect that cannot be explained by simply adding up the causal effects of single
treatments.
A direct consequence of Proposition 1 is that our main estimands are also identified.
The proofs for Proposition 1 and Corollary 1 are provided in the Appendix.
Corollary 1.Under Assumptions 1-3, the ASE and AIE are identified.
4 CAUSAL INFERENCE FOR SINGLE AND INTERACTION TREA T-
MENT EFFECTS NETWORK
4.1 MODEL ARCHITECTURE
The objective of CISI-Net is to learnµ(x,t)and estimate the causal effects defined in
(3) and (4) for any possible treatment vectort. Figure 1 illustrates the architecture of
CISI-Net for estimatingˆµ(x,t). The model consists of three main components: (i) a rep-
resentation learning network with the balancing penalty, (ii) a task embedding network,
and (iii) an outcome prediction network. These components are jointly optimized end-
to-end, which ensures that all components are consistently aligned to learnµ(x,t)and
8

Figure 1: The architecture of CISI-Net consists of three components: the representa-
tion learning network (yellow), the task embedding network (green), and the outcome
prediction network (blue). The latent representationΦ(x)is concatenated with the task
embedding vectort w(t)to predict the outcomey. The model is trained with two loss
terms: the prediction lossL y and the balancing penaltyL Φ (red).
reliably estimate the causal effects.
First, the representation learning network with the balancing penalty maps the ob-
served covariatesx∈R d to a latent representation space which is suitable for estimating
causal effects with reduced selection bias. Formally, it learns a functionΦ :R d→R p,
wherepis a hyperparameter indicating the dimensionality of the learned representations.
A balancing penalty based on the IPM (Shalit et al., 2017) is applied to the learned rep-
resentations to minimize the distance between the distributions associated with different
treatment patterns, which reduces selection bias from treatment assignment. This ensures
that counterfactual predictions are not distorted by selection bias arising from differences
in covariate distributions across treatment patterns.
Second, the task embedding network captures similarities among treatment patterns
by mapping the binary treatment vectortinto aq-dimensional continuous task embedding
vector via a multi-layer perceptronMLP w (LeCun et al., 2015). The output is denoted by
tw(t) = MLPw(t)∈R q. This embedding captures similarities among treatments by posi-
9

tioning treatment patterns with related causal effects closer in the embedding space. As a
result, the embedding itself encodes information that distinguishes components common
to single treatments from contributions specific to interaction treatment effects. The em-
bedding vectort w(t)is then passed to the outcome prediction network, where parameter
sharing across similar treatments becomes possible.
Third, the outcome prediction network takes the concatenated vector ofΦ(x)and
tw(t)as input, which forms a(p+q)-dimensional representation, and outputs the predicted
outcomeYusing a neural networkh:R p+q→R. Unlike previous approaches that use
separate networks for each treatment (Mondal et al., 2022; Parbhoo et al., 2021), CISI-Net
uses a single shared prediction functionhfor all treatment patterns. In the task embedding
space, because treatment patterns with similar causal effects are positioned close to each
other, CISI-Net allows the outcome prediction network to reuse parameters across related
treatment patterns. Through this parameter sharing, CISI-Net achieves stable estimation
by avoiding the construction of separate networks for each treatment pattern.
Our model estimates causal effects by predicting counterfactual outcomes based on
the treatment vector as a direct input. Through training, the proposed model learns a
functionˆµ(x,t)composed of a representation networkΦ, a task embedding networkt w,
and an outcome prediction networkh. Instead of using the actual observed treatment
vectort, a counterfactual treatment vectort ′ is fed intoˆµ(x,t), and the causal effect is
estimated by (3) and (4).
4.2 OBJECTIVE FUNCTION
The objective function of CISI-Net provides a principled optimization strategy for simul-
taneously addressing two key challenges in causal effect estimation: maximizing outcome
prediction accuracy and correcting distributional imbalances caused by selection bias.
Optimizing only for the former can result in biased counterfactual predictions, whereas
focusing solely on the latter can compromise the expressive capacity of the model. To
address this balance among accuracy, bias correction, and overfitting, we design the loss
10

functionLas the sum of three components:
L=L y +αL Φ(Φ,t) +β∥w∥ 2,(5)
where the first termL y represents the outcome prediction error, the second termL Φ(·,·)
is a balancing penalty that reduces distributional differences in the representation space
across treatment patterns, and the third term is an L2 regularization term applied to the
network weights. The coefficientsαandβare hyperparameters that control the strength
of the corresponding components.
Minimizing the outcome prediction errorL y is essential for an accurate estimation of
causal effects. When the frequency of observed treatment patterns is imbalanced, cer-
tain treatment patterns may be underrepresented, which results in biased predictions. To
address this issue, we introduce a correction based on the empirical frequency of each
treatment pattern (Shalit et al., 2017; Zhou et al., 2025):
wi(ti) = 1 2

 1
N
N∑
j=1
I[ti =t j]


−1
,(6)
Ly = 1 N N∑ i=1 wi(ti)(yi−ˆyi)2,(7)
whereˆyi denotes the predicted outcome for uniti, andw i(ti)is the scaled inverse of the
relative frequency of the treatmentt i in the observed data.
The second termL Φ is designed to suppress selection bias by aligning the represen-
tation distributions in all treatment patterns. This term is defined by computing the IPM
between the distribution of learned representations of each pair of distinct treatment pat-
terns and averaging these distances. The use of IPM allows us to effectively capture
non-linear discrepancies between probability distributions, and thus contributes to better
generalization in causal effect estimation (Shalit et al., 2017; Shi et al., 2019):
LΦ = 1(|T|
2
)
∑
{a,b}∈(T 2)
IPM(Sa,S b),(8)
11

whereΦ(x)is the representation network mapping the input covariatesxinto a latent
representation space, and we define the set of representations for a given treatment pattern
aasS a :={Φ(x i)|t i =a}. TheIPM(·,·)measures the discrepancy between the two
distributions of two such sets. Here,|T|denotes the number of distinct treatment patterns
and
(|T|
2
)
is the total number of pairs of treatment patterns.
5 SIMULA TION EXPERIMENT
This section describes the experimental setup, the hyperparameters for the proposed and
baseline models, and the evaluation metrics used in the analysis. To evaluate the effective-
ness of the proposed method, we conducted two types of experiments. First, we compared
the proposed method with several existing methods using three simulation datasets to as-
sess the estimation performance. Second, we conducted an ablation study using one of
the three simulation datasets to investigate the contributions of the key components of the
proposed method, specifically the task embedding network and the balancing penalty.
5.1 SIMULATION DATASETS
We design three simulation scenarios to comprehensively evaluate our framework’s per-
formance under different causal directed acyclic graphs and outcome-generating func-
tions. The first scenario, assuming full observability of true covariates, serves as a fun-
damental setting for comparing estimation accuracy against baselines in the presence of
treatment interactions. Building on this, the second scenario introduces latent covari-
ates, which are true covariates but unobservable, to assess the robustness of each method
in a more realistic setting. Finally, the third scenario features multiple treatments but no
interaction effects. This setting is specifically designed to evaluate the robustness of CISI-
Net against model misspecification by testing whether our model maintains performance
even when the data lacks the interaction effects it is built to capture. Collectively, these
scenarios allow for a thorough assessment of our model’s accuracy, robustness to latent
covariates, and resilience to model misspecification.
12

To clarify the words used in this section and beyond, we distinguish among three types
of covariates: true covariates, latent covariates, and observed covariates. First, the true
covariates refer to the complete set of variables that influence both the treatment and the
outcome. When all true covariates are observed, the data satisfy the assumption of no un-
observed covariates. Second, the latent covariates are a subset of or the entirety of the true
covariates that are unobserved by the analyst. They represent unobserved covariates that
may induce bias in the estimation of causal effects if not properly accounted for (Robins
et al., 2000). Third, the observed covariates consist of variables that are the true covariates
themselves or proxy variables that partially capture the information of latent covariates.
The observed covariates represent the variables that are available to the analyst and can be
directly used for causal effect estimation. Even when latent covariates exist, such proxy
variables can mitigate bias (Kuroki and Pearl, 2014).
We vary the structure of the observed covariatesx i,o and the true covariatesx i,t by
scenarios. In all scenarios, only the observed covariatesx i,o are available to the model
during training and evaluation. The true covariatesx i,t are used exclusively for the data-
generating process (i.e., to generate treatments and outcomes) and are treated as unob-
servable to the model at inference time.
In all scenarios, given the true covariatesxi,t, treatment assignment and outcome gen-
eration follow the same functional form, with the number of treatments fixed atK= 3
and the sample size set toN= 50,000. We introduce an indicator variableHto mir-
ror realistic conditions under which treatment assignment depends on true covariates in a
non-smooth and discontinuous (Ascarza, 2018; Djulbegovic et al., 2014).
H=I
(
x(1) i,t +x (2) i,t >1 ) ,
ti,k∼Bern
(
σ
(
w⊤ tkxi,t−λH−δ )) , k= 1,2,3,
ti = (ti,1,t i,2,t i,3),
Yi∼N
(
f(x i,t,t i,l),1 2
)
, l∈{0,1},
13

whereI(·)is the indicator function,σ(·)is the sigmoid function defined asσ(x) = 1/(1+
exp(−x)), andδandλare bias parameters that vary across simulation scenarios. The
vectorw tk is the weight vector whose elements are independently drawn from the uniform
distributionU(−1,1). The outcome-generating functionfis defined as follows:
f(x i,t,t i,l) =w ⊤ x xi,t + (x(1) i,t + 1)ti,1 + 1.2(x(2) i,t + 1)ti,2 + 0.8(x(3) i,t + 1)ti,3
+l
{
(x(4) i,t + 0.5)ti,1ti,2−0.5(x (5) i,t + 1)ti,1ti,3 + 0.1(x(6) i,t + 1)ti,2ti,3
+ 0.7x(7) i,t ti,1ti,2ti,3
}
+ 2,
where vectorw x is the weight vector whose elements are independently drawn from the
uniform distributionU(−1,1), and the parameterl∈{0,1}determines whether interac-
tion effect terms are included (l= 1) or excluded (l= 0).
The first scenario assumes that true covariates are directly observable, as specified by
the following equations:
x(j) i,n∼N(c (j) n ,1 2), x (j) i,u∼U(−1,1),
xi,o =x i,t = (xi,n,x i,u,x i,b),
wherej∈{1,...,15}andc (j) n are drawn from the uniform distributionU(−1,1). In
simulation dataset 1,l= 1,δ= 1andλ= 1.
The second scenario reflects the assumption adopted by deep generative models (Louizos
et al., 2017; Saini et al., 2019) that latent covariates exist. Specifically, it considers
real-world situations where latent covariates, such as the economic status or lifestyle of
units, exist, and only proxy variables, which correspond to the observed covariates (e.g.,
residential area, occupation, purchase history) are observed. Mathematically, this data-
14

generating process is defined as:
zi∼N(0,I 10), x (j) i,n∼N(w (j)⊤ n zi,1 2),
x(j) i,u∼N(w (j)⊤ u zi,5 2), x (j) i,b∼Bern(σ(w (j)⊤ b zi)),
xi,o = (xi,n,x i,u,x i,b),x i,t =z i,
wherej∈{1,...,10}and the vectorsw (j) n ,w (j) u , andw (j) b are weight vectors whose
elements are drawn independently fromU(−1,1).I d denotes the identity matrixd×d,
which is also used as the variance-covariance matrix. In simulation dataset 2,l= 1,
δ= 0.2andλ= 0.1.
The third scenario adapts the structure of true and observed covariates to match that
in the first scenario and assumes multiple treatments exist, with no interaction effects
present. The effect of multiple treatments is calculated simply as the sum of their single
treatment effects. In simulation dataset 3, the interaction treatment effect is eliminated by
setting the interaction effect control parameter tol= 0, and it is set toδ= 1andλ= 1.
5.2 IMPLEMENTATION DETAILS
Our proposed method consists of three neural networks, all of which are built using fully
connected (FC) layers (LeCun et al., 2015) with 200 units per hidden layer and leaky
ReLU activation (Xu et al., 2020). Three neural networks have three hidden layers. The
task embedding networkt w outputs a five-dimensional embedding vector. The balancing
penalty coefficientαwas set to 0.1, and the IPM used in the penalty was the Wasserstein
distance (Sriperumbudur et al., 2010).
To enable a comprehensive comparison between methods that extend single treat-
ment models to multiple treatment settings and those specifically designed for multiple
treatments, we select four baseline methods: TARNet (Shalit et al., 2017), CFR with
Wasserstein-based balancing (CFR-W ASS)(Shalit et al., 2017), TECE-V AE(Saini et al.,
2019), and NCoRE (Parbhoo et al., 2021). To adapt TARNet and CFR-W ASS to the
15

multi-treatment setting, we construct a separate outcome prediction network for each of
the2 K treatment patterns. In CFR-W ASS, the balancing penalty coefficientαis fixed at
one. In TECE-V AE, the latent dimension is set to 25, and the task embedding network
has three hidden layers with 200 units and ELU activation (Clevert et al., 2016). The
task embedding networkt w produces a five-dimensional embedding vector. In NCoRE,
each interaction subnetwork is implemented as two FC layers with 200 units per layer and
ReLU activation (Nair and Hinton, 2010).
All models are trained with Adam optimizer (Kingma and Ba, 2017), and used a
learning rate of10 −5, a batch size of 128, and an L2 regularization of10 −5. Training is
carried out for 30 epochs. Each dataset is divided into training sets of 70% and test sets of
30%, and all evaluations are carried out on the test set. Training a model with one dataset
and evaluating causal effects on an unseen test set is a conventional estimation scheme in
causal inference using machine learning (Liu et al., 2020; Okasa, 2022).
5.3 EVALUATION METRICS
We evaluate the estimation performance of single and interaction treatment effects us-
ing absolute errors. These are defined analogously to the absolute ATE estimation error
commonly used in single-treatment studies (Cheng et al., 2022; Johansson et al., 2016),
and computed as the absolute difference between the true and estimated ASE or AIE.
Specifically, we defineϵ ASE andϵ AIE as follows:
ϵASE(k) =|τ ASE(k)−ˆτASE(k)|,(9)
ϵAIE(S) =|τ AIE(S)−ˆτAIE(S)|,(10)
wherek∈{1,...K}indexes single treatments, andSdenotes a subset of treatments
with|S|≥2.ˆτ ASE(·)andˆτAIE(·)denote the estimated ASE and AIE.
To ensure robustness against randomness in data generation, we generate 100 inde-
pendent datasets for each scenario using different random seeds. For both the baseline
16

comparison and the ablation study, we evaluate each model across these 100 datasets and
report the average of the resultingϵ ASE andϵ AIE.
6 SIMULA TION RESULTS
Table 1 showsϵ ASE andϵ AIE of the proposed and baseline methods across three types
of simulation datasets. In all datasets, CISI-Net consistently achieved the lowestϵ ASE
andϵ AIE, emphasizing its superior ability to accurately estimate both single and inter-
action treatment effects under diverse conditions. In simulation scenario 2, where the
observed covariates are only proxy variables for latent covariates, CISI-Net maintained
high estimation performance. These results demonstrate that even when only proxy vari-
ables rather than true covariates can be observed, CISI-Net can estimate causal effects
with high performance without relying on latent variable estimation. Furthermore, in
simulation scenario 3, where no actual interaction treatment effects exist and the util-
ity of the task embedding network is limited, CISI-Net still achieved the best accuracy.
These results suggest that CISI-Net is flexible, because it captures interaction treatment
effects when they exist and avoids degradation when they do not. This flexibility offers a
significant practical advantage, because it frees analysts from the need to pre-screen for
interaction treatment effects before applying CISI-Net. In this way, CISI-Net ensures sta-
ble performance across various data generation processes, whether interaction is present
or absent, providing both accuracy and reliability compared to baselines.
When extended to multi-treatment settings, single-treatment architectures like TAR-
Net and CFR-W ASS are fundamentally limited by their inability to share information
across similar treatment patterns. Although their original design enables relatively ac-
curate estimation of ASE, these methods treat each treatment pattern independently and
construct separate outcome prediction networks for each case. Because parameter up-
dates occur only for samples that receive the corresponding treatment, they cannot use
similarities among proximity treatment patterns and thus miss opportunities for parame-
ter sharing. This structural limitation explains why these methods, although competitive
17

Table 1: Comparison of mean and standard deviation ofϵ ASE andϵ AIE across simulation
datasets. Here,k∈{1,2,3}indexes single treatments for ASE, andS⊆{1,2,3}(with
|S|≥2) denotes treatment combinations for AIE.
ϵASE ϵAIE
Sim.Methodk= 1k= 2k= 3 S={1,2}S={2,3}S={1,3}S={1,2,3}
1
TARNet 0.11±0.10 0.11±0.07 0.10±0.07 0.18±0.15 0.16±0.12 0.18±0.14 0.34±0.29
CFR-W ASS 0.12±0.09 0.10±0.08 0.10±0.06 0.19±0.12 0.17±0.12 0.17±0.13 0.30±0.19
NCoRE0.10±0.080.10±0.08 0.10±0.08 0.17±0.12 0.16±0.10 0.15±0.11 0.23±0.18
TECE-V AE 0.13±0.10 0.13±0.10 0.12±0.09 0.12±0.080.14±0.10 0.13±0.11 0.21±0.15
CISI-Net 0.10±0.07 0.09±0.08 0.08±0.07 0.12±0.10 0.13±0.10 0.12±0.10 0.12±0.10
2
TARNet0.17±0.150.19±0.160.16±0.15 0.19±0.12 0.18±0.12 0.17±0.12 0.29±0.22
CFR-W ASS0.17±0.140.19±0.17 0.17±0.16 0.19±0.15 0.18±0.14 0.21±0.14 0.33±0.26
NCoRE 0.19±0.17 0.21±0.19 0.19±0.18 0.23±0.17 0.22±0.16 0.20±0.17 0.28±0.22
TECE-V AE 0.19±0.15 0.22±0.16 0.20±0.16 0.32±0.21 0.16±0.14 0.17±0.140.22±0.17
CISI-Net 0.17±0.16 0.18±0.16 0.16±0.14 0.18±0.15 0.14±0.11 0.16±0.11 0.22±0.16
3
TARNet 011±0.08 0.11±0.72 0.10±0.07 0.17±0.12 0.14±0.12 0.16±0.12 0.31±0.26
CFR-W ASS 011±0.08 0.11±0.09 0.10±0.07 0.16±0.13 0.14±0.11 0.16±0.12 0.28±0.20
NCoRE0.10±0.080.10±0.07 0.09±0.06 0.17±0.13 0.16±0.12 0.15±0.13 0.19±0.16
TECE-V AE 0.12±0.10 0.12±0.09 0.10±0.08 0.13±0.110.12±0.09 0.10±0.090.11±0.09
CISI-Net 0.10±0.06 0.09±0.08 0.08±0.06 0.12±0.09 0.12±0.08 0.10±0.08 0.09±0.07
in estimating single treatment effects, are considerably less stable when estimating inter-
action effects. These results suggest that naively extending single-treatment architectures
is insufficient for robust estimation under multiple concurrent treatments.
NCoRE, which possesses interaction subnetworks updated only in samples receiving
multiple treatments, demonstrates the limitations of estimating interaction effects. Since
such samples are typically rare, these subnetworks are poorly trained under data sparsity,
which results in largeϵ AIE. Moreover, its architecture, which constructs outcome and
interaction networks independently, prevents any parameter sharing across treatment pat-
terns. This design misses a critical opportunity to use treatment similarities, which in turn
leads to more unstable estimates. In simulation scenario 3, these interaction subnetworks
become redundant, which in turn limits stable estimation when interaction is absent.
18

Table 2: Ablation study on simulation dataset 1. Here,k∈ {1,2,3}indexes single
treatments for ASE, andS⊆{1,2,3}(with|S|≥2) denotes treatment combinations for
AIE. TE indicates whether the task embedding network is used, and BP indicates whether
the balancing penalty is applied.αis set to 0.1.
ϵASE ϵAIE
TE BPk= 1k= 2k= 3 S={1,2}S={2,3}S={1,3}S={1,2,3}
✗ ✗0.10±0.070.11±0.07 0.10±0.05 0.18±0.10 0.25±0.14 0.25±0.10 0.66±0.04
✓ ✗0.11±0.09 0.11±0.08 0.09±0.07 0.18±0.15 0.19±0.15 0.21±0.14 0.14±0.10
✗ ✓0.10±0.080.10±0.07 0.10±0.06 0.16±0.11 0.23±0.14 0.25±0.13 0.59±0.07
✓ ✓0.10±0.07 0.09±0.08 0.08±0.07 0.12±0.10 0.13±0.10 0.12±0.10 0.12±0.10
Although TECE-V AE captures interaction treatment effects, it underperforms CISI-
Net due to unnecessary latent recovery caused by model misspecification. In simulation
scenario 1, where no latent covariates exist, the model is forced to infer unnecessary latent
variables, which results in degraded accuracy in both ASE and AIE estimation. In simula-
tion scenario 2, where a situation favorable to TECE-V AE, TECE-V AE achieves compet-
itive results only inϵ AIE({1,2,3}). Despite these favorable settings, its performance falls
short of CISI-Net in most metrics. These results show that reliance on latent assumptions
of TECE-V AE degrades robustness across diverse settings compared to CISI-Net.
Table 2 shows the results of an ablation study that evaluates the impact of the task em-
bedding network and the balancing penalty on the performance of CISI-Net. These results
demonstrate that whereas each component individually contributes to performance, com-
bining the task embedding network with a balancing penalty yields the lowest estimation
errors for all metrics. The balancing penalty, which mitigates selection bias, alone im-
proves AIE estimation because units exposed to multiple treatments are subject to strong
selection bias. The task embedding network encodes both components common to single
treatments and contributions unique to interaction effects, and this encoding improves the
accuracy of estimating single and interaction treatment effects. The interaction of each
component enables the model to consistently achieve lower errors across both single and
interaction effects compared to using either component in isolation.
19

Figure 2: Relationship between treatment vector similarity and learned task embedding
vector similarity in simulation dataset 1. For two treatment vectorst 1 andt 2, their corre-
sponding task embedding vectors are denoted ast w(t1)andt w(t2). The x-axis shows the
Jaccard similarity betweent 1 andt 2, and the y-axis shows the cosine similarity between
tw(t1)andt w(t2). Box plots summarize the distribution of cosine similarities for each
Jaccard similarity value.
Figure 2 demonstrates that the learned task embedding vectors by CISI-Net success-
fully reflect the structural similarity of treatment patterns. As the Jaccard similarity (Ji
et al., 2013) between treatment vectors increases, the cosine similarity (Steck et al., 2024)
between their corresponding embedding vectors also rises consistently. This result indi-
cates that the task embedding network captures the overlap in treatment components and
encodes their causal relevance. This architectural choice enables parameter sharing across
related treatment patterns, which in turn supports the accurate estimation of both single
and interaction effects.
Figure 3 showsϵASE andϵ AIE for different values of the balancing penalty coefficientα
20

of our CISI-Net. The results reveal that a small positive value forαconsistently achieves
the lowestϵ ASE andϵ AIE, emphasizing the importance of moderate distributional bal-
ance. This finding illustrates a fundamental trade-off inherent to balancing-based causal
inference methods. Whenα= 0, although the model prioritizes predictive accuracy,
the lack of a balancing penalty introduces significant selection bias, especially for AIE.
Conversely, an excessively largeα(e.g.,α= 10) degrades performance by forcing dis-
tributional consistency at the expense of the predictive power of the representation. This
sensitivity is not a limitation unique to our CISI-Net and is a well-documented character-
istic of models that employ balancing regularization (Johansson et al., 2022; Shalit et al.,
2017). Therefore, developing a mechanism to adjustαbased on data characteristics adap-
tively presents a promising direction for future research, which could enhance the stability
and versatility of this entire class of models.
Figure 4 showsϵ ASE andϵ AIE of CISI-Net under different sample sizes. The results
indicate that bothϵ ASE andϵ AIE decrease as the sample size increases, butϵ AIE remain
high even atN= 10000. Although deep learning methods are powerful tools for causal
inference (Farrell et al., 2021; Green and Kern, 2012), our proposed method relies on large
sample sizes when estimating interaction treatment effects. This strict sample requirement
is a universal and fundamental challenge for nonparametric deep learning methods that
attempt to estimate complex and nonlinear treatment effects (Jiao et al., 2024; Louizos
et al., 2017; Shi et al., 2019; Tsuboi et al., 2024; Wu et al., 2023). Therefore, future
research should explore strategies such as extending methodologies to incorporate prior
knowledge and hierarchical structures to enhance robustness under conditions of limited
sample size.
7 APPLICA TION TO MULTIPLE MARKETING PROMOTIONS
In this section, we apply CISI-Net to a real-world dataset derived from multiple marketing
promotions. The marketing promotions were conducted by merchants affiliated with a
mobile payment platform operated by a mobile payment provider in Japan. The objective
21

Figure 3:ϵ ASE andϵ AIE for different values of the balancing penalty coefficientαin CISS-
Net.
of this analysis is to empirically demonstrate that the CISI-Net can estimate both single
and interaction treatment effects under observational data.
We use two real-world marketing datasets in which multiple marketing promotions
were simultaneously conducted. The first dataset includes three marketing promotions:
two promotions organized by the same merchant group (denoted as CP1 and CP2) and one
online campaign conducted by another merchant group (denoted as CP 3). The observed
sample proportions were approximately 2% for CP1 only, 15% for CP2 only, 42% for CP3
only, 0.2–1% for combinations of two CPs, 0.2% for all three promotions simultaneously,
and the remainder as the control group. The second dataset includes two marketing pro-
motions conducted by two different merchants in the same industry (denoted as CP 4 and
CP5). The observed sample proportions in the second dataset were approximately 29%
22

Figure 4: Estimation errors of CISI-Net under varying sample sizes on simulation dataset
1. The left panel showsϵ ASE, and the right panel showsϵ AIE. Each line represents the
mean error computed over 100 random seeds.
for CP4 only, 4% for CP5 only, 1% for both promotions, and the remainder as the control
group. In all datasets, the control group consisted of users who were not exposed to any
promotion during the treatment period and were randomly sampled from those who had
at least one mobile payment transaction in the month before the promotions to satisfy the
positivity assumption.
In all datasets, we defined the outcome as the total payment amount during the one
month following campaign implementation, and empirically analyzed the single and in-
teraction treatment effects of the two datasets. For numerical stability and confidentiality,
the outcomeYwas standardized within each dataset by using its own overall mean and
standard deviation. Accordingly, the results reported in this section are based on stan-
dardized outcomes. The original-scale causal effects can be recovered by applying the
inverse transformation of the scaler to the model outputs. This preprocessing does not
distort the estimation results because standardization is an affine transformation (Thakral
and Tˆo, 2023). In particular, consistent interpretation between the standardized and orig-
inal scales is ensured because the signs of the estimated causal effects are preserved. The
observed covariates consisted of 71 variables, which included service usage histories and
user demographic attributes.
The hyperparameters of the proposed model were fixed to the same values as those
23

Figure 5: Estimated single and interaction treatment effects obtained from two real-world
marketing promotion datasets. The left panel corresponds to dataset 1 (CP 1-CP3), and
the right panel corresponds to dataset 2 (CP 4 and CP5). Here,τ (d) ASE(k)andτ (d) AIE(S)are
the estimated effects for single and multiple treatments in datasetd. The outcome is
standardized prior to estimation.
described in Section 5.2. We randomly split the dataset into 70% for training and 30%
for testing, and estimated the causal effects on the test set. The model was trained on the
training set, and causal effects were estimated on the test set according to (3) and (4).
Figure 5 shows the estimated causal effects obtained from two real-world marketing
promotion datasets on a standardized outcome scale. In the first dataset (left panel), all
single treatment effects were positive, with CP 3 achieving the largest single treatment
effect among the three promotions. Regarding interaction treatment effectsτ (1) AIE({1,2})
between two promotions conducted by the same merchant group, a positive effect was
observed. On the other hand, the interaction treatment effects between promotions con-
ducted by different merchant groups (τ (1) AIE({2,3}),τ (1) AIE({1,3}), andτ (1) AIE({1,2,3})) ex-
hibited heterogeneous patterns. In the second dataset (right panel), both single treat-
ment effects were positive, withτ (2) ASE(2)being relatively larger. The interaction effect
τ (2) AIE({1,2})was negative, which implies cannibalization between similar promotions
conducted by different merchants.
The results from the first dataset demonstrate that the direction and magnitude of the
interaction treatment effect vary depending on the combination of promotions. The syn-
24

ergy between CP1 and CP2 suggests that conducting multiple promotions within the same
merchant group at the same time increases user engagement more effectively than con-
ducting them separately at different times. This result is consistent with previous studies,
which have shown that within-group promotions often produce synergies by reinforcing
consumer touchpoints (Dorotic et al., 2021; Lesscher et al., 2021; Widdecke et al., 2023;
Zantedeschi et al., 2017). In contrast, the heterogeneous patterns of interaction effects
observed for cross-group promotions (e.g.,τ (1) AIE({2,3})andτ (1) AIE({1,3})) indicate that
promotional effects may vary depending on the degree of market overlap between differ-
ent merchant groups. These results are consistent with findings from partnership loyalty
programs, where collaboration between distinct partners can result in either synergy or
cannibalization depending on context (Dorotic et al., 2021).
The results from the second dataset suggest that significant cannibalization occurs
when competing merchants conduct promotions simultaneously. These results demon-
strate that when similar promotions are conducted by different merchants in the same
industry at the same time, consumers may split their spending across merchants, which
reduces the total promotional effect. Our analysis is consistent with previous research
indicating that overlapping promotions from competing merchants tend to create canni-
balization rather than synergy (Dorotic et al., 2021). Overall, these results show that CISI-
Net reproduces empirically validated behavioral patterns in multi-promotion settings and
enables the estimation of when and where positive or negative interactions emerge.
8 CONCLUSION
In this study, we propose the Causal Inference for Single and Interaction treatment effects
Network (CISI-Net), a novel deep learning framework specifically designed to estimate
both single and interaction effects in multi-treatment scenarios. CISI-Net estimates causal
effects by combining a task embedding network with a representation learning network
with the balancing penalty. CISI-Net encodes both elements common to single effects and
contributions specific to interaction effects by using the task embedding network, thereby
25

improving the stability and accuracy of causal effect estimation. Additionally, CISI-Net
reduces selection bias via the representation learning network with the balancing penalty.
The experimental results demonstrate the effectiveness of CISI-Net. First, the simu-
lation studies show that our CISI-Net consistently outperforms existing baselines in es-
timating causal effects across a wide range of conditions, regardless of the presence of
interaction effects. Second, these findings are validated by our real-world case study, in
which CISI-Net successfully estimated both single and interaction effects from promo-
tional data, and the results are consistent with prior marketing research. These results
suggest that CISI-Net has great potential as a practical analytical tool for applications
such as evaluating combined drug effects in medicine and optimizing complex promo-
tional strategies in marketing.
Our work opens up several important avenues for future research. A first direction is
to explore systematic strategies for selecting or adaptively adjusting the weightαof the
IPM-based balancing penalty, which our results indicate plays a crucial role in balanc-
ing estimation accuracy and selection bias correction. A second direction is to investi-
gate methodological extensions to address the strict sample requirements. This direction
particularly indicates investigating methods for stably estimating interaction treatment
effects, even under conditions where sample sizes per treatment pattern are severely lim-
ited, such as those involving simultaneous multiple treatments. Possible directions for
future research include incorporating prior knowledge or hierarchical structures to stabi-
lize parameter estimation. A third direction is to reduce the risk of model misspecification
further, extend our framework to a doubly robust estimation setting (Chernozhukov et al.,
2018; Kennedy, 2023) by integrating both propensity score modeling and outcome re-
gression.
References
Alaa, A. M. and M. van der Schaar (2018). Bayesian nonparametric causal inference:
Information rates and learning algorithms.IEEE Journal of Selected Topics in Signal
26

Processing 12(5), 1031–1046.
Ascarza, E. (2018). Retention futility: Targeting high-risk customers might be ineffective.
Journal of Marketing Research 55(1), 80–98.
Cheng, L., R. Guo, R. Moraffah, P. Sheth, K. S. Candan, and H. Liu (2022). Evaluation
methods and measures for causal learning algorithms.IEEE Transactions on Artificial
Intelligence 3(6), 924–943.
Chernozhukov, V ., D. Chetverikov, M. Demirer, E. Duflo, C. Hansen, W. Newey, and
J. Robins (2018, 01). Double/debiased machine learning for treatment and structural
parameters.The Econometrics Journal 21(1), C1–C68.
Chu, Z., H. Ding, G. Zeng, Y . Huang, T. Yan, Y . Kang, and S. Li (2022). Hierarchical
capsule prediction network for marketing campaigns effect. InProceedings of the 31st
ACM International Conference on Information & Knowledge Management, CIKM ’22,
New York, NY , USA, pp. 3043–3051. Association for Computing Machinery.
Clevert, D.-A., T. Unterthiner, and S. Hochreiter (2016). Fast and accurate deep network
learning by exponential linear units (elus).
Danaher, P. J., A. Bonfrer, and S. Dhar (2008). The effect of competitive advertising
interference on sales for packaged goods.Journal of Marketing Research 45(2), 211–
225.
Djulbegovic, B., S. Elqayam, T. Reljic, I. Hozo, B. Miladinovic, A. Tsalatsanis, A. Ku-
mar, J. Beckstead, S. Taylor, and J. Cannon-Bowers (2014). How do physicians decide
to treat: an empirical evaluation of the threshold model.BMC Medical Informatics and
Decision Making 14(1), 47.
Dorotic, M., D. Fok, P. C. Verhoef, and T. H. A. Bijmolt (2021, Sep). Synergistic and
cannibalization effects in a partnership loyalty program.Journal of the Academy of
Marketing Science 49(5), 1021–1042.
27

Egami, N. and K. Imai (2019). Causal interaction in factorial experiments: Application to
conjoint analysis.Journal of the American Statistical Association 114(526), 529–540.
Farrell, M. H., T. Liang, and S. Misra (2021). Deep neural networks for estimation and
inference.Econometrica 89(1), 181–213.
Gradman, A. H., J. N. Basile, B. L. Carter, and G. L. Bakris (2010). Combination therapy
in hypertension.Journal of the American Society of Hypertension 4(2), 90–98.
Green, D. P. and H. L. Kern (2012, 09). Modeling heterogeneous treatment effects in
survey experiments with bayesian additive regression trees.Public Opinion Quar-
terly 76(3), 491–511.
Imbens, G. W. and D. B. Rubin (2015).Causal inference in statistics, social, and biomed-
ical sciences. Cambridge university press.
Ji, J., J. Li, S. Yan, Q. Tian, and B. Zhang (2013). Min-max hash for jaccard similarity.
In2013 IEEE 13th International Conference on Data Mining, pp. 301–309.
Jiao, L., Y . Wang, X. Liu, L. Li, F. Liu, W. Ma, Y . Guo, P. Chen, S. Yang, and B. Hou
(2024). Causal inference meets deep learning: A comprehensive survey.Research 7,
0467.
Johansson, F., U. Shalit, and D. Sontag (2016, 20–22 Jun). Learning representations for
counterfactual inference. In M. F. Balcan and K. Q. Weinberger (Eds.),Proceedings of
The 33rd International Conference on Machine Learning, V olume 48 ofProceedings
of Machine Learning Research, New York, New York, USA, pp. 3020–3029. PMLR.
Johansson, F. D., U. Shalit, N. Kallus, and D. Sontag (2022). Generalization bounds and
representation learning for estimation of potential outcomes and causal effects.Journal
of Machine Learning Research 23(166), 1–50.
Kennedy, E. H. (2023). Towards optimal doubly robust estimation of heterogeneous
causal effects.Electronic Journal of Statistics 17(2), 3008 – 3049.
28

Kingma, D. P. and J. Ba (2017). Adam: A method for stochastic optimization.
K¨unzel, S. R., J. S. Sekhon, P. J. Bickel, and B. Yu (2019). Metalearners for estimating
heterogeneous treatment effects using machine learning.Proceedings of the National
Academy of Sciences 116(10), 4156–4165.
Kuroki, M. and J. Pearl (2014, 03). Measurement bias and effect restoration in causal
inference.Biometrika 101(2), 423–437.
LeCun, Y ., Y . Bengio, and G. Hinton (2015). Deep learning.Nature 521(7553), 436–444.
Lemon, K. N. and S. M. Nowlis (2002). Developing synergies between promotions and
brands in different price-quality tiers.Journal of Marketing Research 39(2), 171–185.
Lesscher, L., L. Lobschat, and P. C. Verhoef (2021). Do offline and online go hand in
hand? cross-channel and synergy effects of direct mailing and display advertising.
International Journal of Research in Marketing 38(3), 678–697.
Liu, R., C. Yin, and P. Zhang (2020). Estimating individual treatment effects with time-
varying confounders. In2020 IEEE International Conference on Data Mining (ICDM),
pp. 382–391.
Lopez, M. J. and R. Gutman (2017). Estimation of causal effects with multiple treatments:
A review and new ideas.Statistical Science 32(3), 432–454.
Louizos, C., U. Shalit, J. M. Mooij, D. Sontag, R. Zemel, and M. Welling (2017). Causal
effect inference with deep latent-variable models. In I. Guyon, U. V . Luxburg, S. Ben-
gio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett (Eds.),Advances in Neural
Information Processing Systems, V olume 30. Curran Associates, Inc.
Mokhtari, R. B., T. S. Homayouni, N. Baluch, E. Morgatskaya, S. Kumar, B. Das, and
H. Yeger (2017). Combination therapy in combating cancer.Oncotarget 8(23), 38022.
Mondal, A., A. Majumder, and V . Chaoji (2022). MEMENTO: Neural model for esti-
mating individual treatment effects for multiple treatments. InProceedings of the 31st
29

ACM International Conference on Information & Knowledge Management, CIKM ’22,
New York, NY , USA, pp. 3381–3390. Association for Computing Machinery.
Naik, P. A. and K. Raman (2003). Understanding the impact of synergy in multimedia
communications.Journal of Marketing Research 40(4), 375–388.
Nair, V . and G. E. Hinton (2010). Rectified linear units improve restricted boltzmann
machines. InProceedings of the 27th International Conference on International Con-
ference on Machine Learning, ICML’10, Madison, WI, USA, pp. 807–814. Omnipress.
Okasa, G. (2022). Meta-learners for estimation of causal effects: Finite sample cross-fit
performance.
Parbhoo, S., S. Bauer, and P. Schwab (2021). NCoRE: Neural counterfactual representa-
tion learning for combinations of treatments.
Robins, J. M., A. Rotnitzky, and D. O. Scharfstein (2000). Sensitivity analysis for selec-
tion bias and unmeasured confounding in missing data and causal inference models. In
M. E. Halloran and D. Berry (Eds.),Statistical Models in Epidemiology, the Environ-
ment, and Clinical Trials, New York, NY , pp. 1–94. Springer New York.
Rubin, D. B. (2005). Causal inference using potential outcomes.Journal of the American
Statistical Association 100(469), 322–331.
Saini, S. K., S. Dhamnani, A. Srinivasan, A. A. Ibrahim, and P. Chavan (2019). Multi-
ple treatment effect estimation using deep generative model with task embedding. In
The World Wide Web Conference, WWW ’19, New York, NY , USA, pp. 1601–1611.
Association for Computing Machinery.
Shalit, U., F. D. Johansson, and D. Sontag (2017, 06–11 Aug). Estimating individual treat-
ment effect: generalization bounds and algorithms. In D. Precup and Y . W. Teh (Eds.),
Proceedings of the 34th International Conference on Machine Learning, V olume 70 of
Proceedings of Machine Learning Research, pp. 3076–3085. PMLR.
30

Shi, C., D. Blei, and V . Veitch (2019). Adapting neural networks for the estimation
of treatment effects. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alch ´e-Buc,
E. Fox, and R. Garnett (Eds.),Advances in Neural Information Processing Systems,
V olume 32. Curran Associates, Inc.
Sriperumbudur, B. K., K. Fukumizu, A. Gretton, B. Sch ¨olkopf, and G. R. G. Lanckriet
(2010). Non-parametric estimation of integral probability metrics. In2010 IEEE Inter-
national Symposium on Information Theory, pp. 1428–1432.
Steck, H., C. Ekanadham, and N. Kallus (2024). Is cosine-similarity of embeddings
really about similarity? InCompanion Proceedings of the ACM Web Conference 2024,
WWW ’24, New York, NY , USA, pp. 887–890. Association for Computing Machinery.
Thakral, N. and L. T. Tˆo (2023).When are estimates independent of measurement units?
Boston University-Department of Economics.
Tsuboi, Y ., Y . Sakai, R. Shimizu, and M. Goto (2024). Multiple treatment effect es-
timation for business analytics using observational data.Cogent Engineering 11(1),
2300557.
Webster, R. M. (2016). Combination therapies in oncology.Nature Reviews Drug Dis-
covery 15(2), 81–82.
Widdecke, K. A., W. I. Keller, K. Gedenk, and B. Deleersnyder (2023). Drivers of the
synergy between price cuts and store flyer advertising at supermarkets and discounters.
International Journal of Research in Marketing 40(2), 455–474.
Wu, A., K. Kuang, R. Xiong, B. Li, and F. Wu (2023, 23–29 Jul). Stable estimation of
heterogeneous treatment effects. In A. Krause, E. Brunskill, K. Cho, B. Engelhardt,
S. Sabato, and J. Scarlett (Eds.),Proceedings of the 40th International Conference on
Machine Learning, V olume 202 ofProceedings of Machine Learning Research, pp.
37496–37510. PMLR.
31

Xu, J., Z. Li, B. Du, M. Zhang, and J. Liu (2020). Reluplex made more practical: Leaky
ReLU. In2020 IEEE Symposium on Computers and Communications (ISCC), pp. 1–7.
Yang, H., Z. Sun, H. Xu, and X. Chen (2024). Revisiting counterfactual regression
through the lens of gromov-wasserstein information bottleneck.
Zantedeschi, D., E. M. Feit, and E. T. Bradlow (2017). Measuring multichannel advertis-
ing response.Management Science 63(8), 2706–2728.
Zhou, C., Y . Li, C. Zheng, H. Zhang, M. Zhang, H. Li, and M. Gong (2025). A two-stage
pretraining-finetuning framework for treatment effect estimation with unmeasured con-
founding. InProceedings of the 31st ACM SIGKDD Conference on Knowledge Discov-
ery and Data Mining V .1, KDD ’25, New York, NY , USA, pp. 2113–2123. Association
for Computing Machinery.
Zhu, F., J. Lu, A. Lin, J. Xuan, and G. Zhang (2023). Direct learning with multi-task
neural networks for treatment effect estimation.IEEE Transactions on Knowledge and
Data Engineering 35(3), 2457–2470.
APPENDIX
PROOFS OF IDENTIFIABILITY
This appendix provides the proofs for the identifiability of the causal estimands introduced
in Section 3. We first provide the proof of Proposition 1.
Proof.The proof proceeds by a sequence of equalities, starting from the definition of
µ(x,t):
µ(x,t) :=E[Y(t)|X=x](by Definition in (1))
=E[Y(t)|X=x,T=t](by Assumption 2)
=E[Y|X=x,T=t](by Assumption 1)
32

Assumption 3 ensures this final quantity is well-defined. This completes the proof of
identifiability forµ(x,t).■
Second, we provide the proof of Corollary 1.
Proof.The ASE and AIE are defined as functions of the conditional average potential
outcomeµ(x,t). Specifically, they are constructed using linear combinations and ex-
pectations over the distributions ofX. Since Proposition 1 establishes thatµ(x,t)is
identifiable from observed data, any quantities derived from it through these operations
are also identifiable.■
33
