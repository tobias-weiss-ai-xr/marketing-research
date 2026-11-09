---
title: Regime-Adaptive Continual Learning for Portfolio Management
url: https://arxiv.org/abs/2606.00143
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Chaofan Pan
- Lingfei Ren
- Linbo Xiong
- Yonghao Li
- Wei Wei
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.00143
pages: 12
chars: 70372
fetched_at: '2026-11-08T13:08:47+00:00'
kb_version: 1
---

# Regime-Adaptive Continual Learning for Portfolio Management

Regime-Adaptive Continual Learning for Portfolio Management
Chaofan Pan
pan.chaofan@foxmail.com
Southwestern University of Finance
and Economics
Chengdu, Sichuan, China
Lingfei Ren
renlf@swufe.edu.cn
Southwestern University of Finance
and Economics
Chengdu, Sichuan, China
Linbo Xiong
xlb_beiqi@outlook.com
Southwestern University of Finance
and Economics
Chengdu, Sichuan, China
Yonghao Li
liyonghao@swufe.edu.cn
Southwestern University of Finance
and Economics
Chengdu, Sichuan, China
Wei Wei
weiwei@sxu.edu.cn
Shanxi University
Taiyuan, Shanxi, China
Xin Yang∗
yangxin@swufe.edu.cn
Southwestern University of Finance
and Economics
Chengdu, Sichuan, China
Abstract
Financial markets are inherently non-stationary, exhibiting fre-
quent regime shifts and structural changes that render traditional
Portfolio Management (PM) approaches ineffective. Existing reme-
dies, such as rolling-window retraining and naive online fine-tuning,
are hindered by high computational costs and insufficient knowl-
edge utilization, respectively, resulting in low returns and limited
adaptability. Continual learning (CL) offers a promising paradigm
by enabling trading agents to accumulate and transfer knowledge
across sequential tasks. In this paper, we proposeRegime-aware
ContinualAdaptivePortfolio management (ReCAP), a novel frame-
work that integrates CL into PM to address the challenges of dy-
namic financial environments. ReCAP employs an adaptive regime
detection module to segment historical market data into variable-
length regimes, enabling regime-specific learning of policy vectors
and the construction of a policy library. During continual trading,
a regime-gate module adaptively combines policy vectors from
the library based on the current market state, facilitating rapid
adaptation to newly detected regimes. Only the regime-gate and
the current regime’s policy vector are continually updated to pre-
serve useful knowledge effectively. Extensive experiments on five
real-world datasets demonstrate that ReCAP consistently outper-
forms popular baselines, achieving superior returns in long-term
investment horizons and rapid adaptation to regime shifts.
CCS Concepts
•Computing methodologies → Lifelong machine learning;•
Applied computing→Economics.
Keywords
Portfolio Management; Continual Learning; Continual Reinforce-
ment Learning; Regime Adaptation
∗Corresponding Author.
This work is licensed under a Creative Commons Attribution 4.0 International License.
KDD 2026, Jeju Island, Republic of Korea.
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2259-2/2026/08
https://doi.org/10.1145/3770855.3817620
ACM Reference Format:
Chaofan Pan, Lingfei Ren, Linbo Xiong, Yonghao Li, Wei Wei, and Xin Yang.
2026. Regime-Adaptive Continual Learning for Portfolio Management. In
Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and
Data Mining V.2 (KDD 2026), August 9–13, 2026, Jeju Island, Republic of Korea.
ACM, New York, NY, USA, 12 pages. https://doi.org/10.1145/3770855.3817620
1 Introduction
The stock market, with a total market capitalization exceeding $90
trillion, has attracted the attention of investors worldwide [ 52].
Portfolio Management (PM), which dynamically allocates capital
proportions among different assets, plays a pivotal role in maxi-
mizing returns [1, 45] and controlling risk for investors [ 14, 19].
With the recent advancements in deep learning and Reinforcement
Learning (RL) [34, 41], quantitative trading has revolutionized PM
by leveraging computational models to execute trades with unprece-
dented speed and precision [3, 29]. However, financial markets are
characterized by persistent non-stationarity and frequent structural
shifts [9, 33], posing fundamental challenges for the design of ro-
bust and adaptive trading policies. While RL-based methods enable
the trade agents to learn flexible trading policies through direct in-
teraction with the market environment [47, 51], these agents often
encounter rapid performance degradation when deployed in real-
world environments [24]. This phenomenon, commonly referred to
as “alpha decay”, arises as the market adapts to and arbitrages away
profitable policies [37], in line with the predictions of the Efficient
Market Hypothesis [42]. As a result, policies trained on offline data,
under the assumption of stationarity, frequently fail to sustain their
edge in the face of evolving market regimes and volatility shifts.
Continual Learning (CL) extends the static learning framework
by enabling systems to learn across a sequence of tasks, incremen-
tally accumulating and transferring knowledge over time [2, 25].
CL has shown significant promise in various non-stationary do-
mains, as it offers mechanisms to mitigate catastrophic forgetting
and facilitate rapid adaptation to new tasks [12, 16, 36]. However,
the application of CL in PM remains largely underexplored, and
existing methods seldom exploit the unique characteristics of finan-
cial markets, such as regime-driven dynamics and the recurrence
of market states [4, 17, 39]. This gap motivates the development of
new approaches that seamlessly integrate regime-aware CL with
PM, empowering trading agents to achieve robust performance in
real-world, ever-changing financial environments.
arXiv:2606.00143v1  [q-fin.PM]  29 May 2026

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Chaofan Pan et al.
Pretraining Policy 0 Testing  Policy 0 Training  Policy 1
Regime 1Historical Data
BTC/USDT
XRP/USDT
AAPL
Regime 3Regime 2
AMGN
Testing  Policy 1
Training  Policy 2
Testing  Policy 2
Training  Policy 3
Start Date
...
Figure 1: Illustration of the continual portfolio management
problem. The multi-asset market evolves over time and is seg-
mented into a sequence of regimes, each marked by distinct
statistical properties. Historical data is used for pre-training,
while subsequent regimes are detected and used for contin-
ual training and testing in an alternating fashion.
Building on the advances of CL, we propose to tackle PM as a
CL problem under non-stationary market conditions. As illustrated
in Figure 1, the problem of “continual portfolio management”
is a sequence of non-stationary decision-making tasks. The agent
interacts with a multi-asset market environment whose statisti-
cal properties and underlying dynamics may shift abruptly over
time due to structural changes, volatility spikes, or macroeconomic
events. The entire market history is first used for offline pre-training,
providing a foundation for the agent’s initial knowledge. As the
market evolves, the data is segmented into a series of regimes, each
corresponding to a distinct period with relatively stable characteris-
tics. At each regime boundary, the agent detects the shift, uses data
from the previous regime for training, and then tests or deploys
the learned policy in the subsequent regime. The core objective is
to maximize long-term returns by continuously adapting to new
regimes, efficiently transferring knowledge from previously en-
countered market conditions. This CL process is more realistic and
poses unique challenges: (1) How to detect and segment regime
shifts in real time; (2) How to retain and reuse regime-specific exper-
tise without incurring excessive computational or memory costs;
and (3) How to dynamically combine historical and newly acquired
knowledge to enable rapid adaptation to novel market conditions.
To address these challenges, we propose a novel framework
namedReCAP(Regime-awareContinualAdaptivePortfolio man-
agement), which leverages advances in CL to enable robust and
adaptive PM in non-stationary markets. ReCAP is designed to sys-
tematically detect market regime shifts, efficiently retain and reuse
regime-specific expertise, and dynamically integrate historical and
novel knowledge for rapid adaptation. Firstly, our framework em-
ploys an adaptive regime detection module, which segments the
historical market data into variable-length regimes. Secondly, the
agent incrementally fine-tunes its policy for each regime to obtain
a policy vector, which is then adaptively stored in a policy library.
Thirdly, a regime-gate module is introduced during continual trad-
ing to assign attention weights to policy vectors in the library based
on the current market state, enabling the agent to synthesize an
effective trading policy tailored to the prevailing regime. Only the
regime-gate and the current regime’s policy vector are updated
continually, which supports efficient knowledge accumulation. By
introducing an adaptive regime detection module, policy vectors, a
policy library, and a regime-gate module, ReCAP provides a unified
solution to the challenges of continual PM in real-world, dynamic
financial environments.
In summary, this paper makes the following contributions:
• We formulate and address the continual PM problem, ex-
plicitly modeling the non-stationary nature of real-world
financial markets as a sequence of regime-aware decision-
making tasks, and highlighting the necessity of continual
adaptation for robust trading performance.
• We propose ReCAP, a novel continual PM framework that
integrates adaptive regime detection, regime-specific policy
learning and maintenance, and regime-aware policy com-
position into a unified framework for efficient knowledge
accumulation and rapid adaptation.
• We conduct extensive empirical studies on five real-world
datasets, covering US and Japanese stock markets as well as
commodity ETFs, demonstrating that ReCAP consistently
outperforms strong baselines across multiple metrics.
2 Related Works
Portfolio Management is a critical task in finance, involving the
allocation of capital across multiple assets to achieve specific in-
vestment objectives such as maximizing returns or minimizing risk.
Pioneering studies, including Universal Portfolios (UP) [ 6], Con-
stant Rebalanced Portfolios (CRP) [18], Exponential Gradient (EG)
[18], M0 [7], Anti-Correlation (Anticor) [8], and Online Newton
Step (ONS) [3], have been proposed to achieve a high-profit invest-
ment. These methods typically rely on classical financial theories
such as mean-variance optimization [10] and factor models [13],
which assume relatively stable market dynamics and often require
strong assumptions about asset return distributions. While these
methods provide foundational insights, their performance can dete-
riorate in complex, non-stationary financial environments [51, 54].
Moreover, traditional methods typically lack the flexibility to incor-
porate market impact and evolving market information in a unified
framework.
RL has emerged as a powerful alternative paradigm for PM by for-
mulating the investment decision process as a sequential decision-
making problem [41]. Unlike supervised learning methods [5], RL
agents learn adaptive trading policies through direct interaction
with the market environment, optimizing long-term, risk-adjusted
returns while naturally incorporating transaction costs and con-
straints. Early works, such as EIIE [ 22] and FinRL [ 31], laid the
groundwork for applying deep RL algorithms to PM. More recent
developments have focused on enhancing expressiveness and ro-
bustness. SARL [51] introduced state augmentation techniques to

