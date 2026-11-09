---
title: 'Reproducing human biases in route choice using large language models: Toward scalable behavioral
  modeling'
url: https://arxiv.org/abs/2607.11632
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Jiangtao Han
- Shoufeng Ma
- Shuxian Xu
- Geng Li
- Shuai Ling
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.11632
pages: 34
chars: 94947
fetched_at: '2026-11-08T13:36:15+00:00'
kb_version: 1
---

# Reproducing human biases in route choice using large language models: Toward scalable behavioral modeling

Reproducing human biases in route choice using large language models:
Toward scalable behavioral modeling
Jiangtao Hana,b, Shoufeng Maa,b, Shuxian Xua,b,∗, Geng Lia,b, Shuai Linga,b, Ning Jiaa,b, Zhengbing Hec,∗
aLaboratory of Computation and Analytics of Complex Management Systems (CACMS), Tianjin University, China
bCollege of Management and Economics, Tianjin University, China
cFaculty of Science and Engineering, University of Nottingham Ningbo China
Abstract
Human choice behavior, including route choice, exhibits systematic behavioral biases that deviate from the
assumptions of full rationality. Cumulative prospect theory (CPT) has been widely recognized as an effective
framework for characterizing such behavioral patterns. However, its large-scale application, particularly in
simulation and agent-based modeling, critically depends on estimating CPT parameters based on individual-
level behavioral data, which remains a major bottleneck. Conventional approaches typically rely on surveys
and controlled experiments to calibrate CPT parameters, yet these methods are difficult to generalize and often
fail to capture the full diversity of human decision-making. To address this challenge, this paper investigates
whether large language models (LLMs) can reproduce human behavioral biases in choice-making without ex-
plicit specification of prospect-theoretic parameters. Using route choice as a representative scenario, we design a
behavioral evaluation framework and systematically compare LLM-generated decisions with established human
behavioral patterns predicted by CPT. Experimental results demonstrate that LLMs are capable of reproducing
non-rational human choice biases and can exhibit decision behaviors consistent with prospect-theoretic effects
under uncertainty. These findings suggest that generative AI models may provide a scalable alternative for mod-
eling human decision processes and offer a promising foundation for next-generation large-scale agent-based
simulation and AI-driven behavioral research.
Keywords:behavioral modeling, large language models, cumulative prospect theory, route choice, generative
agent
∗Corresponding author
Email addresses:shuxianxu@tju.edu.cn(Shuxian Xu),he.zb@hotmail.com(Zhengbing He)
arXiv:2607.11632v1  [cs.AI]  13 Jul 2026

1. Introduction
In real-world decision-making, individuals do not always behave in a fully rational and objective manner.
Instead, decisions are often shaped by subjective perceptions, resulting in systematic behavioral biases that
depart from the assumption of full rationality (Murphy and ten Brincke, 2018). Route choice is a typical example
of this phenomenon (Di et al., 2014). For example, travelers usually make route choice decisions under varying
traffic conditions, such as different travel times and congestion levels. Their decisions do not always follow
the principle of minimizing travel cost or travel time, but instead exhibit characteristics that deviate from the
predictions of fully rational choice models.
Cumulative Prospect Theory (CPT) is arguably the most important and influential descriptive model of risky
choice to date (Barberis, 2013, Fox et al., 2015, Murphy and ten Brincke, 2018). Unlike classical expected utility
theory, CPT can characterize key psychological mechanisms in human decision-making, including reference
dependence, loss aversion, diminishing sensitivity, and nonlinear probability weighting. These mechanisms
explain why individuals make asymmetric evaluations and exhibit different risk preferences under different gain
and loss scenarios. Due to its strong behavioral explanatory power, CPT has been widely applied to various
areas of travel behavior research, including mode choice (Zhou et al., 2024), departure time choice (Geng et al.,
2023), parking mode choice (Hu et al., 2025), and electric vehicle charging mode choice (Zhang et al., 2026).
However, the large-scale application of CPT, particularly in simulation and agent-based modeling, heavily
depends on estimating CPT parameters based on individual-level behavioral data, which remains a major bot-
tleneck. Jou and Chen (2013) estimated CPT parameters by surveying drivers at freeway rest areas about their
route choice outcomes under two sets of freeway experimental scenarios, each involving four different travel
times and corresponding occurrence probabilities. Hu et al. (2025) collected respondents’ parking mode choice
data under uncertain conditions, such as waiting time, parking fees, and cruising costs, and estimated CPT pa-
rameters to reflect autonomous vehicle users’ risk attitudes toward parking choice. Murphy and ten Brincke
(2018) emphasized that the specification of CPT parameters is a key step in quantifying individual preference
heterogeneity and uncovering the cognitive mechanisms underlying observed behavior; however, the accurate
estimation of these parameters remains challenging. Conventional approaches typically rely on surveys and
controlled experiments to calibrate CPT parameters (Zhang et al., 2018, Geng et al., 2023), which can charac-
terize the risk levels of specific groups but are difficult to generalize and often fail to capture the full diversity
of human decision-making (Thomas et al., 2024, Bagaïni et al., 2025).
The rapid development of large language models (LLMs) provides new technical support for human behav-
ior modeling (Park et al., 2023, Yan et al., 2026). Through natural language understanding, role generation,
and contextual reasoning, LLMs are able to characterize the complexity of human behavior. Therefore, LLM-
based virtual behavioral experiments offer a promising research pathway for reproducing systematic biases in
human decision-making, while also helping to alleviate the difficulty of CPT parameter estimation by gener-
ating diversified behavioral data. However, existing studies on LLM-based behavior modeling still face two
key challenges. First, whether LLM-generated behaviors can realistically and robustly reproduce human non-
rational decision biases under risky conditions remains to be examined. Second, constrained by the invocation
cost and computational resources of LLMs, virtual behavioral experiments involving large-scale heterogeneous
populations remain limited, and the capabilities of LLMs in behavioral data generation, parameter estimation,
and theoretical mechanism quantification have not yet been fully validated.
Taking route choice as a representative scenario of human risky decision-making, this paper proposes an
2

LLM-based method for conducting large-scale virtual behavioral experiments. Using this method, we simu-
late human route-choice behavior under different risky scenarios, confirm that LLMs can reproduce systematic
biases in human choice behavior, and further explore their potential for CPT parameter estimation. More specifi-
cally, as shown in Figure 1, heterogeneous human agents with multidimensional attributes are constructed based
on LLMs through standardized prompts, and dynamic traffic environments with different gain and loss condi-
tions are designed to conduct experimental simulations under various risk settings. The behaviors generated
by LLMs are then transformed into structured data suitable for statistical analysis and model calibration, en-
abling the estimation of prospect utility parameters and the inference of reference points. Finally, the proposed
method is evaluated at both the individual and environmental levels, and its accuracy in parameter estimation
and route-choice prediction is compared with that of traditional parameter estimation methods. Experimental re-
sults demonstrate that LLMs are capable of reproducing non-rational human choice biases and exhibit decision
behaviors consistent with prospect-theoretic effects under uncertainty.
The significance of this study lies not only in using LLMs to simulate human route-choice behavior at
scale, but also in demonstrating their potential to reproduce systematic biases in human decision-making. The
findings suggest that LLM-based agents are able to exhibit subjective perception and boundedly rational choice
patterns similar to those of real humans. Therefore, generative AI models may provide a scalable alternative
for modeling human decision processes and offer a promising foundation for next-generation large-scale agent-
based simulation and AI-driven behavioral research.
1 Traffic Environment and
Human Decision Characteristics
Uncertain Traffic Environment
Traffic Accident
Unexpected
Congestion
Temporary
Road Control
Human Decision Characteristics
Bounded Rationality
Risk Perception
1 Traffic Environment and
Human Decision Characteristics
Uncertain Traffic Environment
Traffic Accident
Unexpected
Congestion
Temporary
Road Control
Human Decision Characteristics
Bounded Rationality
Risk Perception
2 LLM-based Human
Agent Construction
2 LLM-based Human
Agent Construction
3 Dynamic Scenario Design
and Virtual Experiment
3 Dynamic Scenario Design
and Virtual Experiment
4 Data Analysis
and Parameter Estimation
4 Data Analysis
and Parameter Estimation
Prompt Engineering
Heterogeneous Human Agents
Personality
Personality
Travel
Purpose
Travel
Purpose
Risk
Preference
Risk
Preference
Travel
Time
Travel
Time
...
Dynamic Traffic Scenarios
Accident
Congestion
Road Control
Virtual Behavior Experiment
LLM-generated
Textual Responses
Structured Route
Choice JSON Data
Behavioral Data
Analysis
CPT Parameter
Estimation
Scenario Input Agent Construction Route Choice Simulation Data AnalysisScenario Input Agent Construction Route Choice Simulation Data Analysis
Environment Input
Provides Human Agents
Simulated Decision Outputs
Figure 1: LLM-based route choice modeling and virtual behavioral experiment framework
The remainder of this paper is organized as follows. Section 2 reviews the relevant literature. Section 3
introduces the mechanisms of LLMs. Section 4 systematically develops the LLM-based route choice simula-
tion framework and proposes methods for determining prospect utility parameters and reference points. Section
5 conducts LLM-based experimental simulations under different risk scenarios, estimates the CPT parameters
based on the simulation results, evaluates the simulation effects, and compares them with other parameter esti-
mation approaches. Finally, Section 6 concludes this study and suggests directions for future research.
3

