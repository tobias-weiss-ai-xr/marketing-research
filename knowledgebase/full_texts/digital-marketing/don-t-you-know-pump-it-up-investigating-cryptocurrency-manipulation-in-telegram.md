---
title: Don't You Know, Pump it Up! Investigating Cryptocurrency Manipulation in Telegram-Driven Activity
url: https://arxiv.org/abs/2609.01176
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Filipe Moura
- Giordano Paoletti
- Carlos H. G Ferreira
- Jussara Almeida
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.01176
pages: 17
chars: 92792
fetched_at: '2026-11-08T13:19:33+00:00'
kb_version: 1
---

# Don't You Know, Pump it Up! Investigating Cryptocurrency Manipulation in Telegram-Driven Activity

Accepted at ICWSM 2027. If you cite this paper, please use the following reference:Moura, Filipe; Paoletti, Giordano; Ferreira,
Carlos H. G.; and Almeida, Jussara M. 2027.Don’t You Know, Pump It Up! Investigating Cryptocurrency Manipulation in
Telegram-Driven Activity.InProceedings of the 21st International AAAI Conference on Web and Social Media(To appear).
Don’t You Know, Pump it Up!
Investigating Cryptocurrency Manipulation in Telegram-Driven Activity
Filipe Moura1, Giordano Paoletti2, Carlos H.G. Ferreira 3, Jussara M. Almeida1
1 Universidade Federal de Minas Gerais, Belo Horizonte, Brazil
2 Politecnico di Torino, Turin, Italy
3 Universidade Federal de Ouro Preto, Ouro Preto, Brazil
{filipe.moura,jussara}@dcc.ufmg.br, giordano.paoletti@polito.it, chgferreira@ufop.edu.br
Abstract
Telegram plays a pivotal role in cryptocurrency communi-
cation and has been repeatedly associated with coordinated
schemes, such as pump-and-dump manipulation. However,
existing studies typically focus on known manipulation chats
or a limited set of cryptocurrencies, leaving open the ques-
tion of how Telegram is leveraged for mass promotional ac-
tivity (shilling) at scale. Moving beyond these limitations, this
work analyzes the interplay between information flows and
market activity across public Telegram channels. To this end,
we propose a scalable framework that (i) classifies crypto-
related messages using a fine-tuned encoder model to filter se-
mantic noise, (ii) detects anomalous spikes in cryptocurrency
mentions via adaptive thresholding, and (iii) validates tem-
poral associations between social bursts and market move-
ments using quasi-experimental econometric methods (RDD
and DiD). We apply this framework to one year of public
Telegram data (14,499 channels and over 20 million mes-
sages) aligned with transaction data for more than 17,000
cryptocurrencies. Our analysis identifies 47 events consis-
tent with potential pump-and-dump activity and 73 sustained
market reactions, showing that manipulative signals are char-
acterized by extreme temporal synchronization and precede
price movements by seconds. Notably, psycholinguistic anal-
ysis reveals that pump-and-dump messages are linguistically
indistinguishable from organic discussions, highlighting the
limits of text-based detection alone. Finally, we estimate
the cumulative financial volume of detected pump-and-dump
events to exceed $200 million and release a public cryptocur-
rency dictionary and a fine-tuned classifier to support future
research.1
Introduction
Telegram has become a central communication infrastruc-
ture for cryptocurrency communities, enabling rapid infor-
mation diffusion through large public channels (no mem-
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
1References:
Codehttps://github.com/Filipey/investigating-cryptocurrency-
manipulation-icwsm2027
Datasethttps://huggingface.co/datasets/filipeasm18/crytpo-
related-labeling
Dictionaryhttps://doi.org/10.5281/zenodo.22116582
Modelhttps://huggingface.co/filipeasm18/roberta-binary-crypto-
related-classifier
bership limits) and other high-reach spaces. At the same
time, its scale and limited oversight create a fertile ground
for institutionally illegal or ethically questionable activities
(La Morgia et al. 2023a; Roy et al. 2024) and have re-
peatedly been associated with coordinated market manip-
ulation, most notablyPump-and-dumpschemes, in a mar-
ket context characterized by high volatility and decentraliza-
tion (Mezquita et al. 2022). While such schemes have been
documented (Hu et al. 2023; Clough and Edwards 2023),
we still lack a clear ecosystem-level understanding of how
broadly public Telegram channels are involved in their co-
ordination beyond a small set of known manipulation chats
and highly visible assets.
Cryptocurrency markets are particularly sensitive to in-
formation flows, as prices react rapidly to speculative sig-
nals and social attention (Krishnan et al. 2024). Social me-
dia platforms, and Telegram in particular, play a key role in
disseminating such information, enabling the coordination
of large numbers of participants around specific assets (Mir-
taheri et al. 2021; Amirzadeh et al. 2023). Within this en-
vironment, coordinated schemes such asPump-and-dump
operations – where collective buying is used to artificially
inflate prices before a rapid sell-off– have emerged as a re-
current form of market manipulation, and their orchestra-
tion on Telegram and other platforms has been widely doc-
umented (La Morgia et al. 2023b).
Prior work has extensively studiedPump-and-dump
schemes by analyzing transaction data, sometimes in com-
bination with social media signals, to characterize their dy-
namics (Dhawan and Putnin ¸ˇs 2022; Nizzoli et al. 2020), de-
tect suspicious events, or predict their success (Amirzadeh
et al. 2023; Krishnan et al. 2024). However, these studies
typically focus on a limited set of predefined cryptocur-
rencies or on Telegram chats already known to orchestrate
manipulation. As a result, we still lack an ecosystem-level
view of how coordinatedPump-and-dumpactivity manifests
across Telegram more broadly, including beyond explicitly
crypto-focused channels.
In this study, we analyze public Telegram communication
alongside cryptocurrency market data to study how coor-
dinatedPump-and-dumpactivity emerges on the platform.
Rather than focusing on predefined assets or known manip-
ulation chats, our approach examines the relationship be-
tween information flows and financial transactions across
arXiv:2609.01176v1  [cs.SI]  1 Sep 2026

Telegram channels, enabling the identification of suspicious
coordination without prior assumptions about the coins or
channels involved. Moreover, since crypto-related discus-
sions frequently occur in non-crypto chats (Perlo et al. 2025;
Paoletti et al. 2025), we extend our analysis to Telegram
channels spanning diverse topical domains.
Drawing on information cascade theory and market
microstructure literature, we hypothesize that successful
Pump-and-dumpschemes may operate in two distinct
phases: a private coordination phase (in closed groups) and
a public amplification phase (in open channels) to gener-
ate sufficient exit liquidity. Regardless of how aPump-and-
dumpscheme is initially orchestrated, this implies that pub-
lic Telegram channels carry a systematic, temporally com-
pressed signal that is observable even without access to pri-
vate orchestration chats. In this study, public Telegram chan-
nels are treated as observable traces of promotional ampli-
fication and shilling activity, rather than as direct evidence
of the private coordination mechanisms that may precede
them. Our goal is to characterize Telegram’s role in potential
Pump-and-dumpschemes by presenting evidence of tem-
poral associations between crypto-related message volumes
and market prices. To this end, we structure our study around
three research questions:
RQ1:How can potentialPump-and-dumpattempts be
surfaced from large-scale Telegram activity and assessed
through subsequent market behavior?
RQ2:When do anomalous increases in cryptocurrency men-
tions on Telegram coincide with short-term market events
consistent withPump-and-dumpactivity?
RQ3:How do communication patterns of Telegram differ
betweenPump-and-dumpevents and periods of increased
cryptocurrency discussion driven by organic market move-
ments (transaction volume and price shifts)?
To address these questions, we propose a three-step an-
alytical framework designed to uncover and validate pat-
terns consistent withPump-and-dumpactivity on Telegram.
First, we build a crypto-related classifier to accurately filter
messages mentioning cryptocurrencies, addressing naming
ambiguities among viralaltcoins(e.g.,$Trump,$Jesus)
whose polysemic names complicate keyword-based detec-
tion (Anderson 2024). Second, we apply theCell-Average
Constant False Alarm Rate(CA-CFAR) method to detect
anomalous increases in daily cryptocurrency mentions, iden-
tifying candidate days for subsequent minute-level analy-
sis (Richards, Scheer, and Holm 2010; Bellutta and Carley
2023). Third, we employ a Regression Discontinuity Design
(RDD) combined with Difference-in-Differences (DiD) to
examine temporal associations between these social bursts
and market behavior (Lee and Lemieux 2010), using stable-
coins and Bitcoin as a control group to filter systemic noise
and distinguishPump-and-dumpattempts from other forms
of market activity. We then characterize the market impact
and communication patterns of the validated events to assess
the potential role of Telegram in market dynamics and how
communication during these events differs from legitimate
discussions.
In sum, our main contributions are fourfold: (1) a scalable
analytical framework that enables the study ofPump-and-
dumpcoordination on Telegram beyond predefined assets or
known manipulation chats; (2) a large-scale empirical anal-
ysis of public Telegram activity and cryptocurrency market
data, providing evidence of when anomalous social atten-
tion aligns with market behavior consistent withPump-and-
dumpactivity; (3) the release of a public dictionary con-
taining over 18,704 cryptocurrency-related terms (17,012
coins) to support future research in this area; and (4) a robust
crypto-related text classifier and a labeled dataset of 2,923
Telegram messages for model training and evaluation.
Background and Related Work
In this section, we review the main forms of cryptocurrency
market manipulation and summarize prior studies onPump-
and-dumpschemes.
Cryptocurrency Manipulation
Cryptocurrency markets are subject to various types of ma-
nipulations, including wash trading (Cong et al. 2023; Cui
and Gao 2023), Ponzi schemes (Bartoletti et al. 2020; Liang,
Chen et al. 2025), opportunistic blockchain transaction re-
ordering (Alipanahloo, Hafid, and Z 2024), and coordinated
NFT market manipulation (Sifat, Tariq, and van Donse-
laar 2024; Niu et al. 2024). Among these,Pump-and-dump
schemes remain one of the most prevalent forms of coor-
dinated manipulation (Victor and Hagemann 2019; Nghiem
et al. 2021; Dhawan and Putnin ¸ˇs 2022).
Briefly, the classicPump-and-dumpscheme consists of
three main steps. First, a target cryptocurrency is selected,
typically characterized by low market capitalization and
high volatility (Xu and Livshits 2019). Second, participants
coordinate high-volume purchases of the target asset (the
pump-coin) to artificially inflate its price. Finally, once the
desired price level is reached, early participants initiate the
dumpphase by selling their holdings at a profit, causing a
rapid price collapse that leaves later investors with signifi-
cant losses (Xu and Livshits 2019).
Pump-and-dumpschemes rely on a large number of par-
ticipants to generate sufficient trading volume, thus attract-
ing new investors and driving the price of the target cryp-
tocurrency. Prior work has documented the orchestration
of such schemes on major social media platforms (Nghiem
et al. 2021; La Morgia et al. 2023b), notably Telegram (Niz-
zoli et al. 2020; Clough and Edwards 2023; Chen and Cai
2023), where group/channel administrators orchestrate syn-
chronized message bursts to attract buyers and profit as early
sellers (Xu and Livshits 2019).
Grounded in market microstructure and behavioral fi-
nance theories of manipulation, we hypothesize that while
the initial orchestration of these schemes may occur in pri-
vate chats, their successful execution inherently requires
massive public exposure to generate exit liquidity and attract
external investors withFear of Missing Out(FOMO). There-
fore, monitoring public channels provides a distinct, highly
synchronized temporal footprint of the operational phase of
market manipulation, especially onPump-and-dumpactivi-
ties.

