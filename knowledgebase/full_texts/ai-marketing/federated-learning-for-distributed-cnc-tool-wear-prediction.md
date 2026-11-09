---
title: Federated Learning for Distributed CNC Tool Wear Prediction
url: https://arxiv.org/abs/2608.11281
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Afsana Khan
- Morris Stallmann
- Marcin Pietrasik
- Charalampos S. Kouzinopoulos
- Anna Wilbik
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.11281
pages: 7
chars: 15726
fetched_at: '2026-11-08T13:28:32+00:00'
kb_version: 1
---

# Federated Learning for Distributed CNC Tool Wear Prediction

Federated Learning for Distributed CNC Tool
Wear Prediction
Afsana Khan⋆, Morris Stallmann, Marcin Pietrasik,
Charalampos S. Kouzinopoulos, and Anna Wilbik
Maastricht University, Maastricht, Netherlands
a.khan@maastrichtuniversity.nl
Abstract.ToolwearpredictionisanimportanttaskinCNCmachining,
where accurate monitoring of tool condition supports product quality
and process reliability. Machine learning methods have shown potential
for this task, but their use in industrial environments is limited by the
distributed nature of machining data and by restrictions on data shar-
ing between machines, sites, or organizations. Federated learning offers a
suitable framework for this setting by enabling collaborative model train-
ing without transferring raw operational data. However, it is open if fed-
erated learning can lead to accuracy gains in CNC tool wear prediction
that justify the increased complexity of such a system. In this experimen-
tal study, real tool trajectories are distributed across simulated clients to
represent a federated learning scenario. The federated models are com-
pared against centralized references and local client baselines. Results
show that federated learning achieves performance close to centralized
learning and improves significantly over local client models. These find-
ings indicate that federated learning can support collaborative tool wear
prediction in distributed CNC manufacturing environments and the in-
creased complexity is justified.
Introduction
Cutting tools are essential in machining processes such as milling, drilling, and
sawing, but are affected by wear due to abrasion, adhesion, and diffusion, which
can eventually lead to tool failure or defective parts [10,12]. Machine learning
(ML) methods have shown promising performance for tool-wear prediction [14,
13], but reliable models require sufficiently diverse data. In realistic CNC envi-
ronments, such data are distributed across machines, production cells, factories,
ororganizations,whilecentralizationmaybecostlyorundesirablebecausesensor
recordings and images are large and may reveal production conditions, machin-
ing strategies, material properties, or process quality. Federated Learning (FL)
provides an alternative by enabling collaborative training while keeping raw op-
erational data local [5]. Previous studies have investigated FL for tool-wear pre-
diction. Kaleli et al. [6] combine feature extraction with a federated (Bi)LSTM
⋆ Corresponding author
arXiv:2608.11281v3  [cs.LG]  22 Sep 2026

2 A. Khan et al.
model on the PHM dataset [7], but do not establish whether federated training
improves over isolated local training. Huang and Lee [4] address client hetero-
geneity through a new aggregation method using the dataset of [8], but focus on
aggregation rather than distributed preprocessing; the original study applies nor-
malization to raw data [8], which may be difficult when data cannot be centrally
shared. De Melo Rosa et al. [2] demonstrate image-based federated tool-wear
prediction and improvements over per-client training, but acknowledge the lim-
ited generality of their small-scale evaluation. Thus, it remains unclear whether
FL can approach centralized performance while improving over local-only learn-
ing under distributed data-processing constraints. We investigate this question
using the Multimodal Automatic Tool Wear Inspection (MATWI) dataset [3].
We construct federated sensor- and image-based prediction pipelines in which
complete tool trajectories remain local to clients and compare federated training
against centralized and local-only baselines.
MATWI Dataset and Preprocessing
The MATWI dataset contains 17 cutting-tool sets, each representing the wear
progression of one milling insert. Each machining cycle includes wear labels,
synchronized force, accelerometer and acoustic recordings, and an image of the
cuttingedge.Weariscategorizedasflankwear,adhesivewear,orcombinedflank-
and-adhesive wear. Following [3], sets 1-13 are used; sets 14-17 are excluded due
to a workpiece-material domain shift. Tool sets remain intact when assigned to
clients. Sensor recordings contain air-cut intervals, where the tool moves without
engaging the workpiece, and active-cutting intervals; only the latter are retained.
A level-four discrete wavelet decomposition using the Daubechies 4 wavelet [9,
1] is applied independently to two sensor channels:
E[k] =|D 1[k]|, z[k] = E[k]−µ E σE + 10−9 ,
whereD 1[k]is the level-one detail coefficient at indexk,E[k]its magnitude,z[k]
the normalized activity score, andµE, σE the mean and standard deviation of
the first 1000E[k]values. Samples withz[k]>10are considered active and the
detected interval is expanded by 5%. For channel intervals[s1, e1]and[s 2, e2], the
retained interval is[max(s1, s2),min(e 1, e2)]. If fewer than 1000 active samples
are detected for a channel, the complete recording is retained.
Air-cut removal (Figure 1a) reduces the total sensor mean absolute error
(MAE) from26.24µm to16.40µm and flank wear MAE from26.02µm to
11.36µm (Figure 1b). Adhesion as well as combined flank wear & adhesion show
smaller improvements, likely because they contain fewer samples and adhesion
is less consistently reflected in process signals.
Federated Tool Wear Prediction
We formulate tool wear prediction as a horizontal federated learning problem in
which industrial data are generated and retained by separate data owners. Each