Regime-Adaptive Continual Learning for Portfolio Management KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
better capture asset dynamics, while HRPM [46] proposed hierarchi-
cal RL frameworks to separate long-term PM from short-term exe-
cution, effectively reducing trading costs. Advances in graph neural
networks [43] and multi-agent systems [28] further improved the
modeling of asset correlations.
Despite these successes, existing RL-based PM methods predom-
inantly assume stationary or slowly varying market conditions
and generally rely on offline training or periodic retraining with
fixed windows. It is essential to integrate CL principles into the
RL-based method, enabling agents to adapt to dynamic financial
markets. Although two recent studies have attempted to apply con-
tinual RL to algorithmic trading, they primarily focus on short-term,
single-asset environments with fixed intervals and lack sufficient
comparison [23, 24]. Additionally, CL methods have not been ex-
plored in the context of PM. To address these gaps, we propose
a novel CL framework for PM on long-term, multi-asset environ-
ments with adaptive regime detection, enabling rapid adaptation
to non-stationary market conditions.
3 Problem Formulation
Definitions.Let 𝑁 denote the number of tradable assets in the
market. At each time step𝑡, the market observation is denoted as
X𝑡 ={𝑥 𝑡,1,...,𝑥 𝑡,𝑁}, where𝑥𝑡,𝑖 represents the feature vector (e.g.,
OHLCV and technical indicators) for asset𝑖. The portfolio allocation
at time𝑡is represented by the weight vectorw 𝑡 =[𝑤 𝑡,0,𝑤𝑡,1,
...,𝑤 𝑡,𝑁], where𝑤𝑡,𝑖 is the proportion of capital allocated to asset
𝑖. The portfolio value at time𝑡is denoted as𝑉 𝑡 .
Portfolio Management.The trading agent interacting with a fi-
nancial market environment can be modeled as a Markov Decision
Process (MDP)(S,A,R,T,𝛾) [31, 50, 53], whereS is the state
space,A is the action space,R :S×A→R is the reward func-
tion,T :S×A×S → [ 0, 1] is the transition dynamics, and
𝛾∈[ 0, 1) is the discount factor. At each discrete time step 𝑡, the
trading agent observes the trading states 𝑡∈S , follows a policy
𝜋 :S→A to select a portfolio allocation actiona𝑡≡ w𝑡∈A , and
receives a reward𝑟𝑡 =R( s𝑡, a𝑡) reflecting the portfolio return. The
state transitions to the next states𝑡+1 according to the transition
dynamics.
Specifically, the states𝑡 =𝑓(𝑋 𝑡∪H𝑡) consists of the latest multi-
asset market features, where𝑓 andH𝑡 denote a feature extraction
function and optional historical features, respectively. The action
w𝑡 is the portfolio weight vector at time𝑡, which is subject to the
constraints ˝𝑁 𝑖=0𝑤𝑡,𝑖 = 1and 𝑤𝑡,𝑖 ≥ 0. The immediate reward is
the log portfolio return𝑟𝑡 =log

𝑉𝑡
𝑉𝑡−1

, where𝑉𝑡 is the portfolio
value at time𝑡. The transition dynamics are implicitly defined by
the market evolution, which is influenced by the agent’s actions
and external factors.
Continual Portfolio Management.We formulate the continual PM
problem as an MDP under regime-shifting market conditions. In
the real world, the financial market is inherently non-stationary
and can be viewed as a sequence of regimes,{𝜏1,𝜏 2,...,𝜏 𝑀}, where
each regime 𝜏𝑘 corresponds to a contiguous time segment with
relatively stable statistical properties. As time progresses, regime
boundaries and their characteristics are typically unknown in ad-
vance. To model this, we formulate the continual PM as a CRL
problem with dynamic MDP:(S,A,R 𝑘,T𝑘,𝛾) . Within each regime
𝜏𝑘, the underlying transition dynamicsT𝑘 and reward functionR𝑘
may differ, reflecting changes in market volatility or return distribu-
tions. Thus, the agent faces a sequence of related PM tasks, where
the optimal policy may shift as the regime changes.
The CRL process alternates between adaptation and deployment.
After a regime boundary is detected, the agent trains on the com-
pleted regime𝜏𝑘−1 underT𝑘−1 andR𝑘−1 to capture its dynamics.
The adapted policy𝜋𝑘−1 is then deployed to make portfolio alloca-
tion decisions in the subsequent regime 𝜏𝑘 until the next regime
shift is detected. The objective is to maximize cumulative portfolio
return over the entire time horizon:
max
{𝜋𝑘−1}𝑀 𝑘=1
E
" 𝑀∑︁
𝑘=1
|𝜏𝑘|−1∑︁
𝑡=0
𝑟(𝑘) 𝑡
#
,(1)
where𝜋𝑘−1 denotes the policy used in𝜏𝑘,|𝜏𝑘| denotes the number
of trading steps in regime𝜏𝑘, and𝑟(𝑘) 𝑡 =R 𝑘(s𝑡, a𝑡) is the reward at
time𝑡under regime-specific dynamicsT 𝑘(·).
4 Method
This section presents our proposed framework for continual PM.
We first provide an overview of ReCAP, followed by detailed de-
scriptions of its core components: theAdaptive Regime Detection
module(ARD), thepolicy vector and policy library, and theRegime-
Gate Module(RGM). The overall workflow of ReCAP is summarized
in Algorithm 1 and Algorithm 2.
4.1 Overview
Figure 2 illustrates the overall workflow of ReCAP. It consists of
two main stages:pretrainingandcontinual trading.
Pretraining Stage.We begin by training a base PM policy pa-
rameterized by 𝜃0 on extensive historical market data covering
a long time horizon. This offline pretraining employs a standard
RL algorithm to learn a robust initial policy that captures general
market dynamics. Next, the ARD analyzes the historical data to iden-
tify structural change points and partitions the data into multiple
regimes{𝜏(0,1),···,𝜏 (0,𝐾)}, each representing a period with rela-
tively stable market characteristics. For each detected regime𝜏(0,𝑗) ,
the base policy𝜃0 is fine-tuned to adapt to regime-specific dynamics,
producing a policy𝜃𝑗 and a policy vectord 𝑗 =𝜃 𝑗−𝜃 0. Collectively,
these vectors are merged to form a policy libraryD =[ d1,···, d𝐾],
which is stored for reuse.
Continual Trading Stage.During continual trading, the frame-
work continuously monitors the market and applies the ARD in real
time to detect regime shifts. If a regime boundary is detected, the
completed regime segment is used for adaptation to produce a new
policy vectord new, which is then available for subsequent trading.
Specifically, at each time step 𝑡, the policy network receives the
asset-level trading states𝑡 , while the RGM receives a market-level
regime feature vectorm𝑡 constructed from market indicators and
aggregated asset information. The RGM outputs a weight vector𝜶𝑡
over the policy library and, during adaptation, the current regime
vector. The effective policy parameter at time𝑡 is then composed
as:
𝜃𝑡 =𝜃 0+ ˜D𝜶𝑡, ˜D=[D,d new,𝑡],(2)

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Chaofan Pan et al.
RGMFrozen
Learnable
Start Date
Pretraining Continual Trading
ARD
Segments
Historical Data RL
Finetune
RL Policy Network
Market
Feature
Softmax
Policy LibraryRegimes
Finetune
Finetune
Training on Regime 1 Testing
ARD Detected
RGM
Softmax
Figure 2: Overview of the ReCAP’s workflow. The offline pretraining stage produces a base policy. The Adaptive Regime
Detection module (ARD) segments historical data into distinct regimes. Each regime is used to fine-tune the base policy,
yielding regime-specific policy vectors and building the policy library. In the continual trading stage, real-time ARD triggers
the Regime-Gate Module (RGM) to dynamically combine stored policy vectors with the current policy vector, producing the
current policy network. A new policy vector is trained and adaptively merged into the policy library. During testing, a daily
state is processed by a dynamic policy network consisting of the base policy, policy library, and RGM to obtain a portfolio
weight.
whered new,𝑡 is the policy vector being learned for the current
regime at time 𝑡, andd new,0 is initialized as zero. The portfolio
weightw𝑡 is computed as:
w𝑡 = exp(o𝑡) ˝𝑁
𝑖=0 exp(𝑜𝑡,𝑖)
,o 𝑡 =𝑓 𝜃𝑡(s𝑡), (3)
wheres 𝑡 is the current state, 𝑓𝜃𝑡 is the policy network parame-
terized by𝜃𝑡 . Only the RGM parameters𝜙 andd new are updated
during training, while𝜃0 andDremain fixed to preserve the learned
knowledge. After training, the new policy vectord new is adaptively
merged into the policy libraryD, accumulating regime-specific
knowledge over time.
In testing, the ARD and the RGM operate jointly with the base
policy𝜃0 and the policy vector libraryDto generate dynamic policy
parameters for each state. The portfolio weight vectorw𝑡 is then
computed from the current trading states 𝑡 using the composed
policy. This design enables efficient zero-shot inference and robust
adaptation to evolving market regimes.
4.2 Adaptive Regime Detection Module (ARD)
A key challenge in continual PM is to identify and segment the mar-
ket into regimes. Accurate detection enables the agent to localize
adaptation and facilitates the building of regime-specific expertise.
To achieve this, we propose the ARD to segment the market into
regimes with approximately stationary dynamics.
Given a sequence of market observations{X𝑡}𝐿 𝑡=1 with length𝐿,
the goal is to partition the market into𝑀 regimes{𝜏1,𝜏 2,...,𝜏 𝑀}
such that each regime 𝜏𝑘 =[𝑡 start 𝑘 ,𝑡 end 𝑘 ] corresponds to a time
interval with approximately stationary dynamics. Letm 𝑡 denote
the market-level feature vector at time 𝑡, which includes indica-
tors such as VIX, turbulence, and aggregated asset statistics. The
regime detection task reduces to identifying a set of change points
C={𝑐 1,𝑐 2,...,𝑐 𝑀−1} such that the distribution ofm 𝑡 changes
significantly at each𝑐𝑖.
We employ a variant of the cumulative sum algorithm [48] to
detect abrupt changes in the distribution of selected market fea-
tures. For a chosen regime-sensitive scalar feature𝑢𝑡 , the statistic
is defined as:
𝑆𝑡 =max(0,𝑆 𝑡−1+(𝑢 𝑡−𝜇 0)−𝜅),(4)
where 𝜇0 is a reference mean estimated from a historical refer-
ence window, and𝜅> 0is a drift parameter controlling detection
sensitivity. A regime change is signaled whenever 𝑆𝑡 exceeds a
predetermined thresholdℎ. After each detected change point, the
statistic is reset to zero and𝜇0 is re-estimated on the subsequent
reference window. This procedure is applied in parallel to multi-
ple features, and the union of detected change points is used for
segmentation:
C=
Ø
𝑢∈U
C𝑢,(5)
whereU is the set of market-level features inm𝑡 , andC𝑢 denotes
the set of change points detected on feature𝑢.
Given the set of change pointsC, the market data is partitioned
into regimes:
𝜏1 =[1,𝑐 1],···,𝜏 𝑀 =[𝑐 𝑀−1+1,𝐿].(6)
Each regime𝜏𝑘 is then treated as a distinct task for regime-specific
policy adaptation. During the continual trading stage, the ARD

