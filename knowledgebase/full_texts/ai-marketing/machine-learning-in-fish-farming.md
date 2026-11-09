---
title: Machine Learning in Fish Farming
url: https://arxiv.org/abs/2609.13919
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Fearghal O'Donncha
- Nikos Papandroulakis
- Jennie Korus
- Abigail Langbridge
- Alexander Timms
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.13919
pages: 42
chars: 133252
fetched_at: '2026-11-08T13:29:49+00:00'
kb_version: 1
---

# Machine Learning in Fish Farming

Machine Learning in Fish Farming
Fearghal O’Donncha1, Nikos Papandroulakis2, Jennie Korus3, Abigail Langbridge4,
Alexander Timms4, Konstantinos Topouzelis5, Abdul Baseer Khan6, Shree Rama Kamal
Kumar Vegu6, Mahtab Sarvmaili6, Ryan Mowat7, Rhanna Turberville8, Tyler Sclodnick3,
and Christopher Whidden6,9
1IBM Research Europe, Dublin, Ireland
2Hellenic Centre for Marine Research, Crete, Greece
3Innovasea Marine Systems Canada, Nova Scotia, Canada
4Imperial College London, United Kingdom
5University of the Aegean, Greece
6Dalhousie University, Halifax, Nova Scotia, Canada
7RS Aqua, Portsmouth, United Kingdom
8Scottish Sea Farms, Orkney, United Kingdom
9DeepSense, Nova Scotia, Canada
Preprint notice.This is a preprint of the following chapter: Fearghal O’Donncha, Nikos
Papandroulakis, Jennie Korus, Abigail Langbridge, Alexander Timms, Konstantinos Topouzelis,
Abdul Baseer Khan, Shree Rama Kamal Kumar Vegu, Mahtab Sarvmaili, Ryan Mowat, Rhanna
Turberville, Tyler Sclodnick and Christopher Whidden, “Machine Learning in Fish Farming,”
published inDigital Twin for Marine Fish Farming, edited by Fearghal O’Donncha, Martin Føre
and Jon Grant, 2026, Springer, reproduced with permission of Springer. The final authenticated
version is available online at:https://doi.org/10.1007/978-3-032-10362-8_3.
Abstract
Thischapterexploreshowmachinelearning(ML)istransformingaquaculture,withaparticular
focus on enhancing decision-making processes and improving operational efficiency. The chapter
is structured to first introduce the challenges in aquaculture and the role of AI, then provide an
overview of ML techniques in the context of aquaculture, followed by applications, emerging
trends, future directions, and case studies. The focus is on real-world applications of ML
techniques, including Random Forest, Convolutional Neural Networks (CNNs), and Recurrent
Neural Networks (RNNs), as well as emerging technologies such as Graph Neural Networks
(GNNs) and transformer-based models. Key applications include biomass estimation, species
recognition, behavioural analysis, and environmental forecasting. The chapter also highlights
the synergy between ML and the Internet of Things (IoT) for real-time monitoring and decision
support. Ultimately, ML-driven innovations have the potential to revolutionize fish farming,
leading to more efficient, sustainable, and productive practices in the aquaculture industry.
Keywords:Machine learning; artificial intelligence; aquaculture; large language models; foundation
models; digital twin
1 Introduction
Aquaculture has emerged as a critical component of global food security, supplying nearly 50% of
the world’s fish consumption. It is recognized as one of the fastest-growing food production sectors,
1
arXiv:2609.13919v1  [cs.LG]  12 Sep 2026

contributing significantly to the supply of high-quality protein, particularly in regions where access to
such food sources is limited [Naylor et al., 2021, Béné et al., 2016]. As global demand for seafood
continues to rise, the expansion of aquaculture is essential to meet these needs sustainably. However,
the industry faces multiple challenges that threaten its long-term viability.
1.1 Challenges in Aquaculture
Despite its rapid growth, aquaculture is constrained by several critical challenges that affect sustain-
ability, efficiency, and profitability.
• Environmental Concerns:The intensification of aquaculture can contribute to habitat degra-
dation, water pollution, and excessive nutrient loading, leading to issues such as harmful algal
blooms and oxygen depletion [Godfray et al., 2010].
• Disease Management:Infectious diseases pose a significant threat to fish health, resulting in
high economic losses. Disease outbreaks require improved early detection and intervention
strategies to prevent large-scale losses [Mandal and Ghosh, 2023].
• Feeding Efficiency and Resource Utilization:Feed is one of the most expensive inputs in
aquaculture, and inefficient feeding practices can lead to increased waste and production costs
. Optimizing feed conversion ratios is essential to reduce environmental impact and improve
profitability [Cooney et al., 2021].
• Labour Shortages and Supply Chain Vulnerabilities:The COVID-19 pandemic exposed
weaknesses in aquaculture operations, highlighting issues such as workforce shortages and
logistical disruptions that can impact production efficiency [Love et al., 2021].
These challenges underscore the urgent need for greater automation and data-driven approaches to
ensure efficient, sustainable, and resilient aquaculture operations [Klinger and Naylor, 2012].
1.2 The Role of Artificial Intelligence in Aquaculture
Artificial Intelligence (AI) is revolutionizing aquaculture by providing advanced analytics, automation,
andpredictivecapabilities. Machinelearning(ML),asubsetofAI,enablesdata-drivendecision-making
and enhances key aspects of aquaculture management, including:
• Optimized Feeding Strategies:AI-driven analysis of fish behaviour and biomass estimation
allows for precise feeding schedules, minimizing waste and improving growth rates.
• Early Disease Detection:ML models analyse behavioural patterns, water quality data, and
historical trends to detect early signs of disease outbreaks, allowing for timely interventions.
• Environmental Monitoring and Prediction:Predictive models improve water quality man-
agement by forecasting dissolved oxygen levels, temperature fluctuations, and harmful algal
blooms [O’Donncha and Grant, 2019].
• Automation of Farm Operations:AI-driven IoT systems enable automated monitoring of fish
health, water conditions, and infrastructure maintenance, reducing reliance on manual labour
[Mandal and Ghosh, 2023].
The integration of AI into aquaculture is not merely a technological advancement but a necessary step
toward increasing efficiency and ensuring long-term sustainability [Maksimovic, 2018].
2

1.3 Scope of This Chapter
This chapter explores the role of machine learning in aquaculture, focusing on its applications in
farm management, decision-making, and operational efficiency. Given the complexity of aquaculture,
which intersects with fields such as oceanography, environmental science, industrial automation, and
logistics, the discussion is centered on how AI-driven approaches can enhance on-farm operations.
The key question addressed is:How can the combination of human expertise and AI-based insights
lead to more effective and sustainable aquaculture practices?
The chapter is structured as follows:
•Section 2provides an overview of machine learning techniques relevant to aquaculture.
• Section 3discusses key applications, including computer vision for fish monitoring, IoT-based
environmental tracking, and predictive modelling for disease detection and feeding efficiency.
•Section 4examines emerging trends, such as Graph Neural Networks (GNNs), large language
models, and AI-integrated digital twins for aquaculture.
•Section 5presents case studies illustrating real-world AI applications in aquaculture.
•Section 6provides conclusions and outlines directions for future research.
This structured approach ensures a comprehensive exploration of machine learning in aquaculture,
highlighting its potential to drive innovation, efficiency, and sustainability in the industry.
2 Machine Learning
Research into applications of artificial intelligence (AI) and machine learning (ML) in aquaculture
and other maritime applications has accelerated at a rapid pace over the last 5 years or so. AI is
a broad field focused on creating smart machines capable of performing tasks that require human
intelligence. ML, on the other hand, is a subset of AI that specifically involves developing algorithms
that allow computers to learn and make decisions from data. In essence, while AI encompasses a wide
range of technologies mimicking human abilities, ML is a specific approach within AI that focuses on
data-driven learning and prediction.
Given access to sufficient and high-quality data, ML techniques can detect, quantify, and predict
complex phenomena relevant to aquaculture operations. While physics-based modelling involves
providing a set of inputs to a model which generates the corresponding outputs based on a non-linear
mapping encoded from a set of governing equations, supervised machine learning instead learns
the requisite mapping by being shown large number of corresponding inputs and outputs. However,
this data-driven approach is only as effective as the data it relies on—a principle often summarized
asrubbish in, rubbish out. If the training data is noisy, sparse, biased, or poorly labelled, the
resulting model will inevitably reflect those flaws, regardless of how sophisticated the algorithm
is. Thus, the selection of an appropriate ML model and its hyperparameters—external settings not
learned from data but critical to model behaviour—must be matched with careful data curation and
preprocessing. Parameters internal to the model are optimized during training, but no model can
overcome fundamentally flawed input. Data quality, therefore, is not a peripheral concern but a central
determinant of model success.
Theremarkablegrowthandsuccessofmachinelearninginrecentyearshasbeenlargelydrivenbythree
pivotal factors: the exponential increase in data volumes, significant advancements in computational
3

power, and substantial innovations in machine learning algorithms. The proliferation of data from
myriad sources such as sensors, Internet of Things (IoT) devices, and social media has provided an
unprecedented amount of raw material for machine learning models. This abundance of data enables
researchers and practitioners to train more robust and accurate models, particularly in domains like
natural language processing, image recognition, and predictive analytics.
Concurrently, there has been a dramatic enhancement in computational power, primarily due to the
advent of specialised hardware such as Graphics Processing Units (GPUs) and Tensor Processing
Units (TPUs). These advancements have drastically reduced the time required for training complex
ML models, making it feasible to process large datasets and perform more sophisticated computations.
Moreover, the evolution of machine learning algorithms, especially in the realms of deep learning
and reinforcement learning, has opened new horizons. Techniques such as convolutional neural
networks (CNNs) [O’shea and Nash, 2015], recurrent neural networks (RNNs) [Schmidt, 2019], and
transformers [Vaswani et al., 2017], have set new standards in accuracy and efficiency, pushing the
boundariesofwhatwaspreviouslyconsideredachievableinML.Thesedevelopmentshavecollectively
propelled the field into a new era of innovation and application, transforming theoretical concepts into
practical solutions across various industries.
2.1 Machine learning algorithms
Machine learning algorithms can be classified based on various criteria, each providing a different
perspective on how the algorithms function and are applied. Some of the primary ways to categorise
these algorithms include:
1.Based on Learning Style:
• Supervised Learning:Algorithms that learn from labelled training data, aiming to make
predictions or decisions. Examples include linear regression, logistic regression, support
vector machines, and neural networks.
• Unsupervised Learning:Algorithms that work with unlabelled data to find underlying
patterns or structures. Common examples are k-means clustering, hierarchical clustering,
and principal component analysis.
• Semi-Supervised Learning:These algorithms use a mix of labelled and unlabelled data,
which are useful when acquiring a fully labelled dataset is expensive or impractical.
• ReinforcementLearning:Algorithmsthatlearntomakedecisionsbyperformingactions
in an environment to achieve a goal. These algorithms learn from the feedback of their
own actions rather than from explicit teaching [Madondo et al., 2023].
2.Based on Functionality:
• Classification Algorithms:Used for tasks where the output is a discrete label. For
instance, identifying whether a fish is feeding or not.
• Regression Algorithms:Used for predicting a continuous-valued output, such as the
dissolved oxygen conditions in a cage over time.
• ClusteringAlgorithms:Aimedatgroupingsetsofsimilaritemsindata,suchasgrouping
fish based on health status.
• Dimensionality Reduction Algorithms:Used to reduce the number of features in a
dataset, either for compression or improved efficiency in subsequent tasks.
3.Based on Approach or Technique:
4

• Decision Trees:Algorithms that model decisions and possible consequences, including
chance event outcomes, resource costs, and utility.
• Bayesian Algorithms:Based on Bayes’ Theorem, these algorithms are particularly used
for classification and prediction.
• Bagging:Techniques like Random Forest that combine the results of multiple models to
improve the overall performance.
• Boosting:Methods like AdaBoost and XGBoost that sequentially build models, with each
model trying to correct the errors of its predecessor.
• Deep Learning:A subset of machine learning based on artificial neural networks with
representation learning. Deep learning can involve a high level of automation in predictive
modelling.
4.Based on Type of Data or Application:
• TextAnalysis/NaturalLanguageProcessing(NLP):Algorithmsspecialisedinprocessing
and analysing text data, like sentiment analysis or topic modelling.
• Time Series Analysis:Algorithms that are designed to analyse time-ordered data, useful
in fields like environmental science, finance, and economics.
Each classification offers a different lens through which to understand and apply machine learning
algorithms, often depending on the nature of the data and the specific problem at hand. It’s essential
for practitioners to comprehend the various strengths and limitations of different algorithms to create
an efficient experimental framework. Although deep learning has garnered widespread success in
numerous fields, it’s important to note that these approaches often require substantial amounts of data,
which may not be feasible for all scenarios. Additionally, in line with the principle of Occam’s Razor,
it’s advisable to gravitate towards the simplest approach that adequately fulfils the requirements of the
task.
2.2 Statistical and Machine Learning
Methods such as linear regressions, Random Forest, and XGBoost are well-established, robust, and
efficient methods commonly used in aquaculture. They are appealing due to their simplicity and
computational efficiency but also due to their ease of interpretability which is particularly important
for industry applications.
2.2.1 Feature Engineering
Feature engineering is a critical step in the process of developing machine learning models. It involves
selecting, modifying, or creating new features from the raw data to improve the performance of
machine learning algorithms [Guyon and Elisseeff, 2003]. The essence of feature engineering lies in
transforming raw data into a format that is more suitable and effective for regression models, such as
linear regression or support vector regression. This process not only enhances the model’s ability to
uncover underlying patterns in the data but also improves its predictive accuracy.
In the context of regression tasks, feature engineering can involve a variety of techniques. One
common approach is feature selection, where irrelevant or redundant features are removed to reduce
model complexity and avoid overfitting [Blum and Langley, 1997]. Another technique is feature
transformation, which includes normalisation or standardisation of features to bring them onto a
similar scale, or applying mathematical transformations to change the distribution of the features.
5