Prior Studies onPump-and-dumpSchemes
Some prior studies ofPump-and-dumpschemes aimed at
characterizing the manipulation ecosystem. For example,
prior work suggested that Twitter can act as a gateway for the
coordination ofPump-and-dumpand Ponzi schemes (Niz-
zoli et al. 2020), and can significantly influence cryptocur-
rency price appreciation (Amirzadeh et al. 2023). Others fo-
cused on pump events orchestrated on Telegram, identifying
the targeted cryptocurrencies and reporting long-term value
drops (Clough and Edwards 2023; Chen and Cai 2023).
Beyond classic pump groups, manipulative behavior has
also been observed in Initial Exchange Offerings (IEOs), a
fundraising mechanism conducted on exchanges, where bot-
driven Twitter hype correlates with short-term volatility and
pump-like dynamics (Tian and Xie 2024).
Another body of research aimed at detectingPump-and-
dumpevents by, for instance, leveraging Telegram mes-
sages to identify affected coins on major exchanges using
transaction-based classifiers (Victor and Hagemann 2019).
Multi-platform approaches, involving Telegram, Twitter and
Discord, have also been proposed (Mirtaheri et al. 2021;
La Morgia et al. 2023b). Additional work showed that tai-
lored oversampling and learning strategies can detect ma-
nipulation signals prior to the pump peak (Fantazzini and
Xiao 2023). Recently, temporal graph neural networks with
contrastive learning was applied on transaction data for real-
timePump-and-dumpdetection(Wu et al. 2025).
Another line of research focused on prediction models, by
using Random Forests with transaction data as input features
to predictPump-and-dumpsuccess in real time (La Morgia
et al. 2020), or leveraging neural networks to estimate the
maximum value reached by a pump (Nghiem et al. 2021).
Additional approaches combined web data (e.g., social me-
dia signals and Google searches) with transaction data to
predict price fluctuations and trading behavior (Boukhers
et al. 2023; Krishnan et al. 2024).
Our work differs from prior studies by addressing open
questions about howPump-and-dumpactivity manifests on
Telegram at scale. First, our approach enables the identi-
fication of cryptocurrencies potentially targeted byPump-
and-dumpmanipulation on Telegram without preselecting
specific coins, exchanges, or channels as orchestrators, un-
like (Victor and Hagemann 2019; Mirtaheri et al. 2021;
Clough and Edwards 2023). By not restricting the analy-
sis to cryptocurrency-focused channels, and acknowledging
that relevant messages may appear outside explicitly crypto-
related chats (Paoletti et al. 2025; Perlo et al. 2025), we cap-
turePump-and-dump-related activity across diverse Tele-
gram channel types. Second, we study how communication
patterns on Telegram differ duringPump-and-dumpevents
compared to periods of increased discussion driven by or-
ganic market movements.
Methodology
To investigate the interplay between online discussions and
cryptocurrency markets, we introduce an analytical frame-
work tailored to Telegram data. Our goal is the characteriza-
tion of patterns consistent withPump-and-dumpmanipula-
tion emerging from Telegram activity and the understand-
ing of how such activity intertwines with cryptocurrency
market dynamics. Specifically, we investigate whether Tele-
gram discussions precede, coincide with, or follow market
fluctuations, highlighting temporal links between social and
market dynamics. To achieve this, we design a three-step
pipeline that progressively refines the analysis, from raw
message streams to fine-grained temporal patterns, ensuring
both scalability and analytical precision. The pipeline, illus-
trated in Fig. 1, consists in:(1)building a classifier to accu-
rately filter crypto-related content;(2)detecting anomalous
spikes in the daily volume of Telegram messages mentioning
cryptocurrencies;(3)uncoveringTelegram–markettempo-
ral association to verify correlation links and assess whether
suspicious Telegram bursts acts as a signal for trading orders
or are an organic behavior tailored by a market trend. Such
temporal associations help characterize Telegram’s role in
market dynamics, revealing when activity patterns are more
consistent with potential manipulation signals or reactive
market responses.
The framework takes two primary data sources as input.
First, for Telegram, we leverage the TGDataset (La Mor-
gia, Mei, and Mongardini 2025), sampling its final year
(July 2021 – July 2022): Over 20 million messages across
14,499 public channels. Second, we utilize a dictionary of
cryptocurrencies, each with a corresponding time series of
transaction volumes and prices from one or more exchanges,
temporally aligned with the Telegram data. Unlike prior
work, this cryptocurrency dictionary is intentionally broad
and not restricted to assets previously linked toPump-and-
dumpevents. This lack of restriction allows for the unbiased
identification of coins exhibiting patterns consistent with po-
tential manipulation. We explain each step of our framework
in detail next.
Cryptocurrency Content-Related Classifier
Before identifying days with an anomalous volume of men-
tions for a cryptocurrency, it is necessary to validate the mes-
sage’s content due to possible polysemy caused by the coin’s
name. For instance, coins such asJesus,Skate, and
Trumpintroduce semantic ambiguity when relying solely
on keyword-based searches, potentially yielding false pos-
itives from discussions unrelated to cryptocurrencies. A se-
mantic classifier is therefore not merely a preprocessing con-
venience but a necessary design choice. To account for mes-
sage context, we employ an experimental setup to evaluate
the usage of Large and Small Language Models (SLMs and
LLMs) to classify captured messages ascrypto-relatedor
not, a new challenge that arises from the abundantPump-
and-dumpoccurrences search across a broad Telegram snap-
shot.
Data AnnotationTo establish a reliable ground truth for
identifying cryptocurrency-related discourse, we curated a
dataset of 2,923 messages. This corpus was strategically
sampled to capture the diverse linguistic nuances of the
ecosystem:
•High-Risk Domain Specific (463 messages):Targeted
samples from assets historically prone to manipulation

Figure 1: Pipeline for revealing possiblePump-and-dumpoccurrences driven by Telegram activities.
(e.g., memecoins and confirmed Pump-and-Dump cases
such as$HAWK 2 and$LIBRA 3).
•Random Lexical Sampling (1,960 messages):Obtained
using a comprehensive 18,704-term cryptocurrency dic-
tionary to capture general organic discourse.
•Manipulative Context (500 messages):Sourced from
known predatory groups during confirmed manipulation
windows as defined by La Morgia et al. (2020).
The annotation process was conducted by three Master’s
students in Computer Science. Given the technical nature
of the task and the absence of external domain special-
ists, annotators followed a rigorous binary classification pro-
tocol:“A message is crypto-related if it mentions Cryp-
tocurrencies (Bitcoin, Ethereum, altcoins, tokens), NFTs,
blockchain, Web3, DeFi, exchanges, wallets, mining, stak-
ing, airdrops, crypto trading, investing, tokens, presales, jar-
gons or memecoins. Even a brief or indirect mention is suffi-
cient”. To ensure the reliability of the resulting ground truth,
we calculated the Fleiss’ Kappa and Krippendorff’s Alpha
score to quantify inter-annotator agreement before adopt-
ing the majority-vote labels for subsequent model evaluation
(McHugh 2012).
Experimental ConfigurationOur experimental design
aims to identify the optimal balance between computa-
tional efficiency and classification effectiveness. We se-
lected a heterogeneous set of models to represent the
current state-of-the-art in both Large Language Mod-
els (LLMs) and encoder-based architectures:Llama 3.1
8b-Instruct,Gemma 7b v1,Qwen2.5 7b, and
RoBERTa-Base(Liu et al. 2019; Grattafiori et al. 2024;
Gemma Team et al. 2024; Bai et al. 2025). The choice
of these specific models is justified by their architec-
tural diversity and performance benchmarks.Llama 3.1,
Gemma, andQwenrepresent top-tier decoder-only models
with strong instruction-following capabilities, optimized for
varying parameter scales that remain feasible for institu-
tional hardware. In contrast,RoBERTa-Basewas selected
as a discriminative baseline; its bidirectional encoder archi-
tecture is traditionally more efficient for sequence classifi-
cation tasks with lower computational overhead compared
to generative LLMs. Each model was evaluated across four
distinct learning paradigms:
2https://www.bbc.com/news/articles/c89xvjkzzyvo
3https://www.bbc.com/news/articles/cp9x9j89evxo
1.Zero-Shot Classification: (ZSC)The model classifies
messages based solely on its pre-trained knowledge with-
out any specific instructions.
2.Zero-Shot In-Context Learning (ZS-ICL):The classi-
fication is guided by the inclusion of the official annota-
tion guidelines within the prompt.
3.Few-Shot In-Context Learning (FS-ICL):The prompt
includes five randomly selected exemplars (3 positive, 2
negative) to provide the model with a linguistic pattern
for comparison, following best practices in recent litera-
ture (Cunha, Rocha, and Gonc ¸alves 2025).
4.Fine-Tuning (FT):The models undergo supervised
weight adjustment on a dedicated training split of the an-
notated dataset, representing the upper bound of domain-
specific adaptation.
To ensure the robustness and generalizability of the Fine-
Tuning results, we implemented a 5-fold Cross-Validation
scheme (80/20 split), mitigating potential biases in the train-
ing distribution. For ICL methods, we maintained a uni-
fied prompt template and employed deterministic decoding
(e.g., temperature set to 0) to ensure fair and reproducible
comparisons between LLMs; the full prompt architecture
is detailed in Appendix A. Beyond standard effectiveness
metrics, specifically, Recall, Precision, F1-Score, and Accu-
racy (Cunha, Rocha, and Gonc ¸alves 2025), we conducted
an efficiency analysis by measuring mean inference time.
This dual-metric approach allows for identifying the optimal
model that achieves high classification performance without
prohibitive computational costs for possible real-time moni-
toring of large-scale Telegram data.
To further ensure the temporal robustness and generaliza-
tion of our annotations, we conducted an additional valida-
tion experiment. We extracted a temporally stratified sam-
ple of 520 messages spanning 13 months (July 2021 to July
2022), balanced by the model’s predictions (predicted pos-
itive vs. negative). By blinding human annotators to the
model’s predictions, we evaluated the False Positive (FP)
and False Negative (FN) rates, confirming that the classifier
maintains stable accuracy across time without introducing
systematic bias. More details are available in Appendix A .
Detection of Anomalous Spikes in Telegram
After training the crypto-related classifier, our framework
proceeds by identifying days exhibiting ananomalousvol-
ume of messages mentioning a cryptocurrency. Specifically,

