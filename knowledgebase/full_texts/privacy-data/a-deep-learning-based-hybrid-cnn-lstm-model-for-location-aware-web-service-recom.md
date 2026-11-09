---
title: A Deep Learning-Based Hybrid CNN-LSTM Model for Location-Aware Web Service Recommendation
url: https://doi.org/10.1007/s11063-024-11687-w
category: privacy-data
subcategory: empirical
date: 2024-09
venue: Neural Processing Letters
authors:
- Ankur Pandey
- Praveen Kumar Mannepalli
- Manish Kumar Gupta
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s11063-024-11687-w.pdf
pages: 25
chars: 66461
fetched_at: '2026-11-08T16:55:05+00:00'
kb_version: 1
---

# A Deep Learning-Based Hybrid CNN-LSTM Model for Location-Aware Web Service Recommendation

Neural Processing Letters (2024) 56:234
https://doi.org/10.1007/s11063-024-11687-w
A Deep Learning-Based Hybrid CNN-LSTM Model for
Location-Aware Web Service Recommendation
Ankur Pandey 1 · Praveen Kumar Mannepalli 2 · Manish Gupta 3 · Ramraj Dangi 4 ·
Gaurav Choudhary 5
Accepted: 22 August 2024 / Published online: 16 September 2024
© The Author(s) 2024
Abstract
Advertising is the most crucial part of all social networking sites. The phenomenal rise of
social media has resulted in a general increase in the availability of customer tastes and
preferences, which is a positive development. This information may be used to improve the
service that is offered to users as well as target advertisements for customers who already
utilize the service. It is essential while delivering relevant advertisements to consumers,
to take into account the geographic location of the consumers. Customers will be ecstatic
if the offerings displayed to them are merely available in their immediate vicinity. As the
user’s requirements will vary from place to place, location-based services are necessary
for gathering this essential data. To get users to stop thinking about where they are and
instead focus on an ad, location-based advertising (LBA) uses their mobile device’s GPS to
pinpoint nearby businesses and provide useful information. Due to the increased two-way
communication between the marketer and the user, mobile consumers’ privacy concerns
and personalization issues are becoming more of a barrier. In this research, we developed
a collaborative ﬁltering-based hybrid CNN-LSTM model for recommending geographically
relevant online services using deep neural networks. The proposed hybrid model is made
using two neural networks, i.e., CNN and LSTM. Geographical information systems (GIS)
are used to acquire initial location data to collect precise locational details. The proposed
B Ramraj Dangi
ramrajdangi@vitbhopal.ac.in
Ankur Pandey
ankur.pandey@jaipur.manipal.edu
Praveen Kumar Mannepalli
praveen.e17513@cumail.in
Manish Gupta
manish.gupta@gla.ac.in
Gaurav Choudhary
gac@mmmi.sdu.dk
1 SCSE, Manipal University Jaipur, Dehmi-Kalan, Jaipur, Rajasthan 303007, India
2 CSE, Chandigarh University, Mohali, India
3 ECE, GLA University, Mathura, Chaumuhan, Mathura, U.P . 281406, India
4 SCSE, VIT Bhopal University, Kothri-Kalan, Sehore, M.P . 466114, India
5 Center for Industrial Software, The Mærsk Mc-Kinney Møller Institute, University of Southern
Denmark, 6400 Sønderborg, Denmark
123

234 Page 2 of 25 A. Pandey et al.
LBA for GIS is built in a Python simulation environment for evaluation. Hybrid CNN-LSTM
recommendation performance beats existing location-aware service recommender systems
in large simulations based on the WS dream dataset.
Keywords Location-based services · Recommendation system · Geographical information
systems · Deep learning · CNN · LSTM
1 Introduction
To advertise an item or service in a particular region, a business may use LBA (location-based
advertising) [1, 2]. The term "location-based advertising," or "LBA" for short, describes a
speciﬁc category of location-based services that make use of geolocation data gathered from
mobile devices like smartphones. LBA might potentially be utilized to hire seasonal or full-
time staff for a neighbourhood company. LBA allows merchants to send location-speciﬁc,
timely communications to consumers. Advertisers may target consumers with various mes-
sages based on their physical location by using their GPS coordinates. Allowing marketers to
contact consumers while they are physically close to their stores has broken down formerly
insurmountable barriers between marketplaces and consumers [ 3].
Recommendation systems (RSS) use a variety of ﬁltering approaches, all of which are
described here. Collaborative ﬁltering is the approach that is most often used. A large num-
ber of online service recommendation systems are being developed based on collaborative
ﬁltering (CF). The analysis of the quality of service-aware web service suggestions and cus-
tomized QoS-aware web service recommendations is discussed in detail [ 4]. Many of the
most common customer-facing tactics are based on user-based or item-based approaches. The
Matrix Factorization (MF) method stands out as one of the most effective approaches [ 5]. It
leverages hidden vector attributes to represent individuals or items, initially mapping them
into a shared latent space [ 6]. While MF has demonstrated considerable success, numerous
adaptations and variations have emerged [7, 8]. However, despite its effectiveness, MF-based
strategies continue to grapple with challenges like cold-start and data sparsity problems [ 9,
10], signiﬁcantly limiting the efﬁcacy of current methodologies.
It is important to include the geographical data that is often a part of the customer database
when clustering the data to generate customer segments, including, in response, selecting
where the channels of distribution need to be positioned. In recent years, geo-marketing has
seen an uptick in the practice of clustering geo-referenced (or spatial) data, although conven-
tional clustering approaches have shown certain limits in light of the industry’s rising need
for precision and consistency [ 11]. To maximize the effectiveness of customized targeting
through the right channels, consumer segmentation must be both precise and homogeneous.
Current Challenges The existing environment of location-based advertising and recom-
mendation systems is fraught with difﬁculties. The commonly used matrix factorization (MF)
technique in recommendation systems encounters data sparsity and cold-start concerns. The
drawbacks of this strategy impede system efﬁciency, particularly when dealing with sparse
data or new user interactions. Furthermore, typical clustering algorithms [ 12, 13] are proven
to have drawbacks in the realms of geo-marketing and clustering geo-referenced data for con-
sumer segmentation. These difﬁculties come as a result of the industry’s increased demand for
precision and consistency, making precise consumer segmentation harder to attain using tra-
ditional clustering methods. Furthermore, analytic methodologies for independent consumer
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 3 of 25 234
data encounter difﬁculties when dealing with vast and complicated geographic datasets,
reducing the depth and accuracy of insights derived from exploratory data analysis.
Proposed Solutions Proposed Solutions: The proposed solutions outlined in this study
aim to address challenges within recommendation systems and geo-marketing by exploring
various methodologies. Firstly, alternatives to Matrix Factorization and strategies to miti-
gate data sparsity and enhance cold-start handling are investigated [14, 15]. Additionally, the
development of hybrid models merging collaborative and content-based ﬁltering or incor-
porating contextual information is suggested for more robust recommendations [ 16–18]. In
the realm of geo-marketing, the study proposes exploring advanced clustering techniques,
potentially integrating machine learning algorithms to manage large geographic datasets
effectively. Furthermore, advocating for the utilization of complex analytic approaches, such
as machine learning models or deep learning methods, to extract meaningful insights from
multidimensional datasets for independent customer data analysis is emphasized. Successful
implementation of these recommended solutions in real-world scenarios would require col-
laboration among data scientists, domain experts, and industry stakeholders. This research
proposes, different deep learning-based approaches that are applied to perform the predic-
tion, and the names of these are the LSTM and CNN, with the employ of these models, a
hybrid model is built to implement this research, and the name of this hybrid model is hybrid
CNN-LSTM model the location-aware web service recommendation.
Customers are independent whenever it comes to exploratory data analysis, even though
most commercially available GIS provides for substantial storage, editing, and display of geo-
referenced data [19]. Due to the extensive size and high complexity of geographic data, as well
as the need for sophisticated data integration and mining tools, this strategy is impractical.
When a dataset has a lot of dimensions, it might be difﬁcult for analytic techniques to work
properly. It is a common issue that not all of the variables will have a signiﬁcant relationship
with one another. Most analyses assume a very basic pattern, which may be adjusted according
to several criteria, and so restrict or compress the ﬁeld of possible hypotheses [ 20]. It is
recommended that the many artiﬁcially enabled location-based services (LBS) in mobile ads
make use of deep learning methods such as long short-term memory (LSTM), convolutional
neural networks (CNN), recurrent neural networks (RNN), and artiﬁcial neural networks
(ANN) [21].
The following article structures the remaining article as follows: The background and
related work on location-based advertising have been discussed in Sect. 2. Section 3 talks
about the proposed work, including location-based advertising and service methods for
an identiﬁed problem. In Sect. 4, we discuss the experimental results of the suggested
approaches and make comparisons to other current methods; in Sect. 5, we conclude and
provide directions for future study.
2 Related Work
Location-based services (LBS) is a broad and evolving ﬁeld that encompasses various tech-
nologies and applications. In this section, we are giving a detailed survey on LBS. Related
research on LBS is presented here.
Tan et al. [ 22] used a partial least squares structural method to analyze advertising on
social media. In addition, an integrated framework based on interaction theory, individual
variables, and the mobile technology acceptance model was used to comprehend customer
preferences. Li and Xu [ 23] proposed a diversity-aware digital ad architecture to adequately
123

