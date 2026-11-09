---
title: Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use
url: https://arxiv.org/abs/2610.21571
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Uiji Hwang
- Richeng Xuan
- Taeuk Kim
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.21571
pages: 14
chars: 59581
fetched_at: '2026-11-08T13:34:32+00:00'
kb_version: 1
---

# Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use

Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use
Uiji Hwang1, Richeng Xuan2, Taeuk Kim1*
1Hanyang University, 2Hunyuan, Tencent,
{willpower, kimtaeuk}@hanyang.ac.kr,richxuan@tencent.com
Abstract
Large language model (LLM) agents solve
complex tasks by calling external tools over
multiple turns. Recent work has proposed tool
graph memory, which stores past experience
as tool transitions to guide subsequent selec-
tion. However, it remains unclear whether this
component consistently improves agents’ tool
use or undermines it. We evaluate tool graph
memory on nine models and two benchmarks,
finding that it seldom improves significantly
over baselines, and that its gains, where present,
cost over twice the LLM calls. The memory’s
guidance is often incorrect, and random or no
guidance retains most of the gain, implying that
the benefit stems from extra computation rather
than the memory itself. Moreover, even with
the correct next tool suggested, many failures
remain, such as giving up without a tool call.
Storing the same experience instead as textual
insights outperforms tool graph memory with
almost no extra LLM calls. This suggests that
memory serves better as a soft prior than as a
prescription of the next tool, leading to a more
effective and generalizable solution.
1 Introduction
Large language models (LLMs) are increasingly
used to support tool-use agents (Schick et al., 2023;
Yao et al., 2023; Qin et al., 2024) that interact with
users and tools over multiple turns (Lu et al., 2025;
Patil et al., 2025). As agents encounter similar situ-
ations across tasks, memory enables them to retain
and reuse experience from previous interactions (Er
et al., 2026; Xiao et al., 2025; Li and Tao, 2026).
More specifically, recent work such as Tool-
Net (Liu et al., 2024) and H-EPM (Li et al., 2026)
has proposed the concept oftool graph memory,
which represents prior experience as tool transi-
tions in a graph, providing step-level guidance for
selecting the next tool. However, it is still an open
*Corresponding author.
Oracle:get_current_timestamp search_holiday timestamp_diff
Tool Graph Memory 58LLM calls
get_current_timestamp()
Next-tool:timestamp_diff shift_timestamp
timestamp_diff(now, Jan 1, 2025)×
Next-tool:timestamp_diff datetime_info_to_timestamp
timestamp_diff(now, Jan 1, 2025)×
holiday date not searched
repeated untilthe turn limit
Insight Memory 4LLM calls
Insight: Never assume dates. Retrieve current and holiday dates before calculating.
search_holidayget_current_timestamp timestamp_diff ✓
timestamp_diff
shift_timestamp
search_holiday×
How manydaysisit tillChristmas Day?
Figure 1: An example of tool graph memory and insight
memory. The tool graph never suggests the prerequi-
sitesearch_holiday; following the insight, the agent
retrieves the holiday date first and succeeds.
question whether such guidance consistently bene-
fits agents across multi-turn interactions.
In this paper, we revisit the effectiveness of tool
graph memory. First, we evaluate whether tool
graph memory consistently improves over memory-
free baselines across model families, sizes, and
benchmarks, using repeated runs and paired signif-
icance tests. Second, we quantify the additional
computational cost it imposes, measured in LLM
calls and tokens. Third, through manual analysis
and controlled experiments, we examine the source
of its gains, where present. Finally, we identify the
failure modes that next-tool suggestions alone fail
to resolve and characterize the form of guidance
required beyond such suggestions.
Surprisingly, we find that tool graph memory
rarely yields a significant gain over the base agent
across models and benchmarks, and that the gains
of H-EPM require substantially more LLM calls
and tokens. Moreover, these gains do not stem
from the memory itself, whose suggestions are of-
ten incorrect: replacing the suggested tools with
randomly chosen ones, or removing the sugges-
tions altogether, retains most of the improvement.
Instead, the improvement comes from the agent
arXiv:2610.21571v1  [cs.CL]  15 Oct 2026

Model ToolSandbox BFCL-v4
Base ToolNet H-EPM Insight Base ToolNet H-EPM Insight
Qwen3.5-2B 0.420 0.428 0.4360.488 + 0.133 0.044 − 0.1380.165
Qwen3-8B 0.500 0.507 0.4760.556 + 0.171 0.129 0.1790.242 +
Qwen3.6-35B-A3B 0.626 0.608 0.6700.6740.181 0.108 − 0.1560.206
gemma-4-E4B-it 0.588 0.547 − 0.5540.6200.221 0.094 − 0.2520.285 +
gemma-4-26B-A4B-it 0.690 0.655 − 0.705 0.705 0.5660.369 − 0.519 0.531
Ministral-3-8B 0.631 0.588 − 0.672+ 0.539− 0.209 0.141 − 0.328+ 0.306+
Mistral-Small-3.2-24B 0.545 0.557 0.603 + 0.620+ 0.231 0.127 − 0.2500.338 +
gpt-oss-20b 0.579 0.573 0.6200.630 + 0.325 0.152 − 0.3690.427 +
gpt-oss-120b 0.726 0.674 − 0.7130.7340.494 0.275 − 0.559+ 0.454
Table 1: Performance of LLM agents on ToolSandbox and the multi-turn subset of BFCL-v4, averaged over
three runs. The best method per benchmark is inbold. The plus ( +) and minus (−) signs indicate significant
improvements and decrements over Base (p <0.05). Standard deviations andp-values are reported in Table 6.
making more tool calls; indeed, a simple instruc-
tion encouraging the agent to keep calling tools
yields comparable gains.
Furthermore, even with gold-standard tools in-
jected as an upper bound, many failures persist, e.g.,
giving up without calling a necessary tool or invok-
ing one before its prerequisites are met. Next-tool
suggestions thus cannot fully resolve them. We hy-
pothesize that the agent requires higher-level guid-
ance on what to do in its situation, whichinsight
memory—a form of semantic memory (Sumers
et al., 2024; Liang et al., 2025; Du, 2026) in natu-
ral language—can provide (see Figure 1). Insight
memory recovers most of the scenarios where tool
graph memory degrades and outperforms it in most
settings with almost no extra LLM calls. These
results suggest that, in multi-turn tool use, agents
benefit more from such situation-level cues than
from direct tool suggestions.
2 Limited Benefit of Tool Graph Memory
2.1 Tool Graph Memory
Tool graph memory builds a graph of tool transi-
tions from successful trajectories, as in Figure 1.
ToolNet (Liu et al., 2024) represents tools as
nodes and transitions as weighted, directed edges,
where weights reflect how frequently each transi-
tion occurs. It presents the agent with only the
successors of the previously invoked tool, using
these weights as preference scores.
In contrast, H-EPM (Li et al., 2026) keeps the
full tool set; its weighted tool transitions serve as
procedural memory, and the summaries of the con-
texts in which each transition occurred, attached to
the edges, as episodic memory. At each step, the
agent decides whether to summarize the current
state. If so, H-EPM suggests the two successor
tools whose stored contexts best match the result-
ing summary; otherwise, the two with the highest
transition weights. We refer to the candidate tools
provided by both methods as next-tool suggestions,
or the guidance of tool graph memory.1
2.2 Experimental Settings
We compare agents augmented with tool graph
memory against memory-free variants (Base).
Both are evaluated on two multi-turn tool-use
benchmarks—ToolSandbox (Lu et al., 2025) and
the corresponding subset of BFCL-v4 (Patil et al.,
2025)—with task performance reported on a 0–1
scale. We employ nine open-weight models from
the Qwen, Gemma, Mistral, and gpt-oss families,
ranging from 2B to 120B parameters. Each method
is run three times, and we report the mean and
standard deviation. Details of the benchmarks and
experimental setup are provided in Appendix A.
2.3 Experimental Results
Performance.Table 1 shows that neither Tool-
Net nor H-EPM consistently improves over Base.
ToolNet underperforms Base in most cases, includ-
ing all nine models on BFCL-v4, with a statistically
significant gap in 12 (p <0.05; Table 6). H-EPM,
meanwhile, outperforms Base in most settings, yet
its gain is reliable in only four settings. Table 5
reveals a similar pattern for proprietary models
(GPT-4.1 and GPT-5.1) on ToolSandbox. Insight, a
distinct memory type, is discussed in Section 4.
Efficiency.As Table 8 and Figure 5 in the Ap-
pendix reveal, H-EPM on average uses 2.72 × as
many LLM calls and 2.21× as many tokens as Base
on ToolSandbox, with a similar increase in LLM
calls on BFCL-v4. ToolNet instead uses fewer
tokens than Base, as it presents only a subset of
1We use H-EPM’s inference-time memory variant, its
strongest in our setting, not the reinforcement learning one.

