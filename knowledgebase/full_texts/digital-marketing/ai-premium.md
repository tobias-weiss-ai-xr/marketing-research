---
title: AI Premium
url: https://arxiv.org/abs/2606.30583
category: digital-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Nicola Borri
- Yukun Liu
- Aleh Tsyvinski
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.30583
pages: 85
chars: 190563
fetched_at: '2026-11-08T13:05:41+00:00'
kb_version: 1
---

# AI Premium

The Cross-Section of Stock Returns and AI Exposure
Nicola Borri, Yukun Liu, and Aleh Tsyvinski*
September 24, 2026
Abstract
We study 380 trillion tokens of realized AI consumption across more than four hundred LLMs.
We build a high-frequency AI factor and show that a long-short strategy based on firms’ AI
exposure earns significantly positive returns. The average strategy return is larger based on
intensive, frontier-oriented AI consumption but smaller based on casual or open-weight us-
age. Internationally, the return spread is significant in developed countries but insignificant
in emerging markets. Examining occupational AI exposure, we find more positive exposure
in occupations intensive in nonroutine interactive tasks and more negative exposure in those
intensive in nonroutine analytical tasks.
*Nicola Borri is with LUISS University. Yukun Liu is with the University of Rochester, Simon Business School.
Aleh Tsyvinski is with Yale University and NBER. Data provided by OpenRouter, Inc. Used under license. The anal-
ysis is based only on aggregated and anonymized derivative data constructed by the authors. The original OpenRouter
data are not redistributed or disclosed. We are grateful to OpenRouter for providing access to the data, especially to
Justin Summerville. We thank Daron Acemoglu, Andrew Atkeson, Alejandro Lopez-Lira, and Pascual Restrepo for
detailed comments, Ron Borzekowski and the Yale Data-Intensive Social Science Center for assistance in onboarding
the data. This paper was previously circulated under the title “AI Premium”.
1
arXiv:2606.30583v3  [cs.CY]  24 Sep 2026

1 Introduction
Using 380 trillion tokens of realized AI consumption across more than four hundred large lan-
guage models from the OpenRouter dataset covering approximately 2 percent of current global
monthly AI token consumption from January 2024 through April 2026, 1 we analyze how AI af-
fects firms, markets, and workers. Leveraging the unprecedented size, scope and granularity of
OpenRouter AI data, we construct and analyze a forward-looking measure of firms’ exposure to AI
consumption growth. We use this measure to study subsequent stock returns and the distribution of
AI exposure across firms, occupations, tasks, and skills. Specifically, we start by constructing the
AI Factor—a high-frequency measure of growth in realized worldwide AI consumption, of which
we further analyze its various important components. We then measure how strongly each public
firm’s equity price co-moves with this factor—firms’AI Betas(or AI exposure)—and characterize
the associated spread in subsequent average stock returns, theAI Premium.
The paper has four main parts. First, we build a high-frequency, time-varying AI factor from
the full universe of OpenRouter AI token consumption data and decompose it into its important
components: frontier closed-source versus open-weight models, core versus new users, seasoned
versus casual users, long versus short prompts, prompt-content categories (e.g., programming,
science, roleplay), and agentic versus ordinary requests. The AI factor and its different com-
ponents show that the diffusion is uneven, token consumption is concentrated in programming,
technology, and sciences, and the share of agentic tokens increased dramatically from negligible
to more than half of total AI consumption. Second, we show that AI exposure is significantly
associated with the cross-section of future stock returns, and the AI premium is both large and
heterogeneous. A value-weighted long-short strategy earns 60.4 basis points per week. We then
show that the premium extends beyond frontier model-release weeks: excluding those weeks, the
spread remains 34.3 basis points per week. Moreover, the AI premium is associated with inten-
sive, frontier-oriented AI consumption—closed-source models, paid/core and seasoned users, and
long prompts, but is not present in open-weight or casual use. Third, the AI exposure reaches
beyond technology firms into consumer-facing and capital-heavy parts of the economy: industry
exposure is most positive in retail and turns most negative in health and non-durable goods. We
1OpenRouter’s May 2026 run rate is about 100 trillion tokens per month (Das and Murphy, 2026). For comparison,
Google alone disclosed processing 3.2 quadrillion tokens per month at I/O 2026 (Pichai, 2026), so accounting for
the other major providers puts total global LLM token consumption at roughly 5 to 7 quadrillion per month and
OpenRouter at about 2 percent, also consistent with the projections by Goldman Sachs Research (Tan, 2026).
1

also show that the AI premium is larger in regions where AI development and adoption are more
advanced—about 10 basis points per week across developed markets, such as Europe, but small
and insignificant in emerging markets, including China. Fourth, we build a market-implied AI
exposure of the tasks and skills across the US economy. We show that the nonroutine, interactive
work—communication, persuasion, instruction, and the installation and repair of new systems—
loads more positively on the AI factor, and analytical, scientific, and operations-control skills load
less. Specifically, the most positive loadings are on the interaction-and-communication skills. An
occupation which is one standard deviation higher in interaction-and-communication content has
a 0.26 standard deviation higher market-implied AI exposure. Our measures are constructed using
market information, building on the literature of using stock-market prices to value innovation (Ko-
gan, Papanikolaou, Seru and Stoffman, 2017), and differ from task-based approaches (Acemoglu
and Restrepo, 2019b), usage-based approaches such as the Anthropic Economic Index (Anthropic,
2026), and survey-based approaches (Bick, Blandin, Deming, Fuchs-Schündeln and Jessen, 2026;
Baslandze, Edwards, Graham, McClure, Meyer, Sparks, Waddell and Weitz, 2026; Lindenlaub,
Oh, Rodriguez and Veldkamp, 2026).
We now provide a detailed description of the underlying data. OpenRouter, Inc. is a global
AI platform that routes requests between users and more than four hundred large language mod-
els through a single interface—from frontier closed-source models such as OpenAI’s GPT, An-
thropic’s Claude, and Google’s Gemini to open-weight models such as Meta’s Llama, DeepSeek,
and Qwen. Our licensed data is built from the universe of OpenRouter data, anonymized and aggre-
gated to the user–model–day level, from January 2024 through April 2026. For each anonymized
user, model, and day, we observe the number of requests, the completion and prompt tokens, and
the dollar cost, as well as many other characteristics. The panel covers millions of anonymized
accounts, allowing us to track individual token consumption of each anonymized user over more
than two years. Two additional features of the data are important to note. First, token consumption
in the dataset is realized consumption rather than reported consumption, since every observation
is a paid request carrying its own token count and dollar cost. Second, the dataset spans every
major provider rather than just a single model: the average user account draws on more than five
distinct AI models, and 70% of users use at least two providers. The unprecedented granularity of
the data allows us to separate frontier closed-source from open-weight AI consumption, intensive
from casual users, to identify the content category of each request, to determine agentic requests
that call external tools, and track a large variety of other salient characteristics of anonymized user
2

token consumption over time and across models. We start by building three weekly series—total
tokens, dollars spent, and distinct active users—that measure the quantity, expenditure, and breadth
of global AI consumption.2
First, using the OpenRouter data, we build an AI factor using realized AI consumption series
as the first principal component of the weekly growth rates of tokens, dollars, and active users. The
weekly AI factor loads positively and evenly on all three measures. Moreover, the user–model–
day granularity also allows us to construct separate sub-factors for different components of token
consumption by model tier, user intensity and tenure, prompt complexity, content category, and
agentic use, to study the subcomponents of AI consumption.
Second, we show that a company’s AI exposure positively and significantly predicts its future
stock returns, which we denote as the AI premium. Firms whose returns covary more positively
with the AI factor—high AI beta firms—earn higher subsequent returns: in value-weighted quin-
tile portfolios, the most exposed firms outperform the least exposed by 60.4 basis points per week,
which is significant at the 1 percent level, and by about 53 basis points after Fama-French five-
factor and momentum adjustment, which is significant at the 5 percent level. Under the Fama-
MacBeth regressions, the coefficients on the AI exposures are also positive and significant after
controlling for size, value, profitability, investment, momentum, reversal, leverage, and accruals.
Two caveats qualify this result. First, the sample covers an early, fast-moving phase of AI diffusion,
so the estimates describe realized return differences during this period. Second, data from Open-
Router, Inc., though exceptionally rich, likely overrepresents sophisticated and developer users, so
the premium is tied to the market pricing of realized observed AI consumption toward these users.
We then test whether the AI factor repackages the recent rally or potential hype in technology
stocks and AI-themed equities. Specifically, we construct first-stage AI exposures controlling for
returns to high-technology stocks, a value-weighted semiconductor portfolio, or an AI/robotics
ETF basket. The value-weighted high-minus-low spread based on these firms’ AI exposure re-
mains significant at 48.7, 35.0, and 53.1 basis points per week, respectively. The spread is also
54.1 basis points, significant at the 1 percent level, after removing the Fama-French 30 industry
component, and 69.1 basis points, significant at the 1 percent level, when the first-stage AI expo-
sure is estimated controlling for Google Trends attention to AI.
2For comparison, the Anthropic Economic Index, currently the most prominent and comprehensive public measure
of AI demand, classifies only about one million Claude conversations from a single provider over a short sample period
(Anthropic, 2026).
3

Third, we analyze the heterogeneity of the AI premium. We start by splitting AI token con-
sumption into its important components. We find that the AI premium is primarily related to
intensive, frontier-oriented AI consumption—frontier models, experienced users, and complex
tasks—rather than to casual or open-weight model usage. The AI premium is larger when ex-
posure is estimated from frontier closed-source model consumption: the high-minus-low spread is
significant at 51.6 basis points per week using closed-source AI consumption compared with 23.0
basis points for AI consumption of open-weight models. Similar results also hold across the other
measures of intensive and sophisticated AI consumption: 44.5 basis points for paid/core users ver-
sus 18.5 basis points for new users, 54.0 basis points for seasoned users versus 31.6 basis points
for non-seasoned users, and 47.7 basis points for long prompts versus 29.6 basis points for short
prompts. Next, we examine the AI premium by country. Repeating the portfolio sorting exercise
gives a significant 10.0-basis-point weekly spread in developed markets but only an insignificant
5.0-basis-point spread in emerging markets, including China. The international results are consis-
tent with the view that the premium is more pronounced in regions where listed firms and investors
are closer to the development and adoption of frontier AI.
We next examine how the AI premium varies around major model releases and whether it
extends beyond release weeks. In our event study of AI model releases, high-AI-beta firms outper-
form low-AI-beta firms around frontier-provider releases by 1.7 percent over the five-day window
and by 0.9 percent after five-factor and momentum adjustment, both of which are statistically sig-
nificant, at the 1 and 10 percent levels, respectively, while the responses to non-frontier releases
are more muted. When we instead remove the frontier model-release weeks from the sample, the
value-weighted high-minus-low spread remains positive and significant at the 5 percent level at
0.343 percent per week. That is, the premium is stronger around releases, but a significant portion
accrues gradually throughout the sample rather than only on AI release dates, suggesting that an
important fraction is not directly tied to AI news surprises.
An important paper by Kogan and Papanikolaou (2014) establishes that a premium for tech-
nology risk generically arises in models in which firm exposures to technological change are het-
erogeneous. Papanikolaou (2011) further shows that the sign of the premium depends both on
the investment-specific technology (IST) shock they study and, under recursive preferences, on
whether households prefer early or late resolution of uncertainty. The premium of the IST shock
depends on two effects: reallocation toward investment today and news about future growth. Under
late resolution, both channels lead to a negative premium of the IST shock. Under early resolution,
4

the reallocation channel carries a negative premium while the second channel carries a positive pre-
mium. That is, the sign of the premium of the IST shock depends on its composition. Kogan and
Papanikolaou (2014) infer the negative price of the IST shock from the cross-section, and Kogan,
Papanikolaou and Stoffman (2020) obtain a negative sign through limited risk sharing between in-
novators and other households. Our cross-sectional results point to a positive price of AI exposure,
and we show that AI shocks are empirically different from the IST shock. 3 The large realized AI
premium we document during a period when the AI phenomenon is rapidly unfolding is also con-
sistent with a non-risk-based mechanism: revisions during the sample to expectations about which
firms’ cash flows AI will raise or displace. The AI release date results described above bear on
both risk and non-risk interpretations. The large responses of high-exposure firms around frontier
releases suggest revisions of expectations during these release periods, while the persistence of the
spread outside release weeks indicates that it is not only confined to AI release news.
Fourth, we use the same baseline firm-level exposures to study the market-implied AI expo-
sure of different occupations and skills in the current organization of work. We first map firm
and industry exposures into occupations using BLS employment weights and then map occupa-
tions into skills using O*NET ratings. Then, we compare AI exposures of occupations with the
task taxonomies in Autor, Levy and Murnane (2003) and Acemoglu and Autor (2011), and the
skill measures in Deming (2017). We construct a market-based AI exposure for the occupations,
which is different from the technical automatability score or labor-displacement forecast that are
the focus of task- and capability-based exposure measures such as Eisfeldt, Schubert and Zhang
(2023), Kogan, Papanikolaou, Schmidt and Seegmiller (2023), and Liu, Papanikolaou, Schmidt
and Seegmiller (2025). We find that a one-standard-deviation increase in nonroutine interactive
content is associated with a significant 0.16-standard-deviation higher market-implied AI expo-
sure, suggesting that the current market implies these tasks may benefit from AI development. On
the other hand, a one-standard-deviation increase in nonroutine analytic content is associated with
a significant 0.17-standard-deviation lower exposure. Regressing AI exposure on the skill content
of occupations, we find that the coefficient estimates of social skills tend to be positive and sig-
nificant. For example, the coefficient estimate of interaction-and-communication is large at 0.26,
significant at the 1 percent level. The coefficient estimate of information use, on the other hand, is
3Our results are further consistent with the transition-risk channel of Pastor and Veronesi (2009), in which new
technologies reallocate rents across firms, sectors, and workers, and a technology’s risk becomes systematic, and
priced, once adoption is large-scale.
5

negative and significant at the 5 percent level. The market-based occupation-level AI-exposures are
significantly different from existing technical automatability measures—existing occupation-level
AI-exposure measures explain less than 2 percent of this variation.
Finally, we provide early evidence on the rise and market-implied effect of agentic AI consump-
tion, defined as models executing multi-step workflows that plan, call external tools, take actions,
and coordinate with other agents (see, e.g., Hassabis and Kavukcuoglu, 2024; Ng, 2024a,b; Yang,
Yonack, Zyskowski, Yarats, Ho and Ma, 2025). We measure this component in the OpenRouter
data as requests in which the model invokes an external tool. We document the rise in the agentic
token share from near zero in 2024 to roughly half of all tokens by the end of the sample, and the
agentic dollar share rises more slowly as the realized price per agentic token falls. The granularity
of the OpenRouter data allows us to track three salient token-level components of this activity:
tool calls, the model’s internal reasoning tokens, and cache reads of recurring prompt prefixes.
We show that tool-call and cache-read shares rise to roughly two-fifths to one-half of total token
consumption, while reasoning tokens rise more slowly. The decline in unit cost is consistent with
more usage of cache tokens and more efficient routing of agentic requests to cost-effective backing
models as firms struggle with skyrocketing AI token budgets. Moreover, in the cross-section of
equity returns, exposure to these agentic-consumption components tends to have positive, although
insignificant, point estimates for the individual agentic factors. Because these estimates are small
and imprecise since agentic token consumption is a very recent phenomenon, we interpret this
result as early and suggestive evidence of a positive agentic premium.
We next briefly relate our paper to the relevant literature. Acemoglu and Restrepo (2019a,b,
2022) provide the task-based mechanism through which automation displaces labor from some
tasks, creates new tasks, and reallocates rents across workers and firms. In asset pricing, Kogan
and Papanikolaou (2014) link technology shocks and growth opportunities to expected returns,
and Garleanu, Kogan and Panageas (2012) and Kogan, Papanikolaou and Stoffman (2020) show
that displacement risk is priced. Recent work also studies AI and market beliefs in asset prices
(Andrews and Farboodi, 2025), and Blumenfeld, Hazell, Lian and Schaab (2026) use firms’ stock-
return exposure to an AI equity index to measure the market-implied software engineering produc-
tivity gains from AI. Lopez-Lira and Tang (2026) show that large language models’ assessments
of news headlines predict initial stock-price reactions and subsequent return drift. Babina, Fedyk,
He and Hodson (2024a) show that firms investing more in AI experience higher market betas, con-
sistent with AI creating growth options. Babina, Fedyk, He and Hodson (2024b); Babina (2026)
6

measure firms’ AI efforts and study their effects on growth, innovation, and broader economic
outcomes. An important paper by Eisfeldt, Schubert and Zhang (2023) uses AI to classify task
exposure and then maps those task scores to occupations and firms. They show that the returns
of the high-exposure firms rose by about 5 percent relative to low-exposure firms after OpenAI
introduced ChatGPT, initially based on GPT-3.5, that the effect is distinct from product-market
AI exposure and stronger for firms with data assets. Our event-study evidence shows similar re-
sults. The OpenRouter–a16z report by Aubakirova, Atallah, Clark, Summerville and Midha (2025)
documents stylized facts about the structure of the token consumption market from a 100-trillion-
token OpenRouter dataset: substantial open-weight adoption, heavy use for roleplay and coding,
the rise of agentic inference, global variation, cost-use patterns, and persistent early-user cohorts.
Demirer, Fradkin, Tadelis and Peng (2025) use early scraped, aggregate data from OpenRouter’s
public website to study LLM pricing and demand. Using micro data from the AI coding platform
Cursor, Sarkar (2026) and Sarkar and Melas-Kyriazi (2026) show that AI agents shift developer
effort from implementation toward supervision and that agent usage rises sharply after model re-
leases.
2 Data
This section describes the data used in the empirical analysis. Section 2.1 introduces the Open-
Router data. Section 2.2 describes the remaining data used in the empirical analysis.
2.1 OpenRouter Data
We measure AI consumption (which we refer to interchangeably asAI use) using a panel of
realized inference requests from OpenRouter, Inc., an AI inference provider that connects users
and developers to hundreds of large language models through a single API endpoint. Users submit
a prompt and select which model runs it—an OpenAI, Anthropic, Google, Meta, DeepSeek, or
open-weight model among more than four hundred available models—and OpenRouter routes the
request to a backing provider that hosts that model. One benefit of the data is the large number of
models available on OpenRouter, making the data particularly useful for measuring aggregate AI
consumption: observed consumption is unlikely to reflect the product cycle of any single provider,
the design of any single consumer application, or the marketing strategy of any single model lab
7

(Aubakirova, Atallah, Clark, Summerville and Midha, 2025). The data are also realized rather than
reported AI consumption. That is, every observation is measured on actual paid requests.
We work with user-level OpenRouter data structured as a panel at the user–model–day level,
where model identifies a specific model version (e.g., Anthropic’s Opus 4.7 is a separate unit from
the earlier Opus 4.6). Each observation summarizes the activity of a single anonymized user with
a particular model on a particular day: for example, the total requests, prompt and completion
tokens, and dollar cost generated by a particular user when interacting with Opus 4.7 on a given
day. Importantly, the panel structure allows us to track each anonymized user’s consumption over
time, across models, and across providers. Starting from this data, we construct three weekly ag-
gregate series that capture important components of AI consumption: total tokens (the quantity of
language-model work demanded), dollar usage (the expenditure on that work, combining quantity
and the actual price paid), and distinct users (the extensive margin of adoption). Our sample covers
the weekly period from January 2024 through April 2026. Over this time period, OpenRouter in-
termediates 380 trillion cumulative tokens, which, to our knowledge, is the largest cross-provider
record of realized AI consumption available outside the model labs themselves.
The user–model–day granularity is one feature that distinguishes our panel from alternative
existing datasets, which are typically tied to a single model, provider, or product. The resulting
panel is both large and detailed, with the dataset covering millions of anonymized accounts. Most
accounts also use multiple models and providers: the average account draws on more than five
distinct models, and seven in ten accounts use at least two providers (see Internet Appendix Ta-
ble IA.1). The granularity of the data allows us to decompose AI consumption along multiple
margins we exploit in the asset-pricing tests: frontier closed-source models versus open-weight
models, paid/core users versus the rest, seasoned users versus new arrivals, and long, complex
prompts versus short ones. The same granularity also supports classification of activity by prompt-
content category and identification of requests that invoke external tools (e.g., agentic use).
Our baseline AI factor aggregates the three main AI consumption series into a single in-
dex, defined as the first principal component of their standardized weekly log growth. We use
growth rather than levels because asset returns tend to respond to the unexpected component of AI
consumption—changes in adoption and intensity—rather than to the mechanical upward trend of
a diffusing technology. The first principal component places weights of 0.665, 0.559, and 0.496
on the three series and accounts for 56.5 percent of their joint variance, so a single common factor
captures the bulk of the comovement across these three margins of AI consumption (see Internet
8

Appendix Table IA.2). Section IA.3 in the Internet Appendix also reports asset pricing results
based on the simple cross-sectional average, and each component series separately as robustness
checks, delivering similar conclusions.
Figure 1 plots weekly total token consumption on a log scale. Total tokens rise from 11.4
billion in the first week to 15.6 trillion in the final observed week, with cumulative total token
consumption of 380.8 trillion over the sample period. The growth persists during the sample and
is not concentrated around a single model release, which is consistent with steady diffusion of the
technology across users and applications.
2024 2025 2026
10B
100B
1T
10T
Start: 11.4B    End: 15.6T    Cumulative: 380.8T    x1362 growth
Total tokens
Figure 1: Weekly Total Tokens
Note:The figure plots weekly total token consumption on a log scale. Total tokens are prompt tokens plus completion
tokens. The in-figure annotation reports the first-week level, final observed-week level, cumulative total token con-
sumption of 380.8 trillion, and growth multiple. The corresponding standardized weekly log growth series is plotted
in Internet Appendix Figure IA.2.
Table 1 reports the full sample summary statistics for the AI variables (Panel A) and the firm
characteristics used in the asset pricing tests (Panel B). Panel A reports the baseline factor and its
three standardized input growth series, along with the AI sub-factors computed on different subsets
of the data:𝐴𝐼 𝐶𝑙𝑜𝑠𝑒𝑑 and𝐴𝐼 𝑂𝑝𝑒𝑛 from closed-source and open-weight model consumption,𝐴𝐼 𝐶𝑜𝑟𝑒
and𝐴𝐼 𝑁𝑒𝑤 from paid/core and new accounts,𝐴𝐼 𝑆𝑒𝑎𝑠𝑜𝑛𝑒𝑑 and𝐴𝐼 𝑁𝑜𝑛𝑠𝑒𝑎𝑠𝑜𝑛𝑒𝑑 from seasoned and
non-seasoned users, andΔln𝑇𝑜𝑘 𝐿𝑜𝑛𝑔 andΔln𝑇𝑜𝑘 𝑆ℎ𝑜𝑟𝑡 from long- and short-prompt total token
growth. We use these additional factors in the analysis of Section 3.
9

Table 1: Summary Statistics
Mean Std. p10 p25 p50 p75 p90
Panel A. AI variables
𝐴𝐼0.000 1.302 -1.561 -0.872 -0.107 0.726 1.596
Δln𝑇𝑜𝑘0.000 1.000 -1.274 -0.555 0.050 0.608 1.249
Δln𝐷𝑜𝑙0.000 1.000 -1.299 -0.609 -0.052 0.581 1.233
Δln𝑈𝑠𝑒𝑟0.000 1.000 -1.168 -0.607 0.004 0.525 1.150
𝐴𝐼𝐶𝑙𝑜𝑠𝑒𝑑 0.000 1.341 -1.555 -0.911 -0.177 0.816 1.381
𝐴𝐼𝑂𝑝𝑒𝑛 0.000 1.297 -1.422 -0.784 -0.103 0.720 1.642
𝐴𝐼𝐶𝑜𝑟𝑒 0.000 1.272 -1.343 -0.849 -0.028 0.773 1.362
𝐴𝐼𝑁𝑒𝑤 0.000 1.271 -1.516 -0.863 0.153 0.898 1.537
𝐴𝐼𝑆𝑒𝑎𝑠𝑜𝑛𝑒𝑑 0.000 1.267 -1.279 -0.884 -0.070 0.759 1.336
𝐴𝐼𝑁𝑜𝑛𝑠𝑒𝑎𝑠𝑜𝑛𝑒𝑑 0.000 1.249 -1.724 -0.709 -0.050 0.786 1.719
Δln𝑇𝑜𝑘 𝐿𝑜𝑛𝑔 0.069 0.183 -0.132 -0.053 0.064 0.184 0.295
Δln𝑇𝑜𝑘 𝑆ℎ𝑜𝑟𝑡 0.053 0.142 -0.079 -0.030 0.039 0.137 0.225
Panel B. Firm characteristics
𝑅𝑒𝑡𝑡+1 0.212 9.762 -6.667 -2.744 0.098 2.924 6.736
ln𝑀𝐸14.42 2.06 11.76 12.93 14.40 15.80 17.21
ln𝐵𝑀-0.90 1.00 -2.25 -1.51 -0.76 -0.14 0.21
𝑃𝑟𝑜𝑓𝑖𝑡0.240 0.253 0.018 0.055 0.206 0.364 0.553
𝐼𝑛𝑣0.100 0.352 -0.108 -0.024 0.037 0.121 0.298
𝑀𝑜𝑚0.086 0.421 -0.387 -0.122 0.082 0.295 0.549
Note:Panel A reports full-sample summary statistics for the weekly AI variables, and Panel B reports full-sample
summary statistics for the firm characteristics.𝐴𝐼is computed as the first principal component of standardized weekly
log growth in total tokens (Δln𝑇𝑜𝑘), usage dollars (Δln𝐷𝑜𝑙), and distinct users (Δln𝑈𝑠𝑒𝑟). The table further reports
summary statistics for AI variables based on closed- and open-weight models, paid/core and new users, seasoned and
non-seasoned users, and long- and short-prompt total-token growth.
Section IA.6 in the Internet Appendix reports additional descriptive information on other as-
pects of the data. Figure 5 decomposes total token consumption into agentic and non-agentic
consumption. Figure IA.1 reports the share of weekly tokens by prompt-content category for all
models and separately for closed- and open-weight models. Figure IA.3 plots the token share
evolution of the four model- and user-side decompositions used to compute the additional factors
reported in Panel A of Table 1.
10

