---
title: 'PowerZooJax: A JAX-based Power System Benchmark for Reinforcement Learning'
url: https://arxiv.org/abs/2609.36052
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Zhanhua Pan
- Xiao Liu
- Zhilong Cao
- Jianhong Wang
- Dawei Qiu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.36052
pages: 42
chars: 128373
fetched_at: '2026-11-08T13:24:14+00:00'
kb_version: 1
---

# PowerZooJax: A JAX-based Power System Benchmark for Reinforcement Learning

PowerZooJax: A JAX-based Power System
Benchmark for Reinforcement Learning
Zhanhua Pan1†, Xiao Liu2†, Zhilong Cao1, Jianhong Wang3‡, Dawei Qiu1‡∗
1Nanyang Technological University, Singapore. 2Cornell University, USA. 3University of Bristol, UK.
Abstract
Power system operation is a safety-critical sequential decision-making problem,
making it a natural testbed for reinforcement learning (RL). However, existing RL
environments for power systems are often narrow in scope and computationally lim-
ited by CPU-based simulation workflows, making large-scale evaluation difficult.
We introduce PowerZooJax, a JAX-based benchmark suite for RL in power system
operation. It provides five constrained Markov decision process tasks spanning
generation, transmission, distribution, distributed energy resources, and data center
microgrid. By rewriting power flow, economic dispatch, market clearing, and de-
vice dynamics as JAX computation graphs, PowerZooJax keeps the entire training
and evaluation loop on the GPU. Experiments show substantial speedups over CPU-
based simulations and demonstrate standardized evaluation of policy returns, safety
violations, and out-of-distribution stress conditions. Our open-source benchmark is
available at:https://github.com/powerzoojax/PowerZooJax.
Benchmark
Task
JAX code
Batched
environments
@jax.vmap
CMDP
trajectories
[ T × B ]
Power system physical model Accelerated Linear Algebra (XLA)-compatible training process
obs × B
action × B
Actor
(policy network)
Learner
(policy update)
GenCos TSO
DSO
DERs
DCMG
CMDP transition T
JAX formulation
Loop
Figure 1: Execution paradigm of PowerZooJax.
1 Introduction
Power systems are undergoing a fundamental transformation driven by the 3Ds: decarbonization,
decentralization, and digitalization [1]. Traditionally, power systems were operated around centralized
generation, long-distance transmission, and largely passive demand. This paradigm is increasingly
challenged by the growing integration of renewable generation, distributed energy resources (DERs),
battery storage, electric vehicle (EV) charging, flexible loads, and emerging critical infrastructure
such as data centers [2]. Furthermore, the rise of artificial intelligence (AI) reinforces the central
role of power systems: AI development depends on reliable, affordable, and sustainable electricity
supply [3], while AI-driven data centers are becoming a major source of new electricity demand [4].
Operating power systems requires sequential decision-making under uncertainty while satisfying
strict physical, operational, and security constraints [ 5, 6]. This structure makes power system
∗Corresponding author:dawei.qiu@ntu.edu.sg. †These authors contributed equally. ‡Co-supervisors.
Preprint.
arXiv:2609.36052v1  [cs.AI]  28 Sep 2026

operation a natural domain formulated as a constrained Markov decision process (CMDP) to study
reinforcement learning (RL) algorithms. As national critical infrastructure, the power system is one
of the most complex and safety-critical physical systems, where operational failures can disrupt
economic activity and public services [7, 8]. System operators must continuously balance supply and
demand, manage constrained power flows, maintain voltage and power quality, coordinate DERs, and
ensure the reliable operation of local microgrids [9].
On the other hand, applying RL to power system operation remains challenging from both modeling
and computational perspectives. Specifically, power systems rely on different physical approximations
and optimization formulations, ranging from DC optimal power flow (DC OPF) in transmission
networks to AC optimal power flow (AC OPF) in distribution networks and device-level DER
coordination at the grid edge. These differences motivate benchmarks that preserve task-specific
power system physics while providing a consistent interface and standardized evaluation protocol for
RL algorithms. Beyond these domain-specific challenges, existing power system RL environments
are often limited by their computational structure. Most environments run power flow calculations
and system dynamics through CPU-based simulators, while RL policies are commonly trained on
GPUs. This separation makes large-scale training inefficient: rollouts are constrained by CPU
simulation speed, and repeated CPU-GPU communication introduces additional overhead. As a
result, evaluation over tremendous conditions, random seeds and trajectories will strongly delay the
procedure of developing RL algorithms for real-world power system applications.
To mitigate this issue, we aim to develop a more efficient benchmark for evaluating RL algorithms in
power system operation. Inspired by the recent proliferation of JAX-based RL environments [10, 11],
we introduce PowerZooJax, a novel power system RL benchmark fully implemented in JAX [12], so
it enables compiled and vectorized rollouts completely on GPUs. This design reduces the CPU-GPU
communication overhead present in many existing power system RL benchmarks [13–15].
The main contributions of this work are threefold. First, we present a unified benchmark scope that
covers five major tasks in daily power system operation, enabling RL algorithms to be evaluated
across the entire power system decision-making problems. Second, we formulate these operational
problems under a consistent CMDP interface, enabling systematic comparison of RL algorithms
across five tasks with different physical models, operational constraints, and objectives. Third, we
provide JAX-based benchmark environments, baseline RL algorithms, and evaluation metrics that
support scalable and reproducible assessment of RL-based power system control methods.
2 Related Work
Power System RL Benchmarks.Existing power system RL benchmarks cover different parts
of the power grid. For grid operation, MAPDN [ 16] studies voltage control, ANDES-Gym [ 17]
supports dynamic power system simulation, PowerGridworld [ 18] examines distribution system
control, and RL2Grid [15] and its multi-agent extension MARL2Grid-TR [19] target transmission
topology and redispatching control. At the end-use DER level, CityLearn v2 [20], GridLearn [21],
and SustainGym [14] provide environments for flexible consumption, building energy management,
demand response, and grid-interactive energy communities. At the microgrid level, pymgrid [ 22]
and CommonPower [23] focus on local generation, storage, and load scheduling. Collectively, these
benchmarks demonstrate that power systems provide realistic sequential decision-making problems
with uncertainty, physical constraints, and operational objectives.
However, most existing benchmarks focus on a specific operational task. Many also rely on CPU-
based solvers, making large-scale parallel rollouts costly: MARL2Grid-TR, for example, reports
roughly 120,000 CPU hours to train and evaluate its baselines. In addition, they often lack stan-
dardized task protocols, violation accounting, and evaluation records, which makes cross-layer
comparison and independent verification difficult. PowerZooJax addresses these limitations through
a JAX-based architecture that provides physically grounded tasks across generation, transmission,
distribution, end-use DER coordination, and microgrid operation. It further offers fixed task protocols,
user-defined reward functions and safety costs, and reproducible evaluation records for scalable and
standardized RL evaluation.
JAX-based RL Benchmarks.Recent years have seen a growing number of RL benchmarks imple-
mented in JAX, motivated by the need for fast, vectorized, and accelerator-compatible environment
simulation. Brax [ 24] is an early and influential JAX-based benchmark for physics-based RL,
2

demonstrating the benefits of differentiable and massively parallel simulation. Gymnax [10] further
re-implements classic Gym control tasks in JAX, providing lightweight environments for benchmark-
ing RL algorithms. Jumanji [25] extends this direction to combinatorial optimization and structured
decision-making problems, while Pgx [26] focuses on classic board games.
Beyond single-agent RL, JAX-based benchmarks have also been developed for multi-agent and long-
horizon settings. JaxMARL [11] re-implements a collection of popular multi-agent RL environments
in JAX, enabling accelerated simulation for MARL research. More recently, Craftax [27] builds on
ideas from MiniHack and Crafter to provide a fast grid-world benchmark for studying long-horizon
exploration and generalization of RL algorithms. Octax [28] re-implements a suite of CHIP-8 games
in JAX for benchmarking different aspects of capabilities of RL algorithms.
PowerZooJax belongs to this growing family of JAX-based RL benchmarks, but targets a distinct
and underrepresented domain: real-world power system operation. Unlike existing JAX benchmarks
that primarily focus on classic control, combinatorial optimization, or games, PowerZooJax provides
tasks grounded in practical power system operation while exposing core RL challenges such as
partial observability, mixed action spaces, heterogeneous agents, long-horizon scheduling, and
multi-objective control. In this sense, PowerZooJax complements existing JAX-based benchmarks by
extending accelerator-compatible RL evaluation to large-scale, safety-critical power system operation.
3 Background and Problem Setting
The daily operation of a modern power system can be decomposed into five tasks, as illustrated in
Figure 2: generation, transmission, distribution, end-use DER, and data center microgrid. These tasks
span dispatching conventional and renewable generation resources to meet time-varying demand,
operating the high-voltage transmission network via DC OPF, operating the lower-voltage distribution
network via AC OPF, coordinating user-side DER flexibility, and managing local generation, battery
storage, backup resources, and critical loads in a data center microgrid.
Wind farms
Solar farms
Power plants
Transformer
Transmission network
Substation
Renewable
Storage
Charging station
Flexible load
Generation Transmission network End-use DERDistribution network Data center microgrid
Switch
Local
generator
Data center
Back-up
generator
Storage
Figure 2: Overview of a modern power system model spanning generation, transmission, distribution,
end-use DERs, and a data center microgrid.
Despite their different physical scales and modeling details, these five tasks share a common sequential
decision-making structure under uncertainties and safety constraints, which can be formulated as
constrained Markov decision processes (CMDPs) [29]. At each step, the system state may include:
demand, renewable availability, generator status, network conditions, voltage profiles, storage states
of charge, and microgrid operating modes. Each agent’s observation space is varied among different
tasks. Agents select actions from task-specific action spaces, such as generation dispatch, power
flow control, DER scheduling, storage charging or discharging, and data center workload scheduling.
The system then evolves according to the physical power flow dynamics, device constraints, and
stochastic exogenous factors (e.g. load variation and renewable uncertainty). Reward functions are
designed by encoding operational objectives, including cost minimization, carbon reduction, and
service continuity, while safety costs capture constraint violations such as power imbalance, voltage
violations, and line overloads. The following five paragraphs provide an overview of the CMDP
formulation for each task; the formal CMDP tuple, notation, and full details on state and action spaces,
transition dynamics, reward functions, and safety costs are deferred to Appendix A and Appendix C.
GenCos (Generation Companies) — competitive market bidding.Five generation companies bid
into the wholesale electricity market on the IEEE 5-bus transmission network case5 over a 24-hour
3

horizon at 30-minute resolution, using Great Britain (GB) demand profiles2. Each agent operating
a generation company observes its own generation status and public market price signals, submits
a piecewise-linear bid curve, and receives realized profit as the reward after security constrained
economic dispatch (SCED)-based market clearing. Thermal line overloads are recorded as the safety
cost. This is a competitive multi-agent RL task with partial observability and strategic interactions.
TSO (Transmission System Operator) — transmission unit commitment.A transmission system
operator commits and dispatches 54 generators on the IEEE 118-bus transmission network case118
using GB demand profiles over a 24-hour horizon at 30-minute resolution. The task enforces ramping
limit, minimum up/down-time, and DC OPF feasibility constraints at each step. The transmission
system operator agent observes the full system state and receives negative operating cost as the
reward, while thermal line overloads and reserve shortfalls are recorded as two separate safety costs.
This is a single-agent RL task with a large mixed continuous-binary action space.
DSO (Distribution System Operator) — distribution demand response.A distribution system
operator coordinates six flexible loads on the IEEE 33-bus distribution network case33bw, using
real Ausgrid distribution demand profiles 3 over a 24-hour horizon at 30-minute resolution. The
distribution system operator agent observes the full system state, including bus voltages, branch flows,
nodal demands, and deferred load-shifting buffers, and selects curtailment and load-shifting fractions
for each controllable load. The reward is negative network loss, while voltage limit violations are
recorded as the safety cost. This is a single-agent RL task for distribution-level demand response and
voltage-aware load coordination.
DERs (Distributed Energy Resources) — cooperative DER coordination.Twelve DERs, including
four batteries, four PV inverters 4, and four flexible loads, are placed at fixed buses of the 141-
bus distribution network case141. Each distributed energy resource agent observes its own bus
voltage, the voltages of its electrically connected neighboring buses, a compact system-wide voltage
summary, and its local device state. Each agent takes a 2-dimensional device-specific action, such as
active/reactive power control for batteries, curtailment/reactive power control for PV inverters, and
curtailment/load shifting for flexible loads. All agents share a negative network loss reward, while
voltage, thermal, and device feasibility violations are recorded as three separate safety costs. This is a
cooperative multi-agent RL task with heterogeneous agents and local observations.
DCMG (Data Center Microgrid) — long-horizon multi-objective scheduling.A data center
microgrid powers an AI data center using on-site PV , battery storage, a diesel generator, and a
connection to the main grid. A microgrid agent controls the system over 288 five-minute steps using
real Google workload traces [30], jointly scheduling training and fine-tuning jobs, cooling, battery
operation, diesel generation, and grid interaction based on workload, thermal, and energy states.
Under normal conditions, the microgrid can operate in grid-connected mode; during disturbances or
outages, it can switch to islanded mode to maintain critical load service. The reward combines energy
use, operating cost, and carbon emissions, while power imbalance, server-zone over-temperature, and
workload incompletion are recorded as three separate safety costs. This is a single-agent RL task for
long-horizon, multi-objective scheduling of critical computing infrastructure.
4 Power System Problem, RL Challenge and Evaluation Scope
From the perspective of RL, the five tasks can be viewed as either single-agent RL or multi-agent RL
problems. This leads to one of our aims in proposing PowerZooJax: to reflect how RL techniques can
address the emergent real-world problems, while providing a clean, unified testbed for AI researchers
to easily pinpoint the key challenges of RL problems. Each task is grounded in a realistic operational
setting, but is also designed to highlight a distinct RL challenge, such as partial observability, mixed
action spaces, heterogeneous agents, long-horizon scheduling, or multi-objective control.
Table 1 summarizes the interrelationship between power system problems embedded in the tasks
we defined and the corresponding RL challenges in the modern RL literature. We categorize the
tasks into centralized and decentralized settings according to their operational roles. Centralized
tasks correspond to decisions that are typically executed by system operators to maintain secure and
2https://www.neso.energy/data-portal/historic-demand-dataNational Energy System Operator (NESO).
3https://www.ausgrid.com.au/Industry/Our-Research/Data-to-share/, Ausgrid.
4https://bmrs.elexon.co.uk/generation-by-fuel-type, Elexon.
4

reliable network operation, while decentralized tasks correspond to settings in which multiple users,
assets, or market participants make individual decisions based on local information.
From the perspective of RL evaluation, Table 1 clearly captures the basic assumptions of popular
RL problems for each task. As a result, researchers can confidently get the information about
what features of their algorithms (RL challenges) are expected to be meaningfully assessed. More
importantly, due to that our benchmark tasks follow the practical settings of power system problems,
algorithms that work well on our benchmark can be explained as possessing the potential to handle
real-world problems. This is what most of previous benchmarks that focused on either games or
simplified grid-world settings lack.
Table 1: Interrelationship between power system problems and RL challenges.
Tasks Power System Problems RL Challenges
GenCos Decentralizedelectricity market bidding with a 3-
dim action space and a 12-dim observation space.
Multi-agent RLwith partial observability (each
agent’s local information).
TSO Centralizedunit commitment with a 108-dim ac-
tion space and a 410-dim observation space.
Single-agent RLwith a large, mixed action
space of continuous and binary variables.
DSO Centralizedcontrol of flexible loads with a 12-dim
action space and a 195-dim observation space.
Single-agent RLwith an easy-to-start setup to
verify initial design ideas.
DERs Decentralizedcontrol of three types of DERs (bat-
tery, PV , flexible loads) with a 2-dim action space
and a 15-dim observation space.
Multi-agent RLwith partial observability (each
agent’s local and neighbor information) and het-
erogeneous agents.
DCMG Centralizedlong-horizon scheduling with a 5-dim
action space and a 24-dim observation space.
Single-agent RLwith a long-horizon sequential
decision making process and multi-objectives.
Note:“dim” is short for dimensional.
5 How Does PowerZooJax Work?
Each of the five tasks in Section 3 runs a power flow (PF) or optimal power flow (OPF) computation at
every environment step. DSO and DERs use radial AC PF, TSO and GenCos rely on DC OPF clearing,
and DCMG combines local power-balance checks with device dynamics. These computations involve
fixed-shape numerical operations, such as matrix updates, constraint evaluation, and batched linear-
algebra routines, which are well suited to compilation and fusion by accelerated linear algebra (XLA).
Conventional pipelines typically write them as host-side Python loops that traverse a feeder tree or
call a CPU solver for a linear program, incurring a host round trip at every step [31]. In contrast, our
PowerZooJax rewrites each iteration as a fixed-shape JAX computation graph and runs the full rollout,
including batched parallel scenarios, inside a compiled accelerator program, as shown in Figure 1.
This design enables PowerZooJax to keep the whole training loop on the GPU. From episode reset,
through transitions, rewards, safety costs, action sampling, and gradient updates, the main computation
operates on GPU-resident arrays. Episode boundaries do not require returning to a Python control
loop: when one episode terminates, the next reset can be executed as the next operation in the same
compiled JAX program. As a result, PowerZooJax avoids per-step CPU-GPU synchronization during
rollout generation, reducing overhead and enabling efficient large-scale parallel training.
5.1 Rewriting Power Flow as a JAX Computation Graph
A traditional radial PF solver, e.g. as implemented in pandapower [ 32], is a host-side fixed-point
iteration. At each iteration k, the solver walks the feeder tree backward to aggregate downstream
loads into branch flows P(k),Q (k), walks it forward to update bus voltages v2,(k), and checks
convergence condition maxn |v2,(k) n −v 2,(k−1) n |< ε inside a Python while loop. Since both sweeps
and the convergence test are controlled on the host, each RL environment step incurs host-side control
overhead and potentially a device-host synchronization. PowerZooJax rewrites the same iterative
procedure as a fixed-shape JAX computation graph through three structural changes. In each change
below, the expression on the left of → denotes the traditional implementation pattern, while the
expression on the right denotes the PowerZooJax replacement.
5

