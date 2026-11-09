---
title: 'Functional Degeneracy in Neural Networks: Measurement and Pruning'
url: https://arxiv.org/abs/2608.30741
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Maria Matveev
- Pascal Esser
- Ayush Bharadwaj
- Lucius Bushnaq
- Gitta Kutyniok
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.30741
pages: 18
chars: 55965
fetched_at: '2026-11-08T13:27:58+00:00'
kb_version: 1
---

# Functional Degeneracy in Neural Networks: Measurement and Pruning

Functional Degeneracy in Neural Networks:
Measurement and Pruning
Maria Matveev1,2 Pascal Esser 1,2
Ayush Bharadwaj3 Lucius Bushnaq4 Gitta Kutyniok1,2,5,6
1Department of Mathematics, LMU Munich
2Munich Center for Machine Learning (MCML)
3Independent
4Goodfire AI
5Institute for Robotics and Mechatronics, DLR-German Aerospace Center
6Department of Physics and Technology, University of Tromsø
Abstract
A central question in modern machine learning is how much a trained model can
be compressed without changing its behavior, to reduce the memory, compute and
energy required to deploy it. To study this, we quantify functional degeneracy
through the behavioral recovery rank, defined as the number of leading behavioral-
Hessian eigendirections required to recover a trained model’s performance. Using
the behavioral recovery rank as a geometric benchmark for compression, we find
that structural and magnitude pruning retain more degrees of freedom, even after
the task is saturated. This gap suggests that functional redundancy is distributed
across parameter directions and is not exposed by individual weights or neurons.
1 Introduction
Trained neural networks exhibit substantial functional redundancy: many parameter directions can be
perturbed or removed with little effect on the function realized by the network [14, 26, 27, 16]. To
quantify the extent of this redundancy, we ask:
Q1: How many parameter directions are required to preserve the learned function?
A high degree of degeneracy indicates that the learned function is insensitive to many parameter
directions, placing the solution in a broad, approximately flat region associated with generalization
and stable optimization [ 13, 20, 24, 12, 31]. This redundancy also provides the basis for model
compression: if many parameters have little influence on the learned function, retaining only a
suitable subset may preserve its approximate performance while reducing the memory, compute,
and energy required for deployment [17, 11]. Although model sizes continue to grow, achievable
compression is still often measured post-hoc by applying a particular method [5]. It therefore becomes
increasingly important to assess the available redundancyas a property of the model, and to determine
how effectively existing compression methods exploit it. This motivates our second question:
Q2: How much of this redundancy do we actually exploit through pruning?
Contributions.To shed light on these questions, we make the following contributions:
(i)We introduce thebehavioral recovery rank, the number of leading behavioral Hessian eigendirec-
tions needed to recover a model’s performance to a given tolerance. This provides a theoretically
grounded way to measure approximate functional degeneracy of a model (Section 2, Appendix D–E).
(ii)We use controlled nonlinear teacher-student experiments, where task complexity is known, to
show that the behavioral recovery rank separatescapacity-limitedfromtask-saturated regimes. The
Preprint.
arXiv:2608.30741v1  [cs.LG]  31 Aug 2026

100 200 300
Leading eigendirections k
2
4
6
8
10
12
14
16
18
20Hidden width d
10 1
test MSE
(a) Test MSE for projecting on vary-
ing number of eigendirections.
2 6 10 14 18
Hidden width d
50
100
150
200rq or r
Absolute
= 0.05
= 0.075
= 0.1
Relative
q = 0.8
q = 0.85
q = 0.9
regression on
rq/r
teacher
d * = 10
(b) Behavioral recovery rank extracted from the pro-
jection curves, mean and std. over5runs.
6 10 14 18
Hidden width d
0
100
200
300degrees of freedom
rτ, τ = 0.075
eigenvalue
loss-optimal
Pruning
structure
magnitude
(c) Pruning and behavioral recov-
ery rank at a fixed loss threshold.
Figure 1: Task-saturated and capacity-limited regimes for non-linear teacher-student regression.
Trend-lines (piecewise regression) of both regimes are given in black.
behavioral recovery rank grows with student width and flattens once the student exceeds the teacher
width (Figure 1(a)–(b)). On MNIST, it grows sublinearly with width (Figure 2).
(iii)We find that structural and magnitude pruning do not exhibit such flattening, i.e. the parameters
they retain keep growing past the teacher’s width (Figure 1(c)). Under loss-optimal ordering of
directions, both pruning methods retain more parameters than the behavioral recovery rank.
Together, these findings suggest that functional redundancy beyond task saturation is not exposed by
weight- or neuron-level structure, and is therefore only partially accessible to standard pruning.
Related Work.Our questions are motivated by several works on degeneracies in neural network
parameterizations. Grigsby et al. [14] characterizeexactdegeneracies, and follow-up work formalizes
this perspective through functional dimension, given by the rank of the Jacobian of the realization
map on a finite-probe1 set [15]. However, we argue that, for understanding task performance, the
definition ofexact symmetry is too narrow: a parameter direction can have only a small effect on the
realized behavior of the model without beingexactlyredundant. This viewpoint is reinforced by the
works onintrinsic dimension, showing that many tasks can be solved in subspaces far smaller than
the parameter space [28, 1], and by analyses of theloss Hessian, whose spectrum typically shows a
large near-zero bulk alongside few outliers [35, 33, 36, 37, 32].
Pruningremoves weights or neurons from a trained network while preserving its function.Un-
structuredmethods rank individual weights by magnitude [ 16] or by a local quadratic model of the
loss [27].Structuredmethods remove whole neurons and therefore yield computational speed-ups,
ranking neurons by norm or by an estimated change in the loss [29, 30]. Both are typically combined
with retraining and evaluated by what fraction of the parameter count can be removed while still
meeting an accuracy threshold [5]. We expand on these works in Appendix B.
2 Methodology
Quantifying degeneracy: Behavioral recovery rank.We first equip the neighborhood of the
parameters at a checkpoint during training with a geometry that tracks changes in functional behavior,
and then quantify how many of the directions it identifies as behaviorally most relevant are needed to
retain a model’s performance.
Formally, for a model fθ parametrized by θ∈R p, following Bushnaq et al. [6], we consider the
behavioral loss2 for two sets of parameters ˜θandθ ∗
Lbeh(˜θ;θ ∗,P) = 1 2|P| X x∈P ∥f˜θ(x)−f θ∗ (x)∥2,(1)
where P={x i}n i=1 is a probe set, and ∥ · ∥denotes the ℓ2 norm. This loss equips the neighborhood of
θ∗ with a geometry tied directly to preservation of learned behavior: perturbations are small when the
predictions f˜θ(x), x∈ P, compared to the reference model’s predictionsfθ∗ (x) are nearly unchanged
1Withprobeset, we refer to a finite reference data set representing the data distribution, such as the training or validation
data sets (that are assumed to be drawn i.i.d. from the data distribution.)
2For notational simplicity we only consider the MSE as a loss; however, the setup directly generalizes to other loss
functions. For example, for a language-model we can consider KL divergence between predictive distributions.
2

