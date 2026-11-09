---
title: The Role of Social Support and Influencers in Social Media Communities
url: https://arxiv.org/abs/2410.04619
category: social-media
subcategory: empirical
date: 2024-10
venue: ''
authors:
- Junwei Su
- Peter Marbach
source: arxiv
pdf_url: https://arxiv.org/pdf/2410.04619
pages: 62
chars: 179041
fetched_at: '2026-11-08T13:02:06+00:00'
kb_version: 1
---

# The Role of Social Support and Influencers in Social Media Communities

arXiv:2410.04619v1  [cs.SI]  6 Oct 2024
The Role of Social Support and Influencers in Social Media Commu nities
JUNWEI SU, Department of Computer Science, University of Hong Kong
PETER MARBACH, Department of Computer Science, University of Toronto
ACM Reference Format:
Junwei Su and Peter Marbach. 2024. The Role of Social Support and I nﬂuencers in Social Media Communities. 1, 1 (October 2024),
62 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn
1 INTRODUCTION
How can individual agents or processes coordinate their act ions in a decentralized way to achieve a common goal?
This question is crucial across various systems—economic, technical, and sociological. In economic systems, it explores
how buyers and sellers coordinate their actions (buying and selling goods and services) to achieve eﬃcient market
outcomes and maximize social welfare. In technical systems , the focus is on algorithms for distributed systems, like
multi-agent AI [1, 2] and distributed computing [3], which e nable agents or processes to work together and optimize
system performance. In sociological systems, it examines how individuals within social groups coordinate their actions
to follow social norms and rules, ensuring the proper functi oning of the group [4–6].
All these three systems—economic, technical, and sociolog ical—face common challenges. First, scalability: in large
systems, agents cannot interact directly with all others, m aking it diﬃcult to determine which actions best contribute
to the shared objective. Second, heterogeneity: agents oft en have varying levels of information and resources, compli -
cating coordination in complex environments. Third, conﬂicting individual and collective goals: agents, while pursuing
their own interests, may not naturally align with the broade r objectives of the community.
Interestingly, economic systems, in the form of markets, oﬀ er an example of how these challenges can be overcome.
In economic markets, the three challenges are present in the following form: (a) scalability— individual buyers and
sellers do not interact with all actors in the market directl y; (b) heterogeneity—actors have diﬀerent interests and re -
sources; and (c) conﬂicting goals—each actor aims to maximi ze personal gain, such as proﬁt, rather than a collective
goal like social welfare. The mechanism that addresses thes e issues is the use of a common currency—money—which
enables buyers and sellers to coordinate their actions whil e pursuing individual goals. Buyers aim to maximize their
utility by purchasing goods that meet their needs, while sellers seek to maximize proﬁts by supplying products that sat-
isfy demand. This dynamic, famously described by Adam Smith ’s "invisible hand, " shows how self-interested behavior
can result in optimal societal outcomes, with goods produce d and consumed eﬃciently, maximizing overall welfare.
Authors’ addresses: Junwei Su, Department of Computer Science, University of Hong Kong; Peter Marbach, Department of Computer Science, University
of Toronto.
Permission to make digital or hard copies of all or part of thi s work for personal or classroom use is granted without fee pr ovided that copies are not
made or distributed for proﬁt or commercial advantage and that copies bear this notice and the full citation on the ﬁrst pa ge. Copyrights for components
of this work owned by others than ACM must be honored. Abstrac ting with credit is permitted. To copy otherwise, or republi sh, to post on servers or
to redistribute to lists, requires prior speciﬁc permissio n and/or a fee. Request permissions from permissions@acm.o rg.
© 2024 Association for Computing Machinery.
Manuscript submitted to ACM
Manuscript submitted to ACM 1

2 Junwei Su and Peter Marbach
This raises an intriguing question: Could similar mechanis ms, such as a common "currency" for coordination, be
applied to other systems? If so, what could this mechanism be that helps agents in technical and sociological contexts
overcome the challenges of scalability, heterogeneity, an d conﬂicting interests?
In this paper, we explore this question in the context of soci al media. Social media platforms have evolved into
dynamic environments where communities form around shared interests. Within these communities, individuals con-
tinuously make decisions about what content to post and shar e, aiming to engage the interests of the broader commu-
nity. This dynamic mirrors that of broader social systems, where individuals coordinate their actions toward achieving
common goals.
Using social media communities provides distinct advantag es when exploring how agents coordinate their actions
in a distributed environment. First, the actions and intera ctions within social media communities are well-deﬁned,
involving activities like posting and sharing content. Sec ond, user activities on social media platforms can be access ed
and analyzed, allowing us to empirically test the theoretic al results presented in this paper. Finally, we believe that the
insights obtained from analyzing social media communities can be extended and applied to more general sociological
systems, as well as technical systems such as multi-agent AI systems, as we discuss further in Section 13.
In our analysis of social media communities, we ﬁrst investi gate whether there is an equivalent to money in eco-
nomic markets—a "currency" that coordinates actions in onl ine communities—and whether it can be formalized. We
propose that social support serves this role. On social medi a platforms, social support manifests in various forms,
such as likes, shares, comments, and retweets. These action s reﬂect approval, engagement, and validation from other
community members.
Social support serves two key purposes in these communities . First, it acts as a reward system for content creators,
guiding them on what type of content to produce in order to max imize their reach and reputation. Second, like money
in traditional markets, social support signals the perceiv ed value of content. Content that is considered more valuabl e
by the community will naturally receive more social support . These observations suggest that social support functions
similarly to a common currency in an economic market. In the f ollowing sections, we formalize this intuition by
examining whether social support can be treated as a currenc y within a content market and how it impacts market
equilibrium.
We also study the role of inﬂuencers in helping individuals coordinate their actions within social media communities.
Inﬂuencers are users with a large number of followers who curate, amplify, and share content, thus playing a signiﬁcant
role in shaping the ﬂow of information within the community. While the role of inﬂuencers as content aggregators is
widely recognized, their inﬂuence on content creation and s haring within these communities is less explored. In this
paper, we investigate whether and how inﬂuencers shape the t ypes of content that are created within social media
communities.
In summary, we analyze the following central questions:
1) Social Support as a Currency: Can social support be accura tely characterized as a currency in content markets
that shapes the actions of individual agents, such as the con tent that is produced and shared within the commu-
nity? If so, how eﬃcient is social support in shaping the acti ons of individual agents, i.e. what is the resulting
social welfare?
2) The Role of Inﬂuencers: Do inﬂuencers impact the actions o f individual agents, particularly the content that is
produced and shared within the community, and if so, how?
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 3
To do that, we model an online community as a content market wh ere agents post (produce), consume (read), and
share content. We distinguish between two types of agents: c ommunity members who create and consume content,
and inﬂuencers who aggregate content for the community. We a ssume that agents act selﬁshly and aim to achieve
their own objectives. We model the objectives and actions of these agents in the content market as follows,
(1) The objective of content consumers is to obtain content t hat is of interest to them. To achieve this goal, content
consumers can follow other community members (content prod ucers) as well as inﬂuencers. We assume that
consumers have limited resources (limited attention) to fo llow content producers and inﬂuencers, and hence
strategically decide who they follow, and how much social su pport they allocate to each agent they follow.
(2) The objective of content producers is to create content t o maximize the social support that they receive, i.e. to
maximize the total number of likes or shares that their conte nt receives.
(3) The objective of inﬂuencers is to attract as many followe rs as possible. To achieve this goal, inﬂuencers aim
at maximizing the social support that they receive from thei r followers by curating (sharing) content that is of
interest to their followers [7–9].
Agents aiming to achieve their own objectives leads to a game (strategic interaction) between content consumers,
producers, and inﬂuencers, for which we study the existence and eﬃciency of a Nash equilibrium.
More precisely, we study the existence and eﬃciency of a Nash equilibrium for two scenarios. First, we assume that
all agents have perfect information, meaning they know the a ctions and preferences (utilities) of all other agents. Thi s
scenario allows us to examine and characterize the market ou tcome, speciﬁcally the equilibrium and social welfare,
for an idealized market with perfect information.
Next, we consider the more realistic case where agents do not have perfect information. In this scenario, content
producers cannot observe the actions of all content consume rs and, therefore, cannot directly assess the social suppor t
they receive from them. Instead, content producers rely on t he social support garnered by inﬂuencers to determine
which content to create. We study how much the social welfare under imperfect information deviates from that of the
idealized market with perfect information.
Through this analysis, we aim to provide insights into the fu nctioning of social support as a currency in content
markets and the dual role of inﬂuencers as both content aggre gators and information proxies. The main results and
insights of our analysis are as follows.
Social Support as a Currency : We formalize how social support operates as a currency. In p articular, we derive a
parallel between how social support works in a content marke t, and how money works in a market economy. Similar
to a market economy, where one observes a ﬂow of money in one direction and a ﬂow of goods in the opposite direction,
in a content market there is a ﬂow of social support in one dire ction, and a ﬂow of content in the other direction. The
ﬂow of social support goes from the content consumers to the i nﬂuencer, and from there to the content producers. The
ﬂow of content goes from the content producers to the inﬂuenc er, and from there to the content consumers. Similar
to a market economy where money signals the utility of a good, social support signals the utility of content. The
social support given by a content consumer to the content sha red by the inﬂuencer signals the (personal) utility of
this content to the consumer. The social support given by the inﬂuencer to content created by a producer signals the
(aggregated) utility to the content market.
The Role of Inﬂuencers : Inﬂuencers play two important roles in the content market. First, as they aggregate content
that is of interest to their followers, inﬂuencers help cont ent consumers to easily ﬁnd content that is of interest to
them. This role of inﬂuencers is well understood. However, i nﬂuencers play another important role: they serve as
Manuscript submitted to ACM

4 Junwei Su and Peter Marbach
an information proxy for content producers. In the case of a l arge content market, where it is too costly for content
producers to follow all content consumers in order to obtain the necessary information to decide which type of content
to create, producers can use inﬂuencers as a proxy for this information. That is, they can use the social support received
by an inﬂuencer as a proxy about the total social support they receive from the content consumers. To the best of our
knowledge, this role of inﬂuencers has not been formally cha racterized in literature.
Price of Inﬂuence : For the scenario where all agents in the content market have perfect information, we show there
exists an eﬃcient Nash equilibrium that maximizes social we lfare. This result suggests that using social support as a
currency can lead to an eﬃcient market outcome (equilibrium ). However, for the scenario where content producers
have limited information, this is no longer the case. That is , using an inﬂuencer as a proxy to obtain information about
the social support of content generally leads to suboptimal decisions by the content producers. These suboptimal
decisions lead to a reduction in the social welfare compared with the scenario where agents have perfect information.
We refer to the reduction of the social welfare as the price of inﬂuence. A surprising result that we obtain is that (under
suitable conditions) the price of inﬂuence becomes small in large content markets (with a large number of content
producers and consumers). This suggests using an inﬂuencer as an information proxy leads to a (near) optimal social
welfare in the case of a large content market.
In summary, our analysis shows that social support function s as an eﬀective mechanism for agents to coordinate
their actions, addressing three key challenges:
(1) Scale, where agents interact with only a limited number of others,
(2) Heterogeneity, where agents diﬀer in their interests and objectives, and
(3) Conﬂicting Interests, where agents aim to optimize their individual objectives.
More speciﬁcally, our analysis demonstrates that social su pport not only helps overcome these challenges but also
results in a coordination mechanism that is:
a) Simple and easily implementable, as agents can rely solel y on social support to guide their actions, and
b) Highly eﬃcient, leading to actions that (nearly) maximiz e social welfare, particularly in large communities.
Returning to our initial question of how agents can coordinate their actions to achieve a shared objective in a distributed
environment, it is natural to consider whether social suppo rt as a coordination mechanism can be applied to more
general multi-agent systems. We believe this is indeed the c ase, and that the results and insights from this analysis
can be extended and applied to broader sociological and tech nical systems, including multi-agent AI systems. This is
a research direction we are actively pursuing and will explo re further in Section 13.
The rest of the paper is organized as follows. In Section 2, we provide an overview of related literature. In Section 3,
we provide an overview of the model that we use for our analysis, and in Section 4 - 6, we provide the formal deﬁnition
of the model. In Section 7 - 8, we model and analyze the case of a content market with perfect information. In Section 9 -
10, we extend the analysis to the case where agents have limit ed information. In Section 12, we provide a discussion
of the results that we obtain, and the insights they provide i nto the questions that we study. In Section 13, we discuss
possible directions for future research.
2 RELATED WORK
In this section we provide an overview of existing literatur e that is relevant to our analysis. This includes modeling
social media as an attention and inﬂuence economy, research on inﬂuence in economic and sociological theory, as well
as research on attention, inﬂuence, and content aggregatio n in social media,
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 5
2.1 A/t_tention Economy and Influence Economy
The activities on social media have been modeled as an attent ion economy [10], where agents aim to maximize and
monetize the attention they receive, and as an inﬂuence econ omy, where inﬂuencers use their received attention to
shape the opinions of their followers, promote products or s ervices, and generate income.
2.1.1 A/t_tention Economy. The attention economy refers to the economic model centered around capturing and mon-
etizing users’ attention on digital platforms, particular ly social media [10]. Attention is considered a scarce resou rce,
and various entities compete to gain users’ limited attenti on. Social media platforms, advertisers, and content creat ors
strive to engage users and keep them active on the platform fo r longer periods to maximize revenue through adver-
tisements, sponsored content, subscriptions, and other mo netization methods. Platforms and advertisers track metri cs
(attention-based outcomes) such as views, likes, shares, c lick-through rates, and time spent on content to assess and
optimize engagement levels.
The model and analysis that we carry out reﬂect this economic model of social media where we assume that a)
attention is a limited resource, and b) agents use attention -based outcomes (to which we refer as social support) to
maximize the attention they obtain.
2.1.2 Influence Economy. The inﬂuence economy refers to the system and dynamics surro unding social media plat-
forms, where inﬂuencers leverage their online presence and following to shape opinions, promote products or services,
and generate income. Inﬂuencers have the ability to inﬂuenc e their audience’s behavior, choices, and preferences
through content creation, endorsements, and collaboratio ns. Advertisers and brands collaborate with inﬂuencers to
reach a highly targeted and engaged audience, utilizing spo nsored content, aﬃliate marketing, brand partnerships,
and inﬂuencer marketing campaigns.
While we also study the role of inﬂuencers and inﬂuence, the f ocus of our analysis diﬀers from the one of the
inﬂuence economy. Instead of studying how inﬂuencers use th eir received attention to shape opinions and generate
income, we focus on how the social support of content consumers shapes the content shared by inﬂuencers and how the
social support of inﬂuencers shapes the content created by c ontent producers. Our analysis provides a complementary
view of inﬂuence activities in social media, focusing on the ﬂow of inﬂuence from content consumers to inﬂuencers
and from inﬂuencers to content producers.
2.1.3 A/t_tention vs Social Support. Similar to an attention economy, attention and social suppo rt are distinct concepts
in our model. Attention refers to the attention one agent pay s to another, while social support represents observable
actions such as likes, shares, and clicks. Attention itself might not be directly observable, whereas social support ca n
be measured. We provide a formal deﬁnition of how we model att ention and social support in Section 4 and 6.
2.2 Influence
Our focus on whether social support can be considered a curre ncy and the role of inﬂuencers aligns with research
questions studied in economic and sociological theory.
2.2.1 Influence and Information Asymmetry. Milgrom and Roberts present in [11] a formal economic model to analyze
inﬂuence activities within organizations, including lobbying, campaigning, and persuasion. They use game theory and
agency theory to study how individuals strategically use in ﬂuence tactics to shape decision-making processes and
outcomes. Information asymmetry plays a crucial role in the emergence of inﬂuence activities in their model.
Manuscript submitted to ACM

6 Junwei Su and Peter Marbach
Our approach shares several similarities with the researchpresented in Milgrom and Roberts [11]. First, they develop
a formal model that integrates economic principles, game th eory, and agency theory to investigate inﬂuence activities .
Second, they model inﬂuence as a strategic interaction amon g actors who possess diverse information, preferences,
and incentives. Thirdly, they emphasize the signiﬁcance of information asymmetry as a fundamental factor leading to
the emergence of inﬂuence and inﬂuence activities within a s ocial system.
Nevertheless, there are notable distinctions between our approach and that of Milgrom and Roberts [11]. First, while
Milgrom and Roberts focus on how individuals endeavor to inﬂ uence decision-makers, within the context of a content
market, this corresponds to how content consumers shape the actions of inﬂuencers. In our analysis, we not only
consider how content consumers inﬂuence the decisions of in ﬂuencers but also how inﬂuencers impact the decisions
of content producers.
Second, we employ a diﬀerent approach regarding how actors are rewarded. Speciﬁcally, we assume that the reward
system manifests as social support, such as likes and retweets, and examine the outcomes when actors seek to optimize
social support. In Milgrom and Roberts [11], the reward system is not predetermined but rather the focus of the analysis.
In other words, the aim of Milgrom and Roberts is to design a re ward system within an organization that encourages
inﬂuence activities beneﬁting the organization while disc ouraging costly inﬂuence activities. Conversely, our analysis
demonstrates that social support as a reward yields a (near) optimal social welfare outcome. The primary objective of
Milgrom and Roberts is not to identify a mechanism that optim izes social welfare but rather to determine the "best"
outcome within a given class of mechanisms, which may still b e suboptimal.
2.2.2 Parsons’ Hypothesis. The sociologist Talcott Parsons proposed in the 1960s that s imilar to money which signals
the utility of goods and services in a market, inﬂuence is use d to signal the utility of social actions and opinions in
a social group [12]. As such, inﬂuence and money are both used to facilitate interactions of agents. Money facilitates
interactions between economic agents, whereas inﬂuence fa cilitates interactions between social agents. If true, thi s
hypothesis would have important implications, providing a formal foundation for studying inﬂuence in a social system,
creating a link to economic theory, and allowing us to levera ge existing results and techniques in economic theory to
study inﬂuence in a social system. However, the hypothesis was never formally or experimentally veriﬁed or disproved.
While we focus in this paper on social media, we believe that o ur results and insights might extend to more general
social systems. In particular, we believe that the model and analysis of this paper can be used to formally study Par-
sons’ hypothesis. A detailed discussion of this is outside t he scope of this paper, and is research that we are currently
undertaking.
2.3 Influence, A/t_tention and Content Aggregation in Social M edia
Our model and analysis are closely related to studies on inﬂu ence, attention, and content aggregation in social media.
2.3.1 Influence. The emergence of social media and the need to comprehend its i mpact on the social structure, as well
as the beliefs and actions of individuals, have led to the dev elopment of a formal study of inﬂuence in social media.
Extensive literature exists on this topic, including measu ring inﬂuence and identifying inﬂuential users (see [13] fo r a
survey), using models to understand the spread of content (s ee [14] for a survey), and maximizing inﬂuence (see [15]
for a survey).
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 7
Of particular relevance to our approach and analysis are cas cade models, which are employed to model inﬂuence in
social networks and social media [14]. These models capture the propagation of content through a social network by as-
suming that individuals share a given content from their connections with a certain probability. Typically, these models
incorporate factors such as tie strength or network prevale nce to determine the probability of content sharing [14].
Cascade models focus on characterizing how a behavior or bel ief spreads across a ﬁxed social network topology
with ﬁxed sharing probabilities. In contrast, our model and analysis allow for variable topology and sharing probabili -
ties, which are outcomes of the strategic interactions betw een content consumers, content producers, and inﬂuencers.
However, there is an interesting connection between cascad e models and our paper’s analysis and results. Speciﬁcally,
our model and analysis provide insights into the interpreta tion and generation of sharing probabilities in social me-
dia, demonstrating that these probabilities can represent the social support paid by one actor to another. Moreover,
the social support exchanged between agents is a result of th e strategic interactions among content producers, con-
tent consumers, and inﬂuencers. Examples of cascade models include the well-known the independent cascade model
(ICM) [16] and linear threshold model (LTM) [17].
Cascade models focus on characterizing how a behavior or bel ief spreads across a ﬁxed social network topology
with ﬁxed sharing probabilities. In contrast, our model and analysis allow for variable topology and sharing probabili -
ties, which are outcomes of the strategic interactions betw een content consumers, content producers, and inﬂuencers.
However, there is an interesting connection between cascad e models and our paper’s analysis and results. Speciﬁcally,
our model and analysis provide insights into the interpreta tion and generation of sharing probabilities in social medi a,
demonstrating that these probabilities can represent the s ocial support paid by one actor to another. Moreover, the
social support exchanged between agents is a result of the st rategic interactions among content producers, content
consumers, and inﬂuencers.
2.3.2 A/t_tention. Research on attention in social media includes studies of th e dynamics of attention [18, 19], using
attention for marketing [20], and the attention economy [10 , 21]. Formal studies of attention include the model and
results presented by Goel and Ronaghi [22], Borgs et al. [23] , and Ghosh and McAfee [24]. These studies adopt a game-
theoretic approach to characterize attention in social med ia, although they diﬀer in how they deﬁne the utility derived
from attention. For instance [22], attention may be interpr eted as the following rate, the number of followers a user
has [23], or the publication of content [24].
These attention models share similarities with our approac h in terms of adopting a game-theoretic perspective
to study attention. However, they diﬀer in two fundamental a spects. First, they assume that content producers do
not make strategic decisions regarding the type of content t hey produce, whereas our analysis considers strategic
decision-making by content producers. Second, these model s do not assume the existence of an inﬂuencer but rather
direct following relationships between content consumers and producers.
2.3.3 Content Aggregation. The problem we study bears resemblance to research on content aggregation for news and
blog posts, with inﬂuencers acting as content aggregators. Existing studies on content aggregation directly relevant to
our work include the following.
Jordan et al. study in [8] how content aggregators decide on t he topics for which they curate content, and users
decide on which content aggregator to follow. They formulate this interaction as a "location game" in which the chosen
location of an aggregator represents the curated content’s topic.
May et al. study in [25] the interaction between bloggers and users (blog readers), where bloggers decide on which
news items to post, and users decide on which bloggers to follow. The bloggers’ objective is to gather as many followers
Manuscript submitted to ACM