Tree walking → dense matrix-vector products.In a radial network, the backward and forward
sweeps can be represented using fixed topology matrices. PowerZooJax precomputes two such
matrices at environment construction time: a downstream-aggregation matrix D∈R Nℓ×N , where N
and Nℓ are the numbers of buses and branches and Dℓ,n = 1 if bus n is downstream of line ℓ, and a
path matrix Π∈R N×N ℓ, where Πn,ℓ = 1 if line ℓ lies on the unique path from the slack bus to busn.
The backward sweep then becomes a matrix-vector multiplication that aggregates downstream active
and reactive loads into branch flows, while the forward sweep becomes a matrix-vector multiplication
that accumulates voltage drops along each root-to-bus path. One PF iteration can therefore be written
as
P(k) =D  pload +p loss,(k−1) ,
v2,(k) =V 2 slack 1−Πδ 2,(k), (1)
with Q(k) computed analogously. Here, pload is the vector of nodal active loads, ploss,(k−1) is the
per-bus loss correction recomputed from the previous iterate, and δ2,(k) denotes the per-line squared-
voltage drop computed from (P(k),Q (k),v 2,(k−1)) using the standard DistFlow recurrence [ 33].
Since D and Π depend only on the network topology, they are precomputed once and reused
throughout training. This replaces explicit feeder-tree traversal with fixed-shape matrix-vector
products that are directly compatible with JAX compilation and batching.
Python while→jax.lax.while_loop .Equation (1) defines a fixed-point iteration body f:
(P,Q,v 2)7→(P ′,Q ′,v ′2), whose output depends only on its input arrays. In PowerZooJax, this
body is implemented entirely with jnp and lax operations, without host-side mutation or external
state updates. JAX therefore traces the iteration body once into a static XLA computation graph and
runs the fixed-point loop with jax.lax.while_loop, replacing the host-controlled Python while
loop with a device-side loop that can be compiled, fused, and batched across parallel environments.
Per-step solver call → batched PF rollout via jax.vmap/jax.lax.scan.Once the radial PF itera-
tion is written as fixed-shape matrix operations and a device-side lax.while_loop, PowerZooJax
can evaluate many PF solves without launching a separate solver at every environment step. The
precomputed topology matrices D and Π are shared across batched scenarios, so the same PF kernel
is applied in parallel over a leading batch dimension with vmap. Across time, lax.scan composes
the per-step PF solve with device updates, rewards, and safety-cost calculations, producing a single
compiled rollout for an entire RL episode. In our tasks, this means that the 48 PF evaluations required
by one DSO or DERs episode are executed as part of one accelerator-resident computation graph,
rather than as repeated Python calls to an external solver.
5.2 Optimal Power Flow as a Computation Graph
The same computation-graph principle applies to OPF kernels. We illustrate this with DC OPF,
which is used by the TSO and GenCos tasks. DC OPF is a linear program that minimizes generation
cost subject to system-wide power balance, generator capacity bounds, and transmission line-flow
limits. In a conventional pipeline, this linear program is passed to an external CPU solver once per
environment step, making the OPF solve a host-side bottleneck. PowerZooJax instead implements
OPF solvers directly inside the JAX graph: an ADMM [ 34] solver for TSO’s DC OPF, and a
PDIPM [35] solver for GenCos market clearing. For example, one iteration of the ADMM DC OPF
solver can be written as p(k+1)
ν(k+1) eq

=A −1 aug

r(k)
1⊤pd

,
z(k+1) 1 = clip  p(k+1) +y (k) 1 /ρ,p , p  , (2)
where p is the generator dispatch vector with output bounds (p, p), pd is the nodal demand vector,
νeq is the multiplier on the system-wide power-balance equality, z1 and y1 are the ADMM auxiliary
and dual variables associated with the generator bounds, ρ >0 is the ADMM penalty parameter,
and r(k) is the residual vector assembled from the current auxiliary and dual iterates. The projection
step for the line-flow auxiliary variable z2 and the dual updates for y1,y 2 complete one iteration
(Appendix B.2, Equation (15)). The augmented KKT matrix Aaug depends only on grid parameters
and does not change with the per-step load, so its inverse is precomputed once at setup, similar to
the topology matrices D and Π used in the PF kernel. Each ADMM iteration is then reduced to
fixed-shape matrix operations and elementwise projections, making the iteration body fully traceable
6

by JAX. The complete OPF solve is executed as a fixed-length lax.fori_loop, so batched OPF
solves can be compiled and run on GPU device without repeated calls to an external CPU solver.
6 Evaluation
We evaluate PowerZooJax on the five benchmark tasks introduced in Section 3. Section 6.1 first evalu-
ates the computational efficiency of the JAX-based implementation described in Section 5, measuring
wall-clock speedups under matched training budgets. Sections 6.2–6.4 then present representative
task-level results for GenCos, TSO, and DCMG, including training returns, safety violations, compar-
isons with task-specific baselines, and performance on out-of-distribution (OOD) splits. Analogous
results for DSO and DERs follow the same protocol and are reported in Appendix G.3–G.4.
Hardware.All experiments are run on a single workstation equipped with an NVIDIA RTX 4500
Ada (24 GB) GPU and an AMD Ryzen Threadripper PRO 7985WX host with 256 GB of RAM.
Evaluation Setup.We evaluate each task with 5 random seeds. Training budgets are task-specific:
5M environment steps for GenCos, 20M for TSO, 3M for DSO, 10M for DERs, and 1M for DCMG.
We use PPO [36] for the single-agent tasks (TSO, DSO, and DCMG), and IPPO [37] for the multi-
agent tasks (GenCos and DERs). DCMG is additionally trained with SAC [38] for the representative
episode in Section 6.4. After training, each seed is evaluated on a held-out split, with task-specific
OOD stress splits when applicable. For each seed, results are averaged over 10–50 evaluation episodes
depending on the task, and final results are reported as mean values with 95% CIs across seeds. Full
hyperparameters and network architectures are in Appendix F.
6.1 Execution Speed and Scaling Performance
We compare three training backends on the five benchmark tasks: (i) PowerZooJax, which runs
both the environment simulation and policy training in JAX on the GPU; (ii) Stable-Baselines3
(SB3) [39], which uses PowerZooPy 5, our CPU-based Python implementation of the same tasks,
for environment simulation and trains a PyTorch policy on the GPU; and (iii) SBX [ 40], the JAX
port of SB3, which trains a JAX policy on the GPU while using the same CPU-based PowerZooPy
environment simulation.
0 1m
50K
100KReturn
4h 6h 0 1h 2h 3h
-500
-250
TSO
0 30s
-0.6
-0.45
30m 1.5h 0 1m
-0.88
-0.8
-0.72
12h16h 0 1m 2m 3m 4m
-6K
-4K
-2K
DCMG
20 24 28 212
100
10KSteps per Sec.
20 24 28 212
100
1K
10K
20 24 28 212
1K
100K
20 24 28 212
1K
100K
20 24 28 212
100
10K
GenCos DSO DERs
Wall-clock time
# of Environments
PowerZooJax (env: JAX-GPU, RL: JAX-GPU) SBX (env: CPU, RL: JAX-GPU) SB3 (env: CPU, RL: PyT orch-GPU)
Figure 3: Cross-backend speed for five benchmark tasks. Top: wall-clock training time under matched
budgets. Bottom: environment throughput with increasing parallelism, shown on log–log axes.
Wall-clock and Throughput.Figure 3 evaluates speed from two perspectives. The wall-clock
measures how long each backend takes to finish the same training budget for each task, including
episode resets, periodic evaluations, and gradient updates. The throughput measures how many
environment steps each backend can generate per second as the number of parallel environments
increases from 20 to 212. Table 2 reports the final wall-clock time and the throughput at 212 parallel
environments, and the corresponding speedup of PowerZooJax over the CPU-based baselines.
Speedup vs Per-step Cost.The largest gains occur when CPU baselines perform solver-heavy
work. GenCos and DERs call CPU-based OPF or PF routines in the CPU implementations, while
5https://github.com/powerzoojax/PowerZooPy, the companion object-oriented Python implementation.
7

Table 2: Cross-backend speed per benchmark task for three training backends.
Wall-clock to matched budget (s) Throughput at2 12 envs (steps/s)
Task BudgetN envs PowerZooJax SBX SB3 speedup PowerZooJax SBX SB3 speedup
GenCos 5M 256 67 9,602 10,868 161×506,134 442 244 2,077×
TSO 20M 256 515 10,799 10,801 21×53,724 1,649 411 131×
DSO 3M 128 32 1,667 3,801 117×134,660 3,435 2,207 61×
DERs 10M 128 79 61,883 59,778 780×414,506 203 233 2,040×
DCMG 1M 64 33 221 257 8×25,132 1,167 1,298 22×
PowerZooJax executes these kernels inside the compiled JAX graph, yielding throughput speedups
above 2,000×. TSO and DSO implemented in JAX also benefit substantially from moving power
system computation onto the GPU. DCMG has the smallest speedup because its transitions are mostly
arithmetic device updates without an external solver call, so the CPU baseline is already fast.
6.2 GenCos: Bidding under Partial Observability
Figure 4 evaluates GenCos under four bidding strategies and three evaluation splits. The two extreme
baselines define the strategic range: Truthful bidding at marginal cost achieves a daily profit of
£6.9k/day, while Max-markup bidding at the maximum allowed price achieves £598k/day. Uniform-
mid, which uses an intermediate markup between Truthful and Max-markup bidding, achieves
£303k/day. IPPO learns a more profitable strategy than Uniform-mid, reaching £395k/day on the
in-distribution split, while remaining below the Max-markup upper baseline. The same ordering is
preserved under the two OOD stress splits: high demand, which increases load by 10%, and low
renewable, which decreases wind generation by 5%. The learned strategy also produces distinct
locational marginal prices (LMPs). When system load exceeds 800 MW, Max-markup clears at an
LMP near £75/MWh, Uniform-mid near £50/MWh, and IPPO around £45/MWh, indicating that
IPPO learns to increase market profit while avoiding the most aggressive markup strategy.
In-distribution High
demand
Low
renewable
0
250
500
750Daily profit (£k)
(a) Profit per strategy and split
400 600 800 1000
System load (MW)
0
25
50
75LMP (£/MWh)
(b) LMP vs load (in-distribution episode)
Strategy
Truthful
Uniform-mid
IPPO
Max-markup
Figure 4: Generation company profit and market clearing price on case5. (a) Total daily profit
for each strategy and evaluation split. (b) Locational marginal price (LMP) vs system load on a
representative evaluation. Error bars in (a) show 95% CIs across 5 seeds.
6.3 TSO: Economic–Safety Cost Trade-off
Figure 5 shows the economic–safety cost trade-off for transmission operation. The merit-order
baseline, which commits generators from cheapest to most expensive until capacity covers demand
plus a 5% reserve margin, while ignoring thermal line limits, achieves an operating cost of £2.89M/day.
The all-on baseline keeps every generator online, improving safety but increasing cost to £4.34M/day.
PPO, trained with negative operating cost as the reward, reduces to £1.58M/day but violates thermal
line limits in 36% and reserve margins in 7% over all evaluations. PPO-Lagrangian [ 41], which
applies adaptive penalties to each violation type, eliminates reserve shortfalls and reduces the thermal
overload rate to 6%, at a higher cost of £3.50M/day. The same pattern holds under the two OOD stress
splits: line-tightening, where line ratings are reduced to 85%, and load-stress, where demand is scaled
by 1.15. Under these stresses, PPO reaches thermal overload rates of 49% and 41%, respectively,
while PPO-Lagrangian reduces them to 16% and 9% and maintains zero reserve shortfall. These
results show that the Lagrangian formulation substantially improves safety, fully eliminating reserve
violations on this network, but thermal overloads remain a harder constraint to satisfy under stressed
conditions.
8

6.4 DCMG: Long-Horizon Scheduling for a Data Center
Figure 6 shows a representative 24-hour SAC policy trajectory over 288 five-minute steps. SAC
charges the battery from the grid during the first two hours when electricity prices are low, discharges
the battery through the morning price peak above £100/MWh, recharges during the midday when PV
generation is available, and cycles again through the evening peak. This repeated charge–discharge
pattern indicates that SAC learns to coordinate storage schedules across the full 288-step horizon.
Throughout the episode, the IT workload is served at every step, showing that SAC learns a price-
aware and constraint-respecting scheduling policy directly from the multi-objective reward.
2 3 4 5
Cost (£m/day)
0
25
50Overload rate (%)
(a) Cost vs thermal overload
2 3 4 5
Cost (£m/day)
0
5
10Shortfall rate (%)
(b) Cost vs reserve shortfall Algorithm
PPO
PPO-Lagrangian
Merit-order
All-on
Split
In-distribution
Line-tightening
Load-stress
Figure 5: TSO economic–safety cost trade-off on case118. (a) Operating cost vs thermal overload
rate. (b) Operating cost vs reserve shortfall rate. Error bars show 95% CIs across 5 seeds.
0 6 12 18 24
Time (h)
0.0
0.5
1.0Power (MW)
(a) Power dispatch
0 6 12 18 24
Time (h)
0.0
0.5
1.0Battery SOC
(b) Storage and grid price
0
50
100
Grid price (£/MWh)
Grid import PV Battery discharge Battery charge IT workload Battery SOC Grid price
Figure 6: DCMG daily scheduling on a representative day. (a) Power supply to the IT workload. (b)
Daily battery state of charge (SoC) and grid electricity price.
7 Conclusion
PowerZooJax shows that power system RL benchmarks can simultaneously balance physical modeling
and computational scalability. By integrating training and evaluation into a GPU-accelerated pipeline,
the benchmark supports fast rollouts while retaining operational metrics that matter for real grid
decision making. The five tasks demonstrate how RL algorithms can be evaluated across diverse
power system settings under a common constrained Markov decision process (CMDP) interface, with
standardized reporting of returns, safety costs, and stress-test performance.
Limitations.PowerZooJax is a benchmark suite, not a deployment-ready power system simulator
or controller. Although it covers five representative tasks, the current version is still limited in
grid scale, uncertainty modeling, operational constraints, and task diversity. Finally, the current
environments are built from public or synthetic grid models and public data, and therefore cannot fully
capture the complexity of real power system with real-time operational data. Strong performance
on PowerZooJax should therefore be interpreted as evidence of an algorithm’s ability to address
representative power system RL challenges, not as a guarantee of safe real-world power system
operation.
Future Work.Future work will extend PowerZooJax in three directions. First, we plan to broaden
PowerZooJax with larger grid cases, richer uncertainty models, more realistic constraints, and
additional tasks. Second, we envision PowerZooJax evolving into a more intelligent programming
tool for power system RL. By integrating PowerZooJax with language models, users could specify
power system requirements in natural language, and the tool could automatically generate the
corresponding RL environment, task configuration, reward and safety cost definitions, and baseline
9

