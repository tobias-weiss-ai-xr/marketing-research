---
title: Neural Network-Assisted Model Predictive Control for Implicit Balancing
url: https://arxiv.org/abs/2604.01805
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Seyed Soroush Karimi Madahi
- Kenneth Bruninx
- Bert Claessens
- Chris Develder
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.01805
pages: 8
chars: 36976
fetched_at: '2026-11-08T12:59:57+00:00'
kb_version: 1
---

# Neural Network-Assisted Model Predictive Control for Implicit Balancing

Neural Network-Assisted Model Predictive Control
for Implicit Balancing
Seyed Soroush Karimi Madahi ∗, Kenneth Bruninx ‡, Bert Claessens ∗†, Chris Develder ∗
∗ IDLab, Ghent University – imec, Ghent, Belgium
† Beebop.ai, Belgium
‡ Faculty of Technology, Policy & Management, Delft University of Technology, Delft, The Netherlands
Abstract—In Europe, balance responsible parties can deliber-
ately take out-of-balance positions to support transmission system
operators (TSOs) in maintaining grid stability and earn profit,
a practice called implicit balancing. Model predictive control
(MPC) is widely adopted as an effective approach for implicit
balancing. The balancing market model accuracy in MPC is
critical to decision quality. Previous studies modeled this market
using either (i) a convex market clearing approximation, ignoring
proactive manual actions by TSOs and the market sub-quarter-
hour dynamics, or (ii) machine learning methods, which cannot
be directly integrated into MPC. To address these shortcomings,
we propose a data-driven balancing market model integrated
into MPC using an input convex neural network to ensure
convexity while capturing uncertainties. To keep the core network
computationally efficient, we incorporate attention-based input
gating mechanisms to remove irrelevant data. Evaluating on
Belgian data shows that the proposed model both improves MPC
decisions and reduces computational time.
Index Terms—Balancing markets, battery, implicit Balancing,
input convex neural network, model predictive control.
I. INTRODUCTION
The integration of variable renewable energy sources in
the power system introduces uncertainty into grid operations,
making supply–demand balancing more challenging for trans-
mission system operators (TSOs). In Europe, TSOs maintain
grid balance by delegating part of the necessary corrective
balancing actions to balance responsible parties (BRPs), such
as energy companies. BRPs that fail to balance their portfolio
in each imbalance settlement period (ISP) are subject to
imbalance prices. Based on the European Electricity Balancing
Guidelines (EBGL), all TSOs should apply a single imbalance
pricing methodology, in which both BRP shortages and BRP
surpluses are exposed to the same price [1]. Depending on the
system imbalance and the position of the BRP, this results in
a net loss or benefit for the BRP. This also implies that BRPs
can consciously take out-of-balance positions to support grid
stability and gain financial profit, a practice known as implicit
or passive balancing. However, implicit balancing is a complex
problem due to the high uncertainty and nonlinear nature of the
balancing energy market, as well as the partial observability
of other BRPs and the TSO’s manual actions.
Submitted to the 24th Power Systems Computation Conference (PSCC 2026).
Implicit balancing, leveraging flexible assets such as battery
energy storage systems (BESS), has been addressed in the
literature through both model-based optimization and model-
free reinforcement learning (RL) methods. Studies focusing
on optimization methods, primarily model predictive control
(MPC), formulate the implicit balancing problem as a bi-level
optimization problem: the upper level determines the BRP’s
profit and the lower level models balancing energy market
clearing [2]–[4]. On the other hand, RL-based approaches
model the implicit balancing problem as a sequential decision-
making problem using a Markov decision process: the RL
agent is trained through interaction with the environment (in
this case, the imbalance market) to take actions at each time
step based on the current state, which usually includes real-
time and historical information about system imbalance, the
grid, and the BRP [5]–[7]. In our previous work [8], we
combined MPC and RL for implicit balancing using a BESS.
By leveraging the complementary nature of MPC and RL, the
MPC-guided RL method outperformed standalone MPC and
RL strategies in terms of profit.
The quality of actions in both optimization-based and
MPC-guided RL methods is strongly influenced by the ac-
curacy of the electricity market model. In [2], [3], [8], the
balancing market used for MPC was modeled based on
quarter-hourly balancing energy market clearing. However,
this model overlooks the sub-quarter-hourly dynamics of the
imbalance settlement mechanism, which play a crucial role in
determining imbalance prices [4]. Moreover, this model does
not account for uncertainties in frequency restoration reserve
(FRR) activations as a result of partially known FRR provider
availability, grid congestion, and out-of-merit-order manual
frequency restoration reserve (mFRR) activations by TSOs,
which also influence imbalance prices [9].
Altenatively, imbalance prices can be directly forecasted
using machine learning and deep learning [10]–[13], which
have been shown to yield more accurate forecasts than funda-
mental, model-based approaches [10]. Smets et al. [10] used a
value-oriented forecasting method to predict imbalance prices
by taking into account the downstream decision problem for
which the forecaster is trained. The predicted imbalance prices
are directly used by the MPC for decision-making. Yet, this
framework ignores the effect of battery actions on imbalance
prices, which is particularly significant for large batteries and
assets [14]. To address this issue, the price prediction model
24th Power Systems Computation Conference
PSCC 2026
Limassol, Cyprus — June 8-12, 2026
arXiv:2604.01805v1  [eess.SY]  2 Apr 2026

