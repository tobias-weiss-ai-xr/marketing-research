---
title: DIGITAL MARKETING IMPACT ON PROMOTION OF KAZAKHSTAN’S AGRO-INDUSTRIAL PRODUCTS
url: https://doi.org/10.48081/btouecon3.2026/101-120
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: Bulletin of Toraighyrov University Economics series
authors:
- S. Zh. Assyl-Keney
- Laura Alimzhanova
- Zh. Zhanatkyzy
source: openalex-oa
pdf_url: https://doi.org/10.48081/btouecon3.2026/101-120
pages: 23
chars: 42827
fetched_at: '2026-11-08T18:36:08+00:00'
kb_version: 1
---

# DIGITAL MARKETING IMPACT ON PROMOTION OF KAZAKHSTAN’S AGRO-INDUSTRIAL PRODUCTS

Торайғыров университетінің
ҒЫЛЫМИ ЖУРНАЛЫ
НАУЧНЫЙ ЖУРНАЛ
Торайгыров университета
ТОР АЙҒЫРОВ
УНИВЕРСИТЕТІНІҢ
ХАБАРШЫСЫ
Экономикалық сериясы
1997 жылдан бастап шығады
ВЕСТНИК
ТОР АЙГЫРОВ
УНИВЕРСИТЕТА
Экономическая серия
Издается с 1997 года
ISSN 2710-3552
№ 3 (2026)
Павлодар

НАУЧНЫЙ ЖУРНАЛ
Торайгыров университета
Экономическая серия
выходит 4 раза в год
СВИДЕТЕЛЬСТВО
о постановке на переучет периодического печатного издания,
информационного агентства и сетевого издания
№ KZ93VPY00029686
выдано
Министерством информации и коммуникаций
Республики Казахстан
Тематическая направленность
публикация материалов в области экономики, управления,
финансов, бухгалтерского учета и аудита
Подписной индекс – 76133
https://doi.org/10.48081/BTOUEcon3.2026/ISSN2710-3552
Бас редакторы – главный редактор
Давиденко Л. М.
доктор PhD
Заместитель главного редактора  Гребнев Л.. С., д.э.н., профессор
Ответственный секретарь   Шеримова Н. М., доктор PhD
Редакция алқасы – Редакционная коллегия
Шмарловская Г. А., д.э.н., профессор (Беларусь);
Кунязов Е. К.,   доктор PhD, доцент;
Алмаз Толымбек,  доктор PhD, профессор (США);
Мукина Г. С.,  доктор PhD,ассоц. профессор, доцент;
Дугалова Г. Н.  д.э.н., профессор
Алтайбаева Ж. К., к.э.н.
Мусина А. Ж.,  к.э.н., ассоц. профессор, доцент;
Титков А. А.,  к.э.н., доцент;
Искакова З. С.  технический редактор.
За достоверность материалов и рекламы ответственность несут авторы и рекламодатели
Редакция оставляет за собой право на отклонение материалов
При использовании материалов журнала ссылка на «Вестник Торайгыров университета» обязательна
© Торайгыров университет

Вестник Торайгыров университета, ISSN 2710-3552                Экономическая серия. № 3. 2026
101
SRSTI 27.17.19
https://doi.org/10.48081/BTOUEcon3.2026/101-120
*S. Zh. Assyl-Keney1, L. M. Alimzhanova2, Zh. Zhanatkyzy3,
J. Kultan4, R. G. Bikmurzin5
1,2,3Al-Farabi Kazakh National University,
Republic of Kazakhstan, Almaty;
4University of Economics in Bratislava,
Slovak Republic, Bratislava;
5Almaty University of Power Engineering and Telecommunications Colledge,
Republic of Kazakhstan, Almaty.
1ORCID: https://orcid.org/0009-0006-3508-914X
2ORCID: https://orcid.org/0000-0002-8172-0493
3ORCID: https://orcid.org/0009-0004-3223-0617
4ORCID: https://orcid.org/0000-0001-6068-9784
5ORCID: https://orcid.org/0009-0006-3524-3135
*e-mail: symbatassylkeney@gmail.com
DIGITAL MARKETING IMPACT ON PROMOTION
OF KAZAKHSTAN’S AGRO-INDUSTRIAL PRODUCTS
This paper develops and numerically investigates a dynamic model
for assessing the effectiveness of digital marketing channels in promoting
agricultural products in Kazakhstan. The model describes the joint
evolution of brand awareness, customer base, and cumulative revenue
under the influence of marketing investments and seasonal demand
fluctuations. The core of the approach is a system of three nonlinear
ordinary differential equations, where the state variables represent brand
awareness A(t), number of active customers C(t), and cumulative revenue
S(t). Digital channels are modeled through control functions ui (t), which
affect both awareness and direct sales, while seasonality is represented
by a sinusoidal component in the awareness equation.
A numerical experiment is carried out for a 24 month planning
horizon with a total digital marketing budget of 10 million KZT, equally
and constantly allocated among three channels (search advertising, social
media, and marketplaces). Under this baseline strategy, brand awareness
increases from 100 to approximately 420 conditional units, the customer

