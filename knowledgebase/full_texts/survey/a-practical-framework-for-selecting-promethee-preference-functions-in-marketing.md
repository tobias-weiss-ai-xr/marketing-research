---
title: A practical framework for selecting PROMETHEE preference functions in marketing decision-making
url: https://doi.org/10.1057/s41270-026-00532-9
category: survey
subcategory: framework
date: 2026-08
venue: Journal of Marketing Analytics
authors:
- Theodore Tarnanidis
- Bertrand Mareschal
- Jason Papathanasiou
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1057/s41270-026-00532-9.pdf
pages: 31
chars: 145045
fetched_at: '2026-11-08T19:17:13+00:00'
kb_version: 1
---

# A practical framework for selecting PROMETHEE preference functions in marketing decision-making

ORIGINAL ARTICLE
Journal of Marketing Analytics
https://doi.org/10.1057/s41270-026-00532-9
 Theodore Tarnanidis
tarnanidis@uom.edu.gr
Bertrand Mareschal
bertrand.mareschal@ulb.be
Jason Papathanasiou
jasonp@uom.edu.gr
Maro Vlachopoulou
mavla@uom.edu.gr
Vijaya Kittu Manda
vijaykittu@hotmail.com
Bruno Sousa
bsousa@ipca.pt
1 Department of Business Administration, University of
Macedonia, 156 Egnatia str., 54636 Thessaloniki, Greece
2 Solvay Brussels School of Economics and Management,
Université libre de Bruxelles (ULB), CP 114, 50 Avenue F.D.
Roosevelt, 1050 Brussels, Belgium
3 Department of Applied Informatics, University of
Macedonia, 156 Egnatia str., 54636 Thessaloniki, Greece
4 Department of Interdisciplinary Research, PBMEIT,
Visakhapatnam 530009, India
5 School of Hospitality and Tourism (ESHT), IPCA –
Polytechnic University of Cávado and Ave,
4750-810 Barcelos, Portugal
Abstract
In marketing decision-making, evaluating competing alternatives using both quantitative and qualitative criteria inherently
yields a complex, multidimensional process. The PROMETHEE (Preference Ranking Organization Method for Enrich -
ment Evaluation) is a powerful multicriteria decision-making (MCDM) methodology that evaluates and ranks options
through head-to-head comparisons, accounting for decision-makers’ preferences. A crucial part of the PROMETHEE
approach involves selecting appropriate preference functions and defining indifference and preference levels that translate
performance disparities into comprehensible degrees of preference. This paper investigates the role of PROMETHEE
preference functions in marketing decision-making and explores practical strategies for determining threshold values that
faithfully represent managerial perspectives. The study explains the method’s utility across various marketing scenarios. In
particular, it discusses brand assessment, ad campaign selection, customer satisfaction measurement, market segmentation,
pricing strategies, and product line evaluation. By combining quantitative performance metrics with subjective managerial
preferences, PROMETHEE provides a clear, adaptable framework that improves decision quality across diverse, some -
times conflicting, evaluation criteria. The research offers actionable recommendations for selecting preference functions
and threshold values, helping marketing executives and scholars construct more reliable and comprehensible decision-
making aids.
Keywords PROMETHEE · Marketing decision-making · Multicriteria decision analysis · Preference functions ·
Threshold determination · Marketing analytics · Decision support systems · PROMETHEE II · Sensitivity analysis ·
Decision tree
JEL Classification M31 · C44 · D81
Received: 2 July 2026 / Accepted: 13 August 2026
© The Author(s) 2026
A practical framework for selecting PROMETHEE preference functions
in marketing decision-making
Theodore Tarnanidis1  · Bertrand Mareschal2  · Jason Papathanasiou1  · Maro Vlachopoulou3  ·
Vijaya Kittu Manda4  · Bruno Sousa5

T. Tarnanidis et al.
Introduction
The process of making marketing decisions has become
notably complicated (Dekimpe and Hanssens 2024; Miles
2026; Montecchi et al. 2024; Rust 2020; Verhoef et al.
2021; Wedel and Kannan 2016). Managers of organiza -
tions are compelled to evaluate competing strategic alterna-
tives across multiple, often conflicting, financial, customer,
operational, and strategic criteria (Gao et al. 2023; Hanssens
2018; Kotler et al. 2022; Petrescu and Krishen 2024). These
situations reflect the growing complexity of contemporary
marketing decision environments. For instance, an adver -
tising campaign could enhance market reach at the cost of
needing a substantially larger budget (Wang et al. 2024). At
the same time, a pricing strategy could boost profitability
at the risk of reduced customer satisfaction (Dwivedi and
McDonald 2025). Likewise, making product line choices
often entails balancing financial success, brand strength,
customer loyalty, and strategic market positioning over
time. Such issues require consideration of both quantitative
and qualitative factors, thereby limiting the effectiveness of
standard, single-criterion evaluation methods in understand-
ing the multifaceted nature of marketing decisions (France
and Ghose 2019; Kotler et al. 2022; Malhotra 2020; Mar-
dani et al. 2018).
The importance of Multicriteria Decision-Making
(MCDM) methods in assisting managerial decision-making
has grown, as they facilitate the concurrent assessment of
multiple performance metrics (Belton and Stewart 2002;
Power 2008; Power et al. 2021). The Preference Ranking
Organization Method for Enrichment Evaluation (PRO -
METHEE), introduced by Brans and Vincke ( 1985), is
among them (Brans and Mareschal 1994). PROMETHEE
has become a leading, widely used evaluation method due
to its transparency, flexibility, and integration of decision-
makers’ preferences into the assessment process (Yatsalo
et al. 2021). Unlike standard evaluation techniques, PRO -
METHEE assesses options through pairwise comparisons.
It gauges the strength of preference among alternatives,
thereby providing more comprehensive decision support
and clearer rankings.
A hallmark of PROMETHEE is the employment of
preference functions and threshold parameters to convert
performance discrepancies into preference levels. These
modeling components assess when observed disparities
between options are deemed insignificant, marginally sig -
nificant, or substantial enough to warrant full preference.
Thus, choosing suitable preference functions and threshold
values significantly impacts the decision model’s robust -
ness, transparency, and credibility.
Practitioners in engineering, environmental management,
energy planning, healthcare, and supply chain management
widely adopt PROMETHEE (Yadav et al. 2024). However,
its use in marketing remains relatively constrained. While
existing marketing studies predominantly use the PRO -
METHEE methodology for specific decision scenarios,
they seldom provide comprehensive guidance on selecting
suitable preference functions or establishing threshold val -
ues. Consequently, researchers and practitioners frequently
depend on subjective assessments or arbitrary parameter
choices. Such choices diminish the transparency, reproduc-
ibility, and practical value of marketing decision models.
This paper addresses this methodological gap by propos-
ing a practical framework for selecting PROMETHEE pref-
erence functions and threshold values in marketing contexts.
Instead of presenting a novel decision-making approach,
the paper offers methodological insights. These will help
researchers and practitioners align various marketing fac -
tors with the most suitable preference models and threshold
levels. The suggested framework translates the theoretical
underpinnings of PROMETHEE into actionable decision
criteria applicable to a wide range of marketing scenarios.
This study makes five principal contributions to the
marketing analytics and multicriteria decision-making lit -
erature. Initially, guidelines are developed for selecting
PROMETHEE preference functions based on the character-
istics of marketing evaluation criteria. Second, it connects
the six standard preference functions to typical marketing
scenarios, such as pricing, ad effectiveness assessment, cus-
tomer satisfaction, brand management, and market segmen-
tation. Third, it suggests a stratified decision-making model
that supports the systematic application of PROMETHEE in
marketing decisions. Fourth, it incorporates a decision tree
to help professionals select appropriate preference func -
tions and threshold values. In conclusion, the paper explores
the managerial impacts of preference modeling and dem -
onstrates how optimal parameter selection enhances the
clarity, uniformity, and comprehensibility of marketing
decision-support frameworks.
The remaining sections of the paper are organized as pre-
sented. The PROMETHEE preference modeling process is
introduced in Sect. “ PROMETHEE in marketing decision-
making: current state of research”. Section “PROMETHEE
preference modeling” explores the application of threshold
concepts to marketing criteria. Section “Threshold concepts
in marketing ” introduces the six PROMETHEE prefer -
ence functions and their practical applications in market -
ing. Section “Selecting PROMETHEE preference functions
for marketing applications ” presents a marketing decision
model and a decision tree for selecting preference functions.
Section “Proposed PROMETHEE framework for marketing
decision-making” demonstrates the application of the frame-
work through a real-data application involving the selection
of a social media platform for marketing communications.

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
Lastly, Sects. “Discussion” and “ Conclusions” explore the
managerial impacts of the proposed framework and outline
the study’s conclusions.
The uniqueness of this study lies in its focus on the PRO-
METHEE methodology rather than its applications. Despite
earlier marketing research that largely used PROMETHEE
to assess specific decision scenarios, surprisingly little effort
has been devoted to providing comprehensive guidance on
selecting preference functions and setting threshold values.
PROMETHEE in marketing decision-making:
current state of research
The section presents a narrative literature review of current
PROMETHEE research findings, focusing on its applica -
tion in marketing decision-making. Narrative reviews are
suitable when the aim is to consolidate the trajectory of a
scholarly domain, pinpoint significant milestones, eluci -
date theoretical frameworks, and underscore areas needing
further investigation, rather than systematically examining
and assessing each published research (Ferrari 2015; Grant
and Booth 2009; Pautasso 2019). Thus, the goal of this
examination is not to offer a comprehensive or systematic
survey of PROMETHEE literature. Instead, the goal is to
outline key methodological advancements, explore repre -
sentative application domains, and pinpoint existing gaps
that motivate the methodological framework presented in
this study. The assessment combines available data through
multicriteria decision-making and marketing research. It
lays the theoretical groundwork for the suggested guidelines
on selecting a preference function and determining thresh -
olds, situating the current research within the broader PRO-
METHEE literature.
PROMETHEE has emerged as one of the most highly
regarded Multicriteria Decision-Making (MCDM) method-
ologies due to its adaptability, clarity, and ability to respect
decision-makers’ preferences via preference functions and
threshold parameters (Brans and Vincke 1985; Macharis et
al. 2015). Ever since its inception, PROMETHEE has been
widely used to address complex decision-making scenarios
involving numerous, often contradictory criteria. Its straight-
forward pairwise comparison method, along with its ability
to integrate qualitative and quantitative data, has facilitated
its broad acceptance in various fields (Behzadian et al. 2010;
Greco et al. 2016). PROMETHEE is widely used and effec-
tive across various areas. Within these areas, the approach
has been used to assess competing options, accounting for
technical, economic, environmental, and social factors.
Various studies have shown that PROMETHEE provides
clear rankings and supports decision-making by thoroughly
integrating decision-makers’ preferences into the evaluation
process. (Behzadian et al. 2010; Biswas et al. 2025; Coque-
let et al. 2025; Ishizaka and Nemery 2013). The ongoing
advancements in PROMETHEE have also led to various
methodological expansions, including PROMETHEE II
for comprehensive ranking (Coquelet et al. 2025), PRO -
METHEE V for handling constrained decision scenarios
(Tibay et al. 2022), and collaborative decision-support sys-
tems that allow multiple stakeholders to contribute to the
evaluation process (Macharis et al. 2015). These advance -
ments have bolstered this method’s position as a top con -
tender in the broad field of multicriteria decision analysis.
The increased accessibility of marketing data, alongside
the growing complexity of strategic decisions, has fueled
interest in applying MCDM methods to marketing prob -
lems. Marketing managers are usually expected to assess
options using several performance metrics, such as finan -
cial results, customer satisfaction, market position, brand
strength, customer loyalty, and advertising impact. Given
that these criteria frequently conflict and encompass both
objective and subjective data, PROMETHEE provides a
compelling framework for supporting marketing decisions.
Research has previously employed PROMETHEE for
several marketing-related challenges, including product
selection, supplier evaluation, assessment of retail sites,
pricing determination, management of customer relation -
ships, evaluation of advertising campaigns, selection of
distribution channels, and evaluation of brand performance.
In many instances, the approach has demonstrated its abil -
ity to aggregate diverse assessment metrics and deliver
clear rankings that facilitate strategic marketing decisions.
Additionally, the inclusion of preference functions allows
marketing managers to account for variations in strategic
emphases and managerial discretion that conventional scor-
ing methods cannot accommodate. (Sklavos et al. 2025;
Tarnanidis and Mareschal 2025; Tarnanidis et al. 2026a;
Wierenga 2011).
With the incorporation of recent advances in marketing
analytics, business intelligence, and customer analytics,
the applicability of MCDM methods has grown (Rialti et
al. 2019; Shu et al. 2026). Modern marketing now heav -
ily depends on vast amounts of customer, transactional, and
behavioral data, necessitating decision-making approaches
that blend quantitative insights with expert expertise (Gupta
and Khan 2024; Tarnanidis et al. 2026a). Therefore, PRO-
METHEE has significant potential to support data-driven
marketing decisions across customer segmentation, digital
marketing, price optimization, campaign management, and
brand portfolio analysis (Wedel and Kannan 2016; Daven-
port and Harris 2017).
While the PROMETHEE method in marketing has
gained popularity, existing research has mainly focused on
assessing specific decision problems rather than providing