must be integrated into the optimization problem. For this
purpose, Dol´anyi et al. [15] introduced the concept of a math-
ematical program with a neural network (NN) constraint, in
which the lower-level problem (market model) is replaced by
a surrogate neural network. State-of-the-art machine learning
models to predict real-time and imbalance prices [11]–[13]
are, however, not convex on their inputs, resulting in mixed-
integer nonlinear programs (MINLP). These are challenging
to solve, which limits their applicability in near-real-time
decision making.
To address these shortcomings, we propose a price-maker
NN-assisted MPC framework for implicit balancing. This is
achieved by modeling the balancing energy market using an in-
put convex neural network (ICNN). This allows leveraging the
powerful capability of NNs to learn nonlinear mappings (such
as the influence of sub-quarter-hourly dynamics on imbalance
prices), to model market uncertainties (such as proactive
mFRR activations), and to capture partially known parameters
(such as other market players’ behavior), while the ICNN ar-
chitecture ensures convexity of its output(s) with respect to its
input(s). By incorporating the proposed ICNN into the implicit
balancing problem, we formulate the optimization problem as
a mixed-integer quadratic program (MIQP), in which finding
the global optimal solution is guaranteed. We furthermore
equip the proposed ICNN with attention and embedding layers
to further boost its performance. The attention and embedding
layers are trained end-to-end with the ICNN to filter FRR bids
based on current and historical system imbalances, providing
the most relevant bids as input to the ICNN. These trainable
preprocessing steps enable the ICNN core network to remain
compact, further reducing the computational complexity of
solving the optimization problem. We evaluate the perfor-
mance of our proposed framework by controlling a battery in
the Belgian imbalance settlement mechanism using data from
2023 (Sections V and VI).
In summary, our main contributions threefold:
•We propose an input-convex, data-driven balancing mar-
ket model to capture uncertainties, nonlinearities, and
partially observable effects, thereby improving on the
quarter-hourly balancing market clearing model used
in [2], [3], [8] (Section III);
•We integrate the proposed ICNN with the implicit bal-
ancing problem and formulate the resulting price-maker
optimization problem as an MIQP to account for the in-
fluence of battery actions on imbalance prices, advancing
beyond the state-of-the-art data-driven imbalance price
prediction models introduced in [10]–[13] (Sections II
and IV);
•We incorporate trainable preprocessing steps into the pro-
posed ICNN to improve its performance and keep the core
network lightweight, which reduces the computational
burden of solving the optimization problem (Section III).
II. IMPLICITBALANCINGPROBLEMFORMULATION
We aim to control batteries in the imbalance settlement
mechanism to minimize their imbalance cost by taking strate-
gic out-of-balance positions. This implies buying energy when
the imbalance prices are low and selling it when they are high.
For this purpose, we cast the implicit balancing problem as an
optimization problem given by (1)-(7).
min
pcha t ,pdis t
X
t∈LH
λt

pcha t −p dis t  ∆t(1)
Subject to:
SOCt+1 =SOC t +