on the probe set. This is in contrast to the empirical loss. Instead of comparing model predictions
to ground-truth labels, the behavioral loss compares predictions to those of a reference checkpoint
and can therefore be interpreted as a form of local self-distillation, with the checkpoint itself acting
as the teacher [19]. By construction, θ∗ is a global minimizer of Lbeh(˜θ;θ ∗,P) , so the first-order
term in its Taylor expansion around θ∗ vanishes. Consequently, the leading nontrivial local object is
the behavioral Hessian, Hbeh(θ∗) :=∇ 2 ˜θLbeh(˜θ;θ ∗,P)

˜θ=θ∗ , whose structure we discuss further in
Appendix E. A second-order Taylor expansion yieldsLbeh(θ∗+δ;θ ∗,P) = 1 2 δ⊤Hbeh(θ∗)δ+o(∥δ∥ 2) for δ∈R p. Thus, the leading eigenvectors of Hbeh(θ∗) identify perturbation directions that induce
the largest changes in model behavior on the probe set. Formally, let Π(beh) k denote the projection onto the top- k eigenspace of Hbeh(θ∗). Given a reference point θref, we reconstruct the learned
displacement with respect toθ ref by
ˆθk =θ ref + Π(beh) k (θ∗ −θ ref ),(2)
where we consider the initialization θ0 or 0 as the reference point θref. We define thebehavioral
recovery rankas the smallest number of leading eigendirections k such that the projected checkpoint
fˆθk recovers a given performance level.3 For a “lower-is-better” metric M, such as the empirical
training/test loss, with toleranceτ >0,q∈(0,1]andM ≤k = minj≤k M(ˆθj), we define:
Relative:ˆrq = min k∈[p]

k: M(θref )− M≤k
M(θref )− M(θ∗) ≥q

,Threshold:r τ = min k∈[p]

k:M( ˆθk)≤τ 	 .
Intuitively, a small behavioral recovery rank means that the trained model’s behavior can be recovered
from a low-dimensional part of the trained solution; if this rank grows much more slowly than
parameter count, additional parameters mainly enlarge the degeneracy.
In our main experiments, we use the train set as the probe set to compute the behavioral loss in
Eq. (1) at a trained model checkpoint θ∗. We ablate this choice in Appendix G. We estimate the top-k
eigenspaces of the Hessian using matrix-free Lanczos iteration; see Appendix C.2 for details.
Pruning baselines.We apply two one-shot gradient-free baselines to the same checkpoints.Mag-
nitude pruningremoves the globally smallest weights [ 16];structural pruningremoves neurons
greedily with respect to M. For each we report the smallest number of retained parameters for
which the model performance M stays within tolerance threshold τ, counting for structural pruning
all parameters attached to surviving neurons. This way, both quantities count degrees of freedom
retained to meet the tolerance τ, in the coordinate basis for pruning and in the behavioral-Hessian
eigenbasis for rτ . We chose two baselines of varying removal granularity, and for comparability with
the projection experiments, we do not retrain. We additionally report arefittedvariant and apply the
same pipeline to the teacher itself in Appendix F.
Model and data.We study degeneracy in two settings of varying difficulty. Firstly, in nonlinear
teacher-student regression, we fix a teacher model and vary student width from under- to over-
complete, which allows for a systematic control of the network capacity relative to the data complexity.
Secondly, we complement these experiments with width-scaled MLPs on a standard classification
task (MNIST [9]). For all experiments, we train with Adam without weight decay [25] for a fixed
number of steps. We provide details on both setups in Appendix C.1.
3 Results and Discussion
Equipped with this methodology, we can now work towards answering our two introductory questions.
Q1: The task-saturated and capacity-limited regimes.The teacher-student setting allows us
to observe the transition between two regimes directly, because task complexity is fixed by the
teacher width, giving us a priori control over model capacity relative to the task. While the student is
capacity-limited(narrower than the teacher), added parameters improve performance gradually as a
large fraction of the available directions contributes to the learned behavior as shown in Figure 1(b).
As the student matches or exceeds the teacher width, the task becomessaturated: the recovery curves
in Figure 1(a) become increasingly steep, only a limited number of leading directions is needed
to approach the final performance, and additional directions yield diminishing improvements. The
3We provide an extended definition in Appendix D. We only defineˆrq ifM(θ ref )>M(θ ∗).
3

0 5000 10000
Leading eigendirections k
0.0
0.2
0.4
0.6
0.8
1.0T est accuracy
Widths
32
64
96
128
160
(a) Test accuracy under projection,
compared to final accuracy (dotted).
32 64 96 128 160
Hidden width w
2000
4000
6000
8000rq or r
Absolute
= 0.85
= 0.90
= 0.92
Relative
q = 0.90
q = 0.95
(b) Leading eigendirections k required to reach an
accuracy thresholdτ, for different widths.
32 64 96 128 160
Hidden width w
0
10000
20000
30000
40000degrees of freedom
rτ, τ = 0.9
eigenvalue
loss-optimal
Pruning
structure
magnitude
(c) Comparison of behavioral recov-
ery rank to two pruning baselines.
Figure 2: On MNIST, wider models need more directions to recover performance, indicating addi-
tional behaviorally relevant directions, but sublinear growth relative to width.
piecewise regression in Figure 1(b) reveals that the growth of the behavioral recovery rank for these
threshold levels slows from 11 to 1.3 directions per added neuron ( 21 parameters). Absolute and
relative recovery criteria exhibit the same qualitative transition.
For MNIST, the task complexity is unknown, and the operating regime must therefore be inferred
from the scaling of the rank. Figure 2(a)–(b) shows that wider models achieve higher accuracy
and require more leading eigendirections to recover their performance. The recovery rank grows
sublinearly with width under both absolute and relative criteria. Thus, the investigated models remain
capacity-limited in the sense that width introduces additional behaviorally relevant directions, but
these directions grow substantially more slowly than the number of parameters.
Q2: Redundancy accessible to pruning.We now use the behavioral recovery rank as a geometric
benchmark for assessing how much of the identified redundancy is exploited by pruning. Figure 1(c)
compares the behavioral recovery rank with structural and magnitude pruning at a fixed performance
threshold. Once the student width reaches the teacher width, the behavioral recovery rank slows
markedly, whereas the number of parameters retained by both pruning methods continues to grow.
Hence, the additional redundancy arising beyond task saturation is not effectively exposed by these
one-shot pruning criteria, which therefore underestimate the degeneracy present in this regime.
The red curve in Figure 1(c) reports the same projection experiment but orders directions by
λj⟨vj, θ∗ −θ ref⟩2 rather than by λj alone. Under the quadratic model, this ordering minimizes
the behavioral loss for a fixed budget of k directions on the probe set. It approximately halves
the recovery rank, indicating even greater degeneracy than the eigenvalue ordering reveals, and
both pruning baselines retain more degrees of freedom at every width. Since individual behavioral
eigendirections can mix parameters across all hidden units, whereas structural and magnitude pruning
remove units or weights in the original parameterization, the observed gap suggests that the redundant
directions are not aligned with these architectural coordinates. The ordering persists on MNIST,
where the recovery rank keeps growing because these models remain capacity-limited (Figure 2(c)).
Discussion.The behavioral recovery rank provides a task-dependent distinction between nominal
model size and the effective number of parameter directions needed to preserve learned behavior.
Pruning operates locally, on the individual weights and units that the architecture provides, whereas
each behavioral eigendirection combines all parameters. Although low-dimensional, this eigenbasis
representation is not directly feasible for compression, since each basis element is as large as the
dense model. The behavioral recovery rank bounds instead what a function-adapted basis could
remove. Consistent with this, closed-form output refitting recovers much of the gap (Appendix F).
Whether such a basis is also inexpensive to describe, for instance via structured families such as
layerwise or blockwise transforms, and how to utilize it for compression remain open.
Because the behavioral recovery rank flattens while the parameter count and the free parameters
retained by pruning continue to grow, compression measured only relative to the original parameter
count may understate the redundancy that remains once task complexity is saturated. This opens an
avenue towards predictive theory, since degeneracy fixed by the task could be measured on a small
model and used to bound what compression can achieve on larger ones.
Limitations and future work.Our experiments are restricted to two small settings in which repeated
behavioral-Hessian eigensolves remain tractable. Making the rank operational will require additional
work, such as blockwise restriction or subsampling of the probe set. Establishing whether the
4

