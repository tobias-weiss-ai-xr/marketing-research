---
title: Will the Carbon Border Adjustment Mechanism Impact European Electricity Prices? A GNN-Based Network
  Analysis
url: https://arxiv.org/abs/2605.03304
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Jiachen Shen
- Jian Shi
- Dan Wang
- Han Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.03304
pages: 5
chars: 21326
fetched_at: '2026-11-08T13:01:56+00:00'
kb_version: 1
---

# Will the Carbon Border Adjustment Mechanism Impact European Electricity Prices? A GNN-Based Network Analysis

Will the Carbon Border Adjustment Mechanism
Impact European Electricity Prices? A GNN-Based
Network Analysis
Jiachen Shen, Jian Shi, Dan Wang and Zhu Han
Abstract—The European Union’s Carbon Border Adjustment
Mechanism (CBAM) creates a complex challenge for the intercon-
nected European electricity market. Traditional static analyses
often miss the cross-border spillover effects that are vital for
understanding this policy. This paper addresses this gap by
developing a spatio-temporal Graph Neural Network (GNN)
framework. It quantifies how CBAM affects electricity prices and
carbon intensity (CI) at the same time. We modeled a subgraph
of eight European countries. Our results suggest that CBAM is
not just a uniform tax. Instead, it acts as a tool that transforms
the market and creates structural differences. In our simulated
scenarios, we observe that low-carbon countries like France and
Switzerland can gain a competitive advantage. This suggests a
potential decrease in their domestic electricity prices. Meanwhile,
high-carbon countries like Poland face a double burden of rising
costs. We identify the primary driver as a fundamental shift in
the market’s merit order.
Index Terms—Carbon Border Adjustment Mechanism
(CBAM), European Electricity Market, Graph Neural Network
(GNN), Network Analysis, Electricity Prices, Carbon Intensity.
I. INTRODUCTION
The European Union (EU) has committed to ambitious
climate goals under the European Green Deal [1]. This in-
cludes the Carbon Border Adjustment Mechanism (CBAM)
to address carbon leakage [2], [3]. This policy arrives while
people are very sensitive about European energy costs. This
follows a recent energy crisis that caused prices to surge.
Consequently, there is significant public concern that CBAM
will be just another tax that burdens consumers.
This paper challenges that assumption. We ask a simple
question. Is this blame accurate? Does CBAM add costs
uniformly, or could its true impact on electricity prices be
more complex and asymmetric? The question is not trivial
because the European power grid is a deeply interconnected
network. It is not a set of isolated markets [4], [5]. Static,
single-country analyses often miss the dynamic, cross-border
spillover effects that define this system. To address this gap,
we develop a modeling framework based on Graph Neural
Networks (GNNs). This allows us to capture these dynamic,
networked effects better than static analysis.
Our analysis suggests that CBAM is not a uniform financial
burden. Instead, it acts as a market transformation tool that
This work is partially supported by NSF ECCS-2338158
J. Shen, J. Shi, and Z. Han are with the Departments of Electrical and
Computer Engineering and Engineering Technology, University of Hous-
ton, Houston, TX, USA. D. Wang is with The Hong Kong Polytechnic
University, Hong Kong. (e-mail:{jshen24, jshi23@central, zhan2}@uh.edu,
dan.wang@polyu.edu.hk).
creates clear differences between countries. We find that low-
carbon countries like France and Switzerland gain a significant
competitive advantage. In our simulated scenarios, the model
suggests that CBAM may lead to a decrease in domestic
electricity prices for these nations. Conversely, high-carbon
grids like Poland and the Czech Republic face a dual challenge
of rising costs and lost competitiveness. We identify the
primary driver as a fundamental shift of the market’s merit
order. The main contributions of this paper are threefold:
•We develop a novel dual-target GNN framework to model
the relationship between price and carbon intensity. This
extends beyond previous single-task forecasting models
[6].
•We provide quantitative, network-aware evidence that
challenges the idea of a uniform tax. We demonstrate
asymmetric economic impacts in our simulations, includ-
ing potential price decreases for specific regions.
•We identify the market mechanisms like merit-order
shifting that drive this divergence. Because we cannot
observe ground truth for a policy that has not fully
happened yet, we focus on internal validity. We support
our findings through predictive back-testing on observed
data, robustness checks, and placebo tests.
II. BACKGROUND ANDMETHODOLOGY
A. CBAM and the Network-Based Challenge
The CBAM regulation requires importers to submit cer-
tificates for the embedded emissions of imported electricity
[3]. The European market is highly coupled and managed
by ENTSO-E [7]. In this system, electricity is pooled. This
makes it nearly impossible to trace the exact origin and carbon
content of an imported megawatt-hour [4]. This complexity
requires a network-based model. A tax applied at one border
like Germany will not stop there. Its cost will factor into
market bids. This influences trade and alters supply and
demand for all neighbors like France and Poland. It eventually
creates spillover effects [8]. These effects vary over time. This
requires a graph analysis that considers both space and time.
B. Spatiotemporal GNN Framework
Our approach extends the carbon intensity forecasting
model (CFCG) presented in [6]. The original CFCG model
is a single-task framework. It was designed only to predict
carbon intensity (CI). Our main innovation is a dual-target,
multi-task learning architecture. This allows us to model and
arXiv:2605.03304v1  [cs.LG]  5 May 2026

