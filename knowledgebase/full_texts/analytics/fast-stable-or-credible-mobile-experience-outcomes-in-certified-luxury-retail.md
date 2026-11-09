---
title: Fast, stable, or credible? Mobile experience outcomes in certified luxury retail
url: https://doi.org/10.1057/s41270-026-00473-3
category: analytics
subcategory: theory
date: 2026-03
venue: Journal of Marketing Analytics
authors:
- Eliza Ciobanu
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1057/s41270-026-00473-3.pdf
pages: 17
chars: 86381
fetched_at: '2026-11-08T17:51:48+00:00'
kb_version: 1
---

# Fast, stable, or credible? Mobile experience outcomes in certified luxury retail

ORIGINAL ARTICLE
Journal of Marketing Analytics
https://doi.org/10.1057/s41270-026-00473-3
contributing to elevated expectations of brand execution
across all consumer touchpoints.
While prior research has extensively examined sustain -
ability in luxury product sourcing and corporate governance
(Kapferer and Michaut-Denizeau 2017; Hepner et al. 2020),
far less attention has been paid to how sustainability com -
mitments are reflected in digital execution, particularly in
mobile environments. This omission is notable given the
increasing dominance of mobile channels in luxury retail
and the heightened sensitivity of luxury consumers to fric -
tion, inconsistency, and perceived imperfections in brand
encounters (Achugbu 2016; Al-Zuabi et al. 2019; Siman -
juntak 2023). Thus, the quality of mobile experiences has
emerged as a decisive factor in shaping customer percep -
tions and behaviors (Boustani and Zielinski 2023; Massi et
al. 2025).
The signaling perspective shows that in luxury markets,
the expectations extend beyond ethics to execution qual -
ity, making mobile UX performance a critical test of sig -
nal credibility. Moreover, in mobile-first contexts, luxury
brands operate under heightened performance expectations
Introduction
Sustainability has become a central dimension of luxury
brand equity, shaping how high-end brands differentiate
themselves and justify premium positioning (Rolling and
Sadachar 2018; Priyadarshini and Prasad 2023). High-net-
worth consumers increasingly expect luxury brands to dem-
onstrate verifiable environmental and social responsibility,
and third-party certifications such as the Butterfly Mark
serve as prominent signals of such commitments (Athwal
et al. 2019; Positive Luxury 2025). These certifications
communicate ethical standards and organizational rigor,
  Eliza Ciobanu
eliza.nichifor@unitbv.ro
1 Marketing, Tourism-Service and International Relations
Department, Faculty of Economic Sciences and Business
Administration, Transilvania University of Brasov, Eroilor
Boulevard, No. 29, 500036 Brasov, Romania
Abstract
Mobile interactions increasingly shape how consumers judge luxury brands, yet it remains unclear whether sustainable-
certified brands deliver mobile experiences consistent with the elevated execution expectations implied by ethical signal -
ing. Drawing on a signaling theory and expectation-based perspectives, this paper conceptualizes mobile UX performance
as an execution-level signal through which certification credibility is reinforced or undermined. Using real-user PageSpeed
Insights field data for 133 Butterfly Mark certified luxury brands, the analysis benchmarks Core Web Vitals and models
Google’s “Fast” mobile classification as a function of loading speed and visual stability. The findings reveal an asym -
metric structure of digital performance signals: visual stability operates primarily as a baseline hygiene condition, with
most brands meeting recommended thresholds and no robust sector-level differences, whereas loading speed, measured by
Largest Contentful Paint, emerges as the dominant predictor of platform-defined mobile experience quality. Even modest
reductions in loading time substantially increase the probability of achieving a “Fast” classification, while additional gains
in stability yield diminishing returns once baseline standards are satisfied. The study advances marketing analytics research
by demonstrating how platform-generated technical metrics can be modeled by showing that sustainability certification
functions as an expectation amplifier.
Keywords Customer experience analytics · Luxury e-commerce · Sustainability certification · Mobile performance
Received: 26 September 2025 / Accepted: 9 March 2026
© The Author(s) 2026
Fast, stable, or credible? Mobile experience outcomes in certified
luxury retail
Eliza Ciobanu1

E. Ciobanu
(Dryl 2023). Mobile interfaces are not merely functional
access points but experiential environments through which
perceptions of quality, fluency, refinement, or seamless jour-
neys are formed rapidly during page loading and interaction
(Klaus 2021). Even brief delays or unstable rendering can
disrupt the sense of effortlessness that defines luxury experi-
ences, making mobile technical performance a consequen -
tial component of brand execution (Holdener et al. 2020;
Ramtohul and Khedo 2023; Bansal 2024).
In luxury contexts, sustainability certifications function
as ex ante indicators of organizational quality, elevating
expectations of execution consistency across digital touch -
points (Song and Kim 2022; Wu and Tang 2022). Mobile
UX performance also has well-documented business impli-
cations. Previous research and industry evidence consis -
tently link mobile loading speed and interface stability to
outcomes such as bounce rates, session depth or duration,
and conversion likelihood (Qualid et al. 2024). In luxury
retail, where customer acquisition costs are high and brand
interactions are expected to be seamless, even small per -
formance frictions can have disproportionate commercial
consequences (Chevalier et al., 2020). Moreover, despite
growing research on luxury sustainability and digital cus -
tomer experience, three gaps remain. First, sustainability
research focuses primarily on messaging and governance,
while largely overlooking execution-level digital perfor -
mance as a credibility test. Secondly, UX research typically
treats technical performance dimensions symmetrically,
without examining whether different dimensions carry
asymmetric informational weight under high-expectation
brand contexts. Thirdly, marketing analytics research rarely
conceptualizes platform-defined technical classifications as
probabilistic experience signals embedded within evalua -
tion ecosystems. This study addresses these gaps by mod -
eling mobile technical performance as an execution-level
signal within sustainability-certified luxury brands.
In this context, the researcher examines mobile UX per -
formance among Butterfly Mark-certified luxury brands
using real-user field data from Google PageSpeed Insights.
Specifically, it uses widely adopted mobile performance
indicators to evaluate how execution quality aligns with
certification-based expectations (Web Dev 2025). The
study pursues three objectives, namely, (O1) to benchmark
mobile performance across luxury sectors, (O2) to assess
which technical metrics are most predictive of a fast mobile
experience, and (O3) to translate performance metrics into
interpretable managerial thresholds.
By reframing mobile performance metrics as execution-
level signals within sustainability-certified luxury con -
texts, this research contributes to marketing analytics by
providing a reproducible audit framework for evaluating
digital execution quality. It also offers actionable insights
for luxury managers seeking to align sustainability signal -
ing with mobile experience delivery in high-expectation
environments.
Empirically, the analysis shows a clear asymmetry
between mobile UX dimensions. Loading speed, captured
by Largest Contentful Paint (hereinafter LCP), emerges as
the dominant driver of Google’s “Fast” mobile classifica -
tion, whereas visual stability, measured by Cumulative Lay-
out Shift (CLS), primarily functions as a baseline hygiene
factor once minimum thresholds are met. This distinction
clarifies how execution-level performance signals operate
in sustainability-certified luxury contexts and motivates the
study’s focus on translating technical metrics into action -
able analytics insights.
From a marketing analytics perspective, this study con -
tributes by reframing mobile UX performance metrics as
execution-level signals rather than as purely technical indi -
cators. While analytics research often treats performance
metrics as background inputs or operational constraints, the
present findings show that platform-defined outcomes such
as Google’s “Fast” classification can be modeled probabi -
listically and interpreted as meaningful experience signals
within digital brand evaluation systems. This extends mar -
keting analytics research by demonstrating how real-user
technical metrics can be integrated into customer experi -
ence analytics as interpretable, decision-relevant signals
and not as opaque engineering outputs.
Literature review
LCX and digital touchpoints
Luxury customer experience (LCX) has emerged as a dis -
tinct domain within customer experience research, reflect -
ing heightened expectations, symbolic consumption, and
non-utilitarian value creation. LCX integrates functional
quality, emotional resonance, symbolic meaning, and per -
sonalization into a seamless brand journey (Mossberg 2008;
Saunila et al. 2019; Kusal et al. 2022). Unlike standard
customer experiences, luxury emphasizes aesthetics, story -
telling, exclusivity, and emotional immersion as core value
drivers.
Digital touchpoints have become central to delivering
LCX as luxury brands increasingly adopt omnichannel
strategies (Baxendale et al. 2015; Ieva and Ziliani 2018;
Fu and Ren 2023). Moreover, they form the scaffolding of
the modern LCX, their impact is increasingly determined
by the medium through which consumers access them (Ieva
and Ziliani 2018; Vannucci and Pantano 2019; Fu and Ren
2023). In luxury contexts, digital performance is not a neu -
tral technical background but an experiential attribute of