identified regimes persist at scale will further require broader architectures and datasets, together with
ablations over the probe set, reference point and parametrization that separate genuine capacity effects
from width-dependent optimization and regularization. We compare against two one-shot pruning
baselines, which may understate the compression a full pipeline with retraining or quantization
could achieve. Finally, a theoretical characterization of the behavioral recovery rank could clarify
under which conditions these width-scaling regimes persist, support compression or generalization
guarantees, and connect the observed transitions to phenomena such as double descent [4].
Acknowledgments
MM, PE and GK acknowledge the support by the Munich Center for Machine Learning (MCML).
MM and GK are supported by the DAAD programme Konrad Zuse Schools of Excellence in Artificial
Intelligence, sponsored by the German Federal Ministry of Research, Technology and Space.
References
[1] Armen Aghajanyan, Sonal Gupta, and Luke Zettlemoyer. Intrinsic dimensionality explains
the effectiveness of language model fine-tuning. In Chengqing Zong, Fei Xia, Wenjie Li,
and Roberto Navigli, editors,Proceedings of the 59th Annual Meeting of the Association for
Computational Linguistics and the 11th International Joint Conference on Natural Language
Processing (Volume 1: Long Papers), pages 7319–7328, Online, August 2021. Association for
Computational Linguistics.
[2] Shun-ichi Amari and Hiroshi Nagaoka.Methods of Information Geometry. Translations of
Mathematical Monographs. American Mathematical Society, 2000.
[3] Yasaman Bahri, Ethan Dyer, Jared Kaplan, Jaehoon Lee, and Utkarsh Sharma. Explaining
neural scaling laws.Proceedings of the National Academy of Sciences, 2024.
[4] Mikhail Belkin, Daniel Hsu, Siyuan Ma, and Soumik Mandal. Reconciling modern machine-
learning practice and the classical bias–variance trade-off.Proceedings of the National Academy
of Sciences, 2019.
[5] Davis Blalock, Jose Javier Gonzalez Ortiz, Jonathan Frankle, and John Guttag. What is the state
of neural network pruning? In I. Dhillon, D. Papailiopoulos, and V . Sze, editors,Proceedings of
Machine Learning and Systems, volume 2, pages 129–146, 2020.
[6] Lucius Bushnaq, Jake Mendel, Stefan Heimersheim, Dan Braun, Nicholas Goldowsky-Dill,
Kaarel Hänni, Cindy Wu, and Marius Hobbhahn. Using degeneracy in the loss landscape for
mechanistic interpretability, 2024.
[7] Lawrence Cayton. Algorithms for manifold learning. Technical Report CS2008-0923, University
of California, San Diego, 2005.
[8] Jeremy Cohen, Simran Kaur, Yuanzhi Li, J Zico Kolter, and Ameet Talwalkar. Gradient descent
on neural networks typically occurs at the edge of stability. InInternational Conference on
Learning Representations, 2021.
[9] Li Deng. The mnist database of handwritten digit images for machine learning research.IEEE
Signal Processing Magazine, 2012.
[10] Zhou Fan and Zhichao Wang. Spectra of the conjugate kernel and neural tangent kernel for
linear-width neural networks.Advances in neural information processing systems, 2020.
[11] Jonathan Frankle and Michael Carbin. The lottery ticket hypothesis: Finding sparse, trainable
neural networks. InInternational Conference on Learning Representations, 2019.
[12] Timur Garipov, Pavel Izmailov, Dmitrii Podoprikhin, Dmitry Vetrov, and Andrew G Wilson.
Loss surfaces, mode connectivity, and fast ensembling of dnns. In S. Bengio, H. Wallach,
H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett, editors,Advances in Neural
Information Processing Systems, volume 31. Curran Associates, Inc., 2018.
5

[13] Ian Goodfellow, Yoshua Bengio, and Aaron Courville.Deep Learning. MIT Press, 2016.
[14] J. Elisenda Grigsby, Kathryn Lindsey, and David Rolnick. Hidden symmetries of ReLU net-
works. InProceedings of the 40th International Conference on Machine Learning, Proceedings
of Machine Learning Research, 2023.
[15] J. Elisenda Grigsby, Kathryn Lindsey, Robert Meyerhoff, and Chenxi Wu. Functional dimension
of feedforward ReLU neural networks.Advances in Mathematics, 2025.
[16] Song Han, Jeff Pool, John Tran, and William J. Dally. Learning both weights and connections
for efficient neural network. In C. Cortes, N. Lawrence, D. Lee, M. Sugiyama, and R. Garnett,
editors,Advances in Neural Information Processing Systems, volume 28. Curran Associates,
Inc., 2015.
[17] Song Han, Huizi Mao, and William J. Dally. Deep compression: Compressing deep neural
network with pruning, trained quantization and huffman coding. InInternational Conference
on Learning Representations, 2016.
[18] Babak Hassibi, David Stork, and Gregory Wolff. Optimal brain surgeon: Extensions and
performance comparisons. In J. Cowan, G. Tesauro, and J. Alspector, editors,Advances in
Neural Information Processing Systems, volume 6. Morgan-Kaufmann, 1993.
[19] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network.
arXiv preprint arXiv:1503.02531, 2015.
[20] Sepp Hochreiter and Jürgen Schmidhuber. Flat minima.Neural Computation, 1997.
[21] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza
Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Thomas
Hennigan, Eric Noland, Katherine Millican, George van den Driessche, Bogdan Damoc, Aurelia
Guy, Simon Osindero, Karén Simonyan, Erich Elsen, Oriol Vinyals, Jack Rae, and Laurent
Sifre. An empirical analysis of compute-optimal large language model training. InAdvances in
Neural Information Processing Systems, 2022.
[22] Arthur Jacot, Franck Gabriel, and Clément Hongler. Neural tangent kernel: Convergence and
generalization in neural networks.Advances in neural information processing systems, 2018.
[23] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child,
Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language
models. 2020.
[24] Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy, and Ping
Tak Peter Tang. On large-batch training for deep learning: Generalization gap and sharp minima.
InInternational Conference on Learning Representations, 2017.
[25] Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization. InInterna-
tional Conference on Learning Representations, 2015.
[26] Edmund Lau, Zach Furman, George Wang, Daniel Murfet, and Susan Wei. The local learning
coefficient: A singularity-aware complexity measure. InThe 28th International Conference on
Artificial Intelligence and Statistics, 2025.
[27] Yann LeCun, John Denker, and Sara Solla. Optimal brain damage. In D. Touretzky, editor,
Advances in Neural Information Processing Systems, volume 2. Morgan-Kaufmann, 1989.
[28] Chunyuan Li, Heerad Farkhoor, Rosanne Liu, and Jason Yosinski. Measuring the intrinsic
dimension of objective landscapes. InInternational Conference on Learning Representations,
2018.
[29] Hao Li, Asim Kadav, Igor Durdanovic, Hanan Samet, and Hans Peter Graf. Pruning filters for
efficient convnets. InInternational Conference on Learning Representations, 2017.
[30] Pavlo Molchanov, Arun Mallya, Stephen Tyree, Iuri Frosio, and Jan Kautz. Importance
estimation for neural network pruning. In2019 IEEE/CVF Conference on Computer Vision and
Pattern Recognition (CVPR), pages 11256–11264, 2019. doi: 10.1109/CVPR.2019.01152.
6

