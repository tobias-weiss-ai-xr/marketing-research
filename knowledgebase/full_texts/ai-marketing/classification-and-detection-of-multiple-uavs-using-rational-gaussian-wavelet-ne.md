---
title: Classification and detection of multiple UAVs using rational Gaussian wavelet neural networks
url: https://arxiv.org/abs/2605.26310
category: ai-marketing
subcategory: measurement
date: 2026-05
venue: ''
authors:
- Ungvári Gergő
- Ferenc Braun
- Attila Ámon
- Péter Kackstädter
- János Volk
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.26310
pages: 19
chars: 44594
fetched_at: '2026-11-08T13:27:39+00:00'
kb_version: 1
---

# Classification and detection of multiple UAVs using rational Gaussian wavelet neural networks

Classification and detection of multiple UA Vs
using rational Gaussian wavelet neural networks
Gerg˝ o Ungv´ ari1,2, Ferenc Braun 6, Attila ´Amon1,5,
P´ eter Kackst¨ adter3, J´ anos Volk6, P´ eter Kov´ acs1*, Tam´ as D´ ozsa2,4
1*Department of Numerical Analysis, E¨ otv¨ os Lor´ and University,
P´ azm´ any P´ eter s´ et´ any, Budapest, 1117, Hungary.
2System and Control Laboratory, HUN-REN Institute for Computer
Science and Control, Kende utca, Budapest, 1111, Hungary.
3Szent Gy¨ orgy Hang- ´ es Filmm˝ uv´ eszeti Technikum, Lenhoss´ ek utca,
Budapest, 1096, Hungary.
4Department of Mathematics and Computer Science,
UniDistanceSuisse, Schinerstrasse, Brig-Glis, 3900, Switzerland.
5Siemens Mobility Kft., G´ abor D´ enes utca, Budapest, 1117, Hungary.
6HUN-REN Centre for Energy Research, Konkoly-Thege Mikl´ os ´ ut,
Budapest, 1121, Hungary.
*Corresponding author(s). E-mail(s): kovika@inf.elte.hu;
Contributing authors: aele02@inf.elte.hu; braun.ferenc@ek.hun-ren.hu;
ze3vjn@inf.elte.hu; kackstadter.peter@broadcast.hu;
volk.janos@ek.hun-ren.hu; tamas.dozsa@unidistance.ch;
Abstract
The detection of unmanned aerial vehicles (UA Vs) is important for the pro-
tection of civilian and military infrastructure. In this paper we propose a cost
effective UA V detection system using sound signals obtained from microphones.
The recorded signals are passed through a signal processing pipeline which
employs interpretable adaptive feature extractors using so-called rational Gaus-
sian wavelets. These adaptive wavelet transformations are embedded into and
trained together with an underlying small neural network which detects and
classifies UA Vs based on the obtained features. This leads to a physically inter-
pretable machine learning algorithm that in addition to classifying UA Vs is
also capable of detecting UA V swarms. We demonstrate our results using data
collected in indoor studio and noisy outdoor environments. We conclude that
1
arXiv:2605.26310v2  [cs.LG]  31 May 2026

the proposed method outperforms traditional machine learning approaches for
detecting and classifying single UA Vs as well as drone swarms, while retaining a
high degree of interpretability. Our implementation of the proposed methods is
made publicly available for reproducibility.
Keywords:Drones, wavelets, machine learning, explainability, neural networks
1 Introduction
The detection and classification of unmanned aerial vehicles (UA Vs) has become an
important problem in recent years. UA Vs, also commonly known as drones, have been
successfully applied for the delivery of goods, agriculture and various other civilian
industries [1]. On the other hand, exploiting their ability to carry weaponry and surveil-
lance equipment, UA Vs have found a large array of military applications and play
an ever increasing role on the modern battlefield [2–4]. In addition, drones provide a
cost efficient method for criminal groups to carry out illegal activities such as smug-
gling [5, 6] and disrupting industry and air traffic [1, 6]. We recommend [1] and [7] for
a deeper discussion on the different threats posed by malicious UA V activity.
In order to counter the threat posed by drones, the development of trustworthy and
affordable technology to detect and classify UA Vs is necessary. Accordingly, several
recent works consider the problem of drone detection using a variety of technologies.
The detection and classification of drones is a difficult measurement and signal pro-
cessing task for a number of reasons. Depending on the type of the UA V, its sound,
radar or visual signatures can vary widely [8]. In addition, the measurement appara-
tus usually needs to operate in an outside environment subject to sudden changes in
weather conditions and significant background noise [8]. The appearance of so-called
drone swarms, where multiple UA Vs perform a coordinated task, further complicates
potential defense strategies [1].
Current state-of-the-art technologies [1, 7] consider signals obtained from different
types of sensors accompanied by a diverse array of signal processing methods to detect
drone activity. Due to the above highlighted difficulties, it is generally accepted that
a high performance UA V detection system should incorporate a variety of signals
obtained from different sensors. The design of such a system can also depend on other
factors, such as the type of infrastructure it is intended to protect, the overall cost
of the system and specifics related to the environment (such as predictable weather
conditions, noise pollution levels, etc.). Nevertheless, drone detection subsystems that
depend on a single mode of measurement are an important field of study, as these
provide the components of an overall drone detection system.
Current UA V detection and classification technologies can be divided into four
classes depending on the type of measurements they rely on. Radar based methods
(see e.g., [9, 10]) use radio waves to detect objects. Advantages of this technology
include robustness against weather conditions, long range and being able to detect
the speed and direction of UA Vs [1]. Unfortunately, the detection of smaller drones
is a difficult task for radar systems due to small radar cross sections and low flying
2

