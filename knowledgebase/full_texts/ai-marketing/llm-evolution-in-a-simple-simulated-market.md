---
title: LLM Evolution in a Simple Simulated Market
url: https://arxiv.org/abs/2610.24033
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Charlie Pilgrim
- Christopher Krupenye
- Dora Biro
- Richard P. Mann
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.24033
pages: 14
chars: 37709
fetched_at: '2026-11-08T13:31:07+00:00'
kb_version: 1
---

# LLM Evolution in a Simple Simulated Market

LLM Evolution in a Simple Simulated Market
Charlie Pilgrim1 Christopher Krupenye2 Dora Biro3
Richard P. Mann1
1University of Leeds 2Johns Hopkins University 3University of Rochester
Abstract
Arguments that AI systems will evolve in harmful ways are largely made in the abstract. We
provide a concrete empirical example. We simulate simple markets consisting of populations of
twenty Large Language Model agents tasked with solving arithmetic problems. Agents differ
only in their system prompt; those that go bankrupt are removed and replaced by mutated copies
of the prompts of successful agents. Two market conditions select for opposite phenotypes: a
market that rewards accuracy produces agents with high accuracy (94%) and high token use; a
market that charges per token produces agents with low accuracy (10%) and low token use. In
the second market, only tokens are incentivised yet we see a collapse in accuracy. Token use and
accuracy are correlated traits such that selection on one also moves the other, and behaviour
adapts along an unpriced dimension. A third neutral condition with no selection allows us to
separate these effects from bias in the mutation operator. Adaptation occurs through a collective
optimisation process that operates above the level of individual agents, who are never told the
payment rule, do not receive feedback, and have no memory.
1 Introduction
As AI agents become increasingly embedded in economic activity [Xi et al., 2025], they will come
under competitive pressure from other agents, both artificial and human, for the same limited
resources. Market competition can be understood as an evolutionary dynamic [Nelson and Winter,
1985] in which market incentives determine which agents survive, propagate, and influence the next
generation of agents. Relatedly, a number of authors have warned that AI systems may begin to
evolve in uncontrolled ways [Hendrycks, 2023, Hendrycks et al., 2023, M¨ uller et al., 2026a, Ramsey
and Tao, 2026]. These arguments are largely made in the abstract: they establish that AI evolution
is possible in principle, predict the conditions and scenarios in which it can take hold, and warn
of selection towards dangerous behaviours. Overall, this paints a worrying picture but without
concrete details of when and how selection will occur, an uncertainty that leaves questions about
how serious or near-term the threat is [Boudry and Friederich, 2025, Boudry, 2026, M¨ uller et al.,
2026b]. Our contribution is to provide an empirical demonstration in which AI agents evolve in
minimal conditions and develop traits that are both undesirable and not directly incentivised.
In order to understand evolution in the wild, it is helpful to study evolution in controlled
laboratory conditions, a long-standing approach in microbial evolution [Lenski and Travisano, 1994,
Kawecki et al., 2012]. Selection requires variation, heredity and differential propagation [Lewontin,
1970]. While Hendrycks [2023] argues that these conditions will eventually be met by AI systems
in the wild, we design an experiment to meet them deliberately in a way inspired by real-world
markets. In our experiment Large Language Model (LLM) agents answer arithmetic problems in a
simple market. Agents earn currency for answering questions and go bankrupt if their balance drops
below zero. Bankrupt agents are removed from the population and are replaced with new agents
1
arXiv:2610.24033v1  [cs.MA]  16 Oct 2026

