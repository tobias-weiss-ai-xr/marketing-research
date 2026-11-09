---
title: 'WARP: A Benchmark for Primal-Dual Warm-Starting of Interior-Point Solvers'
url: https://arxiv.org/abs/2605.05728
category: ai-marketing
subcategory: measurement
date: 2026-05
venue: ''
authors:
- Dhruv Suri
- Helgi Hilmarsson
- Shourya Bose
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.05728
pages: 29
chars: 83819
fetched_at: '2026-11-08T13:29:08+00:00'
kb_version: 1
---

# WARP: A Benchmark for Primal-Dual Warm-Starting of Interior-Point Solvers

W ARP: A Benchmark for Primal-Dual Warm-Starting
of Interior-Point Solvers
Dhruv Suri∗, Helgi Hilmarsson ∗, and Shourya Bose ∗
Pravah
{dhruv.suri, helgi.hilmarsson, shourya.bose}@pravah.com
Abstract
Solving AC Optimal Power Flow (AC-OPF) is of central importance in electricity
market operations, where interior-point methods (IPMs) such as IPOPT are the
standard solvers. A growing body of work uses machine learning to predict
primal warm-start iterates, reporting iteration reductions of 30–46%. We show that
these reported gains rest on an inappropriate evaluation baseline: prior methods
benchmark against the flat start Vm = 1, Va = 0 , whereas the solver’s actual
default—the variable-bound midpoint (l+u)/2 —is near-optimal for log-barrier
centrality. Against this corrected baseline, no primal-only warm-start method
reduces solver iterations. We trace the failure to a geometric property of interior-
point methods: primal prediction accuracy is anticorrelated with convergence
speed, and providing the ground-truth optimal solution x∗ without dual variables
causes the solver to diverge. Oracle experiments establish that the complete primal-
dual-barrier state (x∗, λ∗, z∗, µ∗) reduces IPOPT iterations from 23 to 3—an 85%
reduction that is structurally inaccessible to primal-only methods. To enable
rigorous evaluation of warm-start methods on this task, we release a benchmark
suite comprising dual-labeled AC-OPF datasets with IPOPT-extracted solutions, a
corrected evaluation protocol, and W ARP—a topology-conditioned encode-process-
decode interaction network that predicts the full interior-point state (ˆx,ˆλ,ˆz,ˆµ)on
the heterogeneous constraint graph. WARP achieves a 76% reduction in IPOPT
iterations while natively accommodating N-1 contingency topology variations
without retraining.
1 Introduction
Interior-point methods (IPMs) are the dominant solvers for large-scale constrained nonlinear pro-
grams [Nocedal and Wright, 1999, Nesterov and Nemirovskii, 1994]. In power systems, the primal-
dual IPM solver IPOPT [Wächter and Biegler, 2006] solves the AC Optimal Power Flow (AC-OPF)
problem—a non-convex NLP determining minimum-cost generator dispatch subject to Kirchhoff’s
laws and operational limits [Cain et al., 2012]—every 5–15 minutes at independent system oper-
ators worldwide. Its computational cost motivates a substantial body of work on learning-based
acceleration.
The prevailing approach trains a neural network to predict primal warm-start iterates ˆx, reporting
30–46% iteration reductions over the flat start [Baker, 2019, Diehl, 2019, Zhang and Zhang, 2022,
Cao et al., 2023, Xu et al., 2025]. These results suggest a straightforward principle: predict ˆxcloser to
x∗, and the solver converges faster. We demonstrate that this principle is structurally misaligned with
how interior-point methods converge, and that the reported gains rest on an inappropriate baseline.
Through systematic experimentation, we establish three findings:
∗Equal contribution.
40th Conference on Neural Information Processing Systems (NeurIPS 2026). Track on Evaluations and Datasets.
arXiv:2605.05728v1  [cs.LG]  7 May 2026

1. The evaluation baseline is inappropriate.Prior methods benchmark against the flat start
Vm = 1, Va = 0—not the solver’s default. IPOPT and MIPS initialise at the variable-bound
midpoint (l+u)/2 , which is near-optimal for log-barrier centrality. Against this corrected
baseline, no primal-only method reduces solver iterations.
2. Primal accuracy is anticorrelated with convergence.Among model variants, lower
prediction error yieldsmoresolver iterations. Providing the ground-truth x∗ without duals
causes divergence, confirming the theoretical result of Yildirim and Wright [2002]: the
optimal solution lies at constraint boundaries where the log-barrier is singular.
3. Dual information is necessary and sufficient.Oracle experiments show that the complete
state (x∗, λ∗, z∗, µ∗) reduces iterations by 85%—a ceiling structurally inaccessible to primal-
only methods. The entire iteration gap resides in the dual variables and barrier parameter.
Contributions.We make three contributions:
1. A corrected evaluation protocol and dual-labeled dataset.We release AC-OPF datasets
with IPOPT-extracted primal-dual-barrier solutions (x∗, λ∗, z∗, µ∗), hosted on OpenML
with Croissant metadata. The evaluation protocol benchmarks against the solver’s true
midpoint default rather than the weak flat start employed in prior work.2
2. A systematic diagnosis of the primal-only failure.Fifteen ablation experiments—spanning
prediction, blending, projection, retraction, and constraint screening—characterise the
geometric bottleneck and establish that dual information is both necessary and sufficient for
effective IPM warm-starting.
3. W ARP: a topology-aware primal-dual baseline.An encode-process-decode interaction
network that predicts the full IPM state, achieving 76% iteration reduction. Two architectural
principles are identified: per-step edge feature updates dominate (9× impact), and omitting
node residual connections improves dual prediction by5×.
2 Background
2.1 AC optimal power flow and interior-point methods
The AC-OPF problem determines minimum-cost generator dispatch on a power grid G= (B,E)
with buses B and branches E. Decision variables x= (V a, Vm, Pg, Qg) comprise bus voltage angles
and magnitudes and generator real and reactive power. The problem minimises a quadratic costP
g c2gP 2 g +c 1gPg +c 0g subject to AC power balance P inj i +jQ inj i =V i P k Y ∗ ikV ∗ k , voltage limits,
thermal line ratings, and generator bounds (full formulation in Appendix A). The power balance
constraints are non-convex, making AC-OPF a non-convex NLP.
The standard solver is the primal-dual interior-point method [Wächter and Biegler, 2006, Wang
et al., 2007]. The IPM replaces bound constraints with a logarithmic barrier parameterised by µ >0
and applies Newton’s method to the perturbed KKT system, maintaining the state (x, λ, zl, zu, µ)
where λ∈R m are equality multipliers and zl, zu ∈R n + are bound multipliers. The complementarity
conditions (xi−li)zl,i =µ define thecentral path—a curve of well-centred iterates from largeµ (deep
interior) to µ→0 (the boundary solution). The centrality measure ¯µ= ((x−l)⊤zl +(u−x) ⊤zu)/2n
quantifies how well-centred an iterate is.
Both IPOPT and MIPS initialise at the variable-bound midpoint:
x0 = (l+u)/2(1)
This maximises the minimum slack mini min(xi −l i, ui −x i) and yields large ¯µ. A critical
consequence formalised by Yildirim and Wright [2002] is that x∗ constitutes theleast favorableIPM
starting point: active-constraint slacks vanish, rendering the barrier singular. IPOPT supports warm-
starting via warm_start_init_point, accepting user-supplied (x0, λ0, zl,0, zu,0) with µinit. The
configuration warm_start_bound_push= 10 −20, mu_strategy=monotone, introduced by Gao
et al. [2024], is adopted throughout.
2We also document a silent initialisation defect in pandapower’s PIPS solver that overwrites user-supplied warm-starts; see
Appendix B.
2

2.2 Prior work
Primal warm-starting.Baker [2019] trained random forests, Diehl [2019] used GNNs, Zhang
and Zhang [2022] and Cao et al. [2023] used decision trees, and Xu et al. [2025] proposed ensemble
methods for predicting primal warm-starts. All report 30–46% reductionsrelative to the flat start
Vm = 1, Va = 0—not the solver’s actual midpoint default (1). Deihim et al. [2024] and Liu et al.
[2022] applied GNNs with physics regularisation. All predict only x; the solver reinitialises duals
independently.
Primal-dual methods.Gao et al. [2024] introduced IPM-LSTM, predicting (x, λ, z)via coordinate-
wise LSTMs trained on KKT trajectories. On QPs with up to 200 variables, it achieves 63.9% iteration
reduction. However, it operates on a fixed-dimension KKT vector—necessitating a separate model
per topology—and has not been applied to AC-OPF. Klamkin et al. [2024] proposed dual completion
layers; Sambharya et al. [2024] learned warm-starts for fixed-point splitting; Briden et al. [2024]
targeted SQP solvers.
End-to-end and constraint methods.Solution prediction methods [Fioretto et al., 2020, Donti
et al., 2021, Park and Van Hentenryck, 2023, Chen et al., 2024] replace the solver entirely. Active
constraint identification [Misra et al., 2022, Deka and Misra, 2019, Pineda and Morales, 2020] reduces
problem dimensionality. Both are complementary; we show constraint screening is counterproductive
for IPM (Section 3).
GNN architectures.W ARP belongs to the encode-process-decode (EPD) family [Battaglia et al.,
2016, 2018] applied to physical simulation [Pfaff et al., 2021, Lam et al., 2023] and AC-OPF [Piloto
et al., 2024, Rivera et al., 2025]. These predict only primal variables; we extend to the full primal-
dual-barrier state. Extended discussion in Appendix O.
3 The Primal-Only Warm-Start Failure
All experiments use pglib_opf_case118_ieee from OPFDataset [Falconer and Mones, 2023]
(67,500 training, 3,750 validation instances; 50 held-out test instances). We evaluate on PIPS [Wang
et al., 2007] (via pandapower) and IPOPT [Wächter and Biegler, 2006] (via cyipopt with exact
Hessian and sparse Jacobian).
3.1 Correcting the baseline and systematic ablation
Prior work evaluates against the flat start Vm = 1, Va = 0, which is not the solver’s default. The
midpoint (1) achieves 19.6 mean PIPS iterations and 22.6 mean IPOPT iterations. We additionally
identified a silent defect in pandapower’s PIPS implementation that overwrites user-supplied initial
points (Appendix B).
We train a heterogeneous GNN (DetGNN) predicting(V a, Vm, Pg, Qg)from load data and evaluate
eight strategies for injecting predictions into the solver. Table 1 reports the results.
Table 1: Primal-only warm-start strategies on case118 (PIPS, 50 test instances). Per-variable
normalisation is applied below the second divider. No method improves upon the solver’s midpoint
default.
Method Description Mean iters vs. Midpoint
Midpoint(l+u)/2Solver default 19.6 —
DetGNN (unnorm.) Primalˆx31.0+58%
W ARP diffusionK= 3Primalˆx31.0+58%
DetGNN (norm.) Primalˆx21.1+7.8%
Selective (voltage only) Partialˆx21.6+10%
Barrier retractionˆxretracted to interior 21.3+8.7%
Feasibility projectionˆxprojected to bounds 30.9+58%
Blend (α= 0.5)αˆx+ (1−α)x mid 25.1+28%
Constraint screening Reduced problem 44.1+125%
3

