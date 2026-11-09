---
title: High-Quality Synthetic Financial Time-Series using a GAN-Diffusion Framework
url: https://arxiv.org/abs/2605.27113
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Giuseppe Masi
- Andrea Coletta
- Novella Bartolini
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.27113
pages: 23
chars: 75464
fetched_at: '2026-11-08T13:07:55+00:00'
kb_version: 1
---

# High-Quality Synthetic Financial Time-Series using a GAN-Diffusion Framework

High-Quality Synthetic Financial Time-Series using a
GAN–Diffusion Framework
GIUSEPPE MASI,Sapienza University of Rome, Italy
ANDREA COLETTA∗,Banca d’Italia, Italy
NOVELLA BARTOLINI,Sapienza University of Rome, Italy
In recent years, financial institutions and firms have increasingly adopted synthetic data to address data scarcity
and to generate counterfactual market scenarios. However, reproducing all the statistical properties of financial
time series, commonly known as stylized facts, remains an open challenge for many existing general-purpose
architectures. In this paper, we present a quality-aware generative framework that combines two classes of
generative methods, demonstrating how their integration addresses existing limitations while enhancing the
realism of synthetic data. Specifically, we first introduce CoMeTS-GAN (CorrelatedMultivariate TimeSeries
GAN), a Conditional Generative Adversarial Network (C-GAN) designed to jointly generate mid-price and
volume time-series for correlated stocks. We then show how our GAN architecture can be incorporated
into state-of-the-art diffusion models to enhance the quality of generated correlation structures. Specifically,
the GAN’s Critic serves as a quality evaluation module that guides the diffusion process, enforcing learned
correlation structures in the generated time-series. Our framework offers a lightweight and responsive solution
for realistic stock market simulation, explicitly modeling inter-asset correlation structures. We experimentally
validate our framework against leading generative architectures, showing that it more effectively captures the
stylized facts of stock markets and models inter-asset correlations.
CCS Concepts:•Computing methodologies → Machine learning algorithms;•Mathematics of com-
puting→ Time series analysis;•Theory of computation → Adversarial learning;•Applied computing →
Economics.
Additional Key Words and Phrases: Diffusion models, GANs, synthetic data, time-series, financial data
ACM Reference Format:
Giuseppe Masi, Andrea Coletta, and Novella Bartolini. 2018. High-Quality Synthetic Financial Time-Series
using a GAN–Diffusion Framework.ACM J. Data Inform. Quality37, 4, Article 111 (August 2018), 23 pages.
https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
The recent advancements in Artificial Intelligence (AI) have had a substantial impact on the financial
industry [7, 36], enabling novel algorithms for stock market prediction [40], risk assessment and
management tools [29], portfolio hedging solutions [6], or automated credit scoring systems [34].
The effectiveness of AI in the financial domain is — in part — due to the fact that financial firms are
early adopters of novel technologies, but it has also been largely driven by the huge amount of
historical and high-frequency data. In fact, financial markets are inherently data-driven and require
∗The opinions expressed in this paper are personal and should not be attributed to Banca d’Italia.
Authors’ Contact Information: Giuseppe Masi, masi.g@di.uniroma1.it, Sapienza University of Rome, Italy; Andrea Coletta,
andrea.coletta@bancaditalia.it, Banca d’Italia, Italy; Novella Bartolini, novella@di.uniroma1.it, Sapienza University of Rome,
Italy.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the
full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
©2018 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM 1936-1963/2018/8-ART111
https://doi.org/XXXXXXX.XXXXXXX
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.
arXiv:2605.27113v1  [cs.LG]  26 May 2026

