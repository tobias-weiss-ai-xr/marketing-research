---
title: 'Monetizing Generative AI: YouTubers'' Collective Knowledge on Earning from Generative AI Content'
url: https://arxiv.org/abs/2603.07036
category: ai-marketing
subcategory: theory
date: 2026-03
venue: arXiv (Cornell University)
authors:
- Shuo Niu
- Yao Lyu
- He Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.07036
pages: 28
chars: 101067
fetched_at: '2026-11-08T13:19:28+00:00'
kb_version: 1
---

# Monetizing Generative AI: YouTubers' Collective Knowledge on Earning from Generative AI Content

Monetizing Generative AI: YouTubers’ Collective Knowledge on Earning from
Generative AI Content
SHUO NIU,Clark University, USA
YAO LYU,University of Michigan, USA
HE ZHANG,Pennsylvania State University, USA
NA LI,Pennsylvania State University, USA
BUMJIN KIM,Pennsylvania State University, USA
JIE CAI,Tsinghua University, China
Generative Artificial Intelligence (GenAI) is reshaping creative labor by enabling the rapid production of text, images, and videos. On
YouTube, creators are developing new ways to leverage these tools and share knowledge about how to pursue income through such
strategies. However, little is known about what GenAI knowledge has been collectively constructed around monetizing GenAI as a
community practice of acting both with and against algorithmically mediated platforms. We analyze 377 YouTube videos in which
creators publicly promote workflows, revenue claims, and monetization strategies for GenAI-enabled content. Our analysis identifies
ten shared use cases that frame AI-supported income opportunities, and examines how this GenAI knowledge repository embodies a
collective effort to leverage platform infrastructures for monetization – including advertising, direct sales, affiliate marketing, and
revenue-sharing models. We further surface structural tensions in AI-mediated creative labor, including unverifiable income claims,
content misappropriation, synthetic engagement practices, and shifting authorship norms. We conceptualize creators’ collective
understanding and adoption of GenAI in the context of monetizing creative labor, with implications for the design of creator-centered
GenAI technologies and responsible platform policy.
CCS Concepts:•Human-centered computing→Empirical studies in collaborative and social computing.
Additional Key Words and Phrases: Generative AI; AI ethics; YouTube; content creator; monetization; affiliate marketing; advertisement;
transaction; subscription
ACM Reference Format:
Shuo Niu, Yao Lyu, He Zhang, Na Li, Bumjin Kim, and Jie Cai. 2026. Monetizing Generative AI: YouTubers’ Collective Knowledge on
Earning from Generative AI Content. 1, 1 (March 2026), 28 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn
1 Introduction
Generative Artificial Intelligence (GenAI), including large language models (LLMs) and multimedia generation tools
[29, 35], is increasingly adopted by content creators. AI-generated content significantly influences creative work, social
connections within communities, and platform and market design for sustaining creators’ income. Content creators are
Authors’ Contact Information: Shuo Niu, shniu@clarku.edu, Clark University, Worcester, MA, USA; Yao Lyu, University of Michigan, Ann Arbor,
Michigan, USA, yaolyu@psu.edu; He Zhang, Pennsylvania State University, University Park, USA, hpz5211@psu.edu; Na Li, Pennsylvania State University,
University Park, USA, nzl5264@psu.edu; Bumjin Kim, Pennsylvania State University, University Park, USA, bqk5313@psu.edu; Jie Cai, Tsinghua University,
Beijing, Beijing, China, jie.cai@psu.edu.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not
made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components
of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on
servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
©2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Manuscript submitted to ACM
Manuscript submitted to ACM 1
arXiv:2603.07036v2  [cs.HC]  10 Mar 2026

2 Niu, et al.
increasingly sharing their GenAI tactics and strategies publicly, forming a body of collective knowledge about how
to adopt these tools increative labor[ 73] and increase revenue. While prior Human-Computer Interaction (HCI) and
social computing research has primarily examined the practices related to visibility work [8, 9, 28, 30, 79] and the use of
GenAI in the creative process [2, 29, 40, 53, 77], the emerging community-framed practices around adopting GenAI as a
tool for managing creative labor and navigating governance policies remain underexplored.
On the one hand, GenAI content appears across platforms such as YouTube, TikTok, Instagram, Medium, and
WordPress [40, 53, 61, 77, 86]. GenAI technologies can seamlessly convert text into a wide range of outputs, including
new texts, images, audio/speech, and videos [4], offering the potential to enhance both productivity and creativity. On
the other hand, GenAI content often lacks human connection [38], and its synthetic realism can be used to deceive
audiences [71] or misappropriate copyrighted content [36].
HCI and social computing research has examined how content creators collectively translate scattered experiences
into shared knowledge, including the management of creative labor and their informal theories of visibility work when
navigating recommendation and monetization systems [9, 14, 17, 28, 30, 57, 69, 84]. Analyzing such public discourses
helps inform platform and market design under algorithmic mediation, which shapes creators’ visibility and financial
security [45]. Creators typically earn income through three main approaches: affiliate marketing, ad revenue sharing,
and direct sales of merchandise [73, 84]. These monetization models are designed to reward and incentivize creative
labor that reflects human creativity and originality [46, 89]. Meanwhile, YouTubers must navigate tensions between
maintaining their integrity and generating income [30]. Researchers have identified exploitative practices aimed at
maximizing income, such as account trading, fake engagement, and content theft [16]. However, with the increasing
adoption of GenAI within the content creator community,little is known about creator-AI interaction from a
social science perspective, particularly regarding how GenAI is publicly framed as a viable monetization
pathway and how collective knowledge about GenAI affordances operates within or challenges existing
monetization infrastructures.
This research is motivated by conceptualizing the collective knowledge ofGenerative AI for Monetization (GenAI4Money)
– the publicly taught and circulated strategic uses of generative AI to produce income-generating content. We contribute
a content analysis of a specific yet influential segment of the creator ecosystem. Rather than measuring off-screen
GenAI interactions, these public demonstration videos represent a shared understanding of GenAI that reveals the
emerging workflows and the community’s underlying assumptions about using GenAI as a viable path to income.
Based on a social science theory [39], we triangulate the GenAI use cases, monetization models, and risky behaviors
discussed in these videos. Through this analysis, we aim to initiate broader conversations in HCI and social computing
about community-developed practices surrounding GenAI’s role in creative labor and platform infrastructures [73].
Specifically, we address three research questions:
• RQ1. What use cases do YouTube videos demonstrate for incorporating GenAI into content creation for moneti-
zation?
• RQ2. How do YouTubers’ publicly claimed GenAI4Money use cases align with existing monetization models on
social media platforms?
• RQ3. What challenges emerge from using GenAI in monetizing creative labor, and how are these challenges
related to the identified use cases?
Manuscript submitted to ACM

Generative AI for Monetization 3
We conduct a content analysis of 377 YouTube videos produced by 47 creators, in which they publicly demonstrate the
use of GenAI to monetize GenAI content. YouTube is the largest video-sharing platform with 65.3 million creators in 20251.
These videos exemplify how GenAI4Money strategies function both as forms of self-presentation by YouTubers and as
collective knowledge about media practices [18, 49]. Analyzing publicly shared videos is a well-adopted methodology
for understanding public knowledge formation [14, 19, 27, 28, 63] and for examining YouTubers’ participation in creative
labor and their management of relationships with algorithmic platforms [17, 57, 69]. As a result, we develop a conceptual
framework that illustrates key GenAI4Money knowledge and its impacts on both platforms and creators. Building
on this framework, we discuss three core trade-offs as design and policy implications to guide future HCI and social
computing research in this area.
2 Background
2.1 Monetizing Creative Labor
Content creators on YouTube pursue personal development and self-expression while blending entertainment with
aspirations for influence and monetization [10]. In social computing research, monetization is viewed as a central motive
shaping creators’ platform engagement [30]. Socio-technical research emphasizes how monetization mechanisms, as
part of the “infrastructure for inspiration, ” interact with creative practices [74, 88]. On the one hand, creative labor
theory argues that algorithmic recommendation and reward programs shape creators’ ostensive and performative
practices [73]. Creators continually recalibrate monetization expectations and work strategies in response to algorithmic
infrastructures [15]. On the other hand, creators also cope with and influence platform infrastructures, driving changes
in monetization models, moderation policies, and labor workflows [52, 65].
To generate revenue, creators refine their production skills and transition into professional uploaders [20]. Influencers
earn income through affiliate links, sponsorships, employment, fan support, revenue sharing, deal exchanges, and
knowledge monetization [84]. Creators care about their visibility within algorithmic recommendation systems, as
audience growth can directly influence revenue opportunities [7, 42]. Monetization programs reward desirable content,
incentivize creators to deliver value, foster entrepreneurial identities, and strengthen ties with platforms [3, 46]. To
maximize these benefits, creators adapt their content and distribute it across multiple platforms to expand monetization
opportunities [54]. Some creators directly collaborate with affiliate marketers by producing product review videos [32].
Another line of social computing research has examined how monetary incentives can produce negative consequences.
Some studies highlight that creators often prioritize financial gain over creative expression [15]. The struggle to balance
freedom of expression with economic pressure leads to stress, anxiety, and self-blame [45]. To increase visibility and
earnings, creators adapt their content to align with advertisers’ preferences [11, 15, 55]. Some engage in mass production
of trending content to maximize revenue [75]. Others fail to disclose affiliate marketing activities in their videos [59, 70].
Financial incentives have drawn sexual content creators to share explicit material [11].
Beyond incentivizing content production, research on social computing infrastructure has identified demonetization
(the restriction of content from generating revenue) as a central mechanism of content moderation. Demonetization
has been applied to penalize copyright violations [31], and content misaligned with advertisers’ preferences may also
be excluded from revenue opportunities [55]. Content moderation research in social computing research notes that
such practices are often perceived as punitive and opaque [56], producing visibility and income inequities [11, 26]. This
1https://www.demandsage.com/youtube-creator-statistics/
Manuscript submitted to ACM

4 Niu, et al.
frustration can lead to resistance within creator communities [1]. Some creators even exploit monetization systems
through harmful content, fake engagement, or content theft [16].
Monetization on platforms such as YouTube is a double-edged sword: it motivates some creators to increase production
while pressuring others to compromise self-expression to satisfy advertisers’ preferences. The rise of GenAI introduces
new tools that enable creators to experiment with new practices and reshape community heuristics for managing reach
and revenue [7].
2.2 Use of Generative AI in Content Creation
Generative AI (GenAI) refers to“artificial intelligence systems that can create new content, such as text, images, audio, or
video, rather than just analyzing or acting on existing data”[ 37]. Tools such as LLMs and diffusion models are capable of
producing high-quality digital content, as well as informal and emotional material [29, 35]. GenAI is increasingly adopted
to support creativity [41, 77, 90]. Online creators employ GenAI strategies such as workflow customization, cross-tool
experimentation, community learning, and ethical self-regulation [29, 77]. GenAI has been used to provide inspiration,
access video sources, and automate highlight generation [44]. It also facilitates content modality transformation, such
as converting text into platform-optimized videos [83].
Research has also examined the ethical challenges of GenAI in content creation and monetization. Nah et al. propose
a taxonomy of 16 challenges through which GenAI may negatively impact businesses and creators [ 34], including
the production of harmful or inappropriate content, over-reliance on AI, and copyright violations. Critics argue that
AI-generated content often appears mechanical and inauthentic, lacking emotional depth and human connection [38].
Creators may misuse GenAI to generate harmful or misleading material, and the GenAI itself may contain biases or
hallucinations [71]. The risk of creators becoming overly dependent on AI threatens to reduce originality and innovation
[48]. Furthermore, concerns have emerged regarding copyright infringement [76]. For example, GenAI models such as
DALL·E, Midjourney, and Stable Diffusion have been criticized for exploiting the labor of human artists [36]. While
these harms have been discussed in relation to their impact on human creators and creative work, there is limited
understanding of how monetization demand may actively drive such uses.
Another thread of research has examined the challenges posed by GenAI from the audience’s perspective. An-
thropomorphic features may foster parasocial relationships [72], and virtual AI avatars can enhance users’ sense of
connection [35, 50]. However, some users express strong aversion to the realism of AI avatars [72], citing concerns
about manipulation and a perceived lack of authenticity [58]. Skepticism also persists due to anxieties surrounding
misinformation, impersonation, and deceptive representations [35, 58, 60, 72]. Despite these insights, there remains
limited understanding of what forms of monetizable GenAI content are emerging as new norms of participation on
UGC platforms.
2.3 Creative Labor and the Infrastructural Influence of Generative AI
Simpson and Semaan definecreative laboras“the professionalization and monetization of social media content, involving
not just creation but also strategic navigation of platform demands, audience expectations, and technological systems”[ 73].
Contributing knowledge about GenAI4Money through public videos influences platform infrastructures and creative
labor in three key aspects [73]:creative expression,professionalization, andsocial connection.
Creative expressionrefers to the routines involved in producing influential content, which both shape and are
shaped by the algorithmic infrastructure that determines creators’ visibility [73]. On YouTube, creators must appear
authentic [20] and adapt their content to evolving audience tastes [5, 25], while strategically leveraging the platform as
Manuscript submitted to ACM

