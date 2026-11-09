---
title: 'A literature review on opinion leaders detection in social networks: approaches, methods and metrics'
url: https://doi.org/10.1007/s10791-026-10414-4
category: survey
subcategory: review
date: 2026-08
venue: Discover Computing
authors:
- Malek Chebil
- Mohamed Anis Bach Tobji
- Rim Jallouli
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s10791-026-10414-4.pdf
pages: 34
chars: 128544
fetched_at: '2026-11-08T19:42:06+00:00'
kb_version: 1
---

# A literature review on opinion leaders detection in social networks: approaches, methods and metrics

REVIEW Open Access
Discover ComputingChebil et al. Discover Computing          (2026) 29:513
https://doi.org/10.1007/s10791-026-10414-4
A literature review on opinion leaders detection
in social networks: approaches, methods
and metrics
Malek Chebil1*, Mohamed Anis Bach Tobji1,2 and Rim Jallouli3
*Correspondence:
Malek Chebil
malek.chebil@esen.tn
1Université de Tunis, ISG de Tunis,
LARODEC, Tunis, Tunisia
2Univ. Manouba, ESEN, Manouba,
Tunisia
3Univ. Manouba, ESEN, LIGUE,
Manouba, Tunisia
© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article
are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
Abstract A social network serves as a dynamic arena where online users actively
participate in exchanges involving the sharing of opinions and ideas. Amidst this digital
landscape, certain individuals stand out as opinion leaders, wielding the power to
shape the perspectives of their peers. Opinion leaders are active in diverse domains
such as marketing, advertising, politics, health, finance and investment, education
and scientific research, etc. However, Opinion Leaders Detection (OLD) faces several
challenges, including data collection and data quality, the diversity of social platforms,
the network complexity, the dynamic nature of social networks, the contextualization
of opinion leaders, and the importance of ethical concerns. These challenges have
led to a rich and scattered literature, with a wide range of methods and techniques
developed to address OLD challenges. This paper reviews established methods in OLD,
categorizing them based on criteria such as social network platforms, approaches,
methods, techniques, and evaluation metrics. It highlights the benefits and limitations
of each approach and method, aiming to provide researchers with a comprehensive
overview and suggesting ways to overcome the limitations of conventional methods.
The paper also discusses current literature and identifies future research directions to
address existing gaps.
Highlights
 • Provides a clear definition of opinion leaders and explore their applications
indiverse domains.
 • Conducts a comparative analysis of the approaches and methods used in
existing literature for identifying opinion leaders.
 • Outlines the evaluation metrics used to assess the effectiveness of opinion
leaders detection methods.
 • A comparative table is provided, outlining the analysis and classification
ofrelated works based on their approaches, methods, benefits, and limitations.
 • Discusses emerging trends and potential future directions in opinion leaders
detection research.
Keywords Opinion Leaders Detection, Social network, Methods, Approaches,
Evaluation metrics, Taxonomy

Page 2 of 34
Chebil et al. Discover Computing          (2026) 29:513
1 Introduction
In contemporary society, social networks serve as indispensable communication plat -
forms, fostering interactions among individuals. Within these interactions, people shape
and influence others’ opinions. Those who possess the remarkable ability to sway and
mold the perspectives of their peers are recognized as opinion leaders. The task of iden -
tifying these influential individuals is encapsulated in Opinion Leaders Detection (OLD).
The paramount importance of pinpointing opinion leaders becomes evident when con -
sidering their potent influence in catalyzing trends in business, marketing, and political
movements and raising awareness of public health or environmental issues. This leads
to the critical questions of who these opinion leaders are and how they can be identified
within a social network?
In recent years, substantial efforts have been dedicated to proposing compelling and
precise solutions to address this challenge. Consequently, a deeper understanding of
the constraints inherent in existing approaches is needed to identify and model opinion
leaders to ensure the potential prediction of future information dissemination patterns.
While the literature has witnessed some attempts to provide persuasive and precise solu-
tions to this problem, a limited number of studies offer an inclusive overview, regrouping
and classifying these methods based on their approaches, measures, platform usage, and
evaluation metrics. Evaluating the relevance of opinion leaders is a challenging task due
to the lack of standardized metrics and methods for their identification. Hence, there is a
growing need for a comprehensive understanding of the limitations of existing methods,
in order to facilitate the development of new methods that address these limitations and
build on previous findings.
Existing surveys on Opinion Leaders Detection (OLD) provide valuable classifications
of methods; however, they often lack a clear separation between high-level analytical
perspectives and underlying methodological implementations, and may present over -
lapping or inconsistent categorizations. To address these limitations, this study provides
a novel and structured taxonomy that clearly distinguishes between interaction-based,
content-based, and hybrid approaches, as well as their corresponding methodological
techniques, including graph-based models, PageRank-based methods, diffusion-based
models, statistical and stochastic methods, machine learning techniques, deep learn -
ing methods, and lexicon-based methods. In addition, unlike previous surveys, this
Graphical Abstract

Page 3 of 34
Chebil et al. Discover Computing          (2026) 29:513
review offers a unified comparative analysis of existing methods in terms of their gen -
eral characteristics, strengths, and limitations, together with a systematic classification
of evaluation metrics used to assess and compare OLD techniques and frameworks. This
dual-level organization (approaches vs. methods) represents the main novelty of this
study and enables a more consistent interpretation and comparison of existing work.
The aim of this paper is to offer a comprehensive understanding of the approaches,
the methods and metrics used in OLD in social networks. By thoroughly reviewing the
literature, we aim to explore various facets, including the conceptualization of opinion
leaders, the range of their applicability, research approaches, and the diverse methods
and techniques employed in OLD. Thus, the paper categorizes the existing contributions
based on specific criteria such as social network platforms, approaches, methods, tech -
niques and evaluation metrics emphasizing the benefits and limitations of each approach
and method. This categorization is intended to provide valuable insights for research -
ers aiming to develop innovative techniques, building upon the limitations of exist -
ing approaches and drawing inspiration from previous research endeavors. Ultimately,
the paper aims to contribute to the advancement of OLD techniques and guide future
research in this evolving domain. In addition, the methodology employed in this study
involves the identification of literature related to opinion leaders through a systematic
search across journal and conference papers in diverse academic databases and search
engines. Subsequently, a thorough assessment of the quality of the collected papers was
conducted to determine their alignment with the scope of the survey.
The paper is organized as follows. Section 2 delineates the scope of the literature
review on OLD. Section 3 defines opinion leaders, describes their roles, and highlights
their influence across various domains. Section 4 details the methodology adopted for
the systematic literature review. Section 5 presents a taxonomy of existing methods and
approaches for OLD. Section 6 introduces our proposed classification framework for
OLD approaches. Section 7 provides an in-depth review of the methods employed in
OLD, synthesizing insights from prior studies and systematically describing the associ -
ated techniques. Section 8 outlines the evaluation metrics used in current OLD research.
Section 9 discusses the advantages and limitations of existing approaches and methods,
and identifies key challenges and future research directions. Finally, Section 10 presents
the conclusion of the study.
2 Scope of the literature review
Identifying opinion leaders on social networks poses numerous challenges, including
data collection and quality, privacy concerns, the diversity of platforms with their spe -
cific characteristics, the dynamic and complex nature of social networks, and the need
to consider contextual information for identifying expert leaders based on their content,
as well as ethical considerations. These challenges have led to a large but fragmented
literature, encompassing a variety of methods and techniques. Despite these advances,
few review studies provide a structured synthesis that categorizes and compares existing
approaches based on their methodological principles, the indicators used, the platforms
analyzed, and the evaluation criteria applied. This lack of synthesis hinders the consoli -
dation of knowledge in the field.

Page 4 of 34
Chebil et al. Discover Computing          (2026) 29:513
3 Opinion leaders: definition and application domains
Across different contexts and studies, various definitions have been proposed to char -
acterize opinion leaders. Putnam et al. [ 1] conceptualized opinion leaders through three
facets: identification, network relationships, and communication channels. They were
characterized as individuals who reached less active populations through social influ -
ence, operated within interconnected networks to spread and coordinate ideas, and
preferred impersonal and technically accurate information sources. Moreover, Zatwar -
nicka-Madura et al. [ 2] added that opinion leaders often held prominent organizational
positions, were characterized by high self-esteem, openness to innovation, and strong
professional engagement, and possessed broad expertise and competence that strength -
ened their influence within social networks. Additionally, Jain and Katarya [ 3] described
opinion leaders as observable to peripheral communication in all forms, more sophis -
ticated and deep thinkers, with higher social status and higher competence level, and
more advanced and groundbreakers, occupying central positions in communication net-
works and influencing others who imitate their innovative actions, while also exerting
considerable influence on the behavior and decision-making of others across domains
such as education, politics, and social issues. According to Rogers et al. [ 4], an opinion
leader is an individual with a higher socioeconomic status than their followers, primar -
ily due to extensive exposure to mass media and strong connections with change agents.
This establishes them as influential social participants. Commonly cited characteristics
of an opinion leader include being likable, trustworthy, educationally influential, and
possessing self-confidence [ 5, 6]. Furthermore, Freeman et al. [ 7] described an opinion
leader as someone who has the power to shape the actions of people around them for a
particular purpose. Their views grab attention, spark curiosity about a product or ser -
vice, and occasionally persuade others to make a purchase.
Opinion leaders are highly effective at spreading information, making their identifi -
cation crucial in many fields. In the field of marketing and business, companies have a
growing interest in leveraging opinion leaders to increase their profits through strategic
advertising [8–10]. In addition, in public health, opinion leaders emerge as instrumental
in championing evidence-based practices and expediting the diffusion of health inno -
vations, as evidenced by studies reported in [ 5, 11, 12]. Moreover, the fields of sociol -
ogy and psychology benefit from the illuminating work of Cialdini [ 13] and the dynamic
modeling by Tucci et al. [ 14], shedding light on how opinion leaders manipulate per -
spectives and contribute to collective behavior within intricate social systems. Addition -
ally, in education, Koeslag-Kreunen et al. [ 15] delved into the impact of opinion leaders,
commonly known as “Teacher Leaders” , emphasizing their multifaceted roles in elevat -
ing teaching quality and shaping student perspectives. Turning to the political landscape,
opinion leaders emerge as pivotal figures or entities wielding significant influence within
their communities, actively shaping and disseminating specific political trends [ 16–18].
In agriculture, opinion leaders leverage their high social status and extensive networks
to facilitate and accelerate the acceptance of new innovations. According to Hameed et
al. [ 19], these individuals serve as intermediaries between the community and exten -
sion services, using their interpersonal skills and knowledge to effectively advocate for
agricultural progress. Moreover, in recommender systems, opinion leaders are suggested
as a solution to the cold start problem, helping recommend items that best match user
preferences and needs [8].

Page 5 of 34
Chebil et al. Discover Computing          (2026) 29:513
The multidimensional impact of opinion leaders across marketing, business, health,
sociology, education, politics and agriculture underscores their pervasive significance in
shaping societal dynamics and influencing the decision-making process.
4 Methodology for the literature review
A comprehensive literature review on OLD in social networks was carried out within the
scope of this study. The search was conducted using academic databases such as Elsevier,
Springer, ScienceDirect, Web of Science, Scopus, IEEE, and ACM. Relevant studies were
identified through a set of carefully selected keywords related to the research context,
including: "opinion leaders", "opinion leaders detection", "identifying opinion leaders",
"social networks", "social media", "approaches", "methods", "techniques", "algorithms",
and "metrics". The terms were applied in combination to expand the search scope. A
thorough assessment was then conducted to evaluate the quality and relevance of the
collected articles, excluding those deemed irrelevant. A total of 200 articles were initially
identified through the search. After removing duplicates, 150 articles remained. Fol -
lowing title and abstract screening, 55 articles were excluded as they were out of scope,
leaving 95 for full-text review. A further 35 articles were excluded during full-text assess-
ment, resulting in a final corpus of 60 articles. Only papers published in English were
retained. These 60 articles were reviewed and formed the basis of this study, covering
publications up to March 2026. Based on this review, a taxonomy was proposed to clas -
sify existing approaches, methods, and evaluation metrics for OLD, with a discussion of
their strengths, limitations, gaps, and future research directions. Additionally, 26 papers
from this corpus were selected for detailed analysis and are summarized in Table 4. Fig-
ure 1 illustrates the methodology adopted for the literature review.
5 Taxonomy of methods and approaches for opinion leaders detection
In the literature, the terms "method" and "approach" for detecting opinion leaders in
social networks are often used interchangeably: some authors refer to the same con -
cept as a method, while others call it an approach. Moreover, very few literature review
articles systematically present and classify OLD methods while clearly distinguishing
between conceptual strategies and computational implementations. The majority of pub-
lications in this field are research articles introducing new techniques or frameworks,
while only a limited number of review-type studies propose classification schemes and
taxonomies. Table 1 provides an overview of existing classifications reported in the
literature.
Based on Table 1, existing taxonomies are often heterogeneous and do not clearly
separate high-level conceptual strategies from specific computational techniques. To
address this limitation, we explicitly distinguish between approaches and methods:
approaches refer to high-level strategies for identifying opinion leaders in online social
networks, while methods correspond to the specific computational techniques used to
operationalize these strategies. Accordingly, the literature can be organized into three
main conceptual approaches: interaction-based, content-based, and hybrid approaches
that combine both types of features. These conceptual categories provide a structured
foundation for the detailed computational methods presented in the following section.

Page 6 of 34
Chebil et al. Discover Computing          (2026) 29:513
6 Opinion leaders detection approaches
In this study, approaches for detecting opinion leaders in OSNs are classified into three
categories: interaction-based, content-based, and hybrid approaches. These approaches
represent high-level conceptual strategies that define how influence is modeled in social
networks, rather than specific computational implementations.
6.1 Interaction-based approach
The interaction-based approach focuses on how users engage with one another within a
network. It examines the network structure, the temporal dynamics of interactions, and
user behavior. Furthermore, attributes such as the number of followers or following rela-
tionships are often used as indicators of the intensity of social interactions.
Network structure analysis examines the topology of a social network, focusing on
user connections via edges. It analyzes node positions and relationships to identify the
most influential users [20]. The network structure also determines centrality, measuring
a user’s influence based on their position, and incorporates community measures, which
assess the density of connections within groups. Communities, defined as subnetworks
Fig. 1 Methodology for the literature review

