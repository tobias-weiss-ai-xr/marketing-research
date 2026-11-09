---
title: Stress index strategy enhanced with financial news sentiment analysis for the equity markets
url: https://arxiv.org/abs/2404.00012
category: ai-marketing
subcategory: empirical
date: 2024-03
venue: ''
authors:
- Baptiste Lefort
- Eric Benhamou
- Jean-Jacques Ohana
- David Saltiel
- Beatrice Guez
source: arxiv
pdf_url: https://arxiv.org/pdf/2404.00012
pages: 41
chars: 49646
fetched_at: '2026-11-08T13:15:49+00:00'
kb_version: 1
---

# Stress index strategy enhanced with financial news sentiment analysis for the equity markets

Stress index strategy enhanced with financial news
sentiment analysis for the equity markets
Baptiste Lefort1, 3, Eric Benhamou 2, 3, Jean-Jacques Ohana 3, David Saltiel 3,
Beatrice Guez3, and Thomas Jacquot 3
1CentraleSup´ elec, Paris-Saclay University
2Paris-Dauphine PSL
3Ai For Alpha
Abstract
This paper introduces a new risk-on risk-off strategy for the stock market, which com-
bines a financial stress indicator with a sentiment analysis done by ChatGPT reading
and interpreting Bloomberg daily market summaries. Forecasts of market stress derived
from volatility and credit spreads are enhanced when combined with the financial news
sentiment derived from GPT4. As a result, the strategy shows improved performance,
evidenced by higher Sharpe ratio and reduced maximum drawdowns. The improved
performance is consistent across the NASDAQ, the S&P 500 and the six major equity
markets, indicating that the method generalises across equities markets.
Keywords: Market stress, Volatility, News sentiment, Investment strategy
JEL Codes: G14, D81, C55, G17
arXiv:2404.00012v1  [q-fin.ST]  12 Mar 2024

1 Introduction
Recent advancements in Natural Language Processing (NLP) with Large Language Models
(LLMs) have made the sentiment analysis of financial news by machines a practical achieve-
ment and no longer just a dream. More precisely, Large Language Models (LLMs) have
marked a major step forward in processing large contexts, exhibiting human-level perfor-
mance on various professional and academic benchmarks, although they still have limita-
tions such as reliability issues and limited context windows [OpenAI, 2023]. Their ability to
process more context has shown particularly interesting applications in many business areas
[George and George, 2023]. Hence exploring the potential to extract either weak or strong
signals from financial news to enhance a risk-on risk-off investment strategy becomes highly
pertinent.
Indeed, extracting sentiment from financial news is not new [Tetlock, 2007, Schumaker
and Chen, 2009], and finance has a longstanding tradition of exploiting textual data [Kear-
ney and Liu, 2014]. More precisely, sentiment analysis is a task where we aim at identifying
the underlying sentiment in a text. Many different types of models and methods can be
employed for identifying sentiment [Baccianella et al., 2010, Tang et al., 2023]. Models like
BERT and its finance-focused version FinBERT have exposed their application in the finan-
cial industry [Devlin et al., 2018, Araci, 2019]. These models have significantly increased the
sentiment analysis’s precision [Kant et al., 2018], giving a new opening to using the news
for financial decision-making. Likewise, SentiWordNet 3.0, provides an enhanced lexical
resource for sentiment analysis, showing about 20% accuracy improvement over its earlier
version [Baccianella et al., 2010]. Recent advancements like FinEntity focus on entity-level
sentiment classification in financial texts, demonstrating its utility in investment and reg-
ulatory applications [Tang et al., 2023]. Deep Learning application have also shown clear
improvement and proved their ability to provide consistently reliable sentiment to a complex
text [Zhang et al., 2018].
However, when scrutinized across various equity markets and extended out-of-sample
1

backtesting, these efforts proved to be less than compelling Xing et al. [2018]. Interpreting
financial news has long been a complex task [Loughran and McDonald, 2011], as it involves
intricate concepts open to various interpretations and contains time-sensitive information
with an expiration date of relevance. Moreover, the sentiment conveyed in financial news
is often influenced by human perception, and there are numerous underlying implications
[Ikizlerli et al., 2019, Elliott et al., 2018].
We hypothesize two things that can help solve the seminal problem of interpreting news
in order to forecast equity market regimes. First, the emergence of Large Language Models
(LLMs) could bring fresh perspectives to this longstanding issue, potentially enhancing the
interpretation of ambiguities in financial news. Second, news sentiments should be combined
with other signals in order to have a robust risk-on risk-off strategy accross major equity
markets.
Hence, we present here a new approach to tackle risk-on, risk-off strategy for the stock
market. This approach integrates a financial stress indicator with sentiment analysis per-
formed by ChatGPT, which reads and interprets daily market summaries from Bloomberg.
Additionally, we present a strategy selection method, alternating between the hybrid strat-
egy that combines news signals and stress index and another based only on the conventional
stress index indicator.
The rest of the paper is organized as follows. Section 2 provides a review of existing
literature on the application of ChatGPT in formulating financial strategies. In section
3, we explain how our methodology differs from existing studies and outline our principal
contributions. Section 4 presents the different types of data used: namely news, the stress
index and investment universe overwhich this new strategy is tested. Section 5 details the
comprehensive set of experiments conducted, highlighting the execution of 18 distinct tests.
These tests are designed to ascertain the most effective strategy from a range of alternatives,
namely whether the news signal and the stress index signal are effective or not. In total, six
varied strategies are evaluated across three disparate financial markets to assert whether the
2