No primal-only method improves upon the midpoint.Per-variable normalisation—addressing
a 100× scale disparity between Pg and Vm—was the single most impactful change, improving
from 31.0 to 21.1 iterations, but still 7.8% worse than the midpoint. Feasibility projection and
barrier retraction were ineffective: projecting predictions onto the strict interior with ϵ= 0.02
yields 30.9 iterations; retraction to restore centrality achieves at best 21.3. Constraint screening
was catastrophically counterproductive ( 44.1 iterations, 2.3× the midpoint), consistent with the
observation that removing constraints widens the feasible set and flattens the barrier landscape. Full
per-strategy analysis in Appendix C.
3.2 The centrality-accuracy tradeoff
A blend sweep x0 =αˆxGNN + (1−α)x mid for α∈[0,1] reveals a counterintuitive result:any
intermediate blend is worse than either endpoint, reaching 28.8 iterations at α= 0.1 . The midpoint
(α= 0 , 19.6 iters) and pure GNN prediction (α= 1 , 21.6 iters) are both local minima. This indicates
that the interpolation path between a well-centred interior point and an accurate near-boundary point
traverses regions of high barrier curvature.
Among six diffusion model variants trained with varying physics loss weights, the variant with
the lowest denoising loss ( Lddpm = 0.265) yields the worst solver performance (39.5 iterations),
while the variant with the highest denoising loss (Lddpm = 0.576) yields the best (28.8 iterations).
Minimising prediction error in solution space is a misaligned objective for IPM warm-starting;
physical consistency matters more than pointwise accuracy.
The geometric bottleneck is voltage magnitude Vm. Its feasible range on case118 is only 0.12 p.u.
(Vm ∈[0.94,1.06] ), so any prediction displacing Vm from the midpoint (1.00) rapidly approaches
constraint boundaries, degrading the log-barrier irrespective of accuracy. Selective warm-start
experiments confirm that generator variables contribute negligibly to the iteration count (Appendix C).
3.3 Oracle experiments: the primal-dual-barrier state is necessary and sufficient
We construct a direct cyipopt interface with exact Hessian, sparse Jacobian, and the full warm-start
protocol. Table 2 reports oracle warm-start results.
Table 2: Oracle warm-start experiments (IPOPT, case118, 50 instances). The complete primal-dual-
barrier state yields85%reduction; primal variables alone contribute negatively.
Warm-start content Mean iters Median Reduction
Cold start (midpoint) 22.6 22 —
Oracle primalx ∗ only 23.7 23−4.9%
Ground-truthx ∗ (cold dual init)>50 — Diverges
Oracle(x ∗, λ∗)12.4 12+45%
Oracle(x ∗, λ∗, z∗)4.7 5+79%
Oracle(x ∗, λ∗, z∗, µ∗)3.3 3+85%
Three results merit emphasis. First, the oracle primal x∗ withoutduals yields 23.7 iterations—worse
than cold start (22.6), confirming that primal accuracy alone does not accelerate IPM convergence.
Second, providing x∗ with cold dual initialisation causes divergence (>50 iterations), experimentally
confirming Yildirim and Wright [2002]. Third, the complete state achieves 3.3 iterations (85%
reduction), establishing the ceiling.
The decomposition is instructive: bound multipliers z∗ contribute substantially more than equality
multipliers λ∗ alone (12.4→4.7 ); the barrier parameter µ∗ adds a further reduction to 3.3. The
primal variables contributenegativelyin isolation. The entire iteration gap between cold start and
oracle resides in the dual and barrier state.
4 The W ARP Benchmark Suite
The findings of Section 3 motivate a benchmark that evaluates warm-start methods on the correct
objective: predicting the full primal-dual-barrier state(x, λ, z, µ)and measuring the resulting iteration
count against the solver’s true midpoint default.
4

4.1 Dual-labeled datasets
Existing AC-OPF datasets [Falconer and Mones, 2023, Rivera et al., 2025] provide only primal
solution labels. We augment each instance with the complete IPOPT-converged state:
Di =

x∗ i , λ∗ i , z∗ l,i, z∗ u,i, µ∗ i , f(x∗ i )  (2)
For pglib_opf_case118_ieee: 5,000 training, 500 validation, and 50 test instances, with 100%
IPOPT convergence at ∼2.5 seconds per instance on a single CPU core. The dataset is hosted on
OpenML with Croissant metadata (Appendix P).
The dual variables present distinct challenges for regression. Equality multipliersλ∗ span [−14,4168]
with std 1,564. Bound multipliers z∗ l , z∗ u are 72–85% sparse (exactly zero for non-binding constraints)
with heavy-tailed non-zero entries. The barrier parameterµ∗ ≈3.25×10 −8 is approximately constant
across instances. Per-variable normalisation to N(0,1) was the critical enabler: without it, the MSE
loss is dominated by high-magnitude λ∗, and the model fails to learn the small-but-critical bound
multipliers. Normalisation reduced dual prediction error from 9.45×10 5 to 3×10 −4 (normalised
MSE).
4.2 Evaluation protocol
We define a standardised evaluation protocol: (1)Solver: IPOPT via cyipopt, exact Hessian,
sparse Jacobian, tolerance 10−4. (2)Warm-start configuration: warm_start_init_point=yes,
bound_push= 10 −20, mu_strategy=monotone, mu_init= ˆµ. (3)Baseline: the solver’s mid-
point default (l+u)/2 —notthe flat start. (4)Metric: IPOPT iteration count via intermediate()
callback; mean, median, and per-instance counts. (5)Oracle ceiling: ground-truth(x ∗, λ∗, z∗, µ∗).
This protocol addresses the two methodological deficiencies identified in Section 3: the inappropriate
flat-start baseline and the absence of dual variable evaluation.
4.3 Metrics
We evaluate along three axes.Solver convergence: the primary metric is the IPOPT iteration
count.Prediction quality: normalised MSE decomposed into primal and dual components, and
per-variable Pearson correlation. The decomposition is essential—a model with low total loss but
poor dual prediction yields high iteration counts regardless of primal quality (Section 3.3).Topology
robustness: N-1 contingency scenarios (single line removals, no retraining). For topology-blind
models, we report whether they can process the modified topology at all.
5 W ARP: Topology-Aware Primal-Dual Prediction
The oracle results establish that predicting the full state (x, λ, z, µ)is both necessary and sufficient.
W ARP performs this prediction while operating directly on the grid topology.
5.1 Problem formulation
Given gridG= (B,E)with loads(P d, Qd), the task is:
fθ : (G, Pd, Qd)7→(ˆx, ˆλ,ˆzl,ˆzu,ˆµ)(3)
The model must satisfy two requirements beyond pointwise accuracy: (i) the predicted state should
be well-centred (complementarity products approximately uniform), and (ii) it should operate on the
graph structure ofG, enabling application to varying topologies without retraining.
5.2 Architecture
W ARP employs an encode-process-decode (EPD) architecture [Battaglia et al., 2018] with heteroge-
neous interaction networks [Battaglia et al., 2016] on the typed power grid graph (Figure 1).
5

P (i) d , Q(i) d
Loads
Bus, Gen
Node feats
r, x, b, tap
Edge feats
Concat
Per-type Encoder
Wτ(v) ·x v →d= 128
e(i)
Interaction Network
Processor
×K= 15unshared blocks
g(i)
Primals
Va, Vm, Pg, Qg
Duals
λ, zl, zu
Barrierµ
attn pool

ˆx,ˆλ,ˆz,ˆµ 
IPOPT
µinit = ˆµ,monotone
Global load skip
Interaction Network Block
(one ofK= 15, unshared weights)
h(k) v h(k) e
Edge MLP
(hs, hr, e)→R d
+
LN
X
e′
Node MLP
(hv,agg)→R d
LN
h(k+1) v
Figure 1:W ARP architecture. Left:The encode-process-decode pipeline maps load demands and
grid topology to the full interior-point state(ˆx,ˆλ,ˆz,ˆµ), which warm-starts IPOPT.Right:Detail of
one interaction network block (K= 15total, unshared weights).
Graph construction.Three node types (bus, generator, load) and four directed edge types (AC line,
transformer, generator-bus, load-bus). Node features comprise static grid parameters and instance-
varying load injections (P d i , Qd i ); edge features comprise branch parameters. Load values are injected
directly onto bus and generator features—a design choice that resolved an early failure mode where
the model predicted the training-set mean for all instances.
Encoder.Per-type linear projections map to latent dimension d: h(0) v =W τ(v) xv, h(0) e =W τ(e) xe.
Input dimensions: bus ( 6→d ), generator (13→d ), load (2→d ), AC line (9→d ), transformer
(11→d).
Processor.Kinteraction network blocks withunsharedparameters. Each blockkperforms:
h(k+1) e =h (k) e + LN  MLP(k) e,τ(e)  h(k) e , h(k) s(e), h(k) r(e)  (4)
h(k+1) v = LN  MLP(k) v,τ(v)  h(k) v , P e→v h(k+1) e  (5)
where s(e) and r(e) are sender/receiver nodes, LN is layer normalisation, and the summation
aggregates incoming edge embeddings by type. Each MLP is two-layer with hidden dimension d and
ReLU. The processor comprises7Kunshared MLPs.
Theabsence of node residual connectionsin (5)—departing from MeshGraphNets [Pfaff et al., 2021]
and GraphCast [Lam et al., 2023]—is a deliberate choice justified in Section 6.2. Edge residuals (4)
are retained.
6

