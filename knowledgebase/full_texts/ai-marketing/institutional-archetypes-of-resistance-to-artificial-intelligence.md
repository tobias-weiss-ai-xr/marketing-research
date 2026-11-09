---
title: Institutional archetypes of resistance to artificial intelligence
url: https://doi.org/10.3389/fhumd.2026.1871733
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: Frontiers in Human Dynamics
authors:
- Michal Kubovics
source: openalex-oa
pdf_url: https://www.frontiersin.org/journals/human-dynamics/articles/10.3389/fhumd.2026.1871733/pdf
pages: 8
chars: 45912
fetched_at: '2026-11-08T18:03:15+00:00'
kb_version: 1
---

# Institutional archetypes of resistance to artificial intelligence

EDITED BY
Narcisa Medranda - Morales,
Universidad Politecnica Salesiana - Sede
Quito, Ecuador
REVIEWED BY
Abel Suing,
Universidad Técnica Particular de Loja,
Ecuador
Büş ra Ökten,
Istanbul Medeniyet University, Türkiye
Ionut Virgil Serban,
University of Craiova, Romania
*CORRESPONDENCE
Michal Kubovics
michal.kubovics@ucm.sk
RECEIVED 05 May 2026
REVISED 30 June 2026
ACCEPTED 06 July 2026
PUBLISHED 04 August 2026
CITATION
Kubovics M (2026) Institutional
archetypes of resistance to artificial
intelligence.
Front. Hum. Dyn. 8:1871733.
doi: 10.3389/fhumd.2026.1871733
COPYRIGHT
© 2026 Kubovics. This is an open-access
article distributed under the terms of the
Creative Commons Attribution License
(CC BY). The use, distribution or
reproduction in other forums is
permitted, provided the original author(s)
and the copyright owner(s) are credited
and that the original publication in this
journal is cited, in accordance with
accepted academic practice. No use,
distribution or reproduction is permitted
which does not comply with these
terms.
Institutional archetypes of
resistance to artificial intelligence
Michal Kubovics*
Faculty of Mass Media Communication, Department of Marketing Communication, University of Sts.
Cyril and Methodius in Trnava, Trnava, Slovakia
Introduction: What is the underlying structure of resistance to the adoption of
artificial intelligence in media organisations? This study is the first to combine
Ising network analysis with latent class analysis (LCA) to map the architecture
of barriers to the adoption of artificial intelligence and to identify individual-
level archetypes of resistance, interpreted through the lens of institutional logic.
Methods: Data were collected in March 2026 from 151 media and marketing
professionals from the UK and the US via the Prolific platform. Seven barriers
were measured as binary indicators. The analysis combined Ising network
analysis (IsingFit, with a comparative EBICglasso estimation and bootstrapped
stability checks), latent class analysis (poLCA, K = 2–5), Kruskal-Wallis tests
with effect sizes, and binary logistic regression supplemented with IRT
composites.
Results: The Ising model reveals a sparse ’hub-and-spoke’ network of barriers
(2 out of 21 possible edges), in which mistrust acts as a central node linking
legal risk (w = 2.832) and quality concerns (w = 3.431), whilst the five
remaining barriers function as conditionally independent dimensions. LCA
(K = 2, BIC = 1063.6, entropy = 1.000, bootstrap stable in 99.5% of 200
resamples) identifies two qualitatively distinct archetypes: T1 Practical
Opponents (42.4%, n = 64), characterised by structural and capacity barriers in
the complete absence of distrust [P = 0.000 (95% CI: 0.000, 0.000)]; and T2
Distrustful Sceptics (57.6%, n = 87), defined by absolute distrust [P = 1.000
(0.934, 1.000)] and satur ated legal (P = 1.000) and qualita tiv e barriers
(P = 1.000). A sensitivity LCA without distrust confirms the two-class structure
(BIC = 972.2, entropy = 1.000), thereby establishing robustness beyond a
simple division based on distrust. Membership of an archetype is not
predicted by organisation type, frequency of AI use, or perceived risk/benefit
scores (binary logistic regression, all p > 0.24; Nagelkerke’s pseudo-R2 =
0.040). T2 sceptics demand significantly greater transparency regarding AI
content (M = 4.44 vs. 3.97; H = 9.401, p = 0.002, r = 0.250), whilst exhibiting
comparable preferences for human oversight to T1.
Discussion: Validation of the theory of resistance to innovation confirms that T1
are passive resisters (functional/psychological ratio F/P = 1.16) and T2 are active
resisters (F/P = 0.61; H = 70.324, p < 0.001, r = 0.682). The findings are consistent
with an interpretation of archetypes as epistemological rather than structural
constructs, although the absence of significant predictors does not by itself
exclude measurement limitations or limited statistical power.
KEYWORDS
barriers to the adoption of artificial intelligence, institutional archetypes, Ising model,
latent class analysis, media organisations, network analysis, theory of resistance to
innovation
TYPE Original Research
PUBLISHED 04 August 2026
DOI 10.3389/fhumd.2026.1871733
Frontiers in Human Dynamics 01 frontiersin.org