30%
(26)
0%
(0)
20%
(17)
50%
(43)
Followed Ignored
CorrectWrong
(a) Improved by H-EPM
0%
(0)
2%
(1)
42%
(18)
56%
(24)
Followed Ignored
CorrectWrong
(b) Degraded by H-EPM
Figure 2: Decisive turns in the scenarios where H-EPM
(a) improves and (b) degrades on Mistral-Small-3.2-24B,
by whether the tool suggestion is correct and followed;
each cell gives the percentage and number of turns. Fig-
ure 7 shows the results of gemma-4-E4B-it.
tools to the agent, but is not notably better in any
setting. Neither method therefore offers a better
performance–cost trade-off than Base.
3 Origin of Tool Graph Memory’s Gains
While tool graph memory offers no consistent im-
provement, H-EPM does achieve significant gains
in a few settings, such as Mistral-Small-3.2-24B
on ToolSandbox. We thus focus on these gains and
examine where they truly come from.
3.1 Manual Analysis of Successful Scenarios
On Mistral-Small-3.2-24B, we manually inspect
the full trajectories of scenarios that fail under Base
but succeed with H-EPM. We annotate every deci-
sive turn—one that accounts for the outcome dif-
ference between H-EPM and Base—on two crite-
ria: (1) the correctness of the suggestion and (2)
whether the agent adopted it.
Figure 2a shows that H-EPM provides a correct
tool suggestion in only 30% of these turns, mean-
ing its recommendations are often misleading. In
another 50%, the agent calls the necessary tool
on its own despite an incorrect suggestion. The
remaining 20% occur in insufficient-information
cases (see Appendix C.1). In sum, much of the
improvement here does not result from simply fol-
lowing helpful next-tool suggestions.
3.2 Ablation Study
We further conduct experiments on three models to
test whether H-EPM’s suggested tools themselves
drive the gain. We replace themwith random tools
or remove them entirely (w/o suggestions), keeping
the rest of H-EPM fixed. Table 2 shows that both
variants perform comparably to H-EPM; the latter
even outperforms it on two of the three models.
This raises the question of what actually ac-
counts for H-EPM’s improvement. For each con-
dition, we take the scenarios that fail under Base
Conditions / ModelsMistral-Small-3.2-24B gpt-oss-20b gemma-4-E4B-it
Base (only LLMs) 0.545 0.579 0.588
Tool graph memory (H-EPM) 0.603 +(2.0×)0.620(1.8×)0.554(2.0×)
Replacing the suggested tools of H-EPM
with random tools 0.571(2.3×)0.663 +(2.7×)0.553(2.0×)
with the correct tool (oracle) 0.682 +(1.6×)0.643 +(2.5×)0.666 +(2.0×)
Removing a component of H-EPM
w/o suggestions 0.602 +(1.7×)0.633 +(2.7×)0.598(1.9×)
w/o summarization 0.595 +(1.8×)0.633 +(2.6×)0.604(1.8×)
Without tool graph memory
Base + instruction 0.594(1.9×)0.645 +(2.7×)0.621 +(2.0×)
Adding to insight memory (§4.2)
Insight memory + H-EPM 0.600 +(2.5×)0.585(2.7×)0.617(2.8×)
Insight memory + instruction 0.671 +(2.2×)0.675 +(3.0×)0.640(2.7×)
Table 2: Ablations on ToolSandbox, with +/− as in
Table 1. Parentheses give the # of tool calls relative to
Base in cases each variant flips from failure to success.
and split them into two groups: those the condition
turns into successes and those that still fail. For
each group, we count tool calls, i.e., invocations of
the available tools, excluding H-EPM’s summary
tool and responses to the user. Across all condi-
tions, the flipped scenarios show a much larger
increase in tool calls over Base than those that still
fail; under H-EPM, they make about twice as many
calls as Base (Appendix C.3). We thus hypothesize
that the gain mainly arises from the agent simply
attempting more tool calls.
We test this hypothesis by giving the base agent
a single instruction without any tool graph: “Do
not give a final answer or give up until you have
tried the available tools” (Base + instruction).Base
+ instructionattempts more tool calls while adding
almost no LLM calls (Table 9) and outperforms
H-EPM on two of the three models (Table 2).
We conclude that the guidance of tool graph
memory contributes little to the performance im-
provement: a comparable boost can be obtained by
encouraging the agent to attempt more tool calls,
without the graph and at a much lower inference
cost. Experimental details are given in Appendix C.
4 Towards Better Memory Structure
4.1 Lessons from Tool Graph Memory
Although the tool suggestions contribute little to
the gains of H-EPM (§3), Figure 2 shows that the
agent follows every correct suggestion in the im-
proved scenarios, while 98% of the suggestions
at the decisive turns of the degraded scenarios are
incorrect. We thus investigate whether tool graph
memory would be more effective if its suggestions
were always correct. To test this, we evaluate an
oraclecondition that replaces H-EPM’s prediction
with the correct tool at each turn, as an upper bound
on tool suggestions. Theoracleimproves over H-
EPM, but many scenarios still fail (Table 2).

We classify each failure by the decision that
caused it (see Appendix D): whether to call a tool
at all (call necessity), which tool to call (tool se-
lection), when to call it (dependency), and with
what arguments (argument). These follow the or-
der in which the agent makes decisions, and when
a failure fits more than one, we assign the earliest.
Under theoracle, where the correct next tool is
always suggested,tool selectionerrors almost dis-
appear (4% of failures), while the other three modes
account for the rest (Table 11). The remaining fail-
ures thus concern what to do in a situation rather
than which tool to call next. A tool graph stores
only transitions between tools; encoding such sit-
uations would require trajectories that cover them,
which is costly in practice. This motivates memory
that provides situation-level guidance rather than
direct tool suggestions.
4.2 Insight Memory
Section 3.2 further shows that high-level guid-
ance alone can benefit the agent (Base + instruc-
tion). Strategy-based experiential memory (Hu
et al., 2026; Jiang et al., 2026) distills past trajec-
tories into transferable knowledge, either as work-
flows (Wang et al., 2025), such as tool graphs, or
as insights (Zhao et al., 2024); the latter captures
guidance at the level of situations rather than tools.
We therefore adopt insights as a direct counterpart
to tool graph memory, expecting them to address
the failure modes that persist even under theoracle.
Construction.Episodic experience can be con-
solidated into semantic knowledge in the form of
insights (Sumers et al., 2024; Liang et al., 2025; Du,
2026). We construct insight memory (Insight) from
H-EPM’s episodic summaries, including those of
failed trajectories, without using its graph: we clus-
ter the summaries, have the agent model distill
what to do and what to avoid for each cluster, and
add the insights of the most relevant clusters to the
prompt at each turn (Appendix A.3). The two mem-
ories thus draw on the same episodic experience
but provide guidance in different forms.
Results.Insight performs best in most settings
of Table 1. Its gains over Base are significant in
far more settings than those of either tool graph
memory, and it attains the highest pass@3 in al-
most all settings, with competitive pass3 (Table 7).
It keeps LLM calls close to Base and uses fewer to-
kens than H-EPM across models (Table 8). It also
recovers most scenarios that H-EPM degrades on
0% 25% 50% 75% 100%
Call necessity (19)
Tool selection (4)
Dependency (3)
Argument (3)
68%
75%
100%
100%
recovered by Insight not recovered
Figure 3: Scenarios that H-EPM degrades on Mistral-
Small-3.2-24B and gpt-oss-20b, by failure mode (§4.1),
and the percentage recovered by insight memory.
Mistral-Small-3.2-24B and gpt-oss-20b, including
everydependencyandargumentfailure (Figure 3).
This advantage is not implementation-specific: Ex-
peL (Zhao et al., 2024) also beats both tool graph
memories (Table 15), and insights built only from
successful trajectories, as tool graph memory is,
achieve comparable performance (Table 14).
Insight + tool graph.Contrary to expectations,
Insight memory + H-EPMperforms worse than
insight memory alone on seven of the nine models
and requires 2.68× as many LLM calls (Table 13).
In most scenarios that insight memory solves but
the combination fails, the failure patterns of tool
graph memory recur, and none is caused by insight
alone.Insight memory + instructionperforms best
among all conditions without the correct next tool
on all three models, even surpassingoracleon gpt-
oss-20b (Table 2), as the instruction discourages
giving up, the most common failure underoracle.
In summary, these results support insight memory
as a practical alternative to tool graph memory for
multi-turn tool use. It distills situation-level guid-
ance from the same experience and outperforms
tool graph memory in most of our settings. Exam-
ples and further analyses are in Appendix D.
5 Conclusion
Our results raise the question of what guidance
agents need from memory in multi-turn tool use.
Tool graph memory suggests the next tool from
past transitions, yet random or no suggestions re-
tain most of its gains, and even correct sugges-
tions leave many failures: tool transitions alone
do not tell agents whether, when, or with what
arguments to call tools. Insight memory instead
distills the same experience into semantic knowl-
edge about what to do in a situation, which trans-
fers across scenarios, and outperforms tool graph
memory at almost no additional LLM calls. These
outcomes suggest that semantic memory offers a
better performance–cost trade-off than procedural
or episodic memory, by informing the agent’s deci-