Generative AI for Monetization 5
a medium for transferring informal knowledge and hybridizing community practices [6, 14, 80]. Creators’ communal
expressions of creativity, shared through how-to videos and creative products [19, 27, 63, 80], function as peer-created
knowledge artifacts and forms of collective action that shape emerging community norms. These knowledge-sharing
videos have demonstrated educational value and constitute environments for informal learning [19, 23, 80]. The creative
process – including planning, production, uploading, and management [ 15, 44] – has also been turned into public
tutorials that teach creators how to maximize rewards through monetization [3, 46]. Recent studies further suggest that
GenAI may help alleviate aspects of this creative labor [15, 44].
Professionalizationrefers to creators achieving micro-celebrity status by developing technical and professional
expertise [20]. The tiered system that rewards different levels of professionalism is a central component of YouTube’s
monetization infrastructure [67]. Creators’ professionalization is strongly shaped by algorithmic recommendation
systems [79]. Creators share collective knowledge about algorithmic experiences, which translates scattered experiences
into shared heuristics for managing reach and revenue [7, 17]. Experienced creators also share strategies for increasing
visibility, helping others reduce algorithmic invisibility [9, 57]. These collective interpretations of YouTube’s algorithms
shape common strategies and concerns regarding platform governance [69]. The emergence of GenAI4Money may
therefore influence the three key monetization models –advertising,subscription, andtransaction[ 39]. These infras-
tructures [3, 24], traditionally shaped by algorithmic visibility, are now challenged by rapidly produced AI-generated
content and new GenAI-supported strategies for engaging with recommendation algorithms.
Social connectionin creative labor refers to the effort to connect with others and build community [ 73]. Creators’
learning, synthesizing, and public translation of ideas shape what knowledge is communicated within the community
and how it reaches viewers [ 28, 87]. However, other research has found that platform incentives influence what
knowledge is produced and circulated within the community [30]. Creators must maintain their identities and pursue
visibility by cultivating parasocial relationships and securing audience support [ 32, 85]. For creators who provide
services, sustaining such connections and managing impressions can impose significant emotional burdens [33, 62]. With
the integration of GenAI, it is therefore critical to examine how GenAI may translate these practices into problematic
forms of content creation (such as copyright infringement and harassment [78]), and how such content affects social
interactions between creators and fans.
In summary, the rise of GenAI introduces both efficiencies and potential transformations in creative labor. However,
comprehensive studies examining how content creators collectively form knowledge about GenAI in creative expression,
navigating monetization infrastructures, and building community connections remain largely absent from current HCI
and social computing literature. Drawing on the social media monetization models proposed by Hayes and Graybeal [39],
this study examines the collective knowledge shared through GenAI4Money videos, offering a conceptual understanding
of how GenAI is promoted by YouTube creators for monetization purposes.
3 Data Collection and Screening Process
We examine collective knowledge on GenAI4Money by analyzing YouTube videos created by content creators who
specialize in monetizing GenAI content. The analysis serves three main purposes. First, understanding this collective
knowledge reveals the symbolic actions surrounding GenAI use and explains how GenAI becomes collectively accepted
within socially and culturally embedded media practices [18, 49]. Such use cases may influence other creators’ content
production. Second, publicly shared demonstration videos provide a distinctive basis for understanding the new norms
that may emerge around GenAI use and the monetization of such content [18]. Third, this emerging body of knowledge
Manuscript submitted to ACM

6 Niu, et al.
about GenAI can inform platform governance and encourage improvements in monetization policies that support
healthy and ethical uses of GenAI.
The data collection and filtering process is illustrated in Figure 1. This process involved three steps. First, we collected
preliminary data to explore relevant video topics and identify effective search keywords. Second, we filtered for channels
that primarily focus on GenAI monetization and gathered their videos. Third, we sampled and selected videos that
explicitly address strategies for monetizing GenAI content.
Records identified from initial keyword extraction dataset: (n = 1,652 videos)
IdentificationScreeningEligibility
Additional records identified from large-scale video dataset: (n = 49,008 videos)
Records retained after filtering to English videos: (n = 9,987 videos)
Top 100 keywords extracted via double-ranking
Keywords refined through expert discussion
Records excluded that were not in English:
(n = 39,021 videos)
Channels associated with English videos: (n = 4,698 channels) Records excluded (n = 2,794 channels):
• Remove non-English channels;
• Remove corporate channels;
• Remove channels with no new videos in three months;
• Remove the 25% of channels with the fewest videos
Channels remaining after screening: (n = 1,904 channels) Channels sampled (600) and manually selected based on three criteria
Channels included after manually selection: (n = 47 channels)
Included
Videos retrieved from API between 01/01/2024 – 03/01/2024: (n = 3,897 videos)
Records excluded (n = 3,520):
• Remove videos that did not contain keywords related
to both “AI” and “monetization” in their titles,
descriptions, or tags
• Keep up to 20 videos per channel
Videos included in analysis:
(n = 377 videos)
Fig. 1. Data Collection and Screening Process Workflow
In the first step, we used the YouTube Data API2 to collect a sample of 1,652 videos to identify common terms related
to monetizing AI content. We searched for “AI Marketing, ” extracted tags of the videos, and applied a double-ranking
approach [82] to generate a keyword corpus. Four authors manually screened the top 100 keywords related to Gen AI
tools (e.g., ChatGPT, Midjourney) and monetization (e.g., affiliate marketing, passive income). These keywords were
then used to search a larger dataset of 49,008 videos from the YouTube API, published between December 1, 2023, and
March 1, 2024. Our initial review revealed that, besides tutorials on GenAI monetization, many videos focused on AI
news, business promotions of GenAI, general AI tool introductions without monetization, or personal opinions on AI’s
influence. We also observed that YouTubers tend to focus on similar topics across their channels [10]. Therefore, the
next step aimed to filter videos showcasing monetizing GenAI content from channels specialized in this topic.
In step 2, we extracted the list of channels from the videos in step 1 and programmatically excluded channels with
non-English characters in their names or descriptions, as well as company channels such as “Adobe, ” “Google Cloud, ”
and “Yahoo Finance. ” We then removed the 25% of channels with the fewest videos, as well as those without any videos
published in the past three months. From the remaining channels, we sampled 600 and manually evaluated them
based on the three criteria below. We focus on YouTubers who specialize in GenAI monetization because they are at
the leading edge of GenAI adoption. As video-creation skill-sharing is common within the YouTube community [13],
2https://developers.google.com/youtube/v3
Manuscript submitted to ACM

Generative AI for Monetization 7
leading YouTubers’ practices often reveal emerging monetization logics that may later diffuse across broader creator
communities. Two authors assessed each channel, resolving any disagreements through discussion. This process yielded
47 channels for step 3. All these channels met the criteria:
(1) Independent Content Creators: We included channels operated by independent creators and excluded those
affiliated with profit-making organizations, including AI companies, by verifying the channels’ profile pages.
(2) Focus on GenAI Content Creation and Monetization: We analyzed the titles, descriptions, and content of both
popular and recent videos. Channels were included only if more than half of their videos discussed both GenAI
and monetization.
(3) Language Criterion: We manually reviewed video content to confirm that only channels using English were
included.
In the third step, we collected all videos published by the selected channels between January 1 and March 1, 2024,
totaling 3,897 videos. We applied keyword-based filtering using the compiled list of relevant terms, including only
videos whose titles, descriptions, and tags contained keywords related to both “AI” and “monetization. ” We sampled
up to 20 videos per channel. Compared to complete random sampling, this approach ensured that we had sufficient
videos for analysis while also including content from smaller channels, thereby preventing the over-representation of
larger channels. After programmatic filtering, four researchers manually reviewed the videos, including only those
that provided instructions for creating AI-generated content (e.g., videos, images) and explicitly mentioned how the
content could be monetized. We excluded advertisements for AI tools that lacked walkthroughs or technical details.
Each video was annotated by at least two researchers, and any disagreements were resolved through discussion with
the four authors.
Our data collection process yielded 377 videos that form the corpus for our qualitative analysis. The videos were
produced by 47 channels, with each channel contributing an average of 2.89 videos (𝑆𝐷= 1.67). The average duration is
12.05 minutes. In total, they have accumulated 22,408,488 views, 875,838 likes, and 37,181 comments. All of the data are
publicly available, and we did not process any personally identifiable information; therefore, this research was reviewed
and exempted by the IRB.
4 Research Questions and Analysis Method
Our video analysis focuses on understanding the collective knowledge of GenAI in relation to the three monetization
models:advertisement,subscription, andtransaction[ 39]. We begin by examining the use cases publicly shared about
creating GenAI content for monetization (RQ1). Building on this foundation, we then investigate how these use cases
align with different monetization models (RQ2). To identify the unique challenges posed to content-sharing platforms,
we also annotate potential issues that arise when monetizing GenAI content (RQ3).
4.1 RQ1: Categorize GenAI4Money Use Cases
RQ1 categorizes the GenAI4Money use cases, identifying what GenAI knowledge has been developed for creative labor
and how it is strategically designed to maximize income generation. To address this question, we employed a grounded
theory approach [12], following three stages: open coding, axial coding, and selective coding. In the open coding stage,
we analyzed 200 videos (50 per author), taking notes on key concepts related to GenAI usage and the types of content
generated. During the axial coding phase, we identified relationships among these notes. Using affinity diagramming,
we collaboratively reviewed and grouped the use cases based on similar content types, resulting in 10 distinct categories.
Manuscript submitted to ACM