2.2 Additional Data
For the U.S. equity analysis, we use CRSP common stocks listed on the NYSE, AMEX, and
Nasdaq matched to Compustat accounting data. The baseline sample keeps firms with formation-
week market capitalization of at least $1 million, and we compute weekly returns and the standard
firm characteristics: log market equity, log book-to-market, gross profitability, investment, and
momentum. For factor adjustments, we use the Fama-French five factors (Fama and French, 1993,
2015) and the momentum factor (Jegadeesh and Titman, 1993; Carhart, 1997). For industry adjust-
ments, we use the Fama-French 30 industry classification. For technology-sector returns, we use
the Fama-French 10 high-technology industry return from Kenneth French’s data library. We also
construct a semiconductor portfolio return as the value-weighted return on CRSP common stocks
in three semiconductor-related NAICS industries, as semiconductors are crucial for the develop-
ment of AI infrastructure.4
For the international analysis, we use Compustat Global common stocks split into MSCI de-
veloped and emerging markets, applying the same market-capitalization filter in U.S. dollars and
measuring returns in local currency. For the China test, we use the Datastream China A-share
dataset together with a China-specific AI factor built from mainland-China OpenRouter consump-
tion. To capture broader AI attention and traded AI exposure, we use Google Trends search interest
for the topic “Artificial intelligence” worldwide and an equal-weighted basket of seven AI- and
robotics-themed exchange-traded funds, respectively. 5 Finally, for the event-study analysis, we
hand-collect a calendar of major AI model releases from official model cards (the labs’ technical
release documentation), company blog posts, and developer announcements, separating releases
by the five frontier providers—Anthropic, DeepSeek, Google, Meta, and OpenAI—from those of
other providers. The full calendar with sources is reported in Internet Appendix Table IA.17.
3 The AI Exposure and the Cross-Section of Equity Returns
This section examines whether firms’ AI exposure is significantly related to future cross-
sectional equity returns. Section 3.1 forms portfolios sorted on firm-level AI exposure and docu-
ments the AI premium. Section 3.2 presents the results of Fama-MacBeth (Fama and MacBeth,
4NAICS 334413 (Semiconductor and Related Device Manufacturing), 333242 (Semiconductor Machinery Man-
ufacturing), and 334418 (Printed Circuit Assembly Manufacturing).
5The ETF basket includes the following ETFs: BOTZ, AIQ, IRBO, ROBO, ARTY , WTAI, and CHAT.
11

1973) cross-sectional regressions. Section 3.3 reports results on robustness tests, international evi-
dence, and heterogeneity across subcomponents of AI consumption. Section 3.4 presents firm-level
exposures within the S&P 500.
3.1 AI Portfolios
We define firm𝑖’s market-implied AI exposure at week𝑡,𝛽 𝐴𝐼 𝑖,𝑡 , as the coefficient estimate from
a rolling weekly regression of its log excess return on the baseline AI factor, controlling for the log
excess market return:
𝑟𝑒𝑡𝑖,𝜏=𝛼𝑖,𝑡+𝛽 𝐴𝐼 𝑖,𝑡×𝐴𝐼 𝜏+𝛽𝑟𝑚 𝑖,𝑡×𝑟𝑚𝜏+𝜖𝑖,𝜏, 𝜏∈W 𝑡,(1)
whereW𝑡 is the 13-week estimation window ending at formation week𝑡. The𝑡subscript on𝛽 𝐴𝐼 𝑖,𝑡
indicates that exposure is re-estimated every week and can change as investors revise forward-
looking valuations in response to AI consumption shocks. Our exposure measure is time-varying
and is inferred from realized stock price comovement.
Portfolios are formed by sorting all firms at the beginning of each week into quintiles by their
current AI exposure𝛽 𝐴𝐼 𝑖,𝑡 , with breakpoints based on the full all-stock universe, and are rebal-
anced weekly. Our baseline portfolios are value-weighted. Each quintile contains about 680 stocks
on average. We also report equal-weighted portfolios and NYSE-breakpoint robustness checks.
NYSE breakpoints follow the standard Fama-French sorting convention and reduce the influence
of smaller, less liquid non-NYSE stocks on the portfolio cutoffs (Fama and French, 1992).
Table 2 reports the properties of the quintile portfolios. The first row shows a large and statisti-
cally significant spread in AI exposure across the portfolios. The high-low spread in𝛽𝐴𝐼𝜎𝑤(𝐴𝐼)is
0.0624, significant at the 1 percent level. The five quintiles are otherwise similar in size, book-to-
market, profitability, and investment: averageln𝑀𝐸is 14.02 in the lowest-𝛽 𝐴𝐼 quintile and 14.29
in the highest,ln𝐵𝑀is−0.99versus−0.94, profitability is 0.231 versus 0.254, and investment
is 0.133 versus 0.128. The small cross-quintile differences inln𝑀𝐸and profitability are statis-
tically significant although small in magnitude. The one characteristic that differs systematically
across the quintiles is momentum:𝑀𝑜𝑚rises from 0.034 in the lowest-𝛽 𝐴𝐼 quintile to 0.138 in
the highest, a 10 percent spread that is highly significant. This pattern motivates the inclusion of
momentum among the factor-model controls in the pricing tests below.
Table 3 reports the portfolio sorting results. Panels A and B use value-weighted portfolios
12

Table 2: Properties of U.S. AI-Beta Quintile Portfolios
Low 2 3 4 High H−L
𝛽𝐴𝐼𝜎𝑤(𝐴𝐼)-0.0338 -0.0090 -0.0001 0.0083 0.0286 0.0624
t(H−L)(35.63)
ln𝑀𝐸14.02 14.65 14.59 14.73 14.29 0.27
t(H−L)(5.89)
ln𝐵𝑀-0.99 -0.92 -0.88 -0.86 -0.94 0.05
t(H−L)(1.40)
𝑃𝑟𝑜𝑓𝑖𝑡0.231 0.245 0.237 0.235 0.254 0.023
t(H−L)(3.73)
𝐼𝑛𝑣0.133 0.090 0.080 0.084 0.128 -0.006
t(H−L)(-0.90)
𝑀𝑜𝑚0.034 0.078 0.091 0.111 0.138 0.104
t(H−L)(6.22)
𝜎(𝑅) 13𝑤 0.087 0.049 0.042 0.048 0.078 -0.009
t(H−L)(-6.21)
Analyst disp. 0.364 0.208 0.164 0.175 0.298 -0.067
t(H−L)(-4.61)
# stocks 680 680 680 680 680
Note:The table reports the properties of the AI portfolios. For each formation week, firms are sorted into quintiles by
their pre-formation rolling AI beta,𝛽 𝐴𝐼. Firm betas are estimated from a 13-week rolling regression of weekly log-
excess returns on the log-excess market return and the AI factor. The𝛽 𝐴𝐼𝜎𝑤(𝐴𝐼)row reports the implied portfolio
return using the weekly AI-factor standard-deviation scale. Within each quintile, we take the cross-sectional average
of each firm characteristic, then average across formation weeks.ln𝑀𝐸is log market equity.ln𝐵𝑀is log book-to-
market.𝑃𝑟𝑜𝑓𝑖𝑡is gross profitability (revenues minus cost of goods scaled by assets).𝐼𝑛𝑣is the year-over-year change
in total assets scaled by lagged assets.𝑀𝑜𝑚is the cumulative return from week𝑡−52to𝑡−5.𝜎(𝑅) 13𝑤 is the trailing
13-week standard deviation of weekly log returns. Analyst disp. is the standard deviation of analysts’ FY1 annual
EPS forecasts divided by the absolute value of the mean forecast, using the latest IBES consensus available before the
formation week and requiring at least two analysts. The H−L column reports the time-series average of the weekly
difference between the High and Low quintile means.𝑡(𝐻-𝐿)is the corresponding time-series𝑡-statistic.
with all-stock breakpoints and NYSE breakpoints, respectively. The results are similar across
the two breakpoint choices. With all-stock breakpoints in Panel A, the high-low excess-return
spread is 60.4 basis points per week, significant at the 1 percent level. With NYSE breakpoints in
Panel B, the spread is 46.1 basis points per week, significant at the 5 percent level. Panels C and
D repeat the exercise with equal-weighted portfolios. The spreads are smaller but remain positive
and statistically significant at the 10 percent level, at 29.3 and 25.2 basis points per week. Hence,
the result is stronger for the larger companies but is not driven only by a few mega-cap firms.
Figure 2 plots the cumulative return of the high-minus-low portfolio over the sample period and
13

the mean weekly excess return of each exposure quintile, and previews the robustness of the spread
to the technology-sector, industry, and attention controls examined in Section 3.3. The spread is
also robust to standard risk adjustment. In Panel A, the alpha from the Fama–French five-factor
model (Fama and French, 2015) is 54.5 basis points per week, and the alpha from the five-factor
model augmented with momentum (Carhart, 1997) is 52.6 basis points per week, both of which
are significant at the 5 percent level.6
Additional Internet Appendix results further support this baseline portfolio evidence. Ta-
ble IA.3 repeats the portfolio sorting exercises using each of the three input series of the AI factor
(Δln𝑇𝑜𝑘,Δln𝐷𝑜𝑙,Δln𝑈𝑠𝑒𝑟) separately and finds high-low spreads of 49.4, 35.5, and 39.5 basis
points per week, respectively. Table IA.7 sorts on industry-neutral AI exposure (the difference
between𝛽 𝐴𝐼 and the within-period Fama-French 30 industry median) and finds a spread of 54.1
basis points per week, close to the 60.4-basis-point baseline. Finally, to control for broad public
attention and sentiment toward AI, Table IA.8 re-estimates𝛽 𝐴𝐼 controlling for the log growth of
Google Trends search interest in “Artificial intelligence” and finds a spread of 69.1 basis points per
week with comparable factor-model alphas.
3.2 Regression Method
The portfolio sorting results above document a return spread between high- and low-exposure
firms. Table 4 further reports estimates of the AI premium using the Fama-MacBeth procedure
(Fama and MacBeth, 1973) at the individual-stock level. Each week, we regress individual stock
returns on their pre-formation AI exposure,𝛽 𝐴𝐼 , and standard firm-level characteristics, and we
average the weekly coefficient estimates over time. The coefficient estimate on𝛽 𝐴𝐼 is our variable
of interest. Panel A weights stocks equally, so the weekly cross-sectional regressions are estimated
by OLS regressions. Panel B weights each stock by its market capitalization, so they are estimated
by weighted least squares regressions.
The point estimates of𝛽 𝐴𝐼 are positive and statistically significant across specifications. When
𝛽𝐴𝐼 is the only regressor, the coefficient estimate is 6.26, which is significant at the 10 percent
level in Panel A and 17.04, which is significant at the 1 percent level in Panel B. After controlling
for size, book-to-market, profitability, and investment rate, the coefficient estimate for AI exposure
6Internet Appendix Table IA.4 reports the factor regressions for the value-weighted, all-stock-breakpoint long-
short strategy, including factor coefficient estimates and𝑅 2 values. Internet Appendix Table IA.6 shows that the result
remains positive under block-bootstrap inference and when sorting on empirical-Bayes-shrunk AI betas.
14

Table 3: Excess Returns of AI-Beta Quintile Portfolios
Low 2 3 4 High H−L
Panel A. Value-weighted, all-stock breakpoints
Excess return -0.163 0.147 0.197 0.279 0.441 0.604
𝑡(-0.67) (0.72) (1.00) (1.31) (1.63) (2.85)
FF5𝛼-0.320 -0.007 0.001 0.073 0.224 0.545
𝑡(𝛼)(-2.43) (-0.08) (0.02) (0.90) (1.74) (2.53)
FF5+Mom𝛼-0.306 0.004 0.003 0.064 0.220 0.526
𝑡(𝛼)(-2.32) (0.05) (0.05) (0.78) (1.69) (2.44)
Panel B. Value-weighted, NYSE breakpoints
Excess return -0.037 0.110 0.249 0.275 0.424 0.461
𝑡(-0.16) (0.52) (1.25) (1.29) (1.62) (2.28)
FF5𝛼-0.196 -0.043 0.044 0.062 0.210 0.406
𝑡(𝛼)(-1.60) (-0.50) (0.55) (0.77) (1.67) (1.97)
FF5+Mom𝛼-0.174 -0.038 0.044 0.048 0.209 0.383
𝑡(𝛼)(-1.44) (-0.43) (0.55) (0.60) (1.65) (1.86)
Panel C. Equal-weighted, all-stock breakpoints
Excess return -0.113 0.097 0.173 0.163 0.180 0.293
𝑡(-0.39) (0.45) (0.89) (0.73) (0.64) (1.89)
FF5𝛼-0.231 -0.050 0.032 -0.021 -0.010 0.221
𝑡(𝛼)(-2.28) (-0.98) (0.82) (-0.40) (-0.11) (1.43)
FF5+Mom𝛼-0.208 -0.032 0.037 -0.023 -0.019 0.189
𝑡(𝛼)(-2.10) (-0.68) (0.97) (-0.43) (-0.20) (1.25)
Panel D. Equal-weighted, NYSE breakpoints
Excess return -0.075 0.123 0.174 0.169 0.177 0.252
𝑡(-0.27) (0.59) (0.88) (0.77) (0.65) (1.78)
FF5𝛼-0.198 -0.024 0.029 -0.006 -0.013 0.185
𝑡(𝛼)(-2.16) (-0.51) (0.72) (-0.11) (-0.15) (1.30)
FF5+Mom𝛼-0.173 -0.007 0.031 -0.005 -0.022 0.151
𝑡(𝛼)(-1.97) (-0.16) (0.76) (-0.10) (-0.25) (1.09)
Note:The table reports time-series properties of weekly returns on AI-beta quintile portfolios. Portfolios are rebal-
anced weekly.Excess returnis the average post-formation-week portfolio return in excess of the weekly risk-free
rate.H−Lis the spread between the High and Low AI-beta quintiles. Returns and alphas are in percent per week.
FF5 alphas are intercepts from regressing the portfolio’s post-formation-week excess return on the Fama and French
(2015) five-factor model. FF5+Mom additionally includes the momentum factor of Carhart (1997). Underall-stock
breakpoints, the quintile cutoffs are computed from the full eligible universe. UnderNYSE breakpoints, the quintile
cutoffs are computed from NYSE-listed stocks only and applied to the full universe. AI consumption data is weekly
from January 2024 through April 2026. The equity sample covers 108 formation weeks from March 2024 through
March 2026.
15

Figure 2: The AI Premium: Performance and Robustness
2024-04 2024-07 2024-10 2025-01 2025-04 2025-07 2025-10 2026-01 2026-04
0
20
40
60
80
100Cumulative return (%)
87%
Panel A
Long–short portfolio on AI exposure
Low
exposure
2 3 4 High
exposure
−0.50
−0.25
0.00
0.25
0.50
0.75
1.00
Mean excess return (% per week)
Panel B
Returns by exposure quintile
0.00 0.25 0.50 0.75 1.00
High-minus-low spread (% per week)
Baseline
High-technology
Semiconductors
Industry-demeaned
Search attention
AI ETF basket
Panel C
Robustness to alternative controls
Note:The figure summarizes the portfolio evidence on the AI premium. Firms are sorted each week into quintiles by
their current AI exposure𝛽 𝐴𝐼 𝑖,𝑡 , with breakpoints from the full eligible universe, and portfolios are value-weighted and
held for one week. Panel A plots the cumulative compounded return of the long-short portfolio that buys the highest-
exposure quintile and sells the lowest. Panel B reports the mean weekly excess return of each exposure quintile.
Panel C reports the high-minus-low weekly spread when the first-stage exposure regression adds one control at a
time: the high-technology industry return and the value-weighted semiconductor portfolio return (Table 5), exposures
demeaned within Fama-French 30 industries (Internet Appendix Table IA.7), Google Trends search attention to AI
(Internet Appendix Table IA.8), and the AI/robotics ETF basket return (Table 5). Error bars in Panels B and C are
95 percent confidence intervals. AI consumption data is weekly from January 2024 through April 2026. The equity
sample covers 108 formation weeks from March 2024 through March 2026.
16

remains positive and significant. The result is also robust to a more demanding specification,
which additionally controls for momentum, short-term reversal, leverage, and accruals. Under this
specification, the equal-weighted result is 6.69, which is significant at the 5 percent level, and the
value-weighted result is 14.11, which is significant at the 1 percent level. Thus, Table 4 provides
regression-based evidence that the AI premium is positive.
3.3 Additional Results
This subsection reports three sets of additional results. First, we show that the AI premium
is robust to controlling for technology-sector and AI-themed equity returns. Second, we examine
which subcomponents of AI consumption are most informative for asset prices. Third, we extend
the test to international markets as a cross-market check.
3.3.1 Technology-Sector and AI-Themed Controls
As a robustness test, we test whether the AI premium reflects returns to technology-sector
or AI-themed equity portfolios rather than information about AI consumption from OpenRouter.
This is especially relevant in our short sample, a period in which technology stocks and AI-themed
valuations rose sharply. We address this by re-estimating each firm’s AI exposure with one of
three traded benchmarks added to the market control: the high-technology industry return from the
Fama-French 10 industry classification, the value-weighted semiconductor portfolio return, and an
equal-weighted AI/robotics ETF basket return. We summarize these results in Table 5. Panels
A, B, and C report the results for high-low spreads for these three robustness tests. The spreads
remain positive and statistically significant at the 10% level or better across the three specifications,
at 48.7, 35.0, and 53.1 basis points per week, respectively.7 Panel C of Figure 2 plots these spreads
together with the industry-demeaned and attention-controlled spreads.
The AI factor is also empirically distinct from the conventional investment-specific technol-
ogy shock (e.g., Kogan and Papanikolaou, 2014). The results are presented in Internet Appendix
7Controlling directly for these benchmark returns, rather than adding them to the first-pass regression, leads to
the same conclusion. Internet Appendix Table IA.14 regresses the baseline value-weighted high-minus-low return on
each benchmark, alone and together with the market, the Fama-French five factors, or the five factors plus momentum.
The intercepts range from 52.6 to 60.3 basis points per week with all-stock breakpoints, all significant at the 5 percent
level, and from 38.3 to 45.7 basis points per week with NYSE breakpoints, all significant at the 10 percent level or
better.
17

Table 4: Fama-MacBeth Cross-Sectional Regressions
𝛽𝐴𝐼 ln𝑀𝐸ln𝐵𝑀Profit Inv Mom Rev Lev Accr ¯𝑅2
Panel A. Equal-weighted
(1) 6.26 0.006
t(1.84)
(2) 0.02 0.04 -0.05 -0.04 0.025
t(0.27) (0.49) (-0.81) (-0.84)
(3) 0.01 0.06 -0.04 -0.05 0.12 0.032
t(0.08) (0.80) (-0.63) (-1.18) (1.85)
(4) 5.61 0.00 0.03 -0.05 -0.03 0.031
t(1.77) (0.06) (0.44) (-0.92) (-0.83)
(5) 5.46 -0.01 0.05 -0.04 -0.05 0.11 0.038
t(1.76) (-0.13) (0.76) (-0.74) (-1.16) (1.78)
(6) -0.01 0.03 -0.03 -0.05 0.11 -0.03 -0.02 0.09 0.044
t(-0.12) (0.53) (-0.58) (-1.25) (1.83) (-0.51) (-0.58) (1.82)
(7) 6.69 -0.02 0.03 -0.04 -0.05 0.11 -0.03 -0.01 0.08 0.049
t(2.17) (-0.38) (0.42) (-0.65) (-1.23) (1.74) (-0.56) (-0.44) (1.77)
Panel B. Value-weighted
(1) 17.04 0.024
t(2.91)
(2) 0.06 0.00 0.00 0.06 0.122
t(0.70) (0.02) (0.06) (0.48)
(3) 0.04 0.02 0.01 0.03 0.12 0.161
t(0.54) (0.30) (0.16) (0.32) (0.88)
(4) 11.50 0.05 -0.02 -0.01 0.05 0.141
t(2.21) (0.60) (-0.36) (-0.12) (0.46)
(5) 10.30 0.03 0.00 0.00 0.02 0.14 0.177
t(2.03) (0.44) (-0.05) (-0.02) (0.21) (1.01)
(6) 0.05 0.00 0.00 0.02 0.09 0.07 -0.04 0.07 0.209
t(0.64) (-0.03) (0.05) (0.23) (0.69) (0.67) (-0.70) (0.72)
(7) 14.11 0.05 -0.02 -0.02 0.01 0.09 0.04 -0.05 0.04 0.222
t(2.86) (0.59) (-0.38) (-0.28) (0.11) (0.74) (0.40) (-0.79) (0.46)
Note:This table reports the second step of the Fama-MacBeth procedure, estimated at the individual-stock level. Each
week, individual stock returns are regressed cross-sectionally on the variables shown. Panel A weights stocks equally,
so the weekly regressions are estimated by OLS. Panel B weights each stock by its market capitalization, so they
are estimated by weighted least squares.𝛽 𝐴𝐼 is the pre-formation rolling AI beta estimated in the first-step return
regression. The remaining variables are firm-level characteristics included as controls.ln𝑀𝐸is log formation-week
market equity,ln𝐵𝑀is log book-to-market,𝑃𝑟𝑜𝑓𝑖𝑡is gross profitability,𝐼𝑛𝑣is asset growth,𝑀𝑜𝑚is prior52-to-5-
week return,𝑅𝑒𝑣is prior one-month return,𝐿𝑒𝑣is long-term debt to assets, and𝐴𝑐𝑐𝑟is accruals. Characteristics are
weekly cross-sectionally winsorized at the1st/99th percentiles and standardized to unit variance. Reported coefficients
are time-series averages of the weekly cross-sectional estimates.𝑡-statistics are reported in parentheses and are time-
series𝑡-tests of those estimates (Fama and MacBeth, 1973). The ¯𝑅2 column is the time-series average of weekly
cross-sectional𝑅 2. AI consumption data is weekly from January 2024 through April 2026. The equity sample covers
108 formation weeks from March 2024 through March 2026.
18

Table IA.22. Net of the market, its correlation with the investment-minus-consumption (IMC)
portfolio ranges from−0.02to−0.14across different industry classification vintages, and firms’
AI betas are weakly and negatively related to their IMC betas. We also show that the AI premium
remains 49 to 52 basis points per week after controlling for IMC, the Fama-French five factors,
and momentum.
Table 5: High-Tech-, Semiconductor-, and AI-ETF-Controlled AI-Beta Quintile Portfolios
Low 2 3 4 High H−L
Panel A. FF10 HiTec industry as control
Excess return 0.020 0.145 0.125 0.198 0.508 0.487
𝑡(0.09) (0.72) (0.62) (0.94) (1.82) (2.50)
FF5𝛼-0.121 -0.037 -0.050 -0.029 0.298 0.419
𝑡(𝛼)(-0.96) (-0.48) (-0.74) (-0.36) (2.45) (2.20)
FF5+Mom𝛼-0.098 -0.025 -0.060 -0.029 0.278 0.376
𝑡(𝛼)(-0.79) (-0.33) (-0.89) (-0.36) (2.30) (2.02)
Panel B. NAICS semiconductor industry as control
Excess return 0.030 0.234 0.092 0.233 0.380 0.350
𝑡(0.12) (1.13) (0.45) (1.07) (1.47) (1.75)
FF5𝛼-0.140 0.084 -0.114 0.003 0.158 0.298
𝑡(𝛼)(-1.06) (1.05) (-1.50) (0.03) (1.31) (1.46)
FF5+Mom𝛼-0.122 0.096 -0.108 -0.004 0.138 0.260
𝑡(𝛼)(-0.93) (1.20) (-1.41) (-0.05) (1.15) (1.29)
Panel C. AI ETF basket as control
Excess return -0.014 0.049 0.225 0.219 0.517 0.531
𝑡(-0.06) (0.24) (1.17) (1.00) (1.91) (2.58)
FF5𝛼-0.169 -0.115 0.028 0.018 0.300 0.469
𝑡(𝛼)(-1.36) (-1.36) (0.37) (0.21) (2.29) (2.23)
FF5+Mom𝛼-0.139 -0.108 0.033 0.006 0.290 0.429
𝑡(𝛼)(-1.15) (-1.27) (0.43) (0.08) (2.20) (2.07)
Note:All panels report value-weighted quintile sorts using all-stock breakpoints. Panel A expands the first-pass
regression to include the Fama-French 10-industry HiTec return:𝑟𝑒 𝑖,𝑡 =𝑎+𝑏 mkt𝑟𝑒 𝑚,𝑡+𝑏 HiTec𝑟𝑒 HiTec,𝑡+𝑏 AI𝐴𝐼𝑡. Panel B
instead controls for the value-weighted weekly log return on the U.S. semiconductor industry:𝑟 𝑒 𝑖,𝑡 =𝑎+𝑏 mkt𝑟𝑒 𝑚,𝑡+
𝑏semi𝑟semi,𝑡+𝑏 AI𝐴𝐼𝑡. Panel C controls for the equal-weighted AI ETF basket return:𝑟𝑒 𝑖,𝑡 =𝑎+𝑏 mkt𝑟𝑒 𝑚,𝑡+𝑏 ETF𝑟𝑒 ETF,𝑡+
𝑏AI𝐴𝐼𝑡. Returns and alphas are in percent per week. AI consumption data is weekly from January 2024 through April
2026. The equity sample covers 108 formation weeks from March 2024 through March 2026.
19