Moreover, feature construction is often employed, where new features are created from existing ones,
either through domain-specific knowledge or by detecting interactions between features. This can
be particularly useful in linear regression, where non-linear relationships can be linearised through
transformations, allowing the linear model to capture more complex patterns in the data [Friedman
et al., 2001]. These engineered features are then used to train the regression model, which aims to
predictacontinuousoutcomebasedontheinputfeatures,therebyprovidingmoreaccurateandreliable
predictions.
2.3 Deep Learning
Deeplearning(DL),aspecialisedsubfieldwithinML,enablestheextractionofcomplexpatternsfrom
large datasets, representing a major leap in AI capability. While machine learning employs algorithms
to parse data, learn from that data, and make informed decisions based on what it has learned, deep
learning takes this process a step further. It teaches the computer to perform tasks that come naturally
to humans: learning by example. Deep learning is a type of machine learning that trains a computer
to perform human-like tasks, such as recognising speech, identifying images, or making predictions.
Instead of organising data to run through predefined equations, deep learning sets up basic parameters
about the data and trains the computer to learn on its own by recognising patterns using layers of
processing [LeCun et al., 2015].
The key difference between deep learning and traditional machine learning lies in how the data is
presented to the system. In traditional machine learning, the algorithm requires structured data to
learn and make decisions. This involves a significant amount of manual effort to label and classify
data before it’s fed into the model. Deep learning, on the other hand, learns from raw data, employing
layers of neural networks to understand it. These neural networks, which are algorithms modelled
after the human brain, work by passing data through interconnected layers of nodes, or “neurons”.
Each layer extracts a specific feature from the data, building a hierarchy of learned features. This
hierarchical feature learning enables deep learning models to tackle complex tasks with high accuracy,
making them particularly effective for areas like image and speech recognition [Goodfellow et al.,
2016].
DL can be categorised into subfields based on the key architectures that are typically used:
1. Convolutional Neural Networks (CNNs):Specialised for processing data with a grid-like
topology, such as images. Used in image recognition, video analysis, and natural language
processing [LeCun et al., 1998].
2. Recurrent Neural Networks (RNNs):Designed to work with sequence data, like time series
or text. They have the ability to retain information over time, making them suitable for tasks
like language modeling and speech recognition [Hochreiter and Schmidhuber, 1997].
3. Long Short-Term Memory Networks (LSTMs):A type of RNN that is better at capturing
long-term dependencies, thus avoiding the vanishing gradient problem common in traditional
RNNs.
4. Autoencoders:Used for unsupervised learning tasks, particularly in dimensionality reduction
and feature learning. Autoencoders learn to compress data and then reconstruct it back [Hinton
and Salakhutdinov, 2006].
5. Generative Adversarial Networks (GANs):Consist of two networks, a generator and a
discriminator, which are trained simultaneously. GANs are used for generating new data that
resembles the training data, useful in image generation, super-resolution, and more [Goodfellow
et al., 2020].
6

6. Transformers: Initially developed for natural language processing (NLP), transformers have
emerged as a versatile and powerful architecture for handling sequential data. Unlike recurrent
models, transformers rely on a self-attention mechanism that enables them to process entire
sequences in parallel, significantly improving computational efficiency and scalability [Vaswani
et al., 2017]. This architectural shift has driven breakthroughs in tasks such as machine
translation, sentiment analysis, and text generation. More recently, transformers have been
adapted for computer vision and time-series modelling, further broadening their applicability.
Transformers underpin today’s large language models (LLMs), playing a pivotal role in the
developmentofgenerativeAIsystemsnowbeingexploredacrossaquacultureandenvironmental
domains.
The different architectures in deep learning are significant because their design and functionality make
it particularly suited for certain tasks, leading to more effective and efficient learning outcomes in
diverse applications.
These architectures can also be combined to leverage advantages of multiple methods. Combining
Convolutional Neural Networks (CNNs) with Long Short-Term Memory networks (LSTMs) harnesses
thestrengthsofbotharchitectures,creatingapowerfultoolfortasksinvolvingbothspatialandtemporal
data. CNNs are adept at extracting spatial features and hierarchical patterns in data, particularly useful
in image and video analysis. When this spatial information is extracted by a CNN, it can then be
fed into an LSTM, which is designed to handle sequential data and capture temporal dependencies.
This combination is particularly effective in video processing tasks, where it’s crucial to understand
not just individual frames (spatial information) but also the sequence and evolution of these frames
over time (temporal information) [Donahue et al., 2015]. In environmental applications, CNNs excel
in analysing spatial patterns, such as those observed in satellite imagery of ocean surfaces, while
LSTMs contribute by interpreting temporal changes and patterns over time, crucial for understanding
dynamic ocean processes like current movements, sea surface temperature changes, and algal blooms.
This combination enables a more comprehensive analysis of ocean environments, providing valuable
insights for environmental monitoring and climate studies [Chen et al., 2019].
2.3.1 Deep Learning Summary and Considerations
Deep learning, with its advanced neural network architectures, offers immense potential for both
environmental and industry applications, significantly transforming how we approach complex
problems in these domains. For aquaculture, deep learning techniques like CNN and RNN can
process vast datasets, such as satellite imagery, IoT data, and weather to extract pertinent insights for
management, conservation, and mitigation. Similarly, in operational applications, deep learning can
optimise processes in manufacturing, logistics, and predictive maintenance, enhancing efficiency and
reducing costs [Atitallah et al., 2020].
However, effectively leveraging deep learning across the myriad aspects of aquaculture necessitates
careful consideration of several key factors. The ‘data appetite’ of deep learning models is substantial,
requiring large and diverse datasets for training to achieve high accuracy, which are often difficult to
collectinindustrysettings[Goodfellowetal.,2016]. Overfittingisanothercriticalissue,wheremodels
might perform well on training data but fail to generalise to new, unseen data, necessitating techniques
like regularisation and cross-validation to mitigate this risk. Computational requirements for training
sophisticated deep learning models are also significant, often requiring specialised hardware like
GPUs, which can be a barrier in terms of resources and cost.
Lastly,thechallengeofinterpretabilityindeeplearningmodels,duetotheir‘blackbox’nature,canbea
significanthurdle, especiallyinsectorswhereunderstandingthedecision-makingprocessiscrucialfor
trust and compliance [Samek et al., 2017]. Thus, while deep learning presents exciting opportunities
7

in environmental and operational sectors, its success hinges on judicious data management, mitigating
overfitting, planning for computational resources, and advancing efforts in model interpretability.
3 Applications of Machine Learning in Aquaculture
The multifaceted nature of aquaculture, encompassing aspects such as environmental monitoring,
disease management, feeding efficiency, and yield optimization, makes it an ideal candidate for the
integration of ML techniques. The incorporation of robust ML methodologies not only enhances
the accuracy and efficiency of operations but also contributes to sustainable and economically viable
aquaculture practices. The adaptability of ML to the diverse data sets generated in aquaculture,
from IoT sensor data to satellite imagery, underscores its potential as a key driver of innovation and
productivity in the sector.
In a recent review by Zhao et al. [2021], authors discussed several applications of machine learning in
aquaculture:
1. Biomass Detection of Fish:Machine learning is used for estimating the size, weight, and count
of fish, which is crucial for managing fish populations and predicting yields.
2. Recognition and Classification of Fish:Techniques are employed for identifying fish species,
age, and sex, using machine learning algorithms. This is important for species management and
scientific research.
3. Behavioural Analysis:Machine learning aids in observing and interpreting fish behaviours
such as feeding and group dynamics, which is vital for welfare and environmental assessments.
4. Water Quality Parameter Prediction:Machine learning algorithms are used to predict and
monitor various water quality parameters, ensuring optimal conditions for aquaculture.
These examples illustrate ML’s growing role in driving more efficient, sustainable, and productive
aquaculture practices. The subsequent sections of this chapter will delve further into the diverse
applications of machine learning in fish farming, exploring its various implementations and impacts in
greater detail.
3.1 Computer Vision in Aquaculture
A significant share of research focuses on using computer vision technology to improve observation,
detection, and management of caged fish. Traditional methods using manual sampling often harm
fish and rely on human judgment, making them unsuitable for modern aquaculture’s demands [Jeong
and Revie, 2020]. The integration of machine learning and machine vision presents a new, intelligent
approach for estimating fish size, weight, numbers, and other biological information more accurately.
The inherent nature of farming fish underwater makes computer vision applications in aquaculture
challenging. Yang et al. [2021] summarised some of these challenges:
• Colour Similarity:Fish often change colour to match their environment, leading to a
resemblance between the fish and its background. This similarity complicates fine-grained fish
classification and accurate segmentation, impacting detection performance.
• Deformation:Fish are non-rigid and change posture, causing appearance alterations that can
disrupt tracking.
8

• Scale Change:The distance between the camera and fish affects the fish’s size in images,
influencing detection and counting accuracy. Smaller fish scales include more background,
causing errors, while larger scales may miss multiple targets in a single image, leading to
tracking and counting issues. Scale adaptation is essential.
• Occlusion and Disappearance:Fish may get obscured or disappear temporarily during
movement, resulting in tracking failures and loss of continuity in subsequent frames.
• Illumination Change:Varying light conditions, from sunrise to sunset and on bright to cloudy
days, affect light refraction in water, impacting video/image quality.
• Low Resolution:Camera optical and electronic systems can introduce noise and distortions,
leading to lower resolution images.
• Complex Background:Backgrounds with multiple non-fish objects similar to fish reduce
detection accuracy.
•Weather Change:Sudden weather shifts, like cloudiness, storms, or typhoons, worsen image
contrast, complicating video analysis and target detection.
• High-Density Scene:In dense aquaculture environments, severe occlusion during feeding
complicates individual fish tracking and behavioral analysis, especially since fish move in 3D
space.
•Turbidity:Changes in water clarity, due to factors like plankton, can lead to false positives in
fish movement tracking.
•Biofouling:Algae and dirt buildup on lenses in contact with seawater degrade image quality.
• Periodic and Multimodal Background:Algorithms must handle background movements and
variations, including periodic movements like those of plants in tides, to avoid misidentifying
non-fish objects as targets.
Considering the intricate nature of computer vision applications in aquaculture, considerable research
efforts have been dedicated to creating algorithms designed to effectively address these specific
challenges.
3.1.1 Biomass Detection of Fish
In aquaculture, accurately estimating fish biomass is crucial for effective management and sustainable
production. For size estimation, researchers have used algorithms on datasets like ImageNet and the
Atlantic fish dataset. Monkman et al. [2019] developed an R-CNN model for estimating European
bass length, achieving an average deviation of 2.2%. However, this model’s applicability is limited,
especially for overlapping fish. Li et al. [2020] used a CNN model based on transfer learning for
small sample pond fish data, reaching an accuracy of 93.93%. Voskakis et al. [2021], developed and
deployed a CNN model to estimate the length of European seabass and gilthead seabream in cages
with relative error of 3.1% and 7.4%, respectively
Accurateweightestimatesarecrucialforfarmerssincetheweightoffishdeterminesthepricereceived
at harvest time, impacting the economic viability of aquaculture operations. Therefore, precise weight
estimation is essential for effective planning, resource allocation, and maximising the returns from
the harvest. Typically, researchers focus on predicting quality based on fish body characteristics,
using image processing to extract size and shape features. Fernandes et al. [2020] combined linear
regression and CNN for predicting weight from body area, while Saberioon and Císař [2018] used
9

infrared light for image collection and RF and SVM models for back geometry prediction, overcoming
lighting constraints.
3.1.2 Recognition and Classification of Fish
Fish farmers need comprehensive information on each fish’s attributes such as size, weight, gender,
maturity stage, and skin color throughout their growth phases to efficiently track their development
and manage stocks [Saberioon et al., 2017]. Machine learning facilitates automated fish identification,
extracting their features, and classifying them through conventional computer vision methods. For
instance, the Stingray system employs computer vision to detect and eliminate individual lice on
salmon, addressing parasitic infections in aquaculture [Bui et al., 2020].
The task of fish target detection in aquaculture has seen significant advancements with the application
ofdeeplearningmodelslikeYOLO(YouOnlyLookOnce)andCNN(ConvolutionalNeuralNetworks).
YOLO-based methods have been employed for fish detection in various contexts, such as fish count
[Armalivia et al., 2021] and trajectories [Mohamed et al., 2020]. These methods have been further
refined, for instance, by Cai et al. [2020], who replaced the Darknet-53 network in YOLOv3 with
MobileNet, enhancing feature extraction and overall accuracy. Additionally, CNN models have been
increasingly favoured for their efficacy in fish detection. Villon et al. [2018] used the GoogLeNet
architecture combined with soft-max classification, achieving an accuracy rate of 94.9%. Extensions
of CNN models have further improved accuracy, with Rauf et al. [2019] deepening convolutional
layers to reach a maximum accuracy of 96.63%.
Beyond basic CNN architectures, advanced models like R-CNN and LSTM have also been applied
to fish detection. Li et al. [2016] utilised the Faster R-CNN model, initialised with the pre-trained
Zeiler and Fergus model, to enhance detection speed and accuracy. Techniques like background
subtraction have been employed to distinguish fish from other objects, with varying degrees of success
[Shevchenko et al., 2018, Gaude and Borkar, 2019]. Transfer learning methods, as used by Tamou
et al. [2018], have achieved high accuracy in challenging underwater environments. Additionally,
innovative methods like 360-panoramic systems and binocular vision-based image processing have
been developed, further expanding the scope of aquatic species recognition, including live crabs and
shrimp,withhighaccuracyratesreported[Caoetal.,2020,Huetal.,2020]. Thesediverseapproaches
demonstrate the evolving landscape of target detection in aquaculture, offering valuable insights for
future research in low-resolution image recognition and underwater species identification.
3.1.3 Behavioural Analysis
Accurate recognition of fish feeding behaviour can help farmers optimise feeding, reduce costs, and
enhance economic efficiency [Lopes et al., 2017]. Zhou et al. [2019] have made significant strides in
this area, employing near-infrared imaging technology to assess fish feeding behaviour. By applying
SVM and the gray gradient symbiotic matrix, they quantified the feeding behaviour index, achieving a
high correlation (0.945) with expert manual scores
Parallel efforts by other researchers have also focused on using neural network models for analysing
fishfeedingbehaviour. Måløyetal.[2019]integratedCNNandLSTMtodifferentiatebetweenfeeding
and non-feeding behaviours in salmon, achieving 80% accuracy. Adegboye et al. [2020] further
evaluated feeding behavior using Fourier descriptor threshold analysis, based on Noda and Gleiss’s
prior research dataset, reaching a remarkable 100% accuracy. Georgopoulou et al. [2024] developed a
continuous, real-time monitoring system to analyze and guide the feeding behaviour for seabass, based
on various machine learning models (YOLO and Deep SORT) and computer vision techniques. These
developments underscore the potential of intelligent systems for precise fish feeding management.
10

