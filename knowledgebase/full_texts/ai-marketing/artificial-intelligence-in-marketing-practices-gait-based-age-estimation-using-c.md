---
title: 'Artificial Intelligence in Marketing Practices: Gait Based Age Estimation using CNNs'
url: https://doi.org/10.70917/ijcisim-2026-1855
category: ai-marketing
subcategory: framework
date: 2026-07
venue: International Journal of Computer Information Systems and Industrial Management Applications
authors:
- Murat Berksan
- Didem Ölçer
- Çağatay Berke Erdaş
source: openalex-oa
pdf_url: https://cspub-ijcisim.org/index.php/ijcisim/article/download/1855/2996
pages: 9
chars: 37913
fetched_at: '2026-11-08T20:02:25+00:00'
kb_version: 1
---

# Artificial Intelligence in Marketing Practices: Gait Based Age Estimation using CNNs

International Journal of Computer Information Systems and Industrial Management Applications
ISSN 2150-7988 V olume 18(11s) 2026 pp. 212-220

https://doi.org/10.70917/ijcisim-2026-1855
Article
ARTIFICIAL INTELLIGENCE IN
MARKETING PRACTICES: GAIT BASED
AGE ESTIMATION USING CNNS
Murat Berksan1, Didem Ölçer2, Çağatay Berke Erdaş3, Selay Ilgaz Sümer4 and Emre Sümer5,*
1Baskent University, Department of Computer Engineering, 06790, Ankara, Turkey.
Email: muratberksan@gmail.com
ORCID: https://orcid.org/0000-0002-1009-312X
2Baskent University, Department of Computer Engineering, 06790, Ankara, Turkey.
Email: dtokmak@baskent.edu.tr
ORCID: https://orcid.org/0000-0001-7736-1021
3Baskent University, Department of Computer Engineering, 06790, Ankara, Turkey.
Email: berdas@baskent.edu.tr
ORCID: https://orcid.org/0000-0003-3467-9923
4Baskent University, Department of Business Administration, 06790, Ankara, Turkey.
Email: silgaz@baskent.edu.tr
ORCID: https://orcid.org/0000-0003-1104-276X
5Baskent University, Department of Computer Engineering, 06790, Ankara, Turkey.
Email: esumer@baskent.edu.tr
ORCID: https://orcid.org/0000-0001-8502-9184
[*: Corresponding Author, E-mail: esumer@baskent.edu.tr]

Abstract: . Every day, new developments in technology significantly influence business activities, especially in marketing. This
study explores the application of artificial intelligence to marketing by evaluating how different Convolutional Neural Netwo rk
(CNN) architectures perform in gait -based age estimation, a key biometric feature for personalized marketing strategies, such as
targeted advertising and real-time consumer profiling. Using Gait Energy Image (GEI) representations and the OULP-Age dataset,
we benchmarked models including EfficientNetB7, RegNetY , CrossVIT, InceptionV3, and ResNet152. Among these, CrossVIT
achieved superior performance with a Mean Absolute Error (MAE) of 2.69 years, outperforming all previously published methods,
which typically report MAEs in the 3.7–8.4 range. These findings demonstrate the potential of gait-based deep learning approaches
not only for advancing intelligent, real -time marketing solutions but also for contributing to the broader field of computer vision,
illustrating how advanced neural architectures can effectively address complex behavioral biometric tasks in real-world scenarios.
Keywords: Artificial Intelligence, Marketing, Consumer, Gait, Age Estimation, Convolutional Neural Networks

1. Introduction
With the emergence of digitalization, significant changes have occurred in the world. The ongoing changes
around the world have begun to affect the activities of businesses significantly. Artificial intelligence (AI) along with
the related concepts such as  machine learning and deep learning which have started to be on the agenda frequently
with digitalization, especially in recent years, has brought about significant transformations in business activities. As
a matter of fact, nowadays, AI is being used in different sectors like manufacturing, education, law and business etc.
for different purposes such as analyzing, comprehending and in decision making [13]. As the use of AI becomes more
widespread, it is seen that it has started to gain an important place in marketing activities [30]. The use of AI has paved
the way for decisions regarding marketing activities to be made in an automated manner. In this way, the effectiveness

