---
title: Is AI Widening the Wage Gap? A Hybrid Agentic Simulation for Labor Equity
url: https://arxiv.org/abs/2609.33367
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Zhongbo Hu
- Zonghang Wu
- Georgina Curto
- Aocheng Tang
- Yilei Shao
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.33367
pages: 12
chars: 61801
fetched_at: '2026-11-08T13:21:19+00:00'
kb_version: 1
---

# Is AI Widening the Wage Gap? A Hybrid Agentic Simulation for Labor Equity

Is AI Widening the Wage Gap? A Hybrid Agentic Simulation for
Labor Equity
Zhongbo Hu
Shanghai AI-Finance School, East
China Normal University
Shanghai, China
Zonghan Wu
Shanghai AI-Finance School, East
China Normal University
Shanghai, China
Georgina Curto
United Nations University Institute in
Macau
Macau, China
Aocheng Tang
Shanghai AI-Finance School, East
China Normal University
Shanghai, China
Yilei Shao
Shanghai AI-Finance School, East
China Normal University
Shanghai, China
Abstract
Artificial intelligence (AI) is reshaping labor markets, yet its effects
on wage distribution remain insufficiently understood. Conven-
tional analytical approaches are limited in their ability to directly
examine the dynamic evolution of worker behavior and income
distribution under sustained AI shocks and counterfactual policy
scenarios. To address this limitation, we present a hybrid agentic
framework, which aims to overcome the challenges of scalability
and replicability of rule-based models and the limited explainability
in LLM-agentic frameworks. Using a hybrid approach and sociode-
mographic data from China, we simulate and interpret changes
in wage distribution under repeated AI shocks in the labor mar-
ket. The results show that both the average-wage ratio between
workers in the top and bottom income deciles (T10/B10) and the
Gini coefficient increase persistently, suggesting that AI shocks
widen the wage gap and exacerbate income inequality. This pat-
tern of a widening wage gap remains robust across alternative
large language model decision engines and 30 Monte Carlo sim-
ulations. We further conduct counterfactual policy experiments.
The results show that education subsidies targeted at low-income
workers increase both the number of skill-upgrading attempts and
the number of successful upgrades, with particularly pronounced
improvements in the upskilling success probability of workers in
the bottom income decile. These effects enable the policy to par-
tially mitigate wage inequality. The proposed framework provides
an interpretable, scalable, and replicable simulation approach for
examining the impact of AI shocks on wage distribution. It also
offers policymakers a complementary analytical tool for evaluating
policy interventions.
Keywords
Artificial intelligence, Wage gap, Labor markets, Social Simulations,
Education subsidy policy
1 Introduction
With the advent of Large Language Models (LLMs), Artificial In-
telligence (AI) has become pervasively integrated across diverse
socio-economic sectors. The involvement of AI has significantly
enhanced labor productivity, prompting producers to adopt AI tech-
nologies on an extensive scale. Although the impact of AI varies
across different fields and industries, the potential risk of increased
unemployment remains a major concern for the workforce[ 28].
Existing research suggests that in the current labor market, the
augmentation effect of AI on occupations outweighs its substitu-
tion effect[2, 11]. Nevertheless, it is undeniable that the application
of automation technologies, such as AI-assisted office tools, has
displaced numerous job positions. More granular studies indicate
that AI exerts both substitution and complementary effects on job
roles. In positions characterized by task substitution, specifically,
the wage growth rate of workers is systematically lower than in
positions where AI plays a complementary role [3]. Despite diverse
investigations into AI’s impact on the labor market, few scholars
have focused on the issue of the AI-induced wage gap. Furthermore,
conventional macroeconomic indicators, such as unemployment
and aggregate inflation, as well as traditional methods such as rule-
based ABMs and regression analysis, may not fully capture the
dynamic evolution of this phenomenon. Consequently, three crit-
ical questions arise. First, does sustained AI exposure widen the
wage gap among workers. Second, if wage disparities widen, what
policy instruments can partially mitigate this effect. Third, how can
these dynamics be effectively modeled and characterized.
Agentic frameworks provide a suitable environment for evaluat-
ing the questions outlined above and constitute a valuable method-
ological approach for public policy research. In social simulation
research, agent behavior is traditionally specified through explicitly
programmed rules, giving rise to what are commonly referred to
as agent-based models (ABMs) [15]. ABMs have a long tradition
in computer science [ 32] and are predominantly rule-driven or
bounded-rational decision rules to govern agents’ behavior and
interactions[14, 24, 31]. Such rules may characterize the needs and
motivations of individual agents [ 5] or represent external envi-
ronmental conditions, such as geographical settings [33] or policy
environment[16]. As Macal and North [25] suggests, incorporating
multiple conditions and behavioral rules is often necessary to cap-
ture the growing complexity of real-world social environments. For
example, labor-market simulations may require rules governing
firms’ hiring and firing decisions, workers’ job search, worker–firm
matching, and wage determination.
By simulating social interactions and behavioral responses, ABMs
provide a framework for assessing the impact of environmental
change and policy interventions [10]. One of their principal strengths
lies in their transparency, as researchers can directly observe the
rules governing agent behavior and trace the processes through
Correspondence to: yileishao@sem.ecnu.edu.cn
arXiv:2609.33367v3  [cs.CY]  20 Oct 2026

