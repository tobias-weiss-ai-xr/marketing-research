---
title: Towards Global, Socio-Economic, and Culturally Aware Recommender Systems
url: https://arxiv.org/abs/2312.05805
category: digital-marketing
subcategory: empirical
date: 2023-12
venue: ''
authors:
- Kelley Ann Yohe
source: arxiv
pdf_url: https://arxiv.org/pdf/2312.05805
pages: 39
chars: 119076
fetched_at: '2026-11-08T13:18:50+00:00'
kb_version: 1
---

# Towards Global, Socio-Economic, and Culturally Aware Recommender Systems

Towards Global, Socio-Economic, and Culturally Aware Recommender
Systems
Kelley Ann Yohe*a
aMacquarie University, Sydney, Australia
kelley.yohe@students.mq.edu.au
ABSTRACT
Recommender systems have gained increasing attention to personalise consumer preferences. While these systems
have primarily focused on applications such as advertisement recommendations (e.g., Google), personalized sug-
gestions (e.g., Netflix and Spotify), and retail selection (e.g., Amazon), there is potential for these systems to ben-
efit from a more global, socio-economic, and culturally aware approach, particularly as companies seek to expand
into diverse markets. This paper aims to investigate the potential of a recommender system that considers cul-
tural identity and socio-economic factors. We review the most recent developments in recommender systems and
explore the impact of cultural identity and socio-economic factors on consumer preferences. We then propose an
ontology and approach for incorporating these factors into recommender systems. To illustrate the potential of our
approach, we present a scenario in consumer subscription plan selection within the entertainment industry. We ar-
gue that existing recommender systems have limited ability to precisely understand user preferences due to a lack
of awareness of socio-economic factors and cultural identity. They also fail to update recommendations in response
to changing socio-economic conditions. We explore various machine learning models and develop a final artificial
neural network model (ANN) that addresses this gap. We evaluate the effectiveness of socio-economic and cul-
turally aware recommender systems across four dimensions: Precision, Accuracy, F1, and Recall. We find that a
highly tuned ANN model incorporating domain-specific data, select cultural indices and relevant socio-economic
factors predicts user preference in subscriptions with an accuracy of 95%, a precision of 94%, a F1 Score of 92%,
and a Recall of 90%. Keywords: Recommender systems, personalization, cultural identity, socio-economic factors,
user preferences.
KEYWORDS
Recommender systems, personalization, cultural identity, socio-economic factors, user preferences.
1 INTRODUCTION
Recommender systems have become an integral part of many consumer-related applications in recent years, pro-
viding personalised options to customers28, 81. These systems are primarily used by companies such as Google,
Netflix, Amazon, and Spotify to recommend advertisements, media, and products to consumers41, 80. However,
these systems have been limited in their ability to incorporate socio-economic and cultural factors that can influ-
ence consumer preferences. As companies expand into diverse markets, the need for more culturally aware and
socio-economically sensitive recommender systems is becoming increasingly important. In this context, a recom-
mender system that considers cultural identity and socio-economic factors have the potential to improve customer
satisfaction and increase sales.
This paper aims to investigate the potential of a recommender system that considers cultural identity and socio-
economic factors13. Accordingly, in this paper, we will discuss the most recent developments in recommender sys-
tems and explore the impact of cultural identity and socio-economic factors on consumer preferences. We will pro-
pose an ontology and approach for incorporating these factors into recommender systems. Finally, we will present
arXiv:2312.05805v1  [cs.IR]  10 Dec 2023

a scenario involving consumer subscription and plan selection in the media entertainment industry to illustrate the
potential of our approach.
1.1 Recommendations as a Competitive Advantage
As technological advancements progress, an increasing amount of data is being generated through human activi-
ties, devices, and system processes. The introduction of openly available data has led to an overwhelming number
of choices available to users, surpassing their capacity for understanding. To remain competitive and establish a
strong relationship with their customers, businesses are required to assist users in sorting through this vast amount
of information in order to uncover meaningful preferences40. The ability to accurately identify preferences, provide
recommendations, and profit from those recommendations represent a rapidly expanding and highly competitive
business opportunity. Indeed, it can be a decisive factor in the success of a business strategy that leverages avail-
able customer knowledge to generate revenue, sustain profitability, and achieve a competitive edge.
Despite the potential benefits that recommender systems can offer, significant challenges are associated with their
design and implementation. One major issue is the lack of global, socio-economic, and cultural awareness in cur-
rent recommender systems, which can result in inaccurate recommendations and lost revenue opportunities. For
example, many current recommender systems rely heavily on users’ personal data12, such as their search history,
purchase behavior, and social media activity. However, this approach may not be effective in diverse markets where
cultural and socio-economic factors significantly influence consumer behavior. In such cases, it may be necessary to
develop recommender systems capable of considering these factors and adapting to local contexts.
In addition to the challenge of cultural and socio-economic awareness, there is also a need for transparency and
ethical considerations in recommender systems. As recommender systems become increasingly integrated into our
daily lives, there is a risk that they may perpetuate existing biases and inequalities, particularly in the case of sen-
sitive issues such as healthcare, employment, and finance65. Despite these challenges, significant opportunities are
also associated with developing global, socio-economic, and culturally aware recommender systems. By incorpo-
rating a wider range of factors into the design of recommender systems, it may be possible to provide more ac-
curate and relevant recommendations to users, leading to increased customer satisfaction and loyalty. Moreover,
businesses that can successfully navigate the challenges of global, socio-economic, and cultural awareness in their
recommender systems may tap into new and previously under-served markets, leading to increased revenue and
profitability.
1.2 The Rationale for Intelligent Recommendations
The advent of technology has resulted in an unprecedented increase in information generation, which has facili-
tated the development of more advanced systems with richer content. However, this expansion in content and sys-
tem capabilities has also led to the potential for users to become overwhelmed by the sheer volume of available
choices 72. This is particularly evident in the global connectivity that has been enabled by the internet, which has
allowed for increased interconnections between societies, businesses, and individuals. By 2025, worldwide data cre-
ation is expected to expand to a minimum of 180 zettabytes1 through data connectivity over the internet, ulti-
mately advancing globalization. E-commerce sites such as Amazon2, eBay 3, Alibaba 4, etc. aggregate both prod-
ucts and businesses globally to create large catalogs of information available to a consumer. Spotify5 and Netflix
6 similarly create global catalogs of media, only restricted by licensing and user preferences driven by cultural and
language preferences.
1https://www.statista.com/statistics/871513/worldwide-data-created/
2https://www.amazon.com
3https://www.ebay.com
4https://www.alibaba.com
5https://www.spotify.com
6https://www.netflix.com

Humans, unlike machines, have inherent limitations in storing, retrieving, and processing large information61. This
limitation has led to the development of mechanisms that augment human ability through more efficient filtering,
sorting, summarizing, visualizing, and retrieving information61. However, the need for efficient information pro-
cessing has become increasingly important in today’s digital age, where the volume of data generated is staggering
and ever-increasing. To address this challenge, various additional techniques have emerged, including the devel-
opment of recommender systems75. Recommender systems are intelligent algorithms that assist users in decision-
making processes by providing recommendations based on their preferences and past behavior. These systems have
found widespread use in various industries, including e-commerce, music, and entertainment, and have proven to
be effective in improving customer satisfaction and loyalty. By leveraging machine learning and data mining tech-
niques, recommender systems can analyze user data and make personalized recommendations, thus reducing the
information overload that users may experience78. Despite their potential benefits, recommender systems are not
without their limitations. One challenge is the difficulty in accurately modeling user preferences, particularly in
cases where cultural and socio-economic factors play a significant role in decision-making. Accordingly, it is es-
sential to explore the development of more sophisticated recommender systems that incorporate a wider range of
factors, including cultural and socio-economic considerations. Such systems would require a greater understand-
ing of human decision-making processes and the factors that influence them and would need to be designed with
transparency and ethical considerations in mind.
1.3 Globalization and Plan Selection in Media
Globalization is described as "how trade and technology have made the world into a more connected and inter-
dependent place"73. The digital and information era has accelerated globalization. This phenomenon of accel-
erated globalization has brought tremendous business opportunities for various industries, including the media
and entertainment industry. With the advent of the internet and information and communication technologies,
businesses can now expand into previously restricted markets due to language, regulations, barriers in product
delivery, and commercial costs51. The media entertainment industry, in particular, has traditionally been local-
ized, owing to constraints in localized linear TV programming. Linear TV programming is delivered via a network
provider, where the provider has predefined programming, ads, and time segments1. However, with the emergence
of streaming media and on-demand programming, which account for a minimum of 63% of consumer viewing1, lin-
ear TV has faced intense competition. In response, companies such as Netflix, DisneyPlus + Hulu, and Amazon-
PrimeVideo have recognized the profitability and availability of the global market within the last decade2, leading
to increased competition for market share.
While globalization presents profitability opportunities, it also poses several challenges in business strategy21. To
profit from globalization, businesses need to strike a balance between streamlining product operations and tailoring
products to meet consumer expectations, which may differ from country to country. Differences in user preferences
due to socio-economic, geographic, or cultural variations between countries and regions can create segmentation on
product preferences and pricing17. This complexity is often apparent in product-based media subscription plans
and their prices.
In light of these challenges, businesses in the media entertainment industry need to develop and adopt innovative
approaches that enable them to meet consumer expectations and capitalize on the available opportunities. Recom-
mender systems have emerged as one such approach to assist users in their decision-making by providing intelli-
gent recommendations. These systems have been widely used in the e-commerce, music, and entertainment indus-
tries 75. However, existing recommender systems often fail to consider the socio-economic, geographic, or cultural
variations between countries and regions, thereby limiting their ability to understand user preferences71 accurately.
This limitation underscores the need for a more global, socio-economic, and culturally aware recommender system
that can address the challenges of globalization and provide businesses with a competitive advantage.

1.4 Problem Statement and Challenge
Culture plays an important role in shaping an individual’s preferences in a wide range of domains such as product
selection, social interactions, education, and entertainment. Recommender systems have been extensively studied
for personalizing recommendations in media, music, and consumer products. Previous studies have also evaluated
the efficacy of these systems in providing recommendations that align with cultural, socioeconomic, and geographic
contexts. Despite these efforts, the design of recommender systems that intentionally incorporate contextual in-
formation related to users’ cultural, socioeconomic, and geographic backgrounds remains limited. This represents
a significant research gap, as the lack of culturally, socioeconomically, and geographically aware recommendation
systems may lead to ineffective or biased recommendations that do not adequately account for the specific needs
and preferences of users from different backgrounds. Therefore, there is a need for further research that focuses on
developing more inclusive and culturally sensitive recommender systems, which can effectively serve diverse user
populations by accounting for the contextual factors that influence their preferences.
1.5 Contribution
This paper makes a significant contribution to the field of recommender systems by exploring the potential of a
global, socio-economic, and culturally aware approach. The study’s main focus is to understand the impact of cul-
tural identity and socio-economic factors on consumer preferences and recommenders’ accuracy. The proposed on-
tology and approach for incorporating these factors into recommender systems provide a basis for further research
on this topic. Moreover, the paper provides an illustration of the potential of the proposed approach by presenting
a scenario of consumer subscription and plan selection in the media entertainment industry. The scenario demon-
strates how current recommender systems fall short of understanding user preferences accurately due to their lack
of awareness of socio-economic and cultural factors. The proposed approach addresses this limitation by updating
recommendations in response to changing socio-economic conditions.
This research is significant because it highlights the need for a more comprehensive approach to recommender sys-
tems that can incorporate socio-economic and cultural factors. It contributes to the development of a more accu-
rate and effective recommender system that can cater to diverse markets, and ultimately benefit companies seeking
to expand globally. In particular, this study presents a comprehensive analysis of the current state-of-the-art rec-
ommender systems, focusing on context-aware systems. Specifically, we investigate the potential of incorporating
cultural, socio-economic, and geographic indicators as context into recommender systems. We begin by reviewing
existing literature on cultural models and the limited research that has been conducted on incorporating these in-
dicators into recommender systems. To identify relevant indicators, we leverage publicly available data on these
factors for individual countries across the globe. Based on this analysis, we propose an ontology that incorporates
these indicators and outlines the principal features that can be integrated into recommender systems to enhance
the accuracy of recommendations.
1.6 Summary and Outline
The field of recommender systems has gained significant attention in recent years due to the increasing demand for
personalized and customized options for customers. However, despite their popularity and widespread use, these
systems have been criticized for their limitations in accurately understanding user preferences. Specifically, they
lack awareness of socio-economic and cultural factors, which have a significant impact on consumer behaviour and
preferences. Moreover, these systems often fail to update recommendations in response to changing socio-economic
conditions. To address these limitations, this paper aims to investigate the potential of a recommender system that
takes into account socio-economic and cultural factors.
This section introduced the topic, providing a brief overview of the research problem and our approach to address-
ing it. We presented a motivating scenario and outlined the main objectives of our research. The subsequent sec-
tions of this paper are structured as follows:

