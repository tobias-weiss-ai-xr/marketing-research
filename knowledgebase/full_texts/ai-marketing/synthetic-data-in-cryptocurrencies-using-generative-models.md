---
title: Synthetic data in cryptocurrencies using generative models
url: https://arxiv.org/abs/2604.16182
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- André Saimon S. Sousa
- Otto Pires
- Frank Acasiete
- Oscar M. Granados
- Valéria Loureiro da Silva
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.16182
pages: 24
chars: 59597
fetched_at: '2026-11-08T13:04:14+00:00'
kb_version: 1
---

# Synthetic data in cryptocurrencies using generative models

SYNTHETICDATA INCRYPTOCURRENCIES USINGGENERATIVE
MODELS ∗
André Saimon S. Sousa
Universidade SENAI CIMATEC
Salvador, Brazil
andre.sousa@fbter.org.br
Otto Pires
Universidade SENAI CIMATEC
Salvador, Brazil
otto.pires@fieb.org.br
Frank Acasiete
Universidade SENAI CIMATEC
Salvador, Brazil
frank.quispe@fbter.org.br
Oscar M. Granados
CoFi, Universidad Jorge Tadeo Lozano
Bogotá, Colombia
oscarm.granadose@utadeo.edu.co
Valéria Loureiro da Silva
Universidade SENAI CIMATEC
Salvador, Brazil
valeria.dasilva@fieb.org.br
Hugo Saba
Universidade do Estado da Bahia - UNEB
Salvador, Brazil
hugosaba@uneb.br
ABSTRACT
Data plays a fundamental role in consolidating markets, services, and products in the digital financial
ecosystem. However, the use of real data, especially in the financial context, can lead to privacy risks
and access restrictions, affecting institutions, research, and modeling processes. Although not all
financial datasets present such limitations, this work proposes the use of deep learning techniques
for generating synthetic data applied to cryptocurrency price time series. The approach is based
on Conditional Generative Adversarial Networks (CGANs), combining an LSTM-type recurrent
generator and an MLP discriminator to produce statistically consistent synthetic data. The experiments
consider different crypto-assets and demonstrate that the model is capable of reproducing relevant
temporal patterns, preserving market trends and dynamics. The generation of synthetic series through
GANs is an efficient alternative for simulating financial data, showing potential for applications such
as market behavior analysis and anomaly detection, with lower computational cost compared to more
complex generative approaches.
KeywordsGAN Networks·Deep Learning·Generative AI·Financial Data·Financial Assets·Cryptocurrencies
1 Introduction
Financial data has grown in several ways. In some cases, these data are exclusive to financial institutions, and they
prefer not to share them with other institutions for regulatory or strategic reasons. Open finance and open data are
realities for specific data, but transactions remain secret between institutions. Transaction records have been a highlight
in identifying anomalies such as volatility risk, operational risk, fraud, financial crime, and money laundering. However,
the models are habitually endogenous with data from each institution. This obstacle affects the deployment of methods
based on artificial intelligence. Thus, synthetic data emerges as a solution to address this challenge on different financial
datasets, which can further refine the training of deep reinforcement learning models used in money laundering control,
computational finance, or algorithmic and high-frequency trading.
∗Citation:Sousa A. S. S. et al. Synthetic Data in Finance using Generative Models. Pages.... DOI:000000/11111.
arXiv:2604.16182v1  [cs.LG]  17 Apr 2026

Synthetic Data in Cryptocurrencies
Our problem setting involves applying generative AI to enhance anomaly detection capabilities with synthetic data.
Generative AI, particularly GANs, is employed to create synthetic data that closely resembles real-world data. These
synthetic data serve as a valuable resource for training and testing anomaly detection models. By augmenting existing
datasets with synthetic data, we can address issues such as data scarcity, privacy concerns, and imbalanced class
distributions. This approach enables the development of more robust and accurate anomaly detection systems such as
volatility risk, hedging exposition, financial crime, money laundering, etc. Early research led to the development of a
synthetic information generator for use in both public and private sector research. The proposal consisted of multiple
imputations, i.e., conjugating and simulating with probabilistic sampling techniques called Bootstrap and carrying out
simulations on sets of samples with or without replacement to estimate the value [1]. The estimated value was listed as
the synthetic value with no record. Furthermore, another proposal was to find highly correlated auxiliary variables to
replace the target variable. Subsequently, other techniques were developed to create synthetic values through multiple
imputations using point estimates, supervised and unsupervised learning models, and deep learning [1].
Consequently, GANs are a class of machine learning frameworks that consist of two neural networks competing
in a zero-sum game: a generator and a discriminator. The generator’s goal is to create new data instances that are
indistinguishable from real data, while the discriminator’s goal is to accurately classify these instances as real or fake [2].
During training, the generator produces synthetic data, and the discriminator evaluates its authenticity. The discriminator
provides feedback to the generator, which then adjusts its parameters to improve the realism of its generated data. This
adversarial process continues iteratively, with both networks learning from each other [3]. Over time, the generator
becomes increasingly skilled at creating highly realistic synthetic data, while the discriminator’s ability to distinguish
between real and fake data improves. This dynamic competition drives the development of sophisticated generative
models capable of producing diverse and convincing outputs.
GANs have found a wide range of applications across various domains, including finance. Like Synthetic Data
Generation, privacy-preserving Data: GANs can generate synthetic financial data that mimics real-world data but
preserves privacy by removing sensitive information. Data augmentation, by generating synthetic data, GANs can
augment existing datasets, improving the performance of machine learning models. Stress testing, GANs can simulate
various economic scenarios to stress-test financial models and risk management strategies.
Compared to purely mathematical linear models, GANs are able to present better results in representing complex
distributions related to cryptocurrency price volatility, preserving statistical characteristics and allowing the generation
of realistic data [ 4]. The generation of synthetic data using GANs also stands out for presenting advantages in enriching
datasets in cryptocurrency contexts, increasing the accuracy of predictive models, reducing overfitting, improving
robustness, and increasing accuracy [4, 5, 6].
GANs also have applications in various areas. For example, Zhu [7] developed an algorithm for realistic photographic
manipulation of shape and color. Killoran [8] proposed generative neural network methods to create adjustable DNA
sequences. Additionally, Kadurin [9] developed a model for molecular feature extraction problems. GANs[10] stand out
as a powerful tool for data generation. They have gained significant traction in the field of generative learning and find
application in an extensive variety of domains[11, 12, 13]. In the finance domain, applications of GANs include financial
data generation[14, 15, 16], stock market prediction[17, 18, 19, 20], credit scoring[21], fraud detection[22, 23, 24], and
money laundering [25]. Several other efforts have focused on leveraging deep learning methodologies, particularly in
medical data [26, 27, 28, 29].
This work aims to gain a better understanding of financial anomalies by using synthetic data methods with GAN
networks. Indeed, we apply some tools from diffusion models that are adapted to this setting to create data and detect
the most relevant financial anomalies that develop interactions that are frequently associated with several financial issues.
For this purpose, we deploy a model to create synthetic data in cryptocurrencies as a basis for the analysis of other
financial datasets and introduce a proposal for the anomaly detection of financial transactions and operations in high
volatility contexts. We will also employ other deep learning methods as an aid in this study, other deep learning methods
to consolidate our model, which, in the case of financial data, has the advantage of having an interpretation and is
well-defined in settings where volatility increases suddenly. It is desirable for a more refined analysis of anomalies, but
it will not be attempted here since our purpose is to consider the case when only the minimum quantity of information
is available.
This work has two main contributions. First, provide clarity on the evolution of the dynamics and structure of the
three selected cryptocurrencies across different volatility periods, and assess whether properties inherent to these
cryptocurrencies and to the trading periods could have imposed limitations on the creation of synthetic data. Second, to
extend the understanding of these periods from a machine learning perspective by (a) creating a deep learning model
with combine two methods to directly create dataset by minute that built transactions in all cryptocurrencies in each
market, and (b) by providing an extensive experiments of the temporal and volatility changes in the transactions of each
of these markets during the overall period that consolidate a synthetic data with all properties of real markets.
2