8 Niu, et al.
In the selective coding phase, we refined these categories through three rounds of annotation (30 videos per round, 90
videos in total) to improve category definitions and calculate inter-rater agreement. The finalized GenAI4Money use
cases are summarized in Table 1.
4.2 RQ2: Examine GenAI4Money Monetization Models
RQ2 examines how GenAI content is suggested for monetization based on Hayes and Graybeal’s theory of social media
monetization [39]. In this framework, theadvertisement modelgenerates revenue through ads, banners, or affiliate
marketing by directing traffic to advertisers. Thesubscription modelcharges users for access, often through a freemium
structure in which basic content is free while premium features are paywalled. Thetransaction modelgenerates income
through direct product or service sales from creators to consumers. In this study, we adopt these definitions and adapt
them to the context of YouTube (see Table 1) – specifically, we examine whether GenAI content redirects users to
advertisers, increases traffic to creators’ channels, or promotes products and services for viewers to purchase.
4.3 RQ3: Identify GenAI4Money Challenges
RQ3 investigates the challenges associated with GenAI4Money on content-sharing platforms. During our analysis
for RQ1, we also documented challenges related to GenAI knowledge by referencing the 16 issues identified by Nah
et al. [34]. Although Nah et al. ’s framework addresses the broader societal and business implications of GenAI, it
must be contextualized within content creation to provide a clearer understanding of the specific challenges faced
by creator communities. We adopted a similar coding approach as described in RQ1. We began by taking notes on
potential GenAI-related harms observed in the 200 videos, guided by [34], and identifying instances of statements and
usage demonstrations that exemplify the harm. We then used affinity diagramming to discuss emerging patterns and
inductively develop themes based on recurring patterns that appeared across multiple videos and were pertinent to
GenAI4Money. From this analysis, we identified four key GenAI4Money challenges that were prevalent in our dataset:
synthetic human activity,misappropriation,explicit content, andnon-verification(see Table 1 for definitions).
During independent data annotation, researchers examine the segments in which GenAI use is demonstrated and
review the GenAI actions and YouTubers’ verbal explanations that constitute evidence for each challenge category.
Forsynthetic human activity, we annotate whether the YouTuber showcases AI-generated realistic human figures or
language (e.g., comments or reviews) that are generally perceived as human activities. Formisappropriation, we mark
whether the YouTuber directly uses others’ textual, image, or video content as AI input to generate shareable content.
Forexplicit content, we evaluate whether the YouTuber presents that GenAI can produce violent or sexual material. For
non-verification, we annotate whether the YouTuber generates an entire knowledge- or information-based text and
directly uses it for content creation, without indicating any further validation or fact-checking.
4.4 Final Data Annotation
The finalized codebook is presented in Table 1. For all three research questions, we selected all applicable categories
for each video. In the final selective coding round involving 30 videos, we calculated inter-rater agreement using
Krippendorff’s alpha [47] with Jaccard distance. The resulting scores were 0.58 for GenAI4Money use cases (a lower
score due to the presence of 10 possible categories), 0.89 for monetization models, and 0.61 for GenAI challenges.
After finalizing the codebook, the three authors of this paper independently annotated a total of 287 videos (including
recoding the set of 200 videos used for initial exploration and the remaining 87 videos) divided among them.
Manuscript submitted to ACM

Generative AI for Monetization 9
Category Definition
Use Case
Blog Write or rewrite blogs, microblogs, or online articles with tools like ChatGPT.
E-book Create e-books with GenAI and sell on e-book marketplace like Amazon.
Graphic Design Use tools like Midjourney or Leonardo.AI to create merchandise, stock images, or products (e.g.,
T-shirts, stickers, cover designs, coloring books, print-on-demand).
Influencer Create a social media account with AI-generated human photos.
Newsletter Write emails, Facebook ads, or newsletters with tools like ChatGPT or Gemini.
Product Promotion Video Create AI videos directly promoting products or services.
SEO Optimize titles, tags, or descriptions with GenAI tools to improve search engine rankings.
Trending Video Create AI videos related to public interests or educational topics.
Video Reformatting Reformat videos for multiple platforms or diversify audiences (e.g., create short-form videos or
translate them into different languages).
Web Design Use AI-generated code or templates to design or create websites.
Model
Advertising The video mentions adding links to GenAI content to earn money from affiliate advertisers.
Subscription The video mentions publishing GenAI content to earn through revenue-sharing programs.
Transaction The video mentions selling AI-generated products or offering freelancing services using GenAI.
Challenge
Synthetic Human
Activity
The video demonstrates using GenAI to create content simulating real people’s activities, such as
realistic human figures or users’ comments and reviews.
Misappropriation The video shows the modification of others’ original content (e.g., videos or blogs) in GenAI creations.
Explicit Content The video shows using GenAI to create violent, offensive, or erotic content.
Non-Verification The YouTuber demonstrates using GenAI to generate entire pieces of knowledge or information
without further editing or validation.
Table 1. Descriptions and definitions of GenAI4Money use cases, models, and challenges.
5 Results
The names, counts, and percentages of videos in each category are presented in Figure 2. We conducted a Chi-square
test to examine the relationships among models, challenge categories, and the 10 use cases (𝛼= 0.05, with Bonferroni
correction). Statistically significant associations are visualized in Figure 3.
Trending Video
Blog
Graphic Design
Product Video
SEO
E-Book
Newsletter
Web Design
Other
Reformatting
Influencer
0
50
100
150
200
250Video #
106
28.1% 94 24.9% 85 22.5% 49
13.0% 37 9.8% 30 8.0% 25 6.6% 23 6.1% 21 5.6% 18 4.8% 14 3.7%
Use Case
Advertisement
Transaction
Subscription
181
48.0% 149
39.5%
93
24.7%
Model
Non-Verification
Misappropriation
Synthetic Human
Activity
Explicit Content
125
33.2%
34
9.0% 19 5.0% 2
0.5%
Challenge
Fig. 2. The distribution of YouTube videos in each use case, model, and challenge subcategory.
5.1 RQ1: GenAI4Money Use Cases
5.1.1 Trending Video.The most common use case demonstrated in the knowledge videos involves creating trending
videos with GenAI technologies (𝑁= 106, 28.1%). YouTubers build knowledge around how to use AI tools such as
ChatGPT to generate video scripts, synthesize voice through text-to-speech technologies, and create visuals using
Manuscript submitted to ACM

10 Niu, et al.
79 45 196
85 2711
8
8
78 13
5149 5
10 7
79
45
19
85
27
78
13
51
49
7 10
Fig. 3. Associations among monetization use cases, models, and ethical issues. Numbers indicate the video counts that contain both
categories.
AI-generated or stock footage, all to produce content that can generate revenue through monetization programs.
YouTubers often suggest video niches that can be efficiently produced using various AI tools. These niches cover general
knowledge (e.g., health, travel, pets), entertainment (e.g., children’s stories), or inspirational quotes (e.g., celebrity or
motivational quotes). For example, the video shown in Figure 4a introduces 14 niche ideas suited for AI-generated
videos, such as country/city guides, productivity tips, and spirituality. YouTubers often suggest the potential of using
GenAI to produce various forms of “faceless, ” anonymous content. Figure 4b illustrates a kid short story in which the
script is generated by Google Bard and the images are produced by Leonardo.AI; these materials are then assembled
into a Disney-style video for children. Many of these videos conclude by introducing monetization opportunities – such
as the TikTok Creativity Program or the YouTube Partner Program (Figure 4c).
(a) Travel is one of the popular video
“niches. ”
(b) A kid story video created with
Leonardo.AI.
(c) TikTok creativity program for monetiza-
tion.
Fig. 4. Examples of monetization using AI-generated trending videos.
5.1.2 Blog.Writing blogs with GenAI is another popular suggested use case ( 𝑁= 94, 24.9%). YouTubers develop
knowledge about monetizing AI-generated blogs, product reviews, and posts on social Q&A sites. Many highlight that
GenAI blogs can embed affiliate links and optimize search engine rankings (SEO). AI tools such as ChatGPT and Jasper
AI facilitate the quick creation of product demonstrations, engaging content, and personalized suggestions to attract
customers. For example, Figure 5a demonstrates how to create a blog related to muscle building and insert a link to a
seller’s website for a legal steroid product. Some YouTubers recommend using GenAI to answer related questions on
Quora by writing an article with Google Bard while embedding product links (Figure 5b). Additionally, some creators
mention that they can sell their GenAI blog writing as a service on platforms like Fiverr (Figure 5c).
Manuscript submitted to ACM

Generative AI for Monetization 11
(a) Use ChatGPT to write a blog related to
muscle building.
(b) Write Quora answer with Google Bard.
 (c) Offer AI SEO blog writing on Fiverr.
Fig. 5. Examples of monetization using AI-generated blogs.
5.1.3 Graphic Design.A subset of YouTubers ( 𝑁= 85, 22.5%) share GenAI methods about creating graphic designs for
sale as printable products or digital stock. These merchandise items includes T-shirts, stickers, book covers, coloring
books, stock images, and clipart. Creators frequently demonstrate GenAI knowledge about tools such as DALL·E,
MidJourney, and Stable Diffusion, which transform text prompts into visual AI-generated content. These graphics are
subsequently sold either as digital downloads or through handcraft marketplace platforms such as Etsy (Figure 6a).
Many YouTubers emphasize the importance of tracking and aligning with current design trends to increase sales. Theses
strategies often involve analyzing top-selling products for inspiration, inputting relevant keywords into GenAI tools
to generate new visuals, and producing them through print-on-demand services. For example, one YouTuber utilizes
Alura to analyze popular Etsy designs and uses MidJourney to create similar T-shirt graphics (Figure 6b). Figure 6c
presents an example of print-on-demand services used to apply GenAI designs onto mugs.
(a) Monetizing by selling AI art on Esty.
 (b) Generate designs with MidJourney.
 (c) Mugs with AI-generated design for sale.
Fig. 6. Examples of monetization using AI-generated graphic designs.
(a) Get product info on Digistore24.
 (b) Create human avatar on Synthesia.
 (c) An AI-generated software review video.
Fig. 7. Examples of monetization with AI-generated promotion videos.
Manuscript submitted to ACM

12 Niu, et al.
5.1.4 Product Promotion Video.Out of 377 videos, 49 (13.0%) focus on introducing how to create product promotion
videos to viewers. This use case illustrates how YouTubers develop new ways to use GenAI to directly promote products.
Similar to the creation of trending videos, YouTubers share practices using ChatGPT to generate product description
scripts, image-generating tools to produce visuals, and AI voices for voiceovers. However, unlike videos centered
on general trending topics, these promotional videos emphasize identifying profitable affiliate links and converting
product descriptions into engaging video content. For instance, one YouTuber demonstrates making a video promoting
fitness-related products. They use ChatGPT to brainstorm content ideas and identifies affiliate products on Digistore24
(Figure 7a). They then draft scripts with ChatGPT that include product details and avatar-based narratives, and employs
Synthesia to create an AI talking avatar to present the product (Figure 7b). YouTubers often recommend publishing
these videos on platforms such as YouTube, TikTok, and Instagram to maximize reach. Some videos are styled as
product reviews or personal experiences. For example, certain creators suggest using GenAI to generate product reviews,
embedding affiliate links within the video descriptions (Figure 7c).
5.1.5 SEO.YouTubers suggest using GenAI for search engine optimization (SEO) with social media content ( 𝑁=
37, 9.8%). This use case highlights how GenAI-based SEO tools help creators optimize content with search-friendly
keywords to boost visibility in search engines and recommendation algorithms. For many creators, gaining greater
exposure to online audiences is essential for monetization. Tools like ChatGPT, SurferSEO, and Jasper AI are commonly
introduced for this purpose. SEO applies to various content formats, including blogs and video descriptions. For example,
one YouTuber demonstrates how to use VidIQ to identify relevant keywords for a promotional video (Figure 8).
Fig. 8. Get SEO keywords list using ChatGPT.
5.1.6 E-Book.Some YouTubers ( 𝑁= 30, 8.0%) share knowledge about how to write e-books using GenAI. They explain
how tools like ChatGPT can generate book ideas, develop chapters, and even create complete content. For example, one
video shows how to use AI to create children’s e-books. The creator uses ChatGPT to generate story ideas, outlines,
chapter content, and the book cover design (Figure 9a). They then use Leonardo.AI to create illustrations based on the
story prompts (Figure 9b). YouTubers often claim that these ebooks can be sold via Kindle Direct Publishing (KDP)
programs.
5.1.7 Newsletter.Videos highlight the use case of creating newsletters to generate income ( 𝑁= 25, 6.6%). These
newsletters – typically distributed via email or social media ads – allow content creators to generate revenue by
promoting their own channels or those of affiliate marketers. Creators show how to use tools like ChatGPT to
brainstorm, generate, automate, and edit engaging newsletters that attract customers. One example shows a YouTuber
using ChatGPT to create email newsletters (Figure 10). They feed ChatGPT video transcripts and business details,
Manuscript submitted to ACM

