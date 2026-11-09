---
title: Battery Sales Forecasting Using ARIMA at Store X for Monthly Data Based on Battery Brand
url: https://doi.org/10.58578/mikailalsys.v4i3.12126
category: brand
subcategory: framework
date: 2026-09
venue: Journal of Multidisciplinary Science MIKAILALSYS
authors:
- Rafi Argya Darma Herdiyanto
- Seftin Fitri Ana Wati
- Mohammad Al Hafidz
source: openalex-oa
pdf_url: https://ejournal.yasin-alsys.org/mikailalsys/article/download/12126/8827/12126.pdf
pages: 13
chars: 33350
fetched_at: '2026-11-08T18:58:28+00:00'
kb_version: 1
---

# Battery Sales Forecasting Using ARIMA at Store X for Monthly Data Based on Battery Brand

Volume 4, Issue 3, 2026; Pages 6943-6955
https://ejournal.yasin-alsys.org/mikailalsys
Jurnal         Mikailalsys is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
 e-ISSN : 2987-2286
 p-ISSN : 2987-3924
Index: Harvard, Boston,
Sydney, Copernicus, Sinta 4,
Scilit, Semantic, Google, etc

https://doi.org/10.58578/mikailalsys.v4i3.12126

Battery Sales Forecasting Using ARIMA at Store X
for Monthly Data Based on Battery Brand

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati,
Mohammad Al Hafidz
Universitas Pembangunan Nasional Veteran Jawa Timur, Indonesia
argya12darma@gmail.com; seftin.fitri.si@upnjatim.ac.id

Submitted: Revised: Accepted: Published:
Aug 4, 2026 Sep 1, 2026 Sep 13, 2026 Sep 18, 2026

Abstract

Demand uncertainty poses a persistent challenge for sales planning and
inventory management in retail businesses, particularly when products exhibit
heterogeneous sales patterns across brands. This study aims to develop brand -
specific vehicle battery sales  forecasting models using the Autoregressive
Integrated Moving Average (ARIMA) method. The study follows the Cross -
Industry Standard Process for Data Mining (CRISP -DM) framework,
comprising Business Understanding, Data Understanding, Data Preparation,
Modeling, and Evaluation. Historical sales transaction data from Toko Aki Restu
covering July 2016 to July 2026 were aggregated into monthly sales series for
nine battery brands and divided into training and testing sets using an 80:20 ratio.
Model development  involved stationarity assessment using the Augmented
Dickey-Fuller test, preliminary model identification through the Autocorrelation
Function and Partial Autocorrelation Function, and parameter combination
selection using Grid Search. Forecasting performance was evaluated using Mean
Absolute Error (MAE), Root Mean Square Error (RMSE), and Mean Absolute
Percentage Error (MAPE). The findings indicate that the optimal ARIMA
specification varies across battery brands, reflecting differences in their
underlying sales patterns. GS ASTRA MF achieved the lowest MAE and RMSE,
whereas AMARON recorded the lowest MAPE among the evaluated brands.
The selected models were subsequently used to forecast monthly sales for a 12-
month period from August 2026 to July 2027. Th ese findings demonstrate that
brand-specific ARIMA modeling can accommodate heterogeneous sales
characteristics and provide differentiated forecasts for vehicle battery products.
The study contributes a systematic forecasting approach that can support more

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
 Journal of Multidisciplinary Sciences
6944
informed sales planning and inventory management by aligning forecasting
models with the time-series characteristics of individual brands.
Keywords: ARIMA; Battery Sales; Grid Search; Sales Forecasting; Time Series

