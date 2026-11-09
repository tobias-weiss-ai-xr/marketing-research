---
title: Human-AI Collaboration for Estimating Scientific Replicability
url: https://arxiv.org/abs/2605.27394
category: digital-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Tatiana Chakravorti
- Robert Fraleigh
- Timothy Fritton
- Christopher Griffin
- Vaibhav Singh
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.27394
pages: 15
chars: 50566
fetched_at: '2026-11-08T13:02:53+00:00'
kb_version: 1
---

# Human-AI Collaboration for Estimating Scientific Replicability

Human-AI Collaboration for Estimating
Scientific Replicability
Tatiana CHAKRA VORTIa, Robert FRALEIGH a, Timothy FRITTON a,
Christopher GRIFFIN a, Vaibhav SINGHa, Sai KONERU a, C. Lee GILES a,
David PENNOCK b, Anthony KW ASNICAa, Sarah RAJTMAJER a,1
a The Pennsylvania State University
b Rutgers University
Abstract.Determining whether published scientific findings can successfully be
replicated is a long-standing challenge in the empirical sciences. Existing ap-
proaches for replicability assessment typically rely either on human judgment, i.e.,
creative assembly of human experts, or on machine learning models trained on pa-
per content metadata. While both approaches have demonstrated value, each also
has important limitations. Human forecasts can be influenced by cognitive biases
and narrow exposure to the research literature, while automated assessments often
struggle to capture contextual cues and subtle signals of credibility. In this paper, we
examine a hybrid approach. Specifically, we introduce a hybrid prediction market in
which algorithmic agents trade alongside human participants to jointly estimate the
likelihood that a published scientific finding will be corroborated via the outcome
of a controlled replication study. Agents are trained on outcomes from hundreds
of prior replication studies while human participants contribute domain knowledge
through real-time trading. We evaluate this hybrid approach through multiple live
experiments involving participants from different academic disciplines and com-
pare its performance to artificial-only and human-only baselines. Our results show
that, except for a few cases, hybrid markets match or outperform artificial predic-
tion markets, producing more accurate and reliable replication forecasts.
Keywords.hybrid human-AI forecasting, prediction markets, replication prediction,
scientific credibility
1. Introduction
In recent decades, artificial intelligence (AI) and machine learning (ML) have achieved
substantial advances, reaching or surpassing human level performance on a wide range
of complex tasks. However, despite these successes, the deployment of AI systems in
real-world decision-making remains constrained by important limitations. While today’s
models perform well on standardized benchmarks, such performance may reflect statis-
tical pattern matching rather than robust, generalizable reasoning [15,54,13]. As a re-
sult, they often struggle with tasks requiring counterfactual reasoning, contextual under-
standing, and learning from limited data [33,19,49], and may produce confident but in-
1Corresponding Author: smr48@psu.edu
arXiv:2605.27394v1  [cs.CY]  19 Apr 2026

correct outputs under distribution shift [2,40]. These limitations restrict the use of AI in
high-stakes settings where reliability and interpretability are critical.
At the same time, human judgment provides complementary strengths, including
contextual reasoning, domain expertise, and the ability to interpret incomplete or am-
biguous information. Rather than viewing human and artificial intelligence as substitutes,
a growing body of research emphasizes their potential to function as complementary
components of hybrid systems that integrate human insight with computational scalabil-
ity [20,59]. A central challenge of this work is how to effectively combine heterogeneous
sources of information, e.g., human beliefs and algorithmic predictions, into coherent
and well-calibrated forecasts.
Prediction markets offer a natural framework for this integration. By allowing partic-
ipants to buy and sell contracts tied to future outcomes, prediction markets aggregate dis-
tributed information into probabilistic forecasts through market prices [4,28,42]. Artifi-
cial prediction markets extend this idea to computational settings. In these systems, algo-
rithmic agents participate in a simulated market and interact through market-based mech-
anisms to produce predictions [7]. Prior work has demonstrated that artificial prediction
markets can function as supervised learning algorithms, achieving performance compa-
rable to standard classification methods on select tasks [7,6,44]. However, the effective-
ness of artificial prediction markets is highly sensitive to design choices such as liquid-
ity, market duration, and agent initialization. Moreover, like their human counterparts,
artificial markets can suffer from insufficient participation or engagement [4,57,50]. As
a result, artificial prediction markets have not yet presented a robust alternative to con-
ventional supervised learning techniques.
Rather than viewing these limitations as reasons to abandon market-based ap-
proaches, we argue that they point toward an opportunity for human-AI collaboration. In
hybrid prediction markets, human participants trade alongside trained algorithmic agents,
allowing human and AI information and judgment to be dynamically aggregated into
probabilistic forecasts. This design leverages the speed and breadth of algorithmic agents
while incorporating human contextual insight and expertise. We investigate whether hy-
brid markets can improve predictive performance on complex evaluative tasks.
We study this question in the domain of forecasting scientific replication outcomes,
a task that has proven challenging for both human and automated methods. Prior re-
search has explored human crowd-based approaches, including prediction markets and
structured expert elicitation [41,25], as well as machine learning models trained on paper
metadata and statistical features [3,63,47,62]. Despite these efforts, neither class of ap-
proaches has consistently achieved high predictive accuracy. Human forecasts are shaped
by cognitive biases and limited familiarity with the broader literature, while automated
models often fail to capture nuanced credibility signals embedded within scientific work.
These complementary limitations make replication forecasting an ideal testbed for eval-
uating hybrid human-AI methodologies.
Our work is scaffolded by the following research questions:
RQ1:Are hybrid human-AI prediction markets able to produce more accurate replication
forecasts? How do these forecasts compare to human-only or agent-only markets?
RQ2:What information and strategies do human participants use when participating in
a replication prediction market?
Through a series of live experiments involving human participants from correspond-
ing disciplinary backgrounds, we compare hybrid markets against artificial-only and