234 Page 4 of 25 A. Pandey et al.
meet their clients’ needs (D-AdFeed). The knapsack problem, with several possible solutions,
was used to frame this issue. Both greedy and genetic algorithms were used to ﬁnd a solution.
Goh et al. [ 24] used Logit and Poisson count models to analyse the search patterns and ad
clickthrough rates. By developing a tailored mobile advertising system, Li and Du [ 25]w e r e
able to provide shoppers and businesses with contextually aware advertisements.
Utilising an ensemble-based approach, Haider et al. [26] investigated fraudulent practices
in mobile ads. Consumers’ familiarity with location-based advertising was measured using
the persuasiveness needed for planning by Ryu and Park [ 27]. To examine why customers
make repeat purchases, Lu et al. [ 28] introduced the theory of the planned model. Shin and
Lin [ 29] studied consumer opinions and their propensity to ignore advertisements. Y ang
et al. [ 30] (2013) integrated an advertising model based on technological and emotional
evaluations. Sharma et al. [ 31] used a neural network and partial least squares structure to
increase consumers’ receptivity to mobile marketing.
A c c o r d i n gt o[32] analyse the LBSs’s privacy-preserving strategies. They classify and
provide an in-depth analysis of the current methods. They found the main ideas and most
recent progress in several common works from each group and then analysed them in the
past. For new study possibilities, we also talk about how privacy-preserving methods can
be used in LBSs. This survey, which offers a current and thorough summary of previous
research, may encourage further investigations into this promising ﬁeld.
In [ 33] research examines the feasibility of using workers’ smartphones as a legitimate
tool for employers to do presence control. In addition, they suggest a mobile location-aware
information system that satisﬁes universal access requirements, uses only reactive location
technologies based on terminals and allows for non-intrusive presence control while keeping
costs down. Encouraging workers to feel comfortable and in control of when their location
data is collected while meeting the employer’s control demands is the main emphasis. Using
UAProf data processing at the origin server and A-GPS terminal-based/network-aided mobile
positioning algorithms, the LAMS platform is a cutting-edge framework for synchronous
mobile location-aware content personalisation.
This study [ 34] provides the creation of a set of fake query sequences to conceal mobile
users’ query locations and query characteristics and safeguard their privacy in LBS. First,
they provide a framework that is centred on the client and aims to safeguard user privacy
in LBS. This framework does not need any modiﬁcations to the LBS algorithm used on
the server side, and it also ensures that the accuracy of an LBS query remains unaffected.
Second, they propose a privacy model within the framework to establish the criteria that
ideal dummy query sequences should adhere to. These criteria include: (1) maintaining a
similar feature distribution, which assesses the ability of the dummy query sequences to
conceal the true user query sequence, and (2) ensuring a high level of user privacy protection,
which evaluates the effectiveness of the dummy query sequences in safeguarding the location
and query privacy of a mobile user. Finally, they provide an implementation approach that
meets the privacy model’s requirements. Furthermore, both theoretical analysis and actual
assessment reveal the usefulness of our proposed technique, demonstrating that the location
and attribute privacy underlying LBS inquiries may be successfully safeguarded by the fake
queries created by our approach.
The author [35] offers a wide range of scientiﬁc data for many study topics that are used by
the associated scientiﬁc groups. Frequently, these websites’ architecture or design does not
match the way their customers think. Consequently, the desired data is not easily accessible.
Scientiﬁc online information services may beneﬁt from the methods developed by Usability
Engineering and User Experience to better understand and meet the needs of their users.
An easy-to-implement method for evaluating and improving scientiﬁc online information
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 5 of 25 234
services is detailed in this article. Combining personas, usability inspections, online ques-
tionnaires, Kano models, and web analytics with other techniques that have previously been
effectively used in reality makes up this approach.
In [36] the research suggests an Explainable Food Recommendation system to support its
suggestions using the visual content of food. In particular, a new similarity score is created
and included in the suggestion. This score is based on a propensity measure that quantiﬁes the
degree to which the user community favours a certain cuisine category. To improve the rec-
ommendation outcome’s openness and interpretability, a rule-based explainability is ﬁnally
added. Our results on a crawled dataset demonstrate that compared to other food recom-
mendation methods, the suggested approach improves recommendation quality by 7.35%,
6.70%, 7.32%, and 14.38%, respectively, in terms of recall, precision, F1, and Normalised
Dis-counted Cumulative Gain (NDCG). Additionally, they conduct ablation studies to prove
that our recommendation system’s components are technically sound.
In this study, [ 37] the author proposes to provide a novel strategy called Recommenda-
tion Based on Embedding Spectral Clustering in Heterogeneous Networks (RESCHet). This
approach makes use of the embedding spectral clustering method, whose similarity matrix is
produced using a heterogeneous embedding technique. Subsequently, they used the notions
of submit-paths and atomic meta-paths to identify the connections among people and things
relevant to every cluster. Finally, by calculating the Hadamard product between the perti-
nent vectors, they produced user suggestions. Tests conducted on three publicly available
benchmark datasets have shown that RESCHet performs noticeably better than the current
methods.
In this study [ 38], a recommender system that relies on Facebook user behaviour was
created, and it provides consumers with the option to purchase their favourite things in two
stages. The consumers’ behaviour is examined in the ﬁrst phase, and items are provided to
them depending on their interests. In the second step, the recommender system uses data
mining methods to provide consumers with offers that are related to their past purchases.
The study’s data are accurate, and the ﬁndings are reliable. Furthermore, the ﬁndings show
that the developed recommender system is quite accurate in presenting offers to consumers
(Table 1).
2.1 Research Gap
Certain gaps become apparent within the current corpus of research concerning location-
based services and advertising. To begin with, although research has examined digital
advertising architectures and customer preferences, more extensive inquiries are required to
determine the efﬁcacy and consequences of location-based advertising interventions for con-
sumers. Present models predominantly concentrate on concerns about advertising, customer
preferences, and recommendation systems. Consequently, there exists a knowledge vacuum
concerning the complexities linked to location-based mobile advertisements, including the
need to minimise intrusiveness while optimising openness. Furthermore, the investigation
into energy-efﬁcient and secure routing protocols for wireless sensor networks highlights
the criticality of further research into the intersection of energy efﬁciency and security in
location-based services. Moreover, a comprehensive examination of the integration of user-
generated text and geographical data for spatial market segmentation is lacking. Finally,
although recent research has examined privacy concerns in location-based advertising, there
remains a dearth of knowledge regarding the continual creation of strategies for success-
fully addressing these concerns in light of the growing relationship between advertisers and
123

