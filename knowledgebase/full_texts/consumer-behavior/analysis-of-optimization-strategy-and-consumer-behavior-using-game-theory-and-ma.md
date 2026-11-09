---
title: Analysis of Optimization Strategy and Consumer Behavior using Game Theory and Markov Chain on Marketplace
  Competition.
url: https://doi.org/10.15294/ujm.v15i1.24237
category: consumer-behavior
subcategory: review
date: 2026-10
venue: Unnes Journal of Mathematics
authors:
- Zamzammaimatul Zalfa Laila
source: openalex-oa
pdf_url: https://journal.unnes.ac.id/journals/ujm/article/download/24237/11874
pages: 14
chars: 39974
fetched_at: '2026-11-08T19:34:19+00:00'
kb_version: 1
---

# Analysis of Optimization Strategy and Consumer Behavior using Game Theory and Markov Chain on Marketplace Competition.

UJM 15 (1) 2026
UNNES Journal of Mathematics
http://journal.unnes.ac.id/sju/index.php/ujm

Analysis of Optimization Strategy and Consumer Behavior using Game Theory
and Markov Chain on Marketplace Competition.
Zamzammaimatul Zalfa Laila*, Wakhid Fitri Albar

Department of Mathematics, Faculty of Mathematics and Natural Science,
Universitas Negeri Semarang, Semarang, 50229, Indonesia
Article Info
________________
Article History:
Recived 05-05-2025
Accepted 20-04-2026
Published 30-04-2026

________________
Keywords:
Consumer behavior, game
theory, markov chain,
Marketplace, Optimization
Strategy.
Abstract
____________________________________________________________
_______
Indonesia is one of the largest e-commerce markets, resulting in increasingly intense
competition among marketplaces. This situation highlights the need to identify
effective competitive strategies and understand consumer loyalty to maintain
marketplace co mpetitiveness. This study aims to determine optimal marketplace
strategies using game theory, analyze marketplace loyalty using Markov chains, and
examine consumer behavior among active students at UNNES and IPMAFA. Data
were collected through questionnair es from 250 students selected using the Slovin
formula and analyzed using SPSS and POM -QM. Seven attributes were examined:
product diversity, price, shipping costs, discount vouchers, feature completeness,
payment methods, and product reviews. The results show that the game values for
Shopee vs. TikTok Shop (Tokopedia), TikTok Shop vs. Lazada, and Shopee vs.
Lazada are 70.59, 84, and 135.14, respectively, with discount vouchers, product
reviews, and price emerging as the dominant strategies. The Markov chai n results
indicate transition probabilities of 48.52% for Shopee, 39.50% for TikTok Shop and
Tokopedia, and 11.98% for Lazada. The novelty of this study lies in integrating game
theory and Markov chains to identify competitive strategies and predict market place
loyalty. Discount vouchers are the most preferred attribute influencing purchasing
decisions. Therefore, marketplaces should maintain their competitive advantages,
particularly through effective promotional strategies, while continuously adapting to
consumer preferences to reduce customer switching and strengthen loyalty.

How to cite:
Laila, Z. Z.  & Albar, W. F. , 2026. Analysis of Optimization Strategy and Consumer
Behavior using Game Theory and Markov Chain on Marketplace Competition .
UNNES Journal of Mathematics. 15(1): 67-80

© 2025 Universitas Negeri Semarang
*Correspondence Address
E-mail: zalfalaila12@gmail.com
p-ISSN 2252-6943
e-ISSN 2460-5859

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

68

1. Introduction
 Data from the We Are Social shows that in 2025, there will be 212 million internet users in Indonesia out of a total
population of 285 million in 2024 [1]. The increase in the number of internet users will certainly also impact the growth
in the number of marketplace users. A marketplace is a platform that serves as an intermediary between sellers and
buyers to conduct online transactions. Based on [2], the three most accessed marketplaces by users in Indonesia are
Shopee, Tokopedia, and Lazada. On the other hand, internet users also access social media. Tiktok ranks fourth as
the most used social media [1]. With these advantages, TikTok has partnered with Tokopedia by providing the TikTok
Shop [3]. The data shows that the trend of online shopping is growing very rapidly in Indonesia. Therefore, these
marketplaces are competing fiercely to maintain their existence. An optimal strategy can help a marketplace win the
market competition. To determine the optimal strategy, the strategy can be analyzed by utilizing one of the operation
research through game theory  [4], [5], [6], [7], [8], [9] . Game theory is one of the decision -making methods that
combines mathematical theory and economic theory [4]. The main objective of game theory is to find the optimal
strategy for players in the game [4].
 Game theory uses pure strategies and mixed strategies [7], [10], [11] . First, the problem is solved using pure
strategies to find the saddle point [10], [11]. If the pure strategy does not yield a saddle point, then the solution is carried
out using a mixed strategy [10]. The steps to be taken in this strategy are to reduce the rows and columns using the
principle of dominance, then find the saddle point as done in the pure strategy  [10]. If the saddle point is still not
obtained, then the game value is calculated using one of the alternative methods, namely linear programming  [10],
[11].
 The variety of marketplaces allows users to access the various available marketplaces. This certainly impacts
user loyalty and allows for brand (marketplace) switching. This marketplace migration can be analyzed using the
Markov chain method [5], [12]. Markov chain have a special property of probability that involves how to process will
evolve in the future depending only on the current state of the processs and not on the past [10]. The Markov chain
method is applied by calculating its transition probabilities over a specific time period.
 In choosing and using the desired product, there is a behavior of consumers who are influenced by certain factors
such as psychological factors and other external factors to consider buying the product [13]. This action is referred to
as consumer behavior, which is the way consumers choose, buy, and use products or services to meet their needs or
desires [14]. This consumer behavior analysis is needed to find out what factors influence consumers in considering
buying a product. In this research, data will be collected from respondents who are active students of Universitas Negeri
Semarang and Institut Pesantren Mathaliu’ul Falah. Students from both universities were chosen to conduct an analysis
of consumer behavior in making pur chasing decisions. After conducting preliminary data collection, it was found that
the three marketplaces with the most users are Shopee, Tokopedia or Tiktok Shop, and Lazada.
 Based on the background that has been described, several problem formulations in this research: First, how can