T. Tarnanidis et al.
methodological support for its implementation. Many pub -
lished applications report the final rankings of alternatives
but devote little attention to explaining which preference
functions were chosen or how threshold values were set. In
many instances, preference functions are utilized without
a clear rationale, whereas threshold parameters are chosen
subjectively or without regard to managerial concerns. This
absence of methodological direction generates multiple
challenges for researchers and practitioners. Initially, vary -
ing the selection of preference functions could diminish
comparability in marketing research. Furthermore, specify-
ing arbitrary thresholds restricts the transparency and repro-
ducibility of decision models. Lastly, a lack of explanation
for preference modeling diminishes practitioners’ confi -
dence in interpreting PROMETHEE outcomes, especially
when qualitative marketing factors such as brand percep -
tion, customer loyalty, or perceived quality are assessed.
Various approaches to addressing marketing decision
problems, such as AHP, TOPSIS, ELECTRE, and PRO -
METHEE, can be utilized. These methods vary in how they
portray stakeholder preferences and performance discrep -
ancies. AHP highlights hierarchical organization and com -
parative pairings, whereas TOPSIS assesses options based
on their proximity to optimal and counter-optimal scenar -
ios. Both ELECTRE and PROMETHEE are classification
methods within the outranking group and are particularly
applicable to evaluating alternatives under conflicting fac -
tors. (Ishizaka and Nemery 2013; Mardani et al. 2018).
PROMETHEE is especially pertinent to this study since its
preference functions, along with the associated thresholds,
enable the evaluator to explicitly express how variations in
criterion performance are converted into levels of prefer -
ence. However, this flexibility also raises a significant mod-
eling challenge: incorrect choices of preference functions
or thresholds can affect the resulting ranking. The role of
the current framework, therefore, does not lie in asserting
that PROMETHEE is universally superior to other MCDM
methods; rather, it offers structured guidance for one of its
most critical yet commonly overlooked stages: preference
function and threshold selection.
This methodological concern has grown in importance
within modern marketing analytics, where decision-making
integrates vast amounts of customer, transactional, digital,
and behavioral data with managerial expertise. While arti -
ficial intelligence and machine learning can offer predictive
capabilities and automate decision support, maintaining
explainability is essential for using analytical outputs in
managerial decision-making. Recent advancements in XAI
underscore the need to develop decision-support systems
whose recommendations are understandable and evalu -
able by decision-makers (Kostopoulos et al. 2024). PRO -
METHEE augments these data-driven strategies with an
explicit and traceable portrayal of criteria, weights, prefer -
ence functions, thresholds, and resultant preference streams.
So the suggested framework can be regarded as an inter -
pretable multi-criterion decision-support mechanism rather
than as a substitute for predictive analytics or AI. Accord -
ingly, future hybrid methods might integrate data-driven
forecasting with clear multi-criteria preference modeling.
The current research closes this methodological void
by redirecting attention from the use of PROMETHEE to
its application in marketing decision-making. Rather than
advancing another methodology, the paper develops a prac-
tical framework to help researchers and marketing practitio-
ners. The framework is expected to help them choose suitable
preference functions and threshold values based on the crite-
ria used in marketing evaluations. Specifically, this research
enhances the methodological application of PROMETHEE
in marketing by providing practical guidance for selecting
the six basic preference functions. It also offers systematic
instructions for determining indifference, preference, and
Gaussian thresholds and proposes a structured approach for
integrating PROMETHEE into marketing decision-making.
The proposed framework is implementation-independent
and can be applied using widely available PROMETHEE
software and analytical platforms. Popular tools for prac -
titioners include Visual PROMETHEE, Decision Lab, R,
Python, and Julia. This flexibility enables researchers and
practitioners to incorporate the framework into diverse deci-
sion-support environments without requiring specialized
software, thereby facilitating its adoption in both academic
research and professional marketing practice. Moreover, the
study incorporates a decision tree to aid in selecting suitable
preference functions. It highlights recurring modeling errors
and offers practical tips to enhance the quality, consistency,
and reliability of marketing decision models. By translating
the theoretical core of PROMETHEE into practical imple -
mentation guidelines, the suggested framework enhances
transparency, consistency, repeatability, and interpretabil -
ity in marketing decision-making. Thereby, it serves as a
useful guide for future research and professional practice.
Figure 1 summarizes the broader research implications of
the proposed framework. Beyond supporting the selection
of appropriate PROMETHEE preference functions and
threshold parameters, the framework can be applied across a
wide range of strategic and operational marketing decisions,
including product selection, pricing, customer analytics,
digital marketing, and marketing performance evaluation.
By providing a structured and reusable methodological
guide, the framework facilitates transparent, consistent, and
behaviorally meaningful marketing decision-making across
diverse application contexts.
The proposed framework provides systematic guid -
ance for selecting PROMETHEE preference functions and

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
thresholds across multiple marketing decision domains,
thereby improving transparency, consistency, and decision
quality. Table 1 outlines the progression of PROMETHEE
research, tracing its initial methodological foundation
through to its current use in marketing and decision support
systems.
Table 1 traces the progression of PROMETHEE research,
from its origins in foundational methodologies to its current
applications in marketing and decision-support systems.
It highlights the main objectives and contributions of key
studies while pinpointing the ongoing research areas that
need attention. The examination reveals that many exist -
ing studies have focused primarily on using PROMETHEE
for specific decision-making problems. Insufficient atten -
tion has been given to methodological guidance on select -
ing preference functions and threshold values. This divide
forms the basis of the framework proposed in this research,
which offers actionable recommendations for marketing
decision-making.
PROMETHEE preference modeling
Preference modeling lies at the heart of the PROMETHEE
methodology, as it dictates how variations in the per -
formances of competing alternatives are converted into
quantifiable preference levels (Oubahman et al. 2024).
PROMETHEE, instead of depending exclusively on fixed
criterion values, conducts pairwise comparisons of alterna -
tives and assesses the degree to which one option is deemed
preferable over another on each evaluation criterion (Jitta
et al. 2024). This method permits decision-makers to gauge
not only performance enhancements but also the strength of
their preferences for alternatives, thereby offering an adapt-
able and clear approach to integrate decision-maker pref -
erences into multicriteria assessments (Brans and Vincke
1985; Brans and Mareschal 1992; Behzadian et al. 2010;
Ishizaka and Nemery 2013; Greco et al. 2016; Taherdoost
and Madanchian 2023). For each criterion, the performance
disparity between two marketing options is then evaluated
using a chosen preference function. The computed prefer -
ence level ranges from 0 to 1, with 0 indicating no prefer -
ence, values in this range reflecting partial preference, and 1
indicating full preference. As a result, PROMETHEE cate -
gorizes minor, moderate, and significant performance varia-
tions instead of considering every numerical discrepancy as
equally significant.
Choosing an appropriate preference function is a crucial
initial step in the PROMETHEE methodology, as it dictates
how performance disparities among competing options
are interpreted throughout the decision-making process.
Using indifference, preference, and, as needed, Gaussian
thresholds, PROMETHEE allows decision-makers to dis -
cern minor performance disparities from those that signify
Fig. 1 Research implications and marketing application areas of the proposed PROMETHEE preference function framework

T. Tarnanidis et al.
genuine competitive gains. This versatility enables the com-
bination of objective performance metrics with supervisory
insights and professional expertise, ultimately resulting in
more transparent, robust, and behaviorally plausible assess-
ments. Therefore, the methodology is especially well-suited
for marketing decision-making, where frequent quantitative
performance metrics are often augmented by qualitative
evaluations, uncertainties, and subjective managerial judg -
ment (Behzadian et al. 2010; Cinelli et al. 2020; Coquelet et
al. 2025; Greco et al. 2016; Ishizaka and Nemery 2013; Lu
and Liu 2024; Taherdoost and Madanchian 2023). To depict
this process, Fig. 2 showcases the PROMETHEE prefer -
ence modeling framework. The illustration shows how per-
formance disparities between two options are converted into
standardized preference levels using a suitable preference
function before they are added to the comprehensive list of
alternatives.
As shown in Fig. 2, the PROMETHEE method trans -
lates performance differences into preference levels. The
procedure begins with evaluating two options based on a
designated marketing metric. The observed performance
difference is then assessed using a chosen preference func -
tion. The function converts the numerical disparity into a
standardized preference level ranging from 0 (no prefer -
ence) to 1 (complete preference). A pivotal aspect of the fig-
ure lies in integrating managerial judgment into quantitative
decision analysis. PROMETHEE allows decision-makers to
prioritize performance differences by selecting appropriate
Reference Research focus Main contribution Research gap addressed by
the present study
Brans and
Vincke
(1985)
Original
PROMETHEE
methodology
Introduced the PROMETHEE outranking
method and pairwise preference modeling
Does not provide marketing-
specific implementation
guidance
Brans and
Mareschal
(1992)
PROMETHEE
methodology
Comprehensive description of PRO-
METHEE methods, preference functions,
thresholds, and GAIA visualization
General methodological
framework without marketing
guidelines
Behza-
dian et al.
(2010)
Literature
review
Comprehensive review of PROMETHEE
methodologies and applications across
multiple disciplines
Focuses on applications rather
than practical guidance for
preference-function selection
Greco et al.
(2016)
Multicrite-
ria Decision
Analysis
Reviews advances in MCDA methodolo-
gies and decision-support approaches
Discusses PROMETHEE
within MCDA but does
not address marketing
implementation
Taher-
doost and
Madan-
chian
(2023)
PROMETHEE
procedures
Reviews PROMETHEE I and II pro-
cedures and illustrates their application
across business decision problems
Does not provide criterion-
specific guidance for selecting
preference functions
Tarnani-
dis et al.
(2023)
PROMETHEE
in the field of
marketing
Reviews applications of PROMETHEE
to marketing problems, including product
evaluation, customer satisfaction, and
retail decision-making
Recognizes the growing use
of marketing applications but
stresses the lack of guidance
for selecting preference func-
tions and thresholds
Applica-
tions of
PRO-
METHEE
(2023–
2025)
Decision-
making support
and analytical
tools
Expand the use of PROMETHEE to
include sustainability, business analyt-
ics, digital decision-support systems, and
hybrid MCDM methodologies
Applications are designed
primarily to solve individual
decision problems, not to
provide general implementa-
tion frameworks
Tarnani-
dis et al.
(2026a; b)
Marketing and
eco-friendly
practices
A systematic PRISMA review highlights
PROMETHEE’s use in market selection,
product development, pricing, retail site
selection, and customer satisfaction. It
pinpoints methodological gaps in market-
ing decision support
Asserts the necessity of a
structured methodological
framework for choosing
preference functions and
thresholds
Present
study
Guidelines for
methodological
considerations
in marketing
decisions
Creates a practical structure for choos-
ing PROMETHEE ranking functions
and threshold levels, incorporates a
decision-making tree, outlines a practical
framework, provides methodological sug-
gestions, and identifies typical modeling
errors for marketing scenarios
Offers practical implementa-
tion advice that augments
existing study-oriented
analyses
Table 1 Evolution of PRO-
METHEE research and the posi-
tioning of the present study

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
preference functions and setting sensitivity thresholds.
Therefore, minor variations are often deemed negligible,
while more significant disparities lead to increasingly pro -
nounced preference levels.
The data indicate that the intensity of preference is
influenced by the characteristics of the evaluation criterion
rather than by a universal pattern. Depending on the chosen
preference function, preference might increase instantly,
over time, or only when certain thresholds are met. This
flexibility allows PROMETHEE to better reflect realistic
managerial behavior compared to conventional additive
scoring methods. This process is notably useful in market -
ing decision-making because it incorporates numerous eval-
uation criteria. These include customer satisfaction, brand
image, perceived quality, customer loyalty, and advertis -
ing effectiveness, which cannot be understood exclusively
through numerical distinctions. By incorporating quantita -
tive performance indicators alongside expert assessments,
PROMETHEE delivers a transparent, adaptable, and com -
prehensible approach to evaluating competing marketing
options (Brans and Vincke 1985; Brans and Mareschal
1994; Cinelli et al. 2020).
Threshold concepts in marketing
Thresholds are indispensable parts of the PROMETHEE
methodology, as they determine how variations in criterion
performance are interpreted when evaluating alternatives
through pairwise comparisons (Tsiaras and Mantzou -
kas 2026; Schär et al. 2025). Not all observed differences
between competing marketing alternatives are significant
enough to warrant a preference. Minor variations may be
due to measurement inaccuracies, market fluctuations, or
typical consumer behavior, while significant disparities
may indicate a real competitive edge. By segregating minor,
moderate, and notable performance disparities, benchmark
levels offer a structured approach for integrating manage -
rial insights into the numerical assessment process (Brans
and Mareschal 2005; Behzadian et al. 2010; Coquelet et al.
2025).
Choosing the threshold values hinges on both the traits
of the assessment measure and the decision scenario. Set -
ting appropriate benchmarks ensures that the decision
model accurately captures realistic managerial perspectives
on when performance disparities become strategically sig -
nificant. Consequently, PROMETHEE generates decision
Fig. 2 PROMETHEE preference modeling process. Note: For each evaluation criterion, the PROMETHEE methodology converts the performance
disparity between two rival options into a corresponding preference level, thereby quantifying the decision-maker’s preference intensity

T. Tarnanidis et al.
models that are more transparent and behaviourally realistic
than those produced by methods that rely solely on numeri-
cal comparisons.
Three critical concepts in marketing decision-making are
particularly important: the indifference threshold (q), the
preference threshold (p), and the Gaussian threshold (s). The
preference thresholds in PROMETHEE’s pairwise compar-
ison framework play a vital role in quantifying meaning -
ful deviations to support robust managerial decisions. The
indifference threshold (q) denotes the greatest performance
difference between two options regarded as negligible for
practical purposes. Differences below this level are consid -
ered insignificant and thus do not generate a preference. For
marketing indicators that naturally vary or are subject to
measurement uncertainty, this threshold is especially useful.
A difference in customer satisfaction of less than 0.3 points
on a five-point scale, or a market share difference of less
than 1%, is unlikely to affect the choice between strategies
(Fiorentino 2025). Likewise, slight variations in customer
loyalty or website engagement could merely indicate typical
operational fluctuations.
The preference threshold (p) delineates the minimum
performance gap required for one option to be deemed
decidedly superior to another. Upon surpassing this limit,
full preference is granted. Threshold preferences are typi -
cally set based on strategic goals, industry standards, past
organizational performance, or managerial expertise. Exam-
ples include a 10% boost in market share, a 20% improve -
ment in advertising ROI (return on investment), or a notable
rise in customer lifetime value.
The Gaussian threshold (s) are suitable when preferences
change smoothly rather than abruptly beyond a set limit.
Rather than jumping straight from neutrality to full prefer -
ence, the Gaussian function captures a gradual increase in
the strength of preference as performance disparities widen.
This threshold is especially appropriate for qualitative mar-
keting parameters such as consumer perceptions, behavioral
patterns, brand image, brand equity, customer loyalty, per -
ceived quality, and emotional attachment. In these contexts,
preferences tend to develop gradually over time.
Determining appropriate threshold values is crucial in
PROMETHEE modeling, as they heavily influence the
preference model’s sensitivity. Thresholds ought not to
be chosen at random but should align with the features of
the evaluation standard and the managerial environment.
Various methods can be utilized for establishing threshold
levels:
Organizational knowledge and practical experience
form the basis of managerial expertise.
Using performance metrics from industry bench -
marks, aligning with standards set by competitors or
professional bodies.
Historical organizational data, which is based on pre-
vious marketing campaigns or business performance,
is used.
Expert agreement, derived from workshops or Delphi
studies conducted with marketing experts.
Testing sensitivity analysis, with various threshold val-
ues assessed to gauge the final ranking’ s robustness.
To maintain reproducibility and calibration, the threshold
selection process should be transparent and documented.
Initially, thresholds should be set using relevant evidence,
including historical data, observed variability, industry
standards, or predetermined managerial goals. Second,
the selected values must be validated through sensitivity
analysis to assess whether reasonable adjustments to the
thresholds significantly affect the resulting ranking. Mana -
gerial and expert judgments should not be relied upon as
the sole foundation for establishing preference functions
and thresholds. Instead, such an assessment ought to inte -
grate empirical and theoretically sound evidence, along with
the criterion's measurement attributes, historical records,
observed fluctuations, sectoral benchmarks, and sensitivity
tests.
The final threshold values, data source, and calibration
rule need to be reported explicitly. Thus, the calibration
procedure can be applied universally, whereas the specific
threshold values must be adjusted based on each applica -
tion's data and decision criteria. Given that performance dis-
crepancies can vary across sectors and operational contexts,
standard thresholds should not be uniformly applied from
one utilization to another. Instead, the same calibration pro-
cess should be repeated using context-specific information.
This integrated method minimizes reliance on subjective
judgment while maintaining the contextual understanding
necessary to assess meaningful differences in specific mar -
keting decisions.
Using these approaches ensures that the threshold levels
accurately reflect not only numerical distinctions but also
significant managerial differences. So, they improve the
clarity, reliability, and reproducibility of PROMETHEE
assessments. To illustrate the role of thresholds in prefer -
ence modeling, Fig. 3 integrates the three threshold con -
cepts alongside pertinent marketing applications. This
figure illustrates how threshold levels affect the conversion
of performance disparities into preference intensities. It

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
underscores their significance in encapsulating managerial
viewpoints through the PROMETHEE approach.
Figure 3 illustrates the distinct roles of the indifference,
preference, and Gaussian thresholds in modeling manage -
rial preferences. Rather than handling all performance dif -
ferences uniformly, the three threshold concepts enable the
decision-maker to determine when differences should be
overlooked, when they warrant full preference, and when
partial preference should be escalated progressively. The
analysis underscores that varying marketing standards
necessitate distinct behavior thresholds. Indicators such as
operational efficiency, financial performance, market share,
sales figures, and return on investment (ROI) often relate
to indifference and preference thresholds. This is because
notable performance bounds are often discernible.
On the other hand, behavioral and perceptual factors such
as customer loyalty, brand image, and perceived quality are
better captured through Gaussian thresholds, indicating the
progressive shift in consumer attitudes. A key takeaway
from the figure is that choosing the threshold represents a
strategic modeling decision, not just a mathematical one.
Optimal threshold levels avoid negligible performance dis -
parities caused by skewing assessments while ensuring that
pertinent strategic enhancements receive the appropriate
attention. As a result, defining the threshold enhances the
transparency, consistency, robustness, and managerial inter-
pretability of the decision model.
Selecting PROMETHEE preference functions
for marketing applications
Preference functions are the cornerstone of the PRO -
METHEE methodology, as they determine how differ -
ences in criterion performance are converted into degrees
of preference (Khan et al. 2025). Given that marketing
decision issues encompass both quantitative and qualita -
tive factors, with varying measurement scales and behav -
ioral traits, there is not a single preference function that can
adequately capture all possible decision scenarios. Con -
sequently, PROMETHEE offers six standard preference
functions, each tailored to represent a specific managerial
preference and decision pattern. Selecting an appropriate
preference function enhances the transparency, robustness,
and interpretability of marketing decision models. It ensures
that performance differences are consistently represented in
the measurement scale and the behavioral characteristics of
each evaluation criterion (Brans and Vincke 1985; Cinelli
et al. 2020; Coquelet et al. 2025; Ishizaka and Resce 2021).
Choosing an appropriate preference function hinges on the
attributes of the evaluation criterion, the decision-maker’s
Fig. 3 Threshold concepts in PROMETHEE for marketing decision-
making. Note: The figure depicts how performance differences among
competing marketing alternatives are transformed by the indifference
threshold (Q), the preference threshold (P), and the Gaussian thresh -
old (S) as a function of preference levels, promoting clear, uniform
decision-making within the PROMETHEE framework

