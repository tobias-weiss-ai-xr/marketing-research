---
title: 'Beyond Point Forecasts: A Survey on Probabilistic Forecasting for Time Series and Spatiotemporal
  Data'
url: https://arxiv.org/abs/2609.13345
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Donia Besher
- Rajdeep Pathak
- Madhurima Panja
- Tanujit Chakraborty
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.13345
pages: 77
chars: 309626
fetched_at: '2026-11-08T13:29:51+00:00'
kb_version: 1
---

# Beyond Point Forecasts: A Survey on Probabilistic Forecasting for Time Series and Spatiotemporal Data

Preprint
Beyond Point Forecasts: A Survey on Probabilistic Forecast-
ing for Time Series and Spatiotemporal Data
Donia Besher1 A00021999@sorbonne.ae
Rajdeep Pathak1,2 rajdeep.pathak@sorbonne.ae
Madhurima Panja1 madhurima.panja@sorbonne.ae
Tanujit Chakraborty1,2 tanujit.chakraborty@sorbonne.ae
1SAFIR, Sorbonne University Abu Dhabi, United Arab Emirates
2SCAI, Sorbonne Université, Paris, France
Abstract
Probabilistic forecasting is central to decision-making under uncertainty, yet its method-
ological landscape has become increasingly fragmented across temporal and spatiotem-
poral forecasting, statistical modeling, machine learning, and deep generative modeling.
This survey develops a unified perspective by organizing probabilistic forecasting meth-
ods according to where and how uncertainty is introduced into the forecasting pipeline.
Our taxonomy connects model-agnostic approaches including ensembles and distribution-
free calibration, with model-intrinsic approaches spanning Bayesian modeling, parametric
predictive distributions, distributional regression, and modern generative models, and fur-
ther examines the emerging role of time series foundation models. Beyond methodologi-
cal synthesis, we identify the assumptions, computational demands, and forms of uncer-
tainty represented by different paradigms, and translate these distinctions into data-driven
and domain-specific guidance for method selection. We complement the survey with a
cross-paradigm empirical study on univariate, multivariate, and spatiotemporal forecast-
ing tasks. The results reveal that no single uncertainty-quantification paradigm dominates
across settings. Calibration, sharpness, predictive accuracy, and computational efficiency
can lead to substantially different model preferences, while expressive generative models
and zero-shot foundation models exhibit markedly different accuracy-efficiency trade-offs.
Lastly, we identify unresolved challenges surrounding uncertainty in evolving dependency
structures, physics-informed predictive distributions, forecasting extreme events, handling
count-valued, directional, and continuous-time series, and the development of unified soft-
ware resources. Our survey provides both a conceptual framework and a practical roadmap
for probabilistic forecasting research. Code and supporting materials are available at
https://github.com/PyCoder913/ProbForecasting.
Contents
1 Introduction 4
1.1 Background and Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 Literature Review 8
3 Model-Agnostic Uncertainty Quantification 10
1
arXiv:2609.13345v1  [stat.ML]  11 Sep 2026

Preprint
3.1 Pre-Control Limits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.2 Ensemble-Based Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.2.1 Resampling-Based Ensembles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.2.2 Randomization-Based Ensembles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.2.3 Deep Ensembles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.2.4 Bayesian Model Averaging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.3 Distribution-Free Calibration Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.3.1 Conformal Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.3.2 Conformalized Quantile Regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4 Model-Intrinsic Uncertainty Quantification 15
4.1 Bayesian Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.1.1 Classical Bayesian Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.1.1.1 Bayesian Hierarchical Models. . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.1.1.2 Bayesian State Space Models. . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.1.2 Bayesian Nonparametric Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.1.2.1 Gaussian Processes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.1.2.2 Dirichlet Processes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.1.2.3 Bayesian Additive Regression Trees. . . . . . . . . . . . . . . . . . . . . . . . 19
4.1.3 Bayesian Neural Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.1.4 Approximate Bayesian Inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.1.4.1 Markov Chain Monte Carlo. . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.1.4.2 Monte Carlo Dropout. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.1.4.3 Variational Inference. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.1.4.4 Integrated Nested Laplace Approximation. . . . . . . . . . . . . . . . . . . . 21
4.2 Parametric Predictive Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
4.2.1 Single Parametric Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
4.2.2 Mixture Density Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.3 Distributional Regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.3.1 Quantile Regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.3.2 Engression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.3.3 Loss-Driven Interval Estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.4 Generative Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.4.1 Copula-Based Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.4.2 Hidden Markov Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.4.3 Hierarchical Discretization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.4.4 Variational Autoencoders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
2

Preprint
4.4.5 Generative Adversarial Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.4.6 Normalizing Flows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.4.7 Diffusion Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.4.7.1 Denoising Diffusion Probabilistic Models. . . . . . . . . . . . . . . . . . . . . 33
4.4.7.2 Score-Based Diffusion Models. . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.4.7.3 Latent Diffusion Models. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.4.8 Parametric Prior Mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.4.9 Scenario-Based Probabilistic Forecasting . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5 Foundation Models for Probabilistic Forecasting 35
5.1 Uncertainty Quantification in Foundation Models . . . . . . . . . . . . . . . . . . . . . . . . . 36
5.2 From Temporal to Spatiotemporal Foundation Models . . . . . . . . . . . . . . . . . . . . . . 37
6 Evaluation and Model Selection 38
6.1 Data Resources and Software Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
6.1.1 Datasets and Evaluation Benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
6.1.2 Open-Source Libraries and Repositories . . . . . . . . . . . . . . . . . . . . . . . . . . 38
6.2 Probabilistic Evaluation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
6.3 Robustness and Statistical Significance Tests . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
6.4 Method Guidance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
6.4.1 Data-Driven Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
6.4.2 Domain-Specific Method Guidance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
7 Empirical Demonstration 46
7.1 Temporal Forecasting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
7.2 Spatiotemporal Forecasting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
7.3 Analysis of Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
8 Challenges and Future Directions 51
8.1 Open Challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
8.2 Future Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
9 Conclusion 54
3

Preprint
1 Introduction
Forecasting plays a key role in decision-making across epidemiology, energy systems, transportation, finance,
and environmental monitoring (Hyndman & Athanasopoulos, 2021). In many of these application domains,
however, a single prediction of the future is insufficient as decisions depend critically on the uncertainty
surrounding that prediction (Gneiting & Katzfuss, 2014). For instance, health authorities planning hospital
capacity require reliable uncertainty estimates for future case counts (Stojanović et al., 2019; Karami et al.,
2026b); power-system operators must account for uncertainty when balancing supply and demand (Hong &
Fan, 2016; Xie et al., 2023); financial risk management depends on the tails of predictive distributions rather
thanexpectedoutcomes(Adrianetal.,2019;Blascoetal.,2024); environmentalandhydrologicalapplications
require reliable assessment of rare events such as floods (Pasche & Engelke, 2024; Papacharalampous &
Tyralis, 2022); and transportation systems rely on uncertainty-aware forecasts of congestion and travel times
(Cheng et al., 2024; Pal et al., 2021). These requirements motivate probabilistic forecasting, whose objective
is to characterize the range and likelihood of possible future outcomes instead of providing a single-point
prediction.
These challenges become substantially more pronounced when moving from time series to spatiotemporal
forecasting. Even in purely temporal settings, predictive uncertainty is shaped by serial dependence, nonsta-
tionarity, and the propagation of uncertainty across forecast horizons. Spatiotemporal problems additionally
require accounting for interactions across variables and locations, where the underlying dependency structure
may be complex, asymmetric, time-varying, and influenced by external drivers. In practice, these difficulties
are further compounded by rare but consequential extremes that may invalidate conventional distributional
assumptions (Coles, 2001). Probabilistic forecasting in such contexts must therefore characterize uncertainty
while respecting the temporal and spatial structure of the data. Their quality is consequently governed by
the complementary principles of calibration and sharpness, which require predictive distributions to be sta-
tistically reliable yet sufficiently informative (Gneiting et al., 2007). These challenges have motivated a broad
and rapidly evolving range of probabilistic forecasting methodologies.
We organize these methods into two overarching paradigms according towhere and how uncertainty is
introduced into the forecasting pipeline:model-agnosticandmodel-intrinsicapproaches. Model-agnostic
methods quantify uncertainty around the predictions of an existing forecasting model without fundamentally
modifying its architecture or learning objective. Early approaches often relied on independent and identically
distributed (i.i.d.) Gaussian residuals and fixed-width prediction intervals (Panja et al., 2023), whereas
subsequentdevelopmentsintroducedresampling, ensembleaggregation(Elliottetal.,2013), anddistribution-
free calibration through conformal prediction (Angelopoulos & Bates, 2023). In contrast, model-intrinsic
methods learn predictive uncertainty as part of the forecasting model itself. These approaches range from
parametric predictive distributions (Salinas et al., 2020) and Bayesian formulations (Qiu et al., 2018; Coscia
et al., 2025) to distributional regression (Koenker & Bassett, 1978) and increasingly expressive generative
models (Rasul et al., 2021a;b). More recently, time series foundation models have introduced a new setting
in which probabilistic forecasts may be produced with little or no task-specific training, raising important
questions regarding calibration, transferability, and their extension to structured spatiotemporal systems.
Despite this methodological breadth, the corresponding survey literature remains surprisingly fragmented.
Foundational papers establish the principles of probabilistic forecasting (Gneiting & Katzfuss, 2014), while
other existing works tend to emphasize specific model families (Gao et al., 2022; Chakraborty et al., 2024;
Yang et al., 2026), study uncertainty quantification without explicitly addressing temporal and spatial de-
pendence (Abdar et al., 2021; Gawlikowski et al., 2023), review forecasting architectures while placing greater
emphasis on deterministic prediction (Lim & Zohren, 2021; Benidis et al., 2022; Wang et al., 2022), or focus
on particular application domains (Yuan & Li, 2021; Kaur et al., 2022; Papacharalampous & Tyralis, 2022;
Xie et al., 2023; Eggen et al., 2026). As detailed in Section 2, these perspectives provide substantial depth
individually, but none offers a unified, architecture-agnostic treatment of probabilistic forecasting that si-
multaneously spans temporal and spatiotemporal settings. As a result, developments that address the same
underlying forecasting problem often remain separated across statistical, machine learning, spatiotemporal,
and application-specific literatures.
4

Preprint
Probabilistic
Forecasting
Model-Agnostic
Methods (Sec. 3)
Pre-Control Limits
(Sec. 3.1)
Ensemble-Based Methods
(Sec. 3.2)
Resampling-Based Ensembles (Sec. 3.2.1)
Randomization-Based Ensembles (Sec. 3.2.2)
Deep Ensembles (Sec. 3.2.3)
Bayesian Model Averaging (Sec. 3.2.4)
Distribution-Free
Calibration (Sec. 3.3)
Conformal Prediction (Sec. 3.3.1)
Conformalized Quantile Regression (Sec. 3.3.2)
Model-Intrinsic
Methods (Sec. 4)
Bayesian Modeling
(Sec. 4.1)
Classical Bayesian Models (Sec. 4.1.1)
Bayesian Hierarchical
Models (Sec. 4.1.1.1)
Bayesian State Space
Models (Sec. 4.1.1.2)
Bayesian Nonparametric Methods (Sec. 4.1.2)
Gaussian Processes
(Sec. 4.1.2.1)
Dirichlet Processes
(Sec. 4.1.2.2)
Bayesian Additive
Regression Trees
(Sec. 4.1.2.3)
Bayesian Neural Networks (Sec. 4.1.3)
Approximate Bayesian Inference (Sec. 4.1.4)
Markov Chain Monte
Carlo (Sec. 4.1.4.1)
Monte Carlo Dropout
(Sec. 4.1.4.2)
Variational Inference
(Sec. 4.1.4.3)
Integrated Nested
Laplace Approximation
(Sec. 4.1.4.4)
Parametric Predictive
Distributions (Sec. 4.2)
Single Parametric Distributions (Sec. 4.2.1)
Mixture Density Networks (Sec. 4.2.2)
Distributional Regression
(Sec. 4.3)
Quantile Regression (Sec. 4.3.1)
Engression (Sec. 4.3.2)
Loss-Driven Interval Estimation (Sec. 4.3.3)
Generative Models
(Sec. 4.4)
Copula-Based Models (Sec. 4.4.1)
Hidden Markov Models (Sec. 4.4.2)
Hierarchical Discretization (Sec. 4.4.3)
Variational Autoencoders (Sec. 4.4.4)
Generative Adversarial Networks (Sec. 4.4.5)
Normalizing Flows (Sec. 4.4.6)
Diffusion Models (Sec. 4.4.7)
Denoising Diffusion
Probabilistic Models
(Sec. 4.4.7.1)
Score-Based Diffusion
Models (Sec. 4.4.7.2)
Latent Diffusion
Models (Sec. 4.4.7.3)
Parametric Prior Mapping (Sec. 4.4.8)
Probabilistic Scenarios (Sec. 4.4.9)
Foundation
Models (Sec. 5)
Evaluation &
Model Selection
(Sec. 6)
Data Resources &
Software Tools (Sec. 6.1)
Datasets & Evaluation Benchmarks (Sec. 6.1.1)
Open-Source Libraries & Repositories (Sec. 6.1.2)
Probabilistic Evaluation
Metrics (Sec. 6.2)
Robustness & Statistical
Significance Tests
(Sec. 6.3)
Method Guidance
(Sec. 6.4)
Data-Driven Selection (Sec. 6.4.1)
Domain-Specific Guidance (Sec. 6.4.2)
Empirical
Demonstration
(Sec. 7)
Temporal Forecasting
(Sec. 7.1)
Spatiotemporal
Forecasting (Sec. 7.2)
Analysis of
Results (Sec. 7.3)Challenges & Future Directions
(Sec. 8)
Figure 1: Taxonomy and overview of the survey on probabilistic forecasting methods for time series and
spatiotemporal data.
5

Preprint
This survey aims to bridge these literatures. Rather than organizing methods primarily by forecasting ar-
chitecture or application domain, we classify them according to the mechanism through which predictive
uncertainty is represented and estimated. The resulting taxonomy, illustrated in Fig. 1, connects model-
agnostic and model-intrinsic approaches for uncertainty quantification. Representative methods are summa-
rized in Table 1. Importantly, our objective is not merely to catalogue existing techniques, but to analyze
the assumptions and trade-offs that distinguish them. Specifically, we analyze the type of uncertainty they
represent, the structural assumptions they impose, their computational requirements, calibration properties,
and the forecasting domains in which they are most appropriate. Our main contributions are summarized
as follows:
•A unified methodological view of probabilistic forecasting.We connect classical statis-
tical approaches with recent machine learning developments through a taxonomy based on the
mechanism used to represent predictive uncertainty. The survey spans model-agnostic calibration,
Bayesian modeling, parametric predictive distributions, distributional regression, and modern gen-
erative approaches, while comparing their assumptions, design choices, computational properties,
and limitations. We further examine probabilistic time series foundation models and discuss the
methodological challenges involved in extending them to spatiotemporal forecasting.
•From methodological taxonomy to practical model selection.We complement the review
with benchmark datasets, open-source model implementations, probabilistic evaluation measures,
and statistical comparison procedures. More importantly, we synthesize the methodological differ-
ences into two complementary guidance frameworks: a data-driven framework in Fig. 9, which links
modeling choices to data characteristics, uncertainty requirements, interpretability, and computa-
tionalconstraints; andadomain-specificframeworkthatconnectsprobabilisticforecastingparadigms
to recurring requirements across application areas.
•A cross-paradigm empirical study.We evaluate representative approaches from the taxonomy
under a common protocol on univariate, multivariate, and spatiotemporal forecasting problems.
The goal is not to identify a universally superior model, but to examine how methodological choices
translate into empirical behavior. We therefore analyze point accuracy together with probabilistic
performance, calibration, sharpness, computational cost, and statistical robustness.
•Future research directions on probabilistic forecasting.Drawing on the reviewed literature
and empirical evidence, we identify several problems that remain insufficiently addressed: uncer-
tainty in evolving dependency structures, incorporation of physical knowledge into predictive dis-
tributions, forecasting of rare extremes, zero-inflated spatiotemporal counts, directional data, and
continuous time series, and the lack of unified software implementations for probabilistic forecast-
ing. We additionally discuss emerging opportunities in probabilistic foundation models, adaptive
forecasting systems, and agentic probabilistic forecasting.
The remainder of this survey is organized as follows. Section 1.1 introduces the notation and statistical
foundations, while Section 2 reviews related surveys and positions this work within the broader landscape.
Sections 3 and 4 cover model-agnostic and model-intrinsic uncertainty quantification methods, respectively.
Section 5 discusses probabilistic time series foundation models and their potential extension to spatiotem-
poral settings. Section 6 presents datasets, software resources, probabilistic evaluation measures, statisti-
cal comparison procedures, and guidance for method selection. Section 7 presents the empirical study of
representative approaches across temporal and spatiotemporal forecasting tasks. Section 8 discusses open
challenges and future research directions, and Section 9 concludes the survey.
1.1 Background and Notation
A time series consists of observations recorded at uniformly spaced intervals (Hyndman & Athanasopoulos,
2021). LetS={1,2,...,N}define a set of discrete spatial locations andT={1,2,...,T}denote a sequence
of equally spaced time points. A univariate time series at a specific locations∈Sis defined as the scalar
6

Preprint
Table 1: Representative model-agnostic and model-intrinsic probabilistic forecasting methods organized by
taxonomy. A dash (-) indicates methods without an explicit name in their original publication.
Method Name Uncertainty Quantification Method Data Type Application Domain Venue Year Reference
Model-Agnostic
EWNet Pre-Control Limits Univariate Epidemiology Neural Networks 2023 Panja et al. (2023)
- Resampling-based Ensemble Univariate Energy Solar Energy 2016 Grantham et al. (2016)
S-ESN Randomization-based Ensemble Spatiotemporal Energy JRSS C 2022 Huang et al. (2022)
D-EESN Randomization-based Ensemble Spatiotemporal Meteorology Environmetrics 2019 McDermott & Wikle (2019a)
TimeSeriesXAI Deep Ensemble Univariate Healthcare IEEE JBHI 2021 Wickstrøm et al. (2021)
DESQRUQ Deep Ensemble Spatiotemporal Transportation IEEE T-ITS 2024 Mallick et al. (2024)
- Bayesian Model Averaging Spatiotemporal Meteorology Urban Science 2025 Qin et al. (2025)
- Bayesian Model Averaging Spatiotemporal Meteorology JASA 2010 Sloughter et al. (2010)
STACI Conformal Prediction Spatiotemporal Environmental NeurIPS 2026 Feng et al. (2025)
CSP Conformal Prediction Univariate General ArXiv 2026 Manokhin (2026)
E-STGCN Conformal Prediction Spatiotemporal Environmental JRSS A 2026 Panja et al. (2026a)
MTSA-QRN Conformalized Quantile Regression Spatiotemporal Energy Sustainability 2026 Wang et al. (2026a)
EnCQR Conformalized Quantile Regression Multivariate Energy IEEE TNNLS 2024 Jensen et al. (2024)
CTCQRN Conformalized Quantile Regression Multivariate Energy Energy 2022 Hu et al. (2022)
Bayesian Modeling
BSTI Bayesian Hierarchical Model Spatiotemporal Transportation IEEE Access 2021 Cui et al. (2021)
- Bayesian Hierarchical Model Spatiotemporal Energy AOAS 2020 Lenzi & Genton (2020)
AGCGRU+flow State Space Model Spatiotemporal Traffic ICML 2021 Pal et al. (2021)
MBSTS State Space Model Multivariate Econometrics JMLR 2018 Qiu et al. (2018)
LKGP Gaussian Process Spatiotemporal General ICML 2025 Lin et al. (2025a)
Space-Time.DeepKriging Gaussian Process Spatiotemporal Environmental Spatial Statistics 2023 Nag et al. (2023)
DGGP Gaussian Process Spatiotemporal Traffic IEEE T-ITS 2022 Jiang et al. (2022)
ST-SVGP Gaussian Process Spatiotemporal General NeurIPS 2021 Hamelijnck et al. (2021)
GpGp Gaussian Process Spatiotemporal General Technometrics 2018 Guinness (2018)
- Dirichlet Process Univariate General IEEE ICDMW 2023 Ren et al. (2023)
Sticky HDP-HMM Dirichlet Process Multivariate Speech Processing AOAS 2011 Fox et al. (2011)
ARDL-BART Bayesian Additive Regression Tree Multivariate Macroeconomics AM (SCIRP) 2024 Mahdavi et al. (2024)
BART Bayesian Additive Regression Tree Multivariate Macroeconomics JOF 2019 Prüser (2019)
BNN Bayesian Neural Network Multivariate Macroeconomics J. Econom. 2025 Hauzenberger et al. (2025)
BARNN Bayesian Neural Network Univariate Synthetic ICML 2025 Coscia et al. (2025)
BAST-RNN Bayesian Neural Network Spatiotemporal General Entropy 2019 McDermott & Wikle (2019b)
- Approximate Bayesian Inference (MCMC) Spatiotemporal Environmental Environmetrics 2023 Johnson et al. (2023)
BSTIM Approximate Bayesian Inference (MCMC) Spatiotemporal Epidemiology PLOS ONE 2019 Stojanović et al. (2019)
UA-STTFF Approximate Bayesian Inference (MC Dropout) Spatiotemporal Transportation ICKECS 2026 Hemavathi & Sumathi (2026)
MVE+D Approximate Bayesian Inference (MC Dropout) Univariate Energy CIARP 2019 Serpell et al. (2019)
BayesNF Approximate Bayesian Inference (VI) Spatiotemporal General Nat. Commun. 2024 Saad et al. (2024)
STNN-VB Approximate Bayesian Inference (VI) Spatiotemporal Energy Applied Energy 2020 Liu et al. (2020)
- Approximate Bayesian Inference (INLA) Spatiotemporal Criminology JQC 2021 Mahfoud et al. (2021)
Spliced Gamma-GP Approximate Bayesian Inference (INLA) Spatiotemporal Energy JABES 2019 Castro-Camilo et al. (2019)
Parametric Predictive Distributions
- Single Parametric Distribution Multivariate General NeurIPS 2024 Zheng & Sun (2024)
DeepAR Single Parametric Distribution Multivariate General IJF 2020 Salinas et al. (2020)
EMOS Single Parametric Distribution Spatiotemporal Environmental JRSS A 2010 Thorarinsdottir & Gneiting (2010)
RST Single Parametric Distribution Spatiotemporal Energy JASA 2006 Gneiting et al. (2006)
HSMPF Mixture Density Networks Spatiotemporal Energy IEEE TSTE 2026 He et al. (2026)
WA-IMDN Mixture Density Networks Univariate Energy IEEE TSTE 2022 Yang et al. (2022)
IDMDN Mixture Density Networks Spatiotemporal Energy IEEE TPS 2020 Zhang et al. (2020)
- Mixture Density Networks Spatiotemporal Transportation IEEE RA-L 2019 Zhi et al. (2019)
Distributional Regression
EQRN Quantile Regression Spatiotemporal Hydrology AOAS 2024 Pasche & Engelke (2024)
SQR Quantile Regression Spatiotemporal Energy IEEE IAS 2019 Yu et al. (2019)
LSTM-Engression Engression Multivariate Hydrology GRL 2026 Kraft et al. (2026)
Enformer Engression Multivariate General ArXiv 2026 Pathak et al. (2026a)
GCEN/STEN Engression Spatiotemporal Epidemiology TMLR 2026 Pathak & Chakraborty (2026)
Tube Loss Loss-Driven Interval Prediction Multivariate General TMLR 2026 Anand et al. (2026)
DeepPIPE Loss-Driven Interval Prediction Multivariate General Neurocomputing 2020 Wang et al. (2020a)
Generative Models
STMPNet Copula-Based Model Spatiotemporal Traffic IEEE TKDE 2025 An et al. (2025)
TACTiS-2 Copula-Based Model Multivariate General ICLR 2024 Ashok et al. (2024)
GP-Copula Copula-Based Model Multivariate General NeurIPS 2019 Salinas et al. (2019)
DE-HMM Hidden Markov Model Spatiotemporal Autonomous Systems Transportmetrica A 2026 Zhou et al. (2026)
IOHMM Hidden Markov Model Spatiotemporal Transportation J. Adv. Transp. 2026 Liu et al. (2026)
MOHMM Hidden Markov Model Spatiotemporal Energy Energies 2025 Zhang & Shang (2025)
InfHMM Hidden Markov Model Univariate Energy Solar Energy 2022 Âzeddine Frimane et al. (2022)
C2FAR Hierarchical Discretization Univariate General NeurIPS 2022 Bergsma et al. (2022)
HDT Hierarchical Discretization Multivariate General AAAI 2025 Shibo et al. (2025)
K2VAE Variational Autoencoder Multivariate General ICML 2025 Wu et al. (2025)
Graph-EFM Variational Autoencoder Spatiotemporal Meteorology NeurIPS 2024 Oskarsson et al. (2024)
- Generative Adversarial Networks Spatiotemporal Environmental JMLR 2024 Pacchiardi et al. (2024)
STI-GAN Generative Adversarial Networks Spatiotemporal Autonomous Systems IEEE Access 2021 Huang et al. (2021)
ProFITi Normalizing Flows Multivariate General AAAI 2025 Yalavarthi et al. (2025)
STGNF Normalizing Flows Spatiotemporal Transportation CIKM 2024 An et al. (2024)
DyLand Normalizing Flows Spatiotemporal Geoscience IEEE Trans. Cybern. 2024 Xu et al. (2024)
MotionFlow Normalizing Flows Spatiotemporal Computer Vision IEEE TPAMI 2023 Zand et al. (2023)
LSTM/Transformer-MAF Normalizing Flows Multivariate General ICLR 2021 Rasul et al. (2021b)
NsDiff Denoising Diffusion Probabilistic Model Multivariate General ICML 2025 Ye et al. (2025)
SpecSTG Denoising Diffusion Probabilistic Model Spatiotemporal Transportation IJCNN 2025 Lin et al. (2025b)
DST-DDPM Denoising Diffusion Probabilistic Model Spatiotemporal Environmental Environ. Res. 2024 Chen et al. (2024)
MG-TSD Denoising Diffusion Probabilistic Model Multivariate General ICLR 2024 Fan et al. (2024)
DiffSTG Denoising Diffusion Probabilistic Model Spatiotemporal General SIGSPATIAL 2023 Wen et al. (2023)
TimeDiff Denoising Diffusion Probabilistic Model Multivariate General ICML 2023 Shen & Kwok (2023)
TimeGrad Denoising Diffusion Probabilistic Model Multivariate General ICML 2021 Rasul et al. (2021a)
GenCast Score-based Diffusion Model Spatiotemporal Meteorology Nature 2025 Price et al. (2025)
- Score-based Diffusion Model Multivariate General ICML 2023 Biloš et al. (2023)
DYffusion Score-based Diffusion Model Spatiotemporal General NeurIPS 2023 Cachay et al. (2023)
SHADECast Latent Diffusion Model Spatiotemporal Energy Applied Energy 2025 Carpentieri et al. (2025)
LDT Latent Diffusion Model Multivariate General AAAI 2024 Feng et al. (2024)
LADM Latent Diffusion Model Spatiotemporal Transportation IEEE TIM 2024 Lv et al. (2024)
PPM Parametric Prior Mapping Multivariate General ICML 2026 Li et al. (2026a)
TimePrism Probabilistic Scenarios Multivariate General ICLR 2026 Dai et al. (2026)
TimePre Multiple Choice Learning Multivariate General TMLR 2026 Jiang et al. (2026)
TimeMCL Multiple Choice Learning Multivariate General ICML 2025 Cortes et al. (2025)
7

Preprint
sequence{Y(s,t)} t∈T, whereY(s,t)∈Rrepresents the target variable at timet. Extending this to a mul-
tivariate context, we define a sequence of column vectors{yt}T t=1, whereyt = [Y(1,t),...,Y(N,t)] ⊤∈R N,
stacking the observations across allNlocations at each time stept. The complete collection of these variables
can be represented as a matrixY1:T = [y⊤ 1,...,y ⊤ T ]⊤∈R T×N. This matrix constitutes a spatiotemporal
dataset capturing both temporal dynamics and spatial interdependencies, if additional spatial information
such as connectivity among theNlocations is exploited. Many real-world spatiotemporal systems are de-
scribed by discrete relational structures that encode interactions through connectivity. In systems such as
transportation networks and power grids, observations are defined over nodes of a graphG= (V,E), where
Vis the set ofNspatial locations (nodes) andErepresents the connections (edges) between them. Graph
neural networks (GNNs), including graph convolutional and graph attention-based models, propagate in-
formation along edges to capture these relational dependencies within a spatiotemporal framework (Kipf &
Welling, 2017; Veličković et al., 2018). A more general form of a spatiotemporal dataset measuresDfeatures
forNspatial locations acrossTtime steps, rendering a three-dimensional tensorY∈R T×N×D . A sequence
of exogenous covariates{xt}t∈T may be incorporated alongside the historical data to provide information
on external factors influencing the target variable, thereby improving predictive accuracy.
The forecasting task is to predict future states{yT+1,...,y T+H}for allNlocations over a horizon ofH
steps, given the observed historyY 1:T. A point forecasting model maps this history to produce a single
deterministic estimateˆyT+h∈R N for each future steph∈{1,...,H}. In contrast, probabilistic forecasting
seeks to characterize the uncertainty inherent in future states (Gneiting & Katzfuss, 2014; Hyndman &
Athanasopoulos, 2021). Rather than producing a single fixed vector, a probabilistic model estimates the
conditional predictive probability distributionp(yT+h|Y 1:T )for each future steph∈{1,...,H}, or jointly
over the entire horizon. Point forecasts, prediction intervals, and quantiles can then be obtained as summaries
of the predictive distribution (Gneiting & Katzfuss, 2014). Throughout the remainder of this work, we adhere
to the notations established in this section. Unless explicitly stated otherwise, all standard mathematical
operations involving vector-valued quantities, such as the addition or squaring ofˆyT+h, are to be interpreted
as element-wise operations across theNspatial dimensions.
2 Literature Review
The growing forecasting literature has produced numerous surveys focusing primarily on point estimation
and predictive accuracy. Early reviews established neural networks as viable alternatives to classical forecast-
ing models and laid the foundation for subsequent developments in deep learning-based forecasting (Zhang
et al., 1998). More recent surveys have provided comprehensive overviews of modern architectures, including
recurrent networks, convolutional models, Transformers, and hybrid forecasting frameworks (Lim & Zohren,
2021; Benidis et al., 2022). While these reviews have significantly advanced the understanding of forecasting
methodologies, probabilistic forecasting is often treated as supplementary. The literature on spatiotemporal
forecasting follows a similar pattern. Existing surveys provide extensive coverage of architectures designed
to capture spatial and temporal dependencies, including convolutional recurrent networks, attention mech-
anisms, and GNNs (Wang et al., 2022; Yuan & Li, 2021; Jin et al., 2024). However, these surveys primarily
address modeling architectures and deterministic prediction, with probabilistic forecasting and uncertainty
quantification forming only part of their broader scope. Recent surveys have also examined foundation
models for time series analysis (Liang et al., 2024) and large models for both temporal and spatiotemporal
data (Jin et al., 2026). These surveys cover model architectures, pre-training and adaptation strategies,
data modalities, and downstream tasks, with limited discussion of probabilistic forecasting. However, they
do not focus on predictive uncertainty of foundation models. On the other hand, surveys addressing uncer-
tainty quantification in deep learning often treat it as a broader machine learning problem. For instance,
Abdar et al. (2021) and Gawlikowski et al. (2023) cover techniques such as Bayesian neural networks and
ensembles but pay limited attention to the characteristics that distinguish forecasting from other predic-
tive tasks. Despite the rigorous principles for probabilistic forecasting established by Gneiting & Katzfuss
(2014), this study predates the recent wave of deep learning models and does not address the challenges in-
troduced by modern temporal and spatiotemporal forecasting systems. As a result, many forecasting-specific
considerations remain outside the scope of these surveys.
8

Preprint
Table 2: Comparison of this survey with existing reviews. Coverage is indicated as follows: complete coverage
(✓), partial coverage (❍), and no coverage (✗). “Probabilistic” denotes explicit coverage of predictive
uncertainty. “Architecture Agnostic” denotes coverage of a broad range of methodological paradigms rather
than a single model class, whereas “General Scope” denotes coverage across multiple application domains
rather than a specific forecasting application. TS and ST denote time series and spatiotemporal forecasting,
respectively.
Survey Probabilistic TS Forecasting ST Forecasting Architecture Agnostic General Scope
Gneiting & Katzfuss (2014)✓ ✓ ❍ ✓ ❍
Hong & Fan (2016)✓ ✓ ✗ ✓ ✗
Nowotarski & Weron (2018)✓ ✓ ✗ ✓ ✗
Li & Zhang (2020)✓ ✓ ❍ ✓ ✗
Bazionis & Georgilakis (2021)❍ ✓ ❍ ✓ ✗
Abdar et al. (2021)✓ ❍ ❍ ✓ ✓
Lim & Zohren (2021)✗ ✓ ✗ ❍ ✓
Yuan & Li (2021)✗ ✓ ✓ ✓ ✗
Kaur et al. (2022)❍ ✓ ✗ ✓ ✗
Benidis et al. (2022)❍ ✓ ✗ ❍ ✓
Gao et al. (2022)❍ ❍ ❍ ✗ ✓
Papacharalampous & Tyralis (2022)✓ ✓ ✗ ✓ ✗
Wang et al. (2022)✗ ❍ ❍ ✓ ✓
Gawlikowski et al. (2023)✓ ❍ ✗ ✓ ✓
Xie et al. (2023)❍ ✓ ❍ ✓ ✗
Yu et al. (2024)❍ ✓ ✓ ❍ ✗
Chakraborty et al. (2024)❍ ❍ ✗ ✗ ✓
Liu & Wang (2024)❍ ✓ ✗ ❍ ✓
Blasco et al. (2024)✓ ✓ ✗ ❍ ✗
Jin et al. (2024)❍ ✓ ✓ ✗ ✓
De León Pérez et al. (2025)✓ ✓ ✗ ✓ ✗
Eggen et al. (2026)✓ ✓ ✗ ✓ ✗
Yang et al. (2026)✓ ❍ ❍ ✗ ✓
Our survey✓ ✓ ✓ ✓ ✓
The growing importance of probabilistic forecasting has also motivated a number of domain-specific reviews.
In energy systems, Hong & Fan (2016) provides a tutorial on probabilistic load forecasting, while Li & Zhang
(2020) reviews the integration of probabilistic solar forecasting into power system operations, and Kaur
et al. (2022) surveys smart grid forecasting with an emphasis on probabilistic methods. In wind energy,
Bazionis & Georgilakis (2021) and Xie et al. (2023) survey deterministic and probabilistic methods, offering
practical guidance for practitioners. In finance, Nowotarski & Weron (2018) reviews probabilistic electricity
price forecasting, Eggen et al. (2026) examines probabilistic artificial intelligence methods for financial time
series, and Blasco et al. (2024) surveys uncertainty quantification in deep learning for financial markets. In
hydrology, Papacharalampous & Tyralis (2022) reviews machine learning approaches for probabilistic post-
processing and forecasting, while De León Pérez et al. (2025) provides a comprehensive review of uncertainty
quantification methods across short-to-seasonal horizons. These works offer valuable depth within their
respective domains, but their scope is shaped by domain-specific datasets, assumptions, and evaluation
protocols. They do not establish a methodological perspective that carries across different temporal and
spatiotemporal problems. More recently, dedicated surveys have examined generative adversarial networks
(GANs) broadly (Chakraborty et al., 2024), GANs for spatiotemporal data (Gao et al., 2022), and diffusion
models for temporal and spatiotemporal applications (Yang et al., 2026). These reviews have advanced
understanding of rapidly evolving model families and their applications to forecasting, imputation, and
anomaly detection. However, by focusing on a single methodological paradigm, they offer limited guidance
on how generative approaches compare to alternative probabilistic forecasting frameworks. Therefore, as
summarizedinTable2, thereiscurrentlynocomprehensivesurveythatjointlycoversprobabilisticforecasting
across both temporal and spatiotemporal settings while spanning the full range of approaches from classical
statistical methods through to modern generative models. This survey seeks to address this gap by presenting
a unified review of probabilistic forecasting for time series and spatiotemporal data.
9

Preprint
y
t
y
t
e
t
y
t
t
y
Resampling
Empirical Forecast
Distribution
Deep
Ensembles
NN1
NN2
NNM
...
...
...
Fixed width prediction intervals
Conformal scores
Conformal Prediction
Conformalized Quantile Regression (CQR)
Initial quantile bounds Calibrated quantile bounds
t
y
t
y
Train Calibrate
Base Forecaster f̂
Point Forecasts ŷT+h Probabilistic Output
Pre-control limits
Ensemble-based
Distribution-free calibration
±kσ̂
Residuals Randomization
Bayesian
Model
Averaging
Residuals
Figure 2: Overview of model-agnostic uncertainty quantification strategies applied to a base forecast-
ing model, comprising residual-based pre-control limits, ensemble-based predictive distributions, and
distribution-free calibration.
3 Model-Agnostic Uncertainty Quantification
Model-agnostic uncertainty quantification methods estimate predictive uncertainty through procedures that
can be applied across different forecasting architectures and model classes (Efron & Tibshirani, 1993; Vovk
et al., 2005; Angelopoulos & Bates, 2023). These methods operate largely independently of the underlying
forecaster and can therefore be used with a wide range of models, from classical statistical methods to
modern deep neural networks. Depending on the method, they may be applied post hoc or require repeated
model fitting or an uncertainty-aware base estimator. In contrast to the model-intrinsic approaches reviewed
in Section 4, these methods do not require uncertainty to be encoded in a single forecasting architecture.
Depending on the method, predictive uncertainty is obtained through residual transformation, resampling,
refitting, model randomization, forecast combination, or post-hoc calibration. The approaches reviewed in
this section are grouped into three broad families, illustrated in Fig. 2: pre-control limits (Section 3.1),
ensemble-based approaches (Section 3.2), and distribution-free calibration methods (Section 3.3). Their
main characteristics are summarized in Table 3.
3.1 Pre-Control Limits
Pre-control limits are a simple model-agnostic approach to uncertainty quantification, originating in statisti-
cal process control for monitoring process variability (Rahimifard & Sharifi Ghazvini, 2020). They belong to
a broader class of process control methods that quantify variation using control charts and fixed dispersion-
10