Fig. 1: Our dual-target GNN architecture. It shows the shared encoder
and parallel task-specific (CI and Price) MLP heads.
predict two coupled market variables together: electricity Price
(YP rice) and Carbon Intensity (Y CI ). This section details the
theoretical foundation of our framework.
1) Dual-Target Problem Formulation:Price and CI are not
independent. Under CBAM, they are explicitly linked. The
policy adds a carbon cost to the base price:P CBAM t =
P base t +τ·CI t +ϵ t. This creates a non-zero covariance
(Cov(CIt, Pt)̸= 0) that a single-task model would miss.
Therefore, we formulate the problem as a multi-task learning
challenge.
The original CFCG model optimized a single loss
LCF CG= minθ E[ℓ(fθ(x), yCI )]. In contrast, our dual-target
framework optimizes a composite loss function:
Ldual = min θ,ϕ E(x,y)∼D
h
λ1 ·MSE(Y CI , ˆYCI )
+λ 2 ·MSE(Y P rice, ˆYP rice) +λ3 · LCorr
i (1)
Here,λ 1, λ2, λ3 are weighting hyperparameters. The first two
terms are standard Mean Squared Error (MSE) losses for
each task. The third term,L Corr , is a novel Correlation
Loss. It ensures the model preserves the underlying correlation
structure between the two targets:
LCorr =

ρ(YCI , YP rice)−ρ( ˆYCI , ˆYP rice)

 (2)
whereρ(·,·)is the Pearson correlation coefficient. This term
acts as a coupling regularization. This approach is based on
multi-task learning theory [9], [10], which provides two key
benefits:Inductive Bias Transfer, where the model is forced
to find a joint hypothesis spaceH joint =H CI ∩ HP ricelead-
ing to more generalizable features; andStatistical Efficiency,
as joint estimation reduces parameter variance compared to
independent training.
2) Model Architecture and Optimization:We design a
parallel architecture to learn this representation efficiently (Fig.
1). Instead of using the complex GNN-LSTM stacks found in
the original CFCG, our model employs a shared GNN encoder
(GNNθ) to extract features from the input graphG= (V, E),
utilizing node featuresXand adjacency matrixA. This shared
encoder learns a latent representationZthat captures the
network-wide state:
Z=GNN θ(X, A)∈R |V|×d (3)
Subsequently, this shared representationZis processed by
two parallel, independent Task-Specific Heads implemented
Algorithm 1Dual-Target GNN Training Framework
1:Input:GraphG= (V, E), FeaturesX(incl. policy), Adjacency
A, Ground TruthY CI , YP rice, Loss weightsλ 1, λ2, λ3
2:Output:Trained models GNN θ, MLP CI , MLP P rice
3:Initialize parametersθ(for GNN θ),ϕ CI (for MLP CI ),ϕ P rice
(for MLP P rice)
4:foreach training epochdo
5:▷Shared GNN Encoder (Eq. 3)
6:Z←GNN θ(X, A)▷Task-specific attention applied
7:▷Parallel Task-Specific Heads (Eq. 4)
8: ˆYCI ←MLP CI (Z;ϕ CI )
9: ˆYP rice←MLP P rice(Z;ϕ P rice)
10:▷Calculate Multi-Task Loss (Eq. 1)
11:L M SE−CI←MSE(Y CI , ˆYCI )
12:L M SE−P rice←MSE(Y P rice, ˆYP rice)
13:L Corr ←

ρ(YCI , YP rice)−ρ( ˆYCI , ˆYP rice)