Fast, stable, or credible? Mobile experience outcomes in certified luxury retail
the customer journey. Because luxury value is grounded in
effortlessness, aesthetic coherence, and emotional immer -
sion, disruptions such as slow loading or unstable layouts
directly interfere with the experiential quality of the brand
encounter (Mossberg 2008; Klaus 2021). Accordingly,
mobile performance characteristics such as speed and
visual stability should be understood as constitutive ele -
ments of luxury customer experience, not technical con -
ditions. Thus, digital interfaces function as transactional
platforms but also, as experiential environments, in which
brand meaning and identity are continuously constructed.
In this context, visually unstable or slow-loading interfaces
can disrupt experiential continuity and generate brand dis -
sonance (Bansal 2024). Thus, from a relational perspective,
such breakdowns can be interpreted as violations of implicit
psychological expectations between brand and consumer,
leading to perceived brand incongruity (Berry 2000; Chen
et al. 2010).
Moreover, from a human–computer interaction (HCI)
perspective, digital luxury encounters are cognitive and
affective experiences shaped by interface fluency, percep -
tual continuity, and trustworthiness. As such, technical
execution becomes a necessary condition for sustaining the
symbolic and emotional of LCX. However, despite this rich
conceptualization of luxury customer experience, research
largely treats digital execution quality as a background con-
dition, not only as an empirically observable component of
LCX, leaving open how technical performance contributes
to experience formation in mobile environments.
Mobile-first strategy in luxury contexts
Building on the centrality of digital touchpoints in luxury
customer experience, mobile-first strategies have emerged
as a defining feature of contemporary luxury engagement.
The growing dominance of mobile devices has fundamen-
tally reshaped luxury brand engagement (Chung et al. 2018;
Jain et al. 2022). Mobile-first strategies require designing
interaction, content, and performance with mobile users as
the primary reference point, which represents more than
adapting desktop experiences ex post (AbouElgheit 2024).
In luxury contexts, mobile experiences are especially
consequential because consumers form rapid judgments
about brand quality and credibility during early stages of
mobile interaction (Hepner et al. 2020). Technical imperfec-
tions such as loading delays or unstable layouts are therefore
interpreted not merely as usability flaws but as violations
of the luxury brand promise. From an HCI standpoint,
mobile-first luxury design reflects the need to optimize
perceptual fluency, minimize cognitive load, and maintain
emotional continuity across digital interactions (Al-Zuabi
et al. 2019; Akkaya et al. 2024). Given the importance of
mobile channels in luxury engagement, the effectiveness of
a mobile-first strategy ultimately depends on the technical
performance of the interface, which shapes how seamlessly
and credibly the experience is delivered. Although mobile-
first strategies are widely advocated in luxury research,
empirical evidence linking such strategies to specific per -
formance indicators remains limited, particularly in high-
expectation luxury settings.
For sustainability-certified luxury brands, mobile execu-
tion may carry additional symbolic weight, as certification
can amplify expectations across touchpoints. In this context,
mobile performance becomes more than a usability concern;
it operates as an execution-level signal through which the
credibility of sustainability claims is indirectly assessed. In
this sense, inconsistencies in mobile execution may weaken
the coherence between ethical positioning and operational
delivery. While mobile-first strategies are widely advocated
in luxury research, empirical work rarely specifies which
aspects of mobile execution drive experience outcomes,
particularly under the heightened expectations characteris -
tic of luxury contexts.
Technical performance and mobile luxury UX
From an expectations-based and signaling perspective, not
all technical performance dimensions carry equal infor -
mational weight in shaping early experience judgments.
Research in HCI shows that loading speed directly influ -
ences perceptual fluency and cognitive ease during the
earliest moments of interaction, when users form rapid
assessments of competence and quality (Duric et al. 2002;
Erdman et al. 2025; Lang et al. 2025; Vázquez-Martínez,
et al. 2025). By contrast, visual stability primarily prevents
negative disruption. than generating positive differentiation
once minimum standards are met. This asymmetry sug -
gests that speed functions as a primary execution-level sig -
nal, while stability operates closer to a baseline condition
whose absence is penalized but whose presence is taken for
granted, particularly in high-expectation luxury contexts.
Responding to this dependency, research has increasingly
focused on technical performance indicators that shape how
mobile experiences are rendered and perceived. Technical
performance has long been recognized as a core determi -
nant of digital UX (Shao and Chang 2020; Balcombe and
Leo 2022; Seale et al., 2022), yet its emotional and sym -
bolic implications in luxury contexts remain underexplored.
Metrics such as LCP and CLS introduced within Google’s
Core Web Vitals framework, capture key aspects of mobile
speed and visual stability that shape users’ early interaction
experiences (Król and Sroka 2023; Wibagso 2023; Romero
and Torres 2024).

E. Ciobanu
whose credibility depends on consistent execution across
digital touchpoints.
In parallel with the digital transformation of luxury, sus-
tainability has become a defining axis of differentiation and
consumer engagement (Piligrimienė et al. 2020; Judijanto
et al. 2024). Certifications such as the Butterfly Mark have
been developed to communicate verified environmental and
social commitments across luxury sectors. These third-party
endorsements enhance transparency in markets increasingly
attentive to greenwashing and ESG rhetoric (Kapferer and
Michaut-Denizeau 2017). The Butterfly Mark, in particular,
functions as a communication mechanism that signals ethi -
cal excellence positioning and organizational rigor in com -
plex, information-rich marketplace.
Research suggests that the effectiveness of such signals
depends on the coherence with broader brand execution
and experiential consistency (Chen et al. 2010; Andriyani
and Yudhistira 2023). In digital contexts, especially when
interfaces fail to meet baseline expectations of technical
performance and visual fluidity, misalignment may emerge
between ethical signaling and experiential delivery. In
luxury settings, where perceived authenticity and brand
harmony are especially salient, such inconsistencies can
weaken the alignment between sustainability messaging and
the lived brand experience.
Importantly, signaling theory implies not that certifica -
tion guarantees superior performance, but that it ampli -
fies expectations regarding execution quality. In luxury
contexts, third-party sustainability certifications elevate
assumptions about organizational rigor and operational
competence, increasing the likelihood that execution-
level deviations will be noticed and negatively evaluated.
Mobile UX performance thus becomes a salient arena in
which the credibility of sustainability signaling is tested, as
inconsistencies between ethical positioning and observable
execution can weaken perceived authenticity. Sustainability
certifications have become key quality signals in markets
where consumers and stakeholders cannot directly observe
underlying organizational performance. Signaling theory
suggests that such cues reduce information asymmetry and
allow observers to infer competence and commitment from
external markers. Certifications such as Butterfly Mark,
therefore, communicate ethical achievement and also,
shape expectations of executional excellence, as consum -
ers increasingly interpret sustainability signals through the
lens of brand competence and overall quality perception.
Research shows that sustainability signaling influences how
consumers define brand value, trust, and authenticity and
that third-party certifications enhance perceived credibility
when aligned with coherent performance signals (Theocha-
ris and Tsekouropoulos 2025).
Although other studies document the general impor -
tance of speed and visual stability for user experience, most
treat these dimensions symmetrically or as interchangeable
indicators of “good UX,” offering limited insight into their
potentially asymmetric roles in shaping early judgments,
particularly in luxury entities.
Unexpected layout shifts and slow rendering can disrupt
attentional flow, increase cognitive load, and elicit negative
affective responses (Wang and Rodriguez 2024). By con -
trast, once minimum standards of visual stability are met,
the absence of disruption becomes expected rather than
diagnostic, implying diminishing value for differentiation-
consistent with a “hygiene factor” role. These effects are
amplified in luxury settings, where users are particularly
sensitive to aesthetic coherence and experiential disruptions
(Berry 2000). Empirical evidence further suggests that per -
ceptions of experiential quality and emotional engagement
are shaped early in the mobile page-loading process (Bakar
et al., 2024). Again, from an expectations-based signaling
perspective, loading speed functions as a primary execution
cue through which users rapidly assess whether operational
performance aligns with the quality expectations implied by
brand positioning.
Certifications function as trust signals intended to con -
vey ethical leadership, yet their effectiveness depends on
consistent and high-quality execution across digital touch -
points. For sustainability-oriented luxury brands, technical
execution acquires additional significance, as disruptions
in mobile performance can directly undermine perceptions
of fluency, refinement, and experiential coherence. Sev -
eral studies document the general importance of speed and
visual stability for UX, yet few examine their implications
in luxury contexts or assess these effects using real-user
field data.
While these technical indicators are essential for deliv -
ering seamless mobile experiences, their role becomes
especially consequential when brands engage in sustainabil-
ity-based signaling. Importantly, signaling theory implies
not that certification guarantees superior performance, but
that it amplifies expectations regarding execution quality. In
luxury contexts, third-party sustainability certifications ele-
vate assumptions about organizational rigor and operational
competence, increasing the likelihood that execution-level
deviations will be noticed and negatively evaluated.
Sustainability certification as a digital execution
signal
While the previous section focuses on the experiential con -
sequences of technical performance, this section conceptu -
alizes sustainability certification as a signaling mechanism