234 Page 6 of 25 A. Pandey et al.
Table 1 Review of existing models for location aware-base services
References Title/year Problem Methods Result
[11] Deep learning-based feature
extraction and a bidirectional
hybrid optimized model for
location-based advertising, 2022
There is a growing privacy difﬁculty
among mobile users and
personalization worries as a result
of the increased connection
between the advertiser and the
consumer
To provide precise location details,
GIS gathers relevant location data.
Information about a word’s
geographical context is fed into the
embedding process. A vector and a
matrix are assigned to each word.
Then, a deep sparse autoencoder
(DSAE) is used to gather those
characteristics
Accuracy (99.97%), precision
(99.5%), F-measure (99.5%),
computational time (99.8 ms), the
area under the curve (82.23%), and
recall (99.52%) are only some of
the metrics used to evaluate the
suggested approach over a range of
document volumes
[39] “Uplift modeling for location based
online advertising, 2019
The efﬁcacy of location-based
targeting is unknown at this time
because of the challenges inherent
in determining the net impact of
advertising interventions on
consumers
Many studies have shown the
usefulness of uplift modeling for
estimating the ITE of various
interventions, which include but are
not limited to prescription direct
marketing and online advertising
Two distance characteristics, ﬁve
kinds of activity time, eleven types
of census data, and the number of
trips to 47 POI categories including
sports goods and clothing stores
remain after the advertiser’s store
frequency is subtracted. This allows
for the generation of an uplift curve
[40] Identifying machine learning
techniques for classiﬁcation of
target advertising, 2020
To solve the issues associated with
contextual advertising, the
suggested method employs
multiple instant learning (MIL)
boost
The ﬁndings indicate that 23 unique
user- centric and content-centric
strategies for delivering tailored
online advertisements may be
created with the use of machine
learning
We highlight the typical research
effort and provide a brief overview
of the aims and contributions of
every system in each area
[41] Opening location-based mobile ads:
How openness and location
congruency of location-based ads
weaken negative effects of
intrusiveness on brand choice, 2018
explored how location-based mobile
communications may be optimized
for maximum impact while
minimizing distractions like
unwanted feelings of intrusion
In this research, a virtual supermarket
was utilized in conjunction with a
location-based smartphone app to
recreate conditions that were
similar to those seen in a real
supermarket without leaving the
safety of the lab
switch from logistic regression to
PROCESS because LR can’t
foresee non-linear conditional
effects
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 7 of 25 234
Table 1 continued
References Title/year Problem Methods Result
[42] Recommendations in Location based
Social Networks: A Survey, 2015
It is a challenging task to infer users
social beliefs based on their
knowledge of various geographical
areas
They begin by classifying
recommender systems according to
their intended recommendation
target, which may be a speciﬁc
place, person, activity, or social
network. Then divide recommender
systems into three distinct
categories depending on their
underlying technology
Introduced a multi-tenant, multi-user,
multi-layer collaborative LBS
platform. Location estimation
hardware employed inside smart
buildings makes up the ﬁrst of
these levels
[43] Deep Learning for User Interest and
Response Prediction in Online
Display Advertising, 2019
Multiclass classiﬁcation, in addition
to binary classiﬁcation (for
predicting user clicks) (for user
interest prediction)
Generative modeling is used in the
corporate world. The CTR for a
fresh impression is calculated using
historical data and shown as a tree
model. Examples of generational
models are CTR hierarchy trees
and hierarchical Bayesian networks
Predicting user Ad responses and
user Ad clicks for individual
campaigns is enhanced by
considering patterns and temporal
variation of user requests,
according to experiments and
comparisons with actual data
[44] Smart Proﬁling of City Areas Based
on Web Data, 2018
Distinct areas of the city are marked
off using a computerized grid of
square cells
Selecting relevant data sources,
preprocessing them, extracting
important characteristics, running a
clustering algorithm to generate
city area proﬁles, and ﬁnally
visualizing the results on a city map
are all steps taken by the system
They used k-means clustering and
varying cell sizes to group city
areas. We show how clustered areas
in different city zones have similar
traits
[45] TDP: A Novel Secure and Energy
Aware Routing Protocol for
Wireless Sensor Networks, 2017
The suggested protocol routes in four
steps. Topology management
begins with k-means. LQA
evaluates every network node in the
second stage
Grading, based on LQA value,
assigns grade points to each
network node in the third stage. At
the last stage, grade points
determine the routing’s safest path
The NS2 is used to test the proposed
protocol in a signiﬁcant class of
SONs, such as a WSN. The
effectiveness is measured by the
current LEACH procedure
123