[31] Behnam Neyshabur, Srinadh Bhojanapalli, David McAllester, and Nati Srebro. Exploring
generalization in deep learning. In I. Guyon, U. V on Luxburg, S. Bengio, H. Wallach, R. Fergus,
S. Vishwanathan, and R. Garnett, editors,Advances in Neural Information Processing Systems,
volume 30. Curran Associates, Inc., 2017.
[32] Lorenzo Noci, Alexandru Meterez, Thomas Hofmann, and Antonio Orvieto. Super consistency
of neural network landscapes and learning rate transfer. InAdvances in Neural Information
Processing Systems, 2024.
[33] Vardan Papyan. The full spectrum of deepnet hessians at scale: Dynamics with SGD training
and sample size.arXiv preprint arXiv:1811.07062, 2018.
[34] Yousef Saad.Numerical Methods for Large Eigenvalue Problems. Society for Industrial and
Applied Mathematics, 2011.
[35] Levent Sagun, Utku Evci, V . Ugur Guney, Yann Dauphin, and Leon Bottou. Empirical analysis
of the hessian of over-parametrized neural networks, 2018.
[36] Sidak Pal Singh and Thomas Hofmann. Closed form of the hessian spectrum for some neural
networks. InHigh-dimensional Learning Dynamics 2024: The Emergence of Structure and
Reasoning, 2024.
[37] Sidak Pal Singh, Gregor Bachmann, and Thomas Hofmann. Analytic insights into structure and
rank of neural network hessian maps. In M. Ranzato, A. Beygelzimer, Y . Dauphin, P.S. Liang,
and J. Wortman Vaughan, editors,Advances in Neural Information Processing Systems, 2021.
[38] Sumio Watanabe.Algebraic Geometry and Statistical Learning Theory. Cambridge University
Press, 2009.
[39] Nick Whiteley, Annie Gray, and Patrick Rubin-Delanchy. Statistical exploration of the manifold
hypothesis.Journal of the Royal Statistical Society Series B: Statistical Methodology, 2026.
7

A Ethical Considerations
A.1 Impact statement
This paper presents work whose goal is to advance the field of Machine Learning. There are many
potential societal consequences of our work, none of which we feel must be specifically highlighted
here.
A.2 Disclosure of AI use
We utilized AI tools for support with coding, editing, and ideation. All AI-generated suggestions were
critically reviewed and refined by the authors, and we take full responsibility for the work presented.
B Extended Related Work Discussion
In the following, we discuss the related work directions outlined in the introduction in more detail.
Scaling lawsdescribe how model loss varies with model size, data, and compute [23]. Hoffmann et al.
[21] show that model size and token count should be scaled together, and Bahri et al. [3] emphasize
that different regimes can exhibit different exponents. This motivates studying how the behavioral
recovery rank varies with the hidden size of the model.
Singular learning theorystudies model complexity through the local singular structure around a
solution [38]. The local learning coefficient (LLC) quantifies how the volume of a low-loss region
shrinks as one zooms in around a local minimum [26]. Following this local perspective, we adopt the
behavioral lossintroduced by Bushnaq et al. [6]. In their framework, the LLC of the behavioral loss
defines an effective parameter count, and the rank of its Hessian gives a tractable lower bound on the
corresponding local dimension. They further connect this functional degeneracy to concrete network
properties, such as linear dependence in both the activations and the backpropagated gradients, and
use the so-called interaction basis to interpret the model independent of parameterization.
Hessian analysis.Training is often studied through theHessian of the training or validation loss.
A recurring phenomenon, observed empirically and analyzed in simplified settings, is that the loss
Hessian possesses a spectrum with a large near-zero bulk together with a small set of outliers
[35, 33, 36]. Analytic work further shows that such rank deficiency can follow from architectural
structure itself such as width, depth, and bias configuration [ 37]. More recently, Noci et al. [32]
show that under µP parametrization, certain spectral properties of the loss Hessian remain largely
stable across model sizes, a phenomenon they callsuper consistency. Works on the Edge-of-stability
further connect the loss-curvature to optimization dynamics via the learning rate [8]. Together, these
results suggest that increasing parameter count need not create proportionally many new relevant
loss curvaturedirections. By contrast, our behavioral construction replaces supervised targets by the
outputs of a fixed trained checkpoint on a probe set, instead of the curvature induced by the labels.
This can be viewed as local self-distillation with the checkpoint itself as the teacher [19]. We discuss
the connection of both second-order objects in Appendix E.2.
Intrinsic dimension.The works onintrinsic dimensionsuggest that once a model family is suf-
ficiently large, the actual dimensionality required to solve a task remains relatively stable [ 28].
Aghajanyan et al. [1] report similarly low intrinsic dimensionality in language-model fine-tuning.
Intrinsic dimension is defined through training in random low-dimensional subspaces, whereas our
statistic is computed after training in a Hessian-aligned subspace around a fixed checkpoint. Still,
these results provide a clear prior for our setting: the dimension relevant to the learned solution may
grow substantially more slowly than the total number of parameters. This is also echoed by the
manifold hypothesis, which posits that high-dimensional data concentrate near lower-dimensional
structure [7, 39].
Functional dimensionmeasures the local dimension of the realized function class and can be
computed on finite batches via the rank of the evaluation-map Jacobian [ 15]. Grigsby et al. [14]
show that exact degeneracies of ReLU networks can depend on architectural parameters. The same
finite-probe Jacobian also appears in the empiricalNeural Tangent Kerneltheory [ 22], its spectrum
was analyzed in [10]. However, we use this object post hoc around trained checkpoints, rather than to
analyze training dynamics near initialization. We discuss these connections in Appendix E.
8

