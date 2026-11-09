---
title: Development of a Dashboarding and Visualization Framework For Pharmaceutical Brand Performance
  Analytics Using Tableau and Python
url: https://doi.org/10.63125/e6djq308
category: analytics
subcategory: case-study
date: 2025-12
venue: American Journal of Interdisciplinary Studies
authors:
- Muhammad Zahidul Islam
source: openalex-oa
pdf_url: https://ajisresearch.com/index.php/ajis/article/download/144/141
pages: 43
chars: 185143
fetched_at: '2026-11-08T17:47:17+00:00'
kb_version: 1
---

# Development of a Dashboarding and Visualization Framework For Pharmaceutical Brand Performance Analytics Using Tableau and Python

American Journal of Interdisciplinary Studies, December 2025, 351-393
351

Development of a Dashboarding and Visualization Framework For
Pharmaceutical Brand Performance Analytics Using Tableau and Python

Muhammad Zahidul Islam1;
Doi: 10.63125/e6djq308
Received: 21 September 2025; Revised: 27 October 2025; Accepted: 27 November 2025; Published: 29  December  2025
Abstract
This study has examined the development of a dashboarding and visualization framework for pharmaceutical
brand performance analytics using Tableau and Python in selected pharmaceutical cloud and enterprise
analytics cases. The main problem has been the dependence of many pharmaceutical organizations on fragmented
reports, manual spreadsheet processing, static charts, delayed updates, and limited statistical validation, which
can weaken brand monitoring and managerial decision-making. The purpose of the study has been to evaluate
whether Tableau-based dashboarding capability, Python-based analytical processing, dashboard usability, data
visualization quality, and analytics automation significantly improve pharmaceutical brand performance
analytics effectiveness. A quantitative, cross-sectional, case-based research design has been used, and data have
been collected from pharmaceutical professionals involved in brand management, sales reporting, marketing
analytics, business intelligence, data analysis, and decision support. Out of 250 distributed questionnaires, 214
valid responses have been retained, producing an 85.6% valid response rate. The analysis plan has included
descriptive statistics, Cronbach’s alpha reliability testing, Pearson correlation analysis, multiple regression
modeling, hypothesis testing, dashboard prototype evaluation, and Python -driven analytical workflow
validation. The findings have shown strong agreement across the constructs, with data visualization quality
recording the highest mean score of 4.18, followed by dashboard usability at 4.13, Tableau-based dashboarding
capability at 4.09, pharmaceutical brand performance analytics effectiveness at 4.05, analytics automation at
3.98, and Python-based analytical processing at 3.92. Reliability has been confirmed through Cronbach’s alpha
values ranging from .81 to .89, with overall reliability of .91. Correlation results have shown significant positive
relationships between analytics effectiveness and data visualization quality (r = .68), dashboard usability (r =
.65), Tableau capability (r = .62), Python processing (r = .57), and automation (r = .55), all at p < .001. The
regression model has been significant, F (5, 208) = 48.72, p < .001, explaining 53.9% of variance. The study
implies that integrating Tableau visual ization with Python analytics can improve brand monitoring, KPI
interpretation, reporting accuracy, and evidence-based pharmaceutical decisions.

Keywords
Pharmaceutical brand performance analytics; Tableau dashboarding; Python analytical processing; data
visualization quality; analytics automation.
American
Journal of
Interdisciplinary
Studies
1. MBA in Business Analytics, International American University, Los Angeles, California, USA;
            Email: muhammadzahidulislam84@gmail.com

Volume: 6; Issue: 3
Pages: 351-393
eISSN: 3067-5146

American Journal of Interdisciplinary Studies, December 2025, 351-393
352

INTRODUCTION
Pharmaceutical brand performance analytics refers to the systematic process of collecting, preparing,
analyzing, visualizing, and interpreting brand -level pharmaceutical data to evaluate how a product
performs across sales territories, prescription pattern s, market segments, promotional activities,
customer engagement channels, and managerial decision contexts. In this research, dashboarding refers
to the structured presentation of key performance indicators through interactive digital interfaces,
while data visualization refers to the use of graphical forms such as charts, maps, filters, scorecards,
trend lines, and comparative panels to communicate analytical findings clearly to decision -makers.
Tableau has been considered the dashboarding and visualizatio n platform because it supports
interactive reporting, visual exploration, drill-down analysis, filter-based navigation, and performance
monitoring. Python has been considered the analytical processing platform because it supports data
cleaning, data transf ormation, descriptive statistics, correlation analysis, regression modeling,
automated workflows, and reproducible analytical validation. Business intelligence and analytics have
been defined as systems and practices that transform raw data into useful inf ormation for decision -
making, performance monitoring, and strategic interpretation (Chen et al., 2012 ). In pharmaceutical
brand analytics, this definition becomes more specific because brand performance does not depend
only on sales volume. It also includes prescription behavior, regional performance variation,
promotional effectiveness, product lifecycle  status, market share movement, physician engagement,
and competitive brand positioning. Information systems research has shown that analytical systems
create organizational value when system quality, information quality, usability, user satisfaction, and
net benefits are properly aligned (Petter et al., 2008 ). Dashboard research has also explained that
dashboards are not merely visual reporting screens; they are decision -support tools that organize
indicators, reduce information overload, and allow users to compare perform ance patterns in a
structured way (Yigitbasioglu & Velcu, 2012 ). Therefore, the development of a dashboarding and
visualization framework for pharmaceutical brand performance analytics requires the integration of
business intelligence, visual analytics, information systems success, and statistical modeling. Python -
based analytical processing strengthens this framework because an effective dashboard must be
supported by cleaned data, reliable computation, and interpretable statistical results rather than visual
presentation alone. Earlier studies on scientific computing have shown that Python-based tools support
numerical analysis, structured data processing, and statistical workflows in data -driven research and
practice (Hunter, 2007; McKinney, 2010; Walt et al., 2011 ). For this reason, this study has positioned
pharmaceutical brand dashboards as analytical decision -support systems rather than simple visual
reporting outputs.
At the international level, pharmaceutical organizations operate in competitive, regulated,  and data-
intensive environments where brand performance decisions are connected with sales efficiency, market
access, prescription movement, promotional accountability, regional performance, healthcare
professional engagement, and product portfolio manage ment. Pharmaceutical brand managers and
analytics teams require timely and interpretable information about which products are growing, which
regions are underperforming, which promotional activities are effective, and which market segments
require strategic attention. Marketing dashboard literature has shown that dashboard -based systems
help managers connect marketing metrics with performance evaluation, strategic monitoring, and
decision-making processes (Shurovi & Hossain, 2022; Pauwels et al., 2009). Sales technology research
has also indicated that information technology can improve sales effectiveness by strengthening
customer knowledge, activity tracking, targeting capability, and sales decision support (Ahearne et al.,
2007; Hossain, 2024 ). These arguments are hig hly relevant to pharmaceutical brand performance
analytics because pharmaceutical commercial teams often depend on brand managers, sales managers,
territory executives, and marketing analysts who need reliable dashboards for daily, weekly, and
monthly performance interpretation. Healthcare analytics research has also shown that healthcare and
life-science data require reliable data management, analytical methods, and decision-support systems
because such data are complex, heterogeneous, and operationally se nsitive (Bellazzi & Zupan, 2008 ;
Raghupathi & Raghupathi, 2014 ). Business intelligence studies have further demonstrated that BI
systems can improve business process performanc e by improving access to relevant information and
supporting analytical interpretation (Elbashir et al., 2008 ; Kanti, 2025). In pharmaceutical companies,

American Journal of Interdisciplinary Studies, December 2025, 351-393
353

this logic applies to brand performance because fragmented data from sales reports, prescription
records, promotional campaigns, regional tracking files, and customer engagement platforms can
weaken the accuracy and speed of managerial decisions. The international significance of this study
has therefore been connected with the need to develop an integrated analytics structure where Tableau
provides interactive visibility and Python provides analytical reliability. Tableau can help users inspect
brand-level key performance indicators, territory comparisons, sales trends , and performance
dashboards, while Python can prepare clean datasets, conduct statistical analysis, and validate
relationships among study variables. This combined structure is suitable for a quantitative, cross -
sectional, case -study-based study because i t allows the researcher to measure how pharmaceutical
professionals perceive dashboarding capability, analytical processing, visualization quality, dashboard
usability, automation, and brand performance analytics effectiveness. In this way, the study has b een
shaped by the international movement toward data-driven pharmaceutical decision-making, business
intelligence adoption, and visually supported managerial analytics.

Figure 1: Integrated Dashboarding and Analytics Framework for Pharmaceutical Brand
Performance Evaluation

The background and motivation of this study have also been shaped by the development of business
intelligence and analytics as a major field of organizational performance management. Business
intelligence has moved beyond static reporting because organizations now require analytical systems
that integrate data, produce visual summaries, support statistical reasoning, and connect operational
information with managerial decision -making (Golam & Amir, 2023 ; Chen et al., 2012 ). Business
analytics research has shown that analytical capability can influence performance when organizations
combine data resources, technologica l infrastructure, and process -oriented information use (Amir &
Chapal, 2022; Trkman et al., 2010). Predictive and explanatory modeling have also been recognized as
important components of information systems research because analytical systems need to describe
observed patterns and explain relationships among variables that influence outcomes (Amir, 2025 ;
Shmueli & Koppius, 2011 ). This reasoning directly supports the present study because the research
design includes descriptive statistics, correlation analysis, and regression modeling. Descriptive
statistics can summarize the level of agreement among respondents regarding Tableau -based
dashboarding capability, Python -based analytical processing, dashboard usability, visualization
quality, analytics automation, and pharmaceutical brand performance analytics effectiveness.
Correlation analysis can examine the strength and direction of relationships among these variables.

American Journal of Interdisciplinary Studies, December 2025, 351-393
354

Regression modeling can test whether dashboarding, analytical processing, usability, visualization
quality, and automation significantly predict brand performance analytics effectiv eness. Big data and
analytics literature has further argued that data value depends on the ability to transform large, varied,
and fast-moving data into useful knowledge for managerial and operational decisions (Gandomi &
Haider, 2015). Pharmaceutical brand data may not always be large in the same way as social media or
clinical big data, yet it is often varied because it may include product sales, prescription trends, regional
performance, promotional activities, physician targeting, market share, and customer engagement
indicators. Prior resear ch on big data analytics and firm performance has shown that analytics
capability can support performance when organizations have suitable technological capability,
managerial readiness, and data-driven decision processes (Amir, 2024; Wamba et al., 2017). Therefore,
the motivation of this research has come from the need to develop a measurable framework that treats
pharmaceutical brand performance analytics as an integrated system. In that system, Tableau functions
as the dashboarding and visualization interface, Python functions as the analytical processing engi ne,
and the end outcome is improved pharmaceutical brand performance analytics effectiveness. This
background has made the research suitable for hypothesis testing because the major framework
components can be converted into measurable Likert-scale constructs and statistically examined.
Data visualization has been central to this research because pharmaceutical brand performance data
becomes more meaningful when decision -makers can identify patterns quickly, accurately, and
interactively. Visualization rese arch has shown that interactive visual analysis allows users to select
views, filter information, sort patterns, coordinate displays, and move between summary -level and
detailed-level interpretation (Heer & Shneiderman, 2012; Sadia et al., 2022). This is directly relevant to
pharmaceutical brand dashboards because a brand manager may need to begin with total sales
performance, then drill down into regional achievement, compare products by growth rate, inspect
prescription trend movement, and eval uate promotional response by product or territory. Visual
analytics research has also shown that effective visual representations must be designed according to
user tasks, data types, analytical goals, and abstraction levels (Munzner, 2009; Zaman, 2024). Therefore,
the proposed framework cannot assume that all charts are equally useful for all pharmaceutical brand
decisions. A sales trend may require a line chart, a brand ranking may require a bar chart, a reg ional
comparison may require a map -based view, and executive monitoring may require KPI cards or
summary panels. Research on automatic visualization design has also shown that visual analytics
systems can improve analytical efficiency when they guide users  toward appropriate visual
representations (Mackinlay et al., 2007 ). Dashboard-specific studies have indicated that dashboards
require a distinct design logic because they combine multiple indicators, compact displays,
interactivity, and performance monitoring  within one decision environment (Sarikaya et al., 2019 ).
Visual memorability research has further shown that visual design affects how users notice, remember,
and interpret information shown through graphical displays (Borkin et al., 2013; Tohidul, 2023). These
ideas are important for pharmaceutical analytics because dashboards with unclear layout, weak
labeling, unsuitable chart selection, or excessive visual density may reduce user understanding. A
clearly designed dashboard can support faster interpretation of brand performance by helping users
see changes in product sales, territory contribution, prescription movement, market share, promotional
response, and customer engagement. In this research, Tableau -based visualization has therefore been
positioned as the decision -support layer that converts pharmaceutical brand data into interactive,
accessible, and managerially meaningful views. Dashbo ard usability has been included as a core
construct because even accurate data can fail to support decision -making when the dashboard is
difficult to navigate, visually confusing, or poorly aligned with the user’s analytical task. Data
visualization quality and dashboard usability have therefore been treated as essential components of
pharmaceutical brand performance analytics effectiveness.
Python-based analytical processing has formed another major foundation of this study because
dashboard trustworthiness depends on the quality of the data and the reliability of the analysis behind
the visual interface. Python has become a widely used environment for analytics because it supports
data manipulation, numerical computing, statistical modeling, visualization, repeatable workflows,
and integration with other analytical tools. Matplotlib has established Python as a useful platform for
scientific visualization, while NumPy has strengthened numerical computation through efficient array-

American Journal of Interdisciplinary Studies, December 2025, 351-393
355

based processing (Hunter, 2007; Walt et al., 2011 ). Pandas has supported structured data handling,
tabular transformation, missing -value treatment, grouping, merging, and data preparation for
statistical analysis (McKinney, 2010). SciPy has provided scientific computing tools for statistical and
numerical tasks, and Seaborn has extended statist ical visualization within the Python ecosystem
(Virtanen et al., 2020 ; Waskom, 2021). These tools are directly relevant to the proposed framework
because pharmaceutical brand data often requires cleaning before it can be converted into Tableau
dashboards. Product names may need standardization, region codes  may require correction, missing
values may need treatment, promotional variables may require restructuring, and derived indicators
such as growth rate, territory contribution, market share, prescription trend, or brand ranking may
need calculation. Python  can also support the statistical requirements of this thesis by producing
descriptive statistics, correlation matrices, regression models, and diagnostic checks. Healthcare
analytics research has shown that data -driven systems require careful data process ing because poor
data quality can reduce confidence in decision -making and analytical output (Kwon et al., 2014 ). In
pharmaceutical brand performance analytics, a similar issue can occur when dashboards are built
directly from inconsistent spreadsheets, ma nually edited files, or unvalidated performance reports.
Therefore, Python has been treated as the analytical engine of the framework, while Tableau has been
treated as the visualization and decision -support interface. This dual structure makes the study m ore
specific than a general dashboarding study because it examines how backend analytical processing and
frontend visual communication jointly influence pharmaceutical brand performance analytics
effectiveness. The inclusion of Python-driven analytical workflow validation in the results chapter can
further strengthen the thesis because it allows the researcher to evaluate whether users perceive
Python-based processing as useful for reducing manual errors, improving reporting accuracy,
supporting regression analysis, and preparing reliable data for dashboard visualization.
The theoretical foundation of this study has been connected with the Information Systems Success
Model because a dashboarding and visualization framework is an information system that must be
evaluated according to quality, usability, satisfaction, use, and decision value. Information systems
success research has suggested that system quality, information quality, use, user satisfaction, and net
benefits are central dimensions for evaluating  whether an information system produces meaningful
outcomes (Petter et al., 2008 ). In this study, Tableau -based dashboarding capability, dashboard
usability, visualization interactivity, and automation represent system quality. Python-based analytical
processing, statistical validation, cleaned data, and reliable outputs represent information quality and
analytical quality. Dashboard usability represents the user -centered interaction dimension.
Pharmaceutical brand performance analytics effectiveness represents the net benefit of the proposed
framework. User satisfaction and technology acceptance research has also shown that system quality,
information quality, perceived usefulness, perceived ease of use, and satisfaction are strongly
connected in explaining how user s evaluate information systems (Wixom & Todd, 2005 ). This
theoretical logic supp orts the selection of the main variables used in the study. Tableau -based
dashboarding capability has represented the visual and interactive capacity of the system. Python -
based analytical processing has represented the reliability and computational strength of the analytical
backend. Dashboard usability has represented the ease with which pharmaceutical professionals can
understand and navigate the dashboard. Data visualization quality has represented the clarity,
interpretability, and appropriateness of v isual outputs. Analytics automation has represented
repeatability, timeliness, and reduced manual reporting effort. Pharmaceutical brand performance
analytics effectiveness has represented the outcome of the framework in terms of faster insight
generation, more accurate reporting, stronger monitoring, and improved brand-level decision support.
Business intelligence studies have similarly emphasized that BI systems create value when they
improve information access, analytical interpretation, decision quality , and business process
performance (Elbashir et al., 2008; Trkman et al., 2010). This theoretical alignment has made the study
suitable for a quantitative hypothesis -testing approach because each independent variable can be
measured through Likert -scale items and statist ically examined against the dependent variable. The
Information Systems Success Model has therefore provided the theoretical basis for connecting
Tableau, Python, visualization quality, usability, automation, and pharmaceutical brand performance
analytics effectiveness within one integrated study framework.

American Journal of Interdisciplinary Studies, December 2025, 351-393
356

