---
title: 'Using ChatGPT in Content Marketing: Enhancing Users’ Social Media Engagement in Cross-Platform
  Content Creation through Generative AI'
url: https://doi.org/10.1145/3648188.3675142
category: ai-marketing
subcategory: empirical
date: 2024-08
venue: ''
authors:
- Kholoud K. Aldous
- Joni Salminen
- Ali Farooq
source: openalex-oa
pdf_url: https://strathprints.strath.ac.uk/90546/1/Aldous-etal-2024-Using-ChatGPT-in-content-marketing.pdf
pages: 8
chars: 57127
fetched_at: '2026-11-08T16:52:14+00:00'
kb_version: 1
---

# Using ChatGPT in Content Marketing: Enhancing Users’ Social Media Engagement in Cross-Platform Content Creation through Generative AI

Using ChatGPT in Content Marketing: Enhancing Users’ Social
Media Engagement in Cross-Platform Content Creation through
Generative AI
Kholoud Aldous
Qatar Computing Research Institute
Doha, Qatar
kkaldous@hbku.edu.qa
Joni Salminen
University of Vaasa
Vaasa, Finland
jonisalm@uwasa.fi
Ali Farooq
University of Strathclyde
Glasgow, Scotland
afk@ieee.org
Soon-gyo Jung
Qatar Computing Research Institute
Doha, Qatar
sjung@hbku.edu.qa
Bernard J. Jansen
Qatar Computing Research Institute
Doha, Qatar
jjansen@acm.org
ABSTRACT
As the integration of artificial intelligence into social media con-
tinues to attract attention, the key impacts on content marketing
are still undefined. Initial studies have shown that language models
are capable of producing content that is competitive with content
created by humans. However, how can such content be tailored
for different social media platforms as part of an organization’s
content marketing strategy? To address this question, we evaluate
the effectiveness of using GPT-4, to generate cross-platform content
for Facebook, Instagram, and Twitter (currently X). Participants
(𝑁 = 892) evaluated 30 AI-created content (ACC) and human-
created content (HCC). Findings show that ACC scored higher on
preference by users, call-to-action, and emotional responses than
HCC for Facebook. However, AI’s advantage wanes on Twitter and
Instagram, where posts are terser. The results imply that GPT-4
comprehends what type of content to create for different platforms,
making it a useful tool for cross-platform content creation.
CCS CONCEPTS
• Human-centered computing → Collaborative content cre-
ation; Social media.
KEYWORDS
Social media, Facebook, Instagram, Twitter, Generative AI
ACM Reference Format:
Kholoud Aldous, Joni Salminen, Ali Farooq, Soon-gyo Jung, and Bernard
J. Jansen. 2024. Using ChatGPT in Content Marketing: Enhancing Users’
Social Media Engagement in Cross-Platform Content Creation through
Generative AI. In 35th ACM Conference on Hypertext and Social Media (HT
’24), September 10–13, 2024, Poznan, Poland. ACM, New York, NY, USA,
8 pages. https://doi.org/10.1145/3648188.3675142
This work is licensed under a Creative Commons Attribution International
4.0 License.
HT ’24, September 10–13, 2024, Poznan, Poland
© 2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0595-3/24/09
https://doi.org/10.1145/3648188.3675142
1 INTRODUCTION
Social media is a fundamental part of how people communicate,
share, and interact online [13, 61]. Social media platforms, such as
Facebook (FB), Instagram (IG), and Twitter (TW) (currently “X”),
have their unique features and user bases, creating challenges for
companies and other organizations producing content [2] as part of
their content marketing1. To maximize their reach, organizations
create cross-platform content as a social media marketing strategy
[49, 68]. Cross-platform content refers to digital content (i.e., posts
including text, images, and video) adapted to suit different social
media platforms’ features and user demographics.
Generative artificial intelligence (Gen AI) technology offers new
ways to customize cross-platform content for different social media
platforms, notably using large language models (LLMs) [28]. We
refer to this capability of customizing content for different social
media platforms as the generation of cross-platform content. In
general, LLM technologies, such as OpenAI’s GPT-4, demonstrate
remarkable capabilities in understanding and generating text [24].
Consequently, users’ interaction with AI-generated content is rais-
ing significant interest within fields like computer science, con-
sumer psychology, and marketing [11, 12, 35, 68]. However, ques-
tions remain about how effective generative AI is in generating
engaging cross-platform content, how the cross-platform content
compares to content made by humans in terms of its impact on the
users, and what the overall effects of AI-generated social media
content are on user engagement and preferences. Though nascent
work addresses these questions [35, 62, 68], much remains to be
explored.
Gen AI can create original digital content from prompts (i.e.,
instructions, requests) provided by users [68]. These prompts can
specify the desired output type and characteristics the user desires,
and the AI will produce the requested content. It is, therefore, an
intriguing question if we ask the AI to generate “engaging” content,
is it able to do so? Addressing the problem of cross-platform content
adaptation through LLMs, this research looks into how AI-created
content, specifically using OpenAI’s GPT-4, performs on specific
social media platforms and how it affects user engagement and
emotions. Collecting data from real users, we compare AI-created
1Content marketing is the process of planning, creating, and distributing digital content
to engage customers and improve marketing performance [68].
376