results remains similar across various equity markets. In Section 6, we provide an in-depth
discussion of the result, with a particular focus on the dynamically strategy that alternates
between the stress index and the news sentiment and the stress index alone. The findings
reveal that this combined method consistently outperforms other strategies in all three equity
markets evaluated. The superiority of this approach is highlighted by its higher Sharpe and
Calmar ratio (the ratio of return to maximum drawdown), when compared with the other
strategies that rely on the stress index, news alone, the volatility index (VIX) based strategy,
and a static combination of stress with news. Section 7 concludes and suggests future works.
2 Related Works
In the field of finance and economics, numerous recent academic studies have used Chat-
GPT, including [Hansen and Kazinnik, 2023], [Cowen and Tabarrok, 2023], [Korinek, 2023,
Lopez-Lira and Tang, 2023], and [Noy and Zhang, 2023]. The capabilities of ChatGPT
in various economic and professional contexts are explored in several studies. [Cowen and
Tabarrok, 2023] and [Korinek, 2023] discuss the model’s role in economics education and
research. [Hansen and Kazinnik, 2023] focuses on how ChatGPT interprets Fedspeak, the
complex language used by the Federal Reserve. In a similar vein, [Lopez-Lira and Tang, 2023]
delves into how to effectively prompt the model for stock return forecasts. Additionally, [Noy
and Zhang, 2023] highlights the model’s enhancement of productivity in professional writ-
ing, while [Yang and Menczer, 2023] examines its ability to identify credible news sources.
Beside the increasing number of use of LLMs for sentiment analysis, using news sentiment
in investment strategy is not new. Many studies involve using more classical methods like
lexical approaches for developing news sentiment indicator [Janu´ ario et al., 2022].
The development and utilization of sentiment indicators for trading strategies have also
seen significant progress. The study A Deep Learning Approach with Extensive Sentiment
Analysis for Quantitative Investment by [Li et al., 2023] introduces an approach that incor-
3

porates news content for sentiment analysis in quantitative investment, achieving interesting
annualized returns. In the realm of cryptocurrency, [Yeoh et al., 2023] analyze the impact
of news sentiment on the prices of cryptocurrencies using the FinBERT model for financial
sentiment analysis. Their findings indicate an influence of sentiment on price movements.
[Nakagawa et al., 2022] also contribute to this field with their investment strategy that ex-
ploits the lead-lag effect in company relationships using sentiment analysis. Furthermore,
[Yang, 2023] demonstrates the profitability of investment strategies based on analyst opinions
extracted from text analysis, suggesting an improved daily returns. The market stress is also
a widely studied index for combining it with news sentiment indicator and shows promising
results [Smales, 2015, 2016, Lin et al., 2023]. These studies collectively highlight the grow-
ing importance and effectiveness of sentiment analysis as a tool for developing investment
strategies.
3 Key contributions
In this paper, we present a strategy that combines a stress index with news sentiment anal-
ysis in a way that has never been addressed. We built a crisis-resistant strategy that yields
a constant performance over a long period. Our approach involves several key steps. Firstly,
we generate a signal by analyzing news sentiment, utilizing Bloomberg’s extensive daily mar-
ket summaries. This signal provides a broad, market-wide perspective, focusing on impactful
financial news. Our findings reveal that using this signal alone is not effective. However,
integrating it with the stress index significantly enhances our strategy, making it more con-
sistent and robust. This approach not only improves performance but also demonstrates the
broader applicability of the stress index strategy on a macroeconomic level.
The principal contribution of the paper are the following:
1. News alone is not enough: Although we use premium and heavily scrutinized data,
that is the Bloomberg’s daily market reports to create a news sentiment-based macro
4

indicator thanks to a multiple prompt approach using ChatGPT that has demonstrated
a statistical correlation with equity market returns, we experienced poor results when
using the news sentiment indicator alone. However, when combined with a stress
index combining other data type like volatility and credit spread, we get improved
performance over our benchmark of a naive long only strategy as well as other strategies
based purely on stress index or news.
2. It is crucial to have an alternative method when the news-based signal
becomes inefficient: We present a method to switch between the stress index and
the combination of the stress index and the news sentiments based on the persistence of
the overall performances of one strategy over the other one. This helps us to mitigate
periods of time where the news sentiment indicator becomes inefficient.
3. The method works on various equity markets: Through empirical validation,
we confirm that the integration of the stress index and news signal strategy, coupled
with the transition to a pure risk index in the event of prolonged underperformance,
consistently improves outcomes in various equities markets. This observation under-
scores the strategy’s ability to demonstrate persistent promising results, indicating its
capacity to generalize across major equity markets.
4 Data
To create an investment strategy on various equity markets leveraging financial news and a
stress index indicator, we need to collect multiple data: reliable financial news, stress index
and investment universe. Let us introduce each of these one at a time.
5

4.1 News Data
We use professional news from Bloomberg. Bloomberg provides daily market wraps, that are
daily summaries of the most important news. They are available since 2010 with growing
frequency after 2011. These texts contain both numerical and literal values and are gath-
ering the most informative content and news of the day. Daily market wraps are produced
multiple times during the day and specialized for the three regions: the US, Europe and
Asia. In order to have a consistent data set, we rely on the latest available news before the
European market opening, that is the end of day Asian market wraps. Hence, we collect
3627 daily market wraps. Each of these wraps is about 7000 characters, representing with
line breaks about 140 lines or about 5 pages long. Here is below an example of Bloomberg
Daily Market Wraps for the day. The range of the contents are any news that may impact
financial markets including equity, currencies, cryptocurrencies, bonds and commodities.
- Investor sentiment remains quite negative in China despite a rally in global stocks
during the past two months of 2023, Nomura Group analysts including Chetan Sethin
Singapore wrote in a client note. In China, there have been more signs of support for
the economy, but equity investors still do not appear convinced.
- Bond Traders Seize on 4% Yields, Confident Fed Rate Cuts Coming
- The Australian dollar fell 0.2% to $0.6701 ...
4.1.1 News signal
We follow the same methodology as in [Lefort et al., 2024], and use a two-step approach
to break the sentiment analysis into simpler subtasks for which chatGPT is better suited,
namely text summary and keywords identification. Here are the steps we follow:
1. First, we collect the daily market summaries from Bloomberg to stay updated on
financial trends.
6