which aggregate outcomes emerge. Nevertheless, conventional
ABMs also face important limitations. In such models, agent be-
havior is largely determined by predefined rules, which can limit
behavioral flexibility and adaptability as the complexity of the
environment and the range of possible behaviors increase. Pre-
determined rules may not adequately capture the evolving and
context-dependent nature of social environments, and models de-
veloped for one institutional or cultural setting may not be readily
transferable to another.
The emergence of large language models (LLMs) has partially al-
leviated these limitations and stimulated the development of a wide
range of LLM-based agentic frameworks. Trained on massive tex-
tual corpora, LLMs exhibit certain human-like language capabilities
and can generate plausible context-sensitive responses to chang-
ing and complex environmental conditions [ 39]. LLM-powered
agents can therefore represent human-like social interactions and
behaviors [30], offering new technical possibilities for social sci-
ence research and policy analysis. For example, Ashery et al. [7]
leveraged interactions among LLM-powered agents to examine
the emergence of collective social phenomena. Their experiments
show that repeated local interactions can lead agent populations
to spontaneously develop shared social conventions, collective bi-
ases, and tipping-point dynamics. However, the stand-alone use
of LLMs also entails substantial limitations, including hallucinated
decisions [4], logical inconsistency [13], and limited transparency
and reproducibility [34].
Although a growing body of research has examined LLM-powered
agents in social contexts [ 23, 29], both conventional rule-based
ABMs and stand-alone LLM-based models exhibit significant short-
comings. Meanwhile, wage determination and income distribution
in labor economics constitute another important area in which
agentic approaches can generate valuable insights. To address these
limitations, we develop a hybrid framework that combines explicit
rules with LLM-based decision-making and apply it to investigate
how AI shocks affect the wage gap. Within our framework, explicit
rules and LLM-based decision-making play distinct but complemen-
tary roles. Specifically, at the aggregate level, the labor-market envi-
ronment is governed by a transparent rule-based structure, whereas
individual workers are represented by heterogeneous agents whose
behavioral decisions are generated by an LLM. By structuring agent
attributes and states—including age, occupation, and learning ca-
pacity—the framework enables LLM-powered agents to exhibit
behavioral heterogeneity and respond to qualitative and context-
dependent conditions in ways that are difficult to reproduce using
predetermined rules alone. At the same time, the explicit rules
governing the broader labor-market environment enhance the in-
terpretability and traceability of an otherwise opaque LLM-agent
system, particularly in simulations involving large-scale interac-
tions among agents [38].
The contributions of this research are threefold: (1) It presents a
hybrid agentic methodology that integrates rule-based and LLM-
based approaches, enhancing the scalability of rule-based mod-
els and the explainability of LLM-based models. (2) Relying on
this framework, we offer empirical evidence that continuous AI
shocks induce asymmetric wage distributional effects. (3) We utilize
this framework to evaluate education subsidy policy interventions
aimed at mitigating AI-induced wage polarization. By tracking how
these interventions influence individual agent behavior and aggre-
gate wage distribution, we provide policymakers with an effective
analytical tool to evaluate policies that aim to mitigate inequity in
the AI era.
2 Methodology
2.1 Overall Hybrid Simulation Model
AI-driven wage gap is a distributional problem that unfolds through
individual-level labor-market decisions, aggregated across hetero-
geneous workers. Studying it requires a model that can (i) repre-
sent the overall labor market and individual behavior, (ii) repre-
sent worker heterogeneity along multiple dimensions, (iii) generate
qualitative strategic choices that respond to each worker’s spe-
cific circumstances, and (iv) produce outcomes measured with the
T10/B10 wage ratio (Ratio) to evaluate the wage gap. This section
describes the methodology we use to meet these requirements with
a hybrid agentic framework in which a rule-based labor-market
environment is coupled with an LLM-driven individual agent’s
decision engine. The integrated simulation pipeline is illustrated
in Figure 1. The agents represent the different profiles of workers,
according to their demographics. Environmental factors (including
AI shocks and policies to mitigate wage polarization) influence the
LLM-ruled behavior of agents, towards the status of "upgrade", "mi-
grate", "resist", or "exit" the labor market. The outcome of the agents’
behavior change is measured with a wage inequality (T10/B10) ratio
indicator.
Overall, our simulation proceeds in three stages. First, we con-
struct the initial agent population by assigning each agent a set
of sociodemographic and labor-market attributes. Here, initializa-
tion refers to assigning agents their starting sociodemographic and
labor-market attributes at t=0 (Round 0). Some attributes, such as
age cohort and adaptive elasticity, remain fixed throughout the
simulation, whereas others, such as wages and employment status,
evolve dynamically. Aggregate indicators, including the unemploy-
ment rate and the Gini coefficient, are subsequently calculated from
the evolving agent-level states. Initialization takes place before the
simulation formally begins and therefore involves no LLM-based
decision-making, AI shocks, or subsequent changes in agents’ be-
havioral states and aggregate labor-market outcomes. Second, once
the simulation begins, the LLM-based agents make decisions based
on the environmental information available to them, leading to
dynamic changes in their employment states and wages. GLM-4-
Flash serves as the primary LLM decision engine, while Llama 3.1,
Qwen3, and DeepSeek-V4 (DS) are used as alternative decision en-
gines to assess the robustness of the simulation results. Third, the
wage outcomes of all agents are aggregated to calculate macro-level
indicators, including wage ratios and the Gini coefficient.
At the beginning of the simulation, we initialize 1,000 agents
using sociodemographic data for China, primarily obtained from
the National Bureau of Statistics of China (detailed descriptions
of the data sources are provided insupplementary material). The
sociodemographic data covers aggregate labor market conditions,
demographic composition, occupation-specific wages, and the dis-
tribution of AI exposure across occupations. Although our model
is empirically grounded in real-world data, it may still be subject

Labor Market Simulation Framework (Rule-based Population Dynamics)
Environment
AI AI Shocks
Policies
Economic
Conditions
⋮
Agent-based Simulation (One Round)
1. Agent Proﬁle
Demographics
Occupation
AI Exposure
Wage
…
2. Agents’ Behavior
(LLM-based)
LLM Decision
↑Upgrade Skill
→Migrate
=Resist / Remain
×Exit Market
…
3. State Transition
(Rule-based)
Wage Update
Occupational Adjustment
Wage Reduction
Employment Status
…
Input Observation
(st)
Action
(at)
Output
Labor Market Metrics
Wage Inequality
(T10 / B10)
Top 10% vs Bottom 10%
wage ratio per round
Gini Coefﬁcient
Praticipation Rate
Average Wage
…
Next Round t + 1
Repeat until T rounds (e.g., 1 round = 1 year)
Data Flow Information Flow Feedback Loop stObservation at round tatAction at round t
Figure 1: This figure illustrates the overall simulation pipeline. Under external conditions, including AI shocks, policies,
and economic conditions, the LLM serves as the decision-making engine, generating decisions such as skill upgrading and
occupational migration based on each agent’s individual state (e.g., demographics and occupation) and the external environment.
Rule-based state-transition mechanisms then update wages, occupations, and employment status. Finally, labor-market
outcomes, including the wage inequality measure (T10/B10) and the Gini coefficient, are calculated. Repeated simulation rounds
are conducted to capture the dynamic evolution of wage distribution under AI shocks.
to certain biases in its initialization. To assess how closely the ini-
tialized model and data reproduce the real-world data, we compare
the model-initiated outputs with their corresponding sociodemo-
graphic data. The results indicate that the initialized model closely
matches the sociodemographic data: the absolute deviations for all
proportion-based indicators are within 5 percentage points, while
the relative deviations for all wage-related indicators are below 5%,
with a maximum deviation of 4.7%. Detailed comparison results are
reported in Appendix B.
Furthermore, we formulate the simulation as a discrete-time
systemM, defined as follows:
M=⟨N,E,S,A,𝑓,𝑇⟩,(1)
whereN={ 1, 2, 3,... 𝑁} is the set of worker agents, and we set
the number of agents to N=1000. E denotes the environmental
state, which comprises the aggregate unemployment rate and the
current simulation round;S={𝑠 𝑖,𝑡}𝑁 𝑖=1 denotes the collection of
individual agent states and attributes at simulation round t.A de-
notes the action space, which includes occupational transitions
and employment decisions, with each occupation associated with a
corresponding level of AI exposure.𝑓:S×E×A→S is the state
transition function governed by the LLM, which functions as the
agents’ behavioral engine to determine state updates based on pre-
vious and current conditions and environmental shocks(AI shock
and policy intervention).𝑇 is the simulation horizon in rounds. One
round in the simulation is defined as a year in real-world time. The
above definition also indicates that our model can be further ex-
tended, for example, by incorporating firm and government agents
to form a multi-agent model that captures the interactions among
different labor-market actors and their resulting effects
2.2 Agentic demographics
In the labor market, different types of occupations are associated
with corresponding wage levels. In our framework,Routinerefers
to occupations characterized by standardized, rule-based, and repet-
itive tasks.Manualrefers to occupations involving non-routine
physical tasks that typically require physical presence, spatial judg-
ment, sensory perception, or physical skills.Cognitiverefers to
occupations involving non-routine cognitive tasks that rely on spe-
cialized knowledge, reasoning, creativity, analysis, and judgment.
Managerialrefers to occupations centered on managerial decision-
making, resource allocation, cross-team coordination, and strategic
judgment. In general, workers inManagerialoccupations tend to
earn higher wages than those inRoutineoccupations. With the
rapid development of AI, technological advances may affect work-
ers’ wages by displacing or transforming existing jobs. Workers
facing such technological displacement may exit employment or
transition to other occupations, thereby generating fluctuations in
their earnings. To capture these labor-market dynamics, we model a
single labor market with four occupational types—Routine, Manual,
Cognitive, and Managerial—and three levels of AI exposure (Low,
Medium, High), yielding twelve occupation-exposure cells. There
is no product market or financial market. Accordingly, our model
does not explicitly model the interaction between labor supply and
labor demand; instead, it focuses on the effects of AI shocks on
wage inequality among workers.
Although our analysis focuses exclusively on the labor mar-
ket, it remains a highly complex system. To more closely represent
labor-market dynamics under AI shocks and the states of individual
agents, we assign each agent a set of sociodemographic attributes.
Each agent𝑖 is initialized by sampling the attributes𝑔𝑖,𝑜𝑖,𝑎𝑖,𝑒𝑖,𝑤𝑖,

