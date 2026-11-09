---
title: Application of sequence learning for predicting radiation damage of the CMS electromagnetic calorimeter
url: https://arxiv.org/abs/2610.04058
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Mario Ivan Gallegos Torres
- Leonid Serkin
- Guy Paic
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.04058
pages: 5
chars: 11860
fetched_at: '2026-11-08T13:24:58+00:00'
kb_version: 1
---

# Application of sequence learning for predicting radiation damage of the CMS electromagnetic calorimeter

Application of sequence learning for predicting radiation
damage of the CMS electromagnetic calorimeter
Mario IvanGallegos Torres 1,LeonidSerkin 1,∗ , andGuyPaic 2
1Facultad de Ciencias, Universidad Nacional Autónoma de México, Circuito Exterior s/n, Ciudad de
México 04510, México.
2Instituto de Ciencias Nucleares, Universidad Nacional Autónoma de México, Apartado Postal 70-543,
Ciudad de México 04510, México.
Abstract.In this paper we use machine learning methods to predict radiation
damage in the lead tungstate crystals of the CMS electromagnetic calorimeter at
the Large Hadron Collider. We analyze LHC Open Data collected from 2016 to
2018 and study the time evolution of the crystal optical transparency. We apply
deep neural network models to predict its behavior over different future time
intervals, and find that encoder-decoder sequence-to-sequence architectures can
effectively describe crystal aging.
1 Introduction
The Compact Muon Solenoid (CMS) experiment at CERN’s Large Hadron Collider (LHC)
is designed to detect and measure particles produced in proton collisions [1]. One of the
key components of the CMS detector is the electromagnetic calorimeter (ECAL), which is
composed of lead tungstate (PbWO4) crystals and is used to measure the energy of electrons
and photons generated in collisions at the LHC [2]. This detector played a key role in the
discovery of the Higgs boson in the two-photon decay channel in 2012 [3], as well as in the
precise measurement of the Higgs boson mass and in many other measurements [4].
The ECAL, shown schematically in Fig. 1a, consists of 75,848 lead tungstate crystals, each
approximately 22 cm long, with a cross-sectional area of 2×2 cm 2 and a weight of about
1 kg. These crystals, shown in Fig. 1b, are optically transparent and emit short pulses of light
when they absorb ionizing radiation. When a high-energy particle (an electron or photon)
enters a crystal, it collides with heavy nuclei, producing a cascade of secondary electrons and
photons. These electrons excite nearby atoms; as these return to their original energy level,
they emit blue light, which is detected by a photomultiplier. The amount of blue light emitted
is proportional to the amount of energy deposited in the crystal by the initial particle.
Due to the intense radiation during LHC operation, the optical transparency of the crystals
decreases progressively over time. This degradation phenomenon, known as “radiation dam-
age,” is associated with the creation of atomic-level defects in the crystals, which act as color
centers by absorbing the light that would otherwise propagate through the material [5].
The accuracy of electron and photon detection in the ECAL depends on the ability to measure
and correct changes in crystal transparency. For this purpose, the CMS experiment uses a
∗e-mail: lserkin@ciencias.unam.mx
arXiv:2610.04058v1  [physics.ins-det]  2 Oct 2026

(a)
 (b)
Figure 1: (a) Schematic of the ECAL system of the CMS experiment at the LHC. (b) PbWO4
crystals used in the CMS ECAL.
laser monitoring system that measures, every 40 minutes, changes in the optical properties of
the crystals caused by the radiation generated in collisions. Since predicting the behavior of
optical transparency is essential for the integrity of the experimental measurements and the
physical results derived from them, it is crucial to anticipate and correct the variations caused
by radiation damage [5].
2 Deep neural networks for predicting radiation damage
Deep Neural Networks (DNNs) are extremely powerful machine learning (ML) models that
achieve excellent performance on difficult problems such as speech recognition and visual
object recognition, and have been widely used in the High Energy Physics community [6].
Motivated by recent work by Joshiet al.[7], we analyze the temporal evolution of crystal
optical transparency and explore the application of DNN-based models to predict radiation
damage over different future time intervals.
The main focus of this paper is on encoder–decoder sequence-to-sequence (Seq2Seq) ar-
chitectures [8]. The Seq2Seq architecture used in this work consists of an encoder–decoder
structure based on stacked Long Short-Term Memory (LSTM) layers, as shown in Fig. 2. The
encoder processes the input sequence and compresses the temporal information into its final
hidden and cell states, capturing long-term dependencies. These states are used to initialize
the decoder, which generates the output sequence. Starting from the last observed value, the
decoder produces predictions iteratively through a dense layer, feeding each predicted value
back as input for the next time step until the desired prediction horizon is reached.
The Seq2Seq model employs two LSM layers with 512 units each in both the encoder and
decoder, and is trained for 400 epochs using teacher forcing, with “MinMaxScaler” normal-
ization. The minimization is performed using the Adam algorithm, and the software imple-
mentation is carried out in TensorFlow.
The publicly available LHC Open Data dataset hosted on the Zenodo platform [9] was used.
This dataset contains the laser response of PbWO 4 crystals collected during Run 2 of the
LHC (2016–2018). Each record includes detailed information on the crystal identification,
precise timestamps of the last calibration (transparency) value, as well as accurate data on the
integrated luminosity delivered since the previous measurement.

Figure 2: Seq2Seq architecture used in this work.
After cleaning and exploring the data, we select several representative ECAL crystals for
detailed study. The problem is formulated as a sequence forecasting task: given a sliding
window of past calibration values, we use a Seq2Seq model to predict future calibration
values for a given crystal. We train the model on the full 2016 dataset and evaluate it on
2017–2018 data, with the inputs normalized to unit variance.
The prediction accuracy is evaluated using the mean absolute error (MAE):
MAE= 1 n nX i=1