Торайғыров университетінің Хабаршысы, ISSN 2710-3552      Экономикалық серия. № 3. 2026
102
base grows from 50 to about 1 650 active customers, and cumulative
revenue reaches around 1.4 billion KZT equivalent by the end of the period.
The instantaneous revenue rate rises from about 1.3 million KZT per month
at the beginning to over 40 million KZT per month by month 24.
The obtained results demonstrate a pronounced time lag between
awareness growth and revenue acceleration, a saturation effect in the
customer base due to limited market capacity, and a strong seasonal
modulation of short term performance. The proposed model provides a
quantitative basis for scenario analysis and future optimal allocation of
digital marketing budgets in the agri food sector of Kazakhstan.
Keywords: digital marketing, agribusiness, agricultural products,
Kazakhstan, dynamic modeling, system of differential equations, marketing
budget optimization.
Introduction
The development of digital communication channels has radically changed
the way agricultural products are promoted. For Kazakhstan, where a significant
portion of agricultural products are sold through regional markets, wholesale
purchases, and gradually expanding online channels, the task of assessing the
effectiveness of digital marketing is particularly relevant.
Traditional analysis methods (simple cost-to-sales comparisons, static ROMI
models) poorly account for the dynamics of brand awareness, the inertia of
customer base growth, seasonal fluctuations in demand for agricultural products,
and the interaction of various digital channels (search advertising, targeted
advertising, marketplaces).
With limited marketing budgets, it’s important for agricultural businesses to
not only understand the overall return on their digital investments but also to predict
how these investments will translate into awareness, customers, and revenue over
time. This requires a dynamic, rather than static, approach.
This paper proposes a mathematical model based on a system of ordinary
differential equations that describes the evolution of three key metrics: the integrated
brand awareness index, the number of active customers, and accumulated revenue.
The model is specifically adapted to the conditions of Kazakhstan’s agricultural
sector and focuses on the use of data from digital marketing channels.
The contemporary global economy is undergoing profound transformations,
driven by rapid technological advancements, pervasive digitalization, and the
escalating prominence of online business models and social media [1]. This digital
revolution has significantly altered consumer behavior and market dynamics,
compelling industries worldwide, including the agro-industrial complex, to adapt

Вестник Торайгыров университета, ISSN 2710-3552                Экономическая серия. № 3. 2026
103
their promotional strategies [2]. Specifically, the integration of digital marketing
within the agricultural sector offers novel avenues for product promotion, market
expansion, and enhanced engagement with consumers [3; 4].
The shift towards digital platforms necessitates a robust understanding
of various digital marketing channels and their efficacy in reaching diverse
target audiences within the agricultural sector [5]. This research aims to model
the effectiveness of these digital channels for promoting Kazakhstan’s agro-
industrial products, considering the unique challenges and opportunities present
in this emerging market [6]. This study specifically focuses on leveraging digital
marketing strategies to improve the competitiveness of local agricultural products
by identifying effective approaches for expanding market reach and boosting sales
in the digital era [7].
The successful implementation of such strategies often relies on the nuanced
application of modern marketing research methodologies, which are crucial for
understanding global market dynamics and evolving consumer preferences [8].
Furthermore, the adoption of digital marketing strategies can significantly reduce
advertising costs while increasing profitability, thereby contributing to the efficient
use of resources and sustainable development within the agri-food industry
[9]. Given the increasing global consumption of natural food products and the
imperative to enhance the competitiveness of domestic agro-industrial output,
understanding the optimal deployment of digital marketing channels becomes
paramount for mitigating foreign product intervention and bolstering local markets
[10]. This is particularly relevant given that consumers now spend significantly
more time online than with traditional media, making digital platforms crucial for
reaching potential customers [11]. Moreover, the ability of digital marketing to
provide personalized experiences and targeted content through channels like social
media has further reshaped brand-consumer interactions and expectations [12].
This shift mandates that businesses, particularly those within the agro-industrial
complex, optimize their online presence to effectively engage with discerning
consumers [9].
This paradigm shift necessitates a comprehensive review of existing literature
on digital marketing in agriculture, focusing on its impact on brand awareness,
market expansion, and consumer engagement [1; 13]. Specifically, the integration
of innovative digital tools like short videos and immersive live streaming is
gaining traction as a powerful method for marketing agricultural products,
enhancing consumer trust, and driving sales growth by fostering closer farmer-
consumer connections [14]. This approach helps bridge information asymmetry
and allows unique regional agricultural products to reach broader markets with
lower promotional costs compared to traditional advertising methods [15].

