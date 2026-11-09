---
title: 'MM-FinEval: A Multi-Task Multimodal Benchmark for Real-World Financial Forecasting'
url: https://arxiv.org/abs/2609.38523
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Dong Shu
- Yanguang Liu
- Huopu Zhang
- Saisai Hu
- Haiyan Zhao
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.38523
pages: 23
chars: 93609
fetched_at: '2026-11-08T13:24:42+00:00'
kb_version: 1
---

# MM-FinEval: A Multi-Task Multimodal Benchmark for Real-World Financial Forecasting

MM-FinEval: A Multi-Task Multimodal Benchmark
for Real-World Financial Forecasting
Dong Shu1, Yanguang Liu2, Huopu Zhang 3, Saisai Hu 4, Haiyan Zhao 2, Hekun Huang 2, Mengnan Du 5
1Northwestern University 2New Jersey Institute of Technology 3Georgia Institute of Technology
4Pace University 5The Chinese University of Hong Kong, Shenzhen
Abstract
Financial forecasting from earnings conference
calls requires models to reason over complex
corporate disclosures, market expectations, and
subtle communication signals. However, exist-
ing financial benchmarks are often limited to
unimodal inputs or single-task settings, mak-
ing it difficult to evaluate whether multimodal
large language models (LLMs) can support real-
world financial analysis. In this paper, we in-
troduce MM-FinEval, a novel benchmark de-
signed to evaluate multimodal LLMs across
multiple financial tasks. MM-FinEval spans
a diverse timeline from 2019 to 2022. The
entire proposed dataset contains 2,045 S&P
500 conference earning calls as inputs and 12
financial task labels as outputs. Each input
contains three modalities: a word-to-word text
transcript of the earning call, the corresponding
presentation slides used during the call, and
the entire audio recording. To establish a rig-
orous evaluation framework, we analyze 19
baseline models across three distinct model cat-
egories: Image-Text, Audio-Text, and Any-to-
Any configurations. We observe that small-size
Any-to-Any models processing all three modal-
ities achieve strong performance, even when
compared against larger proprietary models re-
stricted to two-modality inputs. This indicates
that our tri-modal dataset design introduces
useful, non-redundant information. These re-
sults validate that text, audio, and visual data
serve as important, complementary signals that
mimic the decision-making process of expert
human analysts. The MM-FinEval dataset is
available at https://github.com/Tizzzzy/
MM-FinEval.
1 Introduction
Earnings conference calls are important events for
public companies, serving as a primary channel
for management to communicate financial perfor-
mance, strategic outlooks, and operational updates
to the market. The quality of a company’s earnings
conference call is directly linked to the next-day
stock market performance. In practice, financial
analysts rely heavily on these events, extracting
signals from company presentations and Q&A ses-
sions to analyze corporate health and forecast fu-
ture performance. Concurrently, there is a rapidly
growing trend of leveraging LLMs to analyze fi-
nancial markets and automate data processing (Wu
et al., 2023; Li et al., 2023; Huang et al., 2023;
Yang et al., 2023). If LLMs can be trained to suc-
cessfully capture the dense, multi-layered informa-
tion presented during these calls, financial institu-
tions could benefit from an automated and scalable
AI finance analysis pipeline that has historically
required substantial human analysis.
Despite the rapid advancement of LLMs, exist-
ing financial models remain constrained by their
reliance on uni-modal architectures and their ten-
dency to focus on narrow, specific financial tasks
(He and Zhang, 2025; Zhu et al., 2025; Liang and
Carrasco Kind, 2025; Konstantinidis et al., 2024;
Liu et al., 2025b). A major reason for this limita-
tion is that the majority of current financial datasets
are heavily skewed toward a single modality, such
as pure text or numerical time-series data (Chen
et al., 2021; Lai et al., 2025; Shah et al., 2023;
Dong et al., 2024). Furthermore, even when recent
datasets incorporate multimodal elements beyond
text, they are typically restricted to a specific task
(Shu et al., 2025a; Li et al., 2020; Luo et al., 2025;
Shu et al., 2025b). This combination of unimodal
and task-specific training data severely restricts
financial LLMs to learn from additional contex-
tual information, ultimately limiting their broader
applicability in complex, real-world financial envi-
ronments.
To bridge this gap, we propose MM-FinEval, a
large-scale, multi-modal, and multi-label financial
benchmark dataset designed specifically for earn-
ings call analysis. Spanning a period from 2019 to
2022, the dataset encompasses a total of 2045 data
1
arXiv:2609.38523v1  [cs.LG]  29 Sep 2026

All
Publicly
Traded
Firms
in
US
Firm
Collection
AAPL
MSFT
AMZN
NVDA
GOOGL
KO
WMT
...
Audio
Recordings
PPT
Slides
Web
Scrape
Text
Transcript
Cumulative
Abnormal
Return
End-of-Month
Corporate
Bond
Return
Last
5
Days
of
Month
Corporate
Bond
Return
Last
Trading
Day
of
Month
Corporate
Bond
Return
3-Day
Future
Volatility
3-Day
Pre-event
Volatility
7-Day
Future
Volatility
7-Day
Pre-event
Volatility
15-Day
Future
Volatility
15-Day
Pre-event
Volatility
30-Day
Future
Volatility
30-Day
Pre-event
Volatility
MM-FinEval
Labels
Operator:
Good
day
exeryone
...
Executives:
This
is
a
historic
...
Analysts:
I
want
to
ask
you
...
Figure 1: MM-FinEval Construction Pipeline. The dataset construction follows a three-stage process: assembling a
foundational collection of publicly traded US firms, systematically web-scraping synchronized tri-modal data (text
transcripts, audio recordings, and slides), and annotating the multimodal inputs with 12 financial task labels.
points from S&P 500 companies, with 450 from
2019, 273 from 2020, 499 from 2021, and 823
from 2022. Each data point integrates three modal-
ities: word-to-word text transcripts of the earnings
call, the corresponding raw earnings call audio, and
the accompanying presentation slide decks. Fur-
thermore, MM-FinEval is annotated with 12 labels,
providing a benchmark to evaluate the performance
of multimodal financial models. Through an ex-
tensive experiment with 19 state-of-the-art models,
we found that:
• Current LLMs exhibit a severe performance
gap between market return and volatility fore-
casting.
• Integrating all three modalities provides
performance advantage, proving that non-
redundant visual and audio information are
essential for replicating expert financial rea-
soning.
• Model performance on volatility tasks aligns
with the financial theory of information half-
life. As the forecasting horizon expands from
3 to 30 days, the earnings signal is rapidly
diluted by unpredictable market factors.
2 Related Work
2.1 Earnings Conference Call Datasets
Earnings conference calls are important events for
public companies because the quality of the infor-
mation disclosed during these presentations and
Q&A sessions is directly linked to next-day stock
market performance. Recently, researchers have
increasingly deployed machine learning models to
systematically interpret the information in these
calls (Sawhney et al., 2020b,a; Mathur et al., 2022;
Sawhney et al., 2020c), aiming to uncover quantita-
tive investment signals and making money. This ef-
fort to uncover quantitative investment signals has
motivated the community to publish specialized
datasets focusing on earnings conference calls. For
example, ECTSum (Mukherjee et al., 2022) pro-
vides benchmarks for bullet-point summarization
of highly verbose transcripts. FinNLI (Magomere
et al., 2025) is developed to assess logical deduc-
tion. SubjECTive-QA (Pardawala et al., 2024) mea-
sures the subjectivity of Q&A responses across
conference earning calls. Recent large text datasets
like STRUX (Lu et al., 2024) and DEC (Yu et al.,
2025) created for LLM-driven investment decision-
making.
However, these existing datasets remain con-
strained by their reliance on unimodal architectures,
do not include the acoustic and visual signals in-
herent in the actual conference call. EC (Qin and
Yang, 2019) which was the first dataset to combine
textual transcripts with raw audio recordings to pre-
dict financial risk. Building upon this, MAEC (Li
et al., 2020) scaled the available conference call
data and optimized to predict stock volatility. Dat-
sets such as Earnings-21 (Del Rio et al., 2021) and
ConEC (Huang et al., 2024) focus heavily on the
acoustic challenges of the domain, serving primar-
ily as benchmarks for automatic speech recognition
rather than broader financial reasoning. FinCall-
Surprise (Shu et al., 2025a), which provides con-
ference call text transcripts, audio, and slides, is
optimized exclusively for predicting earnings sur-
prises. Despite the success of these existing multi-
modal conference call datasets, they are limited
to a specific financial task. This severely restricts
the ability of financial LLMs to learn from addi-
tional contextual information, directly motivating
2

the need for multi-label multi-modal benchmarks.
3 MM-FinEval Construction
The construction of MM-FinEval dataset follows
a three-stage pipeline designed to collect, synchro-
nize, and annotate data from multiple sources. As
illustrated in Figure 1, the first stage involves gath-
ering a set of liquid public firms in the United
States. To ensure data quality, we restrict the sam-
ple to companies with a market capitalization ex-
ceeding $1 billion and an average daily trading
volume above $50 million. This initial screening
process yielded a pool of over 4,000 companies.
In the second stage, we acquire data across the
three modalities for each firm’s earnings confer-
ence calls. We systematically web-scrape these
contents from official company websites. The col-
lected text transcripts are highly structured, featur-
ing clear speaker identifiers (operators, executives,
and analysts) alongside their corresponding state-
ments. Because most publicly traded firms host one
earnings call per fiscal quarter, we ensure temporal
consistency by manually aligning all data sources
according to their specific reporting dates. Fur-
thermore, we cross-reference the conference call
titles to verify that the transcript, audio recording,
and presentation slides all originate from the exact
same event, ensuring synchronization across our
multimodal dataset.
3.1 Multi-Label Preliminaries
MM-FinEval benchmark includes 12 labels de-
signed to predict a company’s cumulative abnormal
return, stock volatility, and corporate bond returns
based on its quarterly earnings call. The complete
labels are shown on the right side of Figure 1.
Cumulative Abnormal Return.Cumulative ab-
normal return (CAR) measures the market-adjusted
price reaction around an earnings call event (Hirsh-
leifer et al., 2009; Duan et al., 2018). For each firm
i and event date t, we first compute the abnormal
return by subtracting a benchmark market return
from the firm’s realized return:
ARi,t =R i,t −R m,t,(1)
where Ri,t denotes the stock return of firm i on
dayt, andR m,t denotes the corresponding market
return. We then aggregate abnormal returns over
an event window[t 1, t2]:
CARi,[t1,t2] =
t2X
t=t1
ARi,t.(2)
CAR reflects whether the information revealed in
the earnings call leads to a positive or negative
market reassessment of the firm. We include CAR-
based labels over multiple post-call windows to
evaluate whether models can infer short-term and
medium-term directional market reactions from
multimodal earnings-call information.
V olatility.V olatility measures stock-price fluctu-
ations over a finite period and is commonly used
as a measure of risk (Kogan et al., 2009). In our
study, the period is defined relative to the earnings
conference call using pre-event and post-event win-
dows of different lengths. Following Kogan et al.
(Kogan et al., 2009), volatility from day t−τ to
daytis defined as
v[t−τ,t] =
r Pτ
i=0(rt−i −¯r)2
τ ,(3)
where rt is the return on day t, ¯ris the mean
return over the period of day t−τ to day t.
rt =P t/Pt−1 −1 is the return price, with Pt denot-
ing the closing price on day t. While CAR captures
the direction of the market response, volatility cap-
tures stock-price instability regardless of whether
returns are positive or negative. The labelsfut_3d–
fut_30d and past_3d–past_30d measure post-
event and pre-event volatility, respectively, over
windows of 3, 7, 15, and 30 calendar days.
Corporate Bond Return.Corporate bond re-
turns capture the monthly performance of a firm’s
outstanding bonds and provide a debt-market mea-
sure of investors’ responses to information dis-
closed during earnings calls. The bond return data
are observed at the monthly level and are matched
to conference-call observations using the firm’s
stock ticker, recorded as COMPANY_SYMBOL, and the
bond trading month, recorded in DATE. Specifically,
monthly returns are computed as the percentage
change in the bond’s dirty price (clean price plus
accrued interest), adjusted for coupon payments
received during the holding period, following the
standard methodology in the corporate bond lit-
erature (Bessembinder et al., 2008; Jostova et al.,
2013). To account for differences in bond trading
frequency and liquidity, we consider three comple-
mentary return measures that differ only in their
3