Decoder.Per-type MLPs: MLPbus(h(K) v )→R 8 (primal + dual per bus), MLPgen(h(K) v )→R 6
(primal + dual per generator). The barrier parameter ˆµis predicted via attention-weighted pooling:
ˆµ= softplus(MLPµ(P i αih(K) i ))with learned attentionα i.
5.3 Training
The loss combines normalised MSE on primals with a binding-mask decomposition on bound
multipliers:
L=
ˆyprimal −y ∗ primal 2 +∥ˆzbind −z ∗ bind∥2 + 0.1· ∥ˆznon-bind∥2 (6)
where binding status is determined by |z∗ i |>10 −4. All targets are normalised to N(0,1) . The mask
decomposition addresses the sparsity structure: the majority of z∗ i are zero, and the model is penalised
less for small non-zero values at non-binding components than for mispredicting binding magnitudes.
We train with AdamW, batch size 32 (PyG DataLoader), learning rate3×10 −4 with linear warmup
(10 epochs) and step decay (×0.9 every 20 epochs), gradient clipping at norm 1.0, for 200 epochs
(∼3h on a single A100). Default: d= 128 , K= 15 , yielding 6.4M parameters. Full details in
Appendix I.
6 Experiments
Setup.OPFDataset case118; single NVIDIA A100-SXM4-40GB. Baselines: (1) cold start (mid-
point), (2) IPM-LSTM [Gao et al., 2024] (17K params, coordinate-wise LSTM, same dual-labeled
data and warm-start protocol), (3) oracle.
6.1 Main results
Table 3: IPOPT iterations on case118 (50 test instances). WARP trained on primal-dual targets
achieves 76% reduction; the same architecture trained on primals only yields no improvement.
IPM-LSTM achieves81%with richer training supervision but cannot handle topology variations.
Method Prediction target Params Mean iters Reduction Topology
Cold start — — 22.6 — N/A
W ARP (primal only)ˆx6.4M 21.1+7%Yes
IPM-LSTM(ˆx, ˆλ,ˆz,ˆµ)17K 4.3+81%No
W ARP (primal-dual)(ˆx, ˆλ,ˆz,ˆµ)6.4M 5.4+76%Yes
Oracle Ground-truth state — 3.2+86%N/A
Table 3 presents the primary comparison. WARP achieves 5.4 mean iterations (76% reduction).
Critically, the same architecture trained onprimal targets onlyachieves 21.1 iterations—identical
to the normalised DetGNN in Table 1 and no better than the midpoint default. This controlled
comparison confirms that the iteration reduction is attributable to dual prediction, not to architectural
capacity or training procedure.
Why the LSTM outperforms WARP on fixed topology.IPM-LSTM achieves 4.3 iterations
versus WARP’s 5.4 on case118—a consistent 1-iteration gap across instances (Appendix J). Two
factors explain this: (1)Per-coordinate specialisation: the LSTM assigns independent learned
parameters to each of its 1,640 input coordinates, effectively memorising per-variable mappings for a
fixed topology. W ARP shares MLP parameters across all nodes of the same type, limiting per-node
specialisation but enabling topology transfer. (2)Richer supervision: the LSTM is trained on KKT
trajectories(10 outer IPM iterations × 5 inner LSTM steps), observing Newton dynamics. W ARP
performs single-step regression from loads to the converged state. This trajectory-level supervision is
only possible because the LSTM operates on a fixed-dimension vector; it cannot generalise to new
topologies (Section 6.3).
7

Table 4: Architecture ablation on case118. Each row adds one modification to the previous. Removing
node residual connections is the most impactful change.
Configuration Val loss IPOPT iters Key modification
Node-only GNN (8L,H= 128) 1.00 8.0 Baseline
+ EPD + edge updates + unshared 0.45 7.0 Interaction network
+ Binding-mask loss 1.07 6.7 Loss decomposition
+ Two-stage decode 0.85 6.7 Primal→dual conditioning
+ No node residuals 0.09 5.4 Key finding (5×loss improvement)
6.2 Architecture ablations
Table 4 traces the progression from a node-only GNN to the final W ARP configuration.Edge updates
are the dominant feature:transitioning to EPD with per-step edge updates reduced iterations from
8.0 to 7.0. We independently validated this on CANOS-OPF [Piloto et al., 2024] using PF∆ [Rivera
et al., 2025]: removing edge updates degrades primal loss by 2.8×, while removing node or edge
residuals has a neutral or beneficial effect (Table 5).
Table 5: Independent ablation on CANOS-OPF (primal-only, case118). Edge updates are the sole
critical feature; node residuals are detrimental.
Variant Val loss vs. Full
Full CANOS 0.019 —
No node residuals0.0036×better
No edge residuals 0.015 Slightly better
No edge updates 0.0532.8×worse
Removing node residuals improves dual prediction by 5×.On W ARP, removing the additive skip
hv ←h v + ∆hv in (5) reduced validation loss from 0.45 to 0.09 and iterations from 7.0 to 5.4. The
CANOS ablation corroborates this: removing node residuals improvedprimal-onlyloss by6×.
We hypothesise that node residual connections anchor representations to the initial encoding—static
grid parameters (impedance, voltage limits)—across all processor steps. For primal prediction, this is
a useful bias. For dual prediction, the initial encoding is largely uninformative about binding status
under a specific load scenario; without residuals, the processor freely reshapes representations to
encode binding patterns that emerge through message passing. Wider models ( d= 256 , ∼25M
params) and longer training (500 epochs) did not improve beyond 5.3–5.4 iterations (Appendix G).
6.3 Topology generalisation
Table 6: N-1 contingency test (20 line removals, no retraining). WARP handles all topologies; the
LSTM fails on every contingency due to fixed input dimensionality.
Metric W ARP IPM-LSTM
Contingencies processed 20/20 0/20
Valid predictions 20/20 —
Mean bus prediction change 4.5% —
Mean gen prediction change 4.9% —
Failure mode — Dimension mismatch
W ARP produces valid predictions for all 20 N-1 contingencies (Table 6), with physically reasonable
prediction changes and topology-sensitive variation across contingencies. The IPM-LSTM fails on
every case: its input layer requires exactly 1,640 coordinates, and line removal alters the constraint
structure. Zero-shot transfer to case6470 (6,470 buses) produces weak predictions (r <0.2); effective
cross-scale transfer requires multi-topology training (Appendix M).
8

7 Related Work
Warm-starting IPMs.The theoretical difficulty is well-established [Yildirim and Wright, 2002,
Forsgren, 2006]. All prior primal warm-starts for OPF evaluate against the flat start. Our contribution
is the first systematic diagnosis ofwhyprimal-only warm-starts fail, a corrected benchmark, and a
topology-aware GNN baseline. Gao et al. [2024] addressed the primal-dual requirement for QPs; we
extend to AC-OPF and characterise the architectural principles.
GNNs for physical simulation.W ARP’s EPD architecture [Battaglia et al., 2016, Pfaff et al., 2021,
Lam et al., 2023] is standard for learned simulation. Our finding that node residuals harm dual
prediction may generalise to other settings requiring Lagrange multiplier or complementarity variable
prediction.
Dual variable prediction.Klamkin et al. [2024] proposed dual completion layers targeting solution
quality; Liu et al. [2022] predicted locational marginal prices. To our knowledge, WARP is the
first model predicting the complete IPM state—primals, equality multipliers, bound multipliers, and
barrier parameter—for solver warm-starting.
8 Conclusion
We established three findings for learning-based IPM warm-starting. First, primal-only warm-
starts are structurally misaligned with interior-point convergence: the solver’s midpoint default is
near-optimal for centrality, and no learned primal iterate improves upon it. Second, the complete
primal-dual-barrier state is both necessary and sufficient, yielding an 85% iteration reduction ceiling
with the entire gap attributable to dual variables and the barrier parameter. Third, topology-aware
graph networks can predict this state with sufficient accuracy: W ARP achieves 76% reduction within
5 percentage points of a topology-blind LSTM while natively supporting N-1 contingencies.
Limitations.Results are demonstrated on a single test system (case118). Dual label extraction
for larger systems is computationally prohibitive ( >60 min/solve for case6470). Zero-shot cross-
scale transfer produces low-quality predictions. The diffusion-based variant did not improve over
deterministic prediction (Appendix K).
Broader impact.Faster AC-OPF enables more frequent re-dispatch, improving renewable integra-
tion and reducing curtailment. The corrected benchmark and evaluation protocol may prevent future
work from reporting inflated gains against inappropriate baselines.
Reproducibility.Code, trained weights, dual-labeled datasets (OpenML), Croissant metadata, and
the complete evaluation pipeline are released publicly. Given only the released artifacts, a practitioner
can reproduce every result in this paper.
References
Marcin Andrychowicz, Misha Denil, Sergio Gomez, Matthew W Hoffman, David Pfau, Tom Schaul,
Brendan Shillingford, and Nando De Freitas. Learning to learn by gradient descent by gradient
descent. InAdvances in Neural Information Processing Systems (NeurIPS), 2016.
Kyri Baker. Learning warm-start points for AC optimal power flow. InIEEE International Workshop
on Machine Learning for Signal Processing (MLSP), pages 1–6, 2019.
Peter Battaglia, Razvan Pascanu, Matthew Lai, Danilo Jimenez Rezende, and Koray Kavukcuoglu.
Interaction networks for learning about objects, relations and physics. InAdvances in Neural
Information Processing Systems (NeurIPS), 2016.
Peter W Battaglia et al. Relational inductive biases, deep learning, and graph networks.arXiv preprint
arXiv:1806.01261, 2018.
Yoshua Bengio, Andrea Lodi, and Antoine Prouvost. Machine learning for combinatorial optimization:
A methodological tour d’horizon.European Journal of Operational Research, 290(2):405–421,
2021.
9

Shourya Bose, Kejun Chen, and Yu Zhang. Learning to optimize: Accelerating optimal power flow
via data-driven constraint screening.arXiv preprint arXiv:2312.07276, 2023.
Jack Briden, Han-Lim Choi, Brandon Riedel, Koki Ho, and Richard Linares. Constraint-informed
learning for warm-starting trajectory optimization.Journal of Guidance, Control, and Dynamics,
47(6), 2024.
Mary B Cain, Richard P O’Neill, and Anya Castillo. History of optimal power flow and formulations.
Technical report, FERC Staff Technical Paper, 2012.
Y Cao, H Zhao, G Liang, J Zhao, H Liao, and C Yang. Fast and explainable warm-start point learning
for AC optimal power flow using decision tree.International Journal of Electrical Power & Energy
Systems, 153:109369, 2023.
Zhi Chen et al. Learning constrained optimization with deep augmented Lagrangian methods.arXiv
preprint arXiv:2403.03454, 2024.
A Deihim, D Apostolopoulou, and E Alonso. Initial estimate of AC optimal power flow with graph
neural networks.Electric Power Systems Research, 234:110782, 2024.
Deepjyoti Deka and Sidhant Misra. Learning for DC-OPF: Classifying active sets using neural nets.
InIEEE Power Systems Computation Conference (PSCC), 2019.
Frederik Diehl. Warm-starting AC optimal power flow with graph neural networks. InNeurIPS
Climate Change AI Workshop, 2019.
Priya L Donti, David Rolnick, and J Zico Kolter. DC3: A learning method for optimization with hard
constraints. InInternational Conference on Learning Representations (ICLR), 2021.
Thomas Falconer and Letif Mones. Deep learning architectures for inference of AC-OPF solutions.
arXiv preprint arXiv:2011.03352, 2023.
Ferdinando Fioretto, Terrence WK Mak, and Pascal Van Hentenryck. Predicting AC optimal power
flows: Combining deep learning and Lagrangian dual methods. InAAAI Conference on Artificial
Intelligence, volume 34, pages 630–637, 2020.
Anders Forsgren. On warm starts for interior methods.System Modeling and Optimization, pages
51–66, 2006.
Xi Gao, Jinxin Xiong, Akang Wang, Qihong Duan, Jiang Xue, and Qingjiang Shi. IPM-LSTM:
A learning-based interior point method for solving nonlinear programs. InAdvances in Neural
Information Processing Systems (NeurIPS), 2024.
Fouad Hasan, Amin Kargarian, and Javad Mohammadi. Hybrid learning aided inactive constraints
filtering algorithm to enhance AC OPF solution time. InIEEE Power & Energy Society General
Meeting (PESGM), 2020.
Joshua Klamkin, Mathieu Tanneau, and Pascal Van Hentenryck. Dual interior point optimization
learning. InAdvances in Neural Information Processing Systems (NeurIPS), 2024.
James Kotary, Ferdinando Fioretto, Pascal Van Hentenryck, and Bryan Wilder. End-to-end constrained
optimization learning: A survey.International Joint Conference on Artificial Intelligence (IJCAI),
2021.
Remi Lam et al. Learning skillful medium-range global weather forecasting.Science, 382:1416–1421,
2023.
Meiyi Li, Soheil Kolouri, and Javad Mohammadi. Learning to solve optimization problems with hard
linear constraints.IEEE Access, 2023.
Enming Liang, Minghua Chen, and Steven Low. Low complexity homeomorphic projection to
ensure neural-network solution feasibility for optimization over (non-)convex set. InConference
on Parsimony and Learning (Recent Spotlight Track), 2023.
10