234 Page 8 of 25 A. Pandey et al.
Table 1 continued
References Title/year Problem Methods Result
[46] False advertising or slander? Using
location-based tweets to assess
online rating- reliability, 2017
The system utilizes amazon product
reviews and Twitter message
corpora to forecast item classes,
after which they employ these
ratings to discover geographic
clusters. The models use
transformers as an attention
mechanism and BERT-based data
augmentation
This research elucidates the causes of
bias in online rating systems and
gives a quantitative assessment of
such prejudice. The authors
compute a happiness score for a
venue using location-aware tweets
from companies and compare it to
Y elp reviews to see whether the
venue is overrated or underrated
Using the Affective Norms for
English Terms lexicon, we can
mine Foursquare and Twitter to
determine the sentiment of
location-aware tweets (ANEW)
[47] Geo-Spatial Market Segmentation &
Characterization Exploiting User
Generated Text Through
Transformers & Density-Based
Clustering, 2021”
In this paper, we present a study of
spatial market segmentation, which
we believe to be a novel approach
to integrating and combining
geographical data with
user-generated text content to
discover geographic clusters of
textual occurrences and infer links
between each cluster and a set of
retail product categories
Using Amazon customer reviews and
Twitter message corpora, several
machine learning models predict
product classes, and those scores
are then utilized to group the
collected geographic clusters
Effectively producing maps of
regions along with evaluations for
how pertinent they are to a group of
classes is the goal of this method.
Our product document classiﬁer
achieved an F1-Score of 86% for
product reviews and 76% for
tweets after we manually annotated
data from 10 product categories
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 9 of 25 234
mobile users. By recognising and rectifying these deﬁciencies, one can enhance the overall
comprehension of the complexities and potentialities that lie within the dynamic domain
of location-based advertising and services. In contrast to prior investigations, the present
study employs GIS to acquire accurate location data by integrating geographical context
into the word embedding procedure. Innovating the application of advanced deep learning
techniques to location-based advertising is exempliﬁed by the creation of a Bidirectional
Optimised Hybrid Model (BLSTM-DNN-ASOA) and the implementation of a deep sparse
autoencoder (DSAE) for feature extraction. The efﬁcacy of a proposed model is demonstrated
by a comprehensive set of evaluation metrics, which comprise F-measure, precision, accu-
racy, computational time, AUC, and recall. Through the attainment of enhanced performance
compared to prior approaches, this article makes a signiﬁcant contribution to the advance-
ment of knowledge and implementation of deep learning in the domain of location-based
advertising. As a result, it provides industry practitioners and academics with invaluable
insights.
3 Methodology
3.1 Convolutional Neural Network (CNN)
Among the various applications for deep neural networks, image and video processing are
among the most common. This is especially true with convolutional neural networks (CNNs).
There has been a rise in the use of convolutional neural networks (CNNs) to analyze numerical
data, including time series and sensor data, in recent years [ 48]. The main idea behind CNNs
for numeric data is to apply the convolution operation to local temporal windows of the input
data, allowing the network to learn temporal patterns and dependencies in the data. CNNs
are effective at capturing both local and global patterns in time series data, making them
suitable for various applications such as time series forecasting, anomaly detection, and signal
processing. Despite their effectiveness, CNNs for numeric data still face some challenges,
such as dealing with missing data and handling long-term dependencies. Recent advances
in research have focused on developing more robust and efﬁcient CNN architectures, such
as the WaveNet and Temporal Convolutional Network (TCN) models, which have shown
promising results in various applications. In addition to numeric data, CNNs have also been
used for other types of data, such as text and graphs, demonstrating their versatility and
potential to advance the ﬁeld of deep learning. Overall, CNNs represent a powerful tool for
processing various types of data, and their continued development and optimization have the
potential to advance the ﬁeld of artiﬁcial intelligence and its applications in various domains
[49]. In Fig. 1, we see the basic structure of a convolutional neural network (CNN) that may
be used to classify images.
A typical CNN will include the following layers: input, convolution, ReLU, pooling, and
completely connected
• Input The raw pixel values are stored in this layer, as the name implies. The original data
for a photograph may be seen in its "raw" pixel values.
• Convolution Being the primary processing node, this layer is an essential component of
convolutional neural networks.
• ReLU Activation-function-using layer: a layer that takes the output of the previous layer
and utilizes it to activate its output (also called a rectiﬁed linear unit layer). RELU’s
addition to the network’s non-linearity would take another form.
123

234 Page 10 of 25 A. Pandey et al.
Fig. 1 Convolutional neural network (CNN)
• Pooling The pooling layer is another part of convolutional neural networks. Pooling
operations refer to the act of combining the values of neighbouring features into a single
one by using either an average or a histogram operator. The incorporation of pooling into
the model has several goals, the primary ones being to make the model immune to local
distortions and to reduce the total number of features [ 50].
• Fully Connected Moreover, this layer might be referred to as the "output" layer or the
fully linked layer. It is used in the determination of class score output, the outcome of
which is a voluminous 1*1*L array, where L is the integer representing the class score.
3.2 Long Short Term Memory (LSTM)
LSTMs, like RNNs, are composed of many interconnected layers, but the interactions
between these four levels occur differently. There are memory cells in the LSTM model,
and gates control them. There are three distinct types of entrance gates (input gate, output
gate, and forget gate). These gates, which control the ﬂow of data like dials, are responsible
for mixing the data. To alter the data in an LSTM, these gates are used. A ﬁxed quantity of
training data may be stored in the memory module. Cell state memory is the memory unit that
gives LSTM the ability to recall long-term dependencies. There are three primary varieties of
gates: the forget gate, the I/P gate, and the O/P gate [51]. Short-term and long-term memories
are stored in different types of memory cells. It reminds me of a conveyor belt in certain
ways. It permeates the whole sequence and has only minimal pointwise operations with the
gates. LSTM is an excellent tool for classifying processes and making predictions based on
time series over a given amount of time [ 52].
• Hidden State An LSTM layer’s output, known as the hidden state, is used as input in the
layer that follows it. To indicate how much of each piece should be sent, the sigmoid
layer produces values between 0 and 1. The Tanh layer produces new state-enhancing
vectors.
ht = ot · tanh(ct) (1)
• F orget Gate The data stored in a memory cell may be removed using the forget gate.
If the situation changes, the forget gate will produce zeros, which the memory cell will
pointwise multiply, erasing the associated data. The sigmoid layer then generates a vector
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 11 of 25 234
Fig. 2 Long Short Term Memory (LSTM)
with values between 0 and 1.
ft = σ( W f ·[ ht−1, xt ]+ b f ) (2)
• Input Gate The I/P gate of the state cell decides if the input needs to be looked at more
closely to see if data needs to be entered (or changed). For example, the output from
the previous iteration ot-1, the I/P tx, and the initial condition of iteration ct-1 are all
examples of inputs that may need to be looked at more closely. This is put point-ﬁrst into
the memory cell.
it = σ( Wi ·[ ht−1, xt ]+ bi) (3)
• Output Gate The ﬁnal product will be an abstracted version of the current state of memory.
The amount of information sent from the visible state of the cell to the hidden state is
managed by the output gate. Then, we choose which features of the cell will go to the
hidden layer, which is the sigmoid layer (Fig. 2). The cellular state is multiplied by the
sigmoid gate’s output after a tanh-tanh transformation, producing values between -1 and
1.
ot = σ( Wo ·[ ht−1, xt ]+ bo) (4)
4P r o p o s e d M o d e l
An in-depth description of the suggested model and its accompanying algorithm are presented
here, together with a discussion of the research process used to develop it.
123