Pruning.Pruning asks which parameters can be removed from a trained network while preserving
its function. The classical saliency methods estimate the effect of removing a weight through a local
quadratic model of the loss, either under a diagonal approximation of the Hessian [27] or using its
inverse to additionally compensate the remaining weights [ 18]. Magnitude pruning replaces this
by the far cheaper proxy of weight size [ 16], which remains competitive at scale and forms the
first stage of standard compression pipelines [ 17]. Unstructured sparsity does not translate into
speedups on dense hardware without specialized kernel support.Structuredpruning methods remove
neurons, directly impacting the weight matrix size involved in the computation, by ranking them
by norm [29] or by a first-order estimate of the induced change in the loss [30]. These methods are
typically combined with retraining [16] and evaluated by what fraction of the parameter count can be
removed while still meeting an accuracy threshold [5]. In either case the criterion is expressed in the
coordinate basis of the parameterization, whereas the behavioral recovery rank counts directions in
the eigenbasis of the behavioral Hessian, which need not align with any weight or unit. To compare
with the projection experiments, we do not retrain and use a greedy pruning approach, as described in
Section 2.
C Experimental details
This section provides the detailed experimental configuration used throughout the paper, including
datasets, model architectures, training procedures, and implementation specifics. We describe both the
synthetic teacher-student regression setup and the MNIST classification experiments in Section C.1,
together with the optimization settings and computational methods used to analyze the resulting
models in Section C.2.
C.1 Data, models, training
In this section, we introduce the datasets and experimental setups. We describe the data generation
process for the synthetic regression experiments in Section C.1.1 as well as the preprocessing and
training configuration for MNIST classification in Section C.1.2.
C.1.1 Nonlinear teacher-student regression
In order to systematically control model capacity, we utilize a synthetic teacher-student regression
setup with two-layer ReLU MLPs.
For this, we sample the inputs according to
x∼ N(0, Idin ).
The teacher networkf T generates regression targetsy=f T (x) +εwithε∼ N(0, σ2I).
Both teacher and student are two-layer ReLU networks, with bias terms. For the experiments
in the main paper, the teacher has architecture 10→10→10 and the student has architecture
10→d→10, and the data is noise-less. These choices are ablated in Appendix G.
For each width d∈ {2, . . . ,20}, we draw 2048 training examples and 512 test examples. Students
are trained with full-batch Adam for 4000 optimization steps using learning rate 10−3 and β1 =
0.9, β2 = 0.999, ε= 1e−8 and no weight decay. The task loss is mean-squared error to the teacher
outputs. For the projection experiments, we use the reference point θref = 0. We ablate this choice in
Figure 4.
C.1.2 MNIST
For the classification experiment, we train width-scaled MLPs on MNIST. Images are flattened to
vectors in R784, normalized using the empirical mean and standard deviation of the selected training
subset.
The model is a two-hidden-layer ReLU MLP
784→h 1 →h 2 →10.
In width-scaled runs, we seth 1 =h 2 =wand sweep
w∈ {32, 64, 96, 128, 160}.
9

We train with Adam for2000 optimization steps using learning rate 10−3, β1 = 0.9, β2 = 0.999, ε=
1e−8 , mini-batch size 64, no weight decay and cross-entropy loss. For the projection experiments,
we use the initialization as reference pointθ ref =θ 0 and a probe size of10000.
C.2 Implementation
All experiments are implemented in PyTorch and were run on NVIDIA RTX 2080 Ti, TITAN RTX
or RTX A6000. In total, the reported MNIST experiments required approximately 150 GPU-hours of
compute; we note that this is an estimate given the heterogeneous compute environment.
Since explicitly forming the behavioral Hessian is computationally expensive, we instead access it
through matrix-free eigensolves. For this, we work with the equivalent dual operator |P| −1JP J ⊤ P in
probe-output space (see Appendix E), implemented via Jacobian-vector and vector-Jacobian products.
We estimate the leading eigenspaces using symmetric Lanczos iteration with full orthogonaliza-
tion [34]. The number of Lanczos steps is chosen as min(D,max(4k,60)) for a target of k leading
eigenpairs, where D=|P|m is the dimension of the operator. Eigenpairs are retained by the scale-
invariant criterion λj >10 −6λ1, since an absolute cutoff would depend on the output scale, which
varies across widths. Parameter-space eigenvectors are recovered lazily as vj =J ⊤ P uj/∥J ⊤ P uj∥ and
re-orthonormalized by modified Gram-Schmidt before being accumulated.
D Variants of the behavioral recovery rank
Higher-is-better metrics.Recall that
Relative:ˆr q = min k∈[p]

k: M(θref )− M≤k
M(θref )− M(θ∗) ≥q

,M ≤k = min j≤k M(ˆθj).(3)
Threshold:r τ = min k∈[p]

k:M( ˆθk)≤τ 	 .(4)
Then equations (3) and (4) give the forms used for the teacher-student experiments, where M is a
loss. For a “higher-is-better” metricM, such as the accuracy used in the MNIST experiments, with
q∈(0,1]andτ >0, the corresponding definitions are
Relative:ˆrq = min k∈[p]

k:M( ˆθk)≥qM(θ ∗) 	 or Threshold:r τ = min k∈[p]  k:M( ˆθk)≥τ 	 .
The MNIST experiments use accuracy, since it is a classification task.
Ordering the directionsThroughout the main paper ˆrq and rτ project onto the top-k eigendirections
ordered by decreasing eigenvalueλ j.
We will derive a different version, which lower bounds it. For this, let {vj} be the orthonormal
eigenvectors of Hbeh(θ∗) with eigenvalues λj, and expand the learned displacement θ∗ −θ ref in this
basis. Retaining an index setSgives the reconstruction
ˆθS =θ ref + X
j∈S
⟨vj, θ∗ −θ ref ⟩v j,
so the unrecovered component of the displacement is
ˆθS −θ ∗ =− X
j /∈S
⟨vj, θ∗ −θ ref ⟩v j,
ˆθS −θ ∗ 2 = X
j /∈S
⟨vj, θ∗ −θ ref ⟩2.
Evaluating the second-order model of the behavioral loss at ˆθS and using orthonormality of the
eigenbasis gives the exact identity
1
2
ˆθS −θ ∗ ⊤ Hbeh(θ∗) ˆθS −θ ∗  = 1 2 X j /∈S λj⟨vj, θ∗ −θ ref ⟩2,(5)
and Lbeh(ˆθS;θ ∗,P) agrees with (5) up to o(∥ˆθS −θ∗∥2). It is minimized when the eigendirections are
ordered decreasing according to the corresponding λj⟨vj, θ∗ −θ ref ⟩2. We define the corresponding
statistic as theloss-optimal behavioral recovery rankr opt τ ≤r τ .
10