Federated Learning for Distributed CNC Tool Wear Prediction 3
(a) Example sensor recordings before and after air-cut removal.
(b)Effectofair-cutremovalonmodelper-
formance with sensor modality.
Fig.1: Air-cut removal and its effect on sensor-model performance.
client represents an autonomous industrial site that holds different samples but
shares the same feature space and prediction task. This matches the considered
tool wear setting, where different tools or sites contribute data for the same
prediction model while keeping their raw sensor recordings or images local.
Trainingfollowsasynchronousclient-serverprotocol.Atcommunicationround
t, the server broadcasts the current global model parametersθt to all participat-
ing clients. Each client initializes its local model withθt, performs local training
on its dataset, and returns the updated parametersθk t to the server. The server
aggregates the client models using FedAvg [11]:
θt+1 =
KX
k=1
nk
n θk t ,
whereKisthenumberofclients,n k isthenumberofsamplesheldbyclientk,
andn= PK k=1 nk. Thus, clients with more training samples have proportionally
greater influence on the global model.

4 A. Khan et al.
The same federated training protocol is applied to both sensor and image
data. The model architecture and local preprocessing differ by modality, while
client coordination, local training, communication, and server-side aggregation
remain unchanged.
Experimental Setup
Following the MATWI protocol [3], Sets 1, 2, 5, 7, 8, 10, and 11 are used for
training, Sets 3, 6, and 12 for validation, and Sets 4, 9, and 13 for testing. The
split is performed at tool set level so that cuts from the same physical tool do
not occur in multiple splits. The task is regression of the tool wear value for each
machining cycle, evaluated under centralized, local, and federated training.
For the sensor modality pipeline, each active cutting signal is divided into
overlapping windows of 2048 samples with a stride of 1024, following [15]. Each
window inherits the cut-level wear label, and window predictions are averaged
to obtain the cut-level prediction. The 1D-CNN additionally receives a four-
dimensional context vector containing the previous wear value and a one-hot
encoding of the three wear types. The image modality pipeline following the
MATWI dataset paper baseline uses ResNet50. Images are cropped using the
set-specific coordinates, resized to224×224using Lanczos resampling, and
normalized using ImageNet mean[0.485,0.456,0.406]and standard deviation
[0.229,0.224,0.225].
All models use Adam optimizer, Huber loss withδ= 1.0, early stopping with
patience 10, and 5 local epochs per federated round. The sensor model uses a
learning rate of10−4, batch size 32, and 100 federated rounds, while the image
model uses3×10 −4, batch size 16, and 30 rounds.
The training sets are distributed across three clients: Client A is assigned
Sets 1, 5, and 7; Client B Sets 2 and 10; and Client C Sets 8 and 11. Local
models are trained only on their assigned data, while federated training uses
the same partition with all three clients participating in every round. Federated
training is implemented in Flower 1.30.0 using FedAvg. Performance is reported
using mean absolute error (MAE) and the standard deviation of absolute errors
for each wear category.
Results and Discussion
Results on test Sets 4, 9, and 13 are reported as MAE in micrometers. Figure 2
shows comparable performance for centralized and federated models within each
modality. Flank wear follows the ideal trend more closely (dashed grey line),
whereas adhesion shows greater scatter due to fewer samples and weaker repre-
sentation in process signals whereas in images, adhesion is directly observable.
Table 1 reports MAE and standard deviation for all models.
For the sensor modality, federated training remains close to centralized train-
ing, with total MAEs of17.90µm and16.40µm, respectively, while outperform-
ing all three local models. Performance is similar for flank wear, while combined