Preprint
Table 3: Comparison of model-agnostic methods by coverage guarantee, parametric assumptions, adaptive
width, and computational cost. Check marks (✓) denote yes, crosses (✗) denote no.
Method Coverage Guarantee Parametric Assumptions Adaptive Width Computational Cost
Pre-control Limits✗ ✓ ✗Low
Resampling-based Ensembles Asymptotic † ✗ ✗Low
Randomization-based Ensembles✗ ✗ ✓Moderate
Deep Ensembles✗ ✓ ✓High ‡
Bayesian Model Averaging✗ ✓ ✓Moderate
Conformal Prediction Finite-sample✗ ✓Low-Moderate
Conformalized Quantile Regression Finite-sample✗ ✓Moderate
†Coverage is unguaranteed for the i.i.d. bootstrap under serial dependence; block-bootstrap variants provide asymptotic
consistency under stationarity and mixing conditions (Kunsch, 1989).
‡Scales linearly with the number of ensemble members.
based thresholds (Castillo, 2002; Montgomery, 2020). In forecasting, the same principle can be applied to
construct prediction intervals around point forecasts by assuming that errors are i.i.d. and have constant
variance. Given a forecasting model that produces point forecastsˆyT+h and historical in-sample residuals
E={y t−ˆyt}T t=1, the prediction interval for a future observationˆyT+h is constructed asˆyT+h±k·ˆσ, where
ˆσis the standard deviation of the historical residualsEandkis a fixed multiplier. Under a Gaussian as-
sumption,k= 1.5yields an expected coverage of approximately 86% (Panja et al., 2023). The primary
advantage of pre-control limits is their computational simplicity since the intervals are a transformation of
the point forecast that requires a single scalar estimate of residual variance. However, the method relies
on the strong assumptions of stationarity and homoskedasticity (constant variance) of forecast errors. In
temporal data, these assumptions are often violated, leading to severely miscalibrated intervals, especially
for multi-step-ahead forecasts as observed in epidemic forecasting (Panja et al., 2023). These restrictive
assumptions have limited the use of pre-control limits in modern probabilistic forecasting and motivate more
flexible approaches for representing predictive uncertainty.
3.2 Ensemble-Based Methods
Ensemble-based methods extend the model-agnostic perspective by representing predictive uncertainty
through variation across multiple models or forecast trajectories, rather than through a fixed estimate of
residual dispersion. These methods can be broadly divided into two categories: constructing an ensemble
of forecasting models and extracting an ensemble of forecasts from a single model. The latter characterizes
predictive uncertainty through an ensemble of plausible future trajectories rather than a single point forecast,
using the variance among these ensemble members to quantify forecast uncertainty (Elliott et al., 2013). This
inherent flexibility has led to the widespread adoption of ensemble methods across statistical modeling, ma-
chine learning, and environmental forecasting (Dietterich, 2000; Gneiting et al., 2005). Existing approaches
differ primarily in how ensemble diversity is generated, including resampling-based strategies (Section 3.2.1),
model randomization (Section 3.2.2), deep ensembles (Section 3.2.3), and forecast combination methods such
as Bayesian model averaging (Section 3.2.4). Although conceptually simple, applying ensemble methods to
temporal and spatiotemporal forecasting requires careful treatment of temporal and spatial dependence
structures, which are often violated by standard ensemble construction procedures (Cressie & Wikle, 2011).
3.2.1 Resampling-Based Ensembles
Resampling-basedmethodsprovideoneofthemostestablishedmechanismsforgeneratingensemblediversity.
Bootstrap approaches approximate the predictive distribution by repeatedly resampling the observed data or
fitted residuals and generating a collection of plausible future trajectories (Efron & Tibshirani, 1993). Given
a forecasting model that produces a point forecastˆyT+h and a set of historical forecast errorsE={et}T t=1,
wheree t =y t−ˆyt, residual bootstrap methods generate an ensemble of horizon-specific forecast samples by
resampling from these past residuals:
ˆy(m) T+h =ˆyT+h + ˜e(m) h , m= 1,...,M,
11

Preprint
where˜e(m) h is a residual drawn randomly with replacement from the setE. The resulting ensemble{ˆy(m) T+h}M m=1
approximates the predictive distribution for theh-step-ahead time point, from which prediction intervals can
be obtained using empirical quantiles.
However, preserving the temporal dependence structure remains a central challenge. Standard bootstrap
procedures rely on independent sampling and may destroy temporal correlations present in the data. Block
bootstrap methods address this issue by resampling groups of consecutive observations to preserve tem-
poral structure (Kunsch, 1989). An additional limitation of the direct application of residual bootstrap
methods is the assumption that historical errors are representative of future uncertainty. This assumption
is violated when the error distribution changes over time or depends on external factors. To address this
limitation, Grantham et al. (2016) proposed a conditional bootstrap approach for solar radiation forecast-
ing, where residuals are partitioned into bins according to covariates that influence variance, then sampled
from the appropriate bin for each forecast. This method produces prediction intervals that better reflect
the heteroskedastic nature of the forecasting problem. For spatiotemporal forecasting, however, additional
strategies are required to maintain spatial dependence, making uncertainty estimation considerably more
challenging in high-dimensional settings (Cressie & Wikle, 2011).
3.2.2 Randomization-Based Ensembles
Resampling observations or residuals can distort the temporal and spatial dependence structure.
Randomization-based ensembles overcome this by generating diversity through stochasticity in forecast-
ing model. Echo state networks (ESNs) provide an early example of this idea in forecasting (Jaeger, 2001).
ESNs belong to the family of reservoir computing models, where the reservoir weights are randomly ini-
tialized and kept fixed during training, while only the output layer is trained. Despite their effectiveness
in modeling nonlinear temporal dynamics, ESNs yield a single deterministic forecast for a given reservoir
realization. To obtain uncertainty estimates, McDermott & Wikle (2017) introduced the ensemble ESN
(EESN), where an ensemble of ESN models is generated through independent reservoir realizations. For
each future steph∈{1,...,H}, this process generates an ensemble of forecasts{ˆy (m) T+h}M m=1. The resulting
empirical predictive distribution for theh-step-ahead time point is typically summarized by the ensemble
mean and variance:
¯yT+h = 1 M
M∑
m=1
ˆy(m) T+h,andˆσ 2 T+h = 1 M−1
M∑
m=1
(
ˆy(m) T+h−¯yT+h
)2
,
respectively, where the mean (¯yT+h) serves as the point forecast and the variance (ˆσ2 T+h) provides a measure
of predictive uncertainty. Subsequent studies extended this idea to deep reservoir architectures capable of
representing spatiotemporal dynamics (McDermott & Wikle, 2019a) and incorporated spatial dimension
reduction strategies for large-scale spatiotemporal forecasting (Huang et al., 2022). However, generating
sufficiently diverse ensembles can become computationally demanding, particularly for complex forecasting
models and high-dimensional spatiotemporal applications (Cressie & Wikle, 2011; Huang et al., 2022).
Another conventional randomization-based framework is the random forest (Breiman, 2001), which trains
an ensemble of decision trees in parallel using bootstrap samples and randomized feature subsets, thereby
combining data and model randomization. The efficacy of such ensembles relies on aggregating strong,
uncorrelated models. This diversity is classically achieved through bagging (bootstrapping), where indi-
vidual members are fit to distinct resampled subsets of the training data. Standard random forests ap-
proximate the conditional mean of a response variable. To capture the conditional predictive distribution,
Meinshausen (2006) extended random forests through quantile regression forests (QRF), which estimate con-
ditional quantiles from the forest-induced distribution of responses. QRF therefore lies at the intersection
of ensemble-based methods and distributional regression (discussed in Section 4.3). This methodology was
recently adapted for sequential temporal data via the time series QRF (tsQRF) (Shiraishi et al., 2024).
Drawing conceptual similarities from QRF, Hasson et al. (2021) introduced the level set forecaster (LSF),
a model-agnostic approach capable of transforming any point-prediction algorithm into a probabilistic fore-
caster. LSF accomplishes this by grouping training instances that yield sufficiently similar point forecasts,
subsequently utilizing the empirical distribution of the ground-truth values within these localized bins to
formulate the final predictive density.
12

Preprint
3.2.3 Deep Ensembles
Bagging-based ensembles (Breiman, 2001) can be inefficient for deep neural networks because each base
learner is trained on only a subset (∼63%) of the unique training data. Deep ensembles instead induce
diversity through independent parameter initialization and stochastic training while allowing each network
to use the full training dataset (Lakshminarayanan et al., 2017). This combination preserves data efficiency
and model capacity while providing a practical means of quantifying predictive uncertainty from variation
across independently trained models. Recent work has extended deep ensembles to address uncertainty esti-
mation in increasingly complex forecasting settings. For clinical time series, Wickstrøm et al. (2021) quantify
uncertainty in temporal relevance scores by measuring their variation across independently trained neural
networks, providing uncertainty estimates alongside model explanations. Maulik et al. (2023) use genetic
algorithms and Bayesian optimization to construct diverse ensembles of high-performing neural architectures
and decompose predictive variability to quantify uncertainty. For spatiotemporal forecasting, Mallick et al.
(2024) combine deep ensembles with distribution-free simultaneous regression loss to characterize predictive
uncertainty, inducing ensemble diversity through hyperparameter configurations sampled from a Gaussian
copula (discussed in Section 4.4.1) generative model. The utility of such strategies is empirically supported
by Willard & Varadharajan (2025), who evaluate six classical and deep learning ensemble construction meth-
ods, demonstrating that varying input data and combining diverse models significantly enhances both the
accuracy and uncertainty quantification of spatiotemporal hydrologic forecasts. Deep ensembles are also
widely used as a practical approximation to epistemic uncertainty by measuring variability across indepen-
dently trained models. Their forecasts or predictive distributions are aggregated to estimate the overall
predictive uncertainty.
3.2.4 Bayesian Model Averaging
Bayesian model averaging (BMA) provides a probabilistic ensemble framework for addressing model uncer-
tainty in statistical inference (Hoeting et al., 1999). It combines the predictive distributions of multiple
competing models using weights that reflect their posterior support, thereby accounting for their relative
contributions to the combined forecast (Raftery et al., 2005). Given point forecasts fromKdistinct mod-
els, denoted asˆyT+h,1,...,ˆy T+h,K, the BMA predictive density for theh-step-ahead future stateyT+h is
formulated as the conditional mixture distribution:
p(yT+h|ˆyT+h,1,...,ˆy T+h,K ) =
K∑
k=1
wkgk(yT+h|ˆyT+h,k ),
whereg k(yT+h |ˆyT+h,k )represents the conditional predictive density associated with thekth model, and
the weights are constrained such thatw k ≥0and ∑K k=1wk = 1. Under this framework, the weights
wk correspond to posterior probabilities that reflect each model’s relative predictive performance over a
designated training horizon (Raftery et al., 2005). In practice, for continuous variables such as temperature,
the conditional densities are typically modeled as Gaussian distributions centered at the bias-corrected
forecasts. For non-Gaussian variables, the component densities are tailored to the support of the target
domain. Forinstance, skewedcontinuousvariablessuchaswindspeedaremodeledusinggammadistributions
(Sloughter et al., 2010). Conversely, precipitation, which exhibits both zero-inflation and a heavy upper
tail, is accommodated via a discrete-continuous mixture comprising a point mass at zero and a power-
transformed gamma distribution (Sloughter et al., 2007). Parameter estimation is typically conducted via
the Expectation-Maximization (EM) algorithm (Dempster et al., 1977).
In spatiotemporal forecasting, BMA has been applied to weather and climate forecasting, where multiple
numerical simulation systems are often available. For instance, Raftery et al. (2005) employed BMA for
weather ensemble post-processing, while Qin et al. (2025) applied the framework to combine climate model
projections for long-term environmental forecasting. However, most existing implementations estimate mix-
ture parameters independently across spatial locations, limiting their ability to represent spatial dependence
and coherent uncertainty across large spatial domains. Moreover, employing BMA in large-scale spatiotem-
poral domains introduces significant modeling and computational hurdles, rendering standard optimization
routines computationally prohibitive.
13

Preprint
0 2 4 6 8 10 12 14
Time t
0
1
2
3
4
5
6
Time Series Yt
Training Calibration Test
(a) Data Split
1 2 3 4 5 6 7
Calibration time t
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
St
Q1
(b) Conformal Scores
0 2 4 6 8 10 12
Time t
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
St
window v = 4
t
(c) Sliding Window
1 2 3 4 5 6 7
Horizon h
0
1
2
3
4
5
6
7
8
YT + h
(d) Prediction Intervals
Figure 3: Illustration of rolling-window conformal prediction for temporal data. Panel(a)shows the data
split into training (green), calibration (yellow), and test (red) sets. Panel(b)displays the conformal scores
S˜t computed on the calibration set, with the empirical quantile marked as a dashed black line. Panel
(c)demonstrates the sliding window mechanism where only the most recent scores (highlighted in blue)
contribute to computing the conformal quantile. Panel(d)shows the resulting prediction intervals.
3.3 Distribution-Free Calibration Methods
Although ensemble-based methods provide flexible representations of predictive uncertainty, they do not
inherently ensure calibration, as their reliability depends on how ensemble diversity is generated and forecasts
are combined. This limitation motivates distribution-free calibration methods, which construct predictive
intervals by calibrating model outputs against observed forecast errors without specifying a parametric
form for the underlying data distribution. This section reviews two major approaches to distribution-free
calibration: conformal prediction (Section 3.3.1) and conformalized quantile regression (Section 3.3.2).
3.3.1 Conformal Prediction
Conformal prediction (CP) provides a rigorous, distribution-free framework for uncertainty quantification,
providing finite-sample marginal coverage under exchangeability for a target miscoverage rateα∈(0,1). We
refer readers to Vovk et al. (2005); Shafer & Vovk (2008) for a comprehensive discussion of foundational CP
mechanics. To reduce the computational burden of standard CP, split conformal prediction (Papadopoulos
et al., 2002) partitions data into training (I1) and calibration (I2) sets, generating intervals based on the
finite-sample adjusted empirical quantileQ 1−α of the calibration conformity scores. Split CP transforms
point estimators into distribution-free prediction intervals, but its theoretical guarantees rely on exchange-
ability, which is often violated in temporal and spatiotemporal domains due to serial and spatial correlations.
Historical calibration scores may therefore provide poor estimates of future forecast errors when the data
exhibit dependence or distributional changes, leading to degraded empirical coverage (Xu & Xie, 2021; Gibbs
& Candes, 2021). Consequently, recent work has focused on adapting conformal prediction to dependent
data through dynamic and adaptive calibration procedures.
A common approach for temporal forecasting uses weighted sliding windows to emphasize recent observa-
tions, as illustrated in Fig. 3. Instead of assigning equal weight to all historical errors, this method computes
calibration scores from recent model performance and normalizes them against an underlying uncertainty
estimator. A rolling window then retains the most recent conformity scores to determine an adaptive thresh-
old. This allows the resulting prediction intervals to adjust to local variability and nonstationary dynamics
without relying on potentially outdated historical observations. Another conformal approach designed for
dependent time series is ensemble batch prediction intervals (EnbPI) (Xu & Xie, 2021), which combines leave-
one-out predictions from bootstrap ensembles with a sliding window of recent residuals. EnbPI continuously
updates the interval using recent forecasting errors and provides approximately valid marginal coverage for
time series with strongly mixing errors. Recent developments on conformal seasonal pools (CSP) (Manokhin,
2026) instead exploits recurring seasonal structure when constructing prediction intervals. Rather than rely-
ing solely on recent residuals, CSP combines seasonally matched historical observations with residual-based
adjustments around a seasonal baseline forecast, making it particularly suitable for seasonal time series.
14

Preprint
Extending conformal prediction to spatiotemporal forecasting introduces an additional challenge, because de-
pendence must be addressed simultaneously across both space and time. One strategy replaces global calibra-
tion with localized calibration. The spatiotemporal aleatoric conformal inference (STACI) framework (Feng
et al., 2025), for instance, constructs calibration sets using observations located within a local spatiotemporal
neighborhood of the prediction target, relying on the weaker assumption of local exchangeability. A com-
plementary direction integrates conformal calibration with graph-based forecasting architectures. Methods
such as CP-STGCN (Zhao et al., 2025b) leverage spatiotemporal graph convolutional network (STGCN)
(Yu et al., 2018) to capture spatial dependencies while using conformal prediction as a post-hoc calibration
layer. The practical appeal of CP approach has led to its adoption across diverse forecasting settings, includ-
ing clinical and public-health time series (Stankeviciute et al., 2021; Goswami et al., 2026), electricity-price
forecasting (Zaffran et al., 2022), financial-volatility forecasting under distribution shift (Gibbs & Candes,
2021), and air quality prediction (Panja et al., 2026a).
3.3.2 Conformalized Quantile Regression
Conformalized quantile regression (CQR) extends the conformal prediction framework by incorporating
conditional quantile estimation into the calibration process (Romano et al., 2019). CQR first estimates
lower and upper conditional quantile functions, denoted byˆqαlo(xt+h)andˆqαhi(xt+h), respectively, where
xt+h denotes a set of features (or lagged variables) available at timetto predict horizonh. This is done
by minimizing the pinball loss (Steinwart & Christmann, 2011). These quantile estimates are subsequently
calibrated using a held-out calibration setI2. The(1−α) th empirical quantile, denoted byˆQ1−α,h(I2), is
then computed over the horizon-specific set of non-conformity calibration scores. For a forecast of the future
statey T+h at horizonhgiven featuresx T+h, the final adjusted prediction interval is constructed as:
ˆC 1−α T+h = [ ˆqαlo(xT+h )− ˆQ1−α,h(I2),ˆqαhi(xT+h ) +ˆQ1−α,h(I2) ] .
Theresultingintervalmaintainsthefinite-samplecoverageguaranteeofconformalprediction, whileinheriting
the ability of quantile regression to model varying levels of uncertainty across different forecasting conditions.
This property has made CQR suitable for temporal forecasting problems characterized by nonstationarity
and heteroskedasticity. For example, the conformalized temporal convolutional quantile regression network
(CTCQRN) integrates CQR with temporal convolution networks (TCNs) for wind power interval forecasting
(Hu et al., 2022). The TCN architecture captures long-range dependence, while the conformal calibration
layer corrects the quantile estimates to provide reliable uncertainty bounds. More recent approaches, such
as ensemble conformalized quantile regression (EnCQR), combine ensembles of quantile regression models
with adaptive calibration strategies to further improve robustness under evolving temporal dynamics (Jensen
et al., 2024).
For relational and spatiotemporal forecasting, CQR has been extended to exploit dependencies across mul-
tiple correlated time series. Conformal relational prediction (CoRel) (Cini et al., 2025) uses graph-based
learning to estimate residual quantiles across related series, incorporating an adaptive calibration mech-
anism to accommodate non-exchangeability and localized distributional changes. In photovoltaic power
forecasting, the multi-scale temporal-spatial attention quantile regression network (MTSA-QRN) combines
a dual-pathway quantile regression architecture with adaptive conformal calibration (Wang et al., 2026a).
Its temporal pathway uses temporal convolutions and attention mechanisms, while its graph-attention path-
way models dependencies among variables. Physics-informed constraints have also been incorporated into
spatiotemporal CQR. The physics-driven dynamic wake forecasting CQR (PDWF-CQR) framework (Wang
et al., 2026b) constructs a time-varying directed graph from turbine wake interactions and imposes power-
curve-based regularization on the quantile boundaries.
4 Model-Intrinsic Uncertainty Quantification
In contrast to model-agnostic methods, model-intrinsic uncertainty quantification refers to approaches in
which uncertainty is represented within the model formulation, learning objective, or posterior inference
procedure. The model is trained to produce probabilistic outputs as part of the forecasting process. We or-
ganize these methods into four families: Bayesian modeling (Section 4.1), parametric predictive distributions
15

Preprint
Prior
Input
Observed Series
Classical
Hierarchical State Space
Bayesian Models
Bayesian Nonparametric
GP DP BART
Bayesian Neural Network
Posterior Inference
(Approx. Bayesian Inference)
MCMC
Variational Inference
Target posterior
Variational posterior
MC Dropout
INLA
Observed Forecast
Probabilistic Forecast
Stochastic passes
Figure 4: Overview of Bayesian methods for probabilistic forecasting, covering classical Bayesian models,
Bayesian nonparametric methods, and Bayesian neural networks. Posterior predictive distributions are
obtained through exact inference when tractable or through approximate inference methods.
(Section 4.2), distributional regression (Section 4.3), and generative models (Section 4.4). Bayesian models
propagate uncertainty over parameters, functions, or latent states through the posterior predictive distribu-
tion. Parametric predictive models estimate the parameters of an assumed distributional family, whereas
distributional regression directly learns quantiles, intervals, or predictive distributions through loss-based
objectives. Generative models instead learn a stochastic mechanism from which plausible future trajectories
can be sampled.
4.1 Bayesian Modeling
Bayesian modeling provides a framework for probabilistic forecasting by placing prior distributions over
unknown quantities and updating them with observed data to obtain a posterior predictive distribution, as
depicted in Fig. 4. Bayesian approaches can be broadly categorized into three classes. Classical Bayesian
models (Section 4.1.1) explicitly represent dependence through hierarchical structures, latent state processes,
or covariance functions. Bayesian nonparametric methods (Section 4.1.2) relax fixed parametric assumptions
by placing priors over infinite-dimensional spaces. Finally, Bayesian neural networks (Section 4.1.3) extend
these principles to deep learning by treating network weights as random variables. Across these model
classes, exact posterior inference is rarely tractable beyond simple linear Gaussian settings. Consequently,
Bayesian forecasting relies heavily on the approximate inference methods reviewed in Section 4.1.4.
16

Preprint
4.1.1 Classical Bayesian Models
Classical Bayesian models construct predictive distributions by placing priors over unknown quantities and
updating them using observed data. This framework enables uncertainty to propagate coherently from
parameter estimation to forecasting. Two foundational classes are reviewed in this section. Bayesian hier-
archical models (Section 4.1.1.1) decompose the joint distribution into observation, process, and parameter
components, whereas Bayesian state space models (Section 4.1.1.2) capture dynamics through an evolving
latent state process. In both cases, dependence structures are specified explicitly, supporting principled
uncertainty quantification but at the expense of scalability.
4.1.1.1 Bayesian Hierarchical Models.Bayesian hierarchical models (BHMs) decompose the joint
distribution into a data modelp(y|z,W D)describing the observation process, a process modelp(z|W P )
characterizing the latent dynamics, and a parameter modelp(WD,WP )specifying prior distributions (Wikle
& Zammit-Mangion, 2023). For observed datayand latent processz,the structure is given by:
p(z,WD,WP|y)∝p(y|z,W D)p(z|W P )p(W D,WP ),
whereW D andW P denote data and process parameters, respectively. This modular construction allows
each component to be specified independently and adapted to the data characteristics (Wikle & Zammit-
Mangion, 2023; Lovegrove & Siegert, 2023). For example, count observations in epidemiological applications
are accommodated through Poisson or Negative Binomial likelihoods that handle overdispersion (Al-Manji
et al., 2025), while spatial and temporal dependencies can be introduced through conditional autoregressive
models (Cui et al., 2021; Louzada et al., 2025).
A common limitation of BHMs in spatiotemporal applications is the use of a separable covariance structure,
where joint spatiotemporal dependence is represented through distinct spatial and temporal components
(Cressie & Wikle, 2011). Cui et al. (2021) addressed this limitation by introducing explicit spatiotemporal
interaction (STI) terms for online bus speed prediction. A second limitation is the assumption of spatial
isotropy, under which dependence is determined by Euclidean distance and does not vary with direction.
This can be restrictive when spatial dependence is directional or varies across the spatial domain (Fuglstad
et al., 2015). To accommodate nonstationary and anisotropic spatial dependence, Castruccio et al. (2018)
proposed a multi-resolution BHM for functional magnetic resonance imaging (fMRI) data that forms a
spatially weighted combination of local, geometrically anisotropic Matérn processes across subregions. BHMs
have also been developed for multivariate spatiotemporal processes, where dependencies among multiple
variables must be modeled jointly. For instance, Lenzi & Genton (2020) proposed a bivariate model for wind
vector forecasting based on a linear model of coregionalization, expressing each orthogonal wind component
as a weighted combination of latent spatiotemporal processes to induce joint space-time cross-covariance
structures.
4.1.1.2 Bayesian State Space Models.Bayesian state space models (SSMs) provide an alternative
framework for probabilistic forecasting by representing observations through an evolving latent state process.
The (univariate) framework is defined by an observation equation and a state transition equation:
yt =Z⊤ t αt +β⊤xt +ϵt, ϵ t∼N(0,Σ t),andα t+1 =T tαt +Rtηt, η t∼N(0,Q t),(1)
whereα t denotes the latent state vector,Zt,Tt,Rt are model matrices,xt represents exogenous covariates
with coefficientsβ, andΣ t andQ t represent the observation and state noise covariance matrices, respec-
tively (Scott & Varian, 2014). Kalman filter (Kalman, 1960; Diebold, 1992) and smoother enable exact
inference under Gaussian assumptions by recursively estimating the filtering distributionp(αt|Y 1:t)and
the smoothing distributionp(αt|Y 1:T ), respectively. Probabilistic forecasts are then obtained by propagat-
ing the posterior state distribution through the transition dynamics, yielding the full predictive distribution
p(yT+h|Y 1:T )over future observations.
The Bayesian structural time series (BSTS) framework extends the state-space formulation through struc-
tural decomposition and spike-and-slab regression, allowing large sets of candidate covariates to be incor-
porated. (Scott & Varian, 2014). BSTS additively decomposes the target series into level, trend, seasonal,
17

Preprint
and regression components. Posterior inference is performed via a Markov Chain Monte Carlo (MCMC)
algorithm (Section 4.1.4.1) using simulation smoothing and stochastic search variable selection (George &
McCulloch, 1997), while accounting for model uncertainty through Bayesian model averaging (Section 3.2.4).
BSTS has been adopted across applications including economic and financial forecasting (Qiu et al., 2018;
Katarina & Gunardi, 2023), climate policy uncertainty (Besher et al., 2026b), and tourism demand predic-
tion (Andrews & Kimpton, 2023). The multivariate BSTS (MBSTS) (Qiu et al., 2018) generalizes BSTS
by extending the univariate formulation (Eq. 1) to jointly model correlated series by assigning series-specific
state components and capturing cross-series dependence through the observation noise covariance matrixΣt.
MBSTS further incorporates cyclical components with damping factors to capture transient effects, which
improved forecasting performance for financial time series during periods of market instability (Qiu et al.,
2018). Despite these extensions, the state space formulation (Eq. 1) remains limited for spatiotemporal
systems due to restrictive assumptions of linearity and Gaussian noise. Pal et al. (2021) addressed this
limitation through a nonlinear SSM that combines graph convolutional recurrent units (Bai et al., 2020)
for spatiotemporal dependency learning with particle flow inference for posterior approximation, improving
probabilistic forecasting in traffic applications.
4.1.2 Bayesian Nonparametric Methods
Bayesian nonparametric (BNP) methods provide a flexible framework for probabilistic temporal and spa-
tiotemporal forecasting by relaxing the assumption of a fixed parametric model. Instead, they place priors
over infinite-dimensional probability measures or function spaces, allowing model complexity to adapt to
the observed data (Hjort et al., 2010). The choice of prior defines the resulting modeling framework, giv-
ing rise to different BNP approaches. This section discusses three prominent BNP approaches: Gaussian
Processes (Section 4.1.2.1), Dirichlet Processes (Section 4.1.2.2), and Bayesian Additive Regression Trees
(Section 4.1.2.3).
4.1.2.1 Gaussian Processes.A Gaussian process (GP) is a stochastic process defined such that any
finite collection of function values follows a joint Gaussian distribution. Instead of assuming a fixed para-
metric form, GPs specify a prior over functions, offering a flexible nonparametric Bayesian framework for
probabilistic forecasting (Rasmussen, 2004). GP is defined as~f∼GP(Υ(t),Ω(t,t ′)),whereΥ(t)is the mean
function andΩ(t,t′)is the covariance kernel that determines the dependency structure of the process. The
kernel specification controls properties such as smoothness, periodicity, and stationarity of the resulting fore-
casts, and its hyperparameters are learned from data (Williams & Rasmussen, 1995). Given the observed
history and a GP prior with a Gaussian likelihood, the posterior distribution over future states remains
Gaussian with closed-form predictive mean and covariance. Exact GP inference, however, is limited by cubic
computational complexityO(T 3)arising from covariance matrix inversion. Sparse variational GPs address
this limitation by introducing a set ofMinducing points to summarize the training data, reducing the
computational cost toO(TM 2 +M 3)(Wilkinson et al., 2021). For the spatiotemporal setting, methods such
as latent Kronecker GPs accommodate missing observations by operating on an underlying complete grid
representation (Lin et al., 2025a). State-space formulations provide another scalable alternative by exploiting
Markovian structure, enabling linear-time inference through Kalman filtering and smoothing (Hamelijnck
et al., 2021).
GP-based forecasting has been applied across a wide range of domains, including epidemiological forecasting
(Agyemang, 2025), intermittent demand forecasting with TweedieGP (Damato et al., 2025), and short-
term traffic forecasting with deep graph Gaussian processes (DGGP) (Jiang et al., 2022). In large-scale
spatiotemporal applications, sparse variational GP frameworks have been developed for tasks such as crime
and air quality forecasting by combining GP priors with structured approximations (Flaxman et al., 2015;
Schoucair & van Reeuwijk, 2025). Related efforts have also explored replacing covariance-based interpolation
altogether. For instance, Nag et al. (2023) proposed Space-Time.DeepKriging, which uses neural networks
with spatial and temporal basis functions to achieve scalable spatiotemporal forecasting while retaining
uncertaintyestimatesthroughquantile-basedprediction. Forirregularspatialobservations, scalableinference
can instead be achieved through Vecchia approximations (Vecchia, 1988), which condition each observation
on a small set of neighboring observations rather than the full dataset. GpGp (Guinness, 2018) adopts this
18

Preprint
strategy, enabling scalable probabilistic forecasting on large spatiotemporal datasets where Kronecker-based
methods are less suitable.
4.1.2.2 Dirichlet Processes.In contrast to GPs, which define priors over function spaces, Dirichlet
processes(DPs)placepriorsoverprobabilitymeasures, enablinghighlyadaptivemixturemodeling(Ferguson,
1973). A DP, denoted asDP(α,G0), is characterized by a concentration parameterαand a base distribution
G0, acting as a distribution over discrete distributions. In time series and spatiotemporal forecasting, this
property is primarily leveraged through DP mixture models (DPMMs) to dynamically infer an unknown
or theoretically infinite number of latent components, temporal regimes, or spatial clusters directly from
the data (Emonet et al., 2013). For temporal modeling, the hierarchical DP hidden Markov model (HDP-
HMM) (Beal et al., 2001) extends the HDP (Teh et al., 2006) to sequential data by coupling state-specific
transition distributions through a shared hierarchical prior, allowing the number of latent states to be inferred
from the data (HMMs are discussed in Section 4.4.2). Standard HDP-HMMs, however, often over-segment
sequences because they rapidly switch among redundant states. The sticky HDP-HMM (Fox et al., 2011)
addresses this limitation by introducing a self-transition bias that encourages state persistence while retaining
nonparametric state inference and allowing each state’s observation distribution to be modeled flexibly via
DP mixtures. Recent works have also integrated DPs to enhance ensemble forecasting (Ren et al., 2023).
4.1.2.3 Bayesian Additive Regression Trees.Bayesian additive regression trees (BART) provide a
flexible BNP regression framework based on ensembles of regression trees (Chipman et al., 2010). BART
represents the regression function as a sum of weak learners, where regularization priors constrain individual
trees to avoid overfitting while allowing the ensemble to capture complex nonlinear relationships. Although
originally developed for classical machine learning tasks, BART has been extended to probabilistic forecast-
ing through multiple variants. For instance, Prüser (2019) applied BART to macroeconomic forecasting in
predictor-rich settings, demonstrating its ability to model nonlinear temporal relationships, while Mahdavi
et al. (2024) integrated BART into autoregressive distributed lag models to improve forecasting under non-
linear dynamics. Minnesota BART (Lima et al., 2025) introduces sparsity-inducing priors and structured
shrinkage for high-dimensional vector autoregressions. More recently, implicit quantile BART (IQ-BART)
(O’Hagan & Ročková, 2025) places a BART prior on the conditional quantile function and uses a check-
loss likelihood to learn it jointly across quantile levels. The resulting quantile function supports predictive
sampling and can capture multimodal distributions that may be missed by conventional parametric models.
4.1.3 Bayesian Neural Networks
Bayesianneuralnetworks(BNNs)extendclassicalneuralnetworksbytreatingthenetworkweightsasrandom
variables rather than deterministic parameters (Neal, 1996; Ghosh et al., 2019). Given the observed history
Y1:T, inference is performed over the posterior distribution of the weights,p(W |Y 1:T ). Probabilistic
forecasts for a future stateyT+h are then obtained by marginalizing over this posterior:
p(yT+h|Y 1:T ) =
∫
p(yT+h|Y 1:T,W)p(W|Y 1:T )dW,
wherep(yT+h|Y 1:T,W)represents the conditional predictive distribution parameterized by a specific weight
configuration. Exact posterior inference is generally intractable because of the high-dimensional and non-
linear parameter space. Consequently, BNNs rely on approximate inference techniques (Section 4.1.4), most
commonly variational inference and MCMC methods (Graves, 2011). The choice of prior distribution is
also important, particularly in highly overparameterized settings, where hierarchical shrinkage priors such
as the horseshoe prior can improve regularization by reducing the contribution of irrelevant parameters
(Ghosh et al., 2019). The flexibility of neural networks, combined with their ability to represent parameter
uncertainty, has motivated the use of BNNs across several forecasting domains, including macroeconomic
prediction using shrinkage priors and stochastic volatility modeling (Hauzenberger et al., 2025) and spa-
tiotemporal urban flood forecasting (Chu et al., 2024).
BNNs have also been extended to recurrent architectures by placing priors over recurrent weights and per-
forming inference over their posterior distribution, modeling uncertainty in both the sequential observations
and network parameters. For instance, the Bayesian autoregressive and RNN (BARNN) framework (Coscia
19

Preprint
et al., 2025) models the joint distribution of observations and time-varying network weights autoregressively,
sampling the weights at each time step from a variational posterior conditioned on past states. Similarly,
McDermott & Wikle (2019b) proposed BAST-RNN, a BRNN model for spatiotemporal forecasting by plac-
ing priors over recurrent weight matrices and applying MCMC-based inference. Recent work has improved
BNNs for large-scale spatiotemporal forecasting through scalable inference and informative priors, reducing
computational cost and sensitivity to prior specification (Duncker et al., 2023).
4.1.4 Approximate Bayesian Inference
Exact Bayesian inference is generally intractable for the complex models encountered in modern temporal
and spatiotemporal forecasting. Approximate Bayesian inference addresses this challenge by replacing exact
posterior computation with scalable approximations. Existing methods differ fundamentally in both their
computational efficiency and the quality of their posterior approximations. This section reviews four repre-
sentative approaches: Markov Chain Monte Carlo (Section 4.1.4.1), Monte Carlo Dropout (Section 4.1.4.2),
VariationalInference(Section4.1.4.3), andIntegratedNestedLaplaceApproximation(Section4.1.4.4). Their
characteristics and trade-offs are summarized in Table 4.
Table 4: Comparison of approximate Bayesian inference methods. Check marks (✓) denote restricted appli-
cability; crosses (✗) denote no restriction.
Method Approximation Strategy Model Restrictions Posterior Flexibility Computational Cost
Markov Chain Monte Carlo Posterior Sampling✗High High
Monte Carlo Dropout Dropout-based Variational✓ † Low Low
Variational Inference Optimization-based✗Moderate-High § Moderate
Integrated Nested Laplace Approximation Deterministic Approximation✓ ‡ Low-Moderate Low-Moderate ¶
†Requires a network trained with dropout regularization; not a post-hoc wrapper for arbitrary models.
§Depends on the chosen variational family.
‡Restricted to latent Gaussian models with exponential-family likelihoods.
¶Sub-quadratic complexity, though cost remains substantial for very large datasets.
4.1.4.1 Markov Chain Monte Carlo.MCMC methods represent the classical approach to approxi-
mate Bayesian inference by drawing samples from posterior distributions that cannot be evaluated analyt-
ically (Jones & Qin, 2022). MCMC constructs a Markov chain whose stationary distribution is the target
posterior, allowing posterior summaries and predictive quantities to be estimated from Monte Carlo samples.
The Metropolis-Hastings algorithm proposes candidate parameter values and accepts them with a probabil-
ity determined by the posterior-density ratio, adjusted for asymmetry in the proposal distribution (Hast-
ings, 1970). Metropolis-Hastings provides a general inference framework and has been widely adopted for
spatiotemporal forecasting, including Bayesian epidemiological models (Stojanović et al., 2019) and precipi-
tation nowcasting (Johnson et al., 2023). Alternatively, when full conditional distributions are analytically
tractable, Gibbs sampling becomes the standard inference approach (Geman & Geman, 1984). This method
sequentially updates each parameter by drawing directly from its respective conditional posterior, thereby
eliminating the need for an acceptance step. The method’s simplicity and computational efficiency have led
to its widespread adoption in frameworks such as BSTS models via simulation smoothing (Scott & Varian,
2014; Qiu et al., 2018), Gaussian mixture models for travel time forecasting (Chen et al., 2023), and Bayesian
hierarchical spatiotemporal models based on Gaussian Markov random fields (Rue & Held, 2005). Although
MCMC provides asymptotically exact Bayesian inference, its computational cost can be prohibitive for large
spatiotemporal forecasting problems with millions of parameters. Numerous extensions have been proposed
to improve scalability, including parameter expansion (McDermott & Wikle, 2019b) and ensemble Kalman
smoothing within Gibbs sampling (Johnson et al., 2023). These limitations have motivated approximate
inference methods that trade exact posterior sampling for greater computational efficiency.
4.1.4.2 Monte Carlo Dropout.Monte Carlo dropout (MCD) offers a scalable alternative by reinter-
preting dropout as approximate Bayesian inference. Gal & Ghahramani (2016a) established that a network
trained with dropout at ratepimplicitly minimizes the Kullback-Leibler (KL) divergence between a varia-
tional distributionq(W)induced by the dropout masks and the true posteriorp(W|Y 1:T ). This leads to
variational inference without requiring any modification to the training objective beyondℓ2 regularization.
20

