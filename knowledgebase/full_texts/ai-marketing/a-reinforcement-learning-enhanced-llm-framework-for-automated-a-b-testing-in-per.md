---
title: A Reinforcement-Learning-Enhanced LLM Framework for Automated A/B Testing in Personalized Marketing
url: https://arxiv.org/abs/2506.06316
category: ai-marketing
subcategory: empirical
date: 2025-05
venue: ''
authors:
- Haoyang Feng
- Yanjun Dai
- Yuan Gao
source: arxiv
pdf_url: https://arxiv.org/pdf/2506.06316
pages: 10
chars: 28838
fetched_at: '2026-11-08T13:14:25+00:00'
kb_version: 1
---

# A Reinforcement-Learning-Enhanced LLM Framework for Automated A/B Testing in Personalized Marketing

A Reinforcement-Learning-Enhanced LLM Framework for Automated A/B Testing in
Personalized Marketing
Haoyang Feng*
Duke University, Durham, NC, USA, brianmaga2024@gmail.com
Yanjun Dai
Brandeis University, Waltham, MA, USA, yanjundai0000@gmail.com
Yuan Gao
Boston University, Boston, MA, USA, xyan56379@gmail.com
Abstract
For personalized marketing, a new challenge of how to effectively algorithm the A/B  testing to maximum user
response is urgently to be overcome. In this paper, we present a new approach, the RL-LLM-AB test framework, for
using reinforcement learning strategy optimization combined with  LLM to automate and personalize A/B tests.
Design details RL -LLM-AB test is built upon the pre -trained instruction tuning language model, and it firstly
generates A/B versions of candidate content variants with the Prompt -Conditioned Generator, and finally, it
dynamically embeds and fuses the user  portrait and the context o f the current query with the multi -modal
perception mo dule to constitute the current interaction state. Then the content version is assigned in real -time
through the policy optimization module with Actor -Critic structure, and  the long -term revenue is estimated
according to real -time feedback (such as click -through rate and conversion rate). Furthermore, a Memory -
Augmented Reward Estimator is embedded into the framework to capture  the long -term user preference drift
which help to generalize policy across the multiple users and content context. Numerical results  demonstrate the
superiority of our proposed RL -LLM-ABTest over existing B tests based on the classical  A/B testing, Contextual
Bandit, and benchmark reinforcement learning methods on real-world marketing data.
CCS CONCEPTS
• Applied computing ~ Electronic commerce ~ E-commerce infrastructure
Keywords
A/B Testing, Reinforcement Learning, Large Language Models, Personalized Marketing, Decision Optimization.
1 INTRODUCTION
At present, in digital marketing world, personalization is no less than a game changer - when it comes to engaging
your users and improving conversion rates. Because of the ubiquity of online platforms  and mobile devices,
businesses are now able to achieve an extremely large sample of users' click, view, purchase, and other behavioral
data at a very high frequency. This data is rich in information on user preferences, that serves as the foundation for
sensitive content delivery and optimal strategy. By creating user portraits with traffic, marketers can use
recommendation algorithms to deliver the advertisements and push content to match the interest of individuals,
which can improve the user experience and the willingness of interaction to a large extent. Feng and Gao [14]
further demonstrated how machine learning -enhanced ad placement strategies can significantly boost

