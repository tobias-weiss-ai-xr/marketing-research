---
title: A study on evaluating the effectiveness of cross-border e-commerce digital marketing based on deep
  learning
url: https://doi.org/10.1007/s43926-026-00529-x
category: analytics
subcategory: measurement
date: 2026-10
venue: Discover Internet of Things
authors:
- Xi Chen
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s43926-026-00529-x.pdf
pages: 33
chars: 99385
fetched_at: '2026-11-08T18:08:12+00:00'
kb_version: 1
---

# A study on evaluating the effectiveness of cross-border e-commerce digital marketing based on deep learning

Discover Internet of ThingsChen Discover Internet of Things           (2026) 6:225
https://doi.org/10.1007/s43926-026-00529-x
RESEARCH Open Access
A study on evaluating the effectiveness
of cross-border e-commerce digital marketing
based on deep learning
Xi Chen1*
  * C o r r e s p o n d e n c e :
Xi Chen
15896429975@163.com
1Jiangsu College of Safety
Technology, Xuzhou 221000,
Jiangsu, China
© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p :  / / c r e a  t i v e c  o m m o  n s . o r g / l i c e n s
e s / b y - n c - n d / 4 . 0 /     .
Abstract
Businesses looking to broaden their consumer base and access overseas markets
are realizing the importance of cross-border e-commerce as the landscape of
international trade changes. In an increasingly globalized e-commerce landscape,
organizations are grappling with the challenge of tailoring digital marketing tactics
to specific nations and client bases. Continued success in international e-commerce
necessitates digital marketing strategies that can adjust to local tastes and market
conditions. Combining deep learning with quantum computing, the study suggests
Quantum Fusion Deep Learning for Cross-Border Digital Marketing Analytics (QFDL-
CBDMA) to enhance the assessment of digital marketing campaigns. Quantum Fusion
Neural Networks (QF-NNs) are an integral part of this approach; they use quantum
computing to enhance deep learning models that deal with high-dimensional,
multi-modal inputs. For better feature extraction and pattern recognition, the QF-NN
encodes complicated features into quantum states. This allows for quicker and more
effective analysis of data related to demographics, markets, and consumer behaviour.
To further improve the model, the Quantum Gradient Descent (QGD) optimization
method uses quantum computing to speed up training, leading to quicker
convergence and better predictions. QF-DL-CBMS offers adaptive marketing methods
that adjust to the ever-changing market, enhancing campaign targeting, consumer
engagement, and budget allocation. International e-commerce dataset verification
studies show that QF-DL-CBMS achieves a projected accuracy of over 98% and beats
competing approaches in ROI, customer engagement, and cross-cultural consumer
insights.
Keywords Deep learning, Quantum computing, Digital marketing analytics, Cross-
border e-commerce, Quantum fusion neural network, Quantum gradient descent
 1 Introduction
The widespread use of digital trade, the constant development of supply chain systems,
and the quick growth of worldwide marketplaces are all made possible by e-commerce
[1]. For businesses aiming to grow outside their immediate vicinity, digital platforms
are crucial in this age of lowered barriers to trade and shifting consumer tastes [ 2]. This

Page 2 of 33
Chen Discover Internet of Things            (2026) 6:225
shift in viewpoint exemplifies the way in which international trade through the internet
has revolutionized the global market[ 3]. The term "cross-border e-commerce" describes
commercial dealings that take place between countries using the Internet. Cross-bor -
der e-commerce enables enterprises to reach a global consumer base, unlike traditional
trade, which is constrained by geography.
International online sales depend heavily on client satisfaction [ 4], e-commerce, prod-
uct returns can affect consumer happiness, especially if the product doesn't meet expec -
tations [5]. Clothing and electronics products are prone to this kind of mismatch due to
discrepancies in sizing, description, and functionality. Customers typically tell 9 people
about their online service experiences; thus, a single unpleasant encounter might dis -
suade others from using e-commerce and bring a company down [ 6]. One of the biggest
obstacles for e-commerce companies is adapting digital marketing techniques to many
countries and regions, each with its own cultural, economic, and behavioral differences.
Due to the complexity of these situations, standard marketing methods fail to generate
much work and cash [7]. Therefore, models must be increasingly sophisticated and resil-
ient to adapt to the ever-changing digital economy. Marketing initiatives will be success-
ful and effective.
Businesses must find ways to appeal to a large audience while also meeting the inter -
ests, buying habits, and cultural differences of each location [ 8]. Further, companies
are unable to manually or with traditional analytics tools extract useful insights from
the massive consumer data on cross-border e-commerce platforms [ 9]. It increases
the need for advanced data analytics methods capable of handling multi-modal, com -
plex, and high-dimensional datasets. Only a few systems use deep learning and QC to
manage and analyze enormous volumes of data from various sources while taking cul -
tural and behavioural factors into consideration [ 10]. Global e-commerce is too com -
plex and fast-changing for present models. Market prediction and client segmentation
are their main focus [ 11]. Global digital marketing is ever-changing, thus more flexible
models that can manage complex, high-dimensional data are needed. DL and QC make
the proposed system unique and might alter numerous industries, including market -
ing analytics [ 12]. QFDL-CBDMA solves global digital retail advertising problems with
QC and DL. The QF-NN uses quantum computing to improve deep learning networks'
interpretation of high-dimensional, multi-modal data. This data covers demographics,
social media, and buying history. Through quantum encoding, the model can analyze
big datasets faster and improve feature extraction and pattern recognition. We can bet -
ter understand regional buying patterns, market trends, and cultural influences on cus -
tomer choices. The framework uses QGD, an optimization method based on quantum
computing, to hasten the training of deep learning models. QGD outperforms gradient
descent in terms of convergence speed and prediction accuracy. It eliminates or greatly
improves upon the likelihood of a local minimum and is much more efficient. With
QFDL-CBDMA, quantum computing can optimize the training of complicated, large-
scale deep learning models for use in real-time. The QFDL-CBDMA architecture is very
versatile in international online trade due to its ability to adapt to changing market con -
ditions. The framework allows businesses to stay ahead of the competition by adjusting
their marketing strategies in real-time based on consumer and market data. Interna -
tional internet commerce requires this adaptability because cultural trends, consumer
preferences, and market conditions can change quickly.

Page 3 of 33
Chen Discover Internet of Things            (2026) 6:225
The main contributions of the paper include.
  • The proposed QFDL-CBDMA method uses deep learning and quantum computing
to analyze multi-modal data in high-dimensional domains. In international online
commerce, the QF-NN increases feature extraction and pattern recognition, allowing
for more extensive analysis of complicated datasets including client demographics,
purchasing patterns, and regional market dynamics.
  • The recommended model employs the QGD optimization method, leveraging
quantum computing to accelerate convergence and improve predictive accuracy
during deep learning model training.
  • When tested on a worldwide e-commerce dataset, the QFDL-CBDMA framework
outperformed traditional models across customer interaction, cross-cultural
consumer data, and ROI, achieving a projected accuracy of over 98%.
The proposed QFDL-CBDMA framework proposes a hybrid quantum–classical learn -
ing strategy for cross-border e-commerce marketing analytics, which adopts quantum
feature encoding, parameterized quantum circuits, quantum fusion layers, and classi -
cal prediction networks. The framework proposed in this article differs from traditional
deep learning and recommendation methods, which primarily address the modeling of
complex non-linear relations between various features of consumers, transactions, and
markets through classical feature representation and fusion techniques.
The study outline is below. Section  1 introduces digital logistics marketing, the
research challenge, goals, and significance. Section  2 compares the suggested meth -
ods to typical DL, ML, and AI-driven optimization methods in the literature. Section  3
describes data collection and analysis. Section  4 presents results and comparisons from
classical and quantum logistics models. The study concludes with Sect. 5, which summa-
rizes its key results and research contributions.
2 Literature survey
E-commerce is growing worldwide, and sophisticated algorithms are being used in mar -
keting, customer support, and recommendation systems. Digital marketing for multi -
national companies has been suggested for improvement. Many methods suffer with
scalability, market data, and cross-cultural collaboration.
Table 1 presents a comparative review of existing studies on cross-border e-commerce,
recommendation systems, digital marketing analytics, quantum machine learning,
and IoT-enabled logistics. The analysis highlights the proposed methods, application
domains, and key limitations of recent approaches published between 2024 and 2025.
The identified research gaps demonstrate the need for an integrated framework capable
of combining IoT-driven data acquisition, quantum-enhanced learning, and adaptive
cross-border marketing analytics.
The proposed model solves these restrictions by efficiently processing high-dimen -
sional, multi-modal input. Quantum computing and deep learning enable it. For real-
time market adaptation, QFDL-CBDMA has QFNN and QGD. The convergence and
accuracy are faster and higher than traditional methods. We need to understand con -
sumer behavior across cultures to design focused marketing campaigns in the numer -
ous worldwide markets. Compared with the conventional hybrid AI marketing methods
that rely primarily on the classic deep learning, the recommendation engine or ensemble

Page 4 of 33
Chen Discover Internet of Things            (2026) 6:225
Table 1 Related work comparison
Category Author(s)
(year)
Proposed method Application Limitations
A. IoT
logistics
Jin et al. [16]
(2024)
Development environ-
ment of cross-border
E-commerce logistics
Digital marketing in global
e-commerce logistics
Lacks integration with
real-time marketing
analytics
Wang and
Hsu [27]
(2025)
IoT-based logistics data
analytics framework
Real-time logistics
monitoring and shipment
tracking
Focuses primarily on
logistics operations
with limited marketing
integration
Lu [28] (2025) Multimodal deep
reinforcement learning
for IoT-driven logistics
optimization
Global logistics schedul-
ing and supply chain
optimization
Limited support for
customer behavior and
marketing effective-
ness prediction
Xue et al. [29]
(2025)
IoT-based information
integration framework
Supply chain visibility
and operational decision
support
Does not address
multi-modal marketing
analytics or intelligent
recommendations
B. Classical
marketing
models
Kang [13]
(2024)
AI-marketing prediction
model (AI-MPM)
Cross-border e-commerce
marketing predictions
Limited scalability to
global markets
Jin et al. [14]
(2024)
Comparative study of rec-
ommendation algorithms
E-commerce big data
analysis and recommenda-
tion systems
Does not integrate
deep learning for dy-
namic data handling
Yao [15]
(2024)
Cross-border e-commerce
recommendation system
using deep learning
(CBER-DL)
Cross-border e-commerce
recommendation
Focuses on a
single deep learning
approach
Al-Otaibi [17]
(2024)
Deep learning framework
for customer behavior
prediction (DL-CBP)
Customer behavior predic-
tion in e-commerce
Does not address
cross-cultural market
differences
Liu and Kim
[18] (2025)
CNN-based AI recommen-
dation model
Cross-border e-
commerce marketing
recommendations
Limited scalability for
large datasets
Yang [19]
(2024)
Improved BP neural
network for supply chain
performance evaluation
Cross-border e-commerce
supply chain optimization
Focuses mainly
on supply chain
performance
Dritsas and
Trigka [20]
(2025)
Machine learning in
E-commerce
General e-commerce
applications and future
trends
Limited emphasis on
marketing-oriented
deep learning
Shankar et al.
[21] (2024)
Ensemble learning for
E-commerce recommen-
dation (EL-ER)
Intelligent e-commerce
recommendations
Insufficient consider-
ation of cross-border
data variations
Karabila et al.
[22] (2024)
Deep learning and
ensemble-based recom-
mender system
E-commerce recommen-
dation systems
Limited analysis of
dynamic customer
preferences
Valencia et al.
[23] (2024)
AI-based recommender
systems for E-commerce
AI-driven recommenda-
tion platforms
Focuses on static
recommendation
strategies
Okeleke et al.
[24] (2024)
AI-based predictive mar-
ket analytics
Market trend and con-
sumer behavior prediction
Lacks real-time
marketing adaptation
mechanisms
C. Quantum
approaches
Thakkar et al.
[25] (2024)
Hybrid quantum machine
learning
Predictive analytics and
intelligent business
forecasting
Dependent on
quantum simulation
environments
Sáez-Ortuño
et al. [26]
(2025)
Quantum-based digital
market analytics
Consumer behavior and
digital marketing analysis
Limited practical
deployment and real-
time analytics support