Торайғыров университетінің Хабаршысы, ISSN 2710-3552      Экономикалық серия. № 3. 2026
104
Furthermore, digital emotional branding campaigns, particularly through platforms
like Instagram and Facebook, have shown significant potential in fostering deeper
emotional connections with consumers, leading to increased engagement and
substantial sales growth within the agricultural sector [16]. Such strategies enhance
resource efficiency through reduced advertising costs and increased profitability,
a phenomenon observed in established agri-food firms [9]. Moreover, the
increasing accessibility of the internet and its widespread penetration, particularly
in developing regions, underscores the critical role digital marketing plays in
enhancing the visibility and competitiveness of local agribusiness products [17].
The rapid adoption of digital technologies across various sectors highlights
the urgent need for agricultural businesses to embrace digital marketing to
remain competitive and meet evolving consumer demands [11]. Consequently,
agribusinesses must leverage digital marketing to expand their reach, engage with
consumers, and analyze market trends effectively [18]. This includes optimizing
online presence through various digital channels, such as social media, e-commerce
platforms, and emerging technologies like augmented reality and virtual reality,
which offer dynamic engagement opportunities and rich consumer insights [19],
[20]. These digital advancements empower businesses to gather extensive data
on consumer preferences, allowing for highly targeted marketing campaigns and
personalized product offerings that were previously unattainable [11].
The research’s scientific novelty lies in the development of an integrated
dynamic model that, within a single framework, describes the evolution of
awareness, customer base, and revenue, taking into account the influence of
digital channels, forgetting processes, market logistical constraints, conversion,
and the behavior of active customers. This approach fundamentally differs from
static ROMI models in that it is formulated as a system of nonlinear differential
equations, allowing for the tracing of time lags between marketing investments and
financial responses, analyzing saturation and accumulation effects, and examining
the sensitivity of results to parameters. A significant contribution is the inclusion
of a seasonal component in the model, reflecting the specifics of Kazakhstan’s
agricultural markets and allowing for the study of the impact of the temporal
structure of sowing and harvesting cycles on campaign effectiveness. A numerical
experiment with realistic parameters demonstrates the model’s applicability to
agricultural enterprises and provides a foundation for further research in the field
of optimal marketing investment management.
The aim of this study is to develop and numerically test a dynamic model for
assessing the effectiveness of digital marketing channels in promoting Kazakhstan’s
agricultural products. This model allows for a quantitative assessment of the impact
of marketing investments on awareness, customer base, and revenue over time,

Вестник Торайгыров университета, ISSN 2710-3552                Экономическая серия. № 3. 2026
105
taking into account seasonal demand patterns and limited market capacity, and
provides a basis for solving problems of optimally distributing the marketing
budget across digital channels.
Materials and methods
Problem statement
This paper examines the problem of modeling the dynamics of sales of
agricultural products in Kazakhstan under the influence of three main digital
marketing channels, contextual advertising, targeted advertising on social media,
and promotion through marketplaces. The objective function is to maximize the
total revenue of an agricultural enterprise within given budget constraints on
marketing investments.
The specific nature of Kazakhstan’s agro-industrial complex necessitates
accounting for seasonal fluctuations in demand, market saturation effects, time
lags between marketing efforts and consumer responses, and the mutual influence
of channels. Traditional static marketing mix models are unable to adequately
describe these dynamic processes, necessitating the use of differential equations.
We formalize the problem as follows. Let  be the sales volume at time
 be the investment intensities in contextual advertising,
targeted advertising, and marketplaces, respectively. We need to determine the
optimal control action trajectories , that maximize the integrated revenue over
a given time horizon  subject to constraints on the total marketing budget.
Mathematical model
Sales dynamics are described by a system of nonlinear ordinary differential
equations reflecting the processes of consumer awareness formation, conversion
to purchases, and natural customer churn.
Let’s introduce the phase variables.  is the target audience’s awareness
of agricultural products (potential customers reached by marketing messages).
 is the number of active customers (those who have made a purchase and are
in the database).  is the cumulative revenue.
The system of differential equations is as follows:
where the model parameters  are the efficiency coefficients of channel i in
generating awareness, reach per unit of investment,  is the coefficient of natural

Торайғыров университетінің Хабаршысы, ISSN 2710-3552      Экономикалық серия. № 3. 2026
106
brand forgetting,  is the amplitude of seasonal fluctuations in demand typical
for the agro-industrial complex of Kazakhstan,  is the seasonality period
(12 months),  is the coefficient of awareness conversion into active customers,
 is the market capacity, the maximum number of potential customers, μ is the
customer churn coefficient,  is the average revenue per active customer per unit
of time,
  are the coefficients of the direct contribution of channel i to revenue
(for example, through direct sales on marketplaces).
The model describes a process in which awareness is generated linearly
by control signals , taking into account natural forgetting  and
the influence of seasonal fluctuations in demand. The customer base evolves
logistically, with saturation at  and gradual attrition . Revenue
accumulates as a result of existing customer activity and the direct contribution of
the marketing channels used, forming an integral indicator of system performance.
Modeling parameters
For numerical modeling, fixed parameter values are used, in conditional
but realistic units for the agro-industrial complex of Kazakhstan. The
effectiveness of channels by awareness , , . Brand
forgetting  Seasonality ,  months. Conversion of
awareness into customers . Market capacity . Customer
churn  Revenue per customer and direct contribution of channels
Initial conditions  Budget constraint
 The optimal control problem is
formulated as maximization of the functional:
              (2)
where  is a regularization parameter that penalizes excessive investment
volatility.
The total marketing budget for horizon T is assumed to be fixed
thousand tenge.
In this numerical experiment, a simple strategy is adopted: the budget is
spent uniformly over time and equally across three channels. Then, the average
investment intensity in each channel is
The numerical value of  thousand tenge per month per
channel.
This study utilized synthetic data obtained using the author’s dynamic model,
a system of ordinary differential equations. All numerical experiments were
conducted in the Python environment. Real statistical data on the performance of