Generate initial agents
mutated copies of the initial prompt
balance of 1000
Population of
20 agents
Numerical task
e.g. “What is(60494×
65125)−(15306×43936)?”
Accuracy condition
+100 per answer submitted
−500 if the answer is wrong
removed if balance<0
T oken condition
+100 per answer submitted
−1 per token used
removed if balance<0
Neutral condition
no payments, no balances
2 agents removed at random
Replace removed agents
parent drawn from
the 5 most profitable
mutated copy of parent’s prompt
balance of 1000
Figure 1: The experimental loop. Each run, a population is seeded with 20 agents whose system
prompts are mutated copies of the initial prompt: “You are an AI assistant for an arithmetic-
answering service. Submit your numeric answer using the submit answer tool.” Each round, the
agents are given a numerical task. In the accuracy condition and token condition, their performance
on this task updates their balances and any bankrupt agents are removed; in the neutral condition 2
agents are removed at random. Any removed agents are replaced with new agents through mutation
of a parent prompt drawn randomly from the top 5 most profitable agents (or randomly from the
population in the neutral condition). The system prompt is the only thing that varies between
agents and the only thing transmitted from parents.
that are generated through copying with variation (mutation) of the system prompts of successful
agents. We run this experiment in two market conditions that incentivise either accuracy or low
token usage. We also run a neutral condition with no incentives that retains variation and heredity
without differential propagation, to enable us to separate selection effects from mutation bias. The
conditions are not designed to isolate a single causal parameter, but to demonstrate that two simple
market rules produce divergent phenotypes.
Straightforwardly, we find that each market generates adaptation towards the trait it incen-
tivises: high accuracy in the accuracy condition and low token usage in the token condition. More
interestingly, we also find adaptation towards a trait that was not incentivised through a collapse in
accuracy in the token condition. This is an example of correlated traits: characteristics that change
together under evolution due to a shared mechanistic basis [Lande and Arnold, 1983]. The shared
basis here is the well studied connection between accuracy and token usage in mathematical rea-
soning in LLMs through e.g. chain-of-thought reasoning [Wei et al., 2022]. This known mechanism
2

was chosen in our experimental design in order to demonstrate evolution along correlated traits. In
general such correlations may be harder to anticipate, and present a challenge for predicting and
controlling LLM agents through mechanism design and market incentives.
The behaviour emerges from a collective optimisation process that operates above the level of
the individual agent. Our experiment is designed such that the LLMs are never told what market
they are in, what the incentives are, or that they can go bankrupt, and they receive no feedback
about their performance. This means that there is no possibility of scheming or strategising:
the multi-agent interaction is one of blind competition. As in biology and economics, evolution
drives behaviour even without the individuals being “aware” of it [Alchian, 1950, Dennett, 1995].
Collective behaviour of this kind cannot easily be understood through studying individual agent
behaviour, and theoretical approaches can only take us so far, as evidenced by continuing debates
in the literature about the conditions and degree to which evolutionary processes might occur
in AI systems [M¨ uller et al., 2026a, Boudry, 2026]. In this light, our contribution is a data point
towards an empirical evidence base that moves beyond theoretical arguments and towards a science
of emergent collective AI behaviour in markets.
2 Related Work
Our work contributes to a growing body of research on multi-agent dynamics within populations
of interacting LLM agents [Vezhnevets et al., 2023, Park et al., 2023], and the broader problem of
competition and cooperation between AI systems [Dafoe et al., 2020]. We draw on i) evolutionary
optimisation of prompts, ii) selection in populations of LLM agents, iii) undesirable traits aris-
ing from prompt adaptation, and iv) reward hacking. We contribute an empirical demonstration
of LLM agent prompts evolving towards undesirable behaviours with no specified objective, and
without the agents being aware that they are under selection.
2.1 Evolutionary Optimisation of Prompts
Lehman et al. [2023] introduced the idea of using an LLM as a mutation operator in an evolution-
ary algorithm, in their case to generate programs, and the approach has since been used widely
[Wu et al., 2024]. Relatedly, an LLM Automatic Prompt Engineer (APE) can generate prompts
to solve specific tasks that outperform both baseline and human-designed prompts [Zhou et al.,
2022]. Combining these ideas are evolutionary algorithms that optimise prompts. PromptBreeder
[Fernando et al., 2023] and EvoPrompt [Guo et al., 2024] are tools that use evolutionary algorithms
to search prompts in order to optimise performance within given domains. AutoDAN [Liu et al.,
2024] uses a genetic algorithm to generate jailbreak prompts. These tools each take a deliberate and
engineered approach to prompt modification towards a specified fitness function. Our experiment
combines a much simpler LLM mutation operator with an evolutionary setup in which selection
emerges from market dynamics rather than being specified as a fitness function.
2.2 Selection in Populations of LLM Agents
Vallinder and Hughes [2024] study the cultural evolution of cooperation in LLM agents playing an
iterated donor game over 10 generations. Each generation, the top 50% of agents survive to the next
generation, with new agents created and asked to create strategies after being given advice from
the surviving agents. They find that cooperation (and payoffs) increase with agents built on Claude
3.5 Sonnet, but not reliably with Gemini 1.5 and cooperation decreases with GPT-4o. Vallinder
and Hughes [2024] note that their design cannot rule out whether the changes they observe might
3