Shaohui Liu, Chengyang Wu, and Hao Zhu. Topology-aware graph neural networks for learning
feasible and adaptive AC-OPF solutions.IEEE Transactions on Power Systems, 38(5):4477–4488,
2022.
Sidhant Misra, Line A Roald, and Yeesian Ng. Learning for constrained optimization: Identifying
optimal active constraint sets.INFORMS Journal on Computing, 34(1):463–480, 2022.
Yurii Nesterov and Arkadii Nemirovskii.Interior-Point Polynomial Algorithms in Convex Program-
ming. SIAM, 1994.
Jorge Nocedal and Stephen J Wright.Numerical Optimization. Springer, 1999.
Seonho Park and Pascal Van Hentenryck. Self-supervised primal-dual learning for constrained
optimization. InAAAI Conference on Artificial Intelligence, volume 37, pages 4052–4060, 2023.
Tobias Pfaff, Meire Fortunato, Alvaro Sanchez-Gonzalez, and Peter Battaglia. Learning mesh-based
simulation with graph networks. InInternational Conference on Learning Representations (ICLR),
2021.
Luis Piloto et al. CANOS: A fast and scalable neural AC-OPF solver robust to N-1 perturbations.
arXiv preprint arXiv:2403.17660, 2024.
Salvador Pineda and Juan M Morales. Data-driven screening of network constraints for unit commit-
ment.IEEE Transactions on Power Systems, 35(5):3695–3705, 2020.
Tomas Rivera, Kiran Bhagavathula, Daniel Carbonero, and Priya L Donti. PFδ: A physics-informed
benchmark for power flow. InNeurIPS Datasets and Benchmarks, 2025.
Rajiv Sambharya, Georgina Hall, Brandon Amos, and Bartolomeo Stellato. Learning to warm-start
fixed-point optimization algorithms.Journal of Machine Learning Research, 25(166), 2024.
Andreas Wächter and Lorenz T Biegler. On the implementation of an interior-point filter line-search
algorithm for large-scale nonlinear programming.Mathematical Programming, 106:25–57, 2006.
Hongye Wang, Carlos E Murillo-Sánchez, Ray D Zimmerman, and Robert J Thomas. On computa-
tional issues of market-based optimal power flow.IEEE Transactions on Power Systems, 22(3):
1185–1193, 2007.
K Xu, X Zhang, and L Qiu. Explainable warm-start point learning for AC optimal power flow using
a novel hybrid stacked ensemble method.Sustainability, 17(2):438, 2025.
Emre Alper Yildirim and Stephen J Wright. Warm-start strategies in interior-point methods for linear
programming.SIAM Journal on Optimization, 12(3):782–810, 2002.
Ling Zhang and Baosen Zhang. Learning to solve the AC optimal power flow via a Lagrangian
approach.North American Power Symposium (NAPS), pages 1–6, 2022.
A AC-OPF formulation
The AC Optimal Power Flow problem determines the minimum-cost dispatch of generators in an
electrical network subject to Kirchhoff’s laws and operational limits. Let G= (B,E) denote the
power grid graph with buses B and branches E. The decision variables comprise bus voltage angles
Va ∈R |B|, bus voltage magnitudes Vm ∈R |B|, generator real power Pg ∈R |Gg|, and generator
reactive powerQ g ∈R |Gg|, collected asx= (V a, Vm, Pg, Qg). The problem is formulated as:
min
x
X
g∈Gg
c2gP 2 g +c 1gPg +c 0g (7)
s.t.P inj i (Va, Vm)−P d i = 0∀i∈ B(8)
Qinj i (Va, Vm)−Q d i = 0∀i∈ B(9)
V min m ≤V m,i ≤V max m ∀i∈ B(10)
|Sij(Va, Vm)| ≤Smax ij ∀(i, j)∈ E(11)
P min g ≤P g,k ≤P max g , Q min g ≤Q g,k ≤Q max g ∀k∈ Gg (12)
11

where P inj i and Qinj i denote the real and reactive power injections given by the AC power flow
equations, P d i and Qd i are the load demands, Sij is the apparent power flow on branch (i, j), and
c2g, c1g, c0g are generator cost coefficients. The power injection at busiis governed by:
P inj i +jQ inj i =V i
|B|X
k=1
Y ∗ ikV ∗ k (13)
where Y∈C |B|×|B| is the bus admittance matrix constructed from branch impedances and shunt
admittances. Problem (7)–(12) is a non-convex nonlinear program (NLP) due to the quadratic
relationship between power injections and voltage phasors in (13).
Interior-point formulation.Introducing slack variables and collecting all inequality constraints,
the NLP assumes the general form:
min
x
f(x)s.t.h(x) = 0, x≥l, x≤u(14)
where f:R n →R is the objective, h:R n →R m collects the equality constraints, and l, u∈R n
are the variable bounds. The IPM replaces the bound constraints with a logarithmic barrier and solves
a sequence of barrier subproblems parameterised byµ >0:
min
x
f(x)−µ
nX
i=1
h
ln(xi −l i) + ln(ui −x i)
i
s.t.h(x) = 0(15)
The first-order optimality conditions of (15) yield the perturbed KKT system:
∇f(x) +J h(x)⊤λ−z l +z u = 0(16)
h(x) = 0(17)
(x−l)◦z l =µe(18)
(u−x)◦z u =µe(19)
where λ∈R m denotes the equality constraint multipliers, zl, zu ∈R n + are the bound multipliers,
Jh(x) is the constraint Jacobian, and ◦ denotes the Hadamard product. The centrality measure at a
given iterate is:
¯µ=(x−l) ⊤zl + (u−x) ⊤zu
2n (20)
An iterate is well-centred when the componentwise complementarity products (xi −l i)zl,i and
(ui −x i)zu,i are approximately uniform across alli.
B PIPS warm-start defect
Pandapower’s PIPS interior-point solver (pipsopf_solver.py) contains a silent initialisation defect
that renders warm-start injection inoperative. At line 118, the solver overwrites the user-supplied
initial pointx 0 with the variable-bound midpoint for all initialisation modes exceptinit="pf":
# pandapower/pypower/pipsopf_solver.py, line 118
if init != "pf":
ll, uu = xmin.copy(), xmax.copy()
ll[xmin == -inf] = -1e10
uu[xmax == inf] = 1e10
x0 = (ll + uu) / 2 # overwrites warm-start
When init="results" is specified, pandapower correctly loads predicted bus voltages from
net.res_bus into the PYPOWER case structure, and om.getv() returns x0 containing these
values. However, PIPS subsequently discards them by executing the midpoint assignment above. The
only initialisation mode that preserves x0 is init="pf", which first runs a full Newton-Raphson
power flow.
12

The runpp wash-out effect.An initial attempted workaround—calling
pp.runpp(init="results") to seed a power flow solution, then pp.runopp(init="pf") so the
OPF solver uses the converged PF result as x0—produced warm-starts that appeared functional
(28.7% fewer iterations than the midpoint). However, different ML models (DetGNN and WARP)
producedidenticaliteration counts on every instance. The reason: Newton-Raphson power flow
converges to a unique fixed point for given loads; both models’ predictions were sufficiently close
that runpp converged both to the same PF solution, after which runopp(init="pf") started from
an identicalx 0.
This failure mode is particularly insidious because it produces results that appear to validate the
warm-start approach: iterations decrease relative to the midpoint, and different models produce
different prediction errors, suggesting the warm-start is functioning. Only the observation that two
architecturally distinct models yieldidentical per-instanceiteration counts reveals the wash-out.
Corrected implementation.We monkey-patch the PIPS solver to treat init="results" identi-
cally toinit="pf", thereby preserving the user-suppliedx 0:
import pandapower.pypower.opf_execute as _opf_exec
_orig = _opf_exec.pipsopf_solver
def _patched(om, ppopt, out_opt=None):
if ppopt.get(’INIT’) == ’results’:
ppopt = dict(ppopt)
ppopt[’INIT’] = ’pf’
return _orig(om, ppopt, out_opt)
_opf_exec.pipsopf_solver = _patched
The patch must be applied to opf_execute.pipsopf_solver (the call site), not to
pipsopf_solver.pipsopf_solver (the definition site), because opf_execute.py imports the
function at module load time via a direct name binding. Patching the definition site has no effect on
the already-bound reference inopf_execute.
C Full primal-only ablation results
C.1 Unnormalised versus normalised prediction
Training-set statistics reveal a100×scale disparity across variable groups:
Table 7: Per-variable training-set statistics for case118 primal variables.
Variable Mean Std Min Max
Va (rad)−0.1970.149−0.630.0
Vm (p.u.) 1.033 0.019 0.94 1.06
Pg (p.u.) 1.486 1.890 0.0 9.2
Qg (p.u.) 0.158 0.657−2.12.0
Without normalisation, the MSE loss is dominated by Pg (100× the variance of Vm), and the
model learns generator dispatch at the expense of voltage predictions. Normalising each target
dimension to N(0,1) improved DetGNN warm-start iterations from 31.0 to 21.1 on PIPS—a 10-
iteration improvement with no architectural modification. All subsequent experiments employ this
normalisation.
C.2 Feasibility projection
We projected predictions onto the strict feasible interior [l+ϵ(u−l), u−ϵ(u−l)] with ϵ= 0.02 .
Results on 50 test instances:
Projection slightly improved DetGNN (31.6→30.9 ) but substantially degraded WARP (33.7→
38.2). W ARP’s generator predictions have RMSE∼1.2–1.7; when projected, inaccurate predictions
13