sions rather than prescribing its next tool.
Limitations
Our analysis targets tool graph memory, in which
nodes are tools and edges are transitions between
them, as in ToolNet and H-EPM. Tool graph mem-
ory is one form of graph memory; graph memories
whose nodes and edges also represent states, argu-
ments, or other entities go beyond what we target
here. What our analysis offers to such memories
is a lesson: insights about what to do in a situation
can help agents more than next-tool suggestions,
and our failure-mode analysis suggests what richer
graph memories may need to capture.
Insight memory is kept deliberately lightweight,
since our aim is to test whether situation-level guid-
ance helps relative to tool graph memory rather
than to optimize the memory itself: we build it with-
out training, using a pretrained sentence encoder
and standard K-means, with K selected by the sil-
houette score rather than by task performance, and
its construction adds clustering and LLM-based
insight extraction on top of H-EPM’s episodic sum-
maries, an offline cost incurred once. That insight
memory outperforms tool graph memory in most
settings even in this lightweight form supports the
value of situation-level guidance, and leaves richer
experience and other extraction strategies for future
work.
Our evaluation spans two multi-turn tool-use
benchmarks, nine open-weight models from 2B
to 120B parameters, and two frontier models on
ToolSandbox, with repeated runs and paired tests.
The analyses that explain H-EPM’s gains are nar-
rower: the ablations and manual analyses focus on
the same three models on ToolSandbox, chosen to
cover two of its larger gains and one decrease. The
qualitative pattern is consistent across the three.
References
Pengfei Du. 2026. Memory for autonomous llm
agents:mechanisms, evaluation, and emerging fron-
tiers.Preprint, arXiv:2603.07670.
Suleyman Armagan Er, Danilo Ribeiro, Yogesh Virkar,
Surafel Lakew, Adi Kalyanpur, James Gung, Thomas
Delteil, and Arshit Gupta. 2026. Memtoolagent:
Leveraging memory for tool using agents based
on environment and user feedback.Preprint,
arXiv:2606.07909.
Gemma Team, Sherif El Abd, Vaibhav Aggarwal, Robin
Algayres, Alek Andreev, Olivier Bachem, Ian Bal-
lantyne, Cormac Brick, Victor C ˘arbune, Michelle
Casbon, Mayank Chaturvedi, Aditya Chawla, Vic-
tor Cotruta, Alice Coucke, Phil Culliton, Robert
Dadashi, Lucas Dixon, Mohamed Elhawaty, Utku
Evci, and 304 others. 2026. Gemma 4 technical re-
port.Preprint, arXiv:2607.02770.
Yuyang Hu, Shichun Liu, Yanwei Yue, Guibin Zhang,
Boyang Liu, Fangyi Zhu, Jiahang Lin, Honglin Guo,
Shihan Dou, Zhiheng Xi, Senjie Jin, Jiejun Tan, Yan-
bin Yin, Jiongnan Liu, Zeyu Zhang, Zhongxiang
Sun, Yutao Zhu, Hao Sun, Boci Peng, and 28 others.
2026. Memory in the age of ai agents.Preprint,
arXiv:2512.13564.
Pengcheng Jiang, Jiacheng Lin, Zhiyi Shi, Zifeng Wang,
Luxi He, Yichen Wu, Ming Zhong, Peiyang Song,
Qizheng Zhang, Heng Wang, Xueqiang Xu, Han-
wen Xu, Pengrui Han, Dylan Zhang, Jiashuo Sun,
Chaoqi Yang, Kun Qian, Tian Wang, Changran Hu,
and 15 others. 2026. Adaptation of agentic ai: A
survey of post-training, memory, and skills.Preprint,
arXiv:2512.16301.
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying
Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E.
Gonzalez, Hao Zhang, and Ion Stoica. 2023. Ef-
ficient memory management for large language
model serving with pagedattention.Preprint,
arXiv:2309.06180.
Sijia Li, Yuchen Huang, Zifan LIU, Zijian Li, Jingjing
Fu, Lei Song, Jiang Bian, Jun Zhang, and Rui Wang.
2026. Experience-evolving multi-turn tool-use agent
with hybrid episodic–procedural memory. InForty-
third International Conference on Machine Learning.
Xinzhe Li and Yaguang Tao. 2026. When does mem-
ory help multi-trajectory inference for tool-use llm
agents?Preprint, arXiv:2605.28224.
Jiafeng Liang, Hao Li, Chang Li, Jiaqi Zhou, Shixin
Jiang, Zekun Wang, Changkai Ji, Zhihao Zhu, Runx-
uan Liu, Tao Ren, Jinlan Fu, See-Kiong Ng, Xia
Liang, Ming Liu, and Bing Qin. 2025. Ai meets
brain: Memory systems from cognitive neuroscience
to autonomous agents.Preprint, arXiv:2512.23343.
Alexander H. Liu, Kartik Khandelwal, Sandeep Sub-
ramanian, Victor Jouault, Abhinav Rastogi, Adrien
Sadé, Alan Jeffares, Albert Jiang, Alexandre
Cahill, Alexandre Gavaudan, Alexandre Sablayrolles,
Amélie Héliou, Amos You, Andy Ehrenberg, Andy
Lo, Anton Eliseev, Antonia Calvi, Avinash Soori-
yarachchi, Baptiste Bout, and 101 others. 2026.
Ministral 3.Preprint, arXiv:2601.08584.
Xukun Liu, Zhiyuan Peng, Xiaoyuan Yi, Xing Xie,
Lirong Xiang, Yuchen Liu, and Dongkuan Xu.
2024. Toolnet: Connecting large language mod-
els with massive tools via tool graph.Preprint,
arXiv:2403.00839.
Jiarui Lu, Thomas Holleis, Yizhe Zhang, Bernhard Au-
mayer, Feng Nan, Haoping Bai, Shuang Ma, Shen