Вестник Торайгыров университета, ISSN 2710-3552                Экономическая серия. № 3. 2026
107
agricultural enterprises was not used in the numerical modeling; the parameters
were selected to provide realistic estimates of awareness, customer base, and
revenue.
Solution method
To solve the problem numerically, we use the direct Cauchy problem approach.
We fix the control variables  and integrate the system of differential equations using
the fourth-order Runge-Kutta method over the time interval  This allows
us to obtain the trajectories of the phase variables  for a given
investment strategy.
In the right-hand sides of the equations, constants  are substituted instead
of . With constants , the system takes the form:
                                (3)
Let us substitute the total coefficients

Then:
                           (4)
The system is integrated on the interval  using the 4th order
Runge–Kutta method with an adaptive step:

                   (5)
Internally, the method uses the following iterative scheme for each step

Торайғыров университетінің Хабаршысы, ISSN 2710-3552      Экономикалық серия. № 3. 2026
108
with subsequent construction of two approximations of different orders and
automatic selection of the step
To display the results, the solution values are additionally interpolated onto
a uniform grid of 500 points
Results and discussion
The numerical solution shows a steady growth of the function A(t) from the
initial level A(0) = 100 (see Fig. 1). In the early part of the integration, the growth
is due to the dominance of the positive contribution from constant investments
in the channels , over the decaying term
 The seasonal term  generates oscillations around an
increasing trend trajectory.
Interpretatively, this means that with a constant intensive budget on all three
digital channels, brand awareness of the Kazakh agricultural enterprise increases
significantly, while the A(t) trajectory shows annual seasonality, typical for
agricultural products.

Вестник Торайгыров университета, ISSN 2710-3552                Экономическая серия. № 3. 2026
109
Figure 1 – Dynamics of the awareness function A(t) obtained from
the numerical integration of the model under a uniform allocation
of the digital marketing budget. The trajectory demonstrates monotonic
growth with superimposed seasonal oscillations induced
by the sinusoidal term in the awareness equation
In Figure 2, the customer base C(t) also grows monotonically from the initial
level C(0) = 50. The growth rate at the early stage is low, which is reflected in the
close values of C(t) for small t, but as A(t) increases, the influx of new customers
increases due to the term  while C(t) is far from the maximum
market capacity  At the same time, the outflow  acts, which
stabilizes the growth of the customer base and, in the long term, leads to reaching
a quasi-stationary state determined by the balance of inflow and outflow.
In essence, this corresponds to the following: digital marketing channels,
by raising awareness, generate a steady flow of new customers, at the same time,
some customers naturally leave, which hinders unlimited growth.
Figure 2 – Evolution of the customer base C(t)
over the 24-month horizon

Торайғыров университетінің Хабаршысы, ISSN 2710-3552      Экономикалық серия. № 3. 2026
110
The  function (see Fig. 3) is the integral of the current revenue flow
 Even with slow growth of C(t), revenue grows almost
linearly with an increasing slope. The first term, 25C(t), increases as the customer
base expands. The second term,  is fixed and reflects direct sales through
channels (e.g., marketplaces).
The figure 3  shows an upward convex curve: the rate of revenue
accumulation increases over time as the customer base strengthens.
Figure 3 – Accumulated revenue S(t) as the integral of the instantaneous
revenue flow. The curve exhibits upward convexity, reflecting
the accelerating contribution of the expanding customer base combined
with the constant revenue from direct digital-channel effects
Figure 4 illustrates the phase portrait of the system in the (A(t), C(t))-plane,
demonstrating a monotonic expansion of the customer base as brand awareness
increases, with gradually diminishing marginal gains as the market capacity is
approached.
As the integrated awareness indicator A(t) grows, the customer base C(t)
expands monotonically. The trajectory has a characteristic convex shape: in the
early stages, a small increase in awareness yields a limited increase in customers.
Then, upon reaching a certain level of A(t), the sensitivity of C(t) to changes in
awareness increases, and as market capacity approaches, growth gradually slows.

Вестник Торайгыров университета, ISSN 2710-3552                Экономическая серия. № 3. 2026
111
Figure 4 – Phase portrait of the system in the (A(t),C(t)) plane.
The trajectory illustrates a monotonic increase in the customer
base as awareness grows, with diminishing marginal returns
as the system approaches the market capacity
Figure 5 presents the evolution of the instantaneous revenue rate  The
trajectory exhibits an increasing trend, driven primarily by the expansion of the
active customer base, while the direct contribution of digital channels ensures a
non-zero baseline revenue level throughout the planning horizon.
At the beginning of the horizon, the value of instantaneous revenue is small
because the customer base is small. As C(t) increases, the contribution of the
term leads to a nearly monotonic increase in  The constant component associated
with the direct contribution of channels (the term ), sets a non-
zero baseline level of cash flow, even with a low customer base.

Торайғыров университетінің Хабаршысы, ISSN 2710-3552      Экономикалық серия. № 3. 2026
112
Figure 5 – Instantaneous revenue rate  showing a steady
increase throughout the planning horizon. The growth is primarily
driven by the expansion of the active customer base,
while digital channel contributions maintain
a non-zero baseline revenue level
Figure 6 depicts the purely seasonal term in the awareness dynamics equation.
The sinusoidal pattern with a 12-month period captures the seasonality typical for
the agricultural sector, superimposed on the long-term growth trend induced by
digital marketing investments.
This figure visualizes the purely seasonal element in the awareness equation,
that is, the function . The seasonal component is strictly periodic
with an annual cycle (12 months) and determines regular fluctuations in the rate of
change in awareness. Combined with constant marketing influence, this leads to
sinusoidal fluctuations superimposed on the overall upward trend A(t), reflecting
the seasonal specificity of demand for agricultural products.