HT ’24, September 10–13, 2024, Poznan, Poland Kholoud Aldous, Joni Salminen, Ali Farooq, Soon-gyo Jung, and Bernard J. Jansen
content (ACC) with human-created content (HCC) on three promi-
nent social media platforms–FB, IG, and TW–to verify if LLMs can
improve content marketing in social media. Because these three
platforms each impose specific requirements on the type of content
required to be successful in content marketing [ 7], we pose the
following research questions (RQs):
RQ1: How effectively can ACC (vs. HCC) match specific platform
requirements? Again, this is crucial for LLM-aided content mar-
keting to be successful: it needs to demonstrate awareness of the
distinct conditions in different platforms in terms of length, visual-
ity, tone of voice, and so on.
RQ2: How do users’ emotional responses to ACC compare with
HCC? LLM-generated content might be perceived as robotic, stale,
boring, or disengaging. Good online content evokes emotion–thus,
we investigate this aspect of LLMs being able to create emotionally
engaging content.
RQ3: How does users’ engagement with ACC compare with HCC?
“Engagement” is the primary motivation and goal for firms and
other organizations engaging in content marketing [35]. In other
words, these organizations expect reactions and responses from
the audience. Therefore, measuring this aspect of LLM-generated
content is crucial to our investigation.
RQ4: Do users prefer ACC or HCC? Preference relates to users’
overall attitudes, perceptions, and liking of content [2, 6]. To add
value to content marketing, LLM-generated content needs to per-
form well in terms of preference.
We formalize our expectations on the empirical investigation in
the form of hypotheses. Our general expectation, which we then
apply to the individual hypotheses, is that “AI does equally well or
better than humans”. This expectation is based on the growing evi-
dence that LLMs have reached human-level or higher (superhuman)
capabilities across a broad range of tasks [8, 62].
More specifically, for RQ01, we put forth the following hypothe-
ses, all that deal with platform adaptability: ACC scores higher
on topical interest (H01), clarity (H02), tone (H03), and call to
action (CTA) (H04) than HCC.
For RQ02, we put forth the following hypothesis that deals with
users’ emotional responses to content: H05: ACC scores higher
on positive emotional responses than HCC.
For RQ03, we put forth the following hypotheses, all that deal
with individuals’ engagement with social media content: ACC
scores higher on reads (H06), views (H07), likes (H08), comments
(H09), and shares (H10) than HCC.
For RQ4, we put forth a hypothesis that deals with users’ prefer-
ences: H11: ACC scores higher on preference than HCC.
For each of the hypotheses, our premise is that ACC will out-
perform HCC given the reported potential of LLMs in content
generation [28]. To address our RQs, we conducted a user study
where participants evaluated the HCC and ACC for three promi-
nent social media platforms: FB, IG, and TW. Participants were
asked to assess the platform’s adaptability, emotional responses,
engagement, content preferences, and other factors for each post,
without knowing if the post was created using HCC or ACC.
Our findings have implications for a broad range of stakeholders,
including actors like content marketers, news and media organi-
zations, political marketers, non-profits, advertising firms, and so
on. In addition to organizations, individuals–called influencers or
creators—also rely on content marketing on social media to gen-
erate income. The estimated annual value of the digital creator
economy is $14 billion USD [19], involving creative workers such
as writers, podcasters, artists, and musicians who use social media
to reach their audiences and generate income. So, our research is
relevant for several stakeholder groups.
2 LITERATURE REVIEW
Content creators often share similar content across multiple social
media platforms, known ascross-platform content creation [52]. This
approach is used to manage several social media profiles/channels
efficiently. It typically involves tailoring content by platform to
address each platform’s unique features [ 34, 53, 57, 66]. For in-
stance, FB attracts users looking for meaningful and personal con-
nections [58]. IG is more about visuals and lifestyles, so it attracts
users focused on personal and corporate branding [39]. TW is more
about quick updates and news; i.e., concise microtext [32]. These
unique aspects of each platform shape users’ expectations and en-
gagement. So, content that is engaging on one platform may not
necessarily perform well on another, despite the similarities in the
content [3]. However, creating cross-platform engaging content is
both time-consuming and requires significant effort, which high-
lights the need to support creating engaging content for multiple
platforms [2, 51].
Because social media platforms such as FB, IG, and TW each
possess distinctive content ecosystems characterized by unique
linguistic and stylistic norms that dictate user engagement and
interaction [4], it is both a challenge and an opportunity for LLMs to
adapt to these diverse content characteristics–ranging from topical
interest and clarity to tone of voice and CTA–which are critical
determinants of user engagement metrics in content marketing,
including likes, comments, and shares [7, 65]. While research [1, 21,
42, 47] highlights LLMs’ ability to adapt different writing styles and
contextualizing content, a gap remains in understanding how these
capabilities translate to platform-specific content creation, where
each social media platform presents its own set of requirements and
audience expectations. To address this gap, we propose hypotheses
H01-H04, suggesting that ACC may exhibit superior adaptability
in aligning with platform-specific demands.
Emotions are crucial in our daily lives, shaping how we define hu-
manness, express ourselves, and communicate with others [36, 48].
Social media content is a profound reflection of personal expression,
revealing insights into the private and public aspects of individuals’
lives through their emotions, thoughts, and activities [43, 44, 56].
Emotions significantly impact our daily actions, beliefs, and mo-
tivations [36], and understanding emotional reactions is key to
comprehending the motivations of social media users [20, 72]. So-
cial media postings can trigger emotions in readers, leading to
expressions of feelings through comments or other actions [71].
Research on emotional contagion suggests that users mirror emo-
tions in social media, with positive content often leading to positive
reactions [45], while negatively charged content can trigger neg-
ative emotions [31]. LLMs, like ChatGPT, can perform sentiment
and emotion classification comparably to systems like IBM Watson
without explicit training [17], aligning with human emotions [69].
377

Using ChatGPT in Content Marketing HT ’24, September 10–13, 2024, Poznan, Poland
Though emotional analysis in ACC using LLMs has been a subject
of interest [ 26, 73], comparative studies between the emotional
depth of ACC and HCC, especially in a social media context, are
scarce. So, H05 suggests that ACC may evoke higher positive emo-
tional responses than HCC, leveraging AI’s proficiency in sentiment
analysis and emotional tone replication.
User engagement is impacted by many factors, including the
context, content, and creator [37, 50, 54]. User engagement is de-
fined as “the emotional, cognitive, and behavioral connection that
exists, at any point in time and possibly over time, between a
user and a resource, ” with a resource being an online application
or content [ 10]. Our approach involves analyzing user engage-
ment through recorded user behaviors, as detailed in prior stud-
ies [9, 38, 46]. In social media, engagement metrics (e.g., likes, com-
ments, and shares) are crucial for businesses and research to assess
performance in terms of marketing objectives [59].
Empirical studies show that users struggle to discern between
ACC and HCC, often unable to accurately identify the true author
[40, 70]. Specifically, Henestrosa et al. [33] found no significant dif-
ferences in the perceived credibility and trustworthiness between
texts authored by AI and humans. Rezwana and Maher [60] found
that AI-to-human communication significantly enhances user en-
gagement, collaboration experience, and the perception of AI as a
reliable, personal, and intelligent source. In light of the complex
interplay between content characteristics and user engagement
behaviors, H06-H10 explore the potential of ACC to surpass HCC
in engaging users, driven by its adaptability and emotional depth.
In H11, we investigate whether the nuanced capabilities of AI in
content generation might lead to a preference for ACC over HCC.
3 METHODOLOGY
3.1 Participants
To secure a broad and varied sample for investigating our RQs, we
recruited 892 participants through CloudResearch, an online partici-
pant pool [18]. Our invitations targeted US-based social media users
who fulfilled three criteria: (1) active usage of one of the studied
platforms (FB, IG, or TW); (2) passing the quality check questions;
and (3) currently engaged in some form of employment–whether
full-time, part-time, self-employed (both full-time and part-time) or
studying. We applied a bucketed data collection to ensure a reason-
ably sized sample from each platform under investigation. For FB,
the sample consisted of 301 regular users (𝑀𝑎𝑔𝑒 = 41.76 years). Of
these, 36.88% (n = 111) were male, and 63.12% (n = 190) were female.
Participants reported spending 4.58 hours per day on the platform.
For IG, the sample consisted of 305 regular users(𝑀𝑎𝑔𝑒 = 48 years).
Among these participants, 40.66% (n = 124) were male, and 59.34%
(n = 181) were female. Participants reported spending 5.08 hours per
day on the platform. For TW, the sample consisted of 286 regular
users (𝑀𝑎𝑔𝑒 = 41.81 years). Among these participants, 42.66% (n
= 122) were male, and 57.34% (n = 164) were female. Participants
reported spending 5.19 hours per day on the platform.
3.2 Procedure
We first collected and prepared 90 pairs of HCC and ACC, 30 pairs
per platform (i.e., FB, IG, and TW). These pairs relate to 30 cross-
platform content, where each post is shared on three platforms. We
Figure 1: The study pipeline shows the process of FB, IG, and
TW users starting the Qualtrics corresponding survey. Each
participant sees three randomly selected content. Each post
has a video, version A, HCC, and version B, ACC, which is
displayed to users randomly.
conducted three separate surveys, each tailored to a specific social
media platform, on Qualtrics. The study pipeline is shown in Figure
1. To ensure participant attentiveness and genuine engagement,
we integrated 30 quality control questions, spread at one per post.
Participants who failed any of the quality check questions were
excluded from the study. After getting their consent, participants
were assigned the task of evaluating three posts specific to one
platform: FB, IG, or TW.
This study employed a within-subjects design [30, 41]. Each par-
ticipant was presented with two versions of a post related to the
same video on a single social media platform, HCC and ACC, with
the versions counterbalanced across all participants. The partici-
pants were directed to read each post with a link to the original
video to watch. The participants were not informed about the ori-
gin of each post, whether it was created by a human or by GPT-4.
This ensures that every evaluation is a paired comparison within
the same platform and related to the same content. Participants
were exposed to a random selection of three posts from a pool of
30 posts. With the help of Qualtrics’ balanced distribution option,
we ensured that each post received nearly equal evaluations from
different participants and equal ordering. Each post was evaluated
on average 30.1 times on FB, 30.5 times on IG, and 28.6 times on
TW. Given that the impact of labeling ACC on user engagement
behavior is significant [ 26], the current study adopts a method
where we present participants with two versions of the same post
in sequence, without indicating the source.
3.3 Data Collection
Collecting Video Content: We compiled a dataset of 30 video clips,
cross-posted during June and July 2023 on FB, IG, and TW from a
major international news and media organization focused on social
media distribution and applying the cross-channel content strategy.
We selected FB, IG, and TW based on their popularity and diverse
user bases, ranking as the top three platforms widely used at the
time of this study2. Our study focused on video content to reduce
biases from different content types [4].
All videos were sourced exclusively from the organization, AJ+
English, known for its contemporary approach to journalism, lever-
aging digital platforms to reach a global audience. Their content
often covers hard-hitting news with social issues, presenting them
2https://www.similarweb.com/top-websites/united-states/computers-electronics-
and-technology/social-networks-and-online-communities/
378