1 Introduction
The integration of generative artificial intelligence within
media and marketing organisations does not encounter a
uniform type of resistance, but rather qualitatively different
epistemic attitudes. Experts who approach this integration with
hesitation raise fundamentally different objections; specifically,
some point to the absence of the organisational infrastructure
necessary for the responsible deployment of artificial intelligence
tools, whilst others express deep epistemological distrust of the
final outputs produced by these tools. The two types of
resistance mentioned above do not differ in degree but in their
fundamental nature, and as the study’s results empirically
demonstrate, common methodological approaches—whether in
the form of surveys on the frequency of obstacles or composite
resistance scales—are unable to adequately capture this
distinction. Research focused on the challenges of implementing
artificial intelligence in a media context is divided into two
methodological strands. The first catalogs the occurrence of
individual barriers using descriptive statistics (Newman et al.,
2024; Thurman et al., 2019), while the second uses regression
models to verify whether the level of support differs across
organizational groups (Beckett and Deuze, 2016). These two
approaches ultimately define a limitation: within them, barriers
are either treated as mutually uncorrelated items or aggregated
into a single composite index of resistance, with both implicitly
assuming the one-dimensional nature of the phenomenon under
study. The assumption is not sufficiently theoretically grounded
and, as research suggests, empirically verifiable. The theory of
resistance to innovation (Huang et al., 2021) explicitly
distinguishes between functional barriers, practical obstacles that
can be addressed through targeted training and organizational
policies, and psychological barriers that reflect value conflicts
and epistemic dispositions that require systematic trust building
and normative reassessment. The categories refer to empirically
distinguishable professional profiles, which has direct and
significant implications for the design of intervention strategies,
where treating passive and active resisters equally will yield less
than ideal outcomes for both groups. Research defines the
importance of the above question. Focus group surveys of news
organizations in the countries surveyed identify persistent
skepticism toward AI in journalism, with only a minority
comfortable with news stories generated solely by AI and
expressing significantly higher trust when the process is led by a
human (Fletcher and Nielsen, 2025). Parallel focus group
research links skepticism to already low trust in news media and
calls for greater transparency about where and how AI is being
used (Minnesota Journalism Center, 2025). In terms of
production, research on British journalists and newsrooms
documents uneven adoption of AI, influenced not only by
attitudinal and ethical reservations but also by skills gaps
(Thurman et al., 2025), while qualitative studies show that
media professionals are showing deliberate restraint and aligning
the use of AI with established professional values, rather than
rejecting or fully embracing the technology (Cools et al., 2024).
It is important to add that in the field of marketing
communications, there has been extraordinary progress in the
adoption of AI, although legal, quality and ethical concerns
remain (Buder et al., 2024). The aforementioned studies identify
trust, transparency, and professional identity as recurring
problem areas, but continue to address the barriers either
individually or as a whole, without examining the underlying
structure of resistance, a gap that the study addresses.
The research focus of the study is defined by three research
questions:
RQ1: What is the structure of the conditional dependencies of
barriers to the implementation of artificial intelligence; do they
form an interconnected syndrome or a sparse, partially
orthogonal network?
RQ2: Do media and marketing experts form latent classes
defined by qualitatively distinct barrier profiles?
RQ3: Do the identified archetypes differ in their management
requirements, perceptions of artificial intelligence, and
epistemological orientation based on IRT?
2 Theoretical framework
The theory of resistance to innovation (Huang et al., 2021)
identifies two mutually independent sources of resistance to
technology. The identified barriers stem from the perceived
incompatibility of the innovation with current work processes,
skills, and organizational norms. The obvious potential lies in
the fact that these barriers can be overcome, particularly
through appropriate training, clear guidelines, and
communication with stakeholders. Psychological barriers, on the
other hand, reflect value conflicts and epistemic dispositions, as
well as doubts about whether the innovation is trustworthy,
ethically appropriate, or consistent with one’s professional
identity. These barriers cannot be removed simply by providing
information, as they require deeper processes of trust-building
and a reevaluation of norms. The distinction is epistemological
rather than purely attitudinal. In particular, the difference in the
degree of trust reflects the extent to which an individual views
the technology positively, the epistemological orientation relates
to a prior dispositional stance from which evidence about the
technology is interpreted—whether AI outputs are considered
provisionally reliable until proven otherwise, or are inherently
suspect regardless of case-specific evidence. Research examining
journalists’ attitudes toward generative artificial intelligence finds
that experts neither simply accept nor reject this technology, but
rather negotiate their stance through attitudes rooted in their
professional values and understanding of trustworthy knowledge
(Cools et al., 2024). From this perspective, the archetype is not a
transient preference but a relatively stable interpretive
disposition that determines which obstacles an individual
emphasizes, as it is precisely this dispositional, knowledge-and-
value-based character—and not the credibility score itself—that
matters. Talke and Heidenreich (2014) expand on this
framework by distinguishing between passive resistance—
characterized by inaction and a lack of organizational capacity—
and active resistance, which is intentional in nature and rooted
in the expert’s value beliefs. Passive resisters are primarily
prevented from adopting innovation by functional barriers,
while active resisters face barriers of a psychological nature.
These two profiles therefore require fundamentally different
intervention approaches. For the first type, capacity building is
Kubovics                                                                                                                                                               10.3389/fhumd.2026.1871733
Frontiers in Human Dynamics 02 frontiersin.org