14:L dual ←λ 1LM SE−CI+λ 2LM SE−P rice+λ 3LCorr
15:▷Backpropagation
16:Updateθ, ϕ CI , ϕP riceusing∇L dual
17:end for
18:returnθ, ϕ CI , ϕP rice
as Multi-Layer Perceptrons (MLPs). These simpler heads cor-
respond to our dual targets and generate the final predictions:
ˆYCI =MLP CI (Z), ˆYP rice=MLP P rice(Z)(4)
This architecture is much more efficient. The complexity of
the original GNN in CFCG isO GN N=O(|V|·d in ·dout ·|R|).
Here,|R|is the number of relations. Our MLP-based approach
isO M LP=O(|V|·d in ·h+h·d out), wherehis much smaller
thand in ·|R|. This simplification is supported by the Universal
Approximation Theorem for GNNs. It states that GNNs can
approximate any continuous function on a compact set of
graphs [11]. Our shared encoder finds aZthat maximizes
the mutual information for both tasks. This ensures minimal
information loss.
3) Task-Specific Attention Enhancement:We enhance the
GNN encoder with task-specific attention mechanisms to re-
fine the shared representation. The shared encoder learns a
general graph structure. However, the attention weights for
predicting CI may differ from those for predicting Price. We
implement this by making the attention calculation dependent
on the task:
αtask ij = exp(LeakyReLU(aT task[Wtaskhi∥Wtaskhj ]))P
k∈N(i) exp(LeakyReLU(aT task[Wtaskhi∥Wtaskhk])) (5)
wheretask∈ {CI, P rice}. This allows the model to weigh
neighbors (j) differently when creating the representation for
a node (i). It depends on the final objective and improves how
the parallel MLP heads specialize.
III. EXPERIMENTALSETUP
A. Data and Scope
Our analysis focuses on a critical subgraph of the intercon-
nected European grid: Austria (AT), Switzerland (CH), Ger-
many (DE), France (FR), Italy (IT), Netherlands (NL), Poland
(PL), and the Czech Republic (CZ). We utilize public, hourly
time-series data from the ENTSO-E Transparency Platform
[12] (8,759 observations), covering demand, generation mix,

Fig. 2: Predicted CBAM impact on hourly CI. The policy suppresses CI in high-carbon nations like Poland and Czech Republic but not
low-carbon ones like France and Switzerland.
Fig. 3: Predicted CBAM impact on hourly Electricity Prices. Note the counter-intuitive price decrease in low-carbon nations (CH, NL).
cross-border flows, and day-ahead prices. The model is trained
on 70% of the data, validated on 15%, and tested on the
remaining 15%.
To facilitate our analysis, we categorize these countries
based on their average generation-based CI: Low-Carbon (CH,
FR; CI<50 kg CO2/MWh), Medium-Carbon (AT, DE, IT,
NL; 50<CI<130), and High-Carbon (PL, CZ; CI>130)
[13].
B. CBAM Scenario Design
We simulate five scenarios with linear CBAM intensity
increments (0%, 25%, 50%, 75%, 100%) targeting implemen-
tation years 2025–2035. The financial impact of the policy is
calculated as an added cost to cross-border transactions, based
on the carbon intensity of the exporting grid. A key assumption
of our model is the establishment of a carbon intensity
threshold, below which the CBAM cost is not applied. Based
on the low-carbon countries (CH and FR) identified in our
preliminary analysis, we set this threshold at 50 kg CO2/MWh.
We also assume a proxy EU Emissions Trading System (ETS)
price of 85 EUR/tCO2, a reasonable estimate reflecting market
volatility and price levels seen in 2023-2024 [14].
The CBAM cost is thus formulated as:
Cost(EUR/MWh)= max(0, CI−50)×Intensity× ET S 1000 (6)
whereCIis the hourly carbon intensity of the exporter
(kg CO2/MWh),ET Sis the carbon price (EUR/tCO2), and
Intensityis the implementation phase (0.25 to 1.0). Section
IV reports sensitivity over CI threshold and ETS price, and a
placebo policy injection test. This calculatedCostis the core
policy variable injected into our model to predict the market’s
response.
IV. RESULTS ANDANALYSIS
Our analytical framework allows us to analyze the differ-
ential impacts of the CBAM policy across all countries in
the network, both in terms of environmental effectiveness
(carbon intensity) and economic consequences (electricity
price). Before detailing these impacts, we verified the model’s
reliability: our proposed framework achieves a test RMSE
of 4.20 EUR/MWh for price prediction, outperforming the