performance in large-scale e-commerce marketing, underscoring the importance of intelligent delivery systems in
personalized settings. Personalized marketing leads to better near term conversion numbers  and has potentially
far greater value by increasing user loyalty [1].
Classical A/B testing still has a very important function in the optimization of marketing campaigns when thinking
about changes in user behavior upon particular versions of content. But a classic A/B testing model often needs to
keep a set protocol upfront and unchanged for the length of the test (which is at least until you get the amount of
samples needed to reach significance). This process is not only time -consuming in responding, it is also slow to
adjust to changes that occur rapidly in user behavior and  the outside world  [2]. Particularly, when user interest
shift happens all too swiftly, or there’s a strong non-stationary signal, the traditional methods fall short to react in
time, and even make wrong decision or waste the resources. This calls for a more active and intelligent method  of
testing and optimization that complements or replaces the conventional approach.
To overcome these limitations, researchers and practitioners are just starting to consider the integration of AI
technology into A/B testing systems, which facilitates  a more effective, dynamic, and adaptive optimization of
systems. Out of various artificial intelligence technologies, reinforcement learning (RL) is one of the promising
techniques for personalized decision- making due to its “learn  by trial and error” property. Compared with
supervised learning that depends on fixed labels, RL is capable of receiving feedback on interaction and modifying
strategy in real-time, especially in marketing situations with low-level user interactive feedback that also frequently
evolves [3]. Meanwhile, thanks to the e -learning of  RL, it is able to react to the environmental changes
simultaneously which effectively increases the agility and robustness of policy deployment. This mirrors recent
findings in AI -driven credit risk detection [15], where real -time decision systems successfully adapt to fast-
changing user behavior and uncertainty.
By continuous exploration, feedback, updates to policies, reinforcement learning can explore the best path of action
in a complex, dynamic and uncertain environment. In localized marketing applications, this mechanism can be used
to adequately model the long -term interaction between users and  system, and to direct models to optimize for
more than a single click or conversion, but a long term value such as LTV. In particular, the RL system is able to
update the strategy in real-time according to the feedback from each user (e.g., clicks, browsing time etc.) to enable
dynamic content distribution and user adaptation. In addition, the previous studies have proved the remarkable
effect of RL strategy in ad sequencing, recommendation system and remarketing, which offers both theoretical
knowledge and technical support for adopting such strategy in A/B testing [4].
Furthermore, the long-run changes in user behavior and time-lag effect of content interventions complicates digital
marketing efforts. Origins of users preference dramatically change across time, context and  even mentality, and
classical strategy-based optimization methods by short-term feedbacks could not grasp such drift-like trend. On the
other hand, numerous interventions on content (e.g., holiday offers, coupon push) may have zero effects until hours
or even days after a user is  exposed to it, and this  “delayed reward” also poses challenges to reward modeling in
RL. Traditional RL methods conveniently ignore such delays, and such ignorance leads to the strategy optimization
deviating from the true long-term value of the users, may even cause the optimization to degenerate to some short-
sighted behaviors [5]. Lu, Wu, and Huang [16] addressed similar challenges by integrating group -relative policy
learning with time-series fusion to capture long-term user preference drift, which aligns well with our motiva tion
for memory-augmented modeling.

