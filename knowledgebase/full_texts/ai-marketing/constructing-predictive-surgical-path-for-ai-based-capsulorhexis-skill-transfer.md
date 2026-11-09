---
title: Constructing Predictive Surgical Path for AI-based Capsulorhexis Skill Transfer
url: https://arxiv.org/abs/2608.21441
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Mohammad Javad Ahmadi
- Hamid D. Taghirad
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.21441
pages: 7
chars: 40346
fetched_at: '2026-11-08T13:34:10+00:00'
kb_version: 1
---

# Constructing Predictive Surgical Path for AI-based Capsulorhexis Skill Transfer

1
Constructing Predictive Surgical Path for
AI-based Capsulorhexis Skill Transfer
Mohammad Javad Ahmadi and Hamid D. Taghirad
Abstract—Automated training of surgeons is one of the most crucial factors that significantly minimize surgical training risks and
expenses. With recent advances in artificial intelligence (AI) knowledge and available data from various surgeries, AI’s involvement in
surgical training is becoming very promising. It is recommended that at the early stages of AI development, it interferes in the surgery
as a third agent alongside the trainer. As trust in AI increases, this process will lead to an AI agent acting as a trainer in the future.
The first phase in which AI can intervene in the training process is to suggest an improved surgical path to the trainer. A platform must
be constructed in the first step, to accomplish this task and to enhance the movement path of trainee surgeons. This paper introduces
this platform along with an annotated capsulorhexis surgery dataset called the ARAS-Farabi (Cataract LMM) dataset. In this research,
a deep convolutional neural network is pre-trained with JIGSAWS and ARAS-Farabi surgical datasets that can extract surgical skill
characteristics from surgery tool tip motion data. The proposed platform develops a reference model from the feature space of an expert
surgeon’s movement trajectory and proposes an improved path to enhance the skill of a novice surgeon. An optimization with two loss
functions is utilized to create a path that raises the skill level of the novice surgeon’s path while simultaneously predicting and preserving
his/her intent. The results of this study reveal that, with the assistance of an AI agent, the trainee surgeon’s movement path can be
enhanced by at least 20 percent while maintaining his intentional objective. In addition to the recommended deep network, various
tangible indicators have also been developed in this research to verify the level of trainee improvement.
Index Terms—Surgical Dataset, Surgical Skill Assessment, Surgical Skill Tansfer, Style Transfer, Surgical Path Suggestion.
✦
1 INTRODUCTION
T
HEadvances in robotics, control, and artificial intel-
ligence (AI) facilitate the automation of the surgical
training process, bringing ease and security to it. Several
efforts have been made to automate surgical skill assess-
ment. This is a big step toward automating surgical training;
yet, these efforts need more advancements [1], [2]. One
of the most significant challenges in order to automate
the surgical training process is finding an effective system
for the transfer of surgical skills from expert surgeons to
novices.
There are currently haptic and dual-user robotic devices
that allow the trainer surgeon to instruct trainees on how to
move and exert force during the surgery. These technologies
may also be used to correct errors made by novice surgeons.
There have been studies conducted on how to control these
devices for surgical training; however, the majority of them
lack the presence of AI agents. Consequently, the trainer
surgeon is still investing a sizable amount of time and effort
in the surgery training procedures. Adding an AI agent in
the surgical is very promising, in order to impart the master
surgeon’s surgical abilities to the trainee surgeon.
Our previous research focused separately on control
structures and artificial intelligence to facilitate eye surgery
training. The control structures used dual-user haptic sys-
tems and tracked errors between the trainer and trainee
to transfer skills [3], [4]. On the other hand, artificial in-
telligence automatically evaluated surgical performance by
extracting skill features [5]. To effectively train surgeons,
a structure that combines control and artificial intelligence
•Both authors are with the Applied Robotics and AI Solutions (ARAS),
Faculties of Electrical and Computer Engineering, K. N. Toosi University
of Technology, Tehran, Iran.
E-mail: mjahmadi@email.kntu.ac.ir, taghirad@kntu.ac.ir
seems to be essential. The first stage in this process is
creating a platform that generates an expert path from the
movements of a novice surgeon. In future works, this struc-
ture could serve as the interface between traditional control
and artificial intelligence. It is also possible to integrate a
predictive and educative artificial intelligence agent into
robotic devices by incorporating skill-related knowledge ob-
tained from artificial intelligence models that assess surgical
skills.
This platform can be effectively used to enhance training
circumstances, while eliminating the need for an experi-
enced surgeon to supervise trainees, as well. Along with the
trainee surgeon, this AI agent can first carry out the tasks of
a third auxiliary agent (alongside a trained surgeon), before
continuing to instruct surgery by itself.
Various initiatives have been undertaken in the past to
facilitate the transfer of surgical skills. Ershad et al. devel-
oped an AI-enabled surgical training system that identifies
the trainee’s style-based movement flaws and produces
haptic feedback to alert the trainee about existing errors
[6]. However, this study did not provide the trainees with
any guidance on how to enhance their actions. Zahedi et
al. suggested an AI-based guidance system for a virtual
kinesthetic training environment [7]. Fekri et al. created a
platform for instructing new residents in orthopedic surgery
drilling using a recurrent deep neural network [8]. Tan et
al. developed a laparoscopic training robotic system that
instructs students on how to manipulate surgical tools
through demonstrations from human specialists as well
as reinforcement learning [15]. The shortcoming of these
studies is that they cannot account for new paths that the
trainee might want to take during the surgery.
A key hindrance to the adoption of artificial intelligence
arXiv:2608.21441v1  [cs.RO]  18 Aug 2026