pcha t ηcha − pdis t ηdis  ∆t Eb ∀t∈LH (2)
SOC ≤SOC t ≤ SOC∀t∈LH (3)
0≤p cha t ≤z BESS t Pb ∀t∈LH (4)
0≤p dis t ≤  1−z BESS t  Pb ∀t∈LH (5)
zBESS t ∈ {0,1} ∀t∈LH (6)
λt =f market(|pcha t −p dis t |,sgn(p cha t −p dis t ), ⃗ξt)∀t∈LH (7)
The objective function (1) minimizes the imbalance cost over
the defined look-ahead horizon (LH). In (1),p cha t andp dis t are
optimization variables that indicate the charge and discharge
power of the battery at timet. Equation (2) defines the battery
state of charge (SoC), whereη cha andη dis denote charging and
discharging efficiencies,E b represents the maximum capacity
of the battery, and SOCt the battery SoC at timet. Equation (3)
ensures that the battery SoC remains within its limits, where
SOC and SOC are the minimum and maximum SoC of the
battery. Equations (4)-(6) determine battery’s power limits and
prevent simultaneous charging and discharging.P b denotes
the maximum power of the battery. Equation (7) is used
to calculate the imbalance price at timet(λ t), considering
the effect of the battery action. In (7),f market indicates the
balancing market model,|p cha t −p dis t |andsgn(p cha t −p dis t )are
absolute and sign of the battery action, and ⃗ξt represents inputs
that affect price formation (such as the system imbalance) that
are independent of the decisions of the BESS operator.
The problem formulation above is not convex as a result of
the objective function and (7). Using proposition 1 below, we
reformulate the objective function in a convex form.
Proposition 1.The functionxf(x, ⃗ y)is convex inxfor
x≥0, provided thatfis convex and monotonically increasing
with respect tox.
Proof.See Appendix A.
Using Proposition 1, we rewrite the optimization problem
as follows:
min
pcha t ,pdis t
X
t∈LH

pcha t λt +p dis t (−λt|{z}
λ′ t
)

 ∆t(8)
Subject to:
(2)-(6)
λt =f market(pcha t ,1, ⃗ξt)∀t∈LH (9)
λ′ t =f market(pdis t ,−1, ⃗ξt)∀t∈LH (10)
24th Power Systems Computation Conference
PSCC 2026
Limassol, Cyprus — June 8-12, 2026

Since charging and discharging do not occur simultaneously,
the market model can be decomposed into two independent
functions to determine the impact of charging and discharg-
ing on the imbalance price. In this paper, we employ a
single balancing market model (f market) for both charging
and discharging, with a flag indicating the battery mode
(where 1 represents charging). The resulting market prices will
subsequently be used to determine charging and discharging
actions. By formulating the market model as a convex and
monotonically increasing function (see § III-B for details),
the objective function of the reformulated implicit balancing
problem becomes convex. Consequently, the global optimum
of the formulated MIQP is guaranteed to be found using the
branch-and-bound algorithm [16].
III. BALANCINGENERGYMARKETMODEL
A. European Imbalance Settlement Mechanism
TSOs are primarily responsible for ensuring that the grid
frequency remains within the desired range. To achieve this,
they correct system imbalances in real-time through the ac-
tivation of FRR volumes. At the end of each ISP (usually
15 min), BRPs are settled at imbalance prices that reflect
the cost of these activated FRR volumes [17]. As stated
in the EBGL, the imbalance settlement mechanism aims to
encourage BRPs to restore grid balance by adopting a single
pricing methodology [1]. This pricing mechanism exposes all
BRPs (whether in shortage or in surplus) to an identical price.
In this way, the imbalance settlement incentivizes BRPs that
help reduce the system imbalance while imposing penalties
on those that exacerbate it. The EBGL permits BRPs to delib-
erately deviate from their nominations to gain an imbalance
profit. Implicit balancing benefits BRPs and is also promoted
by some TSOs, since it helps reduce system imbalance and
lower FRR activation costs. We chose the Belgian imbalance
settlement mechanism as a case study in this paper because
it is largely consistent with the target model specified in the
EBGL. The Belgian imbalance price calculation is explained
in detail in [4], [18].
B. Proposed Data-driven Balancing Market Model
An overview of the proposed framework is presented in
Fig. 1. The proposed model estimates the imbalance price
for each quarter hour based on the forecasted system imbal-
ance (SI) for that period, the battery action (determined by
solving the optimization problem), and other inputs shown
in Fig. 1. Historical system imbalances (in this paper, the
last two quarter hours) are provided as inputs to the model
to better capture market dynamics and the strategies of other
market participants. The proposed model consists of trainable
preprocessing layers (i.e., embedding and attention layers)
and an ICNN. The main purpose of the preprocessing layers
is to encode key information and filter out irrelevant data.
Following Van Gompel et al. [19], the time feature (quarter
hour) is fed into an embedding layer to effectively extract
useful information.
Fig. 1: The proposed implicit balancing framework.
Fig. 2: The attention layer architecture used in the proposed
market model.
Figure 2 illustrates the attention block used in the proposed
model. In this attention layer, the query vector includes SI-
related data (forecasted and historical system imbalances),
while the key vectors contain bid-related data (price differ-
ences between each bid and its neighboring bids, the signed
and absolute distance between bid cumulative volumes and
the forecasted SI, and the cumulative bid volumes). The
underlying idea is that the network learns the importance
of input bids based on the system imbalance inputs. The
importance weights for all bids are computed by calculating
the dot product of the query vector with all key vectors,
followed by the softmax function. Finally, thekbids (64 bids
for automatic frequency restoration reserve (aFRR) and 8 bids
for mFRR) with the highest weights are selected to be fed
into the ICNN. To make the top-k operation differentiable
and enable backpropagation through it, we apply the straight-
through estimator trick [20].
The ICNN, shown in Fig. 3, is the core component of the
proposed model. An ICNN is a neural network in which its
weights are constrained such that the network is convex in
(a subset of) its inputs [21]. We use a partial ICNN, as we
require the model to be convex only with respect to certain
inputs (i.e., the battery’s charge and discharge actions). The
ICNN defined in Fig. 3 maps the inputs (x var andx static) to
24th Power Systems Computation Conference
PSCC 2026
Limassol, Cyprus — June 8-12, 2026

