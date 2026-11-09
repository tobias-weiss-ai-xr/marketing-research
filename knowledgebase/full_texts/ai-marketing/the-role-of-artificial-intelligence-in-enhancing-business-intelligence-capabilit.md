---
title: The Role of Artificial Intelligence in Enhancing Business Intelligence Capabilities for E-Commerce
  Platforms
url: https://doi.org/10.14569/ijacsa.2024.0150941
category: ai-marketing
subcategory: review
date: 2024-01
venue: International Journal of Advanced Computer Science and Applications
authors:
- Sinek Mehuli Br Perangin-Angin
- David Jumpa Malem Sembiring
- Asprina Br Surbakti
source: openalex-oa
pdf_url: https://thesai.org/Downloads/Volume15No9/Paper_41-The_Role_of_Artificial_Intelligence_in_Enhancing_Business_Intelligence.pdf
pages: 7
chars: 31576
fetched_at: '2026-11-08T19:32:50+00:00'
kb_version: 1
---

# The Role of Artificial Intelligence in Enhancing Business Intelligence Capabilities for E-Commerce Platforms

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 15, No. 9, 2024
416 | P a g e
www.ijacsa.thesai.org
The Role of Artificial Intelligence in Enhancing
Business Intelligence Capabilities for E-Commerce
Platforms
Sinek Mehuli Br Perangin-Angin1*, David Jumpa Malem Sembiring2, Asprina Br Surbakti3, Soleh Darmansyah4
Institut Teknologi Dan Bisnis Indonesia, Medan, Indonesia1, 2, 3
Faculty of Engineering, Universitas Medan Area, Medan, Indonesia4

Abstract—This research focuses on the application of BERT
(Bidirectional Encoder Representations from Transformers) and
Graph Neural Networks (GNNs) to improve busin ess intelligence
(BI) capabilities on e -commerce platforms. The main aim of the
research is to develop automation methods for the classification of
customer interactions and to create a more effective product
recommendation system. In this study, BERT was used to analyze
and classify customer interaction texts, including questions,
complaints, and reviews, with accuracy reaching 97% and
sentiment analysis accuracy of 93%. GNNs are applied to model
complex relationships between customers and products based o n
transaction data, then used to provide product recommendations.
The evaluation results show that the GNNs model achieved a mean
average precision (MAP) of 0.92 and a normalized discounted
cumulative gain (NDCG) of 0.88, indicating high relevance and
accuracy in product recommendations. This research concludes
that the integration of BERT and GNNs improves operational
efficiency through classification automation but also provides
added value in marketing strategies with better personalization of
recommendations.
Keywords—Bidirectional Encoder Representations from
Transformers (BERT); Graph Neural Networks  (GNNs); business
intelligence; e-commerce; product recommendation
I. INTRODUCTION
In recent years, the e-commerce industry has experienced a
significant surge in growth, resulting in the generation of vast
and intricate amounts of data  [1]. This dataset contains
comprehensive information regarding customer transactions,
shopping patterns, customer engagements, and more relevant
data. In order to stay compe titive, e-commerce platforms must
create advanced business intelligence (BI) systems to evaluate
this data and extract practical insights. In this situation, it is
critical to enhance business intelligence (BI) skills using
artificial intelligence (AI) technology [2], [3].
Bidirectional Encoder Representations from Transformers
(BERT) and Graph Neural Networks (GNNs) are two advanced
AI algorithms that have the potential to greatly improve
business intelligence capabilities for e -commerce systems  [4-
6]. Google created the sophisticated transformer model known
as BERT. This paradigm has transformed the field of natural
language processing (NLP) because of its ability to comprehend
bidirectional context in text. Natural language processing tasks
such as natural language interpretation, text classification, and
information retrieval can all benefit from the versatile
application of BERT  [7], [8]. BERT can enhance the study of
customer interaction in e -commerce. By leveraging its
advanced capabilities in comprehe nding conversations and
context, BERT has the potential to enhance customer service by
delivering more prompt and tailored assistance  [9]. Graph
Neural Networks (GNNs) represent a distinct class of neural
networks designed to process and analyze data struc tured in a
graph format. This algorithm is highly efficient at analyzing
intricate linkages and interactions among diverse elements. By
representing products, customers, and transactions as graphs,
we can employ Graph Neural Networks (GNNs) to detect
intricate patterns and correlations in e-commerce. This is highly
beneficial for constructing more precise and pertinent product
suggestion systems by utilizing data on the correlation between
products and client preferences [10-13].
The objective of this study is to investigate the utilization of
BERT and GNNs in enhancing business intelligence
capabilities on e-commerce platforms [14]. This research aims
to analyze customer interactions and make product
recommendations, with the goal of gaining new insights in to
how artificial intelligence (AI) can enhance customer
experience and boost business performance in the e -commerce
industry [15]. It also seeks to evaluate the effectiveness of
different algorithms in real-world situations, offering guidance
for implemen ting improved business intelligence (BI) in the
future [16].
II. RESEARCH METHODOLOGY
A. Methodology
The research commences by examining consumer
interactions utilizing the BERT (Bidirectional Encoder
Representations from Transformers) paradigm [17]. The initial
stage is gathering conversational text data, reviews, and client
inquiries from e -commerce platforms. Subsequently, this data
undergoes pre -processing to eliminate any unwanted
interference and make it ready for subsequent analysis. BERT
models undergo fine-tuning with these datasets to perform tasks
like text categorization and comprehension of conversational
context, resulting in more profound characteristics and a better
grasp of consumer preferences and requirements [18].
Following the study using BERT,  the research proceeds by
constructing an association graph between customers and items
with graph neural networks (GNNs)  [19]. Graphs are
constructed using transaction data and BERT analysis

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 15, No. 9, 2024
417 | P a g e
www.ijacsa.thesai.org
outcomes to depict intricate connections among entities. Graph
Neural Networks (GNNs) are subsequently utilized to represent
and examine relationship patterns inside these graphs, with a
specific emphasis on producing precise and pertinent product
recommendations [20], [21].
Performance evaluations are conducted by utilizing metrics
like precision, recall, F1 -score, and NDCG (normalized
discounted cumulative gain) to assess the efficiency of the
recommendation model [22]. The outcomes of these two phases
are merged to offer a more all -encompassing business
intelligence solution and enhance the e -commerce platform's
abilities in comprehending and catering to its customers can be
seen in Fig. 1.