𝜌𝑖, and𝑟𝑖 from the corresponding distributions reported in thesup-
plementary material.Each agent𝑖 is characterized by a state vector
𝑠𝑖 =(𝑔 𝑖,𝑎 𝑖,𝑜 𝑖,𝑒 𝑖,𝑤 𝑖,𝜌 𝑖,𝑟 𝑖,ℎ 𝑖), where𝑔𝑖 denotes the age cohort;𝑎𝑖
denotes the AI exposure level, reflecting the extent to which the
agent’s occupation is exposed to AI-related technological change.𝑜𝑖
denotes the occupation; 𝑒𝑖 ∈{ 0, 1} denotes the employment in-
dicator;𝑤𝑖 denotes the annual wage measured in Chinese yuan
(RMB) (See Section 2.2 for details);𝜌𝑖 denotes the adaptive elasticity
reflecting the ability to learn new skills and adapt to changes in the
work environment.𝑟𝑖∈{ 0, 1} denotes retirement eligibility and
is specified as a binary parameter applicable only to agents in the
50–59 age cohort. This specification reflects gender differences in
China’s statutory retirement ages. Because our simulation does not
explicitly distinguish between male and female agents, we do not
assign a uniform retirement age to all agents. Instead, we allow
retirement to occur within the 50–59 age cohort to approximate
the heterogeneity in retirement timing between male and female
workers.ℎ𝑖 denotes the action-history buffer. The attributes𝑔𝑖,𝜌𝑖,
and𝑟𝑖 are assigned at initialization and remain fixed throughout the
simulation, as they represent agents’ initial endowments, including
age, adaptive elasticity, and retirement probability. In contrast,𝑎𝑖,
𝑒𝑖,𝑤𝑖, andℎ𝑖 evolve endogenously over the course of the simulation
in response to agents’ actions. Since an agent’s state is determined
by multiple parameters, each agent is inherently heterogeneous.
Employment status.In real-world labor markets, re-employment
following job loss typically involves job search, job matching, and
skill adjustment, resulting in a time lag between unemployment and
re-employment. Given that this study focuses on the dynamic evo-
lution of wage inequality under AI shocks rather than short-term
employment matching, we do not consider intra-round employ-
ment transitions. Specifically, agents who lose their jobs in a given
year cannot be re-employed within the same year. At the same
time, the initial employment status of agents needs to reflect real-
world labor-market conditions. According to data published by the
World Bank [40], China’s urban unemployment rate was 4.6% in
2025. Accordingly, at𝑡= 0(Round 0), we use this 4.6% rate as the
baseline parameter to determine the number of agents initialized as
unemployed. In subsequent simulation rounds, a within-industry
layoff rate (𝜆) of 3% is applied in each round [ 36]. Data from the
National Bureau of Statistics of China (NBS) indicate that young
workers face a substantially higher unemployment rate. To cap-
ture this age-related disparity in unemployment risk, we set the
initial unemployment probability for agents aged 20–29 to three
times the baseline rate. This adjustment is designed to reflect the
disproportionate challenges faced by youth in the Chinese labor
market.
In addition, when jobs are exposed to technological shocks and
face the threat of displacement, workers may respond by switch-
ing occupations or remaining in their current positions at lower
wages[18]. This adjustment process may give rise to frictional un-
employment. Furthermore,Wang et al. [37] estimate that approxi-
mately 54% of jobs in China could be at risk of substitution by AI
over the coming decades. This suggests that workers affected by
AI shocks may either leave employment or switch jobs. Drawing
on their estimate, we introduce a model rule under which agents
in occupations with high AI exposure have a 54% probability of
choosing to Migrate or Exit and a 46% probability of choosing to
Resist—that is, to remain in their current positions. Agents who
choose to Resist incur a 25% wage reduction[21].
Wage.The determination of labor income, a central focus of this
study, is influenced by a multitude of factors, including education,
government policy, and seniority. An initial wage distribution that
reflects real-world conditions is critical to ensuring the realism
and validity of the simulation outcomes. To incorporate real-world-
like characteristics of wage dispersion, we follow the Mincer[26]
tradition by assuming that initial annual wages,𝑤𝑖, follow a log-
normal distribution. The specification is as follows:
𝑤𝑖∼LogNormal 𝜇𝑜𝑖, 𝜎=0.30 ,E[𝑤 𝑖]= ¯𝑤𝑜𝑖,(2)
where the mean annual wage for each occupation, ¯𝑤𝑜𝑖 , is calibrated
using 2024 data from the NBS for urban employees:¥78,561 forRou-
tine,¥77,584 forManual,¥148,046 forCognitive, and¥203,014 for
Managerialroles. To account for intra-occupational heterogeneity,
we set the dispersion coefficient to 𝜎= 0.30[17], consistent with
observed variations in individual labor income within the same
sectors. Furthermore, to reflect institutional protections for work-
ers’ basic livelihood and rights, a statutory minimum wage floor is
imposed. Based on the 2024 national average monthly minimum
wage (¥2,100), we set the annual wage floor at𝑠min =¥ 25, 200. The
remaining parameter configurations and their respective initializa-
tion values are detailed in the appendix A.
In addition to their regular wages, workers can earn a wage
premium by acquiring advanced skills. For workers, AI technology
therefore represents both a potential adverse shock and a source of
economic gains. According to research by scholars at the Oxford
Internet Institute and the Center for Social Data Science at the Uni-
versity of Copenhagen, workers who have mastered AI skills earn
wages approximately 21% above the average[35]. Consequently, in
this study, when an agent successfully executes an Upgrade, its
wage is updated as: 𝑤1 =𝑤 0× 1.21. Furthermore, according to
opportunity cost theory, every economic activity entails an oppor-
tunity cost. When employed individuals devote time to learning
in order to upgrade their skills, they forgo the income that could
have been earned by allocating that time to alternative activities[9].
Accordingly, this study assumes that an employed agent who fails
to complete a skill upgrade incurs a cost equivalent to 5% of their
annual wage.
2.3 LLM-driven individual agents’ (workers’)
behavior
We introduce LLMs to drive the individual agents’ decision-making
process within the rule-based labor market behavioral space. The
rationale for introducing the LLM as the decision-making engine is
that it can adapt its decisions to changes in the environment[19],
while allowing us to observe the resulting decisions in each round
of the simulation. To enable the LLM to better perceive the em-
ployment environment and evaluate strategic trade-offs, we have
developed prompts that translate quantitative parameters into qual-
itative narratives, as follows.
(1) AI Exposure (𝑎𝑖 ):Medium exposure level: “You’ve started
to feel AI’s impact on your work. Some colleagues’ posi-
tions have been optimized away. You’re worried but not yet
panicking. ”