111:2 Masi et al.
precise, data-driven decision-making. Such an environment seems a natural fit for machine learning
models since they could exploit large datasets to extract patterns, model complex dynamics, and
improve predictive accuracy.
However, the huge amount of data generated within financial systems does not always translate
into available datasets for machine learning algorithms, especially for the academic community. This
is primarily due to strict regulations — which limit data sharing and usage — as well as the high costs
associated with high-frequency data sources. For example, while daily stock price data is generally
accessible, more detailed data — such as limit order book data — is often proprietary and not publicly
available. Additionally, rare and extreme market events are, by definition, underrepresented in
historical data, posing novel challenges for training robust models or conducting thorough back-
testing.
Synthetic data.Synthetic data offers a promising solution to these challenges by providing data
with the same characteristics and structure as real data, while avoiding the associated risks and
constraints [22, 39]. Synthetic data tools enable the generation oftheoreticallyunlimited amounts of
free data; they support the creation of counterfactual scenarios for testing and what-if analyses; and
they allow data sharing without compromising privacy or exposing sensitive information. In recent
years, a number of approaches have been designed to generate synthetic data for fundamental
financial applications. Some notable examples include market simulations [9], model calibration [13],
portfolio construction [28, 38], design of hedging strategies [12], or counterfactual markets scenarios
generation [8]. In all these settings, developing data-generation techniques that accurately capture
the complexities of global financial markets — thus produce high-quality synthetic data — is essential
to the effectiveness of downstream tasks. Financial data have specific statistical properties, often
referred to as stylized facts [10], that characterize stock returns, volatility, orders, and all financial
data. However, reproducing such properties is not a trivial task. While recent work addresses
the specific task of realistic financial time-series generation [45], by conditioning the generative
model to preserve the stylized facts, many statistical properties have remained overlooked, and
quality-aware frameworks are still missing. In particular, the correlation structure among multiple
assets is often neglected, with only a few approaches addressing this issue [30], thereby limiting
the realism and applicability of the generated data in multivariate settings.
The need for realistic correlated time-series.Correlation dynamics are among the most impor-
tant statistical properties in the generated time-series. In the financial domain, correlation dynamics
play an essential role in managing the risks within a portfolio by ensuring that the individual assets
are not overly correlated with one another and impacted by similar market conditions [37]. There
are several reasons why stocks may exhibit correlation. Correlation may be sector-specific: for
instance, the technology sector is affected by industry-wide regulations and changes in customer
demands for a given product. Macroeconomic factors like interest rates or inflation may also impact
entire sectors, causing the underlying stocks to react similarly. Furthermore, exogenous news and
events can impact stocks belonging to different economic fields. We underline that even stocks
that do not have fundamental similarities may show relevant correlation, possibly due to investor
sentiment [4, 19]. During periods of market uncertainty or volatility, investors tend to adopt a
risk-aware approach, affecting multiple stocks simultaneously. Finally, another source of correlation
comes from composite financial instruments such as Exchange-Traded Funds (ETFs). Since these
involve a basket of stocks, correlation among otherwise unrelated assets could arise as they align
with the funds’ overall performance [24].
To conclude, the existence of the described correlation dynamics cannot be neglected when
designing AI tools for the generation of synthetic datasets to simulate financial markets. However,
most of the existing approaches attempt to learn stock correlation by solely relying on specific deep
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:3
Time-series
Dataset
CoMeTS-GAN
C
Generator
Critic
G
or
Synthetic
data
Diﬀusion Model
… …
guidance
Using the Critic to improve
correlation realism
Fig. 1. Overview of the CoMeTS-GAN framework. The system employs a conditional GAN consisting of a
Generator (G) and a Critic (C). The Critic not only evaluates realism to properly train the Generator but also
can guide a Diffusion Model during sample generation to improve the overall time-series quality.
learning model architectures (e.g., a transformer layer designed to learn feature dependency [46]).
Yet, our experiments demonstrate that the resulting time-series do not always preserve the existing
correlations.
A novel quality-aware framework for correlated time-series generation.In this paper, we
present a quality-aware generative framework that consists of a Generative Adversarial Network
(GAN) [17] and a Diffusion Model [43].
Specifically, we first introduce CoMeTS-GAN (CorrelatedMultivariate TimeSeriesGAN) for
the synthetic generation of realistic market data (i.e., prices and volumes) that explicitly aims at
providing a responsive market environment whilst capturing the inherent correlation among assets.
Such approach builds on the GAN architecture [17], which has been widely adopted for financial
scenarios [11, 44, 47, 50], as well as in general-purpose time-series generation [ 21, 25, 41]. Our
proposed GAN architecture offers lightweight training and rapid generation, while also leveraging
the two-player setup — aGeneratorand aCritic— to introduce domain-specific constraints. In
particular, we incorporate cross-asset correlation coefficients directly into the Critic model, enabling
the GAN to learn and reproduce realistic correlation dynamics.
Eventually, we show that our Critic can be repurposed as an evaluation module — considering
its capability of assessing the realism of correlation dynamics in the generated time series — and
we demonstrate how it can be seamlessly integrated into a Diffusion-based Model for time-series
generation to guide the sampling process at inference time. We show that such an integrated
approach provides a quality-aware generation pipeline that enforces realistic correlation structures.
Figure 1 shows the overall proposed framework.
Paper Contributions.In detail, the major contributions of this paper are the following:
•A Quality-Aware generative framework consisting of a Conditional Generative Adversarial
Network (CGAN) and a Diffusion Model for multivariate time-series generation, comprising
both price and volume dynamics across multiple correlated assets.
• A Conditional GAN architecture that uses a novelcross-correlation distanceto quantify the
realism of correlation dynamics in generated time-series. A lightweight GAN architecture that
enables fast training and generation, allowing for the synthesis of arbitrarily long time-series
and responsive market simulation.
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:4 Masi et al.
• ACritic-Guidedgeneration strategy for diffusion models, in which the GAN’s Critic module
dynamically steers the denoising process — generation process — of (any) pre-trained diffusion
models at inference time, enhancing cross-correlation dynamics in the generated time-series.
• A thorough experimental campaign that points out the realism of our approaches, capturing
all the known stylized facts and the correlation dynamics. A comparison with existing
approaches reveals that our solution outperforms existing work in its ability to capture
inter-asset correlation, producing longer time-series, with moderate training effort.
• A simulation of counterfactual scenarios, enabling the generation of diversewhat-iffinancial
time-series under hypothetical shifts in correlation dynamics. We also evaluate the model’s
responsiveness to the behavior of experimental agents.
2 Related Work
In this section, we review existing generative models, and related work, aimed at generating time-
series data, with a particular focus on methods developed for financial and stock price datasets.
Time series generation.Early generative models for time-series focused on domains outside
finance. C-RNN-GAN [33] utilized LSTM networks in both the generator and discriminator to
produce sequences of classical music, while RCGAN [16] adapted a similar framework for medical
time-series, introducing a conditioning mechanism distinct from simple auto-regression. These
models rely mainly on binary adversarial feedback, which may be insufficient to capture complex
temporal dependencies prevalent in financial data.
A notable advancement was proposed by Yoon et al. [51] with TimeGAN, a novel framework
combining adversarial objectives with stepwise supervised losses. TimeGAN employs four compo-
nents (embedding function, recovery function, sequence generator, and sequence discriminator),
demonstrating superior performance in terms of discriminative and predictive metrics on bench-
mark datasets. However, despite its merits, TimeGAN generates only fixed-length mini-sequences
and is associated with high training costs, both of which are problematic for financial applications
that require efficient generation of arbitrarily long sequences.
Other recent contributions have further advanced the field. GT-GAN [21] introduced a general-
purpose framework for time-series synthesis based on GANs, designed to handle a diverse range of
sequential data by explicitly modeling temporal patterns and dependencies across various domains.
COSCI-GAN [41] proposed a novel approach for generating multivariate time-series by coordinating
the latent sources underlying different variables, thereby enabling the synthesis of multivariate
sequences with common-source dependencies. While these models expand generative capabilities
beyond single-variate and fixed-length sequences, they have yet to address the specific challenges
of creating realistic, arbitrarily long financial time-series with dynamic interdependencies among
multiple assets.
Diffusion models for Time-Series generation.Recently, a new class of generative models, namely
diffusion models, has been adopted for time-series generation. Diffusion models were originally
introduced in [42] and gained widespread popularity through the Denoising Diffusion Probabilistic
Models (DDPM) proposed in [20]. They have demonstrated superior performance in sample quality
and diversity across modalities [ 14], and recent work has begun extending their applicability
to structured domains such as time-series and dynamical data [ 27]. Notable examples include
DiffTime [8], Diffusion-TS [52], and TSGM [26] for the generation of time-series data.
Financial-specific generative models.The aforementioned work mainly focuses on general-purpose
generative models, which only partially adapt to the specific requirements of financial time-series
generation. In fact, existing models often fail to capture all the stylized facts and statistical properties
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:5
of financial data. Consequently, recent literature has introduced ad-hoc models specifically tailored
to financial data.
Takahashi et al.[44] proposed FIN-GAN, adopting classic GANs with a variety of generator/dis-
criminator structures (multi-layer perceptrons, convolutional neural networks, and hybrids) to re-
produce stylized facts observed in actual market time-series. Wiese et al.[50] developed QuantGAN,
integrating temporal convolutional networks (TCNs) to effectively model long-range dependencies
such as volatility clustering. Li et al. [25] explored transformer-based models for adversarial gener-
ation of time series, leveraging self-attention to improve sequence modeling. Nonetheless, none of
these methods provides a scalable solution for generating multi-stock series that capture evolving
interactions and dependencies among different assets.
Broadening the view, some works focused on the generation of specific aspects. Vuletić et al. [48]
exploit a GAN architecture trained with an economic-driven loss function for the generator to
generate the ETF-excess returns with respect to the underlying stocks to place trades and make
profits. Cont et al. [11] proposed an approach based on GANs to generate price traces that retain
tail risk features observed in the input dataset, to improve the estimation of loss distributions in
dynamic portfolios. However, these approaches do not consider the simultaneous generation of
multiple stocks and their correlation dynamics.
Masi et al. [ 30] is the first work that explicitly addresses the generation of correlated stock
prices, using a conditional GAN architecture. However, in their framework, volumes and prices
are generated independently, which is suboptimal, and the intraday structure of trading activity
is largely overlooked. Our quality-aware generation framework builds upon and extends this
prior work in several aspects. First, we introduce novel temporal features to better capture intra-
day stock dynamics (e.g., the characteristic U-shaped volume profile [ 5]). We extend the GAN
framework to jointly generate trading volumes and prices, thereby enhancing realism by capturing
the strong dependence between volume dynamics and price volatility. Our analysis of stylized facts
is accordingly expanded to encompass empirical regularities in both volume and price series. Finally,
we went beyond a single model by also introducing diffusion models: we show that our trained
Critic can be integrated into any existing diffusion model to guide the generation of time-series
towards more realistic inter-asset correlations. Within this new framework, we also demonstrate
the possibility of counterfactual generation, assessing the model’s ability to simulate previously
unseen market scenarios - for instance, exploring a hypothetical shift in the correlation between
Coca-Cola and Pepsi stock returns from positive to negative.
3 Background
In this section, we briefly review some important pillars that are useful for the reader to approach
this paper.
3.1 Conditional GANs
Generative Adversarial Networks (GANs) [17] are a subclass of generative models based on game
theory. GANs have two neural networks: a generator denoted as𝐺, and a discriminator denoted
as𝐷. The generator creates synthetic data samples from random noise, while the discriminator
distinguishes between real and generated samples. During training, the generator competes against
the discriminator to improve its ability to generate synthetic data samples𝒙∼𝑝 gen that are realistic,
i.e., distributed as the original data distribution𝑝 real.
The generator’s output is 𝒙=𝐺(𝒛 ; 𝜽(𝐺)) where 𝒛∼N( 0,𝑰) is an input noise to ensure variance
at generation time, and 𝜽(𝐺) the parameters of the generator. The discriminator outputs 𝑦=
𝐷(𝒙 ; 𝜽(𝐷))∈[ 0, 1] representing the probability of𝒙 being drawn from𝑝real and 𝜽(𝐷) the parameters
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:6 Masi et al.
of the discriminator. Both𝐺 and𝐷 are trained to optimize their payoff until neither player can
unilaterally improve its cost. The discriminator is trained to maximize the probability of assigning
the correct label to the data, eitherrealorgenerated; conversely, the generator is trained to minimize
it (by generating realistic samples that the discriminator misclassifies as real).
GANs can also be extended to consider conditional input, resulting in what is known as
conditional-GANs [31]. In conditional-GANs, or CGANs, both the generator and discriminator
networks may take additional conditioning information 𝒄 as input, such as class labels or other
contextual features. This allows for generating specific types of data samples based on the provided
conditioning information. The generator’s and discriminator’s input vectors are combined with 𝒄.
In this work, we use a Wasserstein Generative Adversarial Network (WGAN) [2], which demon-
strated better training performance and stability. In a WGAN the discriminator is called critic and
outputs a realness score of the input samples,𝑦=𝐷(𝒙 ; 𝜽(𝐷))∈R , even calledcritic score. Formally,
the optimal generator is𝐺∗:
arg min
𝐺
max
𝐷 E 𝒙∼𝑝 data [𝐷(𝒙|𝒄)]− E 𝒛∼N(0,𝑰) [𝐷(𝐺(𝒛|𝒄))].(1)
3.2 Diffusion Model
Diffusion models generate data by learning to invert a Markovian noising process that maps data
to a tractable prior, such as a standard Gaussian.
Let 𝒙∼𝑝 real be a real sample. Theforward diffusion processprogressively corrupts 𝒙0 into a
sequence of latent variables(𝒙1,...,𝒙 𝑇) using a Markov chain:𝑞(𝒙 1:𝑇|𝒙0)= ˛𝑇 𝑡=1𝑞(𝒙𝑡|𝒙𝑡−1). Each
transition is typically defined as additive Gaussian noise: 𝑞(𝒙𝑡|𝒙𝑡−1)=N

𝒙𝑡;
√︁
1−𝛽 𝑡 𝒙𝑡−1,𝛽𝑡 𝑰

