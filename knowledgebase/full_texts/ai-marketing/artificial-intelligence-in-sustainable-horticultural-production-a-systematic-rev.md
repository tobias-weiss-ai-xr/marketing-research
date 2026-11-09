---
title: 'Artificial intelligence in sustainable horticultural production: a systematic review'
url: https://doi.org/10.1007/s44372-025-00455-2
category: ai-marketing
subcategory: case-study
date: 2025-12
venue: Discover Plants.
authors:
- Vidisha Chaudhary
- Mukesh Kumar
- Veena Chaudhary
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s44372-025-00455-2.pdf
pages: 43
chars: 187585
fetched_at: '2026-11-08T17:46:03+00:00'
kb_version: 1
---

# Artificial intelligence in sustainable horticultural production: a systematic review

REVIEW Open Access
© The Author(s) 2025. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article
are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
Chaudhary et al. Discover Plants           (2025) 2:372
https://doi.org/10.1007/s44372-025-00455-2
*Correspondence:
Mukesh Kumar
k.mukesh123@yahoo.com
1Institute of Business Studies, CCS
University, Meerut,
Uttar Pradesh 250005, India
2Department of Floriculture and
Landscape Architecture, College
of Horticulture, Sardar Vallabhbhai
Patel University of Agriculture and
Technology, Meerut,
Uttar Pradesh 250110, India
3Department of Chemistry, Meerut
College, Meerut,
Uttar Pradesh 250003, India
4Division of Floriculture and
Landscaping, ICAR-Indian
Agricultural Research Institute,
New Delhi 110012, India
Artificial intelligence in sustainable horticultural
production: a systematic review
Vidisha Chaudhary1, Mukesh Kumar2*, Veena Chaudhary3, Ravi Kumar2 and Chetan Chauhan4
1 Introduction
AI has a long history in computer science, with the overarching objective of developing
"intelligent" robots [1], however the term intelligence is not well defined, and evaluating
"intelligence" is exceedingly difficult [2]. A group of computer scientists held a workshop
at Dartmouth College in 1956, which sparked the AI discipline. The aims were exceed -
ingly ambitious: "The study will begin on the basis of the premise that any facet of learn -
ing or any other attribute of intelligence may, in principle, be so accurately characterized
that a computer can be built to replicate it. An attempt will be made to figure out how to
get computers to utilize language, develop abstractions and concepts, solve issues that
are now reserved for people and improve themselves [ 3]". DL, ML and AI are all con -
nected yet different. The following are some significant distinctions between these fields:
(a) The development of intelligent systems that are capable of learning, solving problems,
Discover Plants
Abstract
Artificial intelligence (AI) is playing a key role in making horticultural production
more efficient, sustainable, and precise. This review focuses on recent advances in AI
technologies such as machine learning (ML), deep learning (DL), and the Internet of
Things (IoT) and their applications in horticulture. AI tools like sensors, drones, and
robots help monitor crops in real time, automate tasks, and support better decision-
making. In addition, case studies show how AI can reduce resource use, improve
productivity, and address challenges like climate change and post-harvest losses.
Moreover, AI applications in various areas, including pest and disease management,
prediction of crop yield and quality, harvesting, postharvest handling, processing,
and losses of horticultural crops, cultivar classification and weed detection, retail
marketing of horticultural crops, prediction and detection of crop loss brought on
by natural calamities, soil health monitoring , irrigation management , floriculture
and landscaping, and other applications for sustainable horticultural production,
are covered in the review. Practical challenges in the adoption of AI technologies
in horticulture and future directions are also discussed for achieving sustainable
horticultural production.
Keywords Artificial intelligence, Machine learning, Deep learning, Crop sustainability,
AI-driven predictions

Page 2 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
and making decisions tasks that often require human intelligence is referred to as AI.
(b) ML is a branch of artificial intelligence that uses data patterns and insights to teach
digital machines to carry out tasks without direct instructions. (c) DL is a branch of ML
that learns and makes choices using multi-layered artificial neural networks. It is espe -
cially helpful for jobs involving the analysis of enormous volumes of data, such text (e.g.,
ChatGPT) or photos (e.g., DALL-E2). A form of artificial intelligence known as symbolic
AI uses symbols to represent information (for instance, a dog is a mammal with fur and
four legs) and then applies logical rules to manipulate those symbols in order to solve
problems. It differs from deep learning and machine learning, which identify patterns
in data instead of depending on explicit rules. Nowadays, machine learning and deep
learning are more widely utilized for applications like speech and picture recognition,
making symbolic AI less frequent. Nonetheless, there are still certain uses for symbolic
AI, including expert systems and natural language processing [4, 5].
Recently, there has been an increasing interest in using digital technologies in horti -
culture, such as ML [ 6], AI [ 7], digital twins [ 8, 9], robots [ 10], the IoT [ 11, 12], drones
[13] and DL [ 14]. The use of AI and IoT tools to digitize agriculture was emphasized by
Subeesh and Mehta [15]; Shahriar et al. [16]. The technical aspects of IoT and AI are also
covered, combined with the challenges of putting these new technologies into practice.
This will make it easier to comprehend how the integration of digital technologies can
facilitate the application of AI and IoT-based solutions in agricultural settings and be
integrated into agricultural processes. Furthermore, numerous cutting edge computer
based systems are designed to detect a wide range of important parameters, includ -
ing yield, weed, and crop quality, among many others [ 17]. In order to improve deci -
sion making, farmers including horticultural producers can now benefit from real-time
monitoring of a variety of factors gathered from their fields, such as weather, tempera -
ture, water usage or soil conditions, thanks to AI technologies. AI is utilized to create
intelligent agricultural techniques that provide high yields while minimizing losses for
farmers [18, 19] Furthermore, Javaid et al. [ 20] recommended the utilization of 3D laser
scanning and hyperspectral imaging as the leading AI-based technologies to guarantee
crop health. These AI-driven solutions gather more accurate and comprehensive data on
crop health for study.
AI systems can detect pests, diseases and undernourished plants and can even fore -
cast weather patterns and assess crop health. Drones with AI capabilities can be used
by farmers to check on the health of their crops [ 21, 22].  Moreover, Robots, sensors,
and drones were used for irrigation, weeding, and spraying in the agricultural applica -
tions of AI [18] and reported that AI based methods and tools preserve soil fertility, con-
trol labor costs effectively and improve the quality of output while also saving water and
reducing the need for pesticides and herbicides. Moreover, AI technology also help hor -
ticultural production by selection the right crop varieties, apply cutting-edge techniques
for managing soil and nutrients improve crop yields, manage pests and diseases, proj -
ect crop yields and predict commodities prices [ 23, 24]. Figure 1 shows the procedures
for implementing AI in horticultural production. It has also been well documented that
AI encourages the creation of intelligent farming techniques that maximize yields while
minimizing production losses [25–27]. Additionally, the integration of AI in this domain
offers numerous benefits, such as automating sorting and grading processes enhancing
accuracy, reducing labor, time demands and improving overall production rates [28].

Page 3 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
Additionally, wireless sensors with fuzzy controllers have been suggested for irrigation
system automation [29–31]. The use of microcontroller units to enable a smart irrigation
system was suggested by Xiao and Liu [ 32]. A feedforward neural network with one or
more hidden layers positioned between the input and output layers are called a multi -
layer perceptron (MLP). Nonlinear activation functions are used by the nodes (neurons)
in each layer to identify intricate patterns in the data. A smart controller for a water irri -
gation system based on MLP neural networks was employed by Karar et al. [31]. Modern
portable sensors are integrated into intelligent regulating systems and are employed in
protected cultivation. They allow plants to grow all year round by automatically control -
ling the plant environment. Irrespective of weather or location future big data collect -
ing will allow real-time data access via portable devices. This could make easier access
to many environmental parameters [ 33]. Currently, Zhang et al. [ 34] have highlighted
a number of sensor types such as AM 2303 for temperature and humidity monitoring,
COZIR-W, OGM220 for CO 2 management, 5TE, ECH2O, EC-5, SM100, SM150T for
soil moisture monitoring and PH8ERP , PH8EFP for pH monitoring.
AI is increasingly recognized as a transformative tool in achieving sustainable, efficient
and precise horticultural production. While several studies have reported on the appli -
cations of AI in agriculture few reviews have systematically synthesized its role across
the key domains of horticulture [ 35–38]. In the present review, we classify and discuss
four major areas where AI has made significant contributions: (i) pest and disease man -
agement, (ii) prediction of crop yield and quality, (iii) post-harvest handling and (iv)
retail marketing. Within each domain, we highlight not only the technologies employed
including machine learning (ML), deep learning (DL) and IoT-based tools such as sen -
sors, drones and robots but also the practical impacts these applications have had on
sustainability, productivity and resource efficiency. Furthermore, this review iden -
tifies critical limitations such as data scarcity, lack of generalizable models and adop -
tion barriers and discusses how these challenges can be addressed through emerging
AI innovations. To the best of our knowledge, this is the first comprehensive review
that systematically integrates AI technologies with their applications and outcomes in
horticultural production, while also providing a forward-looking perspective on their
potential to address climate change, reduce post-harvest losses and support sustainable
horticultural development.
Fig. 1 Flowchart of AI applications for achieving the sustainable production of horticultural crops

Page 4 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
2 Methodology
2.1 Research framework and thematic questions
This study employed a systematic literature review (SLR) to evaluate the current state
of research on AI applications in sustainable horticultural production. The review was
guided by three thematic questions:
TQ1 What is AI and how can it be applied to sustainable horticultural production?
TQ2 What tools and software are available for sustainable horticultural production?
TQ3 What are the challenges, solutions and future prospects regarding AI tools for sus-
tainable horticultural production?
The SLR approach was selected for its transparency, reproducibility and methodological
rigor for providing a structured synthesis of existing knowledge and minimizing bias [39,
40]. This framework facilitates the development of a conceptual model linking AI tech -
nologies to sustainable horticultural practices.
2.2 Data collection
The data process was systematic structured and collected from ScienceDirect, Scopus,
and Google Scholar, with preference given to peer-reviewed publications to maintain
quality and reduce bias [ 41]. The search strategy was designed using the following key
terms: “AI in horticulture production” “Artificial intelligence and sustainable horticulture
production” “Machine learning in horticulture” “Deep learning in horticulture” . Keyword
selection was validated by a focus group of five domain experts and further cross-veri -
fied against terms from an initial set of literature [ 42]. The inclusion criteria comprised
English-language articles published between 2005 and 2025 focusing on AI applications
in horticultural sustainability, while the exclusion criteria included non-peer-reviewed
sources, editorials and conference abstracts lacking empirical or theoretical rigor.
2.3 Data pre-processing
To ensure high-quality several pre-processing steps were implemented to find out the
best research paper for artificial intelligence application in horticulture. Duplicate and
retracted article were removed. Moreover, the highly cited articles, research reports,
magazines, Govt reports showed clear objectives for AI application in horticulture used
for writing the review.
2.4 Parameter settings and AI analysis
To enhance replicability and methodological transparency, AI model details were docu -
mented wherever reported. This included the type of algorithms employed such as ANN,
CNN, RNN, SVM, Random Forest and other machine/deep learning models.
2.5 PRISMA-based study selection
The study selection process followed the PRISMA 2020 guidelines. The initial database
search yielded 369 records. Titles and abstracts were screened to remove irrelevant or low-
quality studies. Full-text evaluation resulted in 303 articles meeting all inclusion criteria,
which were subsequently retained for qualitative and bibliometric analyses. The PRISMA

Page 5 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
flow diagram illustrating this process was generated using the Shiny App ( h t t p s :  / / w w w  . e s h a c
k a t h  o n . o r  g / s o f  t w a r e /  P R I S  M A 2 0 2 0 . h t m l) and is presented in Fig. 1.
3 AI based machine and deep tools where AI algorithms used for sustainable
horticultural production
AI addresses agricultural problems through the application of innovative techniques
like ANNs, WSNs, robots, DL, image processing and the IoT (Fig.  2). Large-scale fields
like DL and machine learning, which is a crucial part of AI [ 43, 44]. ML is the capacity
to learn without explicit programming, whereas DL is the study of learning deep neu -
ral networks (DNNs) and AI is the study of building intelligent machines and programs
[45]. In supervised learning for nonlinear regression, time series forecasting and data
categorization, traditional ML methods such as SVM, RF, PLS, ELR, and GP are cru -
cial. Accurate inferences necessitate thorough feature engineering and rigorous testing
[46]. The ML paradigm includes DNNs, sometimes referred to as DL. These networks
fall into three categories: recurrent neural networks (RNNs), convolutional neural net -
works (CNNs) and ANNs. RNNs are a type of ANN that uses internal loops to preserve
a kind of memory in order to handle sequential data. This makes them useful for applica-
tions like speech recognition, natural language processing and time-series forecasting as
it enables them to record temporal relationships and trends over time.
Fig. 2 Systematic Review Framework based on PRISMA Protocol.
Source: h t t p s :  / / w w w  . e s h a c  k a t h  o n . o r  g / s o f  t w a r e /  P R I S  M A 2 0 2 0 . h t m l

Page 6 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
CNNs are DL models specifically designed to interpret grid-like data, such photo -
graphs. They can effectively complete tasks like object identification, picture classifica -
tion, and visual pattern recognition by automatically and hierarchically extracting spatial
data using convolutional layers. With CNNs optimizing complex models, RNNs learn -
ing patterns using sequential data and ANNs learning weights and biases from ground
truth data, these networks are frequently utilized in agricultural applications [ 46]. Mak-
ing problem solving simple is the primary goal of AI and this may involve using ANN
[47, 48] Automating tasks and solving problems are made easier by new concepts with
techniques like ANNs, vision and natural language processing and ML. Among all of
them, ML and ANNs are the most frequently used techniques in agricultural automa -
tion research [49] and both labeled and unlabeled data can be used with ML algorithms
(unsupervised learning and supervised learning). Supervised learning techniques are
used in the majority of data-driven automation and related processes. ANNs, which
excel at difficult classification tasks, are a major component of today's agricultural auto -
mation systems.
The ANNs is a task-based technique that uses an internal task to direct the system
to operate as opposed to a conventional computationally programmed task. The three
layers that form an ANN are the input layer, the hidden (middle) layer and the output
layer. The architecture of ANN is layer-by-layer and is modeled after biological neurons.
They can understand intricate nonlinear interactions because to the architecture. Fur -
thermore, according to Shah et al. [ 48] and Mikhailov et al. [ 50], ANNs are processing
algorithms or hardware designed to function similarly to how the human brain is orga -
nized and functions. Neural networks exhibit exceptional capacities for adaptive learn -
ing and self-organization. The process of learning is experienced by ANN. The process
of learning involves adjusting to oneself when and when the environment changes. The
two methods of learning are unsupervised learning and supervised learning. Jha et al.
[49] worked the connections between AI technologies and different embedded systems
that are relevant to the agricultural area are enclosed. A summary of the several applica -
tions of ML and neural networks in agriculture is provided by Yang et al. [ 51]. More-
over, the process of addressing problems is made easier by the numerous new logics
and techniques that AI has stimulated. The idea of how the human brain functions was
taken into consideration when the ANN method was developed among other logics and
techniques. This method uses a variety of algorithms depending on the application to
train this particular model such as the Dynamic Adaption algorithm, Quickprop, Rprop,
delta-bar-delta, Silva and Almeida's approach.
In agriculture as well as horticulture, AI algorithm performance is task based on data
dependent. CNNs are effective for image-based tasks like disease detection and yield
estimation but require large datasets and high computing power. Tree-based models
(e.g., random forests, XGBoost) are well-suited for structured data tasks such as soil
analysis and yield prediction due to their robustness, interpretability and lower data
demands. SVMs work well with small datasets but scale poorly, while reinforcement
learning is emerging in controlled environments like greenhouses but remains limited
by complexity and data inefficiency [ 15, 52]. Each sensing modality has trade-offs: cam -
eras are cheap and informative but weather-sensitive; LiDAR provides accurate 3D map-
ping but is costly and weather-limited; radar is robust but low-resolution; IMUs are fast
and compact but drift over time. Multimodal sensing enhances reliability but increases

Page 7 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
system complexity [ 53]. Deployment challenges include high computational demands,
limited data availability, poor generalization to field conditions and the need for explain-
ability. Real world adoption is also hindered by hardware costs, regulatory constraints
and the need for user training and maintenance [54].
Preprocessing, variety, augmentation and big datasets are essential for DL. Kamilaris
and Prenafeta-Boldú [ 55] state that DL in horticulture and agriculture as a whole has a
bright future. CNNs serve as the foundation for most of the computer vision methods
based on DL that are widely used in agricultural automation. DL is main components
of AI that is used like as autonomous driving [ 56], 3D point cloud processing [ 57] and
human disease detection [ 58, 59] has led to several researchers incorporating various
network models into a speech-augmented language model SALM [ 60] with numerous
noteworthy outcomes [ 57]. Moreover, several DL tools are frequently employed for the
classification of images such as AlexNet [ 61, 62] VGGNet [ 63], GoogLeNet [ 64], Incep-
tionNet [ 65], ResNet50 [ 66, 67] DenseNet [ 68], XceptionNet [ 69], EfficientNet [ 70]
and NASNet [ 71], CIFAR-10 dataset [ 72], U-Net [ 73], Mask R-CNN, and YOLO [ 74],
YOLOv5 and AlexNet [ 75], NIR and RGB images [ 76]. Additionally fast R-CNN [ 77],
faster R-CNN [78], mask R-CNN [ 79], and region-based convolutional neural networks
(R-CNNs) are employed as DL techniques for a variety of applications. The scientific
community's interest in ANNs has been revived by CNN's remarkable advancements
and outstanding performance in tasks associated with the detection, classification, seg -
mentation and retrieval of images [ 80, 81]. CNN's capacity for learning is ascribed to
its utilization of layers and convolution procedures in various feature extraction phases.
Convolutional, pooling and fully linked layers are some of these phases. Kernels, which
carry out element-wise multiplication and sum to a single pixel are used in convolutional
procedures to extract features from images. Tanh, Singmoid and ReLU activation units
are among the units to which the output is allocated. In particular for huge photos pool -
ing operations minimize parameters. The largest element is identified by max pooling,
while the average of each patch is identified via average pooling. A fully connected neu -
ral network is built and outputs are classified using activation functions such as sigmoid
or softmax. Some of the important applications where AI algorithms used for sustain -
able horticultural production are discussed below.
3.1 Internet of things
It describes a network of physically linked devices that are integrated with sensors, soft -
ware and other technologies that allow data to be collected, sent and exchanged with
other devices and systems over the Internet. Across several domains, this connection
enables intelligent decision making, automation and real time monitoring. According
to Matta and Pant [ 82] a network of physical items is called the IoT or "things," having
network connectivity and the capacity to exchange information, collect data and engage
with their environment. Real time unstructured data is generated by IoT devices, which
first use AI algorithms for basic warnings. Big data necessitates data analysis as IoT sys -
tems get more intricate. AI systems are capable of processing and extracting valuable
information which results in superior decision-making. Sreekantha and Kavya [ 83] add
that IoT technology can also collect information on temperature, moisture, weather
and soil fertility in agriculture, enabling online crop monitoring and weed detection.

Page 8 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
Additionally, it makes use of WSNs, microcontrollers and cell-phones to allow farmers
to monitor conditions and boost productivity from a distance.
The IoT can dramatically cut down on the amount of time required when combined
with an effective clever decision-making mechanism that requires human interven -
tion for a range of agricultural tasks. The system's brain responsible for making intel -
ligent decisions that determines whether automated tasks succeed or fail. AI and the IoT
together create robust systems that are even more accurate than human decision-mak -
ing. Systems that can carry out operations such as speech recognition, visual perception,
decision-making and language translations tasks that frequently call for human intelli -
gence are known as AI-enabled systems [ 84]. The IoT and AI are viewed as complimen -
tary features of the automation of agricultural tasks.
There are several researchers [15, 85] who have emphasized the role of the IoT in agri-
culture, including horticultural crops.. Moreover, DL and ML with several algorithms
can all be applied as kinds of automation. Reducing human intervention and effort is
the goal of using any of these extended strategies [ 49]. Each of these techniques pos -
sesses pros and cons of its own. However, how they are applied sets them apart from
one another. The importance of DL on modern approaches and ML is highlighted by
Kamilaris and Prenafeta-Boldú's [ 55] exploration of DL in agriculture. Fruit counting,
agricultural yield projection and plant identification are the primary goals.
3.2 AI-based robotics
Robots, sensors and drones are being used in horticulture to carry out AI tasks such as
watering, weeding, spraying and harvesting [ 24, 35, 86, 87]. AI-based methods and tools
have been very effective in horticultural crop management (Table  1). Moreover, agro-
based industries have benefited greatly from the most recent developments in auto -
mated systems, which include agricultural robots and drones. Modern computer-based
systems are made to measure a wide range of crucial factors including crop quality, yield
detection, weed identification and many other methods [17, 18, 88]. Three key technolo-
gies, DL, ML and AI are terms used in the robotics industry [ 89–91]. Advanced robotics
is transforming with AI, ML and DL enabling intelligent machines to perform complex
tasks with precision and efficiency. These technologies automate agriculture chores like
planting, harvesting, spraying and optimize farming activities like weather prediction
and crop health monitoring [ 90–92]. Robots can now perceive and interact with their
surroundings, make decisions and finish difficult jobs all because of AI [ 93]. Robots can
learn from data and get better over time thanks to a branch of AI known as "ML" [ 94].
DL has shown to be very beneficial in robotics for applications like as object detection,
speech and image identification and natural language processing. ANNs are also used
in DL through ML, which allows computers to learn from massive volumes of data [95].
Moreover, automated, unmanned and intelligent robots are possible [ 35, 96]. Robotic
arms (hands), ground robots and aerial robots (drones) are extensively employed in
manufacturing and transportation [ 97, 98]. They are currently widely used for a variety
of tasks in horticultural production including growth monitoring [ 99], environmental
information gathering [ 100, 101], weed control [ 102], spraying [ 103, 104], pollination
[105, 106] and additional horticulture producing activities. They may also take the place
of more established farming equipment like combine harvesters and regular tractors.
Global Positioning System (GPS) [107], BeiDou Navigation Satellite System (BDS) [108],

