---
title: Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support
url: https://doi.org/10.25258/ijddt.16.77s.152
category: consumer-behavior
subcategory: framework
date: 2026-10
venue: International Journal of Drug Delivery Technology
authors: []
source: openalex-oa
pdf_url: https://doi.org/10.25258/ijddt.16.77s.152
pages: 11
chars: 47123
fetched_at: '2026-11-08T19:28:29+00:00'
kb_version: 1
---

# Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

RESEARCH PAPER

Page: 1309
Optimized Artificial Intelligence Framework for Retail Sales Prediction and
Decision Support
Tarika Verma1, Prof. (Dr.) Brij Mohan Goel2
1Research Scholar, Computer Science & Engineering (CSE) Department, Baba Mastnath University, Rohtak, Haryana,
India. tverma.work@gmail.com, ORCID: 0009-0003-0748-3471
2Professor and Research Supervisor, Computer Science & Engineering (CSE) Department, Baba Mastnath University,
Rohtak, Haryana, India. brijmohan.vce@gmail.com

Abstract
The retail industry operates in a highly dynamic and competitive environment characterized by fluctuating consumer
behavior, seasonal demand variations, and market uncertainties. Accurate sales forecasting is essential for effective
inventory management, demand planning, pricing strategies, and overall business decision-making. However, traditional
statistical forecasting techniques often fail to capture the complex nonlinear and temporal relationships present in large-
scale retail datasets, resulting in limited predictive performance. To address these challenges, this study proposes an
optimized Artificial Intelligence (AI)-based Decision Support System (DSS) for retail sales forecasting using hybrid
machine learning techniques.
The proposed framework integrates multiple machine learning models to leverage their complementary strengths in
capturing both linear and nonlinear patterns from historical sales data. Advanced optimization techniques are
incorporated for hyperparameter tuning to enhance model accuracy, reduce overfitting, and improve computational
efficiency. The system employs intelligent forecasting mechanisms capable of processing large volumes of retail data
and generating accurate, scalable, and near real-time sales predictions. Furthermore, the integration of the forecasting
framework within a decision support environment enables retailers to obtain actionable insights for inventory control,
supply chain management, promotional planning, and resource allocation.
The proposed AI-based DSS aims to improve forecasting reliability, operational efficiency, and strategic decision -
making in retail organizations. By combining hybrid machine learning models with optimization algorithms, the
framework provides a robust and adaptive solution for modern retail sales forecasting, ultimately contributing to
enhanced business performance, reduced operational costs, and improved customer satisfaction.

Keywords: Retail Sales Forecasting, Artificial Intelligence, Machine Learning, Hybrid Models, Decision Support
System, Hyperparameter Optimization, Predictive Analytics, Retail Management
How to cite this article: Verma T, Goel BM., Optimized Artificial Intelligence Framework for Retail Sales Prediction
and Decision Support. Int J Drug Deliv Technol. 2026;16(77s): 1309-1319; DOI: 10.25258/ijddt.16.77s.152.

Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

IJDDT, Volume16  Issue 77s,  2026
Page: 1310
1. Introduction
The retail sector faces significant challenges in
accurately forecasting sales due to dynamic consumer
behavior, seasonal variations, intense competition, and
market uncertainties. Traditional statistical forecasting
methods often struggle to capture the complex nonlinear
and temporal patterns present in large-scale retail data.
Recent advancements in Artificial Intelligence (AI) and
Machine Learning (ML) have enabled the development
of intelligent forecasting systems that can automatically
identify hidden patterns and improve prediction
accuracy. Hybrid machine learning models, which
combine the strengths of multiple algorithms, have
gained popularity for their enhanced robustness,
generalization capability, and forecasting performance.

Figure 1. Retail Sales Forecasting: Challenges and Role of Artificial Intelligence

Additionally, hyperparameter optimization techniques
such as Bayesian optimization, grid search, random
search, and evolutionary algorithms further improve
model effectiveness by identifying optimal parameter
settings. Integrating these advanced forecasting models
into Decision Support Systems (DSS) provides retailers
with actionable insights for inventory management,
demand planning, pricing, and supply chain optimization.
Therefore, this study proposes an optimized AI-based
DSS that utilizes hybrid machine learning techniques and
optimization methods to deliver accurate, scalable, and
near real-time retail sales forecasts, supporting effective
business decision-making and operational efficiency.
1.1 Background of the Study
The retail industry has undergone significant
transformation with the rapid growth of digital
technologies, e-commerce platforms, and data-driven
business practices. Modern retailers generate massive
volumes of data from transactions, customer interactions,
online purchases, inventory records, and market trends.
This abundance of data presents valuable opportunities
for extracting insights that can improve operational
efficiency and business performance. Among various
retail operations, sales forecasting is one of the most
critical activities because it directly influences inventory
management, demand planning, pricing strategies,
workforce allocation, and supply chain optimization.
Accurate sales forecasting enables retailers to anticipate
future demand, minimize stock shortages and overstock
situations, reduce operational costs, and improve
customer satisfaction. However, forecasting retail sales
remains a challenging task due to the dynamic nature of
consumer behavior, seasonal fluctuations, promotional
campaigns, economic conditions, and competitive market
environments. Traditional forecasting methods such as
moving averages, exponential smoothing, and regression
analysis often struggle to model complex nonlinear
relationships and temporal dependencies inherent in retail
datasets.
Recent advancements in Artificial Intelligence (AI) and
Machine Learning (ML) have provided new
opportunities to enhance forecasting accuracy. ML
algorithms can automatically learn patterns from large
datasets and adapt to changing market conditions without
relying heavily on predefined assumptions. Techniques
such as Random Forest, Gradient Boosting, Support
Vector Machines, Artificial Neural Networks, and Deep
Learning models have demonstrated promising results in
retail demand prediction. However, individual models
may have limitations in capturing all aspects of retail
sales behavior, leading researchers to explore hybrid
machine learning approaches that combine multiple
algorithms to exploit their complementary strengths.
Another important aspect of machine learning -based
forecasting is hyperparameter optimization. The
performance of predictive models depends significantly
on the selection of appropriate parameters. Optimization
techniques such as Grid Search, Random Search,
Dynamic Retail
Environment
Consumer Behavior
Seasonality
Promotions
Market Uncertainty
Competition
Challenges in Sales
Forecasting
Traditional
Forecasting
Limitations
Artificial
Intelligence &
Machine Learning
Better Prediction
Inventory Management
Demand Planning
Pricing
Supply Chain
Decision Making

Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