2. Literature review
2.1. CPT-based route choice modeling
Research on human route choice is one of the core topics in traffic behavior analysis and transportation net-
work modeling, and it also serves as a crucial behavioral basis for traffic assignment, congestion management,
and travel information services (Yang and Zhang, 2009, Qi et al., 2023, 2024). For a long time, mainstream
research in this field has been based on expected utility theory (EUT) and the assumption of full rationality
(Zhang and Nagurney, 1996, Smith, 1984). However, with the continuous observation of real travel behavior
and the accumulation of empirical evidence, the traditional EUT framework has gradually revealed its limita-
tions in explaining route choice behavior under uncertain conditions (Wu et al., 2013, Henn and Ottomanelli,
2006).
Theoretical tools from behavioral economics and psychology have gradually been introduced into travel
behavior research to explain human decision-making behavior under uncertain conditions from the perspec-
tive of bounded rationality. Among these, prospect theory proposed by Kahneman and Tversky (1979) and
its subsequent development, CPT (Tversky and Kahneman, 1992), provide an important theoretical founda-
tion for explaining systematic deviations from rational behavior under uncertain conditions. CPT emphasizes
that: (1) individuals evaluate gains and losses relative to reference points, and decision-making focuses on rel-
ative changes rather than absolute levels; (2) individuals tend to exhibit risk aversion in the domain of gains
and risk seeking in the domain of losses, with losses having a greater psychological impact than equivalent
gains; (3) individuals perceive probabilities in a nonlinear manner, overweighting low-probability events while
underweighting medium- and high-probability events.
Route choice modeling based on CPT typically characterizes behavior through two types of core functions.
The first is the value function, which describes humans’ nonlinear evaluation of gains and losses relative to
a reference point. The second is the probability weighting function, which describes humans’ subjective per-
ception of the probability of different travel outcomes. Existing research has validated and extended the CPT
framework across different dimensions of travel behavior. For example, Jou and Chen (2013) modeled the per-
ception of gains and losses of freeway drivers using CPT by considering their risk attitudes and preferences,
and applied it to the route choice problem of drivers on freeways. Ghader et al. (2019) introduced a CPT-based
travel mode choice modeling framework that uses observational data (household travel surveys) to help travel
demand modelers model reliability using CPT in their trip-based or activity-based models. Zhang et al. (2018)
collected statistical data on the actual route choice decisions of subjects by designing and conducting laboratory
behavioral experiments. Based on CPT, they constructed a day-to-day route choice learning model that included
friends’ travel information and explored the effect of social interaction information from friends on commuters’
daily route choice decisions. Furthermore, other studies (Geng et al., 2023, Hu et al., 2025, Zhang et al., 2026)
have validated and extended the CPT framework across different dimensions of travel behavior, demonstrating
that CPT plays a crucial role in human behavior modeling.
When CPT is used to characterize human behavior, the prospect utility parameters reflect humans’ risk
attitudes and value preferences. Their reasonable setting and accurate estimation not only determine whether
the model can accurately capture human value evaluation and risk perception mechanisms but also directly
affect the model’s predictive ability for human decision-making behavior under uncertain conditions. Therefore,
determining the prospect utility parameters is crucial for improving the model’s explanatory and predictive
power. Xu et al. (2011) designed two types of travel scenarios: time gain and loss scenarios. Each scenario
4

consists of two routes with equal average travel times but different gains or losses. They obtained the CPT
parameter estimation results by conducting a questionnaire survey among part-time postgraduate students and
fitting the collected human route choice preference data. Ghader et al. (2019) conducted a travel behavior survey
of residents in the Washington area, obtained 160 available data records, analyzed the data characteristics of both
rail and driving travel, and estimated the parameters of the CPT model using the maximum likelihood estimation
method. Regarding the determination of reference points, Yang and Jiang (2014) improved the method of
setting reference points in the route choice model by replacing free-flow travel time with actual budgeted travel
time. Zhang et al. (2018) estimated reference points by considering the risk level of the participants through
questionnaire surveys and combining the cumulative distribution function of the participants’ travel time.
Overall, the existing studies based on questionnaire surveys or behavioral experiments provide valuable
insights and methods for estimating CPT parameters, and can realistically depict human basic risk preferences
to a certain extent. However, these methods are often constrained by limited sample sizes and homogeneous
participant groups, making it difficult to fully reflect the behavioral differences caused by different occupational
types, personality traits, travel purposes, and risk attitudes.
2.2. Large language models
Benefiting from large-scale parameterization and pretraining on massive datas, recent LLMs have demon-
strated capabilities approaching human-level intelligence in language understanding, knowledge reasoning, and
generative interaction (Hua et al., 2023, Chen et al., 2024). Compared with traditional rule-based or small-
sample learning intelligent systems, LLMs exhibit stronger task generalization and programmability, enabling
researchers to trigger various behaviors such as information extraction, situational decision-making, and multi-
turn dialogue—through designed prompts. This provides new technical support for behavior simulation driven
by natural language. With the integration of memory mechanisms (Sumers et al., 2023), tool invocation (Schick
et al., 2023), and planning modules (Liu et al., 2023b), LLMs are no longer limited to text generation but are
gradually developing into closed-loop intelligent agents with capabilities for perception, memory, planning, and
action, offering a novel pathway for modeling individual behavior in complex social systems.
Against this backdrop, research on generative agents has provided a new paradigm for simulating human
behavior. Park et al. (2023) from Stanford University first systematically proposed the concept of generative
agents and instantiated a group of agents capable of perceiving the environment, forming memories, planning,
and interacting with others in an interactive sandbox environment. Their results show that LLM-based agents
can not only generate daily behavior trajectories consistent with individual human characteristics, but also
exhibit social phenomena such as information diffusion, social aggregation and collaborative behavior in group
interactions, providing architectural design and interaction paradigms for achieving believable human behavior
simulation. Subsequently, a series of follow-up studies have extended this model to other application scenarios,
including social interaction (Zhou et al., 2023), game reasoning and decision-making (Xu et al., 2023), and
software development (Qian et al., 2024). At the same time, multimodal generation technologies (Wang et al.,
2023, Nguyen et al., 2022) such as speech, images, and video are also accelerating, making it possible to present
behaviors and interactions closer to the real world. In short, LLM-driven agent simulation methods are rapidly
becoming an important tool for simulating complex human behavior.
Although LLMs have been applied in many fields, research on their use for simulating human risky decision-
making behavior remains relatively limited. In particular, whether LLMs can exhibit systematic biases similar
to those observed in humans and demonstrate decision-making behavior consistent with CPT under uncertainty
5

has not been fully verified. Existing studies mostly remain at the level of small-scale scenario testing, making it
difficult to reveal behavioral differences and emergent characteristics among different types of individuals at the
group level. Meanwhile, there is still a lack of systematic methodological frameworks and operational proce-
dures for designing standardized prompts, constructing representative uncertain risk scenarios, and generating
large-scale, reproducible, and statistically analyzable human-like behavioral data.
3. Preliminaries
LLMs are a powerful class of natural language processing systems that are constructed on the transformer
architecture (Vaswani et al., 2017) and trained using in-context learning (ICL) techniques (Brown et al., 2020,
Akyürek et al., 2022). The core of the transformer is scaled dot-product attention, which is defined as:
Attention(A,K,V)=softmax
 QK T
√dk
!
∗V(1)
whereQis the query,Kis the key,d k is the dimension, andVis the value. The attention mechanism applies
the softmax function to obtain the weight of the value by calculating the dot product of the query and the key,
and finally outputs the result with the largest weight. ICL allows language models to learn tasks with only a few
example in the form of demonstrations (Dong et al., 2024). Formally, given a query input textaand a candidate
answer setb=[b 1,...,b n], the possibility of the candidate answerb j is calculated by the scoring functionfof
the thole input sequence:
P(b j|a)
∆
=f M(b j,C,a) (2)
The pre-trained language modelMtakes the candidate answer with the maximum score as the prediction
result, and the final prediction labelbbis the candidate answer with the highest probability:
bb=arg max
b j∈b
P(b j|a) (3)
This mechanism enables the model to perform task-specific behaviours directly from prompts and demon-
strations without additional parameter updates (Liu et al., 2023a). In recent years, LLM-based agents have
demonstrated remarkable human-like capabilities in reasoning and planning (Park et al., 2023, Yao et al., 2023,
Wang et al., 2024b). These agents constitute systems that possess a certain degree of autonomy, goal-directed
behavior, responsiveness, and interactive ability, enabling them to perceive the environment, make decisions,
and take actions independently. In the autonomous agent systems powered by LLMs, the agent brain is com-
posed of several key components, including memory, planning, and action (Weng, 2023).
Memory module.This module enables the agent to acquire, store, and retain information, thereby sup-
porting its subsequent actions. Memory is typically categorized into sensory memory, long-term memory, and
short-term memory.
Planning module.This module assists the agent in breaking down complex tasks into smaller, more man-
ageable subtasks.
Action module.This module functions as the agent’s decision executor, responsible for generating the
specific actions the agent performs.
6

4. Methodology
4.1. Construction of LLM-based human agents
This study adopts a nonparametric prompting method to construct LLM-based human agents, assigning
roles with specific demographic characteristics to the model. The agents are able to act according to predefined
identities and roles, based on their own ideas and feelings. In order to realize the simulation, this paper develops
a standardized prompting architecture that can accurately describe human identity characteristics and capture the
complexity of human behavior. This architecture is modularized into three core components: profile, planning,
and action.
Profile.The human agent’s individual profile is constructed to distinguish the unique characteristics of dif-
ferent simulated individuals. The profile consists of three components: individual attributes, behavior features,
and constraint conditions. The individual attributes include occupation, risk preference, travel purpose, and
time pressure, which are used to describe the agent’s basic identity. The behavior features capture the agent’s
preferences for expected travel time and time volatility of different routes, tolerance intervals for early and
late arrivals, and sensitivity to risks such as traffic accidents, unexpected congestion or temporary road control
measures, which can be understood as the agent’s behavioral parameters and psychological preferences. The
constraint conditions are used to limit the set of feasible travel plans, including mandatory time constraints,
personal ability or characteristic constraints, and environmental constraints.
Planning.The planning ability of the human agent is designed to enable it to decompose and plan complex
tasks under a specific identity and scenario. Through prompting, the travel purpose and risk preference are
clarified, guiding the agent to identify key decision-making factors, such as travel time and time variability. On
this basis, the agent evaluates each route in terms of expected time, variability, and risk according to its travel
objectives, forms subjective assessments and prioritization across routes, and ultimately generates a travel plan
consistent with its identity and psychological preferences.
Action.The decision rules and output formats are established to ensure that the agent can make route choice
decisions that reflect its individual characteristics within a given scenario. The decision rules specify how the
agent should weigh different route attributes and how risk attitudes influence choice preferences. For example,
risk-averse agents are expected to prioritize routes with lower time variability, whereas risk-seeking agents tend
to prefer routes with shorter travel times but higher variability. To ensure that the output is controllable and
suitable for statistical analysis, the LLMs are required to produce strictly structured JSON outputs.
It is important to note that the constraints in the agent profile define the objective limitations related to
occupation, personality traits, travel purpose, and environmental factors, thereby determining the feasible set
of travel options. In contrast, the decision rules describe how the agent weighs attributes such as travel time,
time variability, and risk within this feasible set and constitute the behavioral mechanism that drives the agent
to generate specific route choice decisions.
4.2. Construction of LLM-based route choice travel environment
Travel environments define the specific context in which agents operate. Similar to how humans acquire
information from their surroundings, agents rely on the environment to receive input signals from multiple
sources, which guide their behaviors and decision-making strategies within the system. A comprehensive un-
derstanding of the environment is a prerequisite for agents to make route choice decisions and complete travel
tasks. This study constructs LLM-based route choice travel environments from two dimensions of configuration
and state.
7