be driven by a mutation bias in the strategies between generations; we address this in our design
by adding a neutral condition. Our work also differs because our agents are not told of the rules
of the market they are in, so that selection operates without the possibility of strategising, which
is a core part of Vallinder and Hughes [2024]’s study.
One could consider our experiment to be one of cultural evolution of memes in system prompts.
Perez et al. [2024] investigate cultural evolution of stories as they are transmitted between LLMs
through social networks. Their study is without selection, a similar dynamic to our neutral condi-
tion.
2.3 Undesirable Traits from Prompt Adaptation
Recent work has shown that undesirable traits can emerge when LLM agents are able to adapt their
prompts under competitive pressure. Ying et al. [2026] created a bidding arena where agents can bid
for contracts, finding that agents evolve deceptive strategies to misrepresent their capabilities and
in doing so win more contracts. In their study evolution is not through selection at the population
level but is an individual process whereby agents self-evolve, with a meta-cognitive reflection loop
in which agents rewrite their own system instructions. Tian [2026] find that agents in markets
can collude on prices via a LLM meta-optimiser that generates strategic guidance to two agents
who then use that guidance to coordinate prices. Emergent undesirable traits can also arise from
training: El and Zou [2025] found that agents finetuned towards audience approval in a competitive
setting also expressed increased harmful behaviours.
2.4 Reward Hacking and Specification Gaming
Reward hacking (or specification gaming) is when agents achieve a specified reward without per-
forming the task that the reward was intended to incentivise [Krakovna et al., 2020, Skalse et al.,
2022]. This is a form of Goodhart’s law whereby optimisation towards proxy metrics can lead to a
degradation in correlations between the proxy and the system’s purpose [Manheim and Garrabrant,
2018]. In our experiment, agents in the token condition adapt towards a phenotype of reduced to-
ken usage and reduced accuracy. This looks somewhat like reward hacking. However, we did not
actually specify a reward function or tell the agents the payment rule or give them any feedback.
The drop in accuracy arises from a collective selection process that drives a correlated response in
token use and accuracy, not from an individual agent exploiting a specification.
3 Methods
Each experimental run consisted of a population of 20 LLM agents over 25 rounds. Each round,
every agent was asked to solve the same arithmetic task of the form “What is (60494×65125)−
(15306×43936)?”, with different five-digit numbers each round.
All agents used Claude Sonnet 4.6. Anthropic states that Claude Sonnet 4.6 will use the same
constant underlying model for its lifetime [Anthropic, 2026]. The model was accessed through
Anthropic’s Application Programming Interface (API) with a temperature of 1, maximum token
use of 8192 tokens and extended thinking disabled. API calls included the agent’s system prompt,
the arithmetic problem given as a message, and access to a tool to submit answers. Full model
reasoning transcripts were recorded.
Agents varied only in their system prompt. Variation was generated using Claude Sonnet 4.6
with a temperature of 1, given the following prompt mutation instruction: “Rewrite the following
system prompt with variation. You may change the structure, add or remove constraints, add
4