8 Junwei Su and Peter Marbach
as possible. Their study demonstrates that this "blog-posi tioning game" can result in "eﬃcient" equilibria, where use rs
generally receive the content of their interest. The model p resented in [25] can be interpreted as a "location game"
similar to the one studied in [8].
Dellarocas et al. study in [7] the competition between content creators on the World Wide Web (WWW). Speciﬁcally,
they analyze how the linking ability of content creators to other web pages aﬀects the strategic interaction among them.
The content creators, who curate content from web pages, cor respond to the inﬂuencer in our model.
Our model and analysis diﬀer from these studies in two key asp ects. First, the game we study does not follow the
framework of a location game, rendering the analysis conducted in [8] inapplicable to our model. Second, we model and
analyze the strategic interaction between a single inﬂuenc er and a large number of content consumers and producers.
In contrast, [7] examines the strategic interaction (compe tition) among multiple inﬂuencers.
2.3.4 Discussion. Our model and analysis of the role of social support and inﬂue ncers includes all aspects of the
above literature as it incorporates cascades (through the connection between the ﬂow of attention and ﬂow of content),
attention, social support, and content aggregation and recommendation (through the inﬂuencer). This has the following
implications. First, our model and analysis shows that thes e ideas concepts (cascades, attention and social support,
and content aggregation) are related; each explaining a spe ciﬁc aspect of a social media community, and combined
providing a comprehensive understanding of the role of soci al support and inﬂuence, in social media. Second, as our
model combines all of these concepts, one would expect the re sulting model to be more complex compared with the
exisiting models in the literature. This is indeed the case ( see Section 3 - 7). Third, one would then expect that the
model leads to more complicated results. Surprisingly this is not the case, as the statements of our results in Section 8
and Section 10 turn out to be concise, and have intuitive inte rpretations. We discuss this in more detail in Section 12.
3 SOCIAL MEDIA COMMUNITY AS A CONTENT MARKET
In this section, we provide an overview of the model and research questions considered in this paper. The mathematical
formulation of the model is detailed in Sections 4 - 6.
We model a social media community as a content market consist ing of two types of agents: community members
and inﬂuencers. Community members serve as both content con sumers and producers; they post (produce) and read
(consume) content. Inﬂuencers, by contrast, primarily act as content aggregators, gathering content from the com-
munity and making it accessible to all members. While our mod el can be extended to include inﬂuencers as content
producers, this does not impact the key results and insights of our analysis.
For instance, on X (formerly Twitter), users join communities to post and engage with content of interest. Inﬂuencers,
in turn, collect and share content to attract and engage thei r followers.
The two key concepts that we use in our model are:
a) Following Rate: Social media users follow others to recei ve their content, and the amount of attention they
allocate to those they follow reﬂects their level of interes t. This attention inﬂuences not only how often a user
checks the content but also how carefully they read and engag e with it. In our analysis, we use the following
rate to model this attention. A higher following rate corres ponds to greater attention, indicating more frequent
content checks, and shorter delays in receiving new content . We formally deﬁne following rates in Section 4
and discuss their impact on the delay in receiving content in Section 5.
b) Social Support: In addition to following, users engage wi th content through actions such as sharing (retweeting),
liking, or commenting. These actions provide feedback on ho w interesting or useful the content is, which we
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 9
refer to as social support. We assume that higher levels of so cial support—measured by the number of shares,
likes, and comments—indicate greater community interest i n the content.
Using following rates and social support, we model social me dia communities as a content market, as explained
below.
3.1 Model of Content Market
The actions and objectives of the agents in the content marke t are as follows. Community members, acting as content
consumers, aim to obtain content that interests them. They a chieve this by following inﬂuencers or other community
members (content producers). Additionally, they can acqui re content from sources outside the community, such as
other communities, social media platforms, and websites. C ontent consumers decide on the following rate (attention)
they allocate to inﬂuencers, content producers, and extern al sources. We assume that following rate (attention) is a
scarce resource, and each consumer has a limit on the total fo llowing rate they can allocate. Furthermore, content
consumers provide feedback on content, signaling its utili ty through actions like ’likes’ or sharing (retweeting). Th is
feedback, referred to as social support, indicates the valu e or interest of the content to the community.
As content producers, community members decide on the type o f content to produce. Their goal is to create content
that maximizes the social support (likes, retweets, etc.) r eceived within the community.
The actions of inﬂuencers are similar to those of content con sumers. Inﬂuencers decide which content producers
to follow and the amount of following rate (attention) to all ocate to each. Like content consumers, the following
rate (attention) is a limited resource for inﬂuencers, and t hey have a constraint on the total following rate they can
allocate. However, while content consumers make these decisions to maximize their personal utility, inﬂuencers aim to
aggregate content and attract as many followers as possible . They achieve this by maximizing the social support they
receive from their followers. Since content consumers can also follow other members and external sources, inﬂuencers
face competition for their attention. To achieve their goal s, inﬂuencers can share (retweet) content from the producer s
they follow. We assume that the probability of an inﬂuencer s haring content depends on the following rate allocated
to that producer. In other words, if an inﬂuencer follows a co ntent producer with a high following rate, they are more
likely to share that producer’s content. We interpret this s haring as the social support that the inﬂuencer provides to
the content producer.
In summary, the modeling assumptions that we make for the con tent market that we study are as follows.
(1) Objective of Content Consumers: Content consumers aim to maximize the utility of the content that they receive.
(2) Social Support by Content Consumers: Content consumers are more likely to provide social support for a content
item that provides them a high utility.
(3) Objective of Content Producers: Content producers aim to maximize the social support that th ey receive in the
community.
(4) Objective of Inﬂuencers: The objective of the inﬂuencer is to obtain as much social sup port as possible from their
followers.
(5) Social Support by Inﬂuencers: Inﬂuencers are more likely to provide social support to a con tent item of a com-
munity member that they follow with a high rate.
(6) Following Rate as a Limited Resource: Content consumers and inﬂuencers have a limit (bound) on the total rate
(attention) with which they can follow inﬂuencers and other community members. Similarly, inﬂuencers have
a limit (bound) on the total rate (attention) with which they can follow community members.
Manuscript submitted to ACM

10 Junwei Su and Peter Marbach
3.2 Terminology: Content Consumers and Content Producers
Throughout the paper, we use the following terminology: When discussing the actions of a community member focused
on obtaining content, we refer to that member as a "content co nsumer. " Conversely, when focusing on a community
member’s actions related to creating content, we refer to th at member as a "content producer. " This terminology helps
clearly distinguish between the two primary activities of c ommunity members: consuming and producing content.
3.3 Discussion
Before presenting the mathematical model for the content ma rket, we will discuss the realism and validity of our
modeling assumptions.
We believe that the assumption of a limited following rate (a ttention) is both valid and realistic. This assumption
aligns with observations in the attention economy [10]. Sim ilarly, our assumptions about the objectives of content
consumers, content producers, and inﬂuencers are intuitive and reﬂect the key motivations of agents within the content
market. For instance, social support serves as a measurable metric for content producers and inﬂuencers to optimize
their decisions and assess performance.
However, it is important to acknowledge that some assumptions regarding social support are idealized and may not
perfectly align with reality. For example, while we assume t hat social support reﬂects the utility of content, there may
be other reasons for providing social support beyond utilit y. Thus, the model represents an idealized content market
where social support directly correlates with utility. Fut ure research could extend this model to scenarios where soci al
support does not necessarily reﬂect utility, exploring how such variations might aﬀect market equilibrium and social
welfare. We discuss these potential extensions in more deta il in Section 13, including their implications for studying
social media algorithms, such as content recommendation sy stems.
4 MATHEMATICAL MODEL
In this section, we formally deﬁne the model outlined in Sect ion 3. We begin by specifying the content topics that
interest content consumers. While we assume that content co nsumers share a common set of topics; however, they
diﬀer in their primary interest (i.e., their most favored to pic). Additionally, we assume that content producers vary i n
their ability to create content on diﬀerent topics.
Using the model of this section, we formally deﬁne the utilit ies that content consumers obtain in Section 5. In
Section 6 we formally deﬁne our model of social support. In Se ction 7 we deﬁne the objectives of inﬂuencers, content
consumers, and content producers, as maximization problem s.
Our analysis focuses on a content market with a single inﬂuen cer. However, the model can be extended to include
multiple inﬂuencers without qualitatively altering the re sults and insights of the analysis. In the following, we de-
note the set of community members by 𝐶 and the inﬂuencer by /u1D466.altinﬂ. Furthermore, we denote with 𝑁 the size of the
community 𝐶, i.e. number of community members in 𝐶.
4.1 Topics of Interest to Community
The content market is deﬁned by a set of content topicsT that are of interest to the content consumers. In the following,
we assume that each content item 𝑥 that is created by a content producer is on one of the topics in T . In addition, we
assume that there exists a "measure" that characterizes how closely two content topics are related. More precisely, we
assume that the set of topics T is given by a compact metric space.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 11
A/s.sc/s.sc/u.sc/m.sc/p.sc/t.sc/i.sc/o.sc/n.sc 1. The set T of content topics that are of interest to the community is giv en by a non-empty convex and
compact metric space.
We denote the distance between two topics 𝑥, 𝑥′ ∈ T as 𝑑 (𝑥, 𝑥′). An example of such is given by a bounded subset
T of R𝑁 , i.e. we have that T ⊂ R𝑁 . In this case, we can think of 𝑥 ∈ T as a vector of 𝑁 features that characterize the
content topic.
Assumption 1 serves both technical and intuitive purposes. Technically, it ensures that there is a solution to the
agents’ optimization problems within our analysis. Intuit ively, it implies that the social media community has a coher -
ent focus on the topics of interest, reﬂecting a shared thema tic orientation among community members.
4.2 Main Interest of Community Members
For our analysis, we assume that each community member (content consumer and producer) has a main interest /u1D466.alt ∈ T
which is the content topic of greatest interest to them. We id entify a community member by its main interest /u1D466.alt ∈ T .
As a content consumer, the probability that a community memb er /u1D466.alt will be interested in a content item of topic 𝑥
is given by
𝑝 (𝑥 |/u1D466.alt) = 𝑓 (𝑑 (𝑥, /u1D466.alt)), 𝑥, /u1D466.alt ∈ T , (1)
where 𝑑 (𝑥, /u1D466.alt) is the distance between the main interest /u1D466.alt and the content topic 𝑥, and 𝑓 : R+ /u\i∈∞A6.e\dl→ [ 0, 1], R+ = {𝑥 ∈ R :
𝑥 ≥ 0}, is a decreasing function. This implies that community memb er /u1D466.alt is more interested in content that is close to
its main interest /u1D466.alt.
As a content producer, the ability of community member /u1D466.alt to produce content on topic 𝑥 is represented by
𝑞(𝑥 |/u1D466.alt) = 𝑔(𝑑 (𝑥, /u1D466.alt)), 𝑥, /u1D466.alt ∈ T , (2)
where 𝑔 : R+ /u\i∈∞A6.e\dl→ [ 0, 1] is again a decreasing function. The interpretation of this f unction is as follows. If producer /u1D466.alt
creates a content item on topic 𝑥, then this content item will be relevant to topic 𝑥 with probability 𝑞(𝑥 |/u1D466.alt) given by
Eq. (2). As the function 𝑔 is decreasing, content producers are better at producing co ntent that is close to their main
interest.
For our analysis, we make the following assumptions for the t wo function 𝑓 and 𝑔.
A/s.sc/s.sc/u.sc/m.sc/p.sc/t.sc/i.sc/o.sc/n.sc 2. The functions 𝑓 : R+ /u\i∈∞A6.e\dl→ [ 0, 1] and 𝑔 : R+ /u\i∈∞A6.e\dl→ [ 0, 1] are continuous and strictly decreasing.
The following result shows that, under Assumption 1 and 2, th e topics 𝑥 ∈ T represent shared interests among
community members /u1D466.alt ∈ 𝐶, where each member has a positive probability of being inter ested in a topic 𝑥 and a
positive probability of being able to create content releva nt to that topic.
L/e.sc/m.sc/m.sc/a.sc 1. There exists a 𝑝min > 0 and 𝑞min > 0 such that
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑝min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T
and
𝑞(𝑥 |/u1D466.alt) ≥ 𝑞min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T .
P/r.sc/o.sc/o.sc/f.sc. Recall that we have that
𝑝 (𝑥 |/u1D466.alt) = 𝑓 (𝑑 (𝑥, /u1D466.alt)), 𝑥, /u1D466.alt ∈ T ,
and
𝑞(𝑥 |/u1D466.alt) = 𝑔(𝑑 (𝑥, /u1D466.alt)), 𝑥, /u1D466.alt ∈ T .
Manuscript submitted to ACM

12 Junwei Su and Peter Marbach
By Assumption 1 we have that the metric space T is compact, and it follows that there exists a 𝑏0 such that
𝑑 (𝑧, /u1D466.alt) ≤ 𝑏0, 𝑥, /u1D466.alt ∈ T .
Furthermore, by Assumption 2 we have that the functions 𝑓 and 𝑔 are decreasing with
𝑓 (𝑥) > 0, 𝑥 ∈ R+,
and
𝑔(𝑥) > 0, 𝑥 ∈ R+.
It then follows that for
𝑝min = 𝑓 (𝑏0)
and
𝑞min = 𝑔(𝑏0),
we have that
𝑝min > 0
and
𝑞min > 0,
as well as
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑝min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T
and
𝑞(𝑥 |/u1D466.alt) ≥ 𝑞min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T .
This establishes the result of the lemma. □
4.3 Content Created by Content Producers
Each content producer /u1D466.alt ∈ 𝐶 in the community decides on the topic of content they create, denoted as 𝑥 (/u1D466.alt) ∈ T , where
T is the set of all possible content topics. The content produc tion decision of each content producer /u1D466.alt ∈ 𝐶 is strategic,
and they aim to select a topic 𝑥 (/u1D466.alt) that will attract the maximum social support from both conte nt consumers and
inﬂuencers. We deﬁne the corresponding (utility) optimiza tion problem in Section 7.
We then deﬁne the overall content production 𝑋 of all producers as
𝑋 = (𝑥 (/u1D466.alt))/u1D466.alt ∈𝐶
where 𝐶 is the set of all content producers.
4.4 Following Rates of Content Consumers
To obtain content of interest, content consumers can follow content producers, the inﬂuencer, and sources outside the
community. They can also determine the rate at which they fol low these entities. Formally, we deﬁne the following
rates for a content consumer /u1D466.alt ∈ 𝐶 as follows:
Let 𝜇 (𝑧|/u1D466.alt) be the rate with which content consumer /u1D466.alt follows content producer 𝑧, and let
𝜇 (/u1D466.alt) = (𝜇 (𝑧|/u1D466.alt))𝑧 ∈𝐶\{ /u1D466.alt }
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 13
be the rate allocation vector of content consumer/u1D466.alt ∈ 𝐶. Similarly, let 𝜇 (/u1D466.altinﬂ|/u1D466.alt) be the rate with which content consumer
/u1D466.alt follows the inﬂuencer /u1D466.altinﬂ. Finally, let𝜆(/u1D466.alt) be the rate with which content consumer/u1D466.alt follows content sources outside
the community. The overall rate allocation of a content cons umer /u1D466.alt is then given by
Λ(/u1D466.alt) = (𝜇 (/u1D466.alt), 𝜇(/u1D466.altinﬂ|/u1D466.alt), 𝜆(/u1D466.alt)),
and the overall rate allocation of all content consumers is g iven by
Λ = (Λ(/u1D466.alt))/u1D466.alt ∈𝐶 .
We deﬁne in Section 5 the utility obtained by content consume r /u1D466.alt under an allocation Λ(/u1D466.alt). We refer to this utility
as the content consumption utility.
We assume that there is a bound 𝑀 > 0 on the total rate that a content consumer can allocate, and w e have that
𝜇 (/u1D466.altinﬂ|/u1D466.alt) + 𝜆(/u1D466.alt) +
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇 (𝑧|/u1D466.alt) ≤ 𝑀, /u1D466.alt ∈ 𝐶.
We refer to 𝑀 as the rate budget of the content consumers.
4.5 Following Rates of Influencer
Similar to content consumers, the inﬂuencer /u1D466.altinﬂ can also decide on the rate 𝜇inﬂ (/u1D466.alt) with which it follows a content
producer 𝑧 ∈ 𝐶 in order to obtain (aggregate) content. Let
𝜇inﬂ = (𝜇inﬂ(𝑧))𝑧 ∈𝐶
be the corresponding rate allocation vector of the inﬂuence r /u1D466.altinﬂ.
Again, we assume that there is a bound 𝑀inﬂ > 0 on the total rate that the inﬂuence can allocate, and we have that
/summationdisplay.1
𝑧 ∈𝐶
𝜇inﬂ (𝑧) ≤ 𝑀inﬂ.
We refer to 𝑀inﬂ as the rate budget of the inﬂuencer.
We deﬁne in Section 7 the optimization problem that the inﬂue ncer uses to choose the rate allocation 𝜇inﬂ.
5 CONTENT CONSUMPTION UTILITY
In this section, we formally deﬁne the utility that content c onsumers obtain from the content they receive. To model
the utility that content consumers obtain from content, we a ssume they are delay-sensitive: the lower the delay with
which a content item is obtained, the higher (less discounte d) the utility from this content item. The assumption of
delay-sensitivity has been broadly used in modeling social network formation, dating back to the seminal work by
Jackson and Wolinsky [26].
Recall that content consumers can receive content from the following sources: directly from content producers they
follow, indirectly through the inﬂuencer, and from content sources outside the community. How content consumers
allocate these following rates determines the delay with wh ich they obtain content from these three sources: a higher
rate of following a source results in a lower delay in receivi ng content from that source. Below, we deﬁne the utility
that content consumers obtain from each of these content sou rces as a function of their following rate allocation.
Manuscript submitted to ACM

14 Junwei Su and Peter Marbach
5.1 Utility from Directly Following another Agent
First, we deﬁne the utility that a content consumer /u1D466.alt obtains by following a content producer 𝑧 with rate 𝜇 (𝑧|/u1D466.alt). Recall
that 𝑥 (𝑧) is the topic on which content producer 𝑧 creates content.
Suppose that content consumer /u1D466.alt receives a reward of value 1 for each content item that is of in terest to them. If
content consumer /u1D466.alt receives content from content producer 𝑧 without delay, the (expected) utility of content consumer
/u1D466.alt for receiving content directly from content producer 𝑧 is given by
𝑟𝑝𝐵 (𝑧|/u1D466.alt),
where
𝐵 (𝑧|/u1D466.alt) = 𝑞(𝑥 (𝑧)|𝑧)𝑝 (𝑥 (𝑧)|/u1D466.alt)
is the probability that a content item from content producer 𝑧 is of interest to content consumer /u1D466.alt, and 𝑟𝑝 is the rate
at which content producer 𝑧 creates new content.
We assume that the overall utility that a content consumer /u1D466.alt receives from content produced by 𝑧 depends not only
on the utility 𝐵 (𝑧|/u1D466.alt) but also on the rate 𝜇 (𝑧|/u1D466.alt) with which content consumer /u1D466.alt follows producer 𝑧. The larger the rate
𝜇 (𝑧|/u1D466.alt), the higher the overall utility that /u1D466.alt receives from 𝑧. More precisely, if content consumer /u1D466.alt follows content from
content producer 𝑧 with rate 𝜇 (𝑧|/u1D466.alt), then the (expected) utility rate of content consumer /u1D466.alt is given by
𝜃 (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt), (3)
where the function 𝜃 (𝜇 (𝑧|/u1D466.alt)) models the sensitivity of the overall utility with respect t o the following rate 𝜇 (𝑧|/u1D466.alt), and
hence the delay with which consumer /u1D466.alt receives content from producer 𝑧.
For our analysis, we make the following assumption for the fu nction 𝜃 (𝜇).
A/s.sc/s.sc/u.sc/m.sc/p.sc/t.sc/i.sc/o.sc/n.sc 3. The function 𝜃 (𝜇) : R+ /u\i∈∞A6.e\dl→ R+ is strictly increasing and strictly concave with
𝜃 (0) = 0
and
lim𝜇→∞ 𝜃 (𝜇) = 1.
Furthermore, the function 𝜃 (𝜇) is continuously diﬀerentiable.
Assumption 3 implies that a low following rate 𝜇 leads to a higher discounting of the utility 𝐵 (𝑧|/u1D466.alt).
5.2 Utility from Following the Influencer
Next, we deﬁne the utility of content consumer /u1D466.alt for receiving content from content producer 𝑧 through the inﬂuencer
/u1D466.altinﬂ. For this, suppose that the inﬂuencer /u1D466.altinﬂ follows content producer 𝑧 with rate 𝜇inﬂ (𝑧), and content consumer /u1D466.alt
follows the inﬂuencer /u1D466.altinﬂ with rate 𝜇 (/u1D466.altinﬂ|/u1D466.alt). The utility of content consumer /u1D466.alt for receiving content from content
producer 𝑧 via the inﬂuencer /u1D466.altinﬂ is then given by
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt), (4)
where
𝜃inﬂ (𝑧|/u1D466.alt) = 𝜃 (𝜇inﬂ (𝑧)) 𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) .
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 15
5.3 Utility from Following Sources outside the Community
Finally, we deﬁne the utility of content consumer /u1D466.alt for receiving content from content sources outside the comm unity.
For this, let 𝑟0 > 0 be the total rate (over all content sources) at which new con tent items are generated by sources
outside the community, and let 𝐵0 be the probability that a content item produced from these so urces is of interest to
content consumer /u1D466.alt. The utility of content consumer /u1D466.alt for receiving content from sources outside the community is
given by
𝑟0𝜃 (𝜆(/u1D466.alt)) 𝐵0, (5)
where 𝜆(/u1D466.alt) is the rate with which content consumer /u1D466.alt follows sources outside the community.
Given the rate allocation 𝜇inﬂ of the inﬂuencer /u1D466.altinﬂ and the content production allocation 𝑋 of the content producers,
and rate allocation Λ(/u1D466.alt) of content consumer /u1D466.alt, the total content consumption utility 𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) of content
consumer /u1D466.alt is given
𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) = 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
+ 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt)
+ 𝑟0𝜃 (𝜆(/u1D466.alt)) 𝐵0.
(6)
5.4 Discussion
We make the following two simplifying assumptions in modeli ng the consumption utility.
First, we assume that the rate 𝑟𝑝 at which content producers create new content is uniform acr oss all producers.
This simpliﬁcation aids both the notation and the analysis. While it is possible to extend the analysis to account for
diﬀerent content creation rates among producers, doing so w ould introduce additional complexity to the notation and
analysis without fundamentally altering the results and in sights.
Second, Eq. (6) implies that consumer /u1D466.alt can receive content from producer 𝑧 both directly and indirectly through
the inﬂuencer /u1D466.altinﬂ. In other words, the utility derived from content produced b y producer 𝑧 is double-counted. To
simplify the analysis, we assume that this eﬀect can be disre garded. Speciﬁcally, we assume that consumer /u1D466.alt primarily
obtains content through the inﬂuencer /u1D466.altinﬂ and only directly follows a small fraction of content produc ers. Empirical
evidence supports this assumption, showing that community members typically obtain content directly from only a
minority of other community members. Moreover, it can be for mally demonstrated that this assumption holds when
the inﬂuencer’s rate budget 𝑀inﬂ is suﬃciently large. Although not making this assumption wo uld complicate the
analysis, it would not signiﬁcantly alter the qualitative r esults and insights obtained.
Overall, these simplifying assumptions enable a more tract able analysis without compromising the core ﬁndings
and insights.
6 SOCIAL SUPPORT
We deﬁne social support as the probability with which an agen t (either a content consumer or an inﬂuencer) provides
positive feedback indicating that a content item is of inter est to them. In social media, this positive feedback can take
the form of a like, share, click, etc.
We assume that the probability that a content consumer/u1D466.alt provides positive feedback to a content item from content
producer 𝑧 is proportional to the utility that the content item provide s to /u1D466.alt. More precisely, for a content item obtained
Manuscript submitted to ACM

