---
title: 'BN-AuthProf: Benchmarking Machine Learning for Bangla Author Profiling on Social Media Texts'
url: https://arxiv.org/abs/2412.02058
category: social-media
subcategory: empirical
date: 2024-12
venue: ''
authors:
- Raisa Tasnim
- Mehanaz Chowdhury
- Md Ataur Rahman
source: arxiv
pdf_url: https://arxiv.org/pdf/2412.02058
pages: 7
chars: 37233
fetched_at: '2026-11-08T13:02:45+00:00'
kb_version: 1
---

# BN-AuthProf: Benchmarking Machine Learning for Bangla Author Profiling on Social Media Texts

DRAFT COPY : Accepted to be Published in 2024 27th International Conference on Computer and Information Technology (ICCIT)
BN-AuthProf: Benchmarking Machine Learning for
Bangla Author Profiling on Social Media Texts
Raisa Tasnim
Dept. of CSE , Premier University
Chittagong, Bangladesh
raisatasnim14@gmail.com
Mehanaz Chowdhury
Dept. of CSE , Premier University
Chittagong, Bangladesh
mehanaz.chy09@gmail.com
Md Ataur Rahman
ESSI, Universitat Polit`ecnica de Catalunya
Barcelona, Spain
md.ataur.rahman@upc.edu
Abstract—Author profiling, the analysis of texts to uncover
attributes such as gender and age of the author, has become
essential with the widespread use of social media platforms.
This paper focuses on author profiling in the Bangla language,
aiming to extract valuable insights about anonymous authors
based on their writing style on social media. The primary
objective is to introduce and benchmark the performance of
machine learning approaches on a newly created Bangla Author
Profiling dataset, BN-AuthProf 1. The dataset comprises 30,131
social media posts from 300 authors, labeled by their age
and gender. Authors’ identities and sensitive information were
anonymized to ensure privacy. Various classical machine learning
and deep learning techniques were employed to evaluate the
dataset. For gender classification, the best accuracy achieved was
80% using Support Vector Machine (SVM), while a Multinomial
Naive Bayes (MNB) classifier achieved the best F1 score of 0.756.
For age classification, MNB attained a maximum accuracy score
of 91% with an F1 score of 0.905. This research highlights the
effectiveness of machine learning in gender and age classification
for Bangla author profiling, with practical implications spanning
marketing, security, forensic linguistics, education, and criminal
investigations, considering privacy and biases.
Index Terms—Datasets, Benchmark, Bangla Author Profiling,
Natural Language Processing, Machine Learning
I. I NTRODUCTION
Author profiling has become indispensable with the growing
usage of social media, where anyone can write anything [1]. It
is the study of specific texts to discover unique characteristics
of an author, such as gender, age group, region, and language,
based on their writing style and content [2]. As social media
platforms expand, the need to unravel the characteristics of
authors becomes increasingly apparent in order to ensure the
safety of online activities and communication. Author profiling
has significant implications for security, forensic linguistics,
education, research, and marketing. For example, social media
ads are now mostly curated based on author characteristics,
tailoring content to different demographics. Companies are
leveraging authors’ profiles to understand reviews and better
grasp their target audience. Forensic linguists utilize author
profiling to determine the linguistic profile of suspects, aiding
investigations [3]. Moreover, it could be useful in detecting
fake profiles and news [4]. Nevertheless, discerning the identi-
ties behind texts is a complex and challenging task that needs
further attention, especially for a low-resourced language as
Bangla [5].
1Code & Artifacts : https://github.com/crusnic-corp/BN-AuthProf
Problem Statement and Our Proposal: While author pro-
filing has been extensively explored in languages like Dutch,
English, Greek, and Spanish [6], it remains largely unexplored
in Bangla due to the unavailability of a benchmarked dataset.
This paper aims to fill this gap by benchmarking classical
machine learning (ML) and deep learning (DL) approaches for
predicting authors’ gender and age based on Bangla textual
content from social media platforms. For this purpose, we
extensively compiled the BN-AuthProf Dataset1 by collecting
author IDs with substantial Bangla posts with their consent.
The dataset consists of 300 anonymized authors and 30,131
manually curated Facebook posts in Bangla, tagged with age
and gender information.
The contributions of this paper are summarized as follows:
• We studied author profiling in the Bangla language,
aiming to predict demographic factors such as age group
and gender based on textual content. To the best of our
knowledge, this is the first work of its kind in Bangla.
• We introduced the BN-AuthProf Dataset that includes
30,131 Facebook status from 300 Bengali authors, each
labeled with age and gender. We also compared nine
popular ML/DL algorithms for benchmarking.
• We have drawn several conclusions and recommendations
for the research community to consider. Additionally, our
results could serve as a strong baseline for future machine
learning experiments in this domain.
II. R ELATED WORK
In the recent past, automatic profiling of authorship has seen
a multitude of literary developments. Here we categorically
present these key findings.
Language Based: Though researchers have extensively ex-
plored approaches across various languages, they are still in
their infancy when it comes to low-resource languages like
Bangla [7]. A lexical model was used in an early attempt
to predict age and gender in English on social networks [8].
This system used regression and classification models and
yielded results (91.9% accuracy) in line with state-of-the-
art age and gender prediction. Basile et al. [9] employed a
gender prediction model across English, Spanish, Arabic, and
Portuguese on Twitter data which performed between 0.68
and 0.98, with an average accuracy of 0.86 on the testset.
©2024 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including
reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or
reuse of any copyrighted component of this work in other works.
arXiv:2412.02058v1  [cs.CL]  3 Dec 2024

For identifying Indianic native languages, TF-IDF and n-
gram features showed promising results [10]. Alsmear et al.
[11] studied gender identification in Arabic texts, employing
various classification techniques.
Features Based: Peersman et al. [12] investigated age and
gender prediction on social networks, emphasizing the chal-
lenge of short text lengths (average of 12 words). They utilized
emoticons, image sequences, and character/word n-grams as
features, achieving optimal results with a balanced training
dataset. Parres et al. [13] introduced diverse features, including
structural metrics, part-of-speech analysis, emoticons, and
themes derived from Latent Semantic Analysis (LSA). A
Random Forest classifier with 311 features for age and 476
features for gender prediction yielded the highest accuracy.
However, this approach was relatively slow.
Learning Based: Techniques primarily utilize supervised
learning approaches. Hamda et al. [12] utilized Support Vector
Machine (SVM) classifier for age, gender, and language vari-
ety identification in Arabic, achieving accuracy up to 95.97%
for age and 81.53% for gender. In contrast, Schaetti et al.
[14] combined TF/IDF with Convolutional Neural Networks
(CNNs) to predict language variety and gender, showing
higher accuracy rates of 98% on Portuguese. Our model did
not perform as well as theirs, even if it worked great for CNN
and other neural networks.
Corpus Based: Hsieh et al. [15] investigated author profiling
on Facebook, achieving high accuracy in tasks such as age
and gender prediction. Guimaraes et al. [16] explored age
categorization on Twitter corpus, achieving notable results
using CNN. Zhao et al. [17] investigated age and gender
identification in emails and achieved accuracies of 72.10% for
gender and 81.15% for age classification. Nguyen et al. [18]
conducted a comparative analysis, highlighting limitations in
current computational approaches. The study reveals that over
10% of Twitter users do not conform to their biological sex,
and older users are often mistaken for younger ones.
Dataset Based: Datasets like PAN have been instrumental
in hosting various author profiling tasks, exploring traits
such as gender, age, native language, and personality. While
SVM remains a popular choice among participants [19] [20],
techniques like random forest and logistic regression have
also been employed [21]. Character-level CNNs and RNNs
also demonstrated success, offering alternatives to word-based
approaches [22]. In the 2016 PAN task, V ollenbroek et al.
[23] achieved the highest average accuracy of 52.58% using a
linear SVM with n-grams and part-of-speech feature. However,
Modaresi et al. found that part-of-speech tagging was not
sufficient for domain-independent profiling [24]. CLEF-PAN
2018 challenge [25] included gender prediction from texts and
photos, introducing new subtasks and language options.
Research Gap: The availability of a corpus is a need for
developing any NLP technique in any language. The lack
of an author dataset is the biggest challenge to authorship
classification in the Bengali language. We created this dataset
(BN-AuthProf) in order to address this problem. The dataset
includes 30,131 manually collected Bangla Facebook posts
with age and gender tags, along with 300 anonymized authors.
Various classical machine learning and deep learning tech-
niques were employed to evaluate the dataset by investigating
optimized hyperparameters (such as n-gram, vectorizer, loss,
activation, kernel size, batch size, and epoch).
III. BN-A UTH PROF DATASET
In this section, we comprehensively explore the BN-
AuthProf dataset, its creation, labeling process, and features.
A. Data Accumulation
Social media platforms like Facebook, Twitter, and In-
stagram are widely utilized in both Bangladesh and India.
Facebook, in particular, holds substantial prominence, with ap-
proximately 90.46% usage in Bangladesh 2, and India leading
globally in terms of Facebook users 3. Consequently, Facebook
was chosen as the primary platform for data collection. Our
author selection includes Facebook users from Bangladesh and
West Bengal (an Indian province), spanning various profes-
sions. We manually collected textual data from 300 authors,
each contributing numerous Bengali posts. We contacted each
author before collecting their data and only chose those
who gave consent, following ethical data collection practices.
Personal information, such as user IDs, was systematically
removed, and numerical IDs from 1 to 300 were assigned
for data accumulation and labeling. We followed several
guidelines during data collection:
Author Selection: We only selected authors having a substan-
tial amount of posts ranging from 80 to 100 status.
Content Criteria: Status containing more than 10 words were
included to ensure data quality in terms of semantics.
Language Integrity: Statuses with mixed languages were
excluded to maintain focus on Bengali.
Privacy: Statuses containing personal information or sensitive
data were avoided to maintain the privacy of authors.
Exclusion of External Links: Statuses containing URLs or
external links were excluded to maintain data integrity.
Data Deduplication: Duplicated statuses from the same au-
thor were removed to ensure dataset uniqueness.
Exclusion of Shared Content: Only original posts from
chosen authors were included, excluding shared content.
B. Data Annotation
We have classified authors based on two criteria: age and
gender. Our dataset comprises 300 text documents (one per
author), each named ‘#User Id.txt’, and a separate single file
titled ‘#Truth.txt’. For example ‘1.txt’ file contains the first
authors’ posts, with each line representing an individual post.
Simultaneously, the corresponding labels (i.e., age, gender) are
placed within the ‘#Truth.txt’ file, employing a specific format:
‘#1.txt:::<gender>:::<age>’.
2https://gs.statcounter.com/social-media-stats/all/bangladesh
3https://www.statista.com/statistics/268136/

BN-AuthProf
Dataset
1.txt:::M:::35-49
2.txt:::M:::50-xx
3.txt:::M:::35-49
4.txt:::M:::25-34
5.txt:::F:::25-34
1. সয়দ  শামসুল  হেকর  দয়া ...
2. লখকেদর  বািড়েয়  বলার ...
3. বাংলা  একােডিমর  সভাপিত ...
4. বাংলা  নববেষ র  েভা ...
5. রাজনীিতেত  কাদা  ছাড়াছিড় ,..
#Truth.txt
1.txt
Fig. 1. File Structure of BN-AuthProf Dataset
In the context of the BN-AuthProf dataset, gender classi-
fication employs ‘ M’ to signify males and ‘ F’ for females.
In terms of age classification, labels span four ranges: ‘ 18-
24’, ‘ 25-34’, ‘ 35-49’, and ‘ 50-xx’. Fig. 1 provides a visual
representation of our file structure.
C. Dataset Statistics
Table I delineates the quantitative statistics of our dataset,
where we observed a notable imbalance in gender and age
groups, reflecting broader societal trends in Bangladesh 4.
TABLE I
STATISTICS OF BN-A UTH PROF DATASET.
Number of Quantitative Value
Total Authors 300
Status Per Author 80 - 100
Total Status 30131
Categories 2 (Gender, Age)
Gender: [Male (M), Female (F)] [227, 73]
Age: [18-24, 25-34, 35-49, 50-xx] [43, 127, 82, 48]
D. Data Augmentation
The pie charts in Fig. 2 illustrate the distribution of gender
and age labels in our original dataset. There is a notable
inconsistency in the distribution of these labels, which poses
a challenge during benchmarking with machine learning algo-
rithms by introducing bias toward the ‘M’ gender label and the
‘25-34’ age group. To address this issue, we have employed
a solution that involves randomly generating additional data
from the original dataset to produce a balanced training set.
Male
75.7%
Female
24.3%
25-34
42.3%18-24
14.3%
35-49
27.3%
50-xx
16%
Fig. 2. Distribution of Gender and Age Categories
4https://datareportal.com/reports/digital-2023-bangladesh
Initially, our dataset included data from 227 male and 73 fe-
male authors. To rectify this gender imbalance, we created 154
additional data entries for female authors. This augmentation
was achieved by randomly selecting status updates from the
existing female data and mixing them to create new, synthetic
examples. Regarding age, we had 43 instances for the ‘18-24’
group, 127 for the ‘25-34’ group, 82 for the ‘35-49’ group,
and 48 for the ‘50-xx’ group. To align these groups more
closely with the dominant ‘25-34’ group, we generated an
additional 84 instances for the ‘18-24’ group, 45 instances for
the ‘35-49’ group, and 79 instances for the ‘50-xx’ group. The
same random oversampling technique for generating gender-
specific data was applied to balance the age groups. Table
II provides insights into the adjustments made to address the
initial imbalance in gender and age labels.
TABLE II
AUGMENTED BALANCED DATASET AFTER OVERSAMPLING
Dataset Gender Age M F Total 18-24 25-34 35-49 50-xx Total
Original 227 73 300 43 127 82 48 300
Augmented 0 154 154 84 0 45 79 208
Experimental 227 227 454 127 127 127 127 508
E. Experimental Dataset
For benchmarking, we created the experimental dataset that
combines original data with augmented data (see Table II).
This experimental dataset is divided into two distinct cate-
gories: Gender and Age. We further split each category into
training, development, and testing sets based on the number of
posts. We allocated approximately 80% of each author’s posts
to training, 10% to validation, and 10% to the testing portion.
Table III and Table IV present detailed statistics of the data.
It is important to note that we only used the augmented data
in the training set, while the validation and test sets consisted
solely of original data. This decision ensures that the validation
and test sets are not repeated during our evaluations.
TABLE III
EXPERIMENTAL DATASET FOR GENDER CLASSIFICATION TASK
Exp. Dataset Train Valid Test
(Gender) #Doc #Posts #Doc #Posts #Doc #Posts
Male 277 18078 227 2256 227 2313
Female 277 17211 73 747 73 768
TABLE IV
EXPERIMENTAL DATASET FOR AGE CLASSIFICATION TASK
Exp. Dataset Train Valid Test
(Age) #Doc #Posts #Doc #Posts #Doc #Posts
18-24 127 6944 43 416 43 427
25-34 127 10137 127 1267 127 1300
35-49 127 10387 82 835 82 859
50-xx 127 7673 48 485 48 495
IV. B ENCHMARKING AND EVALUATION
For benchmarking, we used five classical ML models:
Support Vector Machine, Na ¨ıve Bayes, Decision Tree, K-
nearest Neighbor, Logistic Regression, and four deep learning
models: LSTM, BiLSTM, CNN, BiLSTM + CNN. Fig. 3
outlines a structured approach for assessing the performance
of the aforementioned models on the BN-AuthProf dataset.

Classical Machine Learning and
DeepLearning Methods
Raw
Dataset
Data Generation and Spliting
Experimental
Dataset
Data Cleaning
Data Transforming
Benchmarking Methodology
DL Models
LSTM
Stacked LSTM
BiLSTM
CNN
BiLSTM + CNN
ML Models
KNN
SVM
Naive Byes
Decision Tree
Logistic Regression
Performance Assesment and
Comparison
Hyperparameter Tuning
Fig. 3. Benchmarking Approach for BN-AuthProf Dataset
A. Preprocessing
As we required only Bangla status updates, we had to clean
irrelevant information from the original dataset. During the
data preprocessing, we cleaned the data, tokenized it, and
transformed the text into sequences. Fig. 4 shows a general
overview of the data preprocessing pipeline with a flowchart.
Data Cleaning Tokenization and Transformation
Start
Remove
URL
Remove
Newline
Remove Other
Languages
Remove
Hashtags
Remove Special
Character
Remove
Whitespace
No
Deep
Learning?
Sentence
Tokenization
Text to
Sequence
End
Word
Tokenization
TF-IDF/Count
Vectorization
Yes
Fig. 4. Data Preprocessing Pipeline
Briefly, we start by Removing URLs’ from the data. Next,
any ‘Line Feed’ or ‘Newline Character’ (i.e., \r, \n) is
removed. After that, we remove any types of Latin Characters’
that might constitute the English language. We also remove
‘Whitespaces’, ‘Unwanted Characters’, and the ‘Hashtag Sym-
bol’ since these elements do not contribute to the overall
semantics of the data. However, we did not remove emojis,
as they tend to polarize the status for certain groups, such as
younger generations.
Since each status or post consists of multiple sentences, we
need to chunk them into smaller units. This process is known
as tokenization. Thus, in the next step, we determine whether
we are applying classical machine learning approaches or
deep learning techniques. For the deep learning models, we
utilize ‘Sentence Tokenization’, whereas for classical ones,
we tokenize each input into words. For the deep learning
approaches, we convert each sentence into a fixed-sized integer
sequence (i.e., vector), where each element of the sequence
represents either a word or padding. In contrast, for classical
ML, the tokenized words are transformed into numerical repre-
sentations using frequency-based techniques such as counting
or TF-IDF (Term Frequency - Inverse Document Frequency).
B. Classical Machine Learning
The classical ML models are mostly statistical in nature and
straightforward to utilize. However, they require handcrafted
feature engineering, which offers greater insights into the
models’ behavior. Below, we provide details about the settings
we used during our experiments with these classical models:
Support Vector Machine: Support Vector Machine (SVM)
is a supervised learning algorithm primarily used for classi-
fication tasks. It constructs an optimal decision boundary, or
hyperplane, between data points of different classes. SVMs
have been shown to excel in author profiling in the PAN
shared task [6] [23] [25]. For gender classification, SVM
employs binary classification using various kernel functions
such as sigmoid, poly, and linear. Age classification utilizes
multiclass techniques including One-vs-One (OvO) and One-
vs-Rest (OvR), along with kernels like RBF and polynomials.
We utilized both tf-idf and count vectorizers with character
n-gram (range 1-8) and word n-gram (range 1-7) features.
Naive Bayes: Na¨ıve Bayes (NB) classifiers leverage Bayes’
theorem to predict class labels based on feature independence
assumptions. They are computationally efficient, making them
ideal for rapid model development and prediction. Multino-
mial, Bernoulli, and Complement NB models are employed
during the benchmarking with similar settings for n-gram
features as SVM.
Logistic Regression: Logistic Regression (LR) is a statistical
method used to predict binary outcomes by modeling the
relationship between a dependent variable and one or more
independent variables. The tunable parameters in this model
include different solvers: saga, liblinear, newton-cg, and lbfgs.
K-Nearest Neighbor: K-Nearest Neighbor (KNN) is a non-
parametric, supervised learning algorithm used for both clas-
sification and regression tasks. It classifies data points based
on the majority vote of their nearest neighbors, with proximity
serving as the determining factor. To optimize the performance
of KNN, various distance metrics such as Minkowski, Eu-
clidean, and Manhattan, as well as neighbor values ranging
from 1 to 5, are explored.
Decision Tree: Decision Trees (DT) are tree-structured clas-
sifiers that recursively split data based on feature attributes.
They offer a simple yet powerful method for classification and
regression tasks. Criteria functions like Gini and entropy, along
with splitting strategies like best and random, are employed
to construct and prune decision trees.
C. Deep Learning
Deep learning is a subset of machine learning that employs
multi-layered neural networks for prediction tasks. Instead of
relying on manual feature engineering, various hyperparame-
ters play a pivotal role in performance tuning. Here, we will

provide details about the hyperparameter settings we utilized
during our experiments:
LSTM and BiLSTM: Long Short-Term Memory (LSTM), a
type of recurrent neural network (RNN), excels at handling
sequential data by capturing long-term dependencies. In con-
trast, Bidirectional LSTM (BiLSTM) processes input in both
directions, leveraging two layers of 128 LSTM cells each. We
set varying activations, batch sizes, and epochs to optimize the
performance of these models.
Convolutional Neural Network: Convolutional Neural Net-
works (CNN) process sequential data using embedding layers,
with the model architecture featuring convolutional layers with
max-pooling and sigmoid activation. Trained with varying
batch sizes and epochs, CNN is effective in feature extraction.
BiLSTM+CNN: The combined model integrates BiLSTM and
CNN, leveraging their complementary strengths. Employing
the ’adam’ optimizer and different loss functions, this model is
trained with varying batch sizes and epochs. All deep learning
models shared the same hyperparameters including maximum
length, vocabulary size, and embedding dimensions, trained
with adam optimizer,a learning rate of 0.001, and 16 samples
per batch for 3, 5, 10, and 15 epochs.
D. Evaluation Techniques
Measures of Classification Performance: We evaluate the
performance of different models on the experimental datasets
(see Tables III and IV). For task-specific supervision, we use
the training data, while the validation set plays a pivotal role in
tuning hyperparameters and optimizing the model. We perform
evaluations on our test set using the best settings obtained
during validation. We use Precision, Recall, F1-score, and
Accuracy as evaluation measures.
K-fold Cross Validation: We also employed K-fold cross-
validation to account for the model’s generalizability. We used
k = 10, dividing the whole dataset into 10 distinct folds for
iterative processing to obtain a mean Accuracy score.
E. Best Performance
In our study, we conducted an extensive evaluation of
numerous combinations of base classifiers for both gender and
age prediction tasks. Among the classical models for gender
prediction, the SVM model achieved the highest accuracy of
80.6% and F1-score of 0.614. This result was achieved using
an SVM with a polynomial kernel, word n-gram of (2, 3),
and Tf-Idf feature vectorization. The Multinomial Na¨ıve Bayes
(MNB) proved to be a robust choice for gender prediction,
delivering an accuracy of 79.6% and f1-score of 0.756. MNB
was particularly effective when accompanied by character n-
gram of (2, 4) and Count feature vectorization.
Regarding age prediction , the Multinomial NB model
outperformed others with an impressive accuracy of 91% and
F1-score of 0.905. This remarkable accuracy was achieved
using word n-gram of (1, 8) and Count feature vectorization.
Additionally, the SVM model, equipped with a polynomial
kernel plus word n-gram of (2, 5), and Tf-Idf Vectorizer,
achieved a competitive accuracy of 66% and f1-score of 0.582.
The results are summarized in Table V, showcasing the highest
accuracy and f1-score attained by the two best models for
gender and age classification.
TABLE V
RESULTS OF THE TWO BEST PERFORMED MODELS
Class Model Accuracy F1
Gender SVM 0.806 0.614
NB 0.796 0.756
Age SVM 0.660 0.582
NB 0.910 0.905
F . Comprehensive Analysis
Gender Classification: In this section, we present a thorough
assessment of our gender classification experiments. We eval-
uated the performance of both classical machine learning and
deep learning models, employing various feature extraction
techniques, kernel functions, and vectorization methods. To
commence, the bar chart of Fig. 5 showcases the distribution
of accuracy of the benchmarked models. Remarkably, the
Support Vector Machine (SVM) employing a word analyzer
with a polynomial kernel, (2, 3) n-gram, and Tf-Idf Vectorizer
achieved the highest accuracy of 80.6%. The best combina-
tions of hyperparameters achieved 75.67% accuracy for deep
learning models in gender prediction (see Table X).
Table VI provides a comprehensive overview of the gender
classification results, based on precision, recall, and F1-score
scores. Notably, the SVM algorithm exhibited the highest
precision score of 0.898, whereas the NB performed well in
recall, achieving a score of 0.796.
TABLE VI
GENDER CLASSIFICATION RESULTS OF CLASSICAL ML
Models Accuracy Precision Recall F1-Score
SVM 0.806 0.898 0.603 0.614
NB 0.796 0.741 0.796 0.756
DT 0.740 0.489 0.498 0.449
LR 0.683 0.378 0.496 0.429
KNN 0.700 0.468 0.486 0.460
We employed 10-fold cross-validation to assess the robust-
ness of our system. Table VII presents the mean accuracy
scores for the classical models. Support Vector Machine
(SVM) emerged as the most accurate model, with an accuracy
of 75.6%, while Decision Tree (DT) exhibited the lowest ac-
curacy at 74%. Interestingly, NB consistently performed well,
whereas K-Nearest Neighbor (KNN) and Logistic Regression
(LR) showed the same accuracy.
TABLE VII
CROSS VALIDATION FOR GENDER PREDICTION
Models SVM NB DT KNN LR
Accuracy 0.756 0.750 0.74 0.753 0.753

SVM NB DT KNN LR LSTM BiLSTM CNN BiLSTM
+CNN
Models Name
0.0
0.2
0.4
0.6
0.8
Models Accuracy
Fig. 5. Gender Classification Results
0.0 0.2 0.4 0.6 0.8 1.0
Recall
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Precisi
on Fig. 6. Precision Vs. Recall Curve for SVM
SVM NB DT KNN LR LSTM BiLSTM CNN BiLSTM
+CNN
Models Name
0.0
0.2
0.4
0.6
0.8Models Accuracy Fig. 7. Age Classification Results
To investigate further the performance of SVM and NB,
we present the confusion matrices in Fig. 8. It is evident that
NB excelled in classifying females, accurately identifying 58
instances. However, SVM displayed a notable bias towards
classifying instances as males, whereas NB demonstrates a
balanced performance in both gender categories. In order to
examine this phenomenon, we present the precision versus re-
call curve on varying classification margins (C values) of SVM
in Fig. 6. Examination of this curve reveals a gradual decline in
precision once recall exceeds approximately 0.2. Accordingly,
we established a threshold value of 0.67 for C, where precision
is notably high while recall remains comparatively lower for
the SVM classifier.
0DOH )HPDOH
3UHGLFWHG/DEHO
0DOH
)HPDOH
7UXH

/DEHO
 
 
Naive Bayes
0DOH )HPDOH
3UHGLFWHG/DEHO
0DOH
)HPDOH
7UXH

/DEHO
 
 
Support Vector Machine
Fig. 8. Confusion Matrix for Gender Classification (Best)
Turning to deep learning-based methods, Table X sum-
marizes the results using the ‘adam’ optimizer in all cases.
BiLSTM and CNN achieved the highest accuracy of 75.67%
when using the ‘binary crossentropy’ loss and ‘mean abso-
lute percentage error’ loss functions. Both LSTM and CNN
exhibited the lowest results with ‘mean absolute error loss’.
Age Classification: Age classification is a multi-class clas-
sification task, and we compared the models based on their
overall average prediction scores among the classes. Fig. 7
provides a histogram of accuracy for our machine learning
and deep learning models on age classification. Here, among
all the models, Multinomial Na ¨ıve Bayes (MNB) achieved
an impressive accuracy score exceeding 91%. However, the
overall average accuracy of the remaining models spans from
as low as 31% to as high as 71%.
TABLE VIII
AGE CLASSIFICATION RESULTS OF CLASSICAL ML
Models Accuracy Precision Recall F1-Score
SVM 0.660 0.889 0.534 0.582
NB 0.910 0.892 0.932 0.905
DT 0.420 0.168 0.249 0.154
LR 0.306 0.236 0.201 0.160
KNN 0.310 0.276 0.300 0.277
Table VIII lists the results of age classification for the classical
models. We observe that the NB algorithm outperformed all
other models with the highest accuracy score of 0.91% with
similar precision and recall scores. SVM also demonstrated
decent performance, with a precision of 0.88 and an F1 of 0.58.
Table IX provides 10-fold cross-validation scores for various
classical models. SVM in particular had the highest score of
42.3%, whereas KNN and DT had the lowest accuracy.
TABLE IX
CROSS VALIDATION FOR AGE PREDICTION
Models SVM NB DT KNN LR
Accuracy 0.423 0.416 0.399 0.336 0.346
We examined the confusion matrices for SVM and NB
classifiers in Fig. 9. The SVM classifier demonstrates a
distinct reliance on the 25–34 age class, showcasing notable
proficiency in accurately categorizing instances within this
particular age range. However, it is noteworthy that, within
the 18-24 age class, only 15 instances were appropriately
categorized, while the remaining 28 instances were misclas-
sified and attributed to the 25-34 age class. Furthermore,
SVM’s performance displayed inconsistencies in accurately
classifying instances within the 35-44 and 50-xx age classes,
resulting in misclassifications. In contrast, NB exhibited a
commendable level of accuracy across all age categories.
   [[
3UHGLFWHG/DEHO



[[
7UXH

/DEHO
   
   
   
   
1DLYH%D\HV
   [[
3UHGLFWHG/DEHO











[[
7UXH

/DEHO
   
   
   
   
6XSSRUW9HFWRU0DFKLQH
Fig. 9. Confusion Matrix for Age Classification (Best)

Moving to deep learning models, exhibiting lower per-
formance in general for age prediction. CNN stands out
with the highest accuracy of 71%. Meanwhile, LSTM and
BiLSTM achieved accuracy scores ranging from 14% to 42%
respectively. Table X provides an overview of deep learning-
based age prediction using the ‘adam’ optimizer in all cases.
Interestingly, changing the activation function or optimizer did
not significantly impact the scores.
TABLE X
DEEP LEARNING FOR GENDER AND AGE CLASSIFICATION WITH
DIFFERENT HYPERPARAMETERS (ACCURACY SCORES ).
Model Activation Loss Batch Gender Age
LSTM sigmoid BFC 16 0.75 0.42
LSTM softmax MAE 32 0.24 0.42
BiLSTM sigmoid BC 16 0.75 0.42
BiLSTM softmax SCC 32 0.75 0.14
CNN sigmoid MAPE 16 0.75 0.14
CNN relu MAE 72 0.24 0.71
BiLSTM + CNN sigmoid MAE 16 0.75 0.42
BiLSTM + CNN softmax MAE 32 0.24 0.42
Discussion: Our evaluation indicates that classical machine
learning methods generally outperform deep learning in gender
and age classification tasks. Na¨ıve Bayes consistently emerged
as a top performer. Additionally, SVM demonstrates strong
performance. Specific model configurations and optimizers
played a crucial role in DL models. These findings provide
valuable insights into the application of machine learning
algorithms for author profiling.
V. C ONCLUSIONS
We have examined the field of author profiling for Bangla,
extracting information about authors based on their writing
style. This domain has been largely unexplored due to the
unavailability of a dataset, despite having 300 million Bengali
speakers worldwide. This paper presents the BN-AuthProf
dataset encompassing 300 Bengali authors and 30,131 labeled
Facebook status. Our investigation primarily revolved around
crafting and evaluating machine learning and deep learning
models for gender and age classification. Through rigorous ex-
perimentation, we attained promising benchmarks, particularly
with Support Vector Machine and Naive Bayes algorithms. For
our future work, we intend on expanding categories beyond
age and gender and transitioning towards multi-label author
profiling through transformer-based language models.
REFERENCES
[1] E. Lundeqvist and M. Svensson, “Author profiling: A machine learning
approach towards detecting gender, age and native language of users in
social media,” in Dissertation, 2017.
[2] K. C. Santosh, R. Bansal, M. Shekhar, and V . Varma, “Author profiling:
Predicting age and gender from blogs notebook for pan at clef 2013,”
in CLEF, 2013.
[3] F. Rangel, “Author profile in social media: Identifying information about
gender, age, emotions and beyond,” in FDIA, 2013, pp. 58–60.
[4] C. Zhang, Y . Guo, J. Wu, S. Wang, Z. Niu, and W.-F. Cheng, “An
approach for identifying author profiles of blogs,” in ADMA, 2017.
[5] M. R. Hossain, M. M. Hoque, M. A. A. Dewan, E. Hoque, and
N. Siddique, “Authornet: Leveraging attention-based early fusion of
transformers for low-resource authorship attribution,” Expert Systems
with Applications, p. 125643, 2024.
[6] E. Stamatatos, W. Daelemans, B. Verhoeven, M. Potthast, B. Stein,
P. Juola, M. A. Sanchez-Perez, A. Barr ´on-Cede˜no et al. , “Overview
of the author identification task at pan 2014,” in CEUR workshop
proceedings, vol. 1180. CEUR-WS, 2014, pp. 877–897.
[7] S. Ahmed, S. Rakin, K. Urmi, C. K. Nag, and M. M. Akbar, “Emotion
analysis of social media bangla text and its impact on identifying the
author’s gender,” arXiv preprint arXiv:2411.04524 , 2024.
[8] M. Sap, G. Park, J. Eichstaedt, M. Kern, D. Stillwell, M. Kosinski,
L. Ungar, and H. A. Schwartz, “Developing age and gender predictive
lexica over social media,” in EMNLP, 2014, pp. 1146–1151.
[9] A. Basile, G. Dwyer, M. Medvedeva, J. Rawee, H. Haagsma, and
M. Nissim, “Simply the best: minimalist system trumps complex models
in author profiling,” in CLEF. Springer, 2018, pp. 143–156.
[10] H. A. Nayel and H. Shashirekha, “Mangalore-university@ inli-fire-2017:
Indian native language identification using support vector machines and
ensemble approach.” in FIRE, 2017, pp. 106–109.
[11] K. Alsmearat, M. Al-Ayyoub, and R. Al-Shalabi, “An extensive study of
the bag-of-words approach for gender identification of arabic articles,”
in IEEE/ACS AICCSA. IEEE, 2014, pp. 601–608.
[12] H. A. Nayel, “Nayel@ apda: Machine learning approach for author
profiling and deception detection in arabic texts.” in FIRE, 2019, pp.
92–99.
[13] D. Parres and C. Gomez, “Bert sentence embeddings in different
machine learning and deep learning models for author profiling applied
to irony and stereotype spreaders on twitter,” 2022.
[14] N. Schaetti, “Unine at clef 2017: Tf-idf and deep-learning for author
profiling.” in CLEF (Working notes), 2017.
[15] F. Hsieh, R. Dias, and I. Paraboni, “Author profiling from facebook
corpora,” in LREC, 2018.
[16] R. G. Guimaraes, R. L. Rosa, D. De Gaetano, D. Z. Rodriguez, and
G. Bressan, “Age groups classification in social network using deep
learning,” IEEE Access, vol. 5, pp. 10 805–10 816, 2017.
[17] C. Zhao, W. Song, L. Liu, C. Du, and X. Zhao, “Research on author
identification based on deep syntactic features,” in ISCID, vol. 1, 2017,
pp. 276–279.
[18] D. Nguyen, D. Trieschnigg, A. S. Do ˘gru¨oz, R. Gravel, M. Theune,
T. Meder, and F. de Jong, “Why gender and age prediction from tweets
is hard: Lessons from a crowdsourcing experiment,” in COLING 2014,
2014, pp. 1950–1961.
[19] R. Bayot and T. Gonc ¸alves, “Author profiling using svms and word
embedding averages—notebook for pan at clef 2016,” 2016.
[20] M. A. Rahman and Y . A. Akter, “Multi-lingual author profiling: Pre-
dicting gender and age from tweets!” in Image Processing and Capsule
Networks: ICIPCN 2020 . Springer, 2021, pp. 505–513.
[21] D. Dichiu and I. Rancea, “Using machine learning algorithms for author
profiling in social media.” in CLEF (Working Notes), 2016, pp. 858–863.
[22] D. Bagnall, “Author identification using multi-headed recurrent neural
networks,” arXiv preprint arXiv:1506.04891 , 2015.
[23] M. B. op V ollenbroek, T. Carlotto, T. Kreutz, M. Medvedeva, C. Pool,
J. Bjerva, H. Haagsma, and M. Nissim, “Gronup: Groningen user
profiling,” Notebook for PAN at CLEF , 2016.
[24] P. Modaresi, M. Liebeck, and S. Conrad, “Exploring the effects of cross-
genre machine learning for author profiling in pan 2016.” in CLEF
(Working Notes), 2016, pp. 970–977.
[25] E. Stamatatos, F. M. Rangel-Pardo, M. Tschuggnall, B. Stein, M. Keste-
mont, P. Rosso, and M. Potthast, “Overview of pan 2018. author
identification, author profiling, and author obfuscation,” LNCS, vol.
11018, pp. 267–285, 2018.