relevant; for the second type, the systematic building of epistemic
trust is essential. In the context of introducing artificial
intelligence into the media environment, functional barriers
include, in particular, a lack of professional skills, the absence of
clear organizational guidelines, and resistance from clients.
Psychological barriers primarily include distrust of AI-generated
outputs and ethical concerns regarding the potential impact of
AI on the professional integrity of experts. Network analysis of
psychological constructs (Borsboom and Cramer, 2013;
Epskamp and Fried, 2018) offers an alternative to factor analysis
when examining the structure of agreement regarding barriers.
While factor models assume a common latent cause, network
models map direct conditional associations between observed
variables. The Ising model (Haslbeck and Waldorp, 2020; Van
Borkulo et al., 2014) is designed for binary node data, making it
particularly suitable for dichotomous assessments of barriers. If
the barriers form a dense network of conditional relationships
with a high number of strong partial correlations, they can be
interpreted as a resistance syndrome; in such cases, a targeted
solution focused on key nodes can trigger a cascade effect and
also contribute to reducing peripheral barriers. Conversely,
when the network is sparse, individual barriers are conditionally
independent, and each requires a specific intervention approach.
Previous work applying the EBICglasso approach (Epskamp
et al., 2012) to binary data may be subject to a tendency
towards oversimplification, manifested in the generation of
empty networks. The Ising model represents a methodologically
more appropriate alternative for binary data and therefore serves
as the primary network analytical method in this study. The
theory of institutional logic (Lounsbury et al., 2021; Thornton
et al., 2012) is based on the assumption that professional
behaviour reflects a set of competing logics: journalistic logic,
centred on truth and verification; market logic, where efficiency
and profit are key; and professional logic, defined as autonomy
and expertise. These coexist within organisations rather than
being organisationally separated from one another. It follows
from the above that archetypes of resistance to artificial
intelligence will not cluster along lines of company type, sector
or degree of AI usage, but will ultimately reflect the individual
epistemological orientations of individual professionals. Insofar
as affiliation with a given archetype cannot be predicted on the
basis of structural variables, this provides empirical
confirmation of the interpretation in the spirit of institutional
logic theory and, at the same time, suggests that organisations
must operate at the individual level when deploying diagnostic
tools, rather than applying blanket strategies applicable to the
entire sector.
3 Methodology
Data were collected in March 2026 via the Prolific platform,
which has been validated for professional research (Palan and
Schitter, 2018; Peer et al., 2022). Prolific was selected over
alternative professional sampling strategies (e.g., panel providers
or LinkedIn-based recruitment) because it combines pre-
screened, verifiable employment information with documented
data-quality standards and transparent participant
compensation, while allowing targeted recruitment of currently
employed media, journalism and marketing professionals in
the UK and the US. Participants were required to be
currently employed in the media, journalism or marketing
communications in the UK or the US. The final sample
comprised N = 151 respondents. In terms of gender, 53.0% were
women (n = 80), 42.4% were men (n = 64), 2.6% were non-
binary (n = 4), and 2.0% did not wish to specify (n = 3). The
largest age group was 26–35 years (38.4%, n = 58). The type of
organisation was freelancer 35.1% (n = 53), agency 21.2%
(n = 32), other/public sector 16.6% (n = 25), media 15.9%
(n = 24), corporate sector 11.3% (n = 17). 60.9% of respondents
used generative AI several times a week or daily. Participants
selected up to seven barriers from a list of seven options, with
responses being binary (1 = selected, 0 = not selected): (1) Lack
of trust in the reliability and accuracy of the technology; (2)
Ethical concerns and moral dilemmas; (3) Legal risks (copyright,
GDPR); (4) Insufficient quality, consistency or superficiality of
outputs; (5) Resistance from clients or the public; (6) Lack of
digital skills and insufficient staff training; (7) Lack of internal
guidelines and unclear organisational rules. The average number
of selected barriers was M = 3.31 (SD = 1.04). Respondents rated
three statements on a scale from 1 (strongly disagree) to 5
(strongly agree): (1) AI in the workplace requires stricter
internal guidelines; (2) audiences and clients must always be
informed about AI-generated content; (3) human oversight and
fact-checking of AI content are essential. The average overall
management score was M = 4.23 (SD = 0.69). The analysis was
conducted in four stages. In the first stage, a network analysis
was performed using the Ising model via IsingFit (Van Borkulo
et al., 2014) and the comparative EBICglasso method (Epskamp
et al., 2012), with three gamma values (0.25, 0.50, 0.75) tested
and stability verified by bootstrapping (200 repetitions; Epskamp
et al., 2018). In the second phase, latent class analysis was
performed using poLCA (Linzer and Lewis, 2011) with K = 2–5
classes, with model selection based on BIC and entropy, and
stability confirmed by 200 resamplings and 500 repeated LCA
selections. In the third phase, the archetypes were compared
using Kruskal–Wallis tests with rank-biserial r and Cohen’s h
effect sizes. In the fourth phase, binary logistic regression tested
organisational and demographic predictors of archetype
membership, and the results were supplemented with IRT
composites of barriers (Huang et al., 2021). All analyses were
conducted in R 4.5 using the IsingFit, bootnet, poLCA, ggplot2
and patchwork packages.
4 Results
The most frequently reported barriers were legal risks (84.8%,
n = 128) and quality concerns (75.5%, n = 114) (Table 1), which
were present in almost the entire sample. Mistrust (57.6%,
n = 87) and ethical concerns (57.6%, n = 87) had a moderate
prevalence. Less common were client resistance (27.2%), lack of
skills (16.6%) and lack of guidelines (11.9%). As legal and
qualitative barriers were reported by almost everyone, they have
limited ability to distinguish between archetypes. The main
distinguishing feature is therefore mistrust, which occurred
unevenly.
Kubovics                                                                                                                                                               10.3389/fhumd.2026.1871733
Frontiers in Human Dynamics 03 frontiersin.org