Preprint
At inference time, dropout is kept active andMstochastic forward passes are performed. For a given fore-
cast horizonh, each pass applies an independently sampled mask to yield a predictionˆy(m) T+h. The resulting
ensemble{ˆy(m) T+h}M m=1 captures predictive variability induced by the approximate weight posterior. When
combined with an output likelihood that accounts for observation noise, it provides an empirical approxima-
tion to the posterior predictive distributionp(yT+h |Y 1:T ). From this ensemble, the predictive mean and
the epistemic variance are estimated as the sample mean and sample variance across theMforward passes,
respectively. For recurrent architectures, variational dropout applies a fixed dropout mask across all time
steps within a sequence, preserving temporal dependencies while maintaining the Bayesian interpretation of
the model (Gal & Ghahramani, 2016b). MCD has been combined with mean variance estimation to jointly
model epistemic and aleatoric uncertainty for wind speed, wind power, and load forecasting (Serpell et al.,
2019). The method has also been applied to financial time series prediction using Bayesian LSTMs for Bitcoin
price forecasting (Hassan, 2024) and to traffic breakdown probability forecasting using variational LSTMs
(Zechin & Cybis, 2023). For spatiotemporal forecasting, MCD has been integrated with GNNs to quantify
uncertainty in traffic flow forecasting (Hemavathi & Sumathi, 2026) and with convolutional architectures
for quantitative precipitation forecasting (Kim et al., 2026). However, the framework is constrained by the
restrictive variational family induced by the dropout mechanism, which underestimates posterior uncertainty
and offers limited flexibility for incorporating informative priors.
4.1.4.3 Variational Inference.Variational inference (VI) addresses the scalability limitations of
MCMC and the restricted approximation family of MC Dropout by formulating posterior inference as an
optimization problem (Blei et al., 2017). Given a family of tractable distributionsQ, VI seeks to find the
memberq ⋆(W)∈Qthat minimizes the KL divergence to the true posteriorp(W |Y 1:T ). Because this
divergence is itself intractable, optimization is performed by maximizing the evidence lower bound (ELBO):
ELBO(q) =E q(W) [logp(Y 1:T|W)]−KL (q(W)∥p(W)),
which decomposes into a data-fit term and a regularization term that penalizes deviation from the prior.
The most common variational family is the mean-field approximationq(W) =∏ jqj(Wj), which factorizes
over parameters and admits efficient coordinate ascent updates (Blei et al., 2017). In deep neural networks,
inference is performed using stochastic variational inference (Hoffman et al., 2013), where MC estimates of
the ELBO gradients are computed via the reparameterization trick (Kingma & Welling, 2014; Rezende et al.,
2014), enabling VI to scale to high-dimensional parameter spaces (Graves, 2011).
For spatiotemporal forecasting, Liu et al. (2020) proposed the variational Bayesian spatial temporal neural
network (STNN-VB), which places a Gaussian mixture variational posterior over the weights of a convolu-
tional gated recurrent unit (ConvGRU) for wind speed forecasting. Alternatively, Saad et al. (2024) intro-
duced the Bayesian neural field (BayesNF) framework, embedding mean-field variational inference within a
hierarchical BNN to map continuous spatiotemporal coordinates to the target field. VI is also used in the
deep latent variable models discussed in Section 4.4.4. Despite its scalability advantages, VI has several
limitations. The widely used mean-field approximation assumes independence between parameters, which
can underestimate posterior uncertainty and result in overconfident predictions (MacKay, 2003; Bishop,
2006). Similar issues arise in deep latent variable models, where an overly restrictive approximation can
cause posterior collapse, leading the latent variables to become uninformative as the approximate posterior
converges toward the prior (Sáez-Maldonado et al., 2026).
4.1.4.4 Integrated Nested Laplace Approximation.Integrated Nested Laplace Approximation
(INLA) provides a deterministic alternative to MCMC for latent Gaussian models (Rue et al., 2009). It as-
sumesathree-levelhierarchicalstructureinwhichobservationsY(s,t)atspatiallocationssfors∈{1,...,N}
are conditionally independent, given a latent Gaussian fieldXcomprising componentsX(s,t)and likelihood
hyperparametersθ 1. The observation model is typically assumed to belong to the exponential family. The
latent field is modeled as a Gaussian Markov random field (GMRF) with meanΥ(θ2)and precision matrix
Σ−1(θ2)that captures the spatiotemporal dependence structure of the data (Rue & Held, 2005). A prior
distribution is then assigned to the combined hyperparametersθ= (θ 1,θ 2). Given the observed history
21

Preprint
Y1:T, the resulting joint posterior is formulated as:
p(X,θ|Y 1:T )∝p(θ)p(X|θ 2)
N∏
s=1
T∏
t=1
p(Y(s,t)|X(s,t),θ 1),
wherep(θ)denotes the prior on the hyperparameters andp(X|θ 2)is the GMRF prior on the latent field.
The key advantage of INLA over MCMC is that it provides a fast and accurate approximation of posterior
marginals without requiring sampling (Rue et al., 2009).
A key enabler of INLA for spatiotemporal forecasting is the stochastic partial differential equation (SPDE)
approach of Lindgren et al. (2011), which represents Gaussian fields with Matérn covariance as GMRFs
defined over a finite element mesh. The formulation extends to spatiotemporal settings by allowing the
spatial field to evolve through a first-order autoregressive process (Cameletti et al., 2013). Consequently,
the resulting INLA-SPDE framework has become the dominant approach for many Bayesian spatiotemporal
forecasting models. For instance, Mahfoud et al. (2021) forecasted residential burglary across Amsterdam
neighborhoods, while Castro-Camilo et al. (2019) combined a spliced Gamma-Generalized Pareto likelihood
with an SPDE-based spatiotemporal field for short-term extreme wind speed forecasting. INLA has also been
widely applied in epidemiology and environmental monitoring, including COVID-19 hotspot detection using
exceedance probabilities (Jaya & Folmer, 2021), PM2.5 interpolation through spatial prediction models (Jaya
& Folmer, 2024), and dengue forecasting in Costa Rica (Chou-Chen et al., 2023) and Yogyakarta (Salim
et al., 2025). Despite its efficiency, INLA is restricted to latent Gaussian models with observation likelihoods
from the exponential family, limiting its applicability to more general non-Gaussian and deep latent models
(Rue et al., 2009).
4.2 Parametric Predictive Distributions
Parametric predictive distributions quantify uncertainty by specifying a distributional form for future ob-
servations and estimating its parameters from data. In these models, the forecasting architecture outputs
the parameters of the assumed distribution, which are then used to derive predictive intervals and quantiles.
This section reviews two main approaches which differ in flexibility of the predictive distribution. Single
parametric distributions (Section 4.2.1) assume a fixed family, such as the Gaussian distribution, whereas
mixture density networks (Section 4.2.2) extend this idea by learning input-dependent combinations of mul-
tiple distributions.
4.2.1 Single Parametric Distributions
The classical formulation of this approach models forecast uncertainty through a predefined distributional
family, with its parameters estimated from historical observations. Modern frameworks directly parame-
terize distributions inherently tailored to the data. For instance, Thorarinsdottir & Gneiting (2010) use
heteroskedastic censored (tobit) regression and truncated normal distributions for wind speed forecasting.
For nonnegative variables with mass at zero, Gneiting et al. (2006) introduced the cut-off Gaussian distri-
bution, which was adopted in the regime-switching space-time model to improve forecast calibration. More
recently, Salinas et al. (2020) introduced DeepAR, an RNN that maps previous hidden states and covariates
directly to the parameters of a chosen emission distribution, such as a Gaussian for real-valued targets or
a negative binomial for count data. To achieve this, the model maximizes the log-likelihood over the pre-
diction window and employs specialized activation functions, such as a softplus layer, to satisfy structural
constraints like positive scale parameters. More generally, frameworks like generalized additive models for
location, scale, and shape (GAMLSS) allow all parameters of these chosen distributions to vary flexibly as
functions of covariates (Merder et al., 2026).
Despite these developments, each parametric family remains limited by the assumptions of its chosen dis-
tribution and may struggle to capture complex predictive behaviors. A further limitation is the assumption
that errors are temporally independent. Zheng & Sun (2024) addressed this by learning the covariance
structure of errors over multiple steps using a low-rank-plus-diagonal parameterization and latent temporal
processes, improving calibration without increasing parameter size. An alternative non-parametric direction
22

Preprint
constructs predictive distributions by reweighting the empirical distribution of past observations, as in non-
parametric time series forecaster (NPTS) and its deep learning extension, DeepNPTS (Rangapuram et al.,
2023). However, DeepNPTS’ improved flexibility for non-Gaussian data comes at the expense of sample
efficiency. These advances highlight the need for more flexible probabilistic models capable of capturing
richer distributional structures.
4.2.2 Mixture Density Networks
While computationally simple, single parametric distributions lack the flexibility to capture complex, input-
dependent predictive uncertainties such as multimodality or asymmetric tails. Mixture density networks
(MDNs) (Bishop, 1994) overcome this by modeling the conditional predictive density as a weighted combi-
nation of multiple parametric components. Given the observed historyY1:T, a neural network estimates the
parameters of the mixture for a future stateyT+h:
p(yT+h|Y 1:T ) =
K∑
k=1
αk(Y1:T )ϕk(yT+h|Y 1:T ),
where the mixing coefficientsαk(·)are constrained such thatα k≥0and ∑K k=1αk = 1. Each component
densityϕ k is parameterized by a mean vectorµk(·)and a covariance matrixΣk(·). Trained by minimizing
the negative log-likelihood, MDNs generalize from a standard single distribution (K= 1) to a highly flexible
approximator of complex conditional densities as the number of componentsKincreases (Bishop, 1994).
MDNs have been applied extensively in forecasting problems where uncertainty is inherently non-Gaussian.
For wind power forecasting, Zhang et al. (2020) proposed an improved deep MDN that replaces Gaussian
components with beta distributions to respect the bounded nature of power generation. Similarly, for direc-
tional forecasting problems, Zhi et al. (2019) combined LSTM networks with von Mises mixture distributions
to model circular variables such as pedestrian movement directions, where Gaussian assumptions are inap-
propriate due to the periodic structure of the output space. In electricity price forecasting, Afrasiabi et al.
(2022) integrated Gabor feature extraction with a mixture density output layer to capture the multimodal
and volatile nature of price distributions. Recent work has focused on improving the training and scalability
of MDNs. Maximum likelihood training can become unstable when mixture components collapse or when
data is sparse. Yang et al. (2022) addressed this by replacing the negative log-likelihood with a Wasserstein
distance-based adversarial objective that compares the generated and observed distributions. For spatiotem-
poral forecasting, He et al. (2026) combined MDNs with GCNs to output multivariate Gaussian mixtures
with low-rank covariance. The number of mixture components in MDNs must be carefully selected, as insuf-
ficient components limit expressiveness while excessive components increase computational cost and training
instability (Bishop, 1994). Moreover, the number of parameters can grow rapidly in high-dimensional tasks,
further requiring efficient covariance parameterizations (He et al., 2026).
4.3 Distributional Regression
Distributional regression methods learn predictive uncertainty through the training objective, rather than by
specifying a parametric predictive distribution as in Section 4.2 (Kneib et al., 2023). The forecasting model
is trained to predict distributional quantities of interest, such as quantiles, intervals, or entire predictive dis-
tributions, making uncertainty estimation an integral part of the learning process. Fig. 5 illustrates the three
representative approaches reviewed in this section. Quantile regression (Section 4.3.1) estimates conditional
quantiles by minimizing the pinball loss. Engression (Section 4.3.2) learns the predictive distribution by
optimizing the energy score under a pre-additive noise model. Loss-driven interval estimation (Section 4.3.3)
optimizes interval quality without explicitly estimating densities. These methods differ in the predictive
quantities they recover and the associated modeling complexity, as summarized in Table 5.
4.3.1 Quantile Regression
Quantile regression (QR) estimates selected quantiles of the predictive distribution without requiring the
specification of a parametric distributional family (Koenker & Bassett, 1978), offering a flexible alternative
23

Preprint
Observed History Forecasting Model Loss-based learning of predictive uncertainty
Quantile Regression
Selected conditional quantiles
Engression
Empirical Predictive Distribution
Direct Prediction Interval
Loss-driven Interval Estimation
Figure 5: Overview of distributional regression approaches, including quantile regression, engression, and
loss-driven interval estimation.
Table 5: Comparison of distributional regression methods. Check marks (✓) denote recoverability of the full
predictive distribution; crosses (✗) denote otherwise.
Method Predictive Representation Full Distribution Primary Limitation Computational Cost
Quantile Regression Quantiles✗ † Quantile Crossing Low-Moderate
Engression Forecast Ensemble✓ ‡ Noise Specification Low-Moderate §
Loss-Driven Interval Estimation Prediction Interval✗Interval Optimization Low
†Only a finite set of quantiles is estimated; recovering the full density requires additional assumptions.
‡Recovered empirically through forward simulation, as an ensemble of sampled trajectories.
§Training cost scales quadratically in the number of noise realizationsMper instance, butMis typically small.
to the approaches discussed in Section 4.2. The conditional quantile for the future states at levelα∈(0,1)is
estimated by minimizing the pinball loss over the training set (Steinwart & Christmann, 2011). Estimating
multiple quantiles enables the construction of prediction intervals without specifying a parametric predictive
distribution, making QR suitable when the underlying distribution is unknown or difficult to model (Koenker
& Bassett, 1978; Koenker, 2005). QR has been widely adopted in probabilistic forecasting, particularly
in energy applications. Wan et al. (2017) proposed direct quantile regression for wind power forecasting,
improving both calibration and sharpness over kernel density estimation. Quantile regression neural networks
integrate QR with deep learning, replacing the linear predictor with a neural network to capture complex
nonlinear relationships (Cannon, 2011). At the regional scale, Yu et al. (2019) combined convolutional and
recurrent neural networks with quantile loss to capture spatial and temporal dependencies in aggregated
wind power generation. For large spatiotemporal systems, the high-dimensionality of the predictor space
presents an additional challenge. Agoua et al. (2019) addressed this using anℓ1-penalized quantile regression
model that performs variable selection while estimating conditional quantiles, enabling scalable probabilistic
forecasting for photovoltaic power generation across hundreds of spatially distributed sites.
A persistent challenge in QR is quantile crossing, where independently estimated quantiles violate their nat-
ural ordering. Existing solutions include constrained optimization, post-processing methods (Chernozhukov
24

Preprint
et al., 2010), and architectures that jointly estimate multiple quantiles while enforcing monotonicity (Moon
et al., 2021). Fakoor et al. (2023) proposed an alternative approach that combines a differentiable crossing
penalty during training with post-hoc isotonization operators such as sorting and the min-max sweep. They
also proposed deep quantile aggregation, where a neural network learns input-dependent weights to combine
multiple base quantile models. To forecast multiple quantiles over extended time horizons, Wen et al. (2017)
combined a recurrent encoder with a shared decoder for multi-horizon forecasting. At extreme quantile levels
where observations are scarce, Pasche & Engelke (2024) proposed extreme quantile regression neural net-
works (EQRN), which combine QR with extreme value theory (EVT). EQRN combines a recurrent network
for quantile estimation with RNN-parameterized generalized Pareto distributions to model conditional tails
for flood risk forecasting. However, QR estimates only a finite set of quantiles rather than the full predictive
density (Koenker, 2005). Recovering the full distribution therefore requires estimating many quantiles or
introducing additional assumptions, motivating more flexible probabilistic forecasting frameworks.
4.3.2 Engression
Engression, introduced by Shen & Meinshausen (2025), is a neural network-based distributional regression
framework that learns the conditional distribution of the target variable by optimizing the energy score over
a pre-additive noise model. Engression injects noise into the historical observations before passing them
through the network:yT+h =g(Y 1:T +ϵ 1:T ),rather than adding noise after the nonlinear transformation.
This allows the model to generate stochastic forecast trajectories from perturbed input sequences. For a
time stept, given a ground truth target sequenceyt+1:t+H of lengthHand the corresponding in-sample
predictions{ˆy(m) t+1:t+H}M m=1 forMindependent noise realizations from a predefined distribution, training
proceeds by minimizing the empirical energy score loss:
LES = 1 |D| ∑ D

 1
M
M∑
m=1
‖‖‖yt+1:t+H−ˆy(m) t+1:t+H ‖‖‖− 1 2M(M−1) M∑ m=1 M∑ k=1̸=m ‖‖‖ˆy(m) t+1:t+H−ˆy(k) t+1:t+H ‖‖‖  ,(2)
where|D|denotes the size of the training dataset. The first term penalizes deviation from the ground truth
and the second prevents mode collapse. Since the energy score is a strictly proper scoring rule (Gneiting
& Raftery, 2007), minimizing its negative formulation (Eq. 2) recovers the true conditional distribution.
Distinct plausible forecast trajectories can then be sampled from the trained model via forward simulation
using different noise samples, resulting in an empirical approximation of the predictive distribution. This
characteristic has motivated its application to several forecasting problems. For instance, Kraft et al. (2026)
integrated engression with LSTM networks for rainfall runoff forecasting. For multivariate and spatiotempo-
ral epidemiological forecasting, Pathak & Chakraborty (2026) proposed the multivariate engression network
(MVEN), the graph convolutional engression network (GCEN), and the spatiotemporal engression network
(STEN), extending engression to jointly capture temporal and spatial dependencies. More recently, Pathak
et al. (2026a) introduced Enformer and graph Enformer (GEnformer), which leverage Transformer architec-
tures to model long-range temporal dependencies and cross series interactions while improving computational
efficiency. The training procedure incurs a quadratic computational complexity in the number of generated
samplesM(Pathak et al., 2026a), although the models are typically lightweight for small values ofM.
4.3.3 Loss-Driven Interval Estimation
Loss-driven interval estimation encodes the desired properties of the predictive distribution into the training
objective. These approaches treat prediction interval estimation as an empirical risk minimization (ERM)
problem where the loss function balances interval coverage and width without requiring explicit quantile
estimation. The resulting models can be optimized with gradient-based methods, making them particularly
suitable for neural forecasting architectures. The quality driven (QD) loss introduced by Pearce et al. (2018)
represents one such approach to optimizing prediction intervals. The objective combines interval width
minimization with a penalty for insufficient coverage:
LQD =
∑T
t=1
(
ˆfU t − ˆfL t
)
kt
∑T
t=1kt
+λ T α(1−α) max
(
0,(1−α)−
∑T
t=1kt
T
)2
,
25

Preprint
where ˆfL t and ˆfU t denote the estimated lower and upper forecasting bounds at time indext, respectively,kt
is a differentiable approximation of whether the observation lies inside the estimated interval, andλbalances
the trade-off between interval width and coverage.kt is approximated using sigmoid functions, enabling the
objective to be optimized through backpropagation.
Several subsequent methods extend this coverage-width optimization approach. For instance, DeepPIPE
(Wang et al., 2020a) adapts the QD formulation to multi-horizon settings by introducing a unified loss func-
tion that jointly penalizes central point deviations and interval inefficiencies. The hybrid objective balances
a weighted Mean Absolute Error (MAE) for point accuracy with a quadratic penalty that is triggered during
undercoverage, while minimizing the mean prediction interval width. This framework can be incorporated
into a wide range of forecasting models, making it suitable for temporal and spatiotemporal applications
involving long forecasting horizons (Wang et al., 2020a). Despite the distribution-free nature and the ability
of these approaches to yield adaptive interval widths, the QD loss and DeepPIPE frameworks introduce
additional tuning hyperparameters and complicate gradient-based optimization due to their non-convex ob-
jectives. The Tube Loss (Anand et al., 2026) addresses this limitation by encoding the target coverage
through a piecewise quadratic loss function that is differentiable almost everywhere. For a target confidence
level1−α, the Tube Loss is formulated in terms of the lower and upper prediction errors, defined respectively
asl t =y t− ˆfL t andu t =y t− ˆfU t :
Lr 1−α(lt,ut) =



(1−α)u t, u t >0,
−αut, u t≤0, lt≥0,andru t + (1−r)l t≥0,
αlt, u t≤0, lt≥0,andru t + (1−r)l t <0,
−(1−α)l t, l t <0,
,
wherer∈(0,1)is a tunable parameter that controls the positioning of the interval along the response
trajectory. Optimization via ERM ensures that the resulting predictive intervals asymptotically achieve
the target coverage level. For forecasting applications, the Tube Loss has been integrated with LSTM for
probabilisticforecasting, achievingsuperiorperformance, competitiveintervalsharpnessandreducedtraining
cost compared to quantile-based and QD-based approaches across several datasets (Anand et al., 2026).
4.4 Generative Models
Generative models represent predictive uncertainty by learning a stochastic mechanism for the joint distribu-
tionp(y T+1:T+H |Y 1:T ), from which future trajectories can be generated (Bishop, 2006). This differs from
the approaches discussed in Section 4.2, where uncertainty is represented through an explicit parametric
form for the predictive density, and Section 4.3, where models optimize objectives associated with specific
distributional functionals, such as quantiles. Depending on the model, this distribution may admit tractable
likelihood evaluation or may be represented empirically through generated samples (Goodfellow et al., 2014;
Rezende & Mohamed, 2015; Ho et al., 2020).
We organize this section into nine families. Copula-based models (Section 4.4.1) separate the joint predic-
tive distribution into marginal distributions and an explicit dependence structure. Hidden Markov models
(Section 4.4.2) generate observations conditional on an evolving sequence of discrete latent states. Hierarchi-
cal discretization (Section 4.4.3) represents the predictive distribution through a coarse-to-fine partitioning
of the target space. Variational autoencoders (Section 4.4.4) learn continuous latent representations from
which forecast samples are generated, whereas generative adversarial networks (Section 4.4.5) learn an im-
plicit sampling mechanism. Normalizing flows (Section 4.4.6) transform a simple base density through a
sequence of invertible mappings, allowing complex predictive distributions to be modeled with exact like-
lihood evaluation. Diffusion models (Section 4.4.7) generate samples by reversing a progressive noising
process. Parametric prior mapping (Section 4.4.8) combines a learned latent prior with a non-invertible
generative mapping. Scenario-based methods (Section 4.4.9) produce a finite set of future trajectories with
explicit probabilities in a single forward pass. These families differ in how they represent the joint predictive
distribution, whether exact likelihood evaluation is tractable, and the cost of sampling at inference time, as
summarized in Table 6. Figure 6 provides a visual overview of the nine families.
26

Preprint
Observed time series Stochastic generative
mechanism
Forecast trajectories
 Predictive density
Copula-based Models Hidden Markov Models
 Hierarchical Discretization
Normalizing Flows
...
Generative Adversarial Networks
Real
(data)
Real /
fake
Parametric Prior Mapping
Non-invertible
Diffusion Models
Denoising steps
Variational Autoencoders
Enc Dec
Scenario-based Forecasting
Model
Observed Forecast
.
.
.
...
Figure 6: Overview of generative models for probabilistic forecasting.
The distinction between sampling-based uncertainty estimation and generative modeling is important for
two boundary cases in this taxonomy. Engression (Section 4.3.2) represents a boundary case, as it generates
forecast samples by passing noise-perturbed inputs through a learned nonlinear mapping. However, it is
classified as a distributional regression framework because it models the conditional distribution through a
regression framework optimized with the energy score, rather than learning a latent generative process for
the data distribution. Although its uncertainty is recovered from sampled trajectories, its formulation and
theoretical properties align with distributional regression. Copula-based models (Section 4.4.1) represent
another boundary case. According to Sklar’s theorem (Sklar, 1959), a copula combined with specified
marginal distributions defines a multivariate joint distribution, which could motivate their classification as
parametric models. However, the primary role of copulas in probabilistic forecasting is to construct the joint
dependence structure among multiple correlated series, rather than to specify the marginal uncertainty of
an individual target. This distinction is particularly relevant for modern neural copula models, which learn
flexible dependence structures beyond predefined copula families while preserving the objective of modeling
complex multivariate uncertainty. Therefore, copula-based models are grouped with generative approaches,
where the focus is on constructing joint predictive distributions.
27

Preprint
Table 6: Comparison of generative models for probabilistic forecasting. Check marks (✓) denote availability
of exact density evaluation; crosses (✗) denote otherwise. Abbreviation: Exact L. = Exact Likelihood.
Method Generative Mechanism Exact L. Sampling Procedure Inference Cost Key Limitation
Copula-based Models Dependence Modeling✓ † Simulation-based Low-Moderate High-dimensional dependence structure
Hidden Markov Models Latent State Modeling✓Simulation-based Low-Moderate • Limited capacity by discrete latent states
Hierarchical Discretization Discrete Target Representation✗Autoregressive Moderate-High Performance issues with limited data
Variational Autoencoders Latent Variable Modeling✗Single Forward Pass Low Mode collapse & limited generation quality
Generative Adversarial Networks Adversarial Learning✗Single Forward Pass Low Mode collapse & training instability
Normalizing Flows Invertible Transformations✓Single Forward Pass Low-Moderate Invertibility & expensive computation
Diffusion Models Iterative Denoising✗Iterative Denoising Moderate-High ¶ Slow sampling & high inference cost
Parametric Prior Mapping Push-forward Mapping✗Single Forward Pass Low Bandwidth-sensitive density estimation
Scenario-based Forecasting Discrete Scenario Generation✗Single Forward Pass Low Fixed number of scenarios; no density outside support
†Exact evaluation is restricted to copula models with tractable marginals, neural copulas require approximate inference.
•Cost increases with the sequence length and number of latent states.
¶Dependent on diffusion steps; latent diffusion reduces this via space compression (Section 4.4.7.3).
4.4.1 Copula-Based Models
Copula-based methods separate the modeling of marginal distributions from the dependence structure among
variables. According to Sklar’s theorem (Sklar, 1959), any multivariate distribution can be decomposed into
its univariate marginals and a copula capturing their dependence:
F(y 1,...,y N) =C
(
F1(y1),...,F N(yN)
)
,
whereF i are the marginal cumulative distribution functions andCis the copula capturing their dependence
(Nelsen, 2006). This decomposition provides a flexible framework that allows marginals to be modeled inde-
pendently while preserving the joint dependencies. Therefore, copulas have become a prominent approach
for probabilistic forecasting. However, explicitly modeling dependencies becomes challenging as the number
of variables grows, since the number of pairwise relationships scales quadratically with dimensionality. Sali-
nas et al. (2019) addressed this by combining an autoregressive recurrent network for modeling temporal
dynamics with a low-rank Gaussian copula process, in which a low-rank-plus-diagonal covariance reduces the
parameter count. In a different direction, Sun & Yu (2024) developed copula conformal prediction for time
series (CopulaCPTS), which constructs marginal conformal predictive distributions at each horizon step and
subsequently fits an empirical copula to capture dependencies among future prediction errors.
The ability of copulas to represent complex dependence structures has also motivated their integration into
spatiotemporal forecasting. Among the various copula constructions, vine copulas (Joe, 1996) provide a
flexible framework for modeling high-dimensional dependence by decomposing a multivariate distribution
into a hierarchy of bivariate copulas. For instance, Erhardt et al. (2015) extended regular-vine (R-vine) cop-
ulas (Joe et al., 2010) to spatiotemporal forecasting by parameterizing pairwise dependencies as functions of
geographical distance, yielding superior probabilistic temperature forecasts across German weather stations
compared to Gaussian spatial models. However, scaling R-vine copulas to large spatiotemporal systems
remains challenging due to the increasing complexity of the vine structure. Zhang et al. (2026) addressed
this limitation by combining R-vine copulas with Kolmogorov-Arnold Networks (KANs) (Liu et al., 2025e)
for regional wind power forecasting. Copula models have also been adopted for incomplete spatiotempo-
ral observations. An et al. (2025) employed copulas to estimate the joint distribution of missing traffic
measurements, enabling forecasting and data imputation within a unified probabilistic framework.
Another challenge in copula-based forecasting is jointly improving point prediction accuracy and uncertainty
calibration. Kim & Kim (2026) proposed a two-stage copula network (TSCoNet), which combines a hybrid
convolutional neural network (CNN)-LSTM predictor with a Gaussian copula to jointly model point forecasts
and multivariate uncertainty. As forecasting problems become increasingly high-dimensional and irregular,
recent work has explored neural parameterizations of copulas to improve scalability and flexibility. Ashok
et al. (2024) introduced an improved version of Transformer-attentional copulas for time series (TACTiS-
2), which addresses the difficulty of learning valid neural copulas by separating the estimation of marginal
distributions and dependence structures. TACTiS-2 reduces the number of distributional parameters in
TACTiS (Drouin et al., 2022) while enabling scalable probabilistic forecasting for high-dimensional and
irregularly sampled time series. Another active direction focuses on dynamic copulas whose dependence
28

Preprint
structure evolves over time. Zito & Kowal (2025) proposed a Bayesian dynamic copula model that jointly
learns nonparametric marginal distributions and time-varying dependence through a Gaussian copula with
a dynamic factor structure, providing fully Bayesian probabilistic forecasts for multivariate time series.
Similarly, Li et al. (2026c) combined LSTM and generalized autoregressive conditional heteroskedasticity
difference-residual modeling with R-vine copulas to characterize the evolving dependence between wind and
solar power generation, enabling joint uncertainty quantification for renewable energy forecasting.
4.4.2 Hidden Markov Models
Hidden Markov models (HMMs) are latent variable models that represent a time series as observations
generated from a sequence of unobserved states that evolve according to a Markov process (Zucchini et al.,
2016). For the observed historyY 1:T ={y t}T t=1 and a corresponding sequence of hidden statesH 1:T =
{ht}T t=1, an HMM is defined by a state transition modelp(ht|h t−1)and an observation modelp(y t|h t).
The joint distribution factorizes as:
p(Y1:T,H 1:T ) =p(h 1)
T∏
t=2
p(ht|h t−1)
T∏
t=1
p(yt|h t).
The model parameters are typically estimated via EM through the Baum-Welch procedure (Baum et al.,
1970) and forecasts are produced by propagating uncertainty over future state transitions.
Early spatiotemporal applications, such as Zucchini & Guttorp (1991), modeled spatial dependencies by
assuming observations across locations were conditionally independent given a shared hidden (weather)
regime to avoid the computational burden of modeling the full joint distribution. Later works relaxed the
assumptions of fixed transition dynamics and a predefined number of states of standard HMMs. For instance,
non-homogeneous HMMs allow transition probabilities to depend on external covariates, enabling the model
to adapt to changing environmental conditions and seasonal effects (Tezcan & Garcia, 2025). The infinite
hidden Markov model (InfHMM) further removes the need to specify the number of states in advance by
placing nonparametric Bayesian priors over state transitions (Âzeddine Frimane et al., 2022). More flexible
variants relax the model’s conditioning structure. Input-output HMMs (IOHMMs) (Bengio & Frasconi, 1994)
incorporate external inputs into both the transition and observation models. For example, they can combine
environmental covariates and historical activity data with latent behavioral states to forecast trajectories
while retaining interpretability through the learned transitions (Liu et al., 2026). Multi-observation HMMs
(MOHMMs) instead allow several correlated variables to be generated from the same hidden state. This
approach is useful in solar forecasting, where multiple meteorological variables jointly reflect a latent weather
condition (Zhang & Shang, 2025). Each of these extensions relaxes a specific assumption of standard HMMs,
while retaining the same core representation of discrete latent regimes with state-specific observation models.
4.4.3 Hierarchical Discretization
Hierarchical discretization models the predictive distribution over a discretized representation of the target
variable. The core idea is to partition the support of the target into a finite set of bins and predict the
probability of falling into each bin using a categorical distribution (Bergsma et al., 2022; Liu & Wang,
2024). This approach places no shape constraints on the resulting density and naturally accommodates
multimodality, discrete targets, and mixed data types. A basic implementation uses uniform binning over
the range of the target variable, but this introduces a trade-off between resolution and efficiency, since
higher precision requires a rapidly growing number of bins. Bergsma et al. (2022) addressed this through the
coarse-to-fine autoregressive (C2FAR) framework, which introduces a generative hierarchical discretization
strategy. A scalar target valueyis represented as a vector ofBindices,(y 1,...,y B), wherey 1 identifies a
coarse bin and each subsequentyi refines the estimate within the bin identified byyi−1. In practice, C2FAR
uses an LSTM to capture temporal dependencies while the hierarchical categorical outputs characterize
predictive uncertainty at each level of the hierarchy (Bergsma et al., 2022). To handle unbounded support, a
parametric tail distribution, such as the Pareto distribution, is appended to the finest level. A conceptually
similar approach is the hierarchical discrete Transformer (HDT) (Shibo et al., 2025), which reformulates
multivariate forecasting as a token generation task by encoding time series into discrete representations via
29

Preprint
ℓ2-normalized vector quantization. This hierarchical framework first extracts low-level tokens to capture
overarching long-term trends, which subsequently condition the generation of high-level tokens to accurately
model fine-grained dynamics over extended prediction horizons. The extension of the framework by Bergsma
et al. (2022) to spatiotemporal settings remains an open direction. Additionally, the hierarchical factorization
introduces a sequential dependency across precision levels that increases inference cost relative to methods
that produce distributional outputs in a single forward pass.
4.4.4 Variational Autoencoders
Variational autoencoders (VAEs), introduced by Kingma & Welling (2014) and Rezende et al. (2014), are la-
tent variable generative models that learn a probabilistic representation of the data by mapping observations
to a latent distribution (Kingma & Welling, 2019). Given the observationsY1:T, an encoder approximates
the posteriorq ϕ(z|Y 1:T ), from which a latent variablezis sampled and decoded to generate the future
trajectory. Model training maximizes the ELBO (Kingma & Welling, 2014), which balances reconstruction
accuracy with regularization of the latent representation toward a prior distribution. Learning a distribution
over these latent variables enables probabilistic forecasting by sampling from the learned latent space.
Early temporal latent variable models extended VAEs with recurrent architectures to capture sequential
dynamics. Frameworks such as variational recurrent autoencoders (Fabius & Van Amersfoort, 2014) and
variational RNNs (Chung et al., 2015) introduced recurrent states to model time-varying latent distributions.
ProTran (Tang & Matteson, 2021) replaces recurrent latent dynamics with self-attention, allowing each latent
variable to depend on the entire history rather than only the previous state. Later, Koyuncu et al. (2024)
proposed an efficient variant, E-ProTran, which removes autoregressive attention and restricts sampling to
the final layer, achieving comparable performance with substantially faster inference. Vector autoregression-
VAE (VAR-VAE) (Leushuis, 2025) takes a different approach by constraining the latent dynamics with a
first-order VAR process, improving robustness to noisy observations and producing more stable probabilistic
forecasts. Tostabilizetrainingunderdatascarcity, thediffusion, denoise, anddisentanglementVAE(D 3VAE)
model (Li et al., 2022) combines a bidirectional VAE with a diffusion-based noise-augmentation scheme (see
Section 4.4.7) and a score-matching denoising module. For long-term forecasting, Wu et al. (2025) proposed
K2VAE, which transforms nonlinear time series into a linear dynamical system using a learnable Koopman
operator (KoopmanNet) and refines predictions and uncertainty through a Kalman-like filtering mechanism
(KalmanNet) to mitigate error accumulation over extended horizons.
VAEs have also been extended to spatiotemporal forecasting by integrating GNNs to capture spatial de-
pendencies. Graph-based ensemble forecasting model (Graph-EFM) (Oskarsson et al., 2024) introduces
stochastic latent variables on a hierarchical graph representation of the atmosphere, allowing uncertainty to
propagate across multiple spatial resolutions while producing calibrated ensemble weather forecasts. Holm-
berg et al. (2026) extended this approach to global and regional ocean forecasting with Njord, adapting the
hierarchical graph structure to irregular ocean geometries and incorporating physical constraints to model
ocean and sea ice dynamics. However, VAE-based forecasting models remain susceptible to posterior collapse
and the smoothing effects associated with the ELBO objective, discussed in Section 4.1.4.3, which can limit
their ability to capture complex predictive distributions (MacKay, 2003; Sáez-Maldonado et al., 2026). These
limitations have motivated alternative generative approaches, including GANs (Goodfellow et al., 2014) and
diffusion models (Ho et al., 2020), which rely on adversarial learning and iterative denoising, respectively.
4.4.5 Generative Adversarial Networks
Generative adversarial networks (GANs), introduced by Goodfellow et al. (2014), learn a data distribution
through an adversarial game between two neural networks. Training is formulated as a minimax objec-
tive, where a generatorGmaps a latent variablez∼p(z)to a synthetic sample, while a discriminator
Ddistinguishes these generated samples from real observations. GANs learn to generate samples without
defining an explicit predictive distribution, making them highly suitable for probabilistic forecasting (Gao
et al., 2022). However, the adversarial objective was originally developed for independent observations and
does not account for temporal or spatial dependence, motivating forecasting-specific adaptations (Pacchiardi
et al., 2024).
30