HT ’24, September 10–13, 2024, Poznan, Poland Kholoud Aldous, Joni Salminen, Ali Farooq, Soon-gyo Jung, and Bernard J. Jansen
in a format that appeals to the younger generation. AJ+ English had
11M followers on FB, 1.2M followers on TW, and 947K followers
on IG at the time of the study. The collected videos are exactly the
same across the platforms, with the same or different associated
text descriptions or captions.
Across the three platforms, video engagement levels vary, even
when the same content is cross-posted [3]. On FB, on average, a
post had 4,173 likes, 445 comments, and 1,002 shares. On IG, on
average, a post had 7,007 likes, 116 comments, and 1,420 shares. On
TW, on average, a post had 117 likes, 5 comments, and 63 shares.
Video Transcription: We transcribed the 30 collected videos into
text to serve as input for generating LLM content. At the time
of this research, GPT-4 required text-based input. This transcrip-
tion process guarantees that we grasp the precise phrasing and
context vital for generating accurate and engaging LLM content.
On average, a single video transcript contained approximately 493
terms, equivalent to roughly 2,998 characters. The range of terms
per transcript was observed to be quite diverse, with a minimum
of 186 terms (or approximately 1,093 characters) and reaching a
maximum of 1,122 terms (or approximately 6,722 characters). All
transcripts were manually checked for accuracy and consistency
with the video content. For videos featuring non-English speakers,
we integrated the translated text into the video transcripts. GPT-4
has a limit of 32,000 tokens, while our transcripts have a maximum
of 1,122 terms, which is well within the limit.
GPT-4 Prompting: There are two approaches to prompting GPT-4
for cross-platform content generation: individual platform prompt
and combined prompt. The choice between these approaches de-
pends on the goals of the content strategy—whether it prioritizes
uniformity and efficiency or customized engagement for each plat-
form. This research simultaneously adopts the combined prompt for
creating a uniform post across different platforms. We formulated
a prompt for GPT-4 that specifically asked the model to create a
tweet for TW, a caption for IG, and a post for FB. The prompt was
structured as follows: “Please provide a Twitter tweet, an Instagram
caption, and a Facebook post suitable for video content based on the
following transcript: [transcript]” The concatenated prompt and a
video transcript were fed into GPT-4, generating tailored content
for each specified platform. As we have thirty videos, we repeated
the prompting thirty times, one per video transcript.
All prompts were performed on the first of August, 2023, using
GPT-4. The output for TW was the first segment of the response,
designed to adhere to TW’s character limit. The output for IG
focused on generating interest and action, encouraging users to
swipe left or click the video link. The FB post was extracted as a
more descriptive or engaging post that would suit FB’s audience
and platform dynamics. The ACC contains hashtags for the three
platforms, which serve as critical tools for categorizing, enhancing
discoverability, and driving engagement.
ACC underwent a detailed manual review to remove any action-
related text that did not align with our research focus. For example,
even though we mentioned in the prompt it is a video, we still got
‘Swipe ⇒’ and ‘[link to the video]’ on a few IG captions (5 out of
30). These were not relevant to our needs, so we manually removed
them. For each video, we first took a screenshot of the HCC on the
respective platforms. Then, we replaced the post text with the AI-
created post and took another screenshot (AI-created) to create the
survey. When taking the screenshots, we hide engagement metrics
to eliminate any social effect during the evaluation. We ensured
the two versions of the post, ACC and HCC, were the same format
with only different text.
3.4 Measures
Platform Adaptability: For addressing RQ01, platform adaptabil-
ity was evaluated through four aspects: topical interest, clarity,
tone, and CTA. The following survey questions were used, with a
five-scale semantic differential: (1) Topical Interest: The level of
interest users had for the content (Not Interesting (1) to Very Inter-
esting (5)); (2) Clarity (Very unclear (1) to Very clear (5)); (3) Tone
(Very informal (1) to Very formal (5)); and (4) CTA: a statement
motivating viewers to engage with the post (like, comment, share,
etc.) (Very weak (1) to Very strong (5)).
Emotional Response: For addressing RQ02, we compared the par-
ticipant’s emotional responses to HCC and ACC using general
sentiment (positive or negative) [16]. The participants were asked
about their general sentiment through the question, “How did the
post make you feel?” with the responses collected on a Likert scale
from 1 (Very negative) to 5 (Very positive).
Engagement: For measuring user engagement, we used both the
consumption (e.g., views and reads) and contribution measures (e.g.,
likes, comments, and shares) [25, 63]. Participant engagement was
measured through a series of questions using a Likert scale ranging
from Very unlikely (1) to Very likely (5). Participants were asked to
rate their likelihood of reading the post, viewing the video based
on the post content, liking, commenting, and sharing the ACC and
HCC (addressing RQ03).
User Preferences: The measure used to address RQ04 was par-
ticipants’ post-preference. Participants were presented with pairs
of content – one HCC and the other ACC. For each pair, they re-
sponded to the question, “If you had to select, which of the two posts
do you prefer?” . Their responses allowed us to determine which
type of post (human vs. AI) was more preferred.
4 RESULTS
4.1 RQ01
H01. AI-created content has better topical interest than human-
created content. A Wilcoxon signed-rank test was conducted to
compare HCC and ACC for FB, IG, and TW regarding topical in-
terest. For FB, the results indicated that ACC had higher topical
interest scores than HCC, W = 20701.0, p = 0.001. The IG and TW
results were non-significant (see Table 1). Thus, H01 is partially
supported: ACC shows better topical interest than HCC for FB .
H02. AI-created content has better clarity than human-
created content. For FB, the results indicated that ACC had higher
clarity scores than HCC, W = 17957.0, p <0.001. The IG and TW
results were non-significant (see Table 1). Thus, H02 is partially
supported: ACC shows better clarity than HCC for FB .
H03. AI-created content has better tone than human-created
content. For FB, the results indicated that ACC had higher tone
scores than HCC, W = 18818.0, p <0.001. The IG and TW results
were non-significant (see Table 1). Thus, H03 is partially supported:
ACC shows higher tone scores than HCC for FB .
379