Regime-Adaptive Continual Learning for Portfolio Management KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
operates in an online fashion, sequentially updating the statistic𝑆𝑡
and flagging a new regime whenever a change point is detected.
4.3 Policy Vector and Policy Library
In CL, leveraging knowledge from previous tasks in dynamic envi-
ronments is crucial to enhance agent performance in subsequent
tasks. Therefore, we introduce the concept of policy vector and build
a policy library to facilitate efficient knowledge retention and flexi-
ble reuse across different market regimes, inspired by model editing
techniques [20]. Then, we store regime-specific knowledge as a
set of policy vectors and adaptively maintain the library through
merging and pruning.
For each detected regime𝜏(0,𝑗) , we initialize the policy param-
eters as𝜃0 and fine-tune them on regime-specific data to obtain
adapted parameters 𝜃𝑗 . The policy vector is then defined as the
learned parameters that adapt the base policy to a specific regime:
d𝑗 =𝜃 𝑗−𝜃 0.(7)
The set of all such vectors forms the policy libraryD=[ d1,..., d𝐾]∈
R𝑃×𝐾 , where𝑃 is the dimension of the policy parameter space. A
linear combination of multiple policy vectors enables the model
to reuse policy from previous regimes [ 26]. This highlights the
potential of policy vectors to facilitate continual adaptation.
To maintain a compact and informative policy library, we em-
ploy an adaptive merging mechanism that dynamically updates the
library based on the similarity of policy vectors. After generating
all policy vectors from pretrain data, we compute the similarity
between every pair of vectors. If the similarity between two vectors
d𝑖 andd 𝑗 exceeds a threshold𝛿 s, they are merged by averaging:
dm = 1 2(d𝑖+d 𝑗).(8)
Moreover, non-informative policy vectors whoseℓ2-norm is very
small are discarded, as they do not contribute significantly to the
policy adaptation process. When a new regime is encountered and
a new policy vectord new is learned, it is first temporarily added
toD. If the average attention weight from the RGM assigned to
dnew is close to zero, or if itsℓ2-norm is very small, the new vector
is discarded. This indicates that the new regime does not require
significant adaptation from the base policy and the policy library,
and a combination of previous policy vectors is sufficient. Other-
wise,d new is merged with existing vectors inDusing the same
similarity-based criterion as above. This mechanism reduces redun-
dancy and ensures that the policy library retains only distinct and
useful regime adaptations.
4.4 Regime-Gate Module (RGM)
The RGM is designed to dynamically synthesize an effective trad-
ing policy by adaptively weighting the policy vectors in the library
according to the current market regime. At each time step 𝑡, the
market-level feature vectorm𝑡 is fed into a neural network param-
eterized by𝜙:
𝜶𝑡 =Softmax(𝑔 𝜙(m𝑡)),(9)
where 𝜶𝑡 =[𝛼 1 𝑡,𝛼 2 𝑡,...,𝛼 𝐾 𝑡] is a weight vector, 𝐾 is the number
of policy vectors in the library, and 𝜶𝑡 is the attention weight
vector over the policy library. During inference, the current policy
Algorithm 1: Pretraining for ReCAP
Input: Historical market data{X 𝑡}𝑇 𝑡=1
Output: Base policy parameter𝜃 0, policy libraryD
1:// Step 1: Offline base policy learning
2: Train policy network 𝑓𝜃0 on{X𝑡}𝑇 𝑡=1 using standard RL algo-
rithm;
3:// Step 2: Regime segmentation
4: Apply ARD to{X𝑡}𝑇 𝑡=1 to detect change pointsC and partition
data into regimes{𝜏(0,1),...,𝜏 (0,𝐾)};
5:Initialize policy libraryD←∅;
6:foreach regime𝜏 (0,𝑗) do
7:Initialize𝜃 𝑗←𝜃 0;
8:Fine-tune𝜃 𝑗 on data in𝜏(0,𝑗) via RL algorithm;
9:Compute policy vectord 𝑗 by Eq. (7);
10:Addd 𝑗 toD;
11:end for
12:// Step 3: Policy vector merging
13:For all pairs(d 𝑖,d𝑗)inD, merge by Eq. (8) if similarity>𝛿 s;
14:Remove policy vectors with smallℓ 2-norm fromD;
15:return𝜃 0,D;
Table 1: Information about five datasets.
Dataset Assets Training Period Evaluation Period
DOW30 29 2008-05-01 to 2020-04-30 2020-05-01 to 2025-04-29
NAS100 73 2008-05-01 to 2020-04-30 2020-05-01 to 2025-04-29
SP500 398 2008-05-01 to 2020-04-30 2020-05-01 to 2025-04-29
NIKKEI30 29 2008-05-01 to 2020-04-30 2020-05-01 to 2025-04-29
COMMODITY_ETF 7 2008-05-01 to 2020-04-30 2020-05-01 to 2025-04-29
parameter is composed as:
𝜃𝑡 =𝜃 0+D𝜶 𝑡.(10)
During training on each regime, the output head of the RGM is
first expanded to output a new weight𝛼new 𝑡 for the current regime
policy vectord new,𝑡. Only the regime-gate parameters 𝜙 and the
current regime’s policy vectord new are updated via RL algorithms,
while𝜃0 andDremain fixed. After training, the new policy vector
dnew is adaptively merged into the policy libraryD, as described in
Section 4.3. If the new policy vector is discarded, the output head
of the RGM is pruned to output only the weights for the existing
policy vectors in the library.
5 Experiments
5.1 Experimental Setup
Datasets.We conduct our experiments on five datasets covering
diverse financial markets. For US equity markets, we use three
widely adopted benchmarks: DOW30, NAS100, and SP500. We
also introduce the Japanese market dataset NIKKEI30, which con-
tains 29 Nikkei component stocks, and the commodity ETF dataset
COMMODITY_ETF, which includes 7 mainstream commodity ETFs
(Gold, Silver, Combined Commodity Index, Crude Oil, Natural Gas,
Agricultural, and S&P GSCI). The raw data is obtained from Yahoo
Finance, and we select constituent stocks with continuous listing
and data availability throughout the entire period, resulting in 29,
73, 398, 29, and 7 assets for DOW30, NAS100, SP500, NIKKEI30,
and COMMODITY_ETF, respectively. The daily data spans from

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Chaofan Pan et al.
Table 2: Performance comparison of thirteen PM methods and ReCAP on DOW30, NAS100 and SP500. The mean and standard
deviation of the results are reported for RL-based methods. Results in bold show the best results on each dataset.
Dataset DOW30 NAS100 SP500
Method CR%↑SR↑MDD%↓ CR%↑SR↑MDD%↓ CR%↑SR↑MDD%↓
Rule-
based
B&H 84.10 0.88 20.91 123.41 0.92 25.37 111.00 0.92 19.84
CRP 62.41 0.74 23.01 83.10 0.73 30.76 74.44 0.74 24.51
EG 62.37 0.74 23.03 82.92 0.73 30.94 74.28 0.74 24.55
UP 62.33 0.74 23.00 83.16 0.73 30.79 74.37 0.74 24.51
OLMAR -68.38 -0.47 82.99 -90.98 -0.72 95.59 -93.27 -0.78 96.38
WMAMR -5.57 0.12 60.13 -89.98 -0.87 94.27 -61.50 -0.20 78.76
RL-
based
A2C 80.28±11.37 0.85±0.08 20.59±2.13 126.10±5.34 0.93±0.02 24.95±0.77 112.08±3.15 0.92±0.02 19.98±0.57
PPO 84.34±1.49 0.88±0.01 20.92±0.18 123.54±1.30 0.92±0.01 25.37±0.17 111.08±0.22 0.92±0.00 19.82±0.01
SAC 85.86±5.23 0.89±0.04 20.84±1.02 123.54±7.44 0.92±0.03 25.27±0.94 111.55±2.40 0.92±0.01 19.98±0.64
EIIE 83.17±0.95 0.87±0.01 20.92±0.10 123.33±0.32 0.92±0.00 25.35±0.04 110.99±0.02 0.92±0.00 19.84±0.00
SARL 78.69±1.85 0.84±0.02 21.07±0.29 111.87±0.78 0.86±0.00 25.37±0.19 103.93±0.29 0.89±0.00 19.83±0.07
Cross-Insight 90.31±9.30 0.89±0.06 20.85±1.09 125.37±4.93 0.91±0.02 25.73±0.96 110.83±2.54 0.92±0.01 19.92±0.64
AlphaGAT 73.45±0.00 0.80±0.00 21.46±0.00 123.38±0.00 0.91±0.00 25.36±0.00 111.02±0.01 0.92±0.00 19.84±0.00
ReCAP 96.76±2.26 1.00±0.02 17.58±0.48 164.89±2.54 1.14±0.01 23.86±0.35 145.02±1.40 1.14±0.01 19.19±0.13
Table 3: Performance comparison on NIKKEI30 and COMMODITY_ETF.
Dataset NIKKEI30 COMMODITY_ETF
Method CR%↑SR↑MDD%↓ CR%↑SR↑MDD%↓
Rule-
based
B&H 122.77 0.94 25.12 88.75 0.86 26.28
CRP 99.71 0.68 25.24 74.47 0.66 26.18
EG 99.82 0.68 25.41 74.98 0.65 26.18
UP 99.90 0.68 25.36 73.45 0.64 26.68
OLMAR -68.11 -0.36 72.49 -52.18 -0.11 80.03
WMAMR -52.59 -0.23 60.50 -71.60 -0.35 86.22
RL-
based
A2C 124.32±9.21 0.95±0.04 24.72±1.11 92.42±19.37 0.89±0.13 23.43±6.61
PPO 122.55±2.26 0.94±0.01 25.24±0.29 88.44±6.11 0.87±0.03 25.92±1.65
SAC 120.63±6.46 0.92±0.02 25.47±1.04 83.06±14.76 0.82±0.11 27.50±3.72
EIIE 123.08±0.73 0.94±0.00 25.10±0.12 87.83±6.72 0.86±0.05 26.15±1.65
SARL 116.08±2.72 0.91±0.00 25.00±0.19 79.22±5.15 0.81±0.05 26.63±3.18
Cross-Insight 127.70±9.03 0.94±0.05 26.41±1.41 97.13±16.11 0.83±0.10 28.15±2.57
AlphaGAT 122.59±0.00 0.93±0.00 25.09±0.00 87.09±0.15 0.86±0.00 25.86±0.00
ReCAP 133.29±5.26 1.00±0.02 23.69±0.69 97.80±2.00 0.95±0.02 22.88±0.51
May 1, 2008, to April 29, 2025, covering a total of 17 years that en-
compass various market regimes, including bull and bear markets,
financial crises, and periods of high volatility. The first 12 years are
designated as the offline training set, while the subsequent 5 years
are reserved for online evaluation. The statistics of the datasets are
summarized in Table 1.
For feature engineering, the raw data includes daily open, high,
low, close prices, and trading volume for each asset. We compute
adjusted prices, Moving Average Convergence Divergence (MACD),
Bollinger Bands, and 17 common technical indicators to enrich the
feature set. Additional features include turbulence and VIX, which
are incorporated to facilitate regime detection. To avoid look-ahead
bias and ensure realistic evaluation, all pre-processing steps, in-
cluding feature engineering and normalization, are performed in a
strictly time-series fashion, using only past and current informa-
tion at each time step. For reproducibility, the asset-level trading
state uses 26 features per asset: open, high, low, close, volume,
MACD, Bollinger upper and lower bands, RSI-30, CCI-30, DX-30,
30-day and 60-day moving averages, adjusted-price returns over
5/10/15/20/25/30 days, normalized open/high/low prices, adjusted-
price return, close return, VIX, and turbulence. The market-level
input used by ARD and the RGM consists of six regime-sensitive
signals: VIX, turbulence, Bollinger upper and lower bands, the 5-day
adjusted-price return, and RSI-30.
Evaluation Metrics.To comprehensively evaluate the perfor-
mance and robustness of PM methods, we employ three of the
widely accepted financial metrics, includingCumulative Return
(CR),Sharpe Ratio(SR), andMaximum DrawDown(MDD). These
metrics capture different aspects of portfolio performance, includ-
ing profit, risk-adjusted profit, and risk. They are computed online
over the entire test period unless otherwise specified. Moreover,
we follow the standard practice of CL [ 35, 38, 49] and use three
metrics based on the agent’s profit throughout different phases of
its trading process:A verage Performance(AP),Forgetting(FG), and
Forward Transfer(FT) [36].
Baselines.To ensure a comprehensive evaluation, we select a
range of representative methods, including six rule-based and seven
RL-based methods. Rule-based methods include Buy and Hold
(B&H), CRP [ 18], EG [ 18], UP [ 6], OLMAR [ 29], and WMAMR
[11], which are implemented based on PGPortfolio [22]. RL-based
methods include A2C [32], PPO [40], SAC [15], EIIE [22], SARL [51],
Cross-Insight [54], and AlphaGAT [30], which are implemented
based on FinRL [31]. Among them, EIIE is the first work formulating
PM as an MDP with parallel independent evaluators; SARL aug-
ments the state with price movement predictions; Cross-Insight inte-
grates multi-horizon investment insights; and AlphaGAT employs a
two-stage framework with a CATimeMixer network for alpha factor
mining. For CL strategies, we compare with rolling-window Retrain-
ing (Retrain), continuous Finetuning (Finetune), Experience Replay

