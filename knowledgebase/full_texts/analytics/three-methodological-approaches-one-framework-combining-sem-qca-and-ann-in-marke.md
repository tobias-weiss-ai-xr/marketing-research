---
title: 'Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics'
url: https://doi.org/10.1057/s41270-026-00523-w
category: analytics
subcategory: measurement
date: 2026-08
venue: Journal of Marketing Analytics
authors:
- A. Mohammed Abubakar
- Alexandre Sukhov
- Joseph F. Hair
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1057/s41270-026-00523-w.pdf
pages: 36
chars: 149176
fetched_at: '2026-11-08T17:56:22+00:00'
kb_version: 1
---

# Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics

ORIGINAL ARTICLE
Journal of Marketing Analytics
https://doi.org/10.1057/s41270-026-00523-w
 Alexandre Sukhov
alexandre.sukhov@kau.se
A. Mohammed Abubakar
me@mohammedabubakar.com; a.abubakar@ccsu.edu
Joseph F. Hair
jhair@southalabama.edu
1 Central Connecticut State University, New Britain, USA
2 Antalya Bilim University, Antalya, Turkey
3 Karlstad University, Universitetsgatan 2, 651 88 Karlstad,
Sweden
4 University of South Alabama, 307 N University Blvd,
Mobile, AL 36688, USA
Abstract
Marketing analytics has increasingly embraced multi-method approaches to capture the complexity of consumer behavior
and organizational phenomena. Among the most prominent are Structural Equation Modeling (SEM), Qualitative Com -
parative Analysis (QCA), and Artificial Neural Network (ANN), three methodological approaches each grounded in a
distinct logic of exploration/theory testing, explanation, and prediction. Despite their complementary strengths, researchers
have lacked systematic guidance on how and why their combined application would be beneficial. This research addresses
this gap by providing comprehensive guidelines for integrating SEM, QCA, and ANN in a single analytical project. In
this article we summarize the theoretical foundations, assumptions, and practical considerations of each method. More
specifically, using a synthetic dataset, we demonstrate how SEM is effective for identifying linear and global relationships
in a proposed theoretical model. We then explain how QCA can be applied to uncover critical segment-specific “causal
recipes” which often remain hidden in SEM. Finally, ANN searches for interactions as well as nonlinear relationships
among predictors and which may lead to superior predictive accuracy. By combining these analytical approaches under
a single unified analytical framework, this research enhances methodological rigor, mitigates risks of data overfitting and
p-hacking, and supports identification of more nuanced insights into complex marketing phenomena. Recommendations
for future research directions are also discussed.
Keywords Artificial neural network · Structural equation modeling · Qualitative comparative analysis · ANNs · fsQCA ·
CB-SEM · PLS-SEM
Received: 15 August 2025 / Accepted: 23 July 2026
© The Author(s) 2026
Three methodological approaches, one framework: combining SEM,
QCA and ANN in marketing analytics
A. Mohammed Abubakar1,2  · Alexandre Sukhov3  · Joseph F. Hair4
approaches (Abubakar et al. 2017; Kaya et al. 2020; Rich-
ter et al. 2022; Sukhov et al. 2023; Woodside & Schpektor
2013), including Comparative Configurational Methods
such as Qualitative Comparative Analysis (QCA) (Rihoux
& Ragin 2009), Structural Equation Modeling (SEM), par -
ticularly partial least squares structural equation modeling
(PLS-SEM) (Hair et al. 2021; Joreskog 1982; Kline 2023),
and Machine Learning approaches such as Artificial Neural
Networks (ANNs) (DeTienne & DeTienne 2017; Guido et
al. 2011). These emerging methods facilitate a much more
comprehensive exploration of complex individual, social
and organizational dynamics (Hew et al. 2023; Yuan et al.
2025).
In combination, these methods represent three groups of
analytical approaches which build on fundamentally differ-
ent assumptions and logic. SEM is a theory-driven, vari -
able-oriented analytical approach suitable for evaluating
hypotheses in a causal-predictive model (Hair et al. 2026).
By contrast, rather than isolating net effects of individual
Introduction
Statistical analysis has long been an important component
of business and marketing research. Recently, researchers
have increasingly adopted more advanced, multi-method

A. M. Abubakar et al.
variables, QCA focuses on how combinations of conditions
jointly produce unique outcomes. In short, QCA essentially
embraces causal complexity, asymmetry, and equifinality
(Fiss 2007; Ragin 2009b). ANNs, in turn, extend the ana -
lytical toolkit into the domain of advanced prediction based
on pattern recognition capabilities and proficiency in mod -
elling complex, linear and non-linear relationships without
strict parametric assumptions (Abubakar et al. 2019a, b). As
such, these three methods in combination are particularly
valuable when the analytical objective shifts from expla -
nation or theory development to maximizing predictive
accuracy.
Despite the considerable analytical power of these tools,
an important reproducibility challenge and practical gap
have historically persisted in both marketing and manage -
ment research. For instance, recent research published in
Nature found only 34% of analyses and results in the social
and behavioral sciences domain could be fully reproduced
as originally reported (Aczel et al. 2026). The notable rea -
son this problem emerged is scholars often lacked analytical
expertise and guidance on how to effectively carry out anal-
yses or combine analytical methods for better interpreta -
tion, ultimately leading to inconsistent applications (Leong
et al. 2024; Sukhov et al. 2023). Furthermore, adherence to
a single methodological approach has limited researchers’
perspectives (Sukhov et al. 2023; Yuan et al. 2025) since
real-world problems are often too intricate and complex
to draw general conclusions based on the “best model fit”
which is often attributed to a variable-based perspective
(Campbell & Fiss 2026; Ragin 2014). The current research
adds to the literature by introducing more comprehensive
analytical considerations as well as guidelines for applica -
tions of SEM, QCA, and ANN. Moreover, these guidelines
are organized under the “same roof”, providing concise
guidance on their combinatory selection and application.
The primary objective of this article, therefore, is to shed
light on analytical combinations of SEM, QCA and ANN.
Rather than positioning these approaches as competing
methods, we advance the view that they are fundamentally
complementary. When deployed in concert, these methods
enable researchers to more effectively navigate the principal
objectives of empirical inquiry, namely theory exploration/
testing, causal explanation, and prediction of outcomes.
The remainder of this article is organized as follows: first,
theoretical foundations of SEM are illustrated in “Structural
equation modelling ” section. Next, “ Qualitative compara -
tive analysis” section. provides the reader with knowledge
of the main assumptions and logic of QCA. “Artificial neural
network (ANN)” section is focused on ANN and “ Combi-
nations OF SEM, QCA, and ANN ” section extends expla -
nations dealing with the combinations of SEM, QCA and
ANN by analyzing a review of existing studies. “ Strategic
guidelines” section further discusses frameworks for com -
bining the three approaches and outlines comprehensive
guidelines along with practical demonstrations. Finally,
“Conclusions and implications ”section provides conclu -
sions and charts suggesting future research directions.
Structural equation modeling
The SEM analytical approach has roots in econometrics,
psychometrics, and sociology (Babin et al. 2008; Jöreskog
1978; Wold 1975) and has been widely applied to test theo-
retical relationships and confirm models in various social
sciences domains (Hair et al. 2012; Kaplan 2008). If we
examine the evolution of analytical methods, early research-
ers relied mostly on univariate analytics, which later were
extended to multivariate, thereby facilitating the capacity
to test and examine multiple variables simultaneously. An
extensive footprint of first-generation statistical methods
appeared in early marketing and management research, such
as factor analysis, cluster analysis, analysis of variance, lin-
ear and logistic regression (Fornell 1985). Although these
methods are powerful and appropriate in many research
contexts, they typically address measurement and structural
relationships in a somewhat fragmented way, which can
introduce a range of analytical limitations depending on the
specific application.
According to Hair et al. ( 2021) and Hair et al. ( 2019),
these first-generation methods share three significant draw -
backs, namely: (1) quite limited capacity to estimate com -
plex relationships within a single model, making it difficult
to simultaneously estimate statistical models involving
multiple mediators, moderators, indirect effects, or all of
these options simultaneously; (2) reliance on observed vari-
ables with latent constructs typically analyzed in separate
stages (e.g., factor analysis) or identified without explicit
measurement models (e.g., clustering); and (3) dependence
on restrictive statistical assumptions such as linearity, nor -
mality, additivity, independence, and homogeneity. SEM,
particularly PLS-SEM, as a second-generation statistical
method, emerged as a solution to the limitations of first-gen-
eration methods (Cole & Preacher 2014; Hair et al. 2021)
and as a substantially more advanced approach to data ana-
lytics compared to the first-generation methods.
SEM “is not a mere statistical technique but rather an
analytical process involving model conceptualization,
parameter identification and estimation, data-model fit
assessment, and potential model re-specification ” (Han -
cock et al. 2010, p. 1). More specifically, SEM epitomizes
a theory-based analytical modus operandi which facilitates
robust scrutiny of presumptive hypotheses in a causal-pre -
dictive model. SEM has roots in two schools of thought, one

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
referred to as covariance-based (CB-SEM) and the other
partial least squares SEM (PLS-SEM). While CB-SEM is
appropriate for measurement theory testing and confirma -
tion of reflective constructs, PLS-SEM is most often applied
for theory-informed prediction, accommodates both reflec -
tive and formative constructs, and emphasizes maximizing
the explained variance in outcome variables as well as out -
come prediction (Hair et al. 2020, 2026).
Advantages of structural equation modeling
The CB-SEM and PLS-SEM methods are substantial
improvements over traditional regression methods because
they effectively handle complex models involving mul -
tiple latent variables which cannot be directly observed
or measured without proxy variables (Hair et al. 2015,
2017). These two SEM variants provide a powerful means
of simultaneously assessing the quality of measurement as
well as examining causal-predictive structural relationships
among constructs (Wang & Wang 2019, p. 2). This capabil-
ity extends to models having first-order constructs as well as
more complex hierarchical specifications, including second-
order and higher-order constructs, which offer flexible and
rigorous framework hypotheses testing. Latent variables
may be observed or measured to some extent using an indi-
cator or proxy (e.g., degree of satisfaction). However, the
phenomena of interest are hardly captured entirely, which
implies observed variable(s) exhibit measurement errors
which need to be removed to the extent possible.
Two previously applied procedures, canonical correla -
tion and regression, assume measurement errors do not
exist. In contrast, CB-SEM and PLS-SEM approaches
can assess and remove errors in measurement and thereby
improve the accuracy of structural model relationships.
Moreover, SEMs enable scholars to quantify various types
of effects in structural models such as total, direct, and indi-
rect (mediated) effects as well as interaction (moderation)
effects and/or combinations of all these effects. These com-
plex specifications were quite difficult to implement using
classical regression alone. In the contemporary literature,
SEM approaches can easily explore much more compli -
cated analytical structures such as mediated-moderated and
moderated-mediated models (Muller et al. 2005; Sarstedt et
al. 2020).
For demonstrative purposes we built on established
constructs from the diffusion of innovations theory and a
synthetic data sample of n = 800 observations. As shown
in Fig. 1, our theoretical model posits that AI adoption is
Fig. 1 Theoretical model of AI
adoption based on diffusion of
innovations theory

A. M. Abubakar et al.
driven by Relative Advantage, Compatibility, Complexity,
Observability, Trialability, and Transparency. We expect
each of these factors to be positively associated with AI
Adoption, while Complexity is hypothesized to exert a neg-
ative association. Each reflective construct was measured
using a four-item scale on a seven-point Likert scale. PLS-
SEM was deployed since it focuses on both maximizing
the explained variance and the predictive performance of
endogenous constructs. (Hair et al. 2020, 2026). ADANCO
version 2.4.1 was operationalized to test the hypothesized
model.
A Harman’s single factor test was conducted to assess
the presence of CMB in the data. The results indicated a
single factor accounted for only 21.8% of the total variance,
which is well below the commonly recommended threshold
of 50% (Podsakoff et al. 2003). However, it is important to
note that Harman’s test is a basic diagnostic tool and has
well-documented limitations in detecting more subtle forms
of CMV (Podsakoff et al. 2003). To further examine CMV ,
a random variable (RV) marker method was calculated by
introducing an unrelated artificial variable (coded 0 or 1)
into the model as a diagnostic check. First, we included
the RV marker as a predictor. The inclusion of the RV did
not materially change the model’s explanatory power, with
R-squared (R2) remaining stable (37.8% to 37.9%), and the
estimated path coefficients remained largely unchanged
(Lindell & Whitney 2001). Second, we tested the RV as a
dependent variable, where all the model constructs func -
tioned as predictors (with the outcome inclusive). We then
evaluated the VIF values, which were all below the 3.3
thresholds (Kock 2015) prior to the addition and after the
addition of the RV both as a predictor and as an outcome.
Together, the extant evidence indicates CMB does not pose
a significant threat. Finally, although these two methods
complement one another, RV is essentially arbitrary and
may not always capture systematic method effects embed -
ded in your data structure. For the measurement model, the
psychometric properties of the constructs were assessed in
terms of internal consistency reliability (Cronbach’s alpha
and composite reliability) and convergent and discriminant
validity, using the average variance extracted (A VE), the
Fornell–Larcker criterion, and the heterotrait–monotrait
ratio (HTMT). As shown in Table 1, all criteria were satis -
fied. In addition, variance inflation factors (VIF) were below
3.3. The results indicate the SEM measurement models have
been confirmed.
Next, we examined the structural model results and
found the dependent variable (DV) AI Adoption is sig -
nificantly influenced by several of the structural model’s
hypothesized independent variables (IVs), including Com -
patibility, Observability, Trialability, and Transparency. In
contrast, the IVs Relative Advantage and Complexity did
not influence AI adoption. Overall, the IV constructs col -
lectively explained 37.8% of the variance in AI adoption
(R-squared = 0.378). These results are displayed in Table 2.
Summary the results of the SEM analysis indicate the IVs
Compatibility, Observability, Trialability and Transparency
have a significant positive association with AI Adoption,
while Relative advantage and Complexity do not exhibit
significant associations. These findings indicate an increase
Table 1 Psychometric properties, reliability and validity of the constructs
Constructs λ 1 2 3 4 5 6 7
1 Relative advantage 0.800–0.914 0.838 0.017 0.005 0.016 0.541 0.007 0.266
2 Compatibility 0.666–0.941 0.002 0.812 0.023 0.002 0.035 0.487 0.268
3 Complexity 0.793–0.862 0.001 0.001 0.839 0.005 0.358 0.011 0.148
4 Observability 0.770–0.872 0.001 0.001 0.001 0.835 0.020 0.482 0.221
5 Trialability 0.789–0.856 0.292 0.001 0.128 0.001 0.825 0.021 0.465
6 Transparency 0.789–0.859 0.001 0.234 0.001 0.232 0.001 0.829 0.387
7 AI adoption 0.829–0.866 0.071 0.073 0.022 0.049 0.216 0.149 0.849
Cronbach’s alpha 0.904 0.886 0.905 0.902 0.895 0.898 0.912
Composite reliability 0.904 0.884 0.905 0.902 0.895 0.898 0.912
Average variance extracted 0.703 0.660 0.705 0.697 0.681 0.688 0.721
λ = factor loadings, Cα, Alpha, CA, composite reliability, AVE, average variance extracted, Below the diagonal = squared inter-construct cor -
relation, values in the diagonal (in bold) = square root of AVE, Values above the diagonal = HTMT ratios
Table 2 Structural model results
Constructs βeta Standard error t-value p-value Decision
1 Relative advantage 0.022 0.042 0.525  > 0.05 Not supported
2 Compatibility 0.159 0.042 3.754  < 0.01 Supported
3 Complexity − 0.014 0.034 − 0.403  > 0.05 Not supported
4 Observability 0.086 0.042 2.036  < 0.05 Supported
5 Trialability 0.456 0.044 10.430  < 0.01 Supported
6 Transparency 0.259 0.048 5.428  < 0.01 Supported

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
in Compatibility, Observability, Trialability and Transpar -
ency, on average, result in higher AI Adoption. In contrast,
Relative Advantage and Complexity are not associated with
AI Adoption. Thus, our results were quite meaningful but
only partially confirmed our proposed theoretical relation -
ships using PLS-SEM.
Limitations of structural equation modeling
CB-SEM and PLS-SEM differ in their statistical assump -
tions and operational applications (Joreskog 1982). Despite
these differences both approaches primarily rely on regres -
sion-based analytical principles, including linearity in
parameters, predominantly additive main effects, and a net-
effects logic that aligns with unifinality, as contrasted with
the configurational and asymmetric reasoning of QCA (Fiss
2007, 2011). These assumptions imply the effects of exog -
enous variables are modeled as independent contributions,
and interactions between them are not permitted unless
explicitly specified by the researcher (Ragin 2006; Wood-
side 2013). Although both variants of SEM can accom -
modate moderation through interaction terms, such effects
must be predefined and are typically limited to low-order
(pairwise or three-way) interactions. As model complexity
increases, the estimation and interpretation of multiple pre -
dictors and moderators becomes increasingly constrained
(Woodside 2014). For instance, higher-order interactions
(such as a four-way interaction) often lead to severe multi-
collinearity issues associated with unstable models and
results which are difficult to interpret. Other limitations of
CB-SEM include the need for normally distributed data,
homoskedasticity, and large sample sizes (N > 250), and
acceptable goodness-of-fit (GoF). In contrast, PLS-SEM
exhibits many benefits compared to CB-SEM since it pro -
duces solutions with small sample sizes (N = 50) and does
not require normally distributed data, homoskedasticity,
or GoF assumptions (Hair et al. 2026). It is important to
note, however, that both SEM methods are grounded in
assumptions of causal symmetry and net-effects reasoning,
thereby limiting their ability to adequately capture conjunc-
tural causation, equifinality, or formally assess necessary or
sufficient conditions (Rasoolimanesh et al. 2021). On the
positive side for PLS-SEM, however, methodologists have
confirmed out-of-sample prediction methods as a quite use-
ful metric (Manley et al. 2021).
Most limitations of these methods can be addressed
through complementary methodologies. QCA is designed to
model configurational causality by evaluating how combi -
nations of conditions interact together to produce an out -
come, thereby capturing potential complex and higher-order
interactions without explicit specification of every inter -
action term (Fiss 2007; Ragin 2009b). In doing so, QCA
provides a direct means of assessing sufficiency and neces -
sity which are not testable in SEM. Moreover, it is relatively
uncommon for researchers to explicitly examine whether
individual predictors exert nonlinear effects on outcomes.
Belzak and Bauer (2019) argue that insignificant or spurious
interaction effects can emerge when the underlying func -
tional form is incorrectly specified as are nonlinearities also
incorrectly attributed to multiplicative effects between vari-
ables. Consistent with this view, Duncan and Kefford (2021)
comment on how the presence of non-linear relationships
can materially influence the detection and interpretation
of direct and interaction effects, increasing the risk of both
false positives and misleading inferences.
Taken together, these findings underscore a critical model-
ing concern: failure to accommodate potential non-linearity
may lead to biased or erroneous conclusions about interac-
tion effects. In light of this, we propose ANN as a natural
interaction effects detector, particularly in contexts where
functional form is unknown or difficult to pre-specify. Our
rationale is ANN offers a flexible and data-driven mecha -
nism capable of evaluating complex and nonlinear interac -
tion structures implicitly. Rather than requiring researchers
to pre-specify interaction terms, ANN can approximate
complex relationships among predictors, enabling interac -
tion effects to emerge from the data without prior theoretical
specification (Leong et al. 2015; Lo et al. 2022). In sum,
these approaches do not replace SEM but rather extend its
rigor and robustness.
Proposition 1 SEM analyses are effective for identifying lin-
ear and global relationships within a model, while QCA and
ANN can extend and complement some of its limitations.
Qualitative comparative analysis
Beyond the insights generated through SEM analysis, Qual-
itative Comparative Analysis (QCA) provides a useful com-
plementary approach to examine conjunctural causation,
equifinality, and causal asymmetry by identifying how dif -
ferent combinations of conditions can produce the same out-
come and how causal paths vary between the presence and
absence of an outcome (Ragin 2009a). QCA is designed to
combine quantitative (or variable-oriented) and qualitative
(or case-oriented) analytical techniques to obtain improved
solutions. In addition, this midway design enables QCA to
“integrate the best features of the case-oriented approach
with the best features of the variable-oriented approach ”
(Ragin 2014, p. 18). The method also concurrently exam -
ines causal complexity as well as complex causal relation -
ships (Rihoux & Marx 2013).