Regarding group behaviour in aquatic ecosystems, individual actions based on local stimuli can lead
to collective patterns, displaying remarkable coordination and adaptability within groups [Giardina,
2008]. Understanding fish group behaviors offers deeper insights into environmental or social changes
within these groups [O’Donncha et al., 2021]. Han et al. [2020] introduced a group behaviour
recognition method using CNN and spatio-temporal information fusion, successfully identifying six
distinct group behaviours in fish with an average accuracy of 82.5%.
Additionally, the monitoring of abnormal behaviours in fish is crucial for non-invasively assessing
fish welfare in aquaculture [Papadakis et al., 2012, Georgopoulou et al., 2022]. Zhao et al. [2018]
developed an RNN-based method for detecting abnormal behaviours in densely populated fish schools.
In addressing issues like dissolved oxygen anomalies and disease infections, Zhao et al. [2016] and
Morimoto et al. [2018] proposed machine vision-based assessments for abnormal behaviour in tilapia
andshrimp,focusingonindicatorssuchasswimmingspeedandmovementdistance. Theseapproaches
underscore the value of behavioural analysis in enhancing fish welfare and management in aquaculture
settings.
3.2 AI to Forecast Environmental Conditions
The increasing integration of AI and digital twin technologies is revolutionising environmental
management and decision-making processes. Destination Earth is a standout initiative in this domain
[DestinE, 2024]. As a critical part of the European Green Deal, it aims to steer the EU towards a
climate-neutral economy by 2050, employing advanced digital models to simulate Earth’s systems and
support eco-friendly policies [Bauer et al., 2021].
At the heart of Destination Earth is the Digital Twin of the Ocean [EDITO, 2024]. This project is
focused on constructing ahigh-precision digital replica of theocean, facilitating precise simulationsof
oceanic processes. The Digital Twin of the Ocean is multifaceted: it not only offers vital insights
into the health of the oceans but also aids in comprehending the effects of climate change on marine
ecosystems. Importantly, it assists in the sustainable management of marine resources. By modelling
various environmental scenarios, this digital tool enables policymakers to forecast the impacts of
differentpolicychoices,ensuringalignmentwiththeEuropeanGreenDeal’sgoals,suchasminimising
oceanpollution,managingfisheriessustainably, andconservingmarinebiodiversity[Tzilivakis,2022].
Furthermore, the Digital Twin of the Ocean exemplifies the potential of AI and high-performance
computing in fostering ecological sustainability and enhancing climate resilience [Tzachor et al.,
2023]. Fish farms are particularly significant in the context of the Digital Twin of the Ocean, serving
as both a primary source of ocean data and a critical use case for the development and application
of ocean technologies. While there has been extensive research into using AI for ocean forecasting
and water quality prediction [O’Donncha et al., 2024], particularly in freshwater systems [Oruche
et al., 2021, Oruche and O’Donncha, 2023]. Despite promising research, operational deployments of
AI technologies in aquaculture remain limited, underscoring the need for robust infrastructure and
standardized practices [Heimbach et al., 2024]. These studies have concentrated on predicting ocean
currents, waves, temperature, dissolved oxygen levels, and other key water quality indicators.
Yang et al. [2021] summarises some of these applications across univariate and multivariate imple-
mentations as well as forecasting different variables
3.2.1 AI Applications for Environmental Prediction
The application of machine learning (ML) for time-series forecasting has seen extensive exploration
in a broad spectrum of application papers. For classical (linear) time series, where all pertinent
information about the next time step is encapsulated in the recent past, a multilayer perceptron (MLP)
11

is typically adequate to model short-term temporal dependence [Gers and Schmidhuber, 2001]. In
contrast to MLPs, convolutional neural networks (CNNs) autonomously identify and extract features
from the input time series. Unlike MLPs and CNNs, recurrent neural networks (RNNs) explicitly
allow for long-term dependence in the data to persist over time, a feature that is particularly desirable
for modelling time series. A comprehensive review of many of these approaches for time series-based
forecasting is provided in [Esling and Agon, 2012, Gamboa, 2017, Fawaz et al., 2019].
Owing to the significant computational overhead of physical models, there is an increasing trend
towards the application of data-driven DL or ML methods to model physical phenomena [de Bezenac
et al., 2017, Wiewel et al., 2018]. Indeed, the geosciences were among the earliest adopters of
machinelearningtechniques,withthewidespreaduseofKrigingtechniques[WilliamsandRasmussen,
2006]. Kriging, effectively Gaussian Process regression, is a method of interpolation governed by
prior covariances and was first introduced by Matheron [1963] for estimating the most probable
distribution of gold based on samples from a few boreholes. It later made significant contributions to
the field of geostatistics [Dramsch, 2020]. The interest in the potential of machine learning to address
environmental challenges has flourished in the past decade, driven by the growth in data-intensive
computing [Hey et al., 2009]. A central focus has been climate change, and a recent review offers a
comprehensive discussion on the potential impact of various machine learning methods for modelling,
engineering, and mitigation to address this issue [Rolnick et al., 2019].
There is a vast body of literature related to machine learning-based forecasting methods. These
include an array of shallow (e.g., decision trees, random forests, support-vector machines) and
deep neural network (DNN) approaches. Wolff et al. [2020] compared the performance of different
statistical, machine learning, and DNN methods for forecasting sea surface temperature (SST). The
results indicated that, given sufficient training data volumes, simpler methods could achieve accuracy
comparable to DNNs.
Numerous research efforts have developed frameworks to effectively capture the spatiotemporal
characteristics of geophysical systems. The Bidirectional Long Short-Term Memory (BiLSTM)
networks, with their distinctive architecture, are particularly adept at modeling these characteristics,
as they efficiently handle complex dependencies inherent in time series data, encompassing both
spatial and temporal dimensions. O’Donncha et al. [2022] leveraged BiLSTM networks for predicting
temperatureanddissolvedoxygenlevels,utilizingdatafromanetworkofIoTsensors. Thisapplication
underscorestheefficacyofBiLSTMnetworksinprocessingandinterpretingtheintricatespatiotemporal
patterns present in environmental data.
AwidelyusedframeworkcombinesCNNwithLSTMtorepresentboththespatial(CNN)andtemporal
(LSTM)dependencieswithinthedata. Thefundamentalstructureofthisapproachistoformulateboth
the inputs and outputs as spatiotemporal sequences (or a sequence of images). By initially processing
the spatial datasets with a convolutional layer, local correlation and global coherence of each pixel are
expressed and retained by patches with fixed dimensions, which are then processed by an LSTM that
aims to encode the temporal dependencies. This approach has been applied to various geoscientific
tasks, such as precipitation nowcasting from rainfall radar maps [Xingjian et al., 2015] and forecasting
sea surface temperature from satellite-derived observations [Yang et al., 2017].
More recently, Xiao et al. [2021] used a convolutional LSTM algorithm for multivariate time series
prediction. The exogenous features were treated as an "image" and processed with a convolutional
layer that extracted information on the relationship between different exogenous features at a point in
time. The convolved features were then fed to the LSTM model to learn the temporal dependencies.
This framework was applied to time series data from environmental, energy, and financial applications.
A number of studies have investigated data-driven approaches to provide computationally cheaper
surrogatemodels,appliedtowaveforecasting[Jamesetal.,2018,O’Donnchaetal.,2018],airpollution
[Hähnel et al., 2020], viscoelastic earthquake simulation [DeVries et al., 2017], and water-quality
12

investigation [Arandia et al., 2018]. Many studies have explored how machine learning could improve
ocean monitoring and forecasting either by mining large ocean datasets [Gokaraju et al., 2011] or
relating future conditions to historical observations [Wolff et al., 2020]. These include DL-based
approachestoincreasetheresolutionofsatelliteimagerythroughdown-scalingtechniques[Ducournau
and Fablet, 2016]; and data-mining applied to the large datasets generated by ocean monitoring and
modelling tools to identify pertinent events such as harmful algal blooms [Gokaraju et al., 2011].
An alternative approach aims to embed information from physics or heuristic knowledge within the
network. Physics-informed DL is a novel approach for integrating information from physics. This
method approximates the quantity of interest (e.g., governing equation variables) by a deep neural
network (DNN) and embeds the physical law to regularise the network. Training the network is thus
equivalent to the minimisation of a well-designed loss function that contains the PDE residuals and
initial/boundary conditions [Rao et al., 2020].
4 AI and Emerging Trends in Aquaculture
AI applications in aquaculture are at a nascent stage. Technologies such as computer vision, IoT, and
deep neural networks offer immense promise. However, operational deployments at scale are still
limited.
Initiatives like Destination Earth [DestinE, 2024] and the Digital Twin of the Ocean [Tzachor et al.,
2023] are becoming critical enablers for improved decision-making in ocean-related activities. In
parallel, the weather forecasting community has experienced rapid advancements in AI-backed
forecastinginrecentyears. ThissignificantincreaseinAIimplementation, oftenreferredtoasa"quiet
revolution," has marked a notable milestone where AI has, for the first time, outperformed traditional
weather prediction models in terms of efficacy [Maskell, 2023]. These are certainly indicative of
future technology trends related to digital twin solutions for aquaculture[Alvarez Fanjul et al., 2024]
Theworld’stopweatheragency,theEuropeanCentreforMedium-RangeWeatherForecasts(ECMWF),
has embraced the technology: Recently it began to generate its own experimental operational forecasts
based on AI methods. Three different architectures are used:
• FourCastNetv2-small:An advanced version of the Nvidia-led FourCastNet deep learning
system, which employs Spherical Fourier Neural Operators for spatial dependency analysis.
This streamlined model is designed to be compatible with a single Nvidia A100 40GB for
inference purposes. Trained on ERA5 data to reduce mean-squared-error in predictions, it
functions at a resolution of 0.25°[Bonev et al., 2023].
• Graphcast:Developed by Google Deepmind, this deep learning system utilizes a graph
neural network structure, incorporating an encoder-processor-decoder design with a multi-mesh
approach. The model, trained on ERA5 data at a 0.25°resolution, was further refined using the
ECMWF HRES forecast to lower mean-squared-error in its predictions [Lam et al., 2022].
• Pangu-Weather:Created by Huawei, this deep learning system is based on a 3D transformer
architecturetoanalysespatialdependencies. Itcomprisesmultiplemodelsformakingpredictions
overvarioustimeframes,suchas24hoursand6hours. Thetraining,conductedwithERA5data,
focused on reducing mean-squared-error for each predictive model, operating at a resolution of
0.25°[Bi et al., 2023].
Thesesignificantadvancementscaninformalgorithmsanddatapipelinesthatcanenhancedigitaltwin
opportunities for aquaculture. Across these models Graph Neural Networks (GNNs) and transformer
architectures play key role.
13

4.1 Graph Neural Networks
Graph Neural Networks (GNNs) represent a category of neural networks designed to work with
graph-structured data, adept at handling intricate and interlinked relational data. Their ability to
process data represented not as sequences or grids but as networks of interrelations makes them
exceptionally suitable for fields where data is network-centric, like environmental and biological
systems, or transportation networks. An illustrative case is the GraphCast weather forecasting system,
which employs GNNs to effectively handle data with inherent spatial structures.
One of the key strengths of GNNs is their versatility in various scientific and industrial applications.
They have been instrumental in drug discovery, where they help in predicting molecular interactions
[Stokes et al., 2020], and in traffic forecasting, where they analyse and predict traffic patterns in
transportation networks [Derrow-Pinion et al., 2021]. GNNs also find applications in social network
analysis, where they can be used to model and predict user behaviour and interactions within the
network. This broad applicability of GNNs stems from their ability to model complex relational
patterns and dependencies, which are common in many real-world datasets.
In the realm of net-pen fish farming, GNNs present significant potential for enhancing various aspects
of aquaculture through their advanced capability in modelling complex, interrelated data. GNNs,
by their very nature, are adept at capturing relational information, making them particularly suited
for representing and analysing the intricate network of interactions within fish farming ecosystems.
For instance, in water quality monitoring, GNNs can be utilised to predict parameters like dissolved
oxygen, temperature, and nutrient levels.
Parasitic infections, like sea lice in salmon farming, are naturally amenable to graph-based modelling
since the spread of lice between cages, farms, or even regions can be represented as a dynamic
networkofspatialandbiologicalinteractions—makingGraphNeuralNetworks(GNNs)well-suitedfor
capturingsuchrelationalstructures[Langbridgeetal.,2023]. Thisapproachenablespredictiveanalytics
for early detection and intervention, potentially reducing the spread of parasites and minimising
the need for chemical treatments, thus promoting a more sustainable and environmentally friendly
approach to aquaculture.
Moreover, GNNs hold potential in broader industry aspects such as fish behaviour analysis, yield
prediction, and feed optimisation. By analysing the spatial interactions and movements of fish within
cages, GNNs can provide insights into fish behaviour, stress levels, and overall well-being. Such
analyses can inform improved cage management practices, leading to enhanced fish health and growth
rates. Further, construction of an effective graph topology informing similarity between cages, farms,
or regions can enhance the predictive skill of models [Azmat et al., 2023, Ba et al., 2023]. This
is particularly critical for aquaculture where factors like ocean currents play a key role in material
transport between cages and farms.
4.2 Large Language Models
Large Language Models (LLMs), also referred to as foundation models or generative AI, represent a
paradigm shift in artificial intelligence due to their scalability, adaptability, and wide applicability
across domains. These models, trained on extensive and diverse datasets, are capable of learning a
broadrangeoftaskswithouttask-specifictrainingdata. ExamplesincludemodelslikeGPT-4[Achiam
et al., 2023] for natural language processing and early efforts such as BERT [Jawahar et al., 2019]
for text understanding. Their training relies on vast amounts of data, often scraped from the internet,
enablingthemtodevelopawide-rangingunderstandingofhumanlanguage,behaviour,andknowledge.
Once trained, LLMs can be fine-tuned or adapted to specific tasks, making them highly versatile and
efficient for various applications, from language translation and content generation to more complex
14

tasks like answering questions, writing code, or creating artistic content [Bommasani et al., 2021].
The widespread success of LLMs can be attributed to three main factors [Tunstall et al., 2022]:
• Transformer Architecture:Introduced in the 2017 paper "Attention Is All You Need" by
Google researchers [Vaswani et al., 2017], transformers represent a paradigm shift in neural
network design. They replace the sequential processing of RNNs/LSTMs with a parallel
approach, using an ‘attention mechanism’ to assess the relevance of different parts of input
data. This allows for processing entire data sequences simultaneously, enhancing efficiency and
effectiveness for tasks with large sequences, like language modelling and translation. Their
ability to manage long-range dependencies with reduced computational complexity, while
preserving context, has established transformers as the de facto standard for modern natural
language tasks.
• Pre-trained foundation models:Instead of building a model from the ground up for specific
applications, it is now feasible to use a model pre-trained on a general dataset and fine-tune
it for particular needs. This approach reduces the need for large task-specific datasets and
extensivetrainingfromscratch,whichiswhythesemodelsarereferredtoas’foundationmodels’
[Bommasani et al., 2021]. They serve as a versatile starting point for crafting task-specific
models.
• Accessibility through Model Hubs like Hugging Face:The advent of Hugging Face’s
Transformers library marked a significant development. Earlier, finding pre-trained models
was challenging as they were scattered across various platforms. Hugging Face’s open-source
library supports TensorFlow and PyTorch and simplifies accessing, configuring, fine-tuning,
and evaluating state-of-the-art pre-trained models from the Hugging Face Hub. As of 2025,
Hugging Face hosts over 900,000 models on its platform, and serves more than 7 million users
and 50,000 organisations, including major tech companies like Google and Microsoft [Wolf
et al., 2025]
Transformer-basedarchitectures,initiallycelebratedfortheirprowessinlanguagetasks,haveexpanded
their versatility to other sectors including code generation [Jimenez et al., 2023], computer vision,
time series forecasting [Liu et al., 2025], and industrial applications. For example, IBM Research
has innovated a geospatial model using these architectures that can interpret satellite images to map
environmental changes and natural disasters [Mukkavilli et al., 2023]. Utilising these foundation
models, developers and researchers can bypass the extensive time and resources traditionally needed
to develop new models from the ground up. These models offer a strong foundational skill set that can
be customised for specific needs or industries.
While still emerging in aquaculture, the successful application of transformer architectures and
foundation models in other industries suggests strong potential for future adoption. Given the
superiorityoftransformersoverRNNs,LSTMs,andotherdeeplearningmodelsintaskslikesequential
language modeling, it is reasonable to expect their increasing adoption in areas like digital twin
technology for fish farming and enhanced automation.
4.3 LLM Powered Autonomous Agents
The integration of large language models (LLMs) as autonomous agents is creating transformative
opportunities across industries, including aquaculture. By leveraging the natural language capabilities
of LLMs, these agents can interpret, process, and respond to complex queries, making them uniquely
suited for managing data-rich and dynamic environments. In aquaculture, where operations depend on
preciseenvironmentaldata,resourceoptimization,andreal-timemonitoring,LLM-poweredagentscan
15

