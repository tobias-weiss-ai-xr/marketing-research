---
title: 'DumpsterCluster: From Dumpster Diving to Serving LLaMA-70B on $60 GPUs'
url: https://arxiv.org/abs/2608.14614
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Zeyu Cao
- Xuan Guo
- Cheng Zhang
- Cheuk Hang Lau
- Ilia Shumailov
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.14614
pages: 25
chars: 79808
fetched_at: '2026-11-08T13:23:32+00:00'
kb_version: 1
---

# DumpsterCluster: From Dumpster Diving to Serving LLaMA-70B on $60 GPUs

DumpsterCluster: From Dumpster Diving
to Serving LLaMA-70B on $60 GPUs
A Preprint
Zeyu Cao1 Xuan Guo1,3 Cheng Zhang
Cheuk Hang Lau3 Ilia Shumailov2 Yiren Zhao1
1University of Cambridge 2University of Oxford 3Quettaflop AI
August 18, 2026
Abstract
As AI datacenters retire functional GPUs, vast quantities of still capable accelerators
enter secondary markets. This paper investigates whether these “retired” GPUs can find
a productive afterlife to form aDumpsterClusterthat can serve modern LLM inference,
and under what conditions such repurposing is economically viable and environmentally
sustainable. We physically built a 128-GPU DumpsterCluster from scratch using only
second-hand components and ran it for one year. At current market prices ($22K for the
DumpsterCluster vs. $600K for an 8-GPU B200 system), the economic advantages are
substantial. Through pipeline-parallel optimizations, our V100 based DumpsterCluster
achieves competitive LLaMA-70B throughput, validating production viability. However,
our deployment reveals critical context dependencies. Older GPUs consume significantly
more energy per token, making total cost of ownership favorable only in regions with
inexpensive electricity. Under grid-average carbon intensity, second-hand systems can
produce approximately4× higher total carbon emissions per token for 8B models, and over
40× for 70B models, compared to current-generation hardware. These findings show that
GPU afterlife is not universally sustainable – hardware repurposing must be strategically
coupled with low carbon energy sources. When deployed in regions with favourable energy
economics and clean electricity, second-hand GPUs offer a viable pathway for expanding AI
capacity while advancing affordability, energy security, and environmental responsibility.
1 Introduction
The rapid rise of large-scale AI models has triggered unprecedented demand for computational infrastructure
[1, 2]. Hardware vendors have responded with accelerated GPU release cycles [3, 4], each generation offering
improved performance but requiring priority access to constrained semiconductor manufacturing capacity.
This continuous upgrade cycle has created a peculiar phenomenon: datacenters regularly retire still-functional
GPUs to make room for newer hardware, creating a growing secondary market of “discarded” but capable
accelerators.
This pattern raises concerns about sustainability, supply-chain security, and accessibility. From a sustainability
perspective, continual manufacture of new accelerators and premature retirement of functional hardware
arXiv:2608.14614v1  [cs.LG]  10 Jul 2026

Cao et al. DumpsterCluster
impose substantial embodied carbon costs from semiconductor fabrication while contributing to mounting
electronic waste. From a supply-chain perspective, the concentration of advanced GPU production among few
vendors and foundries has made access to frontier hardware increasingly constrained, with many organizations
facing high prices, long procurement delays, and structural dependence on fragile supply chains. From an
accessibility perspective, the escalating costs of current-generation systems – a single 8-GPU B200 node costs
$600K – place state-of-the-art AI infrastructure beyond reach for many researchers and organizations. These
pressures motivate a simple but underexplored alternative: giving retired GPUs a productive afterlife by
repurposing them for modern AI workloads. Such devices are available on secondary markets at a fraction
of new-hardware costs, yet remain computationally capable. This raises a fundamental question: Can
second-hand GPUs form aDumpsterClusterto support LLM inference in a way that is economically viable,
resilient to supply constraints, and genuinely compatible with environmental and energy-security objectives?
To answer this, we designed and built a 128-GPU DumpsterCluster from the ground up using entirely
second-hand components – not only GPU accelerators, but also CPU processors, memory modules, and
motherboards sourced from the secondary market. We deployed this cluster for one year, serving real LLM
inference workloads. The complete hardware configuration from the real build is presented in Figure 3. Each
rack-level node comprises pre-owned motherboards, CPUs, RAM, and NVIDIA V100 GPUs. On the software
side, we developed a custom LLM serving engine in Rust implementing a device-level pipeline parallelism
strategy not found in commodity serving systems. We empirically demonstrate that this serving approach
enables older GPUs, despite their restricted HBM capacity, bandwidth, and GPU-to-GPU interconnect
speeds, to effectively execute inference for state-of-the-art LLMs. Tokens Per Second (TPS) scales linearly
with device count, enabling cost-effective inference compared to modern GPUs such as H100s. In this paper,
we present the first in-depth analysis of the economic and environmental trade-offs of repurposing retired
hardware for LLM inference, revealing critical dependencies on electricity cost and carbon intensity that
determine when second-hand GPU deployment is truly economically and environmentally sustainable.
2 Method
2.1 The advantages and drawbacks of second-hand devices
We mostly consider second-hand hardware devices that are batch-deployed and retired from commercial data
centers after they are superseded by a new generation of hardware. In 2023 alone, NVIDIA shipped more
than 3 million GPU chips to data centers [5]. Many of these data center GPUs are scheduled to be phased
out approximately every three years to make way for new product release cycles, resulting in millions of
second-hand GPUs entering the market with each cycle.
In this study, we focus primarily on NVIDIA V100 GPUs, which are two generations behind the widely
deployed Hopper series (e.g. H100 and H200) and three generations older than the Blackwell (e.g. B100
and B200). V100 GPUs are now widely available on the second-hand market after multiple waves of
decommission [6–9]. The primary advantages of using such devices are their cost-effectiveness and reduced
amortized embodied carbon. In addition, as LLM model serving becomes a major workload, reusing second-
hand hardware also contributes to circular economy and addresses the e-waste concern [10]. However, there
are also significant drawbacks of pre-owned devices, including their potentially high operational carbon and
costs from naive deployments, as well as concerns regarding their reliability.
Price competitivenessSecond-hand GPUs offer great price competitiveness. Today’s second-hand market
prices for V100 16GB cards are now typically$60if one purchases in batch, making them more than100×
cheaper than B200 GPUs (an 8x B200 system is around$600K). We acquired second-hand V100s and also
sourced second-hand CPUs and motherboards to construct a compute DumpsterCluster using these devices.
The cost of assembling this 128-V100 pod, composed entirely of used hardware, including all peripherals,
is$32K (as per March 2026 it further depreciated to$22K). Starting from this hardware configuration,
we designed a highly optimized LLM serving engine. Our approach demonstrates that, despite individual
V100 GPUs being significantly less powerful than H100/B200 GPUs according to datasheet specifications,
careful software engineering can enable scaled-out computation with used GPUs to deliver LLM inference
performance.
To quantify the price depreciation patterns, we collected second-hand market prices for NVIDIA V100 16GB
and A100 40GB GPUs over time, relative to their release dates (May 2018 and May 2020, respectively).
We fitted these depreciation curves using a stretched exponential decay model:P (t) = P0·e−(t/τ) β , where
P0 is the initial launch price,τ represents the characteristic time scale, andβ is the stretching exponent
2

Cao et al. DumpsterCluster
0 12 24 36 48 60 72 84 96
102
103
104
$10k
$170 $130
$85
$60
Months since release
Price (USD, log scale)
V100 16GB
(a) V100 16GB
0 12 24 36 48 60 72
103
104 $12k
$4.3k
$2.6k$1.9k
Months since release
Price (USD, log scale)
A100 40GB
(b) A100 40GB
Figure 1: Second-hand GPU price depreciation over time relative to their release dates. V100 16GB was
released in May 2018 with a launch price of $10,000, while A100 40GB was released in May 2020 at $12,000.
Data points show actual market prices from eBay listings. Solid curves show fitted stretched exponential
decay models. V100 prices drop to $60 (99.4% depreciation) and A100 to $1,900 (84.2% depreciation) by
March 2026. Log scale on the y-axis reveals the accelerating depreciation pattern.
that captures the rate of depreciation acceleration. For V100, we obtainedτ = 48.3months and β = 2.43
(R2=1.000); for A100,τ = 61.7months and β = 4.66(R 2=0.9997). The values ofβ >1indicate accelerating
depreciation, meaning GPUs lose value at an increasing rate as they age; this is a pattern consistent with
technology obsolescence in the face of rapid hardware innovation cycles. Figure 1 shows the fitted curves
on a logarithmic price scale, revealing the non-linear decay pattern. It is worth noting that batch purchase
pricing data is unavailable when these devices are actively deployed in hyperscaler datacenters. Consequently,
the x-axis in Figure 1 shows data points only after 3-4 years from release, when GPUs are phased out from
large-scale production deployments.
Amortized/annualized embodied carbonRe-utilizing second-hand GPUs offers a great reduction in the
embodied carbon (Cem). This is because the manufacture of GPUs and host servers is an energy-intensive
process that can result in a high volume of embodied carbon [11–15], as shown in Table 1. By re-deploying
second-hand GPUs as a DumpsterCluster, this effectively offers a reduction in the annualized embodied
carbon C annual em (T )(Equation (7)) by extending their life span. Furthermore, by reusing GPUs, our approach
can reduce the demand for manufacturing new GPUs of equivalent capacity, further reducingCem by means
of circular economy. As a secondary benefit, this reduced demand could also help alleviate the current GPU
shortage. Deeper analysis of the modern accelerator supply chain is beyond the scope of this paper.
Operational carbon and costsSecond-hand GPUs may incur higher operational carbon (Copt, Equation (2))
emissions and costs if deployed without optimization. Previous-generation GPUs are manufactured with older
silicon technology nodes; for example, V100 uses TSMC 12nm while H100 uses TSMC N4. Later-generation
GPUs are also equipped with higher-bandwidth HBM memory, V100 utilizes HBM2 whereas H100 deploys
HBM3. Advances in manufacturing nodes offer higher transistor density, improving energy efficiency, while
larger and higher-bandwidth HBM also contributes to reduced operational costs. These energy efficiency
improvements reduce both operational carbon and costs for newer-generation GPUs. Furthermore, operational
monetary cost is primarily determined by energy supply pricing, while operational carbon depends on the
energy mix. Lower carbon footprint requires energy mixes dominated by non-fossil fuel sources. We made an
interesting observation in this paper: cost-effectiveness and environmental sustainability both depend on grid
pricing and energy supply mix, as inexpensive energy from low carbon sources is a critical component for
making inference serving on second-hand devices both economically and environmentally viable.
Reliability of used hardwareSecond-hand GPUs can exhibit increased fault rates. Since used GPUs
have typically been deployed for a full product cycle, approximately 3 years from launch to decommission1,
hardware reliability may be degraded. Previous analyses of GPU reliability [16, 17] indicate that most
reliability issues originate from the GPU devices themselves, and system reliability can therefore decrease
1Though newer-generation GPUs are launched on roughly 2-year cycles, the typical deployment period from
shipment to decommissioning is around 3 years, aligned with warranty periods.
3