2
(AI) in surgical training is the issue of trust. Constructing
a foundational platform that highlights the ability of AI
to enhance surgical practices while adhering to established
surgical procedures, is an effective step in cultivating trust.
Inspired by this requirement, this paper presents a dataset
and AI-based system that identifies important information
about an expert surgeon and injects those surgical skills into
a trainee’s behavior. In this study, the general features of
surgery are extracted from the JIGSAWS dataset and injected
into the motion path of novice surgeons. Additionally, this
research resulted in the development of a dataset for cap-
sulorhexis surgeries in order to focus on the expert surgical
style and teach it to the trainees.
The representation of the developed platform can be
provided to the trainee surgeon in a visual format (Aras-
Farabi surgical analysis software [5]) or haptic feedback.
The outline of this paper is as follows. The proposed pro-
cedure is described in section 2. The intelligent approach,
the suggested control structure, and the developed and
utilized datasets are introduced in this section. The results
are introduced and discussed in section 3, while section 4
provides a summary, conclusions, and future directions.
2 METHODOLOGY
This section introduces the proposed platform for the cre-
ation of the predicted-constructed path. This platform in-
corporates a deep convolutional neural network to generate
a reference model while proficiently assessing the trainee
surgeon’s movements. Additionally, this structure employs
two datasets, which are described in the following sections,
while the second one is developed in this study. Starting
with the trainee (novice) surgeon, skill characteristics are
injected into the primary path automatically generated for
him/her. This is accomplished through the reference model
developed by the expert surgeon’s feature space, in order
to create an expert predicted-constructed path. Figure 1
illustrates an overview of this process.
CNN-FFT Network
N
E
𝑳Total = 𝒂𝑳Decision (𝑷, 𝑵) + 𝒃𝑳Skill (𝑬, 𝑷)
𝑳𝑺𝒌𝒊𝒍𝒍 𝑬 𝑷 = ∥ 𝐆𝐫𝐚𝐦𝒇𝑬 − 𝐆𝐫𝐚𝐦𝒇𝑷 ∥𝟐
𝑳Decission (𝑷, 𝑵) = 𝒇𝑷 − 𝒇𝑵 𝟐𝒇𝑵
𝒇𝑬
P
𝒇𝑷
𝒇𝑷
Fig. 1. The proposed structure for skill transfer.
2.1 Datasets
Two datasets are used in this study to consider both general
and specific surgical skills. The first dataset, designated
JIGSAWS, was created by Johns Hopkins University. The
second dataset, dubbed as ARAS-Farabi (Cataract-LMM)
[21], is developed in this paper and was created through
a partnership between the Farabi Hospital and the ARAS
research group. To augment datasets, various methods can
be utilized, such as using different time frames of surgical
data and employing different permutations of Cartesian
coordinates. For instance, interchanging the data related to
x and y coordinates ([x,y] to [y,x]) does not affect the com-
prehension of the skill represented by the data sequence. In
the next sections, we will provide a brief overview of the
two datasets.
2.1.1 JIGSAWS Dataset
JIGSAWS stands for JHU-ISI Gesture and Skill Assessment
Working Set. This dataset has collected 76 kinematic vari-
ables from the movements of 103 surgeons. These data
are obtained from three surgical tasks of suturing, needle
passing, and knot tying, while the skill level of the sur-
geons who performed these tasks is also included in this
dataset [16], [17]. These data were taken from the da Vinci
robotic surgery system, and the skill annotations mostly
depend on hours of surgical experience. An image related
to the JIGSAWS dataset is shown in Figure 2. In this paper
we use the kinematic variablesx, y,andz(position) from
this dataset.
(a) Needle-Passing
 (b) Suturing
 (c) Knot-Tying
Fig. 2. Three general surgical tasks in JIGSAWS dataset.
2.1.2 ARAS-Farabi Software and Dataset
There are several challenges in teaching and learning
cataract surgery while preserving patient safety. One of the
limitations of intraocular surgery teaching is that the attend-
ing surgeon mostly plays the role of an observer/supervisor
during the surgery and can’t prevent potential complica-
tions. Moreover, surgical performance needs deep knowl-
edge of ocular anatomy, manual dexterity, and mastering
basic surgical skills [18]. A continuous curvilinear anterior
capsulotomy (CCC, capsulorhexis) is one of the critical
initial steps in this surgery. The goal of capsulorhexis is
to create a circular opening in the anterior surface of the
cataracted lens. Creating this opening is one of the most
challenging tasks for first-year residents [19], [20], [22].
Therefore, creating a dataset of capsulorhexis surgeries is
important.
On the other hand, as shown in Figure 2, the JIGSAWS
dataset is far from representing a real surgery process,
and research that solely relies on it will not significantly
contribute to the development of effective and realistic
surgical training. To address this issue, this study has de-
veloped a dataset of actual surgical procedures, which is
introduced in this section. In cataract surgery, interventions
are performed on the human eye using tiny tools under a
surgical microscope. The surgical microscope camera cap-
tures the video that the surgeon sees through the eyepiece.