The Ising model identified two significant correlations out of
21 possible ones (Table 2), specifically between mistrust and
legal aspects (weight 2.832) and between mistrust and quality
(weight 3.431). The remaining five barriers showed no
significant correlations following the analysis. EBICglasso
confirmed the same results. When tested with gamma values of
0.25, 0.50 and 0.75, 4, 2 and 2 edges emerged, with both key
connections persisting in all cases. The network stability (CS
coefficient = 0.675) was acceptable. The structure described is
theoretically comprehensible. Distrust functions as the sole
central node of the network (strength centrality = 6.263,
betweenness = 1) and links perceptions of legal and qualitative
risks. The network is neither a dense cluster—five of the seven
barriers remain mutually independent—nor entirely unrelated.
It is rather a specific cluster, as experts who distrust AI have
both legal and qualitative concerns, suggesting a common
source in the form of epistemic distrust in the reliability of AI.
The remaining four barriers (client resistance, lack of skills,
missing guidelines and ethical concerns) operate independently.
BIC clearly favoured the two-class model (BIC = 1,063.6)
(Table 3) over the three-class models (BIC = 1,091.6;
ΔBIC =  + 28.0), four (BIC = 1,122.2; ΔBIC =  + 30.6) and five
classes (BIC = 1,153.2; ΔBIC =  + 31.1). Entropy = 1.000 indicates
perfect class separation, with every respondent reliably assigned
to a single class. The bootstrap BIC confirmed this choice in
99.5% of cases (199 out of 200 repetitions favoured K = 2).
T1 are practical opponents (n = 64; Table 4); these respondents
express no distrust of the technology (0.000), but have relatively
high concerns regarding ethics (0.609) and legal risks (0.641).
They are less concerned about the quality of outputs (0.422).
Client resistance and lack of skills are moderate, whilst a lack of
guidelines is almost non-existent. T2 are distrustful sceptics
(n = 87); these respondents have the highest level of distrust in
the technology (1.000) and, at the same time, the highest
TABLE 1 Prevalence of barriers to AI implementation and effect size across archetypes (N = 151).
Barrier n Prevalence % Cohen’s h (T1 vs. T2) Interpretation
Legal risks 128 84.8 1.286 High, T2 saturated, T1 moderate
Inadequate quality of outputs 114 75.5 1.728 High, T2 saturated, T1 moderate
Lack of trust in technology 87 57.6 3.142 Very large, decisive difference
Ethical concerns 87 57.6 0.117 Negligible, similar across all archetypes
Client/audience resistance 41 27.2 0.464 Low, T1 predominates
Lack of digital skills 25 16.6 0.467 Small, T1 predominates
Lack of internal guidelines 18 11.9 0.053 Negligible, similar across all archetypes
Cohen’s h calculated from archetype-specific conditional probabilities. Mean number of obstacles reported per respondent: M = 3.31, SD = 1.04.
TABLE 2 Ising network, edge weights and node centrality statistics.
Barrier Strength Intermediacy Closeness State
Distrust 6.263 1 1.551 Head Office, brings together the legal and quality departments
Legal risks 2.832 0 1.002 Spoke, margin of distrust (w = 2.832)
Quality of outputs 3.431 0 1.068 Spoke, threshold for distrust (w = 3.431)
Ethics, Client, Skills, Guidelines 0 0 NA Isolated, conditionally independent
Ising model (IsingFit, family = binomial). Total number of edges: 2/21 (9.5%). EBICglasso confirms the same structure with 2 edges. CS coefficient (case-drop bootstrap, 200
resamples) = 0.675.
Bold values indicate the central node of the network (highest strength centrality).
TABLE 4 Conditional LCA probabilities P(barrier=1|class) with 95% bootstrap
confidence intervals.
Barrier T1 Practical
opponents (n = 64)
T2 Distrustful
sceptics (n = 87)
Distrust of
technology
0.000 [0.000, 0.000] 1.000 [0.934, 1.000]
Ethical concerns 0.609 [0.488, 0.733] 0.552 [0.451, 0.653]
Legal risks 0.641 [0.504, 0.757] 1.000 [1.000, 1.000]
Quality of
outputs
0.422 [0.281, 0.550] 1.000 [1.000, 1.000]
Client/audience
resistance
0.391 [0.273, 0.518] 0.184 [0.101, 0.273]
Lack of digital
skills
0.266 [0.154, 0.388] 0.092 [0.036, 0.154]
Lack of internal
guidelines
0.109 [0.045, 0.197] 0.126 [0.061, 0.193]
Bold is defining, increased conditional probability according to archetype. CI = 95%
bootstrap confidence intervals [500 LCA resamples with class assignment via P(Distrust)].
Entropy = 1.000; all classifications are deterministic.
TABLE 3 LCA model fit statistics (K = 2–5).
K BIC AIC Entropy Min. proportion of
classes
LL
2* 1,063.6 1,018.3 1.000 42.4% −494.1
3 1,091.6 1,022.2 0.993 3.1% −488.1
4 1,122.2 1,028.6 0.996 3.2% −483.0
5 1,153.2 1,035.5 0.944 6.0% −478.7
* = selected model. nrep = 50, maxiter = 3,000, set.seed = 42. Bootstrapped BIC: K = 2
selected in 99.5% of 200 repeated samples. ΔBIC (K = 2 vs. K = 3) =  + 28.0.
Bold values indicate the selected model (K = 2, lowest BIC).
Kubovics                                                                                                                                                               10.3389/fhumd.2026.1871733
Frontiers in Human Dynamics 04 frontiersin.org