Configuration.The configuration defines the agent’s travel task and the fundamental structure of the envi-
ronment. It provides static or relatively stable information, including task objectives, the set of optional routes,
and basic route attributes. Travel task constraints establish the agent’s travel time requirements and the conse-
quences of arriving late or early. The set of optional routes and basic route attributes describe the available route
options, normal travel times and potential risk types for each route. The configuration provides the basic input
for agent decision-making, enabling the agent to understand the structural characteristics of the environment.
State.The state represents the observable dynamic information provided by the environment during task
execution, which directly affects the agent’s decisions and behaviors. This dynamic information includes de-
tailed road conditions, such as the occurrence probabilities of different risks and the impact of each risk on travel
time. The agent observes the current state and its dynamic changes, plans travel strategies, and generates travel
decisions.
Based on the nonparametric prompting method, the standardized prompting pattern is constructed, as shown
in Figure 2. The pseudo-code of the LLM-based route choice simulation framework is presented in Algorithm
1.
Individual Human Information
Occupation
 Personality
Risk Preference
 Travel Purpose
Time Pressure
Planning
• Travel Time
• Time Variability
• Route Prioritization
Planning
• Travel Time
• Time Variability
• Route Prioritization
Profile
• Individual Attributes
• Behavior Features
• Constraint Conditions
Profile
• Individual Attributes
• Behavior Features
• Constraint Conditions
Action
• Decision Rules
• Risk Attitudes
• JSON Output
Action
• Decision Rules
• Risk Attitudes
• JSON Output
Travel Environment InformationTravel Environment Information
Travel Tasks
Route Environment
Risk Type
State
• Route Travel Time
• Probability of Risk Occurrence
• Route Travel Time Variability
State
• Route Travel Time
• Probability of Risk Occurrence
• Route Travel Time Variability
Configuration
• Task Objectives
• Optional Routes
• Risk Type
Configuration
• Task Objectives
• Optional Routes
• Risk Type
1
Input
Information
1
Input
Information
2
Standardized
Prompting Pattern
2
Standardized
Prompting Pattern
Travel Environment Prompting Pattern
Context: In a simulated road network, travelers are
tasked with <task objectives>. Multiple <optional
routes> are available. Each route is subject to potential
disturbances, such as <risk type>. The detailed
information for each route is provided as follows:
For route A, <route travel time>, < probability of risk
occurrence>, and <route travel time variability>.
For route B, <route travel time>, < probability of risk
occurrence>, and <route travel time variability>.
...
Travel Environment Prompting Pattern
Context: In a simulated road network, travelers are
tasked with <task objectives>. Multiple <optional
routes> are available. Each route is subject to potential
disturbances, such as <risk type>. The detailed
information for each route is provided as follows:
For route A, <route travel time>, < probability of risk
occurrence>, and <route travel time variability>.
For route B, <route travel time>, < probability of risk
occurrence>, and <route travel time variability>.
...
Human Agent Prompting Pattern
Context: Act as a <occupation> traveler agent with
<risk preference> and <travel purpose>. You have a
<personality>. Under conditions of <time pressure>,
you exhibit <risk attitudes> and <travel behavior
features>. You tend to <route prioritization>. In your
travel decision -making, you evaluate <travel time>,
<time variability>, and apply <decision rules>. In the
simulation environment, you make reasonable travel
decisions based on <constraint conditions>. The <json
output> rules must be strictly observed.
Human Agent Prompting Pattern
Context: Act as a <occupation> traveler agent with
<risk preference> and <travel purpose>. You have a
<personality>. Under conditions of <time pressure>,
you exhibit <risk attitudes> and <travel behavior
features>. You tend to <route prioritization>. In your
travel decision -making, you evaluate <travel time>,
<time variability>, and apply <decision rules>. In the
simulation environment, you make reasonable travel
decisions based on <constraint conditions>. The <json
output> rules must be strictly observed.
2
Standardized
Prompting Pattern
Travel Environment Prompting Pattern
Context: In a simulated road network, travelers are
tasked with <task objectives>. Multiple <optional
routes> are available. Each route is subject to potential
disturbances, such as <risk type>. The detailed
information for each route is provided as follows:
For route A, <route travel time>, < probability of risk
occurrence>, and <route travel time variability>.
For route B, <route travel time>, < probability of risk
occurrence>, and <route travel time variability>.
...
Human Agent Prompting Pattern
Context: Act as a <occupation> traveler agent with
<risk preference> and <travel purpose>. You have a
<personality>. Under conditions of <time pressure>,
you exhibit <risk attitudes> and <travel behavior
features>. You tend to <route prioritization>. In your
travel decision -making, you evaluate <travel time>,
<time variability>, and apply <decision rules>. In the
simulation environment, you make reasonable travel
decisions based on <constraint conditions>. The <json
output> rules must be strictly observed.
3
Agent-Environment
Interaction Layer
3
Agent-Environment
Interaction Layer
• Agent Name
• Agent Type
• Choice Route
Structured
Output
Structured
Output
LLM-based Route Choice Simulation3
Agent-Environment
Interaction Layer
• Agent Name
• Agent Type
• Choice Route
Structured
Output
LLM-based Route Choice Simulation
Figure 2: Standardized prompt generation process based on agent and environmental information
8

Algorithm 1:LLM-based route choice simulation framework
Input:Travel environment information (configuration, state)
Human agent information (profile, planning, action)
Output:Human agents’ route choice simulation results in JSON format
1Configure the OpenAI gpt-5 API (API key and model name);
2Construct the prompt containing travel environment informatione j∈E;
3Construct the prompt containing human agent informationa i∈A;
4for i=1 toN a do
5Match agent prompta i with environment prompte j;
6np j =e j∪{a i|i=1,...,N a};
7NP={np j|j=1,...,N e}
8end
9Invoke thegpt−5 LLM;
10returnjson.loads(results);
11Printname(Agent_i),type,route
4.3. Estimation of cumulative prospect theory parameters and reference point determination
Building on the prospect theory, Tversky and Kahneman (1992) further developed CPT in 1992. CPT
evaluates the cumulative prospect valuePV(x) of alternative options using value functionv(x) and cumulative
decision weightsπ(p). The gains and losses in the value function are relative to a reference pointx 0. When
faced with gains, people tend to avoid risk; when faced with losses, they tend to pursue risk. Furthermore,
people’s aversion to losses is often greater than their preference for the same gains; that is, the value function is
concave in the gain part and convex in the loss part. In this study, the value function is expressed as follows:
v(x)=
 (x−x 0)α x≥x 0 −λ(x0−x) β x<x 0 (4)
where 0< α,β <1 represents the decision maker’s sensitivity to gains and losses, whileλdenotes the risk-
aversion coefficient. Typically,λ≥1, indicating that the decision maker exhibits a risk-averse attitude, and that
the value function is steeper in the loss domain. The cumulative decision weights are defined as follows:
π+(p i)=w(p i +...+p n)−w(p i+1 +...+p n),0≤i≤n(5)
π−(p−j )=w(p −m +...+p −j )−w(p −m +...+p −j−1 ),m≤−j<0 (6)
wherew(p) is the probability weighting function, and its expression is:
w(p)= pγ
(pγ +(1−p) γ)1/γ (7)
where 0< γ <1 represents people tend to overweight rare events with extremely small probabilities while
underweighting more common events with moderate or high probabilities. The weighting function is usually
inversely S-shaped. The cumulative prospect value is expressed as follows:
PV(x)=
Xn
i=0 v(xi)π+(p i)+ X−1 i=−m v(xi)π−(p i) (8)
9

In this study, the prospect utility parameters are estimated by fitting the data generated from LLM-based
agents simulating route choice preferences to the formulations of CPT. The specific form of the value function
is associated with the probability weighting function, which characterizes individuals’ subjective perception
of probabilities. Since decision weighting functions in different domains have the same type of independent
variables, the decision weighting parameter exhibits a degree of universality across different economic sectors,
this study uses the parameter estimate from Wu and Gonzalez (1996) for a general economic sector,γ=0.74.
This study only estimates parametersα,β, andλusing LLMs simulation results.
In the route choice experiments under gain and loss scenarios, it is assumed that a agent receives a gain
of∆x + i with probabilityp i, and incurs a loss of∆x − −i with probabilityp −i. LetP(A j) denote the proportion
of agents choosing routeAin casej, andU(A j) represent the cumulative prospect value of routeAin casej.
Moreover,P(A j >B j)=1/(1+e U(B j)−U(A j)) indicates the probability that routeAis perceived as more valuable
than routeBin casej. Therefore, under the gain case, the sum of squared residuals between the LLM-simulated
route-choice outcomes and those computed from CPT can be expressed as:
f1(α,γ)=
XN+
j=1 (P(A J)−P(A j >B j))2 (9)
whereN + represents the number of gain cases. Under the loss case, the sum of squared residuals for agents’
route choices can be expressed as:
f2(β,λ,γ)=
XN−
j=1 (P(A j)−P(A j >B j))2 (10)
whereN− represents the number of loss cases. In CPT, the reference point serves as the psychological bench-
mark against which gains and losses are evaluated. For human decision-making under uncertain travel times,
the reference point reflects the expected level of travel time. In this study, the reference point is inferred from
the distribution of expected travel times generated by LLM-based agents. During the simulation experiment,
each agent forms an individualized expectation of travel time based on the case information presented. LetN
denote the total number of agents, and lett i represent the expected travel time of agenti. The aggregation of
these expectations provides an empirical basis for determining a case reference point. Formally, the reference
pointx 0 under a given case is computed as:
x0 = 1 N XN i=1 ti (11)
This formulation captures the average tendency of agents’ expectations, thereby ensuring that the subsequent
gain–loss evaluation is grounded in the behavioral patterns revealed by the simulated agents. Unlike traditional
methods that rely on fixed or deterministic reference points, the LLM-based approach for inferring reference
points can more realistically reflect the psychological processes of human agents.
5. Route choice simulation experiments with LLM-based human agents
5.1. Construction of LLM-based human traveler agents
When facing different real-world problems, individuals’ risk attitudes often differ; however, at the group
level, risk-neutral and risk-averse individuals tend to dominate (Holt and Laury, 2002). To realistically simulate
human behavior under uncertain travel conditions, this study references the agent settings in Wang et al. (2025)
and Wang et al. (2024a), defines ten distinct human profiles, and generates 300 agents for each profile, resulting
10

