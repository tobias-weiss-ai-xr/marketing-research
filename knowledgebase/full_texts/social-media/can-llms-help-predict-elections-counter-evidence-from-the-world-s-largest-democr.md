---
title: Can LLMs Help Predict Elections? (Counter)Evidence from the World's Largest Democracy
url: https://arxiv.org/abs/2405.07828
category: social-media
subcategory: empirical
date: 2024-05
venue: ''
authors:
- Pratik Gujral
- Kshitij Awaldhi
- Navya Jain
- Bhavuk Bhandula
- Abhijnan Chakraborty
source: arxiv
pdf_url: https://arxiv.org/pdf/2405.07828
pages: 8
chars: 40133
fetched_at: '2026-11-08T13:06:11+00:00'
kb_version: 1
---

# Can LLMs Help Predict Elections? (Counter)Evidence from the World's Largest Democracy

Can LLMs Help Predict Elections? (Counter)
Evidence from the World’s Largest Democracy
Pratik Gujral ∗, Kshitij Awaldhi ∗, Navya Jain ∗, Bhavuk Bhandula ∗ and Abhijnan Chakraborty †
∗Indian Institute of Technology Delhi, India
†Indian Institute of Technology Kharagpur, India
Abstract—The study of how social media affects the formation
of public opinion and its influence on political results has
been a popular field of inquiry. However, current approaches
frequently offer a limited comprehension of the complex political
phenomena, yielding inconsistent outcomes. In this work, we
introduce a new method: harnessing the capabilities of Large
Language Models (LLMs) to examine social media data and
forecast election outcomes. Our research diverges from tradi-
tional methodologies in two crucial respects. First, we utilize
the sophisticated capabilities of foundational LLMs, which can
comprehend the complex linguistic subtleties and contextual
details present in social media data. Second, we focus on data
from X (Twitter) in India to predict state assembly election
outcomes. Our method entails sentiment analysis of election-
related tweets through LLMs to forecast the actual election
results, and we demonstrate the superiority of our LLM-based
method against more traditional exit and opinion polls. Overall,
our research offers valuable insights into the unique dynamics
of Indian politics and the remarkable impact of social media in
molding public attitudes within this context.
Index Terms—Large Language Models, Social Media Analysis,
Sentiment Analysis, Election Prediction, Politics, X (Twitter).
I. I NTRODUCTION
Elections play a pivotal role in democracies, serving as
the expression of collective public will, and the means for
peaceful transition of power. Multiple research works have
linked political stability with economic prosperity, as institu-
tions and governance structures greatly influence a nation’s
economic well-being [1]. Selecting the right government can
foster enduring economic growth and development, impacting
resource allocation, and citizen welfare [2]. On the other
hand, political uncertainty stemming from unclear election
outcomes can deter capital investment, thereby hindering eco-
nomic development [3]. Thus, the stability and predictability
of political environments, particularly during election cycles,
are vital for attracting business investments and promoting
economic progress [4]. Consequently, the need to forecast
election results arises from the stakeholders’ need to make
well-informed choices. Businesses, investors, and politicians
depend on election forecasts to predict policy shifts, evaluate
market conditions, and manage risks [5]. Understanding po-
tential election outcomes allows citizens to prepare for policy
changes and potentially mobilize around issues they care about
[6]. Opinion polls, exit surveys and, more lately, social media
studies try to fill this need by predicting election results.
Social media sites like X (Twitter) allow people to voice
their political opinions, and traditionally X’s potential as a
rich source of real-time, large-scale, and publicly available
data for studying political behavior and sentiment has led to
its growing use for election prediction. Prior works [7], [8]
have demonstrated the ability of social media to anticipate
election outcomes accurately. Researchers have utilized tweet
content, network architecture, and multi-modal signals to
forecast election outcomes in several nations. Methods such as
sentiment categorization, count-based techniques, and machine
learning models such as V ADER and BERT have played a
crucial role in making these predictions [9], [10].
Although social media shows potential in forecasting elec-
tion results, there are divergent opinions on its efficacy. Several
studies indicate that social media might offer helpful infor-
mation on public opinion and political trends [11]. However,
opposing views suggest that social media cannot accurately
represent the complete range of voter behavior and can be
impacted by biases and false information [12], in addition to
other challenges. To begin with, currently popular approaches
often lack understanding of the general world. Additionally,
the sentiment analysis methods frequently rely solely on
keyword presence to identify the referenced political party.
They assign a single sentiment score to an entire tweet.
However, tweets often contain references to multiple parties
within a single tweet. In cases where a tweet expresses positive
sentiment towards one party and negative sentiment towards
another, current methods fail to disambiguate the references to
different parties within the text, due to the presence of mixed
polarity within the sentences. This can lead the classifiers to
generate a neutral score despite the presence of both positive
and negative sentiment towards different political actors.
In recent times, Large language models (LLMs) have
demonstrated an extraordinary ability to fathom enormous
amount of world knowledge [13], [14]. The basic principle
underlying the GPT models is to compress the world knowl-
edge into the decoder-only Transformer model by language
modeling, such that it can recover (or memorize) the semantics
of world knowledge and serve as a general-purpose task solver
[15]. In this paper, we investigate whether LLMs can navigate
the challenges with social media data, as mentioned earlier,
and be used for predicting election outcomes without any fine-
tuning in a zero-shot fashion.
We specifically take the 2022 state assembly elections in
India (Punjab and Uttar Pradesh) as the use case. We collected
extensive longitudinal data from X alongside the opinion poll
and exit poll results released by several psephology companies.
arXiv:2405.07828v1  [cs.SI]  13 May 2024

