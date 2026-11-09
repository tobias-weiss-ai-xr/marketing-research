---
title: Can LLMs Help Decentralized Dispute Arbitration? A Case Study of UMA-Resolved Markets on Polymarket
url: https://arxiv.org/abs/2604.15674
category: digital-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Junhao Wen
- Juncen Zhou
- Junjie Huang
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.15674
pages: 4
chars: 24840
fetched_at: '2026-11-08T13:01:31+00:00'
kb_version: 1
---

# Can LLMs Help Decentralized Dispute Arbitration? A Case Study of UMA-Resolved Markets on Polymarket

Can LLMs Help Decentralized Dispute Arbitration?
A Case Study of UMA-Resolved Markets on Polymarket
Junhao Wen
Southwest University
Chongqing, China
wen264132454@email.swu.edu.cn
Juncen Zhou
University of Sydney
Sydney, Australia
zhou_2002510@163.com
Junjie Huang∗
Southwest University
Chongqing, China
junjiehuang@swu.edu.cn
Abstract
Web3 prediction markets, exemplified by Polymarket, have gained
prominence for leveraging collective intelligence to forecast a wide
range of social, political, and sports events. However, among the
thousands of prediction market events, consensus disputes still
arise due to imperfections in market mechanisms. On Polymarket
alone, the trading volume involving disputed events has reached
$972,370,804.71, underscoring the critical need for objective and effi-
cient dispute resolution. In this study, we introduce large language
models (LLMs) to: (1) evaluate whether web-enabled LLMs can
reproduce the decision quality of UMA’s on-chain voting process
once a dispute has been raised, and (2) predict, based on event rules,
which market events are likely to face future disputes before they
occur. Our findings show that LLMs are unable to reliably predict
which events will become disputed in advance; however, once a
dispute is initiated, web-enabled LLMs achieve 89.58% agreement
with UMA’s final resolutions and demonstrate strong stability.
CCS Concepts
•Information systems → Collaborative and social computing
systems and tools;Web mining.
Keywords
Web3, Prediction Market, Large Language Models
ACM Reference Format:
Junhao Wen, Juncen Zhou, and Junjie Huang. 2018. Can LLMs Help Decen-
tralized Dispute Arbitration? A Case Study of UMA-Resolved Markets on
Polymarket. InProceedings of Make sure to enter the correct conference title
from your rights confirmation email (Conference acronym ’XX).ACM, New
York, NY, USA, 4 pages. https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
Decentralized prediction markets have emerged as one of the most
prominent applications of Web3, offering a mechanism for aggregat-
ing collective intelligence to forecast real-world events. Platforms
such as Polymarket allow users to trade on outcomes across political,
∗Junjie Huang is the Corresponding author.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
Conference acronym ’XX, Woodstock, NY
©2018 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-XXXX-X/2018/06
https://doi.org/XXXXXXX.XXXXXXX
economic, and sports domains, with market prices reflecting collec-
tive expectations grounded in publicly available information [16].
Despite their scalability and transparency, these systems remain
vulnerable to disputes (i.e., disagreements over event outcomes
raised by users or resolvers) caused by ambiguous event wording, in-
consistent external reporting, or evolving real-world developments.
To address such disagreements, Polymarket relies onUMA’s Op-
timistic Oracle (OO)1, which escalates contested outcomes to a
decentralized token-holder vote. While effective in many cases, this
governance process has faced criticism for potential subjectivity, co-
ordination challenges, and susceptibility to interpretive ambiguity.
Our data indicates that disputed markets on Polymarket—whether
current or historical—represent $972,370,804.71 in trading volume,
demonstrating the vital need for an effective resolution mechanism.
In parallel, recent advances [4, 15, 17] in large language models
(LLMs) have demonstrated strong capabilities in retrieving, inter-
preting, and synthesizing real-world information. Their increasing
reliability raises an important question: Can LLMs serve as im-
partial evaluators in decentralized governance systems, either by
predicting which markets are likely to become disputed or by
resolving disputes once they occur? If effective, LLM-based ad-
judication could offer a scalable and transparent complement to
traditional, human-driven oracle mechanisms.
This study offers the first systematic examination of LLMs within
the lifecycle of Web3 prediction-market governance. We investi-
gate two core research questions:RQ1evaluateswhether LLMs
can reproduce UMA’s final decisionsin disputed Polymarket
events using only information available before the UMA vote is
finalized, thereby assessing whether LLMs can effectively substi-
tute for the token-holder voting stage.RQ2examineswhether
LLMs can predict dispute formation in advancebased solely
on the semantic content of event rules. Our results show that al-
though LLMs struggle to anticipate which events will eventually
be disputed, they achieve high pre-vote agreement with UMA’s
final outcomes once a dispute has been raised—achieving 89.58%
for DeepSeek V3.1 and 89.19% for Qwen Max, with Qwen Max fur-
ther demonstrating exceptionally strong internal stability (96.14%).
These findings indicate that while LLMs exhibit limited predic-
tive capability for identifying disputes, they serve as reliable and
consistent evaluators during thepost-disputeresolution phase.
Overall, this work highlights both the promise and the limita-
tions of LLMs in decentralized governance systems. Rather than
replacing existing oracle mechanisms, LLMs may function as con-
sistent, auditable, and efficient assistants in dispute resolution,
helping to enhance transparency and reduce the burdens associated
with human-driven voting processes.
1https://uma.xyz
arXiv:2604.15674v1  [cs.CY]  17 Apr 2026

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Junhao Wen, Juncen Zhou, and Junjie Huang
Figure 1: The Polymarket dispute lifecycle: a proposed
outcome can be challenged via staking, triggering stake-
weighted voting rounds until resolution. We employ LLMs
to predict and resolve thesedisputes.
2 Background
2.1 Polymarket
Polymarket2 is a leading decentralized prediction market platform
that enables users to trade on the outcomes of real-world events
across politics, economics, and culture. It leverages market mecha-
nisms to aggregate public information and quantify collective be-
liefs through prices that reflect event probabilities. Built on polygon
blockchain technology, Polymarket ensures transparency, liquidity,
and censorship resistance, attracting significant trading volumes
and mainstream attention. To securely resolve market outcomes,
it relies onUMA’s Optimistic Oracle (OO)for decentralized and
verifiable truth determination.
2.2 UMA
UMA (short forUniversal Market Access) is a decentralized protocol
deployed on Ethereum and other blockchains. One of its core com-
ponents is theOptimistic Oracle (OO), a mechanism designed to
securely and efficiently bring verifiable real-world data or event
outcomes (e.g.,whether a person won a competition).
TheOOoperates under anassume honesty firstparadigm:
when a participant submits anassertionabout a real-world fact,
they must post a bond as collateral, and the claim then enters a
predeterminedchallenge period. If no one disputes it during this
window, the assertion is considered correct by default and final-
ized automatically. However, if challenged, the claim escalates to a
dispute phase , where UMA’s Data Verification Mechanism (DVM)
based dispute resolution life circle is invoked(see Figure 1). The
DVMrelies on UMA token holders to vote on the correct outcome,
aligning economic incentives to ensure honest and accurate resolu-
tion. This design allows most queries to be resolved efficiently and
inexpensively, while only the small fraction ofdisputedcases in-
voke the more resource-intensive voting process, striking a balance
between decentralization and scalability.
Nevertheless, theOOsystem also carries certain risks and limita-
tions. Its optimistic design relies on rational and well-incentivized
participants; if voting power becomes overly concentrated or if
community engagement is low, outcomes could be influenced by a
small subset of token holders. Moreover, because many event state-
ments are expressed in natural language, ambiguity in question
2https://polymarket.com
phrasing can lead to inconsistent interpretations or contentious
resolutions. These risks have manifested in real-world applications
such as Polymarket.
2.3DisputedExample
A notable example of these risks occurred in the Polymarket event
Will Zelenskyy wear a suit before July?, which drew over $200
million in trading volume. The market asked whether Ukrainian
President Volodymyr Zelenskyy would appear publicly in a “suit”
between May 22 and June 30, 2025. Controversy emerged after he
attended a NATO summit wearing a dark jacket, shirt, and trousers,
which some participants described as a suit while others rejected
because it lacked traditional elements such as a matching set or a
tie. Both “Yes” and “No” outcomes were proposed and disputed,
promptingOOto resolve the question through its voting mecha-
nism. The final decision of “No” triggered backlash [6] from traders
who claimed governance centralization and subjective interpreta-
tion had compromised fairness. UMA’s co-founder, Hart Lambur,
rejected manipulation claims, but the controversy revealed how
even simple, natural-language questions can challenge decentral-
ized truth systems reliant on collective judgment.
These controversies highlight that whileOOrepresents a ground-
breaking innovation in decentralized data verification, challenges
remain in governance, incentive alignment, and the interpretation
of natural-language conditions.
2.4 Related Work
Prediction markets have long been studied as mechanisms for ag-
gregating distributed beliefs, with foundational work on automated
market makers, illustrating how liquidity and incentives shape infor-
mation aggregation [2, 9]. Decentralized variants, such as Polymar-
ket, extend these ideas to trust-minimized environments, relying
on oracle-based governance to finalize outcomes [3, 7]. UMA’s Op-
timistic Oracle represents a prominent design in this space, using
challenge-based verification and token-holder voting to resolve am-
biguous or disputed events [14]. Despite their scalability, existing
oracle systems also face critical limitations. For example, imple-
mentation surveys have shown that trust-minimized oracle designs
cannot fully eliminate integrity and freshness risks, especially when
aggregating data from heterogeneous sources [10].
Concurrently, rapid advances in large language models (LLMs)
have spurred research into autonomous agents and LLMs’ web-
search for decentralized governance [8, 11, 13]. Recent work shows
that web-enabled LLM agents can evaluate DAO proposals and
align with collective voting behavior [1], while self-sovereign LLM
agents demonstrate the feasibility of trust-minimized autonomous
decision-makers in Web3 systems [5]. Complementary studies in AI-
assisted governance anddispute resolution [12, 18] further suggest
that LLMs can perform structured fact interpretation and rule-based
reasoning. These findings collectively indicate that LLM-driven
agents may augment or partially automate governance workflows
in decentralized environments.
In this paper, we present the first attempt to apply large language
models to decentralized dispute arbitration and investigate whether
LLMs can assist in resolving on-chain disputes.