Regime-Adaptive Continual Learning for Portfolio Management KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Algorithm 2: Continual Trading with ReCAP
Input: Daily market dataX, base policy 𝜃0, policy libraryD, RGM
parameters𝜙, data bufferB, ARD statistics𝑆
Output: Portfolio weightsw, updatedD,𝜙,Band𝑆
1:// Step 1: Portfolio weights computation
2:Obtain trading states 𝑡 and market-level featuresm𝑡 ;
3:Compute policy weights𝜶by Eq. (9);
4:Compose policy parameters𝜃by Eq. (10);
5:Compute portfolio weightswby Eq. (3);
6:// Step 2: Regime detection
7:Update ARD statistics𝑆by Eq. (4);
8:ifregime change detectedthen
9:// Step 3: Regime-specific training
10:Initialized new←0;
11:Expand the output head of RGM;
12:Updated new and𝜙by RL onB, keeping𝜃 0,Dfixed;
13:// Step 4: Policy vector merging and library update
14: ifaverage weight ofd new is small or∥dnew∥2 is smallthen
15:Discardd new;
16:Prune the output head of RGM;
17: else ifthe similarity betweend new and any policy vector in
D>𝛿 s then
18:Merged new intoDby Eq. (8);
19:Prune the output head of RGM;
20:else
21:D←[D,d new];
22:end if
23:Resetd new←0, clearB;
24:else
25:Store(s 𝑡,m𝑡,𝑟𝑡)into bufferB;
26:end if
27:returnportfolio weightsw, updatedD,𝜙,B, and𝑆;
(ER) [21] with a buffer size of 3,000, EWC-regularized finetuning
[27] with a regularization coefficient of 1,000, and Constrained Ra-
tionals (CoR) [44], all using PPO as the underlying RL algorithm.
The Retrain window size is set to 12 years, matching the training
period.
Implementation Details.We implement our framework via Py-
Torch and FinRL [31]. For each RL-based method, we use 10 different
random seeds and report the average results and standard devia-
tions to account for stochasticity. We match the total RL update
budget across RL-based methods, setting the training steps on each
task to10 4 for methods that require task segmentation. The actor
and critic networks each consist of 2 layers of MLP with Tanh ac-
tivation function, with an embedding dimension of 64. The input
state has dimensions of(𝐵,𝐹,𝑁) , where𝐵= 256is the batch size,
𝐹= 26is the number of features per asset, and 𝑁 is the number
of assets. We use z-score normalization to standardize features for
training stability. All methods use Adam optimizer with a learn-
ing rate of10 −4, and transaction costs are set to 10 basis points
per trade. For SARL, EIIE, AlphaGAT and ReCAP, PPO is used as
the underlying RL algorithm, while Cross-Insight uses its official
SAC-based implementation. For ReCAP, we set𝜅 andℎ to 0.5 and
2.5 times the standard deviation based on statistical experience,
respectively. The threshold for merging similar policy vectors𝛿s
is set to 0.5. Following recent work in continual RL, policy vector
learning and reuse are applied only to the actor, while the critic is
reinitialized at each regime. 1
5.2 Comparative Analysis
To comprehensively evaluate the effectiveness and adaptability
of our proposed framework, we conduct extensive comparative
experiments against a diverse set of baseline methods. Our analysis
is structured along two main axes: (1) comparison with established
PM algorithms, including both traditional and RL-based methods,
and (2) comparison with different CL strategies within the RL-based
PM paradigm.
5.2.1 Comparison with PM Methods.Table 2 shows the perfor-
mance of ReCAP and other PM methods on the three datasets. All
methods are trained on the entire training period and evaluated on
the test period, while ReCAP is also continuously trained on the
test period. To ensure a fair comparison, the total training budget
of ReCAP is matched to that of the other RL-based PM methods.
We further report matched rolling-window adaptation results for
the main PM baselines in Appendix B. Under a matched adaptive
protocol on NAS100, using a 360-day window, a 90-day retraining
frequency, a 180-day minimum window, and10 4 update steps per
stage, the strongest adaptive baseline reaches 124.24% CR and 0.92
SR, while ReCAP achieves 164.89% CR and 1.14 SR.
Among rule-based methods, CRP, EG, and UP achieve moderate
returns but are generally limited by their inability to adapt to chang-
ing market conditions, resulting in higher drawdowns and lower
risk-adjusted returns. Notably, B&H’s portfolio values align with
market trends, as it evenly distributes capital across assets initially
and sells them all at the end of the period. Mean reversion-based
methods (OLMAR and WMAMR) perform significantly worse, of-
ten suffering large losses during long-term trading, highlighting
the vulnerability of static heuristics in non-stationary regimes.
RL-based methods demonstrate improved performance over
most rule-based strategies. Among RL baselines, PPO and SAC
achieve competitive results, with PPO serving as a strong baseline
with low standard deviation in most cases. In contrast, AlphaGAT
exhibits poor performance, likely due to its complex two-stage
architecture involving a CATimeMixer network. The significant
imbalance between its large parameter space and the limited sam-
ple size leads to severe overfitting. Cross-Insight, which integrates
multiple investment insights across different horizons, achieves
better performance than most RL baselines by effectively capturing
multi-scale market dynamics. Despite some advancements, most
RL methods still assume stationary environments and lack explicit
mechanisms for continual adaptation, which limits their ability to
capitalize on regime shifts and recurring patterns. In contrast, our
ReCAP framework achieves the best results across all datasets, with
an average cumulative return improvement of over6.45%− 38.79%
compared to the strongest baselines. The lowest maximum draw-
down of ReCAP further indicates enhanced risk management and
robustness to market turbulence.
1Code available at: https://github.com/Dumail/ReCAP

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Chaofan Pan et al.
2020-05-012020-08-252020-12-172021-04-152021-08-092021-12-012022-03-282022-07-222022-11-142023-03-132023-07-072023-10-302024-02-262024-06-202024-10-142025-02-10
Date
1.00
1.25
1.50
1.75
2.00
2.25
2.50
2.75Portfolio Value
1e6
B&H
CRP
UP
EG
SAC
PPO
A2C
EIIE
SARL
Cross-Insight
AlphaGAT
ReCAP
Figure 3: The portfolio values achieved by ReCAP and other
PM methods on the NAS100 dataset. OLMAR and WMAMR
are discarded due to their poor performance. The solid lines
represent the mean portfolio values of each method, while
the shaded areas indicate the standard deviation of the port-
folio values. The gray dashed line represents the start date
of each regime in ReCAP.
To verify the generalization capabilities of our proposed frame-
work across diverse financial markets, we further conduct exper-
iments on the NIKKEI30 and COMMODITY_ETF datasets, with
results presented in Table 3. Consistent with observations from the
US equity markets, ReCAP demonstrates superior performance on
both the Japanese equity market and the commodity ETF market.
Specifically, on the NIKKEI30 dataset, ReCAP achieves a Cumulative
Return (CR) of 133.29% and a Sharpe Ratio (SR) of 1.00, surpass-
ing the second-best baseline, Cross-Insight, which yields a CR of
127.70%. In the COMMODITY_ETF dataset, which exhibits distinct
volatility patterns compared to equities, ReCAP maintains its domi-
nance. These findings underscore the robustness of ReCAP and its
ability to effectively adapt to the unique dynamics of different asset
classes and market environments.
To visualize the performance differences, Figure 3 shows the
portfolio values achieved by ReCAP and other PM methods across
the NAS100. Results on other datasets are provided in the Appendix
B. From the figure, it is evident that our framework consistently
outperforms other models, regardless of the bull or bear market.
Specifically, ReCAP segments the test period into multiple variable-
length regimes and adapts its strategy accordingly, resulting in
superior performance. Furthermore, as the trading duration in-
creases, our method gradually accumulates knowledge of different
regimes through the Policy Library, making the gap between it
and other methods more pronounced and allowing it to achieve
greater excess returns. This demonstrates the advantage of ReCAP
in long-term trading scenarios.
5.2.2 Comparison with CL Strategies.To specifically investigate
the benefits of ReCAP, we compare with five CL strategies based on
PPO. Other details are provided in the Appendix B. The task bound-
aries for these baselines are determined using fixed-length windows
to match common practice in the literature. We additionally report
quarterly and yearly exogenous task boundaries in Appendix B,
which lead to the same qualitative conclusion.
Table 4: Performance comparison of five CL strategies and
ReCAP on three datasets. “Static” refers to training on the
entire training period and evaluating during the test period.
Dataset Strategy AP%↑FT%↑FG%↓
DOW30
Static 13.07±0.19 - -
Retrain 18.26±0.08 - -
Finetune 18.34±0.252.82±11.39 -1.88±5.67
ER 18.47±0.47 0.55±26.41 1.04±21.14
EWC 18.35±0.18 -1.90±4.11 0.78±1.75
CoR 18.31±0.30 1.60±10.02 3.89±10.39
ReCAP 24.92±0.651.35±3.83 -0.69±1.92
NAS100
Static 17.53±0.14 - -
Retrain 24.51±0.05 - -
Finetune 24.59±0.18 0.03±0.23-0.06±0.08
ER 24.49±0.24 -0.02±0.35 -0.02±0.14
EWC 24.56±0.15 0.01±0.02 -0.01±0.01
CoR 24.53±0.09 0.01±0.00 0.01±0.01
ReCAP 39.03±0.35 0.03±0.07-0.02±0.03
SP500
Static 16.18±0.03 - -
Retrain 22.86±0.01 - -
Finetune 22.85±0.04 0.01±0.05 -0.01±0.03
ER 22.85±0.070.01±0.04 -0.01±0.02
EWC 22.87±0.03 0.00±0.01 0.00±0.00
CoR 22.87±0.03 0.00±0.00 0.00±0.00
ReCAP 47.18±0.430.00±0.09 -0.00±0.05
The results in Table 4 provide a comprehensive comparison in
terms of CL metrics. Across three US market datasets, our pro-
posed ReCAP framework consistently achieves the highest average
performance by a substantial margin, outperforming all other CL
baselines. This demonstrates the strong adaptability and knowl-
edge accumulation capability of ReCAP when facing long-term,
non-stationary market environments. Furthermore, as the number
of assets increases, the performance gap widens. On the SP500, Re-
CAP attains a nearly double average performance that of the best
baseline. This indicates that our framework is particularly effective
in complex, high-dimensional environments.
In terms of forgetting and forward transfer, which quantify the
retention of knowledge and the ability to leverage prior knowledge,
ReCAP achieves comparable or superior results relative to other
CL strategies. Notably, with the increase in the number of assets,
the forgetting and forward transfer values of all methods approach
zero. This may be due to the increased independence between tasks
when more assets are involved. Other widely used CL strategies,
including Finetune, ER, and EWC, do not show obvious improve-
ments over the retrain strategy. Moreover, ER and EWC represent
replay-based and regularization-based CL strategies, respectively,
and their overall performance is not superior to native Finetune.
CoR attempts to balance plasticity and stability through constraint
optimization. However, as shown in Table 4, its performance in
the financial domain remains to be verified. This may be because
task segmentation in online trading does not align well with static
data distributions, further highlighting the unique challenges of
continual PM.
5.3 Ablation Studies
To further understand the contribution of each component in our
proposed ReCAP framework, we conduct ablation studies on the
NAS100. We compare the full model with three ablated variants: 1)