Our experiments with two open source LLMs (Llama 2 and
Zephyr) show that, compared to more traditional opinion polls
and exit polls, LLM-based predictions can come much closer
to the actual election outcomes. Overall, to our knowledge,
ours is the first attempt to apply LLM for predicting elec-
tion outcome and can offer a new perspective in this ever-
expanding research domain.
II. L ITERATURE REVIEW
One of the earliest studies in this domain was conducted
by [8], who analyzed tweets related to the 2009 German
federal election. They discovered that the volume of tweets
mentioning a political party could serve as a plausible reflec-
tion of the vote share, with a predictive power comparable to
traditional election polls. This approach was further refined by
[16] through incorporating sentiment detection, which led to
replicating consumer confidence and presidential job approval
polls using data from X. Following these pioneering studies,
researchers worldwide adopted the volume of tweets combined
with automatic sentiment detection as the primary method for
predicting election results. For instance, studies have been
conducted in the Netherlands [17], France [18], and the USA
[19], [20]. Additionally, novel approaches such as regression
or time series methods [16], [21] and models using traditional
polls for training or comparing results [22] were introduced.
In an attempt to enhance the predictive power of social
media data, researchers have also explored the use of advanced
machine learning algorithms. For instance, [23] developed
the ElecBERT model, which leverages sentiment analysis of
election-related tweets to predict electoral outcomes with high
accuracy. Similarly, [24] employed sentiment analysis methods
to analyze X data during the 2019 Indian election, reportedly
achieving predictions that closely mirrored the actual results.
Beyond sentiment analysis, multimodal approaches have been
proposed to integrate various data types for election prediction.
[25] presented a novel method that combined social multime-
dia data with a CNN-based visual sentiment analysis model
to predict US election outcomes. [26] introduced an attention-
based model that performs image-text sentiment analysis,
further expanding the scope of data types used for election
prediction. The role of geographic information in election
prediction has also been investigated. [27] proposed a location-
based model integrating state-level sentiment analysis, offering
a more granular approach to understanding regional political
dynamics. Both [28] and [29] assessed location-weighted
counting methods in the context of the 2018 Turkish election,
emphasizing the importance of spatial factors in electoral
analysis. Additional techniques such as event analysis, social
network analysis, and heterogeneous information diffusion
have been employed to enhance the accuracy of election
predictions [30]–[32]. The computational complexity of these
predictive models has been examined by [33], who investigated
the trade-offs between model complexity and predictive power.
Comprehensive surveys [34], [35] have provided valuable
overviews of the field, identifying current trends and future
research opportunities. In conclusion, the use of social media
data, particularly from X, has emerged as a powerful tool
for predicting election results. Researchers have significantly
enhanced the accuracy of election predictions by incorporating
sentiment analysis, multimodal approaches, geographic infor-
mation, and advanced machine learning algorithms. However,
challenges related to data collection, model complexity, and
computational resources remain, offering opportunities for
further research in this rapidly evolving field.
III. B ACKGROUND ON THE 2022 P UNJAB AND UP
ASSEMBLY ELECTIONS
India, known for its vibrant democracy, conducts elections
every 5 years at various levels of government, including the
legislative assembly elections held in its states and union
territories. The most distinguishing feature of Indian elections
is the diversity of its electorate, which encompasses people
from several cultural, linguistic, and socio-economic back-
grounds. As per the statistical reports released by the Election
Commission of India [36], In 2022, Punjab, with a population
of over 30 million, saw a very competitive election in which
elections were contested in 117 constituencies. During the
2022 legislative assembly election, the state recorded 22.9
million eligible voters, comprising 11.6 million males and
11.3 million females. Notably, around 45% of voters belonged
to the 18-35 age group, highlighting the significant youth
demographic in Punjab’s electorate [36]. The election saw a
diverse range of political parties participating, including the
Indian National Congress (INC), Shiromani Akali Dal (SAD),
and Aam Aadmi Party (AAP). The electoral contest in Punjab
was marked by a robust candidate count, with hundreds of
individuals vying for seats across the state. Uttar Pradesh
(UP), India’s most populous state with over 240 million
people, featured a complex electoral landscape in the 2022
elections, with 403 constituencies. During the 2022 legislative
assembly election, the state recorded 134.6 million eligible
voters, comprising 70.4 million males and 64.2 million females
[36]. UP’s electorate displayed a broad demographic mix,
reflecting the state’s diverse social fabric. The electoral fray
in UP was characterized by a multitude of political parties,
including the Bharatiya Janata Party (BJP), Samajwadi Party
(SP), Bahujan Samaj Party (BSP), and Congress. The state
witnessed a significant number of candidates vying for seats,
underlining the intense competition and strategic significance
of Uttar Pradesh in the political landscape of India. The diverse
demographics, constituency distribution, and political party
participation in these states underscored the complexities of
India’s democratic process.
IV. M ETHODOLOGY
A. Dataset collection
1) Tweets: We collected tweets through the official X
(formerly Twitter) API. To ensure the relevancy of the dataset
and to capture the recent public sentiment, we collected tweets
between February 1, 2022, and March 8, 2022, right before
and during the elections, using search terms, hashtags, and user
mentions. Table I lists the search queries used for collecting