Preprint
Early applications of GANs in forecasting focused on predicting multimodal trajectories. Social GAN (Gupta
et al., 2018) combined an LSTM generator with a social pooling mechanism to generate multiple plausible
pedestrian trajectories, introducing a diversity loss to encourage multimodal predictions. Spatiotempo-
ral interaction graph attention GAN (STI-GAN) (Huang et al., 2021) subsequently replaced the pooling
mechanism with graph attention, allowing the generator to model spatial interactions jointly with temporal
dynamics and improving trajectory prediction in crowded scenes. GANs were also extended to a broader
range of spatiotemporal problems. For example, ImaGINator (Wang et al., 2020b) incorporated a spatiotem-
poral fusion mechanism through encoder-decoder skip connections to preserve appearance while generating
realistic video dynamics. However, adversarial training remains a major limitation of GAN-based frameworks
because maintaining training stability and calibrated uncertainty is challenging in high-dimensional settings
(Gao et al., 2022). Pacchiardi et al. (2024) addressed this limitation by replacing the adversarial objective
with the optimization of proper scoring rules, such as the energy and kernel scores (Gneiting & Raftery,
2007), over sequential forecasts. The proposed framework accounts for temporal dependence through se-
quential conditioning and was later extended to spatiotemporal forecasting using patched scoring rules that
evaluate localized spatial regions.
4.4.6 Normalizing Flows
Normalizing flows, introduced by Tabak & Turner (2013) and comprehensively reviewed by Papamakar-
ios et al. (2021), are a family of generative models that construct expressive probability distributions by
transforming a simple base distribution,pZ(z), into a complex data distribution,pθ(y), through a sequence
of invertible and differentiable transformations. Because the mapping is bijective, it can be evaluated in
reverse for exact density estimation. Given an observation sequencey, the flow learns the mappingfθ that
transforms the data back into the latent base space. The exact density of the observed sequence is then
obtained via the change-of-variables formula:
pθ(y) =pZ(fθ(y))·
⏐⏐⏐⏐det∂fθ(y) ∂y ⏐⏐⏐⏐,
where the Jacobian determinant accounts for the change in volume induced by the transformation (Papa-
makarios et al., 2021). This enables exact likelihood evaluation and efficient sampling, making normalizing
flows a powerful alternative to GANs and VAEs. In the context of probabilistic forecasting, this framework
is typically conditioned on the observed historyY 1:T to model the highly flexible conditional predictive
densityp(y T+h|Y 1:T )of future states. As the model is autoregressive, the predictive distribution factorizes
over the forecast horizon, with each factor obtained by applying the change-of-variables at a single time step
(Rasul et al., 2021b).
In practice, conditional normalizing flows are commonly implemented using affine coupling layers, such as
real-valued non-volume preserving (Dinh et al., 2017), whose triangular Jacobian enables efficient likelihood
computation and exact inversion. Early forecasting models combined conditional normalizing flows with
autoregressive sequence models. Transformer-MAF (Rasul et al., 2021b) integrates a masked autoregressive
flow (MAF) (Papamakarios et al., 2017) with a Transformer decoder, using masked self-attention to condition
each flow transformation on the complete observed history. Subsequent works extended flow-based models
to spatiotemporal forecasting by incorporating explicit spatial representations into the conditioning mecha-
nism. Spatial-temporal graph conditionalized normalizing flow (STGNF) (An et al., 2024) integrates GNNs
with conditional normalizing flows, allowing local and global spatiotemporal dependencies learned from traf-
fic networks to parameterize the flow transformations and yield probabilistic traffic forecasts. MotionFlow
(Zand et al., 2023) instead employs masked convolutions to model spatial autoregressive dependencies for
probabilistic trajectory prediction. Recent work has expanded normalizing flows to non-Euclidean domains.
For land deformation forecasting, DyLand (Xu et al., 2024) combines neural ordinary differential equations
with topology-preserving mappings to model evolving spatial manifolds. Normalizing flows have also been
adapted to extreme value analysis. For instance, De Monte et al. (2025) introduced hyperspherical flow
transformations to model multivariate extremes, mapping the data onto spherical manifolds to estimate the
directional distributions of rare events. Irregularly sampled multivariate time series present another chal-
lenge, as conventional coupling layer architectures assume a fixed-dimensional input. ProFITi (Yalavarthi
31

Preprint
Observed time series
 Probabilistic Forecast
Diffusion Models
DDPM - discrete diffusion in data space
Score-based diffusion - continuous time in
data space
Latent diffusion - discrete diffusion in
latent space
...
Figure 7: Overview of diffusion models, including DDPM, score-based, and latent diffusion models.
et al., 2025) addresses this limitation by replacing fixed-dimensional coupling layers with an invertible at-
tention mechanism conditioned on graph-based representations of observed and queried time-channel pairs.
Hence, the flow can model joint distributions over a variable number of targets. However, the computational
cost of invertible transformations and Jacobian evaluations remains a fundamental challenge for applying
normalizing flows to high-dimensional forecasting tasks (Papamakarios et al., 2021).
4.4.7 Diffusion Models
Diffusion models are latent variable generative models originally introduced from a thermodynamic per-
spective (Sohl-Dickstein et al., 2015) and later formalized for deep generative modeling (Ho et al., 2020).
They generate samples by reversing a predefined diffusion process that progressively perturbs the target with
Gaussian noise. In time series forecasting, this process is conditioned on historical observations to model
the distribution of future trajectories, enabling uncertainty quantification by generating multiple plausible
forecasts (Rasul et al., 2021a). Readers are referred to Yang et al. (2026) for a comprehensive survey on
diffusion models for time series and spatiotemporal forecasting. Diffusion models appeal for their distribu-
tional flexibility and the stability of their training objective compared to adversarial approaches. However,
their iterative sampling procedure introduces high computational costs, motivating a range of approaches
to improve sampling efficiency, conditioning mechanisms, and the representation of temporal uncertainty
(Rasul et al., 2021a; Tang et al., 2024; Ye et al., 2025). More recently, these models have been extended
to spatiotemporal forecasting by incorporating spatial dependencies into the diffusion process (Wen et al.,
2023; Chen et al., 2024; Cachay et al., 2023). We categorize diffusion-based forecasting methods into three
groups, as illustrated in Fig. 7: denoising diffusion probabilistic models (Section 4.4.7.1), score-based dif-
fusion models (Section 4.4.7.2), and latent diffusion models (Section 4.4.7.3). Table 7 summarizes the key
characteristics of these diffusion models.
32

Preprint
Table 7: Comparison of diffusion model formulations for probabilistic forecasting.
Property Denoising Diffusion Probabilistic Model Score-based Diffusion Model Latent Diffusion Model
Key IdeaDiscrete Diffusion Process Continuous-time Diffusion Latent-Space Compression
Time ParameterizationDiscrete Steps Stochastic Differential Equation Discrete Steps
Training ObjectiveDenoising Objective Denoising Score Matching Denoising Objective
Generation SpaceData Space Data Space Latent Space
Sampling CostHigh High Low-Moderate
4.4.7.1 Denoising Diffusion Probabilistic Models.Denoising diffusion probabilistic models
(DDPMs) represent the foundational class of diffusion-based generative models (Ho et al., 2020). They
define a forward diffusion process that corrupts the target sample with Gaussian noise over multiple diffu-
sion steps. A key property of this process is that the noisy sample at any diffusion step can be obtained
directly from the original sample, enabling efficient training by avoiding the sequential simulation of the
forward process. Instead of predicting reverse transition probabilities directly, DDPMs parameterize the
reverse process by training a neural network to estimate the injected noise. This defines the reverse process
used during inference to iteratively transform Gaussian noise into samples from the learned data distribution
(Ho et al., 2020).
The first application of DDPMs to probabilistic forecasting was TimeGrad (Rasul et al., 2021a), which
conditions the denoising network on an RNN hidden state summarizing historical observations. TimeGrad
models the conditional distribution of each future time step through a diffusion process. However, its au-
toregressive formulation requires a complete diffusion process for every predicted time step, scaling inference
cost linearly with both the forecasting horizon and the number of diffusion steps. Subsequent work ad-
dressed this limitation with conditional diffusion models, by jointly diffusing the entire forecast horizon and
incorporating the conditioning informationcinto the reverse process.cencodes information used to guide
the generation process, such as historical observations, graph structure, or auxiliary covariates (Yang et al.,
2026). TimeDiff (Shen & Kwok, 2023) was the first conditional diffusion model designed for forecasting. It
constructs the conditioning signalcusing future mixup and autoregressive initialization to better capture
temporal dependencies during denoising. Furthermore, it departs from conventional DDPMs by predicting
the clean sampley (0) directly instead of the injected noise, to account for the fact that real-world time
series noise is more irregular than standard Gaussian noise (Shen & Kwok, 2023). Transformer-modulated
diffusion model (TMDM) (Li et al., 2024) simplifies distribution learning by using a Transformer to esti-
mate the conditional mean forecast, thus restricting the forward and reverse diffusion processes to modeling
only the residual distribution. DiffSTG (Wen et al., 2023) extends conditional diffusion to spatiotemporal
forecasting by conditioning on both a masked spatiotemporal sequence and spatial structure. The masked
sequence enables the entire forecast horizon to be generated through a single reverse diffusion process, while
the denoising network combines a U-Net architecture with graph convolutions (Ronneberger et al., 2015) to
model temporal and spatial dependencies jointly.
A limitation of early DDPM forecasters is the assumption of stationary noise variance, which fails to capture
the changing uncertainty patterns common in real-world time series. To address this limitation, nonstation-
ary diffusion (NsDiff) (Ye et al., 2025) replaces the conventional additive noise formulation with a location
scale noise model, allowing the diffusion process to capture time-varying uncertainty. A second direction
modifies the denoising process itself. Multi-granularity time series diffusion (MG-TSD) (Fan et al., 2024)
introduces intermediate supervision across multiple temporal granularities during the denoising phase, en-
couraging the model to preserve long-term trends while progressively refining local dynamics. Extending
DDPMs to spatiotemporal forecasting, dynamic spatial-temporal (DST)-DDPM (Chen et al., 2024) combines
a dynamic graph encoder that learns time-varying adjacency matrices with a Transformer-based denoising
network for air quality forecasting. Alternatively, spectral diffusion for spatiotemporal graph (SpecSTG)
(Lin et al., 2025b) performs diffusion in the graph spectral domain, where spatial correlations are repre-
sented through graph Fourier coefficients and conditioned using a spectral GRU. This formulation reduces
the cost of modeling spatial structure while maintaining competitive probabilistic forecasting performance.
For trajectory forecasting, UTD-PTP (Tang et al., 2024) adapts DDPMs to pedestrian movement by pairing
a Transformer sequence encoder with a denoising diffusion implicit model (DDIM) sampler. This compresses
33

Preprint
the multi-step reverse process into a few iterations, accelerating inference while preserving sample diversity.
The iterative reverse process of DDPM models is computationally expensive for long horizons, although
accelerated samplers like DDIM offer partial mitigation. This motivates alternative diffusion formulations
designed for more efficient forecast generation.
4.4.7.2 Score-Based Diffusion Models.Score-based diffusion models formulate the diffusion process
in continuous time through a stochastic differential equation (SDE) rather than a discrete sequence of
diffusion steps (Song et al., 2021). The forward process gradually perturbs the data according to:
dyτ =f(y τ,τ)dτ+g(τ)dw τ,
whereτ∈[0,τ max]denotes the continuous diffusion time,w τ is a standard Wiener process, andf(·,τ)
andg(τ)define the drift and diffusion coefficients, respectively. Sample generation is performed by solving
the corresponding reverse-time SDE, which depends on the score function∇yτ logpτ(yτ)estimated through
denoising score matching. Compared to DDPMs, the continuous formulation removes the need to specify a
discrete diffusion schedule and provides greater flexibility in the design of diffusion trajectories (Song et al.,
2021; Yan et al., 2021). ScoreGrad (Yan et al., 2021) first introduced score-based diffusion to probabilistic
forecasting by replacing TimeGrad’s discrete diffusion process with a continuous SDE formulation. The
modelintegratestemporalfeatureextractionwithconditionalscorematchingtoreducesensitivitytodiffusion
hyperparameters.
Continuous score-based diffusion has also been extended to spatiotemporal forecasting. ProGen (Gong et al.,
2024) integrates GNNs within the SDE framework to capture spatial dependencies for traffic forecasting.
GenCast (Price et al., 2025) applies the same continuous-time formulation, following the parameterization
of Karras et al. (2022), to global weather forecasting. GenCast conditions each diffusion process on the two
most recent atmospheric states to model the distribution of the next state. Alternative approaches modified
the forward diffusion process itself. For instance, dynamics-informed diffusion (DYffusion) (Cachay et al.,
2023) defines the forward process through temporal interpolation rather than Gaussian noise injection. The
model operates on spatiotemporal dynamical systems, such as spatial grids or meshes, and captures spatial
dependencies using CNN and U-Net architectures. A stochastic interpolator learns the forward process, while
a forecasting network approximates the reverse process, reducing the number of diffusion steps required for
sampling without sacrificing probabilistic forecasting performance. For forecasting under extreme conditions,
He & Hu (2025) proposed a score-based conditional diffusion model for offshore wind power prediction during
typhoons. The framework employs a mean-reverting SDE alongside deterministic forecast networks to reduce
the complexity of the denoising process. However, the need to repeatedly solve the reverse SDE remains a
computational limitation of such models.
4.4.7.3 Latent Diffusion Models.Latent diffusion models reduce the computational cost by perform-
ing the denoising process in a compressed latent space rather than in the original data space (Rombach et al.,
2022). The framework first learns an encoder-decoder pair that maps observations into a lower-dimensional
representationz=E(y)and reconstructs the original data throughy=F(z). Diffusion is then applied to
the latent representation instead of the original signal. This reduces the dimensionality of the generative
process and enables more efficient sampling for high-dimensional forecasting tasks. Feng et al. (2024) intro-
duced latent diffusion Transformer (LDT) for multivariate time series forecasting. LDT uses an adaptive
normalization mechanism to improve robustness under distribution shifts and performs non-autoregressive
generation in the latent space, reducing the computational burden of long-horizon forecasting. Latent diffu-
sion is also used in trajectory forecasting (Yang et al., 2026). For instance, learning autoencoder diffusion
model (LADM) (Lv et al., 2024) pairs a VAE with a diffusion refiner. In this setup, a generator pro-
duces coarse trajectories, which the diffusion model then sharpens within the latent space, simplifying the
refinement process and generating higher-quality future movements. For spatiotemporal forecasting, solar
high-resolution adaptive diffusion ensemble forecasting (SHADECast) model (Carpentieri et al., 2025) ap-
plies latent diffusion to high-dimensional solar irradiance fields by compressing spatiotemporal observations
into a latent representation. Although latent models mitigate the computational burden of high-dimensional
forecasting, their performance depends on the quality of the learned representation and the ability of the
latent space to preserve the original data characteristics.
34

Preprint
4.4.8 Parametric Prior Mapping
Parametric prior mapping (PPM) (Li et al., 2026a) relaxes the invertibility requirement of normalizing flows
while avoiding the iterative sampling procedure of diffusion models. The framework combines a learned
context-dependent prior with a non-invertible neural mapping, replacing the fixed latent distributions used
in diffusion models and the bijective transformations required by normalizing flows. Given the observed
historyY 1:T, an encoder estimates the parameters of a multivariate Gaussian latent prior:
pθ(z|Y 1:T ) =N(µ θ(Y1:T ),Σ θ(Y1:T )),
wherezis the latent vector, andµ θ(·)andΣ θ(·)represent the learned mean vector and covariance matrix,
respectively. The joint predictive distribution over the forecast horizon is then obtained as the push-forward
distribution:
qϕ(yT+1:T+H |Y 1:T ) = (gϕ)#pθ(z|Y 1:T ),
where(g ϕ)# denotes the push-forward measure induced by the neural mappinggϕ. Forecasts are generated
in a single forward pass throughgϕ, eliminating the iterative denoising procedure of diffusion models. At
the same time, removing the invertibility constraint permits the use of more flexible neural architectures
than those employed in normalizing flows. This combination substantially reduces inference time while
maintaining competitive probabilistic forecasting performance. Sincegϕ is not invertible, exact likelihood
evaluation is intractable. Training, therefore, combines a kernel density estimation-based negative log-
likelihood with a mean squared error term that regularizes the sample mean and stabilizes optimization (Li
et al., 2026a).
4.4.9 Scenario-Based Probabilistic Forecasting
Analternativetosampling-basedgenerativemodelsistopredictafinitesetoffuturetrajectories, orscenarios,
together with their associated probabilities. In contrast to diffusion and other sampling-based approaches,
scenario-based methods produce explicit {scenario, probability} pairs in a single forward pass. Thus, such
approaches resolve major sampling limitations, specifically the absence of explicit probabilities for trajecto-
ries, inadequate coverage of rare events, and high inference cost (Dai et al., 2026). Most existing approaches
build on multiple choice learning (Guzmán-rivera et al., 2012), where a multi-head network is trained under
a winner-takes-all (WTA) loss so that only the head closest to the ground truth receives a gradient update,
encouraging each head to specialize in a distinct mode of the conditional distribution (Rupprecht et al.,
2017). TimeMCL (Cortes et al., 2025) first adapted multiple choice learning to probabilistic time series fore-
casting by training a multi-head autoregressive network with a WTA loss. However, strict WTA objective
hinders training stability by causing hypothesis collapse, where only few heads receive sufficient gradient
updates while the rest remain underutilized. Subsequent work has focused on mitigating this limitation.
TimePre (Jiang et al., 2026) introduces stabilized instance normalization to reduce scale disparities between
variables, improving optimization stability and preserving hypothesis diversity while retaining the efficiency
of lightweight linear forecasting backbones. TimePrism (Dai et al., 2026) further simplifies the architecture
by decomposing inputs into trend and seasonal components, which are combined to generate a larger set
of candidate scenarios. A parallel linear layer then predicts scenario probabilities, while a relaxed WTA
objective improves the utilization of all prediction heads. TimePrism outperformed generative baselines
across benchmarks at a fraction of the inference cost since its cost remains fixed regardless of the number of
requested scenarios.
5 Foundation Models for Probabilistic Forecasting
Originating from natural language processing, recent advances in large-scale pretraining have led to the emer-
gence of foundation models for time series forecasting (Kottapalli et al., 2025). In contrast to conventional
forecasting models that are trained separately for individual datasets, foundation models are pretrained on
large and diverse collections of time series spanning multiple domains, sampling frequencies, and forecasting
horizons. They are subsequently adapted to forecasting tasks through zero-shot inference or lightweight
fine-tuning, enabling strong transferability with minimal task-specific training (Liang et al., 2024; Zhao
35

Preprint
Lag-Llama
Parametric Student-t
2023 2024
Moirai
Predictive mixture distributions
Chronos
Autoregressive token sampling
2025
TimesFM
Point forecaster (quantile adaptation)
 Covariate-aware token sampling
Chronos-2
Sundial
Flow matching generative sampling
2026
TiRex
Direct quantile forecasting
Figure 8: Evolution of time series foundation models for probabilistic forecasting.
et al., 2026). While several prominent foundation models such as Timer-XL (Liu et al., 2025c) and IBM’s
TTM (Ekambaram et al., 2024) remain dedicated to deterministic point forecasting, the field is increasingly
shifting its focus toward capturing uncertainty. Consequently, foundation models have accelerated progress
in probabilistic forecasting by estimating predictive uncertainty as an intrinsic part of the forecasting pro-
cess. Instead of relying on post-hoc uncertainty estimation, modern foundation models directly produce
predictive distributions through probabilistic mechanisms such as parametric distribution prediction, quan-
tile regression, generative sequence modeling, and mixture distributions. Fig. 8 summarizes the evolution of
probabilistic time series foundation models.
5.1 Uncertainty Quantification in Foundation Models
Foundation models differ not only in their architectures but also in how they estimate predictive uncertainty.
We organize existing approaches according to their probabilistic formulation into five categories. Table 8 pro-
vides an overview of major open-source foundation models based on their base architecture and probabilistic
output mechanism.
Sequence models.These models formulate forecasting as an autoregressive sequence-generation problem,
learning the conditional distribution of future observations given historical context. Chronos (Ansari et al.,
2024), for example, represents time series as discrete token sequences and generates future trajectories
through autoregressive decoding. Prediction intervals and arbitrary quantiles are obtained by repeatedly
sampling from the learned token distribution, whereas Chronos-2 (Ansari et al., 2025) extends this framework
with covariate support and improved calibration via a quantile head. The absence of explicit distributional
assumptions provides considerable flexibility, although repeated sampling increases inference cost.
Mixture-distribution models.These approaches represent predictive uncertainty as a weighted mixture
of probability distributions. Masked encoder-based universal time series forecasting Transformer (Moirai)
(Wooetal.,2024)flattensmultivariatetimeseriesintoasinglesequenceandprojectsnon-overlappingpatches
into vector representations via a multi-patch-size masked encoder. Patches within the forecast horizon are
replacedbylearnablemaskembeddings, whicharesubsequentlydecodedtoparameterizeapredictivemixture
distribution. Moirai learns mixtures of low-variance Gaussian, Student-t, log-normal, and negative binomial
components, allowing the predictive distribution to adapt to heterogeneous noise characteristics. Its any-
variate attention mechanism supports variable-dimensional multivariate forecasting, while Moirai-MoE (Liu
et al., 2024) improves scalability through sparse mixture-of-experts routing.
Parametric probabilistic models.Parametric approaches estimate the parameters of a predefined pre-
dictive distribution (see Section 4.2 for details). A foundation model utilizing this technique is Lag-Llama
36

Preprint
Table 8: Comparative overview of major open-source foundation models for probabilistic forecasting. “Mul-
tivariate:✓” denotes native support or pre-training for multivariate time series reported in the original
work.
Model Architecture Probabilistic Output Zero-shot Multivariate Possible Spatiotemporal Potential
Chronos-2 T5 Quantiles✓ ✓Indirect
Moirai Transformer Mixture distributions✓ ✓Moderate
Lag-Llama Decoder LLM Student-t distribution✓ ✗Limited
TimesFM-2.5 Decoder Transformer Quantiles✓ ✓Moderate
TiRex xLSTM Quantiles✓ ✗Moderate
Sundial Transformer Generative sampling✓ ✗High future potential
(Rasul et al., 2023). The terminal layer of the Lag-Llama architecture employs a dedicated distribution
head, which maps the learned latent features onto the parameter space of a target probability distribu-
tion. The model’s robust representational capacity can be flexibly coupled with various distribution heads
to estimate the parameters of an alternative parametric family. In the original work, Lag-Llama predicts
the location, scale, and degrees of freedom of a Student-tdistribution at each forecasting horizon, enabling
efficient generation of prediction intervals and probabilistic forecasts. This formulation is computationally
efficient, although its performance depends on the suitability of the assumed distribution.
Quantilepredictionmodels.These models estimate conditionalquantileswithout specifying aparametric
likelihood (see Section 4.3.1). Representative examples include TimesFM (Das et al., 2024), TiRex (Auer
et al., 2026), and Chronos-2 (Ansari et al., 2025), which differ primarily in their backbone architectures but
share the same probabilistic formulation. TimesFM is based on a decoder-only Transformer architecture and
was originally introduced as a point forecaster. TimesFM-2.5 subsequently added an optional continuous
quantile head, enabling direct probabilistic forecasting. TiRex, based on xLSTM (Beck et al., 2024), predicts
nine equidistant quantile levels:Q set ={0.1,0.2,...,0.9}, and the model’s parameters are optimized by
minimizing the quantile loss. Chronos-2 (Ansari et al., 2025) further predicts a set of 21 quantiles, resulting
in a richer representation of the predictive distribution compared to the 9-quantile gridQset. Direct quantile
prediction is computationally efficient and straightforward to optimize, although coverage may deteriorate
under distribution shift. ThedartsPython library (Herzen et al., 2022) implements various foundation
models with a quantile regression likelihood, in order to turn them into probabilistic zero-shot forecasters.
Generative models.Generative modeling has become a focal point in the development of foundation
models, primarily due to its efficacy in estimating complex target distributions during pre-training (Zhao
et al., 2026). Sundial (Liu et al., 2025d) is a flow-matching-based generative time-series foundation model
that learns complex predictive distributions without prescribing a fixed parametric predictive family. Sundial
directly processes continuous-valued time series using the TimeFlow Loss, which trains the autoregressive
TransformertomapsimpleGaussiannoisetothetargetdatadistribution. Togenerateprobabilisticforecasts,
the model performs repeated sampling from independent Gaussian noises while efficiently reusing the shared
representation of the historical context.
5.2 From Temporal to Spatiotemporal Foundation Models
Most existing foundation models have been developed for temporal forecasting, where large-scale pretraining
has enabled strong zero-shot and few-shot performance across diverse datasets. These models (Ansari et al.,
2024; Das et al., 2024; Auer et al., 2026) demonstrate that pretrained temporal representations can generalize
effectively across forecasting horizons, domains, and sampling frequencies with little or no task-specific train-
ing. Recent work has extended these capabilities beyond univariate forecasting toward multivariate settings,
where models must capture temporal dynamics together with cross-variable dependencies and exogenous
information. Moirai (Woo et al., 2024) addresses this challenge through any-variate attention, allowing
a variable number of input channels, whereas Chronos-2 (Ansari et al., 2025) and TimesFM (Das et al.,
2024) incorporate contextual covariates to improve forecasting performance. These developments broaden
37

Preprint
the applicability of foundation models but remain focused on collections of temporal sequences rather than
explicitly modeling spatial structure.
Probabilistic spatiotemporal foundation models that transfer across spatial structures and application do-
mains have yet to emerge. Existing deep spatiotemporal forecasting methods continue to rely primarily on
application-specific GNNs (Yu et al., 2018; Panja et al., 2026a; Pathak & Chakraborty, 2026), Transformers
(Wang et al., 2024), diffusion models (Wen et al., 2023; Chen et al., 2024), and physics-informed architec-
tures trained for individual tasks. Although such recent advances in multivariate representation learning,
long-context modeling, and probabilistic generation provide important building blocks, extending foundation
models to full spatiotemporal forecasting introduces additional challenges. These include scalable pretraining
overheterogeneousspatialgraphs, evolvingdependencystructures, irregularspatialobservations, uncertainty
propagation across networks, and the integration of physical constraints. Concurrently, graph foundation
models (GFMs) have emerged, designed to learn generalizable, transferable structural representations across
diverse and heterogeneous graph topologies (Liu et al., 2025a; Wang et al., 2025a). One possible direction is
to combine GFMs, which encode spatial structure, with time-series foundation models that learn temporal
dynamics. Such architectures must also model space-time interactions explicitly rather than treating spatial
and temporal dependence as separable. For probabilistic forecasting, they must represent joint uncertainty
across locations and forecast horizons while maintaining spatial coherence and calibration.
6 Evaluation and Model Selection
This section provides a practical guide to the aspects of evaluating probabilistic forecasting methods. Sec-
tion 6.1 covers data resources, benchmarks, and open-source implementations available. Section 6.2 presents
probabilistic metrics to measure forecast accuracy, while Section 6.3 discusses statistical significance tests to
evaluate model comparisons. Finally, Section 6.4 offers practical guidance on method selection.
6.1 Data Resources and Software Tools
Theempiricalevaluationofprobabilisticforecastingmethodsrequiresaccesstodiversedatasets, standardized
benchmarks for fair comparison, and open-source implementations for reproducibility. This section provides
the key resources available to researchers and practitioners across temporal and spatiotemporal settings. We
first describe widely used datasets and evaluation benchmarks (Section 6.1.1), followed by a summary of
open-source libraries and model implementations (Section 6.1.2).
6.1.1 Datasets and Evaluation Benchmarks
The rich literature in the domain of (probabilistic) forecasting has led to the development and availability
of high quality datasets and benchmarks, both for temporal and spatiotemporal settings. Table 9 presents
a non-exhaustive list of publicly available datasets for temporal and spatiotemporal forecasting, along with
their sources and works utilizing them. These datasets span a wide range of domains including transportation
(traffic forecasting), healthcare (epidemic forecasting), energy, computer vision (human pose forecasting),
and finance. Table 10 lists a set of resources including data repositories, benchmarks, and model evaluation
papers for univariate, multivariate, and spatiotemporal forecasting tasks along with links to the respective
public repositories.
6.1.2 Open-Source Libraries and Repositories
Table 11 summarizes publicly available implementations of representative probabilistic forecasting methods
discussed throughout this survey. The implementations are organized according to the forecasting setting,
including univariate, multivariate, and spatiotemporal models. For each method, we report the program-
ming environment, official repository when available, and the corresponding reference to support reproducing
published results and comparing state-of-the-art approaches. In addition to model-specific implementations,
several open-source libraries provide general frameworks for developing and evaluating probabilistic fore-
casting models. For Bayesian inference, libraries such asPyMC(Abril-Pla et al., 2023),Pyro(Bingham
38

Preprint
Table 9: Publicly available datasets widely used for benchmarking in the forecasting literature. “#Se-
ries/Nodes” indicates the number of time series excluding external covariates. “Analysis & Benchmarks”
consists of works that have analyzed and/or compared model performances on the respective datasets.
Dataset Type Domain #Series/Nodes Frequency Description Source Analysis & Benchmarks
Air Passengers Univariate Transportation 1 Monthly Monthly air passengers dataset,
from 1949 to 1960.
a -
Australian Beer Univariate Production 1 Quarterly Total quarterly beer production in
Australia from 1956 to 2008.
a -
Monthly Milk Univariate Production 1 Monthly Milk production (in pounds per
cow) between Jan 1962 and Dec
1975.
a -
Heart Rate Univariate Health 1 0.5-second 1800 evenly-spacedmeasurements of
heart rate from a single subject.
b Glass et al. (2012)
Hospital Multivariate Health 767 Monthly Monthly time series showing patient
counts related to medical products.
Hyndman (2015) Montero-Manso & Hyndman (2021)
Solar Multivariate Energy 137 Hourly Photovoltaic production of 137 sta-
tions in Alabama State.
c Salinas et al. (2019); Fan et al. (2024);
Pathak et al. (2026a)
Electricity Multivariate Energy 370 15-min Time series of the electricity con-
sumption of 370 customers.
d Salinas et al. (2019); Fan et al. (2024);
Pathak et al. (2026a)
London Smart
Meters Multivariate Energy 5560 30-min Energy consumption readings of London households in kWh. e Nugaliyadde et al. (2019); Kaur et al. (2019)
PEMS-SF Multivariate Transportation 963 Hourly Occupancy rate between 0 and 1, of
963 San Francisco car lanes.
f Salinas et al. (2019); Fan et al. (2024);
Pathak et al. (2026a)
Taxi Multivariate Transportation 1214 30-min Traffic time series of New York taxi
rides taken at 1214 locations.
g Salinas et al. (2019); Fan et al. (2024);
Pathak et al. (2026a)
KDD-cup Multivariate Environmental 270 Hourly Air-quality observations from mon-
itoring stations in Beijing and Lon-
don.
h Fan et al. (2024); Pathak et al. (2026a)
Wikipedia Multivariate Behavioral 2000 Daily Daily page view counts for a set of
Wikipedia articles.
i Salinas et al. (2019); Fan et al. (2024);
Pathak et al. (2026a)
Exchange rate Multivariate Finance 8 Daily Daily exchange rate between 8 cur-
rencies.
j Salinas et al. (2019)
Human3.6M Spatiotemporal Computer Vision - 50 Hz Large-scale motion capture dataset
with 3.6 million video frames.
Ionescu et al. (2013) Tang & Matteson (2021)
HumanEva-I Spatiotemporal Computer Vision 3 60 Hz Human motion dataset comprising 3
subjects recorded at 60 Hz.
Sigal et al. (2010) Tang & Matteson (2021)
METR-LA Spatiotemporal Transportation 207 5-min Traffic readings from 207 loop de-
tectors on highways in Los Angeles
County.
Jagadish et al. (2014) Li et al. (2018); Jiang et al. (2023)
PEMS-BAY Spatiotemporal Transportation 325 5-min Traffic readings from 325 traffic sen-
sors in San Francisco Bay Area.
k Li et al. (2018); Jiang et al. (2023)
PEMS 03, 04,
07, 08 Spatiotemporal Transportation 358, 307, 883, 170 5-min Traffic readings from sensors pro- vided by CalTrans PeMS. k Song et al. (2020); Guo et al. (2021)
LargeST Spatiotemporal Transportation 8600 5-min Large-scale traffic forecasting data
from 8600 traffic sensors in Califor-
nia.
Liu et al. (2023) Liu et al. (2023)
Japan TB Spatiotemporal Epidemiology 47 Monthly Monthly tuberculosis cases from 47
prefectures in Japan.
Sumi & Kobayashi (2019) Barman et al. (2025); Pathak & Chakraborty (2026)
China TB Spatiotemporal Epidemiology 31 Monthly Monthly tuberculosis cases from 31
provinces in China.
Ma & Fan (2023) Barman et al. (2025); Pathak & Chakraborty (2026)
USA ILI Spatiotemporal Epidemiology 50 Weekly Weekly influenza-like illnesses (ILI)
cases from 50 states in the US.
l Pathak & Chakraborty (2026);
Panja et al. (2026b)
Belgium COVID-19 Spatiotemporal Epidemiology 11 Daily Daily COVID-19 cases from 11
provinces in Belgium.
m Pathak & Chakraborty (2026);
Panja et al. (2026b)
Colombia Dengue Spatiotemporal Epidemiology 33 Weekly Weekly dengue cases from 33
provinces in Colombia.
Clarke et al. (2024) Pathak & Chakraborty (2026); Panja et al. (2026b)
Hungary Chickenpox Spatiotemporal Epidemiology 20 Weekly Weekly chickenpox cases from 20
provinces in Hungary.
Rozemberczki et al. (2021b) Pathak & Chakraborty (2026); Panja et al. (2026b)
Shanghai Precipitation Spatiotemporal Environmental 10 Daily Daily precipitation (1965-2015) at
0.1 mm resolution for 10 Shanghai
stations.
n Qin et al. (2025)
Delhi AQI Spatiotemporal Environmental 37 Daily Air pollution data of 37 stations
across Delhi, India.
Panja et al. (2026a) Panja et al. (2026a)
a https://unit8co.github.io/darts/generated_api/darts.datasets.html; b http://ecg.mit.edu/time-series/; c https://www.nrel.gov/grid/solar-power-data.html;
d https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014; e https://www.kaggle.com/jeanmidev/smart-meters-in-london f https://archive.ics.uci.edu/dataset/204/pems+sf;
g https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page; h https://www.kdd.org/kdd2018/kdd-cup; i https://github.com/mbohlkeschneider/gluon-ts/tree/mv_release/datasets;
j https://github.com/mbohlkeschneider/gluon-ts/blob/mv_release/datasets/exchange_rate_nips.tar.gz; k https://dot.ca.gov/programs/traffic-operations/mpr/pems-source;
l https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html; m https://epistat.sciensano.be/covid/; n https://www.resdc.cn/
et al., 2018),NumPyro(Phan et al., 2019), andTensorFlow Probability 1 in Python, alongsideStan,brms
(Bürkner, 2021), andnimble(de Valpine et al., 2017) in R, support MCMC, variational inference, and prob-
abilistic programming. For latent Gaussian and spatial models,R-INLA(Lindgren & Rue, 2015) andpyINLA
(Fattah et al., 2026) enable efficient approximate Bayesian inference using INLA (Section 4.1.4.4). Gaus-
sian process modeling is available through packages such asGPyTorch(Gardner et al., 2018) andGPflow
(Matthews et al., 2017) in Python andGPfit(MacDonald et al., 2015),DiceKriging(Roustant et al.,
2012),GpGp 2, andspBayes(Finley et al., 2007) in R. For general probabilistic forecasting frameworks, sev-
eral open-source libraries offer comprehensive implementations. In Python, libraries such asDarts(Herzen
1https://github.com/tensorflow/probability
2https://cran.r-project.org/package=GpGp
39

Preprint
Table 10: Overview of prominent time-series and spatiotemporal forecasting resources. Probabilistic evalu-
ation indicates whether the cited release explicitly evaluates predictive distributions. Dataset counts corre-
spond to the cited versions.
Resource Type Probabilistic Evaluation Data Type Domain #Datasets Repository Reference
Monash TSF Data Repo✗Uni-/Multivariate Multiple 20 MTSF Repository Godahewa et al. (2021)
LTSF Benchmark✗Uni-/Multivariate Multiple 9 LTSF Repository Zeng et al. (2023)
SynTSBench Benchmark✗Uni-/Multivariate Multiple - SynTSBench Tan et al. (2025)
EpiCastBench Benchmark✗Multivariate Epidemiology 40 EpiCastBench Panja et al. (2026b)
BasicTS Benchmark✗Multivariate Multiple 20 BasicTS Shao et al. (2024)
LargeST Benchmark✗Spatiotemporal Transportation 4 LargeST Liu et al. (2023)
ProbTS Benchmark✓Multivariate Multiple 18 ProbTS Zhang et al. (2024)
Chronos Model Eval.✓Univariate Multiple 42 Chronos-forecasting Ansari et al. (2024)
GIFT-Eval Benchmark✓Uni-/multivariate Multiple 23 GIFT-EVAL Aksu et al. (2024)
fev-bench Benchmark✓Uni-/multivariate Multiple 96 fev Shchur et al. (2025)
Sundial Model Eval.✓Multivariate Multiple 23 Sundial Liu et al. (2025d)
stengression Model Eval.✓Spatiotemporal Epidemiology 6 stengression Pathak & Chakraborty (2026)
AIATP Data Repo✓Spatiotemporal Trajectory Prediction 39 AIATP Li et al. (2020)
et al., 2022),NeuralForecast3,GluonTS(Alexandrov et al., 2020), andPyTorch Forecasting 4, alongside
R packages includingforecast(Hyndman & Khandakar, 2008) andfable(O’Hara-Wild et al., 2026),
support prediction intervals, likelihood estimation, and deep learning architectures. R packages such as
forecastandfablefocus on classic prediction intervals and distributional models. Python libraries in-
cludingDarts,NeuralForecast,GluonTS,PyTorch Forecasting,stengression(Pathak & Chakraborty,
2026), andGenformer(Pathak et al., 2026a) implement parametric likelihood models, deep regression-based
approaches, and deep generative architectures. Model-agnostic approaches are supported across both ecosys-
tems. In R, packages such asensembleBMA5 andconformalForecast 6 enable Bayesian model averaging and
conformal prediction, respectively. In Python, libraries includingMAPIE(Taquet et al., 2022) andTorchCP
(Huang et al., 2025) provide flexible distribution-free uncertainty quantification.
6.2 Probabilistic Evaluation Metrics
Probabilistic forecasts are evaluated differently from point forecasts because the objective is to assess an
entire predictive distribution, rather than a single prediction for each time step over the forecast horizon.
Evaluation therefore combines proper scoring rules for overall distributional quality with separate diagnostics
for calibration and sharpness (Gneiting & Raftery, 2007; Gneiting & Katzfuss, 2014). Calibration measures
the statistical consistency between forecasts and observations, whereas sharpness quantifies the concentration
of predictive distributions (Gneiting et al., 2007). The appropriate metric depends on the form of the
probabilistic forecast, including predictive distributions, quantiles, prediction intervals, or ensembles. For
univariate probabilistic forecasts, the continuous ranked probability score (CRPS) is one of the most widely
used proper scoring rules (Gneiting & Raftery, 2007). Given a predictive cumulative distribution function
Ft and observationyt, it is defined as:
CRPS(Ft,yt) = 1 H
T+H∑
t=T+1
∫ ∞
−∞
(
Ft(x)−I {x≥yt}
)2
dx.
CRPS generalizes the absolute error to probabilistic forecasts. For multivariate forecasts, the (negative)
energy score (ES) extends CRPS to vector-valued predictions:
ES(Ft,yt) =E∥Y t−yt∥β− 1 2 E∥Yt−Y ′ t∥β,
whereY t andY ′ t are independent samples from the predictive distribution andβ∈(0,2)is a hyperparam-
eter. However, the ES can be insensitive to dependence misspecification (Scheuerer & Hamill, 2015). The
3https://github.com/nixtla/neuralforecast
4https://github.com/sktime/pytorch-forecasting
5https://cran.r-project.org/package=ensembleBMA
6https://cran.r-project.org/package=conformalForecast
40