human-only baselines in the context of replication prediction. Our findings demonstrate
that hybrid markets consistently match or outperform artificial markets, with notable
exceptions (in marketing and education). While performance varied by domain, hybrid
markets generally achieved lower or comparable mean absolute error and demonstrated
more stable aggregation of information. Survey evidence indicates that human traders
primarily relied on epistemic beliefs rather than purely profit-maximizing strategies, i.e.,
hybrid markets integrate both algorithmic pattern recognition and domain-informed hu-
man judgment. Our findings suggest that thoughtfully designed hybrid human-AI sys-
tems can improve reliability in complex scientific evaluation tasks, offering a scalable
framework for strengthening evidence assessment in research ecosystems.
2. Related Work
This research builds upon and contributes to several distinct literatures. The first is ap-
proaches to estimate or predict the replicability of scientific findings. The second is prior
work on artificial prediction markets and market-based machine learning systems that
formalize probability estimation as a trading process among algorithmic agents. The third
is emerging literature on human-AI collaboration in forecasting and evaluative judgment.
2.1. Replication prediction
Large-scale replication2 projects in psychology [16], economics [9], sociology [10], bi-
ology [21], physics [23] and beyond have turned up disappointing results, putting ques-
tions of scientific credibility at the forefront of scientific debate. Because direct replica-
tions are costly and slow, replication prediction methods aim to prioritize which stud-
ies to replicate, allocate verification resources, and provide decision-makers with cali-
brated confidence signals about research claims. Recent work has converged on three
complementary approaches: 1) human forecasting; 2) algorithmic prediction using re-
ported statistics and paper metadata; and 3) text-based machine learning that uses fea-
tures of the writing itself, sometimes combined with other signals. A robust line of re-
search shows that researchers’ aggregate beliefs contain meaningful information about
scientific replicability. This has been operationalized through forecasting surveys and
prediction markets, where participants estimate the likelihood that a study will success-
fully replicate [12]. Prior research has established crowd-based forecasting as one of
the two dominant paradigms for predicting replication outcomes, including structured
elicitation methods and prediction markets [41,25]. Collective forecasting principles ex-
tend beyond human participants. Recent work demonstrates that aggregated large lan-
guage model (LLM) “crowds” can match or approach the accuracy of human forecast-
ing crowds [52]. However, large-scale analyses of crowd forecasts also reveal system-
atic calibration challenges and information gaps. These limitations constrain predictive
performance and reflect human cognitive biases as well as restricted domain knowledge
[18]. Alongside crowd-based forecasting, a second dominant paradigm relies on machine
learning models trained on structured features extracted from published studies. These
2A note on terminology: Byreproducibility, we refer to computational repeatability – obtaining consistent
computational results using the same data, methods, code, and conditions of analysis; byreplicability, mean
obtaining consistent results on a new dataset using similar methods. We adopt these definitions from [45].

models use statistical properties, methodological indicators, and other coded character-
istics to estimate replication likelihood [3,63,47,62]. Machine learning approaches aim
to scale replication prediction beyond what is feasible with human forecasting alone, of-
fering automated and potentially generalizable prediction systems across large corpora
of scientific articles. Extending machine learning approaches further, research has devel-
oped large-scale text-based models to estimate replication likelihood directly from article
text. A prominent large-scale study constructed a text-based machine learning model to
estimate replication probabilities across more than 14,000 psychology articles [64]. This
work demonstrates that replicability varies meaningfully across subfields and method-
ological approaches, and that textual signals can help quantify this heterogeneity at scale.
Such findings suggest that replication prediction can move beyond structured metadata
toward richer representations derived from scientific narratives themselves.
2.2. Artificial prediction markets
Prediction markets are platforms to aggregate and disperse information into efficient
forecasts of uncertain future events [4,28,42,61]. Participants in these markets buy and
sell contracts representing outcomes of well-defined future events. The price of an asset
in these markets can be understood as participants’ collective prediction of the given
outcome. Prediction markets have been successfully used, e.g., for sports betting [53],
election forecasting [8], infectious disease prediction [48], and aggregating employee
wisdom in corporate settings [17,27]. A comprehensive review of prediction markets and
their applications is provided in [30].
Artificial prediction markets are numerically simulated markets populated by agent
traders for the purpose of probability estimation. Theoretical work has offered support
for the mathematical connections between artificial markets and machine learning al-
gorithms [14,55,1,31]. In initial formulations by Barbu and Lay [36,7,37,6], each agent
is represented as a budget and a simple betting function. During training, each agent’s
budget is updated based on the accuracy of its predictions over a training dataset. An
alternate market was proposed by Storkey and colleagues based on agents with isoelastic
utilities [56]. Jahedpari et al. [32] introduced an online artificial prediction market that
works like a regressor for adaptive trading strategies. They established that a continuous
artificial prediction market could be useful for syndromic surveillance. Most recently,
Nakshatri et al. [44] proposed an artificial prediction market wherein agent purchase
logic is defined geometrically, in particular, by a convex semi-algebraic set in feature
space. Time-varying asset prices affect the structure of the semi-algebraic sets, leading
to time-varying agent purchase rules. Agent parameters are trained using an evolutionary
algorithm. Authors show that their approach has desirable properties, e.g., the market
satisfies certain universal approximation properties, and there exist sufficient conditions
for convergence. Our work builds on this approach.
2.3. Hybrid human-AI forecasting
Researchers have increasingly emphasized the potential of hybrid intelligence, arguing
that superior outcomes can emerge when human cognitive capabilities such as creativity,
contextual reasoning, and ethical judgment are combined with the scalability and ana-
lytical power of artificial intelligence [20,59]. Prior work spans a broad range of efforts,