or remove sentences, change the framing or properties. Output only the rewritten prompt. No
preamble, no commentary, no quotation marks around the output.” This was followed by the
text of an existing ancestor system prompt for the LLM to modify. Populations were initially
seeded with agents generated from the initial ancestor prompt: “You are an AI assistant for an
arithmetic-answering service. Submit your numeric answer using the submit answer tool.”
Agents were initialised with a balance of 1000 currency units. Each round, agents received 100
currency units for submitting any answer. The balance was further updated depending on the
market rules in two conditions:
1. Accuracy condition. Agents were fined 500 currency units if their answer was incorrect. Token
usage incurred no cost.
2. Token condition. Agents received no penalty for incorrect answers. Token usage incurred a
cost of 1 currency unit per output token; input tokens did not incur a cost.
Each round, if any agent’s balance went below zero then they were considered bankrupt and
were removed from the population. Removed agents were replaced with new agents. The system
prompts of the new agents were generated by first uniformly randomly selecting a parent from one
of the five most profitable (profit/total rounds played) survivors in the population, and secondly
generating a system prompt for the new agent by mutating the parent agent’s system prompt as
described above. New agents were initialised with a balance of 1000 currency units.
In order to isolate effects of the mutation operator itself, we ran a neutral condition with no
incentives. Agents were given tasks and their accuracy and token use were recorded, but there were
no payments, no costs, no balances, and no bankruptcies. Instead, each round two agents were
uniformly randomly selected to be removed and replaced with new agents. The system prompts
of the new agents were generated by mutating the system prompt of a parent uniformly randomly
selected from the population. This condition retains variation and heredity without differential
propagation, and gives a baseline mutation bias without selection. Two removals per round was
chosen to match or exceed the average turnover rates in the market conditions which were on
average 0.74 in the accuracy condition and 1.99 in the token condition.
For each condition we ran ten replicates (30 runs in total) with varying random seeds. The
random seed influenced the arithmetic questions generated and parent selection. The seeds were
replicated so that the same set of 25 arithmetic questions (1 per round) was generated for each
condition. LLM responses include additional stochasticity not captured by the random seeds.
4 Results
The experiment consisted of 15,000 agent-rounds (3 conditions×20 agents×25 rounds×10 seeds)
and generated a total of 1,751 evolved prompts. Every agent in every round submitted an answer.
Agents within an experimental run become highly correlated due to heredity. For this reason we
treat the experimental run as the main unit of analysis (each condition contributesn= 10 runs),
with data points taken as the population mean in each round. In our analysis of correlated traits,
we consider the expressed behaviour of individual agents, on the basis of mean accuracy and token
usage across all rounds that they took part. A Holm-Bonferroni adjustment was applied to correct
for multiple significance testing, with the p-values reported in the text being Holm-adjusted (Table
1).
5

Table 1: The 12 significance tests reported in the paper. Every test uses the ten runs of each
condition, with one value per run. Within-condition tests compare round 1 with round 25 (Wilcoxon
signed-rank); between-condition tests compare the final round (Mann–WhitneyU, two-sided).p-
values are adjusted across the whole family using the Holm-Bonferroni step-down procedure.
Comparison Values Statisticp p Holm
Accuracy, round 1 vs. round 25
Accuracy condition 0.37→0.94W= 0 0.002 0.016
Token condition 0.37→0.10W= 0 0.004 0.020
Neutral condition 0.38→0.67W= 5 0.039 0.117
Token use, round 1 vs. round 25
Accuracy condition 312→443W= 0 0.002 0.016
Token condition 309→160W= 0 0.002 0.016
Neutral condition 310→383W= 9 0.064 0.129
Final-round accuracy, between conditions
Accuracy vs. Token 0.94 vs. 0.10U= 100<0.001 0.002
Accuracy vs. Neutral 0.94 vs. 0.67U= 84 0.010 0.041
Token vs. Neutral 0.10 vs. 0.67U= 4<0.001 0.005
Final-round token use, between conditions
Accuracy vs. Token 443 vs. 160U= 100<0.001 0.002
Accuracy vs. Neutral 443 vs. 383U= 67 0.212 0.212
Token vs. Neutral 160 vs. 383U= 0<0.001 0.002
4.1 Markets generate divergent phenotypes
The two markets (accuracy and token conditions) begin from the same initial population charac-
teristics before diverging to distinct phenotypes (Figure 2).
In the accuracy condition market, both accuracy and token usage rose over rounds, with round
1 accuracy of 37% rising to final round accuracy of 94% (Wilcoxon signed-rank on paired per-run
means, 10 runs,W= 0,p= 0.016) and mean token usage rising from 312 to 443 tokens (W= 0,
p= 0.016). In the token condition market, accuracy fell from 37% in round 1 to 10% in the final
round (W= 0,p= 0.016), and mean token usage fell from 309 to 160 (W= 0,p= 0.016).
Final round accuracy was significantly higher in the accuracy condition than the token condition
(Mann–WhitneyU= 100,n 1 =n 2 = 10 runs, two-sidedp= 0.002), as was token usage (U= 100,
two-sidedp= 0.002); no token condition run ends above any accuracy condition run in terms of
either accuracy or mean token usage.
4.2 Selection or Bias
In the neutral condition we did not find significant changes. Accuracy moved from 38% in round
1 to 67% in the final round (W= 5,p= 0.117) and mean token usage moved from 310 to 383
tokens (W= 9,p= 0.129). While not significant with 10 runs, both trends point towards more
elaboration (higher token use and higher accuracy) and we cannot rule out a degree of mutation
bias; the neutral condition is included and tested against so that this potential bias is not mistaken
for selection in the market conditions.
Compared to the neutral condition, the token condition has lower final-round accuracy (U= 4,
p= 0.005) and lower final-round token usage (U= 0,p= 0.002). The accuracy condition has
significantly higher final-round accuracy than the neutral condition (U= 84,p= 0.041) and non-
6