Table 1: Gini coefficients under the GLM scenario.
Simulation Round All Employed Only
0 0.325 0.278
1 0.339 0.290
2 0.358 0.301
3 0.364 0.311
4 0.377 0.324
5 0.388 0.339
(2) Occupation (𝑜𝑖 ):Routine occupation: “You work on assem-
bly lines or in standardized operations—your tasks are highly
repetitive. ”
(3) Role assignment sets the agent’s persona.You are a
worker living in China. [Age narrative.] [Occupation narra-
tive.] Your current annual salary is RMB [wage]. [AI-exposure
narrative.]
(4) Behavioral options for individual agents.An employed
agent replies with only one word:Resist,Migrate,Up-
grade, orExit. An unemployed agent replies with only
one word:SeekorRemain. Thus, each agent selects an ac-
tion according to the agent’s current employment state. The
complete prompt is provided in the appendix B.
In our simulation framework, agents’ decisions are generated
by the LLM based on the current state of the environment and the
agent’s own action history. Agents face different sets of available
actions depending on whether they are employed or unemployed.
The action space for employed agents,Aemp, is defined as follows:
Aemp ={Upgrade,Migrate,Resist,Exit}.
The action space for unemployed agents,Aunemp, is defined as fol-
lows:
Aunemp ={Seek,Remain}
MigrateandSeekactions trigger a second-stage choice of a tar-
get occupation-exposure cell(𝑜′,𝑎′). If the agent selectsSeek, the
agent may transition into any of the twelve occupational–exposure
combinations in the subsequent round. When an agent selects the
Migratestrategy, it may choose from nine alternative occupa-
tional–exposure combinations (i.e., transitioning from the current
industry to another). In turn, when an agent selects theUpgrade
strategy, it is deemed to have acquired AI-complementary skills,
resulting in enhanced labor market competitiveness and elevated
wages. If an agent selectsExit, it leaves employment and becomes
unemployed. Further details on the agents’ decision-making process
are provided in the appendix C.
3 Results
3.1 The Impact of AI-shocks in Wage
Distribution
We first use the agentic framework to simulate the evolution of the
wage distribution under sustained AI shocks in the Chinese labor
market. The main results are in Figure 2. As shown in Figure 2 (a),
the average annual wage of agents in the top income decile (T10)
increases from RMB 247K in Round 0 to RMB 379K in Round 5. By
contrast, the average wage of workers in the bottom income decile
(B10) rises only modestly, from RMB 47k to RMB 50k, representing
substantially slower wage growth than that experienced by the T10
group. Consequently, the T10/B10 ratio(Ratio) increases steadily
from 5.27 to 7.66. Table 1 further shows that the Gini coefficient
increases from 0.325 to 0.388 from round 0 to round 5 of the simu-
lation. The concurrent increases in the T10/B10 ratio and the Gini
coefficient after the 5 simulation rounds indicate that sustained AI
shocks are associated with greater wage polarization and rising
income inequality in the simulated labor market.
The occupational distribution also changes substantially over
the course of the simulation. Employment inRoutineoccupations
decreases from 276 to 100 workers, whereas employment inMan-
ual,Cognitive, andManagerialoccupations increases from 326 to
427, from 236 to 260, and from 97 to 139 workers, respectively
(Figure 2(b)). These results indicate a gradual reallocation of em-
ployment away from highly codified and repetitiveRoutineoccu-
pations toward other occupational categories, particularly those
associated with higher wages in the simulated environment. This
pattern suggests that workers tend to transition from lower-wage
to higher-wage occupations. Further decomposing employment
by AI exposure reveals that the number of workers in the high-
exposure group declines sharply from 180 to 1, while employment
in the low- and medium-exposure groups increases from 408 to
500 and from 347 to 425, respectively(Figure 2(c)). This indicates
that sustained AI shocks induce a pronounced shift in employment
toward occupations with lower levels of AI exposure. One possible
explanation is that workers in highly AI-exposed occupations face
a greater risk of job displacement and therefore have stronger in-
centives to switch to less-exposed occupations [12].The variation
in employment across different levels of AI exposure demonstrates
that using an LLM as the decision-making engine provides greater
behavioral flexibility than a purely rule-based agent model.
3.2 Sensitivity analysis of two key parameters
Workers’ earnings are closely related to wage premiums from skill
upgrading and the likelihood of re-employment. Drawing on the
skill wage premium literature [22] and labor search-and-matching
theory [27] as the theoretical foundations for these two processes,
we conduct one-at-a-time sensitivity analyses on two key parame-
ters: the wage multiplier associated with skill upgrading and the
probability that an unemployed agent successfully finds employ-
ment after choosingSeek. When varying each target parameter, all
other model parameters are held constant to assess whether the
baseline simulation results depend on specific parameter settings.
The results are reported in Figure 3. Figure 3(a) shows that, although
the Ratio exhibits small non-monotonic fluctuations across adjacent
values of the upgrade wage multiplier, the overall relationship is
strongly positive. This pattern is consistent with the model mecha-
nism: a larger wage premium following successful skill upgrading
produces greater wage gains for workers who complete the up-
grading process, thereby disproportionately increasing wages at
the upper end of the distribution. The Upgrade wage multiplier,
therefore, affects the magnitude of wage polarization rather than
its direction. Even when successful skill upgrading provides no ad-
ditional wage premium, the Round 5 Ratio remains above its initial
Round 0 value of 5.27. Figure 3(b) indicates that the Ratio is less