Cao et al. DumpsterCluster
ShareGPTPrefill-heavyDecode-heavy
103
104
105
Tokens per Second (TPS)
1 H100 1 A100 4 V100
128 V100 1 B200 ShareGPT
Prefill-heavy Decode-heavy
(a) LLaMA 3.1-8B
ShareGPTPrefill-heavyDecode-heavy
103
104
8x H100 8x A100 16 V100
128 V100 8x B200 ShareGPT
Prefill-heavy Decode-heavy
(b) LLaMA 3.1-70B
Configuration Price Peak TPS/$ Notes
8B 70B
1 H100 $18.5K 1.59 - Secondary market, GPU only
8x H100 (pod) $148K - 0.13 Secondary market, GPUs only
1 A100 $5.8K 2.15 - Secondary market, GPU only
8x A100 (pod) $46.4K - 0.19 Secondary market, GPUs only
1 B200 $75K 0.84 - Derived from full system MSRP
8x B200 (pod) $600K - 0.06 Full system MSRP
4 V100 (pod) $240 29.16 - Secondary market, GPUs only
16 V100 (pod) $960 - 0.20 Secondary market, GPUs only
128 V100 (pod) $7.68K 29.16 0.20 GPUs only (Full system with
peripherals is≈$22K)
Figure 2: Tokens per Second (TPS) for B200, H100, A100, and V100 devices evaluated across various
workloads. Hardware configurations range from single instances to full 128-device DumpsterCluster pods,
with associated capital costs and calculated Peak TPS per dollar included for economic comparison. The
monetary cost used in calculation here contains only capital expenditure and does not take operational
expenditure into account.
with extended GPU lifecycles. However, this can be addressed proactively through hardware binning:
stress-testing used GPUs before deployment and removing units unsuitable for the target workload. In our
cluster construction, we conducted this binning process to ensure reliability. Additionally, we implement
software-level mitigation strategies. We employ redundant capacity with load balancing techniques to improve
overall system reliability, and in practice we provision10%additional GPU devices to ensure cluster reliability.
2.2 Building a GPU DumpsterCluster
To demonstrate the potential of second-hand GPUs in serving LLMs, we assembled a GPU DumpsterCluster
with used V100 GPUs as illustrated in Figure 3, where images are taken from our actual hardware fleet. The
pod consisted of128V100 GPU devices, acquired at approximately$200per unit 2.
The GPUs are mounted on specialized SXM baseboards that facilitate300GB/s bidirectional NVLink
connectivity between sets of four GPUs. The SXM baseboard is equipped with two PCIe 3.0 switches, each
2The acquisition of these GPU devices was in May 2024 at$215and July 2024 at$170, the current price of these
V100 is at around$50to$60.
4

Cao et al. DumpsterCluster
Server Server Server Server
Switch
x16
Server
x4 uplink
GPU GPU
GPU GPU
NVLink
PCIE
Switch
PCIE
Switch
CPU
CPU
NIC
NIC
GPU GPU
GPU GPU
NVLink
PCIE
Switch
PCIE
Switch
NIC
NIC
NIC
SXM Baseboard SXM Baseboard
SXM Baseboard
GPU
128V100 GPU POD
Figure 3: An illustration and real pictures of our used GPU pod configuration. The server topology and pod
topology are shown with key components illustrated on the top. Each server node contains 8 V100 GPUs,
and the GPU server pod contains 16 server nodes, providing a total of 128 V100 GPUs. Our cluster has two
of these pods.
linking two V100 GPUs with a single100G Connect-X 5 network interface card (NIC). Each server node
consists of two such baseboards, which are individually connected to a Numa Node on a Dual Socket server
board with an Intel Xeon 6138 processor and256GB DRAM. All 4 NICs are linked to a100Gbps RDMA
fabric, and there is an additional25Gbps Connectx-4 NIC directly attached to CPU1 to handle management
and service traffic. The detailed topology and configuration are shown in Figure 3. In total, the construction
of the GPU pod costs around$32, 000in 2024, including all server and switch components, which is roughly
the same price as a single H100 GPU device at its MSRP in 2024. If one would like to replicate such a
GPU cluster now in March 2026, it would cost only around$22, 000. Also, not only the GPUs but all
other components, such as motherboards and network interface cards, were purchased second-hand. The
entire server pod consists solely of refurbished devices. Because hardware prices are influenced by market
conditions and the depreciation of older GPU devices, we use the prices available to us at the time of writing
– specifically, those observed in March 2026 – for all subsequent analysis and evaluation.
2.3 Scaled-out parallelization for the DumpsterCluster
Older GPU devices commonly face the following constraints:
•Limited HBM memory capacity;
•Limited HBM memory bandwidth;
•Reduced computing capability (lower FLOPs/second);
•Smaller inter-GPU communication bandwidth (slower NVLink).
The constraints of HBM memory and computing capability can be mitigated with scaled-out computing,
which involves utilizing a greater number of GPU devices. Scaled-out inference, in our design, is supported
mainly through aggressive pipeline parallelism. Pipeline parallelism enables scaling by distributing different
model segments across different GPUs, adhering to a predetermined parallelization strategy.
5

Cao et al. DumpsterCluster
L1
L2
L3
L4
Sharding across Layer
GPUs
L11 L12 L13 L14
L21 L22 L23 L24TP-first
Inference L31 L32 L33 L34
L41 L42 L43 L44
Sharding within Layer
GPUs
PP-first
Inference
T=0 T=1 T=2 T=3
❶ ❷
❸ ❹
B1 B2 B3 B4
B1 B2 B3 B4
B1 B1
B1
B2 B3 B2
B1 B1
B1 B1 B1
B2
B3B4
Data Blocks
Data Blocks
❶ ❷
❸ ❹
Figure 4: An illustration of the model parallelism strategy described with our approach. We use a simple
example with inference on a 4 GPU node and a 4-layer model. For TP-first framework such as vLLM [18],
they opted to utilize the high inter-device and compute-bandwidth ratio with a model sharding within layer.
However, with our re-used devices, since our inter-device bandwidth and compute-bandwidth ratio are limited,
for our approach (PP-first inference), we opt to utilize as much pipeline parallelism by layer as possible
regardless of device topology.
Naive Pipeline
GPU 0 W0 W1 W2
GPU 1 W0 W1 W2
GPU 2 W0 W1 W2
GPU 3 W0 W1
Our Pipelining
GPU 0 W0 W1 W2
CPU
GPU 1 W0 W1 W2
CPU
GPU 2 W0 W1 W2
CPU
GPU 3 W0 W1 W2
CPU
Time
GPU Compute
CPU Send/Recv
GPU Comm (NCCL)
Kernel Launch
Figure 5: An illustration of our pipelining compared to a naive pipelining strategy in a 4 GPU setting for
inference. In the Naive Pipeline case, GPUs manage communication via NCCL, this requires a kernel launch
and GPU sends/receives (blocking both GPUs). This creates a large idle time for the GPUs. In our pipelining
approach, CPUs manage all communication asynchronously, overlapping with GPU compute, this requires
only minimal buffering time in between GPU compute. Workload labels (W0-W2) and curved arrows show
data flow across GPUs. GPUs remain dedicated to computation, achieving higher utilization and throughput.
6