3.3.2 Important Components of AI Consumption
A unique feature of the OpenRouter AI dataset is its granularity. For each anonymized user
and model on each day, we observe realized requests, tokens, and dollar usage. This user–model–
day structure lets us ask which components of AI consumption best capture the AI premium.
We decompose AI consumption along four margins: closed-source versus open-weight models,
paid/core versus new accounts, seasoned versus non-seasoned users, and long versus short prompts.
For each of the resulting eight specific AI factors, we re-estimate firm-level exposures and sort
firms on that exposure separately. Table 6 reports the resulting high-minus-low spreads.
The four subcomponents are about different margins of AI consumption. First, following Open-
Router’s model taxonomy, closed-source models are proprietary or restricted-API models whose
weights are not publicly released, while open-weight models have publicly available weights. Sec-
ond, paid/core users are defined as the accounts with at least 13 weeks of tenure, at least eight prior
active weeks, at least $10 of prior OpenRouter usage, and activity in at least two of the previous
eight weeks. New users are accounts with less than four weeks of tenure, and middle/developing
accounts are excluded from this split. Third, seasoned users are a broader experience measure: be-
fore week𝑡, they have been observed for at least 13 weeks, were active in at least eight prior weeks,
and made at least 20 prior requests. The remaining active users are non-seasoned. Finally, long
prompts are requests above the prior-13-week rolling 75th percentile of prompt length, and short
prompts are the remaining requests. We make sure that all user and prompt-length classifications
are predetermined using information available before the portfolio-formation week.
The pattern is consistent across the four splits: the estimated AI premium is larger for exposure
to more intensive, frontier-oriented AI consumption. The high-low spread is 51.6 basis points per
week based on exposure to closed-source model consumption versus 23.0 basis points based on
open-weight consumption (Panel A), 44.5 basis points versus 18.5 basis points based on paid/core
accounts versus new accounts (Panel B), 54.0 basis points versus 31.6 basis points based on sea-
soned versus non-seasoned users (Panel C), and 47.7 basis points versus 29.6 basis points based
on long- versus short-prompt token growth (Panel D). The AI premium is better captured by AI
consumption on frontier models, among experienced users, and for complex tasks, rather than on
casual consumption.
20

Table 6: AI-Beta Quintile Portfolios by Salient Consumption Components
Panel A. AI model class
𝛽𝐴𝐼,𝐶𝑙𝑜𝑠𝑒𝑑 𝛽𝐴𝐼,𝑂𝑝𝑒𝑛
Low 3 High H−L Low 3 High H−L
Excess return -0.037 0.229 0.479 0.516 0.091 0.278 0.322 0.230
𝑡(-0.15) (1.09) (1.77) (2.52) (0.36) (1.55) (1.18) (1.30)
FF5𝛼-0.195 0.047 0.238 0.432 -0.119 0.090 0.107 0.225
𝑡(𝛼)(-1.38) (0.59) (2.21) (2.09) (-1.07) (1.20) (0.93) (1.25)
FF5+Mom𝛼-0.180 0.056 0.231 0.411 -0.112 0.092 0.113 0.225
𝑡(𝛼)(-1.28) (0.70) (2.14) (1.98) (-1.00) (1.22) (0.97) (1.23)
Panel B. Paid/core versus new users
𝛽𝐴𝐼,𝐶𝑜𝑟𝑒 𝛽𝐴𝐼,𝑁𝑒𝑤
Low 3 High H−L Low 3 High H−L
Excess return -0.046 0.164 0.398 0.445 0.110 0.210 0.294 0.185
𝑡(-0.19) (0.80) (1.17) (1.72) (0.36) (0.97) (1.03) (0.78)
FF5𝛼-0.226 -0.016 0.144 0.370 -0.138 0.016 0.098 0.236
𝑡(𝛼)(-1.55) (-0.19) (0.96) (1.54) (-0.98) (0.20) (0.75) (1.09)
FF5+Mom𝛼-0.203 -0.016 0.150 0.354 -0.125 0.019 0.092 0.218
𝑡(𝛼)(-1.40) (-0.19) (1.00) (1.46) (-0.89) (0.24) (0.69) (1.00)
Panel C. Seasoned versus non-seasoned users
𝛽𝐴𝐼,𝑆𝑒𝑎𝑠𝑜𝑛𝑒𝑑 𝛽𝐴𝐼,𝑁𝑜𝑛𝑠𝑒𝑎𝑠𝑜𝑛𝑒𝑑
Low 3 High H−L Low 3 High H−L
Excess return -0.079 0.255 0.460 0.540 0.024 0.101 0.340 0.316
𝑡(-0.31) (1.22) (1.32) (2.11) (0.07) (0.44) (1.18) (1.48)
FF5𝛼-0.243 0.101 0.196 0.439 -0.202 -0.093 0.117 0.320
𝑡(𝛼)(-1.66) (1.17) (1.21) (1.79) (-1.35) (-1.07) (0.94) (1.49)
FF5+Mom𝛼-0.238 0.105 0.209 0.447 -0.191 -0.099 0.090 0.281
𝑡(𝛼)(-1.61) (1.19) (1.28) (1.81) (-1.26) (-1.13) (0.73) (1.32)
Panel D. Prompt length
𝛽𝑇𝑜𝑘,𝐿𝑜𝑛𝑔 𝛽𝑇𝑜𝑘,𝑆ℎ𝑜𝑟𝑡
Low 3 High H−L Low 3 High H−L
Excess return -0.040 0.316 0.437 0.477 0.150 0.203 0.446 0.296
𝑡(-0.17) (1.53) (1.60) (2.16) (0.57) (1.03) (1.62) (1.65)
FF5𝛼-0.228 0.122 0.206 0.433 -0.021 -0.031 0.228 0.249
𝑡(𝛼)(-1.63) (1.34) (1.60) (1.93) (-0.18) (-0.44) (1.78) (1.35)
FF5+Mom𝛼-0.191 0.132 0.172 0.363 -0.022 -0.031 0.237 0.259
𝑡(𝛼)(-1.42) (1.44) (1.39) (1.72) (-0.19) (-0.43) (1.84) (1.40)
Note:This table reports value-weighted, all-stock-breakpoint quintile sorts on split-specific AI exposures. Panels A–
D compare closed- and open-weight model consumption, paid/core and new accounts, seasoned and non-seasoned
users, and long- and short-prompt token growth, respectively (see Section 3.3.2 for the definitions of the groups).
For compactness, the table reports the Low, middle (3), High, and High-minus-Low portfolios. Quintiles 2 and 4 are
omitted. Returns and alphas are in percent per week. AI consumption data is weekly from January 2024 through April
2026. The equity sample covers 108 formation weeks from March 2024 through March 2026.
21

3.3.3 International Evidence
We next extend the test to international markets. We ask whether the AI premium is only a
US phenomenon and, if not, whether it is concentrated in the markets closer to leading-edge AI
development, infrastructure, and commercial deployment. This builds on the “distance to frontier”
framework of Acemoglu, Aghion and Zilibotti (2006), in which an economy’s position relative to
the global technology frontier shapes its innovation and growth dynamics. In our setting, the local
equity markets whose listed firms and investors are closer to AI development and deployment are
what we consider the AI frontier markets. Based on the transition-risk view (Pastor and Veronesi,
2009), if AI exposure matters more for firms and investors nearer the frontier, the spread may be
larger there. We define a local market as a country-level equity market. Using Compustat Global
common stocks, each week and separately within each local market, we sort stocks into quintiles
by AI exposure. We then compute the high-low return spread within each local market and average
these local-market spreads across markets classified by MSCI as developed or emerging.
Panel A of Table 7 combines both local markets classified by MSCI as developed and emerging.
The overall international high-low spread is 7.3 basis points per week, with a significant local-
market alpha of 7.8 basis points. Panels B and C show that this average is mainly driven by
developed local markets. In developed markets, the average high-low spread is 10.0 basis points
per week with a 10.8-basis-point local-market alpha, both statistically significant at the 5% level.
In emerging local markets, the average spread is 5.0 basis points per week and is statistically
insignificant. The results suggest that the AI premium is more pronounced in developed equity
markets, which may be closer to the global AI frontier.
China is a particularly interesting test because Chinese AI consumption has become an impor-
tant share of the global total AI consumption and AI is highly salient to local investors in China.
Internet Appendix Table IA.15 examines China A-shares, sorting either on the baseline AI factor
or on a China-specific AI factor built from mainland-China OpenRouter consumption. In both
specifications, the high-minus-low spreads are negative and statistically insignificant.
3.3.4 Event-Study Evidence
AI is a recent phenomenon, and a series of unanticipated positive surprises could, in principle,
explain part of the observed average excess return. If high-AI-beta firms are those who benefit
most as AI advances, then AI advancing faster than the market expected would also be consistent
22

Table 7: International AI-Beta Quintile Portfolios
Low 2 3 4 High H−L
Panel A. Full international sample
Excess return 0.141 0.157 0.138 0.199 0.214 0.073
𝑡(1.52) (1.95) (2.17) (2.47) (2.36) (2.79)
Local-mkt𝛼0.022 0.051 0.054 0.093 0.101 0.078
𝑡(𝛼)(0.46) (1.34) (1.79) (2.41) (2.00) (2.98)
Panel B. MSCI Developed
Excess return 0.129 0.166 0.126 0.194 0.228 0.100
𝑡(1.10) (1.68) (1.70) (2.02) (2.07) (2.52)
Local-mkt𝛼0.013 0.061 0.049 0.093 0.121 0.108
𝑡(𝛼)(0.21) (1.42) (1.44) (2.15) (1.94) (2.75)
Panel C. MSCI Emerging
Excess return 0.151 0.149 0.147 0.201 0.201 0.050
𝑡(1.71) (1.95) (2.29) (2.61) (2.28) (1.32)
Local-mkt𝛼0.041 0.050 0.066 0.103 0.093 0.053
𝑡(𝛼)(0.70) (1.04) (1.57) (2.08) (1.55) (1.36)
Note:The table reports returns and local-market alphas for international pre-formation AI-beta-sorted quintile portfo-
lios. A local market is a country-level equity market. Panel A pools local markets classified by MSCI as developed
or emerging (the full international sample), and excludes frontier, standalone, and not-rated markets. Panel B restricts
the sample to developed local markets and Panel C to emerging local markets. For each local market and week, stocks
are sorted into quintiles using local-market breakpoints, and quintile returns are equal-weighted across firms. H−L is
formed within each local market. Portfolio returns and H−L spreads are then equal-weighted across local markets.
Firm betas are 13-week rolling log-excess regressions of weekly local-currency returns on the local-market log-excess
return and the AI factor. Daily returns are JKP-style (Jensen, Kelly and Pedersen, 2023) winsorized using same-month
CRSP cutoffs before weekly compounding.Local-mkt𝛼is the intercept from regressing the portfolio’s next-week re-
turn on the value-weighted market return of the included local markets. AI consumption data is weekly from January
2024 through April 2026. Equity betas use 13-week rolling windows, so portfolio formation weeks begin in March
2024.
with high realized returns over our sample. We provide two complementary results on the timing
of the return spread: an event study around AI model releases, and an analysis that removes release
weeks from the sample.
First, we use major AI model releases as the news events, separating releases by the five fron-
tier providers—Anthropic, DeepSeek, Google, Meta, and OpenAI—from those of other providers,
and compare the cumulative abnormal returns (CARs) of high- and low-AI-beta firms in narrow
windows around release dates. Our constructed release calendar, containing 29 frontier and 36
non-frontier events, is reported in the Internet Appendix (Table IA.17). Figure 3 plots the high-
23

minus-low CAR difference from five days before to ten days after each release, with 95 percent
confidence intervals. The effect is concentrated in frontier-provider releases (Panel A): the CAR
difference reaches about 3.5 percent, with evidence of pre-drift before the release and a plateau
about five days after, and is statistically significant within the window. For non-frontier releases
(Panel B), it reaches only about 2 percent, with little pre-drift. These results support the interpre-
tation of AI beta as a measure of firms’ sensitivity to economically important AI developments.
We report the full set of risk-adjusted CAR differences across event windows in the Internet Ap-
pendix (Table IA.16). Using the [0,+5] window, high-AI-beta firms outperform low-AI-beta firms
around frontier-provider releases by 1.7 percent over the five-day window and by 0.9 percent after
five-factor and momentum adjustment, both of which are statistically significant, at the 1 and 10
percent levels, respectively, while the responses to non-frontier releases are more muted.
Second, we remove the model-release weeks from the sample and re-examine the AI premium
result. If the premium were primarily about the ex-post realization of AI news, it should be con-
centrated in those weeks, and excluding them should eliminate the AI premium. Table 8 repeats
the value-weighted quintile sort with these weeks excluded, identified from the model-release cal-
endar in Table IA.17. Dropping weeks with a frontier-provider release, the high-minus-low spread
remains positive and significant at the 5 percent level at 0.343 percent per week, and additionally
dropping non-frontier-release weeks leaves 0.331 percent per week that is significant at the 10 per-
cent level. In both cases, the high AI-beta quintile has a higher average return than the low quintile.
The premium is stronger around releases, as the event study shows, but an important fraction of it
accrues gradually throughout the sample rather than only on model release news dates.
Overall, we find that firms with higher AI exposure earn higher future returns than firms with
lower exposure. These findings can be interpreted through the framework of Kogan and Papaniko-
laou (2014), in which technological change creates heterogeneous firm exposures and gives rise to
a technology-risk premium. As Papanikolaou (2011) shows, the sign of the technology-risk pre-
mium depends on the nature of the shock and, under recursive preferences, on whether households
prefer early or late resolution of uncertainty. For the investment-specific technology (IST) shock
they study, reallocation toward investment today and news about future growth are both priced neg-
atively under late resolution. Under early resolution, reallocation is priced negatively and growth
news positively, making the sign depend on the shock’s composition. The negative price of IST
risk is inferred from the cross-section in Kogan and Papanikolaou (2014) and arises through lim-
ited risk sharing between innovators and other households in Kogan, Papanikolaou and Stoffman
24

−5 −4 −3 −2 −1 0 1 2 3 4 5 6 7 8 9 10
Trading days from frontier model release
0
1
2
3
4
5Cumulative H−L return (%)
Long-short PC3-β portfolio around frontier AI model releases (T = 29 events, VW)
High − Low PC3-β
±1.96 SE
(A) Frontier Model Releases (29 Events)
−5 −4 −3 −2 −1 0 1 2 3 4 5 6 7 8 9 10
Trading days from non-frontier model release
−0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Cumulative H−L return (%)
Long-short PC3-β portfolio around non-frontier AI model releases (T = 36 events, VW)
High − Low PC3-β
±1.96 SE
(B) Non-Frontier Model Releases (36 Events)
Figure 3: Cumulative Average Returns Around AI Model Releases
Note:Daily event-time CAARs to the value-weighted, all-stock-breakpoint long-short AI-𝛽quintile portfolio. In each
panel, firms are sorted on their pre-event 13-week rolling log-excess AI beta and the H−L spread is the High-quintile
minus Low-quintile cumulative return. Time is measured in trading days from the event anchor (same-or-next trading
day on or after the announced release date). The shaded band is the±1.96cross-event standard error of the cumulated
H−L return at each event-time day. Panel A uses the 29 frontier-model events of Table IA.17 Panel A; Panel B uses the
36 non-frontier-model events of Table IA.17 Panel B. Both panels are value-weighted. AI consumption data is weekly
from January 2024 through April 2026. The equity sample covers 108 formation weeks from March 2024 through
March 2026.
25

Table 8: AI-Beta Quintile Portfolios Excluding Model-Release Weeks
Low 2 3 4 High H−L
Panel A. Excluding frontier-release weeks
Excess return 0.022 0.093 0.158 0.228 0.365 0.343
𝑡(0.10) (0.48) (0.77) (1.13) (1.48) (2.15)
Panel B. Excluding frontier and non-frontier release weeks
Excess return -0.096 0.035 0.030 0.146 0.235 0.331
𝑡(-0.35) (0.13) (0.12) (0.65) (0.68) (1.68)
Note:The table reports weekly value-weighted excess returns on AI-beta quintile portfolios, all-stock breakpoints,
after excluding weeks that contain major AI model releases. Panel A excludes holding weeks with a frontier-provider
release (Anthropic, DeepSeek, Google, Meta, OpenAI); Panel B additionally excludes weeks with releases from other
providers. The sorting signal, universe, and portfolio construction match Table 3.H−Lbuys the High and shorts the
Low AI-beta quintile. Returns are in percent per week; Newey–West𝑡-statistics with five lags are in parentheses.
(2020). Our results point to a positive price of AI exposure and show that AI shocks are empiri-
cally distinct from the IST shock. The findings are also consistent with the transition-risk channel
of Pastor and Veronesi (2009), in which new technologies reallocate rents across firms, sectors, and
workers, and technological risk becomes systematic and priced once adoption is large-scale. Con-
sistent with this interpretation, the AI premium is concentrated in frontier-oriented AI consumption
and developed markets, where AI risk may be most systematic.
The large realized AI premium during this period of rapid AI development may also reflect
revisions to expectations about which firms’ cash flows AI will raise or displace. The release-date
evidence bears on both interpretations. The large responses of high-exposure firms around frontier
releases suggest revisions to expectations during these periods. The spread nevertheless persists
outside release weeks, indicating that it is not confined to AI release news.
3.4 Firm-Level AI Exposure
The rolling regressions used in the portfolio tests also give us a firm-level measure of AI ex-
posure. For each firm, we estimate𝛽 𝐴𝐼 from weekly stock returns and then average the estimated
exposure across valid formation weeks. This allows us to move beyond portfolios and ask which
individual firms’ returns comove most strongly with innovations to AI consumption.
Figure 4 reports these exposures. Panel A shows the value-weighted average exposure for
the Fama-French 10 industries, expressed as the weekly industry return in percentage points as-
sociated with a one-standard-deviation AI-factor shock. Most industries have positive exposure,
26

with the largest values in retail. Non-durable goods and health have negative exposure, and the
high-technology industry average is close to zero.8 Panel B shows the fifteen S&P 500 firms with
the most positive and the fifteen with the most negative average exposure, with firms in the high-
technology industry highlighted.9
The highest-ranked firm, AppLovin, a software company whose platform helps mobile-app
developers advertise and monetize apps, has the highest estimated positive AI exposure among
current S&P 500 firms. At the other extreme, Moderna, a biotechnology firm focused on mRNA
medicines and vaccines, has the most negative estimated AI exposure. The positive tail also in-
cludes natural AI-infrastructure names such as Western Digital and Lumentum, digital-platform
and travel firms such as Expedia, and power firms such as NRG Energy. The negative tail includes
Estée Lauder, as well as technology and semiconductor firms such as AMD and ON Semicon-
ductor. The main point of this result is that firm-level AI exposure is not the same as a simple
technology-sector classification, our AI exposure measure identifies firms whose returns covary
with AI consumption across many parts of the economy.
4 AI Exposure across Occupations, Tasks and Skills
This section provides the occupation-level, task-level, and skill-level counterparts of the firm-
level results. We use the firm-level AI betas to link market-implied AI exposure to occupations,
tasks and skills in the current organization of work. We proceed in two steps. First, we map
the firm-level AI betas into occupations using BLS occupation-by-industry employment weights
(the occupation ranking is in Internet Appendix Figure IA.11). Second, we map these occupation
exposures into skills using O*NET, the U.S. Department of Labor database that describes the
tasks, abilities, and skills used in detailed occupations, or the skill-importance ratings for each
occupation.
The firm-level AI exposure comes directly from stock returns and AI-consumption innovations
as described above, the occupation mapping adds employment weights, and the skill mapping adds
O*NET skill-importance ratings. In the end, this procedure produces a market-based measure of
AI exposure for occupations and skills. This measure is thus different from worker surveys, expert
8Internet Appendix Figure IA.6 shows that the coefficient estimates on the AI factor based on industry-level
regressions. Similarly, the health and non-durable goods are at the bottom and retail is near the top.
9Internet Appendix Figure IA.7 reports the full ranking of the top and bottom 50 S&P 500 firms on a common
radial scale, and Internet Appendix Figure IA.5 reports industry exposures for the AI factor and its subcomponents.
27

Figure 4: AI Exposure across Industries and Firms
−0.4 −0.2 0.0 0.2
Response to a one s.d. AI shock
(% per week)
Health
Non-durable goods
High technology
Energy
Manufacturing
Telecoms
Utilities
Consumer durables
Other
Retail & wholesale
near zero on average
Panel A
Industries
−2 −1 0 1 2
Response to a one s.d. AI shock
(% per week)
Moderna
Estée Lauder
Skyworks
AMD
ON Semiconductor
Charles River Labs
Danaher
Chipotle Mexican Grill
Eli Lilly
Monolithic Power
First Solar
Albemarle
Nike
Aptiv
Revvity
Seagate Technology
Western Digital
F5
NRG Energy
EQT
Parker Hannifin
Tapestry
Expedia
Insulet
Expand Energy
Cummins
Baker Hughes
Lumentum
Carvana
AppLovin
Panel B
Firms
High technology
All other industries
Note:The figure reports market-implied AI exposure, the coefficient on the AI factor in 13-week rolling regressions of
a firm’s weekly log-excess return on the AI factor and the log-excess market return. Values are the return response, in
percentage points per week, to a one-standard-deviation AI-factor shock. Panel A reports the value-weighted average
exposure for the Fama-French 10 industries, using formation-week market equity weights. Panel B reports the fifteen
current S&P 500 firms with the most positive and the fifteen with the most negative average exposure, with firm-level
exposures averaged across all weeks in which a firm has a valid estimate. Bar colors indicate whether the firm belongs
to the Fama-French high-technology industry. Internet Appendix Figure IA.7 reports the full ranking of the top and
bottom 50 firms. AI consumption data is weekly from January 2024 through April 2026. The equity sample covers
108 formation weeks from March 2024 through March 2026.
28

labels, or AI labels which ask AI models to judge which skills are exposed. To the best of our
knowledge, this is the first exercise that uses realized AI consumption and equity market valuations
to build a market-implied occupation and skill-level measure of AI exposure.
Table 9 compares the market-implied occupation exposures with task and skill measures from
the literature on technological change and the demand for labor. Tasks are the activities a job
involves, and skills are the worker capabilities those activities require. Columns (1) and (2) of the
table use task-content measures. Column (1) follows the work of Autor, Levy and Murnane (2003)
and assigns each occupation four scores: routine, nonroutine analytic, nonroutine interactive, and
manual/physical. Column (2) keeps the two nonroutine cognitive measures and splits the rest into
routine cognitive, routine manual, and nonroutine manual, following the five-group taxonomy of
Acemoglu and Autor (2011). Columns (3) through (5) assign the skill-based measures of Deming
(2017) to each occupation, including the three headline measures in column (3) (social skills,
nonroutine analytical and mathematical content, and routine tasks), the interaction between social
skills and analytical content that captures his social-cognitive complementarity in column (4), and
the full set of ten O*NET task and skill measures in column (5). All variables are standardized, so
coefficients are in standard-deviation units.
We find a similar pattern across these different task and skill taxonomies, from the routine ver-
sus nonroutine split of Autor, Levy and Murnane (2003) and Acemoglu and Autor (2011) to the
skill-based measures of Deming (2017). Market-implied AI exposure is positive on nonroutine in-
teractive tasks and social skills, suggesting that the current market implies these skills may benefit
from AI development. On the other hand, AI exposure is negative for nonroutine analytical and
math tasks. Specifically, in column (1), the coefficient estimate to nonroutine interactive content is
positive and significant at 0.16 and the coefficient estimate to nonroutine analytic content is neg-
ative and significant at−0.17. The Deming measures in column (3) show the same pattern, the
coefficient estimate is0.11for social skills and is−0.14for nonroutine analytical and math, both
statistically significant. The coefficient estimates to composite routine and manual measures in
column (1) are small and insignificant, but splitting them in more detail in column (2) shows two
offsetting effects: routine manual content has a strongly negative coefficient (−0.36) and nonrou-
tine manual content a positive one (0.30), in line with the installation and repair skills near the top
of Figure IA.11 in the Internet Appendix, and the two nonroutine cognitive coefficients keep their
signs and significance. Column (4) shows that the interaction between social skills and analytical
and math content is small and insignificant. In other words, AI exposure is associated with social
29

skills directly, not with the social-cognitive combination that Deming (2017) emphasizes. Column
(5) splits the composite measures into ten task and skill measures and shows where the pattern
comes from in detail. The positive coefficient comes from interaction/communication tasks, at
0.26 (significant at the 1 percent level), and the negative coefficients from deductive and inductive
reasoning and from information use. That is, with this finer measure, the composite analytical and
math measure of an occupation is no longer significantly associated with the AI exposures of the
occupation. Service tasks also have a negative coefficient, in line with the negative AI exposure of
healthcare occupations in Internet Appendix Figure IA.11.
The positive coefficients on nonroutine interactive tasks and social skills indicate that market-
implied AI exposure is concentrated in occupations built around communication, persuasion, in-
struction, and coordination. The negative coefficients on nonroutine analytical and math content,
deductive and inductive reasoning, and information use indicate that this AI exposure is not only
a measure of abstract analytical or scientific work. If anything, the occupations most intensive
in those tasks have the most negative AI exposure. Overall, the explanatory power using these
existing task and skill measures of occupations is modest, where task and skill contents explain
between 2 and 11 percent of the cross-sectional variation in market-implied AI exposure. Jones
and Tonetti (2026) build on the task framework and emphasize that output is constrained by tasks
where labor improves only slowly relative to capital—the “weak links” that bind even when most
other tasks are automated. The positively-exposed skills in our map—interaction, persuasion, in-
struction, installation and repair—may be the weak links the market expects to bind production as
AI automates other tasks.
Table 10 reports regressions of the market-implied ranking on existing occupation-level mea-
sures of AI exposure. Column (1) uses three technical measures: the ability-based AI occupational
exposure of Felten, Raj and Seamans (2021), the GPT-4 task-exposure measure of Eloundou, Man-
ning, Mishkin and Rock (2023), and the patent-based measure of Webb (2020). Column (2) uses
the generative-AI task exposure of Eisfeldt, Schubert and Zhang (2023), split into exposure through
core tasks, which they tie to labor substitution, and exposure through supplemental tasks, which
they tie to complementarity. Column (3) combines the five measures. We find that market-implied
AI exposure is largely unrelated to these technical automatability measures. Its correlation with
each is below 0.08 in absolute value, and no specification explains more than 2 percent of the
cross-sectional variation. The coefficient estimate to the GPT-4 exposure measure is positive and
significant at 0.13, and the coefficient estimates to the Eisfeldt, Schubert and Zhang (2023) mea-
30