Telegram messages are first matched against a comprehen-
sive cryptocurrency dictionary to collect candidate men-
tions, and are then filtered using the trained classifier to re-
move false positives due to polysemy. Only after this seman-
tic filtering step do we construct time series of daily men-
tion counts. For each cryptocurrencymin the dictionary, we
count the daily number of messages containing its official
ticker (i.e.,$m) and its primary variants (”m”, ”mcoin”, and
”mtoken”). This count is computed across all channels, re-
gardless of their specific topic, as prior work has shown that
cryptocurrency-related information often transcends crypto-
specific channels (Paoletti et al. 2025).
Given the significant heterogeneity in the popularity of
cryptocurrencies, an effective anomaly detection method
must adapt to the specific context of each coin rather than
relying on a single global threshold. Therefore, in this work,
we adopt a time-series anomaly detection method known
asCell-Average Constant False Alarm Rate(CA-CFAR)
(Richards, Scheer, and Holm 2010). This is one of sev-
eral implementations of the CFAR (Constant False Alarm
Rate) algorithm, which has previously been employed for
detecting activityburstsin social media (Bellutta and Car-
ley 2023).
CFAR adjusts a detection threshold adaptively to main-
tain a constant rate of false alarms. Specifically, for a given
time series, CFAR uses a sliding window to evaluate each
data point, referred to as the Cell Under Test (CUT). It then
estimates a thresholdTbased on the signal magnitude in
the cells neighboring the CUT 4. The daily threshold is de-
fined asT=αP n, whereP n represents an estimate of the
background noise derived from neighboring cells, andαis a
scaling factor controlling the sensitivity of the detector.
The background estimateP n is computed from cells ad-
jacent to the CUT on both sides of the time series. A sliding
window centered on the CUT is applied, parameterized by
Ntrainingcells andMguardcells on each side. Theguard
cells, located immediately adjacent to the CUT, are excluded
from the noise calculation to prevent the target signal from
contaminating the background estimate (Richards, Scheer,
and Holm 2010). CA-CFAR estimates the background level
separately for the left and right sides of the CUT and then
averages the two estimates.
Formally, letx t be the value of the time series on day
t, and letddenote the direction relative to the CUT (left:
preceding days;right: subsequent days). LetN d andM d de-
note the number of training and guard cells in directiond,
respectively. For a CUT at dayt, the directional background
estimate is defined as:
Pd(t) = 1 Nd
Md+NdX
k=Md+1
xt+sdk, d∈ {left,right},
wheres left =−1ands right = +1. In our symmetric set-
ting,N left =N right =NandM left =M right =M.
The final background-noise estimate is then computed as
Pn(t) = 1 2 (Pleft(t) +P right(t)). The CA-CFAR algorithm computes the scaling factorα
4https://www.mathworks.com/help/phased/ug/constant-false-
alarm-rate-cfar-detection.html
from a given Probability of False Alarm (P f ), which is in-
terpreted as the expected fraction of data points classified as
anomalies. LetN tot =N left +N right denote the total num-
ber of training cells used to estimate the background level.
The scaling factor is computed asα=N tot

P −1/Ntot f −1  .
With the values ofP n(t)andα, the threshold is computed
asT(t) =αP n(t). For each cryptocurrency time series,
we computeα,P n(t), andT(t)on a daily basis to iden-
tify anomalous days, i.e., days in which the message volume
exceeds the adaptive thresholdT(t).
Considering the context of market manipulation, where
target coins are often less popular andPump-and-dump
events are typically short-lived, frequently lasting only min-
utes or hours (Xu and Livshits 2019; La Morgia et al. 2020;
Nghiem et al. 2021), we set the following parameters:N=
5training cells on each side of the CUT,M= 1guard cell
on each side to mitigate noise from post-event discussions
(La Morgia et al. 2023b; Clough and Edwards 2023; Mirta-
heri et al. 2021), andP f = 0.05. This represents a conser-
vative approach intended to detect only the most significant
deviations from the recent baseline. HigherP f values in-
crease the number of detections but also elevate the risk of
false positives (Richards, Scheer, and Holm 2010). Sensitiv-
ity checks around the definition of training and guard cells
are explored in Appendix B .
Telegram-Market Temporal Association
To rigorously assess the temporal association between
social-media-driven information shocks and cryptocurrency
market microstructures, we employ a multi-layered econo-
metric strategy. This study goes beyond simple correlation
by integrating quasi-experimental designs, specifically, Re-
gression Discontinuity Design (RDD) and Difference-in-
Differences (DiD), to control for unobserved market noise
and systemic volatility.
Data Acquisition and Preprocessing
To investigate temporal associations, we retrieve high-
frequency market data (Open, High, Low, Close, and V ol-
ume) for all cryptocurrencies mentioned in the identified
Telegram bursts. Data is gathered from theCoinDesk
Data APIat a 1-minute resolution 5. This granular scale
is essential to capture the rapid onset ofPump-and-dump
events, which often manifest and peak within minutes rather
than hours (Xu and Livshits 2019). Given the heterogeneous
nature of cryptocurrencies, raw prices and volumes are not
directly comparable. We therefore transform the raw data
into two statistical metrics (Van Tran and Kukal 2022):
1.Accumulated Logarithmic Returns (R acc): We con-
vert closing prices into logarithmic returns (r t =
ln(Pt/Pt−1)), which, unlike simple returns, are time-
additive, a property essential for computing cumulative
returns consistently across our observation window. The
cumulative sum is calculated fromT −30, centering the
series at zero at the start of the analysis to standardize the
baseline across all events.
5https://developers.coindesk.com

2.z-Scored Volume (z vol): Trading volume is normalized
into z-scores (zvol = (V t −µ V )/σV ) based on the local
mean and variance within the analysis window. This met-
ric identifies volume spikes as statistical outliers relative
to each asset’s own baseline, enabling cross-asset com-
parison regardless of underlying liquidity, an approach
more robust than percentage changes, which can be ex-
cessively volatile for low-liquidity assets.
Causality Methods
We adopt the Sharp RDD framework (Lee and Lemieux
2010) to characterize the discontinuity in market behavior
at the onset of a Telegram social burst. In our setting, once
a day is identified as anomalous, the cutoff point (T 0) is de-
fined as the timestamp of the first message mentioning the
cryptocurrency on that day. Market dynamics are then an-
alyzed at minute-level resolution within a 3-hour window
spanning1.5hours before and afterT 0. The RDD exploits
the discontinuity at this threshold, assuming that in the ab-
sence of the “treatment” (the social burst), the market vari-
ables would follow a continuous trend. The model is speci-
fied as:Y t =β 0 +β 1Dt +β 2(t−T 0) +β 3Dt(t−T 0) +ϵ t,
whereD t is a dummy variable indicating the post-burst pe-
riod (t≥T 0). The coefficientβ 1 represents the instanta-
neous Jump in price or volume, whileβ3 captures the change
in the slope, which we use to quantify the subsequent Rever-
sal Ratio and V olume Decay. To ensure the robustness of our
estimates, we performed a sensitivity analysis across a range
of bandwidths:{10,15,30,45,60,90,120}minutes. We ob-
served that narrow windows (under 30 minutes) often failed
to yield statistically significant results due to high-frequency
noise and insufficient data points to establish a stable pre-
treatment trend. Conversely, while larger windows (above
90 minutes) maintained detection stability, they increased
the risk of contamination from exogenous market volatil-
ity. Consequently, the 1.5-hour bandwidth was selected as
the optimal trade-off, providing consistent significance lev-
els and a reliable baseline for characterizing the immedi-
ate impact and subsequent decay of the suspected manip-
ulation. To rigorously account for potential “pre-heating” or
early private coordination leaking into the public domain
(i.e., thatT 0 may follow earlier coordination in private or
smaller channels not captured in the data), we implemented
a placebo test within our RDD framework. We shifted the
analysis window to a placebo threshold 3 hours before the
actual event (T0-3h), ensuring no temporal overlap with the
main RDD window (±1.5h aroundT 0), which could oth-
erwise introduce cross-contamination bias in the estimates.
Any cases exhibiting a statistically significant upward trend
before the main burst were systematically filtered out. This
ensures our detectedT 0 captures a genuine, sudden anomaly
rather than the continuation of prior momentum.
A significant challenge to RDD in financial markets is
the presence of simultaneous external shocks (e.g., a sud-
den Bitcoin price swing occurring exactly atT 0). To miti-
gate this, we implement a Difference-in-Differences (DiD)
framework using a placebo control group. We synchronize
the timestamps of identified anomalies with the market data
of major stablecoins (USDT, USDC, DAI) and Bitcoin, as it
is the most popular cryptocurrency in terms of market capi-
talization ($USD 1.2 trillion), which can guide systematic
fluctuations. As the stable assets are pegged to the USD,
they are theoretically immune to idiosyncraticPump-and-
dumpcoordination, while Bitcoin is effectively unaffected
due to its size and liquidity. By comparing the treated altcoin
with the control group, wedifference outsystemic noise:
δDiD= (Y Target,Post −Y Target,Pre)−(Y Control,Post −Y Control,Pre)
A statistically significantδDiDthat mirrors the RDD jump
provides robust evidence that the market anomaly was id-
iosyncratic to the Telegram activity rather than a reflection
of global market trends. The validity of this combined ap-
proach relies on three key assumptions (Trochim 1990): (i)
continuity of variables around the cutoff in the absence of
the shock, (ii) absence of cutoff manipulation, and (iii) paral-
lel trends between the target coin and the stablecoin/Bitcoin
control beforeT 0.
While alternative approaches, including Interrupted Time
Series (ITS) and Convergent Cross Mapping (CCM), were
also evaluated, the combination of RDD and DiD proved the
most robust and scalable framework for our setting (see Ap-
pendix C for a detailed comparison). Despite these controls,
we interpret the observed discontinuities as strong correla-
tional evidence of social-media-driven market manipulation
rather than absolute causal proof.
To provide a granular distinction between market phe-
nomena, we classify each event into one of three cate-
gories: Insignificant, Sustained Market Reaction, orPump-
and-dump. This classification is governed by two key be-
havioral metrics derived from the post-event window: the
Reversal Ratio (RR) and the V olume Decay (VD). The cate-
gorization criteria are structured as follows: (I) Insignificant:
Events where the RDD jump magnitude (β1) is below 1%, or
the p-value exceeds0.05. This filter eliminates minor fluctu-
ations and statistically weak associations, ensuring that only
robust market movements are analyzed. (ii) Sustained Mar-
ket Reaction: Events that exhibit a significant jump (>1%)
but maintain the price level. This is characterized by a Re-
versal Ratio≤0.7and a V olume Decay≥0.3, suggesting
that the information shock led to a new price equilibrium
supported by ongoing trading interest. (iii)Pump-and-dump
(P&D): Events characterized by a significant price spike fol-
lowed by a rapid collapse. This is identified by a Reversal
Ratio>0.7or a V olume Decay<0.3.
The selection of these thresholds is rooted in the princi-
ples of Market Microstructure and Efficient Market Hypoth-
esis (EMH) adaptations for high-frequency crypto-assets
(Malkiel 1989). In an efficient market, if an announcement
carries fundamental value, the price should stabilize at a new
plateau (Price Discovery). A reversal exceeding 70% of the
initial gain implies that the movement lacked fundamental
support and was driven by transitory, speculative pressure.
We adopt 0.7 as a conservative limit: it allows for minor nat-
ural corrections (up to 30%) while strictly flagging events
where the majority of thewealthcreated by the spike was
decimated shortly after. This aligns with empirical studies on
crypto-manipulation showing thatPump-and-dumpschemes
typically return to the mean (mean-reversion) within min-
utes (La Morgia et al. 2020; Xu and Livshits 2019). V olume