algorithms. Third, we aim to collaborate with the power industry to access grid models and operational
data, build digital-twin environments, and study how AI-based control methods can be evaluated and
transferred toward practical power system applications.
Acknowledgement
Dawei Qiu is supported by the Nanyang Technological University (NTU) Start-Up Grant project
#026749-00001 “Market Design for Low-Carbon Power Systems: Towards a Reliable, Affordable,
and Resilient Transition”. Jianhong Wang is supported by the Engineering and Physical Sciences
Research Council (EPSRC) [Grant Ref: EP/Y028732/1].
10

References
[1] Maria Luisa Di Silvestre, Salvatore Favuzza, Eleonora Riva Sanseverino, and Gaetano Zizzo.
How Decarbonization, Digitalization and Decentralization are changing key power infras-
tructures.Renewable and Sustainable Energy Reviews, 93:483–498, October 2018. ISSN
1364-0321.
[2] Goran Strbac, Dimitrios Papadaskalopoulos, Nikolaos Chrysanthopoulos, Ana Estanqueiro,
Hugo Algarvio, Fernando Lopes, Laurens de Vries, German Morales-Espana, Jos Sijm, Ricardo
Hernandez-Serna, Juha Kiviluoma, and Niina Helisto. Decarbonization of Electricity Systems in
Europe: Market Design Challenges.IEEE Power and Energy Magazine, 19(1):53–63, January
2021. ISSN 1540-7977.
[3] Emma Strubell, Ananya Ganesh, and Andrew McCallum. Energy and Policy Considerations for
Deep Learning in NLP. InProceedings of the 57th Annual Meeting of the Association for Com-
putational Linguistics, pages 3645–3650, Florence, Italy, 2019. Association for Computational
Linguistics.
[4] Tianqi Xiao, Francesco Fuso Nerini, H. Damon Matthews, Massimo Tavoni, and Fengqi You.
Environmental impact and net-zero pathways for sustainable artificial intelligence servers in the
USA.Nature Sustainability, 8(12):1541–1553, December 2025. ISSN 2398-9629.
[5] Warren B. Powell and Stephan Meisel. Tutorial on Stochastic Optimization in Energy—Part I:
Modeling and Policies.IEEE Transactions on Power Systems, 31(2):1459–1467, March 2016.
ISSN 0885-8950.
[6] Yonghong Chen, Feng Pan, Feng Qiu, Alinson S Xavier, Tongxin Zheng, Muhammad Marwali,
Bernard Knueven, Yongpei Guan, Peter B. Luh, Lei Wu, Bing Yan, Mikhail A. Bragin, Haiwang
Zhong, Anthony Giacomoni, Ross Baldick, Boris Gisin, Qun Gu, Russ Philbrick, and Fangxing
Li. Security-Constrained Unit Commitment for Electricity Market: Modeling, Solution Methods,
and Future Challenges.IEEE Transactions on Power Systems, 38(5):4668–4681, September
2023. ISSN 0885-8950.
[7] Yang Yang, Takashi Nishikawa, and Adilson E. Motter. Small vulnerable sets determine
large network cascades in power grids.Science, 358(6365):eaan3184, November 2017. ISSN
0036-8075.
[8] Hao Wu, Xiangyi Meng, Michael M. Danziger, Sean P. Cornelius, Hui Tian, and Albert-László
Barabási. Fragmentation of outage clusters during the recovery of power distribution grids.
Nature Communications, 13(1):7372, November 2022. ISSN 2041-1723.
[9] Benjamin Kroposki, Brian Johnson, Yingchen Zhang, Vahan Gevorgian, Paul Denholm, Bri-
Mathias Hodge, and Bryan Hannegan. Achieving a 100% Renewable Grid: Operating Electric
Power Systems with Extremely High Levels of Variable Renewable Energy.IEEE Power and
Energy Magazine, 15(2):61–73, March 2017. ISSN 1540-7977.
[10] Robert Tjarko Lange. Gymnax: A JAX-based reinforcement learning environment library, 2022.
URLhttp://github.com/RobertTLange/gymnax.
[11] Saptarashmi Bandyopadhyay, Jonathan Cook, Christian de Witt, Benjamin Ellis, Jakob Foerster,
Matteo Gallici, Ravi Hammond, Nick Hawes, Garðar Ingvarsson, Minqi Jiang, Akbir Khan,
Bruno Lacerda, Robert Lange, Chris Lu, Andrei Lupu, Tim Rocktäschel, Alexander Rutherford,
Mikayel Samvelyan, Alexandra Souly, Shimon Whiteson, and Timon Willi. JaxMARL: Multi-
Agent RL Environments and Algorithms in JAX. InAdvances in Neural Information Processing
Systems 37, pages 50925–50951, 2024.
[12] James Bradbury, Roy Frostig, Peter Hawkins, Matthew James Johnson, Yash Katariya, Chris
Leary, Dougal Maclaurin, George Necula, Adam Paszke, Jake VanderPlas, Skye Wanderman-
Milne, and Qiao Zhang. JAX: Composable transformations of Python+NumPy programs, 2018.
URLhttp://github.com/jax-ml/jax.
[13] Ting-Han Fan, Xian Yeow Lee, and Yubo Wang. PowerGym: A Reinforcement Learning
Environment for V olt-Var Control in Power Distribution Systems. InProceedings of The 4th
Annual Learning for Dynamics and Control Conference, pages 21–33. PMLR, May 2022.
11

[14] Christopher Yeh, Victor Li, Rajeev Datta, Julio Arroyo, Nicolas Christianson, Chi Zhang, Yize
Chen, Mohammad Mehdi Hosseini, Azarang Golmohammadi, Yuanyuan Shi, Yisong Yue, and
Adam Wierman. SustainGym: Reinforcement Learning Environments for Sustainable Energy
Systems.Advances in Neural Information Processing Systems, 36:59464–59476, December
2023.
[15] Enrico Marchesini, Benjamin Donnot, Constance Crozier, Ian Dytham, Christian Merz, Lars
Schewe, Nico Westerbeck, Cathy Wu, Antoine Marot, and Priya L. Donti. RL2Grid: Bench-
marking Reinforcement Learning in Power Grid Operations, March 2025.
[16] Jianhong Wang, Wangkun Xu, Yunjie Gu, Wenbin Song, and Tim C Green. Multi-agent
reinforcement learning for active voltage control on power distribution networks.Advances in
neural information processing systems, 34:3271–3284, 2021.
[17] Hantao Cui and Yichen Zhang. Andes_gym: A Versatile Environment for Deep Reinforcement
Learning in Power Systems. In2022 IEEE Power & Energy Society General Meeting (PESGM),
pages 01–05, July 2022.
[18] David Biagioni, Xiangyu Zhang, Dylan Wald, Deepthi Vaidhynathan, Rohit Chintala, Jennifer
King, and Ahmed S. Zamzam. PowerGridworld. InProceedings of the Thirteenth ACM
International Conference on Future Energy Systems, E-Energy ’22, pages 565–570, New York,
NY , USA, June 2022. Association for Computing Machinery. ISBN 978-1-4503-9397-3.
[19] Enrico Marchesini, Eva Boguslawski, Alessandro Leite, Christopher Amato, Matthieu Dussartre,
Marc Schoenauer, Benjamin Donnot, and Priya L. Donti. MARL2Grid-TR: A Multi-Agent RL
Benchmark in Power Grid Operations. InThe Fourteenth International Conference on Learning
Representations, January 2026.
[20] Kingsley Nweye, Kathryn Kaspar, Giacomo Buscemi, Giuseppe Pinto, Han Li, Tianzhen
Hong, Mohamed Ouf, Alfonso Capozzoli, and Zoltan Nagy. CityLearn v2: An OpenAI
Gym environment for demand response control benchmarking in grid-interactive communities.
InProceedings of the 10th ACM International Conference on Systems for Energy-Efficient
Buildings, Cities, and Transportation, BuildSys ’23, pages 274–275, New York, NY , USA,
November 2023. Association for Computing Machinery. ISBN 979-8-4007-0230-3.
[21] Aisling Pigott, Constance Crozier, Kyri Baker, and Zoltan Nagy. GridLearn: Multiagent
reinforcement learning for grid-aware building energy management.Electric Power Systems
Research, 213:108521, December 2022. ISSN 0378-7796.
[22] Gonzague Henri, Tanguy Levent, Avishai Halev, Reda Alami, and Philippe Cordier. Pymgrid:
An Open-Source Python Microgrid Simulator for Applied Artificial Intelligence Research,
November 2020.
[23] Michael Eichelbeck, Hannah Markgraf, and Matthias Althoff. CommonPower: A Framework
for Safe Data-Driven Smart Grid Control.IEEE Transactions on Smart Grid, pages 1–1, 2025.
ISSN 1949-3053.
[24] C. Daniel Freeman, Erik Frey, Anton Raichuk, Sertan Girgin, Igor Mordatch, and Olivier
Bachem. Brax - a differentiable physics engine for large scale rigid body simulation, 2021.
URLhttp://github.com/google/brax.
[25] Clément Bonnet, Daniel Luo, Donal Byrne, Shikha Surana, Sasha Abramowitz, Paul Duckworth,
Vincent Coyette, Laurence I. Midgley, Elshadai Tegegn, Tristan Kalloniatis, Omayma Mahjoub,
Matthew Macfarlane, Andries P. Smit, Nathan Grinsztajn, Raphael Boige, Cemlyn N. Waters,
Mohamed A. Mimouni, Ulrich A. Mbou Sob, Ruan de Kock, Siddarth Singh, Daniel Furelos-
Blanco, Victor Le, Arnu Pretorius, and Alexandre Laterre. Jumanji: A diverse suite of scalable
reinforcement learning environments in JAX, 2024.
[26] Sotetsu Koyamada, Shinri Okano, Soichiro Nishimori, Yu Murata, Keigo Habara, Haruka
Kita, and Shin Ishii. Pgx: Hardware-Accelerated Parallel Game Simulators for Reinforcement
Learning. InAdvances in Neural Information Processing Systems 36, volume 36, pages 45716–
45743, 2023.
12

[27] Michael Matthews, Michael Beukman, Benjamin Ellis, Mikayel Samvelyan, Matthew Jackson,
Samuel Coward, and Jakob Foerster. Craftax: A Lightning-Fast Benchmark for Open-Ended
Reinforcement Learning. InProceedings of the 41st International Conference on Machine
Learning, volume 235, 2024.
[28] Waris Radji, Thomas Michel, and Hector Piteau. Octax: Accelerated CHIP-8 arcade environ-
ments for reinforcement learning in JAX, 2025.
[29] Xin Chen, Guannan Qu, Yujie Tang, Steven Low, and Na Li. Reinforcement Learning for
Selective Key Applications in Power Systems: Recent Advances and Future Challenges.IEEE
Transactions on Smart Grid, 13(4):2935–2958, July 2022. ISSN 1949-3053.
[30] Google/cluster-data. Google, 2019. URLhttps://github.com/google/cluster-data.
[31] Antoine Marot, Benjamin Donnot, Gabriel Dulac-Arnold, Adrian Kelly, Aïdan O’Sullivan, Jan
Viebahn, Mariette Awad, and Isabelle Guyon. Learning to run a Power Network Challenge: A
Retrospective Analysis, March 2021.
[32] Leon Thurner, Alexander Scheidler, Florian Schafer, Jan-Hendrik Menke, Julian Dollichon,
Friederike Meier, Steffen Meinecke, and Martin Braun. Pandapower—An Open-Source Python
Tool for Convenient Modeling, Analysis, and Optimization of Electric Power Systems.IEEE
Transactions on Power Systems, 33(6):6510–6521, November 2018. ISSN 0885-8950.
[33] M.E. Baran and F.F. Wu. Network reconfiguration in distribution systems for loss reduction
and load balancing.IEEE Transactions on Power Delivery, 4(2):1401–1407, April 1989. ISSN
0885-8977.
[34] Tomaso Erseghe. Distributed Optimal Power Flow Using ADMM.IEEE Transactions on Power
Systems, 29(5):2370–2380, September 2014. ISSN 0885-8950.
[35] Hongye Wang, Carlos E. Murillo-Sanchez, Ray D. Zimmerman, Robert J. Thomas, and Hongye
Wang. On Computational Issues of Market-Based Optimal Power Flow.IEEE Transactions on
Power Systems, 22(3):1185–1193, August 2007. ISSN 0885-8950.
[36] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal
Policy Optimization Algorithms, August 2017.
[37] Christian Schroeder de Witt, Tarun Gupta, Denys Makoviichuk, Viktor Makoviychuk, Philip
H. S. Torr, Mingfei Sun, and Shimon Whiteson. Is Independent Learning All You Need in the
StarCraft Multi-Agent Challenge?, November 2020.
[38] Tuomas Haarnoja, Aurick Zhou, Kristian Hartikainen, George Tucker, Sehoon Ha, Jie Tan,
Vikash Kumar, Henry Zhu, Abhishek Gupta, Pieter Abbeel, and Sergey Levine. Soft Actor-Critic
Algorithms and Applications, December 2018.
[39] Antonin Raffin, Ashley Hill, Adam Gleave, Anssi Kanervisto, Maximilian Ernestus, and Noah
Dormann. Stable-baselines3: Reliable reinforcement learning implementations.Journal of
Machine Learning Research, 22(268):1–8, 2021.
[40] Antonin Raffin. Stable Baselines Jax, April 2026. URL https://github.com/araffin/sbx.
[41] Alex Ray, Joshua Achiam, and Dario Amodei. Benchmarking safe exploration in deep rein-
forcement learning. 7(1):2, 2019.
[42] Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel. Constrained Policy Optimization,
May 2017.
[43] Aivar Sootla, Alexander I. Cowen-Rivers, Taher Jafferjee, Ziyan Wang, David Mguni, Jun
Wang, and Haitham Bou-Ammar. Saute RL: Almost Surely Safe Reinforcement Learning Using
State Augmentation, February 2022.
13

Appendix
This supplementary material is organized as follows. Section A formalizes the CMDP tuple shared
by all five tasks and fixes notation. Section B gives the physical-model derivations (radial AC
power flow, DC OPF with ADMM, bid-based market clearing with PDIPM, and the device plus
microgrid couplings). Section C gives the per-task observation, action, reward, and cost equations.
Section D documents external data sources and the split and stress-test taxonomy. Section E provides
a quickstart with install, a minimal Python rollout, configuration excerpts, and CLI commands.
Section F lists algorithm choices, hyperparameters, network architectures, and evaluation protocol.
Section G reports the per-task supplementary tables and figures. Section H reports execution scaling
and the backend comparison.
A Constrained Markov Decision Process Formulation
This section gives the formal constrained Markov decision process (CMDP) tuple shared by all five
tasks, the two constraint forms used in the benchmark (discounted expected cost and zero-violation
constraint), and the Lagrangian formulation used by the safe-RL baselines. The notation used
throughout the appendix is fixed in Table 3 (Section A.5).
A.1 The CMDP tuple
Each task is an episodic CMDP [29, 42]
M=

S,A, P, r,c, γ,b, ρ 0, T

,(3)
where S and A are the state and action spaces, P:S × A →∆(S) is the transition kernel,
r:S × A →Ris the scalar reward, c= (c 1, . . . , ck) :S × A →Rk is the cost vector, γ∈(0,1] is
the discount factor, b∈R k ≥0 is the constraint-threshold vector, ρ0 is the initial-state distribution, and
T is the episode horizon (Table 5 lists per-task T ). Reward and cost are produced as separate outputs
by every task environment so that safety violations cannot be silently absorbed into the scalar return;
the cost-vector order is fixed by the declared constraint names of each task. In the multi-agent tasks
(GenCos and DERs), each agent observes only a projection of the state (Section C), so these tasks are
constrained partially observable problems.
For a stationary policyπ:S →∆(A), define the reward and cost values
Jr(π) =E π
hPT−1
t=0 γt r(st, at) i ,(4)
Jci (π) =E π
hPT−1
t=0 γt ci(st, at) i , i= 1, . . . , k.(5)
A.2 Constraint forms used in the suite
PowerZooJax tasks use one of two constraint forms.Form 1 (budgeted expected cost)is applied
to the DSO voltage channel, the three DERs channels (voltage, thermal, resource), and the three
DCMG channels (workload incompletion, server-zone over-temperature, power imbalance), as well
as the TSO Lagrangian baselines.Form 2 (zero-violation constraint)is applied to the TSO reserve-
shortfall and thermal-overload channels reported in Table 11. The single GenCos thermal-overload
channel is reported as a market-side diagnostic only.
Form 1 (discounted expected-cost budget).
max
π
Jr(π)s.t.J ci (π)≤b i, i= 1, . . . , k.(6)
Used by DSO, DERs, and TSO Lagrangian baselines, where the bi are operational risk budgets per
episode.
Form 2 (zero-violation constraint).
max
π
Jr(π)s.t.P π