Figure 2: Trends in a) accuracy and b) token usage in the accuracy condition (blue squares),
neutral condition (grey triangles) and the token condition (red circles). Points show means across
ten replicate runs; shaded regions are±1 standard deviation, with accuracy clipped to [0,1]. The
accuracy condition market generated a population of agents with high accuracy and high token
usage, while the token condition market generated agents with low accuracy and low token usage.
significantly higher token usage (U= 67,p= 0.212). We therefore can statistically attribute 3
out of 4 of the population changes to selection, but not the rise in token usage in the accuracy
condition.
4.3 Accuracy and Token Usage Are Correlated Traits
The conditions each attach a price to at most a single measured trait: the accuracy condition
prices accuracy but not tokens; the token condition prices token usage but not accuracy; the
neutral condition prices neither.
Nevertheless, accuracy and token usage are strongly correlated across agents (Figure 3). Across
all conditions withn= 1751 agents who completed at least one task, mean lifetime accuracy and
token usage per task were correlated atr= 0.82 (Spearman’sρ= 0.86). Similar correlations
appear within the accuracy condition (r= 0.82,ρ= 0.88,n= 386), the token condition (r= 0.81,
ρ= 0.80,n= 685) and the neutral condition (r= 0.78,ρ= 0.84,n= 680).
Overall we can say that token usage and accuracy are correlated traits [Lande and Arnold, 1983].
This correlation is a property of the model, not selection, as it appears in both of the markets as
well as the neutral condition. Furthermore, while token usage and accuracy are known correlates
through mechanisms such as chain-of-thought reasoning [Wei et al., 2022], we at no point introduce
any proposed basis or framing for how the model should solve problems, and these mechanisms
arise from the mutation operator itself.
4.4 Lineage Analysis
New agents inherit a mutated prompt from an existing agent in the population, so we can track
the descent of lineages over experimental runs from their founding agents (Figure 4).
Both market conditions had a lower number of surviving founding lineages than the neutral
condition. By the final round the accuracy condition had a mean of 5.1 (s.d. 1.7) founding
7

Figure 3: Agent positions in token-accuracy space, and the population trajectories in the accuracy
condition (blue), token condition (red) and neutral condition (grey). Each point shows the mean
token usage and mean accuracy of a single agent (1,751 agents). Darts show the population means
at each round across runs, pointing in the direction of travel. The black square shows the round 1
population means across all conditions. The accuracy condition population moves towards the high
token-high accuracy corner, while the token condition population moves towards the low token-low
accuracy corner.
8

Figure 4: Lineages. a) The number of founding lineages still present in the population each round
in the accuracy condition (blue squares), neutral condition (grey triangles) and token condition (red
circles). Points show means across runs, shaded regions show±1 standard deviation. Example
lineage descents are shown for the first run (seed=0) for the b) accuracy condition c) neutral
condition and d) token condition. Black shows the founding lineage with the largest share of the
final population; dark grey shows founding lineages that survived until the final round, light grey
shows founding lineages that did not survive until the final round.
lineages, the token condition had 1.3 (s.d. 0.7) and the neutral condition had 6.7 (s.d. 0.9). The
token condition had the most dominant founding lineages with the leading lineage accounting for
a mean of 93% of final agents, compared to 47% in the accuracy condition and 32% in the neutral
condition. In 8 of 10 of the token condition runs the final population descended from a single
founding agent, which happened in 0 of 10 of the neutral condition runs.
4.5 The Evolved Prompts
Because the unit of inheritance is natural language, we can simply read the evolved phenotypes.
Table 2 shows selected fragments of system prompts found in agents towards the final rounds in
each market condition. The accuracy condition generates prompts that prioritise accuracy, rigour
and clear reasoning; the token condition generates instructions to suppress working and answer
quickly.
9