Generative AI for Monetization 13
(a) Create text content using ChatGPT.
 (b) Generate images for e-book using Leonardo.AI.
Fig. 9. Examples of monetization using AI-powered e-books.
generating personalized content with matching tone, subject lines, and preheader text. These AI-generated newsletters
are often better formatted and more visually appealing, making them more effective for sharing YouTubers’ updates or
small business news.
Fig. 10. Write customized newsletter with ChatGPT.
5.1.8 Web Design.Creating websites is another use case demonstrated in the videos to generate income ( 𝑁= 23, 6.1%).
These videos build knowledge about how to design websites for affiliate marketing, including web logic, frameworks,
and content, using GenAI. Tools like MidJourney are used for website design, and some creators also use platforms like
Mixo.ai to build websites from scratch (Figure 11). For example, one YouTuber shows how Mixo.ai generates websites
for mobile games from a simple prompt, providing both content and images. They also use ChatGPT to create game
descriptions and articles. The website is later used to promote mobile games and earn a commission.
Fig. 11. Create websites with Mixo.
Manuscript submitted to ACM

14 Niu, et al.
5.1.9 Video Reformatting.A smaller group of YouTubers ( 𝑁= 18, 4.8%) showcase using GenAI to reformat existing
content. They demonstrate how these tools can clip, translate, and mimic styles, facilitating content sharing across
platforms and language barriers. While some creators transform their own content for knowledge explanations, others
imply using content from other creators while attempting to avoid copyright infringement. For example, one creator
suggests downloading videos from TikTok, YouTube, and Instagram in Chinese, transcribing and translating them with
Oris AI, and rewriting scripts using ChatGPT (Figure 12). New voiceovers are generated with Eleven Labs. Some videos
present this use case as a way to inspire creators to repurpose their own content. However, others suggest that GenAI
can be used to modify others’ content for publication on one’s own channel.
Fig. 12. Reformatting a video in a different language.
5.1.10 Social Media Influencer.A few YouTubers ( 𝑁= 14, 3.7%) share a use case for creating virtual influencers on
social media platforms using GenAI. Using GenAI tools to create influencers involves designing virtual avatars with
attractive personalities or professional knowledge to attract a fan base. For example, one YouTuber selects HeyGen
AI to access pre-made avatars, including human-like profiles and realistic environment settings (e.g., an office). They
then uses HeyGen’s text-to-video feature to input video scripts, which are transformed into complete videos with
AI-generated voice-overs and lip-syncing (Figure 13a). In another video, a YouTuber suggests creating a hyper-realistic
AI influencer with Leonardo.AI to promote products (Figure 13b).
(a) Create influencer avatar with HeyGen.
 (b) Create an AI influencer with Leonardo.AI.
Fig. 13. Examples of monetization using AI-generated influencers.
Manuscript submitted to ACM

Generative AI for Monetization 15
5.2 RQ2: GenAI4Money Models
We categorized how creators build knowledge and develop practices for using GenAI to influence the monetization
models ofAdvertisement,Subscription, andTransaction[ 39]. This section discusses these monetization models and their
associations with the identified use cases (Figure 3).
5.2.1 Advertisement.Advertisement is the most frequently mentioned monetization model, appearing in about half of
the videos (𝑁= 181, 48.0%). In our study, the advertisement model refers to using AI-generated content to direct users
to affiliate links and earn profits from the product marketer. The Chi-square analysis indicates a significant positive
association between theAdvertisementmodel andBlog( 𝜒 2 = 65.13,𝑝< 0.001),Product Promotion Video( 𝜒 2 = 43.34,
𝑝< 0.001), andWeb Design( 𝜒 2 = 11.75,𝑝< 0.001) use cases, suggesting that these forms of AI-generated content are
better suited for this monetization model.
(a) Get promotion link on Passively.com.
 (b) Add links under AI videos on YouTube.
Fig. 14. Examples of monetization in the advertisement model.
In theBloguse case, YouTubers recommend affiliate marketplaces such as Clickbank.com, Amazon Associates, and
ProfitPassively.com for earning commissions (e.g., Figure 14a) and embedding affiliate links in blog content. Similarly,
Web Designvideos use AI-generated blogging templates to build affiliate marketing websites and link them to product
promoters. TheProduct Promotion Videouse case also features various affiliate marketplaces, but typically involves
creating videos styled as buying guides or customer reviews. In these cases, affiliate links are often embedded in the
video description (Figure 14b).
Videos in the GenAI4Money model indicate that GenAI tools are framed as an efficient means of creating content
tailored to specific product types and designed to attract viewers – ultimately encouraging clicks on embedded affiliate
links and generating commissions. This model positions GenAI as an attention-capturing tool, where seemingly plausible
and detailed online content, aligned with users’ “niche interests, ” is generated by AI to serve as a hook that redirects
potential traffic to affiliate link URLs.
5.2.2 Transaction.The transaction model, the second most publicly taught strategy in the videos, accounts for over
one-third of the sample (𝑁= 149, 39.5%). In this model, creators suggest practices of selling products made with GenAI
or offering services facilitated by GenAI, enabling them to earn profits directly from customers [39]. The Chi-square
test indicates that this model is significantly associated with theGraphic Design( 𝜒 2 = 167.93,𝑝< 0.001) andE-Book
(𝜒 2 =34.75,𝑝<0.001) use cases.
In theGraphic Designuse case, YouTubers teach how to use AI tools to create digital or merchandise products for
direct sale on platforms such as Etsy, Redbubble, Amazon, and Shopify. Some also recommend offering freelance services
Manuscript submitted to ACM

16 Niu, et al.
or gig work on platforms like Fiverr. For example, one YouTuber illustrates how to profit from digital art by showcasing
watercolor clipart sales and using MidJourney to generate similar content for Etsy (Figure 15a). Similarly, creators can
use AI tools to writeE-Books, even without subject-matter expertise, and sell them through digital publishing platforms
like Kindle or as physical prints on Amazon (e.g., Figure 15b).
GenAI is introduced as a design tool, while print-on-demand services facilitate the production of AI-generated
paintings and e-books. Use cases within this GenAI4Money model often publicly promote such GenAI products as
“creative work” on platforms originally designed for creative professionals (e.g., Etsy) or independent authors (e.g.,
Kindle Direct Publishing).
(a) Sell AI-generated designs on Esty.
 (b) Sell an GenAI storybook on Kindle Direct Publish-
ing.
Fig. 15. Examples of monetization in the transaction model.
5.2.3 Subscription.Around one-fourth of the sampled videos share knowledge about using GenAI for theSubscription
model (𝑁= 93, 24.7%). In this monetization model, YouTubers generate revenue through paid memberships or revenue-
sharing programs offered by social media platforms. These GenAI4Money techniques focus on the mass creation and
uploading of GenAI content, noting that creators can potentially earn cumulative income. A Chi-square test reveals
significant associations between theSubscriptionmodel and the use cases ofTrending Video( 𝜒 2 = 189.88,𝑝< 0.001)
andReformatting(𝜒 2 =23.00,𝑝<0.001).
(a) YouTuber’s subscription rate and income.
 (b) A YouTuber suggests modifying and sharing pop-
ular videos.
Fig. 16. Examples of monetization in the subscription model.
Creators demonstrate AI tools such as ChatGPT and InVideo AI to generateTrending VideosorReformatexisting
content. These use cases often align with trending topics to optimize chances of being recommended by algorithms,
Manuscript submitted to ACM

Generative AI for Monetization 17
thereby increasing traffic and revenue. For example, one video shows a narrator using GenAI to create a YouTube
channel with numerous simply made AI videos and displaying the earnings achieved (Figure 16a). In aReformatting
example, a creator monitors uploads from popular channels and uses GenAI to produce short versions, which are then
uploaded to a different channel for monetization (Figure 16b).
The subscription-based GenAI4Money model illustrates how creators develop new practices that leverage GenAI to
produce videos with greater potential for popularity. Techniques include aligning GenAI content with trending topics on
video-sharing platforms or adapting already popular content. These practices reflect how platform monetization models
influence creators’ content choices and their intent to increase viewership and subscriptions through the strategic use
of GenAI.
5.3 RQ3: GenAI4Money Challenges
For RQ3, we annotate four challenges and analyze the associations between GenAI4Money use cases and the three
most common challenge categories within the collective GenAI4Money knowledge (Figure 3).
5.3.1 Non-Verification.Non-verification is the most common challenge type ( 𝑁= 125, 33.2%). In the demonstration,
YouTubers often demonstrate excessive trust in the answers provided by GenAI [ 34], relying on these AI tools as
experts to generate complete content or suggestions without further validation. Chi-square analysis reveals significant
associations between this ethical subcategory and the use cases ofTrending Video( 𝜒 2 = 11.37,𝑝< 0.001) andBlog
(𝜒 2 =25.15,𝑝<0.001).
In theTrending Videouse case, YouTubers often show using LLM-recommended topics without regard for their
own expertise in the niche (e.g., health, pets, travel). Educational and how-to videos may rely entirely on scripts
generated by GenAI. For example, in Figure 17a, a YouTuber demonstrates how to use ChatGPT to script a short-form
video about honey and mixed fruit that introduces their nutritional benefits, which we annotate as demonstrating the
non-verification challenge because the entire knowledge-based script was generated by ChatGPT without checking.
Similarly, in theBloguse case, creators demonstrate how GenAI can generate complete blog posts that include both
AI-produced text and images, as illustrated in Figure 17b.
Such use of GenAI for social media content demonstrates over-reliance on AI-generated material, which can be
inaccurate or misleading. Creating content with GenAI may result in content creators passing on AI mistakes or errors
to viewers through AI-generated blogs and videos.
(a) Generate script on food with ChatGPT.
 (b) Write review on a book with ChatGPT.
Fig. 17. Examples of the non-verification challenge.
Manuscript submitted to ACM

18 Niu, et al.
5.3.2 Misappropriation.In our data, 34 videos (9.0%) exhibit traits where original content created by others, which
could be protected under copyright laws and regulations, is used as input for GenAI. Chi-square tests reveal significant
associations with theReformatting(𝜒 2 =49.89,𝑝<0.001) andInfluencer(𝜒 2 =29.76,𝑝<0.001) use cases.
YouTubers present methods for modifying and repurposing content created by others, then presenting the results as
their own. For example, one YouTuber demonstrates how to build a faceless channel by producing trending videos in the
“Put Your Fingers Down” niche (a popular TikTok trend, shown in Figure 18a). This video is a case of misappropriation
because the creator mentions using visual content composed of clips taken from others’ original videos, whereas
they use ChatGPT to transform the scripts and incorporate AI-generated voiceovers. In anotherInfluencerexample, a
YouTuber advises using others’ images to prompt ChatGPT and then combining the resulting AI-generated text and
images to launch an Instagram account focused on workouts (Figure 18b).
In the GenAI4Money context, the profit-driven repurposing of others’ content may undermine original creators’ rights
and diminish their opportunities for visibility and popularity [34]. GenAI is often presented as a tool for circumventing
copyright restrictions. YouTubers frequently publicly assert that GenAI sufficiently transforms the content to avoid
copyright strikes under YouTube’s content moderation policies.
(a) Modifying the “Put Your Fingers Down” video.
 (b) Use ChatGPT to convert online images to a Insta-