Synthetic Data in Cryptocurrencies
This paper is divided as follows. In Section 2, we present some basic neural networks and GAN network terminology
employed in the text. The Sect. 3 is devoted to a brief description of the datasets used in this study, and a basic data
analysis also describes our method. In Section 4, we describe our experiments and analyze the results. Finally, we close
with a conclusion and future works in Section 5.
2 Preliminaries
Given observed samples x from a distribution of interest, the goal of a generative model is to learn to model its true data
distribution p(x). Once learned, we can generate new samples from our approximate model at will. Furthermore, we
can use the learned model to evaluate the likelihood of observed or sampled data as well. Below, some concepts are
developed to understand our proposed models.
2.1 Neural Networks
Artificial Neural Networks (ANNs) are an area of Artificial Intelligence where the structure of their model seeks to
resemble the behavior of biological neurons and, by using many layers of complex algebraic circuits, is called deep
learning [30]. The perceptron, which forms the basis of this system, can be described as a node, also called a unit, that
performs the calculation of the weighted sum of the inputs from the previous nodes and then applies a linear function in
order to generate an output [31]. The output of unit j, represented by aj, is given by the activation function gj applied
to the weighted sum of the inputsi, as expressed in the Eq. (1).
aj =g j
 X
i
wi,jai
!
≡g j(inj) (1)
where wi,j refers to the weight of the link from i to j and inj refers to the weighted sum [ 31]. It is important to
highlight that ANN architectures have specific characteristics for certain classes of problems, such as the case where
convolutional networks generalize well to spatial grids (images), while recurrent networks are better suited to sequential
data flows [31].
For the use of sequential data, Recurrent Neural Networks (RNNs) are ideal because they establish cycles in the
computation graph, allowing for memory states and the storage of temporal dependencies [31]. In an RNN, at each time
interval, the input and output are observed, and the memory state is established through the recurrence of information
processing by the hidden layer [31], as demonstrated in the Eq. (2).
zt =f w(zt−1,x t) =gz(Wz,z zt−1 +W x,zxt ≡g z(inz,t)
ˆyt =g y(Wz,y zt)≡g y(iny,t) (2)
The Long Short-Term Memory (LSTM) network follows the same principles as an RNN, adding memory cells to the
network capable of preserving information for many time intervals [ 31]. For the equation below (Eq. (3)), c refers
to the switching component that controls the flow of information; the forget gate f defines what will be forgotten
and what will be remembered; the input gate i defines which information will be added; the output gate o organizes
the short-term memory z; the subscripted weight matrices W refer to the origin and destination; and the symbol ⊙
represents element-by-element multiplication.
ft =σ(W x,f xt +W z,f zt−1)
it =σ(W x,ixt +W z,izt−1)
ot =σ(W x,oxt +W z,ozt−1)
ct =c t−1 ⊙f t +i t ⊙tanh(W x,cxt +W z,czt−1)
zt =tanh(c t)⊙o t
(3)
Figure 1a shows an example of the basic structure of an ANN, an RNN, and an LSTM, respectively, from left to right
[31] [32].
3

Synthetic Data in Cryptocurrencies

x1
x2
3
4
5 ŷ
w1,3
w1,4
w2,3
w2,4
w3,5
w4,5
a) b) c)
Δ
wz,z wx,z
wz,y
y
z
x
Forgotten door
Entrance door
Exit port
c(t-1)
h(t-1)
f(t) g(t) i(t) o(t)
FCFCFCFC
y(t)
c(t)
h(t)
x(t)
Element-by-element
multiplication
Addition
Logistics function
Tanh function
FC
FC
(a) Neural Networks: a) ANN; b) RNN; c) LSTM.
Fig. 1a
2.2 Generative Adversarial Networks (GAN)
The GAN networks involve two competing models of ANNs. The initial model, denoted as the generator (g), is trained
to generate synthetic data, while the second model, the discriminator (d), is trained to distinguish between fake and
real data. In this framework, a zero-sum cooperative game is played, in which both players attempt to optimize their
strategies to outperform their adversary. This specific context focuses on the two neural networks, ensuring a high level
of efficiency in learning by achieving convergence in the cost loss function between them. The generator refines its
learning based on the feedback received from the discriminator’s classifications [33]. The discriminator’s objective is to
determine whether the data is real (from the training dataset) or false (created by the white noise generator).
We can represent the scenario where the game competition function (min; max)is expressed between the two networks
with their goodness parameters of each one of them v

θ(g);θ (d) Eq. (4). That is, during learning, each player tries to
maximize his reward, so that the convergence is given by:
g∗ = arg min
g
max
d
v(g, d).(4)
The function is defined byf(x, v(g, d))the Eq. (5):
v

θ(g), θ(d)

=E x∼pdata(x) [logd(x)] +Ez∼pz (z) [log (1−d(g(z)))],(5)
where: (x) represents the real training data, pdata(x) of their distribution, (z) is noise with which the generator is fed to
synthesize the data, and its distribution pz(z) which is determined as the distribution of the generated data pg(z). The
first neural network, called theGenerator (g), consists of generating samples given at x=g

z;θ (g) . Its adversary, the
second neural network namedDiscriminator (d), tries to distinguish between samples drawn from the training data and
samples drawn from the generator. The discriminator outputs a probability value given by d

x;θ (d) , which calculates
or estimates a probability of x that a sample comes from the training data instead of a fake sample taken from the (g)
[34] model.
Then, learning occurs through a zero-sum game, in which a function given by v(θ(g), θ(d)) determines the reward of
the discriminator [34]. Also, the generator receives −v(θ(g), θ(d)) as its reward, so the discriminator learns to classify
4