Table 8: Feasibility projection results (PIPS, 50 instances). Projection does not improve convergence.
Method Mean iters Median vs. Midpoint
Midpoint 19.6 18 —
DetGNN raw 31.6 31+62%
DetGNN projected 30.9 31+58%
W ARP raw 33.7 30+73%
W ARP projected 38.2 36+95%
are clamped to the nearest bound margin, placing x0 near the constraint boundary—worse than the
midpoint for IPM centrality.
Per-instance analysis: only 3 of 50 instances were improved by projected DetGNN warm-starts; 47
were degraded. Even at prediction RMSE <0.08 , 94% of instances are degraded, confirming that
prediction accuracy in solution space is a misaligned objective for IPM warm-starting.
C.3 Centrality blend sweep
We evaluated x0 =αˆxGNN + (1−α)x mid for α∈ {0,0.05,0.1,0.15,0.2,0.3,0.5,0.7,1.0} on 50
test instances:
Table 9: Centrality blend sweep (PIPS, normalised DetGNN, 50 instances).
αMean iters vs. Midpoint
0.00 (midpoint)19.6—
0.05 26.0+33%
0.10 28.8+47%
0.15 26.6+36%
0.20 25.3+29%
0.30 25.0+28%
0.50 25.1+28%
0.70 27.1+39%
1.00 (pure GNN) 21.6+10%
The result does not exhibit the expected convex tradeoff. The midpoint ( α= 0 ) and pure GNN
(α= 1 ) are both local minima; any intermediate blend is worse than either endpoint, with the
maximum degradation at α= 0.1 (28.8 iterations). This indicates that the line segment connecting
a well-centred interior point to an accurate near-boundary point traverses regions of high barrier
curvature in the feasible set. The non-monotonicity is especially striking: the α= 0.1 blend (90%
midpoint, 10% GNN) is substantially worse than either the midpoint or the pure GNN prediction.
This suggests that even small displacements from the midpoint in the direction of the solution are
harmful when they violate the centrality structure.
C.4 Selective warm-start experiments
We tested four selective warm-start variants on PIPS to isolate the contribution of each variable group:
Table 10: Selective warm-start (PIPS, normalised DetGNN, 50 instances).V m is the bottleneck.
Method Mean iters Medµratio Bottleneck
Midpoint 19.6 18 1.000 —
Full GNN 21.6 22 0.736V m
V oltage only (Va, Vm) 21.6 22 1.000V m
V oltage + gen blend (30%) 21.6 22 0.972V m
Angle only (Va) 24.7 25 1.000V m
Generator predictions are irrelevant to the PIPS iteration count: voltage-only warm-start (generators
at midpoint, µ-ratio 1.000) yields identical iterations (21.6) to the full warm-start ( µ-ratio 0.736).
14

The bottleneck is Vm: its feasible range is only 0.12 p.u. ([0.94,1.06] ), so any prediction displacing
Vm from the midpoint (1.00) rapidly approaches constraint boundaries.
The µ-ratio column reports the ratio of the initial centrality ¯µof the warm-started iterate to that of the
midpoint. A ratio of 1.000 indicates identical centrality; 0.736 indicates 26% centrality degradation.
The voltage-only warm-start has the same iterations as the full warm-start but with µ-ratio 1.000
versus 0.736, confirming that the centrality degradation from generator variables does not actually
affect the solver—the convergence penalty is entirely attributable to voltage displacement.
C.5 Barrier-function-aware retraction
For each variableiwhere the centrality product(x i −l i)(ui −x i)falls below a fractionµ tgt of the
midpoint product, we binary-search blendx i toward(l i +u i)/2to restore centrality:
Table 11: Barrier retraction sweep (PIPS, normalised DetGNN, 50 instances).
µtgt Mean iters vs. Midpoint
Midpoint 19.6 —
0.10 21.6+10.2%
0.30 21.4+9.4%
0.50 21.3+8.8%
0.70 21.3+8.7%
0.90 23.8+21.7%
The best retraction (µtgt = 0.7) reduces the penalty from 10.2% to 8.7%—a marginal improvement.
The retraction correctly identifies and corrects the worst-centralised variables but cannot eliminate
the fundamental displacement cost. At µtgt = 0.9, the retraction is too aggressive: it pulls nearly all
variables back toward the midpoint, effectively negating the warm-start while introducing noise from
the binary search process, resulting in 23.8 iterations (worse than the unretracted 21.6).
C.6 Constraint screening
We used DetGNN predictions to identify and remove non-binding constraints at four Vm margin
thresholds:
Table 12: Constraint screening (PIPS, 50 instances). Removing constraints degrades IPM conver-
gence.
Vm margin Mean iters Constraints removed Convergence rate
Midpoint 19.6 0% 100%
0.005 42.9 81% 4%
0.010 42.5 79% 0%
0.020 44.1 76% 0%
0.030 51.7 72% 0%
Constraint screening is catastrophically counterproductive for PIPS: iteration counts increase by2–3×
and convergence rates drop to 0–4%. For interior-point methods, constraints define the log-barrier
landscape; removing them widens the feasible set, shifts the analytic centre, and flattens the barrier
function. This approach, effective for simplex-based solvers [Pineda and Morales, 2020, Misra et al.,
2022] where removing constraints directly reduces the tableau size, is structurally incompatible with
IPM.
The convergence failure is especially notable: at all margins except 0.005, PIPS fails to converge
within 200 iterations on any test instance. The few instances that converge at margin 0.005 do so
only because the screening at that threshold happens to remove a subset of constraints that does not
substantially alter the barrier landscape.
C.7 Hybrid screening and warm-start
Combining constraint screening with warm-starting does not mitigate the failure:
15

Table 13: Hybrid screening + warm-start (PIPS, 50 instances).
Method Mean iters vs. Midpoint
Midpoint 19.6 —
Screening + midpoint 44.1+125%
Screening + warm-start 50.0+155%
Warm-start only 21.6+10%
The combination is worse than either alone: screening degrades the barrier landscape, and the
warm-start displaces from the (now shifted) analytic centre, compounding both failure modes.
C.8 W ARP diffusion variant results (primal-only)
Six W ARP diffusion variants were trained with varying physics loss weightsλphy:
Table 14: WARP diffusion variants (PIPS, 50 instances). The variant with the best denoising loss
produces the worst warm-start, demonstrating anticorrelation between prediction quality and solver
convergence.
Configλ phy ValL ddpm ValL phy PIPS iters
F (no physics) 0.00.26581.1 39.5
A (baseline) 0.1 0.386 8.6 35.5
D (T= 200) 0.1 0.443 8.3 39.8
B (H= 256) 0.5 0.454 44.3 47.3
C (heavy physics) 1.0 0.5762.6 28.8
The anticorrelation between Lddpm and solver performance is evident: Variant F (best denoising,
Lddpm = 0.265) yields the worst PIPS count (39.5), while Variant C (worst denoising, Lddpm =
0.576) yields the best (28.8). Physical consistency of the predicted state governs solver convergence
more than pointwise accuracy.
This finding has implications for loss function design: a standard MSE or denoising loss optimises
for proximity to x∗ in solution space, but what the IPM needs is proximity to a well-centred point on
the central path. These are geometrically distinct objectives, and optimising one can harm the other.
D Oracle experiment details
D.1 IPOPT configuration
All oracle and model-based IPOPT experiments use the following configuration:
Table 15: IPOPT solver configuration used throughout all experiments.
Parameter Value
tol10 −4
max_iter200
hessian_approximationexact
linear_solverMUMPS
warm_start_init_pointyes
warm_start_bound_push10 −20
warm_start_bound_frac10 −20
warm_start_slack_bound_push10 −20
warm_start_mult_bound_push10 −20
mu_strategymonotone
mu_initmodel-predictedˆµ(or extractedµ ∗)
Iteration counts are measured via the intermediate() callback, counting the number of invocations
prior to convergence.
16

D.2 cyipopt interface
We implemented a direct cyipopt interface (eval/opf_ipopt.py) with:
• Exact Hessian computation viaopf_hessfcn(not L-BFGS approximation)
• Sparse Jacobian with pre-computed sparsity structure from the admittance matrix
• Full warm-start support for(x 0, λ0, zl,0, zu,0)with user-specifiedµ init
• C-level stdout capture for parsing IPOPT’s iteration log
The exact Hessian is critical for fair comparison: L-BFGS approximation would add iterations
unrelated to the warm-start quality. The sparse Jacobian structure is pre-computed from the admittance
matrix topology and reused across all instances and warm-start configurations.
D.3 Full oracle decomposition
Table 16 extends the oracle results from the main text with theλ-only row:
Table 16: Full oracle decomposition (IPOPT, case118, 50 instances). Each row adds one component.
Warm-start content Mean iters Median vs. Cold
Cold start (midpoint) 22.6 22 —
Oraclex ∗ only 23.7 23−4.9%
GTx ∗ (cold dual init)>50 — Diverges
Oracle(x ∗, λ∗)only 12.4 12+45.1%
Oracle(x ∗, λ∗, z∗)4.7 5+79.2%
Oracle(x ∗, λ∗, z∗, µ∗)3.3 3+85.4%
The decomposition reveals a clear hierarchy:
• Primalx ∗ alone:negativecontribution (−4.9%). Worse than cold start.
• Adding λ∗: +45% reduction (22.6→12.4 ). Equality multipliers provide substantial but
incomplete information.
• Adding z∗: +79% (12.4→4.7 ). Bound multipliers contribute more than equality multi-
pliers. This is expected: bound multipliers encode which constraints are binding, which
directly determines the barrier landscape near the solution.
• Adding µ∗: +85% (4.7→3.3 ). The barrier parameter tells the solver where on the central
path to begin, avoiding the need to search for the correctµscale.
D.4 Ground-truth divergence analysis
When the ground-truth optimal solution x∗ is provided as a cold primal start (with default dual
initialisation), IPOPT exceeds 50 iterations without convergence on all test instances. This occurs
because x∗ lies at the boundary of the feasible set: for active bound constraints, x∗ i −l i ≈0 or
ui −x ∗ i ≈0 , causing the log-barrier terms ln(xi −l i) and ln(ui −x i) to approach −∞. The initial
barrier function value is effectively infinite, and the Newton step is ill-conditioned.
This result is consistent with Theorem 3.1 of Yildirim and Wright [2002], which establishes that
for linear programs, the number of IPM iterations required from a warm-start grows without bound
as the warm-start approaches the optimal solution along the boundary of the feasible set. Our
experiments extend this theoretical result to the non-convex AC-OPF setting, providing the first
empirical confirmation that ground-truth warm-starts cause divergence in practice.
D.5 Power flow warm-start results
Newton-Raphson power flow on case118 is too well-conditioned for warm-starting to provide benefit:
Even oracle initialisation slightlyincreasesthe NR iteration count. The flat start ( Vm = 1, Va = 0)
is already close to the PF solution and produces a well-conditioned Jacobian. DC initialisation
17