ci(st, at)>0

= 0,∀t,∀i∈I hard.(7)
Used for the TSO reserve-shortfall and thermal-overload channels: a policy satisfies Form 2 only if
both channels record zero cost at every step, so cost cannot be traded for safety. The TSO results in
Section G.2 are reported under this form.
14

A.3 Lagrangian formulation
For Form 1 with multipliersλ∈R k ≥0, the Lagrangian
L(π,λ) =J r(π)−λ ⊤ Jc(π)−b  (8)
gives the saddle-point reformulation maxπ minλ≥0 L(π,λ) . PPO-Lagrangian and IPPO-Lagrangian
baselines update λ by stochastic ascent on Jc(π)−b while π is updated by PPO clipped-objective
ascent on L. Sauté PPO [43] instead augments the observation with the per-channel remaining cost
budgetb i − P t′<t γt′ ci(st′, at′)and trains plain PPO on the augmented state.
A.4 Per-task instantiation
Each task instantiates M through a TaskSpec/ConstraintSpec pair (the TaskSpec Protocol
surface is shown in Section E.2). Concrete observation, action, reward, and cost equations are given
in the task cards of Section C; per-task safety thresholds are part of each task’s configuration file, and
split definitions are listed in Section D.
A.5 Notation
Table 3: Notation used across the main paper and the appendix.
Symbol Meaning
CMDP and policy
S,AState and action spaces of one task.
PTransition kernel;deterministic given exogenous time-series.
r,c∈R k Scalar reward and per-step cost vector withktask-specific entries.
γ, TDiscount factor and episode horizon (T= 48orT= 288).
b∈R k ≥0 Cost thresholds (Form 1) or zero-violation set (Form 2).
π, ρ0 Policy and initial-state distribution.
λ∈R k ≥0 Lagrange multiplier vector.
Power system
P,QBranch active and reactive power flows.
v2 Vector of squared bus voltage magnitudes (DistFlow uses squared form).
D∈R Nℓ×N Downstream-aggregation matrix (radial PF).
Π∈R N×N ℓ Path matrix from slack bus to each bus (radial PF).
H,H d,H bus Generator-side, demand-side, and full bus-level PTDF (DC OPF).
Aaug Augmented KKT matrix in ADMM DC OPF.
p,p , pGenerator dispatch vector and its lower and upper output bounds (DC OPF).
z1,z 2 ADMM auxiliary variables for the generator-bound and line-flow constraints.
y1,y 2 ADMM dual variables for the generator-bound and line-flow constraints.
r(k) ADMM residual vector at iterationk(right-hand side of the augmented KKT
solve).
ρ, µADMM penalty parameter and PDIPM barrier parameter.
JAX primitives used in PowerZooJax
jax.jitCompiles the full rollout (reset, step, reward, cost) into a single GPU program.
jax.vmapRuns the same environment in parallel across batched scenarios.
jax.lax.scanUnrolls the per-episode loop (48 or 288 steps) on the device.
jax.lax.while_loopDrives the radial PF fixed-point iteration to convergence on the device.
jax.lax.fori_loopRuns a fixed number of ADMM or PDIPM solver iterations on the device.
PRNG key Random seed passed toreset/stepfor reproducible scenario and policy
sampling.
B Physical Models
The five tasks share five physical kernels (Table 4). Main paper Sections 5.1–5.2 give one equation
each for radial PF and DC OPF; this appendix gives the full derivations and shows how each kernel
becomes a fixed-shape JAX computation graph. Section B.4 covers the device dynamics shared by
DSO, DERs, and DCMG, and Section B.5 covers the DCMG couplings.
15

Table 4: Physical kernels reused across tasks.
Kernel Used by Output
Radial AC PF (DistFlow recurrence) DSO, DERs Branch flows, bus voltages, network loss
DC OPF (ADMM) TSO Generator dispatch, line flows, operating cost
Bid-based market clearing (PDIPM) GenCos Cleared dispatch, locational marginal prices, profit
Resource device dynamics DSO, DERs, DCMG SoC, PQ injections, flexible-load shifting, diesel output
DCMG balance and thermal coupling DCMG IT power, cooling demand, grid import, SLA tracking,
carbon emission
B.1 Radial AC power flow as a JAX graph
Standard DistFlow recurrence.Consider a radial feeder withNbuses andN ℓ =N−1branches,
slack bus 0, and per-branch resistance and reactance rℓ, xℓ. Each branch ℓ connects parent bus p(ℓ)
to child bus c(ℓ). Let pload n , qload n be the active and reactive load at bus n, and Pℓ, Qℓ be the active
and reactive flow on branch ℓ (positive in the parent→child direction). The DistFlow recurrence [33]
reads
Pℓ =p load c(ℓ) + X
ℓ′∈children(ℓ)
Pℓ′ +r ℓ
P 2 ℓ +Q 2 ℓ
v2 p(ℓ) ,(9)
Qℓ =q load c(ℓ) + X
ℓ′∈children(ℓ)
Qℓ′ +x ℓ
P 2 ℓ +Q 2 ℓ
v2 p(ℓ) ,(10)
v2 c(ℓ) =v 2 p(ℓ) −2  rℓPℓ +x ℓQℓ  + (r2 ℓ +x 2 ℓ ) P 2 ℓ +Q 2 ℓ v2 p(ℓ) ,(11)
where children(ℓ) denotes the set of branches whose parent bus is c(ℓ). Conventional pipelines walk
the feeder tree backward (children → parent) to evaluate Pℓ, Qℓ, then forward (root → leaves) to
evaluate v2 n, iterating until maxn |v2,(k) n −v 2,(k−1) n |< ε (typically ε= 10 −6). On a host CPU each
pass is a Python tree walk and each iteration triggers a host-device synchronization.
Topology matrices.For a radial network the backward and forward sweeps depend only on topology,
so they can be precomputed once at environment construction time as two binary matrices:
D∈ {0,1}Nℓ×N , D ℓ,n =
1if busnis downstream of branchℓ,
0else,
Π∈ {0,1}N×N ℓ ,Π n,ℓ =
1if branchℓlies on the path from bus0to busn,
0else.
(12)
The DistFlow iteration becomes
P(k) =D  pload +p loss,(k−1) ,
Q(k) =D  qload +q loss,(k−1) ,
δ2,(k) = 2 (r⊙P (k) +x⊙Q (k))−(r 2 +x 2)⊙ (P(k))2 + (Q(k))2
v2,(k−1) p(·) ,
v2,(k) =V 2 slack 1−Πδ 2,(k),
(13)
with the per-bus loss-correction ploss,q loss recomputed from the previous iterate. Equation (13)
expresses one PF iteration as fixed-shape jax.numpy matrix-vector products with no host-side
branching.
Compiled fixed-point loop and batching.The whole iteration body f: (P,Q,v 2)→(P ′,Q ′,v ′2)
is implemented with jnp and lax ops only, with no host-side mutation. PowerZooJax wraps it in
jax.lax.while_loop with the convergence predicate evaluated on traced arrays, then composes the
per-step PF solve with reward and cost computation through jax.lax.scan for time and jax.vmap
16

for batched scenarios. The 48 PF evaluations of one DSO or DERs episode are therefore one
accelerator-resident computation, not 48 host-side solver calls. The same kernel powers DSO and
DERs.
B.2 DC optimal power flow with ADMM
LP formulation.TSO uses a DC OPF with the bus-level PTDF Hbus ∈R Nℓ×N from the prebuilt
case file; H∈R Nℓ×Ng and Hd ∈R Nℓ×Nd select the generator and demand bus columns of Hbus.
Let p∈R Ng be the generator dispatch vector,cg marginal cost, pd ∈R Nd nodal demand, f line-flow
limits, and(p , p)generator output bounds. The DC OPF is the LP
min
p
cg⊤ ps.t.1 ⊤p=1 ⊤pd,|Hp−H dpd| ≤f,p ≤p≤ p.(14)
This DC OPF is the inner solver invoked at every step of the TSO task; commitment, ramp, and
minimum up/down-time constraints are enforced by the environment (Section C.2).
ADMM iteration.We split the box and line-flow constraints into auxiliary variables z1,z 2 with
dual variables y1,y 2 and penalty ρ >0. The system-wide power balance is kept as a hard equality
and handled by an augmented KKT system. After standard derivation [34] the ADMM update for
iterationkreads p(k+1)
ν(k+1) eq

=A −1 aug

r(k)
1⊤pd

,
z(k+1) 1 = clip  p(k+1) +y (k) 1 /ρ,p , p  ,
z(k+1) 2 = clip  Hp(k+1) −H dpd +y (k) 2 /ρ,− f, f  ,
y(k+1) 1 =y (k) 1 +ρ  p(k+1) −z (k+1) 1  ,
y(k+1) 2 =y (k) 2 +ρ  Hp(k+1) −H dpd −z (k+1) 2  ,
(15)
with the residual r(k) =−c g +ρz (k) 1 −y (k) 1 +ρH ⊤(z(k) 2 +H dpd)−H ⊤y(k) 2 , the multiplier νeq on
1⊤p=1 ⊤pd recovered alongside p(k+1) and discarded after extraction, and the augmented KKT
matrix
Aaug =

ρ(I+H ⊤H)1
1⊤ 0

(16)
depending only on the case parameters; PowerZooJax precomputes A−1 aug at construction time, so
each ADMM iteration becomes one matrix-vector product plus elementwise clips. The whole solve
runs as a fixed-length jax.lax.fori_loop (TSO uses 200 iterations and tolerance 10−4), which
compiles to a single XLA program. TSO uses this kernel.
B.3 Bid-based market clearing with PDIPM
GenCos clears a security-constrained economic dispatch (SCED) over piecewise-linear bid curves.
Each agent i submits up to S= 3 break-points; the clearing problem with bid prices cb i,s and segment
caps pi,s is
min
pi,s≥0
X
i,s
cb i,s pi,s s.t. X
i,s
pi,s =D t,|Hp−H dpd| ≤f, p i,s ≤ pi,s.(17)
PowerZooJax solves it with a primal-dual interior-point method [35]. With barrier parameter µ, the
perturbed KKT system is
∇pL= 0, s j ξj =µ,∀j, s j ≥0, ξj ≥0,(18)
where sj, ξj are slacks and multipliers for the inequality constraints. At each iteration the duality gap
µ(k) =s (k)⊤ξ(k)/m is recomputed and shrunk via a centring term: the perturbed complementarity
residual uses target σ µ(k) with σ= 0.2 . Each Newton step solves a reduced KKT system. The
loop runs as a fixed-length jax.lax.fori_loop with early stopping when µ(k) <10 −5. The
dual variable ν∗ on the power-balance equality is recovered analytically from the primal solution;
locational marginal prices are
π∗ =−ν ∗ 1−H ⊤ busξ∗ flow,(19)
where ξ∗ flow =ξ ∗ upper −ξ ∗ lower is the net line-constraint dual built from the duals of the upper and lower
line-flow inequalities in (17).
17

B.4 Resource device dynamics
Battery storage.For battery j with capacity Emax j (MWh) and rated powerP max j (MW), the per-step
state-of-charge update with charge/discharge efficienciesη c j , ηd j and step length∆tis
SoCt+1 j = clip  SoCt j + ∆t Emax j  ηc j pc j,t − 1 ηd j pd j,t  ,SoC min j ,SoC max j  ,(20)
with pc j,t, pd j,t ∈[0, P max j ] and pc j,t pd j,t = 0 enforced by parameterizing the action as pj ∈
[−P max j , Pmax j ] and splitting at zero. Tasks that include batteries (DERs, DCMG) terminate the
episode by adding a quadratic penalty(SoC T j −SoC target j )2.
PV inverter.A PV inverter j with rated apparent power Smax j , available DC power pavail j,t , and
active/reactive setpointsp j,t, qj,t enforces the box-projected PQ envelope
0≤p j,t ≤p avail j,t , p 2 j,t +q 2 j,t ≤(S max j )2,(21)
implemented as a closed-form projection onto the inverter capability circle.
Flexible load.Flexible load j has nominal demand dnom j,t , curtailment cap ηcur j ∈[0,1] , shifting cap
ηshift j , and a shift horizon Hj (steps). Curtailed energy is permanently lost; shifted energy must be
repaid withinH j steps. The realized demand and the per-load energy buffer evolve as
dreal j,t = (1−u cur j,t)d nom j,t −u shift j,t dnom j,t +u recall j,t ,(22)
Eshift j,t+1 =E shift j,t +u shift j,t dnom j,t −u recall j,t ,(23)
withu shift j,t ≤η shift j andu cur j,t ≤η cur j . DSO and DERs use this model.
Diesel generator.Diesel generator j has rated power P max j and a linear fuel cost Cj(p) =c fuel j p
proportional to the delivered active power. The continuous normalized commandadg j,t ∈[0,1] maps to
pj,t = clip(adg j,t P max j ,0, P max j ),cost j,t =C j(pj,t) ∆t,(24)
with an optional minimum-loading threshold (adg j,t < Pmin j /(2P max j ) snaps to 0, in between snaps up
to P min j ) so the operating point respects diesel wet-stacking guidance. DCMG wraps the diesel as
a same-step residual-slack actuator, so dispatch is realized after the workload, cooling, and battery
decisions.
B.5 DCMG coupling
The DCMG task couples the device dynamics of Section B.4 with a lumped-capacitance thermal
model and a single-bus power balance. Let Wt be the GPU-equivalent compute load, θIT t the IT-zone
temperature, θout t the outdoor temperature, and pcool t the cooling electrical power. The IT-zone thermal
dynamics are
θIT t+1 =θ IT t + ∆t Cth  αW Wt −β t pcool t +γ out(θout t −θ IT t )  ,(25)
with thermal capacity Cth, IT-to-heat coefficient αW (so αW Wt is the IT electrical power at step
t, equal to its heat output), wall-to-ambient coefficient γout, and cooling COP βt =β(θ out t ) that
decreases with outdoor temperature. The over-temperature cost channel cth t = (θIT t −θ max)+ is added
to the cost vector at every step. Cooling is implemented as a setpoint-tracking controller: the RL
action acool t sets the IT-zone setpoint, and pcool t equals the resulting heat-removal rate divided by βt
(Section C.5).
The local power balance at the point of common coupling is
pDC t =p PV t +p batt t +p DG t +p grid t ,(26)
where pDC t =p IT t +p cool t +p aux t is the total data-center load and paux t is the auxiliary load (PSU losses
and other site loads, modeled as a fixed fraction ofpIT t ). Grid import pgrid t ∈[0, pgrid] in grid-connected
mode and pgrid t = 0 in islanded mode. SLA tracking compares served workload against committed
jobs; the SLA-deficit cost channel is the per-step expired-task count normalized by the GPU count.
The reward combines energy use, electricity cost (GB MID market price), and carbon emission
(grid-import and DG carbon intensities); the weights are given in Section C.5.
18

