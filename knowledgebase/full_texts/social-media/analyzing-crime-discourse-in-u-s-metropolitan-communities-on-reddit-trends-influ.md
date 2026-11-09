---
title: 'Analyzing Crime Discourse in U.S. Metropolitan Communities on Reddit: Trends, Influences, and
  Insights'
url: https://arxiv.org/abs/2512.18227
category: social-media
subcategory: empirical
date: 2025-12
venue: ''
authors:
- Deepit Sapru
source: arxiv
pdf_url: https://arxiv.org/pdf/2512.18227
pages: 6
chars: 32235
fetched_at: '2026-11-08T13:08:32+00:00'
kb_version: 1
---

# Analyzing Crime Discourse in U.S. Metropolitan Communities on Reddit: Trends, Influences, and Insights

Analyzing Crime Discourse in U.S. Metropolitan
Communities on Reddit: Trends, Influences, and
Insights
Deepit Sapru
University of Illinois Urbana-Champaign
dsapru2@illinois.edu
Abstract—The relationship between crime and the media has
long been a focal point of academic research, with traditional
media playing a significant role in shaping public perceptions
of safety and community well-being. However, the advent of
social media has introduced a new dimension to this discourse,
offering unique platforms for user-driven discussions. Despite the
prominence of social media, research examining its impact on
crime-related discourse remains limited. This paper investigates
crime-related discussions across Reddit communities representing
384 Metropolitan Areas in the United States. By analyzing
user submissions, we identify key trends in crime discourse,
including the higher prevalence of such discussions in larger
metropolitan areas and communities with more liberal political
leanings. Interestingly, we find that reported crime rates do not
strongly influence the frequency or intensity of these discussions.
These findings provide novel insights into how social media
platforms, like Reddit, shape public narratives around crime,
highlighting the growing need to examine digital spaces as
influential mediators of public perception.
Keywords:Computational Social Science, Social Media Anal-
ysis, Spatio-Temporal Data Mining, Online Community Dy-
namics, Sentiment Analysis, Urban Informatics, Digital Soci-
ology, Statistical Discourse Analysis
I. INTRODUCTION
The intersection of crime and media representation has
constituted a significant area of scholarly inquiry for decades,
with traditional media outlets extensively studied for their
role in shaping public understanding of crime and safety
[1]. Television news, newspapers, and radio broadcasts have
historically functioned as primary sources of crime infor-
mation, often influencing community perceptions and policy
decisions [2]. However, the digital revolution has fundamen-
tally transformed media consumption patterns, with social
media platforms increasingly supplanting traditional media as
primary information sources [3].
Reddit, as a prominent social media platform, offers a
unique environment for examining crime discourse due to
its community-driven structure and geographical subreddits.
Unlike traditional media with centralized editorial control,
Reddit enables user-generated content that may more accu-
rately reflect grassroots concerns and discussions [4]. This
paper addresses a critical gap in the literature by systematically
analyzing crime-related discussions across 384 Metropolitan
Statistical Areas (MSAs) in the United States, examining how
these discussions correlate with demographic, political, and
crime statistics.
Our research employs a comprehensive data collection
methodology, gathering 161,166 posts from geographically-
defined subreddits over a two-month period. Through textual
analysis and statistical examination, we investigate whether
crime discourse on social media reflects actual crime rates
or is influenced by other socio-political factors. This approach
builds upon previous work examining crime discourse on plat-
forms like Twitter [5] while addressing the unique community
structure of Reddit.
The significance of this research extends beyond academic
interest, as understanding crime discourse patterns on social
media has implications for public policy, community engage-
ment, and media literacy. As social media platforms increas-
ingly shape public opinion [6], comprehending the dynamics
of crime-related discussions becomes essential for addressing
potential misinformation and understanding community con-
cerns.
This paper makes several key contributions: First, we
develop a robust methodology for identifying crime-related
content across diverse online communities. Second, we pro-
vide empirical evidence regarding the relationships between
crime discourse, population characteristics, political leanings,
and actual crime statistics. Third, we offer insights into the
behavioral patterns of users who frequently engage in crime-
related discussions. Finally, we contextualize our findings
within broader discussions about the role of social media in
shaping public perception of crime and safety.
II. BACKGROUND ANDLITERATUREREVIEW
A. Traditional Media and Crime Representation
Traditional media’s relationship with crime reporting has
been extensively documented in academic literature. Research
consistently demonstrates that media coverage often exagger-
ates crime prevalence and severity, contributing to what schol-
ars term ”crime fear” or ”mean world syndrome” [7]. Heath
and Gilbert [1] found that increased television news consump-
tion correlated with heightened distrust in local communities
and broader society, regardless of actual crime statistics.
The political implications of crime reporting have also
received significant attention. Liu et al. [8] demonstrated how
crime-focused campaign advertisements during the 2016 U.S.
arXiv:2512.18227v1  [cs.SI]  20 Dec 2025