Page 5 of 33
Chen Discover Internet of Things            (2026) 6:225
learning methods, the proposed QFDL-CBDMA framework introduces an AI fusion
mechanism which can model complex cross-modal relationships with entangled quan -
tum states. The existing systems such as AI-MPM, EL-ER, and CBER-DL primarily focus
on the prediction accuracy and recommendation optimization using classical architec -
tures, and fail to include quantum feature encoding, parameterized quantum circuits,
or quantum-aware optimization strategies. The framework not only learns high-dimen -
sional representations but also incorporates Quantum Fusion Neural Networks (QF-
NNs) to encode heterogeneous Consumer, Demographic, and Market information
across quantum states and uses this information to scale high-dimensional representa -
tion learning. Moreover, the Quantum Gradient Descent (QGD) optimization mecha -
nism ensures efficient adaptive learning in an environment of rapidly changing market
conditions across the borders thanks to parameter-shift gradient estimation and quan -
tum parallelism.
3 System methodology
3.1 Problem statement
One of the biggest obstacles for companies doing international online shopping is com -
ing up with digital marketing tactics that are specific to the wants and demands of
consumers in different countries. Building accurate models of high-order, entangled
interactions among multi-modal features remains challenging without an exponential
growth in the number of parameters.
3.1.1 Objective
Develop and evaluate a novel deep learning based E-Commerce Digital Marketing using
the quantum fusion capable of capturing complex feature extractions and accelerating
model training for improved prediction accuracy and adaptive marketing in the cross-
border E-commerce.
Mathematically, the problem can be framed as learning the predictive function f that
maps multi-modal input features 𝑋𝑋𝑋𝑋𝑋 1,𝑋𝑋 2,𝑋𝑋 3 …𝑋𝑋 𝑚𝑚 derived from diverse modalities to
the marketing effectiveness metric ˆ𝑌𝑌 based on Eq. (1).

𝑓𝑓𝑓𝑓𝑓𝑓 ˆ𝑌𝑌𝑌 ˆ𝑌𝑌 𝑌 𝑌𝑌𝑌𝑌𝑌𝑌 min
𝜃𝜃
ℒ (𝑓𝑓𝜃𝜃 (𝑓𝑓) 𝑌𝑌𝑌 ) (1)
where, 𝑓𝑓𝜃𝜃  represents the parameters of the Quantum fusion deep learning model and
ℒ(.) denotes the loss function quantifying the prediction error. It is very hard to build
good models of high-order, entangled interactions among multi-modal features without
the number of parameters growing exponentially. The QF-NN is one solution that uses
entangled quantum circuits is represented in Eq. (2) to show how properties recorded in
quantum states interact with each other:
 ||Ψ𝑓𝑓𝑓𝑓𝑓𝑓 ⟩=℘ 𝑓𝑓𝑓𝑓𝑓𝑓 (𝜃𝜃) ⊗𝑚𝑚 𝑖𝑖𝑖𝑖 |𝜓𝜓𝑖𝑖 ⟩  (2)
Here, |𝜓𝜓𝑖𝑖 ⟩  is the quantum state encoding of the ith modality, ℘𝑓𝑓𝑓𝑓𝑓𝑓 (𝜃𝜃) denotes the param-
eterized unitary operator that performs quantum fusion, enabling the scalable and
expressive representation of multi-modal data relationships.

Page 6 of 33
Chen Discover Internet of Things            (2026) 6:225
3.2 Structure of QFDL-CBDMA
The QFDL-CBDMA model's workflow is depicted in Fig.  1, outlining the key steps for
analyzing and evaluating strategies for cross-border e-commerce.
3.2.1 Data acquisition and pre-processing
Data collection gathers raw data from various sources, which must be cleaned, trans -
formed and organized for analysis. It is the initial step of model building, collecting and
cleaning demographic, market and customer behavior data from multiple international
e-commerce sources.
Demographic, economic and consumer data are collected for international inter -
net commerce. Businesses use demographic data from multiple sources to categorize
and target customers, which marketers use to target different populations in different
countries.
Market data covers latest economic data, industry developments, pricing tactics and
supply chain dynamics from multiple sources. Consumer behavior data refers to cus -
tomer behaviors and preferences in digital marketing from multiple sources. Quan -
tum feature transformation and categorical variable encoding are required for machine
learning.
Additionally, raw data must be cleaned to remove inconsistencies, duplication and
missing entries. Normalizing numerical features improves scale matching. Marketing
analytics pre-processing includes temporal data aggregation, outlier detection and fea -
ture engineering, creating meaningful representations. The QF-NN extracts and ana -
lyzes prepared data. Proper data acquisition and pre-processing are required for the
model to adapt marketing strategies to various global marketplaces.
The proposed framework has an IoT-enabled data acquisition architecture for real-
time cross-border e-commerce analytics, collecting information from RFID tags, GPS-
equipped logistics trackers, warehouse sensors, inventory monitors and customer
interaction systems. Raw edge layer data is processed with noise removal, missing value
handling, value normalization and temporal aggregation to reduce communication over-
head and improve data quality. Preprocessed data is sent via secure channels to the cloud
analytics layer, where multiple data types are merged into a single multi-modal dataset,
then provided to the QFDL-CBDMA framework for quantum encoding, feature fusion,
predictive modelling and marketing effectiveness evaluation. This approach enables
Fig. 1 Overview of proposed model(simulation parameters: 8 qubits, 100 epochs, N = 12,000)

Page 7 of 33
Chen Discover Internet of Things            (2026) 6:225
real-time analysis of logistics processes, customer engagements and market trends, sup -
porting informed decision-making for cross-border marketing strategies.
Raw IoT data is gathered from RFID tags, GPS tracking systems, warehouse sensors
and customer interaction platforms. The edge processing layer processes the data, then
combines it into a single multi-modal dataset. Categorical variables are encoded via one-
hot encoding, and numerical features are normalized to [0,1]. Feature engineering gen -
erates relevant indicators, which are converted to a 16-dimensional feature vector and
fed into QFDL-CBDMA's processing layers.
The practical deployment of the proposed framework in cross-border IoT environ -
ments faces three primary hardware constraints. First, low-power edge terminals (e.g.,
RFID readers and warehouse sensors) typically operate with limited computational
capacity (approximately 50–200 MFLOPS) and memory budgets (under 512 MB), which
precludes on-device execution of quantum circuit simulations. To address this con -
straint, a lightweight preprocessing scheme is proposed: edge nodes perform only noise
filtering, missing-value imputation using running means, and temporal aggregation at
5-min intervals, while all quantum encoding, circuit simulations, and gradient computa -
tions are offloaded to cloud instances. Second, multi-region data synchronization intro -
duces variable delays depending on geographic distance and network infrastructure;
the latency test results (50  ms, 100  ms, 200  ms, and 500  ms) correspond respectively
to intra-region connections, inter-region fiber links, cross-continental undersea cable
routes, and satellite backup channels. The framework maintained predictive accuracy
above 98.2% for delays up to 200 ms and 97.1% at 500 ms, demonstrating that moderate
synchronization latency does not substantially degrade marketing effectiveness predic -
tion. Third, bandwidth limitations (typically 100–500 kbps per edge gateway) necessitate
feature-level compression; the proposed preprocessing reduces raw IoT telemetry from
42 raw signals to 16 normalized features, achieving an 82% reduction in transmission
payload without compromising prediction fidelity.
3.2.2 Quantum fusion neural network
The QF-NN is a core component of the QFDL-CBDMA framework, comprising four
stages: feature preprocessing, quantum encoding, quantum fusion-based feature extrac -
tion, and prediction optimization. Multi-modal e-commerce data—including demo -
graphics, consumer behavior, transaction history, and IoT-derived logistics signals—are
normalized and transformed through classical dense layers. The resulting latent features
are encoded into quantum states via amplitude and hybrid angle encoding, then pro -
cessed through parameterized quantum circuits with entanglement operations to cap -
ture high-order cross-modal interactions. Quantum measurements are fed into classical
prediction layers for marketing effectiveness estimation. The framework is implemented
in a simulator-based hybrid quantum–classical environment with 8 qubits and 144 train-
able parameters, trained using QGD optimization with a learning rate of 0.001, batch
size of 64, and 100 epochs (Fig. 2).
Encoding high-dimensional data into quantum states is the initial stage in running
QF-NN. This research covers consumer behavior, demographics, and markets. The
QF-NN encodes properties as qubits using quantum gates, unlike classical neural net -
works. It helps the QF-NN store and handle data efficiently. This fusion effectively inte -
grates the two CNNs' knowledge, improving performance. The quantum fusion model

Page 8 of 33
Chen Discover Internet of Things            (2026) 6:225
uses a QNN with two blocks, unlike the feed-forward neural network with one layer.
Data transport into a quantum circuit begins with quantum encoding. Quantum opera -
tions are used to deduce information from encoded data in the parameterized quantum
circuit (PQC). This article compares two of the best encoding approaches for predicting
binding affinity. First, amplitude encoding encodes normalized attributes using the com-
putational foundation' quantum state amplitudes. Only ⌈log2(n)⌉ qubits are needed to
convert a single data sample into a quantum state, where n represents the input dimen -
sion of the QNN. The depth of the embedding circuit and the number of parameters
that can be optimized grow at O(log 2(n)). The Hybrid Angle Encoding (HAE) method
uses parallel blocks of independent qubits to encode amplitude. Each feature consists
of b blocks, each with a size of 2 m − 1, where m is the number of qubits. It requires b ×
m qubits to encode the entire data sample into a quantum state. Quantum encoding is
needed to record complex interrelationships among variables that classical models can -
not identify. Quantum superposition and entanglement, which allow the model to repre-
sent multiple possibilities concurrently, improve the network's ability to learn from vast,
diverse datasets. All input modalities, such as consumer demographic vectors, behav -
ioural metrics, and market indicators, are encoded into quantum states. Mathematically,
the physical feature vector x is transformed in Eq. (3)
 |𝜓𝜓𝑖𝑖 ⟩= ⊗𝑑𝑑 𝑖𝑖𝑖𝑖 (𝛼𝛼𝑖𝑖 |0⟩+𝛽𝛽 𝑖𝑖 |1⟩ ) 𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤 |𝛼𝛼𝑖𝑖 |2 + |𝛽𝛽𝑖𝑖 |2 =1  (3)
Quantum fusion explains cross-modal interactions concisely and expressively without
exponential parameter rise, unlike low-rank tensor fusion or feature concatenation. It is
done by entangled modality states in quantum fields, as shown in Eq. (4).

||Ψ𝑓𝑓𝑓𝑓𝑓𝑓 ⟩=℘ 𝑓𝑓𝑓𝑓𝑓𝑓 (𝜃𝜃) ⊗ |𝜓𝜓1⟩ ⊗ |𝜓𝜓2⟩…. ⊗ |𝜓𝜓𝑚𝑚⟩ ≈ ∑ 𝛼𝛼≤𝑃𝑃 𝑐𝑐𝛼𝛼𝑋𝑋𝛼𝛼  (4)
where 𝑃𝑃 is the polynomial degree, 𝛼𝛼 ios the multi-index, and 𝑋𝑋 represents the input
features.
QF-NN follows feature extraction once data is converted to quantum states. Chang -
ing layer weights and backpropagation are typical feature extraction methods in conven-
tional neural networks. The quantum parallelism of QF-NN helps here. It speeds up the
process and allows the model view more features. A quantum fusion operator ℘𝑓𝑓𝑓𝑓𝑓𝑓 (θ)
Fig. 2 Quantum fusion neural network (simulation parameters: 8 qubits, 100 epochs, N = 12,000)