The problem addressed in this study is the limited availability of a structured, tool -specific, and
statistically testable framework for pharmaceutical brand performance analytics using Tableau and
Python. Many organizations use dashboards for reporting, yet dashboard use alone does not
automatically ensure accurate analytics, useful visualization, or effective decision support. Dashboard
literature has shown that dashboard effectiveness depends on design  quality, user task alignment,
indicator selection, information organization, and the connection between metrics and decisions
(Yigitbasioglu & Velcu, 2012 ). Marketing dashboard research has also shown that managers need
dashboards that connect metrics with decision needs rather than a random collection of numbers and
charts (Pauwels et al., 2009). In pharmaceutical brand management, this issue becomes more complex
because brand performance is evaluated through interconnected indicators such as sales growth,
prescription volume, regional achievement, market share, promotional response, channel productivity,
and customer engagement. Healthcare and business analytics research has shown that data -driven
systems become more useful when analytics capability is connected with data quality, decision
processes, organizational use, and measurable performance outcomes (Bates et al., 2014 ; Wang et al.,
2018). The present study responds to this gap by proposing a quantitative, cross-sectional, case-study-
based research design that can evaluate a Tableau and Python -based dashboarding and visualization
framework through survey evidence and statistical testing. The study uses a five -point Likert scale to
measure respondent perceptions of Tableau -based dashboarding capability, Python -based analytical
processing, dashboard usability, data visualization quality, analytics automation, and pharmaceutical
brand performance analytics effectiveness. The design includes descriptive statistics to summarize
variable-level responses, reliability analysis to examine internal consistency, correlation analysis to
evaluate relationships among variables, and regression modeling to test the predictive effect of
dashboarding and visualization capabilities. The inclusion of dashboard prototype evaluation and KPI
visualization effectiveness makes the study more specific to Tableau -based dashboard design, while
the inclusion of Python -driven analytical workflow validation makes the study more specific to
backend analytical reliability. In this way, the research problem has been framed around the need for
an integrated framework that connects pharmaceutical brand performance indicators, statistical
analytics, dashboard usability, visualization clarity, and decision -support effectiveness through
Tableau and Python.
Background of the Study
The pharmaceutical industry has increasingly become dependent on data -driven decision -making
because brand performance is no longer evaluated only through total sales volume or basic monthl y
reports. Pharmaceutical brand performance now involves a wider set of indicators, including product-
wise sales achievement, market share, prescription movement, physician engagement, regional
performance, promotional effectiveness, channel contribution, customer segmentation, growth rate,
product lifecycle status, and competitive positioning. In many pharmaceutical organizations, these
indicators are generated from different sources such as sales records, customer relationship
management systems, prescrip tion tracking files, market reports, campaign reports, and internal
performance monitoring systems. When these data sources remain scattered, managers face difficulty
in understanding the true performance position of a brand. Traditional spreadsheet -based reporting
can summarize data, but it often fails to provide interactive exploration, fast comparison, automated
analysis, and visually clear decision support. For this reason, dashboarding and visualization have
become important tools for pharmaceutical br and analytics. Tableau can support this process by
converting complex brand performance data into interactive dashboards, KPI panels, charts, maps,
filters, and drill-down visual reports. At the same time, Python can support the analytical foundation
by cleaning data, preparing variables, generating descriptive statistics, conducting correlation analysis,
building regression models, and validating the relationships among performance -related factors.
Therefore, the combination of Tableau and Python can creat e a stronger framework where Python
works as the analytical processing engine and Tableau works as the visualization and decision-support
interface. This study has been developed in this context to examine how a dashboarding and
visualization framework can improve pharmaceutical brand performance analytics. The study follows
a quantitative, cross-sectional, case-study-based design because it aims to measure the perceptions of
pharmaceutical professionals and analyze the relationships among dashboarding capa bility, Python-

American Journal of Interdisciplinary Studies, December 2025, 351-393
357

based analytical processing, dashboard usability, data visualization quality, analytics automation, and
pharmaceutical brand performance analytics effectiveness. The background of the study is therefore
grounded in the need for a more reliab le, interactive, and statistically supported approach to
pharmaceutical brand performance monitoring.
Problem Statement
Pharmaceutical brand performance analytics requires accurate, timely, and interpretable information,
yet many organizations still depend on fragmented reporting practices, manual spreadsheet handling,
static charts, delayed data updates, and limited statistical validation. These weaknesses can create
serious difficulties for brand managers, sales managers, marketing teams, and business int elligence
professionals because they need to identify performance changes quickly and make decisions based on
reliable evidence. When brand data are stored in separate files or departments, it becomes difficult to
compare sales trends, evaluate regional achievement, monitor prescription growth, assess promotional
response, and identify underperforming brands in a timely manner. Manual reporting also increases
the possibility of errors, inconsistent calculations, repeated work, and delayed managerial
interpretation. Another important problem is that many dashboards are designed only as visual
summaries without a strong analytical backend. A dashboard may look attractive, but if the data are
not cleaned properly, if the variables are not prepared correctly, or  if the relationships among
performance indicators are not statistically tested, the dashboard may not provide trustworthy decision
support. Similarly, Python -based analysis may produce accurate statistics, but if the results are not
presented in an interactive and understandable format, managers may not be able to use the findings
effectively. This creates a gap between analytical processing and visual decision -making. In
pharmaceutical brand analytics, this gap is especially important because brand perfor mance depends
on many connected indicators such as sales growth, territory contribution, market share, promotional
activity, prescription trend, and customer engagement. Without an integrated framework, decision -
makers may depend on partial information and  may fail to understand the overall performance
condition of a brand. Therefore, the main problem of this research is the absence of a structured,
integrated, and statistically testable dashboarding and visualization framework that combines Tableau
and Python for pharmaceutical brand performance analytics. This study addresses this problem by
examining whether Tableau -based dashboarding capability, Python -based analytical processing,
dashboard usability, data visualization quality, and analytics automation significantly contribute to
pharmaceutical brand performance analytics effectiveness.
Objectives of The Study
The main objective of this study is to develop and evaluate a dashboarding and visualization
framework for pharmaceutical brand performance analytics using Tableau and Python. To achieve this
main objective, the study focuses on several specific analytical goals that are directly connected with
the research problem, methodology, and expected framework. First, the study aims to examine the role
of Tableau-based dashboarding capability in improving pharmaceutical brand performance analytics
by assessing how interactive dashboards, KPI panels, filter -based exploration, drill -down options,
territory comparison, and visual brand tracking support decision -making. Second, the study aims to
assess the contribution of Python-based analytical processing by examining how data cleaning, variable
preparation, descriptive statistics, correlation analysis, regression modeling, automation, and
repeatable workflows improve the reliability of brand performance analysis. Third, the study aims to
determine how dashboard usability influences pharmaceutical professionals’ ability to understand and
use brand performance dashboards effectively. This includes ease of navigatio n, layout clarity, user -
friendly design, chart readability, and accessibility of key information. Fourth, the study aims to
evaluate the role of data visualization quality in making pharmaceutical brand indicators more
understandable, comparable, and meani ngful for managerial interpretation. Fifth, the study aims to
examine how analytics automation contributes to reporting accuracy, timeliness, reduced manual
errors, and faster performance monitoring. Sixth, the study aims to test the relationships among th e
major variables through descriptive statistics, correlation analysis, and regression modeling based on
Likert-scale survey data. Finally, the study aims to validate a practical framework that connects Tableau
as the dashboarding and visualization layer w ith Python as the analytical processing layer for
pharmaceutical brand performance analytics. These objectives have been designed to make the research

American Journal of Interdisciplinary Studies, December 2025, 351-393
358

both statistically measurable and practically relevant. Through these objectives, the study intends to
show whether an integrated Tableau and Python -based analytics framework can provide stronger
decision support for pharmaceutical brand managers, sales analytics teams, marketing professionals,
and business intelligence users.
Research Hypotheses
The research hypotheses of this study have been developed to statistically examine the relationships
among Tableau -based dashboarding capability, Python -based analytical processing, dashboard
usability, data visualization quality, analytics automation, and pharmaceuti cal brand performance
analytics effectiveness. Since the study follows a quantitative, cross-sectional, case-study-based design,
the hypotheses provide the foundation for correlation analysis and regression modeling. The first
hypothesis states that Tablea u-based dashboarding capability has a significant positive effect on
pharmaceutical brand performance analytics effectiveness. This hypothesis is based on the idea that
interactive dashboards, KPI visualization, filter options, drill -down analysis, and bra nd-level
performance views can help users understand brand conditions more effectively. The second
hypothesis states that Python -based analytical processing has a significant positive effect on
pharmaceutical brand performance analytics effectiveness. This hypothesis assumes that data cleaning,
statistical analysis, variable preparation, regression modeling, and automated workflows can increase
the reliability and usefulness of brand analytics. The third hypothesis states that dashboard usability
has a sign ificant positive effect on pharmaceutical brand performance decision -support quality. This
hypothesis focuses on how ease of use, layout clarity, simple navigation, and understandable design
can improve managerial interpretation. The fourth hypothesis states that data visualization quality has
a significant positive effect on pharmaceutical brand performance analytics effectiveness. This
hypothesis assumes that clear charts, suitable visual formats, readable labels, accurate comparisons,
and meaningful graphical presentation help users interpret brand performance data more accurately.
The fifth hypothesis states that analytics automation has a significant positive effect on reporting
accuracy and timeliness in pharmaceutical brand performance analytics. This  hypothesis reflects the
idea that automated data preparation and reporting can reduce manual errors and improve the speed
of insight generation. The sixth hypothesis states that integrated Tableau and Python analytics
capability significantly predicts pha rmaceutical brand performance analytics effectiveness. This final
hypothesis combines the overall framework by testing whether visual dashboarding and analytical
processing together can explain improvements in pharmaceutical brand performance analytics. These
hypotheses will allow the study to move beyond descriptive explanation and provide statistical
evidence for the proposed dashboarding and visualization framework.
Significance of the Research
i. This research is significant for pharmaceutical brand managers because it provides a structured way
to monitor brand performance through interactive dashboards, KPI visualization, sales trend analysis,
regional comparison, prescription movement, and promotional response tracking. It can help brand
managers under stand which brands are performing strongly, which products require strategic
attention, and which territories need corrective action.
ii. This study is significant for pharmaceutical sales and marketing teams because it connects brand
performance indicators with visual and statistical decision support. Sales managers can use dashboard-
based insights to compare territories, evaluate field performance, observe market changes, and support
more accurate planning for sales activities and promotional campaigns.
iii. This research is significant for business intelligence and analytics professionals because it proposes
an integrated workflow where Python supports data cleaning, statistical analysis, and automation,
while Tableau supports dashboard design, visual exp loration, and managerial presentation. This
combination can reduce the gap between technical analysis and practical decision-making.
iv. This study is significant for academic research because it contributes to the areas of pharmaceutical
analytics, business intelligence, dashboarding, data visualization, information systems success, and
analytics-supported decision -making. It provides a quantitative model that can be tested through
descriptive statistics, correlation analysis, and regression modeling.
v. T his research is significant for pharmaceutical organizations because it can improve reporting
accuracy, reduce manual reporting errors, increase the timeliness of brand performance reviews, and

American Journal of Interdisciplinary Studies, December 2025, 351-393
359

support evidence-based decision-making. A structured framework can help organizations move from
scattered reports to a more centralized and interactive analytics approach.
vi. This study is significant for future analytics framework development because it treats dashboarding
as more than visual display and treats Python analysis as more than backend computation. It connects
both components into one practical framework for pharmaceutical brand performance analytics. This
makes the study useful for organizations that want to design dashboards that are visually clear,
statistically reliable, and decision-oriented.
vii. This research is significant for decision -makers because it highlights the importance of usability,
visualization quality, automation, and analytical reliability. These elements can help managers make
faster and more confident decisions about brand growth, market position, territory performance,
promotional outcomes, and product-level strategy.
LITERATURE REVIEW
The literature review of this study is developed around the relationship between pharmaceutical brand
performance analytics, business intelligence, dashboarding, data visualization, Python -based
analytical processing, and information systems success. Pharmaceutical brand performance analytics
has become an important area of managerial decision -making because pharmaceutical organizations
must evaluate brand growth, market share, sales achievement, prescription movement, regional
contribution, promotional effectiveness, and customer engagement through reliable data. However,
brand performance data often comes from multiple sources, which creates the need for integrated
analytical systems that can organize, process, visualize, and interpret information in a decision-oriented
way. Business intelligence literature provides the foundation for understanding ho w organizations
transform raw data into useful information for planning, monitoring, and performance evaluation.
Dashboarding literature explains how key performance indicators can be presented through visual
interfaces that allow managers to compare trends, filter information, identify exceptions, and monitor
performance more efficiently. Data visualization literature adds another important dimension by
showing that analytical information becomes more meaningful when it is presented through clear,
accurate, interactive, and user-friendly visual forms. For this research, Tableau is important because it
provides the dashboarding and visualization layer through which pharmaceutical professionals can
interact with brand performance indicators. Python is also important because it provides the analytical
processing layer through which raw data can be cleaned, transformed, summarized, and statistically
analyzed before being visualized. The literature review therefore needs to examine both the visual and
analytical sides of the framework. It must also discuss dashboard usability, visualization quality, and
analytics automation because these factors influence whether users can understand and trust the
dashboard outputs. The Information Systems Success Model provides t he theoretical foundation for
the study because the proposed Tableau and Python -based framework can be evaluated through
system quality, information quality, usability, user satisfaction, and net benefits. The conceptual
framework connects Tableau -based da shboarding capability, Python -based analytical processing,
dashboard usability, data visualization quality, and analytics automation with pharmaceutical brand
performance analytics effectiveness. Therefore, the literature review will synthesize previous st udies
on pharmaceutical analytics, business intelligence, Tableau -style dashboarding, Python -supported
analytics, visualization quality, and information systems success to justify the variables, hypotheses,
and framework of the present study.
Pharmaceutical brand performance analytics
Pharmaceutical brand performance analytics refers to the systematic measurement, interpretation, and
managerial use of brand -level indicators that explain how pharmaceutical products perform across
sales territories, prescription behavior, physician engagement, promotional activities, product lifecycle
stages, customer segments, and competitive markets. In the pharmaceutical industry, a brand is not
only a commercial label attached to a medicine; it is also a market-facing asset that carries therapeutic
positioning, physician trust, patient accessibility, sales strategy, promotional investment, and
competitive differentiation. Therefore, brand performance analytics needs to evaluate several
connected indicators rather than depen ding only on monthly sales volume. These indicators may
include sales growth, prescription share, market share, promotional response, regional contribution,
product adoption, physician conversion, repeat prescribing, channel productivity, and sales force

American Journal of Interdisciplinary Studies, December 2025, 351-393
360

effectiveness. Earlier research on pharmaceutical marketing communication has shown that marketing
communication affects product choice differently across product lifecycle stages, especially when
customers and prescribers need information to reduce uncertainty about new pharmaceutical products
(Abdur & Iftekhar, 2021; Narayanan et al., 2005). This idea is important for the present research because
pharmaceutical brand dashboards must not present brand performance as a single static number. They
need to show whether the brand is in a launch stage, growth stage, maturity stage, or decline stage,
because the meaning of sales movement and promotional response differs across these stages. A new
pharmaceutical brand may require analytics related to awareness, trial, physician adoption, and early
prescription growth, while a mature brand may require analytics related to retention, market share
defense, regional performance stability, and promotiona l efficiency. Therefore, pharmaceutical brand
performance analytics must combine commercial indicators with time -based interpretation. A
dashboarding and visualization framework using Tableau and Python becomes relevant in this context
because Python can structure and calculate brand-level indicators, while Tableau can present product
movement, regional comparison, lifecycle changes, and sales patterns in a visual and interactive format
for decision-makers.

Figure 2: Analytical Framework for Pharmaceutical Brand Performance Evaluation

Pharmaceutical brand performance is also strongly connected with promotional effectiveness because
pharmaceutical companies invest in several communication and promotional activities to influence
prescribing, pharmacy -level purchasing, product awareness, a nd brand preference. Promotional
activities may include detailing, physician meetings, samples, trade promotions, merchandising,
educational programs, digital communication, and pharmacy -level promotional techniques. A meta -
analysis of pharmaceutical promo tional expenditures has shown that promotional instruments can
affect pharmaceutical demand, although the size and nature of effectiveness may differ across
promotional tools, disease categories, and communication channels (Hasan & Uddin, 2022; Kremer et
al., 2008). This indicates that pharmaceutical brand performance analytics should not only report total
sales but should also examine whether promotional activities are producing measurable brand -level
outcomes. For example, a brand may show sales growth in one region because of stronger physician
engagement, while another region may remain weak due to poor promotional reach, low prescription
conversion, or limited pharmacy -level visibility. Resea rch on physician decision -making has also
shown that marketing actions and patient -related influences affect prescription behavior differently
across brands, and the effects may depend on drug characteristics such as effectiveness and side effects

American Journal of Interdisciplinary Studies, December 2025, 351-393
361

(Mohiul & Badrul, 2022 ; Venkataraman & Stremersch, 2007 ). This finding is highly relevant for
pharmaceutical brand analytics because ev ery brand cannot be interpreted through identical
commercial logic. Some brands may perform better because of therapeutic strength, while others may
depend more heavily on promotional communication, physician relationships, or market accessibility.
Therefore, a strong pharmaceutical brand analytics framework should allow managers to compare
product performance, promotional exposure, prescription outcomes, and brand characteristics
together. Tableau -based dashboards can support this need through brand -wise v isual comparison,
territory-level drill-down, and promotional KPI tracking. Python-based analysis can support this need
by calculating promotional productivity, identifying statistical relationships between promotional
variables and brand performance, and preparing reliable datasets for dashboard visualization. In this
way, pharmaceutical brand performance analytics becomes a structured process of connecting market
activity with measurable brand outcomes.
Pharmaceutical brand performance analytics has becom e more important because modern
pharmaceutical organizations increasingly depend on data -driven commercial systems, customer
relationship management platforms, sales force automation, and digital reporting tools. The value of
such analytics depends on whet her data can be transformed into usable insight for brand managers,
sales leaders, marketing teams, and business intelligence professionals. Recent empirical research on
pharmaceutical organizations has shown that big data analytics can improve sales perfo rmance by
strengthening customer relationship management capabilities, indicating that analytical capability has
direct relevance for pharmaceutical commercial performance (Kanti & Rony, 2022; Shahbaz et al., 2021).
This is important for the present study because brand performance analytics is not only a reporting
activity; it is also a decision-support process that helps organizations understand customers, territories,
product movement, sales opportunities, and promotional outcomes. Pharmacy-level research has also
shown that sales promotion techniques can influence consumers’ purchasing decisions at community
pharmacies, which means that pharmaceutical brand performance must consider market -facing
activities beyond internal sales numbers (Said et al., 2019; Sadia et al., 2022). This supports the idea that
a dashboarding and visualization framework should include indicators related t o promotional
effectiveness, customer response, pharmacy -level activity, regional sales movement, and brand
visibility. In a case-study-based pharmaceutical setting, such analytics can help identify whether brand
performance is being shaped by sales execut ion, prescription behavior, promotional activity, or
customer-level response. Python can strengthen this process through data cleaning, variable
preparation, descriptive analysis, correlation analysis, and regression modeling. Tableau can translate
the pro cessed results into interactive visual dashboards that allow users to compare brands, filter
regions, track KPIs, and interpret performance patterns. Therefore, pharmaceutical brand performance
analytics should be understood as an integrated analytical pra ctice where statistical processing and
visual communication work together. This understanding directly supports the present research
because the study examines how Tableau -based dashboarding capability, Python -based analytical
processing, dashboard usabili ty, data visualization quality, and analytics automation contribute to
pharmaceutical brand performance analytics effectiveness.
Business intelligence and dashboarding in pharmaceutical decision-making
Business intelligence and dashboarding have become imp ortant foundations for pharmaceutical
decision-making because pharmaceutical organizations need to transform scattered operational data
into timely, understandable, and action -oriented information. In pharmaceutical brand management,
decision-makers need t o monitor product performance, regional sales movement, prescription
behavior, promotional return, market share, customer response, and sales force activity through a
structured information environment. Business intelligence supports this process by connec ting data
storage, data preparation, analytical processing, reporting, and managerial interpretation within one
decision-support logic. Decision support systems research has emphasized that modern decision
environments require systems that can organize com plex data, support analytical reasoning, and
improve the quality of managerial decisions under uncertain and information -rich conditions (Arnott
& Pervan, 2008 ; Tohidul, 2023 ). This understanding is high ly relevant to pharmaceutical brand
performance analytics because brand managers often make decisions based on multiple indicators that
change across time, geography, customers, and product categories. A traditional report may show sales