IJDDT, Volume16  Issue 77s,  2026
Page: 1311
Bayesian Optimization, and Evolutionary Algorithms
have emerged as effective approaches for identifying
optimal parameter configurations, thereby improving
prediction accuracy and model robustness.
Furthermore, integrating intelligent forecasting models
into Decision Support Systems (DSS) enhances their
practical applicability in retail environments. A DSS
provides managers with timely forecasts, analytical
insights, and data-driven recommendations that support
strategic and operational decisions. By leveraging AI-
powered forecasting and optimization techniques,
retailers can improve demand planning, inventory
control, resource utilization, and overall business
performance.
Therefore, there is a growing need to develop an
optimized AI-based Decision Support System that
combines hybrid machine learning models and advanced
optimization techniques to provide accurate, scalable,
and near real-time retail sales forecasting. Such a system
can assist retailers in making informed decisions,
improving competitiveness, and achieving sustainable
growth in an increasingly complex and data -intensive
marketplace.
1.2 Need of the Study
The retail industry operates in a highly dynamic
environment characterized by rapidly changing customer
preferences, seasonal demand fluctuations, promotional
activities, and market uncertainties. Accurate sales
forecasting has become essential for retailers to
effectively manage inventory, optimize supply chains,
reduce operational costs, and improve customer
satisfaction. However, traditional forecasting techniques
often fail to capture the complex nonlinear relationships
and temporal dependencies present in modern retail
datasets, resulting in inaccurate predictions and
inefficient decision-making.
With the increasing availability of large-scale retail data,
there is a growing need for intelligent forecasting
systems capable of processing vast amounts of
information and generating accurate predictions in real
time. Machine Learning (ML) and Artificial Intelligence
(AI) techniques have demonstrated significant potential
in improving forecasting performance by automatically
identifying hidden patterns and trends within data.
Nevertheless, individual machine learning models may
not adequately address all forecasting challenges due to
variations in data characteristics and market conditions.
Hybrid machine learning approaches, which combine
multiple algorithms, offer a promising solution by
leveraging the strengths of different models to improve
prediction accuracy and robustness. Additionally, the
performance of these models depends heavily on optimal
hyperparameter selection, creating a need for advanced
optimization techniques. Therefore, there is a strong need
to develop an optimized AI-based Decision Support
System (DSS) that integrates hybrid machine learning
models and optimization methods to provide accurate,
scalable, and timely retail sales forecasts for effective
business decision-making.
1.3 Significance of the Study
This study is significant because it addresses one of the
most critical challenges in the retail sector: accurate sales
forecasting. The proposed optimized AI-based Decision
Support System contributes to both academic research
and practical retail operations by combining hybrid
machine learning techniques with advanced optimization
strategies.
From a business perspective, the system enables retailers
to make informed decisions regarding inventory
management, demand planning, pricing policies,
promotional campaigns, and supply chain operations.
Improved forecasting accuracy can reduce inventory
holding costs, minimize stockouts and overstock
situations, enhance resource utilization, and increase
customer satisfaction. The near real -time forecasting
capability further supports proactive decision-making in
rapidly changing market environments.
From a technological perspective, the study advances the
application of artificial intelligence, machine learning,
and hyperparameter optimization in retail analytics. The
integration of multiple learning models enhances
prediction reliability and model generalization, while
optimization techniques improve computational
efficiency and forecasting performance.
From an academic perspective, the research contributes
to the growing body of knowledge on hybrid machine
learning frameworks and AI-driven decision support
systems. The proposed framework can serve as a
foundation for future studies in retail analytics, predictive
modeling, demand forecasting, and intelligent business
systems. Ultimately, the study supports the development
of data-driven retail strategies that improve
competitiveness, profitability, and sustainable business
growth.