Section 2 - Related Works: This section presents a review of existing research on recommender systems. We will
discuss the current state-of-the-art in various types of recommender systems and their underlying design princi-
ples for generating recommendations. We will devote additional attention to context-aware recommender systems,
which are particularly relevant to our motivating scenario. Moreover, we will examine two primary models for
assessing culture across different regions and countries. We will also survey the existing literature on how socio-
economic and cultural contexts have been incorporated or evaluated in recommender systems.
Section 3 - Methods and Materials: This section will outline the methodology employed to evaluate the efficacy of
incorporating socio-economic and cultural indicators as context in recommender systems. Our proposed solution
entails concatenating non-domain-specific and domain-specific indicators, which are subsequently standardized,
classified, and modelled. The feature set is subjected to rigorous analysis to ensure optimal performance.
Section 4 - Experimentation Results and Evaluation: This section will present the results obtained through the
methodology described earlier. We will discuss the techniques utilized for feature engineering47, model compari-
son, and evaluation to understand the influence of socio-economic and cultural factors on predicting subscription
preferences based on price.
Section 5 - Conclusion: This section will represent the concluding section of our research and will provide a re-
view of the achieved results and their effectiveness in meeting the intended research goals. In this section, we also
briefly discuss potential areas of future research extension that the author intends to pursue.
2 RELATED WORK
Recommender systems are systems such as those seen in Pandora, Netflix, and Spotify, where the system intelli-
gently learns specific preferences for a user over time. Data presents itself as a user interacts with the system, and
the system learns the user’s behaviour. As a result, the system suggests more and more accurate and intelligent
recommendations to a user based on learned preferences through data and time. This data improves the decision-
making process and eliminates information that may not be relevant. Recommender systems are used in various
applications, including those most commonly found in media, social networking, and advertisement. In the case of
advertising, recommender systems may also attempt to persuade a user into a purchase67.
2.1 Variations in Producing Recommendations
With the maturity of Recommender Systems, several techniques have emerged in forming user preferences to pro-
duce a recommendation. These techniques aim to reduce information retrieval, distill information into tasks and
goals, and finally, project a proactive prediction as a recommendation to a user. Various techniques are utilized
to take on obstacles in certain domains. For instance, in the media domain, user feedback on previously made se-
lections, such as liked or not liked, is captured and applied. These previously used selections, with additive user
context, help narrow the future information space by applying a learned understanding of a user’s preference over
time to similar type items, otherwise known as item-based recommendations79. In this case, users may be grouped
together based on their preferences. For example, a user searching for ski apparel may be similarly grouped with
those searching for other snow apparel, such as down jackets. While all these techniques may vary, they all seek to
narrow the information space, derive the intent of a specific user, and assist the user in selecting information, an
experience, or a product relevant to either their need or the search. He et al.33 proposed a Noise-augmented Con-
trastive Learning for Sequential Recommendation (NCL4Rec) that addresses the limitations of current methods
by introducing noise-guided data augmentation and a unique noise loss function, leading to improved performance
over state-of-the-art models in handling noisy data in sequential recommendations. There is a minimum of four
classes of recommender systems: Collaborative Filtering, Content-Based, Knowledge-Based, and Context Aware67.
We will explore these further in the upcoming sections.

2.1.1 Collaborative Filtering Based Recommender
Collaborative Filtering67is a class of recommender systems dependent on the user’s interactions or feedback with
the system. They are considered user-based systems. The system can either explicitly inquire about interactions or
user feedback, or implicitly derive them. Explicit feedback is the feedback that is collected purposefully. Examples
of explicit feedback may be such as those with likes or dislikes in song titles, or those of user ratings when review-
ing restaurants. However, the system can also implicitly derive and collect feedback. Examples of implicit feedback
are those such as when a user searches for a particular movie or book, or even the frequency by which a user may
search for certain clothing.
This feedback is then used to determine similarities or dissimilarities across users. Within collaborative filtering,
we often compute similarity to determine as the method or likelihood of a user selecting a different item for similar
interests or reasoning. The similarity is computed as a mechanism to describe implicit likeness between users based
on their implicit and explicit feedback. In the example of music, these users have selected music titles similar to
other users’ preferences or to other similar music titles they others have listened to in either the past or present
(e.g. current music trends). We may consider these similar users in the same neighbourhood. These neighbours
may have similarity computed based on either the other users’ likes or ratings, or based on the user’s own ratings
or likes63. The similarity relationship may be inferred based on either direction. Collaborative filtering is a flexible
approach to variations in a user’s preference, where it is not dependent on the inference of metadata on an object,
such as genre within the music example. The methods of calculating neighbours are based on machine learning
techniques. They may use neighbourhood models, decision tree models, rule-based models69, latent factorization
models, or even models such as Naive Bayes.
2.1.2 Content Based Recommender
Content-based recommender systems4 are systems that heavily depend on metadata, data embedded or stored, or
data that is systematically collected. This metadata is used to describe the attributes of an object or item. These
recommender systems are typically item-based systems vs user-based systems. Similar to collaborative filtering in
these systems, the recommendation outcome is computing similarity. However, in this case, the similarity is within
the context of the user’s liked or rated item. This metadata is data embedded or stored that describes an object or
item used to find items uniquely similar to the item a user has previously liked or rated. Since similarity is item-
based, content-based recommender systems almost exclusively focus on the owner’s rating or like as a key input to
determining which items a similarity algorithm should initially be based on, vs a neighbouring user. Typically, in
these systems, other users have no role.
Attributes used in content-based recommender systems may either exist on the item or the user. In these cases,
the metadata may be item data that is intentionally stored with the item, such as with a book, song, or movie. In
the example of a book, the genre, the author, the publishing house, and other descriptive attributes are all stored
with the book. A movie’s attributes would include information such as genre, actors, ratings, and other descriptors
that may exist. A user’s attribute information may include domain-specific knowledge relative to that user. In the
music example, this may include titles they have played, or recently played, the items they have liked or not liked,
or inferred data, such as keyword searches, search history, or other similar examples.
The steps to creating a content-based recommender system involve 1) item and domain-based feature extraction,
2) constructing a learning-based User Profile model, and lastly, 3) a method for filtering and predicting a recom-
mendation. Feature extraction plays a pivotal role in content-based systems. We need to pre-process most of the
attributes associated with the user or the item, often extracting them from the text. The emphasis on feature ex-

traction is to provide specific areas of focus that have a meaningful impact on predicting the user’s interests. The
features are then ranked or measured statistically for their impact. The learning-based user model provides a set
of key characteristics that are learned and adapted based on a user’s previous history with items and their ratings,
likes, or interactions. As new items of interest are determined, this model would adapt and change to reflect the
user’s interests accordingly. Lastly, the user model and the features are used to make an effective recommendation
for the user’s future interest.
2.1.3 Knowledge Based Recommender
Knowledge-based recommender systems64, unlike collaborative filtering or content-based systems, heavily depend
on interactions with the user. The user supplies the system with a set of requirements, then the system sources
domain-specific data and combines the domain-specific data with item-specific attributes. Once complete, the sys-
tem then predicts a recommendation. The process is typically iterative and allows users to further refine their re-
quirements based on the set of information predicted. These systems require the use of domain-specific databases
as a critical input to predicting the user’s preference.
In previously described recommender systems, the attributes of items may be used independently or cooperatively
to predict a user’s recommendation. Knowledge-based systems cooperatively use all of an item’s attributes and
match them with the user-provided requirements to make a prediction. A user may specify requirements that are
constraint-based, such as those that may be associated with recommender systems predicting purchase decisions.
Examples in this space may be those associated with flight, real estate, or vehicle purchase recommendations. These
systems often have a predefined set of choices. A flight-based recommender system will request departure and ar-
rival date and time information, preferences in stops, tolerance in the duration of layovers, alliance preference, and
other such constraints. Default requirements may be used as a manner by which to guide a user to make a more
refined selection.
This refinement narrows results. Flights default to exactly that day, and users may also expand the search to +/-
3 days to broaden the results. A ranking process is also used to provide a way to simplify the presentation of in-
formation retrieved to the user. In these cases, the ranking process may be a single attribute. We may see an ex-
ample of this within real estate, where a constraint in an area is drawn with boundaries in a user interactive map
or a zip code. A utility function may frequently define a constraint. This utility function matches the attributes to
a weighting that is based on a pre-determined assumption. The assumption is based on the utility of the attribute
in reference to the user’s selection. For instance, within the real estate system, the system may specify that price
or affordability may have a higher weight in displaying housing when matching a user preference. This system may
set this weighting over a user’s prefer’s preference in the number of bathrooms if in fact, bathrooms were not speci-
fied by the user.
A new type of recommender systems, called Cognitive Recommender Systems13, focus on: (i) organizing the big
data in a Data Lake9; (ii) automatically contextualize it in a knowledge lake10 to form a large knowledge graph;
(iii) mimicking the knowledge of subject-matter experts (using crowdsourcing services) to enrich the knowledge
grapg 7, 8; (iv) leverage the personality, behaviour, and attitude of users to enrich and augment the knowledge
graph 6, 12, 56 ; and (v) use novel embeddings approach to summarize the large knowledge graph70, 78. The whole
model is represented as ProcessGPT14, which fed the enriched knowledge graph into an AI engine to enable intelli-
gent recommendations.

2.1.4 Context Aware Based Recommender
To define context-aware recommender systems, we must first explore context. This includes what it is, how it is
defined in computing, what context awareness is, and how context manifests in systems. Scholars have described
context in various ways in years past, so much so that its use in computing has been for numerous years hotly de-
bated. Within the realm of research, the scope of how wide and how far context has been used was often defined
or constrained by the researcher himself87. Context, however, has a clear purpose. That purpose is to provide clar-
ity and efficiency in communication60. When the context is commonly shared across systems or users, it creates a
basis for understanding. This understanding bridges cultural divides, traverses differences in language, and brings
forth shared understanding in domain knowledge, either in breadth and depth, or cross-domain. Conversely, when
the context does not exist between parties, communication may falter, creating misunderstanding. While many
definitions have been used over the years, context may be thought of as providing reasoning, intent, or rationale to
an event, occurrence, or thought such that it may be understood to the fullest capacity. The basis for this reason-
ing, intent, or rationale is often held within the characteristics surrounding an entity or user’s situation58.
Context awareness in computing is a phrase used to describe the state in which a system is situationally aware.
Gartner uses the following definition to describe context-aware computing: "a style of computing in which situa-
tional and environmental information about people, places and things is used to anticipate immediate needs and
proactively offer enriched, situation-aware and usable content, functions and experiences."7 In other words, con-
text awareness primarily concerns the ability to sense a change in either situation or environmental information
and respond accordingly5. There are several ways in which we can define attributes that are representative of sys-
tems that exhibit context awareness. We can minimally define these attributes within a system as one of the fol-
lowing 87:
1. the awareness of the situational and environmental context surrounding an entity’s environment
2. the ability to utilize awareness to personalize and make a recommendation that is intended to meet an en-
tity’s interest through the context collected
3. the ability to discover or sense, and adapt to the changing needs of the entity and their surrounding environ-
ment or situation and then revise a personalization and recommendation based on that discovery
4. the ability for a system to take ambient signals, such as signals from IOT devices, mobile or biometric de-
vices, to understand and appropriately inject into a recommendation whereby momentary adaptations fre-
quently occur to meet the transient nature of a user
Context-aware recommender systems67, 4 are systems that often describe and make recommendations based on
the relationship of the user and the item at the point of when and where the user is. They are designed on the
presumption that the time (when) and location (where) of the user, at the point of selection, influence what will
result in a successful recommendation by the system. In this case, the user’s when and where are considered the
context in which a user is currently operating. This context can be described in physical conditions of when and
where, and in non-physical conditions such as social, emotional, or activity-based conditions16. The following defi-
nitions can be used to understand the categories of context-aware systems16:
• Location-Based describes geographic attributes that describe where the user is.
• Time-Based (Temporal) describes the point in time where the user exists.
7https://www.gartner.com/en/information-technology/glossary/context-aware-computing-2