TABLE I
SEARCH TERMS , HASHTAGS , AND USER MENTIONS USED TO EXTRACT DATA FROM X
Party Search queries
BJP BJP, @BJP4India, @narendramodi, #BJPwinningUP, @AmitShah, @myogiadityanath, yogi, @JPNadda, @BJP4TamilNadu, @BJP4UP,
#PunjabwelcomesModiji, #Modigoback
INC @INCIndia, @RahulGandhi, Rahul Gandhi, @INCPunjab, channi, @priyankagandhi, #111CongressDubara, @CHARANJITCHANNI,
@INCUttarPradesh
AAP aam aadmi party, #AAP, kejriwal, @AAPPunjab, @ArvindKejriwal, @AamAadmiParty, #LokandaCM, #ArvindKejriwal, #Kejri-
walVsAll, @msisodia, #AAPdePaap, @BhagwantMann
SAD @AkaliDal A, @Officeofbadal, @MSBADAL, @HarsimratBadal, @officialY AD, @bsmajithia, SGPC, Shiromani akali dal
BSP @Mayawati,@BSPIndia, bahujan samaj, mayawati, @AnandAkash BSP, @satishmisrabsp
SP @yadavakhilesh, samajwadi, @samajwadiparty, shivpal Yadav, #MulayamSinghYadav
General #PunjabElections2022, #UPElections2022, #UttarPradeshElections2022
data. Extracting data using these search terms, we collected
403,917 tweets,
2) Opinion Polls and Exit Polls: Opinion polls and exit
polls are conducted by various media houses prior to the elec-
tions to gauge public sentiment and try to predict the outcome
of the elections. They publish these results on their websites
and broadcast them during newsroom hours as debates. Both
opinion polls and exit poll survey results for the election
conducted by various reputed media houses as pollsters were
curated and published by Oneindia on their website for Punjab
[37] and Uttar Pradesh (UP) [38], which we directly used in
our analysis.
Ethical Considerations The data in this work has been
collected only using Twitter API, respecting X’s terms of
service. We exclusively collected the publicly available data,
followed well-established ethical procedures for social data,
and obtained approval from the ethics committee at the first
author’s institution.
B. Data Preparation
1) Tweets Dataset: In order to make full use of the lan-
guage comprehension skills of the Large Language Models
(LLMs), we deliberately refrained from carrying out any
preprocessing on the tweets dataset, except for eliminating
duplicate tweets. We dropped duplicate records on the com-
bination of (“ID”, “created at”, “username”, and “tweet”)
columns. The final dataset, after the completion of cleanup
operations, consisted of 241,301 tweets.
2) Opinion and Exit Polls: As various pollsters released
a predicted range of values for every party in their survey
results, for every pollster, we computed the median value of
the range predicted by them for a party and converted them
to percentage share.
C. Identify sentiment using LLM
After data collection and cleanup, the next task was identi-
fying which parties and states were referred to in a tweet and
the associated sentiment score for each reference. We used
two large language models- Zephyr-7B- β [39] and Llama-2-
13B [40]. We chose these models because they are open, their
inference can run on a low-cost consumer GPU, and at the
time of experimentation, their output was known to be more
accurate and coherent than other 7B and 13B parameter open
foundation models.
The prompt given to Llama-2 was:
<s>[INST]<<SYS>>
You are an expert political analyst specializing in political
social media posts. Use all your knowledge from the Indian
political landscape. Your task is to identify which Indian
political party and state is being talked about in the following
Tweet. Also, what is the sentiment score expressed in that
reference of party and state? The hashtags, mentions, and
names of people used in Tweet can help you identify the
party and state. Your answer should be a JSON with three
keys- party, state, and sentiment score. You have to choose
only one among the following parties– Bhartiya Janta Party
(BJP), Congress (INC), Aam Aadmi Party (AAP), Shiromani
Akali Dal (SAD), Samajwadi Party (SP), Bahujan Samaj Party
(BSP). The state can be either Uttar Pradesh (UP) or Punjab.
Sentiment scores can range between -1 (very negative) to +1
(very positive). Reply with only the JSON containing state,
party, and sentiment score. Do not write anything other than
that. Do not explain your answer.
<</SYS>>
### Instruction: Identify the party, state and sentiment score in
the Tweet. Reply with only JSON. Here is the Tweet: {tweet}
###Response: [/INST]
The same tweets were processed through Zephyr as well,
using the following prompt:
<|system|>
You are an expert political analyst specializing in political
social media posts. Use all your knowledge from the Indian
political landscape. </s>
<|user|>
You are an expert Indian political analyst. You are given a
tweet. The tweet may be in English, Hindi, Punjabi, or mixed
code. It may directly or indirectly refer to one or more political
parties. Your task is to identify which Indian political parties
and states are being talked about in that Tweet, along with
the sentiment score associated with that party. The hashtags,