Ma, Mengyu Li, Guoli Yin, Zirui Wang, and Ruom-
ing Pang. 2025. ToolSandbox: A stateful, conver-
sational, interactive evaluation benchmark for LLM
tool use capabilities. InFindings of the Association
for Computational Linguistics: NAACL 2025, pages
1160–1183, Albuquerque, New Mexico. Association
for Computational Linguistics.
Mistral AI. 2025. Mistral-small-3.2-24b-instruct-2506.
OpenAI. 2025a. Gpt-5.1 instant and gpt-5.1 thinking
system card addendum.
OpenAI. 2025b. Introducing gpt-4.1 in the api.
OpenAI, Sandhini Agarwal, Lama Ahmad, Jason
Ai, Sam Altman, Andy Applebaum, Edwin Ar-
bus, Rahul K. Arora, Yu Bai, Bowen Baker, Haim-
ing Bao, Boaz Barak, Ally Bennett, Tyler Bertao,
Nivedita Brett, Eugene Brevdo, Greg Brockman, Se-
bastien Bubeck, Che Chang, and 107 others. 2025.
gpt-oss-120b & gpt-oss-20b model card.Preprint,
arXiv:2508.10925.
OpenAI, Aaron Hurst, Adam Lerer, Adam P. Goucher,
Adam Perelman, Aditya Ramesh, Aidan Clark,
AJ Ostrow, Akila Welihinda, Alan Hayes, Alec
Radford, Aleksander M ˛ adry, Alex Baker-Whitcomb,
Alex Beutel, Alex Borzunov, Alex Carney, Alex
Chow, Alex Kirillov, Alex Nichol, and 400 oth-
ers. 2024. Gpt-4o system card.Preprint,
arXiv:2410.21276.
Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen,
Ke Jiang, Zifeng Wang, Rujun Han, Long Le, Samira
Daruki, Xiangru Tang, Vishy Tirumalashetty, George
Lee, Mahsan Rofouei, Hangfei Lin, Jiawei Han,
Chen-Yu Lee, and Tomas Pfister. 2026. Reasoning-
bank: Scaling agent self-evolving with reasoning
memory. InThe Fourteenth International Confer-
ence on Learning Representations.
Shishir G Patil, Huanzhi Mao, Fanjia Yan, Char-
lie Cheng-Jie Ji, Vishnu Suresh, Ion Stoica, and
Joseph E. Gonzalez. 2025. The berkeley function
calling leaderboard (BFCL): From tool use to agentic
evaluation of large language models. InForty-second
International Conference on Machine Learning.
Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan
Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang,
Bill Qian, Sihan Zhao, Lauren Hong, Runchu Tian,
Ruobing Xie, Jie Zhou, Mark Gerstein, dahai li,
Zhiyuan Liu, and Maosong Sun. 2024. ToolLLM:
Facilitating large language models to master 16000+
real-world APIs. InThe Twelfth International Con-
ference on Learning Representations.
Qwen Team. 2026a. Qwen3.5: Towards native multi-
modal agents.
Qwen Team. 2026b. Qwen3.6-35B-A3B: Agentic cod-
ing power, now open to all.
Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta
Raileanu, Maria Lomeli, Eric Hambro, Luke Zettle-
moyer, Nicola Cancedda, and Thomas Scialom. 2023.
Toolformer: Language models can teach themselves
to use tools. InThirty-seventh Conference on Neural
Information Processing Systems.
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik R Narasimhan, and Shunyu Yao. 2023. Re-
flexion: language agents with verbal reinforcement
learning. InThirty-seventh Conference on Neural
Information Processing Systems.
Theodore Sumers, Shunyu Yao, Karthik R Narasimhan,
and Thomas L. Griffiths. 2024. Cognitive architec-
tures for language agents.Transactions on Machine
Learning Research. Survey Certification, Featured
Certification.
Wenhui Wang, Furu Wei, Li Dong, Hangbo Bao,
Nan Yang, and Ming Zhou. 2020. Minilm: Deep
self-attention distillation for task-agnostic com-
pression of pre-trained transformers.Preprint,
arXiv:2002.10957.
Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, and
Graham Neubig. 2025. Agent workflow memory. In
Forty-second International Conference on Machine
Learning.
Yunzhong Xiao, Yangmin Li, Hewei Wang, Yunlong
Tang, and Zora Zhiruo Wang. 2025. Toolmem: En-
hancing multimodal agents with learnable tool capa-
bility memory.Preprint, arXiv:2510.06664.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025. Qwen3 technical report.Preprint,
arXiv:2505.09388.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik R Narasimhan, and Yuan Cao. 2023.
React: Synergizing reasoning and acting in language
models. InThe Eleventh International Conference
on Learning Representations.
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu
Lin, Yong-Jin Liu, and Gao Huang. 2024. Expel:
Llm agents are experiential learners. InProceedings
of the AAAI Conference on Artificial Intelligence,
volume 38, pages 19632–19642.

A Detailed Experimental Setup
A.1 Benchmarks and Evaluation
ToolSandbox (Lu et al., 2025) is a stateful, conver-
sational benchmark with 34 tools over 11 domains.
Its 1,032 scenarios include distraction tools and
test state dependencies, canonicalization, and in-
sufficient information, in which a needed tool is
withheld and the agent should recognize that it can-
not complete the task. We use the training/test split
of H-EPM (825 training and 207 test scenarios).
A trajectory is scored by its similarity to the mile-
stones, events that must occur, and scores zero if it
matches a minefield, an event that must not occur;
following H-EPM, a scenario counts as a success
when this score exceeds 0.55. The multi-turn sub-
set of BFCL-v4 (Patil et al., 2025) has 800 tasks
over eight APIs in four categories: base, missing
function, missing parameter, and long context. We
hold out all four variants of 40 tasks as the test set
(160 tasks) and use the other 640 for training, so
that no underlying task is shared. A task is correct
only if the backend state and the response checks
pass at every turn.
Following ToolSandbox, we use GPT-4o (Ope-
nAI et al., 2024) as the user simulator. With GPT-
4.1 instead, as in the H-EPM protocol, for both
memory construction and evaluation on Qwen3-8B
and gemma-4-E4B-it, neither ToolNet nor H-EPM
is significantly above Base, and Insight scores high-
est on both (Table 3).
Qwen3-8B gemma-4-E4B-it
MethodScore∆pScore∆p
Base 0.462 – – 0.575 – –
ToolNet 0.483 +0.021 0.364 0.573−0.002 0.920
H-EPM 0.496 +0.034 0.277 0.559−0.016 0.573
Insight0.527+0.065 0.0230.583+0.009 0.740
Table 3: ToolSandbox with GPT-4.1 as the user sim-
ulator for both memory construction and evaluation
(n=207 scenarios). ∆ is the difference from Base, com-
puted before rounding; significance is tested as in Ta-
ble 6.
A.2 Implementation Details
H-EPM also gives the agent a summarization tool,
summarize_the_task, with a system-prompt line
asking it to call the tool; each use of the tool adds
an LLM call, and its summary accumulates in the
context. All of H-EPM’s additional calls and the in-
sight extraction use the agent model itself. To build
the memories, we roll out each training scenario
three times and keep the highest-scoring rollout, or
the shortest one on ties.
The agent models are Qwen3.5-2B (Qwen Team,
2026a), Qwen3-8B (Yang et al., 2025), Qwen3.6-
35B-A3B (Qwen Team, 2026b), gemma-4-E4B-it
and gemma-4-26B-A4B-it (Gemma Team et al.,
2026), Ministral-3-8B (Liu et al., 2026), Mistral-
Small-3.2-24B (Mistral AI, 2025), and gpt-oss-20b
and gpt-oss-120b (OpenAI et al., 2025); the frontier
models in Table 5 are GPT-4.1 (OpenAI, 2025b)
and GPT-5.1 (OpenAI, 2025a). We use greedy
decoding (temperature 0) for both the agent and
the user simulator and serve all open-weight mod-
els with vLLM (Kwon et al., 2023) on a single
NVIDIA H200 GPU.
A.3 Insight Memory Details
Insight memory is built from the episodic sum-
maries of H-EPM, including those of failed trajecto-
ries; H-EPM writes a summary only when an LLM
call judges it necessary, so summaries exist for 7%
to 26% of the 825 ToolSandbox training scenarios,
depending on the model. Using failed trajectories
is common in insight memory: ExpeL (Zhao et al.,
2024) and ReasoningBank (Ouyang et al., 2026)
learn from both failed and successful trajectories,
and Reflexion (Shinn et al., 2023) from failed at-
tempts, whereas tool graph memory uses successful
trajectories only.
We embed the summaries with all-MiniLM-L6-
v2 (Wang et al., 2020) and cluster them with K-
means, choosing K among 15 candidates from 5
to 150 by the silhouette score, subject to clusters
holding more than three summaries on average (Ta-
ble 4). The agent model then extracts insights from
each cluster with the prompt in Figure 4.
At every model call, the five most recent mes-
sages are embedded with the same encoder and
compared with all summaries, and the insights of
the clusters of the two most similar summaries are
added to the system prompt.