Figure 1. Various Types of Context Aware Systems16
• Social-Based describes the social attributes of the user, such as their social network, social interests, etc.
• Emotion-Based describes the feelings or emotions of a user.
• Activity-Based describes what events or activities the user is engaged in. Event extraction approaches53, 54
can be used for promptly apprehending event information from massive textual data.
• Multi-Dimension describes the combination of any types of context that correlate with each other to form
deeper situational awareness.
Any number of these areas of conditions can be correlated and used to describe a multi-dimensional16 approach
to context. This multi-dimensional approach could be used in recommending certain types of music based on loca-
tion, geography, and time of the year, e.g., where a recommendation combines Spanish influences within Christmas
music because a user’s context is determined to be the Christmas holiday while on vacation in Mexico. Mathemat-
ically, the single and multi-dimensional cases are represented by, the item [I] and the possible recommendations
[R], which are further developed by a set of [C] contextualized attributes3. Types of context may describe the at-
tributes of a specific location or time. For instance, with location, where location is a country, other types of sup-
porting information, such as country-specific demographic information, may further describe the context of the
user’s situational environment. This specific country’s demographic information may include language, currency,
population, macroeconomics, and cultural or social characteristics. With advertisement-based recommender sys-
tems, a recommendation for an advertisement may include a country-specific version of an item. There are cases
where the context of a user is used to identify similar users (e.g. users within the same geographic area) to provide
a recommendation based on an already-learned understanding of other users. In these cases, unsupervised machine
learning clustering techniques, such as K-Means, are used to group and then identify the most similar user(s). The
attributes of the cluster in the geography example are those attributes adjacent in relation to geography, e.g. IP
Address, longitude, and latitude. The Euclidean Distance 2.1.4, the line between two points on a plane, is often
used to calculate the distance between users within the cluster. This helps to determine relationship proximity.
This example is one explored in research on Cultural Heritage36.
dpp, qq“
gffe nÿ
i“1
pqi´ piq2 Equation 1.
2.1 Euclidian Distance. Euclidian Distance

The relationship proximity is then used to find the nearest neighbourq in the cluster to our userp by which to
inform a recommendation. In some cases of measuring geographic distances with more accuracy, the countries rep-
resenting the users within a cluster are measured by researchers utilizing Vincenty’s method of calculating the dis-
tance between countries37. This method measures the shortest spherical distance between two points, where each
point represents a geographic location of a single country on the earth’s surface.
Figure 2. Processes in determining contextual recommendations
Information Processing for Context-Aware Recommendations. Context-aware recommender systems exist in many
application domains. Researchers in 2017 generalized these domains into six areas: (i) travel and tourism, (ii) places,
(iii) e-documents, (iv) multimedia, (v) e-commerce, and (vi) others32. To enrich a recommendation [R] with the
right context [C], there are several stages to processing the set of possibilities to present to a user Figure 2. The
domain (6 - Domain) is the narrower set of information spaces that are used to extract context. Identifying the do-
main or space of context in which enrichment is targeted provides a base for the system. Within each domain, a
process then occurs to determine the attributes (5 - Attribute Identification) of the domain that apply to the item
[I]. Once these attributes are identified, the data related to these attributes are extracted from the domain (4 - In-
formation Extraction). This extraction is a type of pre-filtering. Post-pre-filtering, the information is assimilated
into a single model (3 - Context Modelling). There are several modelling techniques in Table 1: Markup, Logic,
Ontology, Vector, and Graph. There is a final iterative filtering process (2 - Filtering), that reduces irrelevant in-
formation, often through scoring once a model is created, and then lastly a final recommendation is produced (1 -
Final Recommendation).
Temporal Drifts in Context-Aware Recommender Systems. In recommendations, several factors may be consid-
ered when formulating a user’s preference. To predict user preferences, different models have been used with rating
scales to produce relatively static predictions. Humans, however, are more fluid in their preferences, influenced by
others, and develop and change preferences over time. In its simplest form, these systems use rating scales. How-

Markup refers to the tagging, labelling, or inscription of metadata to correlate context further.
Logic refers to the application of logic as a way of describing the correlation of context with the item or user
Ontology describes the formalization of context into an organized structure
Vector describes the mathematical representation of information
Graph refers to the organization of information based on relationship
Table 1. Techniques in modeling context32
ever, to consider recommendations more accurately, the system must consider the human biases that may occur
over time. These biases could be due to cultural influences, economic influences, social influences, or rare, but oc-
casional, personality shifts. An example of a change in preference over time may be a user’s preference towards
animated movies when they are younger, vs action movies as they mature towards a young adulthood. These in-
stances of preferences in time are called temporal drifts83. Temporal drifts can be modelled to show how changes
affect the domain or a user. Zafari83 modelled temporal changes that were tested with both social influences and
conditional preferences at various periods in time. In his work, Zafari included preferences arising from social influ-
ences for certain feature categories. These were tested in very domain-specific areas, such as music.
In these domain-specific areas categories, entity biases were modelled using latent factor techniques to consider
changes in preferences. Latent factorization, a mathematical approach to recognizing otherwise less observed fac-
tors in a model, was used to provide a heavier weighting to recently selected preferences by a user. Koren termed
this approach to temporal-based recommender systems, Latent Temporal Based Optimizations (LTO)50. Further
work has been done to include additional considerations around the dynamic nature of certain categories of pref-
erences, and the ability to capture the granularity of detail within these categories more specifically. This gran-
ularity allowed for the specificity needed to highlight static features that were unchanged due to temporal drift
vs features that were highly likely to be influenced by temporal drift49. Other research reviewed variations in ap-
proaches to determine temporal drift using Bayesian models, tensor factorization, and memory-based time-aware
systems. While these approaches in modelling differed, several of them added a weighting approach to the prefer-
ences to mature the dynamic aspects of features that were heavily influenced by temporal drift83.
2.2 Culture and Culture Models
Culture can be described as “the collective programming of the mind which distinguishes the members of one hu-
man group from another”35. Over the years, several models of culture have been developed and used to both eval-
uate and understand various domains and the effects of culture in models. These various models have been ap-
plied in research to differentiate cultures and provide the relevant context where culture is a factor. There are a
few prominent models in particular, one by Hofstede, and another by Tropenaar.
2.2.1 Hofstede’s Cultural Model
Hofstede developed a well-regarded model for evaluating culture across several key dimensions. Each dimension is
assigned pre-computed indices that describe each country through six distinct measures. These measures can be
used to describe the spatial proximity between countries on each dimension. This relativity between indices is used
to evaluate comparability and similarity across countries both individually at each dimension and in totality across

all six dimensions. The six dimensions35 that Hofstede defined are:
1. Power Distance - the degree at which inequality within society is expected and respected or not expected
and disrespected. For example, high degrees of power distance is associated with centralized or hierarchical
societies.
2. Individualism - this is the importance that individuals place on the need to have collective structures and
interdependence, or autonomy and self.
3. Masculinity - represents a preference for gender-dominant traits within a society. These often describe how
society has an inherent need for achievement, assertion, heroism, competition, or material rewards for suc-
cess. Societies largely more consensus-based, meek, modest, cooperative, and ethereal are regarded as femi-
ninity.
4. Uncertainty Avoidance - represents the most dominant behaviours in how a society thinks about and pre-
pares for the future and how comfortable individuals within the society are with ambiguity.
5. Long Term Orientation - understands how a societal group may perceive and make decisions in relation to
current events pragmatically, or seek to retain its past and traditional norms.
6. Indulgence - describes the society’s tolerance or orientation towards innate human needs that directly relate
to enjoyment vs an orientation towards alignment with social norms that suppress innate needs related to
enjoyment.
2.2.2 Tropenaar’s Cultural Model
Other cultural models have also been developed, showing slightly different models, but representing extremes in
measures to quantify differences accurately. For instance, Tropenaar77, also ascertained in his research that the
more we could understand cultural differences, the more we would be able to bridge those differences in social, re-
lational, community, government, and work. He defined cultural differences around the differences between seven
different pairs of attributes: 1) universalistic and particularistic 2) individualistic and communitarian 3) specific
and diffuse 4) neutral and affective 5) achieved and ascribed, 6) sequential and synchronic 7) internal and external.
These can be explained in more detail below.
1. Universalistic vs Particularistic - Universalistic describes the emphasis in one culture to put universal norms
and truths over relational or achievement-based ones. In Particularistic, relational, and achievement-based
cultures, laws and norms exist to help define the interaction between people and how they relate.
2. Individualistic and Communitarian - Communitarian cultures are cultures that emphasize and reward the
needs of the community over the needs of the individual. In these cultures, individuals are expected to put
the community’s needs over their own. Individualistic cultures emphasize the needs, happiness, and welfare
or fulfilment of the individual, and their systems reward such.
3. Specific vs Diffuse - Specific cultures are those that can differentiate between each component and recognize
how they form a larger structure. These cultures use facts, measures, standards, and contracts to define indi-
vidual components. Business, for instance, is referred to and understood based on these facts15. Diffused cul-
tures, however, rely on relationships and uphold values of empathy, trust, and reliability68. The significance
of these relationships is greater than that of facts, measures, standards, and contracts. Achieving business
aims in this culture begins with creating relationships.

4. Affective vs Neutral - These cultural attributes describe the degree to which the display of emotions by an
individual is acceptable. Neutral cultures deem showing emotion to diminish power and influence. These cul-
tures encourage the curtailing of emotions.
5. Achieved vs Ascribed - These cultural attributes describe how individuals within a culture are assigned ‘sta-
tus’. In achieved cultures, status is derived from results (achievements). An individual’s ability to maintain
their status is derived from the continuity of results. In ascribed cultures, status is assigned by class, birth,
rank, age, gender, or wealth.
6. Sequential vs Synchronic - Time and how people within a culture think of time can be a differentiator. Se-
quential cultures value planning. They value the sequence of plans, and keeping to defined plans over adapt-
ing. Synchronic cultures value the ability to execute time-based events in parallel and adjust as needed.
7. Internally or Externally Controlled - The relationship with the natural environment is also a cultural identi-
fier. Internally controlled societies believe they can exert and direct their lives, including over natural forces
within the environment. Externally controlled societies believe they must exist in harmony with their natural
environment. They exert limited or no control over how their destiny is shaped.
2.3 Socio-economic and Cultural Influences in Context-Aware Recommender Systems
As the use of recommender systems is still early, there has been a limited amount of research reviewing the out-
comes of either socio-economic, or cultural influences in context-aware recommender systems, and even more lim-
ited is the combination of both.
2.3.1 Cultural Influences as Context
In the context frame, culture plays a clear role as an example of an instance that can describe the situation and
environment of a user. Therefore, a system that includes culture is considered context-aware. Culture applies to
a people group. However, country attributes of culture can be considered a reasonable approximation in recom-
mender systems36. Researchers have long studied the impact of culture on recommender systems. These studies
have applied cultural context to the evaluation and validation of results24; 23; 25. This research also suggests that
travellers from different cultures and geographies have varying rating behaviours25. Limited research has included
the use of culture as the context in recommender systems38. Cultural Heritage was one such study that reviewed
how cross-cultural contextualization may be applied within recommender systems. This research utilized rating
data, matrix factorization, and clustering techniques to observe how culture affects user preferences36. This re-
search uncovered that, while often, recommender systems were applied individually, there were cases where aggre-
gate recommendations may also be applied. For example, in cross-cultural contextualization, the research found
that country or geographic location could be used as input into the recommender system.
There have also been a number of studies around the context of user preferences. Hoefstedes model has been used
in research outlining musical preferences amongst geographically distributed users and also in user interfaces in
mobile recommender systems. They used Hoefstede’s model to examine the correlation between similarity in users’
musical preferences. Three specific dimensions of Hoefstede’s indices were found to have a notable correlation (mas-
culinity, long-term orientation, and indulgence)57. In mobile recommender systems studies, uncertainty avoidance
and collectivism were most found to influence people’s behaviours and attitudes towards purchase intentions24.