C Per-Task Cards
This section gives the formal CMDP instantiation, observation, action, reward, cost vector, splits,
baselines, and safety budgets for each of the five tasks. Concrete numerical thresholds, time-step
lengths, and split sizes are taken from the per-task configuration files (Section E.3 shows one such
file). Table 5 gives a one-line summary of the suite.
Notation in the task cards.We use bold lowercase for vectors and bold uppercase for matrices;
symbols without a t subscript are time-invariant. Per-task dimensions follow each task’s case file and
configuration; the explicit dimension counts under each observation/action equation in this section
are evaluated at the canonical case ( case5, case118, case33bw, case141, and the data center
microgrid configuration shipped with the benchmark).
Table 5: One-line task overview.
Task Decision problem Primary metric Cost channels
GenCos 5-agent strategic bidding on 5-bus market, 48
half-hour steps
Total per-agent profit Thermal overload (diagnostic)
TSO 1-agent SCUC on 118-bus system, 48
half-hour steps
Operating cost Reserve, thermal (Form 2)
DSO 1-agent demand response on 33-bus feeder,
48 half-hour steps
Network loss (MWh) V oltage band
DERs 12-agent cooperative DER control on 141-bus
feeder, 48 half-hour steps
Active power loss (MW) V oltage band, thermal, re-
source
DCMG 1-agent data center microgrid scheduling, 288
five-minute steps
Episode return SLA, over-temperature, power
balance
C.1 Generation-company bidding task (GenCos)
Task.Five generation companies (GenCos) compete in a repeated wholesale electricity market
on the IEEE 5-bus transmission grid (case5, GB demand profiles6; see Figure 7). The horizon is
24 hours at 30-minute resolution, so an episode contains 48 sequential market clearing steps. At
each step the market operator clears all bids via a security-constrained economic dispatch (SCED,
an optimization that picks the cheapest feasible bid mix subject to grid limits), returning each
unit’s dispatch level P g i,t and the locational marginal prices (LMPs, the per-bus electricity prices).
Successive clearings are coupled by runtime ramp bounds (per-step limits on how fast a generator
can change output) enforced inside the SCED linear program: at step t each unit’s box constraint is
tightened to pmin i,t = max(pmin i , Pg i,t−1 −∆P down i ) and pmax i,t = min(pmax i , Pg i,t−1 + ∆P up i ), so the
episode is a rolling sequential market rather than 48 independent auctions. The market and the grid
are shared across the five agents, which makes this a competitive multi-agent task.
Observation and Action.Each agent owns one generator and observes only its own physical status
plus a few public market signals. For agenti,
oi,t =

cb i , eP max i , Pg i,t−1,ewi,t−1, hramp i,t , Dfcst t+1, πhist t , τt  ∈R 12.(27)
ai,t ∈[−1,1] Kseg .(28)
Each unit’s true cost is TCi(P) = ai 3 P 3 + bi 2 P 2 +c iP , the integral of a quadratic marginal cost
(the cost of producing one extra MW at output P ) MCi(P) =a iP 2 +b iP+c i; truthful prices
are obtained by evaluating MCi at the midpoint of each of Kseg=3 equal-width segments covering
[pmin i , pmax i ]. The eight observation entries are:
•c b i: unit’s truthful first-segment price (lowest-block marginal cost), normalized by the
configured price scale;
• eP max i : capacity relative to the largest unit;
6Great Britain demand traces from the National Energy System Operator (NESO), https://www.neso.energy/
data-portal/historic-demand-data.
19

B1 B2
B3B4B5
G1 G2
G3G4G5
D2
D3D4
L1
L3 L4
L2
L5L6
Figure 7: IEEE 5-bus market test system (case5) used by the GenCos task: 5 buses B1–B5 (horizontal
bars), 6 transmission lines L1–L6, 5 thermal generators G1–G5 (circled symbols, one per agent; G1
and G2 share bus B1, while G3, G4, G5 sit at buses B3, B4, B5 respectively), and 3 load sites D2,
D3, D4 (outward arrows at buses B2, B3, B4). Each step, the SCED clearing of Section B.3 returns
the per-bus LMPs and per-unit dispatches that drive each agent’s profit.
•P g i,t−1: previous dispatch, normalized by the agent’s capacity;
•ewi,t−1: previous-step profit, normalized by a fixed maximum-revenue scale;
•h ramp i,t = min(pmax i −P g i,t−1,∆P up i )/pmax i : achievable ramp-up next step (the smaller of
remaining capacity and the per-step ramp-up limit);
•D fcst t+1: next-step total-demand forecast (perfect one-step look-ahead, normalized by total
capacity);
• πhist t ∈R 4: circular buffer of the four most recent system-mean LMPs (oldest to newest),
giving every agent a coarse public price-dynamics signal;
•τ t ∈R 2: sin/cos time-of-day encoding.
The six task-level scalars, the four-element price history, and the two-component time encoding sum
to 12.
The raw actiona i,t is mapped to a piecewise bid curve in three steps:
1. Shift to non-negative magnitudesm i,t = (ai,t + 1)/2∈[0,1] Kseg.
2. Sort along the segment axis to enforce a monotone offer (no later block cheaper than an
earlier block).
3. Apply a multiplicative markup capped by a configured maximum, so that the cleared offer
for segment k is offeri,k,t =c seg i,k ·  1 + sort(mi,t)k · m  with cseg i,k the truthful segment
price.
Reward and Violation Cost.Each agent’s reward is its realized profit at the cleared dispatch, equal
to cleared revenue π∗ b(i),t P g i,t ∆t minus true production cost TCi(P g i,t) ∆t, where b(i) is the bus (the
network node where loads and generators connect) of uniti:
ri,t =

π∗ b(i),t P g i,t −TC i(P g i,t)  ∆t, c t =C thermal t ,(29)
with π∗ the cleared LMP vector from Section B.3. The single violation channel C thermal t is the sum
of post-clearing line-flow violations (in MW), shared across agents because line overloads are a
property of the joint outcome rather than of any single bid. This channel is reported as a market-side
diagnostic only.
Baselines.The benchmark releases three non-learning strategic baselines (Truthful, Uniform-mid,
and Max-markup) together with a learned IPPO baseline that uses one shared actor-critic across the
20

five GenCos. The three heuristics bracket the strategic spectrum: Truthful (bidding at marginal cost)
is the competitive-equilibrium reference (the outcome where every bidder offers at marginal cost),
Max-markup (bidding at the configured cap) is the upper envelope of market power, and Uniform-mid
(bidding at the midpoint markup) sits between them as a neutral oligopoly reference.
Challenge.GenCos is a non-stationary, partially observable, competitive multi-agent task. Each
agent only sees its own dispatch, profit, and a small public LMP window, and the market reward
depends on the joint action through the SCED clearing. Policy improvement for one bidder shifts the
optimization problem faced by every other bidder. These factors together define the standard hard
regime for current MARL.
C.2 Transmission dispatch task (TSO)
Task.A single transmission system operator (TSO) runs the 54-generator IEEE 118-bus transmission
grid (case118, 186 lines; see Figure 8) over a 24-hour horizon at 30-minute resolution, which gives
48 sequential decision steps per episode and is driven by GB net-load profiles (gross demand minus
must-take wind and solar)7. At each step the agent decides which generators are on (commitment)
and how much each produces (dispatch); the environment then enforces ramp limits (per-step bounds
on how fast a unit can change output), minimum up/down times (a unit must remain in its current
state for at least this many consecutive steps after a transition), and a DC optimal power flow solution
(a linear approximation that maps generator output to per-line flows). One centralized agent sees the
whole grid, so this is a fully observable single-agent task with a large mixed continuous/binary action
space.
Observation and Action.The observation summarizes the whole grid; the action specifies a
commitment intent and a dispatch preference per generator:
ot =

ut,t state t ,P g t−1,C g,f t−1, D t, ηrsv t , τt,D fcst t  ∈R 410. (30)
at =

ucmd t ,P pref t  ∈[−1,1] 108.(31)
The nine observation entries, withN g=54andN ℓ=186, are:
•u t ∈ {0,1}Ng: on/off status of all generators, carried over from the previous step;
•t state t ∈R Ng: elapsed time each generator has been in its current on/off state (normalized),
letting a learner respect minimum up/down constraints by inspection;
•P g t−1 ∈R Ng: previous dispatch, normalized by per-unit capacity;
•C g ∈R Ng: linear coefficient bi of each unit’s quadratic marginal-cost function MCi(P) =
aiP 2 +b iP+c i, normalized by its maximum across units;
•f t−1 ∈R Nℓ: active power flow on each transmission line, normalized by line capacity;
•D t ∈R: aggregate system demand, normalized by total capacity;
•η rsv t ∈R : committed-headroom reserve ratio (committed capacity minus current load,
divided by load);
•τ t ∈R 2: sin/cos time-of-day encoding;
•D fcst t ∈R 4: four-step (two-hour) perfect look-ahead total-load forecast.
The dimension count is4N g +N ℓ + 4 + 4 = 410.
The action is two-headed:
•u cmd t ∈[−1,1] Ng: commitment intent applied by sign threshold (entries ucmd i,t >0 request
unit i on for the next step), with the active minimum up/down constraints overriding any
request that would violate them;
•P pref t ∈[−1,1] Ng: dispatch preference, denormalized linearly to each unit’s ramp-adjusted
feasible interval [pmin i,t , pmax i,t ] and added as a linear bias to its marginal-cost intercept inside
the DC OPF, so the cleared dispatch follows the preference whenever it is feasible under all
operational limits.
7Demand from the National Energy System Operator (NESO), https://www.neso.energy/
data-portal/historic-demand-data ; wind and solar from Elexon BMRS, https://bmrs.elexon.co.uk/
generation-by-fuel-type.
21

Figure 8: One-line diagram of the IEEE 118-bus transmission test system ( case118) used by the
TSO task: 118 buses (horizontal bars), 186 branches (lines connecting buses), 54 thermal generators
(circled G; arrows pointing into their bus), and 91 load sides (arrows pointing out of their bus). The
TSO task in Section C.2 commits and dispatches the 54 generators on a 30-minute cadence under
DC-OPF redispatch. Source: IIT Power Group, 2003.
The action dimension is2N g = 108.
Reward and Violation Cost.The reward is the negative total operating cost, summing fuel, startup,
and no-load components, rescaled by a fixed factor (Section F.1). The two-channel violation cost
separately reports thermal line overloads C thermal t (the cumulative MW above each line’s capacity)
and reserve-margin shortfalls C reserve t (the MW deficit of committed headroom relative to the
configured 5% margin), so that a safe-RL learner can trade them off explicitly rather than collapse
them into a single penalty. Both channels are reported under Form 2 (zero-violation constraint):
rt =−C operating t ,c t =  C thermal t , Creserve t  .(32)
Baselines.The benchmark provides two heuristic baselines (All-On, which leaves every unit
committed, and Merit Order, which commits the cheapest unit first until total capacity covers demand
plus a fixed 5% reserve margin) and two learned baselines: PPO as the unconstrained reference and
PPO-Lagrangian with a primal-dual update on the two cost channels.
Challenge.TSO mixes 54 binary commitments with 54 continuous setpoints, so the action space
is high-dimensional and combinatorial. Each step also requires the policy to keep an OPF feasible
against ramp, minimum up/down, thermal, and reserve constraints simultaneously. Reserve violations
are sparse and bursty, which hurts safe-RL credit assignment.
C.3 Distribution demand response task (DSO)
Task.A single distribution system operator (DSO) coordinates six flexible loads on the IEEE 33-bus
distribution network ( case33bw; see Figure 9) over a 24-hour episode at 30-minute resolution,
22

which gives 48 sequential decision steps per episode and is driven by real Ausgrid demand profiles8.
The goal is to reduce total active power loss while keeping every bus voltage inside the safe band
[0.94,1.06] p.u. (per unit, the normalized voltage scale used in power systems). One centralized
agent sees the whole network, so this is a fully observable single-agent task with smooth continuous
control.
1
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
19 20 21
22
26 27
28
29 30 31 32
33
23 24 25
Substation
Passive load bus
Flexible load
Figure 9: IEEE 33-bus radial distribution network (case33bw) used by the DSO task. The substation
(factory icon) at bus 1 supplies the network through a main feeder (buses 2–18) and three lateral
branches (19–22, 23–25, 26–33). Gray house icons mark passive loads; orange house icons mark the
six controllable flexible loads at buses 6, 14, 18, 22, 28, and 33. The DSO task in Section C.3 sets
curtailment and load-shift fractions for these six devices on a 30-minute cadence under radial AC
power flow.
Observation and Action.
ot =

Vt,P br t ,Q br t ,P load t ,Q load t , τt,z flex t  ∈R 195.(33)
at =

dcurtail t ,d shift t  ∈[−1,1] 12.(34)
The seven observation entries, withN=33buses andN ℓ=32branches, are:
•V t ∈R N : per-bus voltage magnitude, centered and scaled as (|V| −1)/0.1so nominal
voltages sit near 0 and the band edges0.94/1.06p.u. sit near±0.6;
•P br t ,Q br t ∈R Nℓ: active and reactive (the imaginary part of AC power, in MV Ar) power
flows on each branch, normalized by the reference load;
•P load t ,Q load t ∈R N : active and reactive nodal demands, normalized by the reference load;
•τ t ∈R 2: sin/cos time-of-day encoding;
•z flex t ∈R 30: stacks five normalized variables per controllable load —
[ccur, sout, sin, bfill, beng], namely current curtailment level, outgoing/incoming shift
fractions, deferred-buffer fill ratio, and deferred-buffer energy — across the six flexible
loads.
The dimensions sum to3N+ 2N ℓ + 2 + 6×5 = 99 + 64 + 2 + 30 = 195.
The action is two-headed and per device:
•d curtail t ∈[−1,1] 6: curtailment intent, clipped to [0,1] inside each FlexLoad bundle and
then multiplied by that device’s curtailment cap, applied at the current slot (curtailed energy
is permanently lost);
•d shift t ∈[−1,1] 6: load-shift intent, clipped to [0,1] and multiplied by that device’s shift cap,
postponing demand to a later slot inside the H=4-step (two-hour) shift horizon (shifted
energy must be repaid withinHsteps).
8Ausgrid distribution demand traces, https://www.ausgrid.com.au/Industry/Our-Research/
Data-to-share/.
23

Reward and Violation Cost.The reward is the negative total network loss P loss t (in MW summed
over all Nℓ branches). The violation cost C voltage t is the count of buses whose voltage falls outside
the safe band on the current half-hour slot (an integer in [0, N], then averaged into the per-step rate
reported in Section G.3). This channel is reported under Form 1 (budgeted expected cost):
rt =−P loss t , c t =C voltage t .(35)
Baselines.Three heuristic baselines are released:
•No Control: zero curtailment, zero shift;
• TOU(time-of-use): fixed peak-window rule that curtails and shifts demand during 16:00–
21:00 each day;
• Droop: a local voltage droop response that reacts only to each controllable load’s own bus
voltage.
Four learned baselines are trained on the same observation and reward: PPO, SAC, Sauté PPO, and
PPO-Lagrangian.
Challenge.DSO has a smooth and continuous action space, but the reward (loss) and the cost
(voltage) point in opposite directions: lowering loss often pushes voltages closer to the band edges,
and the band must hold for every bus on every half-hour slot. V oltage couples the six controllers
through the shared power flow equations, so learning has to discover a joint policy that respects a
global constraint from local actions, which is the standard hard regime for safe-RL methods even
when control itself is smooth.
C.4 Distributed energy resource coordination task (DERs)
Task.Twelve heterogeneous distributed energy resources — four batteries, four PV (photovoltaic)
inverters, and four flexible loads — sit at fixed buses of the 141-bus radial distribution feedercase141
(see Figure 10). The horizon is 24 hours at 30-minute resolution, which gives 48 sequential decision
steps per episode, and is driven by real Ausgrid demand profiles 9 for the bus-level loads and GB
solar availability traces10 for the PV bundles. Each device is its own agent. The agents cooperate to
minimize total active power loss while keeping every bus voltage inside the safe band[0.94,1.06] p.u.
and respecting line thermal limits. The actions are heterogeneous: the same 2-dimensional action slot
means different things for batteries, PV inverters, and flexible loads, so this is a partially observable
cooperative MARL task with agents grouped by type.
Observation and Action.The 141-bus network is too large for every agent to read every bus, so
each agent samples the grid only through a small local window. Agent i sits at bus b(i) and reads (i)
its own bus voltage, (ii) the voltages at its K=4 nearest BFS-graph-neighbor buses (the part of the
feeder it directly affects), (iii) a three-number summary of the system-wide voltage profile (its only
global signal), and (iv) its own device internal state:
oi,t =

Vb(i),t,V NK (i),t, eVt, τt,z device i,t  ∈R 15.(36)
The action is per-agent 2-dimensional,a i,t ∈[−1,1] 2, with type-specific physical interpretation:
ai,t =




P bat i,t , Qbat i,t  battery,
κpv i,t, Qpv i,t  PV inverter,
dcurtail i,t , dshift i,t  flexible load. (37)
The five observation entries are:
•V b(i),t ∈R : voltage at the agent’s own bus, centered and scaled the same way as in the DSO
observation;
•V NK (i),t ∈R K: voltages at the agent’s K=4 nearest BFS-graph-neighbor buses, ordered
by graph distance on the feeder topology;
9Ausgrid distribution demand traces, https://www.ausgrid.com.au/Industry/Our-Research/
Data-to-share/.
10GB solar from Elexon BMRS,https://bmrs.elexon.co.uk/generation-by-fuel-type.
24