T. Tarnanidis et al.
responsiveness to performance disparities, and the goals of
the marketing analysis. Selecting an appropriate function
ensures that decision-makers can implement an evaluation
model aligned with realistic managerial perspectives on the
differences among competing marketing strategies.
 ● Type I-VI
Type I- usual preference function
The Usual Preference Function is considered the most basic
preference model within PROMETHEE. It suggests that any
slight performance improvement automatically leads to full
preference, whereas the same level of performance elicits no
preference. Given that no intermediate preference levels are
taken into account, this function is especially well-suited for
binary or dichotomous criteria where the mere presence of a
characteristic is enough to determine superiority. Common
marketing considerations include product accreditation,
legal approval for market entry, availability of distribution
channels, promotional features, and adherence to environ -
mental or sustainability standards.
Type II: U-shape preference function
The U-Shape Preference Function includes an indifference
level, acknowledging that minor performance disparities
are typically insufficient to sway managerial choices. Pref -
erence is granted only after a discernible difference sur -
passes a predetermined threshold. This approach is suitable
for marketing factors susceptible to measurement errors or
inherent variability, such as customer satisfaction scores,
product quality assessments, conversion rates, response
times, and brand recognition metrics.
Type III: V-shape preference function
The V-Shape Preference Function posits that preferences
increase in tandem with performance discrepancies until
full preference is attained. Each enhancement increases
preference strength, making this model especially apt for
marketing metrics where small, strategic upgrades are
highly desirable. Key applications include sales growth,
advertising reach, digital marketing effectiveness, social
media engagement, lead capture, and website traffic.
Type IV: level preference function
The Level Preference Function specifies a halfway point
between indifference and complete preference for partial
preference. The function applies when slight variations are
recognized but not significant enough to warrant a total
preference. Typical applications of marketing evaluations
include qualitative measures like brand reputation, corpo -
rate image, service quality, product positioning, and cus -
tomer service performance.
Type V: linear preference function
The Linear Preference Function posits that preferences
increase in proportion to performance discrepancies until
full preference is attained. Simplicity and intuitive usability
are key factors in its frequent application as one of the most
commonly used preference functions in marketing. It is par-
ticularly suited to continuous quantitative variables such as
product price, sales revenue, marketing profit, market share,
return on investment (ROI), customer lifetime value (CLV),
and marketing expenditure.
Type VI: Gaussian preference function
The Gaussian Preference Function captures preferences as
a gradual, continuous progression rather than abrupt cutoffs
(Oliver 1999; Bai et al. 2024). As performance differences
increase, so does preference intensity, accurately reflecting
human perception and behavioral responses (Fournier 1998;
Hertzum 2025). Thus, this function is particularly suited for
psychological and perceptual marketing elements, such as
customer loyalty, brand trust, brand personality, consumer
perception, brand image, emotional connection, and cus -
tomer experience. Following the comparison of these pref -
erence functions’ characteristics.
Table 2 aggregates the six PROMETHEE preference
functions alongside their prominent marketing applica -
tions. The illustration shows how various functions reflect
different managerial decisions and underscores the need to
choose a preference model that aligns with the traits of each
evaluation factor.
Table 2 offers a comparative summary of the six PRO -
METHEE preference functions, illustrating that each func -
tion encapsulates a distinct managerial perspective on how
performance disparities should inform decision-making.
PROMETHEE allows decision-makers to adapt the prefer -
ence model to the behavioral traits of each marketing vari -
able rather than applying a uniform evaluation rule.
The data indicate that the Usual and U-Shape functions
are particularly suitable for binary criteria or for instances
where minor performance variations can be overlooked.
Conversely, the V-Shape and Linear models are more
appropriate for continuous quantitative data as preference
enhancement becomes more pronounced with improved
performance. The Level function serves as a midpoint
for partial preferences, ideal for qualitative assessments
that recognize slight differences but do not warrant full

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
preference. Ultimately, the Gaussian function provides the
most seamless depiction of managerial intuition and thus
stands out as especially advantageous for perceptual traits
whose assessment unfolds gradually.
This comparison underscores a key difference between
objective and subjective criteria for marketing. Financial
and operational metrics, such as revenue, market share, ad
efficiency, and return on investment, are typically depicted
using linear or V-shaped curves because they often indicate
quantifiable, steady progress. On the other hand, behavioral
and psychological elements, including customer loyalty,
brand trust, brand image, and consumer perception, are bet-
ter modeled using Gaussian or Level functions, which cap -
ture the progressive formation of consumer attitudes.
In summary, Table 2 shows that choosing an appropri -
ate preference function is a crucial modeling decision in
the PROMETHEE methodology. The selection of the pref -
erence function significantly affects how performance dis -
parities are assessed and ultimately determines the ranking
of marketing options by ensuring that the preference func -
tion aligns with each evaluation criterion. PROMETHEE
generates decision frameworks that are notably transparent,
behaviorally plausible, and operationally pertinent (Brans
and Vincke 1985; Brans and Mareschal 2005; Behzadian et
al. 2010).
Methodological guidelines for selecting
PROMETHEE preference functions
Choosing an appropriate preference function is one of the
most crucial steps in the PROMETHEE methodology, as
it defines how performance variations are interpreted and
converted into preference levels. The selection of a prefer -
ence function ought to align with the features of the evalua-
tion criterion, such as its measurement scale, the anticipated
behavior of the decision-maker, and the real importance
of discernible differences. Random selection of prefer -
ence functions or uniform application across criteria is not
recommended.
When making marketing decisions, various assessment
criteria necessitate distinct preference frameworks. Each
type of quantitative financial indicator, qualitative assess -
ment, behavioral measure, and binary variable exhibits
unique traits that affect how managerial preferences should
be modeled. Table 3 provides theoretically informed guide-
lines for selecting PROMETHEE preference functions
according to the measurement and behavioral characteristics
Preference
function
Preference behaviour Threshold(s) Suitable
marketing
criteria
Representative marketing
applications
Type I
Usual
Function
Immediate full preference
should be given whenever
one alternative excels over
another
None Binary
(Yes/No)
criteria
Product certification, legal
authorization, availability of
distribution channels, promotional
features, and compliance with
sustainability requirements
Type II –
U-shape
function
Small variations in perfor-
mance are ignored until
the indifference point is
reached, at which point
complete preference is
given
Indifference
threshold (q)
Quantita-
tive criteria
with mea-
surement
uncertainty
Customer happiness, product
excellence, site conversion rate,
customer response time, brand
recognition
Type III
– V-shape
function
As performance differ-
ences increase, prefer-
ence grows progressively
until it reaches complete
preference
Preference
threshold (p)
Continuous
perfor-
mance
indicators
Metrics such as sales growth, the
scope of advertising, social media
interaction, performance of digital
marketing campaigns, the creation
of leads, and web traffic
Type IV
– level
function
Synthesizes indifference,
partial inclination, and
full inclination based on
the extent of performance
disparities
Indifference
(q) and pref-
erence (p)
Ordinal and
qualitative
criteria
Brand image, corporate reputa-
tion, service excellence, product
placement, customer service
quality
Type V
– linear
function
Preference increases in
tandem with performance
discrepancies, up to the
point where complete
preference is attained
Indifference
(q) and pref-
erence (p)
Continuous
quantitative
variables
Product costs, total sales income,
profits from marketing efforts,
market share, return on investment
(ROI), customer lifetime value
(CLV), and marketing expenses
Type VI –
Gaussian
function
Performance differences
steadily foster smooth and
continuous preference
development
Gaussian
threshold (s)
Psycho-
logical and
perceptual
criteria
Customer allegiance, brand cred-
ibility, brand character, public
image, brand impression, emo-
tional bond, customer encounter
Table 2 PROMETHEE pref-
erence functions and their
applications in marketing
decision-making

T. Tarnanidis et al.
of common marketing criteria . The mappings presented in
Table 3 should be interpreted as theoretically grounded heu-
ristics, not as rigid connections between marketing variables
and preference functions. From a measurement standpoint,
variations in perceived and attitudinal constructs might indi-
cate both real differences and measurement inaccuracies.
Therefore, minor differences in scores should not always
be taken to indicate significant preferences. This facilitates
preference configurations, including indifference zones,
such as U-shaped, flat, or linear functions.
On the other hand, for sustained behavioral or financial
indicators, where incremental performance disparities might
signify progressively greater managerial benefits, V-shaped
or Linear preference configurations might be more appropri-
ate. Binary criteria inherently facilitate a Usual preference
structure since alternatives either meet or fail to meet the
stipulated condition. Hence, selecting a preference function
should take into account more than just the numerical value
of a criterion, including its measurement characteristics,
how score differences are interpreted, and the decision-mak-
er's sense of what constitutes a meaningful change (Brans
and Vincke 1985; Brans and Mareschal 2005; Behzadian et
al. 2010; Zapletal 2022).
Churchill ( 1979)’s paradigm was developed specifi -
cally for marketing and consumer behavior research. It is
one of the foundational frameworks for developing con -
sumer psychology constructs such as attitudes, satisfac -
tion, trust, loyalty, perceived value, and purchase intention.
It integrates psychometric principles into marketing mea -
surement. Similarly, the work of Nunnally and Bernstein
(1994) is the cornerstone of classical psychometric theory. It
explains measurement error, reliability, internal consistency,
and construct validity, concepts that underpin virtually all
consumer psychology scales and behavioral measurement
instruments. DeVellis ( 2003) provided a systematic psy -
chometric framework for item generation, content validity,
factor analysis, and reliability assessment. The procedures
are widely adopted in consumer psychology for construct -
ing latent constructs representing perceptions, beliefs, emo-
tions, and behavioral intentions.
Table 3 provides theoretically informed heuristic guide -
lines for selecting PROMETHEE preference functions
based on the characteristics of marketing criteria. These
Marketing
criterion
Measurement
scale
Recommended
preference
function
Rationale
Product
certification
Binary (Yes/No) Type I – usual Perfect for pass/fail assessments, any positive
disparity will automatically indicate a preference
Legal or regula-
tory approval
Binary Type I – usual Intermediate preference levels are unnecessary,
as compliance either occurs or does not
Customer
satisfaction
Ordinal (Likert
scale)
Type IV – level Slight variations ought to produce partial favor
before a full preference is confirmed
Brand
reputation
Ordinal Type IV – level Reputation is typically assessed through catego-
rized rankings rather than a range of values
Market share Continuous Type V – linear There is an increase in preference that aligns
with growing market share
Sales revenue Continuous Type V – linear Enhancements in finance typically carry manage-
rial significance in proportion to their size
Product price Continuous Type V – linear Slight cost variations gradually affect managerial
choices
Return on
investment
(ROI)
Continuous Type V – linear Properly, continuous financial benefits are aptly
reflected through proportional favor
Sales growth Continuous Type III
– V-shape
Each enhancement gradually aligns with mana-
gerial preferences
Advertising
reach
Continuous Type III
– V-Shape
Strengthening the campaign through continuous
audience reach is key
Social media
engagement
Continuous Type III
– V-shape
Increasing engagement is associated with
enhanced marketing performance
Brand image Perceptual Type VI
– Gaussian
Consumer attitudes change over time, not
suddenly
Brand trust Perceptual Type VI
– Gaussian
Trust accrues gradually and is most aptly illus-
trated by seamless shifts in preferences
Customer
loyalty
Behavioural Type VI
– Gaussian
Loyalty is exemplified by progressive behavioral
shifts over time, not by rigid criteria
Customer
experience
Perceptual Type VI
– Gaussian
Service quality improvements usually corre-
spond with better customer evaluations over time
Table 3 Theoretically informed
preference-function heuristics for
marketing criteria

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
mappings serve as practical guidance rather than as univer -
sal prescriptions.
The guidelines outlined in Table 3 serve as a handy deci-
sion-support tool for selecting preference functions based
on the features of the marketing evaluation criteria. Rather
than relying on capricious choices, decision-makers should
align the selection of the preference function with the under-
lying measurement scales and behavioral traits of each crite-
rion. This enhances the clarity, uniformity, and repeatability
of PROMETHEE implementations while guaranteeing that
preference modeling precisely mirrors managerial logic.
These methodological guidelines, which form the founda -
tion of the decision tree outlined in the subsequent section,
propose a systematic approach to selecting PROMETHEE
preference functions for marketing decisions.
 ● Common Mistakes
Identifying an effective preference function is essential, as
it shapes how performance differences are interpreted and
influences alternative rankings. Misleading outcomes and
reduced credibility can occur when preference functions or
threshold values are not appropriately selected. To uphold
the reliability and transparency of PROMETHEE applica -
tions in marketing, users must avoid frequent modeling mis-
takes. Studies analyzed the sensitivity of preference function
parameters and highlighted how inappropriate selection can
lead to rank reversal or unstable rankings (Lu et al., 2024;
Liu and Liu 2024). They proposed methods to determine
robust parameter ranges and underscored the need for care-
ful choice to maintain reliability and transparency.
Using a Gaussian function for binary criteria : This
Gaussian preference function is used for continuous vari -
ables, with preference increasing gradually. Using it under
binary criteria, such as product certification, legal authori -
zation, or distribution availability, is not suitable, as these
factors indicate distinct outcomes rather than gradual
changes. Binary criteria are more appropriately modeled
using the Type I (Usual) preference function.
Applying the same preference function to every evalu -
ation criterion : Various marketing benchmarks display
distinct measurement attributes and must not be conveyed
through a singular preference function. Financial metrics,
behavioral factors, qualitative evaluations, and binary stan -
dards necessitate varied preference layouts. Assigning the
same function to all criteria simplifies the decision model
excessively and could lead to an inaccurate final ranking.
Confusing the indifference threshold (q) with the prefer -
ence threshold (p) : A frequent error involves treating the
two thresholds as if they were interchangeable. The indif -
ference threshold delineates the greatest disparity deemed
insignificant, while the preference threshold marks the point
at which one option clearly stands out as superior. Mis-spec-
ifying these thresholds could substantially affect the degrees
of preference and the resulting rankings.
Ignoring the measurement scale of the evaluation cri -
terion: Preference functions ought to be chosen based on
the scale used for measuring the criterion. Binary variables,
continuous numerical values, ordinal rating scales, and per-
ceptual constructs necessitate distinct preference functions.
Failing to account for these variations diminishes the behav-
ioral accuracy of the assessment model.
Selecting threshold values arbitrarily : Threshold val -
ues must not be selected without justification. Rather, they
should be sourced from managerial experience, historical
organizational data, industry standards, expert agreement,
or sensitivity analysis. Arbitrarily setting the threshold
decreases transparency, reproducibility, and credibility in
the PROMETHEE analysis.
Although the PROMETHEE methodology offers flexibil-
ity, the trustworthiness of the final decision model depends
heavily on the selection of preference functions and thresh-
old values. Inaccurate specifications can lead to inconsis -
tent preference modeling, skewed rankings, and diminished
transparency in decision-making. Table 4 summarizes com-
mon errors in selecting preference functions and thresholds
in marketing contexts, along with the possible outcomes and
suggested approaches to avoid them. By adhering to these
suggestions, scholars and professionals can enhance the
reliability, uniformity, repeatability, and real-world applica-
bility of PROMETHEE-inspired marketing decision mod -
els, thereby boosting the value of these guidance tools.
To conclude, selecting appropriate preference functions
and threshold values is crucial for creating reliable, behav -
iorally accurate PROMETHEE models. Erecting these fre -
quent modeling mistakes enhances the clarity, uniformity,
and reliability of marketing decision-aid systems, while
Table  4 Common modeling errors and recommended practices for
selecting PROMETHEE preference functions
Common mistake Consequence Recommended
practice
Gaussian for two-
category variables
Preference model-
ing that goes beyond
realism
Use type I (usual)
Uniform application
across all metrics
Distorted rankings Match the function
to the criterion
type
Confusing q and p Inappropriate prefer-
ence level
Define thresholds
independently
Ignoring measurement
scales
Behavior does not
align with the data
Select functions
based on data type
Arbitrary threshold
values
Poor reproducibility Employ expert
analysis, sensitiv-
ity testing, and his-
torical benchmarks