Synthetic Data in Cryptocurrencies
the samples as real or false correctly. Simultaneously, the generator tries to trick the discriminator into believing that
its samples are real. In addition, the convergence of the generator samples is indistinguishable from the real data,
which means that the discriminator must have a high level of learning with a minimum error rate and maximize the
probabilities for the discriminator to make estimates of high performance given at the learning task as represented by
Eq. (5). Additionally, the generator (g) implicitly defines a probability distribution pg as the distribution of the samples
g(z)obtained whenz∼p z [3]. Therefore, it is sought that(g)converges to a good unbiased estimator forp data.
Generative models can be classified into GANs, Variational Autoencoders (V AEs), and AutoRegressive Networks
[35]. GAN is a Machine Learning model presented in 2014 that advances the proposal of generative models by using
backpropagation to optimize the network weights, in contrast to the use of Markov chains and approximate inference in
previous models [36]. GANs aim to indicate, through a discriminating network D and probability estimation, whether
the data distribution is real or created through the generating network G, functioning as a minimax game in its cost
function.
V AE consists of a probabilistic graphical model that aims to model the probabilistic distribution of data, but with a
certain bias, generating samples with lower quality than GANs. Regarding AutoRegressive Networks, PixelRNN is an
example that performs pixel prediction and image generation by processing the pixels one by one, while GANs process
the sample all at once, making it more efficient [35].
The generator is trained so that the probability of the discriminator making an error is maximized, while the discriminator
aims to learn whether the data sample comes from the model distribution or from the data distribution [ 36]. In its
initial proposal, the generative model creates samples by passing random noise through a multilayer perceptron, and the
discriminative model is also a multilayer perceptron [36].
The game should be implemented using an iterative numerical approach, optimizing D by alternating between k steps
and G at each step, keeping D close to its optimal solution by slowly changing G [36]. The training objective for D can
be interpreted as maximizing the log-likelihood to estimate the conditional probability P(Y=y|x) , where Y indicates
whetherxcomes fromp data (withy= 1) or fromp g (withy= 0) [36].
The generator takes as input a random noise vector z, which is typically drawn from a uniform or normal distribution.
To obtain a multidimensional vector, which is a fake sample G(z), the noise is mapped to a new data space through
the generator. Then, the discriminator receives from the data set the real sample and the fake sample created by the
generator, and delivers an output representing the probability characterizing the sample as real, instead of fake, acting
as a binary classifier. The discriminator reaches the optimal state when it learns the distribution of the real data and
makes it indistinguishable to classify the data as coming from the real or fake sample [35].
3 Materials and Methods
Several aspects are critical when developing an Artificial Neural Network (ANN) model. It has four fundamental
components: (a) the dataset; (b) the data transformation model; (c) an objective function to evaluate model quality; and
(d) a tuning algorithm for optimization [37]. The generation of synthetic data offers a methodological alternative to
the manual labeling and protection of sensitive information, such as financial records. Consequently, synthetic data
facilitates the generation of new samples while preserving the underlying relationships and attributes of the original
dataset. This data is typically classified into three categories. First, completely synthetic data, where a generator
constructs values for each variable based on probabilistic parameters. Second, partially synthetic data, which uses
statistical imputation and dimension reduction to transform information. Third, hybrid synthetic data, which integrates
elements from both real and generated sources.
Within the framework of this study (Fig 2a), the process begins by extracting cryptocurrency data (BTC, ETH, and
XRP) over a specific temporal window. Data preprocessing involves cleaning and normalizing these values based on an
analysis of the time-series characteristics. To develop the GAN architecture, we conducted a review of existing models
to identify best practices for construction and performance evaluation. Finally, we propose a model specifically tailored
to the structure of the available data.
5

Synthetic Data in Cryptocurrencies
(a) Methodological Flowchart
Fig. 2a.
3.1 Data
The general period covered in this work spans January 2022 to October 2025. We study cryptocurrencies using
minute-by-minute data across three time points. First, from March 2022 to April 2022. Second, from April 2022 to
May 2022. Third, from September 2025. This work focuses on these three periods starting from the 21st of January
2022 (when the attack of Russia on Ukraine was confirmed) and the one subsequent month. This period was selected
as it portrays the beginning of the war in Europe, as well as when the implementation of monetary policies of several
countries started to reorganize the level of interest rates, announced in the last days of March and early April of 2022.
The final period refers to the global trade changes with Trump’s strategy. This work refers to these three periods as the
“V olatility scenario” or “VS period” for short throughout this document. The dataset comes from the LSEG Platform
and contains approximately 0.5 million records covering three currencies: Bitcoin (BTC), Ethereum (ETH), and XRP.
We impose a strict survivorship filter and retain only records with all information and present over the entire sample.
This harmonizes the cross-section through time and ensures that correlation-based data are well defined.
The records have five variables: period, open, high, low, and close. For data preprocessing, we considered several
criteria regarding the quality. The data eliminated were records with some anomaly. In addition, the month, day, and
time data were extracted from the date field, thus creating three additional variables to become factors in the analysis of
the transactions. For the final dataset, we have 384465 records.
3.2 Data Analysis
The dataset, segmented into three distinct temporal windows (Fig. 4), illustrates the nature of cryptocurrency price
fluctuations during periods of significant volatility, driven by macroeconomic or geopolitical events. By analyzing the
variance of daily percentage changes, we can identify the market’s sensitivity to exogenous shocks and the subsequent
risk inherent in financial assets, including digital assets. During the first period, March–April 2022, the charts in column
(a) (Fig. 4a) reflect a market grappling with the immediate fallout of the Russian invasion of Ukraine. This period is
6

Synthetic Data in Cryptocurrencies
(a) (b)
(c) (d)
(e) (f)
0
20.000
40.000
60.000
80.000
100.000
120.000
140.000
02-ene-2022 02-jul-2022 02-ene-2023 02-jul-2023 02-ene-2024 02-jul-2024 02-ene-2025 02-jul-2025
-20%
-15%
-10%
-5%
0%
5%
10%
15%
20%
02-ene-2022 02-jul-2022 02-ene-2023 02-jul-2023 02-ene-2024 02-jul-2024 02-ene-2025 02-jul-2025
0
1.000
2.000
3.000
4.000
5.000
02-ene-2022 02-jul-2022 02-ene-2023 02-jul-2023 02-ene-2024 02-jul-2024 02-ene-2025 02-jul-2025
-20%
-15%
-10%
-5%
0%
5%
10%
15%
20%
25%
02-ene-2022 02-jul-2022 02-ene-2023 02-jul-2023 02-ene-2024 02-jul-2024 02-ene-2025 02-jul-2025
0,0000
0,5000
1,0000
1,5000
2,0000
2,5000
3,0000
3,5000
4,0000
02-ene-2022 02-jul-2022 02-ene-2023 02-jul-2023 02-ene-2024 02-jul-2024 02-ene-2025 02-jul-2025
-30%
-20%
-10%
0%
10%
20%
30%
40%
50%
60%
70%
02-ene-2022 02-jul-2022 02-ene-2023 02-jul-2023 02-ene-2024 02-jul-2024 02-ene-2025 02-jul-2025
Figure 3: Cryptocurrencies evolution (2022-2025)
7