altitudes. In addition, radar based systems are costly due to the complexity of the
involved instrumentation.
Vision based detection systems usually employ image processing to analyze
recordings from cameras [11]. These are very cost effective and can provide visual
confirmation of UA Vs, however their performance can be hindered by visibility and
weather constraints. In addition, a visual detection system is only able to detect UA Vs
in its line of sight.
Another interesting family of detection methods attempts to recognize drone activ-
ity by capturing and analyzing wireless signals. Methods belonging to this family
include [12, 13]. Benefits of radio frequency analysis include a long operating range
and the ability to classify different types of UA Vs. On the other hand these meth-
ods cannot identify autonomous drones [1] or drones controlled by non-wireless means
such as carbon-optic fibers [14].
Finally, we mention UA V detection systems that operate by recoding sound in the
surrounding area [15, 16]. These systems are easy to deploy and are cost effective.
Additional advantages of sound based detection schemes include the ability to classify
recognized drones, estimate the position of UA Vs [1] and the ability to operate with-
out a line of sight to the target. Difficulties associated with acoustic drone detection
systems include background noise filtering and vulnerability to wind conditions.
In this study, we consider a novel sound based drone detection system. We show
that through the use of appropriate signal processing methods, the proposed system
is able to
1. Mitigate the effect of wind and other background noise, by learning frequency
signatures characteristic of UA Vs of interest,
2. Classify UA V types based on the learned signatures,
3. Recognize drone swarms, that is, distinguish between intrusions by a single UA V
and groups of drones.
In this study, we assume that the drones-to-be-detected, are small, electrical vehicles
that are traditionally difficult to recognize [1, 7]. To reduce the cost of the system,
we employ microphones based on micro-electro-mechanical systems (MEMS) technol-
ogy and a mathematically justified, so-called model driven machine learning (ML)
paradigm.
The use of the proposed novel signal processing scheme clearly distinguishes our
approach from previous sound based UA V detection technologies. Although previous
drone detectors employing artificial intelligence methods on sound signals have been
introduced in [15] and [16], these rely on traditional machine learning architectures.
While deep learning based approaches achieve high performance [17], model parame-
ters do not carry physical meaning. Thus, the output of such models is not explainable.
This poses concerns for safety-critical applications such as drone detection. In addi-
tion, the size of deep neural models often requires specialized hardware for real-time
use, which can lead to increased deployment and maintenance costs.
In contrast, certain previous methods [15] apply static feature extraction steps to
obtain meaningful information from recorded sound signals. The extracted features
are then passed to different ML models, which are usually smaller than their deep
3

learning counterparts [17]. Features are often extracted using time-frequency trans-
formations, and thus the obtained information is interpretable. On the other hand,
previous methods only considered static feature extractors. That is, these methods
apply a fixed transformation (e.g., short time Fourier transform [15]) to each sound
segment. This leads to sub-optimal signal representation, because the feature extractor
methods cannot adapt to different UA V types, maneuvers and changing environmental
conditions.
In contrast, our proposed approach relies on adaptive feature extraction transfor-
mations embedded into small neural networks. The proposed model is suitable for
real time applications on limited hardware and extracts physically meaningful infor-
mation from the sound signals. Furthermore it provides feature transformations that
can adapt to different sound signatures and changing environmental factors.
The proposed signal processing pipeline falls into the category of so-called model
driven machine learning approaches. These mathematically justified ML models are
fully, or partially interpretable and can be used in safety-critical applications. Impor-
tantly, such methods retain the generalization abilities of classical deep learning
approaches, at least in the context of the application to which they are deployed. A
number of model driven ML methods have been recently introduced, including variable
projection based neural networks [18] and kernel methods [19]. Other recent examples
of model driven ML methods include wavelet convolution neural networks [20, 21].
In the current study, we propose a new wavelet convolution layer (and a corre-
sponding model driven neural network) that uses so-called rational Gaussian wavelet
(RGW) kernels [22]. RGW is a recently introduced class of admissible wavelets, whose
morphology can be greatly influenced through a number of parameters. The proposed
layer can learn the shape of the optimal mother wavelet, as well as a finite number
of scales (corresponding to pseudo frequencies [23]) that can be used to detect and
classify UA Vs.
Below, we summarize the most important novelties of our study
1. We propose a novel, RGW convolution based model driven neural network. The
proposed signal processing model obtains physically meaningful wavelet coefficients
from the recorded sound signals. These adaptively extracted features are then
processed by a small neural network to detect UA V presence and classify UA V
types.
2. We demonstrate that our proposed wavelet kernel convolution based machine
learning model can be used to detect the presence of groups of UA Vs.
3. We compare the proposed signal processing approach to several baseline machine
learning methods. We show that in addition to the inherent interpretability of the
proposed model, it significantly outperforms traditional ML methods for drone
detection. All of our experiments are completely reproducible using our publicly
available python implementation of the proposed methods (see data and code
statement at the end of the article).
4. We propose a cost-effective, sound based system for UA V detection and classifica-
tion with a light weight, interpretable ML based signal processing unit.
The rest of this paper is organized as follows. In section 2, we described the hard-
ware used to collect our dataset and the different measurement scenarios. Section 3
4