1
2 3 4 5 6 7 8 9 10 11 12 13
33 34
35
36 111 112 113
37 38 39 40 41
42 43 44 45 46 47 48 49 50 51 52
53
73 74
54 55 56 57 58 59
70 71
72
60 61 62
63 64 65 66 67 68
69
75
76 78 79 80
81 82
77 83
84 85 86 87
14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
135 136 137 138 139 140 141
117
118 119 120 121 122 123 124 125 126 127 128 129 130
131 132
133
134
114 115 116
88 89 90 91 92 93 94 95
96 97
98
99 100 101 102 103 104 105
106
107
108 109
110
Substation
Battery (BESS)
PV inverter
Flexible load
Figure 10: 141-bus radial distribution feeder ( case141) used by the DERs task. The substation
(factory icon) at bus 1 supplies the network through deep radial branches. Twelve DER agents are
sited at fixed buses: 4 batteries (BESS, teal vertical bars) at buses 9, 17, 55, 122; 4 PV inverters
(sun-panel icons) at buses 6, 72, 73, 82; and 4 flexible loads (orange houses) at buses 24, 41, 70, 135.
Small black dots mark passive buses without an attached DER agent. The 12 agents share a team
reward (negative network active power loss) and cooperate under partial observability with K=4
BFS-graph-neighbor windows (Section C.4).
• eVt = (Vmin, Vmax, Vmean)∈R 3: min, max, and mean of the full bus voltage vector — a
coarse global signal that does not reveal per-bus details;
•τ t ∈R 2: sin/cos time-of-day encoding;
•z device i,t ∈R 5: the agent’s own device internal state, sized to the maximum per-device
observation length across DER types and zero-padded for shorter types so all twelve agents
share a fixed 15-dimensional input shape under typed parameter sharing. By type: 3 entries
[SoC, normalized p, normalized q] for a battery; 4 entries [capacity factor (current solar
output relative to nameplate), dispatchedp, dispatched q, curtailment level] for a PV inverter;
5 entries [current curtailment, outgoing shift fraction, incoming shift fraction, deferred-buffer
fill ratio, deferred-buffer energy] for a flexible load.
The dimension count is1 +K+ 3 + 2 + 5 = 15.
The action is type-specific (the same 2-dim slot but different physical meaning):
• Battery: (P bat i,t , Qbat i,t ) active and reactive power, denormalized linearly from [−1,1] 2 to the
inverter capability envelope {(p, q) :p2 +q 2 ≤(S max i )2} (Section B.4) and clipped against
the SoC-feasible discharge / charge bounds;
• PV inverter: (κpv i,t, Qpv i,t) a curtailment factor κ∈[0,1] (fraction of available solar power to
use) and a reactive-power setpoint, projected onto the same PQ envelope (Section B.4) with
ppriority;
• Flexible load: (dcurtail i,t , dshift i,t ) curtailment and load-shift fractions exactly as in the DSO
task — clipped to[0,1], scaled by per-device caps, with a shift horizonH=4steps.
Reward and Violation Cost.All twelve agents share a single team reward, the negative total active
power lossP loss t in MW summed over allN ℓ branches:
rt =−P loss t ,c t =  C voltage t , Cthermal t , Cresource t  .(38)
The three-channel violation cost separately reports:
•C voltage t : count of buses whose voltage falls outside the safe band [0.94,1.06] p.u. on the
current step;
25

•C thermal t : count of branches whose apparent power flow |S| exceeds the line capacity on
the current step;
•C resource t : per-step bundle physical cost — e.g. an opportunity cost when a PV inverter
curtails available solar power, or a clipping penalty when a battery dispatch hits its SoC
bounds.
All three channels are reported under Form 1 (budgeted expected cost).
Baselines.Two heuristic baselines are released:
• No Control: every device idle (battery P=Q=0 , PV at MPPT with no curtailment, flexible
loads serving nominal demand);
•Voltage Droop: a local reactive-power droop rule keyed to each agent’s own bus voltage.
Three learned baselines use type-specific parameter sharing in IPPO, with one shared actor-critic per
agent type:
•IPPO: the reference variant, trained with a voltage-violation penalty of weight 4.0;
•IPPO-rs: the same with the penalty doubled to 8.0;
• IPPO-Lagrangian: separate cost critics for the three cost channels with a shared dual
variable across types.
Challenge.DERs combines partial observability (each agent only sees a K=4 local window plus
a three-number global summary), heterogeneous agents (batteries, PV , and flexible loads share a
reward but not an action interface), and a network-wide constraint (voltage band) that couples all
twelve agents through the power flow equations. The reward is a single global signal (loss in MW),
while the safety violations can fire from any one of the twelve agents, so credit assignment is hard.
These remain open problems for cooperative MARL, especially at feeder sizes where no agent can
hold a global view.
C.5 Data Center Microgrid task (DCMG)
Task.A microgrid powers an AI data center with on-site PV , battery storage, a diesel generator,
and a connection to the main grid. A single operator schedules training and fine-tuning workloads,
cooling, battery dispatch, diesel generation, and grid import over a 24-hour horizon at 5-minute
resolution (288 steps per episode), driven by real Google data center workload traces [30], GB solar
availability traces11 for the on-site PV , and GB MID market grid-import prices12. The microgrid
runs grid-connected by default; under simulated outage scenarios it switches to islanded mode where
unmet demand counts as a hard violation. The setting is a long-horizon, multi-objective single-agent
RL problem: trade off energy use, cost, and carbon while respecting service-level, thermal, and
power-balance constraints.
Observation and Action.At each step the operator observes a joint workload, thermal, and energy
snapshot:
ot =

ucpu t , umem t , qtrain t , qft t , ηt, Tzone t , Tout t ,COP t, αpv t ,SoC t,
mdg t , pload t , pnet t , βdis t , βchg t , πgrid t , πgrid,6h t ,a t−1, τt  ∈R 24. (39)
at =

atrain t , aft t , acool t , abatt t , adg t  ∈[0,1] 3 ×[−1,1]×[0,1].(40)
The 24 observation entries split into five thematic blocks plus the previous action and a time encoding:
• Workload state(5 dims): ucpu t , umem t ∈[0,1] are GPU compute and memory utilization;
qtrain t , qft t ∈[0,1] are the training and fine-tuning queue fills (waiting GPU demand normal-
ized by total GPU count); ηt ∈[−1,1] is the deadline urgency of the most pressing waiting
job (negative means already overdue);
11GB solar from Elexon BMRS,https://bmrs.elexon.co.uk/generation-by-fuel-type.
12GB Market Index Data (MID) from Elexon BMRS,https://data.elexon.co.uk/bmrs/api/v1/datasets/MID.
26

• Thermal state(3 dims): T zone t ∈[0,1] the server-zone temperature, T out t ∈[0,1] the
outdoor temperature (both centered and scaled to the operating range), and COPt ∈[0,1]
the chiller’s coefficient of performance (higher means more cooling delivered per unit
electricity);
• Energy assets(3 dims): αpv t ∈[0,1] the PV capacity factor (current solar output relative to
nameplate), SoCt ∈[0,1] the battery state of charge, and mdg t ∈[0,1] the remaining diesel
headroom;
• Power balance and battery headroom(4 dims): pload t ∈[0,1] the total data-center electrical
load (normalized by total supply capacity), pnet t ∈[−1,1] the residual net load after PV
(signed), and βdis t , βchg t ∈[0,1] the battery’s discharge and charge headroom as fractions of
rated power;
• Grid price signal(2 dims): πgrid t ∈[0,1] the current GB MID grid-import price (normalized)
and πgrid,6h t ∈[0,1] the maximum grid price expected over the next six hours, giving the
policy a forward look-ahead for arbitrage;
• Previous action and time encoding(5 + 2 dims): at−1 ∈R 5 the previous-step action and
τt ∈R 2 the sin/cos time-of-day encoding.
The dimension count is11 + 6 + 5 + 2 = 24.
The 5-dimensional action has mixed bounds:
•a train t , aft t ∈[0,1] : fractions of the training and fine-tuning queues dispatched in the next
5-minute slot;
•a cool t ∈[0,1] : cooling setpoint command (lower means a colder zone setpoint, requiring
more cooling power);
•a batt t ∈[−1,1] : battery dispatch signal (negative charges, positive discharges; scaled by
rated power and clipped against SoC-feasible bounds inside the bundle);
•a dg t ∈[0,1] : diesel generator preference — realized as a same-step residual slack actuator
after the workload, cooling, and battery decisions are applied, soadg acts as a soft preference
rather than a strict setpoint.
Reward and Violation Cost.The reward sums an energy-use term, a grid-cost term, and a carbon-
emissions term, with scalar weights wcost, wcarbon that the operator can pick to encode a Pareto
preference (the canonical benchmark usesw cost = 0.2,w carbon = 0.1):
rt =r energy t +w cost rcost t +w carbon rcarbon t ,c t =  C SLA t , Ctemp t , Cpwr t  .(41)
The three-channel violation cost separately reports:
•C SLA t : workload incompletion — the per-step count of expired tasks normalized by the
GPU count;
•C temp t : server-zone over-temperature,C temp t = (T zone t −T max)+;
•C pwr t : per-step power deficit — the shortfall when on-site generation, battery, and grid
import together cannot serve the data-center load. This channel is the hard constraint
that becomes binding under simulated outage scenarios when the microgrid is forced into
islanded mode.
All three channels are reported under Form 1 (budgeted expected cost).
Baselines.Three heuristic baselines are released:
•No Control: always-on policy with no scheduling;
•Max renewable: serve workload from PV first, then battery, then diesel;
•Rule-based: a heuristic scheduler that respects SLA, temperature, and SoC bands.
Two learned baselines are trained with fixed penalty weights on the SLA, over-temperature, and
deficit channels added to the reward:
•PPOwith a Beta distribution policy head for bounded actions;
27

•SACwith a tanh-squashed Gaussian.
Challenge.DCMG is a long-horizon (288 steps), multi-objective single-agent task with three hard
constraint channels. The objectives (energy, cost, carbon) and the constraints (SLA, over-temperature,
power deficit) are cross-coupled: deferring training jobs saves energy but risks SLA misses; running
cooling harder protects servers but burns diesel; charging the battery during PV peaks improves later
resilience but uses up current SLA headroom. Credit must be propagated across hundreds of 5-minute
steps under stochastic workload, weather, and PV traces, which is precisely the regime that current
model-free RL handles poorly.
D Data Sources and Splits
D.1 Data and splits
Table 6 summarizes the external time-series traces used in the reported results, the network case for
each task, the splits, and the seed and episode budget. Processed copies of these traces are shipped
with the PowerZooJax code release.
Table 6: External time-series traces, splits, and seed and episode budgets per task. GB denotes Great Britain. Bold marks the
primary split used for the headline metric reported in Section G; for DCMG the appendix-only splits follow the semicolon.
Task System / case Time-series source(s) Splits Seed budget
GenCos 5-bus market GB demand train,in-distribution, demand shift,
renewable shock
5 seeds, 30
episodes/seed
TSO 118-bus
transmission
GB demand, wind, and
solar
train,in-distribution, load stress, line
tightening
5 seeds, 50
episodes/seed
DSO 33-bus feeder Ausgrid distribution
demand
in-distribution5 seeds, 50
episodes/seed
DERs 141-bus feeder Ausgrid distribution
demand and GB solar
train,in-distribution, voltage
tightening, PV shift, load stress
5 seeds, 30
episodes/seed
DCMG Behind-the-
meter microgrid
Google workload (Azure
and Alibaba for
workload-OOD splits); GB
solar; GB MID price
train,in-distribution, cooling stress,
renewable drought; appendix: workload
swap, workload shock, dg derating,
SLA tightening
5 seeds, 10
episodes/seed
D.2 Split and stress-test taxonomy
Each split asks a different physical question. Table 7 groups them by the mechanism that changes
between train and evaluation or between routine and stressed evaluation, and states the role of each
split.
Table 7: Split and stress-test taxonomy. Each row states the physical mechanism and the role of the split.
Split type Tasks / split names Physical mechanism Role
Routine
in-distribution
TSO, DSO, DERs, GenCos,
DCMG /in-distribution
Held-out episodes from the
routine evaluation regime
Main task comparison for the
primary metric
Load / demand shift TSO / load stress; DERs / load
stress; GenCos / demand shift
Higher or shifted demand
changes reserve pressure, feeder
loading, or market clearing
Whether an in-distribution policy
remains useful when demand
changes
Renewable / PV shift DERs / PV shift; GenCos /
renewable shock; DCMG /
renewable drought
Renewable generation changes
the controllable/exogenous
balance
Sensitivity to renewable
availability
Network / security
tightening
TSO / line tightening; DERs /
voltage tightening
Tighter physical operating limits
(line capacity or voltage band)
Whether lower cost or lower loss
survives under tighter operating
limits
28

Split type Tasks / split names Physical mechanism Role
Cooling / workload
stress
DCMG / cooling stress (main);
workload swap, workload
shock, SLA tightening
(appendix)
Data center thermal load,
workload mix, or service
deadlines change
Long-horizon resource scheduling
under thermal, workload, or
service stress
Resource-
availability stress
DCMG / dg derating Backup-generation capacity is
reduced
Sensitivity to reduced backup
capacity
E Quickstart and API
This section is a copy-pasteable walk-through of how to install PowerZooJax, run a minimal rollout,
read a task config, read a training config, and trigger a benchmark run from the CLI. Listings E.1–E.3
are minimal Python demos and theTaskSpecProtocol surface, Listings E.4–E.5 are abridged from
the released config files, and the bash blocks in Sections E.1 and E.5 cover install and CLI usage.
E.1 Installation
PowerZooJax requires Python 3.10–3.12. The base install ships a CPU-only JAX; CUDA 12 support
is opt-in via the cuda12 extra; the JAX single-agent RL stack lives behind rl (rejax, distrax) and
the multi-agent stack behind marl (jaxmarl); the benchmark workflow lives behind benchmarks
(Stable-Baselines3, SBX, PettingZoo).
git clone https://github.com/powerzoojax/PowerZooJax && cd PowerZooJax
pip install -e ".[rl,marl,benchmarks]"# CPU JAX
pip install -e ".[cuda12,rl,marl,benchmarks]"# Linux + CUDA 12
# JAX preallocates ~75% of VRAM on first GPU use; disable if sharing the GPU:
export XLA_PYTHON_CLIENT_PREALLOCATE=false
E.2 Minimal rollout
The example below opens a transmission environment on case5, resets it, then runs a 48-step rollout
underjax.lax.scanwith a fixed action schedule. Every transition stays inside JIT.
Listing E.1: Minimal rollout on case5 (Python)
import jax, jax.numpy as jnp
from powerzoojax.case import create_case5
from powerzoojax.envs import TransGridEnv, make_trans_params
from powerzoojax.utils import scan_rollout
env = TransGridEnv()
params = make_trans_params(create_case5())
key = jax.random.PRNGKey(0)
reset_key, rollout_key = jax.random.split(key)
obs, state = env.reset(reset_key, params)
actions = jnp.zeros((48, *env.action_space(params).shape), dtype=jnp.float32)
final_state, obs_traj, reward_traj, cost_traj, done_traj, info_traj = scan_rollout(
env, rollout_key, state, params, actions
)
The same env contract works for the other physical models via the task-level wrapper:
Listing E.2: Task-level interface (Python)
from powerzoojax.tasks.tso import TSOTask
import jax
task = TSOTask()
env = task.make_env(split="iid")
params = task.episode_params(
"iid", episode_idx=0, n_episodes=1, max_steps=48,
29

strategy="seeded", seed=0,
)
obs, state = env.reset(jax.random.PRNGKey(0), params)
The five task classes live inpowerzoojax.tasks.{tso,dso,ders,gencos,dc_microgrid} and
all satisfy theTaskSpecProtocol (Listing E.3, abridged frompowerzoojax/tasks/base.py).
Listing E.3:TaskSpecProtocol surface (powerzoojax/tasks/base.py, abridged)
from typing import Any, Literal, Protocol, runtime_checkable
@runtime_checkable
class TaskSpec(Protocol):
"""Structural interface for the five benchmark tasks."""
task_name: str# "dso" | "tso" | "ders" | "gencos" | "
dc_microgrid"
default_splits: tuple[str, ...]# e.g. ("train", "iid", "load_stress", ...)
def make_env(self, split: str = "train") -> Any: ...
def episode_params(
self,
split: str, episode_idx: int, n_episodes: int, max_steps: int,
*, strategy: Literal["uniform", "seeded"] = "uniform", seed: int = 0,
) -> Any: ...
def rollout(self, env: Any, params: Any, key: Any, policy_fn: Any) -> Any: ...
def constraint_spec(self) -> "ConstraintSpec": ...
E.3 Reading a task config
Every benchmark task is specified by a Y AML file atbenchmarks/<task>/configs/task.yaml.
The TSO file is reproduced below in abridged form.
Listing E.4: TSO task config (benchmarks/tso/configs/task.yaml, abridged)
task: tso
case: case118# IEEE 118-bus / 186-line transmission case
n_units: 54# Thermal units committed by SCUC
max_steps: 48# 48 half-hour intervals = 24 h horizon
dt_hours: 0.5
data_source: gb# Real GB transmission demand & wind trace
gb_train_start: "2025-04-01"
gb_train_end: "2025-12-31"
gb_iid_start: "2026-01-01"
gb_iid_end: "2026-03-31"
reserve_margin_frac: 0.05# SCUC reserve margin
reward_scale: 0.0001# reward scaling factor
solver_mode: 1# DC-OPF solver mode
dcopf_max_iter: 200
dcopf_tol: 0.0001
forecast_horizon_steps: 4# 4 steps = 2 h; sets TSO obs to 410-dim (Section C.2)
baseline_set: [all_on, merit_order]
eval_splits: [train, iid, load_stress, line_tightening]
primary_split: iid
seeds: [0, 1, 2, 3, 4]
eval_episodes: 50
safety_thresholds:
reserve_shortfall_rate: 0.0
30