2. Next, we ask ChatGPT to generate 15 notable headlines every day, ensuring we capture
the most significant events.
3. Once we have our headlines, we take a moment to assess their tone, deciding whether
they convey positive, negative, or indecisive sentiment. Hence, we calculate the daily
count of news evaluated in each category, resulting in a numerical score for each day.
It is a simple scale: -1 points for a negative sentiment, 0 for indecisive, and +1 for the
the days that are positively charged.
4. With these scores in hand, we don’t just look at one day in isolation; we add them up
across a 10-day period to get a broader view of the market’s mood. By averaging these
daily scores over 10 days, we’re able to smooth out the ups and downs and pinpoint
the general trend in news sentiment.
5. We then apply a statistical method called z-scoring to this 10-day sentiment average,
which helps us understand how strongly the news is leaning compared to the norm.
6. The final transformation involves calculating the mean of the z-scored signal over the
preceding 10 days.
7. Finally, we obtain a simple binary news indicator. If the z-score shows a positive
trend, we set it up as 1, indicating a thumbs-up for market sentiment. If the trend dips
negative, we set it to 0, signaling a more cautious outlook. This binary indicator serves
as a quick reference to gauge the overall sentiment in the financial news, allowing us
to make more informed decisions based on the prevailing mood in the market.
4.2 Stress Index
We rely on the stress index as presented in [Guilleminot et al., 2014] to capture contagion
effects in the market and anticipates future crisis. The indicator is documented to be pre-
dictive since it aims at detecting period of high volatility. We prefer this financial stress
7

indicator to the VIX as it has numerous advantages in detecting market contagion:
• Comprehensive Risk Analysis: The stress index combines a broad range of market
prices of risk, including CDS contracts, providing a more detailed view of market stress
compared to the VIX, which focuses mainly on S&P 500 index options.
• Enhanced Normalization Techniques : It employs z-score based normalization,
facilitating more effective comparability across various markets, thereby allowing for a
nuanced understanding of stress levels in different market segments.
• Detection of Market Contagion: It is specially designed to capture interconnected-
ness and contagion in financial markets, reflecting the complex dynamics often missed
by other indicators like the VIX.
• Detection of Crises : Incorporating CDS contracts from the main banks, insurances
and governments enables it to capture signals related to crises.
4.2.1 Stress Signal computation
The step to compute the stress index are the following:
1. We start by gathering market data for a variety of assets, which includes indicators
like the VIX index, TED spread, and CDS index, along with the volatility data for
major equity, bond, and commodity markets.
2. Next, we calculate the price of risk for each asset by standardizing the data with
z-scoring, which adjusts for the variability and scales the risk price in terms of its
deviation from the mean.
3. Then, we aggregate these z-scores by their respective categories such as equities, emerg-
ing bonds, government bonds, financial stocks, foreign exchange, commodities, interest
rates, and corporate credit to form category-specific stress indicators.
8

4. We take the average of these category-specific stress indicators to compile a compre-
hensive stress index that reflects the overall market conditions.
5. Finally, we scale the resulting average to fall between 0 and 1 by applying the cumula-
tive distribution function (norm.cdf) to the computed stress index, which normalizes
our final index value.
Because the stress index final result is a number between 0 and 1 thanks to the cumulative
distribution function of the normal distribution, we directly get a stress index signal.
4.3 Markets Tested
We test the strategy on six different equity markets: NASDAQ, S&P500, Nikkei, Euro Stoxx,
and Emerging Markets from January 2005 to 2024.
We compare the strategy on three cases:
1. The S&P500 alone.
2. The NASDAQ alone.
3. An equally weighted basket of the aforementioned six equity markets.
5 Experiments
5.1 Transaction Costs
To have very realistic simulations, we incorporate linear transaction costs, denoted by b
equals to 2 basis points for all our strategy ( b = 0 .0002). To put some mathematical
notations, assuming we have n assets whose weights are denoted by ( wi t)i=1,...,n and that
the daily returns of our assets are denoted by ( ri t)i=1,...,n, we compute our strategy value
9

recursively with the convention that the strategy starts at 1 at time 0: S0 = 1 as follows:
St = St−1 × (1 +
nX
i=1
wi t−1 × ri t − b|wt − wt−1|) (1)
5.2 The six different strategies
In order to evaluate whether the news signal is predictive or not, we compare six strategies
and run in total eighteen experiments as we compare these strategies over 3 different markets,
namely the US market by testing these strategies on the NASDAQ, the S&P 500, and an
equally weighted strategy combining the 6 major equity markets presented in section 4.3.
Here is the list of the 6 different strategies:
1. Long only: also referred to as the Benchmark in our comparison figures, this strategy
takes a long only position on the tested markets. We term this the Benchmark be-
cause our aim is to assess whether the other quantitative strategies exhibit superior
performance compared to this one.
2. VIX: Weights are directly related to the VIX signal where we assume that periods of
stress are identified by a VIX level above its 80 percentile which is around 26 percents.
3. SI for Stress Index: Weights are directly related to the stress index signal.
4. News: Weights are directly related to the news signal
5. SI News: Weights are obtained by the straighforward multiplication of the two signals,
namely the stress index times the news signal.
6. Dynamic SI News: this strategy is a dynamic selection between the strategy based on
stress index with news and the strategy using the stress index alone. More details can
be found in the section 5.3
In total we have 18 experiments as we compare these 6 strategies over the three cases
listed below:
10