Federated Learning for Distributed CNC Tool Wear Prediction 5
Table 1: Tool wear prediction performance as MAE±standard deviation (µm).
Total denotes MAE over all test samples across wear categories; the best result
for each wear type and modality is shown in bold.
Modality W ear Type Centralized F ederated Client A Client B Client C
Sensor Adhesion58.36±55.74 70.75±52.0556.26±63.4057.62±40.14 62.33±55.78
Flank Wear11.36±12.0412.50±12.58 13.67±13.39 27.56±27.84 16.63±20.84
Flank Wear + Adhesion23.66±18.3722.96±9.7030.27±19.03 49.45±25.64 62.52±26.32
T otal16.40±22.2417.90±22.32 19.21±23.95 33.28±30.21 27.58±32.02
Image Adhesion35.19±40.4326.73±44.2139.17±52.70 36.39±40.06 39.60±36.82
Flank Wear13.64±11.2014.05±13.98 28.15±21.73 31.43±23.79 40.65±20.41
Flank Wear & Adhesion31.08±21.4236.00±31.38 34.58±31.82 53.61±30.31 108.62±169.62
T otal18.06±18.4218.73±22.73 29.97±26.83 35.68±27.62 52.69±78.76
(a) Sensor: Centralized
 (b) Sensor: Federated
(c) Image: Centralized
 (d) Image: Federated
Fig.2:Centralizedandfederatedmodelperformanceforsensorandimagemodal-
ities. The dashed gray line denotes ideal prediction (ˆy=y).
wear is slightly better under federated training. For images, federated training
achieves18.73µm compared with18.06µm centrally and also outperforms all
local models. It performs similarly on flank wear and better on adhesion.
Adhesion is harder to infer from process signals because it may not produce
a clear or consistent signal pattern, whereas in images it is directly visible on
the cutting edge. Overall, federated learning approaches centralized performance
while improving over isolated training. Remaining differences likely reflect client
heterogeneity and the greater variability of the smaller adhesion and combined-
wear classes, while the two modalities provide complementary information across
wear types.