INTRODUCTION
Sales forecasting is one of the important aspects in managing operational activities in
retail businesses because forecasting results can be used as a basis for estimating product
needs and supporting purchasing planning. Demand uncertainty can cause companies to face
inventory conditions that do not match market needs. Excessive inventory can increase
storage costs, while insufficient inventory can increase the risk of product shortages.
Therefore, the ability to estimate sales based on historical patterns is one of the factors that
can support decision-making in retail operations management. (Ramos et al., 2015) explain
that sales forecasting plays an important role in various retail operational decisions, including
purchasing planning and inventory management. In addition, the characteristics of sales data
arranged sequentially over time make it suitable for analysis using a time series approach.
This problem is also found at Store X, which is engaged in vehicle battery sales.
Demand for batteries from various brands changes over time, so the sales volume in a given
period is not always the same. This condition can complicate the planning process i f
purchasing decisions are based solely on sales from the previous period without considering
the overall historical pattern. The transaction data available for the period July 2016 to July
2026 shows sales data that can be utilized to build a forecasting model. In this study, the
transaction data was then aggregated into monthly sales data based on brand in order to
obtain a more structured time series that could be used in the modeling process. The brand-
based aggregation approach was chosen because the study focuses on the demand patterns
of each battery brand, rather than on individual product or battery type level (Kim et al.,
2023).
One method that can be used to forecast time series data is the Autoregressive
Integrated Moving Average (ARIMA). ARIMA is a method that utilizes the relationship
between past observation values and forecasting errors to produce predictions for the next
period. The use of ARIMA in sales forecasting has been applied in various business contexts.
(Saputra, 2024), for example, used monthly sales data and applied the Augmented Dickey -

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
Volume 4, Issue 3, 2026
 6945
Fuller (ADF) test, Autocorrelation Function (ACF), and Partial Autocorrelation Function
(PACF) in the process of forming an ARIMA model. The results show that ARIMA can be
used to model sales data based on time series characteristics. Research by (Ramos et al., 2015)
also shows that ARIMA can be used to forecast retail sales and evaluate forecasting
performance using error measures such as Root Mean Square Error (RMSE), Mean Absolute
Error (MAE), and Mean Absolute Percentage Error (MAPE)(Atesongun & Gulsen, 2024).
Nevertheless, the selection of ARIMA model parameters is an important part of
producing an appropriate forecasting model. Parameter identification through ACF and
PACF can provide an initial indication of the autoregressive (p) and moving average (q)
orders, but the correlation patterns in time series data do not always provide a single
parameter combination that can be directly established as the best model. Therefore, a
systematic search approach can be used to compare several parameter combinations.
(Hasanudin & Mujiyono, 2026) applied Grid Search to ARIMA modeling for monthly sales
forecasting and used a combination of evaluation criteria in determining the appropriate
model. This approach shows that systematic parameter search can help reduce subjectivity
in model selection. Thus, the use of ACF and PACF as initial identification followed by Grid
Search can provide a more systematic modeling process in determining ARIMA parameter
combinations(Chen, 2023).
Based on the previous research above, some studies have applied ARIMA for sales
forecasting and used prediction error -based evaluation, while other studies have developed
systematic parameter search through Grid Search. However, the application of this approach
specifically to battery sales data based on brand with a long historical period still has room
for further study. In addition, the sales characteristics of each brand can differ, so using a
single identical model for all brands may not necessarily produce an optimal level of accuracy.
Therefore, a modeling process is needed that allows each brand to obtain an ARIMA
configuration based on the characteristics of its own data(Kurnia et al., 2025; Kusuma et al.,
2018).
The novelty of this study lies in the application of ARIMA modeling separately for
each battery brand using monthly sales data for the period July 2016 to July 2026. The
modeling process was carried out systematically through the stages of Augmented Dickey-
Fuller to determine the level of stationarity, ACF and PACF to obtain initial parameter
indications, and Grid Search to evaluate combinations of the p and q parameters (Syabrina,

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
 Journal of Multidisciplinary Sciences
6946
2022). The resulting models were then evaluated using MAE, RMSE, and MAPE on the
testing data, so that model selection was not only based on fit to the training data, but also
considered the model's ability to produce predictions on data not used during the tra ining
process. This evaluation approach using out -of-sample data is also in line with the research
of (Ramos et al., 2015), which evaluated ARIMA model performance based on out-of-sample
data.
This study focuses on forecasting monthly battery sales based on nine brands, namely
AMARON, BOSCH, BOSCHAGM, DELKOR, FURUKAWA BATTERY, GS ASTRA,
GS ASTRA MF, RCA BATTERY, and SUPREME. The data consists of 121 monthly
observations for each brand and is divided using a proportion of 80% training data and 20%
testing data. The purpose of this study is to build an appropriate ARIMA model for each
brand, evaluate model performance based on MAE, RMSE, and MAPE, and produce sales
forecasts for the  following period. The results of the study are expected to provide an
overview of the ability of the ARIMA method to model battery sales patterns based on brand
and serve as a basis of information for research and decision -making related to sales
forecasting in the retail business.(Eşidir et al., 2022)