16 Junwei Su and Peter Marbach
by directly following producer 𝑧, the social support is given by
𝜃 (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt),
where
𝐵 (𝑧|/u1D466.alt) = 𝑞(𝑥 (𝑧)|𝑧)𝑝 (𝑥 (𝑧)|/u1D466.alt).
For a content item obtained indirectly through the inﬂuence r, the social support is given by
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt).
Note that both expressions for social support take on a valuein [0, 1] and can therefore be interpreted as a probability.
Furthermore, we assume that the probability that the inﬂuen cer /u1D466.altinﬂ provides positive feedback to a content item
from content producer 𝑧 is proportional to the rate at which the inﬂuencer follows co ntent producer 𝑧, and is given by
𝜃 (𝜇inﬂ (𝑧)) .
Note that this expression for social support again takes on a value in [0, 1] and can hence be interpreted as a probability.
The analysis can be extended to incorporate more general expressions for the social support provided by the inﬂuencer.
Importantly, the analysis and results remain valid as long a s the probability of the inﬂuencer providing social support
to a content item from producer 𝑧 is an increasing function of the following rate 𝜇inﬂ (𝑧).
7 GAME WITH PERFECT INFORMATION
In this section, we model the objectives of the inﬂuencer, co ntent consumers, and content producers as optimization
problems, demonstrating that this results in a strategic in teraction (game) among these agents in the content market.
We assume that all agents have perfect information, meaning they are aware of the actions and preferences (utilities)
of all other agents. In Section 9, we relax this assumption an d consider the case of imperfect information.
7.1 Optimal Rate Allocation by Influencer
The objective of the inﬂuencer is to maximize the social supp ort received from content consumers who follow the
inﬂuencer. Using the deﬁnition of social support provided i n Section 6, the resulting optimization problem for the
inﬂuencer is as follows.
Recall that Λ represents the overall rate allocation of all content consu mers, 𝑋 represents the content production
of all content producers, and 𝜇inﬂ is the rate allocation vector of the inﬂuencer /u1D466.altinﬂ. Additionally, recall Eq. (4), which
deﬁnes the utility that content consumers derive from recei ving content through the inﬂuencer /u1D466.altinﬂ, and the deﬁnition
of social support provided by content consumers given in Sec tion 6.
Given the overall rate allocation Λ and content production 𝑋 , the objective of the inﬂuencer is then to choose a rate
allocation 𝜇inﬂ that solves the following optimization problem,
maximize
𝜇inﬂ ≥0
𝑈inﬂ (𝜇inﬂ|Λ, 𝑋) = 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
subject to
/summationdisplay.1
𝑧 ∈𝐶
𝜇inﬂ (𝑧) ≤ 𝑀inﬂ,
(7)
where
𝐵 (𝑧|/u1D466.alt) = 𝑞(𝑥 (𝑧)|𝑧)𝑝 (𝑥 (𝑧)|/u1D466.alt)
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 17
and
𝜃inﬂ (𝑧|/u1D466.alt) = 𝜃 (𝜇inﬂ (𝑧)) 𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) ,
and 𝑀inﬂ > 0 is the rate budget available to the inﬂuencer for followingcontent producers. We refer to this maximization
problem as 𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ, 𝑋).
Note that in the case where
𝜇 (/u1D466.altinﬂ|/u1D466.alt) = 0, /u1D466.alt ∈ 𝐶,
the maximization problem 𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ, 𝑋) is not well deﬁned as any allocation 𝜇inﬂ that satisﬁes the rate constraints
is an optimal solution. To avoid this ambiguity, we make the f ollowing assumption for our analysis.
A/s.sc/s.sc/u.sc/m.sc/p.sc/t.sc/i.sc/o.sc/n.sc 4. If for the optimization problem 𝑂𝑃𝑇inﬂ (𝜇inﬂ|Λ, 𝑋) given by Eq. (7) we have that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇 (/u1D466.altinﬂ|/u1D466.alt) = 0,
then for optimal allocation
𝜇∗ inﬂ = arg max 𝜇inﬂ ≥0 𝑂𝑃𝑇 inﬂ(𝜇inﬂ|Λ, 𝑋)
we set
𝜇∗ inﬂ (𝑧) = 𝑀inﬂ/𝑁 , 𝑧 ∈ 𝐶,
where 𝑁 is the size of the community 𝐶.
7.2 Optimal Rate Allocation by Content Consumers
The objective of content consumers /u1D466.alt ∈ 𝐶 is to obtain content that maximizes the content consumption utility given
by Eq. (6).
Recall that 𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) given by Eq. (6) is the content consumption utility of conten t consumer /u1D466.alt under the
rate allocation 𝜇inﬂ of the inﬂuencer /u1D466.altinﬂ, the content production 𝑋 of all content producers. The objective of content
consumer /u1D466.alt is then to choose a rate allocation Λ∗ that solves the following optimization problem,
maximize
Λ(/u1D466.alt) ≥0
𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋)
subject to 𝜇 (/u1D466.altinﬂ|/u1D466.alt) + 𝜆(/u1D466.alt) +
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇 (𝑧|/u1D466.alt) ≤ 𝑀, (8)
where 𝑀 > 0 is the rate budget available to content consumer /u1D466.alt. We refer to this maximization problem as the con-
sumption utility maximization problem 𝑂𝑃𝑇𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋).
7.3 Optimal Content Production by Content Producers
The objective of content producer 𝑧 ∈ 𝐶 is to create content on a topic 𝑥 (/u1D466.alt) that maximizes the social support that
𝑧 receives from the content consumers. Using the deﬁnition of the social support as given in Section 6, the resulting
optimization problem is given as follows.
Manuscript submitted to ACM

18 Junwei Su and Peter Marbach
Using the deﬁnitions given in Section 6, the social support 𝑈𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) that producer 𝑧 receives based on the
rate allocation 𝜇inﬂ of the inﬂuencer /u1D466.altinﬂ and the overall rate allocation Λ of all content consumers, is given by
𝑈𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) = 𝑟𝑝
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
+ 𝑟𝑝
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt).
(9)
The objective of content producer 𝑧 is then to create content on topic 𝑥∗ (𝑧) that solves the following optimization
problem,
maximize
𝑥 (𝑧) ∈ T
𝑈𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ). (10)
We refer to this maximization problem as 𝑂𝑃𝑇𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ).
7.4 Nash Equilibrium
Note that the optimal solution of the maximization problem 𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ, 𝑋) of the inﬂuencer depends on the overall
rate allocation Λ of the content consumers and the content production𝑋 of all content producers. Similarly, the optimal
solution of the maximization problem 𝑂𝑃𝑇𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) of content consumer /u1D466.alt depends on the rate allocation 𝜇inﬂ of
the inﬂuencer and the content production 𝑋 of all content producers. Finally, the optimal solution of the maximization
problem 𝑂𝑃𝑇𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) of content producer 𝑧 depends on the rate allocation 𝜇inﬂ of the inﬂuencer and the overall
rate allocation 𝑋 of all content consumers. This coupling creates a strategic interaction between the inﬂuencer and
community members. A Nash equilibrium for the resulting gam e is given as follows.
Let Ω = (𝜇inﬂ, Λ, 𝑋) be a given allocation that characterizes the rate allocatio n 𝜇inﬂ of the inﬂuencer, and the overall
rate allocation Λ of all content consumers, and the content allocation 𝑋 of all content producers.
D/e.sc/f.sc/i.sc/n.sc/i.sc/t.sc/i.sc/o.sc/n.sc 7.1. An allocation ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium if we have that
(1) 𝜇∗ inﬂ is a solution for the maximization problem 𝑂𝑃𝑇inﬂ (𝜇inﬂ|Λ∗, 𝑋∗),
(2) Λ∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋 ∗), and
(3) 𝑥∗ (𝑧), 𝑧 ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇𝑝,𝑧 (𝑥 (𝑧)| 𝜇∗ inﬂ, Λ∗).
Deﬁnition 7.1 states that under a Nash equilibrium ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) no agent in the content market is
able to increase the value of their objective function by uni laterally changing their allocation. In the next two sectio ns,
we analyze the existence and properties of a Nash equilibriu m.
8 RESULTS ON NASH EQUILIBRIUM FOR PERFECT INFORMATION
We ﬁrst analyze the Nash equilibrium. Note that this equilibrium assumes that all agents have perfect information when
deciding on their allocations. For this case, we analyze the existence and eﬃciency of a Nash equilibrium ΩNE (𝑀, 𝑀inﬂ).
We measure the eﬃciency of a Nash equilibrium by the social we lfare (sum of the utilities) over all content consumers.
8.1 Existence and Eﬀiciency of a Nash Equilibrium ΩNE (𝑀, 𝑀infl)
Our ﬁrst result states that there always exists a Nash equili brium.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 1. There exists a Nash equilibrium ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗).
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 19
We provide a proof for Proposition 1 in Appendix A. To prove th e proposition, we show that the game deﬁned in
Section 7 is a potential game for the potential function
Φ(Ω) =
/summationdisplay.1
/u1D466.alt ∈𝐶
𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋), (11)
where 𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) is the consumption utility of community member /u1D466.alt as given by Eq. (6). Note that the potential
function Φ(Ω) is the total consumption utility over all content consumers which contains both the utility obtained
from content producers and the inﬂuencer, as well as content from other sources. In the following we refer to Φ(Ω) as
the social welfare.
The next result states that there always exists a Nash equili brium that maximizes the social welfare. To state the
result, we use the following notation. Let S (𝑀inﬂ, 𝑀) be the set of all admissible allocations Ω = (𝜇inﬂ, Λ, 𝑋), i.e. the set
of all allocations such the rate allocation 𝜇inﬂ is given by a non-negative vector that satisfy the rate budge t constraints
𝑀inﬂ of the inﬂuencer, Λ(/u1D466.alt), /u1D466.alt ∈ 𝐶 is a non-negative vector that satisﬁes the rate budget const raint 𝑀 for the content
consumers, and we have that 𝑥 (𝑧) ∈ T , 𝑧 ∈ 𝐶.
Using the fact that the social welfare Φ(Ω) is a potential function, we obtain the following result.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 2. There exists a Nash equilibrium Ω∗ (𝑀inﬂ, 𝑀) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) that maximizes the social welfare, i.e. we
have that
Ω∗ (𝑀inﬂ, 𝑀) = argmax
Ω∈ S (𝑀inﬂ,𝑀 )
Φ(Ω).
We provide a proof for Proposition 2 in Appendix B.
8.2 Eﬀiciency of Nash Equilibria ΩNE (𝑀, 𝑀infl)
Proposition 2 states that there is a Nash equilibrium Ω∗ (𝑀inﬂ, 𝑀) that maximizes the social welfare given by Eq. (11).
However, it does not state that all Nash equilibria ΩNE (𝑀, 𝑀inﬂ) maximize the social welfare, nor does it provide con-
ditions under which the community interactions converge to a Nash equilibrium Ω∗ (𝑀inﬂ, 𝑀). It is possible to provide
suﬃcient conditions for all Nash equilibria to be eﬃcient, a nd for the community to converge to an eﬃcient Nash
equilibrium. Roughly, these conditions impose additional assumptions on the distribution of the community members
within the community such that the distribution is unimodal . While this analysis is possible, it is outside the scope
of this paper. It is more challenging to identify necessary c onditions for all Nash equilibria to be eﬃcient and for an
eﬃcient Nash equilibrium to emerge. This question is an open problem.
9 GAME WITH IMPERFECT INFORMATION
In Sections 7 and 8, we analyzed the existence and eﬃciency ofa Nash equilibrium for the case where content producers
have perfect information, i.e. they know the actions and preferences (utilities) of all other agents and have access to the
social support that they receive from all content consumers /u1D466.alt ∈ 𝐶. In this section, we consider the more realistic case
where agents do not have perfect information. In particular , we assume that content producers can not observe the
actions of all content consumers, and hence can not directlyobserve the social support that they obtain from the content
consumers. Instead, content producers rely on the social su pport obtained from the inﬂuencer to decide which content
to create. In this section, we deﬁne the resulting game based on this interaction. In Section 10 we analyze the existence
of a Nash equilibrium for this game, and in Section 11 we chara cterize whether, and by how much, the outcome of the
case with limited information deviates from market equilib rium from the idealized of perfect information.
Manuscript submitted to ACM

20 Junwei Su and Peter Marbach
In the following we deﬁne the allocation decisions by the inﬂ uencer, content consumers, and content producers, for
the game with imperfect information.
9.1 Optimal Rate Allocation by Influencer
We assume that the inﬂuencer /u1D466.altinﬂ is able to observe the social support received from the conte nt consumer who follow
the inﬂuencer. The inﬂuencer /u1D466.altinﬂ then use the maximization problem 𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ, 𝑋) given by Eq. (7) to decide on its
allocation 𝜇inﬂ by setting
maximize
𝜇inﬂ ≥0
𝑈inﬂ(𝜇inﬂ|Λ, 𝑋)
subject to
/summationdisplay.1
𝑧 ∈𝐶
𝜇inﬂ (𝑧) ≤ 𝑀inﬂ,
where the objective function 𝑈inﬂ (𝜇inﬂ|Λ, 𝑋) is as given by Eq. (7).
9.2 Optimal Rate Allocation by Content Consumers
We assume that content consumers can observe the content tha t content producers create, i.e. they can observe the
content allocation 𝑋 . One way to achieve this is by following the inﬂuencer, and observing the content 𝑥 (𝑧) of producer
𝑧 that the inﬂuencer shares. Using this assumption, content consumer /u1D466.alt ∈ 𝐶 chooses an allocation Λ(/u1D466.alt) that maximizes
𝑂𝑃𝑇𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) given by
maximize
Λ(/u1D466.alt) ≥0
𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋)
subject to 𝜇 (/u1D466.altinﬂ|/u1D466.alt) + 𝜆(/u1D466.alt) +
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇 (𝑧|/u1D466.alt) ≤ 𝑀.
9.3 Optimal Content Production by Content Producers
We assume that content producers can not directly observe th e social support that they receive, and instead use the
social support obtained by the inﬂuencer as a proxy for the so cial support their content receives from the content
consumers. To formulate the resulting optimization proble m, we use the following notation.
For a given content production vector 𝑋 , we use 𝑋 {𝑧,𝑥 (𝑧) ′ } to denote that the content created by content producer
𝑧 ∈ 𝐶 changed from 𝑥 (𝑧) to 𝑥 (𝑧)′), while the content created by all other content producers is the same.
Furthermore, for a given rate allocation Λ of the content consumers and a given content allocation 𝑋 of the content
producers, let 𝜇∗ inﬂ (Λ, 𝑋) denote the optimal rate allocation of the inﬂuencer /u1D466.altinﬂ as given by Eq. (7). Furthermore, let
𝜇∗ inﬂ (𝑧|Λ, 𝑋) be the following rate that the inﬂuencer /u1D466.altinﬂ allocates to content producer 𝑧 under 𝜇inﬂ (Λ, 𝑋).
Using these deﬁnitions, the objective of content producer 𝑧 is to create content on the topic 𝑥∗ (𝑧) which maximize
the social support received from the inﬂuencer, i.e. we have that
𝑥∗ (𝑧) = argmax
𝑥 (𝑧) ∈ T
𝜃
(
𝜇∗ inﬂ (𝑧|Λ, 𝑋{𝑧,𝑥 (𝑧) }) ) . (12)
9.4 Nash Equilibrium
We deﬁne a Nash equilibrium for the case of limited informati on as follows.
D/e.sc/f.sc/i.sc/n.sc/i.sc/t.sc/i.sc/o.sc/n.sc 9.1. An allocation Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium if we have that
(1) 𝜇∗ inﬂ is a solution for the maximization problem 𝑂𝑃𝑇inﬂ (𝜇inﬂ|Λ∗, 𝑋∗),
(2) Λ∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋 ∗), and
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 21
(3) 𝑥∗ (𝑧) = argmax𝑥 (𝑧) ∈ T 𝜃 ( 𝜇inﬂ(𝑧|Λ∗, 𝑋∗ {𝑧,𝑥 (𝑧) }) ) , 𝑧 ∈ 𝐶.
In the following, we refer to a Nash equilibrium Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) as given by Deﬁnition 9.1 as a Nash
equilibrium for the game with imperfect information, and to a Nash equilibrium ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) as given
by Deﬁnition 7.1 as a Nash equilibrium for the game with perfe ct information.
10 RESULTS ON NASH EQUILIBRIUM FOR LIMITED INFORMATION
In this section we analyze the existence of a Nash equilibriu m for the game with imperfect information as given by
Deﬁnition 9.1, and characterize the optimal allocation 𝑥∗ (𝑧|Λ, 𝑋) of content producer 𝑧 (see Eq. (12)) under a Nash
equilibrium.
10.1 Existence of a Nash Equilibrium Ωinfl (𝑀, 𝑀infl)
Our ﬁrst result states that there always exists a Nash equili brium given by Deﬁnition 9.1.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 3. There exists a Nash equilibrium Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) as given by Deﬁnition 9.1.
We provide a proof for Proposition 3 in Appendix C. We note tha t the game with imperfect information as given by
Deﬁnition 9.1 is no longer a potential game with the social we lfare Φ(Ω) as a potential function. As a result, the proof
for Proposition 3 diﬀers from the one given for Proposition 1 for the game with perfect information.
10.2 Optimal Decision by Content Producers
We next characterize the optimal allocation 𝜇∗ inﬂ of the inﬂuencer under a Nash equilibrium as given by Deﬁniti on 9.1.
Let
𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) =𝑟𝑝 /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt), (13)
be the production utility that producer /u1D466.alt receives through the inﬂuencer /u1D466.altinﬂ under the allocation (Λ, 𝑋) (see Eq. (9)).
We then obtain the following result.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 4. If Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium as given by Deﬁnition 9.1 such that for c ontent
producer 𝑧 ∈ 𝐶 we have
𝜇∗ inﬂ(𝑧) > 0
and /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0,
then we have
𝑥∗ (𝑧) = argmax
𝑥 (𝑧) ∈ T
𝑈
inﬂ
𝑝,𝑧 (𝑥 (𝑧)| 𝜇∗ inﬂ, Λ∗).
We provide a proof for Proposition 4 in Appendix D.
Proposition 4 states that a content topic 𝑥∗ (𝑧) of content producer 𝑧 ∈ 𝐶 under a Nash equilibrium Ωinﬂ (𝑀, 𝑀inﬂ) =
(𝜇∗ inﬂ, Λ∗, 𝑋 ∗) maximizes the social support 𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇∗ inﬂ, Λ∗) that producer 𝑧 receives from content shared by the
inﬂuencer /u1D466.altinﬂ, as given by Eq. (13).
It is important to note that𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) diﬀers from the overall social support𝑈𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) (given by Eq.(9))
that content producer 𝑧 receives in the community, since 𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) excludes the social support that content
producer obtains from content consumers /u1D466.alt ∈ 𝐶 who follow producer 𝑧, and we have 𝜇 (𝑧|/u1D466.alt) > 0.
Manuscript submitted to ACM

22 Junwei Su and Peter Marbach
11 EFFICIENCY OF NASH EQUILIBRIUM Ω∗ infl (𝑀, 𝑀infl)
Let Sinﬂ be the set of all Nash equilibria Ωinﬂ as given by Deﬁnition 9.1, and let
Ω∗ inﬂ (𝑀, 𝑀inﬂ) = argmax
Ωinﬂ ∈ Sinﬂ
Φ(Ωinﬂ) (14)
be a Nash equilibrium that maximizes the social welfare over all Nash equilibria as given by Deﬁnition 9.1.
Proposition 4 states that by maximizing the social support f rom the inﬂuencer /u1D466.altinﬂ, a content producer 𝑧 ∈ 𝐶 maxi-
mizes at a Nash equilibrium the production utility 𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇∗ inﬂ, Λ∗) that content producer 𝑧 obtains from its content
that is shared by the inﬂuencer /u1D466.altinﬂ. An optimal allocation 𝑥∗ (𝑧) for the production utility 𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇∗ inﬂ, Λ∗) generally
does not maximize the consumption utility over all content c onsumers (as it ignores the utility of consumers who
follow the producer 𝑧 directly), and hence generally does not maximize the social welfare.
As a result, a Nash equilibrium Ω∗ inﬂ (𝑀, 𝑀inﬂ) as given by Eq. (14) generally does not maximize the socially opti-
mal allocation as given in Proposition 2, and the social welf are Φ(Ω∗ inﬂ (𝑀, 𝑀inﬂ)) obtained under a Nash equilibrium
Ω∗ inﬂ (𝑀, 𝑀inﬂ) as given by Eq. (14) is generally strictly smaller than the so cial welfare Φ(Ω∗ (𝑀inﬂ, 𝑀)) obtained under a
socially optimal Nash equilibrium Ω∗ (𝑀inﬂ, 𝑀) as given by Proposition. 2. In the following, we analyze the e ﬃciency
of an optimal Nash equilibrium Ω∗ inﬂ (𝑀, 𝑀inﬂ) as given by Eq. (14).
To characterize the eﬃciency of a Nash equilibrium as given by Deﬁnition 9.1, we study the case where the size 𝑁 of
the community and the rate budget 𝑀inﬂ of the inﬂuencer are large, and show that for this case that a N ash equilibrium
Ω∗ inﬂ (𝑀, 𝑀inﬂ) as given by Eq. (14) is socially optimal. We obtain the follow ing result.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 5. Let 𝑀 be a given rate budget for the content consumers. Then there e xists a integer 𝑁0 and a constant
𝑘inﬂ such that if 𝑁 > 𝑁0, and 𝑀inﬂ > 𝑁 𝑘inﬂ, the following is true. For an optimal Nash equilibrium
Ω∗ inﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗)
for the game with imperfect information as given by Eq. (14) we have that
Φ
(
Ω∗ inﬂ (𝑀, 𝑀inﬂ) ) = Φ ( Ω∗ (𝑀inﬂ, 𝑀) ) .
Proposition 5 is the key result of our analysis. It provides t he critical insight that, for a suﬃciently large community
size 𝑁 and a large enough inﬂuencer rate budget 𝑀inﬂ, the following holds:
a) If the inﬂuencer allocates its following rate based on the social support received from content consumers, and
b) If content producers use the social support from the inﬂue ncer to decide which type of content to produce,
then this dynamic leads to an eﬃcient outcome, where a Nash eq uilibria Ω∗ inﬂ (𝑀, 𝑀inﬂ) as given by Eq. (14) maximizes
the social welfare. This highlights the fundamental role th at social support (as a form of currency) and the inﬂuencer
(as an information proxy) play in coordinating the actions o f individual agents in the content market. We discuss this
result in more detail in Section 12.
Proposition 5 is also technically the most challenging to pr ove. The proof is provided in Appendix E.4.
12 DISCUSSION OF RESULTS
In this section, we discuss the results obtained in Sections 8, 10, and 11. We explore the insights these results provide
into the fundamental roles of social support (as a form of cur rency) and the inﬂuencer (as an information proxy) in
coordinating the actions of individual agents within the co ntent market.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 23
12.1 Social Support as a Currency
Proposition 2 establishes the existence of a Nash equilibri um that maximizes social welfare, demonstrating that socia l
support leads to an eﬃcient outcome. This result provides a formal understanding of social support as a currency within
the content market under consideration. Speciﬁcally, it sh ows that achieving an eﬃcient market equilibrium requires
the following three conditions: First, the social support p rovided by content consumers must eﬀectively signal the
utility they derive from content. Second, content producer s must aim to maximize the social support they receive for
their content. Finally, inﬂuencers should strive to maximize the social support obtained from their followers. Deviations
from these three conditions are likely to result in suboptim al market outcomes. We discuss how these insights can be
applied to study algorithms on social media platforms, such as content recommendation algorithms, in Section 13.
12.2 Role of Influencer
In the content market, inﬂuencers serve two crucial roles. F irst, they act as aggregators of content tailored to the inte r-
ests of their followers, facilitating the discovery of rele vant content by consumers. This role is widely recognized an d
aligns with the established understanding of inﬂuencers insocial media and content markets. However, inﬂuencers also
assume another signiﬁcant role. In large content markets, where content producers face substantial costs in tracking all
content consumers to gather relevant information for content creation decisions, inﬂuencers can act as proxies for this
information. Speciﬁcally, content producers can use the so cial support received by an inﬂuencer as an approximation
of the overall social support they would receive from the entire consumer base. The higher the social support garnered
by a content item from an inﬂuencer, the higher the anticipat ed level of social support from all content consumers. By
leveraging inﬂuencers as information proxies, content pro ducers can make nearly optimal decisions, resulting in an
eﬃcient market outcome. This particular role of inﬂuencers has not been formally characterized in existing literature .
12.3 Flow of Social Support and Flow of Content
Our analysis reveals two distinct ﬂows within the content ma rket: the ﬂow of social support and the ﬂow of content.
The ﬂow of social support originates from content consumers , moves towards the inﬂuencer, and then passes to the
content producers. Conversely, the ﬂow of content starts wi th the content producers, moves through the inﬂuencer,
and reaches the content consumers.
This structure resembles a market economy, where there are t wo ﬂows: money ﬂowing in one direction and goods
in the opposite direction. Similarly, in the content market , the ﬂow of social support from consumers to the inﬂuencer,
and then from the inﬂuencer to the content producers, is coup led with the ﬂow of content. This coupling operates in
both directions: (a) the ﬂow of social support determines th e ﬂow of content, and (b) the ﬂow of content determines
the ﬂow of social support.
To elaborate on this coupling, we specify that the ﬂow of soci al support inﬂuences the ﬂow of content in the follow-
ing ways:
• The social support from content consumers determines the co ntent that the inﬂuencer shares.
• The social support received by the inﬂuencer aﬀects the cont ent created by the producers.
Similarly, the ﬂow of content inﬂuences social support as fo llows:
• The utility of the content created by a producer determines t he social support that the producer receives from
the inﬂuencer.
Manuscript submitted to ACM