1. Test on the NASDAQ.
2. Test on the S&P 500.
3. Test on the 6 major world equity markets.
Also to compare these strategies with a naive long only strategy, we also compute a long
only strategy that shares the same volatility as the better performing strategy. Hence, we
calculate ex-post the volatility of our best strategies and rescale the benchmark to have the
same volatility to compare track records with the benchmark in a volatility consistent way.
5.3 Dynamic Strategy Selection
The primary goal involves dynamically shifting between two investment strategies: one only
reliant on the stress index (SI) and another that incorporates news signals alongside the
stress index (SI+News). This strategic alternation aims to navigate efficiently through pe-
riods where the inclusion of news signals doesn’t substantially improve the performance of
the strategy compared to using the stress index alone. Empirical observations reveal a con-
sistent pattern: the SI+News strategy either significantly outperforms or underperforms the
SI-only strategy. Consequently, a strategic selector mechanism has been developed. This
mechanism computes the Sharpe ratio (defined as the ratio of the excess return over the
annualized volatility as in [Sharpe, 1966, 1975]) over a span of 250 observations, equivalent
to an annual rolling period, for the preceding month and consequently selects the strategy
that demonstrated superior performance for the forthcoming month. Notably, there are
intervals where the SI-only strategy surpasses the combined SI+News strategy. The news
signals predominantly act as a performance enhancer during specific scenarios, particularly
in times of crisis.
To elucidate this strategic selection, refer to Table 1. For each month, the Sharpe ra-
tios of the two strategies are calculated. The strategy for the subsequent month is chosen
based on the higher Sharpe ratio. For example, in December 2022, the SI+News strategy,
11

with a Sharpe ratio of 0.9, surpasses the SI-only strategy, which has a Sharpe ratio of 0.4.
Consequently, for December, January, and February, the dominant SI+News strategy is se-
lected. Conversely, in March and April, the SI-only strategy becomes dominant, leading to
its selection in April and May.
Table 1: Illustration of the Method for Switching Between the SI and SI+News Strategies
Month Sharpe SI Sharpe SI+News Selected Strategy
Dec 2022 0.4 0.9 . . .
Jan 2023 -0.1 0.7 SI+News
Feb 2023 0.2 0.5 SI+News
Mar 2023 0.5 0.1 SI+News
Apr 2023 1.2 0.6 SI
May 2023 . . . . . . SI
. . . . . . . . . . . .
To validate the predictive efficacy of each strategy, it is necessary to demonstrate that
the strategy selection exhibits a degree of persistence. The primary indicator of predictive
capability is the frequency of selection for each strategy. Over the period from 2011 to 2024,
the SI-only strategy was selected 71% of the time, while the SI+News strategy was chosen
29% of the time. A random selection mechanism would yield a 50% selection rate for each
strategy. Additionally, a graphical representation of the strategy selection demonstrates that
the SI+News strategy is chosen primarily during specific periods, suggesting that the news
signal is particularly beneficial during certain times.
6 The results
We test our six different strategies from January 2005 to January 2024, hence testing them
over 19 years. Our comparative analysis, as detailed in tables 2, 3, and 4, highlights some
consistency in the comparison of the different investment strategies for the S&P 500, NAS-
DAQ, and major equity markets with the uniform outperformance of the Dynamic SI+News
strategy in terms of Sharpe and Calmar ratios across all markets. It underscores its superior
12

risk-adjusted returns and drawdown management. In the three tables, in order to have short
column name, we denote Sharpe for the Sharpe ratio, Calmar for the Calmar ratio, Vol for
the annualized volatility and Max DD for the maximum drawdowns. We recall that the
Calmar ratio is defined as the annualized return over the maximum drawdowns (see [Young,
1991]).
Table 2: Comparative Analysis of Investment Strategies for the S&P 500
Strategy Sharpe Calmar Vol Max DD Turnover
Dynamic SI+News 0.81 0.56 7.5% 11% 8.6
SI 0.70 0.51 8.0% 11% 7.7
SI+News 0.53 0.30 6.2% 11% 13.4
Long Only 0.45 0.13 7.5% 27% n.a.
VIX 0.42 0.17 8.9% 22% 18.5
News 0.42 0.15 10.6% 29% 17.9
In more details, in the S&P 500 (Table 2), the Dynamic SI+News strategy achieves not
only the highest Sharpe ratio (0.81) but also the highest Calmar ratio (0.56). This improve-
ment of Sharpe ratio is quite important as the benchmark strategy (the long only strategy)
only achieves a Sharpe ratio of 0.45, making the Sharpe ratio improvement quite substantial.
Similarly, in the NASDAQ market (Table 3), the same strategy shows a remarkable Sharpe
ratio of 0.89, further reinforcing its efficacy in a tech-heavy index. The analysis for the major
equity markets (Table 4) also corroborates the superiority of the Dynamic SI+News strategy,
particularly in managing market downturns, as evidenced by its lower maximum drawdown
(Max DD) compared to other strategies like News and VIX.
If we refine our analysis on the Sharpe ratio, we can also notice that the strategy based on
the Stress index alone always comes second indicating that the signals emitted by the stress
index seem quite robust and more effective than the ones using the VIX index. Regarding
turnover, which measures the frequency of trading within the portfolio, we observe notable
differences across strategies. For instance, in the S&P 500 (Table 2), the ’SI+News’ strategy
exhibits the highest turnover rate at 13.4, indicating a more active trading approach. This
contrasts with strategies like ’SI’ and ’Dynamic SI News’ which have lower turnover rates,
13