213
of marketing activities has increased by establishing relationships with consumers in the right way at the right time.
Especially when it is considered that 76% of consumers expect businesses to understand them, the importance of the
contributions that AI will bring to marketing activities can be easily understood [32].
Developments in communication and information technology and the use of AI have positive effects on the
analysis and processing of biometric data [4]. Biometric data is especially important for decision -makers in the
planning of personalized marketing activities [12]. Biometric identifiers are classified as physiological and behavioral
characteristics [18]. Human gait is a behavioral identifier and by using it as a cue, it is possible to overcome the
limitations of physiological identifiers. For example, ca pturing a fingerprint requires cooperation of the subject.
However, capturing human gait is achievable from larger distances and at low resolution which makes the utilization
of this trait desirable. Furthermore, these benefits of using gait as biometric i dentifier enable to analyze human
attributes in the wild [40].
 Human gait differs among age groups and several studies corroborate this argument. Grabiner, Biswas, and
Gabiner [11] proved that age affects the stride width. Correspondingly, Elble et al. [9] showed that as the age increases,
the walking speed and strid e decreases. Thus, the arm swinging, rotation of joints and the maximum amount of foot
height changes. These findings indicate that as the age differs, so does the gait patterns and therefore it is achievable
to deduce age based on human gait.
It is possible to leverage gait-based age estimation in different systems. For instance, a system that is set up on
a street may estimate age of pedestrians, which then can be used to display targeted advertisement on electronic
billboards. Another probable use case can be shown in criminal investigation field. In the case suspect’s face is not
visible, estimating the age may provide important information to the law enforcement. These cases exhibit that gait -
based age estimation can provide valuable information.
There have been various studies to infer age based on gait. While studies such as [2, 5, 7, 8, 27, 29, 44, 47] aim
classifying subjects into their age group, other studies [1, 14, 21 -25, 26, 28, 35, 37, 38 ,42, 43, 45, 46, 48] aim
estimating the age of the  subjects. Although these studies approach the problem in different ways, the general frame
is usually the same which consists of processing subject’s gait footage, feature extraction and classification/estimation.
There are two concepts of the processing step which are model -based and model -free [33]. Model -based
approaches target creating models from locomotion of body parts and model-free approaches focus on spatiotemporal
pattern of human gait, generally by forming representations from binary silhouettes. Even though both concepts have
their advantages and disadvantages, the ability to apply model-free approaches in real-time environments due to their
efficient nature has made them more appealing. Gait Energy Imag e (GEI) is among the most utilized representations
in model-free approaches [20]. It is constructed by converting gait footage into binary gait silhouettes, pinning the
frames that are in one gait cycle and averaging these frames. By doing so, a representa tion that can describe the
subject’s both locomotion and posture are obtained. Thus, this makes GEI an important gait feature descriptor.
However, it is important to note that the performance of the methods that rely on GEI are susceptible to the conditions
such as clothing and object carrying in the original footage [36].
The next steps are feature extraction and interpreting these features to reach a conclusion. To fulfill these steps,
the usability and the effectiveness of various learning methods were researched by previous studies. Additionally, the
choice of dataset is crucial in deep learning-based methods and the dataset needs to be balanced and extensive in order
to obtain unimpaired results.
A CNN, which is a hierarchical multilayered neural network, can extract features and do the learning directly
from the image. Recent studies have been giving a great deal of attention to CNN due its success on tackling harder
problems. In our study, the fe asibility of different CNN models which retrieve GEI as an input for gait -based age
estimation is explored with the aim of low mean absolute error (MAE) and median absolute error (MedAE). While
doing so, several different state -of-the-art deep learning mod els such as EfficientNetB7, RegnetY , CrossVIT,
InceptionV3 and ResNet152 were tested, and their performances were evaluated. Thus, this study provides guidance
on applying networks for the gait-based age estimation, a critical biometric identifier for marketing activities. Beyond
its implications for marketing, the methodological framework presented here is relevant to a wide range of computing
applications, including intelligent surveillance systems, adaptive human–computer interaction, and privacy-preserving
demographic analytics.
The rest of the paper is organized as follows. Section 2 elaborates on how AI technologies are transforming
marketing strategies and practices. Section 3 presents the gait dataset that was used for the experiments. Section 4
summarizes the configurations o f the CNN architectures used. Section 5 contains the performance metrics,

214
experimental results, and comparisons with previously published methods. Finally, section 6 concludes this study
along with the future research directions.
2. Artificial Intelligence in Marketing
In recent years, one of the most important issues in marketing activities is to establish and maintain healthy
relationships between businesses and customers. These established relationships ensure that consumers' expectations
can better be understood and products that meet consumers' needs and wants can be produced. Collecting and using
data related to their needs and wants at the right place and time is very important for the success of marketing activities.
The data used in the planning of marketing acti vities can be obtained from marketing research, market analysis and
competition intelligence. In addition to this, today developing technologies and communication tools have made it
easier to access various data about consumers [17]. This makes it easier to predict what the consumer wants and needs
[15].
            AI emerges as a crucial partner in marketing, which supports the automation, optimization, and