American Journal of Interdisciplinary Studies, December 2025, 351-393
362

volume, but a busi ness intelligence dashboard can connect sales volume with territory achievement,
growth rate, prescription trend, promotional investment, and market share. In this way, dashboarding
strengthens the ability of pharmaceutical managers to observe patterns and  compare brand
performance from different angles. Business intelligence success research has also shown that BI
capability and decision environments influence the usefulness of analytics systems, meaning that
technology alone is not enough unless the system fits the decision problem and user needs (Isik et al.,
2013; Badrul & Mominul, 2023). This point is important for the present study because a pharmaceutical
dashboard should be designed according to the tasks of brand managers, sales managers, marketing
analysts, and business intelligence professionals. Tableau-based dashboards can provide an interactive
visual layer for such tasks, while Python can support the analytical layer by cleaning datasets,
preparing brand indicators, and generating statistical o utputs. Therefore, business intelligence and
dashboarding can be understood as connected decision-support mechanisms that help pharmaceutical
professionals move from raw data to brand-level insight.

Figure 3: Integrated Business Intelligence and Dashboarding Framework for Pharmaceutical Brand
Decision-Making

Dashboarding is particularly important in pharmaceutical decision-making because it allows decision-
makers to visualize performance indicators in a compact, interactive, and comparative format .
Pharmaceutical organizations commonly manage multiple brands, regions, sales teams, promotional
channels, and customer segments, which creates a need for dashboards that can simplify complex

American Journal of Interdisciplinary Studies, December 2025, 351-393
363

information without removing important analytical detail. Healthcare dashboard research has shown
that dashboards can support quality improvement and decision -making when they present relevant
indicators clearly and help users identify areas requiring attention (Dowding et al., 2015 ; Hossan &
Adar, 2023). Although this evidence has come from healthcare settings, the logic is strongly applicable
to pharmaceutical brand analytics because brand teams also need dashboards that highlight
performance gaps, unusual trends, and improvement areas. A brand dashboard can show which
products are achieving targets, which territories are underperf orming, which regions have stronger
prescription movement, and which promotional activities appear more productive. Business
intelligence maturity research has also indicated that analytical decision -making improves when
organizations develop stronger BI m aturity, data-oriented culture, and systematic use of information
(Popovič et al., 2012; Risha & Khalid, 2023). This means that pharmaceutical dashboarding should not
be treated only as a technical reporting e xercise; it should be treated as part of a broader analytical
decision culture. When managers use dashboards regularly, they can compare current performance
with previous performance, identify deviations from targets, and make more evidence -based brand
decisions. In the context of this study, Tableau can support such decision-making through KPI panels,
filter-based exploration, drill -down analysis, maps, and trend visualization. Python can support the
same process by preparing clean and reliable data before  visualization. The connection between
dashboarding and business intelligence is therefore essential because dashboard outputs are only
valuable when the underlying data are accurate, the indicators are relevant, and the visual design
supports managerial i nterpretation. For pharmaceutical brand performance analytics, this creates a
need for an integrated framework that links analytical processing with visual decision support.
Business intelligence and dashboarding also support pharmaceutical decision -making by improving
the speed, consistency, and reliability of performance interpretation. In many pharmaceutical
organizations, managers may receive reports from different departments, including sales operations,
marketing, distribution, prescription tracking, and customer relationship management. When these
reports are not integrated, decision -makers may face delays, inconsistent calculations, and difficulty
comparing indicators across brands and regions. Research on big data and organizational decision
processes has shown that data -based decision-making depends on the ability to process large and
varied information sources and convert them into usable knowledge for organizational decisions
(Kowalczyk & Buxmann, 2015; Hossan, 2024). This is highly relevant to pharmaceutical brand analytics
because brand performance data may include structured sales records, semi -structured promotional
reports, customer relationship management data, and region-wise market information. Dashboards can
improve this situation by centralizing key indicators and presenting them in a format that supports
rapid comparison and interpretation. At the same time, the quality of dashboard -driven decisions
depends on the reliability of analytical processing behind the dashboard. Python can help address this
requirement by supporting data cleaning, missing -value checking, variable preparation, descriptive
analysis, correlation analysis, and regression modeling. Tableau can then communicate the processed
results throu gh interactive dashboards that are understandable to non -technical decision -makers.
Research on the impact of business intelligence on decision quality has shown that BI can improve
decision-making when information quality and analytical use are aligned wi th managerial needs (Ali
et al., 2024 ; Wieder & Ossimitz, 2015 ). This finding supports the present research because
pharmaceutical brand performance analytics effectiveness depends on both the quality of the analytical
system and the usefulness of the visual interface. Therefore, business intelligence and dashboarding in
pharmaceutical decision-making should be understood as a combined process where data processing,
indicator design, visualization quality, user interaction, and statistical validation jointly support brand-
level decisions. This provides a clear foundation for examining Tableau-based dashboarding capability,
Python-based analytical processing, dashboard usability, data visualization quality, and analytics
automation as predictors of pharmaceutical brand performance analytics effectiveness.
Tableau-based visualization and dashboard usability
Tableau-based visualization is highly relevant to pharmaceutical brand performance analytics because
it provides an interactive environment where complex brand indicators can be converted into visible,
comparable, and decision-oriented information. In a pharmaceutical context, brand performance data
may include sales achievement, prescription volume, regional contribution, market share, promotional

American Journal of Interdisciplinary Studies, December 2025, 351-393
364

response, customer segmentation, product growth, and sales force activity. These indicators are often
difficult to interpret through static spreadsheet reports because brand managers need to compare
several dimensions at the same time. Tableau supports th is need by allowing dashboards to include
filters, drill-down options, trend lines, maps, KPI cards, bar charts, line charts, and interactive panels.
However, the usefulness of Tableau does not depend only on the availability of visual features. It
depends on whether the dashboard has been designed according to user needs, analytical tasks, and
the decision environment. Visualization evaluation research has shown that expert review can identify
important usability and design problems in visual interfaces, especially when visual tools are expected
to support interpretation and decision -making (Tory & Möller, 2005 ). This is important for
pharmaceutical dashboarding because a dashboard may contain accurate data but still fail if users
cannot understand the layout, interpret the chart, navigate filters, or connect visual indicators with
brand decisions. For example, a brand manager may need to identify why a product is declining in one
region, whether the decline is related to low prescription movement, weak promotional response, or
poor sales force coverage. A Tableau dashboard can make this type of interpretation easier when it is
designed around brand -level tasks rather than general reporting. Therefore, Tableau -based
visualization in this research has been considered as a structured decision -support mechanism that
helps pharmaceutical professionals transform raw performance records into meaningful visual insight.
Dashboard usability becomes a central issue because users must be able to move from overview to
detail, compare brands, detect patterns, and interpret performance differences without confusion.

Figure 4: Framework for Interactive Dashboard Visualization in Pharmaceutical Brand
Performance Analytics

Dashboard usability is also important because visualization quality depends on the relationship

American Journal of Interdisciplinary Studies, December 2025, 351-393
365

between user tasks, visual design, and evaluation purpose. Information visualization research has
explained that visualization evaluation can involve several scenarios, including user performance, user
experience, communication through visualization, workplace context, and visual reasoning (Lam et al.,
2012; Zaman, 2024). This view is highly useful for the present research because pharmaceutical
dashboards are not developed only to display data; they are developed to help users reason about
brand performance, identify underperforming areas, compare pharmaceutical products, and support
managerial decisions. A dashboard that performs well for one task may not perform well for another
task. For instance, an executive dashboard may need compact KPI indicator s, while a sales analytics
dashboard may need regional drill -down, product comparison, and time -series exploration. Design
study research has also emphasized that visualization systems should be developed through problem-
driven understanding of domain need s, data characteristics, user requirements, and validation
practices (Arif Uz et al., 2025 ; Sedlmair et al., 2012). This idea directly supports the case -study nature
of the current research because pharmaceutical brand analytics has its own domain -specific
requirements. A generic dashboard may not be enough for pharmaceutical brand performance because
brand decisions may require the simultaneous interpretation of therapeutic category, region, sales
target, prescription movement, promotional activity, and customer engagement. Tableau can support
these requirements through flexible dashboard construction, yet usability must be considered during
dashboard planning. If a dashboard includes too many charts, unclear labels, excessive colors, or
inconsistent filters, users may face information overload. If the dashboard is organized around clear
KPI hierarchy, l ogical navigation, and meaningful chart selection, users can interpret brand
performance more effectively. Therefore, dashboard usability in this study has been treated as a
measurable construct that influences pharmaceutical brand performance decision-support quality. This
construct includes ease of use, layout clarity, navigation simplicity, filter usefulness, chart readability,
and the ability to locate important brand indicators quickly.
Tableau-based visualization also becomes more valuable when it is aligned with clear analytical tasks
and adaptable dashboard design. Visualization task research has shown that tasks can be understood
through multiple levels, including why a user needs the visualization, what information is required,
and how visual interactions support the intended analytical goal (Brehmer & Munzner, 2013; Hossan,
2025). This task -based logic is important for pharmaceutical brand performance analytics because
different users interact with dashboards for different reasons. A brand manager may use the dashboard
to evaluate product growth, a sales manager may use it to compare territory achievement, a marketing
analyst may use it to examine promotional response, and a business intelligence professional may use
it to validate performance indicators. Therefore, a Tableau dashboard should not be designed as a single
static reporting page. It should be designed as an interactive decision environment where users can
answer different brand performance questions through filters, charts,  comparisons, and drill -down
paths. Healthcare dashboard research has also shown that adaptable visualization dashboards can
support quality improvement when they are designed around diverse metrics, user groups, and
organizational levels (Elshehaly et al., 2020; Ali et al., 2025). This finding is relevant to pharmaceutical
brand analytics because pharmaceutical organizations also involve multiple users and multiple
decision levels, such as national managers, regional managers, brand executives, marketing teams, and
sales analysts . Each group may require a different level of detail, but all users need reliable and
understandable visual information. Tableau can support this by allowing dashboard pages to be
organized around executive summaries, territory analysis, brand comparison, promotional tracking,
and trend monitoring. In this research, Tableau -based visualization has therefore been positioned as
the visible layer of the framework, while Python-based analytical processing supports the accuracy and
reliability of the data behind  the dashboard. The usability of the Tableau dashboard becomes a key
factor because users must trust the visual outputs, understand the indicators, and apply the information
to pharmaceutical brand performance decisions. Therefore, Tableau -based visualizat ion and
dashboard usability jointly support the effectiveness of pharmaceutical brand performance analytics.
Python-based analytical processing and automation
Python-based analytical processing refers to the use of Python programming tools, libraries, and
computational workflows to clean, transform, analyze, validate, and prepare data for decision-oriented
interpretation. In the context of pharmaceutical brand performance analytics, Python is especially

American Journal of Interdisciplinary Studies, December 2025, 351-393
366

important because raw brand data may come from differe nt sources, including sales records,
prescription reports, promotional activity sheets, regional performance files, customer relationship
management exports, and manually prepared spreadsheets. These data sources may contain missing
values, duplicate records, inconsistent product names, different regional coding systems, irregular date
formats, and unstructured promotional variables. Before any Tableau dashboard can provide
trustworthy visualization, the data must be prepared in a consistent and analyticall y reliable format.
Python supports this requirement by allowing analysts to create repeatable scripts for data cleaning,
variable transformation, grouping, aggregation, filtering, and statistical preparation. Interactive
scientific computing research has shown that Python environments can support exploratory analysis,
visualization, and computational work through flexible interaction between code, data, and output
(Pérez & Granger, 2007 ). This is highly relevant for pharmaceutical brand analytics because analysts
often need to test several performance views before finalizing dashboard indicators. For example, they
may need to calculate monthly sales growth, territory contribution, prescription share, market share
movement, promotional productivity, and brand ranking before those indicators can be visualized in
Tableau. Python also allo ws the same analytical logic to be reused across reporting periods, which
reduces repetitive manual work and improves consistency. In this research, Python -based analytical
processing is therefore treated as the backend foundation of the dashboarding and v isualization
framework. Tableau can make brand performance information visible and interactive, but Python
strengthens the reliability of the information that enters the dashboard. This makes Python -based
processing important for statistical accuracy, data  preparation, and analytical trustworthiness in
pharmaceutical brand performance analytics.

Figure 5: Python-Based Data Processing and Automation Framework for Pharmaceutical Decision
Support

Python also supports the statistical analysis requirements of this study because the research design uses
descriptive statistics, correlation analysis, and regression modeling to test relationships among the
major variables. In a quantitative, cross -sectional, case -study-based study, the researcher needs to
summarize survey responses, check variable distributions, examine relationships among constructs,
and test whether dashboarding and visualization capabilities significantly predict pharmaceutical
brand performance analytics effectiveness. Python can support these tasks through statistical libraries
and model-building environments that allow researchers to run repeatable and transparent analyses.

American Journal of Interdisciplinary Studies, December 2025, 351-393
367

Statistical modeling research in Python has shown that Pytho n-based tools can support econometric
and statistical modeling, including regression analysis, model estimation, diagnostics, and statistical
interpretation (Seabold & Perktold, 2010 ). This is directly connected with the present study because
regression modeling is needed to test whether Tableau -based dashboarding capability, Python-based
analytical processing, dashboard usability, data visualization quality, and analytics automation explain
variation in pharmaceutical brand performance analytics effectiveness. Python can also help create
correlation matrices, reliability summaries, descriptive tables, and clean datasets that can later be
exported to Tableau or other visualization tools. The use of computational notebooks has further
strengthened Python-based research workflows because notebooks allow code, results, explana tions,
tables, and visual outputs to be combined in a single readable and executable environment (Kluyver et
al., 2016). This is useful for pharmaceutical analytics because the analyst can d ocument how raw data
have been cleaned, how variables have been calculated, how statistical tests have been performed, and
how dashboard-ready outputs have been generated. Such documentation improves transparency in
the analytical process. In this study, Python has not been positioned only as a programming language.
It has been positioned as an analytical processing environment that supports data validation, statistical
modeling, workflow documentation, and preparation of reliable brand performance datasets  for
Tableau-based dashboarding.
Automation is another important dimension of Python -based analytical processing because
pharmaceutical brand performance reporting is usually repeated across months, quarters, regions,
brands, and product portfolios. When analysts manually prepare the same reports again and again, the
reporting process becomes time -consuming and exposed to calculation errors, formatting
inconsistencies, and delayed decision-making. Python can reduce these problems by automating data
import, cleaning, transformation, statistical summarization, and export procedures. This is especially
important for a pharmaceutical dashboarding framework because Tableau dashboards become more
useful when they are supported by regularly refreshed and consistent ly prepared datasets. Python -
based visual analytics tools also help analysts explore data before final dashboard development.
Research on interactive statistical visualization in Python has shown that declarative visualization tools
can connect data transf ormation with statistical visualization, making it easier to represent analytical
relationships clearly (VanderPlas et al., 2018). This supports the present study because Python can be
used not only for backend cleaning but also for preliminary visual analysis before final Tableau
dashboard construction. Reproducibility is also important in automated analytics  workflows because
decision-makers need confidence that results can be regenerated from the same data and procedures.
Research on computational notebooks has emphasized that shared analytical workflows should
include clear organization, annotation, reusabl e code, and accessible outputs to improve
reproducibility and interpretation (Rule et al., 2019). This is strongly relevant to pharmaceutical brand
performance analytics because a dashboard is more trustworthy when the data pipeline behind it is
documented and repeatable. In this research, Python -driven analytical workflow va lidation can
therefore evaluate whether Python improves data accuracy, reduces manual errors, supports statistical
testing, and prepares reliable dashboard inputs. The automation capability of Python strengthens the
overall framework by making the analytic s process faster, more consistent, and more transparent.
Therefore, Python-based analytical processing and automation provide the computational foundation
for the proposed Tableau and Python-based pharmaceutical brand performance analytics framework.
Theoretical framework: Information Systems Success Model
The theoretical framework of this study is based on the Information Systems Success Model because
the proposed Tableau and Python-based dashboarding and visualization framework is an information
system that needs to be evaluated through quality, usability, user satisfaction, analytical value, and
performance benefit. In this research, the dashboarding and visualization framework is not viewed
only as a technical arrangement of Tableau dashboards and Python  scripts. It is viewed as a decision-
support information system that receives pharmaceutical brand data, processes the data through
Python, presents the data through Tableau, and supports brand performance interpretation by
managers and analysts. The Information Systems Success Model is suitable for this research because it
explains how system quality and information quality influence user satisfaction, system use, and net
benefits. The theoretical structure can be written in LaTeX equation format as:

American Journal of Interdisciplinary Studies, December 2025, 351-393
368

𝐼𝑆 𝑆𝑢𝑐𝑐𝑒𝑠𝑠 = 𝑓(𝑆𝑄, 𝐼𝑄, 𝑈, 𝑈𝑆, 𝑁𝐵)

Here, 𝑆𝑄represents system quality, 𝐼𝑄represents information quality, 𝑈represents system use,
𝑈𝑆represents user satisfaction, and 𝑁𝐵represents net benefits. In the context of this study, the theory
can be adapted as:
𝑃𝐵𝑃𝐴𝐸 = 𝑓(𝑇𝐷𝐶, 𝑃𝐴𝑃, 𝐷𝑈, 𝐷𝑉𝑄, 𝐴𝐴)

Here, represents pharmaceutical brand performance analytics effectiveness, represents Tableau-based
dashboarding capability, represents Python -based analytical processing, represents dashboard
usability, represents data visualization quality, and represents analytics automation. An empirical test
of the DeLone and McLean model has shown that perceived system quality and perceived information
quality can significantly predict user satisfaction, while system quality can also influence system use in
a mandatory information system context (Iivari, 2005). This idea is highly relevant for pharmaceutical
brand performance analytics because users may depend on dashboards as part of regular reporting
routines. If the dashboard is easy to use, interactive, fast, organized, and visually understandable, users
are more likely to trust it and use it for brand-level decision-making. Similarly, if the information shown
in the dashboard is accurate, timely, complete, and relevant, users are more likely  to consider the
dashboard useful for evaluating sales trends, prescription movement, regional performance, and
promotional outcomes. Therefore, the Information Systems Success Model provides a strong
foundation for linking technological features, analytic al processing, visual communication, user
interaction, and decision-support effectiveness within one research model.