Preprint
Table 11: Summary of open-source implementations for probabilistic forecasting methods. A dash (-) indi-
cates methods without an explicit name in their original publication.
Method Name Data Type Environment Repository Reference
Model-Agnostic
CSP Univariate Python https://github.com/valeman/csp-forecaster Manokhin (2026)
FEWNet Univariate R https://github.com/ctanujit/FEWNet Sengupta et al. (2025)
EnbPI Univariate Python https://github.com/hamrel-cxu/EnbPI Xu & Xie (2021)
EnCQR Multivariate Python https://github.com/FilippoMB/Ensemble-Conformalized-Quantile-Regression Jensen et al. (2024)
STACI Spatiotemporal Python https://github.com/bf5124/STACI Feng et al. (2025)
S-ESN Spatiotemporal Python https://github.com/hhuang90/KSA-wind-forecast Huang et al. (2022)
D-EESN Spatiotemporal R https://github.com/PatrickMcDermottResearch/BD-EESN McDermott & Wikle (2019a)
QESN Spatiotemporal R Wiley Online Library McDermott & Wikle (2017)
Bayesian Modeling
BNN Univariate R https://github.com/nhauzenb/hhkm-joe-bnn Hauzenberger et al. (2025)
BARNN Univariate Python https://github.com/dario-coscia/barnn Coscia et al. (2025)
BSTS Univariate R https://github.com/cran/bsts Scott & Varian (2014)
BSTS Univariate Python https://github.com/Focus/bsts† Scott & Varian (2014)
Bayesian LSTM Multivariate Python https://github.com/patichandanareddy/bayesian-lstm† Hassan (2024)
MBSTS Multivariate R https://github.com/cran/mbsts Qiu et al. (2018)
LKGP Spatiotemporal Python https://github.com/jandylin/Latent-Kronecker-GPs Lin et al. (2025a)
BayesNF Spatiotemporal Python https://github.com/google/bayesnf Saad et al. (2024)
- Spatiotemporal R https://github.com/mindra-bit/HighResolutionForecasting Jaya & Folmer (2024)
Space-Time.DeepKriging Spatiotemporal R https://github.com/pratiknag/Space-Time.DeepKriging Nag et al. (2023)
VLR-STRF Spatiotemporal MATLAB https://github.com/pillowlab/VLR-STRF Duncker et al. (2023)
- Spatiotemporal R https://github.com/swchouchen/DengueCR_Bayesian_ST_Prediction Chen et al. (2023)
AGCGRU+flow Spatiotemporal Python https://github.com/networkslab/rnn_flow Pal et al. (2021)
ST-SVGP Spatiotemporal Python https://github.com/AaltoML/spatio-temporal-GPs Hamelijnck et al. (2021)
BSTIM Spatiotemporal Python https://github.com/ostojanovic/BSTIM Stojanović et al. (2019)
BD-EESN Spatiotemporal R https://github.com/PatrickMcDermottResearch/BD-EESN McDermott & Wikle (2019a)
- Spatiotemporal MATLAB Wiley Online Library Castruccio et al. (2018)
GpGp Spatiotemporal R https://github.com/cran/GpGp Guinness (2018)
Sticky-HDP-HMM Multivariate Python https://github.com/MoonBlvd/Sticky-HDP-HMM Fox et al. (2011)
Parametric Predictive Distributions
WA-IMDN Univariate Python https://github.com/IkeYang/WA-IMDN- Yang et al. (2022)
- Multivariate Python https://github.com/rottenivy/mv_pts_correlatederr Zheng & Sun (2024)
Distributional Regression
QRNN Univariate R https://github.com/cran/qrnn Graves (2011)
MQRNN Univariate Python https://github.com/ErezSC42/qr_forcaster Wen et al. (2017)
NMQN Univariate R https://github.com/Monster-Moon/l1pm Moon et al. (2021)
DQA Multivariate Python https://github.com/amazon-science/quantile-aggregation Fakoor et al. (2023)
LSTM-Engression Multivariate Python https://github.com/bask0/mach-flow-engression Kraft et al. (2026)
Enformer Multivariate Python https://github.com/yuvrajiro/Genformer Pathak et al. (2026a)
Tube Loss Multivariate Python https://github.com/ltpritamanand/Tube_loss Anand et al. (2026)
DESQRUQ Spatiotemporal Python https://github.com/tanwimallick/DESQRUQ Mallick et al. (2024)
EQRN Spatiotemporal R https://github.com/cran/EQRN Pasche & Engelke (2024)
GCEN/STEN Spatiotemporal Python https://github.com/PyCoder913/stengression Pathak & Chakraborty (2026)
Generative Models
InfHMM Univariate R https://github.com/frimane/InfHMM-Infinit-Hidden-Markov-Model Âzeddine Frimane et al. (2022)
C2FAR Univariate Python https://github.com/huaweicloud/c2far_forecasting Bergsma et al. (2022)
PPM Multivariate Python https://github.com/ljl8336/PPM Li et al. (2026a)
TimePrism Multivariate Python https://github.com/Fifthky/TimePrism Dai et al. (2026)
DGFC Multivariate R https://github.com/johnczito/DynamicCopula Zito & Kowal (2025)
HDT Multivariate Python https://github.com/autonomousvision/hdt Shibo et al. (2025)
K2VAE Multivariate Python https://github.com/decisionintelligence/K2VAE Wu et al. (2025)
- Multivariate Python https://github.com/lambertdem/geometricExtremesNF De Monte et al. (2025)
ProFITi Multivariate Python https://github.com/yalavarthivk/ProFITi Yalavarthi et al. (2025)
NsDiff Multivariate Python https://github.com/wwy155/NsDiff Ye et al. (2025)
TimeMCL Multivariate Python https://github.com/Victorletzelter/timeMCL Cortes et al. (2025)
TACTiS-2 Multivariate Python https://github.com/ServiceNow/TACTiS Ashok et al. (2024)
CopulaCPTS Multivariate Python https://github.com/Rose-STL-Lab/CopulaCPTS Sun & Yu (2024)
E-ProTran Multivariate Python https://github.com/bkoyuncu/eprotan Koyuncu et al. (2024)
TMDM Multivariate Python https://github.com/LiYuxin321/TMDM Li et al. (2024)
MG-TSD Multivariate Python https://github.com/Hundredl/MG-TSD Fan et al. (2024)
D3VAE Multivariate Python https://github.com/PaddlePaddle/PaddleSpatial/tree/main/research/D3VAE Li et al. (2022)
Transformer-MAF Multivariate Python https://github.com/zalandoresearch/pytorch-ts Rasul et al. (2021b)
TimeGrad Multivariate Python https://github.com/zalandoresearch/pytorch-ts Rasul et al. (2021a)
ScoreGrad Multivariate Python https://github.com/yantijin/ScoreGradPred Song et al. (2021)
GP-Copula Multivariate Python https://github.com/mbohlkeschneider/gluon-ts/tree/mv_release Salinas et al. (2019)
SpecSTG Spatiotemporal Python https://github.com/lequanlin/SpecSTG Lin et al. (2025b)
GenCast Spatiotemporal Python https://github.com/google-deepmind/weathernext Price et al. (2025)
SHADECast Spatiotemporal Python https://github.com/EnergyWeatherAI/GenerativeNowcasting Carpentieri et al. (2025)
- Spatiotemporal Python https://github.com/LoryPack/GenerativeNetworksScoringRulesProbabilisticForecasting Pacchiardi et al. (2024)
STMPNet Spatiotemporal Python https://github.com/yang-1201/STMPNet An et al. (2025)
Graph-EFM Spatiotemporal Python https://github.com/mllam/neural-lam/tree/prob_model_global Oskarsson et al. (2024)
MotionFlow Spatiotemporal Python https://github.com/MohsenZand/MotionFlow Zand et al. (2023)
DiffSTG Spatiotemporal Python https://github.com/wenhaomin/DiffSTG Wen et al. (2023)
DYffusion Spatiotemporal Python https://github.com/Rose-STL-Lab/dyffusion Cachay et al. (2023)
Social GAN Spatiotemporal Python https://github.com/agrimgupta92/sgan Gupta et al. (2018)
F oundation Models
Lag-Llama Univariate Python https://github.com/time-series-foundation-models/lag-llama Rasul et al. (2023)
TiRex Univariate Python https://github.com/NX-AI/tirex Auer et al. (2026)
Moirai Multivariate Python https://github.com/redoules/moirai Liu et al. (2024)
TimesFM Multivariate Python https://github.com/google-research/timesfm Das et al. (2024)
Chronos-2 Multivariate Python https://github.com/amazon-science/chronos-forecasting Ansari et al. (2024)
†Third-party implementation; not created by the paper’s authors.
variogram score (VS) addresses this limitation by evaluating pairwise dependence structures:
VSp(F,y) =
N∑
s1=1
T∑
t1=1
N∑
s2=1
T∑
t2=1
ws1,t1,s2,t2 (|ys1,t1−ys2,t2|p−EF|Ys1,t1−Ys2,t2|p)2,
whereydenotes the full set of spatiotemporal observations over the entire domain and time horizon,Fis the
joint predictive distribution of the spatiotemporal forecast,ys1,t1,ys2,t2 are the realized observations at two
spatiotemporal points(s 1,t 1)and(s 2,t 2), respectively,Ys1,t1,Ys2,t2 are the corresponding forecast random
variables drawn fromF,pis the order of the VS, andw s1,t1,s2,t2 are non-negative weights assigned to the
41

Preprint
pair of spatiotemporal points (Scheuerer & Hamill, 2015). The weights can be tuned to emphasize specific
distance scales or downweight distant pairs to reduce sampling error (Scheuerer & Hamill, 2015; Jung &
Leutbecher, 2008). For forecasts represented as quantiles or prediction intervals, performance is commonly
evaluated using the pinball loss:
Lτ(qt,τ,yt) =
(
τ−I {yt<qt,τ}
)
(yt−qt,τ),
whereq t,τ is theτ-quantile forecast at timet(Gneiting et al., 2023). To evaluate overall distributional
coverage, theρ-risk metric normalizes the pinball loss and aggregates it across a range of quantile levelsτ:
ρ-risk= 2∑T+H t=T+1 max [τ(yt−ˆyt),(1−τ)(ˆyt−yt)] ∑T+H
t=T+1|yt|
,
where lowerρ-risk values indicate more accurate quantile forecasts across the predictive distribution (Seeger
et al., 2016; Salinas et al., 2020). For prediction intervals, the Winkler score provides a proper scoring rule
that jointly evaluates interval sharpness and coverage (Winkler et al., 1996). Given a prediction interval[
ˆfL t ,ˆfU t
]
with a coverage level1−αand an observationy t, it is defined as:
Wα,t =



(
ˆfU t − ˆfL t
)
+ 2 α
(
ˆfL t −yt
)
, y t < ˆfL t ,
ˆfU t − ˆfL t , ˆfL t ≤y t≤ ˆfU t ,
(
ˆfU t − ˆfL t
)
+ 2 α
(
yt− ˆfU t
)
, y t > ˆfU t .
The score reduces to the interval width when the observation lies within the interval and adds penalties
proportional to the distance outside the bounds; otherwise, penalizing under-dispersion so that lower scores
reflect sharper, better-calibrated intervals (Winkler et al., 1996; Pathak & Chakraborty, 2026). In addition
to the Winkler score, the prediction interval coverage probability (PICP) and mean prediction interval width
(MPIW) are commonly reported (Anand et al., 2026):
PICP = 1 H
T+H∑
t=T+1
I{ˆfL t≤yt≤ˆfU t } andMPIW = 1 H
T+H∑
t=T+1
(
ˆfU t − ˆfL t
)
.
PICP quantifies the proportion of observations falling within the predicted intervals, whereas MPIW assesses
forecast sharpness. Reliable interval forecasts achieve nominal coverage while minimizing interval width
(Gneiting et al., 2007). For ensemble forecasts, the probability integral transform (PIT) assesses calibration
by computing the normalized rank of the true observationyt within an ensemble{ˆy(m) t }M m=1:
PIT = 1 M+ 1
M∑
m=1
I
(
ˆy(m) t <y t
)
.
For well-calibrated forecasts, PIT values follow a uniform distribution, whereas deviations signal bias or
miscalibrated uncertainty dispersion (Gneiting & Raftery, 2007). In practice, evaluation pairs proper scoring
rules for overall predictive quality with PIT, coverage, or interval-width metrics to assess calibration.
6.3 Robustness and Statistical Significance Tests
The metrics presented in Section 6.2 quantify predictive performance but do not determine whether observed
differences between forecasting methods are statistically significant. Statistical significance tests distinguish
meaningful performance improvements from random sampling variation. For probabilistic forecasts, conven-
tional hypothesis tests apply by evaluating differences in proper scoring rules, such as CRPS, rather than
traditional point-forecast errors. The Diebold-Mariano (DM) test (Diebold & Mariano, 1995) remains the
standard approach for pairwise comparison of forecasting methods. For two competing forecasters,Fand
42

Preprint
G, evaluated acrossJcases, letd t =S(F t,yt)−S(G t,yt)denote the score differential. Under the null
hypothesis of equal predictive performance (E[dt] = 0), the test statistic:
TJ =
√
J
¯dJ
ˆσJ
is asymptotically standard Gaussian, where ¯dJ andˆσ2 J are the sample mean and variance estimators of
di, respectively. The Giacomini-White (GW) test (Giacomini & White, 2006) extends the DM framework
to evaluate conditional predictive ability by testing whether loss differences depend on time-tinformation
ht. The test statistic follows an asymptotic chi-square distribution withdim(ht)degrees of freedom and
reduces to the standard DM test whenht = 1. The GW framework supports rolling and recursive re-
estimation, making it ideal for testing adaptive forecasting systems; though it remains limited to pairwise
comparisons. Comparing larger collections of forecasting methods requires procedures that control multiple
comparisons. Mariano & Preve (2012) generalized the DM framework to jointly test the equal predictive
ability of several forecasting models using a Wald-type statistic, avoiding repeated pairwise testing. The
model confidence set (MCS) procedure (Hansen et al., 2011) sequentially eliminates inferior models until a
superior set of statistically indistinguishable forecasting methods remains. A complementary alternative is
the multiple comparisons with the best (MCB) test (Nemenyi, 1963; Koning et al., 2005), which ranks com-
peting methods relative to the best-performing model and constructs confidence intervals for rank differences.
Extending significance testing to spatiotemporal forecasting presents additional challenges because forecast
errors exhibit both temporal and spatial dependence. For panel data, Akgun et al. (2024) proposed two
equal predictive ability tests, namelyS-statistics andC-statistics. The former tests whether two forecasters
perform equally well on average across all panel units and time periods, while the latter evaluates whether
equal predictive performance holds jointly across predefined clusters of units. The AZ-whiteness test (Zam-
bon & Alippi, 2022) offers a complementary diagnostic for graph-structured spatiotemporal data. It uses
sign-based statistics across adjacent time steps and connected nodes to evaluate whether model residuals
retain exploitable spatial or temporal dependencies.
6.4 Method Guidance
Selecting an appropriate probabilistic forecasting method requires navigating several competing consider-
ations, including data availability, distributional characteristics, uncertainty requirements, computational
constraints, and interpretability. No single approach is optimal across all settings. Methods with strong
theoretical guarantees, such as conformal prediction (Section 3.3.1), provide finite-sample marginal coverage
under exchangeability but may require additional calibration strategies to adapt to nonstationary uncer-
tainty (Section 3.3.2). Approaches with explicit probabilistic structure, such as Bayesian hierarchical models
and Gaussian processes (Section 4.1.1), offer interpretability and principled uncertainty decomposition but
face scalability challenges in large spatiotemporal systems compared with deep generative approaches (Sec-
tion 4.4). Conversely, highly expressive generative models, such as diffusion models (Section 4.4.7), can
represent complex predictive distributions but often introduce substantial computational costs during in-
ference. To summarize these trade-offs, Section 6.4.1 presents a decision flowchart that maps forecasting
requirements onto a specific recommended methodology, while Section 6.4.2 examines how these considera-
tions translate into practice across different application domains.
6.4.1 Data-Driven Selection
Fig. 9 summarizes the practical considerations discussed throughout this survey into a decision flowchart
for selecting an appropriate probabilistic forecasting method. The first distinction is whether uncertainty
should be estimated for an existing forecasting model without retraining (model-agnostic methods, Sec-
tion 3) or learned jointly with the forecasting model itself (model-intrinsic methods, Section 4). Within the
model-agnostic branch, the primary considerations are the need for finite-sample coverage guarantees and the
statistical properties of the forecast residuals, guiding the selection between conformal prediction, conformal-
ized quantile regression, ensemble-based methods, and pre-control limits. For model-intrinsic approaches,
the flowchart first distinguishes between interpretable Bayesian models and data-driven deep learning meth-
ods. Bayesian models are selected according to the underlying probabilistic structure, including latent state
43

Preprint
Start:Do you want to quantify uncertainty for an existing model without modifying its architecture?
Is a coverage guarantee required?
Are residuals
heteroskedastic?
Conformalized
Quantile Regression
Conformal
Prediction
Are residuals
stationary?
Pre-Control
Limits⋆
Ensemble-Based
Methods
Do you need an interpretable structure?
Do you want to
interpret how time
series components
evolve over time?
Are you placing a prior over an infinite-dimensional space?
Are you learning functions instead of weights?
What does your prior
place probability over?
Dirichlet Process Bayesian Additive Regression Trees
Gaussian Processes
Is the sample size small or modest?
Bayesian Hierarchical
Models
Bayesian Neural
Networks
Bayesian State
Space Models
Is a generative model required?
Do you need to model the
dependence between series?
Do you have limited data or
require an interpretable model?
Do you need fast sample generation and stable training?
Normalizing Flows What is your available computational budget?
What is your main optimization objective?
Variational Autoencoders Generative Adversarial Networks
Diffusion Models
Hidden Markov Models
Copula-Based
Models
Is a fixed distributional
family required?
Is the distribution
assumed to be unimodal?
Single Parametric
Distributions
Mixture Density
Networks
Do you prefer a lightweight,
minimal-tuning architecture?
Engression Do you need to optimize the coverage-width trade-off?
Loss-Driven Interval Estimation Quantile Regression
Yes
Yes
Yes No
No
Yes No
No
Yes
No
Yes
No
Distributions Ensemble of Weak Learners
Yes
No
Yes No
Yes
No
Yes
No
No
Yes No
Standard
Stable Training Sample Sharpness
Intensive
Yes
Yes
No
Yes
Yes No
No
Yes No
Yes No
Figure 9: Decision flowchart for identifying candidate probabilistic forecasting families based on model
access, coverage requirements, structural assumptions, and computational constraints. Recommendations
are indicative rather than exclusive.⋆Rarely recommended beyond simple, low-resource deployments (Sec-
tion 3.1).
44

Preprint
dynamics, functional priors, hierarchical dependence, and neural parameterizations. The remaining methods
are further divided into parametric, distributional regression, and generative approaches. The subsequent
decisions reflect the trade-offs discussed throughout this survey, including modeling assumptions, computa-
tional cost, optimization objectives, and application-specific requirements.
6.4.2 Domain-Specific Method Guidance
The previous section discussed method selection based on statistical characteristics and modeling require-
ments. In practice, probabilistic forecasting is also shaped by domain-specific considerations, including the
data-generating process, availability of prior knowledge, operational constraints, and regulatory require-
ments. These factors often determine whether forecasting systems prioritize calibrated prediction intervals,
full predictive distributions, interpretability, or computational efficiency. This section identifies recurring
methodological patterns across domains. Applications with limited observations, strong domain knowledge,
or a need for interpretability tend to favor Bayesian formulations, whereas high-dimensional spatiotemporal
systems increasingly rely on deep generative approaches to capture complex dependencies. Distribution-free
calibration provides a complementary strategy when reliable coverage guarantees are required independently
of the forecasting architecture. A breakdown of these domains and their corresponding methodological
frameworks is depicted in Fig. 10.
Domains such as epidemiology, ecology, and environmental science prioritize interpretability (Ferté et al.,
2026; Dietze, 2017; Krapu & Borsuk, 2019). In particular, epidemic and public health forecasting requires
balancing predictive performance with interpretability to support intervention strategies and policy decisions
(Ferté et al., 2026). Bayesian state-space and hierarchical formulations are, therefore, widely adopted to in-
corporate epidemiological knowledge through prior information (Karami et al., 2026b). Recent approaches
have further explored hybrid frameworks that integrate epidemiological principles into deep learning ar-
chitectures to enhance forecasting performance (Barman et al., 2025). These methods can be combined
with conformal prediction to construct calibrated prediction intervals with finite-sample coverage guaran-
tees. Similar considerations arise in ecological forecasting, where sparse observations and imperfect sampling
processes motivate Bayesian models that separate latent ecological dynamics from observation uncertainty
(Clark, 2005; Dietze, 2017). Their ability to update predictions as new observations become available also
aligns with iterative ecological forecasting practices (Dietze et al., 2018). Environmental and hydrological
forecasting extend these challenges to physical systems, where interpretability and uncertainty quantification
are essential for supporting risk-sensitive decisions such as air quality and flood management (Krapu & Bor-
suk, 2019; Papacharalampous & Tyralis, 2022). Thus, Bayesian approaches are commonly employed for their
principled uncertainty propagation and incorporation of domain knowledge (Krapu & Borsuk, 2019; John-
son et al., 2023). Other approaches combine deep learning models with distribution-free calibration methods
(Panja et al., 2025; 2026a), while ensemble methods remain widely used in hydrology (De León Pérez et al.,
2025). Recent advances have further explored flexible generative approaches, such as normalizing flows, for
modeling complex predictive distributions in Earth system forecasting (Xu et al., 2024).
Forecasting domains dominated by large-scale spatiotemporal dynamics have increasingly adopted flexible
probabilistic models capable of representing high-dimensional dependencies. Meteorological forecasting,
for instance, relies on numerical weather prediction systems whose ensemble forecasts often suffer from
miscalibration (Gneiting et al., 2005). BMA and copula-based approaches have addressed this challenge
by calibrating ensemble outputs and modeling dependencies between variables (Gneiting & Katzfuss, 2014).
Recent work, however, has shifted toward deep generative models for probabilistic spatiotemporal forecasting
(Oskarsson et al., 2024; Price et al., 2025) due to their flexibility in capturing high-dimensional, nonlinear
dynamics. Similar challenges arise in transportation forecasting, where graph-structured dynamics and
multimodal traffic states motivate the use of parametric distributional models such as Gaussian mixtures
and MDNs (Zhi et al., 2019; Chen et al., 2023). Recent approaches have also explored loss-driven interval
estimation and diffusion models for calibrated intervals and realistic probabilistic trajectory generation,
respectively (Cheng et al., 2024). Gaussian processes remain useful for smaller-scale mobility problems
where uncertainty calibration outweighs scalability limitations (Steentoft et al., 2024).
High-stakes forecasting in economic, financial, and energy markets requires adapting probabilistic architec-
tures and calibration techniques to domain-specific constraints. Economic and macro-financial forecasting
45

Preprint
Domain Characteristics & Uncertainty Requirements
Epidemiology, Ecology, &
Environmental Forecasting
Meteorology, Climate, &
Transportation Forecasting
Economics, Finance, & Energy
Forecasting
Calibrated
uncertaintyLimited data Prior scientific knowledge
Domain Characteristics
Bayesian models
Mechanistic-deep hybrid
Ensemble forecasting
Common Approaches
(Mechanistic
model)
Multimodal
outcomes
High
dimensionality
Complex spatial
dependence
Domain Characteristics
Ensembles & Copulas
Parametric distributions & MDNs
Deep generative models
Common Approaches
Operational
reliability
Structural
change Volatility & tail risk
Domain Characteristics
Quantile & distributional regression
Bayesian neural networks
Generative models
Common Approaches
...
Diffusion
 Normalizing Flows
Figure 10: Overview of probabilistic forecasting applications across diverse domains alongside their primary
methodological approaches. The associations are illustrative rather than exclusive.
are characterized by limited historical observations, structural breaks, nonlinear dynamics, and a strong
emphasis on tail risk (Elliott et al., 2013). Consequently, distributional methods such as quantile regres-
sion have gained widespread adoption (Adrian et al., 2019; Chavleishvili & Manganelli, 2024). BNNs offer
an alternative approach when uncertainty from model parameters and observations must be represented
jointly (Blasco et al., 2024), while conformal prediction provides a model-agnostic calibration framework for
complex forecasting architectures (Sengupta et al., 2025; Besher et al., 2026a). Energy forecasting shares
these requirements, as weather variability and temporal dynamics make probabilistic modeling essential for
managing financial risk. Distributional regression is frequently applied for load and price forecasting (Hirsch,
2025), while recent works have shifted towards generative approaches (Chen et al., 2025; Dudek et al., 2026).
7 Empirical Demonstration
This section provides an illustrative empirical comparison of representative probabilistic forecasting methods
using point and probabilistic evaluation measures. Sections 7.1 and 7.2 detail the experimental results for
the temporal and spatiotemporal settings, respectively, followed by a brief discussion on model performance
in Section 7.3. Model performance is evaluated across three standard public datasets, spanning distinct
domains: the Air Passengers dataset (Herzen et al., 2022) for univariate forecasting, the PEMS-SF traffic
dataset (Alexandrov et al., 2020) for multivariate analysis, and the Belgium COVID-19 dataset (Panja et al.,
2026b) for spatiotemporal modeling. Table 12 provides an overview mapping of the evaluated probabilistic
forecasting models to their respective classes. Notably, spatiotemporal frameworks such as GpGp and GCEN
46

Preprint
require locational coordinates and spatial adjacency matrices; consequently, they are excluded from the
temporal-only benchmarks due to the absence of spatial metadata. To ensure a standardized comparison, all
models employ the default hyperparameter configurations stipulated by their native libraries. For instance,
the LSTM (Hochreiter & Schmidhuber, 1997) architecture utilizes two layers with 64 hidden units, while
NHITS (Challu et al., 2023) adheres to the default specifications within thedartsframework. The BNN-
MCD model is implemented using an LSTM network with active Monte Carlo dropout during inference
(Hassan, 2024). The three foundation models, namely TimesFM-2.5 (Das et al., 2024), Chronos-2 (Ansari
et al., 2025), and PatchTSTFM7, utilize quantile regression to generate probabilistic forecasts. Training is
performed on a single NVIDIA T4 GPU with 16 GB RAM. We report the probabilistic metrics listed in
Section 6.2 to compare the representative models. Additionally, we compute three point metrics, namely the
Mean Absolute Error (MAE), Mean Absolute Scaled Error (MASE), and Root Mean Squared Scaled Error
(RMSSE) (Hyndman & Athanasopoulos, 2021) to assess the point forecast accuracy.
Table 12: Overview of the representative models used for empirical demonstration. ‘❍’ indicates ‘partial
support’ for a specific data type (e.g., LSTM lacks built-in spatiotemporal capabilities but can still process
these datasets by treating each node independently).
Model Class Univariate Multivariate Spatiotemporal Library
LSTM-PC Pre-control limit✓ ✓ ❍darts
LSTM-BE Bootstrap ensemble✓ ✓ ❍darts
NHITS-CP Conformal prediction✓ ✓ ❍darts
NHITS-CQR Conformalized quantile regression✓ ✓ ❍darts
BNN-MCD Bayesian Monte Carlo dropout✓ ✓ ❍torch
GpGp Gaussian process✗ ✗ ✓gpgp(R)
DeepAR Single parametric distribution✓ ✓ ❍darts
DeepNPTS Nonparametric distribution✓ ✓ ❍neuralforecast
LSTM-QR Quantile regression✓ ✓ ❍darts
MVEN Engression✓ ✓ ❍stengression
GCEN Engression✗ ✗ ✓stengression
K2VAE VAE✓ ✓ ❍K2VAE †
Transformer-MAF Normalizing flows✗ ✓ ❍pytorch-ts
TimeGrad Diffusion✗ ✓ ❍pytorch-ts
TimesFM-2.5 Foundation (quantile regression)✓ ✓ ❍darts
Chronos-2 Foundation (quantile regression)✓ ✓ ❍darts
PatchTSTFM Foundation (quantile regression)✓ ✓ ❍darts
†https://github.com/decisionintelligence/K2VAE
7.1 Temporal Forecasting
In the univariate setting, we evaluate the compatible models outlined in Table 12 on the monthly Air Passen-
gers dataset (Herzen et al., 2022). All task-specific models are trained for 150 epochs using a standardized
context window of 24 months to forecast a 12-month horizon; the results across evaluation metrics are
detailed in Table 13. The evaluatedpytorch-ts8 implementations of Transformer-MAF (and TimeGrad)
were omitted from the univariate experiment because they require a multivariate target representation. For
Transformer-MAF, this limitation arises inherently from the MAF framework, which necessitates a minimum
of two dimensions to construct its internal conditioning masks.
To evaluate probabilistic forecasting methods on multivariate temporal data, we use the PEMS-SF traffic
dataset (Alexandrov et al., 2020), which contains road occupancy rates for 4001 time points from 963 highway
sensors in the San Francisco Bay Area. All compatible task-specific models are trained for 30 epochs under
default hyperparameter configurations, with a 24-hour context window and forecasting horizon. Due to the
dataset’s high dimensionality, conformal prediction-based approaches, namely NHITS-CP and NHITS-CQR,
are excluded because of memory constraints that result in out-of-memory failures during training. The
resulting performance comparison is reported in Table 14.
7https://huggingface.co/ibm-research/patchtst-fm-r1
8https://github.com/zalandoresearch/pytorch-ts
47

Preprint
Table13: ModelevaluationresultsontheunivariateAirPassengersdataset. Thebestresultsarehighlighted.
Metric LSTM-PC LSTM-BE NHITS-CP NHITS-CQR BNN-MCD DeepAR DeepNPTS LSTM MVEN K2VAE TimesFM-2.5 Chronos-2 PatchTSTFM
MAE 37.9239 37.9239 25.060117.007665.9036 53.7476 21.7857 72.1518 39.9051 18.0065 24.1588 32.9886 54.9515
MASE 1.5747 1.5747 1.04050.70622.7364 2.2317 0.9046 2.9958 1.6569 0.7477 1.0031 1.3697 2.2817
RMSSE 1.3269 1.3269 0.94520.61762.753 2.2981 1.0258 3.1015 1.4258 0.7813 0.905 1.2195 2.2387
PICP 0.3333 0.58331.0000 1.00000.3333 0.8333 0.9167 0.8333 0.58331.00000.91671.0000 1.0000
CRPS 28.1875 22.8708 17.701413.808156.4015 39.6796 16.104 56.4844 31.8976 46.2200 15.5024 28.8727 42.8019
Winkler Score 337.4479 253.2515109.7248129.7828 1553.8936 358.7782 130.0086 629.789 510.5805 825.7117 126.1043 416.836 419.3702
Pinball-80 17.3010 12.9625 7.01095.368538.8983 20.0455 11.1319 28.7110 19.3661 30.5515 5.4353 7.0093 15.9202
Training time (sec.) 10.6481 8.7225 8.9764 7.28720.77726.2260 22.3078 5.5053 3.0041 12.9991 7.4556 4.2031 7.9223
Inference time (sec.) 0.0807 0.0735 2.7265 1.7332 0.0462 0.1354 0.0404 0.1477 0.04630.01152.7472 2.2098 3.7060
Table 14: Model evaluation results on the multivariate PEMS-SF traffic dataset. Thebestresults are
highlighted.
Metric LSTM-PC LSTM-BE BNN-MCD DeepAR DeepNPTS LSTM-QR MVEN Transformer-MAF TimeGrad K2VAE TimesFM-2.5 Chronos-2 PatchTSTFM
MAE0.0103 0.01030.0107 0.0209 0.0220 0.01080.01030.0308 0.0119 0.0250 0.0134 0.0196 0.0269
MASE 0.8765 0.8765 0.9057 1.7673 1.8622 0.91540.87402.6096 1.0068 2.1182 1.1339 1.6634 2.2799
RMSSE 0.9731 0.9731 0.9675 1.4404 1.4668 1.01940.95082.6623 1.0296 1.5296 1.1360 1.4350 1.6535
PICP 0.9567 0.9547 0.9114 0.9746 0.8596 0.928 0.9482 0.8000 0.9460 0.8889 0.92320.99410.9813
CRPS 0.0099 0.0088 0.0085 0.0157 0.01630.00770.0082 0.0250 0.0090 0.0411 0.0098 0.0109 0.0181
Winkler Score 0.1580 0.1549 0.1534 0.1961 0.18160.09670.1306 0.3465 0.1169 0.6587 0.1316 0.2316 0.2429
Pinball-80 0.0061 0.0051 0.0051 0.0090 0.0090 0.00480.00470.0137 0.0053 0.0264 0.0063 0.0078 0.0113
Training time (sec.) 88.9435 88.5309 16.2234 120.8953 22.4629 169.8363 1418.9248 390.5839 284.8944 94.2103 7.45824.79718.3082
Inference time (sec.) 0.1033 0.0839 0.0948 0.1962 1.3771 0.34170.051426.7843 16.2917 0.0631 186.4986 661.4305 715.2338
7.2 Spatiotemporal Forecasting
To evaluate model performance on spatiotemporal data, we analyze daily COVID-19 case counts across
11 Belgian provinces from September 2020 to October 2022. Following the methodology in Panja et al.
(2026a), the spatial adjacency matrix is constructed by applying a Gaussian kernel to the pairwise Haversine
distances between locations. For a standardized comparison, all models are configured with a 60-day context
window to forecast across a 30-day prediction horizon. Quantitative evaluation metrics are summarized in
Table 15, while Fig. 11 visualizes the ground truth against the out-of-sample point forecasts (median) and
their corresponding95%prediction intervals.
Table 15: Model evaluation results on the spatiotemporal Belgium COVID-19 dataset. Thebestresults are
highlighted.
Metric LSTM-PC LSTM-BE NHITS-CP NHITS-CQR BNN-MCD GpGp DeepAR DeepNPTS LSTM-QR GCEN Transformer-MAF TimeGrad K2VAE TimesFM-2.5 Chronos-2 PatchTSTFM
MAE 97.0230 97.0230 66.3198 80.0808 152.8920 118.5176 65.0088 74.4091 115.629755.249766.6075 71.5354 98.1925 68.3451 61.3654 66.7250
MASE 0.4954 0.4954 0.3386 0.4089 0.7807 0.6051 0.3319 0.3799 0.59040.28210.3401 0.3653 0.5014 0.3490 0.3133 0.3407
RMSSE 0.2706 0.2706 0.1912 0.2367 0.4118 0.3403 0.2009 0.2245 0.31720.16730.2228 0.2029 0.3081 0.1981 0.1832 0.1979
PICP 0.9485 0.97581.00000.9909 0.27271.00000.8242 0.8121 0.9727 0.8606 0.6000 0.5636 0.9364 0.7394 0.98181.0000
CRPS 72.7486 67.2433 94.5716 64.6509 133.6601 499.1120 48.3278 54.4688 84.721442.213355.2931 54.6017 80.1510 50.3264 44.2722 51.3223
Winkler Score 676.6248 692.9498 2660.9012 1011.9732 3718.1841 7380.7593 489.1249 666.5125 665.1303 563.2885 1230.1843 762.1248 983.2138 612.5202446.9277593.5463
Pinball-80 40.7961 37.0838 59.9327 33.9626 44.6283 246.8415 28.6325 27.7178 49.004721.360639.6408 22.2583 40.9953 29.1404 23.7537 26.8285
Training time (sec.) 48.4836 49.3807 32.6485 16.8667 3.6760 90.9597 32.2584 6.3141 28.6281 81.0000 369.4191 232.8301 63.3808 2.06501.20002.2096
Inference time (sec.) 0.0881 0.087 23.1675 13.628 0.0714 11.9556 0.1235 0.048 0.1054 0.1912 0.5926 16.4660.01646.6694 11.9143 17.7775
7.3 Analysis of Results
This section evaluates the predictive performance of the assessed representative models across the three
diverse datasets. Following Section 6.3, to statistically compare model efficacy across these paradigms, we
perform the Multiple Comparisons with the Best (MCB) test (Koning et al., 2005) using the Continuous
Ranked Probability Score (CRPS), as illustrated in Fig. 12.
For the univariate Air Passengers dataset, conformal prediction integrated with NHITS demonstrates supe-
rior performance. Specifically, NHITS-CQR obtains the lowest MAE, MASE, RMSSE, CRPS, and pinball
loss. It also shares the best average rank with TimesFM-2.5 in the MCB test. Furthermore, conformal
prediction (NHITS-CP) yields the most robust predictive intervals for this univariate data, achieving the
best Winkler score alongside 100% empirical coverage (PICP). Following similar arguments as Pathak &
Chakraborty (2026), we note that PICP alone can be a misleading indicator of prediction interval quality.
Models can artificially achieve full coverage by generating excessively wide, uninformative intervals that
lack practical utility. Consequently, the Winkler score serves as a more reliable metric by jointly penal-
izing both undercoverage and excessive interval width. For instance, K2VAE on the Air Passengers data
and GpGp on the Belgium COVID-19 data both achieve full empirical coverage, yet they incur excessively
48