is a proxy for market conviction. A sustained reaction is typ-
ically accompanied by avolume hysteresis, where trading re-
mains elevated as the market processes the new information.
Conversely, coordinated manipulation relies on a massive,
synchronized burst of orders. A decay below 0.3 indicates
that post-spike liquidity has evaporated to less than 30% of
its peak intensity. Thisliquidity exhaustionis a hallmark of
artificial activity. Once the coordination (or the bot’s execu-
tion) ends, the absence of organic interest causes the volume
todry up, confirming the initial spike was a non-fundamental
artifact. Setting a higher RR (e.g., 0.9) would fail to capture
partial dumps where the price settles slightly above the start.
At the same time, a lower VD (e.g., 0.1) would be too re-
strictive, ignoring cases where residual panic-selling main-
tains some volume. Thus, the 0.7/0.3 threshold pair serves
as a robust filter to isolate coordinated anomalies from or-
ganic price discovery. Importantly, these threshold values
are heavily theory-driven, reflecting the characteristic be-
havior ofPump-and-dumpschemes established in the litera-
ture. To empirically validate these parameters, we conducted
a sensitivity analysis across different threshold configura-
tions (detailed in Appendix C). Overall, event categoriza-
tion intoPump-and-dumpand SMR remains stable across
configurations, with only a small set of borderline cases af-
fected by parameter variation. A targeted manual inspection
of these ambiguous cases confirms that the 70/30 configura-
tion minimizes misclassifications, supporting the robustness
and practical reliability of our automated separation.
Results
This section presents our findings, structured to address:
identifying suspected pump occurrences (RQ1), establish-
ing temporal precedence between social signals and market
shifts (RQ2), and characterizing the information ecosystem
involved (RQ3).
Crypto-Related Classifier
The inter-annotator agreement was fair in overral (Fleiss’
Kappa/Krippendorff’s Alpha =0.88/0.88), with stratified re-
sults showing higher consensus inRandom Lexical Sam-
pling(0.69/0.69) compared to the more ambiguousHigh-
Risk(0.50/0.49) andManipulative(0.40/0.40) contexts,
which underscores the linguistic complexity of predatory
discourse. After annotation, the resulting dataset exhibited a
class distribution of 76% non–crypto-related messages and
24% crypto-related messages. The selection of the primary
classification model was based on a dual-objective optimiza-
tion: maximizing predictive effectiveness (specifically Re-
call for the minority crypto-class) and minimizing compu-
tational overhead for longitudinal large-scale inference. Ta-
bles 1, 2, and 4 provide a comprehensive overview of these
dimensions. To ensure the reliability of our comparisons,
we applied a two-tailed t-test with Bonferroni correction
(α= 0.05) to all metrics.
Our results reveal a stark performance bifurcation be-
tween learning paradigms. Supervised Fine-Tuning (FT)
consistently outperformed all In-Context Learning (ICL)
and Zero-Shot (ZS) configurations by an average mar-
gin of 40 percentage points across F1-scores. Within the
Model/Method Prec 0 Rec0 F10
roberta (FT) 98.1(0.3)▲96.8(0.8)•97.5(0.4)▲
gemma-7b (FT) 97.3(1.0)•97.3(0.9)▲97.3(0.4)•
llama3.1-8B (FT) 97.3(0.8)•97.1(1.3)•97.2(0.4)•
qwen2.5-8B (FT) 97.0(0.6)•97.1(0.6)•97.1(0.2)•
gemma-7b (ZS) 75.88(1.4) 49.21(1.8) 59.69(1.6)
llama3.1-8B (ZS) 74.53(1.5) 47.95(3.0) 58.31(2.6)
qwen2.5-8B (ZS) 76.42(1.9) 50.38(2.5) 60.70(2.2)
gemma-7b (ICL Z) 75.91(0.7) 50.92(2.4) 60.91(1.6)
llama3.1-8B (ICL Z) 76.75(0.9) 48.45(2.5) 59.37(2.1)
qwen2.5-8B (ICL Z) 76.48(1.0) 51.69(0.9) 61.68(0.7)
gemma-7b (ICL F) 75.31(1.9) 49.35(1.7) 59.62(1.8)
llama3.1-8B (ICL F) 75.93(1.1) 48.58(0.8) 59.24(0.7)
qwen2.5-8B (ICL F) 75.93(0.7) 51.10(3.3) 61.04(2.5)
Table 1:Non-Crypto-related performance[Avg(Std)].▲Best,•Tie.
FT paradigm, the models achieved near-perfect perfor-
mance for non-crypto messages (C 0), with F1-scores ex-
ceeding 97%. Critically, for the crypto-related class (C 1),
RoBERTa-baseachieved the highest effectiveness, reach-
ing a Recall of 94.0% and an F1-score of 92.2%. While
RoBERTanumerically surpassed the larger decoder-based
models (e.g.,Llama-3.1-8Bat 91.6% Recall), the t-test
with Bonferroni correction confirmed a statistical tie among
all fine-tuned architectures. This finding demonstrates that
the inherent bidirectional context of an encoder-only archi-
tecture likeRoBERTais as capable as LLMs with60×more
parameters for this specific domain task.
In terms of efficiency, the in-context approaches were
evaluated based on inference time during the validation
phase. For the fine-tuning experiments, we randomly se-
lected a subset of 618,473 messages, from which approxi-
mately 100,000 samples were classified by each model to
measure inference time. While the models were statistically
equivalent in effectiveness, they were profoundly divergent
in computational efficiency.RoBERTa(FT) proved to be the
only viable candidate for real-time monitoring of 17,000 as-
sets. During the validation phase,RoBERTaachieved an av-
erage inference latency of 4.78 ms per message, representing
a13.3×speedup overLlama-3.1-8B(63.63 ms) and an
18.3×speedup overQwen-2.5-7B(87.79 ms); further de-
tails are reported in Table 4 in Appendix A.
The training phase mirrored this efficiency;RoBERTa
completed its fine-tuning process in approximately 89 sec-
onds, being5.6×faster thanLlama-3.1-8B. Given that
ICL methods-despite avoiding training, incurred prohibitive
inference latencies (exceeding 100,000 ms per message in
few-shot settings), the fine-tunedRoBERTamodel was se-
lected as the optimal backbone for our analysis, combining
state-of-the-art predictive power with the throughput nec-
essary for large-scale data processing. These results con-
tribute to a growing body of work questioning the assump-
tion that LLMs are the optimal solution across all NLP
settings (Bucher and Martini 2024; Cunha, Rocha, and
Gonc ¸alves 2025), suggesting that for domain-specific clas-
sification under real-world constraints, architectural simplic-
ity may be preferable to scale.

Model/Method Prec 1 Rec1 F11
roberta (FT) 90.5(2.1)•94.0(1.0)▲92.2(1.1)▲
gemma-7b (FT) 91.4(2.4)▲91.3(3.2)•91.3(1.5)•
llama3.1-8B (FT) 91.0(3.3)•91.6(2.6)•91.2(1.0)•
qwen2.5-8B (FT) 90.9(1.5)•90.6(1.9)•90.7(0.7)•
gemma-7b (ZS) 24.01(1.3) 50.65(2.8) 32.58(1.7)
llama3.1-8B (ZS) 22.76(1.4) 48.36(3.3) 30.94(1.8)
qwen2.5-8B (ZS) 24.54(1.9) 50.92(4.4) 33.10(2.6)
gemma-7b (ICL Z) 23.98(0.6) 48.94(3.7) 32.17(1.7)
llama3.1-8B (ICL Z) 24.87(0.9) 53.77(0.9) 34.00(0.9)
qwen2.5-8B (ICL Z) 24.60(1.0) 49.79(3.0) 32.92(1.6)
gemma-7b (ICL F) 23.43(1.9) 48.94(4.1) 31.69(2.6)
llama3.1-8B (ICL F) 24.02(1.1) 51.35(3.1) 32.73(1.6)
qwen2.5-8B (ICL F) 24.10(0.9) 48.93(2.6) 32.26(1.0)
Table 2:Crypto-related performance[Avg(Std)].▲Best,•Tie.
The temporal robustness and generalization test indicates
stable model performance over time, with a Macro-F1 aver-
aged over 13 months (91.4%) and consistent results across
both classes (0 and 1:92.2%/90.5%), with no evidence of
temporal drift. We also observe substantial inter-annotator
agreement (Fleiss’ Kappa>>0.6across all months), sup-
porting the reliability of these findings (see Appendix A).
TakeawayRoBERTamatches or outperforms LLMs in
identifying crypto-related messages, while also being com-
putationally scalable for large-scale Telegram analysis.
Detection of Anomalous Market Occurrences
Initially, our monitoring infrastructure tracked 17,000
unique digital assets across a vast network of Telegram chan-
nels. To addressRQ1and manage this high-dimensional
data, we employed a fine-tuned RoBERTa model, which
served as a semantic gatekeeper by isolating strictly crypto-
related discourse from general social noise. Once the data
were cleaned, the CA-CFAR algorithm identified 9799
bursts of social activity that reached a statistically anoma-
lous threshold, signaling purely social messaging anomalies.
It is crucial to emphasize that at this stage, no classifica-
tion of manipulation is made. To properly quantify and clas-
sify these events, the social bursts were synchronized with
high-frequency market data to test for price discontinuities
coincident with the bursts. Using a Regression Discontinu-
ity Design (RDD), we observed 302 immediate price and
volumejumpsfollowing the social signals. The RDD-based
placebo test atT 0 −3hyielded only 1 statistically signifi-
cant case, which was filtered out. This near-absence of pre-
existing trends supports the validity of ourT 0 definition as
a genuine, sudden anomaly. To ensure these movements
were idiosyncratic and not merely reflections of broader
market trends, we applied a Difference-in-Differences (DiD)
framework using stablecoins and Bitcoin as a control group.
This econometric rigor allowed us to discard systemic noise,
leaving a core sample of 120 validated high-impact events,
comprising 47Pump-and-dump(P&D) cases and 73 Sus-
tained Market Reactions (SMR), separating two kinds of
temporal association (RQ2). Figure 2a exemplifies the trad-
ing history for one detectedPump-and-dumpcase for the
0.78
0.80
0.82
0.84
Price
Dec 24, 22:03Dec 24, 23:43Dec 25, 01:23
0
50000
Volume
CHR | 2021-12-25
(a)$CHRPump-and-dump.
5.5
6.0
6.5
7.0
7.5
8.0
Price
Dec 08, 23:58Dec 09, 01:38Dec 09, 03:18
0
500
Volume
BICO | 2021-12-09 (b)$BICOmarket trend.
Figure 2: Signature behavior for P&D and SMR cases.
coin$CHRin 2021. The yellow vertical line represents the
detected message burst in Telegram, and the lines indicate
positive or negative pricing movement based on the last ob-
servation (1-minute interval). The chart’s bottom represents
the trading volume and type, where blue lines represent buy
orders and red lines represent sell orders. This$CHRcase
is a classicPump-and-dumpoccurrence, where the target
coin’s final price gets marginally lower or even than the orig-
inal price. The buy orders before the burst of messages are
possible from insiders, who are traders with previous infor-
mation about thePump-and-dumpoccurrence (channel ad-
ministrators or VIP members), as described by (La Morgia
et al. 2020). Figure 2b describes a possible$BICOmarket
valuation trend guided by external events. The trading and
pricing patterns are not aligned with short-livedPump-and-
dumpoccurrences, but could be some long-term manipu-
lation calledCrowd-Pump, which is a cooperative manip-
ulation model that instigates the holding of the target asset
within the goal of further valuation (La Morgia et al. 2023b).
Takeaway:(i) Telegram exhibits frequent anomalous at-
tention bursts, but only a small subset translates into sig-
nificant price and volume discontinuities, surfacing candi-
date Pump-and-dump attempts at scale. (ii) RDD–DiD val-
idation separates coordinated Pump-and-dump events from
sustained, non-manipulative market reactions.
The Telegram Information Ecosystem
In terms of diversity of Telegram’s ecosystem (RQ3), the
P&D cases accomplish 43,675 messages and 2,391 unique
channels. The SMR group contains 7,210 messages and
2,081 channels. From this collection, 2,071 channels were
present in both scenarios, indicating a high overlap in
crypto-related content emissors. 410 channels were exclu-
sive for emitting P&D messages, while only 10 were present
in SMR events. We used the provided channel’s label de-
fined by the dataset creators (La Morgia, Mei, and Mongar-
dini 2025) to explore the spreadness across different social
spheres during crypto manipulation schemes or just com-
monplace discussions. As presented in Figure 3, the major-
ity of channels were fromUS NewsandReligioncommu-
nities from both cases, with crypto groups being less than
10% of the discussion spots. That highlights theCrypto’s
Everywhere phenomenonobserved by Paoletti et al. (2025),
which is the acceptance of this theme across diverse social
contexts, and not only being an echo chamber in social plat-