Synthetic Data in Cryptocurrencies
(a) (b) (c)
-10%
-8%
-6%
-4%
-2%
0%
2%
4%
6%
8%
10%
1-mar-22 8-mar-22 15-mar-22 22-mar-22 29-mar-22 5-abr-22 12-abr-22 19-abr-22 26-abr-22
-10%
-8%
-6%
-4%
-2%
0%
2%
4%
6%
8%
10%
1-mar-22 8-mar-22 15-mar-22 22-mar-22 29-mar-22 5-abr-22 12-abr-22 19-abr-22 26-abr-22
-10%
-8%
-6%
-4%
-2%
0%
2%
4%
6%
8%
10%
1-mar-22 8-mar-22 15-mar-22 22-mar-22 29-mar-22 5-abr-22 12-abr-22 19-abr-22 26-abr-22
-12%
-10%
-8%
-6%
-4%
-2%
0%
2%
4%
6%
8%
10%
01-abr-2022 13-abr-2022 25-abr-2022 07-may-2022 19-may-2022 31-may-2022
-15%
-10%
-5%
0%
5%
10%
01-abr-2022 13-abr-2022 25-abr-2022 07-may-2022 19-may-2022 31-may-2022
-30%
-25%
-20%
-15%
-10%
-5%
0%
5%
10%
15%
01-abr-2022 11-abr-2022 21-abr-2022 01-may-2022 11-may-2022 21-may-2022 31-may-2022
-10%
-8%
-6%
-4%
-2%
0%
2%
4%
6%
8%
10%
01-ago-2025 11-ago-2025 21-ago-2025 31-ago-2025 10-sep-2025 20-sep-2025 30-sep-2025
-10%
-5%
0%
5%
10%
15%
01-ago-2025 11-ago-2025 21-ago-2025 31-ago-2025 10-sep-2025 20-sep-2025 30-sep-2025
-10%
-8%
-6%
-4%
-2%
0%
2%
4%
6%
8%
10%
01-ago-2025 11-ago-2025 21-ago-2025 31-ago-2025 10-sep-2025 20-sep-2025 30-sep-2025
Figure 4: V olatility by periods
characterized by high-frequency oscillations, with daily changes frequently swinging between +8% and -8%. This
represents a risk-off sentiment where investors oscillated between viewing Bitcoin or other cryptocurrencies as an
asset hedge, but at the same time, a speculative high-beta asset. The intraday volatility seen throughout March 2022
indicates several perspectives on cryptocurrency trends, as geopolitical sanctions and energy supply concerns induced
rapid shifts in financial assets’ liquidity. Column (b) represents the most difficult phase of the observed timeline of
the three datasets, coinciding with the change of the US monetary policy and geopolitical issues, which led to the fall
of several assets and the collapse of major algorithmic stablecoin ecosystems. The volatility here is not a result of an
oscillatory process but directional and precipitous. We observe extreme negative outliers, with some assets plunging
beyond -15% and even touching the -30% threshold by mid-May 2022. This period highlights the systemic risk and
structural fragility, exposing underlying structural vulnerabilities in these kinds of financial assets. The charts illustrate
a traditional feedback loop where margin calls and forced liquidations amplified the downward pressure, leading to
a general shift in market confidence. The data for 2025 in column (c) suggests a transition toward a more mature,
albeit still volatile, market structure. While geopolitical tensions remained a persistent factor, the amplitude of the daily
variations narrowed compared to each 2022 period. Most fluctuations were contained within a ±4% range, though
occasional spikes to +10% or -10% persist. The 2025 charts show a market that had priced in a portion of geopolitical
and macroeconomic risk into its pricing model, exhibiting a more "dampened" response to external shocks compared to
the behavior of 2022. However, volatility consistently re-emerges during periods of geopolitical and macroeconomic
uncertainty.
3.3 Method
The defined architecture is a Conditional Generative Adversarial Network (CGAN) with a hybrid LSTM-MLP ar-
chitecture, illustrated by Fig 5a. Processing begins with data loading, conversion from the original format to .csv,
chronological ordering, and normalization of values using the StandardScaler method.
Data normalization was performed using the StandardScaler method, widely used in machine learning tasks for
standardizing numerical variables. This method transforms the data so that they have a mean of zero and a unit variance,
as shown in the following expression (Eq. (6)).
8

Synthetic Data in Cryptocurrencies
x′ = x−µ σ , (6)
where x represents the original value of the observation, µ corresponds to the sample mean of the series, and σ to the
standard deviation. This transformation ensures that the values are centered around the origin and scaled uniformly,
preserving the shape of the original data distribution.
In the context of this research, the StandardScaler was applied exclusively to the cryptocurrency closing variable,
allowing both the generator and the discriminator to operate on normalized data during training. After the generation
process, the inverse transformation was applied to recover the values at the original scale, thereby enabling economic
interpretation of the synthetic results.
The data are structured as pairs, linking values with a conditional label referring to the previous value,
(P ricet−1, P ricet). When training the network, the Generator (LSTM) receives the previous price and noise to
generate the current price (P ricet), and the Discriminator (MLP) classifies the pairs as real or synthetic. The figure
below shows the defined architectural format.
(a) Architecture
Fig. 5a.
We are going to use the following algorithm based on the one proposed by em [38]
9

Synthetic Data in Cryptocurrencies
Algorithm 1Conditional GAN for Time Series Prediction
1: Input:Time series of closing prices, noise dimension l, condition dimension d, batch size k, number of epochs E,
learning rateη, Adam optimizer parameters(β 1, β2).
2:Output:Trained parameters of GeneratorGand DiscriminatorD.
3:Data Loading and Preprocessing:
4:Load closing price time series.
5:Normalize the data usingStandardScaler.
6: Create training pairs (yi, xi), where the condition yi is the normalized price at time t−1 and the real data xi is the
normalized price at timet.
7:Initialization:
8:Set hyperparameters:l= 8,d= 60,k= 64,E= 50,η= 0.0002,β 1 = 0.5,β2 = 0.999.
9:Initialize neural networks:
10:G(y, z): LSTM receiving conditionyand noise vectorz(internally generated) to outputˆx(predicted price att).
11:D(y, x): MLP receiving conditionyand valuex(real or generated) to return classification logits (real vs. fake).
12:Initialize Adam optimizers forGandDwith the defined hyperparameters.
13:Initialize loss function: Binary Cross-Entropy with Logits (BCEWithLogitsLoss).
14:Training Loop:
15:foreach epoche∈ {1, . . . , E}do
16:foreach batch(y, x real)from the datasetdo
17:Train Discriminator:
18:Sample real datax real with corresponding conditionsy.
19:Compute real validity:logits real =D(y, xreal).
20:Compute real loss:L real D =BCEWithLogitsLoss(logits real,1).
21:Generate fake data:ˆx=G(y)(noisezis generated insideG).
22:Compute fake validity (no gradients forG):logits fake =D(y,ˆx.detach()).
23:Compute fake loss:L fake D =BCEWithLogitsLoss(logits fake,0).
24:Compute total discriminator loss:L D = 1 2 (Lreal D +L fake D ).
25:Update discriminator weights:θ D ←Adam(θ D,∇ θD LD).
26:Train Generator:
27:Generate synthetic sequences:ˆx=G(y).
28:Evaluate with Discriminator:logits gen =D(y,ˆx).
29:Compute generator loss (to fool the Discriminator):L G =BCEWithLogitsLoss(logits gen,1).
30:Update generator weights:θ G ←Adam(θ G,∇ θG LG).
31:end for
32:end for
The Binary Cross-Entropy with Logits (BCEWithLogitsLoss) cost function is widely used in binary classification
problems and constitutes a numerically stable formulation of binary cross-entropy combined with the sigmoid function.
Instead of explicitly applying the sigmoid function to the model output and then calculating the cross-entropy, this
function integrates both operations into a single analytical expression, reducing numerical errors associated with extreme
exponential operations.
Formally, considering a scalar output of the discriminator x∈R (logit) and a binary label y∈ {0,1}, the cost function
is defined as (Eq. (7)):
L(x, y) =−