Figure 1: This diagram illustrates the key components and data flows in a large language model
(LLM)-driven agent architecture. The central agent coordinates interactions between tools (e.g.,
calculators, code interpreters, APIs), memory systems (short-term and retrieval-augmented), and
actionmodules. Cognitiveprocessessuchasplanning,taskdecomposition,self-critique,andreflection
support goal-oriented behavior and adaptive reasoning. Guardrails ensure system robustness through
safety, factual reasoning, feedback, and monitoring. The architecture enables scalable, flexible
execution of complex tasks in dynamic environments.
serve as both decision-support tools and proactive managers, bridging the gap between data sources
and actionable insights.
In an LLM-powered autonomous agent system, the LLM functions as the “brain” of the agent,
supported by several essential components [Weng, 2023]:
• Planning: The agent breaks down large, complex tasks into smaller, manageable subgoals,
enabling it to handle intricate processes efficiently.
• Memory: The agent utilizesin-context learning—often facilitated by prompt engineering—to
temporarily retain and apply relevant information, functioning as a form of short-term memory.
This can be augmented with external vector storage for long-term memory capabilities
• External API and Tool Calling: The agent learns to call external APIs for information that is
unavailable within its model weights, which are typically static after pre-training. This includes
access to current data, the ability to execute code, and retrieval from proprietary databases,
expanding the agent’s knowledge and capabilities beyond its pre-trained state.
These components work together to enhance the LLM’s performance, enabling it to plan complex
tasks, remember information effectively, and extend its functionality through external tools. Figure 1
summarises these capabilities.
OneofthemostsignificantadvantagesofLLM-poweredagentsistheirabilitytoperform"toolcalling"
—accessing and interacting with various tools and systems based on the needs of a particular task. In
aquaculture, this functionality allows an agent to autonomously query databases, access web-based
information, interact with APIs, and analyze incoming data streams. By invoking specific tools, such
as:
16

• Databases: Agents can access internal databases to retrieve historical information on fish health,
water quality, and feeding patterns, enabling real-time analysis and historical comparisons.
• Web Search: With access to external web sources, agents can find recent research, industry best
practices, and updates on regional regulations or environmental concerns.
• Weather Data: By accessing weather forecasts and live updates, LLM agents can offer valuable
insights into weather conditions, allowing managers to anticipate challenges related to water
temperature, storms, and seasonal changes that may impact fish welfare.
• Environmental and Model Data: Agents can interface with environmental sensors and model-
based systems, providing real-time updates on factors like dissolved oxygen levels, salinity, and
currents, all of which are critical for maintaining optimal conditions within aquaculture systems.
The ability to interact with these varied data sources positions LLM agents as versatile tools capable
of synthesizing information from multiple channels to create a cohesive and context-aware picture of
operations. This capability is particularly valuable in complex systems like aquaculture, where diverse
and interdependent variables influence outcomes.
LLMs’ fluency in natural language enables their use as a universal interface, making them accessible
to a wider range of users, including those without technical training. This aspect greatly enhances
accessibility and usability, as non-technical personnel in aquaculture can interact with the system
simply by using conversational language. For example, an aquaculture manager could ask the
LLM-powered agent, “What’s the expected water temperature over the next week?” or “Have there
been any significant changes in dissolved oxygen levels in the last 24 hours?” The agent can interpret
these questions, identify relevant data sources, retrieve the necessary information, and provide a
straightforward response.
Thislanguage-basedinterfacealsofacilitatesmorecomplexinteractions,suchasrequestingasummary
ofrecentenvironmentalconditionsandtheirimpactonfishgrowthratesoraskingtheagenttocompile
a report on feeding efficiency based on recent patterns. The agent’s ability to understand and execute
these natural language commands allows for rapid decision-making and reduces the learning curve for
users, promoting broader adoption of technology in aquaculture operations.
The use of LLM-powered agents in aquaculture remains nascent, but their rapid development suggests
significant potential for expanding their capabilities across monitoring, prediction, and autonomous
decision-making. Key areas of potential growth include enhanced integration with remote sensing
technologies, refined models for predicting fish growth and health outcomes based on environmental
factors, and deeper incorporation of machine learning algorithms to enable predictive analytics. As
LLM agents continue to evolve, their ability to learn and adapt to specific aquaculture contexts could
maketheminvaluableasautonomousmanagerscapableofoptimizingoperationswithminimalhuman
oversight.
Overall, LLM-powered autonomous agents offer a compelling vision for the future of aquaculture,
providing a centralised, language-driven interface that leverages diverse data streams and advanced
tool integrations. By harnessing these capabilities, aquaculture operations can become more resilient,
adaptive, and efficient, paving the way for sustainable growth in the face of environmental challenges
and market demands.
5 Case Studies
While AI and machine learning applications in aquaculture are rapidly expanding, much of the
current work remains exploratory or limited to isolated deployments. Unlocking the full value of
17

these technologies depends on building robust data infrastructures, scaling models effectively, and
integrating AI seamlessly into existing operational workflows. Advances in areas such as unmanned
monitoring platforms, remote sensing, edge computing, and simulation offer exciting possibilities for
accelerating the adoption of AI-driven solutions. Notably, the convergence of machine learning with
digital twins and real-time environmental modelling stands to transform aquaculture from reactive
management to proactive, predictive control.
Thefollowingcasestudiesillustratehowsomeoftheseemergingtechnologiesarealreadybeingapplied
in practice. They highlight different strategies to improve environmental forecasting and operational
decision-making in marine and aquaculture settings. Specifically, the case studies demonstrate:
• Thedeployment ofreal-timesensornetworksandmachinelearning modelstoforecastdissolved
oxygen on Atlantic salmon farms in Scotland;
• The use of satellite remote sensing combined with machine learning for spatial estimation of
water quality variables in aquaculture zones;
• A novel LLM-based agentic architecture applied to digital twin workflows for shipping,
showcasing how agentic AI can support complex operational decision-making.
Together, these examples provide a snapshot of how AI and digital twin technologies are beginning to
reshape the aquaculture and marine sectors.
5.1 Case Study 1: Application of a real time sensor network in developing machine
learning models to forecast dissolved oxygen on Atlantic salmon farms in Scotland
Introduction
Oxygen is a critical and dynamic parameter that affects fish metabolism and stress and ultimately
impacts growth efficiency [Remen et al., 2012]. Widescale environmental monitoring on aquaculture
farms has been adopted by the industry to monitor the complex dynamics of dissolved oxygen at the
pen level and is used to inform feeding decisions [Burke et al., 2021]. This adoption has created long
term environmental data sets that can be used in model development to forecast oxygen in open net
pens. Oxygenforecastingcanhelptoimprovedecision-makingtomaximizegrowthefficiency. During
feeding, oxygen levels must be above a given threshold (which varies depending on temperature but
generally, 70% saturation is used) and there must be reasonable confidence that oxygen will remain
above this threshold hours later, during the digestive process that uses up additional oxygen [Remen
et al., 2016]. If oxygen levels are too low, fish become stressed and energy is allocated to other more
critical life functions instead of growth, and in severe cases fish will regurgitate feed resulting in feed
waste and reduced feed conversion ratios (FCRs). Providing confidence in near-term oxygen levels
using machine learning predictions can assist with real time decision making and helps to maximize
growth and enhance welfare by feeding only under optimal environmental conditions.
Machine learning models have been proposed as an alternative to traditional ocean models to capture
thefine-scaleprocessesthatapen-levelforecastnecessitatesandtoaccountfortheeffectofthebiomass
on dissolved oxygen levels in the pen. This project scrutinizes which machine learning models best
capture oxygen dynamics at the pen level and examine the robustness of a model as it is scaled up and
tested on different pens within the same farm, on pens at different farms within the same geographic
region and on pens at farms in different regions. The model was first trained on a farm located in
the Shetland Islands, and then tested on a farm on the west coast of mainland Scotland and finally
performance was evaluated on a farm located on the west coast of Canada. This work is ongoing, but
some preliminary results are presented below.
18

Methodology
Preprocessing of operational data is a critical step as datasets often contain many imperfections
such as erroneous measurements, anomalies, and missing data. The data consisted of historical
observations of oxygen concentration, temperature, and salinity for individual cages on various farms.
During preliminary analysis, temperature and salinity were identified as key features for normalization
and time-based variables such as the day of the week, hour of the day, and month of the year were
also incorporated [Linardatos et al., 2020]. These variables are crucial as they enable the model to
effectively capture the trends and seasonality of oxygen levels. A circular numeric encoding strategy
was adopted for time-based variables to maintain their cyclical nature, enhancing the model’s ability
to discern patterns in oxygen levels. Many different models were tested and compared including linear
regression, random forest, and Long Short-Term Memory (LSTM). However, the Temporal Fusion
Transformer (TFT) model reported best performance due to its effectiveness in handling complex
time-series data. The adoption of this architecture was informed by several standout features:
• Multi-headed Self-attention Mechanism: This feature allows the model to assign differential
significance to various temporal intervals, a critical function for decoding complex time-related
patterns in data, such as seasonal fluctuations and the influence of specific events on oxygen
concentration. By prioritizing relevant periods over others, the model achieves superior
forecasting precision.
• Dual-stage Architecture: The model employs an encoder-decoder framework that combines
historical data analysis with future event prediction. The encoding phase processes past data,
whereas the decoding phase is dedicated to forecasting the target time series. This method
increases the model’s understanding of time patterns, improving its prediction accuracy and
reliability for different forecasting horizons.
• Quantile Forecasting: This enables the prediction of a spectrum of outcomes at varying
probability thresholds. By forecasting seven quantiles of future oxygen concentrations, the
modelprovidesacomprehensiveoverviewofpotentialscenarios, facilitatingenhanceddecision-
making capabilities. Seven is the standard number of quantiles for this model and uses an
uneven distribution of thresholds for the output (0.02, 0.1, 0.25, 0.5, 0.75, 0.9, 0.98).
The refinement of the model involved a detailed evaluation of its forecasting performance, at the
individual pen level and across entire farms, through comparative analysis with baseline models,
utilizing its dual-stage and multi-horizon forecasting functionalities. The models were trained using a
structured cross-validation method to verify its efficiency across assorted data segments, including
different cages, farms, and geographical regions. This approach, coupled with strategic parameter
selection, demonstrated the model’s adaptability and applicability across different farms. To assess the
model’s predictive performance, particularly its ability to forecast extreme changes in oxygen levels,
a set of evaluation metrics was carefully chosen. These included mean absolute error (MAE) and
quantile-based metrics to evaluate accuracy within specific ranges (Figure 2).
Regarding the quantile confidence interval accuracy, the model analyses data at time t and compares it
with the quantiles for time t + 24 hours (ranging from the lowest quantile, Q1, to the highest, Q7 ),
measuring how often the actual oxygen levels fall within these predicted ranges, providing a clear
percentage of coverage (Figure 3) and allowing operators to derive a range of model outputs based
on their risk tolerance. The practical deployment of the model will highlight its utility in generating
real-time forecasts. By analysing data from the preceding 48 hours, it can project oxygen levels for the
upcoming 24-hour period across seven quantiles, delivering insights into potential variances.
19

Figure 2: Mean average error (MAE) of 24-hour prediction for various tests of the model on the same
cage it was trained on, a different cage from the same farm, a cage from a different farm within the
same region and a cage on a farm in a different region.
Conclusions
The model was capable of outputting 24-hour predictions for various farms within the same region,
with an MAE less than 0.7 mg/l. These findings demonstrate that reasonably accurate pen-level
forecasting is achievable, validating ML as a viable alternative to traditional environmental models.
The MAE increased when the model was tested on farms in different geographic regions, which
suggests that models should be trained on data within a reasonable geographic area to achieve the
highest possible accuracy. Operational forecasting is a growing area of research in precision fish
farming, aimed at equipping farmers with data-driven tools for more proactive decision-making.
Oxygen concentration is a dynamic and complex measurement that is impacted by many distinct
factors including, tidal and water exchange, biomass, farm orientation, and plankton presence and
this research shows that machine learning models can accurately capture these complexities and there
is potential for these insights to be used on farms to help with feeding decisions under challenging
conditions.
This study highlights how machine learning can significantly enhance pen aquaculture forecasting by
overcoming the limitations of traditional numerical models, which are bound by their grid resolution
and sub-grid process parametrization. Unlike these conventional methods, machine learning models
adeptly adjust to the scale of observational data. Coupled with the influx of high-resolution data from
Internet of Things (IoT) devices, machine learning enables the development of more detailed and
adaptable forecasting frameworks, paving the way for improvements in aquaculture efficiency and
sustainability. Further details on this work can be found in Khan et al. [2024]
20

Figure 3: Actual raw oxygen concentration and model output of a 24-hour prediction using 7 quantiles
that indicate a confidence interval for the forecasted values. Data presented shows the output of the
model on a single cage that was trained on the entire farm dataset.
5.2 Case Study 2: Dissolved oxygen estimation in aquaculture sites using remote
sensing and machine learning
Introduction
DissolvedOxygen(DO),togetherwithtemperature,isoneofthemostcriticalenvironmentalparameters
affecting the physiology and performance of marine organisms. Consequently, accurate monitoring is
of great importance for finfish aquaculture as it directly affects the survival, growth, food intake, and
health of the farmed fish [Oldham et al., 2019, Burt et al., 2012]. For net pen aquaculture in particular,
the continuous monitoring of DO is a necessity as environmental conditions at the rearing sites are
outside human control and are therefore prone to fluctuations that may threaten production.
DO monitoring has utilised manual, semi-automated, and fully automated in-situ sensors [Parra et al.,
2018]. While such modes of DO monitoring are simple and have been effective in the past, the
rapid expansion of aquaculture towards precision farming methods necessitates advanced systems
that contribute towards real-time monitoring and forecasting [O’Donncha and Grant, 2019, Raju and
Varma, 2017]. Accurate forecasting of dissolved oxygen depends heavily on capturing the unique
spatial and environmental characteristics of each aquaculture site. While in situ sensors are promising,
they do not provide complete coverage at the pen-, farm-, and bay-scale level. Furthermore, organised
zonesofaquacultureactivitywithseveralfarmsinstalledhavesimilarneedsandlargescalemonitoring
isessentialforforecasting. Remotesensingisapowerfultooltoenhancefarmmonitoringanddecision
making.
Although remote sensing is widely used to detect variables that affect the optical properties of water at
specific wavelengths such as chlorophyll-a (Chl-a), total suspended matter (TSS), and temperature,
it is unlikely to record the concentration of DO directly from the reflection values of the satellite
sensors. Instead, it can be estimated indirectly because of its correlation with other parameters, such
as temperature and Chl-a [Guo et al., 2021, Kim et al., 2020].
21