Page 9 of 33
Chen Discover Internet of Things            (2026) 6:225
is intended to embed heterogenous marketing features into a common representation
space which is quantum-enhanced in order to be able to model high-order cross-modal
interactions. The suggested model consists of two classical preprocessing layers, trans -
forming parts of the problem into a "normalised" problem by creating latent feature vec -
tors of the data, followed by an encoding using parameterized rotation gates, that maps
these vectors into quantum states. The consumer-specific marketing attributes are coded
into quantum states based on their semantic and behavioral meaning. For instance, cul -
tural preference indicators can be represented by angular quantum rotations, with the
magnitudes of the features determining the angles of the quantum gates. Equation ( 5)
shows how quantum gates recognize patterns in feature extraction. Parallel processing
helps QF-NN detect data patterns and correlations better than other methods.
 |Ψ𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒 ⟩ = ℚ(𝜑𝜑𝜑 ||Ψ𝑓𝑓𝑓𝑓𝑓𝑓 ⟩ (5)
where ℚ(𝜑𝜑𝜑 i is the trainable quantum circuit for extracting features, it helps with tasks
such as determining how certain demographic factors affect purchasers' choices or iden-
tifying patterns of customer behavior that seem unimportant across numerous market -
places. The Quantum neural network computes the output as shown in Eqs. (6) and (7).
 𝑌𝑌 𝑄𝑄 = ||Ψ𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 || 𝒪𝒪 ||Ψ𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 || (6)
 Ψ𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 = 𝒰𝒰𝒰𝒰𝒰𝒰𝒰 |Ψ𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑓𝑓𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒 ⟩ (7)
where 𝒪𝒪 is the observable encoding prediction, obtained after unitary transformations,
and 𝒰𝒰𝒰𝒰𝒰𝒰𝒰 denotes the parameterized quantum circuit. QF-NN improves forecasts and
model generalizability by uncovering dependencies and interactions traditional net -
works ignore. Ability to handle quantum improvements makes it possible.
3.2.3 Data encoding and feature extraction in QFNN
The QF-NN can quickly handle high-dimensional, multi-modal data by encoding
it, which makes it easier to extract features for cross-border e-commerce analytics
is shown in Fig.  3. It does this by using quantum parallelism and entanglement. First,
the QF-NN maps each feature to qubits using parameterized quantum gates. The fea -
ture encoding process starts with transforming multi-modal classical input data, which
includes demographic vectors, metrics for consumer behaviour, and market indica -
tors, into quantum states. It is done using quantum encoding techniques like amplitude
encoding or hybrid angle encoding. The quantum form uses entanglement and super -
position to record complicated high-dimensional interactions that classical models can -
not handle computationally. Trainable Parameterized Quantum Circuits (PQCs) provide
feature extraction after encoding by applying unitary modifications to the encoded states
through quantum gates.
It allows for parallel processing and improved pattern recognition on international
e-commerce datasets. Measurements of the derived quantum features as classical
observables allow for the integration of multi-modal insights, which in turn allows for
adaptive marketing optimization and predictive analytics. The Hamiltonian operator
‵
𝐻𝐻QF−NN for the quantum fusion deep learning system can be expressed as in Eq. (8).

Page 10 of 33
Chen Discover Internet of Things            (2026) 6:225

HQF−NN(𝑡𝑡𝑡 𝑡
𝑚𝑚
∑
𝑖𝑖𝑖𝑖
𝑑𝑑
∑
𝑗𝑗𝑖𝑖
𝑥𝑥𝑖𝑖𝑗𝑗
‵
𝜎𝜎
(𝑖𝑖𝑖𝑗𝑗𝑖
𝑧𝑧 +
𝐿𝐿
∑
𝑙𝑙𝑖𝑖
𝑁𝑁𝑞𝑞
∑
𝑘𝑘𝑖𝑖
(𝜃𝜃𝑋𝑋 𝑙𝑙𝑘𝑘
‵
𝜎𝜎
(𝑘𝑘𝑖
𝑥𝑥 +𝜃𝜃 𝑌𝑌 𝑙𝑙𝑘𝑘
‵
𝜎𝜎
(𝑘𝑘𝑖
𝑦𝑦 +𝜃𝜃 𝑍𝑍 𝑙𝑙𝑘𝑘
‵
𝜎𝜎
(𝑘𝑘𝑖
𝑧𝑧 ) +
𝑚𝑚
∑
𝑖𝑖𝑖𝑗𝑗
𝑔𝑔𝑖𝑖𝑗𝑗 (
‵
𝜎𝜎
(𝑖𝑖𝑖
+ ⊗
‵
𝜎𝜎
(𝑗𝑗𝑖
− + h.c.𝑡 + ∑
𝛼𝛼
𝑤𝑤𝛼𝛼O𝛼𝛼 (8)
where, ∑
𝑚𝑚
𝑖𝑖𝑖𝑖 ∑
𝑑𝑑
𝑗𝑗𝑖𝑖 𝑥𝑥𝑖𝑖𝑗𝑗
‵
𝜎𝜎
(𝑖𝑖𝑖𝑗𝑗𝑖
𝑧𝑧  is the data encoding Hamiltonian with 𝑚𝑚 is the data modali -
ties, 𝑑𝑑 is the number of features, 𝑥𝑥𝑖𝑖𝑖𝑖  is the classical data value,
‵
𝜎𝜎
(𝑖𝑖𝑖𝑖𝑖𝑖
𝑧𝑧  denotes the Pauli-Z
operator. (𝜃𝜃𝑋𝑋 𝑙𝑙𝑙𝑙
‵
𝜎𝜎
(𝑙𝑙𝑘
𝑥𝑥 +𝜃𝜃 𝑌𝑌 𝑙𝑙𝑙𝑙
‵
𝜎𝜎
(𝑙𝑙𝑘
𝑦𝑦 +𝜃𝜃 𝑍𝑍 𝑙𝑙𝑙𝑙
‵
𝜎𝜎
(𝑙𝑙𝑘
𝑧𝑧 ) denotes the variational Hamiltonian with number
of qubits 𝑁𝑁𝑞𝑞 ,and Trainable parameters 𝜃𝜃𝑋𝑋 𝑙𝑙𝑙𝑙 ,𝜃𝜃𝑌𝑌 𝑙𝑙𝑙𝑙 , and 𝜃𝜃𝑍𝑍 𝑙𝑙𝑙𝑙 .In the Equation 𝑔𝑔𝑖𝑖𝑖𝑖 (
‵
𝜎𝜎
(𝑖𝑖𝑖
+ ⊗
‵
𝜎𝜎
(𝑖𝑖𝑖
− ) is
the quantum fusion Hamiltonian with fusion coupling strength and Hermitian Conju -
gate (h.c.). The term ∑𝛼𝛼 𝑤𝑤𝛼𝛼
‵
𝑂𝑂𝛼𝛼 is the observable Hamiltonian using classical weight ( 𝑤𝑤𝛼𝛼
) and Quantum Observable operator (
‵
𝑂𝑂𝛼𝛼). A theoretical performance baseline and trivial
case boundary for the QNN is given in Eq. (9).
 ℒ𝑄𝑄𝑄𝑄𝑄𝑄𝑄𝑄𝑄 (Δ=2 ) =𝕌𝕌 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡
Δ0𝑋𝑋
𝑋𝑋 = 𝕌𝕌(Δ = 2)𝕌 Ω×𝑄𝑄  (9)
This Equation establishes a boundary condition for feature extraction and defines the
model's trivial task. The model executes simple tasks without additional computing if
we tolerate total inaccuracy in multi-modal input encoding and processing. This refer -
ence is essential for cases where complicated quantum properties are not needed. Since
all important analysis must be done at error tolerances below this maximum threshold,
this Equation proves the QF-NN system's lower performance limit. This requires true
quantum computing.
The QFDL-CBDMA framework consists of two classical preprocessing layers (256
and 128 neurons) followed by a hybrid quantum processing module and two prediction
Fig. 3 Data encoding and feature extraction(simulation parameters: 8 qubits, 100 epochs, N = 12,000)

Page 11 of 33
Chen Discover Internet of Things            (2026) 6:225
layers (64 and 32 neurons). ReLU activation, batch normalization, and a dropout rate
of 0.3 are employed during preprocessing. The generated latent features are reduced to
a 16-dimensional vector and encoded into quantum states using amplitude and hybrid
angle encoding. The quantum module utilizes 8 qubits with a circuit depth of 6 varia -
tional layers composed of Rx, Ry, Rz rotation gates and CNOT-based entanglement
operations, resulting in 144 trainable quantum parameters. Quantum measurements are
obtained using Pauli-Z expectation values and are subsequently processed by the predic-
tion layers with sigmoid or softmax activation for marketing effectiveness prediction.
The Quantum Feature Entanglement Score (QFES) is defined as
𝑄𝑄𝑄𝑄𝑄𝑄𝑄𝑄 𝑄
1
𝑁𝑁
∑
𝑁𝑁
𝑖𝑖𝑖1 ⟨𝜓𝜓𝜓𝜓𝜓𝜓𝜓𝜓𝜓 ⟩𝜓2, where |𝜓𝜓𝑖𝑖 ⟩ and |𝜙𝜙𝑖𝑖 ⟩ represent quantum states encoding feature
subsets from different modalities. The metric is mathematically bounded within  [0,1]
by virtue of the Cauchy–Schwarz inequality, with  QFES = 0  indicating complete inde -
pendence and  QFES=1  indicating maximal entanglement. This bounded property pro -
vides a natural scale for comparing feature interaction strengths across different model
configurations. The physical interpretation of QFES is tied to the Schmidt decompo -
sition of the fused quantum state: higher QFES values correspond to larger Schmidt
coefficients, indicating that the entangled representation captures more non-local cor -
relations among modalities—a capability that classical feature interaction measures (e.g.,
Hilbert–Schmidt Independence Criterion or Mutual Information) require exponentially
growing samples to estimate. The Quantum Complexity Gain Score (QCGS) is defined
as  𝑄𝑄𝑄𝑄𝑄𝑄𝑄𝑄 𝑄
𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞
𝐶𝐶𝑃𝑃𝑃𝑃𝐶𝐶𝐶𝐶𝐶𝐶𝑃𝑃𝐶𝐶𝐶𝐶𝑃𝑃𝑃𝑃𝑃𝑃𝐶𝐶 𝐶𝐶𝑃𝑃𝐶𝐶𝐶𝐶𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞𝑞
/
𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 𝑐𝑐𝑐𝑐𝑞𝑞𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑞𝑞𝑐𝑐
𝐶𝐶𝑃𝑃𝑃𝑃𝐶𝐶𝐶𝐶𝐶𝐶𝑃𝑃𝐶𝐶𝐶𝐶𝑃𝑃𝑃𝑃𝑃𝑃𝐶𝐶 𝐶𝐶 𝑃𝑃𝐶𝐶𝐶𝐶𝑐𝑐𝑐𝑐𝑞𝑞𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑞𝑞𝑐𝑐
, capturing the representa -
tional efficiency gain of quantum-inspired encoding relative to classical alternatives.
Compared with classical measures such as VC-dimension or Rademacher complex -
ity, QCGS is neither upper-bounded nor distribution-free; consequently, its results are
reported as exploratory indicators requiring further validation. This limitation is con -
sistent with recent quantum machine learning literature, where entanglement entropy
and fidelities are routinely used as diagnostic tools without established statistical testing
frameworks.
3.2.4 Quantum gradient descent optimization
The quantum gradient descent (QGD) optimization technique greatly accelerates the
QF-NN learning process. An approach for estimating quantum gradients that employs
entanglement and superposition, two essential concepts in quantum physics, to cal -
culate gradients with a consistent processing cost. QGD speeds up standard gradient
descent by repeatedly updating weights based on erroneous gradients. It does this by
using quantum mechanics to exploit interference and entanglement.
The QFDL-CBDMA framework trains the parameters of the parameterized quantum
circuits by using Quantum Gradient Descent optimization. The optimization process
starts by initializing quantum parameters to be trained, then forward propagating the
quantum circuit to obtain prediction outputs, loss values. The parameter-shift rule is
used to obtain estimates of the gradients by measuring states of shifted quantum cir -
cuits, which allows for accurate calculation of gradients without numerical approxima -
tion. The optimized gradients are then fed back into the quantum circuit parameters in
an iterative manner until convergence. This optimization approach is used to increase

Page 12 of 33
Chen Discover Internet of Things            (2026) 6:225
the learning efficiency, allowing stable adjustment of parameters for complicated feature
interactions among multiple modes.
In the framework of the simulator, the use of quantum parallelism, quantum entangle-
ment, and parameterized quantum transformations are used as representational tools
for learning of complex feature interactions. These properties are part of the expressive
feature modeling within the simulated environment, but in the present study, experi -
mentally attested quantum speedup, computational acceleration, hardware-level ben -
efits over conventional implementations are not claimed. The model starts by initializing
the trainable quantum circuit parameters, typically chosen randomly based on Eq. (10).
 𝜃𝜃(0) = {𝜃𝜃(0) 1 ,𝜃𝜃 (0) 2 … … .𝜃𝜃(0) 𝑛𝑛 } (10)
Figure 4 shows how the suggested model uses gradient estimation in QGD. It also shows
how the model directly relates to the main equations for quantum optimization, as
shown in Eq. (11).
 𝑓𝑓𝑓 (𝜃𝜃) = 𝑓𝑓 (𝜃𝜃 𝜃 𝜃𝜃𝜃𝜃 ) − 𝑓𝑓(𝜃𝜃) 𝜃𝜃𝜃𝜃  (11)
The Numerical Gradient method uses the standard finite-difference method to esti -
mate the derivative of a function on the left panel. The method is shown with two close-
together curve positions joined by a line. The estimate of the true gradient is basic but
noisy. The model provided differs from the more robust quantum technique used in the
suggested framework.
The Parameter-Shift Rule, which is fundamental to the Analytic Gradient approach
used in quantum circuit optimization, is shown in the right panel. Due to the lack of
direct derivative information, computing classical gradients for quantum circuits is dif -
ficult and expensive. QGD uses a parameter shift rule to estimate the gradient of the cost
function 𝐶𝐶𝐶𝐶𝐶𝐶 with respect to each parameter, which is given in Eq. (12).

𝑓𝑓𝑓𝑓𝑓𝑓𝑓 ≈ ∂𝐶𝐶𝑓𝑓𝑓𝑓 ∂𝑓𝑓𝑘𝑘 ≈ 𝐶𝐶 (𝑓𝑓𝜃
𝜋𝜋
2
) −𝐶𝐶 (𝑓𝑓−
𝜋𝜋
2
)
2sin
𝜋𝜋
2
 (12)
where,
𝜋𝜋
2
is the fixed shift, and the cost function C is computed by measuring the expec -
tation value of an observable on the quantum circuit output. The method can accurately
estimate gradients even with large parameter sets, requiring only two quantum circuit
evaluations per parameter. Once gradients are calculated using Eq. ( 13), the parameters
are updated in the direction that minimizes the cost function.
 𝜃𝜃𝑡𝑡𝑡𝑡 =𝜃𝜃 𝑡𝑡 +𝛼𝛼 ∇𝐶𝐶𝐶𝜃𝜃𝑡𝑡 ) (13)
Here, 𝛼𝛼 is the learning rate controlling step size and 𝑡𝑡 indexes the iteration cycle. This
iterative update moves variables closer to the local minimum, thereby improving model
fit. The gradient estimation and parameter update processes are repeated until the model
convergence criteria are met, such as when consecutive changes in the cost function are
small ||𝐶𝐶𝐶𝐶𝐶𝑡𝑡𝑡𝑡 )−𝐶𝐶 𝐶 𝐶𝐶 𝑡𝑡 )|| fall below a threshold. The implementation of Quantum Gradient
Descent (QGD) in the proposed QFDL-CBDMA framework involves iterative optimiza -
tion of trainable quantum circuit parameters using parameter-shift gradient estimation.
Initially, the trainable quantum parameters are randomly initialized, and the encoded

Page 13 of 33
Chen Discover Internet of Things            (2026) 6:225
multi-modal input data are propagated through the parameterized quantum circuit to
compute the prediction output and corresponding loss value. Instead of conventional
finite-difference approximation, QGD computes gradients by shifting each quantum
parameter in positive and negative directions within the quantum circuit and measuring
the resulting expectation values. This mechanism enables accurate gradient estimation
while avoiding excessive computational overhead associated with classical numerical
differentiation.
The major computational advantage of QGD lies in its utilization of quantum paral -
lelism and entanglement for simultaneous exploration of multiple optimization path -
ways. Compared with classical gradient descent methods that often suffer from slow
convergence and local minima trapping in high-dimensional optimization spaces,
QGD provides faster convergence and more stable parameter updates. Furthermore,
the parameter-shift mechanism significantly reduces gradient computation complexity
while improving learning efficiency for large-scale multi-modal datasets. These char -
acteristics make QGD highly suitable for adaptive cross-border e-commerce analyt -
ics where rapid optimization and real-time market adaptation are essential. To further
accelerate convergence, the quantum natural gradient descent technique is represented
by the Eqs. (14) and (15).
 Δ𝜃𝜃𝑄𝑄𝑄𝑄𝑄𝑄 =𝐺𝐺 −1(𝜃𝜃𝜃∇𝐶𝐶(𝜃𝜃𝜃 (14)
 𝜃𝜃𝑡𝑡𝑡𝑡 =𝜃𝜃 𝑡𝑡 − 𝜂𝜂𝜂𝜃𝜃𝑄𝑄𝑄𝑄𝑄𝑄  (15)
where, 𝐺𝐺−1(𝜃𝜃𝜃 is the quantum tensor metric accounting for the curvature of the param -
eter manifold. The improvement allows for faster optimization by allowing bigger, more
informed steps. Quantum parallelism in QGD, evaluating many solutions concur -
rently speeds up the process of finding the optimal parameter set. A major benefit of
the QF-NN for real-time applications in global e-commerce is its capacity to react to
changing market conditions and customer behavior. Faster and more accurate analy -
sis of large datasets is possible with QF-NN thanks to quantum gradient descent. This
will help with the better management of the vast quantities of consumer and market
data generated by worldwide e-commerce. QGD, a cutting-edge optimization method,
speeds up quantum and hybrid quantum–classical ML model parameter training. QGD
uses quantum superposition and entanglement to estimate gradients faster than clas -
sical gradient methods, which require many objective function evaluations to estimate
each gradient component. It is implemented through a simulator-based framework that
includes parameterized quantum circuits (PQCs), quantum state encoding, quantum
entanglement operations and quantum inspired optimization strategies, which simu -
late quantum computational behaviour. High dimensional multi-modal marketing data
was processed by coupling the quantum modules with classical deep learning mod -
ules in a hybrid processing pipeline. Specifically, amplitude encoding and hybrid angle
encoding were used to encode classical feature vectors into simulated quantum states,
and entanglement operations were utilised to interactively learn about the relationship
between demographic, behavioural, and market-related features. The same optimiza -
tion process, called the quantum gradient descent (QGD) optimization process, was also
conducted by numerically making quantum expectation measurements and calculating
quantum gradients using the parameter-shift methods. This hybrid simulation-based

Page 14 of 33
Chen Discover Internet of Things            (2026) 6:225
implementation allowed for efficient experiments, reproducibility and scalability analy -
sis without being limited by the physical constraints of the quantum hardware platforms
that are currently available.
Initialize QGD (QF-NN, θinit, α, max_iter, tol)
Input:
QF-NN: Parameterized Quantum Fusion Neural Netθorα model
θinit: Initial parameters vector of quantum gates
α: Learning rate
max_iter: Maximum number of iterations
tol: Tolerance for convergence
Output:
θopt: Optimized parameters
Cval: Final cost value
Begin
θ ← θinit
for t in 1 to max_iter do
Compute cost function C(θ) by measuring observable on QF-θθ output
for eacα parameter θk in θ do
Θ+ ← θ witα θk sαifted by +s (s = π/2)
Θ-← θ witα θk sαifted by -s
Evaluate cost: C+ ← C (Θ+), C- ← C(Θ-)
Compute gradient estimate:
k C(θ) ← (C+-C -) / (2 * sin(s))
end for
Update parameters:
θnew ← θ - α * C(θ)
Cαeck convergence:
if |C(θnew) -C (θ)| < tol tαen
break
end if
θ ← θnew
end for
θopt ← θ
Cval ← C(θopt)
return θopt, Cval
End
Algorithm 1 QGD optimization
QFES measures the dependency strength among entangled quantum feature represen-
tations, quantifying cross-modal interaction learning beyond predictive metrics. QCGS
evaluates representational efficiency gains from quantum-inspired transformations, con-
trasting with classical complexity measures that focus solely on execution cost. These
two indicators complement standard evaluation metrics by assessing feature interaction
strength and representation efficiency, respectively.

Page 15 of 33
Chen Discover Internet of Things            (2026) 6:225
4 Experimental evaluation
4.1 Dataset description
The dataset filtering procedure involved removing records with missing transaction IDs
(1.2%), negative transaction values (0.3%), and dates outside the 2020–2023 temporal
range (2.8%). IoT signal cleaning was performed by applying a median filter with a win -
dow size of 5 to smooth sensor readings, followed by threshold-based outlier rejection
(values exceeding 3 standard deviations were winsorized). The preprocessed dataset is
available at the original Kaggle repository  (   h t t p  s : / / w  w w . k a g  g l e .  c o m / d a t a s e t s / s m a y a n j
/ e - c o m m e r c e - t r a n s a c t i o n s - d a t a s e t     ) . The complete preprocessing scripts, quantum cir -
cuit simulation code, and model implementation are available at the repository link pro -
vided in the data availability statement, enabling independent replication of all reported
experiments.
The E-Commerce Transactions Dataset originally comprises approximately 500,000
simulated transaction records. For the purpose of model development and statisti -
cal validation, a final analytical sample of 12,000 records was derived through stratified
random sampling. This sampling procedure was designed to preserve the original dis -
tribution of key variables, including product categories, geographic regions, and trans -
action values, while ensuring computational feasibility for the iterative quantum circuit
simulations required by the proposed framework. The reduction from the full dataset
to the analytical sample was necessary because the hybrid quantum–classical training
procedure involves repeated parameter-shift gradient estimations, which impose sub -
stantial computational overhead. The stratified sampling approach ensures that the ana -
lytical sample remains representative of the broader dataset's underlying patterns and
distributions[27].
Fig. 4 Gradient Estimation in QGD(simulation parameters: 8 qubits, 100 epochs, N = 12,000)

Page 16 of 33
Chen Discover Internet of Things            (2026) 6:225
To enhance the transparency and reproducibility of the study, Table  2 presents
the complete list of the 16 input features used in the QFDL-CBDMA framework. For
each feature, the table reports the variable name, data source, data type, preprocessing
method, and a brief functional interpretation. Critically, none of the predictor variables
included in the table were used in the construction of the target variable, thereby pre -
venting target leakage. The features span four distinct modalities: demographic indi -
cators, behavioral metrics, transactional characteristics, and logistics performance
signals, which collectively capture the multi-modal nature of cross-border e-commerce
operations.
The cross-border dimension of the analysis is captured through several variables that
reflect international and regional heterogeneity. Specifically, Customer_Country iden -
tifies the consumer's country of residence, Shipping_Region defines the logistics des -
tination zone, and Product_Category incorporates region-specific product availability.
Additionally, a Cultural_Proximity index was constructed using external cultural dimen-
sion scores (e.g., Hofstede's cultural dimensions) to quantify the similarity between the
consumer's country and the seller's country. However, the dataset does not contain
direct variables for local currency, language preference, or country-specific regulatory
conditions. This limitation is acknowledged as an area for future validation, and the
authors recommend the collection of more granular cross-border variables in subse -
quent research to strengthen the cultural adaptability assessment of the framework.
Table 2 Input feature description
Feature name Source Data type Preprocessing Interpretation
Customer_Age User profile Numerical Min–Max scaling Customer age in years
Customer_Gender User profile Categorical One-hot encoding Gender category
Customer_Country User profile Categorical One-hot encoding Country of residence
Session_Duration Clickstream Numerical Log transformation Time spent per session
(seconds)
Pages_Viewed Clickstream Numerical Min–Max scaling Number of pages viewed
per session
Click_Through_Rate Clickstream Numerical Min–Max scaling Ratio of clicks to impressions
Previous_Purchases Transaction
history
Numerical Min–Max scaling Total prior purchase count
Avg_Purchase_Value Transaction
history
Numerical Z-score
normalization
Historical average spending
per order
Product_Category Transaction
history
Categorical One-hot encoding Product category purchased
Transaction_Frequency Transaction
history
Numerical Min–Max scaling Purchases per unit time
Payment_Method Transaction
history
Categorical One-hot encoding Payment type (credit, digital
wallet, etc.)
Shipping_Region Logistics data Categorical One-hot encoding Regional shipping zone
Delivery_Time Logistics data Numerical Min–Max scaling Average delivery duration
(days)
Logistics_Score Logistics data Numerical Min–Max scaling Composite logistics perfor-
mance indicator
Cultural_Proximity External data Numerical Min–Max scaling Cultural similarity index (0–1
scale)
Market_Growth_Rate External data Numerical Z-score
normalization
Regional e-commerce
market growth rate

Page 17 of 33
Chen Discover Internet of Things            (2026) 6:225
4.2 Hardware and execution environment
The proposed QFDL-CBDMA framework has been realized by simulating a hybrid
quantum–classical environment in python. The experimental setting could be realized
on a workstation running an Intel Core i9 processor (3.6 GHz), with 64 GB of memory
and an NVIDIA RTX 4090 graphics card, with 24 GB of dedicated memory, for accel -
erated quantum circuit simulation and deep learning calculations. The classical deep
learning operations and the modelling of quantum circuits were implemented using the
software environment of Python 3.10 with the help of the libraries TensorFlow, PyTorch,
Qiskit and PennyLane. The parameterized quantum circuit simulators were embedded
in the hybrid learning pipeline for quantum simulation experiments. GPU acceleration
was utilized in the model training process, facilitating them with efficient processing of
high-dimensional, multi-modal e-commerce data. In the training of the QFDL-CBDMA
framework, the learning rate used was 0.001, the number of epochs used was 100 and
the batch size used was 64. To enhance the convergence stability and computation effi -
ciency, adaptive learning rate scheduling and early stopping criterion was also imple -
mented. The average time to train the entire experimental run was around 3.8 h with the
mentioned configuration of hardware, and the average inference time per batch was less
than 120 ms. The implementation details provided reproducibilities support and dem -
onstrate the practical feasibility of the proposed quantum-enhanced digital marketing
analytics framework in terms of computational feasibility.
4.3 Experimental setup
The QFDL-CBDMA framework was trained using Quantum Gradient Descent with
parameter-shift gradient estimation, a learning rate of 0.001, batch size of 64, and 100
training epochs. Adaptive learning-rate scheduling, early stopping, and a fixed random
seed of 42 were employed to ensure stable convergence and reproducibility. The dataset
was divided into training, validation, and testing subsets using a 70:15:15 ratio for model
development and evaluation. Experiments were conducted in a simulator-based hybrid
quantum–classical environment using Python-based quantum machine learning librar -
ies on a workstation with Intel Core i9 CPU, 64 GB RAM, NVIDIA RTX GPU, and Linux
operating system.
The target variable, marketing effectiveness, was defined as a binary construct derived
exclusively from post-exposure behavioral outcomes that are not included in the pre -
dictor feature set. Specifically, an observation was classified as having high marketing
effectiveness if the customer completed a purchase within a 30-day observation window
following campaign exposure and the transaction value exceeded $100 (USD). Other -
wise, it was classified as low effectiveness. This definition ensures complete indepen -
dence between the target variable and the predictive features listed in Table  3, thereby
eliminating any risk of target leakage. The resulting class distribution yielded 3,540 high-
effectiveness cases (29.5%) and 8,460 low-effectiveness cases (70.5%), reflecting a realis -
tic imbalance typical of e-commerce conversion scenarios.
The IoT robustness experiments were conducted under controlled simulation con -
ditions rather than involving physical IoT infrastructure. All perturbations—including
communication latency, missing-data scenarios, sensor-quality degradation, noise injec -
tion, and scalability variations—were artificially introduced into the pre-processed data -
set through systematic data manipulation procedures. Latency conditions (50, 100, 200,

Page 18 of 33
Chen Discover Internet of Things            (2026) 6:225
and 500 ms) were simulated by applying corresponding temporal delays to timestamped
transactional records. Missing-data scenarios (80 and 60% completeness) were gener -
ated through random deletion of feature values according to a missing-at-random mech-
anism. Sensor-quality degradation was emulated by adding zero-mean Gaussian noise
with increasing variance to the logistics-related features. These controlled simulation
procedures enable systematic evaluation of model robustness under standardized per -
turbation conditions while maintaining experimental reproducibility.
The statistical validation was conducted using 10-fold cross-validation with identical
data partitions applied consistently across all compared models. For each fold, the data -
set was partitioned into training and testing subsets, and all models were trained and
evaluated on exactly the same subsets. Confidence intervals (95%) were calculated using
the percentile bootstrap method with 1,000 resampling iterations applied to the cross-
validation accuracy scores. Paired t-tests were performed to compare the proposed
QFDL-CBDMA framework against each baseline model, using the per-fold accuracy dif-
ferences between the two models as the paired observations. The p-values reported in
Table 6 correspond to two-sided t-tests under the null hypothesis that the mean accu -
racy difference between the compared models is zero. This experimental design ensures
that the statistical comparisons are fair, consistent, and interpretable.
The QFDL-CBDMA framework was implemented using a simulator-based hybrid
quantum–classical environment. Quantum circuit simulation was performed using Pen-
nyLane 0.38.0 integrated with PyTorch 2.3.1, while classical processing and optimiza -
tion were executed using Python 3.11. All experiments were conducted in a Linux-based
environment with GPU acceleration to ensure efficient training and evaluation.
Table 3 presents the dataset characteristics, including transaction volume, feature
details, data format, and temporal coverage. The dataset consists of large-scale tabular
e-commerce transaction records suitable for machine learning-based marketing analysis.
The QFDL-CBDMA framework is evaluated on the E-Commerce Transactions Data -
set using 10-fold cross-validation. It achieves 98.5% average accuracy (SD = 0.41) with a
95% confidence interval of [97.9, 99.1%], significantly outperforming baseline models ( p
< 0.05). Key performance metrics include ROI, customer engagement, AOV, and cross-
cultural insight. Regularization, batch normalization, and early stopping are employed
to prevent overfitting, with convergent training and validation loss curves confirming
generalization stability.
Table 3 Dataset parameters
Parameter Details
Number of records Approximately 500,000+ transactions (typical for
mid-sized e-commerce datasets)
Data file size Estimated 2–5 MB (CSV or similar structured format)
Number of features/columns Around 10–15 features (including IDs, quantities,
prices, timestamps, and location)
Image data None (dataset focuses on transactional tabular data)
Categories Multiple product categories included
Temporal span Usually covers 1–3 years of transactions
Data format CSV, suitable for most machine learning frameworks

Page 19 of 33
Chen Discover Internet of Things            (2026) 6:225
4.4 Predictive accuracy
A model's predictive accuracy in e-commerce is its ability to forecast future events, such
as consumer behaviour and sales patterns, by combining historical data with advanced
analytics, such as machine learning. By analysing multi-modal transaction data, the
proposed QFDL-CBDMA  accurately predicts the best marketing outcomes, such as
customer engagement levels and purchase decisions. After 100 training epochs on the
E-Commerce Transactions Dataset, the proposed QFDL-CBDMA algorithm progres -
sively improves its predictive accuracy, as shown in Fig.  5. Starting in the first epoch
of training (85.4% vs. 78.9% for AI-MPM), the proposed model consistently outper -
forms the reference conventional methods CBER-DL, DL-CBP , and EL-ER. The pro -
posed model has been selected because it achieves more accuracy than the current one.
Compared with AI-MPM's greatest classical improvement of 93.0% at epoch 100, the
quantum-enhanced fusion approach enables faster convergence and higher precision,
achieving an astounding 98.5% completion rate. When the model converges, as shown
by the trend of decreasing returns at higher epochs, it will be able to make better predic -
tions, which are crucial for adaptive cross-border E-commerce marketing, and its capac-
ity to learn multi-modal features and market behaviours will increase. The predictive
accuracy metric evaluates the capability of the framework to correctly predict customer
behaviour and marketing outcomes. It is mathematically represented as Eq. (16):
 𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴 𝐴 𝑇𝑇𝑇𝑇 𝑇 𝑇𝑇𝑇𝑇 𝑇𝑇𝑇𝑇 𝑇 𝑇𝑇𝑇𝑇 𝑇 𝑇𝑇𝑇𝑇 𝑇 𝑇𝑇𝑇𝑇 × 100 (16)
where 𝑇𝑇𝑇𝑇, 𝑇𝑇𝑇𝑇, 𝐹𝐹𝐹𝐹, and 𝐹𝐹𝐹𝐹 denote true positive, true negative, false positive, and false
negative predictions respectively. Higher predictive accuracy indicates improved cus -
tomer behaviour modelling and recommendation precision.
4.5 Return on investment (ROI)
ROI measures an investment's profitability and effectiveness by estimating net profit
as a percentage of overall marketing expenditure, showing how much the model's rec -
ommendations boosted the company's returns in international e-commerce situations.
Fig. 5 Predictive accuracy comparison over 100 training epochs (simulation parameters: 8 qubits, 100 epochs,
N=12,000)

Page 20 of 33
Chen Discover Internet of Things            (2026) 6:225
QFDL-CBDMA improves marketing analysis over time and evaluates the model's capac-
ity to optimize marketing impact in the face of changing market conditions and client
behaviours, as captured in the E-Commerce Transactions Dataset. The model's higher
ROI demonstrates its commercial advantage beyond predictive performance. This
is because it shows better resource use and advertising targeting. Figure  6 shows the
10-month ROI growth of the recommended Quantum Fusion Deep Learning model.
The model, which compares to AI-MPM, CBER-DL, DL-CBP , and EL-ER, provides a
higher ROI from marketing spending across all months. The E-Commerce Transactions
Dataset's top methods are examined. The suggested model's ROI reached 67.4% by the
ninth month, beating AI-MPM's 50.7%. Profitability has increased with predictive ana -
lytics and adaptive marketing budget allocation. This detailed comparison shows that the
quantum fusion model can optimize profitability in complex, multi-modal marketplaces,
affecting company decisions, and contrasts show quantum fusion's strength. Return on
Investment (ROI) measures the financial effectiveness of marketing campaigns gener -
ated using the proposed framework and is defined as Eq. (17):
 𝑅𝑅𝑅𝑅𝑅𝑅 𝑅 𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅 𝑅 𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅 𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅 × 100 (17)
where Revenue represents total campaign earnings and Cost denotes total marketing
expenditure. A higher ROI indicates more profitable digital marketing strategies.
4.6 Consumer engagement ratio
Consumer engagement includes everything done to build a long-term relationship with
customers that goes beyond just making impulse purchases. It includes the deep, one-
on-one relationship that grows between a business and its customers at every point of
interaction, whether it's online or in person. This statistic is being utilized to help peo -
ple stay interested in cross-border e-commerce marketing campaigns, suggestions, and
items in the proposed model. It shows how engaged users are by looking at clicks, repeat
visits, and transactions. It does this by using custom insights from the E-Commerce
Transactions Dataset. Figure 7 shows that the suggested model consistently outperforms
Fig. 6 Return on investment (ROI)

Page 21 of 33
Chen Discover Internet of Things            (2026) 6:225
the benchmark approaches AI-MPM, CBER-DL, DL-CBP , and EL-ER when it comes to
human engagement. The Consumer Engagement Rate (%) over the previous 10 months
shows how this has changed. The suggested model does better than AI-MPM, which
had an engagement rate of 62.4% throughout the comparative period (40.5% in the first
month and 86.9% in the tenth month). This continual progress shows that the model's
quantum synthesis of transactional, demographic, and behavioral data lets it target cus -
tomers more accurately, provide suggestions that are more relevant, and keep customers
engaged for longer periods of time in a variety of markets. The model's ability to learn
and adapt is what makes it possible for users to respond consistently well in dynamic
cross-border e-commerce settings, as seen by the gradual increase in interactions. The
Customer Engagement Ratio (CER) evaluates user interaction intensity across digital
marketing platforms and is calculated as Eq. (18):
 𝐶𝐶𝐶𝐶𝐶𝐶 𝐶 𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶 𝐶 𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶 𝐶 𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶 𝑇𝑇𝑇𝑇𝑇𝑇𝐶𝐶𝐶𝐶 × 100 (18)
where higher CER values indicate stronger customer interaction, engagement, and cam -
paign responsiveness.
4.7 Average order value (AOV)
Online businesses rely on AOV as a key performance indicator since it shows customers'
spending habits. Increases in AOV lead to increased revenue and profit as customers
spend more on each purchase. To find out if the suggested model's quantum-backed,
personalized recommendations and insights inspire customers to make more valuable
purchases and interact across borders, AOV can be utilized. Optimizing marketing and
pricing strategies, the model maximizes order value using data from the multi-modal
E-Commerce Transactions Dataset. Make a tally of how often customers buy and cat -
egorize them according to their purchasing habits. Among the models tested over a
10-month period, Quantum Fusion Deep Learning model proved to be the most effec -
tive, as shown in Fig.  8. In the first month, AI-MPM had an average order value (AOV)
of 64.5%; by the tenth month, the suggested model had increased to 89.7. Client expen -
diture rises as a result of enhanced customization, dynamic pricing, and the fusion of
Fig. 7 Consumer engagement ratio

Page 22 of 33
Chen Discover Internet of Things            (2026) 6:225
features powered by quantum computing. Consistently increasing transaction values
show that the model can adjust to the tastes of international customers and stimulate
substantial spending in a number of different nations. Average Order Value (AOV)
measures the average spending amount per customer transaction and is expressed as
Eq. (19):
 𝐴𝐴𝐴𝐴𝐴𝐴 𝐴 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇  (19)
Higher AOV values indicate successful personalized recommendation strategies and
increased customer purchasing behaviour.
4.8 Cross-cultural insight score
Businesses use the Cross-Cultural Insight Score to evaluate cross-cultural performance.
A company's cultural competence, sensitivity, and reaction can be assessed by the Fig.  9.
The model uses quantum-enhanced feature fusion to improve on previous attempts.
This helps analyze complex cross-market relationships and create location-specific
solutions. A higher insight score indicates a model that can adapt and thrive across dif -
ferent cultures to optimize cross-border e-commerce and global marketing. Contrasts
AI-based techniques with the Quantum Fusion Deep Learning model. Also shown are
Ten international markets' Cross-Cultural Insight Scores. The suggested strategy is more
sensitive to cultural and behavioral differences in transaction data between locales.
China and India are fast-paced markets where the proposed strategy obtains 96.7% and
97.4% respectively. This increase comes from the model's ability to combine datasets into
coherent quantum features. Purchase patterns, time preferences, and location-related
actions are characteristics. High ratings across all markets make the model useful for
cross-border e-commerce analytics, where it improves locally adapted marketing strate -
gies. The Cross-Cultural Insight Score (CCIS) evaluates the ability of the framework to
adapt marketing analytics across multiple geographic and cultural regions as shown in
Eq. (20):
 𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶 𝐶
∑
𝑁𝑁
𝑖𝑖𝑖𝑖 𝐶𝐶𝑖𝑖
𝑁𝑁 × 100 (20)
Fig. 8 Average order value (AOV)

Page 23 of 33
Chen Discover Internet of Things            (2026) 6:225
where 𝐶𝐶𝑖𝑖  represents region-specific cultural adaptation performance and 𝑁𝑁 denotes the
number of international markets considered. Higher CCIS values indicate improved
localization and cross-cultural recommendation capability.
T o assess the effect of the uneven distribution of IoT data across cultures, the data
has been split out into various region groups according to the behavior patterns of the
consumers, their demographic features, and availability of IoT data. The results of the
models were evaluated based on the accuracy variation, the confidence intervals and
the prediction error between groups. The results showed that QFDL-CBDMA frame -
work maintained stable performance under various data distributions with variations in
accuracy of < ± 1.8% and F1 score of < ± 2.1%. This shows the ability of the proposed
approach to generalize in a heterogeneous cross-border IoT environment.
4.9 Quantum feature entanglement score
The Quantum Feature Entanglement Score (QFES) measures quantum entanglement
between multi-modal features stored in quantum states within the QF-NN model.
Higher QFES values allow more expressive feature combinations, improving prediction
accuracy. QFDL-CBDMA, EL-ER, AI-MPM, CBER-DL, and DL-CBP are compared in
Fig. 10a, b. With all data points and time intervals, QFDL-CBDMA consistently achieves
the highest QFES (0.85–0.97), indicating well-entangled features. EL-ER and AI-MPM
have moderate QFES scores of 0.70–0.85. CBER-DL and DL-CBP have lower QFES val -
ues of 0.60–0.75. These statistics indicate that the QFDL-CBDMA architecture inte -
grates entanglement-based characteristics better than other systems, which is beneficial
for high-dimensional quantum-enhanced learning in cross-border retail analytics. The
Quantum Feature Entanglement Score (QFES) measures the effectiveness of entangled
quantum feature interactions within the QFDL-CBDMA framework as given in Eq. (21):
 𝑄𝑄𝑄𝑄𝑄𝑄𝑄𝑄 𝑄 1 𝑁𝑁 ∑ 𝑁𝑁 𝑖𝑖𝑖𝑖 |⟨𝜓𝜓𝑖𝑖 |𝜙𝜙𝑖𝑖 ⟩|2 (21)
where |𝜓𝜓𝑖𝑖 ⟩ and |𝜙𝜙𝑖𝑖 ⟩ denote interacting quantum feature states. Higher QFES values indi -
cate stronger quantum feature representation and cross-modal learning efficiency.
Fig. 9 Cross-cultural insight score

Page 24 of 33
Chen Discover Internet of Things            (2026) 6:225
The proposed model outperforms classical and traditional deep learning methods in
ROI, predicted accuracy, customer engagement, average order value, and cross-cultural
insight score. Quantum-based parameter-shift gradient estimation improves predictions
and solves the E-Commerce Transactions Dataset faster. At 100 epochs, predicted accu -
racy is 98.5%, higher than the best classical model's 93%. ROI over 66% shows financial
improvements after 10 months. The discovery highlights quantum hardware and scal -
ability difficulties. The program efficiently handles multi-dimensional e-commerce data
and adapts international marketing campaigns using adaptive insights.
4.10 Quantum complexity gain score (QCGS)
The potential efficiency and effectiveness gains from using quantum-enhanced models
were a main driver for developing QCGS; this is why it emphasizes difficult deep learn -
ing applications. Even when quantum computing has a higher prediction level, there will
be a cost associated with the added complexity of processing the data when using quan -
tum resources. These types of problems that require high-dimensionality and multi-
modality require an abundance of processing when dealing with quantum systems. This
rank speaks to the cost–benefit analysis of these upgrades. Attached is a table comparing
the 10-month QCGS score of the proposed model QFDL-CBDMA to the more conven -
tional models EL-ER, AI-MPM, CBER-DL, and DL-CBP; the data show that a quantum-
enhanced model can outperform the traditional models at a higher level of the QCGS.
At the end of the first month, the scores were clearly in favour of the QFDL-CBDMA
model, which increased from the initial score of 0.92 at the end of the month to a per -
fect score of 1.00 after the tenth month. In fact, the QFDL-CBDMA model produced
a score consistently higher than the other models, particularly regarding progress over
time, as compared to the previous models, making that model the most appropriate. As
shown in Table  4, different models improved their scores over time, although on aver -
age at a slower rate, which further demonstrated that, on average, the QFDL-CBDMA
model was also the best model. As compared to the QFDL-CBDMA quantum-enhanced
model, the traditional models continue to correct to predict the consumer's estimated
fare before check-out, but at a slower and much less efficient rate over time. The Quan -
tum Complexity Gain Score (QCGS) evaluates the computational advantage obtained
through quantum-enhanced learning mechanisms and is represented as Eq. (22):
(a)                                                                           (b)
Fig. 10 Quantum feature entanglement score

Page 25 of 33
Chen Discover Internet of Things            (2026) 6:225

𝑄𝑄𝑄𝑄𝑄𝑄𝑄𝑄 𝑄 𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 𝑄𝑄𝑃𝑃𝑃𝑃𝐶𝐶𝐶𝐶𝐶𝐶𝑃𝑃𝐶𝐶𝐶𝐶𝑃𝑃𝑃𝑃𝑃𝑃𝐶𝐶  (22)
Higher QCGS values indicate improved predictive efficiency and optimization capabil -
ity relative to computational cost. Collectively, these evaluation metrics demonstrate
the predictive strength, business effectiveness, customer interaction capability, cul -
tural adaptability, and quantum learning efficiency of the proposed QFDL-CBDMA
framework.
4.11 Ablation study analysis
The ablation analysis was extended beyond predictive accuracy to include Customer
Engagement Ratio (CER) and Cross-Cultural Insight Score (CCIS), as reported in
Table A3. The complete QFDL-CBDMA framework achieved CER of 86.9% and CCIS
of 96.7%. Removing Quantum Encoding (QE) reduced CER to 80.2% (a 6.7 percentage-
point decline), attributable to the inability of classical embedding layers to capture the
non-linear interactions among heterogeneous IoT modalities such as logistics signals
and behavioral traces. Without Entanglement-Based Fusion (EBF), CCIS dropped by
4.9 percentage points, indicating that quantum entanglement is particularly effective for
modeling cross-cultural patterns that require simultaneous consideration of multiple
weakly correlated regional indicators. The performance degradation patterns observed
in CER and CCIS are more pronounced than those in accuracy for the QE-removal and
EBF-removal variants, suggesting that quantum-inspired components contribute most
substantially to engagement prediction and cultural adaptation, which rely heavily on
sparse, high-dimensional interactions among cross-border IoT data streams.
Further, by changing the amplitude and hybrid angle quantum encoding to classical
feature concatenation, there was noticeable degradation in the prediction stability and
customer engagement analysis, revealing the significance of quantum state representa -
tion for scalable multi-modal learning. The ablation results further indicated that the
efficiency of feature extraction and the modelling of cross-cultural insights play a sig -
nificant role in the modelling of quantum neural networks (QF-NN) based on quantum
parallelism and entanglement operations. The results of the experiments indicate that
the mean predictive generalization, convergence behaviour and performance of adaptive
digital marketing analytics are improved with QF-NN, QGD optimization, and quantum
feature fusion as compared with the partial mode and classical-only mode.
All models were trained and tested on the same computing platform to make sure
there was no experimental bias. All the pre-processing operations, such as handling
Table 4 Quantum complexity gain score (QCGS)
Time (months) QFDL-CBDMA EL-ER AI-MPM CBER-DL DL-CBP
1 0.92 0.85 0.80 0.78 0.82
2 0.93 0.86 0.81 0.79 0.83
3 0.94 0.87 0.82 0.80 0.84
4 0.95 0.88 0.83 0.81 0.85
5 0.96 0.89 0.84 0.82 0.86
6 0.96 0.90 0.85 0.83 0.87
7 0.97 0.91 0.86 0.84 0.88
8 0.98 0.92 0.87 0.85 0.89
9 0.99 0.93 0.88 0.86 0.90
10 1.00 0.94 0.89 0.87 0.91

Page 26 of 33
Chen Discover Internet of Things            (2026) 6:225
missing data, feature normalization, categorical encoding, transaction balancing, and
feature standardization, were performed for all the comparative methods before train -
ing the models. Moreover, all the models were stratified similarly to have a balanced
representation of customer and regional transaction categories. The proposed QFDL-
CBDMA framework outperformed the other ones consistently on the same test setting
with the incorporation of quantum-enhanced feature fusion, quantum representation
learning using entanglement and Quantum Gradient Descent optimization. They are
standardized experimental procedures; that is, the proposed framework is not respon -
sible for the reported improvements because of the variations in the training configura -
tion and/or the pre-processing conditions in which the data were used.
All baseline models (AI-MPM, CBER-DL, EL-ER, and DL-CBP) were trained, opti -
mized and tested with the same dataset, pre-processing pipeline, hardware platform,
evaluation metrics and hyperparameter optimization strategy to make a fair compari -
son. To avoid any possible experimental bias, the train-validation-test splits and early
stopping criteria were the same for all the models. For the comparison of robustness,
10-fold cross-validation was also carried out, and the QFDL-CBDMA was tested with an
average accuracy of 98.5% with a low deviation of ± 0.41, showing a stable result with dif-
ferent partitions of the data. To prevent overfitting, dropout, batch normalization, adap-
tive learning-rate scheduling and L2 regularization were employed. The cross-validation
and robustness analysis demonstrate that the findings of the performance improvements
are statistically valid, repeatable and not simply a result of overfitting and unfair experi -
mental conditions.
The ablation study of the QFDL-CBDMA framework is then carried out, one by one,
as shown in Table  5. The overall model had the best performance, and removing one
or more of the four additional elements (Quantum Encoding (QE), Entanglement-Based
Fusion (EBF), QF-NN, and Quantum Gradient Descent (QGD)) decreased the per -
formance. The contribution of each component to predictive performance and model
robustness is shown in the results that are reported as mean accuracy, standard devia -
tion and 95% confidence intervals derived from 10-fold cross-validation.
Both the complete QFDL-CBDMA and the single part of the framework showed a
measurable performance drop when one of the components was removed, and the best
predictive performance was obtained with the complete version. The observed decreases
highlight the complementary benefits of the four aspects of Quantum Encoding for fea -
ture representation, Entanglement-Based Fusion for cross-modal interaction learning,
QF-NN for quantum-enhanced feature extraction and QGD for optimization efficiency.
The results of the ablation are presented quantitatively to support the effectiveness anal -
ysis of the components.
Table 5 Ablation analysis of QFDL-CBDMA components
Model variant Accuracy (%) Std. dev 95% confidence interval
Full QFDL-CBDMA 98.50 0.42 [97.98, 99.02]
Without quantum encoding (QE) 95.84 0.61 [95.08, 96.60]
Without entanglement-based fusion (EBF) 96.27 0.57 [95.56, 96.98]
Without QF-NN 94.92 0.73 [94.01, 95.83]
Without QGD 96.01 0.65 [95.20, 96.82]

Page 27 of 33
Chen Discover Internet of Things            (2026) 6:225
Table 6 uses numerous key performance indicators to compare cross-border e-com -
merce digital marketing approaches. QFDL-CBDMA excels in projected accuracy, ROI,
customer engagement, AOV, CCI, QFIS, and QCGS. QFDL-CBDMA shows that the
quantum computing-based adaptive marketing and real-time insights outperformed the
competitors. EL-ER performed poorly on CE, CCI, and predictive accuracy, especially
in feature entanglement. Other experimental methods improve predicted accuracy in
some parameters but not others. The table shows that QFDL-CBDMA is best for solving
complicated, high-dimensional e-commerce data problems since it incorporates recent
quantum breakthroughs.
The results of the statistical validation using 10-fold cross-validation are presented
in Table 7. Mean accuracy with standard deviation and 95% confidence intervals, along
with paired t-test p-values, are reported for the performance of the proposed QFDL-
CBDMA framework and baseline models. All models were evaluated on the same parti -
tion of the data set, the same preprocessing approach, the same representation of the
features and the same evaluation metrics, in order to provide a fair and unbiased com -
parison. The statistical analysis gives evidence of the strength, consistency and signifi -
cance of the observed differences in performance. Additionally, error bars representing
the 95% confidence intervals were incorporated into the performance comparison fig -
ures to visually demonstrate model uncertainty and stability.
For assessing prediction uncertainty with noise in the quantum simulation, the QFDL-
CBDMA framework was evaluated with different levels of noise perturbation added
to the simulated quantum circuits. Noise variations of 0, 5, 10 and 15% were used for
both the quantum state encoding and the quantum state measurement. Three measures
of model performance are used: accuracy, F1-score and prediction deviation. The out -
comes indicated that the framework was robust and tolerable to moderate quantum sim-
ulation disturbances, with an accuracy of 98.50% in the absence of noise and 96.82% at
15% noise.
The proposed QFDL-CBDMA framework was comprehensively validated by experi -
mental testing using various performance measures along with comparative studies.
Table 6 Performance comparison
Method Predictive
accuracy
ROI Customer
engagement
AOV Cross-cul-
tural insight
QFES QCGS
QFDL-CBDMA 98.5 67.4 86.9 89.7 96.7 0.97 1.00
EL-ER 91.5 58.3 75.2 72.3 83.2 0.80 0.94
AI-MPM 93.0 60.0 79.4 75.1 85.5 0.85 0.89
CBER-DL 92.4 62.1 81.0 77.5 88.0 0.78 0.87
DL-CBP 90.2 59.8 72.3 74.0 82.6 0.76 0.91
Table 7 Statistical performance comparison of QFDL-CBDMA and baselines
Model Accuracy (%) Std. dev 95% CI p-value
QFDL-CBDMA 98.50 0.42 [97.98, 99.02] –
CNN 94.30 0.76 [93.36, 95.24] 0.003
LSTM 95.10 0.69 [94.24, 95.96] 0.002
DNN 93.80 0.81 [92.80, 94.80] 0.001
Random forest 91.60 0.93 [90.45, 92.75] < 0.001

Page 28 of 33
Chen Discover Internet of Things            (2026) 6:225
Prediction accuracy, error-based metrics, and comparison with other learning methods
are taken into account to evaluate the effectiveness and generalization ability of the pro -
posed method. It is also noted that the experimental setup, training conditions and cal -
culations performed are also reported to enhance transparency and reproducibility. The
validation processes show the robustness and applicability of the proposed framework
for cross-border e-commerce marketing analytics.
For evaluation of scalability under high-volume IoT conditions, more experiments
were carried out by expanding the size of the incoming IoT data streams. The framework
was validated with increased data sizes of 10,000, 50,000 and 100,000 IoT records and
tracked the accuracy of the prediction, F1-score and computational stability. The results
showed that the QFDL-CBDMA framework exhibited consistently good prediction
accuracy, showing minimal variations within 1.5% for varying numbers of data; hence, it
is robust for handling large-scale data generated by IoT.
The cross-cultural sample size of the IoT was small, and the generalization capability
of the framework was further examined. To simulate data scarcity conditions, subsets of
10%, 20% and 30% of the regional samples were used. The proposed framework retained
the consistency of the accuracy, with a decrease from the full dataset evaluation of less
than 2.3%. The results show that the model is capable of successfully capturing mean -
ingful patterns in the heterogeneous marketing data of the IoT, even in the presence of
lesser representation of certain cultural groups.
5 Discussion
The proposed QFDL-CBDMA framework offers practical advantages for cross-border
e-commerce groups, facilitating intelligent and adaptive marketing decisions. The sys -
tem helps companies learn more about consumer behavior, regional trends, and pref -
erences, and make more informed decisions about their marketing strategies. The
proposed system combines the multi-modal consumer and market information, enabling
efficient resource allocation, better customer engagement and faster responsiveness to
the changing international market conditions.
The proposed QFDL-CBDMA framework explores how hybrid quantum–classical
learning techniques can be used in cross-border e-commerce analytics in a simulator
environment. The main one is the work done in the modelling of complex multi-modal
marketing data using quantum-inspired feature representation, quantum fusion and
optimization methods. The study will not show quantum computational advantages at
the hardware level, but rather will concentrate on the efficacy of these mechanisms with
the aim of improving representation learning and predictive performance.
Several approaches are explored to reduce the uncertainty of prediction, such as
quantum noise mitigation techniques, repeated circuit measurement averaging, adap -
tive calibration of quantum parameters and robust training by varying cross-cultural
IoT samples. Moreover, to mitigate the biases from uneven data distribution across
regions, domain adaptation techniques and continuous learning mechanisms can be
applied, which enhance the reliability of the model in dynamic cross-border e-commerce
settings.

Page 29 of 33
Chen Discover Internet of Things            (2026) 6:225
Moreover, in hybrid edge-cloud deployments, caching pre-computed quantum
state embeddings at the edge nodes can substantially reduce network latency, thereby
enabling real-time adaptive marketing analytics even for geographically distributed
cross-border e-commerce operations, without compromising prediction fidelity.
6 Limitations
The simulator-based implementation of QFDL-CBDMA requires 8 qubits and 144 train-
able quantum parameters per forward pass. Extrapolating to the full 500,000-record
dataset would necessitate approximately 4 million circuit evaluations per epoch under
the parameter-shift rule, which the current simulation environment completes in 3.8 h.
On near-term NISQ devices, the same circuit would require 8 physical qubits with an
estimated gate fidelity exceeding 99.9% to maintain the observed prediction accuracy. At
typical NISQ error rates of 10 −3 to 10 −2 per two-qubit gate, the effective circuit fidelity
would drop below 95%, corresponding to an estimated accuracy degradation of 2.5–4.0
percentage points based on extrapolated results. Regarding scaling to larger IoT data -
sets, the logarithmic qubit scaling of amplitude encoding ensures that 12 qubits could
represent up to 4,096-dimensional feature vectors, sufficient for 80% of the full datas -
et's dimensionality. However, the primary bottleneck is classical-quantum data transfer
latency rather than qubit count. To mitigate NISQ-era noise, two compatibility strate -
gies are proposed: (1) zero-noise extrapolation on expectation values to correct readout
errors, and (2) incorporation of randomized compilation into the QGD parameter-shift
gradients to suppress coherent errors without modifying the optimizer structure.
7 Conclusion
Within the scope of the simulator-based experimental environment and the E-Com -
merce Transactions Dataset employed in this study, the proposed QFDL-CBDMA
framework consistently outperformed the implemented baseline models across mul -
tiple evaluation metrics. These results should be interpreted as evidence that quan -
tum-inspired representation and optimization mechanisms offer promising alternative
learning pathways for multi-modal cross-border e-commerce marketing analytics. How-
ever, the observed performance gains are contingent upon the specific dataset charac -
teristics, the chosen baseline configurations, and the simulator-based implementation;
they do not establish general superiority of quantum–classical hybrid architectures in all
e-commerce contexts.
Moreover, businesses can quickly adjust to market changes, optimize campaign per -
formance and make efficient resource allocations by applying quantum insights to opti -
mization. This can be particularly beneficial for multinational eCommerce companies
looking to keep up with the fast-changing digital landscape of consumers. Therefore, the
proposed system is not only expected to assist in the development of advanced compu -
tational marketing analytics but also to offer business intelligence support in the long
run to boost profitability, customer satisfaction, and competitiveness in the global mar -
ket. Additional studies in this field could pave the way for new developments that help
the global e-commerce ecosystem grow over the long run.
The proposed QFDL-CBDMA framework exhibits competitive predictive perfor -
mance and robustness under the considered experimental conditions. The framework
mitigates the effects of noise using quantum-inspired processing and optimization

Page 30 of 33
Chen Discover Internet of Things            (2026) 6:225
methods, but it can't entirely remove the impact of noise. The results achieved suggest
better learning capability with the quantum datasets and quantum simulation environ -
ment tested, and further testing with physical quantum hardware and with larger-scale
IoT environments is needed.
The QFDL-CBDMA framework was found to have better predictive performance
when applied to the cross-border e-commerce IoT marketing dataset considered in
the simulator-based hybrid quantum–classical environment. The findings suggest that
the combination of quantum encoding, quantum fusion mechanisms, and deep learn -
ing elements enhances feature representation and the effectiveness of predictions in
the simulated experimental setup. The results are valid for the data set studied, baseline
comparisons and the simulation conditions and need to be expanded through further
testing with different sets of data, real-world IoT deployments and physical quantum
platforms.
Appendix
Hyperparameter configuration of QFDL-CBDMA
To ensure reproducibility, all implementation parameters of the QFDL-CBDMA frame -
work are summarized in Appendix Table 8. The reported settings include classical pre -
processing architecture, quantum encoding configuration, quantum circuit parameters,
quantum fusion settings, QGD optimization parameters, and training controls. These
hyperparameters were fixed throughout all experiments to ensure consistency, fair com-
parison, and repeatable evaluation.
Supplementary materials are provided that give a complete description of the prepro -
cessing that was performed on the data for both the dataset preparation and the model
development. A total of 12,000 cross-border e-commerce records were first gathered and
then quality checked. Duplicate records (2.1% of the data) were removed and mean values
were used for numerical features, and mode values were used for categorical features,
when the values were missing, which is less than 5% of the data for all features. Min–Max
scaling was used to scale the numerical features to the range of [0,1] and one-hot encod -
ing was applied to the categorical features, resulting in 16 input features for the model.
Manufacturing features such as customer engagement score, transaction frequency, aver-
age purchase value, and logistics performance indicators were created. Data was then
split into a training set of 8,400 samples (70%), a validation set of 1,800 samples (15%)
and a test set of 1,800 samples (15%) through stratified sampling keeping the class distri-
bution. The supplementary materials include all preprocessing scripts, settings and the
workflow for the implementation of the proposed framework to enable its reproduction
and independent validation.
To ensure fully reproducible comparisons, Table 9 reports the optimized hyperparam -
eters for each baseline model implemented in this study. All baseline models were trained
using the same training-validation split (70:15:15), random seed (42), and early stopping
criterion (patience of 10 epochs) as the proposed QFDL-CBDMA framework. Hyperpa -
rameter tuning was performed via grid search over predefined ranges, with the optimal
configuration selected based on validation accuracy.

Page 31 of 33
Chen Discover Internet of Things            (2026) 6:225
Author contributions
Xi Chen: Conceptualization, Methodology, Investigation, Writing—Original Draft, Writing—Review and
Editing, Supervision, Project Administration.
Funding
This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.
Data availability
The primary dataset used in this study is the E-Commerce Transactions Dataset, publicly available on the Kaggle platform
at: https://www .kaggle.com /datasets/s mayanj/e -commerce-transactions-dataset. This synthetic dataset contains
50,000 fictional e-commerce transaction records, including user demographics, product categories, purchase amounts,
payment methods, and transaction dates. The dataset is synthetic and does not contain real user data; it can be used for
research, experimentation, and educational purposes. Additional publicly available data sources consulted for market
trends and consumer behavior context include the UCI Online Retail Dataset (available at:  h t t p s  : / / a r c  h i v e .  i c s .  u c i . e d u / d a t a
s e t / 3 5 2 / o n l i n e + r e t a i l )     reference [6].
Declarations
Ethics approval and consent to participate
Not applicable.
Consent for publication
Not applicable.
Table 8 Hyperparameter configuration of QFDL-CBDMA
Parameter Value
Input feature dimension 16
Classical dense layers 256, 128 neurons
Activation function ReLU
Batch normalization Enabled
Dropout rate 0.30
Number of qubits 8
Quantum encoding method Amplitude encoding + hybrid angle encoding
Quantum circuit depth 6 variational layers
Rotation gates Rx, Ry, Rz
Entanglement operation CNOT gates
Quantum fusion layer Parameterized unitary transformation
Trainable quantum parameters 144
Measurement strategy Pauli-Z expectation values
Optimizer Quantum gradient descent (QGD)
Gradient estimation Parameter-shift rule
Learning rate 0.001
Batch size 64
Maximum epochs 100
Early stopping patience 10 Epochs
Learning rate scheduling Adaptive
Random seed 42
Training-validation-test split 70:15:15
Cross-validation 10-Fold
Computational environment Hybrid quantum–classical simulator
Table 9 Hyperparameter configurations of baseline models
Model Hyperparameters
CNN Filters: 64, 128, 256; Kernel size: 3×3; Activation: ReLU; Pooling: MaxPool2d; Dropout: 0.25;
Optimizer: Adam (lr = 0.001)
LSTM Hidden units: 128, 64; Layers: 2; Dropout: 0.2; Bidirectional: True; Optimizer: Adam (lr = 0.001)
DNN Layers: 256–128-64-32; Activation: ReLU; Dropout: 0.3; Batch Norm: Enabled; Optimizer:
Adam (lr = 0.0005)
Random Forest Trees: 200; Max depth: 20; Min samples split: 5; Min samples leaf: 2; Features: sqrt

Page 32 of 33
Chen Discover Internet of Things            (2026) 6:225
Competing interests
The authors declare no competing interests.
Received: 8 April 2026 / Accepted: 5 October 2026
References
1. Li L. Cross‐border E‐commerce intelligent information recommendation system based on deep learning. Comput Intell
Neurosci. 2022. https://doi.org/10.1155/2022/6602471.
2. Rui C. Research on classification of cross-border E-commerce products based on image recognition and deep learning.
IEEE Access. 2020;9:108083–90. https://doi.org/10.1109/ACCESS.2020.3020737.
3. Wang W. An IoT-based framework for cross-border e-commerce supply chain using machine learning and optimization.
IEEE Access. 2023;12:1852–64. https://doi.org/10.1109/ACCESS.2023.3347452.
4. Feng L. Analysis of product selection strategy for cross-border E-commerce with assistance of artificial intelligence. J
Internet Technol. 2025;26(1):111–21. https://doi .org/10.700 03/16079264 20250126 01010.
5. Zhang Z. The evaluation of marketing competitiveness of B2B E-commerce enterprises based on optimized deep learning
networks. Int J Simul Multidiscip Des Optim. 2023;14:17. https://doi.org/10.1051/smdo/2023022.
6. Li B. Cross-border e-commerce marketing strategy based on consumer behavior in the era of big data. J Comput Methods
Sci Eng. 2023. https://doi.org/10.1177/14727978251364593.
7. Xu Y, Li L, Liang J. Cross-border e-commerce consumer behavior big data analysis and prediction model research.
In: 2025 5th Asia-Pacific conference on communications technology and computer science (ACCTCS). IEEE; 2025. p.
696–700. https://doi .org/10.110 9/ACCTCS662 75.2025. 00126.
8. Chen J, Chunqiong WU. The design of a cross-border E-commerce recommendation system based on big data technol-
ogy. In: 2021, 6th international conference on intelligent computing and signal processing (ICSP). IEEE; 2021. p. 381–84.
https://doi .org/10.110 9/ICSP51882 .2021.94 09014
9. Zhang Y, Feng Y, Zhou WJ, Ye Y, Tan M, Xiao R, Yu J. Multi-domain deep learning from a multi-view perspective for cross-
border e-commerce search. Proc AAAI Conf Artif Intell. 2024;38(8):9387–95. https://doi.org/10.1609/aaai.v38i8.28792
10. Zhao L, Wan Y. Application of AI technology in social media marketing for cross-border e-commerce: hotspot analysis
and trend forecasting. In: 2025 IEEE 8th advanced information technology, electronic and automation control conference
(IAEAC), vol 8. IEEE; 2025. p. 453–62. https://doi .org/10.110 9/IAEAC6519 4.2025.1 1165848.
11. Lu H, Liang J. Consumer behavior analysis model of cross-border e-commerce based on big data. In: 2024 international
conference on power, electrical engineering, electronics and control (PEEEC). IEEE; 2024. p. 722–26.  h t t p s  : / / d o i  . o r g /  1 0 . 1  1 0
9 / P E E E C 6 3 8 7 7 . 2 0 2 4 . 0 0 1 3 6
12. Wang Y. Evaluation of cross-border e-commerce talent cultivation based on back propagation neural network. In: 2025
international conference on intelligent systems and computational networks (ICISCN). IEEE; 2025. p. 1–6.  h t t p s  : / / d o i  . o r g /  1
0 . 1  1 0 9 / I C I S C N 6 4 2 5 8 . 2 0 2 5 . 1 0 9 3 4 1 7 9     .
13. Kang Y. Research on marketing prediction model for cross-border E-commerce enterprises based on artificial intelligence
algorithms. Int J High Speed Electron Syst. 2024:2540257. https://doi.org/10.1142/S0129156425402578.
14. Jin Z, Ye F, Nedjah N, Zhang X. A comparative study of various recommendation algorithms based on E-commerce big
data. Electron Commer Res Appl. 2024;68:101461. https://doi.org/10.1016/j.elerap.2024.101461.
15. Yao N. Research on cross-border e-commerce recommendation system based on deep learning algorithm. In: 2024, 3rd
international conference for innovation in technology (INOCON). IEEE; 2024. pp. 1–4.  h t t p s  : / / d o i  . o r g /  1 0 . 1  1 0 9 / I N O C O N 6 0 7
5 4 . 2 0 2 4 . 1 0 5 1 1 9 5 5     .
16. Jin Y. An empirical study on the development environment of cross-border e-commerce logistics in the global trade
context: exploring the digital marketing landscape. Comput Aided Des Appl. 2024;21(S4):290–305.  h t t p s  : / / d o i  . o r g /  1 0 . 1  4 7 3
3 / c a d a p s . 2 0 2 4 . S 4 . 2 9 0 - 3 0 5     .
17. Al-Otaibi YD. Enhancing e-commerce strategies: a deep learning framework for customer behavior prediction. Eng Tech-
nol Appl Sci Res. 2024;14(4):15656–64. https://doi.org/10.48084/etasr.7945.
18. Liu J, Kim H. Efficacy improvement of convolutional neural network-based artificial intelligence recommendation model
in cross-border E-commerce marketing. J Comb Math Comb Comput. 2025;127:9263–84.
19. Yang Y. The improved BP neural network supply chain performance evaluation model under the cross-border e-com-
merce marketing chain. J Comput Methods Sci Eng. 2024;24(3):1727–40. https://doi.org/10.3233/JCM-24729.
20. Dritsas E, Trigka M. Machine learning in E-commerce: trends, applications, and future challenges. IEEE Access.
2025;13:99048–67. https://doi.org/10.1109/ACCESS.2025.3572865.
21. Shankar A, Perumal P , Subramanian M, Ramu N, Natesan D, Kulkarni VR, et al. An intelligent recommendation system in
e-commerce using ensemble learning. Multim Tools Appl. 2024;83(16):48521–37.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 0 4 2 - 0 2 3 - 1 7 4
1 5 - 1     .
22. Karabila I, Darraz N, El-Ansari A, Alami N, El Mallahi M. Enhanced e-commerce recommender system based on deep learn-
ing and ensemble approaches. In: Proceedings of the 7th international conference on networking, intelligent systems and
security; 2024. pp. 1–8. https://doi.org/10.1145/3659677.3659747
23. Valencia-Arias A, Uribe-Bedoya H, González-Ruiz JD, Santos GS, Ramírez EC, Rojas EM. Artificial intelligence and recom-
mender systems in e-commerce. Trends and research agenda. Intell Syst Appl. 2024;24:200435.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . i s
w a . 2 0 2 4 . 2 0 0 4 3 5     .
24. Okeleke PA, Ajiga D, Folorunsho SO, Ezeigweneme C. Predictive analytics for market trends using AI: a study in consumer
behavior. Int J Eng Res Updates. 2024;7(1):36–49. https://doi.org/10.53430/ijeru.2024.7.1.0032.
25. Thakkar S, Kazdaghli S, Mathur N, Kerenidis I, Ferreira-Martins AJ, Brito S. Improved financial forecasting via quantum
machine learning. Quantum Mach Intell. 2024;6(27):1–18.

Page 33 of 33
Chen Discover Internet of Things            (2026) 6:225
26. Sáez-Ortuño L, Huertas-García R, Forgas-Coll S, Sánchez-García J, Puertas-Prats E. Quantum computing for market
research. J Innov Knowl. 2024;9(3):100510.
27. Wang L, Hsu HH. IoT technology in maritime logistics management: exploration of data analysis methods. Discov Internet
Things. 2025. https://doi.org/10.1007/s43926-025-00167-9.
28. Lu Y. A multimodal deep reinforcement learning approach for IoT-driven adaptive scheduling and robustness optimiza-
tion in global logistics networks. Sci Rep. 2025;15(25195):1–18. https://doi.org/10.1038/s41598-025-10512-1.
29. Xue Y, Yates N, Ghadge A. The relationship between IoT-based information integration, decision-making uncertainty, and
supply chain performance. Int J Log Res Appl; 2025. p. 1–22. https://doi .org/10.108 0/13675567. 2025.255 5491;  h t t    p  s : /  / w  w
w . k  a g g  l   e . c o  m / d a t a  s e t s / s m a y a n j / e - c o m m e r c e - t r a n s a c t i o n s - d a t a s e t
Publisher's Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