Cao et al. DumpsterCluster
In addition to the common data parallelism, existing LLM serving software tools use mainly three forms
of model parallelisms, namely tensor parallelism (TP), sequence parallelism (SP) and pipeline parallelism
(PP) 3. Frameworks like vLLM [18] and SGL [19] typically employ a mixed parallelization plan. They use a
heuristic that conducts intra-node level tensor parallelism first and further expands to pipeline or sequence
parallelism. This effectively means that each layer of the model is divided using tensor parallelism within each
device and requires a scatter and a gather communication operation, as shown in Figure 4, to communicate
the inference inputs and results with intermediate partitions of a layer. This strategy demands a high
GPU-GPU interconnect bandwidth between TP devices, which could be more prone to reliability issues and
incurs increased communication costs with second-hand GPUs. This mixed parallelization plan is efficient
with cutting-edge GPUs like the H100 and B200 for two reasons: first, as detailed in Table 1, devices such
as the H100 possess good local inter-GPU communication links; second, these devices are predominantly
memory-bound, exhibiting a large compute-to-bandwidth ratio (such as 0.29 TFLOPs/GB for H100). This is
related to semiconductor scaling; the growth in compute capabilities (FLOPs/s) has considerably outpaced
that of memory interconnects (GB/s). Using tensor parallelism is a good strategy to harness more HBM
bandwidth and achieve more efficient LLM serving.
This design choice, however, is less attractive for second-hand GPUs, which have a reduced inter-GPU
bandwidth and, more critically, are not as memory-bound as these new GPUs. To address this, we developed
apipeline-first parallelization strategyfor second-hand GPUs, shown in Figure 5. Our approach supports
a novel device-level pipeline-first parallelism, where each device operates as an individual pipeline stage,
diverging from traditional node-level pipelining4. This device-level pipelining is designed to accommodate
at least one layer per GPU device, enabling a maximum pipeline parallelism and creating an exceptionally
deep compute pipeline. This approach enabled us to scale up with a greater number of second-hand devices,
circumventing the small VRAM and limited computational power of individual second-hand GPUs. With
this device-level pipelining, we can achieve up to 80 pipeline stages to fit an LLaMA-70B model on V100
devices, which is a significantly deeper pipeline compared to the one using vLLM [18].
This particular optimization choice also accommodates the lower NVLink bandwidth in second-hand GPUs
by only transferring the forward result after a layer (e.g. layer outputs), saving the communication cost for
gather-scatter in TP. The amount of bandwidth required across GPUs is only 3.125 GB/s which is well below
the cross-device bandwidth that the custom-built V100 GPU pod can offer. In our design, we also support
a mixed parallelization plan by optionally using tensor parallelism in the final phase, as these devices are
inherently less memory bound (lower compute-to-bandwidth ratio shown in Table 1). In essence, frameworks
such as vLLM [18] prioritize tensor parallelism, whereas our approach operates in a pipeline parallelism
first manner when both are operating in mixed parallelization modes. However, a deep device-level pipeline
comes with the cost of increased cross-device communication to forward the intermediate results. In a naively
implemented pipeline parallel strategy (Naive Pipeline), computed results must be transmitted to subsequent
devices, introducing communication latency between each pipeline stage. As shown in Figure 5, this results in
communication delays between each pipeline stage. The common strategy is to establish such communication
through the GPUs, which requires the GPUs to stop doing compute and launch a communication kernel (the
NCCL and Kernel Launch block shown in Figure 5), which introduces extra communication latency into the
pipeline and would force GPUs in the pipeline to stay idle from doing useful computation. It is worth noting
that this is also a scenario of TP inference with node-level pipelines. To address this, we propose and have
implemented an asynchronous data transaction optimization on the host (CPU) side. As Figure 5 outlines,
this optimization enables pre-fetching of data inputs for the (t + 1)th timestep while the GPU is computing
the t-th timestep results. Consequently, this prefetch masking hides the data transaction time and frees up
the GPUs to do more useful work and eliminate their idle computational intervals.
3 Results
3.1 LLM inference service quality
To evaluate whether second-hand GPUs can deliver production-quality LLM inference, we benchmark our
custom serving engine against state-of-the-art systems running on current-generation hardware.
3There are also other forms of parallelism such as expert parallelism (for MoE models), but these are beyond the
scope of this paper.
4Commonly, 4-8 devices would form a compute node, as illustrated in Figure 3, and pipelining happens at this
node level.
7

Cao et al. DumpsterCluster
Table 1: Hardware characterization and embodied carbon for GPUs. The die size and VRAM size data are
obtained from datasheets and the manufacture CPA values are from [12] and [20]. The VRAM embodied
carbon is obtained following the unit CO2e shown in [13]. Given that a single deployment cycle is typically 3
years, we consider the embodied carbon for three generations of devices over potential deployment durations
of 3, 5, and 8 years. For the B200 GPU, since the data are not available, we deduced the data using closest
possible process node for the embodied carbon. These deduced results are marked with an∗.
Categories Units B200 H100 80GB A100 80GB V100 16GB
Hardware characteristics
Compute Capability TFLOPs/s 2250 (BF16) 989 (BF16) 312 (BF16) 125 (FP16)
HBM BW GB/s 8000 3350 1555 900
Compute to BW ratio TFLOPs/GB 0.28 0.29 0.2 0.13
Inter-GPU BW GB/s 1800 900 600 300
Logic die embodied carbon
Manufacture Process - TSMC 4NP TSMC N4 TSMC 7nm TSMC 12nm
Silicon Area mm2 1600 815 826 815
CO2e Per Area kg/cm2 1.8* 1.8 1.6 1.2
CO2e in Total kg 28.8* 14.67 13.21 9.78
VRAM embodied carbon
VRAM Type - HBM3e HBM3 HBM2e HBM2
Size GB 192 80 80 16
Unit CO2e kg/GB 0.24* 0.24 0.24 0.28
Total CO2e kg 46.08* 19.2 19.2 4.48
Equivalent yearly embodied carbon
Carbon 3-year kg/yr 24.96* 11.21 10.77 4.73
Carbon 5-year kg/yr 12.48* 6.74 6.48 2.80
Carbon 8-year kg/yr 8.32* 4.20 3.98 1.73
We focus on a metric that determines the viability of inference deployments: Tokens Per Second (TPS). This
metric directly impacts user experience and operational costs, as modern LLM API providers charge per
token generated. For the 8B model, our 128-V100 cluster achieves around 224K TPS on the Prefill-heavy
workload, demonstrating that scaled-out second-hand hardware can deliver competitive throughput despite
individual device limitations. For the 70B model, while absolute throughput is lower due to the larger model
size, the pipeline-first parallelization strategy enables our V100 cluster to serve these models effectively, which
would otherwise be impossible on individual older GPUs.
We evaluate performance across three representative workload categories, as illustrated in Figures 2a and 2b.
First, ShareGPT [21] represents real-world conversational traces with mixed input/output lengths typical of
chatbot deployments. Second, Prefill-heavy workloads simulate compute-intensive scenarios such as code
generation, where models process longer input contexts and generate substantial output. Third, Decode-heavy
workloads emphasize rapid token generation with shorter prompts, common in conversational AI applications.
This diversity ensures our evaluation captures the full spectrum of inference scenarios encountered in
production deployments. The details about each of these different workloads are summarized in Appendix C.
As shown in Table 2 and Figure 2a, for the 8B parameter model, our 128-V100 cluster demonstrates compelling
performance. On the Prefill-heavy workload, the cluster achieves 223K TPS, substantially outperforming
even the latest B200 GPU (around 62K TPS) through aggressive pipeline parallelization. On ShareGPT, the
cluster delivers 21.5K TPS compared to B200’s 44K TPS. This demonstrates that despite the individual
limitations of V100 GPUs – lower memory bandwidth (900 GB/s vs 3,350 GB/s for H100) and reduced
compute capability in dense FP16 (125 TFLOPs vs 989 TFLOPs) – our pipeline-first parallelization strategy
enables competitive aggregate performance through scale-out computing.
The 70B parameter model presents a more demanding inference workload, requiring substantially more
memory and compute resources. As detailed in Table 3 and Figure 2b, our 128-V100 cluster achieves 1.5K
TPS on the Prefill-heavy workload, compared to B200 8-GPU pod’s 37K TPS and H100 8-GPU pod’s 20K
TPS, and the capital expenditure of 128-V100 is78× less. While the absolute throughput is lower, this
8

Cao et al. DumpsterCluster
result is significant: the 70B model cannot fit on a single V100 (16GB memory), making individual V100s
entirely unsuitable for this workload without our device-level pipeline parallelism approach. The fact that we
achieve any throughput at all – let alone an order of the magnitude performance reduction – demonstrates
the effectiveness of our parallelization strategy in enabling second-hand hardware to serve models that would
otherwise be impossible to deploy on older devices. Our V100 systems, whether with 16-GPU or 128-GPU
configurations, exhibit comparable and superior cost efficiency to the new B200 8-GPU pod,particularly in
regions with lower energy prices. Additionally, the V100’s greater availability in the supply chain and
its reduced initial capital expenditure make it a more accessible option for assembly. It should be noted that
the A100 80GB model, as shown in Figure 2b, emerges as the most cost-effective option over an N-year time
period. The A100-80GB system is calculated from a second-hand construction setup – this reinforces our
argument in favor of the superior cost efficiency of what we term “DumpsterCluster”.
A key observation from Figures 2a and 2b is that our approach exhibits better scaling efficiency with larger
models. For the 8B model, we achieve approximately 7.6× throughput improvement over a 4-V100 pod
when scaling to 128 GPUs. For the 70B model, where the deeper pipeline is essential rather than optional,
the benefits of our device-level parallelization become more pronounced. This scaling behaviour validates
our design choice: pipeline-first parallelization is particularly advantageous for larger models and greater
device counts, precisely the scenario where second-hand GPUs offer the most compelling economic advantages
through scale-out deployment.
3.2 Cost and carbon footprint analysis
Table 2 and Table 3 present our main findings, demonstrating the quality of inference service, the monetary
costs, and the carbon footprint associated with the use of second-hand V100 GPU devices. For all results in
these tables, we follow similar statistics with the conversation dataset published by Azure LLM [21], and
consider an input length of 100 tokens generating 1024 output tokens. This typical measurement setup serves
as a representation of human-AI chatbot dialogues. For the baseline comparisons, B200 benchmarks are
conducted using vLLM v0.17, while H100 and A100 results are obtained using vLLM v0.65; V100 results are
from our custom serving system.
We present inference performance metrics, including Decode Throughput in Tokens Per Second (TPS), for
both 8B and 70B LLaMA model [1] inference. Tokens per Second (TPS) indicates system performance.
Current LLM API providers charge based on each input and output token, so a higher TPS implies the
potential for greater profits. As illustrated in Table 2, a 128-V100 pod ($7.68K in GPU cost) achieves
approximately3.6× the throughput of a single B200 GPU ($75K), while costing roughly10× less in hardware
acquisition. Table 3, which details the 70B model, shows that the 128-V100 pod achieves approximately3.2×
the cost-effectiveness of a B200 system when considering only the capital expenditure required for hardware
purchase, measured as throughput per dollar of GPU cost. It is important to note that our approach has a
greater benefit as the model size increases, due to the pipeline-first parallelization strategy we’ve implemented.
This strategy is designed for scale-out computing and is naturally more advantageous with larger models and
a higher number of devices.
We present the operational cost in Table 2 and Table 3, which are closely linked to electricity prices. We
consider four representative energy supplies from different geographical locations with varying mixes of
renewable energy sources. Specifically, we consider:
•US energy supply mix:20%renewable energy
•China energy supply mix:30%renewable energy
•Brazil energy supply mix:90%renewable energy
•Sole energy supply from wind farms in China:100%renewable energy
The fourth option (100%renewable) is an ideal setup, and even in this case, there is a residual operational
carbon emission of approximately10g/kWh due to lifecycle emissions from renewable infrastructure. Taking
the official electricity unit costs from these regions (more details are available in Appendix A) we report
operational expenses in terms of USD per million tokens (MT) generated.
It is evident in both Table 2 and Table 3, state-of-the-art GPUs (like H100s) show significantly better
operational cost mainly due to the silicon technology scaling. However, it is worth mentioning that existing
5H100 and A100 results were profiled at the time of finishing constructing the cluster, during the 1-year real-serving,
later versions of vLLM and Blackwell devices became available.
9