For two reasons, the eigenvalue ordering is our main definition. First, {λj, vj} depend only on
Hbeh(θ∗), and hence on the model and the probe distribution, whereas λj⟨vj, θ∗ −θ ref⟩ depends in
addition on θref, i.e. on where the optimizer landed. As a result, the loss-optimal rank mixes local
geometry with the training trajectory. Second, the loss-optimal can only be applied within the whole
eigenspace that has actually been computed, with the other definition only requiring the top of the
spectrum.
E Behavioral Hessian geometry
This appendix develops the geometric interpretation of the behavioral Hessian introduced in Section
2 and relates it to several established objects in optimization and representation theory. The sections
are tied together through a common geometric object: the Jacobian of the finite-probe evaluation
map, JP (θ∗). Each section studies how different notions of local model geometry arise from this
same Jacobian, but viewed from different perspectives and in different spaces.
• In Section E.1, the Jacobian defines the behavioral Hessian as the parameter-space Gram
matrix J ⊤ P JP, which characterizes the local sensitivity of model outputs to parameter
perturbations.
• Section E.2 shows that the same structure appears within the generalized Gauss–Newton
component of the task-loss Hessian, thereby connecting behavioral geometry to standard
optimization curvature.
• In Section E.3, the rank and kernel of the Jacobian are related to functional dimension,
linking flat parameter directions to infinitesimal function-preserving transformations.
• Section E.4 then considers the dual object JP J ⊤ P , namely the empirical NTK, which acts in
function space rather than parameter space while sharing the same nonzero spectrum.
• Finally, Section E.5 interprets the same Gram structure statistically as an empirical Fisher
information matrix, providing an information-geometric interpretation in terms of local
identifiability and informative directions.
Taken together, the appendix shows that behavioral curvature, optimization curvature, functional
degeneracy, NTKs, and Fisher information can all be understood as different manifestations of the
same local Jacobian geometry induced by the probe evaluation map.
E.1 Behavioral Hessian geometry
In this section, we discuss the behavioral Hessian introduced in Section 2. Throughout this appendix,
let θ∗ ∈R p be a trained checkpoint, m= dim(f θ(x)) the output dimension, and let P be a finite
probe set. We define the finite-probe evaluation map
FP (θ) =

fθ(x)

x∈P ∈R |P|m ,
wheremis the output dimension and we stack all outputs. Let
JP (θ) = ∂FP (θ) ∂θ
denote its Jacobian. We can now write the behavioral loss in vector notation as
Lbeh(θ;θ ∗,P) = 1 2|P| ∥FP (θ)−F P (θ∗)∥2 2 .
Differentiating once gives
∇θLbeh(θ;θ ∗,P) = 1 |P| JP (θ)⊤ (FP (θ)−F P (θ∗)).
Differentiating again yields
∇2 θLbeh(θ;θ ∗,P) = 1 |P| JP (θ)⊤JP (θ) + 1 |P|
|P|mX
i=1
(FP (θ)−F P (θ∗))i ∇2 θ  FP (θ)  i.
11

At θ=θ ∗, the residual is zero. Therefore the second term vanishes, and the behavioral Hessian is the
Jacobian Gram matrix
Hbeh(θ∗;P) =∇ 2 θLbeh(θ∗;θ ∗,P) = 1 |P| JP (θ∗)⊤JP (θ∗).(6)
We also highlight that by Equation (6),
rank

Hbeh(θ∗;P)

= rank

JP (θ∗)

≤min{p,|P|m}.
Thus the behavioral Hessian is necessarily rank-limited by both parameter dimension and probe-output
dimension. In particular, if|P|m < p, then its nullspace has dimension at leastp− |P|m.
E.2 Connection to the task loss Hessian
Let X={x i}N i=1 denote the training data,{yi}N i=1 corresponding outputs and consider the supervised
task loss
Ltask(θ) = 1 N
NX
i=1
ℓ(fθ(xi), yi).
Define the corresponding stacked evaluation map FX (θ) =

fθ(xi)
N
i=1 ∈R N mwith JX (θ) =
∂FX (θ)
∂θ its Jacobian.
The Hessian of the task loss at θ∗ decomposes into a generalized Gauss-Newton term and a curvature-
residual term:
∇2 θLtask(θ∗) =H GN(θ∗) +R curv(θ∗)
with
HGN(θ∗) =J X (θ∗)⊤
 1
N blockdiagN i=1

∇2 1ℓ(a, yi)

 a=fθ∗ (xi)  JX (θ∗),
where the Hessian ∇2 1ℓ is taken with respect to the first component, the model output fθ(xi). The
remaining term is
Rcurv(θ∗) = 1 N
NX
i=1
mX
j=1
∂ℓ
∂fj

fθ∗ (xi), yi

∇2 θfθ,j (xi)

 θ=θ∗ .
If the probe set is chosen as the training set, P=X , and ℓ is the MSE-loss, the behavioral Hessian
becomes the Gauss-Newton component of the task Hessian:
Hbeh(θ∗;P) =H GN(θ∗).
E.3 Connection to functional dimension
Following Grigsby et al. [15], the batch functional dimension atθ ∗ on a finite probe setPis
FDP (θ∗) = rank

JP (θ∗)

.
The full local functional dimension is obtained by taking the supremum over finite probe sets,
FD(θ∗) = sup
Q
rank

JQ(θ∗)

.
ThusFD P (θ∗)≤FD(θ ∗).
We know from Equation (6) that the behavioral Hessian is the Jacobian Gram matrix J ⊤ P JP, which
has the same kernel asJ P and hence
rank

Hbeh(θ∗;P)

= FDP (θ∗)≤FD(θ ∗).
This connects our local loss-geometry statistic to exact functional degeneracy: Directions in the
kernel for all finite probe sets are infinitesimal degeneracies of the realization map: to first order, they
do not change the represented function.
12

E.4 Connection to the empirical NTK
The same evaluation-map Jacobian also defines the empirical neural tangent kernel on the probe set.
The empirical NTK atθ ∗ is
KP (θ∗) = 1 |P| JP (θ∗)JP (θ∗)⊤ ∈R |P|m×|P|m .
Thus the behavioral Hessian and the empirical NTK have the same nonzero eigenvalues as well as
the same rank. The two matrices act on different spaces. The empirical NTK acts on probe-set output
perturbations, whereas the behavioral Hessian acts onparameterperturbations.
E.5 Connection to Information Geometry
The identification of the behavioral Hessian as a Jacobian Gram matrix in Equation (6) gives us
a natural connection to information geometry (IG) [ 2]. As a central element in IG, we study the
Fisher Information Matrix (FIM) which is defined as the expected outer product of the log-likelihood
gradients of a parameterized distributionp(y|x, θ):
I(θ) =E x∼P

∇θ logp(y|x, θ)∇θ logp(y|x, θ)⊤ ;
which can equivalently be expressed as the negative expectation of the Hessian.
In the following we outline how this can be connected to the behavioral loss. Starting from the
stacked evaluation mapF X (θ) =

fθ(xi)
N
i=1 ∈R N m, the loss
Lbeh(θ) = 1 2|P| ∥FP (θ)−F P (θ∗)∥2
can be reinterpreted as anegative log-likelihood 4 under a Gaussian observation model on the outputs
FP (θ∗) =F P (θ) +ε, ε∼ N(0, I)
equivalently we can write
p(FP (θ)|θ)∝exp (−|P|L beh(θ))
where locally around θ∗, we have defined a parametric statistical model over the probe set output and
Lbeh(θ) =− 1 |P| logp(F P (θ∗)|θ) + constant
Therefore the FIM naturally emerges as
I(θ) =E x∼P