3
The microscope camera records surgical videos with pixel
dimensions of720×576(using the H.264/AVC codec). The
surgical videos were recorded and then pre-processed to
enable annotation and extraction of motion data. The data
sampling rate, which falls within the range of 25 to 30 data
points per second, has been carefully selected to capture
sufficient information to acquire skill features. The amount
of input data has been also calculated with consideration of
providing ample time for the acquisition of such features.
ARAS-Farabi dataset contains more than one hundred
capsulorhexis surgery recordings. Initially, three expert sur-
geons annotated the recordings based on distinct skill indi-
cators and classified them as expert or novice. Subsequently,
the motion data related to surgical videos were retrieved
using the ARAS-Farabi surgical analysis software [8]. This
software is developed with the Python programming lan-
guage and the PyQt library, and it is available in two
versions for Windows and Linux. Although ARAS Group
is trying to improve this software’s tracking tools [9], it
currently relies on OpenCV library trackers. In this software,
any tracking algorithms from the OpenCV library can be
utilized; however, the best method based on an objective
evaluation of the ARAS-Farabi dataset is specified as the
default mode.
This program is user-friendly and can be used for var-
ious medical purposes. It is sufficient for the user to open
the video and identify the main surgical areas. This software
allows human intervention as an observer. It is possible to
redefine the bounding boxes by pausing the video and going
back if the tracker performance needs to be corrected. This
software calculate position, speed, and acceleration of the
centers of the two main areas of the surgery (absolutely
and relatively), stored, and displayed in real-time as graphic
diagrams and numerical data. This software addresses some
Extracting motion information
in various formats
(tip of the instrument relative to the center of the
primary visual environment in cataract surgery)
Storing motion data absolutely.2
1
Fig. 3. Output information of Aras-Farabi software.(Video).
challenges associated with extracting motion data from sur-
gical videos. For example, intraocular light reflection may
mislead computer vision algorithms into tracking the tip
of a capsulorhexis instrument that is visually close to this
reflection. As shown in Figure 4, this software has tracked
and removed the light reflection in all video frames using
morphology operations and OpenCV libraries. To address
the challenge of frame scales and the non-uniformity of
video magnifications, all motion information is scaled ac-
cording to the length of the pupil’s bounding box, which is
nearly the same for all individuals according to our goals
[10].
Removing light reflection.
3
Determining initial
bounding boxes
1
2
The light reflection has
been eliminated.
Fig. 4. Removing light reflections and defining initial bounding boxes
(Video).
Figure 5 compares the 2D position information for the
two tools in a surgery recording of the JIGSAWS dataset
to validate whether the motion information was retrieved
using this tracker-based software is genuinely related to the
accurate sensory information. The JIGSAWS dataset was
chosen for this section because it includes sensing data
synced with the video. The upper subgraphs of each data
point are retrieved from the sensor, and the lower sub-
graphs of each graph are extracted using the ARAS-Farabi
program. The ARAS-Farabi software can keep the surgeon’s
path going in its output data with high accuracy. It merely
requires the appropriate scale to map to the sensor data.
It should be noted that the general moving process rather
than the precise, scaled numerical information is essential
in assessing surgical skills. With this software, a data set of
surgeon movement information in sync with the videos was
created.
0 250 500 750 1000 1250 1500 1750
Intervals
0.10
0.15X1
JIGSAWS Sensors (Suturing_D005)
x1
0 250 500 750 1000 1250 1500 1750
Intervals
400
200
X1
ARAS-Farabi App (Suturing_D005_capture2)
x1
(a) X1
0 250 500 750 1000 1250 1500 1750
Intervals
0.050
0.025
0.000
Y1
JIGSAWS Sensors (Suturing_D005)
y1
0 250 500 750 1000 1250 1500 1750
Intervals
300
200
100
Y1
ARAS-Farabi App (Suturing_D005_capture2)
y1 (b) Y1
Fig. 5. Comparison of information extracted from ARAS-Farabi software
with sensory data.
This study employs position and velocity data retrieved
from videos of capsulorhexis surgery.
2.2 Skill-related feature extraction
Creating a knowledge repository of surgical skills is crucial
for skill transfer. Developing an artificial intelligence model
for differentiating and categorizing surgeons’ skills into
experts and novices enables the model to comprehend the
features of expert surgeons’ motions. The model’s trained
and stored weights, parameters, and layers are then used to
embed these features. These models are trained on JIGSAWS
[16], [17] and ARAS-Farabi datasets to infer both general
and specific surgical skills. With more manageability in the
prediction and motion route generation phase, an AI model
that uses less computational resources for feature extraction
will be more desirable.