2. Literature Review
Khade S. et al. (2026) propose a Causal-XAI framework
for retail sales forecasting using Double Machine
Learning (DML) and Causal Transformer models to
improve prediction accuracy and interpretability. The
study notes that traditional deep learning and ensemble
models fail to distinguish causation from correlation and
lack transparency. The proposed framework improves
forecasting and provides actionable insights by
identifying causal factors affecting sales, thereby
supporting better decision making and return on
investment. [1]
Munawar M. A. and Sudirman I. (2026) study LSTM-
based models for hourly sales forecasting in SME food
and beverage retail. The research compares LSTM with
Naive Forecast and Moving Average models using point-
of-sale data. Results show that LSTM achieves lower
MAE and RMSE and effectively captures intra -day
seasonal patterns. The study concludes that LSTM
reduces losses due to overstocking and understocking,
improving inventory management in retail environments.
[2]
Devi D. G. et al. (2026) present a multi-granular machine
learning approach for retail sales forecasting using
exploratory data analysis and feature engineering. The
study evaluates Linear Regression, Random Forest, and
Gradient Boosting across daily, monthly, and quarterly
datasets. Results show that selecting appropriate models
for different time scales improves forecasting accuracy

Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

IJDDT, Volume16  Issue 77s,  2026
Page: 1312
and supports better strategic decision-making in retail.
[3]
Sangeetha S. et al. (2026) propose an adaptive and
explainable Auto-ARIMA-based forecasting platform.
The study highlights limitations of deep learning models
in interpretability and computational cost. The proposed
system integrates automated model selection, seasonal
decomposition, and anomaly detection, achieving
competitive accuracy with improved transparency and
efficiency for retail decision support systems. [4]
Boyko N. and Salabay B. (2026) conduct a comparative
study of classical and hybrid forecasting models using
retail data. Models such as SES, Holt’s, Holt-Winters,
TheilWage, and SutteARIMA are analyzed. Results show
that Holt-Winters and 8 SutteARIMA perform best by
capturing trend and seasonality effectively, highlighting
the importance of model selection and parameter
optimization. [5]
 Essien I. A. et al. (2025) compare hybrid AI models
including XGBoost, LSTM, and Reinforcement Learning
for real-time decision-making. The study shows that
hybrid approaches improve adaptability and accuracy
under dynamic conditions, with reinforcement learning
aiding optimization and LSTM capturing temporal
dependencies effectively. [6]
 M. H. Zamil (2025) presents a systematic review of AI-
based business analytics models for financial forecasting
in SMEs. The study highlights the growing use of
machine learning-based decision support systems,
including regression models, neural networks, and
ensemble methods. [7]
A. Zach (2025) focuses on retail supply chain forecasting
and inventory optimization using hybrid machine
learning models. The study shows that combining
predictive analytics with inventory control improves
demand forecasting and reduces stockouts, with hybrid
models improving robustness under seasonal and
uncertain demand. [8]
G. V. Radhakrishnan et al. (2025) propose an AI-based
demand forecasting system for supply chain
optimization. The results indicate improved
responsiveness, reduced wastage, and better inventory
planning, especially in large-scale industrial applications.
[9]
S. Mansur et al. (2025) develop a hybrid neural network
model for retail sales forecasting by incorporating
external factors such as promotions, weather, and
customer behavior. The study shows that hybrid models
outperform standalone models by capturing nonlinear
and contextual patterns, leading to more accurate
forecasts. [10]
K. Srinivasan et al. (2024) propose an AI -based
optimization model for e -commerce supply chains
combining HMO, reinforcement learning, tabu search,
and MDVRP. The approach improves demand
forecasting, inventory management, and logistics
efficiency, resulting in higher delivery performance and
reduced operational costs. [11]
Suresh B. S. and Suresh M. (2024) present an AI-based
retail sales management system using optimized
metaheuristic algorithms. The study shows that
evolutionary algorithms improve forecasting accuracy
and recommendation quality, leading to better customer
satisfaction and sales. [12]
H. Sharma et al. (2024) develop machine learning-based
models for forecasting and inventory optimization. The
study emphasizes integrating prediction with inventory
control to improve cost efficiency and demand-supply
balance, enhancing overall decision-making in supply
chain management. [13]
 E. M. Howard (2024) introduces AI -based demand
sensing for improving forecast accuracy using real-time
data and analytics. The study shows improved
responsiveness to market changes and reduced
forecasting errors, making it important for modern supply
chains. [14]
 Nkomo N. and Mupa M. N. (2024) analyze AI-driven
predictive customer behavior analytics in e-commerce.
The study shows that AI models outperform traditional
methods by better identifying customer preferences and
improving personalization and decision-making. [15]
 M. Rahman et al. (2023) study automated
hyperparameter optimization in deep learning. The work
highlights methods such as Bayesian optimization and
evolutionary algorithms, which improve model
performance while reducing computational cost, thereby
enhancing efficiency and accuracy in predictive systems.
[16]
T. A. Rainy et al. (2023) review AI-enhanced decision
support tools in information systems. The study discusses
their applications in service-based enterprises, improving
decision-making, operational efficiency, and business
intelligence through AI integration. [17]
S. Suddala (2023) explores AI-based demand forecasting
and inventory optimization in e-commerce fulfillment
centers. The study shows that AI reduces inventory costs,
improves order fulfillment, and enhances logistics
efficiency. [18]
 L. N. B. Long et al. (2023) propose a decision support