the optimal strategy against marketplace competition be formulated using game theory? Second, what is the
percentage of user loyalty for each marketplace using Markov chain? Then, how is the consumer behavior analysis of
active students of Universitas Negeri Semarang and Institut Pesantren Mathaliu’ul Falah? This research analyzed
optimal strategies using game theory, user loyalty with Markov chai n, and provides a dashboard that presents data
visualization results from the analysis of consumer behavior of students at Universitas Negeri Semarang and Institut
Pesantren Mathali’ul Falah.

2. Method
2.1. Research Population and Research Sample
 The population of this study is the active students from Universitas Negeri Semarang dan Institut Pesantren
Mathali’ul Falah who access the marketplace. This study uses the stratified random sampling technique. To determine
the sample size, the Slovin formula is used. Here is the formula to determine the total sample from each university.
𝑛 = 𝑁 1 + 𝑁𝑒2,
where 𝑁: total population, 𝑛: number of sampel, and 𝑒: error. Because of the number of students in each faculty is
different, then a proportional calculation is used. Here is the formula.
𝑛𝑖 = 𝑁𝑖 𝑁 𝑛,
where 𝑁𝑖: total population of the 𝑖-th stratum and 𝑛𝑖: number of samples of the 𝑖-th stratum.

2.2. Research Variables
 The variables in this study are the attributes of the Shopee, Tiktok Shop (Tokopedia), and Lazada. Here are the
attribute variables in this study.
Table 1. Attribute Variables
Game Attributes
Variables
Shopee Tiktok Shop (Tokopedia) Lazada
Product Diversity 𝑋1 𝑌1 𝑍1
Price 𝑋2 𝑌2 𝑍2

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

69
Shipping Costs 𝑋3 𝑌3 𝑍3
Discount
Vouchers 𝑋4 𝑌4 𝑍4
Feature
Completeness 𝑋5 𝑌5 𝑍5
Payment Methods 𝑋6 𝑌6 𝑍6
Product reviews 𝑋7 𝑌7 𝑍7

2.3. Data and Data Sources
 The data that used in this research is primary data obtained from questionnaires. The questionnaire in this study
is presented in the form of a form through Google Forms. Two questionnaires were distributed to collect data for game
theory and Markov chain calculations. The first questioonaire is preliminary questionnaire to collect data on the three
most used marketplaces, marketplace marketing strategies, and understand the factors influencing users purchasing
decisions. The second one is a research questionnaire to collect data on user preferences in making marketplace
selection decisions.

2.4. Game Theory
Data analysis with game theory is used to determine the game value of each marketplace and to identify the
strategies that are the strengths of those marketplaces. Each game in game theory has two players, namely the row
player and the column player  [10], [11], [15]. Each player will gain and lose based on the strategies they use, where
the row player maximizes gains while the column player minimizes losses [15], [16] . The profit or loss can be
determined by looking at the pay-off values of each player's strategy [15], [17]. Here is the pay-off matrix.
Table 2. Pay-off Matrix
 𝑌1 𝑌2 ⋯ 𝑌𝑛
𝑋1 𝐴11 𝐴12 ⋯ 𝐴1𝑛
𝑋2 𝐴21 𝐴22 ⋯ 𝐴2𝑛
⋮ ⋮ ⋮ ⋮ ⋮
𝑋𝑚 𝐴𝑚1 𝐴𝑚2 ⋯ 𝐴𝑚𝑛
where 𝑃1: row player; 𝑃2: column player; 𝑋𝑖: strategy of player 1, 𝑖 = 1, 2, 3, … , 𝑚, ; 𝑌𝑗: strategy of player 2, 𝑗 =
1, 2, 3, … , 𝑛; 𝑎𝑖𝑗: pay-off value, 𝑖 = 1, 2, 3, . . . , 𝑚 and 𝑗 = 1, 2, ,3, … , 𝑛.

Based on the table 2, the minimum value is taken for the strategy of each row player. Meanwhile, the strategy of
each column player is taken as the maximum value. After that, the row player must choose a strategy whose minimum
pay-off is the largest, while the column player must choose a strategy w hose maximum pay -off is the smallest  [10],
[11]. When the maximin value equals the minimax, then that point is a saddle point [10], [11]. When the saddle point is
reached, the game can be solved with a pure strategy. However, when the saddle point is not reached, the game
cannot be solved with pure strategies. Therefore, according to  [11], to achieve the equilibrium point, a mixed strategy
is used. A game with a mixed strategy is a game where the strategy used by each player is a combination of various
different strategies [7]. A mixed strategy game is a game where the strategy used by each player is a combination of
various different strategies [7]. If both players have more than two strategies, then the dominance technique can be
applied [18]. If a saddle point is obtained, the game can be continued with a solution using pure strategies. If a saddle
point is still not found, then it is necessary to use another alternative solution, one of which is linear programming.
Every game with mixed strategies can be solved by transforming it into a linear programming problem [10].
The row player (𝑃1) is the player who maximizes profit. So, the optimal strategy for 𝑃1 is the choice that
cosrresponds to the maximin price for the mixed strategy.
max
𝑥𝑖 {min (∑ 𝑎𝑖1𝑥𝑖
𝑚
𝑖=1
, ∑ 𝑎𝑖2𝑥𝑖
𝑚
𝑖=1
, … , ∑ 𝑎𝑖𝑛𝑥𝑖
𝑚
𝑖=1
)}
where ∑ 𝑥𝑖 𝑚 𝑖=1 = 1 and 𝑥𝑖 ≥ 0 for all 𝑖 = 1,2, … 𝑚. Let,
 𝑉 = 𝑚𝑖𝑛 (∑ 𝑎𝑖1𝑥𝑖
𝑚
𝑖=1
, ∑ 𝑎𝑖2𝑥𝑖
𝑚
𝑖=1
, … , ∑ 𝑎𝑖𝑛𝑥𝑖
𝑚
𝑖=1
) (1)
then, (1) can be written as max 𝑓0 = 𝑉. We have

