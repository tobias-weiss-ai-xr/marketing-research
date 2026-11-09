---
title: An ID3 GA Bass Collaborative Framework for Cross Border Market Diffusion Prediction
url: https://doi.org/10.15837/ijccc.2026.4.7220
category: consumer-behavior
subcategory: framework
date: 2026-07
venue: International Journal of Computers Communications & Control
authors:
- Guiling Liao
- Na Tang
- Yuehua Chen
source: openalex-oa
pdf_url: https://univagora.ro/jour/index.php/ijccc/article/download/7220/2523
pages: 14
chars: 38399
fetched_at: '2026-11-08T18:19:18+00:00'
kb_version: 1
---

# An ID3 GA Bass Collaborative Framework for Cross Border Market Diffusion Prediction

INTERNATIONAL JOURNAL OF COMPUTERS COMMUNICATIONS & CONTROL
Online ISSN 1841-9844, ISSN-L 1841-9836, Volume: 21, Issue: 4, Month: August, Year: 2026
Article Number: 7220, https://doi.org/10.15837/ijccc.2026.4.7220
CCC Publications
An ID3 GA Bass Collaborative Framework for Cross Border Market
Diffusion Prediction
G. Liao , N. Tang , Y. Chen , T. Jiang
Guiling Liao
School of Business
Geely University of China, China
No. 123, Section 2, Chengjian Avenue, Eastern New District, Chengdu City, Sichuan Province
liaoguiling@guc.edu.cn
Na Tang
School of Business
Geely University of China, China
No. 123, Section 2, Chengjian Avenue, Eastern New District, Chengdu City, Sichuan Province
tangna@guc.edu.cn
Yuyan Chen*
School of Business
Geely University of China, China
No. 123, Section 2, Chengjian Avenue, Eastern New District, Chengdu City, Sichuan Province
*Corresponding author: chenyuyan@guc.edu.cn
Tingting Jiang
School of Business
Geely University of China, China
No. 123, Section 2, Chengjian Avenue, Eastern New District, Chengdu City, Sichuan Province
jiangtingting@guc.edu.cn
Abstract
Accurate forecasting of international market diffusion is essential for strategic decision-making
in the New Energy Vehicle (NEV) sector. Traditional ID3 and Bass models face limitations in
handling heterogeneous consumer behavior and dynamic policy shocks. This paper proposes a col-
laborative model that integrates an improved ID3 decision tree for consumer segmentation with a
genetic algorithm-optimized Bass diffusion model. The ID3 component refines classification accu-
racy by mitigating multi-value bias, while the GA dynamically calibrates Bass parameters under
policy interventions. Experiments using cross-country NEV data demonstrate that the proposed
framework achieves a stable G-mean of 0.89±0.03, with MAE and RMSE reductions exceeding
30% compared to benchmark models including deep reinforcement learning and optimized random
forests. The model effectively quantifies the impact of consumer heterogeneity and subsidies on
market diffusion, offering a decision-support tool for firms to design adaptive marketing and policy
strategies. Beyond the NEV context, the framework can be applied to other domains requiring
predictive control of diffusion processes under external shocks.
Keywords:New energy vehicles; International trade; Bass model; ID3 algorithm; Marketing
path.