system for inventory management under uncertainty. The
model uses probabilistic analysis and machine learning to
handle uncertainty, improving inventory control and
reducing risk. [19]
H. Wagner and K. Becker (2022) design a cloud-based
machine learning decision support system for business
decision-making. The study highlights the scalability and
flexibility of cloud AI systems for handling large datasets
and complex analytics. [20]
M. Garouani et al. (2022) explore explainable AutoML in
industrial data mining. The study emphasizes
transparency, interpretability, and efficiency of AI
models, which are important for industrial adoption and
trust in AI systems. [21]
T. Vasugi (2022) proposes an AI-optimized multi-cloud
resource management architecture for secure banking
systems. The study highlights improved resource
utilization, security, and scalability through AI -based
optimization. [22]
A. Khan et al. (2022) examine AI -based demand
response systems in smart grids. The study shows that AI
improves energy consumption, grid stability, and real-
time energy management. [23]
 R. G. Goriparthi (2021) discusses AI and machine
learning applications in supply chain logistics

Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

IJDDT, Volume16  Issue 77s,  2026
Page: 1313
optimization. The study reports improvements in route
optimization, demand forecasting, and operational
efficiency. [24]
 A. Göppert et al. (2021) propose artificial neural
networks for predicting performance indicators in
interconnected assembly systems. The study shows
improved scheduling efficiency and production
optimization using AI-based predictive models. [25]

Table 1: Comparison of Previous Studies on AI-Based Retail Sales Forecasting
S.
No.
Author(s) &
Year
Method / Model Main Focus Key Contribution /
Findings
Identified Limitation /
Gap
1 Khade et al.
(2026)
Double Machine
Learning (DML),
Causal
Transformer, XAI
Retail sales
forecasting
Improves forecasting
while identifying causal
factors and enhancing
interpretability
Causal-XAI integration
requires further
validation across diverse
retail datasets
2 Munawar &
Sudirman
(2026)
LSTM Hourly retail sales
forecasting
LSTM outperforms
Naive Forecast and
Moving Average for
intra-day forecasting
Focused mainly on
hourly SME food and
beverage retail data
3 Devi et al.
(2026)
Linear Regression,
Random Forest,
Gradient Boosting
Multi-granular
forecasting
Demonstrates that
model selection
according to daily,
monthly, and quarterly
time scales improves
forecasting
Limited integration of
multiple models into a
unified optimized DSS
4 Sangeetha et al.
(2026)
Auto-ARIMA,
seasonal
decomposition,
anomaly detection
Explainable sales
forecasting
Provides adaptive
forecasting with
improved transparency
and computational
efficiency
Classical forecasting
may have limitations in
highly nonlinear retail
environments
5 Boyko &
Salabay (2026)
SES, Holt's, Holt-
Winters,
SutteARIMA
Comparative
forecasting
Holt-Winters and
SutteARIMA
effectively capture
trend and seasonality
Does not provide a
comprehensive hybrid
AI-DSS framework
6 Essien et al.
(2025)
XGBoost, LSTM,
Reinforcement
Learning
Real-time
decision-making
Hybrid AI improves
adaptability and
forecasting under
dynamic conditions
Further optimization and
retail-specific validation
are required
7 Zamil (2025) ML, neural
networks,
ensemble models
AI business
analytics
Reviews AI -based
decision-support
approaches for financial
forecasting in SMEs
Broad financial focus
rather than dedicated
retail sales forecasting
8 Zach (2025) Hybrid Machine
Learning
Retail supply
chain and
inventory
optimization
Combines forecasting
and inventory control to
reduce stockouts and
improve robustness
Further development of
real-time and adaptive
forecasting is needed
9 Radhakrishnan
et al. (2025)
AI-based
forecasting
Supply-chain
demand
forecasting
Improves
responsiveness,
wastage reduction, and
inventory planning
Focus primarily on
supply-chain
applications rather than
integrated retail DSS
10 Mansur et al.
(2025)
Hybrid Neural
Networks
Retail sales
forecasting
Incorporates
promotions, weather,
and customer behavior;
hybrid models
outperform standalone
approaches
More advanced
optimization and
explainability
mechanisms can be
explored
11 Srinivasan et al.
(2025)
HMO, MaxEnt-
RL, Tabu Search,
MDVRP
E-commerce
supply-chain
optimization
Improves demand
forecasting, inventory
management, and
delivery efficiency
Complex framework;
broader retail forecasting
validation is required
12 Suresh &
Suresh (2024)
Optimized
Metaheuristic
Algorithms
Retail sales
management
Optimization improves
forecasting and
recommendation
Greater integration with
real-time DSS and
hybrid deep learning is

Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