ytrue i −y pred i

 ; (1)
and the mean absolute percentage error (MAPE):
MAPE= 100 n nX i=1

 ytrue i −y pred i ytrue i

 .(2)
3 Seq2Seq prediction results
Fig. 3 presents a comparison between the true and predicted calibration for two ECAL crys-
tals, 30600 and 54000, as a function of time during the 2017 LHC data-taking period, using a
12-step prediction horizon. For reference, the lower panel shows the integrated luminosity. It
can be observed that during periods of collisions, the calibration values decrease due to radia-
tion damage, while during periods without collisions, the crystals recover their transparency.
The model achieves a MAE of 2.3×10 −3 and a MAPE of≈26% for crystal 30600, and an
MAE of 1.7×10 −3 with a MAPE of≈18% for crystal 54000, showing a good agreement
with the true calibration values in both cases.
In the following, a comparison is made for predictions on ECAL crystal 54000 using the
model from Ref. [7, 10]. Fig. 4a, taken from Ref. [7], shows a surprising dip in MAPE at
intermediate window sizes. We traced this behavior to a coding bug in the original author’s
implementation. Firstly, we reproduced their model shown as green curve in Fig. 4b. Af-
terwards, we obtained the corrected results, shown as blue line in Fig. 4b, noticing that the
difference between these curves highlights the impact of the bug on the reported performance
in Ref. [7].
Finally, the yellow curve in Fig. 4b corresponds to the predictions obtained with our Seq2Seq
model. Our independent implementation (with identical architecture) exhibits a different and
more stable behavior across window sizes, with MAPE varying smoothly with input length
and showing no anomalous dip. The best performance is achieved at short horizons (MAPE
∼9–15%), while intermediate window sizes maintain a stable error of∼20%. Although per-
formance degrades for very large windows, the model remains significantly more stable and
predictable than previous approaches, indicating improved generalization.

(a)
 (b)
Figure 3: Comparison between the true (blue line) and predicted (red line) calibration for
ECAL crystal (a) 30600 and (b) 54000 as a function of time, using a 12-step prediction
horizon. The lower panel displays the integrated daily luminosity.
(a)
 (b)
Figure 4: (a) Results reported by Joshiet al.[7], including the original 2017 Case 1 (green).
(b) Comparison of this result (green) with the corrected code implementation (blue), and
comparison with the Seq2Seq model (yellow) developed in this paper. All results are shown
for ECAL crystal 54000.

4 Conclusions
In this work, we presented a Seq2Seq LSTM model for forecasting the transparency of CMS
ECAL crystals. The model, based on an encoder–decoder architecture trained with teacher
forcing, is able to capture the temporal evolution of radiation damage and recovery effects
observed during LHC operation.
Our results show that the Seq2Seq architectures can model the long-term time evolution of
crystal aging and our Seq2Seq model provides good agreement with the measured calibration
values. In particular, the model performs best at short prediction horizons, reaching MAPE
values of∼9–15%, while maintaining stable performance of∼20% for intermediate window
sizes. In addition, we compare our results with previous work and find a coding bug in the
original implementation, which leads to anomalous behavior in the reported results.
Future work will focus on extending this approach to a larger set of crystals, including full
ECAL rings, and on exploring alternative deep learning models such as multi-output archi-
tectures. Since the response may vary from one crystal to another, a systematic study will
be needed to determine how well models trained on individual crystals generalize to crys-
tals with different aging and recovery patterns and to complete ECAL rings, as well as to
explore more advanced sequence-learning strategies. By relying on publicly available data
and reproducible methodologies, this work provides a solid basis for further developments in
data-driven calibration studies. These predictions can be useful for the CMS Collaboration
in improving calibration strategies and reducing the impact of radiation damage on detector
performance.
References
[1] CMS Collaboration,Performance of the CMS electromagnetic calorimeter in pp col-
lisions at 13 TeV. JINST19(2024) P09004. https://doi.org/10.1088/1748-0221/19/09/
P09004
[2] CMS Collaboration,CMS physics: Technical design report volume 1: Detector per-
formance and software, CERN-LHCC-2006-001, 2006. https://inspirehep.net/literature/
1614070
[3] CMS Collaboration,Observation of a new boson at a mass of 125 GeV with the CMS
experiment at the LHC. Phys. Lett.B716(2012) 30. https://doi.org/10.1016/j.physletb.
2012.08.021
[4] CMS Collaboration. Scientific Results. 2026. https://cms.cern/org/cms-scientific-results.
[5] CMS Collaboration,Energy calibration and resolution of the CMS electromagnetic
calorimeter in pp collisions at 7 TeV, JINST8(2013) P09009. https://doi.org/10.1088/
1748-0221/8/09/P09009
[6] K. Albertsson et al.,Machine Learning in High Energy Physics Community White Paper,
J. Phys. Conf. Ser. 1085 (2018) 2, 022008. https://doi.org/10.48550/arXiv.1807.02876
[7] B. Joshi, T. Li, B. Liang, R. Rusack, & J. Sun,Predicting the future of the CMS de-
tector: Crystal radiation damage and machine learning at the LHC. arXiv:2303.15291
[physics.ins-det] (2023). https://arxiv.org/abs/2303.15291
[8] I. Sutskever, O. Vinyals and Q. V . Le,Sequence to Sequence Learning with Neural Net-
works, arXiv:1409.3215 [cs.CL] (2014). https://arxiv.org/abs/1409.3215
[9] B. Joshi and R. Rusack,Laser Response in ECAL Crystals in CMS Detector. Zenodo,
2022. https://doi.org/10.5281/zenodo.7510572
[10] FAIR-UMN, fair_ecal_monitoring. https://github.com/FAIR-UMN/fair_ecal_
monitoring