CardingCovidCrypto
Entertainment
Extremists and radicals
Indian edu
Porn
ReligionSocial SoftwareUS news
Videogame modding
World news
Topic
0
10
20
30Channels (%)
Pump & Dump
Sustained Market Reaction
Figure 3: Channel Topics by Event Type (P&D, SMR).
0 200
Frequency
binance coin
volume buy
buy sell
dogecoin doge
attack leaders
defense leaders
castle points
digibyte dgb
bored attacked
market cap
castle attack
smart chain
bnb binance
tetherus binancebnbusdt
binancebnbusdt analysis
(a) P&D frequent bigrams.
0 200 400
Frequency
binance coin
smart chain
buy sell
volume buy
binance smart
jesus christ
bnb chain
god bless
price change
newest submissions
submissions ireland
ireland rss
market cap
buying volume
sell net (b) SMR frequent bigrams.
Figure 4: Most frequent bigrams between P&D and SMR
cases.
forms. Other relevant topics areCovidandEntertainement.
To characterize the distinctions of both cases, we explored
the message’s content, aiming to observe textual patterns
that could differentiate P&D instances from normal discus-
sions, as only overlooking crypto channels seems not be suf-
ficient. First, we observed the most frequent bigrams in each
case, excluding classical stopwords, and also possible links
included. Figure 4 illustrates the most frequent bigrams for
each case. As observed, both mainly contain the same dialect
of incisive terms such asbuy,sell, andbuying. Combinations
such asBinance coin,changing price,smart chainare com-
monly used terms in this environment as well. However, Fig-
ure 4a shows that P&D cases lack many non-crypto bigrams
commonly observed in organic discussions (e.g., references
to news feeds or public figures). Despite punctual mentions,
the bigram frequency reveals the similarity in the text con-
tent for both cases, with the message volume as a disruptive
differential. Examples of messages from P&D and SMR can
be found in Appendix D .
Beyond surface lexical patterns, we apply Linguistic
Inquiry and Word Count (LIWC-2015) (Mohammadin-
odooshan and Carlsson 2025; Trinh, Zarin, and Rezapour
2025) to analyze the psycholinguistic properties of mes-
sages. LIWC maps words to validated linguistic, cognitive,
and emotional categories; we focus on six dimensions com-
monly associated with persuasive, directive, and urgency-
driven communication (Certainty, Power, Reward, Tentative,
Pos Emo, and Focus Present), which prior work has linked
to coordinated influence and financial persuasion. To re-
duce noise from repeated messages, we only consider unique
messages per event. As shown in Figure 5, none of these di-
mensions significantly differ between P&D and SMR mes-
Certainty Power RewardT entativePos_EmoFocus_Present
Psychological Dimension (LIWC 2015)
0
2
4
6
8Mean Word Usage (%)
Pump & Dump
Sustained Market Reaction
Figure 5: LIWC values for each category.
sages. Consistent with our bigram analyses, this shows that
the linguistic surface of pump messages is largely indistin-
guishable from organic crypto discourse, revealing strong
semantic mimicry and disputing the discriminative power of
text-based analysis alone.
Temporal Latency and PrecedenceSince textual pat-
terns alone fail to provide a clear demarcation between the
two cohorts, the critical diagnostic dimension lies not in
what is said but in when it is said relative to the market
event it co-occurs with. Manipulation theory predicts a spe-
cific temporal ordering: in aPump-and-dumpscheme, social
signals serve as the trigger for price movement, meaning co-
ordinated messaging must systematically precede the price
peak. Conversely, in organic Sustained Market Reactions,
social discussion is a response to market events, and mes-
sages should therefore concentrate after the price reaches its
local maximum.
To operationalize this, we compute the latency of each
message relative to the price peak of its associated event
(the moment of maximum accumulated return within the
observation window). Negative latency values indicate mes-
sages that were posted before the price peak; positive val-
ues indicate messages that followed it. Figure 6 illustrates
the resulting distributions forPump-and-dump(N=47) and
Sustained Market Reaction (N=73) events. The distributions
diverge sharply in a manner consistent with the theoretical
prediction. ForPump-and-dumpevents, the median mes-
sage latency is -256seconds (-4.3minutes), meaning that,
at the midpoint of the distribution, coordinated social activ-
ity precedes the price peak by over four minutes. For Sus-
tained Market Reactions, the median is +868seconds (+14.5
minutes), indicating that social discussion concentrates after
the price has already peaked. The difference between medi-
ans is1,124seconds (18.7minutes), a gap large enough to
carry clear interpretive weight. A two-sample Kolmogorov-
Smirnov test confirms that the two distributions are drawn
from significantly different underlying processes (KS statis-
tic =0.272,p= 0.0006), validating that the observed
separation in temporal structure is not attributable to sam-
pling noise. We report median rather than mean as the pri-
mary central tendency measure, given the heavy-tailed, non-
normal character of both distributions.
As illustrated in Figure 6, the P&D density (orange)
is left-skewed relative to the price peak, with substantial
mass concentrated in the pre-peak window between approx-
imately -4,000and 0 seconds. The SMR density (blue) is bi-
modal, with a first mode just before the peak and a dominant
second mode near +3,000seconds, consistent with an initial

6000
 4000
 2000
 0 2000 4000 6000
Seconds relative to Price Peak
0.000000
0.000025
0.000050
0.000075
0.000100
0.000125
0.000150
0.000175
0.000200Message Density
Pump & Dump
Market Reaction
Price Peak
Figure 6: Latency Comparison between P&D and SMR
within±1hour around the price peak.
reactive spike of attention at the price event followed by sus-
tained community discussion as the new price level is pro-
cessed and debated. Together, these temporal profiles consti-
tute the primary behavioral signature distinguishing manip-
ulation from organic market activity in our dataset.Pump-
and-dumpevents are characterized by social coordination
that leads to price peaks; Sustained Market Reactions are
characterized by social discussion that follows them. This
precedence pattern – confirmed across a dataset spanning
17,000 assets and 14,499 channels – is the observable foot-
print of a manipulation phase that requires public amplifica-
tion to secure exit liquidity before organic participants can
react.
Takeaway:(i) Pump-and-dump activity spans many non-
crypto Telegram communities, consistent with the Crypto’s
Everywhere phenomenon. (ii) Linguistic content does not
distinguish Pump-and-dump events from organic market dis-
cussions. (iii) Coordinated Pump-and-dump events are in-
stead characterized by extreme temporal synchronization of
messages.
Economic Impact Analysis
Finally, to measure the market dynamics of the detected
cases, we quantify each validated event’s financial footprint
in USD-equivalent terms using high-frequency minute-level
price (open, high, low, close) and volume data. For this anal-
ysis, we restrict the sample to deduplicated events for which
at least one USD-pegged or convertible trading pair was
available across the observation window. V olume figures are
aggregated across all (exchange, trading pair) combinations
confirmed by the RDD–DiD step, using time-weighted aver-
age price (TW AP) conversions for non-USD-quoted assets.
Price metrics are drawn from the most liquid USD-pegged
pair per event. Table 3 summarizes the resulting statistics.
The volume figures reveal a pattern consistent with the
structural differences identified in the temporal analysis.
SMR events are associated with substantially higher aggre-
gate volume ($828.8 million) than P&D events ($234.8 mil-
lion). This disparity, however, reflects the nature of the assets
involved rather than the intensity of the anomaly: organic
market reactions tend to cluster around higher-liquidity
coins with established trading depth, whereas P&D schemes
systematically target low-capitalization assets where coordi-
nated buy pressure can move prices with far smaller capital.
Cat. V ol. (USD)∆P + (%)∆P − (%) ¯tpump ¯tdump N
P&D $234.8 Mi+9.98−14.8414.6 32.1 47
SMR $828.8 Mi+18.56−5.36— — 73
Table 3: Economic impact summary.∆P +: average maxi-
mum price increase from T 0 to the price peak.∆P −: aver-
age price loss for traders entering at the peak and holding to
the close (upper-bound loss estimate). ¯tpump and ¯tdump: mean
duration of the pump and dump phases (minutes), respec-
tively. All values pegged to USD.
The most diagnostically significant metrics are the asym-
metric price dynamics. P&D events exhibit a mean maxi-
mum price increase of 9.98% fromT 0 to the price peak, a
gain that is entirely reversed and then exceeded by a mean
maximum drawdown of−14.84%for participants who en-
tered at the peak. This sign reversal constitutes the defining
economic harm of the scheme: the coordination mechanism
artificially sustains a price level long enough to attract ex-
ternal buyers, who then absorb the losses when early partic-
ipants exit. In contrast, SMR events show a higher average
price gain (18.56%) that decays into a modest drawdown of
only−5.36%, consistent with a market processing new in-
formation and converging to a new equilibrium rather than
collapsing back below the pre-event baseline.
The temporal structure of P&D events further corrobo-
rates this interpretation. The mean pump phase (14.6min-
utes) is less than half the mean dump phase (32.1 minutes),
producing a Pump-to-Dump ratio below 0.5. This asymme-
try captures the mechanics of the scheme: the pump is exe-
cuted rapidly through coordinated social signals, maximiz-
ing the speed of price inflation before organic participants
can react, while the dump unfolds more gradually as early
sellers unwind positions against declining liquidity. The ex-
tended dump phase is also consistent with the lingering tail
of post-peak social activity identified in the temporal latency
analysis, where the positive skewness of P&D message dis-
tributions reflects the residual shilling and panic-selling that
characterize the scheme’s secondary phase.
Together, these metrics provide economic validation of
our framework’s categorical separation. P&D events are not
simply more volatile than SMR events, they exhibit a struc-
turally distinct pattern of rapid, artificial price inflation fol-
lowed by a collapse that systematically transfers value from
late buyers to early sellers, precisely as predicted by market
microstructure theory.
Takeaway:Pump-and-dump events target low-liquidity
assets and generate rapid, artificial price inflation (averag-
ing a 9.98% coordinated gain) followed by a collapse that
exposes peak buyers to losses exceeding 14.84%. The pump
phase completes in under 15 minutes on average, while the
dump unfolds over twice as long, consistent with sequential
exit by coordinated early sellers against diminishing organic
liquidity.
Conclusion and Future Works
In this study, we presented a multi-layered framework
for identifying and characterizing market anomalies me-
diated by social media, specifically focusing on the Tele-