thermal_violation_rate: 0.0
E.4 Reading a training config
Training-side hyperparameters live next to the task config as train_<algo>.yaml. The TSO PPO
file is below; the master per-algorithm-per-task hyperparameter table is in Section F.2.
Listing E.5: TSO PPO config (benchmarks/tso/configs/train_ppo.yaml)
algo: ppo
total_timesteps: 20000000
num_envs: 256# GPU parallelism for case118 (54 units, 410-dim obs)
n_steps: 48# one episode per update
hidden_dims: [256, 256]
gamma: 0.995
gae_lambda: 0.95
lr: 0.0003
normalize_observations: true
wrapper: log# use'safe'for CMDP cost channel
eval_freq: 100000
eval_episodes: 8# in-training monitor only; benchmark eval uses task.yaml::
eval_episodes
record_eval_wall_time: true# logs per-eval walltime for cross-backend curves
E.5 CLI commands
The benchmark workflow exposes five entry points per task: baseline (run non-learning baselines),
train (run a learning algorithm), eval (evaluate a trained run on a split), summarize (rebuild result
summaries), andplots(regenerate paper figures). The TSO end-to-end example is
# Sanity check: run 5 seeds of the All-On and Merit-Order baselines.
python benchmarks/tso/run.py baseline --seeds 0,1,2,3,4
# Train PPO from train_ppo.yaml.
python benchmarks/tso/run.py train --algo ppo --seed 0
# Evaluate a trained run on the in-distribution split and the line-tightening stress split.
python benchmarks/tso/run.py eval --run-id <id> --split iid
python benchmarks/tso/run.py eval --run-id <id> --split line_tightening
# Rebuild result tables.
python benchmarks/tso/run.py summarize
# Regenerate figures from the result summary.
python benchmarks/tso/run.py plots
A lighter ad-hoc CLI lives atpython -m powerzoojaxfor preset and Y AML-driven runs:
python -m powerzoojax --list-presets
python -m powerzoojax --preset case5-economic-dispatch --seed 0
python -m powerzoojax --preset case5-economic-dispatch --config experiment.yaml --output
result.json
F Training Setup and Hyperparameters
This section gives the algorithm-choice rationale, full per-task per-algorithm hyperparameters, net-
work architectures, and evaluation protocol behind every reported number in the paper.
F.1 Algorithm choices
• TSO, DSO, DCMG (single-agent).PPO [ 36] as the unconstrained baseline; PPO-
Lagrangian as the safe-RL baseline on TSO and DSO, with Sauté PPO [ 43] additionally
reported on DSO. DSO and DCMG additionally train SAC [38]; on DCMG, SAC supplies
31

the appendix PPO-vs-SAC comparison in Section G.5 and the representative episode in
main-text Section 6.4.
• DERs (cooperative MARL).IPPO [ 37] with type-specific parameter sharing: the 12 agents
are partitioned into three types (4 batteries, 4 PV inverters, 4 flexible loads) and each type
carries its own actor-critic. IPPO-rs (reward-shaped IPPO with the voltage penalty doubled)
and IPPO-Lagrangian (separate cost critic per channel, one shared team-level dual variable)
are the safety variants.
• GenCos (competitive MARL).IPPO with full parameter sharing: a single ActorCritic
is shared across the five GenCos, where each agent is conditioned on its private 12-dim
observation and trained on its own profit reward. Truthful, uniform-mid, and max-markup
are reported as non-learning strategic baselines.
PPO-Lagrangian on both TSO and DSO uses a zero cost-budget threshold (bi = 0). The Sauté PPO
observation-augmentation budget, per-algorithm dual learning rates, and other safe-RL specifics are
listed with the master table in Section F.2.
TSO reward scaling.TSO trains with a reward-scaling factor αr = 10−4; the per-step reward seen
by the optimizer is
rt =−α r

C gen t +C startup t +C noload t  .(42)
The operating-cost numbers reported in main-text Section 6.3 and in Section G.2 are the unscaled
per-day operating cost.
F.2 Per-task per-algorithm hyperparameters
Table 8 summarises the key training hyperparameters.
Table 8: Master hyperparameter table. Columns: Ttot total environment steps (millions); Nenvs parallel
envs; ns steps-per-update; E PPO epochs (SAC update epochs); LR learning rate; HD hidden dims;
CL clip-eps; EC entropy coef;γdiscount;λGAE lambda. Optimizer is Adam throughout.
Task AlgoT tot Nenvs ns ELR HD CL ECγ λ
GenCos IPPO 5 256 48 4 3e-4 [128,128] 0.2 0.01 0.995 0.95
TSO PPO 20 256 48 4 3e-4 [256,256] 0.2 0.01 0.995 0.95
TSO PPO-Lag 20 256 48 4 5e-5 [256,256] 0.2 0.005 0.995 0.95
DSO PPO 3 128 48 4 3e-4 [128,128] 0.2 0.01 0.995 0.95
DSO SAC 3 64 — 1 3e-4 [128,128] — — 0.995 —
DSO Sauté PPO 3 128 48 4 3e-4 [128,128] 0.2 0.01 0.995 0.95
DSO PPO-Lag 3 128 48 4 3e-4 [128,128] 0.2 0.01 0.995 0.95
DERs IPPO 10 128 48 4 1e-4 [128,128] 0.2 0.02 0.995 0.95
DERs IPPO-rs 10 128 48 4 1e-4 [128,128] 0.2 0.01 0.995 0.95
DERs IPPO-Lag 10 128 48 4 1e-4 [128,128] 0.2 0.01 0.995 0.95
DCMG PPO 1 64 288 12 1e-4 [256,256] 0.1 0.001 0.99 0.95
DCMG SAC 1 64 — 2 3e-4 [256,256] — — 0.99 —
Safe-RL specifics not in the table: the dual learning rate is 5×10 −3 for TSO PPO-Lagrangian,
2×10 −5 for DSO PPO-Lagrangian, and 5×10 −5 for DERs IPPO-Lagrangian (three independent
cost channels, one shared team-level dual variable). The Sauté PPO observation-augmentation budget
on DSO is 192 violation-step-equivalents. IPPO-rs on DERs sets the voltage penalty to 8.0, twice the
4.0of IPPO.
F.3 Network architectures
• MLP backbone.Actor and critic are independent MLPs with hidden sizes from Table 8.
IPPO (GenCos, DERs) and the CMDP wrapper used for PPO-Lagrangian and Sauté PPO use
tanh activations; the rejax-based PPO and SAC baselines useswish and relu, respectively.
• Continuous policy heads.Plain PPO via rejax (TSO PPO, DSO PPO) emits an unbounded
diagonal Gaussian and clips the sampled action to the action box; the CMDP wrapper applies
a tanh squash to the action mean before adding diagonal Gaussian noise; rejax SAC (DSO
SAC, DCMG SAC) uses a tanh-squashed Gaussian whose support equals the action box;
32

IPPO (GenCos, DERs) emits an unbounded diagonal Gaussian whose samples are clipped
to [−1,1] before the environment step. DCMG PPO uses a bounded Beta policy over the
[0,1] 3 ×[−1,1]×[0,1]action box (Section C.5).
• Mixed action space (TSO).The policy emits a single 108-dim continuous head; the
environment decomposes the output into 54 sign-thresholded commitment intents and 54
dispatch preferences that bias the OPF cost intercept (Section C.2).
• MARL parameter sharing.DERs partitions the 12 agents by type (4 batteries, 4 PV
inverters, 4 flexible loads) and uses one shared actor-critic per type; GenCos shares one
actor-critic across the five generation companies.
• Observation normalization.The single-agent baselines train with running-mean / running-
std observation normalization; the MARL baselines (GenCos and DERs IPPO variants) train
on raw observations.
F.4 Seeds and evaluation protocol
Each task uses 5 seeds (0,1,2,3,4) and an evaluation budget of 10–50 episodes per seed (Table 6).
Episode-level metrics — operating cost, network loss, profit, and episode return — are reported as
across-seed mean ± 95% bootstrap CI; per-task comparisons on the primary metric use a paired
sign-flip permutation test on matched (seed, episode-index) pairs. Per-step rate metrics (thermal
overload, reserve shortfall, voltage violation, SLA deficit) are reported as across-seed mean rates; the
TSO reserve and thermal channels are reported under the zero-violation constraint of Section A.2.
Wall-clock time is recorded at every evaluation point so that learning curves can be aligned across
backends.
G Additional Empirical Results
This section reports the per-task supplementary tables and figures, one subsection per task (Sec-
tions G.1–G.5). Task definitions are in Section C; split meanings are in Table 7; per-task seed and
evaluation-episode budgets are in Table 6; the across-seed mean ± 95% bootstrap CI and the paired
sign-flip permutation test are defined in Section F.4.
G.1 GenCos
The task definition is given in Section C.1. We report the in-distribution baseline comparison (Table 9),
the cross-split profit table (Table 10), and a representative-episode behavior figure (Figure 11). Each
method aggregates 5 seeds and 30 evaluation episodes per seed with 95% bootstrap CIs (Section F.4).
The in-distribution mean total profit places IPPO ( GBP 395,030, 95% CI [291,174,499,652] )
strictly between Uniform-mid ( 302,972, [297,376,309,015] ) and Max-markup ( 597,864,
[587,181,609,873] ), and well above Truthful ( 6,934, [6,412,7,432] ). Under the paired sign-flip
permutation test of Section F.4 on 5seeds×30episodes= 150 matched (seed, episode-index) pairs,
the IPPO advantage over Truthful (+388,096) and Uniform-mid (+92,058) and the IPPO shortfall
against Max-markup ( −202,834) are all significant at p <10 −4. The cross-split table preserves
the same Truthful<Uniform-mid<IPPO<Max-markup ordering on the demand-shift and
renewable-shock splits.
Beyond the ranking, the in-distribution results show two behavioral differences from the heuristics.
First, the three non-learning baselines all bid the same shape and produce nearly identical Herfindahl–
Hirschman Index values ( 0.5664, 0.5663, 0.5662 for Truthful, Uniform-mid, and Max-markup),
while IPPO learns a less concentrated outcome ( HHI = 0.5384 ). Second, the ramp-binding rate
(the fraction of clearing steps in which the SCED ramp constraint is active) drops from 0.58 for
the heuristics to 0.35 under IPPO. Figure 11 resolves these two signals over a single representative
in-distribution episode: the top-left panel shows that IPPO clears at lower locational marginal prices
than Max-markup at high system load, the top-right panel tracks the per-step cumulative profit gap, the
bottom-left panel plots the HHI over the episode, and the bottom-right panel plots the ramp-binding
indicator.
33

Table 9: GenCos in-distribution baseline comparison oncase5, 5 seeds, 30 evaluation episodes per
seed. Higher total profit is better. Profit is the across-seed mean with a 95% bootstrap CI (Section F.4).
HHI denotes the Herfindahl–Hirschman Index of cleared-energy shares.
Method Profit mean (GBP) Profit 95% CI (GBP) HHI
Truthful 6,934[6,412,7,432]0.5664
Uniform-mid 302,972[297,376,309,015]0.5663
IPPO 395,030[291,174,499,652]0.5384
Max-markup 597,864[587,181,609,873]0.5662
Table 10: GenCos total-profit mean (GBP) across splits. Each entry aggregates 5 seeds and 30
evaluation episodes per seed.
Split Truthful Uniform-mid IPPO Max-markup
In-distribution 6,934 302,972 395,030 597,864
Demand shift 9,634 354,978 475,620 702,906
Renewable shock 7,977 329,873 434,642 650,409
400 600 800 1000
T otal load (MW)
20
40
60Mean LMP ($/MWh)
0 10 20 30 40
0
100000
200000
300000
400000
500000Cumulative profit ($)
0 10 20 30 40
30-min interval
0.0
0.2
0.4
0.6
0.8
1.0HHI
0 10 20 30 40
30-min interval
0.0
0.2
0.4
0.6
0.8
1.0Ramp binding rate
Truthful Uniform Mid Max Markup IPPO Uniform dispatch Monopoly
Figure 11: GenCos behavior on a representative in-distribution episode under the same physical load.
Top-left: locational marginal price as a function of system load. Top-right: cumulative profit per
step. Bottom-left: Herfindahl–Hirschman Index of cleared-energy shares. Bottom-right: per-step
ramp-binding indicator.
G.2 TSO
Table 11 reports operating cost and the two per-step violation rates under the zero-violation constraint
of Section A.2. No method satisfies it on both channels: PPO-Lagrangian and All-On record zero
reserve shortfall, while every method records a non-zero thermal-overload rate. The paired sign-flip
permutation test on per-episode operating cost (Section F.4,n= 250 pairs, p <10−4 for the reported
comparisons) confirms that the cost differences are significant. The task card and 24-hour SCUC
formulation are described in Section C.2; Figure 12 decomposes the cost-versus-violation pattern
into worst-rate and per-channel views, separating the reserve channel (PPO-Lagrangian and All-On
at zero) from the thermal channel (every method above zero).
34

Table 11: TSO cost and safety results. Operating cost is reported per 24-hour episode in £M; reserve
and thermal columns are per-step violation rates.
Split Method Operating cost (£M/day) Reserve-shortfall rate Thermal-overload rate
in-distribution PPO 1.58 0.0728 0.3554
in-distribution Merit Order 2.89 0.0096 0.1242
in-distribution PPO-Lag 3.50 0.0000 0.0593
in-distribution All-On 4.34 0.0000 0.0346
line-tightening PPO 1.57 0.0547 0.4932
line-tightening Merit Order 2.89 0.0096 0.3371
line-tightening PPO-Lag 3.50 0.0000 0.1560
line-tightening All-On 4.34 0.0000 0.0504
load-stress PPO 1.82 0.0894 0.4118
load-stress Merit Order 3.31 0.0183 0.1675
load-stress PPO-Lag 3.78 0.0000 0.0889
load-stress All-On 4.68 0.0000 0.0754
1.5 2.0 2.5 3.0 3.5 4.0
T otal operating cost (million GBP)
0.0
0.1
0.2
0.3Max safety violation rate
PPO
Merit Order PPO-Lag All-On
0.0
0.1
0.2
0.3Violation rate
Hard-feasible band PPO Merit Order PPO-Lag All-On Reserve shortfall Thermal violation
Figure 12: TSO cost–safety summary. Left: total operating cost vs the worst safety-violation rate (the
maximum of the reserve-shortfall and thermal-overload rates). Right: the same methods separated by
violation channel, showing that the reserve channel is satisfied for PPO-Lagrangian and All-On while
the thermal channel is not satisfied for any method.
Figure 13 expands the method-level numbers in Table 11 into per-episode dispersion. PPO has the
lowest mean operating cost (£1.58M per 24-hour episode) but a wide spread along the thermal-cost
axis: its mean per-episode total thermal cost is 247.67, and the worst-decile episodes carry thermal
cost more than an order of magnitude above this mean. PPO-Lagrangian shifts the cloud toward
higher cost (£3.50M per episode) while compressing mean thermal cost to 1.76, roughly two orders
of magnitude below PPO. Merit Order and All-On occupy the high-cost low-thermal corner.
Figure 14 complements Table 11 with train-split checkpoint monitoring curves over the 20 M-step
training budget. The curves aggregate the five seeds and show smoothed mean ± one standard
deviation over sparse greedy-evaluation checkpoints. PPO drives operating cost down toward its held-
out in-distribution value of £1.58M per episode (Table 11), but its safety panels move in the opposite
direction, with both reserve-shortfall and thermal-overload incidence rising over training. PPO-
Lagrangian holds reserve-shortfall incidence at zero throughout and lowers final thermal-overload
incidence well below PPO, while its operating cost stays above both PPO and the merit-order
reference. The learning dynamics therefore explain how the cost–safety frontier is reached.
35