2 RELATED WORK
Above all, Singh et al. (2023)  [6] introduced a reinforcement learning -based click -through rate maximization
approach, employed mostly in digital advertising optimization settings. The authors mention that the classic A/B
testing methods suffer from problems of response delay and policy inflexibility  when they are applied to the ad
serving and user reaction feedback. Nichifor et al. (2021)  [7] integrated eye tracking and A/B testing to study the
correlation between personas and creatives in social media advertising. The paper show user pref erence is
translatable to A/B in terms of visual attention distribution and conversion rate data, so -called "user perception
factors" are valuable in the test design.
Angelopoulos et al. (2024)  [8] which is a method to make model generation more efficient by using A/B testing
results as a supervised signal when generating language model. The authors proposed a training data annotation
system using keyphrase extraction in order to  additionally optimize the sensitivity level of language model
generation regarding user actions. Zhang et al. (2023)  [9] introduced PerBid, an  automatic-bidding model
integrating personalization and fairness, for improving the efficiency of adve rtising effectiveness and allocation
resource fairness. PerBid designs deep reinforcement learning to fit the user click-through behavior and introduces
a causal inference technique to control the unbalanced delivery strategy among groups.
Wu et al. (2025)  [10] presented a LLM -based proxy model for automatic persuasive and factually content from
marketing, focused on descriptions of listings in the real estate sector. The model includes three main modules: the
Foundation module (which predicts marketable features), the Personalization module (which serves to fit userâ€™s
preferences), and the Marketing module (emphasizing the facts and the characteristics of the localization of the
content). Iyer et al. (2022)  [11] integrates RL with CF -based algorithms to improve the personalized
recommendation performance of digital advertising. This work is dedicated to offer a hybrid model, which exploits
RL’s real -time learning ability and CF’s superiority on user  preference modeling to adapt the content
recommendation policy dynamically in terms of high-level user engagement and satisfactions.
Hannig (2023) [12] describes the need of automating manual operations in marketing and sales, and the potential
of automation for enhanced process efficiency and decision-making. Sun et al. (2023) [13] investigated the effects
of sender type and anonymous leads on ad exposure and service conversion, and they proposed the AA-IDA model
for improving the conversion rate of hotel advertising. While this work offers useful understanding for specific
industries, it only center s on ad design  and delivery strategie s, without being systematic in optimizing contents.
Wu, Huang, and Lu [17] proposed an LLM -based mental health text intervention framework, highlighting how
domain-informed knowledge integration can enhance personalization and robustness —principles equally
applicable to marketing optimization.
3 METHODOLOGIES
3.1 Conditioned Generation and Multi-Modal State Encoding
The core goal of this module is to construct high-quality and personalized candidate content versions based on large
language models, combining user portraits and contextual information, and to use multimodal embedding
mechanisms to form state representations that can be used by reinforcement learning strategies. Instead of
traditional A/B testing, which relies only on manual design content, we introduce Prommpt's fine-tuned generation
mechanism and embed it into the state modeling process of reinforcement learning, making the entire system
perceptual, generative and adaptable. We define a candidate content generation function controlled by LLM, so that

ℳ𝐿𝐿𝐿𝐿𝐿𝐿 represents the language model that has been fine-tuned by instructions, and the input is a combined prompt
vector 𝑝𝑝 = 𝑔𝑔(𝑢𝑢, 𝑐𝑐) containing user portrait 𝑢𝑢 ∈ ℝ𝑑𝑑𝑢𝑢  and context features 𝑐𝑐 ∈ ℝ𝑑𝑑𝑐𝑐, and generate the A/B version of
the content 𝒱𝒱 = {𝑣𝑣𝐴𝐴, 𝑣𝑣𝐵𝐵}, as shown in Equation 1:
𝑣𝑣𝑘𝑘 = ℳ𝐿𝐿𝐿𝐿𝐿𝐿(𝑝𝑝|𝜃𝜃𝐿𝐿𝐿𝐿𝐿𝐿), 𝑘𝑘 ∈ {𝐴𝐴, 𝐵𝐵}. (1)
In order to improve the behavioral responsiveness of generated content, we build on the insight from Li et al. [19],
who showed that entity-aware prompt refinement and diversified generation can greatly enhance user engagement
and accuracy in the medical domain —a paradigm we adapt for commercial A/B testing. We introduced a Prompt
optimization goal based on click/conversion feedback. Define Immediate Feedback 𝑟𝑟(𝑣𝑣𝑘𝑘, 𝑢𝑢) ∈ ℝ  as the user's
response strength under a particular piece of content, and the optimization goal is to maximize the desired
behavioral utility of the content, as shown in Equation 2:
max
𝜃𝜃𝑝𝑝
𝔼𝔼𝑣𝑣𝑘𝑘~ℳ𝐿𝐿𝐿𝐿𝐿𝐿�𝑝𝑝𝜃𝜃𝑝𝑝 � [𝑟𝑟(𝑣𝑣𝑘𝑘, 𝑢𝑢)] = � 𝑟𝑟(𝑣𝑣𝑘𝑘, 𝑢𝑢) ∙ 𝑃𝑃 �𝑣𝑣𝑘𝑘�𝑝𝑝𝜃𝜃𝑝𝑝 � 𝑑𝑑𝑣𝑣𝑘𝑘. (2)
After the content generation is completed, in order to construct the state representation in reinforcement learning,
We propose a multimodal fusion mechanism, inspired in part by visual -prompt grounding strategies in
instructional video understanding [18], which show how aligned multi -source representations significantly
enhance content relevance and task performance . Stitching that sets the state to a three -part feature shows
Equation 3:
𝑠𝑠𝑡𝑡 = 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓(𝑀𝑀𝑀𝑀𝑃𝑃[𝑢𝑢𝑡𝑡; 𝑐𝑐𝑡𝑡; 𝑒𝑒𝑡𝑡 𝐴𝐴; 𝑒𝑒𝑡𝑡 𝐵𝐵]), (3)
Among them, 𝑒𝑒𝑡𝑡 𝐴𝐴 = 𝐸𝐸𝐸𝐸𝐸𝐸𝑒𝑒𝑑𝑑(𝑣𝑣𝐴𝐴) and 𝑒𝑒𝑡𝑡 𝐵𝐵 = 𝐸𝐸𝐸𝐸𝐸𝐸𝑒𝑒𝑑𝑑(𝑣𝑣𝐵𝐵) are the embedding representations of the content generated
by the LLM through the Transformer embedder or its [CLS] token, which are fused by a three -layer nonlinear
transformation MLP after splicing, and finally form a state of 𝑠𝑠𝑡𝑡 ∈ ℝ𝑑𝑑𝑠𝑠 . This state not only has the ability to
understand the context, but also the ability to understand the quality of candidate content, which significantly
improves the decision-making perception dimension of subsequent policy learning and lays the foundation.
As shown in Figure 1, the architecture of the RL -LLM-ABTest framework can be divided into two main parts: the
content generation and state modeling module using large language models on the left and the policy optimization
module using Actor -Critic on the right. First, the Prompt- Conditioned Generator generates the A/B candidate
content versions with the given user portraits and the context information.