Fig. 4: Scatter plot comparing price impacts predicted by our GNN
(y-axis) vs. a traditional spatial-lag baseline (x-axis).
baseline spatial-lag model (RMSE: 5.42) and ablations lacking
policy features (see Table I), thereby establishing a reliable
foundation for counterfactual inference.
A. Differential Impact on Carbon Intensity and Price
Our primary finding (Fig. 2) is that CBAM creates divergent
results. For PL and CZ, the model predicts a significant CI
reduction as policy intensity increases, while the impact on
low-CI nations (FR, CH) is negligible.
More strikingly, Fig. 3 reveals a counter-intuitive finding:
while high-carbon countries (PL, CZ) experience a clear price
increase, low-carbon countries (CH, NL) show systematically
lower prices under a Full CBAM scenario. This suggests
CBAM is not a simple tax but a market-restructuring tool.
To further validate this asymmetric impact, we benchmarked
our GNN model against a traditional spatial-lag econometric
baseline. As shown in Fig. 4, the two models exhibit strong
directional agreement, with high-carbon nations consistently
clustering in the positive impact quadrant and low-carbon
nations in the negative zone. This methodological consensus
confirms that the observed price asymmetry is a robust struc-
tural feature of the European grid, rather than a model-specific
artifact.
B. Geographic Divergence of Impacts
The national-level price and CI impacts aggregate into a
clear geographic pattern of asymmetric impacts, as visualized
in Fig. 5. The Carbon Intensity Reduction map confirms the
environmental gains are concentrated in the high-CI regions
of Eastern Europe. The Price Increase map illustrates the
economic trade-off, showing that these same regions bear the
brunt of the costs. Our impact classification map synthesizes
the net effect: regions with favorable outcomes (CH, FR,
and SE); nations facing significant challenges (PL, CZ); and
transitioning hubs (DE and AT).
C. Uncovering the Mechanisms of Transformation
The key question arising from these results is: why do prices
decrease for clean-energy countries? Our analysis points to two
fundamental market mechanisms.
First, CBAM triggers a dramatic Import Source Substitution
(Fig. 6), where market reliance on coal-based imports plum-
mets (from 40% to 15%), absorbed primarily by nuclear (15%
to 30%) and renewables (10% to 30%).
Fig. 5: Geographic distribution of CBAM’s impact, identifying re-
gions with favorable outcomes (e.g., CH, FR) and those facing
significant challenges (e.g., PL, CZ).
Fig. 6: Import Source Substitution under Full CBAM, showing a
structural shift from coal to nuclear and renewables.
We quantify this substitution mechanism in Fig. 7, which
correlates the change in clean electricity import share with
domestic price impacts. The scatter plot reveals distinct clus-
ters: High-carbon nations (red) pay a premium for substitution
(driving prices up), whereas low-carbon nations (green) benefit
from improved trade terms.
Second, this substitution is driven by a Merit-Order Reshuf-
fling. By adding a cost (Eq. 6) to high-carbon electricity,
CBAM pushes fossil-fuel generators to the back of the supply
queue, elevating low-cost nuclear and renewable power to a
more dominant, price-setting position [15]. Fig. 8 quantifies
this, showing low-carbon countries (CH, FR) gaining a strong
competitive advantage (green) over high-carbon ones (PL,
CZ).
D. Robustness and Credibility
Given the counterfactual nature of this study, verifying
the causality is crucial. We conducted extensive robustness
checks, summarized in Table I. The results confirm high
directional consistency (SignAgree>0.9) across sensitivity
sweeps. Crucially, in placebo tests where the policy variable
is randomized, the effect magnitude attenuates by over 80%
(Atten.<0.25), confirming that the observed impacts are