2.3.2 Socio-Economic Indicators as Context
Some recent research in recommender systems has incorporated context in musical systems that add context to
traditional content-based approaches by incorporating elements of the user’s environment. In these cases, the user’s
context may include demographic information or information that includes information such as location. In these
cases, the location or demographics of the user’s area may be paired to make musical recommendations related to
select artists from or frequently played in that area45. In other examples, a particular location’s context suggested
music typical for that place of interest19. Similarly, demographic indicators were also factored into travel recom-
mender systems, matching user and destination demographic information to provide more accurate hotel recom-
mendations 22. Housing preferences that match users’ demographic information for similarities in location have also
been an area of research43.
2.3.3 Combining both Socio-Economic and Cultural Context
Several studies have highlighted the fact that certain tendencies toward traditionally elite entertainment experi-
ences, such as Opera, Theatre, Ballet, Museums, and classical music, have been associated with both various cul-
tural influences and economic status. These are commonly created during the early years of development and are
influenced by exposure18. These studies hypothesize that certain elite economic status enables access to various
experiences leading to knowledge and preferences that differ from those associated with lower economic and differ-
ent cultural backgrounds; this is especially relevant in music44.
Within music, there have been different studies that have reviewed various contexts surrounding geographic loca-
tion or the distances between user’s countries, distances between languages of various countries, and socio-economic
characteristics such as GDP or Purchase Price Parity66, 57, 84. In some cases, these socio-economic dimensions and
characteristics have been used to elaborate further on the cultural differences between countries utilizing the World
Happiness Report 8. The World Happiness Report utilizes a series of indices that is believed through study to con-
stitute happiness. These indices include gross domestic product (GDP), social support, healthy life expectancy
at birth, freedom to make life choices, generosity, perceptions of corruption, positive affect, negative affect, and
confidence in national government. In some of these research areas, socio-economic characteristics, in addition to
culture, have provided better accuracy in recommender models over those that relied only on learning user pref-
erences based on ratings, selections, and other user-derived attributes. In a number of cases, a feature vector is
constructed for each user that includes the socio-economic influences gathered from inputs such as the World Hap-
piness Report, in addition to the scores from Hofstede’s Cultural Indices for the user’s country. This feature vector
is then used to find cultural similarities in users’ listening preferences.
In some studies on music preferences, however, there has been no correlation between purely economic and geo-
graphic distances between countries57. In these studies, without attributes that represented the cultural differ-
ences that influence individual user preferences, recommendations did not improve. This may be because there
are varying economic classes within various sub-country geographic levels. The cultural dimensions of masculin-
ity, long-term orientation, indulgence, and the between-country distances in language were found to be positively
correlated with an individual’s musical preferences.
3 METHODOLOGY
For this research, we define a novel approach to understanding the socio-economic-cultural distances between coun-
tries that may be relevant in streaming media entertainment. We use a combination of supervised, and unsuper-
8https://worldhappiness.report/ed/2022/

vised machine learning techniques, an ontology that includes a number of socio-economic-cultural indicators, as
well as economic and opportunity indicators that are specific to streaming video. We determine the relevant fea-
tures that have the highest impact and use these features to create various representative vectors that can be in-
corporated in order to provide a context within a recommender system. In our motivating scenario, we review the
application of how a user in a specific country may have a certain preference in a subscription plan for streaming
based on other users that are in a similar socio-economic-cultural country. We use a combination of key indicators
to calculate this specific similarity in streaming media between countries.
We then utilize a series of steps to pre-process our data, curate and enrich our data, normalize and filter our data,
reduce our data to key features, build and train a model to classify data, and then evaluate our model. These will
be discussed in more detail but a high-level visual of this process can be seen in Figure: 3. Data in this process
is extracted, curated, normalized, and filtered. We then enrich the domain data with socio-economic and cultural
data, select and store our features, and then model them into a final classifier. The final feature set is what we are
able to generalize into recommender systems for media-based subscriptions.
Figure 3. Data, Feature and ML Process for Understanding Socio-Economic-Cultural factors for Streaming Video Subcriptions
3.1 Data and Data Processing
Data Pre-processing. We use subscriber data that represents the plans and pricing selection of users within a coun-
try for a streaming media provider as our domain data. As pricing becomes most relevant when users have dis-
played a self-elected change in plan and price over a period, or subscribe and unsubscribe to a service over a pe-
riod. Therefore, we focus on cohorts who have self-elected a change, have left, and then resubscribed to the service
at least once. Users who have left and re-subscribed to the service at least once, represent a group of users where
potentially the rising costs of subscription services relative to perceived value in an increasingly competitive envi-
ronment is a potential reason for the user to leave the service vs maintain a service52.
We narrow our cohort to understand and try to predict the change in plan and price after the media service has
invoked a price increase. A single user may leave, return to the service (re-subscribe), change plans, or incur a
price change. Our pre-processing of the data includes aggregation by a user’s account, country, number of plan
changes, and the resulting from and to plan change. We used this data to create a base matrix representing each
country’s features. In our scenario, this final matrix will include attributes from our domain data, such as 1) the

population for each plan, 2) corresponding pricing, 3) the data of the most recent plan selection, and 4) the corre-
sponding country. As our research is at the country level, we eliminate the need and use for any personally identi-
fiable data in our dataset, by constructing the data at an aggregate level.
Curate, Enrich, Cleanse. In our domain data, we have all the data for each country. This minimizes some amount
of cleansing. However, depending on when new plans are introduced within a country, the timing of various mar-
keting strategies that drive particular plan selections, or changes in business strategy, our data may not be con-
sistent. To ensure a strong data set, we review the data and calculate various statistics around our data, such as
variance and mean. These statistics assist to identify and enable the removal of outliers.
For each country represented in the domain data, we enrich that country’s data with data made available through
various publicly available knowledge bases. The enriched streaming video plan data describes the country with ad-
ditional cultural, economic, demographic, geographic, infrastructure, and media-related data attributes for each
specific country. The potential feature data, from various knowledge bases, is not available for all countries. This
means that not every feature will be available for each country. In this case, we use techniques that include remov-
ing data, predicting potential substitutes, resorting to the last known observation (in our case the previous year’s
data), or imputing data with the mean using machine learning or other statistical methods.
Normalize and Filter. To minimize variance in constructing our vector, we normalize our features by applying a
logarithmic function that normalizes our data between zero and one. In some cases, we apply a filter to adjust the
range selection of our data. This filtering may be based on domain-related knowledge or to select data most rele-
vant to our model. For example, within the economic factors, the data may have existed for multiple years in some
of our public domain data. However, only the most recent data provides predictability in the current year. As we
classify our data using Neural Networks, features with similar scales help converge gradient descent to a local min-
imum significantly quicker than those that do not27. To do this, we apply a minimum and maximum scaler func-
tion. We can see a sample of the preprocessing steps in the pseudocode below 4.
Figure 4. Data Preprocessing Pseudocode
3.2 Feature Selection
We can group the variables identified with potential impact as cultural factors, economic factors, demographic fac-
tors, and geographic factors. We include country-specific infrastructure data related to broadband internet, mobile

networks, mobile and tv devices, and other media-related data attributes for each specific country. These factors
provide a potential indication of a particular country’s readiness and opportunity for streaming video.
Since our attributes are numerical, we skip feature extraction and move to reduce our feature set through the se-
lection of only highly relevant features. To understand which features are highly relevant, we use apply methods
to select features that may have the best impact on predictability. To achieve this, we organize our input data by
describing the data within an ontology. Our ontology describes a hierarchical class structure grouping related at-
tributes.
3.2.1 Feature Reduction through Correlation
Heatmaps are visualization tools that can allow gradients of colour across both the Y and X axis to visually dis-
play relationships between contexts. We use an approach similar to Buyrukoğlu20 and use a heat map to deter-
mine correlations between features and specifically our target prediction with our classifier. This approach allows
us to examine the relationships between each feature and our target prediction, enabling us to reduce our feature
selection to those with the highest perceived impacts. We reduce our features sets by removing features with less
than .25 correlation (Figure: 5).
Figure 5. Feature Reduction Pseudocode
3.3 Modelling Neural Network for Price Prediction
In this chapter, we reviewed the effectiveness of socio-economic-cultural aware features with domain data to pre-
dict consumer preferences in price. This allowed us to understand the potential positive impact of use in recom-
mender systems. We found these features to positively impact price prediction with relative accuracy.
We also found that the most effective machine learning model in prediction was a well-architected artificial neu-
ral network model with select features. We also learned that, with a well-architected neural network model, the
feature set could be reduced, providing computational efficiency with similar accuracy. For the artificial neural net-
work model, we chose a neural network model with one input layer, two hidden layers, and a final output layer,
with a single neuron. Figure 6 references an example neural network with two hidden layers, each layer reducing
the number of inputs and resulting in a final output layer.
To find the optimal batch size and epoch size, we run a process that tests the permutations of different batch sizes
and epoch sizes. We use mini-batch sizes at multiples of two, and epoch sizes starting at a maximum of three times
the number of predictive features in our input layer and then reducing. We use adaptive moment estimation or
’Adam’ as our optimization algorithm in our neural network to update our weights iteratively. Adam adapts the
learning rate with each training batch. This approach allows us to focus on optimizing our cost function without
concentrating on selecting the optimal learning rate.
We use the following three rules of thumb34to determine the number of neurons in each of our hidden layers:
• the number of neurons in a single hidden layer is somewhere between the number of features used in the in-
put layer, or previously hidden layer and the total number of predicted outputs in the output layer
• the number of neurons is the total number of predicted outputs in the output layer added to approximately

Figure 6. Artificial Neural Network with two hidden layers, and a single output
two-thirds the size of the previous input layer
• the number of neurons is less than twice the size of either the features used for input or the previous hidden
layer
We split our data for training, validation and evaluation. Then, we establish our initial ANN architecture param-
eters, inclusive of two hidden layers, the number of neurons in each layer, the batch and epoch size, the loss func-
tion, optimizer, learning rate, and activation function (Figure: 7).
3.4 Optimizing our Model Architecture
3.4.1 Preventing Over-fitting
In machine learning, when our model’s prediction may be inaccurate, one reason this occurs may be based on how
the training data fits the model. If too many features are incorporated into the model, it may memorize the values
of the training data and fail to generalize the data when applying the model over time to new examples. We know

Figure 7. Initial ANN Pseudocode
this state of memorization as over-fitting82. Similarly, when our model is too simple for our data, it may bias to-
ward certain training data values, also failing to generalize the model to fit different examples. This usually occurs
when there are insufficient features or data to train the model. This is called underfitting39.
Figure 8. Fitting a line to our model (Underfitting, Right Fitting, and Overfitting)
In our research, we aim to have enough data to reduce the likelihood of underfitting by increasing the data vol-
ume. Overfitting our data, however, remains a risk. To ensure that we do not over-fit our model, we use dropout74
as a mechanism to regulate our models in each layer. This regularization technique drops a specified number of
neurons with each training iteration. Dropout techniques work only for robust numbers of features. Each iteration
is equivalent to training a separate model by dropping different neurons in each iteration. In this case, envisioning
each iteration as a different network means each network will over-fit in different ways. Since each network over-
fits differently, the aggregate of all the different iterations reduces over-fitting.
Figure 8 displays the three categories of fit, where in the first example the model underfits the variance of found
in data over time, a second example where a model fits data over time reasonably well with little variance, and
the final example where a model becomes hyperaware to every variation in the data leading to potential issues and
inefficiencies over time.