from incorporating human factors into technology design [5,11,29] to leveraging human
input for training data, as well as enabling post-hoc human interpretation and auditing
in applications related to civic welfare [24], criminal justice [58], and beyond. The over-
arching aim of these efforts is to develop hybrid systems that effectively combine hu-
man intuition with machine rationality, enabling more efficient and robust approaches to
complex societal challenges [60,59,46].
However, research on human-AI collaboration also highlights important limitations
and design challenges. While AI generated inputs can enhance individual decision mak-
ing performance, they may also unintentionally suppress unique human insights or re-
duce the diversity of perspectives that contribute to collective judgments. F ¨ugener et al.
[26], for example, demonstrate that although AI advice can improve individual accuracy,
it can simultaneously harm collective outcomes such as the wisdom of crowds. These
findings illustrate that naive integration of AI advice into human decision processes may
undermine the benefits of human diversity and expertise, underscoring the importance
of carefully designed hybrid systems. A recent study proposes a human-AI collaboration
framework for product demand forecasting, focusing on predicting future sales volume
across different industries [43]. Their framework demonstrates that the optimal alloca-
tion of human and algorithmic input depends on factors such as product life cycle and
demand volatility. Their empirical analysis shows that AI systems perform particularly
well in high-frequency data environments, while human judgment remains essential for
contextual interpretation and adjustments in rare or unexpected situations. Other stud-
ies highlight how human-AI interaction affects forecasting outcomes in practice. Fahse
et al. [22] examine AI-assisted next day sales forecasting in a real-world bakery retail
setting. Their study investigates how human decision makers interact with AI generated
demand forecasts and how this interaction influences operational performance. Although
AI support improved forecast accuracy and reduced product waste, it also led to lower
overall sales. This finding illustrates that minimizing forecast error alone does not nec-
essarily optimize real-world business outcomes, and that human oversight can be nec-
essary to balance predictive accuracy with broader strategic considerations. Similarly,
Revilla et al. [51] conduct a large-scale field experiment in retail demand forecasting
to examine how different levels of human-AI collaboration influence predictive accu-
racy. Their findings show that the effectiveness of human intervention depends heavily
on task uncertainty and the forecasting time horizon. In environments characterized by
high uncertainty and short-term horizons, automated AI forecasting performs best. In
contrast, human augmentation improves predictive accuracy in more stable environments
with long term horizons. These results highlight the context dependent nature of human-
AI complementarities in predictive tasks. Beyond commercial forecasting settings, hy-
brid forecasting approaches have also been applied to operational planning problems. Li
et al. [39,38] examine a scheduling approach for ship refit projects by integrating ma-
chine learning based predictions of task duration into a constraint programming opti-
mization model. Their study compares expert estimates, historical data forecasting, and
augmented human-AI forecasting approaches. The results show that combining human
expertise with AI predictions produces more accurate task duration estimates and leads
to more robust scheduling outcomes.

Figure 1.Forty-one features were extracted from full text and corresponding metadata for each research claim
in the training and test datasets. (see [62])
.
3. Data
Algorithmic agents were trained on the outcomes of 402 replication studies of published
findings in the social and behavioral sciences. In particular, the training dataset included
outcomes of 313 studies assembled from the Reproducibility Project Psychology [16],
the Social Science Replication Project [10], the Experimental Economics Replication
Project [9], Many Labs [34], and Many Labs 2 [35]. The remaining 89 training data-
points leveraged replication studies run by the Center for Open Science as part of the
Defense Advanced Research Project Agency (DARPA)’s Systematizing Confidence in
Open Research and Evidence (SCORE) program,3 spanning psychology, marketing, eco-
nomics, sociology, political science, education, management, health, criminology, and
public administration. Table 1 shows the breakdown of training data by field.
Table 1:Replication outcomes used
for training (total = 402), by domain.
Category n
Psychology 252
Economics 99
Marketing/Org Behavior 20
Sociology 8
Political Science 6
Education 5
Management 5
Health 4
Criminology 2
Public Administration 1
An additional 30 replication study outcomes
from the SCORE project were held out as test data
for the hybrid market experiments, with five stud-
ies evaluated per disciplinary session across six
domains: economics, sociology, psychology, mar-
keting/organizational behavior, political science,
and education.4 Although the SCORE replication
outcomes are now publicly available, they were
not yet published at the time of market experi-
ments, so participants had no way to look them up.
The full text of both training and test pa-
pers, along with corresponding metadata, were
processed through a feature extraction pipeline to
derive semantic, bibliometric, and statistical fea-
tures following the methodology described in [62]. In total, 41 features were extracted per
research claim, including statistical evidence, author characteristics, publication venue
metrics, funding acknowledgments, and related metadata (see Figure 1).
4. Market Model
Prior research has introduced artificial prediction markets composed of AI agents who
buy and sell replication outcomes [50]. In these markets, model weights are optimized
3Seehttps://www.darpa.mil/program/systematizing-confidence-in-open-research-and-evidence.
4All train and test data is available athttps://osf.io/g5sny/overview.