Using ChatGPT in Content Marketing HT ’24, September 10–13, 2024, Poznan, Poland
Table 1: Wilcoxon test results comparing the HCC with the
ACC across measures. Significant results are in green color.
Facebook
RQ Measure M (HCC) M (ACC) Md (HCC) Md (ACC) W p N
RQ01
Topical (H01) 3.807 3.924 4.0 4.0 20701.0 0.001 902
Clarity (H02) 4.264 4.433 5.0 5.0 17957.0 0.000 902
Tone (H03) 3.645 3.867 4.0 4.0 18818.0 0.000 902
CTA (H04) 3.614 3.847 4.0 4.0 23572.5 0.000 902
RQ02 Emotions (H5) 3.494 3.574 3.0 4.0 17605.0 0.008 902
RQ03
Read (H06) 3.650 3.766 4.0 4.0 20374.5 0.001 902
View (H07) 3.641 3.717 4.0 4.0 23083.0 0.014 902
Like (H08) 3.394 3.538 4.0 4.0 20405.0 0.000 902
Comment (H09) 3.155 3.251 3.0 3.0 19613.0 0.005 902
Share (H10) 3.194 3.329 3.0 4.0 18200.5 0.000 902
Instagram
RQ01
Topical (H01) 3.998 4.007 4.0 4.0 18521.5 0.720 914
Clarity (H02) 4.423 4.454 5.0 5.0 20424.0 0.266 914
Tone (H03) 3.719 3.751 4.0 4.0 26310.5 0.203 914
CTA (H04) 3.822 3.898 4.0 4.0 32135.5 0.024 914
RQ02 Emotions (H5) 3.469 3.564 3.0 4.0 15878.0 0.002 914
RQ03
Read (H06) 3.784 3.807 4.0 4.0 21309.5 0.435 914
View (H07) 3.757 3.801 4.0 4.0 24257.0 0.197 914
Like (H08) 3.550 3.576 4.0 4.0 24359.0 0.347 914
Comment (H09) 3.328 3.341 4.0 4.0 17612.0 0.574 914
Share (H10) 3.291 3.319 4.0 4.0 19156.5 0.259 914
Twitter
RQ01
Topical (H01) 3.943 3.980 4.0 4.0 21645.0 0.149 857
Clarity (H02) 4.381 4.429 5.0 5.0 21312.0 0.094 857
Tone (H03) 3.718 3.754 4.0 4.0 31205.5 0.258 857
CTA (H04) 3.693 3.868 4.0 4.0 27260.0 0.000 857
RQ02 Emotions (H5) 3.542 3.578 4.0 4.0 23858.0 0.146 857
RQ03
Read (H06) 3.744 3.793 4.0 4.0 22128.5 0.090 857
View (H07) 3.753 3.773 4.0 4.0 22657.0 0.576 857
Like (H08) 3.561 3.621 4.0 4.0 27759.5 0.070 857
Comment (H09) 3.253 3.321 4.0 4.0 20274.0 0.028 857
Share (H10) 3.360 3.418 4.0 4.0 20693.5 0.072 857
H04: AI-created content has a better call to action than
human-created content. For FB, the ACC had a higher CTA score
than HCC, W = 23572.5, p <0.001. For IG, ACC had a higher CTA
score than HCC, W = 32135.5, p = 0.024. For TW, ACC had a higher
CTA score than HCC, W = 27260.0, p <0.001. Thus, H04 is fully
supported: ACC has a better CTA than HCC for all platforms .
4.2 RQ02
H05. AI-created content results in higher positive emotional
responses than human-created content. For FB, a Wilcoxon test
indicated ACC had higher emotional response scores than HCC, W
= 17605.0, p = 0.008. For IG, ACC had higher emotional response
scores than HCC, W = 15878.0, p = 0.002. The result for TW was
non-significant. Thus, H05 is partially supported: ACC scores higher
on positive emotional responses than HCC (for FB and IG) .
4.3 RQ03
H06: AI-created content will have higher reads than human-
created content. For FB, ACC had higher reads than HCC, W =
20374.5, p = 0.001. The IG and TW results were non-significant.
Thus, H06 is partially supported: ACC has higher reads than HCC for
FB.
H07: AI-created content will have higher views than human-
created content. For FB, ACC had a higher views score than HCC,
W = 23083.0, p = 0.014. The IG and TW results were non-significant.
Thus, H07 is partially supported: ACC has higher views than HCC
for FB.
H08: AI-created content will have higher likes than human-
created content. For FB, ACC had a higher likes score than HCC,
W = 20405.0, p <0.001. The IG and TW results were non-significant.
Thus, H08 is partially supported: ACC has higher likes than HCC for
FB.
H09: AI-created content will have higher comments than
human-created content. For FB, ACC had a higher comments
score than HCC, W = 19613.0, p = 0.005. For TW, ACC had a higher
comments score than HCC, W = 20274.0, p = 0.028. The IG result was
non-significant. Thus, H09 is partially supported: ACC has higher
comments than HCC for FB and TW .
H10: AI-created content will have higher shares than human-
created content For FB, ACC had a higher share score than HCC,
W = 18200.5, p <0.001. The IG and TW results were non-significant.
Thus, H10 is partially supported: ACC has higher reads than HCC for
FB.
4.4 RQ04
H11. AI-created content is preferred relative to human-created
content. The Chi-square test of independence was performed to
test the preference for ACC relative to HCC among participants on
FB, IG, and TW. FB users had a higher preference for ACC, 𝜒 2(1,
N = 903) = 35.48, p <.001. The ACC (n = 541) was preferred more
frequently than HCC (n = 362). TW users had a higher preference
for ACC, 𝜒 2 (1, N = 858) = 12.61, p <.001. The ACC (n = 481) was
preferred more frequently than HCC (n = 377). The result on IG was
non-significant. Thus, H11 is partially supported: ACC is preferred
to HCC for FB and TW .
5 DISCUSSION
5.1 Study Implications
Addressing RQ1, ACC demonstrated superior adaptability for FB,
with better clarity, tone, and topical interest compared to HCC. For
IG and TW, however, the advantages of ACC in matching platform-
specific requirements were not as pronounced, with non-significant
differences observed in most cases. Addressing RQ2, ACC elicited
stronger positive emotional responses than HCC for FB and IG,
indicating that AI has the potential to engage users emotionally
more effectively on these platforms. TW did not show a significant
difference in emotional response between ACC and HCC. Address-
ing RQ3, for FB, ACC consistently led to higher user engagement
across various metrics, including reads, views, likes, comments,
and shares. This suggests that ACC can more effectively drive en-
gagement on this platform. For IG and TW, the impact of AI on
engagement was less clear, with most measures not showing sig-
nificant differences. Addressing RQ4, users showed a preference
for ACC over HCC for FB and TW, indicating a general favorability
towards the former in terms of content preference. IG users did not
exhibit a significant preference between ACC and HCC.
In summary, our findings demonstrate that GPT-4 effectively
generates cross-platform content that is preferable to HCC on FB
and TW and has similar preferences compared to HCC on IG. This
finding highlights the changing nature of LLMs [15], which adapt
to different social media platforms with varying content styles and
audience engagement strategies. In other words, ACC is at least as
good (on IG) and statistically better on FB and TW based on our
study results. For FB, all the tested hypotheses showed significant
results. Participants perceived the ACC as more adapted to the FB
380