Figure 1. Structure Diagram of RL-LLM-ABTest Framework Integrates Language Generation and Policy Optimization.
In the Actor-Critic architecture, we set the learning rate to 3 × 10−4 and the discount factor 𝛾𝛾 to 0.99. Experiments
show that if the learning rate is higher than  5 × 10−4, the model is prone to oscillation and non -convergence. If it
is lower than  1 × 10−4, the training progress will be significantly slower and the policy update will lag.
3.2 Actor-Critic Strategy Optimization and Memory Enhancement Return Modeling
On the basis of complete state modeling, RL -LLM-ABTest realizes the dynamic scheduling of A/B content variants
through reinforcement learning, so that the strategy can still learn the robust and optimal delivery strategy under
different user preferences, content quality and feedback noise. We build a learning module based on the Actor-Critic
architecture, in which the policy network (Actor) is used to output the A/B choice probability, and the value
network (Critic) is used to evaluate the long -term profitability of the current strategy . Specifically, we make the
action space 𝒜𝒜 = {𝐴𝐴, 𝐵𝐵} and the strategy function 𝜋𝜋𝜃𝜃(𝑎𝑎𝑡𝑡|𝑠𝑠𝑡𝑡) output the probability distribution of choosing either
A or B in a given state. The goal of an actor update is to maximize the expected return, as Equation 4:
𝒥𝒥(𝜃𝜃) = 𝔼𝔼𝜋𝜋𝜃𝜃 �� 𝛾𝛾𝑡𝑡𝑅𝑅𝑡𝑡
𝑇𝑇
𝑡𝑡=0
� . (4)
To stabilize training, we use proximal policy optimization loss function to optimize strategy, as Equations 5:
ℒ𝑎𝑎𝑎𝑎𝑡𝑡𝑓𝑓𝑎𝑎(𝜃𝜃) = 𝔼𝔼𝑡𝑡�min�𝑟𝑟𝑡𝑡(𝜃𝜃) ∙ 𝐴𝐴̂𝑡𝑡, 𝑐𝑐𝑐𝑐𝑐𝑐𝑝𝑝(𝑟𝑟𝑡𝑡(𝜃𝜃), 1 − 𝜖𝜖, 1 + 𝜖𝜖) ∙ 𝐴𝐴̂𝑡𝑡��. (5)
Among them, the old and new strategies are like Equation 6:
𝑟𝑟𝑡𝑡(𝜃𝜃) = 𝜋𝜋𝜃𝜃(𝑎𝑎𝑡𝑡|𝑠𝑠𝑡𝑡) 𝜋𝜋𝜃𝜃𝑜𝑜𝑜𝑜𝑜𝑜 (𝑎𝑎𝑡𝑡|𝑠𝑠𝑡𝑡) . (6)
The dominance function is estimated as follows in Equation 7:
𝐴𝐴̂𝑡𝑡 = 𝑅𝑅𝑡𝑡 − 𝑉𝑉𝜙𝜙(𝑠𝑠𝑡𝑡). (7)
𝑉𝑉𝜙𝜙(𝑠𝑠𝑡𝑡) is a state value function output by Critic, and the training goal is to minimize TD error, as Equation 8:
ℒ𝑎𝑎𝑎𝑎𝑓𝑓𝑡𝑡𝑓𝑓𝑎𝑎(𝜙𝜙) = 𝔼𝔼𝑡𝑡 ��𝑉𝑉𝜙𝜙(𝑠𝑠𝑡𝑡) − 𝑅𝑅𝑡𝑡�
2
� . (8)
At this point, we have built a content selector that can intelligently make decisions based on the current
environment. However, traditional reinforcement learning is less robust to long-term changes in user preferences,
such as "cold start" or "interest drift". To this end, we introduce the Memory-Augmented Reward Estimator module,