augmenting of three critical marketing processes: gathering data, generating insights through analysis, and engaging
with customers [17]. Thanks to the use of consumer data and customer profiles by AI tools, healthier communication
can be established with the target audience and communication can be established by creating tailored messages for
each consumer [32]. This is related to AI that have the ability to recognize faces and things. Thanks to AI technology,
businesses can make some recommendations to the consumers about the most suitable products that will meet their
demands and needs [16]. In short, analysis of large volumes of data have become ea sier with AI. Besides, it enables
valuable information to be delivered to consumers. Visitor activity is monitored to quickly display personalized ad
content. Data is continuously gathered and used to inform future changes in advertising materials. It faci litates easy
customer support. For marketing automation, AI applications in marketing play an important role. Furthermore, it
enables data to be processed at a level close to zero error and in a short time. Customer centered choices can be made
with the ability of AI to scan many different data points such as blogs and social media [13]. Thus, it is ensured that
the automated marketing campaigns organized by the businesses reach the right customers [16]. AI provides cost
savings in businesses as well. Various activities that are carried out by humans with intensive work can be carried out
in less time and at low costs with the integration of AI into marketing activities. In other words, the way to make fast
and effective decisions in businesses is through AI  [32]. Apart from these, in the customer segmentation algorithms
for clustering, such as k -means and hierarchical clustering, can successfully group customers based on their
demographic information, purchasing history, and online browsing patterns [31]. Th us, customer segmentation
activities can be carried out more effectively.
3. Data Set
This work utilized the OU -ISIR Gait Database, Large Population Dataset with Age (OULP -Age) [41]. It
contains GEI of 63,846 subjects and the footage of these subjects are recorded in front of a green screen thus the GEI
construction scheme is free from the external factors. An example of the constructed GEI can be seen in Fig. 1.

Fig. 1 An example of GEI in OULP-AGE
The subjects are aged between 2 and 90 years old. This tells that the dataset comprises of an entire generation.
Moreover, even though most of the subjects are between ages 6 and 50, the dataset is able to depict alterations that
occur between different age groups (Figure 2).

215

Fig. 2 Age distribution of the OULP-Age Dataset
The human gait is affected by the gender therefore the gender distribution may affect the age estimation and
there is a correlation between age and gender in terms of gait [25]. The dataset consists of 31,093 males and 32,753
females therefore the dataset is balanced in terms of gender.
The OULP-Age dataset is suitable for this work because a) the dataset is balanced in terms of age and gender
which is important because the ratio of the classes can affect the outcome of machine learning approaches, b) the
dataset is the largest one curren tly available which is one the keys to success in deep learning approaches and c) the
dataset consists of GEI which is composed in an environment that aids minimizing the errors that could occur during
GEI construction.
4. Methods and Evaluation
In this study, to estimate gait -based age, five CNN architectures were selected: EfficientNetB7, RegNetY ,
CrossVIT, InceptionV3 and ResNet152. These CNN architectures were selected due to the nature of the input data,
which are 2D spatial summaries of the temporal gait cycles. These image -based representations are more effectively
processed using CNNs, which are optimized for extracting spatial hierarchies and visual patterns.
EfficientNetB7 uses a compound scaling approach to optimize accuracy and efficiency. This model
systematically scales the depth, width, and resolution of the network, thus excelling in image classification tasks while
maintaining low computational costs [39].
RegNetY was developed for using a design space that automatically determines the optimal model
configurations. RegNetY focuses on efficient block design with channel scaling and bottleneck blocks, which ensures
high accuracy and low computational costs in large-scale image recognition tasks [3].
CrossVIT represents a variant of the Vision Transformer (VIT) model. It is designed to learn both local and
global features using multiple imaging windows at different scales. The parallel operation of image processors of
different sizes enables CrossVIT t o perform effectively in complex image analysis tasks. Moreover, its ability to
process complex data structures makes it particularly advantageous in various applications [6].
InceptionV3 was developed with the aim of improving the efficiency of deep learning models. It uses a parallel
combination of filters of different sizes to achieve high accuracy and minimize computational cost. It is a widely used
model for tasks such as image classification and object detection [34].
ResNet152 improves the trainability of ultra -deep networks by including residual blocks. This network,
consisting of 152 layers, addresses the gradient loss problem through bypass connections, thereby improving the
accuracy of deep models. It is frequently  chosen for tasks such as large -scale image classification and feature
extraction [19].