∑ 𝑎𝑖𝑗𝑥𝑖
𝑚
𝑖=1
≥ 𝑉, 𝑗 = 1,2, … , 𝑛
where ∑ 𝑥𝑖 𝑚 𝑖=1 = 1 and 𝑥𝑖 ≥ 0 for all 𝑖 = 1,2, … , 𝑚;  𝑉 = game value [11]. Let 𝑉 > 0, then  ∑ 𝑎𝑖𝑗𝑥𝑖 𝑚 𝑖=1 𝑉 ≥ 1, 𝑗 = 1,2, … , 𝑛.
Therefore,
∑ 𝑥𝑖 𝑚 𝑖=1
𝑉 (∑ 𝑎𝑖𝑗 𝑚 𝑖=1 ) ≥ 1, 𝑥𝑖 ≥ 0, for all 𝑖. Because of ∑ 𝑥𝑖 𝑚 𝑖=1 = 1, then ∑ 𝑥𝑖 𝑚 𝑖=1 𝑉 = 1 𝑉. Let 𝑥𝑖 𝑉 denoted as 𝑋𝑖 where 𝑖 =
1,2, … , 𝑚. Because of 𝑀𝑎𝑥 𝑉 = 𝑀𝑖𝑛
1
𝑉 = 𝑀𝑖𝑛(𝑋1 + 𝑋2 + ⋯ + 𝑋𝑚), then the general form of the linear program for the row
player is as follows.
Minimize 𝑓0 = 𝑋1 + 𝑋2 + ⋯ + 𝑋𝑚

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

70
Constraint,
𝑎11𝑋1 + 𝑎21𝑋2 + ⋯ + 𝑎𝑚1𝑋𝑚 ≥ 1
𝑎12𝑋1 + 𝑎22𝑋2 + ⋯ + 𝑎𝑚2𝑋𝑚 ≥ 1
⋮
𝑎1𝑛𝑋1 + 𝑎2𝑛𝑋2 + ⋯ + 𝑎𝑚𝑛𝑋𝑚 ≥ 1
where 𝑓0 =
1
𝑉  and
𝑥𝑖
𝑉 = 𝑋𝑖; 𝑋𝑖 ≥ 0; 𝑖 = 1,2, … , 𝑚 [11]
The column player (𝑃2) is the player who minimizes loses. So, the optimal strategy for 𝑃2 is the choice that
cosrresponds to the minimax price for the mixed strategy.
min
𝑦𝑗 {max (∑ 𝑎1𝑗𝑦𝑗
𝑛
𝑗=1
, ∑ 𝑎2𝑗𝑦𝑗
𝑛
𝑗=1
, … , ∑ 𝑎𝑚𝑗𝑦𝑗
𝑛
𝑗=1
)}
where ∑ 𝑦𝑗 𝑛 𝑗=1 = 1 and 𝑦𝑗 ≥ 0 for all 𝑗 = 1,2, … 𝑛. Let,

 𝑉 = 𝑚𝑎𝑥 (∑ 𝑎1𝑗𝑦𝑗
𝑛
𝑗=1
, ∑ 𝑎2𝑗𝑦𝑗
𝑛
𝑗=1
, … , ∑ 𝑎𝑚𝑗𝑦𝑗
𝑛
𝑗=1
) (2)
then, (2) can be written as  𝑚𝑖𝑛 𝑔0 = 𝑉. We have
∑ 𝑎𝑖𝑗𝑦𝑗
𝑛
𝑗=1
≤ 𝑉, 𝑖 = 1,2, … , 𝑚
where  ∑ 𝑦𝑗 𝑛 𝑗=1 = 1 and 𝑦𝑗 ≥ 0 for all  𝑗 = 1,2, … , 𝑛 ; 𝑉 = game value [11]. Let 𝑉 > 0, then ∑ 𝑎𝑖𝑗𝑦𝑗 𝑛 𝑗=1 𝑉 ≤ 1, 𝑖 = 1,2, … , 𝑚.
Therefore
∑ 𝑦𝑗 𝑛 𝑗=1
𝑉 (∑ 𝑎𝑖𝑗 𝑛 𝑗=1 ) ≤ 1, for all 𝑖 = 1,2, … , 𝑚. Because of  ∑ 𝑦𝑗 𝑛 𝑗=1 = 1, then ∑ 𝑦𝑗 𝑛 𝑗=1 𝑉 = 1 𝑉.  Let  𝑦𝑗 𝑉  denoted as 𝑌𝑗
where 𝑗 = 1,2, … , 𝑛. Since 𝑀𝑖𝑛 𝑉 = 𝑀𝑎𝑥
1
𝑉 = 𝑀𝑖𝑛(𝑌1 + 𝑌2 + ⋯ + 𝑌𝑛), the general form of the line ar program for the
column player is as follows.
Maximize 𝑔0 = 𝑌1 + 𝑌2 + ⋯ + 𝑌𝑛
Constraint,
𝑎11𝑌1 + 𝑎12𝑌2 + ⋯ + 𝑎1𝑛𝑌𝑛 ≤ 1
𝑎21𝑌1 + 𝑎22𝑌2 + ⋯ + 𝑎2𝑛𝑌𝑛 ≤ 1
⋮
𝑎𝑚1𝑌1 + 𝑎𝑚2𝑌2 + ⋯ + 𝑎𝑚𝑛𝑌𝑛 ≤ 1
where 𝑔0 =
1
𝑉  and
𝑦𝑗
𝑉 = 𝑌𝑗; 𝑦𝑗 ≥ 0; 𝑗 = 1,2, … , 𝑛 [11].

2.5. Markov Chain
 Markov chain is a method that can be used to estimate future parameters or variables by considering and studying
the current parameters or variables [19]. Based on [10], [20], here is the process in Markov chain modeling.
1. Define the state.
The state 𝑖 of a discrete time Markov chain is observed after each transition, where the possible states are
𝑖 = 0, 1, … , 𝑀 [10].
2. Construct the transition probability matrix.
A matrix whose elements are the transition probability values from one state to another state, or to the same
state within a certain system, is called a transition probability matrix. The 𝑟-step transition probability can be
expressed in matrix form as
𝑃(𝑟) =
(

𝑝00 (𝑟) 𝑝01 (𝑟)
𝑝10 (𝑟)
⋮
𝑝𝑀0 (𝑟)
𝑝11 (𝑟)
⋮
𝑝𝑀1 (𝑟)

⋯ 𝑝0𝑀 (𝑟)
⋯
⋯
⋯
𝑝1𝑀 (𝑟)
⋮
𝑝𝑀𝑀 (𝑟) )

3. Determining the steady state probability.
The steady state probability is defined as lim
𝑛→∞
𝑝𝑐𝑑 (𝑟) = 𝜋𝑑 > 0, where 𝜋𝑑 uniquely satisfy the following steady
state equations [10].
 𝜋𝑑 = ∑ 𝜋𝑐𝑝𝑐𝑑