Cao et al. DumpsterCluster
3-yr 5-yr 8-yr
0.00
0.01
0.01
USD/MT
China (30%)
3-yr 5-yr 8-yr
Wind (100%)
3-yr 5-yr 8-yr
0.00
0.01
0.01
USD/MT
US (20%)
3-yr 5-yr 8-yr
Brazil (90%)
1 B200 1 H100 1 A100 128 V100
(a) LLaMA 3.1-8B (Prefill-heavy)
3-yr 5-yr 8-yr
0.03
0.10
0.30
USD/MT
China (30%)
3-yr 5-yr 8-yr
Wind (100%)
3-yr 5-yr 8-yr
0.03
0.10
0.30
USD/MT
US (20%)
3-yr 5-yr 8-yr
Brazil (90%)
8×B200 8×H100 8×A100 128 V100
(b) LLaMA 3.1-70B (Decode-heavy)
Figure 6: Total cost of ownership (USD per million tokens) across four energy mixes and deployment lifetimes
of 3, 5, and 8 years (data from Tables 2 and 7). For the 8B model (a), the 128-V100 DumpsterCluster is the
cheapest option across all mixes. For the 70B model on decode-heavy workload (b), V100 pods do not always
achieve the lowest cost, but demonstrate superior performance in certain combinations of workload, model
size, and energy mix.
LLM API companies, like Together AI, offer inferences for 8-billion-parameter models at 0.10 USD/MT and
for 70-billion-parameter models at 0.88 USD/MT6. Even with heightened operational costs, systems based on
V100 GPUs can still be extremely profitable.
We also evaluate the combined capital and operational expenditures over a 3-year, 5-year, and 8-year
deployment lifetime (Cost 3-year, Cost 5-year and Cost 8-year) in Table 2 and Table 3; these costs are
visualized in Figure 6. Despite the higher operational costs associated with V100-based systems, their reduced
capital expenses make them a financially viable platform for deployment. Our analysis reveals that for an
8B model, when utilizing a carefully selected energy supply (China Energy Mix), a 128-V100 pod can be
up to6× more cost-effective compared to H100 counterparts. The cost-effectiveness gap shortens with 70B
models: under the China energy mix, the 128-V100 pod’s 3-year total cost per token is approximately1.5×
that of an H100 system (i.e.,67%of H100’s cost efficiency), compared to the6× advantage observed for 8B
models. This reflects the higher per-token operational cost of older hardware at larger model scales. This
demonstrates that, for end-of-life GPUs, like these V100-based systems, with adequate engineering and system
co-development, still show some competitive advantage in deployment, primarily due to their significantly
lower capital cost. We then investigate the potential environmental impacts of running LLM inference with
these V100-based systems. Table 2 and Table 3 show the carbon footprint (Ctotal, Equation (1)) of different
hardware, which combines operational carbon (Copt, Equation (2)) and embodied carbon (Cem, Equation (4)).
We consider a 5-year lifetime for all hardware when calculating the carbon footprint. The lifetime carbon
footprint of V100s can be perceived in different ways. One perspective is to consider that, by repurposing
V100s for LLM serving, their lifespan is effectively extended, which we show as ‘Carbon Footprint (extended)’
in both Table 2 and Table 3. Alternatively, if we consider that these devices, once phased out of data centers,
would have reached the end of their useful life—with their embodied carbon effectively zeroed since they are
being reused instead of discarded—we can present this as ‘Carbon Footprint (zero embodied)’. This basically
assumes that, without reuse, the devices would end up in landfills. We also take into account the operational
carbon emissions from different energy supplies and factor in the embodied carbon to calculate the carbon
footprint per million token generation. As seen in both Table 2 and Table 3, our approach using second-hand
GPUs exhibits a larger carbon footprint. For the 8B model, the carbon footprint could be approximately 3.7
times larger, and for the 70B model, this disparity increases to approximately 41 times due to the inherent
increase in electricity usage of V100 deployment.
6These numbers are taken from inference cost of Llama3 8B Instruct Lite and Llama3.3 70B on together.ai pricing
10

Cao et al. DumpsterCluster
Table 2:Prefill-heavy workload, LLaMA 3.1-8B., Running model serving on new and second-hand
GPUs with LLaMA 3.1-8B. We measure Token Per Second (TPS) and actual Operational cost (USD per
million Tokens) with a unit electricity price from the different energy mixes with Prefill-heavy tasks. We also
consider the combined capital and operational costs with a 3-year, 5-year, and an 8-year life-time. We report
carbon footprints, for V100s, we consider two values “Carbon Footprint (extended)/Carbon Footprint (zero
embodied)”, which are further explained in Section 3.
Metrics Units B200† H100 A100 80GB V100 V100 1 GPU 1 GPU 1 GPU 4-GPU pod 128-GPU pod
Inference serving metrics
Capital cost USD 75K 18.5K 5.8K 240 7.68K
TPS tokens/s 62651 29343 12451 6998 223936
30%renewable energy (China energy mix)
Operational cost USD/MT 0.00010.0002 0.0004 0.0005 0.0005
Cost 3-year USD/MT 0.01 0.01 0.01 0.0008 0.0008
Cost 5-year USD/MT 0.01 0.0042 0.0033 0.0007 0.0007
Cost 8-year USD/MT 0.0049 0.0027 0.0022 0.0006 0.0006
Carbon footprint gCO 2/MT 1.842.82 5.35 6.97/6.65* 6.85/6.65*
100%renewable energy (China Wind Farm )
Operational cost USD/MT 0.00020.0003 0.0005 0.0007 0.0007
Cost 3-year USD/MT 0.01 0.01 0.01 0.0010 0.0010
Cost 5-year USD/MT 0.01 0.0043 0.0035 0.0009 0.0009
Cost 8-year USD/MT 0.0049 0.0028 0.0024 0.0008 0.0008
Carbon footprint gCO 2/MT 0.070.11 0.24 0.43/0.11* 0.31/0.11*
20%renewable energy (US energy mix)
Operational cost USD/MT 0.00040.0006 0.0011 0.0014 0.0014
Cost 3-year USD/MT 0.01 0.01 0.01 0.0017 0.0017
Cost 5-year USD/MT 0.01 0.0046 0.0040 0.0016 0.0016
Cost 8-year USD/MT 0.01 0.0031 0.0029 0.0015 0.0015
Carbon footprint gCO 2/MT 1.151.77 3.37 4.43/4.12* 4.31/4.12*
90%renewable energy (Brazil energy mix)
Operational cost USD/MT 0.00050.0008 0.0015 0.0019 0.0019
Cost 3-year USD/MT 0.01 0.01 0.01 0.0022 0.0022
Cost 5-year USD/MT 0.01 0.0048 0.0044 0.0021 0.0021
Cost 8-year USD/MT 0.01 0.0033 0.0033 0.0020 0.0020
Carbon footprint gCO 2/MT 0.340.53 1.02 1.42/1.11* 1.31/1.11*
†B200 results were profiled with vLLM v0.17; H100, A100, and V100 benchmarks were profiled using vLLM v0.6.
* For V100 carbon footprint, values are reported as “extended/zero embodied” (see Section 3).
4 Discussion and Limitations
Our work demonstrates that second-hand GPUs can offer competitive performance and cost-effectiveness for
LLM inference when paired with specialized software optimizations and appropriate deployment conditions.
However, several important considerations and limitations warrant careful discussion.
4.1 Hardware Reliability and Operational Challenges
While we have implemented hardware binning and stress-testing procedures to mitigate reliability concerns
(Section 2), second-hand hardware reliability remains an issue for production deployments. Unlike new
hardware with full manufacturer warranties and predictable failure rates, second-hand devices carry inherent
uncertainty about their operational history and remaining lifespan.
11

