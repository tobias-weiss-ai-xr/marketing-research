---
title: 'FairLint-DL: An IDE-Native Tool for Fairness Debugging of Deep Learning Software'
url: https://arxiv.org/abs/2609.16321
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Archit Rathod
- Saeid Tizpaz-Niari
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.16321
pages: 5
chars: 34204
fetched_at: '2026-11-08T13:21:30+00:00'
kb_version: 1
---

# FairLint-DL: An IDE-Native Tool for Fairness Debugging of Deep Learning Software

FairLint-DL: An IDE-Native Tool for Fairness Debugging of Deep
Learning Software
Archit Rathod
University of Illinois at Chicago
Chicago, USA
arath21@uic.edu
Saeid Tizpaz-Niari
University of Illinois at Chicago
Chicago, USA
saeid@uic.edu
Abstract
Existing fairness analysis tools predominantly operate as post-
training evaluation frameworks, requiring practitioners to com-
plete the full model development lifecycle before assessing bias.
We presentFairLint-DL, a Visual Studio Code extension that im-
plements ashift-leftapproach to fairness testing by enabling pre-
training, IDE-native bias detection directly on tabular datasets.
FairLint-DLtrains a configurable deep neural network as a proxy
model and applies information-theoretic Quantitative Individual
Discrimination (QID) metrics. Grounded in Shannon and min-entropy,
QID quantifies the causal influence of protected attributes on predic-
tions. The system implements a two-phase gradient-guided search
algorithm for discovering discriminatory instances, a causal de-
bugging pipeline that localizes bias to specific network layers and
neurons via sensitivity analysis, and dual explainability engines
using SHAP and LIME for feature-level attribution. Evaluation on
three tabular benchmarks (Adult Census Income, German Credit,
and Bank Marketing) reveals fairness concerns that vary widely
across datasets: on Adult, 96.0% of analyzed instances exhibit QID
above the 0.1-bit significance threshold, with a mean QID of 0.619
bits and a disparate impact ratio of 0.581, violating the four-fifths
legal rule.FairLint-DLproduces these results within 12 seconds on
cached models, demonstrating the feasibility of integrating fairness
analysis into the developer workflow without significant overhead.
Demo video:https://youtu.be/AmfpjK24uwY
Source:https://github.com/Archit1706/FairLint-DL
Tool:https://open-vsx.org/extension/ArchitRathod/fairlint-dl
CCS Concepts
•Software and its engineering → Software testing and debug-
ging;•Computing methodologies→Machine learning.
Keywords
Debugging, Fairness, Deep Learning Software
ACM Reference Format:
Archit Rathod and Saeid Tizpaz-Niari. 2026. FairLint-DL: An IDE-Native
Tool for Fairness Debugging of Deep Learning Software. InProceedings of the
41st IEEE/ACM International Conference on Automated Software Engineering
(ASE ’26), October 12–16, 2026, Munich, Germany.ACM, New York, NY, USA,
5 pages. https://doi.org/10.1145/3832783.3834602
This work is licensed under a Creative Commons Attribution 4.0 International License.
ASE ’26, Munich, Germany
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2882-2/2026/10
https://doi.org/10.1145/3832783.3834602
1 Introduction
The widespread adoption of deep neural networks (DNNs) in high-
stakes decision-making systems has introduced significant con-
cerns regarding algorithmic fairness. Instances of such AI-assisted
software include systems deciding on recidivism risk, software pre-
dicting benefit eligibility, and tools deciding whether to audit a
given taxpayer [23]. Such models often encode and amplify pre-
existing biases in the training data. The resulting fairness defects
may disadvantage protected groups and may also violate statu-
tory requirements such as the Civil Rights Act’s disparate impact
provisions and the EU AI Act’s fairness mandates.
The Shift-Left Fairness Testing Paradigm.Current fairness
tools predominantly operate in a post-training paradigm: practi-
tioners must complete the full model development lifecycle. Tools
such as IBM’s AI Fairness 360, Google’s What-If Tool, Microsoft’s
Fairlearn, and Fairkit-learn [5, 18, 32, 33] provide valuable post-hoc
analysis but require significant upfront investment before fairness
issues are identified. Pre-training fairness assessment on datasets is
itself well studied; our goal is not to claim it as new, but to make it a
low-friction step inside the developer’s editor.FairLint-DLapplies
this shift-left view to fairness testing, analogous to shift-left testing
in software engineering. Delivered as a VS Code extension, it lets
practitioners assess dataset bias before committing to a specific
model architecture or training pipeline. The proxy DNN is trained
once and cached as a fairness oracle for the dataset, so iteration
cost on the developer’s own model is zero and dataset-level bias
signals (QID, group disparities) surface independently of the final
architecture. Bias detected early is cheaper to fix; the feedback loop
is tighter because results appear where code is written.
We usefairness debuggingto mean the workflow of detecting,
quantifying, localizing, and explaining bias so that a developer can
act on it, and we name the toolFairLint-DLbecause it brings this
workflow to the point of editing, in the spirit of a linter, rather than
performing static analysis on source code.
Contributions.The techniques we build on, namely QID, gradient-
guided search, layer and neuron causal localization, and SHAP/LIME
attribution, are established in prior work [10, 21, 23, 26]; the contri-
bution of this paper is their integration into a single editor-native,
pre-training workflow rather than the techniques themselves. Con-
cretely, we contribute: (1) an editor-integrated tool that packages
pre-training fairness debugging behind a right-click on a dataset; (2)
an end-to-end pipeline combining information-theoretic QID met-
rics, a two-phase discriminatory-instance search, layer and neuron
localization, dual SHAP/LIME attribution, and a composite fairness
score; and (3) an evaluation on three tabular fairness benchmarks.
arXiv:2609.16321v1  [cs.SE]  14 Sep 2026