IJDDT, Volume16  Issue 77s,  2026
Page: 1314
performance needed
13 Sharma et al.
(2024)
Machine Learning
Models
Forecasting and
inventory
optimization
Integrates demand
prediction with
inventory control for
improved cost
efficiency
Limited emphasis on
advanced hybrid
architectures
14 Howard (2024) AI-based Demand
Sensing
Supply-chain
forecasting
Uses real-time data to
improve responsiveness
and reduce forecasting
errors
Requires integration of
broader retail variables
and decision -support
capabilities
15 Nkomo &
Mupa (2024)
Traditional vs. AI-
driven models
Predictive
customer behavior
AI models improve
customer preference
identification and
personalization
Customer behavior focus
rather than complete
sales forecasting
framework
16 Rahman et al.
(2023)
Bayesian
Optimization,
Evolutionary
Algorithms
Hyperparameter
optimization
Automated
optimization improves
deep-learning
efficiency and
predictive performance
Does not specifically
address complete retail
forecasting-DSS
integration
17 Rainy et al.
(2023)
AI-enhanced DSS Decision support Highlights AI
integration for business
intelligence and
operational decision-
making
General information -
system focus; retail -
specific implementation
remains limited
18 Suddala (2023) AI-based demand
forecasting
E-commerce
inventory
optimization
AI reduces inventory
costs and improves
fulfillment and logistics
Limited exploration of
hybrid models and
advanced optimization
19 Long et al.
(2023)
ML and
probabilistic
analysis
Inventory DSS
under uncertainty
Improves inventory
control and risk
management under
stochastic events
Primarily inventory -
focused rather than
comprehensive sales
forecasting
20 Wagner &
Becker (2022)
Cloud-based
Machine Learning
Business DSS Demonstrates
scalability and
flexibility of cloud -
based AI decision
support
Requires retail-specific
forecasting and real-time
implementation
21 Garouani et al.
(2022)
Explainable
AutoML
Industrial data
mining
Improves transparency,
interpretability, and
efficiency of automated
ML
Application is industrial
rather than specifically
retail forecasting
22 Vasugi (2022) AI optimization,
Multi-cloud
architecture
Resource
management
Improves resource
utilization, security, and
scalability
Banking/networking
focus limits direct retail
applicability
23 Khan et al.
(2022)
Artificial
Intelligence
Demand response
and real -time
management
Demonstrates AI
potential for demand
prediction and dynamic
resource management
Smart-grid context;
direct retail forecasting
applicability is limited
24 Goriparthi
(2021)
AI and Machine
Learning
Supply-chain
logistics
Improves route
optimization, demand
forecasting, and
operational efficiency
Limited emphasis on
hybrid forecasting and
retail DSS
25 Göppert et al.
(2021)
Artificial Neural
Networks
Predictive
performance and
scheduling
ANN-based prediction
improves scheduling
and production
optimization
Manufacturing focus;
retail sales forecasting
remains unexplored

From the above literature, it is observed that significant research has been conducted in retail sales forecasting using
machine learning, hybrid models, and decision support systems. However, most studies focus on individual models and
lack effective integration of hybrid approaches with systematic hyperparameter optimization. Limited work has also
been done on combining forecasting models with decision support systems for practical retail use. Therefore, there is a

Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

IJDDT, Volume16  Issue 77s,  2026
Page: 1315
need to develop an optimized hybrid AI-based decision support system that improves forecasting accuracy, robustness,
and real-world applicability.

Figure 2. Technology and Model Evolution in AI-Based Retail Sales Forecasting

2.1 Literature Synthesis
All the reviewed literature showed that there is a clear shift towards Artificial Intelligence (AI), Machine Learning
(ML), deep learning, hybrid models and intelligent Decision Support Systems (DSS) in the field of retail sales
forecasting. The traditional methods like ARIMA, Exponential Smoothing and Holt-Winters are capable of detecting
trend and seasonal components, but are not suitable for addressing complex nonlinear relationships and shifting
consumer behavior [4,5]. Random Forest, Gradient Boosting, XGBoost, ANN and LSTM are examples of models that
have proven better at learning complex sales patterns and temporal relationships, such as machine learning and deep
learning models [2,3,6]. In addition to this, hybrid models use complementary algorithms and external parameters like
promotions, weather and customer behavior to boost forecasting accuracy [8,10].
Additionally, it is important to optimize the hyperparameters of the model to enhance its performance and efficiency,
which can be done through various techniques such as Bayesian optimization, evolutionary optimization, and
metaheuristic optimization as highlighted in the literature [12,16]. Moreover, the use of AI forecasting is growing in
combination with inventory management, supply-chain optimization, and DSS [9,11,18,19]. In summary, research so far
has shown considerable advancement, but it is still scattered and fragmented according to the models used for
forecasting, optimization methods, explainability, and decision support application. This underscores the need to have
an integrated hybrid AI framework that integrates the optimized forecasting models with a smart DSS in order to
empower retailers with accurate, robust and actionable decisions.

3. Research Gap
A comprehensive review of recent studies reveals that substantial progress has been made in retail sales forecasting
through the application of Artificial Intelligence (AI), Machine Learning (ML), Deep Learning (DL), and Decision
Support Systems (DSS). Various approaches, including LSTM, Random Forest, Gradient Boosting, Reinforcement
Learning, AutoML, Explainable AI (XAI), and hybrid forecasting models, have demonstrated improved prediction
accuracy and operational efficiency. Moreover, several studies have explored inventory optimization, demand
forecasting, supply chain management, and customer behavior analytics using AI-driven techniques.

Despite these advancements, several research gaps remain:
1. Limited Integration of Hybrid Models: Most existing studies focus on standalone forecasting models such as
LSTM, XGBoost, Random Forest, or ARIMA. Although hybrid models have shown promising results, there
is limited research on developing optimized hybrid frameworks that effectively combine multiple machine
learning and deep learning algorithms to capture both linear and nonlinear sales patterns.
2. Insufficient Hyperparameter Optimization: The performance of forecasting models is highly dependent on
parameter selection. Many studies employ default settings or basic tuning approaches, resulting in suboptimal
performance. Comprehensive integration of advanced optimization techniques such as Bayesian
AI-Based Decision Support System
Real-Time Forecasting
 Inventory
 Pricing
 Supply Chain
 Business Decisions
Optimization & Explainability
Bayesian Optimization
 Metaheuristic Optimization
 XAI
 Causal-XAI
Hybrid AI Models
LSTM
 XGBoost
 Hybrid Neural Networks
 Ensemble Models