A. M. Abubakar et al.
In the analytics literature, QCA has been described as a
complement to SEM models (Kaya et al. 2020; Sukhov et
al. 2023; Woodside 2013). Specifically, the focus of QCA
is on examining cases (empirical observations) as a whole
(Ragin 2014). The method also includes analysis of “non-
linearity” (when relationships between variables are not
always “symmetric”), “conjunctural causation” (i.e., the
effect of combinations of variables, rather than the addi -
tive net effect of singular variables); and “equifinality,” (the
possibility a certain outcome can be explained by multiple
configurations of conditions rather than “unifinality,” which
assumes a single causal model) (Pappas & Woodside 2021).
The underlying assumption of QCA, therefore, is out -
comes are seldom a product of independent or individ -
ual factors, but rather a result of their interactions with
each other (Ragin 2006). The main objective of the QCA
approach, therefore, is to identify sufficient configurations
of conditions through a systematic case comparison, giv -
ing precedence to empirically observed cases. The resulting
outcome is considered sufficient when all observed cases
exhibit this configuration, and it is possible to observe the
outcome. This enables researchers to conclude that when all
the conditions in a sufficient configuration are present, the
outcome will occur.
In QCA, causality is expressed by determining whether
certain conditions or configurations of conditions are neces-
sary and/or sufficient for the occurrence of a specific out -
come using a set-theoretic algebraic approach (Rubinson et
al. 2019; Sukhov et al. 2021). In other words, QCA “focuses
on the causes of effects, rather than the effects of causes ”
(Rubinson et al. 2019, p. 2), with the primary objective of
PLS-SEM being to identify causal-predictive outcomes
(Hair et al. 2026; Manley et al., 2021). Furthermore, when
applying QCA, researchers must specify conditions which
constitute specific states of a variable through a process of
calibration. This procedure helps to transform qualitative
or quantitative data into sets of defined conditions and out -
comes and anticipates Boolean operations can determine the
necessary conditions and sufficient configurations of condi-
tions. One limitation of QCA, therefore, is the method is
unable to distinguish between the temporal and sequential
roles of the conditions (Caren & Panofsky 2005), and views
the input conditions as suggested “ingredients” and the out-
put configurations of solutions as “recipes.” These charac -
teristics, therefore, confirm a clear distinction between SEM
and QCA approaches in terms of their fundamental assump-
tions and terminology.
Guidelines on types of qualitative comparative
analysis
QCA can take three different forms, each based on some -
what different assumptions about how data is calibrated into
set-membership scores: (1) the crisp-set (csQCA), (2) the
multi-value sets (mvQCA), and (3) the fuzzy set (fsQCA).
The csQCA was initially used when the conditions and
the outcome are perceived as dichotomous, i.e., a case is
either “in” or “out” of a defined set. This is comparable to
a binary variable with two values, 1 (“in,” i.e., female) or
0 (“out,” i.e., non-female). The binary variable, therefore,
is a standard version of QCA initially designed for system -
atic comparisons of qualitative data in empirical samples of
approximately 10–50 cases but more recently has been con-
firmed as useful with larger samples (N > 50). Through this
approach, the researcher takes an active role in defining the
key conditions as being either present or absent (binary). In
addition, the objective of the process is for it to be useful
in, e.g., identifying the presence or absence of individual
activities configured together in an iterative process result -
ing in an anticipated specific outcome (Sukhov et al. 2021).
The multi-value sets (mvQCA) are an extension of
the crisp-set method (csQCA) but equipped for handling
“multi-categorical nominal, ordinal scale, or the use of mul-
tiple thresholds for interval data” (Rihoux & Ragin 2008).
Thus, when the conditions are defined in terms of categories
(e.g., “baby” [0], “toddler” [1], “young child” [2], “teen -
ager” [3]), mvQCA is an appropriate alternative analytical
method. One caution, however, is when the dataset involves
multiple values per condition it can be more complex than
in csQCA. Therefore, the multi-value set method should
be applied with larger datasets to produce more meaning -
ful, reliable and valid results. Although mvQCA relies on
the same procedural steps as cs/fsQCA, it is an extension
of csQCA which enables the use of “real” (i.e., observed)
multi-value conditions, and employs different notations and
Boolean minimization rules during the analyses. Due to this
specificity of mvQCA, the TOSMANA software could be
used since it was purposefully designed for this approach
(Cronqvist 2007), while the R-software package “QCA”
remains the most comprehensive tool for the analysis (Duşa,
2018).
The fsQCA form of QCA is the most frequently applied
option in contemporary research. This is a result of its abil-
ity to distinguish between partial set-membership scores
(Pappas & Woodside 2021; Ragin 2009a). More specifi -
cally, scholars describe the technique as capable of handling
uncertainty, providing fine-grained analysis, adapting to
diverse data, capturing gradations, facilitating rich inter -
pretations, and executing robustness checks by varying
calibration thresholds (Fiss 2011; Schneider and Wagemann

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
2012). In other words, fsQCA variants are used to assign
set-membership scores to conditions between 0 and 1, while
still preserving the two qualitative states of full membership
[1] and full non-membership [0]. Researchers can use this
technique, therefore, to calibrate variables, such as Likert-
scale and continuous measurements into fuzzy set-member-
ship scores. For instance, using a 10-point scale the coding
would be “fully in” a set of high satisfaction [1], “almost but
not fully in” the set of high satisfaction [0.9], “neither in nor
out” of the set of high satisfaction [0.5] (also known as the
crossover-point), “more out than in” the set of high satisfac-
tion [0.3], and “fully out” of the set of high satisfaction [0]
(see Pappas & Woodside 2021).
QCA calibration can follow a direct or an indirect method
(Pappas & Woodside 2021). Direct calibration enables
researchers to set specific thresholds for dividing data into
different categories (“fully in” [1], “the crossover point”
[0.5], and “fully out” [0]) without using complex statistical
models to adjust these thresholds to better fit the data. In
contrast, indirect calibration involves recoding an original
interval-level condition into qualitative categories and then
transforming these categories into numerical set-member -
ship scores, without the need for calibration functions or
anchors (Duşa, 2018).
Proposition 2  Following hypothesis testing via SEM,
researchers can apply QCA to identify alternative config -
urational pathways to the outcome, including equifinality
and causal asymmetry not captured in symmetric and net-
effect SEM models.
For demonstrative purposes, we applied direct calibra -
tion method to the synthetic dataset. See Table 3. Suc -
cessful calibration is not merely technical but interpretive
as well. As Rubinson et al. ( 2019, p. 4) note, “ calibration
requires researchers to carefully reflect upon the nature
of the measures and their meaning ”. Mechanistic calibra -
tion methods like automated clustering or simple rescaling
can yield suboptimal results (Rubinson et al. 2019). So,
researchers should avoid blindly adopting procedures and
instead ensure they fit their project’s specific context. After
the data have been calibrated, the procedure for executing
QCA consists of both a necessity analysis and a sufficiency
analysis.
Necessity analysis
Necessity analysis helps researchers to understand whether
a condition is always present when the outcome is observed.
This means each individual condition is tested against a
necessity hypothesis, i.e., whether the outcome Y is a subset
of the condition X. The empirical cases in the dataset are
then examined against this hypothesis, and if condition X is
present in all cases containing the outcome Y , the condition
is considered to be necessary. If, however, there are numer-
ous cases where the outcome Y is present, but condition X
is absent, the condition cannot be considered necessary. To
better evaluate this relationship, QCA uses measures of con-
sistency and coverage. Consistency measures “ the degree
to which empirical evidence supports the claim that a set
theoretic relation exists” Rihoux and Ragin ( 2008, p. 182),
or how closely the subset relationship is approximated
(Ragin 2006). Coverage on the other hand is “ an assess -
ment on the way the respective terms of the minimal formu-
las ‘cover’ observed cases ”—Rihoux and Ragin ( 2008, p.
182) and measures the relevance of the necessary condition.
Table 3 displays the test of necessary conditions for high AI
adoption. The results indicate none of the examined con -
ditions (predictors) nor their negations meet the threshold
for necessity, as no condition achieves a consistency score
above 0.90 (Ragin 2006).
Table 3 Calibration and necessity test
Constructs Descriptive statistics Necessity test
Range Mean SD Fi Co Fo Consistency Coverage
1 Relative advantage
 ~ Relative advantage
1–7 4.00 1.57 6 4 2 0.655
0.542
0.660
0.543
2 Compatibility
 ~ Compatibility
1–7 4.00 1.53 6 4 2 0.667
0.539
0.667
0.545
3 Complexity
 ~ Complexity
1–7 4.02 1.57 6 4 2 0.641
0.556
0.633
0.569
4 Observability
 ~ Observability
1–7 3.99 1.57 6 4 2 0.647
0.554
0.653
0.555
5 Trialability
 ~ Trialability
1–7 3.98 1.55 6 4 2 0.706
0.503
0.718
0.500
6 Transparency
 ~ Transparency
1–7 4.01 1.56 6 4 2 0.689
0.504
0.687
0.511
AI adoption
 ~ AI adoption
1–7 4.02 1.58 6 4 2 N/A N/A
F-in, full membership; CO, Cross-over; F-o, full non-membership; SD , standard deviation;  ~, negation

A. M. Abubakar et al.
Sufficiency analysis
Sufficiency analysis helps researchers to understand what
combinations of factors (configurations) guarantee the
occurrence of a particular outcome. A configuration (i.e.,
A*B) is considered sufficient if it is a subset of the outcome
Y . In this situation, every case is compared to one another
using a truth table (Rihoux & Ragin 2008), and the consis-
tency and coverage of all possible configurations of condi -
tions1 is evaluated using the fsQCA software. The software
facilitates performing Boolean minimization (“the pairwise
comparison of configurations which have the same outcome
but differ in one other condition”). This procedure simpli -
fies the reported configurations and makes it possible to find
empirically relevant and sensible “causal recipes” which are
sufficient to produce a certain outcome.
The sufficiency analysis generates three types of solu -
tions: complex, parsimonious, and intermediate. The com -
plex solution does not contain any logical remainders and
describes cases that only contain empirical observations.
This means the configurations are very case and data spe -
cific and may make it difficult to make a general interpreta-
tion. Parsimonious solutions produce configurations that are
shared in most cases and result in logically simpler solutions
but may also be limited to show only the core conditions
(Fiss 2011). Although core conditions have a strong con -
nection to the outcome, they do not provide information on
their connectedness to other configurational elements and
hence using only a parsimonious solution may oversim -
plify the configurational explanations. Finally, QCA also
generates intermediate solutions, where the researcher can
make additional decisions regarding which conditions need
to be present or absent based on existing knowledge. This
approach strikes a compromise between the other types
of solutions and is generally a recommended approach to
identifying and reporting sufficient configurations (Greck -
hamer et al. 2013). Moreover, despite the technicalities in
QCA, the final interpretation of which solutions to use and
what the meaning of sufficient configurations is based on
the researcher’s ability to understand and substantiate the
patterns drawing on additional information from theory or
knowledge about the cases.
Advantages of qualitative comparative analysis
QCA is an inherent mixed-method approach. Based on its
set-theoretic foundations, it can be applied flexibly to both
qualitative and quantitative data, as well as small and large
1 The number of theoretically possible configurations of conditions is
determined by the formula 2^k, where k is the number of individual
conditions. This means that if there are, e.g., 7 conditions, they can
form 2^7 = 128 possible configurations.
samples (Greckhamer et al. 2013). Moreover, by placing
primary emphasis on empirical cases, QCA helps to bridge
the divide between theoretical models and observed empiri-
cal reality. Accordingly, the use of QCA enables research -
ers to uncover specific configurations of conditions which
led to a particular outcome in the examined dataset, while
also supporting the development of higher-order interac -
tions and explanations (Fiss 2007; Ragin 2009b). In con -
trast, these features are not readily testable with SEM. In
doing so, QCA ultimately fosters a configurational form of
theorizing that emphasizes how different combinations of
conditions jointly produce a particular outcome (Furnari et
al. 2021; Vis 2012). Table 4 provides an overview of the
primary objectives of QCA depending on its application to
small or large samples.
Following the suggestions offered in Table 4, we
explored the dataset for sufficient conditions that may lead
to AI adoption among users based on the Quine-McCluskey
algorithm. A data matrix was produced with 2 k rows (where
k is the number of conditions), setting a frequency cut-off at
10 and consistency threshold to 0.80 and PRI consistency
to 0.75 recommended for large sample sizes (Mattke et al.
2022; Rihoux & Ragin 2009). The truth table is included
in Appendix Table 14. Sufficiency results in the form of a
configurational chart in Table 5 reveal multiple pathways/
solutions/configurations through which the conditions
(predictors) jointly explain AI adoption. Notably, the SEM
results did not capture the roles of Relative Advantage and
Complexity in shaping user adoption of AI. In contrast,
fsQCA shows Relative Advantage appears in three solution
terms (C1, C2, & C3) and Complexity also in three (C1, C3,
& C4), indicating both conditions are consistently embed -
ded within distinct causal configurations leading to AI
Adoption. These findings suggest Relative Advantage and
Complexity play important, albeit configurational roles in
explaining AI Adoption.
Next, robustness and sensitivity analyses were conducted
by varying calibration anchors, frequency and consistency
thresholds (see Table 6) below. The results remained sub -
stantively stable across alternative settings, with solu -
tion consistency remaining above the commonly accepted
threshold of 0.80. Lowering frequency threshold to 5 and
increasing consistency to 0.90 did not alter the results, and
neither did the cross-over point adjustment (from 0.499 to
0.501). However, PRI consistency threshold proved to mat-
ter most during the robustness tests. Increasing PRI consis -
tency to 0.80 led to a truth table with no cases where the
outcome AI adoption was present, whereas lowering PRI
consistency to 0.70 altered the solutions (simplifying the
solutions but reducing the solution consistency). Although
the alternative 7–4–1 specification increased solution con -
sistency and coverage, it did not provide any conceptual

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
change to configurations and thus was not considered to be
important. Overall, the robustness test procedure helped to
identify the most stable thresholds and thus proved to be
important for the reported configurations.
Summary From the execution of fsQCA, we identified
four distinct configurations that were sufficient for suc -
cessful AI adoption. Essentially, the configurations C1-C4
reveal that AI adoption is not a product of a single condition
or multiple important general factors but instead depends
on a combination of multiple conditions (i.e., conjunctural
causation). Furthermore, the analysis showed that when five
out of six conditions were present, the presence or absence
of Observability or Complexity or Compatibility or Relative
Advantage did not matter. The results indicate, therefore,
the potential absence of these individual conditions could
be compensated for by the presence of other conditions in
the theoretical model. Thus, while our theoretical model
proved highly relevant in practice, the QCA shows that
cases of AI adoption exhibit different configurational pat -
terns, or “recipes,” leading to the same outcome. This case-
oriented, rather than variable-oriented, perspective provides
important insights into how the theoretical model is realized
through multiple combinations of conditions in practice.
Accordingly, SEM and QCA offer complementary
insights. SEM validates the overall theoretical relationships
and the average effects of individual constructs across the
Table  5 Configurational chart of sufficient configurations of condi -
tions for high AI adoption
Conditions Solutions
C1 C2 C3 C4
Relative advantage ● • ●
Compatibility • ● ●
Complexity ● ● •
Observability ● • ●
Trialability • ● • ●
Transparency ● • ● •
Raw coverage 0.250 0.256 0.252 0.246
Unique coverage 0.044 0.050 0.046 0.041
Consistency 0.895 0.895 0.892 0.904
Solution consistency 0.878
Solution coverage 0.387
Large black circles (●) indicate core conditions in the parsimonious
solution, while small black circles (•) indicate peripheral conditions
in the intermediate solution. Blank cells indicate that the condition is
a “don’t care” condition, meaning that its presence or absence is not
relevant to the configuration
Table 6 Robustness and sensitivity checks
Changes in
thresholds
Changes in solutions Solution
consistency
Solution
coverage
Consistency
set to 0.9
No change 0.878 0.387
Frequency set
to 5
No change 0.878 0.387
Alternative
calibration
(7–4–1)
No change 0.911 0.494
PRI consis-
tency set to
0.70
Three simplified solu-
tions remain:
RA*Comp*Tri*Tra
RA*Obs*Tri*Tra
Comp*Complx*Tri*Tra
0.864 0.440
PRI consis-
tency set to
0.80
No outcome is observed – –
Cross-over
point set to
0.501
No change 0.877 0.387
Objectives Small sample Large sample
Philosophical roots Inductive Both inductive and deductive
Aim Theory building for weak associations Theory building and testing
that builds on existing concep-
tual or theoretical foundations
Types of instruments Crisp and fuzzy sets (Likert scales can be
calibrated)
Crisp and fuzzy sets (Likert
scales can be calibrated)
Sample/cases Small (12 to 50) Large (50 +)
Sampling/cases selection Theoretical sampling (with relevance) Theoretical, probability and
non-probability sampling
Number of exogenous
conditions
Between 4 and 8 causal conditions Between 6 to 12 and possibly
more causal conditions
Frequency threshold 1 to 2 cases Minimum of 3 cases
Coverage Typically, high Typically, low
Consistency A consistency score = 1 (i.e., “Always
sufficient”) is tenable, but score of 0.80 is
acceptable
A consistency score >  = 0.80
(i.e., “Almost always suf-
ficient”) is preferred
Interpretation of results Necessity and sufficiency analyses findings
should be interpreted by cross-checking
cases and case knowledge is used to build
theory
Necessity and sufficiency
analyses findings are inter-
preted based on patterns and
causal inferences are drawn
Table 4 Small and large sample
size approaches for fsQCA
Reproduced from Greckhamer et
al. (2013)