sures are small and statistically insignificant. The coefficient estimates to the Felten, Raj and
Seamans (2021) and Webb (2020) measures are significantly negative. In the combined column,
the coefficient estimates to the GPT-4 and Eisfeldt, Schubert and Zhang (2023) measures become
individually insignificant, while the coefficient estimates to the Felten, Raj and Seamans (2021)
and Webb (2020) measures stay significantly negative.
5 The Rise of Agentic AI Consumption
This last section presents early evidence on the rise of agentic AI consumption—models exe-
cuting multi-step workflows by planning, calling external tools, taking actions, and coordinating
with other agents (see, e.g., Ng, 2024a,b). Tool use is especially central for this measurement—a
model becomes agentic when it is given functions it can request to call in order to gather informa-
tion, manipulate data, or take action. We measure the agentic component of AI consumption in the
OpenRouter data as requests whose normalized finish reason istool_calls, in which the model
invoked an external tool.
These agentic requests have grown rapidly. Figure 5 plots weekly agentic and non-agentic
token volumes from January 2024 through April 2026. Both series scale up by several orders of
magnitude over the sample, but agentic tokens grow faster. The agentic share is small in 2024,
rises sharply through 2025 and into 2026, and reaches 52.2 percent of total tokens by the latest full
week (see also Yang, Yonack, Zyskowski, Yarats, Ho and Ma, 2025).
Figure 6 plots agentic token volume against the realized dollars per agentic token over the
same period. V olume rises by orders of magnitude, while the realized dollars per token decline
at the same time. Two forces compress the per-token price: prompt caching serves prefix tokens
without recomputing them through the model, and providers route agentic requests toward cheaper
backing models. Both forces reduce the revenue earned on each agentic token even as agentic
usage expands.
Internet Appendix Figure IA.8 brings these two patterns together. Panel A plots the agentic
share of total tokens against its share of total usage dollars. The token share rises much faster than
the dollar share, because volume growth (Figure 5) outpaces the per-token price decline (Figure 6).
Panel B plots three token-level salient components of agentic activity, each as a share of total
tokens. The tool-call share counts tokens on requests that call an external tool. The cache-read
share counts prompt prefixes the platform serves from cache rather than recomputing through
31

Table 9: Market-Implied Occupation Exposure and Task and Skill Measures
Task content Skill content
(1) (2) (3) (4) (5)
ALM Acemoglu-Autor Deming+interaction detailed
Routine 0.004
(0.09)
Nonroutine Analytic -0.172*** -0.230***
(-4.02) (-4.67)
Nonroutine Interactive 0.163*** 0.116**
(3.09) (2.51)
Manual/Physical 0.035
(0.86)
Routine Cognitive 0.052
(1.08)
Routine Manual -0.363***
(-3.89)
Nonroutine Manual 0.297***
(3.81)
Social Skills 0.111** 0.106** 0.205***
(2.35) (2.22) (2.99)
Nonroutine Analytical / Math -0.141*** -0.140*** 0.097
(-4.02) (-3.97) (0.65)
Routine 0.074 0.071 0.116*
(1.34) (1.26) (1.70)
Social Skills×Analytical / Math -0.027
(-0.70)
Service -0.125***
(-2.70)
Deductive / Inductive Reasoning -0.340***
(-3.72)
Number Facility -0.043
(-0.31)
Information Use -0.267**
(-2.16)
Required Social Interaction 0.059
(1.07)
Coordination / Team Building 0.119
(1.50)
Interaction / Communication 0.262***
(3.06)
Observations 649 649 649 649 649
𝑅2 0.025 0.063 0.020 0.020 0.108
Note:This table reports regressions of standardized market-implied occupation AI exposure on task and skill mea-
sures from the labor literature. Column (1) uses four Autor-Levy-Murnane (ALM) style task groups constructed
from O*NET descriptors, following Autor, Levy and Murnane (2003): routine, nonroutine analytic, nonroutine
interactive, and manual/physical. Column (2) uses an expanded Acemoglu-Autor style taxonomy that keeps the
same nonroutine analytic and nonroutine interactive measures and splits the routine and manual margins into rou-
tine cognitive, routine manual, and nonroutine manual. Columns (1) and (2) use task-content measures. Columns
(3)–(5) use the skill-based measures emphasized in Deming (2017). Column (3) uses his three headline measures:
social skills, nonroutine analytical and mathematical content, and routine tasks. Column (4) adds the interaction be-
tween standardized social skills and standardized nonroutine analytical/math, following Deming’s social-cognitive
complementarity. Column (5) uses the ten Deming-style O*NET task and skill measures. The first three have the
same definitions as in columns (3) and (4). All right-hand-side variables are standardized. The interaction is the
product of standardized components.𝑡-statistics based on HC1 robust standard errors are in parentheses. *, **, and
*** denote significance at the 10%, 5%, and 1% levels, respectively. Underlying firm-level AI betas are estimated
on the equity sample of 108 formation weeks from March 2024 through March 2026.
32

Table 10: Market-Implied Occupation Exposure and AI-Exposure Measures
(1) (2) (3)
Technical AI ESZ (core & suppl.) Combined
Felten AIOE -0.150** -0.133*
(-2.46) (-1.81)
Eloundou GPT-4 0.131** 0.068
(2.33) (0.82)
Webb AI -0.067* -0.085**
(-1.78) (-2.06)
ESZ GenAI Exposure (Core Tasks) -0.010 0.056
(-0.28) (0.77)
ESZ GenAI Exposure (Supplemental Tasks) 0.024 0.022
(0.96) (0.66)
Observations 649 602 602
𝑅2 0.012 0.001 0.013
Note:This table reports regressions of standardized market-implied occupation AI exposure on occupation-
level AI-exposure measures. Column (1) uses technical AI exposure measures from Felten, Raj and Seamans
(2021), Eloundou, Manning, Mishkin and Rock (2023), and Webb (2020). Column (2) uses the occupation-level
generative-AI task exposure of Eisfeldt, Schubert and Zhang (2023) (ESZ), from their public data repository: ex-
posure through core tasks and exposure through supplemental tasks, whose sum is the occupation’s total exposed
task share. In ESZ, exposure through core tasks proxies for labor substitution and exposure through supplemental
tasks for complementarity. Column (3) combines the technical AI and ESZ measures. ESZ scores are mapped
from 2010 SOC to 2018 SOC occupations using the Census occupation-code crosswalk, which reduces the sample
in columns (2) and (3). All right-hand-side variables are standardized.𝑡-statistics based on HC1 robust standard
errors are in parentheses. *, **, and *** denote significance at the 10%, 5%, and 1% levels, respectively. Under-
lying firm-level AI betas are estimated on the equity sample of 108 formation weeks from March 2024 through
March 2026.
the model. The reasoning share counts the model’s internal work plan tokens. A single agentic
exchange can require all three: asked “What is the temperature in Rome?”, the model produces
reasoning tokens to lay out the steps, issues a tool call to an external weather API, and reads the
recurring system prompt from cache rather than re-processing it. The tool-call and cache-read
shares are near zero in 2024 and rise to roughly two-fifths to one-half of all tokens by the end of
the sample, while the reasoning share rises far more slowly.
We then test whether exposure to these agentic-consumption components is priced in the cross-
section of equity returns—whether firms whose returns covary more with these components earn
higher average returns. For each factor we constructed above—agentic, cache-read, and reasoning
tokens, and agentic dollars—we estimate firm-level betas from rolling weekly return regressions,
sort firms into quintiles, and compute the value-weighted high-minus-low spread. Internet Ap-
pendix Table IA.12 reports these spreads, raw and as alphas from the Fama–French three-factor
33

2024-01 2024-05 2024-09 2025-01 2025-05 2025-09 2026-01 2026-05
0.0T
5.0T
10.0T
15.0T
20.0T
25.0TWeekly total tokens
Non-agentic total tokens
Agentic total tokens
Agentic token share
0%
10%
20%
30%
40%
50%
60%
Agentic share of total tokens
Latest share: 52.2%
Peak share: 59.3%
Figure 5: Agentic and Non-Agentic Token Consumption
Note:The figure plots weekly total token consumption in the OpenRouter dataset, decomposed into agentic and non-
agentic total tokens. Total tokens are defined as prompt tokens plus completion tokens. Agentic total tokens are total
tokens from requests whose normalized finish reason istool_calls; non-agentic total tokens are the remaining total
tokens. The black line plots the agentic share of total tokens. Data is weekly from January 2024 through April 2026.
model (Fama and French, 1993), the Fama–French five-factor model (Fama and French, 2015),
and the five-factor model augmented with momentum (Carhart, 1997). The point estimates are
positive for the individual agentic factors and of the same sign as the overall AI premium. They
are, however, estimated imprecisely because of the short sample. We thus take this as early and
suggestive evidence of a positive agentic premium.
34

2025-02 2025-05 2025-08 2025-11 2026-02
0.0T
2.0T
4.0T
6.0T
8.0T
10.0T
12.0T
14.0T
16.0TAgentic weekly tokens
Agentic total tokens (left)
Agentic $ per million tokens (right)
0.0
0.5
1.0
1.5
2.0
2.5
Agentic $ / million tokens
Figure 6: Agentic Token V olume and Realized Price per Token
Note:The figure plots weekly agentic total tokens (left axis; prompt plus completion tokens from requests with
normalized finish reasontool_calls) against the realized dollars per million tokens on the same agentic requests
(right axis; OpenRouter usage dollars divided by agentic total tokens, times one million). Agentic token volume rises
by orders of magnitude while the realized price per token declines, consistent with prompt caching and routing toward
cheaper models compressing revenue per token even as agentic usage expands.
35

References
Acemoglu D, Aghion P, Zilibotti F. 2006. Distance to frontier, selection, and economic growth.
Journal of the European Economic Association4: 37–74.
Acemoglu D, Autor D. 2011. Skills, tasks and technologies: Implications for employment and
earnings. In Ashenfelter O, Card D (eds.)Handbook of Labor Economics, volume 4B. Amster-
dam: Elsevier, 1043–1171.
Acemoglu D, Restrepo P. 2019a. Artificial intelligence, automation, and work. In Agrawal A, Gans
J, Goldfarb A (eds.)The Economics of Artificial Intelligence: An Agenda, chapter 8. Chicago,
IL: University of Chicago Press, 197–236.
Acemoglu D, Restrepo P. 2019b. Automation and new tasks: How technology displaces and
reinstates labor.Journal of Economic Perspectives33: 3–30.
Acemoglu D, Restrepo P. 2022. Tasks, automation, and the rise in U.S. wage inequality.Econo-
metrica90: 1973–2016.
Andrews I, Farboodi M. 2025. Do markets believe in transformative AI? Technical report, Working
paper.
Anthropic. 2026. Anthropic economic index report: Learning curves.https://www.anthropic.
com/research/economic-index-march-2026-report. Accessed June 2026.
Aubakirova M, Atallah A, Clark C, Summerville J, Midha A. 2025. State of AI: An Empirical 100
Trillion Token Study with OpenRouter. OpenRouter and a16z report, arXiv:2601.10088.
Autor DH, Levy F, Murnane RJ. 2003. The skill content of recent technological change: An
empirical exploration.Quarterly Journal of Economics118: 1279–1333.
Babina T. 2026. Understanding firms’ AI efforts and their economic impact. Technical Report
35123, National Bureau of Economic Research.
Babina T, Fedyk A, He A, Hodson J. 2024a. Artificial intelligence and firms’ systematic risk.
Technical report, Social Science Research Network.
Babina T, Fedyk A, He A, Hodson J. 2024b. Artificial intelligence, firm growth, and product
innovation.Journal of Financial Economics151: 103745.
Baslandze S, Edwards Z, Graham J, McClure T, Meyer BH, Sparks M, Waddell SR, Weitz D. 2026.
Artificial intelligence, productivity, and the workforce: Evidence from corporate executives.
Technical report, National Bureau of Economic Research.
36

Bick A, Blandin A, Deming DJ, Fuchs-Schündeln N, Jessen J. 2026. Mind the gap: AI adoption
in Europe and the US. Technical report, National Bureau of Economic Research.
Blumenfeld A, Hazell J, Lian C, Schaab A. 2026. The macroeconomic effect of AI: Sizing the
software engineering channel. Working paper, UC Berkeley and London School of Economics.
Carhart MM. 1997. On persistence in mutual fund performance.Journal of Finance52: 57–82.
Das D, Murphy M. 2026. OpenRouter Now Processes More Than a Quadrillion Tokens a Year.
Menlo Ventures.
Deming DJ. 2017. The growing importance of social skills in the labor market.Quarterly Journal
of Economics132: 1593–1640.
Demirer M, Fradkin A, Tadelis N, Peng S. 2025. The emerging market for intelligence: Pric-
ing, supply, and demand for LLMs. Technical Report 34608, National Bureau of Economic
Research.
Eisfeldt AL, Schubert G, Zhang MB. 2023. Generative AI and firm values. Technical report,
National Bureau of Economic Research.
Eloundou T, Manning S, Mishkin P, Rock D. 2023. GPTs are GPTs: An early look at the labor
market impact potential of large language models. Working paper, OpenAI. ArXiv:2303.10130.
Fama EF, French KR. 1992. The cross-section of expected stock returns.Journal of Finance47:
427–465.
Fama EF, French KR. 1993. Common risk factors in the returns on stocks and bonds.Journal of
Financial Economics33: 3–56.
Fama EF, French KR. 2015. A five-factor asset pricing model.Journal of Financial Economics
116: 1–22.
Fama EF, MacBeth JD. 1973. Risk, return, and equilibrium: Empirical tests.Journal of Political
Economy81: 607–636.
Felten EW, Raj M, Seamans R. 2021. Occupational, industry, and geographic exposure to artificial
intelligence: A novel dataset and its potential uses.Strategic Management Journal42: 2195–
2217.
Garleanu N, Kogan L, Panageas S. 2012. Displacement risk and asset returns.Journal of Financial
Economics105: 491–510.
Gomes JF, Kogan L, Yogo M. 2009. Durability of output and expected stock returns.Journal of
Political Economy117: 941–986.
37

Hassabis D, Kavukcuoglu K. 2024. Introducing gemini 2.0: Our new AI model for the agentic era.
Google Blog.
Jegadeesh N, Titman S. 1993. Returns to buying winners and selling losers: Implications for stock
market efficiency.Journal of Finance48: 65–91.
Jensen TI, Kelly B, Pedersen LH. 2023. Is there a replication crisis in finance?Journal of Finance
78: 2465–2518.
Jones CI, Tonetti C. 2026. Past automation and future A.I.: How weak links tame the growth
explosion. Working paper, Stanford GSB and NBER.
Kogan L, Papanikolaou D. 2014. Growth opportunities, technology shocks, and asset prices.Jour-
nal of Finance69: 675–718.
Kogan L, Papanikolaou D, Schmidt LD, Seegmiller B. 2023. Technology and labor displacement:
Evidence from linking patents with worker-level data. Technical report, National Bureau of
Economic Research.
Kogan L, Papanikolaou D, Seru A, Stoffman N. 2017. Technological innovation, resource alloca-
tion, and growth.Quarterly Journal of Economics132: 665–712.
Kogan L, Papanikolaou D, Stoffman N. 2020. Left behind: Creative destruction, inequality, and
the stock market.Journal of Political Economy128: 855–906.
Lindenlaub I, Oh R, Rodriguez MA, Veldkamp L. 2026. Beyond exposure: Predicting AI adop-
tion based on comparative advantage. Technical Report 35271, National Bureau of Economic
Research.
Liu H, Papanikolaou D, Schmidt LD, Seegmiller B. 2025. Technology and labor markets: Past,
present, and future. Technical Report 34386, National Bureau of Economic Research.
Lopez-Lira A, Tang Y . 2026. Can ChatGPT forecast stock price movements? return predictability
and large language models.Journal of Financial Economics184: 104335.
Ng A. 2024a. Agentic design patterns part 1: Four AI agent strategies that improve GPT-4 and
GPT-3.5 performance. The Batch, DeepLearning.AI.
Ng A. 2024b. Agentic design patterns part 3: Tool use. The Batch, DeepLearning.AI.
Papanikolaou D. 2011. Investment shocks and asset prices.Journal of Political Economy119:
639–685.
Pastor L, Veronesi P. 2009. Technological revolutions and stock prices.American Economic
Review99: 1451–1483.
38

Pichai S. 2026. Google I/O 2026: Sundar Pichai’s opening keynote.https://blog.google/
innovation-and-ai/sundar-pichai-io-2026/. Accessed June 2026.
Sarkar SK. 2026. AI agents and higher-order work. Technical report, Social Science Research
Network.
Sarkar SK, Melas-Kyriazi L. 2026. Returns to intelligence: Worker and firm adaptation to advances
in AI. Technical report, Social Science Research Network.
Tan H. 2026. Goldman Sachs Says the AI Boom Is Bigger Than Investors Think. Business Insider.
Webb M. 2020. The impact of artificial intelligence on the labor market. Working paper, Stanford
University.
Yang J, Yonack N, Zyskowski K, Yarats D, Ho J, Ma J. 2025. The adoption and usage of AI agents:
Early evidence from Perplexity. ArXiv:2512.07828.
39

Internet Appendix for “The Cross-Section of Stock Returns and
AI Exposure”
This is the Internet Appendix to Borri, Liu, and Tsyvinski, “The Cross-Section of Stock Returns
and AI Exposure.”
IA.1 AI Data
This section documents the scale and broad composition of the OpenRouter, Inc. data used
to construct the AI token consumption measures. Figure 1 shows the rapid growth in total-token
consumption on the platform and reports cumulative total-token consumption over the sample.
Cumulative tokens rise to 380.8 trillion by the end of the sample, with most of the growth concen-
trated in the second half of the period and no obvious single-event jump. Figure IA.1 decomposes
AI consumption across twelve prompt-content categories, separately for all models, closed-source
models, and open-weight models. The prompt labels are assigned by OpenRouter as discussed in
Aubakirova, Atallah, Clark, Summerville and Midha (2025). Across all models, programming and
technology together account for the majority of categorized tokens at the end of the sample (37
percent and 26 percent), followed by roleplay and science. Open-weight models tilt more toward
programming and roleplay. Closed-source models tilt more toward technology. Category coverage
begins in May 2025, when OpenRouter started populating the field.
Table IA.1 reports summary statistics for OpenRouter consumption at the account-day, ac-
count, and account-model levels, corresponding to the highest level of granularity of the data we
use. Panel A summarizes active account-days, Panel B summarizes account-level breadth and
concentration, and Panel C summarizes account-model daily consumption and volatility.
1

2025-07 2025-10 2026-01 2026-040%
20%
40%
60%
80%
100%
Share of total categorized tokens
Trivia  (0.2%)
Marketing (SEO)  (0.7%)
Marketing  (1.3%)
Health  (1.2%)
Legal  (1.8%)
Academia  (1.7%)
Translation  (1.3%)
Finance  (3.8%)
Science  (9.4%)
Technology  (26.0%)
Roleplay  (15.9%)
Programming  (36.7%)
(A) All AI Models
2025-07 2025-10 2026-01 2026-040%
20%
40%
60%
80%
100%
Share of total tokens
Trivia  (0.2%)
Marketing (SEO)  (1.3%)
Marketing  (2.1%)
Health  (1.8%)
Legal  (3.2%)
Translation  (1.7%)
Academia  (2.4%)
Finance  (4.7%)
Science  (10.4%)
Roleplay  (9.1%)
Technology  (31.5%)
Programming  (31.8%)
(B) Closed-Source Models Only
2025-07 2025-10 2026-01 2026-040%
20%
40%
60%
80%
100%
Share of total tokens
Trivia  (0.2%)
Marketing (SEO)  (0.2%)
Marketing  (0.6%)
Health  (0.7%)
Legal  (0.6%)
Translation  (1.0%)
Academia  (1.1%)
Finance  (3.0%)
Science  (8.5%)
Roleplay  (22.7%)
Technology  (21.0%)
Programming  (40.4%)
(C) Open-Source Models Only
Figure IA.1: Evolution of AI Consumption by Prompt-Content Category
Note:Each panel in the figure stacks the weekly share of total categorized tokens contributed by each of the 12 prompt-
content categories tagged in the platform’s category-token-share file. Panel A pools all AI models; Panel B restricts
the universe to closed-weight models; Panel C restricts the universe to open-weight models. Within each panel shares
sum to 100% by construction, and the right-hand legend reports the share at the final week (legend ordering matches
the stacking order). Data is weekly from mid-May 2025 (when category coverage becomes available) through April
2026.
2

Table IA.1: OpenRouter Account-Model Data Summary
Mean Std. p10 p25 p50 p75 p90
Panel A. Active account-day consumption
Requests per active account-day 109.9 434.3 1.000 4.000 16.00 49.00 153.0
Total tokens per active account-day (thous.) 1,223 4,778 2.718 14.55 79.44 392.7 1,713
User-days using at least two models (%) 31.66
User-days using at least two providers (%) 44.43
Panel B. Account-level breadth and persistence
Active days per account 16.73 35.73 1.000 1.000 3.000 13.00 47.00
Active weeks per account 5.300 8.131 1.000 1.000 2.000 5.000 15.00
Observed account span (days) 67.24 112.1 1.000 1.000 8.000 84.00 243.0
Lifetime requests 1,127 4,470 2.000 9.000 56.00 348.0 1,683
Lifetime total tokens (thous.) 15,916 64,301 2.258 22.36 288.7 2,723 22,607
Top-model token share within account (%) 79.40 24.56 40.19 59.35 93.15 100.0 100.0
Model-token HHI within account 7,324 2,945 2,791 4,830 8,712 10,000 10,000
Accounts using at least two models (%) 60.37
Accounts using at least five models (%) 29.73
Accounts using at least two providers (%) 70.00
Panel C. Account-model daily consumption and volatility
Active days per account-model pair 5.066 10.07 1.000 1.000 1.000 4.000 12.00
Observed pair span (days) 20.79 44.47 1.000 1.000 1.000 16.00 65.00
Active-day share within pair span (%) 74.38 35.73 12.50 41.18 100.0 100.0 100.0
Requests per active account-model-day 24.12 73.73 1.000 1.500 4.000 14.60 44.50
Total tokens per active account-model-day (thous.) 372.9 1,424 0.419 2.721 16.33 109.2 558.9
SD of daily total tokens (thous.) 971.0 3,385 3.401 13.28 67.03 311.4 1,614
CV of daily total tokens 1.132 0.561 0.561 0.749 1.005 1.379 1.865
Note:This table reports account-level and account-model-level summary statistics computed from the OpenRouter generations data. Non-
share row variables are winsorized at the 1st and 99th percentiles before computing the reported statistics. An active account-day has positive
recorded requests; requests are API calls; total tokens are prompt plus completion tokens. Active days and weeks count positive-use days
and calendar weeks, and observed span is first-to-last positive-use days inclusive. Top-model share and model-token HHI use each account’s
lifetime token shares across models, with HHI scaled by 10,000. For account-model pairs, active-day share is active days divided by span; SD
and CV are computed across active days, with CV equal to SD divided by the mean. V olatility rows require at least five active days. Share
rows are percent means and leave distribution columns blank.
3

IA.2 AI Factor
This appendix documents the construction of the AI factor introduced in Section 2.1 and of the
split-specific factors used in Section 3.3.2. Figure 1 of the main text plots total tokens in levels; we
begin in growth space, which is what enters the construction of the factor.
Figure IA.2 plots the weekly log growth of total tokens, usage dollars, and distinct users after
full-sample standardization. The three series move closely together but are not identical, motivat-
ing the use of their common principal component.
Table IA.2 then reports the principal-component loadings used to combine those three growth
series into the baseline AI factor of Section 2.1. The first principal component places weights of
0.665, 0.559, and 0.496 on total tokens, dollars, and users, and explains 56.5 percent of the joint
variance. The roughly equal loadings indicate that a single common factor captures the bulk of
co-movement across the three margins.
Table IA.2: PCA Loadings for Weekly Log Growth in AI Variables
Comp. 1 Comp. 2 Comp. 3
Δln𝑇𝑜𝑘0.665−0.047−0.745
Δln𝐷𝑜𝑙0.559−0.631 0.538
Δln𝑈𝑠𝑒𝑟0.496 0.774 0.394
Eigenvalue 1.695 0.858 0.447
Proportion 0.565 0.286 0.149
Cumulative 0.565 0.851 1.000
Note:The table reports the loadings of each principal component on the three underlying input seriesΔln𝑇𝑜𝑘,
Δln𝐷𝑜𝑙, andΔln𝑈𝑠𝑒𝑟, where the inputs are the log growth in total tokens, usage dollars, and distinct active users,
respectively. The table reports the weekly Monday-indexed decomposition used to construct the headline asset-pricing
factor𝐴𝐼 𝑡 (the first component of weekly inputs). TheProportionandCumulativerows give the share of the input
variance captured by each principal component. Loadings are in correlation form (eigenvectors of the input correla-
tion matrix, with the sum of squared loadings within each component equal to 1). Data is weekly from January 2024
through April 2026.
We next turn to the four user- and model-side splits that underlie the split-specific factors used
in Table 6 of Section 3.3.2. Figure IA.3 plots each as a weekly token-share time series: the closed-
source share, the paid/core account share, the seasoned-user share, and the long-prompt share. The
four series are distinct and not collinear—the closed-source share fluctuates with frontier-model
4






7RWDOWRNHQV





8VDJHGROODUV
   





'LVWLQFWXVHUV
Figure IA.2: Standardized Weekly Natural-Log Growth of the Three AI-Factor Input Series
Note:The figure plots the full-sample-standardized weekly natural-log growth of the three input components used to
construct the headline AI factor: total tokens, usage dollars, and distinct users. The corresponding weekly levels are
plotted in main-paper Figure 1. Data is weekly from January 2024 through April 2026.
5