T. Tarnanidis et al.
ensuring that evaluation outcomes accurately reflect both
the criteria’s features and managerial judgment.
 ● Decision Tree
Identifying an appropriate preference function is vital for
constructing a reliable PROMETHEE model, as it directly
affects how performance differences among competing
marketing alternatives are interpreted and transformed into
preference degrees. The selection of the preference function
ought to align with the properties of the evaluated criterion,
the decision environment, and the decision-maker’s respon-
siveness to variations in performance.
Figure 4 presents a decision tree that outlines a systematic
approach to selecting the optimal PROMETHEE preference
function. It assists both researchers and practitioners based
Fig. 4 Decision tree for selecting
PROMETHEE preference func-
tions in marketing decision-making

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
on the criteria used in marketing evaluations. By facilitat -
ing a series of logical decisions, the framework diminishes
subjective bias, enhances modeling accuracy, and increases
the transparency and reliability of marketing decision aids
(Brans and Mareschal 2005).
Figure 4 illustrates a decision tree intended to help
researchers and practitioners choose the best PROMETHEE
preference function for marketing decisions. The model
shows that choosing a preference function is not a consis -
tent procedure; instead, it should be guided by the features
of the assessment criterion, the type of available data, and
how decision-makers interpret variations in performance.
By converting methodological principles into a system -
atic sequence of decision stages, the illustration provides a
handy tool for enhancing the predictability and clarity of
PROMETHEE model creation.
The initial step in the decision-making process is to rec -
ognize the attributes of the assessment standard. Binary
or dichotomous variables (such as product certification or
regulatory compliance) align with the Usual (Type I) pref -
erence function because the slightest positive difference is
sufficient to declare a preference. Ordinal and qualitative
criteria (such as service quality ratings or brand reputa -
tion categories) require functions that represent intermedi -
ate levels of preference. They make the Level (Type IV) or
Gaussian (Type VI) functions more appropriate, depending
on the degree of gradualness in managerial judgment.
For continuous variables, a decision tree identifies dis -
tinctions among criteria, separating those for which minor
performance variations are insignificant from those for
which every improvement holds strategic importance. Cri -
teria such as market share, sales revenue, advertising reach,
and return on investment are generally represented by the
Linear (Type V) or V-Shape (Type III) functions because
preference increases progressively with performance. Con -
versely, when small variations should initially be ignored
before preference develops, the U-Shape (Type II) function
provides a more realistic representation.
The figure also emphasizes the importance of threshold
selection. The choice of the preference function determines
how analysts set appropriate indifference (q), preference
(p), or Gaussian (s) thresholds, guided by informed mana -
gerial judgment, historical data, benchmarking, or sensitiv -
ity analysis. This methodical approach minimizes arbitrary
decision-making and ensures that preference modeling
accurately reflects both the criterion's assessment character-
istics and managerial objectives.
Overall, Fig. 4 demonstrates that selecting an appropriate
preference function is a strategic modeling decision rather
than a purely mathematical exercise. By systematically link-
ing marketing evaluation criteria to appropriate preference
functions and threshold concepts, the proposed decision tree
enhances the transparency, robustness, interpretability, and
reproducibility of PROMETHEE-based marketing deci -
sion models, thereby providing practical guidance for both
researchers and practitioners.
To demonstrate the practical application of the proposed
decision tree, Appendix A applies the framework to a real-
world marketing decision involving seven social media
platforms and seven performance criteria. The application
illustrates how criterion characteristics and the managerial
interpretation of performance differences guide preference-
function selection and threshold specification, and then
proceeds to the complete PROMETHEE II analysis and
sensitivity assessment.
Proposed PROMETHEE framework for
marketing decision-making
Utilizing the PROMETHEE methodology in marketing
decision-making requires a methodical, organized approach
that combines quantitative evaluation metrics with manage-
rial insights. General marketing decisions usually consider
several, and often conflicting, factors, such as financial
results, customer satisfaction, brand image, and competitive
market position. Therefore, a clear decision-making model
is crucial to guarantee that all pertinent criteria are con -
sistently assessed and that the ultimate ranking of options
accurately reflects organizational goals.
The proposed framework organizes the PROMETHEE
methodology into seven sequential stages. Each step in
the process helps build a comprehensive decision-support
model, from defining the decision issue to assessing and
ranking various marketing options. The framework is suf -
ficiently flexible to accommodate a wide range of mar -
keting applications, including product evaluation, pricing
strategy selection, advertising campaign assessment, mar -
ket segmentation, distribution channel selection, and brand
management.
Step 1. Define Marketing Alternatives : The procedure
begins by identifying the marketing options to be evaluated.
Based on the type of decision, these options might include
rival offerings, marketing efforts, pricing methodologies,
sales channels, target audiences, promotional schemes, or
brand promotions. Clearly outlining the options forms the
basis for the subsequent assessment procedure.
Step 2. Select Evaluation Criteria : The next step is to
choose the evaluation metrics that most accurately reflect
the objectives of the decision issue. Generally, marketing
decisions necessitate both quantitative and qualitative con -
siderations. Typical evaluation criteria include market share,
sales growth, customer satisfaction, profitability, advertising
effectiveness, return on investment (ROI), customer lifetime

T. Tarnanidis et al.
value (CLV), brand awareness, brand equity, customer loy-
alty, and corporate reputation.
Step 3. Assign Criterion Weights: Because evaluation cri-
teria seldom contribute equally to organizational objectives,
assign weights to reflect their relative importance. Weights
for criteria might be established through managerial judg -
ment, expert consensus, customer preferences, or formal
methods such as the Analytic Hierarchy Process (AHP),
entropy weighting, or direct rating methods (Roszkowska
et al. 2024). Correct weighting is essential to ensure the
assessment accurately reflects the organization’s priorities.
Step 4. Select Preference Functions: For each evaluation
criterion, the most fitting PROMETHEE preference function
is chosen based on the data characteristics and the decision-
maker’s behavior. Quantitative indicators such as sales, rev-
enue, or market share are generally represented using Linear
or V-Shape preference functions. In contrast, qualitative and
behavioral criteria, such as brand image, customer loyalty,
and consumer perception, are better modeled using Level or
Gaussian preference functions. These are well explored in
recent modified versions of PROMETHEE (Zapletal 2022).
Step 5. Determine Threshold Values : After selecting the
preference functions, set the specific threshold values. Based
on the chosen preference function, these can include the
indifference level (q), the preference level (p), or the Gauss-
ian level (s). These benchmarks gauge the decision model’s
sensitivity, separating negligible performance disparities
from those that warrant partial or full preference. Choosing
an appropriate threshold facilitates the direct incorporation
of managerial expertise into quantitative assessments.
Step 6. Calculate Preference Flows : The sixth stage
involves conducting pairwise comparisons for all marketing
options to determine the PROMETHEE preference flows.
Three flow metrics are acquired:
Positive preference flow (Φ⁺): Measures the extent
to which an alternative dominates competing
alternatives.
Negative preference flow (Φ⁻): Measures the extent to
which competing alternatives dominate an alternative.
Net preference flow (Φ): Represents the overall per -
formance of each alternative by combining the posi -
tive and negative preference flows.
These preference flows offer a thorough evaluation of the
comparative advantages and disadvantages of each market-
ing option.
Step 7. Rank Marketing Alternatives : In the final phase,
the options are evaluated based on their net preference
flows. Options with greater net favorable transfers are
deemed more attractive because they outperform compara -
ble options on the chosen assessment metrics. The resulting
ranking gives marketing managers a clear, fair, and justifi -
able foundation for choosing the best marketing strategy.
As a summary, Fig. 5 illustrates the proposed PRO -
METHEE framework for marketing decision-making. The
framework delineates the seven sequential phases required
to establish a PROMETHEE decision model and shows
how performance data and managerial insights are inte -
grated throughout the assessment cycle.
As depicted in Fig. 5, the proposed PROMETHEE
framework for marketing decision-making is presented as
a holistic decision-support system. It encompasses problem
definition, preference modeling, multicriteria assessment,
and managerial interpretation. Rather than viewing PRO -
METHEE merely as a ranking tool, the framework demon -
strates how the methodology can be applied systematically
throughout the marketing decision-making process, from
problem definition to strategy execution and performance
tracking. The framework begins with problem structuring,
involving decision-makers in defining the marketing prob -
lem, selecting competing alternatives, and setting evalua -
tion criteria aligned with the organization's strategic goals.
Until this point, both quantitative and qualitative criteria
have been specified, along with their optimization directions
(maximization or minimization). This ensures that the deci-
sion model accurately reflects the marketing context.
The focus shifts to preference modeling, which forms the
methodological heart of the framework. Preference func -
tions suitable for the PROMETHEE method are chosen
based on the characteristics of each evaluation criterion,
with indifference, preference, or Gaussian thresholds set
as necessary. The purpose of this stage is to consistently
interpret performance differences aligned with managerial
perspectives and the behavioral traits of the marketing vari-
ables being assessed. According to the preference modeling
framework, the framework then moves on to data prepara -
tion and evaluation, during which the performance matrix is
developed, criterion values are normalized as required, and
criterion weights are determined by assigning values based
on expert judgment or other weighting methods. These
operations lay the analytical groundwork for the ensuing
PROMETHEE calculations.
The PROMETHEE analysis phase converts pairwise
performance disparities into preference levels and deter -
mines the positive, negative, and net preference currents
for every marketing option. These flow metrics offer a thor-
ough evaluation of the comparative merits and drawbacks
of various strategies, forming the foundation for the ulti -
mate selection of alternatives. The final stage emphasizes
managerial interpretation and implementation. Rather than
ending with a numerical ranking, the framework encourages

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
decision-makers to interpret the results, conduct sensitiv -
ity analyses to assess model robustness, derive manage -
rial implications, and monitor the implementation of the
selected strategy. Incorporating feedback through sensitiv -
ity analysis made it evident that marketing decision-making
is a cyclical process in which preference functions, thresh -
old settings, and criterion weightings can be adjusted as new
data emerge.
In summary, the suggested framework broadens the
conventional use of PROMETHEE by combining meth -
odological advice with practical decision assistance. By
combining problem structuring, preference modeling, com-
putational analysis, and managerial interpretation within
a single coherent framework, it provides researchers and
practitioners with a transparent, systematic, and reproduc -
ible approach for supporting complex marketing decisions
involving multiple and often conflicting evaluation crite -
ria (Brans and Vincke 1985; Brans and Mareschal 2005;
Behzadian et al. 2010; Ishizaka and Nemery 2013; Cinelli
et al. 2020).
Empirical demonstration of the proposed
framework
To evaluate the practical applicability of the proposed seven-
step framework beyond a hypothetical setting, Appendix A
presents a complete empirical application using a real-world
marketing dataset. The application deliberately incorporates
heterogeneous marketing criteria with different measure -
ment and behavioral characteristics, enabling the proposed
preference-function selection guidelines and threshold-set -
ting procedure to be evaluated under a realistic multicriteria
decision environment. The analysis follows all seven stages
of the proposed framework, from problem formulation and
criterion specification to preference-function selection,
threshold determination, PROMETHEE flow computation,
and final ranking. Sensitivity analyses of criterion weights
and threshold parameters are additionally conducted to
assess the robustness of the resulting rankings. Sensitiv -
ity analyses of criterion weights, threshold parameters,
and alternative preference-function specifications are also
conducted to assess the robustness and consistency of the
resulting rankings. Examining different specifications rela -
tive to the baseline model and assessing potential changes in
ranking help demonstrate how choices in preference func -
tions and parameters can significantly affect the strategic
recommendations produced. The application thus demon -
strates the framework's practical feasibility, highlighting the
significance of systematic preference modeling in complex
marketing decisions.
Fig. 5 Proposed PROMETHEE framework for marketing decision-making