A. M. Abubakar et al.
sample, whereas QCA uncovers the multiple case-specific
configurations of conditions through which those constructs
combine to produce successful AI adoption. Together, these
approaches provide a more comprehensive understanding
than either method alone.
Limitations of qualitative comparative analysis
QCA methods, such as the fsQCA approach, applied in the
preceding section have several limitations. First, research-
ers often rely on trial and error or subjective judgment
during calibration of variables into crips or fuzzy set-mem -
bership scores, which can produce inconsistent results and
reduce both the reproducibility and interpretive accuracy of
findings. For this reason, scholars (e.g., Mattke et al. 2022)
recommend using sensitivity checks (the addition of ± 0.001
during calibration) and also application of robustness
checks where both the consistency and frequency of cut-off
thresholds are varied until meaningful results are obtained
(Greckhamer et al. 2013; Pappas & Woodside 2021).
Second, although our configurational analysis identified
highly consistent solution pathways, researchers should
strive to achieve a stronger balance between consistency
and coverage. One way to strengthen the robustness of
configurational findings is to conduct predictive validity
tests using a holdout sample approach, particularly when
larger samples (> N = 100) are available (Pappas & Wood -
side 2021). By validating configurations identified in one
randomly selected subsample against an independent hold -
out subsample, researchers can assess whether the identi -
fied solution pathways are stable and predictive beyond the
estimation sample, thereby increasing confidence that the
configurations capture both reliable and broadly applicable
patterns.
Third, QCA is not a statistical method for hypothesis test-
ing in the conventional way of drawing inferences from a
sample to a broader population (Braumoeller 2015). In fact,
QCA has two major shortcomings which limit its applica -
tion. These limitations include: (1) drawing conclusions
about populations based on samples and (2) formulating
hypotheses about configurations of causal conditions. In
practice, however, researchers often struggle to formulate
configurational hypotheses or propositions due to (1) lack of
experience in formulating causal and complex relationships
(Fainshmidt et al. 2020), and (2) complexities of phenom -
ena under investigation (where every other “thing/factor”
can have a role). Thus, QCA works well as an exploratory
or explanatory method, and as a complement to traditional
statistical approaches such as SEM.
Fourth, even though QCA is suitable for research sce -
narios where the relationships between conditions and out -
comes are not well understood, this characteristic makes it
useful for theory development in complex settings (Thiem
et al. 2016). However, QCA has been widely critiqued for
its static nature and limitations in examining the dynam -
ics of temporal change. In particular, QCA “ is [naturally]
atemporal and obscures the sequential nature of paths of
causation” (cited in Casady 2023). In response, time dif -
ferencing QCA has been proposed as a means of identifying
changes in data over time and defining causality based on
how conditions change over time (see Casady 2023; Suk-
hov et al. 2021). However, even this application of QCA
remains primarily focused on explaining causal complexity
rather than producing precise point-estimates or quantify -
ing predictive shifts applicable to SEM, or pattern-based or
non-linear predictions applicable to ANN.
Proposition 3  Following SEM and QCA analysis, research-
ers can apply ANN to detect non-linear and complex vari -
able interactions, in an effort to identify predictive patterns
beyond traditional linear modeling approaches.
Artificial neural network (ANN)
Beyond the insights generated by SEM and QCA, ANN can
explore complex non-linear interaction structures implicitly.
In short, ANN are computational models inspired by biolog-
ical neural structures which can learn complex, non-linear
functional mappings from inputs to outputs without assum-
ing a specific underlying distribution of the data (A. M.
Abubakar et al. 2019a, b; Olden & Jackson 2002). ANN can
also include probabilistic outputs via appropriate activation
functions (e.g., softmax, cross-entropy, Tanh (hyperbolic
tangent), sigmoid, relu). Finally, ANN are a type of machine
learning (ML) technique that features a parallel and distrib-
uted system of basic processing units which enables them to
store and apply experiential knowledge and also makes the
method accessible for application (Sharma & Chopra 2013).
ANN consist of numerous fundamental units known as
neurons, which serve as both information processors and
connection points within the network (Abubakar 2018;
Sharma & Chopra 2013; Wang et al. 2022). Each connection
link is associated with a weight, used to multiply the sig -
nal transmitted. When ANN are applied, all neurons utilize
a non-linear function for their net input (sum of weighted
input signals) to determine the output signals. ANN are usu-
ally modeled into one input layer, one or more hidden lay -
ers, and one output layer (see A. M. Abubakar et al. 2019a,
b; Olden & Jackson 2002; Wong et al. 2022). Despite its
simple architecture, the hidden layer unit alongside a non-
linear activation function empowers ANN to adeptly solve a
diverse array of complex problems (Olden & Jackson 2002;
Yakubu et al. 2020).

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
Advantages of artificial neural networks
Unlike traditional methods which generally assess vari -
ables linearly (directly), ANN leverage powerful features to
evaluate both linear and non-linear relationships by adjust -
ing the weights between units across layers (Abubakar et
al. 2017; Leong et al. 2015). A notable divergence between
ANN-SEM and ANN-QCA models lies in their approach
to connecting independent variables (i.e., causal conditions)
with dependent variables (i.e., outcomes). SEM and QCA
models establish direct connections, while ANN establish
connections both directly and indirectly through the deter -
mination of weights between units across layers. In short,
ANN outperform many established methods due to their
ability to effectively learn and predict outcomes with preci-
sion (Leong et al. 2024; Sim et al. 2014).
An important consideration is ANN are not subject to
common statistical limitations such as normality, homosce-
dasticity, and linearity that are associated with both SEM
variants. In addition, they do not require the specification
of an explicit error distribution and can flexibly learn com -
plex input–output mappings. Accordingly, ANN facilitate:
(1) high predictive accuracy and validity; (2) quick learn -
ing capabilities and adaptability to new data or conditions,
(3) improved reliability measurement over CB-SEM or
QCA; (4) fewer restrictive assumptions such as normal -
ity, linearity, homoscedasticity, statistical power, sampling
error, and sample size requirements (Abubakar et al. 2017;
Leong et al. 2015; Sim et al. 2014); and (5) the ability to
analyze both curvilinear and rectilinear models which are
difficult or impossible to analyze using traditional methods.
Collectively, these strengths confirm ANN can complement
and overcome some of the limitations and misconceptions
associated with SEM and QCA (Abubakar 2020; Rumelhart
et al. 1986).
Since we have examined our dataset with SEM and
fsQCA methods. The succeeding section presents ANN
analysis to observe why some of the predictors in SEM were
insignificant or had a weak impact on the outcome variable.
The neuralnet R package  (Fritsch et al. 2019) was used to
create the ANN model in the R environment. The R code is
available in the appendix Table 15. The identification and
design of the neutrons were carried out alongside the ANN
setting (See Table 7).
The neural network model was trained using 70% of the
data and 30% was used for testing the out-of-sample model
prediction accuracy. The training required 17,687 iterations
and the model converged with a final error of 11.55, indicat-
ing acceptable training fit. The trained neural network model
based on a single hidden layer (6 neurons) is illustrated in
Fig. 2. The model revealed a set of complex linear and/or
non-linear relationships between the six predictors and AI
adoption. Among the hidden-layer representations, selected
latent feature combinations positively influenced AI Adop -
tion (e.g., Hidden Neurons 1, 2 and 6), while others exerted
a negative influence (e.g., Hidden Neurons 3, 4 and 5). For
example, given that Hidden Neuron H1 positively influence
AI Adoption (+ 2.299), variables with positive weights into
Hidden Neuron H1 tend to support adoption. Thus, we can
say that the strongest drivers through Hidden Neuron H1
are: Relative Advantage (1.583), Compatibility (1.388) and
Observability (1.198). Another example is the path linking
Hidden Neuron H3  to AI Adoption with negative weights
(− 0.978). From this perspective, we can conclude that
the strongest negative drivers through H3 are: Complexity
(-1.905), Observability (-1.991) etc.
Although the connection weights provide insights into
how information propagates through the neural network,
they should not be interpreted as direct effects of individual
predictors on the outcome variable. Unlike SEM’s beta coef-
ficients, ANN connection weights operate through multiple
hidden neurons and nonlinear activation functions, mak -
ing their individual interpretation inherently limited (A.M.
Abubakar et al. 2019a, b). The predictive contribution of
each predictor variable emerges from the collective interac-
tion of all connection weights across the network rather than
from any single weight in isolation. Consequently, the mag-
nitude or sign of an individual connection weight does not
directly reflect the importance or direction of a predictor’s
influence on AI adoption. Instead, the relative contribution
of each predictor should be evaluated using post hoc pro -
cedures such as sensitivity or relative importance analysis,
which are specifically designed to quantify variable impor -
tance within ANN models.
Table 7 ANN network information
Sample Training N = 560 (70%)
Testing N = 240 (30%)
Input layer Covariates Relative
advantage
Compatibility
Complexity
Observability
Trialability
Transparency
Number of unitsa 6
Hidden layer(s) Number of hidden layers 1
Number of units in hidden
layer 1a
6
Activation function Sigmoid
Output layer Response variable AI adoption
Number of units 1
Activation function Sigmoid
Error function Sum of Squares
a. Excluding the bias unit

A. M. Abubakar et al.
To better demonstrate the role of each predictor in the
ANN model, we draw on Garson Algorithms to interpret the
roles (Garson 1991). The relative importance for the predic-
tors is shown in Fig. 3, and surprisingly it differs from those
in SEM. In our SEM analysis, the 3 most important predic -
tors based on beta coefficients and Cohen’s f-squared values
were Trialability, Transparency and Compatibility, while
the other predictors have weak or non-significant impact. In
Fig. 3 Relative importance analysis for the ANN model

Fig. 2 Single hidden layer ANN architecture for predicting AI adoption

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
Fig. 3, ANN results revealed Observability, Relative Advan-
tage and Compatibility as the factors contributing the most,
suggesting the presence of a non-linear effect.
To further illustrate these associations, we apply par -
tial dependence plots (PDPs), a popular machine learning
method used to show the marginal effect of predictors on
a model’s predicted outcome (Molnar 2020; Rudin 2019).
The method does so by averaging out the effects of all
other predictors to reveal whether the relationship is linear,
monotonic, or more complex, thereby helping to interpret
“black box” issues. Figure 4 also suggests that Transpar -
ency and Trialability exhibit more of a linear effect. In
contrast, Observability and Compatibility exhibit a slight
curvilinear relationship that increases monotonically, while
Complexity and Relative advantage exhibit a non-linear and
complex effect. Indeed, the result indicate that Complexity
Fig. 4 Partial dependence plots for the ANN model