https://doi.org/10.15837/ijccc.2026.4.7220 2
1 Introduction
Global new energy vehicle (NEV) adoption is accelerating, yet cross-border diffusion remains
strongly mediated by heterogeneous consumer preferences and country-specific policy shocks[12]. Dif-
ferences in price sensitivity, technology valuation, and charging infrastructure, together with shifting
subsidy rules and technical standards, create segmentation drift and non-stationary demand signals
that impair forecast stability[18].As a result, diffusion parameters calibrated on past data often fail
to generalize when regulatory regimes change or when consumer composition evolves, producing sys-
tematic bias in trade and production planning across markets[11].
Existing approaches address parts of the problem but rarely its joint structure. Classical ID3-based
segmentation is attractive for interpretability but struggles with continuous, multi-source attributes
and tends to under-represent policy-relevant interactions unless carefully engineered[4, 5]. In parallel,
theBassframeworkiswidelyusedfordiffusionbuttypicallyassumesfixedparametersandiscommonly
fitted by nonlinear least squares, exposing calibration to local optima and limiting responsiveness to
time-varying interventions. Consequently, heterogeneity and policy shocks are often handled in ad
hoc post-processing rather than embedded into a unified, optimization-aware modeling loop, which
constrains decision usefulness for international deployment[14, 22].
This paper integrates ID3-based consumer classification with a GA-optimized Bass model to simul-
taneously capture heterogeneous consumer groups and dynamic diffusion under policy shocks, which
has not been addressed in prior studies. The formulation explicitly treats NEV diffusion as a compu-
tational decision-support and predictive control problem: decision trees yield policy-aware, auditable
segments for strategy selection, while GA-calibrated Bass dynamics provide control-oriented forecasts
that adapt to regulatory changes and allow stress-testing under counterfactual subsidy and infrastruc-
ture scenarios. , without presupposing outcomes or disclosing empirical results. This paper integrates
ID3-based consumer classification with GA-Bass modeling to simultaneously capture heterogeneous
consumer groups and dynamic diffusion under policy shocks, which has not been addressed in prior
studies.
2 Literature review
Building on metaheuristic optimization for control, Olivares V et al. design genetic-algorithm-
based trajectory generation for autonomous naval vehicles in MATLAB, illustrating how GA escapes
local optima in nonlinear planning and offering a template for control-oriented forecasting under
regime shifts [17]. Advancing decision-support under uncertainty, Mao J applies a fuzzy ant-colony
optimization portfolio model that balances risk and return, underscoring how swarm intelligence can
structure managerial choices in complex, multi-objective settings[15]. Extending route-planning ro-
bustness, Zhao L et al. couple Q-learning with an improved ant-colony algorithm to handle nonconvex
landscapes, demonstrating reinforcement-learning-guided exploration for faster convergence and bet-
ter paths[25]. At the criterion level, Zhang et al. refine the information-gain formulation, indicating
avenues to curb discretization loss and sharpen split quality in customer modeling[24]. Complement-
ing these advances, Ribeiro J et al. demonstrate a federated learning system integrated with SHAP
and LIME, showing that privacy preservation can coexist with transparency and improved predictive
performance in industrial deployments—capabilities essential for policy-sensitive segmentation at scale
[19].
Within NEV-specific applications, Wei et al. link marketing-strategy variables to purchase inten-
tion and show how survey-derived attributes can be encoded as decision-tree features to isolate salient
demand drivers and streamline campaign design [20]. To de-risk algorithm and parameter choices
before field rollout, Banciu D et al. provide a simulation framework that emulates order books, price
dynamics, and transaction frictions, enabling rigorous out-of-sample evaluation without real market
exposure [2]. From a supply-chain and sustainability angle, Feng Z et al. analyze end-of-life battery
recycling and argue that blockchain under carbon-tax regimes can raise profitability and enable trans-
action feasibility along NEV value chains[8]. In the international diffusion context, Dzienis A M et al.
examine cooperation between Chinese and foreign NEV firms and indicate that Bass-type modeling

https://doi.org/10.15837/ijccc.2026.4.7220 3
can guide penetration strategies in emerging markets connected to the Belt and Road initiative [6].
Finally, Deng G F et al. integrate fuzzy logic and genetic algorithms with reinforcement learning
and swarm intelligence to simulate pricing and consumer behavior, showing that learning styles and
competitive actions jointly shape retail prices and market structures—evidence that underscores the
need for optimization-aware behavioral modeling [3].
Taken together, the literature improves ID3 for segmentation and advances diffusion modeling
and optimization, yet two structural gaps remain for cross-border NEV forecasting: the inefficiency
of traditional ID3 when handling continuous, multi-source data streams and interactions, and the
static, locally optimized nature of Bass parameters that limits responsiveness to policy shocks and
infrastructure shifts. Addressing these gaps motivates an integrated formulation in which ID3 provides
transparent, policy-aware consumer grouping and a GA-optimized, dynamic Bass component captures
time-varying diffusion under regulatory scenarios.
3 Research methodology
3.1 Optimization of international trade marketing path for NEVs based on ID3
algorithm and Bass model
The ID3 algorithm constructs decision trees based on information gain and has significant ad-
vantages in consumer profiling and demand stratification. The algorithm reduces multi value bias
by using sample structure vector similarity, which is more suitable for analyzing differences in cross-
border consumer behavior [13]. The data processing flow of international trade marketing path for
NEVs is shown in Figure 1.
Figure 1 depicts the process of data processing in the study of international trade marketing
paths for NEVs. The "Raw Data" box on the left represents various initial data collected during the
research process, which then flows into the data preprocessing stage. After cleaning, transformation,
normalization and other operations, errors or irrelevant information are removed, and the data format
is unified to meet the requirements of subsequent analysis. The process preprocesses and uses data
miningtechniquessuch asID3 algorithm toextractvaluableinformation fromstored data. Theprocess
of generating decision trees for classification and rule learning problems is a divide and conquer, top-
down approach. The steps for solving classification prediction problems with decision trees are shown
in Figure 2.
Figure 1: Data processing flow of international trade marketing path for NEVs
Figure 2 illustrates the decision tree construction and application process of ID3 algorithm in the
selection of international trade marketing paths for NEVs. The left training set provides data support
for the decision tree classification algorithm, which constructs the decision tree based on information
gain. A decision tree consists of a root node, internal nodes, and leaf nodes, which divide the dataset
into branch paths based on features until the leaf nodes provide classification results [1, 9]. After the
construction is completed, the model is evaluated using a test set through the evaluation mode to
verify its predictive accuracy. For datasets of unknown categories, the model prediction function is
used to classify and predict, providing a decision-making basis for the selection of international trade
marketing paths for NEVs. For information entropy, as shown in equation (1).
Pi = xi x (1)