Preprint
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(A) LSTM (Pre-control)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(B) LSTM (Bootstrap Ensemble)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(C) NHITS (Conformal)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(D) NHITS (ConformalQR)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(E) GpGp (Bayesian)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(F) BNN (MC Dropout)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(G) DeepAR (Parametric)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(H) LSTM (Quantile Regression)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(I) GCEN (Engression)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(J) K2VAE (VAE)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(K) Transformer-MAF (Normalizing Flows)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(L) TimeGrad (Diffusion)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(M) DeepNPTS (Non-parametric)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(N) TimesFM-2.5 (Foundation, QR)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(O) Chronos-2 (Foundation, QR)
0 10 20 30 40
Time Steps
0
100
200
300
400
500
600
700
800Value
(P) PatchTSTFM (Foundation, QR)
History Ground Truth Prediction 95% Interval
Figure 11: Forecasts and prediction intervals from representative models obtained on COVID-19 cases in
Limburg, Belgium. The point predictions and prediction intervals are shown with a representative color in
the legend; actuals are color-coded following the taxonomy in Table 1.
high Winkler scores, rendering their intervals suboptimal for decision-making. Applying vanilla conformal
prediction to spatiotemporal data can yield similarly uninformative bounds. Ignoring inherent spatial and
temporal dependencies violates the fundamental assumption of exchangeability, thereby forcing the method
to bloat its uncertainty bounds to guarantee coverage. This phenomenon is evident in the Belgium COVID-
19 dataset (Fig. 13), where NHITS-CP achieves 100% PICP at the cost of an excessively high Winkler score.
Conversely, NHITS-CQR mitigates this issue, substantially reducing the Winkler score while maintaining a
highly competitive 99% coverage.
Recent generative methods leveraging normalizing flows (Transformer-MAF) and diffusion processes
(TimeGrad) lack native support for univariate data. Moreover, as detailed in Tables 14-15 and Fig. 14,
these models incur substantial computational overhead during both training and inference compared to their
competitors. In contrast, engression-based methods provide a highly efficient, lightweight alternative. Archi-
tectures such as MVEN and GCEN demonstrate competitive efficacy on the multivariate and spatiotemporal
datasets, respectively. On the Belgium COVID-19 dataset, although GCEN achieves the best average CRPS
across all spatial nodes, it secures only the second-best rank in the MCB test, trailing Chronos-2. Be-
cause arithmetic averages are highly susceptible to skewness from extreme outliers, a model might achieve
a superior overall mean score by significantly outperforming on a few anomalous nodes, even if rank-based
49

Preprint
(A) AirPassengers: CRPS
Mean Ranks of Models
NHITS−CQR − 3.75
TimesFM−2.5 − 3.75
DeepNPTS − 3.83
NHITS−CP − 4.42
LSTM−BE − 5.42
LSTM−PC − 7.42
Chronos−2 − 7.83
DeepAR − 8.17
MVEN − 8.42
BNN−MCD − 8.50
LSTM−QR − 9.58
PatchTSTFM − 9.92
K2VAE − 10.00
2 4 6 8 10 12
(B) PEMS−SF (Traffic): CRPS
Mean Ranks of Models
LSTM−QR − 3.06
MVEN − 4.04
BNN−MCD − 4.29
TimesFM−2.5 − 4.46
LSTM−BE − 4.85
TimeGrad − 4.91
Chronos−2 − 5.57
LSTM−PC − 6.57
DeepAR − 9.65
DeepNPTS − 9.75
PatchTSTFM − 10.29
Transformer−MAF − 11.74
K2VAE − 11.82
4 6 8 10 12
(C) Belgium: CRPS
Mean Ranks of Models
Chronos−2 − 2.45
GCEN − 2.64
DeepAR − 4.91
PatchTSTFM − 5.09
TimesFM−2.5 − 5.36
TimeGrad − 6.00
DeepNPTS − 6.27
Transformer−MAF − 7.45
LSTM−BE − 8.27
NHITS−CQR − 9.45
K2VAE − 10.18
LSTM−PC − 10.45
LSTM−QR − 13.09
NHITS−CP − 13.45
BNN−MCD − 14.91
GpGp − 16.00
0 5 10 15
Figure 12: MCB test results for the empirical evaluation based on CRPS for (A) Univariate Air Passengers,
(B) Multivariate PEMS-SF, and (C) Spatiotemporal Belgium COVID-19 datasets.
0.0
0.2
0.4
0.6
0.8
1.0PICP (Higher is Better)
Mean
nominal 1 = 0.95
LSTM-PC LSTM-BE NHITS-CPNHITS-CQR
GpGp
BNN-MCD DeepAR LSTM-QR GCEN K2VAE
Transformer-MAF
TimeGradDeepNPTSTimesFM-2.5 Chronos-2PatchTSTFM
2000
0
2000
4000
6000
8000
Winkler Score (Lower is Better)
Mean
Figure 13: PICP (top) and Winkler score (bottom) attained by the models on the Belgium COVID-19
dataset across 11 spatial nodes.
tests indicate less consistent performance across the broader dataset. Consequently, Chronos-2 proves more
robust, consistently yielding lower CRPS values across a larger subset of spatial nodes compared to GCEN.
Finally, foundation models such as Chronos-2 and TimesFM-2.5 offer highly competitive predictive perfor-
mance. AnanalysisofcomputationalefficiencyontheBelgiumCOVID-19dataset(Fig.14)revealssignificant
architectural trade-offs. By leveraging zero-shot learning, foundation models demonstrate minimal training
durations, functioning effectively with low initial overhead. In contrast, deep generative architectures de-
mand substantial computational resources; the normalizing-flow-based Transformer-MAF requires the most
50

Preprint
Chronos-2
TimesFM-2.5PatchTSTFM
BNN-MCDDeepNPTSNHiTS-CQR LSTM-QRDeepARNHiTS-CPLSTM-PCLSTM-BE K2VAEGCENGpGp TimeGrad
Transformer-MAF
0
50
100
150
200
250
300
350Time (Seconds)
1.20 2.06 2.21 3.68 6.31
16.87
28.63 32.26 32.65
48.48 49.38
63.38
81.00
90.96
232.83
369.42
(A) Training Time
K2VAE
DeepNPTSBNN-MCDLSTM-BELSTM-PCLSTM-QRDeepARGCEN
Transformer-MAF
TimesFM-2.5
Chronos-2
GpGp
NHiTS-CQRTimeGrad PatchTSTFM NHiTS-CP
0
5
10
15
20Time (Seconds)
0.02 0.05 0.07 0.09 0.09 0.11 0.12 0.19 0.59
6.67
11.91 11.96
13.63
16.47
17.78
23.17
(B) Inference Time
BNN-MCDDeepNPTS
TimesFM-2.5
Chronos-2
PatchTSTFM
LSTM-QR
NHiTS-CQR
DeepARLSTM-PCLSTM-BENHiTS-CP K2VAEGCENGpGp TimeGrad
Transformer-MAF
0
50
100
150
200
250
300
350Time (Seconds)
3.75 6.36 8.73 13.11 19.99
28.73 30.49 32.38
48.57 49.47 55.82
63.40
81.19
102.92
249.30
370.01
(C) Total Time
Training
Inference
Figure 14: (A) Training time, (B) inference time, and (C) total time taken by the representative models on
the spatiotemporal Belgium COVID-19 dataset.
training time, followed by the diffusion-based TimeGrad. However, their inference behaviors diverge, as
TimeGrad requires considerably more inference time than Transformer-MAF, which is highly efficient once
trained. These operational profiles emphasize the necessary compromise between generative complexity and
deployment speed in probabilistic forecasting tasks.
8 Challenges and Future Directions
Existing work demonstrates substantial progress in probabilistic forecasting, yet key open challenges remain,
which we discuss in Section 8.1. Promising research directions in this area are highlighted in Section 8.2.
8.1 Open Challenges
Some fundamental challenges in probabilistic forecasting still remain unresolved: quantifying uncertainty in
spatial dependency structures, embedding physical constraints into predictive distributions, forecasting rare
extremes, handling zero-inflated and count-valued outcomes, forecasting directional and continuous time
series, and bridging the gap between research and practice.
Uncertainty in dependency structures.Most spatiotemporal forecasting methods assume that spatial
dependencies are known or can be estimated deterministically. Whether represented through predefined
graphs (Kipf & Welling, 2017; Veličković et al., 2018), adjacency matrices (Barman et al., 2025; Panja et al.,
2026a), or covariance functions (Lindgren et al., 2011), these structures are treated as fixed during predic-
tion, despite being inferred from incomplete and evolving observations. Consequently, current probabilistic
forecasts account for uncertainty in model parameters or observations, but rarely quantify uncertainty in
the dependency structure itself. Adaptive graph learning methods such as adaptive graph convolutional
recurrent networks (Bai et al., 2020) alleviate the need for predefined connectivity by learning spatial de-
pendencies directly from data. However, the learned dependency structure is treated as deterministic and
uncertainty in these inferred relationships is not propagated into the predictive distribution. Developing
probabilistic forecasting models that jointly quantify uncertainty in both spatial dependencies and future
trajectories, therefore, remains an important research direction.
Physics-informed probabilistic forecasting.Many spatiotemporal systems are governed by known
physical or mechanistic principles, including conservation laws, epidemiological dynamics, and power-system
constraints. Recent methods enforce these constraints through domain-guided graph structures (Wang et al.,
2026b) or hybrid mechanistic-deep learning architectures (Barman et al., 2025). Although these approaches
demonstrate the value of incorporating domain knowledge into forecasting models, domain constraints do
not extend to the uncertainty quantification itself. Instead, predictive intervals are produced independently
51

Preprint
through post-hoc calibration. Embedding physical dynamics into the predictive distribution or calibration
mechanism to enforce domain-constrained predictive bounds remains an open challenge.
Forecasting extremes.Reliable uncertainty estimation for rare events remains one of the most diffi-
cult problems in probabilistic forecasting. Extreme observations are scarce, causing existing probabilistic
objectives to primarily fit the central part of the distribution, with extremes contributing minimally to
the optimization signal. EVT provides a principled statistical framework for modeling distributional tails
(Coles, 2001) and several recent methods have incorporated these ideas through bulk-tail likelihoods for spa-
tial processes (Castro-Camilo et al., 2019), extreme-value-aware graph convolutional forecasting networks
with conformal calibration (Panja et al., 2026a), quantile regression informed by EVT (Pasche & Engelke,
2024), and normalizing flows designed for multivariate tail dependence (De Monte et al., 2025). Despite
these advances, current approaches address different aspects of the problem in isolation. Simultaneously
modeling temporal evolution, spatial dependence, and multivariate tail behavior at realistic spatial scales
remains computationally demanding and evaluation is severely constrained by the scarcity of extreme events
available for calibration and validation.
Zero-inflated and count-valued spatiotemporal forecasting.Many spatiotemporal forecasting appli-
cations, including epidemiological surveillance (Francisco et al., 2024) and crime prediction (Wang et al.,
2025b), involve count-valued observations with a high proportion of zeros arising from absence or infrequent
event occurrence. These characteristics violate the assumptions underlying many probabilistic forecasting
methods, which predominantly model continuous-valued targets; as a result, accurately representing the
probability of observing zero events and the distribution of nonzero counts remains challenging (Wilson
et al., 2022). Although zero-inflated count models are well established in statistical modeling, their integra-
tion with modern probabilistic forecasting architectures remains limited. For example, Liu et al. (2025b)
incorporated Poisson, negative binomial, and zero-inflated likelihoods into an uncertainty-aware online learn-
ing framework, producing calibrated posterior estimates under overdispersion and excess zeros. However, it
models each time series independently and does not capture dependencies among interacting entities that
may be represented through graph structures. Conversely, Francisco et al. (2024) applied a two-stage hurdle
model for zero-inflated dengue forecasting across fine spatial resolutions, albeit their approach targets point
prediction. Recent work has begun to shift from point to probabilistic forecasting of zero-inflated spatiotem-
poral data. For instance, Wilson et al. (2022) extended the hurdle model with a generalized Pareto tail
component to jointly capture zero-inflation and heavy-tailed extremes in a single spatiotemporal framework,
while Wang et al. (2025b) combined diffusion graph convolutions with a zero-inflated negative binomial
likelihood for spatial crime forecasting. However, these approaches are restricted to regular grids with fixed
spatial adjacency. Extending zero-inflated models to irregular spatiotemporal networks remains largely un-
explored, particularly when both multi-horizon temporal dependencies and spatial structures must be jointly
estimated at scale.
Forecasting directional time series.Directional or circular time series consist of sequential observations
represented as angles, degrees, or compass headings. Their periodic topology, with values wrapping around at
360◦, violates the Euclidean assumptions of standard forecasting models and requires methods that account
for circular structure. Such data arises naturally across many scientific domains, such as spatiotemporal
wind directions, ocean current vectors, and animal migration bearings. Although circular data have been
studied extensively in temporal settings (Fisher & Lee, 1994; Di Marzio et al., 2012; Harvey et al., 2024) and
directional fields in spatiotemporal settings (Mastrantonio et al., 2016), existing approaches have focused
predominantly on point forecasting. Recent work has introduced uncertainty quantification for circular data
in regression settings (Prokudin et al., 2018; Pathak et al., 2026b), but reliable probabilistic forecasting for
complex spatiotemporal directional processes remains a significant open challenge.
Continuous-time probabilistic forecasting.Many real-world temporal and spatiotemporal processes
evolve continuously and are observed irregularly, including mobile-health signals such as ECG and wearable
measurements (Li et al., 2026b), financial transactions, network events, traffic systems, and environmental
sensor networks. In these examples, asynchronous sampling, missing observations, and irregular spatial mea-
surements challenge conventional discrete-time forecasting models (Liu & Hauskrecht, 2021). Neural ODEs
and Neural SDEs offer a natural framework for such data by representing latent dynamics in continuous time,
with the latter additionally modeling stochastic fluctuations through a diffusion process (Chen et al., 2018;
52

Preprint
Oh et al., 2024). However, existing continuous-time learning methods have been studied predominantly
from the perspective of point prediction or latent-state reconstruction (Wan et al., 2025), while reliable
probabilistic forecasting under irregular sampling and evolving temporal or spatial dependencies remains
comparatively underdeveloped. An important open challenge is therefore to develop scalable and inter-
pretable continuous-time probabilistic models that jointly accommodate irregular observations, missingness,
multivariate dependence, and dynamic spatial interactions in real-world applications.
Lack of a comprehensive software package.Software tools for probabilistic forecasting remain di-
vided, especially for spatiotemporal settings. As detailed in Section 6.1.2, most existing libraries focus
on temporal data. Spatiotemporal approaches can be implemented using the PyTorch-Geometric-Temporal
(Rozemberczki et al., 2021a) and Torch Spatiotemporal (tsl)9 libraries in Python; however, their capabilities
are restricted to point forecasting. Probabilistic spatiotemporal methods are typically released as research
repositories with incompatible interfaces. Hence, no single library implements all probabilistic forecasting
methods within a unified framework.
8.2 Future Directions
We highlight three promising directions for future research. One prominent trend is the emergence of foun-
dation models for forecasting (Section 5). Adler et al. (2025) showed that many of these models produce
well-calibrated probabilistic distributions in zero-shot settings, although calibration quality varies consider-
ably across architectures. Similar ideas are now being extended to spatiotemporal forecasting. OpenCity
(Li et al., 2025), for example, combines Transformer and GNN architectures to learn transferable represen-
tations that generalize across unseen cities, demonstrating the potential of foundation models for large-scale
spatiotemporal forecasting. Recent evidence also suggests that foundation models can achieve strong point-
forecasting performance on zero-inflated epidemiological datasets (Panja et al., 2026b); however, whether
thesemodelscanproduceequallywell-calibratedprobabilisticforecastsforzero-inflatedspatiotemporalcount
data remains an open question. A key research direction is extending foundation models to produce cali-
brated probabilistic forecasts across spatial domains under distribution shift at a feasible cost for real-world
deployment.
Another emerging direction is the development of adaptive probabilistic forecasting systems. Such systems
are particularly valuable in nonstationary environments, where shifts in data distributions or operating con-
ditions can rapidly degrade predictive performance. Recent work has explored adaptive ensemble strategies
based on multi-armed bandit algorithms, including upper confidence bound (UCB) and the exponential-
weight algorithm for exploration and exploitation (EXP3), which dynamically reweight candidate forecast-
ing models according to their recent performance (Karami et al., 2026a). Although these approaches have
demonstrated improved probabilistic forecasting in applications such as COVID-19 prediction, they primar-
ily adapt the combination of existing forecasts rather than the predictive uncertainty itself. Extending these
ideas toward fully adaptive probabilistic forecasting frameworks in an online manner represents a promising
research direction, particularly for spatiotemporal applications.
A third emerging direction is agentic probabilistic forecasting. Recent agentic frameworks move beyond a
single forecasting model and instead treat forecasting as a sequential decision process involving data diag-
nostics, preprocessing, model selection, validation, ensembling, contextual reasoning, and forecast synthesis.
For example, TimeSeriesScientist (Zhao et al., 2025a) employs specialized agents to automate the end-to-end
forecasting workflow, whereas Nexus (Das et al., 2026) combines multimodal contextual information with
macro- and micro-level reasoning agents and an error-driven calibration mechanism. However, uncertainty
quantification in such agentic systems remains largely unexplored. Existing frameworks primarily optimize
and evaluate point-forecast accuracy, while uncertainty may arise not only from the future observations
themselves, but also from model selection, external information, tool use, reasoning trajectories, and dis-
agreement among agents. A promising direction is therefore to develop agentic forecasting systems that
propagate these multiple sources of uncertainty into calibrated predictive distributions. Such systems could
combine probabilistic forecasting models, conformal calibration, or generative sampling with agent-level
reasoning and adaptive model selection, enabling agents to quantify when forecasts are reliable, recognize
9https://github.com/TorchSpatiotemporal/tsl
53

Preprint
when uncertainty has increased, and revise their forecasting strategy accordingly. Extending this paradigm
to spatiotemporal forecasting, where agents must additionally reason about uncertain and evolving spatial
dependencies, represents an important open frontier.
9 Conclusion
This survey provides a unified perspective on probabilistic forecasting for time series and spatiotemporal
data by organizing existing methods according to how predictive uncertainty is represented and quantified.
The resulting taxonomy discusses model-agnostic and model-intrinsic approaches. Beyond cataloging meth-
ods, our synthesis highlights a central message: no single probabilistic forecasting paradigm is universally
preferable. Our empirical study reinforces this conclusion, showing that point accuracy, calibration, sharp-
ness, probabilistic performance, and computational efficiency can favor substantially different methods across
univariate, multivariate, and spatiotemporal settings.
The field is now moving beyond the construction of prediction intervals around point forecasts toward
richer predictive systems that must represent uncertainty over complex, evolving, and structured futures.
At the same time, foundation models, adaptive forecasting systems, continuous-time probabilistic models,
and emerging agentic forecasting frameworks are creating new opportunities and new sources of uncertainty
that must themselves be quantified and calibrated. Progress will therefore require not only more expres-
sive forecasting architectures, but also principled mechanisms for representing and propagating uncertainty
throughout the forecasting pipeline. We hope that the taxonomy, practical guidance, empirical evidence,
and research agenda developed in this survey provide a foundation for both informed methodological choice
and the next generation of reliable probabilistic forecasting systems.
References
Moloud Abdar, Farhad Pourpanah, Sadiq Hussain, Dana Rezazadegan, Li Liu, Mohammad Ghavamzadeh,
Paul Fieguth, Xiaochun Cao, Abbas Khosravi, U. Rajendra Acharya, Vladimir Makarenkov, and Saeid Na-
havandi. A review of uncertainty quantification in deep learning: Techniques, applications and challenges.
Information Fusion, 76:243–297, 2021.
Oriol Abril-Pla, Virgile Andreani, Colin Carroll, Larry Dong, Christopher J. Fonnesbeck, Maxim Kochurov,
Ravin Kumar, Junpeng Lao, Christian C. Luhmann, Osvaldo A. Martin, Michael Osthege, Ricardo Vieira,
Thomas Wiecki, and Robert Zinkov. PyMC: A Modern and Comprehensive Probabilistic Programming
Framework in Python.PeerJ Computer Science, 9(e1516), 2023. doi: 10.7717/peerj-cs.1516.
Coen Adler, Yuxin Chang, Samar Abdi, and Padhraic Smyth. Calibration Properties of Time Series Foun-
dation Models. In1st ICML Workshop on Foundation Models for Structured Data, 2025.
Tobias Adrian, Nina Boyarchenko, and Domenico Giannone. Vulnerable Growth.American Economic
Review, 109(4):1263–89, April 2019.
Mousa Afrasiabi, Jamshid Aghaei, Shahabodin Afrasiabi, and Mohammad Mohammadi. Probability density
functionforecastingofelectricityprice: Deepgaborconvolutionalmixturenetwork.Electric Power Systems
Research, 213:108325, 2022.
Xwégnon Ghislain Agoua, Robin Girard, and George Kariniotakis. Probabilistic Models for Spatio-Temporal
Photovoltaic Power Forecasting.IEEE Transactions on Sustainable Energy, 10(2):780–789, 2019.
Edmund Fosu Agyemang. A Gaussian Process Regression and Wavelet Transform Time Series approaches
to modeling Influenza A.Computers in Biology and Medicine, 184:109367, 2025.
Oguzhan Akgun, Alain Pirotte, Giovanni Urga, and Zhenlin Yang. Equal predictive ability tests based on
panel data with applications to OECD and IMF forecasts.International Journal of Forecasting, 40(1):
202–228, 2024.
54

Preprint
Taha Aksu, Gerald Woo, Juncheng Liu, Xu Liu, Chenghao Liu, Silvio Savarese, Caiming Xiong, and Doyen
Sahoo. GIFT-Eval: A Benchmark For General Time Series Forecasting Model Evaluation.arXiv preprint
arXiv:2410.10393, 2024.
Abdullah Al-Manji, Adil Al Wahaibi, Mohammed Al-Azri, and Moon Fai Chan. Predicting mosquito-borne
disease outbreaks using poisson and negative binomial models: A comparative study.Journal of Infection
and Public Health, 18(11):102906, 2025.
Alexander Alexandrov, Konstantinos Benidis, Michael Bohlke-Schneider, Valentin Flunkert, Jan Gasthaus,
Tim Januschowski, Danielle C Maddix, Syama Rangapuram, David Salinas, Jasper Schulz, et al. GluonTS:
Probabilistic and Neural Time Series Modeling in Python.Journal of Machine Learning Research, 21(116):
1–6, 2020.
Yang An, Zhibin Li, Wei Liu, Haoliang Sun, Meng Chen, Wenpeng Lu, and Yongshun Gong. Spatio-temporal
Graph Normalizing Flow for Probabilistic Traffic Prediction. InProceedings of the 33rd ACM International
Conference on Information and Knowledge Management, pp. 45–55, 2024.
Yang An, Zhibin Li, Xiaoyu Li, Wei Liu, Xinghao Yang, Haoliang Sun, Meng Chen, Yu Zheng, and Yongshun
Gong. Spatio-Temporal Multivariate Probabilistic Modeling for Traffic Prediction.IEEE Transactions on
Knowledge and Data Engineering, 37(5):2986–3000, 2025.
Pritam Anand, Tathagata Bandyopadhyay, and Suresh Chandra. Tube Loss: A Novel Loss Function for
Prediction Interval Estimation.Transactions on Machine Learning Research, 2026.
Antony Andrews and Sean Kimpton. Econometric Forecasting of Tourist Arrivals Using Bayesian Structural
Time-Series.Economic Papers: A journal of applied economics and policy, 42(2):200–211, 2023.
Anastasios N. Angelopoulos and Stephen Bates. Conformal Prediction: A Gentle Introduction.Foundations
and Trends in Machine Learning, 16(4):494–591, March 2023.
Abdul Fatir Ansari, Lorenzo Stella, Caner Turkmen, Xiyuan Zhang, Pedro Mercado, Huibin Shen, Olek-
sandr Shchur, Syama Sundar Rangapuram, Sebastian Pineda Arango, Shubham Kapoor, et al. Chronos:
Learning the language of time series.Transactions on Machine Learning Research, 2024.
Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, Andreas Auer, Boran Han, Pedro Mercado, Syama Sun-
dar Rangapuram, Huibin Shen, Lorenzo Stella, Xiyuan Zhang, et al. Chronos-2: From Univariate to
Universal Forecasting.arXiv preprint arXiv:2510.15821, 2025.
Arjun Ashok, Étienne Marcotte, Valentina Zantedeschi, Nicolas Chapados, and Alexandre Drouin. TACTiS-
2: Better, Faster, Simpler Attentional Copulas for Multivariate Time Series. InThe Twelfth International
Conference on Learning Representations, 2024.
Andreas Auer, Patrick Podest, Daniel Klotz, Sebastian Böck, Günter Klambauer, and Sepp Hochreiter.
TiRex: Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning.
Advances in Neural Information Processing Systems, 38:57529–57580, 2026.
Lei Bai, Lina Yao, Can Li, Xianzhi Wang, and Can Wang. Adaptive Graph Convolutional Recurrent Network
for Traffic Forecasting.Advances in Neural Information Processing Systems, 33:17804–17815, 2020.
Madhab Barman, Madhurima Panja, Nachiketa Mishra, and Tanujit Chakraborty. Epidemic-guided deep
learning for spatiotemporal forecasting of tuberculosis outbreak.Machine Learning, 114(10), August 2025.
Leonard E. Baum, Ted Petrie, George Soules, and Norman Weiss. A Maximization Technique Occurring
in the Statistical Analysis of Probabilistic Functions of Markov Chains.The Annals of Mathematical
Statistics, 41(1):164–171, 1970.
Ioannis K. Bazionis and Pavlos S. Georgilakis. Review of Deterministic and Probabilistic Wind Power
Forecasting: Models, Methods, and Future Research.Electricity, 2(1):13–47, 2021.
55

Preprint
Matthew Beal, Zoubin Ghahramani, and Carl Rasmussen. The Infinite Hidden Markov Model. InAdvances
in Neural Information Processing Systems, volume 14, 2001.
Maximilian Beck, Korbinian Pöppel, Markus Spanring, Andreas Auer, Oleksandra Prudnikova, Michael
Kopp, Günter Klambauer, Johannes Brandstetter, and Sepp Hochreiter. xLSTM: Extended Long Short-
Term Memory.Advances in Neural Information Processing Systems, 37:107547–107603, 2024.
Yoshua Bengio and Paolo Frasconi. An Input Output HMM Architecture. InAdvances in Neural Information
Processing Systems, volume 7. MIT Press, 1994.
Konstantinos Benidis, Syama Sundar Rangapuram, Valentin Flunkert, Yuyang Wang, Danielle Maddix,
Caner Turkmen, Jan Gasthaus, Michael Bohlke-Schneider, David Salinas, Lorenzo Stella, François-Xavier
Aubet, Laurent Callot, and Tim Januschowski. Deep learning for time series forecasting: Tutorial and
literature survey.ACM Computing Surveys, 55(6), December 2022.
Shane Bergsma, Tim Zeyl, Javad Rahimipour Anaraki, and Lei Guo. C2FAR: Coarse-to-Fine Autoregressive
Networks for Precise Probabilistic Forecasting.Advances in Neural Information Processing Systems, 35:
21900–21915, 2022.
Donia Besher, Madhurima Panja, Shovon Sengupta, and Tanujit Chakraborty. Neural ARFIMA model for
forecasting BRIC exchange rates with long memory.arXiv preprint arXiv:2509.06697, 2026a.
Donia Besher, Anirban Sengupta, and Tanujit Chakraborty. Probabilistic Forecasting of Climate Pol-
icy Uncertainty: The Role of Macro-financial Variables and Google Search Data.arXiv preprint
arXiv:2507.12276, 2026b.
Marin Biloš, Kashif Rasul, Anderson Schneider, Yuriy Nevmyvaka, and Stephan Günnemann. Modeling
Temporal Data as Continuous Functions with Stochastic Process Diffusion. InProceedings of the 40th
International Conference on Machine Learning, volume 202 ofProceedings of Machine Learning Research,
pp. 2452–2470. PMLR, 2023.
Eli Bingham, Jonathan P. Chen, Martin Jankowiak, Fritz Obermeyer, Neeraj Pradhan, Theofanis Karaletsos,
Rohit Singh, Paul Szerlip, Paul Horsfall, and Noah D. Goodman. Pyro: Deep Universal Probabilistic
Programming.Journal of Machine Learning Research, 2018.
Christopher M. Bishop. Mixture density networks. WorkingPaper 4288, Aston University, 1994.
Christopher M. Bishop.Pattern Recognition and Machine Learning. Springer, New York, NY, 1 edition,
2006.
Txus Blasco, J. Salvador Sánchez, and Vicente García. A survey on uncertainty quantification in deep
learning for financial time series prediction.Neurocomputing, 576:127339, 2024.
David M. Blei, Alp Kucukelbir, and Jon D. McAuliffe. Variational Inference: A Review for Statisticians.
Journal of the American Statistical Association, 112(518):859–877, 2017.
Leo Breiman. Random forests.Machine learning, 45(1):5–32, 2001.
Paul-Christian Bürkner. Bayesian Item Response Modeling in R with brms and Stan.Journal of Statistical
Software, 100:1–54, 2021.
Salva Rühling Cachay, Bo Zhao, Hailey Joren, and Rose Yu. DYffusion: A dynamics-informed diffusion
model for spatiotemporal forecasting. InAdvances in Neural Information Processing Systems, volume 36,
pp. 45259–45287, 2023.
Michela Cameletti, Finn Lindgren, Daniel Simpson, and Håvard Rue. Spatio-temporal modeling of particu-
late matter concentration through the SPDE approach.Advances in Statistical Analysis, 97(2):109–131,
2013.
56

Preprint
Alex J. Cannon. Quantile regression neural networks: Implementation in R and application to precipitation
downscaling.Computers & Geosciences, 37(9):1277–1284, 2011.
A. Carpentieri, D. Folini, J. Leinonen, and A. Meyer. Extending intraday solar forecast horizons with deep
generative models.Applied Energy, 377:124186, 2025.
E. Castillo.Statistical Process Adjustment for Quality Control. Wiley Series in Probability and Statistics.
Wiley, 2002.
Daniela Castro-Camilo, Raphaël Huser, and Håvard Rue. A spliced Gamma-Generalized Pareto model for
short-term extreme wind speed probabilistic forecasting.Journal of Agricultural, Biological and Environ-
mental Statistics, 24(3):517–534, 2019.
Stefano Castruccio, Hernando Ombao, and Marc G. Genton. A scalable multi-resolution spatio-temporal
model for brain activation and connectivity in fMRI data.Biometrics, 74(3):823–833, 2018.
Tanujit Chakraborty, Ujjwal Reddy K S, Shraddha M Naik, Madhurima Panja, and Bayapureddy Manvitha.
Ten Years of Generative Adversarial Nets (GANs): A survey of the state-of-the-art.Machine Learning:
Science and Technology, 5(1), 2024.
Cristian Challu, Kin G Olivares, Boris N Oreshkin, Federico Garza Ramirez, Max Mergenthaler Canseco, and
Artur Dubrawski. NHITS: Neural Hierarchical Interpolation for Time Series Forecasting. InProceedings
of the AAAI Conference on Artificial Intelligence, volume 37, pp. 6989–6997, 2023.
Sulkhan Chavleishvili and Simone Manganelli. Forecasting and stress testing with quantile vector autore-
gression.Journal of Applied Econometrics, 39(1):66–85, 2024.
Jieyu Chen, Sebastian Lerch, Melanie Schienle, Tomasz Serafin, and Rafał Weron. Probabilistic intraday
electricity price forecasting using generative machine learning.arXiv preprint arXiv:2506.00044, 2025.
Kehua Chen, Guangbo Li, Hewen Li, Yuqi Wang, Wenzhe Wang, Qingyi Liu, and Hongcheng Wang. Quan-
tifying uncertainty: Air quality forecasting based on dynamic spatial-temporal denoising diffusion proba-
bilistic model.Environmental Research, 249:118438, 2024.
Ricky TQ Chen, Yulia Rubanova, Jesse Bettencourt, and David K Duvenaud. Neural Ordinary Differential
Equations.Advances in Neural Information Processing Systems, 31, 2018.
Xiaoxu Chen, Zhanhong Cheng, Jian Gang Jin, Martin Trépanier, and Lijun Sun. Probabilistic Forecasting
of Bus Travel Time with a Bayesian Gaussian Mixture Model.Transportation Science, 57(6):1516–1535,
November 2023.
Long Cheng, Da Lei, and Sui Tao. Recent advances in deep learning for traffic probabilistic prediction.
Transport Reviews, 44(6):1129–1135, 2024.
Victor Chernozhukov, Iván Fernández-Val, and Alfred Galichon. Rearranging Edgeworth-Cornish-Fisher
Expansions.Economic Theory, 42(2):419–435, 2010.
Hugh A. Chipman, Edward I. George, and Robert E. McCulloch. BART: Bayesian additive regression trees.
The Annals of Applied Statistics, 4(1):266 – 298, 2010. doi: 10.1214/09-AOAS285.
Shu Wei Chou-Chen, Luis A. Barboza, Paola Vásquez, Yury E. García, Juan G. Calvo, Hugo G. Hidalgo,
and Fabio Sanchez. Bayesian spatio-temporal model with INLA for dengue fever risk prediction in Costa
Rica.Environmental and Ecological Statistics, 30(4):687–713, 2023.
Wenhao Chu, Chunxiao Zhang, Heng Li, Laifu Zhang, Dingtao Shen, and Rongrong Li. SHAP-powered in-
sights into spatiotemporal effects: Unlocking explainable Bayesian-neural-network urban flood forecasting.
International Journal of Applied Earth Observation and Geoinformation, 131:103972, 2024.
Junyoung Chung, Kyle Kastner, Laurent Dinh, Kratarth Goel, Aaron Courville, and Yoshua Bengio. A
RecurrentLatentVariableModelforSequentialData.Advances in Neural Information Processing Systems,
28, 2015.
57

Preprint
Andrea Cini, Alexander Jenkins, Danilo Mandic, Cesare Alippi, and Filippo Maria Bianchi. Relational
Conformal Prediction for Correlated Time Series. InForty-second International Conference on Machine
Learning, 2025.
James S. Clark. Why environmental scientists are becoming bayesians.Ecology Letters, 8(1):2–14, 2005.
J Clarke, A Lim, P Gupte, DM Pigott, WG Van Panhuis, and OJ Brady. A global dataset of publicly
available dengue case count data.Scientific Data, 11(1):296, 2024.
S. Coles.An Introduction to Statistical Modeling of Extreme Values. Springer Series in Statistics. Springer,
2001.
Adrien Cortes, Remi Rehm, and Victor Letzelter. Winner-takes-all for Multivariate Probabilistic Time Series
Forecasting. InForty-second International Conference on Machine Learning, 2025.
Dario Coscia, Max Welling, Nicola Demo, and Gianluigi Rozza. BARNN: A Bayesian Autoregressive and
Recurrent Neural Network. InForty-second International Conference on Machine Learning, 2025.
Noel Cressie and Christopher K Wikle.Statistics for Spatio-Temporal Data. John Wiley & Sons, 2011.
Haipeng Cui, Kun Xie, Bin Hu, and Hangfei Lin. Online Bus Speed Prediction With Spatiotemporal
Interaction: A Laplace Approximation-Based Bayesian Approach.IEEE Access, 9:105205–105219, 2021.
Xilin Dai, Zhijian Xu, Wanxu Cai, and Qiang Xu. From Samples to Scenarios: A New Paradigm for
Probabilistic Forecasting. InThe Fourteenth International Conference on Learning Representations, 2026.
Stefano Damato, Dario Azzimonti, and Giorgio Corani. Forecasting intermittent time series with Gaussian
Processes and Tweedie likelihood.International Journal of Forecasting, 2025.
Abhimanyu Das, Weihao Kong, Rajat Sen, and Yichen Zhou. A decoder-only foundation model for time-
series forecasting. InForty-first International Conference on Machine Learning, 2024.
Sarkar Snigdha Sarathi Das, Palash Goyal, Mihir Parmar, Nanyun Peng, Vishy Tirumalashetty, Chun-
Liang Li, Rui Zhang, Jinsung Yoon, and Tomas Pfister. Nexus : An Agentic Framework for Time Series
Forecasting.arXiv preprint arXiv:2605.14389, 2026.
David De León Pérez, Sergio Salazar-Galán, and Félix Francés. Beyond Deterministic Forecasts: A Scoping
Review of Probabilistic Uncertainty Quantification in Short-to-Seasonal Hydrological Prediction.Water,
17(20), 2025.
Lambert De Monte, Raphaël Huser, Ioannis Papastathopoulos, and Jordan Richards. Generative modelling
of multivariate geometric extremes using normalising flows.arXiv preprint arXiv:2505.02957, 2025.
Perry de Valpine, Daniel Turek, Christopher J Paciorek, Clifford Anderson-Bergman, Duncan Temple Lang,
and Rastislav Bodik. Programming With Models: Writing Statistical Algorithms for General Model
Structures With NIMBLE.Journal of Computational and Graphical Statistics, 26(2):403–413, 2017.
A. P. Dempster, N. M. Laird, and D. B. Rubin. Maximum Likelihood from Incomplete Data via the EM
Algorithm.Journal of the Royal Statistical Society Series B: Statistical Methodology, 39(1):1–38, 1977.
Macro Di Marzio, Agnese Panzera, and Charles C Taylor. Non-parametric smoothing and prediction for
nonlinear circular time series.Journal of Time Series Analysis, 33(4):620–630, 2012.
Francis X. Diebold. Forecasting, structural time series models and the kalman filter.Econometric Theory,
8(2):293–299, 1992.
Francis X. Diebold and Roberto S. Mariano. Comparing Predictive Accuracy.Journal of Business &
Economic Statistics, 13(3):253–263, 1995.
Thomas G. Dietterich. Ensemble Methods in Machine Learning. InMultiple Classifier Systems, pp. 1–15.
Springer Berlin Heidelberg, 2000.
58