Fig. 7: The trade-off between grid decarbonization (x-axis) and
economic cost (y-axis).
Fig. 8: CBAM Competitiveness Matrix. Low-carbon nations (CH, FR)
gain a competitive advantage (green) over high-carbon ones (PL, CZ).
causal consequences of the CBAM signal and not statistical
artifacts.
V. POLICYIMPLICATIONS ANDCONCLUSION
A. Policy Implications
Our findings demonstrate that CBAM functions not merely
as a border tax, but as a mechanism for deep market re-
structuring with highly asymmetric outcomes. The statistically
significant “dual burden” identified for high-carbon nations
(e.g., PL, CZ)—characterized by unavoidable price hikes and
the high cost of import substitution—underscores the critical
necessity of a robust “Just Transition” mechanism [16]. Policy
interventions should consider using CBAM revenues not just
for general redistribution, but specifically to subsidize grid
modernization in eastern regions to lower the substitution
premium. Conversely, the structural advantage identified for
low-carbon producers (e.g., FR, CH) confirms that early
decarbonizers are effectively shielded from external carbon
costs, creating a powerful market-based incentive for rapid
green transition.
B. Conclusion
This paper presents a spatio-temporal, network-based analy-
sis of the CBAM’s impact on the European electricity market.
By developing a dual-target GNN framework and validating
it against spatial-lag baselines and extensive placebo tests, we
move beyond static estimates to capture the dynamic spillover
TABLE I: Robustness checks. Ref:T= 50, ETS=85. Metrics: Sign
Agreement (SignAgree), Rank Correlation (ρ), and Attenuation Ratio
(Atten.).
Check Design SignAgree↑ρ↑Atten.↓
Sensitivity (T) Threshold∈
{25,50,75}
0.92 0.88 –
Sensitivity (E) ETS∈ {70,85,100}0.96 0.95 –
Placebo (Time) Shuffle cost over time 0.53 0.04 0.18
Placebo (Node) Permute cost over nodes 0.48 -0.12 0.22
Baseline Spatial-lag Panel 0.85 0.78 –
effects defining this complex system. Our primary finding
is that CBAM drives a structural divergence rather than a
uniform price increase. High-carbon countries face a robust
economic challenge driven by merit-order reshuffling, while
low-carbon countries gain a significant competitive advantage.
Our model suggests this advantage creates a buffer against
price hikes, with the potential to lower domestic electricity
prices under specific network conditions. These results provide
critical evidence that while CBAM effectively accelerates the
green transition through import substitution, its asymmetric
economic consequences must be actively managed to ensure
political and economic stability.
REFERENCES
[1] European Commission, “The european green deal,” Communication
from the Commission, COM(2019) 640 final, December 2019.
[2] C. B ¨ohringer, E. J. Balistreri, and T. F. Rutherford, “The role of border
carbon adjustment in unilateral climate policy: Overview of an energy
modeling forum study (emf 29),”Energy Economics, vol. 34, pp. S97–
S110, 2012.
[3] European Parliament and Council of the EU, “Regulation (eu) 2023/956
of the european parliament and of the council of 10 may 2023 estab-
lishing a carbon border adjustment mechanism,” Official Journal of the
European Union, L 130/52, May 2023.
[4] Eurelectric, “A carbon border adjustment mechanism (cbam) fit for the
power sector,” Position Paper, Eurelectric, Tech. Rep., March 2025.
[5] D. Newbery, G. Strbac, and I. Viehoff, “The benefits of integrating
european electricity markets,”Energy Policy, vol. 94, pp. 253–263, 07
2016.
[6] X. Zhang and D. Wang, “A gnn-based day ahead carbon intensity
forecasting model for cross-border power grids,” inProceedings of
the 14th ACM International Conference on Future Energy Systems,
ser. e-Energy ’23. New York, NY , USA: Association for Computing
Machinery, 2023, p. 361–373.
[7] L. Meeus, K. Purchala, and R. Belmans, “Development of the internal
electricity market in europe,”The Electricity Journal, vol. 18, no. 6, pp.
25–35, 2005.
[8] S. Cevik, “Shocked: Electricity Price V olatility Spillovers in Europe,”
IMF Working Papers, vol. 2025, no. 007, p. 1, 1 2025.
[9] R. Caruana,Multitask learning. USA: Kluwer Academic Publishers,
1998, p. 95–133.
[10] S. Ruder, “An overview of multi-task learning in deep neural networks,”
ArXiv, 2017.
[11] K. Xu, W. Hu, J. Leskovec, and S. Jegelka, “How powerful are graph
neural networks?”ArXiv, vol. abs/1810.00826, 2018.
[12] ENTSO-E, “Entso-e transparency platform,” Online Database, 2024.
[13] Ember, “European electricity review 2023,” Ember, Tech. Rep., January
2023.
[14] International Energy Agency, “Europe’s energy crisis: What factors
drove the record fall in natural gas demand in 2022?” IEA Commentary,
Mar. 2023.
[15] N. C. Figueiredo and P. P. da Silva, “The “merit-order effect” of
wind and solar power: V olatility and determinants,”Renewable and
Sustainable Energy Reviews, vol. 102, pp. 54–62, 2019.
[16] European Commission, “The just transition fund,” Policy overview,
2021.