using genetic algorithms trained on ground-truth replication studies to evolve agent be-
haviors that predict reproducibility. Our hybrid markets adopt this foundational structure.
The mathematical construction of these markets is fully laid out in prior work [44].
At a high level, synthetic agents interact in a simple binary option market using a loga-
rithmic market scoring rule. Agents begin with an initial amount of cash and may choose
to purchase contracts representing ”will replicate” or ”will not replicate” outcomes of a
given replication study (each market corresponds to one replication study). Agents are
instantiated in feature space at the location of training data points and specialize in buy-
ing either ”will replicate” or ”will not replicate” contracts depending on the training dat-
apoint they represent. Agents in the market bid in geometric regions of feature space (see
Figure 2 for notional representation). Agents are sensitive to asset price, which causes
their bid behavior to evolve in time.
Figure 2.:A toy artificial market with input data from
the Reproducibility Project Psychology. Agents are rep-
resented as blue or red ellipsoids representing ”will
replicate” and ”will not replicate” specialization, re-
spectively.Note 1: High dimensional feature space is
projected down for visualization. Note 2: We multiply
the price by 100 and convert to dollars.
In our hybrid markets, each
agent was furnished with $500 cash,
a value that ensured that each agent
would not exhaust its cash supply
during the experiment. We chose this
configuration to mimic real market
forces, where there is consistent mar-
ket momentum throughout the ex-
periment. Human participants were
each given $25 to invest per market,
with each market bookkeeping op-
erating independently. The specific
value balanced budgetary considera-
tions with incentivization. Liquidity
and lambda parameters were tuned
with these amounts fixed, specifi-
cally, in order to support balance be-
tween agent and human influence.
We imposed a minimum activity rule
for human participants, namely, we
required a minimum of three trades
in order for a human participant to be eligible to receive their earned payout.
Hybrid markets were configured to run for a total duration of 12 hours, correspond-
ing to approximately 43,200 one-second increments. During live experiments, software
latency reduced the effective number of increments to roughly 39,000. Agent weights
were determined by the size of the training corpus and the number of agents instantiated
in each market, such that the total weight reflected the product of the number of training
papers and the number of agents participating per market.
4.1. Market Training
For hybrid experiments, we implemented a training methodology that first optimized the
key hyperparameters of the system: lambda; liquidity; percent difference; initial agent
cash, and market duration. The performance of each hyperparameter configuration was
evaluated using two complementary criteria. The first metric assessed overall market ac-

Figure 3.Schematic representation of hybrid markets for replication prediction. Step 1: Features are extracted
from full text of a paper of interest. Step 2: Extracted features are passed to algorithmic traders; the full text
PDF is provided to human traders. Step 3: Algorithmic and human traders buy and sell contracts representing
”will replicate” or ”will not replicate” outcomes of a replication study associated with the primary claim of
the paper of interest. Step 4: Trading manipulates the underlying asset prices via logarithmic market scoring
rule. Step 5. At market close, the price of a ”will replicate” asset is interpreted as the market’s confidence in
the replicability of the given claim. (training phase, orange arrows) Algorithmic traders profit or lose money
based on the total value of the assets they hold. Agents who profit are allowed to reproduce, mutate, and remain
in the market via genetic algorithms.
curacy, defined as the model’s ability to correctly predict ground-truth replication out-
comes in the training dataset. Because multiple configurations may achieve similarly
high predictive accuracy, a second evaluation criterion focused on the plausibility of
agent participation patterns.
To assess whether a given hyperparameter configuration produced a realistic mar-
ket, we examined resulting agent engagement behavior. Configurations that caused all
agent ellipsoids to initialize with excessively small radii resulted in no agents identifying
test data points as sufficiently close, leading to negligible trading activity. Conversely,
configurations that produced excessively large radii caused all data points to appear sim-
ilarly close to all agents, prompting universal participation and eliminating meaningful
differentiation among agents. A viable and realistic configuration is therefore one that
preserves meaningful inter-agent diversity across test data points and supports participa-
tion levels that reflect the categorical distribution and disciplinary variation present in the
training corpus. This dual-metric approach allowed us to select hyperparameter settings
that were both high-performing and behaviorally coherent.
4.2. Market Configuration for Hybrid Experiments
As noted, we adopted a one-second trading resolution for hybrid markets to approximate
the temporal dynamics of traditional financial markets. This required adjustments to the
artificial market’s training parameters in order to extend market convergence normally
achieved within a short sequence of agent-only trades across a substantially longer time-
frame. During artificial market training, the model was optimized using a market duration
of 60 iterations. In contrast, the human-AI hybrid experiment was designed to run for 12
hours, corresponding to 43,200 one-second increments. To maintain continuity of agent
participation under this extended schedule, we reduced the lambda parameter. Lowering
lambda constrained the number of artificial agents eligible to trade at each increment,
preventing premature convergence while preserving realistic market activity.
We also increased the cash allocation for agents to $500 to ensure they remained
solvent throughout the full 12-hour experiment. This modification helped stabilize arti-
ficial trading behavior and maintain consistent market dynamics across agents over the

long duration of human participation. Together, these adjustments allowed us to better
isolate the influence of human trading strategies by ensuring that AI agents continued to
behave coherently and predictably across the extended duration of the hybrid market.
4.3. Hybrid Market Experimental Design
In ongoing research, we have developed and beta-tested a platform that enables bot in-
teractions with real human participants, i.e., a hybrid market environment, for replication
prediction. The platform consists of a web server that hosts a pre-trained artificial market
and provides several API endpoints that: (1) allow artificial agents to buy assets; (2) al-
low human participants to buy and sell assets; and (3) manage transaction bookkeeping
and track experiment statistics. The system also includes an interactive web application
that enables human participants to trade assets through an intuitive interface (see Figure
4). Although the artificial market is theoretically formulated as a continuous system, both
the artificial-only and hybrid markets were implemented as discrete processes that up-
dated every one second. Market transactions were handled using a queuing system that
first processed all participating artificial agents, followed by any human transactions in
a first-in, first-out order. Both artificial agents and human participants were restricted to
single-share trades. After each transaction, asset prices were updated using the logarith-
mic market scoring rule [44].
Institutional Review Board (IRB) approval was obtained for all hybrid and human
prediction markets prior to subject recruitment. Human participants were recruited be-
tween January and March 2023. In particular, we recruited researchers in economics,
sociology, psychology, marketing, political science, and education. Individuals currently
enrolled in a PhD program, University faculty, and PhD-holding individuals outside of
academia were eligible to participate. We scraped the websites of universities in the
United States to obtain email addresses and solicit researchers from relevant domains. In
total, 97 researchers actively participated in this study.
Hybrid market experiments were run as six separate events. Each of the six experi-
ments involved five markets; that is, in each event, participants were given the opportu-
nity to evaluate and buy or sell outcomes of five distinct replication studies. Participants
were provided with the full text of the papers and the identified claims two days in ad-
vance of the market runs. All markets were held online and ran for 12 hours. For eco-
nomics, sociology, and psychology claims, we had three types of experiments: human-
only markets (no agents), hybrid human-AI markets, and artificial markets (agents alone).
For marketing, education, and political science, we ran only hybrid and artificial markets.
Each participant was compensated with $40 for their participation and given $125 to
use in each of their five markets ($25 in each). One of the five markets from each event
was randomly selected as the ”money market”. Participants were allowed to keep their
total cash from the money market at the end of the event. Participants were not informed
which of the 5 was the money market until after markets closed.
5. Experimental Results
5.1. RQ1: Hybrid-AI Forecasts
Hybrid human-AI prediction markets yielded predictive performance comparable to or
better than artificial markets across most domains, the exceptions being marketing and