provides an overview of the most important properties of the collected sound signals.
These properties provide justification for the proposed signal processing pipeline. In
section 4, we review some important properties of rational Gaussian wavelets [22] and
introduce interpretable RGW convolution layers. These are then used to construct a
small, partially interpretable neural network for drone detection. Section 5 details our
experiments and results. Finally, in section 6 we summarize our findings and discuss
future research directions.
2 Data acquisition
In the studio environment, an Audio/Video Recorder (Video Devices PIX 270i)
received the HD-SDI signal from a wide-angle camera and simultaneously generated a
48 kHz word clock signal that was phase-locked to the video reference. Audio record-
ings were captured at a sampling rate of 192 kHz with a 24-bit resolution in signed
Linear Pulse Code Modulation (LPCM) format. The word clock from the PIX 270i
was distributed to a Master Clock Generator (Apogee Big Ben), which operated as
a frequency multiplier to derive a 192 kHz reference. The Big Ben provided this syn-
chronized 192 kHz word clock to an Audio Interface System (Focusrite RedNet) and
the associated Digital Audio Workstation (Pro Tools), ensuring a common time base
across all microphone channels. The PIX 270i also recorded the video feed along with
an analog reference from one of the microphones, allowing precise post-synchronization
between the audio and video domains. The microphones used in the studio were Br¨ uel
& Kjær 4006 and Schoeps MK2 with CMC5 preamplifiers, all of which are pressure-
type electroacoustic transducers, ensuring the most phase-coherent data acquisition
possible.
To simulate real environmental conditions relevant to the intended system applica-
tion, a microphone array equipped with commercial MEMS transducers was deployed
outdoors. The recordings were carried out at a sampling rate of 8 kHz with a 16-
bit resolution in signed LPCM format. The acoustic environment included intense
background noise sources such as helicopter overflights, nearby road traffic, human
speech, and strong wind. As the four microphones were mounted on a common PCB
and shared identical signal-conditioning and acquisition circuitry, their outputs were
recorded in temporal synchronization relative to each other.
The experiments were conducted using several commercially available multirotor
UA Vs, representing different size classes, acoustic signatures, and propulsion con-
figurations. The DJI Mavic Pro and Mavic Pro 2 are foldable quadcopters with a
takeoff weight of approximately 734 g and 907 g, respectively. Both platforms use four
two-blade rotors with typical hover-speed ranges between 5000–7800 RPM.
The DJI Mavic Mini is an ultralight (249 g) quadcopter equipped with four two-
blade rotors, operating at higher fundamental rotor frequencies due to its smaller
propeller diameter and reduced inertia.
For outdoor measurements, additional UA V types were included, such as the DJI
Mavic 3 Pro (958 g, 4 rotors), the DJI Avata 2 (cinewhoop-style ducted quadcopter,
377 g, high-RPM 3-blade rotors), and the DJI Matrice 30T, a larger industrial platform
5

weighing approximately 3.7 kg and equipped with four large-diameter two-blade rotors
rotating at significantly lower RPM ranges (2500–4200 RPM).
These platforms cover a broad acoustic spectrum: lightweight high-RPM systems
produce higher-frequency harmonic structures, while heavier drones exhibit stronger
low-frequency components. This diversity enables robust evaluation of the proposed
signal processing and classification methodology.
UA V Model Mass Rotors Blades/rotor Typical RPM
DJI Mavic Pro 734 g 4 2 5000–7800
DJI Mavic Pro 2 907 g 4 2 5000–7800
DJI Mavic Mini 249 g 4 2 6000–8500
DJI Mavic 3 Pro 958 g 4 2 4800–7200
DJI Avata 2 377 g 4 (ducted) 3 9000–12000
DJI Matrice 30T 3.7 kg 4 2 2500–4200
T able 1Technical specifications of the UA V platforms used in the study
3 Signal description
We review some important properties of the sound signals obtained from the front-
facing Schoeps MK2 microphones described in section 2. Audio recorded from a single
such microphone was used to generate the results presented in Section 5 relating to
the indoor measurements, thus the input to the proposed methods are 1D signals (see
Fig. 1). We note that even though the sound signals obtained from our noisy outdoor
measurement scenario are worse quality, the characteristics discussed here remain true
for them, which is also reflected by our experimental results (see section 5). The signals
considered here have been recorded with a sampling rate of 192 kHz. The audio data
is split into 100 ms long, non-overlapping segments. Thus input samples consisted
of arrays containing 19200 amplitude values each. The only other preprocessing step
applied to the recorded sound signals was normalization, so that the values in every
segment had a mean of 0 and standard deviation 1.
As noted in [1, 15–17], the frequency profiles of the audio signals carry notice-
able differences, characteristic of each drone model. This can also be seen in Fig. 2,
as certain features appear consistently in the spectrogram, or the time-frequency rep-
resentation obtained from the Morlet-transform of signals, only when audio from a
Mavic Pro type drone is present.
The characteristics of these features, however, can be subject to change depending
on factors other than the model, such as the position, or the movement of the drone.
Furthermore, the measured signal segments do not exhibit periodic behavior. If the
transformations used during the classification pipeline are not translation invariant,
the position (in time) of the identifying features may be subject to change as well.
These qualities of the audio signals mean that drone detection is a nonlinear classi-
fication problem of nonstationary and nonperiodic signals. In section 4 we introduce an
ML model based on adaptive rational Gaussian wavelet convolution operators, that can
6

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Time (s)
-4
-2
0
2
4
Amplitude
#10 7 Mavic audio data
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Time (s)
-4
-2
0
2
Amplitude
#10 7 Mavic and Mavic 2 audio data
Fig. 1Audio signals of a Mavic drone (left) and a Mavic and Mavic 2 drones flying at 1 meter high.
successfully process these types of signals. The experimental results of section 5 demon-
strate that the scheme provides an apt solution to the identification and classification
problem set in this paper.
4 Rational Gaussian Wavelet convolution networks
Given a signalfand functionψ, the continuous wavelet transform of the signal is
defined as
Wψ(λ, τ) =
Z +∞
−∞
f(t) ψλ,τ (t)dt,(1)
where
ψλ,τ (t) := 1√ λ ψ  1 λ (t−τ)  (t, λ, τ∈R, λ̸= 0).
We refer to the functionψas the mother wavelet, whileλandτdenote so-called
dilation and translation parameters, respectively. Given fixed parametersλandτ,
7