3.4.2 Optimization and Activation
Neural networks train at different learning rates depending on the algorithm. This learning rate is the rate at
which our algorithm learns and adapts to new training data. In machine learning, as our data learns, it converges
to a local minimum that represents the best possible accuracy in our prediction. For our model, we choose the
Adam optimizer as an optimizer that adapts the fastest to learning our training data. Adam optimizers are com-
putationally efficient and adapt effectively for large feature sets or training data sets11, 48.
In neural networks, the neurons and layers represent weights and biases. In each layer of a neural network, and
with each neuron, these weights and biases are carried into the next stage as input. The technique is similar to
those within the human brain and its methods of learning. Activation functions represent the method by which
each of these weights and biases may be calculated42. We test several activation functions, including using a single
activation function for all layers and, eventually, using tailored and different activation functions for each layer in
our model. In our final model, we explore the use of the Sigmoid function. Our output is a price prediction. The
Sigmoid activation function converges to a single output, making its use in our model logical to test.
The Sigmoid activation function works by reducing our inputs (x) to a range between 0 and 1. It is typically used
in binary classification, or regression when a model output is a certain prediction59.
fpxq“ 1{p1` expp´xqq Equation 2.
3.1 Sigmoid Activation Function. Sigmoid Activation Function
We explore the use of a Relu, Rectified Linear Unit, activation function in one of our hidden layers. Relu activa-
tions are well-adapted and perform optimally for neural network hidden layers62.
fpxq“ maxp0, xq Equation 3.
3.2 Relu Activation Function. Relu Activation Function
And lastly, we experiment with the Tanh activation function, Tanh activation functions follow a more compressed
curve than a sigmoid activation function and therefore are known to perform more efficiently with multilayer mod-
els 46. They are often used in speech-to-text neural networks.
fpxq“ tanhpxq Equation 4.
3.3 Tanh Activation Function. Tanh Activation Function
3.4.3 Evaluation of our Model
We evaluate our classification model by reviewing metrics such as Accuracy, Precision, and F1. These metrics mea-
sure the impacts of what is otherwise known as a confusion matrix55 and the different elements within the ma-

trix relative to the others. In a confusion matrix, predictions are described as True Positives (TP), True Negatives
(TN), False Positives (FP), and False Negatives (FN). Measures utilizing these descriptions are used to evaluate
how well a model performed.
Accuracy represents the efficacy of how accurate our model predictions were by comparing true positives and true
negatives to the total number of predictions made.
Accuracy“ pT P` T Nq pT P` T N` F P` F Nq Equation 5.
3.4 Accuracy. Accuracy
Precision represents how often our positive predictions were correctly made compared to all our positive predic-
tions.
P recision“ T P pT P` F Pq Equation 6.
3.5 Precision. Precision
The recall represents the efficiency of our predictions by comparing our true positive predictions to all the predic-
tions that should have been positive.
Recall“ T P pT P` F Nq Equation 7.
3.6 Recall. Recall
F1 takes into account both precision and recall, noting the trade-off between the two. The equation can be de-
scribed as mathematically as either:
F 1Score“ T P T P` 1 2pF P` F Nq Equation 8.
F1 Score
or
F 1Score“ 2˚ P recision˚ Recall P recision` Recall Equation 9.
3.7 & 3.8 F1 Score

We also compare our model to other classification machine learning models such as Stochastic Gradient Descent,
Random Forest, and Gaussian Naive Bayes.
4 EXPERIMENT, RESULTS AND EVALUATION
4.1 Motivating Scenario: Streaming Media Domain
Our project aims to understand the relationship between streaming media plan selection and cultural and socio-
economic indicators. We use an aggregation of customers across a few selected countries. These particular cus-
tomers have changed subscription plans after a price increase has occurred. These selected countries are based on
available cultural and socio-economic indicators. To represent the reaction to a plan change, we isolate customers
who instantiated what would be considered a down-graded plan change within 3mos of the price increase. We ag-
gregate customers within a country to understand the frequency of plan changes, and the similarities between the
types of plans that these users were on and downgraded to. Our model uses three classes of features, all aggre-
gated at the country level. These three classes of features are streaming media domain features, cultural indica-
tors, and socio-economic features.
4.1.1 Domain Features
For domain-related features, we extract customer categorical and non-categorical numerical features available from
a media-related company. This data is aggregated by country, the type of plan change, the date of sign-up, and
the date of the plan downgrade. We review only downgraded plan data in a single year. We use the domain’s ex-
perts’ and streaming media managers’ points of view about each feature. The main features used in our scenario
are:
• The number of accounts at a country level that has downgraded plans
• The total number of times a customer changed plans throughout the customer history
• Whether they have ever left, they abandoned their subscription and returned to the service at least once
• The type of plan change that occurred, and what the to/from plan type and price were at the time of change
• The number of customers in a given country that enacted a plan downgrade on the same specified day
4.1.2 Cultural Features
We use Hoefstede’s cultural model and indices, as noted earlier in our paper. Hoefstede’s model provides country-
level features that enable the comparison of countries across range-mapped cultural indices, such as Long-Term
Orientation (LTOWVS), Power Distance (PDI), Individualism (IDV), Masculinity (MAS), Uncertainty Avoidance
(UAI), and Indulgence (IVR).
These indices provide spatial distance between countries to help understand cultural differences. For instance,
Japan has a score of 88 for long-term orientation, compared to Columbia, which has a score of 13. This represents
a more significant societal value placed on decisions and values that have an impact across long periods for most
people in Japan, as compared to Columbia, whose score indicates a more short-term orientation in values and deci-
sions. We aim to understand how the cultural indices at a country level may impact any of the media subscription
attributes for customers within that country.

4.1.3 Socio Economic Features
For our social and economic features, we gather publicly available information across several areas. These areas are
both domain and non-domain-relevant. Relevant indicators are typical in understanding a given country’s demo-
graphic, relevant infrastructure, economic status, or economic investments. Entertainment indicators are used to
describe our domain data. We concatenate this data with our country-specific level data both at the country level
and the streaming media domain level. We aim to find the relationship between a country’s socio-economic data
and customer actions in streaming media. We group this data across four main categories for each country:
• Infrastructure - the general network communication and broadband data available within that country. This
data consists of broadband subscriptions, mobile network coverage, and communication infrastructure invest-
ments.
• Demographics - which includes data related to population, and graduates in stem
• Economic Indicators - indicators of a country’s economy such as gross domestic product, foreign exchange
rate, and spending on communication infrastructure
• Market Opportunity - These features represent potential relevance to the opportunity for streaming media
within a given country. They are indicators such as the population streaming television, the average screen
viewing hours, global brand value, national films produced, and spending in entertainment.
4.2 Dataset
For our data set, Figure 9, we compile a list of open data from various sources with globally relevant socio-economic
data on all or most countries. These data sets included sources such as those from World Bank9, UN level data
10, Organization for Economic Co-operation and Development11, and Statista12. This socio-economic data in-
cludes 36 features and up to 195 unique labels, representing the number of potential countries. We use publicly
available data from Hoefstedes’ cultural indices13 across all available countries. The cultural data represents the
full six indices and 112 countries. The data was last updated in late 2015. For our domain data, we use a sampling
of data across 14 specific countries scattered globally across various continents. The domain data in this sample
set represents approximately 100,000 rows and 7 features.
4.3 Pre-Processing
As the data we retrieved is public, the quality and consistency of the data need to be evaluated. Data also is pre-
processed in order to ensure the highest quality of data inputted into our Machine Learning models. This pre-
processing enables the highest accuracy in our predictions.
4.3.1 Removing and Filtering Inconsistent Data
We denote numerous inconsistencies across data our socio-economic data. In particular, a wide range of absent or
stale data exists for certain indicators across countries. Rather than approximating this data with techniques such
9https://www.worldbank.org/en/home
10http://data.un.org/default.aspx
11https://www.oecd.org/
12https://www.statista.com/
13https://geerthofstede.com/research-and-vsm/dimension-data-matrix/

Figure 9. Domain and Non-Domain Specific Features
Figure 10. Sample Data from a selection of the extracted features
as mean, min, max, or zero, we utilize this opportunity to reduce our country feature set, and more densely orient
our domain data to a few countries. We filter only recent data and join all of our publicly available data with an
inner join. This reduces our feature set to 14 specific countries (Figure: 11) and drops all countries with absent or
stale data.
We also remove features in our domain data set that may be too predictive of our final result but will not gener-
alize well. For instance, data such as total downgraded subscribers for a specific date, and country, only indicates
to us that there was a collective reason on that day to downgrade their plan. As we prefer not to have our model
be hyper-aware of temporal differences at this stage, we remove this. In future work, more specific features that

Figure 11. Our 14 Countries with Full Cultural and Socio-Economic Features.
map to temporal differences may yield better, and more specific, predictions. Our current non-domain data set is
limited in its awareness of temporal factors, and as a result, remove this data.
4.3.2 Standardizing Numerical Data
As the range of data attributes across our data varies, and in some cases, the mean or variances of specific features
may differ significantly from one country to another, we standardize our data to minimize any potential deviations
that features may have either with each other or from country to country.
4.3.3 Normalizing Data
We normalize our data or otherwise potential features to be between 0 and 1 to ensure that we fit our model well
and do not inadvertently create biases with large variations in our data. We do this by using a linear transforma-
tion of our input value x. In particular, we perform min-max scaling26, where we take the minimum feature value
min(x) found and the maximum feature value max(x) found in our data and utilize the differences and the differ-
ence with our input value, to arrive at a representation of our original input value x. This new representation of x
is consistently between 0 and 1.
x1“ xscaled“ px´ minpxqq pmaxpxq´ minpxqq Equation 10.
Normalizing Data: Min-Max Scaler
4.3.4 Categorical Data Transformation
For our domain-based data, we identify some data as categorical. Categorical data identified is data such as which
plan the user subscribes to, and the information used to determine whether a customer has left and resubscribed

to the service. Our domain data also contains key date information. For date information, we separate out month
and year. We make use of the technique of one-hot encoding to classify our data into binary columns. We add
these new binary columns to our feature set and drop our previous ones.
Figure 12. Displaying culture correlations using a scatter matrix across countries
4.3.5 Evaluating diversity of our Cultural Data
Since culture is a key component of our work, we evaluate the distribution of diversity across our 14 countries and
their indices. This shows that our cultural data has little overlap and is appropriately spread across various in-
dices. We use a scatter plot to visualize the distribution. With the scatter plot we construct, we are able to under-
stand that our country choices vary well for our modeling exercise.
4.3.6 Splitting our Data
For our model, we split our data into several test data sets. We randomize the data to ensure that it has the possi-
bility of best representing the full data set as much as possible. In our final neural network, our data is divided up
into three parts: training data, test data, and validation data. We use our validation data to determine the hyper-
parameters in our neural network. We use a 30% split of our data across each data set.
4.4 Feature Reduction
We use price as an indicator of preferred plan selection in our population. As this is our predicted output in our
model, we craft a correlation heatmap to evaluate our feature’s relationship with our predicted output. We use

this heatmap to understand which primary features that overlap in our data set. We eliminate any feature whose
correlation with our final price is a scored value less than .25. Scores less than .25 are indicative of low predictabil-
ity in our model. We also eliminate values that seem to correlate highly with other features but with less feature
importance to our final output. Our final feature set can be reviewed in the heatmap shown in Figure 13.
(a) Original Feature Set
 (b) Final Feature Set
Figure 13. Correlation Heatmap for Feature Reduction
After feature reduction, our final selected domain and non-domain features are represented in Table 2 with a brief
description of each attribute.
4.5 Classification
With our data cleansed, normalized, standardized, and all our features selected we use this data as the input to
our model. With one hot encoding our features after feature reduction total 71 inputs to our model. We utilize
Scikit-learn14, an open-source machine learning package, and Python to test our classification
4.5.1 Neural Network Model
For our first artificial neural network model, we use a fully connected artificial neural network with two hidden lay-
ers. In our first hidden layer, using the third rule of thumb where are neurons are less than twice the size of our
features for input. We utilize 100 nodes in our first hidden layer. For our second hidden layer, we use our first
rule of thumb and select a number between our first hidden layer and the number of outputs in our output layer.
Since we are reviewing price as an indication of the plan, we have only one output in our model. Our second hid-
den layer contains 50 nodes.
14https://www.openhub.net/p/scikit-learn

Table 2. Domain and non-domain based final selected features after feature reduction
Activation and Loss Functions. We utilize ReLu, or rectified linear activation function, as our activation function
for our first ANN model. This linear function outputs a zero if the result is negative, else if the result is positive it
passes the input it received as the input into the next layer. We also test a logistic sigmoid function.
Evaluation of Hyper Parameters. To understand the right hyperparameters, epochs, and batch sizes in particu-
lar we should use to train our model, we test several permutations. We use batch sizes of 16, 32, 64, and 96, and
epoch sizes of 25, 50, 100, 120. We graph our output (Figure: 14) and see that our model performs best near a
batch size of 96 and epochs between 100-120. Based on this we select a batch size of 96 and epochs of 120 to train
our model.
Figure 14. Evaluating Hyper Parameters
4.5.2 Evaluating other Machine Learning Models for Classification
We compare the output of our model to several different machine learning models and contrast their performance
to our artificial neural network (ANN). In particular, we review Random Forest Classification, Stochastic Gradient

Descent, Gaussian Naive Bayes, and Support Vector Machines against our ANN model. We find Support Vector
Machines to be inefficient for the size of our data set, taking too long to compute. However, amongst the other
three models, we find Random Forest to be superior to our ANN model. To understand how our feature reduction
compares (Figure: 15a) to our full feature set (Figure: 15b) with regards to impact on our model, we re-implement
our Neural Network with all features. We also implement all features in our three comparison models as well.
(a) Reduced Feature Set
 (b) Full Feature Set
Figure 15. Select Feature and Full Feature Comparison.
We find that our model performs with no significant difference between the full set of features, vs the reduced set
of features. We also find that, compared to Random Forest Classification, our Neural network does not perform as
well across all three evaluation metrics.
4.5.3 Refining our Neural Network Architecture
Since our neural network model performed sub-optimally compared to our Random Forest Model, we look to im-
prove our neural network architecture. Our initial implementation utilizes the Scikit package, which has limita-
tions in designing an optimal neural network. We re-implement our neural network with TensorFlow. TensorFlow
provides more control over the neural network architecture and allows us to tune the following parameters accord-
ingly:
Loss Function. As our model only contains one output and that output is a corresponding value, rather than a
pre-defined label, we select mean absolute error for our loss function over the log loss function that is intrinsically
used within the Scikit library. Mean absolute error measures the variance in the distance between our predicted
output in our model and the actual values in our test data set.
Varying Activation Functions within our Layers. We define an activation function for each hidden layer, vs a single
activation function for all layers. We test different configurations of activation functions in each layer of our model.
Our final model uses a different activation function at each layer. In between our input layer and our first hidden
layer, we use a Relu activation function; in between our first hidden layer and our second hidden layer, we use a

ANN Model Parameter Comparison
ANN Parameter Original Model
(Scikit)
Final Model (Tensorflow)
Loss Function Log Loss MAE (Mean Absolute
Error)
Drop Out Rate 0.0% 25.0%
Layer 1 Activation Function Relu Relu
Layer 2 Activation Function Relu Tanh
Output Layer Activation Function Relu Sigmoid
Table 3. Refining our Model Architecture.
Tanh activation function; and in between our second hidden layer and our output layer, we use a Sigmoid function.
Utilizing Dropout for a More Precise Fit. Lastly to prevent overfitting our data, and to ensure our model more
randomly fits our validation and test data, we implement a dropout layer of 25% at each hidden layer.
Figure 16. Final Model Improvements Pseudocode

Final Results for our Refined Neural Network Architecture. In our review, our revised architecture and final ANN
model constructed with Tensorflow outperformed both original ANN models with either select features or the full
set of features. Our final ANN model also performed comparably with either the select features or the full set of
features. Review Table 4. This leads us to believe that a well-architected ANN model may be superior in perfor-
mance and accuracy when compared to a restricted parameter and simple ANN model, and the ability to optimize
computationally with only a select set of features did not negatively impact the results of the model in this partic-
ular case.
ANN Model Performance Comparison
Features ANN Model Accuracy F1 Score Precision Recall
Select
Features
ANN Original Model 0.8042 0.4853 0.8305 0.5905
ANN Final Model 0.9506 0.9182 0.9394 0.9013
Full
Features
ANN Original Model 0.7948 0.5470 0.7845 0.5511
ANN Final Model 0.9443 0.9058 0.9278 0.8958
Table 4. Comparing Neural Network Architecture and Accuracy
4.6 Discussion
The Effectiveness of Socioeconomic and Culturally Aware Features in Recommender Systems in Media Subscrip-
tion Services. In this chapter, we reviewed the effectiveness of socioeconomic and culturally aware features with
domain data to predict consumer preferences in price. This allowed us to understand the potential positive im-
pact of socioeconomic and cultural features in use in recommender systems. In our motivating scenario, we found
these features to positively impact price prediction with relative accuracy. We can extrapolate that predicting a
consumer-initiated product movement is possible, such as a consumer either down-selecting or up-selecting a sub-
scription service.
This provides the potential for anticipating consumer movement in products, thus a company can possess a deeper
understanding of each customer. Anticipating an existing consumer’s movement and preference allows for the de-
velopment of preemptive custom interstitials that align with a consumer preference, therefore deepening the re-
lationship between the customer and the company lending to better retention. For new customers, an enhanced
design of a user experience can guide a user to a product selection that best anticipates their preference.
Generalizability in Markets beyond Media Subscription. The result of incorporating socioeconomic and cultural
indices differentiate consumer from country to country and could allow businesses to suggest consumer changes as
a way of retention when major socio-economic shifts occur either locally or globally. It also seems plausible that a
socio-economic and culturally aware recommender system could be used beyond determining subscription service
preferences in the media industry, but apply to any subscription-based services, and more importantly be applied
to any product pricing and price changes in other global industries where regional pricing may play a part. We
conclude that a generalized model with socio-economic and cultural awareness of various different regions could
be used to further personalize recommender systems where product pricing recommendations are made unique for
various regional markets.
Modeling Efficiency in Socio-economic and Culturally Aware Recommender Systems. Scientifically, and in terms of
efficiently and effectively predicting consumer behavior in terms of price and plan selection with domain data, cul-
tural indices, and socio-economic factors with a reasonable size data set, and minimal categorical data, we found
that the most effective machine learning model was a well-architected artificial neural network model with select

features (Figure: 5. With this we conclude two specific thoughts with regard to recommender systems with simi-
lar data: 1) A well-architected neural network model with tested parameters may outperform traditional machine
learning models where conditions are correct and computational limits are not imposed (e.g. GPU is available), 2)
Random Forest machine learning models provide a reasonably efficient model with minimal tuning but may have
a trade-off between precision and recall. We also learned that, with a well-architected neural network model, the
feature set could be reduced, providing computational efficiency with similar accuracy.
Final Select Feature ML Model Performance Comparison
Model Accuracy F1 Score Precision Recall
Stochastic Gradient Descent 0.7666 0.4106 0.8994 0.4719
Gaussian Naive Bayes 0.7416 0.5046 0.8994 0.5489
Random Forest 0.8984 0.7146 0.8994 0.6781
ANN Final (Tensor Flow) 0.9506 0.9182 0.9394 0.9013
Table 5. Final ANN Model Performance Compared with other ML Models
5 CONCLUSION AND FUTURE WORK
5.1 Concluding Remarks
With the consistent progression of more and more information and the limitations of human capability, methods
of more accurately understanding a customer’s preference are essential. Recommender systems are necessary to
understand a customer’s preference by automating processes that extract, sort, filter, and process information.
Competition in the streaming media industry is gaining momentum. Globalization is a key to subscriber growth
but adds complexities to differences and preferences in customers across varying regions. Customer preferences in
different regions are impacted by environmental factors, such as those that are reflected in socio-economic and cul-
tural norms. Therefore, incorporating socio-economic and cultural indicators as context to improve the accuracy of
recommender systems is necessary.
In our research, we explored the predictability of socio-economic and cultural factors on a customer’s preference
in plan selection. We did this by predicting the price users in a particular country were willing to pay. We per-
formed feature selection, fusing domain data and our socio-economic and cultural factors associated with the coun-
tries represented by our user base. We found that a well-architected artificial neural network with select cultural,
and socio-economic features could predict the price customers were likely to want to pay with, with an accuracy
of 95%, a precision of 94%, an F1 Score of 92%, and a Recall of 90%. It also performed more superior to other
types of the other classification models we chose to experiment with, Random Forest, Gaussian Naive Bayes, and
stochachastic gradient descent. Our well-architected ANN model uplifted our metrics across all evaluation dimen-
sions by a minimum of 6% in accuracy, 4% in precision, 23% in recall, and 20% in F1, and did so with even greater
consistency and balance (e.g. there is no notably significant trade-off between Precision and Recall).
Therefore, the plan a consumer might select after an involuntary price change occurred is highly predictable, and
this prediction could assist in the longer-term retention of customers by enabling a proactive recommendation to a
customer whose intent is to leave the service.
5.2 Limitations
After the completion of our experiment, the research in this paper may present some limitations that in implemen-
tation could lead to varied results.