Вестник Торайгыров университета, ISSN 2710-3552                Экономическая серия. № 3. 2026
113
Figure 6 – Seasonal component of the awareness dynamics,
represented by the function . The annual
sinusoidal pattern captures the seasonality characteristic of agricultural
markets and modulates the overall growth trend
Numerical modeling shows that the awareness metric A(t) exhibits a steady
upward trend over the entire 24-month horizon. This is driven by two factors:
first, ongoing investments in digital channels (constant u1, u2, u3), and second, the
relatively low forgetting coefficient
This trend is superimposed by pronounced fluctuations generated by the
seasonal term  The amplitude of these fluctuations is significant
relative to the current level of A(t), so that in certain periods, even with constant
marketing expenditures, the rate of change in awareness may decrease or transition
to a short-term decline.
The customer base C(t) grows monotonically, starting from a small initial
level. In the early stages (the first few months), growth is slow: awareness is
still low, and the term  yields a relatively small influx of new
customers.
As A(t) increases, the impact of marketing intensifies, and the rate of
customer influx increases. However, a saturation mechanism is simultaneously
at work: the coefficient  gradually decreases, reflecting the approach to

Торайғыров университетінің Хабаршысы, ISSN 2710-3552      Экономикалық серия. № 3. 2026
114
the market’s maximum capacity. Churn  creates an additional stabilizing
effect: at a sufficiently high level of C(t), net customer growth declines, and the
system tends toward a quasi-stationary regime in which influx and churn are, on
average, balanced.
The S(t) (accumulated revenue) graph grows convexly upward: the slope of
the curve increases over time. This reflects the fact that the instantaneous cash
flow  depends on C(t) and, accordingly, increases as the customer base expands.
The phase portrait of C(t) versus A(t) demonstrates a characteristic S-like
dependence on the trajectory: at low values of A(t), even a significant increase in
awareness yields a limited increase in C(t), at medium values of A(t), the increase
in customers is maximum; at high A(t), the curve straightens out, reflecting market
saturation.
This is important from a decision-making perspective for two reasons. First,
the model quantitatively demonstrates that the impact of additional investments in
awareness on customer base growth depends significantly on the current position on
the curve in the middle zone, customer retention is highest. Second, once awareness
levels reach high levels, further budget increases on the same channels will be less
effective in terms of customer growth; at this stage, strategies focused on retention
and increasing lifetime value (LTV) become more rational than broad reach.
A separate graph of the seasonal component reveals a clear annual cycle.
Combined with the dynamics of A(t) and C(t), this allows us to draw an important
conclusion: with a constant level of investment in digital channels, the actual
system response (in terms of increased awareness, customer acquisition, and
revenue) varies significantly depending on the point in time.
Conclusion
Numerical modeling conducted for a 24-month horizon and a total marketing
budget of 10 million tenge, evenly distributed between three digital channels,
yielded the following key results.
The model shows a significant increase in integrated awareness. From
an initial level of , by the end of the period, awareness reaches
approximately  conventional units. This is a more than fourfold
increase in two years with a constant level of investment. This trend exhibits
annual fluctuations due to a seasonal term with an amplitude of , which
corresponds to the pronounced seasonality of demand for agricultural products.
The number of active clients increases from  to approximately
 clients. Thus, by the end of two years, the client base has grown
more than 30-fold, while remaining significantly below the market’s maximum
capacity of  This means that, even with the chosen basic strategy,

Вестник Торайгыров университета, ISSN 2710-3552                Экономическая серия. № 3. 2026
115
significant potential for further growth remains, and saturation effects are only
just beginning to appear.
Cumulative revenue demonstrates significant accelerating growth.
With an initial value of , by the end of the horizon, total revenue
reaches approximately  thousand tenge, or approximately
1.4 billion tenge. Instantaneous cash flow  increases from approximately
1.3–1.5 million tenge per month at the beginning of the period to more than
40 million tenge per month by the end of the second year, reflecting the cumulative
effect of the expanding customer base.
The phase portrait in the (A,C) plane demonstrates a monotonic, convex
trajectory, indicating that: in the early stages, additional growth in awareness yields
a limited increase in the customer base, in the middle zone, the greatest sensitivity
of C(t) to changes in A(t) is observed; as market capacity approaches, the return
on customers decreases, and the task of retention and increasing profitability per
customer comes to the fore.
Explicitly accounting for seasonality in the equations demonstrates that the
effectiveness of identical investments in digital marketing varies significantly
depending on the time period. Investments made during the positive phase of the
seasonal sine wave lead to faster growth in awareness and, consequently, higher
customer base and revenue growth than the same investments made during the
unfavorable phase.
With a simple strategy of evenly distributing the budget, consistent
investments in digital marketing provide significant growth in awareness, customer
base, and revenue in Kazakhstan’s agricultural sector. However, fully realizing
the market potential requires more flexible management.
The time lag between increased awareness and accelerated revenue growth
should be taken into account when assessing the ROI of campaigns: short-term
indicators may underestimate the long-term impact of investments.
Limited market capacity and customer churn lead to diminishing returns
in customer numbers, which justifies a shift from broad coverage strategies to
retention and LTV-increasing strategies as the market becomes saturated.
Seasonality significantly impacts the effectiveness of digital campaigns;
planning marketing activities without taking seasonal phases into account leads
to a distorted assessment of channel effectiveness.
The proposed model and the numerical results obtained provide a foundation
for further research, including defining and solving optimal marketing budget
management problems, calibrating parameters using real data from Kazakhstani
agricultural enterprises, and comparing alternative digital investment allocation
strategies.