Fig. 2Time-scale representation of audio signals of the Mavic Pro and Mavic Pro 2 drones taken
indoors, with very little noise present. The top left signal is the Mavic Pro flying at 1 meter high and
the top right is the Mavic Pro flying at 4 meters. The bottom is both the Mavic and Mavic 2 flying at
1 meter. The time-scale representation have been obtained via continuous wavelet transform, using
Morle-wavelets.
the numberW ψ(λ, τ), is called a wavelet coefficient and it describes the similarity
betweenfandψ λ,τ . We shall assumeψ, f∈L 2(R) henceforth, which is a sufficient
condition for (1) to exist. Furthermore, if the mother waveletψsatisfies the so-called
admissibility property [23], then the transformation (1) is invertible (in theL 2(R)-
sense). TheW ψ coefficients describe the so-called time-scale representation offwhich
is closely related to time-frequency representations [23].
In [22] the authors introduce a family of wavelet functions, called ratio-
nal Gaussian wavelets (RGW). RGWs are defined with a parameter vectorη:=
[t1, t2, ..., tp, z1, z2, ..., zn] as
ψη(t) =C(η)P η(t)vη(t)e −t2 2 (t∈R,η∈C p+n),(2)
whereCis a constant that depends only onη. The rational termP η(t)vη(t) is defined
as
P η(t) =t
pY
k=1
(t−t k)(t+t k),(t k ∈C\{0}, p∈N) (3)
8

-2 -1.5 -1 -0.5 0 0.5 1 1.5 2
-4
-2
0
2
4
Rational Gaussian function (p=2,z=2)
-2 -1.5 -1 -0.5 0 0.5 1 1.5 2
-1
-0.5
0
0.5
1
#10 -3 Rational Gaussian function (p=10,z=10)
Fig. 3Rational Gaussian functions of Eq. (2), with parameterspandz.
andv η ∈ V, where
V:=
(
v(t) = 1Qn−1
k=0 (t−z k)(t+z k)(t− ˜zk)(t+ ˜zk)
, n∈N
)
(4)
and
˜z:=−ℜ(z) +iℑ(z).
For simplicity, in this work we assume{t k}n k=1 ⊂R. In [22] the admissibility ofψ η
is proven, thus (in theory)fcan be reconstructed from its RGW wavelet coefficients.
Fig. 3 illustrates some RGW mother wavelets with differentηparameter choices.
Fig. 3 also demonstrates how the large number of parameters offers a high degree
of flexibility for influencing the morphology of the mother wavelet. This property of
RGW wavelets is also well exploited in section 5 of this study.
9

In [21] a wavelet based convolution kernel has been introduced, using a fixed mother
wavelet, with the translation and dilation pairs as learnable parameters. The approach
in [21] differs from the one introduced in this article in two regards. First, our use
of RGWs allows us to optimize the morphology of the mother wavelet. Secondly, our
proposed RGW convolution layer only considers the scalesλ k (k= 1, . . . , N, N∈N)
as free parameters. The reason for this is that learning exact translation parameters
would increase the size of the convolution layer without affecting the model’s accuracy
in any meaningful capacity.
An important novelty of the current study is the construction of so-called RGW
convolution operators. Define the functionψ λ as
ψλ(t) := 1√ λ ψ  t λ  (t∈R, λ >0).(5)
The wavelet coefficientsW ψ(λ, τ) from Eq. (1), where (τ∈R) can then be written as
Wψ(λ, τ) = (f∗ψ λ)(τ) =
Z +∞
−∞
f(t) ψλ(t−τ)dt.
In practical cases the signals that have to be processed are usually only available in a
discretely sampled form. Let
fk =f(t k) (t k ∈R +, k= 1, ..., N),
and consider the notationf:= (f 1, f2, ...fN )∈R N . Let furthermore
ψη λ,k :=ψ η λ (tk) (k= 1, ..., M)
denote the discrete sampling of the waveletψ λ (see Eq. (5)).
Then, the wavelet coefficients offcan be approximated with the discrete
convolution
[f∗ψ η λ]k :=
kX
j=1
f jψη λ,k−j+1 .(6)
Previous applications of RGW wavelets considered approximating wavelet coef-
ficients using variable projection operators [24, 25]. This approach however heavily
depends on the periodic, or quasi-periodic property of the signal. As shown in Fig. 1
and in Fig. 2, the audio signals considered in this paper are not periodic, thus vari-
able projection based computation of RGW coefficients will not capture meaningful
features. To overcome this issue, we propose discrete convolution layers with RGW
kernels, that are
1. capable of extracting meaningful features from non-periodic signals using discrete
convolutions,
2. allow for a high degree of adaptivity of the mother wavelet’s morphology due to
the nature of RGW.
10