METHODS
This study uses a quantitative approach with a time series analysis method to forecast
battery sales at Toko Aki Restu. The research framework refers to the Cross -Industry
Standard Process for Data Mining (CRISP -DM), which consists of six stages: Business
Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and
Deployment.(Wang et al., 2024)  However, this study focuses on the stages up to the
forecasting process and model evaluation, so the research results are directed toward
obtaining the best ARIMA model for each battery brand.(Nagalakshmi et al., 2025)
The data used is battery sales transaction data from Toko Aki Restu for the period
July 2016 to July 2026. The initial data consisted of transaction data containing battery sales
information, which was then selected and cleaned to ensure consistency in bra nd naming.
After the data preparation process, sales transactions were grouped by brand and aggregated
into monthly sales data. Aggregation was carried out because the procurement and sales
planning patterns of the research object are more relevant to analyze on a monthly basis.
Based on the grouping results, the study uses nine battery brands, namely AMARON,

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
Volume 4, Issue 3, 2026
 6947
BOSCH, BOSCHAGM, DELKOR, FURUKAWA BATTERY, GS ASTRA, GS ASTRA
MF, RCA BATTERY, and SUPREME. Each brand has 121 monthly observations, which
are then used as a time series in the modeling process. (Maslim et al., 2020; Sumitra & Sidqi,
2024)
In the Data Preparation stage, the monthly data was divided into training data and
testing data with an 80:20 ratio. This division resulted in 97 observations for training data
and 24 observations for testing data for each brand. The training data was used to build and
determine the ARIMA model parameters, while the testing data was used to determine the
model's ability to produce predictions on data not used during the model formation process.
The data division was carried out based on time order so that the time series characteristics
were maintained and no mixing occurred between past data and data to be predicted.(Ensafi
et al., 2022)
The Modeling stage was carried out using the Autoregressive Integrated Moving
Average (ARIMA) method, represented in the form ARIMA(p,d,q). The parameter p
indicates the autoregressive order, d indicates the level of differencing, while q indicates the
moving average order. The value of d was determined through the Augmented Dickey-Fuller
(ADF) test to test data stationarity. If the data was already stationary at the level, then d = 0
was used, while data that was not yet stationary required a differencing process. After the
level of integration was determined, the Autocorrelation Function (ACF) and Partial
Autocorrelation Function (PACF) were used as an initial analysis to identify possible p and
q orders. The use of ACF and PACF provides an overview of the relationship between
observations at several lags and helps determine appropriate candidate models.(Hidayatullah
et al., 2025)
To obtain a more systematic parameter combination, the study then applied Grid
Search to the values of p and q. Testing was carried out over a range of values from 0 to 15
for each parameter, while the value of d was set based on the ADF test results. Each
parameter combination that met the modeling criteria was compared based on the Akaike
Information Criterion (AIC) value and the forecasting error performance on the testing data.
This approach was used to reduce subjectivity in parameter selection and obtain the model
most suited to the characteristics of each brand(Syabrina, 2022).
The Evaluation stage was carried out by comparing the model's forecasting results
with the actual values in the testing data. Three metrics were used to measure model

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
 Journal of Multidisciplinary Sciences