presidential election influenced voting patterns, with viewers
who consumed more crime-related content tending to sup-
port conservative candidates. This relationship highlights how
crime discourse can transcend mere public safety concerns and
become embedded in political narratives.
Institutional responses to crime perception have similarly
been shaped by media representations. The implementation of
policies like ”stop and frisk” and the theoretical underpinnings
of ”Broken Windows” policing [9] emerged from particular
understandings of crime and community safety that were
often amplified through media channels. These policies, while
controversial, demonstrate how media-shaped perceptions can
translate into concrete social interventions [10].
B. Social Media Platforms and Crime Discourse
The transition from traditional to social media as primary
news sources has introduced new dynamics in crime discourse.
Walker and Masta [6] document that nearly half of Americans
now consume news through social media platforms, represent-
ing a fundamental shift in information consumption patterns.
This transition has occurred alongside the decline of traditional
print and broadcast media [3].
Research on crime discourse specific to social media plat-
forms remains relatively limited compared to traditional media
studies. Curiel et al. [5] examined crime-related tweets in Latin
American contexts, finding that Twitter discussions did not
correlate strongly with documented crime rates but effectively
captured community anxiety about crime. This discrepancy
between discussion frequency and actual crime statistics sug-
gests social media may amplify perceived rather than actual
crime threats.
Social media platforms also present unique challenges re-
garding misinformation and content moderation [11]. Unlike
traditional media with established editorial standards, social
media platforms often struggle with balancing free expression
and preventing the spread of false information [12]. This
challenge is particularly relevant for crime discourse, where
misinformation can have real-world consequences, as demon-
strated during events like the Boston Marathon bombing [13].
C. Reddit as a Research Platform
Reddit’s community-driven structure offers distinctive op-
portunities for analyzing geographically-based discussions.
The platform’s subreddit system allows for the examination
of location-specific conversations while maintaining the scale
necessary for robust statistical analysis [14]. Previous research
has examined various aspects of Reddit communities, includ-
ing political discourse [14], misinformation patterns [15], and
community migration behaviors [16].
The geographical nature of many Reddit communities, while
not enforced through technical means, often results in localized
discussions [17]. Blackburn et al. [18] found that even on
platforms without explicit geographical features, users tend
to form communities with local characteristics. This tendency
makes Reddit an valuable platform for examining how crime
discourse varies across different metropolitan contexts.
Content moderation on Reddit represents another important
consideration. Unlike centrally-moderated traditional media,
Reddit communities are typically moderated by volunteers
with varying approaches and standards [4]. This decentralized
moderation can lead to significant variation in discussion
quality and focus across different geographical subreddits,
potentially influencing crime discourse patterns.
III. METHODOLOGY ANDDATACOLLECTION
A. Data Acquisition Framework
Our research employed a comprehensive data collection
strategy focused on Reddit communities representing the 384
Metropolitan Statistical Areas (MSAs) in the United States
as defined by the U.S. Census Bureau [19]. We developed
a specialized crawler utilizing Reddit’s REST API [20] to
gather posts from each geographical subreddit between April
5, 2022, and May 31, 2022. The crawler operated on an hourly
schedule, ensuring comprehensive coverage while minimizing
API rate limit issues.
The data collection infrastructure employed a dual-database
approach for robustness and analytical flexibility. A Cock-
roachDB instance served as the system of record, storing raw
post data in JSON format, while an ElasticSearch database
facilitated efficient text analysis and keyword extraction. This
architecture allowed for both reliable data preservation and
performant analytical processing. The entire system operated
within Docker containers managed by Kubernetes, ensuring
high availability and automatic recovery from potential fail-
ures.
During the two-month collection period, we gathered
161,166 posts across all monitored subreddits. The distribution
of posts followed expected patterns relative to population
size, though with notable variations potentially attributable
to differing moderation policies and community engagement
levels across subreddits. This extensive dataset provided a
robust foundation for analyzing crime discourse patterns across
diverse metropolitan contexts.
B. Crime Discourse Identification
Identifying crime-related content required developing a pre-
cise methodology for classifying posts based on their textual
content. We compiled a comprehensive list of 124 crime-
related keywords derived from FBI Uniform Crime Reporting
categories [21], focusing particularly on violent crimes and
their common synonyms. The keyword list included terms
such as ”assault,” ”burglary,” ”shooting,” ”robbery,” and re-
lated variants, ensuring broad coverage of crime-related dis-
cussions while maintaining specificity.
We implemented a regular expression-based classification
system that analyzed both post titles and linked URLs for
crime-related keywords. Posts containing at least one keyword
from our predefined list were flagged as crime-related. To
validate this approach, we conducted manual analysis of a
400-post sample, achieving 91% classification accuracy. This
accuracy rate compares favorably to similar methodologies

