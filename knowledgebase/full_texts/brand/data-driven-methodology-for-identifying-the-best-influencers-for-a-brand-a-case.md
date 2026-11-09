---
title: 'Data-driven methodology for identifying the best influencers for a brand: A case study on Anemonia'
url: https://doi.org/10.5267/j.msl.2024.4.001
category: brand
subcategory: case-study
date: 2024-04
venue: Management Science Letters
authors:
- Emanuele Fiocco
source: openalex-oa
pdf_url: https://doi.org/10.5267/j.msl.2024.4.001
pages: 8
chars: 24847
fetched_at: '2026-11-08T17:54:30+00:00'
kb_version: 1
---

# Data-driven methodology for identifying the best influencers for a brand: A case study on Anemonia

* Corresponding author.

E-mail address: emanuele.fiocco@icloud.com (E. Fiocco)

© 2025 by the authors; licensee Growing Science, Canada
doi: 10.5267/j.msl.2024.4.001

Management Science Letters 15 (2025) 23–30

Contents lists available at GrowingScience

Management Science Letters

homepage: www.GrowingScience.com/msl

Data-driven methodology for identifying the best influencers for a brand: a case study on Anemonia

Emanuele Fioccoa*

aDepartment of Industrial Engineering, University of Rome Tor Vergata, Italy
C H R O N I C L E                                 A B S T R A C T
Article history:
Received: January 23, 2024
Received in revised format:
February 26 2024
Accepted: April 5, 2024
Available online:
April 5 2024
 This study aims to develop a new data-driven methodology for identifying suitable influencers for
a brand using data from social media. The increasing presence of such figures in these communi-
cation channels makes it challenging to select consistent and influential influencers for a specific
audience. This paper introduces an innovative approach to defining these figures based on the anal-
ysis of relationships within the brand’s network. Specifically, this methodology will be applied to
the case study of a brand named “Anemonia”. The approach relies on the sequential application of
various steps, including the use of tools such as  Social Network Analysis (SNA) centrality, Senti-
ment Analysis (SA), and Analytical Hierarchical Process (AHP). Through the application of this
methodology, the brand has been able to identify influencers consistent with its aesthetics and vi-
sion.

© 2025 by the authors; licensee Growing Science, Canada
Keywords:
AHP
Marketing
Influencer
Social Media
Brand Management

1. Introduction

Accurate definition of influencers for marketing campaigns is crucial to properly support the growth of visibility and pursue
sustainable development of digital presence. These new social actors play a key role in shaping public perception and increas-
ing brand engagement.

“Influencers represent a new category of opinion leaders, with a role positioned between celebrities and friendships, emerging
with the growing opportunities provided by social media” (Belanche et al., 2021). Often in marketing, star strategy campaigns
are carried out, where a specific brand is paired with a celebrity with the aim of creating a direct association in the minds o f
buyers. Although the general purpose remains the same, influencer marketing involves a new type of business strategy as
influencers do not coincide with celebrities.

On a conceptual basis, celebrities and influencers differ inherently, as celebrities are known for activities unrelated to soci al
media, such as sports, music, cinema, etc., while influencers have a public figure that emerges and develops on social media
(Dhanesh & Duthler, 2019). Influencers are focused on an audience with common interests, and users who are part of this
audience become like virtual friends. Due to their positioning between a celebrity and a friend, influencers tend to inspire
more trust and appear more authentic than conventional celebrities (Belanche et al., 2021).

These considerations highlight a type of communication and interaction between influencers and their followers that is sub-
stantially different from a generic star strategy campaign. Indeed, the relationship between influencers and followers becomes
almost intimate, characterized by interactions that, although digital, are frequent over time. This implies that the specific
audience targeted by a brand must identify in the influencer a relatable figure capable of inspiring trust.

24
Therefore, a data-driven strategy for identifying influencers can be of fundamental importance, offering to the brand’s stake-
holders the opportunity to make choices based on tangible data. Within this paper, we will consider a small brand active in
the luxury vintage resale sector, named “Anemonia”. Some studies in the literature have explored methods for identifying
suitable influencers for marketing campaigns, employing SNA (Tan & Lim, 2021, 2022), the AHP(Lee et al., 2019), and SA
(Agarwal & Damle, 2020; Gräve & Greff, 2018). However, this paper aims to advance the discussion to a methodological
level by defining the drivers for accurately evaluating influencers and presenting a concrete application through a case study.
2. Material And Methods

This section is dedicated to illustrating the various steps that outline the data-driven methodology, the focus of the paper.

Fig. 1. Methodological framework