Transcript (words) Slide (pages) Audio (sec)
Year Mini Max Avg. Mini Max Avg. Mini Max Avg. Total
2019 2477 15421 8837.90 1 156 25.97 1096.07 8870.97 3642.66 450
2020 2533 21894 9389.90 1 170 27.89 1404.06 7585.31 3859.25 273
2021 2784 15343 8998.85 1 113 27.47 1197.95 11938.89 3720.29 499
2022 2986 17717 8842.89 2 252 30.73 234.72 31393.57 3770.45 823
Table 1: Data statistics of the MM-FinEval. The dataset spans four years (2019–2022), with each conference call
containing three synchronized modalities: text transcripts, presentation slides, and audio recordings. We report the
minimum, maximum, and average values for each modality. Transcript length is measured in words, slides in pages,
and audio in seconds. The last column shows how much data we have for each year.
definition of the month-end price.RET_EOMis
calculated using the last observed transaction price
during the calendar month, regardless of the trading
date.RET_LDMuses the transaction price on the
last trading day of the month and is missing if the
bond does not trade on that day.RET_L5Muses
the last transaction price observed within the final
five trading days of the month, providing a balance
between month-end pricing and sample coverage.
4 Data Analysis
Table 1 presents a detailed statistical analysis of
our dataset, summarizing its scale and multimodal
structure. MM-FinEval has a total of 2045 data
spanning from 2019 to 2022. On average, an in-
dividual data features a text transcript of approxi-
mately 9,000 words, accompanied by a 27-page
presentation slide deck and an audio recording
spanning roughly 3,700 seconds. As illustrated
in Figure 2a, the content of these calls is con-
sistently structured around three primary speaker
roles: Operators, Executives, and Analysts. Op-
erators typically manage the flow of the event by
opening and closing the call. Executives, such as
the CEO and CFO, deliver the company’s financial
results and strategic outlook. Finally, Analysts rep-
resenting investment firms and financial institutions
ask questions to obtain more information into the
company’s operational and financial performance.
More data analysis including our label statistic is
in Appendix A.
5 Benchmark Settings
5.1 Baseline LLMs
To establish a comprehensive performance bench-
mark for MM-FinEval, we selected 19 state-of-the-
art open- and closed-source models. These models
were categorized into three architectural groups
based on their input capabilities.
The first group comprises Large Vision-
Language Models (LVLMs), which process both
image and text inputs. This group includes the
Qwen 3.5 series (spanning 2B to 35B parameters)
(Qwen Team, 2026a), the Qwen 3.6 series (27B and
35B) (Qwen Team, 2026b), Gemma 3n (Team et al.,
2024), and the Mistral 3 series (3B, 8B, and 14B)
(Jiang et al., 2023). It also includes proprietary
models: GPT-5.4, GPT-5.5, Claude 4.6 Sonnet,
and Claude 4.8 Opus. The second group consists
of Text-Audio Language Models, which process
both audio and text inputs, represented in our study
by V oxtral 24B (Liu et al., 2025a) and Moss 8B
(Team, 2026b). Finally, the third group features
Any-to-Any Models, which are natively equipped
to process all modalities, text, audio, and images,
simultaneously. This includes Gemma 4 E2B and
Gemma 4 E4B (Team, 2026a).
5.2 Benchmark Input Design
To systematically evaluate the performance of the
baseline models, we designed a customized input
and prompting strategy tailored to each modality.
The full set of prompts used in the experiments is
provided in Appendix B.
Image-Text Modality:Because the selected
baseline models represent the current state-of-the-
art, they all support extended context windows ex-
ceeding 128K tokens. Given that the longest text
transcript in our dataset is 21,894 words, we input
the raw transcripts directly without applying any
preprocessing steps, such as textual summariza-
tion. However, the visual data required structural
adaptation. The original presentation slides are
collected in PDF format. Since most models do
not natively support PDF input, we converted each
4

(a)
Transcript
Example
(b)
Labels
Statistic
Labels:
mean
std
min
max
car:
0.003443
0.054573
-0.261699
0.312476
ret_eom:
0.001929
0.024981
-0.208935
0.154950
ret_l5m:
0.001877
0.025233
-0.208935
0.132135
ret_ldm:
0.001620
0.025573
-0.207922
0.121361
fut_3d:
0.017588
0.014283
0.000439
0.152479
fut_7d:
0.019605
0.011929
0.002890
0.114500
fut_15d:
0.019874
0.011657
0.004166
0.143844
fut_30d:

0.020287
0.011600
0.004408
0.161032
past_3d:
0.020148
0.015334
0.000288
0.133771
past_7d:
0.020292
0.011701
0.002662
0.100579
past_15d:
0.019352
0.009554
0.004090
0.074227
past_30d:
0.019842
0.010549
0.004775
0.092727
Input:
Operator:
Good
day,
everyone.
Welcome
to
today's
conference
and
webcast
to
discuss
....
Executives:
Thank
you,
John.
Good
morning,
everyone.
This
is
a
historic
day
for
both
....
Analysts:
Giovanni,
I
want
to
ask
you
where
the
cell
therapy
platform
fits
in
your
....
Operator:
We
will
now
go
live
to
the
presentation.
Please
stand
by...
Executives:
I'm
going
to
take
you
through
the
earnings
presentation,
which
is
available...
Analysts:
Just
a
question
on
loan
growth,
2%
to
3%
on
an
annual
average
basis...
...
Figure 2: Transcript Structure and Label Statistics.
page into a separate image. To accommodate the
image-count limits inherent to many of these mod-
els, we implemented a random sampling strategy.
For each presentation, we randomly selected five
images from the slide deck, explicitly excluding
the first and last pages, which typically contain
non-substantive content such as title cards or con-
cluding remarks. In cases where a presentation
contained five or fewer substantive slides, all avail-
able slides were used. The final input sequence was
structured as: “{Images} {Instruction} {Text Tran-
script} {Answer Format}”. Although this specific
benchmark experiment restricts the visual input to
five sampled images, the complete PDF files are
included in the public dataset release.
Audio-Text Modality:We structured the input
sequence as: “{Audio} {Instruction} {Text Tran-
script} {Answer Format}”.
Image-Audio-Text Modality:To ensure a fair
comparison across all baseline models, we main-
tained the exact input constraints established in the
previous setups. We used the same randomly se-
lected slides as the Image-Text setup. The final
input sequence for this comprehensive modality
was structured as: “{Images} {Audio} {Instruc-
tion} {Text Transcript} {Answer Format}”.
5.3 Benchmark Metrics
Because all of our labels are related to stock re-
turns or volatility, the ground truth data consists of
continuous decimal values. Therefore, we frame
the prediction as a regression task. In this context,
Mean Absolute Error (MAE) serves as the default
metric for evaluating absolute model performance
on our benchmark. For a dataset of n samples,
MAE is defined as:
MAE= 1 n nX i=1 |yi −ˆyi|,(4)
where yi represents the ground-truth numerical
label and ˆyi denotes the model’s prediction. How-
ever, given the inherent complexities of financial
forecasting, relying on a single evaluation metric is
insufficient to capture a model’s true reasoning ca-
pabilities. Therefore, we also employ the Pearson
Correlation Coefficient (r), formulated as:
r=
Pn
i=1(yi −¯y)(ˆyi − ¯ˆy)qPn
i=1(yi −¯y)2 Pn i=1(ˆyi − ¯ˆy)2 .(5)
This metric evaluates the model’s capacity to
correctly identify the relative magnitude of market
reactions across a broad cross-section of compa-
nies. Finally, we report Directional Accuracy (DA).
In financial markets, accurately forecasting the di-
rection of a movement is a important signal for
investment strategies. DA measures the proportion
of predictions that correctly anticipate the mathe-
matical sign of the actual outcome, expressed as:
DA= 1 n nX i=1 1(sgn(yi) =sgn(ˆyi)),(6)
where 1 is the indicator function andsgn extracts
the positive or negative sign of the value.
5