employed in social media research [5], though we acknowl-
edge potential limitations regarding false negatives due to dog-
whistles or localized terminology.
The classification process identified 6,792 crime-related
posts from the total dataset, representing approximately 4.2%
of all collected content. This proportion varied significantly
across different metropolitan areas, with some communities
exhibiting crime discussion rates exceeding 15% while oth-
ers showed minimal crime-related content. These variations
formed the basis for our subsequent analysis of factors influ-
encing crime discourse prevalence.
C. Contextual Data Integration
To contextualize Reddit discourse patterns, we integrated
multiple external datasets characterizing each metropolitan
area. Population data derived from U.S. Census Bureau
statistics [22] enabled normalization of discussion volumes
and examination of size-related patterns. We categorized
MSAs into four population classes: large (over 1,000,000),
medium (500,000-1,000,000), small (200,000-500,000), and
very small (under 200,000), facilitating comparative analysis
across differently-sized communities.
Political context incorporated 2020 presidential election
results [23], specifically the percentage of voters supporting
Democratic candidates within each MSA. We established five
political categories based on voting patterns: very conserva-
tive (under 37.5% Democratic), conservative (37.5-47.5%),
moderate (47.5-52.5%), liberal (52.5-62.5%), and very liberal
(over 62.5% Democratic). This granular categorization allowed
for detailed examination of political correlations with crime
discourse.
Documented crime rates came from the FBI’s Uniform
Crime Reporting system [21], focusing specifically on violent
crime rates per 100,000 residents. We selected violent crime
statistics due to their more consistent reporting standards
across jurisdictions compared to property crimes. All crime
rate data underwent min-max normalization to enable com-
parative analysis with similarly normalized crime discussion
metrics.
IV. EMPIRICALANALYSIS ANDFINDINGS
A. Population Characteristics and Crime Discourse
Our analysis revealed significant relationships between
metropolitan area population size and crime discussion preva-
lence. Large metropolitan areas (population over 1,000,000)
exhibited substantially higher normalized crime discussion
scores (0.260) compared to medium (0.166), small (0.173), and
very small (0.196) areas. This pattern suggests that population
density and urban scale may amplify crime-related discussions
independent of actual crime statistics.
The distribution of crime discourse across population cate-
gories followed distinct patterns. While very small metropoli-
tan areas included both communities with exceptionally high
crime discussion rates and communities with no crime-related
TABLE I
METROPOLITANSTATISTICALAREAS WITHHIGHESTCRIMEDISCUSSION
RATES
Metropolitan
Statistical Area
% Crime Posts Crime Posts
Seattle-Tacoma-
Bellevue, W A
18.2 344
Anniston-
Oxford, AL
15.7 8
Lewiston-
Auburn, ME
15.4 14
Bay City, MI 14.0 7
Lewiston, ID-W A 13.0 7
Los Angeles-
Long Beach-
Anaheim, CA
12.0 257
Portland-
Vancouver-
Hillsboro, OR-
W A
11.4 287
Rocky Mount,
NC
11.3 7
New York-
Newark-Jersey
City, NY-NJ-PA
10.7 196
Flint, MI 9.7 10
posts, large metropolitan areas consistently maintained mod-
erate to high levels of crime discourse. This consistency indi-
cates that population size establishes a baseline level of crime
discussion, though other factors influence specific discussion
volumes.
Notably, the relationship between population size and crime
discussion intensity was not linear. Medium-sized metropolitan
areas actually showed slightly lower average crime discussion
than small areas, suggesting potential threshold effects where
discussion patterns shift at specific population levels. This
nonlinear relationship underscores the complexity of factors
influencing online crime discourse and cautions against sim-
plistic population-based predictions.
Population Size
Crime Discussion
VS S M L
Crime Discussion by Population Category
Fig. 1. Relationship between population size categories and crime discussion
intensity. VS=Very Small, S=Small, M=Medium, L=Large metropolitan areas.
B. Political Correlations with Crime Discourse
Political characteristics emerged as strong predictors of
crime discussion prevalence across metropolitan areas. Our