Cao et al. DumpsterCluster
Table 3:Prefill-heavy workload, LLaMA 3.1-70B.Running model serving on new and second-hand
GPUs with LLaMA 3.1-70B. We measure Token Per Second (TPS) and actual Operational cost (USD per
million Tokens) with a unit electricity price from the different energy mixes with Prefill-heavy tasks. We also
consider the combined capital and operational costs with a 3-year, 5-year, and an 8-year life-time. We report
carbon footprints, for V100s, we consider two values “Carbon Footprint (extended)/Carbon Footprint (zero
embodied)”, which are further explained in Section 3.
Metrics Units B200† H100 A100 80GB V100 V100 8-GPU pod 8-GPU pod 8-GPU pod 16-GPU pod 128-GPU pod
Inference serving metrics
Capital cost USD 600K 148K 46.4K 960 7.68K
TPS tokens/s 37045 19885 8642 189 1512
30%renewable energy (China energy mix)
Operational cost USD/MT 0.00170.0022 0.0041 0.07 0.07
Cost 3-year USD/MT 0.17 0.080.06 0.12 0.12
Cost 5-year USD/MT 0.10 0.050.04 0.10 0.10
Cost 8-year USD/MT 0.07 0.030.03 0.09 0.09
Carbon footprint gCO 2/MT 24.6232.74 60.36 1014.91/985.40* 1014.91/985.40*
100%renewable energy (China Wind Farm)
Operational cost USD/MT 0.00250.0034 0.01 0.10 0.10
Cost 3-year USD/MT 0.17 0.080.06 0.16 0.16
Cost 5-year USD/MT 0.11 0.050.04 0.13 0.13
Cost 8-year USD/MT 0.07 0.030.03 0.12 0.12
Carbon footprint gCO 2/MT 0.610.78 1.53 46.45/16.93* 46.45/16.93*
20%renewable energy (US energy mix)
Operational cost USD/MT 0.010.01 0.01 0.20 0.20
Cost 3-year USD/MT 0.18 0.090.07 0.26 0.26
Cost 5-year USD/MT 0.11 0.050.05 0.24 0.24
Cost 8-year USD/MT 0.07 0.040.03 0.22 0.22
Carbon footprint gCO 2/MT 15.3020.34 37.53 639.04/609.52* 639.04/609.52*
90%renewable energy (Brazil energy mix)
Operational cost USD/MT 0.010.01 0.02 0.28 0.28
Cost 3-year USD/MT 0.18 0.090.07 0.33 0.33
Cost 5-year USD/MT 0.11 0.060.05 0.31 0.31
Cost 8-year USD/MT 0.07 0.040.04 0.30 0.30
Carbon footprint gCO 2/MT 4.275.66 10.50 194.14/164.62* 194.14/164.62*
†B200 results were profiled with vLLM v0.17; H100, A100, and V100 benchmarks were profiled using vLLM v0.6.
* For V100 carbon footprint, values are reported as “extended/zero embodied” (see Section 3).
To empirically assess reliability in practice, we tracked all hardware incidents across our 128-GPU V100 cluster
over one year of continuous operation. Figure 7 presents the breakdown of failure types observed during this
period. Across 58 total incidents, we found that true hardware failures requiring device replacement were
relatively rare: only 8 cases (13.8%) consisted of actual hardware failures—2 NIC failures, 1 GPU failure, and
5 CPU failures. The majority of incidents (50 cases, 86.2%) were recoverable through software interventions:
32 PCIE resets and 18 software-reasoned resets. These recoverable failures typically required only service
restarts or node reboots rather than physical hardware replacement. Notably, 50 total recoverable incidents
over one year across 128 GPUs represents a relatively low failure rate.
This empirical data suggests that properly binned second-hand hardware can achieve acceptable reliability for
production LLM serving. The 8 hardware failures over one year across 128 GPUs translate to approximately
a 6.25% annual device failure rate, which aligns with the10%additional capacity provisioning strategy we
adopted based on prior reliability studies [16, 17]. The predominance of recoverable software-level failures
indicates that robust cluster management software can effectively mask most reliability issues from end users.
12

Cao et al. DumpsterCluster
NIC Failure PCIE Reset
Software ResetGPU Failure CPU Failure
0
20
40
60
3.4%
55.2%
31%
1.7%
8.6%
Failure Rate (%)
Figure 7: Hardware failure rate breakdown from1year of actual operating deployment of our 128-GPU
V100 pod. Out of all service impacting incidents, only 13.8% were true hardware failures requiring device
replacement (NIC, GPU, CPU), while the majority (86.2%) were recoverable resets handled through software
interventions.
However, organizations considering second-hand deployments must account for higher operational overhead
in monitoring, maintenance, and replacement logistics compared to new hardware fleets. The lack of vendor
support means organizations must develop in-house expertise for hardware diagnostics and repair, or accept
higher device replacement rates. The economics of these trade-offs remain favorable when hardware capital
costs dominate—as with V100 clusters at current market prices—but may shift as second-hand prices fluctuate
or if failure rates exceed anticipated levels.
4.2 Energy Infrastructure as a Critical Dependency
Our results in Table 2 and Table 3 reveal a fundamental insight: the viability of second-hand GPU deployment
is inextricably linked to energy infrastructure characteristics, specifically electricity cost and carbon intensity.
This dependency has profound implications for the future of sustainable AI infrastructure and energy security.
The stark contrast in carbon footprints across different energy mixes — ranging from sub-1 g/MT with100%
renewable energy to approximately 7 g/MT with fossil-fuel dominated grids for 8B models — demonstrates
that hardware efficiency improvements alone cannot achieve sustainability goals. For second-hand deployments,
such as the DumpsterCluster, to avoid significant negative environmental impacts, they must be strategically
co-located with clean energy sources.
This presents both opportunities and challenges. Regions with abundant renewable energy capacity, such as
areas with hydroelectric, geothermal, or wind resources, represent ideal deployment targets for second-hand AI
infrastructure. Such deployments can achieve genuine environmental benefits by extending hardware lifecycles
while leveraging low-carbon electricity. Conversely, deploying second-hand GPUs in regions dependent on
fossil fuels may actually worsen the overall carbon footprint of AI services, despite the reduced embodied
carbon from hardware reuse.
Moreover, the lower initial capital investments of second-hand hardware compared to new GPUs reduce the
financial risk of deploying in regions with energy price volatility or regulatory uncertainty. Organizations can
establish distributed inference capacity across multiple energy markets, reducing dependence on any single
energy supplier or grid. This geographic diversification provides resilience against energy supply disruptions,
price shocks, or policy changes that might affect concentrated data center deployments.
Looking forward, as AI inference workloads continue to grow, the energy demands will increasingly stress
electrical grids. The lower energy efficiency of second-hand hardware exacerbates this challenge locally but
enables strategic flexibility globally. Second-hand GPU clusters may find their most appropriate role in
regions where renewable energy is abundant and inexpensive, effectively serving as a mechanism to monetize
otherwise-curtailed renewable generation capacity while reducing pressure on constrained grid infrastructure
in high-demand urban centers.
The importance of clean and cheap energy sources cannot be overstated for the future of AI inference. As
inference demands scale with widespread AI deployment and compute-intensive paradigms like test-time
13

Cao et al. DumpsterCluster
scaling, the aggregate energy consumption will rival or exceed that of training. Without strategic coupling to
low-carbon energy infrastructure, this growth will impose unsustainable environmental costs. Our findings
suggest that future AI infrastructure planning must prioritize energy co-location: matching compute capacity
deployment with renewable energy availability rather than treating energy as a commodity available anywhere
at similar cost and carbon intensity.
4.3 Market Dynamics and Economic Sustainability
Our economic analysis relies on current second-hand market prices, which reflect limited demand for older GPU
models. However, this analysis contains an inherent paradox: if second-hand GPU deployment becomes widely
adopted based on our demonstrated cost advantages, increased demand would likely drive up second-hand
prices, potentially eroding the economic benefits we document.
The second-hand GPU market is currently characterized by excess supply, as hyperscale data centers regularly
retire functional hardware to upgrade to newer generations. V100 prices have declined from approximately
$215 to $50-$60 over the past two years, reflecting a weak demand relative to the available supply. However,
if our approach gains traction and organizations begin systematically acquiring second-hand GPUs for LLM
serving, market dynamics would shift.
Beyond price dynamics, second-hand hardware offers important supply chain security advantages. The
production of cutting-edge GPUs is concentrated among a few manufacturers and fabrication facilities, creating
vulnerability to supply disruptions from geopolitical tensions, natural disasters, or capacity constraints. During
recent GPU shortages, organizations faced procurement delays exceeding 6-12 months for new hardware,
with some unable to secure allocations at all. Second-hand markets provide an alternative channel that is
geographically distributed, less subject to export controls on frontier technology, and immediately accessible
without multi-month lead times.
This supply chain diversification is particularly valuable for organizations in regions with limited access to
new GPU supplies, whether due to vendor prioritization of hyperscale customers, export restrictions, or
geopolitical factors. Second-hand hardware enables these organizations to participate in AI development
and deployment without dependence on fragile supply chains for cutting-edge components. However, this
supply chain independence comes with the trade-off of relying on hardware that major vendors no longer
support, requiring organizations to develop alternative support channels and accept greater self-reliance in
maintenance and repair.
4.4 Workload Specificity: Inference versus Training
A critical limitation of our approach is its primary applicability to inference workloads rather than training.
This specialization stems from fundamental differences in computational characteristics between these
workloads.
LLM training requires:
1. High inter-GPU bandwidth for gradient synchronization across data-parallel and model-parallel
dimensions
2. Large batch sizes to maintain computational efficiency and training stability
3. Precision in numerical computations (often requiring FP32 or mixed-precision training with careful
gradient scaling)
4. Extended continuous operation over weeks or months, amplifying the impact of any hardware
reliability issues
The limited NVLink bandwidth (300 GB/s for V100 versus 900 GB/s for H100) would bottleneck gradient
synchronization across devices. Furthermore, training’s reliability requirements are more stringent—a single
device failure during a multi-week training run can require checkpoint rollback and substantial re-computation,
making the higher failure rates of second-hand hardware particularly costly for training workloads. However,
the computational economics of LLM deployment are increasingly dominated by inference rather than training.
A model is trained once but serves millions or billions of queries over its deployment lifetime, and this is
where this second-hand GPU inference paradigm holds value.
14

Cao et al. DumpsterCluster
5 Conclusion
This paper demonstrates that second-hand GPUs, when paired with specialized software optimizations and
deployed under appropriate conditions, offer a viable pathway for expanding AI inference capacity. We built
a 128-GPU V100 cluster from entirely second-hand components, deployed it in production for one year, and
developed a pipeline-first parallelization strategy that enables competitive LLM serving performance despite
the hardware limitations of older devices. Our empirical analysis reveals that the viability of GPU afterlife
depends critically on three factors: workload characteristics, energy infrastructure, and market conditions.
For inference workloads, which increasingly dominate AI’s computational footprint, second-hand hardware
can achieve throughput competitive with cutting-edge systems at a fraction of the capital cost ($22K vs.
$600K). However, the environmental benefits materialize only when deployments are strategically co-located
with low-carbon energy sources; otherwise, higher operational emissions—approximately4× for 8B and over
40×for 70B models under grid-average carbon intensity—can negate the reduced embodied carbon.
15