Figure 6: Information Systems Success Model for Pharmaceutical Brand Performance Analytics

The Information Systems Success Model is also useful because it allows the study to convert theoretical
dimensions into measurable variables for quantitative analysis. Previous IS success research has argued
that system success should be understood as a multidimensional impact rather than a single technical
outcome, and this view is important for the present research because dashboard success cannot be
measured only by whether a dashboard exists or whether Python code has been used (Gable et al.,
2008). A pharmaceutical dashboard may be technically complete, but it may still have limited value if

American Journal of Interdisciplinary Studies, December 2025, 351-393
369

users cannot understand the visual outputs, if the information is incomplete, if the dashboard does not
match decision tasks, or if the analytical backend does not provide reliable results. In this research, the
theoretical model has been adapted to the specific context of pharmaceutical brand performance
analytics by identifying five independent variables: Tableau -based dashboarding capability, Python -
based analytical processing, dashboard usability, data visualization quality, and analytics automation.
These variables jointly represent the system, information, analytical, usability, and automation
dimensions of the framework. The dependent variable is pharmaceutical brand performance analytics
effectiveness, which represents the perceived net benefit of the proposed system. The main formula
that will be applied throughout the study is the multiple regression model:
𝑃𝐵𝑃𝐴𝐸𝑖 = 𝛽0 + 𝛽1𝑇𝐷𝐶𝑖 + 𝛽2𝑃𝐴𝑃𝑖 + 𝛽3𝐷𝑈𝑖 + 𝛽4𝐷𝑉𝑄𝑖 + 𝛽5𝐴𝐴𝑖 + 𝜀𝑖

In this formula, 𝑃𝐵𝑃𝐴𝐸𝑖means pharmaceutical brand performance analytics effectiveness for
respondent 𝑖, 𝑇𝐷𝐶𝑖means Tableau-based dashboarding capability, 𝑃𝐴𝑃𝑖means Python-based analytical
processing, 𝐷𝑈𝑖means dashboard usability, 𝐷𝑉𝑄𝑖means data visualization quality, 𝐴𝐴𝑖means analytics
automation, 𝛽0means the constant, 𝛽1to 𝛽5mean the regression coefficients, and 𝜀𝑖means the error term.
This formula is the best fit for the whole study because it directly tests whether the main framework
components significantly predict pharmaceutical brand performance analytics effectiveness. It also
connects the theoretical framework with the statistical method because the research design depends on
descriptive statistics, correlation analysis, and regression modeling.
The theoretical framework further supports this research because it explains why the integration of
Tableau and Python should be evaluated through both technical quality and decision value. Studies on
information system quality have shown that system quality, information quality, and service quality
can create organizational impact when these quality dimensions are strong and aligned with user needs
(Gorla et al., 2010). In the present study, this means that Tableau dashboards should not only be visually
attractive; they should also provide reliable, usable, and decision -relevant brand performance
information. Python-based analytical processing should not only produce numerical results; it should
also improve da ta accuracy, reduce manual reporting errors, support statistical testing, and prepare
dashboard-ready datasets. The adapted theoretical relationship for the study can also be expressed as:
𝑁𝑒𝑡 𝐵𝑒𝑛𝑒𝑓𝑖𝑡 = 𝐴𝑛𝑎𝑙𝑦𝑡𝑖𝑐𝑠 𝐸𝑓𝑓𝑒𝑐𝑡𝑖𝑣𝑒𝑛𝑒𝑠𝑠
𝐴𝑛𝑎𝑙𝑦𝑡𝑖𝑐𝑠 𝐸𝑓𝑓𝑒𝑐𝑡𝑖𝑣𝑒𝑛𝑒𝑠𝑠
= 𝐷𝑎𝑠ℎ𝑏𝑜𝑎𝑟𝑑 𝑄𝑢𝑎𝑙𝑖𝑡𝑦 + 𝐴𝑛𝑎𝑙𝑦𝑡𝑖𝑐𝑎𝑙 𝑄𝑢𝑎𝑙𝑖𝑡𝑦 + 𝑈𝑠𝑎𝑏𝑖𝑙𝑖𝑡𝑦 + 𝑉𝑖𝑠𝑢𝑎𝑙𝑖𝑧𝑎𝑡𝑖𝑜𝑛 𝑄𝑢𝑎𝑙𝑖𝑡𝑦
+ 𝐴𝑢𝑡𝑜𝑚𝑎𝑡𝑖𝑜𝑛

In variable form, this becomes:
𝑃𝐵𝑃𝐴𝐸 = 𝑇𝐷𝐶 + 𝑃𝐴𝑃 + 𝐷𝑈 + 𝐷𝑉𝑄 + 𝐴𝐴

Research on employee portal success has shown that information quality, system quality, and
collaboration quality can influence user satisfaction and perceived usefulness in information system
environments (Urbach et al., 2010). This finding is relevant because pharmaceutical brand dashboards
also depend on users’ perceptions of usefulness, clarity, and trust. Brand managers, sales managers,
marketing analysts, and business intelligence professionals are more likely to depend on a dashboard
when it hel ps them compare brands, interpret regional performance, identify weak territories, and
understand promotional response. IS success research in digital service environments has also
validated the importance of information quality, system quality, service qu ality, use, satisfaction, and
perceived net benefit as connected success dimensions (Wang & Liao, 2008). Therefore, the Information
Systems Success Model has been applied in this study as the main theoretical lens for evaluating the
proposed dashboarding and visualization framework. The  model supports the hypotheses by
explaining that Tableau -based dashboarding capability, Python -based analytical processing,
dashboard usability, data visualization quality, and analytics automation should positively contribute
to pharmaceutical brand perf ormance analytics effectiveness. This theoretical alignment makes the
study more coherent because the same model guides the variable selection, questionnaire development,
hypothesis formation, statistical testing, framework validation, and interpretation of results.
Conceptual framework and hypothesis development

American Journal of Interdisciplinary Studies, December 2025, 351-393
370

The conceptual framework of this study has been developed to explain how Tableau -based
dashboarding capability, Python-based analytical processing, dashboard usability, data visualization
quality, and analytics automation contribute to pharmaceutical brand performance analytics
effectiveness. A conceptual framework is important because it converts the theoretical foundation of
the study into a measurable research model that can be tested through qua ntitative analysis. In this
research, the framework has treated pharmaceutical brand performance analytics effectiveness as the
dependent variable because the main purpose of the study is to evaluate whether the proposed Tableau
and Python-based dashboarding and visualization framework can support better brand monitoring,
faster insight generation, more accurate reporting, and stronger decision support. The independent
variables have been selected based on the logic that pharmaceutical brand analytics requi res both
analytical reliability and visual interpretability. Tableau-based dashboarding capability represents the
system’s ability to present sales trends, regional performance, prescription movement, promotional
response, market share, and brand ranking t hrough interactive dashboards. Python -based analytical
processing represents the ability to clean data, prepare variables, calculate indicators, conduct
descriptive statistics, perform correlation analysis, and support regression modeling. Dashboard
usability represents the user’s ability to navigate, understand, and apply dashboard outputs. Data
visualization quality represents the clarity, accuracy, appropriateness, and interpretability of visual
displays. Analytics automation represents the ability to re duce manual reporting effort, improve
timeliness, and support repeatable analytical workflows. Prior research on big data analytics capability
has shown that analytics value is created when data, technology, technical skills, and managerial
capability are organized into a coherent capability structure (Gupta & George, 2016).

Figure 7: Conceptual framework and hypothesis development

This logic supports the present conceptual framework because the research does not examine Tableau
or Python as isolated tools. Instead, it examines them as connected capabilities that support
pharmaceutical brand performance analytics. The basic conceptual relationship can therefore be
expressed as:
𝑃𝐵𝑃𝐴𝐸 = 𝑓(𝑇𝐷𝐶, 𝑃𝐴𝑃, 𝐷𝑈, 𝐷𝑉𝑄, 𝐴𝐴)

where 𝑃𝐵𝑃𝐴𝐸represents pharmaceutical brand performance analytics effectiveness, 𝑇𝐷𝐶represents
Tableau-based dashboarding capability, 𝑃𝐴𝑃represents Python -based analytical processing,
𝐷𝑈represents dashboard usability, 𝐷𝑉𝑄represents data visualization quality, and 𝐴𝐴represents
analytics automation.

American Journal of Interdisciplinary Studies, December 2025, 351-393
371

The hypothesis development of this study has followed t he assumption that pharmaceutical brand
performance analytics effectiveness increases when dashboarding, analytical processing, usability,
visualization quality, and automation are strong. The first hypothesis proposes that Tableau -based
dashboarding capab ility has a significant positive effect on pharmaceutical brand performance
analytics effectiveness because interactive dashboards can help users compare brands, inspect
territories, identify performance gaps, and interpret trends more efficiently. The sec ond hypothesis
proposes that Python -based analytical processing has a significant positive effect on pharmaceutical
brand performance analytics effectiveness because cleaned data, structured variables, reliable statistical
analysis, and repeatable workflows can improve the trustworthiness of dashboard outputs. The third
hypothesis proposes that dashboard usability has a significant positive effect on pharmaceutical brand
performance decision-support quality because users are more likely to apply a dashboard  when it is
easy to understand, logically arranged, and aligned with their decision tasks. The fourth hypothesis
proposes that data visualization quality has a significant positive effect on pharmaceutical brand
performance analytics effectiveness because clear visual design improves interpretation, comparison,
and insight generation. The fifth hypothesis proposes that analytics automation has a significant
positive effect on reporting accuracy and timeliness because automated processing can reduce manual
errors and improve reporting speed. The sixth hypothesis proposes that integrated Tableau and Python
analytics capability significantly predicts pharmaceutical brand performance analytics effectiveness
because the overall system depends on both visual dashb oarding and analytical backend reliability.
Prior business analytics research has shown that analytics capability contributes to business value when
it supports the movement from analysis to insight, decision, and action (Seddon et al., 2017 ). This
pathway directly fits the present framework because Python supports analysis, Tableau supports
insight presentation, managers use the dashboard for decision -making, and pharmaceutical brand
performance analytics effectiveness represents the action -oriented value of the framework. Research
on analytics capab ility and strategy alignment has also shown that analytics creates stronger
performance outcomes when analytical capability is aligned with business strategy (Akter et al., 2016).
Therefore, the hypotheses of this study are aligned with the idea that pharmaceutical brand analytics
becomes more effective when technical tools are connected with brand-level decision needs.
The final conceptual framework has also been designed to support the statistical testing strategy of the
study. Since the study is quantitative, cross-sectional, and case-study-based, the conceptual model must
be measurable through survey items and testable through descriptive statistics, correlation analysis,
and regression modeling. Each indepe ndent variable will be measured through multiple Likert -scale
items, and the dependent variable will also be measured through items related to decision -support
quality, reporting accuracy, timely insight, brand monitoring effectiveness, and managerial usefulness.
The main regression formula for hypothesis testing can be written as:
𝑃𝐵𝑃𝐴𝐸𝑖 = 𝛽0 + 𝛽1𝑇𝐷𝐶𝑖 + 𝛽2𝑃𝐴𝑃𝑖 + 𝛽3𝐷𝑈𝑖 + 𝛽4𝐷𝑉𝑄𝑖 + 𝛽5𝐴𝐴𝑖 + 𝜀𝑖

In this equation, means pharmaceutical brand performance analytics effectiveness for respondent ,
means the constant, to represent the regression coefficients for the five predictors, and represents the
error term. This formula is suitable for the whole study because it directly tests whether the proposed
framework components explain variation in pharmaceutical brand performance analytics effectiveness.
Research on big data analytics value has shown that analytics capability can create business value when
it supports agility, knowledge use, and performance improvement (Côrte-Real et al., 2017 ). This
strengthens the framework because pharmaceutical brand analytics also requires faster interpretation
of market changes, territory performance, and promotional outcomes. Data visualization research has
also shown that visualization can influence decision-making by improving understanding, perception,
and interpretation of information (Park et al., 2021 ). This supports the inclusion of data visualization
quality and dashboard usability in the model. Therefore, the conceptual framework of this study has
linked analytical processing, dashboarding capability, usability, visualization quality, and automation
with pharmaceutical brand performance analytics effectiveness. This framework provides the
foundation for questionnaire development, hypothesis testing, regr ession modeling, dashboard
prototype evaluation, Python -driven workflow validation, and final framework validation in the
results chapter.

American Journal of Interdisciplinary Studies, December 2025, 351-393
372

METHODS
This study has adopted a quantitative, cross -sectional, case-study–based research design to examine
the devel opment of a dashboarding and visualization framework for pharmaceutical brand
performance analytics using Tableau and Python. The quantitative design has been selected because
the study has measured the relationships among Tableau -based dashboarding capabi lity, Python -
based analytical processing, dashboard usability, data visualization quality, analytics automation, and
pharmaceutical brand performance analytics effectiveness through numerical survey responses. The
cross-sectional design has been used becau se data have been collected from respondents at a single
point in time, allowing the researcher to capture their perceptions regarding dashboarding,
visualization, analytics processing, and brand performance decision support within the selected
pharmaceutical analytics context. The case study context has focused on pharmaceutical brand
performance monitoring, where brand managers, sales managers, marketing executives, business
intelligence analysts, data analysts, territory managers, and decision -makers have been involved in
using or interpreting sales reports, prescription trends, promotional indicators, regional performance
records, and product -level performance dashboards. The population of the study has therefore
included pharmaceutical professionals who have had direct or indirect involvement in brand analytics,
sales reporting, marketing analysis, dashboard interpretation, or data-supported decision-making. The
unit of analysis has been the individual respondent because the study has measured the percep tion,
experience, and evaluation of each participant regarding the proposed Tableau and Python -based
analytics framework.

Figure 8: Methodological Framework of the Study

The study has used a purposive sampling strategy because the respondents have been selected based
on their relevance to pharmaceutical brand performance analytics, dashboard use, business
intelligence, or managerial reporting. This sampling strategy has been appropriate because the research
has required informed respondents who have  understood pharmaceutical brand performance
indicators and data -driven decision -making practices. Primary data have been collected through a
structured questionnaire designed with a five -point Likert scale, where 1 has represented strongly
disagree, 2 has  represented disagree, 3 has represented neutral, 4 has represented agree, and 5 has
represented strongly agree. The data collection procedure has involved distributing the questionnaire
to eligible pharmaceutical professionals through online forms, direct  communication, and
organizational or professional networks. The instrument design has included construct-based items for
Tableau-based dashboarding capability, Python-based analytical processing, dashboard usability, data
visualization quality, analytics automation, and pharmaceutical brand performance analytics
effectiveness. The questionnaire has also included demographic items such as job role, department,
work experience, analytics familiarity, and exposure to dashboard-based reporting.
A pilot test has been conducted before the final data collection to check whether the questionnaire items

American Journal of Interdisciplinary Studies, December 2025, 351-393
373

have been clear, understandable, relevant, and aligned with the research objectives. Feedback from the
pilot test has been used to refine unclear word ing, remove repetitive items, and improve the logical
flow of the instrument. Validity has been ensured through literature -based item development, expert
review, and alignment among the research title, objectives, hypotheses, variables, and questionnaire
items. Reliability has been tested through Cronbach’s alpha to confirm the internal consistency of each
construct, with values of .70 or above considered acceptable for the study. SPSS has been used for data
coding, descriptive statistics, reliability analysis, correlation analysis, and regression modeling. Python
has been used for data cleaning, preprocessing, analytical workflow validation, and preparation of
dashboard-ready datasets. Tableau has been used for dashboard prototype development, KPI
visualization, filter-based exploration, and framework demonstration. Microsoft Excel has been used
for initial data organization, screening, and tabulation. EndNote has been used for reference
management, citation organization, and APA 7th edition formatting suppo rt. Through these
methodological procedures, the study has established a structured approach for testing the proposed
dashboarding and visualization framework for pharmaceutical brand performance analytics.
DATA ANALYSIS AND PRESENTATION
Response rate and demographic profile

Table 1: Response rate and demographic profile of respondents

Variable Category Frequency Percentage Result interpretation
Questionnaires
distributed Total distributed 250 100.0% Initial survey target
Questionnaires
returned Returned responses 226 90.4% Strong participation
Valid responses Usable responses 214 85.6% Final sample for analysis
Invalid/incomplete
responses Removed responses 12 4.8% Excluded from analysis
Job role Sales/territory managers 61 28.5% Largest respondent group
Job role Brand/product managers 53 24.8% Strong brand-level representation
Job role Marketing executives 39 18.2% Relevant to promotional analytics
Job role BI/data analysts 32 15.0% Relevant to dashboard and Python analytics
Job role Senior decision- makers/supervisors 29 13.5% Relevant to strategic decision support
Experience 1–3 years 73 34.1% Early to mid-career users
Experience 4–7 years 82 38.3% Largest experience group
Experience More than 7 years 59 27.6% Experienced decision users
Dashboard familiarity Low 31 14.5% Limited exposure
Dashboard familiarity Moderate 96 44.9% Practical exposure
Dashboard familiarity High 87 40.6% Strong dashboard exposure

Table 1 has shown that the study has achieved a strong response pattern and a suitable respondent
profile for examining the dashboarding and visualization framework for pharmaceutical brand
performance analytics. Out of 250 distributed questionnaires, 226 responses have been returned, and
214 responses have been retained as valid for final analysis, creating a valid response rate of 85.6%.

American Journal of Interdisciplinary Studies, December 2025, 351-393
374

This response rate has been sufficient for a quantitative, cross -sectional, case -study-based study
because it has provi ded enough observations for descriptive statistics, reliability analysis, correlation
analysis, and regression modeling. The demographic profile has also supported the relevance of the
sample because respondents have come from job roles directly connected with pharmaceutical brand
performance, sales reporting, marketing analytics, business intelligence, and decision -making. Sales
and territory managers have represented the largest group at 28.5%, followed by brand or product
managers at 24.8%, marketing exe cutives at 18.2%, BI or data analysts at 15.0%, and senior decision -
makers or supervisors at 13.5%. This distribution has indicated that the sample has not depended on
only one category of users; instead, it has included both business users and technical users of analytics.
This has strengthened the study because Tableau -based dashboarding capability and Python -based
analytical processing have needed evaluation from people who understand brand decisions as well as
people who understand data preparation and reporting. The experience profile has also supported the
credibility of the results, as 38.3% of respondents have had 4–7 years of experience and 27.6% have had
more than 7 years of experience. This has suggested that most respondents have had enough
professional exposure to evaluate pharmaceutical brand performance analytics. Dashboard familiarity
has further supported the study, as 44.9% have reported moderate familiarity and 40.6% have reported
high familiarity. In relation to the Information Systems Suc cess Model, this demographic profile has
supported the user-use context of the theory because system quality, information quality, usability, and
net benefits can be meaningfully assessed only by users who have practical involvement with
information system s and decision processes. Therefore, Table 1 has supported the methodological
foundation of the study and has confirmed that the respondent group has been appropriate for proving
the study objectives and testing the hypotheses.
Descriptive statistics of the study variables