𝑀
𝑐=0

(3)
for 𝑑 = 0, 1, . . . , 𝑀 and ∑ 𝜋𝑑 𝑀 𝑑=0 = 1. The 𝜋𝑑 is called the steady state probability of the Markov chain. If ( 3) is
expressed in matrix form, then the equation can be expressed as
𝜋 = 𝜋𝑃(𝑟)
where  𝜋 = (𝜋0, 𝜋1, … , 𝜋𝑀).

2.6. Research Flow Diagram

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

71

Figure 1. Research Flow Diagram
3. Results and discussions
3.1. Research Sample
 The number of respondents in the preliminary questionnaire was assumed to be close to the normal distribution
based on the central limit theorem that a normal approximation to the sample mean will generally be good if 𝑛 ≥ 30
[21]. So, the preliminary questionnaire obtained 108 respondents who used the marketplace and 2 respondents that
did not use the marketplace. The sample calculation of research questionnaires on Universitas Negeri Semarang using
the Slovin method is as follows.
𝑛 =
52.352
1+(52.352)(0,1)2 =
52.352
524,52 = 99,80935
Form this calculation, the sample of active students of Universitas Negeri Semarang was 100 respondents. While the
sample calculation for Institut Pesantren Mathali’ul Falah is as follows.
𝑛 =
1.730
1+(1.730)(0,1)2 =
52.352
18,3 = 94,53551913
Form this calculation, the sample of active students of Institut Pesantren Mathali’ul Falah was 100 respondents.  So,
the minimum total number of respondents of research questionnaire are 200 respondents. After obtaining the total
sample for each college, the number of samples for each faculty was determined by proportional calculation.  In this
study, 250 respondents filled out the research questionnaire who were active students of Universitas Negeri Semarang
and Institut Pesantren Mathali’ul Falah.

3.2. Validity and Reliability Test
In this study, validity and reliability tests were carried out on preliminary questionnaires and research
questionnaires that had been filled out by respondents. The data in the preliminary questionnaire used a likert scale

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

72
while the data in the research questionnaire used a nominal scale. Data was tested for validity using Pearson
correlation. The formula of correlation Product Moment is as follows.
𝑟𝑣𝑤 =
𝑛(∑𝑉𝑊)−(∑𝑉)(∑𝑊)
√[𝑛(∑𝑉2)−(∑𝑉)2][𝑛(∑𝑊2)−(∑𝑊)2]
where 𝑟𝑣𝑤: correlation coefficient, 𝑛: number of samples, 𝑉: variable score of V (strategy), and 𝑊: variable score of W
(strategy). The data on the questionnaire is said to be valid if 𝑟ℎ𝑖𝑡𝑢𝑛𝑔 (𝑟𝑣𝑤) is greater than 𝑟𝑡𝑎𝑏𝑙𝑒 with a significance value
of 10% [22]. Then to test the reliability of data with a likert scale and a nominal scale, the Cronbach's Alpha technique
was used. Here is the formula.
𝑟𝑎𝑢 = [
𝑘
𝑘−1] [1 −
∑𝜎𝑏 2
𝜎𝑇 2 ]
where 𝑟𝑎𝑢: realibility coefficient, 𝑘: number of strategies, ∑𝜎𝑏 2: total variance of items (each strategy), and 𝜎𝑇 2: total
variance.
 The preliminary questionnaire was filled out by 108 respondents. As shown in Table 3, the validity test results for
each user preference factor in choosing a marketplace are valid.
Table 3. Validity of The Initial Data
Strategy/Atrributes r Value r Table Conclusion
Product Diversity 0,667 0,1591 Valid
Price 0,663 0,1591 Valid
Shipping Costs 0,643 0,1591 Valid
Discount Vouchers 0,613 0,1591 Valid
Feature
Completeness 0,624 0,1591 Valid
Payment Methods 0,722 0,1591 Valid
Product reviews 0,638 0,1591 Valid

The reliability test was conducted using Cronbach’s alpha. The reliability test result for the initial data is declared
reliable and has a value of Cronbach’s alpha value that fell into the hight reability because the value was between 0,70-
0,90 [23]. The reliability test results are shown in Table 4.
Table 4. Reliability of The Initial Data
Strategy/Atrributes 𝜶 Conclusion
Product Diversity 0,734 Reliable
Price 0,735 Reliable
Shipping Costs 0,744 Reliable
Discount Vouchers 0,747 Reliable
Feature Completeness 0,765 Reliable
Payment Methods 0,721 Reliable
Product reviews 0,742 Reliable
In addition, the research questionnaire was filled out by 250 respondents. The results of the validity and reliability
tests on the research questionnaire data also stated that the data were valid and reliable.

3.3. Game Theory Solution
3.3.1. Pure Strategy
The solution using a pure strategy is carried out by finding the smallest (minimum) value in each row and the
largest (maximum) value in each column. Then the smallest value from each row is taken as the maximum value
(maximin) and the largest value from each column is taken as the minimum value (minimax) [10], [11].

Table 5. Solution of Pure Strategy of Shopee and Tiktok Shop (Tokopedia)
Tiktok Shop (Tokopedia) Maximin
Shopee
 𝑌1 𝑌2 𝑌3 𝑌4 𝑌5 𝑌6 𝑌7
𝑋1 112 -12 26 -12 104 80 20 -12
𝑋2 84 48 18 -22 108 106 36 -22
𝑋3 66 42 78 -4 90 86 36 -4
𝑋4 94 86 90 82 100 96 70 70
𝑋5 36 -6 24 -20 106 84 34 -20
𝑋6 44 12 8 -2 62 76 26 -2

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

73
𝑋7 42 24 58 -16 78 86 74 -16
Minimax 112 86 90 82 108 106 74
The steady state is not obtained in the pure strategy of Shopee and Tiktok Shop (Tokopedia) competition. So,
based on [11], the solution of this competition is continued with a mixed strategy.

Table 6. Solution of Pure Strategy of Tiktok Shop (Tokopedia) and Lazada
Lazada
Maximin
Tiktok Shop (Tokopedia)
 𝑍1 𝑍2 𝑍3 𝑍4 𝑍5 𝑍6 𝑍7