y·log

σ(x)

+ (1−y)·log

1−σ(x)

,(7)
whereσ(·)represents the sigmoid function, defined by the Eq. (8):
σ(x) = 1 1 +e−x . (8)
The computational implementation uses an equivalent reformulation based on thelog-sum-exptechnique, which avoids
numerical saturation when|x|assumes high values [39, 40].
The validation of the generated data is done through the use of performance metrics, such as Pearson’s correlation, in
order to evaluate statistical similarities between the generated and real series, in addition to MAE (Mean Absolute
10

Synthetic Data in Cryptocurrencies
Error) and RMSE (Root Mean Square Error). Complementarily, visual verification through comparisons shown in
graphs allows visualization of whether the model correctly captured the behavior of the data and the dynamics of the
established series.
4 Results and Discussion
The figures presented below demonstrate the results of the Conditional GAN-LSTM model’s behavior when applied to
minute-by-minute closing price data for BTC, ETH, and XRP across the three selected time periods. The total number
of records for each period is shown below, and 50 epochs were used for each training session.
First period (from March 2022 to April 2022): BTC - 22818; ETH - 22820; XRP - 22821.
Second period (from April 2022 to May 2022): BTC - 84428; ETH - 85693; XRP - 85502.
Third period (from September 2025): BTC - 20124; ETH - 20130; XRP - 20129.
The Fig. 6 shows a comparison between the loss values of the generating and discriminating networks for the first,
second, and third periods of BTC values.
0 10 20 30 40 50
Epochs
0.64
0.66
0.68
0.70
0.72
0.74
0.76Loss
Losses during training
G loss
D loss
(a) BTC - data first period.
0 10 20 30 40 50
Epochs
0.685
0.690
0.695
0.700
0.705Loss
Losses during training
G loss
D loss
(b) BTC - data second period.
0 10 20 30 40 50
Epochs
0.62
0.64
0.66
0.68
0.70
0.72
0.74
0.76
0.78Loss
Losses during training
G loss
D loss
(c) BTC - data third period.
Figure 6: Losses during training: BTC.
11

Synthetic Data in Cryptocurrencies
The Fig. 7 shows a comparison between the loss values of the generating and discriminating networks for the first,
second, and third periods of ETH values.
0 10 20 30 40 50
Epochs
0.64
0.66
0.68
0.70
0.72
0.74
0.76
0.78Loss
Losses during training
G loss
D loss
(a) ETH - data first period.
0 10 20 30 40 50
Epochs
0.685
0.690
0.695
0.700
0.705Loss
Losses during training
G loss
D loss
(b) ETH - data second period.
0 10 20 30 40 50
Epochs
0.66
0.68
0.70
0.72
0.74Loss
Losses during training
G loss
D loss
(c) ETH - data third period.
Figure 7: Losses during training: ETH.
The Fig. 8 shows a comparison between the loss values of the generating and discriminating networks for the first,
second, and third periods of XRP values.
12

Synthetic Data in Cryptocurrencies
0 10 20 30 40 50
Epochs
0.66
0.68
0.70
0.72
0.74Loss
Losses during training
G loss
D loss
(a) XRP - data first period.
0 10 20 30 40 50
Epochs
0.685
0.690
0.695
0.700
0.705Loss
Losses during training
G loss
D loss
(b) XRP - data second period.
0 10 20 30 40 50
Epochs
0.62
0.64
0.66
0.68
0.70
0.72
0.74
0.76
0.78Loss
Losses during training
G loss
D loss
(c) XRP - data third period.
Figure 8: Losses during training: XRP.
The Fig. 9 shows the Pearson correlation between the true and generated values for the BTC data. The parameter results
are: first period: Pearson - 0.9999 and Spearman - 0.9997; second period: Pearson - 1.0000 and Spearman - 0.9999;
third period: Pearson - 0.9998 and Spearman - 0.9994. The MAE and RMSE values are: first period: MAE - 29.085452
and RMSE - 38.880509; second period: MAE - 46.711167 and RMSE - 58.489341; third period: MAE - 41.050079
and RMSE - 53.099261.
13

Synthetic Data in Cryptocurrencies
40000 41000 42000 43000 44000 45000 46000 47000 48000
Real_t
40000
41000
42000
43000
44000
45000
46000
47000
48000Generated_t
Dispersion: Real_t vs Generated_t (Pearson Corr=1.00)
Fit line (Pearson=1.00)
(a) BTC - data first period.
 (b) BTC - data second period.
 (c) BTC - data third period.
Figure 9: Dispersion real vs generated - BTC.
The Fig. 10 shows the Pearson correlation between the true and generated values for the ETH data. The parameter
results are: first period: Pearson - 0.9999 and Spearman - 0.9997; second period: Pearson - 1.0000 and Spearman -
0.9999; third period: Pearson - 0.9996 and Spearman - 0.9987. The MAE and RMSE values are: first period: MAE
- 2.897669 and RMSE - 3.839272; second period: MAE - 2.495395 and RMSE - 3.541045; third period: MAE -
2.713196 and RMSE - 3.727772.
(a) ETH - data first period.
 (b) ETH - data second period.
 (c) ETH - data third period.
Figure 10: Dispersion real vs generated - ETH.
The Fig. 11 shows the Pearson correlation between the true and generated values for the XRP data. The parameter
results are: first period: Pearson - 0.9994 and Spearman - 0.9993; second period: Pearson - 1.0000 and Spearman -
0.9999; third period: Pearson - 0.9997 and Spearman - 0.9997. The MAE and RMSE values are: first period: MAE
- 0.000683 and RMSE - 0.001018; second period: MAE - 0.000656 and RMSE - 0.000945; third period: MAE -
0.001976 and RMSE - 0.003112.
(a) XRP - data first period.
 (b) XRP - data second period.
 (c) XRP - data third period.
Figure 11: Dispersion real vs generated - XRP.
The Fig. 12 shows a comparison between the generated and actual values for the first period of BTC values, and a
sample of the first 1000 samples for better visualization.
14

Synthetic Data in Cryptocurrencies
0 5000 10000 15000 20000
Index
40000
41000
42000
43000
44000
45000
46000
47000
48000Price
Comparison: Real vs Generated Values
Real_t
Generated_t
(a) BTC - data first period.
0 200 400 600 800 1000
Index
40600
40800
41000
41200
41400Price
Comparison: Real vs Generated Values (First 1000 Samples)
Real_t
Generated_t
(b) BTC - data first period - first 1000 samples.
Figure 12: Original series vs generated series: BTC - data first period.
The Fig. 13 shows a comparison between the generated and actual values for the second period of BTC values, and a
sample of the first 1000 samples for better visualization.
0 20000 40000 60000 80000
Index
25000
30000
35000
40000
45000Price
Comparison: Real vs Generated Values
Real_t
Generated_t
(a) BTC - data second period.
0 200 400 600 800 1000
Index
46200
46400
46600
46800
47000
47200Price
Comparison: Real vs Generated Values (First 1000 Samples)
Real_t
Generated_t
(b) BTC - data second period - first 1000 samples.
Figure 13: Original series vs generated series: BTC - data second period.
15