T. Tarnanidis et al.
Discussion
Advancing the methodological application of
PROMETHEE in marketing
This study enhances the marketing analytics literature by
redirecting the focus from applying PROMETHEE to solve
individual marketing problems to methodological imple -
mentation of the PROMETHEE approach. Researchers
have previously used PROMETHEE in specific decision
contexts, including supplier selection, pricing, retail loca -
tion evaluation, advertising campaign assessment, customer
satisfaction measurement, and product portfolio manage -
ment. However, they have typically offered scant guidance
concerning the choice of preference functions and thresh -
old values. As a consequence, many published applications
depend on subjective parameter selections that are infre -
quently explained or systematically documented.
The suggested framework closes this methodological
void by providing structured instructions for selecting the
six standard PROMETHEE preference functions based on
the traits of the marketing evaluation criteria. Rather than
treating preference modeling exclusively as a mathematical
task, the framework argues that preference functions should
be selected based on the evaluated criterion's behavioral
traits. This approach enhances the consistency, clarity, and
repeatability of marketing decision models.
Implications for marketing analytics
With the rise in customer, transactional, digital, and behav-
ioral data, marketing has evolved into a more analytical
profession (Petrescu and Krishen 2023). Modern market -
ing decisions often necessitate the concurrent assessment
of financial performance, customer satisfaction, brand
strength, market share, environmental sustainability, cus -
tomer lifetime value, and digital engagement. Their crite -
ria vary widely across measurement scales and behavioral
traits, making it particularly crucial to select an appropriate
preference function.
The suggested framework enables marketing analysts
to develop PROMETHEE models that more accurately
capture the inherent characteristics of each assessment cri -
terion. Persisting financial metrics may require Linear or
V-shaped preference models. In contrast, perceptual vari -
ables such as customer loyalty, brand image, and perceived
quality are better captured by Gaussian or Level functions.
As a result, the structure enhances the behavioral accuracy
of marketing decision models while minimizing the risk of
unsuitable parameter choices.
Improving transparency and reproducibility
A primary constraint of current PROMETHEE implemen -
tations is the inadequate rationale behind methodological
decisions. Various studies detail the ultimate selection but
offer scant justification for the chosen preference models or
threshold levels. A lack of transparent methodologies ham -
pered the reproducibility of published research and hindered
the comparability of studies.
By including practical selection criteria, threshold rec -
ommendations, a decision model, and an overview of com -
mon modeling pitfalls, the suggested framework aims to
enhance the transparent reporting of PROMETHEE appli -
cations. Explicit justification of methodological choices by
researchers allows for better replication, comparison, and
refinement of existing marketing decision models in future
studies.
Integration with emerging marketing technologies
This proposed framework also aligns with current trends
in marketing analytics, artificial intelligence, and decision
support systems. Predictive analytics, machine learning,
customer intelligence, and business analytics are crucial for
supporting strategic decisions in contemporary marketing
(Zulaikha et al. 2025). Despite the substantial data gener -
ated, managerial input is indispensable for assessing strate -
gic options.
PROMETHEE offers a significant addition to data-based
analytical techniques by integrating quantitative informa -
tion with expert evaluations via preference functions and
level modeling. As a result, the suggested framework could
facilitate explainable decision-support systems by making
the logic behind marketing recommendations clearer and
easier to understand. This trait becomes especially crucial
as entities seek analytical tools that not only offer precise
recommendations but also transparent, justifiable decision-
making pathways.
Theoretical contributions
This research enhances the marketing analytics and MCDM
literature by applying the PROMETHEE methodology in
contexts beyond its conventional role as a decision sup -
port tool. While earlier research has mainly applied PRO -
METHEE to specific marketing issues, there has been
relatively little effort to elucidate how preference models
and threshold settings should be determined. This inves -
tigation closes the methodological void by proposing a
systematic framework that links the features of marketing
assessment criteria to suitable PROMETHEE preference
functions and threshold concepts.

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
A subsequent theoretical advancement combines mar -
keting measurement theory with PROMETHEE preference
modeling. The framework indicates that various marketing
criteria, such as binary, ordinal, continuous, behavioral,
and perceptual variables, are subject to different preference
structures. By linking measurement scales to the choice of
preference functions, this research offers a theoretical basis
for enhancing the behavioral accuracy of marketing deci -
sion models that use PROMETHEE.
The paper also enriches the growing literature on trans -
parent marketing analytics by highlighting transparency
in model construction. Currently, the proposed framework
replaces the treatment of preference functions and threshold
values as arbitrary parameters with explicit methodologi -
cal guidance for their selection. This improves the inter -
pretability, reliability, and replicability of PROMETHEE
implementations and helps build more transparent decision-
making assistance systems.
Finally, the study contributes to methodological research
in marketing by presenting an integrated implementation
framework that combines preference modeling, threshold
determination, methodological guidelines, a decision tree,
and a practical workflow for applying PROMETHEE in
marketing decision-making. Taken together, these com -
ponents create a comprehensive reference system that can
support future empirical investigations and methodological
advancements in marketing analytics.
Practical contributions
From a managerial perspective, the suggested framework
provides marketing executives with a systematic approach
to applying the PROMETHEE methodology in practical
decision-making. Rather than requiring extensive exper -
tise in multicriteria decision analysis, managers can follow
the proposed implementation framework. This framework
helps them identify suitable evaluation criteria, assign cri -
terion weights, select appropriate preference functions,
determine threshold values, and rank competing marketing
alternatives transparently and systematically.
Simplifying one of the most complex steps in PRO -
METHEE implementation is facilitated by following meth-
odological guidelines. This step involves choosing the right
preference function for each criterion, which can be further
supported by constructing a decision tree. By aligning pref-
erence functions with the attributes of marketing metrics,
experts can avoid common modeling errors and improve
the reliability of their analyses. This alignment also helps
generate rankings that more faithfully reflect managerial
perspectives.
The framework is applicable across a broad range of stra-
tegic and operational marketing decisions. Therefore, the
suggested approach provides a flexible decision-making aid
that can be tailored for organizations across various sectors
and market dynamics.
The suggested framework encourages broader use of
data-driven marketing by clearly linking quantitative mar -
keting analytics to managerial skills. As organizations
increasingly employ business intelligence, customer ana -
lytics, artificial intelligence, and machine learning to sup -
port decision-making, the transparent preference modeling
process proposed in this study can enhance explainability,
facilitate managerial acceptance of analytical models, and
increase confidence in strategic marketing decisions (Basu
et al. 2025; Spais and Chryssochoidis 2025).
Managerial implications
The insights from this research show that the PROMETHEE
method offers marketing leaders a clear, methodical way
to assess complex strategic options. PROMETHEE differs
from conventional scoring methods by recognizing that not
all performance differences are equally significant. It also
enables managers to incorporate their expertise by choosing
preference functions and threshold values.
Choosing suitable preference functions enhances the
behavioral realism of marketing decision models by ensur -
ing that various assessment criteria are represented accord -
ing to their inherent traits. Quantitative criteria, such as
cost, revenue, market share, and return on investment, can
be modeled using linear or V-shaped preference functions.
In contrast, qualitative constructs, such as brand image, cus-
tomer loyalty, and consumer perception, are better repre -
sented by level or Gaussian preference functions.
Further refining the threshold improves decision-making
by helping managers avoid overreacting to minor perfor -
mance variations while still highlighting significant, stra -
tegically relevant progress. As a result, decision models
became more robust, transparent, and aligned with real
managerial reasoning.
The PROMETHEE methodology applies to many mar -
keting decisions. These include advertising campaign selec-
tion, product portfolio evaluation, pricing strategy, market
segmentation, distribution channel selection, customer
relationship management, and brand management. By com-
bining objective performance indicators with managerial
insights, PROMETHEE enables more reliable and transpar-
ent strategic decision-making in increasingly competitive
commercial settings.
Limitations and future research
The research has some notable limitations that must be rec-
ognized. While an actual marketing dataset substantiates

T. Tarnanidis et al.
the suggested framework, and its reliability is scrutinized
through sensitivity analysis, the empirical implementation
is limited to a single decision scenario. The framework has
not yet undergone validation across diverse industries, orga-
nizations, and marketing conditions. Additional empirical
evaluations are required to determine its general applicabil-
ity in various marketing settings.
Second, the choice of preference functions and threshold
values remains influenced by the specific decision scenario.
While this paper provides practical guidelines for matching
preference functions to different marketing criteria, the final
selection should always reflect organizational objectives,
managerial expertise, industry characteristics, and the avail-
ability of reliable performance data. The threshold selec -
tion remains context dependent. Therefore, it is advisable
to regard threshold levels as context-dependent variables
rather than fixed, general guidelines.
Additionally, marketing decisions are made amid uncer -
tainty, fluctuating market conditions, and evolving con -
sumer trends. Although the PROMETHEE methodology
accommodates managerial judgment through preference
functions and thresholds, it does not explicitly address
uncertainty. It includes uncertainty arising from incomplete
information, rapidly changing market environments, or
evolving customer preferences. Future investigations might
thus examine the incorporation of fuzzy PROMETHEE,
stochastic methods, or interval-valued preference modeling
to capture uncertainty in marketing decisions better (Bakas
et al. 2025). Importantly, the framework does not replace
managerial expertise.
From a practical standpoint, implementing PRO -
METHEE may face challenges related to data requirements,
parameter definition, and model complexity. Analytical
teams need to establish weight criteria, preference func -
tions, and appropriate threshold values, and these decisions
may require reliable historical data, sensitivity analyses,
and input from decision-makers. Specifying parameters can
become more challenging as the number of criteria, options,
and stakeholders increases. At the same time, differences
among decision-makers might complicate the adjustment of
weights and thresholds. Therefore, PROMETHEE should
not be regarded as universally preferable to other MCDM
techniques. AHP might be more suitable for scenarios
where the main goal is to establish a hierarchical deci -
sion structure and determine priorities via simple pairwise
comparisons, especially when the quantity of criteria and
options is not excessively large. TOPSIS could be preferred
when decision-makers need a straightforward ranking based
on proximity to an ideal solution and do not require specific
preference functions for each criterion or indifference and
preference thresholds. ELECTRE might be more appropri -
ate for scenarios that emphasize ranking superiority, veto
conditions, or contexts in which high scores on certain cri -
teria should not entirely offset poor scores on others. Hence,
the selection between PROMETHEE and alternative mul -
ticriteria decision-making methods should depend on the
structure of the decision problem, the availability of data,
the intended portrayal of management preferences, and the
analytical complexity that decision-makers can practically
handle.
Finally, future studies should empirically validate the
proposed framework across different marketing contexts,
including advertising campaign evaluation, pricing strat -
egy selection, brand management, customer relationship
management, digital marketing, and market segmentation.
Comparative studies involving other multicriteria decision-
making methods, such as the Analytic Hierarchy Process
(AHP), Technique for Order Preference by Similarity to
an Ideal Solution (TOPSIS), and ELimination Et Choix
Traduisant la REalité (ELECTRE), would also provide
valuable insights into the relative strengths and limitations
of the proposed approach (Jitta et al. 2024; Zhou and Chen
2025; Oubahman et al. 2024). Furthermore, integrating
PROMETHEE with state-of-the-art technologies such as
artificial intelligence, machine learning, customer analytics,
and transparent decision-support systems holds consider -
able promise for future marketing research. Further studies
could investigate the concurrent use of PROMETHEE with
currently available statistical software packages, such as
SPSS, Stata, R, SAS, and Python-based analytical platforms,
enabling researchers to integrate robust statistical analyses
with various criterion-based decision-making methods.
This integration would enable more detailed data analysis,
enhance the understanding and validation of results, and
support more robust, data-driven managerial decisions.
Future work may automate threshold estimation using
machine learning, integrate Bayesian optimization, and
combine PROMETHEE with LLM-based decision sup -
port. Eventually, further investigations might examine the
integration of PROMETHEE with explainable artificial
intelligence (XAI), business intelligence systems, and mar -
keting decision-support tools to provide automated, clear
assessment mechanisms for strategic marketing decisions
in today’s more data-focused settings (Kostopoulos et al.
2024).
Conclusions
Marketing decision-making increasingly depends on bal -
ancing conflicting objectives by integrating quantitative
and qualitative criteria. This study demonstrated that the
PROMETHEE methodology provides an effective multicri-
teria decision-support framework that integrates objective

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
performance measures with subjective managerial prefer -
ences using preference functions and threshold values.
Choosing suitable preference functions and threshold
parameters is a crucial step in the modeling process, as
these components determine how performance disparities
are assessed and mapped to preference levels. By disregard-
ing minor discrepancies and focusing on crucial enhance -
ments, PROMETHEE produces decision frameworks that
better align with actual managerial practices than standard
assessment techniques.
The suggested marketing decision-making model dem -
onstrates how PROMETHEE can be systematically applied
to issues such as advertising campaign selection, pricing
strategies, brand assessments, customer relationship man -
agement, and market segmentation. The illustrative case
study also demonstrates the method’s flexibility in support-
ing marketing decisions that involve numerous, often con -
flicting criteria.
Further research might expand this study by incorporat -
ing PROMETHEE with cutting-edge analytical techniques,
such as machine learning, artificial intelligence, customer
insights, predictive marketing frameworks, and live deci -
sion-assisting systems (Basu et al. 2025; Spais and Chrysso-
choidis 2025). Such changes hold the promise to boost both
the precision and flexibility of marketing decision models,
allowing organizations to better adapt to the swiftly evolv -
ing marketplace.
Overall, PROMETHEE offers a clear, adaptable, and
behaviorally grounded framework for assisting in marketing
decision-making. By combining rigorous quantitative anal -
ysis with managerial expertise, the methodology contributes
to more rational, explainable, and strategically informed
marketing decisions (Brans and Vincke 1985; Brans and
Mareschal 2005; Behzadian et al. 2010).
The suggested framework provides marketing research -
ers and practitioners with a structured approach for select -
ing PROMETHEE preference functions and threshold
values based on the characteristics of the marketing evalu -
ation criteria. By translating the theoretical foundations of
PROMETHEE into practical implementation guidelines,
the framework enhances the transparency, consistency, and
reproducibility of multicriteria decision-making in market -
ing. It establishes a foundation for future empirical and AI-
supported marketing applications.
Appendix A
Real-data application: social media platform
selection in Greek grocery retail
This appendix showcases the practical application of the
proposed seven-step PROMETHEE framework using a
real-world marketing dataset from the Greek grocery retail
industry. Empirical data are derived from a previously pub-
lished study on the effectiveness of social media advertising
in supermarkets, in which 27 managers from supermarkets
operating in Northern Greece assessed social media per -
formance metrics and their effectiveness (Tarnanidis et al.
2026b).
The rationale for employing this empirical dataset is not
to replicate the primary conclusions of the original research,
but to illustrate how the preference-function selection
framework we developed in this article can be applied when
decision-makers face diverse marketing considerations.
Specifically, the application demonstrates the journey from
defining the problem and specifying criteria to choosing a
preference function. It helps set thresholds, perform PRO -
METHEE II computations, and interpret results for man -
agement, all of which are decision-making concerns in
choosing the best social media platform for supermarket
marketing communications. Supermarket managers need to
allocate their limited marketing funds across various digital
channels, each offering distinct advantages in financial suc-
cess, sales impact, lead generation, customer engagement,
audience reach, cost-effectiveness, and customer insights.
Given that no single metric captures the full effectiveness
of marketing efforts, the issue is reframed as a multicriteria
decision problem.
Step 1: Definition of the decision problem and alternatives.
The managerial decision is formulated as follows:
Which social media channel delivers the best com -
prehensive performance for supermarket marketing
when evaluated based on financial returns, conver -
sion rates, engagement levels, reach breadth, cost-
effectiveness, and customer feedback?
Seven commonly utilized social media platforms serve as
the decision options:
(A1): Facebook
(A2): Instagram