216
These architectures were designed for classification purposes. To perform regression for age estimation, the last
fully connected layers of these architectures were altered to have one unit with linear function.
We used a 5 -fold cross -validation approach to evaluate model performance. The dataset was randomly
partitioned into five equal subsets, ensuring an even distribution of age and gender across folds. Each model was
trained on four folds and validated on the remaining fold, repeated five times to compute the average performance. To
prevent data leakage, care was taken to ensure that no GEI samples from the same individual appeared in both training
and validation sets. Additionally, the models were trained using a learning rate of 0.01 for 30 epochs.
To evaluate the performance of the models used for age estimation in the relevant study, evaluation metrics
such as Correlation Coefficient, Determination Coefficient, Median Absolute Error, Mean Absolute Error and Root
Mean Square Error were used [10].
The Correlation Coefficient (R) is one of the measures that help to determine how closely related the actual
values and the values predicted by the model are. It takes on a value between -1 and 1 where 1 and -1 show perfect
correlation in a linear regression while 0 shows no linear correlation. A perfect positive linear relationship has a value
of +1 while a perfect negative linear relationship has a value of -1. This means that a value of zero indicates that there
is no linear relationship between the two variables in question.
The Determination Coefficient (R2) shows the proportion of variance in the dependent variable that is explained
by the independent variables. It takes on values between 0 and 1 where a value of 1 show that the model can accurately
predict the dependent var iable. R² statistic shows the how closely the model’s predicted values are to the actual
observed values.
The Root Mean Square Error (RMSE) is calculated by first squaring each of the residuals and then computing
the square root of the average value of these squared residuals Eq. 1). RMSE pays more attention to the size of the
errors and is also quite sensitiv e to large errors as well. Hence, it is used when precision is an important factor in
assessing the performance of the model.
𝑅𝑀𝑆𝐸 =  √1 𝑛⁄ ∑(𝑦𝑖 − 𝑦̂𝑖)2
𝑛
𝑖=1
 (1)

The Median Absolute Error (MedAE) indicates the middle of the absolute differences between the estimated
and real targets (Eq. 2). Thus, MedAE is a more stable error measure as it is not influenced greatly by outliers and is
used to minimize the influence of these on the data set.
𝑀𝑒𝑑𝐴𝐸 =  𝑀𝑒𝑑𝑖𝑎𝑛(|𝑦𝑖 − 𝑦̂𝑖|) (2)

The Mean Absolute Error (MAE) represents the mean of the absolute differences between the predicted and
actual values (Eq. 3). Unlike metrics that square the differences, such as the RMSE, MAE assigns equal weight to all
individual errors, providing a straightforward and interpretable measure of the model’s predictive.
𝑀𝐴𝐸 =  1 𝑛⁄ ∑|𝑦𝑖 − 𝑦̂𝑖|
𝑛
𝑖=1
 (3)
5. Results and Discussion
Table 1 illustrates the age estimation regression performance of the employed models. Accordingly, the
CrossVIT model demonstrates superior performance in all metrics and reached the values of 0.9505, 0.9034, 1.4758,
2.6854, 4.8135 for R, R2, MedAE, MAE,  RMSE metrics, respectively. Although EfficientNetB7, RegNetY models
fall behind the performance of the CrossVIT model, they have reached promising performances. While the
performance achieved for the EfficientNetB7 model is 0.9319, 0.8685, 1.9122, 3.3912, 5.6156 for the same evaluation
metrics, respectively; these values are measured as 0.9301, 0.8651, 2.0398, 3.5632, 5.6877 for the RegNetY model.
While the InceptionV3 model exhibited superior performance to the ResNet152 model, these two models
demonstrated the lowest performance.
Table 1 The experimental results

217
 R R2 MedAE MAE RMSE