Cao et al. DumpsterCluster
Appendix A Regional Energy Supply Characteristics
We derive all the energy prices from the industrial sector energy price offered by various statistics sources.
For the USA, we refer to the EIA statistics [22]. For China, we use the industrial electricity cost reported
from CEIC [23]. For Brazil the electricity cost statistics are derived from [24]. Carbon intensity values are
obtained from regional grid emission factors for 2023 [25], accounting for the energy mix composition of each
region. Renewable energy penetration percentages are derived from [25] from 2023 as well. These data sources
are collected from Ember with major processing of Our World in Data. Table 4 presents the comprehensive
regional energy grid characteristics used in our analysis, including renewable energy penetration, carbon
intensity, and industrial electricity prices.
Table 4: Regional energy supply characteristics
Region Renewable Carbon Intensity Energy Price
(%) (gCO 2/kWh) (USD/kWh)
China (Non-renewable)∼30 584.0 0.0556
United States∼20 393.0 0.12
Brazil∼90 97.0 0.125
China (Renewable)∼100∼10.0 0.0556
The regional variations reflect different energy infrastructure and policy environments:
• China (Non-renewable): Represents deployment in regions with coal-dominated grids (30%
renewable penetration), resulting in high carbon intensity
• United States: Mixed grid with moderate renewable penetration (20%) from various sources
including natural gas, nuclear, and renewables
• Brazil: High renewable content (90%) primarily from hydroelectric sources, resulting in low carbon
intensity despite higher electricity costs
• China (Renewable only): Represents deployment co-located with renewable energy sources (100%
renewable), achieving minimal operational carbon emissions
Appendix B GPU Price Calculation
The hardware cost estimates utilized in this analysis are reported in United States Dollars (USD) and
derived from a combination of direct vendor quotations and secondary market valuations. Specifically, the
pricing for the NVIDIA B200 is based on a full-system quotation of $600,000 obtained from Scan.co.uk. To
calculate the individual per-unit GPU cost, this aggregate system price—which is inclusive of all requisite
peripheral components and networking hardware—is divided by eight. Conversely, the cost estimates for the
NVIDIA H100 and A100 accelerators are sourced from the secondary market; consequently, these figures
are subject to inherent market volatility and may exhibit temporal fluctuations. Individual NVIDIA V100
prices are similarly derived from secondary market data. However, it should be noted that the cost for the
128-GPU V100 pod configuration is reported as a comprehensive total system cost, encompassing both the
computational units and all necessary peripheral infrastructure.
Appendix C Workload Characteristics
To evaluate model performance across varied inference profiles, we utilized three distinct workload
configurations (summarized in Table 5). All workloads utilize a baseline 17-token system prompt.
Table 5: Token distributions across different LLM workloads
Workload Input Tokens Output Tokens (max)
Prefill-heavy 1,259 128
Decode-heavy 199 1,024
SharedGPT∼262 mean /∼94 median (variable) 180
16

Cao et al. DumpsterCluster
• Prefill-Heavy:Evaluates prompt processing bottlenecks using a large input context (1,259 tokens,
dominated by tool definitions) and a strictly capped 128-token generation.
• Decode-Heavy:Assesses auto-regressive generation efficiency using a concise input (199 tokens)
and an extended generation window capped at 1,024 tokens.
• ShareGPT:Simulates real-world variability using 500 sampled conversations from the ShareGPT
dataset (seed=42), chunked to 2,048 tokens per FastChat protocols, with a 180-token maximum
output.
Appendix D Additional Experiment Result
D.1 Decode Heavy Experiment Results
We present the cost and carbon footprint results under the Decode-heavy workload, which uses a concise
199-token input and an extended 1,024-token generation window (see Appendix C). This workload emphasizes
auto-regressive decoding throughput and is representative of conversational AI applications where output
length dominates.
17

Cao et al. DumpsterCluster
Table 6:Decode-heavy workload, LLaMA3.1-8B.Running model serving on new and second-hand
GPUs with LLaMA 3.1-8B. We measure Token Per Second (TPS) and actual Operational cost (USD per
million Tokens) with a unit electricity price from the different energy mixes. We also consider the combined
capital and operational costs with a 3-year, 5-year, and an 8-year life-time. We report carbon footprints, for
V100s, we consider two values “Carbon Footprint (extended)/Carbon Footprint (zero embodied)”, which are
further explained in Section 3.
Metrics Units B200† H100 A100 80GB V100 V100 1 GPU 1 GPU 1 GPU 4-GPU pod 128-GPU pod
Inference serving metrics
Capital cost USD 75K 18.5K 5.8K 240 7.68K
TPS tokens/s 2603711506 5919 254 8128
30%renewable energy (China energy mix)
Operational cost USD/MT 0.00030.0005 0.0008 0.01 0.01
Cost 3-year USD/MT 0.03 0.020.01 0.02 0.02
Cost 5-year USD/MT 0.02 0.010.01 0.02 0.02
Cost 8-year USD/MT 0.01 0.010.0046 0.02 0.02
Carbon footprint gCO 2/MT 4.437.19 11.25 191.92/183.31* 188.80/183.31*
100%renewable energy (China Wind Farm)
Operational cost USD/MT 0.00040.0007 0.0011 0.02 0.02
Cost 3-year USD/MT 0.03 0.020.01 0.03 0.03
Cost 5-year USD/MT 0.02 0.010.01 0.02 0.02
Cost 8-year USD/MT 0.01 0.010.01 0.02 0.02
Carbon footprint gCO 2/MT 0.160.29 0.51 11.76/3.15* 8.64/3.15*
20%renewable energy (US energy mix)
Operational cost USD/MT 0.00090.0014 0.0023 0.04 0.04
Cost 3-year USD/MT 0.03 0.020.01 0.05 0.05
Cost 5-year USD/MT 0.02 0.010.01 0.04 0.04
Cost 8-year USD/MT 0.01 0.010.01 0.04 0.04
Carbon footprint gCO 2/MT 2.774.51 7.08 122.00/113.39* 118.88/113.39*
90%renewable energy (Brazil energy mix)
Operational cost USD/MT 0.00120.0020 0.0031 0.05 0.05
Cost 3-year USD/MT 0.03 0.020.01 0.06 0.06
Cost 5-year USD/MT 0.02 0.010.01 0.06 0.06
Cost 8-year USD/MT 0.01 0.010.01 0.06 0.06
Carbon footprint gCO 2/MT 0.811.34 2.15 39.23/30.62* 36.11/30.62*
†B200 results were profiled with vLLM v0.17; H100, A100, and V100 benchmarks were profiled using vLLM v0.6.
* For V100 carbon footprint, values are reported as “extended/zero embodied” (see Section 3).
D.2 ShareGPT Experiment Results
We present the cost and carbon footprint results under the ShareGPT workload, which samples 500 real-
world conversations with variable input lengths (∼262 mean tokens) and a 180-token maximum output (see
Appendix C). This workload captures realistic conversational variability encountered in production chatbot
deployments.
18

Cao et al. DumpsterCluster
Table 7:Decode-heavy workload, LLaMA 3.1-70B.Running model serving on new and second-hand
GPUs with LLaMA 3.1-70B. We measure Token Per Second (TPS) and actual Operational cost (USD per
million Tokens) with a unit electricity price from the different energy mixes. We also consider the combined
capital and operational costs with a 3-year, 5-year, and an 8-year life-time. We report carbon footprints, for
V100s, we consider two values “Carbon Footprint (extended)/Carbon Footprint (zero embodied)”, which are
further explained in Section 3.
Metrics Units B200† H100 A100 80GB V100 V100 8-GPU pod 8-GPU pod 8-GPU pod 16-GPU pod 128-GPU pod
Inference serving metrics
Capital cost USD 600K 148K 46.4K 960 7.68K
TPS tokens/s 2469510372 5366 317 2536
30%renewable energy (China energy mix)
Operational cost USD/MT 0.00250.0043 0.01 0.04 0.04
Cost 3-year USD/MT 0.26 0.16 0.10 0.07 0.07
Cost 5-year USD/MT 0.16 0.09 0.06 0.06 0.06
Cost 8-year USD/MT 0.10 0.060.04 0.05 0.05
Carbon footprint gCO 2/MT 36.9462.78 97.22 605.11/587.51* 605.11/587.51*
100%renewable energy (China Wind Farm)
Operational cost USD/MT 0.00380.01 0.01 0.06 0.06
Cost 3-year USD/MT 0.26 0.16 0.10 0.09 0.09
Cost 5-year USD/MT 0.16 0.100.06 0.08 0.08
Cost 8-year USD/MT 0.10 0.060.04 0.07 0.07
Carbon footprint gCO 2/MT 0.911.50 2.46 27.69/10.09* 27.69/10.09*
20%renewable energy (US energy mix)
Operational cost USD/MT 0.010.01 0.02 0.12 0.12
Cost 3-year USD/MT 0.26 0.160.11 0.15 0.15
Cost 5-year USD/MT 0.16 0.100.07 0.14 0.14
Cost 8-year USD/MT 0.10 0.070.05 0.13 0.13
Carbon footprint gCO 2/MT 22.9638.99 60.44 381.01/363.41* 381.01/363.41*
90%renewable energy (Brazil energy mix)
Operational cost USD/MT 0.010.02 0.03 0.17 0.17
Cost 3-year USD/MT 0.27 0.170.12 0.20 0.20
Cost 5-year USD/MT 0.16 0.110.08 0.19 0.19
Cost 8-year USD/MT 0.11 0.070.06 0.18 0.18
Carbon footprint gCO 2/MT 6.4010.84 16.91 115.75/98.15* 115.75/98.15*
†B200 results were profiled with vLLM v0.17; H100, A100, and V100 benchmarks were profiled using vLLM v0.6.
* For V100 carbon footprint, values are reported as “extended/zero embodied” (see Section 3).
19