4
Our neural network model was developed based on
research that suggests skilled surgical performance can be
assessed by analyzing hand movements [23]. Rather than
using all of the motion information in Cartesian coordinates
as input, only a portion was utilized. The remaining data
patterns were extracted using neural network filters. Due
to these considerations, our network is light, prepared for
quick processing, and able to decide based on a small subset
of the data. In the following, the architecture of the proposed
network is introduced. The input to the network consists of
N data points (intervals) of absolute or relative x, y (and z
or v) coordinates. The smoothness of the entry path is a key
aspect of the surgeon’s skill, according to our research on
the evaluation of surgical performance [8].
It has been shown in several studies that spatiotemporal
information such as movement fluidity and path smooth-
ness can be effectively obtained in the frequency domain
[8], [11], [12]. Therefore, the input data points are passed
through an Fast Fourier Transform (FFT) block to utilize
the frequency domain. This is the input that the network
receives. The general structure of the network comprises
convolutional layers, batch normalization layers, and ELU
activation functions. Figure 6 depicts an overview of this
network. It is notable that the task of extracting significant
features is left to be handled by the convolutional network
itself, rather than adding more information to the input.
Patterns from the input data, including those that are not im-
mediately apparent to us and those that are intelligible, such
as speed and acceleration, are extracted by convolutional
layers. In Figure 6, it can be observed that the output of the
initial layers is connected to the subsequent layers, which
allows the input information to be preserved throughout
the depths of the network and utilized in the latent space.
It is postulated that if the weights, coefficients, and hyper-
parameters of the structure are adjusted to the extent that it
can differentiate between skilled and novice surgery in its
final fully connected layer, then the pre-classification layer
of the structure will possess a latent space of skilled and
novice surgeons’ movement patterns.
Inputs
JIGSAWS: [x,y,z]
ARAS-Farabi: [x,y,v]
BN BN BN BNConv Conv ConvELU ELU ELUADD Flat. Dense
Fig. 6. The architecture of the proposed network.
2.3 Predictive-constructive
Utilizing optimization techniques and style transfer meth-
ods can enhance the proficiency of novice surgeons without
compromising their surgical intent. For this purpose, a
function for bilateral optimization needs to be developed
[13]. A function is proposed to maintain the surgeon’s
intended path while appearing to have been taken with
greater expertise. The relation for the loss function used in
optimization is defined as:
LT otal=aL Decision( ⃗P ,⃗N) +bL Skill ( ⃗E, ⃗P).(1)
The amount of AI agent intervention required to construct
and suggest an improved path from the original path can be
determined based on the distribution of coefficientsaand
b, and the duration of the novice surgeon’s training. It can
be conceived that at the onset of training, when a novice
surgeon has less expertise, the ratio of a b may be greater
than one, and that over time, this ratio can be decreased to
a value between zero and one.
The novice surgeon’s entry path is aimed to be improved
with minimal deviation from their intention through the
utilization of the decision loss function. This loss function’s
minimization corresponds to minimizing the Euclidean dis-
tance between the points on the novice surgeon’s path
and the suggested path. By utilizing the concept of fea-
ture vectors instead of point distance between the paths,
attention can be directed toward the higher-level features of
movements.
An appropriate loss function for the skill needs to be de-
fined to improve the movement path of the novice surgeon.
This function is capable of operating such that the statistical
distribution of the feature space of the input path is com-
parable to that of the hidden layers of expert surgeons. To
achieve this, the maximum mean square difference (MMD2)
can be utilized to minimize the differences between statis-
tical indicators, such as means, variances, and higher order
moments, in the feature vector distribution of the input path
and the expert path. In this study, the Gram matrices or
the inner product between the distributions of novice and
expert feature vectors and MMD2 are minimized.
The relationships of the decision and skill loss functions
are defined in the form of equation Equation 2, in accor-
dance with the justifications given.
LSkill ( ⃗E, ⃗P) =∥Gram fE −Gram fP ∥2
LDecission( ⃗P ,⃗N) =∥f P −f N ∥2
(2)
3 RESULTS ANDDISCUSSION
The network is trained using the provided data in the first
step, and a 99% F1 score is obtained after tuning the parame-
ters and hyperparameters. The surgical skill knowledge that
is embedded in the network can be utilized by saving the
model as an h5 file. By using the proposed platform and
considering the online path of the trainee (novice) surgeon
during surgery, the suggested path is created. The suggested
path is initialized with the novice path and constructed
using the Adam optimization method with a learning rate
ofγas given in Equation 3.
⃗P:= ⃗P−γ ∂LTotal
∂ ⃗P (3)
The improvement in the skill level is then determined by
passing both paths through the proposed network and
comparing the skill percentage of each. The skillfulness
of the proposed path may not be quantifiable from an
image or network output. To address this issue, quantitative
criteria are employed to assess the output path. Experienced

5
0 100 200 300 400 500 600
Sample
0.6
0.4
0.2
0.0
0.2
X [m]
1.83% Expert (xNovice)
8.81% Expert (xPredicted Constructed)
1.83% Expert (yNovice)
8.81% Expert (yPredicted Constructed)
1.83% Expert (zNovice)
8.81% Expert (zPredicted Constructed)
(a) b a = 1.5
0.6
 0.4
 0.2
 0.0 0.2
0.2
0.1
0.0
0.1
0.2
0.3
1.83% Expert (PathNovice)
8.81% Expert (PathPredicted Constructed)
 (b) b a = 1.5
0 100 200 300 400 500 600
Sample
0.6
0.4
0.2
0.0
0.2
X [m]
1.83% Expert (xNovice)
22.17% Expert (xPredicted Constructed)
1.83% Expert (yNovice)
22.17% Expert (yPredicted Constructed)
1.83% Expert (zNovice)
22.17% Expert (zPredicted Constructed)
(c) b a = 5
0.6
 0.4
 0.2
 0.0 0.2