The key component of the proposed model driven neural network is the RGW
convolution layer. This layer applies discrete convlutions (see Eq. (6)) to the 1Dinput
signals, where the kernelψ η λ is an RGW wavelet characterized by a dilation parameter
λ >0 and the parameters inη∈R p+n. This vector contains the zerost k (k= 1, . . . , p)
of the polynomial term from Eq. (3) and the polesz j (j= 1, . . . , n) from Eq. (4).
Together they greatly influence the shape of the RGW mother wavelet and can be
collected to a single vector by
η= (t 1, t2, ..., tp, z1, z2, ..., zn)∈C n+p
(n, p∈N).
The transformation characterizing the proposed RGW layer is defined by
f→T ηf=


f∗ψ η λ1
f∗ψ η λ2
...
f∗ψ η λm

 =:


Wψη (λ1)
Wψη (λ2)
...
Wψη (λm)

 ∈R m×(N+M−1) ,(7)
wheref∗ψ η λk (k= 1, . . . , m) is the discrete convolution defined in (6). The Jacobian matrix of (7), with respect toη, can be easily computed:
 ∂Tηf
∂η

λk
=f∗ ∂ψ η λk
∂η .(k= 1,· · ·, m).(8)
In [22], the authors offer a formula for computing partial derivatives ofψ η λk with regards tot k andz k. We rely on this formulation to implement the proposed RGW
convolution layer.
The convolution layer is followed by a pooling layer, and a fully connected layer.
The pooling layer uses a scheme in which, for everyλ k (k= 1, . . . , m) scale, only the
wavelet coefficient of the maximal value is retained.
M P(Tηf) =


topQ(|Wψη (λ1)|)
topQ(|Wψη (λ2)|)
...
topQ(|Wψη (λm)|)

 ∈R m×Q,(9)
where the operator topQ selects theQ∈Nlargest elements of the argument vector.
This allows the proposed neural network architecture to retain physically meaning-
ful information in the following sense. Notice that thek-th component ofM P(T ηf)
encodes theQmaximum similarity scores achieved betweenfandψ η λk (k= 1, . . . , m). Since for a fixedλ k dilation the vector of wavelet coefficientsW ψη (λk) (see Eq. (7))
corresponds to a pseudo frequency, the output ofM P(T ηf) can be interpreted as the
maximal amplitude present in the input signalfat the frequency band defined byλ k.
11

Scenario id. T ask Location No. of UA V TypesNo. of UA Vs No. of Classes
1. Multiple UA V Detection Indoor 3 3 3
2. Classification Indoor 3 1 3
3. Detection Outdoor 4 1 2
T able 2Considered experimental scenarios. The number of UA Vs refers to the maximum number
of individual UA Vs present in a single segment, while the number of UA V types refers to the total
number used in that scenario.
Scenario id. Location No. of Categories Segments Per Category Segment Length
1. Indoor 3 1790 100 ms
2. Indoor 3 1000 100 ms
3. Outdoor 2 1050 100 ms
T able 3Structure of the datasets used in the individual experiments.
5 Experiments
We conducted a number of experiments to demonstrate the effectiveness of RGW
convolution networks for audio-based UA V detection. As described in section 2, our
dataset includes indoor and outdoor measurement scenarios along with several differ-
ent types of drones and drone swarms. Accordingly, different experimental scenarios
were considered for the detection and classification of a single, or multiple UA Vs. The
considered scenarios are described as follows.
1. Differentiating between the presence of a single UA V, and multiple UA Vs. The
recordings used for this experiment were taken in a studio environment. The three
categories are no drones being present, the presence of a single UA V, and the
presence of multiple UA Vs (up to three). The UA V models used for this experiment
were DJI Mavic Pro, DJI Mavic Pro 2, and DJI Mavic Mini.
2. The classification of a single UA V in a studio environment. In this case, the model
receives an audio segment with a single UA V present and has to differentiate
between three possible models (Mavic Pro, Mavic Pro 2 and Mavic Mini).
3. Detecting the presence of a single UA V outdoors, in a noisy environment. The
categories are the same as in Scenario 1. The UA V models used for this scenario
are Avata 2, Matrice 30T, Mavic Mini and Mavic Pro 3.
Table 2 gives a summary of the considered scenarios. The outdoor experiment
(as described in section 2) can be regarded as extremely noisy, while the indoor
experiments as noise free.
In each experiment, the recorded sound samples were subjected to an identical
preprocessing regime described in section 3. The proposed ML models were very sim-
ilar for each measurement scenario as well. The most significant difference, between
the models used for indoors and outdoors scenarios, is the size of the used wavelet
convolution kernel (7). In case the size of the kernel does not equalN, the size of the
convolution output will not bem×N, however it is dependant the size of the kernel
12