Cao et al. DumpsterCluster
Table 8:ShareGPT workload, LLaMA 3.1-8B.Running model serving on new and second-hand GPUs
with LLaMA 3.1-8B. We measure Token Per Second (TPS) and actual Operational cost (USD per million
Tokens) with a unit electricity price from the different energy mixes. We also consider the combined capital
and operational costs with a 3-year, 5-year, and an 8-year life-time. We report carbon footprints, for V100s,
we consider two values “Carbon Footprint (extended)/Carbon Footprint (zero embodied)”, which are further
explained in Section 3.
Metrics Units B200† H100 A100 80GB V100 V100 1 GPU 1 GPU 1 GPU 4-GPU pod 128-GPU pod
Inference serving metrics
Capital cost USD 75K 18.5K 5.8K 240 7.68K
TPS tokens/s 439119312 4551 672 21504
30%renewable energy (China energy mix)
Operational cost USD/MT 0.00020.0006 0.0010 0.0048 0.0048
Cost 3-year USD/MT 0.02 0.02 0.01 0.01 0.01
Cost 5-year USD/MT 0.01 0.01 0.01 0.01 0.01
Cost 8-year USD/MT 0.01 0.010.01 0.01 0.01
Carbon footprint gCO 2/MT 2.638.89 14.63 72.54/69.29* 71.36/69.29*
100%renewable energy (China Wind Farm)
Operational cost USD/MT 0.00030.0009 0.0015 0.01 0.01
Cost 3-year USD/MT 0.02 0.02 0.01 0.01 0.01
Cost 5-year USD/MT 0.01 0.01 0.01 0.01 0.01
Cost 8-year USD/MT 0.01 0.010.01 0.01 0.01
Carbon footprint gCO 2/MT 0.100.36 0.67 4.44/1.19* 3.27/1.19*
20%renewable energy (US energy mix)
Operational cost USD/MT 0.00050.0018 0.0029 0.01 0.01
Cost 3-year USD/MT 0.02 0.020.02 0.02 0.02
Cost 5-year USD/MT 0.01 0.010.01 0.02 0.02
Cost 8-year USD/MT 0.010.01 0.01 0.02 0.02
Carbon footprint gCO 2/MT 1.655.58 9.21 46.11/42.86* 44.93/42.86*
90%renewable energy (Brazil energy mix)
Operational cost USD/MT 0.00070.0025 0.0040 0.02 0.02
Cost 3-year USD/MT 0.02 0.020.02 0.02 0.02
Cost 5-year USD/MT 0.010.02 0.01 0.02 0.02
Cost 8-year USD/MT 0.010.01 0.01 0.02 0.02
Carbon footprint gCO 2/MT 0.481.66 2.80 14.83/11.57* 13.65/11.57*
†B200 results were profiled with vLLM v0.17; H100, A100, and V100 benchmarks were profiled using vLLM v0.6.
* For V100 carbon footprint, values are reported as “extended/zero embodied” (see Section 3).
Appendix E Carbon Calculation
We attribute the LLM carbon emissions at the model inference stage to two main sources: (1)operational
carbon( Copt), which is related to the operational energy consumption of running LLM inferences, and
(2)embodied carbon( Cem), which arises from the production of hardware required to deliver the LLM
inference service. The total attributed LLM carbon emission is:
Ctotal =C opt +C em.(1)
E.1 Operational carbon estimation
Operational carbon (Copt) is determined by the run-time energy consumption of the underlying data center
and the carbon intensity of its energy supply:
Copt =E DC×I,(2)
20

Cao et al. DumpsterCluster
Table 9:ShareGPT workload, LLaMA 3.1-70B.Running model serving on new and second-hand GPUs
with LLaMA 3.1-70B. We measure Token Per Second (TPS) and actual Operational cost (USD per million
Tokens) with a unit electricity price from the different energy mixes. We also consider the combined capital
and operational costs with a 3-year, 5-year, and an 8-year life-time. We report carbon footprints, for V100s,
we consider two values “Carbon Footprint (extended)/Carbon Footprint (zero embodied)", which are further
explained in Section 3.
Metrics Units B200† H100 A100 80GB V100 V100 8-GPU pod 8-GPU pod 8-GPU pod 16-GPU pod 128-GPU pod
Inference serving metrics
Capital cost USD 600K 148K 46.4K 960 7.68K
TPS tokens/s 418575265 3402 440 3520
30%renewable energy (China energy mix)
Operational cost USD/MT 0.00150.01 0.01 0.03 0.03
Cost 3-year USD/MT 0.15 0.31 0.15 0.05 0.05
Cost 5-year USD/MT 0.09 0.19 0.10 0.04 0.04
Cost 8-year USD/MT 0.06 0.12 0.06 0.04 0.04
Carbon footprint gCO 2/MT 21.79123.67 153.34 435.95/423.27* 435.95/423.27*
100%renewable energy (China Wind Farm)
Operational cost USD/MT 0.00220.01 0.02 0.04 0.04
Cost 3-year USD/MT 0.15 0.31 0.16 0.07 0.07
Cost 5-year USD/MT 0.09 0.19 0.10 0.06 0.06
Cost 8-year USD/MT 0.06 0.12 0.07 0.05 0.05
Carbon footprint gCO 2/MT 0.542.95 3.88 19.95/7.27* 19.95/7.27*
20%renewable energy (US energy mix)
Operational cost USD/MT 0.00450.03 0.03 0.09 0.09
Cost 3-year USD/MT 0.16 0.32 0.18 0.11 0.11
Cost 5-year USD/MT 0.100.20 0.12 0.10 0.10
Cost 8-year USD/MT 0.060.14 0.09 0.10 0.10
Carbon footprint gCO 2/MT 13.5476.82 95.33 274.50/261.82* 274.50/261.82*
90%renewable energy (Brazil energy mix)
Operational cost USD/MT 0.010.03 0.04 0.12 0.12
Cost 3-year USD/MT 0.16 0.33 0.19 0.14 0.14
Cost 5-year USD/MT 0.100.21 0.13 0.13 0.13
Cost 8-year USD/MT 0.060.15 0.10 0.13 0.13
Carbon footprint gCO 2/MT 3.7821.36 26.68 83.39/70.71* 83.39/70.71*
†B200 results were profiled with vLLM v0.17; H100, A100, and V100 benchmarks were profiled using vLLM v0.6.
* For V100 carbon footprint, values are reported as “extended/zero embodied” (see Section 3).
21

Cao et al. DumpsterCluster
where EDC represents the total energy consumed by the data center — including energy consumed directly
by the servers, cooling systems, and other infrastructure components — andI (in gCO2/kWh) is the carbon
intensity of the energy source.
Data center energy.We consider that all components of the server operate in the same data center.
Consequently, we model their operational energy consumption using:
EDC =E server×PUE,(3)
where PUE7 captures the overhead from cooling and other infrastructure. We adopt a PUE value of1.2for
all hardware components, averaged across configurations reported in the literature: high-efficiency setups
described by Faizet al.[12] and high-density configurations noted by Heydariet al.[26].
Carbon intensity and energy supply.The carbon intensityI varies depending on the energy source.
We consider four representative energy mixes following data reported in [27], summarised in Table 10:
Table 10: Energy supply configurations used in the carbon analysis. Carbon intensity values are obtained
from [28] and [29]. Energy prices are from regional industrial tariffs. Full details are available in Table 4.
Energy Supply RenewableI(gCO 2/kWh) Price (USD/kWh)
US energy mix∼20% 393 0.12
China energy mix∼30% 584 0.0556
Brazil energy mix∼90% 97 0.125
China (renewable only)∼100%∼10 0.0556
These four energy configurations represent a spectrum from fossil-fuel-dominated grids (US at∼20% renewable)
to fully renewable supplies (direct supply from a wind farm or hydroelectric station in China). For even the
completely renewable energy supply, a residual carbon intensity of approximately10g/kWh remains due to
lifecycle emissions from renewable infrastructure [29]. It is also worth noting that the energy supply affects
the operational cost reported in Tables 2 and 3.
E.2 Embodied carbon estimation
Embodied carbon (Cem) quantifies the manufacturing-stage carbon emissions of the hardware used to deliver
LLM inference. We decomposeCem into three additive terms:
Cem =C die +C VRAM +C periph,(4)
where Cdie is the logic-die embodied carbon,CVRAM is the memory (VRAM) embodied carbon, andCperiph
is the peripheral (server-level) embodied carbon.
Logic-die embodied carbon.We estimate Cdie from the GPU silicon area and the carbon per area (CPA)
of its manufacturing process node:
Cdie =A die×CPA,(5)
where Adie (in cm2) is the die area obtained from technical whitepapers [30–32], and CPA (in kgCO2e/cm2)
is sourced from the methodologies of Liet al.[13] and Faizet al.[12].
VRAM embodied carbon.We compute CVRAM from the HBM capacity and a unit embodied-carbon
factor:
CVRAM =S VRAM×U VRAM,(6)
where SVRAM (in GB) is the total HBM size andUVRAM (in kgCO2e/GB) is the unit embodied carbon
obtained from Liet al.[13].
Peripheral embodied carbon.Each GPU hosting server shares a common set of components (CPU,
RAM, chassis, etc.). We adopt a server-level peripheral cost ofCperiph = 150kg CO 2e per server, following
the measurements of Faizet al.[12].
7Power Usage Effectiveness
22