gram post.
Fig. 18. Examples of the misappropriation challenge.
5.3.3 Synthetic Human Activity.We identified 19 videos (5.0%) demonstrating GenAI being used to fabricate human
activities. This knowledge refers to prompting GenAI to generate images or videos that mimic real people, real-world
scenes, or human comments. For example, one YouTuber demonstrates how to promote a pet product using an AI-
generated website. We annotate this video as containing this challenge because the YouTuber adds fake customer
reviews generated by ChatGPT, including AI-generated profile pictures and names (Figure 19a). In another example, a
YouTuber uses a virtual AI avatar to create an online course and claims that the avatar behaves like a human instructor,
with the intent of uploading it to platforms such as Udemy to generate income (Figure 19b).
In this challenge, GenAI content fosters a sense of trustworthiness by generating vivid, real-world personas, scenes,
and speeches. Such uses may mislead users into perceiving the content as authentic. AI-generated reviews illustrate
how GenAI is employed as a credibility-enhancing tool. However, this type of content can constitute misinformation
that deceives other users [34].
5.3.4 Explicit Content.In our data, only two videos include explicit content (0.5%), both of which involve generating
sexualized AI-generated images of women. In one example, a YouTuber demonstrates how to create an AI avatar and
perform a face swap. This video is annotated as explicit content because the face-swapping source comes from a Discord
Manuscript submitted to ACM

Generative AI for Monetization 19
(a) Fake reviews on a product page.
 (b) An AI avatar is used to teach a lesson.
Fig. 19. Examples of the synthetic human activity challenge and the explicit content challenge.
channel containing numerous explicit, semi-naked female images, and the YouTuber further suggests that such an
AI-generated figure can be used for the Tinder dating app (Figure 20).
Fig. 20. Create AI figure and swap faces.
6 Discussion
Our analysis reveals the knowledge space formed around GenAI usage for monetization, highlighting discourse
surrounding creative labor and platform governance. Ultimately, we present a conceptual framework (Figure 21) that
delineates six key GenAI4Money knowledge areas developed and shared within the YouTuber community.
Originality Incentive
Platform
Platform Visibility
Aﬃliate Marketer
opportunistic creation
GenAI
Identity Non- disclosure
Audience Interest
Creativity Recognition
Creator
de- laboriﬁcation
expertise faking
creativity faking
trend alignment
attention redirection
GenAI4Money Activities
inﬂuence
inﬂuence
Fig. 21. A framework summarizing the collective knowledge of GenAI4Money and its effects on platforms and communities.
Manuscript submitted to ACM

20 Niu, et al.
6.1 GenAI4Money Influences Algorithmic, Monetization, and Moderation Infrastructures
6.1.1 GenAI-Driven Opportunistic Creation for Originality Incentives.Our results indicate that YouTubers develop GenAI
knowledge aroundopportunistic creationpractices to profit from social media platforms. In contrast to findings in prior
HCI research, which emphasize AI’s benefits in streamlining creative expression and production pipelines [15, 44, 73],
some YouTubers instead build knowledge around using GenAI as a shortcut to bypass the creative labor necessary
for authentic expression [5]. These practices are particularly evident in demonstrations of mass-produced videos with
GenAI, the reformatting of others’ content for misappropriation, and the generation of entire video scripts without
verification.
The knowledge of GenAI4Money activities around opportunistic creation calls for rethinking how originality-
promotion programs and infrastructures should be reshaped in the age of GenAI. HCI research on “infrastructures for
inspiration” has noted that monetization programs function as sociotechnical and community structures that support
creative identities [74]. Such programs have been found to motivate creators to enhance production skills [ 20] and
foster professionalism [66]. However, our findings suggest that opportunistic creation may instead be amplified by
the ease of producing plausible GenAI content, thereby exploiting incentive programs such as the YouTube Partner
Program and TikTok Creator Rewards. In our analysis, GenAI graphics and e-books are marketed as original works on
platforms such as Etsy and Kindle Direct Publishing.Trending videoandReformattingpractices are strongly associated
with the subscription model, whereasGraphic DesignandE-Bookcreation align more closely with the transaction
model. While prior social computing research has noted that monetization programs encourage high-status creators to
contribute and improve overall content quality [46, 89], our findings suggest that, conversely, the involvement of GenAI
may have the opposite effect, undermining authenticity and diminishing content quality on social media platforms.
These dynamics should prompt platforms to redesign their monetization policies and infrastructures [65, 88].
6.1.2 GenAI for Trend Alignment and Platform Visibility.While the visibility of content has been identified as a critical
concern for creators [ 7, 42], our findings suggest that, as a new form of collective effort in response to platforms’
algorithmic management [7, 9, 57], creators are building new practical knowledge and heuristics [17] for using GenAI
in visibility work. Such knowledge oftrend-alignmentmay help other creators boost their professionalism and visibility
on the platform. Creators demonstrate GenAI-supported media practices through which they identify content ideas that
align with trending topics and algorithmic preferences across platforms. Use cases within subscription models – such as
identifying video topics with GenAI and reformatting content for cross-platform sharing – illustrate how such GenAI
knowledge is used to generate content with high popularity potential. Some creators also demonstrate how to rely on
GenAI to produce SEO-optimized titles and tags or to automate newsletters for strengthening audience relationships.
Social computing research has noted that creators appropriate and cope with infrastructures such as algorithmic
recommendation systems and monetization policies [30, 52, 88]. Creators’ knowledge of trend-alignment with GenAI
represents a new pathway for making sense of how algorithms work and for attempting to work with algorithmic
governance [69, 79]. This new practice introduces both positive and negative dynamics into professional infrastructures.
On the positive side, creators frame GenAI as a novel affordance for adapting to platform preferences and advertiser-
friendly formats [55, 64]. GenAI is taught as a means to research audience interests and respond to such demand [45].
On the other hand, theories of algorithmic creative labor have shown that YouTube’s recommendation and monetization
algorithms pressure creators to shift away from their original interests in favor of algorithmic preferences [11, 46, 55].
Extending these findings, our analysis shows that GenAI-driven trend analysis may further compel some creators to
sacrifice personal distinctiveness, intensifying the risk of content homogenization [21].
Manuscript submitted to ACM

Generative AI for Monetization 21
6.1.3 GenAI for Attention Redirection and Deception.We find that some creators build knowledge around using GenAI
as a powerful tool to supportattention redirection, thereby directing users toward embedded affiliate marketing links.
Prior studies have noted that undisclosed affiliate marketing activities within user-generated content have created
tensions between creators and audiences [59, 70]. Extending these concerns, our study reveals the circulation of GenAI
knowledge about how to review products in videos, write ad-embedded blogs, answer questions on Q&A platforms, and
build AI-generated websites – often with undisclosed intentions of redirecting users to affiliate links. The advertisement
model is particularly associated with use cases such asBlog,Product Video, andWeb Design. These practices introduce
a new practice of endorsement, in which GenAI is leveraged to rapidly generate potentially trending content and
monetize through affiliate marketing.
This GenAI4Money modality within creators’ communities contrasts significantly with previously documented
endorsement behaviors [59], in which creators primarily added affiliate links within their creative work. GenAI may
therefore shift the relationship and norms between creators and affiliate marketers, as creators’ GenAI-driven practices
often occur outside the direct oversight of marketers. The proliferation of low-quality GenAI content may lead to
audience aversion and perceptions of inauthenticity [58, 72]. GenAI advertisements can further undermine user trust
and diminish engagement [22]. When affiliate links are embedded in low-quality GenAI content to redirect viewers’
attention, they may inadvertently harm marketers’ businesses. Furthermore, such practices can disadvantage creators
who invest in producing authentic product reviews or sponsored content [32].
6.2 GenAI4Money Influences Content Creation and Creative Labor
6.2.1 Creativity De-laborification through Identity Non-disclosure.Our results suggest that many creators frame GenAI
as a device for reducing the labor (de-laborification) associated with publicly disclosing their identities on social media.
Addressing creators’ intensive social and emotional burdens has been a central focus of social computing research on
content-sharing platforms [33, 62, 73, 78]. Our findings highlight GenAI’s potential to ease these demands through
what creators in our data frequently describe as the creation of “faceless” content or “faceless” channels. Such GenAI
media practices enable monetization without the need to manage a public identity. This knowledge may therefore trend
toward new content production practices centered on the benefits of identity concealment, offering an alternative form
of publicity that does not require creators to manage their public identities [20, 43].
While GenAI is regarded as a new community practice for reducing creative labor, it may simultaneously diminish
professionalism and social connection [73]. In creative labor, sharing knowledge has traditionally formed informal
learning spaces and helped improve authority, expertise, and community cohesion [14, 19, 63, 80]. While YouTubers
often intend to balance the goals of money-making and supporting informal learning [23, 30], the GenAI knowledge
shared in our data suggests a shift toward reduced creative efforts and stronger monetization motives. For example,
creating blogs and trending videos among interest-driven groups may increasingly rely on AI-produced information
without verification. The emerging knowledge of reformatting others’ content or generating AI-based influencer
personas are closely associated with the misappropriation of existing creative works. Such emerging GenAI creation
norms may hamper creative expression and educational intentions and limit creators’ ability to foster meaningful social
connections [32, 85].
6.2.2 GenAI-Faked Expertise for Interest Pandering.Our data suggest that creators’ collective knowledge depicts AI-
generated content as an authoritative source, using it tofake expertisein order to satisfy audiences’ niche interests.
Examples such as trending videos, blogs, merchandise, and e-books produced with GenAI illustrate how creators align
Manuscript submitted to ACM