concerns regarding legal risks and the quality of outputs (both
1.000). Ethical concerns are moderate (0.552). Client resistance,
lack of skills and lack of guidance are low. T1 is primarily
concerned about practical obstacles (ethics, law, quality), but
does not resist the technology itself. T2 combines complete
distrust of the technology with maximum legal and quality
concerns, which corresponds to the epistemic cluster from the
previous network analysis. An important test was whether the
division into two classes arose solely due to the ‘distrust’
variable. An LCA analysis without this variable confirmed the
same two-class solution (BIC = 972.2; ΔBIC compared to K = 3
is +15.8; Entropy = 1.000; MinClass = 24.5%). The remaining six
barriers were also able to perfectly separate the two classes on
their own, confirming that these are genuine differences in the
configuration of the barriers, not merely the presence or absence
of distrust. Kruskal–Wallis tests (Table 5) showed that the
overall difference in governance between the classes (T1 where
M = 4.08, T2 where M = 4.33; H = 4.033, p = 0.045, r = 0.163)
conceals an important pattern. The only item that differed
significantly between the archetypes was transparency; sceptics
in T2 demanded significantly higher transparency of AI content
(M = 4.44 vs. 3.97; H = 9.401, p = 0.002, r = 0.250, small to
medium effect). Regulation (H = 0.253, p = 0.615) and human
oversight (H = 1.098, p = 0.295) did not differ between groups.
The pattern corresponds to the T2 profile: experts who
fundamentally distrust AI outputs, specifically requiring that the
audience be aware of the origin of AI content, and who perceive
transparency as a systemic safeguard. Practical opponents (T1),
whose barriers are more capacity-related than epistemic, showed
slightly higher, though statistically insignificant, support for
human oversight (M = 4.36 vs. 4.55), which corresponds to their
preference for practical verification protocols.
The greatest difference was in the number of barriers
(H = 88.406, p < 0.001, r = 0.765), where T2 sceptics reported
almost twice as many barriers (M = 3.95) as T1 (M = 2.44),
which is a direct consequence of the fact that distrust, legal risks
and quality occur simultaneously in T2. The benefits, risks and
frequency of AI use did not differ between the groups.
Belonging to an archetype therefore does not depend on how
much someone uses AI or how they rate it overall. The results
confirmed differences between the groups (Table 6), where
functional barriers (legal, quality, client, skills, guidelines) were
higher in T2 (M = 0.480, SD = 0.099) than in T1 (M = 0.366,
SD = 0.153; H = 23.264, p < 0.001, r = 0.392, which is a moderate
effect), reflecting strong legal and quality concerns in T2.
Psychological barriers (distrust, ethics) were significantly higher
in T2 (M = 0.776, SD = 0.250) than in T1 (M = 0.305, SD = 0.246;
H = 70.324, p < 0.001, r = 0.682, large effect). The ratio of
functional to psychological barriers confirms the typology: T1
has a ratio of 1.16 (functional barriers predominate, passive
resistance) and T2 has a ratio of 0.61 (psychological barriers
predominate, active resistance).
Binary logistic regression (dependent variable where T2 = 1,
T1 = 0; predictors such as frequency of AI use, organisation
type, perceived benefits, perceived risks for N = 151) revealed no
significant predictors (all p > 0.24; Nagelkerke’s pseudo-
TABLE 5 Comparison of long-term outcomes by LCA archetype (kruskal–wallis tests).
Variable T1 M (SD) T2 M (SD) H p Sig. r (effect size)
Number of barriers 2.44 (0.77) 3.95 (0.68) 88.406 <0.001 *** 0.765, Large
Composite governance indicator 4.08 (0.77) 4.33 (0.65) 4.033 0.045 * 0.163, Low
Transparency requirement 3.97 (1.08) 4.44 (0.82) 9.401 .002 ** 0.250, Small–medium
Regulatory demand 3.92 (1.01) 4.00 (0.99) 0.253 0.615 ns 0.041, negligible
Requirement for human supervision 4.36 (0.97) 4.55 (0.73) 1.098 0.295 ns 0.085, negligible
Perceived benefits 3.46 (0.98) 3.08 (1.24) 1.976 0.160 ns 0.114, Low
Perceived risks 3.98 (0.80) 4.12 (0.89) 1.850 0.174 ns 0.111, Low
Frequency of AI use 3.77 (1.29) 3.38 (1.45) 2.502 0.114 ns 0.129, Small
Bold values indicate statistically significant differences between archetypes (p < 0.05).
r = effect size according to rank-biserial [r = sqrt(H)/sqrt(N); N = 151]. Interpretation:.1 = small,.3 = medium,.5 = large.
Transparency is a sub-item of the Governance component.
*** p < .001.
** p < .01.
* p < .05.
TABLE 6 IRT validation: composite functional vs. psychological barriers by archetype.
Archetype Functional M (SD) Psychological M (SD) F/P ratio H (KW test) p
T1 Practical opponents 0.366 (0.153) 0.305 (0.246) 1.16 H_func=23.264 < 0.001
T2 Distrustful sceptics 0.480 (0.099) 0.776 (0.250) 0.61 H_psyc=70.324 <0.001
Functional barriers is average (legal, quality, client, skills, guidelines). Psychological barriers = average (distrust, ethics). F/P ratio > 1 is functional dominance (passive resistance to IRT);
<1 = psychological dominance (active resistance to IRT). r (functional) = 0.392; r (psychological) = 0.682.
Bold values indicate the dominant barrier category within each archetype.
Kubovics                                                                                                                                                               10.3389/fhumd.2026.1871733
Frontiers in Human Dynamics 05 frontiersin.org

R2 = 0.040). Organisation type was not significant in any contrast
(all p > 0.43). Frequency of AI use also showed no association
(B = −0.026, SE = 0.180, p = 0.887). Neither perceived benefits
(B = −0.254, p = 0.244) nor perceived risks (B = −0.004,
p = 0.987) were predictive. Pseudo-R2 = 0.040 means that the
factors examined explain only 4% of the variance in archetype
affiliation. This supports the interpretation of institutional logic:
if resistance were primarily structural, the type of organisation
or frequency of AI use would predict it. Their absence confirms
that T1 and T2 reflect epistemological dispositions that occur
across organisations regardless of sector, size or degree of
exposure to technologies.
5 Discussion
Ising’s network revealed a structure that refutes both the
’syndrome’ model, in which barriers form a tight cluster, and the
model of complete independence, in which all barriers are
independent of one another. Instead, a ‘hub-and-spoke’ structure
emerges, where epistemic distrust links legal and quality
concerns, whilst the five other barriers—ethics, client resistance,
skills, guidelines and their interconnections—operate
independently. This structure has direct implications for
intervention. Focusing on epistemic mistrust may lead to a
reduction in legal and quality concerns, but only among T2
professionals, whose profile is encompassed by this cluster. For
practical T1 opponents, building trust would not help; they need
the development of organisational infrastructure. The central
role of distrust builds on theoretical insights into epistemic trust
in AI systems (Gillath et al., 2021; Glikson and Woolley, 2020).
In a media context, legal and quality concerns are not
independent assessments; they are partly rooted in a deeper
dispositional distrust of the reliability of AI. This suggests that
the concerns reported in T2 are not primarily the result of
specific negative experiences or knowledge of legal details, but
rather a more fundamental epistemic attitude towards AI
outputs. The T1 and T2 typology provides the first empirical
validation of the IRT functional-psychological distinction in the
context of AI acceptance, using a person-centred LCA method
instead of composite scales. Previous applications of IRT
(Kleijnen et al., 2009; Laukkanen et al., 2008) used variable-
centred approaches; the LCA approach verifies whether the
categories mentioned actually correspond to latent groups with
distinct configurations of barriers. It should be noted that the
elevated psychological-barrier composite in T2 is driven almost
entirely by distrust rather than by ethical concerns, which were
comparable across archetypes (Cohen’s h = 0.117); the
functional–psychological contrast therefore rests primarily on the
distrust dimension. The finding regarding transparency (T2 > T1;
H = 9.401, p = 0.002, r = 0.250) provides important specificity. T2
sceptics do not call for more regulation in general; specifically,
they demand the systematic disclosure of the origin of AI-
generated content. This is consistent with Diakopoulos (2020)
and Newman et al. (2024); experts who distrust AI want the
audience to have sufficient information for their own evaluation,
rather than automatically trusting AI content. Practical
opponents of T1, conversely, favour human oversight as a
practical tool for quality control, not as a statement of AI’s
untrustworthiness. The absence of significant structural
predictors (pseudo-R2 = 0.040) is a notable finding; rather than
confirming a purely epistemological interpretation, it provides no
evidence that T2 sceptics cluster in journalistic organisations,
small firms without guidelines, or among experienced experts.
This null result is, however, also compatible with the modest
sample size and the limited statistical power available for
detecting structural effects, and should therefore be interpreted
with caution. Both archetypes occur in relatively even
proportions across all structural categories. This is consistent
with the theory of institutional logic: competing logics coexist
within organisations, creating different epistemological
orientations that transcend structural boundaries. We note,
however, that the present data were collected at the individual
level, and the term ‘institutional’ is used here to denote the
logics that individuals internalise, not a measured organisational-
level property. Inferences about organisational resistance should
therefore be treated as theoretical rather than empirically
established. The practical implication is straightforward:
organisations cannot simply identify which departments contain
more sceptics. The typology of resistance to AI is distributed
across organisations and requires diagnostic tools at the
individual level, such as a short five-item screening tool assessing
distrust, client concerns and self-efficacy of skills. The following
are the limitations of the study. Firstly, the sample (N = 151) was
recruited exclusively in the United Kingdom and the United
States via Prolific. This limits the generalisability of the findings
to other geographical and cultural contexts, and future research
should extend the sample to continental European, Latin
American and Asian settings. Secondly, although Prolific is a
validated platform for professional research, participants who
self-select into a study explicitly concerned with AI may hold
attitudes that differ systematically from the broader population
of media and marketing professionals; the choice of Prolific over
alternative professional sampling frames is a pragmatic one,
justified by access to a verified, employed professional pool, but
it is not free of selection bias. Thirdly, the relatively modest
sample size, in relation to the complexity of the combined Ising–
LCA analytical strategy, constrains statistical power, particularly
for the logistic regression predicting archetype membership; null
structural effects should be read in this light. Fourthly, the K = 2
solution is significantly influenced by the distrust variable.
Although a sensitive LCA without the distrust subitem confirms
a two-class structure (BIC = 972.2, entropy = 1.000), the main
classification signal originates from this single binary variable.
Future research should employ graded measures of barrier
intensity to enable more nuanced results. Fifthly, binary
measurements of barriers, where ’selected’ and ‘not selected’ lose
information about intensity; resistance may vary within each
archetype in ways that binary LCA cannot capture. Sixthly, the
cross-sectional design does not allow us to determine whether
experts change their archetype affiliation over time or respond to
organisational interventions. Finally, a two-archetype typology,
while parsimonious and empirically well-separated in the present
data, may not exhaust the diversity of epistemological positions
towards AI; richer, graded measures may reveal additional or
intermediate profiles, and the two-class structure should be
regarded as a first approximation rather than an
exhaustive taxonomy.
Kubovics                                                                                                                                                               10.3389/fhumd.2026.1871733
Frontiers in Human Dynamics 06 frontiersin.org