Fig. 1. Absolute error/deviation of the predicted vote shares using LLMs and opinion polls and exit polls from the actual vote shares
Fig. 2. Predicted vote shares from using different mapping methods individually vs. PoLLMster (Zephyr7B- β) vs. the actual vote share for Punjab
mentions, and names of people used in Tweet, along with all
the knowledge you have about Indian elections, will provide
you enough context to identify the party and the state. A Tweet
may refer to more than one party.
Your answer should be a JSON array, each object containing
three keys- party name, state, and sentiment score. If a tweet
talks about more than one party, then your response should
contain the party name, sentiment score, and state for each
of the identified parties. You need to adhere to the following
constraints– For the party, only the following values are
allowed-“Bhartiya Janta Party (BJP)”, “Congress (INC)”,
“Aam Aadmi Party (AAP)”, “Shiromani Akali Dal (SAD)”,
“Samajwadi Party (SP)”, “Bahujan Samaj Party (BSP)”.
Allowed values for the State are- “Uttar Pradesh (UP)”
and “Punjab”. Sentiment score can range between -1 (very
negative) to 1 (very positive).
Reply with only the valid JSON containing state, party, and
sentiment score. Do not write anything other than JSON. Do
not explain your answer. Your output should be in the for-
mat: [{“party”: “<party name>”, “state”:“<state name>”,
“sentiment score”:<sentiment score>}].
Here is the Tweet: “ {tweet}”
</s><|assistant|>
D. Post-processing
While we had used an LLM output format enforcer to
compel the output as JSON, at the time of experimentation,
the format enforcers were not 100% effective, as in many
cases, LLM has output additional text such as a context in
the beginning or an explanation of its answer towards the
end of its response. Hence, cleaning up the LLM outputs to
remove any redundant data it had produced was imperative. We
implemented a three-step process for extracting the relevant
information.
1) If the output of LLM was valid JSON, we parsed the
state, party, and sentiment scores.
2) If the raw output of LLM was not a valid JSON, we used
regular expressions to extract only the JSON component
from the LLM output. We tried parsing it to extract the
state, party, and the associated sentiment score.
3) If the regular expression patterns used in the previous
step produced no matches, we attempted to extract the
tokens that immediately followed “state”, “party”, and
“sentiment score” in the LLM output to extract the state,
party, and sentiment score, respectively.
We observed that the outputs obtained from the LLM had
multiple aliases for the same state and party. For example,