6 A. Khan et al.
References
1. Daubechies, I.: The wavelet transform, time-frequency localization and signal anal-
ysis. IEEE transactions on information theory36(5), 961–1005 (1990)
2. de Melo Rosa, G.L., Gwose, A., Ganser, P., Bergs, T.: Security-enhanced
cutting tool wear segmentation with federated learning. Procedia CIRP138,
415–420 (2026). https://doi.org/https://doi.org/10.1016/j.procir.2026.01.072,
https://www.sciencedirect.com/science/article/pii/S2212827126000727, 18th
CIRP Conference on Intelligent Computation in Manufacturing Engineering
3. De Pauw, L., Jacobs, T., Goedemé, T.: Matwi: A multimodal automatic tool wear
inspection dataset and baseline algorithms. In: International Conference on Com-
puter Vision Systems. pp. 255–269. Springer (2023)
4. Huang, G.Y., Lee, C.H.: Industrial federated learning algorithm (p-pfedsgd)
for tool wear estimation. Future Generation Computer Systems158, 150–
157 (2024). https://doi.org/https://doi.org/10.1016/j.future.2024.04.026,
https://www.sciencedirect.com/science/article/pii/S0167739X24001547
5. Kairouz, P., McMahan, H.B., Avent, B., Bellet, A., Bennis, M., Nitin Bhagoji,
A., Bonawitz, K., Charles, Z., Cormode, G., Cummings, R., D’Oliveira, R.G.L.,
Eichner, H., El Rouayheb, S., Evans, D., Gardner, J., Garrett, Z., Gascón, A.,
Ghazi, B., Gibbons, P.B., Gruteser, M., Harchaoui, Z., He, C., He, L., Huo, Z.,
Hutchinson, B., Hsu, J., Jaggi, M., Javidi, T., Joshi, G., Khodak, M., Konecný, J.,
Korolova,A.,Koushanfar,F.,Koyejo,S.,Lepoint,T.,Liu,Y.,Mittal,P.,Mohri,M.,
Nock, R., Özgür, A., Pagh, R., Qi, H., Ramage, D., Raskar, R., Raykova, M., Song,
D.,Song,W.,Stich,S.U.,Sun,Z.,Suresh,A.T.,Tramèr,F.,Vepakomma,P.,Wang,
J., Xiong, L., Xu, Z., Yang, Q., Yu, F.X., Yu, H., Zhao, S.: Advances and open
problems in federated learning. Found. Trends Mach. Learn.14(1–2), 1–210 (Jun
2021). https://doi.org/10.1561/2200000083, https://doi.org/10.1561/2200000083
6. Kaleli, I.S., Unal, P., Deveci, B.U., Albayrak, O., Ozbayoglu, A.M.: A domain-
aware federated learning study for cnc tool wear estimation. In: Younas, M., Awan,
I., Petcu, D., Feng, B. (eds.) Mobile Web and Intelligent Information Systems. pp.
250–265. Springer Nature Switzerland, Cham (2024)
7. Li, X.: 2010 phm society conference data challenge (2021).
https://doi.org/10.21227/jdxd-yy51, https://dx.doi.org/10.21227/jdxd-yy51
8. Lin, Y.R., Lee, C.H., Lu, M.C.: Robust tool wear monitoring sys-
tem development by sensors and feature fusion. Asian Journal of Con-
trol24(3), 1005–1021 (2022). https://doi.org/https://doi.org/10.1002/asjc.2741,
https://onlinelibrary.wiley.com/doi/abs/10.1002/asjc.2741
9. Mallat, S.G.: A theory for multiresolution signal decomposition: the wavelet repre-
sentation. IEEE transactions on pattern analysis and machine intelligence11(7),
674–693 (1989)
10. Mativenga, P., Schoop, J., Jawahir, I., Biermann, D., Kipp, M., Kilic, Z.M.,
Özel, T., Wertheim, R., Arrazola, P., Boing, D.: Engineered design of cutting
tool material, geometry, and coating for optimal performance and customized ap-
plications: A review. CIRP Journal of Manufacturing Science and Technology
52, 212–228 (2024). https://doi.org/https://doi.org/10.1016/j.cirpj.2024.06.001,
https://www.sciencedirect.com/science/article/pii/S1755581724000798
11. Mehta, S., Aneja, A.: Securing data privacy in machine learning: The fedavg of
federated learning approach. In: 2024 4th Asian Conference on Innovation in Tech-
nology (ASIANCON). pp. 1–5. IEEE (2024)

Federated Learning for Distributed CNC Tool Wear Prediction 7
12. Patel, D., Muthuswamy, S.: Tool wear state recognition in CNC milling using
reliable labels, robust domain features, and lightweight AI models. J. Intell. Manuf.
37(5), 2129–2164 (May 2026)
13. Shah, R., Pai, N., Thomas, G., Jha, S., Mittal, V., Shirvni, K., Liang, H.: Machine
learning in wear prediction. Journal of Tribology147(4), 040801 (11 2024)
14. Soori, M., Arezoo, B., Dastres, R.: Machine learning and artificial intelligence in
cnc machine tools, a review. Sustainable Manufacturing and Service Economics
2, 100009 (2023). https://doi.org/https://doi.org/10.1016/j.smse.2023.100009,
https://www.sciencedirect.com/science/article/pii/S2667344423000014
15. Yang, C., Zhou, J., Li, E., Wang, M., Jin, T.: Local-feature and global-dependency
based tool wear prediction using deep learning. Scientific Reports12(1), 14574
(2022)