Торайғыров университетінің Хабаршысы, ISSN 2710-3552      Экономикалық серия. № 3. 2026
116
The proposed dynamic model can be adapted to analyze the digital marketing
effectiveness of a specific agricultural enterprise. To do this, simply estimate the
model parameters based on the company’s internal data (channel costs, customer
acquisition funnel, sales dynamics) and set actual budget constraints and target
market capacity. As a result, the model can be used to predict the impact of
alternative marketing budget allocation strategies and select the most effective
digital channel configuration.
REFERENCES
1 Sheeraz, M., Sajid, M. S., Mehmood, Y., Irfan, M., Tahir, I. Brand
Awareness and Digital Marketing: Measurement Tools and Data Analytics for
Agricultural Industry // Journal of Arable Crops and Marketing. – 2023. – Vol. 5.
– № 2. – P. 37.  – https://doi.org/10.33687/jacm.005.01.5047.
2 Zarubina, V., Zarubin, M., Yessenkulova, Z., Salimbayeva, R.,
Satbaeva, G. Digital transformation of the promotion of educational services of
Kazakhstani universities // Journal of Innovation and Entrepreneurship. – 2024.
– Vol. 13. – № 1. – https://doi.org/10.1186/s13731-023-00355-3.
3 Borisova, L., Baranova, I., Bruzhukova, O. Digital Marketing: Drivers
for the Development of the Russian Agricultural Sector // Proceedings of the 2nd
International Scientific and Practical Conference «Modern Management Trends
and the Digital Economy: from Regional Development to Global Economic
Growth» (MTDE 2020). – 2020. – https://doi.org/10.2991/aebmr.k.200502.028.
4 Yu, X., Sheng, G., Sun, D., He, R. Effect of digital multimedia on the
adoption of agricultural green production technology among farmers in Liaoning
Province, China // Scientific Reports. – 2024. – Vol. 14. – № 1. – https://doi.
org/10.1038/s41598-024-64049-w.
5 Ciasullo, M. V., Montera, R., Mercuri, F., Mugova, Sh. When
Digitalization Meets Omnichannel in International Markets: A Case Study from
the Agri-Food Industry // Administrative Sciences. – 2022. – Vol. 12. – № 2. –
 P. 68. – https://doi.org/10.3390/admsci12020068.
6 Fedyaeva, A., Babintseva, A., Lezhnina, O., Egorova, A. A. Evaluating
the effectiveness of integrated marketing communications while implementing a
CRM system in the agricultural industry // E3S Web of Conferences. – 2021. –
Vol. 258. – P. 6061. – https://doi.org/10.1051/e3sconf/202125806061.
7 Ningsih, G. M., Rasyid, H. A., Ningsih, N., Pujotomo, D., Suseno, G. P.
Agricultural Marketing Strategies In The Digital Era: Improving The
Competitiveness Of Local Products // Journal of Social Science (JoSS). – 2024.
– Vol. 3. – № 9. – P. 1756. – https://doi.org/10.57185/joss.v3i9.366.