for different tweets mapped to the state of Uttar Pradesh, the
LLM output the state as “Uttar Pradesh”, “UP,” and “Uttar
Pradesh (UP)” and at times also returned the names of cities
in the state instead of the name of the state itself, such
as Jaunpur, Amethi, and Varanasi. To fix this problem, we
identified the aliases representing 99.9% of the records through
cumulative distribution tables and mapped them to a single
name. Similarly, we repeated the same process to map various
aliases of the same party to a distinct party name.
E. Mapping sentiment scores to vote shares
After computing the sentiment score for each instance of
party and state detected in a Tweet, the resulting data were con-
solidated to determine the final vote share for the competing
parties in the two states. Numerous previous studies, including
[8], used the volume of tweets made for a party as a proxy
for their vote share. However, sentimentality in the tweets
should also be taken into account. While certain tweets express
favorable sentiments towards a particular political party, others
are critical in nature and are composed of supporters of that
party critiquing an opposing party. The sentiment expressed
in tweets can reflect the prevailing mood of the electorate,
potentially influencing the degree of incumbency or anti-
incumbency towards a political party; that is, in addition to the
sentiment expressed in tweets favoring a party, the sentiment
score of tweets criticizing the competitor or opposing parties
should also have a direct bearing on the vote share of a given
political party. Consequently, we used five different functions
in Eqn. 1 to compute vote share from the sentiment scores for
all parties in the two states of UP and Punjab using the two
models- Llama-2-13B and Zephyr-7B- β.
V SP M p = P MpP
i P Mi
V SN M p =
P
i′̸=i N Mi′
P
i N Mi
V SP V p = P VpP
i P Vi
V SN V p =
P
i′̸=i N Vi′
P
i N Vi
V ST V p = T VpP
i T Vi
(1)
where,
V Sp: V ote share for party p
P M: Sum of the magnitude of positive sentiment scores
N M: Sum of the magnitude of negative sentiment scores of
other parties
P V: V olume of tweet references with a positive sentiment
N V: V olume of tweet references with a negative sentiment
for other parties
T V: Total references of a party in tweets by volume
The vote shares obtained using these mapping methods are
listed in Table ??. We then computed PoLLMster vote share–
the final predicted vote share, as the linear average of the vote
shares obtained by the five mapping methods from Eqn. 1, as
shown in Eqn. 2.
PoLLMster vote share VS(p):
V S(p) =1 5
5X
i=1
V Si p (2)
V. E XPERIMENTAL EVALUATION
We tested our methodology to predict the vote share of all
the parties contesting in Punjab and Uttar Pradesh (UP). The
final vote share computed using our methodology is available
in table II. As our Tweets dataset was limited to a few days
just before the poll, it is more logical to compare the LLM-
predicted results with the opinion polls results than comparing
it with the exit poll results as the latter is conducted after
the polls, and so is expected to be more accurate. However,
our method of using LLMs to forecast the election results
outperforms both- opinion and exit poll results for most states
and parties, closely matching the actuals.
A. Vote share mapping methods
An analysis revealed that the sentiment-to-vote-share map-
ping methodologies produced inconsistent outcomes when
applied in isolation to predict the vote share. Fig. 2 compares
the predicted vote shares obtained for Punjab using different
mapping methods in isolation vs. PoLLMster. We obtained
similar results using Llama in Punjab and UP, which are not
included here for brevity. In general, it was found that mapping
methods based on the positive sentiment tweets- V SP V p and
V SP M p performed better than those based on the negative
sentiment tweets- V SN V p and V SN M p . However, this was not
always true. For instance, in Fig. 2, for the AAP and the BJP,
predictions from V SP V p and V SP M p were closer to the actual
as compared to the ones from V SN V p and V SpN M. On the
contrary, the INC’s vote share predicted from V SN V p (23%)
was better than the vote share predicted from V SP V p (25%) as
the actual vote share was 23%. However, combining the vote
share mapping methods by 2 evens the differences and results
in the final predicted vote share close to the actual. By taking
an average of the vote shares predicted from the five mapping
methods, it can be observed that the PoLLMster vote share
is consistently close to the actual vote share across parties
in both states compared to using each method individually,
irrespective of the LLM used. The final predicted vote share
results using Llama-2 and Zephyr are available in Table II. As
observed in Fig. 1, the error in predicting the vote share using
the two LLMs is similar to that forecasted by pollsters in their
opinion and exit polls survey reports.
B. Stability of the results
While Llama-2 and Zephyr predicted the winning parties in
both states accurately, it can be argued that the vote shares
obtained from Llama-2 and Zephyr vary slightly, as seen in
table II. The difference among the vote shares predicted by
the two models was highest for SAD in Punjab at 9%, with
the average deviation being 5%. While there is a difference
in the vote shares predicted by the two models, the deviation
is much lower than that of the opinion and exit poll-predicted
results. The percentage share of each party from the opinion
and exit polls, calculated in section IV-B2, is shown for Punjab
and Uttar Pradesh in Fig. 3 and Fig. 4 respectively. It can be
observed that the survey results can vary significantly among
different pollsters. For instance, in Fig. 4, it can be seen that