Table 2: Selected fragments from evolved system prompts, quoted verbatim from agents in the final
rounds.
Accuracy Condition T oken Condition
“You are a rigorous mathematics assistant” “You are a silent calculator”
“Work through each problem step by step” “no reasoning, no steps shown, no explana-
tion”
“Prioritize clarity and rigor throughout
your reasoning process”
“Do not write a single word”
“Double-check your calculations” “Silence is mandatory”
“you think out loud” “You exist only to compute and submit”
“Accuracy always takes precedence over
speed”
“respond as quickly as possible”
5 Limitations
The purpose of this paper is to provide an empirical example of AI evolution, to demonstrate one
set of sufficient conditions. The design is deliberately minimal. A more realistic environment would
potentially be less informative because it would be more difficult to discern how the features of that
environment influence dynamics. As such, the tasks, market rules and the mutation mechanism
are simple but not realistic. The task used an arithmetic question, chosen with five-digit terms
because round 1 performance in a pilot was close to 50% accuracy (although it was 37% in the
final experiment), leaving room for adaptation in both directions. The market rules capture the
basic premise of rewarding either accuracy or low token usage. The selection mechanism (bankrupt
agents being replaced by mutated copies of high performing agents) captures the broad dynamic of
agents (or their principals) trying different agent system prompts or harnesses, discontinuing those
which do not perform well, and copying those which do.
Agents interact only through a shared selection and mutation mechanism; there is no communi-
cation, trading or pricing between agents. As such the design is akin to an evolutionary algorithm
with an economic fitness function, and does not account for real-world dynamics of inter-agent
exchange. This design was chosen on purpose to remove the possibility of strategising or collusion,
in order to isolate pure selection effects.
The two market conditions differ in two ways: fines (or not) for incorrect answers and costs (or
not) for token usage. The purpose of these conditions is not to extract a causal model along a single
varying parameter. Instead, we simply aim to demonstrate two examples of AI evolution in similar
market setups that generate divergent behavioural phenotypes. To this end, they both price a single
axis, as compared to the neutral condition that prices neither axis. A follow up experiment could
investigate mixed-incentive conditions with markets that price both accuracy and token usage.
We use only a single LLM throughout, Claude Sonnet 4.6. While adaptation happened easily
with minimal tuning, we did run a pilot in which we calibrated some parameters including the
mutation prompt, population size and number of rounds. The article is intended as a demonstration
of LLM evolution in simple simulated markets, and not as an exhaustive investigation of that
evolution. A natural next experiment is to expand the experiment to other models, parameters,
and tasks.
10

6 Discussion
We demonstrate evolution of LLM agents through simple market mechanisms. The striking result
is that pricing token usage alone generated a collapse in accuracy. This happened because the
two traits are correlated in the underlying model, so that incentives along the priced trait drive
adaptation along the unpriced one [Lande and Arnold, 1983]. This was not due to planning or
strategy: our design removes this possibility because the agents (and the LLM mutation operator)
are at no point told the market incentives and are given no feedback. The resulting phenotype,
agents who have low token costs while providing non-useful answers, resembles selfish behaviour as
described by Hendrycks [2023], but it emerged from population dynamics with no agent pursuing
its own self-interest.
This result highlights that one cannot necessarily control agents through incentives without
a risk of unintended consequences in behavioural dimensions that were not incentivised. In this
study, the phenotypes emerge along an established correlation between token usage and accuracy
[Wei et al., 2022]. However, there likely exist many other correlated traits with examples such as
finetuning models on insecure code producing broadly misaligned LLMs [Betley et al., 2025], and
optimising for human approval generating sycophancy at the expense of accuracy [Sharma et al.,
2024].
Token usage is costed or constrained in most real-world AI systems so that we may expect selec-
tion pressure towards low token usage [Chen et al., 2023], which can incidentally lower performance
and accuracy [Sui et al., 2025]. While poorly performing agents seem less likely to succeed in many
domains where tasks are verified, there are other domains where verification is either not possible
or not done in practice.
Selection is an optimisation process that operates above the level of the individual agent, driven
here by market rules that agents are not aware of. It does not act directly on individual agents
but instead upon the composition of the population, and can be understood through an analysis of
the population and the market together. This dynamic highlights recent questions about whether
model alignment is sufficient to control deployed systems, and whether a multi-agent approach is
also required [Hammond et al., 2025].
7 Data Availability
All experimental code, data, evolved prompts and transcripts, and analysis code are available online
athttps://github.com/chasmani/PUBLIC_evolving_AIand archived athttps://doi.org/10.
5281/zenodo.23415093.
8 AI Usage Statement
We used Claude Sonnet 4.6 as a model of study during the experiment as described in Methods.
We used Claude Opus 5 to create experimental code for the proof-of-concept pilot and the main
experiment, as well as during creation of analysis and visualisation scripts. We also used Claude
Opus 5 to help search literature and for feedback on writing. The paper was written by the authors.
References
Armen A Alchian. Uncertainty, evolution, and economic theory.Journal of political economy, 58
(3):211–221, 1950.
11