1. STEP 1: Extraction and manipulation of the brand’s reference network: data publicly accessible regarding the social
network in which the brand is located were extracted using two main online tools: apify.com and phantombuster.com.
2. STEP 2: Application of centrality indexes: the three centrality indices were applied to the entirety of actors in the network.
3. STEP 3: Sentiment Analysis of comments: application of the VADER model and treatment of emojis.
4. STEP 4: Analytical Hierarchical Process (AHP): other criteria for evaluating alternatives were defined (such as the
engagement rate and the number of followers), and through AHP, the final decision was reached.

Next, we will explore the steps and tools used in more detail.

2.1. Extraction and manipulation of the network

The relationships that occur among social media actors can be analyzed using mathematical tools specific to network analysis.

A frequently employed model for modeling and examining a social network is the mathematical approach typical of graph
theory, which enables the formal description of a network and its predominant characteristics.

2.1.1. Graph definition

A graph can be directed or undirected depending on whether the relationships between elements are directed or not.

A graph 𝐺 = (𝑉, 𝐸) is defined by a finite set 𝑉(𝐺) = {𝑣1, … , 𝑣𝑛} of elements called “nodes” and by a set 𝐸(𝐺) = {𝑒1, … ,
𝑒𝑚} ⊆ 𝑉 × 𝑉 of node pairs called “edges”.  Here is an example of an undirected graph:

Fig. 2. Example of undirected graph Fig. 3. Example of directed graph

In directed graphs, the node pairs that form the edges are ordered. For example, the general edge 𝑒 = (𝑢, 𝑣) is distinct from
the edge 𝑒′ = (𝑣, 𝑢), while in undirected graphs, these are equivalent, (𝑢, 𝑣) ≡ (𝑣, 𝑢). In the directed graph shown, it is indicated
that 𝑉(𝐺) = {𝑣1, 𝑣2, 𝑣3, 𝑣4, 𝑣5}, and 𝐸(𝐺) = {𝑒1, 𝑒2, 𝑒3, 𝑒4, 𝑒5, 𝑒6} = {(𝑣1, 𝑣2), (𝑣2, 𝑣1), (𝑣2, 𝑣3), (𝑣3, 𝑣5), (𝑣1, 𝑣5), (𝑣4,
𝑣3)}.

2.1.2. Node’s degree

To understand how a node is connected to its neighbors, we can leverage the notion of degree. The degree of a node represents
the number of edges connected to that specific node, which is equal to the number of adjacent nodes. In a directed graph, one
must distinguish between:

E. Fiocco / Management Science Letters 15 (2025) 25
- In-degree: represents the number of incoming edges to the node.
- Out-degree: represents the number of outgoing edges from the node.

In an undirected graph, the degree is equal to the number of edges connected to that node, so there is no need to distinguish
between in-degree and out-degree since there are no directed edges.

2.1.3. Definition of path, length, and geodesic

A path belonging to the graph 𝐺 = (𝑉, 𝐸) is a sequence of distinct nodes such that each node is adjacent to the previous and/or
succeeding node. The length of the path is equal to the number of edges required to connect two nodes. The geodesic, on the
other hand, is the minimum path that connects two arbitrary points.

2.1.4 Application of STEP 1

As a first step, the one hundred most active followers on Anemonia’s profile were identified. Specifically, those who gave the
most likes and made the most comments on the twenty-four posts published by the brand in August 2023 were considered.
These profiles will define the nodes from which we will start th e definition of the social network, the subject of our first
analysis.

The selection of the one hundred most active users was based on two specific objectives:

1. Identify a social network of interest for the brand: by considering the followers who appreciate the page the most as
the original nodes of our network, a social network with nodes having direct connections to Anemonia’s target audi-
ence can be identified.
2. Improve the effectiveness of the marketing strategy: the most active followers, representing an audience highly inter-
ested in the brand’s content, can be more involved in sharing content, promoting word-of-mouth effects.

Within the network, only public profiles were considered, and the personal profiles of brand stakeholders were not included
among the most active users as they do not play a consumer role.

At the end of this initial analysis, the first one hundred nodes of our graph were identified. Subsequently, the connections,
particularly the “following” relationships, that these one hundred profiles have with other users were extracted, defining new
nodes and edges that connect them.

After some analyses on the network, it was revealed to be sparse with many nodes having a degree equal to one, i.e., “dan-
gling” nodes in the network.

To reduce the complexity of the analysis, simplifications were decided for the network:

- Eliminate dangling nodes.
- Perform a random sampling on this set, extracting 5% of the nodes.

Fig. 3. Network after sampling Fig. 4. Network after the new edges