Page 9 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
machine vision [ 109, 110], electromagnetism, ultrasonic sensors [ 111] and other tech -
nologies for automatic navigation are frequently the basis for these robots operations.
In addition, Hutsol et al. [ 112] identified a number of robots used for different tasks in
horticulture production such as high-resolution stereo cameras, 3D lidar, LiDAR, light
meters, RGB and IR cameras, lasers, rangefinders, IMUs, LiDAR, IR thermometers and
RGB cameras.
3.3 AI based unmanned aerial vehicles
UAVs or drone technology has quickly developed into a disruptive force in a number of
industries, delivering creative solutions and upending conventional wisdom [113]. Moreover,
drones are remotely controlled, unmanned aircraft that may carry out a variety of activities
and gather useful data since they are outfitted with cameras, sensors and other payloads.
Drones are now essential instruments in agriculture especially in the management of fruit
as well as vegetable crops [114–118]. Remote sensing technologies for identifying and man-
aging plants, weeds, pests and illnesses are now possible thanks to developments in com-
puter vision, mechatronics, AI and ML. Additionally, it offers a once-in-a-lifetime chance
to develop accurate fertilization techniques through sophisticated seeding procedures. AI
technologies have the potential to help farmers save waste while improving product quality
and guaranteeing faster market access. Automated tractors are clearing the property in order
to plant and harvest crops and also these tractors might run on their own thanks to GPS
Table 1 AI-based robots, drones, and sensors for sustainable horticultural production
Application Name of Drone/Sensor/robot Description References
Powerful tool for
studying phenom-
ics and genomics
remote sensing platforms
(UAV-RSPs)
Genome to determine the association
of genomic and phenotypic informa-
tion to increase the crop yield
[114]
Pest and disease
detection
RobHortic Field Robot Uses multispectral and hyperspec-
tral cameras for detecting pests and
diseases in carrot crops, particularly
focusing
[88]
Remote disease
detection
Smart drone with LiDAR For sustainable forest planning and
management, remote sensing (RS) plat-
forms are rapidly going mainstream
[116]
Improve the
efficacy of both bio-
control agents and
synthetic pesticides
Remote sensing using drones Drones release beneficial insects for
pest control in orchards, improving
consistency in application of biological
control agents
[124]
Fertilizer, pesticide
and growth regula-
tors application
Drone Agras T20 UAV A multi-rotor drone with sensors for
precision pesticide spraying and fertil-
izer distribution. Applied for targeted
pest
[132]
Application of plant
protection UAVs in
crop pest, disease,
and weed control
UAVs. And MPAPR R-CNN, canopy remote sensing and identifica-
tion; strategies for improving the spray
quality of UAV applications; and spray
drift assessment
[117]
Prevention of dam-
ages through early
diagnosis of various
stress types
Drones equipped with high-
resolution cameras
UAV, with their agility and versatility
play a crucial role in monitoring and
spraying operation in vegetable crops
[118]
Detection of
diseases
CNN integrated within an IoT
based UGV
An intelligent automated system for
real-time detection and classification of
tomato diseases using a CNN integrated
within an IoT based unmanned ground
vehicle (UGV)
[151]

Page 10 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
technology. In addition, drones collect information, use remote sensing to assess the health
of farm produces and crops [119–121].
4 Current applications of AI in horticultural production
Figure3 illustrates the usage of AI applications in horticultural production including
postharvest management and retail marketing.
4.1 AI based diseases and insect management
The detection of diseases and insects can be a labor-intensive process particularly when
relying on conventional laboratory techniques [ 122]. These traditional methods fre -
quently present challenges including significant costs and prolonged timeframes [ 122].
In order to overcome these obstacles and improve agricultural disease diagnosis's pre -
cision and effectiveness, the adoption of advanced technological solutions has become
imperative [ 123]. Consequently, AI methodologies have recently been recognized as
effective solutions for disease and insect detection [ 124–126]. A few important uses of
AI network for managing insects and illnesses are shown in Table  2. Moreover, the effi-
cacy of pest and disease prediction is contingent upon the acquisition and manipula -
tion of copious amounts of pertinent data as noted by [ 127, 128]. To predict pests and
diseases occurrence in crop, gather weather and soil data, choose ML algorithms based
on accuracy, efficiency, interpretability and data characteristics which ensuring optimal
performance in real-world scenarios (Fig. 4).
As stated by Deng et al. [ 129] ML provides strong capabilities for analyzing and inter -
preting a variety of data, including pictures, sensor readings and environmental data in
order to detect and efficiently manage pest infestations. According to Chithambarathanu
and Jeyakumar [130] farming frequently uses ML tools like Decision Tree (DT), Support
Vector Machine (SVM), Naive Bayes (NB) and Random Forest (RF) as well as DL tech -
niques like CNN, DCNN, Long Short-Term Memory (LSTM) and Deep Belief Network
(DBN) for crop protection and pest detection. Images of crops may be recognized and
classified by machine learning algorithms which can also detect indications of pest dam -
age or the presence of pests [ 131] and farm fields can be photographed by devices such
as drones equipped with high resolution cameras. These photos may then be analyzed
Fig. 3 AI-based smart technologies for sustainable horticultural production

