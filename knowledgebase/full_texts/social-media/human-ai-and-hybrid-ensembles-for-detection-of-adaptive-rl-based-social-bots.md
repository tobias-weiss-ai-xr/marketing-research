---
title: Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots
url: https://arxiv.org/abs/2603.23796
category: social-media
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Valerio La Gatta
- Nathan Subrahmanian
- Kaitlyn Wang
- Larry Birnbaum
- V. S. Subrahmanian
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.23796
pages: 26
chars: 89336
fetched_at: '2026-11-08T12:58:45+00:00'
kb_version: 1
---

# Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots

Human, AI, and Hybrid Ensembles for Detection of Adaptive,
RL-based Social Bots
VALERIO LA GATTA,Northwestern University, USA
NATHAN SUBRAHMANIAN,Brandeis University, USA
KAITLYN WANG,Northwestern University, USA
LARRY BIRNBAUM,Northwestern University, USA
V.S. SUBRAHMANIAN,Northwestern University, USA
The use of reinforcement learning to dynamically adapt and evade detection is now well-documented in
several cybersecurity settings including Covert Social Influence Operations (CSIOs), in which bots try to spread
disinformation. While AI bot detectors have improved greatly, they are largely limited to detecting static
bots that do not adapt dynamically. We present the first systematic study comparing the ability of humans,
AI models, and hybrid Human-AI ensembles in detectingadaptivebotspowered by reinforcement learning.
Using data from a controlled, IRB-approved, five-day experiment with participants interacting on a social
media platform infiltrated by RL-trained bots spreading disinformation to influence participants on 4 topics,
we examine factors potentially shaping human detection capabilities: demographic characteristics, temporal
learning effects, social network position, engagement patterns, and collective intelligence mechanisms. We first
test 13 hypotheses comparing human bot detection performance against state-of-the-art AI approaches utilizing
both traditional machine learning and large language models. We further investigate several aggregation
strategies that combine human reports of bots with AI predictions, as well as retraining protocols that leverage
human supervision. Our findings challenge intuitive assumptions about bot detection, reveal unexpected
patterns in how humans identify bots, and show that combining human bot reports with AI predictions
outperforms humans alone and AI alone. We conclude with a discussion of the practical implications of these
results for industry.
CCS Concepts:•Information systems → Social networks;•Human-centered computing → User studies.
Additional Key Words and Phrases: Influence Operations, Human-AI Social Bot Detection
ACM Reference Format:
Valerio La Gatta, Nathan Subrahmanian, Kaitlyn Wang, Larry Birnbaum, and V.S. Subrahmanian. 2018. Hu-
man, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots.J. ACM37, 4, Article 111
(August 2018), 26 pages. https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
Covert Social Influence Operations (CSIOs) threaten democratic discourse by leveraging social media
to manipulate information ecosystems, spread disinformation, and polarize communities [35, 36, 54].
Authors’ Contact Information: Valerio La Gatta, valerio.lagatta@northwestern.edu, Northwestern University, Evanston,
Illinois, USA; Nathan Subrahmanian, nsubrahmanian@brandeis.edu, Brandeis University, Boston, Massachusetts, USA;
Kaitlyn Wang, kaitlynwang2027@u.northwestern.edu, Northwestern University, Evanston, Illinois, USA; Larry Birnbaum, l-
birnbaum@northwestern.edu, Northwestern University, Evanston, Illinois, USA; V.S. Subrahmanian, vss@northwestern.edu,
Northwestern University, Evanston, Illinois, USA.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the
full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
©2018 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM 1557-735X/2018/8-ART111
https://doi.org/XXXXXXX.XXXXXXX
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
arXiv:2603.23796v1  [cs.SI]  25 Mar 2026