Deep Learning
ANN
 LSTM
 CNN
 Transformer
Machine Learning
Linear Regression
 Random Forest
 XGBoost
 SVM
Traditional Forecasting
Moving Average
 Exponential Smoothing
 ARIMA

Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

IJDDT, Volume16  Issue 77s,  2026
Page: 1316
Optimization, Evolutionary Algorithms, and Metaheuristic Optimization within retail forecasting frameworks
remains underexplored.
3. Lack of Unified Decision Support Systems: Existing research primarily emphasizes forecasting accuracy
without integrating prediction models into a comprehensive Decision Support System. Retail managers
require actionable insights for inventory planning, pricing, procurement, and supply chain management;
however, few studies provide an end-to-end DSS framework that supports practical decision-making.
4. Limited Real-Time Forecasting Capability: Many forecasting models are developed and evaluated using static
datasets and offline environments. There is a lack of scalable AI-based systems capable of generating near
real-time forecasts and adapting dynamically to changing market conditions and customer behavior.
5. Inadequate Consideration of Multi-Dimensional Retail Factors: Several forecasting approaches rely mainly on
historical sales data while neglecting external influencing factors such as promotions, seasonal events,
economic conditions, customer preferences, and market trends. Integrating these heterogeneous factors
remains a significant challenge.
6. Trade-off Between Accuracy and Interpretability: Advanced deep learning models often provide high
prediction accuracy but suffer from poor interpretability. Conversely, interpretable models may compromise
forecasting performance. Research is needed to develop frameworks that achieve both high accuracy and
explainability for improved managerial trust and adoption.
7. Limited Focus on Scalable and Generalizable Frameworks: Many proposed models are dataset-specific and
may not generalize well across different retail domains, product categories, or geographical regions. There is
a need for robust and scalable forecasting systems that can perform effectively in diverse retail environments.

Figure 3: Research Gap

4. Problem Statement
Although machine learning techniques are widely
adopted in retail sales forecasting, several limitations
continue to affect their overall effectiveness and practical
applicability. One of the primary challenges is the
inherent volatility and seasonality present in retail data,
which often results in unstable and less reliable
predictions. In addition, standalone machine learning
models are generally limited in their ability to capture
complex nonlinear relationships and rapidly changing
patterns within retail environments. Another significant
issue is poor model generalization, where models trained
on specific datasets tend to perform inconsistently when
applied to different retail contexts or unseen data
distributions. Furthermore, the absence of systematic and
automated hyperparameter optimization often leads to
suboptimal model configurations, thereby reducing both
predictive accuracy and computational efficiency. In
addition, the integration of forecasting models into
decision-making frameworks remains limited,
particularly in terms of supporting structured and
practical decision support in real-world retail operations.
These limitations collectively restrict the effectiveness of
existing approaches in addressing dynamic retail
forecasting requirements. To overcome these challenges,
this research proposes a hybrid and optimized AI-based
Decision Support System aimed at improving forecasting
accuracy, robustness, adaptability, and overall decision-
making efficiency in retail environments.

5. Future Scope
The proposed AI-based Decision Support System (DSS)
for retail sales forecasting offers significant opportunities
for future enhancement and expansion. One important
direction is the integration of real-time data streams from
Point-of-Sale (POS) systems, Internet of Things (IoT)
devices, RFID sensors, and online retail platforms. Such
integration would enable continuous forecasting and
dynamic decision-making, allowing retailers to respond
immediately to changing customer demands and market
conditions.
Future research can explore advanced deep learning
architectures such as Transformers, Temporal Fusion
Transformers (TFT), Attention Mechanisms, Graph
Neural Networks (GNNs), and Large Language Models
(LLMs) to further improve forecasting accuracy and
Hybrid
Integration
Optimization
Real-time
Capability
External
Factors
Interpretability
Scalability
 DSS Integration

Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

IJDDT, Volume16  Issue 77s,  2026
Page: 1317
capture complex temporal dependencies. These models
can better handle long-term trends, seasonal variations,
and multivariate relationships in retail datasets.
Another promising area is the incorporation of
Explainable Artificial Intelligence (XAI) techniques to
improve model transparency and interpretability.
Explainable forecasting systems can help retail managers
understand the key factors influencing predictions,
thereby increasing trust, accountability, and adoption of
AI-driven decision-making tools.
The forecasting framework can also be enhanced by
incorporating external data sources such as weather
conditions, social media sentiment, economic indicators,
public holidays, promotional campaigns, competitor
pricing, and market trends. The integration of these
heterogeneous data sources can provide a more
comprehensive understanding of demand patterns and
improve prediction reliability.
Cloud-based deployment and edge computing
technologies can be utilized to improve system
scalability, accessibility, and computational efficiency. A
cloud-enabled DSS would support large -scale retail
operations across multiple stores and geographical
regions while enabling real-time analytics and centralized
decision-making.
Furthermore, reinforcement learning and adaptive
optimization techniques can be integrated to create self-
learning forecasting systems that continuously update
their models based on new data and feedback. Such
intelligent systems can automatically optimize inventory
levels, pricing strategies, replenishment schedules, and
promotional activities in response to evolving market
dynamics.
Future studies may also investigate personalized
forecasting models for different product categories,
customer segments, and regional markets. Multi -
objective optimization techniques can be incorporated to
simultaneously optimize forecasting accuracy, inventory
costs, customer satisfaction, and supply chain
performance.
Overall, the integration of advanced AI technologies,
real-time analytics, explainability, cloud computing, and
adaptive learning mechanisms can transform the
proposed framework into a highly intelligent, scalable,
and autonomous retail decision support system capable
of supporting next-generation retail operations and
strategic business planning.

