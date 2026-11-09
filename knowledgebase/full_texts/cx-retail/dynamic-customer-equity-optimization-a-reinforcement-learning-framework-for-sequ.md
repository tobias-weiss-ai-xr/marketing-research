---
title: 'Dynamic Customer Equity Optimization: A Reinforcement Learning Framework for Sequential Marketing
  Decision-Making in Volatile Markets'
url: https://doi.org/10.63468/ijbms.7.5.25
category: cx-retail
subcategory: empirical
date: 2026-07
venue: International Journal of Business and Management Sciences
authors:
- Perkha Khan
- Muhammad Junaid
- Muhammad Maroof Ajmal
source: openalex-oa
pdf_url: https://ijbmsjournal.com/index.php/jbmis/article/download/1050/519
pages: 20
chars: 70735
fetched_at: '2026-11-08T19:04:52+00:00'
kb_version: 1
---

# Dynamic Customer Equity Optimization: A Reinforcement Learning Framework for Sequential Marketing Decision-Making in Volatile Markets

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 351
INTERNATIONAL JOURNAL OF BUSINESS AND MANAGEMENT SCIENCES
E-ISSN 2708-4337  |  P-ISSN 2708-4329  |  Volume 07 (05), 2026  |  www.ijbmsjournal.com
  RESEARCH ARTICLE
Dynamic Customer Equity Optimization: A Reinforcement Learning Framework
for Sequential Marketing Decision-Making in Volatile Markets
Perkha Khan 1,*, Dr. Muhammad Junaid 2, Dr. Muhammad Maroof Ajmal 3, Dr. Muhammad Usman Malik 4
Dr. Noheed Khan 5
1 Lecturer, Quaid-i-Azam School of Management Sciences, Quaid-i-Azam University, Islamabad
  perkha.khan@qau.edu.pk
2 Assistant Professor, Quaid-i-Azam School of Management Sciences, Quaid-i-Azam University, Islamabad
  junaid@qau.edu.pk
3 Assistant Professor, University Institute of Management Sciences, PMAS Arid Agriculture University, Rawalpindi
  dr.maroof@uaar.edu.pk
4 Department of Law, Economics, Management and Quantitative Methods (DEMM), University of Sannio, Italy
  usmanmalik836@gmail.com
5 Associate Professor, Department of Management Sciences, Alhamd Islamic University, Islamabad
  dr.noheed@aiu.edu.pk

Article Type Research Article
Article History Received: 01 Jul 2026   ·   Revised: 10 Jul 2026   ·   Accepted: 20 Jul 2026   ·   Published: 31 Jul 2026
DOI https://doi.org/10.63468/ijbms.7.5.25
Corresponding Author Perkha Khan —  perkha.khan@qau.edu.pk
Keywords Customer Equity, Reinforcement Learning, Customer Lifetime Value, Sequential Decision-Making,
Dynamic Marketing, Market Volatility, Value Co-Creation, Offline Policy Learning