Вестник Торайгыров университета, ISSN 2710-3552                Экономическая серия. № 3. 2026
117
8 Valieva, A. Directions for Effective Use of Modern Marketing Research in
Increasing the Export of Leguminous Products // International Journal of Social
Science Research and Review. – 2024. – Vol. 7. – № 9. – P. 13. – https://doi.
org/10.47814/ijssrr.v7i9.2190.
9 Kanellos, Ν., Karountzos, P., Giannakopoulos, N. T., Terzi, M. C.,
Sakas, D. P. Digital Marketing Strategies and Profitability in the Agri-Food
Industry: Resource Efficiency and Value Chains // Sustainability. – 2024. – Vol. 16.
– № 14. – P. 5889. – https://doi.org/10.3390/su16145889.
10 Akzholova, M., Osmonova, A. Digitization of marketing activities of
agricultural entrepreneurship in the conditions of the Kyrgyz Republic // IOP
Conference Series Earth and Environmental Science, IOP Publishing. – 2019. –
P. 12114. – https://doi.org/10.1088/1755-1315/395/1/012114.
11 Nandhini, S. U., Thinakaran, J., Kavitham, V., Navaneetham, B. Digital
Marketing for Global Agricultural Produce: Success in the Digital Era // Agricultural
Science Digest – A Research Journal. – 2025. – https://doi.org/10.18805/ag.d-5967.
12 Haris, A. The Role of Marketing Research in Understanding Consumer
Behavior and Preferences // Advances in Business & Industrial Marketing
Research. – 2024. – Vol. 2. – № 2. – https://doi.org/10.60079/abim.v2i2.259.
13 Xu, W., Xu, Q., Xu, M., Che, P. Digital Marketing’s Impact on Rural
Agricultural Products’ Market Expansion // Advances in Social Science, Education
and Humanities Research/Advances in social science, education and humanities
research. – 2024. – P. 1081. – https://doi.org/10.2991/978-2-38476-277-4_120.
14 Xu, X., Chen, M. Short Video + Immersive Live Streaming’ Assists in
Marketing Strategies for Agricultural and Rural Products // International Journal of
Global Economics and Management. – 2024. – Vol. 4. – № 1. – P. 506. – https://
doi.org/10.62051/ijgem.v4n1.60.
15 Zhu, B., Ping, X., Wang, K. A Multi-group Analysis of Gender Difference
in Consumer Buying Intention of Agricultural Products via Live Streaming //
Research on World Agricultural Economy. – 2023. – Vol. 4. – № 1. – P. 25. –
https://doi.org/10.36956/rwae.v4i1.789.
16 Anwar, M., Megasari, D., Atasa, D., Kartika, D. S. Y., Mandasari, V.
Leveraging Digital Emotional Branding in Transforming the Agricultural Industry
// Nusantara Science and Technology Proceedings. – 2025. – P. 443. – https://doi.
org/10.11594/nstp.2025.4765.
17 Waluyo, T. Digital Marketing Strategy for Local Agribusiness Products
in Indonesia. – 2022. – Vol. 1. – № 1. – P. 64. – https://doi.org/10.58471/ju-sosak.
v1i01.539.
18 Dasic, D., Vucic, V., Turcinovic, Z., Tosic, M.  Digital marketing
– marketing opportunities and the power of digital consumers // Ekonomika

Торайғыров университетінің Хабаршысы, ISSN 2710-3552      Экономикалық серия. № 3. 2026
118
poljoprivrede. – 2023. – Vol. 70. – № 4. – P. 1187. – https://doi.org/10.59267/
ekopolj23041187d.
19 Imran, M., Ferdous, J. Cultivating Connections: Leveraging Digital
Innovation to Engage Gen Z in Agricultural Marketing // SSRN Electronic Journal.
– 2025. – https://doi.org/10.2139/ssrn.5171775.
20 Cai, T. Analysis of Digital Marketing Strategies in the Pet Food
Industry: A Comparative Study of Different Brands // Advances in Economics
Management and Political Sciences. – 2025. – Vol. 151. – № 1. – P. 89. – https://
doi.org/10.54254/2754-1169/2024.19411.
            Received 02.12.25.
            Received in revised form 24.02.26.
            Accepted for publication 01.06.26.
*С. Ж. Асыл-Кеней1, Л. М. Алимжанова2, Ж. Жанатқызы3,
Я. Култан4, Р. Г. Бикмурзин5
1,2,3әл-Фараби атындағы Қазақ ұлттық университеті,
Қазақстан Республикасы, Алматы қ,;
4Братислава Экономика университеті,
Словакия Республикасы, Братислава;
5Алматы энергетика және байланыс университеті колледжі,
Қазақстан Республикасы, Алматы қ.
02.12.25 ж. баспаға түсті.
24.02.26 ж. түзетулерімен түсті.
01.06.26 ж. басып шығаруға қабылданды.
ҚАЗАҚСТАНДА АГРОӨНЕРКӘСІПТІК ӨНІМДЕРДІҢ
ІЛГЕРІЛЕТУГЕ ЦИФРЛЫҚ МАРКЕТИНГТІҢ ӘСЕРІ
Бұл жұмыс Қазақстанда ауылшаруашылық өнімдерін
ілгерілетудегі цифрлық маркетинг арналарының тиімділігін
бағалаудың динамикалық моделін әзірлейді және сандық түрде
зерттейді. Модель маркетингтік инвестициялар мен маусымдық
сұраныс ауытқуларының әсерінен бренд туралы хабардарлықтың,
тұтынушылар базасының және жиынтық кірістің бірлескен
эволюциясын сипаттайды. Әдістің өзегі үш сызықты емес кәдімгі
дифференциалдық теңдеулер жүйесі болып табылады, мұнда
күй айнымалылары бренд туралы хабардар болу A(t), белсенді
тұтынушылар саны C(t) және жиынтық кіріс S(t) көрсетеді.