Synthetic Data in Cryptocurrencies
The Fig. 14 shows a comparison between the generated and actual values for the third period of BTC values, and a
sample of the first 1000 samples for better visualization.
0 2500 5000 7500 10000 12500 15000 17500 20000
Index
108000
110000
112000
114000
116000Price
Comparison: Real vs Generated Values
Real_t
Generated_t
(a) BTC - data third period.
0 200 400 600 800 1000
Index
107500
108000
108500
109000
109500
110000
110500Price
Comparison: Real vs Generated Values (First 1000 Samples)
Real_t
Generated_t
(b) BTC - data third period - first 1000 samples.
Figure 14: Original series vs generated series: BTC - data third period.
The Fig. 15 shows a comparison between the generated and actual values for the first period of ETH values, and a
sample of the first 1000 samples for better visualization.
16

Synthetic Data in Cryptocurrencies
0 5000 10000 15000 20000
Index
2800
2900
3000
3100
3200
3300
3400
3500Price
Comparison: Real vs Generated Values
Real_t
Generated_t
(a) ETH - data first period.
0 200 400 600 800 1000
Index
2740
2750
2760
2770
2780
2790
2800
2810
2820Price
Comparison: Real vs Generated Values (First 1000 Samples)
Real_t
Generated_t
(b) ETH - data first period - first 1000 samples.
Figure 15: Original series vs generated series: ETH - data first period.
The Fig. 16 shows a comparison between the generated and actual values for the second period of ETH values, and a
sample of the first 1000 samples for better visualization.
0 20000 40000 60000 80000
Index
1750
2000
2250
2500
2750
3000
3250
3500Price
Comparison: Real vs Generated Values
Real_t
Generated_t
(a) ETH - data second period.
0 200 400 600 800 1000
Index
3440
3460
3480
3500
3520Price
Comparison: Real vs Generated Values (First 1000 Samples)
Real_t
Generated_t
(b) ETH - data second period - first 1000 samples.
Figure 16: Original series vs generated series: ETH - data second period.
17

Synthetic Data in Cryptocurrencies
The Fig. 17 shows a comparison between the generated and actual values for the third period of ETH values, and a
sample of the first 1000 samples for better visualization.
0 2500 5000 7500 10000 12500 15000 17500 20000
Index
4300
4400
4500
4600
4700Price
Comparison: Real vs Generated Values
Real_t
Generated_t
(a) ETH - data third period.
0 200 400 600 800 1000
Index
4250
4275
4300
4325
4350
4375
4400
4425Price
Comparison: Real vs Generated Values (First 1000 Samples)
Real_t
Generated_t
(b) ETH - data third period - first 1000 samples.
Figure 17: Original series vs generated series: ETH - data third period.
The Fig. 18 shows a comparison between the generated and actual values for the first period of XRP values, and a
sample of the first 1000 samples for better visualization.
18

Synthetic Data in Cryptocurrencies
0 5000 10000 15000 20000
Index
0.78
0.80
0.82
0.84
0.86
0.88
0.90Price
Comparison: Real vs Generated Values
Real_t
Generated_t
(a) XRP - data first period.
0 200 400 600 800 1000
Index
0.7800
0.7825
0.7850
0.7875
0.7900
0.7925
0.7950
0.7975Price
Comparison: Real vs Generated Values (First 1000 Samples)
Real_t
Generated_t
(b) XRP - data first period - first 1000 samples.
Figure 18: Original series vs generated series: XRP - data first period.
The Fig. 19 shows a comparison between the generated and actual values for the second period of XRP values, and a
sample of the first 1000 samples for better visualization.
0 20000 40000 60000 80000
Index
0.4
0.5
0.6
0.7
0.8Price
Comparison: Real vs Generated Values
Real_t
Generated_t
(a) XRP - data second period.
0 200 400 600 800 1000
Index
0.825
0.830
0.835
0.840
0.845
0.850Price
Comparison: Real vs Generated Values (First 1000 Samples)
Real_t
Generated_t
(b) XRP - data second period - first 1000 samples.
Figure 19: Original series vs generated series: XRP - data second period.
19

Synthetic Data in Cryptocurrencies
The Fig. 20 shows a comparison between the generated and actual values for the third period of XRP values, and a
sample of the first 1000 samples for better visualization.
0 2500 5000 7500 10000 12500 15000 17500 20000
Index
2.7
2.8
2.9
3.0
3.1
3.2Price
Comparison: Real vs Generated Values
Real_t
Generated_t
(a) XRP - data third period.
0 200 400 600 800 1000
Index
2.72
2.74
2.76
2.78
2.80
2.82Price
Comparison: Real vs Generated Values (First 1000 Samples)
Real_t
Generated_t
(b) XRP - data third period - first 1000 samples.
Figure 20: Original series vs generated series: XRP - data third period.
The graphical visualization of the generated data behavior indicates that the developed model captured the closing
pattern of BTC, ETH, and XRP during the testing phase. In the architecture, a range of 60 previous observations
was defined, and normalization was performed using StandardScaler. The synthetic sequences faithfully reproduce
the overall price slope, market oscillations, and point fluctuations of the original data. This shows that the network
assimilated the fundamental conditional dependencies between the closing prices of the analyzed cryptocurrencies.
Regarding the learning phase, the configuration of the Adam optimizer (with parameters β1 = 0.5and β2 = 0.999),
the learning rate fixed at 2×10 −4, and the use of the BCEWithLogitsLoss function were crucial to maintaining the
balance of the adversarial training, preventing critical failures in the generator. Finally, mini-batch processing ensured
the necessary computational efficiency and statistical accuracy in creating the validated synthetic samples.
4.1 Discussion
Although the three cryptocurrencies analyzed exhibit similar general dynamics, the results show that the model’s
effectiveness varies consistently between BTC, ETH, and XRP, reflecting structural and statistical differences inherent
to each time series.
In the case of BTC, synthetic data exhibits high agreement with the trajectory observed in real data, preserving
both medium- and long-term trends as well as transitions between market regimes. This superior performance can be
attributed to the greater liquidity, maturity, and informational efficiency of the BTC market, characteristics that contribute
to time series with less relative noise and more stable patterns. Empirical studies indicate that Bitcoin exhibits greater
statistical predictability when compared to other cryptocurrencies, which favors the learning of temporal dependencies
by recurrent architectures, such as LSTMs, especially when integrated with adversarial models [41, 42, 43].
Regarding ETH, the model is able to adequately capture the general direction of price movement; however, a systematic
attenuation is noted in volatility peaks, with the generated series showing amplitudes lower than those observed in
the real data. This behavior is consistent with results reported in the literature on GANs applied to financial series, in
which the generator tends to smooth extreme events due to the difficulty in reproducing abrupt shocks and distributions
with heavy tails [44, 45]. Furthermore, ETH is strongly influenced by exogenous factors, such as protocol updates,
20