24 Junwei Su and Peter Marbach
• The utility of the content shared by the inﬂuencer determine s the social support the inﬂuencer receives from
content consumers.
A Nash equilibrium in this context corresponds to a ﬁxed poin t where these two ﬂows are balanced, similar to the
equilibrium of money and goods ﬂow in a market economy.
Just as money signals the utility of goods in a market economy , social support signals the utility of content. The
social support provided by a content consumer reﬂects the (p ersonal) utility of a content item to that consumer, while
the social support received by the inﬂuencer signals the agg regated utility of content to the inﬂuencer’s followers (se e
Proposition 4).
It is worth noting that existing cascade models in the litera ture primarily focus on how the ﬂow of social support
determines the ﬂow of content [14, 16, 17]. In contrast, our a nalysis identiﬁes and studies the second ﬂow, namely how
the ﬂow of content shapes the ﬂow of social support. Moreover , we demonstrate that these two ﬂows are interlinked
as outcomes of the strategic interactions among content con sumers, content producers, and inﬂuencers.
12.4 Price of Influence
Proposition 2 demonstrates that an eﬃcient market equilibr ium is achieved when agents have perfect information.
However, in the scenario discussed in Section 9, where conte nt producers have limited information, this is no longer
the case. Speciﬁcally, using the inﬂuencer as a proxy to gaug e social support leads to suboptimal decisions by content
producers. Consequently, the social welfare Φ(Ω∗ inﬂ (𝑀, 𝑀inﬂ)) achieved under a Nash equilibrium, as given by Eq. (14),
is generally strictly lower than the social welfare Φ(Ω∗(𝑀inﬂ, 𝑀)) achieved under a socially optimal allocation, as given
by Proposition 2.
We refer to the reduction |Φ(Ω∗ (𝑀inﬂ, 𝑀)) − Φ(Ω∗ inﬂ (𝑀, 𝑀inﬂ))| in social welfare as the “price of inﬂuence. ”
Proposition 5 helps identify situations where the price of i nﬂuence is low, meaning the inﬂuencer’s role as a proxy
results in an equilibrium that is close to maximizing social welfare. This proposition suggests that the price of inﬂuence
decreases when the inﬂuencer’s rate budget 𝑀inﬂ is signiﬁcantly larger than the rate budget 𝑀 of the community mem-
bers. Thus, in large communities where the inﬂuencer’s rate budget greatly exceeds that of the community members,
using the inﬂuencer as an information proxy is eﬀective. Thi s approach allows content producers to gather necessary
information for decision-making by following a single agen t (i.e., the inﬂuencer) rather than all consumers, leading t o
a more eﬃcient market outcome.
13 CONCLUSION
This paper presents a formal study of the role played by socia l support and inﬂuencers within a content market. The
content market being considered here models a community on a social media platform where users both create and
consume content of interest to them, while inﬂuencers curat e and distribute content to attract followers. Our analysis
provides a characterization of social support as a currency within this market, and highlights the inﬂuencers’ dual rol e
as content aggregators and information proxies for social s upport.
The paper’s most signiﬁcant impact lies in its potential to t ransform how social media platforms and multi-agent
systems are understood and designed. By modeling social support as a currency, the paper provides a novel and power-
ful framework to analyze the impact of social media content recommendation algorithms on the ﬂow of content within
social media. Additionally, the insights gained from this w ork have the potential to transform the understanding and
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 25
design of decentralized AI systems and other multi-agent en vironments where coordination and strategic interaction
are critical. We discuss this in more detail below, together with additional important directions for future research.
13.1 Emergence of Influencers
Our analysis assumes the existence of an inﬂuencer whose obj ective is to maximize the social support received from
their followers. This leads to two crucial questions:
(1) Whether and how such an inﬂuencer emerges in a content mar ket.
(2) Whether and why the inﬂuencer chooses to maximize the soc ial support received from their followers as their
objective.
We are currently modeling and analyzing the formation of a co ntent market. Preliminary results demonstrate that
an inﬂuencer indeed emerges once the content market reaches a certain size. Moreover, under suitable assumptions,
the inﬂuencer derives signiﬁcantly higher utility from sharing content rather than creating it. Thus, it is rational for an
inﬂuencer to focus on maximizing social support through content sharing. The inﬂuencer achieves this by aggregating
content from producers in a way that maximizes the social support received from their followers. These results provide
a formal justiﬁcation for the assumptions regarding the rol e and objectives of inﬂuencers in our model.
13.2 Empirical Validation
Using social media communities as a concrete scenario allow s us to test how agents coordinate their actions in a
distributed manner. The activities of users on online socia l media platforms can be accessed and analyzed, providing
a way to empirically test and validate the theoretical resul ts presented in this paper. We are currently conducting
this empirical study, and preliminary results indicate tha t the ﬁndings from our theoretical analysis are observable i n
real-life social media communities. This ongoing research will be detailed in a forthcoming paper.
13.3 Analyzing Social Media Algorithms
The ﬁnding that social support acts as a currency within a con tent market oﬀers a fresh perspective on social media
algorithms, including content recommendation algorithms . Speciﬁcally, it suggests that social media algorithms can
be viewed as actors or mechanisms that inﬂuence the ﬂow of soc ial support and content. Similar to a market economy,
one can investigate social media algorithms by characteriz ing their impact on a) the ﬂow of social support, b) the
ﬂow of content, and c) the market equilibrium and the social w elfare achieved at the equilibrium. Furthermore, it
suggests that social media platforms, equipped with comple te market information, can utilize this insider informatio n
to "manipulate" the content market in their favor, resultin g in high utility for the platform at the expense of reduced
social welfare and user utilities. Exploring these issues c onstitutes an important direction for future research.
13.4 Application to General Multi-Agent Systems
A critical direction for future research is to explore wheth er and how social support, as a mechanism for coordinating
actions, can be applied to more general multi-agent systems , such as multi-agent AI systems or distributed computing
systems. These systems often face similar challenges relat ed to coordination and strategic interaction among agents.
The central idea is to investigate whether a form of "social s upport" can emerge in these environments, where
agents provide feedback or rewards based on each other’s con tributions to shared goals or system-wide eﬃciency.
This concept could be analogous to how likes or shares signal the value of content in social media.
Manuscript submitted to ACM

26 Junwei Su and Peter Marbach
In multi-agent AI systems, this mechanism could enhance coo rdination in scenarios where agents must balance
individual and collective objectives. For instance, in col laborative tasks or competitive environments like resourc e
allocation or complex strategy games, social support could serve as a feedback-based incentive that helps agents adapt
their strategies based on positive reinforcement from othe rs in the system. This could lead to more eﬀective decision-
making in settings such as multi-agent reinforcement learn ing, where agents learn to cooperate or compete within
shared environments.
This direction is ongoing research that we are currently und ertaking, focusing on the application of social support
mechanisms to multi-agent systems and exploring their impact on coordination and strategic interaction among agents.
13.5 Extensions of the Model and Analysis
Finally, there are several possible extensions and generalizations of the model and analysis presented in this paper. F or
instance, while Proposition 2 states the existence of a Nash equilibrium Ω∗ (𝑀inﬂ, 𝑀) that maximizes social welfare (as
deﬁned by Eq. (11)), it does not guarantee that all Nash equil ibria ΩNE (𝑀, 𝑀inﬂ) maximize social welfare, nor does it
provide conditions under which community interactions con verge to the Nash equilibrium Ω∗ (𝑀inﬂ, 𝑀). It is possible
to establish suﬃcient conditions for all Nash equilibria to be eﬃcient and for the community to converge to an eﬃcient
Nash equilibrium. However, identifying the necessary cond itions for an eﬃcient Nash equilibrium to emerge remains
an open problem.
Proposition 5 states that in the limit of an inﬁnite rate budget, we have that all Nash equilibria Ω∗ inﬂ (𝑀, 𝑀inﬂ) as given
by Eq. 14 are eﬃcient in the sense that they maximize the social welfare. However, it does not provide a characterization
of how quickly the allocation Ω∗ inﬂ (𝑀, 𝑀inﬂ) converges to the socially optimal allocation Ω∗ (𝑀inﬂ, 𝑀), nor does it provide
a bound on the price of inﬂuence |Φ(Ω∗ (𝑀inﬂ, 𝑀)) − Φ(Ω∗ inﬂ (𝑀, 𝑀inﬂ))| in communities where the price of inﬂuence is
non-zero. This is another important direction for future re search.
REFERENCES
[1] Jason Noble and Daniel W Franks. Social learning in a mult i-agent system. Computing and Informatics , 22(6):561–574, 2003.
[2] Natasha Jaques, Angeliki Lazaridou, Edward Hughes, Cag lar Gulcehre, Pedro Ortega, DJ Strouse, Joel Z Leibo, and Nan do De Freitas. Social
inﬂuence as intrinsic motivation for multi-agent deep rein forcement learning. In International Conference on Machine Learning , pages 3040–3049.
PMLR, 2019.
[3] S Kartik and C Siva Ram Murthy. Task allocation algorithm s for maximizing reliability of distributed computing syst ems. IEEE Transactions on
Computers, 46(6):719–724, 1997.
[4] Emilie Durkheim. The Division of Labor in Society . 1893.
[5] A. Giddens. The Constitution of Society: Outline of the Theory of Struct uration. Outline of the Theory of Structuration. University of Cali fornia Press,
1984.
[6] P. Bourdieu and L.J.D. Wacquant. An Invitation to Reﬂexive Sociology . University of Chicago Press, 1992.
[7] Chrysanthos Dellarocas, Zsolt Katona, and William Rand . Media, aggregators, and the link economy: Strategic hyper link formation in content
networks. Management Science, 59(10):2360–2379, 2013.
[8] Patrick R Jordan, Uri Nadav, Kunal Punera, Andrzej Skrzy pacz, and George Varghese. Lattice games and the economics o f aggregators. In Proceed-
ings of the 21st international conference on World Wide Web , pages 549–558. ACM, 2012.
[9] Chrysanthos Dellarocas, Zsolt Katona, and William Rand . Media, aggregators and the link economy: Strategic hyperl ink formation in content
networks. School of Management Research Paper , 30:06–131, 2010.
[10] Thomas H Davenport and John C Beck. The attention econom y. Ubiquity, 2001(May):1–es, 2001.
[11] Paul Milgrom and John Roberts. An economic approach to i nﬂuence activities in organizations. American Journal of Sociology, 94:S154–S179, 1988.
[12] Talcott Parsons. On the concept of inﬂuence. Public Opinion Quarterly, 27(1):37–62, 01 1963.
[13] Fabián Riquelme and Pablo González-Cantergiani. Meas uring user inﬂuence on twitter: A survey. Information processing & management, 52(5):949–
975, 2016.
[14] Mahdi Jalili and Matjaž Perc. Information cascades in c omplex networks. Journal of Complex Networks , 5(5):665–693, 2017.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 27
[15] Yuchen Li, Ju Fan, Yanhao Wang, and Kian-Lee Tan. Inﬂuen ce maximization on social graphs: A survey. IEEE Transactions on Knowledge and Data
Engineering, 30(10):1852–1872, 2018.
[16] Duncan J. Watts. A simple model of global cascades on ran dom networks. Proceedings of the National Academy of Sciences , 99(9):5766–5771, 2002.
[17] Peter Dodds and Duncan J. Watts. Threshold Models of Soc ial Inﬂuence. In The Oxford Handbook of Analytical Sociology . Oxford University Press,
2011.
[18] Soroush Vosoughi, Deb Roy, and Sinan Aral. The spread of true and false news online. Science, 359(6380):1146–1151, 2018.
[19] Sharad Goel, Duncan J. Watts, and Daniel G. Goldstein. T he structure of online diﬀusion networks. In Proceedings of the 13th ACM Conference on
Electronic Commerce, EC ’12, page 623–638, New York, NY, USA, 2012. Association f or Computing Machinery.
[20] Donna L Hoﬀman and Marek Fodor. Can you measure the roi of your social media marketing? MIT Sloan management review , 2010.
[21] Zeynep Tufekci. Not this one social movements, the atte ntion economy, and microcelebrity networked activism. American Behavioral Scientist ,
57(7):848–870, 2013.
[22] Ashish Goel and Farnaz Ronaghi. A game-theoretic model of attention in social networks. In Anthony Bonato and Jeann ette Janssen, editors,
Algorithms and Models for the Web Graph , pages 78–92, Berlin, Heidelberg, 2012. Springer Berlin He idelberg.
[23] Christian Borgs, Jennifer Chayes, Brian Karrer, Brend an Meeder, R. Ravi, Ray Reagans, and Amin Sayedi. Game-theor etic models of information
overload in social networks. In Ravi Kumar and Dandapani Siv akumar, editors, Algorithms and Models for the Web-Graph , pages 146–161, Berlin,
Heidelberg, 2010. Springer Berlin Heidelberg.
[24] Arpita Ghosh and Preston McAfee. Incentivizing high-q uality user-generated content. In Proceedings of the 20th International Conference on World
Wide Web, WWW ’11, page 137–146, New York, NY, USA, 2011. Association for Computing Machinery.
[25] Avner May, Augustin Chaintreau, Nitish Korula, and Silvio Lattanzi. Filter & follow: How social media foster content curation. In ACM SIGMETRICS
Performance Evaluation Review, volume 42, pages 43–55. ACM, 2014.
[26] Matthew O. Jackson and Asher Wolinsky. A strategic mode l of social and economic networks. Journal of Economic Theory , 71(1):44–74, 1996.
[27] Claude Berge. Topological spaces: Including a treatment of multi-valued functions, vector spaces and convexity . Oliver & Boyd, 1877.
[28] Viktor Vasilevich Prasolov. Elements of combinatorial and diﬀerential topology , volume 74. American Mathematical Society, 2022.
A PROOF OF PROPOSITION 1
In this appendix we prove Proposition 1 which states that the re exists a Nash equilibrium ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗)
for the game with perfect information as given by Deﬁnition 7 .1.
A.1 Preliminary Results
We ﬁrst show that the game with perfect information given by Deﬁnition 7.1 is a potential game. We proceed as follows.
Recall that the objective function 𝑈inﬂ (𝜇inﬂ|Λ, 𝑋) of the inﬂuencer is given by (see Eq. 7)
𝑈inﬂ (𝜇inﬂ|Λ, 𝑋) = 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
where
𝜃inﬂ (𝑧|/u1D466.alt) = 𝜃 (𝜇inﬂ (𝑧)) 𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) ;
the objective function of a content consumer /u1D466.alt ∈ 𝐶 is given by (see Eq. 8)
𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) = 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
+ 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt)
+ 𝑟0𝜃 (𝜆(/u1D466.alt)) 𝐵0,
Manuscript submitted to ACM

28 Junwei Su and Peter Marbach
the objective function of a content producer 𝑧 ∈ 𝐶 is given by (see Eq. 10)
𝑈𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) = 𝑟𝑝
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
+ 𝑟𝑝
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt),
The next result states that the game with perfect informatio n as given by Deﬁnition 7.1 is a potential game.
L/e.sc/m.sc/m.sc/a.sc 2. The game with perfect information as given by Deﬁnition 7.1 i s a potential game with potential function
Φ(Ω) =
/summationdisplay.1
/u1D466.alt ∈𝐶
𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋)
= 𝑟𝑝
/summationdisplay.1
/u1D466.alt ∈𝐶
 /summationdisplay.1 𝑧 ∈𝐶\{ /u1D466.alt } 𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt) + /summationdisplay.1 𝑧 ∈𝐶\{ /u1D466.alt } 𝜃 (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) 
+
/summationdisplay.1
/u1D466.alt ∈𝐶
𝑟0𝜃 (𝜆(/u1D466.alt)) 𝐵0.
P/r.sc/o.sc/o.sc/f.sc. Recall that Ω = (𝜇inﬂ, Λ, 𝑋) denotes the allocation decision of all agents in the communi ty, where 𝜇inﬂ is
the rate allocation of the inﬂuence /u1D466.altinﬂ, Λ is the rate allocation of all content consumers /u1D466.alt ∈ 𝐶, and 𝑋 indicates the
content production of all content producers 𝑧 ∈ 𝐶. To simplify the notation, for a given rate allocation of the content
consumers Λ, we use Λ{/u1D466.alt,Λ(/u1D466.alt) ′ } to denote that the rate allocation of content consumer /u1D466.alt ∈ 𝐶 changed from Λ(/u1D466.alt) to
Λ(/u1D466.alt)′, while the rate allocations of all other content consumers i s the same. Similarly, for a given content production
vector 𝑋 , we use 𝑋 {𝑧,𝑥 (𝑧) ′ } to denote that the content created by content producer 𝑧 ∈ 𝐶 changed from 𝑥 (𝑧) to 𝑥 (𝑧)′),
while the content created by all other content producers is t he same.
To prove the result of the lemma, we then have to establish the following three properties.
First, for a given allocation Ω = (𝜇inﬂ, Λ, 𝑋) we have show to that if the inﬂuencer /u1D466.altinﬂ changes its rate allocation
from 𝜇inﬂ to 𝜇′ inﬂ, then we have that
Φ(𝜇inﬂ, Λ, 𝑋) − Φ(𝜇′ inﬂ, Λ, 𝑋) = 𝑈inﬂ(𝜇inﬂ|Λ, 𝑋) − 𝑈inﬂ (𝜇′ inﬂ|Λ, 𝑋). (15)
Second, we have to show that if content consumer /u1D466.alt ∈ 𝐶 changes its rate allocation from Λ(/u1D466.alt) to Λ(/u1D466.alt)′, then we
have that
Φ(𝜇inﬂ, Λ, 𝑋) − Φ(𝜇inﬂ, Λ{/u1D466.alt,Λ(/u1D466.alt) ′ }, 𝑋) = 𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) − 𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)′|𝜇inﬂ, 𝑋). (16)
Finally, we have to show that if content producer 𝑧 ∈ 𝐶 changes its content from 𝑥 (𝑧) to 𝑥 (𝑧)′, then we have that
Φ(𝜇inﬂ, Λ, 𝑋) − Φ(𝜇inﬂ, Λ, 𝑋{𝑧,𝑥 (𝑧) ′ } ) = 𝑈𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) − 𝑈𝑝,𝑧 (𝑥′ (𝑧)| 𝜇inﬂ, Λ). (17)
The result that these three properties hold follows directly from the deﬁnitions of the objective functions𝑈inﬂ (𝜇inﬂ|Λ, 𝑋),
𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋), and 𝑈𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ), and we omit here a detailed derivation. □
Recall from Section 8 that S (𝑀inﬂ, 𝑀) is the set of all admissible allocations Ω = (𝜇inﬂ, Λ, 𝑋), i.e. the set of all alloca-
tions such the rate allocation 𝜇inﬂ is given by a non-negative vector that satisfy the rate budge t constraints 𝑀inﬂ of the
inﬂuencer, Λ(/u1D466.alt), /u1D466.alt ∈ 𝐶 is a non-negative vector that satisﬁes the rate budget const raint 𝑀 for the content consumers,
and we have that 𝑥 (𝑧) ∈ T , 𝑧 ∈ 𝐶.
We then have the following result.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 29
L/e.sc/m.sc/m.sc/a.sc 3. The set of all admissible allocations S (𝑀inﬂ, 𝑀) is a convex and compact set.
P/r.sc/o.sc/o.sc/f.sc. By Assumption 1 the set of all possible content allocations 𝑥 (𝑧) of a content producer are given by a convex
and compact set. Furthermore, by deﬁnition we have that the set of all non-negative rate allocations𝜇inﬂ of the inﬂuencer
that satisfy the budget constraint𝑀inﬂ is given by a convex and bounded set, and hence a convex and compact set. Finally,
by deﬁnition we have that the set of all non-negative rate all ocations Λ(/u1D466.alt) of a content consumer /u1D466.alt ∈ 𝐶 that satisfy
the budget constraint 𝑀 is given by a convex and bounded set, and hence a convex and com pact set. The result of the
lemma then follows. □
A.2 Proof of Proposition 1
Using Lemma 2, we proof Proposition 1 as follows.
By Lemma 2, the game with perfect information as given by Deﬁnition 7.1 is a potential game with potential function
Φ(Ω) =
/summationdisplay.1
/u1D466.alt ∈𝐶
𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋).
By Lemma 3, the domain S (𝑀inﬂ, 𝑀) of the potential function is convex and compact, and hence th ere exists an alloca-
tion Ω∗ that maximizes the potential function Φ(Ω), i.e. there exists an allocation Ω∗ ∈ S (𝑀inﬂ, 𝑀) such that
Ω∗ = arg max
Ω∈ S (𝑀inﬂ,𝑀 )
Φ(Ω).
Note that by the deﬁnition of the potential functionΦ(Ω), and by Eq. (15) to (17), the allocationΩ∗ is a Nash equilibrium
as given by Deﬁnition 7.1. The result of Proposition 1 follow s.
B PROOF OF PROPOSITION 2
Proposition 2 follows immediately from the proof of Proposi tion 1 which shows that there exists a Nash equilibrium
Ω∗ that maximizes the potential function Φ(Ω), i.e. there exists a Nash equilibrium Ω∗ such that
Ω∗ = arg max
Ω∈ S (𝑀inﬂ,𝑀 )
Φ(Ω),
where Φ(Ω) is the social welfare under allocation Ω, i.e. we have that
Φ(Ω) =
/summationdisplay.1
/u1D466.alt ∈𝐶
𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋).
C PROOF OF PROPOSITION 3
In this appendix, we provide proof for Proposition 3 which st ates that there exists a Nash equilibrium Ωinﬂ (𝑀, 𝑀inﬂ) =
(𝜇∗ inﬂ, Λ∗, 𝑋 ∗) for the game with imperfect information as given by Deﬁnitio n 9.1.
For our proof, we use Berge’s maximum theorem [27] and Brouwe r’s ﬁxed-point theorem [28], which are given as
follows.
T/h.sc/e.sc/o.sc/r.sc/e.sc/m.sc C.1 (M/a.sc/x.sc/i.sc/m.sc/u.sc/m.sc T/h.sc/e.sc/o.sc/r.sc/e.sc/m.sc). Let 𝐴, 𝐵, and 𝐶, be metrics spaces. Furthermore, let 𝐹 : 𝐴×𝐵 /u\i∈∞A6.e\dl→ 𝐶 be a continuous
function, and let 𝐺 : 𝐵 /u\i∈∞A6.e\dl→ 𝐴 be a compact valued and continuous correspondence such that 𝐺 (𝑏) ≠ ∅, 𝑏 ∈ 𝐵. Then, the
maximum value function
𝑉 (𝑏) = max
𝑎∈𝐺 (𝑏 )
𝐹 (𝑎, 𝑏), 𝑏 ∈ 𝐵,
is continuous.
Manuscript submitted to ACM