2024-01 2024-07 2025-01 2025-07 2026-010.00
0.25
0.50
0.75
1.00Token share
(A) Closed-Source Token Share
2024-01 2024-07 2025-01 2025-07 2026-010.00
0.25
0.50
0.75
1.00Token share (B) Paid/Core Token Share
2024-01 2024-07 2025-01 2025-07 2026-010.00
0.25
0.50
0.75
1.00
Token share
(C) Seasoned-User Token Share
2024-07 2025-01 2025-07 2026-010.00
0.25
0.50
0.75
1.00Token share (D) Long-Prompt (Top 25%) Token Share
Figure IA.3: Evolution of the AI Consumption Decompositions Used in Table 6
Note:Each panel plots, for one of the four splits used in Table 6, the weekly share of total tokens attributable to the
focal leg of that split: Panel A, closed-source AI models (Table 6 Panel A); Panel B, paid/core accounts under the
acct_paiddefinition (Table 6 Panel B); Panel C, seasoned users (Table 6 Panel C); Panel D, the long-prompt seg-
ment defined as rows whose prompt-token count exceeds the prior-13-week rolling 75th percentile (Table 6 Panel D).
Hatched regions and dashed vertical lines in Panels B and C mark burn-in periods for the user classifications.
release cycles, the paid/core and seasoned-user shares evolve more smoothly, and the long-prompt
share is the most volatile—so each generates a different split-specific AI factor in the main analysis.
IA.3 AI Portfolios
This section collects portfolio evidence and robustness tests that complement the main-text
sorts. We organize the discussion around four questions about the headline AI-premium result:
whether it depends on how the AI factor is built, whether it survives standard risk adjustment
and small-sample inference, whether it merely relabels broad technology, attention, or disclosure
exposures, and how it varies across geography and the rise of agentic AI consumption.
We start with the factor construction. Table IA.3 repeats the value-weighted, all-stock-breakpoint
quintile sort using each of the three input series (Δln𝑇𝑜𝑘,Δln𝐷𝑜𝑙,Δln𝑈𝑠𝑒𝑟) in place of the
6

principal-component AI factor. The high-minus-low spreads are 49.4, 35.5, and 39.5 basis points
per week, so the headline result is not driven by a single input.
Table IA.3: AI-Factor Input-Component Quintile Portfolios
Low 2 3 4 High H−L
Panel A. Sorted on𝛽𝑇𝑜𝑘
Excess return -0.111 0.207 0.245 0.081 0.383 0.494
𝑡(-0.46) (1.00) (1.27) (0.40) (1.35) (2.31)
FF5𝛼-0.243 0.005 0.039 -0.098 0.143 0.386
𝑡(𝛼)(-1.94) (0.07) (0.57) (-1.21) (1.07) (1.84)
FF5+Mom𝛼-0.207 0.021 0.030 -0.103 0.128 0.335
𝑡(𝛼)(-1.73) (0.28) (0.44) (-1.26) (0.96) (1.64)
Panel B. Sorted on𝛽𝐷𝑜𝑙
Excess return 0.040 0.129 0.199 0.243 0.395 0.355
𝑡(0.17) (0.61) (1.06) (1.14) (1.40) (1.46)
FF5𝛼-0.092 -0.028 0.008 0.031 0.172 0.264
𝑡(𝛼)(-0.69) (-0.38) (0.12) (0.34) (1.22) (1.12)
FF5+Mom𝛼-0.104 -0.018 0.016 0.027 0.163 0.267
𝑡(𝛼)(-0.77) (-0.25) (0.22) (0.30) (1.15) (1.13)
Panel C. Sorted on𝛽𝑈𝑠𝑒𝑟
Excess return -0.002 0.294 0.062 0.194 0.393 0.395
𝑡(-0.01) (1.34) (0.33) (0.99) (1.36) (2.02)
FF5𝛼-0.177 0.079 -0.121 0.020 0.200 0.377
𝑡(𝛼)(-1.45) (1.00) (-1.75) (0.23) (1.43) (1.88)
FF5+Mom𝛼-0.161 0.076 -0.101 0.023 0.183 0.344
𝑡(𝛼)(-1.32) (0.96) (-1.53) (0.26) (1.31) (1.73)
Note:The table decomposes the AI-factor result of Table 3 into its three input components. The AI factor is the first
principal component of weekly log growth in total tokens, usage dollars, and distinct users. Here we replace the AI
factor with each component individually: for𝑋∈{𝑇𝑜𝑘,𝐷𝑜𝑙,𝑈𝑠𝑒𝑟}, we estimate𝑟 𝑒 𝑖,𝑡 =𝑎+𝑏 mkt𝑟𝑒 𝑚,𝑡+𝛽𝑋 𝑖,𝑡Δln𝑋 𝑡 on a
13-week rolling window, then sort stocks into pooled quintiles by the estimated𝛽𝑋 𝑖,𝑡 . Returns and alphas are in percent
per week, value-weighted by formation-week market capitalization, with all-stock breakpoints; FF5 and FF5+Mom
denote alphas from Fama and French (2015) and from that model augmented with Carhart (1997) momentum. AI
consumption data is weekly from January 2024 through April 2026. The equity sample covers 108 formation weeks
from March 2024 through March 2026.
Turning from factor construction to risk adjustment, Table IA.4 reports the time-series regres-
sion of the value-weighted, all-stock-breakpoint AI-beta long-short return on the FF3, FF5, and
FF5-plus-momentum models. The intercept is 54.0, 54.5, and 52.6 basis points per week respec-
tively, all significant at the 5 percent level, and none of the factor loadings is large. The H−L spread
7

is not absorbed by size, value, profitability, investment, or momentum.
Table IA.4: Fama-French Factor Regressions for the AI-Beta H−L Portfolio
FF3 FF5 FF5+Mom
𝛼0.540 0.545 0.526
𝑡(𝛼)(2.55) (2.53) (2.44)
Mkt-RF 0.194 0.219 0.197
𝑡(1.82) (1.95) (1.72)
SMB 0.070 0.128 0.165
𝑡(0.45) (0.72) (0.91)
HML 0.219 0.205 0.194
𝑡(1.44) (1.21) (1.14)
RMW 0.137 0.153
𝑡(0.64) (0.71)
CMA -0.085 -0.047
𝑡(-0.41) (-0.22)
Mom 0.123
𝑡(0.99)
𝑅2 0.058 0.063 0.072
Note:The dependent variable is the value-weighted all-stock-breakpoint H−L return from Table 3. Returns and factors
are in percent per week. FF3 is the Fama–French three-factor model (Fama and French, 1993). FF5 adds RMW and
CMA (Fama and French, 2015). FF5+Mom additionally includes the momentum factor (Carhart, 1997). The table
reports OLS coefficient estimates,𝑡-statistics in parentheses and𝑅 2. AI consumption data is weekly from January
2024 through April 2026. The equity sample covers 108 formation weeks from March 2024 through March 2026.
Beyond the headline portfolio sorts, Table IA.5 looks directly at incumbent application-layer
firms. It reports value-weighted SaaS-portfolio regressions on the baseline AI factor and the mar-
ket. Over the full sample the SaaS-portfolio loading on𝐴𝐼 𝑡 is 0.183, which is statistically insignif-
icant, and restricted to the last calendar quarter the loading is 0.956 per one-standard-deviation AI
shock, significant at the 1 percent level.
We next address two inference-related concerns about the headline test. Table IA.6, Panel A,
reports a circular moving-block bootstrap that resamples consecutive holding-week observations:
the[2.5,97.5]-percentile interval for the H−L excess return is[24.1,96.6]basis points per week,
with similar coverage for the FF5 and FF5+Mom alphas, so the interval excludes zero in all three
cases. Panel B replaces the raw rolling AI beta with an empirical-Bayes-shrunk beta toward the
cross-sectional mean. The value-weighted, all-stock-breakpoint H−L spread is 46.2 basis points
per week, significant at the 5 percent level, so the result is not an artifact of estimation noise in the
8

Table IA.5: SaaS Exposure to the AI Factor: Full Sample Versus Last Quarter
Full sample Last quarter
Value-weighted SaaS portfolio regression
𝐴𝐼𝑡 0.183 0.956
𝑡(0.83) (3.10)
Mkt-RF 1.152 0.867
𝑡(15.64) (1.52)
𝑅2 0.565 0.154
Avg. firms/week 141.9 143.2
Note:The table reports value-weighted portfolio regressions for public SaaS firms. The SaaS universe is the SaaSDB
public-company list matched by ticker to the CRSP/firm-exposure sample. The dependent variable is the value-
weighted SaaS portfolio excess log return, and the regressors are the baseline AI factor𝐴𝐼 𝑡 and the weekly mar-
ket excess return Mkt-RF. Standard errors use Newey-West five-week lags. The coefficient on𝐴𝐼 𝑡 is multiplied by
100×𝜎𝑤(𝐴𝐼), so the row reports the weekly return effect in percentage points for a one-standard-deviation increase
in the baseline AI factor. AI consumption data is weekly from January 2024 through April 2026. Equity betas use
13-week rolling windows, so portfolio formation weeks begin in March 2024.
firm-level betas.
Table IA.6: Small-Sample Robustness of AI-Beta Portfolio
Panel A. Baseline H−L: Block-Bootstrap Inference
Estimate 2.5% 97.5%𝑡
Excess return 0.604 0.241 0.966 (2.85)
FF5𝛼0.545 0.158 0.923 (2.53)
FF5+Mom𝛼0.526 0.131 0.923 (2.44)
Panel B. H−L Sorts on Shrunk AI Beta
VW All VW NYSE EW All EW NYSE
Excess return 0.462 0.420 0.256 0.246
𝑡(2.48) (2.32) (1.65) (1.57)
FF5𝛼0.411 0.368 0.170 0.163
𝑡(𝛼)(2.18) (2.02) (1.13) (1.07)
FF5+Mom𝛼0.379 0.339 0.128 0.121
𝑡(𝛼)(2.03) (1.87) (0.89) (0.82)
Note:The table examines the robustness of the baseline H−L portfolio in Table 3. Panel A reports percentile confi-
dence intervals from a circular moving-block bootstrap that resamples consecutive holding-week observations. Panel
B repeats the quintile sort after replacing the raw rolling AI beta with an empirical-Bayes-shrunk beta. The shrink-
age target is the formation-week cross-sectional mean beta, and the reliability weight uses the rolling-beta standard
error and the formation-week cross-sectional signal variance. Returns and alphas are in percent per week; FF5 and
FF5+Mom denote alphas from Fama and French (2015) and from that model augmented with Carhart (1997) momen-
tum. Breakpoint and weighting definitions match Table 3. AI consumption data is weekly from January 2024 through
April 2026. The equity sample covers 108 formation weeks from March 2024 through March 2026.
9

We then ask whether the AI premium is simply a relabeling of broader cross-sectional patterns.
Industry tilts are the first candidate. Table IA.7 replaces the AI beta with its deviation from the
within-period Fama-French 30 industry median and re-runs the quintile sort. The value-weighted,
all-stock-breakpoint H−L spread is 54.1 basis points per week, significant at the 1 percent level,
close to the 60.4-basis-point baseline, so the AI premium is a within-industry phenomenon and not
a relabeling of broad industry tilts.
Broad public attention to AI is the second candidate. Table IA.8 re-estimates each firm’s AI
beta after adding the weekly log growth of Google Trends search interest in “Artificial intelligence”
to the first-stage market regression, and sorts on the residual AI beta. The value-weighted, all-
stock-breakpoint H−L spread is 69.1 basis points per week, significant at the 1 percent level, with
comparable factor-model alphas, so the premium is not a relabeling of broad public attention to
AI.
A third candidate is firms’ own AI narratives. Table IA.9 regresses the baseline AI-beta H−L
return on a control H−L portfolio built from firms’ AI mentions in 10-K, 10-Q, and 8-K filings,
using unscaled AI-mention counts in Panel A and word-scaled counts in Panel B. The spanning
intercept ranges from 52.5 to 62.1 basis points per week, comparable to the unconditional H−L re-
turn, and the SEC-mention loading is small and statistically insignificant in all rows. The realized-
consumption signal is distinct from firms’ own AI narratives in their disclosures.
Stepping back to factor construction, Table IA.10 replaces the principal-component AI fac-
tor with an alternative aggregator: the simple equal-weighted average of the three full-sample-
standardized input series. The value-weighted, all-stock-breakpoint H−L spread is 58.5 basis
points per week, significant at the 1 percent level, and the FF5 and FF5+Mom alphas are 52.3
and 50.6 basis points respectively. The headline result is not specific to the principal-component
construction.
We also split AI consumption into agentic and non-agentic components and sort on exposure
to each separately. Table IA.11 builds two alternative factors from token growth split this way:
agentic tokens come from requests with normalized finish reasontool_calls, in which the model
invoked an external tool, and non-agentic tokens are the remainder. Sorting on exposure to non-
agentic token growth yields an H−L spread of 46.1 basis points per week, significant at the 5
percent level. Sorting on exposure to agentic token growth yields a smaller spread of 2.4 basis
points, which is statistically insignificant. Agentic use is a fast-growing but still small share of
total consumption in this sample, and the priced AI signal loads on broader, non-agentic activity.
10

Table IA.7: Industry-Demeaned AI-Beta Quintile Portfolios
Low 2 3 4 High H−L
Panel A. Value-weighted, all-stock breakpoints
Excess return -0.106 0.145 0.169 0.264 0.434 0.541
𝑡(-0.42) (0.75) (0.86) (1.21) (1.61) (2.87)
FF5𝛼-0.299 -0.014 -0.020 0.072 0.223 0.521
𝑡(𝛼)(-2.41) (-0.20) (-0.27) (0.84) (2.02) (2.69)
FF5+Mom𝛼-0.280 -0.011 -0.012 0.064 0.214 0.495
𝑡(𝛼)(-2.27) (-0.15) (-0.16) (0.74) (1.94) (2.56)
Panel B. Value-weighted, NYSE breakpoints
Excess return -0.098 0.146 0.182 0.280 0.436 0.534
𝑡(-0.41) (0.76) (0.90) (1.35) (1.65) (3.08)
FF5𝛼-0.269 -0.016 -0.018 0.095 0.225 0.494
𝑡(𝛼)(-2.52) (-0.21) (-0.23) (1.16) (2.12) (2.79)
FF5+Mom𝛼-0.252 -0.011 -0.009 0.090 0.215 0.468
𝑡(𝛼)(-2.38) (-0.14) (-0.12) (1.09) (2.02) (2.65)
Panel C. Equal-weighted, all-stock breakpoints
Excess return -0.082 0.127 0.153 0.164 0.134 0.215
𝑡(-0.29) (0.59) (0.75) (0.72) (0.48) (1.61)
FF5𝛼-0.215 -0.016 0.002 -0.020 -0.047 0.168
𝑡(𝛼)(-2.33) (-0.37) (0.07) (-0.44) (-0.55) (1.22)
FF5+Mom𝛼-0.190 -0.004 0.008 -0.016 -0.052 0.138
𝑡(𝛼)(-2.14) (-0.10) (0.23) (-0.35) (-0.60) (1.03)
Panel D. Equal-weighted, NYSE breakpoints
Excess return -0.068 0.156 0.170 0.135 0.155 0.223
𝑡(-0.25) (0.74) (0.82) (0.60) (0.57) (1.83)
FF5𝛼-0.202 0.015 0.013 -0.044 -0.024 0.178
𝑡(𝛼)(-2.43) (0.35) (0.36) (-0.95) (-0.31) (1.43)
FF5+Mom𝛼-0.177 0.026 0.017 -0.038 -0.028 0.150
𝑡(𝛼)(-2.25) (0.64) (0.47) (-0.82) (-0.35) (1.23)
Note:The table repeats the headline test of Table 3 after demeaning the sorting variable by FF30 industry. For each
formation week𝑡and FF30 industry𝑗we compute the cross-sectional median AI beta e𝛽𝐴𝐼,(𝑗) 𝑡 =median𝑖∈𝑗(𝛽𝐴𝐼 𝑖,𝑡)across
all firms in industry𝑗that week, requiring at least five eligible firms per industry-week. The industry-demeaned beta is
𝛽𝐴𝐼,𝐼𝑛𝑑 𝑖,𝑡 =𝛽 𝐴𝐼 𝑖,𝑡− e𝛽𝐴𝐼,(𝑗(𝑖)) 𝑡 , and stocks are sorted into quintiles on this within-industry deviation. Industry assignment
follows the Kenneth French convention: the SIC code from the most recent Compustat fiscal year ending in calendar
year𝑡−1(CRSP June-of-𝑡SICCD as fallback) is mapped to one of the 30 Fama-French industries via French’s
Siccodes30. Returns and alphas are in percent per week; FF5 and FF5+Mom denote alphas from Fama and French
(2015) and from that model augmented with Carhart (1997) momentum. AI consumption data is weekly from January
2024 through April 2026. The equity sample covers 108 formation weeks from March 2024 through March 2026.
11

Table IA.8: Google-Trends-Controlled AI-Beta Quintile Portfolios
Low 2 3 4 High H−L
Panel A. Value-weighted, all-stock breakpoints
Excess return -0.118 0.104 0.164 0.393 0.573 0.691
𝑡(-0.47) (0.49) (0.82) (1.84) (2.09) (3.34)
FF5𝛼-0.324 -0.085 -0.050 0.172 0.309 0.633
𝑡(𝛼)(-2.57) (-0.92) (-0.69) (1.93) (2.38) (3.01)
FF5+Mom𝛼-0.312 -0.070 -0.051 0.165 0.293 0.605
𝑡(𝛼)(-2.50) (-0.79) (-0.70) (1.87) (2.31) (2.97)
Panel B. Value-weighted, NYSE breakpoints
Excess return -0.043 0.140 0.147 0.420 0.602 0.644
𝑡(-0.18) (0.65) (0.73) (2.06) (2.16) (3.15)
FF5𝛼-0.224 -0.068 -0.060 0.187 0.353 0.577
𝑡(𝛼)(-1.96) (-0.76) (-0.71) (2.33) (2.78) (2.82)
FF5+Mom𝛼-0.206 -0.063 -0.061 0.182 0.338 0.544
𝑡(𝛼)(-1.89) (-0.71) (-0.72) (2.27) (2.72) (2.79)
Panel C. Equal-weighted, all-stock breakpoints
Excess return -0.111 0.140 0.168 0.216 0.219 0.331
𝑡(-0.38) (0.62) (0.84) (0.94) (0.77) (2.07)
FF5𝛼-0.240 -0.015 0.018 0.043 0.032 0.272
𝑡(𝛼)(-2.30) (-0.30) (0.49) (0.77) (0.34) (1.72)
FF5+Mom𝛼-0.225 -0.006 0.020 0.041 0.025 0.249
𝑡(𝛼)(-2.24) (-0.12) (0.55) (0.73) (0.26) (1.64)
Panel D. Equal-weighted, NYSE breakpoints
Excess return -0.062 0.131 0.199 0.211 0.218 0.280
𝑡(-0.22) (0.61) (0.98) (0.94) (0.77) (1.95)
FF5𝛼-0.193 -0.023 0.050 0.041 0.034 0.226
𝑡(𝛼)(-2.18) (-0.50) (1.28) (0.75) (0.38) (1.59)
FF5+Mom𝛼-0.179 -0.016 0.051 0.040 0.026 0.205
𝑡(𝛼)(-2.12) (-0.35) (1.30) (0.74) (0.30) (1.50)
Note:The table extends the analysis of the properties of the AI-Beta quintile portfolios presented in Table 3 after
expanding the first-pass rolling beta regression to include the weekly log growth in Google Trends search interest for
the topicArtificial intelligenceas an additional control:𝑟 𝑒 𝑖,𝑡 =𝑎+𝑏 mkt𝑟𝑒 𝑚,𝑡+𝑏 gtrendΔlngtrend AI 𝑡 +𝑏 AI𝐴𝐼𝑡. Stocks are
sorted into pooled quintiles by the Google-Trends-controlled𝑏 AI. Returns and alphas are in percent per week; FF5
and FF5+Mom denote alphas from Fama and French (2015) and from that model augmented with Carhart (1997)
momentum. The Google Trends weekly index covers 2023-10 to 2026-02 and is fetched via the Knowledge-Graph
topic API. AI consumption data is weekly from January 2024 through April 2026. The equity sample covers 108
formation weeks from March 2024 through March 2026.
12

Table IA.9: Spanning Regressions with SEC-Based AI Mentions
Model𝛼 𝑡(𝛼)𝑏 Mention 𝑡(𝑏 Mention)𝑅 2
Panel A. Controlling for unscaled SEC-based AI mentions
(1) Mean 0.604 (2.85)
(2) SEC-Based AI Mention 0.621 (2.91) -0.074 (-0.73) 0.005
(3) FF5 0.545 (2.53) 0.062
(4) FF5 + SEC-Based AI Mention 0.552 (2.52) -0.037 (-0.20) 0.063
(5) FF5 + Mom 0.526 (2.44) 0.071
(6) FF5 + Mom + SEC-Based AI Mention 0.541 (2.46) -0.083 (-0.43) 0.073
Panel B. Controlling for word-scaled SEC-based AI mentions
(1) Mean 0.604 (2.85)
(2) SEC-Based AI Mention 0.607 (2.85) -0.053 (-0.46) 0.002
(3) FF5 0.545 (2.53) 0.062
(4) FF5 + SEC-Based AI Mention 0.544 (2.52) 0.039 (0.17) 0.063
(5) FF5 + Mom 0.526 (2.44) 0.071
(6) FF5 + Mom + SEC-Based AI Mention 0.525 (2.42) -0.031 (-0.13) 0.072
Note:The table reports time-series spanning regressions of the baseline AI-beta H−L portfolio return on SEC-based
AI-mention H−L portfolios. The dependent variable is the value-weighted H−L return from sorting stocks on the
baseline rolling AI beta used in Table 3, using all-stock breakpoints. The SEC-based AI-mention controls are con-
structed from the completed SEC filing text archive. We map firms to SEC CIKs using the latest non-missing CIK
from Compustat quarterly data and use 10-K, 10-Q, and 8-K filing text. AI mentions are exact matches toartificial
intelligence,generative AI,machine learning,deep learning,large language model,large language models,LLM,
OpenAI, andAI model. For firm𝑖in formation week𝑡, let𝐻 𝑖,𝑡 be the number of AI phrase mentions over weeks𝑡−13
through𝑡−1, let𝐹 𝑖,𝑡 be the number of filings over the same lagged window, and let𝑊𝑖,𝑡 be the total number of words
in those filings. Panel A sorts on the unscaled measureln(1+𝐻 𝑖,𝑡)−ln(1+𝐹 𝑖,𝑡). Panel B sorts on the word-scaled
measure10,000×𝐻 𝑖,𝑡/𝑊𝑖,𝑡 . In both panels, the SEC-based AI-mention H−L control buys the high-mention quintile
and shorts the low-mention quintile among firms with at least one filing in the lagged window. The reported regression
is𝑅 𝐴𝐼,𝐻−𝐿 𝑡 =𝛼+𝑏 Mention𝑅𝑆𝐸𝐶𝑀𝑒𝑛𝑡𝑖𝑜𝑛,𝐻−𝐿 𝑡 +𝛿′𝑋𝑡+𝜖𝑡, where𝑋 𝑡 is empty in row (2), contains the Fama-French five
factors (Fama and French, 2015) in row (4), and contains the five factors plus Carhart (1997) momentum in row (6).
Returns and factors are in percent per week. AI consumption data is weekly from January 2024 through April 2026.
The equity sample covers 108 formation weeks from March 2024 through March 2026.
13

Table IA.10: Average-Standardized Usage-Growth Quintile Portfolios
Low 2 3 4 High H−L
Panel A. Value-weighted, all-stock breakpoints
Excess return -0.141 0.163 0.166 0.311 0.444 0.585
𝑡(-0.58) (0.79) (0.84) (1.48) (1.64) (2.70)
FF5𝛼-0.293 -0.001 -0.028 0.109 0.229 0.523
𝑡(𝛼)(-2.22) (-0.01) (-0.40) (1.38) (1.74) (2.38)
FF5+Mom𝛼-0.284 0.015 -0.029 0.103 0.222 0.506
𝑡(𝛼)(-2.13) (0.19) (-0.40) (1.29) (1.68) (2.29)
Panel B. Value-weighted, NYSE breakpoints
Excess return -0.032 0.089 0.228 0.267 0.466 0.498
𝑡(-0.14) (0.43) (1.16) (1.26) (1.78) (2.49)
FF5𝛼-0.188 -0.079 0.042 0.053 0.252 0.440
𝑡(𝛼)(-1.56) (-0.93) (0.56) (0.65) (2.02) (2.16)
FF5+Mom𝛼-0.171 -0.072 0.043 0.045 0.248 0.419
𝑡(𝛼)(-1.42) (-0.84) (0.56) (0.55) (1.97) (2.06)
Panel C. Equal-weighted, all-stock breakpoints
Excess return -0.108 0.095 0.171 0.162 0.179 0.286
𝑡(-0.37) (0.44) (0.88) (0.72) (0.64) (1.84)
FF5𝛼-0.227 -0.049 0.024 -0.021 -0.008 0.219
𝑡(𝛼)(-2.22) (-0.94) (0.64) (-0.41) (-0.08) (1.41)
FF5+Mom𝛼-0.205 -0.029 0.027 -0.020 -0.017 0.187
𝑡(𝛼)(-2.05) (-0.61) (0.73) (-0.39) (-0.19) (1.23)
Panel D. Equal-weighted, NYSE breakpoints
Excess return -0.057 0.096 0.166 0.173 0.179 0.236
𝑡(-0.20) (0.46) (0.84) (0.78) (0.65) (1.65)
FF5𝛼-0.180 -0.047 0.016 -0.004 -0.008 0.172
𝑡(𝛼)(-1.95) (-0.99) (0.42) (-0.07) (-0.09) (1.20)
FF5+Mom𝛼-0.156 -0.031 0.018 -0.002 -0.016 0.140
𝑡(𝛼)(-1.76) (-0.69) (0.47) (-0.04) (-0.18) (1.00)
Note:The table presents robustness evidence on the properties of the AI-Beta quintile portfolios of Table 3 after
replacing the AI factor with a simple equal-weighted average of the three full-sample-standardized input series:
Δeln𝑋𝑡 =1/3  𝑧(Δln𝑇𝑜𝑘 𝑡)+𝑧(Δln𝐷𝑜𝑙 𝑡)+𝑧(Δln𝑈𝑠𝑒𝑟 𝑡)  , where𝑧(·)denotes full-sample standardization (subtract
sample mean, divide by sample standard deviation). This construction partly addresses the forward-looking concern
that principal-component weights are estimated from the full sample, although it does not eliminate full-sample in-
formation because the input series are still standardized using their full-sample means and standard deviations. The
first-pass rolling regression is𝑟 𝑒 𝑖,𝑡 =𝑎+𝑏 mkt𝑟𝑒 𝑚,𝑡+𝑏 avgΔeln𝑋𝑡 on a 13-week rolling window. Stocks are sorted into
quintiles by𝑏 avg. The investment universe, weighting, and breakpoint definitions match Table 3. Returns and alphas
are in percent per week. AI consumption data is weekly from January 2024 through April 2026. The equity sample
covers 108 formation weeks from March 2024 through March 2026.
14