Fast, stable, or credible? Mobile experience outcomes in certified luxury retail
across luxury sectors to describe the distribution of load -
ing speed and visual stability among certified brands. Sec -
ondly, it estimates the probability that a website is classified
by Google as delivering a “Fast” mobile experience as a
function of Core Web Vitals. Thirdly, the analysis translates
model estimates into interpretable performance thresholds
that indicate where incremental technical improvements are
associated with meaningful changes in mobile experience
classification.
To enhance robustness, First Contentful Paint (FCP)
is included in an alternative specification as an additional
speed-related metric. All analyses rely on real-user field
data obtained via the Google PageSpeed Insights API and
are designed to provide an execution-focused audit of
mobile UX performance within sustainability-certified lux -
ury brands.
Data collection
The sample comprises 133 luxury brand websites certified
with the Butterfly Mark by Positive Luxury. Brand URLs
were sourced from the public “Real Changers” listing to
ensure transparency and replicability. Sectors include Fash-
ion & Accessories, Interiors & Living, Beauty & Fragrance,
Jewelry & Watches, Premium Drinks, and Travel & Leisure.
Field data were unavailable for some certified brands due to
insufficient real-user Chrome data at the time of collection,
consistent with PageSpeed Insights reporting thresholds. At
the time of data collection, several certified brand websites
did not return field-level Core Web Vitals due to insufficient
traffic volume, restricted data availability, or incomplete
reporting by the API. As a result, only sites with valid CLS
and LCP field data were retained for analysis. Thus, out of
the 133 Butterfly Mark certified brand websites initially
identified, only sites with valid PageSpeed Insights field data
for the relevant Core Web Vitals were retained, resulting in
a final analytic sample of 64 websites after listwise deletion
for missing metrics. Given the relatively small final sample
size, the author acknowledges that the statistical power of
the regression model may be limited, particularly with mul-
tiple sector dummy variables. While no formal power analy-
sis was conducted, robustness checks were performed with
FCP as an additional speed metric, and sector-level com -
parisons were included to provide additional validation. All
descriptive and inferential analyses reported in the Results
section are based on this final sample unless otherwise spec-
ified. Therefore, mobile performance was collected via the
Google PSI API (v5) using the strategy = mobile parameter.
Custom Python 3.11.9 scripts (requests or JSON) handled
API calls with a 1-s rate limit to conform to usage policies.
All raw JSON responses were saved one-per-site to preserve
traceability and enable replication. All PageSpeed Insights
From a HCI perspective, sustainability signaling can
therefore be viewed as interacting with the integrity of the
UX. In mobile environments, where interactions are frequent
and time-constrained, technical UX performance constitutes
a salient execution-level signal through which sustainability
claims are enacted. For such certifications to function effec-
tively as signals, they must be supported by mobile experi -
ences whose performance characteristics are consistent with
the expectations implied by ethical positioning.
Despite the prominence of sustainability certifications as
quality signals, little empirical research examines how their
credibility depends on alignment with observable digital
execution quality, particularly in mobile-first luxury envi -
ronments. In this sense, sustainability certification is better
understood as an expectation-amplifying signal, increasing
the likelihood that execution-level deviations in mobile UX
will be noticed and penalized. This perspective positions
mobile UX performance as an outcome of and as an exe -
cution-level signal through which certification credibility is
reinforced or undermined in practice.
Methodology
Research design
This study adopts a quantitative, descriptive–predictive
research design grounded in marketing analytics. A for -
mal a priori power analysis was not conducted because the
study relies on a fixed population of sustainability-certified
luxury brands with available real-user field data, not on a
sample designed for hypothesis testing. The objective is to
assess whether sustainability-certified luxury brands deliver
mobile user experiences that are technically consistent with
the execution-quality expectations implied by certification.
Rather than evaluating consumer perceptions directly, the
analysis focuses on observable, execution-level perfor -
mance signals captured through real-user mobile perfor -
mance data.
Mobile user experience quality is operationalized using
Google’s Core Web Vitals, which provide standardized,
field-based indicators of how users experience loading
speed and visual stability on mobile devices. Two metrics
are central to the analysis. LCP captures loading speed by
measuring how quickly the main content becomes visible,
while CLS captures visual stability by measuring unex -
pected layout shifts during page rendering. These metrics
are particularly relevant in luxury contexts, where technical
disruptions can undermine perceived fluency, refinement,
and brand credibility.
The empirical strategy combines three analytical com -
ponents. Firstly, the study benchmarks mobile performance