Figure 2: Multidimensional outputs of AI-driven wage polar-
ization. (a) Evolution of wage polarization with and without
AI exposure. (b) Changes in occupational composition. (c)
Employment by AI-exposure level. (d) Comparison of results
generated by different LLMs.
1.0 1.1 1.2 1.3 1.4
Upgrade wage multiplier
6
9
12
15
T10/B10 ratio
Baseline: 1.21
5.53 5.73
6.32 6.58
7.66
9.04
11.56 11.48
13.67
(a) Upgrade wage multiplier
0.4 0.5 0.6 0.7
SEEK success probability
7.6
8.0
8.4
8.8
Baseline: 0.57
7.47
7.85
7.66
8.09
8.39
(b) SEEK success probability
Figure 3: Sensitivity analysis of key parameters: (a) wage
multiplier for successful skill upgrading; (b) probability of
successful employment after choosingSeek.
sensitive to the probability of successful employment after choosing
Seek. The response is not strictly monotonic around the baseline
value: the Ratio is 7.85 when the success probability is 0.45 and
7.66 at the baseline value of 0.57. However, when the probability
increases to 0.65 and 0.75, the ratio rises to 8.09 and 8.39, respec-
tively. One possible explanation is that a higher re-employment
probability increases employment without necessarily compressing
the wage distribution, because newly employed agents may enter
relatively low-wage occupations.
Overall, under every parameter setting considered, the Round 5
Ratio remains above its initial value. The qualitative conclusion
that sustained AI shocks generate a wage gap between employed
agents is therefore preserved.
Table 2: Monte Carlo Simulation Outputs
State AI-On (±SD) AI-Off (±SD) Row Mean
LLM7.310±0.411 6.403±0.173 6.857
Random5.677±0.400 5.765±0.346 5.721
Col Mean6.494 6.084 6.289
3.3 Robustness checks
To assess the validity of the findings, we conduct two sets of ro-
bustness analyses: simulations using three alternative LLMs and
Monte Carlo simulations. First, to assess whether the baseline re-
sults depend on a particular LLM-based decision engine, we conduct
simulations using Qwen3, Llama-3.1, and DeepSeek-V4 (DS-V4),
while holding the initialized population and all model parameters
constant. As shown in Figure 2(d), the T10/B10 ratio generated by
GLM-4-Flash reaches 7.66 in Round 5, which is lower than the cor-
responding values produced by Qwen3 (8.78), Llama-3.1 (9.49), and
DS-V4 (9.82). Although the magnitude of the wage gap varies across
models, all LLMs exhibit a widening wage gap over the simulation
horizon. This consistency indicates that the central finding of wage
gap under AI shocks is not specific to GLM-4-Flash.
Second, we conduct 30 Monte Carlo simulations, each consist-
ing of five rounds, and compare LLM-based and random decision-
making under both AI-on and AI-off scenarios. The random-decision
condition does not employ an LLM. Instead, each agent selects uni-
formly at random from its current feasible action set. Consequently,
decisions in the random condition are independent of individual-
level information, including the agent’s age, occupation, wage, AI
exposure, and adaptive capacity.
Table 2 shows that, regardless of whether AI shocks are present,
the Ratio is consistently higher under LLM-based decision-making
than under the corresponding random-decision condition. This
result suggests that, relative to unconditional random behavior, het-
erogeneous decisions generated by LLMs on the basis of individual
states further amplify disparities in the wage distribution. More-
over, the wage gap is stronger in the AI-on scenario than in the
AI-off scenario, indicating that the model’s AI-exposure mechanism
and workers’ decisions jointly contribute to the widening wage
gap. These Monte Carlo results provide additional simulation-based
robustness evidence for the baseline findings.
3.4 Policy intervention
To examine whether an education subsidy policy can mitigate AI-
induced wage polarization, we introduce an education subsidy for
AI-related skill development into the baseline simulation. We as-
sume that the economy contains a dedicated funding pool that
provides education subsidies to eligible workers in the Chinese con-
text, whose annual income is below RMB 80,000. At the beginning
of each simulation round, workers earning less than RMB 80,000 per
year are informed of their eligibility for the subsidy before making
labor market decisions. Eligible workers may then choose whether
to participate in AI-related skills training. Participants receive a
subsidy of RMB 3,000. The subsidy is recorded as a policy cost and
is not directly included in workers’ labor income.
Employed workers who participate in the training enter the skill-
upgrading process. If the skill upgrade is successful, their wage is

Table 3: Comparison of Skill-Upgrading Outcomes Across
Simulation Scenarios
Indicator Baseline Policy P-Round1 P-Round5
Upgrade attempts 3,289 3,836 85 77
Successful upgrades 1,673 1,807 37 36
Upgrade success rate 50.9% 47.1% 43.5% 46.7%
multiplied by 1.21; if it is unsuccessful, they incur the original 5%
training-failure cost. Unemployed participants do not incur any
wage loss. Workers who are newly displaced during the current
round become eligible to enter the education subsidy process only
in the subsequent round.
After the education subsidy policy is introduced into the simula-
tion, the results show a gradual reduction in the wage gap relative
to the baseline scenario. As illustrated in Figure 4(a), the wage
gap under the education subsidy policy remains identical to that
in the baseline simulation during the first two rounds. From the
third round onward, however, the wage gap under the policy inter-
vention becomes smaller than that in the baseline scenario. These
results suggest that the education subsidy policy can mitigate the
wage gap to some extent, although its effects emerge only after a
certain time lag [6].
To clarify the mechanisms through which the education subsidy
policy operates, we examine two aspects: its incentive effect and its
impact on the middle-income group. First, we analyze workers’ par-
ticipation in subsidized training. Across the five simulation rounds,
93.0%–97.1% of eligible agents choose to participate in the training
program in each round (Figure 4(b)). We present a comparison of
skill-upgrading activities between the baseline and education sub-
sidy policy scenarios in Table 3. Table 3 shows that relative to the
baseline scenario, the number of skill-upgrading attempts increases
from 3,289 to 3,836, while the number of successful upgrades rises
from 1,673 to 1,807. These results indicate that the education sub-
sidy effectively encourages workers to participate in training by
increasing the total number of skill-upgrading attempts. However,
the overall skill-upgrade success rate under the policy scenario is
lower than that under the baseline scenario. This is because the
policy primarily targets laborers with relatively low learning ca-
pacity, who consequently have a lower probability of successfully
upgrading their skills. Nevertheless, a within-policy comparison
between P-Round 1 and P-Round 5 shows that the skill-upgrade
success rate increases over time. Taken together, the comparison
between the policy and baseline scenarios suggests that the educa-
tion subsidy policy encourages workers to participate in AI-related
skill learning. However, the policy does not substantially improve
the overall skill-upgrade success rate among employed workers.
Within the policy scenario, however, the skill-upgrade success rate
increases as the policy continues to be implemented. These findings
suggest that the education subsidy policy primarily promotes skill
development by increasing workers’ participation in skill learning
and gradually improving skill-upgrade outcomes over time, while
its overall effectiveness remains constrained by the relatively low
learning capacity of the targeted workers.
We further examine workers located between the 25th and 75th
percentiles of the income distribution(define it as the middle-income
group) in each simulation round(Table 4). Employment in this
middle-income group decreases slightly from 467 workers in Round 0
to 458 workers in Round 5, while its average annual wage increases
from RMB 95,400 to RMB 118,200. The employment composition
by AI exposure also shifts away from highly exposed occupations
toward occupations with medium or low AI exposure(Figure 4(c)).
Nevertheless, the number of workers employed in high-AI-exposure
occupations under the subsidy policy is approximately 50 times
that observed in the no-policy scenario. This result suggests that
the education subsidy enables some agents to acquire AI-related
skills and remain in, or transition into, occupations with high levels
of AI exposure.
Table 4: Round-Specific P25–P75 Income Group Under the
Education Subsidy Policy
Round 0 Round 5
Group Agents Mean Wage Agents Mean Wage
P25–P75 467 95,400 458 118,200
Overall, the education subsidy increases training participation
and the number of successful skill upgrades among simulated
agents, while partially reducing the T10/B10 ratio. It also raises
the average wage of the middle-income group. More importantly,
the policy enhances workers’ capacity to adapt to a labor market
increasingly affected by AI-related technological shocks.
4 Discussion
The purpose of this study is to examine whether and how AI shocks
affect wage disparities among workers and to explore the policy
measures that may be adopted in response to widening wage in-
equality. To address these questions, we develop a hybrid framework
and conduct simulation experiments. The simulation results show
that sustained AI shocks progressively widen wage disparities and
increase the Gini coefficient. This process is closely associated with
changes in occupational structure.
AI shocks affect not only workers’ earnings but also their occu-
pational choices and the overall structure of employment. When
confronted with a high risk of technological substitution, workers
in the simulation tend to leave highly exposed positions and move
toward occupations that are less exposed or more adaptable to tech-
nological change. This finding is consistent with the central argu-
ments of the skill-biased technological change and task-substitution
literature, which emphasize that the benefits and adjustment costs
associated with new technologies are not distributed evenly across
workers[1, 8]. Technological shocks can consequently induce struc-
tural adjustments in the labor market. Large-scale occupational
mobility represents one manifestation of this adjustment process.
From a governance perspective, the simulation allows to evalu-
ate a diversity of policy frameworks. We incorporate an education
subsidy policy in the Chinese labor market scenario. The policy
evaluation within the simulated framework shows that subsidiz-
ing AI-related skills training for low-income workers can partially