Table IA.11: Agentic and Non-Agentic Token-Growth Quintile Portfolios
Low 2 3 4 High H−L
Value-weighted, all-stock breakpoints
𝛽𝑇𝑜𝑘,𝐴𝑔𝑒𝑛𝑡𝑖𝑐
Excess return 0.275 0.166 0.120 0.000 0.299 0.024
𝑡(0.81) (0.62) (0.41) (0.00) (0.62) (0.06)
FF5𝛼-0.056 -0.065 -0.102 -0.269 0.006 0.061
𝑡(𝛼)(-0.31) (-0.58) (-0.93) (-2.57) (0.03) (0.22)
FF5+Mom𝛼0.003 -0.078 -0.097 -0.291 -0.021 -0.024
𝑡(𝛼)(0.01) (-0.68) (-0.87) (-2.75) (-0.12) (-0.09)
𝛽𝑇𝑜𝑘,𝑁𝑜𝑛𝑎𝑔𝑒𝑛𝑡𝑖𝑐
Excess return -0.118 0.272 0.154 0.163 0.343 0.461
𝑡(-0.48) (1.30) (0.80) (0.79) (1.25) (2.22)
FF5𝛼-0.251 0.081 -0.061 -0.027 0.110 0.361
𝑡(𝛼)(-2.05) (0.99) (-0.88) (-0.32) (0.88) (1.77)
FF5+Mom𝛼-0.221 0.102 -0.065 -0.031 0.093 0.313
𝑡(𝛼)(-1.86) (1.29) (-0.93) (-0.37) (0.75) (1.57)
Note:The table repeats the value-weighted, all-stock-breakpoint portfolio test of Table 3 after replacing the baseline AI
factor with weekly log growth in agentic or non-agentic total tokens. Total tokens are prompt tokens plus completion
tokens. Agentic total tokens are total tokens from requests whose normalized finish reason istool_calls; non-
agentic total tokens are the remaining total tokens. Firm betas are estimated from a 13-week rolling regression of
weekly log-excess returns on the log-excess market return and the token-growth factor. Stocks are sorted into quintiles
by this beta. Returns and alphas are in percent per week; FF5 and FF5+Mom denote alphas from Fama and French
(2015) and from that model augmented with Carhart (1997) momentum. Data is weekly from January 2024 through
April 2026.
15

Table IA.12 extends the agentic portfolio evidence to the agentic-token, cache-read-token,
reasoning-token, and agentic-dollar factors described in Table IA.18.
Table IA.12: Cross-Sectional Pricing of Agentic Factors with Fama–French (Fama and French,
1993, 2015) and Momentum (Carhart, 1997) Adjustments
Raw FF3 FF5 FF5+Mom
Factor𝛼 𝑡 𝛼 𝑡 𝛼 𝑡 𝛼 𝑡
Agentic tokens 0.024 (0.06) 0.072 (0.23) 0.061 (0.22) -0.024 (-0.09)
Cache-read tokens 0.283 (0.75) 0.155 (0.39) 0.340 (0.80) 0.079 (0.23)
Reasoning tokens 0.301 (1.35) 0.275 (1.21) 0.270 (1.15) 0.251 (1.11)
Agentic dollars 0.095 (0.27) 0.113 (0.43) 0.078 (0.30) 0.100 (0.37)
Note:The table reports value-weighted high-minus-low quintile spreads, in percent per week, for salient components
of agentic AI token consumption factors; for details see Table IA.18 in the Internet Appendix. Firm betas are esti-
mated from a 13-week rolling regression of weekly log-excess returns on the log-excess market return and the factor;
stocks are sorted into quintiles by this beta. Columns report the raw spread and alphas from the Fama–French three-
factor model (FF3), the Fama–French five-factor model (FF5), and the five-factor model augmented with momentum
(FF5+Mom), all value-weighted under all-stock breakpoints.𝑡-statistics in parentheses.
Returning to the headline sort, Table IA.13 replaces the quintile portfolios with deciles. The
value-weighted, all-stock-breakpoint H−L spread widens to 69.4 basis points per week, significant
at the 5 percent level, and the FF5+Mom alpha is 53.8 basis points, significant at the 10 percent
level. The relationship between AI exposure and future returns is approximately monotonic and
strengthens at the extreme tails.
16

Table IA.13: AI-Beta Decile Portfolios
Low 2 3 4 5 6 7 8 9 High H−L
Panel A. Value-weighted, all-stock breakpoints
Excess return -0.028 -0.172 0.295 0.020 0.223 0.128 0.229 0.342 0.271 0.666 0.694
𝑡(-0.09) (-0.74) (1.43) (0.09) (1.10) (0.59) (1.03) (1.54) (1.07) (1.97) (2.37)
FF5𝛼-0.183 -0.335 0.130 -0.132 0.060 -0.099 0.034 0.119 0.057 0.422 0.605
𝑡(𝛼)(-0.88) (-2.32) (1.18) (-1.14) (0.58) (-1.03) (0.32) (1.13) (0.42) (2.17) (2.03)
FF5+Mom𝛼-0.157 -0.323 0.161 -0.133 0.066 -0.102 0.026 0.113 0.069 0.381 0.538
𝑡(𝛼)(-0.75) (-2.23) (1.54) (-1.14) (0.63) (-1.06) (0.24) (1.06) (0.50) (2.00) (1.85)
Panel B. Value-weighted, NYSE breakpoints
Excess return -0.107 0.059 0.068 0.129 0.305 0.163 0.235 0.319 0.260 0.576 0.682
𝑡(-0.40) (0.26) (0.31) (0.59) (1.57) (0.75) (1.12) (1.33) (1.09) (1.75) (2.58)
FF5𝛼-0.239 -0.109 -0.096 -0.019 0.125 -0.057 0.016 0.109 0.074 0.332 0.571
𝑡(𝛼)(-1.47) (-0.79) (-0.85) (-0.16) (1.23) (-0.58) (0.17) (0.87) (0.56) (1.79) (2.16)
FF5+Mom𝛼-0.222 -0.078 -0.088 -0.010 0.127 -0.059 0.013 0.091 0.088 0.302 0.524
𝑡(𝛼)(-1.36) (-0.58) (-0.78) (-0.09) (1.24) (-0.59) (0.13) (0.73) (0.66) (1.64) (2.00)
Panel C. Equal-weighted, all-stock breakpoints
Excess return -0.210 -0.017 0.072 0.123 0.151 0.195 0.154 0.171 0.167 0.192 0.402
𝑡(-0.62) (-0.07) (0.32) (0.58) (0.76) (1.00) (0.73) (0.72) (0.64) (0.62) (1.93)
FF5𝛼-0.309 -0.154 -0.072 -0.029 0.016 0.047 -0.022 -0.020 -0.021 0.000 0.309
𝑡(𝛼)(-2.10) (-1.99) (-1.12) (-0.54) (0.32) (1.09) (-0.37) (-0.34) (-0.29) (0.00) (1.49)
FF5+Mom𝛼-0.286 -0.129 -0.049 -0.015 0.027 0.048 -0.025 -0.020 -0.021 -0.017 0.269
𝑡(𝛼)(-1.96) (-1.78) (-0.84) (-0.29) (0.55) (1.09) (-0.44) (-0.33) (-0.29) (-0.13) (1.32)
Panel D. Equal-weighted, NYSE breakpoints
Excess return -0.158 0.048 0.122 0.125 0.156 0.191 0.178 0.162 0.166 0.183 0.341
𝑡(-0.51) (0.20) (0.55) (0.62) (0.78) (0.95) (0.85) (0.68) (0.66) (0.61) (1.93)
FF5𝛼-0.272 -0.088 -0.024 -0.023 0.013 0.043 0.016 -0.026 -0.031 -0.000 0.272
𝑡(𝛼)(-2.32) (-1.16) (-0.42) (-0.48) (0.29) (0.87) (0.27) (-0.43) (-0.46) (-0.00) (1.52)
FF5+Mom𝛼-0.251 -0.061 -0.007 -0.008 0.019 0.041 0.013 -0.022 -0.032 -0.014 0.236
𝑡(𝛼)(-2.17) (-0.87) (-0.12) (-0.17) (0.41) (0.83) (0.22) (-0.36) (-0.48) (-0.12) (1.34)
Note:The table repeats Table 3 with decile, rather than quintile, sorts on 13-week rolling AI beta. Universe, weighting, and breakpoints match
Table 3. Returns and alphas are in percent per week; FF5 and FF5+Mom denote alphas from Fama and French (2015) and that model augmented
with Carhart (1997) momentum. H−L buys High and shorts Low. AI consumption data is weekly from January 2024 through April 2026. The
equity sample covers 108 formation weeks from March 2024 through March 2026.
17

A final candidate relabeling is exposure to traded technology baskets. Table IA.14 reports
spanning regressions of the AI-beta H−L portfolio return on three benchmarks: the Fama-French
10 HiTec industry return (Panel A), the value-weighted NAICS semiconductor portfolio (Panel B),
and an equal-weighted AI/robotics ETF basket (Panel C). Each panel runs the benchmark alone,
on top of the market, on top of FF5, and on top of FF5 plus momentum. The spanning intercepts
range from 38.3 to 60.3 basis points per week and remain individually significant, and the loadings
on the additional benchmarks are small and insignificant in most rows. The AI premium is not
absorbed by exposure to technology-sector, semiconductor, or AI-themed equity baskets.
We then turn to geography. Table IA.15 repeats the quintile sort on the Datastream China
A-share panel, using either the baseline AI factor (Panel A) or a China-specific AI factor built
from OpenRouter consumption originating in mainland China (Panel B). The H−L spreads are
uniformly negative and statistically insignificant in both panels and under both weighting schemes.
The AI premium is concentrated in developed equity markets near the global AI frontier and is
absent from a market where AI is salient to investors but listed firms sit further from that frontier.
Finally, Figure IA.4 plots the 13-week rolling realized volatility of the value-weighted, all-
stock-breakpoint AI-beta long-short return, annualized by
√
52. The series varies meaningfully
over the sample, with peaks around major AI-news episodes, summarizing how the conditional
risk in AI exposure has evolved through the sample.
18

Table IA.14: Spanning Regressions for the AI-Beta H−L Portfolio with High-Tech Returns
𝛼 𝑡(𝛼)𝑏 Add 𝑡(𝑏 Add) ¯𝑅2
Panel A. FF10 HiTec return as additional control
Value-weighted, all-stock breakpoints
(1) HiTec 0.595 (2.79) 0.038 (0.56) 0.003
(2) Mkt + HiTec 0.558 (2.70) -0.454 (-2.48) 0.076
(3) FF5 + HiTec 0.554 (2.59) -0.450 (-1.43) 0.081
(4) FF5 + Mom + HiTec 0.532 (2.48) -0.499 (-1.57) 0.094
Value-weighted, NYSE breakpoints
(1) HiTec 0.454 (2.23) 0.031 (0.47) 0.002
(2) Mkt + HiTec 0.414 (2.12) -0.485 (-2.79) 0.090
(3) FF5 + HiTec 0.418 (2.06) -0.573 (-1.91) 0.094
(4) FF5 + Mom + HiTec 0.391 (1.93) -0.634 (-2.11) 0.115
Panel B. NAICS semiconductor return as additional control
Value-weighted, all-stock breakpoints
(1) Semi 0.600 (2.78) 0.004 (0.09) 0.000
(2) Mkt + Semi 0.603 (2.86) -0.132 (-1.96) 0.057
(3) FF5 + Semi 0.574 (2.63) -0.085 (-1.05) 0.073
(4) FF5 + Mom + Semi 0.560 (2.58) -0.133 (-1.53) 0.093
Value-weighted, NYSE breakpoints
(1) Semi 0.454 (2.20) 0.004 (0.11) 0.000
(2) Mkt + Semi 0.457 (2.27) -0.124 (-1.92) 0.056
(3) FF5 + Semi 0.433 (2.08) -0.080 (-1.03) 0.070
(4) FF5 + Mom + Semi 0.416 (2.02) -0.134 (-1.63) 0.099
Panel C. AI/robotics ETF basket as additional control
Value-weighted, all-stock breakpoints
(1) AI ETF 0.589 (2.77) 0.057 (0.91) 0.008
(2) Mkt + AI ETF 0.570 (2.70) -0.181 (-1.20) 0.035
(3) FF5 + AI ETF 0.546 (2.53) -0.042 (-0.23) 0.063
(4) FF5 + Mom + AI ETF 0.526 (2.43) -0.087 (-0.45) 0.073
Value-weighted, NYSE breakpoints
(1) AI ETF 0.441 (2.18) 0.076 (1.28) 0.015
(2) Mkt + AI ETF 0.431 (2.13) -0.049 (-0.34) 0.024
(3) FF5 + AI ETF 0.404 (1.96) 0.070 (0.39) 0.062
(4) FF5 + Mom + AI ETF 0.383 (1.85) 0.022 (0.12) 0.075
Note:The dependent variable is the H−L value-weighted AI-beta quintile spread. Panel A adds the Fama-French 10-
industry HiTec return, Panel B adds the value-weighted weekly return on the NAICS-defined semiconductor portfolio,
and Panel C adds the simple weekly excess return on an equal-weighted basket of seven AI ETFs (BOTZ, AIQ,
IRBO, ROBO, ARTY , WTAI, CHAT). The ETF basket return is the simple-return aggregation of the daily basket
minus the Fama-French weekly risk-free rate.𝑏 Add is the coefficient on the panel-specific additional control.Mktis
the Fama-French weekly market excess return. FF5 is the Fama-French five-factor model (Fama and French, 2015),
and FF5+Mom adds the momentum factor (Carhart, 1997). Each row is one OLS spanning regression, and no row
combines multiple additional controls. AI consumption data is weekly from January 2024 through April 2026. The
equity sample covers 108 formation weeks from March 2024 through March 2026.
19

Table IA.15: China A-Share Quintile Spreads Sorted on AI-Consumption Betas
Raw China-market𝛼
Weight𝛼 𝑡 𝛼 𝑡
Panel A. China A-shares sorted on𝛽 𝐴𝐼
Value-weighted -0.159 (-0.61) -0.167 (-0.63)
Equal-weighted -0.072 (-0.37) -0.073 (-0.36)
Panel B. China A-shares sorted on𝛽 𝐴𝐼,𝐶ℎ𝑖𝑛𝑎
Value-weighted -0.241 (-1.03) -0.113 (-0.45)
Equal-weighted -0.300 (-1.59) -0.219 (-1.07)
Note:The table reports value-weighted and equal-weighted High−Low spreads for China A-share stocks sorted into
pooled quintiles by their 13-week rolling log-excess AI beta. Panel A uses the overall AI factor. Panel B uses a
China-specific AI factor constructed from the subset of AI consumption originating from users in mainland China.
The sample is the Datastream China A-share common-stock panel.Rawis the time-series mean of the H−L spread.
China-market𝛼is the intercept from regressing the H−L spread on the value-weighted Datastream A-share market
log-excess return. Returns and alphas are in percent per week. AI consumption data is weekly from January 2024
through April 2026. Equity betas use 13-week rolling windows, so portfolio formation weeks begin in March 2024.
Jul 2024 Oct 2024 Jan 2025 Apr 2025 Jul 2025 Oct 2025 Jan 2026 Apr 2026
10
12
14
16
18
20
22Annualized realized volatility (%)
Value-weighted H-L return, all-stock breakpoints; 13-week rolling standard deviation, annualized by sqrt(52).
Figure IA.4: AI VIX: Rolling V olatility of the AI-Premium Portfolio
Note:The figure plots the AI VIX index, constructed as the 13-week rolling standard deviation of the value-weighted
high-minus-low AI-beta portfolio return, annualized by
√
52. The high-minus-low portfolio uses all-stock breakpoints,
the baseline AI beta, and the same value-weighted specification as the baseline portfolio-sort tests. AI consumption
data is weekly from January 2024 through April 2026. The equity sample covers 108 formation weeks from March
2024 through March 2026.
20

IA.4 Event Study of AI Model Releases
This appendix reports the details behind the event study in Section 3.3.4, where high-𝛽𝐴𝐼 firms
are shown to outperform low-𝛽𝐴𝐼 firms in narrow windows around major AI model releases. We
classify releases into two groups by provider. Frontier providers are Anthropic, DeepSeek, Google,
Meta, and OpenAI, and yield 29 events in the sample; releases from other providers add 36 more.
Table IA.17 documents each event with its sources.
Table IA.16 reports the CAR comparison in statistical form. Panel A uses frontier-provider
releases and Panel B uses releases from other providers, each over three event windows ((−1,+1),
(0,+1), and(0,+5)) and adjusted for the market model, the Fama-French three- and five-factor
models, and FF5 plus momentum. The frontier-provider effect dominates throughout. In Panel A,
the value-weighted CAR difference over the(0,+5)window is 1.731 percent (0.932 percent after
FF5+Mom adjustment), against 0.982 percent for non-frontier releases (and weaker after the same
controls).
21

Table IA.16: AI-Beta Long-Short Portfolio Returns Around AI Model Releases
Panel A. Frontier model releases (29 events)
(−1,+1) (0,+1) (0,+5)
Raw 1.127 0.704 1.731
t(2.59) (1.95) (3.31)
Market model 1.089 0.675 1.225
t(2.21) (1.78) (2.12)
FF3 0.787 0.476 0.726
t(1.79) (1.40) (1.37)
FF5 0.799 0.529 0.748
t(1.86) (1.64) (1.39)
FF5+Mom 0.609 0.452 0.932
t(1.62) (1.53) (1.80)
Panel B. Non-frontier model releases (36 events)
(−1,+1) (0,+1) (0,+5)
Raw 0.464 0.384 0.982
t(1.49) (1.58) (2.60)
Market model 0.285 0.194 0.705
t(0.86) (0.78) (1.75)
FF3 0.244 0.135 0.425
t(0.99) (0.75) (1.37)
FF5 0.072 0.103 0.237
t(0.28) (0.54) (0.71)
FF5+Mom 0.281 0.148 0.251
t(1.19) (0.86) (0.72)
Note:Panel A uses 29 frontier AI model release dates from Anthropic, OpenAI, Google, Meta, and DeepSeek. Panel B
uses 36 verified non-frontier releases from non-top-5 providers. For each event, firms in the eligible U.S. universe are
sorted by pre-event 13-week rolling AI beta and formed into value-weighted High-minus-Low portfolios. Windows
are trading days from the event anchor.Rawis the cumulative simple return. The Market model, Fama–French three-
factor model (FF3; Fama and French, 1993), Fama–French five-factor model (FF5; Fama and French, 2015), and
five-factor model augmented with momentum (FF5+Mom; Carhart, 1997) rows subtract expected returns from the
corresponding model estimated over the prior(−250,−30)trading-day window. Reported numbers are cross-event
mean H−L returns in percent, with𝑡-statistics in parentheses. AI consumption data is weekly from January 2024
through April 2026. The equity sample covers 108 formation weeks from March 2024 through March 2026.
22

Table IA.17: AI Model Release Calendar and Primary Sources
Panel A. Frontier model release calendar (29 events)
Date Provider and model Note
2024-04-18 Meta: Llama 3 Open model release; strong open-weight benchmark step.
2024-05-13 OpenAI: GPT-4o OpenAI flagship omni model; cheaper and faster API.
2024-05-14 Google: Gemini 1.5 Flash Fast/efficient Gemini family update at Google I/O.
2024-06-21 Anthropic: Claude 3.5 Sonnet Anthropic frontier Sonnet model.
2024-07-23 Meta: Llama 3.1 405B First frontier-level open-source AI model per Meta.
2024-09-12 OpenAI: o1-preview OpenAI first public reasoning-model series.
2024-10-22 Anthropic: Claude 3.5 Sonnet
new
Upgraded Sonnet plus public beta computer use.
2024-12-06 Meta: Llama 3.3 70B Efficiency/cost-improved Llama model; source is Meta year-end review.
2024-12-11 Google: Gemini 2.0 Google agentic-era model release.
2024-12-27 DeepSeek: DeepSeek-V3 Open-weight frontier MoE model; arXiv date used for public
paper/checkpoint availability.
2025-01-20 DeepSeek: DeepSeek-R1
release
Official model launch date per AWS Bedrock model card.
2025-01-27 DeepSeek: DeepSeek-R1
market recognition
US market-recognition shock one week after the Jan. 20 R1 release.
2025-02-24 Anthropic: Claude 3.7 Sonnet Hybrid reasoning model.
2025-02-27 OpenAI: GPT-4.5 OpenAI largest GPT model research preview.
2025-03-25 Google: Gemini 2.5 Pro Google thinking model.
2025-04-05 Meta: Llama 4 Scout/Maverick Open-weight natively multimodal Llama 4 models.
2025-04-14 OpenAI: GPT-4.1 API model with coding, instruction-following, and long-context gains.
2025-04-16 OpenAI: o3 and o4-mini OpenAI o-series reasoning models with tool access.
2025-05-22 Anthropic: Claude 4 Claude Opus 4 and Sonnet 4.
2025-08-07 OpenAI: GPT-5 OpenAI unified GPT-5 system.
2025-08-21 DeepSeek: DeepSeek V3.1 Hybrid thinking model; DeepSeek’s first step toward the agent era.
2025-09-29 Anthropic: Claude Sonnet 4.5 Anthropic frontier Sonnet model for complex agents and computer use.
2025-11-12 OpenAI: GPT-5.1 GPT-5 series update; agentic-focused API models followed the next day.
2025-11-18 Google: Gemini 3 Pro Gemini 3 flagship; Antigravity agentic platform launched the same day.
2025-11-24 Anthropic: Claude Opus 4.5 Anthropic flagship Opus model for coding, agents, and computer use.
2025-12-01 DeepSeek: DeepSeek V3.2 Stable V3.2 and V3.2-Speciale; reasoning-first open-weight models.
2025-12-11 OpenAI: GPT-5.2 GPT-5 series update for professional work and long-running agents.
2026-02-05 Anthropic: Claude Opus 4.6 Agent teams and 1M-token context; same-day general availability.
2026-02-19 Google: Gemini 3.1 Pro Reasoning-focused Gemini flagship update; preview in the API and AI
Studio.
2026-03-05 OpenAI: GPT-5.4 GPT-5.4, GPT-5.4 Thinking, and GPT-5.4 Pro; mini and nano followed on
March 17.
23

Panel B. Non-frontier model release calendar (36 events)
Date Provider and model Note
2024-03-11 Cohere: Command R RAG / tool-use enterprise LLM (128K context).
2024-03-17 xAI: Grok-1 (open weights) 314B-parameter MoE base model, Apache 2.0.
2024-03-27 Databricks: DBRX 132B-parameter MoE open LLM (36B active).
2024-03-28 AI21: Jamba First production-grade hybrid SSM-Transformer LLM.
2024-04-04 Cohere: Command R+ Scaled-up RAG/tool-use enterprise LLM (104B).
2024-04-15 Reka: Reka Core Frontier-class multimodal model (text/image/video/audio).
2024-04-23 Microsoft: Phi-3 (mini) 3.8B small language model launched on Azure.
2024-05-13 01.AI: Yi-Large 01.AI’s first proprietary closed-source frontier dense LLM.
2024-06-05 Zhipu: GLM-4-9B (open
weights)
Open-weight 9B variant of the GLM-4 family.
2024-06-07 Alibaba: Qwen 2 Qwen 2 family (0.5B-72B) open-source release.
2024-07-24 Mistral: Mistral Large 2 123B-parameter flagship multilingual / code-strong dense LLM.
2024-08-01 Black Forest Labs: FLUX.1 12B rectified-flow text-to-image model family.
2024-08-13 xAI: Grok-2 Grok-2 / Grok-2 mini early-preview release on X.
2024-08-22 AI21: Jamba 1.5 family Hybrid SSM-Transformer family with 256K context.
2024-09-19 Alibaba: Qwen 2.5 Open-source family announced at Apsara Conference.
2024-10-21 IBM: Granite 3.0 Apache-2.0 enterprise LLM family launched at TechXchange.
2024-11-05 Tencent: Hunyuan-Large 389B-parameter MoE (52B active) open-sourced.
2024-11-18 Mistral: Pixtral Large 124B open-weights multimodal model (123B + 1B vision).
2024-11-28 Alibaba: QwQ-32B-Preview Open-weight reasoning model preview from Qwen.
2024-12-03 Amazon: Nova family Foundation-model family launched on Amazon Bedrock at re:Invent.
2024-12-12 Microsoft: Phi-4 14B reasoning-focused SLM (Azure preview, fully open Jan 2025).
2025-01-22 ByteDance: Doubao 1.5 Pro Large-scale sparse MoE flagship on V olcano Engine.
2025-01-28 Alibaba: Qwen 2.5-Max Closed-source MoE flagship API model.
2025-02-17 xAI: Grok-3 Flagship reasoning model trained on Colossus.
2025-03-13 Cohere: Command A 111B enterprise model (256K context, 2 GPU inference).
2025-04-29 Alibaba: Qwen 3 Hybrid thinking/non-thinking dense + MoE family.
2025-06-10 Mistral: Magistral (Small +
Medium)
Mistral’s first reasoning-focused models.
2025-07-09 xAI: Grok 4 Grok 4 / Grok 4 Heavy livestream release.
2025-07-11 Moonshot: Kimi K2 1T-parameter open-weight MoE flagship built for agentic tasks.
2025-07-28 Zhipu: GLM-4.5 355B open-weight flagship with native agent abilities (GLM-4.5 and
GLM-4.5-Air).
2025-10-02 IBM: Granite 4.0 Hybrid Mamba/transformer enterprise model family, general availability.
2025-10-27 MiniMax: MiniMax M2 Open-weight model built for agents and code.
2025-12-02 Amazon: Nova 2 family Nova 2 Lite, Pro, Sonic, and Omni announced at re:Invent.
2025-12-02 Mistral: Mistral Large 3 675B sparse MoE flagship (41B active), released with the Ministral 3 series.
2026-01-27 Moonshot: Kimi K2.5 Visual agentic model; agent swarms of up to 100 sub-agents.
2026-02-12 MiniMax: MiniMax M2.5 Coding, agentic tool use, and search.
2026-02-12 Zhipu: GLM-5 Flagship for complex systems engineering and long-horizon agentic tasks.
2026-02-14 ByteDance: Doubao-Seed-2.0 Doubao-Seed-2.0 series (Pro, Lite, Mini, Code); press source.
2026-02-16 Alibaba: Qwen3.5 Qwen3.5 family: Plus API model and 397B-A17B open weights.
Note:Model names link to the cited sources. Dates are announced public release dates and sources are primary citations. Panel A
is the frontier-event sample. Panel A lists both the DeepSeek-R1 release date and the U.S. market-recognition date one week later.
The event studies anchor DeepSeek-R1 on the January 20, 2025 release date, so the two DeepSeek-R1 rows document a single
event and Panel A contains 29 events. Releases that share an event day (Panel B: the rows dated December 2, 2025; the rows dated
February 12, 2026; the rows dated February 14, 2026 and February 16, 2026 (both anchored on February 17, 2026)) are listed
separately but enter the event studies once, so Panel B contains 36 events. Panel B excludes Anthropic, OpenAI, Google, Meta, and
DeepSeek and keeps flagship or series-defining releases. AI consumption data is weekly from January 2024 through April 2026.
The equity sample covers 108 formation weeks from March 2024 through March 2026.
24