Label Metric Image-Text Audio-Text Any-to-Any
Qw3.5-2B Qw3.5-4B Qw3.5-9B Qw3.5-27B Qw3.5-35B Qw3.6-27B Qw3.6-35B Gm3n Mis3-3B Mis3-8B Mis3-14B GPT-5.4 GPT-5.5 Cld-4.6 Cld-4.8 V ox-24B Moss Gm4-E2B Gm4-E4B
car MAE↓0.0511 0.0498 0.0499 0.0534 0.0470 0.0505 0.0478 0.0740 0.0599 0.0540 0.0546 0.0493 0.0526 0.0493 0.0458 0.04290.1079 0.04180.0437
DA↑21.76% 41.61% 48.07% 50.56% 53.11% 51.64% 51.10% 55.88%46.11% 50.66% 51.98% 51.83% 53.45% 53.69% 41.09% 20.79% 37.60% 55.17%53.20%
ret_eom MAE↓0.0341 0.0198 0.0210 0.0302 0.0199 0.0228 0.0196 0.0346 0.0184 0.0184 0.0184 0.0182 0.01440.0179 0.0177 0.02243.4277 0.0297 0.0248
DA↑37.85% 25.28% 51.00% 56.23% 55.55% 56.77% 57.11% 56.65% 53.55% 56.82% 56.33% 59.49% 71.46% 71.92% 72.41%21.71% 37.16% 60.59%60.10%
ret_l5m MAE↓0.0316 0.0196 0.0207 0.0221 0.0192 0.0201 0.0192 0.0335 0.0193 0.0246 0.0199 0.0182 0.01710.0191 0.0192 0.02100.0748 0.0229 0.0216
DA↑26.50% 26.45% 52.96% 56.67% 55.35% 56.09% 54.03% 56.16% 5.77% 51.25% 54.72% 59.22% 66.01% 67.00% 67.49%23.47% 40.78%59.11% 61.08%
ret_ldm MAE↓0.0318 0.0206 0.0206 0.0215 0.0188 0.0195 0.0187 0.0353 0.0198 0.0225 0.0197 0.0183 0.01800.0188 0.0194 0.02310.1369 0.0295 0.0234
DA↑25.23% 34.23% 51.10% 55.21% 54.38% 53.74% 56.63% 55.17% 6.45% 53.69% 54.87% 59.22% 64.46% 67.98%66.50% 27.09% 39.76% 62.56%62.07%
fut_3d MAE↓0.0230 0.0215 0.0262 0.0253 0.0169 0.0214 0.0154 0.0305 0.0261 0.0319 0.0308 0.0252 0.0221 0.0142 0.0139 0.019221.7155 0.0115 0.0089
DA↑47.04% 95.11% 96.09% 96.58% 99.41% 96.33% 99.32% 97.54% 71.44% 97.75% 97.26% 99.76% 100.00% 100.00% 100.00%35.60% 53.64%98.03% 99.51%
fut_7d MAE↓0.0235 0.0190 0.0236 0.0227 0.0157 0.0191 0.0156 0.0298 0.0267 0.0749 0.0318 0.0254 0.0242 0.0150 0.0106 0.01960.6668 0.0102 0.0087
DA↑46.11% 95.89% 95.84% 95.84% 99.22% 97.11% 98.68% 100.00%66.21% 96.43% 97.36% 100.00% 100.00%99.01% 100.00%32.08% 53.50%98.52% 99.51%
fut_15d MAE↓0.0238 0.0198 0.0241 0.0218 0.0163 0.0205 0.0254 0.0283 0.0242 0.1292 0.0344 0.0265 0.0267 0.0157 0.0097 0.01940.6633 0.0097 0.0085
DA↑46.50% 95.89% 95.94% 98.48% 99.27% 98.34% 99.22% 98.03% 51.64% 94.67% 97.26% 100.00% 100.00%97.54% 100.00%24.01% 53.30%98.52% 99.34%
fut_30d MAE↓0.0246 0.0215 0.0255 0.0227 0.01660.0574 0.1495 0.0331 0.0257 0.2064 0.0573 0.0287 0.0250 0.0586 0.0191 0.01980.1338 0.0106 0.0086
DA↑54.67% 95.50% 96.72% 97.90% 98.78% 98.09% 98.58% 98.52% 58.68% 94.96% 97.21% 100.00% 100.00%98.03% 100.00%31.39% 52.81%98.03% 99.19%
past_3d MAE↓0.0206 0.0213 0.0331 0.0229 0.0177 0.0180 0.0219 0.0397 0.0393 0.1095 0.0337 0.0150 0.0131 0.01180.0123 0.02290.1823 0.0172 0.0152
DA↑4.01% 81.08% 95.26% 99.17% 95.45% 98.88% 84.16% 93.60% 53.64% 95.31% 99.32% 100.00% 100.00% 100.00% 100.00%47.33% 56.87% 94.58%55.17%
past_7d MAE↓0.0205 0.0206 0.0347 0.0214 0.0153 0.0138 0.0288 0.0427 0.0509 0.2498 0.0414 0.0142 0.0166 0.0143 0.0114 0.02260.7153 0.0207 0.0140
DA↑3.42% 81.12% 95.06% 99.66% 98.04% 99.32% 89.19% 96.06% 48.95% 95.35% 99.27% 100.00% 100.00% 100.00% 100.00%46.70% 56.48% 91.63%57.14%
past_15d MAE↓0.0209 0.0206 0.0344 0.0214 0.0150 0.0157 0.0668 0.0482 0.0484 0.2786 0.0546 0.0138 0.0177 0.0340 0.0118 0.02160.7578 0.0403 0.0125
DA↑8.85% 81.17% 95.06% 99.66% 99.12% 99.46% 89.63% 93.43% 32.57% 95.84% 99.36% 100.00% 100.00% 100.00% 100.00%47.48% 57.21% 92.61%63.05%
past_30d MAE↓0.0228 0.0212 0.0374 0.0356 0.01860.1199 0.2120 0.0605 0.0564 0.2872 0.1753 0.0245 0.0243 0.1068 0.0602 0.02411.1258 0.0742 0.0120
DA↑15.99% 78.78% 94.72% 99.61% 99.46% 99.32% 94.72% 95.07% 35.94% 95.75% 98.24% 100.00% 100.00% 100.00% 100.00%50.71% 56.48% 91.63%69.46%
Table 2: Overall Performance of 19 Baseline Models on MM-FinEval. The evaluation reports averaged Mean
Absolute Error (MAE) and Directional Accuracy (DA) across 12 financial tasks spanning the 2019–2022 period.
For each row, the highest score for each metric is highlighted in a distinct color corresponding to the model type.
5.4 Implementation Details
All experiments were conducted on two NVIDIA
A100 GPUs, each with 80GB of memory. For all
baseline models, we maintained their official repos-
itory configurations and loaded them with bfloat16
precision to optimize computational efficiency. Be-
yond this precision setting, no other modifications
were made to the models’ default parameters, en-
suring a fair and reproducible comparison across
all baseline evaluations.
6 Benchmark Results
6.1 The Gap Between Returns and V olatility
As shown in Table 2, an initial analysis of the
benchmark results reveals a large gap in the ability
of LLMs to predict market returns versus market
volatility. Across the majority of baseline models,
Directional Accuracy (DA) for return-based tasks
(car, ret_eom, ret_l5m, ret_ldm) is relatively poor,
frequently ranging between 40% and 60%. Only
few models achieve above 70% (e.g., Claude-4.8
on ret_eom). Because DA evaluates only the binary
sign of the prediction, a score hovering near 50%
indicates that these models only marginally outper-
form random guessing. In contrast, the majority of
models achieve a DA over 90%, and occasionally
reach 100%, when predicting volatility. Exceptions
are rare, with only a few small-size models, such
as Qwen3.5-2B, falling below 50%. However, as
illustrated by the label statistics in Figure 2b, it is
common knowledge in the financial domain that
volatility cannot be negative. Therefore, despite
achieving high DA scores on volatility-based tasks,
small-size LLMs still fail to preserve a basic un-
derstanding of fundamental constraints in financial
domains.
This performance gap is further illuminated by
evaluating the Mean Absolute Error (MAE). For
instance, high-performing models (e.g., Claude,
Gemma-4) achieve MAEs between 0.041 and 0.045
on the Cumulative Abnormal Return (car) task. As
shown in Figure 2b, return-based tasks are inher-
ently noisy: their ground truth means hover near
zero while exhibiting high variance. Consequently,
this MAE is large compared to car ground truth
mean of 0.003443 and representing approximately
77% of the dataset’s standard deviation. In contrast,
volatility tasks demonstrate a tighter error distri-
bution. On tasks like fut_15d, top models achieve
MAEs as low as 0.0085 to 0.0097, which represent
a much smaller fraction of the ground truth mean
(0.019874) and standard deviation (0.011657). We
present a detailed breakdown of each model’s an-
nual MAE performance in Table 3, capturing the
granular trends over each consecutive year from
2019-2022.
6.2 Inconsistent Scaling Laws and the
Proprietary Advantage
Within specific model architectures and tasks, our
benchmark in Table 2 reveals a clear scaling law
where increased parameter count directly corre-
lates with enhanced financial reasoning capabili-
6

Qw3.5-2B
Qw3.5-4B
Qw3.5-9B
Qw3.5-27B
Qw3.5-35B
Qw3.6-27B
Qw3.6-35B
Gm3n
Mis3-3B
Mis3-8B
Mis3-14B
GPT-5.4
GPT-5.5
Cld-4.6
Cld-4.8
Vox-24B
Moss
Gm4-E2B
Gm4-E4B
car
ret_eom
ret_l5m
ret_ldm
fut_3d fut_7d fut_15d
fut_30d
past_3d
past_7d
past_15d
past_30d
0.0
-0.1
0.1
0.2
0.3
0.4
0.5
Figure 3: Overall Pearson Correlation Coefficients of Baseline Models. The heatmap illustrates the models’ capacity
to recognize linear trends in financial data.
ties. This trend is particularly pronounced within
the Qwen 3.5 and 3.6 model family. As the pa-
rameter size scales from 2 billion to 35 billion, we
observe a consistent, upward trajectory in overall
Directional Accuracy across both return-based and
volatility tasks.
However, this scaling law breaks down on the
MAE metric. Rather than exhibiting a consistent
decrease as parameter counts grow, the models’
MAE changes unpredictably across tasks. For ex-
ample, within the Qwen 3.5 family on the Cumula-
tive Abnormal Return task, the 27B model yields
an MAE of 0.0534, performing worse than its
much smaller 4B (0.0498) and 9B (0.0499) counter-
parts. Similar inconsistencies appear across other
model families. For instance, the Mistral-3B model
achieves a lower MAE (0.0261) on the fut_3d task
than both the Mistral-8B (0.0319) and Mistral-14B
(0.0308). These findings suggest that while larger
models have a better ability to predict the market
movement direction, they do not have the knowl-
edge to accurately estimate the magnitude of those
movements.
Beyond model family scaling, the benchmark
results highlight a performance gap between open-
source and proprietary models. Within the Image-
Text modality, the GPT and Claude model families
consistently outperform their open-source coun-
terparts. Leading proprietary models, such as
GPT-5.5 and Claude-4.8, achieve the highest tier
of Directional Accuracy across the majority of
tasks. Specifically, they reach DA scores of ap-
proximately 72% on ret_eom, and 67% on both
ret_l5m and ret_ldm. These results outperform
the near-random guessing baseline (approximately
50%) in return based tasks. Furthermore, their
100% DA on volatility tasks suggests that these
advanced proprietary models have a basic under-
standing of the non-negativity constraints inherent
to financial volatility.
6.3 The Advantage of Any-to-Any
Multimodal Integration
As shown in Table 2, our benchmark results show
the advantage of integrating all three data modali-
ties: text, audio, and visual. The Any-to-Any mod-
els evaluated in this study, specifically Gemma 4
E2B and Gemma 4 E4B, perform well on both
return-based and volatility tasks. Despite their
small size architectures (Gemma 4 E2B is a 5B
parameter model utilizing only 2B active param-
eters, while Gemma 4 E4B is an 8B model with
4B active parameters) both achieve a Directional
Accuracy exceeding 60% across ret_eom, ret_l5m,
7

0.6
0.4
0.2
0.0
-0.2
-0.4
-0.6
2019
2020
2021
2022
2019
2020
2021
2022
2019
2020
2021
2022
2019
2020
2021
2022
fut_15d
fut_30d
fut_3d
fut_7d
past_3d
past_7d
past_15d
past_30d
Qw3.5-2B
Qw3.5-4B
Qw3.5-9B
Qw3.5-27B
Qw3.5-35B
Qw3.6-27B
Qw3.6-35B
Gm3n
Mis3-3B
Mis3-8B
Mis3-14B
GPT-5.4
GPT-5.5
Cld-4.6
Cld-4.8
Vox-24B
Moss
Gm4-E2B
Gm4-E4B
Qw3.5-2B
Qw3.5-4B
Qw3.5-9B
Qw3.5-27B
Qw3.5-35B
Qw3.6-27B
Qw3.6-35B
Gm3n
Mis3-3B
Mis3-8B
Mis3-14B
GPT-5.4
GPT-5.5
Cld-4.6
Cld-4.8
Vox-24B
Moss
Gm4-E2B
Gm4-E4B
Figure 4: Annual Pearson Correlation Trends (2019–2022) on V olatility Tasks. The heatmap illustrates how models’
ability to capture linear relationships shifts over time.
and ret_ldm. This performance is better than much
larger Image-Text modality baselines, such as the
35B parameter Qwen 3.6 model, and even propri-
etary GPT 5.4 model. Furthermore, on the Cumu-
lative Abnormal Return task, both Gemma 4 E2B
(0.0418) and Gemma 4 E4B (0.0437) achieve lower
MAEs than the highly capable Claude-4.8 model
(0.0458).
This unexpected performance strongly validates
that textual, visual, and audio data streams provide
distinct, complementary financial signals rather
than redundant information. In real-world finan-
cial markets, institutional analysts do not evaluate
corporate disclosures solely based on the confer-
ence call transcript. They synthesize what man-
agement is presenting via visual slides, the literal
lexical content of the transcript, and, critically, how
that content is delivered, extracting subtle acoustic
cues from vocal tone, pacing, and inflection. To
accurately predict market reactions, LLMs must
develop a similarly holistic comprehension. The
superior performance of these Any-to-Any mod-
els shows that equipping LLMs with this complete
spectrum of human communication is essential for
replicating expert-level financial reasoning.
6.4 Conservative V ersus Aggressive
Prediction in Audio-Text Models
Another interesting observation in Table 2 is that, in
Audio-Text columns, V oxtral consistently achieves
a superior MAE across the entire benchmark,
whereas Moss performs better on DA. A closer
examination reveals that V oxtral exhibits highly
conservative prediction behaviors, frequently gen-
erating its output close to zero. By minimizing
the absolute magnitude of its predictions, V oxtral
successfully avoids absolute error penalties, result-
ing in a relatively lower MAE. However, this zero-
anchored conservatism prevents the model from
capturing meaningful market momentum, leading
to exceptionally poor DA scores. Conversely, Moss
adopts a highly aggressive predictive strategy. It
frequently generates big numerical prediction, and
is more likely to capture the correct directional
sign.
6.5 Pearson Correlation
In addition to MAE and DA, we evaluated the Pear-
son correlation coefficient to assess the models’ ca-
pacity to recognize linear trends and relative shifts
in the financial data. As illustrated in Figure 3,
open-source models generally exhibit low Pear-
son correlations across all tasks, with the highest
scores peaking near 0.20 on the vol_fut_15d task
(achieved by Qwen3.5 27B and Gemma 3n). Inter-
estingly, proprietary models such as GPT-5.4, GPT-
5.5, and the Claude 4 series achieve surprisingly
moderate-to-strong positive Pearson correlations
on volatility tasks. For instance, GPT-5.4 reaches a
correlation of 0.44 on vol_fut_7d, and Claude 4.8
reaches 0.42. This results reveals that proprietary
architectures can successfully detect relative shifts
8