Fig. 3: The ICNN architecture.
the outputs (λor the imbalance price) as follows:
zi =σ i(W z i−1zi−1 +W x i xvar +W uz i−1ui−1 +b z i )(11)
ui = ˜σi(W u i ui−1 +b u i )(12)
u0 =x static, zk+1 =λ, W z 0 =0(13)
wherez i andu i are hidden units,Wandbare trainable
weights and biases,σ i and˜σi are activation functions (ReLU
in this paper, except forσ k+1 which is linear),x var denotes
the inputs with respect to which the network is convex, and
xstatic represents the remaining inputs. The following propo-
sitions ensure that the defined ICNN is convex and increases
monotonically with respect tox var.
Proposition 2.The networkf(x var, xstatic)is convex inx var
if all elements inW z i (∀i≤k) are nonnegative andσ i (∀i≤
k+ 1) is convex and nondecreasing.
Proof.As shown in [21].
Proposition 3.The networkf(x var, xstatic)is monotonically
increasing with respect tox var if all elements inW x i (∀i≤
k+ 1) are nonnegative andσ i (∀i≤k+ 1) is nondecreasing.
Proof.See Appendix B.
The assumption that the output of the proposed market
model (the imbalance price) monotonically increases with
respect to battery actions aligns with what occurs in prac-
tice: charging the battery causes a negative imbalance, which
increases the upward FRR volume activation (or reduces the
downward FRR volume activation), resulting in an increase
in the imbalance price. On the other hand, as the discharge
power increases, the imbalance price decreases accordingly.
In (10), since our proposed model outputs the negative of the
price, it remains consistent with this monotonically increasing
relationship between discharge power and output of the market
model (i.e., the negative of the imbalance price).
IV. SOLVETHEIMPLICITBALANCINGPROBLEM
We employ MPC, a receding horizon method, to solve the
implicit balancing problem formulated in (2)-(6) and (8)-(10).
The proposed ICNN can be formulated as a mixed-integer
linear program (MILP) by modeling ReLU activation functions
using binary variables [22]. The other parts of the proposed
market model (the purple and blue blocks in Fig. 1) do not
need to be converted into an MILP, as their parameters and
inputs are constant with respect to the decision variables (p cha t
andp dis t ).
We use Gurobi to obtain a solution to the resulting MIQP.
The overall problem is nonconvex due to binary variables
(zBESS t ). However, since the number of binary variables is
relatively small (equal to the look-ahead horizon length and
the binaries obtained from the reformulation of the ICNN)
divide-and-conquer methods such as the branch-and-bound
algorithm can guarantee convergence to the optimal solution,
given that each resulting subproblem is convex [16]. Since
the Belgian ISP is set to 15 minutes, the time resolution of
decision-making is also 15 minutes. At the beginning of each
quarter hour, the optimization problem is solved over the look-
ahead horizon, and the resulting battery action for that quarter
hour is applied. At each time step, the market model output
corresponding to the opposite direction of the taken battery
action does not affect the objective function value in (8), as
the decision variable associated with the opposite direction is
zero (to prevent simultaneous charging and discharging).
V. RESULTS ANDDISCUSSION
A. Simulation Setup
We assess the performance of the proposed NN-assisted
MPC in terms of price prediction and imbalance profit using
the 2023 Belgian balancing dataset. We study both the price-
taker and price-maker scenarios: the former to quantify the
gap between the obtained and optimal imbalance profits,
and the latter to investigate the impacts of battery actions
on price prediction error and imbalance profit. The dataset
is divided as follows: the first 10 months are used for
training, November for validation, and December for testing.
Four different battery configurations are studied to analyze
the effect of battery size: 1 MW/ 2 MWh, 10 MW/ 20 MWh,
50 MW/ 100 MWh, and 100 MW/ 200 MWh, all with a 90%
round-trip efficiency for both charging and discharging. The
proposed ICNN consists of two hidden layers with 64 and
32 neurons for the network usingx var as inputs, and two
hidden layers with 1024 and 512 neurons for the network
usingx static as inputs. The quarter-hour feature shown in Fig. 1
is embedded into a vector of size 4 using a fully connected
network with two hidden layers of 256 and 128 neurons. The
proposed data-driven balancing market model is trained end-
to-end using the Adam optimizer with an L1 loss function and
a learning rate of 2 × 10 −4 for 40 epochs. The proposed model
is trained with 10 random seeds, and the reported results are
averaged over all seeds to ensure reliability. All experiments
24th Power Systems Computation Conference
PSCC 2026
Limassol, Cyprus — June 8-12, 2026