IA.5 AI Exposure
This section reports the industry- and firm-level exposure maps behind the portfolio evidence.
Figure IA.5 shows how the baseline AI factor and the split-specific AI factors revalue the Fama-
French 10 industries. Each cell reports the value-weighted average firm-level AI beta within an
industry, scaled by the weekly standard deviation of the relevant AI factor, so the numbers can
be read as the percentage-point response of an industry-average weekly return to a one-standard-
deviation shock to that AI factor. Most industries have positive baseline AI exposure, with the
largest values in retail. Non-durable goods and health have negative exposure on average. The
high-technology sector is only modestly exposed on the baseline factor, masking strongly positive
exposure of semiconductor and AI-infrastructure firms and negative exposure elsewhere in tech-
nology. The cross-factor columns show that exposures are larger and more concentrated when
the factor is built from closed-source models, paid/core users, seasoned users, and long prompts.
The figure reads AI exposure as a broad diffusion and deployment shock rather than as a narrow
technology-sector label.
Figure IA.6 compares the industry exposures in Panel A of Figure 4, which average the firms’
13-week rolling exposures, with full-sample industry exposures. The full-sample exposure of an
industry is the coefficient on the AI factor in a single regression of the industry’s value-weighted
weekly log-excess return on the AI factor, the Fama-French five factors, and momentum over the
full sample. The two measures order the industries similarly, with a Spearman rank correlation of
0.73. Health and non-durable goods are the two most negative industries under both measures, and
retail/wholesale ranks first under the average measure and second under the full-sample measure.
These three industries are also the only ones whose full-sample exposure is statistically significant,
at the 1 percent level for health and at the 5 percent level for non-durable goods and for retail and
wholesale.
Figure IA.7 reports the firm-level exposure ranking discussed in Section 3.4. Panel A shows
the 50 current S&P 500 firms with the largest positive average rolling AI exposures, and Panel B
shows the 50 firms with the most negative exposures.
25