Figure 4. Interactive web application.Human participants are provided with information about the replica-
tion study and full text of the associated paper. We provide them with initial cash to invest. They may buy and
sell contracts representing ‘will replicate’ and ‘will not replicate’ outcomes of the study via the app.
education. Hybrid markets achieved the lowest prediction error in sociology and politi-
cal science and performed competitively in economics, while human-only markets per-
formed best in psychology. These results suggest that combining algorithmic predictions
with human expert judgment is a plausible approach to scientific forecasting.
EconomicsEconomics markets took place on 19th April 2023. The human-only
market outperformed both the hybrid and AI markets. The mean absolute error (MAE)
was 0.414 for the human-only market, as shown in in Table 4. The hybrid market had a
lower overall absolute error than the AI market, at 0.411 vs. 0.452. A total of 40 partici-
pants were involved in these markets; 20 out of 40 made a profit in the money market.
SociologySociology markets were run on 24th April 2023. Both the AI and hybrid
markets outperformed the human-only market. The hybrid market achieved substantially
lower overall absolute error compared to both the human-only and AI markets, indicating
the highest level of predictive accuracy in this domain (see Table 4). A total of 33 human
participants took part in the event; 14 out of 33 made a profit in the money market.
PsychologyPsychology markets took place on 21st April 2023. The human-only
market again performed better than both the hybrid and AI markets, recording 0.378
MAE (see Table 4). Absolute error was nearly identical for the hybrid and AI markets,
indicating comparable predictive performance between these two approaches. 40 human
participants took part in the event; only 12 made a profit in the money market.
MarketingMarketing markets were run on 12th April 2023. The artificial market
outperformed the hybrid market slightly. The AI market correctly predicted three mar-
kets, whereas the hybrid market correctly predicted two (Table 3). A total of 33 human
participants took part in this study; 11 were able to make a profit in the money market.
Political SciencePolitical Science markets took place on 14th April 2023. The hy-
brid markets demonstrated stronger performance than the artificial markets (see Tables
3, 4). The event included 37 human participants; 18 profited in the money market.
EducationEducation markets took place on 17th April 2023. Both artificial and hy-
brid markets correctly predicted three outcomes of five. However, overall mean absolute
error was slightly lower for the artificial market, indicating marginally better prediction
(see Table 3). Experiments involved 31 participants, of whom 13 profited in the money
market.

Market Final
Price
Artificial
Final
Price
Hybrid
Final
Price
Human
Ground
Truth
Final
Pred.
Artificial
Final
Pred.
Hybrid
Final
Pred.
Human
1574 (Econ) 0.665 0.75 0.69 R R R R
AgO1 (Econ) 0.698 0.727 0.62 R R R R
PIDa (Econ) 0.708 0.737 0.48 R R R NR
QIIV (Econ) 0.67 0.683 0.43 NR R R NR
VB9K (Econ) 0.661 0.586 0.43 NR R R NR
5Kgq (Sociology) 0.63 0.78 0.76 NR R R R
dxQp (Sociology) 0.67 0.77 0.77 R R R R
e227 (Sociology) 0.64 0.83 0.83 R R R R
Vj0p (Sociology) 0.66 0.71 0.75 NR R R R
x0pA (Sociology) 0.62 0.77 0.23 R R R R
521q (Psychology) 0.648 0.741 0.61 NR R R R
88xa (Psychology) 0.643 0.393 0.41 R R NR NR
8wZ0 (Psychology) 0.71 0.574 0.17 NR R R NR
Br0x (Psychology) 0.714 0.903 0.94 R R R R
EQxa (Psychology) 0.637 0.594 0.46 NR R R NR
Table 2Final value (in dollars) of a ”will replicate” asset (contract) in artificial, hybrid, and human-only
markets for economics, sociology, and psychology.R = ”replicated”; NR = ”not replicated”
5.2. RQ2: Trading Strategies as Reported in Post-Experiment Surveys
At the conclusion of market experiments, all participants were asked to complete a brief
survey which asked about their experiences and decisions in the market. Most partici-
pants relied heavily on their prior beliefs about the replication likelihood of the claim
in question. Many explicitly stated that they bought assets corresponding with claims
they personally believed would replicate or that they perceived as “undervalued” by the
market spot price. A second common strategy involved trend-following and price obser-
vation. Some participants reported looking at past price movements or market trends be-
fore making purchases, indicating adaptive behavior in response to market signals rather
than relying solely on initial beliefs. We also saw evidence of profit-oriented and tactical
trading, with a few participants mentioning strategies such as selling immediately when
in profit, balancing buying and selling, or timing trades based on availability during the
day. However, these financially strategic behaviors were less frequently cited. Notably,
several responses indicated limited strategic engagement. Some participants reported not
having a clear strategy, being confused, or participating for the first time without a struc-
tured approach.
6. Conclusions and Limitations
This works puts forward hybrid human-AI prediction markets as a plausible approach to
scientific forecasting. Across multiple live experiments involving participants from di-
verse academic disciplines, hybrid markets consistently matched or outperformed arti-
ficial only and human only baselines in overall predictive accuracy. While performance
varied by domain, the results suggest that combining algorithmic agents trained on large