234 Page 12 of 25 A. Pandey et al.
4.1 Problem Identification
Establishing a measure of service quality is the primary obstacle to service recommendation
(QoS). Location-based advertising is a popular advertising strategy that targets users based
on their geographical location. However, existing location-based advertising methods have
limited accuracy and effectiveness due to several factors, such as inaccurate location data, a
limited understanding of user behaviour, and a lack of personalized targeting. Deep learning
techniques can provide a solution to these problems by leveraging complex models to analyze
and interpret user data, which can be used to generate personalized and effective location-
based advertising.
Therefore, the problem for location-based advertising using deep learning is to develop
accurate and effective models that can leverage user data to generate personalized advertising
recommendations based on their geographical location. This requires addressing the follow-
ing challenges: data quality, user behaviour modeling, personalization, and privacy concerns.
In solving these challenges, developing deep learning models is required to effectively anal-
yse and interpret location data to generate personalized advertising recommendations that
are relevant and effective for individual users while also addressing privacy concerns.
4.2 Research Methodology
In this study, we mix conventional and deep learning techniques to create a hybrid model for
predicting the popularity of location-based services based on user recommendations. Python
is used for the actual implementation. This is accomplished by using the freely available WS-
Dream dataset. There are a total of 5,825 services and 19,74,675 QoS values from 339 users.
Then the collected dataset was preprocessed using different data preprocessing techniques. In
the data preprocessing, handling and ﬁlling in the missing values, and also using the Z-score
normalization technique for data normalization. In addition, the min-max method is used for
data scaling. In this work, features are identiﬁed and extracted in the feature extraction, and
the Pearson correlation coefﬁcient is also calculated in the correlation analysis. Then, split the
dataset into two sets: train sets and test sets, and the ratio of training and testing is 80 and 20.
After this process, different deep learning approaches are applied to perform the prediction,
and the names of these are LSTM and CNN. With the use of these models, a hybrid model is
built to implement this research, and the name of this hybrid model is the hybrid CNN-LSTM
model. The correctness of the proposed model was evaluated using several statistical metrics,
including the average absolute error, root mean squared error, coefﬁcient of determination,
etc. Finally, the proposed hybrid CNN-LSTM model may be used to forecast the QoS values
of online services at indicated locations.
4.3 Hyperparameter Tunning
The design of the hybrid CNN-LSTM model for predicting location-based service popularity
in this research included the use of many crucial hyperparameters. The architecture of the
model was determined by setting the amount of LSTM units and CNN ﬁlters to 64, which
inﬂuenced its ability to collect both temporal and spatial data efﬁciently. The learning rate
of 0.001, an important hyperparameter, was carefully chosen to manage the step size of
the optimization process, which inﬂuences the model’s convergence pace. Another critical
parameter, the dropout rate of 0.3, was used to prevent overﬁtting, with its value controlling
the proportion of neurons randomly destroyed during training. To balance training speed
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 13 of 25 234
and memory limitations, the batch size of 64, which represents several samples processed in
every iteration, was determined. A number of epochs, which represents iterations throughout
the full training dataset, was a critical hyperparameter inﬂuencing training length and model
convergence. Non-linearity was introduced by carefully selecting activation functions in the
layers, such as ReLU for CNN and sigmoid or tanh for LSTM. The optimizer (Adam) and
the loss function (typically Mean Squared Error (MSE) or others adapted to the prediction
task) further inﬂuenced the model’s performance. These hyperparameters worked together to
ﬁne-tune the model’s prediction capabilities, with optimization carried out through extensive
experimentation and validation on training and validation datasets.
4.4 Dataset Collection and Description
For this research, the WS-Dream dataset is utilized to assess how well the suggested method
works. QoS values from several users across multiple services may be found in the WS-Dream
dataset, a massive web services dataset. To evaluate the efﬁcacy of our proposed algorithm,
the dataset’s inclusion of location data for both users and services makes it a particularly
suitable candidate. The WS-Dream dataset includes 19,74,675 quality of service metrics,
collected from 339 users over 5,825 services. There is a wide range of possible quality of
service metrics, including throughput, response time, reliability, and availability. QoS data
was shown as a user-service matrix, with people in the rows and services in the columns, to
make it easier to analyze (Table 2).
4.5 Data Preprocessing
The suggested method would beneﬁt from the addition of the Autonomous System Number
(ASN). The utilized dataset included customers from 30 countries and 136 ASNs and services
from 73 countries and 990 ASNs. To guarantee the algorithm’s success, we preprocessed
the data in question. It included dealing with missing values, which may arise from some
causes, including improper data input or inadequate data gathering. Imputation was used to
manage missing values, which entails replacing them with approximated values based on the
existing data. In this research, we imputed missing values using the attribute’s mean value
using a process called mean imputation. Including CN and ASN attributes into the algorithm
required using Sklearn’s category encoding transforms the labeled features into numerical
embeddings. This allowed us to express each classiﬁed attribute as a nation code, which can
be used to generate personalized ads for each user based on their location. Furthermore, we
also performed data normalization to ensure that all the attributes had the same scale, which is
important for many machine learning algorithms to function correctly. Z-score normalization,
whereby the numbers of every feature are adjusted precisely to have a mean of zero and a
standard deviation of one, was also utilized. Finally, we also performed feature scaling to
ensure that all the features had similar ranges, which is necessary for some algorithms to
function properly. All features are also scaled to fall inside the range [0, 1] using the Min-
Max scaler approach. Overall, these pre-processing steps helped us to ensure that the data
was in a suitable format for machine learning algorithms to be applied and improved the
accuracy and effectiveness of the proposed model.
123

234 Page 14 of 25 A. Pandey et al.
Table 2 Data description
Metric V alue
Dataset WS-Dream
Metrics Quality of Service (QoS), Size
Size 19,74,675 QoS metrics
Users 339
Services 5825
Data Format User-Service Matrix
QoS Metrics Throughput, Response Time, Reliability, Availability, etc
Data Collection Massive web services dataset
Additional Features Includes location data for both users and services
Purpose To assess the efﬁcacy of the proposed algorithm in the context of location-based services
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 15 of 25 234
4.6 Feature Extraction
What we mean by "feature extraction" is the transformation of unstructured data into discrete
characteristics that may be used in subsequent analyses without losing any of the original
data’s context. In this study, we use feature extraction methods to zero in on the data points
that will be most useful to our model. We employed a method called correlation analysis,
which entails determining how closely each characteristic is linked to the desired outcome
(here, the user’s choice for a certain service). The model places a premium on features that
have a strong correlation with the dependent variable. The Pearson correlation coefﬁcient
between each characteristic and the outcome variable was determined for examination of
correlation. The Pearson correlation coefﬁcient, which may also take on ranges around -1
and 1, is used to measure the linear connection between two variables. There is a perfect
positive correlation when the value is 1, no connection at all when the value is 0, and a
perfect negative correlation when the value is -1.
Based on the correlation analysis, we identiﬁed the most relevant features for this proposed
model. These features were then used as input variables for our algorithm, and with careful
feature selection, we were able to boost the model’s accuracy and performance. Overall,
feature extraction techniques such as correlation analysis can be useful in identifying the
most important features of a machine learning model, which can improve its accuracy and
efﬁciency.
4.7 Data Splitting
Machine learning often makes use of data splitting to separate data into distinct groups.
There should ideally be three distinct sets of information: "train," "validation," and "test.".
Dividing data is advised to improve the amount of training data in each dataset. In training
and testing, data is often divided 80:20 or 70:30. For moderate-sized datasets, dividing the
data into three equal parts–70% training, 20% validation, and 10% testing–is suggested. For
this study, we created a training set with 80% of the data and a testing set with 20%. (20%
of total information).
4.8 Proposed Hybrid CNN-LSTM Model
Here, we present a hybrid approach that utilizes LSTM and CNNs, and we evaluate it using
the WS-Dream dataset. Quality of Service (QoS) measurements from many users across
multiple providers may be found in the WS-Dream dataset. Due to the inclusion of user and
service locations, this dataset is ideal for testing the efﬁcacy of the suggested approach. The
proposed CNN-LSTM model takes in user ratings of web service quality from the WS-Dream
dataset. Quality-of-service (QoS) indicators are used to train a convolutional neural network
(CNN) to extract high-level spatial features from an input dataset. The LSTM receives the
CNN’s output and learns to successively process the features while capturing their temporal
relationships. For the LSTM part, we employed cells that can remember and pass along
information about their surroundings over very long periods. The WS-Dream dataset was
used to teach the hybrid model, which has 19,74,675 QoS values across 339 users and 5,825
services. Response time, throughput, availability, and dependability are just a few examples
of the many QoS variables that may be measured. This article describes the deep learning
models and their architectures that were utilized to produce this hybrid model (Fig. 3).
123