6 Conclusion
This study demonstrates that resistance to AI in media and
marketing organisations shifts from a single-construct barrier
problem to a typology of two archetypes based on the theory of
resistance to innovation and institutional logic. The Ising
network reveals that barriers to AI adoption form a ‘hub-and-
spoke’ structure rather than a syndrome structure, with mistrust
being the central epistemic node linking legal and qualitative
concerns. LCA with perfect entropy (E = 1.000) and 99.5%
bootstrap stability identifies two qualitatively distinct archetypes:
practical opponents (42.4%) and distrustful sceptics (57.6%),
whose inter-organisational distribution confirms their
epistemological, rather than structural, nature. An analysis of
governance requirements shows that the archetypes are not
distinguished by the overall level of requirements, but by their
type. T2 sceptics specifically demand transparency regarding AI
content, which corresponds to their focus on systematic
disclosure. For T1 practical opponents, interventions aimed at
capacity building, training, the creation of guidelines and
communication with clients are appropriate. For distrustful T2
sceptics, it is necessary to build epistemic trust through
transparent governance, verifiable quality protocols and clear
disclosure of the origin of AI. Treating both groups equally is
not only ineffective; it represents a fundamental
misunderstanding of the nature of their resistance.
Data availability statement
The data analyzed in this study is subject to the following
licenses/restrictions: The raw data supporting the conclusions of
this article are not publicly available due to participant privacy
considerations. The data were collected via the Prolific platform
under conditions of anonymity; however, re-identification
cannot be fully excluded. The data may be made available by
the corresponding author upon reasonable request, subject to
ethical approval. Requests to access these datasets should be
directed to michal.kubovics@ucm.sk.
Ethics statement
The studies involving humans were approved by Ethical
Committee for Science and Research at the Faculty of Mass
Media Communication at the University of Ss. Cyril and
Methodius in Trnava, Slovakia. The studies were conducted in
accordance with the local legislation and institutional
requirements. The ethics committee/institutional review board
waived the requirement of written informed consent for
participation from the participants or the participants’ legal
guardians/next of kin because the study used a survey
conducted entirely online via the Prolific platform.
Author contributions
MK: Supervision, Methodology, Validation,
Conceptualization, Resources, Investigation, Writing – review &
editing, Data curation, Software, Funding acquisition, Writing –
original draft, Project administration, Formal analysis,
Visualization.
Funding
The author(s) declared that financial support was received for
this work and/or its publication. Funded by the EU
NextGenerationEU through the Recovery and Resilience Plan for
Slovakia under project No. 09I03-03-V04-00367.
Conflict of interest
The author(s) declared that this work was conducted in the
absence of any commercial or financial relationships that could
be construed as a potential conflict of interest.
Generative AI statement
The author(s) declared that generative AI was not used in the
creation of this manuscript.
Any alternative text (alt text) provided alongside figures in this
article has been generated by Frontiers with the support of
artificial intelligence and reasonable efforts have been made to
ensure accuracy, including review by the authors wherever
possible. If you identify any issues, please contact us.
Publisher’s note
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their affiliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
claim that may be made by its manufacturer, is not guaranteed
or endorsed by the publisher.
References
Beckett, C., and Deuze, M. (2016). On the role of emotion in the future of journalism.
Soc. Media Soc. 2 (3), 1–6. doi: 10.1177/2056305116662395
Borsboom, D., and Cramer, A. O. J. (2013). Network analysis: an integrative approach
to the structure of psychopathology. Annu. Rev. Clin. Psychol. 9, 91–121. doi: 10.1146/
annurev-clinpsy-050212-185608
Buder, F., Hesel, P., Schamp, C., and Mende, M. (2024). Transparency Without Trust?
Consumer Reactions to AI-Generated Marketing Content. Nuremberg, Germany: NIM
Marketing Intelligence Review.
Cools, H., Diakopoulos, N., Helberger, N., Li, C., Kung, E., Rinehart, A., et al. (2024).
Generative AI in Journalism: The Evolution of Newswork and Ethics in a Generative
Kubovics                                                                                                                                                               10.3389/fhumd.2026.1871733
Frontiers in Human Dynamics 07 frontiersin.org