and the input, and is different in each scenario. The considered neural network is com-
posed of an RGW convolution layer, followed by two fully connected layers with ReLU
activation functions before each. The output of the RGW layer is first normalized:
Wψη (λk)−E(W ψη (λk))
V ar(Wψη (λk)) ,
whereEis the mean andV aris the variance, then downsampled with a pooling
layer. The pooling layer is unique, in that it samples the dominant coefficients for each
λk (k= 1, . . . , m) dilation parameter, essentially functioning as a 1-dimensional filter,
as described in Eq. (9). The activation function after the final layer is either sigmoid,
in the binary classification case, or softmax, in the case of multiple categories.
The number ofpandnlearnable parameters used to determine the morphology
of the RGW mother wavelet was chosen asp= 1 andn= 10. In these experiments,
we considered 10 wavelet filters (the number of scalesm= 10).
The classifier block used after the RGW layer consists of a single fully connected
layer with 200 neurons. The model is trained for 300 epochs with a batch size of 64.
Each individual experiment was evaluated via 5-fold cross-validation. The training
consisted of randomly splitting the total training data 80-to-20 into a training set,
which has been used to fit the model parameters and a test set, on which the accuracy
of the model was evaluated. This process has been repeated a total of five times for the
experiment, and in the following tables the mean, minimum and maximum accuracy
can be seen.
Model performance has been compared to several baseline ML methods. For this
purpose, we considered the Random Forest (RF) classifier [26], linear and radial Basis
kernel SVM (SVM-L and SVM-RBF) classifiers [27], as well as the naive Bayes clas-
sifier [28] (NB). In addition, we conducted experiments on these scenarios using fully
connected (FCNN) as well as convolutional (CNN) neural networks. In each scenario
the structure of the FCNN model, and the fully connected layers in the CNN model
were identical to the structure of the fully connected layers of the RGW-kernel (7)
model used in that scenario. Furhtermore, the number of channels, and the size of the
convolution layer in the used CNN model had been identical to the one used for the
RGW convolution layer. The results are shown in the following tables 4, 5 and 6.
The accuracy of the trained models are calculated by
Acc= Ntp +N tn
Ntotal
,(10)
whereN tp andN tn are the number of true positive and true negative prediction
respectively, andN total is the total number of segments in the test set.
In the following subsections we describe each experimental scenario in detail. We
note that all of the hyperparameters were determined using a large grid search of the
parameter space. To ensure full reproducibility of our results, we direct the reader to
the data and code availability statement at the end of the article.
5.1 Detecting swarms in a studio environment
The summary of our experimental scenarios can be found in 2. In this section we
consider the indoors experimental scenario wich we label with id. 1. Our dataset
13

+
+
+...
X
X
Mavic Pro
Mavic Pro 2
Mavic Mini
RGW Block
Fig. 4Schematic model of the neural network used for our experiments. The samples are fed first
into an RGW convolution layer for feature extraction, then to a fully connected block, used for
classification.
contains three labels: a category containing samples with only background noise, a
category with sounds from a single drone, and a category which contains samples with
sound recordings from multiple drones. That is, the classification task is to differentiate
between a lone drone, background noise, and the presence of multiple drones.
In this particular scenario, the length of each wavelet kernel was determined to be
32, which results in the size of the convolution output being 10×19169.
The performance of the model has been compared to baseline ML algorithms, as
introduced in the beginning of this section. The results can be seen in Table 4. The
classical methods, as well as the fully connected neural network, fail to achieve high
level of accuracy, while the RGW-kernel based network and the convolutional neural
network is able to accurately identify the UA V types. Furthermore, the RGW-kernel
based approach overperforms the convolutional neural network. It is important to note
that the RGW-kernel based model achieves this accuracy using a lot fewer parameters
and the RGW-kernel layer gives us an output whose parameters carry physical meaning
about the input signals.
Model Mean Acc. Min Acc. Max Acc.
WK-NN (proposed) 92.52% 90.50% 96.00%
RF 78.94% 77.47% 80.07%
SVM-L 50.32% 48.42% 51.96%
SVM-RBF 90.62% 89.20% 91.62%
NB 41.49% 39.85% 42.64%
CNN 90.57% 88.27% 92.26%
FCNN 48.13% 46.66% 49.03%
T able 4Results of detecting the presence of a swarm in a studio
environment (scenario 1. in Table 2).
5.2 Classifying drones in a studio environment
Next, we consider scenario 2. from Table 2. In the case of identifying drone model
types, three categories describe our dataset. Each category contains samples from a
14

single drone, where the categories themselves are characterized by the type of the UA V
that can be heard in the sample.
The parameters of the trained model had been the same as the model used in
section 5.1, with the exception of the activation function at the end being Softmax
instead of Sigmoid.
The results can be seen in Table 5. Similarly to the previous scenario, the CNN
and the RGW-kernel based model are able to achieve a much higher accuracy than
the other approaches.
Model Mean Acc. Min Acc. Max Acc.
WK-NN (proposed) 99.20% 98.33% 99.83%
RF 91.53% 90.33% 92.33%
SVM-L 38.00% 36.83% 38.83%
SVM-RBF 96.37% 95.17% 97.67%
NB 48.10% 46.33% 63.92%
CNN 99.97% 99.83% 100.0%
FCNN 47.63% 43.33% 50.83%
T able 5Results of classifying the UA V model types present in a
studio recording (scenario 2. in Table 2).
5.3 Detecting drones in a noisy environment
Finally we consider experimental scenario 3. from Table 2. For this experiment, our
objective is to detect the presence of a single UA V, however the used dataset has been
collected in a much less controlled environment, being subject to a large number of
noise factors. The details of the noisy dataset are described in section 2.
Just like in the previous examples, the number of dilation parameters learned had
been 10. The numberspandnof RGW mother wavelet parameters remainedp= 1
andn= 10, however the size of the convolution kernel was raised to 64, and the size
of the convolution output changed to 10×4347. As the task is a binary classification
problem, Sigmoid had been used as an activation layer.
Table 6 contains the accuracy of the RGW-based model, as well as the accuracy of
baseline ML methods, also used in the previous experiments. As can be seen, the RGW-
kernel based model outperforms every other neural network, even the CNN model. It
is important to note that in this scenario the task has been a lot more difficult than in
the previous ones, as the audio signal was subject to heavy background noise. In this
case, the interpretability of the RGW-kernel model is especially critical, as it allows
us to verify the validity of the trained model.
6 Conclusion
In this study, we introduce a novel model-based neural network, incorporating Rational
Gaussian-based wavelet transformation. We have demonstrated the effectiveness of this
neural network by solving a series of tasks based around acoustic detection of UA Vs
15

