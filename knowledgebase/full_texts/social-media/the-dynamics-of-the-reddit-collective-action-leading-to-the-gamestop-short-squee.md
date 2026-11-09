---
title: The dynamics of the Reddit collective action leading to the GameStop short squeeze
url: https://arxiv.org/abs/2401.14999
category: social-media
subcategory: empirical
date: 2024-01
venue: ''
authors:
- Antonio Desiderio
- Luca Maria Aiello
- Giulio Cimini
- Laura Alessandretti
source: arxiv
pdf_url: https://arxiv.org/pdf/2401.14999
pages: 49
chars: 102217
fetched_at: '2026-11-08T13:07:15+00:00'
kb_version: 1
---

# The dynamics of the Reddit collective action leading to the GameStop short squeeze

The dynamics of the Reddit collective action
leading to the GameStop short squeeze
Antonio Desiderioa,b,c*, Luca Maria Aiellod,e, Giulio Ciminia,b,+,
Laura Alessandrettic,+
aPhysics Department and INFN, University of Rome Tor Vergata, Via
della Ricerca Scientifica, 1, 00133, Rome, Italy.
bCentro Ricerche Enrico Fermi, Via Panisperna, 89a, 00184, Rome, Italy.
cDepartment of Applied Mathematics and Computer Science, Technical
University of Denmark, Richard Petersens Plads, 2800, Copenhagen,
Denmark.
dComputer Science Department, IT University of Copenhagen, Rued
Langgaards Vej 7, 2300, Copenhagen, Denmark.
ePioneer Centre for AI, Øster Voldgade 3, 2100, Copenhagen, Denmark.
∗To whom correspondence should be addressed: antde@dtu.dk.
+These authors jointly supervised the work.
Abstract
In early 2021, the stock prices of GameStop, AMC, Nokia and BlackBerry expe-
rienced dramatic increases, triggered by short squeeze operations that have been
largely attributed to Reddit’s retail investors. Here we shed light on the extent and
timing of Reddit users’ influence on the GameStop short squeeze. Using statisti-
cal analysis tools with high temporal resolution, we find that increasing Reddit
discussions anticipated high trading volumes. This effect emerged abruptly a few
weeks before the event but waned once the community gained widespread visi-
bility through Twitter. Meanwhile, the collective investment of the community,
quantified through posts of individual positions, closely mirrored the market cap-
italization of the stock. This evidence suggests a coordinated action of users in
developing a shared financial strategy through social media – targeting GameStop
first and other stocks afterwards. Overall, our results provide novel insights into
the role of Reddit users in the dynamics of the GameStop short squeeze.
1
arXiv:2401.14999v4  [physics.soc-ph]  3 Feb 2025

1 Introduction
From swinging elections to fueling social movements, instantaneous global commu-
nication enabled by online social media can shape leading global phenomena [1–5].
Financial markets represent a key area where the activity of social media users can
have destabilizing effects with worldwide resonance [6]. Indeed, there is ample evidence
that user activity on mainstream platforms like Twitter [7, 8] and Google Search [9]
not only mirror the mood of the market but can at times anticipate the evolution
of stock prices [7, 9–13]. This goes along with the increasingly central role played by
retail investors, or non-professional investors, in a sector that was once dominated by
institutional funds and large corporations [14–16].
The dissemination of knowledge on social media stems directly from the dynamic
interactions of users [17], who actively share knowledge and opinions on financial
markets[18]. Thus, this medium has the potential to enhance the discovery of infor-
mation that underlies price formation in financial markets [19]. Social communication,
indeed, supports the price-discovery process [20] and improves market efficiency, when
information is exogenous [21]. However, more than rational agents, social media users
tend to resemble noisy traders [22], suggesting that standard models of efficient mar-
kets should account for behavioral factors, such as investors’ sentiment, public mood
[23], cultural traits, psychological biases, social network structure, and information
asymmetries [24] as influential for price formation. What emerges from this picture
is the complex and evolving interplay between social media signals and stock market
trends, which enables narratives, ideas, and investment strategies to rapidly spread
to a wide audience [25, 26]. Notably, this relationship mainly emerges around specific
events, for example when surges in online interactions catalyze trading activity or,
conversely, when large price variations spark online conversation [27]. As such, social
media signals tend to capture well transient market trends and stock-specific swings
[28].
In early 2021, financial markets were shaken by an unprecedented event: the stock
of video-game retail company GameStop (GME) experienced a “short squeeze”, with a
price surge of almost 1625% within a week [29]. This financial operation was attributed
to activity from users of the social media platform Reddit, particularly the subreddit
WallStreetBets (WSB), and was rapidly followed by similar market rallies for other
stocks: BlackBerry (BB), AMC Entertainment Holdings (AMC) and Nokia (NOK).
The GME short squeeze suggested that retail investors, by sharing their investment
strategies on social media, could potentially challenge the influence of large institu-
tional funds [29]. The Reddit platform could have supported coordination by fostering
community-driven discussions [26, 30–32] focused on shared interests and collective
goals. On the contrary, mainstream social media like Twitter are primarily used as
news feeds [33], and facilitate coordination only to a limited extent through the use
of hashtags [4, 34].
The GME short squeeze has been extensively analyzed in the scientific literature.
Several studies reported a strong correlation between the activity on WSB and the
evolution of the GME price throughout the event [26, 30, 35–38]. However, two major
questions remain unanswered regarding the role of WSB users. Firstly, it is still unclear
if – and from which specific moment – the activity of WSB users anticipated the actual
2

GME price surge. Secondly, it is unclear if WSB served merely as a platform for finan-
cial discourse or as a hub to coordinate a common investment strategy. In this work,
we study the temporal relation among three key signals in the period around the GME
event: the stock market movements, the activity on WSB and the broader public atten-
tion to the stocks. We employ different techniques, from standard Granger Analysis
and Multivariate Vector Autoregressive Models to study linear effects, to Detrended
Cross-Correlation Analysis (DCCA) and Convergent Cross-Mapping (CCM) to cap-
ture the non-linear and complex character of the phenomenon. Our analysis provides
evidence in support of the hypothesis that activity on the WSB community forecast
the price surge of GME, BB, AMC and NOK. Further, we shed light on the tempo-
ral dynamics of the GME short squeeze, characterizing its evolution through three
distinct phases of online behavior: Discussion, Action, and Visibility.
2 Results
2.1 Reddit activity on GME mirrors changes of GME trading
volume.
We characterise the discourse during the GameStop saga using the volume of GME-
related activity on Reddit and on Twitter (see Supplementary Materials, Section 1),
the former reflecting the conversation within the community of WSB users and the
latter capturing the broader public attention to the stock. Following recent literature
[11, 26], we quantify these two signals by measuring the hourly occurrence of the GME
ticker in the text of posts and comments on Reddit and Twitter, respectively (see
Methods for more details). The GameStop saga is described by the series of events
reported in Table 1. Interest in GME within the WSB community began to surge as
early as December 2020 [26, 30]. However, despite this growing public discourse, the
hourly trading volume and price of GME did not exhibit a significant upward trend
until approximately 15 days before the short squeeze date of January 27th – which we
associated with Elon Musk’s tweet. As shown in Figure 1a, this trend closely resembles
the increase in GME-related conversation volume on social media.
This observation suggests a deeper connection between the two signals. To shed
light on this point, we employ detrended cross-correlation analysis (DCCA). This
method allows investigating cross-correlations between time series in the presence of
non-stationarity [39], hence addressing prevalent effects observed in financial time
series such as non-linearity, long-term underlying trends and long-range dependencies
[40]. Specifically, through DCCA, we gauge if fluctuations in GME-related activity are
correlated with fluctuations of GME market volume across multiple time scales [11]
(see Methods for further details). We apply DCCA to time series of absolute values
of hourly returns for GME occurrences, stock price and trading volume [39] from
December 1st, 2020 to July 1st, 2021, computing the detrended covariances for each
combination of signal pairs (see Methods). Results shown in Figure 1 b indicate that
such detrended covariances follow power-law scaling, pointing to long-term coupling
between the signals (see Supplementary Materials, Section 2). Remarkably, the GME
trading volume displays larger detrended covariance with Reddit activity than with
GME price, with a cross-correlation coefficient three times larger than the one observed
3

for the other pairs of signals (see Inset Figure 1 b). This suggests that changes in
trading volume are more tied to Reddit discussions, rather than to price movements.
We further employ Convergent Cross-Mapping (CCM) to corroborate the dynamic
interdependence between Reddit activity and trading volume [41]. This method quan-
tifies the non-linear coupling between variables by assessing whether past states of one
variable x can predict future states of another variable y, without assuming model-
specific dependencies. Results of this approach confirm a strong dynamic coupling
between Reddit activity and trading volume (see Supplementary Materials, Section
3). Overall, we can conclude that large variations in Reddit discussions are strongly
related to changes in trading volume, as more discussions correspond to a general
increase in buying activity and vice versa.
2.2 The collective position of WSB users on GME amounts to
at least 1% of the stock’s market capitalization.
In WSB, some users provide evidence of their financial investments by posting screen-
shots of their accounts taken from trading platforms, which attest their positions and
trading activity [30]. We analyse such screenshots to capture the actual engagement of
WSB users with the GME stock [11, 26], using computer vision techniques (see Meth-
ods for more details and Supplementary Materials, Section 4). We observe that the
values of the individual positions on GME follow a Log-normal distribution (see the
Inset of Figure 1 c). By summing the positions across all users, we obtain the posted
collective investment, which provides a lower-bound estimate of the community stake
in GME, as it includes only the retail investors who have publicly shared their posi-
tions. We find that this posted collective position grew significantly 15 days prior to
the squeeze. This finding complements the observation that the number of WSB users
posting screenshots grew in the period preceding the squeeze [30], likely indicating
that we have more users investing in GME. Notably, the growth of the posted col-
lective position closely follows the market capitalization of GME (see Figure 1 c). We
estimate that the posted collective investments of Reddit users represented – on aver-
age over the time period considered – at least the 1% of the total market capitalization
of GME (see Figure 1 c).
2.3 Granger analysis identifies three distinct phases of online
behavior.
We now test the hypothesis that changes in GME-related activity on social media
anticipated changes in GME trading volume around the short squeeze. Specifically, we
employ the Granger test to assess the chronological anticipation x → y: whether a sig-
nal x has predictive power on another signal y, building a linear regression model for
y(t) leveraging past information on both y and x from t − ∆t up to t − 1. The Granger
Index [42] quantifies the test result as the ratio of predictive accuracy between the
model and a baseline that excludes past information derived from x (see Methods for
more details). As x and y we consider the possible pairs of signals among GME trad-
ing volume and GME-related discussions on Reddit and Twitter. We consider hourly
values during market opening times, within a 15-day time window (corresponding to
4

120 points per time series – see Methods) between January 5 and February 5. This
choice of window size ensures that we capture short-term patterns that are relevant
to our case study [28] and at the same time that we have enough statistics to draw
robust conclusions from the Granger analyses, even in regimes of small coupling [43].
Results are, however, robust to different choices of window length (see Supplemen-
tary Materials, Section 5). After testing the stationarity of the time series within the
specified windows (see Supplementary Materials, Section 5), we apply a daily mov-
ing average (the results remain robust when we do not apply the moving average, see
Supplementary Materials, Section 5) and compute the hourly log returns of the signals.
Figure 2a shows the resulting Granger Index for ∆ t = 1, meaning that the model
uses x(t − 1) to predict y(t). In the plot, triangles correspond to statistical significant
values (p-values < 0.05). Size effects are instead captured by the coefficient of the
regression of the independent variable, reported in Figure 2b for the Reddit-to-Trading
Volume direction (see Supplementary Materials, Section 5 for other values). Results
highlight three distinct phases of online behavior (see Figure 2 a).
Phase 1.
Before January 13th, the Granger Index and size effects are not significantly different
from zero (p-values > 0.1) for all combinations of signals, meaning that no anticipatory
effects are observed.
Phase 2.
On January 13, the Granger Index capturing the anticipatory power of the Reddit
activity on trading volume has a sharp transition to a very high value of 0.47 (p-
values < 0.05). At the same time, size effects grow up to 1.5, meaning that social
media activity has a large positive effect in the prediction of market trends. Simulta-
neously, the predictive power of the trading volume on Reddit is significant; however,
the Granger Index in the Reddit-to-Trading Volume direction is roughly three times
larger than in the opposite Trading Volume-to-Reddit direction. These indices remain
significant – although steadily declining – for about 12 days. The p-values are reported
in Supplementary Materials, Section 5.
Phase 3.
On January 27th, the Tweet “Gamestonk!!” by Elon Musk brought the GME short
squeeze to the public attention. On this date, the anticipatory power of Reddit activ-
ity on the trading volume (and viceversa) is non significant, and size effects vanish.
Instead, Reddit activity starts to anticipate the activity on Twitter: once they became
informed about the short squeeze, Twitter users turned to Reddit for information
about GME.
The three phases identified above suggest the following sequence of events. Prior
to January 13th, WSB users were discussing about GME but did not play a significant
role in the market. Afterwards, from January 13th to 27th, their coordinated action of
buying and holding GME shares began to influence the market. Finally, after January
27th, the operation gained public attention, the market was influenced by a much
5