Limitations in Sample Data. We selected data from countries that we were able to more completely represent in
our domain and non-domain data. However, certain geographical regions are absent, e.g., Africa, North Africa,
Southeast Asia, and the Middle East. These regions may have more significant shifts in cultural and socioeconomic
data, leading to potentially different features weighting in our model.
Training and Test Data Size. In order to narrow the size of our training and test data to match computational ef-
ficiency on a 32-core processor and 60gigabyte memory server, we narrowed the scope of our data. The scope was
reduced to only those individuals who may react to involuntary price changes. In future research, we would run
additional experiments across different profiles of users, not limited to only those that reacted to involuntary price
changes. We may also correspondingly increase computing in order to increase computation efficiency and shorter
durations for experiments.
5.3 Future Work
There are different areas that we can propose to expand and improve on our research. Below are the main domains
that we could explore in future works:
5.3.1 Temporal Drifts and Customer Behaviour
In the context of temporal drifts and customer behavior, a promising avenue for future research involves examining
the impact of socio-economic shifts on customer preferences. While cultural indicators tend to remain relatively
stable over time, socio-economic conditions exhibit temporal variations that can influence changes in customer
preferences. Understanding customer behavior in relation to these socio-economic shifts offers several potential
benefits, including more proactive pricing and plan selection, improved retention and subscriber growth forecast-
ing models, and the creation of more accurate pricing models per region.
To advance this field, future studies can focus on analyzing customer behavior patterns in conjunction with socio-
economic shifts over time. By examining historical data and tracking changes in socio-economic indicators, such as
income levels, employment rates, or inflation rates, it becomes possible to identify correlations between these shifts
and changes in customer preferences.
Once the relationship between socio-economic shifts and customer behavior is established, future work can explore
the integration of this knowledge into pricing and plan selection strategies. By proactively adapting pricing and
plan offerings to align with anticipated customer preferences in response to socio-economic shifts, companies can
enhance customer satisfaction and increase the likelihood of customer retention.
Furthermore, the understanding of customer behavior in relation to socio-economic shifts can also contribute to
the development of more accurate forecasting models for retention and subscriber growth. By incorporating the
temporal dynamics of socio-economic conditions, these models can provide better insights into future customer be-
havior and enable more precise predictions of customer retention and subscriber growth rates.
5.3.2 Proactive Prediction of User’s Intent to Initiate Change
In the pursuit of sustainable growth through customer retention, an intriguing avenue for future research lies in
exploring the similarity between customer behaviors and proactively designed interstitials. This approach aims to
predict a user’s intent to initiate change and recommend relevant suggestions even before the user explicitly re-
quests action. To advance this field, future studies can focus on analyzing user behaviors and identifying patterns