A. M. Abubakar et al.
has a negative non-linear effect (e.g., when Complexity≈
0.0 → AI adoption was≈ 0.50). These results suggest the
ANN approach was able to reveal the hidden effects and
relationships SEM failed to capture. Marketing analytics
and social science researchers are therefore encouraged
to use PDP diagrams to explain and illustrate their ANN
results.
To ensure predictive performance of the ANN model,
we applied a repeated random sub-sampling validation (10
folds, 70/30 train–test split) with min–max normalization
applied within each fold to avoid data leakage. In Table 8,
the model indicates stable generalization performance with
no evidence of substantial overfitting by achieving an aver-
age Root Mean Square Error (RMSE) of 1.22 (train) and
1.45 (test). The smaller the RMSE coefficients, the better
the predictive performance of the model. However, given
that the outcome variable was anchored on a 7-point Likert
scale, predictive accuracy is moderate, with an average error
of approximately 1.45 scale points. Nevertheless, scholars
should always aim for smaller RMSE coefficients.
To convert RMSE values into a prediction accuracy per-
centage based on a 1–7 scale, we first determine the total
possible range of the scale. Because the scale of the out -
come variables is 1 to 7, the maximum possible error (the
range) is:
Range :7 − 1=6 .
Using 6 as range, the accuracy percentage can be calculated
using the formula:
Accuracy %=
(
1 − RM SE Range ) ∗ 100
Summary The ANN analysis extends the SEM and fsQCA
findings by revealing that the relationships between pre -
dictors and AI adoption are not strictly linear or purely
configurational. Instead, several predictors exhibit nonlin -
ear and threshold-like effects, particularly Complexity and
Relative Advantage, which were not captured by SEM due
to its parametric assumptions. Furthermore, the ANN results
suggest implicit interaction effects among predictors, indi -
cating that AI Adoption is shaped by complex, non-additive
relationships of the predictors. This highlights the value
of ANN as a complementary method for uncovering hid -
den functional relationships in AI Adoption that remain
obscured in traditional SEM and QCA approaches.
Limitations of artificial neural networks
Machine learning models such as ANN has been cham -
pioned as an AI tool with the capacity to outperform tra -
ditional models and methods (i.e., regression, SEM) on
grounds related to the detection of both linear and non-
linear relationships and their interactions with high predic -
tive accuracy (Abubakar 2020). Despite these advantages,
ANN is not ideal for testing causal relationships due to the
“black box” operating nature. This makes it challenging to
interpret their internal workings and understand why and
how a specific prediction was made. On the other hand, lin-
ear models such as SEM, may potentially oversimplify the
complexities inherent in decision-making processes (Leong
et al. 2015). ANNs have the capacity to reveal this complex-
ity. But while viewed as an advantage in some situations, in
other situations ANNs can be a limitation because complex
models are more difficult to interpret and require more data
to train effectively.
Further, ANNs require longer training time and can be
overfit, meaning they perform well on the training data but
poorly on new, unseen, or noisy data. This implies a blind
application of ANN can be effective at revealing patterns in
data but researchers may find it difficult to develop a mean-
ingful theoretical justification for the pattern, forcing them
to look for an explanation ex-post the analysis. Thus, the use
of ANN with other methods such as SEM or fsQCA could
complement each other (Abubakar 2020; Frösén et al. 2016;
Sukhov et al. 2023). This is because the “non-compensatory
ANNs analysis can complement the weaknesses of the com-
pensatory and linear SEM or QCA analysis ” (Abubakar et
al. 2017; Sukhov et al. 2023).
Proposition 4   A hybrid analytical framework combin -
ing SEM, QCA, and ANN is proposed to provide a more
robust and nuanced understanding of marketing phenom -
ena than any single method. This multi-stage approach
enables researchers to triangulate findings. That is, using
SEM for theory-based hypothesis testing, QCA for identi -
fying segment-specific configurational pathways and ANN
for enhancing predictive validity and variable ranking.
Table 8 A 10-fold cross-validation performance metrics for the ANN
model
Fold # Training
RMSE
Training accu-
racy (%)
Testing
RMSE
Testing
accuracy
(%)
1 1.18 80.33 1.52 74.67
2 1.19 80.17 1.50 75.00
3 1.24 79.33 1.40 76.67
4 1.23 79.50 1.41 76.50
5 1.20 80.00 1.51 74.83
6 1.25 79.17 1.37 77.17
7 1.22 79.67 1.41 76.50
8 1.21 79.83 1.44 76.00
9 1.24 79.33 1.49 75.17
10 1.20 80.00 1.50 75.00
Mean 1.22 79.67 1.45 75.83

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
Discrepancies between these methods should be treated not
as errors, but as theoretical contributions which reveal the
multi-dimensional complexity of human behavior.
Combinations of SEM, QCA, and ANN
Unfortunately, the so-called “science wars” (see Pfeffer
1995; Van Maanen 1995) have resulted in research methods
and philosophies being treated as a religion to be followed
devoutly, without question. The act of employing different
research methodologies and philosophical frameworks to
scrutinize and interpret data is often seen as “opportunistic”
at best and “heretical” at worst by those who are staunch
adherents of a particular scientific philosophy (Bechara &
Van de Ven 2011). This unwavering commitment to a single
philosophy of science often comes at a cost, severely limit -
ing a researcher’s capacity and hindering innovativeness. In
reality, many challenges presented by real-world problems
are far too intricate, uncertain, and complex to be addressed
by a singular perspective or methodology (Bechara & Van
de Ven 2011). Pioneers of SEM note that the “ next-genera-
tion prediction metrics will substantially improve research-
ers’ ability to assess and report the extent to which their
theoretical models provide meaningful predictions” (Hair et
al. 2021, p. 5), and that “ social science scholars would be
remiss if they did not apply all statistical methods at their
disposal to explore and better understand the phenomena
they are researching” (Hair et al. 2019, p. 17).
Emergence of third-generation methods and their appli -
cations have led to wider acceptance of algorithmic and
asymmetric thinking in social sciences research (Kumar
et al. 2022; Woodside 2013), advanced machine learning
algorithms (Sharma & Chopra 2013) and combinations of
different data analytic approaches (e.g.Dul 2016a, 2016b;
Lo et al. 2022; Sukhov et al. 2023; Wang et al. 2022;
Wong et al. 2022). This perspective underscores the value
of embracing a diverse set of analytical tools to enhance
the rigor and comprehensiveness of research findings. This
paper proposes future third-and-fourth generation methods
will be a combination of methods depending on the purpose
and aims of research, such as exploration/theory testing,
causal explanation, and outcome prediction.
In line with this perspective, this article provides a
comprehensive overview of the current data analytical
paradigms in analytics research and shed light on the state-
of-the-art combinations of different analytical techniques to
complement the shortcomings of one another. We believe
by focusing on combining SEM, QCA and ANN and/or
other approaches in different ways, researchers can develop
a more comprehensive and nuanced understanding of data
relations and be able to formulate more meaningful explana-
tions of the complex nature of the social phenomenon under
investigation. This aligns with the axiology of post-pos -
itivistic research, which aims to attain greater objectivity,
precision, and accuracy in explaining research phenomena
(Guba, 1990).
To obtain a better understanding of the current prac -
tices of combining the methods we performed a search in
the Scopus database, using a combination of the following
Table 9 Discrepancies in studies combining SEM, QCA and ANN
Comparison
point
Studies reporting divergence/contradiction Key insight from divergence
Variable
ranking &
importance
Dang et al. (2025): Only 3 out of 10 pathways matched between PLS-SEM and ANN
rankings
Yuan et al. (2025): PLS-SEM ranked Perceived Critical Mass (PCM) highest, but
ANN (non-linear) ranked Task-Technology Fit (TTF) highest
Chandra Chanda et al. (2025): Discrepancy in rankings between Perceived Knowledge
(PKN) and Perceived Severity (PRS) on Attitude
Non-linear attributes exist that affect
user decision-making, showing that
consumers prioritize factors differ-
ently in the long term (ANN) than
suggested by immediate linear asso-
ciations (PLS-SEM)
Insignificant
Variables
(PLS-SEM)
vs. Critical
Conditions
(fsQCA)
Chandra et al. (Telemedicine): PLS-SEM found Perceived Vulnerability (PV),
Response Efficacy (RE), and Self-Efficacy (SEF) insignificant for Attitude. However,
fsQCA revealed these factors still play a significant role when combined with other
variables in configurations
Chanda et al. (AI Adoption): Factors insignificant in PLS-SEM (facilitating condi-
tions, social identity, self-efficacy) were found to be effective in various causal
configurations by fsQCA
Factors that do not show a significant
average linear effect across the whole
sample (PLS-SEM) are revealed by
fsQCA to be necessary or core condi-
tions for achieving the outcome within
certain specific segments (equifinality)
Model Predic-
tive Accuracy
Chanda et al. (Cybersecurity): PLS-SEM yielded values between 60.2% and 68.9%
for endogenous variables. ANN analysis revealed substantially higher predictive accu-
racy, with values reaching 89% to 99%
Chanda et al. (AI Adoption): PLS-SEM achieved 65.9% for AI adoption intention,
while ANN achieved 99%
ANN consistently demonstrates supe-
rior predictive capability over PLS-
SEM in capturing complex nonlinear
relationships, highlighting the inherent
limitations of relying solely on linear
models for accurate prediction

A. M. Abubakar et al.
search terms: SEM, QCA, ANN. 2 This generated 33 docu -
ments. We then limited the search to subject areas where
marketing research is relevant, including Business, Man -
agement and Accounting, Social Sciences, Psychology, and
Economics, with the result producing 16 documents. This
was followed by a review of titles and abstracts where we
eliminated three documents for being out of scope, leaving
13 documents of empirical studies. We then reviewed the
articles based on their research objectives, data collection
approach, data analysis techniques, and the main conclu -
sions the combination of methods were able to support. See
Appendix Table 16 for a comprehensive summary of the
reviewed literature.
2 We used the following string: ( TITLE-ABS-KEY ( SEM) AND
TITLE-ABS-KEY ( qca) OR TITLE-ABS-KEY ( fsqca) OR TITLE-
ABS-KEY ( configurations) AND TITLE-ABS-KEY  ( ann)) AND
( LIMIT-TO ( SUBJAREA, “BUSI”) OR LIMIT-TO ( SUBJAREA,
“SOCI”) OR LIMIT-TO ( SUBJAREA, “PSYC”) OR LIMIT-
TO ( SUBJAREA, “ECON”)).
Based on the articles reviewed, several major topics were
identified: (1) all 13 studies used a hybrid analytical strat -
egy and variants of PLS-SEM, ANN and fsQCA; (2) the
combined method was motivated by the desire to account
for symmetrical and asymmetrical/non-linear techniques to
gain a deeper understanding of the data; (3) PLS-SEM was
typically used first to test linear hypotheses and measure
the strengths of relationships between variables in the pro -
posed theoretical framework, often chosen for its effective -
ness with complex models or non-normally distributed data.
This initial analysis was followed by ANN models to detect
non-linear relationships and, crucially, rank the relative
importance of the identified significant relationships. Next,
fsQCA was applied to identify multiple causal pathways
which were sufficient for the outcome. Finally, (4) although
the triangulation of the methods was used to enhance
robustness, reliability, and precision of the findings, the
studies report different degrees of discrepancy between the
linear and non-linear results. Indeed, these discrepancies are
Table 10 Integrated findings and interpretations
Predictors PLS-SEM
(Linear
symmetrical
effects)
fsQCA (Config-
ural sufficiency
recipes)
ANN (Non-linear
effects)
Joint Methodological Interpretation
C1 C2 C3 C4
Relative
Advantage
Non-signif-
icant
(Linear
effect
absent)
● ● ● Non-linear
effect—acts as a
complex thresh-
old driver that
captures critical
non-additive
values
Methodological reconciliation: Dismissed by SEM due to its strict
parametric linear assumptions. However, fsQCA and ANN uncover
its hidden criticality. It functions as an essential, non-linear threshold
ingredient that must be activated within configurations C1, C2 and
C3 to successfully catalyze AI adoption
Compatibility Significant
( +)
(Stable
driver)
● ● ● Non-linear
effect—exhibit a
non-linear accel-
eration spikes
Triangulated reinforcement: Universally validated across all three
methods as a foundational pillar. It possesses a baseline linear effect
(SEM), constitutes a necessary building block in 3 out of 4 configural
recipes (fsQCA), and displays an exponential acceleration curve
(ANN), demanding utmost strategic priority
Complexity Non-signif-
icant
(Linear
effect
absent)
● ● ● Non-linear effect
with asymmetri-
cal constraint—
acts as a barrier
Methodological reconciliation: Labeled irrelevant by SEM. However,
fsQCA and ANN indicate that Complexity operates as an asymmetri-
cal non-linear hurdle. It is a mandatory structural element in recipes
C1, C3, and C4, meaning its friction is highly context-dependent and
can only be overcome when combined with specific facilitators
Observability Significant
( +)
(Stable
driver)
● ● ● Linear effect—
acts as an incre-
mental driver
Structural nuance: Characterized by a steady, predictable linear con-
tribution to adoption (confirmed by both SEM and ANN). However,
the configural recipes (fsQCA) highlights an asymmetry: while
highly valuable, it is not universally mandatory and can be entirely
compensated for in recipe C1 if other core forces are heavily present
Trialability Significant
( +)
(Stable
driver)
● ● ● ● Linear effect—
acts as an incre-
mental driver
Universal presence: Trialability demonstrates a robust linear progres-
sion across all tests. It acts as a steady incremental driver in SEM/
ANN and serves as a universally present element across all four
fsQCA causal recipes (C1 to C4), solidifying hands-on piloting as a
non-negotiable prerequisite
Transparency Significant
( +)
(Stable
driver)
● ● ● ● Linear effect—
acts an incremen-
tal driver
Universal presence: Transparency maintains a steady, continuous lin-
ear progression in both SEM and ANN; and shows flawless presence
across all four configural paths in fsQCA (C1–C4). This underscores
AI explainability as strict universal requirements for Adoption
Circles (●) indicate the presence of the conditions. Blank cells indicate that the condition is a “don’t care” condition, meaning that its presence
or absence is not relevant to the configuration

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
considered a key point of reflection and thus represent both
a theoretical and methodological contribution. Table 9 dis-
plays additional examples of these discrepancies and their
comparisons.
By comparing studies where discrepancies were iden -
tified, it became evident that a primary explanation for
divergences lays in the differing analytical assumptions
underlying symmetrical and asymmetrical methods. SEM,
in its conventional specification, tends to model relation -
ships as linear and additive. In contrast, asymmetrical meth-
ods such as ANN and fsQCA are inherently better suited to
capturing complex, non-linear, and non-compensatory inter-
actions. Because real-world decision-making often involves
“hidden” non-linear attributes, linear perspectives may fail
to fully capture how variables interact in complex social
phenomena. Consequently, we believe a linear perspective
Conditions CB-SEM PLS-SEM QCA ANN Hybrid SEM-
ANN-QCA
Type of
sample
 Large Recommended Recommended Recommended Recommended Recommended
 Small Possible Recommended Less suitable Recommended
Type of data Recommended
 Normal Recommended Possible Possible Possible Recommended
 Non-normal Possible Possible Possible Recommended
Type of
measurement
model
Recommended
 Single item
constructs
Possible Possible Recommended Possible Recommended
 Multiple item
constructs
Recommended Recommended Recommended Recommended
Type of struc-
tural model
Recommended
 Complex Recommended Recommended Possible Recommended Recommended
 Simple Possible Possible Recommended Recommended Recommended
Research
orientation
Recommended
 Theory
testing
Recommended Recommended
(particularly
for prediction-
oriented theory
development)
Possible Recommended
 Predictive
analytic
Recommended Possible Recommended Recommended
 Exploration Possible Recommended Recommended Recommended
Assumptions Recommended
 Predomi-
nantly linear
Recommended Recommended Recommended Recommended
 Nonlinear/
configurational
Recommended Recommended Recommended
 Machine
learning
enabled
Recommended Recommended
 Sensitivity
analysis
Recommended Recommended Recommended Recommended Recommended
Software AMOS (SPSS
AMOS), LIS-
REL, Mplus, R
(lavaan package)
WarpPLS,
SmartPLS,
PLS-Graph, R
(plspm, seminr
packages)
fsQCA, R (QCA,
SetMethods
packages),
TOSMANA
SPSS Neural
Networks,
MATLAB
(Neural
Network
Toolbox), R
(neuralnet,
keras), Python
(Tensor-
Flowm Keras,
PyTorch)
Combo of
the software
mentioned
in Column
2, 3, 4 and 5.
Activation
of different
packages in R
Table 11 SEM, QCA and ANN
selection matrix

A. M. Abubakar et al.
alone is often insufficient to examine the intricate relation -
ships between variables as evident in our integrated joint
analysis presented in Table 10.
Discrepancies between PLS-SEM and fsQCA results
arise from the difference between measuring “net effects”
across a whole sample and identifying multiple “recipes”
(equifinality) that lead to the same results. Furthermore,
PLS-SEM primarily supports relationships backed by most
of the respondents, while fsQCA identifies results that apply
to segment(s) of the sample. This is one explanation of why
Fig. 5 Guidelines for methodological combination of multiple methods

Analytical
assumptions
SEM (CB-SEM &
PLS-SEM)
QCA ANN Hybrid SEM-
ANN-QCA
Linearity Assumed Not required Not required Assumed
Nonlinear interactions Limited Implicit Strong Captured
Causal symmetry Assumed Explicitly asymmetric No
assumption
Asymme-
try + symme-
try assumed
Net effects Yes No No Captured
Equifinality No Yes Yes Captured
Unifinality Yes Yes (By Exception) Yes (By
Function)
Captured
Predictive power Low–Moderate Low–Moderate High High
Case orientation No Yes Yes Captured
Necessity and
sufficiency
No Yes No Captured
Typical sample size CB-SEM: ≥ 200
PLS-SEM: 10 × rule
/ power-based;
N > / = 50)
Small–
medium: ~ 12–50 + cases
50 times rule
of thumb
50 times rule
of thumb
Sensitivity to sample
size
CB-SEM: High PLS-
SEM: Moderate
Low High Low–High
Table 12 Benefits to the hybrid
SEM-QCA-ANN

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
a variable found statistically insignificant in a linear model
can be revealed as a core or necessary condition when com-
bined with other specific factors in a configurational path.
More specifically, relative advantage and complexity were
insignificant in the SEM analyses in our synthetic dataset. In
contrast, during fsQCA relative advantage appeared in three
solutions [C1, C2 and C3], while complexity also emerged in
three solutions [C1, C3 and C4]. The same pattern emerged
in our ANN analysis. Specifically, Relative Advantage and
Complexity emerged as the second and fourth most impor -
tant contributors, whereas they were deemed insignificant in
our SEM analysis. Furthermore, Trialability and Transpar -
ency had the highest beta coefficients and effect sizes (f2) in
SEM, but emerged as the least contributors in ANN.
One plausible explanation for these differing but comple-
mentary results is that ANN are consistently more effective
at capturing non-linear patterns and demonstrate superior
explanatory accuracy over SEM. Additionally, the principle
of causal asymmetry dictates that the reasons of a posi -
tive outcome are not just the opposite of the reasons for a
negative one. The fsQCA methodology can capture this
difference, while linear models usually cannot. By triangu -
lating these findings, researchers explain how these diver -
gences are theoretical contributions since they provide a
more nuanced, multi-dimensional understanding of human
behavior which a single method would overlook.
Fig. 6 Step by Step guidelines for a hybrid SEM-QCA-ANN analy -
sis. Combining SEM, QCA, and ANN into a single study creates a
“fourth generation” analytical framework that enables researchers to
more extensively explore as well as test, explain and predict com -
plex phenomena simultaneously. Our proposed framework provides
a structured, multiple-phase workflow to more effectively integrate
these methodologies (Table 13)