Synthetic Data in Cryptocurrencies
changes in the consensus mechanism, and the evolution of its smart contract ecosystem, which introduces additional
non-stationarity and increases the complexity of the temporal modeling process.
In the case of XRP, the results indicate good local accuracy in certain intervals, although accompanied by greater
sensitivity to short-term noise. This greater variability may be associated with the more speculative nature of the
asset and its dependence on external events, such as regulatory announcements, judicial decisions, and institutional
actions, which are not fully reflected in the price history. Previous studies highlight that crypto assets with lower
market efficiency and high statistical nonlinearity pose additional challenges to the generalization capacity of neural
network-based models, including GANs, making them more susceptible to spurious fluctuations [43, 46].
The choice of the StandardScaler method proves particularly suitable in the context of training GANs applied to financial
time series. In gradient-based architectures, such as GANs and LSTM-type recurrent networks, data standardization
directly contributes to the numerical stability of the optimization process, reducing problems associated with gradient
explosion or disappearance.
Furthermore, standardization by mean and variance preserves the relative relationships between the values of the time
series, an essential aspect for modeling dynamic dependencies over time. Unlike interval scaling methods, such as
Min-Max Scaling, StandardScaler is less sensitive to extreme values, a relevant characteristic in financial series, which
frequently exhibit heavy tails and highly volatile events.
Previous studies demonstrate that the use of standardized data favors the convergence of adversarial training and
improves the generator’s ability to capture complex statistical patterns, especially when combined with recurrent and
conditional architectures [36, 45, 44]. Therefore, the use of StandardScaler contributes to more stable and efficient
learning, being a methodological choice consistent with the specialized literature.
In the context of GANs, the discriminator is modeled as a binary classifier responsible for distinguishing real samples
from those synthesized by the generator. The objective function originally proposed by [ 36] is explicitly based on
maximizing binary cross-entropy, which makes BCE a conceptually aligned choice with the adversarial problem.
The use of BCEWithLogitsLoss, in particular, presents significant advantages over the separate application of the
sigmoid function followed by binary cross-entropy. Firstly, the integration of these operations improves numerical
stability during training, reducing the occurrence of zero or explosive gradients — a recurring problem in GANs,
especially when the discriminator becomes overconfident. This feature ensures that informative gradients continue to
be propagated to the generator through the backpropagation process, preserving the dynamics of the minimax game
[36, 47].
Furthermore, by operating directly on the logits, BCEWithLogitsLoss allows the discriminator to maintain a richer
representation of the uncertainty associated with its predictions, which contributes to more balanced training. Empirical
studies, such as the work of [47] in the context of DCGAN, demonstrate that this formulation favors stable convergence
and reduces the probability of mode collapse, especially when combined with appropriate adjustments of the optimizer
and the learning rate.
In applications involving financial time series, characterized by high volatility and non-stationarity, the numerical
robustness of BCEWithLogitsLoss becomes even more relevant. The function allows the discriminator to respond
continuously to small statistical variations in the data, providing more consistent error signals to the generator during
adversarial training, as discussed in modern GAN approaches for time series [48, 45].
5 Conclusion
Our analysis demonstrates that a CGAN, equipped with an LSTM generator and a time window of 60 observations,
effectively replicates the price dynamics of various cryptocurrencies, namely is capable of producing synthetic series.
The model performed best on mature, liquid assets like Bitcoin (BTC), where temporal patterns are relatively stable.
Conversely, performance dipped when modeling more volatile assets such as Ethereum and XRP. These assets’ high
structural volatility and susceptibility to exogenous factors highlight the ongoing challenge of modeling non-stationary
financial series.
The results obtained reinforce the relevance of fundamental methodological choices, such as the appropriate definition
of the time window, the adoption of appropriate normalization techniques, and the careful balancing of adversarial
training, to ensure stability and convergence in GAN applications to financial time series. Additionally, the analysis
highlights that behavioral and statistical differences between assets directly influence the model’s ability to generalize,
indicating that adaptive or asset-specific approaches may represent a promising path for future work.
21

Synthetic Data in Cryptocurrencies
Acknowledgments
This work has been partially supported by QuIIN - EMBRAPII CIMATEC Competence Center in Quantum Technologies,
with financial resources from the PPI IoT/Manufatura 4.0 / PPI HardwareBR of the MCTI grant number 053/2023, signed
with EMBRAPII. The authors would like to thank the Supercomputing Center for Industrial Innovation (CS2I), the
Reference Center for Artificial Intelligence (CRIA), and the Latin American Quantum Computing Center (LAQCC), all
from SENAI CIMATEC, for providing all the technical and infrastructure support. We also thank the National Council
for Scientific and Technological Development (CNPq, Brazil) for partially funding this work. Oscar M. Granados
received funds for Universidad Jorge Tadeo Lozano (Grant 13456 for the Center on Intelligence and Innovation).
References
[1] T. Raghunathan, J. Reiter, and D. Rubin. Multiple imputation for statistical disclosure limitation.AI, 19, 2003.
[2] A. Radford, L. Metz, and S. Chintala. Journal of official statistics.arXiv:1511.06434, 2015.
[3] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y . Bengio.
Generative adversarial nets.Advances In Neural Information Processing Systems, 3:2672–2680, 2014.
[4] Feng Han, Xiaojuan Ma, and Jiheng Zhang. Simulating multi-asset classes prices using wasserstein generative
adversarial network: A study of stocks, futures and cryptocurrency.Journal of Risk and Financial Management,
15(1), 2022.
[5] A. A. Almamoori and W. S. Bhaya. Hybrid deep learning approach utilizing rnn and lstm for the detection of
ddos attacks within the bitcoin ecosystem.Ingénierie des Systèmes d’Information, 28(4):931–937, 2023.
[6] Yousef K. Sanjalawe and Salam R. Al-E’mari. Abnormal transactions detection in the ethereum network using
semi-supervised generative adversarial networks.IEEE Access, 11:98516–98531, 2023.
[7] J. Y . Zhu, P. Krähenbühl, E. Shechtman, and A. A. Efros. Generative visual manipulation on the natural image
manifold.In European Conference on Computer Vision, pages 597–613, 2016.
[8] N. Killoran, L. J. Lee, D. A. Delong, and B. J. Frey Duvenaud. Generating and designing dna with deep generative
models.arXiv:1712.06148, 2017.
[9] A. Kadurin, S. Nikolenko, K. Khrabrov, A. Aliper, and A. Zhavoronkov. Generating and designing dna with deep
generative models.Molecular pharmaceutics, 14(3098), 2017.
[10] Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen. Improved
techniques for training gans, 2016.
[11] Aleksandar Bojchevski, Oleksandr Shchur, Daniel Zügner, and Stephan Günnemann. NetGAN: Generating graphs
via random walks. In Jennifer Dy and Andreas Krause, editors,Proceedings of the 35th International Conference
on Machine Learning, volume 80 ofProceedings of Machine Learning Research, pages 610–619. PMLR, 10–15
Jul 2018.
[12] Tuan A Ngo, Tuyen Nguyen, and Truong Cong Thang. A survey of recent advances in quantum generative
adversarial networks.Electronics, 12(4):856, 2023.
[13] Ankan Dash, Junyi Ye, and Guiling Wang. A review of generative adversarial networks (gans) and its applications
in a wide variety of disciplines: From medical to remote sensing.IEEE Access, 12:18330–18357, 2024.
[14] Shuntaro Takahashi, Yu Chen, and Kumiko Tanaka-Ishii. Modeling financial time-series with generative adversarial
networks.Physica A: Statistical Mechanics and its Applications, 527:121261, 2019.
[15] Yusuke Naritomi and Takanori Adachi. Data augmentation of high frequency financial data using generative
adversarial network. page 641 – 648, 2020.
[16] Fan Zhang, Luyao Wang, and Xinhong Zhang. Desensitized financial data generation based on generative
adversarial network and differential privacy.Big Data Mining and Analytics, 8(1):103 – 117, 2025.
[17] Xingyu Zhou, Zhisong Pan, Guyu Hu, Siqi Tang, and Cheng Zhao. Stock market prediction on high-frequency
data using generative adversarial nets.Mathematical Problems in Engineering, 2018(1):4907423, 2018.
[18] Kang Zhang, Guoqiang Zhong, Junyu Dong, Shengke Wang, and Yong Wang. Stock market prediction based on
generative adversarial network.Procedia computer science, 147:400–406, 2019.
[19] Junyi Li, Xintong Wang, Yaoyang Lin, Arunesh Sinha, and Michael Wellman. Generating realistic stock market
order streams. InProceedings of the AAAI Conference on Artificial Intelligence, volume 34, pages 727–734, 2020.
22