Fig. 1. Research methodology.
B. Problem Solving Approach
1) Artificial Intelligence (AI) in Business Intelligence (BI) for
e-commerce: Artificial intelligence (AI) plays a crucial role in
advancing business intelligence (BI) systems  [23]. Within the
realm of electronic commerce, business intelligence (BI)
converts unprocessed data, including sales transactions,
customer activity, and user interactions, into significant insights
that influence company decision -making [24]. By integrating
artificial intelligence (AI), business intelligence (BI) systems
may analyze vast quantities of data, uncover concealed patterns,
and offer highly precise, pred icted insights. This integration
significantly improves an e -commerce platform's capacity to
comprehend and cater to its clients in a more efficient manner
[25].
2) Bidirectional Encoder Representations from
Transformers (BERT) : BERT possesses the capacity to
comprehend bidirectional context in text, enabling it to
analyze words in sentence context from both the left -to-right
and right -to-left orientations. These tasks, such as text
classification, information retrieval, and natural language
understanding, are particularly crucial  [26]. In the realm of e -
commerce, BERT is employed to scrutinize client
interactions, including product evaluations and dialogues with
customer care, to extract profound insights into customer
requirements and inclin ations. Utilizing this comprehension
of consumer interactions helps enhance customer service and
customization. Below are the sequential instructions for
utilizing BERT.  The following main components underlie
BERT [27-30]:
Phase 1→ Input Embeddings
𝑚𝑏𝑒𝑑𝑑𝑖𝑛𝑔 (𝑥𝑖) = 𝑇𝑜𝑘𝑒𝑛𝐸𝑚𝑏𝑒𝑑𝑑𝑖𝑛𝑔 (𝑥𝑖) +
𝐸𝑆𝑒𝑔𝑚𝑒𝑛𝑡𝐸𝑚𝑏𝑒𝑑𝑑𝑖𝑛𝑔 (𝑥𝑖) + 𝑃𝑜𝑠𝑖𝑡𝑖𝑜𝑛𝐸𝑚𝑏𝑒𝑑𝑑𝑖𝑛𝑔 (𝑥𝑖) (1)
Phase 2 → Self-Attention Mechanism
BERT's key component self -attention allows the model to
focus on different parts of the input sequence when processing
each token.
Scaled Dot-Product Attention
𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛(𝑄, 𝐾, 𝑉) = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 ( 𝑄𝐾𝑇
√𝑑𝑘
) 𝑉     (2)
Where:
𝑄 query matrix
𝐾 key matrix
𝑉 value matrix
𝑑𝑘 dimensions of the key
Multi-Head Attention
𝑀𝑢𝑙𝑡𝑖𝐻𝑒𝑎𝑑(𝑄, 𝐾, 𝑉) =
𝐶𝑜𝑛𝑐𝑎𝑡(ℎ𝑒𝑎𝑑1, ℎ𝑒𝑎𝑑2, … , ℎ𝑒𝑎𝑑ℎ)𝑊𝑂 (3)
Where:
ℎ𝑒𝑎𝑑𝑖 = 𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛(𝑄𝑊𝑖 𝑄, 𝐾𝑊𝑖 𝐾, 𝑉𝑊𝑖 𝑉)
𝑊𝑖 𝑄, 𝑊𝑖 𝐾, 𝑊𝑖 𝑉 weight matrix for the 𝑖 th head
𝑊𝑂 output weight matrix
Phase 3 → Feed-Forward Neural Network
𝐹𝐹𝑁(𝑥) = max(0, 𝑥𝑊1 + 𝑏1) 𝑊2 + 𝑏2     (4)
Phase 4 → Layer Normalization
𝐿𝑎𝑦𝑒𝑟𝑁𝑜𝑟𝑚(𝑥) = 𝑥−𝐸[𝑥] √𝑉𝑎𝑟[𝑥]+𝜖 . 𝛾 + 𝛽 (5)
Where:
𝐸[𝑥] the average value of the input
𝑉𝑎𝑟[𝑥] variance of the input
𝜖 small constant to prevent division by zero
(6)

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 15, No. 9, 2024
418 | P a g e
www.ijacsa.thesai.org
𝛾 and 𝛽 parameters that can be studied
Phase 5 → Loss Function
𝐿𝑜𝑠𝑠 = − ∑ 𝑖 ∈ 𝑚𝑎𝑠𝑘𝑒𝑑 𝑝𝑜𝑠𝑖𝑡𝑖𝑜𝑛𝑠 𝐿𝑜𝑔𝑃(𝑥𝑖|𝑥<𝑖, 𝑥>𝑖)    (6)
Phase 6 →Training Objective
BERT is trained in masked language modeling (MLM) and
next sentence prediction (NSP).
Masked Language Modelling (MLM)
𝑀𝐿𝑀 𝐿𝑜𝑠𝑠
= − ∑ 𝑖 ∈ 𝑚𝑎𝑠𝑘𝑒𝑑 𝑝𝑜𝑠𝑖𝑡𝑖𝑜𝑛𝑠 𝐿𝑜𝑔𝑃 (𝑥𝑖|𝑥𝑚𝑎𝑠𝑘𝑒𝑑)   (7)
Next Sentence Prediction (NSP)
The model is trained to predict whether two input sentences
appear sequentially in the original text.
𝑁𝑆𝑃 𝐿𝑜𝑠𝑠 = −(𝑦 log 𝑃 (𝐼𝑠𝑁𝑒𝑥𝑡)
+(1 − 𝑦) log 𝑃(𝑁𝑜𝑡𝑁𝑒𝑥𝑡))  (8)
Where 𝑦 Binary labels indicate whether two sentences are
sequential or not.
3) Graph Neural Networks (GNNs) : Graph neural networks
(GNNs) proficiently examine intricate connections and
interactions among diverse elements. Graphs consist of nodes
that can represent various entities, such as consumers and items
[31]. The connections between these entities, such as buy
transactions, are represented by edges. Graph Neural Networks
(GNNs) hav e the ability to acquire knowledge about these
graphs and are employed for tasks such as predicting
connections (e.g., suggesting products) and categorizing nodes.
E-commerce platforms can enhance the precision and relevance
of their product recommendation  algorithms by leveraging
graph neural networks (GNNs) to analyze intricate relationship
patterns between products and customers [32-34].
Phase 1 → Graph Representation
Graf 𝐺 defined as a pair (𝑉, 𝐸), where 𝑉 is the set of nodes
and 𝐸 is a set of edges.
Phase 2 → Basic Notation
ℎ𝑢 Features of neighboring nodes 𝑢
𝑊 Learnable weight matrix
𝜎 Non-linear activation function
𝑁(𝑣) Set of neighbors of node 𝑣
Phase 3 → Propagation Rule
General Message -Passing Framework
ℎ𝑣 𝑘 = 𝜎(𝑊𝑘. 𝐴𝐺𝐺𝑅𝐸𝐺𝐴𝑇𝐸𝑘({ℎ𝑢 𝑘−1: 𝑢𝜖𝑁(𝑣)}))   (9)
Phase 4 → Output Layers
After the propagation layer, the node representation is
updated and ready to be used in predictions
C. Data Classification and Analysis
The primary data consists of customer interactions, product
transactions, product details, and relationship networks
connecting customers and products. We evaluate customer
contact data, including chats, reviews, and feedback, using the
BERT model to gain a comprehensive understanding of
customer preferences and wa nts [35]. We utilize data on
product transactions, including client purchases, to construct
graphs that illustrate the correlation between customers and
products. Product information, such as category and price,
enhances the feature nodes in the network. G raph neural
networks (GNNs) subsequently examine the graph representing
the link between customers and products to identify intricate
relationship patterns and deliver precise product suggestions.
The analysis procedure entails extracting features, gatheri ng
information from neighboring nodes in the network, and using
a non -linear activation function to generate node
representations [36] that can be seen in Table I.
TABLE I. NODE REPRESENTATIONS
Data Type Description Analysis Method Objective
Customer
Interaction
Customer
conversations,
reviews and
feedback.
BERT
Understand
customer
preferences and
needs
Product
Transactions
Information about
product purchases
by customers.
Transaction
Analysis
and GNSs
Building
customer-product
relationship graphs
and pattern
analysis.
Product
Information
Product details
include category
and price.
Data
Enrichment
& GNNs
Node features in a
graph.
Relationship
Graph
Graph
representation of the
relationship
between customers
and products based
on transactions.
Graph
Neural
Networks
(GNNs)
Detect relationship
patterns and
product
recommendations.
III. RESULT AND DISCUSSION
Data in Tables II, III and IV include customer interactions,
product transactions, product information, as well as additional
features used in the customer -product relationship graph  and
data in Tables V, VI and VII  include information for analysis,
from customer interactions to product transactions and
relationship graphs. Each parameter in the data, such as Text
Length, Transaction Frequency, Edge Weight, and Node
Features, provides context for understanding how customers
interact with products on an e -commerce platform. This data
provides the basis for in -depth analysis and implementation of
algorithms to improve Business Intelligence on e -commerce
platforms.

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 15, No. 9, 2024
419 | P a g e
www.ijacsa.thesai.org
TABLE II. CUSTOMER INTERACTION DATA
Interaction ID Customer ID Text
1 101 "What is the return policy for this item?"
2 102 "Do you have this product in size M?"
3 103 "How long does shipping take?"
4 104 "Can I change my order after placing it?"
5 105 "Are there any discounts available?"
6 106 "I received a damaged item, what should I do?"
7 107 "Is this product available in other colours?"
8 108 "I need help with tracking my order."
9 109 "Can I get a refund for this purchase?"
10 110 "What is the warranty period for this product?"
TABLE III. PRODUCT TRANSACTION DATA
Transaction
ID
Customer
ID
Product
ID Quantity Transaction Frequency Purchase Variety
1 101 1001 2 3 2
2 102 1002 1 1 1
3 103 1003 3 4 2
4 104 1004 1 2 1
5 105 1005 2 3 1
6 101 1006 1 3 2
7 102 1007 1 1 1
8 103 1008 1 4 2
9 104 1009 1 2 1
10 105 1010 2 3 1
TABLE IV. PRODUCT INFORMATION DATA
Product
ID
Product
Name Category Price Stock Availability Product Ratings
1001 T-shirt Clothing 20 In Stock 4.5
1002 Running Shoes Footwear 50 In Stock 4.7
1003 Leather Jacket Clothing 100 Out of Stock 4.6
1004 Smartwatch Electronics 150 In Stock 4.8
1005 Wireless Earbuds Electronics 30 In Stock 4.4
1006 Backpack Accessories 40 In Stock 4.3
1007 Sunglasses Accessories 25 In Stock 4.5
1008 Laptop Electronics 500 In Stock 4.9
1009 Office Chair Furniture 200 Out of Stock 4.6
1010 Water Bottle Accessories 15 In Stock 4.2
TABLE V. NODES (CUSTOMERS AND PRODUCTS)
Node
ID Type Age Gender Category Price Product Ratings
101 Customer 25 Male - - -
102 Customer 30 Female - - -
103 Customer 22 Male - - -
104 Customer 28 Female - - -
105 Customer 35 Male - - -
1001 Product - - Clothing 20 4.5
1002 Product - - Footwear 50 4.7
1003 Product - - Clothing 100 4.6
1004 Product - - Electronics 150 4.8
1005 Product - - Electronics 30 4.4
TABLE VI. EDGES (TRANSACTIONS)
Source
Node
Target
Node
Transaction
ID Quantity Edge Weight
101 1001 1 2 40
102 1002 2 1 50
103 1003 3 3 300
104 1004 4 1 150
105 1005 5 2 60
TABLE VII. NODE FEATURES
Node ID Feature 1 Feature 2
101 Age: 25 Gender: Male
102 Age: 30 Gender: Female
103 Age: 22 Gender: Male
104 Age: 28 Gender: Female
105 Age: 35 Gender: Male
1001 Category: Clothing Price: 20
1002 Category: Footwear Price: 50
1003 Category: Clothing Price: 100
1004 Category: Electronics Price: 150
1005 Category: Electronics Price: 30
A. Data Processing Results with BERT
Most customers ask about return policies, product
availability, and shipping information. This indicates areas
need to be clarified on e -commerce sites to reduce customer
service burden. Complaints about damaged goods and requests
for refunds were most common, indicating a need to improve
delivery quality and return policies. BERT successfully
classifies customer interaction texts into relevant categories
with a high level of confi dence. This allows e -commerce
platforms to automatically handle various types of customer
inquiries or complaints more efficiently, shown in Table VIII.

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 15, No. 9, 2024
420 | P a g e
www.ijacsa.thesai.org
TABLE VIII. CUSTOMER INTERACTION ANALYSIS (TEXT CLASSIFICATION)
Interaction
ID
Customer
ID Text Predicted Class Confidence Score
1 101
"What is the
return policy
for this
item?"
Inquiry:
Return
Policy
0.98
2 102
"Do you have
this product
in size M?"
Inquiry:
Product
Availability
0.95
3 103
"How long
does shipping
take?"
Inquiry:
Shipping
Information
0.97
4 104
"Can I change
my order
after placing
it?"
Inquiry:
Order
Modification
0.96
5 105
"Are there
any discounts
available?"
Inquiry:
Discounts 0.93
6 106
"I received a
damaged
item, what
should I do?"
Complaint:
Damaged
Item
0.99
7 107
"Is this
product
available in
other
colours?"
Inquiry:
Product
Availability
0.95
8 108
"I need help
with tracking
my order."
Inquiry:
Order
Tracking
0.94
9 109
"Can I get a
refund for
this
purchase?"
Request:
Refund 0.97
10 110
"What is the
warranty
period for this
product?"
Inquiry:
Warranty
Information
0.96
B. Data Processing Results with GNNs
GNNs identify purchasing patterns and provide relevant
product recommendations for each customer. These
recommendations are based on historical relationships between
products frequently purchased together by other customers with
similar purchasing patterns as in the Table IX.
TABLE IX. CUSTOMER SEGMENTATION ANALYSIS
Segment Characteristics Actionable Insights
High-Value
Customers
Customers who buy
products at high prices
Focus on personalizing
premium product offerings
Frequent
Buyers
Customers with high
purchasing frequency
Loyalty offers or discounts
based on volume
Category
Loyalists
Customers who tend to buy
from one category
Promote related products
in the same category
IV. VALIDATION
A. Performance Evaluation of BERT
BERT is used for customer interaction text classification.
Performance evaluation is measured using several metrics [37],
[38].
𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 = (
𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑐𝑜𝑟𝑟𝑒𝑐𝑡 𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛𝑠
𝑇𝑜𝑡𝑎𝑙 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛𝑠 )  (10)
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 =
𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠 (𝑇𝑃)
𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠 (𝑇𝑃)+𝐹𝑎𝑙𝑠𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠 (𝐹𝑃) (11)
𝑅𝑒𝑐𝑎𝑙𝑙 =
𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠 (𝑇𝑃)
𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒𝑠 (𝑇𝑃)+𝐹𝑎𝑙𝑠𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒𝑠 (𝐹𝑁) (12)
𝐹1 − 𝑆𝑐𝑜𝑟𝑒 = 2 ×
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 ×𝑅𝑒𝑐𝑎𝑙𝑙
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙      (13)
Table X shows BERT provides excellent results in text
classification and sentiment analysis, with high scores in all key
metrics. This reflects BERT's ability to effectively understand
and process customer interaction texts for customer service
automation and data -driven decision making in e -commerce
platforms.
TABLE X. BERT PERFORMANCE EVALUATION
Evaluation
Metrics Value Interpretation
Accuracy 97%
97% of BERT's total predictions were correct,
demonstrating a high level of accuracy in customer
interaction text classification.
Precision 0.95
95% of the positive predictions made by BERT
were true positive, indicating that this model has a
low false positive rate.
Recall 0.96
BERT successfully identified 96% of all existing
positive cases, indicating that the model is very
good at detecting the correct classes.
F1-Score 0.96 A harmonious combination of Precision and Recall, showing a good balance between the two.
Sentiment
Analysis
Accuracy
93%
BERT was able to classify sentiment with 93%
accuracy, demonstrating reliability in determining
whether text is positive, negative, or neutral.
B. Performance Evaluation of GNNs
GNNs are used for tasks such as product recommendation
and customer -product relationship graph analysis. Its
performance evaluation is measured using metrics such as
Mean Average Precision (MAP) and Normalized Discounted
Cumulative Gain (NDCG) [39]:
MAP
𝑀𝐴𝑃 =
1
2 ∑ 𝐴𝑃(𝑖)𝑛 𝑖=1   (14)
NDCG
𝐷𝐶𝐺𝑝 = ∑
2𝑖 𝑟𝑒𝑙−1
log2(𝑖+1)
𝑝
𝑖=1   (15)
𝑁𝐷𝐶𝐺𝑝 =
𝐷𝐶𝐺𝑝
𝐼𝐷𝐶𝐺𝑝
   (16)