Table 17: Power flow (Newton-Raphson) warm-start results (case118, 50 instances).
Method Mean NR iters Min Max
Flat start (Vm = 1, Va = 0) 4.00 4 4
DC initialisation 3.00 3 3
DetGNN warm-start 4.60 4 5
Oracle (GT voltages) 4.48 4 5
reduces by one iteration because it provides a structurally consistent approximation (correct angle
relationships), not just a point estimate. This confirms that case118 PF is sufficiently well-conditioned
that ML warm-starting provides no benefit for power flow on this system.
E Dual label extraction pipeline
E.1 Extraction procedure
For each instanceiin the dataset, we:
1. Load the OPFDataset HeteroData graph containing bus, generator, load, and branch data.
2. Construct the cyipopt NLP problem with exact Hessian and sparse Jacobian structure.
3. Initialise IPOPT at the midpoint(l+u)/2with default dual initialisation.
4. Run IPOPT to convergence (tolerance10 −4).
5. Extract the full converged state:D i = (x∗ i , λ∗ i , z∗ l,i, z∗ u,i, µ∗ i , f(x∗ i )).
6. Save as a PyTorch tensor file:data/duals/case118/{split}/duals_{idx:06d}.pt.
E.2 Convergence statistics
Table 18: Dual label extraction statistics for case118.
Split Instances Converged Rate Mean time (s) Total time (h)
Train 5,000 5,000 100% 2.5 3.5
Validation 500 500 100% 2.5 0.35
Test 50 50 100% 2.5 0.035
E.3 Dual variable distributions
The extracted dual variables exhibit the following characteristics:
Table 19: Dual variable statistics across 5,000 training instances.
Variable group Dims Range Std Sparsity
λP (real power balance) 118[−14,4168]1564 0%
λQ (reactive power balance) 118[−13.7,48.9]8.3 0%
zbus l (lower bound, bus) 236[0,561.6]42.1 78%
zbus u (upper bound, bus) 236[0,2527.6]189.3 72%
zgen l (lower bound, gen) 108[0,243.6]18.7 81%
zgen u (upper bound, gen) 108[0,47.9]5.2 85%
µ(barrier parameter) 1≈3.25×10 −8 <10 −10 —
Equality multipliers (λP , λQ) are dense and span 4–5 orders of magnitude. Bound multipliers (zl, zu)
are 72–85% sparse (exactly zero for non-binding constraints) with heavy-tailed non-zero entries. The
barrier parameter µ is approximately constant across all instances, reflecting the solver’s convergence
tolerance. These characteristics—high dynamic range, sparsity, and mixed discrete-continuous
structure—distinguish dual prediction from the smooth primal regression task addressed by prior
work.
18

E.4 Normalisation statistics
Per-dimension normalisation to N(0,1) is computed from the training set. Each of the 926 output
dimensions (118×8 bus + 54×6 gen + 1 µ) has its own mean and standard deviation. Without this
normalisation, dual prediction MSE is dominated by λP (std = 1564), and the model cannot learn
the small-magnitude but IPOPT-critical bound multipliers. Normalisation reduced validation dual
error from9.45×10 5 to3×10 −4.
E.5 Inequality constraint multipliers
The 372 inequality constraint multipliers corresponding to line flow limits (|Sij| ≤Smax ij ) areexactly
zeroacross all 50 test instances and all 5,000 training instances. No thermal line constraints are
binding on case118 under the OPFDataset load variations. Consequently, the model need not predict
these multipliers; they are excluded from the output and loss computation. This is a property of the
case118 load variation range, not a general property of AC-OPF; larger systems with heavier loading
would exhibit binding thermal constraints.
F Architecture details
F.1 Full model specification
Table 20: W ARP architecture specification (d= 128,K= 15).
Component Structure In Out Params
Encoder (7 per-type linear projections)
Bus encoder Linear + bias 6 128 896
Generator encoder Linear + bias 13 128 1,792
Load encoder Linear + bias 2 128 384
AC line edge encoder Linear + bias 9 128 1,280
Transformer edge encoder Linear + bias 11 128 1,536
Gen-bus edge encoder Linear + bias 2 128 384
Load-bus edge encoder Linear + bias 2 128 384
Encoder total6,656
Processor (×15unshared interaction network blocks)
Edge MLP (×4types×15)384→128→128 3d d57,472 ea.
Edge LayerNorm (×4×15) Affine LN 128 128 256 ea.
Node MLP (×3types×15)256→128→128 2d d49,408 ea.
Node LayerNorm (×3×15) Affine LN 128 128 256 ea.
Edge MLPs total60×57,4723,448,320
Edge LNs total60×25615,360
Node MLPs total45×49,4082,223,360
Node LNs total45×25611,520
Processor total5,698,560
Decoder
Bus head128→256→8128 8 35,080
Generator head128→256→6128 6 34,566
µattention vector Linear (no bias) 128 1 128
µMLP128→64→1+ softplus 128 1 8,321
Decoder total78,095
Grand total∼5.78M
The processor dominates the parameter budget (98.5%), with edge MLPs accounting for 59.6% and
node MLPs for 38.4%. Encoder and decoder contribute only 1.5%.
Per-block detail.Each of the 15 processor blocks contains: 4 edge-update MLPs (one per edge
type), each mapping R3d →R d; 4 edge LayerNorm modules; 3 node-update MLPs, each mapping
19

R2d →R d; 3 node LayerNorm modules. Edge updates retain residual connections; node updates do
not. All 15 blocks have independent (unshared) parameters.
F.2 Heterogeneous graph construction
The power grid is represented as a PyGHeteroDataobject with the following structure:
• Bus nodes( |B|= 118 ): features are base kV ,V min m , V max m , bus type (PQ/PV/slack), plus
injected load(P d i , Qd i )scattered from connected load nodes. Total: 6 features.
• Generator nodes( |Gg|= 54 ): features are P min g , P max g , Qmin g , Qmax g , cost coefficients
c0, c1, c2, ramp rates, startup/shutdown costs, plus injected bus load. Total: 13 features.
•Load nodes(|L|): features are(P d i , Qd i ). Total: 2 features.
• AC line edges: from-bus → to-bus (and reverse), features are resistance r, reactance x,
susceptance b, thermal rating, tap ratio (1.0 for lines), angle limits. Total: 9 features per
direction.
• Transformer edges: same structure as AC lines but with non-unity tap ratio and phase shift.
Total: 11 features per direction.
•Generator-bus edges: bidirectional, features are the generator’s bus connection index and
participation factor. Total: 2 features.
• Load-bus edges: directed (load → bus), features are load priority and status. Total: 2
features.
F.3 Load injection
The only features that vary between instances are the load demands (P d i , Qd i ). All bus, generator, and
edge features are static across the dataset. To ensure the model can distinguish between instances,
load values are injected in two ways:
1. Direct concatenation: (P d i , Qd i ) are appended to the feature vector of the bus node at which
the load is connected, and to the feature vectors of all generators connected to that bus.
2. Global load skip: the sum of all loads P i(P d i , Qd i ) is passed through a small MLP and concatenated to the generator decoder input, providing a global demand signal.
Without load injection, the model outputs near-constant predictions (pred std ∼0.01–0.20 versus true
std ∼0.6–1.0, correlation ≈0 for all variables), as the static graph features carry no instance-specific
information. This failure mode was observed in the initial DetGNN experiments and resolved by
explicit load injection.
F.4 Decoder output mapping
Bus decoder outputs (8 dimensions per bus):
• ˆVa: voltage angle (normalised, unconstrained)
• ˆVm: voltage magnitude (normalised, unconstrained)
• ˆλP : real power balance multiplier (normalised, unconstrained)
• ˆλQ: reactive power balance multiplier (normalised, unconstrained)
•ˆzVa l ,ˆzVm l : lower bound multipliers (normalised, unconstrained—softplus applied post- denormalisation if needed)
•ˆzVa u ,ˆzVm u : upper bound multipliers (normalised)
Generator decoder outputs (6 dimensions per generator):
• ˆPg, ˆQg: generator dispatch (normalised)
•ˆzPg l ,ˆzQg l : lower bound multipliers (normalised)
20

•ˆzPg u ,ˆzQg u : upper bound multipliers (normalised)
All outputs are in normalised space during training. At inference, predictions are denormalised using
training-set statistics before injection into IPOPT.
G Architecture evolution and ablation details
Table 21 traces the complete architectural evolution from the initial node-only GNN to the final
W ARP configuration, reporting both validation loss and IPOPT iteration counts for each variant.
Table 21: Complete architecture evolution (case118). Each row represents a distinct trained model.
Experiment Key modification Params Val loss IPOPT iters Reduction
Node-only GNN (8L,H= 128) Baseline 2.58M 1.00 8.0 65%
Exp A (edge updates) + edge feature updates 3.2M — — —
Exp B (EPD, unshared) + EPD + unshared weights 6.4M — — —
Exp C (16 layers) + depth 8→16 5.1M 1.38 — —
Exp D (sigmoid bounds) + sigmoid clamping 2.6M 1.78 — —
Exp E (EPD combined) EPD + edges + unshared 6.41M 0.45 7.0 70%
Exp E2 (+ physics loss) + constraint violation 6.42M 1.10 7.2 69%
Exp F (curriculum) + dual weight ramp 6.41M 1.03 7.2 69%
Exp G (binding mask) + binding-mask loss 6.41M 1.07 6.7 71%
Exp H (two-stage) + primal→dual decode 6.48M 0.85 6.7 71%
gnores−node residuals 6.41M0.09 5.4 76%
gnores_bias + per-node bias 6.41M 0.12 5.3 77%
hnores + two-stage + nores 6.48M 0.12 5.3 77%
gh256 (H= 256) Wider model∼25M 0.66 6.6 71%
best_combo (500 ep) All three + long train 6.48M 0.08 5.4 76%
Key observations.
1. Edge updates broke the 1.0 loss floor.The original node-only GNN plateaued at val
loss 1.0 regardless of training configuration. Adding edge updates (Exp E) reduced loss to
0.45—the first time any GNN variant dropped below 1.0. This suggests that edge features
carry information critical for dual prediction that node-only message passing cannot capture.
2. Loss strategies provided modest iteration gains.Binding-mask loss and two-stage decod-
ing each independently reduced iterations from 7.0 to 6.7, but neither reduced validation loss
substantially. The binding mask helps the model allocate capacity to the sparse but critical
binding multipliers; two-stage decoding conditions dual prediction on predicted primals.
3. Removing node residuals was the decisive change.Val loss dropped from 0.45 to 0.09
(5×), and IPOPT iterations from 7.0 to 5.4, from a single architectural modification. This is
the largest single-modification gain in the entire ablation.
4. Further refinements hit a ceiling at 5.3.Per-node bias (1,268 additional parameters)
and two-stage decoding each independently reached 5.3 iterations. Combining all three
(best_combo, 500 epochs) did not push below 5.4, indicating an architectural ceiling for this
model family on case118.
5. Wider models do not help. H= 256 (∼25M params) achieved 6.6 iterations—worse than
H= 128 . The additional capacity introduces optimisation difficulty without improving
representational quality at this problem scale.
6. Physics loss was counterproductive.Adding an AC power balance violation loss (Exp E2)
increased val loss from 0.45 to 1.10 and worsened iterations from 7.0 to 7.2. The physics
loss conflicts with the per-variable normalisation: the power balance residual operates in
physical units, creating a scale mismatch with the normalised MSE.
21