Following the manipulation, additional relational data about the actors in the network were extracted. Specifically, all types
of following/follow relationships between the considered users were added. These data translate into edges of the directed
graph.

26
2.2. Centrality index application
As stated by Carrington et al. (2005) in their book “Models and Methods in Social Network Analysis”, centrality is one of the
most important and widely used conceptual tools for analyzing social networks.

As declared by Freeman in the article “Centrality in Social Networks Conceptual Clarification” (2002), centrality seeks the
node in the most central position within the network: like the point at the center of a star or the node representing the axis at
the center of a wheel.

This central node possesses a structurally unique position that translates into three key characteristics:
1. It is the node with the maximum degree.
2. It is the node most frequently present in geodesics.
3. It is the node closest to the remaining nodes in the graph.

2.2.1. Degree Centrality

The simplest and most intuitive way defines the centrality as function of node’s degree.

𝐶஽ሺ𝑝௞ሻ = ෍ 𝑎(𝑝௜
௡
௜ୀଵ
, 𝑝௞)

(1)
where:
- 𝐶஽(𝑝௞) is the degree-based centrality index of node 𝑝௞.
- 𝑎(𝑝௜, 𝑝௞) is 1 if 𝑝௜ and 𝑝௞ are adjacent (connected by an edge) and 0 otherwise.
- 𝑛 is the cardinality of the set of nodes V.

2.2.2. Betweenness Centrality

The second indicator for measuring centrality is defined based on the frequency with which a node falls within a geodesic
path connecting a pair of nodes in the graph.

𝐶஻(𝑝௞) = ෍ 𝑏௜௝(
௡
௜ழ௝
𝑝௞)

(2)
where:
- 𝐶஻(𝑝௞) is the betweenness centrality index based on the betweenness property of node 𝑝௞.
- 𝑛 is the cardinality of the set of nodes V.
- 𝑏௜௝ =
௚೔ೕ(௣ೖ)
௚೔ೕ
, which is the ratio of geodesics linking node 𝑝௜ and the node 𝑝௝ that contain node 𝑝௞ to the total geo-
desics linking node 𝑝௜ and 𝑝௝.

2.2.3. Closeness Centrality

The last type of indicators that Freeman explored in his work “Centrality in Social Networks Conceptual Clarification” (2002)
is based on the concept of closeness between nodes. This index is based on the average distance of a node 𝑝௞ to all other nodes
in the network.

𝐶஼(𝑝௞)ିଵ = ෍ 𝑑(𝑝௜, 𝑝௞)
௡
௜ୀଵ

(3)
where:
- 𝐶஼(𝑝௞) is the closeness-based centrality index based on the closeness property of node 𝑝௞. The index increases in-
versely with the proximity between the node 𝑝௞and the other nodes. This is an inverse measure of the centrality of
the node.
- 𝑛 is the cardinality of the set of nodes V;

E. Fiocco / Management Science Letters 15 (2025) 27
- 𝑑(𝑝௜, 𝑝௞) is equal to the number of edges present in the minimum path, i.e., the geodesic, linking node 𝑝௜with 𝑝௞. In
a graph with isolated nodes, i.e., disconnected, the value of the distance between nodes where no edges exist is
infinite.

2.2.4. Application of STEP 2

On the graph shown in Fig. 5, various metrics defining node centrality were then calculated. Below is a portion of the dataset
containing data for the three mentioned metrics.

Fig. 5. Portion of dataset with centrality indexes calculated

2.3. Sentiment Analysis

Sentiment analysis (SA), also known as opinion mining, aims to understand user attitudes and opinions by investigating,
analyzing, and extracting texts related to users’ views, ideas, preferences, and sentiments (Medhat et al., 2014).

Sentiment analysis algorithms can be grouped into two main categories: “machine learning-based” approaches and “lexicon-
based” approaches. In this paper, a lexicon-based approach will be used for sentiment analysis, leveraging the VADER model
(Valence Aware Dictionary and sEntiment Reasoner). This approach was defined by Hutto & Gilbert in 2014 and performs
sentiment scoring, which involves assigning a score representing the sentiment of the text.

2.3.1. Sentiment Analysis

The data used as input for sentiment analysis underwent various extractions and treatments to optimize them for algorithmic
application. Firstly, a list of unique usernames, i.e., the to p ten usernames for each centrality indicator (in-degree centrali ty,
betweenness centrality, closeness centrality), was defined. This resulted in a list of 24 total users, as some of them had high
values for multiple centrality indices and thus appeared in more than one top 10. Subsequently, for each of these users, the
URLs of their latest 12 posts on their social profiles were extracted. Choosing the latest 12 posts aimed to capture sentiment
as current as possible. It’s important to note that not all 24 profiles had 12 posts, some had fewer. For this reason, the obtained
average sentiment scores will be normalized with respect to the number of extracted posts, ensuring that the measure is com-
parable across different profiles.