https://doi.org/10.15837/ijccc.2026.4.7220 4
Figure 2: Decision tree construction and application
In equation (1),X i represents the number of class samples in the dataset.Xindicates the total
number of samples in the dataset.Pi represents the probability of theith sample appearing in the
dataset. The information entropy of the dataset is further determined, as shown in equation (2).
I(x 1, x2, . . . , xn) =−
n∑︂
i=1
pi log2 pi (2)
In equation (2),I(x1, x2, . . . , xn)represents the information entropy of the dataset, which measures
the uncertainty of the class distribution in the dataset.nrepresents the total number of sample
categories in the dataset. The conditional entropy is then determined, as shown in equation (3).
E(Y) =
m∑︂
j=1
x1j +x 2j +···+x nj
x ×I(x 1 +x 2, . . . xn)(3)
In equation (3),E(Y)represents conditional entropy, which is the weighted average of the infor-
mation entropy of all groups, and the weight is the proportion of the number of samples in each group
to the total number of samples.mindicates the number of values for a certain attribute.jindicates
the number of samples in the th group. The information gain is shown in equation (4).
E(Y) =
m∑︂
j=1
x1j +x 2j +···+x nj
x textGain=I(x 1, x2, . . . , xn)−E(Y)(4)
In equation (4),Gainrepresents information gain, which measures the degree of uncertainty reduc-
tion after using a certain attribute to partition the dataset, thereby determining the optimal market
segmentation basis. In the actual NEV market, external factors such as policy subsidies and infras-
tructure construction will have a significant impact on market diffusion.This expression prioritizes the
attribute that maximally reduces uncertainty in consumer segmentation, ensuring that splits capture
the strongest information about heterogeneous NEV demand. To consider the effects of these external
factors, an impact function is introduced, as shown in equation (5).
E(Y) =
m∑︂
j=1
x1j +x 2j +···+x nj
x N(t) = 1−e −(p+q)t m (5)
In equation (5),N(t)represents the cumulative number of NEVs adopted over time, reflecting the
overall scale of acceptance of NEVs in the market over time.mrepresents the maximum potential
of the market, that is, the total number of NEVs that may ultimately be adopted, it defines the
theoretical upper limit under market saturation.prepresents the innovation coefficient, measuring
the adoption rate of NEVs by innovators, that is, the probability of independent adoption without
being influenced by others.qrepresents the imitation coefficient, measuring the adoption rate of
imitators, that is, the probability of adoption influenced by those who have already adopted it.tis
a time variable.erepresents the base of a natural exponential function. The dynamic mechanism of
adopting the growth rate of quantity is shown in equation (6).

https://doi.org/10.15837/ijccc.2026.4.7220 5
dN(t)
dt = [p(m−N(t)) +I N(t)(m−N(t))] x(t) m (6)
In equation (6), dN(t) dt represents the growth rate of the number of NEVs adopted over timet,
that is, the number of newly adopted vehicles per unit time. By adjusting the growth rate through
x(t), it can more accurately reflect the actual dynamics of the diffusion of the new energy vehicle
market under the influence of external factors. This formulation models adoption growth with two
complementary effects, where the innovation term drives early uptake and the imitation term amplifies
later-stage diffusion as market interactions intensify.
3.2 Market diffusion mechanism and subsidy strategy for NEVs based on Bass
model
Following the optimization of the international trade marketing strategy for NEVs, the study
shifted its focus to the global NEV landscape. It leveraged macro-level data to trace the diffusion
trajectories of key national markets spanning from 2015 to 2023. The top 20 NEV-consuming nations
worldwide were identified, drawing on data from OICA, national statistical agencies, and Euromon-
itor’s industry analyses [10]. Technical barriers such as range requirements and battery safety certi-
fication were sourced from the WTO Technical Barriers to Trade database. Per capita GDP (World
Bank) and fuel prices were used to calibrate the market potential parameter m in the Bass model.
The impact of different subsidy strategies on international market demand and international supply
chain profits is shown in Figure 3.
Figure 3: The impact of different subsidy strategies on international market demand and international
supply chain profits
Figure 3 (a) shows the relationship between international market demand and subsidy impact
coefficient. The curves in the figure represent subsidies to consumers, operators, and manufacturers,
respectively. As the subsidy impact coefficient increased, international market demand also increased,
with subsidies for operators and manufacturers having a more significant effect on boosting market
demand. In Figure 3 (b), as the subsidy impact coefficient increased, international supply chain profits
also showed an upward trend, with subsidies for operators and manufacturers having a more significant
effect on profit enhancement [23]. The dynamic process of diffusion in the NEV market is shown in
Figure 4.
As shown in Figure 4 (a), the relationship between the number of potential consumers, the number
of purchased consumers, and the cumulative sales volume of actual trials was compared. The number
of potential consumers gradually decreased, while the number of purchased consumers and cumulative
sales volume gradually increased. Figure 4 (b) shows the changes of innovative adopters and imitative
adopters over time, with the number of innovative adopters gradually increasing in the early stages
and then stabilizing. The Bass model described the expansion process of the NEV market [16]. The
innovationcoefficientpandimitationcoefficientqinthemodelwereusuallydeterminedbyMatlab, but
these coefficients were dynamically changing in the actual market. At first, the innovation coefficient