𝑌1 126 56 90 60 144 122 106 56
𝑌2 112 96 110 58 152 132 120 58
𝑌3 108 70 98 48 108 128 94 48
𝑌4 122 98 128 84 132 126 108 84
𝑌5 78 36 88 48 104 104 76 36
𝑌6 74 46 90 48 82 126 88 46
𝑌7 108 74 96 72 114 134 128 72
Minimax 126 98 128 84 152 134 128

The saddle point in the competition between Tiktok Shop (Tokopedia) and Lazada is 84.

Table 7. Solution of Pure Strategy of Shopee and Lazada
Lazada
Maximin
Shopee
 𝑍1 𝑍2 𝑍3 𝑍4 𝑍5 𝑍6 𝑍7
𝑋1 154 92 126 98 164 140 134 92
𝑋2 154 148 154 110 144 152 132 110
𝑋3 140 112 120 98 146 142 124 98
𝑋4 168 130 158 142 164 148 164 130
𝑋5 136 90 118 84 162 142 150 84
𝑋6 116 94 102 90 136 162 138 90
𝑋7 144 106 136 100 146 150 166 100
Minimax 168 148 158 142 164 162 166
The steady state is not obtained in the pure strategy of Shopee and Lazada competition. So, the solution of
this competition is continued with a mixed strategy [11].

3.3.2. Mixed Strategy
The solution using a mixed strategy is carried out by principle of dominance  [18]. If a row dominates another
row or a column dominates another column, then the dominated row and column are eliminated  [10]. Then
determine the maximin and minimax values with pure strategy.
The reduction for Shopee and Tiktok Shop (Tokopedia)  competition is reducing rows 𝑋2, 𝑋3, 𝑋6, 𝑋1, 𝑋5 and
reducing columns 𝑌1, 𝑌2, 𝑌3, 𝑌5, and 𝑌6. Then, the pay-off matrix after row and column elimination is as follows.
Table 8. Solution of Mixed Strategy of Shopee and Tiktok Shop (Tokopedia)
Tiktok Shop (Tokopedia)
Maximin
Shop
ee  𝑌4 𝑌7
𝑋4 82 70 70

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

74
𝑋7 -16 74 -16
Minimax 82 74
Since the saddle point has not been obtained, the competition between Shopee and Tiktok Shop (Tokopedia) can’t
be solved with a dominance strategy. Therefore, according to [10], the game theory solution is continued with the
linear program simplex method.
The reduction for Shopee and Lazada competition is reducing rows 𝑋1, 𝑋3, 𝑋5, 𝑋6, 𝑋7 and reducing columns 𝑍1,
𝑍3, 𝑍6, dan 𝑍7.
Table 9. Solution of Mixed Strategy of Shopee and Lazada
Lazada
Maximin
Shopee  𝑍2 𝑍4
𝑋2 148 110 110
𝑋4 130 142 130
Minimax 148 142
Since the saddle point has not been obtained, the competition between Shopee and Lazada can’t be solved with a
dominance strategy. Therefore, according to [10], the game theory solution is continued with the linear program
simplex method.
.
3.3.3. Linear Program
The first step in solving game theory using a linear program is to modify the pay -off matrix. The elements of
the pay-off matrix must be non-negative numbers [10]. Therefore, the previous pay-off matrix that contains negative
numbers must be modified by adding the smallest negative element with a constant 𝑘 [10].
1. Shopee and Tiktok Shop (Tokopedia) competition
a. Row Player (Shopee)
 Since in the pay off matrix of Shopee and Tiktok Shop (Tokopedia) competition there is a negative
number -22, then the elements in the pay -off matrix must be added with a constant 𝑘 = 22. Then the
results of solving the linear program on row player using the POM-QM application are as follows.
Table 10. Optimal Solution of Shopee as a Row Player
Minimize 𝑋1 𝑋2 𝑋3 𝑋4 𝑋5 𝑋6 𝑋7  RHS Dual
1 1 1 1 1 1 1
Constraint 1 134 106 88 116 58 66 64 ≥ 1 0
Constraint 2 10 70 64 108 16 34 46 ≥ 1 0
Constraint 3 48 40 100 112 46 30 80 ≥ 1 0
Constraint 4 10 0 18 104 2 20 6 ≥ 1 -0,0004
Constraint 5 126 130 112 122 128 84 100 ≥ 1 0
Constraint 6 102 128 108 118 106 98 108 ≥ 1 0
Constraint 7 42 58 58 92 56 48 96 ≥ 1 -0,0104
Solution 0 0 0 0,0095 0 0 0,0013  0,0108
 Based on the results of the simplex method, to get the game value of the competition between Shopee
and Tiktok Shop (Tokopedia), the following calculations are carried out.
𝑓0 =
1
𝑉 = 0,0108
𝑉 =
1
𝑓0
=
1
0,0108 = 92,59
𝑥4 = 0,0095 × 92,59 = 0,88
𝑥7 = 0,0013 × 92,59 = 0,12
Then 𝑉 is minus by constant of  𝑘 added during the modification of the  pay-off which is 𝑘 = 22. So, the
value of is 𝑉 = 92,59 − 22 = 70,59. Since the value of 𝑥4 = 0.88 and 𝑥7 = 0.12, the optimal strategy of the
Shopee are discount voucher and product review strategies. So , the games value of the row player is
70,59 with strategies 4 and 7, which are discount vouchers (0,88) and product reviews (0,12).

b. Column Player (Tiktok Shop and Tokopedia)
The results of solving the linear program on column player using the POM-QM application are as follows.
Table 11. Optimal Solution of Tiktok Shop (Tokopedia) as a Column Player
Maximize 𝑌1 𝑌2 𝑌3 𝑌4 𝑌5 𝑌6 𝑌7  RHS Dual 1 1 1 1 1 1 1

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