6948
performance: Mean Absolute Error (MAE), Root Mean Square Error (RMSE), and Mean
Absolute Percentage Error (MAPE). MAE was used to measure the average absolute value
of prediction errors, RMSE imposes a larger penalty on large prediction errors, while MAPE
indicates the magnitude of prediction error as a percentage. The use of these three metrics
allows evaluation to be carried out from both absolute and relative error perspectives. The
best model for each brand was determined based on a combination of model selection results
and forecasting error values on the testing data.(Nusamandiri & Rianto, 2025)
After the best model was obtained for each brand, the model was used to generate
sales forecasts for the following period. The forecasting results were used as an estimate of
the sales development of each brand based on the historical patterns learned by the model.
Thus, the research stages produced the best ARIMA model for each brand,  MAE, RMSE,
and MAPE evaluation values, and sales forecasts for the upcoming period.

RESULTS
ARIMA Modeling Results
Based on the results of processing monthly sales data for the nine battery brands, all
time series were tested for stationarity using the Augmented Dickey-Fuller (ADF) test. The
test results show that the data for each brand was stationary at the level, so the differencing
value used was d = 0. Next, initial identification of the autoregressive order ( p) and moving
average order (q) was carried out using ACF and PACF.
The candidate models obtained were then systematically tested using Grid Search
with a range of p and q values from 0 to 15. The model search results produced different
ARIMA combinations for each brand. This difference shows that the sales pattern
characteristics are not entirely the same between brands, so using a single identical model for
all brands was not the approach used in this study.
Table  1. Best ARIMA Model for Each Brand
Brand ARIMA Model AIC
AMARON ARIMA(4,0,4) 655,908
BOSCH ARIMA(0,0,3) 608,006
BOSCHAGM ARIMA(2,0,2) 462,003
DELKOR ARIMA(3,0,3) 573,018
FURUKAWA BATTERY ARIMA(2,0,1) 610,301
GS ASTRA ARIMA(0,0,2) 522,080

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
Volume 4, Issue 3, 2026
 6949
Brand ARIMA Model AIC
GS ASTRA MF ARIMA(2,0,4) 494,019
RCA BATTERY ARIMA(3,0,3) 622,604
SUPREME ARIMA(1,0,9) 537,972

Table 1 best ARIMA model for each brand  shows that the best model differs for
each brand. The ARIMA(4,0,4) model was obtained for AMARON, while BOSCH produced
ARIMA(0,0,3). BOSCHAGM used ARIMA(2,0,2), DELKOR and RCA BATTERY used
ARIMA(3,0,3), while FURUKAWA BATTERY produced ARIMA(2,0,1). GS AST RA
produced ARIMA(0,0,2), GS ASTRA MF produced ARIMA(2,0,4), and SUPREME
produced ARIMA(1,0,9).
Forecast Evaluation Results
The ARIMA models obtained were then evaluated using 24 observations from the
testing data. Evaluation was carried out using MAE, RMSE, and MAPE to determine the
level of prediction error for each model.
Table  2. ARIMA Model Evaluation Results
Brand MAE RMSE MAPE
AMARON 5,50 6,74 13,26%
BOSCH 3,90 4,63 18,96%
BOSCHAGM 2,00 2,60 39,36%
DELKOR 3,60 4,14 30,97%
FURUKAWA BATTERY 4,50 5,75 15,53%
GS ASTRA 2,70 3,82 30,58%
GS ASTRA MF 1,90 2,31 41,24%
RCA BATTERY 4,50 5,00 16,59%
SUPREME 2,80 3,71 26,43%
Based on Table 2 ARIMA model evaluation results , GS ASTRA MF produced the
lowest MAE and RMSE values, at 1.90 and 2.31 respectively. Meanwhile, AMARON
produced the lowest MAPE value at 13.26%, followed by FURUKAWA BATTERY at
15.53% and RCA BATTERY at 16.59%. These results show that model performance ca n
differ depending on whether it is viewed based on absolute or relative error measures.
As shown in Table 2 ARIMA model evaluation esults , the relatively high MAPE
values for some brands, such as GS ASTRA MF at 41.24% and BOSCHAGM at 39.36%,
do not directly indicate that their prediction errors are the largest in absolute terms. This can
be seen from the RMSE value of GS ASTRA MF, which is in fact the lowest, at 2.31. This

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
 Journal of Multidisciplinary Sciences