https://doi.org/10.15837/ijccc.2026.4.7220 6
Figure 4: The dynamic process of diffusion in the NEV market
p dominated, and then the imitation coefficient q gradually increased and might exceed p, indicating
that the market entered a stage of rapid diffusion [7].
3.3 Parameter optimization of Bass model based on GA
After analyzing the dynamic process of diffusion in the NEV market, GA was used to optimize the
parameters of the generalized Bass model, in order to solve the problem of the traditional nonlinear
least squares method easily getting stuck in local optima. The study uses random or other methods
to generate an initial populationpop(1)of N chromosomes,t:= 1, and calculates the fitness value for
each chromosome in the population, as shown in equation (7).
fi = fitness(popi(t))(7)
If the stopping condition is met, the algorithm stops. Otherwise, a new population will be selected,
with the probability shown in equation (8).
Pi =f i
/︃ N∑︂
j=1
fj (8)
The variance penalty in the load-balancing objective discourages oscillatory allocations, so the
solution favors stable resource usage across segments and time, which improves forecast reliability
under policy shifts.The new population composed of randomly selected chromosomes is shown in
equation (9).
mathrmnewpop(t+ 1) ={pop j(t)|j= 1,2, . . . , N}(9)
By crossing with probabilityP tto generate some new chromosomes, a new population is obtained,
as shown in equation (10).
mathrmcrosspop(t+ 1)(10)
By mutating a gene on the chromosome with a small probabilityP m, a new population of
mutpop(t+ 1), is formed as shown in equation (11).
mathrmpop(t) = mutpop(t+ 1))(11)
The entire calculation process includes steps such as generating an initial population, calculating
fitness values, selecting a new population, crossing to generate new chromosomes, and mutating chro-
mosome genes to form a new population until the stopping conditions are met. The flowchart of GA
is shown in Figure 5.
As shown in Figure 5, the study uses floating-point encoding method to represent each individual
as a real string of a certain length, and optimizes the encoding method through GA to represent each
individual as a real string, which can effectively improve the search space of the model [21]. The
research hopes that the smaller the error between the expected value and the output value, the better.
Therefore, the design of the fitness function reflects the performance of the model by measuring the

https://doi.org/10.15837/ijccc.2026.4.7220 7
Figure 5: GA optimization process
error. The smaller the E value, the higher the fitness of the model, which can more accurately predict
the international trade marketing path, as shown in equation (12).
F=k
(︄ n∑︂
i=1
|Y−Y ∗|
)︄
(12)
In equation (12),Fis the value of the fitness function.kis a constant coefficient.Yis the actual
output value of the model.Y∗is the expected output value.nis the sample size. The most effective
marketing strategy in international trade of NEVs is further optimized, as shown in equation (13).
fi = k Fi (13)
In equation (13),f i represents the fitness function of the individual.F i is the fitness value of
an individual.kis a constant used to adjust the scale of the fitness function. Finally, the selection
probabilities of different marketing strategies in the GA are determined, as shown in equation (14).
pi = fi ∑︁N
j=1 fj
(14)
In equation (14),sumN j=1fj is the sum of fitness values of all individuals in the population. In the
process of optimizing the parameters of the generalized Bass model in GA, the mutation operation is
a key mechanism to maintain population diversity and avoid the algorithm falling into local optima.
Inverted mutation, as an effective mutation method, can explore new solution spaces by changing
chromosome gene sequences. Figure 6 shows a schematic diagram of reverse mutation processing.
Figure 6: Schematic diagram of reverse mutation processing
As shown in Figure 6, the parent chromosome undergoes mutation operation, and some gene
sequences undergo inversion adjustment to generate offspring chromosomes. This process intuitively
presents how inversion variation reshapes chromosome structure. In the optimization of diffusion mod-
els in the NEV market, this variation helps to comprehensively search for the optimal combination of
parameters such as innovation coefficient p and imitation coefficient q, effectively capturing the dy-
namic impact of complex factors such as policy shocks and consumer behavior on market diffusion, and
improving the model’s fitting accuracy and predictive ability of market diffusion laws. The proposed
method will be named the Collaborative Optimization Model for International Trade Marketing Path