HT ’24, September 10–13, 2024, Poznan, Poland Kholoud Aldous, Joni Salminen, Ali Farooq, Soon-gyo Jung, and Bernard J. Jansen
platform, which is evident in relevance, clarity, tone, and CTA. They
also responded more emotionally to ACC, increasing engagement
through increased reads, views, likes, comments, and shares.
Our findings indicate that ACC exhibits a notable advantage
in evoking emotional responses on platforms such as FB and IG,
as compared to its performance on TW, where human creators
maintain a competitive edge. This distinction may be attributed to
the nature of the content; we leveraged news content, which has
been demonstrated to elicit varying emotional responses across
different social media platforms [6].
For FB, ACC consistently outperformed HCC across all user en-
gagement metrics. The highest gaps were observed in the ‘Likes’
and ‘Shares’ metrics, indicating that ACC might be more likable
and share-worthy on FB than HCC. Also, ACC encourages more
comments than HCC on TW, but similar reads, views, likes, and
shares. Different types of content work better on different plat-
forms [5]. As a result, it is possible that the nature of ACC is more
suited to FB’s content preferences (e.g., narrative content), which
results in higher engagement, while on TW, where concise and
timely content is often key, ACC performs similarly to HCC.
The CTA is where AI does best across FB, IG, and TW. For in-
stance, for a single video post, ACC CTAs varied as follows: on FB,
the call was “We invite you to share your thoughts on the narratives
that shape our world, ” on IG, it encouraged “Don’t forget to leave a
comment and let us know which artifact you’d like us to explore
next!, ” and on TW, it was “Join us as we explore the captivating yet
controversial history behind these artifacts. ” In contrast, HCC for
the same video lacked any form of CTA.
It is important to highlight that we did not explicitly instruct
GPT-4 to include CTA statements; this was automatically included
on most of the ACC. One reason could be that GPT-4 is trained on
a vast array of text data, which includes countless examples of suc-
cessful social media posts, marketing content, and other forms of
marketing communication that effectively use CTAs. As CTAs were
found to encourage users to engage with social media posts [55].
This training enables the AI to learn which CTAs effectively engage
audiences. Also, the fact that these CTAs were included without ex-
plicit instructions suggests that the AI has learned to recognize the
value of CTAs in digital content as a best practice. This demonstrates
the AI’s ability to apply learned concepts in practical applications,
even when not directly prompted to do so.
Additionally, we observe that although the CTA is more pro-
nounced in ACC across the three studied platforms, the engage-
ment metrics on IG and TW do not significantly differ from those
of HCC, except for TW’s comments. This difference may be due to
several factors explored in the literature, including the audience’s
pre-existing relationship with the content creator [55]. For example,
on IG, a CTA motivates followers to participate in eWOM, but not
non-followers [55]. The reader should observe that the mean scores
of ACC (Table 1) were consistently higher than those of HCC across
all studied measures. However, the differences were not statistically
significant in most cases for IG (8 out of 10) and TW (8 out of 10).
This consistent, though not statistically significant, higher perfor-
mance of AI suggests that the study might require more power to
validate the findings, implying a need for a larger sample size. This
is an area for future research.
5.2 Limitations and Future Work
Our participant base was primarily from the US, potentially not
capturing the diverse global attitudes. This geographical limitation
might mean we missed out on varied cultural interpretations, es-
pecially if the AI models are mostly trained on Western datasets.
Although our study focused on data from a single organization that
posts across FB, IG, and TW, it is important to note that organiza-
tions may utilize different platforms. To gain a more comprehensive
understanding of the adaptability of the LLM, future evaluations
on multiple user groups outside of the US and multiple platforms
such as YouTube and LinkedIn would be valuable.
We employed a combined prompt for generating cross-platform
content from a single prompt, yet future research could explore the
effects of using separate prompts for each platform,. While LLMs
incorporate knowledge of platform-specific characteristics, using
just platform names for prompting may lead to biased outputs; an
alternative is to use real-world examples and user profiles for each
platform to minimize inherent biases, a method future research
could evaluate. Additionally, we relied solely on video content
transcripts to generate social media content. While this is suitable
for videos, it does not consider other content types, such as IG
photo albums, photo captions, and images with overlaid text. Future
studies could explore different content sources.
The study asked people to read social media content carefully,
but users might usually glance quickly in real life. This might affect
how the study’s findings relate to what happens in real social media.
One way to improve future research is by trying out two versions
of the same post on the organization’s social media and seeing how
people engage with it. This could involve making a post in one
way and then making a similar one with a slight difference. By
comparing how people interact with both, we can get insights into
what kind of content gets more attention and why. This real world
experiment would be a worthwhile extension of our research.
The findings could partially be affected by the post lengths due to
the longer post lengths observed in ACC compared to HCC. There
is a noticeable trend that the impact of AI is less effective on shorter
social media posts, like those on TW and IG. This suggests that the
length of content affects how people evaluate it [22, 23, 29]. Also,
there could be different platform-specific dynamics, which affect
how content generation methods impact user engagement. Factors
like the nature of the platform, its user demographics, and typical
content consumption patterns could all play a role in how users
perceive and engage with ACC [14, 27, 64, 67]. More research on
these human factors is needed.
Finally, we employed GPT-4 to generate social media content. In
future research, exploring and assessing the performance of other
LLMs like Gemini, Claude, and Llama would be beneficial.
REFERENCES
[1] Mohammad Awad AlAfnan and Siti Fatimah MohdZuki. 2023. Do artificial
intelligence chatbots have a writing style? An investigation into the stylistic
features of ChatGPT-4. Journal of Artificial intelligence and technology 3, 3 (2023),
85–94.
[2] Kholoud Khalil Aldous, Jisun An, and Bernard J. Jansen. 2019. The Challenges
of Creating Engaging Content: Results from a Focus Group Study of a Popular
News Media Organization. In Extended Abstracts of the 2019 CHI Conference on
Human Factors in Computing Systems (CHI EA ’19) . Association for Computing
Machinery, New York, NY, USA, 1–6. https://doi.org/10.1145/3290607.3312810
381