A. M. Abubakar et al.
Strategic guidelines
A primary conclusion of this research is the combination of
multiple methods helps to overcome individual limitations
of the three methods and provides meaningful information
on the phenomenon under investigation. At the same time,
combinations can take different forms. One way is when
multiple methods help reveal discrepancies between the
results, which invites a closer investigation and exploration
of the phenomenon, as well as additional explanations of the
reasons for these discrepancies resulting in methodological
and theoretical reflections. Another way is when results
show similarities, adding confirmation to the researcher’s
understanding of the phenomenon, but also making it dif -
ficult to assess the added value of this combination apart
from additional reassurance and improved confidence in the
explanation.
These types of situations have become much more com -
mon in many types of scholarly research. For instance,
several scholars have applied QCA to identify configura -
tions of features which are essential for explaining a phe -
nomenon. In addition, they have subsequently applied
ANN to determine the relative importance of the predictors
that emerged from QCA (Aw et al. 2023; Li et al. 2022;
Vizcaíno-González et al. 2017; Wong et al. 2018). Overall,
there are two major justifications for our recommendations:
(1) QCA provides an understanding of various ways an out-
come can be achieved but is quite limited in evaluating the
predictive importance of factors, and (2) scientific tools are
seldom neutral (Woodside 2013, 2014). As a result, there is
Table 13 Comprehensive guidelines of the combined approach
Phase A: Testing and net effects (SEM)
The first stage of the hybrid study typically involves using the appropriate SEM method to assess a theory-based causal-predictive model
Purpose Researchers use this phase to test linear hypotheses and evaluate the measurement model’s reliability and validity
Execution You can choose between CB-SEM for theory confirmation or PLS-SEM for theory-informed causal-predictive
outcome, especially if the data is non-normal or involves complex models
Outcome This phase identifies the significance and strength of individual causal conditions (net effects) within the pro-
posed theoretical framework
Phase B: Configurational recipes and equifinality (QCA)
The next stage employs QCA (typically fsQCA) to look across cases rather than variables
Purpose It identifies “causal recipes”—specific combinations of conditions which are necessary or sufficient to produce
the outcome
Execution Data is calibrated into crisp and/or fuzzy sets, followed by a necessity analysis and a truth table analysis to iden-
tify sufficient configurations
Outcome This phase validates the principle of equifinality, showing multiple distinct pathways can lead to the same result
Phase C: Predictive importance and non-linearity (ANN)
Once the linear relationships are established, both the significant and insignificant variables from the SEM analysis are used as inputs for an
ANN model
Purpose This phase addresses the “black-box” nature of human decision-making by detecting non-linear and non-com-
pensatory relationships that linear models might overlook
Execution Researchers run the ANN model to calculate predictive accuracy (R-square), RMSE and perform a sensitivity
analysis
Outcome The primary goal here is to rank the relative importance of each predictor, often revealing factors with lower
linear impact (in SEM) are critical drivers in a non-linear context
Integrating the findings
The power of this three-pronged approach lays in how the results are synthesized
Theoretical contributions
from discrepancies
If a variable is insignificant in SEM but appears as a core condition in QCA, it suggests the variable only works
in combination with others for specific segments of the sample
Enhanced predictive
validity
The high predictive accuracy of ANN (often 70–99%) provides a robust validation for the lower predictive power
typical of traditional SEM models
Refining theory The insights from the “exploratory” loops of ANN and QCA can be used to re-specify and improve the initial
theoretical model
Methodological considerations
Sample size All three methods are highly recommended for large samples; however, for smaller samples (12–100 cases),
researchers should prioritize a combination of PLS-SEM and QCA
Data characteristics While SEM assumes linearity and symmetry, combining it with QCA and ANN enables the research to capture
non-linearity and causal asymmetry, where the factors causing an outcome may differ from those causing its
absence
Software integration A single study will require a combination of tools, such as SmartPLS or AMOS for SEM, fsQCA for configu-
rational analysis, and SPSS or Python for neural networks. R offers the most comprehensive alternative where
different packages could be downloaded for free and used in a single session

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
often a need to generate additional insights through alterna-
tive methodologies (Kaya et al. 2020; Rasoolimanesh et al.
2021; Sukhov et al. 2023, 2022).
There is a scholarly consensus that the value of scien -
tific methods and tools extends beyond mere data analysis
in many instances and should often be connected to theory
crafting and development. Reflecting on this possibility,
contemporary research has increasingly adopted a robust,
three-staged SEM-QCA-NCA framework to deepen inves -
tigative rigor. This mindset is useful to researchers since it
enables them to report weak or non-significant effects with,
e.g., PLS-SEM, while building an explanation for these
effects with the use of, e.g., NCA and QCA (Sukhov et al.
2023, 2022), instead of trying to fit the data to their model at
all costs in an effort to provide improved explanations and
support for their hypotheses.
A recent review of 50 published studies recommends
the use of the hybrid PLS-SEM and ANN approach, argu -
ing that both SEM variants are primarily selected for their
ability to develop and test hypotheses or theories (Leong
et al. 2024). In addition, ANN was used as complementary
post-hoc technique due to their strong learning and predic -
tive capabilities as well as their high accuracy (Leong et
al. 2024). Interestingly, several studies in the marketing
domain have also applied hybrid SEM-ANN (Mkedder &
Özata 2024; Zhang & Tao 2025). These developments sug-
gest an expansion of the methodological toolbox. To support
more informed methods selection, we encourage research -
ers to align their analytical choices with the aims and objec-
tives of their research, the nature of the data, and the aspired
novelty and contribution. Table 11 provides an overall guide
for selecting an appropriate analytical technique based on
initial assumptions regarding the data.
Taken together, the information in Table 11 helps
researchers to understand the different characteristics of the
selected analytical approaches and improves their choice of
an analytical approach which better suits their objectives
and data. Furthermore, combinations of the methods could
be further motivated by the desire to provide “nuance to a
proposed research model” (see Fig. 5). This means the basis
for analysis could originate in testing a theoretical model
(using SEM variants), since it is accepted as a rigorous
and well-understood analytical tool. But the SEM analy -
ses would then be complemented with QCA and/or ANN
to help identify the significance of contextual differences,
explain the “noise” and other discrepancies between the ini-
tial theoretical model and empirical observation. The results
of these “exploratory” approaches could then further inform
and help refine the theoretical model creating a second, or
even third, loop of data analysis and analytical reflection.
Accordingly, the combined use of SEM, QCA, and ANN
enables a more comprehensive analytical framework that
integrates exploration/theory testing, causal configurational
explanation, and outcome prediction (see Tables 11 and 12).
Our proposed triangulated approach advances understanding
beyond what any single method could achieve in isolation,
offering a richer and more nuanced account of both explana-
tory mechanisms and outcome-generating processes.
Henceforth, we expand existing theorization and meth -
odological landmarks toward combinations of SEM-QCA-
ANN. With the introduction of these common guidelines,
researchers can follow the instructions outlined in Tables 10,
11 and 12, as well as Fig. 6, to ensure more uniform and reli-
able analytical practices. Researchers are also encouraged
to examine their models first using SEM to identify the role
and net effects of individual IVs. In the next phase, perform
analyses to identify necessary conditions, and sufficient
configurations of conditions for a research model. Finally,
ANN can help determine the interactions, non-linear effects
and relative importance of potential causal conditions.
Conclusions and implications
In conclusion, our proposed framework integrating three
useful analytical methodologies demonstrates how combin-
ing diverging analytical techniques can enhance scholarly
research and decision-making processes. Specifically, we
believe applying SEM, QCA, and ANN is particularly valu-
able when an initially theorized model is not fully supported
by empirical data. Rather than trying to overcome limited
or non-significant effects, such outcomes should prompt
researchers to dig deeper and ask “Why?” Further explo -
ration of the data using alternative analytical approaches
could enable them to more completely explain outcomes.
As examples, weak or insignificant SEM paths may reflect
the inherently complex, nonlinear, or configurational nature
of marketing and business phenomena, characteristics that
cannot be fully captured by a single analytical perspective.
By employing complementary techniques, researchers can
potentially uncover hidden patterns, identify multiple causal
pathways, and generate richer explanations which otherwise
would remain obscured. Importantly, the SEM-QCA-ANN
hybrid approach presented in this paper represents a cost-
efficient strategy for continued inquiry, enabling researchers
to extract deeper insights from existing datasets before com-
mitting to additional data collection.
At a broader level, this research conceptually positions
the integration of SEM, QCA, and ANN as a step toward a
“fourth generation ” of analytical techniques in marketing
and social sciences research. This generation moves beyond
confirmation alone and embraces exploration, explanation,
and prediction as equally important scientific goals. Rather
than focusing on only one method, the hybrid approach

A. M. Abubakar et al.
encourages methodological pluralism, where inconsisten -
cies across methods are viewed as theoretically informative
signals rather than analytical shortcomings. Overall, this
research makes several important contributions to theory
development in social sciences research.
First, it challenges the dominance of single-method
research designs by demonstrating how combining differ -
ent analytical techniques can answer fundamentally differ -
ent theoretical questions. SEM primarily addresses “ what
and how” questions by estimating net effects, causal direc -
tion, and strength of relationships. QCA extends theory and
research findings by addressing how and why outcomes
emerge through combinations of conditions, highlighting
causal asymmetry, equifinality, and contextual dependency.
In contrast, ANN further contributes by focusing on “ what
will happen” , capturing complex nonlinear relationships
and enhancing predictive accuracy. Together, these meth -
ods provide a more complete theoretical narrative than any
single approach could offer.
Second, the research reframes methodological discrep -
ancies as opportunities for theory refinement or extensions.
Divergent results across SEM, QCA, and ANN reveal
boundary conditions, hidden nonlinearities, and alterna -
tive causal logics often overlooked previously in traditional
hypothesis-testing frameworks. This perspective encour -
ages scholars to treat unexpected or inconsistent findings
as meaningful theoretical contributions, supporting more
nuanced and realistic explanations of consumer and orga -
nizational behavior.
Third, the research advances methodological theory by
offering a structured framework for aligning research objec-
tives, data characteristics, and analytical techniques. By
explicitly discussing theoretical, methodological, distri -
butional, and sample-size assumptions, this research will
enable scholars to clarify when and why specific methods
or combinations of methods are most appropriate. In doing
so, it contributes to ongoing debates about rigor, robustness,
and transparency in empirical research.
Beyond theory, our propositions have implications for
managers, analysts, and decision-makers who increasingly
rely on data-driven insights. First, the proposed hybrid ana-
lytical approach enables decision-makers to move beyond
“average effects” and gain a more granular understanding of
market and customer behavior. While SEM identifies gen -
eral drivers of outcomes, QCA reveals distinct configura -
tions of conditions that lead to success or failure, and ANN
enhances predictive accuracy. This enables decision-makers
to recognize when and how different strategic “recipes” may
lead to improved outcomes, supporting more flexible and
context-sensitive decision-making.
Second, hybrid approaches support more efficient and
informed resource allocation. Instead of repeatedly collecting
new data until statistically significant results emerge, deci -
sion-makers can leverage multiple analytical perspectives
to better understand existing datasets. The hybrid approach
can also reduce research costs, shorten decision cycles,
and improve the quality of strategic choices, particularly in
environments characterized by uncertainty and complexity.
Third, the proposed framework enables decision-makers
and practitioners to select analytical tools which align with
their specific goals. For example, decision-makers seek -
ing explanation and causal insights may benefit more from
combining SEM and QCA, while individuals focused on
forecasting and scenario planning may rely more heavily on
ANN. The rules of thumb and evaluation metrics suggested
in this research provide practical guidance for choosing,
interpreting, and combining analytical methods in applied
settings.
Recommendations for the hybrid approach
1. Adopt a Multi-Stage Analytical Process : For the most
robust insights, researchers should follow a three-phase
approach: (a) apply SEM to identify net effects and path
significance, (b) explore QCA results to uncover config-
urational pathways and necessity/sufficiency, and (c) use
ANN to determine the relative importance of predictors
through sensitivity analysis.
2. Align Methods with Data and Goals : Selection should
be based on sample size, distribution, and research ori -
entation. For instance, while all methods work for large
samples, only PLS-SEM and QCA are recommended for
smaller samples.
3. Use Hybrid Results to Refine Theory : Instead of fitting
data to a single model, researchers should use the unique
insights from each method, such as QCA’s “recipes”, to
inform and loop back into theory development, provid -
ing more detailed insights into human behavior.
4. Perform Robustness Checks : For all three analytical
methods researchers should use holdout samples to test
predictive validity of theoretical models and to vary cali-
bration thresholds to ensure findings are not results of
subjective bias.
Limitations and future research directions
Despite the analytical power of SEM-QCA-ANN
approaches, each comes with its own limitations. SEM, in
its conventional specification, models linear, additive, and
symmetric relationships; although extensions such as qua -
dratic terms allow PLS-SEM to test specific, researcher-
hypothesized non-linear effects, it remains a confirmatory
technique that estimates net effects across the sample and

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
cannot capture equifinality, asymmetric causal configu -
rations or complex interactions. QCA addresses this by
identifying multiple, non-compensatory configurations of
conditions that lead to the same outcome, but is sensitive
to calibration choices, which may affect reproducibility.
Also, QCA’s requirement for complete data may limit its
applicability in certain empirical contexts. Additionally, the
largely static nature of SEM and QCA restricts their abil -
ity to capture temporal dynamics unless advanced exten -
sions are employed. Finally, ANN offers a fully data-driven
approach capable of uncovering complex and unspeci -
fied non-linear relationships without a priori assumptions
about their functional form, though its black-box nature
limits interpretability without complementary explanatory
methods. Future research could address these limitations by
integrating longitudinal designs to capture temporal dynam-
ics, dynamic modeling and robustness to strengthen QCA’s
reproducibility, and explainable AI approaches (e.g., SHAP,
PDPs) to improve the interpretability of ANN. Such exten -
sions would further strengthen the proposed hybrid frame -
work and enhance its relevance to both theory development
and managerial practice.
Appendix
See Tables 14, 15 and 16.
Table 14 Truth table from QCA for AI adoption
OUT: output value
n: number of casesi nc onfiguration
incl:s ufficiency inclusions core
PRI: proportional reductioni ni nconsistency
RA Comp Complx ObsT ri TraO UT ni nclP RI
11 10 11 12 20 .916 0.788
01 11 11 11 00 .925 0.788
11 11 11 12 50 .909 0.787
10 11 11 11 90 .913 0.772
11 01 11 11 50 .908 0.767
11 00 11 01 40 .903 0.733
10 01 11 01 30 .909 0.726
01 10 11 01 20 .901 0.715
00 11 11 01 10 .888 0.671
11 10 10 02 20 .863 0.653
10 11 10 02 00 .868 0.638
11 00 10 01 00 .869 0.607
01 11 01 02 10 .847 0.590
11 01 01 01 60 .843 0.560
01 01 01 03 40 .815 0.538
10 10 10 02 90 .806 0.526
11 00 01 01 30 .835 0.497
10 00 10 02 10 .816 0.489
01 00 10 01 10 .849 0.480
10 01 01 01 10 .845 0.479
00 11 10 01 00 .822 0.466
00 11 01 01 70 .803 0.433
01 10 01 01 60 .799 0.411
00 00 10 01 00 .809 0.409
00 10 10 01 50 .774 0.382
11 00 00 01 00 .796 0.365
00 01 01 01 80 .778 0.363
01 00 01 02 40 .776 0.360
00 11 00 01 70 .757 0.331
10 01 00 01 60 .753 0.299
00 01 00 02 10 .717 0.271
01 10 00 01 90 .719 0.262
10 00 00 01 90 .711 0.256
00 00 00 04 30 .645 0.229
01 00 00 01 90 .701 0.211
00 10 00 02 40 .665 0.196
RA, relative advantage; Comp, compatibility; Cmplx, complexity; Obs, observability; Tri, trialability; Tra, transparency

A. M. Abubakar et al.
#############################################
# run QCA
#############################################
#upload file
View(DataANN)
data<-DataANN
#activate QCA package
library(QCA)
#############################################
# Calibration
#############################################
data$RA<-calibrate(data$Relative.advantage,type = "fuzzy",thresholds =
"e=2,c=4,i=6",logistic = TRUE)
data$Comp<-calibrate(data$Compatibility,type = "fuzzy",thresholds =
"e=2,c=4,i=6",logistic = TRUE)
data$Complx<-calibrate(data$Complexity,type = "fuzzy",thresholds =
"e=2,c=4,i=6",logistic = TRUE)
data$Obs<-calibrate(data$Observability,type = "fuzzy",thresholds =
"e=2,c=4,i=6",logistic = TRUE)
data$Tri<-calibrate(data$Trialability,type = "fuzzy",thresholds =
"e=2,c=4,i=6",logistic = TRUE)
data$Tra<-calibrate(data$Transparency,type = "fuzzy",thresholds =
"e=2,c=4,i=6",logistic = TRUE)
data$AIa<-calibrate(data$AI.adoption,type = "fuzzy",thresholds =
"e=2,c=4,i=6",logistic = TRUE)
#############################################
# Adjust crossover point
#############################################
data[data==0.5000]<-0.499
#############################################
# Necessity analysis
#############################################
pof(data[,c("RA","Comp","Complx","Obs","Tri","Tra")],data$AIa)
pof(1-data[,c("RA","Comp","Complx","Obs","Tri","Tra")],data$AIa)
#############################################
# Truth Table (two versions: tt and tt_r, tt_r is used for the main analysis)
#############################################
tt<-truthTable(data,outcome = "AIa",conditions = "RA,Comp,Complx,Obs,Tri,Tra",n.cut =
5,incl.cut = 0.9,pri.cut = 0.7,sort.by = "PRI,n+")
tt
tt_r<-truthTable(data,outcome = "AIa",conditions = "RA,Comp,Complx,Obs,Tri,Tra",n.cut
= 10,incl.cut = 0.8,pri.cut = 0.75,sort.by = "PRI,n+")
tt_r
#############################################
# Minimization (two versions: version ending with “_r” is used for main analysis
#############################################
#Complex solution
compsol<-minimize(tt,include = "",details = TRUE)
compsol
compsol_r<-minimize(tt_r,include = "",details = TRUE)
compsol_r
#Parsimonious solution
parsol<-minimize(tt,include = "?",details = TRUE)
parsol
Table 15 R Code for QCA and ANN

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
parsol_r<-minimize(tt_r,include = "?",details = TRUE)
parsol_r
#Intermediate solution
intsol<-minimize(tt,include = "?",dir.exp = c(1,1,1,1,1,1),details = TRUE)
intsol
intsol_r<-minimize(tt_r,include = "?",dir.exp = c(1,1,1,1,1,1),details = TRUE)
intsol_r
#############################################
# Robustness tests
#############################################
#Robustness tests, PRI consistency
tt1<-truthTable(data,outcome = "AIa",conditions = "RA,Comp,Complx,Obs,Tri,Tra",n.cut =
10,incl.cut = 0.8,pri.cut = 0.7,sort.by = "PRI,n+")
intsol<-minimize(tt1,include = "?",dir.exp = c(1,1,1,1,1,1),details = TRUE)
intsol
#Robustness tests, frequency
tt4<-truthTable(data,outcome = "AIa",conditions = "RA,Comp,Complx,Obs,Tri,Tra",n.cut =
5,incl.cut = 0.8,pri.cut =0 .75,sort.by = "PRI,n+")
intsol<-minimize(tt4,include = "?",dir.exp = c(1,1,1,1,1,1),details = TRUE)
intsol
#Robustness tests, consistency
tt5<-truthTable(data,outcome = "AIa",conditions = "RA,Comp,Complx,Obs,Tri,Tra",n.cut =
10,incl.cut = 0.9,pri.cut = 0.75,sort.by = "PRI,n+")
sol1<-minimize(tt5,include = "?",dir.exp = c(1,1,1,1,1,1),details = TRUE)
sol1
#Robustness tests, frequency and consistency
tt2<-truthTable(data,outcome = "AIa",conditions = "RA,Comp,Complx,Obs,Tri,Tra",n.cut =
5,incl.cut = 0.9,pri.cut = 0.75,sort.by = "PRI,n+")
sol2<-minimize(tt2,include = "?",dir.exp = c(1,1,1,1,1,1),details = TRUE)
sol2
#Robustness tests, crossover point
data[data==0.499]<-0.501
tt3<-truthTable(data,outcome = "AIa",conditions = "RA,Comp,Complx,Obs,Tri,Tra",n.cut =
10,incl.cut = 0.8,pri.cut = 0.75,sort.by = "PRI,n+")
intsol<-minimize(tt3,include = "?",dir.exp = c(1,1,1,1,1,1),details = TRUE)
intsol
##Restore data to original calibration
data[data==0.501]<-0.499
#Robustness tests, calibration
data$RA2<-calibrate(data$Relative.advantage,type = "fuzzy",thresholds =
"e=1,c=4,i=7",logistic = TRUE)
data$Comp2<-calibrate(data$Compatibility,type = "fuzzy",thresholds =
"e=1,c=4,i=7",logistic = TRUE)
data$Complx2<-calibrate(data$Complexity,type = "fuzzy",thresholds =
"e=1,c=4,i=7",logistic = TRUE)
data$Obs2<-calibrate(data$Observability,type = "fuzzy",thresholds =
"e=1,c=4,i=7",logistic = TRUE)
data$Tri2<-calibrate(data$Trialability,type = "fuzzy",thresholds =
"e=1,c=4,i=7",logistic = TRUE)
data$Tra2<-calibrate(data$Transparency,type = "fuzzy",thresholds =
"e=1,c=4,i=7",logistic = TRUE)
data$AIa2<-calibrate(data$AI.adoption,type = "fuzzy",thresholds =
"e=1,c=4,i=7",logistic = TRUE)
##Adjust crossover point
data[data==0.5000]<-0.499
tt6<-truthTable(data,outcome = "AIa2",conditions =
"RA2,Comp2,Complx2,Obs2,Tri2,Tra2",n.cut = 10,incl.cut = 0.8,pri.cut = 0.75,sort.by =
"PRI,n+")
intsol<-minimize(tt6,include = "?",dir.exp = c(1,1,1,1,1,1),details = TRUE)
intsol
Table 15 (continued)