30 Junwei Su and Peter Marbach
We then obtain the following corollary.
C/o.sc/r.sc/o.sc/l.sc/l.sc/a.sc/r.sc/y.sc 1. Let 𝐴 and 𝐵 be non-empty compact and convex metrics spaces. Furthermor e, let 𝐹 : 𝐴 × 𝐵 /u\i∈∞A6.e\dl→ 𝐶 be a
continuous function. Then, the maximum value function
𝑉 (𝑏) = max
𝑎∈𝐴
𝐹 (𝑎, 𝑏), 𝑏 ∈ 𝐵,
is continuous.
T/h.sc/e.sc/o.sc/r.sc/e.sc/m.sc C.2 (B/r.sc/o.sc/u.sc/w.sc/e.sc/r.sc’/s.sc F/i.sc/x.sc/e.sc/d.sc/hyphen.sc/p.sc/o.sc/i.sc/n.sc/t.sc T/h.sc/e.sc/o.sc/r.sc/e.sc/m.sc). Let 𝐴 be a convex and compact metric space. Then every contin-
uous function 𝑓 : 𝐴 /u\i∈∞A6.e\dl→ 𝐴 has a ﬁxed point.
Using these two results, the outline of proof for Propositio n 3 is as follows.
(1) We ﬁrst construct a mapping F : S (𝑀inﬂ, 𝑀) /u\i∈∞A6.e\dl→ S ( 𝑀inﬂ, 𝑀) where
F = 𝑓 (1) ◦ 𝑓 (2) ◦ 𝑓 (2)
is a composition of the the optimal solution to the optimizat ion problem that deﬁne a Nash equilibrium for the
game with imperfect information as given by Deﬁnition 9.1.
(2) We next we use Berge’s Maximum theorem to show that each fu nction 𝑓 (1) , 𝑓 (2) , and 𝑓 (3) , is continuous, and
hence the mapping F is continuous.
(3) Finally, we use Brouwer’s ﬁxed-point theorem, we show th at mapping F = 𝑓 (1) ◦ 𝑓 (2) ◦ 𝑓 (3) has a ﬁxed point,
which corresponds to a Nash equilibrium for the game with imp erfect information as given by Deﬁnition 9.1.
C.1 Mapping F = 𝑓 (1) ◦ 𝑓 (2) ◦ 𝑓 (3)
In this appendix we deﬁned and analyze the mapping F : S (𝑀inﬂ, 𝑀) /u\i∈∞A6.e\dl→ S ( 𝑀inﬂ, 𝑀) given
F = 𝑓 (1) ◦ 𝑓 (2) ◦ 𝑓 (3) ,
where each function maps an allocation Ω ∈ S (𝑀inﬂ, 𝑀) to an optimal solution to the optimization problem that deﬁn e
a Nash equilibrium for the game with imperfect information a s given by Deﬁnition 9.1.
Given an allocation Ω = (𝜇inﬂ, Λ, 𝑋) ∈ S ( 𝑀inﬂ, 𝑀), the ﬁrst function 𝑓 (1) : S (𝑀inﬂ, 𝑀) /u\i∈∞A6.e\dl→ S ( 𝑀inﬂ, 𝑀) is given by
Ω (1) = ( 𝜇 (1) inﬂ , Λ(1) , 𝑋 (1) ) = 𝑓 (1) (Ω)
where
𝜇 (1) inﬂ = argmax 𝜇inﬂ ≥0 𝑈inﬂ (𝜇inﬂ|Λ, 𝑋) = 𝑟𝑝 /summationdisplay.1 𝑧 ∈𝐶 /summationdisplay.1 /u1D466.alt ∈𝐶\{ 𝑧 } 𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
subject to
/summationdisplay.1
𝑧 ∈𝐶
𝜇inﬂ (𝑧) ≤ 𝑀inﬂ,
and
Λ(1) = Λ and 𝑋 (1) = 𝑋 .
We then have the following result.
L/e.sc/m.sc/m.sc/a.sc 4. The function 𝑓 (1) : S (𝑀inﬂ, 𝑀) /u\i∈∞A6.e\dl→ S ( 𝑀inﬂ, 𝑀) is continuous.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 31
P/r.sc/o.sc/o.sc/f.sc. Using Assumption 1 and Corollary 1, in order to prove the resu lt of the lemma, it suﬃces to show that the
function
𝑈inﬂ (𝜇inﬂ|Λ, 𝑋) = 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt),
where
𝐵 (𝑧|/u1D466.alt) = 𝑞(𝑥 (𝑧)|𝑧)𝑝 (𝑥 (𝑧)|/u1D466.alt)
and
𝜃inﬂ (𝑧|/u1D466.alt) = 𝜃 (𝜇inﬂ (𝑧)) 𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) ,
is continuous on S (𝑀inﬂ, 𝑀).
Note that the distance function of a metric space is by deﬁnit ion continuous. By Assumption 2, the functions 𝑓 and
𝑔 are continuous. Combining these two results, we obtain that the functions 𝑝 (𝑥 |/u1D466.alt) and 𝑞(𝑥 |/u1D466.alt), 𝑥, /u1D466.alt ∈ T , given by
𝑝 (𝑥 |/u1D466.alt) = 𝑓 (𝑑 (𝑥, /u1D466.alt))
and
𝑞(𝑥 |/u1D466.alt) = 𝑔(𝑑 (𝑥, /u1D466.alt)),
are continuous. Furthermore by Assumption 3, the function𝜃 (𝜇), 𝜇 ≥ 0, is continuous. It then follows that the function
𝑓 (1) : S (𝑀inﬂ, 𝑀) /u\i∈∞A6.e\dl→ S ( 𝑀inﬂ, 𝑀) is a composition of continuous functions, and hence continu ous. The result of the
lemma then follows. □
Recall that the objective function of the optimization prob lem 𝑂𝑃𝑇𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) of content consumer /u1D466.alt ∈ 𝐶, is
given by (see Eq. (8))
𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) = 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
+ 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt)
+ 𝑟0𝜃 (𝜆(/u1D466.alt)) 𝐵0.
Given an allocation Ω = (𝜇inﬂ, Λ, 𝑋) ∈ S ( 𝑀inﬂ, 𝑀), the second function 𝑓 (2) : S (𝑀inﬂ, 𝑀) /u\i∈∞A6.e\dl→ S ( 𝑀inﬂ, 𝑀) is given by
Ω (2) = ( 𝜇 (2) inﬂ , Λ(2) , 𝑋 (2) ) = 𝑓 (2) (Ω)
where
Λ(2) (/u1D466.alt) = argmax
Λ(/u1D466.alt) ≥0
maximize 𝑈𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋)
subject to 𝜇 (/u1D466.altinﬂ|/u1D466.alt) + 𝜆(/u1D466.alt) +
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇 (𝑧|/u1D466.alt) ≤ 𝑀,
and
𝜇 (2) inﬂ = 𝜇inﬂ and 𝑋 (2) = 𝑋 .
We then have the following result.
L/e.sc/m.sc/m.sc/a.sc 5. The function 𝑓 (2) : S (𝑀inﬂ, 𝑀) /u\i∈∞A6.e\dl→ S ( 𝑀inﬂ, 𝑀) is continuous.
Lemma 5 can be proved using the same argument as given in the pr oof for Lemma 4. We omit here a detailed
derivation.
Manuscript submitted to ACM

32 Junwei Su and Peter Marbach
Recall from Section 9 that 𝜇∗ inﬂ (Λ, 𝑋) is the optimal rate allocation of the inﬂuencer /u1D466.altinﬂ as given by Eq. (7) for a given
rate allocation Λ of the content consumers and a given content allocation 𝑋 of the content producers, i.e. we have that
𝜇∗ inﬂ (Λ, 𝑋) = argmax
𝜇inﬂ ≥0
𝑈inﬂ (𝜇inﬂ|Λ, 𝑋) = 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
subject to
/summationdisplay.1
𝑧 ∈𝐶
𝜇inﬂ (𝑧) ≤ 𝑀inﬂ,
Furthermore, recall from Section 9 that 𝜇∗ inﬂ (𝑧|Λ, 𝑋) is the following rate that the inﬂuencer /u1D466.altinﬂ allocates to content
producer 𝑧 under 𝜇inﬂ (Λ, 𝑋).
Given an allocation Ω = (𝜇inﬂ, Λ, 𝑋), the third function 𝑓 (3) (Ω) is then given by
Ω (3) = ( 𝜇 (3) inﬂ , Λ(3) , 𝑋 (3) ) = 𝑓 (3) (Ω)
where
𝑥 (3) (𝑧) = argmax
𝑥 (𝑧) ∈ T
𝜃
(
𝜇∗ inﬂ (𝑧|Λ, 𝑋{𝑧,𝑥 (𝑧) }) ) , 𝑧 ∈ 𝐶,
and
𝜇 (3) inﬂ = 𝜇inﬂ and Λ(3) = Λ.
We then have the following result.
L/e.sc/m.sc/m.sc/a.sc 6. The function 𝑓 (3) : S (𝑀inﬂ, 𝑀) /u\i∈∞A6.e\dl→ S ( 𝑀inﬂ, 𝑀) is continuous.
P/r.sc/o.sc/o.sc/f.sc. Using Assumption 1 and Corollary 1, in order to prove the resu lt of the lemma, it suﬃces to show that the
function 𝜃 (𝜇∗ inﬂ (𝑧|Λ, 𝑋)) is continuous on S (𝑀inﬂ, 𝑀). By Assumption 3, the function 𝜃 (𝜇), 𝜇 ≥ 0, is continuous and
by Lemma 4 the function 𝜇∗ inﬂ (𝑧|Λ, 𝑋) is continuous on S (𝑀inﬂ, 𝑀). It then follows that the function 𝜃 (𝜇∗ inﬂ (𝑧|Λ, 𝑋)) is
continuous on S (𝑀inﬂ, 𝑀). This establishes the result of the lemma. □
C.2 Proof of Proposition 3
Let the three functions 𝑓 (1) , 𝑓 (2) , and 𝑓 (3) , be as deﬁned above. By the deﬁnition of the three functions 𝑓 (1) , 𝑓 (2) ,
and 𝑓 (3) , we have that a ﬁxed point of the function F : S (𝑀inﬂ, 𝑀) /u\i∈∞A6.e\dl→ S ( 𝑀inﬂ, 𝑀) given by F = 𝑓 (1) ◦ 𝑓 (2) ◦ 𝑓 (3) is a
Nash equilibrium of the game with imperfect information as g iven by Deﬁnition 9.1.
By Lemma 3, we have that the set S (𝑀inﬂ, 𝑀) is convex and compact. By Lemma 4 to 6, we have that each of the three
functions 𝑓 (1) , 𝑓 (2) , and 𝑓 (3) , is continuous. This implies that the function F = 𝑓 (3) ◦ 𝑓 (2) ◦ 𝑓 (1) (Ω) is a composition
of the continuous functions, and hence is itself continuous .
By Lemma 3 we have that the setS (𝑀inﬂ, 𝑀) is convex and compact. As the functionF it then follows from Brouwer’s
ﬁxed-point theorem that the function F has a ﬁxed point. As a ﬁxed point of the functionF : S (𝑀inﬂ, 𝑀) /u\i∈∞A6.e\dl→ S ( 𝑀inﬂ, 𝑀)
given by F = 𝑓 (1) ◦ 𝑓 (2) ◦ 𝑓 (3) is a Nash equilibrium of the game with imperfect information as given by Deﬁnition 9.1,
we obtain the result of Proposition 3.
D PROOF OF PROPOSITION 4
In this section we prove Proposition 4 which states that if Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium as given
by Deﬁnition 9.1 such that for content producer 𝑧 ∈ 𝐶 we have
𝜇∗ inﬂ (𝑧) > 0,
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 33
and /summationdisplay.1
𝑧′ ∈𝐶\{ 𝑧 }
𝜇∗ inﬂ (𝑧′) > 0,
then we have
𝑥∗ (𝑧) = argmax
𝑥 (𝑧) ∈ T
𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇∗ inﬂ, Λ∗),
where
𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) = 𝑟𝑝 /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
and
𝜃inﬂ (𝑧|/u1D466.alt) = 𝜃 (𝜇inﬂ (𝑧)) 𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) .
D.1 Preliminary Results
To prove Proposition 4, we ﬁrst derive the following two lemm as.
L/e.sc/m.sc/m.sc/a.sc 7. If Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium for the game with imperfect informatio n as given by
Deﬁnition 9.1 such that for content producer 𝑧0 ∈ 𝐶 we have
𝜇∗ inﬂ (𝑧0) > 0
and /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧0 }
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0,
then we have that
𝑥∗ (𝑧0) = argmax
𝑥 (𝑧0 ) ∈ T
𝜃
(
𝜇∗ inﬂ (𝑧0|Λ∗, 𝑋∗ {𝑧0,𝑥 (𝑧0 ) }) ) ,
if and only if
𝑥∗ (𝑧0) = argmax
𝑥 (𝑧0 ) ∈ T
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧0 }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧0|/u1D466.alt),
where
𝐵 (𝑧0|/u1D466.alt) = 𝑞(𝑥 (𝑧0)|𝑧0)𝑝 (𝑥 (𝑧0)|/u1D466.alt).
P/r.sc/o.sc/o.sc/f.sc. By Assumption 3, the function 𝜃 (𝜇), 𝜇 ≥ 0, is strictly increasing. It then follows that if there exists a content
type 𝑥 such that
𝜃
(
𝜇∗ inﬂ (𝑧0|Λ∗, 𝑋∗ {𝑧0,𝑥 (𝑧0 ) }) ) > 0,
then content producer𝑧0 maximizes 𝜃
(
𝜇∗ inﬂ (𝑧0|Λ∗, 𝑋∗ {𝑧0,𝑥 (𝑧0 ) }) ) , if and only if producer𝑧0 maximizes the rate 𝜇∗ inﬂ (𝑧0|Λ∗, 𝑋∗ {𝑧0,𝑥 (𝑧0 ) }).
By deﬁnition, the rate 𝜇∗ inﬂ (𝑧0|Λ∗, 𝑋∗ {𝑧0,𝑥 (𝑧0 ) }) is given by the rate that the inﬂuencer/u1D466.altinﬂ allocates to content producer
𝑧0 under an optimal solution 𝜇∗ inﬂ to the maximization problem 𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ∗, 𝑋 ∗ {𝑧0,𝑥 (𝑧0 ) }) given by (see Eq. (7))
maximize
𝜇inﬂ ≥0
𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
subject to
/summationdisplay.1
𝑧 ∈𝐶
𝜇inﬂ (𝑧) ≤ 𝑀inﬂ.
Manuscript submitted to ACM

34 Junwei Su and Peter Marbach
Using Assumption 4, without loss of generality we can assumethat an optimal solution𝜇∗ inﬂ to the maximization problem
𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ∗, 𝑋∗ {𝑧0,𝑥 (𝑧0 ) }) we have /summationdisplay.1
𝑧 ∈𝐶
𝜇∗ inﬂ (𝑧) = 𝑀inﬂ.
This implies that for an optimal solution 𝜇∗ inﬂ to the maximization problem 𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ∗, 𝑋∗ {𝑧0,𝑥 (𝑧0 ) }), there exists a
Lagrange multiplier 𝛼∗ (𝑥 (𝑧0)) such that
𝜇∗ inﬂ (𝑧) = 𝐺
( 𝛼∗ (𝑥 (𝑧0))
𝑟𝑝𝛾 (𝑧)
)
, 𝑧 ∈ 𝐶, (18)
and /summationdisplay.1
𝑧 ∈𝐶
𝐺
( 𝛼∗ (𝑥 (𝑧0))
𝑟𝑝𝛾 (𝑧)
)
= 𝑀inﬂ, (19)
where
𝛾 (𝑧) =
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) 𝑞(𝑥 (𝑧)|𝑧)𝑝 (𝑥 (𝑧)|/u1D466.alt) 𝑧 ∈ 𝐶,
and 𝐺 (𝑏), 𝑏 ≥ 0, is the inverse function of 𝜃 ′ (𝜇), 𝜇 ≥ 0. Note that by Assumption 3, the derivative 𝜃 ′ (𝜇), 𝜇 ≥ 0 is
strictly decreasing, and hence the function 𝐺 (𝑏), 𝑏 ≥ 0, is well-deﬁned.
As by Assumption 3 the function 𝜃 (𝜇), 𝜇 ≥ 0, is concave, it follows that 𝜇∗ inﬂ is an optimal solution to the maximiza-
tion problem 𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ, 𝑋{𝑧,𝑥 (𝑧0 ) }) if and only if the optimality conditions given by Eq. (18) and (19) hold.
Note that by Assumption 3, the function 𝐺 (𝑏), 𝑏 ≥ 0, is is strictly decreasing. As a result we have that the lowe r the
value of 𝛼∗ (𝑥 (𝑧0))/𝛾 (𝑧), the higher the value of the function 𝐺 (𝛼∗ (𝑥 (𝑧0))/𝑟𝑝𝛾 (𝑧)). As by assumption we have that
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧0 }
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0,
and hence by Assumption 3 we have that
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧0 }
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) > 0,
it then follows that if the content production 𝑥∗ (𝑧), 𝑧 ∈ 𝐶\{𝑧0}, of all content producers other than producer 𝑧0 are
ﬁxed, then the following is true. Content producer 𝑧0 maximizes 𝐺 (𝛼 (𝑥 (𝑧0))/𝛾 (𝑧), and hence maximizes 𝜇∗ inﬂ (𝑧), if and
only if 𝑥 (𝑧0) maximizes 𝛾 (𝑧0) and we have that
𝑥∗ (𝑧0) = argmax
𝑥 (𝑧0 ) ∈ T
𝑟𝑝
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧0 }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧0|/u1D466.alt),
where
𝐵 (𝑧0|/u1D466.alt) = 𝑞(𝑥 (𝑧0)|𝑧)𝑝 (𝑥 (𝑧0)|/u1D466.alt).
The result of the lemma then follows. □
L/e.sc/m.sc/m.sc/a.sc 8. If Ω = (𝜇inﬂ, Λ, 𝑋) is an allocation such that for content producer 𝑧 ∈ 𝐶 we have
𝜇inﬂ(𝑧) > 0
and /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜇 (/u1D466.altinﬂ|/u1D466.alt) > 0,
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 35
then we have that
𝑥∗ (𝑧) = argmax
𝑥 (𝑧) ∈ T
𝑈
inﬂ
𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ),
if and only if
𝑥∗ (𝑧) = argmax
𝑥 (𝑧) ∈ T
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt),
where
𝐵 (𝑧|/u1D466.alt) = 𝑞(𝑥 (𝑧)|𝑧)𝑝 (𝑥 (𝑧)|/u1D466.alt).
The result of Lemma 8 follows immediately from the deﬁnition of the function 𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) (see Eq. (13)), i.e.
we have that
𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) = 𝑟𝑝 /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt),
where
𝜃inﬂ (𝑧|/u1D466.alt) = 𝜃 (𝜇inﬂ (𝑧)) 𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) .
D.2 Proof of Proposition 4
The result of Proposition 4 follows immediately from Lemma 7 and Lemma 8.
E PROOF FOR PROPOSITION 5
In this appendix we prove Proposition 5, which states that in a large community where the inﬂuencer allocates a large
rate budget 𝑀inﬂ, there exists a Nash equilibrium Ω∗ inﬂ (𝑀, 𝑀inﬂ) for the game with imperfect information that maximizes
the social welfare, i.e. we have that
Φ
(
Ω∗ inﬂ (𝑀, 𝑀inﬂ) ) = Φ ( Ω∗ (𝑀inﬂ, 𝑀) ) ,
where
Ω∗ (𝑀inﬂ, 𝑀) = argmax
Ω∈ S (𝑀inﬂ,𝑀 )
Φ(Ω).
In order to prove this result, we introduce another interact ion between content producer and consumers, and the
inﬂuencer, to which we refer as the proxy game. Under this gam e, content consumers are constrained to only follow
the inﬂuencer, i.e. consumers can obtain content only throu gh the inﬂuencer. In the following, we show that in a large
community where the inﬂuencer allocates a large rate budget 𝑀inﬂ we have that ΩNE (𝑀, 𝑀inﬂ) is Nash equilibrium for
the game with perfect information, and Ωinﬂ (𝑀, 𝑀inﬂ) is Nash equilibrium for the game with imperfect information , if
an only if they are a Nash equilibrium for the proxy game. We th en use this result to prove Proposition 5.
To do that, we proceed as follows. In Subsection E.1, we forma lly deﬁne the proxy game. In Subsections E.2 and E.3,
we provide the result that ΩNE (𝑀, 𝑀inﬂ) is Nash equilibrium for the game with perfect information, a nd Ωinﬂ (𝑀, 𝑀inﬂ)
is Nash equilibrium for the game with imperfect information , if an only if they are a Nash equilibrium for the proxy
game. Finally, we Subsection E.4, we prove Proposition 5.
E.1 Proxy Game
Under the proxy game, content consumers are constrained to o nly follow the inﬂuencer, i.e. content consumers can
obtain content only through the inﬂuencer. The optimizatio n problem of content consumer /u1D466.alt ∈ 𝐶 is now to choose a
Manuscript submitted to ACM