in a total of 3,000 LLM-based agents. Their profile information, as shown in Table 1, covers several key
demographic and behavioral heterogeneity characteristics, including personality, occupation, travel purpose,
and risk preference. Using the standardized prompting pattern proposed in section 4.1, each agent’s individual
profile and planning capability are defined, enabling it to operate as an independent autonomous decision-
making entity. The detailed prompt contents are provided in Appendix A.
Table 1: LLM-based human agents profile information
Type Occupation Personality Risk Preference Travel Purpose
1 Retired worker Cautious and meticulous Averse to time variability; prefers routes with stable travel times Going to the hospital
2 Civil servant Composed and punctual Values stability in travel time and exhibits high sensitivity to temporal fluctuations Daily commuting to work
3 Courier Diligent and pragmatic Prefer the route with stable average time, but can tolerate small range of time fluctuations Commuting for deliveries
4 Parent Responsible and meticulous Prefers routes with stable average travel times, but may choose shorter routes with greater variability Take children to and from school
5 Business manager Steady and pragmatic Values route stability and pursues the optimal time options within the acceptable risk range Attending a business meeting
6 Retirees Peaceful and patient Not concerned with saving time Leisure and recreation
7 Teacher Efficient and rational Tends to balance average travel time and variability Commuting to work
8 Designer Independent and composed Tends to balance average travel time and variability Temporary outing
9 College student Outgoing and spontaneous Values time savings more than reliability; can accept occasional delays Leisure and entertainment
10 Vlogger Outgoing and curious Actively embraces uncertainty in exchange for time-saving routes Visiting and reviewing locations
5.2. Experiment settings
The overall experimental design is consistent with the core behavioral assumptions of CPT (Xu et al., 2011).
First, reference points are constructed to capture agents’ concave preferences in the gain domain and convex
preferences in the loss domain. Second, the scenario settings introduce typical traffic disruptions, such as acci-
dents and unexpected congestion, and quantify their impacts as travel-time increments of different magnitudes.
This design improves the comprehensibility and realism of the scenarios, enabling agents to make judgments
based on real commuting experiences. Next, in each case, the routes are designed to have the same mean travel
time, while the probability of each risk outcome is systematically adjusted to highlight differences in agents’
subjective perceptions of time uncertainty and risk (Zhang et al., 2018). Finally, to balance clarity of infor-
mation presentation and cognitive burden, each route’s travel-time distribution is represented by four discrete
outcomes, which not only clearly characterize different levels of disturbance risk but also improve the stability
and identifiability of parameter estimates (Xu et al., 2011).
Scenario 1:In a simulated road network, agents are assumed to face a commuting trip that must be com-
pleted within 45 minutes. Two alternative routes are available, both having the same average travel time but
subject to potential disruptions such as unexpected congestion, traffic accidents, or temporary road control mea-
sures. For route A, unexpected congestion caused by vehicle breakdowns may add about 5 minutes; traffic
11

accidents such as vehicle rear-end collision will increase the travel time by approximately 10 minutes; and tem-
porary road control measures may result in an additional delay of around 15 minutes. For route B, unexpected
congestion may cause an additional 10-minute delay; traffic accidents may increase travel time by approxi-
mately 20 minutes; and temporary traffic control measures may increase travel time by about 25 minutes. It is
assumed that under all conditions, agents can still arrive within the 45-minute limit; however, earlier arrivals
yield higher travel rewards. In the gain scenario, the occurrence probabilities of the risk events on each route
are shown in Table 2.
Table 2: Travel time and gain distribution for each route
Case Travel time and gain for route A Travel time and gain for route B
1 Time: 30: 20%, 35: 20%, 40: 60%, 45: 0% Time: 20: 10%, 30: 20%, 40: 50%, 45: 20% Gain: 15: 20%, 10: 20%, 5: 60%, 0: 0% Gain: 25: 10%, 15: 20%, 5: 50%, 0: 20%
2 Time: 30: 30%, 35: 30%, 40: 40%, 45: 0% Time: 20: 20%, 30: 20%, 40: 30%, 45: 30% Gain: 15: 30%, 10: 30%, 5: 40%, 0: 0% Gain: 25: 20%, 15: 20%, 5: 30%, 0: 30%
3 Time: 30: 40%, 35: 30%, 40: 20%, 45: 10% Time: 20: 25%, 30: 10%, 40: 45%, 45: 20% Gain: 15: 40%, 10: 30%, 5: 20%, 0: 10% Gain: 25: 25%, 15: 10%, 5: 45%, 0: 20%
4 Time: 30: 50%, 35: 30%, 40: 20%, 45: 0% Time: 20: 30%, 30: 20%, 40: 20%, 45: 30% Gain: 15: 50%, 10: 30%, 5: 20%, 0: 0% Gain: 25: 30%, 15: 20%, 5: 20%, 0: 30%
5 Time: 30: 70%, 35: 20%, 40: 10%, 45: 0% Time: 20: 50%, 30: 0%, 40: 10%, 45: 40% Gain: 15: 70%, 10: 20%, 5: 10%, 0: 0% Gain: 25: 50%, 15: 0%, 5: 10%, 0: 40%
Scenario 2:In a simulated road network, agents are assumed to face a commuting trip that must be com-
pleted within 30 minutes. Two alternative routes are available, both having the same average travel time but
subject to potential disruptions such as unexpected congestion, traffic accidents, or temporary road control mea-
sures. For routes A and B, unexpected congestion caused by vehicle breakdowns may add about 5 minutes;
traffic accidents such as vehicle rear-end collision will increase the travel time by approximately 10 minutes;
and temporary road control measures may result in an additional delay of around 15 minutes. It is assumed that
neither route can reach the destination within 30 minutes (agents can only be on time or late), and the later the
arrival, the higher the loss incurred. In the loss scenario, the occurrence probabilities of the risk events on each
route are shown in Table 3.
Table 3: Travel time and loss distribution for each route
Case Travel time and loss for route A Travel time and loss for route B
6 Time: 30: 70%, 35: 20%, 40: 10%, 45: 0% Time: 30: 80%, 35: 10%, 40: 0%, 45: 10% Loss: 0: 70%, 5: 20%, 10: 10%, 15: 0% Loss: 0: 80%, 5: 10%, 10: 0%, 15: 10%
7 Time: 30: 50%, 35: 30%, 40: 20%, 45: 0% Time: 30: 70%, 35: 0%, 40: 20%, 45: 10% Loss: 0: 50%, 5: 30%, 10: 20%, 15: 0% Loss: 0: 70%, 5: 0%, 10: 20%, 15: 10%
8 Time: 30: 30%, 35: 50%, 40: 15%, 45: 5% Time: 30: 55%, 35: 5%, 40: 30%, 45: 10% Loss: 0: 30%, 5: 50%, 10: 15%, 15: 5% Loss: 0: 55%, 5: 5%, 10: 30%, 15: 10%
9 Time: 30: 15%, 35: 60%, 40: 20%, 45: 5% Time: 30: 45%, 35: 5%, 40: 40%, 45: 10% Loss: 0: 15%, 5: 60%, 10: 20%, 15: 5% Loss: 0: 45%, 5: 5%, 10: 40%, 15: 10%
10 Time: 30: 0%, 35: 70%, 40: 20%, 45: 10% Time: 30: 30%, 35: 10%, 40: 50%, 45: 10% Loss: 0: 0%, 5: 70%, 10: 20%, 15: 10% Loss: 0: 30%, 5: 10%, 10: 50%, 15: 10%
In scenarios 1 and 2, the 3,000 human traveler agents are required to independently make route choice
decisions under 10 different combinations of risk probabilities, and to output their name, agent type, and chosen
12

route.
Scenario 3:In a simulated road network, agents are assumed to face a commuting trip and have three
alternative routes. The average travel time of the three routes is 30 minutes, but there may be unexpected
congestion, traffic accidents or temporary road control measures, and the probability of various emergencies in
each route is not equal. The occurrence probabilities of the risk events on the three routes are shown in Table 4.
The 3,000 human traveler agents are required to independently make a route choice decision among the three
routes and output their name, agent type, expected travel time, and selected route.
Table 4: Travel time distribution for each route in scenario 3
Case Travel time distribution for each route
11
Route A: 12: 15%, 24: 35%, 36: 35%, 48: 15%
Route B: 18: 20%, 26: 30%, 34: 30%, 42: 20%
Route C: 24: 25%, 28: 25%, 32: 25%, 36: 25%
Additionally, this study used OpenAI’s GPT-5 as the simulation generator. The model’s temperature pa-
rameter is set to 1 by default, allowing the generated decisions to retain an appropriate level of behavioral
diversity while avoiding excessive randomness. This setting is consistent with previous behavioral simulation
studies based on LLMs (Brown et al., 2020, Aher et al., 2023, Mou et al., 2025). To ensure the robustness and
reproducibility of the experimental results, each experimental scenario is independently executed three times.
5.3. Experiment results
The route choice distributions of the 3,000 agents across three independent simulations in scenarios 1, 2 and
3 are presented in Appendix B. Based on the three simulation results, the choice counts of each route under the
11 cases are summarized in Table 5. Furthermore, Figure 3 illustrates the distribution of expected travel times
for the 3,000 agents across three independent simulations in experimental scenario 3. It is worth noting that due
to the large number of human agents, the route choice scatter points are highly overplotted, forming a dense
band that appears almost like a straight line, which may also create the illusion that some agents chose both
route A and route B. In fact, this is a visualization artifact caused by point overlap. Taking agents 2,300–2,399
in case 1 as an example, Figure B.12 further presents the detailed choices of these 100 agents.
Using the statistical results of cases 1 to 10 in table 5, the parametersα,βandλare estimated by fitting
equations (9) and (10), yielding the following estimates:α=0.4,β=0.64 andλ=1.43. The corresponding
residual sums of squares aref 1(α,γ)=0.0097 andf 2(β,λ,γ)=0.0022. The goodness of fit values are 1−q
f1(α,γ)/ P5 j=1 (P(A j))2 =0.9332 and 1− q f2(β,λ,γ)/ P10 j=6 (P(A j))2 =0.9497, indicating that the overall
fitting error is small and the fit is acceptable. In terms of parameter interpretation, the valuesα=0.4 and
β=0.64 indicate that the LLM-based agents exhibit pronounced diminishing sensitivity to changes in travel-
time gains and losses. The loss-aversion parameterλ=1.43 indicates that under the same time deviation, the
agent’s subjective sensitivity to the loss of lateness is 1.43 times that of the same gain, reflecting a significant
loss aversion characteristic. Based on these estimated parameters, the cumulative prospect values and choice
probabilities for routes A, B, and C in case 11 are computed, as reported in Table 6.
5.4. Individual-level evaluation of behavioral bias reproduction
To examine whether LLMs can reproduce human behavioral biases in route-choice experiments, this study
evaluates the agents’ role-playing capability and behavioral responses under different risk scenarios at both the
13

