---
title: Privacy Preserving Conversion Modeling in Data Clean Room
url: https://arxiv.org/abs/2505.14959
category: privacy-data
subcategory: framework
date: 2024-10
venue: ''
authors:
- Kungang Li
- Xiangyi Chen
- Ling Leng
source: arxiv
pdf_url: https://arxiv.org/pdf/2505.14959
pages: 5
chars: 24331
fetched_at: '2026-11-08T13:00:05+00:00'
kb_version: 1
---

# Privacy Preserving Conversion Modeling in Data Clean Room

arXiv:2505.14959v1  [cs.LG]  20 May 2025
Privacy Preserving Conversion Modeling in Data Clean Room
Kungang Li
Pinterest Inc.
USA
kungangli@pinterest.com
Xiangyi Chen
Pinterest Inc.
USA
xiangyichen@pinterest.com
Ling Leng
Pinterest Inc.
USA
lleng@pinterest.com
Jiajing Xu
Pinterest Inc.
USA
jiajing@pinterest.com
Jiankai Sun
Pinterest Inc.
USA
jiankaisun@pinterest.com
Behnam Rezaei∗
Pinterest
USA
brezaei@pinterest.com
ABSTRACT
In the realm of online advertising, accurately predicting the con-
version rate (CVR) is crucial for enhancing advertising efficiency
and user satisfaction. This paper addresses the challenge of CVR
prediction while adhering to user privacy preferences and adver-
tiser requirements. Traditional methods face obstacles such as the
reluctance of advertisers to share sensitive conversion data and the
limitations of model training in secure environments like data clean
rooms. We propose a novel model training framework that enables
collaborative model training without sharing sample-level gradi-
ents with the advertising platform. Our approach introduces several
innovative components: (1) utilizing batch-level aggregated gradi-
ents instead of sample-level gradients to minimize privacy risks; (2)
applying adapter-based parameter-efficient fine-tuning and gradi-
ent compression to reduce communication costs; and (3) employing
de-biasing techniques to train the model under label differential pri-
vacy, thereby maintaining accuracy despite privacy-enhanced label
perturbations. Our experimental results, conducted on industrial
datasets, demonstrate that our method achieves competitive ROC-
AUC performance while significantly decreasing communication
overhead and complying with both advertisers’ privacy require-
ments and user privacy choices. This framework establishes a new
standard for privacy-preserving, high-performance CVR prediction
in the digital advertising landscape.
CCS CONCEPTS
• Information systems→ Recommender systems.
KEYWORDS
ADs Conversion, Privacy, CVR Prediction, Differential Privacy
ACM Reference Format:
Kungang Li, Xiangyi Chen, Ling Leng, Jiajing Xu, Jiankai Sun, and Behnam
Rezaei. 2024. Privacy Preserving Conversion Modeling in Data Clean Room.
In 18th ACM Conference on Recommender Systems (RecSys ’24), October 14–18,
∗Currently at Roblox. Work was done while the author was employed at Pinterest Inc..
Permission to make digital or hard copies of part or all of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
RecSys ’24, October 14–18, 2024, Bari, Italy
© 2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0505-2/24/10.
https://doi.org/10.1145/3640457.3688054
2024, Bari, Italy. ACM, New York, NY, USA, 5 pages. https://doi.org/10.1145/
3640457.3688054
1 INTRODUCTION
In online advertising systems, conversion serves as a tangible mea-
sure of user satisfaction and represents a definitive indication of
success in an e-commerce environment [4, 13, 16, 17]. It is often the
primary objective for advertisers in numerous marketing contexts.
Estimating the conversion rate (CVR) is essential in performance-
based digital advertising [8, 9, 23].
However, some advertisers hesitate to share conversion data
with the advertising platforms in order to protect their user con-
version data privacy and maintain competitive advantage. Clean
room is an option they are interested in sharing the conversion
data in a more privacy centric way. A data clean room is a secure
environment where organizations can collaborate and share data
without exposing sensitive information to unauthorized parties
[10, 12]. They are viewed as a trusted third party for both parties,
therefore, matching conversion data and user data from both parties
in the clean room is considered as an viable option for conversion
modeling. But nowadays, clean rooms may have limited computing
capability, limited training visibility and high pricing structure thus
it is not feasible to train complicated models in the clean room.
To overcome the limitations, we borrow the idea of split learning,
which aims at collaboratively training a model using the private
input and label data held by two separate parties [14, 15, 19]. We
have identified two primary reasons why the standard split learning
method is not suitable for our scenario. Firstly, there are privacy
concerns associated with standard split learning. This arises from
the fact that the label information can potentially be inferred by
adversaries through shared sample-level gradients [6, 14, 24], which
are exchanged between the clean room and the advertising plat-
form. These are significant concerns for advertisers, thereby making
the adoption of standard split learning infeasible for us. Secondly,
the inference process in the advertising platform necessitates the
complete model, including the layers within the clean room. This
requirement diverges from the standard split learning approach,
where only a portion of the model is used for inference.
In this work, we proposed an approach to train large conver-
sion models with a new framework. The approach employs pa-
rameter efficient fine-tuning techniques, differential privacy, and
communication-efficient training algorithms to simultaneously