4
6
8
10
0 1 2 3 4 5
Simulation Round
T10/B10 Ratio
7.66
7.30
GLM-4-Flash Education Subsidy
Subsidy Participation
0
100
200
300
400
1 2 3 4 5
Simulation Round
Eligible Agents
93% 94.4%
97.1%
94.6%
95.5% 275
13
Participated Declined
Mean Wages by AI Exposure
0
50
100
150
200
AI Exposure
Mean Wage (¥000)
88.7
114.2
153.2
194.2
79.3 70.1
Low Medium High
408
470
347
398
180
50
Numbers inside bars denote employed agents (n)
Round 0 Round 5
(a) (b) (c)
Figure 4: Effects and mechanisms of the education subsidy policy. (a) presents the evolution of the T10/B10 ratio under the
GLM baseline and education subsidy policy scenarios; (b) shows subsidy participation; and (c) indicates mean wages and
employed-agent counts by AI-exposure level.
mitigate wage polarization. Relative to the baseline scenario, the
wage gap narrows under the subsidy policy. This effect does not
emerge immediately but becomes more pronounced after several
simulation rounds, consistent with the widely recognized time lag
in policy implementation and effectiveness[?]. Nevertheless, the
overall policy effect remains limited. Although the subsidy reduces
the wage gap and raises the average wage of middle-income work-
ers, it does not produce a clear reduction in the Gini coefficient
within the current simulation horizon. Education subsidies should
therefore be understood as a policy instrument for mitigating wage
polarization and strengthening workers’ capacity to adapt to tech-
nological change, rather than as a stand-alone solution to income
inequality.
The hybrid agentic framework proposed in this study integrates
the stability of rule-based mechanisms with the autonomous decision-
making capabilities of LLMs, enabling simulated agents to adapt
their behavior dynamically in response to changes in the environ-
ment. In this way, the framework retains the interpretability of
traditional ABMs while improving behavioral flexibility and model
scalability. Nevertheless, as with other studies of complex social
simulation, the present study is subject to several limitations that
warrant further investigation in future research. First and foremost,
the findings are generated within a simulated and simplified labor
market. Therefore, results should be interpreted as mechanism-
based evidence rather than validated forecasts of China’s actual
wage distribution. Second, worker decisions are informed by LLMs.
These models can generate context-dependent behavioral hetero-
geneity, but their responses may vary across model versions, prompt
designs, and repeated API calls. The comparison across alternative
LLMs and the parameter-sensitivity analysis reduce, but do not
eliminate, this source of uncertainty. Third, the current framework
models the worker side of the labor market without explicitly repre-
senting firms, vacancies, labor demand, productivity, or endogenous
wage bargaining. Wages therefore evolve according to predefined
transition rules rather than through a market-clearing process.
Building on the limitations discussed above, future research
could extend the current framework from the perspectives of dis-
aggregated data comprehensiveness, market structure complexity,
and policy evaluation preparedness. While the present study re-
lies primarily on aggregate statistics, which limits its ability to
explain heterogeneity in individual behavior, subsequent research
could incorporate individual-level demographic, psychological, and
behavioral data, expand the number of agents, and allow communi-
cation and interaction among them. These extensions would enable
the model to more realistically reproduce worker behavior and so-
cial relationships. Finally, the framework could be further extended
by incorporating a dynamic policy environment. The government
could adjust education subsidies, vocational training programs,
unemployment protection, and incentives for firms’ technology
adoption in response to changes in employment, wage inequality,
and the skill composition of the workforce. This extension would
facilitate a more systematic analysis of the temporal effects, inter-
actions, and long-term welfare implications of alternative policy
combinations.
5 Conclusion
This study develops a hybrid agentic framework to examine how AI
shocks affect wage polarization and distributional inequity in China.
The simulation results provide evidence that both the T10/B10 ratio
and the Gini coefficient increase persistently under repeated AI
shocks, indicating a widening wage gap and rising income inequal-
ity in the simulated labor market. Robustness tests using multi-
ple large language models (LLMs) and Monte Carlo simulations
preserve the direction of these trends, suggesting that the main
findings are not specific to a particular decision engine or simula-
tion run. We further conduct an evaluation of an education subsidy
policy within the simulated labor market framework. The policy
experiment illustrates how the T10/B10 income ratio declines when
training subsidies encourage low-income workers to acquire AI-
related skills. This finding suggests that subsidized education and
skills training could serve as an important policy instrument for
mitigating AI-induced wage polarization by strengthening workers’
capacity to adapt to technological change. Beyond its substantive
findings, the proposed framework offers a methodological contri-
bution and a practical analytical tool for policy evaluation in the
labor market within the AI era.

A Model Calibration Results
Table 5: Calibration of the Initial Agent Population: Demographic Composition
Indicator SD Initialization Difference Source
Age share(𝑔𝑖): 20–29 (%) 22.0% 21.7% -0.3 pp NBS, Seventh National Popula-
tion Census (2020)
Age share(𝑔𝑖): 30–39 (%) 25.0% 23.6% -1.4 pp Same as above
Age share(𝑔𝑖): 40–49 (%) 28.0% 29.5% +1.5 pp Same as above
Age share(𝑔𝑖): 50–59 (%) 25.0% 25.2% +0.2 pp Same as above
Occupational share( 𝑜𝑖):
Routine (%)
30.0% 29.4% -0.6 pp NBS 19-industry employment
(2025)
Occupational share( 𝑜𝑖):
Manual (%)
35.0% 34.6% -0.4 pp Same as above
Occupational share( 𝑜𝑖):
Cognitive (%)
25.0% 26.0% +1.0 pp Same as above
Occupational share( 𝑜𝑖):
Managerial (%)
10.0% 10.0% 0.0 pp Same as above
Notes:Data were obtained from the National Bureau of Statistics of China (NBS). SD denotes sociodemographic data. The initialization snapshot comprises 1,000 agents.
Differences are calculated as the model-initialization values minus the corresponding SD values. The abbreviation “pp” denotes percentage points and is used for shares,
unemployment rates, and AI-exposure probabilities, whereas percentage differences are reported for wages.
Table 6: Calibration of the Initial Agent Population: Macroeconomic and Distributional Indicators
Indicator SD Initialization Difference Source
Initial unemployment
rate(𝜆): ages 20–29 (%)
13.8% (3×4.6%) 11.1% -2.7 pp Calculated by author
Initial unemployment
rate(𝜆): ages 30–59 (%)
4.6% 5.2% +0.6 pp World Bank (2025)
Annual minimum-wage
floor((𝑤𝑖)) (RMB)
25,200 25,200 0.0% NBS 2024(¥2,100)×12
Notes:Same as Table 5. The all-agent unemployment target is implied by the age-specific unemployment rule and target age composition.
Table 7: Calibration of the Initial Agent Population: Occupation-Specific Annual Wages
Indicator SD Initialization Difference Source
Routine wage(𝑤𝑖),¥78,561¥80,194 +2.1% NBS Average Wage of Urban
Units (2024)
Manual wage(𝑤𝑖)¥77,584¥78,639 +1.4% Same as above
Cognitive wage(𝑤𝑖)¥148,046¥149,275 +0.8% Same as above
Managerial wage(𝑤𝑖)¥203,014¥212,514 +4.7% Same as above
Notes:Same as Table 5. Occupation-specific initial wages are calculated among employed agents only.
Table 8: Calibration of the Initial Agent Population: Occupation-Conditional AI Exposure Distribution
Occupation SD (%) Initialization (%) Difference (pp) Source
L M H L M H L M H
Routine(𝑎𝑖) 5.2 33.1 61.7 6.5 29.6 63.9 +1.3 -3.5 +2.2 ChinaJob exposure
index[20]
Manual(𝑎𝑖) 100.0 0.0 0.0 100.0 0.0 0.0 0.0 0.0 0.0 Same as above
Cognitive(𝑎𝑖) 31.4 66.4 2.2 29.2 69.2 1.5 -2.2 +2.8 -0.7 Same as above
Managerial(𝑎𝑖) 0.0 100.0 0.0 0.0 100.0 0.0 0.0 0.0 0.0 Same as above
Notes:Same as Table 5. L/M/H denotes low, medium, and high AI exposure, respectively. Each row reports𝑃(𝑎 𝑖|𝑜 𝑖) by occupation; each difference is calculated as the initialized
share minus its occupation-specific target.