TABLE II
VOTE SHARES — PREDICTED VS . ACTUAL .
State Party LLM Predicted Vote Share Predicted through surveys Actual Vote Share
Llama-2 Zephyr Opinion Poll Exit Poll
Punjab AAP 42% 44% 45% 57% 42%
Punjab BJP 8% 11% 2% 3% 7%
Punjab INC 18% 22% 38% 24% 23%
Punjab SAD 32% 23% 15% 16% 18%
UP INC 21% 16% 2% 1% 2%
UP BJP 52% 59% 59% 61% 41%
UP AAP 8% 4% 1% 0% 0%
UP SP 9% 15% 34% 34% 32%
UP BSP 8% 4% 3% 3% 13%
UP AIMIM 2% 1% 1% 0% 0%
Opinion Polls Exit Polls
Fig. 3. Punjab - Exit and opinion polls from various pollsters
while DB Live forecasted that the Samajwadi Party (SP) would
secure 53% share, Republic TV’s forecast for the party stood
at a paltry 16%. similarly, in Punjab, while News24 and India
Today forecasted a whooping 85% and 69% share for the Aam
Aadmi Party (AAP), India TV and DB Live predicted the party
would secure a mere 27% and 24%, respectively. To conclude,
although the two models forecast different vote shares, the
difference is far smaller than the variation observed in the
opinion and exit poll predictions.
VI. C ONCLUSION AND DISCUSSION
The objective of this study was to forecast the results of
the 2022 assembly elections in Punjab and Uttar Pradesh
by employing computational social science techniques. Our
approach used sophisticated natural language processing tech-
niques with extensive linguistic models (LLMs) to examine
the sentiment associated with political parties and candidates
in X tweets. The results of our study show a strong link
between the emotion ratings obtained from LLM outputs
and the actual election outcomes. The sentiment research
in Punjab successfully forecasted the triumph of the Aam
Aadmi Party (AAP), as evidenced by their overwhelming
majority. Similarly, in Uttar Pradesh, the sentiment ratings
aligned with the Bharatiya Janata Party’s (BJP) successful
re-election, demonstrating the effectiveness of our prediction
methodology. The analysis of these findings emphasizes the
capacity of LLMs to comprehend and predict voter conduct.
The precision of our forecasts highlights the significance
of computational techniques in political science, especially
in examining extensive social media data to assess popular
sentiment.
A. Current limitations, biases and ethical concerns
Several inherent challenges impact the precision of the
predictions presented earlier. The low internet penetration rate
in India, coupled with the diverse demographic and linguistic
landscape, especially in Uttar Pradesh, limits the representa-
tiveness of X data. The demographic and linguistic diversity of
the population further complicates the data collection process,
as the sentiments expressed on X may not accurately mirror
the electorate’s views. The incumbency advantage often results
in a skewed perception of performance and increased voter
support, potentially influencing the election outcome. Addi-
tionally, the propensity of X users to express political opinions
does not necessarily reflect the broader voting population. This
bias in data can lead to skewed results, as LLMs are known

Opinion Polls Exit Polls
Fig. 4. Uttar Pradesh - Exit and opinion polls from various pollsters
to learn, perpetuate, and amplify harmful social biases if not
properly mitigated [41]. When applied to election prediction,
large language models (LLMs) raise ethical concerns due to
the possibility of manipulation and bias. These biases may
originate from the data utilized in the training of LLMs, which
could be influenced by societal prejudices or distorted by
particular online communities. Consequently, LLM forecasts
may exhibit a bias towards particular candidates or deter
engagement from specific demographic groups, thereby sub-
verting the integrity of the democratic process.
B. Future work
Despite already performing at par or better than the opinion
and exit poll results, our results can be further enhanced in
several ways, including using a more extensive dataset, better
models, and prompt engineering. Increasing the volume of
tweets collected could provide a more comprehensive dataset,
reflecting a wider range of political sentiments. Employing
more advanced proprietary models, such as GPT-4, Claude-3
and Gemini-Pro, may yield superior results due to their en-
hanced processing capabilities and understanding of nuanced
language, as they currently top several LLM Leaderboards
such as [42]. Furthermore, leveraging prompt engineering
techniques and optimizing prompts could lead to more precise
sentiment extraction and party identification. Being an active
area of research, several works present varying techniques,
including but not limited to exploiting patterns in prompts,
automated prompt generation, chain-of-thought reasoning, and
zero-shot reasoning, to make the model responses more accu-
rate, free from any biases, and harmless [43], [44]. It is crucial
to acknowledge that while LLMs can exhibit cognitive biases,
there is cautious optimism about their performance, provided
genuine biases are identified and efforts are made to reduce
them [45].
In conclusion, while the current methodology may have
limitations, it establishes a solid foundation for future ex-
ploration in the field. The application of LLMs in election
forecasting is an emerging area of research that holds consid-
erable promise. With ongoing advancements in computational
models, data collection methods, and analytical techniques,
there is potential for significant improvements in the accuracy
of election predictions. This study serves as a catalyst for
further investigation, highlighting the need for continuous
innovation to address the challenges identified and to harness
the full potential of LLMs in political analysis.
REFERENCES
[1] J. A. Robinson and D. Acemoglu, Why nations fail: The origins of
power, prosperity and poverty . Profile London, 2012.
[2] A. Przeworski, Democracy and development: Political institutions and
well-being in the world, 1950-1990. Cambridge University Press, 2000.
[3] A. Alesina and R. Perotti, “The political economy of growth: A critical
survey of the recent literature,” The World Bank Economic Review ,
vol. 8, no. 3, pp. 351–371, 1994.
[4] C. Wlezien and R. S. Erikson, “The timeline of presidential election
campaigns,” The Journal of Politics , vol. 64, no. 4, pp. 969–993, 2002.
[5] J. W. Goodell, R. J. McGee, and F. McGroarty, “Election uncertainty,
economic policy uncertainty and financial market uncertainty: a pre-
diction market analysis,” Journal of Banking & Finance , vol. 110, p.
105684, 2020.
[6] B. Bimber, Information and American Democracy: Technology in the
Evolution of Political Power, ser. Communication, Society and Politics.
Cambridge University Press, 2003.
[7] D. Gayo-Avello, “A meta-analysis of state-of-the-art electoral prediction
from twitter data,” Social Science Computer Review , vol. 31, no. 6, pp.
649–679, 2013.
[8] A. Tumasjan, T. Sprenger, P. Sandner, and I. Welpe, “Predicting elections
with twitter: What 140 characters reveal about political sentiment,”
Proceedings of the International AAAI Conference on Web and Social
Media, vol. 4, no. 1, pp. 178–185, May 2010.
[9] A. Jungherr, “Twitter use in election campaigns: A systematic literature
review,” Journal of information technology & politics , vol. 13, no. 1,
pp. 72–91, 2016.