and design a memory unit 𝐸𝐸𝑓𝑓 ∈ ℝ𝑑𝑑𝑚𝑚  to store the long -term behavioral clues of users in the process of historical
interaction. We use gated recurrent units (GRUs) to update memory states, as shown in Equation 9:
𝐸𝐸𝑓𝑓 (𝑡𝑡) = 𝐺𝐺𝑅𝑅𝐺𝐺 �𝐸𝐸𝑓𝑓 (𝑡𝑡−1). [𝑠𝑠𝑡𝑡, 𝑎𝑎𝑡𝑡, 𝐸𝐸𝑓𝑓]� . (9)
This memory vector will be used as part of the reward estimator to influence the modeling of future returns in
reinforcement learning. Finally, use the reward function output of the module, as shown in Equation 10:
𝑟𝑟̃𝑡𝑡 = 𝑓𝑓𝑎𝑎(𝑠𝑠𝑡𝑡, 𝑎𝑎𝑡𝑡, 𝐸𝐸𝑓𝑓), (10)
and use it to construct a cumulative discount return with memory enhancement, as in Equation 11:
𝑅𝑅𝑡𝑡 = � 𝛾𝛾𝑘𝑘 𝑟𝑟̃𝑡𝑡+𝑘𝑘
𝑇𝑇
𝑘𝑘=0
. (11)
By introducing this module, our strategy can not only respond to immediate feedback, but also gradually learn from
users' long -term content preference changes, significantly improving the long -term stability and generalization
ability of the strategy in pe rsonalized marketing. Algorithm 1 shows the Actor -Critic policy optimization process
based on the proximal policy optimization method.
Algorithm 1. Actor-Critic Policy Optimization.
Input: state 𝑠𝑠𝑡𝑡, policy 𝜋𝜋𝜃𝜃, value function 𝑉𝑉𝜙𝜙, rollout buffer 𝐵𝐵.
1: For each episode do
2:  Collect trajectory (𝑠𝑠𝑡𝑡, 𝑎𝑎𝑡𝑡, 𝑟𝑟𝑡𝑡, 𝑠𝑠𝑡𝑡+1) under 𝜋𝜋𝜃𝜃
3:  Compute advantage estimate 𝐴𝐴 ̂𝑡𝑡 = 𝑟𝑟𝑡𝑡 + 𝛾𝛾𝑉𝑉𝜙𝜙(𝑠𝑠𝑡𝑡+1) − 𝑉𝑉𝜙𝜙(𝑠𝑠𝑡𝑡).
4:  Compute PPO clipped loss  ℒ𝑎𝑎𝑎𝑎𝑡𝑡𝑓𝑓𝑎𝑎 = −min (
𝜋𝜋𝜃𝜃�𝑎𝑎𝑡𝑡�𝑠𝑠𝑡𝑡�
𝜋𝜋𝜃𝜃𝑜𝑜𝑜𝑜𝑜𝑜�𝑎𝑎𝑡𝑡�𝑠𝑠𝑡𝑡�).
5:  Update 𝜃𝜃 ← 𝜃𝜃 − ∇𝜃𝜃ℒ𝑎𝑎𝑎𝑎𝑡𝑡𝑓𝑓𝑎𝑎.
6:  Compute value loss  ℒ𝑎𝑎𝑎𝑎𝑓𝑓𝑡𝑡𝑓𝑓𝑎𝑎 = �𝑉𝑉𝜙𝜙(𝑠𝑠𝑡𝑡) − 𝑅𝑅𝑡𝑡�
2
.
7:  Update 𝜙𝜙 ← 𝜙𝜙 − ∇𝜙𝜙ℒ𝑎𝑎𝑎𝑎𝑓𝑓𝑡𝑡𝑓𝑓𝑎𝑎.
8: End for
4 EXPERIMENTS
4.1 Experimental Setup
The Criteo 1TB Display Advertising Challenge dataset was used to evaluate the RL-LLM-ABTest framework. Criteo
Ad Click logs the click logs are that of a typical ad system— over 24 days of training data and 1 day test data covering
283M training instances and 6M test instances where each instance describes a display ad served by Criteo,  a
leading online advertising company. We th en sample a representative subset of the data to build the user status,
contextual input and the candidate ad contents, and employ the click-through rates (CTRs) as the feedback signals,
to facilitate this personalized content generation and strategy optimization from data.
The original Criteo 1TB Display Advertising Challenge dataset contains over 283 million user -ad interaction logs
across 24 days, with 6 million interactions used for evaluation. After preprocessing, we filtered valid ad impression
sessions with non -null click and context fields, sampled a representative 5% subset (~14M entries) for efficient
training, and constructed user status embeddings using browsing and ad history.  In order to improve the
correlation between content generation and user click -through rate, we introduce a reinforcement learning
optimization mechanism based on user feedback.