B the Complete Prompt
Table 9: AI-exposure prompt components.
AI exposure Prompt
Low Your job faces relatively little AI disruption for now; it feels safe in the short term.
Medium You have started to feel AI’s impact on your work. Some colleagues’ positions have been
optimized away. You are worried but not yet panicking.
High Your job is being rapidly replaced by AI. People around you keep getting laid off. You feel anxious
every day, unsure how much longer you can hold on.
Table 10: Occupation prompt components.
Occupation Prompt
Routine You work on assembly lines or in standardized operations; your tasks are highly repetitive.
Manual You do physical labor or service work, such as logistics, food service, construction, and similar
jobs.
Cognitive You do knowledge work that requires professional expertise, such as programming, design, and
analysis.
Managerial You are in management, responsible for team leadership and business decisions. Your income is
higher, but so is the pressure.

C LLM Decision-Making Process
1. Agent State (Observation)
Employment
Status
Wage Occupation AI Exposure Level Other Context (Macro, Policy, ...)
Unemployed
Initial share: 4.6%
Layoff rate: 3% / round
Employed
Active labor force participant
2. LLM Decision Engine
The agent reasons over its state
 expected utility.
Job Search Decision
Remain unemployed
or search for a job?
AI Exposure Assessment
What is the agent's
AI exposure level?
Remain
Unemployed
Seek Job
Match across
12 combinations
Matching Outcome
Re-employment rate: 57%
Success
Become employed
Fail
Remain unemployed
High AI
(e.g., highly
automatable)
Low / Medium
(e.g., partially / low
automatable)
Adjustment Decision
Upgrade, migrate,
resist, or exit?
54% migrate / exit
46% resist / upgrade
Adjustment Decision
Upgrade, migrate,
seek new job, or exit?
Decision
(LLM-based)
3. Action Space
(LLM Output)
4. State Transition
(Rule-based)
Upgrade
Invest in skills
and productivity
Migrate
Move to another
sector / region
Resist
Stay in place and
maintain status
Exit / Seek
Exit labor market or
enter unemployed pool
Rule-based Environment Transition
Update employment status, wage, occupation, and macro variables.
Next Round (t + 1)
Repeat for T rounds (e.g., 1 round = 1 year)
Legend
State / Input
LLM Decision
Action
Transition
Terminal Outcome
Notes
Percentages are
illustrative and can
be calibrated.
and chooses an action that maximizes
Figure 5: This figure illustrates the decision-making and state-transition process of worker agents in each simulation round,
with the LLM serving as the decision-making engine. The LLM first observes each agent’s employment status, occupation, wage,
AI exposure, and other relevant information, and then selects actions such as Upgrade, Migrate, Resist, and Exit/Seek from
the action space according to the agent’s employment status. Subsequently, rule-based state-transition mechanisms update
employment status, wages, and occupations before the simulation proceeds to the next round.