0.2
0.1
0.0
0.1
0.2
0.3
1.83% Expert (PathNovice)
22.17% Expert (PathPredicted Constructed)
 (d) b a = 5
Fig. 7. Comparison of the base path (novice) and the predicted-
constructed path (expert).
surgeons exhibit more fluid and predictable movements. A
hybrid metric is employed, which considers the surgeon’s
back-and-forth hand motion and provides an estimate of
motion entropy. The criterion value decreases as the sur-
geon’s movements become more skilled and predictable.
Furthermore, a combined measure of speed (energy con-
sumption) and the Euclidean smoothness of frequency coef-
ficients is also employed to evaluate motion smoothness.
3.1 ARAS-Farabi Dataset
The ARAS-Farabi dataset was examined to analyze the
structure of skill transfer, with the use of scaled-relative
position and speed data retrieved from the capsulorhexis
cystotome tool-tip. To conduct the first experiment, an input
path was selected based on the novice data from the ARAS-
Farabi dataset. The features of an expert surgery were
injected into the initial path from the surgical path of one
of the surgeries labeled as the expert in the ARAS-Farabi
dataset. By varying the values of coefficientsaandbin
Equation 1, it is possible to control the relative importance
of improving the novice surgeon’s path and preserving
their intended movements. As shown in Figure 7, when the
significance coefficient of the loss function associated with
the skill increases, the suggested movement path becomes
more expert. Additional information about the amount of
change in the skill level of the novice surgeon’s path when
using the proposed path is provided in Table 1. The pro-
posed structure results in a novice surgeon’s new path that
contains more expert characteristics and fewer unexpected
movements and tremors.
The idealized performance of the proposed structure on
the velocity dimension is depicted in Figure 8. It can be
observed that the surgical instrument moves more smoothly
with this architecture, thereby reducing risks and increasing
the surgeon’s skill level.
The proposed structure’s performance is evaluated for
a new path taken by a novice. When these coefficients are
equally considered, it is observed that the skill level of the
movement path is increased by approximately 11%, while
0 100 200 300 400 500 600
0.02
0.00
0.02
0.04
0.06
0.08
0.10
0.12
VNovice
VPredicted Constructed
Fig. 8. Idealized performance of the proposed structure on the velocity
dimension.
preserving the novice surgeon’s general intention (9(a) and
9(b)). The rate of skilled improvement of the movement path
will be about 41% as we increase the important coefficient
of the skill loss function (9(c) and 9(d)). As can be observed
in Figure 9, the surgeon’s actions (including positions and
velocities) are now more fluid and less abrupt, in addition to
having movement characteristics that have more expertise
in terms of the trained network.
The next experiment investigates the impact of employ-
ing various sets of features. The trainee’s path is improved
even further when the network injects skill behaviors ex-
tracted from a more experienced trainer. In other words,
students will benefit from better instruction from a more
experienced instructor. To demonstrate this point, the char-
acteristics of a less expert surgical path are used, and the
proposed path under identical conditions improves the skill
TABLE 1
Skill enhancement of the novice surgeon using the
predicted-constructed path.
Indicators and Ratios of Coefficients b a =1.5 b a =5
Total Skill Level Improvement 6.97 20.33
Total Predictability Improvement 14.34 18.87
Enhancement in Tremor Reduction 0.23 3.44
Enhancement in Noise Cancellation 0.23 2.40
0 100 200 300 400 500 600
Sample
0.4
0.2
0.0
0.2
0.4
0.6
0.8
X [m]
56.64% xBase (Novice)
68.27% xPredicted Constructed (Expert)
56.64% yBase (Novice)
68.27% yPredicted Constructed (Expert)
56.64% vBase (Novice)
68.27% vPredicted Constructed (Expert)
(a) b a = 1.5
0.4
 0.3
 0.2
 0.1
 0.0 0.1 0.2
0.2
0.0
0.2
0.4
0.6
0.8 56.64% PathBase (Novice) 68.27% PathPredicted Constructed (Expert)
 (b) b a = 1.5
0 100 200 300 400 500 600
Sample
0.4
0.2
0.0
0.2
0.4
0.6
0.8
X [m]
56.64% xBase (Novice)
100.0% xPredicted Constructed (Expert)
56.64% yBase (Novice)
100.0% yPredicted Constructed (Expert)
56.64% vBase (Novice)
100.0% vPredicted Constructed (Expert)
(c) b a = 100
0.4
 0.3
 0.2
 0.1
 0.0 0.1
0.2
0.0
0.2
0.4
0.6
0.8 (d) b a = 100
Fig. 9. Comparison of the base path (novice) and the predicted-
constructed path (expert).

6
0 100 200 300 400 500 600
Sample
0.6
0.4
0.2
0.0
0.2
X [m]
1.83% Expert (xNovice)
15.03% Expert (xPredicted Constructed)
1.83% Expert (yNovice)
15.03% Expert (yPredicted Constructed)
1.83% Expert (zNovice)
15.03% Expert (zPredicted Constructed)
(a) b a = 5
0.6
 0.4
 0.2
 0.0 0.2