£1.0M £2.0M £3.0M £4.0M £5.0M £6.0M £7.0M
T otal operating cost (£)
0
10−2
10−1
100
101
102
103
T otal thermal-violation cost (symlog)
PPO (n=250)
PPO-Lag (n=250)
Merit-order (n=250)
All-on (n=250)
Figure 13: TSO per-episode operating cost vs thermal-overload cost on the in-distribution split (4
algorithms × 5 seeds × 50 episodes = 1,000 points). Marker area is proportional to the per-episode
thermal-violation rate; the ellipse around each method covers its 95% covariance region.
0 5 10 15 20
Env. steps (M)
2
3
4
5Cost (GBP M / episode)
0 5 10 15 20
Env. steps (M)
0.00
0.05
0.10
0.15
0.20Reserve rate
0 5 10 15 20
Env. steps (M)
0.0
0.2
0.4
0.6Thermal rate
PPO (5 seeds) PPO-Lag (5 seeds) All-On Merit Order
Figure 14: TSO train-split checkpoint monitor over 20 M environment steps. Panels show evaluation
operating cost, reserve-shortfall incidence, and thermal-overload incidence. Curves are smoothed
means over five seeds; shaded bands show one standard deviation.
G.3 DSO
DSO reports raw in-distribution physical metrics over 5 seeds × 50 evaluation episodes; the voltage
channel is reported under Form 1 with bi=0 (Section A.2). Loss reduction in Table 12 is computed
relative to no control.
Table 12: DSO in-distribution physical metrics. Lower total network loss is better; the voltage column
is the per-step count of buses outside the[0.94,1.06]p.u. band.
Method Total loss (MWh) V oltage violations / step Loss reduction
PPO 1.9355 0.00033 34.45%
Sauté PPO 1.9370 0.00292 34.35%
SAC 2.3178 0.05475 20.54%
PPO-Lag 2.4108 0.01733 15.84%
Droop 2.8593 0.07042 0.74%
No control 2.8909 0.20667 0.00%
Figure 15 visualizes the three columns of Table 12 as bar panels.
Figure 17 expands Table 12 into per-episode behavior distributions over the six methods, with each
box overlaid by the 250 individual episodes so distributional tails remain visible. PPO and Sauté PPO
36

No control
Droop SAC PPO-LagSauté PPO PPO
0
1
2
3T otal loss (MWh)
No control
Droop SAC PPO-LagSauté PPO PPO
0.00
0.05
0.10
0.15
0.20Voltage violations / step
No control
Droop SAC PPO-LagSauté PPO PPO
0
10
20
30Loss reduction (%)
Figure 15: DSO in-distribution physical metrics. Panels report total network loss, voltage-violation
count per step, and loss reduction relative to no control.
0 1.0M 2.0M 3.0M
Environment steps
0.6
0.5
0.4
Episode total reward
0 1.0M 2.0M 3.0M
Environment steps
0.0
0.1
0.2
0.3Voltage violations / step
0 1.0M 2.0M 3.0M
Environment steps
0
50
100
150Lagrange
PPO SAC Saute-PPO PPO-Lag CMDP threshold  cap = exp(5)
Figure 16: DSO learning curves over 3 M environment steps. Left: episode total reward across the
four learned algorithms. Middle: per-step voltage-violation count. Right: PPO-Lagrangian Lagrange
multiplierλ.
use roughly 17 MWh per day of curtailment and 11 MWh per day of shifting, achieving close to 30%
peak shaving with voltage violations driven to near zero on most episodes; tail steps are still visible
above zero in the bottom-right panel. PPO-Lagrangian curtails and shifts substantially less, yet has a
heavier voltage-violation tail than PPO. SAC reaches lower total loss than PPO-Lagrangian on every
paired episode but carries the highest per-step voltage-violation rate of the four learned methods.
Droop’s curtailment and shifting stay well below 1 MWh per day, an order of magnitude under the
four learned policies.
PPO-Lagrangian training dynamics.Under no control the in-distribution DSO carries roughly
0.21 voltage violations per step (Table 12). PPO and Sauté PPO drive the in-distribution rate to near
zero within the first half of the training budget; once the per-step rate is small, the constraint signal
that the dual update consumes becomes sparse, and PPO-Lagrangian converges to a conservative
region with low loss reduction and a heavier violation tail than PPO. The corresponding learning
curves are shown in Figure 16.
37

0 5 10 15
Curtailment (MWh / day)
PPO
Sauté-PPO
PPO-Lag
SAC
Droop
No-control
0 5 10 15
Shift (MWh / day)
PPO
Sauté-PPO
PPO-Lag
SAC
Droop
No-control
−10 0 10 20 30 40
Peak shaving (%)
PPO
Sauté-PPO
PPO-Lag
SAC
Droop
No-control
0.00 0.25 0.50 0.75 1.00 1.25 1.50
Voltage violations (per step)
PPO
Sauté-PPO
PPO-Lag
SAC
Droop
No-control
Figure 17: DSO per-episode in-distribution behavior distributions over 6 algorithms × 5 seeds ×
50 episodes. Each panel reports a single behavior metric; boxes are overlaid by jittered individual
episodes so distributional tails (especially the voltage-violation panel) remain visible.
G.4 DERs
On the in-distribution split, every learned and non-learning method reports zero or near-zero voltage
violations (Table 13). Across all five algorithms and all five evaluation splits, the maximum bus
voltage stays at the slack reference Vmax = 1.000 p.u., so the safe band is exercised only on its
under-voltage side and the operating regime never enters PV-driven over-voltage; this remains true
under the PV-shift split, where the PV bundle capacity is doubled. The voltage-tightening split
(Table 14), which narrows the band from [0.94,1.06] p.u. to [0.96,1.04] p.u., is therefore the split on
which the methods separate on safety.
For the in-distribution loss test, IPPO and IPPO-rs reduce active-power loss to0.1974 MW versus
0.2052 MW for no control — a 3.8% reduction — and beat both no control and voltage droop
at p <10 −4 under the paired sign-flip test of Section F.4. IPPO-Lagrangian has higher loss
(0.2051 MW): it is statistically indistinguishable from no control on the loss test ( p=0.87) and is
statistically worse than voltage droop (mean difference+0.0020MW,p <10 −4).
Under tightening, IPPO and IPPO-rs cut the violation count by 44% relative to no control ( 4.91
vs 8.73 steps per episode); voltage droop cuts it by 32% (5.97); IPPO-Lagrangian cuts it by 9%
(7.94), so the constrained variant trails IPPO and IPPO-rs on both the in-distribution loss test and the
tightening split. The load-stress split shows the same ordering qualitatively: per-episode violation
steps are 0.23 for IPPO and IPPO-rs, 0.33 for voltage droop, 0.83 for IPPO-Lagrangian, and 0.93 for
no control. Figure 18 traces battery state of charge, battery reactive-power command, photovoltaic
curtailment, photovoltaic reactive-power command, flexible-load action, and active-power loss for
each policy on the same in-distribution episode, showing that IPPO and IPPO-rs realize their loss
reduction through coordinated reactive-power dispatch rather than active-power curtailment, while
IPPO-Lagrangian holds the cost critic near its budget and dispatches less aggressively on both
channels.
38

Table 13: DERs in-distribution results. Lower active-power loss is better. Loss values are mean
across5seeds×30episodes.
Method Active loss (MW) Violation steps Violation rate
IPPO-rs 0.1974 0.00 0.0000
IPPO 0.1974 0.00 0.0000
V oltage droop 0.2031 0.00 0.0000
IPPO-Lag 0.2051 0.0067 0.00014
No control 0.2052 0.00 0.0000
Table 14: DERs voltage-tightening stress split (band tightened from [0.94,1.06] to [0.96,1.04] p.u.).
Violation steps are per episode; rates use the 48-step horizon as denominator. Active loss matches the
in-distribution column because tightening changes only the constraint band, not dispatch decisions.
Method Active loss (MW) Violation steps Violation rate
IPPO-rs 0.1974 4.91 0.1022
IPPO 0.1974 4.91 0.1024
V oltage droop 0.2031 5.97 0.1243
IPPO-Lag 0.2051 7.94 0.1654
No control 0.2052 8.73 0.1819
0.0
0.2
0.4
0.6
0.8SOC
0.0
0.2
0.4
0.6Q  [MVAr]
0.00
0.05
0.10
0.15MW
0.00
0.25
0.50
0.75Q  [MVAr]
0 3 6 9 12 15 18 21 24
Hour of day
−0.2
0.0
0.2
0.4
MW
0 3 6 9 12 15 18 21 24
Hour of day
0.0
0.2
0.4
0.6MW
No control Voltage droop IPPO IPPO-rs IPPO-Lag PV active (cf > 0.02)
Figure 18: DERs schedules on a single in-distribution episode. Panels compare battery state of
charge, battery reactive power commands, PV curtailment, PV reactive-power commands, flexible
load actions, and active power loss across IPPO, IPPO-rs, IPPO-Lagrangian, voltage droop, and no
control.
G.5 DCMG
DCMG (Section C.5) is reported on the in-distribution split with all three cost channels (SLA, over-
temperature, power deficit) at a zero threshold. Episode returns are in Table 15. Figure 19 shows
a representative SAC dispatch on one in-distribution episode; the same SAC trajectory underlies
main-text Section 6.4.
39

PPO records zero violations on all three channels; SAC and the three heuristic methods show SLA
rates of10 −7 to10 −6 and zero on the other two channels.
Table 15: DCMG in-distribution results. Higher episode return is better. SLA rate is the per-step
rate of expired tasks; spill cost is the per-step over-generation penalty. The power-deficit and
over-temperature rates are0for every method and are not shown.
Method Episode return SLA rate Spill cost
SAC−2594.59 4.17×10 −7 9.05×10−5
PPO−2845.29 0 1.03×10 −3
No control−3110.68 1.11×10 −6 0
Rule-based−5226.24 8.33×10 −7 4.58×10−4
Max renewable−6010.68 1.39×10 −7 6.30×10−3
0 6 12 18
Hour of day
0.6
0.8
1.0Load [MW]
0 6 12 18
Hour of day
0.5
0.0
0.5
1.0
Power [MW]
0 6 12 18
Hour of day
0.2
0.4
0.6
0.8SoC
PV CF
0
25
50
75
100
Price [$/MWh]
DC load
PV avail.
Net load
Grid import
Diesel gen.
Batt. discharge
Batt. charge
Battery SoC
SoC bounds
Grid price
Figure 19: Representative DCMG dispatch from the SAC policy on one in-distribution episode,
displayed as 30-minute means for readability.Left:real GB solar capacity factor and the data center
IT load.Middle:net load after PV , grid import, diesel output, and battery charge/discharge.Right:
battery state of charge with SoC bounds, alongside the GB MID grid price.
H Execution Scaling and Backend Comparison
This section decomposes the suite-level speed result of Section 6.1 along three axes: backend
architecture, parallelism range, and wall-clock learning efficiency.
H.1 Backend decomposition atN env = 212
The three training backends differ in where the environment transition runs. SB3 runs a PyTorch
policy on the GPU and the PowerZooPy environment on the CPU. SBX runs a JAX policy and
optimizer on the GPU but keeps the same CPU-hosted PowerZooPy environment. PowerZooJax
runs the policy, optimizer, and environment transition end-to-end inside a compiled JAX program
on the GPU. Table 16 decomposes throughput at Nenv = 212 across these three stacks: the SB3-to-
SBX delta isolates the policy-side acceleration (PyTorch → JAX), and the SBX-to-PowerZooJax
delta, reported in the rightmost column “ × vs SBX”, isolates the environment-side acceleration.
The environment-side gain alone is 1,145× on GenCos and 2,040× on DERs, both of which call
CPU-hosted OPF or power-flow solvers in PowerZooPy that PowerZooJax fuses into the compiled
JAX graph. The gain is smaller on DSO ( 39×) and TSO ( 33×), whose CPU steps already run
JAX-friendly kernels rather than an external solver. DCMG (22×) is the smallest case: its step is
dominated by small arithmetic device updates without an external solver call, so the CPU-hosted
environment is already fast.
H.2 Per-task throughput scaling
Figure 20 reports throughput against parallelism for DCMG, DSO, and DERs. PowerZooJax
JAX/GPU is swept over nenv∈ {16,32,64,128,256} on all three; SB3/CUDA is overlaid for
40

Table 16: Throughput at Nenv = 2 12 parallel environments, with the environment-side speedup
isolated. The headline speedup against the slower CPU baseline is in main-text Table 2.
Task PowerZooJax SBX/CUDA SB3/CUDA×vs SBX
GenCos 506,134 442 244 1,145×
DERs 414,506 203 233 2,040×
DSO 134,660 3,435 2,207 39×
TSO 53,724 1,649 411 33×
DCMG 25,132 1,167 1,298 22×
16 32 64 128 256
Parallel envs
1K
10K
100KSteady-state env steps / second
308K
14.1K
7×
DCMG
16 32 64 128 256
Parallel envs
388K
5.3K
39×
DSO
16 32 64 128 256
Parallel envs
284K
DERs
PowerZooJax (JAX/GPU) SB3/CUDA (SubprocVecEnv)
Figure 20: Per-task throughput scaling. PowerZooJax JAX/GPU is plotted over nenv∈
{16,32,64,128,256} for every task; SB3/CUDA is overlaid where its SubprocVecEnv backend
completes (through nenv= 64 for DCMG, through nenv= 128 for DSO; DERs has no paired SB3
sweep). Endpoint labels mark the JAX/GPU and SB3/CUDA throughput at the right end of each
curve; arrows mark the JAX-vs-SB3 ratio at the top of each matched range.
DCMG and DSO under the same warm-up and measurement protocol over the range where its
SubprocVecEnv backend completes. JAX/GPU throughput rises with parallelism on every task:
DCMG from 32.1k to 307.7k env steps/s, DSO from 25.0k to 388.4k, and DERs from 21.6k to
283.8k. The matched-range speedup over SB3/CUDA reaches 7.4× for DCMG (at nenv= 64 ) and
39× for DSO (at nenv= 128 ), the largest parallelism each SB3 path completes; SB3 throughput
tops out at 14.1k on DCMG and 5.3k on DSO. The high-parallel endpoint in Table 16 reports
25.1k, 134.7k, and 414.5k at Nenv = 212 for DCMG, DSO, and DERs respectively under a separate
measurement protocol.
H.3 First-compile cost
The scaling sweeps record the first JAX compilation separately from the steady-state update loop.
Compile cost is single-digit seconds for the three tasks in Figure 20 (Table 17); subsequent updates
run from the cached compiled program.
Table 17: First JAX compilation time in task-specific scaling sweeps. Values are means over seeds.
Task Measured nenv range Compile time JAX throughput at nenv=256
DCMG 16–256 8.2 s 307.7k steps/s
DSO 16–256 2.9 s 388.4k steps/s
DERs 16–256 2.1 s 283.8k steps/s
H.4 Wall-clock learning curves for DSO and TSO
For DSO and TSO, all three backends (PowerZooJax, SBX/CUDA, SB3/CUDA) ran to the same
training budget and recorded per-evaluation-point wall-clock timestamps, which allows learning
curves to be plotted against time rather than environment steps. Figure 21 traces evaluation return
against elapsed time for the three backends on these two tasks at the matched budgets of main-text
41

1s 10s 1m 10m 1h
Wall-clock time
−0.55
−0.50
−0.45
−0.40
−0.35Eval return
DSO
10s 1m 10m 1h
Wall-clock time
−400
−300
−200
−100Eval return
TSO
PowerZooJax GPU SB3 CUDA SBX CUDA
Figure 21: Evaluation return against elapsed wall-clock time for DSO and TSO across PowerZooJax,
SBX/CUDA, and SB3/CUDA.
Table 2. The PowerZooJax run reaches the same training budget in a fraction of the time required by
either CPU-hosted backend.
42