broader audience and other market players – eclipsing the role of WSB users. At
the same time, a larger horde of people joined the WSB community, fundamentally
altering the nature of discussions [26, 30]. To reflect their distinct nature, in the
following, we refer to these three phases as the Discussion, Action, and Visibility
phases, respectively.
Reinforcing effects among Reddit, Twitter and Trading Volume.
The analysis in the previous section considers only pairwise relations among signals.
In order to capture how the mutual relationship between all three signals under study
change over time, we employ a Multivariate Vector Autoregressive model. The method
generalises the Granger analysis to multiple signals: it entails fitting a linear model
that predicts a target output signal y at time t, using past information from t − 1 to
t−∆t on y itself plus one or more input feature signals{x1, x2, x3, . . .}. The coefficients
of the model capture how the individual input signals contribute to predicting future
values of y (see Methods for more details). In particular, a positive coefficient for xi
indicates a positive reinforcing relationship of xi on y, while a negative coefficient
an opposite and counteracting effect. We apply the method to study the hourly log-
returns of Twitter activity, Reddit activity, and trading volume. As we did for the
Granger analysys, we fitted the model within each 15-day period ending on a day
between January 5th and February 5th, for ∆ t = 1 (results for other window period
lengths are reported in the Supplementary Materials, Section 5).
Figure 2 c shows the coefficients that capture the predictive power of the three
signals on the future values of Twitter (top plot), Reddit (mid plot), and trading
volume (bottom plot). First, we observe a self-reinforcing dynamic within Reddit and
Twitter throughout the whole period under study, where increased activity within
the social network leads to further increases. This is evident from the consistently
positive and significant coefficients of the Reddit-to-Reddit and Twitter-to-Twitter
relation. During the Action phase, the self-reinforcing nature of Reddit is even more
pronounced.
Secondly, during the Action phase, the coefficient capturing the Reddit-to-Trading
Volume relation is significant and positive, implying that the increase of activity on
Reddit is followed – within the next hour – by an increase in trading volume. This is
coherent with the size effects observed in the Granger analysis. Notably, in this phase
the magnitude of the Reddit-to-Trading Volume coefficient is similar to the magnitude
of the Reddit-to-Reddit coefficient (the two can be directly compared since we are
considering the log-returns of the signals).
Finally, during the Visibility phase, the trading volume starts following a self-
reinforcing dynamics (as indicated by the significant and positive coefficient for
the Trading Volume-to-Trading Volume relation), while the Reddit-to-Trading Vol-
ume coefficient is non significant. In this phase, the Reddit-to-Twitter coefficient
aligns in both magnitude and direction with the Twitter-to-Twitter coefficient, again
highlighting that public attention was directed towards WSB.
By conducting this analysis at various lags ∆ t, we found that the coefficients
at ∆ t = 1 hour are larger than the others (see Supplementary Materials, Section
5), indicating the greater significance of short time scales in the entwined dynamics
6

of social media and markets. Interestingly, the typical reply speed, defined as the
average time interval between a comment and its direct responses, varies between∼ 2.5
hours during the Discussion phase to ∼ 0.5 hours during the Visibility phase (see
Supplementary Materials, Section 6). Hence, the influence of Reddit on the market
occurs on a timescale closely aligned with that of the unfolding conversations.
The role of WSB users on other short squeezes.
Alongside GME, also BB, AMC, and NOK experienced a short squeeze in January-
February 2021. In this section, we investigate the interplay between discussions on
WBS and these financial events, employing the techniques introduced in the previous
sections. Our analysis focuses on the occurrences of the BB, AMC and NOK tickers
on WSB posts and comments, against the trading volumes of the respective stocks.
By the end of 2020, BB, AMC and NOK ranked below position 10 among the
stocks that were most discussed on WSB, while Palantir (PLTR), Tesla (TSLA) and
NIO Inc. (NIO) occupied the top ranks together with GME (see Figure 3a, top panel).
Interestingly, during the GME Action phase, we observe a fast ramp up of BB, AMC
and NOK which – by mid January 2021 – became the most discussed stocks, just
below GME.
The Granger analysis reveals that, during the GME Action phase, the Reddit-
to-Trading Volume anticipatory relation is only significant for BB (see Figure 3 b).
Interestingly, the Granger Index for BB is statistically significant only five days
after it does so for GME. The analysis for AMC and NOK, instead, does not lead
to significant conclusions (see Supplementary Materials, Section 5), possibly due to
the less attention they received on Reddit (see Figure 3 a). We refer the reader to
the Supplementary Materials, Section 2 for the analyses of long-range detrended
cross-correlations (DCCA) and Convergent Cross-Mapping (Supplementary Materi-
als, Section 3) between trading volume and the frequency of occurrences for BB, AMC
and NOK.
We now consider the Multivariate Autoregression analysis of BB (see Supplemen-
tary Materials, Section 5 for the analysis of NOK and AMC). As Figure 3 c shows, we
find that the Reddit-to-Trading Volume anticipatory effect is reinforcing, as demon-
strated by a significant and positive model coefficient. We observe, however, a different
behaviour compared to the GME case. At the beginning of the Action phase, the
Trading Volume has a positive reinforcing effect on both Reddit and itself; at the same
time, Trading Volume is much better predicted by itself than by Reddit. This trend
reverses one week later, when Trading Volume loses all its explanatory power, while
Reddit enters into a positive relationship with itself and Trading Volume.
But how do BB, AMC and NOK gained popularity among WSB users ? To study
this phenomenon, we compute the overlap coefficient (size of the intersection over size
of the smaller set) and Jaccard index (size of the intersection over size of the union)
among the set of users who talk about GME and those who talk about other stocks (see
Figure 3d and 3e). On January 13th, concurrently with the beginning of the Action
phase, we observe a sharp increase in the overlap between users discussing GME and
other stocks. After January 13th, the overlap index has a plateau at a high value close
to 0 .8, signaling an expansion of discussions among WSB users. Initially focused on
7

GME, they broadened their conversations to include various other stocks. By studying
the Jaccard index, we notice that up to 40% of users interested in GME focused initially
also on BB; then, as the short squeeze approached, they turned to NOK and AMC.
During the same period, the number of users endorsing stocks that were top ranked
before December (PLTR, TSLA, NIO) decreased. When we compute these indices, the
group of users who talk about the other stock (not GME) is always smaller, while the
larger group is mostly made up of users discussing GME (see Supplementary Materials,
Section 7). Additional analyses based on the raw number of users discussing the various
stocks show that, prior to the start of the GME rally, users stopped discussing NIO,
and during the rally started focusing on BB, NOK and AMC (see Supplementary
Materials, Section 7). Simultaneously, mega-threads dedicated to GME appear on
WSB [26, 44], providing additional visibility to other stocks that GME users were also
talking about.
These findings suggest that WSB users engaged with GME also endorsed BB,
AMC and NOK. Approaching the GME short squeeze, and concurrently with the
widespread recognition of WSB on a global level, these stocks emerged as the most
popular choices and ended up as short squeeze targets.
3 Discussion
In January 2021, the activity of WSB users anticipated financial trends. The high
temporal resolution of our analysis enabled us to identify three distinct phases of online
behavior and engagement with the stock market, characterized by Discussion, Action
and Visibility, respectively. First, we observed that the strong anticipatory relation
between WSB users activity and changes in GME trading volume emerged sharply
on January 13th. This suggests a sudden transition between a phase characterized
by Discussion and one characterized by financial Action. Second, we found that –
at around the same time – the value of the collective position on GME started to
closely mirror the evolution of the market capitalization of GME. We estimated that
the size of the total position of WSB users amounted to at least 1% of GME market
capitalization, demonstrating a tangible engagement of the WSB community in the
stock market. This suggests that other market players joined the short squeeze after
it was initiated by WSB users, despite having access to information about GME that
was presumably not inferior to that of the WSB users [45]. After the price hike of
GME and a Tweet by Elon Musk on January 27th, the short squeeze became widely
known, and a broader public started to follow Reddit conversations.
Our study comes with limitations. First, our findings refer to a specific case study,
the GME short squeeze, which so far represents a unique event due to its wide res-
onance. If and when such events will occur again, we could understand whether the
patterns we have observed can be generalized to different contexts. Secondly, our
analysis primarily relies on Granger test, a standard statistical framework that relies
on linear models. As such, it may oversimplify complex relationships, such as those
involved in collective action between social networks and financial markets, where
feedback loops and non-linear dynamics can occur. Recognizing this limitation, we
8

have explored nonlinear techniques; notably, an analysis based on Convergent Cross-
Mapping [41] corroborates our main results (see Supplementary Materials, Section 3).
Third, due to limitation of the available data, our analysis focused solely on Reddit and
Twitter, neglecting offline interactions or happening on other online platforms ( e.g.,
Telegram or Discord), as well as the online/offline actions of institutional investors.
Finally, the proxy used to estimate the size of WSB collective position on GME,
specifically from user screenshots, are inherently partial and noisy. We also have no
information on the identities of the investors behind the screenshots, so we cannot
exclude the potential interference by institutional investors in the financial discourse
on Reddit.
Despite such limitations, we have provided extensive evidence regarding the pos-
sible influence exerted by Reddit users on the GameStop short squeeze. However,
determining a genuine causal link – that Reddit users directly fueled the price rally
– is not possible with the data we can access. Factors such as the true portfolio com-
position of each Reddit user and the potential psychological contagion within Reddit
discussions add uncertainty for the attribution of direct causation.
Overall, our results add further evidence that digital platforms can catalyze col-
lective action and influence real-world outcomes. In an era characterized by rapid
technological advancements, the pace of our daily lives is accelerated to an unprece-
dented rate [46]. This phenomenon has also impacted the financial landscape, where
the emergence of commission-free trading platforms started a new age of dynamism
and accessibility [29]. Our findings highlight the importance of investigating the
dynamic interplay between online engagement and stock market movements at an
hourly scale (or even finer) [7, 9–11], as the coordinated action of retail traders through
social media has become a no-longer-negligible market player.
4 Methods
4.1 Data Descriptions
We gathered Reddit conversation data from Pushshift [47], an API that regularly
copies activity data of Reddit. We queried the service to retrieve information about
posts and comments on WSB from December 01, 2020 to July 1, 2021. The dataset was
cleaned by removing posts/comments by Reddit bots (see Supplementary Materials,
Section 1) as well as by ”[deleted]” users, who deleted their account at the time
Pushshift API collected data. To obtain the occurrences of a given stock within WSB
conversations, we counted how many times the ticker symbol of the stock (e.g., ‘NOK’
for Nokia) appears as a regular expression in the raw text of a post/comment [26].
Within the WSB community, a common practice consists in posting financial
investments by sharing screenshots of open positions, primarily gains, losses, or orders.
These “committed” screenshots were identified and classified using computer vision
techniques by Lucchini et al.[30]. Using Tesseract, an open-source optical character
recognition [48], we extract textual information from these screenshots, converting
image-based text into editable and searchable content. We focused on screenshots con-
taining keywords such as ‘gme,’ ‘gamestop,’ ‘investing,’ and ‘value,’ identified through
manual inspection, and subsequently narrowed down the sample to 6525 screenshots
9