Table 5: Route choice results for case 1 to case 11
Case Route type First simulation Second simulation Third simulation Average choice counts Average choice probability
1 Route A 1981 1999 1997 1985.67 66.19% Route B 1019 1001 1023 1014.33 33.81%
2 Route A 1999 2009 1920 1976.00 65.87% Route B 1001 991 1080 1024.00 34.13%
3 Route A 1816 1924 1928 1889.33 62.98% Route B 1184 1076 1072 1110.67 37.02%
4 Route A 1960 2021 1979 1986.67 66.22% Route B 1040 979 1021 1013.33 33.78%
5 Route A 2059 2020 2079 2052.67 68.42% Route B 941 980 921 947.33 31.58%
6 Route A 1403 1474 1435 1437.33 47.91% Route B 1597 1526 1565 1562.67 52.09%
7 Route A 1345 1517 1440 1434.00 47.80% Route B 1655 1483 1560 1566.00 52.20%
8 Route A 1465 1493 1262 1406.67 46.89% Route B 1535 1507 1738 1593.33 53.11%
9 Route A 989 1107 1167 1087.67 36.26% Route B 2011 1893 1833 1912.33 63.74%
10 Route A 737 761 727 741.67 24.72% Route B 2263 2239 2273 2258.33 75.28%
11
Route A 778 718 680 725.33 24.18%
Route B 1049 1025 1031 1035.00 34.50%
Route C 1173 1257 1289 1239.67 41.32%
Table 6: CPT-estimated values and route choice probabilities in case 11
Case Route type Estimated CPT values Estimated choice probability LLM-simulated choice probability
11
Route A -2.1524 28.72% 24.18%
Route B -1.7805 33.77% 34.50%
Route C -1.2899 37.51% 41.32%
individual and environmental levels. At the individual level, this study analyzes the route choice results of 10
different profile types of agents in cases 1 to 10 (see Figure 4), statistically summarizes their choice results (see
Table 7, 8), and compares the demographic characteristics, travel purposes, and risk preferences of different
types of agents.
Overall, risk-averse agents (types 1–5) exhibit the strongest preference for the more reliable route A, with
an average choice proportion of 73.22%. Risk-neutral agents (types 6–8) follow, with an average proportion of
51.33% choosing route A. In contrast, risk-seeking agents (types 9 and 10) almost always choose route B, with
route A chosen only 6.58% of the time on average. These statistics are closely consistent with the behavioral
profiles assigned to each agent type. From the gain–loss perspective, most agent types tend to choose the stable
route A in the gain domain. In particular, risk-averse types 1, 4, and 5 choose route A with a proportion of 100%,
while risk-neutral types 6–8 also show a high average proportion of 69.15% for route A. In the loss domain,
however, the choice proportion of route A decreases markedly for almost all types: for risk-averse agents (types
1–5), it drops from 90.38% to 56.07%, and for risk-neutral agents (types 6–8) it further declines to 33.50%.
14

(a) First simulation result
(b) Second simulation result
(c) Third simulation result
Figure 3: Expected travel time distribution in case 11
Specifically, in case 10, only 17.33% of retired-worker agents (type 1) chose the reliable route A, which
appears, at first glance, to contradict their risk-averse profile. Further analysis shows that although route A has
lower travel time variability, its on-time arrival probability is zero, meaning that choosing route A entails certain
loss of being late. In this case, most cautious agents instead select the more volatile route B. This suggests that
while they are generally risk-averse, they re-evaluate the outcome distribution when lateness is unavoidable
and exhibit a context-dependent decision mechanism rather than mechanically following a “risk-averse” label.
Similarly, within the overall conservative group, courier human agents (type 3) choose route A with an average
probability of 47.17%, which is lower than their probability of choosing route B (52.83%). This can be attributed
to the fact that courier delivery is highly sensitive to on-time or even early arrival, which directly affects income
15

and performance evaluations. Therefore, rather than simply avoiding travel-time variability, this type is, in some
cases, more willing to choose the shorter but more variable route B to gain the potential benefit of earlier arrival.
In summary, different types of agents exhibit significant differences in route choice behavior, indicating that
LLMs can generate behavioral responses through conditional reasoning based on given profiles. Furthermore,
the agents’ route choice results exhibit decision-making behavior consistent with CPT, suggesting that LLMs
can not only simulate individual differences but also reproduce irrational human choice biases under uncertainty.
Table 7: Route choice proportions of the 10 agent types across cases 1 to 10
Case Route type Type 1 Type 2 Type 3 Type 4 Type 5 Type 6 Type 7 Type 8 Type 9 Type 10
1 Route A 100.00% 85.44% 70.00% 100.00% 100.00% 68.89% 70.00% 67.56% 0.00% 0.00% Route B 0.00% 14.56% 30.00% 0.00% 0.00% 31.11% 30.00% 32.44% 100.00% 100.00%
2 Route A 100.00% 94.22% 65.56% 100.00% 100.00% 65.56% 67.78% 65.56% 0.00% 0.00% Route B 0.00% 5.78% 34.44% 0.00% 0.00% 34.44% 32.22% 34.44% 100.00% 100.00%
3 Route A 100.00% 77.78% 44.67% 100.00% 100.00% 74.44% 64.44% 68.44% 0.00% 0.00% Route B 0.00% 22.22% 55.33% 0.00% 0.00% 25.56% 35.56% 31.56% 100.00% 100.00%
4 Route A 100.00% 94.33% 66.67% 100.00% 100.00% 71.22% 66.67% 63.33% 0.00% 0.00% Route B 0.00% 5.67% 33.33% 0.00% 0.00% 28.78% 33.33% 36.67% 100.00% 100.00%
5 Route A 100.00% 94.22% 66.67% 100.00% 100.00% 70.00% 70.00% 83.33% 0.00% 0.00% Route B 0.00% 5.78% 33.33% 0.00% 0.00% 30.00% 30.00% 16.67% 100.00% 100.00%
6 Route A 100.00% 77.78% 31.00% 94.44% 19.11% 41.56% 39.44% 19.67% 23.67% 32.44% Route B 0.00% 22.22% 69.00% 5.56% 80.89% 58.44% 60.56% 80.33% 76.33% 67.56%
7 Route A 100.00% 65.56% 23.78% 88.89% 32.89% 26.22% 40.56% 24.67% 36.67% 38.78% Route B 0.00% 34.44% 76.22% 11.11% 67.11% 73.78% 59.44% 75.33% 63.33% 61.22%
8 Route A 100.00% 53.56% 53.00% 52.11% 55.56% 66.22% 53.67% 34.78% 0.00% 0.00% Route B 0.00% 46.44% 47.00% 47.89% 44.44% 33.78% 46.33% 65.22% 100.00% 100.00%
9 Route A 55.44% 53.33% 0.00% 61.67% 58.56% 50.22% 50.00% 33.33% 0.00% 0.00% Route B 44.56% 46.67% 100.00% 38.33% 41.44% 49.78% 50.00% 66.67% 100.00% 100.00%
10 Route A 17.33% 53.22% 50.33% 51.11% 53.00% 22.22% 0.00% 0.00% 0.00% 0.00% Route B 82.67% 46.78% 49.67% 48.89% 47.00% 77.78% 100.00% 100.00% 100.00% 100.00%
Table 8: Route choice proportions of the 10 agent types in gain and loss cases
Route type Type 1 Type 2 Type 3 Type 4 Type 5 Type 6 Type 7 Type 8 Type 9 Type 10
Gain case Route A 100.00% 89.20% 62.71% 100.00% 100.00% 70.02% 67.78% 69.64% 0.00% 0.00% Route B 0.00% 10.80% 37.29% 0.00% 0.00% 29.98% 32.22% 30.36% 100.00% 100.00%
Loss case Route A 74.56% 60.69% 31.62% 69.64% 43.82% 41.29% 36.73% 22.49% 12.07% 14.24% Route B 25.44% 39.31% 68.38% 30.36% 56.18% 58.71% 63.27% 77.51% 87.93% 85.76%
Average Route A 87.28% 74.94% 47.17% 84.82% 71.91% 55.66% 52.26% 46.07% 6.03% 7.12% Route B 12.72% 25.06% 52.83% 15.18% 28.09% 44.34% 47.74% 53.93% 93.97% 92.88%
5.5. Environmental-level evaluation of context-dependent group behavior
Across three repeated simulation experiments, the average expected travel time of each agent type falls
within the feasible travel time range of the corresponding route (as shown in Figure 5). The overall mean of
expected travel time across agent types is 28.83 minutes, which is very close to the average travel time of 30
minutes for the three routes. This indicates that, regardless of risk preference, agents’ subjective expectations
16

(a) Type-1 agent
 (b) Type-2 agent
(c) Type-3 agent
 (d) Type-4 agent
(e) Type-5 agent
 (f) Type-6 agent
(g) Type-7 agent
 (h) Type-8 agent
(i) Type-9 agent
 (j) Type-10 agent
Figure 4: Proportion of choices for route A
17

are generally centered around the mean and are not reduced simply because a route contains a small probability
of extremely short travel times. In other words, the travel time distributions induce time expectations that are
more consistent with rational distributional characteristics, rather than being dominated by extreme tail events.
Moreover, in terms of the stability of expected travel time, most agent types exhibit relatively low variance. For
example, types 4 and 6 show very small variances, and their expected travel times remain almost unchanged in
different replication experiments.
Although the overall expectation level is relatively stable, differences still exist in the experimental repro-
duction among different agent types. This indicates that the travel environment does not output a single fixed
time perception. Instead, while maintaining stable outputs, it allows different agent types to exhibit varying
degrees of sensitivity to uncertainty. For instance, type 7 shows a relatively low mean expected travel time but a
large variance. This does not contradict its risk-preference setting; rather, it can be consistently explained by its
profile characteristics. As a teacher commuter with a moderate level of time pressure, the type 7 agents are ra-
tional and efficiency-oriented, can tolerate minor fluctuations, and tend to lower their subjective expected travel
time more actively when environmental risk is low. Importantly, risk neutrality does not imply that expectations
do not fluctuate; instead, it reflects a tendency to avoid extreme risk aversion or risk seeking and to balance
efficiency and stability within a tolerable range of uncertainty.
Furthermore, by statistically summarizing the route choice results in case 11, we obtain the group choice
results in Table 9. As shown in Table 9, conservative human agents (type 1-5) overall tend to prefer the route
C with lower travel time variability (approximately 62.11%) as well as route B with moderate variability (ap-
proximately 29.64%), which is consistent with the individual-level findings that conservative agents favor stable
options. Risk-neutral human agents (type 6-8) distribute their choices in a relatively balanced way across the
three routes. Risk-seeking human agents show a stronger preference for Route A (approximately 48.78%),
which offers shorter travel times but also larger fluctuations. Notably, within the conservative group, type 3
income-constrained courier agents still exhibit a preference for route B (approximately 55.89%). This is consis-
tent with their behavior in the two-route settings, where they moderately accept risk to achieve earlier deliveries,
demonstrating behavioral continuity across scenarios.
In summary, at the environmental level, the expected travel times and route choice results in case 11 reflect
rational perceptions of route travel time distributions while also exhibiting clear behavioral differentiation across
risk types. These differences are consistent with the predefined profiles of the human agents and corroborate the
individual level analysis. Therefore, the LLM-based agents are able not only to reproduce human non-rational
choice biases at the individual level but also to generate context-dependent group behavioral patterns at the
environmental level.
Table 9: Route choice proportions of the 10 agent types in cases 11
Case Route type Type 1 Type 2 Type 3 Type 4 Type 5 Type 6 Type 7 Type 8 Type 9 Type 10
11
Route A 0.00% 2.67% 18.00% 2.00% 18.55% 39.67% 31.45% 31.89% 48.33% 49.22%
Route B 4.11% 34.55% 55.89% 5.89% 47.78% 30.22% 40.33% 38.89% 36.56% 50.78%
Route C 95.89% 62.78% 26.11% 92.11% 33.67% 30.11% 28.22% 29.22% 15.11% 0.00%
5.6. Method comparison
To further examine the accuracy of LLMs in reproducing human behavioral biases, this section compares the
parameters obtained from LLM-based simulations with those estimated from real-world behavioral experiments.
18