Information Ecosystem. New York, NY, United States: Associated Press/Northwestern
University.
Diakopoulos, N (2020). Computational news discovery: towards design
considerations for editorial orientation algorithms in journalism. Digit. Journal.
8(7), 964–977. doi: 10.1080/21670811.2020.1736946
Epskamp, S., Borsboom, D., and Fried, E. I. (2018). Estimating psychological
networks and their accuracy: a tutorial paper. Behav. Res. Methods 50 (1), 195–212.
doi: 10.3758/s13428-017-0862-1
Epskamp, S., Cramer, A. O. J., Waldorp, L. J., Schmittmann, V. D., and Borsboom, D.
(2012). qgraph: network visualizations of relationships in psychometric data. J. Stat.
Softw. 48 (4), 1–18. doi: 10.18637/jss.v048.i04
Epskamp, S., and Fried, E. I. (2018). A tutorial on regularized partial correlation
networks. Psychol. Methods. 23 (4), 617–634. doi: 10.1037/met0000167
Fletcher, R., and Nielsen, R. K. (2025). Generative AI and News Report 2025: How
People Think About AI’s Role in Journalism and Society. Oxford, United Kingdom:
Reuters Institute for the Study of Journalism.
Gillath, O., Ai, T., Branicky, M. S., Keshmiri, S., Davison, R. B., and Spaulding, R.
(2021). Attractiveness and trust in artificial intelligence. Comput. Human. Behav.
115, 106607. doi: 10.1016/j.chb.2020.106607
Glikson, E., and Woolley, A. W. (2020). Human trust in artificial intelligence: review of
empirical research. Acad. Manag. Ann. 14 (2), 627–660. doi: 10.5465/annals.2018.0057
Haslbeck, J. M. B., and Waldorp, L. J. (2020). mgm: estimating time-varying mixed
graphical models in high-dimensional data. J. Stat. Softw. 93 (8), 1–46. doi: 10.
18637/jss.v093.i08
Huang, D., Jin, X., and Coghlan, A. (2021). Advances in consumer innovation
resistance research: a review and research agenda. Technol. Forecast. Soc. Change.
166, 120594. doi: 10.1016/j.techfore.2021.120594
Kleijnen, M., Lee, N., and Wetzels, M. (2009). A review of consumer resistance to
innovation and its determinants. J. Econ. Psychol. 30 (3), 344–357. doi: 10.1016/j.
joep.2009.02.004
Laukkanen, T., Sinkkonen, S., Kivijarvi, M., and Laukkanen, P. (2008). Segmentation
of banking customers based on resistance to mobile banking. Int. J. Mob. Commun. 6
(3), 309–320. doi: 10.1504/IJMC.2008.017513
Linzer, D. A., and Lewis, J. B. (2011). poLCA: an R package for latent class analysis
with polytomous variables. J. Stat. Softw. 42 (10), 1–29. doi: 10.18637/jss.v042.i10
Lounsbury, M., Steele, C. W. J., Wang, M. S., and Toubiana, M. (2021). New
directions in the study of institutional logics: from tools to phenomena. Annu. Rev.
Sociol. 47, 261–280. doi: 10.1146/annurev-soc-090320-111734
Minnesota Journalism Center. (2025). As Newsrooms look to Innovate with AI,
Americans Remain Skeptical and Distrusting. Minneapolis, MN, United States:
Minnesota Journalism Center, Hubbard School of Journalism and Mass
Communication.
Newman, N., Fletcher, R., Eddy, K., Robertson, C. T., and Nielsen, R. K. (2024). The
Reuters Institute Report on Digital News 2024. Oxford, United Kingdom: Reuters
Institute for the Study of Journalism.
Palan, S., and Schitter, C. (2018). Prolific.ac, A participant database for online
experiments. J. Behav. Exp. Finance. 17, 22–27. doi: 10.1016/j.jbef.2017.12.004
Peer, E., Rothschild, D., Gordon, A., Evernden, Z., and Damer, E. (2022). Data quality
of platforms and panels for online behavioral research. Behav. Res. Methods. 54,
1643–1662. doi: 10.3758/s13428-021-01694-3
Talke, K., and Heidenreich, S. (2014). Overcoming biases in favour of
change: incorporating passive and active resistance to innovation into innovation
decision-making models. J. Prod. Innov. Manag. 31 (5), 894–907. doi: 10.1111/
jpim.12130
Thornton, P. H., Ocasio, W., and Lounsbury, M. (2012). The Institutional Logic
Perspective. Oxford, United Kingdom: Oxford University Press.
Thurman, N., Moeller, J., Helberger, N., and Trilling, D. (2019). My friends, editors,
algorithms, and I: examining audience attitudes to news selection. Digit. Journal. 7
(4), 447–469.
Thurman, N., Thäsler-Kordonouri, S., and Fletcher, R. (2025). AI Adoption by UK
Journalists and their Newsrooms: Surveying Applications, Approaches, and
Attitudes. Oxford: Reuters Institute for the Study of Journalism. doi: 10.60625/
risj-ea11-q402
Van Borkulo, C. D., Borsboom, D., Epskamp, S., Blanken, T. F., Boschloo, L.,
Schoevers, R. A., et al. (2014). A new method for constructing networks from
binary data. Sci. Rep. 4, 5918. doi: 10.1038/srep05918
Kubovics                                                                                                                                                               10.3389/fhumd.2026.1871733
Frontiers in Human Dynamics 08 frontiersin.org