that indicate an intent to initiate change. By examining various aspects of user interactions, such as browsing his-
tory, purchase patterns, or engagement metrics, it may be possible to identify behavioral signals that precede a
user’s desire for change. Once these behavioral patterns are established, the next step involves designing intersti-
tials that proactively suggest relevant recommendations to users. These interstitials, strategically placed within the
user experience, can provide tailored suggestions or options that align with the anticipated change in user prefer-
ences or needs. Also, advanced entity recognition and sentence ranking improve recommender systems’ accuracy
and help predict user intent, leading to more timely and relevant content suggestions85.
An essential aspect of this research would be to develop robust algorithms and methodologies that accurately pre-
dict user intent based on behavioral similarity. This may involve employing machine learning techniques, such as
clustering or classification algorithms, to identify users exhibiting similar behavioural patterns. By leveraging these
patterns, proactive predictions can be made regarding the users’ intentions to initiate change. Explainable AI can
also enhance recommender systems by providing transparent, understandable reasons for suggestions, thereby in-
creasing user trust, improving personalization, and aiding in regulatory compliance and system optimization30, 31.
Reinforcement learning can also enhance recommender systems by continuously learning from user interactions
to make increasingly personalized and effective recommendations, thereby improving user engagement and satis-
faction 76. Another future line of work, can enhance deep reinforcement learning guided graph neural networks to
revolutionize recommender systems by leveraging complex user-item interaction patterns and continuously learning
from user feedback, leading to more sophisticated, adaptive, and effective recommendations86.
5.3.3 Expanding Non-Domain Data
Our research had fewer socioeconomic factors and did not describe any social media trends within those regions
that may present relevant factors in media plan selection preferences. By extracting features in social media trends
as additional socio-economic factors, we may be able to react more proactively and recommend plans to new users.
This may, therefore, positively impact subscriber growth in a media subscription-based company.
To advance this field, future studies can focus on identifying and extracting features from social media trends that
are indicative of socioeconomic factors. By analyzing user-generated content, engagement patterns, and emerging
topics on social media platforms, relevant insights can be gained regarding the preferences and behaviours of po-
tential subscribers. These insights can then be incorporated as additional socioeconomic factors in the media plan
selection process.
By expanding the range of socioeconomic factors considered, media subscription-based companies can make more
informed and tailored recommendations to new users. This proactive approach enables the delivery of personal-
ized plans that align with individual preferences and expectations29. By incorporating social media trends, which
often reflect evolving societal interests and cultural shifts, the recommendations can stay abreast of the latest de-
velopments and ensure relevance to users’ evolving preferences. Equity and regulation, however, may impact how
personalized a model could be designed, and would need further review and investigation.
5.3.4 Vector Based User Distances and Graphs
In the domain of cultural and socio-economic data analysis, an intriguing direction for future research lies in har-
nessing the potential of vector-based representations and graph-based data stores to differentiate sub-areas within
this data. This approach offers the opportunity to gain valuable insights into the distances and similarities be-
tween regions, ultimately leading to enhanced planning, price assignments, and recommendations across countries.

To advance this research direction, future studies can focus on designing data representations that capture the dis-
tinct sub-areas within cultural and socio-economic data. Each sub-area can be transformed into a separate vector
representation, encapsulating the unique characteristics and attributes of that region. By employing appropriate
feature extraction and vectorization techniques, the data can be effectively transformed into a format conducive to
analysis and comparison.
Once the vectors representing different sub-areas are obtained, future work can explore the utilization of graph-
based data stores for organizing and querying these vectors. Graph databases enable efficient storage and retrieval
of complex interconnected data, allowing for flexible querying and analysis of relationships between the vectors.
Constructing a queryable graph-based data store incorporating the vectors can facilitate the identification of simi-
larities and distances between regions, thereby informing the development of enhanced recommendations and pric-
ing strategies.
5.3.5 Transfer Learning
In the realm of recommender systems, an exciting avenue for future exploration lies in leveraging transfer learning
techniques to enhance the incorporation of cultural and socio-economic data as contextual information. Specifi-
cally, this research direction holds promise in refining viewing recommendations in media selection domains, such
as TV series, by aligning socio-economic and cultural indicators with individual users.
To advance this field, future studies can investigate the effectiveness of transfer learning approaches in capturing
and transferring knowledge from diverse datasets containing socio-economic and cultural information. By lever-
aging pre-trained models or knowledge learned from similar domains, recommender systems can benefit from the
transfer of relevant information to enhance their understanding of user preferences.
One potential avenue is to explore domain adaptation techniques in transfer learning, whereby models trained
on a source domain, such as a dataset containing socio-economic and cultural indicators, are adapted to a target
domain, such as a TV series recommendation dataset. This would enable the recommender system to effectively
incorporate cultural and socio-economic context specific to each user, leading to more accurate and personalized
viewing recommendations.
REFERENCES
1. Linear vs. Streaming: What’s Your Strategy?, Aug. 2021. [Online; accessed 3. Sep. 2022].
2. Netflix Is Now Available Around the World - About Netflix, Sept. 2022. [Online; accessed 3. Sep. 2022].
3. G. Adomavicius, R. Sankaranarayanan, S. Sen, and A. Tuzhilin. Incorporating contextual information in rec-
ommender systems using a multidimensional approach. ACM transactions on information systems, 23(1):103–
145, 2005.
4. C. C. Aggarwal. Content-Based Recommender Systems, pages 139–166. Springer International Publishing,
Cham, 2016.
5. J. H. Alan Colman, Mahmoud Hussein and M. Kapuruge. Context aware and adaptive systems. Context in
Computing, 2014.
6. M. C. Barukh, S. Zamanirad, M. Baez, A. Beheshti, B. Benatallah, F. Casati, L. Yao, Q. Z. Sheng, and
F. Schiliro. Cognitive augmentation in processes. Next-Gen Digital Services. A Retrospective and Roadmap
for Service Computing of the Future: Essays Dedicated to Michael Papazoglou on the Occasion of His 65th
Birthday and His Retirement, pages 123–137, 2021.
7. A. Beheshti. Knowledge base 4.0: Using crowdsourcing services for mimicking the knowledge of domain ex-
perts. In 2022 IEEE International Conference on Web Services (ICWS), pages 425–427. IEEE, 2022.

8. A. Beheshti. Empowering generative ai with knowledge base 4.0: Towards linking analytical, cognitive, and
generative intelligence. In 2023 IEEE International Conference on Web Services (ICWS), pages 763–771. IEEE,
2023.
9. A. Beheshti, B. Benatallah, R. Nouri, V. M. Chhieng, H. Xiong, and X. Zhao. Coredb: a data lake service. In
Proceedings of the 2017 ACM on Conference on Information and Knowledge Management, pages 2451–2454,
2017.
10. A. Beheshti, B. Benatallah, R. Nouri, and A. Tabebordbar. Corekg: a knowledge lake service. Proceedings of
the VLDB Endowment, 11(12):1942–1945, 2018.
11. A. Beheshti, B. Benatallah, A. Tabebordbar, H. R. Motahari-Nezhad, M. C. Barukh, and R. Nouri. DataSy-
napse: A social data curation foundry. 37(3):351–384, 2018.
12. A. Beheshti, V. Moraveji-Hashemi, S. Yakhchi, H. R. Motahari-Nezhad, S. M. Ghafari, and J. Yang. person-
ality2vec: Enabling the analysis of behavioral disorders in social networks. In Proceedings of the 13th interna-
tional conference on web search and data mining, pages 825–828, 2020.
13. A. Beheshti, S. Yakhchi, S. Mousaeirad, S. M. Ghafari, S. R. Goluguri, and M. A. Edrisi. Towards cognitive
recommender systems. Algorithms, 13(8):176, 2020.
14. A. Beheshti, J. Yang, Q. Z. Sheng, B. Benatallah, F. Casati, S. Dustdar, H. R. M. Nezhad, X. Zhang, and
S. Xue. Processgpt: Transforming business process management with generative artificial intelligence. arXiv
preprint arXiv:2306.01771, 2023.
15. S.-M.-R. Beheshti, B. Benatallah, S. Sakr, D. Grigori, H. R. Motahari-Nezhad, M. C. Barukh, A. Gater, and
S. H. Ryu. Business process paradigms. Process analytics: Concepts and techniques for querying and analyzing
process data, pages 19–60, 2016.
16. I. Ben Sassi, S. Mellouli, and S. Ben Yahia. Context-aware recommender systems in mobile environment: On
the road of future research. Information Systems, 72:27–61, 2017.
17. R. N. Bolton and M. B. Myers. Price-based global market segmentation for services. Journal of marketing,
67(3):108–128, 2003.
18. P. Bourdieu. Distinction: A social critique of the judgement of taste. Routledge, 2013.
19. M. Braunhofer, M. Kaminskas, and F. Ricci. Recommending music for places of interest in a mobile travel
guide. In Proceedings of the Fifth ACM Conference on Recommender Systems, RecSys ’11, page 253–256, New
York, NY, USA, 2011. Association for Computing Machinery.
20. S. Buyrukoğlu and A. Akbaş. Machine learning based early prediction of type 2 diabetes: A new hybrid fea-
ture selection approach using correlation matrix with heatmap and sfs. Balkan Journal of Electrical and Com-
puter Engineering, 10(2):110 – 117, 2022.
21. D. V. Caprar, T. M. Devinney, B. L. Kirkman, and P. Caligiuri. Conceptualizing and measuring culture in in-
ternational business and management: From challenges to potential solutions. Journal of international business
studies, 46(9):1011–1027, 2015.
22. K. Chaudhari and A. Thakkar. A comprehensive survey on travel recommender systems. Archives of computa-
tional methods in engineering, 27(5):1545–1571, 2020.
23. L. Chen and P. Pu. Experiments on user experiences with recommender interfaces. Behaviour and information
technology, 33(4):372–394, 2014.
24. J. Choi, H. J. Lee, F. Sajjad, and H. Lee. The influence of national culture on the attitude towards mobile
recommender systems. Technological forecasting and social change, 86(-):65–79, 2014.
25. W.-T. Chu and W.-H. Huang. Cultural difference and visual information on hotel rating prediction. World
wide web (Bussum), 20(4):595–619, 2017.
26. S. K. Dey, A. Hossain, and M. M. Rahman. Implementation of a web application to predict diabetes disease:
An approach using machine learning algorithm. In 2018 21st International Conference of Computer and Infor-
mation Technology (ICCIT), pages 1–5, 2018.