RecSys ’24, October 14–18, 2024, Bari, Italy Kungang Li et al.
f
x
i
intermediate
layer

h
i
Input
features
X
Advertising
Platform
g
p
i
Loss
L
i

Labels
y
w/wo
noise
Advertiser
Join
Sample
level
gradients
f
x
i
logit

z
i
p
i
Loss
L
i
Input
features
X
Labels
y
Compute
aggregated
gradients
D ata
Clean
Room
w/wo
noise
Advertiser
Advertising
Platform
Join
Sample
level
gradients
Update
model
parameters
(a)
Standard
split
learning
fram ework
(b)
Proposed
m odel
learning
fram ework
with
data
clean
room
Figure 1: Comparison of (a) standard split learning frame-
work and (b) the proposed framework to train conversion
models in the data clean room.
comply with privacy restrictions for conversion data and enable ef-
ficient coordination between clean room and advertising platforms
to train CVR models.
2 METHODOLOGY
2.1 Model training framework
Figure 1 compares the standard split learning and our proposed
approach with the context that the advertising platform is the party
with raw input features (the feature party) and the advertiser is the
party with ground truth labels (the label party). In our proposed
framework, the feature party conducts most computation of the
forward pass and send the computed logits to the clean room, which
are joined with labels to compute the training loss. To compute the
gradients with respect to the model parameters without disclos-
ing sample level gradients from the clean room to the advertising
platform, the aggregated gradient is computed in the clean room.
The feature party computes and sends the partial derivatives of the
logits with respect to the model parameters 𝜕𝑧𝑖 𝜕𝑓 , which are joined
with the loss with respect to logit partial derivatives𝜕𝐿𝑖 𝜕𝑧𝑖 to compute
∇𝑓 𝐿 1. In our case,∇𝑓 𝐿 is given by ˝𝑏 𝑖=1(𝑝𝑖− 𝑦𝑖) 𝜕𝑧𝑖 𝜕𝑓 , where binary
cross-entropy loss with sum reduction is applied, 𝑝𝑖 is the predic-
tion score for being positive for sample 𝑖, 𝑦𝑖 is the ground truth
label, and 𝑏 denotes the batch size. The aggregated gradients are
returned to the advertising platform to update model parameters.
Because we use very large batch size (tens of thousands) during
training, the label information from the aggregated gradients shall
not be easily attacked by the gradient matching technique such as
DLG [28]. In order to strengthen privacy protection, we integrate
differential privacy, specifically when the number of trainable pa-
rameters∥𝑓∥ surpasses the batch size 𝑏. This strategy effectively
defends against potential adversaries who attempt to solve the
aforementioned equation, where there are 𝑏 unknown labels, by
1We do not need to conduct other complicated computation within the clean room.
extracting label information from a set of equations formed by the
number of parameters∥𝑓∥.
2.2 Adapter based efficient training
N umerical
Feature
Categorical
Feature
Sequence
Feature
Feature
Preprocessing
Layers
Sequence
Transformer
M odule
Unified
Dimension
Projection
Layer
M LP
M odule
Transformer
M odule
Ensemble
Layer
Add
&
N orm
M LP
Task
1
Task
2
Task
N
...
...
LoRA
LoRA
LoRA
LoRA
LoRA
Gating
Embedding
Feature
Multiple
layers
Figure 2: Adapter based CVR model.
In modern ads delivery systems, the CVR models used in late stage
ads ranking are usually very large, with model sizes from a few
GBs to TBs [21, 25–27]. This creates a significant challenge due to
the high communication costs associated with transmitting sample-
level partial derivatives from the advertising platform to the clean
room. In our use case, it would take about2.5 days to complete train-
ing on 1 day’s data for some big advertisers with 10 Gbps network
bandwidth, which makes it impractical to land into production. To
reduce the communication cost, we propose two approaches: (1)
Reduce the trainable model parameters by applying pretrain and pa-
rameter efficient fine tuning approach; (2) Compress the gradients.
The per-sample partial derivatives are compressed before sending
to clean room.
Inspired by adapter approach in large language model (LLM),
such as Low-Rank Adaptation (LoRA) [11], we proposed a gated
adapter approach for this conversion modeling use case. We apply
plug-in adapter module with some trainable parameters to selected
layers of the CVR model during fine tuning.
We add gated LoRA adapter layers to the core modules of the
CVR model, include the QKV layer in multi-head attention in the
sequence transformers, the linear layers in the feature interaction
modules, and the linear layers in the multi-task towers (Figure 2 ).
Depending on the model size and network bandwidth between
the advertising platform and the clean room, communication cost
may need to be further reduced. In this case, the advertising plat-
form can employ gradient compression techniques [22] like QSGD
[3], top-k [2], and powerSGD [20] to compress the per-sample par-
tial derivatives sent to the clean room.