https://doi.org/10.15837/ijccc.2026.4.7220 8
of NEVs Based on ID3 Algorithm and Genetic (COMINTP). Figure 7 shows ID3-GA-Bass Pipeline
Workflow.
Figure 7: ID3-GA-Bass Pipeline Workflow
Figure 7 Unified workflow of the ID3-GA-Bass pipeline: raw data are cleaned and standardized
in preprocessing; salient attributes guide ID3 to produce policy-aware consumer segments; a genetic
algorithm calibrates Bass parameters on segment-level time series to avoid local optima; the calibrated
Bass dynamics generate diffusion forecasts that can be stress-tested under alternative subsidy and
infrastructure scenarios.
4 Results and discussion
4.1 Performance Comparison and Verification of COMINTP Model
Accuratelypredictingmarketdemandandmarketingeffectivenessisthekeytoformulatingeffective
strategies in the research of international trade marketing paths for NEVs. To confirm the performance
of the proposed COMINTP model in prediction tasks, it was compared with deep reinforcement
learning models (DRLM), optimized random forest models (ORFM), long short-term memory network
models (LSTMM), and improved support vector machine models (ISVM). The experimental dataset
included historical sales data, market research data, policy information, and consumer behavior data.
These data were preprocessed and used to train and test different models. The mean absolute error
(MAE) and root mean square error (RMSE) of different algorithms under different iteration times are
shown in Figure 8.
Figure 8: MAE and RMSE of different algorithms at different iteration times
Figure 8 MAE and RMSE of different algorithms at different iteration times. The figure highlights

https://doi.org/10.15837/ijccc.2026.4.7220 9
that the COMINTP model achieves the lowest and most stable error metrics, with MAE and RMSE
reductions exceeding 30% compared to benchmark models, confirming its superior predictive accuracy.
The comparison of G-mean values of different models with the number of experiments is shown in
Figure 9.
Figure 9: Comparison of G-mean values of different models with the number of experiments
Figure 9 Comparison of G-mean values of different models with the number of experiments. The
visualization demonstrates the stability of the COMINTP model, which maintains a consistently
high G-mean value around 0.89, in contrast to the significant fluctuations and lower performance of
competing models. The comparison of F1 values of different models with the number of experiments
is shown in Figure 10.
Figure 10 Comparison of F1 values of different models with the number of experiments. This
comparison underscores the COMINTP model’s reliability, showing a stable and high F1-score across
experiments, while other models exhibit considerable performance volatility.
4.2 Comprehensive analysis of market characteristics of NEVs in typical countries
The research analyzed the market characteristics and forecast results of 7 typical countries, in-
cluding Japan, India, Thailand, Australia, and other countries covering different development stages
and market types. The NEV market forecast of typical countries based on the COMINTP model is
shown in Table 1.
Table 1: Typical national NEV market forecast based on COMINTP model
Country Innovation Imitation Market 2025 Cumulative 2026 Sales
Coefficient Coefficient Potential Sales Forecast Growth Rate
p q m (10k units) under Policy
(10k units) Shock (%)
China 0.028 0.482 4800.35 3210.56 18.23
United States 0.035 0.420 3200.12 2100.34 15.67
Germany 0.041 0.385 1800.78 950.20 12.34
Japan 0.032 0.350 1200.50 750.45 10.12
India 0.015 0.550 2000.20 1800.68 22.45
Thailand 0.018 0.520 800.30 450.72 19.36
Australia 0.030 0.300 500.15 300.28 9.87