TABLE I: Imbalance profit for 1 MW/ 2 MWh battery on December 2023.
Horizon SI Forecast Method
Profit ( C/ MW/ QH)
All|SI| ≥20 MW|SI|<20 MW
1 QH
PF
Optimal 9.59 11.23 8.06
Clearing Approx. 8.01 9.89 6.27
Proposed 8.4±0.08 * 10.43±0.15 6.49±0.14
Noise Clearing Approx. 5.58 10.51 1.02
Proposed 7.68±0.19 10.56±0.15 4.99±0.45
4 QH
PF
Optimal 10.84 14.02 7.9
Clearing Approx. 9.7 12.58 7.03
Proposed 9.59±0.14 13.31±0.35 6.14±0.13
Noise Clearing Approx. 6.55 12.87 0.64
Proposed 8.87±0.23 13.46±0.4 4.60±0.44
* Standard deviation over the 10 random seeds
were executed on a 6-core Intel Core i5 (2.90 GHz) machine
with 32 GB of RAM.
For both upward and downward directions, aFRR and
mFRR bids are separately aggregated to form the available
regulation capacity (ARC) merit order for each quarter hour.
The resulting ARC merit orders for aFRR and mFRR are
discretized in 2 MW and 100 MW steps. In most cases, we
assume perfect foresight (PF) on the system imbalance to
isolate the impact of the balancing market models on MPC
decision quality. To study the robustness of the proposed
framework to imperfect system imbalance forecasts, we also
show results when introducing zero-mean Gaussian noise with
a standard deviation of 10 MW, increasing exponentially by
20% across the optimization look-ahead horizon.
The proposed model is benchmarked against the quarter-
hour-level, optimization-based balancing market clearing
model (hereafter referred to as the clearing approximation
model in this paper), as detailed in [2], [8]. The clearing
approximation model is widely used due to its simplicity
and convexity. It estimates the imbalance price using the
average system imbalance over the quarter hour, neglecting
sub-quarter-hourly dynamics and changes in system imbalance
within that quarter hour.
The final imbalance profit of the battery, resulting from the
MPC actions of both the proposed and clearing approximation
models, is calculated by implementing these actions on a real-
minute-based balancing market simulator [18]. 1
B. Price-taker Battery
The proposed MPC framework is applied to a
1 MW/ 2 MWh battery. Since the battery is small-scale
in this case, it cannot significantly influence imbalance prices
and is therefore a price-taker. Consequently, the optimal
1Although the Belgian TSO calculates imbalance prices through a 4-
second optimization cycle for aFRR activations, the available balancing data
(system imbalance, aFRR/mFRR activations, etc.) are published at one-minute
intervals. Thus, our balancing market simulator uses a one-minute resolution
as the finest available granularity.
Fig. 4: Price prediction error and the probability of idle action
for 1 MW/ 2 MWh battery.
imbalance profit can be obtained for this case. Table I
summarizes the imbalance profits for different methods
and look-ahead horizons. The results show that when both
the clearing approximation and the proposed models have
access to the exact SI values over their horizon, their MPC
performance is close to optimal (i.e., approximately 11%
24th Power Systems Computation Conference
PSCC 2026
Limassol, Cyprus — June 8-12, 2026

Fig. 5: Price prediction error and the probability of idle action
for 50 MW/ 100 MWh battery.
lower than the optimal profit for a 4-quarter-hour (QH)
horizon). As Fig. 4 demonstrates, the proposed model
improves the average price prediction RMSE for quarter
hours with large SI (|SI| ≥20MW) by 23% compared to the
clearing approximation model, whereas for quarter hours with
small SI (|SI|<20MW), the benchmark model performs
better in terms of RMSE. This aligns with the results shown
in Table I, where the proposed method outperforms the
clearing approximation model for large SI, while the latter
makes higher profit for quarter hours with small SI.
Adding noise to SI values significantly reduces the perfor-
mance of the clearing approximation model, particularly for
small SI values. This occurs because adding noise to SI values
in this range can reverse the direction of the SI. Consequently,
the noisy values mislead the benchmark model about the
correct direction of the SI, leading to a large prediction error.
On the other hand, the proposed method is robust to noise,
with its performance reduced by about 8% compared to the
perfect foresight case. In this case, the proposed method
outperforms the clearing approximation model by 35.4% in
terms of imbalance revenue when the look-ahead horizon is
four quarter-hours.
C. Price-maker Battery
For large-scale batteries, whose impact on the grid is
greater, sub-quarter-hour variations in SI become increasingly
(a)
(b)
Fig. 6: The QH profit spread of the 50 MW battery for quarter
hours with small SI (a) PF (b) noise.
important in determining the final imbalance price. This leads
to an increase of 11% in the price prediction error of the
clearing approximation model for the 50 MW battery com-
pared to the price-taker case, as illustrated in Fig. 5. For
quarter hours with large SI values, the prediction error of the
clearing approximation model increases by 15.5% compared
to the price-taker case, whereas for the proposed method, this
deterioration is limited to 6.8%. In contrast, the prediction
error of the proposed model increases substantially for quarter
hours with small SI. However, the proposed model yields a
higher imbalance profit for these quarter hours compared to the
benchmark model, as indicated in Table II. The reason is that
the proposed framework executes noticeably more idle actions
during these quarter hours. Figure 6 shows that the quarter
hour profits for quarter hours with small SI in the proposed
model are mostly centered close to zero, in spite of their high
prediction error. The positive tails of the contours for both
models are almost the same, which indicates that the quarter
24th Power Systems Computation Conference
PSCC 2026
Limassol, Cyprus — June 8-12, 2026