6950
difference occurs because MAPE measures error relative to actual values, so it can produce
a high percentage for data with relatively small sales values. Therefore, the interpretation of
model performance in this study takes MAE, RMSE, and MAPE into account together.
Sales Forecasting Results
The best model for each brand was then used to generate sales forecasts for the next
12 periods, namely August 2026 to July 2027. The forecasting results provide an estimate of
monthly sales volume for each brand based on the historical patterns learned by the ARIMA
model.

Figure 1. Results ARIMA Forecasting

Figure 1 results ARIMA forecasting illustrates the ARIMA forecasting results for the
nine battery brands over the 12-month forecasting horizon from August 2026 to July 2027.
The forecasts represent the expected monthly sales volumes generated from the best ARIMA
model selected for each brand based on the preceding modeling and evaluation stages. The
figure provides a comparative view of the predicted sales patterns across brands, allowing
the variation in forecast levels and trends to be observed over the forecasting period. As an
illustration, the AMARON model predicts sales of 44.7 units in August 2026, followed by
44.2 units in September, 43.9 units in October, and 42.0 units in November, indicating a
relatively stable pattern with a gradual decline. Similar forecasts were generated for the other
brands according to their respective ARIMA configurations, resulting in a total of 108
monthly predictions. These forecasting results indicate that the selected ARIMA models can
be used to estimate future sales based on the historical characteristics of each brand, while
the differences in forecast patterns further reflect the distinct sales behavior observed across

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
Volume 4, Issue 3, 2026
 6951
the battery brands. The implications of these forecasting results are further discussed in the
following section.

DISCUSSION
The results show that the ARIMA model obtained differs for each battery brand.
This difference can be seen in the parameter combinations selected, namely AMARON using
ARIMA(4,0,4), BOSCH ARIMA(0,0,3), BOSCHAGM ARIMA(2,0,2), DELKOR
ARIMA(3,0,3), FURUKAWA BATTERY ARIMA(2,0,1), GS ASTRA ARIMA(0,0,2), GS
ASTRA MF ARIMA(2,0,4), RCA BATTERY ARIMA(3,0,3), and SUPREME
ARIMA(1,0,9). These differences in models show that sales pattern characteristic s are not
entirely the same across brands, so using a single ARIMA configuration for all brands is not
appropriate. This finding is in line with research by (Suryawan et al., 2024), which shows that
forecasting model performance can differ according to the characteristics of the sales data
analyzed. That study also shows that ARIMA can provide good performance on certain sales
data compared to other alternative methods.(Husein et al., 2021)
The model identification stage in this study began with stationarity testing using the
Augmented Dickey-Fuller (ADF) test. The test results show that all nine brand sales series
were stationary at the level, so the differencing value used was d=0. After that, ACF and
PACF were used to obtain an initi al overview of the possible autoregressive order (p) and
moving average order (q). The use of ADF, ACF, and PACF in the ARIMA model
identification process has also been used in previous sales research, particularly to determine
differencing needs and identify initial model parameters (Simanungkalit, 2024). Thus, the
identification stages used in this study are consistent with the general approach to ARIMA
modeling of monthly sales data.
The initial identification results through ACF and PACF were then followed by Grid
Search to obtain a more systematic combination of the p and q parameters. In this study, the
values of p and q were tested over a range of 0 to 15, while the value of d was set based on
the stationarity test results. This approach was used to reduce reliance on parameter selection
based solely on visual interpretation of ACF and PACF. Grid Search allows a number of
model combinations to be tested and compared based on predetermined criteria. The use of
systematic parameter search has also been found in sales fore casting research that utilizes

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
 Journal of Multidisciplinary Sciences