36 Junwei Su and Peter Marbach
rate allocation Λ∗ (/u1D466.alt) that solves the following optimization problem,
maximize
Λ(/u1D466.alt) ≥0
𝑟0𝜃 (𝜆(/u1D466.alt)) 𝐵0 + 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
subject to 𝜆(/u1D466.alt) + 𝜇 (/u1D466.altinﬂ|/u1D466.alt) ≤ 𝑀,
(20)
where 𝑀 > 0 is the rate budget available to content consumer/u1D466.alt. We refer to this maximization problem as𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋).
The optimization problem of the inﬂuencer and content produ cer stay the same as given by Eq. (7), and Eq. (10),
respectively.
A Nash equilibrium for the proxy game is then deﬁned as follow s.
D/e.sc/f.sc/i.sc/n.sc/i.sc/t.sc/i.sc/o.sc/n.sc E.1. An allocation Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium for the proxy game if we have
that
(1) 𝜇∗ inﬂ is a solution for the maximization problem 𝑂𝑃𝑇inﬂ (𝜇inﬂ|Λ∗, 𝑋∗),
(2) Λ∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋 ∗) with
𝜇 (𝑧|/u1D466.alt) = 0, 𝑧 ∈ 𝐶\{/u1D466.alt},
(3) 𝑥∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇𝑝,/u1D466.alt (𝑥 (/u1D466.alt)| 𝜇∗ inﬂ, Λ∗).
The following result states that the proxy game is a potentia l game.
L/e.sc/m.sc/m.sc/a.sc 9. The proxy game is a potential game with potential function
Φ𝑝𝑟𝑜𝑥 (Ω𝑝𝑟𝑜𝑥 ) = /summationdisplay.1
/u1D466.alt ∈𝐶
𝑈 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋),
where 𝑈 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) is the consumption utility of community member /u1D466.alt under the proxy game given by
𝑈 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) = 𝑟0𝜃 (𝜆(/u1D466.alt)) 𝐵0 + 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt).
Using the result of Lemma 9, we obtain the following result.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 6. There exists a Nash equilibrium Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) for the proxy game as given by
Deﬁnition E.1.
We can prove Lemma 9 and Proposition 6 using the same argument as given to prove Lemma 2 and Proposition 1
for the game with perfect information as deﬁned in Subsectio n 7.4. We omit here a detailed proof.
We provide an analysis of the properties of a Nash equilibriu m Ω𝑝𝑟𝑜𝑥 for the proxy game in Appendix F.
E.2 Properties of Nash equilibrium ΩNE (𝑀, 𝑀infl)
The following result connects a Nash equilibrium ΩNE (𝑀, 𝑀inﬂ) for the game with perfect information with a Nash
equilibrium for the proxy game.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 7. Let 𝑀 be a given rate budget for the content consumers. Then there e xists a integer 𝑁0 and a constant
𝑘inﬂ such that if 𝑁 > 𝑁0, and 𝑀inﬂ > 𝑁 𝑘inﬂ, the following is true. An ΩNE (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium
of the game with perfect information as given by Deﬁnition 7. 1, if and only if ΩNE (𝑀, 𝑀inﬂ) is a Nash equilibrium for the
proxy game as given by Deﬁnition E.1.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 37
We provide a proof for Proposition 7 in Appendix G. While the r esult of Proposition 7 is intuitive, its proof is
surprisingly involved.
E.3 Properties of Nash equilibrium Ω∗ infl (𝑀, 𝑀infl)
In addition, we have the following result that connects a Nas h equilibrium Ωinﬂ (𝑀, 𝑀inﬂ) for the game with imperfect
information with a Nash equilibrium for the proxy game.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 8. Let 𝑀 be a given rate budget for the content consumers. Then there e xists a integer 𝑁0 and a constant
𝑘inﬂ such that if 𝑁 > 𝑁0, and 𝑀inﬂ > 𝑁 𝑘inﬂ, the following is true. An allocation Ωinﬂ = (𝜇inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium
of the game with imperfect information as given by Deﬁnition 9.1, if and only if Ω∗ inﬂ (𝑀, 𝑀inﬂ) is a Nash equilibrium for
the proxy game as given by Deﬁnition E.1.
We provide a proof for Proposition 8 in Appendix H.
E.4 Proof of Proposition 5
Using Proposition 7 and Proposition 8, we can prove Proposit ion 5 as follows.
Combining Proposition 7 and Proposition 8, we obtain the following result. For a given rate budget𝑀 for the content
consumers, then there exists a integer 𝑁0 and a constant 𝑘inﬂ such that if 𝑁 > 𝑁0, and 𝑀inﬂ > 𝑁 𝑘inﬂ, the following is true.
An ΩNE (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium of the game with perfect information as given by Deﬁnition 7.1,
if and only if Ωinﬂ (𝑀, 𝑀inﬂ) is a Nash equilibrium for the game with imperfect informatio n as given by Deﬁnition 9.1.
Furthermore, by Proposition 2 there always exists a Nash equilibrium Ω∗ NE (𝑀, 𝑀inﬂ) that maximizes the social welfare,
i.e. we have
Φ
(
Ω∗ NE (𝑀, 𝑀inﬂ) ) = Φ ( Ω∗ (𝑀inﬂ, 𝑀) ) ,
where
Ω∗ (𝑀inﬂ, 𝑀) = argmax
Ω∈ S (𝑀inﬂ,𝑀 )
Φ(Ω).
Combining the above two results, it obtain the following result. For a given rate budget 𝑀 for the content consumers,
there exists a integer 𝑁0 and a constant 𝑘inﬂ such that if 𝑁 > 𝑁0, and 𝑀inﬂ > 𝑁 𝑘inﬂ, then the following is true. Let
Ω∗ NE (𝑀, 𝑀inﬂ) is a Nash equilibrium for the game with perfect information t hat maximizes the social welfare. Then
Ω∗ inﬂ (𝑀, 𝑀inﬂ) = Ω∗ NE (𝑀, 𝑀inﬂ),
is a Nash equilibrium Ω∗ inﬂ (𝑀, 𝑀inﬂ) with imperfect information that maximizes the social welfa re. The result of Propo-
sition 5 then follows.
F ANALYSIS OF OF NASH EQUILIBRIUM Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀infl) FOR PROXY GAME
In this section, we analyze the properties of a Nash equilibrium of the proxy game as given by Deﬁnition E.1. Recall that
under this game, content consumers are constrained to only f ollow the inﬂuencer, i.e. consumers can obtain content
only through the inﬂuencer.
Manuscript submitted to ACM

38 Junwei Su and Peter Marbach
Recall that for the proxy game, the objective of content cons umer /u1D466.alt ∈ 𝐶 is now to choose a rate allocation Λ∗ (/u1D466.alt)
that solves the following optimization problem 𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇inﬂ, 𝑋) given by (see Eq. (20))
maximize
Λ(/u1D466.alt) ≥0
𝑟0𝜃 (𝜆(/u1D466.alt)) 𝐵0 + 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
subject to 𝜆(/u1D466.alt) + 𝜇 (/u1D466.altinﬂ|/u1D466.alt) ≤ 𝑀,
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇 (𝑧|/u1D466.alt) = 0.
where 𝑀 > 0 is the rate budget available to content consumer /u1D466.alt.
The optimization problem of the inﬂuencer and content produ cer stay the same and are given by Eq. (7), and Eq. (8),
respectively.
In the following we analyze the properties of a Nash equilibr ium Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) of the proxy game.
F.1 Optimality Conditions for Nash Equilibrium Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀infl)
We ﬁrst derive necessary and suﬃcient conditions for a Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) to be a Nash equilibrium for
the proxy game as given by Deﬁnition E.1
L/e.sc/m.sc/m.sc/a.sc 10. Under Assumption 4, an Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium as given by Deﬁnition E.1,
if an only if the following conditions hold true,
a) For all content producers𝑧 ∈ 𝐶, the content allocation𝑥∗ (𝑧) is a solution for the maximization problem𝑂𝑃𝑇𝑝,/u1D466.alt (𝑥 (/u1D466.alt)| 𝜇inﬂ, Λ).
b) For all content consumers /u1D466.alt ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇∗(𝑧|/u1D466.alt) = 0.
c) For all content consumers /u1D466.alt ∈ 𝐶 we have that
𝜆∗ (/u1D466.alt) + 𝜇∗(/u1D466.altinﬂ|/u1D466.alt) = 𝑀.
d) If for content consumer /u1D466.alt ∈ 𝐶 we have that 𝜆∗ (/u1D466.alt) > 0, then we have
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0 ≥ 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ(𝑧) ) 𝐵 (𝑧|/u1D466.alt).
e) If for content consumer /u1D466.alt ∈ 𝐶 we have that 𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0, then we have
𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ (𝑧) ) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0.
f) We have that /summationdisplay.1
𝑧 ∈𝐶
𝜇∗ inﬂ (𝑧) = 𝑀inﬂ.
g) If for content producer 𝑧 ∈ 𝐶 we have that 𝜇∗ inﬂ (𝑧) > 0, then we have for 𝑧′ ∈ 𝐶\{𝑧} that
𝜃 ′
(
𝜇∗ inﬂ (𝑧) ) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ ( 𝜇∗ inﬂ (𝑧′) ) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt).
P/r.sc/o.sc/o.sc/f.sc. Recall that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium of the proxy game as given by Deﬁnition E.1,
if an only if the following conditions hold true,
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 39
1) 𝜇∗ inﬂ is a solution for the maximization problem 𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ∗, 𝑋 ∗),
2) Λ∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋∗) with
𝜇 (𝑧|/u1D466.alt) = 0, 𝑧 ∈ 𝐶\{/u1D466.alt},
3) 𝑥∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇𝑝,/u1D466.alt (𝑥 (/u1D466.alt)| 𝜇∗ inﬂ, Λ∗).
To show that the result of the lemma holds, we have to show that the above Properties 1)-3) hold if and only if the
Properties a)-g) in the statement of the lemma hold.
As Property a) is identical to Property 3), in order to show th at the above Properties 1)-3) hold if and only if the
Properties a)-f) in the statement of the lemma hold, it suﬃce s to prove the following two statements.
First, we have that Λ∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋∗) (Property 1)), if
and only if Properties b)-e) hold.
Second, we have that 𝜇∗ inﬂ is a solution for the maximization problem 𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ∗, 𝑋 ∗) (Property 2)), if and only if
Properties f) and g) hold.
We ﬁrst prove that that Λ∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋∗) (Property
1)), if and only if Properties b)-e) hold.
Note that Property b) follows from the deﬁnition of the proxy game which states that content consumers can get
content only through the inﬂuencer, and hence we have that if Λ∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem
𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋∗) with /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇∗(𝑧|/u1D466.alt) = 0.
Note that by deﬁnition we have that 𝐵0 > 0. As a result, if Property c) does not hold and we have that
𝜆∗ (/u1D466.alt) + 𝜇∗(/u1D466.altinﬂ|/u1D466.alt) < 𝑀,
then we increase the objective function in the maximization problem 𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋∗) by setting
𝜆(/u1D466.alt) = 𝜆∗ (/u1D466.alt) + 𝜖0,
where
𝜖0 = 𝑀 −
[
𝜆∗ (/u1D466.alt) + 𝜇∗(/u1D466.altinﬂ|/u1D466.alt) ] > 0.
As a result, we have that if Λ∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋∗), then we
have that, then we have that
𝜆∗ (/u1D466.alt) + 𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) = 𝑀.
Using the two constraints given by Properties b) and c), Prop erties d) and e) correspond to the ﬁrst-order optimality
conditions for the optimization problem 𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋∗). As by Assumption 3 the function 𝜃 (𝜇), 𝜇 ≥ 0, is
concave, it follows that Λ∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem 𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋∗), if and only if
it satisﬁes the ﬁrst-order optimality conditions.
Combining the above results, it followsΛ∗ (/u1D466.alt), /u1D466.alt ∈ 𝐶, is a solution to the maximization problem𝑂𝑃𝑇 𝑝𝑟𝑜𝑥 𝑐,/u1D466.alt (Λ(/u1D466.alt)| 𝜇∗ inﬂ, 𝑋 ∗)
(Property 1)), if and only if Properties b)-e) hold.
Using the same line of argument as given for Property 1), one c an show that under Assumption 4 we have that 𝜇∗ inﬂ
is a solution for the maximization problem 𝑂𝑃𝑇 inﬂ (𝜇inﬂ|Λ∗, 𝑋∗) (Property 2)), if and only if Properties f) and g) hold. We
omit here a detailed derivation.
Manuscript submitted to ACM

40 Junwei Su and Peter Marbach
The result of the lemma then follows. □
F.2 Properties of Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀infl) for /summationtext.1 /u1D466.alt ∈𝐶 𝜇∗(/u1D466.altinfl |/u1D466.alt) > 0
We next characterize the properties of a Nash equilibrium Ω𝑝𝑟𝑜𝑥 = (𝜇∗ inﬂ, Λ∗, 𝑋∗) such that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0. (21)
In Appendix F.4 we provide conditions under which the inequa lity given by Eq. (21) holds.
L/e.sc/m.sc/m.sc/a.sc 11. If Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium for the proxy game given by Deﬁnition E. 1 such
that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0,
then we have that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) > 0.
P/r.sc/o.sc/o.sc/f.sc. By Assumption 3 we have that the function 𝜃 (𝜇), 𝜇 ≥ 0, is concave. As a result, we have that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) ≥ 𝜃 /parenlefttpA/parenleftexA
/parenleftbtA
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)/parenrighttpA/parenrightexA
/parenrightbtA
.
Furthermore, by Assumption 3 we have that the function 𝜃 (𝜇), 𝜇 ≥ 0, is positive. As a result, if we have that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0,
then we obtain that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) ≥ 𝜃 /parenlefttpA/parenleftexA
/parenleftbtA
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt)/parenrighttpA/parenrightexA
/parenrightbtA
> 0.
This establishes the result of the lemma. □
L/e.sc/m.sc/m.sc/a.sc 12. Let 𝛼, 0 < 𝛼 < 0.5, be a given constant, then the following is true. If Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a
Nash equilibrium for the proxy game given by Deﬁnition E.1 su ch that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) > 0,
then there exists a content producer 𝑧0 ∈ 𝐶 such that
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) > 𝛼 /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) , 𝑧 ∈ 𝐶\{𝑧0}.
P/r.sc/o.sc/o.sc/f.sc. Let 𝜖0 be given by
𝜖0 =
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) > 0.
Suppose that the result of the lemma is not true, and for 𝛼, 0 < 𝛼 < 0.5, there exist two content producer 𝑧0, 𝑧′ ∈ 𝐶,
𝑧0 ≠ 𝑧′, such that /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) < 𝛼𝜖0
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 41
and /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧0 }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) < 𝛼𝜖0.
As by assumption we have that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) = 𝜖0 > 0,
we obtain that
𝜃 (𝜇 (/u1D466.altinﬂ|𝑧0)) > (1 − 𝛼)𝜖0
and
𝜃 (𝜇 (/u1D466.altinﬂ|𝑧′)) > (1 − 𝛼)𝜖0.
Using the fact that for 𝛼 we have that
0 < 𝛼 < 0.5,
it follows that /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) > (1 − 𝛼)𝜖0 > 𝛼𝜖0
and /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧0 }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) > (1 − 𝛼)𝜖0 > 𝛼𝜖0.
This leads to a contradiction to our assumption that
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) < 𝛼𝜖0
and /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧0 }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) < 𝛼𝜖0.
Hence we have that there is a most one content producer 𝑧0 such that for 𝛼, 0 < 𝛼 < 0.5, we have that
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) < 𝛼𝜖0.
This establishes the result of the lemma. □
L/e.sc/m.sc/m.sc/a.sc 13. For every 𝜇0 > 0 there exists a constant 𝑘inﬂ such that if 𝑀inﬂ > 𝑁 𝑘inﬂ, then the following is true. If
Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium for the proxy game given by Deﬁnition E. 1 such that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0,
then there exists a content producer 𝑧0 ∈ 𝐶 such that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶\{𝑧0}.
P/r.sc/o.sc/o.sc/f.sc. From Lemma 1, we have that there exists a 𝑝min > 0 and 𝑞min > 0 such that
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑝min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T ,
and
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑞min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T .
Manuscript submitted to ACM

42 Junwei Su and Peter Marbach
Given a target following rate 𝜇0 and a constant 𝛼, 0 < 𝛼 < 0.5, let 𝑘inﬂ then be such that
𝑘inﬂ > 𝜇0
and
𝜃 ′ (𝑘inﬂ) < 𝜃 ′ (𝜇0) 𝑝min𝑞min𝛼.
Such a 𝑘/u1D466.altinﬂ exists as from Assumption 3 we have that
𝜃 ′ (𝜇) > 0, 𝜇 ∈ R+,
and
lim𝜇→∞ 𝜃 ′ (𝜇) = 0.
Furthermore, let 𝑧0 ∈ 𝐶 be such that
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) > 𝛼 /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) , 𝑧 ∈ 𝐶\{𝑧0}.
Such a 𝑧0 ∈ 𝐶 exists by Lemma 12.
Using these values of 𝜇0 and 𝑘/u1D466.altinﬂ , as well as our choice of 𝑧0 ∈ 𝐶, we then show if Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗)
is a Nash equilibrium of the proxy game given by Deﬁnition E.1 with a rate budget 𝑀inﬂ > 𝑁 𝑘inﬂ, then we have that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶\{𝑧0}.
We show this result by contradiction as follows. Suppose that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium of
the proxy game given by Deﬁnition E.1 with a rate budget𝑀inﬂ > 𝑁 𝑘inﬂ, and there exists a content producer𝑧′ ∈ 𝐶\{𝑧0}
such
𝜇∗ inﬂ (𝑧0) < 𝜇0
and
𝜇∗ inﬂ (𝑧′) < 𝜇0.
As by Property f) of Lemma 10 we have that
/summationdisplay.1
𝑧 ∈𝐶
𝜇∗ inﬂ (𝑧) = 𝑀inﬂ = 𝑁 𝑘inﬂ
and by construction we have that
𝜇∗ inﬂ (𝑧′) < 𝜇0 < 𝑘inﬂ,
it follows that there exists a content producer 𝑧′′ ∈ 𝐶 such that
𝜇∗ inﬂ (𝑧′′) ≥ 𝑘inﬂ.
We then proceed as follows. First note that for all content pr oducers 𝑧 ∈ 𝐶 we have
𝑝min𝑞min
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≤
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≤
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) .
Using Lemma 12 and the fact that b
By Assumption 3 the function 𝜃 (𝜇), 𝜇 ≥ 0, is concave, and we have
𝜇0 ≥ 𝜇∗ inﬂ (𝑧′)
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 43
that
𝜃 ′ (𝜇∗ inﬂ (𝑧′)) ≥ 𝜃 ′ (𝜇0) ,
Using Lemma 12 and our choice of 𝑧0, we have for the content producer 𝑧′ as given above that
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) > 𝛼 /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) ,
and
𝜃 ′ (𝜇0) 𝑝min𝑞min𝛼 /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧′|/u1D466.alt) < 𝜃 ′ (𝜇∗ inﬂ (𝑧′)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧′|/u1D466.alt).
Similarly, as for the content consumer 𝑧′′ as deﬁned above we have
𝜇∗ inﬂ (𝑧′′) ≥ 𝑘/u1D466.altinﬂ,
we obtain that
𝜃 ′ (𝜇∗ inﬂ (𝑧′′)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′′ }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧′|/u1D466.alt) ≤ 𝜃 ′ (𝑘/u1D466.altinﬂ ) /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) .
As we have chosen the constant 𝑘/u1D466.altinﬂ such that
𝜃 ′ (𝑘inﬂ) < 𝜃 ′ (𝜇0) 𝑝min𝑞min𝛼,
we have that
𝜃 ′ (𝑘inﬂ) /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) < 𝜃 ′ (𝜇0) 𝑝min𝑞min𝛼 /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) ,
and it follows from the above inequalities that
𝜃 ′ (𝜇∗ inﬂ (𝑧′′)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′′ }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧′′|/u1D466.alt) < 𝜃 ′ (𝜇∗ inﬂ (𝑧′)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧′|/u1D466.alt).
However, as by construction we have that
𝜇∗ inﬂ (𝑧′′) ≥ 𝑘/u1D466.altinﬂ,
this violates Property g) of the Lemma 10 which provides the necessary and suﬃcient conditions for a Nash equilibrium
of the proxy game. This contradicts our assumption that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium of the
proxy game as given by Deﬁnition E.1. The result of the lemma t hen follows. □
L/e.sc/m.sc/m.sc/a.sc 14. For every 𝜇0 > 0 there exists a 𝑘inﬂ such that if 𝑀inﬂ > 𝑁 𝑘inﬂ then the following is true. If Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) =
(𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium for the proxy game given by Deﬁnition E. 1 such that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0,
then for every content consumer /u1D466.alt ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ (𝑧) ) ≥ ( 𝑁 − 2)𝜃 (𝜇0) .
The result of this lemma follows immediately from Lemma 13, and from Assumption 3 which states that the function
𝜃 (() 𝜇), 𝜇 ≥ 0, is strictly increasing.
Manuscript submitted to ACM

44 Junwei Su and Peter Marbach
F.3 Properties of Nash Equilibrium Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀infl) for /summationtext.1 𝑧 ∈𝐶\{ /u1D466.alt } 𝜃 (𝜇∗ infl (𝑧)) ≥ 𝑁 𝛼𝜅0
We next characterize the properties of a Nash equilibrium Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) such that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ 𝑁 𝛼𝜅0.
L/e.sc/m.sc/m.sc/a.sc 15. Let 𝑀 be a given rate budget. Then for every 𝜅0 > 0 and 𝛼, 0 < 𝛼 < 0.5, there exist constants 𝑁0 and 𝜖0 > 0
such that if 𝑁 > 𝑁0, then the following is true. If Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium for the proxy
game given by Deﬁnition E.1 such that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ (𝑧) ) ≥ 𝛼𝑁 𝜅0, /u1D466.alt ∈ 𝐶,
then we have that
𝜇 (/u1D466.altinﬂ|/u1D466.alt) > 𝜖0, /u1D466.alt ∈ 𝐶.
P/r.sc/o.sc/o.sc/f.sc. Let 𝜅0 > 0 and 𝛼, 0 < 𝛼 < 0.5, be given constants. From Lemma 1 we have that there exists a 𝑝min > 0 and
𝑞min > 0 such that
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑝min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T
and
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑞min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T .
Note that we have that
𝑝min𝑞min𝜅0
𝐵0
> 0.
We then choose 𝑁0 and 𝜖0, 0 < 𝜖0 < 𝑀, such that
𝜃 ′ (𝑀 − 𝜖0) 𝑟0𝐵0 < 𝜃 ′ (𝜖0) 𝑟𝑝𝑝min𝑞min𝛼 (𝑁0 − 2)𝜅0.
Note that such constants exist.
Using these values for 𝑁0 and 𝜖0, we then show that if 𝑁 > 𝑁0 and Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash
equilibrium for the proxy game given by Deﬁnition E.1, such t hat for content consumer /u1D466.alt ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ 𝛼𝑁 𝜅0,
then we have that
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 𝜖0.
We show this result by contradiction as follows. For 𝑁 > 𝑁0, suppose that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash
equilibrium of the proxy game given by Deﬁnition E.1 such tha t for content consumer /u1D466.alt ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ 𝛼𝑁 𝜅0
and
𝜇 (/u1D466.altinﬂ|/u1D466.alt) ≤ 𝜖0.
By construction we have
0 < 𝜖0 < 𝑀,
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 45
and we obtain that
𝜆∗ (/u1D466.alt) ≥ 𝑀 − 𝜖0 > 0.
We then proceed as follows. Combining the fact that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ 𝛼𝑁 𝜅0
and
𝜇 (/u1D466.altinﬂ|/u1D466.alt) ≤ 𝜖0,
with Assumption 3 that states that the function 𝜃 (𝜇), 𝜇 ≥ 0, is concave, we obtain that
𝜃 ′ (𝜖0) 𝑝min𝑞min𝛼 (𝑁0 − 2)𝜅0 ≤ 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt).
Furthermore, as we have that
𝜆∗ (/u1D466.alt) ≥ 𝑀 − 𝜖0 > 0,
and as by Assumption 3 the function 𝜃 (𝜇), 𝜇 ≥ 0, is concave, we obtain that
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝐵0 ≤ 𝜃 ′ (𝑀 − 𝜖0) 𝐵0.
By construction, we have that
𝜃 ′ (𝑀 − 𝜖0) 𝑟0𝐵0 < 𝜃 ′ (𝜖0) 𝑟𝑝 𝑝min𝑞min𝛼 (𝑁0 − 2)𝜅0
and we obtain from the above inequalities that
𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt) > 𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0.
However, as by construction we have that
𝜆∗ (/u1D466.alt) ≥ 𝑀 − 𝜖0 > 0,
this violates Property d) of Lemma 10, which provides necess ary and suﬃcient conditions for a Nash equilibrium for
the proxy game. This implies that the allocation Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is not a Nash equilibrium for the proxy
game given by Deﬁnition E.1.
This contradicts our assumption that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium for the proxy game given
by Deﬁnition E.1. The result of the lemma then follows. □
F.4 Properties of Nash Equilibrium Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀infl)
Finally, we derive the key properties of a Nash equilibrium Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) for the proxy game as given
by Deﬁnition E.1.
The ﬁrst result provides conditions such that for a Nash equi librium Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) of the proxy
game we have /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0.
L/e.sc/m.sc/m.sc/a.sc 16. There exist constants 𝑁0 and 𝑘inﬂ such that if 𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ, then the following is true. If
Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium for the game with perfect information a s given by Deﬁnition E.1,
Manuscript submitted to ACM