Page 7 of 34
Chebil et al. Discover Computing          (2026) 29:513
Ref
and
years
Type Taxonomy Issues, gaps or suggestions identified by authors
[20]
2017
Review Measures based on
network structure,
methods based on
interaction, methods
based on content
mining, and methods
based on content
and interaction.
- Leadership definitions vary by context, complicating universal
detection.
- Key features may be missing or unclear in available data.
- Structural, interaction, and content-based methods have limita-
tions; hybrid approaches are often required.
- Effective detection should integrate network structure, diffu-
sion, interactions, and content.
- Comparisons are difficult due to diverse datasets and inconsis-
tent evaluation metrics.
[21]
2018
Review Self-assessment
method, assessment
by other methods,
and algorithmic as-
sessment method.
- Traditional methods (self-assessment and assessment by others)
often produce inconsistent results, while algorithmic assessment
identifies different types of opinion leaders with different criteria.
- Traditional and algorithmic methods rarely measure opinion
leaders as information transmitters, focusing mostly on content
sharing and persuasion.
- Algorithmic assessment tracks influence via activity, contacts,
feedback, and sharing; differentiating by function, reach, or topic
can clarify influence.
- Few studies compare different methods of identifying opinion
leaders, leaving unclear which criteria or methods are most
reliable.
[22]
2019
Review Descriptive ap-
proaches, statisti-
cal and stochastic
methods, diffusion
process based ap-
proaches, topological
based methods, data
mining and learning
methods, and hybrid
content mining
approaches.
- Each approach has strengths but faces scalability and high
computational costs in large networks.
- The lack of labeled datasets limits the performance of machine
learning methods.
- No single method outperforms in all situation; better bench-
marks are needed.
- Topological methods often overlook trust, making them vulner-
able to manipulation by fake leaders.
- Topological methods need better integration with text and
sentiment for improved detection.
- Hybrid approaches are recommended.
- More research is needed on trust models and differentiating
trolls from real leaders.
[23]
2021
Research Diffusion-based
approaches, graph-
based approaches,
statistical and sto-
chastic approaches,
PageRank-based
approaches, and
machine learning
approaches.
- There is no common way to evaluate opinion leaders, so results
from different methods cannot be reliably compared.
- Graph-based measures are insufficient on their own and require
complementary behavioral and content features.
- Current models rely on static networks and need adaptation to
dynamic, real-time influence diffusion.
[24]
2022
Review Network structure-
based measures,
interaction-based
methods, content
mining-based meth-
ods, and content and
interaction-based
methods.
- Leader definition varies across contexts, making universal
detection methods challenging.
- Integrating structural, personal, and content features into OLD
remains difficult.
- No comprehensive framework exists for OLD across different
environments.
- Hybrid models combining multiple approaches could improve
OLD accuracy.
- Limited research on scalable methods for OLD in large
networks.
Table 1 Taxonomy of methods and approaches for OLD

Page 8 of 34
Chebil et al. Discover Computing          (2026) 29:513
Ref
and
years
Type Taxonomy Issues, gaps or suggestions identified by authors
[25]
2022
Review Measures based on
network structure,
methods based on
interaction, methods
based on content
mining, and methods
based on content
and interaction.
- Limited use of real social-media data, with reliance on surveys
and clustering.
- Lack of analysis of posts and interactions, especially opinion
leader–follower dynamics.
- Need for integrated methods combining content features and
interaction patterns.
- Potential for wider application in medical, political, and market-
ing domains.
[26]
2022
Review Diffusion based
approaches, graph-
based approaches,
statistical and sto-
chastic approaches,
PageRank based
approaches, and
machine learning
approaches.
- OLD methods depend on dataset size and problem context.
- No method performs reliably or generalizes across different
social-media environments.
- Further research is needed to develop robust and adaptable
OLD frameworks.
[27]
2023
Research Methods based
on interactions,
methods based on
content, methods
combine interac-
tion and content-
based, and methods
based on sentiment
analysis.
- Interaction-based methods do not handle dynamic networks
well.
- Content-based methods often ignore context of posts.
- Sentiment analysis alone may miss subtle opinions.
- Evaluation of methods is inconsistent, making comparisons
difficult.
- Real-time detection and multimodal data are needed for
improvement.
[28]
2024
Research Singular approaches
(questionnaire,
graph analysis) and
hybrid approaches
(graph + content
analysis, graph +
questionnaire).
- Graph-based methods are time-consuming, need large datas-
ets, and fail when network data is missing.
- Hybrid approaches combining graph analysis with content or
surveys improve detection and engagement assessment.
- OLD at firm level may not capture broader influence on supply
chains and collaboration.
- Effectiveness depends on context, dataset size, and method
choice; no single method fits all scenarios.
[29]
2024
Review Descriptive ap-
proaches, topologi-
cal-based methods,
lexicon-based ap-
proach, sentiment
analysis, data mining
and machine learn-
ing approaches,
hybrid approaches,
and maximization
technique.
- Limited adaptivity in capturing the evolving nature of influence
in dynamic social networks.
- Overemphasis on global influencers, neglecting detection of
local or community-level leaders.
- Heavy reliance on structural or content-based features without
integrating a multi-dimensional view.
- Challenges in scalability and practical deployment due to high
data and computational needs.
- Recommendation to develop hybrid, dynamic, scalable frame-
works focused on local detection with standardized evaluation
benchmarks.
[30]
2026
Research Trust-based, opinion
analysis-based,
propagation-based,
and structure-based
and learning-based
approaches.
- Trust-based methods are often too static and ignore semantic
and temporal context.
- Opinion-analysis methods can be domain-specific and may not
generalize well.
- Propagation-based methods are often computationally expen-
sive and rely on strong diffusion assumptions.
- Structure/learning-based methods may focus too much on
network popularity and not enough on true opinion leadership.
- Suggestion to combine semantic, behavioral, and topological
features in a hybrid model to better detect real opinion leaders.
Table 1 (continued)

Page 9 of 34
Chebil et al. Discover Computing          (2026) 29:513
with high internal connectivity among users sharing common traits, play a crucial role
in opinion leadership [ 31–33]. By considering user interdependencies, researchers can
identify key opinion leaders exerting significant influence. Moreover, temporal inter -
action analysis examines how user influence evolves over time by tracking interaction
patterns. It considers the timing and sequence of interactions between users, enabling
a flexible analysis of influence dynamics. However, user interaction behaviors describe
how individuals engage with content through actions such as likes, shares, and com -
ments. Likes increase content visibility and engagement, directly affecting user decisions
[34]. Shares expand reach, reflecting the perceived value of content [ 35], while com -
ments indicate deeper engagement, though their influence on decisions may be lower
[34]. Studying these behaviors helps identify opinion leaders based on their engagement
levels and the impact of their interactions on others.
6.2 Content-based approach
The content-based approach distinguishes between two complementary types of analy -
sis. Content metadata analysis examines measurable attributes associated with posts or
user accounts, such as profile descriptions, post length, hashtags, mentions, and other
structural features, without performing deep semantic analysis. Contextual content
analysis, in contrast, focuses on the textual content of posts to capture themes, topics,
and expressed sentiments. These two levels capture different but complementary aspects
of user-generated content in online social networks. Metadata-based indicators mainly
reflect the visibility, reach, and interaction potential of content, while contextual analysis
captures the semantic, thematic, and emotional meaning conveyed by users. By integrat-
ing these two perspectives, the content-based approach enables a more comprehen -
sive assessment of user influence, combining observable engagement signals with deep
semantic understanding of what is communicated and how it may affect other users.
Within contextual content analysis, user influence can be further characterized through
multiple linguistic and semantic signals.
By analyzing the topics a user engages with, researchers can assess their expertise in
specific domains, as influencers often guide discussions around particular subjects [ 36–
39]. The influence of a user is further reflected through the originality of their contribu -
tions (novelty) and the clarity and depth of their expression (eloquence) [40].
Sentiment analysis complements this approach by evaluating the emotions conveyed
in content, highlighting the impact that strong emotional expressions can have on oth -
ers. Sentiment analysis is also part of contextual content analysis, as it captures the
emotional tone embedded in user-generated content and helps evaluate how emotional
expressions contribute to influence propagation and user engagement.
Together, these analyses allow the content-based approach to provide a comprehen -
sive understanding of a user’s influence, focusing on what they communicate, how they
express it, and the relevance and quality of their contributions.
6.3 Hybrid approach
The hybrid approach combines insights from both interaction-based and content-
based analyses to provide a more comprehensive understanding of user influence in
online social networks. It integrates network interactions, such as connections, com -
munication patterns, and engagement metrics, with content features, including textual

Page 10 of 34
Chebil et al. Discover Computing          (2026) 29:513
themes, sentiments, and metadata attributes. By leveraging both dimensions, the hybrid
approach can identify opinion leaders who are not only central or active within the
network but also produce high-quality, engaging, and influential content. This dual
perspective allows researchers to capture the multifaceted nature of influence, encom -
passing both social connectivity and informational impact, and is particularly effective
for detecting users whose authority emerges from both their interactions and the sub -
stance of their contributions [41–43]. The hybrid approach overcomes the limitations of
single-approach strategies and offers more refined detection of opinion leaders.
For instance, Li et al. [44] introduced an enhanced mixed framework to identify topic-
specific opinion leaders, considering user behavior, textual content, and time. Through
the analysis of these factors, the study categorizes and ranks opinion leaders based on
four distinct features: expertise, novelty, influence, and activity. Moreover, Song et al.
[45] proposed a hybrid approach to detect opinion leaders and influential comments in
Chinese news comment networks. The approach models comment networks and user
networks using explicit and implicit links, while incorporating sentiment analysis to
evaluate comment content. By integrating network structure and content features, the
method dynamically identifies both the most influential comments and the key opinion
leaders within the network.
7 Opinion leaders detection methods
In this study, we present the most common methods for identifying opinion leaders in
social networks, classified as descriptive, graph-based, PageRank, diffusion process-
based, statistical and stochastic, machine learning, deep learning, and lexical methods.
These methods correspond to computational techniques that implement the interaction-
based, content-based, and hybrid approaches defined previously, and differ in how they
model influence, extract information, and quantify opinion leadership within social net -
works. Typically, graph-based methods, PageRank, diffusion processes, and statistical/
stochastic methods are associated with interaction-based analyses, while machine learn -
ing, deep learning, and lexical methods are applied in content-based analyses. Descrip -
tive methods, which capture general user activity and engagement metrics, are generally
used as complementary measures alongside these techniques.
These methods are often combined, forming hybrid approaches that leverage both
interaction- and content-based techniques. By integrating multiple types of evidence,
such hybrid methods enable the detection of opinion leaders who are not only struc -
turally central within the network but also produce influential and high-quality content,
resulting in a more robust and comprehensive framework for OLD.
7.1 Descriptive methods
Descriptive methods are traditional methods for identifying opinion leaders and fall into
three categories: observation, surveys, and interviews [ 22]. Observation involves sys -
tematically monitoring interactions and recording behaviors, but it is prone to obser -
vational bias and provides only a limited view of the overall community, and is mainly
suitable for small or local communities due to its simplicity. Surveys ask participants to
identify influential individuals based on predefined criteria, though they can be costly
and time-consuming for large samples and are prone to sampling bias and volunteer
response bias. Finally, face-to-face interviews are used to collect data directly, but they

Page 11 of 34
Chebil et al. Discover Computing          (2026) 29:513
also involve high costs, time constraints, and potential biases from both interviewers and
respondents, especially in large-scale networks where data collection becomes expensive
and difficult to scale.
The study by Valente and Pumpuang [ 46], reviewed approximately 200 sociological
studies and identified ten distinct descriptive techniques for detecting opinion lead -
ers. These methods are primarily sociological in nature and differ from more technical
detection methods that rely on network metrics, statistical analysis, or machine learning
techniques.
7.2 Graph-based methods
Graph-based methods for detecting opinion leaders in social networks leverage the
representation of these networks as graphs, where nodes represent individuals and
edges capture interactions or relationships. These methods often use network analy -
sis techniques, such as centrality measures (degree, betweenness, closeness), to iden -
tify influential users who can affect opinions and behaviors within the network. Recent
advancements integrate graph embeddings that map networks into low-dimensional
vector spaces, enabling more scalable and nuanced detection by capturing structural–
and sometimes semantic–patterns. Aditionnaly, other approaches combine community
detection with influence scoring on local and global structures.
For instance, Liu et al. [ 47] proposed a Synthesize Centrality (SC) method that identi -
fies opinion leaders by combining degree centrality, betweenness centrality, and close -
ness centrality. This method outperformed PageRank and HITS algorithms in terms of
accuracy in identifying opinion leaders. Moreover, Shafiq et al. [ 48] analyzed topological
measures on Facebook and found that opinion leaders tend to have high degree central -
ity, strong eigenvector and PageRank centrality, the highest clustering coefficients, and
the shortest paths in the network. Similarly, Gökçe et al. [ 49] identified Turkish political
opinion leaders using degree centrality to estimate audience size, eigenvector central -
ity to assess network relevance, and betweenness centrality to capture communication
flows. Fan et al. [ 50] combined content analysis, social network analysis, and Borda
ranking to identify opinion leaders and their supportive roles in online forums. Cui and
Pi [ 51] proposed a latent-variable graph model based on user features and behaviors,
achieving improved detection accuracy on Sina and Twitter data. Foughali et al. [ 30]
integrated content features with HITS ranking using influence, expertise, activity, and
novelty, outperforming baseline methods on benchmark datasets. Furthermore, Chekkai
et al. [ 52] proposed two graph-based methods using Minimum Vertex Cover and frag -
mentation techniques to identify influential nodes in recommender graphs. Hui et al.
[53] introduced a model-agnostic framework that embeds dynamic social networks into
node vectors and aggregates multiple rankings to detect opinion leaders.
The study by Li et al. [ 54] proposed a graph-based framework combining opinion
dynamics and compressive sensing to reconstruct networks and analyze the impact of
leader attributes. Jain and Katarya [ 55] introduced a community-based approach using
modified Louvain clustering and firefly optimization to detect local and global opin -
ion leaders, achieving superior performance over baseline methods. Also, another
study in [ 56] proposed D_OLMiner for dynamic networks using community detec -
tion and k-means clustering, improving efficiency and accuracy. Semenkovich et al.
[57] used SVM with user activity features to detect opinion leaders, outperforming