0.2
0.1
0.0
0.1
0.2
0.3
1.83% Expert (PathNovice)
15.03% Expert (PathPredicted Constructed)
 (b) b a = 5
Fig. 10. Comparison of the base path (novice) and the predicted-
constructed path (expert).
0 100 200 300 400 500 600
Sample
0.6
0.4
0.2
0.0
0.2
X [m]
1.83% Expert (xNovice)
67.85% Expert (xPredicted Constructed)
1.83% Expert (yNovice)
67.85% Expert (yPredicted Constructed)
1.83% Expert (zNovice)
67.85% Expert (zPredicted Constructed)
(a)
0.6
 0.4
 0.2
 0.0 0.2
0.2
0.1
0.0
0.1
0.2
0.3
1.83% Expert (PathNovice)
67.85% Expert (PathPredicted Constructed)
 (b)
0 100 200 300 400 500 600
Sample
0.6
0.4
0.2
0.0
0.2
X [m]
1.83% Expert (xNovice)
58.7% Expert (xPredicted Constructed)
1.83% Expert (yNovice)
58.7% Expert (yPredicted Constructed)
1.83% Expert (zNovice)
58.7% Expert (zPredicted Constructed)
(c)
0.6
 0.4
 0.2
 0.0 0.2
0.2
0.1
0.0
0.1
0.2
0.3
1.83% Expert (PathNovice)
58.7% Expert (PathPredicted Constructed)
 (d)
0 100 200 300 400 500 600
Sample
0.6
0.4
0.2
0.0
0.2
X [m]
1.83% Expert (xNovice)
31.3% Expert (xPredicted Constructed)
1.83% Expert (yNovice)
31.3% Expert (yPredicted Constructed)
1.83% Expert (zNovice)
31.3% Expert (zPredicted Constructed)
(e)
0.6
 0.4
 0.2
 0.0 0.2
0.2
0.1
0.0
0.1
0.2
0.3
1.83% Expert (PathNovice)
31.3% Expert (PathPredicted Constructed)
 (f)
0 100 200 300 400 500 600
Sample
0.6
0.4
0.2
0.0
0.2
X [m]
1.83% Expert (xNovice)
68.74% Expert (xPredicted Constructed)
1.83% Expert (yNovice)
68.74% Expert (yPredicted Constructed)
1.83% Expert (zNovice)
68.74% Expert (zPredicted Constructed)
(g)
0.6
 0.4
 0.2
 0.0 0.2
0.2
0.1
0.0
0.1
0.2
0.3
1.83% Expert (PathNovice)
68.74% Expert (PathPredicted Constructed)
 (h)
Fig. 11. Comparison of the base path (novice) and the predicted-
constructed path (expert) for four different surgical procedures per-
formed by an expert surgeon.
level by 7% less. Both Figure 10 and Table 2 illustrate this
fact.
In the final experiment given in this section, the informa-
tion related to a novice surgeon is considered, and the skills
of four different surgical procedures performed by an expert
surgeon are transferred to him. With the same coefficients,
it can be seen that the proposed path becomes 55% more
expert on average. Figure 11 contains the graphs associated
with this experiment.
TABLE 2
Skill enhancement of the novice surgeon using two different expert
paths.
Indicators and expert paths ID1 (4.35/5) ID17 (5/5)
Total Skill Level Improvement 13.20 20.33
Total Predictability Improvement 16.34 18.87
Enhancement in Tremor Reduction 2.33 3.44
Enhancement in Noise Cancelation 1.32 2.40
3.2 JIGSAWS Dataset
Since the JIGSAWS dataset contains information on x, y, and
z, the skill transfer structure is applied to these variables.
As shown in Figure 12, when the significance coefficient
of the loss function linked to skill improves, the suggested
movement path becomes increasingly expert. Table 3 gives
further information regarding the degree of change in the
rookie surgeon’s skill level when employing the proposed
path. Using the proposed platform, the revised path of the
inexperienced surgeon will feature more expert traits and
fewer surprising motions and tremors.
0 100 200 300 400 500 600
Sample
0.06
0.04
0.02
0.00
0.02
X [m]
5.86% Expert (xNovice)
11.54% Expert (xPredicted Constructed)
5.86% Expert (yNovice)
11.54% Expert (yPredicted Constructed)
5.86% Expert (zNovice)
11.54% Expert (zPredicted Constructed)
(a) b a = 1.5
0.04
0.03
0.02
0.01
0.000.010.020.03 0.02
 0.01
0.00
0.01
0.02
0.03
0.06
0.05
0.04
0.03
0.02
0.01
0.00
0.01
0.02
5.86% Expert (PathNovice)
11.54% Expert (PathPredicted Constructed)
 (b) b a = 1.5
0 100 200 300 400 500 600
Sample
0.06
0.04
0.02
0.00
0.02
X [m]
5.86% Expert (xNovice)
18.88% Expert (xPredicted Constructed)
5.86% Expert (yNovice)
18.88% Expert (yPredicted Constructed)
5.86% Expert (zNovice)
18.88% Expert (zPredicted Constructed)
(c) b a = 5
0.04
0.03
0.02
0.01
0.000.010.020.03 0.02
 0.01
0.00
0.01
0.02
0.03
0.06
0.04
0.02
0.00
0.02
5.86% Expert (PathNovice)
18.88% Expert (PathPredicted Constructed)
 (d) b a = 5