analysis demonstrated a clear positive relationship between lib-
eral voting patterns and crime discourse intensity. Very liberal
metropolitan areas exhibited the highest average normalized
crime discussion scores (0.274), followed by moderate (0.207),
liberal (0.201), conservative (0.179), and very conservative
(0.170) areas.
This political gradient remained evident even when control-
ling for population size. Among large and medium metropoli-
tan areas, those with higher proportions of Democratic voters
consistently showed elevated crime discussion rates. The most
conservative large metropolitan area in our dataset, Provo-
Orem, Utah, recorded no crime-related posts during the study
period, while strongly liberal areas like Seattle, Portland, and
New York City exhibited crime discussion rates exceeding
10%.
The divergence between crime discussion and documented
crime rates across political categories was particularly note-
worthy. Very liberal metropolitan areas, while showing the
highest crime discussion levels, actually had lower average
documented violent crime rates than conservative areas. This
discrepancy suggests that crime discourse on social media
reflects factors beyond objective crime statistics, potentially
including political identity, media consumption patterns, or
community values regarding public safety discussions.
C. Documented Crime Rates and Online Discourse
Contrary to intuitive expectations, we found no strong
correlation between documented violent crime rates and the
prevalence of crime-related discussions on Reddit. Metropoli-
tan areas with the highest violent crime rates, including
Birmingham-Hoover, Alabama (1,397.2 per 100,000) and
Farmington, New Mexico (1,199.8 per 100,000), showed only
moderate crime discussion rates of 2.52% and 1.61% respec-
tively.
The disconnect between actual crime statistics and on-
line discussion became particularly evident when examining
normalized difference scores between crime discussion and
documented crime rates. Metropolitan areas with the largest
positive differences (indicating disproportionately high crime
discussion relative to actual crime) were predominantly large,
liberal areas in coastal regions, while areas with large negative
differences (high crime but low discussion) tended to be
smaller, conservative communities in the South and Midwest.
This misalignment between objective crime indicators and
subjective online discussions has important implications for
public understanding of crime patterns. If social media dis-
course disproportionately represents certain types of commu-
nities or perspectives, it may distort public perception of actual
crime risks and appropriate policy responses. This potential
distortion underscores the importance of critical media literacy
regarding crime-related social media content.
V. USERBEHAVIOR ANDSENTIMENTANALYSIS
A. Sentiment Patterns in Crime Discourse
Our analysis of user sentiment revealed distinct differences
between individuals who frequently post crime-related content
TABLE II
METROPOLITANAREAS WITHHIGHESTDOCUMENTEDVIOLENTCRIME
RATES
Metropolitan Statistical Area Crime Rate % Crime Discussion
Birmingham-Hoover, AL 1,397.2 2.52
Farmington, NM 1,199.8 1.61
Anchorage, AK 1,194.6 2.36
Kansas City, MO-KS 1,159.4 3.16
Memphis, TN-MS-AR 1,120.5 3.43
Winston-Salem, NC 1,073.6 2.32
Albuquerque, NM 1,043.4 4.53
Danville, IL 935.7 0.00
Pine Bluff, AR 895.4 12.50
Odessa, TX 881.8 4.30
and those who do not. Focusing on the r/nyc subreddit as a
case study, we examined 1,197 unique posters, identifying 134
users who had posted about crime at least once. Sentiment
analysis of these users’ comments and posts, both within and
outside the New York City community, showed consistently
more negative sentiment among crime posters.
Crime-posting users exhibited average sentiment polarity
scores of -0.07 both within r/nyc and in their broader Reddit
activity. In contrast, non-crime posters showed positive average
sentiment scores of 0.09 within the community and 0.10
elsewhere on the platform. This sentiment gap suggests that
users who frequently engage with crime content may have
generally more negative outlooks that extend beyond specific
crime-related discussions.
The consistency of sentiment patterns across different sub-
reddits for crime-posting users indicates that negative expres-
sion may represent a stable characteristic of these individuals’
online behavior rather than a situation-specific response to
local crime conditions. This finding aligns with research
suggesting that certain personality traits or worldviews may
predispose individuals to focus on negative societal aspects
[24].
B. Community Engagement Patterns
Analysis of user engagement across different subreddits
revealed distinctive patterns between crime-posting and non-
crime-posting users. Using the Jaccard Index to measure
community overlap [25], we found that crime posters showed
strong connections to specific crime-focused communities like
CrimeInNYC and NYStateOfMind, with overlap scores of
0.83 and 0.12 respectively.
Non-crime posters demonstrated stronger connections to
location-specific hobby and interest communities, including
nycrail (0.81), RunNYC (0.48), and various neighborhood sub-
reddits. This pattern suggests that while crime posters maintain
some local engagement, their community connections are more
diffuse than those of non-crime posters, who show tighter
integration with geographically-based interest communities.
The political subreddit engagement patterns further dis-
tinguished these user groups. Crime posters showed higher
engagement with conservative-leaning communities like Lock-
downSkepticism and Conservative, while non-crime posters