27. K. Djordjevic, M. Jordovic Pavlovic, Z. Cojbasic, S. Galovic, M. Popovic, M. Nesic, and D. Markushev. Influ-
ence of data scaling and normalization on overall neural network performances in photoacoustics. Optical and
Quantum Electronics, 54, 08 2022.
28. M. Elahi, A. Beheshti, and S. R. Goluguri. Recommender systems: Challenges and opportunities in the age of
big data and artificial intelligence. Data Science and Its Applications, pages 15–39, 2021.
29. S. Ghodratnama, A. Behehsti, and M. Zakershahrak. A personalized reinforcement learning summarization
service for learning structure from unstructured data. In 2023 IEEE International Conference on Web Services
(ICWS), pages 206–213. IEEE, 2023.
30. A. Hanif, A. Beheshti, B. Benatallah, X. Zhang, Habiba, E. Foo, N. Shabani, and M. Shahabikargar. A com-
prehensive survey of explainable artificial intelligence (xai) methods: Exploring transparency and interpretabil-
ity. In International Conference on Web Information Systems Engineering, pages 915–925. Springer, 2023.
31. A. Hanif, A. Beheshti, B. Benatallah, X. Zhang, and S. Wood. Evidence based pipeline for explaining artifi-
cial intelligence algorithms with interactions. In 2022 IEEE 9th International Conference on Data Science and
Advanced Analytics (DSAA), pages 1–9. IEEE, 2022.
32. K. Haruna, M. Akmar Ismail, S. Suhendroyono, D. Damiasih, A. C. Pierewan, H. Chiroma, and T. Herawan.
Context-aware recommender system: A review of recent developmental process and future research direction.
Applied Sciences, 7(12), 2017.
33. K. He, S. Meng, Q. Li, X. Liu, A. Beheshti, X. Chi, and X. Zhang. Noise-augmented contrastive learning for
sequential recommendation. In International Conference on Web Information Systems Engineering, pages 559–
568. Springer, 2023.
34. J. Heaton. Artificial Intelligence for Humans, volume 3: Deep Learning and Neural Networks. CreateSpace
Independent Publishing Platform, 2015.
35. G. Hofstede. Dimensionalizing cultures: The hofstede model in context. Online Readings in Psychology and
Culture, 2(1), 2011.
36. M. Hong, S. An, R. Akerkar, D. Camacho, and J. J. Jung. Cross-cultural contextualisation for recommender
systems. Journal of Ambient Intelligence and Humanized Computing, 2019.
37. M. Hooijberg. Forward long line - vincenty’s method. In Geometrical Geodesy. Springer Berlin / Heidelberg,
Germany, 2007.
38. L. Huang, M. Fu, F. Li, H. Qu, Y. Liu, and W. Chen. A deep reinforcement learning based long-term recom-
mender system. Knowledge-based systems, 213:106706–, 2021.
39. H. Jabbar and R. Z. Khan. Methods to avoid over-fitting and under-fitting in supervised machine learning
(comparative study). Computer Science, Communication and Instrumentation Devices, 70:163–172, 2015.
40. A. Jalayer, M. Kahani, A. Pourmasoumi, and A. Beheshti. Ham-net: Predictive business process monitoring
with a hierarchical attention mechanism. Knowledge-Based Systems, 236:107722, 2022.
41. D. Jannach, P. Resnick, A. Tuzhilin, and M. Zanker. Recommender systems — beyond matrix completion.
Commun. ACM, 59(11):94–102, oct 2016.
42. N. Jones. The learning machines. Computer science: The learning machines, 505(7482):146–148„ 2014.
43. H. J. Jun, J. H. Kim, D. Y. Rhee, and S. W. Chang. "seoulhouse2vec": An embedding-based collaborative
filtering housing recommender system for analyzing housing preference. Sustainability (Basel, Switzerland),
12(17):6964–, 2020.
44. K. Kalinowski, A. Kozłowska, M. Malesza, and D. P. Danel. Evolutionary origins of music. classical and recent
hypotheses. Anthropological review (Poznań, Poland), 84(2):213–231, 2021.
45. M. Kaminskas and F. Ricci. Contextual music information retrieval and recommendation: State of the art and
challenges. Computer Science Review, 6(2):89–119, 2012.
46. B. Karlik and A. Vehbi. Performance analysis of various activation functions in generalized mlp architec-
tures of neural networks. International Journal of Artificial Intelligence and Expert Systems (IJAE), 1(4):pp.
111–122, 2011.

47. S. Khadivizand, A. Beheshti, F. Sobhanmanesh, Q. Z. Sheng, E. Istanbouli, S. Wood, and D. Pezaro. Towards
intelligent feature engineering for risk-based customer segmentation in banking. In Proceedings of the 18th
International Conference on Advances in Mobile Computing & Multimedia, pages 74–83, 2020.
48. D. P. Kingma and J. Ba. Adam: A method for stochastic optimization. In 3rd International Conference for
Learning Representations, 2017.
49. N. Koenigstein, G. Dror, and Y. Koren. Yahoo! music recommendations: modeling music ratings with tem-
poral dynamics and item taxonomy. In Proceedings of the fifth ACM conference on recommender systems,
RecSys ’11, pages 165–172. ACM, 2011.
50. Y. Koren. Collaborative filtering with temporal dynamics. In Proceedings of the 15th ACM SIGKDD interna-
tional conference on knowledge discovery and data mining, KDD ’09, pages 447–456. ACM, 2019.
51. K. L. Kraemer, J. Gibbs, and J. Dedrick. Impacts of globalization on e-commerce use and firm performance: A
cross-country investigation. The Information Society, 21(5):323–340, 2005.
52. H. J. Kweon and S. H. Kweon. Pricing strategy within the u.s. streaming services market: A focus on netflix’s
price plans. International journal of contents, 17(2):1–8, 2021.
53. Q. Li, J. Li, J. Sheng, S. Cui, J. Wu, Y. Hei, H. Peng, S. Guo, L. Wang, A. Beheshti, et al. A survey on deep
learning event extraction: Approaches and applications. IEEE Transactions on Neural Networks and Learning
Systems, 2022.
54. Q. Li, H. Peng, J. Li, Y. Hei, R. Sun, J. Sheng, S. Guo, L. Wang, J. Wu, A. Beheshti, et al. A comprehensive
survey on schema-based event extraction with deep learning. arXiv preprint arXiv:2107.02126, 2021.
55. J. Liang. Confusion matrix: Machine learning. POGIL Activity Clearinghouse, 3(4), Dec. 2022.
56. F. Liu, X. Ma, J. Wu, J. Yang, S. Xue, A. Beheshti, C. Zhou, H. Peng, Q. Z. Sheng, and C. C. Aggarwal. Da-
gad: Data augmentation for graph anomaly detection. In 2022 IEEE International Conference on Data Mining
(ICDM), pages 259–268. IEEE, 2022.
57. M. Liu, X. Hu, and M. Schedl. The relation of culture, socio-economics, and friendship to music preferences: A
large-scale, cross-country study. PloS one, 13(12):e0208186–e0208186, 2018.
58. S. Moradizeyveh. Intent recognition in conversational recommender systems. arXiv preprint arXiv:2212.03721,
2022.
59. C. Nwankpa, W. Ijomah, A. Gachagan, and S. Marshall. Activation functions: Comparison of trends in prac-
tice and research for deep learning. arXiv preprint arXiv:1811.03378, 2018.
60. A. J. G. Patrick Brezillon. Preface by the editors. Context in Computing, 2014.
61. P. Pirolli and S. Card. The sensemaking process and leverage points for analyst technology as identified
through cognitive task analysis. In Proceedings of international conference on intelligence analysis, volume 5,
pages 2–4. McLean, VA, USA, 2005.
62. K. H. Z. S. Ren; and J. Sun. Delving deep into rectifiers: Surpassing human-level performance on imagenet
classification. arXiv, 2015.
63. F. Ricci. Recommender Systems Handbook. Springer, New York, NY, 3rd ed. edition, 2022.
64. R. L. Rosa, G. M. Schwartz, W. V. Ruggiero, and D. Z. Rodriguez. A knowledge-based recommendation
system that includes sentiment analysis and deep learning. IEEE transactions on industrial informatics,
15(4):2124–2135, 2019.
65. Z. Rouhollahi, A. Beheshti, S. Mousaeirad, and S. R. Goluguri. Towards proactive financial crime and fraud
detectionthrough artificial intelligence and regtech technologies. In The 23rd International Conference on Infor-
mation Integration and Web Intelligence, pages 538–546, 2021.
66. M. Schedl, C. Bauer, W. Reisinger, D. Kowald, and E. Lex. Listener modeling and context-aware music recom-
mendation based on country archetypes. Frontiers in Artificial Intelligence, 3, 2021.
67. C. Scheel, A. Castellanos, T. Lee, and E. W. De Luca. The reason why: A survey of explanations for recom-
mender systems. In Adaptive Multimedia Retrieval: Semantics, Context, and Adaptation, volume 8382 of Lec-
ture Notes in Computer Science, pages 67–84, Cham, 2014. Springer International Publishing.

68. F. Schiliro, N. Moustafa, I. Razzak, and A. Beheshti. Deepcog: A trustworthy deep learning-based human
cognitive privacy framework in industrial policing. IEEE Transactions on Intelligent Transportation Systems,
2022.
69. N. Shabani, A. Beheshti, H. Farhood, M. Bower, M. Garrett, and H. Alinejad-Rokny. A rule-based approach
for mining creative thinking patterns from big educational data. AppliedMath, 3(1):243–267, 2023.
70. N. Shabani, J. Wu, A. Beheshti, J. Foo, A. Hanif, and M. Shahabikargar. A survey on graph neural networks
for graph summarization. arXiv preprint arXiv:2302.06114, 2023.
71. Y. Shi, M. Larson, and A. Hanjalic. Collaborative filtering beyond the user-item matrix: A survey of the state
of the art and future challenges. ACM Comput. Surv., 47(1), may 2014.
72. F. Sobhanmanesh, A. Beheshti, N. Nouri, N. M. Chapparo, S. Raj, and R. A. George. A cognitive model for
technology adoption. Algorithms, 16(3):155, 2023.
73. N. G. Society. Globalization.
74. N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov. Dropout: A simple way to pre-
vent neural networks fromoverfitting. Journal of Machine Learning, 15:1929, 2014.
75. A. Tabebordbar, A. Beheshti, and B. Benatallah. ConceptMap: A conceptual approach for formulating user
preferences in large information spaces. In Web Information Systems Engineering – WISE 2019, Lecture Notes
in Computer Science, pages 779–794. Springer International Publishing, 2019.
76. A. Taheri, K. RahimiZadeh, A. Beheshti, J. Baumbach, R. V. Rao, S. Mirjalili, and A. H. Gandomi. Par-
tial reinforcement optimizer: An evolutionary optimization algorithm. Expert Systems with Applications,
238:122070, 2024.
77. F. Trompenaars and C. Hampden-Turner. Riding the waves of culture: Understanding diversity in global busi-
ness. McGraw Hill, 1998.
78. S. Wang, A. Beheshti, Y. Wang, J. Lu, Q. Z. Sheng, S. Elbourn, and H. Alinejad-Rokny. Learning distributed
representations and deep embedded clustering of texts. Algorithms, 16(3):158, 2023.
79. S. Yakhchi. Learning complex users’ preferences for recommender systems. arXiv preprint arXiv:2107.01529,
2021.
80. S. Yakhchi, A. Behehsti, S.-m. Ghafari, I. Razzak, M. Orgun, and M. Elahi. A convolutional attention network
for unifying general and sequential recommenders. Information Processing & Management, 59(1):102755, 2022.
81. S. Yakhchi, A. Beheshti, S.-M. Ghafari, M. A. Orgun, and G. Liu. Towards a deep attention-based sequential
recommender system. IEEE Access, 8:178073–178084, 2020.
82. X. Ying. An overview of overfitting and its solutions. Journal of Physics: Conference Series, 1168(2):022022,
feb 2019.
83. F. Zafari, I. Moser, and T. Baarslag. Modelling and analysis of temporal preference drifts using a component-
based factorised latent approach. Expert systems with applications, 116:186–208, 2019.
84. E. Zangerle, M. Pichl, and M. Schedl. Culture-aware music recommendation. In Proceedings of the 26th Con-
ference on user modeling, adaptation and personalization, UMAP ’18, pages 357–358. ACM, 2018.
85. G. Zhang, X. Zhang, Z. Wang, and A. Beheshti. Multi-granularity entity recognition based sentence ranking
for multi-document summarization. In 2023 IEEE 10th International Conference on Data Science and Ad-
vanced Analytics (DSAA), pages 1–10. IEEE, 2023.
86. X. Zhao, J. Wu, H. Peng, A. Beheshti, J. J. Monaghan, D. McAlpine, H. Hernandez-Perez, M. Dras, Q. Dai,
Y. Li, et al. Deep reinforcement learning guided graph neural networks for brain network analysis. Neural
Networks, 154:56–67, 2022.
87. Y. M. R. A. A. Zmily. User-centered approaches to context awareness: Prospects and challenges. Context in
Computing, 2014.