Market Final
Price
Artificial
Final
Price
Hybrid
Final
Price
Human
Ground
Truth
Final
Pred.
Artificial
Final
Pred.
Hybrid
Final
Pred.
Human
5XEE (Marketing) 0.61 0.35 - NR R NR -
8w97 (Marketing) 0.674 0.6 - NR R R -
EKBZ (Marketing) 0.76 0.35 - R R NR -
G1Lr (Marketing) 0.66 0.437 - R R NR -
N8pB (Marketing) 0.712 0.711 - R R R -
mxyQ (Political Sci) 0.663 0.49 - NR R NR -
qgWj (Political Sci) 0.65 0.843 - R R R -
wRvv (Political Sci) 0.673 0.753 - R R R -
xYbO (Political Sci) 0.677 0.586 - NR R R -
z4dO (Political Sci) 0.619 0.549 - R R R -
BIRQ (Education) 0.681 0.578 - R R R -
Bixd (Education) 0.69 0.642 - R R R -
bY2A (Education) 0.696 0.668 - NR R R -
Kybl (Education) 0.622 0.683 - NR R R -
zqwm (Education) 0.659 0.689 - R R R -
Table 3Final value (in dollars) of a ”will replicate” asset (contract) in artificial and hybrid markets for mar-
keting, political science, and education.R = ”replicated”; NR = ”not replicated”
Discipline MAE Artificial MAE Hybrid MAE Human-only
Econ 0.452 0.411 0.414
Sociology 0.472 0.424 0.536
Psychology 0.528 0.523 0.378
Marketing 0.430 0.490 -
Political SC 0.480 0.386 -
Education 0.458 0.488 -
Table 4Mean Absolute Error (MAE) by discipline.
replication datasets with human contextual judgment can enhance reliability in complex
evaluative tasks. Overall, this work provides empirical support for the value of thought-
fully designed human-AI collaboration systems in scientific decision-making and con-
tributes insights for building hybrid intelligence frameworks that integrate computational
efficiency with human expertise.
These initial studies faced several limitations. Hybrid market experiments were con-
ducted on a relatively small set of replication studies in specified domains, which may
limit their generalizability. Larger-scale deployments would be needed to assess robust-
ness across additional fields and claim types. In addition, participant engagement var-
ied across experiments. In several markets, a non-trivial number of participants made no
transactions, suggesting heterogeneity in participation, strategic sophistication, or famil-
iarity with prediction markets. This variability may have influenced market performance
and the degree to which human judgment was effectively aggregated.

References
[1] J. Abernethy, Y . Chen, and J. Wortman Vaughan. An optimization-based framework for automated
market-making. InProceedings of the 12th ACM conference on Electronic commerce, pages 297–306,
2011.
[2] A. Alansari and H. Luqman. Large language models hallucination: A comprehensive survey.arXiv
preprint arXiv:2510.06265, 2025.
[3] A. Altmejd, A. Dreber, E. Forsell, J. Huber, T. Imai, M. Johannesson, M. Kirchler, G. Nave, and
C. Camerer. Predicting the replicability of social science lab experiments.PloS one, 14(12):e0225826,
2019.
[4] K. J. Arrow, R. Forsythe, M. Gorham, R. Hahn, R. Hanson, J. O. Ledyard, S. Levmore, R. Litan, P. Mil-
grom, F. D. Nelson, G. R. Neumann, M. Ottaviani, T. C. Schelling, R. J. Shiller, V . L. Smith, E. Snow-
berg, C. R. Sunstein, P. C. Tetlock, P. E. Tetlock, H. R. Varian, J. Wolfers, and E. Zitzewitz. The promise
of prediction markets.Science, 320(5878):877–878, May 2008.
[5] G. Bansal, B. Nushi, E. Kamar, W. S. Lasecki, D. S. Weld, and E. Horvitz. Beyond accuracy: The role
of mental models in human-ai team performance. InProceedings of the AAAI Conference on Human
Computation and Crowdsourcing, volume 7, pages 2–11, 2019.
[6] A. Barbu and N. Lay. Artificial prediction markets for lymph node detection. In2013 E-Health and
Bioengineering Conference (EHB), pages 1–7. IEEE, 2013.
[7] A. Barbu, N. Lay, and S. Mannor. An introduction to artificial prediction markets for classification.
Journal of Machine Learning Research, 13(7), 2012.
[8] J. E. Berg, F. D. Nelson, and T. A. Rietz. Prediction market accuracy in the long run.International
Journal of Forecasting, 24(2):285–300, 2008.
[9] C. F. Camerer, A. Dreber, E. Forsell, T.-H. Ho, J. Huber, M. Johannesson, M. Kirchler, J. Almenberg,
A. Altmejd, T. Chan, et al. Evaluating replicability of laboratory experiments in economics.Science,
351(6280):1433–1436, 2016.
[10] C. F. Camerer, A. Dreber, F. Holzmeister, T.-H. Ho, J. Huber, M. Johannesson, M. Kirchler, G. Nave,
B. A. Nosek, T. Pfeiffer, et al. Evaluating the replicability of social science experiments in nature and
science between 2010 and 2015.Nature Human Behaviour, 2(9):637–644, 2018.
[11] L. B. Canonico, C. Flathmann, and N. McNeese. The wisdom of the market: Using human factors
to design prediction markets for collective intelligence. InProceedings of the Human Factors and
Ergonomics Society Annual Meeting, volume 63, pages 1471–1475. SAGE Publications Sage CA: Los
Angeles, CA, 2019.
[12] S. P. Chandrashekar, D. Viganola, A. Dreber, M. Johannesson, T. Pfeiffer, A. Siegel, and G. Feldman.
Using prediction markets and forecasting surveys to predict 28 replication outcomes of classic articles
in social psychology and judgement and decision making.Royal Society Open Science, 13(1), 2026.
[13] S. Chen, Y . Chen, Z. Li, Y . Jiang, Z. Wan, Y . He, D. Ran, T. Gu, H. Li, T. Xie, et al. Benchmarking large
language models under data contamination: A survey from static to dynamic evaluation. InProceedings
of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 10091–10109,
2025.
[14] Y . Chen, L. Fortnow, N. Lambert, D. M. Pennock, and J. Wortman. Complexity of combinatorial market
makers. InProceedings of the 9th ACM Conference on Electronic Commerce, pages 190–199, 2008.
[15] P. Chizhov, M. Nee, P.-C. Langlais, and I. P. Yamshchikov. What the hellaswag? on the validity of
common-sense reasoning benchmarks.arXiv preprint arXiv:2504.07825, 2025.
[16] O. S. Collaboration. Estimating the reproducibility of psychological science.Science,
349(6251):aac4716, 2015.
[17] B. Cowgill, J. Wolfers, and E. Zitzewitz. Using prediction markets to track information flows: Evidence
from google. Inamma, page 3, 2009.
[18] S. DellaVigna and E. Vivalt. Forecasting social science: Evidence from 100 projects. Technical report,
National Bureau of Economic Research, 2025.
[19] D. Dellermann, A. Calma, N. Lipusch, T. Weber, S. Weigel, and P. Ebel. The future of human-
ai collaboration: a taxonomy of design knowledge for hybrid intelligence systems.arXiv preprint
arXiv:2105.03354, 2021.
[20] D. Dellermann, P. Ebel, M. S ¨ollner, and J. M. Leimeister. Hybrid intelligence.Business & information
systems engineering, 61(5):637–643, 2019.
[21] T. M. Errington, E. Iorns, W. Gunn, F. E. Tan, J. Lomax, and B. A. Nosek. An open investigation of the
reproducibility of cancer biology research.Elife, 3, 2014.