Figure 5: Distribution of expected travel time for the 10 agent types in case 11
This study adopts the route choice experimental data conducted by Xu et al. (2011) based on real respondents
as the reference benchmark. The experiment designed two travel routes with different travel time distributions
and recorded respondents’ route choices results under the given scenario. For horizontal comparison, this
study selects four representative sets of parameters, all of which were estimated under relatively universal
experimental conditions and have cross-scenario representativeness: (1) the parameters (0.37, 0.59, 1.51) and
(0.50, 0.54, 1.85) estimated based on the route choice experiment of real respondents in Xu et al. (2011) and
Zhang et al. (2018). (2) Two sets of classic prospect utility parameters (0.52, 0.52, 2.25) and (0.99, 0.99,
2.25) from non-travel decision situations (Xu et al., 2011). These parameters are widely used to characterize
risk preferences in domains such as finance and gambling. (3) The prospect utility parameters (0.40, 0.64,
1.43) estimated based on the simulated data of LLM human agents in this study. In this scenario, CPT is
used to compute the prospect utility of each route and the corresponding choice probabilities under different
parameter sets. The error values between the prediction results and the route choice results of real respondents
are calculated using equation 12, as shown in Table 10. Equation 12 represents the sum of squared residuals
between the predicted values ˜p l and the observed valuesp l overLroutes. Figure 6 presents the total error
between the predicted and observed values in Xu et al. (2011)’s study.
e=
XL
l=1 ( ˜pl−p l)2 (12)
Overall, as shown in Figure 6, the parameters estimated using the LLM-based route choice simulation
method in this study have the smallest total error under multiple reference points, at 0.0682. The total errors of
the parameter sets from Xu et al. (2011) and Zhang et al. (2018) are 0.0812 and 0.1004, respectively, whereas
the classic parameter (0.99, 0.99, 2.25) from non-travel fields has the largest error, at 0.6634. This indicates
that cross-domain general parameters cannot effectively characterize risky behavior in route choice, whereas
the proposed method better approximates actual human decision-making and achieves higher overall predictive
accuracy.
Furthermore, as shown in Table 10, the parameters in this paper exhibit the smallest prediction error at refer-
ence points 30 and 35, with the error at reference point 40 only slightly higher than that of the first group, and are
not optimal at reference point 50. Because reference points can be considered potential psychological thresh-
olds that vary with individual and scenario factors, they often fluctuate with changes in individual attributes and
19

context. This paper achieves the minimum total error across multiple reference points. At a reference point
of 50, the proposed method yields a relatively large local error; however, this error remains smaller than that
obtained using the parameters estimated from the real-world behavioral experiment reported in Xu et al. (2011).
This indicates that when both routes fall into the loss domain, choice probabilities are more sensitive to the loss
aversion coefficient and the curvature of the value function, thus amplifying the error differences of different
parameter combinations at this reference point.
The aforementioned parameter sets are subsequently applied to predict the three-route choice results in case
11. Specifically, each parameter set is incorporated into the CPT framework to compute the prospect values and
choice probabilities of the three routes in case 11, and the predicted results are compared with the simulation
route choice results generated by the LLM-based human agents. The corresponding prediction results and errors
values are shown in Table 11. As shown in Table 11, all parameter sets exhibit the similar bias trend in predicting
route choices results. The predicted probability of choosing route A is generally higher than the corresponding
proportion observed for the LLM-based human agents in the simulation, while the predicted probabilities of
choosing routes B and C are generally lower. This indicates that, compared to the simulated choice behavior of
the LLM-based human agents, the parameter prediction results tend to overestimate the attractiveness of routes
with shorter possible travel times, while underestimating the attractiveness of routes with more stable travel
times. In terms of error metrics, the method presented in this paper has the smallest prediction error in case 11,
at only 0.0036, while the parameter combination (0.99, 0.99, 2.25) corresponds to the largest prediction error,
at 0.0110. This trend is consistent with the conclusions obtained in the real respondent experiments.
Table 10: Prediction results based on CPT under different parameters
Parameters Reference point Route 1 Route 2 Error value
(0.37, 0.59, 1.51)
30 69.31% 30.69% 0.0050
35 29.39% 70.61% 0.0100
40 14.33% 85.67% 0.0003
50 44.65% 55.35% 0.0659
(0.50, 0.54, 1.85)
30 75.63% 24.37% 0.0257
35 33.86% 66.14% 0.0267
40 13.69% 86.31% 0.0007
50 41.88% 58.12% 0.0473
(0.52, 0.52, 2.25)
30 78.37% 21.63% 0.0396
35 31.24% 68.76% 0.0160
40 10.94% 89.06% 0.0042
50 41.43% 58.57% 0.0446
(0.99, 0.99, 2.25)
30 11.85% 88.15% 0.5503
35 2.94% 97.06% 0.0749
40 6.63% 93.37% 0.0157
50 37.12% 62.88% 0.0225
(0.40, 0.64, 1.43)
30 66.69% 33.31% 0.0011
35 27.32% 72.68% 0.0050
40 13.99% 86.01% 0.0005
50 44.04% 55.96% 0.0616
20

Figure 6: Error values in real behavioral experiments
Table 11: Prediction results and error values in LLM simulation experiments
Parameters Reference point Route A Route B Route C Error value
(0.37, 0.59, 1.51) 28.83 29.12% 33.59% 37.26% 0.0042
(0.50, 0.54, 1.85) 28.83 30.61% 33.37% 36.02% 0.0071
(0.52, 0.52, 2.25) 28.83 31.04% 33.42% 35.54% 0.0082
(0.99, 0.99, 2.25) 28.83 31.81% 34.05% 34.13% 0.0110
(0.40, 0.64, 1.43) 28.83 28.72% 33.77% 37.51% 0.0036
5.7. Further analysis
In experimental scenarios 1 and 2, gains and losses were designed based on different reference points.
Therefore, this study introduces experimental scenario 4, in which gains and losses are defined under the same
reference point to test the robustness of the method.
Scenario 4:In a simulated road network, agents are assumed to face a commuting trip that must be com-
pleted within 30 minutes. There are two alternative routes, both having potential disruptions such as unexpected
congestion, traffic accidents or temporary road control measures. For route A, unexpected congestion may
cause an additional 5-minute delay; traffic accidents may increase travel time by approximately 10 minutes; and
temporary traffic control measures may increase travel time by about 15 minutes. For route B, unexpected con-
gestion may cause an additional 5-minute delay; traffic accidents may increase travel time by approximately 15
minutes; and temporary traffic control measures may increase travel time by about 20 minutes. The occurrence
probabilities of the risk events and the time gains and losses for each route are shown in Table 12.
Table 12: Travel time distribution for each route in case 12 and 13
Case Travel time for route A Travel time for route B
12 Time: 15: 30%, 20: 30%, 25: 20%, 30: 20% Time: 10: 20%, 15: 20%, 25: 30%, 30: 30% Gain: 15: 30%, 10: 30%, 5: 20%, 0: 20% Gain: 20: 20%, 15: 20%, 5: 30%, 0: 30%
13 Time: 30: 20%, 35: 20%, 40: 30%, 45: 30% Time: 30: 35%, 35: 20%, 45: 30%, 50: 15% Loss: 0: 20%, 5: 20%, 10: 30%, 15: 30% Loss: 0: 35%, 5: 20%, 15: 30%, 20: 15%
21

Figure B.11 shows the simulation results of 3,000 agents in scenario 4. Based on three independent sim-
ulation experiments, the choice proportions of each route choice were statistically analyzed. In the gain case,
the probability of choosing route A is 54.10%, and the probability of choosing route B is 45.90%. In the loss
case, the probability of choosing route A is 45.07%, and the probability of choosing route B is 54.93%. This
behavioral pattern is consistent with those observed in experiments using different reference points.
Table 13: Prediction results and error values for case 12 and 13
Parameters Case 12 Case 13 Error value
(0.37, 0.59, 1.51) Route A: 53.10% Route A: 44.18% 0.0004Route B: 46.90% Route B: 55.82%
(0.50, 0.54, 1.85) Route A: 52.95% Route A: 42.18% 0.0019Route B: 47.05% Route B: 57.82%
(0.52, 0.52, 2.25) Route A: 52.87% Route A: 40.51% 0.0045Route B: 47.13% Route B: 59.49%
(0.99, 0.99, 2.25) Route A: 38.79% Route A: 70.79% 0.1792Route B: 61.21% Route B: 29.21%
(0.40, 0.64, 1.43) Route A: 53.11% Route A: 45.18% 0.0002Route B: 46.89% Route B: 54.82%
Furthermore, these results are compared with the prediction results under different CPT parameters, as
shown in Table 13. From the perspective of route choice prediction error, the CPT parameters estimated using
the LLM-based simulation method proposed in this study achieve higher prediction accuracy, with the predic-
tion error reduced to 0.0002. Compared with traditional methods, the proposed method also maintains robust
predictive performance in scenarios with consistent reference points.
6. Conclusion
This study primarily investigates whether LLMs can reproduce human behavioral biases in route choices
without explicitly specifying CPT parameters, and addresses the bottleneck in CPT parameter estimation by
constructing large-scale route-choice behavioral experiments.
The contributions of this study are manifested in two key aspects. First, this study proposes a standardized
prompt-based generation process for constructing human agents and travel environments, enabling LLMs to
realistically reproduce human route-choice behavioral biases and thereby enhancing the methodological feasi-
bility and credibility of applying LLMs to human behavior research. Second, this study proposes an LLM-based
method for estimating CPT parameters, which leverages the scalability of LLMs to batch-generate large-scale
heterogeneous agents, validates the capability of LLMs in behavioral data generation, parameter estimation, and
theoretical mechanism quantification, and provides a low marginal cost, scalable computational experimental
paradigm for human behavior research.
Future research can be expanded in the following three aspects. First, this study mainly focuses on the
independent behavioral decisions made by agents in given scenarios. Further research could introduce learning,
communication, and social interaction mechanisms to construct a dynamically evolving multi-agent interaction
system. Second, this study mainly uses LLMs to reproduce non-rational behavioral biases in human choices.
Future research can integrate LLM-based simulation with traffic assignment and equilibrium models to inves-
tigate the evolution and equilibrium characteristics of traffic flows after behavioral biases are introduced at
22