Privacy Preserving Conversion Modeling in Data Clean Room RecSys ’24, October 14–18, 2024, Bari, Italy
2.3 Training with label DP
To further protect label privacy, the advertiser may choose to imple-
ment differential privacy (DP) [1, 5]. There are two primary meth-
ods to add DP noise for label protection. The first method involves
applying Gaussian or Laplace noise to the aggregated gradients.
The second method employs label DP [ 7, 18, 24], where under a
binary classification setting, some labels are randomly flipped to
their opposite value based on a probability that is determined by the
privacy budget 𝜖. In this paper, we focus on label DP and leave the
application of noise to aggregated gradients for future exploration.
Training directly on such perturbed labels will bias conversion
probability and make the CVR model miscalibrated given conver-
sion labels are highly class-imbalanced. A simple and effective
remedy is to factorized the label transition probability into loss
function to debias the prediction. Denote 𝑞𝜖 = 𝑒𝜖 𝑒𝜖+1 being the
probability to keep the original label and 𝑙(𝑝𝑖) being the original
loss function on prediction 𝑝𝑖, the de-biased loss can be written as
𝑙𝑑𝑒𝑏(𝑝𝑖) = 𝑙(𝑝𝑖𝑞𝜖+( 1− 𝑝𝑖)( 1− 𝑞𝜖)).
3 EXPERIMENT AND RESULTS
We conducted all experiments on internal industrial datasets, which
contains more than 10 B entries and approximately 300 distinct
features. The main predictive task is click through CVR and there
are five auxiliary tasks such as click through rate (CTR) to help the
main task prediction. We use ROC-AUC as the metric to evaluate
model predictive performance offline as we found it correlates
well with online business metrics in our settings. Table 1 lists the
offline ROC-AUC performance of LoRA fine tuning. From it, we
can see that with only fine tuning 2 millions parameters (about 1%
of fine tuning all parameters), we can achieve a high ROC-AUC
gain (about 95% of the gain from fine tuning all parameters). This
is a acceptable tradeoff considering it would reduce the training
time from 2.5 days to less than 1 hour on 1 day’s data for some big
advertisers with 10 Gbps network bandwidth. Even with as few as
0.06 million parameters, we can still achieve a+3% ROC-AUC gain.
In our experiments, adding label DP will cause drop in ROC-AUC
(−2.1% for 𝜖 = 5 and−8.3% for 𝜖 = 3) and calibration issue (1.4 for
𝜖 = 5 and 4.0 for 𝜖 = 3) without de-bias. With the de-bias approach,
the predictions are fully calibrated (1.0), and the ROC-AUC drop
is around 0.2% - 0.5% for 𝜖 ranging from 5 to 3, which is accept-
able in production. For gradient compression, we tested applying
QSGD [3] compression and BF16 quantization to per-sample gradi-
ents, these techniques can provide up to 4x compression rate with
ROC-AUC drop around 0.6% and we believe designing compression
techniques tailored for per-sample gradients can further mitigate
the performance loss (Table 2).
Based on our online A/B experiments for conversion ads, we
expect that adopting this technique could lead to a reduction of
more than 10% in the cost per action (CPA) for advertisers who
currently lack conversion data in CVR model. This improvement is
significant as it helps lower advertiser costs and increases long-term
platform revenue.
4 CONCLUSION
In conclusion, our proposed model training framework addresses
privacy and efficiency challenges by using batch-level aggregated
Table 1: Results of LoRA adapter fine tuning on CVR model.
Baseline is without conversion data.
Model setting ROC-AUC
diff (%)
# trainable params
(millions)
Baseline 0 200
Fine tune all params +3.63 200
Fine tune LoRA (rank 64) +3.48 4
Fine tune LoRA (rank 32) +3.44 2
Fine tune LoRA (rank 1) +3.02 0.06
Table 2: Results of Label DP and gradient compression. Base-
line is no privacy constraint.
Model setting ROC-AUC diff(%) Calibration
Baseline 0 1.0
No debias, 𝜖=3 -8.3 4.0
No debias, 𝜖=5 -2.1 1.4
Debias, 𝜖=3 -0.5 1.0
Debias, 𝜖=5 -0.2 1.0
QSGD, 8bit -0.61 1.0
BF16, 16bit -0.67 1.0
gradients, adapter-based fine-tuning methods, and label differential
privacy with de-biasing techniques. Experimental results on real-
world datasets indicate that our framework maintains competitive
performance while adhering to privacy requirements, setting a
new benchmark for privacy-preserving, high-performance CVR
prediction in the digital advertising industry.
ACKNOWLEDGMENTS
The authors would like to thank Aayush Mudgal, Andy Kimbrough,
Ang Xu, Jaewon Yang, Joey Wang, Stephanie deWet, Susan Walker,
Xiaofang Chen, Yingwei Li, Zhifang Liu for their valuable discussion
and paper review.
REFERENCES
[1] Martin Abadi, Andy Chu, Ian Goodfellow, H Brendan McMahan, Ilya Mironov,
Kunal Talwar, and Li Zhang. 2016. Deep learning with differential privacy. In
Proceedings of the 2016 ACM SIGSAC conference on computer and communications
security. 308–318.
[2] Alham Fikri Aji and Kenneth Heafield. 2017. Sparse communication for dis-
tributed gradient descent. arXiv preprint arXiv:1704.05021 (2017).
[3] Dan Alistarh, Demjan Grubic, Jerry Li, Ryota Tomioka, and Milan Vojnovic. 2017.
QSGD: Communication-efficient SGD via gradient quantization and encoding.
Advances in neural information processing systems 30 (2017).
[4] Olivier Chapelle. 2014. Modeling delayed feedback in display advertising. In
Proceedings of the 20th ACM SIGKDD international conference on Knowledge
discovery and data mining . 1097–1105.
[5] Cynthia Dwork. 2006. Differential privacy. In International colloquium on au-
tomata, languages, and programming . Springer, 1–12.
[6] Chong Fu, Xuhong Zhang, Shouling Ji, Jinyin Chen, Jingzheng Wu, Shanqing
Guo, Jun Zhou, Alex X Liu, and Ting Wang. 2022. Label inference attacks against
vertical federated learning. In 31st USENIX security symposium (USENIX Security
22). 1397–1414.
[7] Badih Ghazi, Noah Golowich, Ravi Kumar, Pasin Manurangsi, and Chiyuan
Zhang. 2021. Deep learning with label differential privacy. Advances in neural
information processing systems 34 (2021), 27131–27145.
[8] Yuyao Guo, Haoming Li, Xiang Ao, Min Lu, Dapeng Liu, Lei Xiao, Jie Jiang, and
Qing He. 2022. Calibrated Conversion Rate Prediction via Knowledge Distillation
under Delayed Feedback in Online Advertising. In Proceedings of the 31st ACM
International Conference on Information & Knowledge Management . 3983–3987.