DOgenerallyexhibitsanegativecorrelationwithseatemperature[MatearandHirst,2003,Mavropoulou
etal.,2020]. PrimaryproductionalsoaffectsDOlevels,whichisoftenmeasuredbyChl-a,anindicator
of phytoplankton abundance in surface waters [Guy et al., 1993, Lewis et al., 2016].
Based on the above theoretical mechanisms, several researchers have tried to develop models for the
correlation of DO with environmental parameters, such as sea surface temperature (SST) and Chl-a
[Karakaya and Evrendilek, 2011, Batur and Maktav, 2018, Kim et al., 2020, Guo et al., 2021]. This
aims to provide the potential to monitor DO from satellite sensors. Different approaches such as
Response Surface Regression (RSR), Multiple Linear Regression (MLR), Artificial Neural Network
(ANN),SupportVectorMachines(SVM)andSupportVectorRegression(SVR)havebeenscrutinized.
While previous research has been successful in estimating DO levels, data sparsity and the demand for
high resolution estimation in coastal zones has limited the value of the approach for aquaculture. In
our study, we developed a methodology for the estimation of DO in coastal areas with aquaculture
facilities, based on daily CMEMS data and machine learning techniques.
Methods and Data
ThesatellitedatausedwerefromCopernicusMarineEnvironmentMonitoringService(CMEMS)that
provides regular and systematic biogeochemical and physical information on the marine environment.
In our study, we exploited Level-4, daily, gap-free satellite observations for Chl-a concentration and
SST from multi-platform observations. Our in-situ dataset includes field measures of DO and SST
from a fish farm in Lesvos Island, Greece. Dissolved oxygen was measured daily between 8:00am
and 10:00am using an OxyGuard sensor with a scavenging packet. 80% of the dataset served as the
training sample, while the remaining 20% was utilized as the test sample.
The farm is located at Lesvos Island, in North Aegean Sea, an area which is generally characterized as
an oligotrophic sea [Krom et al., 1991]. The capacity of the farm is 380T per year and the main fish
farmed are the European sea bass (Dicentrarchus labrax) and the gilthead sea bream (Sparus aurata).
Water temperature in the surrounding area ranges between 14°C to 24°C and the salinity is constant at
39 psu. The average depth in the farm is approximately 50m.
For the study, we developed an approach for DO estimation based on a Support Vector Regression
machine learning model, using CMEMS data and in-situ observations. For each spatial coordinate, an
input array was constructed incorporating chlorophyll-a (Chl-a) and sea surface temperature (SST)
values across a three-day lagged window prior to sampling.
SupportVectorRegression(SVR)hasbeendemonstratedtoeffectivelytacklebothlinearandnonlinear
problems, showing strong performance even with small datasets [Guo et al., 2021]. SVR, a variant
of Support Vector Machines, is a non-linear, non-parametric machine learning model that adheres
to Vapnik’s principle of structural risk minimization for supervised learning [Vapnik, 2013]. Unlike
linear regression, which seeks to minimize squared error sums, SVR aims to manage errors within a
predefined tolerance, enabling the selection of error margins (𝜖) and the determination of the optimal
hyperplane for decision-making. This approach provides flexibility in model accuracy by adjusting (𝜖)
and incorporating slack variables (𝜉) to tolerate training errors, enhancing the model’s resilience to
noise and outliers. The model’s formulation involves an objective function and constraints, detailed in
equations 1 and 2, which guide the optimization process:
min 1 2∥𝑤∥ 2+𝐶 𝑛∑︁ 𝑖=1 |𝜉𝑖|(1)
|𝑦 𝑖−𝑤 𝑖𝑥𝑖|≤𝜖+|𝜉 𝑖|(2)
22

where 𝑦𝑖 is the target,𝑤𝑖 is the coefficient, and𝑥𝑖 is the predictor (feature).𝐶 corresponds to a
user-selectedparametertocontrolthecomplexityofthemodel,actingasatrade-offparameterbetween
nonlinearity and number of training errors.
Tocapturemoreintricatehyperplaneshapesbeyondlinearapproaches,onecanutilizekernelfunctions
like polynomial, radial basis function (RBF), and sigmoid kernels. In the current study, the RBF
kernel was chosen for its promising capabilities [Guo et al., 2021]. SVR, with its simple structure,
is supported by various programming languages. Model development was performed in Python 3.4
usingthescikit-learnlibrary(v0.18.1),whichprovidesefficientsupportforSVRandrelatedregression
techniques. Model evaluation was conducted using residual analysis alongside mean absolute error
(MAE) and root mean square error (RMSE) as standard performance metrics. MAE calculates the
precision expressing the average distance between the estimated and the real values, and is described
by equation 3. RMSE describes the standard deviation of the residuals (equation 4).
MAE=
˝𝑛
𝑖=1|𝑦 𝑖−𝑥 𝑖|
𝑛 (3)
RMSE=
√︄ ˝𝑛
𝑖=1(𝑦 𝑖−𝑥 𝑖)2
𝑛 (4)
where𝑦𝑖 is the predicted values and𝑥𝑖 the measured values. The initial dataset included dates, in-situ
DOmeasurements,latitude,andlongitudetogetherwiththevaluesofChl-aandSSTfromCMEMSfor
each date and the previous 3 days. In Fig. 4, a graphical representation of the approach is presented.
Results
The data collected from CMEMS (Chl-a, SST) and the estimated DO were used to create daily maps
for examining their spatial distribution with a resolution of 1 km. Fig. 5 presents snapshots of SST,
Chl-a and DO in the surrounding sea area of Lesvos.
Fig. 5(c)presentsmodelledestimatesofDO.Naturally, thespatialdistributionfollowssimilarpatterns
to those of SST and Chl-a. Higher concentrations are observed in the north-eastern waters, near the
coastline, presenting a clear negative correlation with SST and a weaker positive correlation with
Chl-a. In general, DO concentration varied from 7 to 7.8 ppm across the year with four pronounced
dropsbelow6.5ppm. Highestvaluesweredetectedinthewinterandspringmonthswithlowestvalues
reported during summer and fall.
The accuracy of our model was tested using the value of Mean Absolute Error (MAE) and Root Mean
Squared Error (RMSE), as well as plots of the residuals. These are the most widely-used metrics
for evaluating a regression model. Both metrics quantify the distance between the actual and the
predicted values and are measured in the same units as the output variable, which contributes towards
an interpretable performance metric. Our model performed well with MAE of 0.11 and RMSE of
0.13, and the residuals were evenly distributed around 0. These indicate accurate model performance
with no obvious bias present.
WehavechosentouseMAEandRMSEindicestovalidateourmodelastheygiveaclearerviewofthe
error and distribution of the residuals. On the contrary,𝑅2 was poor (0.32) compared to other studies.
𝑅2 is generally used in similar studies to examine the fitness of the model instead of the performance,
and it doesn’t adequately consider the magnitude and direction of error. In this context, we do not
consider the poor value of𝑅2 to be informative for the practical applicability of the method.
Our results show a promising approach to estimate DO at aquaculture sites, which paves the way for
the development of real-time monitoring systems for aquaculture. The methodology successfully
23

Figure 4: Flowchart of the implemented methodology. Reproduced from Chatziantoniou et al. [2022],
https://doi.org/10.1016/j.rsase.2022.100865, under the CC BY-NC-ND 4.0 licence.
correlates DO with SST and Chl-a, reporting high agreement with field data. The model replicates
not only shifts in the seasonal patterns of DO but also sudden drops in concentration in at least four
occasions during the summer. While the drops in the analyzed time-series are of minor practical
interest because they are relatively small and thus, don’t constitute a concern for fish, the capability
of the method to realistically capture them is reflective of its potential as a monitoring tool that can
accurately estimate high resolution dynamics.
Another advantage of the proposed approach is that it increases the spatial scale at which monitoring
can occur. While in-situ sensors are paramount for precise measurements within a single cage of a
farm, a remote sensing approach offers a better representation of the oxygen conditions, and thus,
potential dangers, at a larger area. Considering that aquaculture farms are often aggregated within
the limited coastal space of suitable farming areas, either as single operations or as an organized
industrial park, it is imperative for the aquaculture producers to monitor the DO at a higher spatial
scale. The same applies to administrative authorities that may be interested in the supervision of zones
of organized aquaculture activity at a regional level.
24

(a)
 (b)
 (c)
Figure 5: The spatial distribution of (a) SST (b) Chl-a and (c) DO around Lesvos Island for four
representative dates (fall, winter, spring, summer). Reproduced from Chatziantoniou et al. [2022],
https://doi.org/10.1016/j.rsase.2022.100865, under the CC BY-NC-ND 4.0 licence.
5.3 Case Study 3: Agentic AI for Digital Twin Applications in Shipping
Introduction
The global shipping industry, comprising over 100,000 vessels facilitates the transport of 90% of the
world’s goods, yet it also contributes 3% of global greenhouse gas emissions, which have risen by
20% in the past decade [United Nations Conference on Trade and Development, 2023, Stuchtey et al.,
2023]. To meet its environmental targets, reducing emissions by 20% by 2030 and 70% by 2040, the
International Maritime Organization (IMO) prioritizes improvements in ship efficiency [International
Maritime Organisation, 2023].
However, these ambitions are complicated by an ageing global fleet, where over half of the vessels
are older than 15 years, making them difficult to retrofit yet premature for scrapping [United Nations
Conference on Trade and Development, 2023]. In the midst of these constraints, digitalisation and
AI offer transformative potential in areas such as route optimization, fuel efficiency, and predictive
maintenance [Katsoulakos et al., 2024]. While platforms like Maersk’s TradeLens and Rolls-Royce’s
autonomous ship initiatives have made strides, the industry’s complexity and regulatory hurdles
demand more scalable, integrated solutions accessible to a broad range of industry persona [Jovanovic
et al., 2022, Rolls-Royce Marine, 2016].
Key priorities include, seamless data integration across fragmented systems, real-time monitoring
for predictive maintenance, scalability for diverse fleets, and transparent adherence to regulatory
compliance across global frameworks [Katsoulakos et al., 2024]. Additionally, solutions must provide
automation and configurability to address the varied needs of industry personas without relying on
specialised expertise [O’Donncha et al., 2024].
AI Agents
Artificial Intelligence (AI) agents are systems designed to autonomously perform tasks by perceiving
their environment, making decisions, and executing actions to achieve specific goals. Recent advances
in large language models (LLMs) have significantly enhanced the capabilities of AI agents, enabling
them to handle more complex and dynamic tasks.
LLM-based AI agents can now plan and act by analysing tasks, formulating strategies, and adjusting
25

their actions based on feedback. This mirrors human problem-solving processes, allowing agents to
refine their approaches through self-critique and iterative improvements. For example, these agents
can autonomously search the web, solve mathematical problems, and even review and correct their
work, thereby increasing their effectiveness in various applications.
To manage these complex tasks, engineers are enhancing LLMs with additional modules that improve
memory, planning, and tool-utilisation capabilities. This development marks a shift from traditional,
monolithic AI models to more sophisticated, multicomponent systems. Such systems integrate various
functionalities, enabling AI agents to perform a broader range of tasks with greater autonomy and
adaptability.
Digital Twin for Green Shipping AI Agents
This case study introduces a digital twin for green shipping (DT4GS) framework that uses large
language model (LLM) agents to enhance automation and efficiency in the shipping industry [Timms
et al., 2025]. At its core, the system includes a central reasoning agent that breaks down complex tasks
into smaller, manageable steps and coordinates with specialised tools to carry them out. By using
natural language as the main interface, this approach allows different users—such as ship owners,
captains, engineers, and technicians—to interact with the digital twin in a simple and intuitive way.
Eachusercanqueryandexploreshipsystemsbasedontheirspecificneeds,withoutrequiringtechnical
expertise in AI or system modeling.
We developed a suite of tools specifically designed for industrial applications, enhancing agentic
decision-makingbyprovidingacomprehensiveviewofreal-timeshipoperationsalongwithcontextual
insights. These tools integrate structured information from a domain-specific knowledge graph,
real-time sensor data, and technical specifications, including potential failure data. By leveraging
LangGraph1, the framework’s modular and adaptable design allows it to meet diverse operational
requirements and significantly improve decision-making efficiency. LangGraph is a multi-agent
orchestration framework built on LangChain that we adopted to manage tool-using LLM agents in
DT4GS. A planner in LangGraph (or in similar LLM-based systems) is a critical component that
is responsible for task decomposition, decision-making, and execution sequencing. In AI agent
frameworks, planners allow agents to break down high-level objectives into manageable subtasks,
prioritise them, and decide in what order and manner those subtasks should be executed.
We demonstrate the capabilities of this framework on real-world shipping use cases, showcasing its
practical applicability and scalability. Figure 6 presents the pipeline that integrates agentic reasoning
with a domain-specific knowledge graph and contextual data to streamline the selection, refinement,
and execution of digital twin tasks. This framework allows the agent to leverage core digital twin
functionalities, including:
• Dataspace: A centralised repository encompassing sensor and operational data, providing a
comprehensive view of various ship operations.
• Knowledge Graph: A structured representation capturing the relationships between the vessel,
its components, and associated operational variables. The graph interconnects critical elements
such as the main engine, auxiliary engine, and cargo system with key variables like temperature,
pressure, and performance metrics, forming a network that reflects the vessel’s functional state.
• Model Builder: A system designed to handle the selection, construction, and refinement of
machine learning models tailored to specific task requirements. It ensures that predictive and
prescriptive analytics align with the operational goals of the digital twin.
1https://langchain-ai.github.io/langgraph/
26

Figure 6: The DT4GS Agent acts as a central orchestrator that coordinates specialized sub-agents
and tools to support key operational tasks. It includes a planning module that decomposes tasks and
delegatesthemtoappropriateagents(e.g.,anomalydetection,assethealth,shipassistant). Thememory
and reflection modules track context and assess system performance. On the left, agent resources such
as a data space, knowledge graph, and edge/cloud platforms provide contextual information. On the
right, agent tools perform domain-specific functions such as anomaly detection, FMEA, and reporting.
This modular, language-driven framework enables flexible, autonomous interaction with complex ship
systems.
• Edge Orchestration Engine: A component utilising the Linux Foundation’s Open Horizon2
to efficently manage the deployment and placement of containerised applications across a
distributed fleet of edge nodes. This enables real-time processing and decision-making close to
the data source.
Agents are equipped with a suite of external tools that extend their ability to interact with digital
twin resources and enhance their ability to observe, analyse, and act upon system states. These tools
include:
• IoT Tool: Facilitates integration with IoT-enabled systems, allowing the agent to retrieve and
process real-time sensor data.
• Knowledge Graph Tool: Grants agent access to a domain-specific knowledge graph, enabling
complexqueriesonshipoperations, assetrelationships, andhistoricaldataforenricheddecision
support.
• DataQualityTool: Conductsinitialdataqualityassessmentsbyevaluatingexpectedbehaviours,
identifying inconsistencies, and ensuring data integrity before further processing. Within an
agentic workflow, it can generate metrics on data quality, providing users with insights for
further refinement and iteration.
2https://lfedge.org/projects/open-horizon/
27