4.2 Experimental Analysis
In order to assess the performance of the proposed RL -LLM-ABTest framework, we compared it with four
representative methods:
 Static-A/B (Static A/B Test Baseline): This approach is the most straightforward A/B testing paradigm, in
which two content variants (A and B) are pre-computed during the test phase, randomized to the users, clicks
are collected and the most successful variant is adopted as the main content.
 Contextual Bandit  (LinUCB): We concatenates user features and context string as the input state, build a
linear regression model to predict click probability, and uses UCB strategies to explore and exploit. Even
though this method has some degree of person alization, it is essentially restricted to the modeling of short-
term feedback and does not consider the problem of long-term reward or preference drift.
 DeepFM with A/B Re-ranking (DeepFM): We take the deep FM model (DeepFM) as a typical recommendation
algorithm, feed the A/B content versions into the model at the same time, sort the content versions based on
the predicted click probability, and select one version with a higher ranking as the current version.
 Prompt-LM + RulePolicy: We generate A/B content based on the similar pretrained language  model as that
in this paper, but the delivery strategy is based on manually set heuristic rules.

Figure 2. CTR Comparison Across Different A/B Testing Methods.
Click-Through Rate  (CTR) is the mostly widely used performance metric for A/B testing to compare the
effectiveness of different variants at encouraging clicks. As shown in Figure 2, RL-LLM-ABTest has always kept the
highest CTR level with the smallest confidence interval throughout the entire number of impressions, which
indicates that the method possesses the strongest capability of improvement to the click-through rate and the best
stability of result.
In comparison, Static -A/B quickly stabilized after an initial burst,  and was no longer able to grow with massive
campaigns. Despite the meteoric rise of LinUCB in the early phase, however, it eventually dips to a low level with
the number of impressions, indicating an instability due to over-exploration. DeepFM and Prompt-LM + RulePolicy
kept increasing in a moderate and smooth manner, but the increase was not as sharp as RL-LLM-ABTest.
The Confidence Interval is the estimated range for the parameter tested. It can be seen from Fig. 3 and the shadow
band And it can be seen that the CTR of all methods increases with the number of training rounds, however the
enhancement amplitude and the stability difference are significant. Static A/B testing (Static-A/B) is flat and does