234 Page 16 of 25 A. Pandey et al.
Fig. 3 Structure of Proposed Hybrid CNN-LSTM model
5 Experimental Results and Analysis
Here, we report on our experiments with Python-based location-based services applied to the
WS-Dream dataset. The success of the proposed method may be measured in two ways.
5.1 Evaluation Metrics
RMSE and MAE are common statistical assessment metrics used to determine how well the
provided method performs.
1. Mean Absolute Error (MAE) While calculating the mean absolute error, the errors are not
squared. The absolute value of the mistakes is determined and then averaged.
We only care about the magnitude of the difference between the estimated and real target
values; hence, the MAE uses the absolute value. This prevents the MAE from being
inaccurately calculated due to mistakes cancelling each other out. The formula for RMSE
is as follows Eq. 5.
MA E = 1 n n∑ i=1 |yi − xi | (5)
In this formula: MAE represents the Mean Absolute Error. n: is the number of data points
or observations. yi : represents the actual or observed values. xi : represents the predicted
or estimated values for the corresponding observations.
2. Root Mean Squared Error (RMSE) The Root Mean Squared Error (RMSE) is calculated
by averaging the squared errors over all samples and then squaring the result. This is
similar to the Mean Squared Error (MSE) but with a square root instead of a plus sign.
This allows RMSE to produce an error metric that is consistent with the target variable’s
measurement system. If next year’s sales are our objective y, then the RMSE will offer
the error in dollars, whereas the MSE will give the error in dollars squared, which is
considerably less comprehensible. The formula for RMSE is as follows Eq. 6.
RMSE =
√
1
n /Sigma1n i=1(Yi − ˆYi)2 (6)
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 17 of 25 234
In this formula: RMSE represents the Root Mean Square Error. n: is the number of data
points or observations. yi : represents the actual or observed values. xi : represents the
predicted or estimated values for the corresponding observations.
The selection of RMSE and MAE as evaluation metrics for this research is driven by
their interpretability, sensitivity to outliers, and suitability for model optimisation. The mea-
sures used provide a fair assessment of both the average magnitude of mistakes and the
consequences of bigger deviations. The combination of RMSE and MAE allows for a com-
prehensive evaluation that aligns with speciﬁc characteristics and priorities of a dataset and a
recommendation system in the domain of location-aware recommendations, where the goal
is to provide accurate and meaningful suggestions to users.
5.2 Result
This section provides visual representations of the different WS-Dream dataset-based trial
results. The output for the WS-Dream dataset utilized is presented in the form of graphs and
tables below.
Table 3, showcases a performance result of a proposed Hybrid CNN-LSTM model, eval-
uated employing the WS-Dream dataset. For the metric of Response Time, the MAE and
RMSE exhibit a decreasing trend as the density increases from 0.5 to 0.25, with the lowest
MAE and RMSE observed at a density of 0.25. Speciﬁcally, at a density of 0.25, the MAE is
0.359 and the RMSE is 0.1388. Similarly, for Throughput, both MAE and RMSE decrease as
density increases, with the lowest values again observed at a density of 0.25. At this density,
the MAE is 12.764, and the RMSE is 37.874. These results suggest that increasing density
leads to improved performance of the Hybrid CNN-LSTM model in predicting both RT and
Throughput metrics for location-aware web service recommendation tasks.
Table 4, showcases a performance result of a proposed Hybrid CNN-LSTM model, eval-
uated employing the WS-Dream dataset. For the metric of Response Time, the MAE and
RMSE exhibit a decreasing trend as the density increases from 0.5 to 0.25, with the lowest
MAE and RMSE observed at a density of 0.25. Speciﬁcally, at a density of 0.25, the MAE is
0.359 and the RMSE is 0.1388. Similarly, for Throughput, both MAE and RMSE decrease as
density increases, with the lowest values again observed at a density of 0.25. At this density,
the MAE is 12.764, and the RMSE is 37.874. These results suggest that increasing density
leads to improved performance of the Hybrid CNN-LSTM model in predicting both RT and
Throughput metrics for location-aware web service recommendation tasks.
Table 5 presents a comprehensive comparison of experimental results for Response Time
in Location-Aware Web Service Recommendation across various models and densities. The
performance metrics, like MAE and RMSE, are depicted for densities ranging from 0.5 to
0.25. Among the models evaluated, Hybrid CNN-LSTM demonstrates competitive perfor-
mance with decreasing MAE and RMSE values as density increases. Notably, at a density
of 0.25, the Hybrid CNN-LSTM model achieves an MAE of 0.359 and an RMSE of 0.1388.
For RLSD, at the same density, the MAE is 0.5214, and the RMSE is 0.1583. Comparison
with other models reveals varying levels of effectiveness, with UMEAN, IMEAN, UPCC, and
IPCC demonstrating relatively higher errors across different densities. Models like LDCF and
NCF exhibit lower errors compared to others, while RLSD displays consistent performance
across densities. Overall, the results underscore the effectiveness of the Hybrid CNN-LSTM
model in accurately predicting Response Time, particularly at higher densities, showcasing
its potential for enhancing location-aware web service recommendation systems.
Figures 4 and 5 show the results of an MAE and RMSE comparison of a proposed hybrid
123

234 Page 18 of 25 A. Pandey et al.
Table 3 Performance results of the proposed hybrid CNN-LSTM model
Hybrid CNN- LSTM Model Density
0.5 0.10 0.15 0.20 0.25
MAE RMSE MAE RMSE MAE RMSE MAE RMSE MAE RMSE
Response Time 0.5275 0.1683 0.4066 0.1388 0.359 0.1683 0.5214 0.1583 0.4588 0.1244
Throughput 18.534 52.566 13.566 45.687 12.784 40.533 12.654 45.656 12.764 37.874
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 19 of 25 234
Table 4 Response time experimental results
Approaches Density
0.5 0.10 0.15 0.20 0.25
MAE RMSE MAE RMSE MAE RMSE MAE RMSE MAE RMSE
UMEAN 0.876 0.853 0.873 1.857 0.874 1.857 0.873 1.858 0.874 1.858
IMEAN 0.703 0.567 0.686 1.542 0.684 1.533 0.681 1.529 0.68 1.525
UPCC 0.634 0.377 0.553 1.311 0.511 1.258 0.483 1.22 0.467 1.189
IPCC 0.633 1.397 0.591 1.341 0.507 1.258 0.454 1.208 0.431 1.175
UIPCC 0.624 1.386 0.579 1.328 0.498 1.247 0.448 1.197 0.425 1.165
RegionKNN 0.594 1.641 0.577 1.637 0.569 1.627 0.569 1.617 0.562 1.619
LACF 0.682 1.5 0.65 1.468 0.61 1.416 0.582 1.381 0.562 1.357
PMF 0.568 1.537 0.487 1.321 0.451 1.221 0.43 1.171 0.416 1.139
NCF 0.44 1.325 0.385 1.283 0.372 1.253 0.362 1.205 0.349 1.138
LDCF 0.246 0.7398 0.2787 0.895 0.2291 0.7573 0.237 0.8004 0.2585 0.8819
RLSD 0.5643 0.1765 0.4977 0.1699 0.53 0.1892 0.6155 0.1831 0.5977 0.171
Hybrid CNN- LSTM Model 0.5275 0.1683 0.4066 0.1388 0.359 0.1683 0.5214 0.1583 0.4588 0.1244
Bold indicates the result of proposed model
123