E. Ciobanu
UX. LCP was included as the primary speed metric used
by Google to summarize real-user loading experience. FCP
was added in a robustness specification to capture earlier
render timing and to assess overlap with LCP. INP which
shows responsiveness was not returned by the API for this
sample and is therefore excluded from inference; for visu -
alization only, TBT from Lighthouse lab audits is used as a
clearly labelled proxy.
All raw PageSpeed Insights JSON files were batch-pro -
cessed in Python 3.11.9 using pandas. The author extracted
the reported percentile/p75 values for CLS, LCP, and FCP.
CLS values were verified to be on a fractional scale; where
a value exceeded 1.0, it was divided by 100 to normalize to
0.00–1.00. LCP and FCP were obtained in milliseconds and
converted to seconds for modeling. Variance inflation fac -
tors were examined to assess multicollinearity; all VIF val -
ues were below commonly accepted thresholds, indicating
that collinearity between LCP and FCP does not materially
affect model estimation.
Statistical analysis and visualization techniques
The analysis is descriptive and predictive in nature; no
causal relationships are inferred and proceeded in three
stages. Firstly, descriptive benchmarks for the field metrics
were produced, reporting means, medians, and 95% con -
fidence intervals for CLS and LCP (with FCP included in
a robustness summary). The researcher also reported the
share of sites in Google’s threshold bands ( good, needs
improvement, poor) and visualized distributions with his -
tograms and box plots. Secondly, to assess sectoral differ -
ences, the Kruskal–Wallis test was applied to non-normally
distributed metrics and conducted Holm-adjusted post-hoc
pairwise comparisons. Thirdly, a binary logistic regres -
sion was estimated for the probability of a fast classifica -
tion (FastUX = 1) as a function of CLS and LCP with sector
controls; a robustness model added FCP to gauge overlap
in speed information. The author reports coefficients, odds
ratios, 95% confidence intervals, and model discrimination
by using the area under ROC curve. From the fitted models
were computed marginal effects and predicted probabilities,
translating metric changes into percentage-point shifts use -
ful as managerial thresholds. Interaction terms, such as CLS
crossed by sector, were explored to benchmark mobile UX
performance across luxury sectors.
Visualizations were created in Python using matplotlib
and seaborn. To highlight relationships among metrics, a
CLS–LCP convergence plot and a radar chart were used
to show normalized performance profiles for top sites. The
radar chart combines CLS, LCP, FCP and, for visualization
only, TBT.
API requests were executed within a single, continuous
data-collection window in April 2025, ensuring temporal
consistency across observations despite the rolling nature
of field data.
Variables and measurement
The dependent variable is mobile experience quality, opera-
tionalized as a binary indicator (as FastUX) derived from
PageSpeed’s page-level field data: sites classified as FAST
are coded 1, and those classified as A VERAGE or SLOW are
coded 0. The core predictors are Google’s Core Web Vitals
from field data. CLS captures visual stability and is used
in its fractional form (0–1), with values ≤ 0.10 interpreted
as “good.” LCP captures loading speed and is obtained in
milliseconds; for modeling the researcher analyzes it in
seconds. FCP also in milliseconds (analyzed in seconds), is
included in a robustness specification to assess overlapping
speed information with LCP. Interaction to Next Paint was
not returned by the PageSpeed API for this sample and is
therefore not analyzed; this fact is labelled by the researcher
as a limitation. For the multidimensional radar visualization
only, Lighthouse’s Total Blocking Time (or TBT) was added
as a lab proxy for responsiveness; TBT is clearly labeled as
lab data and is not used for inference in the main field-data
models.
Control variables include sector (treated as a categori -
cal factor with Fashion & Accessories as the reference cat -
egory) and available brand descriptors (region, founding
year, and employee count, where recorded). All metrics are
extracted from the PageSpeed Insights response’s loading
experience. CLS requires no unit conversion beyond con -
firming fractional scale; LCP and FCP were converted from
milliseconds to seconds for interpretability and comparabil-
ity in regression. Website URLs are normalized (scheme
and trailing-slash harmonization) and merged to the brand
list; observations with missing values for a given analysis
are removed by listwise deletion. The dataset presents valid
field coverage for CLS: 65 sites, LCP: 64 sites, FCP: 65
sites, and INP (Interaction to Next Paint (noted as INP):
0 sites. The predictive sample used for the main logistic
regression (complete cases for FastUX, CLS, and LCP) was
N = 64. FastUX is operationalized using Google PageSpeed
Insights’ field-based classification, where pages labeled
“FAST” are coded as 1 and “A VERAGE” or “SLOW” as 0.
Metric selection and justification
Metric choice followed both theoretical relevance for
mobile CX and data availability in PageSpeed Insights
field responses. CLS was selected as the primary indica -
tor of visual stability, a perceptual quality central to luxury

Fast, stable, or credible? Mobile experience outcomes in certified luxury retail
categories. Descriptively, Fashion & Accessories tends to
cluster at very low CLS, Jewelry & Watches appears higher
on average, and Interiors & Living lies in between, with
Beauty & Fragrance and Travel & Leisure mostly within
the good category (Fig. 2). However, formal testing finds no
statistically significant sectoral differences in CLS (Krus -
kal–Wallis H = 6.078, p  = 0.299; Holm-adjusted pairwise
contrasts non-significant). Accordingly, sector patterns are
reported as descriptive benchmarks rather than evidence
of systematic sector differences in this sample. Thus, sec -
tor patterns should be treated as indicative, not robust once
variability and sample sizes are considered.
To examine the joint behavior of stability and speed,
Fig. 3 presents a CLS–LCP convergence matrix cross -
ing CLS bands (≤ 0.10; 0.10–0.25; > 0.25) with LCP bands
(≤ 2.5 s; 2.5–4.0 s; > 4.0 s). Nearly half of the sample sits in
the good–good cell (29/64, 45.3%). A further 28.1% achieve
good CLS but slower LCP (2.5–4.0 s or > 4.0 s), indicat -
ing that loading speed is the more prevalent constraint. The
mirror trade-off fast LCP with unstable CLS accounts for
14.1% of cases, and only 3.1% fall into the poor–poor cell.
Overall, the matrix shows broad success on visual stability
with meaningful room to improve loading speed; prioritiz -
ing LCP optimization would shift many sites from mixed
quadrants into the good–good cell (top-left of the matrix).
The researcher modelled the probability that a site is
classified as Fast on mobile (FastUX = 1) using a binary
logistic regression with CLS and LCP as predictors and
sector dummies (Fashion & Accessories as the reference).
Model discrimination is outstanding (AUC = 0.919) on
N = 64 complete cases and results (Table 1) show that LCP
is the dominant driver; each additional second reduces the
odds of a Fast label by about 96% (β =  − 3.204, OR = 0.041,
p = 0.003). Equivalently, cutting LCP by one second multi -
plies the odds by roughly 24 × ; even a 0.1-s improvement
raises the odds by about 38%. To see how changes in LCP
To mitigate estimation instability arising from low cell
counts, sector categories with fewer than other sector, such
as ‘Interiors & Living’ observations, were collapsed into
a broader ‘Other luxury categories’ group for regression
analyses.
Ethical considerations
All data were obtained from public sources (Positive Luxury
listings and Google PageSpeed Insights API). The dataset
contains no human subjects or personal data and involves
no intervention; therefore, ethics committee approval was
not required. API requests complied with Google’s Terms
of Service and were rate-limited to avoid undue load. Brand
names and website URLs are publicly available identifiers;
only site-level performance metrics were collected. Raw
JSON files were stored securely and processed into aggre -
gated analysis tables for reproducibility.
Results
The histogram (Fig. 1) shows a strongly right-skewed (posi-
tively skewed) distribution, with most websites clustered
in the good category. Among the 65 sites with valid CLS,
48 (73.8%) meet Google’s good threshold (CLS ≤ 0.10), 7
(10.8%) require improvement (0.10–0.25), and 10 (15.4%)
are poor (> 0.25). This pattern suggests broad adoption of
layout-stability practices, alongside a non-trivial tail of
underperformance that may undermine perceived polish.
A few outliers exhibit very high CLS values, which mer -
its brand-level diagnostics such as late-injected content,
deferred media without reserved space, or font reflow.
Sector-level comparisons are presented for descriptive
benchmarking purposes and should be interpreted as explor-
atory, given the limited number of observations in some
Fig. 1 Distribution of Mobile CLS
Scores. Vertical dashed lines mark
Google’s thresholds at 0.10 (good)
and 0.25 (poor)

E. Ciobanu
By contrast, CLS is not a meaningful predictor here
(β =  − 0.557, OR = 0.573, p  = 0.657); within the observed
range, a 0.10 increase changes the odds by only 5%, and the
confidence interval is wide. After controlling for metrics,
translate into the likelihood of achieving a “Fast” mobile
classification, the visualization presented in Appendix B
strengthens interpretability by making the nonlinear impact
of loading speed immediately visible.
Fig. 3 CLS–LCP convergence
matrix (quadrant markers indicate
good/good, good/slow, etc.). Note:
Cell entries show absolute counts,
with percentages relative to the
full sample (N = 64) reported in
parentheses

Fig. 2 CLS by sector. Note: Kruskal–Wallis H = 6.078,  p = 0.299 (no significant sector differences)

Fast, stable, or credible? Mobile experience outcomes in certified luxury retail
are reported numerically to maintain interpretive caution
given the limited sample size and the exploratory nature of
the field data.
Therefore, improving CLS from 0.18 to 0.08 yields
small gains in the predicted probability of a Fast classifica -
tion: + 1.4 pp in Jewelry & Watches (0.55 to 0.56), + 1.1 pp
in Premium Drinks (0.28–0.29), + 1.0 pp in Fashion &
Accessories (0.75–0.76), and + 0.9 pp in Beauty & Fra -
grance (0.19–0.20). For Interiors & Living and Travel &
Leisure, effects are approximately zero at current median
LCP levels. Managerially, this points to a clear priority:
reduce LCP through asset optimization, critical-path CSS/
JS, server/TTFB improvements, and caching/CDN, while
treating CLS hardening as hygiene that protects perceived
polish.
As a robustness check, adding FCP as an additional speed
indicator raises discrimination to AUC = 0.931. In this speci-
fication, FCP absorbs much of the speed signal (β =  − 5.214,
OR = 0.005, p = 0.055), and LCP remains negative but is no
longer significant (β =  − 1.810, p  = 0.131). This pattern is
consistent with overlapping information between the two-
timing metrics and the modest sample size; the substantive
conclusion is unchanged: speed drives Fast. The robustness
specification including FCP highlights the conceptual over-
lap among speed-related performance metrics. That FCP
absorbs some of LCP’s predictive power is theoretically
consistent with both metrics capturing different phases of
the same underlying construct: perceived loading speed.
Rather than contradicting the main findings, this conver -
gence reinforces the conclusion that speed, irrespective of
the specific metric, is the dominant driver of Fast classifica-
tion. By contrast, CLS appears closer to a baseline hygiene
factor, critical for preserving experiential coherence but
offering limited incremental explanatory power once speed
is accounted for.
For completeness, a radar chart illustrating normalized
performance profiles for selected sites is provided in Appen-
dix A. It shows top five sites with the lowest CLS, combin -
ing CLS, LCP, FCP and, for visual context only, TBT from
Lighthouse. Axes are min–max normalized so values closer
to the center indicate better performance. FAST sites remain
near the center across axes, while several A VERAGE
sites show low CLS but higher LCP/FCP (and sometimes
higher TBT), revealing loading and main-thread bottle -
necks despite stable layouts. Note: Fig. 4 is presented for
descriptive and illustrative purposes only, combining field-
based and lab-based metrics to provide a broad overview of
mobile performance dimensions; no statistical inference or
direct comparison across measurement contexts is implied.
The robustness model including FCP is intended to assess
sensitivity to alternative speed metrics and should be inter -
preted as a supplementary analysis.
Beauty & Fragrance sites have significantly lower odds
of being Fast than Fashion & Accessories (β =  − 2.430,
OR = 0.088,   p = 0.037). Travel & Leisure shows a border -
line penalty (p = 0.066). Jewelry & Watches and Premium
Drinks are not statistically different. Interiors & Living
shows an extreme negative coefficient with an unbounded
confidence interval. Due to quasi-separation caused by
sparse observations in certain sectors, coefficient estimates
for individual sector dummies are reported descriptively and
are not interpreted inferentially. Sector-level coefficients,
particularly for categories with low observation counts such
as Interiors & Living, should be interpreted descriptively
rather than inferentially due to estimation instability.
To translate coefficients into practical guidance, the
researcher computed marginal effects holding each sector’s
median LCP constant. Holding other variables constant,
increases in LCP are associated with a monotonic decline in
the probability that a site is classified as delivering a “Fast”
mobile experience. The magnitude of this decline acceler -
ates as LCP moves beyond commonly used performance
benchmarks, underscoring the practical importance of load-
ing speed for mobile experience outcomes. Marginal effects
Table 1 Predictors of Google “Fast” Mobile Classification
Variable Coef (β) Odds
ratio
(OR)
OR
95%
CI low
OR 95% CI
high
p-value
Intercept 7.981 2925.050 20.173 424,120.674 0.002
CLS  − 0.557 0.573 0.049 6.686 0.657
LCP  − 3.204 0.041 0.005 0.345 0.003
Beauty &
Fragrance
(vs
Fashion &
Accessories)
 − 2.430 0.088 0.009 0.864 0.037
Interiors &
Living
(vs
Fashion &
Accessories)
 − 13.495 0.000 0.000 ∞ 0.944
Jewellery &
Watches
(vs
Fashion &
Accessories)
 − 1.366 0.255 0.035 1.870 0.179
Premium
Drinks
(vs
Fashion &
Accessories)
 − 1.680 0.186 0.012 2.867 0.228
Travel &
Leisure
(vs
Fashion &
Accessories)
 − 2.605 0.074 0.005 1.193 0.066
Dependent variable FastUX ( 1 = Fast). Reference sector = Fashion &
Accessories. N = 64; AUC = 0.919

E. Ciobanu
experience signals. Rather than treating Google’s ‘Fast’
classification as a black-box output, the analysis models its
underlying execution drivers and translates metric changes
into probability shifts, thereby transforming engineering
indicators into decision-relevant analytics insights. Thus,
this distinction contributes to marketing analytics research
by showing that not all UX metrics carry equal explana -
tory or managerial value, and that performance analytics
should account for asymmetric metric roles. This study
connects two strands that are rarely examined together in
luxury research, namely, performance based UX metrics
and sustainability signaling. Using field data from Butterfly
Mark–certified brands, it shows that the credibility of ethi -
cal claims in digital contexts is intertwined with the techni-
cal quality of mobile experiences. In short, the sustainability
story is only as persuasive as the interface that carries it.
It is important to note that the “Fast” classification used
as the dependent outcome in this study is a platform-defined
label assigned by Google, reflecting how mobile perfor -
mance is evaluated and operationalized within a dominant
digital ecosystem. As such, the findings are directly rele -
vant for managers seeking to optimize performance within
platform-mediated environments where external classifica -
tion systems shape visibility, ranking, and user experience
judgments.
The logistic model achieves outstanding discrimina -
tion and indicates that LCP dominates the probability of
being classified as Fast, whereas CLS adds little incremen -
tal predictive power at the levels observed in this sample.
The asymmetric roles of LCP and CLS can be interpreted
through established principles in human–computer inter -
action and luxury customer-experience research. Loading
speed directly shapes users’ earliest perceptual and cogni -
tive evaluations during the critical initial moments of mobile
interaction, when judgments of fluency, responsiveness, and
competence are formed. Delays in content rendering inter -
rupt attentional flow and increase perceived effort, making
speed a highly salient execution signal in mobile-first con -
texts. By contrast, visual stability appears to function as a
hygiene factor: disruptive layout shifts are noticeable and
damaging when present, but once a minimum threshold of
stability is achieved, further improvements yield diminish -
ing experiential returns. In luxury contexts, where baseline
expectations of polish are high, stability is therefore nec -
essary to avoid negative disconfirmation but insufficient to
differentiate experience quality or platform-level perfor -
mance classifications. This interpretation aligns with the
observed distribution of CLS in the sample, where most
certified brands already meet “good” stability thresholds,
leaving loading speed as the primary remaining source
of variation in mobile experience outcomes. This finding
complements HCI theory on interface fluency and trust:
The figure plots the top five sites with the lowest CLS.
Each axis is min–max normalized within the sample to 0–1,
so values closer to the center indicate more favorable per -
formance across metrics. Sites labelled FAST tend to remain
near the center on all axes, indicating balanced strength in
stability and speed. Several A VERAGE sites exhibit low
CLS yet higher LCP and/or FCP (and sometimes higher
TBT), revealing bottlenecks in loading and main thread
blocking despite stable layouts. This pattern underscores the
need to evaluate Web Vitals holistically: strength in visual
stability does not compensate for weaknesses in speed or
responsiveness.
Discussion
This study advances marketing theory by demonstrating
that execution-level digital performance metrics operate as
asymmetric signals within sustainability-certified luxury
contexts. While research conceptualizes sustainability cer -
tification as a quality signal (Kauppi et al. 2025), it has not
examined how observable technical execution interacts with
elevated expectations in mobile-first environments. The
findings show that loading speed functions as a dominant
execution signal (result aligned with other outcomes in the
literature such as Kim et al. ( 2009), whereas visual stabil -
ity operates as a hygiene condition once baseline standards
are met. This also confirms the Deloitte’s ( 2018) insight
which states for 0.1 s improvement in mobile speed which
increases conversion rates and engagement. Therefore, this
asymmetric structure extends signaling theory by specify -
ing that not all execution cues are equally diagnostic under
high-expectation brand positioning. Certification amplifies
expectations of operational competence, rendering execu -
tion-level deviations more consequential in evaluative judg-
ments. This pattern aligns with work on service brand equity
(Berry 2000) and luxury experience formation (Klaus 2021),
which emphasize that violations of expected fluency are
disproportionately penalized in high-value brand contexts.
Loading delays interrupt perceptual continuity and cogni -
tive ease, reinforcing the salience of speed as an execution-
level signal.
Thus, the paper presents the advance analytics theory by
distinguishing between dominant and hygiene performance
dimensions within platform-mediated evaluation environ -
ments. Loading speed emerges as a dominant metric that
strongly shapes classification outcomes, whereas visual sta-
bility functions as a hygiene condition whose primary role is
to prevent negative disconfirmation once baseline thresholds
are met. From a marketing analytics perspective, this study
demonstrates how platform-generated technical metrics
can be reverse-engineered into interpretable probabilistic

Fast, stable, or credible? Mobile experience outcomes in certified luxury retail
From a signaling perspective, this suggests that Beauty &
Fragrance brands may face a sharper tension between expe-
riential richness and executional efficiency, making speed
optimization particularly consequential in this category.
Importantly, this interpretation is descriptive and explor -
atory; it highlights where performance governance efforts
may be most impactful.
Managerially, the implication is clear, by highlighting to
prioritize LCP improvement, optimize image and font pipe-
lines, trim or defer non-critical CSS/JS on the critical path,
reduce TTFB via server and CDN tuning, and cache aggres-
sively. CLS hardening remains essential hygiene (reserved
space for media, predictable font loading, controlled late-
injected content) because it protects perceived polish and
trust, but it does not materially shift the Fast classification
once speed is addressed. The marginal-effects analysis
underscores the asymmetry, tightening CLS from 0.18 to
0.08 yields small probability gains, whereas shaving even
fractions of a second from LCP can move sites across the
fast threshold.
By situating these analytics insights within sustainability-
certified luxury contexts, the study also extends research on
ethical signaling by showing how analytics-based execution
signals interact with expectation formation. Sustainability
certification amplifies expectations of operational quality,
increasing the diagnostic value of execution-level analyt -
ics signals such as mobile performance. From an analytics
standpoint, this highlights how performance metrics gain
contextual meaning depending on brand positioning and
certification status, reinforcing the need for context-aware
analytics frameworks.
Methodologically, the paper demonstrates how Core
Web Vitals can be operationalized as marketing-analytics
signals for LCX dashboards. Convergence matrices reveal
where portfolios sit relative to benchmarks; regression and
marginal effects translate technical changes into managerial
probabilities. These tools are replicable for ongoing perfor-
mance governance and for auditing alignment between sus-
tainability narratives and mobile UX delivery.
Finally, the results foreground an important boundary
condition for sustainability communication in luxury. Certi-
fication may earn initial trust, but ongoing trust is mediated
by experience quality in the high-expectation, mobile-first
contexts where brand meaning is negotiated. Investing in
fast, stable interfaces is more than a technical exercise; it
is a strategic requirement for preserving the authenticity
and premium positioning that sustainability is intended to
support.
The findings translate into clear and prioritized guidance
for luxury brand managers responsible for digital execution.
Firstly, loading speed should be treated as the primary perfor-
mance lever. Actions with the highest expected impact include
moment-to-moment load performance shapes users’ cog -
nitive ease and, by extension, perceptions of quality and
credibility.
At the same time, visual stability is not irrelevant. The
CLS distribution is encouraging, nearly three-quarters of
sites meet the ≤ 0.10 “good” threshold, suggesting that
layout hygiene is largely institutionalized among certified
brands. The convergence matrix clarifies where progress is
still needed; almost half of sites are good on both stability
and speed, yet over a quarter combine good stability with
slow loading, revealing LCP as the more common bottle -
neck. The mirror trade-off, fast but unstable, is smaller but
non-trivial, reinforcing the need to manage both dimensions.
The lack of statistically significant sector differences in
CLS suggests that, within sustainability-certified luxury
brands, visual stability may be closer to a standardized
“hygiene” requirement than a sector-specific differentiator.
One explanation is that Core Web Vitals benchmark logic and
mobile UX conventions impose similar minimum expecta -
tions across categories, so brands converge on layout-sta -
bility practices regardless of sector. A second explanation is
shared technological infrastructure: luxury sites often rely
on similar stacks (CMS platforms, tag managers, consent
tools, third-party scripts), which can homogenize stability
outcomes across verticals even when creative content dif -
fers. Finally, sector-level variation may exist but remain
difficult to detect in field-based samples with uneven cell
sizes; in that setting, the absence of statistical significance
is consistent with effects that are smaller than the domi -
nant, cross-sector role of loading performance. Overall, the
results imply that sector comparisons are most informative
as benchmarks, while the primary actionable leverage point
remains reducing loading delays. Sector patterns should be
interpreted cautiously. Descriptively, some verticals popu -
late the “good–good” cell more often, but formal tests show
no significant sector differences in CLS (p = 0.299). In the
regression, only Beauty & Fragrance retains a residual pen-
alty after controlling for CLS and LCP, which likely reflects
unmeasured content or infrastructure factors, such as asset
strategies, personalization scripts, and hosting architecture.
The residual performance penalty observed for Beauty
& Fragrance sites after controlling for loading speed and
visual stability likely reflects category-specific execution
choices. Beauty and fragrance brands tend to rely heavily
on rich visual assets, high-resolution imagery, video back -
grounds, personalization layers, and third-party integrations
(such as recommendation engines, analytics, consent tools),
all of which can increase critical-path load and main-thread
activity. In mobile contexts, these design and marketing fea-
tures may be strategically justified to convey sensorial rich-
ness and brand storytelling, yet they introduce performance
trade-offs that disproportionately affect loading speed.

E. Ciobanu
observed here. Accordingly, the dominance of loading speed
over visual stability should not be assumed to generalize beyond
luxury or similarly high-expectation brand environments.
This study contributes to business analytics research by
demonstrating how platform-defined technical classifications
can be reverse-engineered into interpretable, probability-based
performance insights. Rather than treating Google’s “Fast”
label as a black-box outcome, the analysis shows how underly-
ing execution metrics can be modeled to quantify the marginal
impact of technical improvements on experience classifica-
tions. This approach advances analytics research by illustrat-
ing how operational data generated by digital platforms can
be transformed into actionable decision metrics, bridging the
gap between technical measurement systems and managerial
analytics.
From a business analytics practice perspective, the findings
provide a clear framework for prioritizing digital optimization
efforts. The results show that not all UX metrics contribute
equally to platform-level outcomes: loading speed functions
as a high-leverage variable with large marginal effects, while
visual stability operates primarily as a risk-mitigation met -
ric once baseline standards are met. For analytics teams, this
implies that dashboards, KPIs, and optimization roadmaps
should differentiate between dominant and hygiene metrics.
Based on these insights, several analytics-oriented recom-
mendations follow. Firstly, organizations should integrate Core
Web Vitals into customer experience analytics as probabilis-
tic performance indicators rather than binary pass–fail checks.
Secondly, analytics governance should focus on monitoring
and optimizing loading speed as the primary driver of plat -
form-defined experience outcomes, using marginal-effects
analyses to guide resource allocation. Thirdly, stability metrics
should be treated as hygiene thresholds that protect experience
quality but offer limited incremental returns once minimum
standards are achieved. Together, these recommendations pro-
vide a structured analytics approach for aligning sustainability
signaling, mobile execution, and performance governance in
high-expectation digital environments.
Conclusions
This study makes two primary theoretical contributions.
Firstly, to marketing analytics, it demonstrates how plat -
form-level technical metrics, specifically Google’s Core
Web Vitals, can be operationalized as execution-quality
signals within customer experience analytics. The analysis
reframes them as probabilistic predictors of platform-medi-
ated experience classifications, translating engineering met-
rics into interpretable managerial thresholds. This extends
marketing analytics research by showing how real-user per-
formance data can be integrated into experience governance
optimizing and resizing hero images and video thumbnails,
preloading and sub-setting brand fonts, reducing render-block-
ing CSS and JavaScript on the critical path, improving server
response time through CDN configuration, and caching non-
critical assets. Even small reductions in LCP can materially
increase the likelihood of delivering a “Fast” mobile experi-
ence. Secondly, visual stability should be managed as a non-
negotiable hygiene requirement. Brands should ensure reserved
space for images and embedded media, avoid late-injected con-
tent above the fold, implement predictable font-loading strate-
gies, and audit third-party scripts that introduce layout shifts.
While these measures may not substantially increase Fast clas-
sification probabilities on their own, they protect perceived
polish, trust, and experiential coherence. Thirdly, resource pri-
oritization matters. When budgets or development capacity are
constrained, the evidence suggests that investments in speed
optimization yield higher returns than marginal improvements
in already-acceptable stability. For categories such as Beauty
& Fragrance, where rich media and personalization are central
to storytelling, performance governance should focus on bal-
ancing experiential richness with disciplined asset and script
management to prevent speed degradation. Together, these
recommendations enable luxury brands to align sustainability
signaling with credible, high-quality mobile execution.
In practice, luxury brands often face trade-offs between
competing digital investments, particularly when develop -
ment resources, budgets, or release cycles are constrained. The
findings suggest that not all UX improvements deliver equal
returns. When baseline visual stability is already acceptable,
further refinements in CLS may protect experiential polish
but generate limited incremental gains in mobile performance
classification. By contrast, investments that reduce loading
delays, such as optimizing media assets, streamlining scripts,
or improving server response times, offer disproportionately
higher returns by materially increasing the probability of deliv-
ering a fast mobile experience. For resource-constrained teams,
this implies a sequencing logic: first secure layout stability to
avoid negative disconfirmation, then allocate incremental
resources to speed optimization, which functions as the pri-
mary driver of performance outcomes. Framing mobile UX
optimization in this way enables managers to make defensible,
data-informed trade-offs rather than pursuing uniformly “per-
fect” experiences that may not be economically feasible.
The findings should also be interpreted considering the spe-
cific context examined. The analysis focuses on sustainability-
certified luxury brands, which operate under unusually high
expectations of quality, polish, and execution consistency. In
such contexts, baseline visual stability may already be insti-
tutionalized, rendering CLS closer to a hygiene condition. In
mass-market or low-involvement categories, where expecta-
tions and tolerance for friction differ, the relative roles of speed
and stability may not follow the same asymmetric pattern

Fast, stable, or credible? Mobile experience outcomes in certified luxury retail
(reserved space, predictable font loading, disciplined late-
injection) as hygiene that protects perceived polish and
trust, even if it does not, on its own, shift the Fast classi -
fication. Thirdly, use convergence matrices and marginal-
effects dashboards to track portfolios and translate technical
changes into clear probability gains for decision-making.
In sustainability-certified luxury contexts, mobile perfor-
mance carries symbolic weight: interface delays or insta -
bility can undermine the perceived authenticity of ethical
positioning by signaling executional inconsistency.
Limitations
In terms of limits, the author is aware that cohort is restricted
to Butterfly Mark, certified brands, which may limit general-
izability. It is important to note that the sample size for this
study (N = 64) remains a limitation, particularly with respect to
the inclusion of several sector dummies in the logistic regres-
sion model. Although the findings provide useful insights, they
should be interpreted with caution, and future research should
aim for larger, more representative samples to validate these
results. Moreover, sector-level coefficients should be inter -
preted descriptively, not inferentially, as the analysis is not
powered to estimate precise effects for low-frequency catego-
ries. The study relies on Core Web Vitals field data available
in the PageSpeed API; INP was not returned for this sample
and could not be modeled, and FCP was used only as a robust-
ness check. Core Web Vitals are commonly interpreted using
benchmark thresholds such as “good” vs. “needs improve -
ment”. In this study, thresholds are used primarily to support
interpretability and managerial translation and then to claim
universal cutoffs. Alternative threshold choices such as stricter
targets for high-end luxury experiences, or more lenient cutoffs
reflecting heterogeneous mobile conditions would change the
proportion of sites classified as meeting benchmarks, but they
would not change the conceptual interpretation of the models:
loading performance metrics capture the dominant source of
variation in “Fast” classification in this dataset, whereas visual
stability appears closer to a baseline hygiene condition among
certified luxury brands. Accordingly, threshold-based state-
ments should be interpreted as decision aids more than immu-
table standards. The design is observational, so causal claims
are not warranted; coefficients and AUC are in-sample and
may be optimistic. Given the limited number of observations
in some sectors, sector effects are included primarily to control
for broad category differences. Additionally, within this sample
of sustainability-certified luxury brands, technical mobile per-
formance varies, indicating that certification alone does not
imply uniformly high execution quality. Finally, the researcher
does not model back-end architecture or front-end framework
choices that undoubtedly shape performance. Nevertheless,
the study’s strengths, such as, ecologically valid field data,
and diagnostic dashboards in high-expectation categories.
Secondly, to HCI, the findings provide field-based evidence
for an asymmetric role of mobile UX dimensions in lux -
ury contexts. Loading speed emerges as a dominant signal
shaping early experience judgment, while visual stability
operates as a hygiene condition that prevents negative dis -
confirmation but offers limited differentiation once baseline
expectations are met. By situating this distinction within
sustainability-certified luxury environments, the study
advances HCI research on how performance signals interact
with contextual expectations and symbolic brand meaning
under real-world mobile conditions.
Managerial implications
This study offers both theoretical and managerial implications
by linking sustainability signaling, luxury customer experi-
ence, and mobile performance analytics within a unified exe-
cution-level framework. The findings yield several actionable
implications for luxury brand managers and digital leaders.
Firstly, mobile loading speed should be treated as the primary
performance lever in mobile optimization efforts. Even small
improvements in loading time materially increase the likeli-
hood that a site is classified as delivering a fast experience, sug-
gesting high returns from investments in image optimization,
critical-path CSS and JavaScript reduction, server response
time improvements, and content delivery networks.
Secondly, visual stability should be managed as a baseline
hygiene factor and not a differentiator. While most certified
brands already meet recommended CLS thresholds, lapses in
layout stability can quickly erode perceptions of polish and
trust. Managers should therefore enforce strict layout-disci-
pline practices, including reserving space for dynamic content,
controlling late content injection, and stabilizing font loading.
Thirdly, sustainability-certified luxury brands should recog-
nize that ethical signaling elevates expectations of execution
quality across digital touchpoints. Certification alone does not
insulate brands from negative experience judgments if mobile
performance falls short. Accordingly, mobile UX metrics
should be integrated into brand governance and sustainability
oversight processes, ensuring that technical execution aligns
with the values communicated through certification.
Finally, the convergence-matrix and marginal-effects
approach demonstrated in this study provides a practical diag-
nostic framework that managers can use to prioritize optimi-
zation efforts, benchmark portfolios, and translate technical
metrics into clear probability-based performance targets.
Managerial implications are direct. Firstly, treat LCP
reduction as the priority lever by optimizing images and
fonts, minimize critical-path CSS/JS, reduce TTFB through
server/CDN tuning, and use caching and lazy-loading for
non-critical assets. Secondly, maintain CLS hardening

E. Ciobanu
practices that explain why some sustainability-certified brands
achieve superior mobile execution while others do not.
More broadly, the findings underscore that in contemporary
luxury markets, digital marketing strategy cannot be separated
from technical execution. Mobile interfaces are not neutral
delivery channels but active sites where brand meaning, trust,
and credibility are negotiated in real time. Sustainability certi-
fications and ethical narratives may attract attention and shape
expectations, but their persuasive power ultimately depends
on whether the mobile experience performs in ways consis-
tent with luxury’s promise of effortlessness and refinement.
From a strategic perspective, this implies that luxury brands
must integrate mobile performance governance into their core
brand management and sustainability strategies and not treat-
ing it as a downstream technical concern. Investments in speed,
stability, and performance monitoring should be understood as
brand-protective actions that sustain premium positioning in
mobile-first environments. As digital touchpoints increasingly
dominate luxury consumption journeys, technical excellence
becomes a central component of how luxury value is created,
communicated, and maintained.
Appendix A. The radar chart
See Fig. 4.
objective industry-standard metrics, a transparent and repro-
ducible pipeline, triangulation across descriptive benchmarks,
non-parametric tests, predictive modeling, and robustness
checks, which support credible inferences and deliver action-
able guidance for luxury managers while providing a replicable
analytics template for future research.
Future research
Several targeted research directions emerge from this study.
Firstly, comparative designs that include both sustainabil -
ity-certified and non-certified luxury brands would allow
researchers to test whether certification is associated with
systematically different levels of mobile UX performance or
whether the observed variation reflects broader industry prac-
tices. Secondly, future work should incorporate responsiveness
metrics such as INP as field data coverage improves, enabling a
more complete assessment of how speed, stability, and interac-
tivity jointly shape luxury mobile experiences. Thirdly, linking
Core Web Vitals to downstream behavioral and commercial
outcomes, such as bounce rates, conversion probability, dwell
time, or repeat visits, would clarify how technical performance
translates into economic value in luxury contexts. Finally,
mixed-method approaches combining field metrics with
qualitative interviews of UX and digital teams could surface
organizational constraints, design trade-offs, and governance
Fig. 4 Radar chart for top sites,
combining field metrics (CLS,
LCP, FCP) and TBT as a lab proxy.
Note: CLS, LCP, and FCP are field-
based metrics, while TBT is a lab-
based metric. Metrics are displayed
jointly for illustrative context only
and are not directly comparable.
Moreover, TBT is included for
illustrative purposes only and is not
used in statistical inference

Fast, stable, or credible? Mobile experience outcomes in certified luxury retail
are provided to support transparency and interpretability
and are not intended for out-of-sample prediction (Tables
2 and 3).
Calculation details
Predicted probabilities are computed using the estimated
logistic regression model:
logit (P (Fast = 1)) = β0+ βLCPLCP + βCLSCLS
P (f ast)= 1 1+e −logit
Data availability Available data on request.
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
Appendix B. Predicted probabilities and
marginal effects
This appendix reports the predicted probabilities underly -
ing Fig. 5 and documents how these values were derived
from the estimated logistic regression model. The results
Table 2 Predicted probability of a “Fast” mobile classification by LCP
(CLS fixed at 0.10)
LCP (seconds) CLS (fixed) Predicted probability of fast
1.50 0.10 0.9577
1.75 0.10 0.9104
2.00 0.10 0.8201
2.25 0.10 0.6718
2.50 0.10 0.4788
2.75 0.10 0.2920
3.00 0.10 0.1562
3.25 0.10 0.0767
3.50 0.10 0.0360
3.75 0.10 0.0165
4.00 0.10 0.0075
4.25 0.10 0.0034
4.50 0.10 0.0015
4.75 0.10 0.0007
5.00 0.10 0.0003
5.25 0.10 0.0001
5.50 0.10 0.0001
5.75 0.10 0.0000
6.00 0.10 0.0000
The predicted probabilities are post-estimation quantities derived
directly from the coefficients reported in Table 1 and are included
solely to aid interpretation
Table 3 Logistic regression coefficients used for predicted probabili -
ties
Variable Coeficient
Intercept 7.981
LCP  − 3.204
CLS  − 0.557
Fig. 5 Predicted Probability of a
“Fast” Mobile Classification as a
Function of Loading Speed LCP.
Note: Predicted probabilities are
derived from the main logistic
regression model reported in
Table 1. Largest Contentful Paint
varies across the range shown,
while Cumulative Layout Shift is
held constant at 0.10 (the “good”
threshold). All other covariates are
held at their reference levels

E. Ciobanu
Deloitte. 2018. Millisecond makes milions. A study on how improve -
ments in mobile site speed positively affect a brand’s bottom
line.Available at:  h t t p  s : /  / w w w  . t  h i n  k w i t  h g o  o g l  e . c  o m /  _ q s /  d o  c u m
e n t s  / 9 7  5 7 /  M i l  l i s  e c o n  d s  _ M a  k e _ M  i l l  i o n  s _ r e p o r t _ h Q Y A b Z J . p d f
(Accessed: 9 February 2026).
Web Dev. 2025. Core Web Vitals | web.dev. Available at:  h t t p  s : /  / w e b  . d  e
v /  e x p l  o r e  / l e  a r n  - c o  r e - w  e b  - v i t a l s (Accessed: 30 April 2025).
Dryl, W. 2023. History as a factor creating the value of a luxury brand.
Annales Universitatis Mariae Curie-Skłodowska Sectio H Oeco -
nomia 56 (5): 63–80.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  7 9 5  1 / h  . 2 0 2 2 . 5 6 . 5 . 6 3 - 8 0.
Duric, Z., W. D. Gray, R. Heishman, F. Li, A. Rosenfeld, M. J.
Schoelles, C. Schunn, and H. Wechsler. 2002. Integrating per -
ceptual and cognitive modeling for adaptive and intelligent
human-computer interaction. Proceedings of the IEEE  90 (7):
1272–1289.
Erdman, A., A. Gouwy, G. Sananes, et al. 2025. Experience-based
risk taking is primarily shaped by prior learning rather than by
decision-making. Nature Communications 16:6310.  h t t p  s : /  / d o i  . o  r
g /  1 0 . 1  0 3 8  / s 4  1 4 6 7 - 0 2 5 - 6 1 6 0 9 - 0.
Fu, X., and X. Ren. 2023. Order effect of multi-touchpoints on Genera-
tion Z consumers. International Journal of Consumer Studies 47
(4): 1516–1532.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 1 1  / i j  c s . 1 2 9 3 1.
Hepner, J., J. Chandon, and D. Bakardzhieva. 2020. Competitive
advantage from marketing the SDGs: A luxury perspective. Mar-
keting Intelligence & Planning 39 (2): 284–299.  h t t p  s : /  / d o i  . o  r g /  1
0 . 1  1 0 8  / m i  p - 0 7 - 2 0 1 8 - 0 2 9 8.
Holdener, M., A. Gut, and A. Angerer. 2020. Applicability of the user
engagement scale to mobile health: a survey-based quantitative
study. Jmir Mhealth and Uhealth  8 (1) : e13244.  h t t p s : / / d o i . o r g
/ 1 0 . 2 1 9 6 / 1 3 2 4 4     .
Ieva, M., and C. Ziliani. 2018. The role of customer experience touch-
points in driving loyalty intentions in services. The TQM Journal
30 (5): 444–457.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 0 8  / t q  m - 1 1 - 2 0 1 7 - 0 1 4 1.
Jain, S., S. Mishra, and G. Saxena. 2022. Luxury customer’s motiva -
tions to adopt gamification. Marketing Intelligence & Planning
41 (2): 156–170.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 0 8  / m i  p - 0 5 - 2 0 2 2 - 0 2 0 7.
Judijanto, L., R. Nurrohman, and E. Erwin. 2024. A bibliometric
exploration of corporate sustainable marketing: innovation strat -
egy and consumer engagement. West Science Social and Humani-
ties Studies 2 (09): 1457–1469.  h t t p  s : /  / d o i  . o  r g /  1 0 . 5  8 8 1  2 / w  s s h s . v
2 i 0 9 . 1 2 7 0.
Kapferer, J. and Michaut-Denizeau, A. 2017. ‘Is Luxury Compatible
With Sustainability? Luxury Consumers’ Viewpoint’, pp. 123–
156.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 0 7  / 9 7  8 - 3 - 3 1 9 - 5 1 1 2 7 - 6 _ 7.
Kauppi, K., C. Hannibal, and M. Bryde-Evens. 2025. ‘The certificate
doesn’t taste like anything’: Perspectives of sustainability signal-
ing in global supply chains. European Management Journal.  h t t p
s : /  / d o i  . o  r g /  1 0 . 1  0 1 6  / j .  e m j . 2 0 2 5 . 1 1 . 0 0 3.
Kim, H., and L. M. Niehm. 2009. The impact of website quality on
information quality, value, and loyalty intentions in apparel retail-
ing. Journal of Interactive Marketing 23 (3): 221–233.  h t t p  s : /  / d o
i  . o  r g /  1 0 . 1  0 1 6  / j .  i n t m a r . 2 0 0 9 . 0 4 . 0 0 9.
Klaus, P. 2021. What matters most to ultra-high-net-worth individu -
als? Exploring the UHNWI luxury customer experience (ULCX).
Journal of Product & Brand Management 31 (3): 368–376.  h t t p  s
: /  / d o i  . o  r g /  1 0 . 1  1 0 8  / j p  b m - 1 0 - 2 0 2 0 - 3 1 6 4.
Król, K., and W. Sroka. 2023. Internet in the middle of nowhere: Per -
formance of geoportals in rural areas according to Core Web
Vitals. Isprs International Journal of Geo-Information  12 (12) :
484.  h t t p  s : /  / d o i  . o  r g /  1 0 . 3  3 9 0  / i j  g i 1 2 1 2 0 4 8 4.
Kusal, S., et al. 2022. AI-based conversational agents: A scoping
review from technologies to future directions. IEEE Access
10:92337–92356.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 0 9  / A C  C E S S . 2 0 2 2 . 3 2 0 1 1
4 4.
Lang, X., C. Fang, W. Li, Z. Wang, and W. Cai. 2025. Biases of experi-
ence: How entrepreneurial background shapes CEO preferences
holder. To view a copy of this licence, visit  h t t p  : / /  c r e a  t i  v e c  o m m o  n s .  o
r g  / l i c e n s e s / b y / 4 . 0 /.
References
AbouElgheit, E. 2024. The role of generative AI in shaping millen -
nials and gen Z’s orientation toward luxury products. Journal of
Marketing Development and Competitiveness.  h t t p  s : /  / d o i  . o  r g /  1 0 .
3  3 4 2  3 / j  m d c . v 1 8 i 2 . 7 0 1 2.
Abu Bakar, N. A., R. Musa, and M. Muda. 2024. Does social media
influencer credibility affect attitudes and engagement behav -
iour? - Empirical evidence. European Proceedings of Social and
Behavioural Sciences .  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  5 4 0  5 / e  p s b s . 2 0 2 4 . 0 5 . 6
1.
Achugbu, T. U. 2016. Exploration of customers’ expectation of, and
perception of the service they receive from mobile phone provid-
ers. Texila International Journal of Management 2 (1): 158–211.
h t t p  s : /  / d o i  . o  r g /  1 0 . 2  1 5 2  2 / t  i j m  g . 2  0 1 5 .  0 2  . 0 1 . a r t 0 1 4.
Akkaya, B., C. Popescu, and S. Üstgörül. 2024. How can we remove
psychological entrepreneurship barriers on entrepreneurship
intention for health organizations in the future? Sustainability 16
(8) : 3503.  h t t p  s : /  / d o i  . o  r g /  1 0 . 3  3 9 0  / S U  1 6 0 8 3 5 0 3.
Al-Zuabi, I. M., A. Jafar, and K. Aljoumaa. 2019. Predicting custom -
er’s gender and age depending on mobile phone data. Journal of
Big Data.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 8 6  / s 4  0 5 3 7 - 0 1 9 - 0 1 8 0 - 9.
Andriyani, N. K. R., and P. G. A. Yudhistira. 2023. How does conven-
tional travel agent services enhance brand loyalty? The relation -
ship between customer experience, brand credibility, and brand
trust. Jurnal Manajemen Teori Dan Terapan | Journal of Theory
and Applied Management 16 (1): 162–178.  h t t p  s : /  / d o i  . o  r g /  1 0 . 2  0
4 7  3 / j  m t t . v 1 6 i 1 . 4 3 1 7 0.
Athwal, N., et al. 2019. Sustainable luxury marketing: A synthesis and
research agenda. International Journal of Management Reviews
21 (4): 405–426.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 1 1  / i j  m r . 1 2 1 9 5.
Balcombe, L., and D. De Leo. 2022. Human-computer interaction in
digital mental health. Informatics 9 (1) : 14.  h t t p  s : /  / d o i  . o  r g /  1 0 . 3  3
9 0  / i n  f o r m a t i c s 9 0 1 0 0 1 4.
Bansal, D. 2024. How SEO makes website loads faster and helps in
user engagement. International Journal for Multidisciplinary
Research.  h t t p  s : /  / d o i  . o  r g /  1 0 . 3  6 9 4  8 / i  j f m  r . 2  0 2 4 .  v 0  6 i 0 2 . 1 5 2 9 1.
Baxendale, S., E. K. Macdonald, and H. Wilson. 2015. The impact of
different touchpoints on brand consideration. Journal of Retail -
ing 91 (2): 235–253.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 1 6  / j .  j r e t a i . 2 0 1 4 . 1 2 . 0 0 8.
Berry, L. L. 2000. Cultivating service brand equity. Journal of the
Academy of Marketing Science 28 (1): 128–137.  h t t p  s : /  / d o i  . o  r g /  1
0 . 1  1 7 7  / 0 0  9 2 0 7 0 3 0 0 2 8 1 0 1 2.
Boustani, G., and H. Zielinski. 2023. ‘How does a fashion brand’s cus-
tomer experience translate in premium & luxury retail formats?
A parisian retail market outlook. Journal of Business & Retail
Management Research.   h t t p  s : /  / d o i  . o  r g /  1 0 . 2  4 0 5  2 / j  b r m  r / v  1 7 i s  0 2  /
a r t - 0 3.
Chen, Y ., et al. 2010. Impact of signals and experience on trust and
trusting behavior. Cyberpsychology Behavior and Social Net -
working 13 (5): 539–546.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 9  / c y  b e r . 2 0 0 9 . 0 1
8 8.
Chevalier, M., and M. Gutsatz. 2020. Luxury retail and digital man -
agement: Developing customer experience in a digital world .
Hoboken: John Wiley & Sons.
Chung, S., T. Krämer, and E. M. Wong. 2018. Do touch interface users
feel more engaged? The impact of input device type on online
shoppers’ engagement, affect, and purchase decisions. Psychol-
ogy and Marketing  35 (11): 795–806.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 0 2  / m
a  r . 2 1 1 3 5.

Fast, stable, or credible? Mobile experience outcomes in certified luxury retail
Theocharis, D., and G. Tsekouropoulos. 2025. Sustainable consump -
tion and branding for Gen Z: How brand dimensions influence
consumer behavior and adoption of newly launched technological
products. Sustainability 17 (9) : 4124.  h t t p  s : /  / d o i  . o  r g /  1 0 . 3  3 9 0  / s u
1 7 0 9 4 1 2 4.
Vannucci, V ., and E. Pantano. 2019. Digital or human touchpoints?
Insights from consumer-facing in-store services. Information
Technology and People  33 (1): 296–310.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 0
8  / I T  P - 0 2 - 2 0 1 8 - 0 1 1 3.
Vázquez-Martínez, U., J. Morales-Mediano, A. L. Leal-Rodríguez, et
al. 2025. Navigating the storm: How managers’ decisions shape
companies in crisis. Review of Managerial Science  19:1567–
1597.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 0 7  / s 1  1 8 4 6 - 0 2 4 - 0 0 8 0 1 - w.
Wang, Y . M., and C. Q. Rodriguez. 2024. The aesthetic factors shap-
ing Chinese Millennial consumers’ purchase intentions of luxury
pyjamas: Implications for future design. Advances in Science and
Technology 146:107–114.  h t t p  s : /  / d o i  . o  r g /  1 0 . 4  0 2 8  / p -  u 2 e z k j.
Wibagso, S. S. 2023. The empirical study of Joomla CMS map
extension and location performance. Matrix Jurnal Manajemen
Teknologi Dan Informatika 13 (2): 94–105.  h t t p  s : /  / d o i  . o  r g /  1 0 . 3  1 9
4  0 / m  a t r i x . v 1 3 i 2 . 9 4 - 1 0 5.
Wu, L., and Y .-C. Tang. 2022. Mobile payment in omnichannel retail-
ing: Dynamics between trust and loyalty transfer processes. Inter-
net Research 32 (6): 1783–1805.  h t t p s :   /  / d o  i . o  r  g  /  1 0  . 1 1   0 8 /  i  n t r  - 0 6
-  2 0 2 1 - 0 4 0 2.
Publisher's Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
Dr. Eliza Ciobanu  is a researcher and lecturer in digital marketing
and data-driven consumer research. She holds a Ph.D. in Marketing
and works as a lecturer at the Transylvania University of Brașov in
Romania, where she teaches and supervises research at the intersec -
tion of digital marketing, analytics, and consumer behaviour. Her
research spans digital marketing strategy, consumer behaviour, tech -
nology acceptance, and online customer experience, with publications
addressing topics such as mobile performance in customer journeys,
behavioural intention to adopt emerging technologies, the digital
divide in European contexts, and the role of analytical frameworks in
understanding digital consumer interactions. Dr. Ciobanu combines
analytical rigor with a multidisciplinary approach to evaluate how
digital environments shape decision-making and marketing outcomes.
Her work draws on quantitative and qualitative methods to explore
how organisations and consumers interact with digital systems, includ-
ing analytics, consumer profiling, ethical signalling, and the adoption
of AI-supported tools, contributing to theory and practice in digital
marketing and data analytics. She actively collaborates with academic
and industry partners across Europe, bridging research and practice to
contribute to data-driven marketing initiatives and human-technology
interaction studies.
in green innovation. Journal of Behavioral Finance.  h t t p  s : /  / d o i  . o
r g /  1 0 . 1  0 8 0  / 1 5  4 2 7  5 6 0  . 2 0 2  5 .  2 6 0 3 9 6 6.
Positive Luxury. 2025 The Butterfly Mark - Sustainability Certification
for Luxury Brands. Available at:  h t t p  s : /  / w w w  . p  o s i  t i v e  l u x  u r y  . c o  m /
b  u t t e  r fl   y - m a r k / (Accessed: 30 April 2025).
Massi, M., et al. 2025. Toward D2A: enhancing luxury fashion with
seamless and immersive phygital customer experiences. Interna-
tional Journal of Consumer Studies .  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 1 1  / i j  c s .
7 0 0 4 5.
Mossberg, L. 2008. Extraordinary experiences through storytelling.
Scandinavian Journal of Hospitality and Tourism 8 (3): 195–210.
h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 0  / 1 5  0 2 2 2 5 0 8 0 2 5 3 2 4 4 3.
Piligrimienė, Ž, et al. 2020. Internal and external determinants of con-
sumer engagement in sustainable consumption. Sustainability 12
(4): 1349.  h t t p  s : /  / d o i  . o  r g /  1 0 . 3  3 9 0  / s u  1 2 0 4 1 3 4 9.
Priyadarshini, B. I., and U. D. Prasad. 2023. ‘Luxury redefined:
exploring sustainable practices and ethical branding in the green
age. International Journal for Multidisciplinary Research.  h t t p  s : /
/ d o i  . o  r g /  1 0 . 3  6 9 4  8 / i  j f m  r . 2  0 2 3 .  v 0  5 i 0 6 . 8 6 5 1.
Qualid, C., D. Selma, and B. Soufyane. 2024. The impact of content
personalization on customer engagement and market risks of
E-stores. Financial Markets, Institutions and Risks  8 (3): 37–56.
h t t p  s : /  / d o i  . o  r g /  1 0 . 6  1 0 9  3 / f  m i r . 8 ( 3 ) . 3 7 - 5 6 . 2 0 2 4.
Ramtohul, A. and Khedo, K. K. 2023 An engaging user experience
framework for mobile augmented reality.  h t t p  s : /  / d o i  . o  r g /  1 0 . 2  1 2 0
3 / r  s . 3 . r s - 3 0 8 0 6 8 0 / v 1.
Rolling, V ., and A. Sadachar. 2018. Are sustainable luxury goods a
paradox for Millennials? Social Responsibility Journal  14 (4):
802–815.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 0 8  / s r  j - 0 7 - 2 0 1 7 - 0 1 2 0.
Romero, D. J. M. and Torres, F. 2024 ADAN pharmacy greater acces-
sibility.  h t t p  s : /  / d o i  . o  r g /  1 0 . 2  1 3 9  / s s  r n . 4 9 0 4 3 9 9.
Saunila, M., J. Ukko, and T. Rantala. 2019. Value co-creation through
digital service capabilities: The role of human factors. Informa-
tion Technology and People 32 (3): 627–645.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1
1 0 8  / i t  p - 1 0 - 2 0 1 6 - 0 2 2 4.
Seale, M., A. Hicks, and K. Nicholson. 2022. Toward a critical turn in
library UX. College & Research Libraries .  h t t p  s : /  / d o i  . o  r g /  1 0 . 5  8
6 0  / c r  l . 8 3 . 1 . 6.
Shao, S. and Chang, W. 2020. ‘Research on computer wireless net -
work assisted industrial design in human-computer interaction’.  h
t t p  s : /  / d o i  . o  r g /  1 0 . 2  1 2 0  3 / r  s . 3 . r s - 3 0 3 3 8 / v 1.
Simanjuntak, R. A. 2023. Customer perceptions of mobile telecommu-
nication providers in determining satisfaction and loyalty: Focus-
ing on college students. Gema Wiralodra 14 (3): 1047–1060.  h t t p
s : /  / d o i  . o  r g /  1 0 . 3  1 9 4  3 / g  w . v 1 4 i 3 . 5 7 6.
Song, S., and H. Kim. 2022. Is social media marketing worth it for
luxury brands? The dual impact of brand page satisfaction and
brand love on word-of-mouth and attitudinal loyalty intentions.
Journal of Product & Brand Management 31 (7): 1033–1046.  h t t
p  s : /  / d o i  . o  r g /  1 0 . 1  1 0 8  / j p  b m - 0 6 - 2 0 2 0 - 2 9 3 6.