TABLE II: Imbalance profit for large batteries with 4 QH look-ahead horizon on December 2023.
Battery SI Forecast Method
Profit ( C/ MW/ QH)
All|SI| ≥20 MW|SI|<20 MW
10 MW/ 20 MWh
PF
Clearing Approx. 6.41 11.04 2.59
Proposed 6.93±0.22 * 11.73±0.37 2.98±0.27
Noise Clearing Approx. 3.54 10.51−2.36
Proposed 6.83±0.18 11.72±0.36 2.79±0.22
50 MW/ 100 MWh
PF
Clearing Approx. 2.76 6.19 0.49
Proposed 3.6±0.13 6.86±0.23 1.28±0.14
Noise Clearing Approx. 1.32 5.30−1.67
Proposed 3.59±0.13 6.88±0.24 1.26±0.13
100 MW/ 200 MWh
PF
Clearing Approx. 1.36 3.79 0.04
Proposed 2.21±0.04 4.15±0.12 0.42±0.07
Noise Clearing Approx. 0.55 3.30−1.19
Proposed 2.21±0.04 4.15±0.12 0.43±0.1
* Standard deviation over the 10 random seeds
hours in which the proposed method takes an idle action are
those in which the benchmark model takes an incorrect non-
idle action, leading to negative profits. For quarter hours with
large SI, the proposed method achieves superior imbalance
profits than the benchmark, owing to its lower prediction error.
In general, the proposed method improves the imbalance profit
by 8.1%, 30.4%, and 62.5% for 10 MW, 50 MW, and 100 MW
batteries, respectively, compared to the benchmark.
The results in Table II confirm that, similar to the price-
taker case, our proposed framework is robust to noise. Also, as
the battery size increases, the proposed method becomes less
sensitive to noise because it takes more idle actions during
quarter hours with small SI values: for these quarter hours,
the proportion of idle actions increases from 0.23 in the price-
taker case to 0.55 for the 50 MW battery.
Finally, Replacing the clearing approximation model with
the proposed model can speed up the optimization process,
regardless of battery size. The computational time per quarter
hour is reduced on average from 60.59 ms in the benchmark
model to 30.3 ms in the proposed model.
VI. CONCLUSION
We propose an NN-assisted MPC framework for controlling
batteries in the imbalance settlement mechanism. We model
the balancing energy market using a data-driven ICNN-based
network to efficiently capture uncertainties and partial ob-
servability, ensure the convexity of the objective function of
the resulting optimization problem, and achieve low compu-
tational time. We compare our proposed framework against
the commonly used quarter-hour-level market clearing model
approximation, in a case study using 2023 Belgian balancing
data. Our proposed framework using the ICNN outperforms
an MPC that uses the baseline market clearing model to
make decisions, achieving 8.1% to 62.5% higher imbalance
profits across different battery sizes. Although the benchmark
model has smaller price prediction errors for quarter hours
with small system imbalance values (below 20 MW), our
proposed framework still achieves higher overall imbalance
profits for these quarter hours, as it more often resorts to the
idle action — particularly in the price-maker case, when a large
battery system is used. For both price-taker and price-maker
scenarios, the imbalance profit of our proposed framework
is less sensitive to noise added to the system imbalance
forecasts. In this case, the proposed framework achieves 35.4%
to 301.8% higher imbalance revenue for different battery sizes
relative to the clearing approximation model. Overall, our
proposed data-driven market model helps the MPC make better
decisions while reducing computational time by 50%.
The current work can be extended by enriching the inputs to
the proposed model with longer historical data and additional
grid-related features, such as renewable forecast errors. A deep
neural network can be used to extract useful information from
these inputs and feed it to the ICNN, which could poten-
tially improve model accuracy. Moreover, since the ICNN is
lightweight and capable of modeling nonlinearities, our pro-
posed framework enables formulating the implicit balancing
problem on a minute basis, allowing it to take advantage of
minute-level balancing data and the most recent information
for decision-making. Future work includes exploring such
minute-based battery control actions. In this work, we use a
simple linear battery model. Another direction for future work
is to replace this basic battery model with a one that captures
the battery behavior more accurately, but still retains convexity.
ACKNOWLEDGMENTS
This research was partly funded by the Flemish Government
under the “Onderzoeksprogramma Artifici¨ele Intelligentie (AI)
Vlaanderen” programme as well as a travel grant from the
Research Foundation – Flanders (FWO).
24th Power Systems Computation Conference
PSCC 2026
Limassol, Cyprus — June 8-12, 2026