234 Page 20 of 25 A. Pandey et al.
Table 5 Throughput experimental results
Approaches Density
0.5 0.10 0.15 0.20 0.25
MAE RMSE MAE RMSE MAE RMSE MAE RMSE MAE RMSE
UMEAN 54.333 110.296 53.947 110.345 53.971 110.201 53.906 110.19 53.862 110.194
IMEAN 27.342 65.844 26.962 64.843 26.757 64.266 26.669 64.069 26.595 63.873
UPCC 27.559 60.757 22.687 54.598 20.525 50.906 19.243 48.834 18.253 47.135
IPCC 27.102 62.665 26.27 60.479 25.487 57.561 23.726 54.564 22.286 52.293
UIPCC 27.07 60.51 22.44 54.506 20.256 50.585 18.888 48.238 17.863 46.392
RegionKNN 26.857 69.614 25.352 68.015 24.947 67.365 24.687 66.923 24.746 66.831
LACF 27.419 65.77 24.847 62.057 22.943 58.816 21.562 56.507 20.587 54.785
PMF 18.943 57.02 16.004 47.933 14.668 43.642 13.988 41.652 13.398 40.025
NCF 15.468 49.703 13.616 46.034 12.284 42.317 11.833 41.263 11.312 39.534
LDCF 17.629 57.746 14.711 50.73 13.952 48.871 13.199 47.323 12.332 45.142
RLSD 19.517 61.822 16.154 53.344 14.958 50.681 14.388 49.393 14.332 49.195
Hybrid CNN- LSTM Model 18.534 52.566 13.566 45.687 12.784 40.533 12.654 45.656 12.764 37.874
Bold indicates the result of proposed model
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 21 of 25 234
Fig. 4 Loss values comparison of response time
Fig. 5 Loss values comparison of throughput
CNN-LSTM model with those of current models in terms of reaction time and throughput
at varying densities (0.05 to 0.25). A more precise model could be possible with less loss
(except if the model was overﬁtting to the data in the training set). During both training and
testing, the loss value may be calculated to evaluate the model’s efﬁcacy on the two datasets.
Similar to accuracy, the loss does not have a proportional representation. It’s the sum of all
the blunders in a sample’s training and testing data. In terms of reaction time and throughput,
the suggested hybrid CNN-LSTM model was demonstrably superior to modern methods.
Figures 4 and 5 shows the results of comparing the proposed hybrid CNN-LSTM model
with current models in terms of reaction time and throughput at different densities (0.05 to
0.25) using the mean absolute error (MAE) and root mean squared error (RMSE). A more
precise model could be possible with less loss (except if the model was overﬁtting to the
data in the training set). During both training and testing, the loss value may be calculated
to evaluate the model’s efﬁcacy on the two datasets. Similar to accuracy, the loss does not
123

234 Page 22 of 25 A. Pandey et al.
have a proportional representation. It’s the sum of all the blunders in a sample’s training and
testing data. In terms of reaction time and throughput, the suggested hybrid CNN-LSTM
model was demonstrably superior to state-of-the-art methods.
6 Conclusion
This research offers a unique deep neural network-based Location-aware services recom-
mendation model, in particular the Hybrid CNN-LSTM model, which has been suggested
as an approach for location-aware web service recommendation, exhibits outstanding accu-
racy in the WS-Dream dataset at different densities. The assessment, illustrated through the
utilization of tables and ﬁgures, demonstrates that the model’s precision in forecasting reac-
tion time and throughput enhances as the density level decreases. Notably, the minimum
values of MAE and RMSE are detected at density 0.25. As illustrated in Tables 3 and 4,
the reduced MAE and RMSE values for reaction time and throughput indicate that a model
consistently outperforms modern approaches. The model’s precision is further underscored
by loss value comparisons in Figs. 4 and 5, which demonstrate reduced losses throughout
the training and testing phases in comparison to existing models. The combined evidence
highlights the effectiveness of the Hybrid CNN-LSTM model that has been proposed for
improving the precision of location-aware web service recommendations, with a particular
emphasis on its performance at lower density levels. Despite this, it does what we need it to
do; nonetheless, more research and improvement in QoS prediction are required. We hope to
modify the hyperparameters of the deep learning model used for location service recommen-
dations shortly. This study presents an application survey and research scope to encourage
researchers to solve service recommendation difﬁculties and to aid them in picking a more
effective algorithm strategy for a suggestion based on the system’s requirements and input
sets. This work will continue to progress in the area of recommendation systems and improve
their ability to fulﬁl user requirements.
Funding Not applicable
Data Availability Statement The data used in this study will be made available upon reasonable request.
Declarations
Conﬂict of interest The authors declare that they have no Conﬂict of interest.
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction
in any medium or format, as long as you give appropriate credit to the original author(s) and the source,
provide a link to the Creative Commons licence, and indicate if you modiﬁed the licensed material. Y ou do
not have permission under this licence to share adapted material derived from this article or parts of it. The
images or other third party material in this article are included in the article’s Creative Commons licence,
unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative
Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use,
you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit
http://creativecommons.org/licenses/by-nc-nd/4.0/ .
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 23 of 25 234
References
1. Ketelaar PE, Bernritter SF, Riet J, Hühn AE, Woudenberg TJ, Müller BC, Janssen L (2017) Disentangling
location-based advertising: the effects of location congruency and medium type on consumers’ ad attention
and brand choice. Int J Advert 36(2):356–367
2. Afanador JJC, Rivero AJL, Gallego JÁR (2020) Analysis of geolocation accuracy by gps: dedicated
support signal integration and collaborative network in location-based services. In: 2020 15th Iberian
conference on information systems and technologies (CISTI). IEEE, pp 1–8
3. Aydin G, Karamehmet B (2017) A comparative study on attitudes towards sms advertising and mobile
application advertising. Int J Mobile Commun 15(5):514–536
4. Rohilla V , Chakraborty D (2019) Random forest with harmony search optimization for location based
advertising. Int J Innov Technol Explor Eng 8:1092–1097. https://doi.org/10.35940/ijitee.I7761.078919
5. Koren Y , Bell R, V olinsky C (2009) Matrix factorization techniques for recommender systems. Computer
42(8):30–37
6. Vlachos M, Dünner C, Heckel R, V assiliadis VG, Parnell T, Atasu K (2018) Addressing interpretability and
cold-start in matrix factorization for recommender systems. IEEE Trans Knowl Data Eng 31(7):1253–1266
7. Kumar R, V erma B, Rastogi SS (2014) Social popularity based svd++ recommender system. Int J Comput
Appl 87(14)
8. He X, Liao L, Zhang H, Nie L, Hu X, Chua T-S (2017) Neural collaborative ﬁltering. In: Proceedings of
the 26th international conference on world wide web, pp 173–182
9. Laurent G, Kapferer J-N (1985) Measuring consumer involvement proﬁles. J Mark Res 22(1):41–53
10. Bruner GC, Kumar A (2007) Attitude toward location-based advertising. J Interact Advert 7(2):3–15
11. Rohilla V , Chakraborty S, Kumar R (2022) Deep learning based feature extraction and a bidirectional
hybrid optimized model for location based advertising. Multimedia Tools Appl 81(11):16067–16095
12. Jenifer M, Kannan ST (2018) Lacfac-location-aware collaborative ﬁltering and association-based
clustering approach for web service recommendation. Int J Web Eng Technol 13(3):203–224
13. Nguyen HHC, Bui TK, Nguyen VL, Nguyen TT (2022) An effective method for clustering-based web
service recommendation
14. Guo G (2013) Improving the performance of recommender systems by alleviating the data sparsity and
cold start problems. In: Twenty-third international joint conference on artiﬁcial intelligence
15. Choi S-M, Lee D, Jang K, Park C, Lee S (2023) Improving data sparsity in recommender systems using
matrix regeneration with item features. Mathematics 11(2):292
16. Afoudi Y , Lazaar M, Al Achhab M (2021) Hybrid recommendation system combined content-
based ﬁltering and collaborative prediction using artiﬁcial neural network. Simul Model Pract Theory
113:102375
17. Saini S, Bansal R (2023) Geo-marketing: a new tool for marketers. In: Enhancing customer engagement
through location-based marketing. IGI Global, pp 102–112
18. Ravi L, V airavasundaram S, et al (2016) A collaborative location based travel recommendation system
through enhanced rating prediction for the group of users. Comput Intell Neurosci 2016
19. Rohilla V , Kaur M, Chakraborty S (2022) An empirical framework for recommendation-based location
services using deep learning. Eng Technol Appl Sci Res 12(5):9186–9191
20. Rohilla V , Chakraborty S, Singh MS, et al (2019) Data clustering using bisecting k-means. In: 2019
International conference on computing, communication, and intelligent systems (ICCCIS). IEEE, pp
80–83
21. Rohilla V , Chakraborty S, Kaur M, et al (2022) Artiﬁcial intelligence and metaheuristic-based location-
based advertising. Sci Program 2022
22. Tan GW-H, Lee V -H, Hew J-J, Ooi K-B, Wong L-W (2018) The interactive mobile social media
advertising: an imminent approach to advertise tourism products and services? Telematics Inform
35(8):2270–2288
23. Li Y , Xu W (2021) D-adfeed: a diversity-aware utility-maximizing advertising framework for mobile
users. Comput Netw 190:107954
24. Goh K-Y , Chu J, Wu J (2015) Mobile advertising: an empirical study of temporal and spatial differences
in search behavior and advertising response. J Interact Mark 30(1):34–45
25. Li K, Du TC (2012) Building a targeted mobile advertising system for location-based services. Decis
Support Syst 54(1):1–8
26. Haider CMR, Iqbal A, Rahman AH, Rahman MS (2018) An ensemble learning based approach for
impression fraud detection in mobile advertising. J Netw Comput Appl 112:126–141
27. Ryu S, Park Y (2020) How consumers cope with location-based advertising (lba) and personal information
disclosure: the mediating role of persuasion knowledge, perceived beneﬁts and harms, and attitudes toward
lba. Comput Hum Behav 112:106450
123