• Anomaly Detection Tool: An online unsupervised anomaly detection approach that leverages
an efficient formulation of the optimal transport (OT) problem in one dimension to detect
anomalies in noisy seasonal time series data (described further in Langbridge et al. [2024].
• Failure Modes and Effects Analysis (FMEA) Tool: FMEA is a systematic method that is used
to identify and assess possible failure modes within a system, process, or product. It focuses on
understanding the causes and effects of each failure mode and evaluating their potential impact
[Stamatis, 2003]. FMEA helps prioritise risks based on factors such as severity, occurrence,
and detectability, enabling preventive measures to be taken. Typical information included in an
FMEA consists of the component or system location, potential failure modes, causes of failure,
severity of the failure, and the resulting effects of the failure on the system. In industrial sectors
like shipping, Failure Mode and Effects Analysis (FMEA) is often mandated by classification
societies, including the American Bureau of Shipping [American Bureau of Shipping, 2015].
• Time series forecasting tool: Configures a time series forecasting model to analyse sensor
data identified by the agent. This enables predictive assessments of component health based
on historical data and relevant contributory features. The model can be deployed in zero-shot
mode for immediate inference or further fine-tuned using historical data for improved accuracy.
• Edge Orchestration Tool: Automates the generation of JSON policy documents to manage the
deployment of applications at the edge on a specific ship. Deployment decisions are based on
parameters such as ship name, geographic location, company affiliation, or integration with an
IoT tool, ensuring adaptive and policy-driven orchestration of edge computing resources.
• Work Order Generation Tool: Automates failure response planning by evaluating identified
anomalies and leveraging FMEA insights to suggest potential root causes and recommend
mitigation actions. This tool streamlines maintenance workflows and enhances predictive
maintenance strategies.
Deployment of the DT4GS Agent
Shipboardassetmanagementandmaintenancerequireastructuredworkflowthatintegratesdata-driven
diagnostics with AI-powered automation. This process involves data retrieval, model inference, results
visualisation, and actionable diagnosis. Agentic workflows facilitate an end-to-end solution, reducing
manual intervention while enhancing predictive capabilities for shipboard systems.
Figure 7 illustrates a modular agentic workflow for handling use cases such as these. The process
begins with a user prompt that the Planning Agent receives. This agent decomposes the prompt into a
series of subtasks and sends them to domain-specialized agents based on the nature of each task.
Each specialised agent—such as those for navigation, data exploration, failure analysis (FMEA),
and ship systems—has access to tailored tools and APIs required for task execution. Once an agent
completes its task, its output is returned to theRe-router, which assesses the response in the context of
the original goal. If additional actions are needed, theRe-routerinvokes further agents or returns the
final result.
This architecture supports sequential and iterative agent interactions, enabling the system to handle
complex, multi-step workflows with minimal human intervention. By encapsulating functionality into
modular agents and enabling flexible coordination, the framework offers a scalable and extensible
approach to digital twin interactions in maritime operations.
The entire workflow of extracting pertinent sensor data, deploying anomaly detection models,
diagnosing root causes is automated by the AI agent [Timms et al., 2024]. It is insightful to view the
trajectory or reasoning process adopted by the LLM to resolve the user query. Figure 8 presents the
28

Figure 7: Schematic of the agentic workflow using a planner–router architecture. The Planning Agent
parses the initial user prompt and assigns subtasks to specialized agents (e.g., Navigation, FMEA,
Ship Exploration). The Re-router coordinates execution flow by determining whether further steps are
needed, enabling iterative multi-agent collaboration.
trajectory including task decomposition, tool calling, and natural language understanding to resolve
the task.
Agent capabilities include: accurately identifying relevant IoT variables associated with asset
components (guided by a knowledge graph), detecting exogenous variables that may influence system
dynamics (leveraging pre-trained knowledge from an LLM), applying off-the-shelf anomaly detection
algorithms to these variables, and presenting the results to the user through visualisations or natural
language summaries.
The agent planner module processes the user query and decomposes it into a series of sub tasks. It
identifies pertinent tool calls and the associated arguments. For example, it identifies that it needs to
extract data related to the main engine so it correctly calls the toolget_data_knowledge_graphwith
the appropriate arguments forcomponentand,months_of_data.
The agent proceeds through four iterations of think-act-observe (TAO in AI agents’ parlance), to
accomplish required subtasks such as data retrieval, applying anomaly detection model, getting failure
modes and effects for the component, generating a visualisation and work order, and finally returning
all the information to the user. This highlights the powerful capabilities of AI agents in terms of
automation and user interaction in natural language.
Discussion and Conclusion
Decarbonising the shipping industry is a critical societal goal, with efficiency improvements through
digital twin technologies playing a key role in achieving it. However, the inherent complexity of ship
systems, vessel heterogeneity, and the diverse range of operational challenges make it difficult to scale
digital twin solutions, often requiring significant in-house data science expertise. Agentic LLMs,
when augmented with external tools, can significantly accelerate progress towards these objectives by
automating and streamlining decision-making processes across various ship types and operational
scenarios, making digital twin capabilities more scalable and accessible through a generic natural
language interface.
29

Figure8: Sampletrajectoryillustratingthestep-by-stepprocessofrespondingtoauserqueryregarding
anomalies in a ship engine. It demonstrates the integration of multiple tools—such as data retrieval,
anomaly detection, and failure mode analysis—to detect, visualize, and recommend maintenance
strategies. The process culminates in generating a work order based on detected anomalies, filtered by
external factors like speed and ambient pressure, ensuring informed decision-making for condition-
based maintenance.
This case study presented an agentic LLM-based framework for anomaly detection in shipping,
leveraging real-time data integration, knowledge graphs, and external tools to support complex
decision-making in industrial asset management. By evaluating on real-world data, we demonstrated
the ability to streamline the anomaly detection process, and provide contextual insights through
dynamic tool selection. This approach offers a scalable solution to the challenges of digitalisation in
themaritimesector,addressingissuessuchasmachinerydegradation,dataintegration,andoperational
efficiency. Future work will focus on enhancing explainability, improving tool orchestration, and
30

integrating additional predictive analytics to further support decarbonisation and automation efforts in
shipping.
Summary of ML Techniques in Aquaculture
To consolidate the chapter’s discussion of machine learning methods, Table 1 provides a structured
overview of key ML techniques currently applied or emerging in aquaculture. The table highlights
representative use cases, the primary benefits these models provide in operational or research settings,
and estimated Technology Readiness Levels (TRLs) based on reported deployments and commercial
maturity.
The techniques included span both traditional and deep learning models, along with recent advances
such as GNNs, LLMs, and AI agents. Additionally, the table includes foundational approaches in
time-series modelling, unsupervised learning, and Bayesian inference—methods particularly relevant
for data-scarce environments, uncertain decision contexts, or real-time predictive tasks.
By summarising these methods side by side, the table serves as a reference point for selecting
appropriate ML approaches depending on the complexity of the aquaculture system, data availability,
and deployment goals.
Table 1: Key machine learning techniques applied in aquaculture, including typical use cases, benefits,
and estimated TRLs based on current research and deployments.
ML Technique Application in Aquaculture Benefits TRL
CNNs Fish behavior and health moni-
toring via computer vision
Non-invasive, continuous visual
monitoring
6–8
GNNs Modelinginteractionsamongen-
vironmental and biological sys-
tems
Captures system connectivity
and spatial relationships
2–4
SVR Forecasting dissolved oxygen us-
ing satellite or sensor data
Site-specific, accurate environ-
mental predictions
7–8
LLMs Natural language interfaces, log
analysis, document summariza-
tion
Scalable knowledge extraction
across diverse sources
2–4
AI Agents Autonomous task execution and
adaptive response agents
Decision automation and re-
duced manual intervention
2–4
Random Forests /
Decision Trees
Classification and anomaly de-
tectioninwaterqualityorsensor
data
Robust predictions with explain-
able outputs
7–9
RNNs / LSTMs Time-series forecasting of DO,
temperature, or feeding needs
Handles temporal dependencies
in aquaculture processes
5–7
Unsupervised
Learning (e.g.,
Clustering)
Anomaly detection, behavior
clustering, farm typologies
Extracts structure without need-
ing labeled data
4–6
Bayesian Models Uncertainty-awareforecastingin
small or sparse datasets
Probabilistic modeling and un-
certainty quantification
3–5
Note:Technology Readiness Levels (TRLs) are indicative estimates based on literature, commercial trials, and reported
deployments.
31

6 Conclusions
Machinelearningisemergingasakeyenablerinthedigitaltransformationofaquaculture. Frompredic-
tive analytics and real-time decision support to autonomous monitoring and control, ML technologies
can enhance productivity, sustainability, and resilience across the value chain. However, realising this
potential depends on improved data infrastructure, model interpretability, and collaboration between
AI developers and aquaculture practitioners.
As aquaculture scales to meet global food demands, ML applications provide critical insights, from
optimising feeding schedules and monitoring water quality to predicting potential environmental
impacts. Emerging technologies such as Graph Neural Networks (GNNs), large language models
(LLMs), and AI agents are driving this shift, enhancing traditional aquaculture practices with data-
driven intelligence and paving the way for the digital twin’s role in real-time, predictive management.
The use of computer vision, for instance, enables continuous and non-invasive monitoring of fish
behaviour and health, providing an unprecedented level of observation that supports better decision-
making and aligns with sustainability goals. At the same time, GNNs offer promising capabilities
for modelling complex, interconnected systems, such as the relationships between water quality
parameters, fish behaviour, and external environmental factors, which are often difficult to capture
using conventional data analysis techniques.
LLMs and AI agents bring adaptability and scalability to the aquaculture industry. With their
broad applicability across diverse datasets and environments, LLMs or foundation models allow for
generalization, enabling aquaculture operations to adopt sophisticated AI solutions with minimal
fine-tuning. AIagents,ontheotherhand,facilitateautonomousdecision-makingprocesses,potentially
transforming daily operations and reducing dependency on manual interventions.
As aquaculture embraces the digital twin concept, the role of AI will expand further into predictive
analytics, real-time decision support, and complex ecosystem modelling, driving both operational
efficiency and environmental responsibility. Ultimately, the convergence of machine learning and
digital twin technology presents a robust framework for achieving sustainable, intelligent aquaculture
practices capable of meeting the needs of a growing population while preserving aquatic ecosystems
for future generations.
Acknowledgements
The research presented in this chapter was supported by multiple sources of funding and institutional
support. The work received funding from the European Union’s Horizon Europe Research and
Innovation programme under grant agreement no. 101157369.
The authors of Case Study 1 acknowledge project support and computing resources provided by
DeepSense, as well as funding from the Mitacs Accelerate program under grant IT33656.
ChristopherWhiddenissupportedbyaNaturalSciencesandEngineeringResearchCouncilofCanada
(NSERC) Discovery Grant (RGPIN-2021-02988).
The authors of Case Study 3 gratefully acknowledge support from the Horizon Europe programme
under grant agreement no. 101056799.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report.
32

arXiv preprint arXiv:2303.08774, 2023.
Mutiu A Adegboye, Abiodun M Aibinu, Jonathan G Kolo, Ibrahim Aliyu, Taliha A Folorunso, and
Sun-Ho Lee. Incorporating intelligence in fish feeding system for dispensing feed based on fish
feeding intensity.IEEE Access, 8:91948–91960, 2020.
Enrique Alvarez Fanjul, S Ciliberti, J Pearlman, Kirsten Wilmer-Becker, Pierre Bahurel, Fabrice
Ardhuin, Alain Arnaud, Kamyar Azizzadenesheli, Roland Aznar, M Bell, et al. Promoting best
practices in ocean forecasting through an operational readiness level.Frontiers in Marine Science,
11:1443284, 2024.
American Bureau of Shipping. Guidance notes on failure mode and effects analysis (fmea) for
classification. Technical report, American Bureau of Shipping, Texas, USA, 2015.
Ernesto Arandia, Fearghal O’Donncha, Sean McKenna, Seshu Tirupathi, and Emanuele Ragnoli. Sur-
rogate modeling and risk-based analysis for solute transport simulations.Stochastic Environmental
Research and Risk Assessment, pages 1–15, may 2018. ISSN 1436-3240. doi: 10.1007/s00477-018
-1549-6. URLhttp://link.springer.com/10.1007/s00477-018-1549-6.
Siska Armalivia, Zahir Zainuddin, Andani Achmad, and Muh Arief Wicaksono. Automatic counting
shrimp larvae based you only look once (yolo). In2021 International Conference on Artificial
Intelligence and Mechatronics Systems (AIMS), pages 1–4. IEEE, 2021.
Safa Ben Atitallah, Maha Driss, Wadii Boulila, and Henda Ben Ghézala. Leveraging deep learning
and iot big data analytics to support the smart cities development: Review and future directions.
Computer Science Review, 38:100303, 2020.
Muneeza Azmat, Malvern Madondo, Arun Bawa, Kelsey Dipietro, Raya Horesh, Michael Jacobs,
Raghavan Srinivasan, and Fearghal O’Donncha. Forecasting Soil Moisture Using Domain Inspired
Temporal Graph Convolution Neural Networks To Guide Sustainable Crop Management. In
IJCAI 2023, volume 6, pages 5897–5905, August 2023. doi: 10.24963/ijcai.2023/654. URL
https://www.ijcai.org/proceedings/2023/654. ISSN: 1045-0823.
Amadou Ba, Fearghal O’Donncha, Joern Ploennigs, and Muneeza Azmat. Efficient extraction of
insights at the edges of distributed systems. In2023 IEEE International Conference on Big Data
(BigData), pages 1610–1619. IEEE, 2023.
Ersan Batur and Derya Maktav. Assessment of surface water quality by using satellite images fusion
basedonpcamethodinthelakegala,turkey.IEEETransactionsonGeoscienceandRemoteSensing,
57(5):2983–2989, 2018.
Peter Bauer, Bjorn Stevens, and Wilco Hazeleger. A digital twin of earth for the green transition.
Nature Climate Change, 11(2):80–83, 2021.
Christophe Béné, Robert Arthur, Hannah Norbury, Edward H Allison, Malcolm Beveridge, Simon
Bush, Liam Campling, Will Leschen, David Little, Dale Squires, et al. Contribution of fisheries
and aquaculture to food security and poverty reduction: assessing the current evidence.World
development, 79:177–196, 2016.
KaifengBi,LingxiXie,HenghengZhang,XinChen,XiaotaoGu,andQiTian. Accuratemedium-range
global weather forecasting with 3d neural networks.Nature, 619(7970):533–538, 2023.
Avrim L Blum and Pat Langley. Selection of relevant features and examples in machine learning.
Artificial intelligence, 97(1-2):245–271, 1997.
33

Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx,
MichaelSBernstein,JeannetteBohg,AntoineBosselut,EmmaBrunskill,etal. Ontheopportunities
and risks of foundation models.arXiv preprint arXiv:2108.07258, 2021.
Boris Bonev, Thorsten Kurth, Christian Hundt, Jaideep Pathak, Maximilian Baust, Karthik Kashinath,
and Anima Anandkumar. Spherical fourier neural operators: Learning stable dynamics on the
sphere.arXiv preprint arXiv:2306.03838, 2023.
Samantha Bui, Lena Geitung, Frode Oppedal, and Luke T Barrett. Salmon lice survive the straight
shooter: A commercial scale sea cage trial of laser delousing.Preventive veterinary medicine, 181:
105063, 2020.
Meredith Burke, Jon Grant, Ramon Filgueira, and Tim Stone. Oceanographic processes control
dissolved oxygen variability at a commercial atlantic salmon farm: application of a real-time sensor
network.Aquaculture, 533:736143, 2021.
Kim Burt, Dounia Hamoutene, Gehan Mabrouk, Chris Lang, Thomas Puestow, Dwight Drover, Randy
Losier, and Fred Page. Environmental conditions and occurrence of hypoxia within production
cagesofatlanticsalmononthesouthcoastofnewfoundland.AquacultureResearch, 43(4):607–620,
2012.
Kewei Cai, Xinying Miao, Wei Wang, Hongshuai Pang, Ying Liu, and Jinyan Song. A modified
yolov3 model for fish detection based on mobilenetv1 as backbone.Aquacultural Engineering, 91:
102117, 2020.
Xinkai Cao, Yiran Liu, Jianping Wang, Chunhong Liu, and Qingling Duan. Prediction of dissolved
oxygen in pond culture water based on k-means clustering and gated recurrent unit neural network.
Aquacultural Engineering, 91:102122, 2020.
Andromachi Chatziantoniou, Spyros Charalampis Spondylidis, Orestis Stavrakidis-Zachou, Nikos
Papandroulakis, and Konstantinos Topouzelis. Dissolved oxygen estimation in aquaculture sites
usingremotesensingandmachinelearning.RemoteSensingApplications: SocietyandEnvironment,
28:100865, 2022.
Rui Chen, Xiang Wang, Weimin Zhang, Xiaoyu Zhu, Aiping Li, and Chao Yang. A hybrid cnn-lstm
model for typhoon formation forecasting.GeoInformatica, 23:375–396, 2019.
Ronan Cooney, Alex HL Wan, Fearghal O’Donncha, and Eoghan Clifford. Designing environmentally
efficient aquafeeds through the use of multicriteria decision support tools.Current Opinion in
Environmental Science & Health, 23:100276, 2021.
Emmanuel de Bezenac, Arthur Pajot, and Patrick Gallinari. Deep Learning for Physical Processes:
Incorporating Prior Scientific Knowledge.arxiv preprint arXiv:1711.07970, nov 2017. URL
http://arxiv.org/abs/1711.07970.
Austin Derrow-Pinion, Jennifer She, David Wong, Oliver Lange, Todd Hester, Luis Perez, Marc
Nunkesser, Seongjae Lee, Xueying Guo, Brett Wiltshire, et al. Eta prediction with graph neural
networksingooglemaps. InProceedingsofthe30thACMInternationalConferenceonInformation
& Knowledge Management, pages 3767–3776, 2021.
DestinE. Destination Earth, 2024. URLhttps://destination-earth.eu/.
Phoebe M. R. DeVries, T. Ben Thompson, and Brendan J. Meade. Enabling large-scale viscoelastic
calculations via neural network acceleration.Geophysical Research Letters, 44(6):2662–2669, mar
2017. ISSN 00948276. doi: 10.1002/2017GL072716. URLhttp://doi.wiley.com/10.1002/
2017GL072716.
34

Jeffrey Donahue, Lisa Anne Hendricks, Sergio Guadarrama, Marcus Rohrbach, Subhashini Venu-
gopalan, Kate Saenko, and Trevor Darrell. Long-term recurrent convolutional networks for visual
recognition and description. InProceedings of the IEEE conference on computer vision and pattern
recognition, pages 2625–2634, 2015.
JesperSörenDramsch. 70yearsofmachinelearning ingeoscience inreview.AdvancesinGeophysics,
61:1, 2020.
Aurelien Ducournau and Ronan Fablet. Deep learning for ocean remote sensing: an application of
convolutional neural networks for super-resolution on satellite-derived SST data. In2016 9th IAPR
Workshop on Pattern Recogniton in Remote Sensing (PRRS), pages 1–6. IEEE, dec 2016. ISBN
978-1-5090-5041-3. doi: 10.1109/PRRS.2016.7867019. URLhttp://ieeexplore.ieee.org/
document/7867019/.
EDITO. EDITO: European Digital Twin Ocean, 2024. URLhttps://www.edito.eu/.
Philippe Esling and Carlos Agon. Time-series data mining.ACM Computing Surveys (CSUR), 45(1):
1–34, 2012.
Hassan Ismail Fawaz, Germain Forestier, Jonathan Weber, Lhassane Idoumghar, and Pierre-Alain
Muller. Deep learning for time series classification: a review.Data Mining and Knowledge
Discovery, 33(4):917–963, 2019.
Arthur FA Fernandes, Eduardo M Turra, Erika R de Alvarenga, Tiago L Passafaro, Fernando B Lopes,
Gabriel FO Alves, Vikas Singh, and Guilherme JM Rosa. Deep learning image segmentation for
extraction of fish body measurements and prediction of body weight and carcass traits in nile tilapia.
Computers and electronics in agriculture, 170:105274, 2020.
JeromeFriedman,TrevorHastie,andRobertTibshirani.Theelementsofstatisticallearning.Number10.
Springer series in statistics New York, 2001.
John Cristian Borges Gamboa. Deep learning for time-series analysis.CoRR, abs/1701.01887, 2017.
URLhttp://arxiv.org/abs/1701.01887.
Girish S Gaude and Samarth Borkar. Fish detection and tracking for turbid underwater video. In2019
International Conference on Intelligent Computing and Control Systems (ICCS), pages 326–331.
IEEE, 2019.
Dimitra Georgopoulou, Charalabos Vouidaskis, and Nikos Papandroulakis. Swimming behavior as a
potential metric to detect satiation levels of european seabass in marine cages.Frontiers in Marine
Science, 11:1350385, 2024.
Dimitra G Georgopoulou, Eleftheria Fanouraki, Dimitris Voskakis, Nikos Mitrizakis, and Nikos
Papandroulakis. European seabass show variable responses in their group swimming features after
tag implantation.Frontiers in Animal Science, 3:997948, 2022.
Felix A Gers and E Schmidhuber. Lstm recurrent networks learn simple context-free and context-
sensitive languages.IEEE Transactions on Neural Networks, 12(6):1333–1340, 2001.
IreneGiardina. Collectivebehaviorinanimalgroups: theoreticalmodelsandempiricalstudies.HFSP
journal, 2(4):205–219, 2008.
H Charles J Godfray, John R Beddington, Ian R Crute, Lawrence Haddad, David Lawrence, James F
Muir, Jules Pretty, Sherman Robinson, Sandy M Thomas, and Camilla Toulmin. Food security: the
challenge of feeding 9 billion people.science, 327(5967):812–818, 2010.
35

Balakrishna Gokaraju, Surya S. Durbha, Roger L. King, and Nicolas H. Younan. A Machine Learning
Based Spatio-Temporal Data Mining Approach for Detection of Harmful Algal Blooms in the
Gulf of Mexico.IEEE Journal of Selected Topics in Applied Earth Observations and Remote
Sensing, 4(3):710–720, sep 2011. ISSN 1939-1404. doi: 10.1109/JSTARS.2010.2103927. URL
http://ieeexplore.ieee.org/document/5701668/.
Ian Goodfellow, Yoshua Bengio, and Aaron Courville.Deep learning. MIT press, 2016.
Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair,
Aaron Courville, and Yoshua Bengio. Generative adversarial networks.Communications of the
ACM, 63(11):139–144, 2020.
HongweiGuo,JinhuiJeanneHuang,XiaotongZhu,BoWang,ShangTian,WangXu,andYouquanMai.
Ageneralizedmachinelearningapproachfordissolvedoxygenestimationatmultiplespatiotemporal
scales using remote sensing.Environmental Pollution, 288:117734, 2021.
Robert D Guy, Marilyn L Fogel, and Joseph A Berry. Photosynthetic fractionation of the stable
isotopes of oxygen and carbon.Plant Physiology, 101(1):37–47, 1993.
Isabelle Guyon and André Elisseeff. An introduction to variable and feature selection.Journal of
machine learning research, 3(Mar):1157–1182, 2003.
Philipp Hähnel, Jakub Mareček, Julien Monteil, and Fearghal O’Donncha. Using deep learning to
extend the range of air pollution monitoring and forecasting.Journal of Computational Physics,
408:109278, 2020.
Fangfang Han, Junchao Zhu, Bin Liu, Baofeng Zhang, and Fuhua Xie. Fish shoals behavior
detection based on convolutional neural network and spatiotemporal information.IEEE Access, 8:
126907–126926, 2020.
Patrick Heimbach, Fearghal O’Donncha, Jose Maria Garcia-Valdecasas, Alain Arnaud, and Liying
Wan. Crafting the future: Machine learning for ocean forecasting.State of the Planet Discussions,
2024:1–11, 2024.
Tony Hey, Stewart Tansley, Kristin Tolle, et al.The fourth paradigm: Data-intensive scientific
discovery, volume 1. Microsoft Research, 2009.
Geoffrey E Hinton and Ruslan R Salakhutdinov. Reducing the dimensionality of data with neural
networks.science, 313(5786):504–507, 2006.
Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory.Neural computation, 9(8):
1735–1780, 1997.
Wu-Chih Hu, Hsin-Te Wu, Yi-Fan Zhang, Shu-Huan Zhang, and Chun-Hung Lo. Shrimp recognition
using shrimpnet based on convolutional neural network.Journal of Ambient Intelligence and
Humanized Computing, pages 1–8, 2020.
International Maritime Organisation. IMO strategy on reduction of GHG emissions from ships.
Technical report, International Maritime Organisation, 2023.
Scott C. James, Yushan Zhang, and Fearghal O’Donncha. A machine learning framework to
forecast wave conditions.Coastal Engineering, 137:1–10, jul 2018. ISSN 0378-3839. doi:
10.1016/J.COASTALENG.2018.03.004. URLhttps://www.sciencedirect.com/science/
article/pii/S0378383917304969.
36

Ganesh Jawahar, Benoît Sagot, and Djamé Seddah. What does bert learn about the structure of
language? InACL 2019-57th Annual Meeting of the Association for Computational Linguistics,
2019.
JaewoonJeongandCrawfordWRevie. Appropriatesamplingstrategiestoestimatesealiceprevalence
on salmon farms with low infestation levels.Aquaculture, 518:734858, 2020.
Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik
Narasimhan. Swe-bench: Can language models resolve real-world github issues?arXiv preprint
arXiv:2310.06770, 2023.
Marin Jovanovic, Nikola Kostić, Ina M Sebastian, and Tomaz Sedej. Managing a blockchain-based
platform ecosystem for industry-wide adoption: The case of tradelens.Technological Forecasting
and Social Change, 184:121981, 2022.
Nusret Karakaya and Fatih Evrendilek. Monitoring and validating spatio-temporal dynamics of
biogeochemical properties in mersin bay (turkey) using landsat etm+.Environmental monitoring
and assessment, 181:457–464, 2011.
Takis Katsoulakos, Georgia Tsiochantari, Fearghal O’Donncha, Eleftherios Kaklamanis, Allesandro
Maccari, and Marcin Mucharski. Shipping digital twin landscape. InState-of-the-Art Digital Twin
Applications for Shipping Sector Decarbonization, pages 1–25. IGI Global, 2024.
AbdulBaseerKhan,JennieKorus,TylerSclodnick,andChristopherWhidden. Applyingdeeplearning
to predict adverse environmental conditions in fish aquaculture pens. InOCEANS 2024-Halifax,
pages 1–8. IEEE, 2024.
Yong Hoon Kim, Seunghyun Son, Hae-Cheol Kim, Bora Kim, Young-Gyu Park, Jungho Nam, and
JongseongRyu. Applicationofsatelliteremotesensinginmonitoringdissolvedoxygenvariabilities:
A case study for coastal waters in korea.Environment international, 134:105301, 2020.
Dane Klinger and Rosamond Naylor. Searching for solutions in aquaculture: charting a sustainable
course.Annual Review of Environment and Resources, 37:247–276, 2012.
MD Krom, N Kress, S Brenner, and LI Gordon. Phosphorus limitation of primary productivity in the
eastern mediterranean sea.Limnology and Oceanography, 36(3):424–432, 1991.
Remi Lam, Alvaro Sanchez-Gonzalez, Matthew Willson, Peter Wirnsberger, Meire Fortunato,
Alexander Pritzel, Suman Ravuri, Timo Ewalds, Ferran Alet, Zach Eaton-Rosen, et al. Graphcast:
Learningskillfulmedium-rangeglobalweatherforecasting.arXivpreprintarXiv:2212.12794, 2022.
Abi Langbridge, Fearghal O’Donncha, James Rayfield, and Bradley Eck. Optimal transport for
efficient,unsupervisedanomalydetectiononindustrialdata. In2023IEEEInternationalConference
on Big Data (BigData). IEEE, 2024.
Abigail Langbridge, Fearghal O’Donncha, Amadou Ba, Fabio Lorenzi, Christopher Lohse, and
Joern Ploennigs. Causal temporal graph convolutional neural networks (CTGCN).arXiv preprint
arXiv:2303.09634, 2023.
Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner. Gradient-based learning applied to
document recognition.Proceedings of the IEEE, 86(11):2278–2324, 1998.
Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning.nature, 521(7553):436–444, 2015.
37

KM Lewis, BG Mitchell, GL Van Dijken, and KR Arrigo. Regional chlorophyll a algorithms in the
arctic ocean and their effect on satellite-derived primary production estimates.Deep Sea Research
Part II: Topical Studies in Oceanography, 130:14–27, 2016.
Peifeng Li, Pei Hua, Dongwei Gui, Jie Niu, Peng Pei, Jin Zhang, and Peter Krebs. A comparative
analysis of artificial neural networks and wavelet hybrid approaches to long-term toxic heavy metal
prediction.Scientific reports, 10(1):13439, 2020.
Xiu Li, Min Shang, Jing Hao, and Zhixiong Yang. Accelerating fish detection and recognition by
sharing cnns with objectness learning. InOCEANS 2016-Shanghai, pages 1–5. IEEE, 2016.
Pantelis Linardatos, Vasilis Papastefanopoulos, and Sotiris Kotsiantis. Explainable ai: A review of
machine learning interpretability methods.Entropy, 23(1):18, 2020.
JiangtaoLiu,ChaopengShen,FearghalO’Donncha,YalanSong,WeiZhi,HylkeEBeck,TaddBindas,
Nicholas Kraabel, and Kathryn Lawson. From rnns to transformers: benchmarking deep learning
architectures for hydrologic prediction.EGUsphere, 2025:1–21, 2025.
F Lopes, H Silva, JM Almeida, C Pinho, and Eduardo Silva. Fish farming autonomous calibration
system. InOCEANS 2017-Aberdeen, pages 1–6. IEEE, 2017.
David C Love, Edward H Allison, Frank Asche, Ben Belton, Richard S Cottrell, Halley E Froehlich,
Jessica A Gephart, Christina C Hicks, David C Little, Elizabeth M Nussbaumer, et al. Emerging
covid-19 impacts, responses, and lessons for building resilience in the seafood system.Global Food
Security, 28:100494, 2021.
Malvern Madondo, Muneeza Azmat, Kelsey Dipietro, Raya Horesh, Michael Jacobs, Arun Bawa,
Raghavan Srinivasan, and Fearghal O’Donncha. A swat-based reinforcement learning framework
for crop management. InAI4SG-23: The Workshop on Artificial Intelligence for Social Good at
AAAI 2023, 2023. Workshop presentation.
M Maksimovic. Greening the future: Green internet of things (g-iot) as a key technological enabler
of sustainable development.Internet of things and big data analytics toward next-generation
intelligence, pages 283–313, 2018.
Håkon Måløy, Agnar Aamodt, and Ekrem Misimi. A spatio-temporal recurrent network for salmon
feeding action recognition from underwater videos in aquaculture.Computers and Electronics in
Agriculture, 167:105087, 2019.
Arghya Mandal and Apurba Ratan Ghosh. Role of artificial intelligence (ai) in fish growth and health
status monitoring: a review on sustainable aquaculture.Aquaculture International, pages 1–30,
2023.
Kathy Maskell. The rise of machine learning in weather forecasting, June 2023. URLhttps:
//www.ecmwf.int/en/about/media-centre/science-blog/2023/rise-machine-learn
ing-weather-forecasting.
RJ Matear and AC Hirst. Long-term changes in dissolved oxygen concentrations in the ocean caused
by protracted global warming.Global Biogeochemical Cycles, 17(4), 2003.
Georges Matheron. Principles of geostatistics.Economic geology, 58(8):1246–1266, 1963.
Apostolia-MariaMavropoulou, VassiliosVervatis, andSarantisSofianos. Dissolvedoxygenvariability
in the mediterranean sea.Journal of Marine Systems, 208:103348, 2020.
38

Hussam El-Din Mohamed, Ali Fadl, Omar Anas, Youssef Wageeh, Noha ElMasry, Ayman Nabil, and
Ayman Atia. Msr-yolo: Method to enhance fish detection and tracking in fish farms.Procedia
Computer Science, 170:539–546, 2020.
Graham G Monkman, Kieran Hyder, Michel J Kaiser, and Franck P Vidal. Using machine vision to
estimate fish length from images using regional convolutional neural networks.Methods in Ecology
and Evolution, 10(12):2045–2056, 2019.
Takehiro Morimoto, Thi Thi Zin, and Toshiaki Itami. A study on abnormal behavior detection of
infected shrimp. In2018 IEEE 7th Global Conference on Consumer Electronics (GCCE), pages
291–292. IEEE, 2018.
S Karthik Mukkavilli, Daniel Salles Civitarese, Johannes Schmude, Johannes Jakubik, Anne Jones,
Nam Nguyen, Christopher Phillips, Sujit Roy, Shraddha Singh, Campbell Watson, et al. Ai
foundation models for weather and climate: Applications, design, and implementation.arXiv
preprint arXiv:2309.10808, 2023.
Rosamond L Naylor, Ronald W Hardy, Alejandro H Buschmann, Simon R Bush, Ling Cao, Dane H
Klinger, David C Little, Jane Lubchenco, Sandra E Shumway, and Max Troell. A 20-year
retrospective review of global aquaculture.Nature, 591(7851):551–563, 2021.
Fearghal O’Donncha and Jon Grant. Precision aquaculture.IEEE Internet of Things Magazine, 2(4):
26–30, 2019.
Fearghal O’Donncha, Yushan Zhang, Bei Chen, and Scott C. James. An integrated framework that
combines machine learning and numerical models to improve wave-condition forecasts.Journal of
Marine Systems, 186:29–36, oct 2018. ISSN 0924-7963. doi: 10.1016/J.JMARSYS.2018.05.006.
URLhttps://www.sciencedirect.com/science/article/pii/S0924796317304827.
Fearghal O’Donncha, Caitlin L Stockwell, Sonia Rey Planellas, Giulia Micallef, Paulito Palmes, Chris
Webb, Ramon Filgueira, and Jon Grant. Data driven insight into fish behaviour and their use for
precision aquaculture.Frontiers in Animal Science, 2:695054, 2021.
Fearghal O’Donncha, Yihao Hu, Paulito Palmes, Meredith Burke, Ramon Filgueira, and Jon Grant.
A spatio-temporal lstm model to forecast across multiple temporal and spatial scales.Ecological
Informatics, 69:101687, 2022.
Fearghal O’Donncha, John D Sheehan, Maroun Touma, Sofiane Zemouri, and Rob H High. Towards
intelligent ship-edge computing enabling automated configuration of ship models and adaptive
self-learning. InState-of-the-Art Digital Twin Applications for Shipping Sector Decarbonization,
pages 73–93. IGI Global, 2024.
Tina Oldham, Barbara Nowak, Malthe Hvas, and Frode Oppedal. Metabolic and functional impacts
of hypoxia vary with size in atlantic salmon.Comparative Biochemistry and Physiology Part A:
Molecular & Integrative Physiology, 231:30–38, 2019.
RolandOrucheandFearghalO’Donncha. Attention-baseddomainadaptationforecastingofstreamflow
in data-sparse regions.arXiv preprint arXiv:2302.05386, 2023.
Roland Oruche, Lisa Egede, Tracy Baker, and Fearghal O’Donncha. Transfer learning to improve
streamflow forecasts in data sparse regions.arXiv preprint arXiv:2112.03088, 2021.
Keiron O’shea and Ryan Nash. An introduction to convolutional neural networks.arXiv preprint
arXiv:1511.08458, 2015.
39

FearghalO’Donncha,AlbertAkhriev,BrunoFragoso,andJohnIcely. Forecastingclosuresonshellfish
farms using machine learning.Aquaculture International, 32(5):5603–5623, 2024.
Vassilis M Papadakis, Ioannis E Papadakis, Fani Lamprianidou, Alexios Glaropoulos, and Maroudio
Kentouri. Acomputer-visionsystemandmethodologyfortheanalysisoffishbehavior.Aquacultural
engineering, 46:53–59, 2012.
Lorena Parra, Gines Lloret, Jaime Lloret, and Miguel Rodilla. Physical sensors for precision
aquaculture: A review.IEEE Sensors Journal, 18(10):3915–3923, 2018.
K Raghu Sita Rama Raju and G Harish Kumar Varma. Knowledge based real time monitoring system
for aquaculture using iot. In2017 IEEE 7th international advance computing conference (IACC),
pages 318–321. IEEE, 2017.
Chengping Rao, Hao Sun, and Yang Liu. Physics informed deep learning for computational
elastodynamics without labeled data.arXiv preprint arXiv:2006.08472, 2020.
Hafiz Tayyab Rauf, M Ikram Ullah Lali, Saliha Zahoor, Syed Zakir Hussain Shah, Abd Ur Rehman,
andSyedAhmadChanBukhari. Visualfeaturesbasedautomatedidentificationoffishspeciesusing
deep convolutional neural networks.Computers and electronics in agriculture, 167:105075, 2019.
Mette Remen, Frode Oppedal, Thomas Torgersen, Albert K Imsland, and Rolf Erik Olsen. Effects of
cyclic environmental hypoxia on physiology and feed intake of post-smolt atlantic salmon: initial
responses and acclimation.Aquaculture, 326:148–155, 2012.
Mette Remen, Michael Sievers, Thomas Torgersen, and Frode Oppedal. The oxygen threshold for
maximal feed intake of atlantic salmon post-smolts is highly temperature-dependent.Aquaculture,
464:582–592, 2016.
Rolls-Royce Marine. Autonomous ships. the next step.Rolls-Royce plc, 2016.
David Rolnick, Priya L Donti, Lynn H Kaack, Kelly Kochanski, Alexandre Lacoste, Kris Sankaran,
Andrew Slavin Ross, Nikola Milojevic-Dupont, Natasha Jaques, Anna Waldman-Brown, et al.
Tackling climate change with machine learning.arXiv preprint arXiv:1906.05433, 2019.
Mohammadmehdi Saberioon and Petr Císař. Automated within tank fish mass estimation using
infrared reflection system.Computers and electronics in agriculture, 150:484–492, 2018.
Mohammadmehdi Saberioon, Asa Gholizadeh, Petr Cisar, Aliaksandr Pautsina, and Jan Urban.
Application of machine vision systems in aquaculture with emphasis on fish: state-of-the-art and
key issues.Reviews in Aquaculture, 9(4):369–387, 2017.
Wojciech Samek, Thomas Wiegand, and Klaus-Robert Müller. Explainable artificial intelligence:
Understanding,visualizingandinterpretingdeeplearningmodels.arXivpreprintarXiv:1708.08296,
2017.
Robin M Schmidt. Recurrent neural networks (rnns): A gentle introduction and overview.arXiv
preprint arXiv:1912.05911, 2019.
Violetta Shevchenko, Tuomas Eerola, and Arto Kaarna. Fish detection from low visibility underwater
videos. In2018 24th International Conference on Pattern Recognition (ICPR), pages 1971–1976.
IEEE, 2018.
Diomidis H Stamatis.Failure mode and effect analysis: FMEA from theory to execution. Quality
Press, 2003.
40

JonathanMStokes,KevinYang,KyleSwanson,WengongJin,AndresCubillos-Ruiz,NinaMDonghia,
Craig R MacNair, Shawn French, Lindsey A Carfrae, Zohar Bloom-Ackermann, et al. A deep
learning approach to antibiotic discovery.Cell, 180(4):688–702, 2020.
Martin R Stuchtey, Adrien Vincent, Andreas Merkl, Maximilian Bucher, Peter M Haugan, Jane
Lubchenco, and Mari Elka Pangestu. Ocean solutions that benefit people, nature and the economy.
InThe Blue Compendium: From Knowledge to Action for a Sustainable Ocean Economy, pages
783–906. Springer, 2023.
Abdelouahid Ben Tamou, Abdesslam Benzinou, Kamal Nasreddine, and Lahoucine Ballihi. Transfer
learning with deep convolutional neural network for underwater live fish recognition. In2018 IEEE
International Conference on Image Processing, Applications and Systems (IPAS), pages 204–209.
IEEE, 2018.
Alexander Timms, Abigail Langbridge, and Fearghal O’Donncha. Agentic anomaly detection for
shipping. InNeurIPS 2024 Workshop on Open-World Agents, 2024.
Alexander Timms, Abigail Langbridge, Antonis Antonopoulos, Antonis Mygiakis, Eleni Voulgari,
and Fearghal O’Donncha. Agentic ai for digital twin. InProceedings of the AAAI Conference on
Artificial Intelligence, volume 39, pages 29703–29705, 2025.
LewisTunstall,LeandroVonWerra,andThomasWolf.Naturallanguageprocessingwithtransformers.
" O’Reilly Media, Inc.", 2022.
AsafTzachor, OfirHendel, andCatherineERichards. Digitaltwins: asteppingstonetoachieveocean
sustainability?npj Ocean Sustainability, 2(1):16, 2023.
Kathy Tzilivakis. A tale of two oceans: Scientists are building digital twins of the ocean | Research
and Innovation.European Commission, February 2022. URLhttps://ec.europa.eu/resea
rch-and-innovation/en/horizon-magazine/tale-two-oceans-scientists-are-bui
lding-digital-twins-ocean.
United Nations Conference on Trade and Development. Review of maritime transport 2023. Annual
report, United Nations Conference on Trade and Development, New York, 2023.
Vladimir Vapnik.The nature of statistical learning theory. Springer, 2013.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. Attention is all you need.Advances in neural information processing
systems, 30, 2017.
SébastienVillon, DavidMouillot, MarcChaumont, EmilySDarling, GérardSubsol, ThomasClaverie,
and Sébastien Villéger. A deep learning method for accurate and fast identification of coral reef
fishes in underwater images.Ecological informatics, 48:238–244, 2018.
Dimitris Voskakis, Alexandros Makris, and Nikos Papandroulakis. Deep learning based fish length
estimation. an application for the mediterranean aquaculture. InOCEANS 2021: San Diego–Porto,
pages 1–5. IEEE, 2021.
Lilian Weng. LLM Powered Autonomous Agents, June 2023. URLhttps://lilianweng.github.
io/posts/2023-06-23-agent/. Section: posts.
Steffen Wiewel, Moritz Becher, and Nils Thuerey. Latent-space Physics: Towards Learning the
Temporal Evolution of Fluid Flow.arxiv preprint arXiv:1802.10123, feb 2018. URLhttp:
//arxiv.org/abs/1802.10123.
41

Christopher K Williams and Carl Edward Rasmussen.Gaussian processes for machine learning,
volume 2. MIT press Cambridge, MA, 2006.
Thomas Wolf, Clement Delangue, and Matthieu Lapeyre. Hugging Face to sell open-source robots
thanks to Pollen Robotics acquisition, May 2025. URLhttps://huggingface.co/blog/hugg
ing-face-pollen-robotics-acquisition.
StefanWolff,FearghalO’Donncha,andBeiChen. Statisticalandmachinelearningensemblemodelling
to forecast sea surface temperature.Journal of Marine Systems, 208:103347, 2020.
Yuteng Xiao, Hongsheng Yin, Yudong Zhang, Honggang Qi, Yundong Zhang, and Zhaoyang Liu. A
dual-stage attention-based conv-lstm network for spatio-temporal correlation and multivariate time
series prediction.International Journal of Intelligent Systems, 36(5):2036–2057, 2021.
Shi Xingjian, Z Chen, H Wang, D. Y. Yeung, W. K. Wong, and W. C. Woo. Convolutional LSTM
network: A machine learning approach for precipitation nowcasting. InAdvances in neural
information processing systems, pages 802–810, 2015. URLhttp://papers.nips.cc/paper
/5955-convolutional-lstm-network-a-machine-learning-approach-for-precipi
tation-nowcasting.
LingYang,YeqiLiu,HuihuiYu,XiaominFang,LihuaSong,DaoliangLi,andYingyiChen. Computer
vision models in intelligent aquaculture with emphasis on fish detection and behavior analysis: A
review.Archives of Computational Methods in Engineering, 28:2785–2816, 2021.
Yuting Yang, Junyu Dong, Xin Sun, Estanislau Lima, Quanquan Mu, and Xinhua Wang. A cfcc-lstm
model for sea surface temperature prediction.IEEE Geoscience and Remote Sensing Letters, 15(2):
207–211, 2017.
Jian Zhao, Zhaobin Gu, Mingming Shi, Huanda Lu, Jianping Li, Mingwei Shen, Zhangying Ye, and
Songming Zhu. Spatial behavioral characteristics and statistics-based kinetic energy modeling in
special behaviors detection of a shoal of fish in a recirculating aquaculture system.Computers and
Electronics in Agriculture, 127:271–280, 2016.
Jian Zhao, Weijun Bao, Fengdeng Zhang, Songming Zhu, Ying Liu, Huanda Lu, Mingwei Shen, and
Zhangying Ye. Modified motion influence map and recurrent neural network-based monitoring of
the local unusual behaviors for fish school in intensive aquaculture.Aquaculture, 493:165–175,
2018.
Shili Zhao, Song Zhang, Jincun Liu, He Wang, Jia Zhu, Daoliang Li, and Ran Zhao. Application of
machine learning in intelligent fish aquaculture: A review.Aquaculture, 540:736724, 2021.
Chao Zhou, Daming Xu, Lan Chen, Song Zhang, Chuanheng Sun, Xinting Yang, and Yanbo Wang.
Evaluationoffishfeedingintensityinaquacultureusingaconvolutionalneuralnetworkandmachine
vision.Aquaculture, 507:457–465, 2019.
42