ASE ’26, October 12–16, 2026, Munich, Germany Archit Rathod and Saeid Tizpaz-Niari
Table 1: Positioning ofFairLint-DLrelative to existing fair-
ness tools.IDE: editor-native integration;Pre: pre-training fo-
cus;DNN: DNN causal localization, i.e., attributing bias to spe-
cific layers and neurons of a deep network;QID: information-
theoretic QID;GS: gradient-guided search;Grp: group fair-
ness;XAI: SHAP/LIME. These dimensions describe the de-
sign spaceFairLint-DLtargets, not an exhaustive ranking;
toolkits such as AI Fairness 360 and Fairlearn expose many
statistical fairness metrics thatFairLint-DLdoes not.
Tool IDE Pre DNN QID GS Grp XAI
AI Fairness 360 [5] — — — — —✓part.
Fairlearn [32] — — — — —✓—
What-If Tool [33] — — — — —✓part.
Fairkit-learn [18] — — — — —✓—
FairLay-ML [35] — — — — —✓LIME
DICE (CLI) [23] — —✓ ✓— — —
NeuFair (CLI) [10] — —✓—✓ ✓—
FairLint-DL✓ ✓ ✓ ✓ ✓ ✓ ✓
2 Background
Fairness Definitions.Individual fairness, formalized by Dwork et
al. [12], requires that similar individuals receive similar outcomes.
Group fairness requires parity of some statistical measure across
demographic groups.FairLint-DLcomputes Demographic Parity,
Equalized Odds [ 16], and Equal Opportunity. These metrics are
complementary: well-known impossibility results show that cali-
bration, equalized odds, and unequal base rates cannot be jointly
satisfied [9, 19], motivating the multi-metric approach.
State-of-the-art Tools.The DICE framework [ 23] introduced
Quantitative Individual Discrimination (QID) as an information-
theoretic characterization of discrimination, and a causal debugging
algorithm that uses interventions on neuron activations to localize
layers and neurons with significant causal effects on QID. Neu-
Fair [10] extends the search via a two-phase global-local approach
with gradient-based optimization, and formulates fairness repair as
simulated annealing over neuron dropout.FairLint-DLalso draws
on the EVT framework [22], which applies extreme value theory
to worst-case discrimination.
Table 1 comparesFairLint-DLwith representative tools. AI
Fairness 360 and Fairlearn are Python APIs that practitioners in-
strument after training; the What-If Tool is a post-training GUI;
Fairkit-learn targets model selection on the fairness-accuracy fron-
tier; FairLay-ML [35] is a separate web application for scikit-learn
classifiers; and DICE [ 23] and NeuFair [ 10], the closest research
artifacts, are CLI tools tied to benchmark scripts.FairLint-DLcom-
bines the information-theoretic rigor of DICE with the search of
NeuFair behind an editor-native workflow.
3 System Architecture and Design
FairLint-DLoperates as a client-server application with two pri-
mary components communicating over HTTP/REST onlocalhost:8765
(Figure 1). TheVS Code Extension (Client), written in TypeScript,
handles all user interaction, file system access, WebView dashboard
rendering with Plotly.js charts, and manages the lifecycle of the
Python backend. ThePython FastAPI Backend (Server)hosts
the PyTorch models and all analysis algorithms, including data
preprocessing, model training, QID computation, causal debugging,
Figure 1:FairLint-DLclient-server architecture overview.
discriminatory instance search, and SHAP/LIME explainability. The
extension launches and manages the backend as a local process, so
no separate server deployment is required. Because the two compo-
nents communicate only over HTTP/REST, the tool is not bound to
VS Code: the extension runs unmodified in any VS Code-compatible
IDE, including Cursor and Antigravity, and the same endpoints can
be driven by a CI job or a script.
Six-Step Analysis Pipeline.The pipeline is: model training (or
cached load), PCA-based internal space visualization, QID and
group fairness computation across all protected attributes [ 23],
gradient-guided global plus perturbation-based local search for dis-
criminatory instances [10, 23], layer/neuron causal debugging [23],
and batch SHAP (KernelExplainer on log-odds) plus LIME explana-
tions [21, 26].
4 Algorithmic Methodology
DNN Proxy Model.FairLint-DLtrains a feedforward DNN as a
proxy model to serve as a “fairness oracle. ” The default architec-
ture uses 5 fully-connected hidden layers of ⟨64, 32, 16, 8, 4⟩ neu-
rons followed by a 2-unit softmax output head (∼4K parameters
total), following the architecture used in prior fairness testing lit-
erature [10, 23]. Each hidden layer applies Batch Normalization,
ReLU activation, and Dropout ( 𝑝= 0.2). We train a DNN rather
than run statistical tests on raw data because the differentiable
model supports counterfactual and gradient-based search, learns
non-linear feature interactions, and lets causal debugging trace bias
through internal representations.
QID Metrics.For non-protected 𝑋=𝑥 and protected 𝑍=𝑧 ,
the Shannon entropy QID quantifies prediction uncertainty when
varying𝑍at fixed𝑋:
QIDShannon(𝑥)=−
∑︁
𝑦
¯𝑃(𝑌=𝑦|𝑥)log 2 ¯𝑃(𝑌=𝑦|𝑥)(1)
where ¯𝑃(𝑌=𝑦|𝑥) is the average prediction probability across all
counterfactual variations of the protected attributes [23].FairLint-
DLalso computes the disparate impact ratio
DI(𝑥)=min
𝑧
𝑃( ˆ𝑌=1|𝑥, 𝑧)/max
𝑧
𝑃( ˆ𝑌=1|𝑥, 𝑧)(2)
The four-fifths rule (DI≤ 0.8) is the established U.S. civil rights
threshold for adverse impact in employment discrimination; we
keep it fixed by legal convention rather than as a tunable knob,