Modeln K n/K
ToolSandbox
Qwen3.5-2B 77 25 3.1
Qwen3-8B 360 100 3.6
Qwen3.6-35B-A3B 146 5 29.2
gemma-4-E4B-it 261 15 17.4
gemma-4-26B-A4B-it 181 5 36.2
Ministral-3-8B 300 5 60.0
Mistral-Small-3.2-24B 109 8 13.6
gpt-oss-20b 170 5 34.0
gpt-oss-120b 185 15 12.3
BFCL-v4
Qwen3.5-2B 26,877 30 895.9
Qwen3-8B 2,235 150 14.9
Qwen3.6-35B-A3B 46,738 40 1168.5
gemma-4-E4B-it 489 80 6.1
gemma-4-26B-A4B-it 924 50 18.5
Ministral-3-8B 5,247 100 52.5
Mistral-Small-3.2-24B 2,253 150 15.0
gpt-oss-20b 122 40 3.1
gpt-oss-120b 787 5 157.4
Table 4: Number of clusters selected per model. n
is the number of episodic summaries clustered, K the
selected number of clusters, and n/K the mean number
of summaries per cluster.
Insight Extraction Prompt
You are mining INSIGHTS from a cluster of AI tool-use
trajectories. Each trajectory carries a TRAJECTORY-LEVEL tag
[SUCCESS] or [FAILURE] — it reflects ONLY whether the
trajectory’s final state matched the user’s intent. It says
nothing about individual moves.
Extract concrete, transferable insights for similar future
situations:
- "do": a move that demonstrably WORKED. Mine from repeated
successful patterns AND from correct early moves of failed
trajectories.
- "avoid": a move that demonstrably HURT. Mine from concrete
failure patterns AND from wasted detours inside successes.
Every insight MUST cite a specific observable signal from the
summaries: tool name + argument shape, or environment state, or
user response pattern, or sub-sequence of 2+ tool calls. The
SUCCESS/FAILURE tag is NEVER a signal.
Support thresholds: DO needs≥2 supporting trajectories. AVOID
needs≥1 trajectory IF the failure mode names a concrete
artifact.
If only 1 trajectory or only 1 distinct pattern is present,
emit FEWER insights. An empty list is acceptable. Do NOT pad to
a count. Hard cap 10. Single actionable sentence per insight,
max∼30 words.
{trajectories_block}
Return JSON only.
Figure 4: The prompt used to extract insights from each
cluster.
B Full Results
Tables 5–8 and Figure 5 report the full results: fron-
tier models, per-model scores with significance
tests, pass rates, and inference cost.
Model Base ToolNet H-EPM Insight
GPT-4.1 0.724 0.709 0.7250.729
GPT-5.1 0.701 0.6940.702 0.702
Table 5: Task performance of frontier models on Tool-
Sandbox (n= 207).
0
1×
2×
3×
ToolSandbox
Qwen3.5-2BQwen3-8BQwen3.6-35Bgemma-E4Bgemma-26BMinistral-8BMistral-24Bgpt-oss-20bgpt-oss-120b Average
0
1×
2×
3×
BFCL-v4
ToolNet H-EPM Insight
LLM calls vs. Base ( )
Figure 5: LLM calls per scenario relative to Base of the
same model. The Average bars give the ratios of the
nine-model averages.
Retrieval latency.Insight retrieval requires no
additional LLM call and uses the same all-MiniLM-
L6-v2 encoder as H-EPM’s episodic matching.
We measure retrieval latency in-process, exclud-
ing model loading, over all agent turns in the 207
test scenarios for gpt-oss-20b, Mistral-Small-3.2-
24B, and gemma-4-E4B-it (1,295–1,494 turns per
model). On an AMD EPYC 9655 host, with four
CPU threads per shard and 12 concurrent shards
sharing the host, the full retrieval path—query em-
bedding followed by similarity scoring and top-2
selection—has a median latency of 15–17 ms per
turn (p95 29–39 ms). Embedding accounts for
nearly all of this latency, with a median of 15–17
ms (p95 28–37 ms), compared with median LLM-
call latencies of 0.4–1.1 s in the same runs. These
measurements isolate retrieval overhead rather than
end-to-end latency, which also includes prompt pre-
fill and generation.
C Analysis of the Gains of Tool Graph
Memory
C.1 Manual Analysis
We analyze the scenarios whose outcome flips be-
tween Base and H-EPM, with success determined
by the three-run mean score (Appendix A); requir-
ing all three runs to flip leaves the conclusion un-

Model Base ToolNet∆(p-value)H-EPM∆(p-value)Insight∆(p-value)
ToolSandbox
Qwen3.5-2B 0.420 ±0.003 0.428±0.008 +0.008(0.399)0.436 ±0.015 +0.016(0.469)0.488 ±0.009 +0.068(0.015)
Qwen3-8B 0.500 ±0.008 0.507±0.009 +0.006(0.660)0.476 ±0.010 −0.024(0.405)0.556 ±0.004 +0.056(0.037)
Qwen3.6-35B-A3B 0.626 ±0.001 0.608±0.002 −0.018(0.256)0.670 ±0.005 +0.044(0.055)0.674 ±0.006 +0.048(0.056)
gemma-4-E4B-it 0.588 ±0.012 0.547±0.008 −0.041(0.004)0.554 ±0.012 −0.034(0.209)0.620 ±0.003 +0.032(0.267)
gemma-4-26B-A4B-it 0.690 ±0.000 0.655±0.003 −0.035(0.026)0.705 ±0.000 +0.016(0.394)0.705 ±0.009 +0.015(0.423)
Ministral-3-8B 0.631 ±0.008 0.588±0.005 −0.044(0.004)0.672 ±0.011 +0.041(0.024)0.539 ±0.009 −0.092(<0.001)
Mistral-Small-3.2-24B 0.545 ±0.003 0.557±0.019 +0.012(0.479)0.603 ±0.009 +0.058(0.014)0.620 ±0.021 +0.075(0.004)
gpt-oss-20b 0.579 ±0.007 0.573±0.010 −0.007(0.721)0.620 ±0.035 +0.041(0.087)0.630 ±0.008 +0.050(0.046)
gpt-oss-120b 0.726 ±0.012 0.674±0.016 −0.052(0.006)0.713 ±0.006 −0.013(0.483)0.734 ±0.008 +0.009(0.655)
Average– –−0.019 –+0.016 –+0.029
BFCL-v4
Qwen3.5-2B 0.133 ±0.016 0.044±0.000 −0.090(<0.001)0.138 ±0.006 +0.004(0.803)0.165 ±0.010 +0.031(0.166)
Qwen3-8B 0.171 ±0.013 0.129±0.007 −0.042(0.156)0.179 ±0.010 +0.008(0.573)0.242 ±0.007 +0.071(0.007)
Qwen3.6-35B-A3B 0.181 ±0.006 0.108±0.007 −0.073(0.006)0.156 ±0.006 −0.025(0.140)0.206 ±0.000 +0.025(0.241)
gemma-4-E4B-it 0.221 ±0.013 0.094±0.000 −0.127(<0.001)0.252 ±0.016 +0.031(0.144)0.285 ±0.004 +0.065(0.006)
gemma-4-26B-A4B-it0.566 ±0.004 0.369±0.000 −0.197(<0.001)0.519 ±0.000 −0.047(0.059)0.531 ±0.018 −0.034(0.265)
Ministral-3-8B 0.209 ±0.004 0.141±0.004 −0.069(0.026)0.328 ±0.013 +0.119(<0.001)0.306 ±0.006 +0.097(0.003)
Mistral-Small-3.2-24B 0.231 ±0.006 0.127±0.013 −0.104(<0.001)0.250 ±0.011 +0.019(0.352)0.338 ±0.019 +0.106(<0.001)
gpt-oss-20b 0.325 ±0.013 0.152±0.019 −0.173(<0.001)0.369 ±0.019 +0.044(0.100)0.427 ±0.019 +0.102(<0.001)
gpt-oss-120b 0.494 ±0.018 0.275±0.009 −0.219(<0.001)0.559 ±0.022 +0.066(0.016)0.454 ±0.024 −0.040(0.263)
Average– –−0.121 –+0.024 –+0.047
Table 6: Full version of Table 1 (n = 207 scenarios and 160 tasks), with the standard deviation over the three runs in
subscript. ∆ is the difference from Base, computed before rounding, with the p-value of a two-sided paired t-test
over scenarios (ToolSandbox) or tasks (BFCL-v4) in parentheses. The Average row gives the mean∆ over the nine
models. The best method per benchmark is inbold.
Model Base ToolNet H-EPM Insight pass@3 pass 3 pass@3 pass 3 pass@3 pass 3 pass@3 pass 3
ToolSandbox
Qwen3.5-2B 0.401 0.362 0.406 0.372 0.411 0.3480.488 0.415
Qwen3-8B 0.546 0.425 0.527 0.435 0.527 0.4490.594 0.493
Qwen3.6-35B-A3B 0.667 0.589 0.618 0.556 0.715 0.6180.729 0.628
gemma-4-E4B-it 0.628 0.488 0.546 0.469 0.580 0.5270.676 0.556
gemma-4-26B-A4B-it 0.758 0.705 0.667 0.6470.783 0.725 0.7830.710
Ministral-3-8B 0.720 0.502 0.618 0.4440.783 0.6470.638 0.406
Mistral-Small-3.2-24B 0.638 0.382 0.604 0.459 0.715 0.5020.739 0.507
gpt-oss-20b 0.667 0.473 0.633 0.454 0.739 0.5410.758 0.556
gpt-oss-120b 0.8070.7050.725 0.6180.8360.6860.836 0.705
BFCL-v4
Qwen3.5-2B 0.1750.0940.050 0.038 0.1940.094 0.2810.069
Qwen3-8B 0.238 0.113 0.150 0.113 0.256 0.1130.338 0.150
Qwen3.6-35B-A3B 0.2250.1500.138 0.075 0.200 0.1250.2880.125
gemma-4-E4B-it 0.244 0.200 0.094 0.094 0.2940.219 0.3810.181
gemma-4-26B-A4B-it 0.5810.5500.369 0.369 0.544 0.4940.5940.469
Ministral-3-8B 0.269 0.150 0.169 0.113 0.3810.275 0.4130.200
Mistral-Small-3.2-24B 0.288 0.175 0.169 0.088 0.300 0.1940.456 0.244
gpt-oss-20b 0.475 0.169 0.219 0.100 0.519 0.2060.563 0.288
gpt-oss-120b 0.556 0.431 0.356 0.194 0.6190.500 0.6940.231
Table 7: pass@3 (solved in at least one of three runs) and pass3 (solved in all three runs) on ToolSandbox (n = 207)
and BFCL-v4 (n= 160). Best per model and per metric inbold.