Can LLMs Help Decentralized Dispute Arbitration?
A Case Study of UMA-Resolved Markets on Polymarket Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
31.5%
20.4%
16.7%
11.6%
6.1%
6.1%
3.4%2.3%
Polymarket Disputed Events Category Distribution
Categories
Sports (176)
Politics (114)
Crypto (93)
World (65)
Elections (34)
Culture (34)
Tech (19)
Mentions (13)
Finance (5)
Economy (4)
Earnings (1)
Figure 2: Distribution of Polymarket disputed Events by Cat-
egory. Sports (31.5%), Politics (20.4%), and Crypto (16.7%) are
the three largest categories.
3 Dataset and Data Preprocessing
We retrieved all available event data from Polymarket using the
officialAPI 3 endpoint, iteratively accessing paginated results to
ensure complete coverage of all active and historical markets. The
API was queried three times at regular intervals, and we observed
that each subsequent query returned all previously obtained events
along with newly created ones, indicating that the official endpoint
is stable and consistent4. Each record represents a prediction mar-
ket event with detailed metadata including its identifier, question
content, resolution statuses , market outcomes, prices, and sub-
event grouping information.Using the umaResolutionStatuses ,
we filtered for records containing the keyword disputed, resulting
in a total of 558 user-disputed events.Based on these events, we will
conduct further filtering and analysis in Section 4 and Section 5.
A multi-LLM classification employing three distinct models was
performed on the disputed events. The outcome demonstrated high
classification stability, with457events (81.90%) achieving full consis-
tency (Very Stable) and98events (17.56%) showing large consistency
(Stable), resulting in nearly99 .5%of events exhibiting robust agree-
ment. Only three events (0.54%) were inconsistent (Unstable), which
were subsequently resolved through manual review and assigned to
theMentionscategory (IDs:542935,534923,570937). As depicted
in Figure 2, the distribution of event categories post-classification
reveals a significant concentration of disputed events within the
Sports,Politics, andCryptodomains, collectively accounting for
approximately68 .6%of all disputes. This pronounced asymmetry,
reliably identified via highly stable LLM classification, suggests a
clear direction for subsequent research, primarily focusing on char-
acterizing the unique factors driving disputes specifically within
these three predominant categories.
3https://gamma-api.polymarket.com/markets
4The most recent retrieval was performed on UTC 2025-10-27 11:58:47 , yielding a
total of 140,582 Polymarket events.
Table 1: Consistency reflects how closely LLM predictions
align with UMA’s final resolutions across 259 events.
Model Consistency (259) Very-Stable Stable Unstable
DeepSeekV3.1 232 (89.58%) 227 (87.64%) 32 (12.36%) 0 (0.00%)
Qwen Max 231 (89.19%) 249 (96.14%) 10 (3.86%) 0 (0.00%)
Claude-4.5-Sonnet 228 (88.03%) 248 (95.75%) 11 (4.25%) 0 (0.00%)
gpt4o 203 (78.38%) 166 (64.09%) 89 (34.36%) 4 (1.54%)
gpt-4o-search-preview 185 (71.43%) 223 (86.10%) 35 (13.51%) 1 (0.39%)
4 Can LLMs Reproduce UMA’s Final Decisions?
A Polymarket event’s complete dispute trajectory (see Figure 1) is
encoded in the umaResolutionStatuses field, which records each
state transition the market undergoes. A typical sequence may look
like:
["proposed", "disputed", "proposed", "resolved"].
Using this field in our collected API data, we first identify all in-
dividual occurrences of the disputed state, yielding a total of 558
user-initiated dispute events. Next, we restrict attention to mar-
kets that both (1) contain at least one disputed transition and (2)
ultimately reach a terminal resolved state. Applying these crite-
ria results in a final set of 259 disputed-and-resolved markets,
which form the basis of our subsequent analysis.Our goal is to
investigate whether LLMs equipped with web-search capabilities
can independently reproduce UMA’s final resolutions. If LLMs can
match UMA’ outcomes, this would suggest the feasibility of a more
transparent and objective mechanism for resolving decentralized
prediction markets—potentially mitigating subjective biases or ma-
nipulation risks in the UMA voting process.To evaluate this, we
prompt five frontier LLMs to search only for information available
before the UMA decision timestamp and to infer the correct mar-
ket resolution according to the official Polymarket rulebook. Each
model is queried three independent times to measure stability. For
each event, a model’s final answer is determined by majority vote
across its three runs. Consistency is then computed as the agree-
ment rate between the model’s majority-vote prediction and the
ground-truth UMA resolution across the 259disputedmarkets.
The results, including both model–UMA consistency and model
internal stability (very-stable, stable, unstable across the three runs),
are shown in Table 1. Across the five evaluated frontier models, we
observe a clear separation in both alignment with UMA outcomes
and internal stability. DeepSeekV3.1, Qwen Max, and Claude-4.5-
Sonnet achieve the highest consistency (88–90%) and very-stable
rates (exceeding 95% for the latter two), demonstrating that fron-
tier LLMs can reproduce UMA’s final resolutions with high fi-
delity when limited to information available at decision time. While
the two OpenAI variants show comparatively lower consistency—
especially gpt-4o-search-preview (71.43%)—their performance
still exceeds chance by a wide margin, indicating nontrivial signal
extraction under temporal constraints. Overall, these results affirm
that LLMs are capable of approximating UMA arbitration outcomes,
though persistent model-specific reliability gaps highlight the need
for careful validation before deploying LLM-assisted adjudication
in decentralized governance settings.

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Junhao Wen, Juncen Zhou, and Junjie Huang
Table 2: Model performance when predicting dispute out-
comes using only pre-dispute semantic information.
Model Accuracy Precision Recall F1 Score
Claude-Sonnet-4.5 0.5701 0.6305 0.3388 0.4408
DeepSeek-V3.1 0.5410 0.5680 0.3424 0.4273
Qwen-Max 0.4731 0.4601 0.3157 0.3745
GPT-4o 0.3998 0.3618 0.2623 0.3041
5 Can LLMs Predict UMA Disputes in Advance?
To evaluate this hypothesis, we construct a structured few-shot
prompt using twelve events: nine disputed cases covering diverse
dispute types (semantic ambiguity, definitional uncertainty, ev-
identiary limitations, reporting inconsistencies, and temporal in-
stability), plus three non-disputed events. The choice of twelve
exemplars balances coverage of major dispute categories while
keeping the prompt size tractable for all models. Models receive
only the event rule text and timestamps, ensuring that predictions
rely solely on semantic features of the rule descriptions.
The dataset for this experiment is derived from all Polymarket
events that contain at least one user-initiated disputed transition,
yielding 558 total dispute events. From these, ninedisputed events
are selected as in-context exemplars for the prompt, leaving 549
remaining disputed cases. For evaluation, we pair these 549 cases
with 549 randomly sampled non-disputed events, forming a bal-
anced test set of 1,098 samples. Because the dataset is balanced, a
random or majority-class baseline corresponds to an accuracy of
0.50. We evaluate four LLMs on this test set, and their performance
is shown in Table 2.
From Table 2, we observe that predictive performance remains
limited across all models. Although some models perform slightly
above the random baseline (for example, Claude with an accuracy
of 0.5701), none achieve strong discriminative ability. This indicates
that semantic information derived solely from event rules and pre-
dispute descriptions provides only weak signals for forecasting
futuredisputes.
This observation leads to two insights. First, within our dataset,
neither the clarity nor the structural quality of Polymarket rule
wording appears to play a decisive role in determining whether
an event will later become disputed. Textual cues alone are not
sufficient for reliably anticipating dispute formation. Second, the
emergence of disputes seems to be shaped mainly by external
real-world developments, including evolving facts, unstable or in-
complete evidence, conflicting reports, media dynamics, and delays
in authoritative confirmation.
6 Conclusion
Our analysis provides clear answers to the two research questions
posed in this work. ForRQ1, we find that advanced LLMs with con-
trolled access to public information can closely align with UMA’s
final dispute resolution outcomes, showing strong agreement and
internal stability within our experimental setting. This result indi-
cates that the evidence interpretation process, which is traditionally
carried out through decentralized voting by token holders, can in
part be approximated by an autonomous agent equipped with re-
trieval capabilities. Rather than replacing human governance, LLMs
may function as complementary adjudication tools that deliver con-
sistent and auditable reasoning and help promote transparency and
scalability in optimistic oracle frameworks.
ForRQ2, we show that LLMs cannot reliably predict which
Polymarket events will become disputed when limited to the se-
mantic content of event rules. Textual clarity or ambiguity in the
rule descriptions does not provide a sufficient signal for forecasting
dispute formation. Instead, disputes tend to emerge from external
real-world uncertainty, evolving evidence, reporting inconsisten-
cies, and delays in authoritative confirmation, all of which fall
outside the rule text itself.
Taken together, these findings point to a natural division of
labor. The emergence of disputes is shaped by the evolving state
of real-world information, whereas dispute resolution depends on
interpreting that information once it becomes available. Within this
lifecycle, LLMs appear well-suited for assisting in the resolution
stage but are not effective for anticipating disputes based solely
on event semantics. This reveals a realistic and bounded role for
LLM-based agents in decentralized governance: providing stable
and consistent evaluations in the post-dispute stage while leaving
pre-dispute forecasting to market behavior.
References
[1] Agostino Capponi et al. 2025. DAO-AI: Evaluating Collective Decision-Making
with Web-Enabled LLM Agents.arXiv preprint arXiv:2510.21117(2025).
[2] Yiling Chen and David Pennock. 2010. A survey of prediction market design. In
Algorithmic Game Theory. 1–33.
[3] Andrea Chiarelli et al . 2023. A Systematic Literature Review of Blockchain
Oracles.Aalto University Publication Series(2023).
[4] Zheng Chu, Jingchang Chen, Qianglong Chen, Haotian Wang, Kun Zhu, Xiyuan
Du, Weijiang Yu, Ming Liu, and Bing Qin. 2024. BeamAggR: Beam Aggregation
Reasoning over Multi-source Knowledge for Multi-hop Question Answering. In
ACL. 1229–1248.
[5] Botao Amber Hu, Yuhan Liu, and Helena Rong. 2025. Trustless Autonomy:
Self-Sovereign Large Language Model Agents in Decentralized Systems.arXiv
preprint arXiv:2505.09757(2025).
[6] Joel Khalili and Kate Knibbs. 2025.Volodymyr Zelensky’s Clothing Has Sparked a
Polymarket Rebellion. https://www.wired.com/story/volodymyr-zelensky-suit-
polymarket-rebellion
[7] Kartikay Kumar and Muhammad Khan. 2021. Decentralized oracles: A compre-
hensive survey.IEEE Access9 (2021), 92272–92294.
[8] Ollie Liu, Deqing Fu, Dani Yogatama, and Willie Neiswanger. 2025. DeLLMa:
Decision Making Under Uncertainty with Large Language Models. InICLR.
[9] Othman et al . 2013. A practical liquidity-sensitive automated market maker.
TEAC1, 3 (2013), 1–25.
[10] Amir Pasdar and Young Choon Lee. 2023. A Survey on Blockchain Oracle
Implementation.Comput. Surveys55, 12 (2023), 1–36.
[11] Oriane Peter and Kate Devlin. 2025. Decentralising LLM Alignment: A Case for
Context, Pluralism, and Participation. InAAAI.
[12] Jaromir Savelka et al. 2023. Large Language Models in Legal Reasoning: A Study
on Real-World Case Interpretation.Journal of Artificial Intelligence and Law
(2023).
[13] Sofia Eleni Spatharioti et al . 2025. Effects of LLM-based Search on Decision
Making: Speed, Accuracy, and Overreliance. InCHI. ACM.
[14] UMA Protocol. 2024. Understanding UMA’s Optimistic Oracle and Its Governance
Mechanisms.
[15] Zhepei Wei, Wei-Lin Chen, and Yu Meng. 2025. InstructRAG: Instructing
Retrieval-Augmented Generation via Self-Synthesized Rationales. InICLR.
[16] Justin Wolfers and Eric Zitzewitz. 2004. Prediction Markets.Journal of Economic
Perspectives18, 2 (2004), 107–126.
[17] Qianqian Xie et al . 2024. FinBen: A Holistic Financial Benchmark for Large
Language Models. InNeurIPS.
[18] Shunyu Yao et al. 2024. Lawyer GPT: A Legal Large Language Model with En-
hanced Domain Knowledge and Reasoning Capabilities. InProceedings of the 2024
3rd International Symposium on Robotics, Artificial Intelligence and Information
Engineering. 108–112.