A B S T R A C T
In a world of unparalleled market volatility and fragmented customer journeys, the old customer equity
management models based on fixed segmentation and post -hoc analytics have not been sufficient to capture the
dynamic development of customer -firm relationships. This paper presents an elaborate reinforcement learning
(RL) model of dynamic customer equity optimization, which views marketing decisions as adaptive interventions
that are sequential in non -stationary environment. To construct a practically impl ementable and theoretically
based architecture of real -time marketing decision -making, we combine recent developments in the deep
reinforcement learning, causal inference, and customer lifetime value (CLV) modeling. The framework combines:
(1) multi-response state models that maintain Markov properties whilst learn online customer value signals; (2)
conservative Q-learning to ensure reliable policy learning on offline data; (3) factor sensitive reward designs that
include time varying customer engagement dy namics; and (4) multi -objective optimization that balances
acquisition, retention and profitability goals. Empirical results on a variety of industry applications show that RL -
based methods obtain significant improvements over constant baselines, and reported improvements in targeting
efficiency of 27% (Qini coefficient), ROI gains of 18-58 and CLV impact gains of 45-85 (Wang and Chen, 2025). We
cover theoretical background, issues in implementation and research directions in the future by arguing that
dynamic customer equity optimization is a paradigm shift; instead of reactive, campaign-based marketing, dynamic
customer equity optimization is proactive, relationship-oriented value co-creation. The paper ends by highlighting
research gaps that are crucial to fill and outlining an agenda to further develop the  combination of reinforcement
learning and customer equity theory.

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 352
INTRODUCTION
The Challenge of Customer Equity Management in Volatile Markets
The term customer equity, which refers to the total lifetime value of current and potential customers of a given
firm has become one of the cornerstone strategic frameworks in marketing (Rust, Zeithaml, and Lemon, 2000;
Rust, Lemon, and Zeithaml, 2004). Rust, Lemon, and Zeithaml (2004) defined customer equity as the metric that
unites the firm to trade off options competing in marketing strategies based on estimated financial payback. This
model, which has been operationalized to mean the change in customer  equity in relation to incremental
expenditure, has had a significant impact on how marketing leaders frame resource allocation, customer
relationship management and creation of long term value (Berger et al., 2006; Kumar et al., 2010).
Nevertheless, the initial customer equity approach, despite its revolutionary nature, was created in a period when
the market was relatively stable, customer journeys were linear, and there was a lack of real-time data (Ascarza,
Zhang, and Netzer, 2025). The modern markets are completely different. The growth of digital touchpoints, the
division of customer attention between channels, and the speed of preference changes, the growing number of
exogenous shocks, such as pandemics or political instability, have led to a state of continuous volatility that is
disrupting the premises of the conventional customer-equity framework (Libai et al., 2020; Ngai and Wu, 2022).
This volatility comes in a number of ways which makes customer equity optimization difficult. To begin with, there
is non-stationarity in customer preferences and behavior: the trend between marketing behavior and customer
reaction varies with time, making a static response model outdated (Netzer, Lattin, and Srinivasan, 2008; Zhang,
Netzer, and Ansari, 2015). Second, customer expectations are quickly shifting with new entrants and disruptive
business models rapidly redefining competitive dynamics (McManus, 2013; Karvanen , Rantanen, and Luoma,
2014). Third, the abundance of fine -grained behavioral data presents opportunities and challenges: on the one
hand, companies have never had such access to customer behavior, and on the other hand, the sheer volume and
speed of data overwhelm traditional methods of analysis (Ram and Zhang, 2022; Line, Hanks and McGinley, 2020).
Limitation of Traditional Approaches
The customary customer equity optimization approaches can be grouped into three general groups, which have
different restrictions. The former group is those that are statistically optimized to assign the marketing resources
by estimating the customer lifet ime value and response elasticity (Berger and Bechwati, 2001; Venkatesan and
Kumar, 2004). Although analytically rigorous, these models make the assumption  that the underlying
relationships between marketing activities and customer reactions do not vary over time. This is often not the
case in volatile markets, which can result in suboptimal or even counterproductive allocation of resources
(Ovchinnikov, Boulu-Reshef, and Pfeifer, 2014).
The second category includes predictive CLV models, which predict the future value of customers, but do not
consider maximizing marketing actions (Fader, Hardie, and Lee, 2005; Reinartz and Kumar, 2000, 2003). Other
approaches, like the NBD/Pareto framewor k of non -contractual settings (Schmittlein, Morrison, and Colombo,
1987), and other types of machine learning-based CLV prediction (Kanchanapoom and Chongwatpol, 2023; Singh
et al., 2024) offer informative information about customer valuation but do not recommend the best sequential
interventions. They make marketing decisions exogenous to the prediction process without considering the
recursive nature of marketi ng behaviors and customer value development (Ascarza et al., 2018; Salisbury,
Nenkov, and Blanchard, 2023).
The third category includes rule-based and heuristic methods that convert customer segmentation into marketing
activities. They are operationally simple yet lack flexibility: they do not adapt to evolving customer dynamics, do
not leverage the richness of behavioral data, and often have systematic biases, including overspending on high -
value customers and underspending on those with high incremental potential (Ovchinnikov et al., 2014; Mandania
et al., 2026).

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 353
The Promise of Reinforcement Learning
Another strong alternative paradigm that can be used to optimize customer equity involves reinforcement
learning. In contrast to the classical models of approaching marketing as a one-time decision-making process that
involves making allocations in isolation, RL views marketing as a sequence of decision -making processes where
the business repeatedly learns about customer feedbacks and adjusts its policies to them (Sutton and Barto, 1998;
Mandania et al., 2026). Such framing is inherently consistent with the dynamism of customer-firm relationships,
where the state of the relationship at a given moment in time determines future states and opportunities (Ascarza
et al., 2025; Wang and Chen, 2025).
The theoretical attractiveness of RL to marketing applications is based on a few important properties. First, RL
algorithms are specifically formulated in terms of making decisions in a sequence under uncertainty, learning
policies that trade between short -term rewards (e.g., short -term revenue) and long -term effects (e.g., customer
retention and lifetime value) (Sutton and Barto, 1998; Kumar et al., 2025). Second, RL is capable of handling non-
stationarity associated with volatile markets due to ongoing learning and adapting of policies (Mandania et al.,
2026; Jung and Oh, 2025). Third, RL models can use complex and high-dimensional state representations, such as
transaction histories, enga gement metrics, and contextual variables, to reflect the complexity of customer
behavior (Ascarza et al., 2025; Zhang et al., 2015). Fourth, recent developments in offline RL make it possible to
learn policies using historical data, a practical limitation of online experimenting that may not be possible or too
expensive (Kumar et al., 2020; Levine et al., 2020).
Research Objectives and Contribution
The objective of this paper is to further the theoretical and practical underpinnings of dynamic customer equity
optimization using reinforcement learning. In particular, we discuss the following research questions:
RQ1: What are ways to design RL structures to maximize customer equity in volatile non -stationary market
conditions?
RQ2: Which state representations, reward, and learning algorithms work best in sequential marketing decision-
making?
RQ3: What are the solutions to the issues of offline policy learning, such as sparsity of data, distributional shift
and partial observability, in marketing?
RQ4: How is the empirical evidence of the superiority of RL -based methods to traditional methods, and in what
circumstances do the benefits arise?
We make three times the contribution. To begin with, we build an elaborate theoretical framework that combines
the learning of customer equity theory, reinforcement learning, causal inference and dynamic optimization. This
framework offers a systematic basis of the academic study and real practice. Second, we compile empirical results
of the recent implementations, showing the effectiveness of RL-based methods in various industry contexts. Third,
we determine research gaps that are crucial, and we suggest a forward -looking research agenda that will cover
the most urgent issues in the optimization of dynamic customer equity.
LITERATURE REVIEW
Customer Equity: Foundations and Evolutions
The concept of customer equity was developed out of the acknowledgment that customers are the most valuable
part of a firm and that marketing should be measured on its effect on the value of this asset as opposed to
intermediate measures that include awareness or satisfaction (Rust et al., 2000, 2004). Rust, Lemon and Zeithaml
(2004) presented an integrated strategic framework whereby competing marketing strategy alternatives are
considered in terms of estimated financial payoff, operationalized as the chan ge in customer equity versus
incremental spending.

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 354
The most important element of this framework is an idea of customer lifetime value which is the present value of
future cash flows that can be ascribed to a customer (Rust et al., 2000). The lifetime value of each customer is
based on the frequency of category purchases, quantity of purchases, brand switching behaviour, and contribution
margin of the firm (Rust et al., 2004). Longitudinal or cross -sectional data, estimated using logit choice models,
can be used to capture competitive dynamics and facilitate the projection of customer equity change in response
to marketing investments as a brand-switching matrix (Rust et al., 2004; Karvanen et al., 2014).
Rust, Zeithaml and Lemon (2000) extended the framework of customer equity by establishing three drivers
namely; Value Equity (customer perceptions of value), Brand Equity (customer perceptions of brand quality and
associations) and Retention Equity (the re lationship between the firm and its customers). These drivers offer
managers practical levers of customer equity improvement, and the model allows identifying the most important
drivers in a particular industry environment (Rust et al., 2000; Kim, Boo, and Qu, 2018).
The customer equity concept has subsequently been expanded and narrowed down in other directions through
subsequent research. Petersen et al. (2009) recommended the correlation of unobserved variables like share of
wallet with forward-looking measures like CLV in resource allocation problem. The value of customer equity in
the context of Omni channel (Berman and Thelen, 2024), the contribution of big data to customer valuation (Ram
and Zhang, 2022; Line et al., 2020), and how customer equity can be integrat ed with other financial indicators
have also been studied (Berger et al., 2006; Kumar et al., 2010). Terblanche (2015) studied the correlation
between loyalty programs and customer equity, whereas Talon -Ballestero, Nieto-Garcia and Gonzalez -Serrano
(2022) research the relationship between pricing strategies and customer equity. Stakhovych and Tamaddoni
(2020) studied the recovery perspective of the relationship quality and customer equity, and Manosuthi, Lee, and
Han (2021) investigated the customer engagement and CLV in the sharing economy.
Regardless of these developments, the original customer equity model is essentially unchanged. The interactions
between market activities and customer reactions are normally approximated based on past data and presumed
to be true throughout the planning pe riod (Ascarza  et al., 2025). Although it allows the assumption to be
analytically tractable, it is becoming unsustainable in unstable market conditions. According to Mandania et al.
(2026, p. 3), traditional models of analysis are usually in a state of stagnation, they  do not evolve with current
behavioral trends, and cannot update the decision at real time.
Customer Lifetime Value: Measurement and Application
Customer lifetime value has become a key construct in academic marketing and management (Fader et al., 2005;
Reinartz and Kumar, 2000, 2003; Kumar et al., 2010). Although a detailed overview of the CLV measurement
practices is not within the context of this paper, there are a few important techniques applicable to our framework.
The conventional method of CLV modelling is based on probabilistic customer behavior models. Originally
formulated by Schmittlein, Morrison, and Colombo (1987), the NBD/Pareto framework is a model of customer
transaction processes and dropouts in non-discipline contracts. This method has been expanded and elaborated
in many forms, such as those that include covariates (Ascarza  & Hardie, 2013), support more than two types of
transactions (Fader et al., 2005), and allow prediction into the future (Reinartz & Kumar, 2003).
In recent years, machine learning -based methods of predicting CLV have spread as behavioral data in digital
settings grows, making use of the richness of such behavioral data. These methods involve survival models (Singh
et al., 2024), gradient boosting machines (Kanchanapoom and Chongwatpol, 2023), and deep learning models that
employ the complicated nonlinear associations between customer features and future value (Meire et al., 2019;
Ngai and Wu, 2022). Recent studies have also addressed representation learning usage to generate state
embeddings that maintain predictive information of long -term customer value whilst supporting high -
dimensional raw data (Ascarza et al., 2025; Wang and Chen, 2025).
Nonetheless, the main issue with CLV modeling, as Ascarza et al. (2018) report, is that customer spending data is
very sparse, with most customers and time points having a spend of zero. This sparsity may blur significant trends:

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 355
zero expenditure may be disengagement, mere non -purchasing behavior, or the impact of marketing efforts. A
successful CLV model should be able to discriminate between the two situations, and to do that, it should include
an engagement signal and retention proxies in addition to monetary performance (Ascarza et al., 2018; Zhang et
al., 2015).
Reinartz and Kumar (2000, 2003) established that the most important factor to make resource allocation
decisions is the profitability and not the tenure . The fact that long -tenured customers are not always the most
profitable customers was a challenge to conventional wisdom, and the value of dynamic, forward -looking
customer valuation. This observation can be compared to the RL framework, which distribute s resources
according to the anticipated future value and not on the past loyalty (Mandania et al., 2026; Wang and Chen, 2025).
Reinforcement Learning: Foundations and Marketing Applications
Reinforcement learning has become a potent paradigm in sequential decision-making in uncertain situations. The
main RL model consists of the interaction between an agent and an environment in discrete time, where the agent
perceives the states, acts, and receives rewards (Sutton and Barto, 1998). The goal of the agent is to discover an
action-state policy- mapping that maximizes long term cumulative reward.
The use of RL in marketing issues has gained much momentum within the past few years. Mandania et al. (2026)
created an RL -based promotion optimization model, which keeps on updating promotional strategies through
real-time responding customer transactions. Their solution deals with two important issues: (1) lack of complete
information about customers (e.g. unobserved share of wallet) and (2) the fact that customers should be treated
as co-creators, but not as receivers of value. Through simulations involving a ferry travel agency, they show that
the RL can be used to dynamically adapt promotional strategies to achieve maximum CLV and help in co-creation
of values.
The aspect of treating the customers as value co -creators is a major theoretical development. Conventional CLV
and customer equity methods assume that customers are passive consumers of marketing programs and that the
value is created by the firm (Rust et al., 2000, 2004). The RL framework, on the other hand, acknowledges that the
reaction of customers to marketing activities are  a good source of information that must be used in future
decision-making (Mandania et al., 2026). This vision coincides with the idea of value co -creation presented by
Prahalad and Ramaswamy (2004), whereby value is created when firms engage with customers.
Multi-objective RL has been studied in recent work as well in the context of integrated marketing strategy. Kumar
et al. (2025) created a framework which is a combination of Heterogeneous Graph Neural Networks, Contrastive
Predictive Coding, Generative Adversarial Uplift Modeling, and multi-agent reinforcement learning. This method
proved to be much more effective in various goals: CLV prediction accuracy improved by 92.1, uplift targeting
efficiency by 24.7, and churn reduction by 19.2. This multi-objective view is critical to the marketing use, wherein
the trade -offs between acquisition, retention, and profitability have to be balanced (Wang and Chen, 2025;
Torkzadeh and Dhillon, 2025).
Sequential Decision-Making in Marketing
The sequentially of customer -firm relationships is a phenomenon in marketing research that has been known
decades. The changes in customer relationships occur over time under a sequence of interactions, in which each
interaction shapes the future states an d opportunities (Zhang et al., 2015; Netzer et al., 2008). Such a time
framework suggests that the best marketing choices must not only focus on short -term effects but also on
outcomes in terms of future relationship paths (Ascarza et al., 2025; Salisbury et al., 2023).
There are some research streams that have dealt with sequential decision -making in marketing. Optimizing
customer relationship management, balancing between acquisition and retention investments across time, is
optimized through dynamic programming approaches (Ovchinnikov et al., 2014; Von Mutius and Huchzermeier,
2021). Reinforcement learning builds on these models by allowing the learning of data instead of having to
explicitly specify transition dynamics and reward functions (Sutton and Barto, 1998; Mandania et al., 2026).

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 356
The recent efforts have been concerned with the problem of conserving the Markov properties of customer state
representations. Multi-task representation learning, where the learned state representation is conditioned by the
various prediction targets, is u sed to solve this problem by Ascarza  et al. (2025): (1) response prediction
(predicting the reaction of the customer to the state), (2) action prediction (prediction of the action that caused
state transitions), and (3) sequence order prediction (prediction of the difference between sequenti al and non-
sequential pairs of states). This methodology will guarantee that the representation learned can have predictive
cues on long-term values without compromising the Markov property that is necessary to achieve successful RL.
Dynamic treatment effects have also been found to be important. The classical uplift model presupposes the use
of fixed treatment effects that do not change over time and situations (Gutierrez & Gérardy, 2017). Dynamic uplift
models research expands on thi s methodology by letting treatment effects change over time as the customers
build their relationships (Wang and Chen, 2025; Kumar et al., 2025). This time -based approach is paramount to
the field of marketing since the success of any intervention in many cases can rely on the stage of relations with
the customer and recent history (Ascarza et al., 2018; Zhang et al., 2015).
Gaps and Opportunities
Although much has been done, there are still a number of  gaps in the part of integrating reinforcement learning
and customer equity optimization. First, there is limited development of the treatment of market volatility and
non-stationarity. Although it is theoretically possible to make it so that RL algorithms  can adapt to changing
environments, the practical implementation of adaptive policies in volatile markets is challenging due to the
exploration-exploitation trade-offs, forgetting, and policy stability (Jung and Oh, 2025; Kirtac, 2025).
Second, the reward structure design to achieve customer equity optimization needs further theoretical
elaboration. Although the cumulative revenue/profit is the natural goal, the milestone rewards that drive learning
might have to include engagement, reten tion, and other indicators that portend long -term value (Ascarza et al.,
2025; Wang and Chen, 2025). Questions of what the best mix of short-term and long-term rewards should be, and
the discounting of future payoffs, are still open (Sutton and Barto, 1998; Mandania et al., 2026).
Third, the offline policy learning problem, which is to find the best policies, based on history, without conducting
online trials, is especially severe in marketing. Although offline RL algorithms such as the conservative Q-learning
are promising (Kumar et al., 2020; Levine et al., 2020), the specifics of the marketing data (sparsity, selection bias,
partial observability) pose unique issues, which need to be explored further (Ascarza et al., 2018; Wang and Chen,
2025).
Fourth, the combination of causal inference and RL is a current research topic. The uplift modeling is a kind of
foundation of knowing the heterogeneous treatment effects (Gutierrez and Gérardy, 2017; Devriendt et al., 2020),
although the conversion of suc h knowledge into sequential policies to consider the dynamic treatment effects
remains in its infancy (Wang and Chen, 2025; Kumar et al., 2025).
Theoretical Framework for Dynamic Customer Equity Optimization
Problem Formulation
We formalize model dynamic customer equity maximization as a Markov Decision Process (MDP) characterized
by the following (S, A, P, R, γ) where:
• S The state space, which is the information available to the firm about every customer at time t.
• A is the action space, which is the combination of marketing interventions that can be undertaken.
• P(s'|s,a) The transition probability, which describes the change of customer states with actions.
• R(s,a) is the reward function, which is the immediate contribution of customer equity.
• γ ∈ [0,1] is a discount factor which is in [0,1] balancing between immediate and future rewards.

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 357
The task is to learn a policy π(a|s) which maximizes the cumulative discounted reward expected:

This equation describes the sequentially of customer-firm relationships: any marketing activity affects the future
state of the customer (e.g., their engagement, purchase behavior, retention probability), which in turn determines
the value of future opportunities (Ascarza et al., 2025; Zhang et al., 2015; Netzer et al., 2008).
Customer State Representation
State representation is essential to successful RL since it dictates the information the agent employs to decide
(Sutton and Barto, 1998; Allen, Bouchard and Balduzzi, 2021). The raw data at the disposal of the firm in
marketing contexts is often noisy and  high-dimensional, such as transaction history, browsing behavior,
demographic, and contextual variables (Ngai and Wu, 2022; Ram and Zhang, 2022). Representing a state
effectively has to be able to draw out the relevant signals and reject the irrelevant variation.
In the style of the method proposed by Ascarza et al. (2025) we suggest a multi -response state representation
which assumes three kinds of prediction targets:
Response Prediction
The state representation must be able to predict short-term customer reactions such as monetary (e.g., quantity
of purchase, probability of transaction) and engagement signals (e.g., recency, frequency, intensity of interaction).
The answers help to give f eedback on the marketing activities in real -time and record the current relationship
state of the customer (Ascarza et al., 2018; Bijmolt et al., 2010).
Action Prediction
The representation must allow forecasting the action that resulted in transitions between states of customers.
This condition guarantees that transition dynamics in the learnt representation space are consistent with original
customer characteristics dynam ics under the behavioral policy (Ascarza et al., 2025). The dynamics of the
representation space are identical to those of the original space when two consecutive learned representations
are able to predict the action taken between observed characteristics with high accuracy, as shown by Ascarza et
al. (2025).
Sequence Order Prediction
This representation must be able to differentiate between sequential and non-sequential pairs of customer states.
This condition maintains the density ratio, which is to make sure that the relative probability of observing
transitions in the original data is maintained in the learned space of representations (Ascarza et al., 2025; Allen et
al., 2021).
The multi-response state representation can address two important issues in the customer RL application: (1) the
sparsity of the transaction data, where zero spending may represent varying amounts of different states, which
demand different responses (Ascarza et al., 2018; Zhang et al., 2015); and (2) the necessity to capture long -term
value signals that are not directly related to immediate monetary consequences (Kumar et al., 2010; Mandania et
al., 2026).
Formally, the state representation map Φ is learned by jointly minimizing three loss functions:

and where f is the prediction of the customer responses, g is the prediction of actions, h is the prediction of the
sequence order, and are the weights of the relative importance of the Markov preservation tasks (Ascarza et al.,
2025; Allen et al., 2021).

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 358
Reward Design for Customer Equity
The reward mechanism in the customer equity optimization must be aligned to the long-term goal of the customer
value maximization (Sutton and Barto, 1998; Mandania et al., 2026). Nevertheless, there are a number of
challenges in how to design effective reward functions of RL.
Immediate vs. Delayed Rewards
Customer equity is a delayed construct in nature (Rust et al., 2000, 2004). Delays in the occurrence of rewards
should be discounted in the distant future but the discounting factor 7 should correspondingly balance the delayed
value desire with the practical challenge in learning in the face of delayed signals (Sutton and Barto, 1998). The
decision of γ is important to policy behavior: small value of the discount factor results in short -term oriented
policies that maximize short -term revenue, whereas large value of the discount factor results in long -term
relationship building policies, but possibly slow learning (Mandania et al., 2026; Wang and Chen, 2025).
Multiple Objective Integration
Customer equity is a multiple dimension concept, including acquisition, retention, profitability, that can be
conflicting (Rust et al., 2004; Berger et al., 2006). Pareto optimization can resolve these trade -offs by a multi -
objective RL method as shown by Kumar et al. (2025) and Torkzadeh and Dhillon (2025). The reward mechanism
may be designed as a weighted or combination of goals, with the weights indicating strategic priorities:

Where Oi -individual objectives and 1 -summation of ∑wi = 1 (Kumar et al., 2025; Torkzadeh and Dhillon, 2025).
Factor-Sensitive Rewards
We propose that factor -sensitive rewards should be added based on the recent studies in factor -based RL to
allocate assets (Jung and Oh, 2025), with the rationale being that customers need to be exposed to the important
relationship drivers. These factors include:
• Engagement Momentum:  This is the curve of customer engagement, i.e. whether the customer is
becoming more or less engaged (Bijmolt et al., 2010; Meire et al., 2019).
• Retention Risk: The risk of losing a customer, to be punished to promote retention -driven behavior
(Ascarza et al., 2018; Zhang et al., 2015)
• Value Velocity: This is the rate at which customer value is generated, which is a measure of how the
customer is moving through the value curve (Kumar et al., 2010; Salisbury et al., 2023).
• Loyalty Elasticity: How customer behavior is responsive to loyalty -building interventions (Terblanche,
2015; Yoo, Bai, and Singh, 2020)
The factor-sensitive reward structure can be modeled as:

Where the weights are the strategic priorities of the firm and the factors are estimated using the customer data
(Jung and Oh, 2025; Wang and Chen, 2025).
Learning Algorithms for Marketing Application
The choice of learning algorithm depends on the characteristics of the marketing environment and the available
data (Sutton & Barto, 1998; Levine et al., 2020). Three main algorithmic methods, which we take into
consideration, are:

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 359
Deep Q-Network (DQN) and Extensions
DQN can be used in scenarios with discrete action spaces (e.g., selecting between promotional offers, channel
assignments, treatment options) (Mnih  et al., 2015; Van Hasselt, Guez, and Silver, 2016). Such extensions as
Double DQN (minimizing overestimation bias), Prioritized Experience Replay (emphasizing on informative
transitions), and Dueling Network Architecture (estimating state values and actio n advantages separately) have
been found to substantially enhance performance in marketing settings (Wang and Chen, 2025; Kumar et al.,
2025). The loss of DQN is:

Where D the replay buffer, and θ− desired network parameters (Mnih et al., 2015).
Conservative Q-Learning (CQL)
CQL is an effective method of learning observational data without online experimentation, which penalizes the
actions whose actions have an overestimated Q -function as a result of  distributional shift (Kumar et al., 2020).
This is especially useful in marketing applications, where the data -generating procedure encapsulates historical
policies that might not have exhaustively investigated all potential actions (Wang and Chen, 2025; Levine et al.,
2020). The CQL goal includes a negative penalty:

In which π^β is the behavioral policy (Kumar et al., 2020).
Proximal Policy Optimization (PPO)
PPO provides a stable and efficient sample-wise policy gradient method when the action space is continuous (e.g.,
budget allocation, discount levels) or the action space is large enough to be treated as continuous (Schulman et
al., 2017). The clipped objec tive of PPO is what makes the policy updates not too huge, and keeps the policy
consistent even in the absence of non-stationary customer behavior:

Addressing Market Volatility
Volatility and non-stationarity are inherent issues with RL in marketing (Jung and Oh, 2025; Kirtac, 2025). To keep
policy effective in volatile settings several strategies can be used:
Adaptive Reward Calibration
Rewards are to be tuned in terms of prevailing conditions in the market. A context -specific reward system
suggested by Jung and Oh (2025) modulates elements of rewards according to time -varying variables. It makes
sure that the policies can adjust to chang ing circumstances instead of optimizing to historical trends that might
no longer apply (Wang and Chen, 2025).
Dynamic State Representation
The state representation needs to have time -dependent features that indicate a regime change (Jung and Oh,
2025). By including volatility measures, market sentiment, and competitive dynamics in the state representation,
the agent can condition its policy on the prevailing market situation (Kirtac, 2025; Ascarza et al., 2025).

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 360
Sentiment-Augmented Learning
The most recent findings in the field of portfolio optimization have shown the importance of the addition of
sentiment signals based on unstructured data ( Kirtac, 2025). Sentiment indicators of social media, customer
feedback, and survey results can be utilized to give early warnings of preferences and respond adaptively to policy
changes, which can be applied to marketing purposes (Meire et al., 2019; Ngai and Wu, 2022).
Ensemble Approaches
The idea of combining several RL agents with various exploration strategies or time horizons can be used to
improve resilience to volatility, as the agents could perform well in distinct market conditions (Kumar et al., 2025;
Wang and Chen, 2025). The ensemble policy can be defined as:

where πk are individual agent policies (Kumar et al., 2025).
Empirical Evidence and Application
Overview of Empirical Studies
The recent empirical research has presented some evidence of effectiveness of RL -based methods in marketing
applications. We generalize the results of important research to evaluate the size and stability of performance
gains.
Performance Comparison Analysis
In one of the studies that tested dynamic causal RL methods (Wang and Chen, 2025), several methods were
compared on the RetailCo CRM Dataset, using performance metrics based on targeting efficiency (Qini coefficient),
and lift at various thresholds, ROI, and CLV impact. The findings show significant differences with business rule
baselines and traditional uplift modeling methods.
Table 1: Comprehensive Performance Comparison Across Methods
Method Qini Coefficient Lift@10% Lift@20% Lift@30% ROI CLV Impact Incremental Gain
Random
Assignment 0.00 1.00 1.00 1.00 0.28 0.005 -
Business Rule 0.31 1.58 1.42 1.31 0.62 2.45 Baseline
2Response
Model 0.29 1.52 1.38 1.28 0.58 2.18 -6.4%
Traditional
Uplift Model 0.38 1.89 1.67 1.52 0.75 3.21 +22.6%
Static Causal
Forest 0.41 2.05 1.75 1.61 0.81 3.59 +32.3%
Dynamic Uplift
Model 0.44 2.12 1.85 1.66 0.86 3.82 +41.9%
Contextual
Bandits 0.46 2.19 1.89 1.69 0.89 3.95 +48.4%
Dynamic
Causal RL 0.52 2.42 2.05 1.82 0.98 4.53 84.9%

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 361
The Dynamic Causal RL model has a Qini coefficient of 0.52, which is 27 points higher than the baseline of business
rule (0.31) and 19 points higher than the traditional uplift models (0.38). The lift measures are stable in all
thresholds, with Lift 10% being 2.42 against 1.58 with the busines s rule and 1.89 with the traditional uplift. ROI
is 0.98, as compared to 0.62 of the business rule baseline  and 0.75 of traditional uplift -improvements of 58 and
31, respectively. CLV impact of 4.53 is 85 percent and 41 percent greater than the business rule baseline of 2.45
and traditional uplift of 3.21.
Table 2: Ablation Study Results: Component Contribution Analysis
Variant Qini Coefficient ROI Performance Drop Key Insight
Full Framework (Dynamic Causal RL) 0.52 0.98 - Complete Framework
Without Causal Forest 0.43 0.84 -17.3% Causal Estimation Crucial
Without Dynamic Effects 0.46 0.88 -11.5% Temporal Dynamics Matter
Without Adaptive Reward 0.49 0.92 -5.8%
Adaptive Rewards
Provide Moderate
Gains
Without Reinforcement Learning 0.44 0.85 -15.4%
RL Sequential
Optimization
Essential
Without State Representation Learning 0.40 0.80 -23.1% State Representation Most Critical
Ablation study shows that the performance decreases by 17.3% when the causal forest component is removed,
which proves the significance of the correct estimation of heterogeneous treatment effects (Gutierrez and
Gérardy, 2017; Devriendt et al., 2020). The elimination of the RL element decreases performance by 15.4, which
is indicative of the importance of sequential optimization (Sutton and Barto, 1998; Mandania  et al., 2026).
Elimination of the dynamic effects decreases performance by 11.5 percent, which proves that the temporal
dynamics of customer response should be captured (Zhang et al., 2015; Netzer et al., 2008). The most important
learning is the state re presentation learning with a 23.1% drop highlighting the significance of maintaining
Markov properties.
Table 3: DQN Extension Performance Analysis
DQN Variant Qini Coefficient ROI Training Stability Convergence Speed
Vanilla DQN 0.44 0.87 Moderate Moderate
Double DQN 0.47 0.91 High Moderate
Prioritized Experience Replay 0.50 0.95 High Fast
Dueling Network Architecture  0.48 0.93 High Moderate
All Extensions Combined 0.52 0.98 Very High Fast
Further studies on DQN extensions indicate that all three, Double DQN (Van Hasselt et al., 2016), Prioritized
Experience Replay (Schaul et al., 2016), and Dueling Network Architecture (Wang et al., 2016), have a beneficial
impact on performance. The most important individual contribution is Prioritized Experience Replay (Qini: 0.50,
ROI: 0.95), which is probably due to the generally imbalanced conversion events in marketing datasets, and
prioritization of experience with larger temporal -difference errors would allow the agent to learn better about

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 362
rare but informative conversion events (Wang and Chen, 2025; Schaul et al., 2016). The combined approach
achieves the highest performance with very high training stability and fast convergence.
Findings from Promotion Optimization Studies
Mandania et al. (2026) built a promotion optimization model based on RL, which constantly changes the
promotional strategies according to real-time responses in terms of customer transactions. Their simulated study
in a context of a ferry travelling agency gives some valuable insights.
Table 4: Promotion Optimization Performance Metrics
Performance Metric Static Approach RL Approach Improvement
Average CLV ($) 1245 1892 +52.0%
Customer Retention Rate (%) 62.3% 78.1% +25.4%
Promotion Efficiency (ROI) 1.45 2.18 +50.3%
Customer Acquisition Cost ($)  185 142 -23.2%
Share of Wallet (%) 34.2% 41.7% +21.9%
Customer Satisfaction Score 4.12 4.38 +6.3%
The RL-based methodology shows important gains in all measures. Average CLV increases from $1,245 to $1,892
(+52.0%), customer retention improves from 62.3% to 78.1% (+25.4%), and promotion ROI increases from 1.45
to 2.18 (+50.3%). Customer acquisition cost decreases from $185 to $142 ( -23.2%), while share of wallet
increases from 34.2% to 41.7% (+21.9%). These advantages underscore the dynamic lea rning potential of RL,
which is specifically useful in volatile markets, where customer preferences change quickly (Jung and Oh, 2025;
Kirtac, 2025).
To begin with, RL strategy exhibits the capacity to adjust the promotional strategies to changing customer
preferences. In contrast to the other methods that are in place, which are based on assumptions that might be
invalid with the passage of time, the RL algorithm is an algorithm that learns about the current trends in behavior
and, based on them, updates decisions (Mandania  et al., 2026). Second, it is important to focus on mid -tier
customers as noted in the study. The conventional method tends to concentrate marketing resources on the high-
value customers, whereas the RL model finds out that customers at the middle of the v alue distribution can be
more profitable to target (Mandania et al., 2026). This observation is echoed by the fact that Ovchinnikov, Boulu-
Reshef, and Pfeifer (2014) reported that companies are more likely to spend much on high -value customers and
less on low-value customers.
Third, the research shows the importance of considering customers as co-creators of value (Mandania et al., 2026).
The RL approach facilitates a collaborative process where customer responses are used to influence future
promotional strategies by introducing real-time customer feedback into the learning process.
Multi-Objective Optimization
The use of a multi -objective machine learning optimization framework that integrates RL with other advanced
methods (Kumar et al., 2025) showed substantial advancements in various marketing goals.
Table 5: Multi-Objective Optimization Performance
Objective Baseline Performance Optimized Performance Improvement
CLV Prediction Accuracy (R2) 0.62 0.89 +92.1%
Uplift Targeting Efficiency (Qini) 0.38 0.47 +24.7%

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 363
Churn Reduction (%) 12.5% 14.9% +19.2%
Cross-Domain Adaptability (%) 68.3% 78.5% +10.2%
Campaign ROI  1.82 2.45 +34.6%
Customer Engagement Score 3.56 4.21 +18.3%
The framework includes Heterogeneous Graph Neural Networks to represent customers (Kipf and Welling, 2017),
Contrastive Predictive Coding to mine latent intents (Oord, Li and Vinyals , 2018), Generative Adversarial Uplift
Modeling to predict CLV (Goodfellow et al., 2014), and multi-agent RL to make coordinated decisions (Lowe et al.,
2017). Findings indicate that CLV prediction accuracy, uplift targeting, and churn were 92.1, 24.7, and 19.2 higher,
respectively. The adversarial transfer learning also enhanced the cross-domain adaptability by an average of 10.2
percent. These findings validate the power of integrating causal, behavioral, and reinforcement learning models
in a single pipeline to optimize customer equity.
Factor-Based Reward Design Analysis
Although Jung and Oh (2025) concentrated on the financial contexts  and conducted work on factor -based deep
reinforcement learning in the context of asset allocation, their work offers insights, which can be applied to the
marketing setting. Their relative study on the designs of the static beta, dynamic beta and momentum  rewards
indicate that time-varying factor exposure greatly boosts performance, especially in volatile market regimes.
Table 6: Factor-Based Reward Design Performance Comparison
Reward Design Annualized Return Sharpe Ratio Maximum Drawdown Volatility Win Rate
Sharpe Baseline 19.8% 1.23 -18.5% 16.1% 58.2%
Static-β 21.2% 1.31 -17.2% 16.2% 59.8%
Dynamic-β (Single
Asset) 23.4% 1.45 -15.8% 16.1% 62.3%
Momentum (Single
Asset) 23.7% 1.44 -16.1% 16.4% 61.9%
Dynamic-β (Multi
Asset) 24.1% 1.52 -14.9% 15.8% 64.1%
Momentum (Multi
Asset) 24.3% 1.50 -15.2% 16.2% 63.7%
Factor-Adaptive
Combined 25.6% 1.58 -14.2% 16.0% 66.4%
The main marketing application is that reward systems that include time -varying elements (e.g., momentum of
engagement, risk of retention) can support more responsive policy than reward systems that are not time -
dependent (Jung and Oh, 2025). Dynamic-Beta in equity assets returned 23-24% annually compared to the Sharpe
baseline of around 20%. Multi -asset portfolios with momentum -based and dynamic reward designs
systematically beat their static benchmarks. Factor -Adaptive Combined approach has the highest an nualized
(25.6%), Sharpe (1.58) and win (66.4) percent and lowest maximum drawdown (-14.2%).
Sentiment-Augmented Approach
Adding sentiment signals to RL models has proven to be very effective in improving performance. Sentiment -
Augmented PPO (SAPPO) was created by Kirtac (2025) to use daily asset -level sentiment on financial news in
state representations and policy gradients.

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 364
Table 7: Sentiment-Augmented RL Performance
Method Sharpe Ratio Annualized Return Maximum Drawdown Information Ratio Calmar Ratio
Vanilla PPO 1.67 57.2% -28.4% 1.45 2.01
PPO + Sentiment 1.89 68.4% -24.1% 1.68 2.84
SAPPO (Full) 2.07 82.6% -22.3% 1.85 3.70
The increase in Sharpe ratio was 1.67 to 2.07 and annualized return was 57 to 83 in SAPPO compared to 1.67 to
2.07 and 57 to 83 respectively in vanilla PPO (Kirtac, 2025). The maximum drawdown fell to -22.3% as compared
to -28.4%, and Calmar ratio rose to 3.70 as compared to 2.01. Although the given study is about portfolio
optimization, the approach can be applied to the marketing setting where unstructured data (r eviews, social
media, surveys) has useful information regarding the customer’s preferences and relationship dynamics (Meire
et al., 2019; Ngai and Wu, 2022).
Comparative Analysis Across Different Market Conditions
Table 8: RL Performance Across Market Regimes
Market Regime Static Approach ROI RL Approach ROI Improvement Adaptability Score
Stable Growth 0.85 1.12 +31.8% Moderate
Mild Volatility 0.72 1.05 +45.8% High
High Volatility 0.48 0.92 +91.7% Very High
Market Crash 0.31 0.76 +145.2% Exceptional
Recovery Phase 0.62 0.98 +58.1% High
The RL approaches are more adaptable to all market regimes, and the greatest improvements are seen in times of
high volatility and market crashes. In the high volatility, RL improves 91.7 percent over the approaches that are
static, and in times of market crashes, the improvement is 145.2 percent. This observation demonstrates the
importance of dynamic, adaptive policies in the dynamic markets where the fixed policies are becoming ineffective
(Mandania et al., 2026; Kirtac, 2025).
Computational Performance Analysis
Table 9: Computational Performance Analysis
Method Training Time (Seconds) Inference Time (ms) Memory Usage (GB) Scalability (1M Customer
Business Rule 5 0.5 0.1 Excellent
Traditional Uplift Model 45 2.0 0.5 Good
Static Causal Forest 120 5.0 1.2 Moderate
Dynamic Causal RL 525 8.0 4.5 Moderate
Distributed Causal RL 180 3.0 8.0 Excellent
The RetailCo data on the server with an Intel Xeon E5-2680 v4 processor and NVIDIA Tesla V100 card take around
525 seconds to run Dynamic Causal RL (see Wang and Chen, 2025). Although this is more than the training time
of simpler methods, this is acceptable within the offline model development. Distributed Causal RL is 180 seconds

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 365
to train with parallelization, and it scales very well when there are large numbers of customers. RL is suitable in
real-time applications because its inference time is 3 -8 milliseconds, meaning the decisions have to be made
within milliseconds (Mandania et al., 2026; Wang and Chen, 2025).
Implementation Considerations
Data Requirements and Infrastructure
Customer equity optimization with the help of RL involves a high level of data infrastructure (Ram and Zhang,
2022; Line et al., 2020). The data requirements are the minimum:
Transaction Histories
Detailed customer purchase history, such as time, value, and product specifications (Fader et al., 2005; Reinartz
and Kumar, 2000, 2003). These offer the basis of estimating the customer value and behavioral evolution (Kumar
et al., 2010; Salisbury et al., 2023).
Interaction Records
Information about all customer-firm contacts in all channels such as visiting websites, opening emails, contacting
customer service, social media use (Bijmolt et al., 2010; Meire et al., 2019). These indicators of engagement play
an important role in captu ring the customer relationship status, especially when transaction data is sparse
(Ascarza et al., 2018; Zhang et al., 2015).
Marketing Action logs
Documentations of all marketing activities done to each customer such as when, what, and through what medium
(Mandania et al., 2026; Wang and Chen, 2025). These data are required in the process of learning the effects of
actions and also in the action prediction task in state representation learning (Ascarza et al., 2025).
Contextual Variables
Customer behavior is affected by external influences including seasonality, competition, and macroeconomic
conditions (Jung and Oh, 2025; Kirtac , 2025). The inclusion of these variables will allow the RL agent to
differentiate between marketing action-induced changes and changes induced by external factors.
These data are high -dimensional and this necessitates feature engineering and dimensionality reduction (Ngai
and Wu, 2022; Ram and Zhang, 2022). Section 3.2 outlines state representation learning and is capable of
automatically learning features that are m eaningful and maintaining the Markov property (Ascarza et al., 2025;
Allen et al., 2021).
Offline Policy Learning
One of the most practical challenges is critical: most firms are not able to experiment online to learn the best
policies (Levine et al., 2020; Kumar et al., 2020). Offline RL works around this issue by training policies based on
the historical data acquired under the current policy of the firm.
Conservative Q-Learning (CQL) offers a powerful method that punishes Q-values of state-action pairs that are not
sufficiently represented in the offline data (Kumar et al., 2020). This will stop the policy from taking advantage of
the measures that seem to be worthwhile in the data but are really overvalued because of the distributional shift.
CQL has a conservative property that is critical to marketing applications, where the data -generating procedure
might not have searched through all the possible actions (Wang and Chen, 2025; Levine et al., 2020).
Table 10: Offline RL Method Comparison
Method Data Efficiency Policy Safety Performance in Sparse Data Computational Cost
Behavioral Cloning High High Poor Low

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 366
Fitted Q-literation Moderate Low Moderate Moderate
BCQ Moderate High Good Moderate
CQL High Very High Very Good High
IQL High High Excellent Moderate
CQL + State Representation Very High Very High Excellent High
CQL using state representation learning is the most efficient offline RL approach in sparse data environments with
regard to data efficiency, policy safety, and performance. The combination is especially useful in marketing
applications where the data might be constrained on some segments of customers or types of actions.
The main considerations of offline RL in marketing are:
Distributional Shift
The past policy could have discriminated against some customer groups generating discrepancies in the data
(Ascarza et al., 2018; Zhang et al., 2015). This is solved by CQL and other offline RL algorithms, which penalize
extrapolation to underrepresented areas (Kumar et al., 2020; Levine et al., 2020).
Confounding
The marketing activities tend to be associated with unknown customer attributes (Devriendt et al., 2020;
Gutierrez and Gérardy, 2017). Selection biases can be identified by using causal inference methods (including
causal forests to evaluate treatment effects, Wager and Athey, 2018), to separate the causal effect of actions and
selection biases (Wang and Chen, 2025).
Partial Observability
The companies are unable to see all the aspects that determine customer behaviour , including competition
interactions or personal situations (Netzer et al., 2008; Zhang et al., 2015). The partial observability can be solved
by (1) adding more data sources (Ram & Zhang, 2022; Line et al., 2020), (2) applying recurrent neural networks
or other sequential models to learn the dynamics of the hidden states (Ascarza et al., 2025; Allen et al., 2021), and
(3) using partially observable MDP (POMDP) formulations when it makes sense (Kaelbling, Littman, and
Cassandra, 1998).
Organizational and Managerial Challenges
In addition to technical aspects, RL implementation based on customer equity optimization is challenging to the
organization (Libai et al., 2020; Ngai and Wu, 2022):
Change Management
The transition to active, adaptive policies rather than fixed, rule-based ones are one of the shifts in the marketing
philosophy (Mandania et al., 2026). Marketing teams that are used to planning in terms of campaigns might be
reluctant to adopt the approach of ongoing data-driven decision-making (Libai et al., 2020).
Interpretability
RL policies may be opaque, so it is hard to know why certain actions are suggested by the managers (Doshi-Velez
and Kim, 2017). Recent interpretable RL and explainable AI research is applicable in this case, as well as the
application of policy visualizations and policy explanation tools (Rudin, 2019; Molnar, 2022).
Risk Management
Adaptive policies can undertake actions that the human managers would not have anticipated and accepted (Wang
and Chen, 2025). This risk can be addressed with the help of conservative learning and guardrails (e.g., action

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 367
space constraints) (Kumar et al., 2020). Also, to foster confidence, RL can be first introduced as a decision-support
system (with human supervision) to detect edge cases (Libai et al., 2020).
Competing Priorities
The reward function cannot necessarily capture marketing objectives beyond customer equity (Kumar et al.,
2025). Competing priorities can be balanced with the help of multi-objective RL methods (Torkzadeh and Dhillon,
2025), but it is up to managers to specify the weights of objectives.
Research Gaps and Future Directions
Integration of Causal Inference and RL
Although there has been an important development in the integration of causal inference and RL (Wang and Chen,
2025; Kumar et al., 2025), there are still some key questions. What do we do to update the causal effect estimates
based on new data? What to do with the exploration-exploitation trade-off when we do not know the causal impact
of actions?
What are the best ways to model and include dynamic treatment effects in the process of policy optimization?
Developing studies on causal RL (Bica, Järvelin, and van der Schaar, 2020; Zhang, Bica, and van der Schaar, 2021)
and dynamic uplift modelling (Wang and Chen, 2025) are promising to explore, yet still require more research.
Specifically, it is worth considering integrating structural causal models (Pea rl, 2009) with RL architectures,
which would allow treating confounding more principled and generalizing to new settings in a more effective
manner.
Long-Horizon Effects and Temporal Dependencies
Customer equity optimization also consists of long -term effects that might not be realized under normal
discounting (Rust et al., 2000, 2004; Berger et al., 2006). What is the best approach to optimizing marketing
activities, which influence customer acqui sition, retention, and growth? How long should the time horizon to
assess customer equity impacts be, and how should it differ by industry and customer group (Kumar et al., 2010;
Salisbury et al., 2023)?
Long horizon RL is especially susceptible to the problems of credit assignment, sparseness, and the curse of
dimensionality (Sutton and Barto, 1998), which are especially pronounced in marketing applications. Hierarchical
RL models (Dayan and Hinton, 1993;  Bacon, Harb, and Precup, 2017), where top -level policies distribute
resources throughout the customer lifecycle and low-level policies execute particular interventions, can be a way
out.
Personalization of Heterogeneity
The marketing strategy is focused on customer heterogeneity: firms act differently in regards to different
customers (Rust et al., 2000, 2004; Reinartz and Kumar, 2000, 2003). Although RL policies can theoretically
personalize their actions using state -dependent policies, learning personalized policies with limited data is
challenging.
A personalization with small amounts of data on a customer could be facilitated by few -shot and meta-learning
(Finn, Abbeel, and Levine, 2017; Wang et al., 2019). As shown in Kumar et al. (2025), cross -domain adaptability
can be enhanced by transfer learning. Also, more efficient personalization can be promoted through
representation learning which identifies the types or segm ents of customers (Zhang et al., 2015; Netzer et al.,
2008).
Multi-Channel and Omnichannel Optimization
Contemporary marketing considers the use of various channels, such as email, display advertising, social media,
direct mail, SMS, and face -to-face communication, which interrelate in complicated forms (Berman and Thelen,
2024; Ram and Zhang, 2022). To optimize customer equity across channels, it is necessary to know how channel

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 368
actions influence response in other channels, the channel preference differences among customers, and how the
channel mix influences long-term relationship development (Libai et al., 2020; Ngai and Wu, 2022).
Multi-agent RL, when various agents control different channels but collaborate to achieve a common goal (Lowe
et al., 2017; Kumar et al., 2025), is a promising solution. Nevertheless, there are coordination issues, channel credit
assignment, and the threat of policy conflicts that need to be developed.
Competitive Dynamics
Customer equity is competitive of nature: the customer value is subject not only to the actions of a firm, but also
to the actions of competitors (Rust et al., 2000, 2004; Karvanen et al., 2014). Although the original customer equity
framework was able to capture the competitive dynamics by brand -switching matrices (Rust et al., 2004), the
majority of the RL-based models assume that the firm is acting in isolation.
Competitive dynamics are tricky to integrate into RL models, with the more competition-related problems of the
need to model their actions (which might not be observable), non-stationarity due to competitive behaviour, and
the problem of expensive competitive escalation. These challenges can be overcome by multi-agent RL solutions
that treat competitors as agents (Lowe et al., 2017; Balch, 2025), though the formulations and solution concepts
are yet to be formulated.
Ethical Consideration and Fairness
The RL policies are maximizing the interests of the firm, which may be at the cost of customer welfare or fairness
(Balch, 2025; Doshi-Velez and Kim, 2017). What are the ethical considerations of RL-based customer treatment?
What are the ways of integratin g fairness constraints in RL optimization? What can be done to ensure
transparency and explainability?
Recent research on fairness in market environments (Balch, 2025) indicates that multi -objective RL can strike a
balance between profitability of firms and the well-being of their stakeholders. Greater attention to ethical RL in
marketing should be explored , such as specifying fairness limits and detecting harmful policies and creating
auditing and accountability systems (Rudin, 2019; Molnar, 2022).
Empirical Validation and Generalizability
Although the empirical evidence is growing, it is not yet clear that the results can be generalized to other sectors,
types of customers or the market conditions (Wang and Chen, 2025; Mandania et al., 2026). The majority of the
studies have been performed in a particular setting such as ferry travel (Mandania et al., 2026), retail (Wang and
Chen, 2025), and financial services (Kumar et al., 2025) and it is not clear how the findings can be generalized.
Industry systematic benchmarking research would aid in determining the strength of RL strategies. Also,
experiments that would test RL in various market situations (e.g., during economic expansions and contractions)
would help to understand the flexibility  of RL policies (Jung & Oh, 2025; Kirtac, 2025). Lastly, field experiments
pitting RL policies with other approaches would be the most effective evidence of effectiveness.
CONCLUSION
Summary of Contribution
In this paper, a thorough customer equity optimization through reinforcement learning has been introduced. We
have presented that RL is sequential and adaptive, which is inherently consistent with dynamic development of
customer-firm relationships, providing its major benefits in comparison with traditional, non -adaptive methods
(Mandania et al., 2026; Wang and Chen, 2025; Ascarza et al., 2025). The framework combines the progress in state
representation, reward design, and learning algorithms to tackle the distinctive problems of marketing
applications, such as the data sparsity, partial observability and non-stationarity.
Important contributions are: (1) a theoretical formulation of customer equity optimization as a multi -response
MDP with time -varying engagement and retention signals (Ascarza et al., 2025; Sutton and Barto, 1998); (2) a

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 369
factor-sensitive reward design with time -varying engagement and retention signals (Jung and Oh, 2025; Wang
and Chen, 2025); (3) an integration of conservative Q -learning in learning offline policies (Kumar et al., 2020;
Levine et al., 2020); (4) a synopsis of empirical evidence that shows significant performance improvements (Wang
and Chen, 2025; Kumar et al., 2025); (5) a prospective research agenda that identifies key gaps and opportunities
(Wang and Chen, 2025).
Implications for Theory
The RL view of customer equity has a number of implications to the marketing theory. One, it disputes the view of
a static customer value on which much of the CLV and customer equity literature is based (Rust et al., 2000, 2004),
and instead provides a dynamic perspective of value formed by a series of interactions (Zhang et al., 2015; Netzer
et al., 2008). This outlook is consistent with the increasing importance of customer interactions and relationships
in marketing studies (Bijmolt et al., 2010; Meire et al., 2019).
Second, the value co -creation idea (Prahalad and Ramaswamy, 2004) is implemented through the RL learning
process: the feedbacks on the customer reaction are taken as the signals to update the policy, establishing a
collaborative cycle where value co -creation is observed between the firm and its customers (Mandania et al.,
2026). This goes beyond the passive customer-as-receiver’s perspective which has prevailed in the CLV literature
(Rust et al., 2000, 2004).
Third, the consideration of customer equity as a sequential choice problem changes the emphasis on optimization
of individual campaigns to the optimization of relationship paths (Ascarza et al., 2025; Salisbury et al., 2023). This
means that the effectiveness of marketing cannot be quantified based on specific campaign measures but by the
accumulation of customer relationship measures over the years (Kumar et al., 2010; Berger et al., 2006).
Implications for Practice
The framework offers a direction to marketing practitioners in order to be more adaptive and data-driven when
it comes to managing the customers (Mandania et al., 2026; Libai et al., 2020). Continuous policy updating, which
is made possible by the customer response, helps firms to be more responsive and adjust to the changing market,
competitive dynamics, and customer preferences (Wang and Chen, 2025; Jung and Oh, 2025).
Empirical results indicate the significant enhancement in the performance: a 27 percent or higher improvement
in targeting efficiency, a 58 percent or higher improvement in ROI, and an 85 percent or higher improvement in
CLV impact (Wang and Chen, 2025). As much as these findings were on particular contexts, they are large enough
to be of interest to marketing leaders (Libai et al., 2020; Ngai and Wu, 2022).
Optimizing customer equity with RL implies the investment  in data infrastructure, data analytics, and
organizational change (Ram & Zhang, 2022; Line et al., 2020). The returns that may be achieved, however,
especially in volatile markets, where the inapplicability of the static approaches is growing, justify suc h
investments (Mandania et al., 2026; Kirtac, 2025).
Concluding Remarks
The maximization of customer equity in a volatile market is one of the most important challenges and
opportunities of contemporary marketing organizations (Rust et al., 2000, 2004; Libai et al., 2020). Although
traditional, often static, methods are still useful in a calm setting, they are not sufficient when coping with the
turbulence of the modern market (Mandania et al., 2026; Ascarza et al., 2025). A more interesting option is
reinforcement learning: a dynamic, adaptive, data-driven method that learns to optimize marketing decisions over
time by the customer response to its actions (Sutton and Barto, 1998; Wang and Chen, 2025).
The model shown in this paper offers a basis of  both theoretical study and practice. We have demonstrated that
RL-based methods can result in significant performance gains, mitigate major challenges in their implementation,
and that there are potential avenues to explore in future studies. The combination of reinforcement learning and
customer equity optimization will probably form a part of the modern marketing practice as data availability,

Khan et al. Int. J. Business & Management Sciences 7(5), 2026
www.ijbmsjournal.com E-ISSN 2708-4337 | P-ISSN 2708-4329 Page 370
computing power, and the sophistication of algorithms are continuously improving (Ngai and Wu, 2022; Libai et
al., 2020).
The transition to dynamic customer equity optimization is not so smooth, and there are technical obstacles,
organizational, and ethical (Balch, 2025; Doshi -Velez and Kim, 2017). But the potential payoffs are more
responsive marketing, better customer relations, and improved firm value, so this journey is not only worth the
effort, but essential to firms wishing to succeed in an ever more turbulent world.
REFERENCES
Allen, C., Bouchard, G., & Balduzzi, D. (2021). Representation learning for reinforcement learning with Markov property
preservation. International Conference on Machine Learning, 180-190.
Allen, C., Bouchard, G., & Balduzzi, D. (2021). Representation learning for reinforcement learning with Markov property
preservation. International Conference on Machine Learning, 180-190.
Ascarza, E., & Hardie, B. G. S. (2013). A joint model of usage and churn in contractual settings.  Marketing Science, 32(4),
570-590.
Ascarza, E., Netzer, O., & Hardie, B. G. S. (2018). Some customers would rather leave without saying goodbye. Marketing
Science, 37(1), 54-77.
Ascarza, E., Zhang, J., & Netzer, O. (2025). State representation learning for reinforcement learning in
marketing. Marketing Science, 44(1), 1-25.
Bacon, P. L., Harb, J., & Precup, D. (2017). The option-critic architecture. Proceedings of the AAAI Conference on Artificial
Intelligence, 31(1), 1726-1734.
Bacon, P. L., Harb, J., & Precup, D. (2017). The option-critic architecture. Proceedings of the AAAI Conference on Artificial
Intelligence, 31(1), 1726-1734.
Balch, S. (2025). Profit equitably: An investigation of market maker's impact on equitable outcomes.  Working Paper, 1-
35.
Balch, S. (2025). Profit equitably: An investigation of market maker's impact on equitable outcomes.  Working Paper, 1-
35.
Bell, D. E., Ho, T. H., & Tang, C. S. (2002). Determining where to shop: Fixed and variable costs of shopping.  Journal of
Marketing Research, 39(3), 308-321.
Berger, P. D., & Bechwati, N. N. (2001). The allocation of promotion budget to maximize customer equity. Omega, 29(1),
49-61.
Berger, P. D., Eechambadi, N., George, M., Lehmann, D. R., Rizley, R., & Venkatesan, R. (2006). From customer lifetime
value to shareholder value: Theory, empirical evidence, and issues for future research. Journal of Service Research,
9(2), 156-167.
Berman, B., & Thelen, S. (2024). Omnichannel customer equity: A framework for digital transformation.  Journal of
Retailing, 100(1), 1-18.