Page 12 of 34
Chebil et al. Discover Computing          (2026) 29:513
centrality-based methods. Furini et al. [ 58] combined temporal graphs, PageRank, and
psycholinguistic features for leader detection. Yang et al. [59] integrated LDA with com-
munity detection for local and global influence analysis. Zhang et al. [ 60] proposed
RacRank, using clustering and ranking to reduce complexity while maintaining com -
petitive performance. Moreover, Huang et al., [ 61] used a directed graph weighted by
textual similarity and common neighbors, applied k-means to detect communities, and
ranked users by topological and behavioral scores to select leaders. Zhang [ 62] intro-
duced INFOE, which tracked opinion leaders’ evolution via BTM, community mapping,
and a multidimensional index of behavior, sentiment, and topology, with temporal drift
(IDI) and stability (ISI) enabling online leader tracking.
7.3 PageRank-based methods
PageRank-based methods identify opinion leaders by measuring the influence of nodes
within social networks through the quality and quantity of their incoming links. The
algorithm assigns higher scores to users who are cited by other influential users, effec -
tively capturing global network influence. Adaptations, such as topic-sensitive PageRank
[63], refine this by considering domain-specific interactions, improving the detection
of opinion leaders relevant to particular subjects. These methods are scalable and have
proven effective in highlighting key influencers for information dissemination in diverse
online communities. PageRank has been used in various OLD methods, often alongside
topic models [22]. Researchers have enhanced these methods by modifying PageRank or
using it as a baseline for new approaches.
For instance, Song et al. [ 64] introduced InfluenceRank to identify opinion leaders
in the blogosphere. It assesses blog centrality and novelty using cosine similarity based
on LDA. Despite strong results in coverage and diversity, Influencerank overlooks the
impact of posting time. Other algorithms, such as TwitterRank [ 65] and TrustRank [66],
modify PageRank for different networks such as Twitter followers and sentiment-labeled
networks. OpinionRank [ 67] adapted PageRank by ranking nodes based on opinion
scores, producing results similar to standard PageRank, while DBSCAN-based tempo -
ral comment network analysis improved OLD but required accurate NLP and implicit
link modeling [22]. Also, Luo et al. [ 68], introduced an enhanced Weighted LeaderRank
algorithm incorporating user activity metrics (replies, posts, likes), where reply-based
influence outperformed PageRank and LeaderRank. Furthermore, Alp and öğüdücü
[69] applied a Personalized PageRank (PPR) algorithm using network topology and user
features (focus speed, originality) to identify the top 25 opinion leaders per topic via
LDA-labeled tweets, and showed improved performance over baseline methods.. Addi -
tionally, Zhu et al. [ 70] introduced Leader-PageRank, extending PageRank with emo -
tional weighting to better capture influence and identify positive, professional opinion
leaders. Liqing et al. [42] developed HybridRank, combining topic analysis and temporal
features to track user influence in thematic groups over time, showing superior perfor -
mance on Sina BBS data.
7.4 Diffusion process-based methods
Diffusion process-based methods detect opinion leaders by modeling how information
spreads through social networks. These methods identify key leaders as those who initi -
ate or significantly accelerate the spread of information, thus maximizing reach within

Page 13 of 34
Chebil et al. Discover Computing          (2026) 29:513
the network. By simulating diffusion models like Independent Cascade or Linear Thresh-
old, they capture the dynamic process of influence propagation and effectively highlight
users essential for broad and fast information dissemination. Building on this idea, the
concept of influence maximization has gained attention in OLD research. Kempe et al.
[71] addressed it by identifying seed agents to spread information.
Moreover, the concept of influence maximization has gained attention in OLD
research. Kempe et al. [ 71] addressed it by identifying seed agents to spread informa -
tion. Also, Zhao et al. [ 72] developed IM-LPA, an influence maximization algorithm
using label propagation to identify central nodes within communities without prior
parameters. Through seed selection and label propagation, it efficiently uncovers com -
munity structure. Its near-linear complexity makes it suitable for large networks, and
experiments on real and synthetic data confirmed its effectiveness. Additionally, Cho et
al. [73] studied opinion leaders in marketing, focusing on how their traits affect diffusion
speed and total adopters. Highly sociable leaders accelerated spread, while those with
high closeness centrality maximized cumulative adoption. Their influence depended on
network type and reaching a critical mass of initial adopters, underlining their role in
effective product adoption.
Recent studies have further extended influence maximization to higher-order network
structures such as hypergraphs, providing a more realistic modeling of complex diffusion
processes and, consequently, of OLD. For instance, the study [ 74] proposes an adaptive
heuristic (HADP) that exploits higher-order interactions to improve efficiency in influ -
ence maximization under hypergraph-based diffusion dynamics. Similarly, the study
[75] introduces a meta-heuristic genetic algorithm (HGA) that integrates evolutionary
operators to identify influential seed sets in hypergraphs, highlighting the importance of
combining structural diversity with diffusion modeling. These works show that modern
influence maximization approaches relevant to OLD move beyond traditional pairwise
diffusion models by explicitly considering higher-order interactions, which significantly
affect diffusion behavior and seed selection strategies.
7.5 Statistical and stochastic methods
Identifying opinion leaders can be considered an anomaly detection problem, as these
individuals exhibit behaviors, opinions and thoughts that deviate from majority patterns
[76]. Statistical and stochastic methods, among the oldest approaches in this field dating
back to the 19th century, share a fundamental assumption: normal instances are found in
the high-probability regions of a stochastic model, while anomalies appear in the low-
probability regions. These methods rely on mathematical calculations and a common
probabilistic foundation, which justifies their grouping into a single category. Statistical
models analyse data statically to estimate probabilities or extract features, while stochas-
tic processes model the dynamic and random evolution of the network over time. Thus,
they share a probabilistic basis, but differ in the way they represent and analyse the data
[22, 26].
Statistical methods:  Generally, the statistical methods analyse social networks by
extracting numerical characteristics of nodes, such as reputation, follower/following
ratio, or activity level. Statistical methods use indicators such as frequency, mean, stan -
dard deviation, or correlations to identify users with significant impact. These meth -
ods can be content-based or interaction-based. They thus allow for the synthesis and

Page 14 of 34
Chebil et al. Discover Computing          (2026) 29:513
interpretation of what is visible in users’ behaviors or publications. These characteristics
combine structural (network connectivity) and behavioral (interactions, shared content)
information to quantify users’ influence and understand their role in the network [22].
Stochastic methods:  OLD based on statistical and stochastic methods represents a
sophisticated method within the broader field of opinion leader identification. These
methods leverage probabilistic and statistical models to analyze user influence and
behavior, effectively capturing patterns of information flow and social influence within
networks. Statistical methods focus on extracting and quantifying numerical character -
istics of nodes–such as reputation scores, follower/following ratios, and activity levels–
using indicators like frequency, mean, standard deviation, and correlations to identify
users with significant impact. In contrast, stochastic methods emphasize modeling the
dynamic and uncertain nature of social networks by treating opinion formation and
influence spread as stochastic processes that evolve over time. This includes techniques
such as probabilistic centrality measures and weighted averaging models to estimate
influence and conformity among users. Compared to purely structural approaches, these
methods incorporate uncertainty, temporal changes, and probabilistic behavior, offering
a more nuanced and realistic evaluation of opinion leaders’ roles.
Statistical and stochastic models are used to analyze complex networks. For example,
Guimera and Amaral [77] applied such models to identify tightly connected groups with
limited links to other communities, introducing measures like internal degree and par -
ticipation coefficient to characterize node roles. Stochastic methods often rely on the
Markov principle, which states that a system’s next state depends only on its current
state [22]. Accordingly, Markov chains are frequently used to model processes where the
probability of an event is determined solely by the preceding state [78]. Also, Amor et al.
[79] proposed a method to identify communities and user roles in follower and tweet-
sharing networks by analyzing communication patterns. Using Markov stability, they
detected groups with similar role profiles, implicitly revealing potential opinion leaders.
Fang et al. [80] conducted a statistical analysis of Weibo data during the COVID-19 out-
break in China and found that positive sentiment significantly influenced information
diffusion.
Moreover, Ellero et al. [ 81] studied agent interactions using Galam’s stochastic model
[82], showing that a few opinion leaders can accelerate or reverse consensus. Oueslati
et al. [ 43] proposed a dynamic detection method (DDOL) that identifies opinion lead -
ers through temporal snapshots, combining statistical analysis of social interactions and
opinion term frequency without modeling direct user relationships. Aditionnaly, Kumar
et al. [ 83] proposed a stochastic algorithm, MSMA, inspired by spider monkey forag -
ing. It combines node2vec graph embedding with k-means++ clustering to detect opin -
ion leaders by iteratively updating their positions. Tested on large real networks with
IC and SIR diffusion models, MSMA outperformed classical and metaheuristic meth -
ods in detection quality and computational efficiency. In another study, Weizhe et al.
[84] proposed an opinion leader detection system using Markov Logic Networks (MLN),
combining data collection, feature selection, and probabilistic reasoning. MLNs model
user attribute relationships to estimate leadership likelihood, offering higher accuracy
and robustness. Stochastic methods treat influence as uncertain, capturing behavioral
randomness through entropy.

Page 15 of 34
Chebil et al. Discover Computing          (2026) 29:513
7.6 Machine learning methods
The detection of opinion leaders based on machine learning methods leverages various
algorithms to analyze user features, behaviors, and network structures in order to iden -
tify influential individuals in social networks. These methods include supervised learn -
ing techniques such as classification models trained on labeled data to predict opinion
leaders based on selected features. Beyond classification, unsupervised methods like
clustering group users with similar influence profiles, and topic modeling techniques
uncover dominant themes in user-generated content, enriching the detection process.
Semi-supervised learning also plays a crucial role when only a small amount of labeled
data is available, combining labeled and unlabeled data to improve model accuracy.
Machine learning methods provide a flexible and robust framework to integrate struc -
tural, behavioral, and semantic data for opinion leader identification.
The study in [ 85], introduced OLMiner, an algorithm designed to efficiently iden -
tify opinion leaders in social networks. This algorithm uses community detection to
reduce candidate sizes and employs clustering-based analysis for leadership identifica -
tion. Experiments show that OLMiner effectively discovers influential opinion leaders
across various real datasets while ensuring efficiency and scalability. Moreover, Chen et
al. [86] proposed the TCOL-Miner method, which constructed a post-and-follow social
network weighted by publication time, applied a modified H_Cluster for community
detection and k-means for filtering leader candidates, and used sentiment and semantic
analysis to identify opinion leaders, outperforming existing methods. Also, Duan et al.
[87] proposed a method combining clustering and sentiment analysis to detect opinion
leaders on stock market forums. It clusters user activities to find candidates and evalu -
ates their opinions against actual price changes. Tested on Chinese market data, it out -
performs traditional network-based methods by capturing behavior and opinion quality.
In addition, Zhai et al. [ 88] combined sentiment analysis, network centrality, and a BP
neural network to identify opinion leaders on Weibo. They used sentiment scores and
closeness centrality as inputs, and a three-layer neural network to predict leader impor -
tance, showing the strong impact of sentiment. The dominant method is machine learn -
ing. Besides, Aleahmad et al., [ 89] proposed a OLFinder method which first uses LDA to
extract key topics, then calculates a competency score based on these topics and a popu-
larity score from the network links to effectively identify opinion leaders. In the [ 23],
the authors developped Social Network Opinion Leaders (SNOL), a two-step system to
identify topical opinion leaders on social media. Tweets are first classified by topic, then
users are scored using centrality measures and other indicators. Tests on a large Twitter
dataset show SNOL outperforms PageRank and other existing methods.
Furthermore, Liu et al. [ 90] proposed the Modality-Consistent Harmonized Discrimi -
nant Embedding (MCHDE) method, a subspace learning approach that projects mul -
tiple data modalities into a shared space while preserving discriminant and structural
information. Experiments showed its effectiveness in identifying opinion leaders on
synthetic and real social media data. Additionally, the authors in [ 91] introduced the
Opinion Leader Detection (OLED) method, a two-step method combining thematic
tweet classification and subnetwork analysis to identify opinion leaders, outperform -
ing PageRank in most domains. In addition, Chebil et al. [ 38] proposed Twitter Opinion
Leaders’ Detection (TOLD), a hybrid method combining content and interaction. Using
machine learning, statistical, graph-based, and PageRank-based techniques, this method