from November 1, 2020 to February 04, 2021. After parsing the structures, we isolated
dollar-sign-prefixed numbers, determining the final value of the position as the high-
est extracted value. However, such value may represent trading volume or the price
of GME taken from online trading applications, rather than an actually investment.
To address this, we filtered out screenshots with values below 10 2 and above 10 6, as
these are likely indicative of price or trading volume. We manually examined values
above 106 to validate our findings. Additionally, we manually validated 1000 screen-
shots using log-transformed data, computing the logarithms of the ratios between true
and estimated values. We determined that our procedure extracts the correct value
with an accuracy of 0.85, where accuracy is based on a binary classifier where correct-
ness is determined by applying a threshold of 0.05 to the absolute logarithmic ratios
(see Supplementary Materials, Section 4). The root mean square error (RMSE) of the
logarithmic ratios between true and estimated values is 0.47, and the point estimate
(i.e., the average ratio for a single screenshot) amounts to -0.07. This indicates that
the automated predictions slightly overestimate the actual values (on average +17%).
However, this difference is more pronounced at screenshot values below 10 3, with a
relative logarithmic error of -0.1, while it approaches zero at higher values. Overall the
automated extraction procedure leads to a total discrepancy of approximately +0.2%
in the WSB posted collective position. Note that this validation was intended solely to
assess the error of the employed framework in estimating the collective financial posi-
tion – the incorrect estimates were not replaced. Indeed, missing posts, and possibly
fake ones, represent a much larger source of error, which we cannot control.
We measured Twitter interest towards GME using Twitter API for academic
research. From this service, we collected tweets with the #GME or #Gamestop hash-
tags posted between December 1, 2020 and February 5, 2021 [30]. Data on stock close
price and traded volumes were retrieved from the API service of https://polygon.io.
Data on stock close price and traded volumes were retrieved from the API ser-
vice of https://polygon.io, wherein the price data reflects stock split adjustments
that occurred during the stock split in 2022. All signals were taken into account
exclusively during market hours (9 a.m. to 5 p.m.). When analyzing the changes
of a particular signal, denoted as x(t), we compute its hourly logarithmic return as
r(t) = ln[x(t + 1)/x(t)].
4.2 Detrended Cross-Correlation Analysis
Detrended Cross-Correlation Analysis is a statistical technique designed to explore
long-range dependencies between two time series, by studying how the fluctuations of
local trends evolve across temporal scales [39, 49]. The underlying idea is to decompose
two signals into smaller overlapping segments using a given time window, compute the
covariance between the two detrended signals within each segment, average the results
obtained over the various segments, and finally repeat all the steps for windows of
different lengths to assess potential scale relations. Following Podobnik et al.[49], we
consider two time series x(τ ) and y(τ ) of equal length T and compute the integrated
signals I (x)(t) = Pt τ =1 x(τ ) of each time series. For the analysis at window length t,
we divide the signals into T − t consecutive segments (window t), each containing t + 1
values. In each segment that starts at i and ends at i + t, we define the local trend
10

as the ordinate of a linear least-squares fit S(x) i (t) and remove it from the integrated
windowed signal I (x) i (t) to compute the residuals. We define the covariance of the
residuals in each segment as
fDCOV (i, t) = 1 t − 1
t+iX
τ =i
(I (x)(τ ) − S(x) i (τ ))(I (y)(τ ) − S(y) i (τ )) , (1)
and if x = y we have the variance of the residuals f 2 DV AR(i, t). Then, the detrended
covariance F (x,y) DCOV (t) is defined as the average covariance of the residuals over the
overlapping segments at the given window t: F (x,y) DCOV (t) = 1 T −t PT −t j=1 fDCOV (j, t). In
our case, the time series have temporal length T ∼ 103 and the windows considered
are logarithmically spaced, each containing 30 points. The detrended cross-correlations
coefficient is finally defined as
FDCCA (t) = F (x,y) DCOV (t)q
F (x,x) DV AR(t) q F (y,y) DV AR(t) . (2)
If two series are power-law cross-correlated, then the detrended covariance as a func-
tion of the window length t follows a power law, F (x,y) DCOV (t) ∼ tλ and the magnitude of
FDCCA indicates the correlation strength [49]. The exponent λ identifies whether this
cross-correlation is short-range (λ = 0.5) or long-range (λ >0.5). If two time series are
short-range correlated or cross-correlations is absent, FDCCA could be non zero and
slightly be dependent on window t due to size effects [49]. To identify statistically sig-
nificant values, we compare the obtained cross-correlations against those obtained for
two independent random signals (see Inset Figure 1 c, gray area)[49]. In our case, we
observe values of cross-correlation always exceeding the confidence interval, and scal-
ing exponents λ > 0.5, pointing to power-law cross-correlations (see Supplementary
Materials, Section 2). However, it is crucial to interpret the fitting of the exponents
as an exercise due to the limitation of short time series. We further corroborate our
findings by estimating the Hurst exponent through R/S analysis (see Supplementary
Materials, Section 2).
4.3 Granger test and Multivariate Vector Autoregressive
Model
The Granger test is commonly used in time series analysis to determine whether the
predictability of y(t) in a given model decreases when the time series x(t) is excluded
from that model [10]. The key idea is that when both past values of x and y are
incorporated rather than just past values of y, the prediction of y improves, thus
indicating that x Granger-causes y. In our case, we consider a vector autoregressive
11

model of order ∆ t
yt = ea0 +
∆tX
l=1
ealyt−l + eϵt and
yt = ba0 +
∆tX
l=1
balyt−l +
∆tX
l=1
bblxt−l + bϵt , (3)
where the first equation is the restricted model and the second the full model. After
fitting these models, the p-values are computed from the F-statistic, which reflects
the difference in the residual sum of squares ( RSS ). These p-values indicate the likeli-
hood of obtaining results as extreme as the observed F-statistic under the assumption
that the restricted model is correct. Size effects are given by the values of the regres-
sion coefficients bal and bbl, which capture the contribution of the lagged variables
y and x in predicting y. The Granger Index, on the other hand, focuses only on
the predictive accuracy of the full model in relation to the restricted model, defined
as GI = ln( RSSrestricted/RSSf ull). To conduct the Granger test, we need first to
evaluate the stationarity of signals within the specified windows. The results of the
Augmented Dickey-Fuller test are reported in Supplementary Materials, Section 5.
Following the full model of the Granger test, we consider a Multivariate Vector
Autoregressive model to analyze relationships and dependencies among two or more
time series simultaneously. The significance of a particular regression coefficient is
established by evaluating its corresponding p-value, computed similarly to the Granger
analysis. Both for Granger and Multivariate Vector Autoregressive Model, we analyzed
the data by sliding it within 15-day windows, shifting by one day each time. The
resulting length of the time series is thus of 120 points (8 hourly points per day) – a
reasonable statistics to perform linear regression analysis [43, 50, 51].
Declarations
• Data Availability: Reddit conversation data used in this study (the same used
by Mancini et al.[26] and Lucchini et al.[30]) can be retrieved from the Pushshift
API at https://www.reddit.com/r/pushshift/ and were collected in December 2022.
Twitter data used in this analysis are the same used by Lucchini et al.[30], and
were retrieved from Twitter API before April 2022. Stock market data used in this
analysis can be retrieved from the Polygon.io API at https://polygon.io and were
collected in December 2022, while the GME Market Capitalization was collected in
September 2023.
• Code Availability: The data and code to reproduce the analysis is released on
GitHub. For inquiries, please contact A.D. antde@dtu.dk.
• Acknowledgements A.D. acknowledges the helpful discussions on Twitter and
screenshot data analysis with Lorenzo Lucchini. A.D. acknowledges the helpful dis-
cussions on Reddit conversations analysis with Riccardo Di Clemente, Anna Mancini
and Gabriele Di Antonio. A.D. acknowledges Danish Data Science Academy for
12

their funding support (”Grant ID DDSA-V-2023-008”). L.M.A. acknowledges sup-
port from the Carlsberg Foundation through the COCOONS project (CF21-0432).
G.C. acknowledges support from “Deep ’N Rec” Progetto di Ricerca di Ateneo of
University of Rome Tor Vergata.
• Author Contributions: A.D. and L.M.A gathered the data. A.D. performed the anal-
ysis and made the figures. L.A. and G.C designed the analysis and supervised the
project. All authors discussed the results and contributed to the final manuscript.
• Competing Interests: The authors declare no competing interests
References
[1] Heidemann, J., Klier, M., Probst, F.: Online social networks: A survey of a global
phenomenon. Computer Networks 56(18), 3866–3878 (2012) https://doi.org/10.
1016/j.comnet.2012.08.009
[2] Aral, S., Dellarocas, C., Godes, D.: Introduction to the Special Issue—Social
Media and Business Transformation: A Framework for Research. Information
Systems Research 24(1), 3–13 (2013) https://doi.org/10.1287/isre.1120.0470
[3] Halu, A., Zhao, K., Baronchelli, A., Bianconi, G.: Connect and win: The role of
social networks in political elections. EPL (Europhysics Letters) 102(1), 16002
(2013) https://doi.org/10.1209/0295-5075/102/16002
[4] Wolfsfeld, G., Segev, E., Sheafer, T.: Social Media and the Arab Spring: Politics
Comes First. The International Journal of Press/Politics 18(2), 115–137 (2013)
https://doi.org/10.1177/1940161212471716
[5] Del Vicario, M., Zollo, F., Caldarelli, G., Scala, A., Quattrociocchi, W.: Mapping
social dynamics on Facebook: The Brexit debate. Social Networks50, 6–16 (2017)
https://doi.org/10.1016/j.socnet.2017.02.002
[6] Bouchaud, J.-P., Farmer, J.D., Lillo, F.: How markets slowly digest changes in
supply and demand. Handbooks in Finance, 57–160 (2009) https://doi.org/10.
1016/B978-012374258-2.50006-3
[7] Bollen, J., Mao, H., Zeng, X.: Twitter mood predicts the stock market. Journal of
Computational Science 2(1) (2011) https://doi.org/10.1016/j.jocs.2010.12.007
[8] Oliveira, N., Cortez, P., Areal, N.: The impact of microblogging data for stock
market prediction: Using Twitter to predict returns, volatility, trading volume and
survey sentiment indices. Expert Systems with Applications 73, 125–144 (2017)
https://doi.org/10.1016/j.eswa.2016.12.036
[9] Moat, H.S., Curme, C., Avakian, A., Kenett, D.Y., Stanley, H.E., Preis, T.: Quan-
tifying Wikipedia Usage Patterns Before Stock Market Moves. Scientific Reports
3(1), 1801 (2013) https://doi.org/10.1038/srep01801
13