Table 2: Descriptive statistics of major study variables based on five-point Likert scale

Variable
code Study variable Mean Standard deviation Likert interpretation Rank
DVQ Data visualization quality 4.18 0.61 High agreement 1
DU Dashboard usability 4.13 0.64 High agreement 2
TDC Tableau-based dashboarding capability 4.09 0.66 High agreement 3
PBPAE Pharmaceutical brand performance analytics effectiveness 4.05 0.63 High agreement 4
AA Analytics automation 3.98 0.69 Agreement 5
PAP Python-based analytical processing 3.92 0.71 Agreement 6

Table 2 has presented the descriptive statistics of the major variables of the study and has shown that
respondents have generally agreed with the usefulness of the proposed dashboarding and visualization
framework for pharmaceutical brand performance anal ytics. Since the study has used a five -point
Likert scale, a mean score above 3.50 has indicated agreement, while a mean score above 4.00 has
indicated strong agreement. Data visualization quality has received the highest mean score of 4.18 with
a standard deviation of 0.61, which has indicated that respondents have viewed visual clarity, chart
appropriateness, KPI readability, brand comparison, and visual interpretation as the strongest parts of
the proposed framework. This result has supported the objecti ve related to evaluating the role of
visualization quality in pharmaceutical brand performance analytics. Dashboard usability has ranked
second with a mean score of 4.13 and a standard deviation of 0.64, showing that respondents have
positively evaluated dashboard navigation, layout clarity, filter usefulness, and ease of understanding.
Tableau-based dashboarding capability has ranked third with a mean score of 4.09 and a standard
deviation of 0.66, indicating strong agreement that Tableau can support interactive reporting, territory
comparison, brand-level KPI monitoring, and drill-down analysis. Pharmaceutical brand performance
analytics effectiveness has recorded a mean score of 4.05, showing that respondents have perceived the

American Journal of Interdisciplinary Studies, December 2025, 351-393
375

framework as useful for bra nd monitoring, reporting accuracy, timely insight generation, and
managerial decision support. Analytics automation has recorded a mean of 3.98, while Python -based
analytical processing has recorded a mean of 3.92. These values have still indicated positive agreement,
although they have ranked slightly lower than visualization and usability, possibly because more
respondents have been business users than technical users. From the perspective of the Information
Systems Success Model, these descriptive findin gs have shown that system quality, information
quality, usability quality, and perceived net benefit have all been positively evaluated. The high scores
for visualization quality, dashboard usability, and Tableau capability have supported the system
quality and user satisfaction logic of the theory, while the positive scores for Python analytical
processing and analytics automation have supported the information quality and analytical reliability
dimensions. Therefore, Table 2 has provided initial descriptive support for the research objectives and
has indicated that all variables have been suitable for further correlation and regression testing.
Reliability analysis
Table 3: Reliability analysis of measurement constructs

Construct
code Construct name Number of items Cronbach’s alpha Reliability level Decision
TDC Tableau-based dashboarding capability 5 .86 Good Accepted
PAP Python-based analytical processing 5 .84 Good Accepted
DU Dashboard usability 5 .88 Good Accepted
DVQ Data visualization quality 5 .87 Good Accepted
AA Analytics automation 5 .81 Good Accepted
PBPAE
Pharmaceutical brand
performance analytics
effectiveness
5 .89 Good Accepted
Overall
instrument All measurement items 30 .91 Excellent Accepted

Table 3 has presented the reliability analysis of the research instrument and has confirmed that the
measurement scales used in the study have been internally consistent. Cronbach’s alpha has been used
to assess reliability because the study has measured each construct through multiple Likert-scale items.
A Cronbach’s alpha value of .70 or above has been considered acceptable, while values above .80 have
indicated good reliability. The results have shown that all constructs have exceeded the accepted
reliability threshold. Pharmaceutical brand performance analytics effectiveness has produced the
highest construct-level alpha value at .89, indicating that the items measuring decision-support quality,
reporting accuracy, timely insight, brand monitoring effect iveness, and managerial usefulness have
been highly consistent. Dashboard usability has recorded an alpha value of .88, while data visualization
quality has recorded .87 and Tableau -based dashboarding capability has recorded .86. These values
have confirmed that the items related to dashboard navigation, filter use, KPI visibility, visual clarity,
chart readability, and interactive dashboard capability have measured their intended constructs
reliably. Python-based analytical processing has recorded an alpha value of .84, confirming that items
related to data cleaning, statistical processing, regression support, workflow repeatability, and
analytical reliability have been consistent. Analytics automation has recorded the lowest but still good
alpha value of . 81, which has indicated that automated reporting, reduced manual error, repeatable
processing, faster analysis, and timely dashboard updating have formed a reliable construct. The
overall questionnaire has produced a Cronbach’s alpha value of .91, showing excellent internal
consistency across all thirty measurement items. These reliability results have been important for
proving the objectives and hypotheses because unreliable measures would weaken the validity of
correlation and regression findings. In relation to the Information Systems Success Model, the reliability

American Journal of Interdisciplinary Studies, December 2025, 351-393
376

of these constructs has shown that the adapted theoretical dimensions have been measured coherently.
Tableau capability has reflected system quality, Python processing has reflected informatio n and
analytical quality, dashboard usability has reflected use -related quality, visualization quality has
reflected information presentation quality, automation has reflected process quality, and
pharmaceutical brand performance analytics effectiveness has reflected net benefit. Therefore, Table 3
has supported the measurement strength of the study and has justified the use of the variables in further
statistical testing.
Correlation analysis

Table 4: Pearson correlation matrix among study variables

Variable TDC PAP DU DVQ AA PBPAE
TDC 1
PAP .49** 1
DU .58** .46** 1
DVQ .61** .51** .63** 1
AA .44** .56** .48** .50** 1
PBPAE .62** .57** .65** .68** .55** 1
Note. **p < .001. TDC = Tableau -based dashboarding capability; PAP = Python-based analytical
processing; DU = Dashboard usability; DVQ = Data visualization quality; AA = Analytics automation;
PBPAE = Pharmaceutical brand performance analytics effectiveness.

Table 4 has presented the Pearson correlation results and has show n that all independent variables
have had positive and statistically significant relationships with pharmaceutical brand performance
analytics effectiveness. The strongest correlation has been found between data visualization quality
and pharmaceutical bra nd performance analytics effectiveness, with r = .68 and p < .001. This has
indicated that respondents who have perceived higher visualization quality have also perceived
stronger analytics effectiveness. This result has supported H4 and the objective rela ted to evaluating
how visual clarity, chart appropriateness, and KPI readability improve pharmaceutical brand
interpretation. Dashboard usability has shown the second strongest relationship with pharmaceutical
brand performance analytics effectiveness, wit h r = .65 and p < .001. This has supported H3 and has
shown that ease of navigation, layout clarity, and filter usefulness have been strongly related to
decision-support quality. Tableau -based dashboarding capability has shown a strong positive
correlation with the dependent variable, with r = .62 and p < .001, supporting H1 and indicating that
interactive dashboarding, drill -down analysis, territory comparison, and KPI monitoring have been
important for effective brand performance analytics. Python -based a nalytical processing has also
shown a significant positive relationship with pharmaceutical brand performance analytics
effectiveness, with r = .57 and p < .001, supporting H2 and confirming that data cleaning, statistical
modeling, and reliable analytical  preparation have contributed to stronger analytics outcomes.
Analytics automation has shown a positive correlation of r = .55 and p < .001, supporting H5 and
indicating that automated reporting, faster data preparation, and reduced manual errors have been
related to improved brand performance reporting. The inter-correlations among independent variables
have also been positive but not excessively high, suggesting that the variables have been related but
conceptually distinct. For example, Tableau capabilit y and data visualization quality have correlated
at .61, while Python processing and analytics automation have correlated at .56. These results have
made sense because dashboarding, visualization, automation, and analytical processing work together
in an i ntegrated framework. In relation to the Information Systems Success Model, the correlation
findings have shown that system quality, information quality, usability, and process automation have
all been associated with perceived net benefits. Therefore, Tabl e 4 has provided strong preliminary
evidence for the hypotheses and has justified the need for regression analysis to test the predictive
strength of the proposed framework.

American Journal of Interdisciplinary Studies, December 2025, 351-393
377

Regression model for dashboarding and visualization capability

Table 5: Multiple regression model predicting pharmaceutical brand performance analytics
effectiveness

Predictor variable Unstandardized B Standard error Standardized beta t- value p- value Hypothesis result
Constant 0.61 0.22 — 2.77 .006 —
Tableau-based
dashboarding capability 0.20 0.06 .21 3.14 .002 H1 supported
Python-based analytical
processing 0.16 0.06 .18 2.78 .006 H2 supported
Dashboard usability 0.23 0.06 .24 3.91 < .001 H3 supported
Data visualization
quality 0.30 0.07 .29 4.42 < .001 H4 supported
Analytics automation 0.14 0.06 .15 2.39 .018 H5 supported

Table 6: Regression model summary

Model indicator Value Interpretation
R .734 Strong combined relationship
R² .539 53.9% variance explained
Adjusted R² .528 Stable explanatory power
F-value 48.72 Model has been significant
df 5, 208 Predictor and residual degrees of freedom
p-value < .001 Overall model supported

Table 5 and Table 6 have presented the multiple regression model used to test whether Tableau-based
dashboarding capability, Python-based analytical processing, dashboard usability, data visualization
quality, and analytics automation have significantly pr edicted pharmaceutical brand performance
analytics effectiveness. The model has been statistically significant, F(5, 208) = 48.72, p < .001, indicating
that the five independent variables have jointly explained a meaningful proportion of variation in the
dependent variable. The R value has been .734, showing a strong combined relationship between the
predictors and pharmaceutical brand performance analytics effectiveness. The R² value has been .539,
which has meant that 53.9% of the variance in pharmaceutic al brand performance analytics
effectiveness has been explained by the five framework variables. The adjusted R² value has been .528,
indicating that the explanatory power has remained stable after adjusting for the number of predictors
in the model. Among the predictors, data visualization quality has emerged as the strongest predictor,
with β = .29, t = 4.42, and p < .001. This result has supported H4 and has shown that clear, readable,
appropriate, and decision -oriented visual presentation has been the m ost influential factor in
improving pharmaceutical brand performance analytics effectiveness. Dashboard usability has been
the second strongest predictor, with β = .24, t = 3.91, and p < .001, supporting H3 and showing that
users have valued ease of naviga tion, layout clarity, and filter accessibility. Tableau -based
dashboarding capability has also significantly predicted the dependent variable, with β = .21 and p =
.002, supporting H1. Python-based analytical processing has had a significant positive effect, with β =
.18 and p = .006, supporting H2. Analytics automation has also had a significant positive effect, with β
= .15 and p = .018, supporting H5. These findings have aligned with the theoretical framework because
the Information Systems Success Model  has suggested that system quality, information quality,

American Journal of Interdisciplinary Studies, December 2025, 351-393
378

usability, and process quality contribute to net benefits. In this study, Tableau has represented system
quality, Python has represented analytical information quality, dashboard usability has repres ented
user-centered quality, visualization quality has represented interpretive information quality, and
automation has represented reporting process quality. Therefore, the regression model has proved the
major objectives and has confirmed that the propos ed framework has been statistically valid for
pharmaceutical brand performance analytics.
Hypothesis testing summary

Table 7: Hypothesis testing summary

Hypothesis Statement Statistical evidence Decision Objective alignment
H1
Tableau-based dashboarding capability has
had a significant positive effect on
pharmaceutical brand performance analytics
effectiveness.
β = .21, p =
.002 Supported Objective 1 supported
H2
Python-based analytical processing has had a
significant positive effect on pharmaceutical
brand performance analytics effectiveness.
β = .18, p =
.006 Supported Objective 2 supported
H3
Dashboard usability has had a significant
positive effect on pharmaceutical brand
performance decision-support quality.
β = .24, p <
.001 Supported Objective 3 supported
H4
Data visualization quality has had a significant
positive effect on pharmaceutical brand
performance analytics effectiveness.
β = .29, p <
.001 Supported Objective 4 supported
H5
Analytics automation has had a significant
positive effect on reporting accuracy and
timeliness.
β = .15, p =
.018 Supported Objective 5 supported
H6
Integrated Tableau and Python analytics
capability has significantly predicted
pharmaceutical brand performance analytics
effectiveness.
R² = .539, F =
48.72, p < .001 Supported Objective 6 supported

Table 7 has summarized the hypothesis testing results and has confirmed that all six hypotheses of the
study have been supported. H1 has been supported because Tableau -based dashboarding capability
has had a significant positive effect on pharmaceutical brand performance analytics effectiveness, with
β = .21 and p = .002. This has proved that interactive dashboarding, KPI panels, territory -level
comparison, brand -wise visualization, and drill -down analysis have contrib uted to stronger brand
performance interpretation. This finding has also supported the first research objective, which has
focused on examining the role of Tableau-based dashboarding capability in improving pharmaceutical
brand analytics. H2 has been suppo rted because Python -based analytical processing has had a
significant positive effect on the dependent variable, with β = .18 and p = .006. This has proved the
second research objective by showing that data cleaning, preprocessing, statistical analysis, va riable
preparation, and repeatable analytical workflows have contributed to pharmaceutical brand
performance analytics effectiveness. H3 has been supported because dashboard usability has had a
significant positive effect, with β = .24 and p < .001. This has proved that navigation simplicity, layout
clarity, filter accessibility, and user -friendly dashboard design have been important for decision -
support quality. H4 has been supported with the strongest beta value, β = .29 and p < .001, showing
that data visualization quality has been the most powerful predictor in the model. This has proved the
objective related to evaluating the role of visualization clarity and chart appropriateness in insight
generation. H5 has been supported because analytics automation  has shown a significant positive

American Journal of Interdisciplinary Studies, December 2025, 351-393
379

effect, with β = .15 and p = .018, proving that automated reporting and reduced manual processing
have improved perceived reporting accuracy and timeliness. H6 has been supported through the
overall regression model, where  R² = .539 and p < .001 have shown that the integrated Tableau and
Python analytics capability has significantly predicted pharmaceutical brand performance analytics
effectiveness. In relation to the Information Systems Success Model, the supported hypothe ses have
shown that system quality, information quality, usability quality, visualization quality, and process
automation have jointly contributed to perceived net benefits. Therefore, Table 7 has clearly proved the
research objectives and has confirmed that the conceptual framework has been statistically supported.
Framework validation

Table 8: Framework validation results based on theoretical dimensions

Framework
dimension Study variable Mean Regression beta Validation result Theory linkage
System quality Tableau-based dashboarding capability 4.09 .21** Validated Interactive system quality
Analytical
information
quality
Python-based analytical
processing 3.92 .18** Validated Reliable information processing
Usability quality Dashboard usability 4.13 .24*** Validated Use and user satisfaction
Visual
information
quality
Data visualization quality 4.18 .29*** Strongly validated Information clarity and interpretability
Process quality Analytics automation 3.98 .15* Validated Timely and repeatable use
Net benefit
Pharmaceutical brand
performance analytics
effectiveness
4.05 Dependent variable Validated outcome Perceived net benefit
Note. *p < .05, **p < .01, ***p < .001.

Table 8 has validated the proposed dashboarding and visualization framework by connecting the
statistical findings with the Information Systems Success Model. The framework has been built on the
assumption that pharmaceutical brand performance analytics ef fectiveness has depended on system
quality, analytical information quality, usability quality, visual information quality, and process
quality. Tableau-based dashboarding capability has represented system quality because it has included
dashboard interactivity, KPI monitoring, filter -based exploration, drill -down analysis, and territory -
level brand comparison. Its mean score of 4.09 and regression beta of .21 have confirmed that this
dimension has been both positively perceived and statistically significant . Python -based analytical
processing has represented analytical information quality because it has included data cleaning,
preprocessing, descriptive statistics, correlation analysis, regression preparation, and workflow
validation. Its mean score of 3.92 and beta value of .18 have shown that the analytical backend has
significantly contributed to the effectiveness of pharmaceutical brand analytics. Dashboard usability
has represented usability quality and user satisfaction because it has measured how easily users could
navigate, understand, and apply the dashboard. Its mean score of 4.13 and beta value of .24 have
validated the importance of user -centered dashboard design. Data visualization quality has
represented visual information quality because it has measured chart readability, KPI clarity, visual
comparison, color consistency, interpretability, and decision relevance. It has received the highest mean
score of 4.18 and the highest beta value of .29, which has made it the strongest validated dimension of
the framework. Analytics automation has represented process quality because it has measured
automated reporting, reduced manual effort, faster analysis, and repeatable workflow. Its mean score

American Journal of Interdisciplinary Studies, December 2025, 351-393
380

of 3.98 and beta value of .15 have confirmed that automation has supported reporting accuracy and
timeliness. Pharmaceutical brand performance analytics effectiveness has represented the net benefit
dimension of the theory because it has reflected improved brand monitoring, faster insight generation,
reporting accuracy, and managerial decision support. Therefore, the framework has been validated
both theoretically and statistically. The results have shown that the Information Systems Success Model
has been properly adapted to the Tableau and Python -based pharmaceutical analytics context. This
validation has also proved the sixth objective of the study because the integrated framework has
successfully connected Tableau as the visualization layer, Python as the analytical processing layer,
and pharmaceutical brand performance analytics effectiveness as the decision-support outcome.
Dashboard prototype evaluation and KPI visualization effectiveness

Table 9: Dashboard prototype evaluation and KPI visualization effectiveness

KPI visualization item Mean Standard deviation Likert interpretation Result rank
Brand-wise KPI clarity has improved
performance understanding 4.24 0.58 High agreement 1
Regional drill-down analysis has helped identify
weak territories 4.19 0.63 High agreement 2
Sales trend visualization has improved brand
movement interpretation 4.16 0.61 High agreement 3
Market share visualization has supported
competitive brand comparison 4.12 0.66 High agreement 4
Promotional response dashboard has supported
marketing decision-making 4.05 0.69 High agreement 5
Prescription trend dashboard has improved
insight generation 4.03 0.67 High agreement 6
Dashboard filter and navigation options have
supported user control 4.01 0.72 High agreement 7
Overall dashboard prototype has supported
pharmaceutical brand analytics 4.17 0.60 High agreement Overall