RecSys ’24, October 14–18, 2024, Bari, Italy Kungang Li et al.
[9] Elad Haramaty, Zohar Karnin, Arnon Lazerson, Liane Lewin-Eytan, and Yoelle
Maarek. 2023. Extended conversion: Capturing successful interactions in voice
shopping. In Proceedings of the 17th ACM Conference on Recommender Systems .
826–832.
[10] Tilman Herbrich. 2022. Data Clean Rooms. Computer Law Review International
23, 4 (2022), 109–120.
[11] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean
Wang, Lu Wang, and Weizhu Chen. 2021. Lora: Low-rank adaptation of large
language models. arXiv preprint arXiv:2106.09685 (2021).
[12] Garrett Johnson, Julian Runge, and Eric Seufert. 2022. Privacy-centric digital
advertising: Implications for research. Customer Needs and Solutions 9, 1 (2022),
49–54.
[13] Kuang-chih Lee, Burkay Orten, Ali Dasdan, and Wentong Li. 2012. Estimating
conversion rate in display advertising from past erformance data. In Proceedings
of the 18th ACM SIGKDD international conference on Knowledge discovery and
data mining. 768–776.
[14] Oscar Li, Jiankai Sun, Xin Yang, Weihao Gao, Hongyi Zhang, Junyuan Xie, Vir-
ginia Smith, and Chong Wang. 2021. Label leakage and protection in two-party
split learning. arXiv preprint arXiv:2102.08504 (2021).
[15] Yang Liu, Yan Kang, Tianyuan Zou, Yanhong Pu, Yuanqin He, Xiaozhou Ye, Ye
Ouyang, Ya-Qin Zhang, and Qiang Yang. 2024. Vertical Federated Learning:
Concepts, Advances, and Challenges. IEEE Transactions on Knowledge and Data
Engineering (2024).
[16] Xiao Ma, Liqin Zhao, Guan Huang, Zhi Wang, Zelin Hu, Xiaoqiang Zhu, and Kun
Gai. 2018. Entire space multi-task model: An effective approach for estimating
post-click conversion rate. In The 41st International ACM SIGIR Conference on
Research & Development in Information Retrieval . 1137–1140.
[17] Junwei Pan, Yizhi Mao, Alfonso Lobos Ruiz, Yu Sun, and Aaron Flores. 2019.
Predicting different types of conversions with multi-task learning in online
advertising. In Proceedings of the 25th acm sigkdd international conference on
knowledge discovery & data mining . 2689–2697.
[18] Jiankai Sun, Xin Yang, Yuanshun Yao, and Chong Wang. 2022. Label Leakage
and Protection from Forward Embedding in Vertical Federated Learning. (2022).
arXiv:2203.01451 [cs.LG]
[19] Nam-Phuong Tran, Nhu-Ngoc Dao, The-Vi Nguyen, and Sungrae Cho. 2022.
Privacy-preserving learning models for communication: A tutorial on advanced
split learning. In 2022 13th International Conference on Information and Commu-
nication Technology Convergence (ICTC). IEEE, 1059–1064.
[20] Thijs Vogels, Sai Praneeth Karimireddy, and Martin Jaggi. 2019. PowerSGD:
Practical low-rank gradient compression for distributed optimization. Advances
in Neural Information Processing Systems 32 (2019).
[21] Xue Xia, Pong Eksombatchai, Nikil Pancha, Dhruvil Deven Badani, Po-Wei Wang,
Neng Gu, Saurabh Vishwas Joshi, Nazanin Farahpour, Zhiyuan Zhang, and An-
drew Zhai. 2023. Transact: Transformer-based realtime user action model for
recommendation at pinterest. In Proceedings of the 29th ACM SIGKDD Conference
on Knowledge Discovery and Data Mining . 5249–5259.
[22] Hang Xu, Chen-Yu Ho, Ahmed M Abdelmoniem, Aritra Dutta, El Houcine Bergou,
Konstantinos Karatsenidis, Marco Canini, and Panos Kalnis. 2021. Grace: A
compressed communication framework for distributed machine learning. In 2021
IEEE 41st international conference on distributed computing systems (ICDCS) . IEEE,
561–572.
[23] Zixuan Xu, Penghui Wei, Weimin Zhang, Shaoguo Liu, Liang Wang, and Bo Zheng.
2022. Ukd: Debiasing conversion rate estimation via uncertainty-regularized
knowledge distillation. In Proceedings of the ACM Web Conference 2022 . 2078–
2087.
[24] Xin Yang, Jiankai Sun, Yuanshun Yao, Junyuan Xie, and Chong Wang. 2022.
Differentially Private Label Protection in Split Learning. arXiv:2203.02073 [cs.LG]
https://arxiv.org/abs/2203.02073
[25] Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, Xuan Cao, Leon Gao, Zhao-
jie Gong, Fangda Gu, Michael He, et al. 2024. Actions Speak Louder than Words:
Trillion-Parameter Sequential Transducers for Generative Recommendations.
arXiv preprint arXiv:2402.17152 (2024).
[26] Buyun Zhang, Liang Luo, Yuxin Chen, Jade Nie, Xi Liu, Daifeng Guo, Yanli Zhao,
Shen Li, Yuchen Hao, Yantao Yao, et al. 2024. Wukong: Towards a Scaling Law
for Large-Scale Recommendation. arXiv preprint arXiv:2403.02545 (2024).
[27] Buyun Zhang, Liang Luo, Xi Liu, Jay Li, Zeliang Chen, Weilin Zhang, Xiaohan
Wei, Yuchen Hao, Michael Tsang, Wenjun Wang, et al. 2022. DHEN: A deep
and hierarchical ensemble network for large-scale click-through rate prediction.
arXiv preprint arXiv:2203.11014 (2022).
[28] Ligeng Zhu, Zhijian Liu, and Song Han. 2019. Deep Leakage from Gradients.
arXiv:1906.08935 [cs.LG]