suggesting a more passive strategy. The buy and hold strategy has by definition no turnover
as we hold the position for ever. It is interesting to note that the Stress Index based strategy
is effectively more moderate in terms of turning the position compared to the VIX based
strategy.
Table 3: Comparative Analysis of Investment Strategies for the NASDAQ
Strategy Sharpe Calmar Vol Max DD Turnover
Dynamic SI+News 0.89 0.62 9.2% 13% 8.6
SI 0.84 0.53 9.8% 16% 7.6
Long Only 0.62 0.20 9.2% 28% n.a.
SI+News 0.61 0.38 7.5% 12% 13.4
VIX 0.58 0.25 11.3% 27% 18.5
News 0.43 0.15 12.3% 34% 17.9
Table 4: Comparative Analysis of Investment Strategies for the major equity markets
Strategy Sharpe Calmar Vol Max DD Turnover
Dynamic SI+News 0.85 0.44 6.8% 13% 8.5
SI 0.71 0.39 7.2% 13% 7.7
SI+News 0.61 0.20 5.5% 17% 13.4
Long Only 0.52 0.13 6.8% 28% n.a.
VIX 0.42 0.15 8.4% 23% 18.4
News 0.32 0.09 8.1% 29% 16.2
Similarly, in the NASDAQ (Table 3) and major equity markets (Table 4), the ’VIX’ and
’News’ strategies are characterized by higher turnover rates (18.5 and 17.9 for NASDAQ, 18.4
and 16.2 for major equity markets, respectively), again reflecting a more active management
style. This frequent trading could be indicative of an attempt to capitalize on short-term
market movements.
In terms of the Calmar ratio, which assesses the risk-adjusted performance of an in-
vestment by comparing the average annual compounded rate of return and the maximum
drawdown, the ’Dynamic SI+News’ strategy consistently outperforms others across all mar-
kets. This is evident from its higher Calmar ratios (0.56 for S&P 500, 0.62 for NASDAQ, and
0.44 for major equity markets). The superior Calmar ratios suggest that this strategy not
14

only provides higher returns but also does so with less risk, as indicated by lower maximum
drawdowns.
In contrast, strategies like ’Long Only’ and ’News’ show lower Calmar ratios, implying
that they bear a higher risk (as seen in their higher maximum drawdowns). This could be
a critical factor for investors who are risk-averse and prefer strategies that limit potential
losses.
Figures 1, 2, and 3 provide a visual representation of these findings and compare the best
performing strategy namely the ’Dynamic SI+News’ strategy versus the passive long only
benchmark. The subplot in all figures 1, 2, and 3 reveal how the Dynamic SI+News strategy
dynamically adjusts its allocation, contributing to its robust performance.
All in all, when compiling our 18 experiments, our analysis demonstrates the effectiveness
of the Dynamic SI News strategy across different markets, with its ability to adapt to market
conditions and maintain superior performance metrics standing out as a key takeaway.
Additionally we provide in the appendix figures 4 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
15 the comparative performance of other investment strategies over time, alongside their
corresponding allocations and over the 3 different market universes, namely the S&P 500,
the NASDAQ, and Major Equities Markets. For each figure, we give as the top plot the
temporal performance comparison with the benchmark, the long only strategy, while the
subplot details the overall allocation.
Figure 4 illustrates the performance of a news-based strategy against a naive long-only
strategy within the S&P 500 universe. This figure highlights the temporal evolution of the
strategy’s effectiveness in comparison to the benchmark. In Figure 5, we observe a similar
analysis within the NASDAQ universe. The subplot is particularly insightful for under-
standing the allocation differences underlined by the news-based strategy. Figure 6 extends
this comparison to the Major Equities Markets, offering a broader view of the strategy’s
applicability in a global context.
Figures 7, 8, and 9 delve into strategies that amalgamate news with stress index data.
15

Figure 1: Comparison of the dynamic strategy combining Stress index and News and Stress
index alone using persistence of overperformance of one strategy over the other one versus
the naive long only strategy (rescaled at the same volatility) for the S&P 500 universe. The
first plot compares the two strategies over time while the subplot provides the corresponding
overall allocation.
16

Figure 2: Comparison of the dynamic strategy combining Stress index and News and Stress
index alone using persistence of overperformance of one strategy over the other one versus the
naive long only strategy (rescaled at the same volatility) for the NASDAQ 100 universe. The
first plot compares the two strategies over time while the subplot provides the corresponding
overall allocation.
17

Figure 3: Comparison of the dynamic strategy combining Stress index and News and Stress
index alone using persistence of overperformance of one strategy over the other one versus the
naive long only strategy (rescaled at the same volatility) for the Major Equities Markets. The
first plot compares the two strategies over time while the subplot provides the corresponding
overall allocation.
18

These figures offer an intriguing perspective on the synergistic effects of combining these two
data sources across different market universes.
Figures 10, 11, and 12 focus on strategies purely based on the stress index. These plots
are crucial for understanding the standalone impact of the stress index on the investment
strategy.
Finally, Figures 13, 14, and 15 compare the VIX-based strategy with the naive long-
only approach. The temporal comparison and allocation subplots underscore the unique
characteristics and performance of the VIX-based strategy in different market settings.
6.1 Intuition of the results
The integration of news signals with the stress index in investment strategies, as demon-
strated in the S&P 500, NASDAQ, and major equity markets (Tables 2, 3, and 4), makes
a lot of sense and is grounded in both empirical results and theoretical underpinnings from
financial literature.
6.1.1 Added Values of News
Intuitively incorporating news read by a machine into an investment strategy based on the
stress index can improve the strategy’s effectiveness for several reasons:
• Signal Reactivity: News can detect new trend or sentiment in the markets quicker.
This is effectively illustrated by the higher turnover of the pure news strategy.
• Objectivity and Consistency: Unlike human analysts, reading news by a machine
is less prone to cognitive biases or emotional responses. The news signal should be
quite consistent and objective.
• Quality of the data: Since we use Bloomberg market wraps that are supposed to
capture all major news, the news signal should be triggered by any weak signals from
news.
19