Figure IA.5: Industry Exposure to AI Factor
AI AIClosed AIOpen
1R'XU
'XUEO
0DQXI
(QUJ\
+L7HF
7HOFP
6KRSV
+OWK
8WLOV
2WKHU
  
  
  
  
  
  
  
  
  
  
3DQHO$0RGHO7\SH
AI AICore AINoncore
1R'XU
'XUEO
0DQXI
(QUJ\
+L7HF
7HOFP
6KRSV
+OWK
8WLOV
2WKHU
  
  
  
  
  
  
  
  
  
  
3DQHO%8VHU,QWHQVLW\
AI AISeasoned AINonseasoned
1R'XU
'XUEO
0DQXI
(QUJ\
+L7HF
7HOFP
6KRSV
+OWK
8WLOV
2WKHU
  
  
  
  
  
  
  
  
  
  
3DQHO&8VHU7HQXUH
AI ln TokLong
 ln TokShort
1R'XU
'XUEO
0DQXI
(QUJ\
+L7HF
7HOFP
6KRSV
+OWK
8WLOV
2WKHU
  
  
  
  
  
  
  
  
  
  
3DQHO'3URPSW/HQJWK
Note:The figure reports the implied weekly industry return in percent associated with a one-standard-deviation in-
crease in each AI variable for the Fama-French 10 industries. For each firm-week, the relevant beta is estimated from
the same 13-week rolling regression of weekly log-excess returns on the log-excess market return and the AI variable
used in the portfolio sorts. Within each FF10 industry, we take the value-weighted mean of firm-level betas using
formation-week market equity weights; each cell reports100× 𝛽
𝑋
𝑗,vw×𝜎𝑤(𝑋)for the column variable𝑋. The base-
line𝐴𝐼factor is the first principal component of weekly log growth in total tokens, usage dollars, and distinct users.
Panel A compares𝐴𝐼,𝐴𝐼 𝐶𝑙𝑜𝑠𝑒𝑑 , and𝐴𝐼 𝑂𝑝𝑒𝑛 . Panel B compares𝐴𝐼,𝐴𝐼 𝐶𝑜𝑟𝑒 , and𝐴𝐼 𝑁𝑜𝑛𝑐𝑜𝑟𝑒 . Panel C compares
𝐴𝐼,𝐴𝐼 𝑆𝑒𝑎𝑠𝑜𝑛𝑒𝑑 , and𝐴𝐼 𝑁𝑜𝑛𝑠𝑒𝑎𝑠𝑜𝑛𝑒𝑑 . Panel D compares𝐴𝐼,Δln𝑇𝑜𝑘 𝐿𝑜𝑛𝑔 , andΔln𝑇𝑜𝑘 𝑆ℎ𝑜𝑟𝑡 . Samples vary by split
according to non-missing rolling-beta availability. Cell shading is scaled within each column; blue denotes positive
responses and red denotes negative responses. AI consumption data is weekly from January 2024 through April 2026.
The equity sample covers 108 formation weeks from March 2024 through March 2026.
26

Figure IA.6: Industry AI Exposure: Average Firm Exposure and Full-Sample Regressions
−0.4 −0.2 0.0 0.2
Response to a one s.d. AI shock
(% per week)
Health
Non-durable goods
High technology
Energy
Manufacturing
Telecoms
Utilities
Consumer durables
Other
Retail & wholesale
Panel A
Average firm exposure
−0.4 −0.2 0.0 0.2
Response to a one s.d. AI shock
(% per week)
Health
Non-durable goods
Manufacturing
Utilities
High technology
Other
Energy
Telecoms
Retail & wholesale
Consumer durables
Panel B
Full-sample regression
Note:The figure reports AI exposure for the Fama-French 10 industries, as the return response, in percentage points per
week, to a one-standard-deviation AI-factor shock. Panel A repeats Panel A of Figure 4, the value-weighted average
of firm-level exposures, where a firm’s exposure is the coefficient on the AI factor in 13-week rolling regressions of
its weekly log-excess return on the AI factor and the log-excess market return. Panel B reports full-sample exposure.
For each industry, the value-weighted weekly log-excess return is regressed once on the AI factor, the Fama-French
five factors, and momentum over the 108 holding weeks from March 2024 through March 2026. Industry returns use
the same firms and formation-week market equity weights as Panel A. The two panels share the horizontal axis.
27

Panel A. Top 50 S&P 500 Firms
1. APP AppLovin
2. CVNA Carvana
3. LITE Lumentum
4. BKR Baker Hughes
5. CMI Cummins
6. EXE Expand Energy
7. PODD Insulet Corporation
8. EXPE Expedia Group
9. TPR Tapestry, Inc.
10. PH Parker Hannifin
11. EQT EQT Corporation
12. NRG NRG Energy
13. FFIV F5, Inc.
14. WDC Western Digital
15. STX Seagate Technology
16. KVUE Kenvue
17. TRGP Targa Resources
18. RL Ralph Lauren Corporation
19. PGR Progressive Corporation
20. ORLY O’Reilly Automotive
21. TRMB Trimble Inc.
22. GEV GE Vernova
23. OKE Oneok
24. RF Regions Financial Corporation
25. COHR Coherent Corp.
26. JCI Johnson Controls
27. GRMN Garmin
28. AZO AutoZone
29. CFG Citizens Financial Group
30. FIX Comfort Systems USA
31. SW Smurfit Westrock
32. VMC Vulcan Materials Company
33. CTAS Cintas
34. CRWD CrowdStrike
35. IBKR Interactive Brokers
36. C Citigroup
37. UAL United Airlines Holdings
38. WELL Welltower
39. WM Waste Management
40. ETR Entergy
41. KEY KeyCorp
42. ROL Rollins, Inc.
43. TAP Molson Coors Beverage Company
44. IDXX Idexx Laboratories
45. SBUX Starbucks
46. NCLH Norwegian Cruise Line Holdings
47. MAR Marriott International
48. AON Aon plc
49. XEL Xcel Energy
50. FAST Fastenal
1
2
0
High-tech Shops Utilities All other industries
Figure IA.7: S&P 500 Firm-Level AI Exposure
28

Panel B. Bottom 50 S&P 500 Firms
1. MRNA Moderna
2. EL Estée Lauder Companies
3. SWKS Skyworks Solutions
4. AMD Advanced Micro Devices
5. ON ON Semiconductor
6. CRL Charles River Laboratories
7. DHR Danaher Corporation
8. CMG Chipotle Mexican Grill
9. LLY Lilly (Eli)
10. MPWR Monolithic Power Systems
11. FSLR First Solar
12. ALB Albemarle Corporation
13. NKE Nike, Inc.
14. APTV Aptiv
15. RVTY Revvity
16. MRK Merck & Co.
17. NEE NextEra Energy
18. MCHP Microchip Technology
19. REGN Regeneron Pharmaceuticals
20. EFX Equifax
21. VRTX Vertex Pharmaceuticals
22. QCOM Qualcomm
23. ABBV AbbVie
24. AES AES Corporation
25. ZTS Zoetis
26. CHTR Charter Communications
27. DOW Dow Inc.
28. HII Huntington Ingalls Industries
29. JBHT J.B. Hunt
30. NXPI NXP Semiconductors
31. TECH Bio-Techne
32. PFE Pfizer
33. BAX Baxter International
34. KDP Keurig Dr Pepper
35. AKAM Akamai Technologies
36. MRVL Marvell Technology
37. IQV IQVIA
38. ADM Archer Daniels Midland
39. LULU Lululemon Athletica
40. COO Cooper Companies
41. CF CF Industries
42. AMT American Tower
43. ORCL Oracle Corporation
44. HRL Hormel Foods
45. PTC PTC Inc.
46. PYPL PayPal
47. BBY Best Buy
48. BALL Ball Corporation
49. ABNB Airbnb
50. VTRS Viatris
-1
-2
0
High-tech Healthcare Manufacturing All other industries
Figure IA.7: S&P 500 Firm-Level AI Exposure (continued)
Note:The figure plots the 50 current S&P 500 firms with the largest positive (Panel A) and most negative (Panel B)
average rolling exposures to the baseline AI factor. Firm-level𝛽 𝐴𝐼 is estimated from 13-week rolling regressions of
weekly log-excess returns on the market log-excess return and the AI factor, then averaged across valid weeks. Radial
distance reports100× 𝛽
𝐴𝐼
𝑖 ×𝜎𝑤(𝐴𝐼), the weekly return in percentage points associated with a one-standard-deviation
AI-factor shock. Label colors denote Fama-French 10 industries, as shown in the legend. Both panels use the same
radial scale.
29

IA.6 Additional AI Stylized Facts
This section collects additional stylized facts on AI consumption based on the OpenRouter
data.
Table IA.18 lists the agentic-economy concepts we extract from the OpenRouter data and the
weekly factor that proxies each. These salient components of AI token consumption associated
with agentic calls are used in the analysis of firms’ exposure to agentic consumption discussed in
Section 5 of the paper and specifically in Table IA.12.
Table IA.18: Agentic-Economy Concepts and Factor Definitions
Factor Concept Construction
Agentic tokens Tool use Log growth in total tokens on requests whose normalized
finish reason istool_calls.
Cache-read tokens Context reuse Log growth in cache-read tokens—prompt-prefix tokens
served from cache rather than recomputed.
Reasoning tokens Test-time compute Log growth in reasoning tokens—the model’s internal
reasoning (“work plan”) tokens.
Agentic dollars Token economics Log growth in usage dollars on requests whose normal-
ized finish reason istool_calls.
Note:Each row is one weekly factor built from the OpenRouter inference logs; the corresponding token and dollar
shares are plotted in Figure IA.8. Total tokens are prompt plus completion tokens. Each factor is a weekly log growth,
ln𝐿𝑡−ln𝐿 𝑡−1 , of a positive weekly level. The agentic, cache-read, and reasoning slices are populated only after their
instrumentation onset.
Figure IA.8 reports the corresponding token, dollar, cache-read, and reasoning shares.
Table IA.19 compares the granular OpenRouter user–model–day panel with the scraped, ag-
gregate data from the OpenRouter public website used by Demirer, Fradkin, Tadelis and Peng
(2025).
30

Panel A. Agentic Token Share versus Dollar Share
2025-04 2025-07 2025-10 2026-01 2026-04
0%
10%
20%
30%
40%
50%
60%Agentic share of OpenRouter total
Token share
Dollar (cost) share
Panel B. Tool-Call, Cache-Read, and Reasoning Token Shares
2025-04 2025-07 2025-10 2026-01 2026-04
0%
10%
20%
30%
40%
50%
60%Share of total tokens
Tool-call
Cache-read
Reasoning
Figure IA.8: Token, Dollar, and Intensity Shares of Agentic AI Consumption
Note:The two panels plot the weekly evolution of agentic AI consumption in the OpenRouter data, January 2024
through April 2026. Panel A compares the agentic share of total tokens with its share of total usage dollars. The
agentic margin is defined as all tokens on requests whose normalized finish reason istool_calls. Panel B plots three
token-level margins, each as a share of total tokens: the agentic share, the cache-read share (cached tokens divided by
total tokens), and the reasoning share (reasoning tokens divided by total tokens).
31

Table IA.19: Granular OpenRouter Facts for Comparison with Demirer, Fradkin, Tadelis and Peng (2025)
Panel A. Open-Source Token and Dollar Shares
Period Week Class Request share Token share Dollar share
First week 2024-01-01 Closed 9.4 15.6 51.9
First week 2024-01-01 Open 90.6 84.4 48.1
Final week 2026-04-13 Closed 54.8 51.6 84.7
Final week 2026-04-13 Open 45.2 48.4 15.3
Panel B. Market Dynamism in Tokens and Dollars
Metric Model HHI first Model HHI latest Change Author HHI first Author HHI latest Change
Requests 1321.7 267.5 -79.8 1764.7 1565.1 -11.3
Tokens 1057.9 333.4 -68.5 1508.6 1117.0 -26.0
Usage dollars 975.6 959.3 -1.7 1996.2 3435.8 72.1
Metric Horizon Model top-10 retention Author top-10 retention
Requests 4 weeks 87.0 91.0
Requests 8 weeks 85.0 90.0
Requests 12 weeks 80.0 90.0
Tokens 4 weeks 58.0 78.0
Tokens 8 weeks 36.7 73.3
Tokens 12 weeks 35.0 85.0
Usage dollars 4 weeks 70.0 92.0
Usage dollars 8 weeks 50.0 86.7
Usage dollars 12 weeks 35.0 80.0
Panel C. Prompt-Price Elasticity Comparison
Specification Paper coef. Our coef. Our𝑡-stat. Obs.
Date FE -0.55 -0.450 (-4.67) 52,728
Date + model FE -1.08 -1.170 (-5.66) 52,728
Model-date + model-provider FE -1.11 0.280 (0.79) 53,800
Panel D. Multihoming and Concentration Across OpenRouter Entities
Entity First Latest≥2 first≥2 latest
API key 2025-01-01 2026-04-01 48.7 51.8
Application 2025-01-01 2026-04-01 38.3 35.8
Note:Panel A reports shares among the open-plus-closed model universe using realized requests, prompt-plus-completion tokens, and usage dollars. Panel B reports Herfindahl-
Hirschman indices across models and authors and average top-10 retention in the latest 90 days of the sample. Panel C compares the prompt-price elasticity estimates in Demirer,
Fradkin, Tadelis and Peng (2025), Table 2, with the corresponding granular OpenRouter reconstruction. The sample is open-source model-provider-days, the dependent variable
is log token quantity, and the price regressor is log posted prompt price. Panel D reports multihoming among OpenRouter applications and API keys. Usage dollars are the
realized OpenRouterusagefield, not a recomputation from posted prices. Shares and changes are reported in percent. Data is weekly from January 2024 through April 2026.
32

Their public scrape records posted prices and aggregate token counts but cannot observe re-
alized spending, individual users, or within-model variation, and four of their headline findings
change once these margins are visible in our licensed user–model–day panel. First, Demirer, Frad-
kin, Tadelis and Peng (2025) report that the average price per token is roughly constant. The series
they recover is a token-weighted list price, which the scrape cannot distinguish from the price ac-
tually paid. We find that the price paid fell by about 30 percent within their 2025 window and by
about half over our full sample. Second, Demirer, Fradkin, Tadelis and Peng (2025) put the open-
weight share at about 48 percent of tokens. The same models earn only about 15 percent of realized
dollars, overstating open-weight’s economic weight by roughly threefold. Third, Demirer, Fradkin,
Tadelis and Peng (2025) document rapid turnover among leading models and creators. Weighted
by realized dollars rather than tokens, the market instead consolidates: creator-level concentration
rises by 72 percent. Fourth, Demirer, Fradkin, Tadelis and Peng (2025) estimate short-run prompt-
price elasticities just above one. With model-date and provider fixed effects in our panel, these
elasticities become small and statistically insignificant. The table also reports application-level
multihoming: only 35.8 percent of applications use at least two models in the latest month, with
the median top-model token share at 100 percent.
Figures IA.9 and IA.10 show how long AI consumption persists at the account level. Retention
at week𝑘is the share of the accounts that start using a model, or any model of a provider, in a given
week and are active on it in week𝑘or in a later week within twelve weeks. Among the five frontier
providers in Figure IA.9, 41 to 58 percent of new accounts use the provider again within twelve
weeks, and 6 to 13 percent are still active in the twelfth week. DeepSeek retains the most accounts
over the first five weeks, and Anthropic retains the most from the sixth week on. In the twelfth
week, 12.8 percent of Anthropic’s new accounts are still active, against 6.4 percent of Meta’s.
Figure IA.10 splits model adopters along two of the margins in Section 3.3.2. Closed-source
and open-weight models retain their adopters at almost the same rate, with 5.4 and 4.8 percent still
active in the twelfth week, even though exposure to closed-source consumption earns the larger
premium in Table 6. Seasoned users stay longer than non-seasoned users at every horizon. Within
twelve weeks, 47.2 percent of seasoned adopters use the model again, against 39.8 percent of non-
seasoned adopters, and 6.9 against 4.4 percent are still active in the twelfth week. Exposure to
seasoned-user consumption also earns the larger premium in Table 6.
33

1 2 4 6 8 10 12
Weeks since first use
0%
10%
20%
30%
40%
50%
60%Share of accounts retained Anthropic
DeepSeek
Google
Meta
OpenAI
Figure IA.9: User Retention by Model Provider
Note:The figure plots twelve-week user retention for the five frontier providers in the event study of Section 3.3.4:
Anthropic, DeepSeek, Google, Meta, and OpenAI. For each provider, a cohort consists of the accounts that use any of
the provider’s models for the first time in a given week. Retention at week𝑘is the share of the cohort that is active
on any of the provider’s models in week𝑘or in a later week within twelve weeks of first use. Cohorts are pooled
over the weeks from January 29, 2024 through January 12, 2026, the last week that can be followed for twelve weeks
before the data end in April 2026. Cohorts from the first four weeks of 2024 are left out because accounts first seen
in those weeks may have used the provider before the sample starts. The pooled cohorts contain between 0.5 million
(Anthropic) and 2.1 million (DeepSeek) accounts.
34

Panel A. Closed-Source versus Open-Weight Models
1 2 4 6 8 10 12
Weeks since first use
0%
10%
20%
30%
40%
50%Share of accounts retained
Closed-source models
Open-weight models
Panel B. Seasoned versus Non-Seasoned Users
1 2 4 6 8 10 12
Weeks since first use
0%
10%
20%
30%
40%
50%Share of accounts retained
Seasoned users
Non-seasoned users
Figure IA.10: User Retention by Model Type and User Experience
Note:The two panels plot twelve-week retention of model adopters along two of the margins in Section 3.3.2. A
cohort consists of the accounts that use a given model for the first time in a given week, and each curve pools the
cohorts of all models in the group. Retention at week𝑘is the share of the cohort that is active on the same model in
week𝑘or in a later week within twelve weeks of first use. Panel A splits models into closed-source and open-weight
models following OpenRouter’s model taxonomy. Panel B splits adopters by whether the account is seasoned in the
week of first use, that is, observed for at least 13 weeks, active in at least eight prior weeks, and with at least 20 prior
requests. Cohorts are pooled over the weeks from January 29, 2024 through January 12, 2026. Panel A pools 6.9
million first uses of closed-source models and 11.5 million first uses of open-weight models (models without a closed
or open classification are left out), and Panel B pools 3.9 million first uses by seasoned accounts and 15.0 million by
non-seasoned accounts.
35

IA.7 Skill Exposure to AI
This section reports the occupation-level exposure map that underlies the skill-exposure ex-
ercise in the main text. Figure IA.11 maps firm and industry AI exposures into SOC minor
occupation groups using BLS occupation-by-industry employment weights, and plots the result-
ing employment-weighted occupation exposure to the baseline AI factor. Panels A and B to-
gether rank all 109 SOC minor occupation groups, with the colored rail flagging coherent eco-
nomic themes. Positive exposure clusters in installation, maintenance, persuasion, instruction, and
systems-integration occupations. Negative exposure clusters in science, healthcare, and operations-
control occupations. The pattern is the occupation-level counterpart of the firm-level finding that
the AI premium is broad rather than confined to the technology sector.
36

Panel A. Ranks 1–55
001 Postsecondary T eachers, All Other
002 Postsecondary T eachers
003 Vehicle/mobile equipment mechanics, installers, repairers
004 Extraction Workers
005 Other Transportation Workers
006 Other educational instruction and library occupations
007 Material Moving Workers, All Other
008 Law Enforcement Workers
009 T our and Travel Guides
010 Other Personal Care and Service Workers
011 Librarians, Curators, and Archivists
012 Helpers, Construction Trades
013 Electricians
014 Sheet Metal Workers
015 Entertainment Attendants and Related Workers
016 Firefighting and Prevention Workers
017 Supervisors: building/grounds cleaning and maintenance
018 Retail Sales Workers
019 Entertainers and Performers, Sports and Related Workers
020 Supervisors: sales workers
021 Supervisors: construction and extraction
022 Supervisors: installation, maintenance, repair
023 Office and Administrative Support Workers, All Other
024 Grounds Maintenance Workers
025 Material Moving Workers
026 Water Transportation Workers
027 Supervisors: personal care and service
028 Air Transportation Workers
Ranks 1-28
0.0 0.5
Occupation AI beta × 100
+0.38
+0.38
+0.35
+0.34
+0.32
+0.31
+0.30
+0.30
+0.28
+0.24
+0.23
+0.23
+0.22
+0.21
+0.21
+0.19
+0.17
+0.17
+0.17
+0.16
+0.16
+0.15
+0.15
+0.15
+0.14
+0.14
+0.13
+0.11
029 Building Cleaning and Pest Control Workers
030 Information and Record Clerks
031 Sales Representatives, Services
032 Other Management Occupations
033 Electrical/electronic equipment mechanics, installers, repairers
034 Preschool, elementary, secondary, special- ed teachers
035 Other T eachers and Instructors
036 Weighers, Measurers, Checkers, and Samplers, Recordkeeping
037 Legal Support Workers
038 Religious Workers
039 Construction Trades Workers
040 Supervisors: transportation and material moving
041 Media/communication equipment workers
042 Sales Representatives, Wholesale and Manufacturing
043 Other Office and Administrative Support Workers
044 Advertising, marketing, PR, and sales managers
045 Other Installation, Maintenance, and Repair Occupations
046 Financial Specialists
047 Baggage Porters, Bellhops, and Concierges
048 Business Operations Specialists
049 Supervisors: office and administrative support
050 Supervisors: farming, fishing, forestry
051 Lawyers, Judges, and Related Workers
052 Operations Specialties Managers
053 T op Executives
054 Computer Occupations
055 Occupational health/safety specialists and technicians
Ranks 29-55
0.0 0.5
Occupation AI beta × 100
+0.10
+0.10
+0.10
+0.096
+0.094
+0.086
+0.077
+0.076
+0.069
+0.068
+0.067
+0.065
+0.062
+0.061
+0.054
+0.052
+0.045
+0.043
+0.039
+0.030
+0.030
+0.030
+0.028
+0.028
+0.028
+0.026
+0.024
Human capital
Physical build-out
Commercialization
Trust/risk control
Scarce human experience
Mixed boundary
Local/non-scalable
37

Panel B. Ranks 56–109
056 Business Operations Specialists, All Other
057 Forest/conservation/logging workers
058 Human Resources Managers
059 Mathematical Science Occupations
060 Plant and System Operators
061 Art and Design Workers
062 Communications Equipment Operators
063 Financial Clerks
064 Home health/personal care aides; nursing aides/orderlies
065 Metal Workers and Plastic Workers
066 Material recording, scheduling, dispatching, distributing workers
067 Welders, Cutters, Solderers, and Brazers
068 Food Processing Workers
069 Other Food Preparation and Serving Related Workers
070 Receptionists and Information Clerks
071 Other Construction and Related Workers
072 Assemblers and Fabricators
073 Cooks and Food Preparation Workers
074 Food and Beverage Serving Workers
075 Supervisors: food preparation and serving
076 Counselors, social workers, community/social service specialists
077 Woodworkers
078 Secretaries and Administrative Assistants
079 Packaging and Filling Machine Operators and T enders
080 Media and Communication Workers
081 Supervisors: protective service
082 Motor Vehicle Operators
Ranks 56-82
0.0 0.5
Occupation AI beta × 100
+0.022
+0.015
+0.013
+0.012
+0.011
+0.009
+0.007
+0.004
+0.004
+0.001
+0.000
-0.000
-0.004
-0.010
-0.014
-0.015
-0.016
-0.017
-0.020
-0.021
-0.022
-0.024
-0.024
-0.025
-0.026
-0.026
-0.033
083 Supervisors: production workers
084 Agricultural Workers
085 Drafters, engineering technicians, mapping technicians
086 Other healthcare practitioners and technical occupations
087 Industrial Engineers
088 Engineers
089 Other Sales and Related Workers
090 Other Protective Service Workers
091 Registered Nurses
092 Other Production Occupations
093 Architects, Surveyors, and Cartographers
094 Managers, All Other
095 Funeral Service Workers
096 Health T echnologists and T echnicians
097 Healthcare Diagnosing or Treating Practitioners
098 Rail Transportation Workers
099 Life, physical, and social science technicians
100 Physicians, All Other
101 T extile, Apparel, and Furnishings Workers
102 Other Healthcare Support Occupations
103 Personal Appearance Workers
104 Printing Workers
105 Physical Scientists
106 Animal Care and Service Workers
107 Social Scientists and Related Workers
108 Life Scientists
109 Occupational/physical therapy assistants and aides
Ranks 83-109
0.0 0.5
Occupation AI beta × 100
-0.041
-0.041
-0.046
-0.050
-0.051
-0.053
-0.067
-0.068
-0.071
-0.072
-0.080
-0.082
-0.083
-0.085
-0.089
-0.096
-0.11
-0.12
-0.14
-0.15
-0.15
-0.16
-0.18
-0.20
-0.20
-0.25
-0.26
Commercialization
Scarce human experience
Mixed boundary
Routine information
Routine production
Healthcare/care
Long-cycle science
Local/non-scalable
Mature networks
Figure IA.11: Occupation Exposure to the AI Factor
Note:The figure plots the full-firm occupation ranking based on SOC minor occupation groups. NAICS-level exposure
is the market-equity-weighted mean of firm-level AI betas within NAICS-week cells, requiring at least three firms in a
NAICS-week, averaged over time and mapped to occupations using BLS OEWS occupation-by-industry employment
weights. Detailed SOC occupations are aggregated to SOC minor groups using employment weights. The plotted
value is100×𝛽 𝐴𝐼 𝑜 , where𝛽 𝐴𝐼 𝑜 is the employment-weighted occupation exposure to the baseline AI factor. The colored
rail marks the coherent economic theme assigned to each occupation group. Panel A reports ranks 1–55, and Panel
B reports ranks 56–109. Underlying firm-level AI betas are estimated on the equity sample of 108 formation weeks
from March 2024 through March 2026.
38

IA.8 Determinants of Firm-Level AI Betas
This section asks which firm characteristics are associated with the firm-level AI betas that
underlie the portfolio sorts. Table IA.20 reports pooled panel regressions of the weekly rolling
AI beta on firm characteristics, with week fixed effects (Panel A) or week and Fama-French 30
industry fixed effects (Panel B) and standard errors clustered by week and firm. High-AI-beta firms
are past winners and are more profitable and more levered: in the full specification of Panel A, the
momentum, gross-profitability, and leverage coefficients are 0.464, 0.402, and 0.358, all significant
at the 1 percent level. AI exposure declines with idiosyncratic volatility and with R&D intensity,
with coefficients of−10.814and−1.568that are both significant at the 1 percent level, and the
unconditional size gradient in column (1) largely disappears once the full set of controls is included.
The within-industry estimates in Panel B show a similar pattern, so the characteristic profile of
high-AI-beta firms is not a by-product of industry composition.
39

Table IA.20: Determinants of Firm-Level AI Betas
(1) (2) (3) (4) (5)
Panel A. Week fixed effects
ln𝑀𝐸0.056 0.059 0.064 0.010 0.010
(6.95) (5.61) (5.89) (1.08) (1.05)
ln𝐵𝑀0.079 0.135 0.093 0.055
(3.01) (4.93) (3.96) (2.27)
𝑀𝑜𝑚0.456 0.488 0.474 0.464
(6.24) (6.67) (6.71) (6.55)
𝑃𝑟𝑜𝑓𝑖𝑡0.507 0.492 0.402
(5.80) (5.66) (4.66)
𝐴𝐺-0.045 0.068 0.040
(-0.77) (1.24) (0.73)
𝑅𝑂𝐸0.011 -0.053
(0.27) (-1.24)
𝐿𝑒𝑣0.481 0.358
(6.93) (5.20)
𝐼𝑣𝑜𝑙-12.264 -10.814
(-6.90) (-6.11)
𝑇𝑢𝑟𝑛0.001 0.000
(0.36) (0.07)
𝐼𝑙𝑙𝑖𝑞0.007 0.004
(0.40) (0.23)
𝐶𝑎𝑝𝑥-0.480
(-0.78)
𝑅&𝐷-1.568
(-5.00)
Obs 367,059 263,850 257,421 255,939 255,084
𝑅2 0.054 0.078 0.083 0.099 0.101
(1) (2) (3) (4) (5)
Panel B. Week and industry fixed effects
ln𝑀𝐸0.054 0.040 0.046 0.017 0.017
(6.71) (4.05) (4.50) (1.82) (1.79)
ln𝐵𝑀-0.004 0.051 0.052 0.031
(-0.17) (2.05) (2.18) (1.32)
𝑀𝑜𝑚0.409 0.420 0.442 0.438
(5.67) (5.90) (6.23) (6.15)
𝑃𝑟𝑜𝑓𝑖𝑡0.631 0.576 0.520
(6.41) (6.17) (5.68)
𝐴𝐺0.002 0.055 0.038
(0.04) (0.99) (0.67)
𝑅𝑂𝐸-0.050 -0.083
(-1.24) (-1.97)
𝐿𝑒𝑣0.205 0.148
(2.88) (2.10)
𝐼𝑣𝑜𝑙-9.710 -9.113
(-5.41) (-5.12)
𝑇𝑢𝑟𝑛-0.000 -0.000
(-0.01) (-0.08)
𝐼𝑙𝑙𝑖𝑞0.003 0.001
(0.20) (0.08)
𝐶𝑎𝑝𝑥-0.906
(-1.44)
𝑅&𝐷-1.067
(-3.37)
Obs 355,322 261,095 254,798 253,329 252,474
𝑅2 0.069 0.093 0.099 0.106 0.106
Note:This table reports pooled panel regressions of firm-level AI betas on firm characteristics. The dependent variable is the rolling 13-week
AI beta, winsorized at the1st/99th percentiles within each week. Coefficients are multiplied by100.ln𝑀𝐸is log market equity,ln𝐵𝑀is log
book-to-market,𝑀𝑜𝑚is prior52-to-5-week return,𝑃𝑟𝑜𝑓𝑖𝑡is gross profitability,𝐴𝐺is asset growth,𝑅𝑂𝐸is return on equity,𝐿𝑒𝑣is total debt
over total assets,𝐼𝑣𝑜𝑙is idiosyncratic volatility,𝑇𝑢𝑟𝑛is average daily share turnover,𝐼𝑙𝑙𝑖𝑞is Amihud illiquidity,𝐶𝑎𝑝𝑥is capital expenditures
over total assets, and𝑅&𝐷is research and development expense over total assets and is set to zero when missing. All characteristics are
winsorized at the1st/99th percentiles within each week. Panel A includes week fixed effects. Panel B includes week and Fama-French 30
industry fixed effects.𝑡-statistics are reported in parentheses and are based on standard errors clustered by week and firm. Intercepts are
absorbed by the fixed effects.
40

IA.9 Attention-Orthogonalized AI Factor
Table IA.8 shows that the AI premium survives controlling for Google Trends attention in the
first-pass beta regression. This section reports a complementary two-step exercise that instead
strips attention out of the factor itself. Panel A of Table IA.21 regresses the weekly AI factor
on the weekly log growth of Google Trends search interest in “Artificial intelligence.” Attention
comoves with the factor, with a coefficient of 2.419 that is significant at the 10 percent level,
but explains only 2.7 percent of its weekly variance, so the AI factor is largely orthogonal to
broad public attention to AI. Panel B re-estimates the first-pass rolling betas with the regression
residual replacing the raw AI factor and repeats the value-weighted, all-stock-breakpoint quintile
sort. The H−L spread is 58.2 basis points per week, significant at the 1 percent level, and the FF5
and FF5+Mom alphas are 53.3 and 51.1 basis points, close to the 60.4-basis-point baseline. The
premium reflects exposure to the component of AI consumption growth that is orthogonal to public
attention.
Table IA.21: Attention-Orthogonalized AI Factor: Spanning Regression and Portfolio Sorts
Panel A. Spanning regression of the AI factor on Google Trends attention
𝑏gtrend 𝑡 𝑅 2 𝑁
𝐴𝐼𝑡 onΔlngtrend AI 𝑡 2.419 (1.72) 0.027 112
Panel B. Value-weighted quintile portfolios sorted on the residual-factor beta
Low 2 3 4 High H−L
Excess return -0.148 0.216 0.149 0.459 0.435 0.582
𝑡(-0.57) (1.03) (0.75) (2.11) (1.59) (2.82)
FF5𝛼-0.350 0.020 -0.061 0.233 0.183 0.533
𝑡(𝛼)(-2.69) (0.22) (-0.88) (2.59) (1.42) (2.52)
FF5+Mom𝛼-0.334 0.028 -0.062 0.224 0.177 0.511
𝑡(𝛼)(-2.63) (0.31) (-0.90) (2.52) (1.37) (2.45)
Note:This table reports the two-step attention-orthogonalization exercise. Panel A regresses the weekly AI fac-
tor on the weekly log growth in Google Trends search interest for the topicArtificial intelligence:𝐴𝐼 𝑡 =𝑎+
𝑏gtrendΔlngtrend AI 𝑡 +𝑒𝑡. The𝑡-statistic is based on Newey-West standard errors with five lags and is reported in paren-
theses. The residual𝑒 𝑡 is the attention-orthogonalized AI factor. Panel B repeats the baseline portfolio exercise of Ta-
ble 3 with the residual replacing the raw AI factor in the first-pass rolling beta regression:𝑟𝑒 𝑖,𝑡 =𝑎+𝑏 mkt𝑟𝑒 𝑚,𝑡+𝑏 AI,⊥𝑒𝑡,
estimated over rolling13-week windows. Stocks are sorted into pooled quintiles by𝑏 AI,⊥ using all-stock breakpoints,
and portfolios are value-weighted. Returns and alphas are in percent per week. FF5 is the Fama-French five-factor
model and FF5+Mom adds the momentum factor.𝑡-statistics are reported in parentheses.
41

IA.10 The AI Factor and Investment-Specific Technology Risk
This section asks whether the AI factor is the investment-specific technology (IST) shock priced
in Papanikolaou (2011) and Kogan and Papanikolaou (2014), whose estimated price of risk is
negative. Because the IST shock is not directly observable, that literature prices its tradable proxy,
the investment-minus-consumption (IMC) portfolio, which is long investment-good producers and
short consumption-good producers. We build IMC on our sample in three ways. The first uses the
published industry classification of Gomes, Kogan and Yogo (2009), which assigns each industry
to the final-demand category with the largest share of its output in the 1987 benchmark input-
output accounts. The other two rebuild the same classification on the 2012 and 2017 benchmark
accounts. The vintage matters for the industries at the center of our sample. The 1987 accounts
predate the treatment of software as fixed investment, and in that year the largest final-demand
destination of semiconductors, electronic components, and computer and data processing services
was government, reflecting defense electronics and federal computing, so these industries belong to
neither leg and much of the technology sector is absent from the 1987 portfolio, although computer
manufacturing was already an investment good. On the modern accounts software publishers and
computer systems design enter the investment leg, and data processing and hosting enters the
consumption leg on the 2012 accounts and the investment leg on the 2017 accounts, so the modern
portfolios contain the technology firms the AI factor is about. Within each leg we value-weight the
following week’s return by formation-week market equity, matching the convention of the portfolio
tests.
Table IA.22 reports three sets of results. Net of the market, the correlation between the AI fac-
tor and IMC is small and negative in every classification. The cross-sectional correlation between
firms’ AI betas and their IMC betas is close to zero on the 1987 classification and small and neg-
ative on the modern ones. The AI premium is essentially unchanged by controlling for IMC: the
high-minus-low alpha on the five factors, momentum, and IMC ranges from 0.49 to 0.52 percent
per week, against 0.53 with no IMC control. On the 2017 classification the high-minus-low port-
folio does load positively on IMC, so high-AI-beta firms carry some modern investment-specific
exposure, but that exposure does not explain the premium. The AI factor is empirically distinct
from these IMC proxies.
42

Table IA.22: The AI Factor and Investment-Specific Technology Risk
GKY 1987 BEA 2012 BEA 2017
Panel A. Factor-level correlation with IMC
corr(𝐴𝐼𝑡,𝑅 𝐼𝑀𝐶 𝑡 ), net of the market−0.016−0.134−0.138
(−0.17) (−1.44) (−1.49)
Panel B. Cross-section of exposures
corr(𝛽𝐴𝐼 𝑖 ,𝛽 𝐼𝑀𝐶 𝑖 )−0.008−0.123−0.089
(−0.30) (−4.04) (−2.80)
Panel C. Spanning of the AI premium
H−L𝛼(FF5+Mom+IMC) 0.521 0.508 0.494
(2.60) (2.50) (2.56)
𝑏𝐼𝑀𝐶 0.045 0.094 0.280
(0.33) (0.66) (2.22)
Note:The table asks whether the AI factor is the investment-specific technology shock of Papanikolaou (2011) and
Kogan and Papanikolaou (2014) by comparing it with the investment-minus-consumption (IMC) portfolio that mimics
that shock. Columns differ in the industry classification defining the legs: the published Gomes, Kogan and Yogo
(2009) classification based on the 1987 benchmark input-output accounts, and the same algorithm applied to the 2012
and 2017 benchmark accounts, in which investment is private fixed investment excluding inventories and net exports
are exports less imports. IMC is the value-weighted return of investment-good producers minus consumption-good
producers, weighting the following week’s return by formation-week market equity. The legs hold 658 and 1,491
firms (1987), 553 and 2,968 (2012), and 765 and 2,822 (2017), and IMC correlates−0.24to−0.43with HML, as
an investment portfolio should. Panel A reports the weekly correlation of the AI factor with the IMC return after
residualizing the AI factor on the market. Panel B reports the mean weekly cross-sectional correlation between firm-
level AI betas and IMC betas, both estimated from 13-week rolling regressions with at least 9 non-missing weeks.
Panel C reports the intercept and IMC loading from regressing the value-weighted, all-stock-breakpoint H−L return
on IMC, the Fama and French (2015) factors, and momentum (Carhart, 1997), with Newey-West standard errors with
five lags. Returns and alphas are in percent per week.𝑡-statistics in parentheses. AI consumption data is weekly from
January 2024 through April 2026. The equity sample covers 108 formation weeks from March 2024 through March
2026.
IA.11 Variable Definitions
Table IA.23 reports the definitions of the variables used in the analysis and their correspondence
in the OpenRouter dataset and the additional datasets and sources used in the paper.
Table IA.23: Variable Definitions
Name Definition Dataset used
AI consumption and attention variables
𝑇𝑜𝑘𝑡 Total OpenRouter prompt plus completion tokens in week
𝑡.
OpenRouter
𝐷𝑜𝑙𝑡 Total dollar-denominated OpenRouter usage in week𝑡. OpenRouter
𝑈𝑠𝑒𝑟𝑡 Distinct active OpenRouter users in week𝑡. OpenRouter
43

Name Definition Dataset used
Δln𝑇𝑜𝑘 𝑡 Weekly log growth in total OpenRouter tokens. OpenRouter
Δln𝐷𝑜𝑙 𝑡 Weekly log growth in OpenRouter usage dollars. OpenRouter
Δln𝑈𝑠𝑒𝑟 𝑡 Weekly log growth in distinct active OpenRouter users. OpenRouter
𝐴𝐼𝑡 First principal component ofΔln𝑇𝑜𝑘 𝑡,Δln𝐷𝑜𝑙 𝑡, and
Δln𝑈𝑠𝑒𝑟 𝑡.
OpenRouter
𝐴𝐼𝐶𝑙𝑜𝑠𝑒𝑑 𝑡 ,𝐴𝐼 𝑂𝑝𝑒𝑛 𝑡 AI factors constructed separately from closed-weight and
open-weight model consumption.
OpenRouter; model cata-
log
𝐴𝐼𝐶𝑜𝑟𝑒 𝑡 ,𝐴𝐼 𝑁𝑒𝑤 𝑡 AI factors constructed separately from paid/core-user and
new-user consumption.
OpenRouter account data
𝐴𝐼𝑁𝑜𝑛𝑐𝑜𝑟𝑒 𝑡 AI factor constructed from non-paid/core account con-
sumption, the complement of paid/core account consump-
tion.
OpenRouter account data
𝐴𝐼𝑆𝑒𝑎𝑠𝑜𝑛𝑒𝑑 𝑡 ,
𝐴𝐼𝑁𝑜𝑛𝑠𝑒𝑎𝑠𝑜𝑛𝑒𝑑 𝑡
AI factors constructed separately from seasoned-user and
non-seasoned-user consumption.
OpenRouter account data
Δln𝑇𝑜𝑘 𝐿𝑜𝑛𝑔 𝑡 ,
Δln𝑇𝑜𝑘 𝑆ℎ𝑜𝑟𝑡 𝑡
Weekly token-growth series for long prompts and short
prompts, split by the rolling prompt-length cutoff.
OpenRouter row-level us-
age
𝑆ℎ𝑎𝑟𝑒𝑐𝑎𝑡 𝑐,𝑡 Share of categorized tokens assigned to prompt category
𝑐in week𝑡.
OpenRouter category-
token file
𝑆ℎ𝑎𝑟𝑒𝐶𝑙𝑜𝑠𝑒𝑑 𝑡 ,
𝑆ℎ𝑎𝑟𝑒𝐶𝑜𝑟𝑒 𝑡 ,
𝑆ℎ𝑎𝑟𝑒𝑆𝑒𝑎𝑠𝑜𝑛𝑒𝑑 𝑡 ,
𝑆ℎ𝑎𝑟𝑒 𝐿𝑜𝑛𝑔 𝑡
Weekly usage shares for closed-weight models, paid/core
users, seasoned users, and long prompts.
OpenRouter; model cata-
log; account data
Δlngtrend 𝐴𝐼 𝑡 Weekly log growth in Google Trends interest for the topic
“Artificial intelligence.”
Google Trends
Return, exposure, and control variables
𝑟𝑒 𝑖,𝑡 Weekly log excess return of stock𝑖over the risk-free rate. CRSP; Fama-French
𝑟𝑒 𝑚,𝑡 or𝑟𝑚 𝑡 Weekly log excess market return. Fama-French
𝛽𝑟𝑚 𝑖,𝑡 Rolling market beta of stock𝑖from the first-pass return
regression.
CRSP; Fama-French
𝛽𝐴𝐼 𝑖,𝑡 Rolling AI exposure of stock𝑖: coefficient on the AI factor
in a 13-week regression of𝑟 𝑒 𝑖,𝑡 on𝑟 𝑒 𝑚,𝑡 and𝐴𝐼 𝑡.
CRSP; OpenRouter;
Fama-French
𝛽𝑇𝑜𝑘 𝑖,𝑡 Rolling exposure of stock𝑖toΔln𝑇𝑜𝑘 𝑡. CRSP; OpenRouter;
Fama-French
𝛽𝐷𝑜𝑙 𝑖,𝑡 Rolling exposure of stock𝑖toΔln𝐷𝑜𝑙 𝑡. CRSP; OpenRouter;
Fama-French
𝛽𝑈𝑠𝑒𝑟 𝑖,𝑡 Rolling exposure of stock𝑖toΔln𝑈𝑠𝑒𝑟 𝑡. CRSP; OpenRouter;
Fama-French
𝛽𝐴𝐼,𝐼𝑛𝑑 𝑖,𝑡 AI beta minus the same-week median AI beta of stock𝑖’s
Fama-French 30 industry.
CRSP; Compustat; Open-
Router; Fama-French
𝑟𝑒 HiTec,𝑡 Fama-French HiTec industry excess return used as a first-
pass control.
Fama-French
𝑟semi,𝑡 Weekly log return of the U.S. semiconductor industry
used as a first-pass control.
CRSP; Compustat
𝛽𝐴𝐼,𝐶𝑙𝑜𝑠𝑒𝑑 𝑖,𝑡 ,𝛽 𝐴𝐼,𝑂𝑝𝑒𝑛 𝑖,𝑡 Rolling exposures of stock𝑖to𝐴𝐼 𝐶𝑙𝑜𝑠𝑒𝑑 𝑡 and𝐴𝐼 𝑂𝑝𝑒𝑛 𝑡 . CRSP; OpenRouter; model
catalog
44

Name Definition Dataset used
𝛽𝐴𝐼,𝐶𝑜𝑟𝑒 𝑖,𝑡 ,𝛽 𝐴𝐼,𝑁𝑒𝑤 𝑖,𝑡 Rolling exposures of stock𝑖to𝐴𝐼 𝐶𝑜𝑟𝑒 𝑡 and𝐴𝐼 𝑁𝑒𝑤 𝑡 . CRSP; OpenRouter ac-
count data
𝛽𝐴𝐼,𝑆𝑒𝑎𝑠𝑜𝑛𝑒𝑑 𝑖,𝑡 ,
𝛽𝐴𝐼,𝑁𝑜𝑛𝑠𝑒𝑎𝑠𝑜𝑛𝑒𝑑 𝑖,𝑡
Rolling exposures of stock𝑖to𝐴𝐼 𝑆𝑒𝑎𝑠𝑜𝑛𝑒𝑑 𝑡 and
𝐴𝐼𝑁𝑜𝑛𝑠𝑒𝑎𝑠𝑜𝑛𝑒𝑑 𝑡 .
CRSP; OpenRouter ac-
count data
𝛽𝑇𝑜𝑘,𝐿𝑜𝑛𝑔 𝑖,𝑡 ,𝛽 𝑇𝑜𝑘,𝑆ℎ𝑜𝑟𝑡 𝑖,𝑡 Rolling exposures of stock𝑖toΔln𝑇𝑜𝑘 𝐿𝑜𝑛𝑔 𝑡 and
Δln𝑇𝑜𝑘 𝑆ℎ𝑜𝑟𝑡 𝑡 .
CRSP; OpenRouter row-
level usage
ln𝑀𝐸 𝑖,𝑡 Natural log of stock𝑖’s formation-week market equity. CRSP; Compustat
ln𝐵𝑀𝑖,𝑡 Natural log of stock𝑖’s book-to-market equity. Compustat; CRSP
𝑃𝑟𝑜𝑓𝑖𝑡 𝑖,𝑡 Gross profitability, revenue minus cost of goods sold
scaled by assets.
Compustat
𝐼𝑛𝑣𝑖,𝑡 Asset growth, measured as the year-over-year change in
total assets scaled by lagged assets.
Compustat
𝑀𝑜𝑚𝑖,𝑡 Prior stock return from week𝑡−52through week𝑡−5. CRSP
𝑅𝑒𝑣𝑖,𝑡 Prior one-month stock return used as a short-term reversal
control.
CRSP
𝐿𝑒𝑣𝑖,𝑡 Long-term debt scaled by assets. Compustat
𝐴𝑐𝑐𝑟𝑖,𝑡 Accruals. Compustat
International and event-study variables
𝑟𝑙𝑜𝑐𝑎𝑙 𝑖,𝑡 Weekly local-currency return of non-U.S. stock𝑖. Compustat Global
𝑟𝑙𝑜𝑐𝑎𝑙 𝑚,𝑡 Weekly regional local-market return. Compustat Global; market
returns
𝐴𝐼𝐶ℎ𝑖𝑛𝑎 𝑡 AI factor constructed from OpenRouter usage originating
from mainland China.
OpenRouter country-
coded usage
𝑟𝐶ℎ𝑖𝑛𝑎 𝑚,𝑡 Weekly Datastream China A-share market log excess re-
turn.
Datastream; Fama-French
𝑟𝐴𝐼𝐸𝑇𝐹 𝑡 Weekly excess return on the AI and robotics ETF basket
used as a first-pass and spanning control.
ETF return data; Fama-
French
𝐶𝐴𝑅𝑒,[𝑎,𝑏] Cumulative abnormal H-minus-Low return for event𝑒
over trading-day window[𝑎,𝑏].
CRSP; Fama-French; re-
lease calendar
𝐶𝐴𝐴𝑅[𝑎,𝑏] Cross-event average of𝐶𝐴𝑅 𝑒,[𝑎,𝑏] over the specified
event window.
Constructed
Note:The table defines the variables used in the analysis and identifies the dataset used for each.
45