Preprint
Michael C. Dietze.Ecological Forecasting. Princeton University Press, 2017.
Michael C. Dietze, Andrew Fox, Lindsay M. Beck-Johnson, Julio L. Betancourt, Mevin B. Hooten, Cather-
ine S. Jarnevich, Timothy H. Keitt, Melissa A. Kenney, Christine M. Laney, Laurel G. Larsen, Henry W.
Loescher, Claire K. Lunch, Bryan C. Pijanowski, James T. Randerson, Emily K. Read, Andrew T. Tre-
dennick, Rodrigo Vargas, Kathleen C. Weathers, and Ethan P. White. Iterative near-term ecological
forecasting: Needs, opportunities, and challenges.Proceedings of the National Academy of Sciences, 115
(7):1424–1432, 2018.
LaurentDinh, JaschaSohl-Dickstein, andSamyBengio. DensityestimationusingRealNVP. InInternational
Conference on Learning Representations, 2017.
Alexandre Drouin, Étienne Marcotte, and Nicolas Chapados. TACTiS: Transformer-Attentional Copulas for
Time Series. InProceedings of the 39th International Conference on Machine Learning, volume 162 of
Proceedings of Machine Learning Research, pp. 5447–5493. PMLR, 2022.
Grzegorz Dudek, Paweł Piotrowski, Marcin Kopyt, and Dariusz Baczyński. Recent Advances in Probabilistic
Electricity Price Forecasting: A Review of Methods and Evaluation Metrics.Energies, 19(15):3552, 2026.
Lea Duncker, Kiersten M. Ruda, Greg D. Field, and Jonathan W. Pillow. Scalable Variational Inference for
Low-Rank Spatiotemporal Receptive Fields.Neural Computation, 35(6):995–1027, 2023.
Bradley Efron and Robert J. Tibshirani.An Introduction to the Bootstrap, volume 57 ofMonographs on
Statistics and Applied Probability. Chapman & Hall/CRC, Boca Raton, FL, 1993.
Sivert Eggen, Tord Johan Espe, Kristoffer Grude, Morten Risstad, and Rickard Sandberg. Financial Time
Series Uncertainty: A Review of Probabilistic AI Applications.Journal of Economic Surveys, 40(2):
915–953, 2026.
Vijay Ekambaram, Arindam Jati, Pankaj Dayama, Sumanta Mukherjee, Nam H Nguyen, Wesley M Gifford,
Chandra Reddy, and Jayant Kalagnanam. Tiny Time Mixers (TTMs): Fast Pre-trained Models for
Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series. InAdvances in Neural Information
Processing Systems, volume 37, pp. 74147–74181, 2024.
Graham Elliott, Clive Granger, and A. Timmermann (eds.).Handbook of Economic Forecasting, volume 2.
Elsevier, 1 edition, 2013.
Rémi Emonet, Jagannadan Varadarajan, and Jean-Marc Odobez. Temporal Analysis of Motif Mixtures
Using Dirichlet Processes.IEEE Transactions on Pattern Analysis and Machine Intelligence, 36(1):140–
156, 2013.
Tobias Michael Erhardt, Claudia Czado, and Ulf Schepsmeier. R-vine models for spatial time series with an
application to daily mean temperature.Biometrics, 71(2):323–332, 06 2015.
Otto Fabius and Joost R Van Amersfoort. Variational Recurrent Auto-Encoders.arXiv preprint
arXiv:1412.6581, 2014.
Rasool Fakoor, Taesup Kim, Jonas Mueller, Alexander J. Smola, and Ryan J. Tibshirani. Flexible Model
Aggregation for Quantile Regression.Journal of Machine Learning Research, 24(162):1–45, 2023.
Xinyao Fan, Yueying Wu, Chang Xu, Yuhao Huang, Weiqing Liu, and Jiang Bian. MG-TSD: Multi-
Granularity Time Series Diffusion Models with Guided Learning Process. InThe Twelfth International
Conference on Learning Representations, 2024.
Esmail Abdul Fattah, Elias Krainski, and Havard Rue. PyINLA: Fast Bayesian Inference for Latent Gaussian
Models in Python.arXiv preprint arXiv:2603.27276, 2026.
Brandon R. Feng, David Keetae Park, Xihaier Luo, Arantxa Urdangarin, Shinjae Yoo, and Brian Reich.
STACI: Spatio-temporal aleatoric conformal inference. InThe Thirty-ninth Annual Conference on Neural
Information Processing Systems, 2025.
59

Preprint
Shibo Feng, Chunyan Miao, Zhong Zhang, and Peilin Zhao. Latent Diffusion Transformer for Probabilistic
Time Series Forecasting. InProceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp.
11979–11987, 2024.
Thomas S Ferguson. A Bayesian analysis of some nonparametric problems.The Annals of Statistics, pp.
209–230, 1973.
T. Ferté, V. Thevenet, X. Hinaut, P. Legrand, D. Dutartre, R. Griffier, V. Jouhet, B. Hejblum, and
R. Thiébaut. Epidemic Forecasting: Lessons Learned from the SARS-CoV-2 Pandemic to Balance Accu-
racy, Feasibility, and Impact.Journal of Epidemiology and Population Health, 74:203421, 2026.
Andrew O Finley, Sudipto Banerjee, and Bradley P Carlin. spBayes: An R Package for Univariate and
Multivariate Hierarchical Point-referenced Spatial Models.Journal of Statistical Software, 19:1–24, 2007.
NI Fisher and AJ Lee. Time series analysis of circular data.Journal of the Royal Statistical Society: Series
B (Methodological), 56(2):327–339, 1994.
Seth Flaxman, Andrew Wilson, Daniel Neill, Hannes Nickisch, and Alex Smola. Fast kronecker inference in
gaussian processes with non-gaussian likelihoods. InProceedings of the 32nd International Conference on
Machine Learning, volume 37 ofProceedings of Machine Learning Research, pp. 607–616. PMLR, 2015.
Emily B. Fox, Erik B. Sudderth, Michael I. Jordan, and Alan S. Willsky. A sticky HDP-HMM with appli-
cation to speaker diarization.The Annals of Applied Statistics, 5(2A):1020–1056, 2011.
Micanaldo Ernesto Francisco, Thaddeus M. Carvajal, and Kozo Watanabe. Hybrid Machine Learning Ap-
proach to Zero-Inflated Data Improves Accuracy of Dengue Prediction.PLOS Neglected Tropical Diseases,
18(10):1–22, 10 2024.
Geir-Arne Fuglstad, Daniel Simpson, Finn Lindgren, and Håvard Rue. Does non-stationary spatial data
always require non-stationary random fields?Spatial Statistics, 14:505–531, 2015.
Yarin Gal and Zoubin Ghahramani. Dropout as a Bayesian Approximation: Representing Model Uncertainty
in Deep Learning. InProceedings of The 33rd International Conference on Machine Learning, volume 48
ofProceedings of Machine Learning Research, pp. 1050–1059. PMLR, 2016a.
Yarin Gal and Zoubin Ghahramani. A Theoretically Grounded Application of Dropout in Recurrent Neural
Networks.Advances in Neural Information Processing Systems, 29, 2016b.
Nan Gao, Hao Xue, Wei Shao, Sichen Zhao, Kyle Kai Qin, Arian Prabowo, Mohammad Saiedur Rahaman,
and Flora D. Salim. Generative Adversarial Networks for Spatio-temporal Data: A Survey.ACM Trans-
actions on Intelligent Systems and Technology, 13(2), February 2022.
Jacob Gardner, Geoff Pleiss, Kilian Q Weinberger, David Bindel, and Andrew G Wilson. GPyTorch: Black-
box Matrix-Matrix Gaussian Process Inference with GPU Acceleration.Advances in Neural Information
Processing Systems, 31, 2018.
Jakob Gawlikowski, Cedrique Rovile Njieutcheu Tassi, Mohsin Ali, Jongseok Lee, Matthias Humt, Jianxiang
Feng, Anna Kruspe, Rudolph Triebel, Peter Jung, Ribana Roscher, Muhammad Shahzad, Wen Yang,
Richard Bamler, and Xiao Xiang Zhu. A survey of uncertainty in deep neural networks.Artificial Intelli-
gence Review, 56(1):1513–1589, July 2023.
Stuart Geman and Donald Geman. Stochastic Relaxation, Gibbs Distributions, and the Bayesian Restoration
of Images.IEEE Transactions on Pattern Analysis and Machine Intelligence, (6):721–741, 1984.
Edward I. George and Robert E. McCulloch. Approaches for Bayesian variable selection.Statistica Sinica,
7(2):339–373, April 1997.
Soumya Ghosh, Jiayu Yao, and Finale Doshi-Velez. Model Selection in Bayesian Neural Networks via
Horseshoe Priors.Journal of Machine Learning Research, 20(182):1–46, 2019.
60

Preprint
Raffaella Giacomini and Halbert White. Tests of Conditional Predictive Ability.Econometrica, 74(6):
1545–1578, 2006.
Isaac Gibbs and Emmanuel Candes. Adaptive Conformal Inference Under Distribution Shift. InAdvances
in Neural Information Processing Systems, volume 34, pp. 1660–1672, 2021.
Leon Glass, Peter Hunter, and Andrew McCulloch.Theory of heart: biomechanics, biophysics, and nonlinear
dynamics of cardiac function. Springer Science & Business Media, 2012.
Tilmann Gneiting and Matthias Katzfuss. Probabilistic Forecasting.Annual Review of Statistics and Its
Application, 1:125–151, 2014.
Tilmann Gneiting and Adrian E Raftery. Strictly Proper Scoring Rules, Prediction, and Estimation.Journal
of the American Statistical Association, 102(477):359–378, 2007.
Tilmann Gneiting, Adrian E. Raftery, Anton H. Westveld, and Tom Goldman. Calibrated Probabilistic
Forecasting Using Ensemble Model Output Statistics and Minimum CRPS Estimation.Monthly Weather
Review, 133(5):1098 – 1118, 2005.
Tilmann Gneiting, Kristin Larson, Kenneth Westrick, Marc G Genton, and Eric Aldrich. Calibrated Proba-
bilistic Forecasting at the Stateline Wind Energy Center.Journal of the American Statistical Association,
101(475):968–979, 2006.
Tilmann Gneiting, Fadoua Balabdaoui, and Adrian E. Raftery. Probabilistic forecasts, calibration and
sharpness.Journal of the Royal Statistical Society Series B: Statistical Methodology, 69(2):243–268, 2007.
Tilmann Gneiting, Daniel Wolffram, Johannes Resin, Kristof Kraus, Johannes Bracher, Timo Dimitriadis,
Veit Hagenmeyer, Alexander I. Jordan, Sebastian Lerch, Kaleb Phipps, and Melanie Schienle. Model
Diagnostics and Forecast Evaluation for Quantiles.Annual Review of Statistics and Its Application, 10:
597–621, 2023.
RakshithaWathsadiniGodahewa, ChristophBergmeir, GeoffreyIWebb, RobHyndman, andPabloMontero-
Manso. Monash Time Series Forecasting Archive. InThirty-fifth Conference on Neural Information
Processing Systems Datasets and Benchmarks Track (Round 2), 2021.
Mingze Gong, Lei Chen, and Jia Li. ProGen: Revisiting Probabilistic Spatial-Temporal Time Series Fore-
casting from a Continuous Generative Perspective Using Stochastic Differential Equations.arXiv preprint
arXiv:2411.01267, 2024.
Ian J Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron
Courville, and Yoshua Bengio. Generative Adversarial Nets.Advances in Neural Information Processing
Systems, 27, 2014.
Rahul Goswami, Shinjini Paul, Palash Ghosh, and Tanujit Chakraborty. Long-Memory Reservoir Computing
for Data-Scarce Dengue Forecasting.arXiv preprint arXiv:2607.11272, 2026.
Adrian Grantham, Yulia R. Gel, and John Boland. Nonparametric short-term probabilistic forecasting for
solar radiation.Solar Energy, 133:465–475, 2016.
Alex Graves. Practical Variational Inference for Neural Networks. InAdvances in Neural Information
Processing Systems, volume 24, 2011.
Joseph Guinness. Permutation and Grouping Methods for Sharpening Gaussian Process Approximations.
Technometrics, 60(4):415–429, 2018.
Shengnan Guo, Youfang Lin, Huaiyu Wan, Xiucheng Li, and Gao Cong. Learning dynamics and hetero-
geneity of spatial-temporal graph data for traffic forecasting.IEEE Transactions on Knowledge and Data
Engineering, 34(11):5415–5428, 2021.
61

Preprint
Agrim Gupta, Justin Johnson, Li Fei-Fei, Silvio Savarese, and Alexandre Alahi. Social GAN: Socially Ac-
ceptable Trajectories with Generative Adversarial Networks. In2018 IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pp. 2255–2264, 2018.
Abner Guzmán-rivera, Dhruv Batra, and Pushmeet Kohli. Multiple Choice Learning: Learning to Produce
Multiple Structured Outputs. InAdvances in Neural Information Processing Systems, volume 25, 2012.
Oliver Hamelijnck, William Wilkinson, Niki Loppi, Arno Solin, and Theodoros Damoulas. Spatio-Temporal
Variational Gaussian Processes.Advances in Neural Information Processing Systems, 34:23621–23633,
2021.
Peter R. Hansen, Asger Lunde, and James M. Nason. The Model Confidence Set.Econometrica, 79(2):
453–497, 2011.
Andrew Harvey, Stan Hurn, Dario Palumbo, and Stephen Thiele. Modelling circular time series.Journal of
Econometrics, 239(1):105450, 2024.
Masoud Muhammed Hassan. Bitcoin Price Prediction Using Deep Bayesian LSTM With Uncertainty Quan-
tification: A Monte Carlo Dropout–Based Approach.Stat, 13(3):e70001, 2024.
Hilaf Hasson, Bernie Wang, Tim Januschowski, and Jan Gasthaus. Probabilistic forecasting: A level-set
approach.Advances in Neural Information Processing Systems, 34:6404–6416, 2021.
W. K. Hastings. Monte Carlo Sampling Methods Using Markov Chains and Their Applications.Biometrika,
57(1):97–109, 1970.
Niko Hauzenberger, Florian Huber, Karin Klieber, and Massimiliano Marcellino. Bayesian neural networks
for macroeconomic analysis.Journal of Econometrics, 249:105843, 2025.
Jinhua He and Zechun Hu. Probabilistic Forecasting Method for Offshore Wind Farm Cluster under Typhoon
Conditions: a Score-Based Conditional Diffusion Model.arXiv preprint arXiv:2508.10705, 2025.
Zhiqiang He, Can Wan, Kaiming Zhang, and Ping Ju. Hybrid Score-Driven Multivariate Probabilistic
Forecasting of Correlated PV Generation Using Deep Mixture Density Network.IEEE Transactions on
Sustainable Energy, pp. 1–14, 2026.
N Hemavathi and R Sumathi. Modelling Predictive Uncertainty for Reliable Traffic Flow Forecasting Using
UA-STTFF Framework. In2026 4th International Conference on Knowledge Engineering and Communi-
cation Systems, pp. 1–8, 2026.
Julien Herzen, Francesco Lässig, Samuele Giuliano Piazzetta, Thomas Neuer, Léo Tafti, Guillaume Raille,
Tomas Van Pottelbergh, Marek Pasieka, Andrzej Skrodzki, Nicolas Huguenin, et al. Darts: User-friendly
modern machine learning for time series.Journal of Machine Learning Research, 23(124):1–6, 2022.
Simon Hirsch. Online Multivariate Regularized Distributional Regression for High-dimensional Probabilistic
Electricity Price Forecasting.arXiv preprint arXiv:2504.02518, 2025.
Nils Lid Hjort, Chris Holmes, Peter Müller, and Stephen G Walker.Bayesian nonparametrics, volume 28.
Cambridge University Press, 2010.
Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising Diffusion Probabilistic Models.Advances in Neural
Information Processing Systems, 33:6840–6851, 2020.
Sepp Hochreiter and Jürgen Schmidhuber. Long Short-Term Memory.Neural Computation, 9(8):1735–1780,
November 1997.
Jennifer A. Hoeting, David Madigan, Adrian E. Raftery, and Chris T. Volinsky. Bayesian model averaging:
A tutorial.Statistical Science, 14(4):382 – 417, 1999.
Matthew D. Hoffman, David M. Blei, Chong Wang, and John Paisley. Stochastic variational inference.
Journal of Machine Learning Research, 14(40):1303–1347, 2013.
62

Preprint
Daniel Holmberg, Joel Oskarsson, Erik Wikingsson, Fredrik Lindsten, and Teemu Roos. Njord: A Proba-
bilistic Graph Neural Network for Ensemble Ocean Forecasting.arXiv preprint arXiv:2605.15470, 2026.
Tao Hong and Shu Fan. Probabilistic electric load forecasting: A tutorial review.International Journal of
Forecasting, 32(3):914–938, 2016.
JianmingHu, QingxiLuo, JingweiTang, JianiHeng, andYuwenDeng. Conformalizedtemporalconvolutional
quantile regression networks for wind power interval forecasting.Energy, 248:123497, 2022.
Huang Huang, Stefano Castruccio, and Marc G. Genton. Forecasting High-Frequency Spatio-Temporal Wind
Power with Dimensionally Reduced Echo State Networks.Journal of the Royal Statistical Society Series
C: Applied Statistics, 71(2):449–466, 03 2022.
Jianguo Huang, Jianqing Song, Xuanning Zhou, Bingyi Jing, and Hongxin Wei. TorchCP: A Python Library
for Conformal Prediction.Journal of Machine Learning Research, 26(266):1–25, 2025.
Lei Huang, Jihui Zhuang, Xiaoming Cheng, Riming Xu, and Hongjie Ma. STI-GAN: Multimodal Pedestrian
Trajectory Prediction Using Spatiotemporal Interactions and a Generative Adversarial Network.IEEE
Access, 9:50846–50856, 2021.
Rob Hyndman and G. Athanasopoulos.Forecasting: Principles and Practice. OTexts, Australia, 3rd edition,
2021.
Rob J. Hyndman.expsmooth: Data Sets from Forecasting with Exponential Smoothing, 2015. URLhttps:
//cran.r-project.org/web/packages/expsmooth/. R package version 2.3.
Rob J Hyndman and Yeasmin Khandakar. Automatic Time Series Forecasting: The forecast Package for R.
Journal of Statistical Software, 27:1–22, 2008.
Catalin Ionescu, Dragos Papava, Vlad Olaru, and Cristian Sminchisescu. Human3.6M: Large scale datasets
and predictive methods for 3D human sensing in natural environments.IEEE Transactions on Pattern
Analysis and Machine Intelligence, 36(7):1325–1339, 2013.
Herbert Jaeger. The “echo state” approach to analysing and training recurrent neural networks-with an
erratum note.Bonn, Germany: German national research center for information technology gmd technical
report, 148(34):13, 2001.
Hosagrahar V Jagadish, Johannes Gehrke, Alexandros Labrinidis, Yannis Papakonstantinou, Jignesh M
Patel, Raghu Ramakrishnan, and Cyrus Shahabi. Big data and its technical challenges.Communications
of the ACM, 57(7):86–94, 2014.
I. Gede Nyoman M. Jaya and Henk Folmer. Bayesian spatiotemporal forecasting and mapping of COVID-19
risk with application to West Java Province, Indonesia.Journal of Regional Science, 61(4):849–881, 2021.
I Gede Nyoman Mindra Jaya and Henk Folmer. High-Resolution Spatiotemporal Forecasting with Missing
Observations Including an Application to Daily Particulate Matter 2.5 Concentrations in Jakarta Province,
Indonesia.Mathematics, 12(18), 2024.
Vilde Jensen, Filippo Maria Bianchi, and Stian Normann Anfinsen. Ensemble Conformalized Quantile
Regression for Probabilistic Time Series Forecasting.IEEE Transactions on Neural Networks and Learning
Systems, 35(7):9014–9025, 2024.
Lingyu Jiang, Lingyu Xu, Peiran Li, Dengzhe Hou, Qianwen Ge, Dingyi Zhuang, Shuo Xing, Wenjing
Chen, Xiangbo Gao, Ting-Hsuan Chen, et al. TimePre: Bridging Accuracy, Efficiency, and Stability in
Probabilistic Time-Series Forecasting.Transactions on Machine Learning Research, 2026.
Renhe Jiang, Zhaonan Wang, Jiawei Yong, Puneet Jeph, Quanjun Chen, Yasumasa Kobayashi, Xuan Song,
Shintaro Fukushima, and Toyotaro Suzumura. Spatio-temporal meta-graph learning for traffic forecasting.
InProceedings of the AAAI Conference on Artificial Intelligence, volume 37, pp. 8078–8086, 2023.
63

Preprint
Yunliang Jiang, Jinbin Fan, Yong Liu, and Xiongtao Zhang. Deep Graph Gaussian Processes for Short-Term
Traffic Flow Forecasting From Spatiotemporal Data.IEEE Transactions on Intelligent Transportation
Systems, 23(11):20177–20186, 2022.
Ming Jin, Huan Yee Koh, Qingsong Wen, Daniele Zambon, Cesare Alippi, Geoffrey I. Webb, Irwin King, and
Shirui Pan. A Survey on Graph Neural Networks for Time Series: Forecasting, Classification, Imputation,
and Anomaly Detection.IEEE Transactions on Pattern Analysis and Machine Intelligence, 46(12):10466–
10485, 2024.
Ming Jin, Yaxuan Kong, Yuxuan Liang, Chaoli Zhang, Siqiao Xue, Xue Wang, James Zhang, Yi Wang,
Haifeng Chen, Xiao-Li Li, et al. Large models for time series and spatio-temporal data: A survey and
outlook.ACM Computing Surveys, 58(14):1–38, 2026.
Harry Joe. Families of m-Variate Distributions with Given Margins and m(m-1)/2 Bivariate Dependence
Parameters.Lecture Notes-Monograph Series, 28:120–141, 1996.
Harry Joe, Haijun Li, and Aristidis K. Nikoloulopoulos. Tail dependence functions and vine copulas.Journal
of Multivariate Analysis, 101(1):252–270, 2010.
S. R. Johnson, S. E. Heaps, K. J. Wilson, and D. J. Wilkinson. A Bayesian spatio-temporal model for
short-term forecasting of precipitation fields.Environmetrics, 34(8):e2824, 2023.
Galin L. Jones and Qian Qin. Markov Chain Monte Carlo in Practice.Annual Review of Statistics and Its
Application, 9:557–578, 2022.
Thomas Jung and Martin Leutbecher. Scale-dependent verification of ensemble forecasts.Quarterly Journal
of the Royal Meteorological Society, 134(633):973–984, 2008.
R. E. Kalman. A new approach to linear filtering and prediction problems.Journal of Basic Engineering,
82(1):35–45, 03 1960.
Hamed Karami, Javier Redondo Anton, Geunsoo Jang, K Selcuk Candan, and Gerardo Chowell. Adap-
tive COVID-19 Trajectory Forecasting Using MAB-Inspired Ensemble Weighting.arXiv preprint
arXiv:2606.18575, 2026a.
Hamed Karami, Ruiyan Luo, Pejman Sanaei, and Gerardo Chowell. Comparative study of Bayesian and
frequentist methods for epidemic forecasting: Insights from simulated and historical data.Statistical
Methods in Medical Research, 35(1):21–39, 2026b.
Tero Karras, Miika Aittala, Timo Aila, and Samuli Laine. Elucidating the Design Space of Diffusion-Based
Generative Models.Advances in Neural Information Processing Systems, 35:26565–26577, 2022.
Benita Katarina and Gunardi. Optimization of Bayesian Structural Time Series (BSTS) Applications in
Forecasting Stock Prices Through State Components Selection. InProceedings of the 8th International
Conference on the Applications of Science and Mathematics, pp. 229–248. Springer Nature Singapore,
2023.
Devinder Kaur, Rahul Kumar, Neeraj Kumar, and Mohsen Guizani. Smart grid energy management using
rnn-lstm: A deep learning-based approach. In2019 IEEE global communications conference (GLOBE-
COM), pp. 1–6. IEEE, 2019.
Devinder Kaur, Shama Naz Islam, Md Apel Mahmud, Md Enamul Haque, and Zhao Yang Dong. Energy
forecasting in smart grid systems: recent advancements in probabilistic deep learning.IET Generation,
Transmission & Distribution, 16(22):4461–4479, 2022.
Jongwook Kim and Jong-Min Kim. TSCoNet: A Two-Stage Copula CNN-LSTM for Uncertainty-Aware
Spatio-Temporal Forecasting.arXiv preprint arXiv:2607.10410, 2026.
64

Preprint
Younghun Kim, Giang V. Nguyen, Sungho Jung, and Linh Nguyen Van. Quantifying epistemic uncertainty
in deep learning models for quantitative precipitation forecasting using synthetic rainfall fields.Stochastic
Environmental Research and Risk Assessment, 40(6):136, May 2026.
Diederik P Kingma and Max Welling. Auto-Encoding Variational Bayes. In2nd International Conference
on Learning Representations, ICLR, 2014.
Diederik P. Kingma and Max Welling. An Introduction to Variational Autoencoders.Foundations and
Trends in Machine Learning, 12(4):307–392, November 2019.
Thomas N. Kipf and Max Welling. Semi-Supervised Classification with Graph Convolutional Networks. In
International Conference on Learning Representations, 2017.
Thomas Kneib, Alexander Silbersdorff, and Benjamin Säfken. Rage against the mean – a review of distri-
butional regression approaches.Econometrics and Statistics, 26:99–123, 2023.
Roger Koenker.Quantile Regression. Cambridge University Press, 2005.
Roger Koenker and Gilbert Bassett. Regression Quantiles.Econometrica, 46(1):33–50, 1978.
Alex J. Koning, Philip Hans Franses, Michèle Hibon, and H.O. Stekler. The M3 competition: Statistical
tests of the results.International Journal of Forecasting, 21(3):397–409, 2005.
Siva Rama Krishna Kottapalli, Karthik Hubli, Sandeep Chandrashekhara, Garima Jain, Sunayana Hubli,
Gayathri Botla, and Ramesh Doddaiah. Foundation models for time series: A survey.arXiv preprint
arXiv:2504.04011, 2025.
Batuhan Koyuncu, Tim Nico Bauerschmidt, and Isabel Valera. E-ProTran: Efficient Probabilistic Trans-
formers for Forecasting. InICML 2024 Workshop on Structured Probabilistic Inference & Generative
Modeling, 2024.
Basil Kraft, Steven Stalder, William H. Aeberhard, Nicolás Harrington Ruiz, Nicolai Meinshausen, Xinwei
Shen, and Lukas Gudmundsson. Modeling Uncertainty With Engression: A Deep Generative Time-Series
Approach.Geophysical Research Letters, 53(2), 2026.
Christopher Krapu and Mark Borsuk. Probabilistic programming: A review for environmental modellers.
Environmental Modelling & Software, 114:40–48, 2019.
Hans R. Kunsch. The Jackknife and the Bootstrap for General Stationary Observations.The Annals of
Statistics, 17(3):1217 – 1241, 1989.
Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. Simple and Scalable Predictive Un-
certainty Estimation using Deep Ensembles.Advances in Neural Information Processing Systems, 30,
2017.
Amanda Lenzi and Marc Genton. Spatiotemporal probabilistic wind vector forecasting over Saudi Arabia.
The Annals of Applied Statistics, 14, 10 2020.
Radmir Mishelevich Leushuis. Probabilistic forecasting with VAR-VAE: Advancing time series forecasting
under uncertainty.Information Sciences, 713:122184, 2025.
Binghui Li and Jie Zhang. A review on the integration of probabilistic solar forecasting in power systems.
Solar Energy, 210:68–86, 2020. Special Issue on Grid Integration.
Jiachen Li, Fan Yang, Masayoshi Tomizuka, and Chiho Choi. Evolvegraph: Multi-agent trajectory prediction
with dynamic relational reasoning. InAdvances in Neural Information Processing Systems (NeurIPS),
2020.
Jinglin Li, Jun Tan, QI Fang, and Ning Gui. Parametric Prior Mapping Framework for Non-stationary
Probabilistic Time Series Forecasting. InForty-third International Conference on Machine Learning,
2026a.
65

Preprint
Sirui Li, Shuhan Xiao, Mihir Joshi, Ahmed Metwally, Daniel McDuff, Wei Wang, and Yuzhe Yang. HEARTS:
Benchmarking LLM Reasoning on Health Time Series. InForty-third International Conference on Machine
Learning, 2026b.
Xilong Li, Feng Zheng, Jianjian Zhao, Cheng Tang, Lingfeng Zhou, Ziwen Liu, and Zhenghua Chen. Uncer-
tainty interval assessment method for joint output of renewable power stations considering time-varying
volatility correlations.Sustainable Energy, Grids and Networks, 45:102157, 2026c.
Yaguang Li, Rose Yu, Cyrus Shahabi, and Yan Liu. Diffusion Convolutional Recurrent Neural Network:
Data-Driven Traffic Forecasting. InInternational Conference on Learning Representations, 2018.
Yan Li, Xinjiang Lu, Yaqing Wang, and Dejing Dou. Generative Time Series Forecasting with Diffusion,
Denoise, and Disentanglement.Advances in Neural Information Processing Systems, 35:23009–23022,
2022.
Yuxin Li, Wenchao Chen, Xinyue Hu, Bo Chen, Baolin Sun, and Mingyuan Zhou. Transformer-Modulated
Diffusion Models for Probabilistic Multivariate Time Series Forecasting. InThe Twelfth International
Conference on Learning Representations, 2024.
Zhonghang Li, Long Xia, Lei Shi, Yong Xu, Dawei Yin, and Chao Huang. Open Spatio-Temporal Foundation
Models for Traffic Prediction.ACM Transactions on Intelligent Systems and Technology, 2025.
Yuxuan Liang, Haomin Wen, Yuqi Nie, Yushan Jiang, Ming Jin, Dongjin Song, Shirui Pan, and Qingsong
Wen. Foundation models for time series analysis: A tutorial and survey. InProceedings of the 30th ACM
SIGKDD conference on knowledge discovery and data mining, pp. 6555–6565, 2024.
Bryan Lim and Stefan Zohren. Time-series forecasting with deep learning: a survey.Philosophical Trans-
actions of the Royal Society A: Mathematical, Physical and Engineering Sciences, 379(2194):20200209, 02
2021.
Pedro A Lima, Carlos M Carvalho, Hedibert F Lopes, and Andrew Herren. Minnesota BART.arXiv preprint
arXiv:2503.13759, 2025.
Jihao Andreas Lin, Sebastian Ament, Maximilian Balandat, David Eriksson, José Miguel Hernández-Lobato,
and Eytan Bakshy. Scalable Gaussian Processes with Latent Kronecker Structure. InProceedings of the
42nd International Conference on Machine Learning, volume 267 ofProceedings of Machine Learning
Research, pp. 37730–37744. PMLR, 2025a.
Lequan Lin, Dai Shi, Andi Han, and Junbin Gao. SpecSTG: A Fast Spectral Diffusion Framework for
Probabilistic Spatio-Temporal Traffic Forecasting. In2025 International Joint Conference on Neural
Networks, pp. 1–10, 2025b.
Finn Lindgren and Håvard Rue. Bayesian Spatial Modelling with R-INLA.Journal of Statistical Software,
63:1–25, 2015.
Finn Lindgren, Håvard Rue, and Johan Lindström. An explicit link between Gaussian fields and Gaus-
sian Markov random fields: The stochastic partial differential equation approach.Journal of the Royal
Statistical Society: Series B: Statistical Methodology, 73(4):423–498, 2011.
Jiawei Liu, Cheng Yang, Zhiyuan Lu, Junze Chen, Yibo Li, Mengmei Zhang, Ting Bai, Yuan Fang, Lichao
Sun, Philip S Yu, et al. Graph Foundation Models: Concepts, Opportunities and Challenges.IEEE
Transactions on Pattern Analysis and Machine Intelligence, 47(6):5023–5044, 2025a.
Siqi Liu and Milos Hauskrecht. Event Outlier Detection in Continuous Time. InInternational Conference
on Machine Learning, pp. 6793–6803. PMLR, 2021.
Xiang Liu, Boyi Lei, Hongtai Yang, Ke Han, and Lee D. Han. Modeling and Predicting the Spatiotempo-
ral Dynamics of Construction Waste Hauling Trucks Using an Input–Output Hidden Markov Approach.
Journal of Advanced Transportation, 2026(1):8896444, 2026.
66

Preprint
Xinhe Liu and Wenmin Wang. Deep Time Series Forecasting Models: A Comprehensive Survey.Mathemat-
ics, 12(10), 2024.
Xu Liu, Yutong Xia, Yuxuan Liang, Junfeng Hu, Yiwei Wang, Lei Bai, Chao Huang, Zhenguang Liu,
Bryan Hooi, and Roger Zimmermann. LargeST: A Benchmark Dataset for Large-Scale Traffic Forecasting.
Advances in Neural Information Processing Systems, 36:75354–75371, 2023.
Xu Liu, Juncheng Liu, Gerald Woo, Taha Aksu, Yuxuan Liang, Roger Zimmermann, Chenghao Liu, Silvio
Savarese, Caiming Xiong, and Doyen Sahoo. Moirai-MoE: Empowering Time Series Foundation Models
with Sparse Mixture of Experts.arXiv preprint arXiv:2410.10469, 2024.
Xueqing Liu, Nina Deliu, Tanujit Chakraborty, Lauren Bell, and Bibhas Chakraborty. Thompson sampling
for zero-inflated count outcomes with an application to the Drink Less mobile health study.The Annals
of Applied Statistics, 19(2):1403 – 1425, 2025b.
Yong Liu, Guo Qin, Xiangdong Huang, Jianmin Wang, and Mingsheng Long. Timer-xl: Long-context
transformers for unified time series forecasting. InInternational Conference on Learning Representations,
volume 2025, pp. 83982–84006, 2025c.
Yong Liu, Guo Qin, Zhiyuan Shi, Zhi Chen, Caiyin Yang, Xiangdong Huang, Jianmin Wang, and Mingsheng
Long. Sundial: A Family of Highly Capable Time Series Foundation Models. InForty-second International
Conference on Machine Learning, 2025d.
Yongqi Liu, Hui Qin, Zhendong Zhang, Shaoqian Pei, Zhiqiang Jiang, Zhongkai Feng, and Jianzhong Zhou.
Probabilistic spatiotemporal wind speed forecasting based on a variational Bayesian deep learning model.
Applied Energy, 260:114259, 2020.
Ziming Liu, Yixuan Wang, Sachin Vaidya, Fabian Ruehle, James Halverson, Marin Soljacic, Thomas Hou,
and Max Tegmark. KAN: Kolmogorov–Arnold Networks. InInternational Conference on Learning Rep-
resentations, pp. 70367–70413, 2025e.
Francisco Louzada, Carlos Alberto Ribeiro Diniz, Oluwafunmilayo Adenike Dawodu, and Osafu Augustine
Egbon. Bayesian spatio-temporal modelling: A systematic review.Research in Statistics, 3(1):2568891,
2025.
Joshua Lovegrove and Stefan Siegert.Improving Numerical Weather Forecasts by Bayesian Hierarchical
Modelling, pp. 193–218. Springer International Publishing, Cham, 2023.
Kai Lv, Liang Yuan, and Xiaoyu Ni. Learning Autoencoder Diffusion Models of Pedestrian Group Relation-
ships for Multimodal Trajectory Prediction.IEEE Transactions on Instrumentation and Measurement,
73:1–12, 2024.
Zhipeng Ma and Hong Fan. Influential factors of tuberculosis in mainland China based on MGWR model.
Plos one, 18(8):e0290978, 2023.
Blake MacDonald, Pritam Ranjan, and Hugh Chipman. GPfit: An R Package for Fitting a Gaussian Process
Model to Deterministic Simulator Outputs.Journal of Statistical Software, 64:1–23, 2015.
David J. C. MacKay.Information Theory, Inference and Learning Algorithms. Cambridge University Press,
Cambridge, UK, 2003.
Pegah Mahdavi, Mohammad Ali Ehsani, Daniel Felix Ahelegbey, and Mehrnaz Mohammadpour. Measuring
causal effect with ARDL-BART: A macroeconomic application.Applied Mathematics, 15(04):292–312,
2024.
Maria Mahfoud, Wim Bernasco, Sandjai Bhulai, and Rob van der Mei. Forecasting Spatio-Temporal Vari-
ation in Residential Burglary with the Integrated Laplace Approximation Framework: Effects of Crime
Generators, Street Networks, and Prior Crimes.Journal of Quantitative Criminology, 37(4):835–862,
December 2021.
67