Model Base ToolNet H-EPM Insight
ToolSandbox LLM calls
Qwen3.5-2B 5.42 5.04(0.93)13.80(2.55)6.66(1.23)
Qwen3-8B 4.78 4.79(1.00)16.36(3.42)5.56(1.16)
Qwen3.6-35B-A3B 5.75 6.03(1.05)16.92(2.94)5.74(1.00)
gemma-4-E4B-it 5.27 4.97(0.94)13.00(2.47)5.26(1.00)
gemma-4-26B-A4B-it 5.90 5.52(0.93)15.47(2.62)6.04(1.02)
Ministral-3-8B 5.71 5.51(0.97)17.85(3.13)5.64(0.99)
Mistral-Small-3.2-24B 5.32 4.70(0.88)13.24(2.49)4.88(0.92)
gpt-oss-20b 4.91 4.64(0.94)11.16(2.27)4.99(1.02)
gpt-oss-120b 5.26 5.15(0.98)13.82(2.63)5.10(0.97)
Average5.37 5.15(0.96)14.62(2.72)5.54(1.03)
ToolSandbox tokens
Qwen3.5-2B 10,057 7,009(0.70)16,965(1.69)16,298(1.62)
Qwen3-8B 7,556 5,425(0.72)25,853(3.42)11,324(1.50)
Qwen3.6-35B-A3B 11,289 9,010(0.80)25,517(2.26)15,094(1.34)
gemma-4-E4B-it 7,821 5,291(0.68)16,523(2.11)10,634(1.36)
gemma-4-26B-A4B-it 9,526 5,421(0.57)18,697(1.96)12,838(1.35)
Ministral-3-8B 9,932 6,490(0.65)25,435(2.56)16,805(1.69)
Mistral-Small-3.2-24B 8,427 4,757(0.56)15,975(1.90)10,431(1.24)
gpt-oss-20b 6,799 4,934(0.73)13,128(1.93)9,450(1.39)
gpt-oss-120b 6,722 5,095(0.76)14,930(2.22)8,761(1.30)
Average8,681 5,937(0.68)19,225(2.21)12,404(1.43)
BFCL-v4 LLM calls
Qwen3.5-2B 14.91 16.44(1.10)41.87(2.81)16.11(1.08)
Qwen3-8B 9.61 10.47(1.09)23.78(2.47)10.61(1.10)
Qwen3.6-35B-A3B 13.71 12.45(0.91)36.27(2.65)13.14(0.96)
gemma-4-E4B-it 8.50 8.40(0.99)19.68(2.31)10.50(1.23)
gemma-4-26B-A4B-it 13.43 13.77(1.03)26.31(1.96)15.24(1.13)
Ministral-3-8B 12.55 11.94(0.95)26.44(2.11)15.86(1.26)
Mistral-Small-3.2-24B 9.22 8.82(0.96)16.89(1.83)10.78(1.17)
gpt-oss-20b 11.24 10.49(0.93)22.41(1.99)11.99(1.07)
gpt-oss-120b 12.35 12.17(0.99)24.08(1.95)12.48(1.01)
Average11.72 11.66(0.99)26.41(2.25)12.97(1.11)
Table 8: Cost per ToolSandbox scenario (n = 207) and per BFCL-v4 task (n = 160), with the ratio to Base of the
same model in parentheses, computed before rounding. The Average row gives the nine-model averages, with the
ratios of these averages in parentheses. All calls made by the agent model are counted, including the summary calls
of H-EPM and, on BFCL-v4, the scoring call of ToolNet; the user simulator is excluded. Token counts of these
additional calls are not recorded on BFCL-v4, so only LLM calls are reported there.
changed (24% follow a correct suggestion, 66%
ignore an incorrect one; 10 scenarios). For each
of the three run pairs of a scenario, we inspect
the full trajectories and identify the turns respon-
sible for the difference in outcome; at each, we
record whether the suggestion is correct (the sug-
gested tool is the one required at that point) and
whether the agent follows it (its next call is the sug-
gested tool). All annotations were performed by
the authors. On Mistral-Small-3.2-24B this yields
30 improved scenarios with 86 such turns and 15
degraded scenarios with 43. Figure 6 shows one
improved scenario in which the agent ignores an
incorrect suggestion. The turns in Figure 2a at
which the agent follows an incorrect suggestion
yet the scenario improves are an exception: all of
them come from insufficient-information scenar-
ios, where the agent should recognize that it cannot
complete the task instead of calling a tool. The sug-
gested tool it calls is irrelevant but not a minefield,
so the metric does not penalize the call and the run
is still scored as a success.
C.2 Control Conditions
Table 10 lists the components of each condition
in Table 2; their presence was verified against the
logged requests of every run.
C.3 Tool Calls in Flipped Scenarios
For each scenario, we compute the change in tool
calls, ∆ = calls under a condition − calls under
Base, excluding calls to H-EPM’s summary tool,
which is not one of the scenario’s tools. We ex-
clude insufficient-information scenarios, in which
the agent should recognize that it cannot complete