Synthetic Data in Cryptocurrencies
[20] Milena Vuleti´c, Felix Prenzel, and Mihai Cucuringu. Fin-gan: forecasting and classifying financial time series via
generative adversarial networks.Quantitative Finance, 24(2):175–199, 2024.
[21] Yanzhe Kang, Liao Chen, Ning Jia, Wei Wei, Jiang Deng, and Haizhang Qian. A cwgan-gp-based multi-task
learning model for consumer credit scoring.Expert Systems with Applications, 206:117650, 2022.
[22] Teema Leangarun, Poj Tangamchit, and Suttipong Thajchayapong. Stock price manipulation detection using
generative adversarial networks. In2018 IEEE symposium series on computational intelligence (SSCI), pages
2104–2111. IEEE, 2018.
[23] Ugo Fiore, Alfredo De Santis, Francesca Perla, Paolo Zanetti, and Francesco Palmieri. Using generative
adversarial networks for improving classification effectiveness in credit card fraud detection.Information Sciences,
479:448–455, 2019.
[24] Seyyede Zahra Aftabi, Ali Ahmadi, and Saeed Farzi. Fraud detection in financial statements using data mining
and gan models.Expert Systems with Applications, 227:120144, 2023.
[25] O. Granados, O. García-Bedoya, and E. González. Gan+abm to simulate suspicious money laundering trajectories.
IEEE International Conference On Data Mining Workshops (ICDMW), pages 262–269, 2024.
[26] Y . Yang, F. Nan, P. Yang, Q. Meng, Y . Xie, D. Zhang, and K. Muhammad. Gan-based semi-supervised learning
approach for clinical decision support in health-iot platform.IEEE Access, 7(6):8048–8057, 2019.
[27] B. Beaulieu-Jones, Z. Wu, C. Williams, R. Lee, S. Bhavnani, J. Byrd, and C. Greene. Privacy-preserving generative
deep neural networks support clinical data sharing.Circulation: Cardiovascular Quality And Outcomes, 7(12),
2019.
[28] V . Sandfort, K. Yan, P. Pickhardt, and R. Summers. Data augmentation using generative adversarial networks
(cyclegan) to improve generalizability in ct segmentation tasks.Scientific Reports, (11), 2019.
[29] J. Yoon, J. Jordon, and M. Schaar. Gan-based semi-supervised learning approach for clinical decision support in
health-iot platform.International Conference on Learning Representations, 2019.
[30] Rogério Ferreira.Deep learning. SRV Editora LTDA, 2021. E-book.
[31] Stuart Russell and Peter Norvig.Inteligência Artificial. LTC, Rio de Janeiro, 3 edition, 2021.
[32] Aurélien Géron.Mãos à Obra: Aprendizado de Máquina com Scikit-Learn, Keras & TensorFlow — Conceitos,
Ferramentas e Técnicas para a Construção de Sistemas Inteligentes. Alta Books, Rio de Janeiro, 2021. E-book.
[33] J. Langr and V . Bok.GANs in Action: Deep Learning with Generative Adversarial Networks. Manning
Publications, 2019.
[34] I. Goodfellow, Y . Bengio, and A. Courville.Deep Learning. MIT Press, 2016.
[35] Zhaoqing Pan, Weijie Yu, Xiaokai Yi, Asifullah Khan, Feng Yuan, and Yuhui Zheng. Recent progress on generative
adversarial networks (gans): A survey.IEEE Access, 7:36322–36333, 2019.
[36] Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron
Courville, and Yoshua Bengio. Generative adversarial nets. InProceedings of the 28th International Conference
on Neural Information Processing Systems - Volume 2, NIPS’14, page 2672–2680, Cambridge, MA, USA, 2014.
MIT Press.
[37] Aston Zhang, Zachary C. Lipton, Mu Li, and Alexander J. Smola.Dive into Deep Learning. Cambridge University
Press, 2023.
[38] Lokesh Saravana, Quang-Ha Ngo, Jianhua Zhang, Tuyen Vu, and Thanh Long Vu b. Integrated attentive bi-lstm
conditional gan for power system oscillation localization.Electric Power Systems Research, 242, May 2025.
[39] Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization.International Conference on
Learning Representations, 2015.
[40] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen,
Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Köpf, Edward Yang, Zachary DeVito,
Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai, and Soumith Chintala.
Pytorch: An imperative style, high-performance deep learning library.Advances in Neural Information Processing
Systems, 32, 2019.
[41] Andrew Urquhart. The inefficiency of bitcoin.Economics Letters, 148:80–82, 2016.
[42] Paraskevi Katsiampa. V olatility estimation for bitcoin: A comparison of garch models.Economics Letters,
158:3–6, 2017.
23

Synthetic Data in Cryptocurrencies
[43] Salim Lahmiri and Stelios Bekiros. Cryptocurrency forecasting with deep learning chaotic neural networks.Chaos,
Solitons & Fractals, 118:35–40, 2019.
[44] Magnus Wiese, Robert Knobloch, Ralf Korn, and Peter Kretschmer. Quant gans: Deep generation of financial
time series.Quantitative Finance, 20(9):1419–1440, 2020.
[45] Jinsung Yoon, Daniel Jarrett, and Mihaela van der Schaar. Time-series generative adversarial networks.Advances
in Neural Information Processing Systems, 32:5508–5518, 2019.
[46] Yuchen Zhang et al. Forecasting cryptocurrency prices using deep learning.Finance Research Letters, 41:101798,
2021.
[47] Alec Radford, Luke Metz, and Soumith Chintala. Unsupervised representation learning with deep convolutional
generative adversarial networks.International Conference on Learning Representations, 2016.
[48] Cristóbal Esteban, Stephanie L. Hyland, and Gunnar Rätsch. Real-valued (medical) time series generation with
recurrent conditional gans.arXiv preprint arXiv:1706.02633, 2017.
24