Page 16 of 34
Chebil et al. Discover Computing          (2026) 29:513
identifies opinion leaders through multidimensional metrics. Results show TOLD out -
performs existing methods in correlation and similarity. Similarly, in [ 92], TOLD was
extended by the Selecting Opinion Leaders using Skyline Query (SOL-SQ) method. The
Skyline Query is used to select non-dominated opinion leaders based on multi-metric
evaluation without predefined weights or Top-N ranking.
7.7 Deep learning methods
Opinion leaders detection based on deep learning methods exploits advanced neural
network architectures designed to capture complex and non-linear relationships within
social networks. One of the prominent techniques is the use of Graph Neural Networks
(GNNs), which model the social network as a graph and aggregate information from a
node’s neighbors to learn rich latent representations that reflect both the structure of the
network and users’ influence patterns. These models go beyond traditional hand-crafted
features by automatically learning multi-layered abstractions of the data, including
behavioral patterns and textual content associated with users. Deep learning models like
Recurrent Neural Networks (RNNs) and temporal embedding methods also incorporate
the dynamic evolution of user influence over time, enabling continuous adaptation to
changing network conditions. This results in enhanced accuracy and scalability in identi-
fying opinion leaders in large-scale, real-world social networks. Deep learning methods
have thus become essential in contemporary research for detecting opinion leaders, par -
ticularly due to their ability to handle high-dimensional, multimodal data and capture
intricate patterns of influence and information diffusion.
Recent advances in deep learning have further expanded OLD capabilities through
Transformer-based models and Large Language Models (LLMs). Transformer architec -
tures are particularly effective in capturing contextual and semantic information from
user-generated content, enabling a deeper understanding of influence-related behaviors
and interactions. In this context, recent studies have explored the use of LLMs for ana -
lyzing user-generated content, modeling user behavior, and simulating opinion dynam -
ics in social networks [ 93, 94]. These studies demonstrate that LLMs can reproduce
interaction patterns and collective opinion formation in controlled environments. Com -
plementary works in social media analytics also show that Transformer- and LLM-based
models are capable of learning rich semantic representations from user-generated con -
tent and improving downstream social understanding tasks, which is directly relevant
to OLD since influence identification relies on behavioral and semantic cues [ 95, 96].
However, other works highlight that LLMs remain limited in reliably exhibiting opinion
leadership behavior and may produce biased outputs due to limitations in their training
data [97]. To further improve learning effectiveness in complex network environments,
recent studies have investigated advanced optimization strategies such as multi-dimen -
sional feature fusion with ensemble learning mechanisms and reinforcement learning-
based decision models, which enhance robustness and performance in network-based
detection tasks [ 98, 99]. These techniques, in combination with graph-based neural
architectures such as GNNs, enable the joint modeling of network structure and content
semantics, thereby improving the identification of influential users in complex social
media environments.
Similarly, Chen [100] developed a deep learning-based method for detecting key opin -
ion leaders by combining dynamic social network construction, pseudo-labeling, and

Page 17 of 34
Chebil et al. Discover Computing          (2026) 29:513
optimized GCN models. Experiments on real datasets show that the method signifi -
cantly improves leader identification accuracy. In the study by Jain et al. [101], the GNN-
based Opinion Leader Identification (GOLI) method was proposed to detect opinion
leaders by measuring neighbor reputation using trust and centrality conciliation. Tested
on six large OSNs, it effectively identifies Top-N leaders and their impact on information
diffusion, outperforming traditional SNA measures. Community detection and cluster -
ing further assist by highlighting influential nodes within specific communities. In addi -
tion, Nikseresht [ 102] introduced a deep learning-based framework that uses a game
theory algorithm to detect social-media opinion leaders and a Stacked BiLSTM model
to forecast tourism demand. Applied to Hong Kong and Sanya data, the method outper -
forms existing techniques and demonstrates strong robustness in dynamic conditions.
7.8 Lexicon-based methods
The detection of opinion leaders using lexicon-based methods on social networks
involves analyzing the text content generated by users, such as posts, comments, or
tweets, through predefined sentiment lexicons. These lexicons are lists of words anno -
tated with sentiment polarity (positive, negative, or neutral) and sometimes intensity.
By scoring the sentiment of users’ content based on these lexicons, the method identi -
fies users who express strong or influential opinions. These users are considered opinion
leaders because their language carries significant subjective weight or sentiment impact
in the network [27, 103, 104].
For instance, the study in [105] introduced an unsupervised lexicon-based method that
detects extreme positive or negative opinions by building a list of highly polarized terms.
Similarly, Al-Otaibi et al. [ 106] proposed Muatheer, which identifies influential Insta -
gram users by classifying comment sentiment using a rule and lexicon-based method
combined with VADER, achieving high accuracy. Additionally, Li et al. [ 107] identified
opinion communities by analysing similarities in users’ content, timing, and interac -
tions. They then measured each member’s influence through message analysis and emo -
tional cues, with a focus on negative terms. Each user receives an influence score, and
the highest-scoring member is considered the group’s opinion leader. Also, the study in
[108] showed that the feedback users receive shapes their future behaviour, whether the
reactions are positive or negative. By analysing only post text with a statistical model,
the authors estimated content quality and highlighted individuals who are more likely to
attract attention and steer community discussions. Moreover, Wang and Fikis [109] clas-
sified tweets using SentiStrength and combined this with network analysis to identify
users who amplify strong positive or negative attitudes. Also, Oueslati et al. [ 27] applied
a hybrid method on Facebook that integrates sentiment analysis of posts and comments
with interaction patterns to improve OLD.
8 Evaluation metrics for opinion leaders detection
Evaluating OLD methods is a complex task due to the diversity of social networks and
the multi-dimensional nature of influence. This evaluation requires different metrics
depending on whether the dataset is labeled (ground truth available) or unlabeled (no
ground truth). In labeled settings, metrics are used to evaluate predictive performance
through classification accuracy, regression error, or ranking agreement, while in unla -
beled settings, evaluation relies on indirect validation such as structural consistency,

Page 18 of 34
Chebil et al. Discover Computing          (2026) 29:513
stability of detected leaders, or diffusion-based propagation behavior. The literature
highlights a range of quantitative and qualitative metrics for both scenarios, but there is
no clear agreement on the optimal evaluation metrics [23, 110].
To clarify their roles and selection conditions, correlation metrics measure rank
agreement and are applicable in both labeled settings (comparison with ground truth
rankings) and unlabeled settings (agreement between methods or stability analysis). In
contrast, regression metrics quantify absolute prediction errors in continuous influence
scores and require ground truth, whereas classification metrics evaluate leader identifi -
cation performance and are also supervised. Network structure metrics and influence
propagation metrics are mainly used as indirect evaluation tools, particularly in unla -
beled scenarios, while also serving as complementary validation when ground truth is
available.
These metrics can be numerical scores, rating scales, or graphical representations.
They can be categorized into subjective evaluation metrics, classification performance
metrics, correlation and statistical metrics, regression metrics, network structure met -
rics, influence propagation and dynamics metrics, and complexity and performance
metrics. The list of metrics presented here is not exhaustive, but it includes the most
commonly used metrics in this context. Table 2 presents the most commun evaluation
metrics category used for OLD.
Moreover, Table 3 links each OLD method family to its relevant metric categories.
The proposed mapping is based on the analysis of the 60 studies selected in this litera -
ture review. Correlation and statistical metrics serve as a common baseline across most
methods. Network structure metrics are specific to graph-based and PageRank meth -
ods, while propagation metrics dominate diffusion-based evaluation. Classification and
regression metrics are central to machine learning and deep learning. Subjective evalu -
ation is most frequently used with lexicon-based methods but can apply to any method
requiring expert validation. Complexity and performance metrics apply uniformly to
all methods. This mapping serves as a practical reference for researchers to determine
which metric categories are most relevant to their particular OLD method.
9 Discussion and research directions
9.1 Discussion
In recent years, the identification of opinion leaders has gained importance across vari -
ous application domains, prompting focused attention on the approaches and methods
for leader detection. Accordingly, we conducted an in-depth analysis of 26 representa -
tive research articles on OLD, selected from the 60 studies included in this literature
review, which are summarized in Table 4.
To provide a structured interpretation of these studies, we propose a comprehensive
framework illustrating the approaches, methods, and evaluation metrics used in OLD,
as shown in Figure 2. The figure also highlights the social network platforms analyzed in
the reviewed studies, including Facebook, Instagram, Twitter, forums, blogs, and email,
with Twitter being the most frequently examined, while LinkedIn, YouTube, and TikTok
remain underrepresented. In addition, Figure 2 organizes the techniques and algorithms
reported in the literature according to their dominant OLD method. Each technique is
classified based on its primary underlying method. It shows that graph-based methods
represent the main methodological paradigm in OLD, as most proposed techniques are

Page 19 of 34
Chebil et al. Discover Computing          (2026) 29:513
primarily built on graph structures and may incorporate additional methods as support -
ing components.
A closer inspection of the reviewed studies also reveals important dataset-related
characteristics that affect the comparability of existing approaches. In particular, bench -
mark datasets are highly heterogeneous across studies in terms of size, structure, and
annotation quality. Moreover, most datasets are derived from different social media
platforms, with Twitter being the most widely used source due to its historically open
data access through public APIs and its rich interaction structure (e.g., retweets, men -
tions, and replies), which facilitates large-scale network construction. However, access
to Twitter data has become increasingly restricted in recent years following platform
policy changes (transition to X and paid API access), which has reduced data availabil -
ity and recency for research purposes. In comparison, Facebook is also frequently used,
Table 2 Evaluation metrics for comparing OLD techniques
Category Description
Subjective evalu-
ation metrics
Use experts to assess users’ comments for perceived influence, categorizing them as strong
or weak. These assessments are aggregated to calculate each user’s overall influence score,
typically considering social skills, knowledge, leadership, and other qualities. Methods
are validated by comparing their results to expert judgments, ensuring consistency with
human or domain-specific standards. Many studies use expert ratings and expert-defined
criteria to deliver credible, scientific influence assessments, especially for detecting opinion
leaders [38, 39, 92, 111].
Classification
performance
metrics
Measures the effectiveness of OLD methods using standard metrics such as accuracy, preci-
sion, recall, and F1-score. These metrics evaluate how well a method correctly identifies
opinion leaders compared to a reference or ground truth.
Additional measures include MCC (binary classification quality), Cohen’s kappa (inter-rater
agreement), Brier score (accuracy of probabilistic predictions), ROC curve and AUC (binary
classifier performance), and error rate (frequency of misclassifications) [101, 112].
Correlation and
statistical metrics
Assess the strength and direction of the relationship between predicted and actual values.
A correlation coefficient of 1 or -1 indicates a strong relationship, while values near 0 indi-
cate a weak relationship, providing insight into method effectiveness [113]. Kendall’s and
Spearman’s rank correlations evaluate ordinal associations [114], while Osim similarity and
the Jaccard coefficient measure similarity between sets [114, 115].
Regression
metrics
Use quantitative measures to evaluate how accurately a method predicts continuous influ-
ence scores in OLD. Key metrics include Root Mean Squared Error (RMSE), Mean Absolute
Error (MAE), Mean Squared Error (MSE), R-squared, Adjusted R-squared, and Mean Absolute
Percentage Error (MAPE), which assess the difference between predicted and actual values
and the proportion of variance explained by the model.
Network struc-
ture metrics
Use measures of node position, connectivity, and influence, such as degree, closeness,
betweenness, and eigenvector centrality, to identify opinion leaders. Clustering coefficient
quantifies how nodes cluster together, while Katz centrality, Hubbell measure, and Bonacich
Power assess paths and influence across the network [116, 117]. Community-based metrics
like modularity (Q) and modularity gain evaluate the quality of network clusters, where
opinion leaders often occupy central positions. High modularity indicates well-defined
communities, and modularity gain measures improvements during community detection,
helping compare methods for effectively identifying influential nodes [86, 118–122].
Influence
propagation and
dynamic metrics
Use measures that capture how influence spreads and evolves over time. The infection
probability measures the likelihood of influence passing between users, coverage measures
the proportion of the network reached, the influence scale indicates the strength of a user’s
influence, and the influence scope (σ(S)) quantifies the overall impact of a set of users.
These dynamic metrics complement static evaluations by providing a temporal perspec-
tive on how influence evolves in a network and how users’  influence changes dynamically.
These metrics evaluate the reach, speed, and impact of opinion leaders, considering tempo-
ral interactions and cascading effects in information diffusion.
Complexity and
performance
metrics
Use measures to evaluate how efficiently and effectively OLD methods operate. This
includes computational cost (time and memory), ability to handle different graph types
(directed or undirected) [43], and adaptability to network changes over time, reflecting
robustness in dynamic environments [22, 83].

Page 20 of 34
Chebil et al. Discover Computing          (2026) 29:513
although its data access remains more limited and restrictive for large-scale extraction.
In addition, many studies rely on private or non-public datasets, which reduces repro -
ducibility and prevents consistent benchmarking. Another key challenge concerns miss -
ing or incomplete data in social network structures, which may affect the reliability of
evaluation results. Furthermore, feature extraction is often dataset-specific, as each
study designs its own representation depending on the nature of the collected data,
which further reduces standardization. These limitations highlight the need for publicly
available benchmark datasets and unified evaluation protocols to improve the practical
significance and comparability of OLD methods.
Based on these observations, we position our taxonomy as a unified framework
for organizing the literature. Compared with existing survey studies on OLD, this
work distinguishes itself by providing a clear separation between high-level analytical
approaches, methodological techniques, and evaluation metrics. While most existing
reviews tend to conflate these levels or focus on partial classifications, our taxonomy
integrates interaction-based, content-based, and hybrid approaches with their corre -
sponding methods, including graph-based, PageRank, diffusion process-based, statis -
tical and stochastic, machine learning, deep learning, and lexicon-based techniques,
within a unified framework. This organization enables a more coherent interpretation of
existing studies and facilitates a systematic comparison of OLD frameworks across the
literature. Furthermore, the inclusion of a structured classification of evaluation metrics
provides a consistent basis for assessing and comparing different methods.
Moreover, we summarized the advantages and limitations of OLD approaches in Table
5. The interaction-based approach provides advantages in capturing network structure
and diffusion patterns through observable interactions such as follows, mentions, and
retweets. However, it is limited by its inability to capture semantic content and by scal -
ability challenges in large-scale networks. The content-based approach leverages tex -
tual information, including topics and sentiment, to better understand user opinions,
but it is constrained by language ambiguity and the need for advanced text processing.
The hybrid approach combines structural and textual information to provide a more
Table 3 Mapping between OLD method families and evaluation metric categories
Method Recommended metric categories
Graph-based Network structure•••
Correlation and statistical••
PageRank Network structure•••
Correlation and statistical••
Diffusion-based Propagation and dynamics•••
Correlation and statistical••
Statistical and stochastic Correlation and statistical•••
Regression••
Machine learning Classification performance•••
Regression••
Deep learning Classification performance•••
Regression••
Propagation and dynamics•
Lexicon-based Subjective evaluation•••
Correlation and statistical••
All methods Complexity and performance•
••• = strongly recommended        ••= recommended        •= occasionally used