car
ret_eom
ret_l5m
past_3d
past_7d
past_15d
past_30d
fut_3d
fut_7d
2019
2020
2021
2022
0
40
80
0
40
80
0
40
80
ret_ldm
fut_15d
fut_30d
2019
2020
2021
2022
2019
2020
2021
2022
2019
2020
2021
2022
Figure 5: Annual Directional Accuracy (DA) Trends Across MM-FinEval (2019–2022). Each line represents an
individual model’s performance over the four-year period, illustrating how predictive accuracy shifts across different
financial tasks.
in market risk.
We also observe a universal failure across all
architectures to predict Cumulative Abnormal Re-
turn (car). While proprietary models demonstrate
strong positive correlations on discrete return met-
rics, with GPT-5.5 achieving an impressive 0.60 on
ret_eom (End of Month Return). Both open-source
and closed-source models exhibit near-zero or even
negative correlations on the CAR task. This dis-
crepancy likely stems from the structural complex-
ity of Cumulative Abnormal Return, which isolates
the firm-specific stock reaction by mathematically
regressing against broader market benchmarks over
a specific event window.
Finally, the correlation data exposes a clear tem-
poral degradation in model performance across
volatility prediction horizons. For the proprietary
models, predictive capability is highest at the short-
term 3-day and 7-day intervals, but gradually de-
cays through the 15-day mark, ultimately col-
lapsing at the 30-day horizon for both post-event
and pre-event volatility. This progressive decay
strongly aligns with the financial theory of infor-
mation half-life: the qualitative and quantitative
signals extracted directly from an earnings call are
most potent in the immediate short term (Hafez
et al., 2021; Molinaro, 2026). As the prediction
window expands to a full month, the initial catalyst
of the earnings signal is rapidly diluted and over-
whelmed by unpredictable market factors. This
confirms that forecasting long-term variance is in-
herently unfeasible for current LLM architectures.
To further validate the information half-life the-
ory, we map the Pearson correlation coefficients
for the volatility tasks across the 2019–2022 time-
line in Figure 4. This visualization reinforces the
theory by revealing a clear temporal degradation
as the prediction horizon expands. For instance,
when observing the proprietary models across post-
event volatility windows, GPT and Claude achieve
strong correlations for the 3-day and 7-day intervals
(fut_3d and fut_7d); however, this predictive capa-
bility steadily deteriorates at the 15-day and 30-day
marks (fut_15d and fut_30d). An isolated excep-
tion occurs with Claude 4.8, which exhibits unusu-
ally high performance across all post-event volatil-
ity tasks specifically in the year 2021. Despite
this outlier, the overarching trend of progressive
decay strongly aligns with our findings in Figure
3, reaffirming that the predictive signal contained
within a corporate disclosure is rapidly diluted by
unpredictable market factors over extended tempo-
ral windows. More results analysis is in Appendix
C.
9

6.6 Temporal Degradation on Direction
Accuracy
To evaluate how model performance changes over
time, we analyze the annual Directional Accuracy
trends from 2019 to 2022. As illustrated in Figure
5, there is a consistent decline in Directional Ac-
curacy from 2019 to 2022 across the return-based
tasks (ret_eom, ret_l5m, and ret_ldm). In 2019,
several top-performing models tightly cluster near
peak accuracies between 70% and 90%. However,
this performance decreases and drops to a DA range
of 30% to 40% in 2022. This highlights a lack of
temporal generalization in current LLMs. It sug-
gests that post-pandemic market dynamics intro-
duced increased market complexity that reduced
the models’ predictive capabilities.
7 Conclusion
In this work, we introduced MM-FinEval, a multi-
modal benchmark for evaluating LLMs across 12
financial tasks using 2,045 S&P 500 earnings con-
ference calls spanning a 2019–2022 period. The
three modalities inputs in MM-FinEval reflect the
analysis process of expert human financial analysts,
who must synthesize not only what executives dis-
close but how they present it to execute complex
financial reasoning. Our extensive baseline evalu-
ation across Image-Text, Audio-Text, and Any-to-
Any configurations exposes the boundary where
pure language modeling must transition into multi-
sensory, calibrated quantitative reasoning. We hope
this dataset serves as a benchmark for the AI and
finance communities, supporting future work to-
ward multimodal financial analysis for economic
forecasting.
10

References
Hendrik Bessembinder, Kathleen M Kahle, William F
Maxwell, and Danielle Xu. 2008. Measuring ab-
normal bond performance.The Review of Financial
Studies, 22(10):4219–4258.
Zhiyu Chen, Wenhu Chen, Charese Smiley, Sameena
Shah, Iana Borova, Dylan Langdon, Reema Moussa,
Matt Beane, Ting-Hao Huang, Bryan R Routledge,
and 1 others. 2021. Finqa: A dataset of numerical
reasoning over financial data. InProceedings of the
2021 Conference on Empirical Methods in Natural
Language Processing, pages 3697–3711.
Miguel Del Rio, Natalie Delworth, Ryan Wester-
man, Michelle Huang, Nishchal Bhandari, Joseph
Palakapilly, Quinten McNamara, Joshua Dong, Pi-
otr Zelasko, and Miguel Jetté. 2021. Earnings-21:
A practical benchmark for asr in the wild.arXiv
preprint arXiv:2104.11348.
Zihan Dong, Xinyu Fan, and Zhiyuan Peng. 2024. Fn-
spid: A comprehensive financial news dataset in time
series. InProceedings of the 30th ACM SIGKDD
Conference on Knowledge Discovery and Data Min-
ing, pages 4918–4927.
Junwen Duan, Yue Zhang, Xiao Ding, Ching Yun
Chang, and Ting Liu. 2018. Learning target-specific
representations of financial news documents for cu-
mulative abnormal return prediction. InProceed-
ings of the 27th international conference on compu-
tational linguistics, pages 2823–2833.
Peter Hafez, Ricard Matas Navarro, Francisco Gomez,
and Marko Kangrga. 2021. Three trading signals
generated systematically from earnings conference
calls.Available at SSRN 4323558.
Zhenzhi He and Cong Zhang. 2025. Cross-sectional
spillovers of earnings surprises and asset price anoma-
lies.Available at SSRN 5415255.
David Hirshleifer, Sonya Seongyeon Lim, and
Siew Hong Teoh. 2009. Driven to distraction: Ex-
traneous events and underreaction to earnings news.
The Journal of Finance, 64(5):2289–2325.
Allen H Huang, Hui Wang, and Yi Yang. 2023. Finbert:
A large language model for extracting information
from financial text.Contemporary Accounting Re-
search, 40(2):806–841.
Ruizhe Huang, Mahsa Yarmohammadi, Jan Trmal,
Jing Liu, Desh Raj, Leibny Paola Garcia, Alexei
Ivanov, Patrick Ehlen, Mingzhi Yu, Ariya Rastrow,
Dan Povey, and Sanjeev Khudanpur. 2024. ConEC:
Earnings call dataset with real-world contexts for
benchmarking contextual speech recognition. InPro-
ceedings of the 2024 Joint International Conference
on Computational Linguistics, Language Resources
and Evaluation (LREC-COLING 2024), pages 3700–
3706, Torino, Italia. ELRA and ICCL.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, Lélio Renard Lavaud,
Marie-Anne Lachaux, Pierre Stock, Teven Le Scao,
Thibaut Lavril, Thomas Wang, Timothée Lacroix,
and William El Sayed. 2023. Mistral 7b.Preprint,
arXiv:2310.06825.
Gergana Jostova, Stanislava Nikolova, Alexander
Philipov, and Christof W Stahel. 2013. Momentum
in corporate bond returns.The Review of Financial
Studies, 26(7):1649–1693.
Shimon Kogan, Dimitry Levin, Bryan R Routledge, Ja-
cob S Sagi, and Noah A Smith. 2009. Predicting
risk from financial reports with regression. InPro-
ceedings of human language technologies: the 2009
annual conference of the North American Chapter of
the Association for Computational Linguistics, pages
272–280.
Thanos Konstantinidis, Giorgos Iacovides, Mingxue
Xu, Tony G Constantinides, and Danilo Mandic.
2024. Finllama: Financial sentiment classification
for algorithmic trading applications.arXiv preprint
arXiv:2403.12285.
Viet Lai, Michael Krumdick, Charles Lovering, Varshini
Reddy, Craig Schmidt, and Chris Tanner. 2025. Sec-
qa: A systematic evaluation corpus for financial qa.
InProceedings of The 10th Workshop on Financial
Technology and Natural Language Processing, pages
221–236.
Jiazheng Li, Linyi Yang, Barry Smyth, and Ruihai Dong.
2020. Maec: A multimodal aligned earnings confer-
ence call dataset for financial risk prediction. InPro-
ceedings of the 29th ACM International Conference
on Information & Knowledge Management, pages
3063–3070.
Yinheng Li, Shaofei Wang, Han Ding, and Hang Chen.
2023. Large language models in finance: A survey.
InProceedings of the fourth ACM international con-
ference on AI in finance, pages 374–382.
Qingwen Liang and Matias Carrasco Kind. 2025. How
does managers’ willingness to disclose affect an-
alysts’ earning forecasts-a measurement by llms.
Available at SSRN 5199752.
Alexander H Liu, Andy Ehrenberg, Andy Lo, Clé-
ment Denoix, Corentin Barreau, Guillaume Lam-
ple, Jean-Malo Delignon, Khyathi Raghavi Chandu,
Patrick von Platen, Pavankumar Reddy Muddireddy,
and 1 others. 2025a. V oxtral.arXiv preprint
arXiv:2507.13264.
Zhaowei Liu, Xin Guo, Zhi Yang, Fangqi Lou, Lingfeng
Zeng, Jinyi Niu, Mengping Li, Qi Qi, Zhiqiang
Liu, Yiyang Han, and 1 others. 2025b. Fin-r1:
A large language model for financial reasoning
through reinforcement learning.arXiv preprint
arXiv:2503.16252.
11