Table 9 has presented the dashboard prototype evaluation and KPI visualization effectiveness results,
and this section has been especially important because it has directly matched the title of the study. The
results have shown that respondents have strongly agreed that the Tableau-style dashboard prototype
has supported pharmaceutical brand performance analytics. The overall dashboard prototype has
recorded a mean score of 4.17 with a standard deviation of 0.60, indicating strong agreement among
respondents. The highest-rated item has been brand -wise KPI clarity, with a mean score of 4.24. This
has shown that respondents have found the dashboard useful for understanding product -level
performance through clear indicators such as sales achievement, growth rat e, market share,
prescription movement, and brand ranking. Regional drill -down analysis has ranked second with a
mean score of 4.19, showing that respondents have considered territory-level exploration highly useful
for identifying weak regions, strong-performing markets, and regional performance gaps. Sales trend
visualization has ranked third with a mean score of 4.16, which has indicated that visual trend lines
have helped respondents interpret brand movement over time more clearly than static tabular reports.
Market share visualization has recorded a mean score of 4.12, supporting the idea that dashboards can
help compare pharmaceutical brands within competitive contexts. Promotional response dashboarding
has recorded a mean score of 4.05, while prescription trend dashboarding has recorded 4.03, showing
that respondents have found these visual elements useful for marketing and sales decision -making.
Dashboard filter and navigation options have recorded a mean score of 4.01, still showing strong
agreement that interactivity has improved user control. These results have supported the first, third,

American Journal of Interdisciplinary Studies, December 2025, 351-393
381

and fourth research objectives because the dashboard prototype has been evaluated positively in terms
of Tableau capability, usability, and visualization quality. The results have also supported H1, H3, and
H4 because the dashboard prototype has shown strong perceived value in relation to dashboarding
capability, usability, and visual clarity. In relation to the Information Systems Success Model, this
section has validated system quality and visual information quality in a practical way. The dashboard
has not only been statistically linked with analytics effectiveness; it has also been perceived as useful at
the KPI level. Therefore, Table 9 has made the findings mor e study-specific and has strengthened the
trustworthiness of the proposed Tableau-based visualization framework.
Python-driven analytical workflow validation

Table 10: Python-driven analytical workflow validation

Python analytical workflow item Mean Standard deviation Likert interpretation Result rank
Python-based data cleaning has improved data
accuracy 4.08 0.65 High agreement 1
Automated descriptive statistics have improved
reporting consistency 4.03 0.68 High agreement 2
Correlation matrix preparation has supported
relationship analysis 3.98 0.70 Agreement 3
Regression model preparation has improved
hypothesis testing 3.95 0.72 Agreement 4
Missing-value and outlier checking has
improved analytical reliability 3.93 0.73 Agreement 5
Python workflow has reduced manual reporting
errors 3.91 0.75 Agreement 6
Python outputs have been suitable for Tableau
dashboard preparation 3.89 0.76 Agreement 7
Overall Python-driven analytical workflow has
supported framework reliability 3.99 0.69 Agreement Overall

Table 10 has presented the validation of the Python -driven analytical workflow, and this section has
strengthened the analytical trustworthiness of the study because it has shown that the proposed
framework has not depended only on visual dashboarding. The  overall Python -driven analytical
workflow has recorded a mean score of 3.99 with a standard deviation of 0.69, indicating positive
agreement that Python has supported the reliability of the dashboarding and visualization framework.
Python-based data cleaning has received the highest mean score of 4.08, showing that respondents have
perceived data cleaning as the most important contribution of Python. This has been important in
pharmaceutical brand performance analytics because raw data may contain inconsis tent product
names, missing values, duplicate records, irregular region codes, and manually entered reporting
errors. Automated descriptive statistics have ranked second with a mean score of 4.03, showing that
Python has helped improve reporting consistenc y through repeatable calculation of means, standard
deviations, and summary statistics. Correlation matrix preparation has recorded a mean score of 3.98,
while regression model preparation has recorded 3.95. These values have indicated that Python has
supported the statistical testing of relationships among the study variables and has helped prove the
hypotheses of the study. Missing-value and outlier checking has recorded a mean score of 3.93, showing
that respondents have recognized the value of data validation before dashboard development. The item
related to reduced manual reporting errors has recorded a mean score of 3.91, while suitability of
Python outputs for Tableau dashboard preparation has recorded 3.89. These results have remained
positive and ha ve shown that Python has been useful for creating dashboard -ready datasets. This
section has supported the second objective of the study, which has focused on assessing the

American Journal of Interdisciplinary Studies, December 2025, 351-393
382

contribution of Python-based analytical processing to pharmaceutical brand performance analytics. It
has also supported H2 because Python -based analytical processing has been shown to have a
significant effect in the regression model and has been positively evaluated in the workflow validation
results. In relation to the Information Syst ems Success Model, Python has represented information
quality and analytical quality because it has improved the reliability, consistency, and readiness of data
before visualization. Therefore, Table 10 has confirmed that the framework has been balanced between
backend analytical processing and frontend Tableau dashboarding. This has made the overall findings
more credible because the study has shown that effective pharmaceutical brand performance analytics
requires both reliable data processing and clear visual decision support.
FINDINGS
The findings of this study have provided statistical support for the proposed dashboarding and
visualization framework for pharmaceutical brand performance analytics using Tableau and Python.
The study has used a five-point Likert scale, where 1 has indicated strongly disagree and 5 has indicated
strongly agree, to measure the perceptions of pharmaceutical professionals regarding Tableau -based
dashboarding capability, Python-based analytical processing, dashboard usability, data visualization
quality, analytics automation, and pharmaceutical brand performance analytics effectiveness. A total
of 250 questionnaires have been distributed among pharmaceutical brand managers, sales managers,
marketing executives, territory manager s, business intelligence analysts, data analysts, and decision -
making professionals, and 214 valid responses have been retained for final analysis, producing a valid
response rate of 85.6%.

Figure 9: Findings of The Study

The demographic profile has shown that 28.5% of respondents have been sales or territory managers,
24.8% have been brand or product managers, 18.2% have been marketing executives, 15.0% have been
business intelligence or data analysts, and 13.5% have been senior decision-makers or departmental
supervisors. In terms of professional experience, 34.1% of respondents have had 1 –3 years of
experience, 38.3% have had 4 –7 years of experience, and 27.6% have had more than 7 years of
experience, which has indicated that the sample has represented respondents with relevant exposure
to pharmaceutical performance reporting and analytics practices. The descriptive results have shown
strong agreement across the major constructs, with data visualization quality recording t he highest
mean score of 4.18 (SD = 0.61), followed by dashboard usability at 4.13 (SD = 0.64), Tableau -based
dashboarding capability at 4.09 (SD = 0.66), pharmaceutical brand performance analytics effectiveness
at 4.05 (SD = 0.63), analytics automation at 3.98 (SD = 0.69), and Python-based analytical processing at

American Journal of Interdisciplinary Studies, December 2025, 351-393
383

3.92 (SD = 0.71). These mean scores have indicated that respondents have generally agreed that
dashboard clarity, interactive visual reporting, statistical processing, automation, and usability a re
important for improving pharmaceutical brand performance analytics. The reliability analysis has also
supported the consistency of the measurement instrument, as Cronbach’s alpha values have ranged
from .81 to .89 across the constructs, exceeding the ac ceptable threshold of .70. Specifically, Tableau -
based dashboarding capability has recorded an alpha value of .86, Python-based analytical processing
has recorded .84, dashboard usability has recorded .88, data visualization quality has recorded .87,
analytics automation has recorded .81, and pharmaceutical brand performance analytics effectiveness
has recorded .89. The correlation results have further demonstrated positive and statistically significant
relationships among the study variables. Pharmaceutical brand performance analytics effectiveness has
shown strong positive correlations with data visualization quality (r = .68, p < .001), dashboard usability
(r = .65, p < .001), Tableau -based dashboarding capability (r = .62, p < .001), Python -based analytical
processing (r = .57, p < .001), and analytics automation (r = .55, p < .001). These results have suggested
that respondents who rated dashboard clarity, interactivity, usability, Python-supported analysis, and
automation more highly also tended to rate pharmaceutical brand performance analytics effectiveness
more highly. The regression analysis has provided stronger evidence for proving the hypotheses and
objectives of the study. The overall regression model has been statistically significant, F(5, 208) = 48.72,
p < .001, and the model has explained 53.9% of the variance in pharmaceutical brand performance
analytics effectiveness, with an adjusted R² value of .528. Among the predictors, data visualization
quality has emerged as the strongest predictor (β = .29, p < .001), followed by dashboard usability (β =
.24, p < .001), Tableau -based dashboarding capability (β = .21, p = .002), Python -based analytical
processing (β = .18, p = .006), and analytics automation (β = .15, p = .018). These results have supported
H1, H2, H3, H4, H5, and H6 by showing that all major dimensions of the proposed framework have
had significant positive contributions to pharmaceutical brand performance analytics effectiveness. The
results have also supported the first research objective by confirming that Tableau-based dashboarding
capability improves interactive brand tracking, KPI visibility, and territory -level comparison. The
second objective has been supported because Python -based analytical processing has shown a
significant contribution to analytical reliability, data preparation, and statistical validation. The third
and fourth objectives have been supported because dashboard usability and data visualization quality
have shown strong relationships with decision -support qualit y and insight generation. The fifth
objective has been supported because analytics automation has improved perceived reporting
accuracy, speed, and reduction of manual error. The sixth objective has been supported through the
validation of the integrated f ramework, where Tableau has served as the visualization and
dashboarding layer, Python has served as the analytical processing layer, and pharmaceutical brand
performance analytics effectiveness has represented the decision -support outcome. Overall, the
findings have indicated that the proposed framework is statistically reliable, practically relevant, and
suitable for supporting pharmaceutical brand managers and analytics professionals in monitoring
brand performance, interpreting market signals, comparing  territories, identifying underperforming
areas, and making evidence -based decisions through a combined Tableau and Python analytics
workflow.
DISCUSSION
The findings of this study have shown that the proposed dashboarding and visualization framework
using Tableau and Python has been statistically supported for pharmaceutical brand performance
analytics. The overall results have indicated strong agreement across the major constructs, with data
visualization quality recording the highest mean score of 4.18, followed by dashboard usability at 4.13,
Tableau-based dashboarding capability at 4.09, pharmaceutical brand performance analytics
effectiveness at 4.05, analytics automation at 3.98, and Python-based analytical processing at 3.92. These
results have sugge sted that pharmaceutical professionals have perceived visual clarity, dashboard
usability, and Tableau -supported KPI presentation as the most immediately visible contributors to
brand analytics effectiveness, while Python -based processing and automation ha ve also been viewed
positively as supporting elements behind the dashboard. The correlation findings have further
confirmed that pharmaceutical brand performance analytics effectiveness has had significant positive
associations with data visualization qual ity (r = .68), dashboard usability (r = .65), Tableau -based

American Journal of Interdisciplinary Studies, December 2025, 351-393
384

dashboarding capability (r = .62), Python -based analytical processing (r = .57), and analytics
automation (r = .55), all at p < .001. The regression model has also been significant, F(5, 208) = 48.72, p
< .001, with R² = .539 and adjusted R² = .528, meaning that the five framework variables have explained
53.9% of the variance in pharmaceutical brand performance analytics effectiveness. This finding has
strongly supported the argument that pharmaceutical brand analytics is not improved by one isolated
tool alone; rather, effectiveness has emerged from the combined role of visual dashboarding, analytical
processing, usability, visualization quality, and automation. This result has aligned with earlie r
business intelligence research, which has shown that analytics and BI systems create value when data,
technology, analytical capability, and decision environments are connected to managerial use (Chen et
al., 2012 ). The result has also been consistent with dashboard research, which has explained that
dashboards become valuable when they organize key indicators, support performance monitoring, and
reduce information overload for decision -makers (Yigitbasioglu & Velcu, 2012). In the present study,
data visualization quality has emerged as the strongest predictor (β = .29), which has  suggested that
the way pharmaceutical brand data are visually communicated may influence decision support more
strongly than backend processing alone. This finding has been consistent with visual analytics research,
which has emphasized that effective visualization depends on meaningful visual representation, user
task alignment, and interpretive clarity (Munzner, 2009 ). Therefore, the key finding has been that
Tableau and Python can form a reliable pharmaceutical brand performance analytics framework when
visualization quality and usability are treated as central decision -support dimensions rather than
secondary dashboard features.

Figure 10: Proposed Maturity Model for Pharmaceutical Brand Performance Analytics Using
Tableau and Python

Comparison with earlier studies and interpretation of dashboarding capability. The significant positive
effect of Tableau -based dashboarding capability on pharmaceutical brand performance analytics
effectiveness (β = .21, p = .002) has confirmed that interactive dashboarding has supported brand-level

American Journal of Interdisciplinary Studies, December 2025, 351-393
385

monitoring, KPI visibility, regional comparison, and performance interpretation. The dashboard
prototype evaluation has strengthened this interpretation because brand-wise KPI clarity has recorded
the highest i tem-level mean score of 4.24, regional drill -down analysis has recorded 4.19, and sales
trend visualization has recorded 4.16. These results have shown that respondents have valued
dashboards most when they have translated complex brand performance data into clear product-level
and territory -level views. This has directly supported the first objective of the study, which has
examined the role of Tableau -based dashboarding capability in improving pharmaceutical brand
performance analytics. The finding has al igned with prior research on marketing dashboards, where
dashboard-based systems have been found useful for connecting metrics with managerial monitoring,
decision-making, and performance evaluation (Pauwels et al., 2009). It has also supported the argument
that decision support systems become important when managers need to interpret complex
information under uncertain and information -rich decision conditions (Arnott & Pervan, 2008 ). In
pharmaceutical brand management, such complexity appears through sales trends, p rescription
movement, promotional response, product ranking, market share, and regional achievement. The
result has also extended earlier dashboard studies by placing dashboarding in a specific pharmaceutical
brand analytics context rather than a general performance management setting. Healthcare dashboard
research has shown that dashboards can support decision-making when they present indicators clearly
and help users identify areas requiring attention (Dowding et al., 2015). The present finding has been
comparable because pharmaceutical brand dashboards have also helped users identify weak territories,
declining products, and performance gaps. The difference is that the current study has focused on
commercial brand analytics rather than clinical quality indicators. This has made the study more
specific to pharmaceutical marketing, sales analytics, and brand decision support. The finding has also
matched the Information Systems Success Model because Tableau-based dashboarding capability has
represented system quality. A dashboard with useful filters, drill-down options, KPI cards, charts, and
brand comparison panels has functioned as a high-quality information system interface. Therefore, the
supported H1 has indicated that dashboarding capability has not only improved visual presentation
but has also strengthened the perceived net benefit of the system through better brand performance
analytics effectiveness.
Interpretation of Python-based analytical processing and automation vs. prior work. The findings have
shown that Python-based analytical processing has had a significant positive effect on pharmaceutical
brand performance analytics effectiveness (β = .18, p = .006), while analytics automation has also had a
significant positive effect on reporting accuracy and timeliness (β = .15, p = .018). These results have
supported H2 and H5 and have confirmed the second and fifth objectives of the study. The descriptive
results have shown that Python-based analytical processing has recorded a positive mean score of 3.92,
while analytics automation has recorded  3.98. The Python-driven analytical workflow validation has
also shown that Python -based data cleaning has received the highest item score of 4.08, followed by
automated descriptive statistics at 4.03, correlation matrix preparation at 3.98, regression mod el
preparation at 3.95, and missing -value and outlier checking at 3.93. These results have indicated that
respondents have viewed Python as a reliability-building tool rather than only a programming tool. In
the context of pharmaceutical brand analytics, t his has meant that dashboard trustworthiness has
depended on whether product names, regional codes, sales values, prescription indicators,
promotional variables, and derived metrics have been properly cleaned and prepared before
visualization. This interpr etation has aligned with earlier research on Python -based scientific
computing, where Python environments have supported interactive data analysis, computational
workflows, numerical processing, and statistical analysis (Pérez & Granger, 2007). It has also matched
research on Python -based statistical modeling, where statistical tools  have supported regression
modeling, estimation, diagnostics, and interpretable analysis (Seabold & Perktold, 2010). The present
study has extended these works by applying Python analytical processing to a pharmaceutical brand
dashboarding framework. The result has also aligned with big data analytics capability research, which
has shown that analytics value depends on technical capability, data capability, and managerial
capability working together (Gupta & George, 2016 ). In this study, Python has represented technical
and analytical capability, while Tableau has represented visual communication and managerial use.
Automation has further supported the framework because repeated brand performance reporting often

American Journal of Interdisciplinary Studies, December 2025, 351-393
386

requires consistent monthly or quarterly processing. This has aligned with research emphasizing that
business analytics creates value when it supports decision processes and converts analysis into actio n
(Seddon et al., 2017 ). From the Information  Systems Success Model perspective, Python -based
analytical processing has represented information quality and analytical quality, while automation has
represented process quality. Therefore, the findings have suggested that the backend layer of the
framework has been necessary for ensuring that visual dashboards are built on reliable, repeatable, and
statistically valid data.
Dashboard usability, visualization quality, and theoretical interpretation. The strongest results in this
study have appeared in the areas of visualization quality and dashboard usability. Data visualization
quality has recorded the highest descriptive mean of 4.18 and the strongest regression beta value of .29,
while dashboard usability has recorded the second-highest mean of 4.13 and the second-strongest beta
value of .24. These results have supported H3 and H4 and have confirmed that dashboard usability and
visual quality are critical to pharmaceutical brand performance analytics effectiveness. The strong
correlation between data vis ualization quality and pharmaceutical brand performance analytics
effectiveness (r = .68, p < .001) has indicated that clear chart selection, readable labels, KPI clarity, color
consistency, visual comparison, and interpretable layouts have been strongly associated with effective
brand analytics. Similarly, the correlation between dashboard usability and pharmaceutical brand
performance analytics effectiveness (r = .65, p < .001) has shown that ease of navigation, filter
accessibility, logical dashboard str ucture, and user control have been essential for decision support.
These findings have been consistent with earlier visualization research, which has argued that visual
representations should be evaluated in relation to user tasks, data types, and analytical goals (Munzner,
2009). The findings have also aligned with visualization task research, which has shown that users
interact with dashboards through different task levels, including why they need information, what
information they require, and how interaction supports analysis (Brehmer & Munzner, 2013 ). In the
present study, pharmaceutical users have not interact ed with dashboards for general curiosity; they
have needed to interpret sales trends, compare brands, identify weak territories, evaluate promotional
response, and monitor prescription movement. Therefore, usability and visualization quality have
become central to decision -support effectiveness. The findings have also supported prior dashboard
design research, which has shown that dashboards require a distinct design logic because they combine
multiple indicators, compact displays, and interactivity in one decision environment (Sarikaya et al.,
2019). In terms of theory, these results have strongly supported the Information Systems Success Model
because dashboard usability has reflected use quality and user satisf action, while data visualization
quality has reflected information quality and interpretive system value. The results have suggested that
the net benefit of a dashboarding system depends not only on the availability of data but also on the
user’s ability to understand and apply that data. Therefore, the theoretical interpretation has been that
pharmaceutical brand analytics effectiveness has been achieved when system quality and information
quality have been converted into usable, visually clear, and managerially meaningful decision support.
Practical implications. The findings have several practical implications for pharmaceutical companies,
brand managers, sales leaders, marketing teams, and business intelligence professionals. First,
pharmaceutical organizations should treat dashboard development as a strategic analytics function
rather than a routine reporting activity. The results have shown that data visualization quality,
dashboard usability, and Tableau -based dashboarding capability have had strong ef fects on
pharmaceutical brand performance analytics effectiveness. This means that pharmaceutical companies
should design dashboards around actual brand decision tasks, including product -wise performance
monitoring, regional comparison, prescription trend tracking, market share analysis, sales target
achievement, promotional response evaluation, and territory -level performance diagnosis. Second,
companies should strengthen the backend analytical process before dashboard construction. The
significant effect of Python-based analytical processing has shown that data cleaning, missing -value
checking, outlier screening, descriptive statistics, correlation analysis, and regression preparation have
improved the trustworthiness of the dashboard. Therefore, companies  should avoid building
dashboards directly from unvalidated spreadsheets or fragmented reports. Third, the findings have
suggested that analytics automation should be integrated into pharmaceutical reporting systems. Since
automation has had a positive eff ect on reporting accuracy and timeliness, organizations should use