gram ecosystem. By integrating NLP-based semantic filter-
ing (RoBERTa), statistical burst detection (CA-CFAR), and
rigorous econometric validation (RDD-DiD), we identified
47 candidatePump-and-dumpevents and 73 Sustained Mar-
ket Reactions from a dataset spanning 17,000 assets. Our re-
sults reveal a critical finding: while manipulators employ se-
mantic mimicry that renders their messages linguistically in-
distinguishable from organic discourse, they are betrayed by
a distinct temporal signature, coordinated social activity that
systematicallyprecedesprice peaks by a median of 4.3 min-
utes, whereas organic market reactions follow price peaks
by a median of 14.5 minutes. This directional asymmetry,
confirmed by a Kolmogorov-Smirnov test (p= 0.0006),
provides content-independent evidence consistent with so-
cial signs leading price changes in manipulation events, and
price changes leading social discussion in organic events.
Economically,Pump-and-dumpevents target low-liquidity
assets and generate rapid artificial inflation – averaging a
9.98% coordinated gain fromT0 to the price peak – followed
by a collapse that exposes peak buyers to losses exceeding
14.84%, nearly three times the 5.36% drawdown observed in
organic Sustained Market Reactions. This asymmetric harm
profile, where the pump benefits early coordinated sellers at
the direct expense of late buyers, points to a systemic risk to
market fairness in decentralized cryptocurrency markets.
This research bridges a gap in the literature by extending
the detection ofPump-and-dumpschemes beyond special-
ized echo chambers into a broader social ecosystem. By im-
plementing a classification layer that resolves semantic pol-
ysemy in cryptocurrency identifiers, our work accounts for
theCrypto’s Everywherephenomenon, where manipulative
signals diffuse across diverse social spheres, from crypto
channels to news and entertainment communities. Unlike
prior studies restricted to known predatory groups, our ap-
proach combines econometric validation with temporal pro-
filing to identify coordinated anomalies amidst general-
purpose social discourse, while also distinguishing deliber-
atePump-and-dumporchestrations from sustained market
reactions to emerging trends.
As for future work, we intend to explore coordination pat-
terns more deeply, analyzing the network topology of cross-
channel synchronization and the role of automated accounts
in amplifying signals. We also plan to extend our analysis
to public Telegram groups beyond the channels considered
in this study, broadening the scope of observable coordina-
tion signals. A major objective is the construction of a com-
prehensive, multimodal ground-truth dataset forPump-and-
dumpoccurrences, fusing verified social media commands
with high-frequency order book data to provide the research
community with a benchmark for training more resilient de-
tection models.
Limitations
While our multi-modal framework demonstrates robust de-
tection capabilities, we acknowledge certain scope bound-
aries. First, our primary data source consists of Telegram
public channels, which utilize a broadcast communication
model. While it is highly likely that the initial orchestration
of these schemes occurs within closed private groups/chan-
nels, the intrinsic mechanics of a pump-and-dump scheme
necessitate public exposure to secure exit liquidity. There-
fore, while planning may be private, the execution may gen-
erate a massive footprint in public channels. The CA-CFAR
algorithm is particularly well-suited to capture these high-
intensity signal injections.
Second, the RDD-DiD framework is inherently reactive,
identifying anomalies after the initial social signal. How-
ever, our temporal analysis demonstrates that manipulative
bursts precede price movements by mere seconds, suggest-
ing that even reactive detection can inform near-real-time
monitoring systems. The reliance on stablecoins and Bit-
coin control groups to filter systemic noise is robust under
normal conditions; during extreme market-wide volatility,
correlation shifts may introduce bias, which we mitigate by
excluding dates with documented systemic shocks. Finally,
the semantic mimicry identified in this work poses an on-
going challenge. As manipulators evolve, they may adjust
their temporal patterns to evade detection. This underscores
the need for continuous model adaptation and motivates our
future work on multimodal ground-truth datasets that can
capture evolving manipulation strategies.
References
Alipanahloo, Z.; Hafid, A. S.; and Z, K. 2024. Maximum
extractable value (mev) mitigation approaches in ethereum
and layer-2 chains: A comprehensive survey.IEEE Access.
Amirzadeh, R.; Nazari, A.; Thiruvady, D.; and Ee, M. S.
2023. Modelling Determinants of Cryptocurrency Prices:
A Bayesian Network Approach. arXiv:2303.16148.
Anderson, D. 2024.Riding the Crypto MemeCoins Wave:
The Unstoppable Surge of Meme Coins in Crypto Trends.
Estalontech.
Bai, S.; Chen, K.; Liu, X.; Wang, J.; Ge, W.; Song, S.; Dang,
K.; Wang, P.; Wang, S.; Tang, J.; et al. 2025. Qwen2. 5-vl
technical report.arXiv preprint arXiv:2502.13923.
Bartoletti, M.; Carta, S.; Cimoli, T.; and Saia, R. 2020. Dis-
secting Ponzi schemes on Ethereum: identification, analysis,
and impact.Future Generation Computer Systems.
Bellutta, D.; and Carley, K. M. 2023. Investigating coor-
dinated account creation using burst detection and network
analysis.Journal of Big Data, 10(1): 20.
Boukhers, Z.; Bouabdallah, A.; Yang, C.; and J ¨urjens, J.
2023. Beyond Trading Data: The Hidden Influence of Pub-
lic Awareness and Interest on Cryptocurrency V olatility. In
Proc. CIKM ’23.
Bucher, M. J. J.; and Martini, M. 2024. Fine-tuned small
LLMs (still) significantly outperform zero-shot generative
AI models in text classification.arXiv:2406.08660.
Chen, H.; and Cai, W. 2023. How information manipulation
on social media influences the NFT investors’ behavior: A
case study of goblintown.wtf.IEEE Trans.Comput.Soc.Syst.
Clough, J.; and Edwards, M. 2023. Pump, Dump, and then
What? The Long-Term Impact of Cryptocurrency Pump-
and-Dump Schemes. InProc. APWG eCrime.
Cong, L. W.; Li, X.; Tang, K.; and Yang, Y . 2023. Crypto
wash trading.Management Science, 69(11): 6427–6454.

Cui, W.; and Gao, C. 2023. WTEYE: On-chain wash trade
detection and quantification for ERC20 cryptocurrencies.
Blockchain: Research and Applications, 4(1): 100108.
Cunha, W.; Rocha, L.; and Gonc ¸alves, M. A. 2025.
A thorough benchmark of automatic text classification:
From traditional approaches to large language models.
arXiv:2504.01930.
Dhawan, A.; and Putnin ¸ˇs, T. J. 2022. A New Wolf in Town?
Pump-and-Dump Manipulation in Cryptocurrency Markets.
Review of Finance, 27(3): 935–975.
Fantazzini, D.; and Xiao, Y . 2023. Detecting Pump-
and-Dumps with Crypto-Assets: Dealing with Imbalanced
Datasets and Insiders’ Anticipated Purchases.Economet-
rics, 11(3): 22.
FORCE11. 2020. The FAIR Data principles.
Gebru, T.; Morgenstern, J.; et al. 2021. Datasheets for
Datasets.Communications of the ACM, 64(12): 86–92.
Gemma Team; Mesnard, T.; Hardin, C.; et al. 2024. Gemma:
Open Models Based on Gemini Research and Technology.
arXiv:2403.08295.
Grattafiori, A.; Dubey, A.; Jauhri, A.; et al. 2024. The Llama
3 Herd of Models. arXiv:2407.21783.
Hu, S.; Zhang, Z.; Lu, S.; He, B.; and Li, Z. 2023. Sequence-
Based Target Coin Prediction for Cryptocurrency Pump-
and-Dump.Proc. ACM Manag. Data, 1(1).
Krishnan, L. P.; Vakilinia, I.; Reddivari, S.; and Ahuja, S.
2024. Analyzing Cryptocurrency Social Media for Price
Forecasting and Scam Detection. InProc. ISDFS 2024, 1–6.
La Morgia, M.; Mei, A.; and Mongardini, A. M. 2025.
TGDataset: Collecting and Exploring the Largest Telegram
Channels Dataset. InProc. SIGKDD ’25, 2325–2334.
La Morgia, M.; Mei, A.; Mongardini, A. M.; and Wu, J.
2023a. It’s a Trap! Detection and Analysis of Fake Chan-
nels on Telegram. InProc. IEEE ICWS.
La Morgia, M.; Mei, A.; Sassi, F.; and Stefa, J. 2020. Pump
and Dumps in the Bitcoin Era: Real Time Detection of Cryp-
tocurrency Market Manipulations. InProc. IEEE ICCCN.
La Morgia, M.; Mei, A.; Sassi, F.; and Stefa, J. 2023b. The
Doge of Wall Street: Analysis and Detection of Pump and
Dump Cryptocurrency Manipulations.ACM Trans. Internet
Technol., 23(1).
Lee, D. S.; and Lemieux, T. 2010. Regression discontinuity
designs in economics.J. Econ. Lit., 48(2): 281–355.
Liang, R.; Chen, J.; et al. 2025. Towards effective detection
of ponzi schemes on ethereum with contract runtime behav-
ior graph.ACM Trans. Softw. Eng. Methodol., 34(4): 1–32.
Liu, Y .; Ott, M.; Goyal, N.; et al. 2019. RoBERTa:
A Robustly Optimized BERT Pretraining Approach.
arXiv:1907.11692.
Malkiel, B. G. 1989. Efficient market hypothesis. InFi-
nance, 127–134. Springer.
McHugh, M. L. 2012. Interrater reliability: the kappa statis-
tic.Biochemia medica, 22(3): 276–282.
Mezquita, Y .; Gil-Gonz´alez, A. B.; Prieto, J.; and Corchado,
J. M. 2022. Cryptocurrencies and Price Prediction: A Sur-
vey. InBlockchain and Applications.
Mirtaheri, M.; Abu-El-Haija, S.; Morstatter, F.; et al. 2021.
Identifying and Analyzing Cryptocurrency Manipulations in
Social Media.IEEE Trans.Comput.Soc.Syst., 8(3): 607–617.
Mohammadinodooshan, A.; and Carlsson, N. 2025. Suc-
cessful Rhetorics: How Do Linguistic Dimensions Affect
User Engagement with Different News Categories on Twit-
ter? InProc. AAAI ICWSM.
Nghiem, H.; Muric, G.; Morstatter, F.; and Ferrara, E.
2021. Detecting cryptocurrency pump-and-dump frauds us-
ing market and social signals.Expert Syst. Appl.
Niu, Y .; Li, X.; Peng, H.; and Li, W. 2024. Unveiling wash
trading in popular NFT markets. InProc. Companion ACM
Web Conf., 730–733.
Nizzoli, L.; Tardelli, S.; Avvenuti, M.; Cresci, S.; Tesconi,
M.; and Ferrara, E. 2020. Charting the Landscape of Online
Cryptocurrency Manipulation.IEEE Access.
Paoletti, G.; Ferreira, C. H. G.; Vassio, L.; Rocha, L.; and
Almeida, J. M. 2025. Tracing the 2024 U.S. Election De-
bate on Telegram with LLMs and Graph Analysis.Social
Network Analysis and Mining, 15(1): 91.
Perlo, A.; Paoletti, G.; Jha, N.; et al. 2025. Topic-wise Ex-
ploration of the Telegram Group-verse. InProc. Companion
ACM Web Conf., 1792–1801.
Richards, M. A.; Scheer, J. A.; and Holm, W. A. 2010.Prin-
ciples of modern radar: basic principles. IET.
Roy, S. S.; Vafa, E. P.; Khanmohamaddi, K.; and Nilizadeh,
S. 2024. DarkGram: A Large-Scale Analysis of Cybercrim-
inal Activity Channels on Telegram.Stud. Health Technol.
Inform., 310: 981–985.
Sifat, I.; Tariq, S. A.; and van Donselaar, D. 2024. Suspi-
cious trading in nonfungible tokens (NFTs).Information &
Management, 61(1): 103898.
Tian, Y .; and Xie, Y . 2024. Artificial cheerleading in IEO:
Marketing campaign or pump and dump scheme.Informa-
tion Processing & Management, 61(1): 103537.
Trinh, Q. M.; Zarin, S.; and Rezapour, R. 2025. Master
of Deceit: Comparative Analysis of Human and Machine-
Generated Deceptive Text. InProc. ACM WebSci 2025,
189–198.
Trochim, W. M. 1990. The regression-discontinuity design.
Res. Methodol.: Strength. Causal Interpret. Nonexp. Data,
119–139.
Van Tran, Q.; and Kukal, J. 2022. A novel heavy tail distri-
bution of logarithmic returns of cryptocurrencies.Finance
Research Letters, 47: 102574.
Victor, F.; and Hagemann, T. 2019. Cryptocurrency Pump
and Dump Schemes: Quantification and Detection. InInter-
national Conference on Data Mining Workshops.
Wu, C.; Chen, J.; L., J.; Xu, J.; J., J.; Hu, Y .; Feng, Y .; Liu, Y .;
and Xiang, Y . 2025. Profit or Deceit? Mitigating Pump and
Dump in DeFi via Graph and Contrastive Learning.IEEE
Transactions on Information Forensics and Security.
Xu, J.; and Livshits, B. 2019. The anatomy of a cryptocur-
rency pump-and-dump scheme. InProceedings of the 28th
USENIX Conference on Security Symposium, 1609–1625.