H Independent CANOS ablation
To validate our architectural findings independently, we ran PF ∆’s CANOS-OPF reimplementa-
tion [Rivera et al., 2025] on the same case118 data and ablated three features. CANOS predicts
primal variables only( Va, Vm, Pg, Qg), so this ablation isolates the architectural effect from the dual
prediction task.
Configuration.CANOS-OPF with H= 128 , K= 16 interaction network steps,
include_sent_messages=true, batch size 64, 50,000 training steps with LR warmup and step
decay. Training data: 67,500 instances from OPFDataset (primal labels only).
Table 22: CANOS ablation (primal-only prediction, case118). Results after full training convergence.
Variant Best val loss vs. Full Finding
Full CANOS 0.019 — —
No node residuals0.0036×better Node residuals harmful
No edge residuals 0.015 Slightly better Edge residuals near-neutral
No edge updates 0.0532.8×worse Edge updates are critical
The CANOS ablation corroborates both of our key architectural findings: (i) edge updates are the
dominant feature (2.8× degradation, the largest of any ablation), and (ii) removing node residuals im-
proves performance (6× improvement). The finding that node residuals are detrimental is especially
notable because it contradicts the standard recipe in MeshGraphNets [Pfaff et al., 2021] and Graph-
Cast [Lam et al., 2023], both of which employ node residual connections at every message-passing
step.
The 6× improvement onprimal-onlyprediction (not just dual) suggests that the node-residual finding
is a property of power grid graph structure, not specific to the dual prediction task. We hypothesise
that the static grid parameters (impedance, voltage limits) encoded in the initial node embeddings
anchor representations in a way that impedes the processor’s ability to learn instance-specific patterns
through message passing.
I Training details
I.1 Learning rate schedule
•Warmup: linear increase from 0 to3×10 −4 over the first 10 epochs.
•Step decay: multiply LR by 0.9 every 20 epochs.
• For the 500-epoch best_combo run: decay every 40 epochs (slower schedule).
I.2 Batch construction
We use PyG’s DataLoader for automatic heterogeneous graph batching. PyG merges multiple
HeteroData graphs into a single batch by offsetting edge indices and maintaining per-graph batch
vectors. The GNN’s message passing and element-wise losses operate correctly on batched graphs.
The physics loss (AC power balance violation) requires per-graph admittance matrix construction,
which is incompatible with the merged batch representation. We extract one random graph per batch
viadata.to_data_list()and compute the physics loss on that single graph:
if hasattr(data["bus"], "batch"):
graphs = data.to_data_list()
gi = torch.randint(0, len(graphs), (1,)).item()
bm = data["bus"].batch == gi
gm = data["generator"].batch == gi
bx_s, gx_s = clamp_sol(bx[bm], gx[gm])
G, B = build_ybus(graphs[gi])
Lp = physics_loss(bx_s, gx_s, graphs[gi], G, B)
22

I.3 The batch_size=1 bottleneck
Initial training used batch_size=1, resulting in 67,500 individual forward/backward passes per
epoch (∼19 minutes per epoch, 18% GPU utilisation on A100). Increasing to batch_size=64 with
num_workers=4 reduced epoch time to ∼2 minutes (9.5× speedup) with substantially improved
GPU utilisation.
I.4 Training curves
The gnores model (our best configuration) exhibits the following training trajectory:
Table 23: Training trajectory for gnores (d= 128,K= 15, 200 epochs).
Epoch Val primal Val dual Val total LR
1 — — 1.253.0×10 −5
18 0.75 0.50 1.253.0×10 −4
50 0.30 0.15 0.452.7×10 −4
115 0.093 0.059 0.152.0×10 −4
140 0.073 0.045 0.121.7×10 −4
186 0.059 0.036 0.091.3×10 −4
200 0.065 0.039∼0.101.2×10 −4
The primal-dual decomposition reveals that both components improve throughout training, with the
primal loss converging slightly faster. No overfitting is observed (train and val losses track closely).
The slight uptick at epoch 200 (0.065 vs 0.059 at epoch 186) is within noise; the model has effectively
converged by epoch 150.
I.5 Wall-clock training times
Table 24: Wall-clock training times on a single NVIDIA A100-SXM4-40GB.
Model Epochs Time per epoch Total
LSTM (IPM-LSTM) 200 0.4 s∼80 s
Node-only GNN 200 20 s∼67 min
EPD-GNN (Exp E) 200 55 s∼3 h
gnores (W ARP) 200 29 s∼1.6 h
best_combo 500 25 s∼3.5 h
W ARP-PD (diffusion) 200 31 s∼1.7 h
The gnores model trains faster per epoch than Exp E (29s vs 55s) despite identical architecture
because gnores does not compute the physics loss, which requires per-graph admittance matrix
construction.
J IPM-LSTM baseline reproduction
J.1 Architecture
We reproduce the IPM-LSTM architecture of Gao et al. [2024] adapted for AC-OPF:
• Single-layer coordinate-wise LSTM with shared parameters across all coordinates.
• Input: flattened KKT state vector of dimension 1,640 (118 buses × 8 + 54 generators × 6 +
1µ, after zero-padding to align dimensions).
• Hidden dimension: 50.
• Total parameters: 17,217.
• 10 outer IPM iterations×5 inner LSTM time steps during training.
23

The key difference from the original IPM-LSTM paper is the problem domain: the original evaluated
on convex QPs, QCQPs, and non-convex QPs with up to 200 variables. Our case118 instance has
344 primal variables and 926 total output dimensions.
J.2 Training configuration
• Training data: 2,000 instances with IPOPT-extracted dual labels (same pipeline as Section E).
• Batch size: 128.
• Learning rate:10 −4 (Adam).
• Epochs: 200 (early stopping with patience 50).
• Per-variable normalisation: identical to W ARP (Section 4.1 of the main text).
• Training time:∼80 seconds total on A100.
J.3 Per-instance comparison
Table 25: Per-instance IPOPT iterations: LSTM vs. W ARP vs. Oracle (first 10 test instances).
Instance Cold LSTM W ARP (gnores)
#0 23 5 5
#1 24 4 5
#2 24 4 5
#3 22 4 5
#4 24 4 5
#5 24 5 5
#6 21 4 5
#7 24 4 6
#8 23 4 5
#9 22 4 5
Mean 23.1 4.3 5.4
The LSTM achieves 4 iterations on most instances where W ARP achieves 5. The consistent 1-iteration
gap reflects two factors discussed in the main text: (1) per-coordinate specialisation (each of 1,640
input coordinates has independently learned parameters), and (2) richer training supervision (KKT
trajectory vs single-step regression).
J.4 LSTM topology failure mode
The LSTM’s input layer is Linear(1640, 50) . When a line is removed (N-1 contingency), the
KKT vector structure changes: the number of line flow constraints decreases, altering the dimension
of z. The LSTM raises a RuntimeError: mat1 and mat2 shapes cannot be multiplied
on every N-1 contingency tested (20/20 failures). There is no way to process a modified topology
without retraining a new LSTM with the correct input dimension.
K Diffusion over IPM state (negative result)
K.1 W ARP-PD architecture
The W ARP-PD model wraps the gnores EPD backbone in a DDPM diffusion framework:
• Denoiser: same 15-block EPD-GNN with no-node-residuals, augmented with sinusoidal
timestep embedding (dim 64) projected tod= 128via a 2-layer MLP.
• Input augmentation: noisy IPM state is concatenated to static node features. Bus input: 6
(static) + 8 (noisy state) + 128 (time embedding) = 142 dims. Generator input: 13 + 6 + 128
= 147 dims.
•Noise schedule: cosineβschedule,T= 1000.
•Parameters: 6,466,318 (∼same as deterministic model).
24

K.2 Training
• Loss: DDPM noise prediction loss∥ϵ−ˆϵ θ(xt, t)∥2 on normalised(x, λ, z)targets.
• Batched training with PyG DataLoader (batch size 32), per-graph random timesteps ex-
panded to per-node via batch vectors.
• 200 epochs, 31 s/epoch (∼103 minutes total).
• LR warmup + step decay (same schedule as deterministic model).
K.3 Inference: DDIM sampling with KKT scoring
• DDIM sampling with 50 steps,t start = 0.98T(to avoid division by √¯α999 ≈5×10 −5).
•x 0 clamping to[−5,5]in normalised space at each step.
•K candidate samples scored by a complementarity-based proxy: P i |ˆzl,i ·(ˆxi −l i)−ˆµ|+ |ˆzu,i ·(u i −ˆxi)−ˆµ|in normalised space.
• Lowest-scoring sample passed to IPOPT.
K.4 Results
Table 26: W ARP-PD diffusion results (IPOPT, case118, 50 instances).
Method Val loss IPOPT iters vs. Cold
Deterministic (gnores) 0.095.4+76%
W ARP-PDK= 10.069 6.7+71%
W ARP-PDK= 30.069 6.6+71%
W ARP-PDK= 50.069 7.3+68%
K.5 Analysis of failure
The diffusion model achieves lower val loss (0.069 vs. 0.09) but worse IPOPT iterations (6.6 vs. 5.4).
Five factors contribute:
1. The noise prediction task is harder than direct regression.The diffusion model must
learnϵ(x t, t)at every noise level, a strictly harder mapping than directx0 prediction.
2. DDIM sampling introduces cumulative error.Each of the 50 denoising steps contributes
a small approximation error that compounds.
3. The KKT scoring proxy is approximate.A full KKT residual computation (requiring
Jacobian evaluation) would be more accurate but also more expensive.
4. Case118 is effectively unimodal.Each load scenario maps to a single well-separated
optimum. Multi-sample diversity provides no benefit when the solution mapping is deter-
ministic.
5.K= 5 is worse than K= 1 .The scoring function may select atypical samples with low
complementarity proxy but poor overall KKT satisfaction, suggesting the proxy metric is
not well-aligned with IPOPT convergence.
Diffusion-based warm-starting may prove beneficial for genuinely multimodal settings such as
stochastic OPF or security-constrained dispatch with combinatorial contingency structure, where the
mapping from parameters to solutions is one-to-many.
K.6 DDIM explosion fix
The original W ARP primal-only diffusion suffered from numerical explosion during DDIM sampling.
At t= 999 , √¯α999 ≈5×10 −5 under the cosine schedule, and the x0 prediction ˆx0 = (x t −√1−¯αt ·ˆϵ)/√¯αt amplifies any noise prediction error by ∼20,000×. The first sampling step
produced|ˆx0|= 2538(expected:∼1.0), and subsequent steps could not recover.
The fix: start sampling from tstart = 0.98T (where √¯α= 0.030, reducing amplification to ∼33×),
and clampˆx0 to physical ranges at each step. This reduced W ARP bus RMSE from 37.5 to 0.17.
25