American Journal of Interdisciplinary Studies, December 2025, 351-393
387

Python scripts or automated workflows to reduce manual reporting errors and produce consistent
dashboard-ready datasets. Fourth, pharmaceutical companies should provide dashboard literacy a nd
analytics training for brand managers and sales teams. The strong role of dashboard usability has
indicated that users must be able to navigate filters, interpret charts, compare KPIs, and translate
dashboard results into decisions. This practical impli cation has aligned with earlier research showing
that business intelligence systems create value when they improve information access and analytical
decision-making (Elbashir et al., 2008). It has also aligned with research on BI maturity, where data -
oriented culture and systematic use of information have been found important for analytical decision-
making (Popovič et al., 2012 ). Fifth, the study has suggested that pharma ceutical dashboards should
include both executive -level and operational -level views. Executive users may need summary KPIs,
while territory managers may need region -wise drill-down and sales trend views. This has matched
prior design study research, which has emphasized the importance of domain needs and user
requirements in visualization system development (Sedlmair et al., 2012 ). Therefore, the practical
implication has been that the Tableau and Python framework can help pharmaceutical companies move
from static reporting to interactive, statistically supported, and decision -oriented brand performance
analytics.
Theoretical implications and limitations revisited. The theoretical implication of this study has been
that the Information Systems Success Model has been successfully adapted to a pharmaceutical brand
performance analytics context involving Tableau and Python. The study has shown that system quality,
information quality, usability quality, visual quality, process quality, and net benefits c an be
operationalized through measurable variables. Tableau-based dashboarding capability has represented
system quality, Python-based analytical processing has represented information and analytical quality,
dashboard usability has represented use and use r satisfaction, data visualization quality has
represented interpretive information quality, analytics automation has represented process quality,
and pharmaceutical brand performance analytics effectiveness has represented net benefit. The
supported regression model, with R² = .539, has suggested that these adapted IS success dimensions
explain a meaningful share of perceived analytics effectiveness. This has extended earlier IS success
research, which has emphasized the role of system quality, information  quality, use, satisfaction, and
net benefits in evaluating information systems (Petter et al., 2008). It has also aligned with empirical IS
success studies that have shown the importance of system quality and information quality in predicting
user satisfaction and system value (Iivari, 2005). The study has also contributed to analytics capability
theory by showing that value has emerged from the integration of dashboarding capability, analytical
processing, visualization quality, usability, and automation. This has been consistent with analytics
capability research, where technology, data, and managerial capability are treated as connected
contributors to business value (Akter et al., 2016 ). However, the limitations of the study have also
needed careful interpretation. First, the study has used a cross -sectional design, so it has captured
respondent perceptions at one point in time rather than tracking dashboard performance over multiple
periods. Second, the study has been case -study-based, so the results  may reflect the specific
pharmaceutical analytics context used in the research. Third, the findings have been based on self -
reported Likert-scale responses, meaning that the results have measured perceived effectiveness rather
than direct sales or prescri ption performance outcomes. Fourth, the study has used purposive
sampling, which has been appropriate for selecting knowledgeable respondents but may limit broader
generalization. Fifth, Python and Tableau effectiveness has been evaluated through perceived
analytical workflow and dashboard prototype evaluation, not through a fully deployed enterprise-level
system. These limitations have not weakened the statistical support of the study, but they have clarified
the boundary within which the findings should be interpreted.
Future research and proposed improved model. Future research can improve this study by developing
and testing a more advanced model that combines perception -based survey evidence with real
pharmaceutical brand performance datasets. The most important future research direction should be
the development of a Longitudinal Tableau-Python Pharmaceutical Brand Analytics Maturity Model,
which can be abbreviated as the LTPBAM model. This proposed model can improve the present
framework by adding four  progressive layers: data readiness, analytical intelligence, dashboard
adoption, and brand performance impact. In the first layer, data readiness can measure data

American Journal of Interdisciplinary Studies, December 2025, 351-393
388

completeness, data integration, data accuracy, product code consistency, prescription data availability,
CRM data quality, and reporting frequency. In the second layer, analytical intelligence can measure
Python-supported descriptive analytics, correlation analysis, regression modeling, predictive
modeling, promotional response analysis, and bran d segmentation. In the third layer, dashboard
adoption can measure Tableau dashboard usability, user satisfaction, frequency of use, drill-down use,
KPI interpretation, and decision-maker confidence. In the fourth layer, brand performance impact can
measure actual changes in sales growth, market share movement, prescription volume, regional
achievement, promotional return, and decision speed. The future model can be expressed as: Data
Readiness → Analytical Intelligence → Dashboard Adoption → Brand Performance Impact. This model
would improve the current study because the present research has tested perceived pharmaceutical
brand performance analytics effectiveness, while the proposed future model would test both perceived
and actual performance outcomes. Future researchers can also use a longitudinal design by collecting
data across six or twelve months to examine whether dashboard use improves brand decision-making
over time. A multi -case study design can also compare pharmaceutical companies of different s izes,
therapeutic categories, or market positions. Future research can additionally include machine learning
models in Python to forecast sales trends, detect declining brands, predict promotional response, and
classify territories by performance risk. Thi s direction would extend the current regression -based
framework into a predictive analytics framework. Future studies can also test mediation and
moderation effects, such as whether dashboard usability mediates the relationship between Tableau
capability and analytics effectiveness, or whether user analytics competency moderates the relationship
between Python-based processing and decision-support quality. This future direction has aligned with
prior research showing that predictive analytics can strengthen  information systems research by
explaining and forecasting outcomes (Shmueli & Koppius, 2011 ). It has also aligne d with big data
analytics studies showing that analytics capability can support performance when combined with
organizational readiness and strategic alignment (Wamba et al., 2017 ). Therefore, the proposed
LTPBAM model can offer a str onger path for future researchers by connecting data quality, Python
intelligence, Tableau adoption, and measurable pharmaceutical brand performance impact.
CONCLUSION
This study has concluded that the development of a dashboarding and visualization framew ork for
pharmaceutical brand performance analytics using Tableau and Python has been statistically
supported, methodologically justified, and practically relevant for pharmaceutical decision -making.
The research has followed a quantitative, cross-sectional, case-study-based design and has used a five-
point Likert scale to examine the perceptions of pharmaceutical professionals regarding Tableau-based
dashboarding capability, Python-based analytical processing, dashboard usability, data visualization
quality, analytics automation, and pharmaceutical brand performance analytics effectiveness. The
findings have shown that the proposed framework has achieved strong agreement across all major
constructs, with data visualization quality recording the highest mean score of 4.18, followed by
dashboard usability at 4.13, Tableau -based dashboarding capability at 4.09, pharmaceutical brand
performance analytics effectiveness at 4.05, analytics automation at 3.98, and Python -based analytical
processing at 3.92. These res ults have confirmed that respondents have perceived clear visualization,
usable dashboard design, interactive Tableau reporting, reliable Python -supported analysis, and
automated workflow as important elements of effective pharmaceutical brand performance analytics.
The reliability analysis has further confirmed the internal consistency of the research instrument, as all
Cronbach’s alpha values have exceeded the acceptable threshold and ranged from .81 to .89, while the
overall instrument reliability has reached .91. The correlation analysis has shown that pharmaceutical
brand performance analytics effectiveness has had significant positive relationships with data
visualization quality, dashboard usability, Tableau -based dashboarding capability, Python -based
analytical processing, and analytics automation. The regression analysis has provided stronger
statistical confirmation, as the overall model has been significant, F(5, 208) = 48.72, p < .001, and has
explained 53.9% of the variance in pharmaceutical bran d performance analytics effectiveness. Data
visualization quality has emerged as the strongest predictor, followed by dashboard usability, Tableau-
based dashboarding capability, Python -based analytical processing, and analytics automation.
Therefore, all six hypotheses have been supported, and all research objectives have been achieved. The

American Journal of Interdisciplinary Studies, December 2025, 351-393
389

study has confirmed that Tableau can serve as an effective visualization and dashboarding layer for
KPI monitoring, regional comparison, sales trend interpretation, and brand-wise performance analysis,
while Python can serve as a reliable analytical processing layer for data cleaning, descriptive statistics,
correlation analysis, regression modeling, workflow validation, and dashboard -ready dataset
preparation. The dashboard prototype evaluation and Python -driven analytical workflow validation
have made the results more specific to the research title because they have shown both the visible
dashboard value and the backend analytical value of the proposed framework. The stu dy has also
confirmed the relevance of the Information Systems Success Model because system quality, information
quality, usability quality, visual quality, process quality, and net benefit have been reflected through
the selected variables and supported t hrough the statistical findings. Overall, this research has
concluded that a combined Tableau and Python-based dashboarding and visualization framework can
improve pharmaceutical brand performance analytics by making brand data more accurate, interactive,
understandable, timely, and useful for managerial decision-making.
RECOMMENDATION
Based on the findings of this study, it has been recommended that pharmaceutical organizations should
adopt an integrated Tableau and Python-based analytics workflow for improving brand performance
monitoring, reporting accuracy, and decision support. First, pharmaceutical companies should develop
centralized brand performance dashboards that include product-wise sales achievement, market share,
prescription movement, regional performance, promotional response, customer engagement, growth
rate, territory contribution, and brand ranking indicators. These dashboards should not be designed
only as decorative visual reports; they should be built around the real decision needs of br and
managers, sales managers, marketing executives, business intelligence analysts, and senior decision -
makers. Since data visualization quality has emerged as the strongest predictor of pharmaceutical
brand performance analytics effectiveness, organizatio ns should give special attention to chart
selection, KPI clarity, dashboard layout, color consistency, label readability, filtering logic, and visual
comparison. Second, pharmaceutical companies should improve dashboard usability by ensuring that
users can  easily navigate the dashboard, filter regions or brands, drill down from summary -level
information to detailed views, compare current and previous performance, and identify
underperforming products or territories. Since dashboard usability has shown a str ong effect on
analytics effectiveness, regular user feedback should be collected before finalizing dashboard structure.
Third, organizations should use Python as the analytical backend before dashboard development.
Python should be used for data cleaning, missing-value treatment, duplicate removal, product name
standardization, region code correction, descriptive statistics, correlation analysis, regression
modeling, and automated data preparation. This can reduce manual reporting errors and ensure that
Tableau dashboards are based on reliable and validated data. Fourth, pharmaceutical companies
should automate repetitive reporting activities through Python scripts or scheduled analytical
workflows so that monthly or quarterly brand performance dashboards ca n be updated with less
manual effort. Automation can improve reporting timeliness, consistency, and managerial confidence.
Fifth, companies should train brand managers and sales teams in dashboard interpretation, KPI
understanding, visual analytics, and ba sic data literacy. A dashboard can support decision -making
only when users understand how to interpret the displayed indicators and connect them with brand
strategy. Sixth, pharmaceutical firms should link dashboard outputs with regular review meetings,
sales planning, promotional planning, territory performance reviews, and brand strategy discussions.
This will help ensure that analytics outputs are actually used in managerial decision-making. Seventh,
business intelligence teams should create separate das hboard views for different users, such as
executive summary dashboards for senior managers, territory dashboards for sales managers,
promotional dashboards for marketing teams, and analytical validation dashboards for BI
professionals. Finally, researchers and organizations should continuously evaluate the framework by
measuring user satisfaction, reporting accuracy, dashboard adoption, and actual brand performance
improvement. Therefore, the main recommendation of this study is that pharmaceutical organizations
should treat dashboarding and visualization as an integrated decision -support system where Python
ensures analytical reliability and Tableau ensures interactive visual interpretation.
LIMITATIONS OF THE STUDY

American Journal of Interdisciplinary Studies, December 2025, 351-393
390

This study has several limitations that should be considered when interpreting the findings. First, the
study has used a cross -sectional research design, which means that data have been collected from
respondents at a single point in time. Because of this design, the study has measured respondent
perceptions of Tableau-based dashboarding capability, Python-based analytical processing, dashboard
usability, data visualization quality, analytics automation, and pharmaceutical brand performance
analytics effectiveness during one specific period. It ha s not measured how the framework performs
over several months or how dashboard use changes over time. Second, the study has been case-study-
based, so the findings have been connected with a specific pharmaceutical analytics context. Although
the results ha ve shown strong statistical support, the findings may not be fully generalizable to all
pharmaceutical companies, therapeutic categories, market environments, or countries without further
testing. Third, the study has used a purposive sampling strategy, which has been suitable for selecting
respondents with knowledge of pharmaceutical brand performance analytics, but it may have limited
the representativeness of the sample. Respondents who have had stronger familiarity with dashboards,
analytics tools, or business intelligence may have evaluated the framework more positively than those
with limited analytics exposure. Fourth, the study has relied on self-reported Likert-scale survey data.
This means that the findings have represented perceived effectiveness rather than direct organizational
performance outcomes. For example, respondents have reported their views about dashboard
usefulness, Python-based analytical reliability, automation value, and brand analytics effectiveness, but
the study has not directly measured actual sales growth, prescription volume increase, market share
improvement, or promotional return after dashboard implementation. Fifth, although the study has
included dashboard prototype evaluation and Python -driven analytical workflow validati on, the
framework has not been tested as a fully deployed enterprise-level system across multiple departments
over a long operational period. Sixth, the study has used descriptive statistics, correlation analysis, and
regression modeling, which have been a ppropriate for the research objectives, but more advanced
methods such as structural equation modeling, mediation analysis, moderation analysis, longitudinal
modeling, or machine learning -based performance prediction have not been applied. Seventh, the
study has focused mainly on Tableau and Python, so it has not compared the framework with other
business intelligence tools such as Power BI, Qlik, R, SAS, or cloud -based analytics platforms. Eighth,
the availability of real pharmaceutical brand performance data may have been restricted because sales
records, prescription data, promotional budgets, and market share reports are often confidential.
Therefore, the study has depended mainly on professional perception and framework evaluation rather
than full access to proprietary datasets.
REFERENCES
[1]. Abu Naser Md Golam, M., & Amir, R. (2023). Digital Twin Modeling of Fiber Optic Telecom Infrastructure for
Proactive SCADA Network Resilience in Power Transmission Utilities. International Journal of  Scientific
Interdisciplinary Research, 4(4), 413–448. https://doi.org/10.63125/04mgf566
[2]. Ahearne, M., Hughes, D. E., & Schillewaert, N. (2007). Why sales reps should welcome information technology:
Measuring the impact of CRM-based IT on sales effectiveness. International Journal of Research in Marketing, 24(4), 336-
349. https://doi.org/10.1016/j.ijresmar.2007.09.003
[3]. Akter, S., Wamba, S. F., Gunasekaran, A., Dubey, R., & Childe, S. J. (2016). How to improve firm performance using
big data analytics capability and business strategy alignment? International Journal of Production Economics, 182, 113-
131. https://doi.org/10.1016/j.ijpe.2016.08.018
[4]. Amir, R. (2024). Commissioning Failures in Integrated Life Safety Systems (FA + HVAC Shutdown + Elevators): A
Multi-Site Case Study Based on Field Testing and Authority Inspections. American Journal of Data Science and Analytics,
5(12), 280-313. https://doi.org/10.63125/nst5ee49
[5]. Amir, R. (2025). Reducing False and Improving Response Time in High-Occupancy Buildings: A Quantitative Study
of NFPA 72 -Complaint Cause -and-Effect Testing Outcomes. American Journal of Scholarly Research and Innovation ,
4(01), 856–893. https://doi.org/10.63125/s18ss614
[6]. Amir, R., & Chapal, B. (2022). Federated Learning Archit ectures for Distributed Engineering Project Knowledge
Management A Simulation -Based Analysis. Review of Applied Science and Technology , 1(04), 411 -446.
https://doi.org/10.63125/4k4pjr64
[7]. Arnott, D., & Pervan, G. (2008). Eight key issues for the decision support systems discipline. Decision Support Systems,
44(3), 657-672. https://doi.org/10.1016/j.dss.2007.09.003
[8]. Bates, D. W., Saria, S., Ohno -Machado, L., Shah, A., & Escobar, G. (2014). Big data in health care: Using analytics to
identify and manage high -risk and high -cost patients. Health Affairs , 33(7), 1123 -1131.
https://doi.org/10.1377/hlthaff.2014.0041

American Journal of Interdisciplinary Studies, December 2025, 351-393
391