Using ChatGPT in Content Marketing HT ’24, September 10–13, 2024, Poznan, Poland
[3] Kholoud Khalil Aldous, Jisun An, and Bernard J. Jansen. 2019. Predicting Audi-
ence Engagement Across Social Media Platforms in the News Domain. In Social
Informatics (Lecture Notes in Computer Science). Springer International Publishing,
Cham, 173–187. https://doi.org/10.1007/978-3-030-34971-4_12
[4] Kholoud Khalil Aldous, Jisun An, and Bernard J Jansen. 2019. Stylistic features
usage: Similarities and differences using multiple social networks. In Social Infor-
matics: 11th International Conference, SocInfo 2019, Doha, Qatar, November 18–21,
2019, Proceedings 11. Springer, 309–318.
[5] Kholoud Khalil Aldous, Jisun An, and Bernard J Jansen. 2019. View, like, comment,
post: Analyzing user engagement by topic at 4 levels across 5 social media
platforms for 53 news organizations. In Proceedings of the International AAAI
Conference on Web and Social Media , Vol. 13. 47–57.
[6] Kholoud Khalil Aldous, Jisun An, and Bernard J. Jansen. 2022. Measuring 9
Emotions of News Posts from 8 News Organizations across 4 Social Media Plat-
forms for 8 Months. Trans. Soc. Comput. 4, 4, Article 15 (mar 2022), 31 pages.
https://doi.org/10.1145/3516491
[7] Kholoud Khalil Aldous, Jisun An, and Bernard J. Jansen. 2023. What really
matters?: characterising and predicting user engagement of news postings using
multiple platforms, sentiments and topics. Behaviour & Information Technology
42, 5 (April 2023), 545–568. https://doi.org/10.1080/0144929X.2022.2030798
[8] Mostafa M. Amin, Erik Cambria, and Björn W. Schuller. 2023. Will Affective
Computing Emerge From Foundation Models and General Artificial Intelligence?
A First Evaluation of ChatGPT. 38, 2 (2023), 15–23. Publisher: IEEE.
[9] Jisun An and Ingmar Weber. 2018. Diversity in online advertising: a case study
of 69 brands on social media. In Social Informatics: 10th International Conference,
SocInfo 2018, St. Petersburg, Russia, September 25-28, 2018, Proceedings, Part I 10 .
Springer, 38–53.
[10] Simon Attfield, Gabriella Kazai, Mounia Lalmas, and Benjamin Piwowarski. 2011.
Towards a science of user engagement (position paper). In WSDM workshop on
user modelling for Web applications . 9–12.
[11] Claus Atzenbeck, Sam Brooker, and Daniel Roßner. 2023. Storytelling Machines.
In Proceedings of the 6th Workshop on Human Factors in Hypertext (Rome Italy,
2023-09-04). ACM, 1–9. https://doi.org/10.1145/3603607.3613481
[12] Navid Ayoobi, Sadat Shahriar, and Arjun Mukherjee. 2023. The Looming Threat
of Fake and LLM-generated LinkedIn Profiles: Challenges and Opportunities for
Detection and Prevention. InProceedings of the 34th ACM Conference on Hypertext
and Social Media (Rome Italy, 2023-09-04). ACM, 1–10. https://doi.org/10.1145/
3603163.3609064
[13] Fabrício Benevenuto, Tiago Rodrigues, Meeyoung Cha, and Virgílio Almeida.
2012. Characterizing user navigation and interactions in online social networks.
Information Sciences 195 (2012), 1–24.
[14] Aparajita Bhandari and Sara Bimo. 2022. Why’s everyone on TikTok now? The
algorithmized self and the future of self-making on social media. Social Media+
Society 8, 1 (2022), 20563051221086241.
[15] Michael Bossetta and Rasmus Schmøkel. 2022. Cross-Platform Emotions and Audi-
ence Engagement in Social Media Political Campaigning: Comparing Candidates’
Facebook and Instagram Images in the 2020 US Election.Political Communication
40 (2022), 48 – 68. https://doi.org/10.1080/10584609.2022.2128949
[16] Erik Cambria, Dipankar Das, Sivaji Bandyopadhyay, and Antonio Feraco. 2017.
Affective Computing and Sentiment Analysis. In A Practical Guide to Sentiment
Analysis. Springer International Publishing, Cham, 1–10. https://doi.org/10.1007/
978-3-319-55394-8_1
[17] David Carneros-Prado, Laura Villa, Esperanza Johnson, Cosmin C Dobrescu, Al-
fonso Barragán, and Beatriz García-Martínez. 2023. Comparative Study of Large
Language Models as Emotion and Sentiment Analysis Systems: A Case-Specific
Analysis of GPT vs. IBM Watson. In International Conference on Ubiquitous Com-
puting and Ambient Intelligence. Springer, 229–239.
[18] Jesse Chandler, Cheskie Rosenzweig, Aaron J. Moss, Jonathan Robinson, and
Leib Litman. 2019. Online panels in social science research: Expanding sampling
methods beyond Mechanical Turk. Behavior Research Methods 51, 5 (Oct. 2019),
2022–2038. https://doi.org/10.3758/s13428-019-01273-7
[19] David De Cremer, Nicola Morini Bianzino, and Ben Falk. 2023. How Generative AI
Could Disrupt Creative Work. (2023). https://hbr.org/2023/04/how-generative-
ai-could-disrupt-creative-work Section: AI and machine learning.
[20] Alberto Dafonte-Gómez. 2018. News Media and the Emotional Public Sphere
Audiences as Medium: Motivations and Emotions in News Sharing. International
Journal of Communication 12 (2018), 20.
[21] Mariano de Rivero, Cristhiam Tirado, and Willy Ugarte. 2021. FormalStyler:
GPT based Model for Formal Style Transfer based on Formality and Meaning
Preservation.. In KDIR. 48–56.
[22] Qi Deng, Michael J. Hine, Shaobo Ji, and Yun Wang. 2021. Understanding con-
sumer engagement with brand posts on social media: The effects of post linguistic
styles. Electronic Commerce Research and Applications 48 (July 2021), 101068.
https://doi.org/10.1016/j.elerap.2021.101068
[23] Qi Deng, Yun Wang, Michel Rod, and Shaobo Ji. 2021. Speak to head and heart:
The effects of linguistic features on B2B brand engagement on social media.
Industrial Marketing Management 99 (Nov. 2021), 1–15. https://doi.org/10.1016/j.
indmarman.2021.09.005
[24] Weiping Ding, Mohamed Abdel-Basset, Hossam Hawash, and Ahmed M Ali. 2022.
Explainability of artificial intelligence methods, applications and challenges: A
comprehensive survey. Information Sciences 615 (2022), 238–292.
[25] Rebecca Dolan, Jodie Conduit, Catherine Frethey-Bentham, John Fahy, and Steve
Goodman. 2019. Social media engagement behavior: A framework for engaging
customers through social media content. European Journal of Marketing 53, 10
(Jan. 2019), 2213–2243. https://doi.org/10.1108/EJM-03-2017-0182
[26] Duo Du, Yanling Zhang, and Jiao Ge. 2023. Effect of AI Generated Content
Advertising on Consumer Engagement. In International Conference on Human-
Computer Interaction. Springer, 121–129.
[27] Brooke Erin Duffy, Urszula Pruchniewska, and Leah Scolere. 2017. Platform-
Specific Self-Branding: Imagined Affordances of the Social Media Ecology. In
Proceedings of the 8th International Conference on Social Media & Society (#SM-
Society17). Association for Computing Machinery, New York, NY, USA, 1–9.
https://doi.org/10.1145/3097286.3097291
[28] Yunhe Feng, Pradhyumna Poralla, Swagatika Dash, Kaicheng Li, Vrushabh Desai,
and Meikang Qiu. 2023. The Impact of ChatGPT on Streaming Media: A Crowd-
sourced and Data-Driven Analysis using Twitter and Reddit. In2023 IEEE 9th Intl
Conference on Big Data Security on Cloud (BigDataSecurity), IEEE Intl Conference on
High Performance and Smart Computing, (HPSC) and IEEE Intl Conference on Intel-
ligent Data and Security (IDS) . 222–227. https://doi.org/10.1109/BigDataSecurity-
HPSC-IDS58521.2023.00046
[29] Dimitris C Gkikas, Katerina Tzafilkou, Prokopis K Theodoridis, Aristogiannis
Garmpis, and Marios C Gkikas. 2022. How do text characteristics impact user
engagement in social media posts: Modeling content readability, length, and
hashtags number in Facebook. International Journal of Information Management
Data Insights 2, 1 (2022), 100067.
[30] Anthony G. Greenwald. 1976. Within-subjects designs: To use or not to use?
Psychological Bulletin 83, 2 (1976), 314–320. https://doi.org/10.1037/0033-2909.
83.2.314
[31] Jeffrey T. Hancock, Kailyn Gee, Kevin Ciaccio, and Jennifer Mae-Hwah Lin. 2008.
I’m Sad You’Re Sad: Emotional Contagion in CMC. In Proceedings of the ACM
Conference on Computer Supported Cooperative Work (CSCW ’08) . ACM, 295–298.
[32] Valerie Hase, Karin Boczek, and Michael Scharkow. 2023. Adapting to affordances
and audiences? A cross-platform, multi-modal analysis of the platformization
of news on Facebook, Instagram, TikTok, and Twitter. Digital Journalism 11, 8
(2023), 1499–1520.
[33] Angelica Lermann Henestrosa, Hannah Greving, and Joachim Kimmerle. 2023.
Automated journalism: The effects of AI authorship and evaluative information
on the perception of a science journalism article. Computers in Human Behavior
138 (2023), 107445.
[34] Tim Highfield and Tama Leaver. 2016. Instagrammatics and digital methods:
studying visual social media, from selfies and GIFs to memes and emoji. Commu-
nication Research and Practice 2 (2016), 47 – 62. https://doi.org/10.1080/22041451.
2016.1155332
[35] Linda D. Hollebeek, Choukri Menidjel, Marko Sarstedt, Johan Jansson, and
Sigitas Urbonavicius. 2024. Engaging consumers through artificially intel-
ligent technologies: Systematic review, conceptual model, and further re-
search. 41, 4 (2024), 880–898. https://doi.org/10.1002/mar.21957 _eprint:
https://onlinelibrary.wiley.com/doi/pdf/10.1002/mar.21957.
[36] Carroll E. Izard. 1991. The Psychology of Emotions . Springer Science & Business
Media.
[37] Roope Jaakonmäki, Oliver Müller, and Jan Vom Brocke. 2017. The impact of
content, context, and creator on user engagement in social media marketing. In
Proceedings of the Annual Hawaii International Conference on System Sciences ,
Vol. 50. IEEE Computer Society Press, 1152–1160.
[38] Bernard Jansen. 2009. Understanding User-Web Interactions via Web Analytics.
Synthesis Lectures on Information Concepts, Retrieval, and Services 1 (2009), 1–102.
[39] Xiaoyan Jiang, Jie Lin, Chao Wang, and Lixin Zhou. 2024. How far is reality
from vision: An online data-driven method for brand image assessment and
maintenance. Information Processing & Management 61, 5 (2024), 103769. https:
//doi.org/10.1016/j.ipm.2024.103769
[40] Jaemin Jung, Haeyeop Song, Youngju Kim, Hyunsuk Im, and Sewook Oh. 2017.
Intrusion of software robots into journalism: The public’s and journalists’ per-
ceptions of news written by algorithms and human journalists. Computers in
human behavior 71 (2017), 291–298.
[41] Gideon Keren. 2014. Between-or within-subjects design: A methodological
dilemma. In A Handbook for Data Analysis in the Behaviorial Sciences . Vol. 1.
Psychology Press, 257–272.
[42] Jan Kocoń, Igor Cichecki, Oliwier Kaszyca, Mateusz Kochanek, Dominika Szydło,
Joanna Baran, Julita Bielaniewicz, Marcin Gruza, Arkadiusz Janz, Kamil Kanclerz,
et al. 2023. ChatGPT: Jack of all trades, master of none. Information Fusion (2023),
101861.
[43] Michal Kosinski, Sandra C Matz, Samuel D Gosling, Vesselin Popov, and David
Stillwell. 2015. Facebook as a research tool for the social sciences: Opportunities,
challenges, ethical considerations, and practical guidelines.American psychologist
70, 6 (2015), 543.
382