6. Conclusion
The retail industry faces increasing challenges in
accurately forecasting sales due to dynamic customer
behavior, seasonal fluctuations, market uncertainties, and
growing competition. Traditional forecasting methods
often struggle to capture the complex relationships
present in large-scale retail data, creating the need for
more intelligent and adaptive forecasting solutions.
Advances in Artificial Intelligence (AI) and Machine
Learning (ML) have demonstrated significant potential
for improving forecasting accuracy and supporting data-
driven decision-making in retail environments.
This study highlights the importance of developing an
optimized AI-based Decision Support System (DSS) that
integrates hybrid machine learning techniques and
advanced optimization methods for retail sales
forecasting. The literature review reveals that while
numerous forecasting models have been proposed,
limitations remain in terms of model integration,
hyperparameter optimization, scalability, interpretability,
and practical decision support capabilities. Addressing
these limitations requires a comprehensive framework
capable of leveraging the strengths of multiple
forecasting approaches while providing actionable
business insights.
The proposed framework aims to combine hybrid
machine learning models with optimization techniques to
improve prediction accuracy, robustness, and
computational efficiency. By integrating forecasting
outcomes into a decision support environment, the
system can assist retailers in inventory management,
demand planning, pricing strategies, resource allocation,
and supply chain optimization. Such a data -driven
approach can reduce operational costs, minimize
stockouts and overstock situations, and enhance customer
satisfaction.
Overall, the development of an optimized hybrid AI -
based DSS represents a promising solution for modern
retail forecasting challenges. The proposed system has
the potential to improve business intelligence, support
strategic decision-making, and enhance organizational
competitiveness in a rapidly evolving retail landscape.
Furthermore, future integration of real-time analytics,
explainable AI, cloud computing, and adaptive learning
techniques can further strengthen the effectiveness and
applicability of intelligent retail forecasting systems.

References
1. Khade, S., Singh, K. R., & Karule, K. (2026).
A Causal-XAI Framework for Retail Sales
Forecasting: Addressing Transparency and
Lack of Robustness in Deep Learning Models.
In 2026 3rd International Conference on
Emerging Trends in Engineering and Medical
Sciences (ICETEMS). IEEE.
https://doi.org/10.1109/ICETEMS66917.2026.
11469728
2. Munawar, M. A., & Sudirman, I. (2026).
LSTM-Based Hourly Sales Forecasting in
SME Food and Beverage Retail. In 2026
International Seminar on Intelligent Business
and Edge-Computing Research (ISIBER).
IEEE.
https://doi.org/10.1109/ISIBER68248.2026.11
469764
3. Devi, D. G., Sehrawat, K., & Dixit, S. (2026).
Prédictive Sales Forecasting in Retail: A Data-
Driven, Multi-Granular Machine Learning
Approach for Strategic Business Decision -
Making. SSRN Electronic Journal.
https://doi.org/10.2139/ssrn.6559098
4. Sangeetha, S., Valency, R., & Nanthetha Sri,
C. S. (2026). Design of an Adaptive and
Explainable Sales Forecasting Platform Using
Auto-ARIMA. In 2026 Second International
Conference on Multi-Agent Systems for

Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