Model Mean Acc. Min Acc. Max Acc.
WK-NN (proposed) 90.55% 87.75% 94.75%
RF 80.40% 78.00% 82.57%
SVM-L 62.34% 61.42% 63.42%
SVM-RBF 77.71% 74.85% 80.57%
NB 49.48% 48.85% 51.14%
CNN 89.60% 87.00% 91.25%
FCNN 55.90% 53.50% 58.75%
T able 6Results of detecting drone presence in a noisy
environment (scenario 3. in Table 2).
in various environments. By using a generic model, we have shown that our scheme
can achieve accurate results, and for some tasks, can even surpass the state-of-the art
CNN approach, with the use of fewer parameters and small datasets.
In the future, we plan on using more specialized models in order to achiever higher
accuracy on specific tasks, as well as to use these trained models for real time detection
and classification.
Acknowledgment
This research was funded by the Ministry of Innovation and Technology of Hungary
from the National Research, Development and Innovation Fund, financed under the
TKP2021 funding scheme, grant number TKP2021-NV A-03. TD received funding from
the Swiss Government Excellence Scholarship No. 2025.0057. This work was supported
by the University Excellence Fund of E¨ otv¨ os Lor´ and University, Budapest, Hungary
(ELTE). Project no. K146721 has been implemented with the support provided by the
Ministry of Culture and Innovation of Hungary from the National Research, Devel-
opment and Innovation Fund, financed under the K 23 ”OTKA” funding scheme.
This work was supported by the J´ anos Bolyai Research Scholarship of the Hungarian
Academy of Science. Supported by the EK ¨OP-KDP-24 university excellence scholar-
ship program cooperative doctoral program of the Ministry for Culture and Innovation
from the source of the National Research, Development and Innovation Fund.
References
[1] Seidaliyeva, U., Ilipbayeva, L., Taissariyeva, K., Smailov, N., Matson, E.T.:
Advances and challenges in drone detection and classification techniques: A
state-of-the-art review. Sensors24(1), 125 (2023)
[2] Bera, B., Das, A.K., Garg, S., Jalil P., M., Hossain, M.S.: Access control proto-
col for battlefield surveillance in drone-assisted iot environment. IEEE Internet
of Things Journal9(4), 2708–2721 (2022) https://doi.org/10.1109/JIOT.2020.
3049003
[3] Swinney, C.J., Woods, J.C.: A review of security incidents and defence techniques
relating to the malicious use of small unmanned aerial systems. IEEE Aerospace
16

and Electronic Systems Magazine37(5), 14–28 (2022)
[4] Wang, J., Liu, Y., Song, H.: Counter-unmanned aircraft system(s) (c-uas): State
of the art, challenges, and future trends. IEEE Aerospace and Electronic Systems
Magazine36(3), 4–29 (2021)
[5] Samaras, S., Diamantidou, E., Ataloglou, D., Sakellariou, N., Vafeiadis, A.,
Magoulianitis, V., Lalas, A., Dimou, A., Zarpalas, D., Votis, K.,et al.: Deep learn-
ing on multi sensor data for counter UAV applications—A systematic review.
Sensors19(22), 4837 (2019)
[6] Dedrone Inc.: Worldwide Drone Incidents. Accessed: 25 October 2023
[7] Taha, B., Shoufan, A.: Machine learning-based drone detection and classification:
State-of-the-art in research. IEEE Access7, 138669–138682 (2019) https://doi.
org/10.1109/ACCESS.2019.2942944
[8] Mohsan, S.A.H., Othman, N.Q.H., Li, Y., Alsharif, M.H., Khan, M.A.: Unmanned
aerial vehicles (UAVs): Practical aspects, applications, open challenges, security
issues, and future trends. Intelligent service robotics16(1), 109–137 (2023)
[9] Wang, C., Tian, J., Cao, J., Wang, X.: Deep learning-based UAV Detection in
Pulse-Doppler Radar. IEEE Transactions on Geoscience and Remote Sensing60,
1–12 (2022) https://doi.org/10.1109/TGRS.2021.3104907
[10] Tanveer, L., Misbah, M., Ahmad, A., Khan, A., Iqbal, N., Kaleem, Z.: From lab
to field trials: Real-time multi-model drone detection in low snr environments.
IEEE Aerospace and Electronic Systems Magazine, 1–10 (2025)
[11] Zhao, J., Zhang, J., Li, D., Wang, D.: Vision-Based Anti-UAV Detection and
Tracking. IEEE Transactions on Intelligent Transportation Systems23(12),
25323–25334 (2022) https://doi.org/10.1109/TITS.2022.3177627
[12] Mandal, S., Satija, U.: Time–Frequency Multiscale Convolutional Neural Network
for RF-Based Drone Detection and Identification. IEEE Sensors Letters7(7), 1–4
(2023) https://doi.org/10.1109/LSENS.2023.3289145
[13] Nemer, I., Sheltami, T., Ahmad, I., Yasar, A.U.-H., Abdeen, M.A.R.: RF-based
UAV detection and identification using hierarchical learning approach. Sensors
21(6), 1947 (2021)
[14] Shindo, N., Kobatake, T., Masson, D., Fafard, S., Matsuura, M.: Optically pow-
ered and controlled drones using optical fibers for airborne base stations. In:
Photonics, vol. 9, p. 882 (2022). MDPI
17