[22] T. Fahse and A. Schmitt. Exploring the synergies in human-ai hybrids: A longitudinal analysis in sales
forecasting. 2023.
[23] S. S. Feger, S. Dallmeier-Tiessen, A. Schmidt, and P. W. Wo ´zniak. Designing for reproducibility: A
qualitative study of challenges and opportunities in high energy physics. InProceedings of the 2019
CHI Conference on Human Factors in Computing Systems, pages 1–14, 2019.
[24] R. Fogliato, M. De-Arteaga, and A. Chouldechova. A case for humans-in-the-loop: Decisions in the
presence of misestimated algorithmic scores.Available at SSRN 4050125, 2022.
[25] H. Fraser, M. Bush, B. C. Wintle, F. Mody, E. T. Smith, A. M. Hanea, E. Gould, V . Hemming, D. G.
Hamilton, L. Rumpff, et al. Predicting reliability through structured expert elicitation with the replicats
(collaborative assessments for trustworthy science) process.Plos one, 18(1):e0274429, 2023.
[26] A. F ¨ugener, J. Grahl, A. Gupta, and W. Ketter. Will humans-in-the-loop become borgs? merits and
pitfalls of working with ai.MIS quarterly, 45(3):1527–1556, 2021.
[27] B. J. Gillen, C. R. Plott, and M. Shum. Information aggregation mechanisms in the field: Sales forecast-
ing inside intel. InWorking paper. 2012.
[28] R. Hanson, R. Oprea, and D. Porter. Information aggregation and manipulation in an experimental
market.Journal of Economic Behavior & Organization, 60(4):449–459, 2006.
[29] R. H. Harper. The role of hci in the age of ai.International Journal of Human–Computer Interaction,
35(15):1331–1344, 2019.
[30] C. F. Horn, B. S. Ivens, M. Ohneberg, and A. Brem. Prediction markets: A literature review 2014.The
Journal of Prediction Markets, 8(2):89–126, 2014.
[31] J. Hu and A. Storkey. Multi-period trading prediction markets with connections to machine learning. In
International Conference on Machine Learning, pages 1773–1781, 2014.
[32] F. Jahedpari, T. Rahwan, S. Hashemi, T. P. Michalak, M. De V os, J. Padget, and W. L. Woon. Online
prediction via continuous artificial prediction markets.IEEE Intelligent Systems, 32(1):61–68, 2017.
[33] J. Kim, A. Podlasek, K. Shidara, F. Liu, A. Alaa, and D. Bernardo. Limitations of large language models
in clinical problem-solving arising from inflexible reasoning.Scientific reports, 15(1):39426, 2025.
[34] R. A. Klein, K. A. Ratliff, M. Vianello, R. B. Adams Jr, ˇS. Bahn´ık, M. J. Bernstein, K. Bocian, M. J.
Brandt, B. Brooks, C. C. Brumbaugh, et al. Investigating variation in replicability.Social psychology,
2014.
[35] R. A. Klein, M. Vianello, F. Hasselman, B. G. Adams, R. B. Adams Jr, S. Alper, M. Aveyard, J. R. Axt,
M. T. Babalola, ˇS. Bahn´ık, et al. Many labs 2: Investigating variation in replicability across samples and
settings.Advances in Methods and Practices in Psychological Science, 1(4):443–490, 2018.
[36] N. Lay and A. Barbu. Supervised aggregation of classifiers using artificial prediction markets. InICML,
2010.
[37] N. Lay and A. Barbu. The artificial regression market.arXiv preprint arXiv:1204.4154, 2012.
[38] J. Li, I. Aziez, R. Boudreault, and D. Lafond. Augmented human-ai forecasting for ship refit project
scheduling: A predict-then-optimize approach. InInternational Conference on Machine Learning, Op-
timization, and Data Science, pages 375–389. Springer, 2024.
[39] J. Li, Y . Yin, D. Lafond, A. Ghasemi, C. Diallo, and E. Bertrand. Integrated human-ai forecasting for
preventive maintenance task duration estimation. InInternational Conference on Machine Learning,
Optimization, and Data Science, pages 3–18. Springer, 2023.
[40] V . Lin, L.-P. Morency, and E. Ben-Michael. Omitted variable bias in language models under distribution
shift.arXiv preprint arXiv:2602.16784, 2026.
[41] Y . Liu, M. Gordon, J. Wang, M. Bishop, Y . Chen, T. Pfeiffer, C. Twardy, and D. Viganola. Repli-
cation markets: Results, lessons, challenges and opportunities in ai replication.arXiv preprint
arXiv:2005.04543, 2020.
[42] C. F. Manski. Interpreting the predictions of prediction markets.economics letters, 91(3):425–429,
2006.
[43] D. Nair and M. J. Saenz. Pair people and ai for better product demand forecasting.MIT Sloan Manage-
ment Review, 65(2):1–5, 2024.
[44] N. Nakshatri, A. Menon, C. L. Giles, S. Rajtmajer, and C. Griffin. Design and analysis of a synthetic
prediction market using dynamic convex sets.arXiv preprint arXiv:2101.01787, 2021.
[45] National Academies of Sciences, Engineering, and Medicine et al.Reproducibility and replicability in
science. National Academies Press, 2019.
[46] K. Okamura and S. Yamada. Adaptive trust calibration for human-ai collaboration.Plos one,
15(2):e0229132, 2020.