the network level. Third, with the development of multimodal LLMs and tool invocation capabilities, future
research could introduce external information tools such as maps and real-time events to make the agents’
perception, reasoning, and decision-making more closely resemble the real decision process.
Data availability
Data will be made available on request.
Declaration of competing interest
The authors declare that there is no competing financial interests and personal relationships with other
people or organizations.
Acknowledgments
This research is supported by the National Natural Science Foundation of China (72431006, 72271175).
CRediT authorship contribution statement
Jiangtao Han: Writing-original draft, Methodology, Data curation, Visualization;Shoufeng Ma: Concep-
tualization, Supervision, Funding acquisition;Shuxian Xu: Writing – review & editing, Funding acquisition,
Methodology;Geng Li: Writing – review & editing, Formal analysis;Shuai Ling: Writing – review & editing,
Validation;Ning Jia: Writing – review & editing;Zhengbing He: Writing – review & editing, Supervision,
Conceptualization.
References
Aher, G.V ., Arriaga, R.I., Kalai, A.T., 2023. Using large language models to simulate multiple humans and
replicate human subject studies, in: International conference on machine learning, PMLR. pp. 337–371.
Akyürek, E., Schuurmans, D., Andreas, J., Ma, T., Zhou, D., 2022. What learning algorithm is in-context
learning? investigations with linear models. arXiv preprint arXiv:2211.15661 .
Bagaïni, A., Liu, Y ., Kapoor, M., Son, G., Bürkner, P.C., Tisdall, L., Mata, R., 2025. A systematic review and
meta-analyses of the temporal stability and convergent validity of risk preference measures. Nature Human
Behaviour 9, 700–712.
Barberis, N.C., 2013. Thirty years of prospect theory in economics: A review and assessment. Journal of
economic perspectives 27, 173–196.
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G.,
Askell, A., et al., 2020. Language models are few-shot learners. Advances in neural information processing
systems 33, 1877–1901.
Chen, W., Su, Y ., Zuo, J., Yang, C., Yuan, C., Chan, C.M., Yu, H., Lu, Y ., Hung, Y .H., Qian, C., et al., 2024.
Agentverse: Facilitating multi-agent collaboration and exploring emergent behaviors., in: ICLR.
23

Di, X., He, X., Guo, X., Liu, H.X., 2014. Braess paradox under the boundedly rational user equilibria. Trans-
portation Research Part B: Methodological 67, 86–108.
Dong, Q., Li, L., Dai, D., Zheng, C., Ma, J., Li, R., Xia, H., Xu, J., Wu, Z., Chang, B., et al., 2024. A survey
on in-context learning, in: Proceedings of the 2024 conference on empirical methods in natural language
processing, pp. 1107–1128.
Fox, C.R., Erner, C., Walters, D.J., 2015. Decision under risk: From the field to the laboratory and back. The
Wiley Blackwell handbook of judgment and decision making 2, 41–88.
Geng, K., Wang, Y ., Cherchi, E., Guarda, P., 2023. Commuter departure time choice behavior under congestion
charge: Analysis based on cumulative prospect theory. Transportation research part A: policy and practice
168, 103564.
Ghader, S., Darzi, A., Zhang, L., 2019. Modeling effects of travel time reliability on mode choice using
cumulative prospect theory. Transportation Research Part C: Emerging Technologies 108, 245–254.
Henn, V ., Ottomanelli, M., 2006. Handling uncertainty in route choice models: From probabilistic to possibilis-
tic approaches. European journal of operational research 175, 1526–1538.
Holt, C.A., Laury, S.K., 2002. Risk aversion and incentive effects. American economic review 92, 1644–1655.
Hu, Y ., Feng, T., Li, M., 2025. Examining the temporary use behavior of autonomous vehicles under uncertainty:
A stated preference analysis. Transportation Research Part A: Policy and Practice 198, 104520.
Hua, W., Fan, L., Li, L., Mei, K., Ji, J., Ge, Y ., Hemphill, L., Zhang, Y ., 2023. War and peace (waragent): Large
language model-based multi-agent simulation of world wars. arXiv preprint arXiv:2311.17227 .
Jou, R.C., Chen, K.H., 2013. An application of cumulative prospect theory to freeway drivers’ route choice
behaviours. Transportation Research Part A: Policy and Practice 49, 123–131.
Kahneman, D., Tversky, A., 1979. Prospect theory: An analysis of decision under risk. Econometrica 47,
263–292.
Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., Neubig, G., 2023a. Pre-train, prompt, and predict: A systematic
survey of prompting methods in natural language processing. ACM computing surveys 55, 1–35.
Liu, Z., Yao, W., Zhang, J., Xue, L., Heinecke, S., Murthy, R., Feng, Y ., Chen, Z., Niebles, J.C., Arpit, D.,
et al., 2023b. Bolaa: Benchmarking and orchestrating llm-augmented autonomous agents. arXiv preprint
arXiv:2308.05960 .
Mou, X., Liang, J., Lin, J., Zhang, X., Liu, X., Yang, S., Ye, R., Chen, L., Kuang, H., Huang, X.J., et al., 2025.
Agentsense: Benchmarking social intelligence of language agents through interactive scenarios, in: Proceed-
ings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational
Linguistics: Human Language Technologies (V olume 1: Long Papers), pp. 4975–5001.
Murphy, R.O., ten Brincke, R.H., 2018. Hierarchical maximum likelihood parameter estimation for cumulative
prospect theory: Improving the reliability of individual risk parameter estimates. Management Science 64,
308–326.
24

Nguyen, T.T., Nguyen, Q.V .H., Nguyen, D.T., Nguyen, D.T., Huynh-The, T., Nahavandi, S., Nguyen, T.T.,
Pham, Q.V ., Nguyen, C.M., 2022. Deep learning for deepfakes creation and detection: A survey. Computer
Vision and Image Understanding 223, 103525.
Park, J.S., O’Brien, J., Cai, C.J., Morris, M.R., Liang, P., Bernstein, M.S., 2023. Generative agents: Interactive
simulacra of human behavior, in: Proceedings of the 36th annual acm symposium on user interface software
and technology, pp. 1–22.
Qi, H., Jia, N., Qu, X., He, Z., 2023. Investigating day-to-day route choices based on multi-scenario laboratory
experiments, part i: Route-dependent attraction and its modeling. Transportation Research Part A: Policy and
Practice 167, 103553.
Qi, H., Jia, N., Qu, X., He, Z., 2024. Investigating day-to-day route choices based on multi-scenario labora-
tory experiments, part ii: Route-dependent attraction-based stochastic process model. Communications in
Transportation Research 4, 100123.
Qian, C., Liu, W., Liu, H., Chen, N., Dang, Y ., Li, J., Yang, C., Chen, W., Su, Y ., Cong, X., et al., 2024.
Chatdev: Communicative agents for software development, in: Proceedings of the 62nd Annual Meeting of
the Association for Computational Linguistics (V olume 1: Long Papers), pp. 15174–15186.
Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Hambro, E., Zettlemoyer, L., Cancedda, N.,
Scialom, T., 2023. Toolformer: Language models can teach themselves to use tools. Advances in Neural
Information Processing Systems 36, 68539–68551.
Smith, M.J., 1984. The stability of a dynamic model of traffic assignment—an application of a method of
lyapunov. Transportation science 18, 245–252.
Sumers, T., Yao, S., Narasimhan, K., Griffiths, T., 2023. Cognitive architectures for language agents. Transac-
tions on Machine Learning Research .
Thomas, T., Straub, D., Tatai, F., Shene, M., Tosik, T., Kersting, K., Rothkopf, C.A., 2024. Modelling dataset
bias in machine-learned theories of economic decision-making. Nature Human Behaviour 8, 679–691.
Tversky, A., Kahneman, D., 1992. Advances in prospect theory: Cumulative representation of uncertainty.
Journal of Risk and uncertainty 5, 297–323.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł., Polosukhin, I., 2017.
Attention is all you need. Advances in neural information processing systems 30.
Wang, C., Chen, S., Wu, Y ., Zhang, Z., Zhou, L., Liu, S., Chen, Z., Liu, Y ., Wang, H., Li, J., et al., 2023. Neural
codec language models are zero-shot text to speech synthesizers. arXiv preprint arXiv:2301.02111 .
Wang, J., Jiang, R., Yang, C., Wu, Z., Onizuka, M., Shibasaki, R., Koshizuka, N., Xiao, C., 2024a. Large
language models as urban residents: An llm agent framework for personal mobility generation. Advances in
Neural Information Processing Systems 37, 124547–124574.
Wang, L., Duan, P., He, Z., Lyu, C., Chen, X., Zheng, N., Yao, L., Ma, Z., 2025. Agentic large language models
for day-to-day route choices. Transportation Research Part C: Emerging Technologies 180, 105307.
25

Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y ., et al., 2024b.
A survey on large language model based autonomous agents. Frontiers of Computer Science 18, 186345.
Weng, L., 2023. Llm-powered autonomous agents. lilianweng.github.io URL:https://lilianweng.
github.io/posts/2023-06-23-agent/.
Wu, G., Gonzalez, R., 1996. Curvature of the probability weighting function. Management science 42, 1676–
1690.
Wu, J., Sun, H., Wang, D.Z., Zhong, M., Han, L., Gao, Z., 2013. Bounded-rationality based day-to-day evolu-
tion model for travel behavior analysis of urban railway network. Transportation Research Part C: Emerging
Technologies 31, 73–82.
Xu, H., Zhou, J., Xu, W., 2011. A decision-making rule for modeling travelers’ route choice behavior based on
cumulative prospect theory. Transportation Research Part C: Emerging Technologies 19, 218–228.
Xu, Y ., Wang, S., Li, P., Luo, F., Wang, X., Liu, W., Liu, Y ., 2023. Exploring large language models for
communication games: An empirical study on werewolf. arXiv preprint arXiv:2309.04658 .
Yan, Y ., Liu, T., Yin, Y ., 2026. Valuing time in silicon: Can large language models replicate human value of
travel time. Travel Behaviour and Society 44, 101245.
Yang, F., Zhang, D., 2009. Day-to-day stationary link flow pattern. Transportation Research Part B: Method-
ological 43, 119–126.
Yang, J., Jiang, G., 2014. Development of an enhanced route choice model based on cumulative prospect theory.
Transportation Research Part C: Emerging Technologies 47, 168–178.
Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y ., Narasimhan, K., 2023. Tree of thoughts: Deliberate
problem solving with large language models. Advances in neural information processing systems 36, 11809–
11822.
Zhang, C., Liu, T.L., Huang, H.J., Chen, J., 2018. A cumulative prospect theory approach to commuters’ day-
to-day route-choice modeling with friends’ travel information. Transportation Research Part C: Emerging
Technologies 86, 527–548.
Zhang, D., Nagurney, A., 1996. On the local and global stability of a travel route choice adjustment process.
Transportation Research Part B: Methodological 30, 245–262.
Zhang, F., Lv, H., Xu, Z., Feng, T., Ji, Y ., Blythe, P., 2026. Charging mode choice of electric micromobility
users under uncertainty. Transportation Research Part A: Policy and Practice 204, 104827.
Zhou, X., Zhu, H., Mathur, L., Zhang, R., Yu, H., Qi, Z., Morency, L.P., Bisk, Y ., Fried, D., Neubig, G.,
et al., 2023. Sotopia: Interactive evaluation for social intelligence in language agents. arXiv preprint
arXiv:2310.11667 .
Zhou, Y ., Wang, P., Zheng, S., Zhao, M., Lam, W.H., Chen, A., Sze, N., Chen, Y ., 2024. Modeling dynamic
travel mode choices using cumulative prospect theory. Transportation Research Part A: Policy and Practice
179, 103938.
26