22 Niu, et al.
their output with popular interests, even when the content lacks personal relevance or authenticity [20, 73, 87]. Some
HCI research has focused on understanding the impact of GenAI’s human-likeness [58, 72], while creators’ collective
knowledge frames GenAI as an infrastructure for generating ideas and content to satisfy audience demand [87]. While
platform monetary incentives shape creators’ topic choices and content formats [30], our findings indicate that creators’
GenAI knowledge may further influence their topic choices and perceived expertise on the topic.
However, expertise-faking with GenAI introduces a new indirect way in which AI-produced content may affect users.
In our analysis, YouTubers’ suggestions to use GenAI to generateTrending VideoandBlogcontent are significantly
associated with the challenge of non-verification, suggesting that monetization incentives may encourage irresponsible
uses of GenAI. Given that GenAI contains biases and hallucinations [4, 34, 71], such issues may be bypassed by creators
and passed on to audiences through user-generated content.
6.2.3 GenAI Erosion of Creativity Recognition.Besides faking expertise, the integration of GenAI is also framed as
a device for entering handcrafted and stock-image marketplaces through practices offaking creativity, which may
undermine recognition of artisans’ creative work. Our results suggest that some creators recommend using GenAI
to sell printed merchandise featuring GenAI graphics, digital graphic designs, and AI photographs. Platforms like
Etsy were designed to support artisans in selling handmade crafts [51, 68], emphasizing originality, authenticity, and
distinction from mass-produced products. However, such GenAI-driven practices may reshape such transactional
models by altering how creators define, and how audiences perceive, products traditionally regarded as creative, such
as handmade goods, digital art, and creative services.
On one hand, many creators integrate GenAI into their workflows as a legitimate source of inspiration and illus-
tration [41, 77, 90]. On the other hand, community knowledge frames GenAI designs as cost-effective substitutes for
human artistry, offering comparable visual appeal at a lower cost. Therefore, future research should examine not only
how AI is embedded in creative processes [44] but also how creators and buyers assess the value of human creativity in
AI-generated artistic work [36]. A deeper understanding is needed of how GenAI can preserve the uniqueness and
rarity valued within artisan communities.
6.3 Implications
The YouTube creator community is building a collective knowledge of GenAI4Money that introduces new dynamics
into established HCI theories on socio-technical infrastructure and creative labor. Our framework serves as a conceptual
guide summarizing how the community tends to disseminate GenAI knowledge for monetization. By making explicit
the interplay between monetization and associated GenAI uses, the framework operationalizes key considerations for
evaluating future GenAI technologies for creativity support and identifying associated risks for researchers, designers,
and policymakers. Based on this conceptual framework (Figure 21), we discuss design implications along three key
aspects impacted by GenAI4Money—creative labor, expertise, and creativity.
• Tradeoff between alleviating creative labor and opportunistic use of GenAI.The emergence of GenAI
knowledge in content creation challenges prior creative labor theory, which views human performers’ routines
as embedded within content-sharing infrastructures [73]. In contrast, we find that GenAI4Money knowledge
tends to frame GenAI as a de-laborification technique that conceals creator identity and enables opportunistic
monetization. For technologies that integrate GenAI for creative workflow optimization [44, 77] or replace human
labor with AI-generated performance [35, 72], our conceptualization suggests that these designs should consider
whether GenAI tools help alleviate extraneous workloads (such as managing creators’ public presentation or
Manuscript submitted to ACM

Generative AI for Monetization 23
selecting trending titles), while also supporting value expression (e.g., topic research and aligning AI-generated
content with creators’ authentic interests). A future direction is to design evaluation metrics that assess how
the tool amplifies creative agency while reducing creators’ tendency to use it for opportunistic creation. Our
framework also highlights the need to re-examine how revenue-sharing and moderation infrastructures (e.g.,
subscription and advertisement models) intersect with GenAI use [26, 56]. Platform policymakers need to develop
explicit community guidelines that discourage the use of GenAI to misappropriate original content (e.g., through
modification or reposting) [31]. To reduce opportunistic creation with GenAI, monetization programs should
de-emphasize the quantity of production and instead guide creators to assess how GenAI-generated content
influences user engagement and what forms of GenAI content are acceptable within the community.
• Tradeoff between expertise enhancement and expertise faking.Prior work has shown that creative agency
and responsibility are reshaped by GenAI [41, 90]. The spread of knowledge about expertise enhancement and
expertise faking in GenAI4Money introduces new tensions between novice and expert creators. GenAI lowers
skill barriers and enables novices to generate plausible content [77], but it may also introduce AI hallucinations
or inaccuracies [44] into niche communities. Based on the GenAI4Money framework, we propose three design
recommendations. First, GenAI tools need to be built with consideration of creators’ levels of expertise. For
professional creators, GenAI tools should enhance expertise by supporting idea discovery, trend alignment, and
topic selection. For novice creators, GenAI tools should be designed to encourage the foregrounding of their
expertise, provide guidance on questioning the authority and quality of AI-generated content, and promote
responsibility for AI-created content. Second, because AI outputs still exhibit quality problems [ 44] and we
observed cases of non-verification in our study, GenAI tools should prompt creators to verify accuracy and
quality – for example, by highlighting uncertainty in AI-generated scripts or blogs and encouraging human
validation. Third, as GenAI tools are rapidly adopted for analyzing trending content (e.g., for SEO) and shaping
monetization strategies, platforms should build GenAI tools to support standard methods for working with
algorithm with GenAI to reduce visibility inequality [84].
• Tradeoff between AI creativity and human creativity.Our framework should foster design considerations
that balance GenAI creativity with human creativity. While prior work argues that AI reshapes rather than
replaces creative agency [41], the rise of GenAI knowledge within transaction and advertisement models requires
stakeholders to reassess the boundaries of GenAI creativity. First, because monetization is a common creator
practice [59, 70], we argue that GenAI production should shift from mimicking human-created content toward
forms that are recognizably GenAI yet still creative and trending (e.g., trending AI art). Such media knowledge
and practices must be examined to help creators develop healthy GenAI knowledge and skills [20]. For example,
dedicated channels and platforms for sharing GenAI-enabled creativity could be developed. Second, beyond
examining audiences’ ability to identify AI content [81], HCI research should assess how new forms of GenAI
creativity align with users’ and advertisers’ interests, ensuring that GenAI complements rather than replaces
human creativity. Business advertisers should have options to determine whether permitting GenAI content
may redirect traffic to their brands. Buyers on handcraft marketplace platforms should also be informed about
whether GenAI is used. Third, our research highlights the need for new knowledge to guide creators in being
aware of transparency in GenAI usage. Creativity-faking behaviors (e.g., selling AI art as an original piece or
modifying others’ original work) should be mitigated. Platforms should also establish clear guidelines that allow
creators to declare GenAI use in their creative work and that inform buyers when an art piece is generated by AI.
Manuscript submitted to ACM

24 Niu, et al.
7 Conclusion
In conclusion, this study offers a foundational conceptual understanding of YouTubers’ collective knowledge surrounding
the use of GenAI for monetization, contributing valuable insights into the rapid growth of GenAI in user-generated
content [40]. We identified 10 GenAI4Money use cases and examined their alignment with monetization models and
the creative labor challenges they introduce. We conclude with a framework that highlights how GenAI4Money shapes
content-sharing infrastructures and creative labor. This framework guides future GenAI tool design, GenAI adoption,
and policymaking by clarifying the tradeoffs between creative labor and opportunistic use, expertise enhancement
and expertise faking, and AI creativity and human creativity. Although this work captures the breadth of GenAI in
monetization, we acknowledge several limitations and outline directions for future research.
First, our dataset captures on-screen demonstrations and claims about GenAI monetization strategies, not direct logs
of creators’ off-screen practices or verified income. The videos reveal patterns of YouTubers’ collective knowledge and
perceived effective ways of using GenAI for monetization, but they do not confirm the actual workflows or any other
potentially unethical uses of GenAI. Future interviews and surveys with YouTube creators could further uncover the
rationales for GenAI adoption beyond monetization.
Second, our data collection focused primarily on YouTube, though GenAI is also extensively used on other platforms
such as TikTok, Instagram, and Twitter. From the audience’s perspective, researchers should examine how GenAI-driven,
de-identified content reshapes parasocial relationships and influences long-term trust in AI-mediated creators across
platforms [85].
References
[1] Ali Alkhatib and Michael Bernstein. 2019. Street-Level Algorithms: A Theory at the Gaps Between Policy and Decisions. InProceedings of
the 2019 CHI Conference on Human Factors in Computing Systems (CHI ’19). Association for Computing Machinery, New York, NY, USA, 1–13.
doi:10.1145/3290605.3300760
[2] Torin Anderson and Shuo Niu. 2025. Making AI-Enhanced Videos: Analyzing Generative AI Use Cases in YouTube Content Creation. (3 2025).
doi:10.1145/3706599.3719991/ASSET/84AB381D-FEB3-4141-8B07-0044399A038D/ASSETS/GRAPHIC/CHIEA25-505-FIG6.JPG
[3] Taylor Annabell. 2025. The Ideal Influencer: How Influencer Coaches and Platforms Construct Creators as Monetizing for the Right Reasons.Social
Media + Society11, 1 (1 2025), 20563051251323951. doi:10.1177/20563051251323951
[4] Ajay Bandi, Pydi Venkata Satya Ramesh Adapa, and Yudu Eswar Vinay Pratap Kumar Kuchi. 2023. The Power of Generative AI: A Review of
Requirements, Models, Input–Output Formats, Evaluation Metrics, and Challenges.Future Internet15, 8 (2023). doi:10.3390/fi15080260
[5] Kristen Barta and Nazanin Andalibi. 2021. Constructing Authenticity on TikTok: Social Norms and Social Support on the "Fun" Platform.Proc. ACM
Hum.-Comput. Interact.5, CSCW2 (10 2021). doi:10.1145/3479574
[6] Ralph Barthel, Shaaron Ainsworth, and Mike Sharples. 2013. Collaborative knowledge building with shared video representations.International
Journal of Human-Computer Studies71, 1 (2013), 59–75. doi:10.1016/j.ijhcs.2012.02.006
[7] Sophie Bishop. 2019. Managing visibility on YouTube through algorithmic gossip.New Media & Society21, 11-12 (6 2019), 2589–2606. doi:10.1177/
1461444819854731
[8] Sophie Bishop. 2019. Managing visibility on YouTube through algorithmic gossip.New Media & Society21, 11-12 (11 2019), 2589–2606. doi:10.1177/
1461444819854731
[9] Sophie Bishop. 2020. Algorithmic Experts: Selling Algorithmic Lore on YouTube.Social Media + Society6, 1 (1 2020), 2056305119897323.
doi:10.1177/2056305119897323
[10] Jean Burgess and Joshua Green. 2018.YouTube: Online video and participatory culture. John Wiley & Sons, Cambridge, UK.
[11] Robyn Caplan and Tarleton Gillespie. 2020. Tiered Governance and Demonetization: The Shifting Terms of Labor and Compensation in the
Platform Economy.Social Media + Society6, 2 (4 2020), 2056305120936636. doi:10.1177/2056305120936636
[12] Kathy Charmaz and Linda Liska Belgrave. 2015. Grounded Theory. InThe Blackwell Encyclopedia of Sociology. doi:10.1002/9781405165518.wbeosg070.
pub2
[13] Clement Chau. 2010. YouTube as a participatory culture.New Directions for Youth Development2010, 128 (2010), 65–74. doi:10.1002/yd.376
[14] Si Chen, Xinyue Chen, Zhicong Lu, and Yun Huang. 2023. "My Culture, My People, My Hometown": Chinese Ethnic Minorities Seeking Cultural
Sustainability by Video Blogging.Proc. ACM Hum.-Comput. Interact.7, CSCW1 (4 2023). doi:10.1145/3579509
Manuscript submitted to ACM