234 Page 24 of 25 A. Pandey et al.
28. Lu C-C, Wu L, Hsiao W-H (2019) Developing customer product loyalty through mobile advertising:
affective and cognitive perspectives. Int J Inf Manage 47:101–111
29. Shin W, Lin TT-C (2016) Who avoids location-based advertising and why? Investigating the relationship
between user perceptions and advertising avoidance. Comput Hum Behav 63:444–452
30. Y ang B, Kim Y , Y oo C (2013) The integrated mobile advertising model: the effects of technology-and
emotion-based evaluations. J Bus Res 66(9):1345–1352
31. Sharma A, Dwivedi YK, Arya V , Siddiqui MQ (2021) Does sms advertising still have relevance to increase
consumer purchase intention? A hybrid pls-sem-neural network modelling approach. Comput Hum Behav
124:106919
32. Jiang H, Li J, Zhao P , Zeng F, Xiao Z, Iyengar A (2021) Location privacy-preserving mechanisms in
location-based services: a comprehensive survey. ACM Comput Surv (CSUR) 54(1):1–36
33. Rios-Aguilar S (2014) Intelligent position aware mobile services for seamless and non-intrusive clocking-
in
34. Wu Z, Li G, Shen S, Lian X, Chen E, Xu G (2021) Constructing dummy query sequences to protect
location privacy and query privacy in location-based services. World Wide Web 24:25–49
35. Schön E-M, Hellmers J, Thomaschewski J (2014) Usability evaluation methods for special interest internet
information services
36. Rostami M, Muhammad U, Forouzandeh S, Berahmand K, Farrahi V , Oussalah M (2022) An effective
explainable food recommendation using deep image clustering and community detection. Intell Syst Appl
16:200157
37. Forouzandeh S, Berahmand K, Sheikhpour R, Li Y (2023) A new method for recommendation based on
embedding spectral clustering in heterogeneous networks (reschet). Expert Syst Appl 120699
38. Forouzandeh S, Soltanpanah H, Sheikhahmadi A (2015) Application of data mining in designing a
recommender system on social networks. Int J Comput Appl 124(1)
39. Kawanaka S, Moriwaki D (2019) Uplift modeling for location-based online advertising. In: Proceedings
of the 3rd ACM SIGSPA TIAL international workshop on location-based recommendations, geosocial
networks and geoadvertising, pp 1–4
40. Choi J-A, Lim K (2020) Identifying machine learning techniques for classiﬁcation of target advertising.
ICT Express 6(3):175–180
41. Ketelaar PE, Bernritter SF, Woudenberg TJ, Rozendaal E, Konig RP , Hühn AE, V an Gisbergen MS, Janssen
L (2018) “opening” location-based mobile ads: How openness and location congruency of location-based
ads weaken negative effects of intrusiveness on brand choice. J Bus Res 91:277–285
42. Bao J, Zheng Y , Wilkie D, Mokbel M (2015) Recommendations in location-based social networks: a
survey. GeoInformatica 19:525–565
43. Gharibshah Z, Zhu X, Hainline A, Conway M (2020) Deep learning for user interest and response
prediction in online display advertising. Data Sc Eng 5(1):12–26
44. D’Andrea E, Ducange P , Loffreno D, Marcelloni F, Zaccone T (2018) Smart proﬁling of city areas based
on web data. In: 2018 IEEE international conference on smart computing (SMARTCOMP). IEEE, pp
226–233
45. Karthick S (2018) Tdp: A novel secure and energy aware routing protocol for wireless sensor networks.
Int J Intell Eng Syst 11(2)
46. Poddar A, Banerjee S, Sridhar K (2019) False advertising or slander? using location based tweets to assess
online rating-reliability. J Bus Res 99:390–397
47. Ferro-Díez LE, Villegas NM, Díaz-Cely J, Acosta SG (2021) Geo-spatial market segmentation & charac-
terization exploiting user generated text through transformers & density-based clustering. IEEE Access
9:55698–55713
48. Dangi R, Lalwani P (2023) Harris hawks optimization based hybrid deep learning model for efﬁcient
network slicing in 5g network. Cluster Comput:1–15
49. Alzubaidi L, Zhang J, Humaidi AJ, Al-Dujaili A, Duan Y , Al-Shamma O, Santamaría J, Fadhel MA, Al-
Amidie M, Farhan L (2021) Review of deep learning: concepts, cnn architectures, challenges, applications,
future directions. J big Data 8:1–74
50. V arshney RP , Sharma DK A novel deep learning framework with stacked bi-directional long-short term
memory and cnn with enhanced adaptive moment optimizer and error correction strategy for predicting
time-series data. Available at SSRN 4209096
51. Dangi R, Lalwani P , Mishra MK (2023) 5g network trafﬁc control: a temporal analysis and forecasting
of cumulative network activity using machine learning and deep learning technologies. Int J Ad Hoc
Ubiquitous Comput 42(1):59–71
52. Dangi R, Lalwani P (2023) A novel hybrid deep learning approach for 5g network trafﬁc control and
forecasting. Concurr Comput Pract Exp 35(7):7596
123

A Deep Learning-Based Hybrid CNN-LSTM Model... Page 25 of 25 234
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional afﬁliations.
123