Privacy Preserving Conversion Modeling in Data Clean Room RecSys ’24, October 14–18, 2024, Bari, Italy
A APPENDIX
A.1 CVR model architecture
A1 shows our CVR model architecture. We use transformers to con-
sume the sequence features. The output vectors enter into feature
interaction modules to cross with the other feature (numerical and
categorical) projected vectors. Our feature interaction modules com-
prise of stacked layers where each layer contains heterogeneous
feature crossing modules to fully capture bit-wise and vector-wise
feature interactions. The final predictions have a classical multi-task
learning setup.
Figure A1: CVR model architecture.
A.2 Adapter based fine tuning
Adding gated LoRA adapter layers to the CVR model: the selected
layers include the QKV layer in multi-head attention in the se-
quence transformers, the linear layers in the feature interaction
modules, and the linear layers in the multi-task towers. It has the
following benefits: (1) It is parameter efficient. We only need to
tune 1-2% parameters relative to the full model parameters; (2) It is
flexible. We can add LoRA layers to both low level and high level
layers in the pretrained model; (3) It is gated and we can use this
unified model to serve all advertisers. During serving, only the
ads candidates from the sensitive advertiser that we fine tuned on
will go through LoRA layer; the advertisers in the pretraining data
domain still use the original model parameters and is not impacted;
(4) It is scalable to multiple advertisers. We just need to add more
LoRA layers horizontally for each core module; each LoRA layer
serves one advertiser. The model training can happen in parallel
and independently even if the advertisers use different clean room
providers.
A.3 Label DP experiment results
Reduce Calibration Error . Suppose 𝑝 is the original positive
probability, 𝑛+ is the number of positive instances, and 𝑛− is the
number of negative instances in the original dataset. Then, 𝑝 =
𝑛+
𝑛++𝑛− = 1 1+ 𝑛− 𝑛+ . Suppose the flipping probability is 1− 𝑞𝜖. After flip-
ping, the new positive ratio is 𝑝′ = 𝑛+𝑞𝜖+𝑛−(1−𝑞𝜖) 𝑛++𝑛− = 𝑞𝜖+ 𝑛− 𝑛+(1−𝑞𝜖) 1+ 𝑛− 𝑛+ .
Hence 𝑝′ = 𝑝𝑞𝜖+( 1− 𝑝)( 1− 𝑞𝜖). During model training, we can
use the de-biasing function in our loss function 𝑙𝑑𝑒𝑏(𝑝) = 𝑙(𝑝′) =
𝑙(𝑝𝑞𝜖+( 1− 𝑝)( 1− 𝑞𝜖)) to adjust the predictions. At model serving
time, we use the model output directly as our prediction, which is
close to the original distribution. We demonstrated the effectiveness
of the debias function as shown in Table A1.
Calibration ratio used in our experiments is calculated as˝𝑛 𝑖 𝑝𝑖 𝑛+ 𝑛++𝑛−
where 𝑝𝑖 is the predicted probability for sample 𝑖. If the ratio is
above 1, it means our model is over-forecasting. If the ratio is smaller
than 1, it indicates that our model is under-forecasting. A perfect
ratio would be 1.