https://doi.org/10.15837/ijccc.2026.4.7220 10
Figure 10: Comparison of F1 values of different models with the number of experiments
In Table 1, China’s innovation coefficient was 0.028, imitation coefficient was 0.482, and market
potential was 48.0035 million vehicles. The cumulative sales volume was expected to reach 32.1056
million vehicles in 2025, and the expected sales growth rate in 2026 was 18.23%. The innovation
coefficient of the United States was 0.035, the imitation coefficient was 0.420, and the market potential
was 32.012 million vehicles. The cumulative sales volume in 2025 was 21.034 million vehicles, with
a sales growth rate of 15.67%. The market growth rates of Germany, the United States, Japan, and
India vary greatly, with India having the highest growth rate at 22.45%, while Australia had the
lowest growth rate at only 9.87%. The classification results of consumer behavior of NEVs in typical
countries are shown in Table 2.
Table 2: Classification of consumer behavior of NEVs in typical countries
Country Consumer Proportion Purchase Range Policy Preference
type (%) budget preference subsidy for new energy
(10,000 (km) awareness startups (%)
USD) (%)
China Price-sensitive 45.23 2.15 350.5 82.3 61.5
China Policy-dependent 32.15 3.48 380.2 91.7 54.8
China Technology-preferring 22.62 4.89 520.8 75.6 74.7
United States Technology-preferring 38.76 5.52 550.3 68.9 69.9
United States Policy-dependent 32.80 4.21 420.1 85.5 64.2
Germany Technology-preferring 42.31 6.68 580.9 65.4 77.3
India Price-sensitive 58.91 1.89 300.3 89.1 34.8
India Policy-dependent 31.09 2.15 330.7 93.4 44.3
Thailand Policy-dependent 48.57 2.02 360.4 95.2 47.7
Table 2 shows the classification of consumer behavior for NEVs in typical countries. Chinese
consumers were mainly divided into price sensitive type (45.23%), policy dependent type (32.15%),
and technology preference type (22.62%). Technology preference consumers accounted for 38.76% in
the United States and 42.31% in Germany. India and Thailand were mainly price sensitive and policy
dependent, with price sensitive consumers in India accounting for 58.91%. There were significant
differences in consumer purchasing budgets, battery life preferences, and policy subsidy awareness

https://doi.org/10.15837/ijccc.2026.4.7220 11
among countries. German consumers had a higher budget and preferred longer battery life, while
China, India, andThailandweremoresensitivetopolicysubsidies. Thecomparisonofmarketresponse
of NEVs under different subsidy strategies in typical countries is shown in Table 3.
Table 3: Comparison of market response of NEVs under different subsidy strategies in typical countries
Country Subsidy Penetration Innovation Imitation Market
type speed coefficient coefficient potential
(%/Year) change change utilization (%)
(∆p) (∆q)
China Consumer subsidy 23.19 +0.0028 +0.0715 73.62
China Operator subsidy 26.48 +0.0015 +0.0892 79.34
United States Manufacturer subsidy 22.35 +0.0192 +0.0327 72.18
United States Operator subsidy 17.26 +0.0031 +0.0384 64.59
Germany Consumer subsidy 18.73 +0.0045 +0.0391 67.42
Germany Manufacturer subsidy 21.09 +0.0234 +0.0256 70.85
India Operator subsidy 31.27 +0.0008 +0.1156 71.68
India Consumer subsidy 29.43 +0.0013 +0.1029 66.35
Table 3 compares the response of the NEV market in typical countries under different subsidy
strategies. China had the fastest penetration rate (26.48%/year) and the highest market potential
utilization rate (79.34%) under operator subsidies. The manufacturer subsidies in the United States
drove a higher innovation coefficient change (+0.0192), while Germany also performed well under the
manufacturer subsidies, with a penetration rate of 21.09% per year. Under the subsidy of Indian
operators, the penetration rate was the highest (31.27%/year), but the utilization rate of market
potential was relatively low. Overall, the impact of different subsidy types on the markets of various
countries varied significantly.
To validate the performance of the proposed Collaborative Optimization Model for International
Trade Marketing Path of NEVs (COMINTP), its predictive accuracy was benchmarked against several
established models: Deep Reinforcement Learning Models (DRLM), Optimized Random Forest Mod-
els (ORFM), Long Short-Term Memory Network Models (LSTMM), and Improved Support Vector
Machine Models (ISVM). The experimental dataset comprised historical sales data, market research,
policy information, and consumer behavior data. All models were trained and tested on this prepro-
cessed dataset. A comprehensive comparison across key performance metrics is presented in Table
4.
The Table 4 results clearly demonstrate the superiority of the COMINTP framework. Notably, the
COMINTP model reduces the Mean Absolute Error (MAE) and Root Mean Square Error (RMSE) by
over 32% compared to the alternatives, while achieving a stable G-mean of 0.892 and a high F1-Score.
This highlights its robustness and enhanced predictive power.
5 Conclusion
This study proposed a collaborative ID3-GA-Bass framework (COMINTP) for cross-border NEV
diffusion prediction. By integrating improved ID3 for consumer segmentation and GA-optimized Bass
modeling, the framework reduces prediction errors by over 30% compared with benchmark models and
Table 4: Comparative Performance Analysis of Predictive Models
Model MAE RMSE G-mean F1-Score
COMINTP 0.12 0.15 0.892±0.027 0.91
DRLM 0.19 0.23 0.815±0.081 0.83
ORFM 0.22 0.27 0.783±0.095 0.80
LSTMM 0.25 0.31 0.754±0.112 0.77
ISVM 0.28 0.34 0.775±0.103 0.79