more frequently participated in moderate and liberal political
spaces like neoliberal and V oteDEM. This political divergence
occurred despite New York City’s overall liberal orientation,
suggesting that crime posters may represent a politically
distinct subgroup within their communities.
Crime Posters Non-Crime Posters
Conservative
Communities
Local Hobby
Communities
Distinct Community Engagement Patterns
Fig. 2. Visualization of distinct community engagement patterns between
crime-posting and non-crime-posting users
VI. DISCUSSION ANDIMPLICATIONS
A. Interpreting the Crime Discourse Landscape
Our findings present a complex picture of crime discourse
on social media, challenging several common assumptions
about the relationship between online discussions and real-
world conditions. The strong correlation between liberal polit-
ical leanings and crime discussion prevalence contradicts nar-
ratives that conservative communities focus more heavily on
crime issues. Instead, our results suggest that crime discourse
may serve different social or political functions in different
community contexts.
The disconnect between documented crime rates and dis-
cussion frequency raises important questions about what drives
online crime conversations. If these discussions do not primar-
ily reflect objective crime conditions, they may instead express
broader community anxieties, political positions, or responses
to media narratives. This interpretation aligns with research
suggesting that social media often amplifies perceived risks
rather than actual threats [5].
The demographic patterns we observed—specifically the
elevated crime discussion in larger metropolitan areas—may
reflect genuine differences in urban experience, including
higher population density, greater anonymity, and more fre-
quent stranger interactions. However, the magnitude of the
difference suggests that additional factors, such as media
ecosystem differences or community norms around public
discussion, also play significant roles.
B. Practical Implications and Applications
Our research has several practical implications for com-
munity leaders, law enforcement agencies, and media or-
ganizations. First, the demonstrated misalignment between
online crime discourse and actual crime statistics highlights
the potential for social media to distort public understanding
of safety issues. Organizations communicating about crime
should recognize this potential distortion and consider strate-
gies to provide context and accurate statistics.
Second, the political dimensions of crime discourse suggest
that crime discussions on social media may function partially
as expressions of political identity rather than straightforward
reporting of community conditions. Recognizing this dimen-
sion could help community leaders interpret crime-related so-
cial media activity more accurately and respond appropriately
to constituent concerns.
Third, the behavioral patterns of frequent crime
posters—including their more negative general sentiment and
distinct community affiliations—suggest that crime discourse
may be driven by a subset of community members with
particular characteristics. Understanding these patterns could
inform more effective community engagement strategies and
help identify potential misinformation sources.
C. Limitations and Future Research Directions
While our study provides comprehensive analysis of crime
discourse patterns, several limitations warrant acknowledg-
ment. Our keyword-based classification approach, while vali-
dated through manual review, may miss nuanced crime discus-
sions or local terminology. Future research could incorporate
more advanced natural language processing techniques to
capture broader semantic patterns.
The temporal scope of our data collection—approximately
two months—provides a snapshot of discussion patterns but
may not capture seasonal variations or responses to specific
events. Longitudinal studies tracking crime discourse over
extended periods could reveal how these patterns evolve in
response to real-world developments and media cycles.
Our focus on Reddit, while providing valuable insights into
one prominent platform, limits generalizability to other social
media environments with different user demographics and
communication norms. Comparative studies across multiple
platforms—such as Facebook, Nextdoor, and Twitter—could
illuminate platform-specific dynamics in crime discourse.
Future research could also explore more nuanced aspects of
crime discourse, including the types of crimes most frequently
discussed, the framing of these discussions, and their rela-
tionship to local media coverage. Additionally, investigating
intervention strategies to ensure accurate crime perception in
social media-saturated environments represents an important
direction for applied research.
VII. CONCLUSION
This research provides systematic examination of crime-
related discussions across U.S. metropolitan areas on Reddit,
revealing distinct patterns that challenge simplistic assump-
tions about crime discourse. Our findings demonstrate that
crime discussion prevalence correlates strongly with popula-
tion size and political leanings but shows little relationship
to documented crime rates. These patterns suggest that social
media crime discourse serves complex social functions beyond
simple information sharing about local safety conditions.