Yiming Lu, Yebowen Hu, Hassan Foroosh, Wei Jin,
and Fei Liu. 2024. Strux: An llm for decision-
making with structured explanations.arXiv preprint
arXiv:2410.12583.
Junyu Luo, Zhizhuo Kou, Liming Yang, Xiao Luo,
Jinsheng Huang, Zhiping Xiao, Jingshu Peng,
Chengzhong Liu, Jiaming Ji, Xuanzhe Liu, and 1 oth-
ers. 2025. Finmme: Benchmark dataset for financial
multi-modal reasoning evaluation. InProceedings
of the 63rd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 29465–29489.
Jabez Magomere, Elena Kochkina, Samuel Mensah,
Simerjot Kaur, and Charese Smiley. 2025. FinNLI:
Novel dataset for multi-genre financial natural lan-
guage inference benchmarking. InFindings of the
Association for Computational Linguistics: NAACL
2025, pages 4545–4568, Albuquerque, New Mexico.
Association for Computational Linguistics.
Puneet Mathur, Mihir Goyal, Ramit Sawhney, Ritik
Mathur, Jochen L Leidner, Franck Dernoncourt, and
Dinesh Manocha. 2022. Docfin: Multimodal fi-
nancial prediction and bias mitigation using semi-
structured documents. InFindings of the Association
for Computational Linguistics: EMNLP 2022, pages
1933–1940.
Matéo Molinaro. 2026. Do earnings call transcripts
predict post-announcement returns?Available at
SSRN 6695758.
Rajdeep Mukherjee, Abhinav Bohra, Akash Banerjee,
Soumya Sharma, Manjunath Hegde, Afreen Shaikh,
Shivani Shrivastava, Koustuv Dasgupta, Niloy Gan-
guly, Saptarshi Ghosh, and Pawan Goyal. 2022. ECT-
Sum: A new benchmark dataset for bullet point sum-
marization of long earnings call transcripts. InPro-
ceedings of the 2022 Conference on Empirical Meth-
ods in Natural Language Processing, pages 10893–
10906, Abu Dhabi, United Arab Emirates. Associa-
tion for Computational Linguistics.
Huzaifa Pardawala, Siddhant Sukhani, Agam Shah, Veer
Kejriwal, Abhishek Pillai, Rohan Bhasin, Andrew
DiBiasio, Tarun Mandapati, Dhruv Adha, and Sud-
heer Chava. 2024. Subjective-qa: Measuring sub-
jectivity in earnings call transcripts’ qa through six-
dimensional feature analysis.Advances in Neural
Information Processing Systems, 37:59342–59372.
Yu Qin and Yi Yang. 2019. What you say and how
you say it matters: Predicting stock volatility using
verbal and vocal cues. InProceedings of the 57th
Annual Meeting of the Association for Computational
Linguistics, pages 390–401.
Qwen Team. 2026a. Qwen3.5: Towards native multi-
modal agents.
Qwen Team. 2026b. Qwen3.6-35B-A3B: Agentic cod-
ing power, now open to all.
Ramit Sawhney, Arshiya Aggarwal, Piyush Khanna,
Puneet Mathur, Taru Jain, and Rajiv Ratn Shah.
2020a. Risk forecasting from earnings calls acoustics
and network correlations. InINTERSPEECH, pages
2307–2311.
Ramit Sawhney, Piyush Khanna, Arshiya Aggarwal,
Taru Jain, Puneet Mathur, and Rajiv Shah. 2020b.
V oltage: V olatility forecasting via text audio fusion
with graph convolution networks for earnings calls.
InProceedings of the 2020 conference on empirical
methods in natural language processing (EMNLP),
pages 8001–8013.
Ramit Sawhney, Puneet Mathur, Ayush Mangal, Piyush
Khanna, Rajiv Ratn Shah, and Roger Zimmermann.
2020c. Multimodal multi-task financial risk forecast-
ing. InProceedings of the 28th ACM international
conference on multimedia, pages 456–465.
Agam Shah, Suvan Paturi, and Sudheer Chava. 2023.
Trillion dollar words: A new financial dataset, task &
market analysis. InProceedings of the 61st Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 6664–6679.
Dong Shu, Yanguang Liu, Huopu Zhang, and Mengnan
Du. 2025a. Fincall-surprise: A large scale multi-
modal benchmark for earning surprise prediction.
arXiv preprint arXiv:2510.03965.
Dong Shu, Haoyang Yuan, Yuchen Wang, Yanguang
Liu, Huopu Zhang, Haiyan Zhao, and Mengnan
Du. 2025b. Finchart-bench: Benchmarking finan-
cial chart comprehension in vision-language models.
arXiv preprint arXiv:2507.14823.
Gemma Team. 2026a. Gemma 4 technical report.
Preprint, arXiv:2607.02770.
Gemma Team, Thomas Mesnard, Cassidy Hardin,
Robert Dadashi, Surya Bhupatiraju, Shreya Pathak,
Laurent Sifre, Morgane Rivière, Mihir Sanjay Kale,
Juliette Love, and 1 others. 2024. Gemma: Open
models based on gemini research and technology.
arXiv preprint arXiv:2403.08295.
OpenMOSS Team. 2026b. Moss-audio techni-
cal report. https://github.com/OpenMOSS/
MOSS-Audio. GitHub repository.
Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski,
Mark Dredze, Sebastian Gehrmann, Prabhanjan Kam-
badur, David Rosenberg, and Gideon Mann. 2023.
Bloomberggpt: A large language model for finance.
arXiv preprint arXiv:2303.17564.
Hongyang Yang, Xiao-Yang Liu, and Christina Dan
Wang. 2023. Fingpt: Open-source financial large
language models.arXiv preprint arXiv:2306.06031.
Ding Yu, Zhuo Liu, and Hangfeng He. 2025. Same com-
pany, same signal: The role of identity in earnings
call transcripts. InFindings of the Association for
Computational Linguistics: ACL 2025, pages 18403–
18422.
12

Yu Zhu, Xiao Liu, and Olivia R Liu Sheng. 2025. Post-
earnings-announcement drift prediction: Leveraging
postevent investor responses with multitask learning.
Information Systems Research, 36(4):2191–2212.
13

A Data Analysis
In Figure 2, we detail the label statistics, including
the mean, standard deviation, minimum, and max-
imum for all 12 financial task labels. An analysis
of these distributions explicitly confirms the struc-
tural differences between discrete return tasks and
continuous volatility tasks.
The return-based tasks (car, ret_eom, ret_l5m,
and ret_ldm) exhibit a classic zero-centered finan-
cial return distribution. The means for these labels
hover barely above zero, ranging from 0.001620
to 0.003443. In contrast, their standard deviations
are substantially larger, ranging from 0.024981 to
0.054573. This high variance relative to the mean
confirms a notoriously low signal-to-noise ratio in-
herent to predicting market direction. Furthermore,
the minimum and maximum values demonstrate
that returns fluctuate wildly in both directions. For
instance, the Cumulative Abnormal Return (car)
spans from a minimum of -0.261699 to a maximum
of 0.312476, illustrating the extreme, bidirectional
stochastic shocks that models must account for.
Conversely, the volatility-based tasks display a
fundamentally different statistical profile. Most no-
tably, the minimum values across all eight volatility
labels are strictly positive (e.g., the lowest absolute
minimum is 0.000288 for past_3d). This directly re-
flects the hard non-negativity constraint of financial
volatility. The means are significantly higher and
tightly clustered between 0.017588 and 0.020292.
Additionally, the standard deviations (0.009554 to
0.015334) are much smaller relative to their re-
spective means when compared to the return labels.
This points to a tighter, more structured distribution
characterized by volatility clustering, making it a
more autoregressive and stable phenomenon.
These distinct distributional characteristics math-
ematically explain the performance divergence ob-
served in our benchmark results. Return tasks
are heavily obscured by symmetric, zero-centered
noise, making them highly resistant to accurate
quantitative regression. V olatility tasks, however,
present a structured, bounded, and clustered target
that is quantitatively easier for models to map, per-
fectly mirroring established financial econometrics.
B Prompt Used in Our Experiments
B.1 CAR Task
Image-Text Models
You are an expert quantitative equity analyst. Your task is
to predict the stock’s Cumulative Abnormal Return (CAR)
for a company based on its earnings call transcript and the
accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the Cumulative Abnormal Return (CAR) asso-
ciated with this earnings event. CAR measures the sum
of the differences between the stock’s actual return and its
expected return over the event window.
2. Provide 1-2 sentences explaining the key driver.
3. Your CAR prediction must be represented as a decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ CAR decimal ]]
Audio-Text Models
You are an expert quantitative equity analyst. Your task is
to predict the stock’s Cumulative Abnormal Return (CAR)
for a company based on its earnings call transcript and
earnings call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Predict the Cumulative Abnormal Return (CAR) asso-
ciated with this earnings event. CAR measures the sum
of the differences between the stock’s actual return and its
expected return over the event window.
2. Provide 1-2 sentences explaining the key driver.
3. Your CAR prediction must be represented as a decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ CAR decimal ]]
Any-to-Any Models
You are an expert quantitative equity analyst. Your task is
to predict the stock’s Cumulative Abnormal Return (CAR)
for a company based on its earnings call transcript, earn-
ings call audio, and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the Cumulative Abnormal Return (CAR) asso-
ciated with this earnings event. CAR measures the sum
of the differences between the stock’s actual return and its
expected return over the event window.
2. Provide 1-2 sentences explaining the key driver.
3. Your CAR prediction must be represented as a decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ CAR decimal ]]
14

B.2 ret_eom
Image-Text Models
You are an expert quantitative fixed-income analyst. Your
task is to predict the End-of-Month corporate bond re-
turn (ret_eom) for a company based on its earnings call
transcript and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the ret_eom (End-of-Month corporate bond
return). It represents the percentage gain or loss of an
investment or business value over the course of one month.
2. Provide 1-2 sentences explaining the key driver.
3. Your ret_eom prediction must be represented as a deci-
mal (e.g., 0.052 or -0.014).
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ ret_eom decimal ]]
Audio-Text Models
You are an expert quantitative fixed-income analyst. Your
task is to predict the End-of-Month corporate bond re-
turn (ret_eom) for a company based on its earnings call
transcript and earnings call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Predict the ret_eom (End-of-Month corporate bond
return). It represents the percentage gain or loss of an
investment or business value over the course of one month.
2. Provide 1-2 sentences explaining the key driver.
3. Your ret_eom prediction must be represented as a deci-
mal (e.g., 0.052 or -0.014).
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ ret_eom decimal ]]
Any-to-Any Models
You are an expert quantitative fixed-income analyst. Your
task is to predict the End-of-Month corporate bond re-
turn (ret_eom) for a company based on its earnings call
transcript, earnings call audio, and the accompanying pre-
sentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the ret_eom (End-of-Month corporate bond
return). It represents the percentage gain or loss of an
investment or business value over the course of one month.
2. Provide 1-2 sentences explaining the key driver.
3. Your ret_eom prediction must be represented as a deci-
mal (e.g., 0.052 or -0.014).
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ ret_eom decimal ]]
B.3 ret_l5m
Image-Text Models
You are an expert quantitative fixed-income analyst. Your
task is to predict the corporate bond return for the last 5
days of the month (ret_l5m) for a company based on its
earnings call transcript and the accompanying presentation
slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the ret_l5m (Return Last 5 Days of Month).
It represents the percentage gain or loss of the corporate
bond during the final 5 trading days of the month.
2. Provide 1-2 sentences explaining the key driver.
3. Your ret_l5m prediction must be represented as a deci-
mal (e.g., 0.052 or -0.014).
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ ret_l5m decimal ]]
Audio-Text Models
You are an expert quantitative fixed-income analyst. Your
task is to predict the corporate bond return for the last 5
days of the month (ret_l5m) for a company based on its
earnings call transcript and earnings call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Predict the ret_l5m (Return Last 5 Days of Month).
It represents the percentage gain or loss of the corporate
bond during the final 5 trading days of the month.
2. Provide 1-2 sentences explaining the key driver.
3. Your ret_l5m prediction must be represented as a deci-
mal (e.g., 0.052 or -0.014).
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ ret_l5m decimal ]]
Any-to-Any Models
You are an expert quantitative fixed-income analyst. Your
task is to predict the corporate bond return for the last
5 days of the month (ret_l5m) for a company based on
its earnings call transcript, earnings call audio, and the
accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the ret_l5m (Return Last 5 Days of Month).
It represents the percentage gain or loss of the corporate
bond during the final 5 trading days of the month.
2. Provide 1-2 sentences explaining the key driver.
3. Your ret_l5m prediction must be represented as a deci-
mal (e.g., 0.052 or -0.014).
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ ret_l5m decimal ]]
15