Generative AI for Monetization 25
[15] Yoonseo Choi, Eun Jeong Kang, Min Kyung Lee, and Juho Kim. 2023. Creator-Friendly Algorithms: Behaviors, Challenges, and Design Opportunities
in Algorithmic Platforms. InProceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI ’23). Association for Computing
Machinery, New York, NY, USA. doi:10.1145/3544548.3581386
[16] Andrew Chu, Arjun Arunasalam, Muslum Ozgur Ozmen, and Z Berkay Celik. 2022. Behind the Tube: Exploitative Monetization of Content
on YouTube. In31st USENIX Security Symposium (USENIX Security 22). USENIX Association, Boston, MA, 2171–2188. https://www.usenix.org/
conference/usenixsecurity22/presentation/chu
[17] Kelley Cotter. 2024. Practical knowledge of algorithms: The case of BreadTube.New Media & Society26, 4 (4 2024), 2131–2150. doi:10.1177/
14614448221081802
[18] Nick Couldry. 2004. Theorising media as practice.Social Semiotics14, 2 (8 2004), 115–132. doi:10.1080/1035033042000238295
[19] Michael Dezuanni and Amy Schoonens. 2024. #BookTok’s Peer Pedagogies: Invitations to Learn About Books and Reading on TikTok.Social
Media + Society10, 4 (10 2024), 20563051241309499. doi:10.1177/20563051241309499
[20] Xianghua(Sharon) Ding, Yubo Kou, Yiwen Xu, and Peng Zhang. 2022. “As Uploaders, We Have the Responsibility”: Individualized Professionalization
of Bilibili Uploaders. InProceedings of the 2022 CHI Conference on Human Factors in Computing Systems (CHI ’22). Association for Computing
Machinery, New York, NY, USA. doi:10.1145/3491102.3517509
[21] Anil R Doshi and Oliver P Hauser. 2024. Generative AI enhances individual creativity but reduces the collective diversity of novel content.Science
Advances10, 28 (10 2024), eadn5290. doi:10.1126/sciadv.adn5290
[22] Duo Du, Yanling Zhang, and Jiao Ge. 2023. Effect of AI Generated Content Advertising on Consumer Engagement.Lecture Notes in Computer
Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)14039 LNCS (2023), 121–129. doi:10.1007/978-3-
031-36049-7{_}9/TABLES/3
[23] Ilana Dubovi and Iris Tabak. 2019. Examining the educative value of person-to-person knowledge sharing on social media: The case of youtube as a
site of cscl? (2019).
[24] Brooke Erin Duffy, Annika Pinch, Shruti Sannon, and Megan Sawey. 2021. The Nested Precarities of Creative Labor on Social Media.Social Media
+ Society7, 2 (4 2021), 20563051211021368. doi:10.1177/20563051211021368
[25] Brooke Erin Duffy, Thomas Poell, and David B Nieborg. 2019. Platform Practices in the Cultural Industries: Creativity, Labor, and Citizenship.
Social Media + Society5, 4 (10 2019), 2056305119879672. doi:10.1177/2056305119879672
[26] Arun Dunna, Katherine A Keith, Ethan Zuckerman, Narseo Vallina-Rodriguez, Brendan O’Connor, and Rishab Nithyanand. 2022. Paying Attention
to the Algorithm Behind the Curtain: Bringing Transparency to YouTube’s Demonetization Algorithms.Proc. ACM Hum.-Comput. Interact.6,
CSCW2 (11 2022). doi:10.1145/3555209
[27] Adam G Emerson, Shreyosi Endow, and Cesar Torres. 2024. Anther: Cross-Pollinating Communities of Practice via Video Tutorials. InProceedings
of the 2024 ACM Designing Interactive Systems Conference (DIS ’24). Association for Computing Machinery, New York, NY, USA, 1991–2005.
doi:10.1145/3643834.3660727
[28] Adam G Emerson, Shreyosi Endow, and Cesar Torres. 2024. Shared, Shaped, and Stolen: Tracing Sites of Knowledge Transfer across Creative
Communities of Practice. InProceedings of the 16th Conference on Creativity & Cognition (C&C ’24). Association for Computing Machinery, New
York, NY, USA, 638–650. doi:10.1145/3635636.3656199
[29] Ziv Epstein, Aaron Hertzmann, the Investigators of Human Creativity, Memo Akten, Hany Farid, Jessica Fjeld, Morgan R Frank, Matthew Groh,
Laura Herman, Neil Leach, Robert Mahari, Alex Pentland, Olga Russakovsky, Hope Schroeder, and Amy Smith. 2023. Art and the science of
generative AI.Science380, 6650 (6 2023), 1110–1111. doi:10.1126/science.adh4451
[30] Tess Eschebach, Nikola Banovic, and Allison McDonald. 2025. Playing ’Google’s Game’: How Educational YouTubers Manage Tensions Between
Education and Monetization.Proc. ACM Hum.-Comput. Interact.9, 7 (10 2025). doi:10.1145/3757496
[31] Casey Fiesler, Cliff Lampe, and Amy S Bruckman. 2016. Reality and Perception of Copyright Terms of Service for Online Content Creation. In
Proceedings of the 19th ACM Conference on Computer-Supported Cooperative Work & Social Computing (CSCW ’16). Association for Computing
Machinery, New York, NY, USA, 1450–1461. doi:10.1145/2818048.2819931
[32] Widia Resti Fitriani, Arif Budi Mulyono, Achmad Nizar Hidayanto, and Qorib Munajat. 2020. Reviewer’s communication style in YouTube
product-review videos: does it affect channel loyalty?Heliyon6, 9 (9 2020). doi:10.1016/j.heliyon.2020.e04880
[33] Eureka Foong. 2020. Understanding and designing sociotechnical systems to support the impression management practices of online freelance workers.
Proceedings of the International ACM SIGGROUP Conference on Supporting Group Work(1 2020), 25–33. doi:10.1145/3323994.3371017;JOURNAL:
JOURNAL:ACMCONFERENCES;PAGEGROUP:STRING:PUBLICATION
[34] Fiona Fui Hoon Nah, Ruilin Zheng, Jingyuan Cai, Keng Siau, and Langtao Chen. 2023. Generative AI and ChatGPT: Applications, challenges, and
AI-human collaboration.Journal of Information Technology Case and Application Research25, 3 (7 2023), 277–304. doi:10.1080/15228053.2023.2233814
[35] Dilrukshi Gamage, Piyush Ghasiya, Vamshi Bonagiri, Mark E Whiting, and Kazutoshi Sasahara. 2022. Are Deepfakes Concerning? Analyzing
Conversations of Deepfakes on Reddit and Exploring Societal Implications. InProceedings of the 2022 CHI Conference on Human Factors in Computing
Systems (CHI ’22). Association for Computing Machinery, New York, NY, USA. doi:10.1145/3491102.3517446
[36] Trystan S. Goetze. 2024. AI Art is Theft: Labour, Extraction, and Exploitation: Or, On the Dangers of Stochastic Pollocks.2024 ACM Conference on
Fairness, Accountability, and Transparency, FAccT 2024(6 2024), 186–196. doi:10.1145/3630106.3658898;CSUBTYPE:STRING:CONFERENCE
[37] Roberto Gozalo-Brizuela and Eduardo C Garrido-Merchan. 2023. ChatGPT is not all you need. A State of the Art Review of large Generative AI
models.arXiv preprint arXiv:2301.04655(2023).
Manuscript submitted to ACM

26 Niu, et al.
[38] Brett A. Halperin and Daniela K. Rosner. 2025. “AI is Soulless”: Hollywood Film Workers’ Strike and Emerging Perceptions of Generative Cinema.
ACM Transactions on Computer-Human Interaction32, 2 (4 2025), 1–27. doi:10.1145/3716135
[39] Jameson Hayes and Geoffrey Graybeal. 2011. Synergizing Traditional Media and the Social Web for Monetization: A Modified Media Micropayment
Model.Journal of Media Business Studies8, 2 (6 2011), 19–44. doi:10.1080/16522354.2011.11073521
[40] Yiqing Hua, Shuo Niu, Jie Cai, Lydia B Chilton, Hendrik Heuer, and Donghee Yvette Wohn. 2024. Generative AI in User-Generated Content. In
Extended Abstracts of the 2024 CHI Conference on Human Factors in Computing Systems (CHI EA ’24). Association for Computing Machinery, New
York, NY, USA. doi:10.1145/3613905.3636315
[41] Angel Hsing-Chi Hwang. 2022. Too Late to be Creative? AI-Empowered Tools in Creative Processes. InExtended Abstracts of the 2022 CHI Conference
on Human Factors in Computing Systems (CHI EA ’22). Association for Computing Machinery, New York, NY, USA. doi:10.1145/3491101.3503549
[42] Nadia Karizat, Dan Delmonaco, Motahhare Eslami, and Nazanin Andalibi. 2021. Algorithmic Folk Theories and Identity: How TikTok Users
Co-Produce Knowledge of Identity and Engage in Algorithmic Resistance.Proc. ACM Hum.-Comput. Interact.5, CSCW2 (10 2021). doi:10.1145/3476046
[43] Susie Khamis, Lawrence Ang, and Raymond Welling. 2017. Self-branding, ‘micro-celebrity’ and the rise of Social Media Influencers.Celebrity Studies
8, 2 (4 2017), 191–208. doi:10.1080/19392397.2016.1218292
[44] Jini Kim and Hajun Kim. 2024. Unlocking Creator-AI Synergy: Challenges, Requirements, and Design Opportunities in AI-Powered Short-Form
Video Production. InProceedings of the 2024 CHI Conference on Human Factors in Computing Systems (CHI ’24). Association for Computing Machinery,
New York, NY, USA. doi:10.1145/3613904.3642476
[45] Sena A Kojah, Ben Zefeng Zhang, Carolina Are, Daniel Delmonaco, and Oliver L Haimson. 2025. "Dialing it Back:" Shadowbanning, Invisible Digital
Labor, and how Marginalized Content Creators Attempt to Mitigate the Impacts of Opaque Platform Governance.Proc. ACM Hum.-Comput. Interact.
9, 1 (1 2025). doi:10.1145/3701191
[46] Susanne Kopf. 2020. “Rewarding Good Creators”: Corporate Social Media Discourse on Monetization Schemes for Content Creators.Social Media +
Society6, 4 (10 2020), 2056305120969877. doi:10.1177/2056305120969877
[47] Klaus Krippendorff. 2004. Reliability in Content Analysis: Some Common Misconceptions and Recommendations.Human Communication Research
30, 3 (7 2004), 411–433. doi:10.1111/j.1468-2958.2004.tb00738.x
[48] Nir Kshetri, Yogesh K Dwivedi, Thomas H Davenport, and Niki Panteli. 2024. Generative artificial intelligence in marketing: Applications,
opportunities, challenges, and research agenda.International Journal of Information Management75 (2024), 102716. doi:10.1016/j.ijinfomgt.2023.
102716
[49] Thomas R Lindlof and Bryan C Taylor. 2017.Qualitative communication research methods. Sage publications.
[50] Zhicong Lu, Chenxinran Shen, and Jiannan Li. 2021. More kawaii than a real-person live streamer: Understanding how the otaku community engages
with and perceives virtual youtubers.Conference on Human Factors in Computing Systems - Proceedings(5 2021). doi:10.1145/3411764.3445660;PAGE:
STRING:ARTICLE/CHAPTER
[51] Susan Luckman. 2013. The aura of the analogue in a digital age: Women’s crafts, creative markets and home-based labour after Etsy.Cultural
Studies Review19, 1 (3 2013), 249–270. https://search.informit.org/doi/10.3316/informit.273273712487637https://search.informit.org/doi/pdf/10.3316/
informit.273273712487637https://search.informit.org/doi/full/10.3316/informit.273273712487637
[52] Yao Lyu, Jie Cai, and John M Carroll. 2025. A Systematic Literature Review of Infrastructure Studies in SIGCHI.Proc. ACM Hum.-Comput. Interact.9,
7 (10 2025). doi:10.1145/3757545
[53] Yao Lyu, He Zhang, Shuo Niu, and Jie Cai. 2024. A Preliminary Exploration of YouTubers’ Use of Generative-AI in Content Creation. InExtended
Abstracts of the 2024 CHI Conference on Human Factors in Computing Systems (CHI EA ’24). Association for Computing Machinery, New York, NY,
USA. doi:10.1145/3613905.3651057
[54] Renkai Ma, Xinning Gui, and Yubo Kou. 2023. Multi-Platform Content Creation: The Configuration of Creator Ecology through Platform Prioritization,
Content Synchronization, and Audience Management. InProceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI ’23).
Association for Computing Machinery, New York, NY, USA. doi:10.1145/3544548.3581106
[55] Renkai Ma and Yubo Kou. 2021. "How Advertiser-Friendly is My Video?": YouTuber’s Socioeconomic Interactions with Algorithmic Content
Moderation.Proc. ACM Hum.-Comput. Interact.5, CSCW2 (10 2021). doi:10.1145/3479573
[56] Renkai Ma, Yue You, Xinning Gui, and Yubo Kou. 2023. How Do Users Experience Moderation?: A Systematic Literature Review.Proceedings of the
ACM on Human-Computer Interaction7, CSCW2 (10 2023). doi:10.1145/3610069;WGROUP:STRING:ACM
[57] Thomas W L MacDonald. 2021. “How it actually works”: Algorithmic lore videos as market devices.New Media & Society(6 2021), 14614448211021404.
doi:10.1177/14614448211021404
[58] Takuya Maeda and Anabel Quan-Haase. 2024. When Human-AI Interactions Become Parasocial: Agency and Anthropomorphism in Affective
Design.2024 ACM Conference on Fairness, Accountability, and Transparency, FAccT 2024(6 2024), 1068–1077. doi:10.1145/3630106.3658956
[59] Arunesh Mathur, Arvind Narayanan, and Marshini Chetty. 2018. Endorsements on Social Media: An Empirical Study of Affiliate Marketing
Disclosures on YouTube and Pinterest.Proc. ACM Hum.-Comput. Interact.2, CSCW (11 2018). doi:10.1145/3274388
[60] Anthony McCosker. 2024. Making sense of deepfakes: Socializing AI and building data literacy on GitHub and YouTube.New Media & Society26, 5
(2024), 2786–2803. doi:10.1177/14614448221093943
[61] Nusrat Jahan Mim, Dipannita Nandi, Sadaf Sumyia Khan, Arundhuti Dey, and Syed Ishtiaque Ahmed. 2024. In-Between Visuals and Visible: The
Impacts of Text-to-Image Generative AI Tools on Digital Image-making Practices in the Global South. InProceedings of the 2024 CHI Conference on
Human Factors in Computing Systems (CHI ’24). Association for Computing Machinery, New York, NY, USA. doi:10.1145/3613904.3641951
Manuscript submitted to ACM