The behavioral characteristics of frequent crime
posters—including generally negative sentiment and distinct
community affiliations—further complicate the interpretation
of crime-related social media content. Rather than representing
broad community concerns, crime discourse may often reflect
the perspectives and motivations of specific subgroups within
communities.
As social media platforms continue to evolve as primary
spaces for public discourse, understanding the dynamics of
crime-related discussions becomes increasingly important for
accurate public perception and effective policy responses. Our
research contributes to this understanding by documenting
systematic patterns in how crime is discussed across different
community contexts and identifying factors that shape these
discussion patterns.
Future research should build upon these findings to de-
velop more sophisticated models of crime discourse dynamics,
examine cross-platform patterns, and explore strategies for
ensuring that online discussions accurately reflect community
safety conditions. Through continued investigation of these
issues, researchers can help ensure that social media serves
as a constructive rather than distorting influence on public
understanding of crime and safety.
REFERENCES
[1] L. Heath and K. Gilbert, “Mass media and fear of crime,”American
Behavioral Scientist, vol. 39, no. 4, pp. 379–386, 1996.
[2] V . F. Sacco, “Media constructions of crime,”The Annals of the American
Academy of Political and Social Science, vol. 539, no. 1, pp. 141–154,
1995.
[3] R. K. Nielsen and R. Sambrook, “What is happening to television news,”
Digital News Project, Reuters Institute, 2016.
[4] S. Jhaver, A. Bruckman, and E. Gilbert, “Does transparency in modera-
tion really matter? user behavior after content removal explanations on
reddit,” inProceedings of the ACM on Human-Computer Interaction,
vol. 3, no. CSCW, 2019, pp. 1–27.
[5] R. P. Curiel, S. Cresci, C. I. Muntean, and S. R. Bishop, “Crime and
its fear in social media,”Palgrave Communications, vol. 6, no. 1, pp.
1–10, 2020.
[6] M. Walker and K. E. Masta, “News consumption across social media in
2021,”Pew Research Center, 2021.
[7] J. Shanahan and M. Morgan,Television and its viewers: Cultivation
theory and research. Cambridge University Press, 1999.
[8] J. Liu, E. F. Fowler, L. Baum, and S. E. Gollust, “Campaign advertising
and the cultivation of crime worry: Testing relationships with two large
datasets from the 2016 us election cycle,”The International Journal of
Press/Politics, p. 19401612211020929, 2021.
[9] J. Q. Wilson and G. L. Kelling, “Broken windows,”The Atlantic
Monthly, vol. 249, no. 3, pp. 29–38, 1982.
[10] T. L. Meares, “The law and social science of stop and frisk,”Annual
Review of Law and Social Science, vol. 10, pp. 335–352, 2014.
[11] S. Phadke and T. Mitra, “Many faced hate: A cross platform study
of content framing and information sharing by online hate groups,”
inProceedings of the 2020 CHI Conference on Human Factors in
Computing Systems, 2020, pp. 1–13.
[12] S. Zannettou, ““i won the election!”: An empirical analysis of soft
moderation interventions on twitter,” inProceedings of the International
AAAI Conference on Web and Social Media, vol. 15, 2021, pp. 865–876.
[13] L. Potts and A. Harrison, “Interfaces as rhetorical constructions: Reddit
and 4chan during the boston marathon bombings,” inProceedings of the
31st ACM international conference on Design of communication, 2013,
pp. 143–150.
[14] A. Rajadesingan, C. Budak, and P. Resnick, “Political discussion is
abundant in non-political subreddits (and less toxic),” inProceedings of
the International AAAI Conference on Web and Social Media, vol. 15,
2021, pp. 484–494.
[15] M. H. Ribeiro, S. Jhaver, S. Zannettou, J. Blackburn, E. De Cristofaro,
G. Stringhini, and R. West, “Do platform migrations compromise content
moderation? evidence from r/the donald and r/incels,”Proceedings of the
ACM on Human-Computer Interaction, vol. 5, no. CSCW2, pp. 1–24,
2021.
[16] C. Davies, S. Jhaver, J. An, K. Gummadi, and S. Zannettou, “Multi-scale
user migration on reddit,”Workshop on Cyber Social Threats at the 15th
International AAAI Conference on Web and Social Media (ICWSM),
2021.
[17] S. Scellato, C. Mascolo, M. Musolesi, and V . Latora, “Distance matters:
Geo-social metrics for online social networks,” inProceedings of the
3rd conference on Online social networks, 2010, pp. 1–6.
[18] J. Blackburn, H. Kwaket al., “Cheating in online games: A social
network perspective,”ACM Transactions on Internet Technology (TOIT),
vol. 13, no. 3, pp. 1–25, 2014.
[19] U.S. Census Bureau, “About metropolitan and micropolitan areas,” https:
//www.census.gov/programs-surveys/metro-micro/about.html, 2020.
[20] Reddit, “Reddit api documentation,” https://www.reddit.com/dev/api/,
2022.
[21] Federal Bureau of Investigation, “Uniform crime reporting,” https://
www.fbi.gov/services/cjis/ucr, 2020.
[22] U.S. Census Bureau, “Age and sex,” https://data.census.gov/cedsci/table?
q=age&tid=ACSST5Y2020.S0101, 2020.
[23] Associated Press, “United states election results,” https://elections.ap.
org/dailykos/results/2020-11-03/state/US, 2020.
[24] W. Medhat, A. Hassan, and H. Korashy, “Sentiment analysis algorithms
and applications: A survey,”Ain Shams Engineering Journal, vol. 5,
no. 4, pp. 1093–1113, 2014.
[25] S. Fletcher and M. Z. Islam, “Comparing sets of patterns with the jaccard
index,”Australasian Journal of Information Systems, vol. 22, 2018.