B.4 ret_ldm
Image-Text Models
You are an expert quantitative fixed-income analyst. Your
task is to predict the corporate bond return specifically on
the last trading day of the month (ret_ldm) for a company
based on its earnings call transcript and the accompanying
presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the ret_ldm (Return Last Day of Month). It
represents the percentage gain or loss of the corporate
bond exactly on the final trading day of the month.
2. Provide 1-2 sentences explaining the key driver.
3. Your ret_ldm prediction must be represented as a deci-
mal (e.g., 0.052 or -0.014).
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ ret_ldm decimal ]]
Audio-Text Models
You are an expert quantitative fixed-income analyst. Your
task is to predict the corporate bond return specifically on
the last trading day of the month (ret_ldm) for a company
based on its earnings call transcript and earnings call mp3
audio.
Transcript:
{text_transcript}
Instructions:
1. Predict the ret_ldm (Return Last Day of Month). It
represents the percentage gain or loss of the corporate
bond exactly on the final trading day of the month.
2. Provide 1-2 sentences explaining the key driver.
3. Your ret_ldm prediction must be represented as a deci-
mal (e.g., 0.052 or -0.014).
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ ret_ldm decimal ]]
Any-to-Any Models
You are an expert quantitative fixed-income analyst. Your
task is to predict the corporate bond return specifically on
the last trading day of the month (ret_ldm) for a company
based on its earnings call transcript, earnings call audio,
and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the ret_ldm (Return Last Day of Month). It
represents the percentage gain or loss of the corporate
bond exactly on the final trading day of the month.
2. Provide 1-2 sentences explaining the key driver.
3. Your ret_ldm prediction must be represented as a deci-
mal (e.g., 0.052 or -0.014).
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ ret_ldm decimal ]]
B.5 vol_fut_3d
Image-Text Models
You are an expert quantitative analyst. Your task is to
predict the post-event 3-day volatility (vol_fut_3d) for
a company based on its earnings call transcript and the
accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_3d (V olatility Future 3 Days). This
represents the expected price turbulence, uncertainty, and
fluctuation of the asset over the 3 trading days immediately
following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_3d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_3d decimal ]]
Audio-Text Models
You are an expert quantitative analyst. Your task is to
predict the post-event 3-day volatility (vol_fut_3d) for a
company based on its earnings call transcript and earnings
call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_3d (V olatility Future 3 Days). This
represents the expected price turbulence, uncertainty, and
fluctuation of the asset over the 3 trading days immediately
following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_3d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_3d decimal ]]
Any-to-Any Models
You are an expert quantitative analyst. Your task is to
predict the post-event 3-day volatility (vol_fut_3d) for a
company based on its earnings call transcript, earnings
call audio, and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_3d (V olatility Future 3 Days). This
represents the expected price turbulence, uncertainty, and
fluctuation of the asset over the 3 trading days immediately
following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_3d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_3d decimal ]]
16

B.6 vol_fut_7d
Image-Text Models
You are an expert quantitative analyst. Your task is to
predict the post-event 7-day volatility (vol_fut_7d) for
a company based on its earnings call transcript and the
accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_7d (V olatility Future 7 Days). This
represents the expected price turbulence, uncertainty, and
fluctuation of the asset over the 7 trading days immediately
following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_7d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_7d decimal ]]
Audio-Text Models
You are an expert quantitative analyst. Your task is to
predict the post-event 7-day volatility (vol_fut_7d) for a
company based on its earnings call transcript and earnings
call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_7d (V olatility Future 7 Days). This
represents the expected price turbulence, uncertainty, and
fluctuation of the asset over the 7 trading days immediately
following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_7d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_7d decimal ]]
Any-to-Any Models
You are an expert quantitative analyst. Your task is to
predict the post-event 7-day volatility (vol_fut_7d) for a
company based on its earnings call transcript, earnings
call audio, and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_7d (V olatility Future 7 Days). This
represents the expected price turbulence, uncertainty, and
fluctuation of the asset over the 7 trading days immediately
following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_7d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_7d decimal ]]
B.7 vol_fut_15d
Image-Text Models
You are an expert quantitative analyst. Your task is to
predict the post-event 15-day volatility (vol_fut_15d) for
a company based on its earnings call transcript and the
accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_15d (V olatility Future 15 Days).
This represents the expected price turbulence, uncertainty,
and fluctuation of the asset over the 15 trading days imme-
diately following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_15d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_15d decimal ]]
Audio-Text Models
You are an expert quantitative analyst. Your task is to
predict the post-event 15-day volatility (vol_fut_15d) for a
company based on its earnings call transcript and earnings
call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_15d (V olatility Future 15 Days).
This represents the expected price turbulence, uncertainty,
and fluctuation of the asset over the 15 trading days imme-
diately following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_15d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_15d decimal ]]
Any-to-Any Models
You are an expert quantitative analyst. Your task is to
predict the post-event 15-day volatility (vol_fut_15d) for
a company based on its earnings call transcript, earnings
call audio, and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_15d (V olatility Future 15 Days).
This represents the expected price turbulence, uncertainty,
and fluctuation of the asset over the 15 trading days imme-
diately following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_15d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_15d decimal ]]
17

B.8 vol_fut_30d
Image-Text Models
You are an expert quantitative analyst. Your task is to
predict the post-event 30-day volatility (vol_fut_30d) for
a company based on its earnings call transcript and the
accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_30d (V olatility Future 30 Days).
This represents the expected price turbulence, uncertainty,
and fluctuation of the asset over the 30 trading days imme-
diately following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_30d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_30d decimal ]]
Audio-Text Models
You are an expert quantitative analyst. Your task is to
predict the post-event 30-day volatility (vol_fut_30d) for a
company based on its earnings call transcript and earnings
call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_30d (V olatility Future 30 Days).
This represents the expected price turbulence, uncertainty,
and fluctuation of the asset over the 30 trading days imme-
diately following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_30d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_30d decimal ]]
Any-to-Any Models
You are an expert quantitative analyst. Your task is to
predict the post-event 30-day volatility (vol_fut_30d) for
a company based on its earnings call transcript, earnings
call audio, and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Predict the vol_fut_30d (V olatility Future 30 Days).
This represents the expected price turbulence, uncertainty,
and fluctuation of the asset over the 30 trading days imme-
diately following this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_fut_30d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_fut_30d decimal ]]
B.9 vol_past_3d
Image-Text Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 3-day volatility (vol_past_3d) for
a company based on its earnings call transcript and the
accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_3d (V olatility Past 3 Days). This
represents the realized volatility (price turbulence and un-
certainty) of the asset over the 3 trading days immediately
preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_3d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_3d decimal ]]
Audio-Text Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 3-day volatility (vol_past_3d) for a
company based on its earnings call transcript and earnings
call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_3d (V olatility Past 3 Days). This
represents the realized volatility (price turbulence and un-
certainty) of the asset over the 3 trading days immediately
preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_3d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_3d decimal ]]
Any-to-Any Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 3-day volatility (vol_past_3d) for
a company based on its earnings call transcript, earnings
call audio, and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_3d (V olatility Past 3 Days). This
represents the realized volatility (price turbulence and un-
certainty) of the asset over the 3 trading days immediately
preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_3d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_3d decimal ]]
18

B.10 vol_past_7d
Image-Text Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 7-day volatility (vol_past_7d) for
a company based on its earnings call transcript and the
accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_7d (V olatility Past 7 Days). This
represents the realized volatility (price turbulence and un-
certainty) of the asset over the 7 trading days immediately
preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_7d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_7d decimal ]]
Audio-Text Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 7-day volatility (vol_past_7d) for a
company based on its earnings call transcript and earnings
call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_7d (V olatility Past 7 Days). This
represents the realized volatility (price turbulence and un-
certainty) of the asset over the 7 trading days immediately
preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_7d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_7d decimal ]]
Any-to-Any Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 7-day volatility (vol_past_7d) for
a company based on its earnings call transcript, earnings
call audio, and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_7d (V olatility Past 7 Days). This
represents the realized volatility (price turbulence and un-
certainty) of the asset over the 7 trading days immediately
preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_7d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_7d decimal ]]
B.11 vol_past_15d
Image-Text Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 15-day volatility (vol_past_15d) for
a company based on its earnings call transcript and the
accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_15d (V olatility Past 15 Days).
This represents the realized volatility (price turbulence
and uncertainty) of the asset over the 15 trading days
immediately preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_15d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_15d decimal ]]
Audio-Text Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 15-day volatility (vol_past_15d)
for a company based on its earnings call transcript and
earnings call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_15d (V olatility Past 15 Days).
This represents the realized volatility (price turbulence
and uncertainty) of the asset over the 15 trading days
immediately preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_15d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_15d decimal ]]
Any-to-Any Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 15-day volatility (vol_past_15d) for
a company based on its earnings call transcript, earnings
call audio, and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_15d (V olatility Past 15 Days).
This represents the realized volatility (price turbulence
and uncertainty) of the asset over the 15 trading days
immediately preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_15d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_15d decimal ]]
19