FairLint-DL: An IDE-Native Tool for Fairness Debugging of Deep Learning Software ASE ’26, October 12–16, 2026, Munich, Germany
whereas the QID significance threshold, epochs, batch size, layer
sizes, and sample count are all user-configurable settings.
Gradient-Guided Search.The search for discriminatory instances
is formulated as a two-phase optimization problem [10, 23]. Phase
1 (Global) maximizes the QID score directly using gradient ascent
over input features. Phase 2 (Local) explores the neighborhood of
the global optimum by adding Gaussian noise to non-protected
features and filtering neighbors that exceed a threshold of0 .1bits.
Causal Debugging.Layer localization determines which layer is
most sensitive to discriminatory inputs by computing the gradi-
ent of layer activations with respect to the input and aggregating
the magnitude of these gradients for known discriminatory in-
stances. Within the bias-critical layer, neuron localization follows
the Average Causal Difference framework from DICE [23]: the tool
intervenes on each neuron by forcing it active or inactive and mea-
sures the resulting change in QID. Neurons with disproportionately
high impact scores are candidates for pruning or repair.
Composite Fairness Score.A 0 to 100 score combines five penalty
components (mean QID, % discriminatory, disparate impact, max
QID, group fairness). The weights are fixed constants in the current
release and are listed in the artifact; exposing them as user settings
is left to future work.
5 Implementation and Usage
Technology Stack.The backend uses PyTorch 2.0+ for model
training and gradient computation, FastAPI + Uvicorn for the REST
API, Pandas and Scikit-learn for data processing, and SHAP and
LIME for feature attribution. The frontend is a TypeScript VS Code
extension that renders interactive charts via Plotly.js.
Model Caching.To avoid redundant retraining,FairLint-DL
caches trained models under a deterministic SHA-256 key com-
puted from the CSV contents, label column, sorted sensitive fea-
tures, hidden layer sizes, epochs, and batch size.
Workflow.Users trigger analysis via the context menu (right-click
on a .csv file) (Figure 2). The extension presents QuickPick dialogs
for selecting the label column, protected attributes, and model archi-
tecture. Protected attributes are auto-detected by matching column
names, case-insensitively, against a small curated set of regular
expressions for common sensitive categories: sex or gender, race
or ethnicity, age, nationality or country, religion, and disability.
Auto-detection is only a default; the developer can deselect or add
attributes in the QuickPick dialog. Configurable settings are ex-
posed through VS Code’s settings API, including training epochs,
batch size, hidden layer configuration, QID threshold, maximum
analysis samples, server port, and visualization theme.
Availability.FairLint-DLis MIT-licensed and published on the
VS Code Marketplace and Open VSX for one-click install in any
compatible IDE; from source, npm install && npm run compile
builds the extension and pip install -r requirements.txt the
backend. The backend ships with a unit-test suite covering QID,
search, causal debugging, and group fairness.
6 Experimental Evaluation
Dataset.The Adult Census Income dataset [ 4] contains 32,561
records from the 1994 U.S. Census Bureau database; the predic-
tion task is binary classification of whether annual income exceeds
Figure 2:FairLint-DLintegrates into the editor workflow.
$50,000. Four protected attributes were selected: age (71 unique
values), race (5), sex (2), and native-country (42). The dataset was
split into 22,792 training, 3,256 validation, and 6,513 held-out test
instances; the proxy DNN was trained for 30 epochs (training-set
class distribution: 17,303 negative, 5,489 positive), and all fairness
results below are computed on 500 instances sampled from the held-
out test split. To test generalizability beyond a single benchmark,
we apply the same architecture and protocol to German Credit [17]
(1,000 records; protected attributes age and sex) and Bank Market-
ing [24] (45,211 records; protected attributes age and marital status).
Table 2 reports QID and composite results for all three; the figures
below detail the Adult case.
QID Analysis.On Adult, 500 sampled test instances reveal perva-
sive individual discrimination (Table 2): a mean QID of 0.619 bits (of
a 1.0-bit maximum) and a 96.0% discrimination rate mean the model
changes its prediction for nearly every individual when protected
attributes are altered, and the mean disparate impact of 0.581 falls
well below the 0.8 threshold. The QID histogram (Figure 3) is bi-
modal, with a small cluster near zero and a large mass approaching
1.0 bit, indicating that discrimination is a systemic property of the
decision boundary rather than an edge-case phenomenon. The same
pipeline surfaces markedly different profiles on the other bench-
marks (Table 2): German Credit is the most severe at the individual
level (mean QID 0.935, all instances discriminatory), while Bank
Marketing is the mildest (mean QID 0.284, 51.6% discriminatory),
giving composite scores of 46 and 75 against Adult’s 41. German
Credit also illustrates that individual and group views can disagree:
nearly every instance is individually discriminatory even though
its aggregate disparate impact ratio of 0.94 satisfies the four-fifths
rule.
Causal Debugging.Layer 2 (32 neurons) is the most bias-sensitive
layer (sensitivity 1.933), indicating that early-to-middle layers en-
code protected information before it propagates deeper. This matches
the DICE results on Adult, which also identified the second layer [23].
Within Layer 2, Neurons 30 (1.362), 17 (1.270), and 8 (1.220) have
the highest impact and are prime candidates for the neuron-level
dropout proposed by NeuFair [10].
Explainability.SHAP global importance (log-odds) rankseducation
-num (0.891), age (0.690), and marital-status (0.688) highest; age,
a protected attribute, ranks second. SHAP and LIME agree on