L N-1 contingency topology test
L.1 Implementation
For each contingency c∈ {1, . . . ,20}, we remove one AC line (and its reverse edge) from the
HeteroData graph:
mask = torch.ones(n_edges, dtype=bool)
mask[line_idx] = False
mask[line_idx + n_lines] = False # reverse edge
data_n1["bus","ac_line","bus"].edge_index =
data["bus","ac_line","bus"].edge_index[:, mask]
data_n1["bus","ac_line","bus"].edge_attr =
data["bus","ac_line","bus"].edge_attr[mask]
No weights are modified; the same trained model processes the modified topology. Lines are selected
to span a range of topological importance (radial endpoints, meshed loops, inter-area ties).
L.2 Results
All 20 contingencies produce valid model outputs with physically reasonable prediction changes:
• Mean absolute prediction change (bus variables): 4.5% of the base-case prediction magni-
tude.
• Mean absolute prediction change (generator variables): 4.9%.
• Prediction variance across contingencies: predictions differ for each removed line, confirm-
ing topology sensitivity.
• No numerical instabilities, NaN outputs, or convergence failures.
The predictions are not merely noise: they vary systematically with which line is removed, with
larger changes for topologically important lines (inter-area ties) and smaller changes for redundant
lines in meshed subnetworks. This confirms that the model is responsive to the graph structure rather
than producing topology-invariant outputs.
The LSTM baseline raises a dimension mismatch error on every contingency because its input layer
requires exactly 1,640 coordinates corresponding to the case118 KKT structure. Removing a line
alters the constraint count, changing the KKT vector dimension.
M Case6470 scaling attempt
M.1 Dataset processing
The OPFDataset for pglib_opf_case6470_rte comprises 6,470 buses, 761 generators, 7,426 AC
lines, and 821 transformers, with 13,500 training and 750 test instances. PyG processing of the
126 GB raw data required approximately 30 minutes.
M.2 Dual extraction: computational barrier
IPOPT solves on the 6,470-bus network proved computationally prohibitive: each solve required>60
minutes (compared to 2.5 seconds for case118), with the bottleneck in the exact Hessian computation
at each iteration. After 51 minutes, no single instance had converged across three parallel extraction
processes. At this rate, extracting 1,000 training instances would require ∼40 days of continuous
computation.
Potential mitigations include: (i) L-BFGS Hessian approximation (trading iterations for per-iteration
cost), (ii) a pandapower-based extraction pipeline with PIPS (which may be more efficient on larger
systems), or (iii) an OPFDataset-to-pandapower network converter. We leave dual extraction at scale
to future work.
26

M.3 Zero-shot transfer results
We evaluated the case118-trained gnores model on case6470 test instances:
Table 27: Zero-shot transfer from case118 to case6470 (primal variable correlation).
Variable PearsonrAssessment
Va 0.14 Weak
Vm −0.06Negligible
Pg −0.21Weak negative
Qg 0.20 Weak
Predictions are effectively random. The model has learned case118-specific patterns (topology
structure, normalisation statistics) that do not transfer to a 55 × larger grid with entirely different
topology. The model executes without error on case6470—demonstrating the architectural flexibility
of graph-based models—but effective cross-scale transfer would require training on diverse topologies
or fine-tuning with case6470 data.
The LSTM baseline cannot process case6470 at all: its input layer requires exactly 1,640 dimensions
(case118 KKT vector), and case6470’s KKT vector has∼13,000 dimensions.
N Raw-space prediction quality
Table 28 reports per-variable prediction quality for the gnores model on a representative test instance,
in raw (denormalised) space:
Table 28: Per-variable prediction quality (gnores, raw space, single representative instance).
Variable RMSE PearsonrTrue range Relative error
Va (rad) 0.008 0.996[0.26,0.64]2.1%
Vm (p.u.) 0.001 0.998[0.99,1.06]1.4%
Pg (p.u.) 0.024 1.000[0.00,4.99]0.5%
Qg (p.u.) 0.032 0.998[−1.82,1.78]0.9%
λP 10.8 0.996[3645,4125]0.3%
λQ 1.35 0.993[−13.7,48.9]2.2%
zbus l 3.44 1.000[0,561.6]0.6%
zbus u 5.19 1.000[0,2527.6]0.2%
zgen l 3.78 0.997[0,243.6]1.6%
zgen u 0.60 0.997[0,47.9]1.3%
All variable groups achieve Pearson correlation >0.99 . The remaining IPOPT iterations (5.4 vs.
oracle 3.2) are attributable to small absolute errors on high-magnitude equality multipliers ( λP :
RMSE 10.8 on values ∼4000) and large-valued upper bound multipliers (zbus u : RMSE 5.2 on values
up to 2528). In relative terms, all predictions are within 2.2% of the true value.
The gap between prediction quality (r >0.99) and solver performance (5.4 vs 3.2 iterations) suggests
that the IPM is highly sensitive to small absolute errors in the dual state—even 0.3% relative error
on λP (which translates to RMSE 10.8 on values ∼4000) is sufficient to add 2 iterations. This
underscores that dual prediction for IPM warm-starting requires higher absolute accuracy than might
be suggested by correlation metrics alone.
O Extended related work
This section provides detailed discussion of related work categories summarised in the main text.
End-to-end solution prediction.One category of methods trains a neural network to approximate
the mapping from problem parameters to optimal solutions, obviating the need for a numerical
solver at inference time. Fioretto et al. [2020] employed supervised learning with Lagrangian
dual penalties to predict AC-OPF solutions. Donti et al. [2021] proposed DC3, which enforces
27

equality constraints via a differentiable completion step and corrects inequality violations through
gradient-based projection. Park and Van Hentenryck [2023] introduced a self-supervised primal-dual
learning scheme that jointly trains primal and dual networks without pre-solved labels. Li et al.
[2023] developed gauge-map projections for problems with linear constraints, while Liang et al.
[2023] proposed homeomorphic projections for non-convex feasible regions. More recently, Chen
et al. [2024] trained networks to predict feasible dual solutions, recovering associated primals via
the stationarity condition. Our objective differs from these approaches: we seek to reduce solver
iterations while retaining the feasibility and optimality guarantees of the numerical method.
Active constraint identification.A related line of work learns to identify the optimal active
constraint set, using this information to formulate a reduced problem. Misra et al. [2022] demonstrated
that learning the optimal active set is a well-posed classification problem with strong generalisation on
DC-OPF benchmarks from PGLib-OPF. Deka and Misra [2019] employed neural network classifiers
for the same task. Pineda and Morales [2020] proposed data-driven constraint screening for unit
commitment, and Hasan et al. [2020] developed hybrid regression-classification methods for inactive
AC-OPF constraint identification. Bose et al. [2023] combined constraint screening with data-driven
selection. These methods reduce the dimensionality of the problem presented to the solver; in contrast,
our approach reduces the iteration count on the full-dimensional problem. We evaluate constraint
screening as one of 15 primal-only strategies and find that it is counterproductive for interior-point
methods (Section 3.1 of the main text).
Learning to optimise.The broader L2O paradigm [Bengio et al., 2021, Kotary et al., 2021]
encompasses methods that replace solvers and methods that accelerate them. Andrychowicz et al.
[2016] introduced the idea of learning optimiser update rules. Sambharya et al. [2024] learned warm-
starts for fixed-point splitting methods on QPs by differentiating through unrolled solver iterations.
Briden et al. [2024] proposed Lagrangian-informed losses for warm-starting trajectory optimisation
under an SQP solver.
Graph neural networks for physical simulation.Battaglia et al. [2016] introduced interaction
networks for learning physical dynamics. Battaglia et al. [2018] formalised the encode-process-decode
framework. Pfaff et al. [2021] developed MeshGraphNets, employing 15 unshared message-passing
steps for mesh-based fluid simulation. Lam et al. [2023] scaled this paradigm to global weather
forecasting with GraphCast. In the power systems domain, Piloto et al. [2024] applied this architecture
to AC-OPF primal prediction, achieving sub-percent error on standard benchmarks, while Rivera et al.
[2025] provided an open-source reimplementation with physics-informed branch flow derivations.
Liu et al. [2022] developed topology-aware GNNs with physics-based feasibility regularisation,
demonstrating adaptivity to topological perturbations. We adopt the same architectural family but
extend it to predict the full primal-dual-barrier state—a task that these prior models do not address.
P Datasheet for dual-labeled OPF dataset
Following the framework of Gebru et al. (2021), we provide a datasheet for the dual-labeled AC-OPF
dataset released as part of the W ARP benchmark.
P.1 Motivation
• Purpose: Enable training and evaluation of ML models that predict the full interior-point
state(x ∗, λ∗, z∗, µ∗)for warm-starting IPM solvers on AC-OPF.
•Creators: The authors of this paper.
•Funding: [Anonymised for review].
P.2 Composition
• Instances: 5,550 AC-OPF problem instances for pglib_opf_case118_ieee (5,000 train /
500 val / 50 test), each comprising a heterogeneous graph (HeteroData) with bus, generator,
load, and branch data, plus the IPOPT-converged primal-dual-barrier solution tuple.
• Instance format: PyTorch tensor files ( .pt) containing (x∗, λ∗, z∗ l , z∗ u, µ∗, f∗) where
x∗ ∈R 344 (118 buses×2 + 54 gens×2),λ ∗ ∈R 236,z ∗ l , z∗ u ∈R 344,µ ∗ ∈R,f ∗ ∈R.
28

• Graph data: from OPFDataset [Falconer and Mones, 2023], which in turn draws from
PGLib-OPF benchmark library.
• No confidential data: all instances are synthetically generated by varying load demands on
a public test system.
•No personally identifiable information.
P.3 Collection process
• Primal labels and graph structure: downloaded from OPFDataset via PyG
(torch_geometric.datasets.OPFDataset).
• Dual labels: extracted by running IPOPT to convergence on each instance using our cyipopt
interface (Appendix D) with exact Hessian and tolerance10 −4.
• Extraction rate:∼2.5 seconds per instance on a single CPU core (Intel Xeon, 2.10 GHz).
• 100% convergence rate across all splits.
P.4 Preprocessing
• Per-dimension normalisation statistics (mean, std) computed on the training set and applied
consistently to validation and test sets.
• Binding status labels derived from|z ∗ i |>10 −4.
• No data augmentation or synthetic modification beyond the OPFDataset’s native load
variation.
P.5 Distribution
• The dataset is hosted on HuggingFace with Croissant metadata (core + RAI fields).
• License: MIT (consistent with PF∆and OPFDataset).
• Format: directory of.ptfiles indexed by split and instance number.
• The extraction pipeline code is released alongside the dataset.
P.6 Maintenance
• The dataset is static and will not be updated after release.
• The extraction pipeline code is included, enabling users to generate dual labels for other
PGLib-OPF test cases.
• Issues may be reported via the associated code repository.
• Long-term hosting is ensured by OpenML’s institutional infrastructure.
29