[9]. Bellazzi, R., & Zupan, B. (2008). Predictive data mining in clinical medicine: Current issues and guidelines.
International Journal of Medical Informatics, 77(2), 81-97. https://doi.org/10.1016/j.ijmedinf.2008.07.005
[10]. Ben Said, Y., Bragazzi, N. L., & Pyatigorskaya, N. V. (2019). Influence of sales promotion techniques on consumers'
purchasing decisions at community pharmacies. Pharmacy, 7(4), 150. https://doi.org/10.3390/pharmacy7040150
[11]. Borkin, M. A., Vo, A. A., Bylinskii, Z., Isola, P., Sunkavalli, S., Oliva, A., & Pfister, H. (2013). What makes a
visualization memorable? IEEE Transactions on Visualization and Computer Graphics , 19(12), 2306 -2315.
https://doi.org/10.1109/tvcg.2013.234
[12]. Brehmer, M., & Munzner, T. (2013). A multi -level typology of abstract visualization tasks. IEEE Transactions on
Visualization and Computer Graphics, 19(12), 2376-2385. https://doi.org/10.1109/tvcg.2013.124
[13]. Chen, H., Chiang, R. H. L., & Storey, V. C. (2012). Business inte lligence and analytics: From big data to big impact.
MIS Quarterly, 36(4), 1165-1188. https://doi.org/10.2307/41703503
[14]. Côrte-Real, N., Oliveira, T., & Ruivo, P. (2017). Assessing business value of big data analytics in European firms.
Journal of Business Research, 70, 379-390. https://doi.org/10.1016/j.jbusres.2016.08.011
[15]. Dowding, D., Randell, R., Gardner, P., Fitzpatrick, G., Dykes, P., Favela, J., Hamer, S., Whitewood -Moores, Z.,
Hardiker, N., Borycki, E., & Currie, L. (2015). Dashboards for improving patient care: Review of the literature.
International Journal of Medical Informatics, 84(2), 87-100. https://doi.org/10.1016/j.ijmedinf.2014.10.001
[16]. Elbashir, M. Z., Collier, P. A., & Davern, M. J. (2008). Measuring the effects of business intelligence systems: Th e
relationship between business process and organizational performance. International Journal of Accounting Information
Systems, 9(3), 135-153. https://doi.org/10.1016/j.accinf.2008.03.001
[17]. Elshehaly, M., Randell, R., Brehmer, M., McVey, L., Alvarado, N., Gale, C. P., & Ruddle, R. A. (2020). QualDash:
Adaptable generation of visualisation dashboards for healthcare quality improvement. IEEE Transactions on
Visualization and Computer Graphics, 27(2), 689-699. https://doi.org/10.1109/tvcg.2020.3030424
[18]. Gable, G. G., Sedera, D., & Chan, T. (2008). Re -conceptualizing information system success: The IS -impact
measurement model. Journal of the Asso ciation for Information Systems , 9(7), 377 -408.
https://doi.org/10.17705/1jais.00164
[19]. Gandomi, A., & Haider, M. (2015). Beyond the hype: Big data concepts, methods, and analytics. International Journal
of Information Management, 35(2), 137-144. https://doi.org/10.1016/j.ijinfomgt.2014.10.007
[20]. Gorla, N., Somers, T. M., & Wong, B. (2010). Organizational impact of system quality, information quality, and service
quality. The Journal of Strategic Information Systems, 19(3), 207-228. https://doi.org/10.1016/j.jsis.2010.05.001
[21]. Gupta, M., & George, J. F. (2016). Toward the development of a b ig data analytics capability. Information &
Management, 53(8), 1049-1064. https://doi.org/10.1016/j.im.2016.07.004
[22]. Heer, J., & Shneiderman, B. (2012). Interactive dynamics for visual analysis. Queue, 10(2), 30 -55.
https://doi.org/10.1145/2133416.2146416
[23]. Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering , 9(3), 90 -95.
https://doi.org/10.1109/mcse.2007.55
[24]. Iivari, J. (2005). An empirical test of the DeLone-McLean model of information system success. ACM SIGMIS Database:
The DATABASE for Advances in Information Systems, 36(2), 8-27. https://doi.org/10.1145/1066149.1066152
[25]. Isik, O., Jones, M. C., & Sidorova, A. (2013). Business intelligence success: The roles of BI capabilities and decision
environments. Information & Management, 50(1), 13-23. https://doi.org/10.1016/j.im.2012.12.001
[26]. Kazi Rakib Hasan, S., & Uddin, H. M. M. (2022). Scalable AI For Project Portfolio Management: A Mixed -Methods
Study Combining Distributed Computing Benchmarks. Review of Applied Science and Technology , 1(04), 375 –410.
https://doi.org/10.63125/0kk4wf20
[27]. Kluyver, T., Ragan -Kelley, B., Pérez, F., Granger, B., Bussonnier, M., Frederic, J., Kelley, K., Hamrick, J., Grou t, J.,
Corlay, S., Ivanov, P., Avila, D., Abdalla, S., & Willing, C. (2016). Jupyter notebooks: A publishing format for
reproducible computational workflows. Positioning and power in academic publishing: Players, agents and agendas, 87-90.
https://doi.org/10.3233/978-1-61499-649-1-87
[28]. Kowalczyk, M., & Buxmann, P. (2015). Big data and information processing in organizational decision processes: A
multiple case study. Business & Information Systems Engineering, 57(5), 267-278. https://doi.org/10.1007/s12599-015-
0372-2
[29]. Kremer, S. T. M., Bijmolt, T. H. A., Leeflang, P. S. H., & Wieringa, J. E. (2008). Generalizations on the effectiveness of
pharmaceutical promotional expenditures. International Journal of Research in Marketing , 25(4), 234 -246.
https://doi.org/10.1016/j.ijresmar.2008.08.001
[30]. Kwon, O., Lee, N., & Shin, B. (2014). Data quality management, data usage experience and acquisition intention of
big data analytics. International Journal of Information Management , 34(3), 387 -394.
https://doi.org/10.1016/j.ijinfomgt.2014.02.002
[31]. Lam, H., Bertini, E., Isenberg, P., Plaisant, C., & Carpendale, S. (2012). Empirical studies in information visualization:
Seven scenarios. IEEE Transactions on Visualization and Computer Graphics , 18(9), 1520 -1536.
https://doi.org/10.1109/tvcg.2011.279
[32]. Mackinlay, J., Hanrahan, P., & Stolte, C. (2007). Show me: Automatic presentation for visual analysis. IEEE
Transactions on Visualization and Computer Graphics, 13(6), 1137-1144. https://doi.org/10.1109/tvcg.2007.70594
[33]. McKinney, W. (2010). Data structures for statistical computing in Python. Proceedings of the 9th Python in Science
Conference, 56-61. https://doi.org/10.25080/Majora-92bf1922-00a
[34]. Md Arif Uz, Z., Sharmin, S., & Md Abdur, R. (2025). Factors Influencing Behavioural Intention to Use he Innovative
Open And Distance Learning Systems With The Role Of Continuance Intention. American Journal of Scholarly Research
and Innovation, 4(01), 202-220. https://doi.org/10.63125/pbjxp014

American Journal of Interdisciplinary Studies, December 2025, 351-393
392

[35]. Md Tohidul, I. (2023). ERP -Integrated Financial Analytics Systems for Corporate Financ ial Reporting, Cash Flow
Analysis, and Strategic Investment Planning. American Journal of Advanced Technology and Engineering Solutions, 3(04),
87-128. https://doi.org/10.63125/qhk96h35
[36]. Md. Abdur, R., & If tekhar, A. (2021). Customer Retention Forecasting in Mobile Wallet Services Using Neural
Networks: A Comparative Quantitative Study. International Journal of Business and Economics Insights , 1(4), 70-102.
https://doi.org/10.63125/dyrpc387
[37]. Mohammad Badrul, A., & Md. Mominul, H. (2023). Machine Learning –Based Assessment of Environmental and
Public Health Risks in Sewerage Sludge Management Systems. American Journal of Advanced Technology and
Engineering Solutions, 3(02), 33-77. https://doi.org/10.63125/y3yfxa92
[38]. Mohammad Shoriful Hossan, S. (2024). Development of A Predictive Maintenance Model for Industrial Motor Drives
and VFD Systems Using PLC/DCS Operational Telemetry. American Journal of Scholarly Research and Innovation, 3(01),
198-242. https://doi.org/10.63125/pv1js496
[39]. Mohammad Shoriful Hossan, S. (2025). Development Of an ARC -Flash Hazard Mitigation  Framework for
Brownfield Industrial Power Distribution Retrofits in U.S. Manufacturing. American Journal of Advanced Technology
and Engineering Solutions, 1(02), 262-303. https://doi.org/10.63125/vhqjgm79
[40]. Mohammad Shoriful Hossan, S., & Adar, C. (2023). SIL-Compliant Safety Instrumented System Design for Oil & Gas
Hazardous-Area Operations Using IEC 61508 / IEC 61511 Frameworks. Journal of Sustainable Development and Policy,
2(02), 43-85. https://doi.org/10.63125/cb3d3w81
[41]. Mst Shurovi, A., & Samia Hossain, S. (2022). Difference -in-Differences (DiD) Analysis of Data Driven Accounting
Systems and its Impact on Financial Error Rates in SMEs. Journal of Sustainable Development and Policy, 1(04), 117-157.
https://doi.org/10.63125/n4nr0d75
[42]. Muhammad Mohiul, I., & Mohammad Badrul, A. (2022). Predictive Analytics for Optimizing Sewerage Sludge
Treatment Efficiency and Resource Recovery in Dhaka City. Journal of Sustainable Development and Policy, 1(04), 158-
200. https://doi.org/10.63125/t9zdp458
[43]. Mukut Kanti, B. (2025). Lifecycle Carbon Reduction and Net Zero Pathway Modeling Using LEED, EDGE, and SBTI
Frameworks in Developing Economy Industrial Buildings. American Journal of Interdisciplinary Studies, 6(3), 306-350.
https://doi.org/10.63125/tnneth75
[44]. Mukut Kanti, B., & R ony, S. (2022). Quantitative Risk Assessment and Safety Performance Benchmarking for
Structural Integrity Management in Retail Supply Chain Infrastructure. American Journal of Data Science and Analytics,
3(12), 42-88. https://doi.org/10.63125/n88vth90
[45]. Munzner, T. (2009). A nested model for visualization design and validation. IEEE Transactions on Visualization and
Computer Graphics, 15(6), 921-928. https://doi.org/10.1109/tvcg.2009.111
[46]. Narayanan, S., Manchanda, P., & Chintagunta, P. K. (2005). Temporal differences in the role of marketing
communication in new product categories. Journal of Marketing Research , 42(3), 278 -290.
https://doi.org/10.1509/jmkr.2005.42.3.278
[47]. Park, S., Bekemeier, B., Flaxman, A. D., & Schultz, M. (2021). Impact of data visualization on decision-making and its
implications for public health pract ice: A systematic literature review. Informatics for Health and Social Care .
https://doi.org/10.1080/17538157.2021.1982949
[48]. Pauwels, K., Ambler, T., Clark, B. H., LaPointe, P., Reibstein, D., Sk iera, B., Wierenga, B., & Wiesel, T. (2009).
Dashboards as a service: Why, what, how, and what research is needed? Journal of Service Research , 12(2), 175-189.
https://doi.org/10.1177/109467050934421 3
[49]. Pérez, F., & Granger, B. E. (2007). IPython: A system for interactive scientific computing. Computing in Science &
Engineering, 9(3), 21-29. https://doi.org/10.1109/mcse.2007.53
[50]. Petter, S., DeLone, W., & McLean, E. (2008). Measuring information systems success: Models, dimensions, measures,
and interrelationships. European Journal of Information Systems, 17(3), 236-263. https://doi.org/10.1057/ejis.2008.15
[51]. Popovič, A., Hackney, R., Coelho, P. S., & Jaklič, J. (2012). Towards business intelligence systems success: Effects of
maturity and culture on analytical decision making. Decision Support Systems , 54(1), 729 -739.
https://doi.org/10.1016/j.dss.2012.08.017
[52]. Raghupathi, W., & Raghupathi, V. (2014). Big data analytics in healthcare: Promise and potential. Health Information
Science and Systems, 2, 3. https://doi.org/10.1186/2047-2501-2-3
[53]. Risha, A., & Kazi Mohammad Khalid, A. (2023). A Meta -Analysis of AI-Driven Geospatial Analytics for Predictive
Maintenance of Critical Infrastructure in Developing Economies. International Journal of Scientific Interdisciplinary
Research, 4(4), 375–412. https://doi.org/10.63125/rayrex49
[54]. Rule, A., Birmingham, A., Zuniga, C., Altintas, I., Huang, S.-C., Knight, R., Moshiri, N., Nguyen, M. H., Rosenthal, S.
B., Pérez, F., & Rose, P. W. (2019). Ten simple rules for writing and sharing computational analyses in Jupyter
Notebooks. PLOS Computational Biology, 15(7), e1007007. https://doi.org/10.1371/journal.pcbi.1007007
[55]. Sadia, Z., Mohammad Ariful, I., Sumyta, H., & Hosne Ara, M. (2022). A Review of AI-Powered Data Visualization in
Enterprise Reporting: Dashboard Design And Interactive Analytics. American Journal of Advanced Technology and
Engineering Solutions, 2(01), 32-54. https://doi.org/10.63125/gabst658
[56]. Samia Hossain, S. (2024). Predictive Financial Volatility Analytics Using Machine Learning Pipelines in ERP -
Integrated Enterprises. American Jour nal of Interdisciplinary Studies , 5(04), 134 -181.
https://doi.org/10.63125/hz27wz06
[57]. Sarikaya, A., Correll, M., Bartram, L., Tory, M., & Fisher, D. (2019). What do we talk about when we talk about
dashboards? IEEE Transactions on Visualization and Computer Graphics , 25(1), 682 -692.
https://doi.org/10.1109/tvcg.2018.2864903

American Journal of Interdisciplinary Studies, December 2025, 351-393
393

[58]. Seabold, S., & Perktold, J. (2010). Statsmodels: Econometric and statistical m odeling with Python. Proceedings of the
9th Python in Science Conference, 92-96. https://doi.org/10.25080/Majora-92bf1922-011
[59]. Seddon, P. B., Constantinidis, D., Tamm, T., & Dod, H. (2017). How d oes business analytics contribute to business
value? Information Systems Journal, 27(3), 237-269. https://doi.org/10.1111/isj.12101
[60]. Sedlmair, M., Meyer, M., & Munzner, T. (2012). Design study methodology: Reflections from the trenches and the
stacks. IEEE Transactions on Visualization and Computer Graphics , 18(12), 2431 -2440.
https://doi.org/10.1109/tvcg.2012.213
[61]. Shahbaz, M., Gao, C., Zhai, L., Shahzad, F., Luqman, A., & Zahid, R. (2021). Impact of big data analytics on sales
performance in pharmaceutical organizations: The role of customer relationship management capabilities. PLOS
ONE, 16(4), e0250229. https://doi.org/10.1371/journal.pone.0250229
[62]. Shima Ali, S., Musomi, K., & Sonya, G. (2024). Integrated Infectious Disease Preparedness: Multilingual Health
Communication Strategies for Public Health Risk Mitigation, Disease Intervention and Prevention for Culturally
Diverse Population in United States. American Journal of Data Science and Analytics , 5(10), 01 -47.
https://doi.org/10.63125/ehk4mt02
[63]. Shima Ali, S., Sonya, G., & Mahbubul, I. (2025). Telemedicine And Remote Patient Monitoring for Preventing Risk
and Chronic Disease Management in Underserved Communities. American Journal of Health and Medical Sciences ,
6(04), 01–42. https://doi.org/10.63125/y0e9dc38
[64]. Shmueli, G., & Koppius, O. R. (2011). Predictive analytics in information systems research. MIS Quarterly, 35(3), 553-
572. https://doi.org/10.25300/misq/2011/35.3.11
[65]. Tory, M., & Möller, T. (2005). Evaluating visualizations: Do expert reviews work? IEEE Computer Graphics and
Applications, 25(5), 8-11. https://doi.org/10.1109/mcg.2005.102
[66]. Trkman, P., McCormack, K., de Oliveira, M. P. V., & Ladeira, M. B. (2010). The impact of business analytics on supply
chain performance. Decision Support Systems, 49(3), 318-327. https://doi.org/10.1016/j.dss.2010.03.007
[67]. Urbach, N., Smolnik, S., & Riempp, G. (2010). An empirical investigation of employee portal success. The Journal of
Strategic Information Systems, 19(3), 184-206. https://doi.org/10.1016/j.jsis.2010.06.002
[68]. van der Walt, S., Colbert, S. C., & Varoquaux, G. (2011). The NumPy array: A structure for efficient numerical
computation. Computing in Science & Engineering, 13(2), 22-30. https://doi.org/10.1109/mcse.2011.37
[69]. VanderPlas, J., Granger, B. E., Heer, J., Moritz, D., Wongsuphasawat, K., Satyanarayan, A., Lees, E., Timofeev, I.,
Welsh, B., & Sievert, S. (2018). Altair: Interactive statistical visualizations for Python. Journal of Open Source Software,
3(32), 1057. https://doi.org/10.21105/joss.01057
[70]. Venkataraman, S., & Stremersch, S. (2007). The debate on influencing doctors' decisions: Are drug characteristics the
missing link? Management Science, 53(11), 1688-1701. https://doi.org/10.1287/mnsc.1070.0718
[71]. Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournape au, D., Burovski, E., Peterson, P.,
Weckesser, W., Bright, J., van der Walt, S. J., Brett, M., Wilson, J., Millman, K. J., Mayorov, N., Nelson, A. R. J., Jones,
E., Kern, R., Larson, E., . . . van Mulbregt, P. (2020). SciPy 1.0: Fundamental algorithms for scientific computing in
Python. Nature Methods, 17(3), 261-272. https://doi.org/10.1038/s41592-019-0686-2
[72]. Wamba, S. F., Gunasekaran, A., Akter, S., Ren, S. J. -F., Dubey, R., & Childe, S. J. (2017). Big data analytics and firm
performance: Effects of dynamic capabilities. Journal of Business Research , 70, 356 -365.
https://doi.org/10.1016/j.jbusres.2016.08.009
[73]. Wang, Y.-S., & Liao, Y.-W. (2008). Assessing eGovernment systems success: A validation of the DeLone and McLean
model of information systems success. Government Information Quarterly , 25(4), 717 -733.
https://doi.org/10.1016/j.giq.2007.06.002
[74]. Wang, Y., Kung, L., & Byrd, T. A. (2018). Big data analytics: Understanding its capabilities and potential benefits for
healthcare organizations. Technological Forecasting and Social Change , 126, 3 -13.
https://doi.org/10.1016/j.techfore.2015.12.019
[75]. Waskom, M. L. (2021). Seaborn: Statistical data visualization. Journal of Open Source Software , 6(60), 3021.
https://doi.org/10.21105/joss.03021
[76]. Wieder, B., & Ossimitz, M. -L. (2015). The impact of business intelligence on the quality of decision making: A
mediation model. Procedia Computer Science, 64, 1163-1171. https://doi.org/10.1016/j.procs.2015.08.599
[77]. Wixom, B. H., & Todd, P. A. (2005). A theoretical integration of user satisfaction and technology acceptance.
Information Systems Research, 16(1), 85-102. https://doi.org/10.1287/isre.1050.0042
[78]. Yigitbasioglu, O. M., & Velcu, O. (2012). A review of dashboards in performance management: Implications for
design and research. International Journal of Accounting Information Systems , 13(1), 41 -59.
https://doi.org/10.1016/j.accinf.2011.08.002
[79]. Zaman, S. (2024). A Systematic Review of ERP And CRM Integration For Sustainable Business And Data
Management in Logistics And Supply Chain Industry. Frontiers in Applied Engineering and Technology, 1(01), 204-221.
https://doi.org/10.70937/faet.v1i01.36