B.12 vol_past_30d
Image-Text Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 30-day volatility (vol_past_30d) for
a company based on its earnings call transcript and the
accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_30d (V olatility Past 30 Days).
This represents the realized volatility (price turbulence
and uncertainty) of the asset over the 30 trading days
immediately preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_30d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_30d decimal ]]
Audio-Text Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 30-day volatility (vol_past_30d)
for a company based on its earnings call transcript and
earnings call mp3 audio.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_30d (V olatility Past 30 Days).
This represents the realized volatility (price turbulence
and uncertainty) of the asset over the 30 trading days
immediately preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_30d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_30d decimal ]]
Any-to-Any Models
You are an expert quantitative analyst. Your task is to
estimate the pre-event 30-day volatility (vol_past_30d) for
a company based on its earnings call transcript, earnings
call audio, and the accompanying presentation slides.
Transcript:
{text_transcript}
Instructions:
1. Estimate the vol_past_30d (V olatility Past 30 Days).
This represents the realized volatility (price turbulence
and uncertainty) of the asset over the 30 trading days
immediately preceding this earnings call.
2. Provide 1-2 sentences explaining the key driver.
3. Your vol_past_30d estimate must be represented as a
decimal.
**Answer format**
Rationale = [[ 1-2 sentences rationale ]]
Prediction = [[ vol_past_30d decimal ]]
C Pearson Correlation Temporal
Observations
We evaluated the Pearson correlation coefficient
across the 2019–2022 timeline. Figure 6 indicates
that proprietary models improve their ability to cap-
ture linear relationships over time. For example,
on the ret_eom task, GPT-5.5 exhibits a strict up-
ward trajectory, scaling from a correlation of 0.309
in 2019 to 0.581 by 2022. Similarly, Claude 4.8
improves from 0.144 in 2019 to 0.437 in 2022 on
the exact same task. This temporal strengthening
suggests that massive, closed-source models are
highly adept at mapping evolving macroeconomic
environments to relative asset rankings. In contrast,
open-source models demonstrate no such temporal
adaptation. Models like Qwen 3.5 and Mistral 3
remain near-zero correlations on ret_eom across
the four-year span.
D Examples of Model Responses
Qwen3.5 2B
Rationale = The Cumulative Abnormal Return (CAR) is
predicted to be positive, driven by the company’s achieve-
ment of all-time record quarterly and full-year operating
income and operating ratio, which significantly outper-
formed analyst expectations and the broader market.
Prediction = [[ 0.045 ]]
Qwen3.5 4B
Rationale = [[ The company reported a 22% decline in
GAAP earnings per share due to significant one-time costs,
including severance charges and litigation expenses, which
negatively impacted the market’s sentiment despite under-
lying non-GAAP growth. The management’s focus on
cost-cutting and the uncertainty surrounding future market
conditions likely led to a negative market reaction.]]
Prediction = [[ -0.035 ]]
Qwen3.5 9B
Rationale = The company delivered solid full-year results
with revenue growth, margin expansion, and strong free
cash flow, but the stock price likely already priced in the
positive momentum from the second half of the year. Ad-
ditionally, the guidance for 2019 EPS of $13.90 was pre-
sented as a ¨floor¨rather than a target, and the company ex-
plicitly noted that the Red Hat acquisition (a major value
driver) is excluded from 2019 financial expectations due
to timing uncertainty, which may limit the upside surprise
in the immediate reaction.
Prediction = [[ 0.012 ]]
Qwen3.5 27B
Rationale = [[ The company reported a 22% year-over-
year decline in GAAP earnings per share to $0.84, missing
expectations due to significant one-time charges for sever-
20

0.6
0.4
0.2
0.0
-0.2
-0.4
-0.6
2019
2020
2021
2022
2019
2020
2021
2022
2019
2020
2021
2022
2019
2020
2021
2022
fut_15d
fut_30d
fut_3d
fut_7d
past_3d
past_7d
past_15d
past_30d
car
ret_eom
ret_l5m
ret_ldm
Qw3.5-2B
Qw3.5-4B
Qw3.5-9B
Qw3.5-27B
Qw3.5-35B
Qw3.6-27B
Qw3.6-35B
Gm3n
Mis3-3B
Mis3-8B
Mis3-14B
GPT-5.4
GPT-5.5
Cld-4.6
Cld-4.8
Vox-24B
Moss
Gm4-E2B
Gm4-E4B
Qw3.5-2B
Qw3.5-4B
Qw3.5-9B
Qw3.5-27B
Qw3.5-35B
Qw3.6-27B
Qw3.6-35B
Gm3n
Mis3-3B
Mis3-8B
Mis3-14B
GPT-5.4
GPT-5.5
Cld-4.6
Cld-4.8
Vox-24B
Moss
Gm4-E2B
Gm4-E4B
Qw3.5-2B
Qw3.5-4B
Qw3.5-9B
Qw3.5-27B
Qw3.5-35B
Qw3.6-27B
Qw3.6-35B
Gm3n
Mis3-3B
Mis3-8B
Mis3-14B
GPT-5.4
GPT-5.5
Cld-4.6
Cld-4.8
Vox-24B
Moss
Gm4-E2B
Gm4-E4B
Figure 6: Annual Pearson Correlation Trends (2019–2022) on the MM-FinEval Benchmark. The heatmap illustrates
how models’ ability to capture linear relationships shifts over time.
ance, litigation, and headquarters relocation totaling $0.16
per share. Although non-GAAP earnings grew 9%, the
market reaction is likely to be negative due to the headline
GAAP miss and the explicit guidance that equity markets
will not be a significant contributor to revenue growth in
2019. ]]
Prediction = [[ -0.035 ]]
Qwen3.5 35B
Rationale = PNC delivered a strong 2020 with record
revenue and positive operating leverage, but the market
reaction is likely tempered by the guidance for a modest
decline in Net Interest Income (NII) for 2021 and the
significant drag on reserves ($3.2 billion provision) due
to the pandemic, resulting in a neutral to slightly negative
market response.
Prediction = -0.012
Qwen3.6 27B
Rationale = [[ The company significantly raised its full-
year 2021 revenue guidance to a range of $5.5-$6.0 billion
and projected a substantial expansion in operating margins
to 10.4%-11.0%, driven by strong net order growth and a
robust backlog. Additionally, the firm highlighted a strong
balance sheet with a low debt-to-capital ratio and a clear
path to double-digit community count growth, signaling
strong future profitability. ]]
Prediction = [[ 0.065 ]]
Qwen3.6 35B
Rationale = BlackRock reported record full-year revenue
growth of 20% and operating income growth of 19%, sig-
nificantly outperforming expectations with record net in-
flows of $540 billion and a 10% increase in AUM to $10
trillion. The company also announced a strong capital
return program, including an 18% dividend increase and
$1.5 billion in share repurchases, signaling high confi-
dence in future cash flows and growth.
Prediction = [[ 0.035 ]]
Gemma3n
Rationale = [[ The earnings call presented a strong Q3
performance with solid growth across key products like
Opdivo and Eliquis, and positive momentum from new
launches like Zeposia and Abecma. The company reaf-
firmed its financial guidance and expressed confidence in
its ability to navigate the challenges of generic erosion
while continuing to invest in innovation, which is likely to
be viewed favorably by investors. ]]
Prediction = [[ 0.06 ]]
21