Next, comments below each post were extracted. The number of comments is not constant, and this will be a factor to consider
in the normalization. These comments were then reorganized by merging data, using the post URL as the primary key. This
merging process associated each comment with the respective user it was addressed to. The final output was a dataset with
two columns: the first column containing the reference username and the second column containing the comment related to
the user’s post.

28

Fig. 6. Some usernames and comments Fig. 7. Some comments with its sentiment score

It is important to highlight that the left column in the above figure indicates the user to whom the comment in the right col-
umn was addressed.

2.3.2. Application of VADER model

Firstly, the VADER model was applied to the comments collected in the data extraction phase. The application of this model
was carried out using the R library called "vader" and the following code, also in the R language. Below is a portion of the
dataset where each comment has a sentiment value.

It can be observed that in various comments, such as the one at row 4 or row 5, heart emojis are present, but they do not have
a corresponding sentiment value. However, within the total extracted comments, not only heart emojis are present; there are
various emojis that can impact the identified sentiment score. For this reason, the “lexicons” library, a programming language
library in R, was used in conjunction. This library accurately identifies emojis and associates them with sentiment values.

The reference scales for the VADER model and the model built based on the “lexicons” library are different. Therefore, it
was necessary to scale the values of this latter library to a range of [-4,4]. An emoji evaluation algorithm was applied, and a
column containing the sentiment score associated with the emojis present in the comment was added to the dataset, as shown
in Fig. 8.

Fig. 8. Comments with text and emojis sentiment scores Fig. 9. Portion of dataset with normalized sentiment scores

It is important to note that a logarithmic factor was introduced to smooth the growth in the sentiment score when an emoji
was repeated multiple times within the same comment. This operation was performed under the idea that a comment contain-
ing, for example, the heart emoji four times does not have the significance of four comments, each with a single heart emoji.

After it was summed the various associated sentiment scores  for each user. Subsequently, the sentiment score was propor-
tioned with the number of extracted comments and the number of extracted posts since, as mentioned earlier, it is not a constant
value. In Fig.9. there is a portion of the dataset with the profile, the number of extracted posts, and the proportioned sentiment
score value.

2.4. AHP

The Analytical Hierarchy Process (AHP) is a multicriteria decision support technique developed by mathematician Saaty
(1990). The methodology allows for comparing multiple alternatives in relation to a plurality of criteria, which can be either
qualitative or quantitative, and deriving an overall evaluation for each alternative. For the application of AHP, a survey among
decision-makers is required to define relative weights for the evaluation criteria of the alternatives. To do this, questions must
be posed to the group of decision-makers to define the pairwise comparison matrix A, asking how much more important the

E. Fiocco / Management Science Letters 15 (2025) 29
criterion in the i-th row is compared to the criterion in the j-th column. The decision-maker can respond with an integer in the
range [1, 9], representing the relative importance between the criteria. Before applying the aforementioned multicriteria meth-
odology, other decision criteria to evaluate influencers were collected, such as the number of followers, the number of likes
and the number of comments. In this case, data for the number of likes and the number of comments were extracted from the
last 12 posts for each user. As mentioned previously, not all users have this quantity of posts, so the values will be proportioned
to be comparable both in terms of the number of posts actually extracted and the number of followers. By making a linear
combination of the two proportioned values (average number of likes per post and per follower, average number of comments
per post and per follower), an average engagement rate value for each user can be obtained.  The average engagement rate per
post per follower is defined by the following formula:

𝐸𝑅 = 1 × 𝐿 + 5 × 𝐶

where:
- “ER” is the average engagement rate per post per follower.
- “L” is the average number of likes per post and per follower.
- “C” is the average number of comments per post and per follower.

The correlation between variables in the dataset presented in Fig, 10 is being examined to avoid linear dependency between
variables and, thus, redundant information. From the evaluation, the variables “average number of likes per post per follower”
and “average number of comments per post per follower” are excluded, and only the variable “average engagement rate per
post per follower” will be considered, as it is a linear combination of the two.

Fig. 10. Correlations between criteria Fig. 11. Pairwise comparison matrix

It can be observed that there are no significant correlations among the variables, and thus they can be considered in their
entirety. In the subsequent decision-making process, only one centrality measure will be taken into account, namely in-degree
centrality. This choice has been made to streamline the decision-making process conducted in collaboration with the brand
stakeholders.