HT ’24, September 10–13, 2024, Poznan, Poland Kholoud Aldous, Joni Salminen, Ali Farooq, Soon-gyo Jung, and Bernard J. Jansen
[44] Michal Kosinski, David Stillwell, and Thore Graepel. 2013. Private traits and
attributes are predictable from digital records of human behavior. Proceedings of
the national academy of sciences 110, 15 (2013), 5802–5805.
[45] Adam D. I. Kramer, Jamie E. Guillory, and Jeffrey T. Hancock. 2014. Experi-
mental evidence of massive-scale emotional contagion through social networks.
Proceedings of the National Academy of Sciences 111, 24 (2014), 8788–8790.
[46] Mounia Lalmas, Heather O’Brien, and Elad Yom-Tov. 2014. Measuring User
Engagement. Synthesis Lectures on Information Concepts, Retrieval, and Services 6
(2014), 1–132.
[47] Mina Lee, Percy Liang, and Qian Yang. 2022. Coauthor: Designing a human-
ai collaborative writing dataset for exploring language model capabilities. In
Proceedings of the 2022 CHI conference on human factors in computing systems .
1–19.
[48] Michael Lewis, Jeannette M Haviland-Jones, and Lisa Feldman Barrett. 2010.
Handbook of emotions. Guilford Press.
[49] Fan Lu. 2024. Content Marketing Planning, Execution, and Mea-
surement. In Digital Content Marketing . Routledge, 13–30. https:
//www.taylorfrancis.com/chapters/edit/10.4324/9781003346500-2/content-
marketing-planning-execution-measurement-fan-lu
[50] Guixun Luo, Zhiyuan Zhang, and Sumeng Diao. 2022. Empirical analysis and
modelling social network user interaction behavior and time characteristics based
on selection preference. Information Sciences 608 (2022), 1202–1220.
[51] Renkai Ma. 2023. Conceptualizing and Rethinking the Design of Cross-platform
Creator Moderation. In Extended Abstracts of the 2023 CHI Conference on Human
Factors in Computing Systems (CHI EA ’23). Association for Computing Machinery,
New York, NY, USA, 1–4. https://doi.org/10.1145/3544549.3577049
[52] Renkai Ma, Xinning Gui, and Yubo Kou. 2023. Multi-Platform Content Creation:
The Configuration of Creator Ecology through Platform Prioritization, Content
Synchronization, and Audience Management. In Proceedings of the 2023 CHI
Conference on Human Factors in Computing Systems (Hamburg Germany, 2023-
04-19). ACM, 1–19. https://doi.org/10.1145/3544548.3581106
[53] N. Muhammad. 2019. An analysis to determine the most suitable type of multi-
media used on Facebook social media platform. International Journal of Advance
Research, Ideas and Innovations in Technology 5 (2019), 2146–2154.
[54] Taberez Ahmed Neyazi, Sheryl Wei Ting Ng, Mitchell Hobbs, and Audrey Yue.
2023. Understanding user interactions and perceptions of AI risk in Singapore.
Big Data & Society 10, 2 (2023), 20539517231213823.
[55] Itziar Oltra, Carmen Camarero, and Rebeca San Jose Cabezudo. 2022. Inspire me,
please! The effect of calls to action and visual executions on customer inspiration
in Instagram communications. International Journal of Advertising 41, 7 (2022),
1209–1234.
[56] Gregory Park, H Andrew Schwartz, Johannes C Eichstaedt, Margaret L Kern,
Michal Kosinski, David J Stillwell, Lyle H Ungar, and Martin EP Seligman. 2015.
Automatic personality assessment through social media language. Journal of
personality and social psychology 108, 6 (2015), 934.
[57] Mark J. Pelletier, Alexandra Krallman, F. Adams, and Tyler Hancock. 2020. One
size doesn’t fit all: a uses and gratifications analysis of social media platforms.
Journal of Research in Interactive Marketing (2020). https://doi.org/10.1108/jrim-
10-2019-0159
[58] Giulio Perrotta. 2022. Psychopathological profiles and trends of Italian social
network users (Facebook, Instagram, Twitter, and TikTok). Annals of Psychiatry
and Treatment 6, 1 (2022), 053–061.
[59] Kay Peters, Yubo Chen, Andreas M Kaplan, Björn Ognibeni, and Koen Pauwels.
2013. Social media metrics—A framework and guidelines for managing social
media. Journal of interactive marketing 27, 4 (2013), 281–298.
[60] Jeba Rezwana and Mary Lou Maher. 2022. Understanding user perceptions,
collaborative experience and user engagement in different human-AI interaction
designs for co-creative systems. InProceedings of the 14th Conference on Creativity
and Cognition. 38–48.
[61] Dmitri Rozgonjuk, Cornelia Sindermann, Jon D. Elhai, and Christian Montag.
2020. Fear of Missing Out (FoMO) and social media’s impact on daily-life and
productivity at work: Do WhatsApp, Facebook, Instagram, and Snapchat Use
Disorders mediate that association? Addictive Behaviors 110 (Nov. 2020), 106487.
https://doi.org/10.1016/j.addbeh.2020.106487
[62] Francesco Salvi, Manoel Horta Ribeiro, Riccardo Gallotti, and Robert West. 2024.
On the Conversational Persuasiveness of Large Language Models: A Randomized
Controlled Trial. https://doi.org/10.48550/arXiv.2403.14380 arXiv:2403.14380
[cs]
[63] Bruno Schivinski, George Christodoulides, and Dariusz Dabrowski. 2016. Mea-
suring Consumers’ Engagement With Brand-Related Social-Media Content: De-
velopment and Validation of a Scale that Identifies Levels of Social-Media En-
gagement with Brands. Journal of Advertising Research 56, 1 (March 2016), 64–80.
https://doi.org/10.2501/JAR-2016-004
[64] Donghee Shin. 2020. User Perceptions of Algorithmic Decisions in the Personal-
ized AI System:Perceptual Evaluation of Fairness, Accountability, Transparency,
and Explainability. Journal of Broadcasting & Electronic Media 64, 4 (Oct. 2020),
541–565. https://doi.org/10.1080/08838151.2020.1843357
[65] Andrew T Stephen, Michael R Sciandra, and Jeffrey J Inman. 2015. The effects
of content characteristics on consumer engagement with branded social media
content on Facebook. Marketing Science Institute Working Paper Series 15, 110
(2015), 1–51.
[66] Mingfei Sun and Shaojing Sun. 2024. Users’ engagement in WeChat-based support
communities: A multilevel perspective. Information Processing & Management
61, 2 (2024), 103604. https://doi.org/10.1016/j.ipm.2023.103604
[67] Briana M Trifiro and Jennifer Gerson. 2019. Social media usage patterns: Research
note regarding the lack of universal validated measures for active and passive
use. Social Media+ Society 5, 2 (2019), 2056305119848743.
[68] Risqo Wahid, Joel Mero, and Paavo Ritala. 2023. Written by ChatGPT, illus-
trated by Midjourney: generative AI for content marketing. 35, 8 (2023), 1813–
1822. https://www.emerald.com/insight/content/doi/10.1108/APJML-10-2023-
994/full/html Publisher: Emerald Publishing Limited.
[69] Xuena Wang, Xueting Li, Zi Yin, Yue Wu, and Jia Liu. 2023. Emotional intel-
ligence of large language models. Journal of Pacific Rim Psychology 17 (2023),
18344909231213958.
[70] Anja Wölker and Thomas E Powell. 2021. Algorithms in the newsroom? News
readers’ perceived credibility and selection of automated journalism. Journalism
22, 1 (2021), 86–103.
[71] Borchuluun Yadamsuren and Jannica Heinström. 2011. Emotional reactions to
incidental exposure to online news. Information Research 16, 3 (2011), 16–3.
[72] Chen Yang, Xiaohong Chen, Lei Liu, and Penny Sweetser. 2021. Leveraging
semantic features for recommendation: Sentence-level emotion analysis. Infor-
mation Processing & Management 58, 3 (2021), 102543. https://doi.org/10.1016/j.
ipm.2021.102543
[73] Fattane Zarrinkalam, Havva Alizadeh Noughabi, Zeinab Noorian, Hossein Fani,
and Ebrahim Bagheri. 2024. Predicting users’ future interests on social networks:
A reference framework. Information Processing & Management 61, 5 (2024),
103765. https://doi.org/10.1016/j.ipm.2024.103765
383