46 Junwei Su and Peter Marbach
then we have that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0.
P/r.sc/o.sc/o.sc/f.sc. From Lemma 1 we have that there exists a 𝑝min > 0 and 𝑞min > 0 such that
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑝min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T
and
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑞min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T .
We then choose constants 𝑁0 and 𝑘inﬂ > 0 such that
𝜃 ′ (0) 𝑟0𝐵0 < 𝜃 ′ (0) (𝑁0 − 1)𝑟𝑝𝑝min𝑞min𝜃 (𝑘inﬂ) 𝐵0 .
Note that such constants exist.
We then show that the following is true for these values for 𝑁0 and 𝑘inﬂ. If for 𝑁 > 𝑁0 we have that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) =
(𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium with 𝑀inﬂ > 𝑁 𝑘inﬂ, then we have
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0.
We prove this results by contradiction as follows. For 𝑁 > 𝑁0, suppose that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a
Nash equilibrium as given by Deﬁnition E.1 with 𝑀inﬂ > 𝑁 𝑘inﬂ, such that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) = 0.
Note that in this case we have that
𝜆∗ (/u1D466.alt) = 𝑀 > 0.
We then proceed as follows. As for the Nash equilibrium Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) we have that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) = 0,
we obtain from Assumption 4 that in this case we have
𝜇∗ inﬂ (𝑧) = 𝑀inﬂ/𝑁 = 𝑘inﬂ, 𝑧 ∈ 𝐶.
It then follows that for every content consumer /u1D466.alt ∈ 𝐶 we have
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇∗ inﬂ (𝑧) = (𝑁 − 1)𝜃 (𝑘inﬂ) .
We then have that for 𝑁 > 𝑁0 that
(𝑁0 − 1)𝜃 ′ (0) 𝑝min𝑞min𝜃 (𝑘inﬂ) ≤ 𝜃 ′ (0) /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt).
Furthermore as by Assumption 3 the function 𝜃 (𝜇), 𝜇 ≥ 0, is concave, we have that
𝜃 ′ (𝑀) 𝐵0 ≤ 𝜃 ′ (0) 𝐵0.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 47
As by construction we have that
𝜃 ′ (0) 𝑟0𝐵0 < 𝜃 ′ (0) (𝑁0 − 1)𝑟𝑝𝑝min𝑞min𝜃 (𝑘inﬂ) 𝐵0 ,
we obtain from the above inequalities that
𝜃 ′ (𝑀) 𝑟0𝐵0 < 𝜃 ′ (0) /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt).
However, as by assumption we have that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) = 0
and hence
𝜆∗ (/u1D466.alt) = 𝑀 > 0,
this violates Property d) of the Lemma 10 which provides the necessary and suﬃcient conditions for a Nash equilibrium
of the proxy game. This contradicts our assumption that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium of the
proxy game as given by Deﬁnition E.1. The result of the lemma t hen follows. □
The next result states that if the community size 𝑁 and the rate budget 𝑀inﬂ of the inﬂuencer are large enough, then
under a Nash equilibrium of the proxy game we have that each co nsumer follows the inﬂuencer with a positive rate.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 9. Let 𝑀 be a given rate budget. Then there exist constants 𝑁0, 𝑘inﬂ, and 𝜖0 > 0, such that if 𝑁 > 𝑁0 and
𝑀inﬂ > 𝑁 𝑘inﬂ, the following is true. If Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium for the proxy game given by
Deﬁnition E.1, then we have that
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 𝜖0, /u1D466.alt ∈ 𝐶.
P/r.sc/o.sc/o.sc/f.sc. Given the rate budget 𝑀, we choose the constants 𝑁0 > 2, 𝑘inﬂ, and 𝜖0 > 0, such that for 𝑁 > 𝑁0 and
𝑀inﬂ > 𝑁 𝑘inﬂ the following properties are true:
(1) If Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium for the proxy game given by Deﬁnition E. 1, such that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0,
then for every content consumer /u1D466.alt ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ ( 𝑁 − 2)𝜃 (𝜇0) .
(2) If Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium for the proxy game given by Deﬁnition E. 1, such that
for content consumer /u1D466.alt ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ 𝛼𝑁 𝜅0,
then we have that
𝜇 (/u1D466.altinﬂ|/u1D466.alt) > 𝜖0.
(3) If Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium for the proxy game given by Deﬁnition E. 1, then we
have that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0.
Manuscript submitted to ACM

48 Junwei Su and Peter Marbach
Such constants 𝑁0 > 2, 𝑘inﬂ and 𝜖0 exist by Lemma 14, Lemma 15, and Lemma 16.
Note that for these values of 𝑁0 > 2, 𝑘inﬂ and 𝜇0 > 0, we have from Property 2) that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ 𝛼𝑁 𝜅0
with
𝛼 = 1 3
and
𝜅0 = 𝜃 (𝜇0) > 0.
The result of the lemma then follows immediately from Proper ty 3). □
The next result states that if the community size 𝑁 and the rate budget 𝑀inﬂ of the inﬂuencer are large enough, then
under a Nash equilibrium of the proxy game we that the inﬂuene r allocates a large rate to each producer 𝑧 ∈ 𝐶.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 10. Let 𝑀 be a given rate budget, and let 𝜇0 be a given rate. Then there exist constants 𝑁0 and 𝑘inﬂ such
that if 𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ, the following is true. If Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium of the
proxy game given by Deﬁnition E.1, then we have that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶.
P/r.sc/o.sc/o.sc/f.sc. From Lemma 1, we have that there exists a 𝑝min > 0 and 𝑞min > 0 such that
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑝min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T ,
and
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑞min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T .
Given the rate budget 𝑀, we choose the constants 𝑁0 > 2, 𝑘inﬂ > 0, and 𝜖0 > 0, such that for 𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ
the following properties are true:
(1) If Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium for the proxy game given by Deﬁnition E. 1, then we
have that
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 𝜖0, /u1D466.alt ∈ 𝐶.
(2) 𝜃 ′ (𝑘inﬂ) 𝜃 (𝑀) < 𝜃 ′ (𝜇0) 𝑝min𝑞min𝜃 (𝜖0).
(3) 𝑘/u1D466.altinﬂ > 𝜇0.
Such constants exist by Proposition 9 and by Assumption 3 whi ch states that for the function 𝜃 (𝜇), 𝜇 ≥ 0, we have
that
𝜃 ′ (𝜇) > 0, 𝜇 ∈ R+,
and
lim𝜇→∞ 𝜃 ′ (𝜇) = 0.
Using these values of 𝜇0, 𝑘/u1D466.altinﬂ , and 𝑚, we then show if Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ∗, 𝑋∗) is an optimal Nash equilibrium
of the proxy game given by Deﬁnition E.1 with a rate budget 𝑀inﬂ > 𝑁 𝑘inﬂ, then we have that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 49
We show this result by contradiction as follows. Suppose tha t Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ∗, 𝑋 ∗) is an optimal Nash
equilibrium of the proxy game given by Deﬁnition E.1 with a ra te budget 𝑀inﬂ > 𝑁 𝑘inﬂ, and there exists a content
producer 𝑧0 ∈ 𝐶 such
𝜇∗ inﬂ (𝑧0) < 𝜇0.
As by construction we have that
𝑘/u1D466.altinﬂ | > 𝜇0,
it follows from Property f) of Lemma 10 that in this case there exists a content producer 𝑧′ ∈ 𝐶 such that
𝜇∗ inﬂ (𝑧′) ≥ 𝑘/u1D466.altinﬂ,
We then proceed as follows. First note that for every content producer 𝑧 ∈ 𝐶 that
𝑝min𝑞min (𝑁 − 1)𝜃 (𝜖0) ≤
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇𝑖) 𝐵 (𝑧|/u1D466.alt) ≤ ( 𝑁 − 1)𝜃 (𝑀) .
We then have for the content producer 𝑧0 as given above that
𝜃 ′ (𝜇0) ( 𝑁 − 1)𝑝min𝑞min𝜃 (𝜖0) ≤ 𝜃 ′ (𝜇∗ inﬂ (𝑧0)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧0 }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧0|/u1D466.alt).
Similarly, for the content consumer 𝑧′ as deﬁned above, we have that
𝜃 ′ (𝜇∗ inﬂ (𝑧′)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧0|/u1D466.alt) ≤ 𝜃 ′ (𝑘inﬂ) ( 𝑁 − 1)𝜃 (𝑀) ,
where we used the fact that by Assumption 3 the function 𝜃 (𝜇) is concave.
As we have chosen the constant 𝑘/u1D466.altinﬂ such that
𝜃 ′ (𝑘inﬂ) 𝜃 (𝑀) < 𝜃 ′ (𝜇0) 𝑝min𝑞min𝜃 (𝜖0)
we have that
𝜃 ′ (𝑘inﬂ) ( 𝑁 − 1)𝜃 (𝑀) < 𝜃 ′ (𝜇0) ( 𝑁 − 1)𝑝min𝑞min𝜃 (𝜖0) ,
and it follows from the above two inequalities that
𝜃 ′ (𝜇∗ inﬂ (𝑧′)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧′|/u1D466.alt) < 𝜃 ′ (𝜇∗ inﬂ (𝑧0)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧0 }
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧0|/u1D466.alt).
However, as by construction we have that
𝜇∗ inﬂ (𝑧′) ≥ 𝑘/u1D466.altinﬂ > 0,
this violates Property g) of the Lemma 10 which provides the necessary and suﬃcient conditions for a Nash equilibrium
of the proxy game. This contradicts our assumption that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium of the
proxy game as given by Deﬁnition E.1. The result of the propos ition then follows
□
G ANALYSIS OF NASH EQUILIBRIUM ΩNE (𝑀, 𝑀infl) FOR GAME WITH PERFECT INFORMATION
In this section, we derive additional properties of a Nash eq uilibrium of the game with perfect information as given by
Deﬁnition 7.1 that we use to in Appendix G.6 to prove Proposit ion 7.
Manuscript submitted to ACM

50 Junwei Su and Peter Marbach
G.1 Preliminary Result
We ﬁrst derive a result on the properties of an allocation Ω = (𝜇inﬂ, Λ, 𝑋) that we use in our analysis.
Recall from Section 8 that S (𝑀inﬂ, 𝑀) is the set of all admissible allocations Ω = (𝜇inﬂ, Λ, 𝑋), i.e. the set of all non-
negative following rate allocations 𝜇inﬂ and Λ that satisfy the rate budget constraints 𝑀inﬂ for inﬂuencer, and the rate
budget constraint 𝑀 for all content consumers /u1D466.alt ∈ 𝐶, respectively, and all the content allocations𝑋 such that 𝑥 (𝑧) ∈ T ,
𝑧 ∈ 𝐶.
We then have the following lemma.
L/e.sc/m.sc/m.sc/a.sc 17. For a given rate budget 𝑀, there constants 𝑁0 and 𝜇0 such that for 𝑁 > 𝑁0 the following is true. If
Ω = (𝜇inﬂ, Λ, 𝑋) ∈ 𝑆 (𝑀, 𝑀inﬂ) is an admissible allocation such that
𝜇inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶,
then we have for all content consumers /u1D466.alt ∈ 𝐶 that
𝜃 ′ (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) < 𝜃 ′ (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝐵 (𝑧|/u1D466.alt)𝜃 (𝜇inﬂ (𝑧)) , 𝑧 ∈ 𝐶\{/u1D466.alt}.
P/r.sc/o.sc/o.sc/f.sc. From Lemma 1 we have that there exists a 𝑝min > 0 and 𝑞min > 0 such that
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑝min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T
and
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑞min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T .
Given the rate budget 𝑀, we choose the constants 𝑁0 and 𝜇0 such that
𝜃 ′ (0) < 𝜃 ′ (𝑀) ( 𝑁0 − 1)𝑝min𝑞min𝜃 (𝜇0) .
Note that such constants exist.
By Assumption 3 the function 𝜃 (𝜇), 𝜇 ≥ 0, is concave, and we have that
𝜃 ′ (𝜇∗(𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≤ 𝜃 ′ (0) .
By Assumption 3 the function 𝜃 (𝜇), 𝜇 ≥ 0, is concave and strictly increasing, and we have that
𝜃 ′ (𝑀) ( 𝑁0 − 1)𝑝min𝑞min𝜃 (𝜇0) ≤ 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt).
By construction we have that
𝜃 ′ (0) < 𝜃 ′ (𝑀) ( 𝑁0 − 1)𝑝min𝑞min𝜃 (𝜇0) ,
and it follows from the above inequalities that
𝜃 ′ (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) < 𝜃 ′ (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧′ ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇inﬂ (𝑧′)) 𝐵 (𝑧′|/u1D466.alt), 𝑧 ∈ 𝐶\{/u1D466.alt}.
This establishes the result of the lemma. □
G.2 Optimality Condition for Nash Equilibrium ΩNE (𝑀, 𝑀infl)
The next result provides necessary and suﬃcient conditions for a Nash equilibrium of the game with perfect informa-
tion.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 51
L/e.sc/m.sc/m.sc/a.sc 18. An ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium as given by Deﬁnition 7.1, if an only if t he following
conditions hold true,
a) For all content producers𝑧 ∈ 𝐶, the content allocation𝑥∗ (𝑧) is a solution for the maximization problem𝑂𝑃𝑇𝑝,/u1D466.alt (𝑥 (/u1D466.alt)| 𝜇inﬂ, Λ).
b) For all content consumers /u1D466.alt ∈ 𝐶 we have that
𝜆∗ (/u1D466.alt) + 𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) + /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇∗(𝑧|/u1D466.alt) = 𝑀
c) If for content consumer /u1D466.alt ∈ 𝐶 we have that 𝜆∗ (/u1D466.alt) > 0, then we have
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0 ≥ 𝜃 ′ (𝜇∗(𝑧|/u1D466.alt)) 𝑟𝑝𝐵 (𝑧|/u1D466.alt), 𝑧 ∈ 𝐶\{/u1D466.alt}
and
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0 ≥ 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ(𝑧) ) 𝐵 (𝑧|/u1D466.alt).
d) If for content consumer /u1D466.alt ∈ 𝐶 we have that 𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0, then we have
𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧′ ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ(𝑧′) ) 𝐵 (𝑧′|/u1D466.alt) ≥ 𝜃 ′ (𝜇∗ (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt), 𝑧 ∈ 𝐶\{/u1D466.alt}
and
𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ (𝑧) ) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0.
e) If for content consumer /u1D466.alt ∈ 𝐶 and content producer 𝑧 ∈ 𝐶\{/u1D466.alt} we have that 𝜇∗(𝑧|/u1D466.alt) > 0, then we have
𝜃 ′ (𝜇∗(𝑧|/u1D466.alt)) 𝑟𝑝𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0,
𝜃 ′ (𝜇∗ (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧′ ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ (𝑧′) ) 𝐵 (𝑧′|/u1D466.alt),
and
𝜃 ′ (𝜇∗(𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜇∗(𝑧′|/u1D466.alt)) 𝐵 (𝑧′|/u1D466.alt), 𝑧 ′ ∈ 𝐶\{/u1D466.alt, 𝑧}.
f) We have that /summationdisplay.1
𝑧 ∈𝐶
𝜇∗ inﬂ (𝑧) = 𝑀inﬂ.
g) If for content producer 𝑧 ∈ 𝐶 we have that 𝜇∗ inﬂ (𝑧) > 0, then we have for 𝑧′ ∈ 𝐶\{𝑧} that
𝜃 ′
(
𝜇∗ inﬂ (𝑧) ) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ ( 𝜇∗ inﬂ (𝑧′) ) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧′|/u1D466.alt).
We can prove Lemma 18 using the same line of argument that we us ed to prove Lemma 10, and we omit here a
detailed proof.
G.3 Properties of Nash Equilibrium ΩNE (𝑀, 𝑀infl) for /summationtext.1 /u1D466.alt ∈𝐶 𝜇∗ (/u1D466.altinfl|/u1D466.alt) > 0
We next characterize the properties of a Nash equilibrium Ω𝑝𝑟𝑜𝑥 = (𝜇∗ inﬂ, Λ∗, 𝑋∗) such that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0. (22)
In Appendix G.5 we provide conditions under which the inequa lity given by Eq. (22) holds.
Manuscript submitted to ACM

52 Junwei Su and Peter Marbach
The following lemmas, Lemma 19 - 22, can be proved using the sa me argument as given in the proof for Lemma 11 -
14 that we obtained for the proxy game in Appendix F, and we omi t here detailed proofs.
L/e.sc/m.sc/m.sc/a.sc 19. If ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium for the game with perfect information a s given by
Deﬁnition 7.1 such that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇 (/u1D466.altinﬂ|/u1D466.alt) > 0,
then we have that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) > 0.
L/e.sc/m.sc/m.sc/a.sc 20. Let 𝛼, 0 < 𝛼 < 0.5, be a given constant, then the following is true. If ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash
equilibrium for the game with perfect information as given b y Deﬁnition 7.1 such that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇 (/u1D466.altinﬂ|/u1D466.alt) > 0,
then there exists a content producer 𝑧0 ∈ 𝐶 such that
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) > 𝛼 /summationdisplay.1
/u1D466.alt ∈𝐶
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) , 𝑧 ∈ 𝐶\{𝑧0}.
L/e.sc/m.sc/m.sc/a.sc 21. For every 𝜇0 > 0 there exists a constant 𝑘inﬂ such that if 𝑀inﬂ > 𝑁 𝑘inﬂ, then the following is true. If
ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium for the game with perfect information a s given by Deﬁnition 7.1
such that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇 (/u1D466.altinﬂ|/u1D466.alt) > 0,
then there exists a content producer 𝑧0 ∈ 𝐶 such that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶\{𝑧0}.
L/e.sc/m.sc/m.sc/a.sc 22. For every 𝜇0 > 0 there exists a 𝑘inﬂ such that if 𝑀inﬂ > 𝑁 𝑘inﬂ then the following is true. If ΩNE (𝑀, 𝑀inﬂ) =
(𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium for the game with perfect information a s given by Deﬁnition 7.1 such that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇 (/u1D466.altinﬂ|/u1D466.alt) > 0,
then for every content consumer /u1D466.alt ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ (𝑧) ) ≥ ( 𝑁 − 2)𝜃 (𝜇0) .
G.4 Properties of Nash Equilibrium ΩNE (𝑀, 𝑀infl) for /summationtext.1 𝑧 ∈𝐶\{ /u1D466.alt } 𝜃 (𝜇∗ infl (𝑧)) ≥ 𝛼𝑁 𝜅0
We next characterize the properties of a Nash equilibrium ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) such that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ 𝑁 𝛼𝜅0.
L/e.sc/m.sc/m.sc/a.sc 23. Let 𝑀 be a given rate budget. Then for every 𝜅0 > 0 and 𝛼, 0 < 𝛼 < 0.5, there exist constants 𝑁0 and 𝜖0 > 0
such that if 𝑁 > 𝑁0, then the following is true. If ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium for the game with
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 53
perfect information as given by Deﬁnition 7.1 such that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ (𝑧) ) ≥ 𝛼𝑁 𝜅0, /u1D466.alt ∈ 𝐶,
then we have that
𝜇 (/u1D466.altinﬂ|/u1D466.alt) > 𝜖0, /u1D466.alt ∈ 𝐶.
P/r.sc/o.sc/o.sc/f.sc. Let 𝜅0 > 0 and 𝛼, 0 < 𝛼 < 0.5, be given constants.
From Lemma 1 we have that there exists a 𝑝min > 0 and 𝑞min > 0 such that
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑝min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T
and
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑞min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T .
Note that we have that
𝑝min𝑞min𝜅0
𝐵0
> 0.
We then choose the integer 𝑁0 and 𝜖0 such that
0 < 𝜖0 < 𝑀,
and
𝜃 ′ (0) max{𝑟𝑝, 𝑟0𝐵0} < 𝜃 ′ (𝜖0) 𝛼𝑁 0𝜅0𝑟𝑝𝑝min𝑞min.
Note that such a 𝑁0 and 𝜖0 exist.
Using these values for 𝑁0 and 𝜖0, we then show that if𝑁 > 𝑁0 and ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium
for the proxy game given by Deﬁnition 7.1, such that for conte nt consumer /u1D466.alt ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ 𝛼𝑁 𝜅0,
then we have that
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 𝜖0.
We show this result by contradiction as follows. For 𝑁 > 𝑁0, suppose that ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash
equilibrium of the proxy game given by Deﬁnition 7.1 such tha t for content consumer /u1D466.alt0 ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt0 }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ 𝛼𝑁 𝜅0
and
𝜇 (/u1D466.altinﬂ|/u1D466.alt0) ≤ 𝜖0.
Using Property b) of Lemma 18, we have in this case for content consumer /u1D466.alt0 ∈ 𝐶 that either
𝜆∗ (/u1D466.alt0) > 0 (23)
or there exists a content producer 𝑧 ∈ 𝐶\{/u1D466.alt} such that
𝜇∗(𝑧|/u1D466.alt0) > 0. (24)
Manuscript submitted to ACM