Page 11 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
by ML systems to find abnormalities that could be signs of insect infestations. A key fac -
tor in reducing horticultural crop losses from pests and diseases is the deployment of
robotic ML and AI systems [37]. The revolutionary influence of AI and ML technologies
in pest and disease prediction and detection is highlighted by [ 27, 132]. The research
reveals that the effectiveness of ML algorithms like CNNs and support vector machines
varies across different crop varieties and farming scales, emphasizing the need for cus -
tomizing AI solutions for diverse agricultural contexts. Hruday et al. [133] demonstrated
the use of AI and robotics in horticultural pest and disease control.
They used machine learning algorithms, OpenCV-enabled image processing tech -
niques and Raspberry Pi as a central orchestrator to identify plant diseases. The system
also utilized high-capacity water pumps for targeted pesticide administration, reducing
environmental impact. The integration of advanced navigation systems and ultrasonic
sensors ensured smooth agricultural operations. The precise application of treatment to
damaged areas is made possible by AI algorithms that assess the data gathered by the
Table 2 Artificial intelligence-based applications in disease and pest management in horticultural
crops
Crop Application Disease/Pest References
Cereal crops,
Tomato, Cucur-
bitaceae Crops
BNI Frusarium Head Blight (Fusarium graminearum), Root
rot, Fruit rot
[154]
Apple RF Apple leaf diseases- Mosaic (Papaya ringspot virus)
Brown spot (Marssonina coronaria), Rust (Pucciniaceae
glue rust), Alternaria leaf spot (Alternaria alternata f.
sp mali)
[155]
Cereal Crops
and Vegetable
Crops
AvrLm4-7, Pep1, MC69 Rust, Powdery mildew [156]
CNN Blast [157]
Banana DTL System Bunchy top disease, Black sigatoka, Yellow sigatoka,
Xanthomonas wilt
[145]
Banana DCNN Corm weevil [145]
Carrot, Grape GNSS (Global Naviga-
tion Satellite System)
Citrus stubborn disease (Spiroplasma citri) Flower
malformation (Candidatus phytoplasma)
[88]
Citrus DNNM (Deep neural
network model
Fruit and Leaves Diseases [158]
Tomato CCMT Leaf blight, Leaf curl, Septoria leaf spot, Verticillium wilt [159]
Cashew CCMT Anthracnose, Leaf miner, Red rust [159]
Cassava CCMT Bacterial blight, Brown spot, Green mite, Mosaic [159]
Cashew CCMT Armyworm [159]
Cassava CCMT Grasshopper [159]
Tomato CCMT Leaf beetle [159]
Tomato,
Chilli, Potato,
Cucumber
IoT, CNN, ANN, KNN Down curl, Gemini virus, Cercospora, Leaf spot [125]
Date Palm DFR model (Decision
forest regression)
Date palm mite infestation [27, 160]
Tomato Python-based REST
API, PostgreSQL, and
Keycloak
Tuta absoluta (Meyrick) [126]
Tomato CNN integrated within
an IoT based UGV
Late Blight, Early Blight, Septoria Leaf Spot, Tomato Yel-
low Leaf Curl Virus, Bacterial Spot, Target Spot, Tomato
Mosaic Virus, Leaf Mold, Spider Mites Two-Spotted
Spider Mite, Powdery Mildew
[151]
– GeoAgriGuard: AI-
Driven system
– [153]

Page 12 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
robotic devices. These robotic sprayers with AI efficiently manage pests and illnesses,
minimize chemical usage and improve dosage by employing real-time data [ 134]. Fur-
thermore, AI systems combine information on pests and diseases with other variables
such as meteorological conditions and markers of plant health, to enable proactive deci -
sion making. In addition, ML and AI-powered picture recognition models correctly
identify pests and diseases based on visible signs. By assisting with accurate diagno -
sis and suggesting appropriate therapies, these systems stop the spread of disease. AI
systems also offer the benefit of data driven decision making for managing diseases
and pests. Large amounts of data are processed by AI algorithms, including historical
records of pest and disease activity meteorological trends and crop health data. AI sys -
tems use this data to create prediction models that foretell outbreaks, enabling farmers
to take preventative action [ 134]. By independently checking crops for pests and ill -
nesses, robotic devices also help to lower agricultural losses. Horticulturists can opti -
mize pest and disease management leading to lower crop losses, higher yields, and more
effective use of resources by implementing robotic and AI systems [ 37, 134]. DL tech -
nologies such as CNNs and DBNs have been proposed for plant anomaly and pest detec-
tion. These methods have shown promising results in the identification and detection of
lesions from digital photographs [ 135, 136]. According to Lin et al. [ 137] and Stančić et
al. [138] CNNs are a particular kind of deep learning model that works well for image
classification tasks such as identifying leaf diseases. CNNs and DBNs are two recent
DL techniques for plant disease diagnosis [ 139]. By teaching a network to identify the
underlying features of the images, these methods enable the detection of subtle symp -
toms of diseases that traditional image processing methods would overlook [ 140, 141].
Ullah et al. [ 142] claimed that because DL models can handle large and complex pic -
tures, they are suitable for high resolution photographs.
AI and machine vision have been combined to create an automated system that can
identify and locate the citrus psyllid ( Diaphornia citri ) in citrus orchards [ 143]. Zhang
and Ren [ 144] constructed a federated continual learning comprehensive model based
on the Swin Transformer model (SSPW224-LwF-3) attaining good accuracy, precision,
Fig. 4 AI-based different applications for achieving the sustainable production of horticultural crops

Page 13 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
recall and F1 scores. The model has an average accuracy of 47.06% over 18 methods, out-
performing previous network models in the identification and classification of plant leaf
diseases. Additionally, a detection model utilizing AI and DL systems enables even indi -
viduals with limited knowledge of banana pest and disease symptoms to identify several
issues affecting banana crops [145]. Moreover, a comparable system was created to facili-
tate the diagnosis and treatment of banana diseases, providing valuable insights into dis -
ease management [146]. In a similar way, an expert system based on knowledge has been
developed to identify and treat a range of diseases that impact pineapples [ 147]. It was
possible to identify the most common postharvest illness in Golden Delicious apples by
employing electronic nose (E-Nose) technology in the packaging and processing phases
[148]. Furthermore, an automated system has been developed to identify diseases across
multiple crops, using picture segmentation techniques such as banana, mango, jackfruit,
lemon and beans [140].
Additionally Maniyath et al. [ 122] implemented various ML models to distinguish
between papaya leaf diseases and health, with the random forest (RF) model demon -
strating superior performance, achieving an accuracy of 70.14%, while in grape support
vector machine (SVM) classification, resulting in an impressive disease accuracy at the
rate of 98.71% [ 149]. In addition Rani, [ 150] developed a MobileNetV2 model for clas -
sifying citrus diseases which has an accuracy of above 97%. Recently for identification
and classification of plant leaf diseases [ 144] constructed a federated continual learning
comprehensive model based on the Swin Transformer model (SSPW224-LwF-3), attain-
ing good accuracy, precision, recall, and F1 scores. The model has an average accuracy
of 47.06% over 18 methods. In one study, Farooq et al. [151] used a CNN integrated with
an IoT based autonomous ground vehicle. Following training on over 20,000 images of
tomato leaves, the system achieved an accuracy of 83%. In recent study, citrus farms
worldwide suffer from a bacterial disease known as huanglongbing, which is caused by
the E3 ubiquitin ligase PUB21 breaking down the immunological protein MYC2. Zhao
et al. [152] used AI methods to find microbial peptides that inhibit proteolysis and then
found a single small peptide that stabilizes MYC2 and reduces disease symptoms.
In a recent study, Sharda et al. [153] developed the GeoAgriGuard AI-Driven Pest and
Disease Management System, which uses state-of-the-art AI models and remote sens -
ing technologies to combat pest and disease outbreaks in agriculture. The system uses a
hybrid deep learning ensemble, multi-spectral and hyper-spectral data, and vegetation
indicators to predict and classify pest and disease outbreaks. An automated method for
the real-time identification and classification of tomato diseases was developed by.
In molecular based plant protection AI and ML are increasingly applied in horticul -
tural pest and disease management. For example, Bayesian network inference has been
used to reconstruct the global gene regulatory network of Fusarium graminearum
[154] and deep convolutional neural networks have enabled accurate identification
of apple leaf diseases [ 155]. Tools such as ApoplastP for effector prediction [ 156] and
DeepT3 for bacterial type III secreted effectors [ 157] highlight the role of AI in molecu -
lar plant pathology. In horticultural production, AI-based models have been developed
for automatic detection of citrus diseases [ 158] crop pest and disease datasets such as
CCMT [159] and prediction of date palm mite infestations [ 160]. These studies collec -
tively demonstrate the growing potential of AI-driven approaches in disease and insect
management.

Page 14 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
Insect control has benefited greatly from the use of deep learning techniques and AI-
based technologies [161]. These days pixel-wise labeling of insects or damage symptoms
is made possible by the widespread use of deep learning-based segmentation techniques
using CNNs such as U-Net [ 162], DeepLab [ 163], or Mask R-CNN [ 164, 165]. These
models are perfect for large-scale entomological applications since they can generalize
effectively across different field circumstances and backdrops. To classify insects across
three taxonomic levels, Ong et al. [ 166] evaluated the performance of four deep-learn -
ing models including InceptionV3, VGG19, MobileNetV2, and Xception. Among these
InceptionV3 demonstrated superior accuracy particularly in distinguishing insect orders
and families giving it a clear advantage over the other models. Valan et al. [ 167] used
VGG19 to classify four insect datasets (Diptera, Coleoptera, and Plecoptera) with an
accuracy of at least 90%. Using the deep learning algorithms VGG16 and InceptionV3
Ozdemir et al. [ 168] created mobile applications for the categorization of insect orders
achieving an average accuracy of at least 80%. Using a random forest approach with a
selection operator Lytle et al. [ 169] were able to accurately classify 89.5% of stonefly
photos that belonged to nine species and seven families. Another potential approach to
automated taxonomic classification is to use other supervised machine learning models
such as deep recurrent neural networks (DRNN) which can self-learn the misclassified
group and eventually improve by retrieving a previous output (prediction result) as a
new input for the current step [ 170]. To extract the higher-level characteristics from the
raw input data DL uses multi-layered neural networks. DL has demonstrated remarkable
success in a number of natural language processing applications such as image identifi -
cation and pest monitoring and detection in urban and agricultural settings [ 171]. Using
deep learning algorithms, AgShift's "DeepAgro" software analyzes crop photos to detect
insect infestations, disease infections, and other problems [ 172]. To classify and identify
the pest, CNN uses an AI-driven system called YOLOv3. CNN automatically counts the
amount of insects on the plants using image processing algorithms.
To strengthen post-border surveillance efforts, Christakaki et al. [126] recently recom-
mended AI-based image analysis for monitoring invasive alien species, newly emerg -
ing pests, native pests, and quarantine-listed organisms. Using PostgreSQL, Keycloak,
and a Python-based REST API, a mobile application was created. Field testing was
done to show the app's efficacy in real world agricultural scenarios like identifying Tuta
absoluta (Meyrick) infestations in tomato crops. The study's findings demonstrated that
T. absoluta may be found with a 70.2% (mAP50) accuracy using sophisticated DL mod -
els. Boissard et al. [ 173] automated the quick identification of whiteflies on rose leaves
by using knowledge-based systems and image processing. Moreover IoT-enabled bug
traps with cameras and sensors are used in the "Trapview" system created by EFOS
Ltd. In order to enable prompt action AI algorithms evaluate the gathered data to track
insect populations in vineyards and orchards [ 174]. The University of Georgia's "PestID"
software utilizes ML to recognize insect pests from photos taken with a smartphone's
camera [ 175]. The 36 species of bumblebees were recognized using ML methods by
Spiesman et al., [ 176]. The Lepidopteran insects were identified with 75% accuracy by
using the Angel invariant Gabor algorithm [ 177]. Now, there are several apps that have
been developed by several people for pest management in crops, including Plant Vil -
lage [178], PestNet [179], PestID [175], IPM Toolkit [180], FieldScout GreenIndex [181],
FieldX scout [182], Agrian Mobile [183] and Crop Scouting by Encirca [184].

Page 15 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
4.2 AI based crop quality and yield prediction
The evaluation of the quality of horticultural products is essential for ensuring adher -
ence to market standards, which in turn affects their marketability and pricing. Con -
sequently, precise quality categorization is crucial for improving pricing strategies,
minimizing postharvest losses and waste, and bringing products into line with market
expectations [17, 185]. A number of important applications of AI for horticulture crop
quality and yield prediction are listed in Table 3. According to Jabed and Murad [186] RF,
ANN, and SVM are the most widely used machine learning methods for crop prediction.
CNN, Long-Short Term Memory (LSTM), and DNN are frequently used in the field of
deep learning to forecast yield [186, 187]. Hani et al. [188] proposed deep learning-based
fruit detection and counting approach for predicting apple output. Their comparison
of semi-supervised approaches with deep learning techniques revealed that Gauss -
ian mixture models generally performed better than CNN, Fast R-CNN, and U-NET
across most datasets for yield estimation. Among deep learning models, DNN, LSTM
and CNN remain the most commonly employed for predicting agricultural production.
LSTM, a specialized type of recurrent neural network (RNN), is especially effective for
capturing and processing time-dependent data [ 189]. In a study by Zulkifli et al. [ 190], a
predictive model for determining papaya ripening stages was developed by integrating
an SVM model, discriminant analysis, and a machine vision system. Among the tested
approaches, linear discriminant analysis delivered the best performance, achieving an
accuracy of 83.5%.
In another study, Sengupta and Lee [191] used support vector machines (SVM) to esti-
mate the number of immature green citrus fruits in a tree canopy, attaining an accuracy
of 80.4% for fruit detection and counting. Additionally, Abbas et al. [ 192] developed a
model utilizing support vector regression (SVR), k-nearest neighbors (KNN), elastic net
(EN), and linear regression (LR) to predict potato yield in Canada's Atlantic Region. The
study's conclusions are crucial for developing management strategies tailored to individ-
ual fields for the potato farmers in the region. Another noteworthy method of yield pre -
diction created by Northwest Nazarene University Robotics Vision Lab entails counting
blossoms to estimate fruit yield [193]. During the flowering phase, photosynthetic activ -
ity tends to rose, which has a positive relationship to the fruiting process. Consequently,
the correlation between the number of fruits and the number of flowers can be used to
estimate the fruit output on the tree and the identified blossoms in an image. This early
yield prediction system has been effectively implemented in Pink Lady Apple cultivars
[194]. In addition, AI-based approaches have also been employed for crop growth and
yield prediction. For instance, machine learning models have been applied to predict
tomato growth in hydroponic systems [195]. Similarly, in intelligent greenhouse systems,
sensors integrated with AI have been utilized to optimize climate control, irrigation, and
management strategies thereby enhancing cherry tomato yield and quality [196].
Table 3 Artificial intelligence-based technologies for horticultural crops' quality and yield
Model Crop References
KASPRO and INTKAM Cherry tomato [196]
Bi-LSTM Tomato [195]
DNN, SVM, ANN Potato [231]
Support vector machines (SVM), random forest (RF),
and k-nearest neighbors (KNN) classifiers
Tomato [216]
YOLOv8n Strawberries [206]

Page 16 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
4.3 AI for harvesting, postharvest handling, processing and losses of horticultural crops
An AI driven solution designed to facilitate harvesting significantly reduces the labor
costs associated with the process while ensuring that produce is harvested at the optimal
time. Early assessments of crop maturity along with predictions regarding harvest dates
and yields can now be accomplished through various nondestructive methods includ -
ing hyperspectral imaging [ 197], multispectral imaging [ 198] and near-infrared spec -
troscopy [199]. The field of robotic fruit harvesting has attracted considerable interest
in recent years particularly in studies focused on citrus [ 200], apples [201], and bananas
[202]. An improved one stage RGB image detection network based on YOLO-V3 was
used by Kang et al. [ 203, 204] to conduct object detection in apple orchards. Recently,
Yan et al. [ 205] developed APYOLO, an improved apple recognition algorithm that
increases operational speed and detection accuracy. Its multi scale channel attention
mechanism and better prior distribution intersection over union loss function outper -
form the original YOLOv11 by 2.2%, 2.1%, 0.8% and 2.3% respectively. Liu et al. [ 206]
predict strawberry output for the upcoming week using real-time plant photo data and
environmental data. They used YOLOv8n to count blooms, immature fruit and ripe fruit
per plant and trained several AI models for production prediction. The approach out -
performed traditional machine learning methods.
In order to identify fruit in intricate orchard environments, researchers have been
experimenting with multi-modality sensors and multi images. A DL method for grape
harvesting based on color estimate was created by Amemiya et al. [ 74]. They employed
an autoencoder based anomaly detection model for diseased grains and YOLOv5, an
object detection model for bunch and grain detection. In a practical experiment with
real grapes, they suggested a multitask learning model that used AlexNet and metric
learning to obtain an accuracy of 72.1% in color estimation and an accuracy of 81.6%
in detecting whether grapes were suitable for harvesting. For multi class segmentation
in terms of precision and recall YOLOv8 fared better than Mask R-CNN with infer -
ence times of 10.9  ms and 7.8  ms respectively [ 207]. As a result, it can be concluded
that YOLOv8 is more precise and effective in ML applications especially for real time
applications like robotically picking and cutting young green fruit. ML approaches were
employed by Ma et al. [ 207] to improve the identification of chilies in natural environ -
ments. They replaced the YOLOv8n baseline with an upgraded version of the HGNetV2
model, added SEAM to the detection head, improved feature fusion and replaced the
traditional up-sample operator with CARAFE. With the modified model decreasing
parameter count and GFLOPs by 29.5% and 28.4%, respectively, chili target detection
rose by 96.47%, 96.3%, and 79.4%.
An innovative visual approach to evaluate fruit harvesters with mapping algorithm
were employed by Yin et al. [ 208] to construct a completely autonomous citrus harvest -
ing robot system. With an average picking time of 10.9 s per fruit, the system achieved
an overall success percentage of 87.2%. AYDY, an algorithm for identifying and organiz -
ing a sweet pepper picking sequence was created by Ning et al. [209]. To locate and iden-
tify sweet peppers, the method makes use of a clustering approach and a convolutional
block attention module. After dividing them into picking clusters, it employs profes -
sional judgment to choose an anti collision picking order. With a collision free harvest -
ing success rate of 90.04%, an average localization accuracy of 89.55%, and F1-score of
91.84% were attained by the method. A robotic fruit harvesting system with six degrees

Page 17 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
of freedom, an RGB-D camera, a computer and a storage container was created by Arad
et al. [ 210]. With average cycle duration of 24  s, the system was tested in a commer -
cial greenhouse. Increased robot speed enhanced system efficiency, harvest success rates
were 61% under ideal crop circumstances and 18% under current ones. Furthermore, uti-
lizing a single RGB image, Sun et al. [ 211] created a fruit harvest estimate algorithm. To
predict the rotation vector and determine the navel point, they suggested using a multi
task learning model known as FPENet. Hyper parameter was also incorporated into the
model for simultaneous convergence. The experiment revealed that FPENet had an aver-
age error of 11.13 and 88.92 AP score for fruit navel point detection. Images captured in
RGB and infrared by using Kinect v2 were merged to identify sweet pepper, resulting in
a 4.1% improvement in F1 score over using a single image identification algorithm [212].
Additionally, fruit ripening can be monitored using ANN providing information about
the precise physiological condition of the fruit [ 213]. To determine the ideal ripeness
levels, Dutta et al. [ 214] proposed the use of zero-shot models capable of transferring
knowledge from generalized AI prediction frameworks. This technology presents a prac-
tical, cost-effective and real-time solution for stakeholders in the fruit supply chain to
accurately predict ripeness levels. Additionally, Occhiuzzi et al. [ 215] created an RFID
based system to track the storage conditions of avocado fruits and determine when they
are ready to ripen. With an accuracy of over 85%, the system made use of tag reader
data that was SVM-processed to classify the fruits into the following categories: unripe,
stock, grocery and consumer. Furthermore, a recent investigation by Mputu et al. [ 216]
analyzed tomato quality through the application of k-nearest neighbors (KNN), RF and
support vector machines (SVM) classifiers. Notably, when CNN-SVM was employed as
a feature extractor in place of Inceptionv3, it surpassed other hybrid models 97.54% of
the tomatoes were correctly classified as ripe, unripe, old or damaged. Moreover, in one
study, Torkashvand et al. [217] used ANNs in the kiwi fruit to forecast the calcium (Ca)
and nitrogen (N) concentrations as well as their ratio at harvest in order to determine
the firmness of the fruit.
The traditional manual sorting methods are not only labor intensive and time consum-
ing but also subjective, prompting the integration of ML technologies to overcome these
limitations. Furthermore, Opara et al. [ 218] emphasize the significance of sorting fruits
and vegetables as their visual appeal is a major factor in how fresh produce is graded
influencing both quality and market value. Therefore, the integration of AI-driven ML
technology is necessary to improve productivity and efficiency in the grading and sort -
ing of fresh food. Recent studies highlight an increase ML use in postharvest manage -
ment and processing of horticultural products [ 24, 219]. Piedad et al. [ 220] presented
a model that uses tiers to classify bananas rather than evaluating each fruit separately.
Based on color and size characteristics, this study divided banana tiers into four separate
categories: reject class, class II, class I and extra class. Additionally, in order to distin -
guish between healthy and defective tomatoes, Ireri et al. [ 221] suggested a system for
machine vision that combined the RBF-SVM classifier with color pictures. This system
effectively categorized tomatoes into four groups by analyzing color, texture, shape and a
combination of these features.
Fruits, vegetables and flowers are especially vulnerable to postharvest losses because
of their high moisture content and short shelf life [ 24, 222]. Numerous factors contrib -
ute to the food value chain's postharvest losses as highlighted by [ 218, 223–225]. The

Page 18 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
effective use of ML for yield prediction [ 191, 226], disease identification [ 122, 149, 227]
and crop quality assessment [ 228] indicates that employing ML to measure and fore -
cast postharvest waste throughout the food value chain is essential for production plan -
ning and policy development. Additionally, AI has been employed in DL models like
ResNet50, Efficient NetB7 and NasNetLarge for the sorting and grading of banana fruits.
These models are trained on datasets of bananas in order to classify the fruits accord -
ing to their ripeness and quality [ 229, 230]. Singha and Swain [ 231] used mask R-CNN,
U-Net and DeepLab CNN models to identify and forecast postharvest degradation
zones in apple fruits that were kept. This approach was notable for its ability to indepen -
dently delineate and forecast areas of decay and non decay in the fruits. In addition, El
Akrouchi et al. [ 232] developed a system for accurate early stage citrus fruit detection,
segmentation and counting in orchard situations. The system uses two photographs:
close up images for training and full tree shots for testing and real-world applications.
MViTv2_L backbone outperformed alternatives with mean Average Precision (mAP) of
84.40% for masks and 72.97% for bounding boxes.
Additionally, apple harvesting varies seasonally and the current approach primarily
relies on manual labor [233]. Even while mechanical harvesting technologies can signifi -
cantly speed up the process, fruit quality is sometimes decreased owing to mechanical
damage during harvesting, packing and transportation [225, 234]. In this context, Han et
al. [235] developed the FDNet-p methodology for stem features and an improved DPC-
AWKNN segmentation method for apple body segmentation. They developed an intel -
ligent apple grading model using the GBDT algorithm. The findings showed outstanding
performance in stem detection and apple grading with a weighted Jaccard Score, Preci -
sion, Recall and F1 Score. Li et al. [ 233] developed a Box-Behnken-designed response
surface model for apple damage area and contact force to ascertain the optimal parame -
ters for small, medium and big apples. The model showed a damage rate of 12% for grade
I apples and 0% for grade II apples when compared to vibration harvesting.
Recent advances in hyperspectral and fluorescence imaging have provided powerful
tools for postharvest quality monitoring and loss reduction in horticultural crops. For
example, Vis–NIR hyperspectral imaging has been used for rapid detection and visual -
ization of early decay in citrus [236], while optical sensor-based approaches have enabled
early detection of fungal infections in stored apple fruit by comparing biospeckle, hyper -
spectral imaging and chlorophyll fluorescence techniques [ 237]. Hyperspectral meth -
ods have also been employed for quality sorting of hazelnuts [ 238], detection of codling
moth infestation in apples [ 239] and foreign substance detection on fresh-cut lettuce
[240]. Similarly, fluorescence hyperspectral imaging using violet LEDs has proven effec -
tive in identifying fecal contaminants on spinach leaves [ 241]. Beyond detection, these
technologies are increasingly applied to assess and maintain the quality of fresh fruits
and vegetables, thereby supporting the horticulture and agro-industrial sectors [242].
Overall, ML is essential for accurately assessing postharvest losses in horticulture
goods. This requires data from environmental parameters, storage methods, logistics
and physical quantification. Research combining ML with physical measurement data is
needed to fill the gap in measuring waste and physical postharvest loss, enabling better
policymaking and successful execution. Table 4 presents some significant applications of
AI to horticultural product harvesting and postharvest quality management.

Page 19 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
4.4 AI for cultivar classification and weed detection
AI technologies have proven to be highly effective in detecting crops, identifying cul -
tivars and weed detection (Table  5). In the classification of various crops, including
both herbaceous and woody types Pena et al. [ 243] applied C4.5 decision trees, logistic
regression (LR), SVM and MLP algorithms. Moreover, using seven supervised ML algo -
rithms Vazquez et al. [ 244] created a novel classification framework with seven discrete
form classes. Outperforming human classifiers with an accuracy of 88% the support vec -
tor machine model outperformed the other technologies. Among the AI methodolo -
gies, individual classifiers maximum classification accuracy of 88% was attained using
MLP and SVM. However, SVM performed better in hierarchical classification, increas -
ing accuracy to 89%. In their research, Yang et al. [ 245] classified apricots according
to their morphological traits using decision trees (DT), k-nearest neighbors (KNN),
Table 4 Artificial intelligence-based applications for harvesting and postharvest quality of
horticultural products
Imaging mode Application Refer-
encesSafety attribute Crop
Reflectance Fecal contamination Microbial
infection
Apple
Apple
Citrus
Spinach
[236,
237]
Insect infestation Apple
Jujube
Mango
Hazelnut
[238,
239]
Fluorescence Fecal contamination Apple
Cantaloupe
Lettuce
[240]
Quality detection technologies Shelf life Banana
Papaya
Mango
[242]
Multiscale Vision Transformers
version 2 (MViTv2) with Cascade
Mask R-CNN
Module is responsible early detec-
tion and segmentation of green
citrus fruits in orchards
Citrus fruits [232]
Table 5 Artificial intelligence- based applications for cultivar classification and weed detection in
horticultural crops
Models Cultivar
classification
Weed detection Refer-
ences
ANNs, NMR Apulian Olive – [248]
ANN with NIR Grapevine – [249]
Machine learning Apricot – [245]
VGG-16, Grad-CAM Litchi – [250]
Visual Transformers (ViT) – Weeds in beet, parsley, and
spinach crop
[261]
Machine learning, CNNs Apple – [251]
CNNs – Weed in tomato [266]
The Convolutional Neural Network (CNN) – Weeds in brinjal [264]
UAV, Vis, kNN, SVM, RF, XGBoost, Spectral bands
(Green, GRVI, GN, REN, CIRE), CHM, TCA
Almond – [247]
R-CNN Mango – [252]
Deep learning Tomato – [253]
YOLOv7, YOLOv8, and Faster-RCNN – Multiple weed (and crop) spe-
cies and/or multiple instances
of one species
[267]

Page 20 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
naive Bayes (NB), linear discriminant analysis (LDA), support vector machines (SVM),
and backpropagation neural networks (BPNN). LDA, quadratic discriminant analysis
(QDA), SVM, KNN, DT, and NB classified of pineapples into three distinct cultivars,
with SVM achieving a remarkable 100% accuracy compared to other models [ 246]. In a
more recent investigation, Guimarães et al. [247] successfully identified almond cultivars
using high-resolution multispectral data collected from an unmanned aerial vehicle. The
two most effective ML classifiers among the four utilized were SVM and RF with perfor -
mance further improved by the canopy height model, RF and XGBoost demonstrated
the highest accuracy. Moreover, artificial neural networks have been used to compare
NMR, NIR and mereological data for the classification of Apulian olive oils [ 248], while
machine learning approaches integrating leaf morpho-colorimetry, fractal dimension
and near-infrared spectroscopy parameters enabled automated grapevine cultivar classi-
fication [249]. More recently, deep learning techniques have been employed for cultivar
discrimination in litchi fruit [250], apple [251], mango [252] and tomato [253] highlight-
ing the growing role of AI in accurate cultivar identification and management.
AI instruments, such as the utilization of high-definition photographs obtained via
unmanned aerial vehicles, facilitate the effective recognition, identification and distinc -
tion of weeds from the primary crop [ 254–256]. Many authors have drawn attention to
this aspect through their diverse research projects utilizing a range of methodologies
and applying them to different vegetable crop types such as onion [ 257], strawberry
[258] and cabbage [ 259]. Pallottino et al. [ 260] for instance used a light drone to pre -
cisely measure the amount of weeds on baby-sized red lettuce grown beneath a plastic
multi tunnel greenhouse. These technologies have also been used in protected habitats.
Furthermore, to decrease the amount of the labeled dataset, Reedha et al. [ 261] devel-
oped the Visual Transformers (ViT) methodology showcasing the method's capability
for classifying weeds in beet, parsley and spinach fields. However, a novel semi-super -
vised technique was presented by Khan et al. [ 262], which uses an algorithm to create a
new training dataset for model training. With 80% of the training data remaining unla -
beled, this technique attained a 90% accuracy rate in classifying weeds in strawberry
and pea fields. Furthermore, Bah et al. [ 263] presented an entirely automatic learning
approach (unsupervised) for weed detection and in tests carried out in spinach fields,
this system produced results similar to supervised methods with only 1.5% inaccuracies.
For the purpose of classifying weed and non-weed photos, Patel et al. [ 264] used CNN
models and additional DL models were used for object detection. In comparison to
Intersection over Union (IoU), accuracy and memory consumption of DL models. The
suggested study makes use of ResNet-18, YOLOv3, CenterNet and Faster RCNN. With
an accuracy of 88%, CenterNet performs better than any other model. Moreover, using
RGB photos of monocotyledonous and dicotyledonous weeds, López-Correa et al. [ 265]
compared the Yolov7 and Faster-RCNN weed detection models. The best results were
obtained by RetinaNet, however Faster-RCNN and YOLOv7 also did well especially
with data augmentation. For species of monocot weed, YOLOv7 proved less accurate.
Recently employed the EfficientNet, GoogLeNet and ResNet models to detect weeds in
vegetables. The requirement for real time weed identification was satisfied by the ResNet
model, which showed the maximum computational efficiency of all models with a classi-
fication time of 12.76 ms per photo and a matching frame rate of 80.31 fps. Moreno et al.
[266] created synthetic training images for CNNs focusing on three distinct weeds found

Page 21 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
in tomato crops: Setaria verticillata  L., Solanum nigrum L., and Portulaca oleracea  L.
The Yolov8l model, which has a Frame Detection Speed (FDS) of 10.2 ms, was the best
choice for real-time detection systems. Using 5997 photos of corn plants and four weed
species, Hasan et al. [ 267] produced a tagged weed dataset from the corn weed dataset.
They classified weeds in fields using DL models such as YOLOv7, YOLOv8, and Faster-
RCNN. While YOLOv8m improved outcomes by correcting class imbalance, YOLOv7
and its variants attained great precision and detection accuracy.
4.5 AI for retail marketing of horticultural crops
AI applications are designed to improve profitability, decrease lower risk and increase
return on investment. Currently AI-driven strategies are proving advantageous for mar -
keting horticultural products, contributing to increased revenue for horticultural pro -
ducers [ 23, 27]. Moreover; forecasts are created based on past and present business
activity trends in order to assist with these decisions [ 268, 269]. The retail marketing
sector has significantly benefited from the integration of AI technology across various
domains such as personalized product recommendations, automated customer seg -
mentation and targeting prediction of consumer behavior and preferences, optimization
of pricing and promotions and improved accuracy in forecasting. Furthermore, retail -
ers can leverage AI to enhance forecasting precision and more effectively predict cus -
tomer demand, thereby increasing operational efficiency and reducing costs [ 270–272].
A summary of key AI applications in retail marketing is provided in Table  6. According
to a study by Valecha et al. [ 273], the RF classifier was employed to analyze customer
purchasing behavior taking into account different aspects of shopping habits including
interpersonal, individual, environmental and organizational aspects. Using attributes
taken from historical sales data, Dairu and Shilong [ 274] provided a method that pow -
ered the eXtreme Gradient Boosting (XGBoost) model to forecast future sales.
The Autoregressive Integrated Moving Average (ARIMA) and Long Short-Term Mem-
ory (LSTM) models were beaten by the XGBoost model, which had a Root Mean Square
Error (RMSE) of 0.878. In a related investigation, Swami et al. [ 275] utilized XGBoost,
LSTM, and ARIMA models to predict total sales for products and stores. Compared
to the other models, XGBoost fared better also achieving an RMSE of 0.878. Addition -
ally, in a study focused on vegetable demand forecasting, Priyadarshi et al. [ 276] applied
Table 6 Artificial intelligence-based tools for retail marketing of horticultural produces
Involved technologies Involved entities References
RFID and Blockchain Technology Plant, farm, warehouse centre, transport vehicle, sales mar-
ket, and government departments & third-party regulators
[281]
IoT and Blockchain technology
with distributed databases
Farmer/Producer, processor, wholesaler, retailer, authority
organizations
[282]
IoT and Blockchain smart contracts Farmer, rural credit bank, private warehouse agent, trading
company agent, food processing company
[283]
AI, digital twins (DT), distributed
ledger technology (DLT), and the
Internet of Things (IoT)
Supply chain and decision making of products for marketing [280]
AI AI techniques to analyze customer data, identify customer
preferences, and predict customer behavior to provide AI-
based recommendations
[279]
Digital technology Farmers fruit orchards [284]
AI consumer experience tools
(AI-CE)
Implementing Al Consumer Experience Tools in Supply
Chains
[285]

Page 22 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
several AI models, LSTM, ARIMA, SVR, Gradient Boosting Regression (GBR), Random
Forest Regression (RFR) and XGBoost. LSTM and SVR performed better than the other
algorithms. For tomatoes, the LSTM RMSE values ranged from 3.75 to 15.68, 7.03 to
21.6 for potatoes and 8.20 to 20.77 for onions. Similarly, the SVR RMSE values for pota -
toes, onions and tomatoes ranged from 14.04 to 28.88, 6.28 to 21.11 and 7.92 to 26.8
respectively. In their daily demand forecast for onions and potatoes, Shukla et al. [ 277]
utilized ARIMA and various AI tools. The mean absolute percentage error (MAPE)
was 28.296 for onions and 29.51 for potatoes. As part of their AI toolkit, Arunraj and
Ahrens, [ 278] implemented a number of models for banana sales forecasting, includ -
ing SARIMA, MLPNN-1, MLPNN-2, SARIMA-MLR and SARIMA-QR. Among these,
SARIMA-MLR and SARIMA-QR demonstrated exceptional performance, obtaining
19.14 and 19.35 root mean square errors (RMSE) respectively. In addition, Yaiprasert
and Hidayanto [279] conducted an analysis of consumer data to identify preferences and
predict behaviors through the application of AI techniques. The nearest neighbor and
decision tree algorithms achieved flawless predictions, while the Naïve Bayes algorithm
yielded an accuracy of 97.175% with a margin of error of 0.028. Additionally, a study
by Vilas-Boas et al. [ 280] collected and analyzed data on how stakeholder demands and
product tracking can improve supply chain efficiency providing essential insights for
management.
In recent years, blockchain and IoT-based technologies have gained attention for
enhancing transparency and trust in agri-food supply chains. For example, radio fre -
quency identification (RFID) combined with blockchain has been utilized to establish
a traceability system for China’s agri-food sector [ 281]. Building on this, an integrated
framework incorporating Hazard Analysis and Critical Control Points (HACCP), block -
chain and IoT was proposed to strengthen food safety and traceability in supply chains
[282]. Similarly, a blockchain business network was developed for grain quality assur -
ance and tracking, providing a case study that demonstrates the feasibility of blockchain
applications in agricultural marketing and quality monitoring [ 283]. Such traceability
systems are increasingly relevant for the retail marketing of horticultural crops, where
consumer demand for quality assurance, food safety and supply chain transparency is
rapidly growing. Additionally, Sharma et al. [ 284] examined the utilization of digital
technology by farmers who work on a large and small scale. Cheng et al. [ 285] revealed
that user privacy sensitivity determines the best AI-CE implementation approach.
Because joint implementation reduces comparative disadvantage and channel competi -
tion retailers should use AI-CE when customer sensitivity is low and not when sensitiv -
ity is considerable. They underscored the importance of developing sustainable solutions
that focus on income generation, enhancing supply chain efficiency and minimizing
post-harvest losses throughout the agricultural process.
4.6 AI for prediction and detection of crop loss brought on by natural calamities
It is acknowledged that AI enhances natural catastrophe management [ 286]. Natural
disasters represent a critical area where AI can be effectively applied. The global preva -
lence of natural disasters and the risks they pose to both property and human life are on
the rise. This escalation in risk, often attributed to climate change, coincides with the
rapid advancements in AI and its various applications [ 287, 288]. With the UN's [ 289]
Sendai framework emphasizing their potential for early prediction and monitoring,

Page 23 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
high-accuracy AI and ML modeling algorithms are being employed more and more in
disaster risk reduction. From the perspective of agriculture, drought is one of the most
dangerous and significant catastrophe kinds. Among all catastrophe categories, the
exceptionally low rainfalls that resulted in higher moisture deficits caused 15.1% of crop
losses and 85.8% of animal damage and losses the largest of any disaster [ 290]. Drought
catastrophe risk management has received a lot of attention lately because of very vari -
able weather patterns and international campaigns on water shortage. Zhang et al. [ 291]
used a meta-Gaussian model based on precipitation and soil moisture data to predict
agricultural dryness in China using the standardized soil moisture index (SSI). Addition-
ally, Saha et al. [ 292] employed artificial neural networks (ANN) to create a geographi -
cal drought vulnerability index for efficient risk reduction and monitoring in the Indian
state of Karnataka. Researchers are actively exploring innovative and effective methods
to mitigate the impacts of disasters and alleviate human suffering through the use of AI
in disaster management [293].
Numerous well known deep learning models including SegNet U-Net, FCNs,
FCDenseNet, PSPNet, HRNet and DeepLab, have demonstrated noteworthy success in
a range of applications including as mapping floods, assessing earthquake damage and
delineating forest fires [ 294]. These models exhibit a high degree of effectiveness in dif -
ferentiating between various land cover types, identifying areas that are vulnerable to
additional hazards due to fire and recognizing compromised or destroyed infrastructure.
Worldwide, floods are frequent natural disasters brought on by both man-made and nat-
ural factors [ 295]. In order to identify visual patterns linked to increasing water levels
and buried structures, flood-affected areas must be automated using image processing
and deep learning namely the CNN architecture. Rapid and precise automated evalu -
ation of flood-affected areas is possible with deep CNN models [ 296]. By combining a
CNN algorithm with UNet, UNetFormer, HarDNet, SegFormer, BiSeNetV1, BiSeNetV2,
DDRNet and PIDNet, Safavi and Rahnemoonfar [ 297] were able to attain an accuracy of
more than 60% using FloodNet.
4.7 AI based for Soil health monitoring
The advancement of AI technologies has significantly enhanced the monitoring of soil
health [ 298–300]. Monitoring soil health is greatly aided by machine learning tech -
niques [301]. To assess the health of soil, supervised learning techniques including sup -
port vector regression, random forest and Bayesian estimation are frequently employed.
Bayesian estimate works well for dynamic soil health evaluations because it is a proba -
bilistic method that modifies predictions when fresh soil data becomes available [ 302].
An ensemble learning method called random forest uses many decision trees to create
a model for evaluating the health of soil. Its ability to manage the intricate interactions
between various soil characteristics and environmental conditions without over-fitting
makes it ideal for evaluating the health of soil. It is useful for predicting important soil
quality indicators including microbial activity, moisture content and nutrient levels and
for evaluating big datasets with lots of variables [303].
A supervised learning technique called support vector regression finds the best hyper -
plane to maximize the margin between data points thereby connecting input factors
to the appropriate soil health metrics [ 304]. Moreover, AI, ML and sensing technolo -
gies have opened new avenues for soil health monitoring and fertility management. For

Page 24 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
instance, AI models have been employed to predict Robusta coffee yield based on soil
fertility properties [305], while the emerging concept of the Internet of Things has been
proposed for real-time soil fertility monitoring [ 306]. Embedded machine learning sys -
tems have also been designed to support sustainable soil fertility management and eco
friendly crop prediction [307]. Comprehensive reviews have highlighted the potential of
machine learning approaches in enhancing soil fertility assessment [ 308] and precision
nutrient application techniques for improving both soil fertility and crop yield [ 309].
Furthermore, recent developments in soil fertility indices integrating machine learn -
ing with visible near infrared spectroscopy demonstrate promising directions for non-
destructive soil health evaluation [310].
 PEAT, a start-up located in Berlin has created a DL application called Plantix which
is designed to identify nutrient deficiencies in soil. This application employs algorithms
that link specific foliage patterns to particular soil deficiencies [ 311]. Additionally,
Palaniappan et al. [ 312] developed a system utilizing image processing and an ANN to
assess soil properties thereby facilitating the recommendation of appropriate crops for
the given soil type. In 2024, Bhattacharya and Pandey, [ 313] introduced a power aware
and delay aware TinyML model aimed at managing and monitoring the quality of agri -
cultural soil. This model highlights the potential for farmers to optimize resource alloca -
tion, fertilization and irrigation by effectively tracking and controlling soil conditions,
ultimately enhancing soil yield while minimizing environmental impacts. A summary of
significant applications of AI in soil health monitoring is provided in Table 7.
4.8 AI-based irrigation management
AI techniques, which use sensors and other tools implanted in robots and drones
have proven to be very successful in crops according to water requirements [ 18]. The
definition and scheduling of irrigation prescriptions in irrigation applications could
be improved by AI [ 314–316]. A soil moisture sensor is one of several methods used
to determine the moisture content. It is placed in soil near the root zone of the crop.
An accurate moisture content reading is provided by sensors and sent to the irrigation
controller. According to Dukes et al. [ 317] and Quails et al. [ 318] soil moisture sensors
can also significantly reduce your water usage. Through the use of a moisture sensor,
farmers can adjust the moisture threshold based on the capacity of their soil. Sensors
will only allow the controller to water a zone when the appropriate amount of water or
moisture content falls below the designated threshold. As the scheduled watering time
approaches, it additionally verifies the zone's moisture threshold value before approv -
ing irrigation based on demand. The duration and start time for each zone are neces -
sary [319]. Furthermore, the dielectric constant or soil mass permittivity can be used to
determine the moisture content of soil [ 320]. Kuyper and Balendonck [ 321] describe a
unique technique that integrates dielectric soil moisture sensors into a real-time irriga -
tion control system that is automated. According to Xing et al. [322], the most promising
measuring strategy is the one based on dielectric properties. Furthermore, Kumar [ 323]
discusses irrigation strategies with the primary objective of developing a system that is
more resource efficient and performs better. For example, fertility meters and pH meters
are placed in fields to measure the percentage of the main constituents of soil such as
nitrogen, phosphorus and potassium in order to assess the fertility of the soil.

Page 25 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
Wireless technology is utilized to sow drip irrigation systems for the plants in auto -
matic way. This technique guarantees both the efficient use of water resources and the
fertility of the soil. In order to save labor and time during the irrigation process, Jha et
al. [49] has created an Arduino-based automated irrigation system. Moreover, an auto -
mated robotic model for determining the moisture content and temperature of embed -
ded devices such as Arduino Uno was created by Shekhar et al. [ 324] and sent data to a
Raspberry Pi 3. After detecting the data and converting it to digital form the model ini -
tiates irrigation. Moreover, Savitha and Uma Maheshwari [ 325] additionally developed
the idea for a 40% more productive irrigation system by using Arduino technology to
create remote sensors. In addition, to minimize water waste and maximize crop yield
under water demand conditions, Viani et al. [ 326] created an affordable wireless moni -
toring and decision-support system for agriculture that saves water. This system com -
bined wireless sensors, actuation network technology and consideration of soil and crop
Table 7 Artificial intelligence-based tools for soil health monitoring in horticultural crops
Model Application References
ELM
MLR
RF
Soil Organic Matter
pH
Available K
Available B
Available Zn
Available S
Available P
Available N
Exchangeable Ca
[305]
ANN
IoT
pH level
Temperature
Moisture content of Soil
Humidity of Soil
NPK
Organic Matter
Carbon level
[311]
IoUT Underground soil sensing for fertility monitoring [306]
Machine learning Soil fertility management [307]
Machine learning
Cubist models
Nutrient levels
Soil pH
Climate Conditions
Digital Soil Mapping
Soil Fertility Prediction
[98]
Machine learning
Deep learning
Soil fertility [308]
VRT,
Sensor-based
Techniques,
GIS and GPS
Integration,
Drones and UAVs,
Real-time Monitoring
and Data analysis
Adjusting fertilizer rate of fertilizers, pesticides and seeds,
Soil Conditions (NPK level), weather parameters,
Soil Mapping, Soil Properties, Soil Topography, Accuracy of nutrient
application,
Data can include multispectral and thermal imagery, 3D models of fields,
Soil nutrient management, Irrigation
[309]
VNIR
LUCAS
SVMs
Soil fertility
Soil Properties
[310]
Convolutional Neural
Networks (CNNs),
Recurrent Neural Net-
works (RNNs), and Q
Learning techniques
Soil conditions enables farmers to optimize irrigation, fertilization [313]

Page 26 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
models. The result was an irrigation schedule that was optimized and context aware.
With the help of ML and data from soil moisture sensors, Prasanna Lakshmi et al. [ 327]
created an irrigation model that uses 46% less water when employed on tomatoes and
eggplants.
Additionally, they created software to display graphical data gathered by the surveil -
lance system and webcam views from a system placed all around the plants. Dong et
al. [328] developed an application to control an autonomous precision irrigation system
based on wireless subterranean sensor networks in a center pivot irrigation system uti -
lizing TinyOS software architecture on a far bigger scale. Varatharajalu and Ramprabu
[329] presented another automated irrigation system in which various sensors were
designed for specific functions such as the molecular sensor for improved crop growth,
the pressure regulator sensor to keep pressure constant, the temperature sensor to gauge
the ground's surface temperature and the soil moisture sensor to gauge the moisture
content of the soil. Additionally, physical operations and computation are combined in
cyber-physical systems (CPS). Physical processes can have their resources handled by
embedded systems, sensor networks and controllers typically with system feedback
[316, 330]. Cyber-physical system (CPS) has a tight relationship with the internet and its
users. According to Seshia et al. [ 331], a CPS is a system made up of two parts: a func -
tionally modeled portion and a real component that interacts with the other. Further -
more, Jimenez et al. [316] created a cyber-physical intelligent agent based on the idea of
a rational agent which was created and applied for irrigation scheduling in horticultural
crops. Site-specific and regional environmental data were obtained employing a weather
station and a wireless sensor network respectively. A reasoning approach based on a
heuristic based on yield and water use efficiency criteria was used to construct irriga -
tion prescriptions. A central station was used to receive and process raw data. In the
end, the intelligent agent powers on solenoid valves in the field by activating an actua -
tor system via activation messages. Since the AI based predictive algorithm-based irri -
gation management system is genuinely scalable to any crop by determining the proper
soil capacity level, it is an affordable option for optimizing water management in agri -
culture [332]. CNNs and long short-term memory performed well, while support vec -
tor machines had the lowest accuracy, according to Mokhtar et al. [ 333] assessment of
irrigation water requirements using ML algorithms. Additionally, Srivastava et al. [ 334]
used a RFR and recurrent ANN to create a probabilistic framework for irrigation strate -
gies based on soil moisture, leaf area index and evapotranspiration. Weights were then
adjusted based on actual values. In 2019, Keswani et al. [ 335] created a smart irrigation
system with the help of neural networks (NN) and a wireless sensor network (WSN)
made up of CO2 sensors, daylight intensity sensors, soil moisture (MC) probes, environ-
mental temperature sensors and environmental humidity sensors. Utilizing neural net -
work-based soil water requirement prediction to control individual valves for consistent
water application, the system determines the best irrigation use. Recently, Sapkota et al.
[336] investigated the YOLOv8 and Mask R-CNN ML models for orchard segmentation.
The datasets for the dormant season and the early growth season were both utilized.
According to Sitharthan et al. [337], an intelligent system that irrigates fields based on
environmental conditions have been developed by integrating IoT and 6G with a predic-
tion algorithm based on weather history data and current soil moisture. This system has
achieved 86% accuracy, 89% sensitivity and 91% precision. Idaho researchers, King and

Page 27 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
Shellie, [338] used an AI neural network model to develop a decision support system
(DSS) for precise irrigation on two small commercial vineyards. The system hosted on-
site using edge computing displayed a 12-day history of daily CWSI, soil water avail -
ability, meteorological conditions and demonstrating successful irrigation demands.
A low-cost, IoT-based intelligent module for smart irrigation systems utilizing neural
networks (NN) was proposed by Nawandar and Satpute [ 339] in a different study. Via
sensors that are linked to the IoT module which employs NN-based decision-making to
send commands to the irrigation unit turning on and off water for the necessary zones,
the system continuously monitors temperature, humidity and soil moisture. Ai-based
smart irrigation system in some horticulture crops is presented in Table  8. Moreover, AI
and IoT-based technologies are increasingly being integrated into irrigation management
systems to enhance water use efficiency and crop productivity. For example, IoT-enabled
SCADA systems have been developed for intelligent irrigation control in banana cultiva-
tion [340] while AI-based frameworks have been applied to open-field pineapple farms
for irrigation management coupled with pest and disease prediction [ 341]. Precision
Table 8 Ai-based smart irrigation system in horticulture crops
Ai-based smart ir-
rigation system
Research work Horticultural
crops
Ref-
er-
ences
Internet of Things
(IoT) [SCADA System]
Proposes a Smart Irrigation Control Panel (SICP), based on the
Internet of things, as part of a SCADA system for automation of
irrigation control of said crop, in the experimental farm “Santa
Inés” of the Technique University of Machala
Banana [340]
Sensors and AI Developed intelligent algorithms and use sensor data to deter-
mine climate setpoints, irrigation control and crop manage-
ment strategy
Cherry tomato [196]
IoT, Data-Driven
and AI-empowered
Smart Irrigation
Irrigation Control and Pest/Disease Prediction for Open-field
Pineapple Farm
Pineapple [341]
Precision irrigation
system using the
(IoT)
A smart framework for growing tomatoes is developed, with
influence from IoT devices or modules. With the help of IoT
modules, we can forecast soil moisture levels and fine-tune the
watering schedule
Tomato [342]
Internet of Things
(IoT)
Use the microcontroller which processes the data available
from various sources and gives back the required amount of
water needed for the irrigation of mango trees
Mango [344]
Internet of Things
(IoT)
Proposed a smart irrigation system for optimum usage of water
during irrigation in potato fields
Potato [345]
Internet of Things
(IoT) [DHT11 sensor]
Development of an internet of things-based irrigation control
and monitoringsystem testbed for a chilli plantation
Chilli [346]
Internet of Things
(IoT)
A drip irrigation system that is based on Internet of Things (IoT)
technology for automation of irrigation scheduling was devel-
oped and tested for Egg Plant (Brinjal) crop in vertisols
Egg Plant
(Brinjal)
[347]
Internet of Things
(IoT)
Design a long-range (LoRa) edge IoT computing-based sustain-
able and customized smart irrigation framework to capture the
real-time data of tomato plants
Tomato [343]
Fuzzy logic and wire-
less sensor networks
(WSN)
Develop an advanced system for managing and supervising
irrigation processes, utilizing fuzzy logic and wireless sensor
networks (WSN)
Apple [348]
Neural networks and
fuzzy logic
An intelligent irrigation system based on neural networks and
fuzzy logic, to avoid the presence of pests due to excess rela-
tive humidity in rose crops in Cotopaxi
Roses [349]
AI-supported irriga-
tion system
AI-Supported Autonomous Irrigation Systems on Water
Efficiency and Plant Quality: A Case Study of Geranium
psilostemon Ledeb
Geranium
psilostemon
[350]

Page 28 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
irrigation systems supported by IoT have also been demonstrated in tomato [ 342, 343],
mango [344], potato [345], chilli [346], eggplant [347] and apple orchards [348]. In addi-
tion, AI driven prototypes have been developed for automated irrigation in ornamental
crops such as roses in Cotopaxi [ 349]. Collectively, these studies highlight the potential
of AI and IoT based smart irrigation systems in optimizing resource use and ensuring
sustainable horticultural production. Recently, Oğuztürk et al. [ 350] recently conducted
research in two different environments: one that employed an AI supported irrigation
system and the other that depended on manual watering. Natural plant species may be
successfully grown using AI supported irrigation systems which hold great potential for
water conservation and ecological balance.
4.9 AI based approaches applicable in floriculture and landscaping
Many researchers/landscapers in the landscaping sector of the contemporary ornamen -
tal flower industry have adopted AI based technology [351–353] and have also been very
effective tools for promoting sustainable practices in greenhouse plants and the orna -
mental industry [ 111, 352, 354]. However, compared to the actual accuracy of visual
inspection, the majority of the studies concentrated more on the benefits of DL and the
computational efficiency metrics of various architectures leaving a research gap that
needs to be filled. A wide range of activities have been accomplished with DL including
the detection and identification of healthy flowers [ 355, 356]. Additionally, AI has the
potential to improve supply chain management by tracking the location and condition
of flowers during transportation by using data from cameras and sensors. AI algorithms
have the ability to predict the most economical routes and modes of transportation for
flower delivery which reduces waste and expenses [ 357]. Moreover, supply chain man -
agement could be greatly enhanced by AI like the terms as effective flower produc -
tion, quality and sustainability. In addition, using automated ML techniques, Kwon and
Heo [ 358] developed a model to predict the post-harvest vase life of Lisianthus from
the pre-harvest period. This model identified the most important vase life predictor.
This model shows that vase life may be approximated by the use of attributes that have
a good association with vase life as ML features. In recent study, Kwon and Heo [ 359]
compared the vase life of cut Lisianthus flowers grown in soil, hydroponic (H) and soil
(S) culture methods using the H 2O package ML tool [ 360]. Classifying vase life stages
based on petal color information was more successful with the H-cultivated cut flowers.
This shows that petal color measurement, rather than requiring damaging procedures
can assist reliably detect bad cut flowers and help organize vase life stages. Furthermore,
Herrera and colleagues [ 361] devised a method that employs sophisticated computer
vision in conjunction with UAVs to recognize roses ideal for cultivation. The approach
reduces the amount of effort spent manually counting and monitoring by using DL to
estimate crop yields with a mean average precision of 94.1%.
Conventional techniques for identifying flowers are incorrect, time-consuming and
ineffective. Despite being widely used for floral photo classification and deep learning
convolutional neural networks (CNNs) are challenging to implement on mobile devices
because of parameter redundancy. A machine learning method for flower categorization
was previously established by Zawbaa et al. [ 362] employing segmentation based fractal
texture analysis and scale invariant feature transform. With the SIFT based SVM system
outperforming random forests, the method combines segmentation, feature extraction

Page 29 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
and classification. Furthermore, a compact darknet model for flower categorization was
created by Tian et al. [363]. to automatically extract and categorize floral visual attributes
and deep network model was trained on a dataset of 17 different flower types. When
paired with a softmax classifier, the model outperformed the original model and other
well known techniques, achieving 92% classification accuracy. A flower classification
network design called RCS-net, created by Mao et al. [ 364] also improves the efficiency
and accuracy of floral photo categorization by utilizing channel attention mechanisms
and transfer learning. Through experimental validation, RCS net outperformed well
known models achieving a 96.1% accuracy rate on a floral dataset that was made publicly
available. Furthermore, ResNet-50, a deep convolutional neural network pre-trained on
ImageNet uses residual learning to capture intricate patterns. In one report, Bhuria [365]
achieved an outstanding 91% accuracy rate using ResNet-50 for several types of flower
categorization. The flower dataset was trained using the CNN model VGG16.2 by Zheng
and Lin [366] using transfer learning on the trimmed model. Experiments show that the
pruning strategy yields the highest accuracy of 93.10% while training the flower dataset.
4.9.1 Other important AI-based applications in horticultural production
Researchers at Monash University have utilized computer vision and AI to meticulously
track the movements of various pollinators, including honey bees, hoverflies, moths,
butterflies and wasps. This effort has resulted in the creation of a comprehensive data -
base comprising over 2000 insect tracks recorded at a commercial strawberry farm in
Victoria. This study's main goal is to examine the contributions made by various spe -
cies to the pollination process ultimately enhancing both pollination efficiency and crop
yield. This information will empower farmers to adjust the number and placement of
hives to optimize pollination levels. Additionally, a prototype of a robotic micro air
vehicle designed for autonomous pollination featuring flapping wings was developed by
Chen and Li [ 367]. This innovative device is characterized by its small size, energy effi -
ciency and agility making it well-suited for pollination tasks. It operates by gathering
real time data from crops and flowers through the use of cameras and thermal sensors
which is then transmitted to a central control system via wireless connections to manage
the robotic swarm effectively. To illustrate the concentrations of tomato pigment in the
pericarp and epidermis, Xu and Liu [ 368] developed a logistic model and a first-order
kinetic model. A genotype to phenotype simulation method and a gradient descent-
based method for accurate color conversion were also provided. Experiments verified
that the process could be used to other fruits. In a recent study, Cassity et al. [ 369] used
DBSCAN based filtering and DL to create a volumetric root segmentation technique for
horticulture plant species. They optimized a Mask R-CNN model and obtained good
Dice, IoU, precision and recall scores on scans of onions and poinsettias.
5 AI as a potential tool for sustainable horticultural production
AI is driving a paradigm shift in agriculture, including the horticultural sector by
enabling precision, efficiency and sustainability [ 85, 370, 371]. With the rapid growth of
the global population and the intensification of environmental challenges the demand
for sustainable agricultural practices has become more urgent than ever. AI applications
in horticulture offer promising solutions to these challenges by optimizing resource

Page 30 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
utilization, improving crop management and fostering environmentally responsible pro-
duction systems [372, 373].
The integration of AI within horticultural systems leverages advanced computational
approaches, machine learning algorithms, computer vision and sensor-based technolo -
gies to support data driven decision making. These tools enable producers to monitor
and analyze large-scale, real-time datasets, thereby improving understanding of field
conditions and facilitating timely interventions. Such approaches enhance the quality
and consistency of horticultural produce while mitigating risks related to weeds, pests
and diseases. The growing availability of sophisticated sensors, smart instruments and
automated machinery is further transforming horticultural practices. Production of
fruits, vegetables and floricultural crops is influenced by diverse factors such as weather
variability, soil properties, water availability, harvesting techniques and the prevalence of
plant pathogens and pests. AI driven solutions provide predictive insights into these fac -
tors enabling proactive crop management and reducing post harvest losses. For example,
AI can assist in minimizing spoilage of fresh produce through advanced logistics plan -
ning and the generation of retail marketing intelligence [27].
The convergence of AI algorithms, decision support systems and automated data
acquisition will accelerate the development of cutting-edge strategies for sustainable
horticultural production. Moreover, the deployment of robotic systems both terrestrial
and aerial will enhance mechanization and digitalization with applications in harvesting,
disease detection, pest management and field monitoring. Collectively, these advance -
ments demonstrate that AI is not only a supportive tool but a transformative driver for
achieving sustainability, efficiency and resilience in horticultural production systems.
5.1 Practical challenges in the adoption of AI technologies in horticulture
5.1.1 Technical and infrastructural barriers
Although AI technologies such as sensors, drones and decision support systems have
shown considerable promise their implementation in real world horticulture often
encounters infrastructural limitations. For instance, smallholder tomato farms in a
recent case study employing IoT and ML based irrigation systems reported up to 25%
yield improvement and 35% water savings [ 374]. However, these benefits were condi -
tional on reliable internet connectivity and timely sensor maintenance both of which are
often inconsistent in rural agricultural regions. Similar findings from Algerian trials with
low cost fog-IoT systems for anomaly detection highlight that without stable infrastruc -
ture and routine device upkeep the sustainability of such solutions remains uncertain
[375].
5.1.2 Economic and financial constraints
One major obstacle for small and medium-sized horticultural businesses is the cost of
purchasing, setting up and maintaining sophisticated AI-based solutions. Evidence from
organic farms in the Visegrad countries (Czech Republic, Hungary, Poland and Slovakia)
demonstrates that although drones and remote-sensing technologies can enhance crop
monitoring farmers remain hesitant due to high upfront costs and uncertain return on
investment [376]. Even where subsidies or government incentives are available they are
frequently insufficient to offset the perceived risks particularly for farms operating on
narrow profit margins.

Page 31 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
5.1.3 Knowledge and skill gaps
A recurring challenge is the lack of technical expertise among farmers and field work -
ers to effectively integrate and interpret AI outputs. Studies have shown that while AI
enabled anomaly detection or disease diagnosis systems can be highly accurate adoption
is constrained by farmers limited familiarity with digital interfaces and data interpreta -
tion. This knowledge gap not only reduces the confidence of users in AI technologies but
also increases their dependency on external technical support raising operational costs
and slowing down widespread adoption [377].
5.1.4 Technological limitations and integration issues
Despite rapid advancements many AI tools face limitations in adaptability under het -
erogeneous field conditions. For example, robotics designed for harvesting encounter
performance bottlenecks in varying canopy structures and lighting environments lead -
ing to reduced accuracy in fruit detection and picking [ 378]. A review on agricultural
robotics adoption further emphasizes that the lack of interoperability with existing farm
machinery and the absence of robust business models hinder commercial deployment
[379]. Consequently, while AI integration into robotics is theoretically sound its transla -
tion into scalable solutions remains slow.
5.1.5 Farmer perceptions and socio-cultural resistance
Beyond technical and financial barriers, socio-cultural resistance also plays a role. In
Algerian smallholder communities, even low cost AI enabled irrigation systems encoun -
tered resistance due to distrust of new technologies and fear of device malfunction [380].
Such perceptions highlight that farmer adoption is not merely a function of techno -
logical performance but is also influenced by trust, familiarity and perceived reliability.
Awareness campaigns, participatory design and user-friendly interfaces may therefore
be as important as the technology itself in driving adoption.
6 Conclusion
Artificial intelligence is rapidly reshaping the horticultural sector by enabling precise
monitoring, predictive modelling, and automation throughout the entire production
chain from soil evaluation and crop management to harvesting, postharvest processes,
and market distribution. Through the integration of data from sensors, drones, and sat -
ellite imagery, AI enhances real-time decision-making, improves resource efficiency, and
helps reduce risks related to climate fluctuations, pests, and diseases. These advance -
ments establish AI as a major force driving sustainability, efficiency, and resilience
in horticulture. Moving forward, the continued adoption of AI presents a remarkable
opportunity to link productivity improvements with environmental stewardship. By
systematically addressing existing challenges AI can evolve into not only a cornerstone
of precision agriculture but also a catalyst for equitable, climate-resilient horticultural
systems.
7 Future directions
AI has the potential to transform horticulture by enhancing efficiency, sustainability, and
resilience, but its practical impact relies on addressing current technical and operational
limitations. Future studies should prioritize the development of unified and interoperable

Page 32 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
data standards to integrate diverse datasets from sensors, drones, and imaging technolo-
gies. Approaches such as transfer learning, domain adaptation, and ensemble modelling
can be explored to improve the robustness and adaptability of AI models across differ -
ent crops, climates, and field conditions. High deployment expenses, weak digital infra -
structure in rural areas, limited access to robust datasets, and insufficient technical skills
among farmers continue to hinder broad adoption of AI technologies. These challenges
highlight the need for further research and development. Additionally, many AI systems
are primarily designed for large commercial farming operations, leaving smallholder
farmers who constitute a major share of global horticultural producers at a disadvantage.
Overcoming these limitations, calls for targeted interventions, including investment in
affordable and scalable AI tools, improved rural connectivity, participatory training and
capacity-building initiatives, and policy frameworks that offer financial incentives and
risk-sharing options. Moreover, extensive field testing across diverse agro-ecological
regions will be crucial to verify the reliability and scalability of AI solutions.
In addition to technological advancements, future research must also address socio-
economic and human-centered factors. Developing cost-effective, modular AI tools tai -
lored to smallholder farmers, creating user-friendly interfaces, and offering participatory
training initiatives can enhance adoption and strengthen local capacities. Furthermore,
examining enabling policies, regulatory frameworks, and incentive structures is essential
to promote equitable access and responsible use of AI systems. By combining technical
innovation with social and policy considerations, upcoming efforts can help transform
AI advancements into practical, sustainable, and inclusive field-ready solutions.
Acknowledgements
All authors are thankful to anonymous reviewers who have made significant comments to improve the manuscript.
Author contributions
Vidisha Chaudhary(V.C.): Write the manuscript Mukesh Kumar (M.K.): Edited the manuscript Veena Chaudhary (V.C): Final
edited the paperRavi Kumar (R.K): Prepared the figureChetan Chauhan (C.C): Paper collected.
Funding
No funding was associated with this work.
Data availability
No datasets were generated or analysed during the current study.
Declarations
Conflict of interests
The authors declare no competing interests.
Received: 23 June 2025 / Accepted: 11 December 2025
References
1. Turing AM. Computing machinery and intelligence. Mind. 1950;59(236):433–60. https://doi.org/10.1093/mind/LIX.236.433.
2. Holzinger A, Kickmeier-Rust M, Müller H. Kandinsky patterns as IQ-test for machine learning. Lecture notes in computer
science LNCS 11713. Cham: Springer/Nature; 2019. p. 1–14. https://doi.org/10.1007/978-3-030-29726-8-1.
3. McCarthy J, Minsky ML, Rochester N, Shannon CE. A proposal for the dartmouth summer research project on artificial
intelligence, August 31, 1955. AI Mag. 2006;27(4):12–4. https://doi.org/10.1609/aimag.v27i4.1904.
4. Bratko I, Muggleton S. Applications of inductive logic programming. Commun ACM. 1995;38(11):65–70.  h t t p s : / / d o i . o r g / 1 0 .
1 1 4 5 / 2 1 9 7 1 7 . 2 1 9 7 7 1     .
5. Muggleton SH, Schmid U, Zeller C, Tamaddoni-Nezhad A, Besold T. Ultra-strong machine learning: comprehensibility of
programs learned with ILP . Mach Learn. 2018;107:1119–40. https://doi.org/10.1007/s10994-018-5707-3.
6. Thirumagal P , Abdulwahid AH, HadiAbdulwahid A, Kholiya D, Rajan R, Gupta M. IoT and machine learning based affordable
smart farming. In: Proceedings of the 2023 Eighth International Conference on Science Technology Engineering and
Mathematics (ICONSTEM), Chennai, India, 7–11 August 2023; Institute of Electrical and Electronics Engineers Inc.: Piscat-
away, NJ, USA, 2023; pp. 1–6.

Page 33 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
7. Das R, Bhatt SS, Kathuria S, Singh R, Chhabra G, Malik PK. AI and Internet of Things Based Technological Advancement in
Domain of Horticulture 4.0. In: Proceedings of the 2023 IEEE Devices for Integrated Circuit (DevIC), Kalyani, India, 7–8 April
2023; Institute of Electrical and Electronics Engineers Inc.: Piscataway, NJ, USA, 2023; pp. 207–211.
8. Qi Q, Tao F, Hu T, Anwer N, Liu A, Wei Y, et al. Enabling technologies and tools for digital twin. J Manuf Syst. 2021;58:3–21.
https://doi.org/10.1016/j.jmsy.2019.10.001.
9. Ariesen-Verschuur N, Verdouw C, Tekinerdogan B. Digital twins in greenhouse horticulture: a review. Comput Electron
Agric. 2022;199:107183.
10. Kutyrev A, Kiktev N, Jewiarz M, Khort D, Smirnov I, Zubina V, et al. Robotic platform for horticulture: assessment methodol-
ogy and increasing the level of autonomy. Sensors. 2022;22:8901.
11. Li Q, Huarui W. Research on vegetable growth monitoring platform based on facility agricultural IoT. In: International
conference on geo-informatics in resource management and sustainable ecosystem. Springer, Singapore. 2016
12. Kim S, Lee M, Shin C. IoT-based strawberry disease prediction system for smart farming. Sensors (Basel). 2018;18(11):4051.
https://doi.org/10.3390/s18114051.
13. Hafeez A, Husain MA, Singh SP , Chauhan A, Khan MT, Kumar N, et al. Implementation of drone technology for farm moni-
toring & pesticide spraying: a review. Inf Process Agric. 2023;10(2):192–203.
14. Fuentes A, Yoon S, Kim CS, Park SD. A robust deep-learning-based detector for real-time tomato plant diseases and pests’
recognition. Sensors (Basel). 2017;17:2022.
15. Subeesh A, Mehta CR. Automation and digitization of agriculture using artificial intelligence and internet of things. Artif
Intell Agric. 2021;5:278–91.
16. Shahriar S, Corradini MG, Sharif S, Moussa M, Dara R. The Role of Generative Artificial Intelligence in Digital Agri-Food. J
Agric Food Res. 2025;20:101787.
17. Liakos K, Busato P , Moshou D, Pearson S, Bochtis D. Machine learning in agriculture: a review. Sensors. 2018;18(8):2674.
https://doi.org/10.3390/s18082674.
18. Talaviya T, Shah D, Patel N, Yagnik H, Shah M. Implementation of AI in agriculture for optimization of irrigation and applica-
tion of pesticides and herbicides. AI in Agric. 2020;4:58–73.
19. Ben Ayed R, Hanana M. AI to improve the food and agriculture sector. J Food Qual. 2021;2021(1):5584754.
20. Javaid M, Haleem A, Khan IH, Suman R. Understanding the potential applications of AI in Agriculture Sector. Adv Agro-
chem. 2023;2(1):15–30.
21. De Ocampo ALP , Montalbo FJP . A multi-vision monitoring framework for simultaneous real-time unmanned aerial moni-
toring of farmer activity and crop health. Smart Agric Technol. 2024;8:100466.
22. Raj EFI, Appadurai M, Thiyaharajan D, Pushparaj TL. State-of-the-art technologies for crop health monitoring in the mod-
ern precision agriculture. In: precision agriculture for sustainability (pp. 21–39). Apple Academic Press. 2024.
23. Kumar V, Jakhwal R, Chaudhary N, Singh S. AI in horticulture crops. Ann Hortic. 2023;16(1):72–9.
24. Tempelaere A, De Ketelaere B, He J, Kalfas I, Pieters M, Saeys W, et al. An introduction to AI in machine vision for posthar-
vest detection of disorders in horticultural products. Postharvest Biol Technol. 2023;206:112576.
25. Yang B, Xu Y. Applications of deep-learning approaches in horticultural research: a review. Hortic Res. 2021.  h t t p s : / / d o i . o r g
/ 1 0 . 1 0 3 8 / s 4 1 4 3 8 - 0 2 1 - 0 0 5 6 0 - 9     .
26. Manonmani S, Senthilkumar S, Govind USA, Manivannan S. Application of AI in fruit production: a review. Agric Sci Dig.
2024;44(1):1–5. https://doi.org/10.18805/ag.D-5482.
27. Opara IK, Opara UL, Okolie JA, Fawole OA. Machine learning application in horticulture and prospects for predicting fresh
produce losses and waste: a review. Plants. 2024;13(9):1200.
28. Shaheb MR, Sarker A, Shearer SA. Precision agriculture for sustainable soil and crop management. In Soil Sci Emerging
Technol Global Perspect Appl. 2022. https://doi.org/10.5772/intechopen.101759.
29. Gao L, Zhang M, Chen G. An intelligent irrigation system based on wireless sensor network and fuzzy control. J Netw.
2013;8(5):1080.
30. Carrasquilla-Batista A, Chacon-Rodrıguez A. Proposal of a fuzzy logic controller for the improvement of irrigation schedul-
ing decision-making in greenhouse horticulture. In: 2017 1st Conference on PhD Research in Microelectronics and
Electronics Latin America (PRIME-LA) (pp. 1–4). IEEE. 2017.
31. Karar ME, Al-Rasheed MF, Al-Rasheed AF, Reyad O. IoT and neural network-based water pumping control system for smart
irrigation. arXiv preprint arXiv:2005.04158. 2020.
32. Xiao J, Liu D. Water-saving irrigation intelligent control system based on STC89C52 MCU. In: future control and automa-
tion: proceedings of the 2nd international conference on future control and automation (ICFCA 2012)-Volume 2 (pp.
223–230). Springer Berlin Heidelberg. 2012.
33. Kabir MS, Islam S, Ali M, Chowdhury M, Chung SO, Noh DH. Environmental sensing and remote communication for smart
farming: a review. Precis Agric. 2022;4:82.
34. Zhang M, Han Y, Li D, Xu S, Huang Y. Smart horticulture as an emerging interdisciplinary field combining novel solutions:
past development, current challenges, and future perspectives. Hortic Plant J. 2023.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . h p j . 2 0 2 3 . 0 3 . 0
1 5     .
35. Singh R, Singh R, Gehlot A, Akram SV, Priyadarshi N, Twala B. Horticulture 4.0: Adoption of industry 4.0 technologies in
horticulture for meeting sustainable farming. Appl Sci. 2022;12(24):12557.
36. Ghosh I. AI in horticultural crop improvement. In: Innovative methods in horticultural crop improvement: molecular tools,
nanotechnology and AI. Cham: Springer International Publishing; 2024. p. 25–47.
37. Gammanpila HW, Sashika MN, Priyadarshani SVGN. Advancing horticultural crop loss reduction through robotic and AI
technologies: innovations, applications, and practical implications. Adv Agric. 2024;2024(1):2472111.
38. Pearson S. Artificial intelligence in horticulture. J Hortic Sci Biotechnol. 2025.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  8 0 / 1 4  6 2 0 3 1  6 . 2 0 2 5  . 2 4 7  5
4 0 1.
39. Carrera-Rivera A, Ochoa W, Larrinaga F, Lasa G. How-to conduct a systematic literature review: a quick guide for computer
science research. MethodsX. 2022;9:101895.
40. Abd Rahman NS, Arifin K, Aiyub K. Systematic literature review on new technologies in agriculture: present and future.
PaperASIA. 2025;41(1b):168–83.

Page 34 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
41. Ren S, Zhang Y, Liu Y, Sakao T, Huisingh D, Almeida CMVB. A comprehensive review of big data analytics throughout prod-
uct lifecycle to support sustainable smart manufacturing: a framework, challenges and future research directions. J Clean
Prod. 2019;210:1343–65.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  1 6 / j .  j c l e p  r o . 2 0 1  8 . 1 1  . 0 2 5.
42. Qu C, Kim E. Reviewing the roles of AI-integrated technologies in sustainable supply chain management: research propo-
sitions and a framework for future directions. Sustainability. 2024. https://doi.org/10.3390/su16146186.
43. Meshram V, Patil K, Meshram V, Hanchate D, Ramkteke SD. Machine learning in agriculture domain: a state-of-art survey.
Artif Intell Life Sci. 2021;1:100010.
44. Durai SKS, Shamili MD. Smart farming using machine learning and deep learning techniques. Decis Anal J. 2022;3:100041.
45. Taye MM. Understanding of machine learning with deep learning: architectures, workflow, applications and future direc-
tions. Computers. 2023;12(5):91.
46. Gano B, Bhadra S, Vilbig JM, Ahmed N, Sagan V, Shakoor N. Drone-based imaging sensors, techniques, and applications in
plant phenotyping for crop breeding: a comprehensive review. Plant Phenome J. 2024;7(1):e20100.
47. Shahid N, Rappon T, Berta W. Applications of artificial neural networks in health care organizational decision-making: a
scoping review. PLoS ONE. 2019;19(2):e0212356. https://doi.org/10.1371/journal.pone.0212356.
48. Shah D, Dixit R, Shah A, Shah P , Shah M. A comprehensive analysis regarding several breakthroughs based on computer
intelligence targeting various syndromes. Augment Hum Res. 2020;5:14. https://doi.org/10.1007/s41133-020-00033-z.
49. Jha K, Doshi A, Patel P , Shah M. A comprehensive review on automation in agriculture using AI. AI in Agric. 2019;2:1–12.
50. Mikhailov GG, Orobinskaya VN, Pachina NN, Kostoglotov AA, Lavrova TN, Blinnikov VA. Methodology and technology of
using neural networks in agriculture. In: 2024 4th International Conference on Technology Enhanced Learning in Higher
Education (TELE) (pp. 198–202). IEEE. 2024.
51. Yang H, Liusheng W, Junmin Hongli X. Wireless sensor networks for intensive irrigated agriculture, consumer communica-
tions and networking conference, 2007. CCNC 2007. 4th IEEE. pp. 197–201 Las Vegas, Nevada.
52. Ghazal S, Munir A, Qureshi WS. Computer vision in smart agriculture and precision farming: techniques and applications.
Artif Intell Agric. 2024;13:64–83. https://doi.org/10.1016/j.aiia.2024.06.004.
53. Zhang Y, Carballo A, Yang H, Takeda K. Perception and sensing for autonomous vehicles under adverse weather condi-
tions: a survey. ISPRS J Photogramm Remote Sens. 2023;196:146–77.
54. Gao P , Adnan M. Overview of emerging electronics technologies for artificial intelligence: a review. Mater Today Electron.
2025. https://doi.org/10.1016/j.mtelec.2025.100136.
55. Kamilaris A, Prenafeta-Boldú FX. Deep learning in agriculture: a survey. Comput Electron Agric. 2018;147:70–90.
56. Cui S, Liu F, Wang Z, Zhou X, Yang B, Li H, et al. A lightweight and accurate object detector using dilated aggregation
network for autonomous driving. Electronics. 2024;2024(13):3410.
57. Liu Y, Sun X, Shao W, Yuan Y. S2ANet: combining local spectral and spatial point grouping for point cloud processing.
Virtual Real Intell Hardw. 2024;2024(6):267–79.
58. Ali R, Sheng B, Li P , Chen Y, Li H, Yang P , et al. Optic disk and cup segmentation through fuzzy broad learning system for
glaucoma screening. IEEE Trans Industr Inf. 2020;17(4):2476–87.
59. Dai L, Wu L, Li H, Cai C, Wu Q, Kong H, et al. A deep learning system for detecting diabetic retinopathy across the disease
spectrum. Nat Commun. 2021;12:3242.
60. Chen Z, Huang H, Andrusenko A, Hrinchuk O, Puvvada KC, Li J, Ginsburg B. Salm: speech-augmented language model
with in-context learning for speech recognition and translation. In: ICASSP 2024–2024 IEEE International Conference on
Acoustics, Speech and Signal Processing (ICASSP) (pp. 13521–13525). IEEE. 2024.
61. Krizhevsky A, Sutskever I, Hinton GE. ImageNet classification with deep convolutional neural networks. In: Pereira, F.,
Burges, C.J.C., Bottou, L., Weinberger, K.Q. (Eds.), Advances in Neural Information Processing Systems. 25. Curran Associates,
Inc, pp. 1097–1105. 2012.
62. Zhou Y, Wang M. Remote sensing image classification based on AlexNet network model. In: Hung J, Yen N, Chang JW, edi-
tors. Frontier computing. FC 2019. Lecture notes in electrical engineering, vol. 551. Singapore: Springer; 2020.  h t t p s :  / / d o i  . o
r g / 1  0 . 1 0  0 7 / 9 7  8 - 9 8 1  - 1 5 - 3 2  5 0 - 4  _ 1 1 7.
63. Tammina S. Transfer learning using vgg-16 with deep convolutional neural network for classifying images. Int J Sci Res Pub
(IJSRP). 2019;9(10):143–50.
64. Anand R, Shanthi T, Nithish MS, Lakshman S. Face recognition and classification using GoogleNET architecture. In: Soft
Computing for Problem Solving SocProS 2018, vol. 1. Singapore: Springer Singapore; 2020. p. 261–9.
65. Ajitha ME, Nivedha MV, Parvathi MB. Detection and prevention of tomato leaf disease using convolutional neural network
and inception net. In: 2024 Third International Conference on Intelligent Techniques in Control, Optimization and Signal
Processing (INCOS) (pp. 1–6). IEEE. 2024.
66. He K, Zhang X, Ren S, Sun J. Deep residual learning for image recognition. In: Proceedings of the IEEE conference on
computer vision and pattern recognition (pp. 770–778). 2016.
67. Hassan E, Hossain MS, Saber A, Elmougy S, Ghoneim A, Muhammad G. A quantum convolutional network and ResNet
(50)-based classification architecture for the MNIST medical dataset. Biomed Signal Process Control. 2024;87:105560.
68. Hou Y, Wu Z, Cai X, Zhu T. The application of improved densenet algorithm in accurate image recognition. Sci Rep.
2024;14(1):8645.
69. Ghous U, Sarfraz MS, Ahmad M, Li C, Hong D. (2+ 1) D extreme xception net for hyperspectral image classification. IEEE J
Select Top Appl Earth Observ Remote Sens. 2024;17:5159–72.
70. Vats S, Bhati JP , Singla A, Kukreja V, Sharma R. Advanced image classification on intel datasets using optimized EfficientNet
and MobileNetV2. In: 2024 IEEE 9th International Conference for Convergence in Technology (I2CT) (pp. 1–4). IEEE. 2024.
71. Krishnamoorthy TV, Venkataiah C, Rao YM, Prasad DR, Chowdary KU, Jayamma M, et al. A novel NASNet model with LIME
expandability for lung disease classification. Biomed Signal Process Control. 2024;93:106114.
72. Bird JJ, Lotfi A. Cifake: image classification and explainable identification of ai-generated synthetic images. IEEE Access.
2024. https://doi.org/10.1109/ACCESS.2024.3356122.
73. Siddique N, Paheding S, Elkin CP , Devabhaktuni V. U-net and its variants for medical image segmentation: a review of
theory and applications. IEEE Access. 2021;9:82031–57.
74. Redmon J, Divvala S, Girshick R, Farhadi A. You only look once: unified, real-time object detection. In: proceedings of the
IEEE conference on computer vision and pattern recognition, pp. 779–788. http://pjreddie.com/yolo/. 2016.

Page 35 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
75. Amemiya T, Leow CS, Buayai P , Makino K, Mao X, Nishizaki H. Appropriate grape color estimation based on metric learning
for judging harvest timing. Vis Comput. 2022;38(12):4083–94.
76. Soroush R, Baleghi Y. NIR/RGB image fusion for scene classification using deep neural networks. Vis Comput.
2023;39:2725–39. https://doi.org/10.1007/s00371-022-02488-0.
77. Girshick R. Fast R-CNN. In Proceedings of the (2015). IEEE international conference on computer vision (ICCV), Santiago,
Chile, 7–13 December 2015; pp. 1440–1448.
78. Ren S, He K, Girshick R, Sun J. Faster R-CNN: towards real-time object detection with region proposal networks. IEEE Trans
Pattern Anal Mach Intell. 2017;39:1137–49.
79. He K, Gkioxari G, Dollár P , Girshick R. Mask R-CNN. In: proceedings of the 2017 IEEE international conference on computer
vision (ICCV), Venice, Italy, 22–29 October 2017; Institute of Electrical and Electronics Engineers Inc.: Piscataway, NJ, USA,
2017; pp. 2961–2969.
80. Cireşan D, Meier U, Masci J, Schmidhuber J. Multi-column deep neural network for traffic sign classification. Neural Netw.
2012;32:333–8.
81. Indolia S, Goswami AK, Mishra S, Asopa P . Conceptual understanding of convolutional neural network- a deep learning
approach. Procedia Comput Sci. 2018;132:679–88. https://doi.org/10.1016/j.procs.2018.05.069.
82. Matta P , Pant B. Internet-of-things: genesis, challenges and applications. J Eng Sci Technol. 2019;14:1717–50.
83. Sreekantha DK. Kavya AM. Agricultural crop monitoring using IOT-a study. In: 2017 11th international conference on intel-
ligent systems and control (ISCO), 2017; pp. 134–139. https://doi .org/10.110 9/ISCO.2017 .78559 68
84. Yang LB. Application of AI in electrical automation control. Procedia Comput Sci Proc Int Conf Mechatron Intell Robot
(ICMIR-2019). 2020;166:292–5. https://doi.org/10.1016/j.procs.2020.02.097.
85. Mana AA, Allouhi A, Hamrani A, Rahman S, el Jamaoui I, Jayachandran K. Sustainable AI-based production agriculture:
exploring AI applications and implications in agricultural practices. Smart Agric Technol. 2024;7:100416.
86. Wang C, Luo L. Application of smart technology and equipment in horticulture. Horticulturae. 2024;10(7):676.
87. Padhiary M. The convergence of deep learning, IoT, sensors, and farm machinery in agriculture. In: designing sustainable
internet of things solutions for smart industries (pp. 109–142). IGI Global. 2025.
88. Cubero S, Marco-Noales E, Aleixos N, Barbé S, Blasco J. Robhortic: a field robot to detect pests and diseases in horticultural
crops by proximal sensing. Agriculture. 2020;10(7):276.
89. Woschank M, Rauch E, Zsifkovits H. A review of further directions for AI, machine learning, and deep learning in smart
logistics. Sustainability. 2020;12(9):3760.
90. Soori M, Arezoo B, Dastres R. AI, machine learning and deep learning in advanced robotics, a review. Cogn Robot.
2023;3:54–70.
91. Padhiary M, Kumar R. Enhancing agriculture through AI vision and machine learning: the evolution of smart farming. In:
Advancements in intelligent process automation (pp. 295–324). IGI Global. 2025.
92. Linaza MT, Posada J, Bund J, Eisert P , Quartulli M, Döllner J, et al. Data-driven AI applications for sustainable precision
agriculture. Agronomy. 2021;11(6):1227.
93. Fahle S, Prinz C, Kuhlenkötter B. Systematic review on machine learning (ML) methods for manufacturing processes–Iden-
tifying AI (AI) methods for field application. Procedia CIRP . 2020;93:413–8.
94. Vrontis D, Christofi M, Pereira V, Tarba S, Makrides A, Trichina E. AI, robotics, advanced technologies and human resource
management: a systematic review. In: AI and international HRM, 2023; pp. 172–201.
95. Howard J. AI: implications for the future of work. Am J Ind Med. 2019;62(11):917–26.
96. Wang XY, Yang LY, Huang ZX, Ji ZP , He YQ. Collaborative path planning for agricultural mobile robots: A review. In: interna-
tional conference on autonomous unmanned systems, pp. 2942–2952. 2021.
97. Fountas S, Mylonas N, Malounas I, Rodias E, Hellmann Santos C, Pekkeriet E. Agricultural robotics for field operations. Sen-
sors. 2020;20:2672.
98. Kumar A, Sharma H, Kumar S. AI-based soil fertility management review: challenges and opportunities. J Surv Fish Sci.
2022;8:283–8.
99. Cho S, Kim T, Jung DH, Park SH, Na Y, Ihn YS, et al. Plant growth information measurement based on object detection and
image fusion using a smart farm robot. Comput Electron Agric. 2023;207:107703.
100. Wang W, Li CY, Chu LH, Qu CY. Study on air-ground amphibious agricultural information collection robot. In: 13th interna-
tional conference on ubiquitous robots and ambient intelligence, pp. 938–944. 2016.
101. Kabir H, Tham ML, Chang YC. Internet of robotic things for mobile robots: concepts, technologies, challenges, applications,
and future directions. Digit Commun Netw. 2023;9(6):1265–90.
102. Wu XL, Aravecchia S, Lottes P , Stachniss C, Pradalier C. Robotic weed control using automated weed and crop classifica-
tion. J Field Robot. 2020;37:322–40.
103. Meshram AT, Vanalkar AV, Kalambe KB, Badar AM. Pesticide spraying robot for precision agriculture: a categorical literature
review and future trends. J Field Robot. 2021;39:153–71.
104. Bykov S. World trends in the creation of robots for spraying crops. In: E3S Web of Conferences (Vol. 380, p. 01011). EDP
Sciences. 2023.
105. Ohi N, Lassak K, Watson R, Strader J, Du Y, Yang C, Hedrick G, Nguyen J, Harper S, Reynolds D. Design of an autonomous
precision pollination robot. In: 2018 IEEE/RSJ international conference on intelligent robots and systems (IROS) IEEE, pp.
7711–7718. 2018.
106. Li M, Azizi A, Zhang Z, Yuan D, Wang X. Sensing and automation technologies applied in pollination. In: Towards
Unmanned Apple Orchard Production Cycle: Recent New Technologies (pp. 123–137). Singapore: Springer Nature Singa-
pore. 2023.
107. Thenmozhi S, Mahima V, Maheswar R. Gps based autonomous ground vehicle for agricultural utility. In: innovations in
electronics and communication engineering, pp. 143–150. 2019.
108. Huang CJ, Jing Z, Chen Z, Boshi L, Dekui X. Beidou-GPS integrated dual-system with multi-satellites for positioning and
navigating farm vehicles. Int J Agric Biol Eng. 2015;8:79–85.
109. Yue G, Pan YT. Intelligent control system of agricultural unmanned tractor tillage trajectory. J Intell Fuzzy Syst.
2020;38:7449–59.
110. Hou G, Chen H, Jiang M, Niu R. An overview of the application of machine vision in recognition and localization of fruit
and vegetable harvesting robots. Agriculture. 2023;13(9):1814.

Page 36 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
111. Mahmud MS, Zahid A, Das AK. Sensing and automation technologies for ornamental nursery crop production: current
status and future prospects. Sensors. 2023;23(4):1818.
112. Hutsol T, Kutyrev A, Kiktev N, Biliuk M. Robotic technologies in horticulture: analysis and implementation prospects. Agric
Eng. 2023;27(1):113–33.
113. Cunliffe AM, Brazier RE, Anderson K. Ultra-fine grain landscape-scale quantification of dryland vegetation structure with
drone-acquired structure-from-motion photogrammetry. Remote Sens Environ. 2016;183:129–43.
114. Yang G, Liu J, Zhao C, Li Z, Huang Y, Yu H, et al. Unmanned aerial vehicle remote sensing for field-based crop phenotyping:
current status and perspectives. Front Plant Sci. 2017;8:1111.
115. Deng L, Mao Z, Li X, Hu Z, Duan F, Yan Y. UAV-based multispectral remote sensing for precision agriculture: a comparison
between different cameras. ISPRS J Photogramm Remote Sens. 2018;146:124–36.
116. Dainelli R, Toscano P , Di Gennaro SF, Matese A. Recent advances in unmanned aerial vehicle forest remote sensing—a
systematic review. Part I: a general framework. Forests. 2021;12(3):327.
117. Zhang R, Hewitt A, Li L, Yuan H, Ferguson JC, Chen L. Advanced technologies of UAV application in crop pest, disease and
weed control. Front Plant Sci. 2023;14:1253841.
118. Canicattì M, Vallone M. Drones in vegetable crops: a systematic literature review. Smart Agric Technol. 2024.  h t t p s : / / d o i . o r g
/ 1 0 . 1 0 1 6 / j . a t e c h . 2 0 2 4 . 1 0 0 3 9 6     .
119. Swetha DN, Balaji S. Agriculture cloud system based emphatic data analysis and crop yield prediction using hybrid AI. J
Phys Conf Ser. 2021;2040(1):012010.
120. Fuentes-Peñailillo F, Gutter K, Vega R, Silva GC. Transformative technologies in digital agriculture: leveraging Internet of
Things, remote sensing, and AI for smart crop management. J Sens Actuator Netw. 2024;13(4):39.
121. Padhiary M, Saikia P , Roy P , Hussain N, Kumar K, Mr PS. A review on advancing agricultural efficiency through geographic
information systems, remote sensing, and automated systems. Cureus J Eng. 2025.  h t t p s : / / d o i . o r g / 1 0 . 7 7 5 9 / s 4 4 3 8 8 - 0 2 4 - 0 0
5 5 9 - 7     .
122. Maniyath SR, Vinod PV, Niveditha M, Pooja R, Prasad Bhat N, Shashank N, Hebbar R. Plant disease detection using machine
learning. In: proceedings of the 2018 international conference on design innovations for 3Cs compute communicate
control (ICDI3C 2018), Bangalore, India, 25–28 April 2018; pp. 41–45. 2018.
123. Petrellis N. Mobile application for plant disease classification based on symptom signatures. In: proceedings of the 21st
pan-hellenic conference on informatics, Larissa, Greece, pp. 1–6. 2017.
124. Gossen BD, McDonald MR. New technologies could enhance natural biological control and disease management and
reduce reliance on synthetic pesticides. Can J Plant Pathol. 2020;42(1):30–40.
125. Jafar A, Bibi N, Naqvi RA, Sadeghi-Niaraki A, Jeong D. Revolutionizing agriculture with AI: plant disease detection methods,
applications, and their limitations. Front Plant Sci. 2024;15:1356260.
126. Christakakis P , Papadopoulou G, Mikos G, Kalogiannidis N, Ioannidis D, Tzovaras D, et al. Smartphone-based citizen science
tool for plant disease and insect pest detection using AI. Technologies. 2024;12:101.
127. Hang L, Che J, Song P , et al. Studies on pest prediction based on machine learning and image processing technologies. J
Southwest Univ (Natural Science Edition). 2020;42(1):134–41.
128. Song S, Chen Z, Zheng Y, et al. Research progress of deep learning in intelligent identification of agricultural diseases and
insect pests. J Smart Agric. 2023;3(4):1–4.
129. Deng L, Wang Y, Han Z, Yu R. Research on insect pest image detection and recognition based on bio-inspired methods.
Biosyst Eng. 2018;169:139–48.
130. Chithambarathanu M, Jeyakumar MK. Survey on crop pest detection using deep learning and machine learning
approaches. Multimedia Tools Appl. 2023;82(27):42277–310.
131. Khanramaki M, Asli-Ardeh EA, Kozegar E. Citrus pests classification using an ensemble of deep learning models. Comput
Electron Agric. 2021;186:106192.
132. Ochieng’ V, Rwomushana I, Ong’amo G, Ndegwa P , Kamau S, Makale F, et al. Optimum flight height for the control of
desert locusts using unmanned aerial vehicles (UAV). Drones. 2023;7(4):233.
133. Hruday PJ, Kiran ABVS, Reddy VP . Horticulture robot for precision plant health management. In: 2024 10th international
conference on communication and signal processing (ICCSP) (pp. 448–452). IEEE. 2024.
134. De Baerdemaeker J, Hemming S, Polder G, Chauhan A, Petropoulou A, Rovira-Más F, Hostens I. AI n the agri-food sector:
Applications, risks and impacts. In: panel for the future of science and technology, EPRS, European parliamentary research
service. 2023.
135. Kaur L, Sharma SG. Identification of plant diseases and distinct approaches for their management. Bull Natl Res Cent.
2021;45(1):1–10. https://doi.org/10.1186/s42269-021-00627-6.
136. Wang B. Identification of crop diseases and insect pests based on deep learning. Sci Program. 2022;2022:1–10.  h t t p s : / / d o i .
o r g / 1 0 . 1 1 5 5 / 2 0 2 2 / 9 1 7 9 9 9 8     .
137. Lin TY, Goyal P , Girshick R, He K, Dollar P . Focal loss for dense object detection. IEEE Trans Pattern Anal Mach Intell.
2020;42(2):318–27. https://doi.org/10.1109/TPAMI.2018.2858826.
138. Stančić A, Vyroubal V, Slijepčević V. Classification efficiency of pretrained deep CNN models on camera trap images. J
Imaging. 2022;8(2):20. https://doi.org/10.3390/jimaging8020020.
139. Karthik R, Hariharan M, Anand S, Mathikshara P , Johnson A, Menaka R. Attention embedded residual CNN for disease
detection in tomato leaves. Appl Soft Comput. 2020;86:105933. https://doi.org/10.1016/j.asoc.2019.105933.
140. Singh V, Misra AK. Detection of plant leaf diseases using image segmentation and soft computing techniques. Inf Process
Agric. 2017;4(1):41–9. https://doi.org/10.1016/j.inpa.2016.10.005.
141. Liu J, Wang X. Plant diseases and pests detection based on deep learning: a review. Plant Methods. 2021;17(1):1–18.
https://doi.org/10.1186/s13007-021-00722-9.
142. Ullah A, Muhammad K, Haq IU, Baik SW. Action recognition using optimized deep autoencoder and CNN for surveillance
data streams of nonstationary environments. Future Gener Comput Syst. 2019;96:386–97.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . f u t u r e .
2 0 1 9 . 0 1 . 0 2 9     .
143. Partela V, Nunesa L, Stanslyb P , Ampatzidisa Y. Automated vision-based system for monitoring Asian citrus psyllid in
orchards utilizing AI. Comput Electron Agric. 2019;162:328–36.
144. Zhang H, Ren G. Intelligent leaf disease diagnosis: image algorithms using Swin Transformer and federated learning. Vis
Comput. 2024;41:1–24.

Page 37 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
145. Selvaraj MG, Vergara A, Ruiz H, Safari N, Elayabalan S, Ocimati W, et al. AI powered banana diseases and pest detection.
Plant Methods. 2019;15:92. https://doi.org/10.1186/s13007-019-0475-z.
146. Almadhoun HR, Abu-Naser SS. Banana knowledge-based system diagnosis and treatment. Int J Acad Pedagog Res.
2018;2(7):1–11.
147. Shawwa MA, Naser SSA. Knowledge based system for diagnosing pineapple diseases. Int J Acad Pedagog Res.
2018;2(7):12–9.
148. Jia W, Liang G, Tian H, Sun J, Wan C. Electronic nose-based technique for rapid detection and recognition of moldy apples.
Sensors. 2019;19:1526. https://doi.org/10.3390/s19071526.
149. Javidan SM, Banakar A, Vakilian KA, Ampatzidis Y. Diagnosis of grape leaf diseases using automatic K-means clustering and
machine learning. Smart Agric Technol. 2023;3:100081.
150. Rani R. Efficient citrus disease classification using a fine-tuned MobileNetV2 Model for sustainable agriculture. In: 2025 6th
international conference on mobile computing and sustainable informatics (ICMCSI) (pp. 1375–1379). IEEE. 2025.
151. Farooq F, Muneer MH, Babar M, Zahid F. Smart ground robot for real-time detection of tomato diseases using deep learn-
ing and IoT technologies. ICCK Trans Sens Commun Control. 2025;2(2):66–74.
152. Zhao P , Yang H, Sun Y, Zhang J, Gao K, Wu J, et al. Targeted MYC2 stabilization confers citrus Huanglongbing resistance.
Science. 2025;388(6743):191–8.
153. Sharada K, Choudhary SL, Harikrishna T, Dixit RS, Suman SK, Ayyappa Chakravarthi M, et al. GeoAgriGuard: AI-driven pest
and disease management with remote sensing for global food security. Remote Sens Earth Syst Sci. 2025.  h t t p s : / / d o i . o r g /
1 0 . 1 0 0 7 / s 4 1 9 7 6 - 0 2 5 - 0 0 1 9 2 - w     .
154. Guo L, Zhao G, Xu JR, Kistler HC, Gao L, Ma LJ. Compartmentalized gene regulatory network of the pathogenic fungus
Fusarium graminearum. New Phytol. 2016;211(2):527.
155. Liu B, Zhang Y, He D, Li Y. Identification of apple leaf diseases based on deep convolutional neural networks. Symmetry.
2017;10(1):11.
156. Sperschneider J, Dodds PN, Singh KB, Taylor JM. ApoplastP: prediction of effectors and plant proteins in the apoplast using
machine learning. New Phytol. 2018;217(4):1764–78.
157. Xue L, Tang B, Chen W, Luo J. DeepT3: deep convolutional neural networks accurately identify Gram-negative bacterial
type III secreted effectors using the N-terminal sequence. Bioinformatics. 2019;35(12):2051–7.
158. Saini AK, Bhatnagar R, Srivastava DK. AI based automatic detection of citrus fruit and leaves diseases using deep neural
network model. J Discrete Math Sci Cryptogr. 2021;24(8):2181–93.
159. Mensah PK, Akoto-Adjepong V, Adu K, Ayidzoe MA, Bediako EA, Nyarko-Boateng O, et al. CCMT: Dataset for crop pest and
disease detection. Data Brief. 2023;49:109306.
160. Mohammed M, El-Shafie H, Munir M. Development and validation of innovative machine learning models for predicting
date palm mite infestation on fruits. Agronomy. 2023;13(2):494.
161. Chakrabarty S, Deb CK, Marwaha S, Haque MA, Kamil D, Bheemanahalli R, et al. Application of artificial intelligence in
insect pest identification-A review. Artif Intell Agric. 2025;16:44–61.
162. Biradar N, Hosalli G. Segmentation and detection of crop pests usingnove lU-Net with hybrid deep learning mechanism.
Pest Manag Sci. 2024;80(8):3795–807. https://doi.org/10.1002/ps.8083.
163. Yuan H, Zhu J, Wang Q, Cheng M, Cai Z. An improved deeplab v3+ deep learning network applied to the segmentation of
grape leaf black rot spots. Front Plant Sci. 2022;13:795410.
164. Kasinathan T, Uyyala SR. Detection of fall armyworm (Spodoptera frugiperda) in field crops based on mask R-CNN. Signal
Image Video Process. 2023;17(6):2689–95.
165. Wu X, Liu Y, Xing M, Yang C, Hong S. Image segmentation for pest detection of crop leaves by improvement of regional
convolutional neural network. Sci Rep. 2024;14(1):24160. https://doi.org/10.1038/s41598-024-75391-4.
166. Ong SQ, Hamid SA. Next generation insect taxonomic classification by comparing different deep learning algorithms.
PLoS ONE. 2022;17(12):e0279094.
167. Valan M, Makonyi K, Maki A, Vondraček D, Ronquist F. Automated taxonomic identification of insects with expert-level
accuracy using effective feature transfer from convolutional networks. Syst Biol. 2019;68(6):876–95.  h t t p s : / / d o i . o r g / 1 0 . 1 0 9 3
/ s y s b i o / s y z 0 1 4     .
168. Ozdemir D, Kunduraci MS. Comparison of deep learning techniques for classification of the insects in order level with
mobile software application. IEEE Access. 2022;10:35675–84.
169. Lytle DA, Martınez-Muñoz G, Zhang W, Larios N, Shapiro L, Paasch R, et al. (2010) Automated processing and identification
of benthic invertebrate samples. J N Am Benthol Soc. 2010;29(3):867–74.
170. Ong BT, Sugiura K, Zettsu K. Dynamic pre-training of deep recurrent neural networks for predicting environmental moni-
toring data. In2014 IEEE International Conference on Big Data (Big Data) 2014 (pp. 760–765). IEEE.
171. Alfarisy AA, Chen Q, Guo M. Deep learning-based classification for paddy pests & diseases recognition. In: Proceedings of
2018 international conference on mathematics and artificial intelligence 2018 (pp. 21–25).
172. Khan MK, Ullah MO. Deep transfer learning inspired automatic insect pest recognition. In: proceedings of the 3rd inter-
national conference on computational sciences and technologies (pp. 17–19). Jamshoro, Pakistan: Mehran University of
Engineering and Technology. 2022.
173. Boissard P , Martin V, Moisan S. A cognitive vision approach to early pest detection in greenhouse crops. Comput Electron
Agric. 2008;62(2):81–93.
174. EFOS Ltd, 2024. Trapview, https://trapview.com/, Accessed on: 17/ 05/2024.
175. University of Georgia, 2024. PestID, https://pestid.com.au/, Accessed on: 17/05/2024.
176. Spiesman BJ, Gratton C, Hatfield RG, Hsu WH, Jepsen S, McCornack B, et al. Assessing the potential for deep learning and
computer vision to identify bumble bee species from images. Sci Rep. 2021;11(1):7580.
177. Huang S, Zhou M, Geng G. An angle-independent Gabor-SVM insect recognition. J Chin Comput Syst.
2010;31(2010):143–6.
178. Penn State University, 2024. Plant Village, https://plantvillage.psu.edu/, Accessed on: 17/05/2024
179. FAO, 2024. PestNet., https://www.plantwise.org/pestnet, Accessed on: 17/05/2024
180. UC IPM, 2024. IPM Toolkit., https://www2.ipm.ucanr.edu/tools/, Accessed on: 17/05/2024
181. Spectrum Technologies, 2024. FieldScout GreenIndex+, https://www.specmeters.com/greenindexplus/, Accessed on:
17/05/2024.

Page 38 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
182. FieldX, 2024. FieldX Scout, https://www.fieldx.com/, Accessed on: 17/05/2024
183. Agrian, 2024. Agrian Mobile, https://www.agrian.com/, Accessed on: 17/05/2024
184. Corteva Agriscience, 2024. Crop Scouting by Encirca, https://www.encirca.com/, Accessed on: 17/05/2024.
185. Okere EE, Arendse E, Nieuwoudt H, Fawole OA, Perold WJ, Opara UL. Non-invasive methods for predicting the quality of
processed horticultural food products, with emphasis on dried powders, juices and oils: a review. Foods. 2021;10:3061.
186. Jabed MA, Murad MAA. Crop yield prediction in agriculture: a comprehensive review of machine learning and deep learn-
ing approaches, with insights for future research and sustainability. Heliyon. 2024.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  1 6 / j .  h e l i y  o n . 2 0 2  4 . e
4  0 8 3 6.
187. Sairamkumar S. Design of ANN based machine learning method for crop prediction. J Innov Image Process.
2021;3(3):223–39.
188. Häni N, Roy P , Isler V. A comparative study of fruit detection and counting methods for yield mapping in apple orchards. J
Field Robotics. 2020;37(2):263–82.
189. Alibabaei K, Gaspar PD, Lima TM. Crop yield estimation using deep learning based on climate big data and irrigation
scheduling. Energies. 2021;14(11):3004.
190. Zulkifli N, Hashim N, Harith HH, Mohamad Shukery MF, Onwude DI. Prediction of the ripening stages of papayas using
discriminant analysis and support vector machine algorithms. J Sci Food Agric. 2021;102:3266–76.
191. Sengupta S, Lee WS. Identification and determination of the number of immature green citrus fruit in a canopy under
different ambient light conditions. Biosyst Eng. 2014;117:51–61.
192. Abbas F, Afzaal H, Farooque AA, Tang S. Crop yield prediction through proximal sensing and ML algorithms. Agronomy.
2020;10:1046.
193. Braun B, Bulanon DM, Colwell J, Stutz A, Stutz J, Nogales C, Hestand T, Verhage P , Tracht T. A fruit yield prediction method
using blossom detection. In: 2018 ASABE Annual International Meeting. American Society of Agricultural and Biological
Engineers. 2018; p. 1. https://doi.org/10.13031/aim.201801542.
194. Braddock T, Roth S, Bulanon J, Allen B, Bulanon DM. Fruit yield prediction using AI. In: 2019 ASABE annual international
meeting. American Society of Agricultural and Biological Engineers. 2019. P . 1.
195. Mohmed G, Grundy S, Lotfi A, Lu C. Using AI approaches for predicting tomato growth in hydroponic systems. In: UK
Workshop on Computational Intelligence. Cham: Springer International Publishing; 2021. p. 277–87.
196. Hemming S, Zwart FD, Elings A, Petropoulou A, Righini I. Cherry tomato production in intelligent greenhouses—sensors
and AI for control of climate, irrigation, crop yield, and quality. Sensors. 2020;20(22):6430.
197. Li X, Tang W, Zhang Y, Xie Q, Zhang F, Wu R, et al. Discriminant model for field maturity of tobacco leaves based on hyper-
spectral imaging technology. Tob Sci Technol. 2022;55:17–24.
198. Zhang M, Shen M, Pu Y, Li H, Zhang B, Zhang Z, et al. Rapid identification of apple maturity based on multispectral sensor
combined with spectral shape features. Horticulturae. 2022;8:361.
199. Van Beers R, Aernouts B, León Gutiérrez L, Erkinbaev C, Rutten K, Schenk A, et al. Optimal illumination-detection distance
and detector size for predicting braeburn apple maturity from vis/nir laser reflectance measurements. Food Bioproc Tech.
2015;8:2123–36.
200. Xiong JT, Zou XJ, Peng HX, Chen WG, Lin GC. Real-time identification and picking point localization of disturbance citrus
picking. Trans Chin Soc Agric Mach. 2014;45:6.
201. Duan L, Yang F, Yan B, Shi S, Qin J. Research progress of apple production intelligent chassis and weeding and harvesting
equipment technology. Smart Agric. 2022;4:24–41.
202. Wu FY, Duan JL, Ai PY, Chen ZY, Yang Z, Zou XJ. Rachis detection and three-dimensional localization of cut off point for
vision-based banana robot. Comput Electron Agric. 2022;198:107079.
203. Kang H, Zhou H, Chen C. Visual perception and modeling for autonomous apple harvesting. IEEE Access. 2020;8:62151–63.
204. Kang H, Zhou H, Wang X, Chen C. Real-time fruit recognition and grasping estimation for robotic apple harvesting. Sen-
sors. 2020;20(19):5670.
205. Yan Z, Wu Y, Zhao W, Zhang S, Li X. Research on an Apple recognition and yield estimation model based on the fusion of
improved YOLOv11 and DeepSORT. Agriculture. 2025;15(7):765.
206. Liu S, Ampatzidis Y, Zhou C, Lee WS. AI-driven time series analysis for predicting strawberry weekly yields integrating fruit
monitoring and weather data for optimized harvest planning. Comput Electron Agric. 2025;233:110212.
207. Ma N, Wu Y, Bo Y, Yan H. Chili pepper object detection method based on improved YOLOv8n. Plants. 2024;13:2402.  h t t p s : / /
d o i . o r g / 1 0 . 3 3 9 0 / p l a n t s 1 3 1 7 2 4 0 2     .
208. Yin H, Sun Q, Ren X, et al. Development, integration, and field evaluation of an autonomous citrus-harvesting robot. J Field
Robot. 2023;40(6):1363–87.
209. Ning Z, Luo L, Ding XM, et al. Recognition of sweet peppers and planning the robotic picking sequence in high-density
orchards. Comput Electron Agric. 2022;196:106878.
210. Arad B, Balendonck J, Barth R, et al. Development of a sweet pepper harvesting robot. J Field Robot. 2020;37(6):1027–39.
211. Sun Q, Zhong M, Chai X, et al. Citrus pose estimation from an RGB image for automated harvesting. Comput Electron
Agric. 2023;211:108022.
212. Sa I, Ge Z, Dayoub F, Upcroft B, Perez T, McCool C. Deepfruits: a fruit detection system using deep neural networks. Sen-
sors. 2016;16(8):1222.
213. Altaf S, Ahmad S, Zaindin M, Soomro MW. Xbeebased WSN architecture for monitoring of banana ripening process using
knowledge-level artificial intelligent technique. Sensors. 2020;20:4033. https://doi.org/10.3390/s20144033.
214. Dutta J, Patwardhan M, Deshpande P , Karande S, Rai B. Zero-shot transfer learned generic ai models for prediction of
optimally ripe climacteric fruits. Sci Rep. 2023;13:7347.
215. Occhiuzzi C, Camera F, D’Orazio M, D’Uva N, Amendola S, Bianco GM, et al. Automatic monitoring of fruit ripening rooms
by UHF RFID sensor network and machine learning. IEEE J Radio Freq Identif. 2022;6:649–59.
216. Mputu HS, Abdel-Mawgood A, Shimada A, Sayed MS. Tomato quality classification based on transfer learning feature
extraction and machine learning algorithm classifiers. IEEE Access. 2024. https://doi.org/10.1109/ACCESS.2024.3352745.
217. Torkashvand AM, Ahmadi A, Nikravesh NL. Prediction of kiwi fruit firmness using fruit mineral nutrient concentration by
artificial neural network (ANN) and multiple linear regressions (MLR). J Integr Agric. 2017;16(7):1634–44.
218. Opara IK, Fawole OA, Kelly C, Opara UL. Quantification of on-farm pomegranate fruit postharvest losses and waste, and
implications on sustainability indicators: South African case study. Sustainability. 2021;13:5168.

Page 39 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
219. He J, Van Doorselaer L, Tempelaere A, Vignero J, Saeys W, Bosmans H, et al. Nondestructive internal disorders detection of
‘Braeburn’apple fruit by X-ray dark-field imaging and machine learning. Postharvest Biol Technol. 2024;214:112981.
220. Piedad E, Larada JI, Pojas GJ, Ferrer LVV. Postharvest classification of banana (Musa acuminata) using tier-based machine
learning. Postharvest Biol Technol. 2018;145(93–100):1–4.
221. Ireri D, Belal E, Okinda C, Makange N, Ji CA. Computer vision system for defect discrimination and grading in tomatoes
using machine learning and image processing. Artif Intell Agric. 2019;2:28–37.
222. Pathmanaban P , Gnanavel BK, Anandan SS, et al. Advancing post-harvest fruit handling through AI-based thermal imag-
ing: applications, challenges, and future trends. Discov Food. 2023;3:27. https://doi.org/10.1007/s44187-023-00068-2.
223. Kader AA. Increasing food availability by reducing postharvest losses of fresh produce. Acta Hortic. 2005;682:2169–76.
224. Opara IK, Fawole OA, Opara UL. Postharvest losses of pomegranate fruit at the packhouse and implications for sustain-
ability indicators. Sustainability. 2021;13:5187.
225. Al-Dairi M, Pathare PB, Al-Yahyai R, Opara UL. Mechanical damage of fresh produce in postharvest transportation: current
status and future prospects. Trends Food Sci Technol. 2022;124:195–207.
226. Ramos PJ, Prieto FA, Montoya EC, Oliveros CE. Automatic fruit count on coffee branches using computer vision. Comput
Electron Agric. 2017;137:9–22.
227. Pantazi XE, Tamouridou AA, Alexandridis TK, Lagopodi AL, Kontouris G, Moshou D. Detection of Silybum marianum infec-
tion with Microbotryum silybum using VNIR field spectroscopy. Comput Electron Agric. 2017;137:130–7.
228. Zhang M, Li C, Yang F. Classification of foreign matter embedded inside cotton lint using short wave infrared (SWIR) hyper-
spectral transmittance imaging. Comput Electron Agric. 2017;139:75–90.
229. Duth PS, Shashidhara BS. Banana grading using deep learning techniques. In: 2022 IEEE international conference on data
science and information system (ICDSIS). 2022.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / i c  d s i s 5  5 1 3 3 . 2  0 2 2 .  9 9 1 5 9 9 8.
230. Raghavendra S, Ganguli S, Selvan PT, Nayak MM, Chaudhury S, Espina RU, et al. Deep learning based dual channel banana
grading system using convolution neural network. J Food Qual. 2022. https://doi.org/10.1155/2022/6050284.
231. Singha C, Swain KC. Rice and potato yield prediction using AI techniques. Internet Things Anal Agric. 2022;3:185–99.
232. El Akrouchi M, Mhada M, Bayad M, Hawkesford MJ, Gérard B. Ai-based framework for early detection and segmentation of
green Citrus fruits in orchards. Smart Agric Technol. 2025. https://doi.org/10.1016/j.atech.2025.100834.
233. Li Y, Zhang K, Li J, Yang X, Wang P , Liu H. Parameter optimization and experimental study of an Apple postharvest damage-
reducing conveyor device based on airflow cushioning technology. Agriculture. 2025;15(8):860.
234. Li Z, Thomas C. Quantitative evaluation of mechanical damage to fresh fruits. Trends Food Sci Technol. 2014;35(2):138–50.
235. Han B, Zhang J, Almodfer R, Wang Y, Sun W, Bai T, et al. Research on innovative apple grading technology driven by intel-
ligent vision and machine learning. Foods. 2025;14(2):258.
236. Li J, Huang W, Tian X, Wang C, Fan S, Zhao C. Fast detection and visualization of early decay in citrus using Vis-NIR hyper-
spectral imaging. Comput Electron Agric. 2016;127:582–92.
237. Pieczywek PM, Cybulska J, Szymańska-Chargot M, Siedliska A, Zdunek A, Nosalewicz A, et al. Early detection of fungal
infection of stored apple fruit with optical sensors–Comparison of biospeckle, hyperspectral imaging and chlorophyll
fluorescence. Food Control. 2018;85:327–38.
238. Moscetti R, Saeys W, Keresztes JC, Goodarzi M, Cecchini M, Danilo M, et al. Hazelnut quality sorting using high dynamic
range short-wave infrared hyperspectral imaging. Food Bioprocess Technol. 2015;8:1593–604.
239. Rady A, Ekramirad N, Adedeji AA, Li M, Alimardani R. Hyperspectral imaging for detection of codling moth infestation in
Gold Rush apples. Postharvest Biol Technol. 2017;129:37–44.
240. Mo C, Kim G, Kim MS, Lim J, Cho H, Barnaby JY, et al. Fluorescence hyperspectral imaging technique for foreign substance
detection on fresh-cut lettuce. J Sci Food Agric. 2017;97(12):3985–93.
241. Everard CD, Kim MS, Cho H, O’Donnell CP . Hyperspectral fluorescence imaging using violet LEDs as excitation sources for
fecal matter contaminate identification on spinach leaves. J Food Meas Charact. 2016;10:56–63.
242. Gnanavel S, Manohar S, Sridhar KE, Sokkanarayanan S, Sathiyanarayanan M. Quality detection of fresh fruits and veg-
etables to improve horticulture and agro-industries. In: 2019 International Conference on contemporary Computing and
Informatics (IC3I) 2019 (pp. 268–272). IEEE.
243. Peña JM, Gutiérrez PA, Hervás-Martínez C, Six J, Plant RE, López-Granados F. Object-based image classification of summer
crops with machine learning methods. Remote Sens. 2014;6:5019–41.
244. Vazquez DV, Spetale FE, Nankar AN, Grozeva S, Rodriguez GR. Machine learning-based tomato fruit shape classification
system. Plants. 2024;13:2357. https://doi.org/10.3390/plants13172357a.
245. Yang X, Zhang R, Zhai Z, Pang Y, Jin Z. Machine learning for cultivar classification of apricots (Prunus armeniaca L.) based
on shape features. Sci Hortic. 2019;256:108524.
246. Mohd Ali M, Hashim N, Abd Aziz S, Lasekan O. Characterization of pineapple cultivars under different storage conditions
using infrared thermal imaging coupled with machine learning algorithms. Agriculture. 2022;12:1013.
247. Guimarães N, Pádua L, Sousa JJ, Bento A, Couto P . Almond cultivar identification using machine learning classifiers applied
to UAV-based multispectral data. Int J Remote Sens. 2023;44(5):1533–55.
248. Binetti G, Del Coco L, Ragone R, Zelasco S, Perri E, Montemurro C, et al. Cultivar classification of Apulian olive oils: use of
artificial neural networks for comparing NMR, NIR and mereological data. Food Chem. 2017;219:131–8.
249. Fuentes S, Hernández-Montes E, Escalona JM, Bota J, Viejo CG, Poblete-Echeverría C, et al. Automated grapevine cultivar
classification based on machine learning using leaf morpho-colorimetry, fractal dimension and near-infrared spectros-
copy parameters. Comput Electron Agric. 2018;151:311–8.
250. Osako Y, Yamane H, Lin SY, Chen PA, Tao R. Cultivar discrimination of litchi fruit images using deep learning. Sci Hortic.
2020;269:109360.
251. Krug S, Hutschenreuther T. A case study toward apple cultivar classification using deep learning. AgriEngineering.
2023;5(2):814–28.
252. Borianne P , Sarron J, Borne F, Faye E. Deep mango cultivars: cultivar detection by classification method with maximum
misidentification rate estimation. Precis Agric. 2023;24(4):1619–37.
253. Vanhees DJ, Vanderbeken M, Verlinden BE, Nicolaï B. Tomato (Solanum lycopersicum) shape classification with deep learn-
ing AI-algorithms. In: VII international conference postharvest unlimited 1396 (pp. 185–192). 2023.
254. Hasan AM, Sohel F, Diepeveen D, Laga H, Jones MG. A survey of deep learning techniques for weed detection from
images. Comput Electron Agric. 2021;184:106067.

Page 40 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
255. Marco E, Mariano C, Valerio C, Fabrizio S, Albino M. Drone and sensor technology for sustainable weed management: a
review. Chem Biol Technol Agric. 2021. https://doi.org/10.1186/s40538-021-00217-8.
256. Rai N, Zhang Y, Ram BG, Schumacher L, Yellavajjala RK, Bajwa S, et al. Applications of deep learning in precision weed
management: a review. Comput Electron Agric. 2023;206:107698. https://doi.org/10.1016/j.compag.2023.107698.
257. Parico AIB, Ahamed T. An aerial weed detection system for green onion crops using the you only look once (YOLOv3)
deep learning algorithm. Eng Agric Environ Food. 2020;13(2):42–8.
258. Khan S, Tufail M, Khan MT, Khan ZA, Anwar S. Deep learning-based identification system of weeds and crops in strawberry
and pea fields for a precision agriculture sprayer. Precis Agric. 2021;22(6):1711–27.
259. Ong P , Teo KS, Sia CK. Uav-based weed detection in Chinese cabbage using deep learning. Smart Agric Technol.
2023;4:100181.
260. Pallottino F, Pane C, Figorilli S, Pentangelo A, Antonucci F, Costa C. Greenhouse application of light-drone imaging tech-
nology for assessing weeds severity occurring on baby-leaf red lettuce beds approaching fresh-cutting. Span J Agric Res.
2020;18(3):7.
261. Reedha R, Dericquebourg E, Canals R, Hafiane A. Transformer neural network for weed and crop classification of high-
resolution UAV images. Remote Sens. 2022;14(3):592.
262. Khan S, Tufail M, Khan MT, Khan ZA, Iqbal J, Alam M. A novel semi-supervised framework for UAV based crop/weed clas-
sification. PLoS ONE. 2021;16(5):e0251008.
263. Bah MD, Hafiane A, Canals R. Deep learning with unsupervised data labeling for weed detection in line crops in UAV
images. Remote Sens. 2018;10(11):1690.
264. Patel J, Ruparelia A, Tanwar S, Alqahtani F, Tolba A, Sharma R, et al. Deep learning-based model for detection of brinjal
weed in the era of precision agriculture. Comput Mater Continua. 2023. https://doi.org/10.32604/cmc.2023.038796.
265. López-Correa JM, Moreno H, Ribeiro A, Andújar D. Intelligent weed management based on object detection neural
networks in tomato crops. Agronomy. 2022;12(12):2953.
266. Moreno H, Gómez A, Altares-López S, Ribeiro A, Andújar D. Analysis of stable diffusion-derived fake weeds performance
for training convolutional neural networks. Comput Electron Agric. 2023;214:108324.
267. Hasan AM, Diepeveen D, Laga H, Jones MG, Sohel F. Object-level benchmark for deep learning-based detection and clas-
sification of weed species. Crop Prot. 2024;177:106561.
268. Huber J, Stuckenschmidt H. Daily retail demand forecasting using machine learning with emphasis on calendric special
days. Int J Forecast. 2020;36:1420–38.
269. Ramirez-Asis E, Bhanot A, Jagota V, Chandra B, Hossain MS, Pant K, et al. Smart logistic system for enhancing the farmer‐
customer corridor in smart agriculture sector using AI. J Food Qual. 2022;1:7486974.
270. Chola C. AI in Retail Marketing. AI for Business: An Implementation Guide Containing Practical and Industry-Specific Case
Studies, 86. 2023.
271. Kundu N, Mustafa F, Hemachandran K, Chola C. AI in Retail Marketing. In: AI for Business 2023; (pp. 86–107). Productivity
Press.
272. Venigandla K, Vemuri N, Thaneeru N, Tatikonda VM. Leveraging AI-enhanced robotic process automation for retail pricing
optimization: a comprehensive analysis. J Knowl Learn Sci Technol. 2023;2(2):361–70.
273. Valecha H, Varma A, Khare I, Sachdeva A, Goyal M. Prediction of consumer behaviour using random forest algorithm. In:
Proceedings of the 2018 5th IEEE Uttar Pradesh section international conference on electrical, electronics and computer
engineering, UPCON 2018, Gorakhpur, India, 2–4 November 2018; pp. 1–6.
274. Dairu X, Shilong Z. Machine learning model for sales forecasting by using XGBoost. In: proceedings of the 2021 IEEE inter-
national conference on consumer electronics and computer engineering, ICCECE 2021, Guangzhou, China, 15–17 January
2021; pp. 480–483.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  8 8 / 1 7  5 7 - 8 9  9 X / 7 4 0  / 1 / 0  1 2 2 0 5.
275. Swami D, Shah AD, Ray SKB. Predicting Future Sales of Retail Products Using Machine Learning. 2020.  h t t p s : / / a r x i v . o r g / p d f /
2 0 0 8 . 0 7 7 7 9 . p d f     . Accessed 2 April 2023.
276. Priyadarshi R, Panigrahi A, Routroy S, Garg GK. Demand forecasting at retail stage for selected vegetables: a performance
analysis. J Model Manag. 2019;14:1042–63.
277. Shukla M, Jharkharia S. Applicability of ARIMA models in wholesale vegetable market: an investigation. Int J Inf Syst Supply
Chain Manage (IJISSCM). 2013;6(3):105–19.
278. Arunraj NS, Ahrens D. A hybrid seasonal autoregressive integrated moving average and quantile regression for daily food
sales forecasting. Int J Prod Econ. 2015;170:321–35.
279. Yaiprasert C, Hidayanto AN. AI-driven ensemble three machine learning to enhance digital marketing strategies in the
food delivery business. Intell Syst Appl. 2023;18:200235.
280. Vilas-Boas JL, Rodrigues JJ, Alberti AM. Convergence of distributed ledger technologies with digital twins, IoT, and AI for
fresh food logistics: challenges and opportunities. J Ind Inf Integr. 2023;31:100393.
281. Tian F. An agri-food supply chain traceability system for China based on RFID & blockchain technology. In: 2016 13th
international conference on service systems and service management (ICSSSM) 2016; (pp. 1–6). IEEE.
282. Tian F. A supply chain traceability system for food safety based on HACCP , blockchain & Internet of things. In: 2017 Interna-
tional conference on service systems and service management 2017; (pp. 1–6). IEEE.
283. Lucena P , Binotto AP , Momo FDS, Kim H. A case study for grain quality assurance tracking based on a Blockchain business
network. arXiv preprint arXiv:1803.07877. 2018.
284. Sharma K, Kumar R, Kumar A, et al. A digital ecosystem for sustainable fruit supply chain in Uttarakhand: a comprehensive
review. Environ Dev Sustain. 2024;26:13217–52. https://doi.org/10.1007/s10668-023-04142-8.
285. Cheng M, Shen B, Chan HL. Implementing artificial intelligence consumer experience tools in supply chains. IEEE Trans
Eng Manag. 2025. https://doi.org/10.1109/TEM.2024.3525412.
286. Albahri AS, Khaleel YL, Habeeb MA, Ismael RD, Hameed QA, Deveci M, et al. A systematic review of trustworthy AI applica-
tions in natural disasters. Comput Electr Eng. 2024;118:109409.
287. Ogie RI, Rho JC, Clarke RJ. AI in disaster risk communication: a systematic literature review. In: 2018 5th international
conference on information and communication technologies for disaster management (ICT-DM) 2018; (pp. 1–8). IEEE.
288. Ogie RI, Verstaevel N. Disaster informatics: an overview. Prog Disaster Sci. 2020;7:100111.
289. UN. Sendai framework for disaster risk reduction 2015–2030. In: United Nations. 2015.

Page 41 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
290. FAO. The impact of natural hazards and disasters on agriculture and food security and nutrition: a call for action to build
resilient livelihoods. In: FAO report (issue May). http://www.fao.org/3/a-i4434e.pdf. 2015.
291. Zhang Y, Hao Z, Feng S, Zhang X, Xu Y, Hao F. Agricultural drought prediction in China based on drought propagation and
large-scale drivers. Agric Water Manag. 2021;255:107028. https://doi.org/10.1016/j.agwat.2021.107028.
292. Saha S, Gogoi P , Gayen A, Chandra G. Constructing the machine learning techniques based spatial drought vulnerability
index in Karnataka state of India. J Clean Prod. 2021;314:128073.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  1 6 / j .  j c l e p  r o . 2 0 2  1 . 1 2  8 0 7 3.
293. Guha S, Jana RK, Sanyal MK. Artificial neural network approaches for disaster management: a literature review. Int J Disas-
ter Risk Reduct. 2022;81:103276.
294. Akhyar A, Zulkifley MA, Lee J, Song T, Han J, Cho C, et al. Deep artificial intelligence applications for natural disaster man-
agement systems: a methodological review. Ecol Indic. 2024;163:112067.
295. Chaudhary MT, Piracha A. Natural disasters origins, impacts, management. Encyclopedia. 2021;1(4):1101–31.  h t t p s : / / d o i . o r
g / 1 0 . 3 3 9 0 / e n c y c l o p e d i a 1 0 4 0 0 8 4     .
296. Muhadi NA, Abdullah AF, Bejo SK, Mahadi MR, Mijic A. Deep learning semantic segmentation for water level estimation
using surveillance camera. Appl Sci. 2021. https://doi.org/10.3390/app11209691.
297. Safavi F, Rahnemoonfar M. Comparative study of real-time semantic segmentation networks in aerial images during flood-
ing events. IEEE J Sel Top Appl Earth Observ Remote Sens. 2023;16:15–31. https://doi.org/10.1109/JSTARS.2022.3219724.
298. Wilhelm RC, van Es HM, Buckley DH. Predicting measures of soil health using the microbiome and supervised machine
learning. Soil Biol Biochem. 2022;164:108472.
299. Senanayake S, Pradhan B, Wedathanthirige H. Spatial intelligence in AI applications for assessing soil health to monitor
farming systems and associated ESG risk. In: Intelligence Systems for Earth Environmental and Planetary Sciences. Amster-
dam: Elsevier; 2024. p. 81–111.
300. Padhiary M, Hoque A, Prasad G, Kumar K, Sahu B. Precision agriculture and ai-driven resource optimization for sustainable
land and resource management. In: Smart water technology for sustainable management in modern cities. Hershey: IGI
Global Scientific Publishing; 2025. p. 197–232.
301. Gayathri P , Muthumanickam D, Pazhanivelan S, Kumaraperumal R, Kannan P , Prabu PC. Emerging trends in AI-based soil
health assessment: a review. Plant Sci Today. 2025;12(3):1–14. https://doi.org/10.14719/pst.6669.
302. Nadporozhskaya M, Kovsh N, Paolesse R, Lvova L. Recent advances in chemical sensors for soil analysis: a review. Chemo-
sensors. 2022;10(1):35. https://doi.org/10.3390/chemosensors10010035.
303. Naresh R, Chandra MS, Vivek S, Charankumar G, Chaitanya J, Alam MS, et al. The prospect of artificial intelligence
(AI) in precision agriculture for farming systems productivity in sub-tropical India: a review. Curr J Appl Sci Technol.
2020;39(48):96–110.  h t t p s :  / / d o i  . o r g / 1  0 . 9 7  3 4 / c j  a s t / 2  0 2 0 / v 3  9 i 4 8  3 1 2 0 5.
304. Naveed M, Zahid N, Fatima I, Saleem A, Majeed M, Abid A, et al. Sustainable AI-driven applications for plant care and
treatment. In: Khamparia A, Pandey B, Pandey DK, Gupta D, editors., et al., Microbial data intelligence and computational
techniques for sustainable computing. Singapore: Springer Nature; 2024. p. 235–58.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 9 8 1 - 9 9 - 9
6 2 1 - 6 _ 1 6     .
305. Kouadio L, Deo RC, Byrareddy V, Adamowski JF, Mushtaq S. AI approach for the prediction of Robusta coffee yield using
soil fertility properties. Comput Electron Agric. 2018;155:324–38.
306. Ghosh D, Anand A, Gautam SS, Vidyarthi A. Soil fertility monitoring with internet of underground things: a survey. IEEE
Micro. 2021;42(1):8–16.
307. Nalwanga R, Nsenga J, Rushingabigwi G, Gatare I. Design of an embedded machine learning based system for an environ-
mental-friendly crop prediction using a sustainable soil fertility management. In: 2021 IEEE 19th Student Conference on
Research and Development (SCOReD) 2021; pp. 251–256. IEEE.
308. Sujatha M, Jaidhar CD. Machine learning-based approaches to enhance the soil fertility—a review. Expert Syst Appl,
122557. 2023.
309. Raza I, Zubair M, Zaib M, Khalil MH, Haidar A, Sikandar A, Ashfaq MA. Precision nutrient application techniques to improve
soil fertility and crop yield: A review with future prospect. Int Res J Edu Tecnol. 2023.
310. Jia X, Fang Y, Hu B, Yu B, Zhou Y. Development of soil fertility index using machine learning and visible-near-infrared spec-
troscopy. Land. 2023;12(12):2155.
311. Varshitha DN, Choudhary S. An AI solution for soil fertility and crop friendliness detection and monitoring. Int J Eng Adv
Technol. 2021;10(3):172–5.
312. Palaniappan S, Nisha SP , Kumar MM, Sreehari K, Swasthik VK. Prediction of soil properties using image processing with
ANN (Artificial Neural Network) for crop cultivation. Indian J Nat Sci. 2019;9(53):17299–308.
313. Bhattacharya S, Pandey M. Deploying an energy efficient, secure & high-speed sidechain-based TinyML model for soil
quality monitoring and management in agriculture. Expert Syst Appl. 2024;242:122735.
314. Jimenez AF, Herrera EF, Ortiz BV, Ruiz A, Cardenas PF. Inference system for irrigation scheduling with an intelligent agent.
In: advances in information and communication technologies for adapting agriculture to climate change II. AACC 2018.
Adv. Intell. Syst. Comput., vol 893. Springer, Cham, 2019; pp. 1–20.
315. Jimenez AF, Cardenas PF, Canales A, Jimenez F, Portacio A. A survey on intelligent agents and multi-agents for irrigation
scheduling. Comput Electron Agric. 2020;176:105474.
316. Jimenez AF, Cardenas PF, Jimenez F, Ruiz-Canales A, López A. A cyber-physical intelligent agent for irrigation scheduling in
horticultural crops. Comput Electron Agric. 2020;178:105777.
317. Dukes MD, Shedd M, Cardenas-Lailhacar B. Smart irrigation controllers: How do soil moisture sensor (SMS) irrigation
controllers work? 2009; pp. 1–5. IFAS Extension.
318. Quails RJ, Scott JM, DeOreo WB. Soil moisture sensors for urban landscape irrigation: Effectiveness and reliability. J Am
Water Resour Assoc. 2001;37(3):547–59.
319. Yong W, Shuaishuai L, Li L, Minzan L, Ming L, Arvanitis KG, et al. Smart sensors from ground to cloud and web intelligence.
IFAC-PapersOnLine. 2018;51(17):31–8.
320. Gebregiorgis MF, Savage MJ. Determination of the timing and amount of irrigation of winter cover crops with the use of
dielectric constant and capacitance soil water content profile methods. S Afr J Plant Soil. 2006;23(3):145–51.
321. Kuyper MC, Balendonck J. Application of dielectric soil moisture sensors for real-time automated irrigation control. Acta
Hortic. 2001;562:71–9.

Page 42 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
322. Xing Z, Zheng W, Shen C, Yang Q, Sun G. The measurement of soil water content using the dielectric method. In: 2010
World automation congress, WAC 2010 2010; pp. 241–245.
323. Kumar G. Research paper on water irrigation by using wireless sensor network. Int J Sci Eng Technol, IEERT conference
Paper, 2014; pp. 123–125.
324. Shekhar Y, Dagur E, Mishra S, Tom RJ, Veeramanikandan M, Sankaranarayanan S. Intelligent IoT based automated irrigation
system. Int J Appl Eng Res. 2017;12(18):7306–20.
325. Savitha M, UmaMaheshwari OP . Smart crop field irrigation in IOT architecture using sensors. Int J Adv Res Comput Sci.
2018;9(1):302–6.
326. Viani F, Bertolli M, Salucci M, Polo A. Low-cost wireless monitoring and decision support for water saving in agriculture.
IEEE Sens J. 2017;17:4299–309.
327. Prasanna Lakshmi GS, Asha PN, Sandhya G, Vivek Sharma S, Shilpashree S, Subramanya SG. An intelligent IOT sensor
coupled precision irrigation model for agriculture. Measure Sens. 2023;25:100608.
328. Dong X, Vuran MC, Irmak S. Autonomous precision agriculture through integration of wireless underground sensor
networks with center pivot irrigation systems. Ad Hoc Netw. 2013;11:1975–87.
329. Varatharajalu K, Ramprabu J. Wireless irrigation system via phone call & SMS. Int J Eng Adv Technol. 2018;8(2S):397–401.
330. Rad CR, Hancu O, Takacs IA, Olteanu G. Smart monitoring of potato crop: a cyber-physical system architecture model in
the field of precision agriculture. Agric Agric Sci Procedia. 2015;6:73–9.
331. Seshia SA, Hu S, Li W, Zhu Q. Design automation of cyber-physical systems: challenges, advances, and opportunities. IEEE
Trans Comput Aided Des Integr Circ Syst. 2016;36(9):1421–34.
332. Preite L, Vignali G. AI to optimize water consumption in agriculture: a predictive algorithm-based irrigation management
system. Comput Electron Agric. 2024;223:109126.
333. Mokhtar A, Al-Ansari N, El-Ssawy W, Graf R, Aghelpour P , He H, et al. Prediction of irrigation water requirements for green
beans-based machine learning algorithm models in arid region. Water Resour Manage. 2023;37(4):1557–80.
334. Srivastava S, Kumar N, Malakar A, Sruti, Choudhury D, Ray C, et al. A machine learning-based probabilistic approach for
irrigation scheduling. Water Resour Manage. 2024. https://doi.org/10.1007/s11269-024-03746-7.
335. Keswani B, Mohapatra AG, Mohanty A, Khanna A, Rodrigues JJPC, Gupta D, et al. Adaptingweather conditions based IoT
enabled smart irrigation technique in precision agriculture mechanisms. Neural Comput Appl. 2019;31:277–92.
336. Sapkota R, Ahmed D, Karkee M. Comparing YOLOv8 and Mask R-CNN for instance segmentation in complex orchard
environments. AI Agric. 2024;13:84–99.
337. Sitharthan R, Rajesh M, Vimal S, Saravana E, Yuvaraj S, Abhishek K, et al. A novel autonomous irrigation system for smart
agriculture using AI and 6G enabled IoT network. Microprocess Microsyst. 2023;101:104905.
338. King BA, Shellie KC. A crop water stress index based internet of things decision support system for precision irrigation of
wine grape. Smart Agric Technol. 2023;4:100202.
339. Nawandar NK, Satpute VR. IoT based low cost and intelligent module for smart irrigation system. Comput Electron Agric.
2019;162:979–90.
340. Berrú-Ayala J, Hernandez-Rojas D, Morocho-Díaz P , Novillo-Vicuña J, Mazon-Olivo B, Pan A. SCADA system based on IoT
for intelligent control of banana crop irrigation. In: international conference on applied technologies 2019; pp. 243–256.
Cham: Springer International Publishing.
341. Arora AS, Yun CM. AI-based irrigation control and pest/disease prediction for open-field pineapple farm. Korean Soc Hortic
Sci Acad Present Summ, 130–131. 2022.
342. Singh D, Biswal AK, Samanta D, Singh V, Kadry S, Khan A, et al. Smart high-yield tomato cultivation: precision irrigation
system using the Internet of Things. Front Plant Sci. 2023;14:1239594.
343. Kasera RK, Acharjee T. A comprehensive IoT edge based smart irrigation system for tomato cultivation. Internet Things.
2024. https://doi.org/10.1016/j.iot.2024.101356.
344. Chandu E, Shukla MK. IoT-based smart irrigation system for mango orchard. In: AI and Machine Learning in Satellite Data
Processing and Services: Proceedings of the International Conference on Small Satellites, ICSS 2022 2023; pp. 61–69.
Singapore: Springer Nature Singapore.
345. Gour S, Kasera RK, Singh WN, Acharjee T. Low cost IoT based smart irrigation system for potato cultivation. In: 2023 IEEE
Guwahati Subsection Conference (GCON) 2023; pp. 01–06. IEEE.
346. Abd Halim AA, Mohamad R, Rahman FYA, Harun H, Anas NM. IoT based smart irrigation, control, and monitoring system
for chilli plants using NodeMCU-ESP8266. Bull Electr Eng Inform. 2023;12(5):3053–60.
347. Kumar V, Singh CD, Rao KR, Rajwade YA, Kumar M, Asha KR. Development and evaluation of smart drip irrigation system
for egg plant using internet of things: smart drip irrigation for egg plant. J Sci Ind Res (JSIR). 2024;83(3):300–8.
348. Boumehrez F, Sahour A, Bekhouche A, Maamri F, Djellab H. Smart irrigation system for orchards apple trees based on fuzzy
logic and WSNs. In: 2024 IEEE International Conference on Advanced Systems and Emergent Technologies (IC_ASET) 2024;
pp. 1–6. IEEE.
349. Quisphe MWV, Moreano JAC, Chisag JCC. AI: prototype of an automated irrigation system for the cultivation of roses in
Cotopaxi. Data and Metadata. 2024;3:398–398.
350. Oğuztürk GE, Murat C, Yurtseven M, Oğuztürk T. The effects of AI-supported autonomous irrigation systems on water
efficiency and plant quality: a case study of Geranium psilostemon Ledeb. Plants. 2025;14(5):770.
351. Liu D. Application of modern urban landscape design based on machine learning model to generate plant landscaping.
Sci Program. 2022;2022(1):1610427.
352. Wani MA, Din A, Nazki IT, Rehman TU, Al-Khayri JM, Jain SM, et al. Navigating the future: exploring technological advance-
ments and emerging trends in the sustainable ornamental industry. Front Environ Sci. 2023;11:1188643.  h t t p s : / / d o i . o r g / 1 0
. 3 3 8 9 / f e n v s . 2 0 2 3 . 1 1 8 8 6 4 3     .
353. Hussein MYA, AL-Karablieh M, Al-Kfouf S, Taani M. Machine learning-driven sustainable urban design: transforming Singa-
pore’s landscape with vertical greenery. Asian J Civ Eng. 2024. https://doi.org/10.1007/s42107-024-01016-w.
354. Wang B, Ding Y, Wang C, Li D, Wang H, Bie Z, et al. G-ROBOT: an intelligent greenhouse seedling height inspection robot. J
Robot. 2022. https://doi.org/10.1155/2022/.
355. Naik PM, Rudra B. Flower phenotype recognition and analysis using YoloV5 models. In: proceedings of the 13th interna-
tional conference on advances in computing, control, and telecommunication technologies, ACT 2022, Hyderabad, India,
27–28 June 2022; pp. 838–848.

Page 43 of 43
Chaudhary et al. Discover Plants           (2025) 2:372
356. Srivastava DK, Jha DN. Hibiscus flower health detection to produce oil using convolution neural network. In: proceedings
of the 2022 international conference on advancements in smart, secure and intelligent computing (ASSIC), Bhubaneswar,
India, 19–20 November 2022; Institute of Electrical and Electronics Engineers Inc.: Piscataway, NJ, USA, 2022; pp. 1–5.
357. Wang G, Sun Y, Wang J. Automatic image-based plant disease severity estimation using deep learning. Comput Intell
Neurosci. 2017;2017:1–8. https://doi.org/10.1155/2017/2917536.
358. Kwon HS, Heo S. Classification of vase life day based on petal colorimetric data in cut Lisianthus using AutoML. Horticul-
turae. 2024;10(10):1033.
359. Kwon HS, Heo S. Predicting vase life of cut Lisianthus based on biomass-related characteristics using AutoML. Agriculture.
2024;14(9):1543.
360. Fryda T, LeDell E, Gill N, Aiello S, Fu A, Candel A, Click C, Kraljevic T, Nykodym T, Aboyoun P . et al. H2O: R Interface for the
‘H2O’ SCALABLE Machine Learning Platform. R Package Version 3.40.0.4. 2023. 2024;  h t t p s : / / C R A N . R - p r o j e c t . o r g / p a c k a g e = h
2 o     . Accessed 10 July 2024.
361. Herrera D, Escudero-Villa P , Cárdenas E, Ortiz M, Varela-Aldás J. Combining image classification and unmanned aerial
vehicles to estimate the state of explorer roses. Agri Eng. 2024;6(2):1008–21.
362. Zawbaa HM, Abbass M, Basha SH, Hazman M, Hassenian AE. An automatic flower classification approach using machine
learning algorithms. In: 2014 international conference on advances in computing, communications and informatics
(ICACCI) 2014; pp. 895–901. IEEE.
363. Tian M, Chen H, Wang Q. Flower identification based on deep learning. J Phys Conf Ser. 2019;1237(2):022060.
364. Mao Z, Zhong T, Wei M, Hu R, Liu J. RCSnet——flower classification network design based on transfer learning and chan-
nel attention mechanism. In: international conference on intelligent computing 2024; pp. 48–59. Singapore: Springer
Nature Singapore.
365. Bhuria R Feature extraction and classification performance of fine-tuned ResNet-50 in plant species recognition. In: 2024
2nd international conference on advances in computation, communication and information technology (ICAICCIT) (Vol.
1, pp. 574–579). 2024. IEEE.
366. Zheng Y, Lin W. Research on flower classification technology based on VGG16 neural network. In: fourth international con-
ference on electronic information engineering and data processing (EIEDP 2025) (Vol. 13574, pp. 1181–1186). SPIE. 2025.
367. Chen Y, Li Y. Intelligent autonomous pollination for future farming-a micro air vehicle conceptual framework with AI and
human- in-the-loop. IEEE Access. 2016;4:2–13.
368. Xu Y, Liu S. Botanical-based simulation of color change in fruit ripening: taking tomato as an example. Comput Anim
Virtual Worlds. 2024;35(1):e2225.
369. Cassity ME, Bartley PC, Bao Y. Root segmentation of horticultural plants in X-ray CT images by integrating 2D instance
segmentation with 3D point cloud clustering. Smart Agric Technol. 2024. https://doi.org/10.1016/j.atech.2024.100666.
370. Sharma A, Sharma A, Tselykh A, Bozhenyuk A, Choudhury T, Alomar MA, et al. AI and internet of things oriented sustain-
able precision farming: towards modern agriculture. Open Life Sci. 2023;18(1):20220713.
371. Gryshova I, Balian A, Antonik I, Miniailo V, Nehodenko V, Nyzhnychenko Y. AI in climate smart in agricultural: toward a
sustainable farming future. Access Sci Bus Innov Digital Econ. 2024;5(1):125–40.
372. Karunathilake EMBM, Le AT, Heo S, Chung YS, Mansoor S. The path to smart farming: innovations and opportunities in
precision agriculture. Agriculture. 2023;13(8):1593.
373. Adewusi AO, Asuzu OF, Olorunsogo T, Iwuanyanwu C, Adaga E, Daraojimba DO. AI in precision agriculture: a review of
technologies for sustainable farming practices. World J Adv Res Rev. 2024;21(1):2276–85.
374. Monchusi BB, Kgopa AT, Mokwana TI. Integrating IoT and AI for precision agriculture: enhancing water management and
crop monitoring in small-scale farms. In: international conference on intelligent and innovative computing applica-
tions 2024; pp. 151–158.
375. Alatawi T, Aljuhani A. Anomaly detection framework in fog-to-things communication for industrial internet of things.
Comput Mater Contin. 2022;73(1):1067–86. https://doi.org/10.32604/cmc.2022.029283.
376. Petrovic B, Kononets Y, Csambalik L. Adoption of drone, sensor, and robotic technologies in organic farming systems of
Visegrad countries. Heliyon. 2025.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  1 6 / j .  h e l i y  o n . 2 0 2  4 . e 4  1 4 0 8.
377. Atapattu AJ, Perera LK, Nuwarapaksha TD, Udumann SS, Dissanayaka NS. Challenges in achieving artificial intelligence in
agriculture. In: Artificial intelligence techniques in smart agriculture 2024; pp. 7–34. Singapore: Springer Nature Singapore.
378. Tan Y, Liu X, Zhang J, Wang Y, Hu Y. A review of research on fruit and vegetable picking robots based on deep learning.
Sensors (Basel). 2025;25(12):3677.
379. Spagnuolo M, Todde G, Caria M, Furnitto N, Schillaci G, Failla S. Agricultural robotics: a technical review addressing chal-
lenges in sustainable crop production. Robotics (Basel). 2025;14(2):9.
380. Dahane A, Benameur R, Kechar B. An innovative smart and sustainable low-cost irrigation system for smallholder farmers'
communities. In: 2022 3rd International Conference on Embedded & Distributed Systems (EDiS) 2022; pp. 37–42. IEEE.
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