111:2 La Gatta et al.
However, a common theme in cybersecurity is that attackers adapt. This occurs with CSIOs as well:
state-backed cyber threat actors deploy increasingly sophisticated strategies that adapt dynamically
to countermeasures [2, 5]. Recent advances in artificial intelligence (AI) have accelerated this threat.
Reinforcement learning (RL) agents can dynamically adapt to static malware detectors [ 3, 42],
create attack paths through a network [26], neutralizing graph-neural network based detectors
focused on node injection attacks[45], and creating fake reviews in online marketplaces[56].
[24] presents a reinforcement learning-based CSIO (RL_CSIO) attack in which an adversary can
deploy autonomous, dynamically adaptive agents that control bot accounts to maximize influence
while changing their behavior to evade detection [24]. RL-operated bots, unlike static accounts,
learn adaptive behaviors through continuous interaction, developing sophisticated strategies that
simultaneously spread narratives and evade detection by AI classifiers. This potentially marks
a fundamental shift from manually orchestrated campaigns run by nation states, to a future in
which nation states and other malign actors may well leverage reinforcement learning to create
autonomous, self-optimizing systems capable of real-time adaptation to platform defenses. Such
RL_CSIO’s will continuously learn and exploit a model of the classifiers used by social platforms —
and perhaps others — to detect bots. Today, most bot detectors in industry use a combination of
rule-based and machine learning classifiers∗† that attempt to learn a model that distinguishes bots
from genuine accounts. However if the adversary uses RL to dynamically change its behavior, this
becomes challenging as this attack model changes continuously.
There has been substantial research in automated bot detection. AI approaches have evolved from
early classifiers based on behavioral features [6, 51] to sophisticated systems leveraging graph neural
networks [18, 19], large language models [10, 57], and temporal models [53]. Detection frameworks
specifically targeting CSIO-operated accounts employ content analysis [1, 2], behavioral pattern
recognition [4, 7, 32], and coordinated signal detection [33, 39, 41]. Despite this progress, automated
methods face inherent limitations: they operate retrospectively, they require labeled training data
that may not generalize to new evasion tactics, and they are engaged in an asymmetric arms race
where adaptive bots can learn to evade known detectors.
In contrast, human detection remains critically understudied, yet may offer complementary
capabilities. The limited research on human-based bot detection reveals problematic patterns:
individuals frequently fail to recognize sophisticated bots, achieving precision typically below
0.5 [23]. Paradoxically, greater social media experience does not guarantee improved accuracy and
may foster overconfidence [22]. Cognitive and political biases further reduce sensitivity to bots
expressing aligned viewpoints [47, 49]. However, these findings emerge almost exclusively from
studies ofstaticbot behaviors where the bots do not adapt dynamically. Critical questions remain
unanswered:How do humans perform against adaptive, RL-based bots that actively learn to evade
detection? What individual, social, and collective factors shape detection capabilities in adversarial
contexts? Can human judgment be aggregated to overcome individuals’ limitations? Can human
reports and AI predictions be combined to improve detection performance?
This paper addresses these questions through the first controlled investigation of human bot
detection against RL-based bots‡ operating in active CSIOs. We examine whether demographic
characteristics are linked to users’ detection performance, whether users learn to identify bots
over time, how social activity influences accuracy, and whether collective intelligence mechanisms
can aggregate individual judgments effectively. We benchmark human capabilities against three
∗https://www.snopes.com/articles/435482/spot-a-bot/
†https://mitsloan.mit.edu/ideas-made-to-matter/study-finds-bot-detection-software-isnt-accurate-it-seems
‡Hereafter, we use the term "bots" to refer to RL-based adaptive bots proposed by [24].
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:3
state-of-the-art AI detectors to assess complementarity, and investigate hybrid strategies that
combine human reports with AI predictions.
Our analysis leverages data from a five-day controlled experiment in which 225 participants
interacted on a social media platform infiltrated by four concurrent RL_CSIO campaigns [ 24],
providing unprecedented insight into human detection capabilities under realistic adversarial
conditions. Our contributions are:
• We provide the first systematic analysis of human-based bot detection performance against
RL-based adaptive botsin active influence operations, building on prior work on human bot
detection ability againststatic, non-adaptive bots[8, 21, 23, 37]
• We test 13 hypotheses examining how individual characteristics (age, education, language pro-
ficiency, platform usage), temporal dynamics (learning effects over time), and collective mech-
anisms (multiple report aggregation) shape detection performance under realistic adversarial
conditions.
• We compare human ensemble performance against three recent AI detectors spanning traditional
machine learning and large language models, examining both overall performance metrics and
pairwise agreement patterns to assess whether humans and AI identify bots through similar or
distinct mechanisms.
• We investigate aggregation strategies that combine human reports with AI predictions and
retraining protocols that leverage human supervision to improve detector performance.
2 Related Work
Influence Campaigns on Social Media.Covert social influence operations (CSIOs) represent a
growing threat to democratic discourse, increasingly leveraging sophisticated, multi-platform coor-
dination strategies [5, 35]. Between 2013 and 2018, at least 53 covert campaigns were documented
across 24 countries [36], with state-backed actors continually adapting to platform countermea-
sures [54]. The emergence of reinforcement learning (RL) has further advanced these operations,
enabling bots to strategically balance influence maximization and detection avoidance [24]. A wide
range of AI detection approaches have been proposed, targeting both automated accounts [4, 7] and
human operators [14]. These methods include content-based [1, 2], behavior-based [32, 41], and
hybrid frameworks [20, 44]. Recent advances integrate multiple behavioral signals such as timing
synchrony and coordination [33], while unsupervised methods improve adaptability to unseen
scenarios [39]. Yet, these AI methods remain constrained by retrospective analyses and limited
generalization to evolving CSIO tactics.
In contrast, bot detection by humans has received far less attention. Prior work primarily explores
public awareness [30] and training interventions such as “spot the troll” exercises [28], focusing
on static bot behaviors.This study bridges this gap by presenting the first systematic investigation
of real-time human detection of adaptive, RL-driven bots embedded in active influence campaigns,
examining how demographic, temporal, and collective factors shape human detection performance.
Bot Detection.Social bot detection research has progressed from early classifiers based on lin-
guistic, behavioral, and network features [6, 51, 53] to advanced models leveraging graph neural
networks [18, 19] and large language models [10, 57]. Tools such as Botometer [50] remain widely
used, yet comparative studies show low agreement among detectors, with inconsistent classifica-
tions across identical datasets [37].
Human performance in bot detection, by contrast, remains poorly understood. Empirical studies
reveal that individuals often fail to recognize sophisticated bots [8], achieving precision typically
below 0.5 and highly variable recall [21, 23, 37]. Moreover, greater social media experience does not
guarantee improved accuracy and may instead foster overconfidence [22]. Cognitive and political
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:4 La Gatta et al.
biases also reduce sensitivity to bots expressing opposing viewpoints [ 47, 49]. Some evidence,
however, suggests gradual learning effects with repeated exposure [24].
Our study extends this literature through the first controlled evaluation of human detection perfor-
mance againstadaptive, RL-based bots, not operating according to a static behavioral model,
testing 13 hypotheses on the roles of demographic traits, temporal learning, social interaction, and
collective intelligence in shaping human detection capabilities.
3 Materials & Methods
Kumar et al. [24] performed a controlled social media experiment involving 225 U.S. participants
recruited on Amazon Mechanical Turk (MTurk). The current study uses the data collected in this
experiment, only parts of which were used and released in [24].We will release the additional data
upon publication of this paper.
3.1 Participants
190 participants (84.4%) were male and 35 (15.6%) were female. The majority (71%) were between 25
and 34 years old, with the remainder distributed across the 18–24, 35–44, and 45–54 age brackets.
Most participants (97.2%) reported holding a bachelor’s or master’s degree, and 87.4% indicated
either native English proficiency or full professional English competency.
All participants reported familiarity with at least two major social media platforms (Facebook,
Instagram, X/Twitter, TikTok, Reddit) and used social media for various purposes: 86.7% for social-
izing, 77.8% for news consumption, 78.1% for professional networking, and 68% for entertainment.
65% expressed interest in all four topics used in the influence campaigns, while all participants
indicated interest in at least two topics.
Of the 225 recruited participants, 86 actively engaged with the experimental platform, with 32
participating daily and 54 exhibiting sporadic engagement patterns. All experimental protocols
were approved by Northwestern University’s Institutional Review Board, and informed consent
was obtained from all participants.
3.2 Materials
Because all major social platforms ban the creation of bot accounts and the running of CSIOs, we
used the DartPost platform [31] that was explicitly designed to mirror real-world social platforms
for the purpose of running IRB-approved experiments in a legal and ethical manner. Following
[24], we used 305 accounts (225 humans, 80 bots) and ran four concurrent CSIOs, each controlling
20 bots through an RL_CSIO agent. The campaigns promoted positive sentiment toward: (1) U.S.
government COVID-19 response adequacy, (2) implementing a 2% wealth tax on assets exceeding
$50 million, (3) “Medicare for all who want it” policy, and (4) GMO food safety.
RL_CSIO Agent Architecture.The RL_CSIO agent utilized is from [ 24] and uses an actor-critic
RL architecture. It models the social influence task as a Markov Decision Process (MDP) where the
agent controls its bots to balance two competing objectives: maximizing influence spread while
minimizing detection by an automated bot detection algorithm.
The agent architecture has three key components: (1) a Graph Convolutional Network (GCN)
encoder that processed the social network state, including both graph topology and user attributes
such as follower counts, posting behavior, and sentiment; (2) an actor network that generated
probability distributions over possible actions for each controlled bot account; and (3) a critic
network that estimated the value function for state-action pairs to guide policy optimization.
The state representation captures the dynamic social network at each timestep, encoding account
attributes (role, centrality, polarity, blocked status, activity level) and network relationships. The
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:5
action space includes posting content with specified sentiment polarity, following other accounts,
liking posts, remaining inactive, and activating dormant accounts from the agent’s reserve pool.
Reward Structure and Learning DynamicsThe RL_CSIO agent [24] optimizes a multi-component
reward function that captures the dual objectives of influence operations. The reward structure
includes: (1) activation rewards for gaining new human followers; (2) infection rewards for influenc-
ing neighbors’ sentiment toward the target topic; (3) termination rewards for achieving complete
sentiment conversion; and (4) penalties when accounts were suspended by the bot detector.
This reward design encourages agents to develop sophisticated strategies that avoid detection
while achieving influence. Agents learn to vary posting frequencies, adjust content sentiment,
strategically time interactions, and manage account activation patterns to evade both AI and human
detection mechanisms.
Training and DeploymentAs in [ 24], prior to deployment, RL_CSIO agents underwent extensive
training in synthetic environments populated with simulated accounts. The training environment
replicated realistic social media dynamics, with simulated users exhibiting probabilistic behaviors
for content creation, engagement, and inactivity. Simulated accounts updated their sentiment
polarities through exponentially weighted moving averages based on content exposure, modeling
gradual opinion shifts observed in real social influence processes.
During deployment, each CSIO campaign began with five active bot accounts, plus access to 15
additional accounts for strategic activation when suspensions of their active accounts occurred
following detection. The social network was initialized with realistic follower distributions (3–6
connections per account on average) mimicking real-world social media topologies.
Following [24], we used the bot detector proposed in [ 15], which employs a random forest
classifier that periodically scanned all 305 accounts using behavioral features (e.g., posting frequency,
follower growth patterns, and network characteristics).
3.3 Procedure
Participants engaged with the DartPost platform [31] for at least 30 minutes daily over five consec-
utive days. DartPost replicated key functionalities of mainstream social media, including posting,
liking, following, and content discovery features (e.g., a homepage with trends and most viral
content).
Daily data collection also included comprehensive surveys administered at the end of each
experiment day. These surveys captured: (1) participants’ stance toward each campaign topic using
5-point Likert scales, and (2) reports of accounts suspected to be bots. To understand whether
participants were able to enhance their bot detection abilities over time in a natural setting without
ground truth feedback, they were not told if the accounts they reported were really bots or not. To
ensure data quality, surveys included attention checks requiring participants to correctly identify
specific platform features and recall basic experimental parameters.
Additional behavioral data was automatically collected throughout each session, including all
platform interactions (posts, likes, follows), content engagement patterns, and temporal activity
distributions. Platform-generated metrics tracked account suspension events, interaction networks,
and content propagation patterns.
Participants received daily email reminders to complete their tasks, with monetary incentives
tied to task completion and bonus rewards for high engagement levels and accurate bot detection
performance. Only participants who completed the daily requirements received compensation,
though re-engagement in subsequent days was permitted regardless of previous participation gaps.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:6 La Gatta et al.
4 Results
4.1 Demographic Characteristics
To examine how individual characteristics influence bot detection capabilities, we analyzed per-
formance differences across various demographic factors. Table 1 presents F1-scores for the bot
class across demographic groups, with statistical comparisons conducted using permutation testing
[11, 16].All 𝑝-values reported in this paper include adjustments for multiple hypothesis testing using
the Benjamini–Hochberg false discovery rate (FDR) correction. Statistical significance was assessed
using conventional thresholds: *𝑝<0.05, **𝑝<0.01, ***𝑝<0.001.
Hypothesis 1.
Female and male participants have similar bot detection performance.
Male participants achieved an F1-score of 0.454 (𝑁= 65) while female participants scored 0.435
(𝑁= 21), showing no statistically significant difference in bot detection abilities (FDR-corrected
𝑝= 0.902). The performance gap of 0.019 between groups is not statistically significant, thus
confirming our hypothesis.
Hypothesis 2.
Younger participants (under 35 years old) are better at detecting bots compared to older participants
(35 years and above).
We split participants based on whether they were younger or older than 35 years because people
under 35 are considered to be "digital natives", i.e., the first generation to grow up entirely immersed
in digital environments, social media, and online interactions from early childhood§. Contrary to
expectations, older participants (≥ 35 years) significantly outperformed younger participants (<
35 years) in bot detection, achieving F1-scores of 0.570 versus 0.344 respectively (FDR-corrected
𝑝= 0.045). The older group (𝑁= 25) demonstrated a substantial 0.226-point advantage over the
younger group (𝑁= 61). Not only is our hypothesis rejected, but in fact,people over 35 years of age
performed better than those below 35 at detecting bots.
Hypothesis 3.
Native speakers have higher bot detection capabilities than non-native English speakers.
Native English speakers substantially outperformed non-native speakers, achieving F1-scores of
0.516 versus 0.153 respectively (FDR-corrected𝑝= 0.009). This represents a striking 0.363-point
performance gap, with native speakers (𝑁= 49) showing more than three times the detection
capability of non-native speakers (𝑁= 37). Therefore, our hypothesis is confirmed - native speak-
ers exhibit significantly better bot detection capabilities than non-native English speakers. This
substantial difference may reflect deeper familiarity with the specific topics promoted by the bots
rather than purely linguistic advantages, i.e., native English speakers located in the U.S. may possess
greater contextual knowledge about the influence campaigns discussed in the experiment (e.g., U.S.
government’s COVID-19 response adequacy, or "Medicare for all who want it" policies).
Hypothesis 4.
Participants with a higher educational background (master’s degree or above) are better at detecting
bots than those with lower educational levels.
§https://www.techtarget.com/whatis/definition/digital-native
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:7
Table 1. Bot Detection Performance by Demographics. F1-scores represent performance on the bot class.
Statistical comparisons are made between different groups using permutation testing.
Demographic Group N F1 FDR-corrected
Factor𝜇 𝜎p-value
Gender Male 65 0.454 0.030 0.902Female 21 0.435 0.047
Age <3561 0.344 0.044 0.045∗
≥3525 0.570 0.032
English
Proficiency
Native 49 0.516 0.028 0.009∗∗
Non-native 37 0.153 0.025
Education Master’s+ 72 0.068 0.023 0.028∗
Bachelor’s- 14 0.542 0.021
Twitter
Usage
User 57 0.496 0.032 0.646Non-user 29 0.350 0.043
Reddit
Usage
User 30 0.277 0.061 0.208Non-user 56 0.538 0.029
Participants with lower educational levels (bachelor’s degree or below) dramatically outperformed
those with master’s degrees or higher, achieving F1-scores of 0.542 versus 0.068 respectively (FDR-
corrected𝑝= 0.028).Despite the smaller sample size ( 𝑁= 14vs 𝑁= 72), the lower-education group
showed nearly eight times better detection performance.Our hypothesis is thus rejected. This result
may be because highly educated subjects had preconceived notions of what bots should look like
(e.g., repetitive posting patterns, poor grammar), leading them to search for stereotypical indicators
that RL-based bots quickly learned to avoid.
Hypothesis 5.
Participants who use social media platforms are better at detecting bots compared to those who do not.
Since bots primarily operate within social platforms, we expect that users who frequently use
these platforms would develop intuitions about authentic user behavior, content patterns, and
interaction dynamics that could translate into better bot detection performance. We examined
two platforms: Twitter (now X) and Reddit, given their prominence in bot-related discussions
[17, 34, 40, 48] and DartPost’s similarity to Twitter’s interface. For each platform, "non-users" refers
to participants who reported not using that specific platform, rather than non-users of social media
generally.
Our results show mixed, non-significant patterns across platforms. Twitter users ( 𝑁= 57)
achieved a higher F1-score of 0.496 compared to 0.350 for non-users (𝑁= 29), but the 0.146-point
difference was not statistically significant (FDR-corrected𝑝= 0.646). Conversely, participants who
do not use Reddit (𝑁= 56) outperformed Reddit users (𝑁= 30) with F1-scores of 0.538 versus 0.277,
representing a 0.261-point advantage, though this difference was also not statistically significant
(FDR-corrected𝑝=0.208).
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:8 La Gatta et al.
1 2 3 4 5
Day
0.0
0.1
0.2
0.3
0.4
0.5Score
Precision
Recall
F1
(a)
1 2 3 4 5
Day
0.0
0.1
0.2
0.3
0.4
0.5Score
Precision
Recall
F1 (b)
Fig. 1. Human bot detection performance across the five-day experiment. (a) Day-specific: accounts classified
as bots if reported on that specific day. (b) Cumulative: accounts classified as bots if reported on any day up
to and including the current day.
To further disentangle platform-specific effects, we compared Twitter-only users (those reporting
Twitter but not Reddit usage) against all other participants and found no significant difference (FDR-
corrected𝑝= 0.342). An insufficient number of Reddit-only users (𝑁= 5) prevented symmetric
analysis.
Overall, our hypothesis is rejected: social media platform usage does not systematically improve
bot detection performance. This result is in line with prior work [22] showing that greater social
media experience does not guarantee improved accuracy and may foster overconfidence.
4.2 Temporal Learning Effects
Hypothesis 6.
Participants’ bot detection performance improves progressively throughout the five-day experiment.
RL-based bots in our experiment were trained to evade an automatic detector rather than human
judgment. Therefore, we study if humans implicitly learnt bots’ behavioral patterns over time, even
without explicit feedback on their reports.
We analyzed performance over five days using two methods.Day-specificanalysis evaluated
detection accuracy separately for each day, classifying an account as a bot if it was reported at least
once that day. Thecumulativeapproach considered an account as a bot if it was reported on any
day up to and including the current one.
Results indicate no evidence that human participants learned over time for both the day-specific
and cumulative approaches. There were only five incorrect reports on day 1, yielding zero precision,
recall, and F1-scores on the bot class. From day 2 onward, performance was stable, with minimal day-
to-day variation across all metrics (see Figure 1 for visual trends). Linear regression models usingday
as the predictor of F1 score confirmed no improvement: for theday-specificanalysis, 𝛽= 3.10× 10−4
(FDR-corrected𝑝= 0.987), and for thecumulativeanalysis, 𝛽= 5.44× 10−2 (𝑝= 0.379), both
statistically non-significant. We therefore reject our hypothesis:Human participants exhibited no
measurable learning or adaptation, maintaining consistent detection performance throughout the
experiment.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:9
0 20 40 60 80 100
BER (%)
0.2
0.0
0.2
0.4
0.6
0.8
1.0
Score
precision
recall
f1
(a)
0 20 40 60 80 100
BER (%)
0.0
0.2
0.4
0.6
0.8
1.0
1.2Score
precision
recall
f1 (b)
50 60 70 80 90 100
BXR (%)
0.0
0.2
0.4
0.6
0.8
1.0Score
precision
recall
f1 (c)
0 20 40 60 80 100
BXR (%)
0.0
0.2
0.4
0.6
0.8
1.0Score (d)
Fig. 2. Relationship between bot interaction patterns and detection performance. (a-b) Bot Engagement Ratio
(BER): proportion of user’s outgoing interactions (follows-likes) directed toward bots. (c-d) Bot Exposure
Ratio (BXR): proportion of incoming interactions (follows-likes) received from bots.
4.3 Social Media Activity
To examine the relationship between human social media activity and their bot detection ability,
we define two complementary metrics: (i) Bot Engagement Ratio (𝐵𝐸𝑅) measures the proportion of
a user’s outgoing interactions directed toward bot accounts, calculated separately for likes (𝐵𝐸𝑅 like)
and follows (𝐵𝐸𝑅 follow). (ii) Bot Exposure Ratio (𝐵𝑋𝑅 ) is the proportion of incoming interactions
a user receives from bots, again measured for both likes (𝐵𝑋𝑅 like) and follows (𝐵𝑋𝑅 follow). These
metrics capture distinct aspects of human-bot interaction: BER reflects users’ voluntary engagement
with bot-generated content, while BXR represents exposure to bot activity regardless of user intent.
Hypothesis 7.
Users who engage more frequently with bots have a higher bot detection performance compared to
participants with lower engagement levels.
Figures 2a and 2b present detection performance metrics (precision, recall, F1-score on the bot
class) as a function of 𝐵𝐸𝑅 follow and𝐵𝐸𝑅 like, respectively. We observe positive trends across all
metrics. To validate these results, we also fitted linear regression models with detection performance
as the dependent variable and𝐵𝐸𝑅 follow and𝐵𝐸𝑅 like as predictors. For𝐵𝐸𝑅 follow, we find𝛽= 0.004
(FDR-corrected 𝑝= 0.003) for precision, 𝛽= 0.007(FDR-corrected 𝑝= 0.003) for recall, and
𝛽= 0.005(FDR-corrected 𝑝= 0.003) for F1-score. Similarly, for 𝐵𝐸𝑅 like, we observe 𝛽= 0.005
(FDR-corrected𝑝= 1.7× 10−4) for precision,𝛽= 0.007(FDR-corrected 𝑝= 0.001) for recall, and
𝛽= 0.006(FDR-corrected 𝑝= 7.1× 10−5) for F1-score. Table 6 in Appendix A shows full regression
statistics. Overall, these results confirm our hypothesis:users who engage more frequently with bot
accounts develop enhanced detection capabilities.
Hypothesis 8.
Users who receive a higher volume of interactions initiated by bot accounts are better at detecting bots
than those who receive fewer such bot interactions.
Figures 2c and 2d show detection performance metrics (precision, recall, F1-score) as a function
of bot exposure ratios,𝐵𝑋𝑅 follow and𝐵𝑋𝑅 like, respectively. We fitted analogous linear regression
models using𝐵𝑋𝑅 like and𝐵𝑋𝑅 follow as predictors.
The patterns diverge substantially between interaction types. For𝐵𝑋𝑅 like, we observe a positive
relationship similar to the engagement metrics:𝛽= 0.005(FDR-corrected 𝑝= 0.033) for precision,
𝛽= 0.008(FDR-corrected 𝑝= 0.044) for recall, and 𝛽= 0.007(FDR-corrected 𝑝= 0.017) for
F1-score. This aligns with evidence from the original experiment [24] where increased views of
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:10 La Gatta et al.
0 1 2 3 4
No. Reports (k)
0.0
0.2
0.4
0.6
0.8
1.0P(bot | k reports)
N=228
N=30
N=19
N=9
N=7P(bot|k reports)
P(bot) = 0.262
Fig. 3. Conditional probability of bot given it was reported 𝑘 times,𝑃(𝑏𝑜𝑡|𝑘) . The red dashed line shows the
overall proportion of bots in the original experiment (0.262).
bot content improved human detection capabilities. In contrast, 𝐵𝑋𝑅 follow shows no significant
relationship with detection performance (FDR-corrected𝑝> 0.70). This difference likely depends
on the nature of each interaction type. Each time that a bot likes a user’s post, the user receives a
notification in their Dartpost’s feed, and may inspect the bot’s profile, providing direct exposure to
the bot’s behavioral patterns. In contrast, when a bot follows a user, this generates only a one-time
notification and does not entail ongoing exposure to the bot’s content or activity.
These results provide partial support for our hypothesis:users receiving observable interactions
from bots (likes) show improved detection performance, while passive follower relationships which do
not translate into behavioral exposure show no effect.
Taken together, the results from both hypotheses reveal significant differences between active
engagement (𝐵𝐸𝑅) by users and passive exposure (𝐵𝑋𝑅 ). The consistent positive effects of 𝐵𝐸𝑅
across both likes and follows, compared with the weak and inconsistent effects of𝐵𝑋𝑅 , suggest
that active engagement with bot content drives improvement in humans’ detection ability. Users
who voluntarily interact with bots may develop mental models of bot behavior patterns through
direct experience which may help them better detect bots in the future. Passive exposure, by
contrast, improves detection only when it involves observable interactions (likes) that prompt
users to examine bot accounts, rather than mere follower relationships that provide no behavioral
information.
4.4 Collective Intelligence
Hypothesis 9.
Accounts reported as bots multiple times have a higher probability of actually being bots compared to
accounts reported by single participants.
Multiple participants, even across different days, could report accounts as bots. Figure 3 shows
the conditional probability that an account is a bot given it was reported𝑘times:
𝑃(𝑏𝑜𝑡|𝑘)= No. of actual bot accounts reported𝑘times No. of accounts reported𝑘times
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:11
In line with [24], the baseline probability of an account being a bot is0.262(80 bots out of 305
accounts). We observe a clear positive relationship between report frequency and bot probability.
Accounts reported once (𝑁= 30) show 𝑃(𝑏𝑜𝑡|𝑘= 1)= 0.467, nearly double the baseline rate.
This probability increases further to0.632for accounts reported twice (𝑁= 19), and to0.857for
accounts reported four times (𝑁= 7). We omit results for larger𝑘 as they are extremely sparse, i.e.,
𝑁≤3for any𝑘∈[5,11].
Interestingly, unreported accounts (𝑁= 228) exhibit𝑃(𝑏𝑜𝑡|𝑘= 0)= 0.167, substantially below
the baseline (0.262). This indicates that unreported accounts are less likely to be bots than the
average account. However, the fact that 75% (228 out of 305) of accounts—including 38 actual
bots—were unreported exposes a major coverage limitation: collective detection, while accurate
where it occurs, operates over a narrow subset of the population, potentially missing bots.
These results provide strong support for our hypothesis:report frequency is a reliable, but imperfect,
indicator of bot likelihood.However, they also highlight a fundamental trade-off: aggregated human
reporting exhibits valuable collective intelligence but suffers from severe coverage constraints that
may limit its systemic effectiveness.
Hypothesis 10.
Aggregating reports weighted by reporters’ F1-scores achieves better bot detection performance than
classifying bots based solely on whether they exceed a fixed number of reports.
We test whether incorporating the quality of each reporter further enhances detection accuracy.
While multiple reports generally increase confidence, not all participants display the same detection
ability. To address this heterogeneity, we compare two aggregation strategies that differ in how
they combine human judgments.
TheCount-based strategyclassifies an account as a bot if there are at least 𝑘 independent reports
that it is a bot:
𝑎is bot⇐⇒ |𝑅(𝑎)|≥𝑘
where𝑅(𝑎) denotes the set of reports for account𝑎, and𝑘∈{ 1, 2, 3, 4, 5} is a reporting threshold.
This approach assumes all reports are equally informative, regardless of reporter skill.
TheQuality-weighted strategyinstead accounts for reporter reliability by weighting each report
by the reporter’s F1-score:
𝑠(𝑎)=
∑︁
𝑖∈𝑅(𝑎)
𝐹1 𝑖
An account is deemed a bot if 𝑠(𝑎)≥𝜏= 0.533. This threshold (0.533) represents the mean F1-
score across all reporters, and corresponds to the evidence contributed by one average-performing
reporter⁄pilcrow.
Both strategies operate independently of ground-truth labels and are equally affected by the
coverage limitation observed earlier (Hypothesis 9), whereby many accounts remain unreported.
Table 2 summarizes performance. As expected, increasing𝑘 in the count-based strategy reduces
recall by overlooking true bots. However, precision does not improve consistently, peaking at𝑘= 3
(0.666) and then declining for higher𝑘 values, indicating that frequent reports from uninformed
users can reduce accuracy. The highest F1-score (0.549) occurs at 𝑘= 1, suggesting that report
volume alone is an unreliable indicator of detection quality.
⁄pilcrowThis setting simulates a realistic scenario in which platforms maintain reporter reliability scores via periodic audits.
Because participants received no feedback and showed no significant learning effects (Hypothesis 6), their end-of-experiment
performance serves as a reasonable proxy for capabilities throughout this study.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:12 La Gatta et al.
Table 2. Performance comparison of two aggregation strategies in terms precision, recall, F1-score on the bot
class along with overall accuracy. Count-based: flag account as bot if reported at least𝑘 times (treating all
reports equally). Quality-weighted: give more weight to reports from human reporters who performed better
(in terms of F1-score) at bot detection, then flag accounts exceeding a weighted score threshold𝜏= 0.533
(mean reporter F1).
Strategy Threshold Precision Recall F1 Accuracy
Count-based: All reports weighted equally
Count-based𝑘=1 0.575 0.525 0.549 0.584
Count-based𝑘=2 0.589 0.413 0.485 0.578
Count-based𝑘=3 0.666 0.325 0.436 0.596
Count-based𝑘=4 0.647 0.275 0.385 0.578
Count-based𝑘=5 0.608 0.175 0.272 0.548
Quality-weighted vs Count-based
Count-based𝑘=1 0.575 0.525 0.549 0.584
Quality-weighted Mean F1 (0.533) 0.672 0.513 0.582 0.645
Difference +14.4% -2.30% +5.67% +9.46%
Comparing the bestCount-basedstrategy ( 𝑘= 1) to theQuality-weightedapproach reveals an
advantage for the latter: precision increases by 14.4% (0.575→ 0.672), recall decreases slightly by
-2.3%, leading to a 5.67% relative F1 improvement (0.549→ 0.582). The two methods agree on 92.7%
of classifications, diverging on 12 accounts—all correctly resolved by theQuality-weightedstrategy.
We find that this difference is statistically significant. A Chi-square test yields 𝜒 2 = 117.2, FDR-
corrected𝑝= 1.99× 10−27, and McNemar’s test on disagreements yields𝜒 2 = 1.0, FDR-corrected
for multiple hypothesis testing𝑝=0.006.
Overall, these findings provide strong support for Hypothesis 10, highlighting that incorporating
reporter reliability can enhance collective human detection performance.
4.5 Human Ensemble vs. ML Bot Detectors
We evaluated the performance of human ensembles (“crowds”) against several SOTA AI detectors. In-
dividual human predictions were aggregated using thequality-weightedstrategy (cf. Hypothesis 10),
where each report is weighted by the reporter’s individual F1-score.
We compared the human ensemble with three recent bot detectors:(i) RFS[ 15] and(ii) Bot-
Buster[ 38] employ hand-crafted features based on behavioral patterns and metadata (e.g., follower
counts, posting frequency).(iii) LLM-based Detector[ 13] utilizes a prompt-based approach with in-
context examples for bot identification. We instantiated this baseline with four LLMs:llama3.1:8b,
llama3.1:70b,mistral:7b,mistral:24b.
Hypothesis 11.
Human ensembles are better at detecting bots than AI bot detectors.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:13
Table 3. Human Ensemble vs. AI Bot Detection Performance: Precision, Recall, and F1-score on the bot class,
along with overall Accuracy. For all detectors except the LLM-based baseline, "Training Dataset" refers to
the dataset used for training. For the LLM-based baseline, the column lists the LLM under analysis. Bold
indicates the best performance, and underline indicates the first runner-up.
Method Training Dataset Precision Recall F1 Accuracy
Human Ensemble Detection
Humans N/A0.6720.513 0.5820.645
AI Detection
BotBuster [38]
Twibot-20 0.564 0.600 0.582 0.558
Cresci-2017 0.539 0.425 0.476 0.519
Caverlee-2011 0.437 0.388 0.411 0.429
RFS [15]
Twibot-20 0.491 0.650 0.559 0.474
Cresci-2017 0.400 0.400 0.400 0.385
Caverlee-2011 0.5131.000 0.6780.513
LLM-based [13]
llama 3.1:8b0.501 0.448 0.474 0.530
llama 3.1:70b0.494 0.475 0.484 0.481
mistral:7b0.350 0.087 0.140 0.482
mistral:24b0.513 0.950 0.667 0.513
All AI detectors were pretrained on standard benchmarks—Twibot-20 [ 12], Cresci-2017 [ 9],
and Caverlee-2011 [27]—and deployed on our experimental dataset∥. This setup emulates realistic
operational conditions in which detectors face novel, unseen influence campaigns. See Appendix B
for benchmark performance∗∗ We assess human performance over all 305 accounts, treating the
human “crowd” as a full ensemble-based detection system in which unreported accounts are
implicitly considered human.
Table 3 presents performance in terms of precision, recall, F1-score on the bot class, and overall
accuracy. Human ensembles achieved the highest precision on the bot class (0.672) and overall
accuracy (0.645), while AI approaches generally attained higher recall.
However, these patterns reflect fundamentally different failure modes rather than calibration
differences.
One AI detector (RFS trained on Caverlee-2011) collapses by predicting all accounts as bots.
Indeed, it achieved perfect recall (1.000) but near-chance precision (0.513). Among the others, a
consistent recall-over-precision bias emerges: RFS on Twibot-20 (precision 0.491, recall 0.650),
mistral:24b (precision 0.513, recall 0.950), and BotBuster on Twibot-20 (precision 0.564, recall
0.600).
Humans show the inverse pattern, higher precision than recall, but for a distinct reason: incom-
plete coverage rather than conservative classification. Of the 305 accounts, 228 (including 38 bots)
were never reported by any participant, thus reducing recall. Importantly, this does not indicate
that humans are more cautious classifiers; rather, they only evaluate a subset of accounts, and
∥Fine-tuning on our experimental data was not performed to maintain realism as, in the real-world, we would not be
able to fine-tune models on an actual bot campaign before it started.
∗∗All detectors exhibited lower performance on our experimental data compared to their original benchmark test sets,
reflecting the challenges of out-of-distribution (OOD) evaluation [ 43, 52] and detecting adaptive bots powered by RL.
Although methods like BotBuster emphasize improved generalization to unseen data, addressing OOD robustness is beyond
the scope and contributions of this study.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:14 La Gatta et al.
HumansBotBuster
RFS
llama:70bmistral:24b
Humans
BotBuster
RFS
llama:70b
mistral:24b
100% 51.9%46.2%54.5%46.2%
100% 66.5%63.3%66.5%
100% 61.4%94.9%
100% 66.5%
100%
 0