ASE ’26, October 12–16, 2026, Munich, Germany Archit Rathod and Saeid Tizpaz-Niari
Table 2: Individual (QID) and group fairness across three
benchmarks (500 test instances each for Adult and Bank; 200
for German). Protected: Adult (age, race, sex, country), Ger-
man (age, sex), Bank (age, marital). Group diffs are averaged
over attributes; Bank’s are near zero as its majority-class pre-
dictions give near-equal group rates.
Metric Adult German Bank
Mean QID (Shannon, bits) 0.619 0.935 0.284
Mean min-entropy QID (bits) 0.214 0.428 0.108
Mean disparate impact ratio 0.581 0.939 0.815
Discriminatory (QID>0.1) 96.0% 100.0% 51.6%
Violating 80% rule 69.8% 3.5% 42.2%
Demographic parity diff. 0.091 0.095 0.000
Equalized odds diff. 0.102 0.114 0.000
Model accuracy (%) 84.1 68.5 88.3
Composite fairness score 41 46 75
Figure 3: Distribution of QID values across 500 analyzed in-
stances on Adult Census; 96.0% exceed the 0.1-bit threshold.
Figure 4: SHAP and LIME global feature importance on Adult
Census; both methods agree that education-num and age (a
protected attribute) are top drivers.
education-num and on the measurable influence of age (Figure 4),
giving high confidence in the attribution.
Composite Fairness Score and Performance.Adult’s final score
of approximately 41 out of 100 is rated “Concerning. ” With caching,
the full analysis completes in about 12 (s) (SHAP+LIME dominates
at∼7s; other steps≤2s); first-run training adds about 77 (s).
7 Discussion and Limitations
Interpretation.On Adult, discrimination is a property of the
learned decision boundary rather than an edge case. Although
race shows minimal direct SHAP importance (0.010), the group fair-
ness analysis reveals significant discrimination across racial groups
(race-specific DP ratio 0.564), suggesting that race influences predic-
tions indirectly through correlated proxy features, a form of proxy
discrimination that single-method analysis may miss.
Limitations.FairLint-DLtrains its own DNN proxy rather
than analyzing a user-supplied model, so the detected bias reflects
the proxy and may differ from a production model with a different
architecture or fairness constraints; we have not yet compared QID
on our proxy against alternative families such as gradient-boosted
trees. The≤ 0vs. > 0group split suits binary attributes but not
continuous or multi-class ones, where quantile-based splits are a
natural extension. SHAP’s KernelExplainer scales quadratically in
the number of features and is the bottleneck. Broader validation on
intersectional attributes remains future work.
8 Related Work
Fairness Testing.Counterfactual discrimination, introduced by
Galhotra et al. [14], catalyzed a broad line of research on generating
test cases at scale [2, 6, 13]. One family of generators operates in
ablack-boxsetting and requires no access to the internals of the
classifier under test, includingAEQUITAS[ 30],SG[ 2],ExpGA[ 13],
LIMI[ 34], andAFT[ 40]. A second family adopts awhite-boxsetting
and exploits gradient- or neuron-level information from the model,
includingADF[ 39],EIDIG[ 37],NeuronFair[ 41],DICE[ 23], and
MAFT[ 31].FairLint-DLbuilds on this white-box tradition, and
its metrics are closely related to the information-theoretic view of
discrimination [3, 23]. However,FairLint-DLsurfaces IDIs early
in development and directly within the IDE. The complementary
problem of group fairness testing has likewise been studied exten-
sively [7, 8, 27, 29, 36].
Bias Mitigation.A substantial body of work mitigates bias in
machine learning outputs through pre-, in-, and post-processing
interventions, including post-processing methods that adjust model
decisions after training [ 10, 11, 15, 20, 28, 38]. These efforts are
largely orthogonal and complementary toFairLint-DL.
9 Conclusion and Future Work
We presentedFairLint-DL, a VS Code extension for deep learning-
based fairness debugging of machine learning datasets. By imple-
menting the shift-left fairness testing paradigm,FairLint-DLen-
ables practitioners to detect, quantify, localize, and explain bias di-
rectly within their development environment. Future work includes
integrating in-processing fairness interventions such as adversarial
debiasing, fairness-constrained optimization [ 1], or the NeuFair
dropout strategy [10] directly into the extension; extending evalua-
tion to further datasets such as COMPAS; analyzing intersectional
fairness across combinations of protected attributes; and supporting
external model analysis beyond proxy models.
Acknowledgments
This project has been partially supported by NSF award CCF-2536640.