Regime-Adaptive Continual Learning for Portfolio Management KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
CR SR MDD AP
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0Values of CR / SR
w/o-ARD
w/o-PL
w/o-RGM
ReCAP
0.10
0.15
0.20
0.25
0.30
0.35
0.40
Values of MDD / AP
Figure 4: Ablation study of ReCAP on the NAS100. We com-
pare ReCAP with three ablated variants: without adaptive
regime detection (w/o-ARD), without policy library (w/o-PL),
and without regime-gate module (w/o-RGM).
w/o-ARD, where the market is segmented using fixed-length win-
dows instead of using ARD; 2)w/o-PL, where only the most recent
policy vector is retained and reused, discarding the accumulated
policy library; and 3)w/o-RGM, where the RGM is removed and
policy vectors are combined using random weights;
Figure 4 summarizes the results across four evaluation metrics.
Among the ablated variants, w/o-ARD exhibits the largest drop
in performance across all indicators. This result underscores the
critical importance of accurate and adaptive regime segmentation
for continual PM. Without proper regime identification, the agent
is unable to align its learning and adaptation process with true
market dynamics. The w/o-PL variant performs second worst, indi-
cating that the absence of a policy library severely limits the agent’s
ability to accumulate and reuse knowledge from past regimes. This
also leads to the worst average performance of the final policy on
all regimes, i.e., the lowest AP. The full framework consistently
achieves the best performance on all metrics, demonstrating that
all three components are indispensable for addressing continual
PM. The synergy among these modules enables ReCAP to not only
accumulate and retain valuable knowledge but also to deploy it
effectively in response to evolving market conditions.
5.4 Parameter Sensitivity
We further investigate the sensitivity of ReCAP to the hyperparam-
eters in the adaptive regime detection module, specifically the drift
parameter𝜅 and the regime change thresholdℎ. Table 5 presents
the performance on NAS100 under different parameter settings,
where𝜅 andℎ are set as multiples of the standard deviation𝜎. The
results show that ReCAP maintains superior performance across a
range of parameter values. Varying𝜅 while fixingℎ consistently
yields high cumulative returns and Sharpe ratios. Similarly, the per-
formance remains robust when adjustingℎ. This indicates that the
effectiveness of ReCAP is not sensitive to precise hyperparameter
tuning, demonstrating the robustness of our proposed framework.
Replacing CUSUM with an HMM equipped with BIC-based model
selection on NAS100 still yields 146.38% CR, 1.10 SR, and 24.22%
MDD, indicating that the gain does not depend on a single detector
implementation. Under additional +5 bps and +10 bps cost settings,
ReCAP preserves a clear advantage. Detailed results are provided
in Appendix B.
5.5 More Discussion
The experimental results show that ReCAP outperforms both pop-
ular PM methods and common CL strategies. Two observations
are important. First, task segmentation that better matches true
regime shifts is important for continual adaptation, as fixed-window
segmentation leads to noticeable degradation. Second, the combi-
nation of adaptive regime detection, policy-vector accumulation,
and regime-aware policy composition improves long-horizon re-
turn, risk-adjusted performance, and drawdown control in a uni-
fied framework. The modular design also leaves room for stronger
regime detectors, knowledge distillation, and multi-agent exten-
sions. Limitations and future directions are discussed in the Appen-
dix C.
Table 5: Parameter sensitivity analysis on NAS100. We com-
pare different settings of the drift parameter𝜅 and the regime
change thresholdℎ.
𝜅 ℎCR%↑SR↑MDD%↓
0.3𝜎2.5𝜎164.12±3.18 1.15±0.02 17.07±0.72
0.5𝜎2.5𝜎164.89±2.54 1.14±0.01 23.86±0.35
0.7𝜎2.5𝜎172.07±3.80 1.17±0.03 17.03±0.70
0.5𝜎2.0𝜎160.21±0.05 1.12±0.00 25.82±0.11
0.5𝜎3.0𝜎132.61±0.00 1.00±0.00 26.60±0.13
6 Conclusion
In this work, we identified and attempted to address the fundamen-
tal challenge of non-stationarity in financial markets, a pervasive
issue due to “alpha decay”. We proposedReCAP(Regime-aware
ContinualAdaptivePortfolio management), a principled frame-
work that reformulates portfolio management as a continual learn-
ing process. ReCAP introduces a novel synergy between adaptive
regime detection, a reusable policy library, and a regime-gate mech-
anism, enabling the agent to dynamically detect market shifts, retain
historical expertise, and rapidly adapt to novel regimes. Compre-
hensive experiments on five real-world datasets, covering major
US and Japanese stock indices as well as commodity ETFs, demon-
strate the superiority of our approach. ReCAP not only consistently
outperforms state-of-the-art rule-based and RL-based baselines in
terms of profitability and risk control but also surpasses existing
continual learning strategies in average performance and forward
transfer. These results highlight the effectiveness of ReCAP in bal-
ancing continual adaptation and knowledge retention in dynamic
financial environments.
7 Acknowledgments
This work was supported by the National Natural Science Founda-
tion of China (Nos. 62476228, 62506308), and the Chengdu Science
and Technology Program (No.2025-YF12-00030-RC).
References
[1] Guido Abate, Ignazio Basile, and Pierpaolo Ferrari. 2024. The Integration of
Environmental, Social and Governance Criteria in Portfolio Optimization: An
Empirical Analysis.Corporate Social Responsibility and Environmental Manage-
ment31, 3 (2024), 2054–2065.
[2] David Abel, André Barreto, Benjamin Van Roy, Doina Precup, Hado P van Hasselt,
and Satinder Singh. 2023. A Definition of Continual Reinforcement Learning. In
NeurIPS, Vol. 36. 50377–50407.

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Chaofan Pan et al.
[3] Amit Agarwal, Elad Hazan, Satyen Kale, and Robert E. Schapire. 2006. Algorithms
for portfolio management based on the Newton method. InICML. 9–16.
[4] Andrew Ang and Allan Timmermann. 2012. Regime Changes and Financial
Markets.Annual Review of Financial Economics4, 2012 (2012), 313–337. https:
//doi.org/10.1146/annurev-financial-110311-101808
[5] Shaojie Bai, J Zico Kolter, and Vladlen Koltun. 2018. An Empirical Evaluation of
Generic Convolutional and Recurrent Networks for Sequence Modeling.arXiv
preprint arXiv:1803.0127110 (2018).
[6] Avrim Blum and Adam Kalai. 1997. Universal Portfolios With and Without
Transaction Costs. InCOLT. 309–313.
[7] Allan Borodin, Ran El-Yaniv, and Vincent Gogan. 2000. On the Competitive
Theory and Practice of Portfolio Selection. InLATIN. Springer, 173–196.
[8] Allan Borodin, Ran El-Yaniv, and Vincent Gogan. 2003. Can We Learn to Beat
the Best Stock. InNeurIPS, Vol. 16.
[9] Barkha Dhingra, Shallu Batra, Vaibhav Aggarwal, Mahender Yadav, and Pankaj
Kumar. 2024. Stock Market Volatility: A Systematic Review.Journal of Modelling
in Management19, 3 (2024), 925–952.
[10] István Erlich, Ganesh K Venayagamoorthy, and Nakawiro Worawat. 2010. A
Mean-Variance Optimization Algorithm. InIEEE CEC. 1–6.
[11] Li Gao and Weiguo Zhang. 2013. Weighted Moving Average Passive Aggressive
Algorithm for Online Portfolio Selection. InIHMSC, Vol. 1. 327–330.
[12] Christian Geishauser, Carel van Niekerk, Nurul Lubis, Michael Heck, Hsien-
Chin Lin, Shutong Feng, and Milica Gašić. 2022. Dynamic Dialogue Policy for
Continual Reinforcement Learning.arXiv preprint arXiv:2204.05928(2022).
[13] Stefano Giglio, Bryan Kelly, and Dacheng Xiu. 2022. Factor Models, Machine
Learning, and Asset Pricing.Annual Review of Financial Economics14, 1 (2022),
337–368.
[14] Abhishek Gunjan and Siddhartha Bhattacharyya. 2023. A Brief Review of Portfo-
lio Optimization Techniques.Artificial Intelligence Review56, 5 (2023), 3847–3886.
[15] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. 2018. Soft
Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a
Stochastic Actor. InICML. 1861–1870.
[16] Muhammad Burhan Hafez and Stefan Wermter. 2021. Behavior Self-Organization
Supports Task Inference for Continual Robot Learning. InIROS. IEEE, 6739–6746.
[17] Jiayi He, Pengjian Shang, and Yali Zhang. 2020. Global Recurrence Quantification
Analysis and Its Application in Financial Time Series.Nonlinear Dynamics100
(2020), 803–829.
[18] David P Helmbold, Robert E Schapire, Yoram Singer, and Manfred K Warmuth.
1998. On-Line Portfolio Selection Using Multiplicative Updates.Mathematical
Finance8, 4 (1998), 325–347.
[19] Mohammad Enamul Hoque, Low Soo-Wah, and Mabruk Billah. 2023. Time-
Frequency Connectedness and Spillover Among Carbon, Climate, and Energy
Futures: Determinants and Portfolio Risk Management Implications.Energy
Economics127 (2023), 107034.
[20] Gabriel Ilharco, Marco Tulio Ribeiro, Mitchell Wortsman, Ludwig Schmidt, Han-
naneh Hajishirzi, and Ali Farhadi. 2023. Editing models with task arithmetic. In
ICLR.
[21] David Isele and Akansel Cosgun. 2018. Selective Experience Replay for Lifelong
Learning, In AAAI.AAAI32, 1, 3302–3309.
[22] Zhengyao Jiang, Dixing Xu, and Jinjun Liang. 2017. A Deep Reinforcement
Learning Framework for the Financial Portfolio Management Problem.arXiv
preprint arXiv:1706.10059(2017).
[23] Dimitrios Katsikas, Nikolaos Passalis, and Anastasios Tefas. 2024. Bi-Directional
Knowledge Transfer For Continual Deep Reinforcement Learning in Financial
Trading. InMLSP. 1–6.
[24] Dimitrios Katsikas, Nikolaos Passalis, and Anastasios Tefas. 2025. Plasticity
Driven Knowledge Transfer for Continual Deep Reinforcement Learning in
Financial Trading. InICPR. 80–93.
[25] Khimya Khetarpal, Matthew Riemer, Irina Rish, and Doina Precup. 2022. To-
wards Continual Reinforcement Learning: A Review and Perspectives.Journal
of Artificial Intelligence Research75 (2022), 1401–1476.
[26] Byungjai Kim, Chanho Ahn, Wissam J. Baddar, Kikyung Kim, HUIJIN LEE, Sae-
hyun Ahn, Seungju Han, Sungjoo Suh, and Eunho Yang. 2025. Test-Time Ensem-
ble via Linear Mode Connectivity: A Path to Better Adaptation. InICLR.
[27] James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume
Desjardins, Andrei A. Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka
Grabska-Barwinska, Demis Hassabis, Claudia Clopath, Dharshan Kumaran, and
Raia Hadsell. 2017. Overcoming Catastrophic Forgetting in Neural Networks.
Proceedings of the National Academy of Sciences114, 13 (2017), 3521–3526.
[28] Jinho Lee, Raehyun Kim, Seok-Won Yi, and Jaewoo Kang. 2020. MAPS: Multi-
Agent reinforcement learning-based Portfolio management System.. InIJCAI.
4520–4526.
[29] Bin Li and Steven C. H. Hoi. 2012. On-line portfolio selection with moving
average reversion. InICML. 563–570.
[30] Shicheng Li, Jinshan Zhang, and Feng Wang. 2025. AlphaGAT: A Two-Stage
Learning Approach for Adaptive Portfolio Selection. InIJCAI, Vol. 1. 7500–7508.
[31] Xiao-Yang Liu, Hongyang Yang, Jiechao Gao, and Christina Dan Wang. 2021.
FinRL: Deep reinforcement learning framework to automate trading in quantita-
tive finance. InACM ICAIF.
[32] Volodymyr Mnih, Adria Puigdomenech Badia, Mehdi Mirza, Alex Graves, Timo-
thy Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu. 2016. Asynchro-
nous Methods for Deep Reinforcement Learning. InICML. 1928–1937.
[33] Sattarov Otabek and Jaeyoung Choi. 2024. Multi-Level Deep Q-Networks for
Bitcoin Trading Strategies.Scientific Reports14, 1 (2024), 771.
[34] Adedoyin Tolulope Oyewole, Omotayo Bukola Adeoye, Wilhelmina Afua Addy,
Chinwe Chinazo Okoye, Onyeka Chrisanctus Ofodile, and Chinonye Esther
Ugochukwu. 2024. Predicting Stock Market Movements Using Neural Networks:
A Review and Application Study.Computer Science & IT Research Journal5, 3
(2024), 651–670.
[35] Chaofan Pan, Lingfei Ren, Yihui Feng, Linbo Xiong, Wei Wei, Yonghao Li, and Xin
Yang. 2025. Multi-granularity Knowledge Transfer for Continual Reinforcement
Learning. InIJCAI.
[36] Chaofan Pan, Xin Yang, Yanhua Li, Wei Wei, Tianrui Li, Bo An, and Jiye
Liang. 2025. A Survey of Continual Reinforcement Learning.arXiv preprint
arXiv:2506.21872(2025).
[37] Julien Pénasse. 2022. Understanding Alpha Decay.Management Science68, 5
(2022), 3966–3973.
[38] Sam Powers, Eliot Xing, Eric Kolve, Roozbeh Mottaghi, and Abhinav Gupta.
2022. CORA: Benchmarks, Baselines, and Metrics as a Platform for Continual
Reinforcement Learning Agents. InCoLLAs, Vol. 199. 705–743.
[39] Huntley Schaller and Simon Van Norden. 1997. Regime Switching in Stock
Market Returns.Applied Financial Economics7, 2 (1997), 177–191.
[40] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.
2017. Proximal Policy Optimization Algorithms.arXiv preprint arXiv:1707.06347
(2017).
[41] Ashish Kumar Shakya, Gopinatha Pillai, and Sohom Chakrabarty. 2023. Rein-
forcement Learning Algorithms: A Brief Survey.Expert Systems with Applications
231 (2023), 120495.
[42] William F Sharpe. 1970. Efficient Capital Markets: A Review of Theory and
Empirical Work: Discussion.The Journal of Finance25, 2 (1970), 418–420.
[43] Farzan Soleymani and Eric Paquet. 2021. Deep graph convolutional reinforcement
learning for financial portfolio management – DeepPocket.Expert Systems with
Applications182 (2021), 115127.
[44] Rafał Surdej, Michał Bortkiewicz, Alex Lewandowski, Mateusz Ostaszewski, and
Clare Lyle. 2025. Balancing Expressivity and Robustness: Constrained Rational
Activations for Reinforcement Learning. InCoLLAs.
[45] Taariq GH Surtee and Imhotep Paul Alagidede. 2023. A Novel Approach to Using
Modern Portfolio Theory.Borsa Istanbul Review23, 3 (2023), 527–540.
[46] Rundong Wang, Hongxin Wei, Bo An, Zhouyan Feng, and Jun Yao. 2021. Com-
mission Fee Is Not Enough: A Hierarchical Reinforced Framework for Portfolio
Management. InAAAI, Vol. 35. 626–633.
[47] Zhicheng Wang, Biwei Huang, Shikui Tu, Kun Zhang, and Lei Xu. 2021. Deep-
trader: A Deep Reinforcement Learning Approach for Risk-Return Balanced
Portfolio Management With Market Conditions Embedding. InAAAI, Vol. 35.
643–650.
[48] Austin Warner and Georgios Fellouris. 2022. CuSum for sequential change
diagnosis. InIEEE ISIT. 486–491.
[49] Maciej Wolczyk, Michal Zajac, Razvan Pascanu, Lukasz Kucinski, and Piotr Milos.
2021. Continual World: A Robotic Benchmark For Continual Reinforcement
Learning. InNeurIPS. 28496–28510.
[50] Ke Xu, Yifan Zhang, Deheng Ye, Peilin Zhao, and Mingkui Tan. 2020. Relation-
Aware Transformer for Portfolio Policy Learning. InIJCAI-20. 4647–4653.
[51] Yunan Ye, Hengzhi Pei, Boxin Wang, Pin-Yu Chen, Yada Zhu, Ju Xiao, and Bo Li.
2020. Reinforcement-Learning Based Portfolio Management With Augmented
Asset Movement Prediction States. InAAAI, Vol. 34. 1112–1119.
[52] Wentao Zhang, Yilei Zhao, Shuo Sun, Jie Ying, Yonggang Xie, Zitao Song, Xinrun
Wang, and Bo An. 2024. Reinforcement Learning with Maskable Stock Represen-
tation for Portfolio Management in Customizable Stock Pools. InACM WWW.
187–198.
[53] Yifan Zhang, Peilin Zhao, Qingyao Wu, Bin Li, Junzhou Huang, and Mingkui
Tan. 2022. Cost-Sensitive Portfolio Selection via Deep Reinforcement Learning.
IEEE Transactions on Knowledge and Data Engineering34, 1 (2022), 236–248.
[54] Zetao Zheng, Jie Shao, Shilong Deng, Anjie Zhu, Heng Tao Shen, and Xiaofang
Zhou. 2024. Cross-Insight Trader: A Trading Approach Integrating Policies With
Diverse Investment Horizons for Portfolio Management. InICDE. 4685–4698.
Appendix
A Definitions
Definition A.1 (OHLCV).The Open-High-Low-Close-Volume is
a time series representation of asset prices. For a market consisting
of𝑁 tradable assets, letX𝑡 ={𝑥 𝑡,1,...,𝑥 𝑡,𝑁} denote the market ob-
servation at time𝑡. Each asset𝑖∈[ 1,𝑁] is represented by OHLCV,