20
40
60
80
100
Agreement Rate (%)
(a)
HumansBotBuster
RFS
llama:70bmistral:24b
Humans
BotBuster
RFS
llama:70b
mistral:24b
1 0.045 0.000 0.089 0.007
1 0.200 0.227 0.210
1 0.200 0.740
1 0.300
1
0.0
0.2
0.4
0.6
0.8
1.0
Cohen's Kappa (b)
Fig. 4. Human vs AI Comparison: Pairwise Agreement Rate (a) and Cohen’s 𝜅 (b) for humans and the best
performing detectors, i.e., BotBuster (trained on Twibot-20), RFS (trained on Caverlee-2011), LLM-based
(llama:70b), and LLM-based (mistral-24b).
within that subset, their precision remains 0.672. The coverage gap, not classification threshold,
drives the precision-recall asymmetry.
To understand whether humans and AI algorithms identify the same bots, we analyzed pairwise
agreement across all detection methods and humans. Figure 4 presents pairwise agreement in
terms of raw agreement rate and Cohen’s𝜅 values between humans and the best-performing AI
models. We find minimal agreement: humans and AI algorithms achieved agreement rates ranging
from 46.2% (RFS) to 54.5% ( llama:70b), with𝜅 values close to zero (𝜅∈[ 0.0, 0.089]). Similarly,
AI methods have little mutual consistency (e.g., BotBuster vs. llama:70b:𝜅= 0.20). The only
exception is the RFS-mistral:24b pair where agreement rate is 94.9% and𝜅= 0.74, and it depends
on the fact that the two detectors tend to classify every account as a bot (bot recall> 0.9in Table 3).
This lack of concordance demonstrates that humans and AI algorithms do not merely differ in
accuracy but also in the type of evidence they rely upon. Rather than detecting the same bots with
varying success, they appear to target disjoint subsets of accounts using fundamentally different
heuristics and behavioral indicators.Overall, these findings partially support our hypothesis: humans
show superior precision but markedly lower recall and F1-scores than AI detectors.In addition, the low
agreement between humans and AI algorithms indicates complementarity rather than redundancy.
Hypothesis 12.
Combining human reports with AI predictions improves bot detection performance compared to
using either source alone.
We combine human reports and AI predictions using 7 strategies in two categories: model-only
ensembles that combine AI detectors, and hybrid ensembles that additionally incorporate human
reports.
• Model-only ensemble: We evaluate three standard ensemble methods: (i)Hard Voting, which
assigns the majority label across detectors; (ii)Soft Voting, which averages predicted proba-
bilities; and (iii)Late Fusion, which computes a weighted average of probabilities.
• Hybrid ensemble: We evaluate four strategies that integrate human reports with AI predic-
tions [55]. (iv)Human Firstapplies soft voting to AI predictions to obtain an interim vote,
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:15
then combines this interim vote with all individual human reports via hard voting. (v)Model
Firstaggregates human reports using the quality-weighted approach (cf. Hypothesis 10), then
combines this with AI predictions via soft voting. (vi)Meta Votingenumerates all possible
subgroups of voters (both human and AI), computes both hard and soft voting outcomes
within each subgroup, and reaches a final decision by hard voting over all subgroup outcomes.
(vii)Hybrid Late Fusionextends the model-only variant by including human reports as an
additional source, weighted by individual reporter F1-scores.
These strategies require optimization on held-out data. As soft voting requires the selection
of a probability threshold, we evaluated thresholds from 0.5 to 0.95 and selected 0.71 based on
validation F1-score. As late fusion requires weight optimization, we randomly sampled 1,000
weight configurations (constrained to sum to 1) and retained the configuration with the highest
validation F1-score. Hybrid strategies inherit these optimization procedures from their model-only
counterparts.
To enable this optimization and ensure fair comparison across all strategies and individual
models, we fine-tuned all detectors on our experimental data using 5-fold cross-validation††. We
selected 5-fold over 10-fold cross-validation because it provides a more favorable training-to-test
ratio (80%-20% vs. 90%-10%), ensuring sufficient training data for fine-tuning LLM-based detectors
while maintaining stable evaluation. Specifically, we retrained BotBuster and RFS from scratch
using Dartpost training data in each fold, while we fine-tuned llama:70b and mistral:24b using
LoRA (Low-Rank Adaptation) for parameter-efficient updates.
Table 4 presents results across all aggregation strategies. ‡‡. Unsurprisingly, fine-tuning sub-
stantially improves individual detector performance compared to the pretrained-only setting (cf.
Table 3): RFS achieves an F1-score of 0.723 (vs. 0.559 pretrained on Twibot-20), and LLM-based
detection with llama:70b reaches 0.749 (vs. 0.484 pretrained). Human ensemble performance
remains unchanged at 0.582 F1, as no fine-tuning applies.
Model-only ensemblesimprove over individual detectors. Among these methods,Late Fusion
achieves the best precision (0.831), accuracy (0.777), and F1-score (0.745), whileSoft Votingattains
the highest recall (0.850). However, hybrid ensembles yield further gains across most metrics.
Hybrid Late Fusionachieves the highest precision (0.871) and accuracy (0.795), improving +4.0
percentage points in precision and +1.8 points in accuracy over its model-only counterpart. It also
achieves the second-best F1-score (0.761) among all methods. This gain stems from incorporating
high-performing human reports without inheriting their coverage limitation: the optimized model
weights maintain recall at 0.675 while human contributions boost precision.
Meta Votingachieves the highest F1-score (0.801), outperforming the best individual detector
(llama:70b, F1 = 0.749) by 5.2 percentage points and the best model-only ensemble (Late Fusion,
F1 = 0.745) by 5.6 points. Unlike late fusion, which maximizes precision,Meta Votingachieves a
more balanced precision-recall trade-off by leveraging agreement patterns across all possible voter
combinations: when any subgroup of humans and detectors agree on an account, that agreement
gets captured even if other sources disagree. In contrast,Human FirstandModel Firstrequire
majority agreement, missing bots detected by only a few sources.
Overall, these findings support our hypothesis: combining human reports with AI predictions improves
bot detection performance.
††This setup resolves the out-of-distribution limitations observed in the previous hypothesis.
‡‡We do not report AUC as it cannot be measured for aggregation strategies producing discrete classifications (e.g., Hard
Voting, Meta Voting).
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:16 La Gatta et al.
Table 4. Aggregation strategies for bot detection. “No Aggregation” shows individual detector and human
ensemble performance after fine-tuning. “Models-only” combines AI detectors. “Hybrid” integrates human
reports with AI predictions. Bold indicates best performance per metric; underline indicates second-best
performer.
Aggregation
Method Precision Recall F1 Accuracy
No
Aggregation
Humans 0.672 0.513 0.582 0.645
BotBuster 0.567 0.675 0.606 0.605
RFS 0.739 0.708 0.723 0.719
LLM-based
(llama:70b) 0.709 0.793 0.749 0.684
LLM-based
(mistral:24b) 0.688 0.766 0.703 0.619
AI Models-only
Hard Voting 0.677 0.811 0.738 0.723
Soft Voting 0.6600.8500.740 0.717
Late Fusion 0.831 0.675 0.745 0.777
Hybrid
Human First 0.677 0.812 0.738 0.723
Model First 0.723 0.750 0.736 0.741
Meta Voting 0.741 0.7460.8010.761
Late Fusion0.8710.675 0.761 0.795
Hypothesis 13.
Human reports provide effective supervision for incrementally retraining bot detectors.
We now investigate whether human reports can improve detectors at training time by serving as
supervision for incremental retraining. We design a time-based retraining protocol that simulates
incremental deployment. On each day𝐷, we retrain each detector using its original benchmark
data augmented with accounts discovered on days 1 through𝐷− 1, then evaluate on accounts on
day𝐷. This protocol mirrors realistic deployment where detectors are periodically updated with
newly acquired data.
We compare three supervision strategies for selecting retraining instances:
• Ground-Truth Supervision.The detector is retrained on instances where its previous bot
predictions were correct. This strategy represents an ideal scenario because it requires access
to ground-truth labels.
• Self-Supervision.The detector is retrained on instances it predicted with confidence exceeding
a reasonable threshold. This strategy requires no access to ground-truth. We evaluated
thresholds from 0.5 to 0.95 and selected 0.7, which achieved the best performance in terms of
F1-score across all detectors. See Appendix B.2.1 for additional results.
• Human Supervision.The detector is retrained on instances reported by human participants
aggregated using thequality-weightedstrategy.
We apply this retraining protocol to four detectors (BotBuster, RFS, LLM-based with llama:70b,
and LLM-based with mistral:24b) across three benchmark datasets (Twibot-20, Cresci-2017,
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:17
D1 D2 D3 D4 D5
T est Day
5
0
5
10
15
20
twibot20
F1 Impr. (%)
A
Llama
D1 D2 D3 D4 D5
T est Day
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
B
Mistral
D1 D2 D3 D4 D5
T est Day
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
C
BotBuster
D1 D2 D3 D4 D5
T est Day
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
D
RFS
Baseline (No Improvement) Ground-Truth Supervision Self-Supervision Human Supervision
Fig. 5. Relative F1-score improvement over baseline (no retraining) across experimental days for four detectors
pretrained on Twibot-20. Each subplot shows one detector.Ground-Truth Supervisionretrains on correct
predictions,Self-Supervisionretrains on high-confidence predictions (threshold 0.7), andHuman Supervision
retrains on human reports.
Caverlee-2011), yielding 12 detector-benchmark configurations. For each configuration, we mea-
sure relative F1-score improvement over the baseline detector that is initially pre-trained on the
benchmark dataset and receives no incremental retraining.
Figure 5 shows relative F1-score improvement across experimental days for each detector and
retraining strategy, assuming Twibot-20 as benchmark pre-training dataset. See Appendix B.2 for
results with Cresci-2017 and Caverlee-2011 benchmarks. On Day 1, no improvement is observed
for any strategy because both the baseline and retrained models are trained only on benchmark
data (no experimental accounts are available yet for retraining).
Self-Supervisionyields marginal and inconsistent effects. The maximum improvement is 2.91%
(BotBuster, Day 2), while performance decreases up to -6.8% (llama:70b, Day 3). This instability
reflects the risk of reinforcing errors when retraining on the model’s own predictions.
Ground-Truth Supervisionconsistently improves performance, with gains reaching 17.4% for
BotBuster and RFS on Day 5. This confirms that access to correct labels, while an idealized scenario,
provides reliable supervision for incremental retraining.
Human Supervisiongenerally yields improvements comparable to, and sometimes exceeding,
Ground-Truth Supervision. For llama:70b on Day 4, Human Supervision achieves 20% improvement
compared to 8.5% for Ground-Truth. Similarly, for mistral:24b on Day 3, Human Supervision
reaches 16.2% versus 2.6% for Ground-Truth. This counterintuitive result may be becauseGround-
Truth Supervisiononly retrains on instances the model predicted correctly. When a detector has
relatively few correct predictions, its retraining sample is small and less effective.Human Supervision,
by contrast, provides an independent labeling source that can include instances the model missed.
However, it can also decrease performance, as observed forllama:70b on Days 2 and 3. This occurs
when human reports are insufficient in quantity or unreliable in quality during early experimental
days.
Overall, these findings support our hypothesis: human reports provide effective supervision for
incremental retraining.Human Supervision achieves improvements comparable to Ground-Truth
Supervision without requiring access to ground-truth labels, offering a practical alternative for
real-world deployment.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:18 La Gatta et al.
5 Relevance to Social Platform Security
Over 2000 years have passed since the publication of Sun Tzu’s celebrated book, “The Art of
War”[46]. Yet, his statement that “To know your Enemy, you must become your Enemy” remains
valid. It is widely known that social media companies use a mix of human “content moderators”
and AI to detect bots and entities involved in CSIOs (and for many other purposes)[ 25, 29]. To
protect social platforms from malign covert social influence campaigns, they must “become” the
enemy and understand how malign actors will leverage AI to run CSIOs in the future. As mentioned
earlier, malign actors have already leveraged reinforcement learning to dynamically, adaptively,
and autonomously evade static malware detectors [3, 42], create attack paths through a network
[26], attack graph-neural network based detectors focused on node injection attacks[45], and create
fake reviews in online marketplaces[56]. [24] provides a first message to social platforms that they
need to anticipate and deter future CSIOs that leverage RL.
The findings of this paper, summarized in Table 5, lead us to make several recommendations to
social media companies.
Recommendation 1.Social platforms mustcontinuously monitor bot detection performance
of both human reporters and AI botswithin their defensive arsenal.
This recommendation is based on Hypothesis 10 that shows that quality-based bot detection (in
the human case) is better than merely counting the number of human reports that an account is a
bot.
Recommendation 2.Social platforms shouldincorporate Hybrid (Human + AI) bot detection
within their bot detection infrastructure via either Meta Voting or Late Fusion.
This recommendation is based on Hypothesis 12 (see also Table 4) which suggests that Meta-
voting and Late Fusion achieve the best F1 score and Accuracy, respectively. Such an incorporation
could occur at several levels. For example, Hybrid bot detection could be implemented in order
to determine which accounts should be reviewed by content moderators. Alternatively, consider
platforms with tiered moderation systems (e.g., ordinary moderators and senior trained supervisors).
In the first round, Hybrid detection could combine user reports with AI predictions to flag accounts
for junior moderators. In the second round, it could combine junior moderators’ judgments with
AI predictions to escalate difficult cases to senior supervisors.
Recommendation 3.The human supervision strategy with quality-weighting should be
used for retraining of AI-based bot detectors used by the social platform.
This recommendation is based on Hypothesis 13 which investigates three strategies for retrain-
ing: ground-truth supervision, self-supervision, and human-supervision and finds that human
supervised training using quality-weighting avoids the need for access to ground truth labels and
beats out both other strategies.
6 Limitations
Like any study, ours has several limitations.(i)Our U.S.-based participant sample may limit general-
izability across different geographies.(ii)We evaluated AI detectors trained on benchmark datasets
against experimental data without fine-tuning, creating realistic but challenging out-of-distribution
conditions. While this mirrors many real-world deployments, new moderation systems may use
incremental learning.(iii)The experimental DartPost platform differs from real-world social media,
but must be used as ethical constraints and legal terms of use agreements prevent running CSIOs
on real social platforms.(iv)The five-day experimental window may have been insufficient to
capture learning effects emerging over longer periods, though running experiments over a longer
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:19
Table 5. Summary of hypotheses and key findings.
H# Key Finding
Demographic Characteristics
1 No significant gender difference in bot detection performance
2 Older participants (≥35) outperformed younger “digital natives”
3 Native English speakers showed 3×better detection than non-native speakers
4 Lower education (Bachelor’s or below) associated with 8× better detection in terms of
F1-score
5 Social media platform usage (Twitter, Reddit) showed no systematic benefit
Temporal & Behavioral Factors
6 No learning effects observed over five days without feedback
7 Active engagement with bots improves detection capabilities
8 Exposure to bot behavior via received likes improves detection; follower relationships
show no effect
Collective Intelligence
9 Report frequency indicates bot likelihood, but 75% of accounts were unreported
10 Quality-weighted aggregation outperforms count-based (+5.67% F1, +9.46% Acc.)
Human vs. AI Detection
11 Humans achieve higher precision/accuracy; pre-trained AI achieves higher recall
12 Hybrid ensembles outperform human and AI ensembles
13 Human supervision enables incremental retraining without ground-truth labels
duration present practical challenges.(v)Our analyses focus exclusively on RL-based adaptive bots
[24]—the findings may not generalize to other bot types, campaigns, or coordination strategies.
7 Conclusion & Future Work
This study provides the first systematic investigation of human detection capabilities against
RL-based adaptive bots operating in active CSIOs. Through controlled experimentation with 225
participants across five days, we tested 13 hypotheses spanning individual, social, and collective
factors that shape bot detection performance. Our findings challenge some conventional assump-
tions: older participants outperformed younger digital natives, higher education correlated with
worse detection, and social media platform usage showed no systematic benefit. Temporal analysis
revealed no learning effects, while network centrality had no relationship with detection ability.
Critically, active engagement with bots—not passive exposure—improved detection capabilities,
suggesting that voluntary interaction enables development of behavioral recognition patterns. Col-
lective intelligence analysis showed that report frequency is not a reliable indicator of bot likelihood.
In contrast, accounting for reporter capability yields significantly better detection performance.
Benchmarking against three state-of-the-art AI bot detection algorithms revealed that the human
ensemble performs better than any individual AI detector when both operate under realistic
deployment conditions: humans received no feedback on their reports, while AI detectors were
pretrained on benchmark datasets without fine-tuning on the experimental data. This comparison
reflects scenarios where both humans and AI face novel, unseen influence campaigns. However,
humans and AI detectors appear to complement each other, finding different bots.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:20 La Gatta et al.
We operationalized this complementarity by combining human reports with AI predictions. We
investigated multiple aggregation strategies that integrate both human and AI detectors and show
that the combination outperforms either in isolation: Meta Voting achieves the highest F1-score by
capturing agreement patterns across all voter combinations, while Hybrid Late Fusion maximizes
precision by incorporating high-performing human reports without inheriting their coverage
limitations. Finally, human reports provide effective supervision for incremental retraining.
As mentioned previously, a strong defense requires the ability to “know the enemy”§§. RL-based
attacks are a likely wave in many settings including covert social influence operations. This paper
analyzes human bot detection, AI-based bot detectors, and multiple Hybrid Combinations. We
summarize our key actionable findings into recommendations that social platforms can potentially
incorporate into their bot detection strategies, and which we hope will be useful to these social
platforms inproactivelyprotecting against malign CSIO operators.
References
[1] Aseel Addawood, Adam Badawy, Kristina Lerman, and Emilio Ferrara. 2019. Linguistic cues to deception: Identifying
political trolls on social media. InProceedings of the international AAAI conference on web and social media, Vol. 13.
15–25.
[2] Meysam Alizadeh, Jacob N Shapiro, Cody Buntain, and Joshua A Tucker. 2020. Content-based features predict social
media influence operations.Science advances6, 30 (2020), eabb5824.
[3] Hyrum S Anderson, Anant Kharkar, Bobby Filar, David Evans, and Phil Roth. 2018. Learning to evade static PE machine
learning malware models via reinforcement learning.arXiv preprint arXiv:1801.08917(2018).
[4] Zhouhan Chen and Devika Subramanian. 2018. An Unsupervised Approach to Detect Spam Campaigns that Use
Botnets on Twitter.CoRRabs/1804.05232 (2018). arXiv:1804.05232 http://arxiv.org/abs/1804.05232
[5] Lorenzo Cima, Lorenzo Mannocci, Marco Avvenuti, Maurizio Tesconi, and Stefano Cresci. 2024. Coordinated behavior
in information operations on Twitter.IEEE Access12 (2024), 61568–61585.
[6] Stefano Cresci. 2020. A decade of social bot detection.Commun. ACM63, 10 (2020), 72–83.
[7] Stefano Cresci, Roberto Di Pietro, Marinella Petrocchi, Angelo Spognardi, and Maurizio Tesconi. 2016. DNA-inspired
online behavioral modeling and its application to spambot detection.IEEE Intelligent Systems31, 5 (2016), 58–64.
[8] Stefano Cresci, Roberto Di Pietro, Marinella Petrocchi, Angelo Spognardi, and Maurizio Tesconi. 2017. The paradigm-
shift of social spambots: Evidence, theories, and tools for the arms race. InProceedings of the 26th international conference
on world wide web companion. 963–972.
[9] Stefano Cresci, Roberto Di Pietro, Marinella Petrocchi, Angelo Spognardi, and Maurizio Tesconi. 2017. The Paradigm-
Shift of Social Spambots: Evidence, Theories, and Tools for the Arms Race. InProceedings of the 26th International
Conference on World Wide Web Companion(Perth, Australia)(WWW ’17 Companion). International World Wide Web
Conferences Steering Committee, Republic and Canton of Geneva, CHE, 963–972. doi:10.1145/3041021.3055135
[10] Jinglong Duan, Weihua Li, Quan Bai, Minh Nguyen, Xiaodan Wang, and Jianhua Jiang. 2025. LLM-BotGuard: A Novel
Framework for Detecting LLM-Driven Bots With Mixture of Experts and Graph Neural Networks.IEEE Transactions
on Computational Social Systems(2025), 1–13. doi:10.1109/TCSS.2025.3545822
[11] Michael D Ernst. 2004. Permutation methods: a basis for exact inference.Statist. Sci.(2004), 676–685.
[12] Shangbin Feng, Herun Wan, Ningnan Wang, Jundong Li, and Minnan Luo. 2021. TwiBot-20: A Comprehensive
Twitter Bot Detection Benchmark. InProceedings of the 30th ACM International Conference on Information & Knowledge
Management(Virtual Event, Queensland, Australia)(CIKM ’21). Association for Computing Machinery, New York, NY,
USA, 4485–4494. doi:10.1145/3459637.3482019
[13] Shangbin Feng, Herun Wan, Ningnan Wang, Zhaoxuan Tan, Minnan Luo, and Yulia Tsvetkov. 2024. What Does
the Bot Say? Opportunities and Risks of Large Language Models in Social Media Bot Detection. InProceedings
of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Lun-Wei Ku,
Andre Martins, and Vivek Srikumar (Eds.). Association for Computational Linguistics, Bangkok, Thailand, 3580–3601.
doi:10.18653/v1/2024.acl-long.196
[14] Emilio Ferrara. 2023. Social bot detection in the age of ChatGPT: Challenges and opportunities.First Monday(2023).
[15] Jefferson Viana Fonseca Abreu, Célia Ghedini Ralha, and João José Costa Gondim. 2020. Twitter Bot Detection
with Reduced Feature Set. In2020 IEEE International Conference on Intelligence and Security Informatics (ISI). 1–6.
doi:10.1109/ISI49825.2020.9280525
§§https://militairespectator.nl/artikelen/clausewitz-and-sun-tzu
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:21
[16] Phillip Good. 2013.Permutation tests: a practical guide to resampling methods for testing hypotheses. Springer Science &
Business Media.
[17] Simon Hegelich and Dietmar Janetzko. 2021. Are Social Bots on Twitter Political Actors? Empirical Evidence from a
Ukrainian Social Botnet.Proceedings of the International AAAI Conference on Web and Social Media10, 1 (Aug. 2021),
579–582. doi:10.1609/icwsm.v10i1.14764
[18] Di Huang, Jinbao Song, and Xingyu Zhang. 2025. Semi-Supervised Social Bot Detection with Relational Graph
Attention Transformers and Characteristics of the social environment.Information Fusion118 (2025), 102956.
[19] Haitao Huang, Hu Tian, Xiaolong Zheng, Xingwei Zhang, Daniel Dajun Zeng, and Fei-Yue Wang. 2024. CGNN: A
Compatibility-Aware Graph Neural Network for Social Media Bot Detection.IEEE Transactions on Computational
Social Systems11, 5 (2024), 6528–6543. doi:10.1109/TCSS.2024.3396413
[20] Jane Im, Eshwar Chandrasekharan, Jackson Sargent, Paige Lighthammer, Taylor Denby, Ankit Bhargava, Libby
Hemphill, David Jurgens, and Eric Gilbert. 2020. Still out there: Modeling and Identifying Russian Troll Accounts
on Twitter. InProceedings of the 12th ACM Conference on Web Science(Southampton, United Kingdom)(WebSci ’20).
Association for Computing Machinery, New York, NY, USA, 1–10. doi:10.1145/3394231.3397889
[21] Daniel Kats and Mahmood Sharif. 2022. “I Have No Idea What a Social Bot Is”: On Users’ Perceptions of Social Bots
and Ability to Detect Them. InProceedings of the 10th International Conference on Human-Agent Interaction. 32–40.
[22] Ryan Kenny, Baruch Fischhoff, Alex Davis, Kathleen M Carley, and Casey Canfield. 2024. Duped by bots: why some
are better than others at detecting fake social media personas.Human factors66, 1 (2024), 88–102.
[23] Maxim Kolomeets, Olga Tushkanova, Vasily Desnitsky, Lidia Vitkova, and Andrey Chechulin. 2024. Experimental
evaluation: Can humans recognise social media bots?Big Data and Cognitive Computing8, 3 (2024), 24.
[24] Saurabh Kumar, Valerio La Gatta, Andrea Pugliese, Andrew Pulver, V.S. Subrahmanian, Jiazhi Zhang, and Youzhi
Zhang. 2025. Reinforcement-Learning Based Covert Social Influence Operations. InProceedings of the ACM on Web
Conference 2025(Sydney NSW, Australia)(WWW ’25). Association for Computing Machinery, New York, NY, USA,
2435–2449. doi:10.1145/3696410.3714729
[25] Vivian Lai, Samuel Carton, Rajat Bhatnagar, Q Vera Liao, Yunfeng Zhang, and Chenhao Tan. 2022. Human-ai
collaboration via conditional delegation: A case study of content moderation. InProceedings of the 2022 CHI Conference
on Human Factors in Computing Systems. 1–18.
[26] Hyo Sun Lee, Min Geun Song, and Huy Kang Kim. 2025. An Approach to Creating the Optimal Attack Path Based on
Reinforcement Learning. In2025 IEEE 30th Pacific Rim International Symposium on Dependable Computing (PRDC).
IEEE, 152–157.
[27] Kyumin Lee, Brian Eoff, and James Caverlee. 2021. Seven Months with the Devils: A Long-Term Study of Content
Polluters on Twitter.Proceedings of the International AAAI Conference on Web and Social Media5, 1 (Aug. 2021), 185–192.
doi:10.1609/icwsm.v5i1.14106
[28] Jeffrey Lees, John A Banas, Darren Linvill, Patrick C Meirick, and Patrick Warren. 2023. The Spot the Troll Quiz
game increases accuracy in discerning between real and inauthentic social media accounts.PNAS Nexus2, 4 (03
2023), pgad094. arXiv:https://academic.oup.com/pnasnexus/article-pdf/2/4/pgad094/50997710/pgad094.pdf doi:10.
1093/pnasnexus/pgad094
[29] Adi Levi, Or Levi, Sardhendu Mishra, and Jonathan Morra. 2025. AI vs. Human Moderators: A Comparative Evaluation
of Multimodal LLMs in Content Moderation for Brand Safety. InProceedings of the IEEE/CVF International Conference
on Computer Vision. 5965–5973.
[30] Bjørnar Fidje Liberg. 2021.Risk perception of influence operations on social media. Master’s thesis. NTNU.
[31] Rui Liu, Kevin T Greene, Ruibo Liu, Mihovil Mandic, Benjamin A Valentino, Soroush Vosoughi, and VS Subrahmanian.
2021. Using impression data to improve models of online social influence.Scientific reports11, 1 (2021), 16613.
[32] Luca Luceri, Silvia Giordano, and Emilio Ferrara. 2020. Detecting troll behavior via inverse reinforcement learning: A
case study of russian trolls in the 2016 us election. InProceedings of the international AAAI conference on web and social
media, Vol. 14. 417–427.
[33] Luca Luceri, Valeria Pantè, Keith Burghardt, and Emilio Ferrara. 2024. Unmasking the web of deceit: Uncovering
coordinated activity to expose information operations on twitter. InProceedings of the ACM Web Conference 2024.
2530–2541.
[34] Ming-Cheng Ma and John P. Lalor. 2020. An Empirical Analysis of Human-Bot Interaction on Reddit. InProceedings of
the Sixth Workshop on Noisy User-generated Text (W-NUT 2020), Wei Xu, Alan Ritter, Tim Baldwin, and Afshin Rahimi
(Eds.). Association for Computational Linguistics, Online, 101–106. doi:10.18653/v1/2020.wnut-1.14
[35] Lorenzo Mannocci, Michele Mazza, Anna Monreale, Maurizio Tesconi, and Stefano Cresci. 2024. Detection and
characterization of coordinated online behavior: A survey.arXiv preprint arXiv:2408.01257(2024).
[36] Diego A Martin, Jacob N Shapiro, and Michelle Nedashkovskaya. 2019. Recent trends in online foreign influence
efforts.Journal of Information Warfare18, 3 (2019), 15–48.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:22 La Gatta et al.
[37] Franziska Martini, Paul Samula, Tobias R Keller, and Ulrike Klinger. 2021. Bot, or not? Comparing three methods for
detecting social bots in five political discourses.Big data & society8, 2 (2021), 20539517211033566.
[38] Lynnette Hui Xian Ng and Kathleen M Carley. 2023. Botbuster: Multi-platform bot detection using a mixture of experts.
InProceedings of the international AAAI conference on web and social media, Vol. 17. 686–697.
[39] Diogo Pacheco, Pik-Mai Hui, Christopher Torres-Lugo, Bao Tran Truong, Alessandro Flammini, and Filippo Menczer.
2020. Uncovering coordinated networks on social media.arXiv preprint arXiv:2001.0565816 (2020).
[40] Marian-Andrei Rizoiu, Timothy Graham, Rui Zhang, Yifei Zhang, Robert Ackland, and Lexing Xie. 2018. #DebateNight:
The Role and Influence of Socialbots on Twitter During the 1st 2016 U.S. Presidential Debate.Proceedings of the
International AAAI Conference on Web and Social Media12, 1 (Jun. 2018). doi:10.1609/icwsm.v12i1.15029
[41] Karishma Sharma, Yizhou Zhang, Emilio Ferrara, and Yan Liu. 2021. Identifying coordinated accounts on social media
through hidden influence and group behaviours. InProceedings of the 27th ACM SIGKDD Conference on Knowledge
Discovery & Data Mining. 1441–1451.
[42] Wei Song, Xuezixiang Li, Sadia Afroz, Deepali Garg, Dmitry Kuznetsov, and Heng Yin. 2020. Mab-malware: A
reinforcement learning framework for attacking static malware classifiers.arXiv preprint arXiv:2003.03100(2020).
[43] Yuxuan Song, Qiudan Li, Shu Wu, Zheng Xie, and Daniel Dajun Zeng. 2025. A Self-Supervised Adaptive Tuning
Approach for Out-of-Distribution Social Media Bot Detection. InCompanion Proceedings of the ACM on Web Conference
2025(Sydney NSW, Australia)(WWW ’25). Association for Computing Machinery, New York, NY, USA, 1312–1315.
doi:10.1145/3701716.3715495
[44] Venkatramanan S Subrahmanian, Amos Azaria, Skylar Durst, Vadim Kagan, Aram Galstyan, Kristina Lerman, Linhong
Zhu, Emilio Ferrara, Alessandro Flammini, and Filippo Menczer. 2016. The DARPA Twitter bot challenge.Computer
49, 6 (2016), 38–46.
[45] Yiwei Sun, Suhang Wang, Xianfeng Tang, Tsung-Yu Hsieh, and Vasant Honavar. 2020. Adversarial attacks on graph
neural networks via node injections: A hierarchical reinforcement learning approach. InProceedings of the web
conference 2020. 673–683.
[46] Sun Tzu, Alexander Adams, Samuel B Griffith, and Sunzi. 1963.The art of war. Vol. 84. Oxford University Press Oxford.
[47] Magdalena Wischnewski, Rebecca Bernemann, Thao Ngo, and Nicole Krämer. 2021. Disagree? You Must be a Bot! How
Beliefs Shape Twitter Profile Perceptions. InProceedings of the 2021 CHI Conference on Human Factors in Computing
Systems(Yokohama, Japan)(CHI ’21). Association for Computing Machinery, New York, NY, USA, Article 160, 11 pages.
doi:10.1145/3411764.3445109
[48] Wentao Xu, Kazutoshi Sasahara, Jianxun Chu, Bin Wang, Wenlu Fan, and Zhiwen Hu. 2025. Social media warfare:
investigating human-bot engagement in English, Japanese and German during the Russo-Ukrainian war on Twitter
and Reddit.EPJ Data Science14, 1 (2025), 10.
[49] Harry Yaojun Yan, Kai-Cheng Yang, Filippo Menczer, and James Shanahan. 2021. Asymmetrical perceptions of
partisan political bots.New Media & Society23, 10 (2021), 3016–3037. arXiv:https://doi.org/10.1177/1461444820942744
doi:10.1177/1461444820942744
[50] Kai-Cheng Yang, Emilio Ferrara, and Filippo Menczer. 2022. Botometer 101: Social bot practicum for computational
social scientists.CoRRabs/2201.01608 (2022). arXiv:2201.01608 https://arxiv.org/abs/2201.01608
[51] Kai-Cheng Yang, Onur Varol, Clayton A Davis, Emilio Ferrara, Alessandro Flammini, and Filippo Menczer. 2019.
Arming the public with artificial intelligence to counter social bots.Human Behavior and Emerging Technologies1, 1
(2019), 48–61.
[52] Kai-Cheng Yang, Onur Varol, Pik-Mai Hui, and Filippo Menczer. 2020. Scalable and generalizable social bot detection
through data selection. InProceedings of the AAAI conference on artificial intelligence, Vol. 34. 1096–1103.
[53] Kai-Cheng Yang, Onur Varol, Alexander C Nwala, Mohsen Sayyadiharikandeh, Emilio Ferrara, Alessandro Flammini,
and Filippo Menczer. 2023. Social bots: detection and challenges.arXiv preprint arXiv:2312.17423(2023).
[54] Savvas Zannettou, Tristan Caulfield, William Setzer, Michael Sirivianos, Gianluca Stringhini, and Jeremy Blackburn.
2019. Who let the trolls out? towards understanding state-sponsored trolls. InProceedings of the 10th acm conference
on web science. 353–362.
[55] Xia Zeng, David La Barbera, Kevin Roitero, Arkaitz Zubiaga, and Stefano Mizzaro. 2024. Combining Large Language
Models and Crowdsourcing for Hybrid Human-AI Misinformation Detection. InProceedings of the 47th International
ACM SIGIR Conference on Research and Development in Information Retrieval(Washington DC, USA)(SIGIR ’24).
Association for Computing Machinery, New York, NY, USA, 2332–2336. doi:10.1145/3626772.3657965
[56] Youzhi Zhang, Sayak Chakrabarty, Rui Liu, Andrea Pugliese, and VS Subrahmanian. 2023. SockDef: A dynamically
adaptive defense to a novel attack on review fraud detection engines.IEEE Transactions on Computational Social
Systems11, 4 (2023), 5253–5265.
[57] Ming Zhou, Dan Zhang, Yuandong Wang, Yangli-ao Geng, Yuxiao Dong, and Jie Tang. 2025. Lgb: Language model and
graph neural network-driven social bot detection.IEEE Transactions on Knowledge and Data Engineering(2025).
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:23
Table 6. Regression Analysis: Performance metrics as a function of𝐵𝐸𝑅 like,𝐵𝐸𝑅 follow,𝐵𝑋𝑅 like,𝐵𝑋𝑅 follow.
BER (like) BER (follow) BXR (like) BXR (follow)
Precision Recall F1 Precision Recall F1 Precision Recall F1 Precision Recall F1
𝑅2 0.301 0.225 0.303 0.221 0.221 0.223 0.004 0.0001 0.002 0.123 0.111 0.152
𝛽 0.005 0.007 0.006 0.004 0.007 0.005 0.0007−0.001 0.0006 0.005 0.0083 0.0073
𝑝−value 0.00017∗∗∗ 0.001∗∗∗ 0.000071∗∗∗ 0.003∗∗ 0.003∗∗ 0.003∗∗ 0.701 0.968 0.788 0.033∗ 0.044∗ 0.017∗
A Social Media Activity
We examine the relationship between social media activity metrics and bot detection performance.
Specifically, we analyze how Bot Engagement Ratio (𝐵𝐸𝑅) and Bot Exposure Ratio (𝐵𝑋𝑅 ), measured
separately for like and follow actions, correlate with users’ detection capabilities in terms of preci-
sion, recall, and F1-score.𝐵𝐸𝑅 quantifies the proportion of a user’s outgoing interactions directed
toward bot accounts, calculated separately as 𝐵𝐸𝑅 like and𝐵𝐸𝑅 follow These metrics reflect users’
voluntary engagement with bot-generated content. 𝐵𝑋𝑅 quantifies the proportion of incoming
interactions a user receives from bots, calculated separately as𝐵𝑋𝑅 like and𝐵𝑋𝑅 follow. These metrics
represent passive exposure to bot activity.
Table 6 reports summary statistics of the regression models fitting users’ precision, recall and F1
using𝐵𝐸𝑅 like,𝐵𝐸𝑅 follow,𝐵𝑋𝑅 like,𝐵𝑋𝑅 follow.
B Human vs AI Algorithms
We evaluated three representative bot detection methods spanning different technical paradigms
and feature types:
Hand-Crafted Feature Methods.(i)RFS[ 15] uses a random forest trained on behavioral and
metadata features (follower counts, following counts, posting frequency) extractable from any
social platform. This detector was employed in the original experiment and served as the adversarial
target for RL-bot training.
(ii)BotBuster[ 38] employs a multi-platform mixture of experts architecture combining three
specialized components: post content analysis, user metadata features, and account-level posting
patterns. We adapted the original implementation for our experimental setup, optimizing the
number of experts, learning rates, and class weights to improve performance on our benchmark
datasets.
Generative Methods(iii)LLM-based Detector[ 13] utilizes a prompt-based approach with in-
context learning, where the model receives examples of bot and human accounts before classifying
new instances. We evaluated four models from two families:llama3.1:8b, llama3.1:70b) and Mis-
tral (mistral:7b, mistral:24b), using the official repository⁄pilcrow⁄pilcrow. Table 7 presents performance on
the Twibot-20 dataset [12] across LLMs with varying numbers of in-context examples (0 vs. 4). With
the exception of precision, mistral:24b consistently achieved the highest performance, and larger
models (llama3.1:70b, mistral:24b) outperformed their smaller counterparts ( llama3.1:8b,
mistral:7b).
B.1 Training and Evaluation
All AI detectors except the LLM-based baseline were trained and validated using five-fold cross-
validation on three benchmark datasets: Twibot-20 [12], Cresci-2017 [9], and Caverlee-2011 [27].
The LLM-based detector relied on direct prompting with in-context examples rather than training,
we tested four LLMs from two families: llama3.1:8b, llama3.1:70b) and Mistral (mistral:7b,
⁄pilcrow⁄pilcrowhttps://github.com/BunsenFeng/botsay
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:24 La Gatta et al.
Table 7. Performance comparison of LLM-based bot detectors on Twibot-20 with varying numbers of in-
context examples: Precision, Recall and F1-score on the bot class, and overall Accuracy. Bold indicates best
performance, underline the first runner up.
LLM In-context Example Precision Recall F1 Accuracy
llama3.1:8b 0 0.570 0.380 0.450 0.510 4 0.500 0.330 0.400 0.460
llama3.1:70b 0 0.8250.228 0.357 0.556 4 0.717 0.333 0.455 0.568
mistral-7b 0 0.710 0.293 0.413 0.550 4 0.560 0.301 0.561 0.492
mistral-24b 0 0.732 0.517 0.606 0.636 4 0.7290.615 0.668 0.669
Table 8. Performance on Benchmark Datasets. Bold indicates best performance, underline the first runner up.
Dataset Model Precision Recall F1 Accuracy AUC
Twibot-20
BotBuster0.756 0.986 0.856 0.819 0.857
RFS 0.713 0.915 0.801 0.746 0.796
LLM 0.729 0.615 0.668 0.669−
Cresci-2017
BotBuster0.962 0.904 0.932 0.971 0.989
RFS 0.950 0.851 0.898 0.957 0.977
LLM 0.582 0.464 0.516 0.807−
Caverlee-2011
BotBuster0.899 0.916 0.907 0.899 0.948
RFS 0.889 0.887 0.888 0.860 0.929
LLM 0.744 0.590 0.658 0.693−
mistral:24b). Table 8 reports precision, recall, F1-score for the bot class, and overall accuracy and
AUC across datasets. BotBuster achieved the best performance on all benchmark datasets.
For our comparative analysis with humans (Hypothesis 11), we applied these pre-trained models
directly to the DartPost experimental data without additional training or fine-tuning. This evaluation
setup mimics realistic deployment scenarios where detection algorithms encounter novel influence
campaigns not represented in their training data. This setup also mirrors the human evaluation
condition, where participants received no feedback during the experiment.
B.2 Incremental Retraining
Figures 6 and 7 present relative F1-score improvement for detectors pretrained on Cresci-2017 and
Caverlee-2011, respectively. Results are consistent with those observed for Twibot-20 (Figure 5):
Ground-Truth Supervisionconsistently improves performance except for llama:70b, whileHuman
Supervisionachieves comparable gains but may still decrease performance in some cases.
We also observe an effect of benchmark dataset on retraining effectiveness. Pretraining on
Cresci-2017 (Figure 6) yields lower performance improvements for llama:70b, mistral:24b, and
BotBuster compared to other benchmarks. This likely reflects a language mismatch: Cresci-2017 is
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