6952
parameter search to obtain a model configuration with better performance (Hasanudin &
Mujiyono, 2026).
Evaluation on the testing data shows differences in accuracy levels between brand s.
The GS ASTRA MF model produced an MAE of 1.90 and an RMSE of 2.31, which are the
lowest values compared to other brands. Meanwhile, AMARON produced the lowest MAPE
value at 13.26%. These differences in results show that there is no single error measure that
comprehensively describes model performance across all brands. MAE and RMSE indicate
the magnitude of prediction error in sales data units, while MAPE indicates error as a
percentage. The simultaneous use of MAE, RMSE, and MAPE has also been used in
ARIMA-based sales forecasting research to provide an overview of model performance from
several evaluation perspectives (Simanungkalit, 2024; Suryawan et al., 2024).
One finding that needs attention is the relatively high MAPE value for some brands,
even though their MAE and RMSE values are relatively low. GS ASTRA MF, for example,
produced an MAE of 1.90 and an RMSE of 2.31, but had a MAPE of 41.24%. This condition
shows that errors in unit terms may appear small, but when calculated relative to a low actual
value, the resulting error percentage can become larger. Therefore, the interpretation of
MAPE for data with relatively small sales values needs to be done carefully and should not
be used as the sole basis for determining model quality. In contrast, AMARO N had the
lowest MAPE at 13.26%, but its RMSE of 6.74 was higher than that of GS ASTRA MF.
These results show that different evaluation measures can provide different perspectives on
model performance.
Differences in performance between brands also reinforce the importance of
modeling separately at the brand level. The research data was not treated as a single overall
sales series, but was formed into nine series based on brand. This approach allows the
characteristics of each brand to be preserved during the identification and modeling process.
This is relevant because previous research has shown that ARIMA performance can vary
depending on the characteristics of the category or sales series used (Brykin, 2024). Thus, the
results of this study support the use of ARIMA models tailored to the characteristics of each
brand rather than applying a single identical model to all data.
The forecasting results for the next twelve months show that the resulting models
can be used to generate sales estimates for each brand for the period August 2026 to July
2027. The use of these forecasting results can provide quantitative information on t he

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
Volume 4, Issue 3, 2026
 6953
demand trends of each brand, which can serve as a consideration in sales planning. Research
by (Suryawan et al., 2024)  also shows that sales forecasting results can be used to help
companies anticipate changes in demand and support sales-related decision-making.
Although it provides results that can be used for forecasting, this study has several
limitations. The ARIMA model used only utilizes historical sales patterns and does not yet
incorporate external variables such as price, promotions, economic conditions, or changes
in consumer preferences. In addition, the study was conducted at the brand level using data
that had been aggregated monthly. This aggregation helps produce a more consistent time
series, but causes sales variation at the individual type or product level not to be analyzed
directly. Future research could consider the use of external variables through models such as
ARIMAX or compare ARIMA with other methods, including LSTM, Prophet, or hybrid
models. Research by Suryawan et al. (2024) and Brykin (2024) shows that comparing ARIMA
with other methods can provide additional information on model suitability for different
data characteristics.

CONCLUSION
This study successfully applied the Autoregressive Integrated Moving Average
(ARIMA) method to forecast battery sales at the brand level at Toko Aki Restu using the
CRISP-DM framework. Based on the stationarity test results, all sales data from the nine
brands were stationary at the level, so the differencing value used was d=0. The ACF and
PACF identification process, followed by Grid Search, produced different ARIMA models
for each brand, na mely ARIMA(4,0,4) for AMARON, ARIMA(0,0,3) for BOSCH,
ARIMA(2,0,2) for BOSCHAGM, ARIMA(3,0,3) for DELKOR, ARIMA(2,0,1) for
FURUKAWA BATTERY, ARIMA(0,0,2) for GS ASTRA, ARIMA(2,0,4) for GS ASTRA
MF, ARIMA(3,0,3) for RCA BATTERY, and ARIMA(1,0,9) for SUPREME.
Evaluation results using the testing data show that model performance differs for
each brand. The GS ASTRA MF model produced the lowest MAE and RMSE values, at
1.90 and 2.31 respectively, while the AMARON model produced the lowest MAPE at
13.26%. These res ults show that the ARIMA model is able to produce different levels of
error according to the characteristics of each sales series. The resulting models were then
used to generate sales forecasts for 12 months, namely the period from August 2026 to July
2027.(Ferdinansyah et al., 2026)

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
 Journal of Multidisciplinary Sciences