APPENDIXA
Proof.Letα∈(0,1)andx 1, x2 ≥0. Asfis a monotonically
increasing function, we can write:
α(1−α)(x 2 −x 1)(f(x 2, ⃗ y)−f(x1, ⃗ y))≥0(14)
By expanding (14), we obtain the following inequality.
(αx1 + (1−α)x 2)

(αf(x 1, ⃗ y) + (1−α)f(x2, ⃗ y)

≤
αx1f(x 1, ⃗ y) + (1−α)x2f(x 2, ⃗ y)(15)
On the other hand, sincefis convex, the definition of
convexity gives the following inequality.
f(αx 1 + (1−α)x 2, ⃗ y)≤αf(x1, ⃗ y) + (1−α)f(x2, ⃗ y)(16)
Multiplying (16) by(αx 1 + (1−α)x 2)(which is nonneg-
ative) yields the following inequality.
(αx1 + (1−α)x 2)f(αx 1 + (1−α)x 2, ⃗ y)≤
(αx1 + (1−α)x 2)

(αf(x 1, ⃗ y) + (1−α)f(x2, ⃗ y)

(17)
Combining (15) and (17) results in (18).
(αx1 + (1−α)x 2)f(αx 1 + (1−α)x 2, ⃗ y)≤
αx1f(x 1, ⃗ y) + (1−α)x2f(x 2, ⃗ y)(18)
In (18), the convexity ofxf(x, ⃗ y)is demonstrated.
APPENDIXB
Proof.Considerx var ≥x ′ var. Fori= 1in (11), the following
inequality can be written.
W x 1 xvar +W uz 0 xstatic +b z 1 ≥W x 1 x′ var +W uz 0 xstatic +b z 1 (19)
Sinceσ 1 is nondecreasing, applying it to both sides of the
inequality in (19) yieldsz 1 ≥z ′ 1. Similarly, fori≥2in (11),
we can obtain the following inequality.
σi(W z i−1zi−1 +W x i xvar +W uz i−1ui−1 +b z i )| {z }
zi
≥
σi(W z i−1zi−1 +W x i x′ var +W uz i−1ui−1 +b z i )| {z }
z′ i
(20)
Using (20),z k+1 =f(x var, xstatic)≥z ′ k+1 =f(x ′ var, xstatic),
which demonstrates the monotonicity off.
REFERENCES
[1] European Network of Transmission System Operators for Electricity,
“Explanatory document to all tsos’ proposal to further specify and
harmonise imbalance settlement in accordance with article 52(2) of com-
mission regulation (eu) 2017/2195 of 23 november 2017, establishing a
guideline on electricity balancing,” 2018.
[2] R. Smets, K. Bruninx, J. Bottieau, J.-F. Toubeau, and E. Delarue,
“Strategic implicit balancing with energy storage systems via stochastic
model predictive control,”IEEE Transactions on Energy Markets, Policy
and Regulation, vol. 1, no. 4, pp. 373–385, 2023.
[3] E. Wessel, R. Smets, and E. Delarue, “Risk-aware participation in day-
ahead and real-time balancing markets for energy storage systems,”
Electric Power Systems Research, vol. 235, p. 110741, 2024.
[4] S. S. K. Madahi, K. Bruninx, B. Claessens, and C. Develder, “Gaming
strategies in european imbalance settlement mechanisms,” in2025 IEEE
PES Innovative Smart Grid Technologies Conference Europe (ISGT
Europe), 2025, pp. 1–5.
[5] S. S. K. Madahi, B. Claessens, and C. Develder, “Distributional re-
inforcement learning-based energy arbitrage strategies in imbalance
settlement mechanism,”Journal of Energy Storage, vol. 104, p. 114377,
2024.
[6] S. S. K. Madahi, F. Pavirani, B. Claessens, and C. Develder, “Risk-
sensitive reinforcement learning-based strategies for dutch implicit bal-
ancing,” in2025 21st International Conference on the European Energy
Market (EEM). IEEE, 2025, pp. 1–6.
[7] S. Ally, T. Verstraeten, A. Now ´e, and J. Helsen, “Day-ahead trading
and power control for hybrid wind-hydrogen plants with multi-agent
reinforcement learning,”Applied Energy, vol. 401, p. 126588, 2025.
[8] S. S. K. Madahi, K. Bruninx, B. Claessens, and C. Develder, “Model
predictive control-guided reinforcement learning for implicit balancing,”
arXiv preprint arXiv:2510.04868, 2025.
[9] J. Allard, A. Arrigo, J. Bottieau, G. Bertrand, Z. De Gr `eve, and F. Vall´ee,
“A forecast-driven stochastic optimization method for proactive activa-
tion of manual reserves,”Electric Power Systems Research, vol. 235, p.
110804, 2024.
[10] R. Smets, J.-F. Toubeau, M. Dolanyi, K. Bruninx, and E. Delarue,
“Value-oriented price forecasting for arbitrage strategies of energy
storage systems through loss function tuning,”Energy, p. 137112, 2025.
[11] J. Bottieau, G. Audemard, S. Bellart, J. Lagniez, P. Marquis,
N. Szczepanski, and J.-F. Toubeau, “Logic-based explanations of im-
balance price forecasts using boosted trees,”Electric Power Systems
Research, vol. 235, p. 110699, 2024.
[12] A. Lucas, K. Pegios, E. Kotsakis, and D. Clarke, “Price forecasting
for the balancing energy market using machine-learning regression,”
Energies, vol. 13, no. 20, p. 5420, 2020.
[13] K. Plakas, N. Andriopoulos, D. Papadaskalopoulos, A. Birbas,
E. Housos, and I. Moraitis, “Prediction of imbalance prices through
gradient boosting algorithms: An application to the greek balancing
market,”IEEE Access, 2025.
[14] M. Bruninx, T. Verstraeten, J. Kazempour, and J. Helsen, “Day-ahead
bidding strategies for wind farm operators under a one-price balancing
scheme,” inProceedings of the 16th ACM International Conference on
Future and Sustainable Energy Systems, 2025, pp. 719–726.
[15] M. Dol ´anyi, K. Bruninx, J.-F. Toubeau, and E. Delarue, “Capturing
electricity market dynamics in strategic market participation using
neural network constrained optimization,”IEEE Transactions on Power
Systems, vol. 39, no. 1, pp. 533–545, 2023.
[16] R. Fletcher and S. Leyffer, “Numerical experience with lower bounds for
miqp branch-and-bound,”SIAM Journal on Optimization, vol. 8, no. 2,
pp. 604–616, 1998.
[17] F. Pavirani, J. Van Gompel, S. S. K. Madahi, B. Claessens, and
C. Develder, “Predicting and publishing accurate imbalance prices using
monte carlo tree search,”Applied Energy, vol. 392, p. 125944, 2025.
[18] Elia, “Terms and conditions for balance responsible parties,” 2024.
[19] J. Van Gompel, B. Claessens, and C. Develder, “Probabilistic forecasting
of power system imbalance using neural network-based ensembles,”
Applied Energy, vol. 401, p. 126714, 2025.
[20] Y . Bengio, N. L ´eonard, and A. Courville, “Estimating or propagating
gradients through stochastic neurons for conditional computation,”arXiv
preprint arXiv:1308.3432, 2013.
[21] B. Amos, L. Xu, and J. Z. Kolter, “Input convex neural networks,” in
International conference on machine learning. PMLR, 2017, pp. 146–
155.
[22] M. Fischetti and J. Jo, “Deep neural networks and mixed integer linear
optimization,”Constraints, vol. 23, no. 3, pp. 296–309, 2018.
24th Power Systems Computation Conference
PSCC 2026
Limassol, Cyprus — June 8-12, 2026