∇θ logp(y|x, θ)∇θ logp(y|x, θ)⊤
= 1 |P| JP (θ)⊤JP (θ).
So atθ ∗,
I(θ ∗) =H beh(θ∗;P),
and the behavioral Hessian is exactly the empirical Fisher Information Matrix of this probe-induced
model.
This gives us directly the interpretation that behavioral degeneracy is linked to statistical non-
identifiability under the probe distribution, which directly links back to the previously discussed
notion of functional dimension. Similarly, the rank can be interpreted as an information-geometric
notion where the behavioral recovery rank ˆrq becomes the minimal number of informationally
significant directions needed to recover performance. Finally, we can recall that we previously noted
Hbeh = 1 |P| J ⊤J, K P = 1 |P| J J⊤.
From an IG viewpoint, we can therefore see Hbeh as a metric on the parameter space and KP as a
metric on the function space, which describes a dual relationship via the evaluation map.
4Remark: this is not a unique choice for building a statistical model but illustrates how the connection to the behavioral loss
can be established formally. This model is not meant to describe a real data-generating process globally, instead it captures
local deviations in the function space and instead should be viewed as a local statistical model that probes how parameters
affect outputs nearθ ∗.
13

6 10 14 18
Hidden width d
0
50
100
150
200degrees of freedom
rτ, τ = 0.075
eigenvalue
loss-optimal
Pruning
structure
magnitude
(a) Noiseless.
6 10 14 18
Hidden width d
0
50
100
150
200
250degrees of freedom
rτ, τ = 0.075
eigenvalue
loss-optimal
Pruning
structure
magnitude (b)σ 2 = 0.01
Figure 3: We repeat the pruning experiments of Figure 1(c), refitting the student’s output layer in
closed form after each removal. The dash-dotted lines show a teacher control: the same pipeline
applied to the teacher network itself. With refitting, structure pruning curves flatten similarly to
the recovery rank, approaching the teacher’s compressible level. Magnitude pruning still increases
notably.
F Pruning with refitting
The baselines in Section 2 delete parameters and leave the remainder untouched. We additionally
report arefittedvariant in which the output layer is refitted after each removal. Since the network
output is linear in the final layer given the surviving hidden activations, the optimal weights for a
fixed set of retained units are available in closed form as a least-squares solution, so no gradient
steps are required and the procedure remains one-shot. The refit is computed on the training split
and respects the sparsity pattern, in that entries removed by pruning are held at zero and only the
surviving support is re-solved.
The refitted variant quantifies whether the retained units still span enough of the function, since their
contributions are recombined optimally afterwards. This is a substantial intervention, since the output
layer comprises roughly half of the weights in these two-layer students.
Figure 3 repeats Figure 1(c) under this refitting, together with the same quantities measured on the
teacher network itself (dash-dotted). The retained degrees of freedom fall substantially for structure
pruning, and greedy neuron removal becomes approximately flat in width rather than continuing to
grow. Part of the gap reported in Section 3 therefore reflects the absence of compensation rather than
the coordinate basis alone, although both baselines remain above the loss-optimal recovery rank. We
do not repeat this variant on MNIST, since the closed form relies on a squared-error objective and has
no counterpart under cross-entropy.
G Further experimental results
In this appendix, we provide further experimental results that were omitted in the main paper for
brevity.
G.1 Teacher-student Experiments
Changes of probe set and reference point.Figures 4–5 suggest that the recovery behavior is
qualitatively stable under changes of probe set and reference point, suggesting that the observed
trends are not tied to a particular reconstruction choice. For θref =θ 0, the curve flattens less for
widths exceeding teacher width, but still significantly.
Changes of model architectureWe change parts of our teacher/student architecture to test the
robustness of the findings and show Figure 1 under these changes. In practice, we modify the input
size (Figure 6), output size (Figure 7), and both (Figure 8). As an additional ablation, we add noise to
the training data in our base architecture ( 10→d→10 , described in Appendix C.1.1), shown in
Figure 9. Finally, Figure 10 compares the final MSE on the test/train set with and without noise, where
14

5.0 7.5 10.0 12.5 15.0 17.5 20.0
Hidden width d
60
80
100
120
140
160
180
200r , = 0.075
train, ref = 0
train, ref = 0
test, ref = 0
test, ref = 0
(a) Test MSE.
5.0 7.5 10.0 12.5 15.0 17.5 20.0
Hidden width d
60
80
100
120
140
160
180
200r , = 0.075
train, ref = 0
train, ref = 0
test, ref = 0
test, ref = 0
 (b) Train MSE.
Figure 4: Ablations experiments, confirming robustness under reconstruction choices. We vary
the probe set and θref, mean over 5 runs. The behavioral recovery rank growth is larger in the
task-saturated regime for θref =θ 0 in comparison to θref = 0, but still significantly flattens more than
in the capacity-limited regime.
2 6 10 14 18
Hidden width d
0
50
100
150
200rq or r
Absolute
= 0.05
= 0.075
= 0.1
Relative
q = 0.8
q = 0.85
q = 0.9
regression on
rq/r
teacher
d * = 10
(a) Same as Figure 1 (b), but the test
set is used as probe set.
6 10 14 18
Hidden width d
100
150
200
250rq or r
Absolute
= 0.05
= 0.075
= 0.1
Relative
q = 0.8
q = 0.85
q = 0.9
regression on
rq/r
teacher
d * = 10
(b) Same as Figure 1 (b), but θref =
θ0.
2 6 10 14 18
Hidden width d
50
100
150
200rq or r
Absolute
= 0.05
= 0.075
= 0.1
Relative
q = 0.8
q = 0.85
q = 0.9
regression on
rq/r
teacher
d * = 10
(c) Same as Figure 1 (b), but train MSE, not test
MSE
Figure 5: Ablation experiments: Detailed curves for different behavioral rank thresholds, showing
the ranks for selected curves of Figure 4.
a slight double descent is visible. These experiments confirm that our findings on the teacher-student
model seem robust across different architectural parameters.
Spectral structure.The spectral structure of the behavioral Hessian further supports the interpretation
of Figure 1. Figure 11 (a) shows that the leading eigenvalues remain separated from a broad tail
across widths, while Figure 11 (b) and Figure 11 (c) indicate that a limited subset of eigenmodes
captures most of the spectral mass even as the parameter count grows.
G.2 MNIST
Evolution over training.Figure 12 shows test loss and accuracy evolution over training, reaching
final accuracies exceeding.95,for all considered widths.
Projection.In Figure 13, we show the projection impact also on the training loss and accuracy.
Spectral structure.Figure 14 shows a concentrated behavioral spectrum, further supporting the view
that only a restricted subset of local parameter directions dominates functional recovery.
15