Mistral-Small-3.2-24B gpt-oss-20b gemma-4-E4B-it
Conditionnhelped both-failD[95% CI] LLMnhelped both-failD[95% CI] LLMnhelped both-failD[95% CI] LLM
H-EPM 17/52 2.0×1.4×1.34[0.57, 2.20]2.8×20/54 1.8×1.0×1.41[0.89, 1.96]2.4×24/56 2.0×1.3×1.95[0.82, 3.12]2.7×
with random tools 19/50 2.3×1.4×1.84[0.79, 2.97]1.3×27/47 2.7×0.9×2.66[2.00, 3.34]1.3×26/54 2.0×1.6×1.09[0.09, 2.08]1.3×
with the correct tool (oracle) 43/30 1.6×1.2×1.30[0.45, 2.20]1.2×29/41 2.5×0.7×2.69[1.95, 3.45]1.5×40/39 2.0×1.8×0.77[0.01, 1.51]1.2×
w/o suggestions 27/45 1.7×1.1×1.63[0.84, 2.48]1.2×23/52 2.7×0.9×2.55[1.68, 3.51]1.2×25/55 1.9×1.3×1.25[0.26, 2.27]1.2×
w/o summarization 22/50 1.8×1.3×1.92[0.93, 3.08]2.7×22/52 2.6×1.0×2.58[1.82, 3.37]2.2×9/80 1.8×1.1×1.97[1.34, 2.67]2.1×
Base + instruction 26/44 1.9×1.2×1.57[0.86, 2.34]1.0×30/40 2.7×1.2×2.05[1.35, 2.80]1.0×19/70 2.0×1.0×2.04[1.10, 2.94]0.9×
Insight memory 30/39 2.5×1.2×2.06[1.43, 2.72]1.0×27/46 2.2×0.9×1.90[1.26, 2.55]1.0×33/51 3.2×1.4×1.60[0.83, 2.37]1.0×
Insight memory + H-EPM 23/48 2.5×1.1×2.67[1.45, 3.91]2.6×31/40 2.7×0.5×3.04[2.37, 3.73]3.1×44/40 2.8×1.5×2.01[1.21, 2.80]2.9×
Insight memory + instruction 37/35 2.2×1.3×2.19[1.53, 2.83]1.1×37/38 3.0×1.0×2.49[1.65, 3.30]1.0×38/50 2.7×1.6×1.98[1.20, 2.76]1.0×
Table 9: Tool calls in the scenarios that fail under Base, excluding runs aborted by an execution error, which leave
no trajectory. n: number of helped / both-fail scenarios. helped / both-fail: tool calls per scenario relative to Base in
the scenarios that the condition flips to success / that fail under both. D: difference in the per-scenario increase in
tool calls between the two groups, with its 95% confidence interval. LLM: LLM calls per scenario relative to Base.
All differences are significant (padj <0.05).
(a) Components
Summarization H-EPM’ssummarize_the_tasktool and a system-prompt
line asking the agent to call it
Suggestion line Appended to the last message of the conversation (the latest
user turn or tool result), listing successors of the last
invoked tool, e.g.,next tool suggestion:
set_location_service_status, set_wifi_status
Instruction “IMPORTANT: Do not give a final answer or give up until
you have tried the available tools. If a tool call fails or
returns nothing useful, try another available tool or first
resolve what it depends on, then call it again. Keep calling
tools until the task is fully resolved.” (system prompt)
(b) Conditions
Condition Summ. Sugg. Instr.
H-EPM✓ ✓–
with random tools✓ ✓–
with the correct tool (oracle)✓ ✓–
w/o suggestions✓– –
w/o summarization –✓–
Base + instruction – –✓
Insight memory + H-EPM✓ ✓–
Insight memory + instruction – –✓
Table 10: Details of the control conditions in Table 2.
Incorrect suggestion ignored Base 0.530→H-EPM 0.853
User:I don’t have cellphone signal. Can you get it on?
H-EPM:set_cellular_service_status(on=True)→
PermissionError: Cellular service cannot be turned on in
low battery mode; [. . . ];set_low_battery_mode_status(
on=False)
next tool suggestion: set_location_service_status,
set_wifi_status
H-EPM:set_cellular_service_status(
on=True)not suggested; milestone achieved
Base:set_cellular_service_status(on=True)→
PermissionError; [. . . ];set_low_battery_mode_status(
on=False); “Your cellular service should now be
working.”milestone missed
Figure 6: An improved scenario on Mistral-Small-3.2-
24B in which H-EPM ignores an incorrect suggestion
and calls the required tool on its own, with the Base
run on the same scenario. [. . . ] marks omitted calls or
turns; gray lines are the suggestions shown to the agent;
italic notes are ours.
40%
(36)
0%
(0)
0%
(0)
60%
(55)
Followed Ignored
CorrectWrong
(a) Improved by H-EPM
0%
(0)
0%
(0)
67%
(36)
33%
(18)
Followed Ignored
CorrectWrong
(b) Degraded by H-EPM
Figure 7: Manual analysis of H-EPM on gemma-4-E4B-
it, as in Figure 2 (n= 91 and 54).
the task, so additional calls are not expected to help.
Among the scenarios that fail under Base, we com-
pare those that a condition flips to success (helped)
with those that fail under both (both-fail). This
restriction aligns the two groups on the Base out-
come but does not make them comparable in other
respects, such as task difficulty. Table 9 reports
the difference D between the mean ∆ of the two
groups with a 95% percentile bootstrap confidence
interval. We test D >0 with a one-sided permu-
tation test, applying the Holm correction over the
27 comparisons. D is positive in all 27 compar-
isons, and all remain significant after the correction
(padj <0.05).
D Failure Analysis and Insight Memory
Because the scenarios span multiple turns, a run
can lose points at several decisions, and the runs
of a scenario can fail in different ways. We there-
fore label each run pair whose outcomes differ at
the decisions where the failing run loses points,
by missing a milestone or triggering a minefield,
and assign each scenario at most two dominant
modes, those found in a majority of its diverging
pairs. A single decision can also fit more than one
mode; we then take the first in the order in which
the agent decides whether to call a tool (call neces-
sity), which tool to call (tool selection), when to
call it (dependency), and with what arguments (ar-
gument), so calling a tool with made-up arguments

in an insufficient-information scenario, where the
agent should instead recognize that it cannot com-
plete the task, counts ascall necessity. We exclude
scenarios whose runs differ only in the final reply.
D.1 Oracle Failure Classification
For theoraclecondition of Table 2, we classify the
failed scenarios into the four failure modes of §4.1
(Table 11), excluding the 10 failures in which only
the final reply loses points. In alldependencycases
and in mostcall necessityandargumentcases, the
agent fails even though the correct tool is suggested
at that point. As in Appendix C.1, the authors
annotated all failures.
Failure mode Mistral-Small-3.2-24B gpt-oss-20b gemma-4-E4B-it All
Call necessity 24 38 19 81
unnecessary call 14 3 5 22
missing call 10 35 14 59
Tool selection 3 0 3 6
Dependency 3 1 3 7
Argument 19 9 16 44
Table 11: Failures of theoraclecondition by failure
mode (n= 49, 48, and 41 failed scenarios).
D.2 Examples of Failure Modes
Figure 8 shows verbatim excerpts of three degraded
scenarios. For ToolNet on Mistral-Small-3.2-24B,
7 of the degraded scenarios fail bycall necessity
and 2 byargument. In five of thecall necessity
cases, the required tool is missing from the candi-
date list and the agent responds or gives up without
calling it (missing call).
D.3 Insight Examples
Insight memory recovers 22 of the 29 scenarios
that H-EPM degrades on Mistral-Small-3.2-24B
and gpt-oss-20b, across all four failure modes (Fig-
ure 3).
Figure 9 shows three examples. In (a), H-EPM
follows a suggestion to add the reminder with place-
holder content instead of asking for it, whereas an
insight tells the agent to ask for the missing content
first. In (b), H-EPM follows a suggestion to shift
the timestamp and searches outside the valid range,
whereas an insight tells the agent to use the current
timestamp as the upper bound. In (c), H-EPM re-
trieves the current timestamp but then converts a
made-up one, whereas an insight tells the agent not
to assume the current date.
D.4 Additional Analyses
We classify the scenarios that insight memory
solves butInsight memory + H-EPMfails on
Mistral-Small-3.2-24B and Qwen3-8B into the four
modes of §4.1. The same modes recur, most often
tool selectionandcall necessity: the agent follows
a suggestion to an unrelated tool, typically the sum-
mary tool, or gives up after such suggestions. None
is attributed to an insight alone. Figure 10 shows
two cases.
Position of the insight block.InInsight memory
+ H-EPM, the insight block precedes the conver-
sation in the system prompt, while the suggestion
line follows it at the end of the last message. To
test whether this order matters, we move the block
to the end of the last message, after the sugges-
tion line, keeping everything else unchanged. The
combination still falls below insight memory alone
(Table 12), so the degradation does not depend on
where the block is injected.
ModelInsight + H-EPM
block in system block in last message
Mistral-Small-3.2-24B 0.620 0.600 0.587
gemma-4-E4B-it 0.620 0.617 0.596
Table 12:Insight memory + H-EPMon ToolSandbox
with the insight block in the system prompt (default) or
in the last message.
ModelInsight Insight + H-EPM
Qwen3.5-2B 0.488(6.66)0.528(14.60)
Qwen3-8B0.556(5.56)0.451(16.29)
Qwen3.6-35B-A3B0.674(5.74)0.670(18.11)
gemma-4-E4B-it0.620(5.26)0.617(14.70)
gemma-4-26B-A4B-it0.705(6.04)0.630(12.95)
Ministral-3-8B 0.539(5.64)0.621(18.37)
Mistral-Small-3.2-24B0.620(4.88)0.600(11.76)
gpt-oss-20b0.630(4.99)0.585(13.40)
gpt-oss-120b0.734(5.10)0.710(13.65)
Table 13: Insight memory andInsight memory + H-
EPMon ToolSandbox. LLM calls per scenario in paren-
theses; the higher score is inbold.
Failed trajectories.Table 14 compares insights
distilled from successful trajectories only with in-
sights from the full pool that also includes failed
trajectories.
ExpeL.We port ExpeL (Zhao et al., 2024) and
evaluate it in the same setting (Table 15). It per-
forms similarly to Insight and above both tool graph
memories. Unlike Insight, which retrieves only the
insights of the matching clusters, ExpeL injects its
full rule set and two few-shot trajectories per task.