Page 21 of 34
Chebil et al. Discover Computing          (2026) 29:513
Ref
and
years
Platforms Approaches  Methods Evaluation
metrics
Benefits Limitations
[72]
2016
Football, SFI, and
PGP networks.
Facebook and
Email
Interaction Dominant: diffusion
process
Influence spread,
modularity (Q),
time complexity,
and influence
scope (σ(S))
Parameter-free, captures community structure via label
propagation, outperforms influence maximization methods,
and is scalable with low complexity.
Performance depends on seed selection and
weak community boundaries, and assumes
influential nodes have high degree, which may
not always hold.
[47]
2013
Sina microbolg Interaction Dominant: graph-based Accuracy Outperforms PageRank and HITS, showing strong correlation
and improved accuracy with more leaders.
Based on network structure only, ignores message
content and temporal dynamics, and assumes
influence is stable over time.
[100]
2024
Mobile01 Forum Interaction Dominant: deep learning
Other: grap-based
Influence Spread Considers temporal dynamics of social networks and im-
proves influence propagation compared to existing methods.
Computationally expensive, depends on temporal
data quality, and is sensitive to parameter tuning.
[56]
2017
Mobile01 Forum Interaction Dominant: graph-based
Other: machine learning
Influence spread Reduces execution time by identifying community structure,
handles dynamic networks via temporal modeling, and im-
proves influence diffusion compared to existing method.
Requires precise temporal data, ignores semantics,
is sensitive to parameters, unstable for dynamic
communities, and computationally expensive.
[57]
2019
Twitter Interaction Dominant: graph-based
Other: machine learning
Accuracy Combines network structure and user activity, improving
accuracy over classical centrality-based methods.
Ignores semantic content and user evolution over
time.
[60]
2020
Weibo microblog Interaction Dominant: graph-based
Others: machine learn-
ing and statistical
DLT, ADLT, C-
value, and time
complexity
Reduces computational complexity via clustering, offers a
good trade-off between precision and efficiency (close to UI_
LR), and outperforms other methods including ClusterRank.
Relies on interaction and topology analysis,
ignores content, is sensitive to clustering param-
eters, and does not support temporal or real-time
detection.
[83]
2023
LastFM, Epinions,
Wiki, Bitcoin,
Github, and
Deezer networks.
Facebook and
Email
Interaction Dominant: stochastic
and statistic
Other: graph-based,
machine learning and
diffusion process
Total opinion
spread, number
of opinion lead-
ers, influence
spread, infection
probability, and
computational
time
Outperforms classical (PageRank, Degree, Eigenvector) and
metaheuristic methods, is robust across diffusion models (IC,
SIR, COD), balances performance and time, and improves
node representation with node2vec.
Ignores temporal dynamics and content, and is
sensitive to parameter settings.
[102]
2025
Facebook, Twit-
ter, Baidu, and
TripAdvisor
Interaction Dominant: deep learning MAE, RMSE, and
MAPE
Combines game theory and deep learning to improve ac-
curacy, handles non-stationary data, supports multi-platform
detection, and applies to various domains.
Computationally expensive, requires large high-
quality datasets, and is sensitive to hyperparam-
eter tuning.
Table 4 Summarized review of the related works

Page 22 of 34
Chebil et al. Discover Computing          (2026) 29:513
Ref
and
years
Platforms Approaches  Methods Evaluation
metrics
Benefits Limitations
[43]
2021
Facebook Content Dominant: statistical Complexity,
graph type, net-
work dynamicity,
and precision
Considers temporal dynamics, supports different graph types,
and outperforms classical centrality methods in accuracy.
Measures content influence using likes, shares,
and comments without modeling user interac-
tions, and relies on arbitrary weighting that may
affect robustness.
[58]
2025
Twitter Hybrid Dominant: graph-based
Other: pageRank
Pearson correla-
tion coefficients
Captures temporal influence dynamics, distinguishes active
and passive interactions, integrates psycholinguistic analysis,
and outperforms classical approaches.
Requires structured temporal data, struggles with
irony and sarcasm, and lacks semantic content
analysis.
[59]
2022
Micro-blogging Hybrid Dominant: graph-based
Other: machine learning
Accuracy, F1
score, Normal-
ized Mutual In-
formation (NMI),
and modularity
(Q)
Integrates semantic content analysis, identifies local opinion
leaders, and outperforms baseline methods in accuracy.
Computationally expensive and does not support
real-time network evolution.
[62]
2025
Sohu and Tiao-
tiao forums
Weibo microblog
Hybrid Dominant: graph-based
Others: machine
learning, statistical and
stochastic
F1-score Captures temporal influence, combines interactions, senti-
ment and network structure, identifies leader cohesion and
segmentation, and improves F1-score compared to existing
methods.
Requires historical data, struggles with sudden
events, assumes similar interests among lead-
ers, and is computationally expensive for large
networks.
[61]
2025
Sina microblog Hybrid Dominant: graph-based
Others: statistical and
machine learning
Nnumber of
infuential users
and coverage
Objectively determines the number of opinion leaders and
provides a more precise and reliable identification than exist-
ing methods.
High computational cost, relies on limited evalu-
ation criteria, is sensitive to clustering parameters,
and requires weight tuning.
[30]
2026
Twitter Hybrid Dominant: graph-based
Other: statistical
F1-score, recall,
precision, ac-
curacy, and
G-Mean
Integrates semantic, behavioral, and structural features, im-
proving accuracy over HITS and baselines across domains.
Depends on data quality and availability, limiting
generalization across platforms.
[87]
2014
Forum Gouba Hybrid Dominant: machine
learning
Other: statistical
Correlation
coefficient
Reduces computational cost via clustering, correlates
opinions with market behavior to identify relevant users, and
outperforms PageRank in leader detection.
Sensitive to clustering parameters, relies on static
dictionaries, ignores deep semantic content, and
depends on the analysis period.
Table 4 (continued)

Page 23 of 34
Chebil et al. Discover Computing          (2026) 29:513
Ref
and
years
Platforms Approaches  Methods Evaluation
metrics
Benefits Limitations
[86]
2016
Mobile01 Forum Hybrid Dominant: machine
learning
Others: graph-based and
statistical
Influence spread Considers temporal context and leadership quality, and
distinguishes positive and negative leaders using sentiment
analysis.
Sensitive to clustering parameters, depends on
dictionary quality for sentiment analysis, and mea-
sures expertise only by publication count without
semantic understanding.
[88]
2021
Weibo microblog Hybrid Dominant: ma-
chine learning and
graph-based
MSE Considers emotional factors in influence assessment and
achieves good predictive performance (low MSE).
Limited by outdated sentiment lexicon cover-
age and incomplete data due to Weibo access
restrictions.
[89]
2016
Twitter Hybrid Dominant: machine
learning
Others: graph-based and
statistical
Precision, recall,
average preci-
sion, and P@N
Integrates thematic competence and network popularity, and
outperforms existing methods in precision, recall, average
precision, and P@N.
Sensitive to topic extraction quality (LDA) and
affected by indiscriminate popularity based on
retweets.
[91]
2020
Twitter Hybrid Dominant: machine
learning
Others: graph-based and
statistical
Precision Outperforms PageRank, integrates semantic and structural
features, and enables topic-based OLD for marketing.
Does not supports temporal dynamics or real-
time detection, and is sensitive to the quality of
topic extraction (LDA).
[23]
2021
Twitter Hybrid Dominant: machine
learning
Other: graph-based
RTcount, spread
score, F1 score,
and precision
Integrates thematic classification, user modeling, centrality,
and sentiment analysis, outperforms PageRank in precision
and dissemination, and uses distributed big data tools for
scalability.
Ignores temporal dynamics and is computation-
ally expensive in distributed environments.
[90]
2018
Instagram Hybrid Dominant: machine
learning
Others: graph-based and
statistical
F1-score and
time complexity
Achieves strong performance with only 2% annotated data,
outperforms state-of-the-art methods in F1-score, and mod-
els cross-modal relationships for better representation.
Relies on linear transformations, limiting the mod-
eling of complex relationships, is computationally
expensive, and ignores semantic and temporal
dynamics.
[27]
2023
Facebook Hybrid Dominant: lexicon-based
Others: machine learn-
ing and statistical.
MSE, MAE,
R-squared, and
precision
Combines interaction, content, and emotion features,
extends DDOL with sentiment analysis (NDDOL), improves
accuracy over PageRank, Betweenness, and DDOL, and con-
siders network dynamics.
Limited sample size, incomplete user history, lexi-
cal dictionary limitations (e.g., irony and nuances),
and dependence on structured temporal data.
Table 4 (continued)

Page 24 of 34
Chebil et al. Discover Computing          (2026) 29:513
Ref
and
years
Platforms Approaches  Methods Evaluation
metrics
Benefits Limitations
[84]
2014
Forum Hybrid Dominant: statistical and
stochastic
Other: machine learning
Accuracy Outperforms traditional non-relational models and integrates
MLN (Markov Logic Networks) to model complex relation-
ships and uncertainty.
Computationally expensive MLN training on
large data, requires expert predicate design and
complete relational data, and ignores semantic
and temporal dynamics.
[70]
2016
Automotive
Forum
Hybrid Dominant: pageRank
Other: machine learning
Precision, recall,
F1 score, and
accuracy
Corrects data imbalance via SMOTE and extends classic Pag-
eRank by adding emotional weighting to improve accuracy.
Does not supports temporal dynamics or real-
time detection, favors positive sentiment leading
to bias against negative leaders, and uses manu-
ally weighted scoring that may affect robustness.
[38]
2024
Twitter Hybrid Dominant: machine
learning
Other: statistical, graph-
based and pageRank
Kendall correla-
tion, spearman
correlation,
Osim similar-
ity, and expert
rating
Combines multiple influence metrics (topical, domain,
engagement, popularity, and network structure) and enables
topic-specific OLD for more relevant recommendations.
Combining multiple influence metrics increases
computational and implementation complexity,
and the model lacks temporal dynamics, limiting
its ability to capture evolving network behavior.
[92]
2025
Twitter Hybrid Dominant: machine
learning
Other: statistical, graph-
based and pageRank
Jaccard coef-
ficient, standard
deviation, expert
rating, and
quartiles
Automatically selects key opinion leaders that are not
dominated by any others and without assigning preference
weights to the various metrics.
Some neighboring users of the opinion leaders
which are selected by the Skyline Query, may be
valuable but are not selected.
Table 4 (continued)

Page 25 of 34
Chebil et al. Discover Computing          (2026) 29:513
comprehensive view of influence, but this integration increases computational cost
and implementation complexity. Overall, the three approaches present complementary
trade-offs between structural analysis, semantic understanding, and integration capabil -
ity. Interaction-based methods are more suitable for large-scale diffusion analysis, con -
tent-based methods are effective for opinion and sentiment understanding, while hybrid
methods are preferred when both structural and semantic perspectives are required. The
choice of approach depends on data availability, application objectives, and scalability
constraints.
Additionally, Table 6 summarizes the advantages and limitations of OLD methods,
which support opinion leader detection through interaction-based, content-based, and
hybrid approaches. The selection of an appropriate method depends on the application
context and the adopted approach.
Fig. 2 Global framework of OLD in OSNs

Page 26 of 34
Chebil et al. Discover Computing          (2026) 29:513
To address the question of method suitability, we further clarify that no single method
is universally superior. Instead, each method is more appropriate under specific applica -
tion scenarios depending on the trade-off between scalability, accuracy, interpretability,
and data availability. The comparative analysis shows that these methods exhibit clear
trade-offs in terms of scalability, accuracy, and computational complexity. Graph-based
methods effectively exploit network topology, centrality measures, and community
structure to identify influential users, but they are computationally expensive in large-
scale networks and may overlook semantic and contextual information. PageRank-based
methods capture global influence through link structure and connectivity, but similarly
ignore content and sentiment signals, which may limit the quality of influence estima -
tion. These methods are particularly suitable when the objective is to detect structurally
important or highly connected opinion leaders in large-scale networks. Statistical and
stochastic methods model influence under uncertainty using probabilistic frameworks,
but they often rely on simplifying assumptions that may not fully reflect the heteroge -
neity of real social behavior. They are more appropriate when influence is represented
through aggregated behavioral or probabilistic features under uncertainty. Diffusion
process-based methods analyze information cascades and propagation patterns to iden -
tify influential seed users, but their effectiveness depends strongly on accurately model -
ing interaction dynamics, which remains challenging in real social networks. They are
best suited for modeling influence spread and information diffusion scenarios. Machine
learning methods integrate user features, behavioral signals, and content information to
improve detection performance. However, they require high-quality labeled data, which
is often difficult to obtain in practice. These methods are most suitable when labeled
data is available and the goal is to predict influence based on engineered features. Deep
learning methods further enhance accuracy by learning complex representations from
network structure, user behavior, and content, but they are highly resource-intensive
and suffer from limited interpretability due to their black-box nature. They are particu -
larly effective for large-scale and content-rich datasets where complex patterns must be
learned automatically. Lexicon-based methods are computationally efficient and easy to
deploy using predefined sentiment resources, but their performance strongly depends
Table 5 Opinion leaders’ approaches comparative analysis
Approaches Advantages Limitations
Interaction-based Network-centric: captures user influence
through network position and interactions.
Real-time tracking: identifies active leaders
from ongoing interactions.
Quantifiable influence: uses measurable
signals such as retweets and mentions.
Scalability issues: expensive on large
networks.
Overlooking content: ignores semantic
meaning of content.
Dynamic networks: difficult to adapt to
evolving networks.
Content-based Content-centric: analyzes textual content to
extract opinions and influence signals.
Sentiment detection: captures emotional
tone in user-generated content.
Topic relevance: identifies domain-specific
expertise.
NLP complexity: requires advanced text
mining techniques.
Subjectivity: interpretation of sentiment
and language may vary across users and
contexts.
Neglects network position: ignores how
the content is spread through the network.
Hybrid Comprehensive insight: combines network
structure and content.
Balanced influence: captures both diffusion
and semantics.
Adaptability: can be tuned to different
contexts.
High complexity: computationally
expensive.
Complex implementation: difficult to inte-
grate interaction and content analysis.
Overfitting risk: complex models may not
generalize well across networks.