not improve with more training; LinUCB increase rapidly after a few training samples and then converge fast, and
the confidence bound only decrease slightly with more training, the level of decrease of the confidenece is limited.

Figure 3. CTR Comparison with 95% Confidence Intervals and Training Epochs.
DeepFM and Prompt -LM + RulePolicy have relatively continuous growth down to the bottom and the confidence
interval drops quickly, which means their recommendation and rule strategy are robust. But the CTR of RL -LLM-
ABTest is not only the highest at each stage of model training, but also that the range of the confidence interval is
also the smallest, that it means the method not only can continue to optimize  the click effect in the long -term
iterative process, but also have the higher reliability and stability of the result.
To evaluate the role of each core module in the RL-LLM-ABTest framework, we performed an ablation experiment
in which three key components were removed sequentially and the effect on click-through rate was observed. The
results show that removing the Promp t conditional generation module and replacing it with a static manual
template will significantly reduce the adaptability of the content to user interest. After removing the Actor -Critic
policy optimization module and using the manual rule distribution str ategy, the model cannot adjust the delivery
strategy according to the real-time feedback, which shows obvious rigidity and inefficiency.
In order to verify the effectiveness of the prompt word optimization mechanism, we designed a comparative
experiment to compare the performance difference between static template prompt words and dynamic
optimization prompt words in content generation. The  experimental results show that the optimized prompt is
increased by 7.3% on average in the click -through rate index, indicating that the prompt words automatically
constructed for user portrait and context can stimulate user behavior more.
5 CONCLUSION
In conclusion, the RL-LLM-ABTest framework proposed in this paper combines pre-trained instruction tuning large
language model with reinforcement learning strategy optimization based on actor -critic to formulate a close -loop
process from content generation, multimodal sta te modeling, policy decision- making to memory enhancement
reward estimation, and the experiment shows its great promotion in CTR and stability on the real -scale Criteo
advertising dataset. By contrast, compared to context bandits, deep reco mmendation models and rule -base
strategies, at the same time, higher click-through rate, smaller confidence interval are achieved with stronger long-
term learning and generalization for  RL-LLM-ABTest. In the future, the work in the paper can be extended in the
following aspects deployment in online systems to validate the practicability in real-time and the effect of long-term
optimization on ad click multimodal, fairness and privacy protection mechanism, and the progress of personalized