Label Year Image-Text Audio-Text Any-to-Any
Qw3.5-2B Qw3.5-4B Qw3.5-9B Qw3.5-27B Qw3.5-35B Qw3.6-27B Qw3.6-35B Gm3n Mis3-3B Mis3-8B Mis3-14B GPT-5.4 GPT-5.5 Cld-4.6 Cld-4.8 V ox-24B Moss Gm4-E2B Gm4-E4B
car
2019 0.0531 0.0486 0.0495 0.0525 0.0470 0.0493 0.0459 0.0618 0.0588 0.0527 0.0521 0.0489 0.0522 0.0450 0.0475 0.0437 0.1131 0.0410 0.0418
2020 0.0521 0.0502 0.0517 0.0543 0.0485 0.0541 0.0514 0.0594 0.0600 0.0569 0.0565 0.0507 0.0522 0.0435 0.0495 0.0451 0.0951 0.0331 0.0344
2021 0.0471 0.0481 0.0469 0.0516 0.0441 0.0468 0.0445 0.1017 0.0590 0.0508 0.0523 0.0457 0.0495 0.0620 0.0448 0.0415 0.1030 0.0501 0.0536
2022 0.0520 0.0522 0.0513 0.0553 0.0485 0.0517 0.0493 0.0732 0.0617 0.0558 0.0573 0.0517 0.0549 0.0466 0.0414 0.0411 0.1205 0.0430 0.0449
ret_eom
2019 0.0360 0.0203 0.0211 0.0305 0.0202 0.0245 0.0195 0.0312 0.0186 0.0184 0.0185 0.0183 0.0142 0.0178 0.0177 0.0229 1.0074 0.0241 0.0240
2020 0.0392 0.0193 0.0210 0.0315 0.0194 0.0246 0.0214 0.0411 0.0178 0.0178 0.0178 0.0176 0.0135 0.0170 0.0173 0.0215 1.4456 0.0232 0.0225
2021 0.0298 0.0201 0.0210 0.0307 0.0204 0.0217 0.0191 0.0374 0.0187 0.0187 0.0187 0.0185 0.0150 0.0182 0.0178 0.0233 3.6173 0.0230 0.0226
2022 0.0314 0.0195 0.0211 0.0279 0.0195 0.0206 0.0185 0.0287 0.0183 0.0187 0.0187 0.0185 0.0148 0.0185 0.0180 0.0217 1.9141 0.0483 0.0302
ret_l5m
2019 0.0337 0.0201 0.0208 0.0222 0.0197 0.0204 0.0194 0.0295 0.0191 0.0242 0.0200 0.0184 0.0166 0.0192 0.0192 0.0214 0.0827 0.0178 0.0209
2020 0.0342 0.0191 0.0207 0.0224 0.0193 0.0206 0.0197 0.0398 0.0188 0.0239 0.0205 0.0177 0.0163 0.0181 0.0184 0.0200 0.0898 0.0171 0.0195
2021 0.0279 0.0199 0.0208 0.0222 0.0195 0.0199 0.0190 0.0360 0.0194 0.0253 0.0196 0.0184 0.0174 0.0194 0.0194 0.0215 0.0638 0.0217 0.0213
2022 0.0304 0.0194 0.0206 0.0214 0.0185 0.0193 0.0185 0.0287 0.0198 0.0252 0.0196 0.0185 0.0182 0.0195 0.0197 0.0211 0.0630 0.0349 0.0247
ret_ldm
2019 0.0342 0.0213 0.0208 0.0218 0.0192 0.0200 0.0190 0.0315 0.0198 0.0220 0.0197 0.0185 0.0176 0.0191 0.0195 0.0238 0.1585 0.0213 0.0225
2020 0.0345 0.0203 0.0208 0.0221 0.0188 0.0203 0.0195 0.0425 0.0197 0.0222 0.0205 0.0178 0.0171 0.0179 0.0186 0.0221 0.1601 0.0213 0.0212
2021 0.0280 0.0208 0.0206 0.0216 0.0189 0.0194 0.0187 0.0381 0.0196 0.0228 0.0194 0.0186 0.0182 0.0190 0.0195 0.0241 0.1118 0.0305 0.0235
2022 0.0304 0.0200 0.0204 0.0206 0.0181 0.0184 0.0177 0.0292 0.0201 0.0232 0.0192 0.0185 0.0192 0.0190 0.0200 0.0226 0.1171 0.0450 0.0264
fut_3d
2019 0.0214 0.0210 0.0250 0.0235 0.0152 0.0195 0.0138 0.0253 0.0258 0.0322 0.0304 0.0247 0.0205 0.0125 0.0123 0.0184 1.3412 0.0101 0.0075
2020 0.0259 0.0246 0.0315 0.0284 0.0201 0.0250 0.0198 0.0422 0.0305 0.0368 0.0335 0.0298 0.0261 0.0178 0.0163 0.0227 48.0640 0.0142 0.0107
2021 0.0226 0.0211 0.0248 0.0256 0.0162 0.0217 0.0141 0.0316 0.0241 0.0289 0.0298 0.0234 0.0218 0.0135 0.0141 0.0177 0.1583 0.0116 0.0084
2022 0.0221 0.0194 0.0234 0.0235 0.0160 0.0193 0.0140 0.0230 0.0241 0.0296 0.0293 0.0229 0.0201 0.0130 0.0128 0.0178 37.2985 0.0101 0.0090
fut_7d
2019 0.0215 0.0186 0.0225 0.0213 0.0143 0.0175 0.0141 0.0251 0.0264 0.0768 0.0314 0.0249 0.0227 0.0134 0.0092 0.0188 0.6125 0.0091 0.0076
2020 0.0266 0.0219 0.0283 0.0255 0.0181 0.0225 0.0193 0.0409 0.0305 0.0805 0.0345 0.0298 0.0286 0.0183 0.0124 0.0233 0.8126 0.0125 0.0104
2021 0.0233 0.0185 0.0222 0.0227 0.0149 0.0190 0.0141 0.0311 0.0246 0.0682 0.0306 0.0236 0.0233 0.0144 0.0107 0.0177 0.6152 0.0102 0.0083
2022 0.0227 0.0171 0.0212 0.0212 0.0156 0.0175 0.0150 0.0222 0.0254 0.0740 0.0307 0.0232 0.0222 0.0139 0.0101 0.0185 0.6271 0.0089 0.0084
fut_15d
2019 0.0218 0.0194 0.0230 0.0205 0.0150 0.0189 0.0260 0.0242 0.0242 0.1293 0.0340 0.0260 0.0252 0.0142 0.0085 0.0186 0.6105 0.0088 0.0076
2020 0.0268 0.0225 0.0289 0.0243 0.0187 0.0239 0.0270 0.0382 0.0271 0.1388 0.0371 0.0310 0.0312 0.0191 0.0113 0.0230 0.8037 0.0118 0.0099
2021 0.0235 0.0193 0.0228 0.0218 0.0155 0.0206 0.0226 0.0298 0.0223 0.1217 0.0333 0.0247 0.0259 0.0148 0.0097 0.0176 0.6111 0.0096 0.0082
2022 0.0231 0.0181 0.0217 0.0206 0.0159 0.0184 0.0259 0.0209 0.0230 0.1271 0.0332 0.0242 0.0246 0.0147 0.0093 0.0185 0.6279 0.0084 0.0083
fut_30d
2019 0.0225 0.0210 0.0242 0.0213 0.0153 0.0543 0.1493 0.0285 0.0258 0.2079 0.0571 0.0281 0.0238 0.0592 0.0175 0.0190 0.1311 0.0096 0.0076
2020 0.0278 0.0242 0.0305 0.0252 0.0190 0.0578 0.1485 0.0437 0.0284 0.2195 0.0607 0.0335 0.0287 0.0578 0.0218 0.0233 0.1396 0.0129 0.0101
2021 0.0244 0.0210 0.0240 0.0228 0.0159 0.0579 0.1504 0.0345 0.0239 0.1983 0.0560 0.0267 0.0246 0.0593 0.0188 0.0180 0.1310 0.0106 0.0084
2022 0.0237 0.0197 0.0231 0.0214 0.0163 0.0597 0.1501 0.0256 0.0245 0.2000 0.0553 0.0263 0.0229 0.0579 0.0181 0.0188 0.1337 0.0093 0.0083
past_3d
2019 0.0193 0.0210 0.0315 0.0224 0.0174 0.0179 0.0214 0.0322 0.0396 0.1118 0.0328 0.0148 0.0131 0.0118 0.0121 0.0223 0.1970 0.0163 0.0151
2020 0.0234 0.0242 0.0401 0.0270 0.0206 0.0210 0.0257 0.0543 0.0435 0.1207 0.0391 0.0176 0.0153 0.0139 0.0145 0.0270 0.2201 0.0205 0.0175
2021 0.0198 0.0204 0.0306 0.0216 0.0167 0.0170 0.0209 0.0416 0.0371 0.1030 0.0316 0.0140 0.0123 0.0109 0.0115 0.0213 0.1517 0.0166 0.0142
2022 0.0197 0.0195 0.0301 0.0205 0.0162 0.0161 0.0197 0.0308 0.0369 0.1026 0.0313 0.0136 0.0118 0.0104 0.0111 0.0211 0.1604 0.0154 0.0140
past_7d
2019 0.0192 0.0204 0.0330 0.0210 0.0151 0.0138 0.0284 0.0351 0.0514 0.2520 0.0406 0.0141 0.0166 0.0144 0.0113 0.0221 0.6559 0.0196 0.0139
2020 0.0231 0.0234 0.0416 0.0253 0.0175 0.0160 0.0326 0.0581 0.0558 0.2721 0.0468 0.0166 0.0191 0.0166 0.0133 0.0266 0.8647 0.0257 0.0161
2021 0.0199 0.0196 0.0323 0.0202 0.0145 0.0131 0.0275 0.0454 0.0487 0.2372 0.0392 0.0133 0.0157 0.0133 0.0107 0.0210 0.6622 0.0192 0.0131
2022 0.0199 0.0190 0.0318 0.0192 0.0141 0.0123 0.0266 0.0322 0.0477 0.2379 0.0388 0.0129 0.0152 0.0129 0.0103 0.0206 0.6784 0.0183 0.0127
past_15d
2019 0.0195 0.0204 0.0327 0.0211 0.0149 0.0157 0.0665 0.0396 0.0494 0.2804 0.0537 0.0137 0.0178 0.0340 0.0117 0.0211 0.6970 0.0381 0.0124
2020 0.0234 0.0234 0.0410 0.0255 0.0171 0.0182 0.0717 0.0645 0.0531 0.3013 0.0605 0.0161 0.0202 0.0374 0.0136 0.0253 0.9080 0.0491 0.0144
2021 0.0203 0.0197 0.0321 0.0201 0.0143 0.0150 0.0650 0.0504 0.0463 0.2662 0.0522 0.0129 0.0167 0.0328 0.0110 0.0201 0.7022 0.0378 0.0118
2022 0.0204 0.0189 0.0317 0.0189 0.0138 0.0141 0.0641 0.0381 0.0448 0.2667 0.0519 0.0125 0.0162 0.0320 0.0106 0.0199 0.7240 0.0360 0.0113
past_30d
2019 0.0214 0.0210 0.0354 0.0355 0.0185 0.1202 0.2118 0.0496 0.0573 0.2882 0.1741 0.0244 0.0245 0.1068 0.0594 0.0237 1.0544 0.0706 0.0119
2020 0.0257 0.0241 0.0441 0.0416 0.0213 0.1246 0.2173 0.0792 0.0617 0.3090 0.1834 0.0287 0.0278 0.1118 0.0673 0.0282 1.3091 0.0874 0.0140
2021 0.0221 0.0203 0.0350 0.0334 0.0177 0.1180 0.2100 0.0643 0.0543 0.2755 0.1718 0.0230 0.0230 0.1051 0.0577 0.0223 1.0560 0.0709 0.0113
2022 0.0221 0.0194 0.0350 0.0321 0.0170 0.1166 0.2088 0.0489 0.0525 0.2762 0.1718 0.0222 0.0221 0.1037 0.0563 0.0221 1.0838 0.0679 0.0109
Table 3: Annual MAE Trends (2019–2022) on the MM-FinEval Benchmark.
Mistral3 3B
Rationale = [The strong execution in 2018, with signifi-
cant improvements in ROTCE (14.1%), efficiency ratio
(56.7%), and underlying EPS growth, alongside disci-
plined balance sheet growth and robust credit quality, sug-
gests strong investor confidence. The company’s strategic
initiatives like TOP programs, balance sheet optimiza-
tion, and digital transformation, combined with a pos-
itive economic outlook and prudent risk management,
should drive positive abnormal returns. The stock’s cur-
rent valuation discount relative to peers, especially in a
recession-sensitive sector, and the company’s ability to
sustain growth through organic and strategic acquisitions,
are likely to support a positive CAR.]
Prediction = [0.065]
Mistral3 8B
Rationale =Capital One’s fourth quarter 2019 earnings call
and presentation highlighted several positive yet nuanced
financial developments. The company reported strong
loan growth (7% year-over-year), solid revenue growth
(7%), and a stable credit environment, though offset by
increased provisions for credit losses (up 11%) and the
transition to CECL, which added $2.9B to the allowance.
The Walmart partnership launch, digital transformation
progress, and moderate marketing expense growth suggest
sustained growth momentum, but the CECL impact and
higher provisioning could dampen near-term profitability
expectations. The net charge-off rate remained stable at
1.93%, and the company’s disciplined capital management
and strategic investments in technology and marketing
indicate long-term value creation.
Prediction = [[ 0.025 ]]",
Mistral3 14B
Rationale = [[BNY Mellon’s earnings call highlighted
strong organic growth, innovation in digital assets and
real-time payments, and a robust capital position, which
should positively surprise investors. The guidance for
double-digit EPS growth in 2022, driven by higher net
interest revenue and fee revenue recovery, further supports
a positive market reaction.]]
Prediction = [[0.035]]
22

GPT 5.4
Rationale = [[ Kimberly-Clark delivered a clear 2020 beat
with strong EPS, margin expansion, cash flow, and im-
proved market share, but the market reaction is likely
tempered by a cautious 2021 outlook featuring only 1-2%
organic growth and significant commodity inflation that
is expected to pressure margins. The net effect should be
modestly positive because execution and restructuring/cost
savings were strong, yet guidance implies a tougher earn-
ings quality and margin backdrop ahead. ]]
Prediction = [[ 0.012 ]]
GPT 5.5
Rationale = [[ Despite record full-year results, the event
was dominated by investor concern over a Q4 EPS miss
driven by sharply higher compensation/non-comp ex-
penses, wage inflation, and weaker sequential trading
performance. Management’s commentary on continued
investment spending, capital headwinds, and limited near-
term buybacks likely reinforced negative revisions to for-
ward profitability. ]]
Prediction = [[ -0.065 ]]
Claude 4.6
Rationale = [[ PMI delivered a strong beat with Q2 ad-
justed diluted EPS of $1.57 (+17.8% organic), raised full-
year EPS guidance to $5.97-$6.07 (implying +15-17% in
dollar terms), confirmed a $5-7B share buyback program,
and announced the imminent IQOS ILUMA Japan launch
all meaningfully positive catalysts that likely exceeded
consensus expectations and drove a positive abnormal re-
turn. ]]
Prediction = [[ 0.038 ]]
Claude 4.8
Rationale = [[ WBA delivered a strong Q1 beat (adjusted
EPS $1.68, up 53%, well ahead of expectations) driven by
COVID vaccinations/testing and robust retail comps, plus
raised full-year guidance, which should be received posi-
tively despite headwinds from shrink, labor investments,
and softer underlying scripts. ]]
Prediction = [[ 0.045 ]]
V oxtral 24B
**Answer**
Rationale = The company’s strong financial performance,
with a 32% increase in comparable basis EPS excluding
canopy equity earnings, and the announcement of a $2
billion share repurchase program, are the key drivers for
the stock’s CAR. The company’s commitment to returning
$5 billion in value to shareholders through fiscal 23 also
supports a positive outlook.
Prediction = 0.035
Moss
Rationale = [[ This earnings call seems to be a ’surprising
positive’ event which can lead to a strong positive CAR. It
may provide a signal that the outlook for the company is
improving, leading to an increase in the company’s stock
price. ]]
Prediction = 0.123
Gemma4 E2B
Rationale = [[ The company reported strong retail sales
growth in Q3, driven by improved mix and digital sales,
and provided guidance indicating a strong Q3 and a cau-
tious outlook for Q4. The financial results show a positive
trend in retail sales and margin expansion, which are posi-
tive indicators for the stock. ]]
Prediction = [[ 0.025 ]]
Gemma4 E4B
Rationale = [[ The earnings call presents a positive out-
look with strong underlying sales growth and a significant
increase in adjusted segment EBIT, which should lead
to a positive market reaction. The company also high-
lights strong free cash flow and a positive ESG momentum,
which further supports a bullish sentiment. ]]
Prediction = [[ 0.035 ]]
23