References
[1] Daron Acemoglu. 2002. Technical Change, Inequality, and the Labor Market.
Journal of Economic Literature40, 1 (2002), 7–72. doi:10.1257/0022051026976
[2] Daron Acemoglu, David Autor, and Simon Johnson. 2026.Building Pro-Worker Ar-
tificial Intelligence. Working Paper 34854. National Bureau of Economic Research.
doi:10.3386/w34854
[3] Daron Acemoglu and Pascual Restrepo. 2022. Tasks, automation, and the rise in
US wage inequality.Econometrica90, 5 (2022), 1973–2016. doi:10.3982/ECTA19815
[4] Amr Adel and Noor Alani. 2025. Can generative AI reliably synthesise literature?
Exploring hallucination issues in ChatGPT.AI & Society40 (2025), 6799–6812.
doi:10.1007/s00146-025-02406-7
[5] Alba Aguilera, Nieves Montes, Georgina Curto, Carles Sierra, and Nardine Osman.
2024. Can Poverty Be Reduced by Acting on Discrimination? An Agent-Based
Model for Policy Making. InProceedings of the 23rd International Conference on
Autonomous Agents and Multiagent Systems. 22–30. doi:10.65109/CFUL3373
[6] Anna Aizer, Nancy Early, Shari Eli, Guido Imbens, Keyoung Lee, Adriana Lleras-
Muney, and Alexander Strand. 2024. The Lifetime Impacts of the New Deal’s
Youth Employment Program.The Quarterly Journal of Economics139, 4 (2024),
2579–2635. doi:10.1093/qje/qjae016
[7] Ariel Flint Ashery, Luca Maria Aiello, and Andrea Baronchelli. 2025. Emergent
Social Conventions and Collective Bias in LLM Populations.Science Advances11,
20 (2025), eadu9368. doi:10.1126/sciadv.adu9368
[8] David H. Autor, Frank Levy, and Richard J. Murnane. 2003. The Skill Content of
Recent Technological Change: An Empirical Exploration.The Quarterly Journal
of Economics118, 4 (2003), 1279–1333. doi:10.1162/003355303322552801
[9] Nicola Bianchi and Michela Giorcelli. 2022. The Dynamics and Spillovers of
Management Interventions: Evidence from the Training Within Industry Program.
Journal of Political Economy130, 6 (2022), 1630–1675. doi:10.1086/719277
[10] Eric Bonabeau. 2002. Agent-based modeling: Methods and techniques for simulat-
ing human systems.Proceedings of the National Academy of Sciences99, suppl_3
(2002), 7280–7287. doi:10.1073/pnas.082080899
[11] Kathryn Bonney, Cory Breaux, Catherine Buffington, Emin Dinlersoz, Lucia
Foster, Nathan Goldschlag, John Haltiwanger, Zachary Kroff, and Keith Savage.
2024. The Impact of AI on the Workforce: Tasks versus Jobs?Economics Letters
244 (2024), 111971. doi:10.1016/j.econlet.2024.111971
[12] Mauro Cazzaniga, Carlo Pizzinelli, Emma Rockall, and Marina M. Tavares. 2025.
Exposure to Artificial Intelligence and Occupational Mobility: A Cross-Country
Analysis.Economía LACEA Journal24, 1 (2025), 314–339. doi:10.31389/eco.451
[13] F. Cheng, H. Li, F. Liu, et al. 2025. Empowering LLMs with Logical Reasoning: A
Comprehensive Survey. arXiv:2502.15652 doi:10.48550/arXiv.2502.15652
[14] George Datseris, Ali R. Vahdati, and Timothy C. DuBois. 2024. Agents.jl: a perfor-
mant and feature-full agent-based modeling software of minimal code complexity.
SIMULATION100, 10 (2024), 1019–1031. doi:10.1177/00375497211068820
[15] Frank Dignum (Ed.). 2021.Social Simulation for a Crisis: Results and Lessons from
Simulating the COVID-19 Crisis. Springer, Cham. doi:10.1007/978-3-030-76397-8
[16] Esther Dweck, Matheus Trotta Vianna, and Arthur da Cruz Barbosa. 2020. Dis-
cussing the role of fiscal policy in a demand-led agent-based growth model.
EconomiA21, 2 (2020), 185–208. doi:10.1016/j.econ.2019.03.004
[17] Andrés Erosa, Luisa Fuster, Gueorgui Kambourov, and Richard Rogerson. 2024.
Wage and earnings inequality between and within occupations: The role of labor
supply.Journal of Monetary Economics145 (2024), 103553. doi:10.1016/j.jmoneco.
2024.01.006
[18] Frank M. Fossen and Alina Sorgner. 2022. New Digital Technologies and Hetero-
geneous Wage and Employment Dynamics in the United States: Evidence from
Individual-Level Data.Technological Forecasting and Social Change175 (2022),
121381. doi:10.1016/j.techfore.2021.121381
[19] Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli
Xu, et al. 2024. Large language models empowered agent-based modeling and
simulation: a survey and perspectives.Humanities and Social Sciences Communi-
cations11 (2024), 1259. doi:10.1057/s41599-024-03611-3
[20] Muqing Hao, Zhongbo Hu, Zonghan Wu, and Yilei Shao. 2026. ChinaJob: An
Occupational AI Exposure Index for China. https://github.com/SAIFS-AIHub/
ChinaJob. Accessed: 2026-07-22.
[21] Hannah Illing, Johannes Schmieder, and Simon Trenkle. 2024. The Gender Gap
in Earnings Losses after Job Displacement.Journal of the European Economic
Association22, 5 (2024), 2108–2147. doi:10.1093/jeea/jvae019
[22] Lawrence F. Katz and Kevin M. Murphy. 1992. Changes in Relative Wages, 1963–
1987: Supply and Demand Factors.The Quarterly Journal of Economics107, 1
(1992), 35–78. doi:10.2307/2118323
[23] Nian Li, Chen Gao, Min Li, , et al . 2024. EconAgent: Large Language Model-
Empowered Agents for Simulating Macroeconomic Activities. InProceedings of
the 62nd Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers). 15523–15536. doi:10.18653/v1/2024.acl-long.829
[24] Yuanyuan Liu, Ying Zhou, Le Yang, and Yangpeng Xin. 2024. Simulating staff ac-
tivities in healthcare environments: An empirical multi-agent modeling approach.
Journal of Building Engineering84 (2024), 108580. doi:10.1016/j.jobe.2024.108580
[25] Charles M. Macal and Michael J. North. 2005. Tutorial on Agent-Based Modeling
and Simulation. InProceedings of the 2005 Winter Simulation Conference. IEEE, 14.
doi:10.1109/WSC.2005.1574234
[26] Jacob Mincer. 1958. Investment in Human Capital and Personal Income Distribu-
tion.Journal of Political Economy66, 4 (1958), 281–302. doi:10.1086/258055
[27] Dale T. Mortensen and Christopher A. Pissarides. 1994. Job Creation and Job
Destruction in the Theory of Unemployment.The Review of Economic Studies61,
3 (1994), 397–415. doi:10.2307/2297896
[28] Mai Nguyen, Lars-Erik Casper Ferm, and Liem Viet Ngo. 2026. AI is taking my
job! Task programmability and employee job thriving in the age of AI.Journal of
Business Research210 (2026), 116119. doi:10.1016/j.jbusres.2026.116119
[29] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy
Liang, and Michael S. Bernstein. 2023. Generative Agents: Interactive Simulacra
of Human Behavior. InProceedings of the 36th Annual ACM Symposium on User
Interface Software and Technology. Association for Computing Machinery, New
York, NY, USA, Article 2, 22 pages. doi:10.1145/3586183.3606763
[30] Jinghua Piao et al. 2024. AgentSociety: Large-Scale Simulation of LLM-Driven
Generative Agents Advances Understanding of Human Behaviors and Society.
arXiv:2410.14408 doi:10.48550/arXiv.2410.14408
[31] Sebastian Poledna, Michael Gregor Miess, Cars Hommes, and Katrin Rabitsch.
2023. Economic forecasting with an agent-based model.European Economic
Review151 (2023), 104306. doi:10.1016/j.euroecorev.2022.104306
[32] Carl Orge Retzlaff, Martina Ziefle, and André Calero Valdez. 2021. The history
of agent-based modeling in the social sciences. InInternational Conference on
Human-Computer Interaction. Springer, 304–319. doi:10.1007/978-3-030-77817-
0_22
[33] Derek T. Robinson, Daniel G. Brown, Dawn C. Parker, Pepijn Schreinemachers,
Marco A. Janssen, Marco Huigen, Heidi Wittmer, Nicholas Gotts, Sudhir Chella
Rajan, Paul Ormerod, et al. 2007. Comparison of empirical methods for building
agent-based models in land use science.Journal of Land Use Science2, 1 (2007),
31–55. doi:10.1080/17474230701201349
[34] R. Sapkota, S. Raza, and M. Karkee. 2025. Comprehensive Analysis of Trans-
parency and Accessibility of ChatGPT, DeepSeek, and Other SOTA Large Lan-
guage Models. arXiv:2502.18505 doi:10.48550/arXiv.2502.18505
[35] University of Oxford. 2023. Artificial Intelligence Skills Can Increase Salaries by
as Much as 40%. https://www.ox.ac.uk/news/2023-10-24-artificial-intelligence-
skills-can-increase-salaries-much-40. Accessed: 2026-08-03.
[36] U.S. Bureau of Labor Statistics. 2026. Job Openings and Labor Turnover Survey.
https://www.bls.gov/jlt/. Accessed: 2026-07-22.
[37] Chengzhang Wang, Min Zheng, Xiaoming Bai, Youwei Li, and Wei Shen. 2023.
Future of Jobs in China under the Impact of Artificial Intelligence.Finance
Research Letters55 (2023), 103798. doi:10.1016/j.frl.2023.103798
[38] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang,
Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, et al. 2024. A survey on large
language model based autonomous agents.Frontiers of Computer Science18, 6
(2024), 186345. doi:10.1007/s11704-024-40231-1
[39] Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, William Fedus,
Maarten Li, Harold Tu, Kevin Laikas, Oscar Ames, et al. 2022. Emergent Abilities
of Large Language Models. arXiv:2206.07682 doi:10.48550/arXiv.2206.07682
[40] World Bank. 2025. China | Data. https://data.worldbank.org/country/china.
Accessed: 2026-07-22.