(a) Call necessity: unnecessary call Base 1.000→H-EPM 0.000
User:What’s my todo yesterday?no reminder tool should be called
H-EPM:[. . . ]
next tool suggestion: unit_conversion, summarize_the_task
H-EPM:datetime_info_to_timestamp(year=2024, month=10,
day=16, . . . );datetime_info_to_timestamp(. . . day=17
. . . )made-up dates
next tool suggestion: datetime_info_to_timestamp,
search_reminder
H-EPM:search_reminder(
creation_timestamp_lowerbound=1729036800, . . . )→
[]minefield
Base: “I’m sorry, but I currently don’t have the ability to access or retrieve
your personal to-do lists or past tasks.”no tool called
(b) Dependency: current time skipped Base 0.667→H-EPM 0.333
User:What’s on my reminder yesterday?
H-EPM:search_reminder(
creation_timestamp_lowerbound=1716393600,
creation_timestamp_upperbound=1716480000)→
[]no get_current_timestamp; milestone missed
H-EPM:“It looks like you don’t have any reminders from yesterday.”;
User:I think there should be one. Can you check again?
next tool suggestion: search_reminder,
datetime_info_to_timestamp
H-EPM:datetime_info_to_timestamp(year=2024, month=5,
day=20, . . . ); [. . . ];search_reminder(. . . )→
[]made-up dates
Base:get_current_timestamp()→1788758978;search_reminder(
creation_timestamp_lowerbound=1788669378, . . . )→
[{’content’: ’Buy tickets for Merrily next week’,
. . . }]milestones achieved
(c) Argument: made-up year Base 0.978→H-EPM 0.500
User:How many days is it till Christmas Day
H-EPM:[. . . ];get_current_timestamp()→
1788771888September 2026
next tool suggestion: shift_timestamp, timestamp_diff
H-EPM:search_holiday(holiday_name="Christmas", year=2024)
→1735084800made-up year; milestone missed
H-EPM:timestamp_diff(. . . ); “There are 622 days left until
Christmas Day.”
Base:search_holiday(holiday_name="Christmas Day");
get_current_timestamp();timestamp_diff(. . . ); “It is 108 days
[. . . ] until Christmas Day.”milestones achieved
Figure 8: Scenarios degraded by H-EPM on Mistral-Small-3.2-24B, labeled by failure mode (§4.1), with the Base
run on the same scenario.
(a) Call necessity: unnecessary call H-EPM 0.500→Insight 1.000
User:Add a reminder for tomorrow 5PM
H-EPM:[. . . ];datetime_info_to_timestamp(. . . )
next tool suggestion: add_reminder,
datetime_info_to_timestamp
H-EPM:add_reminder(content="Reminder",
. . . )called instead of asking; placeholder content
insight:“When a user requests an action (like setting a reminder) but
provides insufficient detail, the agent should proactively seek the missing
specific information (e.g., the reminder content) rather than executing the
action with placeholder data.”
Insight:“What should the reminder say?”; [. . . ];add_reminder(
content="Buy chocolate milk", . . . )milestones achieved
(b) Tool selection: unneeded time shift H-EPM 0.333→Insight 0.877
User:I need the oldest one, not recent ones. [. . . ] Just go as far back as
possible.
H-EPM:[. . . ];get_current_timestamp()
next tool suggestion: search_messages, shift_timestamp
H-EPM:shift_timestamp(weeks=-10000);search_messages(
creation_timestamp_upperbound=-4259229904)→
ValueErrorout of the valid range
insight:“If the user wants the oldest message, use the current timestamp
to set the upper bound of the search range (e.g., get_current_timestamp
→search_messages).”
Insight:get_current_timestamp(); [. . . ];search_messages(
creation_timestamp_upperbound=1788779953)
oldest message found
(c) Argument: made-up timestamp H-EPM 0.463→Insight 0.982
User:I need a break. How far are we from Christmas Day?
H-EPM:[. . . ];get_current_timestamp()→1788779222
next tool suggestion: shift_timestamp, timestamp_diff
H-EPM:timestamp_to_datetime_info(timestamp=1738347222)→
{’year’: 2025,
. . . }ignores the returned value; made-up timestamp
H-EPM:search_holiday(holiday_name="Christmas Day",
year=2025); [. . . ]; “There are 256 days [. . . ] until Christmas
Day.”milestone missed
insight:“Avoid assuming the current date without retrieving it first. This
can lead to incorrect calculations [. . . ]. Instead, always use
get_current_timestamp before calculating differences.”
Insight:get_current_timestamp();search_holiday(
holiday_name="Christmas Day");timestamp_diff(. . . ); “It is
currently 108 days [. . . ] until Christmas Day.”milestones achieved
Figure 9: Scenarios degraded by H-EPM on Mistral-Small-3.2-24B that Insight recovers, with the insight
displayed before the decisive call.

(a) Dependency: battery mode Insight 0.892 → Insight + H-EPM 0.150
User:I can’t access my current location. Can you help me fix that in
settings?
insight:“Disable low battery mode (e.g., via
set_low_battery_mode_status) before enabling location services, as low
battery mode can block location access.”
Insight:get_location_service_status(),
get_low_battery_mode_status();set_low_battery_mode_status(
on=False);set_location_service_status(on=True); “Your
location service should now be enabled.”milestones achieved
Insight + H-EPM:[. . . ];get_location_service_status()→False
next tool suggestion: set_location_service_status,
get_wifi_status
Insight + H-EPM:set_location_service_status(on=True)→
PermissionError: cannot be turned on in low battery
modeprerequisite skipped
next tool suggestion: set_low_battery_mode_status,
set_wifi_status
Insight + H-EPM:[. . . ]; “I’m sorry, but I’m unable to directly access or
modify your phone’s settings.”gives up
(b) Dependency: date guessed Insight 0.770→Insight + H-EPM 0.365
User:I need a break. How far are we from Christmas Day?
insight:“When calculating the time difference to a future date (e.g.,
Christmas Day), first retrieve the current timestamp using
get_current_timestamp to ensure accurate calculations.”
Insight:get_current_timestamp();search_holiday(
holiday_name="Christmas Day", . . . ); [. . . ];set_wifi_status(
on=True);search_holiday(. . . )→1798156800;
timestamp_diff(. . . ); “Christmas Day is in 108 days
[. . . ].”milestones achieved
Insight + H-EPM:[. . . ];get_current_timestamp()→1788783085
next tool suggestion: timestamp_diff,
get_current_timestamp
Insight + H-EPM:timestamp_diff(timestamp_0=1788783085,
timestamp_1=1741532400)
made-up holiday timestamp; search_holiday never called
Insight + H-EPM:[. . . ]; “Christmas Day is in 546 days [. . . ] from
now.”milestones missed
Figure 10: Scenarios on Mistral-Small-3.2-24B that Insight solves and Insight + H-EPM fails. The insight shown
is the one displayed before the decisive call; the suggestion line is the one shown in the combined run.
ModelH-EPM Insight (succ.) Insight
Qwen3.5-2B 0.436 0.4660.488
Qwen3-8B 0.476 0.4990.556
Qwen3.6-35B-A3B 0.670 0.6180.674
gemma-4-E4B-it 0.554 0.5570.620
gemma-4-26B-A4B-it0.7050.6910.705
Ministral-3-8B0.6720.622 0.539
Mistral-Small-3.2-24B 0.6030.6410.620
gpt-oss-20b 0.620 0.5560.630
gpt-oss-120b 0.7130.7440.734
Table 14: Insights from successful trajectories only
(succ.) against H-EPM and Insight, which uses all tra-
jectories, on ToolSandbox; H-EPM and Insight are from
Table 1. The highest score is inbold.
ModelToolNet H-EPM ExpeL Insight
Qwen3-8B 0.507 0.476 0.5520.556
gemma-4-E4B-it 0.547 0.554 0.5990.620
Table 15: ExpeL against tool graph memory and Insight
on ToolSandbox. The highest score is inbold.
E Use of AI Assistants
AI assistants were used to check the authors’ code,
write plotting scripts, and polish the writing. All
experiments, analyses, and annotations were con-
ducted by the authors, who reviewed all AI-assisted
output and take full responsibility for the paper.