Вестник Торайгыров университета, ISSN 2710-3552                Экономическая серия. № 3. 2026
119
Сандық арналар u i (t) басқару функциялары арқылы модельденеді,
олар хабардарлыққа да, тікелей сатуға да әсер етеді, ал маусымдық
хабардарлық теңдеуінде синусоидалы компонент көрсетіледі.
Цифрлық маркетингтің жалпы бюджеті 10 миллион теңгені
құрайтын 24 айлық жоспарлау көкжиегі үшін сандық эксперимент
үш арнаға (іздеу жарнамасы, әлеуметтік медиа және базарлар)
бірдей және тұрақты бөлінген. Осы базалық стратегия аясында
бренд туралы хабардарлық 100-ден шамамен 420 шартты бірлікке
дейін артады, тұтынушы базасы 50-ден шамамен 1650 белсенді
тұтынушыға дейін өседі және жиынтық табыс кезеңнің соңына
қарай шамамен 1,4 млрд теңге баламасына жетеді. Лездік кіріс
деңгейі басында айына шамамен 1,3 миллион теңгеден 24 айға қарай
40 миллион теңгеден асады.
Алынған нәтижелер хабардарлықтың өсуі мен кірістің
жылдамдауы, шектеулі нарық сыйымдылығына байланысты
тұтынушылар базасындағы қанықтыру әсері және қысқа мерзімді
өнімділіктің күшті маусымдық модуляциясы арасындағы айқын
уақыттық кідірісті көрсетеді. Ұсынылып отырған модель сценарийді
талдау және Қазақстанның агроазық-түлік секторындағы цифрлық
маркетингтік бюджеттерді болашақта оңтайлы бөлу үшін сандық
негізді қамтамасыз етеді.
Кілтті сөздер: цифрлық маркетинг, агробизнес, ауылшаруашылық
өнімдері, Қазақстан, динамикалық модельдеу, дифференциалдық
теңдеулер жүйесі, маркетингтік бюджетті оңтайландыру.
*С. Ж. Асыл-Кеней1, Л. М. Алимжанова2, Ж. Жанатқызы3,
Я. Култан4, Р. Г. Бикмурзин5
1,2,3Казахский национальный университет имени аль-Фараби,
Республика Казахстан, г. Алматы;
4Братиславский экономический университет,
Словацкая Республика, г. Братислава;
5Колледж Алматинского университета энергетики и связи,
Республика Казахстан, г. Алматы.
Поступило в редакцию 02.12.25.
Поступило с исправлениями 24.02.26.
Принято в печать 01.06.26.

Торайғыров университетінің Хабаршысы, ISSN 2710-3552      Экономикалық серия. № 3. 2026
120
ВЛИЯНИЕ ЦИФРОВОГО МАРКЕТИНГА
НА ПРОДВИЖЕНИЕ АГРОПРОМЫШЛЕННОЙ
ПРОДУКЦИИ КАЗАХСТАНА
В данной работе разработана и численно исследована динамическая
модель оценки эффективности цифровых маркетинговых каналов в
продвижении сельскохозяйственной продукции в Казахстане. Модель
описывает совместную динамику узнаваемости бренда, клиентской
базы и совокупного дохода под влиянием маркетинговых инвестиций
и сезонных колебаний спроса. В основе подхода лежит система
трёх нелинейных обыкновенных дифференциальных уравнений, где
переменные состояния представляют узнаваемость бренда A(t),
количество активных клиентов C(t) и совокупный доход S(t). Цифровые
каналы моделируются с помощью управляющих функций ui(t), которые
влияют как на узнаваемость, так и на прямые продажи, а сезонность
представлена синусоидальный компонент в уравнении узнаваемости.
Численный эксперимент проводится для горизонта планирования
24 месяца с общим бюджетом на цифровой маркетинг в размере
10 миллионов тенге, равномерно и постоянно распределяемым
между тремя каналами (поисковая реклама, социальные сети и
маркетплейсы). В рамках данной базовой стратегии узнаваемость
бренда увеличивается со 100 до примерно 420 условных единиц,
клиентская база увеличивается с 50 до примерно 1650 активных
клиентов, а совокупный доход к концу периода достигает около
1,4 миллиарда тенге в эквиваленте. Мгновенный доход увеличивается
с примерно 1,3 миллиона тенге в месяц в начале до более чем
40 миллионов тенге в месяц к 24-му месяцу.
Полученные результаты демонстрируют выраженный временной
лаг между ростом узнаваемости и ускорением роста выручки,
эффект насыщения клиентской базы ввиду ограниченной емкости
рынка и сильную сезонную модуляцию краткосрочных показателей.
Предложенная модель обеспечивает количественную основу для
анализа сценариев и оптимального распределения бюджетов на
цифровой маркетинг в агропродовольственном секторе Казахстана
в будущем.
Ключевые слова: цифровой маркетинг, агробизнес,
сельскохозяйственная продукция, Казахстан, динамическое
моделирование, система дифференциальных уравнений, оптимизация
маркетингового бюджета.

Теруге 07.09.2026 ж. жiберiлдi. Басуға 30.09.2026 ж. қол қойылды.
Электронды баспа
3,25 Mb RAM
Шартты баспа табағы 30,2
Компьютерде беттеген: З. С. Искакова
Корректоры: А. Р. Омарова, Д. А. Кожас
Тапсырыс № 4598
Сдано в набор 07.09.2026 г. Подписано в печать 30.09.2026 г.
Электронное издание
3,25  Mb RAM
Усл.п.л. 30,2
Компьютерная верстка: З. С. Искакова
Корректорлар: А. Р. Омарова, Д. А. Кожас
Заказ № 4598
«Toraighyrov University» баспасынан басылып шығарылған
Торайғыров университеті
140008, Павлодар қ., Ломов к., 64, 137 каб.
«Toraighyrov University» баспасы
Торайғыров университеті
140008, Павлодар қ., Ломов к., 64, 137 каб.
8 (7182) 67-36-69
e-mail: kereku@tou.edu.kz
www.vestnik.tou.edu.kz
www.vestnik-economic.tou.edu.kz