At the end of the survey for the definition of the pairwise comparison matrix, the following output was obtained:

where:
- “SS” is the acronym for Average Sentiment Score per post per comment.
- “NF” is the acronym for Number of Followers.
- “ER” is the acronym for Average Engagement Rate per post per follower.
- “IDC” is the acronym for In-Degree Centrality.

3. Results

For the application of the algorithm, an online tool (www.bpmsg.com/ahp) was used, resulting in the following weight vector:
w = [0.151, 0.265, 0.508, 0.075]. The result was achieved after fi ve iterations of the algorithm, considering the following
tolerance thresholds: Consistent Ratio (CR) = 0.1 and 𝜀 = 0.1. The dataset below shows the usernames ordered based on the
final value obtained in the alternative evaluation phase of the AHP (See Fig. 12). Therefore, it can be concluded that in the
top three users who could best perform the role of influencers for Anemonia, in order, are @gabbriette, @alexconsani, and
@gremlita, with final evaluation scores of approximately 0.093, 0.087, and 0.074, respectively.

30

Fig. 12. Final dataset with AHP scores

4. Conclusion

The accurate definition of influencers for marketing campaigns of one's brand is crucial to properly support the growth of
visibility and pursue sustainable development of the digital presence. These new social actors play a key role in shaping public
perception and increasing brand engagement. For these reasons, a data-driven methodology for defining and evaluating influ-
encers can be essential, allowing brand stakeholders to make informed decisions based on concrete data, thus optimizing
campaign effectiveness and maximizing return on investment. The uniqueness of the analysis presented in this paper lies in
its ability to consider both relational data and textual data representing user opinions. As a result of this case study, we ha ve
identified three influencers who have been recognized and positively evaluated by the brand’s stakeholders, namely: @gab-
briette, @alexconsani, and @gremlita. This positive outcome highlights the potential to extend this methodology to new
brands and in new contexts with the goal of streamlining the decision-making process in identifying suitable profiles for
influencer marketing campaigns.

References

Agarwal, S., & Damle, M. (2020). Sentiment analysis to evaluate influencer marketing: Exploring to identify the parameters
of influence. PalArch's Journal of Archaeology of Egypt/Egyptology, 17(6), 4784-4800.
Belanche, D., Casaló, L. V., Flavián, M., & Ibáñez-Sánchez, S. (2021). Understanding influencer marketing: The role of
congruence between influencers, products and consumers. Journal of Business Research, 132, 186-195.
Carrington, P. J., Scott, J., & Wasserman, S. (Eds.). (2005). Models and methods in social network analysis (Vol. 28). Cam-
bridge university press.
Dhanesh, G. S., & Duthler, G. (2019). Relationship management  through social media influencers: Effects of followers’
awareness of paid endorsement. Public relations review, 45(3), 101765.
Freeman, L. C. (2002). Centrality in social networks: Conceptual clarification. Social network: critical concepts in sociology.
Londres: Routledge, 1, 238-263
Gräve, J. F., & Greff, A. (2018, July). Good KPI, good influencer? Evaluating success metrics for social media influencers.
In Proceedings of the 9th International Conference on Social Media and Society (pp. 291-295).
Hutto, C., & Gilbert, E. (2014, May). Vader: A parsimonious rule-based model for sentiment analysis of social media text.
In Proceedings of the international AAAI conference on web and social media (Vol. 8, No. 1, pp. 216-225).
Lee, D., Lee, S., & Park, S. (2019). A study on influencer characteristic factors by using AHP. Journal of the Society of Korea
Industrial and Systems Engineering, 42(3), 184-1
Medhat, W., Hassan, A., & Korashy, H. (2014). Sentiment analysis algorithms and applications: A survey. Ain Shams engi-
neering journal, 5(4), 1093-1113.
Saaty, T. L. (1990). Multicriteria decision making: The analytic hierarchy process: planning, priority setting, resource alloca-
tion, 2, 1-20.
Tan, W. B., & Lim, T. M. (2021, October). A study on the centrality measures to determine social media influencers in twitter.
In International Conference on Digital Transformation and Applications (ICDXA) (Vol. 25, p. 26).
Tan, W. B., & Lim, T. M. (2022). A study on the centrality measures to determine social media influencers of food-beverage
products in Twitter.

Sitography

www.anemonia.it
www.bpmsg.com/ahp
www.depop.com
www.apify.com
www.phantombuster.com

© 2025 by the authors; licensee Growing Science, Canada. This is an open access article distrib-
uted under the terms and conditions of the Creative Commons Attribution (CC-BY) license
(http://creativecommons.org/licenses/by/4.0/).