A. M. Abubakar et al.
#############################################
# Predictive validity
#############################################
#Predictive validity
##Split data into training and holdout samples
###set.seed() makes the random split reproducible
set.seed(123)
###Sample() randomly selects 50% of cases
train_index<-sample(1:nrow(data),size = 0.5*nrow(data))
###train_data() used to build QCA solution
train_data<-data[train_index,]
###test_data() used only for validation
test_data<-data[-train_index,]
##Create the truth table using the training sample
tt_train<-truthTable(train_data,outcome = "AIa",conditions =
"RA,Comp,Complx,Obs,Tri,Tra",incl.cut = 0.8,n.cut = 5,pri.cut = 0.7,sort.by =
"PRI,n+")
tt_train
##Minimize the truth table
sol_train<-minimize(tt_train,include="?",details = TRUE)
sol_train
##Apply solution(s) to holdout sample
test_solution_1<-with(test_data,pmax(pmin(Comp,Tri,Tra)))
pof(test_solution_1,test_data$AIa,relation = "sufficiency")
test_solution_2<-with(test_data,pmax(pmin(RA,Obs,Tri,Tra)))
pof(test_solution_2,test_data$AIa,relation = "sufficiency")
##Visualize sufficiency relation
XYplot(test_solution_1,test_data$AIa,data,relation = "sufficiency",mguides =
TRUE,jitter = FALSE,clabels = NULL,enhance = FALSE,model = FALSE)
XYplot(test_solution_2,test_data$AIa,data,relation = "sufficiency",mguides =
TRUE,jitter=  FALSE,clabels = NULL,enhance = FALSE,model = FALSE)
#############################################
# 1. Load packages for ANN
#############################################
library(neuralnet)
library(boot)
library(plyr)
library(NeuralNetTools)
library(fastshap)
library(pdp)
library(scales)
#############################################
# 2. Missing values checking
#############################################
apply(DataANN, 2, function(x) sum(is.na(x)))
#############################################
# 2. Train-test data split
#############################################
set.seed(123)
index <- sample(1:nrow(DataANN), round(0.70 * nrow(DataANN)))
train1 <- DataANN[index, ]
test1  <- DataANN[-index, ]
mins <- apply(DataANN, 2, min)
maxs <- apply(DataANN, 2, max)
Table 15 (continued)

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
scaled <- as.data.frame(scale(DataANN, center = mins, scale = maxs - mins))
train_ <- scaled[index, ]
test_  <- scaled[-index, ]
#############################################
# 3. NEURAL NETWORK (ANN)
#############################################
set.seed(123)
nn.fit <- neuralnet(AI.adoption ~ Relative.advantage + Compatibility + Complexity +
Observability + Trialability +Transparency,
data = train_,  hidden = c(6), linear.output = TRUE, err.fct = "sse",
stepmax = 1e6)
plotnet(nn.fit)#basic without weights
plot(nn.fit)# advabced wıth weights
nn.fit$result.matrix
dev.off() # just for control to reset graphics device
#This function allow us to see the relative importance of each var
garson(nn.fit)
#############################################
# 4. VIEW ANN INTERACTIONS WITH D OUTCOME
#############################################
# to draw the distribution 4 each variable..4 non-linear effect
par(mfrow=c(2,2))
gwplot(nn.fit, selected.covariate= "Relative.advantage", selected.response =
"AI.adoption",  min=-1, max=1)
gwplot(nn.fit, selected.covariate= "Compatibility", selected.response = "AI.adoption",
min=-1, max=1)
gwplot(nn.fit, selected.covariate= "Complexity", selected.response = "AI.adoption",
min=-1, max=1)
gwplot(nn.fit, selected.covariate= "Observability", selected.response = "AI.adoption",
min=-1, max=1)
gwplot(nn.fit, selected.covariate= "Trialability", selected.response = "AI.adoption",
min=-1, max=1)
gwplot(nn.fit, selected.covariate= "Transparency", selected.response = "AI.adoption",
min=-1, max=1)
# 2 show the non-linear effect and fluctuations--
pdp::partial(nn.fit, pred.var = "Relative.advantage")
pdp_Relative.advantage <- partial( object = nn.fit, pred.var = "Relative.advantage",
train = train_)
plot(pdp_Relative.advantage, main = "Partial Dependence: Relative.advantage →
AI.adoption")
pdp::partial(nn.fit, pred.var = "Compatibility")
pdp_Relative.advantage <- partial( object = nn.fit, pred.var = "Compatibility", train =
train_)
plot(pdp_Relative.advantage, main = "Partial Dependence: Compatibility → AI.adoption")
pdp::partial(nn.fit, pred.var = "Complexity")
pdp_Relative.advantage <- partial( object = nn.fit, pred.var = "Complexity", train =
train_)
plot(pdp_Relative.advantage, main = "Partial Dependence: Complexity → AI.adoption")
pdp::partial(nn.fit, pred.var = "Observability")
pdp_Relative.advantage <- partial( object = nn.fit, pred.var = "Observability", train =
train_)
plot(pdp_Relative.advantage, main = "Partial Dependence: Observability → AI.adoption")
pdp::partial(nn.fit, pred.var = "Trialability")
pdp_Relative.advantage <- partial( object = nn.fit, pred.var = "Trialability", train =
train_)
plot(pdp_Relative.advantage, main = "Partial Dependence: Trialability → AI.adoption")
pdp::partial(nn.fit, pred.var = "Transparency")
pdp_Relative.advantage <- partial( object = nn.fit, pred.var = "Transparency", train =
train_)
plot(pdp_Relative.advantage, main = "Partial Dependence: Transparency → AI.adoption")
Table 15 (continued)

A. M. Abubakar et al.
#############################################
# 5. TRAINED ANN MODEL PREDICTIONS
#############################################
columns <- c( "Relative.advantage", "Compatibility", "Complexity", "Observability",
"Trialability", "Transparency")
nn.pred.scaled <- compute(nn.fit, test_[, columns])$net.result
####inverse scaleing (back 2 original units)#####
range_y <- maxs["AI.adoption"] - mins["AI.adoption"]
min_y <- mins["AI.adoption"]
nn.pred <- nn.pred.scaled * range_y + min_y
test.real <- test_$AI.adoption * range_y + min_y
###################################################
# 6. TRAINED ANNMODEL PREDICTIOn ERROR RATE CHECKING
###################################################
MSE.nn <- mean((nn.pred - test.real)^2)
RMSE.nn <- sqrt(MSE.nn)
print(paste("ANN MSE =", MSE.nn))
print(paste("ANN RMSE =", RMSE.nn))
#############################################
# 7-FOLD CV FOR ANN
#############################################
set.seed(123)
k <- 10
cv.train.error <- numeric(k)
cv.test.error <- numeric(k)
for(i in 1:k){
index <- sample(1:nrow(DataANN),
round(0.70 * nrow(DataANN)))
train.cv <- DataANN[index, ]
test.cv  <- DataANN[-index, ]
# scaling inside fold (IMPORTANT)
mins.cv <- apply(train.cv, 2, min)
maxs.cv <- apply(train.cv, 2, max)
train.scaled <- as.data.frame(scale(train.cv,
center = mins.cv,
scale = maxs.cv - mins.cv))
test.scaled <- as.data.frame(scale(test.cv,
center = mins.cv,
scale = maxs.cv - mins.cv))
#ANN model settıng-single hidden layer
<vc.nn-  ~noitpoda.IA(tenlaruen
Relative.advantage+Compatibility+Complexity+Observability+Trialability+Transparency,
data = train.scaled,
hidden = c(6),
linear.output = TRUE,
stepmax = 1e6
)
#ANN training MSE
pred.train <- compute(nn.cv, train.scaled[, columns])$net.result
pred.train.real <- pred.train * (maxs.cv["AI.adoption"] - mins.cv["AI.adoption"]) +
mins.cv["AI.adoption"]
train.actual.real <- train.cv$AI.adoption
cv.train.error[i] <- mean((pred.train.real - train.actual.real)^2)
#ANN testing MSE
pred.test <- compute(nn.cv, test.scaled[, columns])$net.result
Table 15 (continued)

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
pred.test.real <- pred.test * (maxs.cv["AI.adoption"] - mins.cv["AI.adoption"]) +
mins.cv["AI.adoption"]
test.actual.real <- test.cv$AI.adoption
cv.test.error[i] <- mean((pred.test.real - test.actual.real)^2)
print(paste("Fold", i, "Train MSE =", cv.train.error[i], "Test MSE =",
cv.test.error[i]))
}
#############################################
# 8. FORMATING & REPORTING D MSE
#############################################
results <- data.frame(
Fold = 1:k,
Train_MSE = cv.train.error,
Test_MSE=  cv.test.error
)
results
colMeans(results[, c("Train_MSE", "Test_MSE")])
#############################################
# 9. FORMATING & REPORTING D RMSE
#############################################
results <- data.frame(
Fold = 1:k,
Train_RMSE = sqrt(cv.train.error),
Test_RMSE = sqrt(cv.test.error)
)
results
colMeans(results[, c("Train_RMSE", "Test_RMSE")])
Table 15 (continued)
Article Research
Objective
Data Collection Data Analysis Conclusions
1 1.Azad et al. (2024):
Investing in our
planet: Examining
retail investors’ prefer-
ence for green bond
investment
Aims to examine
the factors influ-
encing investment
behavior toward
Green Bonds
(GBS)
Sample: Multi-stage
stratified random
sampling of 506 Indian
retail investors. Data
collection spanned
over 6 months, com-
mencing on September
5, 2022
Method/context: A
structured question-
naire administered
online containing 36
items representing 12
constructs
Multi-method analytical approach
combining Partial Least Squares
Structural Equation Modeling
(PLS-SEM), fuzzy-set Qualitative
Comparative Analysis (fsQCA), and
Artificial Neural Networks (ANN)
PLS-SEM was used to evaluate
predefined relationships
fsQCA was used to uncover mul-
tiple causal pathways
ANN was used to rank the relative
importance of each factor
Although the TPB framework
demonstrates a remarkable
ability to predict behavioral
intention, researchers suggest
that it should be comple-
mented with context-specific
factors to provide enriched
contextual information
2 2.Cai et al. (2025):
Post-pandemic job
market: an analysis
of factors influencing
university students’
willingness for flexible
employment based on
SEM-ANN-fsQCA
Investigates how
self-determination
efficacy influences
university stu-
dents’ willingness
to pursue flexible
jobs in China
Analyzes how
attitudes, per-
ceived behavioral
control, and social
influences affect
choices
Sample: 1270 survey
responses from
Chinese university
graduates (2023 &
2024 cohorts)
Method/Context:
Distributed via online
platforms (Wenjuanx-
ing) in two phases
(May–July 2023 and
May–July 2024).
Based on SDT and
TPB models
Mixed-Method: PLS-SEM, Artifi-
cial Neural Networks (ANN), and
Fuzzy-Set Qualitative Comparative
Analysis (fsQCA)
PLS-SEM measured linear relation-
ships and mediating roles of WLB,
JS, and SDP
ANN identified variable impor-
tance and explored nonlinear
relationships
fsQCA uncovered complex
pathways. Multi-Group Analysis
(MGA) verified robustness
Job Satisfaction (JS) and
Work-Life Balance (WLB)
are the primary factors influ-
encing students’ intentions
toward flexible employment.
Intrinsic motivation medi-
ates employment inten-
tions through WLB and JS;
extrinsic motivation mediates
through WLB, JS, and Self-
Development Perception
(SDP)
Table 16 A summary of studies combining SEM, QCA and ANN

A. M. Abubakar et al.
Article Research
Objective
Data Collection Data Analysis Conclusions
3 3.Chanda et al.
(2025a): Artificial
intelligence teaching
assistant adoption in
university education:
Key drivers through
the ability, motiva-
tion and opportunity
framework
Aims to under-
stand the factors
influencing stu-
dents’ intentions
to utilize artificial
intelligence (AI)
as a teaching
tool for enhanc-
ing academic
performance
Sample: 363 valid
responses
Method/Context:
Online question-
naire using purposive
sampling. Data col-
lected from students at
various universities in
three major Bangla-
deshi cities. Based on
the MOA (Motivation,
Opportunities, and
Ability) model
Multi-stage: PLS-SEM-ANN-
fsQCA technique
PLS-SEM assessed predefined
linear hypotheses
ANN measured relative sig-
nificance/linear and non-linear
interactions
fsQCA determined various causal
configurations
Attitude toward AI is the
most influential predictor, fol-
lowed by relative advantage
and interactivity. PLS-SEM
supported significant relation-
ships for interactivity, attitude
toward AI, hedonic motiva-
tion, relative advantage, and
compatibility with adoption
intention. fsQCA identified
seven combinations leading to
higher adoption intention
4 4.Chanda et al.
(2025b): Assess-
ing cybersecurity
awareness among
bank employees: A
multi-stage analytical
approach using PLS-
SEM, ANN, and
fsQCA in a developing
country context
RQ1: What fac-
tors influence
bank employ-
ees’ perceived
threat (PT) and
perceived vulner-
ability (PVU) to
cybersecurity?
RQ2: To what
extent can PT and
PVU generate
cybersecurity
awareness (CSA)
among bank
employees?
Sample: 355 valid
responses
Method/Context: Face-
to-face questionnaire
using purposive sam-
pling from employees
(IT professionals,
security practitioners,
managers) in banks
across four major
districts of Bangla-
desh. Based on the
Stimulus–Organism–
Response (S–O–R)
framework
Multi-stage: PLS-SEM, ANN, and
fsQCA
PLS-SEM tested the structural
model hypotheses, finding direct
effects
ANN assessed non-linear rela-
tionships and ranked predictors’
importance
fsQCA derived complex configura-
tions explaining CSA
Perceived Vulnerability
(PVU) and Perceived Threat
(PT) jointly contribute to
generating CSA. PLS-SEM
supported Information
Security Awareness (ISA) and
Knowledge of Cyber Threats
(KCT) significantly influenc-
ing both PT and PVU. KCT
was the most influential vari-
able for PT (100%) and PVU
(100%) via ANN. FsQCA
highlighted that PT and PVU
are necessity conditions for
generating high CSA
5 5.Chanda Chanda
et al.(2025): Adop-
tion of telemedicine
services among older
adults in a low-income
developing country:
an fsQCA, ANN and
PLS-SEM approach
Explores the
determinants
influencing the
adoption of tele-
medicine services
by older adults
in a low-income
developing
country
Sample: 348
respondents
Method/Context:
Employed a purposive
sampling technique in
a low-income develop-
ing country (Bangla-
desh). Integrates the
Technology Accep-
tance Model (TAM)
and Protection Motiva-
tion Theory (PMT)
Combined Methodological
Approach: PLS-SEM, fsQCA, and
ANN
PLS-SEM tested linear
relationships
ANN performed sensitivity analysis
to identify relative importance
fsQCA uncovered seven distinct
combinations/configurations
Perceived Usefulness (PU)
was the most influential factor
on Attitude (ATT) (100% via
ANN). ATT toward telemedi-
cine is the most influential
factor in generating Adoption
Intention (ITAT) (100% via
ANN). PLS-SEM found PU,
PEOU, Perceived Knowledge
(PKN), and Perceived Sever-
ity (PRS) positively influence
ATT. FsQCA revealed that
Self-efficacy (SEF) and
Response efficacy (RE) are
key antecedents influencing
ATT
6 6.Dang et al. (2025):
From reality to
virtuality: Unveiling
Gen Z’s purchasing
behavior through
virtual influencers in
the metaverse
Examines the fac-
tors influencing
Generation Z’s
(Gen Z) purchase
intentions (PI)
through their
interactions with
virtual influencers
(VIs)
Sample: 352 individu-
als with prior experi-
ence as VIs
Method/Context: Used
judgmental sampling.
Data collected via
online platforms
(August–November
2024). Extends Uses
and Gratifications
Theory (UGT)
Mixed-Method: Fuzzy-set
Qualitative Comparative Analysis
(fsQCA), PLS-SEM, and ANN
PLS-SEM tested linear relation-
ships and mediation by Customer
Satisfaction (CS)
ANN assessed normalized
importance, capturing non-linear
relationships
fsQCA delineated configurational
paths leading to high PI
PLS-SEM revealed the piv-
otal roles of virtual influencer
quality (Perceived Credibility,
Perceived Trustworthiness)
and social presence (Close-
ness, Interactivity, Perceived
Human-likeness) in shaping
PI, mediated by Customer
Satisfaction (CS)
ANN revealed Perceived
Trustworthiness (PT) as the
fundamental driver
FsQCA results validated
equifinality, showing multiple
configurations leading to
high PI
Table 16 (continued)

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
Article Research
Objective
Data Collection Data Analysis Conclusions
7 7.Jain & Chawla
(2025): Fuelling
sustainability through
green bonds: Investi-
gating the impact of
pro-environmental
values on retail inves-
tors’ decisions
RQ1: Do
investors’ pro-
environmental
values (Collectiv-
ism, Altruism,
and Biospheric
Values) influence
their intention
(IN) to invest in
GBS? RQ2: How
does SRI Bias
affect investors’
IN to invest in
GBS? RQ3: Does
attitude (AT)
mediate the rela-
tionships between
these antecedents
and IN toward
GBS?
Sample: Indian retail
investors
Method/Context: Non-
probabilistic judgmen-
tal sampling. Collected
data via online survey
(Dec 2023–Mar 2024).
Targeted investors with
experience and aware-
ness of GBS. Based on
the V AB model
Combined Approach: PLS-SEM,
ANN, and fsQCA
PLS-SEM evaluated predefined
relationships and mediation effects
ANN ranked relative importance
fsQCA uncovered multiple causal
pathways (intermediate solutions
analyzed)
Attitude (AT) plays a sig-
nificant role in forming IN
toward GBS. AT fully medi-
ated the relationship between
Biospheric Values (BV) and
IN, and partially mediated the
linkage between Collectivism
(CV) and IN, and SRI Bias
(SB) and IN. ANN ranked
AT (100%), followed by SB
(96%) and BV (90%) as the
most important factors
8 8.Kang (2025): Risks
and Benefits of Future
Travel with Hyper-
loop: A Multi-Analyti-
cal Approach
Examines the
perceptions and
behaviors of
frequent and occa-
sional travelers
regarding Hyper-
loop technology
Investigates how
four perceived
benefits (eco-
nomic, envi-
ronmental,
socio-cultural,
time-saving) and
four perceived
risks (func-
tional, physical,
psychological,
financial) influ-
ence intention to
use Hyperloop for
tourism
Sample: 600 travel-
ers (386 frequent, 214
occasional)
Method/Context:
Online survey
including a screening
question, an audio
test, and a two-minute
news report about a
Hyperloop test track in
South Korea. Guided
by prospect theory
Multi-Analytical Methods: PLS-
SEM, Multi-Group Analysis
(MGA), fsQCA, and Artificial Neu-
ral Networks (ANN) (deep learning
models)
Frequent travelers prioritize
time-saving benefits, while
occasional travelers are
influenced by economic,
environmental, socio-cultural
benefits, and functional risks.
FsQCA identified distinct
benefit-risk configurations
influencing travel decisions
for both groups
9 9.Malik et al. (2024):
Technological sensing
and response capabili-
ties as drivers for radi-
cal innovation in the
context of apocalyptic
uncertainty
Addresses calls
for more research
to identify fac-
tors that impact
different types
of innovations
(incremental and
radical) by SMEs
Sample: 228 completed
questionnaires received
from Indian SMEs.
Method/Context: Two-
stage study: qualitative
interviews (N = 24) fol-
lowed by main survey.
Cross-industry sample
operating in six indus-
tries in the Northern
Capital Region (NCR)
of India
Analysis: PLS-SEM, fsQCA, and
Artificial Neural Network analysis
PLS-SEM tested direct effects
fsQCA utilized a 5-step methodol-
ogy to identify sufficient causal
configurations
ANN was used for sensitivity
analyses och theoretical constructs
Technological opportunism,
conceptualized as technol-
ogy sensing capability and
technology response capabil-
ity, had a significant positive
impact on the adoption of
both incremental and radical
innovation. FsQCA showed
high overall coverage (91%
for incremental, 87% for radi-
cal adoption), demonstrating
different paths to achieve high
adoption willingness
Table 16 (continued)

A. M. Abubakar et al.
Article Research
Objective
Data Collection Data Analysis Conclusions
10 10.Mishra et al.
(2023): Investing for
a better tomorrow:
Values-driven ante-
cedents of investment
in socially responsible
equity funds by Indian
retail investors
Aims to under-
stand factors
(including values,
reasons for/
against SRI)
driving retail
investors’ socially
responsible
investment (SRI)
behavior
Sample: 370 valid
responses from Indian
retail investors
Method/Context:
Multi-stage stratified
random sampling tech-
nique. Investors had
prior experience (at
least 1 year) in equity
and mutual funds.
Questionnaire based on
prior SRI literature
Combined Approach: PLS-SEM
(two-stage approach for higher-
order constructs), ANN (non-
linear relations, importance), and
fsQCA (synergetic combination of
predictors)
Attitude (ATT) was the stron-
gest predictor of behavioral
intention (BI) (100% normal-
ized importance via ANN).
Religiosity Beliefs (RB)
positively influence Reasons
For (RF) SRI behavior and
negatively influence Reasons
Against (RA) SRI behavior.
FsQCA suggested that ATT or
SRI Awareness (AW) alone
are sufficient conditions to
drive BI
11 11.Wang & Wu
(2025): Building a
triadic model of tech-
nology, motivation,
and engagement: a
mixed-methods study
of AI teaching assis-
tants in design theory
education
How do psycho-
logical (PA, PC),
technological
(CQ, ITF, TTF),
and contextual
factors (SS, LS)
shape student
engagement (SE)
with AI teach-
ing assistants in
design theory
education?
Sample: Undergradu-
ate students majoring
in art and design dis-
ciplines in China. All
used the AI teaching
assistant “MinArt AI”
Method/Context:
Mixed-methods design
including a quantita-
tive survey and qualita-
tive semi-structured
interviews. Based on a
new Triadic Engage-
ment Model
Hybrid Analytical Strategy: PLS-
SEM, ANN, and fsQCA, comple-
mented by qualitative thematic
analysis
PLS-SEM performed significance
testing and mediation analysis
ANN performed sensitivity analy-
sis. fsQCA analyzed configurations
for high SE
Task-Technology Fit (TTF)
(100% via ANN) and School
Support (SS) (77.3% via
ANN) are the most influential
variables in driving Student
Engagement (SE). PLS-SEM
supported PA, PC, CQ, TTF,
and SS having significant
positive effects on SE. Quali-
tative analysis emphasized the
AI assistant’s accessibility,
efficiency, and role in foster-
ing critical engagement
12 12.Yuan et al. (2025):
What shapes mobile
fintech consumers’
post-adoption experi-
ence? A multi-analyti-
cal PLS-ANN-fsQCA
perspective
Aims to under-
stand the forma-
tion of consumers’
post-adoption
experience
response (ER)
toward using
mobile fintech
apps in China
Sample: 1022 effective
responses
Method/Context:
Non-probability
convenience sampling
via online survey
platforms (Sojump and
Credamo). Focused on
Chinese mobile fintech
users
Triple-Stage Analysis: PLS-SEM,
ANN, and fsQCA
PLS-SEM tested linear hypotheses
ANN detected non-linear relation-
ships and derived normalized
importance
fsQCA interpreted conjunctional
causations and configurations
Task-Technology Fit (TTF)
(100% normalized impor-
tance via ANN) is the most
important factor in predicting
Experience Response (ER).
PLS-SEM supported MSE,
PIIT, TTF, SA, and Perceived
Critical Mass (PCM) as
significant predictors of ER.
FsQCA yielded five solutions,
validating the proposition of
equifinality (multiple paths
lead to the same outcome),
that were categorized into
three user persona’s contribut-
ing to a better segmentation
for user retention
13 13.Shao, Z. (2024):
How the characteris-
tics of social media
influencers and live
content influence
consumers’ impulsive
buying in live stream-
ing commerce? The
role of congruence and
attachment
Investigates how
live content–SMIs
congruence (LSC)
and multi-dimen-
sional attachments
(to live content,
SMIs, endorse-
ments) influence
impulsive buying
(IB)
Sample: 608 valid
replies
Method/Context:
Purposive sampling
targeting live stream-
ing commerce enthu-
siasts (over 3 years of
experience) in China.
Based on the Elabora-
tion Likelihood Model
(ELM) and Attachment
Theory
Analysis: PLS-SEM, ANN, and
fsQCA
PLS-SEM supported all hypotheti-
cal paths linking congruence and
attachment factors to impulsive
buying
ANN determined relative
importance
fsQCA examined asymmetry and
conjunctural causation
The core model paths,
including LSC, Relevance
(RE), Credibility (CR), and
Attachment to SMIs (AS)
positively relating to Attach-
ment to Live Content (AC),
were supported. Relevance
of Live Content (RE) was the
most significant predictor for
AC (100% via ANN), while
Attachment to SMIs (AS) was
the most critical predictor for
Impulsive Buying (IB) (100%
via ANN). FsQCA provided
six solutions, demonstrating
that different combinations of
factors lead to IB
Table 16 (continued)

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
Supplementary Information  The online version contains
supplementary material available at  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 5 7 / s 4 1 2 7 0 - 0
2 6 - 0 0 5 2 3 - w     .
Acknowledgements The authors have no conflict of interest and the
only data associated with this research is synthetic.
Funding Open access funding provided by Karlstad University.
Data Availability The dataset is provided in the Supplementary mate -
rial 1
Open Access   This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit  h t t  p : / /  c r e  a t i  v e c o m m o n s . o
r g / l i c e n s e s / b y / 4 . 0 /     .
References
Abubakar, A. M. 2018. Linking work-family interference, workplace
incivility, gender and psychological distress. Journal of Manage-
ment Development  37 (3): 226–242.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 0 8 / J m
d - 0 6 - 2 0 1 7 - 0 2 0 7     .
Abubakar, A. M. 2020. Using hybrid SEM–artificial intelligence:
Approach to examine the nexus between boreout, generation,
career, life and job satisfaction. Personnel Review 49 (1): 67–86.
Abubakar, A. M., B. H. Namin, I. Harazneh, H. Arasli, and T. Tunc.
2017. Does gender moderates the relationship between favorit -
ism/nepotism, supervisor incivility, cynicism and workplace
withdrawal: A neural network and SEM approach. Tourism Man-
agement Perspectives 23:129–139.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . t m p .
2 0 1 7 . 0 6 . 0 0 1     .
Abubakar, A. M., E. Behravesh, H. Rezapouraghdam, and S. B. Yildiz.
2019a. Applying artificial intelligence technique to predict
knowledge hiding behavior. International Journal of Information
Management 49 (December): 45–57.
Abubakar, A. M., E. Behravesh, H. Rezapouraghdam, and S. B. Yildiz.
2019b. Applying artificial intelligence technique to predict
knowledge hiding behavior. International Journal of Information
Management 49:45–57.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . i j i n f o m g t . 2 0 1 9 .
0 2 . 0 0 6     .
Aczel, B., et al. (2026). Investigating the analytical robustness of the
social and behavioural sciences. Nature 652(8108): 135–142.
https:/ /doi.or g/10.10 38/s4 1586-025-09844-9
Aw, E.C.-X., T. Zha, and S.H.-W. Chuah. 2023. My new financial
companion! Non-linear understanding of Robo-advisory service
acceptance. Service Industries Journal 43 (3–4): 185–212. https:/
/doi.or g/10.10 80/02 642069.2022.2161528.
Azad, S., S. L. Tulasi Devi, and A. K. Mishra. 2024. Investing in our
planet: Examining retail investors’ preference for green bond
investment. Business Strategy and the Environment  33 (6):
5151–5173.
Babin, B. J., J. F. Hair, and J. S. Boles. 2008. Publishing research in
marketing journals using structural equation modeling. Journal of
Marketing Theory and Practice 16 (4): 279–286.
Bechara, J., and A. H. Van de Ven. 2011. Triangulating philosophies
of science to understand complex organizational and manage -
rial problems. In Philosophy and organization theory , 343–364.
Emerald Group Publishing Limited.
Belzak, W. C., and D. J. Bauer. 2019. Interaction effects may actu -
ally be nonlinear effects in disguise: A review of the problem and
potential solutions. Addictive Behaviors 94:99–108.
Braumoeller, B. F. 2015. Guarding against false positives in qualitative
comparative analysis. Political Analysis 23 (4): 471–487.
Cai, Q., W. Chen, M. Wang, and K. Di. 2025. Post-pandemic job mar-
ket: An analysis of factors influencing university students’ will -
ingness for flexible employment based on SEM-ANN-fsQCA.
Humanities & Social Sciences Communications 12 (1): 1–18.
Campbell, J.T., and P.C.Fiss. 2026. Tackling the complexity challenge:
When and how to engage in configurational and hybrid theoriz -
ing. Academy of Management Review.
Caren, N., and A. Panofsky. 2005. TQCA: A technique for adding tem-
porality to qualitative comparative analysis. Sociological Meth-
ods & Research 34 (2): 147–172.
Casady, C.B. 2023. A time differencing qualitative comparative analy-
sis (QCA) of public-private partnership (PPP) market maturity.
Public Management Review, 1–23.
Chanda, R. C., A. Vafaei-Zadeh, H. Hanifah, and T. Ramayah. 2025a.
Artificial intelligence teaching assistant adoption in university
education: Key drivers through the ability, motivation and oppor-
tunity framework. Education and Information Technologies  30
(10): 14123–14164.
Chanda, R. C., A. Vafaei-Zadeh, H. Hanifah, and D. Nikbin. 2025b.
Assessing cybersecurity awareness among bank employees:
A multi-stage analytical approach using PLS-SEM, ANN, and
fsQCA in a developing country context. Computers & Security
149 : 104208.
Chandra Chanda, R., A. Vafaei-Zadeh, H. Hanifah, D. Nikbin, and T.
Ahmed. 2025. Adoption of telemedicine services among older
adults in a low-income developing country: An fsQCA, ANN and
PLS-SEM approach. Aslib Journal of Information Management
77 (6): 1176–1222.
Cole, D. A., and K. J. Preacher. 2014. Manifest variable path analysis:
Potentially serious and misleading consequences due to uncor -
rected measurement error. Psychological Methods 19 (2): 300.
Cronqvist, L. (2007). Tosmana–tool for small-N analysis (Version 1.3)
[Software]. Marburg, Hesse, Alemanha. In.
Dang, T. Q., T. M. Nguyen, P. T. Tran, T. T. C. Phan, T. B. Huynh, and
L. T. Nguyen. 2025. From reality to virtuality: Unveiling Gen Z’s
purchasing behavior through virtual influencers in the metaverse.
Digital Business. https:/ /doi.or g/10.10 16/j. digbus.2025.100141.
DeTienne, K. B., and D. H. DeTienne. 2017. Neural networks in stra -
tegic marketing: Exploring the possibilities. Journal of Strategic
Marketing 25 (4): 289–300.
Dul, J. 2016a. Identifying single necessary conditions with NCA and
fsQCA. Journal of Business Research 69 (4): 1516–1523.
Dul, J. 2016b. Necessary condition analysis (NCA) logic and method-
ology of “necessary but not sufficient” causality. Organizational
Research Methods 19 (1): 10–52.
Duncan, R. P., and B. J. Kefford. 2021. Interactions in statistical mod-
els: Three things to know. Methods in Ecology and Evolution 12
(12): 2287–2297.
Duşa, A. 2018. QCA with R: A comprehensive resource. Springer.
Fainshmidt, S., M.A.Witt, R.V . Aguilera and A. Verbeke. 2020. The
contributions of qualitative comparative analysis (QCA) to inter-
national business research. In (V ol. 51, pp. 455–466): Palgrave
Macmillan UK.

A. M. Abubakar et al.
Fiss, P. C. 2007. A set-theoretic approach to organizational configura-
tions. Academy of Management Review 32 (4): 1180–1198. https:/
/doi.or g/10.23 07/20 159362.
Fiss, P. C. 2011. Building better causal theories: A fuzzy set approach
to typologies in organization research. Academy of Management
Journal 54 (2): 393–420.
Fornell, C. 1985. A second generation of multivariate analysis: Clas -
sification of methods and implications for marketing research.
Fritsch, S., F. Guenther, M.N. Wright, M. Suling, S.M. Mueller. 2019.
Neuralnet: Training of neural networks (R package version
1.44.2) [Computer software manual]. In CRAN.  h t t  p s : /  / c r  a n .  r - p  r
o j  e c t .  o r  g / w e b / p a c k a g e s / n e u r a l n e t / n e u r a l n e t . p d f
Frösén, J., J. Luoma, M. Jaakkola, H. Tikkanen, and J. Aspara. 2016.
What counts versus what can be counted: The complex interplay
of market orientation and marketing performance measurement.
Journal of Marketing 80 (3): 60–78.
Furnari, S., D. Crilly, V . F. Misangyi, T. Greckhamer, P. C. Fiss, and
R. V . Aguilera. 2021. Capturing causal complexity: Heuristics for
configurational theorizing. Academy of Management Review  46
(4): 778–799.
Garson, G. D. 1991. Interpreting neural-network connection weights.
AI Expert 6 (4): 46–51.
Greckhamer, T., V . F. Misangyi, and P. C. Fiss. 2013. Chapter 3 the
two QCAs: From a small-N to a large-N set theoretic approach. In
Configurational theory and methods in organizational research ,
49–75. Emerald Group Publishing Limited.
Guba, E.G. 1990. The paradigm dialog. Alternative Paradigms Confer-
ence, Mar, 1989, Indiana University, School of Education, San
Francisco, CA, US.
Guido, G., M. I. Prete, S. Miraglia, and I. De Mare. 2011. Targeting
direct marketing campaigns by neural networks. Journal of Mar-
keting Management 27 (9–10): 992–1006.
Hair, J. F., M. Sarstedt, C. M. Ringle, and J. A. Mena. 2012. An assess-
ment of the use of partial least squares structural equation model-
ing in marketing research. Journal of the Academy of Marketing
Science 40:414–433.
Hair, J. F., G. T. M. Hult, C. M. Ringle, M. Sarstedt, and K. O. Thiele.
2017. Mirror, mirror on the wall: A comparative evaluation of
composite-based structural equation modeling methods. Journal
of the Academy of Marketing Science 45:616–632.
Hair, J. F., J. J. Risher, M. Sarstedt, and C. M. Ringle. 2019. When to
use and how to report the results of PLS-SEM. European Business
Review 31 (1): 2–24. https:/ /doi.or g/10.11 08/EB R-11-2018-0203.
Hair, J. F., M. C. Howard, and C. Nitzl. 2020. Assessing measurement
model quality in PLS-SEM using confirmatory composite analy -
sis. Journal of Business Research 109:101–110.  h t t  p s : /  / d o  i . o  r g / 1
0 . 1 0 1 6 / j . j b u s r e s . 2 0 1 9 . 1 1 . 0 6 9     .
Hair, J. F., G. T. M. Hult, C. M. Ringle, and M. Sarstedt. 2021. A
primer on partial least squares structural equation modeling
(PLS-SEM). Sage publications.
Hair, J. F., G. T. M. Hult, C. M. Ringle, and M. Sarstedt. 2026. A
primer on partial least squares structural equation modeling
(PLS-SEM). 4th ed. Sage.
Hair, J., C. Ringle, and M. Sarstedt. 2015. PLS-SEM: Indeed a silver
bullet. Journal of Marketing Theory and Practice 19(2).
Hancock, G. R., R. O. Mueller, and L. M. Stapleton. 2010. The
reviewer’ s guide to quantitative methods in the social sciences .
Routledge.
Hew, J.-J., V .-H. Lee, and L.-Y . Leong. 2023. Why do mobile con -
sumers resist mobile commerce applications? A hybrid fsQCA-
ANN analysis. Journal of Retailing and Consumer Services  75
: 103526.
Jain, S., and S. Chawla. 2025. Fuelling sustainability through green
bonds: investigating the impact of pro-environmental values on
retail investors’ decisions. Journal of Environmental Planning
and Management, 1–28.
Jöreskog, K. G. 1978. Structural analysis of covariance and correlation
matrices. Psychometrika 43 (4): 443–477.
Joreskog, K.G. 1982. The ML and PLS techniques for modeling with
latent variables: Historical and comparative aspects. Systems
under indirect observation, part I. 263–270.
Kang, S. E. 2026. Risks and benefits of future travel with hyperloop:
A multi-analytical approach. Journal of Travel Research 65 (3):
735–752.
Kaplan, D. 2008. Structural equation modeling: Foundations and
extensions, vol. V ol. 10. SAGE publications.
Kaya, B., A. M. Abubakar, E. Behravesh, H. Yildiz, and I. S. Mert.
2020. Antecedents of innovative performance: Findings from
PLS-SEM and fuzzy sets (fsQCA). Journal of Business Research
114:278–289.
Kline, R. B. 2023. Principles and practice of structural equation mod-
eling. Guilford publications.
Kock, N. 2015. Common method bias in PLS-SEM: A full collinearity
assessment approach. International Journal of E-Collaboration
11 (4): 1–10. https:/ /doi.or g/10.40 18/ij ec.2015100101.
Kumar, S., S. Sahoo, W. M. Lim, S. Kraus, and U. Bamel. 2022.
Fuzzy-set qualitative comparative analysis (fsQCA) in business
and management research: A contemporary overview. Techno-
logical Forecasting and Social Change 178 : 121599.
Leong, L.-Y ., T.-S. Hew, V .-H. Lee, and K.-B. Ooi. 2015. An SEM–
artificial-neural-network analysis of the relationships between
SERVPERF, customer satisfaction and loyalty among low-cost
and full-service airline. Expert Systems with Applications 42 (19):
6620–6634.
Leong, L.-Y ., T.-S. Hew, K.-B. Ooi, G.W.-H. Tan, and A. Koohang.
(2024). An SEM-ANN approach-guidelines in information sys -
tems research. Journal of Computer Information Systems, 1–32.
Li, F., E.C.-X. Aw, G.W.-H. Tan, T.-H. Cham, and K.-B. Ooi. 2022.
The Eureka moment in understanding luxury brand purchases! A
non-linear fsQCA-ANN approach. Journal of Retailing and Con-
sumer Services 68 : 103039.
Lindell, M. K., and D. J. Whitney. 2001. Accounting for common
method variance in cross-sectional research designs. Journal of
Applied Psychology 86 (1): 114.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 3 7 / 0 0 2 1 - 9
0 1 0 . 8 6 . 1 . 1 1 4     .
Lo, P.-S., Y . K. Dwivedi, G.W.-H. Tan, K.-B. Ooi, E.C.-X. Aw, and
B. Metri. 2022. Why do consumers buy impulsively during live
streaming? A deep learning-based dual-stage SEM-ANN analy -
sis. Journal of Business Research 147:325–337.
Van Maanen, J. 1995. Fear and loathing in organization studies. Orga-
nization Science 6:687–692.
Malik, G., P. Sharma, R. Kingshott, T. Y . Leung, and D. Abdolrazagh.
2024. Technological sensing and response capabilities as drivers
for radical innovation in the context of apocalyptic uncertainty.
R&D Management 54 (3): 525–541.
Manley, S. C., J. F. Hair, R. I. Williams, and W. C. McDowell. 2021.
Essential new PLS-SEM analysis methods for your entrepreneur-
ship analytical toolbox. International Entrepreneurship and Man-
agement Journal 17 (1): 1–21.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 7 / s 1 1 3 6 5 - 0 2
0 - 0 0 6 8 7 - 6     .
Mattke, J., C. Maier, T. Weitzel, J. E. Gerow, and J. B. Thatcher. 2022.
Qualitative comparative analysis (QCA) in information systems
research: Status quo, guidelines, and future directions. Communi-
cations of the Association for Information Systems .  h t t  p s : /  / d o  i . o  r
g / 1 0 . 1 7 7 0 5 / 1 C A I S . 0 5 0 0 8     .
Mishra, A. K., R. Bansal, and P. K. Maurya. 2023. Investing for a bet-
ter tomorrow: Values-driven antecedents of investment in socially
responsible equity funds by Indian retail investors. Journal of
Cleaner Production 420: 138441.
Mkedder, N., and F. Z. Özata. 2024. I will buy virtual goods if I like
them: A hybrid PLS-SEM-artificial neural network (ANN) ana -
lytical approach. Journal of Marketing Analytics 12 (1): 42–70.

Three methodological approaches, one framework: combining SEM, QCA and ANN in marketing analytics
Molnar, C. 2020. Interpretable machine learning. Lulu. com.
Muller, D., C. M. Judd, and V . Y . Yzerbyt. 2005. When moderation is
mediated and mediation is moderated. Journal of Personality and
Social Psychology 89 (6): 852.
Olden, J. D., and D. A. Jackson. 2002. Illuminating the “black box”: A
randomization approach for understanding variable contributions
in artificial neural networks. Ecological Modelling  154 (1–2):
135–150.
Pappas, I. O., and A. G. Woodside. 2021. Fuzzy-set qualitative com -
parative analysis (fsQCA): Guidelines for research practice in
Information Systems and marketing. International Journal of
Information Management 58 : 102310.
Pfeffer, J. 1995. Mortality, reproducibility, and the persistence of styles
of theory. Organization Science 6 (6): 681–686.
Podsakoff, P. M., S. B. MacKenzie, J.-Y . Lee, and N. P. Podsakoff.
2003. Common method biases in behavioral research: A critical
review of the literature and recommended remedies. Journal of
Applied Psychology 88 (5): 879–903.  h t t p s : / / d o i . o r   g /  1  0  . 1 0 3 7 / 0 0
2 1 - 9 0 1 0 . 8 8 . 5 . 8 7 9     .
Ragin, C. C. 2006. Set relations in social research: Evaluating their
consistency and coverage. Political Analysis  14 (3): 291–310.
https://doi.org/10.1093/pan/  mpj019.
Ragin, C. C. 2009a. Qualitative comparative analysis using fuzzy sets
(fsQCA). In Configurational comparative methods: Qualitative
comparative analysis (QCA) and related techniques, 87–122.
Ragin, C. C. 2009b. Redesigning social inquiry: Fuzzy sets and
beyond. University of Chicago Press.
Ragin, C. C. 2014. The comparative method: Moving beyond qualita-
tive and quantitative strategies. Univ of California Press.
Rasoolimanesh, S. M., C. M. Ringle, M. Sarstedt, and H. Olya. 2021.
The combined use of symmetric and asymmetric approaches:
Partial least squares-structural equation modeling and fuzzy-set
qualitative comparative analysis. International Journal of Con -
temporary Hospitality Management 33 (5): 1571–1592.
Richter, N. F., S. Hauff, C. M. Ringle, and S. P. Gudergan. 2022. The
use of partial least squares structural equation modeling and
complementary methods in international management research.
Management International Review 62 (4): 449–470.
Rihoux, B., and A. Marx. 2013. QCA, 25 years after “The comparative
method” mapping, challenges, and innovations—Mini-sympo -
sium. Political Research Quarterly 66 (1): 167–235.
Rihoux, B., and C. C. Ragin. 2008. Configurational comparative meth-
ods: Qualitative comparative analysis (QCA) and related tech -
niques. Sage Publications.
Rihoux, B., and C. C. Ragin. 2009. Configurational comparative meth-
ods: Qualitative comparative analysis (QCA) and related tech -
niques, vol. V ol. 1-51. SAGE Publications, Inc.  h t t    p  s :  /  / d  o i  . o r g / 1 0
. 4 1 3 5 / 9 7 8 1 4 5 2 2 2 6 5 6 9     .
Rubinson, C., L. Gerrits, R. Rutten, and T. Greckhamer. 2019. Avoid-
ing common errors in QCA: A short guide for new practitioners.
Sociology 9 (2019): 397–418.
Rudin, C. 2019. Stop explaining black box machine learning models
for high stakes decisions and use interpretable models instead.
Nature Machine Intelligence 1 (5): 206–215.
Rumelhart, D. E., G. E. Hinton, and R. J. Williams. 1986. Learning
representations by back-propagating errors. Nature 323 (6088):
533–536.
Sarstedt, M., J. F. Hair Jr., C. Nitzl, C. M. Ringle, and M. C. Howard.
2020. Beyond a tandem analysis of SEM and PROCESS: Use of
PLS-SEM for mediation analyses! International Journal of Mar-
ket Research 62 (3): 288–299.
Schneider, C. Q., and C. Wagemann. 2012. Set-theoretic methods for
the social sciences: A guide to qualitative comparative analysis .
Cambridge University Press.
Shao, Z. 2024. How the characteristics of social media influencers
and live content influence consumers’ impulsive buying in live
streaming commerce? The role of congruence and attachment.
Journal of Research in Interactive Marketing 18 (3): 506–527.
Sharma, A., and A. Chopra. 2013. Artificial neural networks: Applica-
tions in management. Journal of Business and Management  12
(5): 32–40.
Sim, J.-J., G.W.-H. Tan, J. C. Wong, K.-B. Ooi, and T.-S. Hew.
2014. Understanding and predicting the motivators of mobile
music acceptance–a multi-stage MRA-artificial neural network
approach. Telematics and Informatics 31 (4): 569–584.
Sukhov, A., K. Lättman, L. E. Olsson, M. Friman, and S. Fujii. 2021.
Assessing travel satisfaction in public transport: A configura -
tional approach. Transportation Research Part d, Transport and
Environment 93 : 102732.
Sukhov, A., L. E. Olsson, and M. Friman. 2022. Necessary and suf -
ficient conditions for attractive public transport: Combined use of
PLS-SEM and NCA. Transportation Research Part a, Policy and
Practice 158:239–250.
Sukhov, A., M. Friman, and L. E. Olsson. 2023. Unlocking potential:
An integrated approach using PLS-SEM, NCA, and fsQCA for
informed decision making. Journal of Retailing and Consumer
Services 74 : 103424.
Thiem, A., M. Baumgartner, and D. Bol. 2016. Still lost in translation!
A correction of three misunderstandings between configurational
comparativists and regressional analysts. Comparative Political
Studies 49 (6): 742–774.
Vis, B. 2012. The comparative advantages of fsQCA and regression
analysis for moderately large-N analyses. Sociological Methods
& Research 41 (1): 168–198.
Vizcaíno-González, M., J. Pineiro-Chousa, and J. Sáinz-González.
2017. Selecting explanatory factors of voting decisions by means
of fsQCA and ANN. Quality & Quantity 51:2049–2061.
Wang, J., and X. Wang. 2019. Structural equation modeling: Applica-
tions using Mplus. John Wiley & Sons.
Wang, G., G.W.-H. Tan, Y . Yuan, K.-B. Ooi, and Y . K. Dwivedi. 2022.
Revisiting TAM2 in behavioral targeting advertising: A deep
learning-based dual-stage SEM-ANN analysis. Technological
Forecasting and Social Change 175 : 121345.
Wang, A., and X. Wu. 2025. Building a triadic model of technol -
ogy, motivation, and engagement: A mixed-methods study of AI
teaching assistants in design theory education. Frontiers in Psy-
chology 16: 1624182.
Wold, H. 1975. Path models with latent variables: The NIPALS
approach. In Quantitative sociology, 307–357. Elsevier.
Wong, T. C., M. Y . Haddoud, Y . Kwok, and H. He. 2018. Examin -
ing the key determinants towards online pro-brand and anti-brand
community citizenship behaviours: A two-stage approach. Indus-
trial Management & Data Systems 118 (4): 850–872.
Wong, L.-W., G. W.-H. Tan, K.-B. Ooi, B. Lin, & Y . K. Dwivedi. 2022.
Artificial intelligence-driven risk management for enhancing sup-
ply chain agility: A deep-learning-based dual-stage PLS-SEM-
ANN analysis. International Journal of Production Research ,
1–21.
Woodside, A. G. 2014. Embrace• perform• model: Complexity theory,
contrarian case analysis, and multiple realities. Journal of Busi -
ness Research 67 (12): 2495–2503.
Woodside, A.G., and A. Schpektor. 2013. Triple sense-making of find-
ings from marketing experiments using the dominant variable
based-logic, case-based logic, and isomorphic modeling. Interna-
tional Journal of Business & Economics, 12(2).
Woodside, A.G. 2013. Moving beyond multiple regression analysis to
algorithms: Calling for adoption of a paradigm shift from sym -
metric to asymmetric thinking in data analysis and crafting the -
ory. 66:463–472. Elsevier.
Yakubu, M. N., S. I. Dasuki, A. M. Abubakar, and M. M. Kah. 2020.
Determinants of learning management systems adoption in

A. M. Abubakar et al.
Nigeria: A hybrid SEM and artificial neural network approach.
Education and Information Technologies 25:3515–3539.
Yuan, Y .-P., G.W.-H. Tan, and K.-B. Ooi. 2025. What shapes mobile
fintech consumers’ post-adoption experience? A multi-analytical
PLS-ANN-fsQCA perspective. Technological Forecasting and
Social Change 217 : 124162.
Zhang, D., & Tao, X. (2025). How do technology and gamifica -
tion influence continued usage intention of AI-based wearable
devices? Evidence from SEM-ANN. Asia Pacific Journal of Mar-
keting and Logistics, 1–22.
Publisher's Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
A. Mohammed Abubakar  Associate Professor of Management
Information Systems at Central Connecticut State University, United
States. His research spans into information systems, AI, business ana-
lytics, big data, knowledge management, digital labor and market
platforms, workplace, and employee relations domain. His work has
appeared in top-tier journals including the European Journal of Infor -
mation Systems, International Journal of Information Management,
Journal of Business Research, Journal of Knowledge Management,
International Journal of Contemporary Hospitality Management etc.
He has been included in the list of top 2 % of the world’s scientists
compiled by Stanford University and Elsevier BV .
Alexandre Sukhov Associate Professor in Business Administration
at Karlstad University, Sweden. His research has focused on innova -
tion management, public transport and data analytics. He has expertise
in QCA and interest in research methods.
Joseph F. Hair  Is a distinguished Professor of marketing at University
of South Alabama. He has expertise in multivariate analysis, business
analytics, marketing, SEM and PLS-SEM. He is ranked #1 globally in
Multivariate Data Analysis, Marketing, SEM, and PLS-SEM.