marketing in a more intelligent, efficient and responsible direction. Future work may also explore multilingual or
low-resource personalization strategies, following efforts like those in [20], which improve neural machine
translation by centering language-specific context—a promising path for globalized marketing optimization.
REFERENCES
[1] Anozie, U. C., Onyenahazi, O. B., Ekeocha, P. C., Adekola, A. D., Ukadike, C. A., & Oloko, O. A. (2024). Advancements
in artificial intelligence for omnichannel marketing and customer service: Enhancing predictive analytics,
automation, and operational eff iciency. International Journal of Science and Research Archive, 12(2), 1621 -
1629.
[2] Yuan, Y., & Altenburger, K. M. (2023). A two -part machine learning approach to characterizing network
interference in a/b testing. arXiv preprint arXiv:2308.09790.
[3] Verma, C., Vijayalakshmi, P., Chaturvedi, N., Umesh, U., Rai, A., & Ahmad, A. Y. B. (2025, February). Artificial
Intelligence in Marketing Management: Enhancing Customer Engagement and Personalization. In 2025
International Conference on Pervasive Computational Technologies (ICPCT) (pp. 397-401). IEEE.
[4] Ye, Z., Yoganarasimhan, H., & Zheng, Y. (2025). Lola: Llm- assisted online learning algorithm for content
experiments. Marketing Science.
[5] Seebacher, U. G. (2021). The B2B marketing ecosystem: Finding your way through the world of colorful B2B
terms!. In B2B Marketing: A Guidebook for the Classroom to the Boardroom (pp. 31 -52). Cham: Springer
International Publishing.
[6] Singh, V., Nanavati, B., Kar, A. K., & Gupta, A. (2023). How to maximize clicks for display advertisement in digital
marketing? A reinforcement learning approach. Information Systems Frontiers, 25(4), 1621-1638.
[7] Nichifor, E., Lixăndroiu, R. C., Chițu, I. B., Brătucu, G., Sumedrea, S., Maican, C. I., & Tecău, A. S. (2021). Eye
tracking and an a/b split test for social media marketing optimisation: The connection between the user profile
and ad creative components. Journal of Theoretical and Applied Electronic Commerce Research, 16(6), 2319 -
2340.
[8] Angelopoulos, P., Lee, K., & Misra, S. (2024). Causal alignment: Augmenting language models with A/B tests.
Available at SSRN.
[9] Zhang, H., Niu, L., Zheng, Z., Zhang, Z., Gu, S., Wu, F., ... & Zheng, B. (2023, August). A personalized automated
bidding framework for fairness-aware online advertising. In Proceedings of the 29th ACM SIGKDD Conference
on Knowledge Discovery and Data Mining (pp. 5544-5553).
[10] Wu, J., Yang, C., Mahns, S., Wang, C., Zhu, H., Fang, F., & Xu, H. (2025). Grounded Persuasive Language Generation
for Automated Marketing. arXiv preprint arXiv:2502.16810.
[11] Iyer, D., Sharma, D., Singh, N., & Patel, S. (2022). Enhancing Digital Advertising through AI -Powered
Personalization: Leveraging Reinforcement Learning and Collaborative Filtering Algorithms. International
Journal of AI ML Innovations, 11(8).
[12] Hannig, U. (2023). Automation of repetitive processes in marketing and sales. In Marketing and Sales
Automation: Basics, Implementation, and Applications (pp. 7-18). Cham: Springer International Publishing.
[13] Sun, X., Li, Y., Guo, B., & Gao, L. (2023). Marketing Automation: How to Effectively Lead the Advertising
Promotion for Social Reconstruction in Hotels. Sustainability, 15(5), 4397.
[14] H. Feng and Y. Gao, "Ad Placement Optimization Algorithm Combined with Machine Learning in Internet E -
Commerce," Preprints, 2025.
[15] Z. Wang, Q. Zhang, and Z. Cheng, "Application of AI in real-time credit risk detection," Preprints, 2025.
[16] D. Lu, S. Wu, and X. Huang, "Research on Personalized Medical Intervention Strategy Generation System based
on Group Relative Policy Optimization and Time-Series Data Fusion," arXiv:2504.18631, 2025.
[17] S. Wu, X. Huang, and D. Lu, "Psychological health knowledge -enhanced LLM -based social network crisis
intervention text transfer recognition method," arXiv:2504.07983, 2025.
[18] S. Li, B. Li, B. Sun, and Y. Weng, "Towards Visual-Prompt Temporal Answer Grounding in Instructional Video,"

IEEE TPAMI, vol. 46, no. 12, pp. 8836–8853, 2024.
[19] B. Li, B. Sun, S. Li, et al., "Distinct but correct: generating diversified and entity -revised medical response,"
Science China Information Sciences, vol. 67, no. 3, p. 132106, 2024.
[20] B. Li, Y. Weng, F. Xia, and H. Deng, "Towards better Chinese-centric neural machine translation for low-resource
languages," Computer Speech & Language, vol. 84, p. 101566, 2024.