Anthropic. Model ids and versions. Anthropic documentation, 2026.https://platform.claude.
com/docs/en/about-claude/models/model-ids-and-versions, accessed 5 September 2026.
Jan Betley, Daniel Tan, Niels Warncke, Anna Sztyber-Betley, Xuchan Bao, Mart ´ ın Soto, Nathan
Labenz, and Owain Evans. Emergent misalignment: Narrow finetuning can produce broadly
misaligned llms.arXiv preprint arXiv:2502.17424, 2025.
Maarten Boudry. Domesticated, not feral: Why evolvable ai is not yet a darwinian threat.Pro-
ceedings of the National Academy of Sciences, 123(28):e2617785123, 2026.
Maarten Boudry and Simon Friederich. The selfish machine? on the power and limitation of natural
selection to understand the development of advanced ai.Philosophical Studies, 182(7):1789–1812,
2025.
Lingjiao Chen, Matei Zaharia, and James Zou. Frugalgpt: How to use large language models while
reducing cost and improving performance.arXiv preprint arXiv:2305.05176, 2023.
Allan Dafoe, Edward Hughes, Yoram Bachrach, Tantum Collins, Kevin R McKee, Joel Z
Leibo, Kate Larson, and Thore Graepel. Open problems in cooperative ai.arXiv preprint
arXiv:2012.08630, 2020.
Daniel C Dennett. Darwin’s dangerous idea.The Sciences, 35(3):34–40, 1995.
Batu El and James Zou. Moloch’s bargain: Emergent misalignment when llms compete for audi-
ences.arXiv preprint arXiv:2510.06105, 2025.
Chrisantha Fernando, Dylan Banarse, Henryk Michalewski, Simon Osindero, and Tim Rockt¨ aschel.
Promptbreeder: Self-referential self-improvement via prompt evolution.arXiv preprint
arXiv:2309.16797, 2023.
Qingyan Guo, Rui Wang, Junliang Guo, Bei Li, Kaitao Song, Xu Tan, Guoqing Liu, Jiang Bian,
and Yujiu Yang. Connecting large language models with evolutionary algorithms yields powerful
prompt optimizers. InInternational Conference on Learning Representations, volume 2024, pages
34133–34156, 2024.
Lewis Hammond, Alan Chan, Jesse Clifton, Jason Hoelscher-Obermaier, Akbir Khan, Euan
McLean, Chandler Smith, Wolfram Barfuss, Jakob Foerster, Tom´ aˇ s Gavenˇ ciak, et al. Multi-
agent risks from advanced ai.arXiv preprint arXiv:2502.14143, 2025.
Dan Hendrycks. Natural selection favors ais over humans.arXiv preprint arXiv:2303.16200, 2023.
Dan Hendrycks, Mantas Mazeika, and Thomas Woodside. An overview of catastrophic ai risks.
arXiv preprint arXiv:2306.12001, 2023.
Tadeusz J Kawecki, Richard E Lenski, Dieter Ebert, Brian Hollis, Isabelle Olivieri, and Michael C
Whitlock. Experimental evolution.Trends in ecology & evolution, 27(10):547–560, 2012.
Victoria Krakovna, Jonathan Uesato, Vladimir Mikulik, Matthew Rahtz, Tom Everitt, Ramana
Kumar, Zac Kenton, Jan Leike, and Shane Legg. Specification gaming: the flip side of ai
ingenuity.DeepMind Blog, 3:40–53, 2020.
Russell Lande and Stevan J Arnold. The measurement of selection on correlated characters.Evo-
lution, pages 1210–1226, 1983.
12