Appendix A. Prompts for constructing individual human agents
Agent type: Cautious
You are a traveler AI agent representing a cautious elderly individual with a pronounced
tendency toward risk aversion. You are a retired employee, and your primary travel
purpose is to visit the hospital for a medical check-up. Under conditions of high time
pressure, you place great emphasis on the reliability and predictability of your trip.
You are conservative, meticulous, and highly organized, showing strong sensitivity to
variations in travel time. You tend to prefer stable routes with minimal fluctuations to
ensure punctuality and peace of mind. In your travel decision-making, you usually evaluate
the average travel time and volatility of each path, and tend to choose a highly stable
travel path as a travel plan. In the simulation environment, you make well-reasoned travel
decisions based on the cognition and feeling of your own role. Your decision-making logic
is clear and structured, reflecting the behavioral characteristics of a risk-averse
individual and demonstrating a preference for stability in travel time.
Agent type: Conservative
You are a traveler AI agent representing a conservative commuter with a moderately risk-averse
tendency. Your occupation is a civil servant, and your personality characteristics are
cautions, steady and punctual. Your primary daily travel purpose is commuting to work,
under conditions of high time pressure, where punctual arrival is particularly important
to you. You value order, planning and certainty, and you tend to avoid the stress caused
by uncertainty. You will ensure the reliability of routes, but you will also tend to take
risks because of good mood or under lower time pressure, and choose a route with short
travel time but high volatility. In travel decision-making, you tend to comprehensively
evaluate the travel time and sudden risk of each route. However, your decisions can
sometimes be influenced by emotions, leading you to choose riskier routes with shorter
expected travel times. In the simulation environment, you will take the initiative to make
reasonable travel decisions based on the cognition and feelings of your own simulation
roles. Your decision-making style is rational, clear and logical, effectively reflecting
a general preference for stability and punctuality in travel time under most circumstances.
Agent type: Income-limited
You are a traveler AI agent representing an income-constrained worker with a moderately risk-
averse tendency. Your occupation is a courier, the main purpose of travel is commuting and
performing delivery tasks under high time pressure. Your character is diligent, thrifty
and focusing on practicality and efficiency. In the travel, you tend to choose the route
with less risk and overall reliability, but also choose the route with shorter travel time
and greater time fluctuation. In the decision-making process, you will consider factors
such as traffic accidents and congestion, and choose the most appropriate route to ensure
the successful completion of the delivery task. In a simulated environment, you will take
the initiative to make well-founded travel decisions based on the cognition and feelings
of your role. Your behavior shows a realistic and robust way of thinking, expressing direct
and logical pragmatic features.
Agent type: Time-sensitive
You are a traveler AI agent representing a risk-averse individual responsible for taking
children to and from school. You are meticulous, organized, and highly responsible. Your
primary goal is to ensure punctuality while maintaining a balance between reliability and
time efficiency. In your travel decisions, you rely on rational analysis, comprehensively
evaluating each route’s average travel time, time variability, and potential disruptions.
You typically choose routes that optimize expected arrival time while ensuring basic
punctuality. When a route can save more time while keeping punctuality within an acceptable
range, you are willing to tolerate moderate variability; however, if the time savings are
27

minimal and variability is high, you tend to select a more stable route. When faced with
dynamic changes, you make timely judgments based on travel time and its fluctuation. In
the simulation environment, you make well-reasoned travel decisions grounded in your
role’s cognition and perception. Your decision-making is rational, structured, and
reflective of a parent’s realistic trade-off between temporal stability and overall
travel efficiency.
Agent type: Composed
You are a traveler AI agent representing a risk-averse business manager. Your occupation is a
business manager, and your primary travel purpose is attending a meeting, where punctual
arrival is very importance. You are steady, pragmatic, and decisive, focusing on results
and efficiency. In travel decision-making, you comprehensively evaluate each route’s
average travel time, delay probability, and real-time traffic conditions. You tend to
choose routes with high reliability and low variability, but you also favor shorter travel
times, even if there are risks. You can accept risks within a reasonable range, and when
faced with dynamic information, you are strategic, tend to be flexible in adjusting plans,
and maintain efficient decision-making and execution under sudden traffic changes or
external disturbances to ensure that meetings arrive on time. In the simulation environment,
you make decisions based on rational judgment and goal orientation consistent with your role.
Your thinking is clear and logical, your actions are decisive and pragmatic, and your
behavior fully reflects the characteristics of a business traveler who balances efficiency
and stability while remaining results-oriented.
Agent type: Relaxed
You are a traveler AI agent representing a leisure and risk-neutral retired traveler. Your
occupation is retired, and your primary travel purpose is leisure and recreation, with a
moderate level of time pressure. You are calm, peaceful, and patient, showing no particular
aversion or attraction to travel time variability. You evaluate each route primarily based
on its average travel time. You will choose a route with low time variability, but you will
also choose a route with short travel time though greater uncertainty. In your travel
decisions, you can comprehensively assess each route’s average travel time and variability.
When facing traffic changes, you remain composed and do not frequently alter your
plans—only when significant delays occur do you carefully consider adjusting your route.
In the simulation environment, you make reasoned travel decisions based on your role’s
cognition and perception. Your behavior is steady and unhurried, fully reflecting the
characteristics of a retiree’s relaxed travel experience.
Agent type: Rational
You are a traveler AI agent representing a rational decision-making style and a risk-neutral
preference. Your occupation is a teacher, the purpose of travel is daily commuting with
a moderate level of time pressure. Your personality is rational, self-disciplined, focus
on planning and efficiency, tend to arrange time reasonably before travel, and are
moderately sensitive to the fluctuation of travel time. You hope that the travel time
will be shorter, but also hope that the travel process will remain stable and controllable.
Your risk preference is to pursue higher efficiency under the premise of reliability,
tolerating minor fluctuations in travel time. In travel decisions, you strive to balance
average travel time and temporal stability. When faced with dynamic traffic information,
you can comprehensively analyze and adjust when the risk is beyond the tolerance range.
In the simulation environment, you make reasoned travel decisions based on your decisions
based on your cognition and perception as this role. Your decision logic is clear and
your actions are steady, fully demonstrating the characteristics of a rational individual
who carefully balances travel efficiency and time stability.
Agent type: Flexible
28

You are a traveler AI agent representing a remote worker with flexible thinking and risk-neutral
preference. Your occupation is a freelancer or designer, and your main travel purposes
include working outside or attending occasional meetings. You experience moderate time
pressure, and both travel efficiency and overall experience are important to you. You are
composed, independent, and highly adaptable, capable of adjusting your travel plans flexibly
according to circumstances. Your risk preference is to choose faster routes while remaining
open to stable travel time. In your travel decisions, you rely on comprehensive analysis,
evaluating the average travel time and variability of each route. When facing dynamic
traffic information, you can quickly assess the situation and make appropriate
adjustments, maintaining both flexibility and initiative. In the simulation environment,
you make reasoned travel decisions based on your cognition and perception as this role.
Your behavior is open and logically consistent, reflecting a balanced preference
between stability and exploration.
Agent type: Adventurous
You are a traveler AI agent representing an adventurous young traveler with a risk-seeking
preference. Your occupation is a college student, and your main travel purpose is to
participate in leisure and entertainment activities. You experience low time pressure,
and the enjoyment and experience of the journey are just as important to you as
reaching the destination. You are outgoing, spontaneous, and curious, enjoying exploring
the unknown and trying new things. You hold a positive attitude toward change and
uncertainty. In travel decision-making, you tend to choose routes that save more time,
even if they involve higher variability and uncertainty. Even when facing risks or
delays, you maintain a relaxed mindset, considering risk and change as part of the
travel experience—something that can even bring excitement and satisfaction. When
encountering dynamic information or unexpected events, you tend to respond quickly and
adjust your plans flexibly to embrace new possibilities and challenges. In the simulation
environment, you make reasoned travel decisions based on your cognition and perception
as this role. Your thinking style is open and adventurous, your expression is natural
and lively, and your decisions reflect a pursuit of speed, freedom, and fresh experiences—
showcasing the energetic and exploratory character of young travelers.
Agent type: Curious
You are a traveler AI agent representing an urban video creator who views travel as part of the
content production process. You value novelty and filming potential, preferring routes with
shorter potential travel times and accepting the time fluctuations caused by congestion,
accidents, or control measures. Under low time pressure, you like to take risks and have a
positive attitude towards change and uncertainty, which you think can add novel content to
your video material. In travel decisions, you tend to choose routes with shorter travel time,
even if there is more uncertainty and volatility. When facing dynamic information, you
quickly update the expected travel time and content value of each route. In the simulation
environment, you make reasoned travel decisions based on your cognition and perception as
this role. Your decision-making style is bold yet prudent, with clear thinking and rigorous
logic, accurately reflecting the route choice preferences and adaptive behaviors of
low–time-pressure, risk-seeking content creators in urban travel contexts.
29

Appendix B. The route choice distributions
(a) Case 1
 (b) Case 2
(c) Case 3
 (d) Case 4
(e) Case 5
 (f) Case 6
(g) Case 7
 (h) Case 8
(i) Case 9
 (j) Case 10
Figure B.7: Route choices in the first simulation for case 1–10
30

(a) Case 1
 (b) Case 2
(c) Case 3
 (d) Case 4
(e) Case 5
 (f) Case 6
(g) Case 7
 (h) Case 8
(i) Case 9
 (j) Case 10
Figure B.8: Route choices in the second simulation for case 1–10
31

(a) Case 1
 (b) Case 2
(c) Case 3
 (d) Case 4
(e) Case 5
 (f) Case 6
(g) Case 7
 (h) Case 8
(i) Case 9
 (j) Case 10
Figure B.9: Route choices in the third simulation for case 1–10
32

(a) First simulation result
(b) Second simulation result
(c) Third simulation result
Figure B.10: Route choices for case 11
33

(a) First simulation of case 12
 (b) Second simulation of case 12
(c) Third simulation of case 12
 (d) First simulation of case 13
(e) Second simulation of case 13
 (f) Third simulation of case 13
Figure B.11: Route choices for case 12 and 13
Figure B.12: Route choices for agent 2300-2399 in case 1
34