Paper Checklist
1. For most authors...
(a) Would answering this research question advance sci-
ence without violating social contracts, such as violat-
ing privacy norms, perpetuating unfair profiling, exac-
erbating the socio-economic divide, or implying disre-
spect to societies or cultures? Yes
(b) Do your main claims in the abstract and introduction
accurately reflect the paper’s contributions and scope?
Yes
(c) Do you clarify how the proposed methodological ap-
proach is appropriate for the claims made? Yes
(d) Do you clarify what are possible artifacts in the data
used, given population-specific distributions? NA
(e) Did you describe the limitations of your work? Yes,
see section Limitation.
(f) Did you discuss any potential negative societal im-
pacts of your work? NA
(g) Did you discuss any potential misuse of your work?
NA
(h) Did you describe steps taken to prevent or mitigate po-
tential negative outcomes of the research, such as data
and model documentation, data anonymization, re-
sponsible release, access control, and the reproducibil-
ity of findings? NA
(i) Have you read the ethics review guidelines and en-
sured that your paper conforms to them? Yes
2. Additionally, if your study involves hypotheses testing...
(a) Did you clearly state the assumptions underlying all
theoretical results? Yes
(b) Have you provided justifications for all theoretical re-
sults? Yes
(c) Did you discuss competing hypotheses or theories that
might challenge or complement your theoretical re-
sults? NA
(d) Have you considered alternative mechanisms or expla-
nations that might account for the same outcomes ob-
served in your study? Yes. We account for alternative
explanations including market-wide shocks and or-
ganic information diffusion by using RDD combined
with DiD and stablecoin controls, and we interpret our
findings as correlational rather than strictly causal.
(e) Did you address potential biases or limitations in your
theoretical framework? Yes
(f) Have you related your theoretical results to the existing
literature in social science? NA
(g) Did you discuss the implications of your theoretical
results for policy, practice, or further research in the
social science domain? Yes
3. Additionally, if you are including theoretical proofs...
(a) Did you state the full set of assumptions of all theoret-
ical results? NA
(b) Did you include complete proofs of all theoretical re-
sults? NA
4. Additionally, if you ran machine learning experiments...
(a) Did you include the code, data, and instructions
needed to reproduce the main experimental results (ei-
ther in the supplemental material or as a URL)? Yes.
We will release a public GitHub repository containing
the full experimental code and detailed instructions to
reproduce the main results, along with the cryptocur-
rency dictionary collected in this study. The Telegram
data used in our analysis are already publicly avail-
able, and the repository will document how to access
and preprocess them.
(b) Did you specify all the training details (e.g., data splits,
hyperparameters, how they were chosen)? Yes
(c) Did you report error bars (e.g., with respect to the ran-
dom seed after running experiments multiple times)?
NA
(d) Did you include the total amount of compute and the
type of resources used (e.g., type of GPUs, internal
cluster, or cloud provider)? No
(e) Do you justify how the proposed evaluation is suffi-
cient and appropriate to the claims made? Yes
(f) Do you discuss what is “the cost“ of misclassification
and fault (in)tolerance? NA
5. Additionally, if you are using existing assets (e.g., code,
data, models) or curating/releasing new assets,without
compromising anonymity...
(a) If your work uses existing assets, did you cite the cre-
ators? Yes
(b) Did you mention the license of the assets? NA
(c) Did you include any new assets in the supplemental
material or as a URL? No
(d) Did you discuss whether and how consent was ob-
tained from people whose data you’re using/curating?
Yes. This study relies exclusively on an existing pub-
lic dataset from the literature, consisting of messages
collected from Telegram public channels. The dataset
was originally gathered via the Telegram API and in-
cludes only content that is openly accessible by design,
where users have no reasonable expectation of privacy.
Following established ethical guidelines for computa-
tional social science research, individual consent was
not sought, as the data are public, non-interactive, and
analyzed in aggregate form.
(e) Did you discuss whether the data you are using/curat-
ing contains personally identifiable information or of-
fensive content? Yes. The data consist of public Tele-
gram channel content and may include user-generated
material, but we do not curate the dataset nor analyze
personally identifiable information, focusing only on
aggregated signals.
(f) If you are curating or releasing new datasets, did you
discuss how you intend to make your datasets FAIR
(see FORCE11 (2020))? NA
(g) If you are curating or releasing new datasets, did you
create a Datasheet for the Dataset (see Gebru, Morgen-
stern et al. (2021))? NA

6. Additionally, if you used crowdsourcing or conducted
research with human subjects,without compromising
anonymity...
(a) Did you include the full text of instructions given to
participants and screenshots? NA
(b) Did you describe any potential participant risks, with
mentions of Institutional Review Board (IRB) ap-
provals? NA
(c) Did you include the estimated hourly wage paid to
participants and the total amount spent on participant
compensation? NA
(d) Did you discuss how data is stored, shared, and dei-
dentified? NA
Ethical Considerations
This study relies exclusively on observational data and does
not involve any interaction or intervention with human sub-
jects. All Telegram data analyzed originate from publicly ac-
cessible Telegram channels and were collected from an ex-
isting dataset released by prior work. The authors did not ac-
cess private groups, bypass platform restrictions, or engage
with users in any form.
We adopt a strict de-identification approach and do not at-
tempt to identify, track, or profile individual users, adminis-
trators, or coordinated actors. All analyses are performed at
the aggregate level (messages, channels, and events), and no
personally identifiable information is collected or inferred.
Market data (prices and transaction volumes) are obtained
from public sources through official APIs and collected in
accordance with their documented usage policies.
While we identify patterns consistent with potential
pump-and-dump activity, our findings are descriptive and
focused on characterizing market anomalies. They do not
constitute legal evidence of intent or wrongdoing by specific
individuals, but rather serve to highlight the systemic risks
that coordinated social media activity poses to the fairness
of decentralized financial markets.
Appendix A - Language Models
This section describes the Hyperparameters used in the eval-
uated models, the prompt templates used during ICL infer-
ences, and the generalization/robustness validation experi-
ment
Hyperparameters:To identify the optimal configuration
for our classification models, we conducted an extensive
hyperparameter search (Grid-Search) using a Bayesian op-
timization approach (Optuna). The search space was de-
signed to balance model stability with domain adapta-
tion, exploring the following ranges: learning rate∈ {1×
10−5,2×10 −5,3×10 −5,5×10 −5}, training epochs
∈ {2,3,4}, weight decay∈ {0.0,0.01,0.1}, and dropout rate
∈{0.1,0.2,0.3}. All trials were evaluated using the validation
split of our ground-truth dataset.
TheRoBERTa-basemodel, which was subsequently
selected as our primary classifier, achieved its peak perfor-
mance (Objective Score: 0.9429) with the following opti-
mized hyperparameters: a learning rate of 3×10-5, 4 training
Model ZS ICL Z ICL F FT
gemma-7b≈53k≈65k≈116k 69.47 (554.26±44.03)
llama3.1-8B≈55k≈67k≈125k 63.63 (503.36±34.11)
qwen2.5-8B≈47k≈56k≈100k 87.79 (831.27±35.49)
roberta – – – 4.78 (89.14±8.40)
Table 4:Average inference time (ms) per message across strate-
gies. FT column includes fine-tuning time (mean±95% CI).
epochs, a weight decay of 0.01, and a dropout rate of 0.1.
These settings ensured the best trade-off between capturing
specialized cryptocurrency jargon and maintaining general-
isation across different Telegram channel styles, effectively
mitigating the risk of overfitting during the fine-tuning pro-
cess.
Beyond classification effectiveness, we also assess the
computational implications of the selected hyperparameter
configuration. Table 4 summarizes the average inference
time per message across models and training strategies, con-
textualizing the scalability of the proposed approach.
Prompt Templates:We here present the prompts used
for Zero-Shot Classification, Zero-Shot In-Context Learning
(ICL), and Few-Shot In-Context Learning (ICL). The Zero-
Shot Classification prompt is nearly identical to the Zero-
Shot ICL prompt, except that it does not include the con-
textual guideline describing the criteria for a message to be
considered crypto-related.
Zero-Shot In-Context Learning
You are an expert in analyzing Telegram cryptocur-
rency communication.
Classify the message strictly as:
1 = Crypto-related
0 = Not crypto-related
A message is crypto-related if it mentions:
- Cryptocurrencies (Bitcoin, Ethereum, altcoins, to-
kens)
- NFTs, blockchain, Web3, DeFi, exchanges, wallets,
mining, staking, airdrops
- Crypto trading, investing, tokens, presales, jargons or
memecoins
Even a brief or indirect mention is sufficient.
Message:
{message}
Answer only with 0 or 1:
Few-Shot In-Context Learning (5examples)
You are an expert in cryptocurrency communication
analysis.
Classify the message strictly as:

1 = Crypto-related
0 = Not crypto-related
Here are some examples:
Message:{message}
Label:{label}
Now classify the next message:
Message:{message}
Answer only with 0 or 1:
Robustness and Generalization:To further validate the
temporal robustness and generalization capabilities of our
fine-tuned RoBERTa model, we conducted a longitudinal
annotation experiment. We extracted a temporally stratified
sample of 520 messages spanning the 13 months of our anal-
ysis dataset (40 messages per month, equally balanced be-
tween predicted positive and negative classes). Three inde-
pendent annotators, strictly blinded to the model’s predic-
tions, manually classified these samples following our origi-
nal labeling codebook. To evaluate the reliability of this new
ground truth, we computed both Fleiss’ Kappa and Krip-
pendorff’s Alpha. As shown in Figure 7 (left), both metrics
yielded nearly identical values and consistently exceeded
the substantial agreement threshold (0.6) across all months.
This minimal divergence and high sustained value confirm
a strong, reliable consensus among the human annotators
over time. Furthermore, when evaluated on this longitudi-
nally re-annotated data, the model demonstrated remark-
able temporal stability. As illustrated in Figure 7 (right), the
monthly Macro-F1 scores remain consistent across the en-
tire observation period for both the crypto-related and non-
crypto classes, remaining consistent with the performance
observed on the held-out test set. These results empirically
demonstrate that our semantic filter does not suffer from
temporal degradation, ensuring robust and generalized de-
tection across the entire observation period of this study.
Appendix B - CA-CFar Sensibility Analysis
To calibrate the CA-CFAR algorithm, we performed a sen-
sitivity analysis on two critical parameters: Guard Cells
and Training Cells. To establish a reference for this tun-
ing, we utilized a subset of verifiedPump-and-dump(P&D)
events annotated by La Morgia et al. (2020). Although
this external dataset lacks the original message content, we
successfully cross-referenced two major channels—Whales
Crypto Guide(WCG) andCoach(formerlyCrypto coin
B) – to our repository. After filtering for temporal consis-
tency, we isolated 16 confirmed P&D events from the WCG
channel (2018–2020) to serve as a validation ground-truth.
While these events precede our primary analysis window
(2021–2022), they provide the necessary structural patterns
of social bursts required for parameter optimization.
We tested a range of values for both parameters:
{1,2,3,5,7,15,30}days. The Guard Cells define the period
immediately surrounding the analysis day that must be ig-
nored to prevent the signal burst from corrupting the base-
line, while the Training Cells establish the historical window
used to calculate the noise floor. Our analysis revealed that a
configuration of 1 Guard Cell and 5 Training Cells achieved
the highest sensitivity, successfully detecting 15 out of 16
ground-truth events.
The preference for these specific values is driven by the
intrinsic nature of social media manipulation. We observed
that increasing the Guard Cell window led to a significant
drop in detection rates; this is likely because the highly
concentrated, short-lived nature of social bursts is absorbed
or “smoothed over” by excessively long exclusion zones,
which fail to isolate the localized discontinuity of a pump
signal. Similarly, a 5-day Training Cell window provided the
optimal balance for the noise floor, long enough to establish
a stable baseline of organic discussion, yet short enough to
remain responsive to the rapid shifts in cryptocurrency so-
cial trends. This configuration ensures that the algorithm re-
mains highly sensitive to sudden, synchronized bursts while
filtering out systemic background noise.
Appendix C - Causality Methods Evaluation
While this study primarily relies on the synergy between
Regression Discontinuity Design (RDD) and Difference-in-
Differences (DiD), we also explored Interrupted Time Se-
ries (ITS) and Convergent Cross Mapping (CCM). This
appendix details their mechanics and justifies why RDD
and DiD remain the superior choices for detecting high-
frequency market manipulations. Finally, we demonstrate
the threshold sensitivity duringPump-and-dumpand Sus-
tained Market Reaction classifications during the RDD +
DiD framework.
Interrupted Time Series - ITSITS is a quasi-
experimental design that models a series of observations
over time, interrupted by a specific event. Unlike RDD,
which focuses on the instantaneous “jump” at the thresh-
old, ITS is designed to evaluate the slope change and long-
term trends before and after an intervention. It is ideal for
capturing the “persistence” of a shock. It excels at identi-
fying if a market reaction has “long-memory” properties or
if the intervention caused a permanent shift in the baseline
trading volume. The primary weakness of ITS in thePump-
and-dumpcontext is its reliance on a stable pre-intervention
trend. Cryptocurrency markets are notoriously volatile; a
120-minute window often contains secondary shocks that
contaminate the slope estimation. While ITS provides a
good view of V olume Decay, it lacks the “local precision”
of RDD, which is less sensitive to distant noise within the
time series.
Convergent Cross Mapping (CCM)CCM is a non-linear
state-space method used to detect causal coupling in com-
plex systems. It reconstructs the shadow manifolds (attrac-
tors) of two variables (e.g., Telegram message volume and
Price returns) to see if information from one is embedded in
the other. Unlike Granger Causality, CCM can detect “pre-
event leakage” or “insider trading” where social media ac-
tivity forces price movements in a non-linear, coupled fash-

2021-072021-082021-092021-102021-112021-122022-012022-022022-032022-042022-052022-062022-07
Month
0.0
0.2
0.4
0.6
0.8
1.0Agreement coefficient
Inter-annotator agreement over time
Fleiss' kappa
Krippendorff's alpha
Substantial threshold (0.6)
2021-072021-082021-092021-102021-112021-122022-012022-022022-032022-042022-052022-062022-07
Month
0.6
0.7
0.8
0.9
1.0F1 Score
T emporal Macro-F1 (re-annotated) vs. held-out test set F1
Macro-F1 (re-annotated)
RoBERT a F1, held-out test set (Non-Crypto)
RoBERT a F1, held-out test set (Crypto-Related)
Figure 7: Annotation agreement evaluation (left) and generalization experiment (right)
ion before the officialT 0. In the case of this study, it pre-
sented the following challenges and limitations: (i) Model
Fitting and Stability: During our implementation, CCM pre-
sented significant fitting problems. Financial time series are
often non-stationary and contain high levels of stochastic
noise, which “shatters” the manifold reconstruction, leading
to poor convergence. (ii) Scalability and Retraining: CCM is
inherently asset-specific. A manifold reconstruction model
must be individually trained and tuned for every single coin
in the dataset. Given the thousands of anomalous events de-
tected across hundreds of different altcoins, a per-coin CCM
approach is computationally prohibitive and less viable for
a generalized detection framework compared to the RDD +
DiD strategy.
Thresold Sensitiviy AnalysisTo empirically validate the
robustness of our classification thresholds, we conducted
a comprehensive sensitivity analysis. We evaluated nine
distinct parameter configurations by varying the Rever-
sal Ratio across0.6,0.7, and0.8, and the V olume Decay
across0.2,0.3, and0.4. The categorization of events re-
mained highly stable across the majority of these combi-
nations, demonstrating that our pipeline is not overly sen-
sitive to minor parameter adjustments. However, we identi-
fied 18 (15%) borderline cases where the event classification
(Pump-and-dumpvs. Sustained Market Reaction) fluctuated
depending on the specific configuration applied. To resolve
these discrepancies, we conducted a rigorous manual qual-
itative inspection of the high-frequency financial time se-
ries for these 18 boundary events. Our analysis revealed that
deviating from the baseline0.7and0.3configuration fre-
quently introduced false positives into both categories. As
presented by Table 5, for instance, alternative values either
misclassified partial-dump manipulations as organic price
discovery or flagged legitimate sustained reactions exhibit-
ing natural trading lulls as artificial dumps. Consequently,
we determined that retaining the0.7/0.3configuration pro-
vides the most accurate and theoretically sound separation.
Selected examples of these manually inspected boundary
cases – such as BICO, BNB, and SUSHI (in two different
exchanges) – are presented in Figure 8 to illustrate how true
sustained reactions can be prematurely flagged as manipu-
lation under suboptimal threshold configurations, and how
Pump-and-dumpcan be missclassified as sustained market
Vol. 0.2 0.3 0.4
Rev. P&D SMR P&D SMR P&D SMR
0.6 3 15 11 7 18 0
0.7 0 18 8 10 15 3
0.8 0 18 13 5 15 3
Table 5: Sensitivity of boundary event classification (n=
18) across threshold configurations.
reactions even with abrupt pre-burst buy orders followed by
differentpumpstages, which were sensitive to the V olume
Decay threshold.
Appendix D - Messages Examples
This section includes examples of messages during abrupt
events (Pump-and-dumpand Sustained Market Reactions).
Pump & Dump Validated Samples
P&D Example 1: Coordination and Historical Returns
#RVN #1 (BTC) [Bittrex]
15 min burst detected
V ol24h: 12.55 (+7.38 BTC) 142.8%
Price Change: +14.81%
Previous events:10 Aug +68.92% (15 min); 06 Aug
+59.45% (15 min).
RVN - Ravencoin (CMC #83)
P&D Example 2: Signal Accuracy and ROE Shilling
4 XBT signals in last 48 hours with 100% Accuracy.
#XBT 1: 140% ROE — #XBT 3: 214% ROE
#BAT: 35% Profit — #CHZ: 151% Profit
Exchanges: Binance.
P&D Example 3: Influencer-Led Urgency (FOMO)
DOGE COIN HEADING SKYROCKET. Elon Musk
Promoted this Early Morning. Invest and Earn a Big
stack. Move your btc to DOGE. Buy and Sell using
[URL].

5.5
6.0
6.5
7.0
7.5
8.0Price
BICO | 2021-12-09
REVERSAL=0.000   VOL_DECAY=0.322
P&D in 3/9 configs   |   Best fit: SMR
Dec. 09. 00:30Dec. 09. 01:00Dec. 09. 01:30Dec. 09. 02:00Dec. 09. 02:30Dec. 09. 03:00Dec. 09. 03:30
0
200000Volume
(a) BICO (2021-12-09)
195
200
205
210
215
220Price
BNB | 2021-02-19
REVERSAL=0.078   VOL_DECAY=0.315
P&D in 3/9 configs   |   Best fit: SMR
Feb. 18. 23:00Feb. 18. 23:30Feb. 19. 00:00Feb. 19. 00:30Feb. 19. 01:00Feb. 19. 01:30Feb. 19. 02:00
0
2Volume
(b) BNB (2021-02-19)
1.07
1.08
1.09
1.10
1.11Price
SUSHI | 2022-06-20
REVERSAL=0.000   VOL_DECAY=0.233
P&D in 6/9 configs   |   Best fit: P&D
Jun. 20. 09:30Jun. 20. 10:00Jun. 20. 10:30Jun. 20. 11:00Jun. 20. 11:30Jun. 20. 12:00Jun. 20. 12:30
0
250Volume
(c) SUSHI (2022-06-20)
1.01
1.02
1.03
1.04
1.05Price
SUSHI | 2022-06-20
REVERSAL=0.788   VOL_DECAY=0.527
P&D in 6/9 configs   |   Best fit: P&D
Jun. 20. 09:30Jun. 20. 10:00Jun. 20. 10:30Jun. 20. 11:00Jun. 20. 11:30Jun. 20. 12:00Jun. 20. 12:30
0
10000Volume
(d) SUSHI (2022-06-20) in another ex-
change
Figure 8: Manual inspection of borderline cases.$BICOand
$BNBare SMR events misclassified asPump-and-dumpun-
der some threshold settings, due to transient corrections or
temporary volume drops. The$SUSHIpanels show staged
P&D patterns across two exchanges, where the dump phase
appears as discrete bursts rather than a single decline.
Sustained Market Reaction Samples
Market Reaction 1: Infrastructure and Rebranding
First it was Binance chain, then Binance smart chain
and now itsBNB(Build & Build)chain. Official Sup-
port Link: [URL]
Market Reaction 2: Whale Activity and Liquidity Flows
12,499,999 #XLM (2,722,654 USD) transferred from
unknown wallet to #Coinbase. [Details on Whale Alert].
Market Reaction 3: Organic Community Speculation
Maybe if we are lucky we can convince Elon Musk to
send all of us to another universe on his rocket with all
of the Dogecoin so that we can escape this insanity.