IJDDT, Volume16  Issue 77s,  2026
Page: 1318
Collaborative Intelligence (ICMSCI). IEEE.
https://doi.org/10.1109/ICMSCI67830.2026.1
1469517
5. Boyko, N., & Salabay, B. (2026). Assessing
Sales Forecasting Methods: A Comparative
Evaluation of Exponential Smoothing Models
and SutteARIMA. Applied Computational
Intelligence and Soft Computing.
https://doi.org/10.1155/acis/6686245
6. Essien, I. A., Nwokocha, G. C., Erigha, E. D.,
Obuse, E., & Akindemowo, A. O. (2025).
Hybrid AI Models for Real-Time Decision-
Making in Dynamic Business Environments:
A Comparative Study of XGBoost, LSTM,
and Reinforcement Learning. International
Journal of Scientific Research in Humanities
and Social Sciences, 2(4), 156 -174.
https://ijsrhss.com/home/article/view/IJSRHSS
25288
7. Zamil, M. H. (2025). AI -Driven business
analytics for financial forecasting: a systematic
review of decision support models in SMEs.
Review of Applied Science and Technology,
4(02), 86 -117.
https://doi.org/10.63125/gjrpv442
8. Zach, A. (2025). Data-Driven Forecasting and
Inventory Optimization in Retail Supply
Chains Using Hybrid Machine Learning
Models. International Journal of Economics
and Commerce Research (IJECR), 5(1), 28–
34.
https://iaeme.com/Home/article_id/IJECR_05_
01_002
9. Radhakrishnan, G. V., Gaikwad, P. P.,
Pimplapure, V., Mohammed, I. A., Todmal, A.
D., & Sanne, S. H. V. (2025). AI -Based
Demand Forecasting System for Supply Chain
Optimization. In 2025 Second International
Conference on Intelligent Technologies for
Sustainable Electric and Communications
Systems (iTech SECOM). IEEE.
https://doi.org/10.1109/iTechSECOM64750.2
025.11307472
10. Mansur, S., Sattar, K., Hosseini, S. E., Pervez,
S., Ahmad, I., Saleem, K., & Elhendi, A. Z.
(2025). Sales Forecasting for Retail Stores
Using Hybrid Neural Networks and Sales -
Affecting Variables. PeerJ Computer Science,
11, e3058. https://doi.org/10.7717/peerj -
cs.3058
11. Srinivasan, K., Chauhan, G. S., Jadon, R.,
Budda, R., Gollapalli, V. S. T., & Garikipati,
V. (2025). AI-Driven Optimization Models for
E-Commerce Supply Chains: Integrating
HMO, MaxEnt RL, TS, and MDVRP for
Enhanced Demand Forecasting, Inventory
Management, and Delivery Efficiency.
International Journal of Modern Electronics
and Communication Engineering, 13(1).
12. Suresh, B. S., & Suresh, M. (2024). AI-Based
Retail Sales Management: Leveraging
Optimized Metaheuristic Algorithms for
Forecasting and Recommendations. In 2024
Second International Conference on Networks,
Multimedia and Information Technology
(NMITCON). IEEE.
https://doi.org/10.1109/NMITCON62075.2024
.10699202
13. Sharma, H., Sahu, N., Singhal, R. K., Garg,
A., Singhal, R., & Tripathi, S. (2024). Data-
Driven Forecasting and Inventory
Optimization Using Machine Learning Models
and Methods. In 2024 1st International
Conference on Advanced Computing and
Emerging Technologies (ACET). IEEE.
https://doi.org/10.1109/ACET61898.2024.107
30235
14. Howard, E. M. (2024). AI -Based Demand
Sensing: Improving Forecast Accuracy in
Supply Chains. Journal of Informatics
Education and Research, 4(2).
https://doi.org/10.52783/jier.v4i2.1205
15. Nkomo, N., & Mupa, M. N. (2024). The
Impact of Artificial Intelligence on Predictive
Customer Behaviour Analytics in E -
Commerce: A Comparative Study of
Traditional and AI-Driven Models. Iconic
Research and Engineering Journal, 8(5), 432–
452.
16. Rahman, M., Nahar, S., Rahman, M. M.,
Rahman, M. M., & Ullah, M. S. (2023).
Automated Hyperparameter Optimization in
Deep Learning: AI-Driven Approaches for
Model Efficiency and Accuracy. International
Journal of Innovative Research in Computer
and Communication Engineering, 11(09).
https://doi.org/10.15680/IJIRCCE.2023.11090
02
17. Rainy, T. A., Goswami, D., Rabbi, M. S., & Al
Maruf, A. (2023). A Systematic Review of AI-
Enhanced Decision Support Tools in
Information Systems: Strategic Applications in
Service-Oriented Enterprises and Enterprise
Planning. Review of Applied Science and
Technology.
https://doi.org/10.63125/73djw422
18. Suddala, S. (2023). AI -Powered Demand
Forecasting and Inventory Optimization in E-
Commerce Fulfillment Centers. International
Journal of Novel Research and Development,
8(2), d32 –d37.
https://ijnrd.org/papers/IJNRD2302304.pdf
19. Long, L. N. B., Kim, H. S., Cuong, T. N., &
You, S. S. (2023). Intelligent decision support
system for optimizing inventory management
under stochastic events. Applied Intelligence,
53(20), 23675 –23697.
https://doi.org/10.1007/s10489-023-04801-3
20. Wagner, H., & Becker, K. (2022). Decision
Support System for Cloud ML Powers
Strategic Business Choices. International
Journal of Contemporary Research and
Literacy Works, 3(1), 29 –41.
https://ijcrl.com/1/article/view/58

Optimized Artificial Intelligence Framework for Retail Sales Prediction and Decision Support

IJDDT, Volume16  Issue 77s,  2026
Page: 1319
21. Garouani, M., Ahmad, A., Bouneffa , M.,
Hamlich, M., Bourguin, G., & Lewandowski,
A. (2022). Towards big industrial data mining
through explainable automated machine
learning. The International Journal of
Advanced Manufacturing Technology, 120(1),
1169–1188.  https://doi.org/10.1007/s00170-
022-08761-9
22. Vasugi, T. (2022). AI-Optimized Multi-Cloud
Resource Management Architecture for Secure
Banking and Network Environments.
International Journal of Research and Applied
Innovations, 5(4), 7368 –7376.
https://doi.org/10.15662/IJRAI.2022.0504003
23. Khan, M. A., Saleh, A. M., Waseem, M., &
Sajjad, I. A. (2022). Artificial intelligence
enabled demand response: Prospects and
challenges in smart grid environment. IEEE
Access, 11, 1477 –1505.
https://doi.org/10.1109/ACCESS.2022.323144
4
24. Goriparthi, R. G. (2021). Optimizing Supply
Chain Logistics Using AI and Machine
Learning Algorithms. International Journal of
Advanced Engineering Technologies and
Innovations, 1(2), 279-298.
25. Göppert, A., Mohring, L., & Schmitt, R. H.
(2021). Predicting performance indicators with
ANNs for AI-based online scheduling in
dynamically interconnected assembly systems.
Production Engineering, 15(2), 619 –633.
https://doi.org/10.1007/s11740-021-01057-z