6954
This study contributes by applying ARIMA modeling individually to nine battery
brands using monthly sales data for the period July 2016 to July 2026. This approach allows
the characteristics of each brand to be preserved during the modeling process and produces
different models suited to the data patterns. The forecasting results can serve as supporting
information for Toko Aki Restu in understanding the sales trends of each brand in the
upcoming period.
Future research could develop the model by considering external variables that may
affect sales, such as price, promotions, seasons, or economic conditions. In addition, future
research could compare ARIMA with other forecasting methods or hybrid approaches to
determine the method most suited to the characteristics of battery sales data. The use of data
at the type or product level could also be considered if the number of observations and data
consistency are sufficient.

REFERENCES
Atesongun, A., & Gulsen, M. (2024). A hybrid forecasting structure based on ARIMA and
artificial neural network models. Applied Sciences, 14 (16), 7122.
https://doi.org/10.3390/app14167122
Brykin, D. (2024). Sales forecasting models: Comparison between ARIMA, LSTM and
Prophet. Journal of Computer Science, 20 (10), 1222 –1230.
https://doi.org/10.3844/jcssp.2024.1222.1230
Chen, C. (2023). A method for sales prediction based on time series. In Proceedings of the 2nd
International Conference on Information Economy, Data Modeling and Cloud Computing (ICIDC
2023). EAI. https://doi.org/10.4108/eai.2-6-2023.2334677
Ensafi, Y., Hassanzadeh Amin, S., Zhang, G., & Shah, B. (2022). Time-series forecasting of
seasonal items sales using machine learning —A comparative analysis. International
Journal of Information Management Data Insights, 2 (1), 100058.
https://doi.org/10.1016/j.jjimei.2022.100058
Eşidir, K. A., Gür, Y. E., Yoğunlu, V., & Çubuk, M. (2022). Yapay sinir ağları (YSA) ve
ARIMA modelleri ile Türkiye’de aylık sıfır km otomobil satış adetlerinin tahmin
edilmesi. Pamukkale Üniversitesi İşletme Araştırmaları Dergisi, 9 (2), 260 –277.
https://doi.org/10.47097/piar.1132101
Ferdinansyah, E. T., Roffi, M., Ramadhan, R., & Prasiwiningrum, E. (2026). Comparative
analysis of ARIMA and Facebook Prophet algorithms for e-commerce product sales
forecasting. Collabits, 3(1), 87–95. https://doi.org/10.22441/collabits.v3i1.37651
Hasanudin, M., & Mujiyono, S. (2026). Peramalan Penjualan Mitra Konsinyasi Menggunakan
SARIMA Berbasis Grid Search dan Evaluasi Akurasi. Jurnal Algoritma, 23 (1), 329–
341. https://doi.org/10.33364/algoritma/v.23-1.3147
Hidayatullah, A., Wulandari, D., & Ramadhani, N. W. (2025). Penggunaan Prediksi Akurasi
Forecasting Menggunakan Metode ARIMA dan Holt-Winters pada Penjualan (Studi
Empiris pada PT. Karunia Alam Segar Tahun 2020–2024). E-Jurnal Akuntansi TSM,
5(3), 145–158. https://doi.org/10.34208/ejatsm.v5i3.2917

Rafi Argya Darma Herdiyanto, Seftin Fitri Ana Wati, Mohammad Al Hafidz
Volume 4, Issue 3, 2026
 6955