• Hidden pattern catching: The news signal is capable of capturing more complex
relationships between news items than a human can.
6.1.2 Empirical Evidence
As already presented, the Dynamic SI+News strategy, which combines both news signals
and stress index data, shows a remarkable performance across various markets. In the S&P
500, this strategy not only achieves the highest Sharpe ratio (0.81) but also a significant
Calmar ratio (0.56), surpassing the benchmark long only strategy’s Sharpe ratio of 0.45.
6.1.3 Theoretical Insights
Combining news signals with the stress index aligns with the principles of Behavioral Fi-
nance, particularly as detailed in [Barber and Odean, 2008]. Their research demonstrates
how news and media attention significantly influence investor behavior, often leading to ir-
rational decision-making based on recent news rather than long-term trends. This indicates
a potential edge in combining news analysis with stress indices, which act as barometers for
market sentiment and stress. By integrating recent news, which potentially triggers over-
reactions or underreactions, with the more steady and sentiment-focused stress indices, a
more balanced and informed investment the strategy can be improved by capitalizing on the
quick, news-driven shifts in investor behavior while being anchored by the broader, more
stable market insights provided by the stress index.
6.1.4 Role of Stress Index
The stress index alone consistently ranks second in terms of Sharpe ratio across different
markets, underscoring its robustness. It acts as a gauge of market tension and uncertainty,
often signaling impending market corrections or volatility, making it a crucial component of
a holistic investment strategy.
20

6.1.5 Turnover Analysis
Analyzing turnover rates sheds light on strategy aggressiveness. The ’SI+News’ strategy
exhibits the highest turnover (13.4 in the S&P 500), indicative of an active trading approach.
This is quite logical as the news based signals is supposed to react very quickly. The same
applies to the VIX strategy that seems to overreact to any high volatility environement. In
contrast, ’SI’ and ’Dynamic SI+News’ strategies demonstrate more moderation, suggesting
a balanced approach that leverages the predictive power of stress indices while avoiding
excessive trading.
6.1.6 Impact on Maximum Drawdown and Calmar Ratio
The integration of news signals into the stress index strategy has a significant impact on the
maximum drawdown (Max DD) and, consequently, on the Calmar ratio. This is evident in
the comparative analysis of investment strategies across various markets (Tables 2, 3, and
4).
Max DD Reduction The Dynamic SI+News strategy consistently demonstrates a lower
Max DD compared to other strategies, especially the News-only strategy. For example, in
the S&P 500, the Max DD for Dynamic SI+News is 11%, markedly lower than the 29% Max
DD for the News strategy. This reduction in Max DD is crucial for risk-averse investors and
indicates enhanced strategy stability during market downturns.
Enhanced Calmar Ratio The Calmar ratio, which measures the return per unit of down-
side risk, is notably higher in the Dynamic SI+News strategy across all markets. For instance,
in the S&P 500, this strategy achieves a Calmar ratio of 0.56, surpassing the Stress Index
(SI) alone at 0.51 and significantly outperforming the News strategy at 0.15. This trend is
consistent across the NASDAQ and major equity markets.
21

Rationale for Improvement Incorporating news into the stress index strategy enhances
its ability to adapt to market sentiments and trends rapidly. News provides real-time insights
and immediate market reactions, which, when combined with the stress index’s broader mar-
ket sentiment gauge, allows for a more dynamic and responsive strategy. This combination
effectively mitigates risks during volatile periods, leading to a reduced Max DD and an
improved Calmar ratio.
Literature Support This finding aligns with the existing financial literature that empha-
sizes the importance of combining various types of market information to achieve a more
comprehensive and robust investment strategy. For instance, [Tetlock, 2007] highlights how
media and news content significantly influence investor sentiment and stock market dy-
namics, underscoring the value of incorporating real-time news into investment strategies
[Tetlock, 2007]. Similarly, Baker et al. [2016] in their study provide insights into how eco-
nomic policy uncertainty, derived from news media coverage, impacts market conditions and
investor behavior, further justifying the inclusion of news data alongside stress index infor-
mation in strategic decision-making[Tetlock, 2007]. Additionally, Da et al. [2011] through
their work emphasize the influence of media attention on stock prices and trading volumes,
suggesting that the attention garnered by specific news can be pivotal in financial market
movements and should be integrated into comprehensive investment strategies [Da et al.,
2011]. These studies collectively support the synergy between real-time news and stress
index data, enhancing the ability to capture and react to market anomalies and stress con-
ditions, thereby improving the overall risk-adjusted performance of the strategy.
7 Conclusion
This paper introduces a novel risk-on, risk-off strategy for the stock market, leveraging
a financial stress indicator combined with sentiment analysis performed by ChatGPT on
Bloomberg’s daily market summaries. The strategy enhances market stress forecasts, which
22

are based on volatility and credit spreads, using financial news sentiment derived from GPT4.
This results in a significant improvement in performance, evidenced by a higher Sharpe ratio
and reduced maximum drawdowns. The method’s effectiveness is not limited to a single
market; it is consistent across various equity markets, including the NASDAQ and S&P
500, as well as six other major equity markets, indicating its broad applicability. There
are many potential directions for future research. Future works could investigate if the
strategy can be applied to different financial markets such as commodities, bonds, and
foreign exchange markets, to test its versatility and robustness. Additionally, it would be
worthwhile to investigate whether additional data sources, such as social media sentiment
or macroeconomic indicators, could further improve the strategy’s performance. Identifying
patterns in economic events where the news signal is most effective is also a potential avenue
for future research.
8 Bibliographical References
References
Dogu Araci. Finbert: Financial sentiment analysis with pre-trained language models. CoRR,
abs/1908.10063, 2019. URL http://arxiv.org/abs/1908.10063.
Stefano Baccianella, Andrea Esuli, and Fabrizio Sebastiani. SentiWordNet 3.0: An enhanced
lexical resource for sentiment analysis and opinion mining. In Nicoletta Calzolari, Khalid
Choukri, Bente Maegaard, Joseph Mariani, Jan Odijk, Stelios Piperidis, Mike Rosner,
and Daniel Tapias, editors, Proceedings of the Seventh International Conference on Lan-
guage Resources and Evaluation (LREC’10) , Valletta, Malta, May 2010. European Lan-
guage Resources Association (ELRA). URL http://www.lrec-conf.org/proceedings/
lrec2010/pdf/769_Paper.pdf.
23