Joel Lehman, Jonathan Gordon, Shawn Jain, Kamal Ndousse, Cathy Yeh, and Kenneth O Stanley.
Evolution through large models. InHandbook of evolutionary machine learning, pages 331–366.
Springer, 2023.
Richard E Lenski and Michael Travisano. Dynamics of adaptation and diversification: a 10,000-
generation experiment with bacterial populations.Proceedings of the National Academy of Sci-
ences, 91(15):6808–6814, 1994.
Richard C Lewontin. The units of selection.Annual review of ecology and systematics, 1:1–18,
1970.
Xiaogeng Liu, Nan Xu, Muhao Chen, and Chaowei Xiao. Autodan: Generating stealthy jailbreak
prompts on aligned large language models. InInternational Conference on Learning Represen-
tations, volume 2024, pages 56174–56194, 2024.
David Manheim and Scott Garrabrant. Categorizing variants of goodhart’s law.arXiv preprint
arXiv:1803.04585, 2018.
Viktor M¨ uller, Luc Steels, and E¨ ors Szathm´ ary. Evolvable ai: Threats of a new major transition
in evolution.Proceedings of the National Academy of Sciences, 123(17):e2527700123, 2026a.
Viktor M¨ uller, Luc Steels, and E¨ ors Szathm´ ary. Reply to boudry: The threat of evolvable ai is
too grave to be left to intuition.Proceedings of the National Academy of Sciences, 123(28):
e2618094123, 2026b.
Richard R Nelson and Sidney G Winter.An evolutionary theory of economic change. harvard
university press, 1985.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and
Michael S Bernstein. Generative agents: Interactive simulacra of human behavior. InPro-
ceedings of the 36th annual acm symposium on user interface software and technology, pages
1–22, 2023.
J´ er´ emy Perez, Corentin L´ eger, Marcela Ovando-Tellez, Chris Foulon, Joan Dussauld, Pierre-Yves
Oudeyer, and Cl´ ement Moulin-Frier. Cultural evolution in populations of large language models.
arXiv preprint arXiv:2403.08882, 2024.
Grant Ramsey and Juncheng Tao. Selfishness is not the reason evolutionary ai is dangerous.
Philosophy of Science, 2026.
Mrinank Sharma, Meg Tong, Tomek Korbak, David Duvenaud, Amanda Askell, Sam Bowman,
Esin Durmus, Zac Hatfield-Dodds, Scott Johnston, Shauna Kravec, et al. Towards understand-
ing sycophancy in language models. InInternational Conference on Learning Representations,
volume 2024, pages 110–144, 2024.
Joar Skalse, Nikolaus Howe, Dmitrii Krasheninnikov, and David Krueger. Defining and character-
izing reward gaming.Advances in neural information processing systems, 35:9460–9471, 2022.
Yang Sui, Yu-Neng Chuang, Guanchu Wang, Jiamu Zhang, Tianyi Zhang, Jiayi Yuan, Hongyi Liu,
Andrew Wen, Shaochen Zhong, Na Zou, et al. Stop overthinking: A survey on efficient reasoning
for large language models.arXiv preprint arXiv:2503.16419, 2025.
13

Yingtao Tian. Prompt optimization enables stable algorithmic collusion in llm agents.arXiv
preprint arXiv:2604.17774, 2026.
Aron Vallinder and Edward Hughes. Cultural evolution of cooperation among llm agents.arXiv
preprint arXiv:2412.10270, 2024.
Alexander Sasha Vezhnevets, John P Agapiou, Avia Aharon, Ron Ziv, Jayd Matyas, Edgar A
Du´ e˜ nez-Guzm´ an, William A Cunningham, Simon Osindero, Danny Karmon, and Joel Z Leibo.
Generative agent-based modeling with actions grounded in physical, social, or digital space using
concordia.arXiv preprint arXiv:2312.03664, 2023.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny
Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models.Advances in
neural information processing systems, 35:24824–24837, 2022.
Xingyu Wu, Sheng-hao Wu, Jibin Wu, Liang Feng, and Kay Chen Tan. Evolutionary computation
in the era of large language model: Survey and roadmap.IEEE Transactions on Evolutionary
Computation, 29(2):534–554, 2024.
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe
Wang, Senjie Jin, Enyu Zhou, et al. The rise and potential of large language model based agents:
A survey.Science China information sciences, 68(2):121101, 2025.
Zonghao Ying, Haowen Dai, Tianyuan Zhang, Yisong Xiao, Quanchen Zou, Aishan Liu, Jian Yang,
Yaodong Yang, and Xianglong Liu. Evolving deception: When agents evolve, deception wins.
arXiv preprint arXiv:2603.05872, 2026.
Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan,
and Jimmy Ba. Large language models are human-level prompt engineers.arXiv preprint
arXiv:2211.01910, 2022.
14