Husein, A. M., Lubis, F. R., & Harahap, M. K. (2021). Analisis Prediktif untuk Keputusan
Bisnis: Peramalan Penjualan. Data Sciences Indonesia, 1 (1).
https://doi.org/10.47709/dsi.v1i1.1196
Kim, H.-J., Kim, J.-H., & Im, J.-B. (2023). Forecasting offline retail sales in the COVID -19
pandemic period: A case study of a complex shopping mall in South Korea. Buildings,
13(3), 627. https://doi.org/10.3390/buildings13030627
Kurnia, Y., Yakub, Arijanto, R., Layanda, W., & Dwi Putra, D. S. (2025). Web-based car sales
prediction system using the ARIMA (Autoregressive Integrated Moving Average)
model for optimizing automotive marketing strategies. RUBINSTEIN, 4(1), 44–56.
https://doi.org/10.31253/rubin.v4i1.4039
Kusuma, A. K. Q. W., Prasetyo, E., & Zainal, R. F. (2018). Shoes sales forecasting using
Autoregressive Integrated Moving Average (ARIMA) (case study UD. Wardana
Mojokerto). JEECS (Journal of Electrical Engineering and Computer Sciences), 3 (2), 467–
478. https://doi.org/10.54732/jeecs.v3i2.134
Maslim, M., Ernawati, & Arinanda, K. (2020). Motorcycle parts sales forecasting using auto-
regressive integrated moving average model. International Journal of Computer Theory and
Engineering, 12(1), 28–31. https://doi.org/10.7763/IJCTE.2020.V12.1259
Nagalakshmi, M. V. N., Sai Sri Charan, Y. V. N., Reddy, P. C., Jadhav, P. D., Pillai, D., &
Dogra, A. K. (2025). Sales forecasting and demand prediction through time series
analysis and machine learning. International Journal of Applied Mathematics, 38 (6s).
https://doi.org/10.12732/ijam.v38i6s.656
Sunendar, N., & Rianto, Y. (2025). Comparison of ARIMA, LSTM, and GRU models for
forecasting sales of HIT aerosol products. Jurnal Pilar Nusa Mandiri, 21(2), 153–159.
https://doi.org/10.33480/pilar.v21i2.6412
Ramos, P., Santos, N., & Rebelo, R. (2015). Performance of state space and ARIMA models
for consumer retail sales forecasting. Robotics and Computer-Integrated Manufacturing, 34,
151–163. https://doi.org/10.1016/j.rcim.2014.12.015
Saputra, B. H. (2024). Evaluation of ARIMA model performance in projecting future sales:
Case study on electronic products. Jurnal Teknik Informatika C.I.T Medicom, 16(5), 275–
283. https://doi.org/10.35335/cit.Vol16.2024.993.pp329-337
Simanungkalit, E. (2024). Evaluation of ARIMA model performance in projecting future
sales: Case study on electronic products. Journal of Intelligent Decision Support System
(IDSS), 7(4), 309–317. https://doi.org/10.35335/idss.v7i4.274
Sumitra, I. D., & Sidqi, F. (2024). Predicting selling product of single variant using ARIMA,
trend analysis, and single exponential smoothing methods (case study: Swalayan XYZ
Store). International Journal of Informatics, Information System and Computer Engineering, 5(1),
43–52. https://doi.org/10.34010/injiiscom.v5i1.12486
Suryawan, I. G. T., Putra, I. K. N., Meliana, P. M., & Sudipa, I. G. I. (2024). Performance
comparison of ARIMA, LSTM, and Prophet methods in sales forecasting. Sinkron:
Jurnal dan Penelitian Teknik Informatika, 8 (4), 2410 –2421.
https://doi.org/10.33395/sinkron.v8i4.14057
Wang, C., Stupina, A., & Bezhitskiy, S. (2024). Online sales prediction approach using
methodology of CRISP -DM. ITM Web of Conferences, 59 , 01006.
https://doi.org/10.1051/itmconf/20245901006