Page 27 of 34
Chebil et al. Discover Computing          (2026) 29:513
Methods Advantages Limitations
Descriptive Observation: simple to apply in small or
local communities for identifying opinion
leaders.
Survey: allows users to select or rate
opinion leaders using predefined criteria.
Interview: provides in-depth informa-
tion through direct interaction; useful for
detecting fake accounts (e.g., bots).
Observation: bias in observation and
selection.
Survey: costly and time-consuming for
large samples; prone to sampling and
volunteer bias.
Interview: expensive and time-consuming,
especially in large networks.
Graph-based Topological insight: exploits network
topology to identify influential nodes.
Dynamic modeling: can capture evolving
relationships.
Node centrality: quantifies influence
through centrality metrics (e.g., degree,
betweenness, closeness).
High complexity: computationally expen-
sive on large networks.
Static assumption: often ignores temporal
changes.
Limited context: overlooks content and
semantics.
PageRank-based Topological insight: leverages link struc-
ture to estimate user influence.
Scalability: efficient on large-scale
networks.
Simplicity: easy to implement and widely
applicable.
Context limitation: ignores sentiment, top-
ics, and interaction context, which may lead
to misleading influence estimates.
Link sensitivity: influenced by link quantity
and quality, which may be noisy.
Static nature: less effective in rapidly evolv-
ing networks.
Diffusion process
based
Modeling opinion spread: simulates
how information cascades and opinions
propagate in networks.
Influence measurement: captures how
opinion leaders affect follower behavior.
Dynamic adaptability: adapts to chang-
ing social dynamics.
Complex modeling: requires detailed be-
havioral modeling of users and interactions.
Data dependency: needs large-scale and
rich datasets.
Uncertainty in outcomes: results may
be inconsistent due to variability in user
behavior.
Statistical and
stochastic
Dynamic analysis: captures temporal
changes in opinion propagation and
diffusion patterns.
Rich data utilization: leverages complex
user interactions for deeper network
understanding.
Probabilistic inference: quantifies uncer-
tainty in user influence using statistical
models.
Assumption limitations: relies on simpli-
fied assumptions about user interactions
and behavior that may not fully reflect
real-world complexity, leading to prediction
errors.
Computational cost: expensive on large and
complex networks.
Sensitivity: results depend on model param-
eters and initial conditions.
Machine learning Enhanced accuracy: can model complex
feature interactions and often outper-
forms traditional approaches.
Data-driven insights: automatically learns
patterns from user activity such as posts,
likes, and comments.
Scalability: handles large-scale social
network data efficiently.
Data dependency: requires high-quality la-
beled data, which may be difficult to obtain.
Implementation complexity: requires high
computational resources, making real-world
deployment difficult.
Data dependency: requires high-quality
labeled data for supervised learning.
Overfitting risks: models may fit training
data too closely, reducing performance on
unseen social networks.
Deep learning Automatic feature learning: learns rel-
evant features directly from data without
manual feature design.
Strong performance: effective on
unstructured data such as text and social
network interactions.
Graph modeling: captures complex
relationships using architectures such as
Graph Neural Networks.
Data and computation intensive: equires
large-scale data and high computational
resources.
Low interpretability: acts as a black-box
model, limiting explainability.
Overfitting risks: requires proper regulariza-
tion to ensure generalization.
Implementation complexity: requires ad-
vanced models and expertise for develop-
ment and deployment.
Table 6 Opinion leaders’ methods comparative analysis

Page 28 of 34
Chebil et al. Discover Computing          (2026) 29:513
on lexicon coverage and they lack contextual understanding, particularly in handling
ambiguous or evolving language. They are mainly suitable for sentiment-driven or
opinion-based influence detection tasks with limited computational resources. These
methods can be combined in different ways by integrating interaction-based and con -
tent-based approaches, which generally improves accuracy but increases computational
cost and system complexity. Overall, this comparative analysis provides a clear mapping
between method families and application scenarios, showing that the optimal choice
depends on the specific requirements of the task rather than the intrinsic superiority of
any single method.
9.2 Opened research direction
This literature review reveals several open research directions for OLD. These directions
are derived from the limitations of existing methods in the literature, the ongoing evolu-
tion of opinion leaders, and the continuous advancements in Artificial Intelligence (AI).
These directions form an interconnected set of research challenges that can be struc -
tured into four main thematic and interdependent axes: reliability, modeling complexity,
interpretability, and generalization in dynamic and heterogeneous environments. A list
of challenges and future directions is proposed as follows:
  • Authenticity of opinion leaders: Existing methods for OLD often fail to distinguish
between human accounts and fake accounts, such as bots or spammers. While
these methods are effective in identifying influential users, they do not consider
the authenticity of these users or the potential for misinformation. Bots, which may
spread false information, may be falsely identified as opinion leaders, leading to
skewed results. This gap highlights the need for a more comprehensive approach that
not only identifies influential users but also profiles them as human or fake, ensuring
the integrity of the identified opinion leaders. This research avenue is important and
challenging especially since bots and human opinion leaders share several features,
and distinguishing them is not straightforward especially since the emergence of
generative AI. Moreover, authenticity is strongly linked to both ethical considerations
and the reliability of all subsequent influence modeling tasks.
  • Domain-specific opinion leaders: Most of OLD methods retrieve generic opinion
leaders. The literature needs new methods that contextualize the identification
process to relate the opinion leaders to their expertise domains. Future research
may focus on domain-specific metrics to evaluate the relevance of identified opinion
leaders. Advanced NLP techniques for content analysis, domain-specific community
detection, and prior-knowledge-based analysis constitute relevant research
directions for contextualized OLD. This direction is also related to sentiment analysis
Methods Advantages Limitations
Lexicon-based Efficiency: low computational cost
enables fast sentiment analysis.
Simplicity: provides clear and interpre-
table sentiment identification.
Ease of implementation: relies on pre-
defined sentiment lexicons and requires
no training data.
Lexicon limitations: performance depends
on lexicon quality, leading to possible
misclassification.
Dynamic nature of social networks:
struggles to adapt to evolving social media
language.
Context limitation: fails to capture sarcasm
and contextual meanings.
Table 6 (continued)

Page 29 of 34
Chebil et al. Discover Computing          (2026) 29:513
and explainability, as domain understanding can improve the interpretation of
influence and provide richer context for analyzing the sentiment associated with
influential content.
  • Explainable AI for OLD: OLD is addressed by several black box machine learning-
based approaches. Developing explainable AI models to provide transparent and
interpretable insights into why certain users are identified as opinion leaders is
challenging future research. Explainability can be further enhanced through domain-
specific modeling, as the interpretation of influence becomes more meaningful when
grounded in contextual or topical knowledge.
  • Dynamic and temporal analysis: Social networks are extremely dynamic, especially
with emergence of generative AI where the generation of content and fake accounts
is accelerating. Investigating how opinion leaders emerge, sustain, or lose their
influence over time constitutes a relevant research avenue. This direction is closely
related to cross-platform analysis, as understanding the temporal evolution of
influence can help assess the consistency and transferability of opinion leadership
across heterogeneous platforms.
  • Supporting sentiment analysis: The role of emotional contagion in the spread of
influence should be improved in OLD. While sentiment analysis is widely used,
accurately capturing the nuances of emotional tone and understanding the context
in which opinions are expressed remains complex. Differentiating between genuine
emotional responses and strategically manipulated sentiment can be difficult,
especially when detecting opinion leaders who may influence others through subtle
emotional cues. Future research should focus on refining sentiment analysis models
to better capture these nuances and enhance their effectiveness in identifying true
opinion leaders, particularly in dynamic and evolving social contexts. Sentiment
analysis is closely linked to authenticity, since bots and coordinated actors may
manipulate emotional signals to distort influence detection.
  • Cross-platform analysis: The methods for OLD proposed in the literature are often
platform-specific, which limits their ability to be generalized. Each social platform,
whether Twitter, Facebook, or Instagram, has unique characteristics, such as
network structure, specific content type, and distinct engagement mechanisms.
These particularities strongly influence the methods for detecting opinion leaders,
making them difficult to adapt from one platform to another. An interesting research
direction would be to focus on cross-platform analysis to identify opinion leaders
who exert their influence on several platforms. Cross-platform analysis is therefore
dependent on dynamic and temporal modeling, since tracking influence across
platforms requires consistent temporal representation of user behavior.
  • Ethical and responsible influence: The literature lacks methods that ensure OLD
is used responsibly and does not manipulate public opinion. The objective is to
investigate the ethical implications of identifying and targeting opinion leaders,
particularly in sensitive areas like politics or public health. Ethical considerations
are closely related to both authenticity and explainability, since trustworthy systems
require both reliable detection and transparent decision-making.

Page 30 of 34
Chebil et al. Discover Computing          (2026) 29:513
10 Conclusions
The growing   influence of individuals in shaping opinions on social platforms has ele -
vated OLD as a pivotal area of research. This review has presented a comprehensive
synthesis of the literature, categorizing OLD approaches into interaction-based, con -
tent-based, and hybrid approaches, and identifying the primary methods used, includ -
ing descriptive, graph-based, PageRank-based, diffusion process based, statistical and
stochastic, machine learning, and lexicon-based methods. Furthermore, the study has
consolidated various evaluation metrics for assessing OLD effectiveness, including sub -
jective evaluation, classification performance, correlation and statistical, regression, net -
work structure, influence propagation and dynamic, and Complexity and performance
metrics.
The findings of this review show that most of the studies analyzed in this review rely
on graph-based methods for OLD, due to their effectiveness in modeling relational
structures in social networks. In addition, hybrid approaches emerge as particularly
effective, as they integrate interaction-based and content-based signals, although they
remain computationally expensive in terms of time and complexity.
This review also provides a systematic comparison of OLD approaches and methods,
focusing on their advantages and limitations, thereby offering a clearer understanding of
their suitability across different application contexts. Furthermore, it identifies and orga-
nizes the main categories of evaluation metrics used in the literature, which are particu -
larly relevant for evaluating and benchmarking newly proposed OLD methods against
existing approaches, especially when labeled data are available. Despite these advances,
OLD remains a challenging and multifaceted problem due to the dynamic nature of
social networks, the diversity of platforms, and the evolving forms of online influence.
Overall, this study provides a comprehensive and structured reference for the OLD
field, offering a clear roadmap for future research and supporting the development
of robust, transparent, and ethically responsible OLD methods in complex digital
environments.
Authors contributions
MC performed the literature review, paper selection, study design, methodology development, writing, and preparation
of figures and tables. MB and RJ supervised the work, reviewed and corrected the methodology, and validated the
manuscript. All authors read and approved the final version.
Funding
This research received no funding.
Data availability
No datasets were generated or analysed during the current study.
Declarations
Ethics approval and consent to participate
Not applicable.
Consent for publication
Not applicable.
Competing Interests
The authors declare that they have no known competing financial interests or personal relationships that could have
influenced the work reported in this paper.
Received: 22 April 2026 / Accepted: 27 July 2026