T. Tarnanidis et al.
(A3): YouTube
(A4): TikTok
(A5): X (formerly Twitter)
(A6): LinkedIn
(A7): Pinterest
These options symbolize competing pathways through
which supermarket managers can direct marketing commu-
nication expenditures.
Step 2: Identification and characterization of evaluation
criteria.
The assessment is based on seven criteria. These crite -
ria were derived from the original empirical study, which
combined 34 social media performance indicators into con-
ceptually separate higher-order dimensions according to
managerial significance and decision relevance:
(C1): Return on Investment (ROI)
(C2): Revenue Contribution
(C3): Lead Generation
(C4): Engagement
(C5): Reach
(C6): Cost Efficiency
(C7): Feedback and Electronic Word-of-Mouth
(eWOM) Quality
Benefit-focused normalized indices represent each cri -
terion, so a higher score indicates better performance. The
scores range from 0 to 100, enabling comparisons across
diverse marketing performance metrics.
Step 3 : Construct the Real-Data Decision Matrix
(Table 5).
Step 4: Assign Criterion Weights.
In the PROMETHEE II model, the seven criteria were
given equal weightings. All criteria were given a weight of
1.00, implying equal significance. Each criterion contrib -
utes 14.29% to the total weight. Therefore, each of the seven
criteria is weighted equally when determining the overall
evaluation of the social media platforms (Table 6).
The weight signifies the criterion's significance in the
PROMETHEE methodology. Given that each of the seven
criteria carries equal weight of 1.00, they are deemed equally
important. After normalization, each criterion accounts for
approximately 14.29% of the overall evaluation (100% ÷ 7).
This ensures that the ultimate ranking is not skewed by giv-
ing undue weight to any single factor.
Step 5a: Application of the Decision Tree to the Empiri-
cal Criteria.
The selection of preference functions for the empirical
application was based on the logic depicted in Fig. 4. The
criteria were initially assessed based on their measurement
characteristics and how performance discrepancies should
be interpreted.
ROI, Revenue Impact, Lead Flow, Engagement Lev -
els, Reach Metrics, and Cost-Effectiveness are illustrated
using consistent quantitative performance indicators. Based
on the decision tree, these criteria were given a V-shaped
preference function, as enhancing performance differences
Table 5 Real-data performance matrix for social media platform evaluation
Alternative ROI Revenue Leads Engagement Reach Cost efficiency Feedback
Facebook 78.0 71.8 67.6 63.2 78.2 66.0 65.7
Instagram 71.1 72.3 63.4 74.6 73.5 61.5 67.7
YouTube 61.4 67.9 54.6 58.2 69.3 57.6 64.9
TikTok 63.2 67.9 56.8 79.9 77.9 59.9 61.4
X (Twitter) 49.2 51.6 42.4 45.5 56.7 52.2 51.3
LinkedIn 46.8 50.1 53.9 41.2 42.7 52.1 62.4
Pinterest 40.5 42.1 37.7 49.0 56.0 59.6 48.3
The application contains 7 alternatives × 7 criteria = 49 empirical performance values. All criteria are benefit criteria (Max). Higher scores
indicate better performance. Scores are normalized indices on a 0–100 scale
Table 6 Criterion weights for the PROMETHEE II evaluation model
Code Criterion PROMETHEE
weight
Per-
centage
(C1) Return on investment (ROI) 1.00 14.29%
(C2) Revenue contribution 1.00 14.29%
(C3) Lead generation 1.00 14.29%
(C4) Engagement 1.00 14.29%
(C5) Reach 1.00 14.29%
(C6) Cost efficiency 1.00 14.29%
(C7) Feedback and eWOM Quality 1.00 14.29%
Total 7.00 100%

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
steadily reinforces the inclination towards the more effi -
cient platform. The Level preference function was chosen
for Feedback and eWOM Quality because this metric bet -
ter captures subjective, qualitative aspects: small variations
might be insignificant, moderate disparities could suggest a
partial inclination, and significant differences may highlight
a clear preference.
The practical implementation thus shows how the deci -
sion tree transitions from the features of a marketing crite -
rion to selecting an appropriate PROMETHEE preference
function, prior to determining the corresponding threshold
parameters (Table 7).
Step 5b: Preference Function.
To evaluate how PROMETHEE II perceives performance
differences on two social media platforms, preference func-
tions were selected. For quantitative criteria, including ROI,
Revenue Contribution, Lead Generation, Engagement,
Reach, and Cost Efficiency, a V-shaped preference func -
tion was utilized. With this mechanism, minor variations
produce a mild inclination, but that preference strengthens
progressively as the disparity between the systems grows.
When the preference threshold (p) is exceeded, the more
effective platform is regarded as the preferred option. The
Level preference function was used to assess feedback and
eWOM quality, as this criterion incorporates more qualita -
tive and perceptual data. Therefore, small differences are
considered negligible, moderate disparities signal partial
preference, and larger differences indicate a clear inclina -
tion. These preference functions enable PROMETHEE II to
differentiate between slight and significant platform perfor-
mance differences, rather than assigning equal importance
to every numerical gap.
Step 5c: Threshold determination.
Thresholds were employed to ascertain when meaningful
differences existed in the performance of two social media
platforms. Thresholds were not uniformly applied but were
instead set according to the standard deviation (σ) of each
criterion's performance scores. This enables the thresholds
to reflect the actual variation observed in the data. For the
six quantitative criteria, only the preference threshold (P)
is required when using the V-shaped preference function. It
was calculated as:
p =0 .25σ
A slight divergence between two systems yields a modest
inclination, whereas preference tends to grow more substan-
tial as the gap widens. When the difference reaches a certain
level, the better-performing platform is considered clearly
preferred. For the quality of feedback and earned word of
mouth (eWOM), which employs the Level preference func-
tion, two thresholds were utilized:
q =0 .10σ, p =0 .25σ
Here, q denotes the indifference threshold, capturing a
difference that is too slight to be considered noteworthy.
The p-value serves as the significance cutoff and denotes
substantial differences. The difference between q and p indi-
cates an intermediate level of preference (Table 8).
Specifically, the ROI preference threshold stands at 3.16.
For ROI, the preference threshold is 3.16. Preference for
the better-performing platform increases as the ROI differ -
ence grows. A difference of 3.16 points or more indicates a
clear preference. If the performance margin is 3.16 points
or greater, the superior platform is definitely favored. The
principle holds for Revenue Contribution, Lead Generation,
Engagement, Reach, and Cost Efficiency. For assessment
of feedback and electronic word of mouth (eWOM) qual -
ity, differences of up to 0.69 are deemed negligible, differ -
ences ranging from 0.69 to 1.73 indicate an intermediate
Table  7 Application of the preference-function decision tree to the
social media criteria
Criterion Criterion
characteristic
Decision-tree logic Selected
function
ROI Continuous
quantitative
There is a growing pro-
gression in the differences
V-shape
Revenue
contribution
Continuous
quantitative
Increasing disparities are
becoming increasingly
significant
V-shape
Lead
generation
Continuous
quantitative
Each beneficial change
enhances preference
V-shape
Engagement Continuous
quantitative
Increasing differences
progressively matter
V-shape
Reach Continuous
quantitative
Every improvement con-
tributes to preference
V-shape
Cost
efficiency
Continuous
quantitative
Progressive differences
have become increasingly
significant
V-shape
Feedback/
eWOM
quality
Perceptual/
qualitative
composite
Minor, moderate, and
obvious distinctions can
be discerned
Level
Table 8 Preference functions and criterion-specific threshold param -
eters for the PROMETHEE II model
Code Criterion Preference
Function
Std.
Dev.
(σ)
q p
C1 Return on investment
(ROI)
V-shape 12.63 – 3.16
C2 Revenue contribution V-shape 11.35 – 2.84
C3 Lead generation V-shape 9.87 – 2.47
C4 Engagement V-shape 13.61 – 3.40
C5 Reach V-shape 12.41 – 3.10
C6 Cost efficiency V-shape 4.63 – 1.16
C7 Feedback and eWOM
quality
Level 6.92 0.69 1.73
q represents the indifference threshold, and p represents the prefer -
ence threshold. A dash (–) means that the threshold is not required for
that preference function