200 400
Leading eigendirections k
2
4
6
8
10
12
14
16
18
20Hidden width d
10 1
test MSE
(a) Test MSE for projecting on vary-
ing number of eigendirections.
2 6 10 14 18
Hidden width d
100
200
300rq or r
Absolute
= 0.05
= 0.075
= 0.1
Relative
q = 0.8
q = 0.85
q = 0.9
regression on
rq/r
teacher
d * = 10
(b) Behavioral recovery rank extracted from the pro-
jection curves, mean and std. over5runs.
6 10 14 18
Hidden width d
0
100
200
300
400
500degrees of freedom
rτ, τ = 0.075
eigenvalue
loss-optimal
Pruning
structure
magnitude
(c) Pruning and behavioral recov-
ery rank to loss threshold.
Figure 6: Same setup as Figure 1, but with input dimension set to20.
200 400
Leading eigendirections k
2
4
6
8
10
12
14
16
18
20Hidden width d
10 2
10 1
test MSE
(a) Test MSE for projecting on vary-
ing number of eigendirections.
2 6 10 14 18
Hidden width d
50
100
150
200
250rq or r
Absolute
= 0.05
= 0.075
= 0.1
Relative
q = 0.8
q = 0.85
q = 0.9
regression on
rq/r
teacher
d * = 10
(b) Behavioral recovery rank extracted from the pro-
jection curves, mean and std. over5runs.
6 10 14 18
Hidden width d
0
100
200
300
400
500degrees of freedom
rτ, τ = 0.075
eigenvalue
loss-optimal
Pruning
structure
magnitude
(c) Pruning and behavioral recov-
ery rank to loss threshold.
Figure 7: Same setup as Figure 1, but with output dimension set to20.
200 400
Leading eigendirections k
2
4
6
8
10
12
14
16
18
20Hidden width d
10 1
6 × 10 2
2 × 10 1
3 × 10 1
test MSE
(a) Test MSE for projecting on vary-
ing number of eigendirections.
2 6 10 14 18
Hidden width d
0
100
200
300
400rq or r
Absolute
= 0.05
= 0.075
= 0.1
Relative
q = 0.8
q = 0.85
q = 0.9
regression on
rq/r
teacher
d * = 10
(b) Behavioral recovery rank extracted from the
projection curves, mean and std. over5runs.
6 10 14 18
Hidden width d
0
100
200
300
400degrees of freedom
rτ, τ = 0.075
eigenvalue
loss-optimal
Pruning
structure
magnitude
(c) Pruning and behavioral recov-
ery rank to loss threshold.
Figure 8: Same setup as Figure 1, but with input dimension set to20, and output dimension5.
200 400
Leading eigendirections k
2
4
6
8
10
12
14
16
18
20Hidden width d
10 1
test MSE
(a) Test MSE for projecting on vary-
ing number of eigendirections.
2 6 10 14 18
Hidden width d
100
200
300rq or r
Absolute
= 0.05
= 0.075
= 0.1
Relative
q = 0.8
q = 0.85
q = 0.9
regression on
rq/r
teacher
d * = 10
(b) Behavioral recovery rank extracted from the pro-
jection curves, mean and std. over5runs.
6 10 14 18
Hidden width d
0
100
200
300degrees of freedom
rτ, τ = 0.075
eigenvalue
loss-optimal
Pruning
structure
magnitude
(c) Pruning and behavioral recov-
ery rank to loss threshold.
Figure 9: Same setup as Figure 1, but with noiseσ 2 = 0.01. The same regimes emerge.
16

2 6 10 14 18
Hidden width d
10 9
10 8
10 7
10 6
10 5
10 4
10 3
10 2
10 1
Final MSE
train MSE
test MSE
(a) Noiseless.
2 6 10 14 18
Hidden width d
10 4
10 3
10 2
10 1
Final MSE
train MSE
test MSE (b)σ 2 = 0.01
Figure 10: We show final MSE for different student widths d. While in the noiseless setting, the
training and test losses almost match, for the setting with noise, the students’ train mean errors recover
the noise level, with a slight double-descent-like behavior. The test data is noiseless.
10 20 30 40
Behavioral-Hessian eigenvalue index k
100
Eigenvalue
4
6
8
10
12
14
16
18
20
Hidden width d
(a) Top eigenvalues of the behavioral Hes-
sian, for different student widths.
2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0
Hidden width d
25
50
75
100
125
150
175
200
225Spectral rank sq
q=0.90
q=0.95
q=0.99
(b) Number of eigenvalues needed to
reachq× P i λi.
0 100 200 300 400
T op eigenvalues k
0.0
0.2
0.4
0.6
0.8
1.0Fraction of total eigenvalues
4
6
8
10
12
14
16
18
20
Hidden width d (c) For different students, we plot the pro- portion of the top k eigenvalues among
all Pk i λi/ P i λi. Dotted lines indicate
the thresholdsq= 0.90,0.95,0.99.
Figure 11: Spectral quantities for the teacher-student experiments, for one seed.
0 250 500 750 1000 1250 1500 1750 2000
Training Step
0.0
0.2
0.4
0.6
0.8
1.0T est accuracy
Widths
32,32
64,64
96,96
128,128
160,160
(a) Test accuracy.
0 250 500 750 1000 1250 1500 1750 2000
Training Step
0.0
0.5
1.0
1.5
2.0Cross-Entropy Loss
Widths
32,32
64,64
96,96
128,128
160,160 (b) Test loss.
Figure 12: For different widths of the MLP on MNIST, we report the accuracy and loss over the test
set. The final accuracy exceeds95%for all widths.
17

0 2000 4000 6000 8000 10000 12000
Number of leading eigendirections k
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0Cross Entropy Loss
Widths
32,32
64,64
96,96
128,128
160,160
Final loss
(a) Training loss.
0 2000 4000 6000 8000 10000 12000
Number of leading eigendirections k
0.0
0.2
0.4
0.6
0.8
1.0Train accuracy
Widths
32,32
64,64
96,96
128,128
160,160 (b) Training accuracy.
Figure 13: Additional MNIST experiments, showing the training loss and training accuracy over the
number of leading eigendirections.
0 2000 4000 6000 8000 10000 12000
Behavioral Hessian eigenvalue index k
10 2
10 1
100
101
102
103
Eigenvalues
Widths
32,32
64,64
96,96
128,128
160,160
(a) Eigenvalues overk, for different widths.
26,506
(32,32)
55,050
(64,64)
85,642
(96,96)
118,282
(128,128)
152,970
(160,160)
Parameter count p (widths)
0
1000
2000
3000
4000
5000
6000
7000
8000Leading eigenvalues
q=0.90
q=0.95
q=0.99 (b) Number of eigenvalues needed to reach q×Pm
i λi among the top m= 12000 ones, for
different widths.
0 2000 4000 6000 8000 10000 12000
T op eigenvalues k
0.0
0.2
0.4
0.6
0.8
1.0Fraction of total eigenvalues
Widths
32,32
64,64
96,96
128,128
160,160
(c) Proportion of the top k eigenvalues among
the top 12,000 ones, Pk i λi/ P12,000 i λi, for
different widths. Dotted lines indicate the thresh-
oldsq= 0.90,0.95,0.99.
Figure 14: Spectral quantities for the MNIST experiments.
18