Page 31 of 34
Chebil et al. Discover Computing          (2026) 29:513
References
1. Putnam BB, Lamm AJ, Lundy LK. Using critical thinking styles of opinion leaders to drive extension communication. J Agric
Educ. 2017;58(3):323–37. https://doi.org/10.5032/jae.2017.03323.
2. Zatwarnicka-Madura B, Nowacki R, Wojciechowska I. Influencer marketing as a tool in modern communication-possibili-
ties of use in green energy promotion amongst poland’s generation z. Energies. 2022;15(18):6570.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0
/ e n 1 5 1 8 6 5 7 0     .
3. Jain L, Katarya R. A systematic survey of opinion leader in online social network. In: 2018 international conference on soft-
computing and network security (ICSNS). IEEE; 2018, p. 1–5. https://doi.org/10.1109/icsns.2018.8573639.
4. Rogers EM, Singhal A, Quinlan MM. Diffusion of innovations. In: An integrated approach to communication theory and
research, second edition Edition. Routledge, New York; 2014, p. 432–448.
5. Flodgren G, O’Brien MA, Parmelli E, Grimshaw JM. Local opinion leaders: effects on professional practice and healthcare
outcomes. Cochrane Database Syst Rev. 2019. https://doi .org/10.100 2/14651858. CD000125 .pub5.
6. Chan KK, Misra S. Characteristics of the opinion leader: a new dimension. J Advert. 1990;19(3):53–60.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0
8 0 / 0 0 9 1 3 3 6 7 . 1 9 9 0 . 1 0 6 7 3 1 9 2     .
7. Freeman LC. Centrality in social networks conceptual clarification. Soc Netw. 1978;1(3):215–39.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / 0 3
7 8 - 8 7 3 3 ( 7 8 ) 9 0 0 2 1 - 7     .
8. Mohammadi SA, Andalib A, Using the opinion leaders in social networks to improve the cold start challenge in recom-
mender systems. In: 2017 3th international conference on web research (ICWR). IEEE; 2017, p. 62–66.  h t t p s : / / d o i . o r g / 1 0 . 1 1
0 9 / I C W R . 2 0 1 7 . 7 9 5 9 3 0 6     .
9. Grissa K. What makes opinion leaders share brand content on professional networking sites (eg linkedin, viadeo, xing,
skilledafricans...). In: International conference on digital economy (ICDEc). IEEE; 2016, vol. 2016, p. 8–15.  h t t p s : / / d o i . o r g / 1 0 . 1
1 0 9 / I C D E C . 2 0 1 6 . 7 5 6 3 1 3 9     .
10. Tejavibulya P , Eiamkanchanalai S. The impacts of opinion leaders towards purchase decision engineering under different
types of product involvement. Syst Eng Proc. 2011;2:12–22. https://doi.org/10.1016/j.sepro.2011.10.003.
11. Gentina E, Kilic D, Dancoine P-F. Distinctive role of opinion leaders in the social networks of school adolescents: an investi-
gation of e-cigarette use. Public Health. 2017;144:109–16. https://doi.org/10.1016/j.puhe.2016.11.020.
12. Gotecha MR, Patwardhan MS. Identification of key opinion leaders in healthcare domain using weighted social network
analysis. In: 2016 international conference on computing communication control and automation (ICCUBEA). IEEE; 2016,
p. 1–6. https://doi.org/10.1109/ICCUBEA.2016.7860000.
13. Cialdini R, Cialdini RB. Influence: science and practice, BoD–Books on Demand. 2013.
14. Tucci K, González-Avella J, Cosenza M. Rise of an alternative majority against opinion leaders. Physica A. 2016;446:75–81.
https://doi.org/10.1016/j.physa.2015.11.022.
15. Koeslag-Kreunen MG, Van der Klink MR, Van den Bossche P , Gijselaers WH. Leadership for team learning: the case of univer-
sity teacher teams. High Educ. 2018;75:191–207. https://doi.org/10.1007/s10734-017-0126-0.
16. Rocha L, Mourao F, Vieira R, Neves A, Carvalho D, Bandyopadhyay B, Parthasarathy S, Ferreira R. Connecting opinions to
opinion-leaders: a case study on brazilian political protests. In: 2016 IEEE international conference on data science and
advanced analytics (DSAA). IEEE; 2016, p. 716–725. https://doi.org/10.1109/DSAA.2016.77.
17. Horio BM, Shedd JR. Agent-based exploration of the political influence of community leaders on population opinion
dynamics. In: Winter simulation conference (WSC). IEEE; 2016, vol. 2016, p. 3488–99.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / W S C . 2 0 1 6 . 7 8 2
2 3 7 8     .
18. Lees-Marshment J. Political marketing and opinion leadership: comparative perspectives and findings. In: Comparative
political leadership. Springer, Palgrave Macmillan, London; 2012, p. 165–185. https://doi.org/10.1057/9781137264916_8.
19. Hameed TS, Sawicka B. The importance of opinion leaders in agricultural extension. World Sci News. 2017;76:35–41.
20. Parau P , Lemnaru C, Dinsoreanu M, Potolea R. Opinion leader detection. Elsevier; 2017. p. 157–70.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 1 6 /
b 9 7 8 - 0 - 1 2 - 8 0 4 4 1 2 - 4 . 0 0 0 1 0 - 3     .
21. Jungnickel K. New methods of measuring opinion leadership: a systematic, interdisciplinary literature analysis. Int J Com-
mun. 2018;12:23.
22. Bamakan SMH, Nurgaliev I, Qu Q. Opinion leader detection: a methodological review. Expert Syst Appl. 2019;115:200–22.
https://doi.org/10.1016/j.eswa.2018.07.069.
23. Girgin BA. Ranking influencers of social networks by semantic kernels and sentiment information. Expert Syst Appl.
2021;171:114599. https://doi.org/10.1016/j.eswa.2021.114599.
24. Sharma K, Bajaj M. A review on opinion leader detection and its applications. In: 2022 7th international conference on
communication and electronics systems (ICCES). IEEE; 2022, p. 1645–1651.  h t t p s  : / / d o i  . o r g /  1 0 . 1  1 0 9 / i c c e s 5 4 1 8 3 . 2 0 2 2 . 9 8 3 5 8
7 0     .
25. Choudhary S, Sharma K, Bajaj M. A review on opinion leader detection and it’s applications. Available at SSRN 4293604.
2022. https://doi .org/10.110 9/ICCES5418 3.2022.9 835870.
26. GİRGİN ABA, Gümüşçekiçci G. From past to present: spam detection and identifying opinion leaders in social networks.
Sigma J Eng Nat Sci—Sigma Mühendislik ve Fen Bilimleri Dergisi 2022. https://doi.org/10.14744/sigma.2022.00043.
27. Oueslati W, Mejri S, Al-Otaibi S, Ayouni S. Recognition of opinion leaders in social networks using text posts’ trajectory
scoring and users’ comments sentiment analysis. IEEE Access. 2023;11:123589–609.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / A C C E S S . 2 0 2 3 .
3 3 2 9 0 4 9     .
28. Baziyad H, Kayvanfar V, Toloo M. A data envelopment analysis model for opinion leaders’ identification in social networks.
Comput Ind Eng. 2024;190:110010. https://doi.org/10.1016/j.cie.2024.110010.
29. Oueslati W, Mejri S, Akaichi J. A comprehensive study on social networks analysis and mining to detect opinion leaders. Int
J Comput Appl. 2024;46(8):641–50. https://doi .org/10.108 0/1206212x. 2024.238 0655.
30. Foughali A, Hlaoua L, Omri M, A hybrid approach for opinion leader detection integrating semantic, behavioral, and
topological features in online social networks. In: Proceedings of the 18th international conference on agents and artificial
intelligence. SCITEPRESS - Science and Technology Publications; 2026, p. 3807–3814.  h t t p s : / / d o i . o r g / 1 0 . 5 2 2 0 / 0 0 1 4 4 7 4 0 0 0
0 0 4 0 5 2     .
31. Newman ME. The structure and function of complex networks. SIAM Rev. 2003;45(2):167–256.
32. Fortunato S. Community detection in graphs. Phys Rep. 2010;486(3–5):75–174.

Page 32 of 34
Chebil et al. Discover Computing          (2026) 29:513
33. Katz E. The two-step flow of communication: an up-to-date report on an hypothesis. Public Opin Q. 1957;21(1):61–78.
https://doi.org/10.1086/266687.
34. Rosli N, Johar ER, Lazim MLHBM, Hashim S, Juhari NF. From hearts to carts Understanding the impact of comments likes
and share functions on consumer purchase intentions in a social media landscape. Eur J Sustain Dev. 2024;13(2):46–46.
https://doi.org/10.14207/ejsd.2024.v13n2p46.
35. Tenenboim O. Comments, shares, or likes: What makes news posts engaging in different ways. Soc Med Soc. 2022.  h t t p s : / /
d o i . o r g / 1 0 . 1 1 7 7 / 2 0 5 6 3 0 5 1 2 2 1 1 3 0 2 8 2     .
36. Chebil M, Jallouli R, Bach Tobji MA. Clustering social media data for marketing strategies: literature review using topic
modelling techniques. J Telecommun Digit Econ. 2024;12(1):510–37. https://doi.org/10.18080/jtde.v12n1.889.
37. Chebil M, Jallouli R, Bach Tobji MA, Ben Ncir CE, Topic modeling of marketing scientific papers: An experimental survey. In:
Digital economy. Emerging technologies and business innovation. Springer International Publishing; 2021, p. 147—-171.
https://doi.org/10.1007/978-3-030-92909-1_10.
38. Chebil M, Bach Tobji MA, Jallouli R. Twitter opinion leaders’ detection (told): a comprehensive approach, vol. 246. Elsevier
BV; 2024. p. 1140–9. https://doi.org/10.1016/j.procs.2024.09.537.
39. Chebil M, Jallouli R, Bach Tobji MA. Advanced methods for identifying and profiling social media influencers: a data-driven
framework. J Bus Anal. 2025. https://doi .org/10.108 0/2573234x. 2025.254 5923.
40. Hung C, Yeh P-W. Identification of opinion leaders using text mining technique in virtual community. SIMBig. 2014, p.
8–13.
41. Aghdam SM, Gharehchopogh FS, Masdari M. A hybrid approach in opinion leaders selection using African vultures opti-
mization and hunger games search algorithms. Soc Netw Anal Min. 2024. https://doi.org/10.1007/s13278-024-01228-7.
42. Liqing Q, Jinlong D, Haiyan L, Yan W. Detecting opinion leaders in online social networks using hybridrank algorithm. J
Intell Fuzzy Syst. 2018;35(1):513–22. https://doi.org/10.3233/jifs-169607.
43. Oueslati W, Arrami S, Dhouioui Z, Massaabi M. Opinion leaders’ detection in dynamic social networks. Concurr Comput
Pract Exp. 2020. https://doi.org/10.1002/cpe.5692.
44. Li Y, Ma S, Zhang Y, Kinshuk RH. An improved mix framework for opinion leader identification in online learning communi-
ties. Knowl-Based Syst. 2013;43:43–51. https://doi.org/10.1016/j.knosys.2013.01.005.
45. Song K, Wang D, Feng S, Yu G. Detecting opinion leader dynamically in chinese news comments. In: International confer-
ence on web-age information management. Springer; 2011, p. 197–209. https://doi.org/10.1007/978-3-642-28635-3_19.
46. Valente TW, Pumpuang P . Identifying opinion leaders to promote behavior change. Health Educ Behav. 2007;34(6):881–96.
https://doi.org/10.1177/1090198106297855.
47. Liu H, Yu X, Lu J. Identifying top-n opinion leaders on local social network. In: IET international conference on smart and
sustainable city 2013 (ICSSC 2013). IET; 2013, p. 325–328. https://doi.org/10.1049/cp.2013.1970.
48. Shafiq MZ, Ilyas MU, Liu AX, Radha H. Identifying leaders and followers in online social networks. IEEE J Sel Areas Commun.
2013;31(9):618–28. https://doi .org/10.110 9/JSAC.2013 .SUP .051 3054.
49. Gökçe OZ, Hatipoğlu E, Göktürk G, Luetgert B, Saygin Y. Twitter and politics: identifying Turkish opinion leaders in new
social media. Turk Stud. 2014;15(4):671–88. https://doi.org/10.1080/14683849.2014.985425.
50. Fan X, Zhang J, Wang X. Understanding social support and opinion leaders in a tuberculosis-related online community in
China: content and network analyses. JMIR Infodemiology. 2026;6:e79140. https://doi.org/10.2196/79140.
51. Cui L, Pi D. Identification of micro-blog opinion leaders based on user features and outbreak nodes. Int J Emerg Technol
Learn (iJET). 2017;12(01):141. https://doi.org/10.3991/ijet.v12i01.6139.
52. Chekkai N, Kheddouci H. Top-key influential nodes for opinion leaders identification in travel recommender systems.
In: Advances in model and data engineering in the digitalization era. Springer Nature Switzerland; 2022, p. 149—-161.
https://doi.org/10.1007/978-3-031-23119-3_11.
53. Hui Y, Chekol M, Wang S. Leveraging graph embedding for opinion leader detection in dynamic social networks. In: Artifi-
cial intelligence. ECAI 2023 international workshops. Springer Nature Switzerland; 2024, p. 5—-22.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 /
9 7 8 - 3 - 0 3 1 - 5 0 4 8 5 - 3 _ 1     .
54. Li R, Guo Q, Liu J. Leader-driven social network reconstruction. Chaos Interdiscip J Nonlinear Sci. 2026.  h t t p s : / / d o i . o r g / 1 0 . 1
0 6 3 / 5 . 0 3 0 2 6 3 9     .
55. Jain L, Katarya R. Discover opinion leader in online social network using firefly algorithm. Expert Syst Appl. 2019;122:1–15.
https://doi.org/10.1016/j.eswa.2018.12.043.
56. Chen Y-C, Hui L, Wu CI, Liu H-Y, Chen S-C, Opinion leaders discovery in dynamic social network. In: 2017 10th international
conference on Ubi-media computing and workshops (Ubi-Media). IEEE; 2017, p. 1–6.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / U M E D I A . 2 0 1
7 . 8 0 7 4 1 1 0     .
57. Semenkovich SA, Tsukanova OA. On the algorithms of identifying opinion leaders in social networks. Proc Comput Sci.
2019;162:778–85. https://doi.org/10.1016/j.procs.2019.12.050.
58. Furini M, Mariotti L, Martoglia R, Montangero M. A novel graph-based approach to identify opinion leaders in twitter. IEEE
Trans Comput Soc Syst. 2025;12(3):1268–78. https://doi.org/10.1109/tcss.2024.3455415.
59. Yang H, Liu Q, Ding X, Chen C, Wang L. Detecting local opinion leader in semantic social networks: a community-based
approach. Front Phys. 2022;10:858225. https://doi.org/10.3389/fphy.2022.858225.
60. Zhang B, Bai Y, Zhang Q, Lian J, Li M. An opinion-leader mining method in social networks with a phased-clustering
perspective. IEEE Access. 2020;8:31539–50. https://doi.org/10.1109/ACCESS.2020.2972997.
61. Huang W, Wang Y, Gan Z, Xi T, Xi J, Xu X, et al. An opinion leader mining method based on text contents and network
features. World Wide Web. 2025;28(2):21. https://doi.org/10.1007/s11280-025-01331-5.
62. Zhang C. Influence index evolution and empirical study of opinion leaders in Chinese social networks. J Inf Process Syst.
2025;21(1):28–42.
63. Haveliwala TH. Topic-sensitive pagerank. In: Proceedings of the 11th international conference on World Wide Web. ACM;
2002, p. 517—-526. https://doi.org/10.1145/511446.511513.
64. Song X, Chi Y, Hino K, Tseng B. Identifying opinion leaders in the blogosphere. In: Proceedings of the sixteenth ACM
conference on conference on information and knowledge management. 2007, p. 971–974.  h t t p s : / / d o i . o r g / 1 0 . 1 1 4 5 / 1 3 2 1 4
4 0 . 1 3 2 1 5 8 8     .
65. Weng J, Lim E-P , Jiang J, He Q. Twitterrank: finding topic-sensitive influential twitterers. In: Proceedings of the third ACM
international conference on web search and data mining. 2010, p. 261–270. https://doi.org/10.1145/1718487.1718520.