75
Constraint 1 134 10 48 10 126 102 42 ≤ 1 0
Constraint 2 106 70 40 0 130 128 58 ≤ 1 0
Constraint 3 88 64 100 18 112 108 58 ≤ 1 0
Constraint 4 116 108 112 104 122 118 92 ≤ 1 0,0095
Constraint 5 58 16 46 2 128 106 56 ≤ 1 0
Constraint 6 66 34 30 20 84 98 48 ≤ 1 0
Constraint 7 64 46 80 6 100 108 96 ≤ 1 0,0013
Solution 0 0 0 0,0004 0 0 0,0104  0,0108
Based on the results of the simplex method, to get the game value of the competition between Shopee
and Tiktok Shop (Tokopedia), the following calculations are carried out.
𝑔0 =
1
𝑉 = 0,0108
𝑉 =
1
𝑔0
=
1
0,0108 = 92,59
𝑦4 = 0,0004 × 92,59 = 0,037
𝑦7 = 0,0104 × 92,59 = 0,96
Then 𝑉 is minus by constant of  𝑘 added during the modification of the  pay-off which is 𝑘 = 22. So, the
value of is 𝑉 = 92,59 − 22 = 70,59. Since the value of 𝑦4 = 0.037 and 𝑦7 = 0.96, the optimal strategy of
the Tiktok Shop (Tokopedia) are discount voucher and product review strategies. So, the games value of
the column player is 70,59 with strategies 4 and 7, which are discount vouchers (0,37) and product reviews
(0,96).

2. Shopee and Lazada competition.
a. Row Player (Shopee)
 The results of solving the linear program on row player using the POM-QM application are as follows.
Table 12. Optimal Solution of Shopee as a Row Player
Minimize 𝑋1 𝑋2 𝑋3 𝑋4 𝑋5 𝑋6 𝑋7  RHS Dual
1 1 1 1 1 1 1
Constraint 1 154 154 140 168 136 116 144 ≥ 1 0
Constraint 2 92 148 112 130 90 94 106 ≥ 1 -0,0048
Constraint 3 126 154 120 158 118 102 136 ≥ 1 0
Constraint 4 98 110 98 142 84 90 100 ≥ 1 -0,0027
Constraint 5 164 144 146 164 162 136 146 ≥ 1 0
Constraint 6 140 152 142 148 142 162 150 ≥ 1 0
Constraint 7 134 132 124 164 150 138 166 ≥ 1 0
Solution 0 0,0018 0 0,0057 0 0 0  0,0074
Based on the results of the simplex method, to get the game value of the competition between Shopee
and Lazada, the following calculations are carried out.
𝑓0 =
1
𝑉 = 0,0074
𝑉 =
1
𝑓0
=
1
0,0074 = 135,14
𝑥2 = 0,0018 × 135,14 = 0,24
𝑥4 = 0,0057 × 135,14 = 0,77
 Since the value of 𝑥2 = 0,24 and 𝑥4 = 0,77, the optimal strategy of the Shopee are price and discount
voucher strategies. So , the games value of the row player is 135,14 with strategies 2 and 4, which are
price (0,24) and discount voucher (0,77).
b. Column Player (Lazada)
The results of solving the linear program on column player using the POM-QM application are as follows.
Table 13. Optimal Solution of Lazada as a Column Player
Maximize 𝑍1 𝑍2 𝑍3 𝑍4 𝑍5 𝑍6 𝑍7  RHS Dual
1 1 1 1 1 1 1
Constraint 1 154 92 126 98 164 140 134 ≤ 1 0
Constraint 2 154 148 154 110 144 152 132 ≤ 1 0,0018
Constraint 3 140 112 120 98 146 142 124 ≤ 1 0
Constraint 4 168 130 158 142 164 148 164 ≤ 1 0,0057
Constraint 5 136 90 118 84 162 142 150 ≤ 1 0

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

76
Constraint 6 116 94 102 90 136 162 138 ≤ 1 0
Constraint 7 144 106 136 100 146 150 166 ≤ 1 0
Solution 0 0,0048 0 0,0027 0 0 0  0,0074
𝑔0 =
1
𝑉 = 0,0074
𝑉 =
1
𝑔0
=
1
0,0074 = 135,14
𝑧2 = 0,0048 × 135,14 = 0,65
𝑧4 = 0,0027 × 135,14 = 0,36
 Since the value of 𝑧2 = 0,65 and 𝑧4 = 0,36, the optimal strategy of the Lazada are price and discount
voucher strategies. So, the games value of the column player is 135,14 with strategies 2 and 4, which are
price (0,65) and discount voucher (0,36).

3.4. Markov Chain Solution
1. Define the state.
 The state in this research is the marketplaces. From the results of the preliminary questionnaire, the top three
marketplaces are Shopee, Tiktok Shop (Tokopedia), and Lazada.
Table 14. State Marketplace
State i Marketplace Brand
State 0 Shopee
State 1 Tiktok Shop and Tokopedia
State 2 Lazada

2. Transition probability matrix
 Based on the results of the research questionnaire that has been distributed to 250 respondents, the table
below is a recapitulation of the values obtained.
Table 15. Markov Chain Data Recapitulation
 Shopee Tiktok Shop and Tokopedia Lazada Total Users
Shopee 26 150 32 208
Tiktok Shop
and Tokopedia 27 4 4 35
Lazada 7 0 0 7
Total 250
After the data recapitulation from the Markov chain is obtained, the data is made into a transition probability
matrix, by dividing each item by the number of users. The transition probability matrix is as follows.
Table 16. Transition Probability Matrix
 Shopee Tiktok Shop and Tokopedia Lazada Total
Shopee 0,1250 0,7212 0,1538 1
Tiktok Shop and Tokopedia 0,7714 0,1143 0,1143 1
Lazada 1 0 0 1
3. Steady state probability
The next step is to determine the steady state probability in a transition probability matrix.
(𝜋0 𝜋1 𝜋2) = (𝜋0 𝜋1 𝜋2) (
0,1250 0,7212 0,1538
0,7714 0,1143 0,1143
1 0 0
)
then,
𝜋0 = 0,125𝜋0 + 0,7714𝜋1 + 𝜋2 ⇔ 0,8750𝜋0 − 0,7714𝜋1 − 𝜋2 = 0
𝜋1 = 0,7212𝜋0 + 0,1143𝜋1 ⇔ −0,7212𝜋0 + 0,8857𝜋1 = 0
𝜋2 = 0,1538𝜋0 + 0,1143𝜋1 ⇔ −0,1538𝜋0 − 0,1143𝜋1 + 𝜋2 = 0
and
𝜋0 + 𝜋1 + 𝜋2 = 1
then we have the following equation
0,8750𝜋0 − 0,7714𝜋1 − 𝜋2 = 0 (4)
−0,7212𝜋0 + 0,8857𝜋1 = 0 (5)
−0,1538𝜋0 − 0,1143𝜋1 + 𝜋2 = 0 (6)
𝜋0 + 𝜋1 + 𝜋2 = 1 (7)