,
with a time-dependent noise schedule{𝛽𝑡}𝑇 𝑡=1. After𝑇 steps, 𝒙𝑇 becomes approximately standard
Gaussian, i.e.,𝑞(𝒙 𝑇)≈N(0,𝑰)for large𝑇.
Thereverse processaims to reconstruct data from noise by learning the reverse conditional
distributions:𝑝𝜙(𝒙0:𝑇)=𝑝(𝒙 𝑇) ˛𝑇 𝑡=1𝑝𝜙(𝒙𝑡−1|𝒙𝑡), where𝑝(𝒙𝑇)=N( 0,𝑰) and each𝑝𝜙(𝒙𝑡−1|𝒙𝑡) is
typically parameterized as𝑝𝜙(𝒙𝑡−1|𝒙𝑡)=N 𝒙𝑡−1 ;𝝁𝜙(𝒙𝑡,𝑡),𝚺 𝜙(𝒙𝑡,𝑡) , with the mean and covari-
ance learned via a neural network𝜖𝜙.
In practice, this neural network is trained by maximizing a variational lower bound on the
marginal log-likelihood log𝑝𝜙(𝒙0), yielding a loss that includes a (reweighted) denoising score-
matching term [20]:
E𝑡,𝒙 0,𝜖
h𝜖−𝜖 𝜙(𝒙𝑡,𝑡) 2i ,
where𝜖∼N(0,𝑰)and𝒙 𝑡 =√ ¯𝛼𝑡 𝒙0+√1− ¯𝛼𝑡𝜖, with ¯𝛼𝑡 = ˛𝑡 𝑠=1(1−𝛽 𝑠).
Sampling proceeds by initializing 𝒙𝑇∼N( 0,𝑰) and sequentially applying the learned reverse
transitions𝑝 𝜙(𝒙𝑡−1|𝒙𝑡)for𝑡=𝑇,...,1, reconstructing data via iterative denoising.
3.3 Stylized Facts
The variation of asset price exhibits several statistical properties that are common across a wide
range of markets and timeframes. These properties capture the market behavior over different
time periods and are referred to asstylized facts[ 10, 49]. In this work, we use them to evaluate the
quality of samples generated by the model. In particular, we consider the following stylized facts:
• Fat-tailed distributionorheavy tails. The distribution of the asset returns displays a
power-law or Pareto-like tail, meaning that extreme returns occur more frequently than
predicted by a normal distribution.
• Aggregational normality. As the time period for computing returns ( Δ𝑡) increases, the
distribution of returns resembles a normal distribution.
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:7
• Linear unpredictabilityorabsence of autocorrelation. The linear autocorrelation of the
return corr(𝑟𝑡,𝑇,𝑟𝑡+Δ𝑡,𝑇) rapidly decays to zero within minutes and becomes insignificant for
periods longer thanΔ𝑡=20minutes, with𝑇the length of the series [49].
• Volatility clustering. Large changes in prices tend to cluster together, that is, volatility
shows a positive autocorrelation over several trading days.
•Volume/Volatility Correlation. Trading volume and volatility are positively correlated.
Specifically, these properties allow us to assess the preservation of the realism of generated traces.
3.4 Correlation Dynamics
Interdependency and correlation dynamics need new analytical tools to analyze the set of stocks in
relation to each other. We recall the importance of correlation dynamics in portfolio management,
the use of correlation as a measure to evaluate portfolio diversification is a common practice.
The principal aim is to mitigate the total risk by strategically including assets that exhibit a low
correlation with each other. To achieve this, it is imperative to maintain a realistic understanding
of the correlation dynamics among stocks.
In order to evaluate the effectiveness of the model in capturing these dynamics, we suggest the
following quantitative metric, thecross-correlation distance:
Cross-correlation distance.This metric measures the distance between the cross-correlations
of real and generated stocks. Formally, let𝜌(·,·) be thePearson correlation coefficient(PCC). For a
pair of stocks(𝑆 𝑖,𝑆𝑗), we can measure:
𝑑𝜌(𝑆𝑖,𝑆𝑗)=MSE(𝜌(𝑆 𝑖,𝑆𝑗),(𝜌( b𝑆𝑖, b𝑆𝑗)),
where b𝑆𝑖 and b𝑆𝑗 are the synthetic version of the stocks𝑆𝑖 and𝑆𝑗 and MSE being the mean squared
error.
We will utilize this metric to scrutinize the model’s performance with respect to stocks that
show varying degrees of correlation. For instance, let us consider two prominent companies, Coca-
Cola and PepsiCo, which generally demonstrate a strong positive correlation. This correlation is
attributable to their simultaneous presence in the same market, competing for similar consumer
demographics, and facing exposure to similar exogenous factors (i.e., suppliers). On the other hand,
during times of market turmoil, investors often seek out defensive stocks as opposed to riskier,
growth-oriented stocks. This pattern of trading behavior may result in a shift to Coca-Cola, a
beverage firm, from a technology company, for instance, Nvidia, leading to a negative correlation
between these two stocks.
Understanding these correlation patterns is not just academically interesting, it is critical for
managing risk and unlocking profit opportunities.
4 System Model
The purpose of our framework is to generate multivariate time-series capturing crucial aspects of
the stock markets for multiple stocks simultaneously, which include mid-prices and volumes. A key
focus of our approach is to ensure the preservation of the correlation between the considered stocks.
The framework’s underlying model is trained to maximize both the similarity and the match in
the correlation of the generated time-series to real ones. This architecture can be used to generate
time-series also of other domains. Nonetheless, we will mostly stress its strengths in the financial
field; more specifically, we are interested in mid-prices and volumes of a chosen set of stock. In the
following, we analyze in detail the main components of the framework.
Output.The output of our framework is a multivariate time-series of length 𝐹 units of time,
two series (price and volume) for each stock in the set S. This output is structured as a matrix
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:8 Masi et al.
ˆ𝒙future∈R 𝐹×2𝑛 , with𝑛=|S| (i.e., the number of stocks). To generate longer time-series, an auto-
regressive approach can be used, that is, iteratively feeding the conditional generator with its own
output. More details on the auto-regressive generation are provided in the following paragraphs.
Training Data.The dataset used to train the model is generated from historical stock traces in
the temporal period[0,𝑇] . Let 𝒙𝑠∈R 2×𝑇 be the time-series representing the mid-price and the
volume of stock𝑠∈S in the considered temporal period. For the given set of stocks, we stack
the individual time-series 𝒙𝑠 along the columns to create the multivariate time-seriesXS∈R𝑇×2𝑛 .
In order to capture the dependencies between past and future stock movements, we segment the
multivariate time-seriesXS over time to construct the dataset as follows. For each time-step𝑡, we
create a pair consisting of the past𝑃 time-steps, denoted as 𝒙past and the future𝐹 steps denoted as
𝒙future. By applying this segmentation for𝑡∈[𝑃,𝑇−𝐹] , we generate the dataset which we denote
as:
D={(X S[𝑡−𝑃:𝑡],X S[𝑡+1 :𝑡+1+𝐹])} 𝑇−𝐹 𝑡=𝑃 (2)
The objective of the model is to generate a continuation ˆ𝒙future of an observed time-series 𝒙past, by
training the model on tuples of the form(𝒙past,𝒙 future)∈D . The simultaneous generation of2𝑛
time-series allows the preservation of the correlation dynamics observed in the training set.
4.1CoMeTS-GANArchitecture
The underlying model of CoMeTS-GAN is a Conditional Wasserstein Generative Adversarial Network
(C-WGAN) [2, 31]. This model is trained to learn the joint probability distribution of the collection
of future time-series 𝒙future in the training datasetD by optimizing the critic score. As for the
generator and the critic of the C-WGAN, we used a mixture of vanilla and temporal convolutional
neural networks. Figure 2 shows the architecture of our model.
Thegenerator 𝐺 is the main component ofCoMeTS-GAN. It is responsible for the actual generation
of the time-series ˆ𝒙future, which retains the statistical properties of the real time-series observed
by the generator. The architecture used for the generator network is composed of a series of 7
temporal convolutional blocks [3] with increasing dilation size and a final linear layer to adjust the
size of the output vector. Each temporal block is followed by a leaky ReLU activation function and
adropoutlayer.
Thecritic 𝐷 is responsible for assessing the realness of the generated samples. The architecture
used for the critic network is made of a series of convolutional layers having increasing filter
sizes, followed by a series of linear layers. Each convolutional and linear layer is followed by a
leaky ReLU activation and a dropout layer, and spectral normalization is applied on top of each
network layer. No activation function is used for the last layer of the network. We denote the
output of this sequential network as𝑜1, which is devoted to measuring the realness of the generated
time-series. A linear layer is present within the critic (top right of the figure) and is meant to address
the correlations of the multivariate time-series. The linear layer takes as input the correlation
coefficients computed between all pairs of the mid-prices and volumes of the 𝑛 stocks (i.e., 2𝑛 2 
pairs) and it outputs𝑜 2.
The overall output of the critic (i.e., the critic score) is the sum𝑜=𝑜 1+𝛼·𝑜 2, with𝛼∈[ 0, 1]
being a hyperparameter to weigh the relevance of the correlation. By summing these two scores,
we aim to capture the realism and correlation of the𝑛stocks.
CoMeTS-GAN Training.Upon input pair (𝒙past,𝒙 future)∈D , the framework is trained as follows.
The input of the generator is the concatenation of the past sequence 𝒙past and a noise vector
𝒛∼N( 0,𝑰) of the same length summed to a vector 𝒕 to embed the time information. The temporal
information is computed by first mapping each timestamp to the number of minutes elapsed since
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:9
Temporal convolutional block 1
Historical
Data
Temporal convolutional block 2
Temporal convolutional block N
Linear layer
Convolutional block 1
Convolutional block N
Linear block 1
Linear block N
Linear layer
MLP
Embedding
MLP
Embedding
Fig. 2. C-WGAN architecture. The ⌢ operator represents the concatenation of two vectors. The or operator
iteratively alternates between the real series𝒙 future and the generated series ˆ𝒙future.
the start of the trading day. This value is then discretized into uniform intervals, each representing
a fixed duration (10 minutes), effectively segmenting the trading session into a sequence of time
bins. This variable is then mapped to a high-dimensional embedding using a sinusoidal positional
encoding scheme, similar to those used in transformer architectures. In the generator, the time-step
embedding is processed by a 2-layer MLP with a non-linear activation function (𝑓(𝑥)=𝑥· 𝑒𝑥 1+𝑒𝑥 ) to
further enhance its expressiveness. The resulting time embedding is added directly to the noise,
effectively conditioning the generative process on the temporal context. This integration allows
the model to generate outputs that are sensitive to the progression of time within each sequence,
improving its ability to model temporal dynamics.
Each temporal block is fed with the output of the previous, concatenated with the noise vector𝑧
along the dimension of the features. The noise injection technique allows diversity in the model’s
output. Finally, the output of the last temporal block is directly fed to the last linear layer. The
output of the generator network is the future sequence ˆ𝒙future.
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:10 Masi et al.
The input of the critic is the concatenation of the past sequence 𝒙past with either the real
continuation 𝒙future drawn from the dataset, or a generated one ˆ𝒙future from the generator. In the
discriminator, the temporal information is processed in the same way of the generator, but the
resulting time embedding is concatenated as an additional channel to the input sequence along the
feature dimension.
The result of the concatenation is fed to the convolution and linear blocks to produce a single
value in output, representing the standard critic score𝑜1. Additionally, the correlations between
the features of the future sequence in the input are computed. All the 2𝑛 2  correlation coefficients
are input to the linear layer to produce the score𝑜2. The output of the critic is the sum of the two
contributions, as mentioned above.
We adopt spectral normalization to enforce the Lipschitz continuity constraint, due to its superior-
ity to other techniques like weight clipping or gradient penalty and for its ease of applicability [32].
4.2 Diffusion Models: ACritic-Guidedgeneration
Sohl-Dickstein et al. [42] and Song et al. [43] show that any pre-trained diffusion model can be
conditioned using the gradients of a classifier, steering the denoising (i.e., generation) process
towards an arbitrary class label y. This technique, called classifier guidance, in diffusion models
typically involves modifying the score function to incorporate the gradient from an external
classifier that estimates the likelihood that a sample belongs to a target class.
In CoMeTS-GAN, we note that the Critic module is trained to distinguish between real and synthetic
stock price sequences; it implicitly learns a representation of realism. Therefore, we propose to
utilize our Critic as a surrogate classifier, where its gradient can be leveraged to enhance the
generation process of the diffusion model. Mathematically, the diffusion model’s score function,
denoted as𝑠(𝑥 𝑡,𝑡), is adjusted by incorporating the gradient of the WGAN critic𝐷(𝑥):
˜𝑠=𝑠(𝑥 𝑡,𝑡)+𝑤·∇ 𝑥𝑡𝐷(𝑥𝑡),(3)
where𝑤 modulates the guidance strength. This modification encourages the diffusion process
to produce samples that align more closely with the distribution learned by the WGAN critic,
effectively biasing the sampling trajectory toward regions of higher realism.
In the experimental section, we instantiate ourCritic-Guidedstrategy using DiffTime [ 8], a state-
of-the-art Diffusion Model trained on our time-series datasets. We demonstrate how the gradients
of the Critic can actually guide the diffusion denoising process at inference time, improving the
cross-correlation fidelity of the generated time-series and yielding a quality-aware generation
pipeline. More broadly, our approach suggests that any differentiable generative network trained on
a domain-specific realism metric can be used to enhance the generation quality of general-purpose
diffusion models.
5 Experiments
In this section, we evaluate the performance of our framework against SOTA approaches. We first
compare CoMeTS-GAN using several benchmarks and newly curated datasets to ensure a rigorous
assessment. Our primary focus is assessing the fidelity of the generated time-series in comparison
to real ones. Eventually, we examine the improvement in generation realism achieved by the
Critic-Guidedstrategy, instantiated using DiffTime [ 8] a recent diffusion models for time-series
generation. We ran our Python-based framework on a NVIDIA 2060 GPU.1
1We commit to publicly releasing our source code upon acceptance, enabling other researchers to reproduce our results and
use the framework for their own experiments.
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:11
5.1 Datasets
We test the performance of our framework across data showing varying periodicity, discreteness,
level of noise, regularity of time-steps, and correlation across time and features. We also include real
stock market time-series. In detail, the considered datasets — including well-known benchmarks
from the literature — are the following:
• Sines[ 51]: Multivariate sinusoidal sequences with different frequencies 𝜂 and phases 𝜙.
Specifically, the dataset is obtained with𝑠𝑖(𝑡)=sin(2𝜋𝜂 𝑖𝑡+𝜃 𝑖), where𝑖∈{ 1,..., 5},𝜂𝑖∼
U[0,1]and𝜃 𝑖∼U[−𝜋,𝜋].
• Multivariate Gaussian Model[ 51]: Sequences from auto-regressive multivariate Gaussian
models, defined as:𝑔𝑖(𝑡)=𝜙 𝑖𝑔𝑖(𝑡− 1)+𝑞 where𝑞∼N( 0,𝜎𝑖+( 1−𝜎𝑖)),𝜙𝑖∈[ 0, 1], and
𝜎𝑖 ∈ [−1, 1]. The coefficients 𝜙𝑖 and𝜎𝑖 allow to control the correlation across time and
features, respectively.
• Stock Mid-Prices & Volumes[ 1]: The source of stock market data is LOBSTER2, an online limit
order book data tool to provide limit order book data for the NASDAQ traded stocks. From
limit order book data, it is easy to compute the mid-price with the temporal resolution of
choice, that in our case, is minute. We focus on four stocks, namely, Coca-Cola (KO), PepsiCo
(PEP), Nvidia (NVDA), and Kansas City Southern (KSU). The time period of choice is from
2018-02-02 to 2018-10-11 for the training set, and from 2018-10-12 to 2018-11-14 for the
validation set. Table 1 shows the Pearson correlation coefficient between them.
We observe how some are highly positively correlated (KO and PEP, NVDA and KSU), and
some are highly negatively correlated (PEP and NVDA, PEP and KSU, KO and KSU, KO
and NVDA). To test the scalability of our generative framework, we selected the 30 stocks
composing the DJIA index from 2017-02-02 to 2017-10-11 for the training set and from
2017-10-12 to 2017-11-14 for the validation set.
For these time-series, we follow the same preprocessing pipeline. For the mid-prices, we
compute the log-returns normalized using a𝑧-score approach. Instead, volumes are scaled
in the[−1, 1] with a min-max approach, then followed by tanh activation function, which
scales the volumes to the positive domain.
KO PEP NVDA KSU
KO 1.0 0.94−0.66−0.52
PEP 0.94 1.0−0.81−0.56
NVDA −0.66−0.81 1.0 0.65
KSU −0.52−0.56 0.65 1.0
Table 1. Pearson correlation between the stock prices in the validation set of the multi-stock dataset.
5.2 Evaluation Metrics
We measure the performance of our framework in terms of the following aspects:Realism,Diversity,
Stylized Facts,Reactivity,Scalability.
Realism.We measure the realism of generated time-series by using theDiscriminative Score,
which offers a quantitative measure of the similarity betweenrealandsynthetic(orgenerated)
time-series. It was proposed in [51] and is computed as follows. An LSTM is trained to differentiate
between sequences from the original and generated datasets. A standard supervised learning task
2LOBSTER https://lobsterdata.com/
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:12 Masi et al.
is performed and the resulting classification error on the test set (the lower the better) provides a
quantitative measure of similarity.
Diversity.This aspect refers to the range and variability of patterns and structures present
in the generated time-series data. It is crucial because a well-working generative model should
produce data that fully explores the natural variations present in real time-series, rather than simply
replicating or memorizing the training data (problem known as “mode collapse").
Cross-correlation distance.In order to examine the model’s ability to capture the correlation
dynamics that exist between stocks we measure the distance between the cross-correlations of real
and generated stocks using the cross-correlation distance defined in 3.4. Formally, at the end of
each epoch, for each of the 2𝑛 2  pairs of features(𝑆𝑖,𝑆𝑗), we measure the𝑑𝜌(𝑆𝑖,𝑆𝑗) with respect to
their synthetic counterparts.
Stylized Facts.We investigate the properties of the synthetic traces by analyzing the most
common stylized facts in the financial domain as discussed in Section 3.3.
5.3CoMeTS-GANResults
5.3.1 Realness of Generated Data.We can generate arbitrarily long stock traces thanks to the
auto-regressive applicationof the model to the input time-series. The generation process can be
defined as follows: (1) the model is fed with a multivariate of length𝑃, that is a tensor in R𝑃×2𝑛 of
original stock data; (2) the output of the model, is a multivariate time-series of length𝐹 that is a
tensor in R𝐹×2𝑛 of synthetic stock data; (3) the last𝑃 time-steps of the synthetic sequence are fed
to the model; (4) steps 2 and 3 are repeated until a total number of generative steps are done.
By varying the random seed we are able to generate several multivariate time-series. Figure 3
shows the execution of three runs, in addition to the real trace (orange line). As we can observe,
the model does not incur self-induction (i.e., it does not generate a trend that remains indefinitely
influenced by it). Furthermore, the model respects the diversity property, generating different
sequences from the same input if the random noise changes, preserving the correlation dynamics.
In fact, as the training of the model proceeds, the average cross-correlation distance between real
and synthetic data decreases, as we can see in Figure 4, becoming negligible among all the pairs of
stocks.
2500 5000 7500390
Steps
45.0
47.5
50.0Price ($)
KO
2500 5000 7500390
Steps
105
110
115Price ($)
PEP
2500 5000 7500390
Steps
200
250Price ($)
NVDA
2500 5000 7500390
Steps
90
100
110Price ($)
KSU
Observed Real
Fig. 3. Diversity in price generation.
The fact that the model is able to capture the correlation dynamics is also evident in Figure 5,
where we plot the prices of the stocks, and the average cross-correlation distance is0.04. Figure 6
shows the corresponding volumes.
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:13
0 20 40 60 80 100
Epoch
0.0
0.2
0.4
0.6
MSE( ( , ), ( , ))
Price Volume
Fig. 4. Average cross-correlation distance during training.
0 5000
40
50Price ($)
KO
0 5000
Steps
(PEP, KO) = 0.94
110
120
130
PEP
0 5000
Steps
(NVDA, KO) = 0.66
150
200
250
NVDA
0 5000
Steps
(KSU, KO) = 0.52
90
100
110 KSU
0 5000
40
50Price ($)
0 5000
Steps
(PEP, KO) = 0.90
110
120
130
0 5000
Steps
(NVDA, KO) = 0.56
150
200
250
0 5000
Steps
(KSU, KO) = 0.65
90
100
110
Observed Real CoMeTS-GAN
Fig. 5. Price - Correlation between KO and the other stocks. While the generated data shows a downward
trend, PEP and KO time-series keep the same correlation property of real data.
2500 5000 7500390
Steps
0
50000
100000Shares
KO
2500 5000 7500390
Steps
0
100000Shares
PEP
2500 5000 7500390
Steps
0
100000
200000Shares
NVDA
2500 5000 7500390
Steps
0
20000Shares
KSU
Observed Real CoMeTS-GAN
Fig. 6. Real and Synthetic volumes - the synthetic data is able to partially reproduce the U-shaped volume
pattern observed in the real data.
We measure the stylized facts on the auto-regressive generation of stock mid-prices and volumes
for 24 trading days, given that a trading day lasts for 6.5 hours, we generate 9360 minutes in total.
Notice that most of existing approaches are unable to generate such a long stock time-series data.
Results are averaged over 10 runs where we vary the seed and the randomization of the generation.
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:14 Masi et al.
0.02
 0.00 0.02
Minutely Log-Returns
100
102
Density
KO
0.02
 0.00 0.02
Minutely Log-Returns
100
102
Density
PEP
0.02
 0.00 0.02
Minutely Log-Returns
100
102
Density
NVDA
0.02
 0.00 0.02
Minutely Log-Returns
100
102
Density
KSU
Real CoMeTS-GAN
(a) Intraday log-return distribution:Δ𝑡=1.
0.02
 0.00 0.02
15 Minute Log-Returns
101
102
Density
KO
0.02
 0.00 0.02
15 Minute Log-Returns
101
102
Density
PEP
0.02
 0.00 0.02
15 Minute Log-Returns
101
102
Density
NVDA
0.02
 0.00 0.02
15 Minute Log-Returns
101
102
Density
KSU
Real CoMeTS-GAN (b) Intraday log-return distribution:Δ𝑡=15.
Fig. 7. Real and synthetic distribution of intraday log-return distributions. The similarity between the
distributions assesses the model’s ability to replicate these statistical features of real market data.
Figure 7a and 7b show the histogram of the intraday log-returns with periods of Δ𝑡= 1and
Δ𝑡= 15minutes, respectively. Results show a fat-tailed distribution as expected for the first one,
and as we increase the period Δ𝑡, the distribution of returns better fits a normal distribution. The
described property is often referred to asaggregational normality. As seen in the figures, both real
and generated data closely follow these known properties for all the stocks.
In Figure 8, we plot the autocorrelation of the minutely intraday log-returns of the stocks with
different time lags of 1, 10, 20, and 30 minutes. As we can observe, at increasing lag, the returns tend
to cluster around a null correlation value. The stylized fact related to theabsence of autocorrelation
is thus present in both real and generated traces.
Figure 9 shows the autocorrelation coefficients of the volatility at varying day lag. The volatility
is computed as the standard deviation of the returns. We observe that the correlation is much
higher when the lag is short and decreases as the lag increases, confirming that the volatility tends
to cluster in time. The plot also confirms that all the considered stocks show this behavior, both in
the real and generated traces.
5.3.2 Comparison with State-of-the-Art.We now compare CoMeTS-GAN with several state-of-the-art
approaches, namely TTS-GAN [25], COSCI-GAN [41], GT-GAN [21], TimeGAN [51], RCGAN [16]
and C-RNN-GAN [33]. For purely auto-regressive approaches, we compare against RNNs trained
with teacher-forcing (T-Forcing) [18] as well as professor-forcing (P-Forcing) [23]. For additional
comparison, we consider the performance of WaveNet [35] as well as its GAN counterpart Wave-
GAN [15]. We first focus on standard general-domain benchmarks from the literature, and the we
focus on financial data.
Synthetic data realism on literature benchmarks.We first show the results obtained on the Gaussian
model dataset and on the Sines dataset in Table 2 in terms of discriminative score (i.e., realism).
Numerical results show that our model performances are somehow comparable with respect to
more complex state-of-the-art approaches. In fact, our model is specifically designed for financial
data while the literature benchmarks do not focus on financial datasets. This experiment highlights
both the potential performance and the versatility of our model, beyond the specific domain for
which it was originally developed.
It is also important to note that our model is structurally different from more advanced models
such as TimeGAN, COSCI-GAN, and GT-GAN. In such work, the original time-series is factorized
in short sub-sequences, and the model outputs a synthetic set of such sub-sequences at inference
time, but there is no natural and intuitive way to recombine them to obtain a longer sequence,
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:15
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
101
Density
Lag=1
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
100
101
Density
Lag=10
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
100
101
Density
Lag=20
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
101
Density
Lag=30
Real CoMeTS-GAN
(a) KO
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
101
Density
Lag=1
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
100
101
Density
Lag=10
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
101
Density
Lag=20
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
101
Density
Lag=30
Real CoMeTS-GAN (b) PEP
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
101
Density
Lag=1
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
100
Density
Lag=10
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
100
101
Density
Lag=20
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
101
Density
Lag=30
Real CoMeTS-GAN
(c) NVDA
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
100
Density
Lag=1
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
101
Density
Lag=10
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
101
Density
Lag=20
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
101
Density
Lag=30
Real CoMeTS-GAN (d) KSU
Fig. 8. Distributions of returns autocorrelation coefficients with increasing lags ( Δ𝑡= 1, 10, 20, 30min). The
close match between real and CoMeTS-GAN demonstrates that the model faithfully replicates the diminishing
autocorrelation.
1 2 3 4 5 6 7 8 9 10
Lag (Days)
0.2
0.0
Correlation
Coefficient
KO
1 2 3 4 5 6 7 8 9 10
Lag (Days)
0.2
0.0
0.2
Correlation
Coefficient
PEP
1 2 3 4 5 6 7 8 9 10
Lag (Days)
0.2
0.0
0.2
Correlation
Coefficient
NVDA
1 2 3 4 5 6 7 8 9 10
Lag (Days)
0.0
0.2
Correlation
Coefficient
KSU
Real CoMeTS-GAN
Fig. 9. Correlation coefficients of volatility at increasing day lag. CoMeTS-GAN successfully captures the
general trend and low level of volatility autocorrelations found in real financial data.
retaining temporal continuation. Instead, our model is able to generate a single time-series with up
to 9360 observations (24 trading days). Furthermore, the training times of such complex models
are generally higher — typically in the range of tens of hours (e.g., TimeGAN required 39 hours of
training, compared to just 4 hours and 20 minutes for our model).
Finally, Table 2 presents also an ablation study to assess the contribution of the cross-correlation
term in the critic score. In particular, rows one and two of the table report the discriminative score
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:16 Masi et al.
for𝛼= 0and 𝛼= 1, respectively. The results indicate that incorporating the cross-correlation term
improves model performance, especially in settings with high inter-feature correlation (i.e., high
values of𝜙), thereby demonstrating the effectiveness of the cross-correlation coefficients.
Correlation dynamics on financial synthetic data.As previously mentioned, our model has com-
parable performance wrt more recent approaches, though it does not outperform them in terms of
realism. However, our model is specifically designed for financial data, and to improved correlation
dynamics of synthetic data. Therefore, we now evaluate the most promising approaches in Table 2,
i.e. COSCI-GAN [41] and GT-GAN [21], with respect to our financial dataset, to highlight the
advantages ofCoMeTS-GANover the aforementioned general-purpose approaches.
Figure 10 depicts the pair-wise correlations of the stocks’ price over windows of one trading day
(390 time-steps) showing that CoMeTS-GAN is the best model in respecting the correlation values of
the real data, as also reported in Table 3 in terms of Wasserstein distance between the histograms.
CoMeTS-GAN COSCI-GAN GT-GAN
KO - PEP 0.13 0.29 0.30
KO - NVDA 0.19 0.28 0.28
KO - KSU 0.10 0.71 0.25
PEP - NVDA 0.20 0.52 0.29
PEP - KSU 0.25 0.85 0.26
NVDA - KSU 0.05 0.52 0.35
Table 3. Wasserstein distance of the distributions in Figure 10.
Figure 11 shows the distribution of the correlation between the average traded volume and
the volatility over two trading days. According to the stylized fact, trading volume and volatility
are positively correlated, and it is clear that CoMeTS-GAN’s data are the best in reproducing this
expected behavior.
5.3.3 Reactivity.An important what-if question in finance concerns the market impact of meta-
orders and the subsequent propagation of price shocks [5]. In other words, how would the market
react if a given amount of money were traded? In this section, we demonstrate how our conditional
framework can be leveraged to simulate interactive market dynamics, and address such questions.
In particular, we conducted an experiment in which a perturbation was manually introduced to the
Gaussian Dataset Sines Dataset
Temporal Correlations (fixing𝜎=0.8) Feature Correlations (fixing𝜙=0.8)
Model 𝜙=0.2 𝜙=0.5 𝜙=0.8 𝜎=0.2 𝜎=0.5 𝜎=0.8
Discriminative score (lower the better)
CoMeTS-GAN(w/o cross-corr.) 0.211±0.007 0.195±0.005 0.137±0.012 0.187±0.006 0.206±0.018 0.137±0.012 −−
CoMeTS-GAN(w/ cross-corr.) 0.187±0.003 0.183±0.005 0.102±0.006 0.180±0.009 0.164±0.011 0.102±0.006 0.013±0.007
TTS-GAN 0.494±0.004 0.470±0.010 0.437±0.025 0.305±0.019 0.311±0.037 0.437±0.024 0.092±0.045
COSCI-GAN 0.167±0.007 0.105±0.013 0.070±0.018 0.091±0.020 0.075±0.030 0.070±0.018 0.042±0.019
GT-GAN 0.364±0.082 0.162±0.122 0.172±0.120 0.085±0.091 0.147±0.110 0.172±0.120 0.012±0.014
TimeGAN 0.175±0.006 0.174±0.012 0.105±0.005 0.181±0.006 0.152±0.011 0.105±0.005 0.011±0.008
RCGAN 0.177±0.012 0.190±0.011 0.133±0.019 0.186±0.012 0.190±0.012 0.133±0.019 0.022±0.008
C-RNN-GAN 0.391±0.006 0.227±0.017 0.220±0.016 0.198±0.011 0.202±0.010 0.220±0.016 0.229±0.040
T-Forcing 0.500±0.000 0.500±0.000 0.499±0.001 0.499±0.001 0.499±0.001 0.499±0.001 0.495±0.001
P-Forcing 0.498±0.002 0.472±0.008 0.396±0.018 0.460±0.003 0.408±0.016 0.396±0.018 0.430±0.027
WaveNet 0.337±0.005 0.235±0.009 0.229±0.013 0.217±0.010 0.226±0.011 0.229±0.013 0.158±0.011
WaveGAN 0.336±0.011 0.213±0.013 0.230±0.023 0.192±0.012 0.205±0.015 0.230±0.023 0.277±0.013
Table 2. Discriminative score for the Gaussian and Sines datasets. First and second best are highlighted in
bold and underline respectively.
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:17
1
 0 1
0
2
4
6Density
KO - PEP
1
 0 1
0
2
4
6 KO - NVDA
1
 0 1
0
2
4
6 KO - KSU
1
 0 1
0
2
4
6 PEP - NVDA
1
 0 1
0
2
4
6 PEP - KSU
1
 0 1
0
2
4
6NVDA - KSU
1
 0 1
0
2
4
6Density
1
 0 1
0
2
4
6
1
 0 1
0
2
4
6
1
 0 1
0
2
4
6
1
 0 1
0
2
4
6
1
 0 1
0
2
4
6
1
 0 1
0
2
4
6Density
1
 0 1
0
2
4
6
1
 0 1
0
2
4
6
1
 0 1
0
2
4
6
1
 0 1
0
2
4
6
1
 0 1
0
2
4
6
Real CoMeTS-GAN COSCI-GAN GT-GAN
Fig. 10. Pairwise correlation distributions of daily asset prices (390 minutes). CoMeTS-GAN most closely
matches the empirical correlation structures.
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
100
Density
KO
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
100
Density
PEP
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 1
100
Density
NVDA
1.0
 0.5
 0.0 0.5 1.0
Correlation Coefficient
10 2
10 1
100
Density
KSU
Real CoMeTS-GAN COSCI-GAN GT-GAN
Fig. 11. Distributions of volume–volatility correlation coefficients over windows of two days. CoMeTS-GAN
shows superior ability to reproduce this key market relationship.
time-series of KO, to observe how the model reacts in generating the other stocks. In particular, we
focus on the reaction of PEP, which is highly positively correlated with KO.
Specifically, let ˆ𝒙𝑡:𝑡+𝐹 be the sub-sequence generated by the model starting at time𝑡. A pertur-
bation is introduced by substituting what the model actually generates with ˆ𝒙𝑡:𝑡+𝐹+𝛼·𝜎( ˆ𝒙𝑡:𝑡+𝐹),
where𝜎(·)being the standard deviation function.
Figure 12 shows the perturbation introduced on KO in the red window. It is interesting to observe
how the model “propagates" the shock and adjusts the generation of the non-perturbed stock in
order to preserve the correlation following the perturbation event.
Figure 13 shows the correlation of KO and PEP, varying the intensity of the perturbation. The
orange line is the correlation between real KO and real PEP, which is highly positive, close to 1. The
green line is the correlation between their synthetic versions cKO and dPEP, which is still positive
and high. Let dKO𝑝 be the synthetic version of KO subject to the perturbation. The red line is the
correlation between dKO𝑝 and dPEP. Let PEP𝑟 be the synthetic version of PEP generated by the model
in response to the perturbation observed in KO. The purple line is the correlation betweendKO𝑝 and
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:18 Masi et al.
0 390 990 1290 8191
Steps
400000
450000Price ($)
KO
0 390 990 1290 8191
Steps
1.0
1.1Price ($)
1e6 PEP
W/o Per W/ Per = 0.4
Fig. 12. Price evolution of KO (top) and PEP (bottom) under two scenarios: with and without a perturbation
applied to KO (𝜎=0.4, highlighted period).
PEP𝑟 . The experiment was repeated for several seeds, generating the standard error evidenced by
the bands in the figure. As we can see, the model punctually intervenes in adjusting the generation
of PEP to preserve the correlation with KO after the perturbation.
0.1 0.2 0.3 0.4 0.5 0.6 0.7
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Correlation
coefficient
(KO, PEP)
(KO, PEP)
(KOp, PEP)
(KOp, PEPr)
Fig. 13. Correlation of the KO and PEP stocks varying the intensity of the perturbation. The experiment
demonstrates that a shock to KO’s price induces a correlated response in PEP, illustrating CoMeTS-GAN ’s
capacity to simulate realistic cross-asset market reactions, preserving inter-stock dependencies following
external interventions.
5.3.4 Scalability.Considering the model’s architecture in Figure 2, the size of the input and output
of the generator and the input of the discriminator linearly depend on𝑛. On the other hand, the
intermediate hidden layers of the networks remain constant with respect to𝑛. The linear layer in the
critic takes as input a vector of size 2𝑛 2 . To test the model’s scalability, we run the auto-regressive
application on all 30 stocks included in the DJIA index (Figure 14), obtaining realistic correlation
dynamics. Indeed, the synthetic traces still show the expected correlation properties, even when
considered in the simultaneous generation of numerous time-series. Furthermore, all the stylized
facts that characterize the returns are preserved.
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:19
AAPL AMGN AXP BA CAT
CRM CSCO CVX DIS GE
GS HD HON IBM INTC
JNJ JPM KO MCD MMM
MRK MSFT NKE PG TRV
UNH V VZ WBA WMT
Prices
Observed Real Synthetic
Fig. 14. Concurrent price generation of the 30 components of the DJIA, demonstrating the framework’s
scalability.
5.4 A Critic-as-a-Guide framework
While WGANs leverage a critic to estimate the Wasserstein distance and enforce realistic data
distributions, diffusion models utilize iterative noise conditioning to generate high-fidelity samples.
In this section, we explore the theoretical and practical implications of repurposing a pre-trained
WGAN critic as a guidance mechanism for classifier-guided diffusion models, with a focus on stock
price generation.
To assess efficacy, we propose benchmarking both guided and unguided diffusion models by
examining the correlation dynamics of the generated time-series. Specifically, we employ a diffusion
model based on DiffTime [8] for the unconditional generation windows of 150 time-steps across
four selected stocks: KO, PEP, NVDA, and KSU. For each generated window, we compute the
pairwise correlations between the stocks, resulting in the distributions visualized in Figure 15a. It
illustrates the correlation distributions derived from the unguided diffusion model (𝑤= 0in Eq. 3),
while Figure 15b shows those obtained with guided generation (𝑤= 250), highlighting a much
closer alignment with the real data distribution and demonstrating a substantial improvement due
to guidance. To quantify the improvement, we report the Wasserstein distance in Table 4.
To further highlight the value of re-purposing the WGAN critic to guide the generation, Figure 15c
presents the generation of a counter-factual scenario. In particular, the guidance is applied in the
opposite direction, i.e., by flipping the classifier gradients (𝑤=− 250). By reversing the guidance
signal, the generated samples are explicitly discouraged from aligning with the real data distribution,
resulting in correlation patterns that diverge markedly from the empirical ones and from those
generated by both the guided and unguided models. This experiment underscores the importance
of effective guidance not only for enhancing sample quality but also for generating meaningful
counterfactuals under adversarial guidance.
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:20 Masi et al.
Real
DiffTime
DiffTime + Critic
DiffTime + Critic (CF)
1
 0 1
0
2
4Density
KO - PEP
1
 0 1
0
2
4 KO - NVDA
1
 0 1
0
2
4 KO - KSU
1
 0 1
0
2
4 PEP - NVDA
1
 0 1
0
2
4 PEP - KSU
1
 0 1
0
2
4NVDA - KSU
(a) Synthetic.
1
 0 1
0
2
4Density
KO - PEP
1
 0 1
0
2
4 KO - NVDA
1
 0 1
0
2
4 KO - KSU
1
 0 1
0
2
4 PEP - NVDA
1
 0 1
0
2
4 PEP - KSU
1
 0 1
0
2
4NVDA - KSU
(b) Synthetic with guidance.
1
 0 1
0
2
4Density
KO - PEP
1
 0 1
0
2
4 KO - NVDA
1
 0 1
0
2
4 KO - KSU
1
 0 1
0
2
4 PEP - NVDA
1
 0 1
0
2
4 PEP - KSU
1
 0 1
0
2
4NVDA - KSU
(c) Synthetic with guidance for counterfactual generation.
Fig. 15. Distributions of price correlations between asset pairs for real data and synthetic series generated by
three diffusion model variants:DiffTime,DiffTime + Critic, andDiffTime + Critic (CF). Adding the Critic as
guidance (middle row) results in synthetic correlations that more closely match the real market structure,
while counterfactual guidance (bottom row) produces distinctly different correlation patterns, illustrating the
model’s flexibility for simulating both realistic and counterfactual scenarios.
DiffTime + Critic (𝑤=250) DiffTime (𝑤=0)
KO - PEP 0.07 0.26
KO - NVDA 0.09 0.21
KO - KSU 0.15 0.20
PEP - NVDA 0.04 0.23
PEP - KSU 0.17 0.19
NVDA - KSU 0.04 0.30
Table 4. Wasserstein distance of the distributions in Figure 15.
6 Discussion and Conclusion
In this work, we discuss novel solutions for generating high-quality interdependent markets using
deep learning models. Our quality-aware framework introduces three key contributions: First, we
create a new critic score for a C-WGAN, specifically suitable for time-series generation, based
on the degree of realism of the cross-correlation between the features; Then we introduce a new
architecture based on a C-WGAN, to capture aspects of interdependence among financial markets
and to generate time-series with similar characteristics to real ones; Finally, we discuss how our
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:21
Critic can be repurposed to enhance the performance of any existing diffusion model framework.
We thoroughly analyze the model’s performance both on benchmark datasets and new stock
market traces measuring the performance in terms ofDiscriminative Score,Diversity,Stylized Facts,
Reactivity, andScalability. The results are promising: in all respects, the proposed architecture yields
good results with respect to state-of-the-art approaches such as TimeGAN, solving its inherent
issues related to training time and temporal continuation of long time-series.
We believe this work demonstrates that a small GAN architecture can be effectively employed in
specific domains, to preserve particular statistical properties of synthetic data. Most importantly,
GANs’ critics can be reused within more sophisticated diffusion models without the need for
retraining. We release our code to foster future research in this direction.
Code and Data availability
Data are extracted fromLOBSTER 3, an online limit order-book data provider, which is publicly
available for the research community with an annual fee.
We commit to publicly releasing our source code upon acceptance.
References
[1] [n. d.]. LOBSTER: Limit Order Book System - The Efficient Reconstructor. https://lobsterdata.com/.
[2] Martin Arjovsky, Soumith Chintala, and Léon Bottou. 2017. Wasserstein Generative Adversarial Networks. In
Proceedings of the 34th International Conference on Machine Learning. PMLR, 214–223.
[3] Shaojie Bai, J Zico Kolter, and Vladlen Koltun. 2018. An empirical evaluation of generic convolutional and recurrent
networks for sequence modeling.arXiv preprint arXiv:1803.01271(2018).
[4] Malcolm Baker and Jeffrey Wurgler. 2007. Investor sentiment in the stock market.Journal of economic perspectives21,
2 (2007), 129–151.
[5] Jean-Philippe Bouchaud, Julius Bonart, Jonathan Donier, and Martin Gould. 2018.Trades, quotes and prices: financial
markets under the microscope. Cambridge University Press.
[6] Hans Buehler, Lukas Gonon, Josef Teichmann, and Ben Wood. 2019. Deep hedging.Quantitative Finance19, 8 (2019),
1271–1291.
[7] Longbing Cao. 2022. Ai in finance: challenges, techniques, and opportunities.ACM Computing Surveys (CSUR)55, 3
(2022), 1–38.
[8] Andrea Coletta, Sriram Gopalakrishnan, Daniel Borrajo, and Svitlana Vyetrenko. 2023. On the constrained time-series
generation problem.Advances in Neural Information Processing Systems36 (2023), 61048–61059.
[9] Andrea Coletta, Matteo Prata, Michele Conti, Emanuele Mercanti, Novella Bartolini, Aymeric Moulin, Svitlana
Vyetrenko, and Tucker Balch. 2021. Towards Realistic Market Simulations: A Generative Adversarial Networks
Approach. InProceedings of the Second ACM International Conference on AI in Finance (ICAIF ’21). 1–9.
[10] Rama Cont. 2001. Empirical properties of asset returns: stylized facts and statistical issues.Quantitative finance1, 2
(2001), 223.
[11] Rama Cont, Mihai Cucuringu, Renyuan Xu, and Chao Zhang. 2025. Tail-gan: Learning to simulate tail risk scenarios.
Management Science(2025).
[12] Rama Cont and Milena Vuletić. 2025. Data-driven hedging with generative models.A vailable at SSRN 5282525(2025).
[13] Christa Cuchiero, Wahid Khosrawi, and Josef Teichmann. 2020. A Generative Adversarial Network Approach to
Calibration of Local Stochastic Volatility Models.Risks8, 4 (Dec. 2020), 101. doi:10.3390/risks8040101
[14] Prafulla Dhariwal and Alexander Nichol. 2021. Diffusion models beat gans on image synthesis.Advances in neural
information processing systems34 (2021), 8780–8794.
[15] Chris Donahue, Julian McAuley, and Miller Puckette. 2018. Adversarial audio synthesis.arXiv preprint arXiv:1802.04208
(2018).
[16] Cristóbal Esteban, Stephanie L. Hyland, and Gunnar Rätsch. 2017. Real-Valued (Medical) Time Series Generation with
Recurrent Conditional GANs.arXiv:1706.02633 [cs, stat](Dec. 2017). arXiv:1706.02633 [cs, stat]
[17] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and
Yoshua Bengio. 2014. Generative Adversarial Nets. InAdvances in Neural Information Processing Systems, Vol. 27.
Curran Associates, Inc.
[18] Alex Graves. 2013. Generating sequences with recurrent neural networks.arXiv preprint arXiv:1308.0850(2013).
3https://lobsterdata.com/
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:22 Masi et al.
[19] David Hirshleifer and Siew Hong Teoh. 2003. Herd behaviour and cascading in capital markets: A review and synthesis.
European Financial Management9, 1 (2003), 25–66.
[20] Jonathan Ho, Ajay Jain, and Pieter Abbeel. 2020. Denoising diffusion probabilistic models.Advances in neural
information processing systems33 (2020), 6840–6851.
[21] Jinsung Jeon, Jeonghak Kim, Haryong Song, Seunghyeon Cho, and Noseong Park. 2022. GT-GAN: General Purpose
Time Series Synthesis with Generative Adversarial Networks.Advances in Neural Information Processing Systems35
(2022), 36999–37010.
[22] James Jordon, Lukasz Szpruch, Florimond Houssiau, Mirko Bottarelli, Giovanni Cherubin, Carsten Maple, Samuel N
Cohen, and Adrian Weller. 2022. Synthetic Data–what, why and how?arXiv preprint arXiv:2205.03257(2022).
[23] Alex M Lamb, Anirudh Goyal ALIAS PARTH GOYAL, Ying Zhang, Saizheng Zhang, Aaron C Courville, and Yoshua
Bengio. 2016. Professor forcing: A new algorithm for training recurrent networks.Advances in neural information
processing systems29 (2016).
[24] Markus Leippold, Lujing Su, and Alexandre Ziegler. 2016. How index futures and ETFs affect stock return correlations.
A vailable at SSRN 2620955(2016).
[25] Xiaomin Li, Vangelis Metsis, Huangyingrui Wang, and Anne Hee Hiong Ngu. 2022. Tts-gan: A transformer-based
time-series generative adversarial network. InArtificial Intelligence in Medicine: 20th International Conference on
Artificial Intelligence in Medicine, AIME 2022, Halifax, NS, Canada, June 14–17, 2022, Proceedings. Springer, 133–143.
[26] Haksoo Lim, Minjung Kim, Sewon Park, and Noseong Park. 2023. Regular time-series generation using SGM.arXiv
preprint arXiv:2301.08518(2023).
[27] Lequan Lin, Zhengkun Li, Ruikun Li, Xuliang Li, and Junbin Gao. 2024. Diffusion models for time-series applications:
a survey.Frontiers of Information Technology & Electronic Engineering25, 1 (2024), 19–41.
[28] G. Marti. 2020. CORRGAN: Sampling Realistic Financial Correlation Matrices Using Generative Adversarial Networks.
ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)(2020). doi:10.
1109/ICASSP40776.2020.9053276
[29] Akib Mashrur, Wei Luo, Nayyar A Zaidi, and Antonio Robles-Kelly. 2020. Machine learning for financial risk manage-
ment: a survey.Ieee Access8 (2020), 203203–203223.
[30] Giuseppe Masi, Matteo Prata, Michele Conti, Novella Bartolini, and Svitlana Vyetrenko. 2023. On correlated stock
market time series generation. InProceedings of the Fourth ACM International Conference on AI in Finance. 524–532.
[31] Mehdi Mirza and Simon Osindero. 2014. Conditional Generative Adversarial Nets.arXiv:1411.1784 [cs, stat](Nov. 2014).
arXiv:1411.1784 [cs, stat]
[32] Takeru Miyato, Toshiki Kataoka, Masanori Koyama, and Yuichi Yoshida. 2018. Spectral Normalization for Generative
Adversarial Networks. InInternational Conference on Learning Representations.
[33] Olof Mogren. 2016. C-RNN-GAN: Continuous Recurrent Neural Networks with Adversarial Training.arXiv:1611.09904
[cs](Nov. 2016). arXiv:1611.09904 [cs]
[34] Vincenzo Moscato, Antonio Picariello, and Giancarlo Sperlí. 2021. A benchmark of machine learning approaches for
credit score prediction.Expert Systems with Applications165 (2021), 113986.
[35] Aaron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalchbren-
ner, Andrew Senior, and Koray Kavukcuoglu. 2016. Wavenet: A generative model for raw audio.arXiv preprint
arXiv:1609.03499(2016).
[36] Ahmet Murat Ozbayoglu, Mehmet Ugur Gudelek, and Omer Berat Sezer. 2020. Deep learning for financial applications:
A survey.Applied soft computing93 (2020), 106384.
[37] Szilard Pafka and Imre Kondor. 2004. Estimated correlation matrices and portfolio optimization.Physica A: statistical
mechanics and its applications343 (2004), 623–634.
[38] Jochen Papenbrock, Peter Schwendner, Markus Jaeger, and Stephan Krügel. 2021. Matrix Evolutions: Synthetic
Correlations and Explainable Machine Learning for Constructing Robust Investment Portfolios.The Journal of
Financial Data Science3, 2 (April 2021), 51–69. doi:10.3905/jfds.2021.1.056
[39] Vamsi K Potluru, Daniel Borrajo, Andrea Coletta, Niccolò Dalmasso, Yousef El-Laham, Elizabeth Fons, Mohsen
Ghassemi, Sriram Gopalakrishnan, Vikesh Gosai, Eleonora Kreačić, et al. 2023. Synthetic data applications in finance.
arXiv preprint arXiv:2401.00081(2023).
[40] Matteo Prata, Giuseppe Masi, Leonardo Berti, Viviana Arrigoni, Andrea Coletta, Irene Cannistraci, Svitlana Vyetrenko,
Paola Velardi, and Novella Bartolini. 2024. Lob-based deep learning models for stock price trend prediction: a benchmark
study.Artificial Intelligence Review57, 5 (2024), 116.
[41] Ali Seyfi, Jean-Francois Rajotte, and Raymond Ng. 2022. Generating multivariate time series with COmmon Source
CoordInated GAN (COSCI-GAN).Advances in neural information processing systems35 (2022), 32777–32788.
[42] Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli. 2015. Deep unsupervised learning
using nonequilibrium thermodynamics. InInternational conference on machine learning. pmlr, 2256–2265.
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.

High-Quality Synthetic Financial Time-Series using a GAN–Diffusion Framework 111:23
[43] Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. 2020. Score-
based generative modeling through stochastic differential equations.arXiv preprint arXiv:2011.13456(2020).
[44] Shuntaro Takahashi, Yu Chen, and Kumiko Tanaka-Ishii. 2019. Modeling financial time-series with generative
adversarial networks.Physica A: Statistical Mechanics and its Applications527 (2019), 121261.
[45] Yuki Tanaka, Ryuji Hashimoto, Takehiro Takayanagi, Zhe Piao, Yuri Murayama, and Kiyoshi Izumi. 2025. CoFinDiff:
Controllable Financial Diffusion Model for Time Series Generation.arXiv preprint arXiv:2503.04164(2025).
[46] Yusuke Tashiro, Jiaming Song, Yang Song, and Stefano Ermon. 2021. Csdi: Conditional score-based diffusion models
for probabilistic time series imputation.Advances in neural information processing systems34 (2021), 24804–24816.
[47] Milena Vuletić and Rama Cont. 2024. Volgan: a generative model for arbitrage-free implied volatility surfaces.Applied
Mathematical Finance31, 4 (2024), 203–238.
[48] Milena Vuletić, Felix Prenzel, and Mihai Cucuringu. 2023. Fin-gan: Forecasting and classifying financial time series via
generative adversarial networks.A vailable at SSRN 4328302(2023).
[49] Svitlana Vyetrenko, David Byrd, Nick Petosa, Mahmoud Mahfouz, Danial Dervovic, Manuela Veloso, and Tucker
Balch. 2020. Get real: Realism metrics for robust limit order book market simulations. InProceedings of the First ACM
International Conference on AI in Finance. 1–8.
[50] Magnus Wiese, Robert Knobloch, Ralf Korn, and Peter Kretschmer. 2020. Quant GANs: Deep Generation of Financial
Time Series.Quantitative Finance20, 9 (Sept. 2020), 1419–1440. doi:10.1080/14697688.2020.1730426
[51] Jinsung Yoon, Daniel Jarrett, and Mihaela Van der Schaar. 2019. Time-series generative adversarial networks.Advances
in neural information processing systems32.
[52] Xinyu Yuan and Yan Qiao. 2024. Diffusion-ts: Interpretable diffusion for general time series generation.arXiv preprint
arXiv:2403.01742(2024).
Received 20 February 2007; revised 12 March 2009; accepted 5 June 2009
ACM J. Data Inform. Quality, Vol. 37, No. 4, Article 111. Publication date: August 2018.