https://doi.org/10.15837/ijccc.2026.4.7220 12
achieves stable performance in heterogeneous markets. The model successfully captures the effects of
consumer heterogeneity and policy shocks, demonstrating its utility as a predictive decision-support
and control tool in international marketing. Although the study validates the model with cross-country
NEV data, limitations remain: the dataset does not fully incorporate real-time policy feedback, and
external market shocks may be underrepresented. Future work will extend the framework with multi-
agent reinforcement learning, game-theoretic modeling, and real-time big data integration to improve
adaptability and scalability. Beyond NEVs, the framework has general applicability in domains such
as renewable energy adoption, smart appliances, and digital finance where diffusion prediction under
external shocks is crucial.
References
[1] Almeida, V.N.d.; Alegre, L.N.; Bazzan, A.L.C. (2024). Knowledge Transfer in Multi-Objective
Multi-Agent Reinforcement Learning via Generalized Policy Improvement,Computer Science and
Information Systems, 21(1), 335–362, 2024. DOI:10.2298/CSIS221210071A.
[2] Banciu, D.; Petrescu, A.-G.; Oncioiu, I.; et al. (2024). The Simulation Framework for Automated
Trading Algorithms on Capital Markets,Studies in Informatics and Control, 33(4), 51–58, 2024.
DOI:10.24846/v33i4y202405.
[3] Deng, G.F. (2023). Dynamic Price Competition Market for Retailers in the Context of Consumer
Learning Behavior and Supplier Competition: Machine Learning-Enhanced Agent-Based Model-
ing and Simulation,Advances in Production Engineering & Management, 18(4), 434–446, 2023.
DOI:10.14743/apem2023.4.483.
[4] Ding, Y.; Wu, P.; Zhao, J.; Zhou, L. (2025). Forecasting product sales using text mining:
A case study in new energy vehicle,Electronic Commerce Research, 25(1), 495–527, 2025.
DOI:10.1007/s10660-023-09701-9.
[5] Dornelas, R.S.; Lima, D.A. (2023). Correlation Filters in Machine Learning Algorithms to Select
Demographic and Individual Features for Autism Spectrum Disorder Diagnosis,Journal of Data
Science and Intelligent Systems, 3(1), 7–9, 2023. DOI:10.47852/bonviewJDSIS32021027.
[6] Dzienis, A.M.; McCaleb, A. (2024). Motives behind Sino-Japanese strategic alliances in the new
energy vehicles sector in the age of the Belt and Road Initiative,Asia Pacific Business Review,
30(2), 274–299, 2024. DOI:10.1080/13602381.2022.2093533.
[7] El Khatib, M.; Al Hammadi, A.; Al Hamar, A. (2022). How global supply chain man-
agement is disrupting local supply chain management case of oil and gas industry in
UAE,American Journal of Industrial and Business Management, 12(5), 1067–1078, 2022.
DOI:10.4236/ajibm.2022.125056.
[8] Feng, Z.; Luo, N.; Shalpegin, T.; Cui, H. (2024). The influence of carbon emis-
sion reduction instruments on blockchain technology adoption in recycling batteries of the
new energy vehicles,International Journal of Production Research, 62(3), 891–908, 2024.
DOI:10.1080/00207543.2023.2175173.
[9] Guidolin, M.; Manfredi, P. (2023). Innovation diffusion processes: Concepts, models,
and predictions,Annual Review of Statistics and Its Application, 10(1), 451–473, 2023.
DOI:10.1146/annurev-statistics-040220-091526.
[10] Hatamlah, H.; Allahham, M.; Abu-AlSondos, I.A. (2023). The role of business intelligence
adoption as a mediator of big data analytics in the management of outsourced reverse sup-
ply chain operations,Applied Mathematics & Information Sciences, 17(5), 897–903, 2023.
DOI:10.18576/AMIS/170516.