To obtain the steady state probability, the (4), (5), and (6) equation can be expressed as

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

77
(𝜋0 𝜋1 𝜋2) (
0,875 −0,7212 −0,1538
0,7714 0,8857 −0,1143
−1 0 1
) = (0 0 0).
Since the matrix multiplication is equal to zero matrix, so, the (4) equation is replaced by (7). Then,
(𝜋0 𝜋1 𝜋2) (
1 −0,7212 −0,1538
1 0,8857 −0,1143
1 0 1
) = (1 0 0)
⇔ (𝜋0 𝜋1 𝜋2) = (1 0 0) (
1 −0,7212 −0,1538
1 0,8857 −0,1143
1 0 1
)
−1

⇔ (𝜋0 𝜋1 𝜋2) = (1 0 0) (
0,4852 0,3951 0,1198
−0,6104 0,6320 −0,0216
−0,4852 −0,3951 0,8802
)
⇔ (𝜋0 𝜋1 𝜋2) = (0,4852 0,3951 0,1198)
Thus, the steady state probability is
Table 17. Steady State Probability
Variable Marketplace Steady State Probability
𝜋0 Shopee 0,4852
𝜋1 Tiktok Shop and Tokopedia 0,3951
𝜋2 Lazada 0,1198
The steady state probabilities can also be generated from transition probabilities over a period of time. A
probability is said to reach a steady state if the transition probability produces the same value continuously. The
calculation of the transition probability using POM-QM is obtained as follows.
Table 18. Transition Probability at Time Period
Period Shopee Tiktok Shop and Tokopedia Lazada
1 0,24 0,616 0,144
2 0,6492 0,2435 0,1073
3 0,3763 0,496 0,1277
4 0,5574 0,3281 0,1146
5 0,4373 0,4394 0,1232
6 0,5169 0,3656 0,1175
7 0,4641 0,4145 0,1213
⋮ ⋮ ⋮ ⋮
20 0,4853 0,3949 0,1198
21 0,4851 0,3951 0,1198
22 0,4852 0,395 0,1198
23 0,4852 0,395 0,1198
24 0,4852 0,395 0,1198
Based on table 18, it can be seen that one year ahead after the current period, Shopee has decreased users
quite drastically, from 83 ,2% to 24%. Entering the 2nd period, Shopee users began to increase again to 64%,
then decreased again in the 3rd period. The number of Shopee users from period to period is unstable because
it increases and decreases alternately every period until period 2 1. However, in the 22nd period onwards, the
number of Shopee users began to stabilize at a value of 48 ,52%. Meanwhile, Tiktok Shop (Tokopedia ) has
increased to 61 ,6% where these users are users who initially chose Tiktok Shop (Tokopedia) and users from
other marketplaces who switch to the Tiktok Shop (Tokopedia).  However, after the 1st period, Tiktok Shop
(Tokopedia) decreased drastically to 24,32%. Then it increased again in the 3rd period, but the number of users
decreased again in the 4th period. The number of Tiktok Shop (Tokopedia) users from period to period is unstable
because it increases and decreases alternately every period. However, in the 22nd period onwards, the number
of Tiktok Shop (Tokopedia) users began to stabilize at a value of 39,5%.  In contrasted with Lazada, the number
of Lazada users is relatively stable at 11%. In the 22nd period onwards, the number of Lazada users reached a
steady state of 11,98%. Therefore, it can be concluded that the transition probability reaches a steady state during
the 22nd period where 48,52% of users (loyal users and users switching from other marketplaces) will use Shopee
as the main marketplace, 39,5% use Tiktok Shop and Tokopedia, and 11,98% use Lazada.

3.5. Consumer Behavior Analysis
Datasets that have been processed in data cleaning and data preparation through Google Colab, then visualized
in a dashboard through Looker Studio. The following is the visualization dashboard.

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

78

Figure 2. Marketing Perfomance Dashboard
The dashboard can be accessed through  https://lookerstudio.google.com/reporting/0f845b81-edc7-4541-bf0d-
64158e51473f.
 Based on the dashboard, analysis of consumer behavior among active students of Universitas Negeri Semarang
and students of Institut Pesantren Mathali’ul Falah revealed that out of a total of 250 respondents, only 12.5% of users
continued using Shopee and 11.4% continued using Tiktok Shop and Tokopedia. As many as 72.1% of Shopee users
switched to Tiktok Shop (Tokopedia), 77.1% of Tiktok Shop (Tokopedia) users switched to Shopee, 11.4% of Tiktok
Shop (Tokopedia) users switched to Lazada, 15.4% of Shopee users switched to Lazada, and 100% of Lazada users
switched to Shopee.  Here, a fairly unique incident occurs where it is possible to exchange users between these

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

79
marketplaces. From the dashboard, we can also know that the strategy most chosen by users before making a
purchase decision on the three marketplaces is a discount voucher.  So, the possibility of switching brands by users
can occur because the dominant strategy of the three marketplaces is the same. If a marketplace has problems or a
decline in its superior strategy, then users may move to other marketplaces that offer the same strategy.  From the
previous Markov chain results, it was found that in the first  period, the number of Tiktok Shop (Tokopedia) users
increased drastically from 14% to 61.6% because many Shopee users switched to Tiktok Shop (Tokopedia). This
happens because the strategies most chosen by users from both marketplaces are relatively the s ame, such as
excelling in discount voucher strategies, pricing, and product reviews. So, if one of the marketplaces encounters an
issue, users will easily switch to the other marketplace. Therefore, both marketplaces must compete with each other
on those s trategies to maintain their existence. So, each marketplace must maintain the strategy that becomes its
advantage according to calculations using game theory.