Fig. 12. Comparison of the base path (novice) and the predicted-
constructed path (expert).
TABLE 3
Skill enhancement of the novice surgeon using the
predicted-constructed path.
Indicators and Ratios of Coefficients b a =1.5 b a =5
Total Skill Level Improvement 5.67 13.01
Total Predictability Improvement 8.95 5.96
Enhancement in Tremor Reduction 5.91 18.44
Enhancement in Noise Cancelation 0.39 3.40
4 CONCLUSION
In this study, a CNN-FFT network pre-trained with motion
data from the JIGSAWS and ARAS-Farabi datasets is pre-
sented. The network generates a feature space, referred to as
a reference model when expert surgeon data is used as input
to the network. When the network is given the movement
path of the novice surgeon, a proposed movement path is

7
constructed using two loss functions and an optimization
procedure. The suggested path not only takes into account
the trainee surgeon’s objective but also enhances their skill
level. The amount of improvement was demonstrated by
employing the newly developed convolutional network and
some concrete indicators. It has been demonstrated that the
inclusion of a valuable AI agent for skill transfer in the
surgical training cycle can be accomplished through the
utilization of this platform. It was also demonstrated that
as the skill level of the reference model increases, there is
a greater likelihood of enhancing the movement patterns
of trainee surgeons. This research offers an advantage over
previous studies by preserving the surgeon’s aim in cap-
sulorhexis surgery, although the precise nature of that aim
is not specified. This approach is suitable for a wide range
of surgical training applications because it emphasizes both
general and specific (capsulorhexis) surgical abilities. By us-
ing a robotic haptic device and impedance control structure,
trainee surgeons can sense and learn the suggested path
applied to their hands.
ACKNOWLEDGMENTS
NIMAD-INSF Grant...
REFERENCES
[1] E. Yanik et al., “Deep neural networks for the assessment of
surgical skills: A systematic review,” The Journal of Defense Mod-
eling and Simulation: Applications, Methodology, Technology, vol.
19, no. 2. SAGE Publications, pp. 159–171, Aug. 20, 2021. doi:
10.1177/15485129211034586.
[2] K. Lam et al., “Machine learning for technical skill assessment in
surgery: a systematic review,” npj Digital Medicine, vol. 5, no.
1. Springer Science and Business Media LLC, Mar. 03, 2022. doi:
10.1038/s41746-022-00566-0.
[3] A. Rashvand, M. J. Ahmadi, M. Motaharifar, M. Tavakoli, and
H. D. Taghirad, “Adaptive Robust Impedance Control of Haptic
Systems for Skill Transfer,” 2021 9th RSI International Conference
on Robotics and Mechatronics (ICRoM). IEEE, Nov. 17, 2021. doi:
10.1109/icrom54204.2021.9663486.
[4] A. Rashvand et al., “An Observer-Based Responsive Vari-
able Impedance Control for Dual-User Haptic Training Sys-
tem,” 2022 IEEE/RSJ International Conference on Intelli-
gent Robots and Systems (IROS). IEEE, Oct. 23, 2022. doi:
10.1109/iros47612.2022.9981977.
[5] M. J. Ahmadi et al., “ARAS-Farabi Experimental Framework for
Skill Assessment in Capsulorhexis Surgery,” 2021 9th RSI Interna-
tional Conference on Robotics and Mechatronics (ICRoM). IEEE,
Nov. 17, 2021. doi: 10.1109/icrom54204.2021.9663494.
[6] M. Ershad, R. Rege, and A. M. Fey, “Adaptive Surgical Robotic
Training Using Real-Time Stylistic Behavior Feedback Through
Haptic Cues.” arXiv, 2021. doi: 10.48550/ARXIV .2101.00097.
[7] E. Zahedi, F. Khosravian, W. Wang, M. Armand, J. Dargahi, and
M. Zadeh, “Towards Skill Transfer via Learning-Based Guidance in
Human-Robot Interaction: An Application to Orthopaedic Surgical
Drilling Skill,” Journal of Intelligent &amp; Robotic Systems, vol.
98, no. 3–4. Springer Science and Business Media LLC, pp. 667–678,
Nov. 05, 2019. doi: 10.1007/s10846-019-01082-2.
[8] P . Fekri, J. Dargahi, and M. Zadeh, “Deep Learning-Based
Haptic Guidance for Surgical Skills Transfer,” Frontiers in
Robotics and AI, vol. 7. Frontiers Media SA, Jan. 20, 2021. doi:
10.3389/frobt.2020.586707.
[9] M. Lafouti et al., “Surgical Instrument Tracking for Capsulorhexis
Eye Surgery Based on Siamese Networks,” 2022 10th RSI Interna-
tional Conference on Robotics and Mechatronics (ICRoM). IEEE,
Nov. 15, 2022. doi: 10.1109/icrom57054.2022.10025355.
[10] Walker HK, Hall WD, Hurst JW, editors. Clinical Methods: The
History, Physical, and Laboratory Examinations. 3rd ed. Boston:
Butterworths; 1990. PMID: 21250045.
[11] A. Soleymani, A. A. Sadat Asl, M. Yeganejou, S. Dick, M. Tavakoli,
and X. Li, “Surgical Skill Evaluation From Robot-Assisted Surgery
Recordings,” 2021 International Symposium on Medical Robotics
(ISMR). IEEE, Nov. 17, 2021. doi: 10.1109/ismr48346.2021.9661527.
[12] A. Soleymani, X. Li, and M. Tavakoli, “Deep Neural Skill
Assessment and Transfer: Application to Robotic Surgery
Training,” 2021 IEEE/RSJ International Conference on Intelli-
gent Robots and Systems (IROS). IEEE, Sep. 27, 2021. doi:
10.1109/iros51168.2021.9636627.
[13] I. Lenz, R. Knepper, and A. Saxena, “DeepMPC: Learning Deep
Latent Features for Model Predictive Control,” Robotics: Science
and Systems XI. Robotics: Science and Systems Foundation, Jul. 13,
2015. doi: 10.15607/rss.2015.xi.012.
[14] S. S. Pon Kumar, A. Tulsyan, B. Gopaluni, and P . Loewen,
“A Deep Learning Architecture for Predictive Control,” IFAC-
PapersOnLine, vol. 51, no. 18. Elsevier BV , pp. 512–517, 2018. doi:
10.1016/j.ifacol.2018.09.373.
[15] X. Tan, C.-B. Chng, Y. Su, K.-B. Lim, and C.-K. Chui, “Robot-
Assisted Training in Laparoscopy Using Deep Reinforcement
Learning,” IEEE Robotics and Automation Letters, vol. 4, no. 2.
Institute of Electrical and Electronics Engineers (IEEE), pp. 485–492,
Apr. 2019. doi: 10.1109/lra.2019.2891311.
[16] Gao, Yixin et al. “JHU-ISI Gesture and Skill Assessment Working
Set ( JIGSAWS ) : A Surgical Activity Dataset for Human Motion
Modeling.” (2014).
[17] N. Ahmidi et al., “A Dataset and Benchmarks for Segmentation
and Recognition of Gestures in Robotic Surgery,” IEEE Transactions
on Biomedical Engineering, vol. 64, no. 9. Institute of Electrical
and Electronics Engineers (IEEE), pp. 2025–2041, Sep. 2017. doi:
10.1109/tbme.2016.2647680.
[18] A. Neufeld, L. L. Hanson, and J. Pettey, “Teaching in the operating
room: trends in surgical skills transfer in ophthalmology,” Annals
of Eye Science, vol. 2. AME Publishing Company, pp. 41–41, 2018.
doi: 10.21037/aes.2017.06.05.
[19] V . Adwe, K. Bharucha, A. Hegade, R. Deshpande, M. Deshpande,
and V . S. Kalyani, “Evaluation of skills transfer in short-term pha-
coemulsification surgery training program by International Council
of Ophthalmology -Ophthalmology Surgical Competency Assess-
ment Rubrics (ICO-OSCAR) and assessment of efficacy of ICO-
OSCAR for objective evaluation of skills transfer,” Indian Journal
of Ophthalmology, vol. 68, no. 8. Medknow, p. 1573, 2020. doi:
10.4103/ijo.ijo 2058 19.
[20] G. Prakash, V . Jhanji, N. Sharma, K. Gupta, J. S. Titiyal, and
R. B. Vajpayee, “Assessment of perceived difficulties by residents
in performing routine steps in phacoemulsification surgery and
in managing complications,” Canadian Journal of Ophthalmology,
vol. 44, no. 3. Elsevier BV , pp. 284–287, Jun. 2009. doi: 10.3129/i09-
051.
[21] M. J. Ahmadi, I. Gandomi, P . Abdi,et al., “Cataract-LMM Large-
Scale Multi-Source Multi-Task Benchmark for Deep Learning in
Surgical Video Analysis,”Scientific Data, vol. 13, p. 1189, 2026. doi:
10.1038/s41597-026-07464-0.
[22] J. B. Randleman, “The Resident Surgeon Phacoemulsification
Learning Curve,” Archives of Ophthalmology, vol. 125, no. 9.
American Medical Association (AMA), p. 1215, Sep. 01, 2007. doi:
10.1001/archopht.125.9.1215.
[23] C. Chen et al., “Crowd-Sourced Assessment of Technical Skills:
a novel method to evaluate surgical performance,” Journal of
Surgical Research, vol. 187, no. 1. Elsevier BV , pp. 65–71, Mar. 2014.
doi: 10.1016/j.jss.2013.09.024.
[24] L. A. Gatys, A. S. Ecker, and M. Bethge, “Image Style Transfer
Using Convolutional Neural Networks,” 2016 IEEE Conference on
Computer Vision and Pattern Recognition (CVPR). IEEE, Jun. 2016.
doi: 10.1109/cvpr.2016.265.
[25] J. Johnson, A. Alahi, and L. Fei-Fei, “Perceptual Losses for
Real-Time Style Transfer and Super-Resolution.” arXiv, 2016. doi:
10.48550/ARXIV .1603.08155.
[26] Y. Li, N. Wang, J. Liu, and X. Hou, “Demystifying Neural Style
Transfer,” Proceedings of the Twenty-Sixth International Joint Con-
ference on Artificial Intelligence. International Joint Conferences
on Artificial Intelligence Organization, Aug. 2017. doi: 10.24963/ij-
cai.2017/310.