Regime-Adaptive Continual Learning for Portfolio Management KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea.
Table 6: Performance comparison of five CL strategies and
ReCAP on NAS100 in terms of three PM metrics and AP.
Method CR%↑SR↑MDD%↓AP%↑
Static 123.54±1.30 0.92±0.01 25.37±0.17 17.53±0.14
Pretrain 145.83±1.31 1.09±0.01 24.57±0.14 24.55±0.12
Retrain 145.57±0.45 1.09±0.00 24.56±0.04 24.51±0.05
Finetune 145.60±2.13 1.09±0.01 24.53±0.22 24.59±0.18
ER 145.30±1.49 1.09±0.01 24.59±0.23 24.49±0.24
EWC 145.72±1.37 1.09±0.01 24.57±0.18 24.56±0.15
ReCAP 164.89±2.54 1.14±0.01 23.86±0.35 39.03±0.35
that is𝑥𝑡,𝑖 =

𝑂𝑡,𝑖,𝐻𝑡,𝑖,𝐿𝑡,𝑖,𝐶𝑡,𝑖,𝑉𝑡,𝑖

, where𝑂𝑡,𝑖 ,𝐻𝑡,𝑖 ,𝐿𝑡,𝑖 ,𝐶𝑡,𝑖 , and
𝑉𝑡,𝑖 denote the open, high, low, close prices, and trading volume of
asset𝑖at time𝑡, respectively.
Definition A.2 (Technical Indicators).Technical indicators are
derived from OHLCV data and are used to analyze market trends
and volatility. Typical indicators include Moving Average (MA),
Relative Strength Index (RSI), and Moving Average Convergence
Divergence (MACD). We usef𝑡,𝑖 to denote the concatenation of raw
OHLCV𝑥𝑡,𝑖 and technical features for asset𝑖at time𝑡.
Definition A.3 (Portfolio).A portfolio is a collection of assets
held by an investor. At time𝑡, it is defined by a vector of weights
w𝑡 =[𝑤 𝑡,0,𝑤𝑡,1,...,𝑤 𝑡,𝑁], where𝑤𝑡,𝑖 represents the proportion of
total capital allocated to asset 𝑖∈[ 1,𝑁] or risk-free cash (𝑖= 0),
subject to the constraints𝑤𝑡,𝑖≥ 0,˝𝑁 𝑖=0𝑤𝑡,𝑖 = 1. Short selling is not
considered in this work, but can be incorporated by relaxing the
non-negativity constraint.
Definition A.4 (Portfolio Value and Return).The portfolio value at
time𝑡 is defined as the total market value of all assets held, including
the cash. Let𝑉𝑡 denote the portfolio value at time𝑡. Assuming an
initial capital𝑉 0, the portfolio value evolves as follows:
𝑉𝑡 =𝑉𝑡−1· w⊤ 𝑡−1 r𝑡 ·(1−𝑐 𝑡),(11)
wherew𝑡−1 is the portfolio at time𝑡− 1,r𝑡 =[ 1,𝑟𝑡,1,...,𝑟 𝑡,𝑁]⊤ is
the vector of gross returns for each asset (with𝑟𝑡,𝑖 = 𝐶𝑡,𝑖 𝐶𝑡−1,𝑖 ), and𝑐𝑡
denotes the proportional transaction cost incurred at time𝑡. Then,
the single-period portfolio return at time𝑡 is defined as the relative
change in portfolio value:
𝑅𝑡 =𝑉𝑡−𝑉𝑡−1 𝑉𝑡−1 .(12)
B More Experimental Results
Table 6 compares ReCAP with five CL strategies on NAS100 and
also includes a Pretrain baseline that learns a base policy on the full
training period before task-wise finetuning. The Pretrain baseline
performs similarly to Retrain, and all fixed-boundary CL variants
improve over the Static baseline only within a limited range. In
contrast, ReCAP achieves clearly stronger results across all metrics,
indicating that adaptive regime detection and policy-vector accumu-
lation are more effective than periodic reuse of data or parameters
alone.
Figure 5 shows the portfolio values achieved by ReCAP and
other PM methods in the DOW30, SP500, NIKKEI30 and COMMOD-
ITY_ETF datasets. As the number of assets increases, the standard
deviation of portfolio values decreases because the impact of in-
dividual asset fluctuations is averaged out. ReCAP demonstrates
a more stable performance across different asset configurations.
On DOW30, ReCAP initially underperforms, particularly between
2020-11-09 and 2021-12-30, likely due to the unique regime charac-
teristics and longer regime duration during that period. However, as
knowledge accumulates, ReCAP gradually surpasses other methods,
achieving the highest portfolio value after 2024-04-25, outperform-
ing the state-of-the-art method Cross-Insight. On SP500, ReCAP ex-
hibits a similar trend. In the earlier period, it performs well but does
not significantly exceed Cross-Insight. However, after 2023-03-10,
ReCAP begins to diverge from other methods, ultimately achiev-
ing over 30% excess return compared to them. These observations
highlight ReCAP’s ability to leverage knowledge accumulation and
adapt to changing market conditions effectively. Moreover, ReCAP
demonstrates a characteristic of achieving greater excess returns
in scenarios with a larger number of assets and longer investment
horizons, aligning with the principles of CL and practical PM needs.
Table 7 reports additional CL comparisons under exogenous quar-
terly and yearly task boundaries. Even under these fixed schedules,
the strongest baseline reaches 19.52% AP on DOW30 and 28.45% AP
on NAS100, both remaining well below the corresponding ReCAP
results in the main text. This indicates that the advantage of ReCAP
does not depend on regime-derived task boundaries.
Table 8 reports a matched rolling-window adaptation compari-
son on NAS100, where competing PM baselines are also allowed
to update online using a 360-day window, a 90-day retraining fre-
quency, a 180-day minimum window, and10 4 update steps per
retraining stage. Under this matched adaptive protocol, ReCAP still
maintains a clear margin over all PM baselines.
To test robustness to the choice of detector, we replace CUSUM
in ARD with an HMM equipped with BIC-based model selection
on NAS100. The resulting policy still achieves 146.38% CR, 1.10 SR,
and 24.22% MDD over 5 seeds, confirming that the overall gain is
not tied to a single detector implementation.
Table 9 reports turnover and transaction-cost sensitivity on
NAS100. Although ReCAP trades slightly more actively than A2C,
it preserves a substantial advantage under both +5 bps and +10 bps
cost settings.
As an interpretability diagnostic, we track the policy-library
evolution on NAS100 for seed 0. After pretraining, the initial li-
brary contains 12 policy vectors. During the subsequent 37 detected
regimes, the framework performs 10 insertions, 12 merges, and 15
discards, leading to a final library of 22 vectors. The final gate
weights are also highly concentrated: the top five vectors account
for 34.3%, 26.1%, 10.5%, 10.2%, and 4.3% of the total weight, re-
spectively. This indicates that the library remains compact while
preserving a small set of dominant reusable policies.
C Limitations and Future Work
While ReCAP demonstrates strong performance and adaptability
in dynamic financial markets, several limitations remain. First, the
regime detection module relies on statistical change-point detec-
tion, which may struggle with subtle transitions or gradual market
changes, especially in high-frequency settings where noise obscures
regime boundaries. Second, the current policy-library maintenance
strategy is based on cosine similarity, which is efficient but may
merge distinct policies with similar parameters or discard rare yet