Preprint
Tanwi Mallick, Jane Macfarlane, and Prasanna Balaprakash. Uncertainty Quantification for Traffic Fore-
casting Using Deep-Ensemble-Based Spatiotemporal Graph Neural Networks.IEEE Transactions on In-
telligent Transportation Systems, 25(8):9141–9152, 2024.
Valery Manokhin. Training-Free Probabilistic Time-Series Forecasting with Conformal Seasonal Pools.arXiv
preprint arXiv:2605.03789, 2026.
Roberto S. Mariano and Daniel Preve. Statistical tests for multiple forecast comparison.Journal of Econo-
metrics, 169(1):123–130, 2012.
Gianluca Mastrantonio, Giovanna Jona Lasinio, and Alan E Gelfand. Spatio-temporal circular models with
non-separable covariance structure.TEST, 25(2):331–350, 2016.
Alexander G de G Matthews, Mark Van Der Wilk, Tom Nickson, Keisuke Fujii, Alexis Boukouvalas, Pablo
León-Villagrá, Zoubin Ghahramani, and James Hensman. GPflow: A Gaussian Process Library using
TensorFlow.Journal of Machine Learning Research, 18(40):1–6, 2017.
Romit Maulik, Romain Egele, Krishnan Raghavan, and Prasanna Balaprakash. Quantifying uncertainty
for deep learning based forecasting and flow-reconstruction using neural architecture search ensembles.
Physica D: Nonlinear Phenomena, 454:133852, 2023.
Patrick L. McDermott and Christopher K. Wikle. An ensemble quadratic echo state network for non-linear
spatio-temporal forecasting.Stat, 6(1):315–330, 2017.
Patrick L. McDermott and Christopher K. Wikle. Deep echo state networks with uncertainty quantification
for spatio-temporal forecasting.Environmetrics, 30(3):e2553, 2019a.
PatrickL.McDermottandChristopherK.Wikle. BayesianRecurrentNeuralNetworkModelsforForecasting
and Quantifying Uncertainty in Spatial-Temporal Data.Entropy, 21(2), 2019b.
Nicolai Meinshausen. Quantile regression forests.Journal of Machine Learning Research, 7(6), 2006.
Julian Merder, Robert A. Rigby, Andreas Mayr, Gillian Heller, Thomas Kneib, Nikolaus Umlauf, Fernanda
De Bastiani, Reto Stauffer, Jonathan Tonkin, Nikos Logothetis, Achim Zeileis, and Mikis Stasinopoulos.
Distributional regression using generalized additive models for location, scale and shape.Nature Reviews
Methods Primers, 6:49, November 2026.
Pablo Montero-Manso and Rob J Hyndman. Principles and algorithms for forecasting groups of time series:
Locality and globality.International Journal of Forecasting, 37(4):1632–1653, 2021.
D.C. Montgomery.Introduction to Statistical Quality Control. Wiley, 2020.
Sang Jun Moon, Jong-June Jeon, Jason Sang Hun Lee, and Yongdai Kim. Learning Multiple Quantiles With
Neural Networks.Journal of Computational and Graphical Statistics, 30(4):1238–1248, 2021.
Pratik Nag, Ying Sun, and Brian J. Reich. Spatio-temporal DeepKriging for interpolation and probabilistic
forecasting.Spatial Statistics, 57:100773, 2023.
Radford M Neal.Bayesian Learning for Neural Networks. Lecture Notes in Statistics. Springer New York,
NY, New York, NY, 1 edition, 1996.
Roger B. Nelsen.An Introduction to Copulas. Springer Series in Statistics. Springer New York, NY, 2nd
edition, 2006.
Peter Bjorn Nemenyi.Distribution-Free Multiple Comparisons. Princeton University, 1963.
JakubNowotarskiandRafałWeron. Recentadvancesinelectricitypriceforecasting: Areviewofprobabilistic
forecasting.Renewable and Sustainable Energy Reviews, 81:1548–1568, 2018.
Anupiya Nugaliyadde, Upeka Somaratne, and Kok Wai Wong. Predicting electricity consumption using deep
recurrent neural networks.arXiv preprint arXiv:1909.08182, 2019.
68

Preprint
YongKyung Oh, Dongyoung Lim, and Sungil Kim. Stable Neural Stochastic Differential Equations in Ana-
lyzing Irregular Time Series Data. InInternational Conference on Learning Representations, volume 2024,
pp. 38231–38262, 2024.
Sean O’Hagan and Veronika Ročková. Generative regression with IQ-BART.arXiv preprint
arXiv:2507.04168, 2025.
Mitchell O’Hara-Wild, Rob Hyndman, and Earo Wang.fable: Forecasting Models for Tidy Time Series,
2026. URLhttps://fable.tidyverts.org. R package version 0.5.0.
Joel Oskarsson, Tomas Landelius, Marc Peter Deisenroth, and Fredrik Lindsten. Probabilistic Weather
Forecasting with Hierarchical Graph Neural Networks. InThe Thirty-eighth Annual Conference on Neural
Information Processing Systems, 2024.
Lorenzo Pacchiardi, Rilwan A. Adewoyin, Peter Dueben, and Ritabrata Dutta. Probabilistic Forecasting
with Generative Networks via Scoring Rule Minimization.Journal of Machine Learning Research, 25(45):
1–64, 2024.
Soumyasundar Pal, Liheng Ma, Yingxue Zhang, and Mark Coates. RNN with Particle Flow for Probabilistic
Spatio-temporal Forecasting. InProceedings of the 38th International Conference on Machine Learning,
volume 139 ofProceedings of Machine Learning Research, pp. 8336–8348. PMLR, 2021.
Madhurima Panja, Tanujit Chakraborty, Uttam Kumar, and Nan Liu. Epicasting: An Ensemble Wavelet
Neural Network for forecasting epidemics.Neural Networks, 165:185–212, 2023.
Madhurima Panja, Dhiman Das, Tanujit Chakraborty, Arnob Ray, R. Athulya, Chittaranjan Hens, Sya-
mal K. Dana, Nuncio Murukesh, and Dibakar Ghosh. Forecasting precipitation in the arctic using prob-
abilistic machine learning informed by causal climate drivers.Chaos: An Interdisciplinary Journal of
Nonlinear Science, 35(11):113108, 11 2025.
Madhurima Panja, Tanujit Chakraborty, Anubhab Biswas, and Soudeep Deb. E-STGCN: extreme spatio-
temporal graph convolutional networks for air quality forecasting.Journal of the Royal Statistical Society
Series A: Statistics in Society, pp. qnag010, 02 2026a.
Madhurima Panja, Danny D’Agostino, Huitao Li, Tanujit Chakraborty, and Nan Liu. EpiCastBench:
Datasets and Benchmarks for Multivariate Epidemic Forecasting.arXiv preprint arXiv:2605.11598, 2026b.
Georgia Papacharalampous and Hristos Tyralis. A review of machine learning concepts and methods for
addressing challenges in probabilistic hydrological post-processing and forecasting.Frontiers in Water, 4,
2022.
Harris Papadopoulos, Kostas Proedrou, Volodya Vovk, and Alexander Gammerman. Inductive Confidence
Machines for Regression. InProceedings of the 13th European Conference on Machine Learning, ECML
’02, pp. 345–356, Berlin, Heidelberg, 2002. Springer-Verlag.
GeorgePapamakarios, TheoPavlakou, andIainMurray. MaskedAutoregressiveFlowforDensityEstimation.
InAdvances in Neural Information Processing Systems, volume 30, 2017.
George Papamakarios, Eric Nalisnick, Danilo Jimenez Rezende, Shakir Mohamed, and Balaji Lakshmi-
narayanan. Normalizing Flows for Probabilistic Modeling and Inference.Journal of Machine Learning
Research, 22(57):1–64, 2021.
Olivier C. Pasche and Sebastian Engelke. Neural networks for extreme quantile regression with an application
to forecasting of flood risk.The Annals of Applied Statistics, 18(4):2818 – 2839, 2024.
Rajdeep Pathak and Tanujit Chakraborty. Deep Generative Spatiotemporal Engression for Probabilistic
Forecasting of Epidemics.Transactions on Machine Learning Research, 2026.
69

Preprint
Rajdeep Pathak, Rahul Goswami, Madhurima Panja, Palash Ghosh, and Tanujit Chakraborty. Deep
Generative Transformers for Probabilistic Time Series and Spatiotemporal Forecasting.arXiv preprint
arXiv:2603.11909v2, 2026a.
Rajdeep Pathak, Archi Roy, and Tanujit Chakraborty. ANGLE: Angular Neural Generative Learning via
Engression.arXiv preprint arXiv:2607.12833, 2026b.
Tim Pearce, Alexandra Brintrup, Mohamed Zaki, and Andy Neely. High-Quality Prediction Intervals for
Deep Learning: A Distribution-Free, Ensembled Approach. InProceedings of the 35th International
Conference on Machine Learning, pp. 4075–4084. PMLR, 2018.
Du Phan, Neeraj Pradhan, and Martin Jankowiak. Composable effects for flexible and accelerated proba-
bilistic programming in NumPyro.arXiv preprint arXiv:1912.11554, 2019.
Ilan Price, Alvaro Sanchez-Gonzalez, Ferran Alet, Tom R. Andersson, Andrew El-Kadi, Dominic Masters,
Timo Ewalds, Jacklynn Stott, Shakir Mohamed, Peter Battaglia, Remi Lam, and Matthew Willson.
GenCast: Diffusion-based ensemble forecasting for medium-range weather.Nature, 637:84–90, 2025.
Sergey Prokudin, Peter Gehler, and Sebastian Nowozin. Deep directional statistics: Pose estimation with
uncertainty quantification. InEuropean Conference on Computer Vision, pp. 542–559. Springer, 2018.
JanPrüser. ForecastingwithmanypredictorsusingBayesianadditiveregressiontrees.Journal of Forecasting,
38(7):621–631, 2019.
Yifeng Qin, Caihua Yang, Hao Wu, Changkun Xie, Afshin Afshari, Veselin Krustev, Shengbing He, and
Shengquan Che. Optimization of CMIP6 Precipitation Projection Based on Bayesian Model Averaging
Approach and Future Urban Precipitation Risk Assessment: A Case Study of Shanghai.Urban Science,
9(9), 2025.
Jinwen Qiu, S. Rao Jammalamadaka, and Ning Ning. Multivariate bayesian structural time series model.
Journal of Machine Learning Research, 19(68):1–33, 2018.
Adrian E. Raftery, Tilmann Gneiting, Fadoua Balabdaoui, and Michael Polakowski. Using Bayesian Model
Averaging to Calibrate Forecast Ensembles.Monthly Weather Review, 133(5):1155 – 1174, 2005.
Ali Rahimifard and Mohammadreza Sharifi Ghazvini. Adjusting the Project Schedule by Pre-Control Chart.
Annals of Optimization With Applications, 1(2):66–77, May 2020.
Syama Sundar Rangapuram, Jan Gasthaus, Lorenzo Stella, Valentin Flunkert, David Salinas, Yuyang Wang,
and Tim Januschowski. Deep Non-Parametric Time Series Forecaster.arXiv preprint arXiv:2312.14657,
2023.
Carl Edward Rasmussen.Gaussian Processes in Machine Learning, pp. 63–71. Springer Berlin Heidelberg,
Berlin, Heidelberg, 2004.
Kashif Rasul, Calvin Seward, Ingmar Schuster, and Roland Vollgraf. Autoregressive Denoising Diffusion
Models for Multivariate Probabilistic Time Series Forecasting. InProceedings of the 38th International
Conference on Machine Learning, volume139ofProceedings of Machine Learning Research, pp.8857–8868.
PMLR, 2021a.
Kashif Rasul, Abdul-Saboor Sheikh, Ingmar Schuster, Urs M Bergmann, and Roland Vollgraf. Multivariate
Probabilistic Time Series Forecasting via Conditioned Normalizing Flows. InInternational Conference on
Learning Representations, 2021b.
Kashif Rasul, Arjun Ashok, Andrew Robert Williams, Hena Ghonia, Rishika Bhagwatkar, Arian Kho-
rasani, Mohammad Javad Darvishi Bayazi, George Adamopoulos, Roland Riachi, Nadhir Hassen, et al.
Lag-Llama: Towards Foundation Models for Probabilistic Time Series Forecasting.arXiv preprint
arXiv:2310.08278, 2023.
70

Preprint
Yinuo Ren, Feng Li, Yanfei Kang, and Jue Wang. Infinite forecast combinations based on Dirichlet process.
In2023 IEEE International Conference on Data Mining Workshops (ICDMW), pp. 579–587. IEEE, 2023.
Danilo Rezende and Shakir Mohamed. Variational Inference with Normalizing Flows. InProceedings of
the 32nd International Conference on Machine Learning, volume 37 ofProceedings of Machine Learning
Research, pp. 1530–1538. PMLR, 2015.
Danilo Jimenez Rezende, Shakir Mohamed, and Daan Wierstra. Stochastic Backpropagation and Approxi-
mateInferenceinDeepGenerative Models. InProceedings of the 31st International Conference on Machine
Learning, volume 32 ofProceedings of Machine Learning Research, pp. 1278–1286. PMLR, 2014.
Yaniv Romano, Evan Patterson, and Emmanuel Candes. Conformalized Quantile Regression. InAdvances
in Neural Information Processing Systems, volume 32, 2019.
Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution
image synthesis with latent diffusion models. InProceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pp. 10684–10695, 2022.
Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-Net: Convolutional Networks for Biomedical
Image Segmentation. InInternational Conference on Medical Image Computing and Computer-Assisted
Intervention, pp. 234–241. Springer, 2015.
Olivier Roustant, David Ginsbourger, and Yves Deville. DiceKriging, DiceOptim: Two R Packages for
the Analysis of Computer Experiments by Kriging-Based Metamodeling and Optimization.Journal of
Statistical Software, 51:1–55, 2012.
Benedek Rozemberczki, Paul Scherer, Yixuan He, George Panagopoulos, Alexander Riedel, Maria Aste-
fanoaei, Oliver Kiss, Ferenc Beres, Guzman Lopez, Nicolas Collignon, et al. PyTorch Geometric Temporal:
Spatiotemporal Signal Processing with Neural Machine Learning Models. InProceedings of the 30th ACM
International Conference on Information & Knowledge Management, pp. 4564–4573, 2021a.
Benedek Rozemberczki, Paul Scherer, Oliver Kiss, Rik Sarkar, and Tamas Ferenci. Chickenpox Cases in
Hungary: a Benchmark Dataset for Spatiotemporal Signal Processing with Graph Neural Networks.arXiv
preprint arXiv:2102.08100, 2021b.
Håvard Rue and Leonhard Held.Gaussian Markov Random Fields: Theory and Applications. Chapman and
Hall/CRC, 1st edition, 2005.
Håvard Rue, Sara Martino, and Nicolas Chopin. Approximate Bayesian inference for latent Gaussian models
by using integrated nested Laplace approximations.Journal of the Royal Statistical Society: Series B:
Statistical Methodology, 71(2):319–392, 2009.
Christian Rupprecht, Iro Laina, Robert DiPietro, Maximilian Baust, Federico Tombari, Nassir Navab, and
Gregory D. Hager. Learning in an Uncertain World: Representing Ambiguity Through Multiple Hypothe-
ses. InIEEE International Conference on Computer Vision, pp. 3611–3620, 2017.
Feras Saad, Jacob Burnim, Colin Carroll, Brian Patton, Urs Köster, Rif A. Saurous, and Matthew Hoffman.
Scalable spatiotemporal prediction with Bayesian neural fields.Nature Communications, 15(1):7942, 2024.
Francisco Javier Sáez-Maldonado, Juan Maroñas, and Daniel Hernández-Lobato. An Analysis of Posterior
Collapse, Parameterization and Initialization in Variational Deep Gaussian Processes.arXiv preprint
arXiv:2606.25882, 2026.
Marko Ferdian Salim, Tri Baskoro Tunggul Satoto, and Danardono. Predicting spatio-temporal dynamics
of dengue using INLA (integrated nested laplace approximation) in Yogyakarta, Indonesia.BMC Public
Health, 25(1):1321, 2025.
David Salinas, Michael Bohlke-Schneider, Laurent Callot, Roberto Medico, and Jan Gasthaus. High-
dimensional multivariate forecasting with low-rank Gaussian copula processes.Advances in Neural In-
formation Processing Systems, 32, 2019.
71

Preprint
David Salinas, Valentin Flunkert, Jan Gasthaus, and Tim Januschowski. DeepAR: Probabilistic forecasting
with autoregressive recurrent networks.International Journal of Forecasting, 36(3):1181–1191, 2020.
Michael Scheuerer and Thomas M. Hamill. Variogram-Based Proper Scoring Rules for Probabilistic Forecasts
of Multivariate Quantities.Monthly Weather Review, 143(4):1321 – 1334, 2015.
Matteo Schoucair and Maarten van Reeuwijk. Nowcasting street-level NO2 concentrations using Gaussian
processes.Science of The Total Environment, 991:179717, 2025.
Steven L. Scott and Hal R. Varian. Predicting the present with Bayesian structural time series.International
Journal of Mathematical Modelling and Numerical Optimisation, 5:4–23, 2014.
Matthias W Seeger, David Salinas, and Valentin Flunkert. Bayesian Intermittent Demand Forecasting for
Large Inventories. InAdvances in Neural Information Processing Systems, volume 29, 2016.
Shovon Sengupta, Tanujit Chakraborty, and Sunny Kumar Singh. Forecasting CPI inflation under economic
policy and geopolitical uncertainties.International Journal of Forecasting, 41(3):953–981, 2025.
Cristián Serpell, Ignacio Araya, Carlos Valle, and Héctor Allende. Probabilistic Forecasting Using Monte
Carlo Dropout Neural Networks. InProgress in Pattern Recognition, Image Analysis, Computer Vision,
and Applications, pp. 387–397. Springer International Publishing, 2019.
Glenn Shafer and Vladimir Vovk. A Tutorial on Conformal Prediction.Journal of Machine Learning
Research, 9:371–421, June 2008.
Zezhi Shao, Fei Wang, Yongjun Xu, Wei Wei, Chengqing Yu, Zhao Zhang, Di Yao, Tao Sun, Guangyin Jin,
Xin Cao, et al. Exploring progress in multivariate time series forecasting: Comprehensive benchmarking
and heterogeneity analysis.IEEE Transactions on Knowledge and Data Engineering, 37(1):291–305, 2024.
Oleksandr Shchur, Abdul Fatir Ansari, Caner Turkmen, Lorenzo Stella, Nick Erickson, Pablo Guerron,
Michael Bohlke-Schneider, and Yuyang Wang. fev-bench: A Realistic Benchmark for Time Series Fore-
casting.arXiv preprint arXiv:2509.26468, 2025.
Lifeng Shen and James Kwok. Non-autoregressive Conditional Diffusion Models for Time Series Prediction.
InProceedings of the 40th International Conference on Machine Learning, volume 202 ofProceedings of
Machine Learning Research, pp. 31016–31029. PMLR, 2023.
Xinwei Shen and Nicolai Meinshausen. Engression: extrapolation through the lens of distributional regres-
sion.Journal of the Royal Statistical Society Series B: Statistical Methodology, 87(3):653–677, 07 2025.
Feng Shibo, Peilin Zhao, Liu Liu, Pengcheng Wu, and Zhiqi Shen. HDT: Hierarchical Discrete Transformer
for Multivariate Time Series Forecasting. InProceedings of the AAAI Conference on Artificial Intelligence,
volume 39, pp. 746–754, 2025.
Hiroshi Shiraishi, Tomoshige Nakamura, and Ryotato Shibuki. Time series quantile regression using random
forests.Journal of Time Series Analysis, 45(4):639–659, 2024.
LeonidSigal, AlexandruOBalan, andMichaelJBlack. HumanEva: SynchronizedVideoandMotionCapture
Dataset and Baseline Algorithm for Evaluation of Articulated Human Motion.International Journal of
Computer Vision, 87(1):4–27, 2010.
Abe Sklar. Fonctions de répartition à n dimensions et leurs marges.Publications de l’Institut de Statistique
de l’Université de Paris, 8:229–231, 1959.
J. Mc Lean Sloughter, Adrian E. Raftery, Tilmann Gneiting, and Chris Fraley. Probabilistic Quantitative
Precipitation Forecasting Using Bayesian Model Averaging.Monthly Weather Review, 135(9), 2007.
J. McLean Sloughter, Tilmann Gneiting, and Adrian E. Raftery. Probabilistic Wind Speed Forecasting
Using Ensembles and Bayesian Model Averaging.Journal of the American Statistical Association, 105
(489):25–35, 2010.
72

Preprint
Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli. Deep Unsupervised Learning
using Nonequilibrium Thermodynamics. InProceedings of the 32nd International Conference on Machine
Learning, volume 37 ofProceedings of Machine Learning Research, pp. 2256–2265. PMLR, 2015.
Chao Song, Youfang Lin, Shengnan Guo, and Huaiyu Wan. Spatial-temporal synchronous graph convolu-
tional networks: A new framework for spatial-temporal network data forecasting. InProceedings of the
AAAI Conference on Artificial Intelligence, volume 34, pp. 914–921, 2020.
Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole.
Score-Based Generative Modeling through Stochastic Differential Equations. InInternational Conference
on Learning Representations, 2021.
Kamile Stankeviciute, Ahmed M Alaa, and Mihaela Van der Schaar. Conformal Time-series Forecasting.
Advances in Neural Information Processing Systems, 34:6216–6228, 2021.
Aike Steentoft, Bu-Sung Lee, and Markus Schäpfer. Quantifying the uncertainty of mobility flow predictions
using Gaussian processes.Transportation, 51(6):2301–2322, 2024.
Ingo Steinwart and Andreas Christmann. Estimating conditional quantiles with the help of the pinball loss.
Bernoulli, 17(1):211 – 225, 2011.
Olivera Stojanović, Johannes Leugering, Gordon Pipa, Stéphane Ghozzi, and Alexander Ullrich. A Bayesian
Monte Carlo approach for predicting the spread of infectious diseases.PLOS ONE, 14(12):1–20, 12 2019.
Ayako Sumi and Nobumichi Kobayashi. Time-series analysis of geographically specific monthly number of
newly registered cases of active tuberculosis in japan.PLoS One, 14(3):e0213856, 2019.
Sophia Huiwen Sun and Rose Yu. Copula Conformal prediction for multi-step time series prediction. InThe
Twelfth International Conference on Learning Representations, 2024.
E. G. Tabak and Cristina V. Turner. A Family of Nonparametric Density Estimation Algorithms.Commu-
nications on Pure and Applied Mathematics, 66(2):145–164, 2013.
Qitai Tan, Yiyun Chen, Mo Li, Ruiwen Gu, Yilin Su, and Xiao-Ping Zhang. SynTSBench: Rethinking Tem-
poral Pattern Learning in Deep Learning Models for Time Series. InThe Thirty-ninth Annual Conference
on Neural Information Processing Systems Datasets and Benchmarks Track, 2025.
Binh Tang and David S. Matteson. Probabilistic Transformer For Time Series Analysis. InAdvances in
Neural Information Processing Systems, 2021.
Yingjuan Tang, Hongwen He, Yong Wang, and Yifan Wu. Using a Diffusion Model for Pedestrian Trajectory
Prediction in Semi-Open Autonomous Driving Environments.IEEE Sensors Journal, 24(10):17208–17218,
2024.
Vianney Taquet, Vincent Blot, Thomas Morzadec, Louis Lacombe, and Nicolas Brunel. MAPIE: an open-
source library for distribution-free uncertainty quantification.arXiv preprint arXiv:2207.12274, 2022.
Yee Whye Teh, Michael I Jordan, Matthew J Beal, and David M Blei. Hierarchical Dirichlet Processes.
Journal of the American Statistical Association, 101(476):1566–1581, 2006.
Burcu Tezcan and Margaret Garcia. Training a hidden Markov model with PMDI and temperature to create
climate informed scenarios.Frontiers in Water, 7, 2025.
Thordis L. Thorarinsdottir and Tilmann Gneiting. Probabilistic Forecasts of Wind Speed: Ensemble Model
Output Statistics by using Heteroscedastic Censored Regression.Journal of the Royal Statistical Society
Series A: Statistics in Society, 173(2):371–388, 04 2010.
A. V. Vecchia. Estimation and Model Identification for Continuous Spatial Processes.Journal of the Royal
Statistical Society. Series B: Statistical Methodology, 50(2):297–312, 1988.
73

Preprint
Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Liò, and Yoshua Bengio.
Graph Attention Networks. InInternational Conference on Learning Representations, 2018.
Vladimir Vovk, Alex Gammerman, and Glenn Shafer.Algorithmic Learning in a Random World. Springer,
New York, 2005.
Can Wan, Jin Lin, Jianhui Wang, Yonghua Song, and Zhao Yang Dong. Direct Quantile Regression for Non-
parametric Probabilistic Forecasting of Wind Power Generation.IEEE Transactions on Power Systems,
32(4):2767–2778, 2017.
Guancheng Wan, Zewen Liu, Xiaojun Shan, Max SY Lau, B Aditya Prakash, and Wei Jin. EARTH:
Epidemiology-Aware Neural ODE with Continuous Disease Transmission Graph. InForty-second Inter-
national Conference on Machine Learning, 2025.
Bin Wang, Tianrui Li, Zheng Yan, Guangquan Zhang, and Jie Lu. DeepPIPE: A distribution-free uncertainty
quantification approach for time series forecasting.Neurocomputing, 397:11–19, 2020a.
Guanghu Wang, Yan Zhou, Yan Yan, Zhihan Zhou, Zikang Yang, Litao Dai, and Junpeng Huang. Proba-
bilistic Photovoltaic Power Forecasting with Reliable Uncertainty Quantification via Multi-Scale Tempo-
ral–Spatial Attention and Conformalized Quantile Regression.Sustainability, 18(2), 2026a.
Senzhang Wang, Jiannong Cao, and Philip S. Yu. Deep Learning for Spatio-Temporal Data Mining: A
Survey.IEEE Transactions on Knowledge and Data Engineering, 34(8):3681–3700, 2022.
Yang Wang, Haiyun Wang, and Qianyu Ma. Physics-informed dynamic wake graphs for probabilistic wind-
farm power forecasting.Electric Power Systems Research, 259:113241, 2026b.
Yaohui Wang, Piotr Bilinski, Francois Bremond, and Antitza Dantcheva. ImaGINator: Conditional Spatio-
Temporal GAN for Video Generation. In2020 IEEE Winter Conference on Applications of Computer
Vision, pp. 1149–1158, 2020b.
Zehong Wang, Zheyuan Liu, Tianyi Ma, Jiazheng Li, Zheyuan Zhang, Xingbo Fu, Yiyang Li, Zhengqing
Yuan, Wei Song, Yijun Ma, et al. Graph Foundation Models: A Comprehensive Survey.arXiv preprint
arXiv:2505.15116, 2025a.
Zepu Wang, Xiaobo Ma, Huajie Yang, Weimin Lyu, Yang Liu, Peng Sun, and Sharath Chandra Guntuku.
Uncertainty-Aware Crime Prediction With Spatial Temporal Multivariate Graph Neural Networks. In
IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 1–5, 2025b.
Zhenghong Wang, Yi Wang, Furong Jia, Fan Zhang, Nikita Klimenko, Leye Wang, Zhengbing He, Zhou
Huang, and Yu Liu. Spatiotemporal Fusion Transformer for large-scale traffic forecasting.Information
Fusion, 107:102293, 2024.
Haomin Wen, Youfang Lin, Yutong Xia, Huaiyu Wan, Qingsong Wen, Roger Zimmermann, and Yuxuan
Liang. DiffSTG: Probabilistic Spatio-Temporal Graph Forecasting with Denoising Diffusion Models. In
Proceedings of the 31st ACM International Conference on Advances in Geographic Information Systems.
Association for Computing Machinery, 2023.
Ruofeng Wen, Kari Torkkola, Balakrishnan Narayanaswamy, and Dhruv Madeka. A Multi-Horizon Quantile
Recurrent Forecaster.arXiv preprint arXiv:1711.11053, 2017.
Kristoffer Wickstrøm, Karl Øyvind Mikalsen, Michael Kampffmeyer, Arthur Revhaug, and Robert Jenssen.
Uncertainty-aware deep ensembles for reliable and explainable predictions of clinical time series.IEEE
Journal of Biomedical and Health Informatics, 25(7):2435–2444, 2021.
Christopher K Wikle and Andrew Zammit-Mangion. Statistical deep learning for spatial and spatiotemporal
data.Annual Review of Statistics and Its Application, 10(1):247–270, 2023.
74

Preprint
William Wilkinson, Arno Solin, and Vincent Adam. Sparse Algorithms for Markovian Gaussian Processes.
InProceedings of The 24th International Conference on Artificial Intelligence and Statistics, volume 130
ofProceedings of Machine Learning Research, pp. 1747–1755. PMLR, 2021.
Jared D Willard and Charuleka Varadharajan. Machine learning ensembles can enhance hydrologic predic-
tions and uncertainty quantification.Journal of Geophysical Research: Machine Learning and Computa-
tion, 2(3):e2025JH000732, 2025.
Christopher Williams and Carl Rasmussen. Gaussian processes for regression. InAdvances in Neural Infor-
mation Processing Systems, volume 8. MIT Press, 1995.
Tyler Wilson, Andrew McDonald, Asadullah Hill Galib, Pang-Ning Tan, and Lifeng Luo. Beyond Point
Prediction: Capturing Zero-Inflated & Heavy-Tailed Spatiotemporal Data with Deep Extreme Mixture
Models. InProceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
pp. 2020–2028, 2022.
R. L. Winkler, Javier Muñoz, José L. Cervera, José M. Bernardo, Gail Blattenberger, Joseph B. Kadane,
Dennis V. Lindley, Allan H. Murphy, Robert M. Oliver, and David Ríos-Insua. Scoring rules and the
evaluation of probabilities.Test, 5(1):1–60, 1996.
Gerald Woo, Chenghao Liu, Akshat Kumar, Caiming Xiong, Silvio Savarese, and Doyen Sahoo. Unified
Training of Universal Time Series Forecasting Transformers. InForty-first International Conference on
Machine Learning, 2024.
Xingjian Wu, Xiangfei Qiu, Hongfan Gao, Jilin Hu, Bin Yang, and Chenjuan Guo. K2VAE: A Koopman-
Kalman Enhanced Variational AutoEncoder for Probabilistic Time Series Forecasting. InForty-second
International Conference on Machine Learning, 2025.
Yuying Xie, Chaoshun Li, Mengying Li, Fangjie Liu, and Meruyert Taukenova. An overview of deterministic
and probabilistic forecasting methods of wind energy.iScience, 26(1):105804, 2023.
Chen Xu and Yao Xie. Conformal prediction interval for dynamic time-series. InInternational Conference
on Machine Learning, pp. 11559–11569. PMLR, 2021.
Xovee Xu, Ting Zhong, Fan Zhou, Rongfan Li, Goce Trajcevski, and Qinggang Meng. Learning Spatiotem-
poral Manifold Representation for Probabilistic Land Deformation Prediction.IEEE Transactions on
Cybernetics, 54(1):572–585, 2024.
Vijaya Krishna Yalavarthi, Randolf Scholz, Stefan Born, and Lars Schmidt-Thieme. Probabilistic Forecasting
of Irregularly Sampled Time Series with Missing Values via Conditional Normalizing Flows.Proceedings
of the AAAI Conference on Artificial Intelligence, 39(20):21877–21885, Apr. 2025.
Tijin Yan, Hongwei Zhang, Tong Zhou, Yufeng Zhan, and Yuanqing Xia. ScoreGrad: Multivariate Prob-
abilistic Time Series Forecasting with Continuous Energy-based Generative Models.arXiv preprint
arXiv:2106.10121, 2021.
Luoxiao Yang, Zhong Zheng, and Zijun Zhang. An Improved Mixture Density Network Via Wasserstein
Distance Based Adversarial Learning for Probabilistic Wind Speed Predictions.IEEE Transactions on
Sustainable Energy, 13(2):755–766, 2022.
Yiyuan Yang, Ming Jin, Haomin Wen, Chaoli Zhang, Yuxuan Liang, Lintao Ma, Yi Wang, Chenghao Liu,
Bin Yang, Zenglin Xu, Shirui Pan, and Qingsong Wen. A Survey on Diffusion Models for Time Series and
Spatio-Temporal Data.ACM Computing Surveys, 58(8), February 2026.
Weiwei Ye, Zhuopeng Xu, and Ning Gui. Non-stationary diffusion for probabilistic time series forecasting.
InProceedings of the 42nd International Conference on Machine Learning, 2025.
Bing Yu, Haoteng Yin, and Zhanxing Zhu. Spatio-temporal graph convolutional networks: a deep learning
framework for traffic forecasting. InProceedings of the 27th International Joint Conference on Artificial
Intelligence, pp. 3634–3640, 2018.
75

Preprint
Junfeng Yu, Xiaodong Li, Lei Yang, Linze Li, Zhichao Huang, Keyan Shen, Xu Yang, Xu Yang, Zhikang
Xu, Dongying Zhang, and Shuai Du. Deep learning models for pv power forecasting: Review.Energies,
17(16), 2024.
Yixiao Yu, Xueshan Han, Ming Yang, and Jiajun Yang. Probabilistic Prediction of Regional Wind Power
Based on Spatiotemporal Quantile Regression. In2019 IEEE Industry Applications Society Annual Meet-
ing, pp. 1–16, 2019.
Haitao Yuan and Guoliang Li. A Survey of Traffic Prediction: from Spatio-Temporal Data to Intelligent
Transportation.Data Science and Engineering, 6:63–85, 03 2021.
Margaux Zaffran, Olivier Féron, Yannig Goude, Julie Josse, and Aymeric Dieuleveut. Adaptive Conformal
Predictions for Time Series. InInternational Conference on Machine Learning, pp. 25834–25866. PMLR,
2022.
Daniele Zambon and Cesare Alippi. AZ-whiteness test: A test for signal uncorrelation on spatio-temporal
graphs. InAdvances in Neural Information Processing Systems, volume 35, pp. 11975–11986, 2022.
Mohsen Zand, Ali Etemad, and Michael Greenspan. Flow-Based Spatio-Temporal Structured Prediction of
Motion Dynamics.IEEE Transactions on Pattern Analysis and Machine Intelligence, 45(11):13523–13535,
2023.
Douglas Zechin and Helena Beatriz Bettella Cybis. Probabilistic traffic breakdown forecasting through
Bayesian approximation using variational LSTMs.Transportmetrica B: Transport Dynamics, 11(1):1026–
1044, 2023.
Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu. Are transformers effective for time series forecasting?
InProceedings of the AAAI Conference on Artificial Intelligence, volume 37, pp. 11121–11128, 2023.
Guoqiang Zhang, B. Eddy Patuwo, and Michael Y. Hu. Forecasting with artificial neural networks:: The
state of the art.International Journal of Forecasting, 14(1):35–62, 1998.
Hao Zhang, Yongqian Liu, Jie Yan, Shuang Han, Li Li, and Quan Long. Improved Deep Mixture Density
Network for Regional Wind Power Probabilistic Forecasting.IEEE Transactions on Power Systems, 35
(4):2549–2560, 2020.
Jiawen Zhang, Xumeng Wen, Zhenwei Zhang, Shun Zheng, Jia Li, and Jiang Bian. ProbTS: Benchmarking
point and distributional forecasting across diverse prediction horizons.Advances in Neural Information
Processing Systems, 37:48045–48082, 2024.
Jiaxin Zhang and Siyuan Shang. Fast and Interpretable Probabilistic Solar Power Forecasting via a Multi-
Observation Non-Homogeneous Hidden Markov Model.Energies, 18(10), 2025.
Jinhua Zhang, Zhenyang Huang, Haizheng Wang, Zhongyang Li, Weishu Wang, and Yongqian Liu. Joint
probability aggregation for regional wind power forecasting via R-vine copula and Kolmogorov-Arnold
networks.Results in Engineering, 29:109822, 2026.
Haokun Zhao, Xiang Zhang, Jiaqi Wei, Yiwei Xu, Yuting He, Siqi Sun, and Chenyu You. TimeSeriesScientist:
A General-Purpose AI Agent for Time Series Analysis.arXiv preprint arXiv:2510.01538, 2025a.
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Zican Dong, Yupeng Hou, Beichen Zhang, Yingqian
Min, Junjie Zhang, Peiyu Liu, et al. A survey of large language models.Frontiers of Computer Science,
20(12):2012627, 2026.
Yang Zhao, Yuzhou Chen, and Xinghua Shi. Uncertainty Quantification of Conformalized Spatio-Temporal
Graph Convolutional Network on Forecasting. InIEEE International Conference on Data Mining, pp.
1712–1721, 2025b.
Vincent Zhihao Zheng and Lijun Sun. Multivariate Probabilistic Time Series Forecasting with Correlated
Errors. InThe Thirty-eighth Annual Conference on Neural Information Processing Systems, 2024.
76

Preprint
Weiming Zhi, Ransalu Senanayake, Lionel Ott, and Fabio Ramos. Spatiotemporal Learning of Directional
Uncertainty in Urban Environments With Kernel Recurrent Mixture Density Networks.IEEE Robotics
and Automation Letters, 4(4):4306–4313, 2019.
Zhuping Zhou, Zixu Wang, Yang Liu, Zheng Chen, and Yongneng Xu. Dependent Hidden Markov Model for
pedestrian intention prediction: considering Multivariate Interaction Force.Transportmetrica A: Transport
Science, 22(1):2373921, 2026.
John Zito and Daniel R Kowal. A dynamic copula model for probabilistic forecasting of non-Gaussian
multivariate time series.arXiv preprint arXiv:2502.16874, 2025.
Walter Zucchini and Peter Guttorp. A Hidden Markov Model for Space-Time Precipitation.Water Resources
Research, 27(8):1917–1923, 1991.
Walter Zucchini, Iain L Macdonald, and Roland Langrock.Hidden Markov Models for Time Series: An
Introduction Using R. Chapman & Hall/CRC, Boca Raton, FL, 2nd edition, 2016.
Âzeddine Frimane, Joakim Munkhammar, and Dennis van der Meer. Infinite hidden Markov model for
short-term solar irradiance forecasting.Solar Energy, 244:331–342, 2022.
77