EfficientNetB7 0.9319 0.8685 1.9122 3.3912 5.6156
RegnetY 0.9301 0.8651 2.0398 3.5632 5.6877
CrossVIT 0.9505 0.9034 1.4758 2.6854 4.8135
Inception V3 0.9058 0.8205 2.0082 4.0187 6.5608
ResNet152 0.8751 0.7657 2.5940 4.7318 7.4951
The variations in the performance of the models can be explained by architectural complexity, feature
representation, and learning ability. For instance, CrossVIT can learn dependencies better with the help of VIT based
approaches. This makes it easier for the model to capture relationships in regression tasks and this way low errors can
be realized. Other models like EfficientNetB7 and RegNetY are the modern CNN architectures which have been
developed with a focus on parameter and computational efficiency.  These models have a well-balanced performance
in terms of the accuracy and the errors as well. Although ResNet152 has a very complex network architecture, too
many layers may cause a problem known as  ‘gradient fading’ thus decreasing the performance of the network.
CrossVIT can make more general and accurate predictions as it has the capacity to learn the local and the global
features at the same time. This enhances the R-score and minimizes the errors. InceptionV3 employs multi-scale filters
for feature extraction. But this approach may not be able to identify some complex features at times, which may result
in relatively higher error rates. RegNetY possesses a flexible modular architecture in feature extraction. Such choice
of the layer width and the number of channels ensures that the model learns features in the most efficient manner. This
makes the ResNet152 capable of extracting high -level features given that there are numerous layers but may
compromise on the generality of features in some cases.
The comparison of the result obtained with CrossVIT and the existing studies in the literature are shown in
Table 2.
Table 2 Comparison of the gait based age estimation methods
Method MAE
[45] 6.27
[37] 5.84
[38] 5.79
[48]
[1]
[42]
[43]
5.12
3.70
5.43
8.39
CrossVIT (Our result) 2.69
The results of the compared methods were obtained by training on OULP -Age dataset and all these methods
utilize a deep learning approach. The CrossVIT method in this study outperforms the method proposed in [38] which
utilizes gender and age group information that is extracted before the age estimation. Furthermore, CrossVIT has also
achieved much better results than the network that is proposed in [37] which is based on DenseNet. Similarly, the
CrossVIT method outperforms GL-CNN that was proposed in study [48] in terms of MAE. GL-CNN is composed of
multiple CNN architectures to extract information from both local parts of the GEI and the GEI as whole. Moreover,
although an age and gender -based approach proposed by Abirami et al. [1] achieved the closest performance to
CrossVIT, it fell short of the CrossVIT model. Finally, CrossVIT model outperforms the two more recent studies
conducted by Xu et al. [43] and Xu et al. [42]. The former one is based on an uncertainty -aware gait-based approach,
while the lat ter includes a real -time CNN framework from a single image. Like CrossVIT, other two approaches,
EfficientNetB7 and RegNetY presented in the study, have achieved more successful results than the current literature.

218
These results illustrate the effectiveness of combining transformer-based and convolutional approaches for structured
visual data, highlighting a pathway for the development of next -generation hybrid architectures, which is an area of
significant interest in contemporary computing research.
6. Conclusion and Future Work
The developments in technology have made significant contributions to the businesses' ability to continue their
existence in a competitive environment. The dizzying speed of technology has significantly affected the marketing
activities of the companies. T echnology has opened the doors for marketing managers to access the data they need
faster and more efficiently.
Considering the fierce competitive environment, it would not be wrong to say that data is an important key for
businesses to achieve successful activities. Decision makers in marketing are constantly flooded with large volumes
of data. At this point, artif icial intelligence aids them by leveraging predictive analytics by efficiently gathering and
interpreting these data. Besides, the use of AI in marketing has paved the way for personalization.
This study explored the use of various CNN architectures for gait -based age estimation using Gait Energy
Images (GEIs), with CrossVIT emerging as the most effective model across multiple evaluation metrics. The proposed
approach not only achieves state -of-the-art performance but also highlights the potential of leveraging behavioral
biometrics in data -driven decision -making. The best performing CrossVIT model is a variation of the VIT model
designed to capture both fine-grained (local) movements such as joint rotations and broader (global) gait patterns like
stride length by utilizing image windows of different scales. Its parallel processing of varied window sizes allows it
to model complex age-related characteristics more effectively than traditional CNNs. This hybrid attention mechanism
enhances its sensitivity to nuanced motion cues that correlate with age. The second -best solution, EfficientNetB7
employs a compound scaling method to enhance both accuracy and efficiency by proportionally adjusting the
network's depth, width, and resolution. This enables it to achieve high performance in image classification tasks while
keeping computational costs low. The third-best solution, RegNetY is designed with an automated approach to identify
optimal model configur ations. It emphasizes efficient block design using channel scaling and bottleneck blocks,
achieving high accuracy and low computational costs for large-scale image recognition tasks.
Beyond technical contributions, this research has practical implications for marketing practices. Accurate age
estimation through non -intrusive gait analysis enables businesses to deliver personalized content in public
environments—such as targeted advertisements on digital billboards—or tailor in-store experiences based on customer
demographics. These capabilities contribute to more effective consumer segmentation, real -time profiling, and data -
informed campaign strategies, all while preserving user anonym ity. From a computing perspective, the proposed
approach exemplifies how advances in deep neural architectures can be translated into practical, scalable solutions
that bridge research and application.
Despite promising results, several limitations must be acknowledged. First, although the OULP -Age dataset
provides high-quality GEI images with minimal background noise, it does not include labeled metadata for walking
speed or clothing conditions. Therefo re, the model’s robustness across such variations could not be assessed in this
study. Future work will involve evaluating the models on more diverse datasets (e.g., CASIA -B or TUM -GAID),
which include covariates such as carrying conditions, walking speeds , and clothing changes. Additionally, while the
OULP-Age dataset is extensive and balanced, any model trained on a specific demographic distribution may exhibit
biases when applied across different cultures, postures, or age ranges. Finally, the model’s in terpretability, though
addressed using quantitative metrics, could benefit from further exploration through visual explanations or explainable
AI techniques.
Future research could address these limitations by incorporating multimodal data (e.g., gait + facial cues or
skeletal tracking), testing on in -the-wild datasets, and refining interpretability using saliency maps or attention
visualizations. Further, utilizing more advanced transformer-based architectures or hybrid models that combine CNNs
and vision transformers may refine the ability to capture local and global features. With these improvements businesses
will likely continue to experience significant imp acts from emerging technological advancements. Artificial
intelligence, as one of the most prominent technological developments, will play a pivotal role in this transformation.
Author Contributions: M.B. contributed to the research investigation, formal analysis, methodology, and
original draft. Ç.B.E. and D.Ö. conducted the experimentation and data reporting. S.I.S. conceptualized the study and
contributed to the original draft. E.S. contributed to t he original draft, reviewed the manuscript, and supervised the
whole study.