[47] S. Pawel and L. Held. Probabilistic forecasting of replication studies.PloS one, 15(4):e0231416, 2020.
[48] P. M. Polgreen, F. D. Nelson, G. R. Neumann, and R. A. Weinstein. Use of prediction markets to forecast
infectious disease activity.Clinical Infectious Diseases, 44(2):272–279, 2007.
[49] X. Puig, T. Shu, S. Li, Z. Wang, Y .-H. Liao, J. B. Tenenbaum, S. Fidler, and A. Torralba. Watch-and-
help: A challenge for social perception and human-ai collaboration.arXiv preprint arXiv:2010.09890,
2020.
[50] S. Rajtmajer, C. Griffin, J. Wu, R. Fraleigh, L. Balaji, A. Squicciarini, A. Kwasnica, D. Pennock,
M. McLaughlin, T. Fritton, et al. A synthetic prediction market for estimating confidence in published
work. InProceedings of the AAAI Conference on Artificial Intelligence, volume 36, pages 13218–13220,
2022.
[51] E. Revilla, M. J. Saenz, M. Seifert, and Y . Ma. Human–artificial intelligence collaboration in prediction:
a field experiment in the retail industry.Journal of Management Information Systems, 40(4):1071–1098,
2023.
[52] P. Schoenegger, I. Tuminauskaite, P. S. Park, R. V . S. Bastos, and P. E. Tetlock. Wisdom of the sil-
icon crowd: Llm ensemble prediction capabilities rival human crowd accuracy.Science Advances,
10(45):eadp1528, 2024.
[53] M. Spann and B. Skiera. Sports forecasting: a comparison of the forecast accuracy of prediction markets,
betting odds and tipsters.Journal of Forecasting, 28(1):55–72, 2009.
[54] A. Spiesberger, J. J. Vazquez, N. Pochinkov, T. Gaven ˇciak, P. Grietzer, G. Leech, and N. Schoots. Soft
contamination means benchmarks test shallow generalization.arXiv preprint arXiv:2602.12413, 2026.
[55] A. Storkey. Machine learning markets. InProceedings of the Fourteenth International Conference on
Artificial Intelligence and Statistics, pages 716–724, 2011.
[56] A. Storkey, J. Millin, and K. Geras. Isoelastic agents and wealth updates in machine learning markets.
arXiv preprint arXiv:1206.6443, 2012.
[57] P. C. Tetlock. Liquidity and prediction market efficiency.Available at SSRN 929916, 2008.
[58] G. V . Travaini, F. Pacchioni, S. Bellumore, M. Bosia, and F. De Micco. Machine learning and criminal
justice: a systematic review of advanced methodology for recidivism risk prediction.International
journal of environmental research and public health, 19(17):10594, 2022.
[59] D. Wang, E. Churchill, P. Maes, X. Fan, B. Shneiderman, Y . Shi, and Q. Wang. From human-human
collaboration to human-ai collaboration: Designing ai systems that can work together with people. In
Extended abstracts of the 2020 CHI conference on human factors in computing systems, pages 1–6,
2020.
[60] D. Wang, J. D. Weisz, M. Muller, P. Ram, W. Geyer, C. Dugan, Y . Tausczik, H. Samulowitz, and A. Gray.
Human-ai collaboration in data science: Exploring data scientists’ perceptions of automated ai.Pro-
ceedings of the ACM on Human-Computer Interaction, 3(CSCW):1–24, 2019.
[61] J. Wolfers and E. Zitzewitz. Interpreting prediction market prices as probabilities. Technical report,
National Bureau of Economic Research, 2006.
[62] J. Wu, R. Nivargi, S. S. T. Lanka, A. M. Menon, S. A. Modukuri, N. Nakshatri, X. Wei, Z. Wang,
J. Caverlee, S. M. Rajtmajer, et al. Predicting the reproducibility of social and behavioral science papers
using supervised learning models.arXiv preprint arXiv:2104.04580, 2021.
[63] Y . Yang, W. Youyou, and B. Uzzi. Estimating the deep replicability of scientific findings using human
and artificial intelligence.Proceedings of the National Academy of Sciences, 117(20):10762–10768,
2020.
[64] W. Youyou, Y . Yang, and B. Uzzi. A discipline-wide investigation of the replicability of psychology pa-
pers over the past two decades.Proceedings of the National Academy of Sciences, 120(6):e2208863120,
2023.