Page 33 of 34
Chebil et al. Discover Computing          (2026) 29:513
66. Chen Y, Wang X, Tang B, Xu R, Yuan B, Xiang X, Bu J. Identifying opinion leaders from online comments. In: Social media
processing: third national conference, SMP 2014, Beijing, China; November 1–2, 2014. Proceedings, Springer; 2014, p.
231–239. https://doi.org/10.1007/978-3-662-45558-6_21.
67. Zhou H, Zeng D, Zhang C, Finding leaders from opinion networks. In: 2009 IEEE international conference on intelligence
and security informatics. IEEE; 2009, p. 266–268. https://doi.org/10.1109/ISI.2009.5137323.
68. Luo L, Yang Y, Chen Z, Wei Y. Identifying opinion leaders with improved weighted Leaderrank in online learning communi-
ties. Int J Perform Eng. 2018;14(2):193. https://doi .org/10.239 40/ijpe.18. 02.p1.19 3201.
69. Alp ZZ. ˚U Gündüz Öğüdücü, identifying topical influencers on twitter based on user behavior and network topology.
Knowl-Based Syst. 2018;141:211–21. https://doi.org/10.1016/j.knosys.2017.11.021.
70. Zhu M, Lin X, Lu T, Wang H, Identification of opinion leaders in social networks based on sentiment analysis: Evidence
from an automotive forum. In: 2016 international conference on modeling, simulation and optimization technologies and
applications (MSOTA2016). Atlantis Press; 2016, p. 412–416. https://doi.org/10.2991/msota-16.2016.91.
71. Kempe D, Kleinberg J, Tardos É., Maximizing the spread of influence through a social network. In: Proceedings of the ninth
ACM SIGKDD international conference on Knowledge discovery and data mining. 2003, p. 137–146.  h t t p s : / / d o i . o r g / 1 0 . 1 1 4
5 / 9 5 6 7 5 0 . 9 5 6 7 6 9     .
72. Zhao Y, Li S, Jin F . Identification of influential nodes in social networks with community structure based on label propaga-
tion. Neurocomputing. 2016;210:34–44. https://doi.org/10.1016/j.neucom.2015.11.125.
73. Cho Y, Hwang J, Lee D. Identification of effective opinion leaders in the diffusion of technological innovation: a social
network approach. Technol Forecast Soc Chang. 2012;79(1):97–106. https://doi .org/10.101 6/j.techfor e.2011.0 6.003.
74. Xie M, Zhan X-X, Liu C, Zhang Z-K. An efficient adaptive degree-based heuristic algorithm for influence maximization in
hypergraphs. Inf Process Manag. 2023;60(2):103161. https://doi.org/10.1016/j.ipm.2022.103161.
75. Xie M, Liu C, Chen Y, Zhang Z, Liu X, Zhan X. A universal meta-heuristic framework for influence maximisation in hyper-
graphs. CAAI Trans Intell Technol. 2025;11(2):396–410. https://doi.org/10.1049/cit2.70082.
76. Chandola V, Banerjee A, Kumar V. Anomaly detection: a survey. ACM Comput Surv (CSUR). 2009;41(3):1–58.  h t t p s : / / d o i . o r g /
1 0 . 1 1 4 5 / 1 5 4 1 8 8 0 . 1 5 4 1 8 8 2     .
77. Guimera R, Amaral LAN. Cartography of complex networks: modules and universal roles. J Stat Mech: Theory Exp.
2005;2005(02):P02001. https://doi .org/10.108 8/1742-5468 /2005/02 /P02001.
78. Gagniuc P A. Markov chains: from theory to implementation and experimentation. Wiley; 2017.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 2 / 9 7
8 1 1 1 9 3 8 7 5 9 6     .
79. Amor BR, Vuik SI, Callahan R, Darzi A, Yaliraki SN, Barahona M. Community detection and role identification in directed
networks: understanding the twitter network of the care. Data debate. In: Dynamic networks and cyber-security. World
Scientific, United States; 2016, p. 111–136. https://doi.org/10.1142/9781786340757_0005.
80. Fang W, Gao B, Li N. Analysis of the influence of opinion leaders on public emergencies through microblogging. Open J
Soc Sci. 2020;8(5):154–8. https://doi.org/10.4236/jss.2020.85010.
81. Ellero A, Fasano G, Sorato A. Stochastic model of agent interaction with opinion leaders. Phys Rev E. 2013;87(4):042806.
https://doi.org/10.1103/PhysRevE.87.042806.
82. Galam S. Modelling rumors: the no plane pentagon French hoax case. XXPhys A. 2003;320:571–80.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6
/ S 0 3 7 8 - 4 3 7 1 ( 0 2 ) 0 1 5 8 2 - 0     .
83. Kumar S, Kumar A, Mallik A, Dhall S. Opinion leader detection in Asian social networks using modified spider monkey
optimization. ACM Trans Asian Low-Resour Lang Inf Process. 2023;22(5):1–26. https://doi.org/10.1145/3555311.
84. Zhang W, Li X, He H, Wang X. Identifying network public opinion leaders based on Markov logic networks. Sci World J.
2014;2014:1–8. https://doi.org/10.1155/2014/268592.
85. Chen Y-C. A novel algorithm for mining opinion leaders in social networks. World Wide Web. 2018;22(3):1279–95.  h t t p s : / / d
o i . o r g / 1 0 . 1 0 0 7 / s 1 1 2 8 0 - 0 1 8 - 0 5 8 6 - x     .
86. Chen Y-C, Cheng J-Y, Hsu H-H. A cluster-based opinion leader discovery in social network. In: Conference on technologies
and applications of artificial intelligence (TAAI). IEEE; 2016, vol. 2016, p. 78–83. https://doi.org/10.1109/TAAI.2016.7880184.
87. Duan J, Zeng J, Luo B. Identification of opinion leaders based on user clustering and sentiment analysis. In: IEEE/WIC/ACM
international joint conferences on web intelligence (WI) and intelligent agent technologies (IAT). IEEE; 2014, vol. 1, 2014, p.
377–83. https://doi.org/10.1109/WI-IAT.2014.59.
88. Zhai Y, Wang Z, Zeng H, Hu Z. Social media opinion leader identification based on sentiment analysis, in: Proceedings of
the 2021 International Conference on Bioinformatics and Intelligent Computing, 2021, pp. 436–440.  h t t p s : / / d o i . o r g / 1 0 . 1 1
4 5 / 3 4 4 8 7 4 8 . 3 4 4 8 8 1 6     .
89. Aleahmad A, Karisani P , Rahgozar M, Oroumchian F . Olfinder: Finding opinion leaders in online social networks. J Inf Sci.
2016;42(5):659–74. https://doi.org/10.1177/01655515156052.
90. Liu Y, Gu Z, Ko TH, Liu J. Identifying key opinion leaders in social media via modality-consistent harmonized discriminant
embedding. IEEE Transactions on Cybernetics. 2018;50(2):717–28. https://doi.org/10.1109/TCYB.2018.2871765.
91. Altinel AB, Hakkoz MA, Bozdag EB, Ganiz MC. Identifying topic-based opinion leaders in social networks by content and
user information. Int J Intell Syst Appl Eng. 2020;8(4):214–20. https://doi.org/10.18201/ijisae.2020466315.
92. Chebil M, Bach Tobji MA, Elmi S, Jallouli R. Selecting opinion leaders using skyline query (sol-sq): a new approach. Int J
Comput Appl. 2025. https://doi .org/10.108 0/1206212x. 2025.246 4554.
93. Chuang Y-S, Goyal A, Harlalka N, Suresh S, Hawkins R, Yang S, Shah D, Hu J, Rogers T. Simulating opinion dynamics with
networks of llm-based agents. In: Findings of the association for computational linguistics: NAACL 2024, Association for
Computational Linguistics; 2024, p. 3326—-3346. https://doi .org/10.186 53/v1/2024. findings -naacl.211.
94. Du S, Zhang X. Helmsman of the masses? evaluate the opinion leadership of large language models in the werewolf
game. 2024. arXiv preprint arXiv:2404.01602.
95. Al-yousef A, Mohawesh R, Saifan AA, Al-Shannaq MA. A self-supervised transformer framework for cross-domain fraudu-
lent review detection (cross-frd). J Supercomput. 2025. https://doi.org/10.1007/s11227-025-08061-5.
96. Mohawesh R, AlQarni AA, Alkhushayni SM, Daradkeh T, Bany SH. A new multilingual framework for fake reviews detection
based on a large language model. J Supercomput. 2025. https://doi.org/10.1007/s11227-025-07636-6.
97. Zhu Y. Public opinion evolution driven by large language models. Appl Comput Eng. 2026;225(1):55–62 (10.54254/2755-
2721/2026.ch32124).

Page 34 of 34
Chebil et al. Discover Computing          (2026) 29:513
98. Zhang H, Li J-L, Liu X-M, Dong C. Multi-dimensional feature fusion and stacking ensemble mechanism for network intru-
sion detection. Futur Gener Comput Syst. 2021;122:130–43. https://doi.org/10.1016/j.future.2021.03.024.
99. Xiao L, Li J, Xiao Y, Lv Z, Wang C, Li P . Reinforcement learning-based accurate worm detection for smart grids. IEEE Internet
Things J. 2025;12(17):36686–96. https://doi.org/10.1109/jiot.2025.3583379.
100. Chen Y. Dynamic identification and optimization of key opinion leaders in social networks using advanced gcn models. In:
5th international conference on machine learning and computer application (ICMLCA). 2024. p. 96–102.  h t t p s  : / / d o i  . o r g /  1 0
. 1  1 0 9 / i c m l c a 6 3 4 9 9 . 2 0 2 4 . 1 0 7 5 4 2 0 5     .
101. Jain L, Katarya R, Sachdeva S. Opinion leaders for information diffusion using graph neural network in online social net-
works. ACM Trans Web. 2023;17(2):1–37. https://doi.org/10.1145/3580516.
102. Nikseresht A. A hybrid game-theory and deep learning framework for predicting tourist arrivals via big data analytics and
opinion leader detection. 2025. arXiv preprint arXiv:2507.03411.
103. Sharma A, Ghose U. Lexicon a linguistic approach for sentiment classification. In: 2021 11th international conference on
cloud computing, data science & engineering (confluence). IEEE; 2021, p. 887–893.  h t t p s  : / / d o i  . o r g /  1 0 . 1  1 0 9 / c o n fl   u e n c e 5 1 6
4 8 . 2 0 2 1 . 9 3 7 7 0 5 7     .
104. Keyvanpour M, Karimi Zandian Z, Heidarypanah M. Omlml: a helpful opinion mining method based on lexicon and
machine learning in social networks. Soc Netw Anal Min. 2020;10(1):10. https://doi.org/10.1007/s13278-019-0622-6.
105. Almatarneh S, Gamallo P . A lexicon based method to search for extreme opinions. PLoS ONE. 2018;13(5):e0197816.  h t t p s : / /
d o i . o r g / 1 0 . 1 3 7 1 / j o u r n a l . p o n e . 0 1 9 7 8 1 6     .
106. Al-Otaibi S, Al-Rasheed AA, AlHazza B, Khan HA, AlShfloot G, AlFaris M, et al. Finding influential users in social networking
using sentiment analysis. Informatica. 2022. https://doi.org/10.31449/inf.v46i5.3829
107. Li C, Bai J, Zhang L, Tang H, Luo Y. Opinion community detection and opinion leader detection based on text information
and network topology in cloud environment. Inf Sci. 2019;504:61–83. https://doi.org/10.1016/j.ins.2019.06.060.
108. Cheng J, Danescu-Niculescu-Mizil C, Leskovec J. How community feedback shapes user behavior. In: Proceedings of the
international AAAI conference on web and social. media. 2014, vol. 8, p. 41–50.https://doi.org/10.48550/arXiv.1405.1429
109. Wang Y, Fikis DJ. Common core state standards on twitter: public sentiment and opinion leaders. Educ Policy.
2017;33(4):650–83. https://doi.org/10.1177/0895904817723739.
110. Jin B, Zou M, Wei Z, Guo W. How to find opinion leader on the online social network? Appl Intell. 2025;55(7):624.  h t t p s : / / d o
i . o r g / 1 0 . 1 0 0 7 / s 1 0 4 8 9 - 0 2 5 - 0 6 5 2 5 - y     .
111. Kang M, Liang T, Sun B, Mao H-Y. Detection of opinion leaders: static vs. dynamic evaluation in online learning communi-
ties. Heliyon. 2023;9(4):e14844. https://doi .org/10.101 6/j.heliyon .2023.e1 4844.
112. Chicco D, Warrens MJ, Jurman G. The Matthews correlation coefficient (mcc) is more informative than Cohen’s kappa and
brier score in binary classification assessment. IEEE Access. 2021;9:78368–81. https://doi.org/10.1109/access.2021.3084050.
113. Franzese M, Iuliano A, et al. Correlation analysis. In: Encyclopedia of bioinformatics and computational biology: ABC of
bioinformatics. Elsevier; 2018, Vol. 1, p. 706–721.
114. Ishfaq U, Khan HU, Iqbal K. Identifying the influential bloggers: a modular approach based on sentiment analysis. J Web
Eng. 2017;16(5):505–23.
115. Jaccard P . The distribution of the flora in the alpine zone. 1. New Phytol. 1912;11(2):37–50.  h t t    p  s :  /  / d   o i  . o  r g  /  1 0 .  1 1 1 1 / j . 1 4 6 9 - 8
1 3 7 . 1 9 1 2 . t b 0 5 6 1 1 . x     .
116. Ghorbani Z, Ghafouri S, Khasteh SH. Opinion leader detection in online social networks based on output and input links.
Wireless Pers Commun. 2024;138(2):1027–53. https://doi.org/10.1007/s11277-024-11544-y.
117. Ribeiro AC, Azevedo B, Oliveira e Sá J, Baptista AA. How to measure influence in social networks? In: International confer-
ence on research challenges in information science. Springer; 2020, p. 38–57.
118. Vieira VDF, Xavier CR, Ebecken NFF, Evsukoff AG. Performance evaluation of modularity based community detection
algorithms in large scale networks. Math Probl Eng. 2014;2014(1):502809. https://doi.org/10.1155/2014/502809.
119. Agarwal G, Kempe D. Modularity-maximizing graph communities via mathematical programming. Eur Phys J B.
2008;66(3):409–18. https://doi.org/10.1140/epjb/e2008-00425-1.
120. Newman MEJ, Girvan M. Finding and evaluating community structure in networks. Phys Rev E. 2004.  h t t p s : / / d o i . o r g / 1 0 . 1 1
0 3 / p h y s r e v e . 6 9 . 0 2 6 1 1 3     .
121. Chen Y-C, Zhu W-Y, Peng W-C, Lee W-C, Lee S-Y. Cim: Community-based influence maximization in social networks. ACM
Trans Intell Syst Technol (TIST). 2014;5(2):1–31. https://doi.org/10.1145/2532549.
122. Tsai H-T, Chen C-M, Liu C-Y. An automatic text annotation system to improve reading comprehension of chinese ancient
texts. In: 7th international congress on advanced applied informatics (IIAI-AAI). IEEE; 2018, vol. 2018, p. 176–81.  h t t p s : / / d o i .
o r g / 1 0 . 1 1 0 9 / i i a i - a a i . 2 0 1 8 . 0 0 0 4 2     .
Publisher's Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