Cao et al. DumpsterCluster
Annualized embodied carbon.To compare devices across different deployment durations, we amortize
the total embodied carbon over the expected lifespanT(in years):
C annual em (T) = Cdie +C VRAM T + Cperiph NGPU×T ,(7)
where NGPU is the number of GPUs sharing the same server peripherals. We report the annualized values for
deployment durations ofT∈{3,5,8}years in Table 1.
For the B200 GPU, since manufacturing data are not publicly available, we estimate its CPA using the closest
available process node. These deduced results are marked with an∗in Table 1.
Reliability overhead for second-hand devices.For second-hand devices such as the V100, an additional
factor must be considered: hardware reliability. During the reuse process, we apply a binning procedure that
involves stress-testing all components and removing those that are faulty on arrival. An additional round of
production testing is conducted to filter out GPUs prone to early failure.
After binning, we deploy10%additional devices as spare capacity to cover in-service failures, based on the
∼ 90%survival rate observed over a 5-year service lifespan reported by Ostrouchovet al.[16]. For V100s
previously deployed for an initial 3-year data-center cycle, this extends their total product lifecycle to 8 years
(3 + 5).
The reliability-adjusted annualized embodied carbon for second-hand GPUs is therefore:
C annual,adj em (T) =C annual em (T)×1.1,(8)
where the factor1.1accounts for the10%additional devices deployed. The resulting 3, 5, and 8-year embodied
carbon costs for V100s are shown in Table 1.
Carbon footprint perspectives for second-hand devices.When reporting the per-token carbon
footprint (Ctotal, Equation (1)) in Tables 2 and 3, we present two accounting perspectives for second-hand
V100 devices:
1. Extended perspective.The hardware lifecycle is viewed as extended from the original first-life
deployment into a second-life reuse period. The full embodied carbon is amortized over the second-life
deployment durationTusing the reliability-adjusted annualized cost (Equation (8)):
C extended total =C opt +C annual,adj em (T).(9)
2. Zero embodied perspective.The V100s were scheduled for decommission and would otherwise
be discarded (e.g. landfilled). Since their embodied carbon was already “spent” during the initial
data-center cycle, reuse incurs no additional manufacturing emissions. The carbon footprint thus
comprises only operational carbon:
C zero total =C opt.(10)
For new hardware (B200, H100, A100), only a single carbon footprint is reported, computed using the
standard annualized embodied carbonC annual em (T )from Equation (7). The two perspectives above represent
anupper bound(extended) and alower bound(zero embodied) on the attributable embodied carbon for
reused devices; the appropriate allocation depends on the carbon accounting framework adopted.
It is worth noting that this lifecycle analysis excludes emissions from end-of-life disposal (e.g. metal recycling
and landfill), as comprehensive GPU lifecycle data remain limited in the literature. Our CPA estimates
thus primarily account for manufacturing carbon and do not explicitly isolate upstream material-sourcing
emissions.
23

Cao et al. DumpsterCluster
References
[1] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha
Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models.arXiv
preprint arXiv:2407.21783, 2024.
[2] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774, 2023.
[3] Jack Choquette. NVIDIA Hopper H100 GPU: Scaling Performance.IEEE Micro, (3):9–17, 2023.
[4] AMD Instinct MI300 Series Accelerators. https://www.amd.com/en/products/accelerators/
instinct/mi300.html. Accessed: 2024-03-03.
[5] Doug Eadline. Nvidia shipped 3.76 million data-center gpus in 2023,
according to study, Jun 2024. URL https://www.hpcwire.com/2024/06/10/
nvidia-shipped-3-76-million-data-center-gpus-in-2023-according-to-study/.
[6] Jade HPC. Jade service end of life announcement, 2024. URLhttps://www.jade.ac.uk/.
[7] microsoft. Migration guide for gpu compute workloads in azure - azure virtual machines, Mar
2025. URL https://learn.microsoft.com/en-us/azure/virtual-machines/migration/sizes/
n-series-migration.
[8] microsoft azure. Ncv3 and nc24rs retirement - azure virtual machines, Mar 2025. URLhttps://learn.
microsoft.com/en-us/azure/virtual-machines/ncv3-nc24rs-retirement.
[9] Procurri. Decommissioned the largest nvidia dgx a100 environment outside
of a hyperscaler, Dec 2024. URL https://www.linkedin.com/posts/procurri_
weve-just-decommissioned-the-largest-nvidia-activity-7275473830779703297-cQuQ.
[10] Peng Wang, Ling-Yu Zhang, Asaf Tzachor, and Wei-Qiang Chen. E-waste challenges of generative
artificial intelligence.Nature Computational Science, pages 1–6, 2024.
[11] Baolin Li, Rohan Basu Roy, Daniel Wang, Siddharth Samsi, Vijay Gadepally, and Devesh Tiwari.
Toward sustainable hpc: Carbon footprint estimation and environmental implications of hpc systems. In
Proceedings of the international conference for high performance computing, networking, storage and
analysis, pages 1–15, 2023.
[12] Ahmad Faiz, Sotaro Kaneda, Ruhan Wang, Rita Osi, Prateek Sharma, Fan Chen, and Lei Jiang.
Llmcarbon: Modeling the end-to-end carbon footprint of large language models.arXiv preprint
arXiv:2309.14393, 2023.
[13] Yueying Lisa Li, Omer Graif, and Udit Gupta. Towards carbon-efficient llm life cycle. InProceedings of
the 3rd Workshop on Sustainable Computer Systems (HotCarbon), 2024.
[14] Bill Tomlinson, Rebecca W Black, Donald J Patterson, and Andrew W Torrance. The carbon emissions
of writing and illustrating are lower for ai than for humans.Scientific Reports, 14(1):3732, 2024.
[15] Tharindu B Hewage, Shashikant Ilager, Maria Rodriguez Read, and Rajkumar Buyya. Aging-aware
cpu core management for embodied carbon amortization in cloud llm inference.arXiv preprint
arXiv:2501.15829, 2025.
[16] George Ostrouchov, Don Maxwell, Rizwan A Ashraf, Christian Engelmann, Mallikarjun Shankar, and
James H Rogers. Gpu lifetimes on titan supercomputer: Survival analysis and reliability. InSC20:
International Conference for High Performance Computing, Networking, Storage and Analysis, pages
1–14. IEEE, 2020.
[17] Apostolos Kokolis, Michael Kuchnik, John Hoffman, Adithya Kumar, Parth Malani, Faye Ma, Zachary
DeVito, Shubho Sengupta, Kalyan Saladi, and Carole-Jean Wu. Revisiting reliability in large-scale
machine learning research clusters.arXiv preprint arXiv:2410.21680, 2024.
[18] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph
Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving
with pagedattention. InProceedings of the 29th Symposium on Operating Systems Principles, pages
611–626, 2023.
[19] Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Livia Sun, Jeff Huang, Cody Hao Yu, Shiyi
Cao, Christos Kozyrakis, Ion Stoica, Joseph E Gonzalez, et al. Sglang: Efficient execution of structured
language model programs.Advances in Neural Information Processing Systems, 37:62557–62583, 2024.
24

Cao et al. DumpsterCluster
[20] Anvita Bhagavathula, Leo Han, and Udit Gupta. Understanding the implications of uncertainty in
embodied carbon models for sustainable computing. InHotCarbon. 2024.
[21] Pratyush Patel, Esha Choukse, Chaojie Zhang, Aashaka Shah, Íñigo Goiri, Saeed Maleki, and Ricardo
Bianchini. Splitwise: Efficient generative llm inference using phase splitting. In2024 ACM/IEEE 51st
Annual International Symposium on Computer Architecture (ISCA), pages 118–132. IEEE, 2024.
[22] U.S. Energy Information Administration. Average price of electricity to ultimate customers by end-use
sector, table 5.6.a. https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_
5_6_a, 2025. Industrial sector prices (cents per kWh) for March 2025; Accessed: 2025-05-19.
[23] CEIC Data. China electricity price: Industrial usage, 35 kv & above (jan 2003–jan 2025).https:
//www.ceicdata.com/en/china/electricity-price-36-city, 2025. Industrial electricity usage price
by city; Accessed: 2025-05-19.
[24] GlobalPetrolPrices. Brazil electricity prices. https://www.globalpetrolprices.com/Brazil/
electricity_prices/, 2026. Accessed: 2026-03-17.
[25] Ember and Our World in Data. Lifecycle carbon intensity of electricity generation – ember.https://
archive.ourworldindata.org/20260304-094028/grapher/carbon-intensity-electricity.html,
2026. Dataset. Original data: Ember, “Yearly Electricity Data Europe”; Ember, “Yearly Electricity
Data”. Major processing by Our World in Data. Retrieved March 16, 2026 (Archived on March 4, 2026).
[26] Ali Heydari, Bahareh Eslami, Vahideh Radmard, Fred Rebarber, Tyler Buell, Kevin Gray, Sam Sather,
and Jeremy Rodriguez. Power usage effectiveness analysis of a high-density air-liquid hybrid cooled data
center. InInternational Electronic Packaging Technical Conference and Exhibition, volume 86557, page
V001T01A014. American Society of Mechanical Engineers, 2022.
[27] Hannah Ritchie and Pablo Rosado. Energy mix.Our World in Data, 2020.
https://ourworldindata.org/energy-mix.
[28] Global Carbon Project and U.S. Energy Information Administration and Energy Institute, processed
by Our World in Data. Carbon intensity of energy production – gcb.https://ourworldindata.org/
grapher/co2-per-unit-energy, 2025. Data sources: Global Carbon Budget (2024); U.S. Energy
Information Administration “International Energy Data” (2023); Energy Institute “Statistical Review of
World Energy” (2024); retrieved 19 May 2025.
[29] Parliamentary Office of Science and Technology. Carbon footprint of electricity generation.
Technical Report POSTnote268, UK Parliament, October 2006. URL https://www.parliament.
uk/globalassets/documents/post/postpn268.pdf. Offshore wind life-cycle emissions: 5.25 gCO2
eq/kWh; Accessed: 2025-05-19.
[30] NVIDIA Corporation. Nvidia tesla v100 gpu architecture whitepaper. Technical report, NVIDIA GPU
Technology Conference, 2017. Die Size: 815mm2; Accessed: 2025-05-17.
[31] NVIDIA Corporation. Nvidia a100 tensor core gpu architecture whitepaper. Technical report, NVIDIA
GPU Technology Conference, 2020. Die Size: 826mm2; Accessed: 2025-05-17.
[32] NVIDIA Corporation. Nvidia h100 tensor core gpu architecture whitepaper. Technical report, NVIDIA
GPU Technology Conference, 2022. Die Size: 814mm2; Accessed: 2025-05-17.
25