Generative AI for Monetization 27
[62] Isabel Munoz, Michael Dunn, Steve Sawyer, and Emily Michaels. 2022. Platform-mediated Markets, Online Freelance Workers and Deconstructed
Identities.Proceedings of the ACM on Human-Computer Interaction6, CSCW2 (11 2022). doi:10.1145/3555092
[63] Shuo Niu, Cat Mai, Katherine G McKim, and D Scott McCrickard. 2021. #TeamTrees: Investigating How YouTubers Participate in a Social Media
Campaign.Proc. ACM Hum.-Comput. Interact.5, CSCW2 (10 2021). doi:10.1145/3479593
[64] Jacob Ørmen and Andreas Gregersen. 2022. Institutional Polymorphism: Diversification of Content and Monetization Strategies on YouTube.
Television & New Media24, 4 (7 2022), 432–451. doi:10.1177/15274764221110198
[65] William Clyde Partin. 2020. Bit by (Twitch) Bit: “Platform Capture” and the Evolution of Digital Platforms.Social Media + Society6, 3 (7 2020),
2056305120933981. doi:10.1177/2056305120933981
[66] Bernd Ploderer, Steve Howard, and Peter Thomas. 2010. Collaboration on Social Network Sites: Amateurs, Professionals and Celebrities.Computer
Supported Cooperative Work (CSCW)19, 5 (2010), 419–455. doi:10.1007/s10606-010-9112-0
[67] Hector Postigo. 2014. The socio-technical architecture of digital labor: Converting play into YouTube money.New Media & Society18, 2 (7 2014),
332–349. doi:10.1177/1461444814541527
[68] Lubna Razaq, Beth Kolko, and Gary Hsieh. 2022. Making crafting visible while rendering labor invisible on the Etsy platform.DIS 2022 - Proceedings
of the 2022 ACM Designing Interactive Systems Conference: Digital Wellbeing(6 2022), 424–438. doi:10.1145/3532106.3533573/SUPPL{_}FILE/
SELLER{_}INTERVIEW{_}PROTOCOL.PDF
[69] CJ Reynolds and Blake Hallinan. 2024. User-generated accountability: Public participation in algorithmic governance on YouTube.New Media &
Society26, 9 (9 2024), 5107–5129. doi:10.1177/14614448241251791
[70] Bernhard Rieder, Erik Borra, Òscar Coromina, and Ariadna Matamoros-Fernández. 2023. Making a Living in the Creator Economy: A Large-Scale
Study of Linking on YouTube.Social Media + Society9, 2 (4 2023), 20563051231180628. doi:10.1177/20563051231180628
[71] Henrik Skaug Sætra. 2023. Generative AI: Here to stay, but for good?Technology in Society75 (2023), 102372. doi:10.1016/j.techsoc.2023.102372
[72] Cherie Sew, Sarah Schömbs, Ryan M. Kelly, and Jorge Goncalves. 2025. User Willingness to Engage with AI-Generated Influencer Content.Proceedings
of the Extended Abstracts of the CHI Conference on Human Factors in Computing Systems(4 2025), 1–7. doi:10.1145/3706599.3719916
[73] Ellen Simpson and Bryan Semaan. 2023. Rethinking Creative Labor: A Sociotechnical Examination of Creativity & Creative Work on TikTok. In
Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI ’23). Association for Computing Machinery, New York, NY,
USA. doi:10.1145/3544548.3580649
[74] Ellen Simpson and Bryan Semaan. 2025. Infrastructures for Inspiration: The Routine of Creative Identity Through Inspiration on the Creative
Internet. InProceedings of the 2025 CHI Conference on Human Factors in Computing Systems (CHI ’25). Association for Computing Machinery, New
York, NY, USA. doi:10.1145/3706598.3713105
[75] Michael Soha and Zachary J McDowell. 2016. Monetizing a Meme: YouTube, Content ID, and the Harlem Shake.Social Media + Society2, 1 (1 2016),
2056305115623801. doi:10.1177/2056305115623801
[76] Vishvesh Soni. 2023. Adopting Generative AI in Digital Marketing Campaigns: An Empirical Study of Drivers and Barriers.Sage Science Review of
Applied Machine Learning6, 8 (8 2023), 1–15. https://journals.sagescience.org/index.php/ssraml/article/view/108
[77] Yuan Sun, Eunchae Jang, Fenglong Ma, and Ting Wang. 2024. Generative AI in the Wild: Prospects, Challenges, and Strategies. InProceedings
of the 2024 CHI Conference on Human Factors in Computing Systems (CHI ’24). Association for Computing Machinery, New York, NY, USA.
doi:10.1145/3613904.3642160
[78] Kurt Thomas, Patrick Gage Kelley, Sunny Consolvo, Patrawat Samermit, and Elie Bursztein. 2022. “It’s Common and a Part of Being a Content
Creator”: Understanding How Creators Experience and Cope with Hate and Harassment Online. InProceedings of the 2022 CHI Conference on Human
Factors in Computing Systems (CHI ’22). Association for Computing Machinery, New York, NY, USA. doi:10.1145/3491102.3501879
[79] Roland Verwiebe, Claudia Buder, Sarah Weissmann, Chiara Osorio-Krauter, and Aaron Philipp. 2026. “The algorithm is like a mercurial
god”: Exploring content creators’ perception of algorithmic agency on YouTube.New Media & Society28, 3 (3 2026), 1219–1238. doi:10.1177/
14614448241307931
[80] Justice Walker, Stefan Slater, and Yasmin Kafai. 2019. A scaled analysis of how Minecraft gamers leverage YouTube comment boxes to participate
and collaborate. (2019).
[81] Ke Wang, Lehao Lin, Maha Abdallah, and Wei Cai. 2025. Where is the Boundary? Understanding How People Recognize and Evaluate Generative
AI-extended Videos. InProceedings of the 2025 CHI Conference on Human Factors in Computing Systems (CHI ’25). Association for Computing
Machinery, New York, NY, USA. doi:10.1145/3706598.3714061
[82] Shuai Wang, Zhiyuan Chen, Bing Liu, and Sherry Emery. 2016. Identifying Search Keywords for Finding Relevant Social Media Posts.Proceedings of
the AAAI Conference on Artificial Intelligence30, 1 (3 2016). doi:10.1609/aaai.v30i1.10387
[83] Sitong Wang, Samia Menon, Tao Long, Keren Henderson, Dingzeyu Li, Kevin Crowston, Mark Hansen, Jeffrey V Nickerson, and Lydia B Chilton.
2024. ReelFramer: Human-AI Co-Creation for News-to-Video Translation. InProceedings of the 2024 CHI Conference on Human Factors in Computing
Systems (CHI ’24). Association for Computing Machinery, New York, NY, USA. doi:10.1145/3613904.3642868
[84] Philip Weber, Thomas Ludwig, Sabrina Brodesser, and Laura Grönewald. 2021. “It’s a Kind of Art!”: Understanding Food Influencers as Influential
Content Creators. InProceedings of the 2021 CHI Conference on Human Factors in Computing Systems (CHI ’21). Association for Computing Machinery,
New York, NY, USA. doi:10.1145/3411764.3445607
[85] Donghee Yvette Wohn, Guo Freeman, and Caitlin McLaughlin. 2018. Explaining Viewers’ Emotional, Instrumental, and Financial Support Provision
for Live Streamers. InProceedings of the 2018 CHI Conference on Human Factors in Computing Systems (CHI ’18). Association for Computing Machinery,
Manuscript submitted to ACM

28 Niu, et al.
New York, NY, USA, 1–13. doi:10.1145/3173574.3174048
[86] Allison Woodruff, Renee Shelby, Patrick Gage Kelley, Steven Rousso-Schindler, Jamila Smith-Loud, and Lauren Wilcox. 2024. How Knowledge
Workers Think Generative AI Will (Not) Transform Their Industries. InProceedings of the 2024 CHI Conference on Human Factors in Computing
Systems (CHI ’24). Association for Computing Machinery, New York, NY, USA. doi:10.1145/3613904.3642700
[87] Haijun Xia, Hui Xin Ng, Chen Zhu-Tian, and James Hollan. 2022. Millions and Billions of Views: Understanding Popular Science and Knowledge
Communication on Video-Sharing Platforms. InProceedings of the Ninth ACM Conference on Learning @ Scale (L@S ’22). Association for Computing
Machinery, New York, NY, USA, 163–174. doi:10.1145/3491140.3528279
[88] Qian Yang, Richmond Y Wong, Steven Jackson, Sabine Junginger, Margaret D Hagan, Thomas Gilbert, and John Zimmerman. 2024. The Future of
HCI-Policy Collaboration. InProceedings of the 2024 CHI Conference on Human Factors in Computing Systems (CHI ’24). Association for Computing
Machinery, New York, NY, USA. doi:10.1145/3613904.3642771
[89] J H Ye and C E H Chua. 2024. Monetization for Content Generation and User Engagement on Social Media Platforms: Evidence from Paid Q&A.
IEEE Transactions on Engineering Management71 (2024), 4022–4034. doi:10.1109/TEM.2022.3209534
[90] Nur Yildirim, Alex Kass, Teresa Tung, Connor Upton, Donnacha Costello, Robert Giusti, Sinem Lacin, Sara Lovic, James M O’Neill, Rudi O’Reilly
Meehan, Eoin Ó Loideáin, Azzurra Pini, Medb Corcoran, Jeremiah Hayes, Diarmuid J Cahalane, Gaurav Shivhare, Luigi Castoro, Giovanni Caruso,
Changhoon Oh, James McCann, Jodi Forlizzi, and John Zimmerman. 2022. How Experienced Designers of Enterprise Applications Engage AI as a
Design Material. InProceedings of the 2022 CHI Conference on Human Factors in Computing Systems (CHI ’22). Association for Computing Machinery,
New York, NY, USA. doi:10.1145/3491102.3517491
Manuscript submitted to ACM