54 Junwei Su and Peter Marbach
We then proceed as follows. Combining the fact that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt0 }
𝜃 (𝜇∗ inﬂ (𝑧)) ≥ 𝛼𝑁 𝜅0
and
𝜇 (/u1D466.altinﬂ|/u1D466.alt0) ≤ 𝜖0,
with Assumption 3, which states that the function 𝜃 (𝜇), 𝜇 ≥ 0, is concave, we obtain that
𝜃 ′ (𝜖0) 𝑝min𝑞min𝛼 (𝑁0 − 2)𝜅0 ≤ 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt0)) /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt0 }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt0).
Furthermore, as by Assumption 3 the function 𝜃 (𝜇), 𝜇 ≥ 0, is concave, we have that
𝜃 ′ (𝜆∗ (/u1D466.alt0)) 𝐵0 ≤ 𝜃 ′ (0) 𝐵0
and
𝜃 ′ (𝜇∗(𝑧′|/u1D466.alt0)) 𝐵 (𝑧′|/u1D466.alt) ≤ 𝜃 ′ (0) .
By construction, we have that
0 < 𝜖0 < 𝑀,
and
𝜃 ′ (0) max{𝑟𝑝, 𝑟0𝐵0} < 𝜃 ′ (𝜖0) 𝛼𝑁 0𝜅0𝑟𝑝𝑝min𝑞min,
and we obtain from the above inequalities that
𝜃 ′ (𝜆∗ (/u1D466.alt0)) 𝑟0𝐵0 < 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt0)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt0 }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt) (25)
and
𝜃 ′ (𝜇∗(𝑧′|/u1D466.alt0)) 𝐵 (𝑧′|/u1D466.alt0) < 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt0)) /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt0 }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt0). (26)
However, by Lemma 18, and Eq. (23) and Eq. (24), we either have that
𝜆∗ (/u1D466.alt0) > 0
or there exists a content producer 𝑧 ∈ 𝐶\{/u1D466.alt0} such that
𝜇∗(𝑧|/u1D466.alt0) > 0,
and the inequalities given by Eq. (25) and Eq. (26) either vio late Property c) or e) of Lemma 18. This contradicts our
assumption that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium as given by Deﬁnition 7.1. The result of the
lemma then follows. □
G.5 Properties of Nash Equilibrium ΩNE (𝑀, 𝑀infl)
Finally, we derive the key properties of a Nash equilibrium ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) for the game with perfect
information as given by Deﬁnition 7.1.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 55
The ﬁrst result provides conditions such that for a Nash equi librium ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) of the game with
perfect information we have /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0.
L/e.sc/m.sc/m.sc/a.sc 24. There exist constants 𝑁0 and 𝑘inﬂ such that if 𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ, then the following is true. If
ΩNE (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ∗, 𝑋 ∗) is a equilibrium of the game with perfect information as give n by Deﬁnition 7.1, then we
have that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0.
P/r.sc/o.sc/o.sc/f.sc. From Lemma 1 we have that there exists a 𝑝min > 0 and 𝑞min > 0 such that
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑝min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T
and
𝑝 (𝑥 |/u1D466.alt) ≥ 𝑞min, /u1D466.alt ∈ 𝐶, 𝑥 ∈ T .
We then choose constants 𝑁0 and 𝑘inﬂ > 0 such that
𝜃 ′ (0) max{1, 𝐵0} < 𝜃 ′ (0) (𝑁0 − 1)𝑝min𝑞min𝜃 (𝑘inﬂ) 𝐵0 .
Note that such constants exists.
We then show that the following is true for these values for 𝑁0 and 𝑘inﬂ. If for 𝑁 > 𝑁0 we have that ΩNE (𝑀, 𝑀inﬂ) =
(𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium with 𝑀inﬂ > 𝑁 𝑘inﬂ, then we have
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0.
We prove this results by contradiction as follows. For 𝑁 > 𝑁0, suppose that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a
Nash equilibrium as given by Deﬁnition 7.1 with 𝑀inﬂ > 𝑁 𝑘inﬂ, such that
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) = 0.
Using Property b) of Lemma 18, we have in this case for every co ntent consumer /u1D466.alt ∈ 𝐶 that either
𝜆∗ (/u1D466.alt) > 0 (27)
or there exists a content producer 𝑧 ∈ 𝐶\{/u1D466.alt} such that
𝜇∗ (𝑧|/u1D466.alt) > 0. (28)
We then obtain the following results. As by Assumption 3 the f unction 𝜃 (𝜇), 𝜇 ≥ 0, is concave, we have that
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝐵0 ≤ 𝜃 ′ (0) 𝐵0, /u1D466.alt ∈ 𝐶,
and
𝜃 ′ (𝜇∗ (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≤ 𝜃 ′ (0) , /u1D466.alt ∈ 𝐶, 𝑧 ∈ 𝐶\{/u1D466.alt}.
By Assumption 4, we have for the case where
/summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) = 0
Manuscript submitted to ACM

56 Junwei Su and Peter Marbach
that
𝜇∗ inﬂ (𝑧) = 𝑀inﬂ/𝑁 = 𝑘inﬂ, 𝑧 ∈ 𝐶.
It then follows that for 𝑁 > 𝑁0 we that
(𝑁0 − 1)𝜃 ′ (0) 𝑝min𝑞min𝜃 (𝑘inﬂ) ≤ 𝜃 ′ (0) /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt).
As by construction we have that
𝜃 ′ (0) max{𝑟𝑝, 𝑟0𝐵0} < 𝜃 ′ (0) (𝑁0 − 1)𝑟𝑝𝑝min𝑞min𝜃 (𝑘inﬂ) 𝐵0 ,
we obtain from the above inequalities that
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0 < 𝜃 ′ (0) /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt), /u1D466.alt ∈ 𝐶, (29)
and
𝜃 ′ (𝜇∗(𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) < 𝜃 ′ (0) /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt), /u1D466.alt ∈ 𝐶, 𝑧 ∈ 𝐶\{/u1D466.alt}. (30)
However, by Lemma 18, and Eq. (27) and Eq. (28), we either have that
𝜆∗ (/u1D466.alt) > 0
or there exists a content producer 𝑧 ∈ 𝐶\{/u1D466.alt} such that
𝜇∗ (𝑧|/u1D466.alt) > 0,
and the inequalities given by Eq. (29) and Eq. (30) either vio late Property c) or e) of Lemma 18. This contradicts our
assumption that Ω𝑝𝑟𝑜𝑥 (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium as given by Deﬁnition 7.1. The result of the
lemma then follows. □
The next result states that if the community size 𝑁 and the rate budget 𝑀inﬂ of the inﬂuencer are large enough, then
under a Nash equilibrium of the game with perfect informatio n we have that each consumer follows the inﬂuencer
with a positive rate.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 11. Let 𝑀 be a given rate budget. Then there exist constants 𝑁0, 𝑘inﬂ, and 𝜖0 > 0, such that if 𝑁 > 𝑁0
and 𝑀inﬂ > 𝑁 𝑘inﬂ, the following is true. If ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium as given by Deﬁnition 7.1,
then we have that
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) ≥ 𝜖0, /u1D466.alt ∈ 𝐶.
Proposition 11 can be proved using the same argument as given in the proof for Proposition 9, and we omit here a
detailed derivation.
The next result states that if the community size 𝑁 and the rate budget 𝑀inﬂ of the inﬂuencer are large enough, then
under a Nash equilibrium of the game with perfect informatio n we that the inﬂuencer allocates a large rate to each
producer 𝑧 ∈ 𝐶.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 12. Let 𝑀 be a given rate budget, and let 𝜇0 be a given rate. Then there exist constants 𝑁0 and 𝑘inﬂ such
that if 𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ, the following is true. If ΩNE (𝑀, 𝑀inﬂ) (𝑀inﬂ) = (𝜇 (𝑀inﬂ ) inﬂ , Λ∗, 𝑋∗) is a Nash equilibrium of
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 57
the game with perfect information as given by Deﬁnition 7.1, then we have that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶.
Proposition 12 can be proved using the same argument as given in the proof for Proposition 10, and we omit here
a detailed derivation.
The next result states that if the community size 𝑁 and the rate budget 𝑀inﬂ of the inﬂuencer are large, then the all
consumers /u1D466.alt ∈ 𝐶 will get their content through the inﬂuencer.
L/e.sc/m.sc/m.sc/a.sc 25. For a given rate budget 𝑀, there exist constants 𝑁0 and 𝜇0 such that for 𝑁 > 𝑁0 the following is true. If
ΩNE (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ, 𝑋) is a Nash equilibrium for the game with perfect information a s given by Deﬁnition 7.1, such
that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶,
then we have for all content consumers /u1D466.alt ∈ 𝐶 that
𝜇∗ (𝑧|/u1D466.alt) = 0, 𝑧 ∈ 𝐶\{/u1D466.alt}.
P/r.sc/o.sc/o.sc/f.sc. Let 𝑀 be a given rate budget. From Lemma 17, we have that there exist exist constants 𝑁0 and 𝜇0 such that
for 𝑁 > 𝑁0 the following is true. If ΩNE (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ, 𝑋) is a Nash equilibrium as given by Deﬁnition 7.1 such
that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶,
then we have for all content consumers /u1D466.alt ∈ 𝐶 that
𝜃 ′ (𝜇∗(𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) < 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧′ ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧′)) 𝐵 (𝑧′|/u1D466.alt), 𝑧 ∈ 𝐶\{/u1D466.alt}.
Combining this result with Lemma 18 which gives the necessar y and suﬃcient conditions for a Nash equilibrium, we
obtain that there exist constants 𝑁0 and 𝜇0 such that for 𝑁 > 𝑁0 the following is true. If ΩNE (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ, 𝑋) is
a Nash equilibrium as given by Deﬁnition 7.1 such that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶,
then we have for all content consumers /u1D466.alt ∈ 𝐶 that
𝜇∗ (𝑧|/u1D466.alt) = 0, 𝑧 ∈ 𝐶\{/u1D466.alt}.
This establishes the result of the lemma. □
G.6 Proof of Proposition 7
In this appendix we provide a proof for Proposition 7. Recall that Proposition 7 states that for a given rate budget 𝑀,
there exist constants 𝑁0 and 𝜇0 such that for 𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ, then the following is true. The allocation
ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium of the game with perfect information as given by Deﬁnition 7.1, if
and only if ΩNE (𝑀, 𝑀inﬂ) is a Nash equilibrium for the proxy game.
We prove Proposition 7 as follows. Let 𝑀 be a given rate budget. Then by Lemma 17 and Lemma 25 there exis t
constants 𝑁0 and 𝜇0 such that the following is true. If ΩNE (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ, 𝑋) is a Nash equilibrium as given by
Deﬁnition 7.1 such that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶,
Manuscript submitted to ACM

58 Junwei Su and Peter Marbach
then we have for all content consumers /u1D466.alt ∈ 𝐶 that
𝜃 ′ (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) < 𝜃 ′ (𝜇 (/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧′ ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇inﬂ (𝑧′)) 𝐵 (𝑧′|/u1D466.alt), 𝑧 ∈ 𝐶\{/u1D466.alt}
and
𝜇∗ (𝑧|/u1D466.alt) = 0, 𝑧 ∈ 𝐶\{/u1D466.alt}.
As a result, from Lemma 17, Lemma 18, and Lemma 25, we have that there exist constants 𝑁0 and 𝑘inﬂ such that for
𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ the following is true. An ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium as given by
Deﬁnition 7.1, if an only if the following conditions hold tr ue,
a) For all content producers 𝑧 ∈ 𝐶, the content allocation 𝑥∗ (𝑧) is a solution for the maximization problem
𝑂𝑃𝑇𝑝,/u1D466.alt (𝑥 (/u1D466.alt)| 𝜇inﬂ, Λ).
b) For all content consumers /u1D466.alt ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇∗(𝑧|/u1D466.alt) = 0.
c) For all content consumers /u1D466.alt ∈ 𝐶 we have that
𝜆∗ (/u1D466.alt) + 𝜇∗(/u1D466.altinﬂ|/u1D466.alt) + /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇∗(𝑧|/u1D466.alt) = 𝑀
d) If for content consumer /u1D466.alt ∈ 𝐶 we have that 𝜆∗ (/u1D466.alt) > 0, then we have
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0 ≥ 𝜃 ′ (𝜇∗(𝑧|/u1D466.alt)) 𝑟𝑝𝐵 (𝑧|/u1D466.alt), 𝑧 ∈ 𝐶\{/u1D466.alt}
and
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0 ≥ 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt).
e) If for content consumer /u1D466.alt ∈ 𝐶 we have that 𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0, then we have
𝜃 ′ (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0.
f) For all content consumers /u1D466.alt ∈ 𝐶 we have that
𝜃 ′ (0) 𝐵 (𝑧|/u1D466.alt) < 𝜃 ′ (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧′ ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧′)) 𝐵 (𝑧|/u1D466.alt′), 𝑧 ∈ 𝐶\{/u1D466.alt}
g) We have that /summationdisplay.1
𝑧 ∈𝐶
𝜇∗ inﬂ (𝑧) = 𝑀inﬂ.
h) If for content producer 𝑧 ∈ 𝐶 we have that 𝜇∗ inﬂ (𝑧) > 0, then we have for 𝑧′ ∈ 𝐶\{𝑧} that
𝜃 ′ (𝜇∗ inﬂ (𝑧)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜇∗ inﬂ (𝑧′)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧′|/u1D466.alt).
In addition, from Lemma 17 and Lemma 10 we have that there exis t constants 𝑁0 and 𝑘inﬂ such that for 𝑁 > 𝑁0 and
𝑀inﬂ > 𝑁 𝑘inﬂ the following is true. An ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium of the proxy game as given
by Deﬁnition E.1, if an only if the following conditions hold true,
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 59
a’) For all content producers 𝑧 ∈ 𝐶, the content allocation 𝑥∗ (𝑧) is a solution for the maximization problem
𝑂𝑃𝑇𝑝,/u1D466.alt (𝑥 (/u1D466.alt)| 𝜇inﬂ, Λ).
b’) For all content consumers /u1D466.alt ∈ 𝐶 we have that
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇∗(𝑧|/u1D466.alt) = 0.
c’) For all content consumers /u1D466.alt ∈ 𝐶 we have that
𝜆∗ (/u1D466.alt) + 𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) = 𝑀.
d’) If for content consumer /u1D466.alt ∈ 𝐶 we have that 𝜆∗ (/u1D466.alt) > 0, then we have
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0 ≥ 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt).
e’) If for content consumer /u1D466.alt ∈ 𝐶 we have that 𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0, then we have
𝜃 ′ (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0.
f’) For all content consumers /u1D466.alt ∈ 𝐶 we have that
𝜃 ′ (0) 𝐵 (𝑧|/u1D466.alt) < 𝜃 ′ (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧′ ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇∗ inﬂ (𝑧′)) 𝐵 (𝑧|/u1D466.alt′), 𝑧 ∈ 𝐶\{/u1D466.alt}
g’) We have that /summationdisplay.1
𝑧 ∈𝐶
𝜇∗ inﬂ (𝑧) = 𝑀inﬂ.
h’) If for content producer 𝑧 ∈ 𝐶 we have that 𝜇∗ inﬂ (𝑧) > 0, then we have for 𝑧′ ∈ 𝐶\{𝑧} that
𝜃 ′ (𝜇∗ inﬂ (𝑧)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜇∗ inﬂ (𝑧′)) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt).
Note that the Properties a)-h) are identical to the Properti es a’)-h’). It then follows that for a given rate budget 𝑀,
there exist constants 𝑁0 and 𝜇0 such that for 𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ, then the following is true. The allocation
ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium of the game with perfect information as given by Deﬁnition 7.1, if
and only if ΩNE (𝑀, 𝑀inﬂ) is a Nash equilibrium for the proxy game.
H ANALYSIS OF NASH EQUILIBRIUM Ω∗ infl (𝑀, 𝑀infl) FOR IMPERFECT INFORMATION
In this section, we derive additional properties of a Nash eq uilibrium of the game with imperfect information as given
by Deﬁnition 9.1 that we use to in Appendix H.3 to prove Propos ition 8.
Most of the analysis follows the same argument as given in App endix G for the analysis of a Nash equilibrium
ΩNE (𝑀, 𝑀inﬂ) of the game with perfect information. We repeat here only the key results and arguments; for all other
results and arguments, we refer to the analysis in Appendix G .
H.1 Optimality Condition for Nash Equilibrium Ωinfl (𝑀, 𝑀infl)
Our ﬁrst result provides necessary and suﬃcient conditions for a Nash equilibrium of the game with perfect informa-
tion.
Manuscript submitted to ACM

60 Junwei Su and Peter Marbach
L/e.sc/m.sc/m.sc/a.sc 26. An Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium as given by Deﬁnition 9.1, if an only if t he following
conditions hold true,
a) For all content producers 𝑧 ∈ 𝐶, the content allocation 𝑥∗ (𝑧) is a solution for the maximization problem
𝑥∗ (𝑧) = argmax
𝑥 (𝑧) ∈ T
𝜃
(
𝜇inﬂ (𝑧|Λ∗, 𝑋∗ {𝑧,𝑥 (𝑧) }) ) .
b) For all content consumers /u1D466.alt ∈ 𝐶 we have that
𝜆∗ (/u1D466.alt) + 𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) + /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜇∗(𝑧|/u1D466.alt) = 𝑀
c) If for content consumer /u1D466.alt ∈ 𝐶 we have that 𝜆∗ (/u1D466.alt) > 0, then we have
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0 ≥ 𝜃 ′ (𝜇∗(𝑧|/u1D466.alt)) 𝑟𝑝𝐵 (𝑧|/u1D466.alt), 𝑧 ∈ 𝐶\{/u1D466.alt}
and
𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0 ≥ 𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ(𝑧) ) 𝐵 (𝑧|/u1D466.alt).
d) If for content consumer /u1D466.alt ∈ 𝐶 we have that 𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0, then we have
𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧′ ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ(𝑧′) ) 𝐵 (𝑧′|/u1D466.alt) ≥ 𝜃 ′ (𝜇∗ (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt), 𝑧 ∈ 𝐶\{/u1D466.alt}
and
𝜃 ′ (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝑟𝑝 /summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ (𝑧) ) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0.
e) If for content consumer /u1D466.alt ∈ 𝐶 and content producer 𝑧 ∈ 𝐶\{/u1D466.alt} we have that 𝜇∗(𝑧|/u1D466.alt) > 0, then we have
𝜃 ′ (𝜇∗(𝑧|/u1D466.alt)) 𝑟𝑝𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜆∗ (/u1D466.alt)) 𝑟0𝐵0,
𝜃 ′ (𝜇∗ (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) /summationdisplay.1
𝑧′ ∈𝐶\{ /u1D466.alt }
𝜃
(
𝜇∗ inﬂ (𝑧′) ) 𝐵 (𝑧′|/u1D466.alt),
and
𝜃 ′ (𝜇∗(𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ (𝜇∗(𝑧′|/u1D466.alt)) 𝐵 (𝑧′|/u1D466.alt), 𝑧 ∈ 𝐶\{/u1D466.alt, 𝑧′}.
f) We have that /summationdisplay.1
𝑧 ∈𝐶
𝜇∗ inﬂ (𝑧) = 𝑀inﬂ.
g) If for content producer 𝑧 ∈ 𝐶 we have that 𝜇∗ inﬂ (𝑧) > 0, then we have for 𝑧′ ∈ 𝐶\{𝑧} that
𝜃 ′
(
𝜇∗ inﬂ (𝑧) ) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃 (𝜇∗(/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt) ≥ 𝜃 ′ ( 𝜇∗ inﬂ (𝑧′) ) /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧′ }
𝜃 (𝜇∗ (/u1D466.altinﬂ|/u1D466.alt)) 𝐵 (𝑧′|/u1D466.alt).
Lemma 26 can then be proved using the same argument as given fo r Lemma 10 which establishes the necessary and
suﬃcient conditions for a Nash equilibrium of the proxy game , and we omit here a detailed derivation.
H.2 Properties of Nash Equilibrium Ωinfl (𝑀, 𝑀infl)
Next, we derive the key properties of a Nash equilibrium Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) for the game with imperfect
information as given by Deﬁnition 9.1.
Manuscript submitted to ACM

The Role of Social Support and Inﬂuencers in Social Media Com munities 61
The ﬁrst result provides conditions such that for a Nash equi librium ΩNE (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) of the game with
perfect information we have /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗(/u1D466.altinﬂ|/u1D466.alt) > 0.
L/e.sc/m.sc/m.sc/a.sc 27. There exist constants 𝑁0 and 𝑘inﬂ such that if 𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ, then the following is true. If
Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ∗, 𝑋∗) is a equilibrium of the game with imperfect information as gi ven by Deﬁnition 9.1, then we
have that /summationdisplay.1
/u1D466.alt ∈𝐶
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0.
Lemma 27 can be proved using the same argument as given in the p roof for Lemma 27, and we omit here a detailed
derivation.
The next result states that if the community size 𝑁 and the rate budget 𝑀inﬂ of the inﬂuencer are large enough, then
under a Nash equilibrium of the game with imperfect informat ion we have that each consumer follows the inﬂuencer
with a positive rate.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 13. For a given rate budget 𝑀, there exist constants 𝜖0 > 0, 𝑁0 and 𝜇0 such that for 𝑁 > 𝑁0 and
𝑀inﬂ > 𝑁 𝑘inﬂ, the following is true. If Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) is a Nash equilibrium for the game with imperfect
information as given by Deﬁnition 9.1, then we have that
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) ≥ 𝜖0, /u1D466.alt ∈ 𝐶.
Proposition 13 can be proved using the same argument as given in the proof for Proposition 9, and we omit here a
detailed derivation.
In addition we have that if the community size 𝑁 and the rate budget 𝑀inﬂ of the inﬂuencer are large enough, then
under a Nash equilibrium of the game with perfect informatio n we that the inﬂuencer allocates a large rate to each
producer 𝑧 ∈ 𝐶.
P/r.sc/o.sc/p.sc/o.sc/s.sc/i.sc/t.sc/i.sc/o.sc/n.sc 14. Let 𝑀 be a given rate budget, and let 𝜇0 be a given rate. Then there exist constants 𝑁0 and 𝑘inﬂ such
that if 𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ, the following is true. If Ωinﬂ (𝑀, 𝑀inﬂ) (𝑀inﬂ) = (𝜇 (𝑀inﬂ ) inﬂ , Λ∗, 𝑋∗) is a Nash equilibrium of
the game with imperfect information as given by Deﬁnition 9. 1, then we have that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶.
Proposition 14 can be proved using the same argument as given in the proof for Proposition 10, and we omit here
a detailed derivation.
The next result states that if the community size 𝑁 and the rate budget 𝑀inﬂ of the inﬂuencer are large, then the all
consumers /u1D466.alt ∈ 𝐶 will get their content through the inﬂuencer.
L/e.sc/m.sc/m.sc/a.sc 28. For a given rate budget 𝑀, there exist constants 𝑁0 and 𝜇0 such that for 𝑁 > 𝑁0 the following is true. If
Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇inﬂ, Λ, 𝑋) is a Nash equilibrium as given by Deﬁnition 9.1 such that
𝜇∗ inﬂ (𝑧) ≥ 𝜇0, 𝑧 ∈ 𝐶,
then we have for all content consumers /u1D466.alt ∈ 𝐶 that
𝜇∗ (𝑧|/u1D466.alt) = 0, 𝑧 ∈ 𝐶\{/u1D466.alt}.
Manuscript submitted to ACM

62 Junwei Su and Peter Marbach
Lemma 28 can be proved using the same argument as given in the p roof for Lemma 25, and we omit here a detailed
derivation.
H.3 Proof of Proposition 8
In this appendix we provide a proof for Proposition 8. Recall that Proposition 8 states that for a given rate budget 𝑀,
there exist constants 𝑁0 and 𝜇0 such that for 𝑁 > 𝑁0 and 𝑀inﬂ > 𝑁 𝑘inﬂ, then the following is true. The allocation
Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) is a Nash equilibrium of the game with imperfect information as given by Deﬁnition 9.1,
if and only if Ωinﬂ (𝑀, 𝑀inﬂ) is a Nash equilibrium for the proxy game.
We prove Proposition 8 as follows. Using Proposition 4, for aNash equilibrium Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋 ∗) as given
by Deﬁnition 9.1 with
𝜇∗(𝑧|/u1D466.alt) = 0, /u1D466.alt ∈ 𝐶, 𝑧 ∈ 𝐶\{/u1D466.alt},
as well as
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0, /u1D466.alt ∈ 𝐶,
and
𝜇∗ inﬂ (𝑧) > 0, 𝑧 ∈ 𝐶,
we have for all content producers 𝑧 ∈ 𝐶 that
argmax
𝑥 (𝑧) ∈ T
𝜃
(
𝜇inﬂ (𝑧|Λ∗, 𝑋∗ {𝑧,𝑥 (𝑧) }) ) = argmax 𝑥 (𝑧) ∈ T 𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) = argmax 𝑥 (𝑧) ∈ T 𝑈𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ),
where
𝑈 inﬂ 𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) = 𝑟𝑝 /summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
and
𝑈𝑝,𝑧 (𝑥 (𝑧)| 𝜇inﬂ, Λ) = 𝑟𝑝
/summationdisplay.1
/u1D466.alt ∈𝐶\{ 𝑧 }
𝜃inﬂ (𝑧|/u1D466.alt) 𝐵 (𝑧|/u1D466.alt)
+ 𝑟𝑝
/summationdisplay.1
𝑧 ∈𝐶\{ /u1D466.alt }
𝜃 (𝜇 (𝑧|/u1D466.alt)) 𝐵 (𝑧|/u1D466.alt).
Therefore, in the case where for a Nash equilibrium Ωinﬂ (𝑀, 𝑀inﬂ) = (𝜇∗ inﬂ, Λ∗, 𝑋∗) as given by Deﬁnition 9.1 with
𝜇∗(𝑧|/u1D466.alt) = 0, /u1D466.alt ∈ 𝐶, 𝑧 ∈ 𝐶\{/u1D466.alt},
as well as
𝜇∗ (/u1D466.altinﬂ|/u1D466.alt) > 0,
and
𝜇∗ inﬂ (𝑧) > 0, 𝑧 ∈ 𝐶,
the necessary and suﬃcient conditions for a Nash equilibriu m given in Lemma 10 are the same as the ones given the
proof of Proposition 7. The result of Proposition 8 can then b e proven using the same argument as given in the proof
for Proposition 7, and we omit here a detailed derivation.
Manuscript submitted to ACM