[15] Anwar, M.Z., Kaleem, Z., Jamalipour, A.: Machine Learning Inspired Sound-
Based Amateur Drone Detection for Public Safety Applications. IEEE Transac-
tions on Vehicular Technology68(3), 2526–2534 (2019) https://doi.org/10.1109/
TVT.2019.2893615
[16] Ohlenbusch, M., Ahrens, A., Rollwage, C., Bitzer, J.: Robust Drone Detection for
Acoustic Monitoring Applications. In: 2020 28th European Signal Processing Con-
ference (EUSIPCO), pp. 6–10 (2021). https://doi.org/10.23919/Eusipco47968.
2020.9287433
[17] Wang, Y., Chu, Z., Ku, I., Smith, E.C., Matson, E.T.: A Large-Scale UAV
Audio Dataset and Audio-Based UAV Classification Using CNN. In: 2022 Sixth
IEEE International Conference on Robotic Computing (IRC), pp. 186–189 (2022).
https://doi.org/10.1109/IRC55401.2022.00039
[18] Kov´ acs, P., Bogn´ ar, G., Huber, C., Huemer, M.: VPNet: Variable projection
networks. International Journal of Neural Systems32(01), 2150054 (2022)
[19] D´ ozsa, T., Deuschle, F., Cornelis, B., Kov´ acs, P.: Variable Projection Support
Vector Machines and Some Applications Using Adaptive Hermite Expansions.
International Journal of Neural Systems34(01), 2450004 (2024) https://doi.org/
10.1142/S0129065724500047
[20] Wang, T., Lu, C., Sun, Y., Yang, M., Liu, C., Ou, C.: Automatic ECG classi-
fication using continuous wavelet transform and convolutional neural network.
Entropy23(1), 119 (2021)
[21] Li, T., Zhao, Z., Sun, C., Cheng, L., Chen, X., Yan, R., Gao, R.X.: WaveletKer-
nelNet: An interpretable deep neural network for industrial intelligent diagnosis.
IEEE Transactions on Systems, Man, and Cybernetics: Systems52(4), 2302–2312
(2021)
[22] ´Amon, A.M., Fenech, K., Kov´ acs, P., D´ ozsa, T.: Rational Gaussian Wavelets
and Corresponding Model Driven Neural Networks. IEEE Transactions on Signal
Processing73, 3140–3155 (2025) https://doi.org/10.1109/TSP.2025.3592099
[23] Daubechies, I.: Ten lectures on wavelets. Society for industrial and applied
mathematics (1992)
[24] Golub, G.H., Pereyra, V.: The differentiation of pseudo-inverses and nonlinear
least squares problems whose variables separate. SIAM Journal on numerical
analysis10(2), 413–432 (1973)
[25] Golub, G., Pereyra, V.: Separable nonlinear least squares: the variable projection
method and its applications. Inverse problems19(2), 1 (2003)
[26] Pal, M.: Random forest classifier for remote sensing classification. International
18

journal of remote sensing26(1), 217–222 (2005)
[27] Chapelle, O.: Training a support vector machine in the primal. Neural Computing
19, 1155–1178 (2007)
[28] Yang, F.-J.: An Implementation of Naive Bayes Classifier. In: 2018 International
Conference on Computational Science and Computational Intelligence (CSCI),
pp. 301–306 (2018). https://doi.org/10.1109/CSCI46756.2018.00065
Code and data availability
The python implementation of the proposed methods and experiments can be
downloaded from
https://gitlab.com/aele02/drone-classification-and-detection/-/tree/main.
Data that support the findings of this study is available from HUN-REN Centre for
Energy research, but restrictions apply to the availability of the data, which was used
under license for the current study. The data is not publicly available.
CRediT Author statement
Gerg˝ o Ungv´ ari: Formal Analysis, Software, Writing - Original Draft.F erenc
Braun: Data Curation, Writing - Original Draft.Attila ´Amon: Software, Writing -
Review & Editing.P´ eter Kackst¨ adter: Resources, Writing - Original Draft.J´ anos
V olk: Supervision, Funding Acquisition, Writing - Review & EditingP´ eter Kov´ acs:
Project Administration, Writing - Review & Editing.T am´ as D´ ozsa: Methodology,
Software, Writing - Original Draft.
Acknowledgment
This research was funded by the Ministry of Innovation and Technology of Hungary
from the National Research, Development and Innovation Fund, financed under the
TKP2021 funding scheme, grant number TKP2021-NV A-03. TD received funding from
the Swiss Government Excellence Scholarship No. 2025.0057. This work was supported
by the University Excellence Fund of E¨ otv¨ os Lor´ and University, Budapest, Hungary
(ELTE). Project no. K146721 has been implemented with the support provided by the
Ministry of Culture and Innovation of Hungary from the National Research, Devel-
opment and Innovation Fund, financed under the K 23 ”OTKA” funding scheme.
This work was supported by the J´ anos Bolyai Research Scholarship of the Hungarian
Academy of Science. Supported by the EK ¨OP-KDP-24 university excellence scholar-
ship program cooperative doctoral program of the Ministry for Culture and Innovation
from the source of the National Research, Development and Innovation Fund.
19