Scott R Baker, Nicholas Bloom, and Steven J Davis. Measuring economic policy uncertainty.
The quarterly journal of economics , 131(4):1593–1636, 2016.
Brad M Barber and Terrance Odean. All that glitters: The effect of attention and news
on the buying behavior of individual and institutional investors. The review of financial
studies, 21(2):785–818, 2008.
Tyler Cowen and Alexander T. Tabarrok. How to Learn and Teach Economics with
Large Language Models, Including GPT. SSRN Electronic Journal , XXX(XXX):0–0, 3
2023. ISSN 1556-5068. doi: 10.2139/SSRN.4391863. URL https://papers.ssrn.com/
abstract=4391863.
Zhi Da, Joseph Engelberg, and Pengjie Gao. In search of attention. The journal of finance ,
66(5):1461–1499, 2011.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: pre-training
of deep bidirectional transformers for language understanding. CoRR, abs/1810.04805,
2018. URL http://arxiv.org/abs/1810.04805.
W Brooke Elliott, Stephanie M Grant, and Frank D Hodge. Negative news and investor
trust: The role of $ firm and # ceo twitter use. Journal of Accounting Research , 56(5):
1483–1519, 2018.
A Shaji George and AS Hovan George. A review of ChatGPT AI’s impact on several business
sectors. Partners Universal International Innovation Journal , 1(1):9–23, 2023.
Beno ˆ ıt Guilleminot, Jean-Jacques Ohana, and Steve Ohana. A new financial stress indicator:
properties and conditional asset price behavior. SSRN Electronic Journal , January 2014.
Available at SSRN: https://ssrn.com/abstract=2317321 or http://dx.doi.org/10.
2139/ssrn.2317321.
24

Anne Lundgaard Hansen and Sophia Kazinnik. Can ChatGPT Decipher Fedspeak? SSRN
Electronic Journal, XX(XX):XX, 3 2023. ISSN 1556-5068. doi: 10.2139/SSRN.4399406.
URL https://papers.ssrn.com/abstract=4399406.
Deniz Ikizlerli, Phil Holmes, and Keith Anderson. The response of different investor types to
macroeconomic news. Journal of Multinational Financial Management , 50:13–28, 2019.
Brenda A. Janu´ ario, Arthur Emanuel de O. Carosia, Ana Estela A. da Silva, and Guil-
herme P. Coelho. Sentiment analysis applied to news from the brazilian stock market.
IEEE Latin America Transactions, 20(3):512–518, 2022. doi: 10.1109/TLA.2022.9667151.
Neel Kant, Raul Puri, Nikolai Yakovenko, and Bryan Catanzaro. Practical text classification
with large pre-trained language models, 2018.
Colm Kearney and Sha Liu. Textual sentiment in finance: A survey of methods and models.
International Review of Financial Analysis , 33:171–185, 2014.
Anton Korinek. Language Models and Cognitive Automation for Economic Research. Cam-
bridge, MA , XX(XX):XX, 2 2023. doi: 10.3386/W30957. URL https://www.nber.org/
papers/w30957.
Baptiste Lefort, Eric Benhamou, Jean-Jacques Ohana, David Saltiel, Beatrice Guez, and
Damien Challet. Can ChatGPT Compute Trustworthy Sentiment Scores from Bloomberg
Market Wraps. Available at SSRN , January 2024. URL https://papers.ssrn.com/
sol3/papers.cfm?abstract_id=4688451.
Wang Li, Chaozhu Hu, and Youxi Luo. A deep learning approach with extensive senti-
ment analysis for quantitative investment. Electronics, 12(18):3960, 2023. doi: 10.3390/
electronics12183960. URL https://dx.doi.org/10.3390/electronics12183960.
Tse-Mao Lin, Jing-Long Yu, Jhih-Wei Chen, and Chin-Sheng Huang. Application of ma-
25

chine learning with news sentiment in stock trading strategies. International Journal of
Financial Research, 14:1, 05 2023. doi: 10.5430/ijfr.v14n3p1.
Alejandro Lopez-Lira and Yuehua Tang. Can ChatGPT Forecast Stock Price Movements?
Return Predictability and Large Language Models. SSRN Electronic Journal , XXX(XX-
XX):XX, 4 2023. ISSN 1556-5068. doi: 10.2139/SSRN.4412788. URL https://papers.
ssrn.com/abstract=4412788.
Tim Loughran and Bill McDonald. When is a liability not a liability? textual analysis,
dictionaries, and 10-ks. The Journal of finance , 66(1):35–65, 2011.
Kei Nakagawa, Shingo Sashida, and Hiroki Sakaji. Investment strategy via lead lag effect
using economic causal chain and ssestm model. In IIAI International Conference on
Advanced Applied Informatics, 2022. doi: 10.1109/IIAIAAI55812.2022.00065. URL https:
//dx.doi.org/10.1109/IIAIAAI55812.2022.00065.
Shakked Noy and Whitney Zhang. Experimental Evidence on the Productivity Effects of
Generative Artificial Intelligence. SSRN Electronic Journal , XX(XX):XX, 3 2023. doi:
10.2139/SSRN.4375283. URL https://papers.ssrn.com/abstract=4375283.
OpenAI. Gpt-4 technical report, 2023.
Robert P Schumaker and Hsinchun Chen. Textual analysis of stock market prediction us-
ing breaking financial news: The azfin text system. ACM Transactions on Information
Systems (TOIS) , 27(2):1–19, 2009.
William F. Sharpe. Mutual fund performance. The Journal of Business , pages 119–138,
January 1966.
William F. Sharpe. Adjusting for risk in portfolio performance measurement. Journal of
Portfolio Management , pages 29–34, Winter 1975.
26