Human, AI, and Hybrid Ensembles for Detection of Adaptive, RL-based Social Bots 111:25
D1 D2 D3 D4 D5
T est Day
8
6
4
2
0
2
4
6
cresci2017
F1 Impr. (%)
A
Llama
D1 D2 D3 D4 D5
T est Day
2
1
0
1
2
3
4
B
Mistral
D1 D2 D3 D4 D5
T est Day
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
C
BotBuster
D1 D2 D3 D4 D5
T est Day
0
5
10
15
20
25
30
D
RFS
Baseline (No Improvement) Ground-Truth Supervision Self-Supervision Human Supervision
Fig. 6. Relative F1-score improvement over baseline (no retraining) across experimental days for four detectors
pretrained on Cresci-2017. Each subplot shows one detector.Ground-Truth Supervisionretrains on correct
predictions,Self-Supervisionretrains on high-confidence predictions (threshold 0.7), andHuman Supervision
retrains on human reports.
D1 D2 D3 D4 D5
T est Day
0
5
10
15
20
25
30
caverlee2011
F1 Impr. (%)
A
Llama
D1 D2 D3 D4 D5
T est Day
0
5
10
15
20
25
30
35
B
Mistral
D1 D2 D3 D4 D5
T est Day
10
5
0
5
10
C
BotBuster
D1 D2 D3 D4 D5
T est Day
0
5
10
15
20
D
RFS
Baseline (No Improvement) Ground-Truth Supervision Self-Supervision Human Supervision
Fig. 7. Relative F1-score improvement over baseline (no retraining) across experimental days for four detectors
pretrained on Caverlee-2011. Each subplot shows one detector.Ground-Truth Supervisionretrains on correct
predictions,Self-Supervisionretrains on high-confidence predictions (threshold 0.7), andHuman Supervision
retrains on human reports.
multilingual while our experiment was conducted in English. Supporting this interpretation, RFS,
which does not rely on content features, still achieves substantial improvements on this benchmark
(up to 31.1% on Day 5 for Ground-Truth Supervision and 21.9% on Day 5 for Human Supervision).
B.2.1 Self-Supervision Threshold Selection.In theSelf-Supervisionretraining strategy, detectors are
retrained on instances they predicted as bots with confidence exceeding a threshold. This approach
requires no access to ground-truth labels, making it attractive for fully automated deployment.
However, the choice of threshold involves a trade-off: higher thresholds isolate predictions where
the model is most confident, but this is not necessarily beneficial as retraining on these instances
may reinforce systematic errors. Additionally, higher thresholds reduce the number of instances
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.

111:26 La Gatta et al.
0.5 0.6 0.7 0.8 0.9 0.95
Confidence Threshold
0.45
0.50
0.55
0.60
Retrained F1
Detector
Llama
Mistral
BotBuster
RF
Fig. 8. Effect of confidence threshold on Self-Supervision retraining. F1-score of retrained detectors (trained
up to day 4, evaluated on day 5) on Twibot-20 as a function of the confidence threshold used to select
retraining instances.
available for retraining, limiting the model’s exposure to new behavioral patterns. We empirically
evaluated thresholds from 0.5 to 0.95 across all four detectors. Figure 8 presents F1-scores for models
trained up to day 4 and evaluated on day 5 using the Twibot-20 benchmark.
Results show that a threshold of 0.7 yields the best or equivalent F1-score across all detectors.
For RFS, performance remains stable regardless of threshold, suggesting this detector’s confidence
scores are not informative for instance selection. For Mistral, performance degrades at thresholds
above 0.7, indicating that high-confidence predictions may reinforce errors. For Llama and BotBuster,
performance plateaus at 0.7 and remains stable at higher thresholds. Given these results, we select
0.7 as it achieves optimal performance while maximizing the number of instances available for
retraining.
Received 22 March 2026
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