KDD 2026, August 9–13, 2026, Jeju Island, Republic of Korea. Chaofan Pan et al.
2020-05-012020-08-252020-12-172021-04-152021-08-092021-12-012022-03-282022-07-222022-11-142023-03-132023-07-07
2023-10-302024-02-262024-06-202024-10-142025-02-10
Date
1.0
1.2
1.4
1.6
1.8
2.0Portfolio Value
1e6
B&H
CRP
UP
EG
SAC
PPO
A2C
EIIE
SARL
Cross-Insight
AlphaGAT
ReCAP
(a) DOW30
2020-05-012020-08-252020-12-172021-04-152021-08-092021-12-012022-03-282022-07-222022-11-142023-03-132023-07-072023-10-302024-02-262024-06-202024-10-142025-02-10
Date
1.00
1.25
1.50
1.75
2.00
2.25
2.50
2.75Portfolio Value
1e6
B&H
CRP
UP
EG
SAC
PPO
A2C
EIIE
SARL
Cross-Insight
AlphaGAT
ReCAP
 (b) SP500
2020-05-012020-08-312020-12-282021-04-262021-08-252021-12-212022-04-202022-08-182022-12-152023-04-132023-08-092023-12-062024-04-052024-08-012024-11-282025-04-01
Date
1.00
1.25
1.50
1.75
2.00
2.25
2.50
2.75Portfolio Value
1e6
B&H
CRP
UP
EG
SAC
PPO
A2C
EIIE
SARL
Cross-Insight
AlphaGAT
ReCAP
(c) NIKKEI30
2020-05-012020-08-252020-12-172021-04-152021-08-092021-12-012022-03-282022-07-222022-11-142023-03-132023-07-072023-10-302024-02-262024-06-202024-10-142025-02-10
Date
1.0
1.2
1.4
1.6
1.8
2.0
2.2
2.4Portfolio Value
1e6
B&H
CRP
UP
EG
SAC
PPO
A2C
EIIE
SARL
Cross-Insight
AlphaGAT
ReCAP (d) COMMODITY_ETF
Figure 5: The portfolio values achieved by ReCAP and other PM methods on the DOW30, SP500, NIKKEI30 and COMMOD-
ITY_ETF datasets. OlMAR and WMAMR are discarded due to their poor performance.
Table 7: CL baselines under exogenous quarterly and yearly task boundaries.
Finetune EWC CoR ER
Dataset Boundary AP%↑FT%↑FG%↓ AP%↑FT%↑FG%↓ AP%↑FT%↑FG%↓ AP%↑FT%↑FG%↓
DOW30 Quarterly 19.52±0.40 0.95±0.51 6.81±14.05 19.43±0.11 0.18±0.32 -0.10±0.15 19.14±0.28 -1.30±3.15 0.56±4.03 19.39±0.65 0.23±0.30 -9.08±18.76
DOW30 Yearly 14.41±0.18 0.40±0.82 0.19±0.14 14.36±0.19 0.04±0.06 -0.01±0.04 14.35±0.12 -1.36±0.75 0.82±0.69 14.17±0.19 -0.22±1.07 0.06±0.80
NAS100 Quarterly 28.22±0.24 0.04±0.11 -0.03±0.08 28.29±0.12 0.01±0.01 -0.01±0.01 28.45±0.34 0.26±0.10 -0.16±0.09 28.27±0.27 0.09±0.18 -0.06±0.16
NAS100 Yearly 21.68±0.16 -0.05±0.26 0.03±0.10 21.70±0.10 0.01±0.04 -0.00±0.02 21.68±0.17 0.17±0.46 -0.09±0.21 21.77±0.21 -0.03±0.17 -0.06±0.09
Table 8: Matched rolling-window retraining comparison on
NAS100.
Method CR%↑SR↑MDD%↓
Cross-Insight 124.24±7.69 0.91±0.03 26.08±0.76
PPO 123.73±1.16 0.92±0.01 25.39±0.15
SAC 123.55±6.59 0.91±0.03 25.59±0.83
A2C 121.90±7.12 0.90±0.03 25.75±0.36
SARL 112.31±2.62 0.86±0.01 25.31±0.22
AlphaGAT 123.38±2.30 0.92±0.00 25.36±0.45
EIIE 123.22±0.15 0.92±0.00 25.35±0.05
ReCAP164.89±2.54 1.14±0.01 23.86±0.35
Table 9: Turnover and transaction-cost sensitivity on NAS100.
Cost Method Turnover↓CR%↑SR↑
+5 bps A2C 0.0440±0.0104 115.97±0.03 0.87±0.01
+5 bps ReCAP 0.0504±0.0041139.96±2.88 1.067±0.01
+10 bps A2C 0.0403±0.0165 104.00±0.05 0.82±0.03
+10 bps ReCAP 0.0505±0.0016130.12±1.40 1.02±0.00
useful regimes. Third, although the regime-gate module provides in-
terpretability through attention weights, stronger explainability and
financial transparency are still needed for real-world deployment.
Fourth, our experiments focus on day trading, so the generalization
of ReCAP to higher-frequency data remains to be validated. Finally,
although ReCAP performs strongly over long investment horizons,
it may be less effective in short-horizon settings that require very
rapid adaptation.
Future work includes more data-driven regime segmentation,
broader cross-market evaluation, improved interpretability and risk
control, and extensions that better support short-horizon trading.