L.A. Smales. Risk-on / risk-off: Financial market response to investor fear. Journal of
International Financial Markets, Institutions and Money , 2015. School of Economics &
Finance, Curtin University, Australia.
Lee A. Smales. Time-varying relationship of news sentiment, implied volatility and stock re-
turns. Applied Economics , 48(51):4942–4960, November 2016. doi: 10.1080/00036846.
2016.116. URL https://ideas.repec.org/a/taf/applec/v48y2016i51p4942-4960.
html.
Yixuan Tang, Yi Yang, Allen H Huang, Andy Tam, and Justin Z Tang. Finentity: Entity-
level sentiment classification for financial texts, 2023.
Paul C. Tetlock. Giving Content to Investor Sentiment: The Role of Media in the Stock
Market. The Journal of Finance , 62(3):1139–1168, 6 2007. ISSN 1540-6261. doi: 10.
1111/J.1540-6261.2007.01232.X. URL https://onlinelibrary.wiley.com/doi/full/
10.1111/j.1540-6261.2007.01232.x.
Frank Z Xing, Erik Cambria, and Roy E Welsch. Natural language based financial forecast-
ing: a survey. Artificial Intelligence Review , 50(1):49–73, 2018.
Cheol-Won Yang. Investment strategy via analyst report text mining. Journal of Data
and Qualitative Science , 2023:1–12, 2023. doi: 10.1108/jdqs-09-2022-0022. URL https:
//dx.doi.org/10.1108/jdqs-09-2022-0022 .
Kai-Cheng Yang and Filippo Menczer. Large language models can rate news outlet credi-
bility. Technical report, arxiv, 4 2023. URL https://arxiv.org/abs/2304.00228v1.
Eik Den Yeoh, Tinfah Chung, and Yuyang Wang. Predicting price trends using sentiment
analysis: A study of stepn’s socialfi and gamefi cryptocurrencies. Cryptocurrency Mar-
kets, 44, 2023. doi: 10.37256/cm.4420232572. URL https://dx.doi.org/10.37256/cm.
4420232572.
27

T.W. Young. Calmar ratio: A smoother tool. Futures, 20, Nr 1:40–41, 1991.
Lei Zhang, Shuai Wang, and Bing Liu. Deep learning for sentiment analysis: A survey.Wiley
Interdisciplinary Reviews: Data Mining and Knowledge Discovery , 8(4):e1253, 2018.
28

Figures
Figure 4: Comparison of the strategy based only on news versus the naive long only strategy
(rescaled at the same volatility) for the S&P 500 universe. The first plot compares the two
strategies over time while the subplot provides the corresponding overall allocation.
29

Figure 5: Comparison of the strategy based only on news versus the naive long only strategy
(rescaled at the same volatility) for the NASDAQ 100 universe. The first plot compares the
two strategies over time while the subplot provides the corresponding overall allocation.
30

Figure 6: Comparison of the strategy based only on news versus the naive long only strategy
(rescaled at the same volatility) for the Major Equities Markets. The first plot compares the
two strategies over time while the subplot provides the corresponding overall allocation.
31

Figure 7: Comparison of the strategy combining Stress index and News versus the naive
long only strategy (rescaled at the same volatility) for the S&P 500 universe. The first plot
compares the two strategies over time while the subplot provides the corresponding overall
allocation.
32

Figure 8: Comparison of the strategy combining Stress index and News versus the naive long
only strategy (rescaled at the same volatility) for the NASDAQ 100 universe. The first plot
compares the two strategies over time while the subplot provides the corresponding overall
allocation.
33

Figure 9: Comparison of the strategy combining Stress index and News versus the naive long
only strategy (rescaled at the same volatility) for the Major Equities Markets. The first plot
compares the two strategies over time while the subplot provides the corresponding overall
allocation.
34

Figure 10: Comparison of the Stress Index based strategy versus the naive long only strategy
(rescaled at the same volatility) for the S&P 500 universe. The first plot compares the two
strategies over time while the subplot provides the corresponding overall allocation.
35

Figure 11: Comparison of the Stress Index based strategy versus the naive long only strategy
(rescaled at the same volatility) for the NASDAQ 100 universe. The first plot compares the
two strategies over time while the subplot provides the corresponding overall allocation.
36

Figure 12: Comparison of the Stress Index based strategy versus the naive long only strategy
(rescaled at the same volatility) for the Major Equities Markets. The first plot compares the
two strategies over time while the subplot provides the corresponding overall allocation.
37

Figure 13: Comparison of the VIX based strategy versus the naive long only strategy
(rescaled at the same volatility) for the S&P 500 universe. The first plot compares the
two strategies over time while the subplot provides the corresponding overall allocation.
38

Figure 14: Comparison of the VIX based strategy versus the naive long only strategy
(rescaled at the same volatility) for the NASDAQ 100 universe. The first plot compares
the two strategies over time while the subplot provides the corresponding overall allocation.
39

Figure 15: Comparison of the VIX based strategy versus the naive long only strategy
(rescaled at the same volatility) for the Major Equities Markets. The first plot compares the
two strategies over time while the subplot provides the corresponding overall allocation.
40