FairLint-DL: An IDE-Native Tool for Fairness Debugging of Deep Learning Software ASE ’26, October 12–16, 2026, Munich, Germany
Data Availability Statement
TheFairLint-DLsource code, datasets, and evaluation scripts
are archived on Zenodo [25] (DOI: https://doi.org/10.5281/zenodo.
21362910) under the MIT license; the archive includesreproduce.py,
which regenerates Table 2 from the bundled datasets. The live
source and packaged extension are linked in the abstract.
References
[1] Alekh Agarwal, Alina Beygelzimer, Miroslav Dudík, John Langford, and Hanna Wallach. 2018.
A Reductions Approach to Fair Classification. InProceedings of the 35th International Conference
on Machine Learning (ICML) (PMLR, Vol. 80). 60–69.
[2] Aniya Aggarwal, Pranay Lohia, Seema Nagar, Kuntal Dey, and Diptikalyan Saha. 2019. Black
Box Fairness Testing of Machine Learning Models. InProceedings of the 2019 27th ACM Joint
Meeting on European Software Engineering Conference and Symposium on the Foundations of
Software Engineering (ESEC/FSE 2019). 625–635. doi:10.1145/3338906.3338937
[3] Ranit D. Akash, Ashish Kumar, Verya Monjezi, Ashutosh Trivedi, Gang Tan, and Saeid Tizpaz-
Niari. 2025. Uncovering Discrimination Clusters: Quantifying and Explaining Systematic
Fairness Violations. In2025 40th IEEE/ACM International Conference on Automated Software
Engineering (ASE). 1680–1692. doi:10.1109/ASE63991.2025.00141
[4] Barry Becker and Ronny Kohavi. 1996. Adult. UCI Machine Learning Repository. DOI:
https://doi.org/10.24432/C5XW20.
[5] R. K. E. Bellamy, K. Dey, M. Hind, et al. 2019. AI Fairness 360: An extensible toolkit for detecting
and mitigating algorithmic bias.IBM Journal of Research and Development63, 4/5 (2019),
4:1–4:15. doi:10.1147/JRD.2019.2942287
[6] Sumon Biswas and Hridesh Rajan. 2023. Fairify: Fairness Verification of Neural Networks. In
Proceedings of the 45th International Conference on Software Engineering(Melbourne, Victoria,
Australia)(ICSE ’23). IEEE Press, 1546–1558. doi:10.1109/ICSE48619.2023.00134
[7] Joymallya Chakraborty, Suvodeep Majumder, and Tim Menzies. 2021. Bias in Machine Learning
Software: Why? How? What to Do?. InProceedings of the 29th ACM Joint Meeting on European
Software Engineering Conference and Symposium on the Foundations of Software Engineering
(ESEC/FSE 2021). Association for Computing Machinery, New York, NY, USA, 429–440. doi:10.
1145/3468264.3468537
[8] Joymallya Chakraborty, Suvodeep Majumder, Zhe Yu, and Tim Menzies. 2020. Fairway: a way
to build fair ML software. InProceedings of the 28th ACM Joint Meeting on European Software
Engineering Conference and Symposium on the Foundations of Software Engineering(Virtual
Event, USA)(ESEC/FSE 2020). Association for Computing Machinery, New York, NY, USA,
654–665. doi:10.1145/3368089.3409697
[9] Alexandra Chouldechova. 2017. Fair Prediction with Disparate Impact: A Study of Bias in
Recidivism Prediction Instruments.Big Data5, 2 (2017), 153–163. doi:10.1089/big.2016.0047
[10] Vishnu Asutosh Dasu, Ashish Kumar, Saeid Tizpaz-Niari, and Gang Tan. 2024. NeuFair: Neural
Network Fairness Repair with Dropout. InProceedings of the 33rd ACM SIGSOFT International
Symposium on Software Testing and Analysis (ISSTA). 1541–1553. doi:10.1145/3650212.3680380
[11] Vishnu Asutosh Dasu, Md Rafi Ur Rashid, Vipul Gupta Saeid Tizpaz-Niari, and Gang Tan. 2026.
Attention Pruning: Automated Fairness Repair of Language Models via Surrogate Simulated
Annealing. In48th International Conference on Software Engineering (ICSE). To appear.
[12] Cynthia Dwork, Moritz Hardt, Toniann Pitassi, Omer Reingold, and Richard Zemel. 2012.
Fairness Through Awareness. InProceedings of the 3rd Innovations in Theoretical Computer
Science Conference (ITCS). 214–226. doi:10.1145/2090236.2090255
[13] Ming Fan, Wenying Wei, Wuxia Jin, Zijiang Yang, and Ting Liu. 2022. Explanation-guided
fairness testing through genetic algorithm. InProceedings of the 44th International Conference
on Software Engineering(Pittsburgh, Pennsylvania)(ICSE ’22). Association for Computing
Machinery, New York, NY, USA, 871–882. doi:10.1145/3510003.3510137
[14] Sainyam Galhotra, Yuriy Brun, and Alexandra Meliou. 2017. Fairness testing: testing software
for discrimination. InProceedings of the 2017 11th Joint Meeting on Foundations of Software
Engineering (ESEC/FSE’17). ACM, 498–510. doi:10.1145/3106237.3106277
[15] Xuanqi Gao, Juan Zhai, Shiqing Ma, Chao Shen, Yufei Chen, and Qian Wang. 2022. FairNeu-
ron: improving deep neural network fairness with adversary games on selective neurons. In
Proceedings of the 44th International Conference on Software Engineering(Pittsburgh, Penn-
sylvania)(ICSE ’22). Association for Computing Machinery, New York, NY, USA, 921–933.
doi:10.1145/3510003.3510087
[16] Moritz Hardt, Eric Price, and Nathan Srebro. 2016. Equality of Opportunity in Supervised
Learning. InProceedings of the 30th International Conference on Neural Information Processing
Systems (NIPS). 3323–3331.
[17] Hans Hofmann. 1994. Statlog (German Credit Data). UCI Machine Learning Repository. DOI:
https://doi.org/10.24432/C5NC77.
[18] Brittany Johnson and Yuriy Brun. 2022. Fairkit-learn: a fairness evaluation and comparison
toolkit. InProceedings of the ACM/IEEE 44th International Conference on Software Engineering:
Companion Proceedings(Pittsburgh, Pennsylvania)(ICSE ’22). Association for Computing
Machinery, New York, NY, USA, 70–74. doi:10.1145/3510454.3516830
[19] Jon Kleinberg, Sendhil Mullainathan, and Manish Raghavan. 2016. Inherent Trade-Offs in the
Fair Determination of Risk Scores. arXiv:1609.05807 [cs.LG] https://arxiv.org/abs/1609.05807
[20] Tianlin Li, Xiaofei Xie, Jian Wang, Qing Guo, Aishan Liu, Lei Ma, and Yang Liu. 2023. Faire:
Repairing Fairness of Neural Networks via Neuron Condition Synthesis.ACM Trans. Softw.
Eng. Methodol.33, 1, Article 21 (Nov. 2023), 24 pages. doi:10.1145/3617168
[21] Scott M. Lundberg and Su-In Lee. 2017. A unified approach to interpreting model predictions. In
Proceedings of the 31st International Conference on Neural Information Processing Systems(Long
Beach, California, USA)(NIPS’17). Curran Associates Inc., Red Hook, NY, USA, 4768–4777.
[22] Verya Monjezi, Ashutosh Trivedi, Vladik Kreinovich, and Saeid Tizpaz-Niari. 2025. Fairness
Testing through Extreme Value Theory. InProceedings of the IEEE/ACM 47th International
Conference on Software Engineering(Ottawa, Ontario, Canada)(ICSE ’25). IEEE Press, 1501–1513.
doi:10.1109/ICSE55347.2025.00070
[23] Verya Monjezi, Ashutosh Trivedi, Gang Tan, and Saeid Tizpaz-Niari. 2023. Information-
Theoretic Testing and Debugging of Fairness Defects in Deep Neural Networks. InProceedings
of the 45th International Conference on Software Engineering (ICSE). 1571–1582. doi:10.1109/
ICSE48619.2023.00136
[24] S. Moro, P. Rita, and P. Cortez. 2014. Bank Marketing. UCI Machine Learning Repository. DOI:
https://doi.org/10.24432/C5K306.
[25] Archit Rathod and Saeid Tizpaz-Niari. 2026. Reproduction Package for Article ‘FairLint-DL:
An IDE-Native Tool for Fairness Debugging of Deep Learning Software’. Zenodo. doi:10.5281/
zenodo.21142733
[26] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. 2016. “Why Should I Trust You?”:
Explaining the Predictions of Any Classifier. InProceedings of the 22nd ACM SIGKDD Inter-
national Conference on Knowledge Discovery and Data Mining (KDD). 1135–1144. doi:10.1145/
2939672.2939778
[27] Salvador Robles Herrera, Verya Monjezi, Vladik Kreinovich, Ashutosh Trivedi, and Saeid Tizpaz-
Niari. 2024. Predicting Fairness of ML Software Configurations. InProceedings of the 20th
International Conference on Predictive Models and Data Analytics in Software Engineering(Porto
de Galinhas, Brazil)(PROMISE 2024). Association for Computing Machinery, New York, NY,
USA, 56–65. doi:10.1145/3663533.3664040
[28] Bing Sun, Jun Sun, Long H. Pham, and Jie Shi. 2022. Causality-based neural network repair.
InProceedings of the 44th International Conference on Software Engineering(Pittsburgh, Penn-
sylvania)(ICSE ’22). Association for Computing Machinery, New York, NY, USA, 338–349.
doi:10.1145/3510003.3510080
[29] Saeid Tizpaz-Niari, Ashish Kumar, Gang Tan, and Ashutosh Trivedi. 2022. Fairness-aware
configuration of machine learning libraries. InProceedings of the 44th International Conference
on Software Engineering(Pittsburgh, Pennsylvania)(ICSE ’22). Association for Computing
Machinery, New York, NY, USA, 909–920. doi:10.1145/3510003.3510202
[30] Sakshi Udeshi, Pryanshu Arora, and Sudipta Chattopadhyay. 2018. Automated directed fairness
testing. InProceedings of the 33rd ACM/IEEE International Conference on Automated Software
Engineering(Montpellier, France)(ASE ’18). Association for Computing Machinery, New York,
NY, USA, 98–108. doi:10.1145/3238147.3238165
[31] Zhaohui Wang, Min Zhang, Jingran Yang, Bojie Shao, and Min Zhang. 2024. MAFT: Efficient
Model-Agnostic Fairness Testing for Deep Neural Networks via Zero-Order Gradient Search.
InProceedings of the IEEE/ACM 46th International Conference on Software Engineering(Lisbon,
Portugal)(ICSE ’24). Association for Computing Machinery, New York, NY, USA, Article 121,
12 pages. doi:10.1145/3597503.3639181
[32] Hilde Weerts, Miroslav Dudík, Richard Edgar, Adrin Jalali, Roman Lutz, and Michael Madaio.
2023. Fairlearn: Assessing and Improving Fairness of AI Systems.Journal of Machine Learning
Research24, 1, Article 257 (2023).
[33] James Wexler, Mahima Pushkarna, Tolga Bolukbasi, Martin Wattenberg, Fernanda B. Viégas,
and Jimbo Wilson. 2019. The What-If Tool: Interactive Probing of Machine Learning Models.
IEEE Transactions on Visualization and Computer Graphics26 (2019), 56–65. doi:10.1109/TVCG.
2019.2934619
[34] Yisong Xiao, Aishan Liu, Tianlin Li, and Xianglong Liu. 2023. Latent Imitator: Generating
Natural Individual Discriminatory Instances for Black-Box Fairness Testing. InProceedings
of the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis(Seattle,
WA, USA)(ISSTA 2023). Association for Computing Machinery, New York, NY, USA, 829–841.
doi:10.1145/3597926.3598099
[35] Normen Yu, Luciana Carreon, Gang Tan, and Saeid Tizpaz-Niari. 2025. FairLay-ML: Intuitive
Debugging of Fairness in Data-Driven Social-Critical Software. InProceedings of the 47th
International Conference on Software Engineering (ICSE), Companion. IEEE, 25–28. doi:10.1109/
ICSE-COMPANION66252.2025.00016
[36] Jie M. Zhang and Mark Harman. 2021. "Ignorance and Prejudice" in Software Fairness. In43rd
IEEE/ACM International Conference on Software Engineering, ICSE 2021, Madrid, Spain, 22-30
May 2021. IEEE, 1436–1447. doi:10.1109/ICSE43902.2021.00129
[37] Lingfeng Zhang, Yueling Zhang, and Min Zhang. 2021. Efficient white-box fairness testing
through gradient search. InProceedings of the 30th ACM SIGSOFT International Symposium
on Software Testing and Analysis(Virtual, Denmark)(ISSTA 2021). Association for Computing
Machinery, New York, NY, USA, 103–114. doi:10.1145/3460319.3464820
[38] Mengdi Zhang and Jun Sun. 2022. Adaptive fairness improvement based on causality analysis.
InProceedings of the 30th ACM Joint European Software Engineering Conference and Symposium
on the Foundations of Software Engineering(Singapore, Singapore)(ESEC/FSE 2022). Association
for Computing Machinery, New York, NY, USA, 6–17. doi:10.1145/3540250.3549103
[39] Peixin Zhang, Jingyi Wang, Jun Sun, Guoliang Dong, Xinyu Wang, Xingen Wang, Jin Song Dong,
and Ting Dai. 2020. White-box fairness testing through adversarial sampling. InProceedings
of the ACM/IEEE 42nd International Conference on Software Engineering(Seoul, South Korea)
(ICSE ’20). Association for Computing Machinery, New York, NY, USA, 949–960. doi:10.1145/
3377811.3380331
[40] Zhenjiang Zhao, Takahisa Toda, and Takashi Kitamura. 2024. Approximation-guided Fairness
Testing through Discriminatory Space Analysis. InProceedings of the 39th IEEE/ACM Interna-
tional Conference on Automated Software Engineering(Sacramento, CA, USA)(ASE ’24). Associ-
ation for Computing Machinery, New York, NY, USA, 1007–1018. doi:10.1145/3691620.3695481
[41] Haibin Zheng, Zhiqing Chen, Tianyu Du, Xuhong Zhang, Yao Cheng, Shouling Ji, Jingyi Wang,
Yue Yu, and Jinyin Chen. 2022. NeuronFair: interpretable white-box fairness testing through
biased neuron identification. InProceedings of the 44th International Conference on Software
Engineering(Pittsburgh, Pennsylvania)(ICSE ’22). Association for Computing Machinery, New
York, NY, USA, 1519–1531. doi:10.1145/3510003.3510123
Received 2026-05-09; accepted 2026-06-19