T. Tarnanidis et al.
preference, and differences exceeding 1.73 signify a clear
preference. Overall, this method enables PROMETHEE II
to distinguish between minor discrepancies that carry mini-
mal significance and more substantial distinctions that influ-
ence the evaluation of social media platforms.
Step 6: PROMETHEE Preference-Flow Calculation.
The decision model utilized Visual PROMETHEE for
implementation. Seven evaluation criteria were used to
compare each social media platform with the others. The
performance discrepancies were translated into preference
scores using the prescribed preference algorithms and lim -
its, and these scores were subsequently aggregated to deter-
mine the overall preference one platform holds over another.
Three preference flows were calculated for each platform.
The positive flow (Φ +) indicates how strongly a platform
performs relative to the other alternatives, while the nega -
tive flow (Φ-) indicates how strongly the other alternatives
perform relative to it. The net preference flow (Φ) combines
these two measures:
Φ=Φ + − Φ−\
An increased net flow indicates superior performance.
Using the net preference flows, PROMETHEE II estab -
lished the final ranking for the seven social media plat -
forms. The published analysis revealed that Facebook led
the pack, followed by Instagram, TikTok, and YouTube,
with X (Twitter), LinkedIn, and Pinterest occupying lower
positions. Facebook's prominent position underscores its
robust performance across various metrics, notably finan -
cial health, audience size, and operational efficiency. Insta -
gram did well, too, especially in terms of engagement and
consumer response, whereas TikTok excelled primarily due
to its superior engagement and reach.
Step 7: Ranking and Managerial Interpretation.
The visual representation in Fig. 6 shows the final rank -
ing computed using PROMETHEE II. Using PROMETHEE
principles, the ordering is established by the net preference
flow (Φ), which reflects the equilibrium between the positive
and negative flow preferences derived from pairwise com -
parisons of options (Brans and Mareschal 2005). Facebook
achieves the strongest overall preference position and ranks
first, followed by Instagram, TikTok, and YouTube, while
X (Twitter), LinkedIn, and Pinterest occupy the lower posi-
tions. Thus, the figure demonstrates how the PROMETHEE
preference-modeling principles, explored theoretically, are
applied to produce an interpretable ranking in an empirical
marketing context (Tables 9, 10).
The positive flow (Φ +) shows how strongly a platform
performs against the other alternatives, whereas the nega -
tive flow (Φ−) represents how strongly the other alternatives
perform against it. The net flow (Φ) quantifies this disparity
and ultimately determines the final PROMETHEE II clas -
sification. With a net flow of 0.7833, Facebook was placed
Table 9 Criterion-level preference flows for the social media platforms
Platform ROI Revenue Leads Engagement Reach Cost efficiency Feedback/eWOM
Facebook 1.0000 0.7917 1.0000 0.3333 0.8583 1.0000 0.5000
Instagram 0.6667 0.8750 0.6667 0.6667 0.3333 0.6250 1.0000
YouTube 0.0776 0.1667 − 0.1083 0.0000 0.0000 − 0.3333 0.5000
TikTok 0.2557 0.1667 0.3333 1.0000 0.8083 0.2250 − 0.1667
X (Twitter) − 0.3813 − 0.3750 − 0.6667 − 0.6667 − 0.4417 − 0.8250 − 0.6667
LinkedIn − 0.6187 − 0.6250 − 0.2250 − 1.0000 − 1.0000 − 0.8417 − 0.1667
Pinterest − 1.0000 − 1.0000 − 1.0000 − 0.3333 − 0.5583 0.1500 − 1.0000
Values greater than zero signify superior performance on a criterion, while values less than zero indicate inferior performance. These represent
criterion-based preference flow values, not the final PROMETHEE II net flows (Φ), which are used to determine the overall ranking
Fig. 6 PROMETHEE II ranking

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
first. Following Instagram closely, a net flow of 0.6905 was
observed. TikTok ranked third (Φ = 0.3746), followed by
YouTube (Φ = 0.0432). With negative net flows, the remain-
ing platforms ranked sixth for LinkedIn (Φ=−0.6396),
seventh for Pinterest (Φ=−0.6774), and fifth for Twitter
(Φ=−0.5747).
Therefore, the final PROMETHEE II ordering is:
Facebook > Instagram > TikTok > YouTube > X (Twit-
ter) > LinkedIn > Pinterest.
Sensitivity analysis and rank-reversal
assessment
In the final evaluation phase, a sensitivity analysis was
also conducted to assess how variations in model assump -
tions affect the resulting platform ranking. Specifically, the
assessment evaluates modifications to weight adjustments
for criteria and preference-function definitions, intended to
determine whether these changes result in the options being
ranked in the opposite order (Fig. 7).
A sensitivity analysis was carried out to determine
whether the PROMETHEE II ranking remains consistent as
the criteria's importance varies. This step is crucial, as the
weights assigned to criteria can vary with managerial pri -
orities. A model considered robust should produce a stable
ranking when weights change slightly.
The analysis can be concisely stated as:
w′j = wj (1 ± 0.20)
where w′j is the original weight of criterion j, and w′j is the
weight after a 20% increase or decrease.
The sensitivity graph shows how the final PROMETHEE
II ranking changes as the weight assigned to a criterion is
adjusted. The horizontal axis denotes the weight assigned to
the criterion, whereas the vertical axis reflects the net flow
(Φ) obtained through PROMETHEE II. An increased net
flow suggests a higher-ranking option.
For the baseline model, each of the seven criteria was
assigned an approximate weight.
1
7 =0 .1429 = 14. 29%
At this weight, the ranking is:
Facebook > Instagram > TikTok > YouTube > X >
LinkedIn > Pinterest
According to the sensitivity graph, Facebook continues to
hold the top spot with an original weight of around 14.29%,
followed by Instagram, TikTok, and YouTube. Similarly, X
(Twitter), LinkedIn, and Pinterest remain in the lower posi-
tions. This shows that the ranking remains consistent with
the criterion's baseline weight.
To determine if the final PROMETHEE II ranking is
responsive to variations in the weight of each criterion, a
±20% adjustment can be made independently to each crite -
rion. In the base model, each of the seven criteria is deemed
equally important, assigning to each a normalized weight
of:
1
7 =0 .1429 = 14. 29%
For the sensitivity analysis, the weight of each criterion
was escalated and diminished by 20% of its initial value
w′j = wj (1 ± 0.20)
Therefore, the minimum and maximum weights are:
14.29% × 0.80 = 11 .43%
And
14.29% × 1.20 = 17 .15%
Modifying the weight of one criterion led to proportional
adjustments in the weights of the other six, maintaining the
total at 100%. Each criterion was altered individually, with
the same seven options—performance data, preference func-
tions, and thresholds—remaining unchanged (Table 11).
For instance, in the ROI sensitivity test, the initial ROI
weight of 14.29% is initially decreased to 11.43% and sub -
sequently raised to 17.15%. After each modification, the
net flows calculated by PROMETHEE II are recalculated.
Following the same procedure, separate applications were
conducted for Revenue Contribution, Lead Generation,
Engagement, Reach, Cost Efficiency, and Feedback/eWOM
Quality.
Table 10 PROMETHEE II preference flows and final ranking of social
media platforms
Rank Platform Positive flow
(Φ+) Negative flow (Φ−) Net flow
((Φ)
1 Facebook 0.8607 0.0774 0.7833
2 Instagram 0.8333 0.1429 0.6905
3 TikTok 0.6353 0.2607 0.3746
4 YouTube 0.4845 0.4413 0.0432
5 X (Twitter) 0.1872 0.7619 −0.5747
6 LinkedIn 0.1429 0.7824 −0.6396
7 Pinterest 0.1429 0.8202 −0.6774

T. Tarnanidis et al.
The resulting scores are contrasted with the baseline
ranking.
Facebook > Instagram > TikTok > YouTube > X (Twit-
ter) > LinkedIn > Pinterest.
If the ranking remains the same after ±20% adjustments,
the outcome can be deemed stable or resilient to minor vari-
ations in the weight of criteria. When two platforms swap
places, a reversal of rankings occurs. Within a sensitivity
graph, this observation occurs when lines for two alterna -
tives intersect within the tested range of weights.
Ranking changes occur when the weight of a criterion
shifts, flipping the positions of two options. For example,
suppose initially:
Φ( Facebook) > Φ( Instagram)
Facebook outranks Instagram in the ranking. If the
weight of a criterion changes and the new results become:
Φ( Instagram) > Φ( Facebook)
A rank reversal has occurred.
Table 11 Weight-sensitivity scenarios for the PROMETHEE II model
Scenario Criterion varied Baseline − 20% + 20%
S1 ROI 14.29% 11.43% 17.15%
S2 Revenue contribution 14.29% 11.43% 17.15%
S3 Lead generation 14.29% 11.43% 17.15%
S4 Engagement 14.29% 11.43% 17.15%
S5 Reach 14.29% 11.43% 17.15%
S6 Cost efficiency 14.29% 11.43% 17.15%
S7 Feedback and eWOM quality 14.29% 11.43% 17.15%
Fig. 7 Sensitivity of the PROMETHEE II ranking to changes in criterion weight

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
The point where two lines cross in the sensitivity graph
indicates a possible rank reversal. If the lines fail to inter -
sect within the specified weight limits, their relative order
remains unchanged. In the sensitivity graph presented, there
is no notable crossing near the initial weight of 14.29%,
suggesting stability in the primary ranking within that area.
Another use of sensitivity analysis is to check if rankings
change when the structure of the decision model is modi -
fied. For example, incorporating a new criterion could alter
the significance of the existing ones, since the weights need
to be redistributed. If the original seven criteria are equally
weighted, each receives:
1
7 =0 .1429 = 14. 29%
Including an eighth equally weighted criterion would
lead to each criterion receiving:
1
8 =0 .1250 = 12. 50%
The newly introduced criterion also provides data for the
comparison. As a result, flow changes may occur, and some
platforms might swap ranking positions. Such a modifica -
tion is not necessarily an error; it suggests that the extra
criterion offers data that influences the overall decision.
Alternatively, removing a criterion, adjusting its weight, or
redefining its preference function can influence preference
flows and might result in rank reversal. Thus, a sensitivity
analysis is a useful way to assess whether the final ordering
is overly reliant on certain modeling decisions.
The threshold sensitivity can be assessed in the same
manner. To assess changes in net flows and platform rank -
ings, baseline threshold values should be compared with
lower and higher threshold settings. If two platforms
exchange positions after the thresholds are modified, a rank
reversal occurs, indicating that the final decision is sensi -
tive to the specification of the thresholds. Conversely, if the
ranking stays the same, the outcome indicates resilience to
variations in reasonable thresholds.
Mathematically, adjustments to the threshold values influ-
ence the preference levels, which in turn affect the net flows
(Φ); a rank reversal occurs when the order between two plat-
forms is altered due to a different threshold specification.
The findings show that the ranking remains consistent
with reduced threshold levels. Nevertheless, raising the
thresholds resulted in an inversion of ranks, with LinkedIn
outperforming X. Under the base model, X ranks fifth and
LinkedIn sixth, but under the higher-threshold specification,
LinkedIn jumps to fifth place while X drops to sixth. This
outcome indicates that the choice of thresholds affects the
results of PROMETHEE II, especially for alternatives with
nearly identical overall performance.
The findings indicate that the platform's ranking stays
consistent regardless of the four preference-function specifi-
cations. No reversal in ranking is observed compared to the
baseline model (S1), suggesting that the ordering remains
solid regardless of the preference-function selections con -
sidered. Stability, however, does not signify that preference-
function selection becomes irrelevant, as other functions
can still influence individual preference levels and overall
preference shifts, even when the final ranking of alternatives
stays constant. Conversely, the threshold-sensitivity analy -
sis presented in Table 12 resulted in a reversal of rankings
for X and LinkedIn when using the higher threshold. When
combined, Tables 12 and 13 show that, for this empirical
Table 12 Threshold sensitivity and rank-reversal assessment
Scenario Threshold
specification
Resulting ranking Rank
reversal
T1 baseline V-shape: p=0.25σ;
Level: q=0.10σ;
p=0.25σ
Facebook > Instagram
> TikTok > YouTube
> X > LinkedIn >
Pinterest
–
T2 lower
thresholds
V-shape: p=0.15σ;
Level: q=0.05σ;
p=0.15σ
Facebook > Instagram
> TikTok > YouTube
> X > LinkedIn >
Pinterest
No
T3 higher
thresholds
V-shape: p=0.50σ;
Level: q=0.20σ;
p=0.50σ
Facebook > Instagram
> TikTok > YouTube
> LinkedIn > X >
Pinterest
Yes
σ denotes the criterion-specific standard deviation. For V-shape cri -
teria, only the preference threshold p is required, whereas the Level
function uses both the indifference threshold q and the preference
threshold p
Table  13 Preference-function sensitivity scenarios for the PRO -
METHEE II model
Scenario Model specification Resulting ranking Rank
rever-
sal vs.
S1
S1
(Baseline)
V-shape for six quantita-
tive criteria; Level for
Feedback/eWOM
Facebook > Insta-
gram > TikTok
> YouTube > X
> LinkedIn >
Pinterest
–
S2 V-shape applied to all
seven criteria
Facebook > Insta-
gram > TikTok
> YouTube > X
> LinkedIn >
Pinterest
No
S3 Engagement changed
from V-shape to Level
Facebook > Insta-
gram > TikTok
> YouTube > X
> LinkedIn >
Pinterest
No
S4 Feedback/eWOM changed
from Level to V-shape
Facebook > Insta-
gram > TikTok
> YouTube > X
> LinkedIn >
Pinterest
No

T. Tarnanidis et al.
application, the overall ranking is more influenced by the
calibration of the threshold than by the various preference-
function specifications that were examined. The finding car-
ries practical importance since it emphasizes the necessity
of accurately calibrating and validating threshold param -
eters when using PROMETHEE II in marketing decision
contexts.
Author contributions Conceptualization, T.T., B.M., J.P., and M.V .;
methodology, T.T., B.M., and J.P.; validation, J.P., M.V . and T.T.; for-
mal analysis, T.T., J.P. and B.M.; investigation, T.T. and J.P.; resources,
T.T.; data curation, V .K.M., T.T. and B.M.; writing-original draft prep-
aration, T.T., V .K.M. and B.M.; writing-review and editing, T.T., J.P.
M. V ., and B.M.; visualization, V .K.M. B.S; supervision, B.M., J.P. and
B.S..; project administration, T.T. All authors have read and agreed to
the published version of the manuscript.
Summary statement of contribution This study offers a methodologi-
cal framework that integrates PROMETHEE theory with marketing
practice to incorporate preference modeling into marketing decision-
making. It advances the literature by establishing practical guidelines
for selecting the six standard PROMETHEE preference functions and
determining appropriate threshold values, while aligning marketing
evaluation criteria with preference model characteristics. Additionally,
the research proposes a decision tree, an implementation framework,
and best-practice guidelines that improve the clarity, uniformity, and
interpretability of multi-criteria marketing assessments. The suggested
framework provides researchers and practitioners with a useful guide
for implementing PROMETHEE in intricate marketing scenarios, in -
tegrating various quantitative and qualitative factors, which lays the
groundwork for future collaboration with marketing analytics, busi -
ness intelligence, and explainable artificial intelligence.
Funding Open access funding provided by HEAL-Link Greece. This
research received no external funding.
Data availability The empirical data used in the illustrative application
were derived from the authors’ previously published study (Tarnanidis
et al. 2026b) and are reproduced and reanalyzed here for the method -
ological purpose of demonstrating the proposed PROMETHEE pref -
erence-function selection framework. The data required to reproduce
the illustrative analysis are reported in Appendix A.
Declarations
Competing interests The authors declare that they have no competing
interests.
Consent to participate Not applicable.
Consent for publication Not applicable. This manuscript does not con-
tain any personal data.
Ethical approval Not applicable.
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
Bai, T., X. Wang, Z. Zhang, W. Song, B. Wu, and J.-Y . Nie. 2024. GPR-
OPT: A practical Gaussian optimization criterion for implicit rec-
ommender systems. Information Processing & Management  61
(1) : 103525. https:/ /doi.or g/10.10 16/j. ipm.2023.103525.
Bakas, T., C. Papadopoulos, D. Latinopoulos, I. Kagalou, and M.
Spiliotis. 2025. Extended intuitionistic fuzzy PROMETHEE II
group decision making for Mediterranean basin management.
Water Resources Management 39 (9): 4243–4260.  h t t  p s : /  / d o  i . o  r
g / 1 0 . 1 0 0 7 / s 1 1 2 6 9 - 0 2 4 - 0 3 9 9 9 - 2     .
Basu, R., Md. . N. . Aktar, and S. Kumar. 2025. The interplay of arti -
ficial intelligence, machine learning, and data analytics in digital
marketing and promotions: A review and research agenda. Jour-
nal of Marketing Analytics 13 (2): 267–287.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0
5 7 / s 4 1 2 7 0 - 0 2 4 - 0 0 3 5 5 - 6     .
Behzadian, M., R. B. Kazemzadeh, A. Albadvi, and M. Aghdasi. 2010.
PROMETHEE: A comprehensive literature review on methodolo-
gies and applications. European Journal of Operational Research
200 (1): 198–215. https:/ /doi.or g/10.10 16/j. ejor.2009.01.021.
Belton, V ., and T. J. Stewart. 2002. The multiple criteria problem. In
Multiple criteria decision analysis: An integrated approach , ed.
V . Belton and T. J. Stewart, 13–33. Springer US.  h t t  p s : /  / d o  i . o  r g / 1
0 . 1 0 0 7 / 9 7 8 - 1 - 4 6 1 5 - 1 4 9 5 - 4 _ 2     .
Biswas, T., A. Ishizaka, A. Majumder, B. Mandal, S. Dey, S. Mukher-
jee, Aniket Baishya, Sahely Kanthal, Samrat Ghosh, Anwe -
sha Mandal, Riti Chatterjee, Soumik Ray, Snehasish Bhunia,
Swarnali Duary, Suvendu Bhattacharjee, Pradeep Mishra, and
S. K. Acharya. 2025. The PROMETHEE-GAIA: A multicriteria
decision-making method for identifying best conservation agri -
cultural practices. Soil and Tillage Research 245 : 106315.
Brans, J. P., and B. Mareschal. 1992. Promethee V: MCDM problems
with segmentation constraints. INFOR: Information Systems and
Operational Research 30 (2): 85–96.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 0 3 1
5 5 9 8 6 . 1 9 9 2 . 1 1 7 3 2 1 8 6     .
Brans, J.-P., and B. Mareschal. 1994. The Promcalc & Gaia decision
support system for multicriteria decision aid. Decision Support
Systems 12 (4): 297–310.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / 0 1 6 7 - 9 2 3 6 ( 9 4
) 9 0 0 4 8 - 5     .
Brans, J.-P., and B. Mareschal. 2005. Promethee methods. In Multiple
criteria decision analysis: State of the art surveys, ed. J. Figueira,
S. Greco, and M. Ehrogott, 163–186. Springer New York.  h t t  p s : /  /
d o  i . o  r g / 1 0 . 1 0 0 7 / 0 - 3 8 7 - 2 3 0 8 1 - 5 _ 5     .
Brans, J. P., and P. Vincke. 1985. Note—A preference ranking organ-
isation method. Management Science 31 (6): 647–656.  h t t  p s : /  / d o
i . o  r g / 1 0 . 1 2 8 7 / m n s c . 3 1 . 6 . 6 4 7     .
Churchill, G. A., Jr. 1979. A paradigm for developing better measures
of marketing constructs. Journal of Marketing Research  16 (1):
64–73. https:/ /doi.or g/10.11 77/00 2224377901600110.
Cinelli, M., M. Kadziński, M. Gonzalez, and R. Słowiński. 2020. How
to support the application of multiple criteria decision analysis?
Let us start with a comprehensive taxonomy. Omega 96 : 102261.
https:/ /doi.or g/10.10 16/j. omega.2020.102261.
Coquelet, B., G. Dejaegere, and Y . De Smet. 2025. Evaluating the Pro-
methee ii ranking quality. Algorithms 18 (10) : 597.  h t t  p s : /  / d o  i . o
r g / 1 0 . 3 3 9 0 / a 1 8 1 0 0 5 9 7     .

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
Davenport, T., and J. Harris. 2017. Competing on analytics: Updated,
with a new introduction: The new science of winning . Harvard
Business Press.
Dekimpe, M. G., and D. M. Hanssens. 2024. Persistence modeling in
marketing: Descriptive, predictive, and normative uses. Austral-
asian Marketing Journal 32 (2): 91–97.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 7 7 / 1
4 4 1 3 5 8 2 2 3 1 2 2 2 3 1 1     .
DeVellis, R. F. 2003. Scale development: Theory and applications. 2nd
ed. Sage Publications.
Dwivedi, A., and McDonald, B. 2025. A model of brand price premi -
umness and its marketing outcomes. Journal of Marketing Theory
and Practice, 1–22.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 1 0 6 9 6 6 7 9 . 2 0 2 5 . 2 5 4 4
6 7 1
Ferrari, R. 2015. Writing narrative style literature reviews. Medical
Writing 24 (4): 230–235.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 7 9 / 2 0 4 7 4 8 0 6 1 5 Z .
0 0 0 0 0 0 0 0 0 3 2 9     .
Fiorentino, A. 2025. Beyond boundaries: A multidisciplinary approach
to understand the relationship between customer satisfaction
and behavior in services. Italian Journal of Marketing  2025 (1):
51–69. https:/ /doi.or g/10.10 07/s4 3039-025-00108-y.
Fournier, S. 1998. Consumers and their brands: Developing relation -
ship theory in consumer research. Journal of Consumer Research
24 (4): 343–353. https:/ /doi.or g/10.10 86/20 9515.
France, S. L., and S. Ghose. 2019. Marketing analytics: Methods,
practice, implementation, and links to other fields. Expert Sys -
tems with Applications  119:456–475.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . e
s w a . 2 0 1 8 . 1 1 . 0 0 2     .
Gao, K., T. Liu, D. Yue, et al. 2023. An integrated spherical fuzzy
multi-criterion group decision-making approach and its applica -
tion in digital marketing technology assessment. International
Journal of Computational Intelligence Systems 16:125.  h t t  p s : /  / d o
i . o  r g / 1 0 . 1 0 0 7 / s 4 4 1 9 6 - 0 2 3 - 0 0 2 9 8 - 3     .
Grant, M. J., and A. Booth. 2009. A typology of reviews: An analysis
of 14 review types and associated methodologies. Health Infor-
mation & Libraries Journal 26 (2): 91–108.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1
1 1 / j . 1 4 7 1 - 1 8 4 2 . 2 0 0 9 . 0 0 8 4 8 . x     .
Greco, S., J. Figueira, and M. Ehrgott. 2016. Multiple criteria decision
analysis, vol. V ol. 37. New York: springer.
Gupta, Y ., and F. M. Khan. 2024. Role of artificial intelligence in
customer engagement: A systematic review and future research
directions. Journal of Modelling in Management  19 (5): 1535–
1565. https:/ /doi.or g/10.11 08/JM 2-01-2023-0016.
Hanssens, D. M. 2018. The value of empirical generalizations in mar-
keting. Journal of the Academy of Marketing Science 46 (1): 6–8.
https:/ /doi.or g/10.10 07/s1 1747-017-0567-0.
Hertzum, M. 2025. Understanding preference: A meta-analysis of user
studies. International Journal of Human-Computer Studies 195 :
103408. https:/ /doi.or g/10.10 16/j. ijhcs.2024.103408.
Ishizaka, A., and P. Nemery. 2013. Multicriteria decision analysis:
Methods and software. John Wiley & Sons.
Ishizaka, A., and G. Resce. 2021. Best-worst PROMETHEE method
for evaluating school performance in the OECD’s PISA project.
Socio-Economic Planning Sciences 73 : 100799.  h t t  p s : /  / d o  i . o  r g / 1
0 . 1 0 1 6 / j . s e p s . 2 0 2 0 . 1 0 0 7 9 9     .
Jitta, M. R., S. Radhakrishnan, and V . K. Manda. 2024. Applica -
tions of classical, pairwise, and hierarchical MCDM techniques
in marketing management. In Advances in marketing, customer
relationship management, and e-services , ed. T. Tarnanidis, J.
Papathanasiou, V . Ismyrlis, and V . Kittu. Manda, 49–74. IGI
Global.
Khan, M. R., K. Ullah, Z. Ali, E. Rak, D. Pamucar, and Y . Shang.
2025. The MCDM approach using preference ranking organi -
zation method for enrichment evaluation (PROMETHEE) for
intuitionistic fuzzy sets with AHP-based weight information.
International Journal of Fuzzy Systems .  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 7 /
s 4 0 8 1 5 - 0 2 5 - 0 2 1 4 2 - 6     .
Kostopoulos, G., G. Davrazos, and S. Kotsiantis. 2024. Explainable
artificial intelligence-based decision support systems: A recent
review. Electronics 13 (14) : 2842.  h t t  p s : /  / d o  i . o  r g / 1 0 . 3 3 9 0 / e l e c t
r o n i c s 1 3 1 4 2 8 4 2     .
Kotler, P., K. L. Keller, and A. Chernev. 2022. Marketing management.
16th Global ed. Pearson UK.
Liu, X., and Y . Liu. 2024. Sensitivity analysis of the parameters for
preference functions and rank reversal analysis in the PRO -
METHEE II method. Omega 128 : 103116.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0
1 6 / j . o m e g a . 2 0 2 4 . 1 0 3 1 1 6     .
Lu, W., L. Zhang, and Y . Liu. 2024. Evaluation of urban complex
utilization based on AHP and MCDM analysis: A case study of
China. Buildings 14 (7): 2179.  h t t  p s : /  / d o  i . o  r g / 1 0 . 3 3 9 0 / b u i l d i n g s
1 4 0 7 2 1 7 9     .
Macharis, C., B. Mareschal, J. P. Waaub, and L. Milan. 2015. PRO -
METHEE–GDSS revisited: Applications so far and new develop-
ments. International Journal of Multicriteria Decision Making  5
(1–2): 129–151. https:/ /doi.or g/10.15 04/IJ MCDM.2015.067941.
Malhotra, N. K., D. Nunan, and D. F. Birks. 2020. Marketing research.
Pearson UK.
Mardani, A., A. Jusoh, K. Halicka, J. Ejdys, A. Magruk, and U. N.
U. Ahmad. 2018. Determining the utility in management by
using multicriteria decision support tools: A review. Economic
Research-Ekonomska Istraživanja 31 (1): 1666–1716.  h t t  p s : /  / d o  i
. o  r g / 1 0 . 1 0 8 0 / 1 3 3 1 6 7 7 X . 2 0 1 8 . 1 4 8 8 6 0 0     .
Miles, C. 2026. Constructions of marketing work: A critical review.
Journal of Marketing Management 42 (3–4): 324–354.  h t t  p s : /  / d o
i . o  r g / 1 0 . 1 0 8 0 / 0 2 6 7 2 5 7 X . 2 0 2 5 . 2 5 5 1 1 6 9     .
Montecchi, M., A. Gvirtz, K. Plangger, G. Prendergast, and D. West.
2024. Marketing experts are always right…aren’t they? Disen -
tangling the effects of expertise and decision-making processes.
Psychology & Marketing 41 (7): 1432–1442.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1
0 0 2 / m a r . 2 1 9 8 8     .
Nunnally, J. C., and I. H. Bernstein. 1994. Psychometric theory. 3rd
ed. McGraw-Hill.
Oliver, R. L. 1999. Whence consumer loyalty? Journal of Marketing
63 (4_suppl1): 33–44.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 7 7 / 0 0 2 2 2 4 2 9 9 9 0 6 3 4 s
1 0 5     .
Oubahman, L., S. Duleba, and D. Esztergár-Kiss. 2024. Analyzing
university students’ mode choice preferences by using a hybrid
AHP group-PROMETHEE model: Evidence from Budapest city.
European Transport Research Review 16 (1) : 8.  h t t  p s : /  / d o  i . o  r g / 1
0 . 1 1 8 6 / s 1 2 5 4 4 - 0 2 3 - 0 0 6 2 6 - w     .
Pautasso, M. 2019. The structure and conduct of a narrative literature
review. In A guide to the scientific career, 299–310.  h t t  p s : /  / d o  i . o  r
g / 1 0 . 1 0 0 2 / 9 7 8 1 1 1 8 9 0 7 2 8 3 . c h 3 1
Petrescu, M., and A. S. Krishen. 2023. A decade of marketing analytics
and more to come: JMA insights. Journal of Marketing Analytics
11 (2): 117–129. https:/ /doi.or g/10.10 57/s4 1270-023-00226-6.
Petrescu, M., and A. S. Krishen. 2024. Marketing analytics in 2024
conferences: AI and data-driven decision-making. Journal of
Marketing Analytics 12 (4): 743–745.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 5 7 / s 4
1 2 7 0 - 0 2 4 - 0 0 3 5 7 - 4     .
Power, D. J. 2008. Decision support systems: A historical overview.
In Handbook on decision support systems 1: Basic themes, ed. F.
Burstein and C. W. Holsapple, 121–140. Springer Berlin Heidel-
berg. https:/ /doi.or g/10.10 07/97 8-3-540-48713-5_7.
Power, D. J., C. Heavin, and Y . O’Connor. 2021. Balancing privacy
rights and surveillance analytics: A decision process guide. Jour-
nal of Business Analytics 4 (2): 155–170.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 /
2 5 7 3 2 3 4 X . 2 0 2 1 . 1 9 2 0 8 5 6     .
Rialti, R., L. Zollo, A. Ferraris, and I. Alon. 2019. Big data analytics
capabilities and performance: Evidence from a moderated multi-
mediation model. Technological Forecasting and Social Change
149 : 119781. https:/ /doi.or g/10.10 16/j. techfore.2019.119781.

T. Tarnanidis et al.
Roszkowska, E., M. Filipowicz-Chomko, A. Łyczkowska-
Hanćkowiak, and E. Majewska. 2024. Extended Hellwig’s
method utilizing entropy-based weights and Mahalanobis dis -
tance: Applications in evaluating sustainable development in the
education area. Entropy 26 (3): 197.  h t t  p s : /  / d o  i . o  r g / 1 0 . 3 3 9 0 / e 2 6
0 3 0 1 9 7     .
Rust, R. T. 2020. The future of marketing. International Journal of
Research in Marketing 37 (1): 15–26.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . i j
r e s m a r . 2 0 1 9 . 0 8 . 0 0 2     .
Schär, S., E. Pohl, and J. Geldermann. 2025. Analysing the compensa-
tory properties of the outranking approach PROMETHEE. Jour-
nal of Multicriteria Decision Analysis 32 (2) : e70013.  h t t  p s : /  / d o  i
. o  r g / 1 0 . 1 0 0 2 / m c d a . 7 0 0 1 3     .
Shu, Z., J. J. Galán Hernández, and Á. Carrasco-Aguilar. 2026. Profil-
ing the application of the 2-tuple linguistic model in marketing:
A comprehensive analysis and future directions. Fuzzy Optimiza-
tion and Decision Making 25 (2): 285–313.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0
0 7 / s 1 0 7 0 0 - 0 2 6 - 0 9 4 7 7 - 1     .
Sklavos, G., G. Zournatzidou, K. Ragazou, and N. Sariannidis. 2025.
Unmasking greenwashing in finance: A PROMETHEE II-based
evaluation of ESG disclosure and green accounting alignment.
Risks 13 (7) : 134. https:/ /doi.or g/10.33 90/ri sks13070134.
Spais, G., and G. Chryssochoidis. 2025. Trends and future of artificial
intelligence (AI), machine learning (ML) algorithms, and data
analytics and their applications and implications for digital mar -
keting and digital promotions. Journal of Marketing Analytics 13
(2): 263–266. https:/ /doi.or g/10.10 57/s4 1270-025-00406-6.
Taherdoost, Hamed & Madanchian, Mitra. 2023. Using PROMETHEE
method for multicriteria decision making: Applications and pro -
cedures. Iris journal of economics & business management, V ol-
ume 1-Issue 1, Available at SSRN: https:/ /ssrn.c om/abst ract=
4464669
Tarnanidis, T., J. Papathanasiou, B. Mareschal, M. Vlachopoulou, V .
K. Manda, and B. Sousa. 2026a. Sustainable value creation in
global marketing decisions: A systematic PRISMA review of
PROMETHEE applications. Journal of Marketing Analytics .
https:/ /doi.or g/10.10 57/s4 1270-026-00486-y.
Tarnanidis, T., J. Papathanasiou, B. Mareschal, M. Vlachopoulou, and
V . K. Manda. 2026b. A decision-aid approach to social media
assessment using PROMETHEE II in Greek grocery retail.
Administrative Sciences 16 (3): 114.  h t t  p s : /  / d o  i . o  r g / 1 0 . 3 3 9 0 / a d m
s c i 1 6 0 3 0 1 1 4     .
Tarnanidis, T., Papathanasiou, J., Vlachopoulou, M., & Mareschal,
B. (2023). Review and the Use of PROMETHEE Methods in
Marketing (Problems). In T. Tarnanidis, M. Vlachopoulou, & J.
Papathanasiou (Eds.), Influences of Social Media on Consumer
Decision-Making Processes in the Food and Grocery Industry
(pp. 196-212). IGI Global Scientific Publishing.  h t t  p s : /  / d o  i . o  r g /
1 0 . 4 0 1 8 / 9 7 8 - 1 - 6 6 8 4 - 8 8 6 8 - 3 . c h 0 0 9
Tarnanidis, T., and Mareschal, B. 2025. The future of PROMETHEE
in marketing. International journal of business and applied social
science, 11(4), 7–13. https:/ /doi.or g/10.33 642/I JBASS.V11N4P2
Tibay, E., R. Quinones, H. Quinones, E. Selerio, S. S. Evangelista, J.
L. Aro, F. Maturan, N. M. Atibing, K. Yamagishi, and L. Ocampo.
2022. Optimal planning of university technology transfer mea -
sures with FDANP-F-FlowSort and an extended multiobjective
PROMETHEE V . IEEE Access 10:56629–56651.  h t t  p s : /  / d o  i . o  r g
/ 1 0 . 1 1 0 9 / A C C E S S . 2 0 2 2 . 3 1 7 6 6 4 1     .
Tsiaras, S., and S. Mantzoukas. 2026. PROMETHEE-based ranking of
EU countries across key agricultural and environmental indica -
tors. Applied Sciences 16 (2): 1131.  h t t  p s : /  / d o  i . o  r g / 1 0 . 3 3 9 0 / a p p
1 6 0 2 1 1 3 1     .
Verhoef, P. C., E. Kooge, N. Walk, and J. E. Wieringa. 2021. Creating
value with data analytics in marketing: Mastering data science .
Routledge.
Wang, R., Q. Wang, and W. K. Chiang. 2024. Optimal promotional
mix and pricing when faced with uncertain product value. Euro-
pean Journal of Operational Research 313 (2): 637–651.  h t t  p s : /  /
d o  i . o  r g / 1 0 . 1 0 1 6 / j . e j o r . 2 0 2 3 . 0 8 . 0 4 2     .
Wedel, M., and P. K. Kannan. 2016. Marketing analytics for data-rich
environments. Journal of Marketing 80 (6): 97–121.  h t t  p s : /  / d o  i . o
r g / 1 0 . 1 5 0 9 / j m . 1 5 . 0 4 1 3     .
Wierenga, B. 2011. Managerial decision making in marketing: The next
research frontier. International Journal of Research in Marketing
28 (2): 89–101. https:/ /doi.or g/10.10 16/j. ijresmar.2011.03.001.
Yadav, A., S. Sen, and G. L. Vanapalli. 2024. Advanced MCDM
techniques and emerging trends for marketing applications. In
Advances in marketing, customer relationship management, and
e-services, ed. T. Tarnanidis, J. Papathanasiou, V . Ismyrlis, and V .
Kittu. Manda, 1–26. IGI Global.  h t t  p s : /  / d o  i . o  r g / 1 0 . 4 0 1 8 / 9 7 9 - 8 - 3
6 9 3 - 9 1 2 2 - 8 . c h 0 0 1     .
Yatsalo, B., A. Korobov, B. Öztayşi, C. Kahraman, and L. Martínez.
2021. Fuzzy extensions of PROMETHEE: Models of different
complexity with different ranking methods and their comparison.
Fuzzy Sets and Systems  422:1–26.  h t t p s : / / d o i . o  r   g /  1  0 . 1 0 1 6 / j . f s s . 2
0 2 0 . 0 8 . 0 1 5     .
Zapletal, F. 2022. Revised PROMETHEE algorithm with reference
values. Central European Journal of Operations Research 30 (2):
521–545. https:/ /doi.or g/10.10 07/s1 0100-021-00767-0.
Zhou, F., and T.-Y . Chen. 2025. A synergetic intuitionistic fuzzy model
combining AHP, entropy, and ELECTRE for data fabric solution
selection. Artificial Intelligence Review 58 (5): 137.  h t t  p s : /  / d o  i . o  r
g / 1 0 . 1 0 0 7 / s 1 0 4 6 2 - 0 2 5 - 1 1 1 2 8 - 7     .
Zulaikha, S., H. Mohamed, M. Kurniawati, S. Rusgianto, and S. A.
Rusmita. 2025. Customer predictive analytics using artificial
intelligence. The Singapore Economic Review  70 (04): 1009–
1020. https:   //d oi. or g/10 .114 2/S0217590820480021.
Publisher's Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
Theodore Tarnanidis   is a researcher in Applications of PRO -
METHEE at the University of Macedonia, a Reader, and a marketing
scholar with extensive teaching and research experience across aca -
demic institutions, including the International Hellenic University and
Metropolitan College. He also has more than six years of professional
experience in marketing and decision-making. He holds two doctoral
degrees: a PhD in Marketing from London Metropolitan University
(UK), fully funded through a government scholarship, and a doctorate
in Management and Decision Science from the University of Mace -
donia (Greece). He also holds an MPhil from the University of Man -
chester (UK), an MBA in Marketing from the University of Liverpool
(UK), and a Postgraduate Certificate in Management from Bielefeld
University (Germany). He completed a Postdoctoral Research Fel -
lowship in Sustainable Entrepreneurship at the University of Mace -
donia. His research interests include Digital Marketing, Consumer
Behaviour, Artificial Intelligence in Marketing, Sustainable Entrepre -
neurship, Marketing Analytics, Decision Science, and Multi-Criteria
Decision Making (MCDM). His scholarly work has been published in
internationally recognized peer-reviewed journals, including the Jour-
nal of Business Ethics, Journal of Retailing and Consumer Services,
Current Issues in Tourism, Journal of Global Marketing, and Journal
of Marketing Analytics. He has also edited more than 20 international
academic books and authored numerous book chapters and conference
papers.

A practical framework for selecting PROMETHEE preference functions in marketing decision-making
Bertrand Mareschal  is a Professor of Quantitative Methods (Opera-
tions Research and Statistics) at the Solvay Brussels School of Eco -
nomics and Management (SBS-EM), Université libre de Bruxelles
(ULB), CP 114, 50 Avenue F.D. Roosevelt, 1050 Brussels, Belgium.
His research expertise includes Multiple-Criteria Decision Analysis
(MCDA). He is the developer of the Visual PROMETHEE software
and Editor-in-Chief of the O&D Open Journal.
Jason Papathanasiou  is a Professor at the Department of Business
Administration, University of Macedonia, Greece. He holds a PhD in
Operational Research and Informatics and a degree in Physics from
the Aristotle University of Thessaloniki. He has worked for several
years at various institutes and has organized and participated in numer-
ous international scientific conferences and workshops. He has pub -
lished papers in international, peer-reviewed scientific journals such
as Environmental Monitoring and Assessment, Regional Studies, and
the European Journal of Operational Research, and has participated in
many research projects in FP6, FP7, Interreg, and COST; he was also
a member of the TDP Panel of COST.
Maro Vlachopoulou  is a Professor at the Department of Applied
Informatics, University of Macedonia, Greece. Her professional
expertise, research and teaching interests include marketing infor -
mation systems, electronic commerce, e- mobile business, e- mobile
marketing, Internet marketing, social media/networks & marketing,
Enterprise Resource Planning (ERP) systems, Customer Relation -
ship Management (CRM) systems, e-supply chain management,
e-logistics, and SC information systems, with particular emphasis
on specific applications (agribusiness, e-health, e-tourism and envi -
ronment). She participates in several European-funded Research and
Development programmes in the above fields. She is also a member
of editorial board and reviewer for several scientific journals, includ -
ing International Journal of Production Economics, European Journal
of Operation Research, International Journal of Physical Distribution
and Logistics Management, European Journal of Information Systems,
Journal of Enterprise Information Management, International Journal
of Business Information Systems, International Journal of Internet
Marketing (IJIMA), International Journal of Logistics, Computational
Management Science journal (special issue on “Computational Clas -
sification Methods for Decision Making”), member of the editorial
board of The International Journal of Business Information Systems
(Inderscience Publishers), and of International Journal of Sustainable
Agricultural Management and Informatics (IJSAMI).
Vijaya Kittu Manda   has nearly 13+ years of experience in capi -
tal markets, financial planning, and investing. He is a Researcher at
PBMEIT. He is an Advocate, a technocrat, an academician, a book
writer, and a stock market enthusiast. He holds 12 postgraduate degrees
from universities across various disciplines. He holds a Ph.D. in Man-
agement (Finance). His thesis was on Mutual Funds and their Market
Competition. His thesis won the prestigious NSE-IEA Best Thesis
Award in 2023. He is currently pursuing his second Ph.D. in Computer
Science with a focus on Blockchain. He contributed over 750 articles
to various magazines. He is the Chief Editor for a Management Book
Series, a Peer Reviewer, a Certified Peer Review Supervisor, and a
Session Chair and Advisor for various academic and industrial confer-
ences. He writes Research Papers and Case Studies, Book Chapters,
and sits on the editorial boards of various journals. He is a resource
person for various research events and a guest speaker for colleges
and universities.
Bruno Sousa  is a Professor and Coordinator of Marketing at Poly -
technic University of Cávado and Ave (IPCA), Portugal. He holds a
PhD in Marketing and Strategy from Universidade do Minho, Portugal.
Bruno Sousa is also Head of the Master’s Program in Tourism Man -
agement and Tourism Marketing (IPCA); CiTUR – Center for Tour -
ism Research, Development and Innovation; and a UNIAG research
member. Bruno Sousa’s teaching fields include marketing, strategy,
and tourism. Bruno Sousa’s research areas include brand management
and consumer behavior, strategy implementation, niche marketing,
niche tourism, and brand attachment. He has published in the Jour -
nal of Enterprising Communities, Tourism Management Perspectives,
Current Issues in Tourism, Journal of Organizational Change Manage-
ment, World Review of Entrepreneurship, Management and Sustain -
ability. Development, among others.