219
Funding: There is no external funding support for this work.
Clinical Trial Number: not applicable.
Consent for Publication: not applicable.
Ethics Approval and Consent to Participate: not applicable.
Conflict of Interest: The authors declare that they have no conflict of interest.
Data Availability: The data that support the findings of this study are available from the Institute of Scientific
and Industrial Research (ISIR), Osaka University (OU) but restrictions apply to the availability of these data, which
were used under license for the current s tudy, and so are not publicly available. However, data can be provided by
Prof. Yasushi Yagi [Yagi Laboratory, Department of Intelligent Media] through mail
(GaitDB_admin@am.sanken.osaka-u.ac.jp) or alternatively by filling the Release Agreement in
[http://www.am.sanken.osaka-u.ac.jp/BiometricDB/GaitLPAge.html] (upon request).
References
1. Abirami B, Subashini TS, Mahavaishnavi V (2020) Automatic age -group estimation from gait energy images. Mater
Today Proc 33:4646-4649. doi:10.1016/j.matpr.2020.08.298
2. Al Musalhi N, Celebi E (2024) Advanced age group estimation using gait analysis: A novel multi -energy image and
invariant moments method. Trait Signal 41(2):879-889. doi:10.18280/ts.410228
3. Alam TM, et al. (2022) An efficient deep learning -based skin cancer classifier for an imbalanced dataset. Diagnostics
(Basel) 12(9):2115. doi:10.3390/diagnostics12092115
4. Awad AI, Babu A, Barka E, Shuaib K (2024) AI-powered biometrics for Internet of Things security: A review and future
vision. J Inf Secur Appl 82:2214-2226
5. Begg RK, Palaniswami M, Owen B (2005) Support vector machines for automated gait classification. IEEE Trans
Biomed Eng 52(5):828-38. doi:10.1109/TBME.2005.845241
6. Chandrasiri MDN, Talagala PD (2023) Cross-ViT: Cross-attention vision transformer for image duplicate detection. 2023
8th Int Conf Inf Technol Res (ICITR) p. 1-6. doi:10.1109/ICITR61062.2023.10382916
7. Chuen BKY , Connie T, Song OT, Goh M (2015) A preliminary study of gait-based age estimation techniques. APSIPA
Proc p. 800-806. doi:10.1109/APSIPA.2015.7415382
8. Davis JW (2001) Visual categorization of children and adult walking styles. Proc Third Int Conf Audio Video -Based
Biometric Person Authentication p. 295-300. doi:10.1007/3-540-45344-X_43
9. Elble R, Thomas SS, Higgins C, Colliver J (1991) Stride -dependent changes in gait of older people. J Neurol 238(1):1 -
5. doi:10.1007/BF00319700
10. Erdas ÇB, Sümer E (2023) A fully automated approach involving neuroimaging and deep learning for Parkinson’s disease
detection and severity prediction. PeerJ Comput Sci 9:e1485. doi:10.7717/peerj-cs.1485
11. Grabiner PC, Biswas ST, Grabiner MD (2001) Age-related changes in spatial and temporal gait variables. Arch Phys Med
Rehabil 82(1):31-35. doi:10.1053/APMR.2001.18219
12. Gupta T, Bansal S (2023) Biometric data usage in personalized marketing: Balancing innovation and privacy. J Mark
Supply Chain Manag 2(3):1-7.
13. Haleem A, Javaid M, Qadri MA, Singh RP, Suman R (2022) Artificial intelligence (AI) applications for marketing: A
literature-based study. Int J Intell Netw 3:119-132
14. Hofmann M, Geiger J, Bachmann S, Schuller B, Rigoll G (2014) The TUM gait from audio, image and depth (GAID)
database: Multimodal recognition of subjects and traits. J Vis Commun Image Represent 25(1):195 -206.
doi:10.1016/J.JVCIR.2013.02.006
15. HRD V , Nayak T, Shahare P, Singh PK (2022) Role of artificial intelligence in marketing and customer relationship
management: A quantitative investigation of recent practices. Int J Food Nutr Sci 11(1):912-924
16. Ibrahim MK, Muhammed A, Ahmed S (2023) Artificial intelligence in marketing: A theoretical overview from a
developing economy. Austin J Bus Adm Manag 7(3):1064-1068
17. Jabeen M (2022) The use of AI in marketing: Its impact and future. World J Adv Res Rev 16(3):730-733
18. Jain AK, Bolle R, Pankanti S (1998) Biometrics: Personal identification in networked society. Kluwer Academic
Publishers
19. Jain N, Peddi P (2023) Gender classification model based on the ResNet 152 architecture. 2023 IEEE Int Carnahan Conf
Secur Technol (ICCST) p. 1-7. doi:10.1109/ICCST59048.2023.10474266
20. Ju H, Bhanu B (2006) Individual recognition using gait energy image. IEEE Trans Pattern Anal Mach Intell 28(2):316 -
322. doi:10.1109/TPAMI.2006.38
21. Li X, Makihara Y , Xu C, Yagi Y , Ren M (2019) Make the bag disappear: Carrying status-invariant gait-based human age
estimation using parallel generative adversarial networks. BTAS'19: Proc 10th IEEE Int Conf Biometrics Theory Appl
Syst Tampa, FL, USA

220
22. Li X, Makihara Y , Xu C, Yagi Y , Ren M (2018) Gait-based human age estimation using age group -dependent manifold
learning and regression. Multimed Tools Appl 77(21):28333-28354. doi:10.1007/s11042-018-6049-7.
23. Livne M, Sigal L, Troje NF, Fleet DJ (2012) Human attributes from 3D pose tracking. Comput Vis Image Underst
116(5):648-660. doi:10.1016/J.CVIU.2012.01.003
24. Lu J, Tan YP (2010a) Cost-sensitive subspace learning for human age estimation. Proc 2010 IEEE Int Conf Image Process
p. 1593-1596. doi:10.1109/ICIP.2010.5650873
25. Lu J, Tan YP (2010b) Gait -based human age estimation. IEEE Trans Inf Forensics Secur 5(4):761 -770.
doi:10.1109/TIFS.2010.2069560
26. Lu J, Tan YP (2013) Ordinary preserving manifold analysis for human age and head pose estimation. IEEE Trans Hum
Mach Syst 43(2):249-258. doi:10.1109/TSMCC.2012.2192727
27. Makihara Y , Mannami H, Yagi Y (2011) Gait analysis of gender and age using a large-scale multi-view gait database.
Proc 10th Asian Conf Comput Vis p. 440-451. doi:10.1007/978-3-642-19309-5_34
28. Makihara Y , Okumura M, Iwama H, Yagi Y (2011) Gait-based age estimation using a whole -generation gait database.
Proc 2011 Int Jt Conf Biometrics (IJCB'11) p. 1-6. doi:10.1109/IJCB.2011.6117531
29. Mansouri N, Issa MA, Jemaa YB (2018) Gait features fusion for efficient automatic age classification. IET Comput Vis
12(1):69-75. doi:10.1049/iet-cvi.2017.0055
30. Masnita Y , Ali JK, Zahra A, Wilson N, Murwonugroho (2024) Artificial intelligence in marketing: Literature review and
future research agenda. J Syst Manag Sci 14(1):120-140
31. Murthy A, Mamoria P, Kumar R, Shrivastava S, Thomas SK (2023) Artificial intelligence and machine learning in
marketing: A review of recent advances and future trends. Eur Chem Bull 12(8):3517-3528
32. Nalini K, Radhakrishnan P, Yogi G, Santhiya S, Harivardhini V (2021) Impact of artificial intelligence (AI) on marketing.
Int J Aquat Sci 12(2):3159-3167
33. Nixon MS, Carter JN (2006) Automatic recognition by gait. Proc IEEE 94(11):2013 -2024.
doi:10.1109/JPROC.2006.886018
34. Ogundokun RO, Abdulahi AT, Adenike AR, Babatunde AN, Babatunde RS (2023) Inception V3 based approach for the
recognition of age-related macular degeneration disease. 2023 Int Conf Sci Eng Bus Sustain Dev Goals (SEB -SDG) p.
1-7. doi:10.1109/SEB-SDG57117.2023.10124539
35. Punyani P, Gupta R, Kumar A (2018) Human age-estimation system based on double-level feature fusion of face and gait
images. Int J Image Data Fusion 9(3):222-236. doi:10.1080/19479832.2018.1423644
36. Rida I, Jiang X, Marcialis GL (2016) Human body part selection by group lasso of motion for model-free gait recognition.
IEEE Signal Process Lett 23(1):154-158. doi:10.1109/LSP.2015.2507200
37. Sakata A, Makihara Y , Takemura N, Muramatsu D, Yagi Y (2019) Gait-based age estimation using a DenseNet. Lect
Notes Comput Sci (LNCS) 11367:55-63. doi:10.1007/978-3-030-21074-8_5
38. Sakata A, Takemura N, Yagi Y (2019) Gait-based age estimation using multi -stage convolutional neural network. IPSJ
Trans Comput Vis Appl 11(1). doi:10.1186/s41074-019-0054-2
39. Singh R, Gupta S, Bharany S, Almogren A, Altameem A, Ur Rehman A (2024) Ensemble deep learning models for
enhanced brain tumor classification by leveraging ResNet50 and EfficientNet-B7 on high-resolution MRI images. IEEE
Access 12:178623-178641. doi:10.1109/ACCESS.2024.3494232
40. Verlekar TT, Soares LD, Correia PL (2018) Gait recognition in the wild using shadow silhouettes. Image Vis Comput
76:1-13. doi:10.1016/j.imavis.2018.05.002
41. Xu C, Makihara Y , Ogi G, Li X, Yagi Y , Lu J (2017) The OU-ISIR gait database comprising the large population dataset
with age and performance evaluation of age estimation. IPSJ Trans Comput Vis Appl 9(1):24. doi:10.1186/s41074-017-
0035-2
42. Xu C, Makihara Y , Liao R, Niitsuma H, Li X, Yagi Y , Lu J (2021) Real-time gait -based age estimation and gender
classification from a single image. Proc IEEE/CVF Winter Conf Appl Comput Vis (WACV). p. 3460-3470
43. Xu C, Sakata A, Makihara Y , Takemura N, Muramatsu D, Yagi Y , Lu J (2021) Uncertainty -aware gait -based age
estimation and its applications. IEEE Trans Biom Behav Ident Sci 3(4):479-494. doi:10.1109/TBIOM.2021.3080300
44. Zaki MH, Sayed T (2014) Using automated walking gait analysis for the identification of pedestrian attributes. Transp
Res Part C Emerg Technol 48:16-36. doi:10.1016/J.TRC.2014.08.004
45. Zhang S, Wang Y , Li A (2019) Gait-based age estimation with deep convolutional neural network. Proc Int Conf
Biometrics (ICB) p. 1-8. doi:10.1109/ICB45273.2019.8987240
46. Zhang Y , Huang Y , Wang L, Y u S (2019) A comprehensive study on gait biometrics using a joint CNN-based method.
Pattern Recognit 93:228-236. doi:10.1016/j.patcog.2019.04.023
47. Zhang D, Wang Y , Bhanu B (2010) Age classification based on gait using HMM. Proc 2010 20th Int Conf Pattern
Recognit (ICPR) p. 3834-3837. doi:10.1109/ICPR.2010.934
48. Zhu H, Zhang Y , Li G, Zhang J, Shan H (2019) Ordinal distribution regression for gait -based age estimation. arXiv
preprint Available from: http://arxiv.org/abs/1905.11005