[10] Bordino, I., Battiston, S., Caldarelli, G., Cristelli, M., Ukkonen, A., Weber, I.:
Web Search Queries Can Predict Stock Market Volumes. PLoS ONE 7(7), 40014
(2012) https://doi.org/10.1371/journal.pone.0040014
[11] Curme, C., Preis, T., Stanley, H.E., Moat, H.S.: Quantifying the semantics
of search behavior before stock market moves. Proceedings of the National
Academy of Sciences 111(32), 11600–11605 (2014) https://doi.org/10.1073/pnas.
1324054111
[12] Souma, W., Vodenska, I., Aoyama, H.: Enhanced news sentiment analysis using
deep learning methods. Journal of Computational Social Science 2(1), 33–46
(2019) https://doi.org/10.1007/s42001-019-00035-x
[13] Souza, T.T.P., Aste, T.: Predicting future stock market structure by combining
social and financial network information. Physica A: Statistical Mechanics and its
Applications 535, 122343 (2019) https://doi.org/10.1016/j.physa.2019.122343
[14] Aramonte, S., Avalos, F.: The rising influence of retail investors. Technical report,
BIS Quarterly Review (March 2021). https://doi.org/https://www.bis.org/publ/
qtrpdf/r qt2103v.htm
[15] De Silva, T., Smith, K., So, E.C.: Losing is Optional: Retail Option Trading
and Earnings Announcement Volatility. SSRN Electronic Journal (2022) https:
//doi.org/10.2139/ssrn.4050165
[16] Van Der Beck, P., Jaunin, C.: The Equity Market Implications of the Retail
Investment Boom. SSRN Electronic Journal (2021) https://doi.org/10.2139/ssrn.
3776421
[17] Gonz´ alez-Bail´ on, S., Borge-Holthoefer, J., Rivero, A., Moreno, Y.: The Dynamics
of Protest Recruitment through an Online Network. Scientific Reports 1(1), 197
(2011) https://doi.org/10.1038/srep00197
[18] Lillo, F., Miccich` e, S., Tumminello, M., Piilo, J., Mantegna, R.N.: How news
affects the trading behaviour of different categories of investors in a financial
market. Quantitative Finance 15(2), 213–229 (2015) https://doi.org/10.1080/
14697688.2014.931593
[19] Goldstein, I.: Information in financial markets and its real effects 27(1), 1–32
https://doi.org/10.1093/rof/rfac052 . Accessed 2024-12-04
[20] Fan, R., Talavera, O., Tran, V.: Social media and price dis-
covery: The case of cross-listed firms. Journal of Financial
Research 46(1), 151–167 (2023) https://doi.org/10.1111/jfir.12310
https://onlinelibrary.wiley.com/doi/pdf/10.1111/jfir.12310
14

[21] Han, B., Yang, L.: Social networks, information acquisition, and asset prices. Man-
agement Science 59(6), 1444–1457 (2013) https://doi.org/10.1287/mnsc.1120.
1678 https://doi.org/10.1287/mnsc.1120.1678
[22] Tetlock, P.C.: Giving Content to Investor Sentiment: The Role of Media in the
Stock Market. The Journal of Finance 62(3), 1139–1168 (2007) https://doi.org/
10.1111/j.1540-6261.2007.01232.x
[23] Bukovina, J.: Social media big data and capital markets—an overview. Journal of
Behavioral and Experimental Finance 11, 18–26 (2016) https://doi.org/10.1016/
j.jbef.2016.06.002
[24] Ak¸ cay, E., Hirshleifer, D.: Social finance as cultural evolution, transmission bias,
and market dynamics. Proceedings of the National Academy of Sciences 118(26),
2015568118 (2021) https://doi.org/10.1073/pnas.2015568118
[25] RANTALA, V.: How do investment ideas spread through social
interaction? evidence from a ponzi scheme. The Journal of
Finance 74(5), 2349–2389 (2019) https://doi.org/10.1111/jofi.12822
https://onlinelibrary.wiley.com/doi/pdf/10.1111/jofi.12822
[26] Mancini, A., Desiderio, A., Di Clemente, R., Cimini, G.: Self-induced consensus
of Reddit users to characterise the GameStop short squeeze. Scientific Reports
12(1), 13780 (2022) https://doi.org/10.1038/s41598-022-17925-2
[27] Ranco, G., Aleksovski, D., Caldarelli, G., Grˇ car, M., Mozetiˇ c, I.: The Effects of
Twitter Sentiment on Stock Price Returns. PLOS ONE 10(9), 0138441 (2015)
https://doi.org/10.1371/journal.pone.0138441
[28] Vassallo, D., Bormetti, G., Lillo, F.: A tale of two sentiment scales: disentangling
short-run and long-run components in multivariate sentiment dynamics. Quanti-
tative Finance 22(12), 2237–2255 (2022) https://doi.org/10.1080/14697688.2022.
2119159
[29] Duterme, T.: Bloomberg and the GameStop saga: The fear of stock market democ-
racy. Economy and Society, 1–26 (2023) https://doi.org/10.1080/03085147.2023.
2189819
[30] Lucchini, L., Aiello, L.M., Alessandretti, L., De Francisci Morales, G., Starnini,
M., Baronchelli, A.: From Reddit to Wall Street: the role of committed minorities
in financial collective action. Royal Society Open Science 9(4), 211488 (2022)
https://doi.org/10.1098/rsos.211488
[31] Olson, R.S., Neal, Z.P.: Navigating the massive world of reddit: using backbone
networks to map user interests in social media. PeerJ Computer Science 1, 4
(2015) https://doi.org/10.7717/peerj-cs.4
15

[32] Centola, D., Becker, J., Brackbill, D., Baronchelli, A.: Experimental evidence for
tipping points in social convention. Science 360(6393), 1116–1119 (2018) https:
//doi.org/10.1126/science.aas8827
[33] Center, P.R.: The Behaviors and Attitudes of U.S. Adults
on Twitter. https://www.pewresearch.org/internet/2021/11/15/
the-behaviors-and-attitudes-of-u-s-adults-on-twitter/ (2021)
[34] Borge-Holthoefer, J., Perra, N., Gon¸ calves, B., Gonz´ alez-Bail´ on, S., Arenas, A.,
Moreno, Y., Vespignani, A.: The dynamics of information-driven coordination
phenomena: A transfer entropy analysis. Science Advances 2(4), 1501158 (2016)
https://doi.org/10.1126/sciadv.1501158
[35] Sornette, D., Lera, S.C., Lin, J., Wu, K.: Non-normal interactions create socio-
economic bubbles. Communications Physics 6(1), 261 (2023) https://doi.org/10.
1038/s42005-023-01379-7
[36] Ly´ ocsa,ˇS., Baum¨ ohl, E., V´ yrost, T.: YOLO trading: Riding with the herd during
the GameStop episode. Finance Research Letters 46, 102359 (2022) https://doi.
org/10.1016/j.frl.2021.102359
[37] Long, S.C., Lucey, B., Xie, Y., Yarovaya, L.: “I just like the stock”: The role of
Reddit sentiment in the GameStop share rally. Financial Review 58(1), 19–37
(2023) https://doi.org/10.1111/fire.12328
[38] Suchanek, M.: Social interactions in short squeeze scenarios. International Review
of Economics & Finance 91, 898–919 (2024) https://doi.org/10.1016/j.iref.2024.
01.062
[39] Podobnik, B., Horvatic, D., Petersen, A.M., Stanley, H.E.: Cross-correlations
between volume change and price change. Proceedings of the National Academy of
Sciences 106(52), 22079–22084 (2009) https://doi.org/10.1073/pnas.0911983106
[40] Mantegna, R.N., Stanley, H.E.: Introduction to Econophysics: Correlations and
Complexity in Finance, 1st edn. Cambridge University Press, Cambridge, UK
(1999). https://doi.org/10.1017/CBO9780511755767 . https://www.cambridge.
org/core/product/identifier/9780511755767/type/book
[41] Sugihara, G., May, R., Ye, H., Hsieh, C.-h., Deyle, E., Fogarty, M., Munch, S.:
Detecting Causality in Complex Ecosystems. Science 338(6106), 496–500 (2012)
https://doi.org/10.1126/science.1227079
[42] Geweke, J.F.: Measures of conditional linear dependence and feedback between
time series. Journal of the American Statistical Association 79(388), 907–915
(1984)
[43] Ramos, A., Macau, E.: Minimum sample size for reliable causal inference using
16

transfer entropy. Entropy 19(4), 150 (2017) https://doi.org/10.3390/e19040150
[44] Pei, S., Muchnik, L., Andrade, J.S., Zheng, Z., Makse, H.A.: Searching for super-
spreaders of information in real-world social media. Scientific Reports 4(1), 5547
(2014) https://doi.org/10.1038/srep05547
[45] Pelaez, A., R. Winston, E., Samuel, J.: David and Goliath revisited: How small
investors are changing the landscape of financial markets. In: Northeast Decision
Sciences Institute, pp. 287–292 (2021). https://doi.org/10.7282/00000176
[46] Lorenz-Spreen, P., Mønsted, B.M., H¨ ovel, P., Lehmann, S.: Accelerating dynamics
of collective attention. Nature Communications 10(1), 1759 (2019) https://doi.
org/10.1038/s41467-019-09311-w
[47] Baumgartner, J., Zannettou, S., Keegan, B., Squire, M., Blackburn, J.: The
Pushshift Reddit Dataset. Proceedings of the International AAAI Conference on
Web and Social Media 14, 830–839 (2020) https://doi.org/10.1609/icwsm.v14i1.
7347
[48] Smith, R.: An overview of the tesseract ocr engine. In: 2007 9th International
Conference on Document Analysis and Recognition, vol. 2, pp. 629–633. IEEE
Computer Society, Los Alamitos, CA, USA (2007). https://doi.org/10.1109/
ICDAR.2007.56 . https://doi.ieeecomputersociety.org/10.1109/ICDAR.2007.56
[49] Podobnik, B., Jiang, Z.-Q., Zhou, W.-X., Stanley, H.E.: Statistical tests for power-
law cross-correlated processes. Physical Review E 84(6), 066118 (2011) https:
//doi.org/10.1103/PhysRevE.84.066118
[50] Austin, P.C., Steyerberg, E.W.: The number of subjects per variable required in
linear regression analyses. Journal of Clinical Epidemiology68(6), 627–636 (2015)
https://doi.org/10.1016/j.jclinepi.2014.12.014
[51] Box, G.E.P., Jenkins, G.M., Reinsel, G.C.: Time Series Analysis, 1st edn. Wiley
Series in Probability and Statistics. Wiley, Hoboken, NJ (2008). https://doi.org/
10.1002/9781118619193
[52] Carbone, A., Castelli, G., Stanley, H.E.: Time-dependent Hurst exponent in finan-
cial time series. Physica A: Statistical Mechanics and its Applications 344(1-2),
267–271 (2004) https://doi.org/10.1016/j.physa.2004.06.130
[53] Runge, J., Nowack, P., Kretschmer, M., Flaxman, S., Sejdinovic, D.: Detecting
and quantifying causal associations in large nonlinear time series datasets. Science
Advances 5(11), 4996 (2019) https://doi.org/10.1126/sciadv.aau4996
[54] Bradley, E., Kantz, H.: Nonlinear time-series analysis revisited. Chaos: An Inter-
disciplinary Journal of Nonlinear Science 25(9), 097610 (2015) https://doi.org/
10.1063/1.4917289
17

[55] Takens, F.: On the numerical determination of the dimension of an attractor.
In: Braaksma, B.L.J., Broer, H.W., Takens, F. (eds.) Dynamical Systems and
Bifurcations vol. 1125, pp. 99–106. Springer, Berlin, Heidelberg (1985). https://
doi.org/10.1007/BFb0075637 . Series Title: Lecture Notes in Mathematics. http:
//link.springer.com/10.1007/BFb0075637
[56] Sugihara, G., May, R.M.: Nonlinear forecasting as a way of distinguishing chaos
from measurement error in time series. Nature 344(6268), 734–741 (1990) https:
//doi.org/10.1038/344734a0
[57] Takens, F.: Detecting strange attractors in turbulence. In: Rand, D., Young, L.-
S. (eds.) Dynamical Systems and Turbulence, Warwick 1980 vol. 898, pp. 366–
381. Springer, Berlin, Heidelberg (1981). https://doi.org/10.1007/BFb0091924 .
Series Title: Lecture Notes in Mathematics. http://link.springer.com/10.1007/
BFb0091924
[58] Cao, L.: Practical method for determining the minimum embedding dimension
of a scalar time series. Physica D: Nonlinear Phenomena 110(1-2), 43–50 (1997)
https://doi.org/10.1016/S0167-2789(97)00118-8
[59] Camps-Valls, G., Gerhardus, A., Ninad, U., Varando, G., Martius, G., Balaguer-
Ballester, E., Vinuesa, R., Diaz, E., Zanna, L., Runge, J.: Discovering Causal
Relations and Equations from Data. arXiv (2023) https://doi.org/10.48550/
ARXIV.2305.13341 . Publisher: arXiv Version Number: 1
[60] Stavroglou, S.K., Pantelous, A.A., Stanley, H.E., Zuev, K.M.: Hidden interactions
in financial markets. Proceedings of the National Academy of Sciences 116(22),
10646–10651 (2019) https://doi.org/10.1073/pnas.1819449116
[61] Luo, M., Kantz, H., Lau, N.-C., Huang, W., Zhou, Y.: Questionable dynamical
evidence for causality between galactic cosmic rays and interannual variation in
global temperature. Proceedings of the National Academy of Sciences 112(34)
(2015) https://doi.org/10.1073/pnas.1510571112
18

Date Event Description
2020-12-08 GME Q3 Earnings Reports GameStop’s Q3 earnings highlighted a significant
257% surge in e-commerce revenues.
2021-01-11 New Board of Directors GameStop revealed a new Board of Directors,
including several experts in e-commerce, signaling
a new leadership direction.
2021-01-13 GME Stock Rise Begins GME stock price started rising significantly,
increasing by around 60% in a single day.
2021-01-19 Citron Tweet Citron Research criticized GameStop’s stock valu-
ation and forecasted a price drop, belittling GME
buyers on Twitter.
2021-01-22 BB Stock Surge BlackBerry stock surged by 30%.
2021-01-27 Elon Musk Tweet Elon Musk tweeted, “Gamestonk!” with a link to
the subreddit r/WallStreetBets. GME stock surged
over 135%.
2021-01-28 Robinhood Trading Restrictions Robinhood and other brokerage platforms
restricted the buying of GME, AMC, BB, and
NOK stocks, leading to a temporary price crash.
AMC stock rose by 300%, BlackBerry by 32%,
and Nokia stocks surged by 30%.
T able 1 Major events relevant to the GameStop (GME) short squeeze and the subreddit
r/WallStreetBets (WSB).
19

b
Window
Detrended Covariance / Variance
Price - Trading V.
Price - Reddit
Trading V. - Reddit
Trading V. - Trading V.
Price - Price
Reddit - Reddit
1
10-1
10-2
10-3
10-4
10-5
10-6
101 102
Window
0 20 40 60 80 100
0.0
0.2
0.4
0.6
0.8
1.0DCCA
c
01 Dec 15 Dec 01 Jan 15 Jan 01 Feb
WSB Collective Position on GME (USD)
WSB Position Market Capitalization
Market Capitalization of GME (USD)
109
108
107
1011
1010
109
Individual Position (USD)
102 104 106
10− 2
10− 4
10− 6
10− 8
10− 10
PDF
Fit LogNormal
108
102
10-3
10-2
10-1
100
101
100
10
1 Price (USD)
Normalized Volume
01 Dec 15 Dec 01 Jan 15 Jan 01 Feb
a RedditTwitter
 PriceTrading Volume
Fig. 1 The correlation between Reddit activity and GameStop market indicators. a)
Daily occurrences of the “GME” ticker in conversations on WSB (orange, y-right axis) and Twitter
(lightblue, y-right axis), along with the daily trading volume of the GME stock (blue, right y-axis) and
its daily closing price (green, left y-axis). The vertical gray dotted line marks January 13th, identified
as the WSB-led action’s start (see subsequent sections), while the dashed line marks January 27th,
when Elon Musk’s Tweet broadly publicized the action. To improve the chart’s clarity, we applied
a 5-day moving average to each signal and normalized the trading volume, Reddit and Twitter
signals by their mean (we remark these modifications are not employed in the analysis). b) Values
of detrended variance for price (green), trading volume (blue) and Reddit activity (red) signals, and
values of detrended covariance for the pairs price / trading volume (purple), price / Reddit activity
(pink), trading volume / Reddit activity (yellow), as a function of the time window considered. Inset:
Detrended Cross Correlation Coefficients for paired combinations of GME signals (same color schemes
of the main panel). The shaded gray area represents the 95% confidence interval for correlation values
obtained from pairs of independent signals. c) Daily value of the WSB posted collective position on
GME (orange, y-right axis) and GME Market Capitalization (blue, y-left axis). Inset: Distribution of
values of users’ individual position on GME (red) alongside the Log-Normal fit (grey line, µ = 4.96,
σ = 3.63).
20

a
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
0.0
0.1
0.2
0.3
0.4
0.5
Granger Index
c
Trading V. Model
-2.0
-1.5
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
 Reddit
 Trading VolumeTwitter
CoefficientCoefficientCoefficient
Target: Reddit
Target: Twitter
Target: Trading V
Twitter ModelReddit Model
-2.0
-1.5
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
-2.0
-1.5
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb 05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
-2.0
-1.5
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
b
Trading V. --> Reddit
Reddit --> Trading V.
Trading V. --> Twitter
Reddit --> Twitter p < 0.05
p < 0.1
Reddit
 Trading Volume p < 0.05 p < 0.1
p < 0.05 p < 0.1
Fig. 2 Reddit activity anticipates trading volume during the short squeeze. In all the
following subplots the vertical gray dotted line indicates the beginning of the Action phase (13
January 2021), whereas the vertical gray dashed line corresponds to the Tweet by Elon Musk (27
January 2021) that brought the squeeze to the public attention. Triangles correspond to p-values
< 0.05, squares to p-values < 0.1. Each point is computed considering time series spanning the 15
preceding days. a) Granger Index capturing the predictive power of a signal on another (with a lag
of 1 hour) for the following pairs: Trading Volume-to-Reddit (blue), Reddit-to-Trading Volume (red),
Trading Volume-to-Twitter (gray) and Reddit-to-Twitter (yellow). b) Coefficients of the Granger
Model predicting Trading Volume, capturing the size effects of Reddit (magenta) and Trading Volume
(green) activities. c) Each panel shows the coefficients of a Multivariate Vector Autoregressive Model
predicting Twitter (top), Reddit (middle), and Trading Volume (bottom) activities, corresponding to
antecedent values of Reddit (solid orange), Twitter (dashed lightblue), and trading volume (dotted
blue).
21

a
-2.0
-1.5
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0Coefficient
Trading V. Model
Target: Trading V.
-2.0
-1.5
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
Reddit BB Trading Volume BB
Reddit Model
Target: Reddit
15 Dec22 Dec01 Jan08 Jan15 Jan22 Jan01 Feb08 Feb15 Feb
0.0
0.2
0.4
0.6
0.8
1.0
Overlap
GME-AMCGME-BB GME-NOK GME-NIOGME-PLTR GME-TSLA
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8Jaccard
GME-AMCGME-BB GME-NOK GME-NIOGME-PLTR GME-TSLA
b
c
d e
BB Trading V. --> BB Reddit NOK Reddit --> NOK Trading V.
05 Jan09 Jan13 Jan17 Jan21 Jan25 Jan29 Jan01 Feb05 Feb
0.00
0.05
0.10
0.15
0.20
0.25
0.30Granger Index
BB Reddit --> BB Trading V. AMC Reddit --> AMC Trading V.
PLTR GME
GME
NIO
TSLA
AMC
NOK
BB
PLTR
NIO
TSLA
AMC
NOK
BB
5
>10
  04 Jan 11 Jan 18 Jan 25 Jan
Stocks Ranking
05 Jan09 Jan13 Jan17 Jan21 Jan25 Jan29 Jan01 Feb05 Feb
GME AMC BB NOK NIO TSLA PLTR
15 Dec22 Dec01 Jan08 Jan15 Jan22 Jan01 Feb08 Feb15 Feb
Cumulative Occurrences
101
102
103
104
105
106
15 Dec22 Dec01 Jan08 Jan15 Jan22 Jan01 Feb08 Feb15 Feb
15 Dec22 Dec01 Jan08 Jan15 Jan22 Jan01 Feb08 Feb15 Feb 15 Dec22 Dec01 Jan08 Jan15 Jan22 Jan01 Feb08 Feb15 Feb15 Dec22 Dec01 Jan08 Jan15 Jan22 Jan01 Feb08 Feb15 Feb
Fig. 3 BB, AMC, NOK and the role of GME-engaged users. In all the following subplots
the vertical gray dotted line indicates the beginning of the GME Action (13 January 2021), whereas
the vertical gray dashed line corresponds to the Tweet by Elon Musk (27 January 2021). Triangles
correspond to p-values < 0.05, squares to p-values < 0.1. a) (top) Rank chart of stock tickers on
WSB based on their average daily occurrence within each 15-days window. a) (bottom) Cumulative
number of occurrences of a given stock on WSB. b) Granger Index for possible combinations of BB,
NOK, AMC signals. c) Coefficients of the Multivariate Vector Autoregressive Model for BB-related
activity on Reddit (top panel) and BB trading volume (bottom panel), related to the Reddit (solid
orange) and trading volume (dashed blue) signals. d) Overlap index for pairs of stocks, computed
over a 5-day window with a one-day shift, measuring the proportion of users discussing each pair
of stocks. We observe in both panels an increasing overlap after the starting of the GME rally. e)
Jaccard index for pairs of stocks, computed over a 5-day window with a one-day shift, measuring the
proportion of users discussing both pair of stocks.
22

Supplementary Materials, Section 1: Dataset
Information
Column Description
Author Username
Author ID ID that uniquely identifies each Reddit user
Comment ID ID that uniquely identifies each comment
Submission ID ID of the post under which the comment was made
Parent ID ID of the post or ID of the comment to which the given
comment is a reply
Text Text of the comment
UTC Epoch Unix timestamp of the comment
Supplementary T able 2 Metadata downloaded from Pushshift for each
Reddit comment.
Column Description
Author Username
Author ID ID that uniquely identifies each Reddit user
Submission ID ID that uniquely identifies each submission
Text Text of the submission
Title Title of the submission
UTC Epoch Unix timestamp of the submission
Supplementary T able 3 Metadata downloaded from Pushshift for each
Reddit submission.
Bot name
WSBVoteBot
RemindMeBot
Generic Reddit Bot
ReverseCaptioningBot
LimbRetrieval-Bot
NoGoogleAMPBot
RepostSleuthBot
GetVideoBot
CouldWouldShouldBot
Supplementary T able
4 Reddit bots removed.
23

Column Description
Time Day timestamp of Stock Index
Open Daily Opening Value of Stock Index
Close Daily Closing Value of Stock Index
High Daily High Value of Stock Index
Low Daily Low Value of Stock Index
Trading Volume Daily Volume of Stock Transactions
Supplementary T able 5 Metadata downloaded from polygon.io
for each stock ticker.
Column Description
Time Day timestamp of Market Capitalization
Market Capitalization Daily Market Capitalization
Outstanding Shares Outstanding shares held by investors
Supplementary T able 6 Metadata downloaded from polygon.io for
GME market capitalization.
24

Supplementary Materials, Section 2: Detrended
Cross-Correlations and Hurst Exponent
As discussed in the main text, we perform the detrended cross-correlation analysis
on BB, AMC, NOK. However, in this case, our analysis focuses on data spanning
from January 31st to July 1st, 2021. This time frame is chosen as these stocks were
not extensively discussed prior to January, as reported in the main text. Unlike the
GME case reported in the main text, we observe that the cross-correlation coefficients
exhibit variation and dependence on the scale t (see Figure S1). This variability could
be attributed to the limited number of time scales considered and it is similar to the
variability observed by Podobnik et al. [49] for the New York and Shanghai Stock
Exchange Composite index. Nevertheless, the power-law relationship of the covariances
and variances (see Figure S2), as well as the fitted scale exponent reported in Table
7, supports the findings reported in the main text.
Stock Combination λ
BB Price - Trading V. 0.92
BB Price - Reddit 0.82
BB Trading V. - Reddit 0.66
BB Trading V. - Trading V. 0.65
BB Price - Price 0.99
BB Reddit - Reddit 0.67
AMC Price - Trading V. 0.94
AMC Price - Reddit 0.99
AMC Trading V. - Reddit 0.66
AMC Trading V. - Trading V. 0.69
AMC Price - Price 0.93
AMC Reddit - Reddit 0.71
NOK Price - Trading V. 0.95
NOK Price - Reddit 0.89
NOK Trading V. - Reddit 0.60
NOK Trading V. - Trading V. 0.65
NOK Price - Price 0.84
NOK Reddit - Reddit 0.61
GME Price - Trading V. 0.98
GME Price - Reddit 0.92
GME Trading V. - Reddit 0.66
GME Trading V. - Trading V. 0.63
GME Price - Price 0.93
GME Reddit - Reddit 0.7
Supplementary T able 7 Scale
exponents λ of the possible combinations
of the detrended covariances and variances
for all the stocks. The exponents are fitted
starting from window 20.
We perform an additional analysis by examining the detrended variance of each
signal removing the mean of the signal in each window to further characterise the
non-linear dependencies. This latter exercise allows us to estimate the Hurst exponent
25

a b c
0 20 40 60
Window
0.0
0.2
0.4
0.6
0.8
1.0
Detrended Cross Correlations
BB
Price - Trading V.
Price - Reddit
Trading V. - Reddit
0 20 40 60
Window
0.0
0.2
0.4
0.6
0.8
1.0 AMC
Detrended Cross Correlations
0 20 40 60
Window
0.0
0.2
0.4
0.6
0.8
1.0 NOK
Detrended Cross Correlations
Supplementary Figure S1 Detrended Cross Correlation coefficients for the following combinations
of signals: price / trading volume (light blue), price / Reddit activity (pink), trading volume / Reddit
activity (purple), for BB (panel a), AMC (panel b) and NOK (panel c).
[40, 52]. In this case, instead of considering the variance as a function of the window t,
we examine the rescaled range R/S [40]. The rescaled range is the ratio between the
range of the signal, which is the difference between the maximum and minimum values
in the cumulative sum of the residuals from the mean, and the standard deviation of
the residuals (variance up to a square root). We consistently observe similar results
across the analyzed stocks: the Reddit signals exhibit an almost power-law behavior
in the rescaled range as a function of the window t, along with a Hurst exponent
greater than 0.5 (see Figure S3 and Table 8). In this case, we represent all windows t
since the fluctuations, though less pronounced than the previous analysis, align with
common findings in the literature [40]. These results suggest a persistent and trending
behavior in the Reddit changes, indicating the presence of long-range dependencies in
the signal. To accurately determine the Hurst exponent or the scale exponent, it is
recommended to include a broader range of time scales in the analysis – such as years
[40]. Our analysis serves as an exercise in exploring possible non-linear dependencies
in social media / financial markets dynamics.
26

Price - Trading V.
Price - Reddit
Trading V. - Reddit
Trading V. - Trading V.
Price - Price
Reddit - Reddit
100 101 102
Window
10− 8
10− 6
10− 4
10− 2
1
Detrended Cov./Var.
BB
a b c
102100 101
Window
10− 8
10− 6
10− 4
10− 2
1
AMC
Detrended Cov./Var.
100 101 102
Window
10− 8
10− 6
10− 4
10− 2
1
NOK
Detrended Cov./Var.
Supplementary Figure S2 Detrended Variances for each signal: price (red), trading volume (blue)
and Reddit activity (green); detrended covariances for their paired combinations (same color-scheme
of Figure S1); for BB (panel a), AMC (panel b) and NOK (panel c).
Stock Signal Hurst Exponent
GME Reddit 0.696
GME Trading Volume 0.587
GME Price 0.777
NOK Reddit 0.564
NOK Trading Volume 0.707
NOK Price 0.773
BB Reddit 0.776
BB Trading Volume 0.797
BB Price 0.698
AMC Reddit 0.677
AMC Trading Volume 0.708
AMC Price 0.796
Supplementary T able 8 Hurst exponent for
all stocks and signals. The exponents are fitted
from window length 10 to 200.
27

t [hour]
100
101
102
103
R/S
H=0.677
AMC
100
101
102
103
R/S
H=0.708
101 102 103
100
101
102
103
R/S
H=0.796
100
101
102
103
R/S
H=0.696
GME
100
101
102
103
R/S
H=0.587
101 102 103
t [hour]
100
101
102
103
R/S
H=0.777
100
101
102
103
R/S
H=0.564
NOK
100
101
102
103
R/S
H=0.707
101 102 103
t [hour]
100
101
102
103
R/S
H=0.773
R/SR/SR/S
100
101
102
103
H=0.777
BB
100
101
102
103
H=0.797
101 102 103
t [hour]
100
101
102
103
H=0.698
a b
c d
Reddit Price Trading Volume Reddit Price Trading Volume
Reddit Price Trading Volume Reddit Price Trading Volume
Supplementary Figure S3 Rescaled range analysis conducted for each signal: price (red), trading
volume (blue), and Reddit activity (green). The grey lines represent linear fits, and the corresponding
Hurst exponents are provided in the legend. In panel a, BB, in panel b, AMC, in panel c, GME, and
in panel d, NOK.
28

Supplementary Materials, Section 3: Convergent
Cross-Mapping
To capture and quantify non-linear coupling relations between variables of the same
dynamical systems, we employ a statistical technique known as Convergent Cross
Mapping (CCM) [41]. Similar to Granger Test, the key concept behind CCM is to
test whether the knowledge of the past states of variable x can improve predictions of
variable y ’s future states. Unlike Granger Test, CCM does not assume that we can
separate the information about x from the rest of the systems, as it is often the case
in nonlinear models [53, 54]. Given a time series x(t), we consider the delay vectors
Xτ,D (t) = ( x(t), . . . , x(t − (D − 1)τ )) and for large enough embedding dimension D
(larger than the attractor dimensions) the manifold MX identified by X reconstructs
the original true manifold MS (or all the topological invariant of the dynamical systems
S). Given two time series x(t) and y(t), we assume that these are generated from an
unknown high-dimensional dynamical systems S. Using Takens’ theorem [55–57], we
can construct from each time series s a manifold Ms and confront at a given time t
the points on one reconstructed manifold ( MX ) with the other (MY ). If X → Y , then
information from X is stored in Y and gets embedded in MY , thus it follows that we
can use MY to better predict X (the manifold MY contain the information of both X
and Y ).
Operationally, given the embedding D and lag τ , we consider the vector
˜Yτ,D (t) = (y(t), . . . , y(t − (D − 1)τ ), x(t)) and we perform a neighbor search using the
first dimensions to predict last dimension, i.e., x(t). The correlation ρY Xsummarises
the results of this prediction [41]. CCM requires two criteria to conclude synergistic
relation: cross mapping and convergence [41]. Cross mapping is linked to the correla-
tion ρ and the stronger the coupling in one (or both) direction, the higher the value of
ρ, since the prediction error using one manifold is either lower or equal to that of the
other. Convergence refers to improving the cross-mapping with time-series length T
(sample size to reconstruct the manifold, referred as library size [41]) and it is related
to Takens’ theorem. The more the data, the more precise is the reconstruction of the
attractor, resulting in closer nearest neighbors and higher correlation ρ.
Nonetheless, we still need to determine the appropriate embedding dimension D
and time lag τ [55, 56]. The optimal time lag τ has been considered as the first
minimum of the auto-correlation function of a given time series x(t)[54]. With this
choice, we add as much new information as possible when we introduce new dimensions
to the delay vector. To compute the optimal embedding dimension D, we employ
the Cao’s method, also known as the approximate false nearest neighbors method
[58]. False nearest neighbors are points that are close to each other in the lower-
dimensional embedding space but far apart in the higher-dimensional space [54, 59].
The method works as follows. First, for a point i in a given dimension D, we find its
first nearest neighbors n(i). Next, we calculate the ratio of distances between pairs
(i, n(i)) when computed in dimension D and dimension D + 1. Then, we calculate the
average ratio for all such pairs, defining it asaD. The number of false nearest neighbors
is monotonically decreasing with D and therefore the ratio E1 = aD+1/aD converges
slowly to 1. The method assumes one already has an optimal time lag τ , and then
29

compute the statistics E1 as function of the dimension D. The optimal embedding
dimension is the one corresponding to the knee point of the statistics E1, as it balances
between capturing the underlying dynamics and avoiding excessive sparse points.
Following the Granger analysis and the approach taken by Stavroglou et al. [60],
we have considered the hourly return of the Reddit, trading volume and price sig-
nals. Figure S4 shows the autocorrelation and the E1 statistics for all stocks signals.
Notably, we observe that the optimal lag falls within the range of 6 to 8, and the opti-
mal dimension lies within the range of 5 to 7. Furthermore, we have found that for
every stock, there are at least two combinations of the three signals that have the same
optimal lag and dimension. We have specifically selected this combination for comput-
ing the correlation ρ in Convergent Cross Mapping. Following Luo et al. [61], we have
computed the average correlation ρ on contiguous time series windows of lengthT with
a randomly selected starting point (100 repetitions). This approach reduces the influ-
ence of noise for small windows, thereby resulting in a smoother convergence[41, 61].
Figure S5 shows the correlation ρ for all the combinations of the signals. The changes
in trading volume and Reddit conversations are mutually coupled, as the correla-
tion coefficients in both directions are higher than the others. Moreover, there is a
marginally greater influence of the trading volume on Reddit conversations (negligible
for GME). This result should not surprise since platforms like Reddit tend to influ-
ence the stock market primarily during specific events and with short-term impacts
[28]. The stock market serves as the primary source of information, aggregating infor-
mation from multiple channels, thus it is more likely that trading volume changes
predate Reddit changes. Furthermore, the findings of the price indicate that trading
volume assumes a dominant role – large variations of trading volume were essential
to trigger the short squeezes. Figure S6 displays the correlation cross-mapping for the
GME case using various combinations of optimal dimensions and lags, and we note
no variations in the results. These results corroborate that changes in trading volume
are more tied to the Reddit discussions, rather than to price movements.
30

c d
ba
0 20 40
-1.0
-0.5
0.0
0.5
1.0 BB Reddit (τ = 6)
0 20 40
-1.0
-0.5
0.0
0.5
1.0 BB Trading Volume  (τ = 6)
0 20 40
-1.0
-0.5
0.0
0.5
1.0 BB Price ( τ = 7)
d
10 20 30
E₁
0.0
0.5
1.0
BB Reddit  (D = 5)
d
0 10 20 30
E₁
0.0
0.5
1.0
BB Trading Volume  (D = 5)
d
0 10 20 30
E₁
0.0
0.5
1.0
BB Price (D = 5)
Reddit
Optimal Lag
Trading V.
Optimal Lag
Price
Optimal Lag
Reddit
Optimal dim.
Trading V.
Optimal dim.
Price
Optimal dim.
0 20 40
-1.0
-0.5
0.0
0.5
1.0 AMC Reddit (τ = 6)
0 20 40
-1.0
-0.5
0.0
0.5
1.0 AMC Trading  Volume  (τ = 6)
0 20 40
-1.0
-0.5
0.0
0.5
1.0 AMC Price  (τ = 7)
d
0 10 20 30
E₁
0.0
0.5
1.0
AMC Reddit (D = 7)
d
0 10 20 30
E₁
0.0
0.5
1.0
AMC Trading Volume   (D = 7)
d
0 10 20 30
E₁
0.0
0.5
1.0
AMC Price  (D = 4)
Reddit
Optimal Lag
Trading V.
Optimal Lag
Price
Optimal Lag
Reddit
Optimal dim.
Trading V.
Optimal dim.
Price
Optimal dim.
0 20 40
-1.0
-0.5
0.0
0.5
1.0 NOK Reddit  (τ = 6)
0 20 40
-1.0
-0.5
0.0
0.5
1.0 NOK Trading Volume (τ = 6)
0 20 40
-1.0
-0.5
0.0
0.5
1.0 NOK Price ( τ = 5)
d
10 20 30
E₁
0.0
0.5
1.0
NOK Reddit (D = 6)
d
0 10 20 30
E₁
0.0
0.5
1.0
NOK Trading  Volume  (D = 6)
d
0 10 20 30
E₁
0.0
0.5
1.0
NOK Price (D = 6)
Reddit
Optimal Lag
Trading V.
Optimal Lag
Price
Optimal Lag
Reddit
Optimal dim.
Trading V.
Optimal dim.
Price
Optimal dim.
0 20 40
-1.0
-0.5
0.0
0.5
1.0 GME Reddit  (τ = 7)
0 20 40
-1.0
-0.5
0.0
0.5
1.0 GME Trading  Volume (τ = 6)
0 20 40
-1.0
-0.5
0.0
0.5
1.0 GME Price  (τ = 8)
d
0 10 20 30
E₁
0.0
0.5
1.0
GME Reddit (D =  5)
d
0 10 20 30
E₁
0.0
0.5
1.0
GME Trading  Volume   (D = 7)
d
0 10 20 30
E₁
0.0
0.5
1.0
GME Price  (D = 5)
Reddit
Optimal Lag
Trading V.
Optimal Lag
Price
Optimal Lag
Reddit
Optimal dim.
Trading V.
Optimal dim.
Price
Optimal dim.
Autocorrelation AutocorrelationAutocorrelationAutocorrelationAutocorrelationAutocorrelation
Autocorrelation AutocorrelationAutocorrelationAutocorrelationAutocorrelationAutocorrelation
Lag
Lag
Lag
Lag
Lag
Lag
Lag
Lag
Lag
Lag
Lag
Lag
Supplementary Figure S4 Optimal lag and dimension for all the stocks. Autocorrelation
(Left) and E1 statistics (Right) for all the signals (each sub-panel) and all the stocks (each panel).
The markers identified the optimal lag (square) and the optimal dimension (circle). In panel a, BB,
in panel b, AMC, in panel c, NOK, and in panel d, GME. Autocorrelation Reddit (orange), trading
volume (blue), price (green). E1 statistics Reddit (red), trading volume (purple), price (black).
31

0 200 400 600
BB(τ = 6, D = 5)
0 200 400 600
BB(τ = 6, D = 5)
0 200 400 600
BB(τ = 6, D = 5)
Reddit -> Trading V.
Trading V. -> Reddit
Price -> Trading V.
Trading V. -> Price
Price -> Reddit
Reddit -> Price
0 200 400 600
AMC(τ = 6, D = 7)
0 200 400 600
AMC(τ = 6, D = 7)
0 200 400 600
AMC(τ = 6, D = 7)
Reddit -> Trading V.
Trading V. -> Reddit
Price -> Trading V.
Trading V. -> Price
Price -> Reddit
Reddit -> Price
ba
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
Library Size TLibrary Size TLibrary Size T
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
Library Size TLibrary Size TLibrary Size T
0 200 400 600
NOK(τ = 6, D = 6)
0 200 400 600
NOK(τ = 6, D = 6)
0 200 400 600
NOK(τ = 6, D = 6)
Reddit -> Trading V.
Trading V. -> Reddit
Price -> Trading V.
Trading V. -> Price
Price -> Reddit
Reddit -> Price
0 200 400 600
GME(τ = 7, D = 5)
0 200 400 600
GME(τ = 7, D = 5)
0 200 400 600
GME(τ = 7, D = 5)
Reddit -> Trading V.
Trading V. -> Reddit
Price -> Trading V.
Trading V. -> Price
Price -> Reddit
Reddit -> Price
c d
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
-1.0
-0.5
0.0
0.5
1.0Correlation ρ
Library Size TLibrary Size TLibrary Size T Library Size TLibrary Size TLibrary Size T
Supplementary Figure S5 Convergent Cross-Mapping for all the stocks. Correlation
(ρ) as a function of the length of time series T for optimal lag τ and optimal dimension D for
different combinations of signals: Reddit-to-trading volume (orange, left panel), trading volume-to-
Reddit (blue, left panel), trading volume-to-price (purple, center), price-to-trading volume (light
green, center), price-to-Reddit (light blue, right panel), Reddit-to-price (pink, right panel). In panel
a, BB ( τ = 6 , D= 5), in panel b, AMC ( τ = 6 , D= 7), in panel c, NOK ( τ = 6 , D= 6), and in
panel d, GME ( τ = 7, D= 5).
32

0 200 400 600
-1.0
-0.5
0.0
0.5
1.0 GME(τ = 6, D = 7)
0 200 400 600

Correlation ρ
-1.0
-0.5
0.0
0.5
1.0 GME(τ = 6, D = 7)
0 200 400 600
-1.0
-0.5
0.0
0.5
1.0 GME(τ = 6, D = 7)
Reddit -> Trading V.
Trading V. -> Reddit
Price -> Trading V.
Trading V. -> Price
Price -> Reddit
Reddit -> Price
a
Library Size TLibrary Size TLibrary Size T
Correlation ρ
Correlation ρ
0 200 400 600
-1.0
-0.5
0.0
0.5
1.0 GME(τ = 8, D = 5)
0 200 400 600
-1.0
-0.5
0.0
0.5
1.0 GME(τ = 8, D = 5)
0 200 400 600
-1.0
-0.5
0.0
0.5
1.0 GME(τ = 8, D = 5)
Reddit -> Trading V.
Trading V. -> Reddit
Price -> Trading V.
Trading V. -> Price
Price -> Reddit
Reddit -> Price
b
Correlation ρ
Correlation ρ
Correlation ρ
Library Size TLibrary Size TLibrary Size T
Supplementary Figure S6 Convergent Cross-Mapping for GME for different optimal
lag and dimension. Correlation ρ as a function of length of time series T for different combinations
of GME signals: Reddit-to-trading volume (orange, left panel), trading volume-to-Reddit (blue, left
panel), trading volume-to-price (purple, center), price-to-trading volume (light green, center), price-
to-Reddit (light blue, right panel), Reddit-to-price (pink, right panel). In panel a optimal lag τ = 6
and optimal dimension D = 7, and in panel b optimal lag τ = 8 and optimal dimension D = 5. We
observe consistent results with Figure S5.
33

Supplementary Materials, Section 4: Screenshot
analysis
As detailed in the main text, we employ computer vision techniques to extract actual
financial investments within the WSB community. Indeed users in the WSB commu-
nity typically share screenshots of their open positions. Lucchini et al. [30] quantified
the WSB community’s commitment to GME by parsing these screenshots using a
combination of text analysis and computer vision techniques. We rely on this previ-
ous analysis and consider the dataset of 78468 screenshots as our initial dataset. We
note that these screenshots exhibit arbitrary structures, as WSB users do not use a
specific app and screenshots are handmade, resulting in a lack of standardized for-
mat. Through manual inspection of a sample of the screenshots, we identify a set of
keywords that proved useful in narrowing down the selection to those representing
actual investments (6525 screenshots), as discussed in the main text. Our extraction
technique, for instance, does not accommodate the possibility of multiple orders in a
single screenshot, as we extract only the highest value.
Given this arbitrariness, we consider a sample of 1000 screenshot and validate the
extraction through manual inspection. Figure S7 a displays the comparison between
OCR technique and manual inspection, with an accuracy of 0.85 and an RMSE of
0.47, where RMSE is computed using log-transformed data and accuracy is determined
through a binary classification method with a threshold of 0.05 for correctness. We
perform an additional exercise using all the dataset [30] and extract all stocks ticker
symbols in a given screenshot. Figure S7 b summarises the popularity of a given stock
in the screenshots, notably observing the same stock ranking as reported in the main
text using ticker occurrences in posts/comments. Table 9 details the number of co-
occurrences of two stocks in a screenshot. Notably, we observe that the stocks AMC,
BB, NOK and GME exhibit a clustering pattern, while PLTR, TSLA and NIO show
comparatively fewer connections, primarily appearing in conjunction with GME.
34

Stock A Stock B Number of Screenshots
AMC PLTR 56
GME NIO 62
NOK PLTR 62
NIO PLTR 65
AMC NIO 70
NIO TSLA 80
PLTR TSLA 81
AMC TSLA 98
BB PLTR 132
GME TSLA 148
GME PLTR 183
BB NOK 457
GME NOK 484
AMC BB 648
AMC NOK 698
BB GME 719
AMC GME 1773
Supplementary T able 9 Cumulative number
of screenshots for stock ticker pairs.
a b
GME: 42.7 %
AMC: 18.9 %
BB: 8.8 %
NOK: 6.7 %
NIO: 2.5 % TSLA: 3.7 %
PLTR: 5.9 %
Other (less than 2%): 10.9 %
101 102 103 104 105 106 107
Human
101
102
103
104
105
106
107
OCR
Supplementary Figure S7 Comparison between OCR and human extraction and stocks
rank. a) Scatter plot displaying the comparison between position values extracted using OCR and
human visual inspection. b) Treemap rank chart showing the occurrences of stock tickers in screen-
shots.
35

Supplementary Materials, Section 5: Robustness
checks on Granger Test
Granger Test: stationarity tests
Twitter Trading Volume Reddit
Date t p-value t p-value t p-value
2020-12-17 -4.296 0.000 -4.299 0.000 -4.429 0.000
2020-12-18 -4.251 0.001 -4.236 0.001 -4.504 0.000
2020-12-19 -4.894 0.000 -4.233 0.001 -4.405 0.000
2020-12-20 -4.894 0.000 -4.233 0.001 -4.405 0.000
2020-12-21 -4.894 0.000 -4.233 0.001 -4.405 0.000
2020-12-22 -5.000 0.000 -4.168 0.001 -4.350 0.000
2020-12-23 -4.627 0.000 -5.939 0.000 -5.031 0.000
2020-12-24 -5.182 0.000 -4.987 0.000 -5.315 0.000
2020-12-25 -5.149 0.000 -4.134 0.001 -4.947 0.000
2020-12-26 -4.853 0.000 -3.853 0.002 -4.601 0.000
2020-12-27 -4.853 0.000 -3.853 0.002 -4.601 0.000
2020-12-28 -4.853 0.000 -3.853 0.002 -4.601 0.000
2020-12-29 -4.751 0.000 -3.880 0.002 -4.666 0.000
2020-12-30 -4.729 0.000 -4.091 0.001 -4.712 0.000
2020-12-31 -1.841 0.360 -4.280 0.000 -5.348 0.000
2021-01-01 -3.202 0.020 -4.657 0.000 -5.688 0.000
2021-01-02 -2.931 0.042 -4.244 0.001 -5.259 0.000
2021-01-03 -2.931 0.042 -4.244 0.001 -5.259 0.000
2021-01-04 -2.931 0.042 -4.244 0.001 -5.259 0.000
2021-01-05 -2.938 0.041 -4.258 0.001 -5.288 0.000
2021-01-06 -2.698 0.074 -4.552 0.000 -4.940 0.000
2021-01-07 -2.715 0.072 -4.689 0.000 -4.820 0.000
2021-01-08 -2.788 0.060 -5.738 0.000 -5.764 0.000
2021-01-09 -2.931 0.042 -6.234 0.000 -6.076 0.000
2021-01-10 -2.931 0.042 -6.234 0.000 -6.076 0.000
2021-01-11 -2.931 0.042 -6.234 0.000 -6.076 0.000
2021-01-12 -3.698 0.004 -6.108 0.000 -5.725 0.000
2021-01-13 -3.815 0.003 -5.685 0.000 -4.988 0.000
2021-01-14 -1.185 0.680 -4.290 0.000 -4.738 0.000
2021-01-15 -5.310 0.000 -4.294 0.000 -4.785 0.000
2021-01-16 -5.680 0.000 -4.425 0.000 -5.053 0.000
2021-01-17 -5.680 0.000 -4.425 0.000 -5.053 0.000
2021-01-18 -5.680 0.000 -4.425 0.000 -5.053 0.000
2021-01-19 -5.346 0.000 -4.167 0.001 -4.937 0.000
2021-01-20 -5.225 0.000 -4.147 0.001 -4.752 0.000
2021-01-21 -5.104 0.000 -3.747 0.004 -4.792 0.000
2021-01-22 -5.362 0.000 -4.006 0.001 -4.843 0.000
2021-01-23 -5.393 0.000 -3.965 0.002 -4.949 0.000
2021-01-24 -5.393 0.000 -3.965 0.002 -4.949 0.000
2021-01-25 -5.393 0.000 -3.965 0.002 -4.949 0.000
2021-01-26 -4.094 0.001 -4.004 0.001 -5.068 0.000
2021-01-27 -4.972 0.000 -3.601 0.006 -10.878 0.000
2021-01-28 -4.298 0.000 -4.008 0.001 -3.058 0.030
2021-01-29 -4.189 0.001 -4.101 0.001 -2.560 0.102
2021-01-30 -3.637 0.005 -4.127 0.001 -2.636 0.086
2021-01-31 -3.637 0.005 -4.127 0.001 -2.636 0.086
2021-02-01 -3.637 0.005 -4.127 0.001 -2.636 0.086
2021-02-02 -3.254 0.017 -4.352 0.000 -2.881 0.048
2021-02-03 -3.864 0.002 -4.358 0.000 -2.767 0.063
2021-02-04 -3.460 0.009 -3.839 0.003 -2.696 0.075
2021-02-05 -3.702 0.004 -3.995 0.001 -2.989 0.036
2021-02-06 -3.690 0.004 -4.153 0.001 -3.051 0.030
2021-02-07 -3.690 0.004 -4.153 0.001 -3.051 0.030
2021-02-08 -3.690 0.004 -4.153 0.001 -3.051 0.030
2021-02-09 -3.001 0.035 -3.754 0.003 -2.262 0.184
2021-02-10 -2.733 0.069 -3.412 0.011 -2.268 0.182
2021-02-11 -2.702 0.074 -3.446 0.009 -2.765 0.063
2021-02-12 -3.432 0.010 -3.196 0.020 -2.123 0.235
2021-02-13 -3.045 0.031 -3.006 0.034 -1.854 0.354
Supplementary T able 10 Results of the Augmented Dickey-Fuller test conducted on the
Twitter, Trading Volume, and Reddit signals to assess stationarity. The test statistics (t) and
corresponding p-values (rounded to the third decimal) are reported for each signal in various time
windows, identified by the Date column. Each row represents a separate test conducted on the
respective signal within the specified time window.
36

Granger Test: p-values and coefficient of the Autoregressive
Model
Date Reddit − > Trading Volume Trading Volume − > Reddit Reddit − > Twitter Twitter − > Reddit Twitter − > Trading Volume Trading Volume − > Twitter
2021-01-02 0.909 0.041 0.687 0.742 0.934 0.197
2021-01-03 0.909 0.041 0.687 0.742 0.934 0.197
2021-01-04 0.909 0.041 0.687 0.742 0.934 0.197
2021-01-05 0.606 0.07 0.651 0.804 0.998 0.176
2021-01-06 0.488 0.757 0.846 0.751 0.603 0.225
2021-01-07 0.458 0.815 0.963 0.81 0.62 0.296
2021-01-08 0.606 0.698 0.716 0.734 0.549 0.282
2021-01-09 0.479 0.602 0.742 0.876 0.578 0.266
2021-01-10 0.479 0.602 0.742 0.876 0.578 0.266
2021-01-11 0.479 0.602 0.742 0.876 0.578 0.266
2021-01-12 0.462 0.472 0.833 0.756 0.983 0.3
2021-01-13 0.507 0.855 0.67 0.589 0.987 0.226
2021-01-14 0 0.001 0.703 0.327 0.43 0.636
2021-01-15 0 0.001 0.634 0.531 0.618 0.769
2021-01-16 0 0.003 0.54 0.575 0.811 0.521
2021-01-17 0 0.003 0.54 0.575 0.811 0.521
2021-01-18 0 0.003 0.54 0.575 0.811 0.521
2021-01-19 0 0.006 0.524 0.611 0.884 0.497
2021-01-20 0 0.023 0.571 0.675 0.958 0.603
2021-01-21 0 0.033 0.487 0.714 0.877 0.499
2021-01-22 0 0.03 0.42 0.681 0.93 0.461
2021-01-23 0 0.045 0.515 0.64 0.816 0.649
2021-01-24 0 0.045 0.515 0.64 0.816 0.649
2021-01-25 0 0.045 0.515 0.64 0.816 0.649
2021-01-26 0.002 0.086 0.579 0.722 0.742 0.797
2021-01-27 0.001 0.036 0.769 0.92 0.938 0.91
2021-01-28 0.339 0.663 0.067 0.518 0.741 0.865
2021-01-29 0.26 0.296 0.1 0.487 0.611 0.758
2021-01-30 0.346 0.321 0.084 0.764 0.457 0.946
2021-01-31 0.346 0.321 0.084 0.764 0.457 0.946
2021-02-01 0.346 0.321 0.084 0.764 0.457 0.946
2021-02-02 0.405 0.31 0.126 0.787 0.848 0.571
2021-02-03 0.189 0.474 0.117 0.919 0.369 0.797
2021-02-04 0.342 0.504 0.077 0.967 0.416 0.603
2021-02-05 0.308 0.501 0.127 0.888 0.449 0.714
2021-02-06 0.183 0.602 0.095 0.92 0.482 0.819
2021-02-07 0.183 0.602 0.095 0.92 0.482 0.819
2021-02-08 0.183 0.602 0.095 0.92 0.482 0.819
2021-02-09 0.225 0.739 0.118 0.986 0.287 0.796
2021-02-10 0.29 0.795 0.425 0.842 0.215 0.907
2021-02-11 0.657 0.749 0.999 0.194 0.501 0.938
2021-02-12 0.239 0.783 0.821 0.191 0.805 0.521
2021-02-13 0.408 0.817 0.932 0.302 0.641 0.451
Supplementary T able 11 Results of the Granger test between Reddit, Trading Volume, and
Twitter signals (GME). The table reports the p-values (rounded to the third decimal) for the
different directions across time windows identified by the Date column. Each row represents a
separate test conducted for a specific direction: Reddit anticipating Trading Volume, Trading
Volume anticipating Reddit, Reddit anticipating Twitter, Twitter anticipating Reddit, Twitter
anticipating Trading Volume, and Trading Volume anticipating Twitter.
37

a
b
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
Reddit Model
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
CoefficientCoefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
Reddit Trading Volume
Reddit ModelTrading V. Model
Reddit Trading Volume
Supplementary Figure S8 Coefficients of the autoregressive model capturing the relationship
between signals over time. In panel a, the coefficient is computed for the restricted model (with only
one signal): Reddit (top) and Trading Volume (bottom). In panel b, the coefficients are computed
for the full model predicting Reddit. Each point represents the coefficients over time series spanning
from 5 January 2021 to 5 February 2021. The vertical gray dotted line indicates the initiation of
the Action phase (13 January 2021), whereas the vertical gray dashed line corresponds to the tweet
by Elon Musk (27 January 2021). The triangles refer to statistical significant test (p-value p <0.1)
within the window.
38

Granger Test and Multivariate Vector Autoregression model
with a lag of 7
Figure S9 displays the Granger Index for various combinations of GME signals at lag
7 (approximately 1 day), both when it is significant (p-value p <0.1) and when it is
not. The Granger Index in the Reddit-to-Trading Volume direction becomes significant
during the Action phase, similar to the analysis at lag 1 reported in the main text.
Notably, the magnitude of the Granger Index at lag 7 is higher than at lag 1, and
the Reddit-to-Trading Volume direction shows the strongest relationship among all
possible combinations. Furthermore, we observe a significant Granger Index in the
Reddit-to-Twitter direction from the Action and Visibility phases, and in the Trading
Volume-to-Twitter direction for the Action phase only.
However, when we consider the Multivariate Vector Autoregression model, we find
different results compared to those reported in the main text. Figure S10 displays the
different coefficients for each signal in various models at lag 7, both when it is sig-
nificant (p-value p < 0.1) and when it is not. We observe that the coefficients are
consistently close to zero and not statistically significant, except for the Reddit-to-
Twitter coefficient in the upper panel, which becomes significant and positive during
the Visibility phase. The coefficients at lag 1 are the same of the analysis reported
in the main text. Overall, these results corroborate that the shortest time scales
are of more significance in the social-media/market dynamics. Furthermore, with the
inclusion of lags, the model’s error diminishes as the information content increases [51].
39

05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
0.0
0.2
0.4
0.6
0.8
1.0
Granger Index
Trading V. --> Reddit Reddit --> Trading V. Trading V. --> Twitter Reddit --> Twitter
Supplementary Figure S9 Granger Index capturing the predictive power of a signal on another
(with a lag of 1 day) for the following pairs: Trading Volume-to-Reddit (blue), Reddit-to-Trading
Volume (red), Trading Volume-to-Twitter (gray) and Reddit-to-Twitter (yellow). The vertical gray
dotted line indicates the initiation of the Action phase (13 January 2021), whereas the vertical gray
dashed line corresponds to the Tweet by Elon Musk (27 January 2021) that marks the start of the
Visibility phase. The triangles correspond to statistical significant values (p-values < 0.1).
40

− 2.0
− 1.5
− 1.0
− 0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
Twitter Reddit Trading Volume
− 2.0
− 1.5
− 1.0
− 0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
− 2.0
− 1.5
− 1.0
− 0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
Twitter ModelReddit ModelTrading Volume Model
Supplementary Figure S10 Each panel shows the coefficients of the multivariate autoregressive
model at lag 7 predicting Twitter (top), Reddit (middle), and Trading Volume (bottom) activities,
from antecedent values of Reddit (orange), Twitter (lightblue), and Trading Volume (blue). The
vertical gray dotted line indicates the initiation of the Action phase (13 January 2021), whereas the
vertical gray dashed line corresponds to the tweet by Elon Musk (27 January 2021). The triangles
refer to statistical significant test (p-value p <0.1) within the 15-days window.
41

Granger Test and Multivariate Vector Autoregression model
for different window length
We replicate the analysis outlined in the main text, specifically employing Granger Test
and the multivariate vector autoregression model, while varying the window length to
validate the robustness of our results [51]. Figure S11 displays the temporal evolution
of the Granger index over four distinct windows, ranging from 13 to 17 days, and
Figure S11 displays the coefficient of multivariate vector autoregression models over
the same windows. Consistently, we observe results aligning with those presented in
the main text, particularly in relation to the three phases. We note that the Granger
index diminishes as the window length increases, yet the ratio between Granger indices,
or the ratio of a Granger index at one time to that at a subsequent time, remains
constant. This variation is not observed in the coefficients of the Multivariate Vector
Autoregression models, given that we are modeling log-returns. However, we also note
a shift (of one day) in the third phase in both these results.
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
0.0
0.1
0.2
0.3
0.4
0.5Granger Index
Window = 13
0.0
0.1
0.2
0.3
0.4
0.5
Window = 14
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
 Window = 16
0.00
0.05
0.10
0.15
0.20
0.25
0.30
 Window = 17
Trading V. --> Reddit Reddit --> Trading V.
Trading V. --> Twitter Reddit --> Twitter Significant
Granger Index
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
Granger Index
Granger Index
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
Trading V. --> Reddit Reddit --> Trading V.
Trading V. --> Twitter Reddit --> Twitter Significant
Trading V. --> Reddit Reddit --> Trading V.
Trading V. --> Twitter Reddit --> Twitter Significant
Trading V. --> Reddit Reddit --> Trading V.
Trading V. --> Twitter Reddit --> Twitter Significant
a b
dc
Supplementary Figure S11 Granger Index capturing the predictive power of a signal on another
(with a lag of 1 hour) for the following pairs: Trading Volume-to-Reddit (blue), Reddit-to-Trading
Volume (red), Trading Volume-to-Twitter (gray) and Reddit-to-Twitter (yellow). Each point is com-
puted considering time series spanning the w preceding days. In panel a w = 13, in panel b w = 14,
in panel c w = 16 and in panel d w = 17. The vertical gray dotted line indicates the initiation of
the Action phase (13 January 2021), whereas the vertical gray dashed line corresponds to the tweet
by Elon Musk (27 January 2021). The triangles refer to statistical significant test (p-value p <0.1)
within the window.
42

Twitter Reddit Trading Volume
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
Twitter ModelReddit ModelTrading V. Model
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb 05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
Twitter ModelReddit ModelTrading V. Model
Twitter Reddit Trading Volume
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
Twitter ModelReddit ModelTrading V. Model
Twitter ModelReddit ModelTrading V. Model
Twitter Reddit Trading Volume Twitter Reddit Trading Volume
a b
dc
Supplementary Figure S12 Each sub-panel shows the coefficients of a multivariate vector autore-
gressive model predicting Twitter (top), Reddit (middle), and Trading Volume (bottom) activities,
from antecedent values of Reddit (solid orange), Twitter (dashed lightblue), and trading volume (dot-
ted blue). Each point is computed considering time series spanning the w preceding days. In panel a
w = 13, in panel b w = 14, in panel c w = 16 and in panel d w = 17. The vertical gray dotted line
indicates the initiation of the Action phase (13 January 2021), whereas the vertical gray dashed line
corresponds to the tweet by Elon Musk (27 January 2021). The triangles refer to statistical signifi-
cant test (p-value p <0.1) within the window.
43

Granger Test and Multivariate Vector Autoregression model
on daily log returns
Trading V. --> Reddit Reddit --> Trading V. Trading V. --> Twitter Reddit --> Twitter
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
0.0
0.1
0.2
0.3
0.4
0.5
Granger Index
Supplementary Figure S13 Granger Index capturing the predictive power of a signal on another
(using daily log return with a lag of 1 hour) for the following pairs: Trading Volume-to-Reddit (blue),
Reddit-to-Trading Volume (red), Trading Volume-to-Twitter (gray) and Reddit-to-Twitter (yellow).
The time windows span 15-day, corresponding to 120 points per time series. The vertical gray dotted
line indicates the initiation of the Action phase (13 January 2021), whereas the vertical gray dashed
line corresponds to the Tweet by Elon Musk (27 January 2021) that marks the start of the Visibility
phase. The triangles correspond to statistical significant values (p-values < 0.1).
44

Twitter ModelReddit ModelTrading Volume Model
Twitter Reddit Trading Volume
− 2.0
− 1.5
− 1.0
− 0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
− 2.0
− 1.5
− 1.0
− 0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
− 2.0
− 1.5
− 1.0
− 0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
Supplementary Figure S14 Each panel shows the coefficients of the multivariate autoregressive
model using daily log return at lag 1 hour predicting Twitter (top), Reddit (middle), and Trading
Volume (bottom) activities, from antecedent values of Reddit (orange), Twitter (lightblue), and
Trading Volume (blue). The time windows span 15-day, corresponding to 120 points per time series.
The vertical gray dotted line indicates the initiation of the Action phase (13 January 2021), whereas
the vertical gray dashed line corresponds to the tweet by Elon Musk (27 January 2021). The triangles
refer to statistical significant test (p-value p <0.1) within the 15-days window.
45

Multivariate Vector Autoregression AMC and NOK during
January 2021
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
AMC Reddit Trading Volume
05Jan 09Jan 13Jan 17Jan 21Jan 25Jan 29Jan 01Feb 05Feb
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
Reddit ModelTrading Volume Model
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
NOK Reddit Trading Volume
05Jan 09Jan 13Jan 17Jan 21Jan 25Jan 29Jan 01Feb 05Feb
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Coefficient
Reddit ModelTrading Volume Model
a b
Supplementary Figure S15 Each panel shows the coefficients of an autoregressive model predict-
ing Reddit (top) and Trading Volume (bottom) activities, from antecedent values of Reddit (orange)
and Trading Volume (blue). The triangles correspond to statistical significant values (p-values< 0.1).
The x-values of the lineplots correspond to the last day of each 15-days window. In all the subplots
the vertical gray dotted line indicates the initiation of the Action phase (13 January 2021), whereas
the vertical gray dashed line corresponds to the Visibility phase (27 January 2021). In panel a AMC
and in panel b NOK.
46

Supplementary Materials, Section 6: Reply speed
0.0
0.5
1.0
1.5
2.0
2.5
3.0Reply Speed [hour]
Reply Speed std Reply Speed
05 Jan 09 Jan 13 Jan 17 Jan 21 Jan 25 Jan 29 Jan 01 Feb 05 Feb
Supplementary Figure S16 Daily average (and standard deviation of the mean) of the reply
speed, defined as the average time interval between a comment and its direct responses under a Reddit
post. The average by post is weighted using the number of comments underneath the post. We apply
a 5-day moving average to the time series and consider only weekdays to enhance the chart’s clarity.
47

Supplementary Materials, Section 7: Users’ interests
in stocks and shifts in January
a
Number of Users
AMC
GME - AMC
BB
GME - BB
GME
NOK
GME - NOK
PLTR
TSLA
GME
NIO
GME - PLTR
GME - TSLA
GME - NIO
15 Dec 22 Dec 01 Jan 08 Jan 15 Jan 22 Jan 01 Feb 08 Feb 15 Feb
1
101
102
103
104
105
106
15 Dec 22 Dec 01 Jan 08 Jan 15 Jan 22 Jan 01 Feb 08 Feb 15 Feb 15 Dec 22 Dec 01 Jan 08 Jan 15 Jan 22 Jan 01 Feb 08 Feb 15 Feb
1
101
102
103
104
105
106
15 Dec 22 Dec 01 Jan 08 Jan 15 Jan 22 Jan 01 Feb 08 Feb 15 Feb 15 Dec 22 Dec 01 Jan 08 Jan 15 Jan 22 Jan 01 Feb 08 Feb 15 Feb 15 Dec 22 Dec 01 Jan 08 Jan 15 Jan 22 Jan 01 Feb 08 Feb 15 Feb
Number of Users
b
Supplementary Figure S17 Raw Number of users talking of stock. Each subpanel represents
the number of users discussing GME (red solid line), a stock and both (dashed lines). Panela displays
the stocks that gained popularity in January: BB (left panel), AMC (central panel) and NOK (right
panel). Panel b displays the stocks that are no longer in the top rank: PLTR (left panel), TSLA
(central panel) and NIO (right panel). The vertical gray dotted line indicates the beginning of the
Action phase (13 January 2021), whereas the vertical gray dashed line corresponds to the Tweet by
Elon Musk (27 January 2021).
48

08 Dec 15 Dec 22 Dec 01 Jan 08 Jan 15 Jan 22 Jan 01 Feb
101
102
103
104
105
Number of Users BB, AMC, NOK
BB, AMC, NOK NIO
50
100
150
200
250
300
350
400
Number of Users NIO
Supplementary Figure S18 Users shift from NIO to BB, AMC, NOK during January .
The plot displays the dynamic shift in user engagement, contrasting the raw number of users “leaving”
NIO with the raw number of users “adopting” BB, AMC, NOK over time. “Leaving” users are those
who have stopped discussing NIO, while ”adopting” users are those initiating discussions for the first
time. The vertical gray dotted line indicates the beginning of the Action phase (13 January 2021),
whereas the vertical gray dashed line corresponds to the Tweet by Elon Musk (27 January 2021).
49