Precision@K
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛@𝐾
=
𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑟𝑒𝑙𝑒𝑣𝑎𝑛𝑡 𝑖𝑡𝑒𝑚𝑠 𝑖𝑛 𝐾 𝑟𝑒𝑐𝑜𝑚𝑚𝑒𝑛𝑑𝑎𝑡𝑖𝑜𝑛𝑠
𝐾  (17)

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 15, No. 9, 2024
421 | P a g e
www.ijacsa.thesai.org
TABLE XI. GNNS PERFORMANCE EVALUATION
Evaluation
Metrics Value Interpretation
Mean Average
Precision (MAP) 0.92
92% of the products recommended by
GNNs are relevant and match customer
preferences.
Normalized
Discounted
Cumulative Gain
(NDCG)
0.88
Relevant recommendations tend to appear at
the top of the recommendation list,
increasing the likelihood of a product being
chosen by a customer.
Precision@5 0.93 93% of the top five recommendations are relevant to customers.
Precision@10 0.89 89% of the top ten recommendations are relevant to customers.
Coverage 85%
GNNs cover 85% of the products in the
catalogue, ensuring diverse and varied
recommendations.
Hit Rate 0.90
90% of all customers find at least one
relevant product in their recommendation
list.
V. CONCLUSION
This research reveals how the use of BERT (Bidirectional
Encoder Representations from Transformers) and Graph
Neural Networks (GNNs) can improve business intelligence
(BI) capabilities on e -commerce platforms. Through in -depth
analysis, BERT was proven to be effective in classi fying
customer interaction texts with an accuracy rate of 97% and was
able to perform sentiment analysis with an accuracy rate of
93%. This enables automation in the management of customer
inquiries and complaints, directly increasing customer service
efficiency. GNNs show good performance in providing relevant
product recommendations, with a mean average precision
(MAP) of 0.92 and a normalized discounted cumulative gain
(NDCG) of 0.88. GNNs also managed to cover 85% of the
products in the catalog, ensurin g that the recommendations
provided were varied. Customer segmentation generated by
GNNs allows the identification of segments such as high-value
customers and frequent buyers, which can be targeted with
more precise marketing strategies, increasing campai gn
effectiveness and customer loyalty.
REFERENCES
[1] Alsmadi, A. Shuhaiber, M. Al -Okaily, A. Al -Gasaymeh, and N.
Alrawashdeh, “Big data analytics and innovation in e-commerce: current
insights and future directions,” Journal of Financial Services Marketing,
May 2023, doi: 10.1057/s41264-023-00235-7.
[2] R. B. Y. Syah, H. Satria, M. Elveny, and M. K. M. Nasution, “Complexity
prediction model: a model for multi-object complexity in consideration to
business uncertainty problems,” Bulletin of Electrical Engineering a nd
Informatics, vol. 12, no. 6, pp. 3697 –3705, Dec. 2023, doi:
10.11591/eei.v12i6.5380.
[3] Y. Yang, N. Chen, and H. Chen, “The Digital Platform, Enterprise Digital
Transformation, and Enterprise Performance of Cross -Border E -
Commerce—From the Perspective of D igital Transformation and Data
Elements,” Journal of Theoretical and Applied Electronic Commerce
Research, vol. 18, no. 2, pp. 777 –794, Mar. 2023, doi:
10.3390/jtaer18020040.
[4] Z. Yu et al., “Embedding text -rich graph neural networks with sequence
and topical semantic structures,” Knowl Inf Syst, vol. 65, no. 2, pp. 613–
640, Feb. 2023, doi: 10.1007/s10115-022-01768-4.
[5] S. Fan et al., “BOMGraph: Boosting Multi-scenario E-commerce Search
with a Unified Graph Neural Network,” in Proceedings of the 32nd ACM
International Conference on Information and Knowledge Management,
New York, NY, USA: ACM, Oct. 2023, pp. 514 –523. doi:
10.1145/3583780.3614794.
[6] T. Jiang, W. Sun, and M. Wang, “MSGAT-Based Sentiment Analysis for
E-Commerce,” Information, vol. 14, no. 7, p. 416, Jul. 2023, doi:
10.3390/info14070416.
[7] I. Karabila, N. Darraz, A. EL -Ansari, N. Alami, and M. EL Mallahi,
“BERT-enhanced sentiment analysis for personalized e -commerce
recommendations,” Multimed Tools Appl, vol. 83, no. 19, pp. 56463 –
56488, Dec. 2023, doi: 10.1007/s11042-023-17689-5.
[8] Y. Xiong, N. Wei, K. Qiao, Z. Li, and Z. Li, “Exploring Consumption
Intent in Live E -Commerce Barrage: A Text Feature -Based Approach
Using BERT-BiLSTM Model,” IEEE Access, vol. 12, pp. 69288–69298,
2024, doi: 10.1109/ACCESS.2024.3399095.
[9] W. Chang and M. Zhu, “Sentiment analysis method of consumer
comment text based on BERT and hierarchical attention in e -commerce
big data environment,” Journal of Intelligent Systems, vol. 32, no. 1, Dec.
2023, doi: 10.1515/jisys-2023-0025.
[10] S. Zhou and N. S. Hudin, “Advancing e -commerce user purchase
prediction: Integration of time -series attention with event -based
timestamp encoding and Graph Neural Network -Enhanced us er
profiling,” PLoS One, vol. 19, no. 4, p. e0299087, Apr. 2024, doi:
10.1371/journal.pone.0299087.
[11] L. Zheng, Z. Li, J. Gao, Z. Li, J. Wu, and C. Zhou, “Domain Adaptation
for Anomaly Detection on Heterogeneous Graphs in E-Commerce,” 2023,
pp. 304–318. doi: 10.1007/978-3-031-28238-6_20.
[12] G. Xv et al., “E -commerce Search via Content Collaborative Graph
Neural Network,” in Proceedings of the 29th ACM SIGKDD Conference
on Knowledge Discovery and Data Mining, New York, NY, USA: ACM,
Aug. 2023, pp. 2885–2897. doi: 10.1145/3580305.3599320.
[13] Z. Wen, “Generalizing Graph Neural Network across Graphs and Time,”
in Proceedings of the Sixteenth ACM International Conference on Web
Search and Data Mining, New York, NY, USA: ACM, Feb. 2023, pp.
1214–1215. doi: 10.1145/3539597.3572986.
[14] X. Zhang, F. Guo, T. Chen, L. Pan, G. Beliakov, and J. Wu, “A Brief
Survey of Machine Learning and Deep Learning Techniques for E -
Commerce Research,” Journal of Theoretical and Applied Electronic
Commerce Research, vol. 18, no. 4, pp. 2188 –2216, Dec. 2023, doi:
10.3390/jtaer18040110.
[15] N. A. Sharma, A. B. M. S. Ali, and M. A. Kabir, “A review of sentiment
analysis: tasks, applications, and deep learning techniques,” Int J Data Sci
Anal, Jul. 2024, doi: 10.1007/s41060-024-00594-x.
[16] X. Guo et al., “Int elligent online selling point extraction and generation
for e‐commerce recommendation,” AI Mag, vol. 44, no. 1, pp. 16 –29,
Mar. 2023, doi: 10.1002/aaai.12083.
[17] P. Radanliev, “Artificial intelligence: reflecting on the past and looking
towards the next paradigm shift,” Journal of Experimental & Theoretical
Artificial Intelligence, pp. 1 –18, Feb. 2024, doi:
10.1080/0952813X.2024.2323042.
[18] T. Vo, “A Novel Semantic -Enhanced Text Graph Representation
Learning Approach through Transformer Paradigm,” Cybern Syst, vo l.
54, no. 4, pp. 499–525, May 2023, doi: 10.1080/01969722.2022.2067632.
[19] C. Gao et al., “A Survey of Graph Neural Networks for Recommender
Systems: Challenges, Methods, and Directions,” ACM Transactions on
Recommender Systems, vol. 1, no. 1, pp. 1 –51, Mar.  2023, doi:
10.1145/3568022.
[20] D. Wu, Q. Wang, and D. L. Olson, “Industry classification based on
supply chain network information using Graph Neural Networks,” Appl
Soft Comput, vol. 132, p. 109849, Jan. 2023, doi:
10.1016/j.asoc.2022.109849.
[21] E. E. Kosasih,  F. Margaroli, S. Gelli, A. Aziz, N. Wildgoose, and A.
Brintrup, “Towards knowledge graph reasoning for supply chain risk
management using graph neural networks,” Int J Prod Res, vol. 62, no.
15, pp. 5596–5612, Aug. 2024, doi: 10.1080/00207543.2022.2100841.
[22] H. Brama, L. Dery, and T. Grinshpoun, “Evaluation of neural networks
defenses and attacks using NDCG and reciprocal rank metrics,” Int J Inf
Secur, vol. 22, no. 2, pp. 525–540, Apr. 2023, doi: 10.1007/s10207-022-
00652-0.

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 15, No. 9, 2024
422 | P a g e
www.ijacsa.thesai.org
[23] C. Wang et al., “An empirical evaluation of technology acceptance model
for Artificial Intelligence in E -commerce,” Heliyon, vol. 9, no. 8, p.
e18349, Aug. 2023, doi: 10.1016/j.heliyon.2023.e18349.
[24] S. J, Ch. Gangadhar, R. K. Arora, P. N. Renjith, J. Bamini, and Y. devidas
Chincholkar, “E -commerce customer churn prevention using machine
learning-based business intelligence strategy,” Measurement: Sensors,
vol. 27, p. 100728, Jun. 2023, doi: 10.1016/j.measen.2023.100728.
[25] M. Azmi, A. Mansour, and C. Azmi, “A Context -Aware Empowering
Business with AI: Case of Chatbots in Business Intelligence Systems,”
Procedia Comput Sci, vol. 224, pp. 479 –484, 2023, doi:
10.1016/j.procs.2023.09.068.
[26] M. Elveny, R. B. Y. Syah, and M. K. M. Nasution, “An boosting business
intelligent to customer lifetime value w ith robust M -estimation,” IAES
International Journal of Artificial Intelligence (IJ -AI), vol. 13, no. 2, p.
1632, Jun. 2024, doi: 10.11591/ijai.v13.i2.pp1632-1639.
[27] H. Murfi, Syamsyuriani, T. Gowandi, G. Ardaneswari, and S. Nurrohmah,
“BERT-based combination of convolutional and recurrent neural network
for indonesian sentiment analysis,” Appl Soft Comput, vol. 151, p.
111112, Jan. 2024, doi: 10.1016/j.asoc.2023.111112.
[28] K. Taneja, J. Vashishtha, and S. Ratnoo, “Transformer Based
Unsupervised Learning Approac h for Imbalanced Text Sentiment
Analysis of E-Commerce Reviews,” Procedia Comput Sci, vol. 235, pp.
2318–2331, 2024, doi: 10.1016/j.procs.2024.04.220.
[29] M. Elveny, M. K. M. Nasution, and R. B. Y. Syah, “A Hybrid
Metaheuristic Model for Efficient Analytical B usiness Prediction,”
International Journal of Advanced Computer Science and Applications,
vol. 14, no. 8, 2023, doi: 10.14569/IJACSA.2023.0140848.
[30] S. Gheewala, S. Xu, S. Yeom, and S. Maqsood, “Exploiting deep
transformer models in textual review based reco mmender systems,”
Expert Syst Appl, vol. 235, p. 121120, Jan. 2024, doi:
10.1016/j.eswa.2023.121120.
[31] K. Sharma et al., “A Survey of Graph Neural Networks for Social
Recommender Systems,” ACM Comput Surv, vol. 56, no. 10, pp. 1 –34,
Oct. 2024, doi: 10.1145/3661821.
[32] X. Li, L. Sun, M. Ling, and Y. Peng, “A survey of graph neural network
based recommendation in social networks,” Neurocomputing, vol. 549, p.
126441, Sep. 2023, doi: 10.1016/j.neucom.2023.126441.
[33] Y. Mahendra and B. Bolla , “Unveiling the power of knowledge graph
embedding in knowledge aware deep recommender systems for e -
commerce: A comparative study,” Procedia Comput Sci, vol. 235, pp.
1364–1375, 2024, doi: 10.1016/j.procs.2024.04.128.
[34] G. Stalidis et al., “Recommendation Systems for e-Shopping: Review of
Techniques for Retail and Sustainable Marketing,” Sustainability, vol. 15,
no. 23, p. 16151, Nov. 2023, doi: 10.3390/su152316151.
[35] B. Khemani, S. Patil, K. Kotecha, and S. Tanwar, “A review of graph
neural networks: concepts, architectures, techniques, challenges, datasets,
applications, and future directions,” J Big Data, vol. 11, no. 1, p. 18, Jan.
2024, doi: 10.1186/s40537-023-00876-4.
[36] Y. Chen et al., “SP -GNN: Learning structure and position information
from graphs,” Neural Networks, vol. 161, pp. 505 –514, Apr. 2023, doi:
10.1016/j.neunet.2023.01.051.
[37] A. Bello, S.-C. Ng, and M.-F. Leung, “A BERT Framework to Sentiment
Analysis of Tweets,” Sensors, vol. 23, no. 1, p. 506, Jan. 2023, doi:
10.3390/s23010506.
[38] R. B. Y. Syah, R.  Muliono, M. Akbar Siregar, and M. Elveny, “An
efficiency metaheuristic model to predicting customers churn in the
business market with machine learning -based,” IAES International
Journal of Artificial Intelligence (IJ-AI), vol. 13, no. 2, p. 1547, Jun. 2024,
doi: 10.11591/ijai.v13.i2.pp1547-1556.
[39] H. Yang and T. Gonçalves, “Field features: The impact in learning to rank
approaches,” Appl Soft Comput, vol. 138, p. 110183, May 2023, doi:
10.1016/j.asoc.2023.110183.