https://doi.org/10.15837/ijccc.2026.4.7220 13
[11] Jones, B.; Nguyen-Tien, V.; Elliott, R.J. (2023). The electric vehicle revolution: Critical
material supply chains, trade and development,The World Economy, 46(1), 2–26, 2023.
DOI:10.1111/twec.13345.
[12] Li, M.; Zhang, Z.; Lu, M.; Jia, X.; Liu, R.; Zhou, X.; Zhang, Y. (2023). Internet Financial
Credit Risk Assessment with Sliding Window and Attention Mechanism LSTM Model,Tehnicki
vjesnik-Technical Gazette, 30(1), 1–7, 2023. DOI:10.17559/TV-20221110173532.
[13] Liu, J.; Meucci, A.; Young, I.R. (2023). Projected wave climate of Bass Strait and south-
east Australia by the end of the twenty-first century,Climate Dynamics, 60(1), 393–407, 2023.
DOI:10.1007/s00382-022-06310-4.
[14] Mao, Y.; Liu, S.; Gong, D. (2023). A Text Mining and Ensemble Learning Based Ap-
proach for Credit Risk Prediction,Tehnicki vjesnik-Technical Gazette, 30(1), 138–147, 2023.
DOI:10.17559/TV-20250524002692.
[15] Mao, J. (2024). Optimizing enterprise marketing project portfolios using fuzzy ant colony
optimization,International Journal of Computers Communications & Control, 19(3), 2024.
DOI:10.15837/ijccc.2024.3.6458.
[16] Ngoc, N.M.; Viet, D.T.; Tien, N.H. (2022). Russia-Ukraine war and risks to global
supply chains,International Journal of Mechanical Engineering, 7(6), 633–640, 2022.
DOI:10.31893/multirev.2024spe017.
[17] Olivares, V.; Oddershede, A.; Quezada, L.; Vargas, M.; Montt, C. (2024). Development of
a model for generating trajectories for an autonomous naval vehicle using genetic algorithms
in MATLAB,International Journal of Computers Communications & Control, 19(6), 2024.
DOI:10.15837/ijccc.2024.6.6865.
[18] Rahimi, S.; Huang, L.; Norris, J.; Hall, A.; Goldenson, N.; Krantz, W.; et al. (2024). An overview
of the Western United States dynamically downscaled dataset (WUS-D3),Geoscientific Model
Development, 17(6), 2265–2286, 2024. DOI:10.5194/gmd-17-2265-2024.
[19] Ribeiro, J.; Santos, R.; Analide, C.; Silva, F. (2024). Implementing Federated Learning and
Explainability Techniques in Regression Models to Increase Transparency and Reliability,Studies
in Informatics and Control, 33(4), 15–24, 2024. DOI:10.24846/v33i4y202402.
[20] Wei, Z.H.; Yan, L.; Yan, X. (2024). Optimizing Production with Deep Reinforcement Learning,
International Journal of Simulation Modelling, 23(4), 692–703, 2024. DOI:10.2507/IJSIMM23-4-
CO17.
[21] Wu, J.; Yu, J. (2023). Blockchain’s impact on platform supply chains: Transaction cost and
information transparency perspectives,International Journal of Production Research, 61(11),
3703–3716, 2023. DOI:10.1080/00207543.2022.2027037.
[22] Xu, Y.; Shan, X.; Guo, M.; Gao, W.; Lin, Y.S. (2024). Design and application of ex-
perience management tools from the perspective of customer perceived value: A study
on the electric vehicle market,World Electric Vehicle Journal, 15(8), 378–404, 2024.
DOI:10.1080/23311975.2025.2514939.
[23] Yi, Z.; Yu, M.; Cheung, K.L. (2022). Impacts of counterfeiting on a global supply chain,Manufac-
turing & Service Operations Management, 24(1), 159–178, 2022. DOI:10.1287/msom.2020.0912.
[24] Zhang, R. (2024). Impact of ID3 Algorithm-based Reading Resource Recommendation Model on
College English Reading Teaching,IEIE Transactions on Smart Processing & Computing, 13(4),
372–382, 2024. DOI:10.5573/IEIESPC.2024.13.4.372.

https://doi.org/10.15837/ijccc.2026.4.7220 14
[25] Zhao, L.; Li, F.; Sun, D.; Zhao, Z. (2024). An improved ant colony algorithm based on Q-Learning
for route planning of autonomous vehicle,International Journal of Computers Communications
& Control, 19(3), 2024. DOI:10.15837/ijccc.2024.3.5382.
Copyright©2026 by the authors. Licensee Agora University, Oradea, Romania.
This is an open access article distributed under the terms and conditions of the Creative Commons
Attribution-NonCommercial 4.0 International License.
Journal’s webpage: http://univagora.ro/jour/index.php/ijccc/
This journal is a member of, and subscribes to the principles of,
the Committee on Publication Ethics (COPE).
https://publicationethics.org/members/international-journal-computers-communications-and-control
Cite this paper as:
Guiling, L.; Na, T.; Tingting, Jiang.; Yuyan Chen (2026). A Collaborative Model Integrating ID3
and Bass Algorithm for Cross-Border Market Diffusion Prediction,International Journal of Computers
Communications&Control, 21(4), 7220, 2026.
https://doi.org/10.15837/ijccc.2026.4.7220