4. Conclusion
Based on the research results obtained, it can be concluded that Shopee's optimal strategies are discount
vouchers (0,88) and product reviews (0,12). Tiktok Shop (Tokopedia)'s optimal strategy is discount vouchers (0,037)
and product reviews (0,96). The game value generated by both is 70,59. Then the optimal strategy of Tiktok Shop
(Tokopedia) and Lazada is price. The game value in their competition is 84. In Shopee and Lazada competition,
Shopee's optimal strategy is price (0, 24) and discount vouchers (0,77). Lazada's optimal strategy is price (0,65) and
discount voucher (0,36). The game value generated by both is 135,14. The percentage of marketplace user loyalty
based on calculations using Markov chain obtained that the perce ntage of Shopee's transition probability is 48,52%,
Tiktok Shop and Tokopedia is 39,5%, and Lazada is 11,98%. Analysis of consumer behavior among active students
of Universitas Negeri Semarang and students of Institut Pesantren Mathali’ul Falah revealed that there is a possibility
of switching users from one marketplace to another. If the initial marketplace used has problems or a decrease in its
superior strategy, then there is a possibility that users move from one marketplace to another because the three
marketplaces have relatively the same superior strategy, which is a  discount voucher strategy. So, if one of the
marketplaces encounters an issue, users will easily switch to the other marketplace. Therefore, the marketplaces must
compete with each other on those strategies to maintain their existence. Each marketplace must maintain the strategy
that becomes its advantage according to calculations using game theory.

References
[1] We Are Social, “Digital 2025.” [Online]. Available: https://wearesocial.com/id/blog/2025/02/digital-2025/
[2] SimilarWeb, “Marketplace in Indonesia.” [Online]. Available: https://www.similarweb.com/top-websites/indonesia/e-
commerce-and-shopping/marketplace/
[3] N. K. Putri, “TikTok Shop Resmi Kembali Buka, Kerja Sama dengan Tokopedia,” Liputan6, 2023. [Online].
Available: https://www.liputan6.com/regional/read/5478012/tiktok -shop-resmi-kembali-buka-kerja-sama-dengan-
tokopedia?page=3
[4] V. D. Ramadhanty, A. P. Subriadi, and V. Lukitosari, “Optimal Marketing Strategy of Private Tutoring: An Application
of Game Theory,” Procedia Comput. Sci., vol. 234, pp. 946–953, 2024, doi: 10.1016/j.procs.2024.03.083.
[5] N. Z. Rizkita, Sutanto, and N. A. Kurdhi, “Game Theory and Markov Chain Analysis of the Displacement of Shopping
Mall Visitors in Surakarta City,” Barekeng, vol. 19, no. 2, pp. 1047 –1056, 2025, doi:
10.30598/barekengvol19iss2pp1047-1056.
[6] R. Amelia, H. Wijayanti, and M. Widyastiti, “Analisis Strategi Pemasaran Dalam Persaingan Perusahaan
Marketplace antara Tokopedia, Shopee, dan Lazada Menggunakan Game Theory,” Interval J. Ilm. Mat., vol. 3, no.
1, pp. 1–14, 2023.
[7] N. F. Y. Sitio and Zahedi, “Penentuan Strategi Pemasaran Optimum dengan Teori Permainan pada Marketplace (
Studi Kasus : Persaingan Shopee dan Lazada ),” Mat. dan Pendidik. Mat., vol. 6, pp. 50–57, 2023.
[8] D. Y. Putra and D. Ahmad, “Strategi Kompetisi Antara Tokopedia Dan Shopee Menggunakan Teori Permainan,” J.
Math., vol. 6, no. 3, pp. 85–90, 2021.
[9] A. N. Azizah and R. P. Sari, “Analisis Brand Switching dan Penentuan Strategi Pemasaran Produk Bubble Tea
Menggunakan Metode Markov Chain dan Game Theory,” J. Optim., vol. 7, pp. 25–34, 2021.
[10] F. S. Hillier and G. J. Lieberman, Introduction to Operations Research, Eleventh., vol. 153. McGraw-Hill Education,
2021.

  Laila & Albar/UNNES Journal of Mathematics 15(1) (2026)

80
[11] H. A. Taha, Operation Research an Introduction, Tenth. Pearson Education, 2017.
[12] R. I. Halim and P. Sitompul, “Analisis Brand Switching dan Strategi Pemasaran Menggunakan Markov Chain dan
Game Theory di Kota Medan,” J. Ris. Rumpun Mat. Dan Ilmu Pengetah. Alam , vol. 3, no. 1, pp. 412 –423, 2024,
doi: 10.55606/jurrimipa.v3i1.2548.
[13] N. A. B. Sinulingga and H. T. Sihotang, Perilaku Konsumen Strategi dan Teori. IOCS Publisher, 2021.
[14] D. I. Jusuf, Perilaku Konsumen di masa bisnis online. Penerbit Andi, 2021.
[15] W. L. Winston, Operations research. 2004.
[16] A. E. Cahyani and Y. P. Astuti, “Analisis Strategi Persaingan Layanan Jasa Pesan -Antar Makanan Menggunakan
Game Theory (Studi Kasus Persaingan Shopeefood Dan Gofood),” MATHunesa J. Ilm. Mat. , vol. 10, no. 1, pp.
190–198, 2022, doi: 10.26740/mathunesa.v10n1.p190-198.
[17] A. Saifuddin, N. K. T. Tastrawati, and K. Sari, “Penerapan Konsep Teori Permainan (Game Theory) dalam
Pemilihan Strategi Kampanye Politik (Studi Kasus: Strategi Pemenangan Pemilukada DKI Jakarta Tahun 2017),”
E-Jurnal Mat., vol. 7, no. 2, p. 173, 2018, doi: 10.24843/mtk.2018.v07.i02.p200.
[18] P. Affandi, Buku Ajar Riset Operasi. CV IRDH, 2019.
[19] F. A. Kurniawan, “Aplikasi markov chain untuk memprediksi tekanan darah,” InComTech J. Telekomun. dan
Komput., vol. 8, no. 2, pp. 103–120, 2018, doi: 10.22441/incomtech.v8i2.4087.
[20] Oktaviyani, Dwijanto, and Supriyono, “Optimasi Penjadwalan Produksi Dan Perencanaan Bahan Baku
Menggunakan Rantai Markov (Studi Kasus Kinken Cake & Bakery Kutoarjo),” UNNES J. Math., vol. VII, no. 2, pp.
165–180, 2018.
[21] R. E. Walpole, R. H. Myers, S. L. Myers, and K. Ye, Probability & Statistics for Engineers & Scientist , Ninth. New
York: Macmillan, 2015.
[22] H. Taherdoost, “Validity and Reliability of the Research Instrument; How to Test the Validation of a
Questionnaire/Survey in a Research,” SSRN Electron. J., vol. 5, no. 3, pp. 28–36, 2018, doi: 10.2139/ssrn.3205040.
[23] P. R. Hinton, Statistics Explained, 2nd ed. Routledge, 2005. doi: 10.1088/1751-8113/44/8/085201.