[10] P. Barber ´a, J. T. Jost, J. Nagler, J. A. Tucker, and R. Bonneau, “Tweeting
from left to right: Is online political communication more than an echo
chamber?” Psychological science, vol. 26, no. 10, pp. 1531–1542, 2015.
[11] M. Conover, J. Ratkiewicz, M. Francisco, B. Gonc ¸alves, F. Menczer,
and A. Flammini, “Political polarization on twitter,” in Proceedings of
the international aaai conference on web and social media, vol. 5, no. 1,
2011, pp. 89–96.
[12] R. M. Bond, C. J. Fariss, J. J. Jones, A. D. Kramer, C. Marlow, J. E.
Settle, and J. H. Fowler, “A 61-million-person experiment in social
influence and political mobilization,” Nature, vol. 489, no. 7415, pp.
295–298, 2012.
[13] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and
J. Steinhardt, “Measuring massive multitask language understanding,”
arXiv preprint arXiv:2009.03300 , 2020.
[14] W. Zhong, R. Cui, Y . Guo, Y . Liang, S. Lu, Y . Wang, A. Saied, W. Chen,
and N. Duan, “Agieval: A human-centric benchmark for evaluating
foundation models,” 2023.
[15] W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y . Hou, Y . Min, B. Zhang,
J. Zhang, Z. Dong, Y . Du, C. Yang, Y . Chen, Z. Chen, J. Jiang, R. Ren,
Y . Li, X. Tang, Z. Liu, P. Liu, J.-Y . Nie, and J.-R. Wen, “A survey of
large language models,” 2023.
[16] B. O’Connor, R. Balasubramanyan, B. Routledge, and N. Smith, “From
tweets to polls: Linking text sentiment to public opinion time series,”
in Proceedings of the international AAAI conference on web and social
media, vol. 4, no. 1, 2010, pp. 122–129.
[17] K. et al., “Adjustment of issue positions based on network strategies in
an election campaign: A two-mode network autoregression model with
cross-nested random effects,” Social Networks , 2013, special Issue on
Advances in Two-mode Social Networks.
[18] K. Sokolova and C. Perez, “Elections and the twitter community:
The case of right-wing and left-wing primaries for the 2017 french
presidential election,” in ASONAM 2018. IEEE, 2018, pp. 1021–1026.
[19] S. Alashri, S. S. Kandala, V . Bajaj, R. Ravi, K. L. Smith, and K. C.
Desouza, “An analysis of sentiments on facebook during the 2016 us
presidential election,” in ASONAM 2016. IEEE, 2016, pp. 795–802.
[20] D. Gayo-Avello, P. Metaxas, and E. Mustafaraj, “Limits of electoral
predictions using twitter,” in Proceedings of the International AAAI
conference on web and social media , vol. 5, no. 1, 2011, pp. 490–493.
[21] A. Ceron, L. Curini, S. M. Iacus, and G. Porro, “Every tweet counts?
how sentiment analysis of social media can improve our knowledge of
citizens’ political preferences with an application to italy and france,”
New media & society , vol. 16, no. 2, pp. 340–358, 2014.
[22] F. Mancini, E. F. Letouze, P. Meier, P. Vinck, G. M. Musila, R. Muggah,
G. Diniz, H. Puig Larrauri, A. Matveeva, and M. O’Reilly, “New
technology and the prevention of violence and conflict,” International
Peace Institute, UNDP , USAID (2013), 2013.
[23] A. Khan, H. Zhang, N. Boudjellal, A. Ahmad, and M. Khan, “Improv-
ing sentiment analysis in election-based conversations on twitter with
elecbert language model.” Computers, Materials & Continua , vol. 76,
no. 3, 2023.
[24] P. Chauhan, N. Sharma, and G. Sikka, “The emergence of social media
data and sentiment analysis in election prediction,” Journal of Ambient
Intelligence and Humanized Computing , vol. 12, pp. 2601–2627, 2021.
[25] Q. You, J. Luo, H. Jin, and J. Yang, “Robust image sentiment analysis
using progressively trained and domain transferred deep networks,”
Proceedings of the AAAI Conference on Artificial Intelligence , vol. 29,
no. 1, Feb. 2015.
[26] F. Huang, K. Wei, J. Weng, and Z. Li, “Attention-based modality-
gated networks for image-text sentiment analysis,” ACM Transactions
on Multimedia Computing, Communications, and Applications (TOMM),
vol. 16, no. 3, pp. 1–19, 2020.
[27] M. R. H. Khan, U. S. Afroz, A. K. M. Masum, S. Abujar, and S. A.
Hossain, “Sentiment analysis from bengali depression dataset using
machine learning,” in ICCCNT 2020, 2020, pp. 1–5.
[28] C. Bayrak and M. Kutlu, “Predicting election results via social media:
A case study for 2018 turkish presidential election,” IEEE Transactions
on Computational Social Systems , vol. 10, no. 5, pp. 2362–2373, 2023.
[29] A. Rashed, M. Kutlu, K. Darwish, T. Elsayed, and C. Bayrak,
“Embeddings-based clustering for target specific stances: The case of
a polarized turkey,” ICWSM 2021 , vol. 15, no. 1, pp. 537–548, May
2021.
[30] Z. Xie, G. Liu, J. Wu, and Y . Tan, “Big data would not lie: prediction
of the 2016 taiwan election via online heterogeneous information,” EPJ
Data Science, vol. 7, no. 1, pp. 1–16, 2018.
[31] M. Li, E. Perrier, and C. Xu, “Deep hierarchical graph convolution for
election prediction from geospatial census data,” in Proceedings of the
AAAI conference on artificial intelligence , vol. 33, no. 01, 2019, pp.
647–654.
[32] J. Jiang, X. Ren, and E. Ferrara, “Retweet-bert: Political leaning
detection using language features and information diffusion on social
networks,” ICWSM 2023, vol. 17, no. 1, pp. 459–469, Jun. 2023.
[33] D. Baumeister and T. Hogrebe, “On the complexity of predicting election
outcomes and estimating their robustness,” SN Computer Science, vol. 4,
no. 4, p. 362, 2023.
[34] M. Reveilhac, “The influences of political strategies and communication
styles on political candidates’ online and offline visibility,” Journal of
Political Marketing, pp. 1–18, 2023.
[35] Q. Alvi, S. F. Ali, S. B. Ahmed, N. A. Khan, M. Javed, and H. Nobanee,
“On the frontiers of twitter data and sentiment analysis in election
prediction: a review,” PeerJ Computer Science, vol. 9, p. e1517, 2023.
[36] “Election commission of india statistical report,” May 2022. [Online].
Available: https://www.eci.gov.in/statistical-reports
[37] “Punjab Election 2022 Opinion Poll and Exit Poll Results, Survey
and Predictions - Oneindia,” https://www.oneindia.com/punjab-election-
2022-opinion-poll-and-exit-poll/.
[38] “Uttar Pradesh Election 2022 Opinion Poll and Exit Poll Results, Survey
and Predictions - Oneindia,” https://www.oneindia.com/uttar-pradesh-
election-2022-opinion-poll-and-exit-poll/.
[39] L. T. et al., “Zephyr: Direct distillation of lm alignment,” 2023.
[40] H. T. et al., “Llama 2: Open foundation and fine-tuned chat models,”
2023.
[41] I. O. Gallegos, R. A. Rossi, J. Barrow, M. M. Tanjim, S. Kim,
F. Dernoncourt, T. Yu, R. Zhang, and N. K. Ahmed, “Bias and fairness
in large language models: A survey,” arXiv preprint arXiv:2309.00770 ,
2023.
[42] E. Beeching, C. Fourrier, N. Habib, S. Han, N. Lambert, N. Rajani,
O. Sanseviero, L. Tunstall, and T. Wolf, “Open llm leaderboard,” 2023.
[43] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal,
A. Neelakantan, P. Shyam, G. Sastry, A. Askell et al., “Language mod-
els are few-shot learners,” Advances in neural information processing
systems, vol. 33, pp. 1877–1901, 2020.
[44] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever et al.,
“Language models are unsupervised multitask learners,” OpenAI blog ,
vol. 1, no. 8, p. 9, 2019.
[45] D. Thorstad, “Cognitive bias in large language models: Cau-
tious optimism meets anti-panglossian meliorism,” arXiv preprint
arXiv:2311.10932, 2023.
