---
title: Cautious optimism for deep parameterized quantum circuits
url: https://arxiv.org/abs/2607.21409
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: ''
authors:
- Marie Kempkes
- Elies Gil-Fuster
- Carlos Bravo-Prieto
- Aroosa Ijaz
- Alissa Wilms
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.21409
pages: 21
chars: 84593
fetched_at: '2026-11-08T13:27:18+00:00'
kb_version: 1
---

# Cautious optimism for deep parameterized quantum circuits

Cautious optimism for deep parameterized quantum circuits
Marie Kempkes,1, 2,∗ Elies Gil-Fuster, 3, 4 Carlos Bravo-Prieto,3 Aroosa Ijaz, 5, 6
Alissa Wilms,3, 7 Jens Eisert, 3 Evert van Nieuwenburg, 1 and Vedran Dunjko1
1Leiden University, Niels Bohrweg 1, 2333 CA Leiden, Netherlands
2Volkswagen Group Innovation, Berliner Ring 2, 38440 Wolfsburg, Germany
3Dahlem Center for Complex Quantum Systems, Freie Universit ¨at Berlin, 14195 Berlin, Germany
4Fraunhofer Heinrich Hertz Institute, 10587 Berlin, Germany
5Department of Physics and Astronomy, University of Waterloo, ON N2L 3G1, Canada
6Vector Institute, Toronto, ON M5G 0C6, Canada
7Porsche Digital GmbH, 71636 Ludwigsburg, Germany
A central challenge in quantum machine learning is understanding the scaling behavior ofparameterized
quantum circuits(PQCs). In particular, it remains unclear how their performance on unseen data changes as
the number of trainable parameters increases. Prior works have derived formal generalization guarantees for
quantum models, but it is well-known that many such results do not fully characterize generalization behavior
in practice. In this work, we show that gradient-based PQCs can exhibit improved performance on unseen
data as model size increases, displaying the phenomenon of double descent. This contrasts with the traditional
view that larger models lead to degraded generalization. We provide analytical results rigorously underpinning
this behavior by leveraging add-one-in perturbation techniques and spectral properties of random matrices. We
support these results with numerical experiments on re-uploading PQCs across several data sets and training set
sizes, consistently observing the predicted double descent behavior. While other obstacles on the path toward
practical quantum machine learning remain, our finding that deeper parameterized quantum circuits do not
necessarily exhibit degraded performance provides reasons for cautious optimism.
Quantum machine learning(QML) has emerged as a
promising paradigm at the intersection of quantum comput-
ing and data-driven learning, with the potential to outper-
form classical methods for specific learning tasks. Indeed,
a growing body of work has identified concrete settings in
which quantum models can offer computational advantages
over classical counterparts [1–11]. Despite this substantial
progress, many fundamental aspects of QML remain poorly
understood. In particular, it is still unclear whether, and under
what precise conditions, quantum advantage can be expected,
especially as models are scaled to larger numbers of trainable
parameters. While several limitations to the trainability ofpa-
rameterized quantum circuits(PQCs) are now well charac-
terized [12–16], considerable effort has also been devoted to
understanding their generalization behavior through bounds
on the difference between empirical and expected risk. These
bounds depend, for example, on the training set size, the num-
ber of trainable gates, and the data-encoding strategy [17–24].
However, they do not directly address how the expected risk
attained by a trained model changes as the number of param-
eters crosses the so-calledinterpolation threshold, namely,
the critical point at which the number of parameters becomes
comparable to the number of training points.
In classical machine learning, studying the behavior of
models across this threshold has led to substantial insights
through the so-calleddouble descentphenomenon [25]. Con-
trary to traditional expectations from statistical learning the-
ory, double descent describes a non-monotonic relationship
between test error and model size. As the number of param-
eters increases, the test error initially follows a classical U-
shaped curve, peaking near the interpolation threshold. Re-
markably, further overparameterization often leads to a sec-
ond descent phase, during which the test error decreases again
and eventually saturates. This behavior marks a transition
from the underparameterized to the overparameterized regime
and has been observed across a wide range of classical models
and learning tasks [25–28].
In the realm of quantum machine learning, however, anal-
ogous scaling behavior has so far been much less explored.
Ref. [29] has shown that quantum kernel methods can, in prin-
ciple, exhibit a similar scaling behavior in the overparameter-
ized regime, assuming trainability can be maintained. More
recently, Ref. [30] has reported non-monotonic test-error dy-
namics during the training of overparameterized PQCs. This
naturally raises the question of whether PQCs trained with
gradient-based methods also exhibit double descent as a func-
tion of the number of trainable parameters. To date, some
evidence has pointed toward a standard U-shaped risk curve
for PQCs, suggesting that overparameterization may not yield
a second descent [31]. This conclusion is obtained for cir-
cuits in which concentration effects dominate, a regime often
associated with poor trainability.
In this work, we instead focus on PQCs operating in a train-
able regime and study their generalization properties as the
number of trainable parameters increases. Building on an ex-
isting lower bound on the expected risk, we show that, un-
der reasonable assumptions, the bound attains a maximum at
the interpolation threshold. We further derive a correspond-
ing upper bound and show that it likewise attains a maximum
at interpolation. Together, these results establish a double de-
scent behavior in the risk bounds of PQCs analogous to that
observed in classical machine learning. We further support
our theoretical findings with numerical experiments on a va-
riety of datasets. Overall, our results provide new insight into
the scaling behavior of gradient-based quantum models and
suggest that overparameterization may play a role in PQCs
arXiv:2607.21409v2  [quant-ph]  5 Aug 2026

2
similar to that observed in classical machine learning, offer-
ing cautious optimism for the prospects of quantum machine
learning at scale.
PRELIMINARIES
We consider the ubiquitous setting of supervised learning
with quantum learning models based onparametrized quan-
tum circuits(PQCs). Refer to Appendix A for a fully-formal
presentation of our framework. We consider a learning task
ond-dimensional inputsxandK-dimensional labelsy, and
assume we are given a training setS={(x i, yi)}N i=1 ofN
input-output pairs, sampled i.i.d. from the underlying distri-
bution that defines the problem.
Considerdata re-uploadingPQCs [32], where data-
dependent layersU ℓ(x)and trainable layersV ℓ(ϑ)are alter-
nated, forℓ∈ {1, . . . , L}. Here,ϑis ap-dimensional vector
of trainable parameters. Starting from an initial state, the data
re-uploading PQC prepares a parametrized stateρ(x;ϑ)that
depends on both the dataxand the parametersϑ. To fully
specify our model, we fix observablesOk fork∈ {1, . . . , K},
from which we define the hypothesis functions. Specifically,
thek th output of the hypothesis function is given by the ex-
pectation value ofO k with respect to the parametrized state
ρ(x;ϑ)
[fϑ(x)]k = Tr{ρ(x;ϑ)O k}.(1)
Given a loss functionℓ((x, y);ϑ), our goal is to minimize
theexpected risk, defined as the average loss over the problem
distribution
L(ϑ) =E[ℓ((x, y);ϑ)].(2)
In practice, we assume the underlying distribution is un-
known, and we explicitly optimize theempirical risk– the
average loss over the training set
ˆLS(ϑ) = 1 N
NX
i=1
ℓ((xi, yi);ϑ),(3)
where(x i, yi)are the elements of the training setS. In this
work, we focus on the mean-squared error lossℓ((x, y);ϑ) =
1
2 ∥fϑ(x)−y∥ 2.
We next follow the formalism in Ref. [33], with further
technical details being deferred to Appendix B. Our study
is specialized to the final parameters reached during training,
which we denote by ˆϑS. We make the explicit assumption that ˆϑS is alocal minimum of the empirical risk, as is common in
gradient-based QML. Under this assumption, ˆϑS satisfies
∇ϑ ˆLS( ˆϑS) = 0and ˆHS( ˆϑS)⪰0,(4)
where ˆHS(ϑ) :=∇ 2 ϑ ˆLS(ϑ)is the Hessian matrix of the em-
pirical risk.
We now derive an approximation of the expected risk via
a so-calledadd-one-inanalysis. Specifically, we consider in-
serting an additional pair(x ′, y′)to the training setS. Denote
by ˆϑS′ the final training parameters, whereS′ is the union ofS
and the new datum. The value of the lossℓ((x ′, y′); ˆϑS′)will
depend on the new datum. With these, define the so-called
add-one-in lossL ′(S)as
L′(S) :=E h ℓ  (x′, y′); ˆϑS′ i ,(5)
where the average is over(x ′, y′)being drawn from the prob-
lem distribution. While not immediately obvious, the quantity
L′(S)plays a central role in deriving an approximation of the
expected risk. The key idea is that the transition fromSto
S′ constitutes a small perturbation of the training set, allow-
ing the parameter displacement ˆϑS′ − ˆϑS and the associated
change in loss at(x ′, y′)to be approximated via so-called in-
fluence functions [34]. Averaging over the choice of the addi-
tional sample(x ′, y′)then yields an approximation of the ex-
pected risk that is accurate up to corrections of orderO(N−2).
To state the resulting expression, we introduce the gra-
dients of the loss functionJ ℓ((x, y);ϑ) =∇ ϑℓ((x, y);ϑ)
and the gradients of the hypothesis functionsJ f ((x, y);ϑ) =
∇ϑfϑ(x). Denote by
C(ϑ) :=E[J ℓ((x, y);ϑ)Jℓ((x, y);ϑ)⊺](6)
the average of the outer product of the loss gradients over the
problem distribution. Analogously,C f (ϑ)is given by the av-
erage of the outer product of the hypothesis gradients
Cf (ϑ) :=E[J f ((x, y);ϑ)Jf ((x, y);ϑ)⊺].(7)
As a technical comment, we condition the average inC f (ϑ)
to be only over samples(x, y)for which∥J f ((x, y);ϑ)∥2 is
greater than zero. Note that bothC(ϑ)andC f (ϑ)are uncen-
tered covariance matrices.
With these quantities, Theorem 3 in Ref. [33] provides an
error decomposition for the expected risk
L( ˆϑS) =L ′(S)+ 1 N+ 1 Tr h ˆHS( ˆϑS) i−1 C( ˆϑS)  (8)
evaluated at the local minimum ˆϑS, where the inverse of the
Hessian is understood as the Moore–Penrose pseudoinverse.
The decomposition holds up to second- and higher-order cor-
rectionsO

N −2 . Building on this decomposition, Theorem
4 in Ref. [33] derives a lower bound on the expected risk in
the scalar-output case (K= 1) by rewriting the trace term and
applying standard eigenvalue inequalities, yielding
L( ˆϑS)≥ L′(S) + 1 N+ 1 α ξ2 minλmin(Cf ( ˆϑS)) λmin( ˆHS( ˆϑS)) .(9)
Here,ξ 2 min is the smallest non-zero value of∥J f ((x, y);ϑ)∥2,
and the theorem assumes that data can be found for which

3
∥Jf ((x, y);ϑ)∥2 >0with probabilityαover the problem dis-
tribution. Further,λ min denotes the smallest non-zero eigen-
value of a matrix. We note that the lower bound scales in-
versely with the smallest non-zero eigenvalue of the Hessian
matrix of the empirical risk at local minima,λ min( ˆHS( ˆϑS)).
The authors of Ref. [33] then carefully investigate the smallest
non-zero eigenvalues of the matrices arising in classical neu-
ral networks. At this point, we depart from their formalism,
and rather specialize to usual gradient-based PQCs.
DOUBLE DESCENT BEHA VIOR IN PQCS
Our goal is to characterize the behavior of the lower bound
on the expected risk in Eq. (9) as we vary the number of train-
able parameters in our modelp, as well as the number of train-
ing dataN. In particular, we consider the asymptotic limit
wherep, N→ ∞with fixed ratiop/N→γ. The analysis
relies on a series of formal assumptions, listed in Appendix C
together with all further technical details. These assump-
tions are meant to capture the behavior of QML models in
practice, when undergoing gradient-based training, and they
mostly concern statements about the spectral properties of ma-
trices related to the Hessian and the covariance matrices intro-
duced above. We expect our assumptions to be largely ansatz-
agnostic and to hold for a broad class of trainable PQCs, in-
cluding data re-uploading architectures. We further test a se-
lection of these assumptions numerically in Appendix F.
We can now state our main result, which holds in the sim-
pler case of learning tasks with a single output dimension
K= 1.
Theorem 1(Double descent peak at interpolation – informal).
With the definitions above, and under reasonable assump-
tions, for Gaussian-distributed input datax∼ N(0,I d), out-
putsy∈R, and considering the mean-squared error loss, the
lower bound onL( ˆϑS)attains a maximum atp=Nwith high
probability in the limitp, N→ ∞with fixed ratiop/N→γ.
The formal version of this result is Theorem C.3, which
can be found in Appendix C. The proof can be found in Ap-
pendix D. The main idea for the proof is to carefully control
the spectral properties of several random matrices, which we
achieve by combining our assumptions with seminal results in
random matrix theory. Ultimately, we argue that the smallest
non-zero eigenvalue of the dominant contribution to the Hes-
sian matrix follows the behavior predicted by the so-called
Marˇcenko-Pastur law in the stated limit. Our analysis is in-
spired by the framework of Ref. [33], with suitable modifica-
tions to the underlying assumptions.
The assumption of i.i.d. Gaussian inputs is standard in high-
dimensional random matrix analyses and has been extensively
studied in classical literature [35, 36]. The earlier work on
double descent in QML [29] already argues that such assump-
tions often extend beyond strictly Gaussian data. Notably,
the datasets considered in our numerical experiments in Sec-
tion are non-Gaussian, suggesting that the predicted behavior
may extend beyond the assumptions of the theorem.
Theorem C.3 is restricted to the scalar-output caseK= 1.
Nevertheless, the interpolation threshold in the proof arises
from the spectral properties of a matrix of sizep×N Kin
the general case, suggesting that the relevant transition should
more generally occur when the number of parameters matches
the number of scalar training constraintsN K. We therefore
conjecture that, under the assumptions of Theorem C.3, the
lower bound on the expected risk exhibits a double descent
peak atp=N Kalso forK >1. Our numerical experiments
provide evidence supporting this conjecture.
Finally, in Appendix E we provide further results concern-
ingupper boundsto the expected risk. Specifically, in Theo-
rem E.1 we give the upper bound
L( ˆϑS)≤ L′(S) + 1 N+ 1 α ξ2 max R λmax(Cf ( ˆϑS)) λmin( ˆHS( ˆϑS)) .(10)
Similarly as in Eq. (9), this bound holds up to second-order
correctionsO(N −2), and is dominated by spectral proper-
ties of the Hessian matrix ˆHS( ˆϑS)and the covariance matrix
Cf ( ˆϑS). Hereξ 2 max is defined analogously as before, andR
is the rank of the Hessian matrix, i.e., the number of non-zero
eigenvalues. Under a slightly different set of assumptions, we
show in Theorem E.2 that this upper bound also peaks at in-
terpolationp=N, with high probability in the same limit as
above.
EMPIRICAL EVIDENCE OF DOUBLE DESCENT IN PQCS
The theoretical results presented in the previous section
hold in the asymptotic limit and rely on assumptions about the
local geometry of the loss landscape at local minima as well
as the data being Gaussian. In this section, we provide numer-
ical evidence that gradient-based data re-uploading PQCs dis-
play the predicted double descent behavior. In particular, we
show that, when training converges, the test loss, used here as
a proxy for the expected risk, exhibits a pronounced peak near
the interpolation thresholdp=N K, wherepis the number
of trainable parameters,Nis the training set size, andKis
the output dimension.
We consider re-uploading PQCs where each inputxis en-
coded through angle embeddings onn= 8qubits, followed
by trainable single-qubit rotations and nearest-neighborCZ
gates. The model output is obtained by measuring Pauli-X
expectation values onKqubits, givingf θ(x)∈R K. Before
evaluating the loss, we rescale these expectation-value outputs
by a fixed factorc= 150. Empirically, we find that such a
rescaling substantially improves optimization and makes con-
vergence to local minima significantly more reliable.
We perform numerical experiments on three datasets,
shown in Fig. 1. The first is the MNIST-1D dataset [37], used
as a multiclass classification task withK= 8classes. The
second is the Fashion MNIST dataset [38], also restricted to

4
200 400 600
Number of parameters
2
4
6
8
10Test loss
(a) MNIST-1D
N=21
N=30
N=39
N=48
200 400 600
Number of parameters
2
4
6
8
(b) Fashion MNIST
200 400 600
Number of parameters
20
40
60
80
(c) Regression
Figure 1. Test loss as a function of the number of parameterspfor (a) MNIST-1D and (b) Fashion MNIST classification, and (c) a multi-
dimensional synthetic regression task, for different training set sizesN. Vertical dashed lines indicate the predicted interpolation thresholds
p=N K. In all three tasks, the test loss peaks close to interpolation and decreases again in the overparameterized regime, displaying a
characteristic double descent profile. The shaded areas correspond to the standard deviation for ten independent experiment repetitions, each
using independently sampled training data.
K= 8classes. Finally, the third dataset is a synthetic multi-
dimensional regression task with input dimensiond= 8and
output dimensionK= 8, generated from a noisy linear tar-
get function. For each dataset, we vary the number of train-
ing samplesN∈ {21,30,39,48}and vary the circuit depth,
thereby scanning across the underparameterized and overpa-
rameterized regimes. Further implementation details are pro-
vided in Appendix G. The vertical dashed lines in Fig. 1 mark
the corresponding interpolation thresholdsp=N K.
These results provide empirical evidence that double de-
scent appears in trainable PQCs optimized by gradient de-
scent. Importantly, the second descent occurs in regimes
where the number of trainable parameters exceeds the num-
ber of training samples, showing that increasing the size of
the PQC further does not necessarily degrade performance on
unseen data, contrary to the traditional expectation that larger
models generalize worse. Instead, once the model passes the
interpolation threshold and training succeeds, additional pa-
rameters can improve generalization. Note, however, that this
does not imply that overparameterized models outperform un-
derparameterized ones. Rather, it supports the main conclu-
sion of our analysis: overparameterization can play a con-
structive role in gradient-based quantum machine learning.
We provide further details in Appendix F and some perspec-
tives in Appendix H. In particular, we show numerical results
systematically testing the formal assumptions we introduce
for Theorem C.3.
DISCUSSION
In this work, we investigate the scalability of gradient-
basedparameterized quantum circuits(PQCs) by analyzing
how their expected risk evolves across different parameteriza-
tion regimes. By combining an add-one-in perturbation anal-
ysis with spectral arguments from random matrix theory, and
building on an existing lower bound on the expected risk, we
show that the bound attains a maximum at the interpolation
threshold. We further derive a corresponding upper bound
and show that it exhibits the same qualitative dependence on
model size. Our analysis therefore establishes that, under mild
assumptions, the risk bounds of a broad class of PQCs exhibit
double descent behavior. We confirm these findings through
comprehensive numerical experiments with data re-uploading
PQCs on both classification and regression tasks.
Our work offers a complementary perspective to the grow-
ing literature on scalable QML under the slogan “train classi-
cal, deploy quantum” [39–42] and extends previous findings
of double descent in quantum kernel methods [29]. The pre-
sented results indicate that overparameterized regimes may be
compatible with favorable learning behavior [25, 43, 44], pro-
viding grounds for cautious optimism about the prospects of
deep PQCs.
The reason why we advocate forcautiousoptimism is
twofold. First, our analysis is restricted to trainable PQCs.
Ref. [31] already pointed out that, in concentration-dominated
regimes where trainability breaks down, larger models may
not exhibit favorable generalization behavior. Our results
should therefore be understood as a statement about what may
be possible if trainability can be maintained as the number of
parameters increases. We regard trainability as a prerequisite
for practically relevant quantum machine learning and there-
fore focus on the generalization properties of models operat-
ing in such a regime. In this sense, we do not solve well-
known trainability problems of QML [12, 15, 45, 46]. At the
same time, we expect the assumptions underlying our analysis
to hold for a broad class of trainable PQCs. Consequently, the
qualitative phenomenon identified here may remain relevant
for future trainable quantum models of practical relevance.
The second reason for caution is that our results do not im-
ply that overparameterized PQCs outperform underparameter-
ized ones. Rather, they show that increasing the number of pa-
rameters beyond the interpolation threshold need not be detri-
mental to generalization, contrary to the traditional expecta-
tion from statistical learning theory that increasing model size
ultimately leads to poorer generalization [47–50]. Determin-

5
ing when overparameterization leads to overall improvements
in expected risk, and under which conditions such improve-
ments can be realized in practice, remain important research
directions.
Another noteworthy observation from our numerical exper-
iments is that rescaling the PQC outputs by a large constant
improves convergence to local minima. One possible expla-
nation is that expectation values are typically concentrated
around zero, so that rescaling increases the density of low-
training-loss solutions in parameter space by shifting the tar-
get labels away from the boundaries of the output interval.
Understanding this effect theoretically is likely of indepen-
dent interest and is left for future work.
Overall, this work provides a framework for understanding
how the generalization performance of parameterized quan-
tum circuits evolves under scaling. We expect these results
to inform future studies of learning, generalization, and over-
parameterization in increasingly large quantum models, and
ultimately provide cautious optimism for deep parameterized
quantum circuits.
Code and data availability.The code and data used in this
study are available in GitHub [51].
Acknowledgments.The authors would like to thank Evan
Peters and Pablo Rodriguez-Grasa for insightful comments on
an earlier version of this manuscript. E.G.-F., C.B.-P. A.W.
and J.E. acknowledge the BMFTR (MUNIQC-Atoms, HY-
BRID, QuSol, Hybrid++), the DFG (CRC 183 and SPP 2514),
Bifold, the Quantum Flagship (Millenion, PasQuanS2), the
Munich Quantum Valley, Berlin Quantum and the European
Research Council (DebuQC) for financial support. E.G.-
F. further acknowledges support from a 2023 Google PhD
Fellowship. V .D. acknowledges support from the European
Union’s Horizon Europe program through the ERC CoG Be-
MAIQuantum (Grant No. 101124342). V .D. and E.vN ac-
knowledge the Dutch National Growth Fund (NGF) as part
of the Quantum Delta NL programme. GPT-5.6 was used to
assist with code development and mathematical consistency
checks during the preparation of this manuscript. All scientific
ideas, analyses, and conclusions are those of the authors, and
all AI-assisted code and text were carefully reviewed, manu-
ally checked, and validated prior to inclusion.
Disclaimer.The results, opinions, and conclusions ex-
pressed in this publication are not necessarily those of V olk-
swagen Aktiengesellschaft or of Porsche Digital GmbH or
those of the European Union or the European Research Coun-
cil Executive Agency. None of the parties involved can be
held responsible for them.
∗ marie.kempkes@volkswagen.de
[1] V . Havl´ıˇcek, A. D. C´orcoles, K. Temme, A. W. Harrow, A. Kan-
dala, J. M. Chow, and J. M. Gambetta, Supervised learning with
quantum-enhanced feature spaces, Nature567, 209 (2019).
[2] R. Sweke, J.-P. Seifert, D. Hangleiter, and J. Eisert, On the
quantum versus classical learnability of discrete distributions,
Quantum5, 417 (2021).
[3] N. Pirnay, R. Sweke, J. Eisert, and J.-P. Seifert, A super-
polynomial quantum-classical separation for density modelling,
Physical Review A107, 042416 (2023).
[4] R. Molteni, S. C. Marshall, and V . Dunjko, Quantum ma-
chine learning advantages beyond hardness of evaluation,
arXiv:2504.15964 (2025).
[5] R. Molteni, C. Gyurik, and V . Dunjko, Exponential quantum ad-
vantages in learning quantum observables from classical data,
npj Quantum Information12, 19 (2026).
[6] G. Carleo, I. Cirac, K. Cranmer, L. Daudet, M. Schuld,
N. Tishby, L. V ogt-Maranto, and L. Zdeborov´a, Machine learn-
ing and the physical sciences, Reviews of Modern Physics91,
045002 (2019).
[7] J. Biamonte, P. Wittek, N. Pancotti, P. Rebentrost, N. Wiebe,
and S. Lloyd, Quantum machine learning, Nature549, 195
(2017).
[8] S. Masot-Llima, E. Gil-Fuster, C. Bravo-Prieto, J. Eisert, and
T. Guaita, Prospects for quantum advantage in machine learn-
ing from the representability of functions, arXiv:2512.15661
(2025).
[9] A. Barthe, M. Y . Rad, M. Grossi, and V . Dunjko, Quantum ad-
vantage in learning quantum dynamics via fourier coefficient
extraction, arXiv:2506.17089 (2025).
[10] R. Bandyopadhyay, R. Molteni, J. Eisert, V . Dunjko, and
S. Jerbi, Provable learning separation for predicting time-
evolution of quantum many-body systems, arXiv:2607.06472
(2026).
[11] J. Eisert and J. Preskill, Mind the gaps: The fraught road to
quantum advantage, arXiv:2510.19928 (2025).
[12] J. R. McClean, S. Boixo, V . N. Smelyanskiy, R. Babbush, and
H. Neven, Barren plateaus in quantum neural network training
landscapes, Nature Communications9, 4812 (2018).
[13] M. Cerezo, A. Sone, T. V olkoff, L. Cincio, and P. J. Coles, Cost
function dependent barren plateaus in shallow parametrized
quantum circuits, Nature Communications12, 1791 (2021).
[14] S. Wang, E. Fontana, M. Cerezo, K. Sharma, A. Sone, L. Cin-
cio, and P. J. Coles, Noise-induced barren plateaus in variational
quantum algorithms, Nature Communications12, 6961 (2021).
[15] E. R. Anschuetz and B. T. Kiani, Quantum variational algo-
rithms are swamped with traps, Nature Communications13,
7760 (2022).
[16] A. A. Mele, A. Angrisani, S. Ghosh, S. Khatri, J. Eisert,
D. Stilck Franc ¸a, and Y . Quek, Noise-induced shallow circuits
and the absence of barren plateaus, Nature Physics22, 751
(2026).
[17] M. C. Caro, E. Gil-Fuster, J. J. Meyer, J. Eisert, and R. Sweke,
Encoding-dependent generalization bounds for parametrized
quantum circuits, Quantum5, 582 (2021).
[18] A. Abbas, D. Sutter, C. Zoufal, A. Lucchi, A. Figalli, and
S. Woerner, The power of quantum neural networks, Nature
Computational Science , 403 (2021).
[19] L. Banchi, J. Pereira, and S. Pirandola, Generalization in quan-
tum machine learning: A quantum information standpoint,
PRX Quantum2, 040321 (2021).
[20] M. C. Caro, H.-Y . Huang, M. Cerezo, K. Sharma, A. Sorn-
borger, L. Cincio, and P. J. Coles, Generalization in quantum
machine learning from few training data, Nature Communica-
tions13, 4919 (2022).
[21] Y . Du, Z. Tu, X. Yuan, and D. Tao, Efficient measure for the ex-
pressivity of variational quantum algorithms, Physical Review
Letters128, 080506 (2022).
[22] E. Gil-Fuster, J. Eisert, and C. Bravo-Prieto, Understanding
quantum machine learning also requires rethinking generaliza-

6
tion, Nature Communications15, 2277 (2024).
[23] P. Rodriguez-Grasa, M. C. Caro, J. Eisert, E. Gil-Fuster, F. J.
Schreiber, and C. Bravo-Prieto, A PAC-Bayesian approach to
generalization for quantum models, arXiv:2603.22964 (2026).
[24] E. Peters and M. Schuld, Generalization despite overfitting in
quantum machine learning models, Quantum7, 1210 (2023).
[25] M. Belkin, D. Hsu, S. Ma, and S. Mandal, Reconciling mod-
ern machine-learning practice and the classical bias-variance
trade-off, Proceedings of the National Academy of Sciences
116, 15849 (2019).
[26] P. Nakkiran, G. Kaplun, Y . Bansal, T. Yang, B. Barak, and
I. Sutskever, Deep double descent: where bigger models and
more data hurt, Journal of Statistical Mechanics: Theory and
Experiment2021, 124003 (2021).
[27] T. Hastie, A. Montanari, S. Rosset, and R. J. Tibshirani, Sur-
prises in high-dimensional ridgeless least squares interpolation,
Annals of Statistics50, 949 (2022).
[28] S. Mei and A. Montanari, The generalization error of random
features regression: Precise asymptotics and double descent
curve, Communications on Pure and Applied Mathematics75,
667 (2022).
[29] M. Kempkes, A. Ijaz, E. Gil-Fuster, C. Bravo-Prieto, J. Spiegel-
berg, E. van Nieuwenburg, and V . Dunjko, Double descent in
quantum kernel methods, PRX Quantum7, 010312 (2026).
[30] D. Pranji ´c, M. Roth, and C. Tutschku, Grokking and
epoch-wise double descent in quantum neural networks,
arXiv:2607.08350 (2026).
[31] Y . Du, Y . Yang, D. Tao, and M.-H. Hsieh, Problem-dependent
power of quantum neural networks on multiclass classification,
Physical Review Letters131, 140601 (2023).
[32] A. P ´erez-Salinas, A. Cervera-Lierta, E. Gil-Fuster, and J. I.
Latorre, Data re-uploading for a universal quantum classifier,
Quantum4, 226 (2020).
[33] S. P. Singh, A. Lucchi, T. Hofmann, and B. Sch ¨olkopf, Phe-
nomenology of double descent in finite-width neural net-
works, inInternational Conference on Learning Representa-
tions (ICLR 2022)(2022).
[34] F. R. Hampel, R. E. M, R. P. J, and S. W. A,Robust Statistics:
The Approach Based on Influence Functions, V ol. 196 (1986).
[35] M. E. A. Seddik, C. Louart, M. Tamaazousti, and R. Couil-
let, Random matrix theory proves that deep learning represen-
tations of GAN-data behave as Gaussian mixtures, inInterna-
tional Conference on Machine Learning(PMLR, 2020).
[36] R. Couillet and Z. Liao,Random Matrix Methods for Machine
Learning(Cambridge University Press, 2022).
[37] S. Greydanus and D. Kobak, Scaling down deep learning with
MNIST-1D, inProceedings of the 41st International Confer-
ence on Machine Learning, ICML (2024).
[38] H. Xiao, K. Rasul, and R. V ollgraf, Fashion-MNIST: a novel
image dataset for benchmarking machine learning algorithms,
arXiv:1708.07747 (2017).
[39] A. Huang, W. Maxwell, V . Belis, E. Peters, J. Pye, S. Jahangiri,
and J. Bowles, Spectral Born machines: classically trainable
quantum generative models for discrete data, arXiv:2607.06675
(2026).
[40] E. Recio-Armengol, S. Ahmed, and J. Bowles, Train on classi-
cal, deploy on quantum: scaling generative quantum machine
learning to a thousand qubits, arXiv:2503.02934 (2026).
[41] A. Kurkin, K. Shen, S. Pielawa, H. Wang, and V . Dunjko, Uni-
versality and kernel-adaptive training for classically trained,
quantum-deployed generative models, arXiv:2510.08476
(2025).
[42] R. J. Banks, A. Crippa, M. Traube, J. Unger, C. Ertler, and
W. Lechner, Qudit extension of parameterized iqp circuits: A
generative quantum machine learning approach to integer data
(2026), arXiv:2606.28236 [quant-ph].
[43] S. D’Ascoli, M. Refinetti, G. Biroli, and F. Krzakala, Double
trouble in double descent: Bias and variance(s) in the lazy
regime, inProceedings of the 37th International Conference
on Machine Learning, Proceedings of Machine Learning Re-
search, V ol. 119, edited by H. D. III and A. Singh (PMLR,
2020) pp. 2280–2290.
[44] Y . Dar, V . Muthukumar, and R. G. Baraniuk, A farewell to the
bias-variance tradeoff? An overview of the theory of overpa-
rameterized machine learning, arXiv:2109.02355 (2021).
[45] E. Anschuetz, A unified theory of quantum neural network loss
landscapes, inInternational Conference on Learning Represen-
tations, V ol. 2025 (2025) pp. 97859–97918.
[46] S. Thanasilp, S. Wang, M. Cerezo, and Z. Holmes, Exponential
concentration in quantum kernel methods, Nature Communica-
tions15(2024).
[47] V . N. Vapnik and A. Y . Chervonenkis, On the uniform con-
vergence of relative frequencies of events to their probabilities,
inMeasures of complexity: festschrift for alexey chervonenkis
(Springer, 2015) pp. 11–30.
[48] V . Vapnik, An overview of statistical learning theory, IEEE
Transactions on Neural Networks10, 988 (1999).
[49] L. G. Valiant, A theory of the learnable, Commun. ACM27,
1134–1142 (1984).
[50] S. Shalev-Shwartz and S. Ben-David,Understanding machine
learning(Cambridge University Press, Cambridge, England,
2014).
[51] Cautious optimism for deep parameterized quantum circuits,
GitHub repository (2026).
[52] Y . Fang, K. Loparo, and X. Feng, Inequalities for the trace of
matrix product, IEEE Transactions on Automatic Control39,
2489 (1994).
[53] P. Yaskov, Necessary and sufficient conditions for the
Marchenko-Pastur theorem, Electronic Communications in
Probability21, 1 (2016).
[54] C. Louart and R. Couillet, Concentration of measure and large
random matrices with an application to sample covariance ma-
trices, arXiv:1805.08295 (2021).
[55] R. Mathias,Singular values and singular value inequalities
(CRC Press, 2013).
[56] K. Karhadkar, M. Murray, H. Tseran, and G. Mont ´ufar, Mildly
overparameterized ReLU networks have a favorable loss land-
scape, arXiv:2305.19510 (2024).
[57] V . Bergholm, J. Izaac, M. Schuld, C. Gogolin, and N. Killo-
ran, Pennylane: Automatic differentiation of hybrid quantum-
classical computations, arXiv:1811.04968 (2018).
[58] F. Pedregosa, G. Varoquaux, A. Gramfort, V . Michel,
B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss,
V . Dubourg,et al., Scikit-learn: Machine learning in python,
The Journal of Machine Learning Research12, 2825 (2011).
[59] N. E. Karoui, The spectrum of kernel random matrices, Annals
of Statistics38, 1 (2010).
[60] X. Cheng and A. Singer, The spectrum of random inner-product
kernel matrices, Random Matrices: Theory and Applications2,
1350010 (2013).
[61] Z. Fan and A. Montanari, The spectral norm of random inner-
product kernel matrices, Probability Theory and Related Fields
173, 27 (2019).

7
Supplementary Material for
“Cautious optimism for deep parameterized quantum circuits”
Appendix A: Framework
Throughout this work, we consider supervised learning tasks on a data spaceZ :=X × Y, whereX ⊆Rd denotes the
input domain andY ⊆R K the output domain. Samplesz= (x, y)are assumed to be drawn i.i.d. from an unknown but fixed
distributionDonZ. Given a training setS={z i}N i=1, the goal is to learn a hypothesisf ϑ ∈ F, whereF={f ϑ :X → Y |ϑ∈
Θ}denotes the hypothesis class andΘ⊆R p the parameter space. The hypothesis class is realized byparameterized quantum
circuits(PQCs). For a classical inputx, the model prepares a quantum state
ρ(x, ϑ) =U(x, ϑ)ρ0U †(x, ϑ),(A1)
whereρ 0 is the initial state andU(x, ϑ)is the unitary implemented by the PQC. A common architecture consists of alternating
data-dependent and parameter-dependent layers,
U(x, ϑ) =
LY
l=1
Vl(ϑ)Ul(x),(A2)
commonly referred to as data re-uploading [32]. We consider vector-valued modelsf ϑ :X → Y ⊆RK with outputs
fϑ(x) =

[fϑ(x)]1, . . .[fϑ(x)]K

,(A3)
where each component is obtained as the expectation value
[fϑ(x)]k = Tr{ρ(x, ϑ)Ok}, k= 1, . . . , K,(A4)
of a Hermitian observable. For classification tasks withK >1, the model outputf ϑ(x)is interpreted as a vector of class scores,
while the predicted label is typically given byargmax k[fϑ(x)]k. ForK= 1, a setting commonly used in binary classification,
the predicted label can instead be obtained by thresholding the output, e.g., viasign(f ϑ(x)).
Let a learning task be specified by a data distributionD(Z), which we assume to be fixed and unknown. We denote by
S={(x i, yi)}N i=1 a training set of sizeNcomposed of i.i.d. samplesz i := (x i, yi)from the problem distributionS∼ D N .
Next, letℓ:Z ×Θ→R ≥0 be a twice-differentiable loss function, which givenz∈ Zand a parameter specificationϑ∈Θ
acts as a measure of distance between the predictionf ϑ(x)and the correct labely. From the loss functionℓand the problem
distributionDwe define the expected risk functionalL: Θ→R ≥0 as
L(ϑ) :=E
z∼D
[ℓ(z, ϑ)].(A5)
The goal in supervised learning is to find a set of parameters that achieve a small expected risk, though this task cannot be tackled
head-on due to the assumption thatDis unknown. Rather, the common approach is to use a proxy quantity relative to a given
training setS, which we denoteempirical risk ˆLS : Θ→R ≥0, defined as
ˆLS(ϑ) := 1 N
NX
i=1
ℓ(zi, ϑ).(A6)
This way, the empirical risk is an unbiased estimator for the expected risk. In the following, we abuse language in that we
identify a functionf ϑ (also calledhypothesis) with its parametersϑ.
Definition A.1(Local minimum).Given the modelF, a training setS, and the empirical risk functional ˆLS, we call a parameter
vectora local minimum, denoted by ˆϑS, if it fulfills
∇ϑ ˆLS( ˆϑS) = 0,(A7)
ˆHS( ˆϑS)⪰0.(A8)
To avoid confusion with other differential operators that appear below,∇ϑ represents the gradient operator
∇ϑ :=

∂
∂ϑ1 · · ·∂ ∂ϑp
⊺
(A9)
with respect to the parameters. Specifically, for anyϑ∈Θ, the gradient of the loss with respect to the parameters is ap-
dimensional column vector∇ ϑ ˆLS(ϑ)∈R p.

8
Remark(Local minima as output).From here on, we make the explicit assumption that standard gradient-based training
techniques produce local minima as output.
We denote by ˆHS(ϑ)the Hessian matrix of the empirical risk
ˆHS(ϑ) =∇ ϑ∇⊺ ϑ ˆLS(ϑ) =

∂2 ˆLS(ϑ)
∂ϑi∂ϑj
!p
i,j=1
.(A10)
The inverse of the Hessian.Our results below are stated in terms of the inverse of the Hessian matrix, which does not exist
unless the matrix is full rank. Throughout this work, we therefore interpret[ ˆHS(ϑ)]−1 as the Moore-Penrose pseudoinverse of ˆHS(ϑ), obtained by inverting only the non-zero eigenvalues. This is particularly relevant in overparameterized models, where
redundant parameters give rise to zero eigenvalues.
Appendix B: Expected risk at local minima
Since double descent is fundamentally a phenomenon of the expected risk, we first derive an explicit expression for the
expected risk attained attained at local minima. To this end, we analyze the effect of adding a single sample to the training set.
Following Ref. [33], we consider an add-one-in perturbation of the empirical risk. Under this perturbation, the empirical risk
changes only slightly, and the corresponding local minimum is therefore expected to remain close to that of the original training
set. This motivates a local expansion around the original local minimum.
Definition B.1(Add-one-in perturbation).Given a training setSand a datumz ′ ∈ Znot already-contained inS, we refer to
S′ =S∪ {z′}as theadd-one-in perturbationofS.
We do not include thez ′ dependence ofS ′ explicitly because below we only make statements that hold in expectation over
z′ ∼ D. The distinction we keep in mind regarding notation is the size of the sets: for|S|=Nwe have|S ′|=N+ 1. Note that
if we callD S the uniform distribution overS, and similarly forS ′, thenD S′ = (1−ε)D S +εδ z′. Hereδ z′ is a delta distribution
centered atz ′, and
ε= 1 N+ 1 .(B1)
In the regime of largeN, we have thatεbecomes small, which justifies callingD S′ a “perturbation” ofD S. Again, we abuse
language and we identify the setsSandS ′ with their uniform distributions.
Lemma B.2(Influence function for add-one-in perturbation, adapted from Ref. [33, Prop. 2]).LetFbe a hypothesis family,S
a training set of sizeN. LetS ′ be the add-one-in perturbation ofS, and let ˆϑS, ˆϑS′ be local minima with respect toSandS ′
respectively. Then, the first-order contribution from adding samples to the training set is as
ℓ(z′, ˆϑS′)−ℓ(z ′, ˆϑS)
ε =−∇ ϑℓ(z′, ˆϑS)⊺
h
ˆHS( ˆϑS)
i−1
∇ϑℓ(z′, ˆϑS) +O
 1
N

.(B2)
Definition B.3(Add-one-in loss).Suppose we are given the modelF, a training setSand its corresponding local minimum
ˆϑS. Further, for any add-one-in perturbationS ′ =S∪ {z′}, let ˆϑS′ be its local minimum. Then, we denote theadd-one-in loss
L′(S)as
L′(S) :=E
z′∼D
h
ℓ(z′, ˆϑS′) i .(B3)
Definition B.4(Uncentered covariance of loss gradients).For any parameter vectorϑ∈R p, we define theuncentered covariance
matrix of the loss gradientsas
C(ϑ) :=E
z∼D
[∇ϑℓ(z, ϑ)∇ϑℓ(z, ϑ)⊺].(B4)
Lemma B.5(Error decomposition, Theorem 3 in Ref. [33]).LetFbe the hypothesis family of a learning model, letSbe a
training set of sizeN, letℓbe a twice-differentiable loss function, let ˆϑS be a local minimum, letL ′(S)be the add-one-in loss,
and let ˆHS( ˆϑS)be the Hessian matrix of the empirical loss at the local minimum. Then, the expected riskL( ˆϑS)fulfills
L( ˆϑS) =L ′(S) + 1 N+ 1 Tr h ˆHS( ˆϑS) i−1 C( ˆϑS)  +O  1 N 2  .(B5)
We refer to the summand with the trace as thecomplexity term.

9
Proof.We prove this statement directly, starting from Lemma B.2 and taking an expectation overD. We start by taking the
equation in the Lemma and substituting
ε= 1 N+ 1 ,(B6)
in order to get
ℓ(z′, ˆϑS′)−ℓ(z ′, ˆϑS)
ε =−∇ ϑℓ(z′, ˆϑS)⊺
h
ˆHS( ˆϑS)
i−1
∇ϑℓ(z′, ˆϑS) +O
 1
N

(B7)
ℓ(z′, ˆϑS′)−ℓ(z ′, ˆϑS) =−ε∇ ϑℓ(z′, ˆϑS)⊺
h
ˆHS( ˆϑS)
i−1
∇ϑℓ(z′, ˆϑS) +O
 1
N 2

(B8)
=− 1 N+ 1 ∇ϑℓ(z′, ˆϑS)⊺ h ˆHS( ˆϑS) i−1 ∇ϑℓ(z′, ˆϑS) +O  1 N 2  .(B9)
Next we perform a common step to turn a vector-matrix-vector product into the trace of a matrix-matrix product as
ℓ(z′, ˆϑS′)−ℓ(z ′, ˆϑS) =− 1 N+ 1 ∇ϑℓ(z′, ˆϑS)⊺ h ˆHS( ˆϑS) i−1 ∇ϑℓ(z′, ˆϑS) +O  1 N 2  (B10)
=− 1 N+ 1 Tr  ∇ϑℓ(z′, ˆϑS)⊺ h ˆHS( ˆϑS) i−1 ∇ϑℓ(z′, ˆϑS)  +O  1 N 2  (B11)
=− 1 N+ 1 Tr h ˆHS( ˆϑS) i−1 ∇ϑℓ(z′, ˆϑS)∇ϑℓ(z′, ˆϑS)⊺  +O  1 N 2  .(B12)
We now take the expectation overz ′ ∼ Don both sides and simplify the terms that do not depend onz′, in order to get
E
z′∼D
h
ℓ(z′, ˆϑS′)−ℓ(z ′, ˆϑS) i =E z′∼D  − 1 N+ 1 Tr h ˆHS( ˆϑS) i−1 ∇ϑℓ(z′, ˆϑS)∇ϑℓ(z′, ˆϑS)⊺  +O  1 N 2  ,(B13)
E
z′∼D
h
ℓ(z′, ˆϑS′) i −E z′∼D h ℓ(z′, ˆϑS) i =− 1 N+ 1 Tr h ˆHS( ˆϑS) i−1 E z′∼D h ∇ϑℓ(z′, ˆϑS)∇ϑℓ(z′, ˆϑS)⊺ i +O  1 N 2  .(B14)
Notice that the two expectations on the left-hand side are precisely the add-one-in loss and the expected risk, and the expectation
value on the right-hand side corresponds to the uncentered covariance of the gradients. From here we need only shift terms
around to complete the proof,
L′(S)− L(ˆϑS) =− 1 N+ 1 Tr h ˆHS( ˆϑS) i−1 C( ˆϑS)  +O  1 N 2  (B15)
L( ˆϑS) =L ′(S) + 1 N+ 1 Tr h ˆHS( ˆϑS) i−1 C( ˆϑS)  +O  1 N 2  .(B16)
RemarkRecall that[ ˆHS( ˆϑS)]−1 denotes the Moore-Penrose pseudoinverse. Consequently, directions corresponding to zero
Hessian eigenvalues do not contribute to the complexity termTr
n
[ ˆHS( ˆϑS)]−1C( ˆϑS) o . Therefore, Lemma B.5 does not con-
tradict the common intuition that flat minima may generalize better. Rather, it shows that the expected risk is increased by
directions that simultaneously exhibit small non-zero curvature and large gradient variance as quantified byC( ˆϑS). Intuitively,
such directions are only weakly constrained by the training set, despite corresponding to directions along which typical samples
from the underlying distribution exhibit substantial gradients.
We next reproduce the lower bound for this error decomposition, following the formalism in Ref. [33]. To this end, we restrict
our attention to the scalar-output caseK= 1and introduce a mild regularity assumption on the loss gradients. We start by
introducing two auxiliary lemmas that will be used in the proof.
Lemma B.6.LetA, B∈R m×m be symmetric matrices, withA, B≥0further being positive semi-definite. Then
λmin(A) Tr{B} ≤Tr{AB} ≤λmax(A) Tr{B}.(B17)
Here,λ min(A)corresponds to the smallest eigenvalue ofA, and similarly forλ max.

10
The proof of Lemma B.6 can be found in Ref. [52].
Lemma B.7.Under Assumption 1 and in the caseK= 1, the complexity term from Lemma B.5 fulfills
Tr
h
ˆHS( ˆϑS)
i−1
C( ˆϑS)

=αE
z∼D
ξ2 z >0

ξ2 z Tr
h
ˆHS( ˆϑS)
i−1
∇ϑf ˆϑS (z)∇ϑf ˆϑS (z)⊺

.(B18)
Proof.We prove this statement directly. We first use the chain rule to relate∇ ϑℓ(z, ϑ)and∇ ϑfϑ(z), and then we separate the
expectation value into the two disjoint conditionsξ 2 z >0andξ 2 z = 0,
∇ϑℓ(z, ϑ):=

∂ℓ(z, ˆϑs)
∂ϑm
!p
m=1
=
 ∂ℓ(z, ϑ)
∂fϑ(x)
∂fϑ(z)
∂ϑm
p
m=1
= ∂ℓ(z, ϑ) ∂fϑ(x) ∇ϑfϑ(x).(B19)
In the caseK= 1, ∂ℓ(z,ϑ) ∂fϑ(x) ∈Ris a scalar and∇ ϑfϑ(x)∈R p is ap-dimensional column vector. We now substitute the chain
rule into the definition ofC( ˆϑS), to obtain
C( ˆϑS) =E z′∼D
h
∇ϑℓ(z′, ˆϑS)∇ϑℓ(z′, ˆϑS)⊺
i
=E
z′∼D



 ∂ℓ(z ′, ˆϑS) ∂fϑ(x)

 2 ∇ϑf ˆϑS (x′)∇ϑf ˆϑS (x′)⊺   .(B20)
The squared term inside the expectation value is exactly∥∇ f ℓ(z′, ˆϑS)∥2 in the case ofK= 1, which we defined asξ 2 z′ in
Assumption 1,
E
z′∼D



 ∂ℓ(z ′, ˆϑS) ∂fϑ(x)

 2 ∇ϑf ˆϑS (x′)∇ϑf ˆϑS (x′)⊺   =E z′∼D h ξ2 z′∇ϑf ˆϑS (x′)∇ϑf ˆϑS (x′)⊺ i .(B21)
Now, we split the expectation value over two disjoint conditionsE z′∼D[·] =P(ξ 2 z′ >0)E z′∼D
ξ2 z′ >0
[·] +P(ξ 2 z′ = 0)E z′∼D
ξ2 z′ =0
[·].
Assumption 1 can be restated as: there exists anα >0such thatP z∼D (ξ2 z >0) =α. With this, we obtain
E
z′∼D
h
ξ2 z′∇ϑf ˆϑS (x′)∇ϑf ˆϑS (x′)⊺
i
=P(ξ 2 z′ >0)E z′∼D
ξ2 z′ >0
h
ξ2 z′∇ϑf ˆϑS (x′)∇ϑf ˆϑS (x′)⊺
i
(B22)
+P(ξ 2 z′ = 0)E z′∼D
ξ2 z′ =0
h
ξ2 z′∇ϑf ˆϑS (x′)∇ϑf ˆϑS (x′)⊺
i
(B23)
=αE
z′∼D
ξ2 z′ >0
h
ξ2 z′∇ϑf ˆϑS (x′)∇ϑf ˆϑS (x′)⊺
i
.(B24)
The second summand vanishes due to theξ 2 z′ = 0condition. Directly substituting these in the complexity term finishes the
proof,
Tr
h
ˆHS( ˆϑS)
i−1
C( ˆϑS)

= Tr



h
ˆHS( ˆϑS)
i−1
αE
z′∼D
ξ2 z′ >0
h
ξ2 z′∇ϑf ˆϑS (x′)∇ϑf ˆϑS (x′)⊺
i


 (B25)
=αE
z′∼D
ξ2 z′ >0

ξ2 z′ Tr
h
ˆHS( ˆϑS)
i−1
∇ϑf ˆϑS (x′)∇ϑf ˆϑS (x′)⊺

.(B26)
Assumption 1(Regularity assumption).There exists a samplez∼ Dwith non-zero probabilityαsuch thatξ 2 z :=
∥∇f ℓ(z, ˆϑS)∥2 >0, where∇ f denotes the gradient with respect to the model output.
For the mean-squared error loss considered in this work, Assumption 1 merely requires that predictions of the model with
parameters ˆϑS differ from the true targets on a subset of the data distribution with non-zero probability.

11
Definition B.8(Uncentered covariance of function gradients).For any parameter vectorϑ∈R p, we define theuncentered
covariance matrix of the function gradientsas
Cf (ϑ) :=E z∼D
ξ2 z >0
[∇ϑfϑ(x)∇ϑfϑ(x)⊺].(B27)
Combining the error decomposition from Lemma B.5 with Assumption 1 yields the following lower bound on the expected
risk in terms of the spectrum ofC f ( ˆϑS)and the Hessian matrix of the empirical risk ˆHS( ˆϑS)at local minima.
Theorem B.9(Lower bound on the expected risk, Theorem 4 Ref. [33]).Under the setting of Lemma B.5, under Assumption 1
and forK= 1, the expected riskL( ˆϑS)at the local minimum ˆϑS fulfills the lower bound
L( ˆϑS)≥ L′(S) + 1 N+ 1 α ξ2 minλmin(Cf ( ˆϑS)) λmin( ˆHS( ˆϑS)) .(B28)
Here, we defineξ 2 min = minz∼D
ξ2 z >0 {ξ2 z }, andλ min(·)the smallest non-zero eigenvalue of its matrix argument.
Proof.The proof follows directly from Lemmas B.5, B.6, and B.7.
We first provide a lower bound for the complexity term in Lemma B.7 using the definition ofξ 2 min
Tr
h
ˆHS( ˆϑS)
i−1
C( ˆϑS)

=αE
z∼D
ξ2 z >0

ξ2 z Tr
h
ˆHS( ˆϑS)
i−1
∇ϑf ˆϑS (z)∇ϑf ˆϑS (z)⊺

(B29)
≥α ξ2 min Tr



h
ˆHS( ˆϑS)
i−1
E
z∼D
ξ2 z >0
h
∇ϑf ˆϑS (z)∇ϑf ˆϑS (z)⊺
o


 (B30)
=α ξ2 min Tr
h
ˆHS( ˆϑS)
i−1
Cf ( ˆϑS)

.(B31)
Lemma B.6 allows us to lower-bound this quantity in terms of the eigenvalues ofC f ( ˆϑS)as
Tr
h
ˆHS( ˆϑS)
i−1
Cf ( ˆϑS)

≥λ min(Cf ( ˆϑS)) Tr
h
ˆHS( ˆϑS)
i−1
.(B32)
Now, under the assumption that ˆHS( ˆϑS)is full-rank, we can immediately relate the trace of its inverse to the eigenvalues of the
Hessian. Namely: the trace of a matrix is the sum of its eigenvalues, and for Hermitian matrices, the eigenvalues of the inverse
are the inverse of the eigenvaluesλ i([ ˆHS( ˆϑS)]−1) = (λi( ˆHS( ˆϑS)))−1,
Tr
h
ˆHS( ˆϑS)
i−1
=
pX
i=1
λi
h
ˆHS( ˆϑS)
i−1
(B33)
=
RX
i=1
1
λi

ˆHS( ˆϑS)
 (B34)
≥ 1
λmin( ˆHS( ˆϑS)) .(B35)
We callR= rank( ˆHS( ˆϑS)), namely the number of non-zero eigenvalues of the Hessian. From the first to the second line, we
replace a sum overpeigenvalues (dimension of the matrix) with a sum over theR-many inverses of non-zero eigenvalues. In
the last step, we lower-bounded the value of a sum of positive numbers by the value of the largest element in the sum. We can

12
finally insert these bounds in the error decomposition (Eq. (B5) from Lemma B.5), to get
L( ˆϑS) =L ′(S) + 1 N+ 1 Tr h ˆHS( ˆϑS) i−1 C( ˆϑS)  +O  1 N 2  (B36)
≥ L′(S) + 1 N+ 1  α ξ2 min Tr h ˆHS( ˆϑS) i−1 Cf ( ˆϑS)  +O  1 N 2  (B37)
≥ L′(S) + α ξ2 min
N+ 1

λmin(Cf ( ˆϑS)) Tr
h
ˆHS( ˆϑS)
i−1
+O
 1
N 2

(B38)
≥ L′(S) + α ξ2 minλmin(Cf ( ˆϑS)) N+ 1  1 λmin( ˆHS( ˆϑS)) ! +O  1 N 2  (B39)
=L ′(S) + 1 N+ 1 α ξ2 minλmin(Cf ( ˆϑS)) λmin( ˆHS( ˆϑS)) +O  1 N 2  .(B40)
This completes the proof.
In particular, the lower bound is governed by the smallest non-zero eigenvalue of the Hessian matrix of the empirical risk at
local minima,λ min( ˆHS( ˆϑS)), a quantity that will play a central role in our subsequent analysis. A complementary upper bound,
obtained using analogous techniques, is presented in Theorem E.1 in Appendix E.
Appendix C: Double descent behavior in PQCs
We now establish that, as the number of trainable parameterspis varied, the lower bound on the expected risk exhibits a
double descent peak. While this does not directly imply that the expected risk itself exhibits double descent, numerical results
presented later provide evidence for a corresponding phenomenon. Restricting to the scalar-output caseK= 1, we show that
the peak occurs atp=N, corresponding to the interpolation threshold. Numerical results presented later indicate the same
qualitative behavior forK >1. We therefore keep the general notation in terms ofKthroughout, although the rigorous results
derived below are restricted toK= 1. Our analysis is inspired by the framework of Ref. [33], with suitable modifications to the
underlying assumptions.
A central ingredient in the derivation is a decomposition of the Hessian of the empirical risk into the so-called outer-product
Hessian ˆH o S(ϑ)and the functional Hessian ˆH f S (ϑ),
ˆHS(ϑ) = ˆH o S(ϑ) + ˆH f S (ϑ),(C1)
where
ˆH o S(ϑ) = 1 N
NX
i=1
∇ϑfϑ(xi)
h
∇f ∇⊺ f ℓ(zi, ϑ) i ∇ϑfϑ(xi)⊺,(C2)
ˆH f S (ϑ) = 1 N
NX
i=1
∇⊺ f ℓ(zi, ϑ)∇ϑ∇⊺ ϑfϑ(xi).(C3)
To prove our main result, Theorem C.3, we require several assumptions on the quantities appearing in the Hessian decompo-
sition and the ensuing spectral analysis. This section culminates with the statement of Theorem C.3, and its proof (including
a derivation for the decomposition of the Hessian) is provided in Appendix D in a self-contained way. We first introduce two
quantities that will play a central role in formulating these assumptions.
Definition C.1(Sample Jacobian of the function).For a training setS={(x i, yi)}N i=1 and parameter vectorϑ∈R p, the
sample Jacobian of the function is defined as
ZS(ϑ) :=  ∇ϑfϑ(x1), . . . ,∇ϑfϑ(xN )  ∈R p×N K.(C4)
Definition C.2(Uncentered sample covariance of function gradients).For a training setS={(x i, yi)}N i=1 and parameter
vectorϑ∈R p, the uncentered sample covariance of the function gradients is defined as
ˆC f S(ϑ) := 1 N ZS(ϑ)ZS(ϑ)⊺ ∈R p×p.(C5)

13
The following assumptions serve different purposes in the analysis. Assumption 2 concerns the behavior of the functional
Hessian near interpolation, while the subsequent assumptions concern properties of the outer-product Hessian and the covariance
of function gradients.
Assumption 2.In the underparameterized regimep < N K, the largest eigenvalueλmax
 ˆH f S ( ˆϑS)  of the functional Hessian at
local minima decreases with the number of trainable parameterspin a neighborhood of the interpolation thresholdp=N K.
For the mean-squared error loss, the functional Hessian depends explicitly on the training residuals. Assumption 2 is therefore
consistent with the expectation that these residuals decrease as the number of trainable parameters increases. We investigate this
assumption numerically later.
The next assumption concerns the second term in the Hessian decomposition, namely the outer-product Hessian ˆH o S(ϑ). For
the scalar-output mean-squared error loss, this term reduces to the uncentered sample covariance of the function gradients,
ˆC f S(ϑ). This follows immediately from the fact that the first derivative of the loss is∇f ℓ(zi, ϑ) = (fϑ(xi)−y i)while its second
derivative∇ f (fϑ(xi)−y i)) = 1. We can, therefore, write
ˆH o S(ϑ) = ˆC f S(ϑ) = 1 N ZS(ϑ)ZS(ϑ)⊺.(C6)
Our next assumption addresses the rank of the sample Jacobian of the function in the overparameterized regime.
Assumption 3.In the overparameterized regimep≥N K, the sample Jacobian of the function at local minimaZ S( ˆϑS)∈
Rp×N Khas full rank,
rank

ZS( ˆϑS)

=N K.(C7)
Intuitively, Assumption 3 means that the trainable parameters affect theN Ktraining outputs in sufficiently many independent
ways. One may expect this condition to hold in sufficiently expressive PQCs, and we provide numerical evidence that it is
satisfied in the settings considered here. We further assume that the spectrum of the uncentered (sample) covariance of function
gradients remains stable during training.
Assumption 4.The smallest eigenvalue of the uncentered sample covariance of the function gradients remains comparable to
its value at initialization uniformly in the number of trainable parametersp:
λmin

ˆC f S( ˆϑS)  ≍λ min  ˆC f S(ϑ0)  .(C8)
More precisely, there exist constantsA, B >0independent ofpsuch that
A λmin

ˆC f S(ϑ0)  ≤λ min  ˆC f S( ˆϑS)  ≤B λmin  ˆC f S(ϑ0)  .(C9)
We further assume that an analogous relation holds for the uncentered covariance of function gradientsC f , with constants
A′, B′ >0. These relations hold with high probability with respect to the random draw of the training setS, the initialization
ϑ0, and the local minimum ˆϑS returned by the training procedure.
Assumption 4 formalizes a form of spectral stability during training. We provide empirical evidence that this assumption
holds in the PQCs considered here.
The next Assumption 5 is a regularity condition on the covariance of function gradients at initialization. It ensures that the
spectrum remains bounded and non-degenerate as the number of trainable parameters varies, thereby enabling random matrix
theoretic analysis, as we discuss in more detail in Appendix D.
Assumption 5(Spectrum of the uncentered covariance of function gradients at initialization).The uncentered covariance of
function gradients at initialization has bounded spectrum. That is, there exist constantsc, c′ >0, independent of the number of
trainable parametersp, such that
c≤λ min (Cf (ϑ0))≤λ max (Cf (ϑ0))≤c ′.(C10)
We expect this assumption to hold for circuit architectures with non-redundant parameterizations and generic initializations.
Our next assumption relates the smallest non-zero eigenvalue of the empirical-risk Hessian to the spectra of its outer-product
and functional contributions.

14
Assumption 6(Weyl-like inequality).The smallest non-zero eigenvalue of the empirical-risk Hessian at ˆϑS satisfies
λmin( ˆH o S( ˆϑS)) +λ min( ˆH f S ( ˆϑS))≤λ min( ˆHS( ˆϑS))≤λ min( ˆH o S( ˆϑS)) +λ max( ˆH f S ( ˆϑS)).(C11)
Note that ifrank( ˆH o S( ˆϑS)) = rank( ˆHS( ˆϑS)), then Weyl’s inequality directly implies Assumption 6. One may therefore
interpret this assumption as requiring that the functional Hessian does not alter the rank structure induced by the outer-product
Hessian. The final assumption concerns the add-one-in loss term appearing in the expected-risk decomposition.
Assumption 7(Add-one-in loss).The add-one-in lossL ′(S)does not dominate the lower bound in Theorem B.9 in a neighbor-
hood of the interpolation threshold.
SinceL ′(S)corresponds to the loss obtained after perturbing the training set by a single sample, one may expect it to remain
close to the empirical risk of the trained model, which is typically small around the interpolation threshold.
We are now ready to present the main result of this work. The following theorem shows that, under the above assumptions,
the lower bound on the expected risk from Theorem B.9 attains a maximum at the interpolation threshold, leading to a double
descent peak as the number of parameters increases.
Theorem C.3(Double descent peak at interpolation).LetS={(x i, yi)}N i=1 be a dataset withd-dimensional Gaussian normal
inputsx i ∼ N(0,Id)and outputsy i ∈R. Letf ϑ :R d →Rbe a parameterized quantum circuit as in Eq.(A4)forK= 1,
consisting ofpparameters. Under Assumptions 1–7, and considering the mean-squared error loss function, the lower bound on
L( ˆϑS)at a local minimum from Theorem B.9 attains a maximum atp=Nwith high probability in the limitN, p→ ∞with
fixed ratiop/N→γ.
Proof sketch.Starting from the lower bound of Theorem B.9, it suffices to analyze the dependence onpof the Hessian-dependent
contribution appearing in the bound. To this end, we use the decomposition from Eq. (C1). Using the upper bound from As-
sumption 6 together with Assumption 4, this term can be further bounded by the smallest non-zero eigenvalue of the uncentered
sample covariance of function gradients at initialization. Consequently, we need to characterize the behavior ofλ min( ˆC f S(ϑ0))
as a function of the parameter dimensionp. Under Assumption 5 and using standard singular value inequalities, central results
in random matrix theory dictate thatλ min( ˆC f S(ϑ0))approaches zero at the interpolation thresholdp=N, while remaining
bounded away from zero on either side of this point with high probability. It therefore remains to control the second term in the
denominator involvingλ max( ˆH f S ( ˆϑS)). In the underparameterized regime, Assumption 2 implies thatλ max( ˆH f S ( ˆϑS))decreases
with increasingp, causing the lower bound to increase. In the overparameterized regime, we can show that Assumption 3 implies
ˆH f S ( ˆϑS) = 0at local minima. Combining these observations with the fact thatλ min( ˆC f S(ϑ0))is minimized at the interpolation
threshold, we conclude that the lower bound attains its maximum atp=N.
A corresponding result on the double descent peak holds for the upper bound derived in Appendix E; see Theorem E.2, which
shows that the upper bound likewise has a maximum at the interpolation thresholdp=N.
Theorem C.3 is restricted to the scalar-output caseK= 1. Nevertheless, the interpolation threshold in the proof arises from
the spectral properties of the sample JacobianZ S(ϑ)∈R p×N K, suggesting that the relevant transition should more generally
occur when the number of parameters matches the number of scalar training constraintsN K. This motivates the following
conjecture.
Conjecture C.4(Interpolation threshold forK >1).Under the setting of Theorem C.3, except thatK >1, the lower bound on
the expected risk exhibits a double descent peak atp=N K.
Our numerical experiments provide evidence supporting this conjecture.
Appendix D: Proof of Theorem C.3
In this section, we prove Theorem C.3, which establishes that the lower bound on the expected risk from Theorem B.9 attains
its maximum at the interpolation threshold. We first collect several auxiliary results concerning the spectrum of the Hessian of
the empirical risk and its decomposition into outer-product and functional contributions. These ingredients are then combined
with random matrix arguments to characterize the behavior of the lower bound as a function of the parameter dimension.

15
Lemma D.1(Decomposition of the Hessian).For a given training setS={z i := (xi, yi)}N i=1, we consider the empirical risk
ˆLS(ϑ) = 1 N PN i=1 ℓ(zi, ϑ). We define the Hessian of the empirical riskˆHS(ϑ) :=∇ ϑ∇⊺ ϑ ˆLS(ϑ). Then, the decomposition
ˆHS(ϑ) = ˆH o S(ϑ) + ˆH f S (ϑ),(D1)
outer-product Hessian: ˆH o S(ϑ) := 1 N
NX
i=1
∇ϑfϑ(xi)
h
∇f ∇⊺ f ℓ(zi, ϑ) i ∇⊺ ϑfϑ(xi),(D2)
functional Hessian: ˆH f S (ϑ) := 1 N
NX
i=1
∇⊺ f ℓ(zi, ϑ)∇ϑ∇⊺ ϑfϑ(xi)(D3)
holds.
Proof.The proof follows the direct application of the chain rule, being careful about the sizes of the algebraic objects involved.
To be precise, we treat∇ ϑ and∇ ⊺ ϑ as operator-valued column and row vectors, respectively; and similarly for∇ (⊺) f .
For anyx, we havef ϑ(x)∈R K,∇ ⊺ ϑfϑ(x)∈R K×p, and∇ ϑ∇⊺ ϑfϑ(x)∈R K×(p×p). The second∇ ϑ acts along a different
direction than the original dimension of the output. For anyz= (x, y), when instantiating the chain rule, we treatℓ(z, ϑ)as
ℓ((f, y);ϑ), withf=f(x). Then, for anyz, we write
∇⊺ ϑℓ(z, ϑ)| {z }
1×p
=∇ ⊺ f ℓ(z, ϑ) | {z }
1×K
∇⊺ ϑfϑ(x)| {z }
K×p
.(D4)
Then, for the second derivative, we have
∇ϑ
1×Kz }| {
∇⊺ f ℓ(z, ϑ)  | {z }
p×K
=∇ ϑfϑ(x)| {z }
p×K
∇f ∇⊺ f ℓ(z, ϑ) | {z }
K×K
.(D5)
We use this for the chain rule of the second derivative, to get
∇ϑ∇⊺ ϑℓ(z, ϑ)| {z }
p×p
=∇ ϑ

∇⊺ f ℓ(z, ϑ)∇⊺ ϑfϑ(x)  (D6)
=

∇ϑ∇⊺ f ℓ(z, ϑ)  ∇⊺ ϑfϑ(x) +∇ ⊺ f ℓ(z, ϑ) (∇ϑ∇⊺ ϑfϑ(x))(D7)
=∇ ϑfϑ(x)| {z }
p×K
∇f ∇⊺ f ℓ(z, ϑ) | {z }
K×K
∇⊺ ϑfϑ(x)| {z }
K×p
+∇ ⊺ f ℓ(z, ϑ) | {z }
1×K
∇ϑ∇⊺ ϑfϑ(x)| {z }
K×(p×p)
.(D8)
Having proven this for arbitraryz= (x, y), the linearity of the differential operators guarantees that it holds for each summand
in ˆHS(ϑ), and hence for the whole sum.
For completeness, we also give expressions for the entries of the two summands, avoiding the matrix-matrix product notation.
Written out in terms of scalars, the(j, j′)th entry of each of the summands in terms of thekth entry of the function[f ϑ(x)]k takes
the form
h
ˆH o S(ϑ) i j,j′ = 1 N NX i=1 KX k,k′=1 ∂[fϑ(xi)]k ∂ϑj ∂2ℓ(zi, ϑ) ∂fk∂fk′ ∂[f ϑ(xi)]k′ ∂ϑj′ ,(D9)
h
ˆH f S (ϑ) i j,j′ = 1 N NX i=1 KX k=1 ∂ℓ(zi, ϑ) ∂fk ∂2[fϑ(xi)]k ∂ϑj∂ϑj′ .(D10)
Lemma D.2(Theorem 2.1 in Ref. [53]).LetXbe a matrix withNcolumnsx p ∈R p. Assumex p are isotropic (i.e.,E[x px⊺ p] =
Ip) random vectors and so-called concentration of quadratic forms
1
p
"
x⊺ p
 1
N XX ⊺ +εI p
−1
xp −Tr
 1
N XX ⊺ +εI p
−1#
→0(D11)

16
is satisfied, asN→ ∞withp=p(N)andp/N→γ. Then, the empirical spectral distribution of the sample covariance
1
N XX ⊺ converges weakly to theMarˇcenko-Pastur(MP) distributionµ MP in the asymptotic limit. Its non-zero eigenvalue density
is given by
µMP(dλ) =
p
(λ+ −λ)(λ−λ −)
2πγλ dλ,(D12)
λ± = (1± √γ)2,(D13)
whereλdenotes an eigenvalue of the sample covariance matrix 1 N XX ⊺, andλ − andλ + denote the lower and upper edges of
the support of the non-zero spectrum, respectively.
Definition D.3(Exponentially-concentrated random vectors [35, Def. 2.1]).Letx∈R p a random vectorx∼ P. We sayxis
anexponentially-concentrated random vectorif, for any1-Lipschitz functionh:R p →R, the following holds:
P
x∼P
h

f(x)−E
x∼P
[f(x)]

 > t i ≤Ae −Bt2 ,(D14)
for constantsA, B >0.
Lemma D.4(Theorem 2.40 in Ref. [54]).Letx∈R p be an exponentially-concentrated random vectorx∼ P, and letA∈R p×p
be a matrix with bounded operator norm. Then,x ⊺Ax−Tr{A}is sharply concentrated.
Definition D.5(Data whitening).Let us callg i =∇ ϑfϑ0 (xi)∈R p for eachi∈ {1, . . . , N}, and recall thatCf (ϑ0) :=
Ezi∼D, ξ2z >0[gig⊺ i ]. Under Assumption 5, we refer to the following aswhitenedrandom vectors:˜g i =C f (ϑ0)−1/2gi. At
the matrix level, we define ˜ZS(ϑ0) = (˜g1, . . . ,˜gN )∈R p×N , which corresponds to ˜ZS(ϑ0) =C f (ϑ0)−1/2ZS(ϑ0). Anal-
ogously, we define ˜C f S(ϑ0) = ˜ZS(ϑ0) ˜ZS(ϑ0)⊺/N(we drop the hat ˜ˆC f S to avoid cluttering notation), which corresponds to
˜C f S(ϑ0) =C f (ϑ0)−1/2 ˆC f S(ϑ0)Cf (ϑ0)−1/2. We call ˜C f S(ϑ0)thewhitened uncentered sample covariance of the function gradi-
ent at initialization.
Lemma D.6(Gaussian vectors [35, Prop. 2.2]).Letx∼ N(0,I d). Thenxis an exponentially-concentrated random vector.
Lemma D.7(Lipschitz stability of concentrated random vectors [35, Prop. 2.3]).Letx∈R d be an exponentially-concentrated
random vector, and letG:R d →R p be anL-Lipschitz function, whereLmay depend onp. Then the random vectorG(x)is
also exponentially concentrated.
Lemma D.8(Properties of whitened vectors).Under Assumption 5, letf ϑ be a parameterized quantum circuit as in Eq.(A4)
withK= 1, and let˜g i =C f (ϑ0)−1/2gi withg i =∇ ϑfϑ0 (xi)∈R p as in Def. D.5. For Gaussian normal inputsxi ∼ N(0,Id),
the vectors˜gi are independent, isotropic, and fulfill concentration of quadratic forms.
Proof.Consider the notation from Def. D.5. Then,Z S(ϑ0) = (g 1, . . . , gN )∈R p×N , and still ˆC f S(ϑ0) =Z S(ϑ0)ZS(ϑ0)⊺/N.
Since the training datax i are sampled i.i.d. andϑ 0 is fixed at initialization, it follows that the random vectorsg i are independent
among themselves. This implies that˜g i are also independent. We immediately have that the whitened random vectors are
isotropicE zi∼D [˜gi˜g⊺ i ] =I p, since
E
zi∼D
[˜gi˜g⊺ i ] =E zi∼D
h
Cf (ϑ0)−1/2gig⊺ i Cf (ϑ0)−1/2
i
=C f (ϑ0)−1/2 E zi∼D [gig⊺ i ]C f (ϑ0)−1/2 (D15)
=C f (ϑ0)−1/2Cf (ϑ0)Cf (ϑ0)−1/2 =I p.(D16)
Here, we have used thatC f (ϑ0)−1/2 =  Cf (ϑ0)−1/2⊺ is symmetric and does not depend onz i.
Since furtherx i ∼ N(0,Id), we know by Lemma D.6 that they are concentrated random vectors. For standard PQCs, the
mapx7→ ∇ ϑfϑ0 (x)is Lipschitz continuous, since the parameter-shift rule expresses gradient components as differences of
Lipschitz-continuous function evaluations. It therefore follows from Lemma D.7 that the function gradientsg i =∇ ϑfϑ0 (xi)
are also concentrated random vectors. Moreover, by construction,˜g i =C f (ϑ0)−1/2gi. SinceC f (ϑ0)−1/2 is a linear map
with bounded operator norm by Assumption 5, a second application of Lemma D.7 shows that the whitened vectors˜g i are
concentrated random vectors as well. Therefore, the concentration of quadratic forms follows from Lemma D.4.
Lemma D.9(Whitened-vector matrix converges to MP law).In the setting of Lemma D.8, the empirical spectral distribution of
the whitened uncentered sample covariance of the function gradient at initialization ˜C f S(ϑ0)converges weakly almost surely to
the Marˇcenko-Pastur law in the limit whereN, p→ ∞andp/N→γ.

17
Proof.Our strategy is to invoke Lemma D.2, which requires two conditions: independent, isotropic columns and concentration
of quadratic forms, which we confirm using Lemma D.8.
Corollary D.10(Smallest eigenvalue convergence for whitened vectors).The smallest non-zero eigenvalue of the whitened
uncentered sample covariance of the function gradient at initialization ˜C f S(ϑ0)converges almost surely to(1− p p/N)2.
Proof.Follows directly from Lemma D.9.
Lemma D.11(Smallest eigenvalue convergence for original vectors).In the setting of Lemma D.8, the smallest non-zero eigen-
value of the (original) sample covariance of the function gradient at initialization ˆC f S(ϑ0)achieves a minimum atN=p, in the
limit whereN, p→ ∞andp/N→γ.
Proof.We relate the eigenvalues of both sample covariance matrices: the whitened one and the original one. In both cases,
the smallest non-zero eigenvalues of the sample covariance matrixλ min( ˜C f S(ϑ0))correspond to the smallest non-zero singular
values of the matrix of function gradientsσ2 min( ˜ZS(ϑ0))(and analogously for ˆC f S(ϑ0)andZ S(ϑ0)). Using the identity ˜ZS(ϑ0) =
Cf (ϑ0)−1/2ZS(ϑ0), standard singular value inequalities (see, e.g., Ref. [55]) imply
σmin

˜ZS(ϑ0)

σmin

Cf (ϑ0)1/2

≤σ min (ZS(ϑ0))≤σ min

˜ZS(ϑ0)

σmax

Cf (ϑ0)1/2

.(D17)
By Corollary D.10,σ min

˜ZS(ϑ0)

converges to1−
p
p/Nwith high probability, which isσ min

˜ZS(ϑ0)

→0in the stated
limit ofp=N. From Assumption 5 it then follows thatσ min (ZS(ϑ0))→0in the same limit, thus achieving a minimum.
Lemma D.12(Adapted from Ref. [56]).LetK= 1,p≥N, and ˆϑS a local minimum as in Definition A.1. Under Assumption 3,
and considering the mean-squared error loss function, ˆϑS is a global minimum of the empirical risk
ˆϑS ∈arg min ϑ
h
ˆLS(ϑ)
i
.(D18)
Proof.We start with the definition of local minima:∇ ϑ ˆLS(ϑ) = 0. From the definition of the empirical risk, this becomesPN
i=1 ∇ϑℓ(zi, ˆϑS) = 0. We first use the chain rule∇ ϑℓ(zi, ˆϑS) =∇ ϑf ˆϑS (xi)∇f ℓ(zi, ˆϑS), and we note that, for the mean-
squared error lossℓ(z, ϑ) = (f ϑ(x)−y) 2/2, we have∇ f ℓ(z, ϑ) =f ϑ(x)−y. We introduce the vector of errors ˆES =
(f ˆϑS (xi)−y i)N i=1, and we re-write the sum overx i ∈Sas a matrix-vector multiplication, in order to get
NX
i=1
∇ϑℓ(zi, ˆϑS) =
NX
i=1
∇ϑf ˆϑS (xi)∇f ℓ(zi, ˆϑS) =
NX
i=1
∇ϑf ˆϑS (xi)(fϑ(xi)−y i) =Z S( ˆϑS) ˆES.(D19)
With this, the condition that ˆϑS is a local minimum becomesZ S( ˆϑS) ˆES = 0.
Assumption 3 dictates that, in the overparameterized regimep≥N, the sample Jacobian matrix fulfillsrank(Z S( ˆϑS)) =N
(is full rank). From this, it follows that the only possibility forZ S( ˆϑS) ˆES = 0to hold is that ˆES = 0. Since ˆES is the vector
of errors, it being zero means that the model makes no errors on the training set, which by definition implies the empirical risk
achieves its lowest possible value0. This confirms that ˆϑS is a global minimum of ˆLS.
Theorem C.3(Double descent peak at interpolation).LetS={(x i, yi)}N i=1 be a dataset withd-dimensional Gaussian normal
inputsx i ∼ N(0,Id)and outputsy i ∈R. Letf ϑ :R d →Rbe a parameterized quantum circuit as in Eq.(A4)forK= 1,
consisting ofpparameters. Under Assumptions 1–7, and considering the mean-squared error loss function, the lower bound on
L( ˆϑS)at a local minimum from Theorem B.9 attains a maximum atp=Nwith high probability in the limitN, p→ ∞with
fixed ratiop/N→γ.
Proof.Let us start from the lower bound in Theorem B.9, given by
L( ˆϑS)≥ L′(S) + 1 N+ 1 αξ2 minλmin(Cf ( ˆϑS)) λmin  ˆHS( ˆϑS)  +O  N −2 .(D20)
We first turn our attention to the decomposition of ˆHS( ˆϑS)from Lemma D.1: ˆHS( ˆϑS) = ˆH o S( ˆϑS) + ˆH f S ( ˆϑS). Then, we
apply the upper bound from Assumption 6:λ min

ˆHS( ˆϑS)

≤λ min

ˆH o S( ˆϑS)  +λ max  ˆH f S ( ˆϑS)  . Also, specializing to the

18
mean-squared error loss simplifies the expression for the outer-product Hessian, since the first derivative yields∇ f ℓ(zi, ϑ) =
(fϑ(xi)−y i)and the second derivative∇ f (fϑ(xi)−y i)) = 1. With these, we have
ˆH o S(ϑ) := 1 N
NX
i=1
∇ϑfϑ(xi)
h
∇f ∇⊺ f ℓ(zi, ϑ) i | {z }
=1
∇ϑfϑ(xi)⊺ = 1 N
NX
i=1
∇ϑfϑ(xi)∇ϑfϑ(xi)⊺ =: ˆC f S(ϑ).(D21)
The outer-product Hessian becomes the uncentered sample covariance of the function gradient. Substituting both this and the
inequality from Assumption 6 into the lower bound, we obtain
L( ˆϑS)≥ L′(S) + 1 N+ 1 αξ2 minλmin(Cf ( ˆϑS)) λmin  ˆC f S( ˆϑS)  +λ max  ˆH f S ( ˆϑS)  +O  N −2 .(D22)
With Assumption 4, we can further replace the ˆϑS dependence by the value of the parameters at initializationϑ 0, for some
constantsA, B >0, to get
L( ˆϑS)≥ L′(S) + 1 N+ 1 αξ2 minAλmin(Cf (ϑ0)) Bλmin  ˆC f S(ϑ0)  +λ max  ˆH f S ( ˆϑS)  +O  N −2 .(D23)
First of all, recall that the first term in both regimes,L′(S) =E z′∼D
h
ℓ(z′, ˆϑS′) i , denotes the add-one-in loss. Since it depends
on a training set perturbed by only a single sample, we do not expect its variation withpto dominate the Hessian-dependent
complexity term near interpolation.
Let us now consider the overparameterized regimep≥N. From Assumption 3 and Lemma D.12, for our choice of mean-
squared error loss, we have that ˆH f S ( ˆϑS) = 0. The denominator in the lower bound then becomes simplyBλ min

ˆC f S( ˆϑS)  .
Wielding Lemma D.11 we note thatλ min

ˆC f S( ˆϑS)  achieves a minimum atp=N, and hence it is an increasing function ofp
forp≥N. With this, we confirm that the lower bound ofL( ˆϑS)is decreasing in the overparameterized regime.
In the underparameterized regimep < N, the local minimum ˆϑS is not necessarily a global minimum of the empirical
risk, and hence both summands in the denominator of the lower bound remain. In this case, we combine Assumption 2 and
Lemma D.11 to argue that, withp < N, both summands are decreasing functions ofp. Forλ max

ˆH f S ( ˆϑS)  , Assumption 2
explicitly states this fact; and forλ min

ˆC f S(ϑ0)  , it followsλ min  ˆC f S(ϑ0)  having a minimum atp=N. We thus confirm that
the lower bound ofL( ˆϑS)is increasing in the underparameterized regime near interpolation. The last two paragraphs combined
complete the proof: the lower bound ofL( ˆϑS)has a maximum atp=N.
Appendix E: Upper bound
In this section we complement Theorems B.9 and C.3 with analogous results for anupper boundon the expected risk. We use
the same notation and language as in Appendices B and C.
Theorem E.1(Upper bound on the expected risk).Under the setting of Lemma B.5, under Assumption 1 and forK= 1, the
expected riskL( ˆϑS)at the local minimum ˆϑS fulfills the following upper bound:
L( ˆϑS)≤ L′(S) + 1 N+ 1 α ξ2 max R λmax(Cf ( ˆϑS)) λmin( ˆHS( ˆϑS)) +O  1 N 2  .(E1)
Here, we defineξ 2 max = max z∼D
ξ2 z >0 {ξ2 z },R= rank( ˆHS( ˆϑS)),λ min(·)the smallest non-zero eigenvalue of its matrix argument,
and analogously for the largest eigenvalueλ max(·).

19
Proof.The proof follows the steps of the proof of Theorem B.9, using the opposite direction of Lemma B.6,
L( ˆϑS) =L ′(S) + 1 N+ 1 Tr h ˆHS( ˆϑS) i−1 C( ˆϑS)  +O  1 N 2  (E2)
≤ L′(S) + 1 N+ 1  α ξ2 max Tr h ˆHS( ˆϑS) i−1 Cf ( ˆϑS)  +O  1 N 2  (E3)
≤ L′(S) + α ξ2 max
N+ 1

λmax(Cf ( ˆϑS)) Tr
h
ˆHS( ˆϑS)
i−1
+O
 1
N 2

(E4)
≤ L′(S) + α ξ2 maxλmax(Cf ( ˆϑS)) N+ 1  R λmin( ˆHS( ˆϑS)) ! +O  1 N 2  (E5)
=L ′(S) + 1 N+ 1 α ξ2 max R λmax(Cf ( ˆϑS)) λmin( ˆHS( ˆϑS)) +O  1 N 2  .(E6)
The only qualitative difference in this expression is in the trace of the inverse of the Hessian. This time, we upper bound a sum
of positive terms by the largest of the terms(λ min( ˆHS( ˆϑS)))−1 times the number of termsR. This concludes the proof.
Assumption 2’.In the underparametrized regimep < N K, the smallest eigenvalueλ min( ˆH f S ( ˆϑS))of the functional Hessian
at local minima decreases with the number of trainable parameterspin a neighborhood of the interpolation thresholdp=N K.
Assumption 4’.The largest eigenvalue of the uncentered covariance of the function gradients remains comparable to its value
at initialization, uniformly in the number of parametersp,λ max(Cf ( ˆϑS))≍λ max(Cf (ϑ0)). This relation holds with high
probability with respect to the random draw of the training setS, the initialization ˆϑ0, and the local minimum ˆϑS returned by
the training procedure.
Theorem E.2(Upper bound peak at interpolation).LetS={(x i, yi)}N i=1 be a dataset withd-dimensional Gaussian normal
inputsx i ∼ N(0,Id)and outputsy i ∈R. Letf θ :R d →Rbe a parameterized quantum circuit as in Eq.(A4)forK= 1,
consisting ofpparameters. Under Assumptions 1, 2’, 3, 4, 4’, and 5–7, and considering the mean-squared error loss function,
the upper bound onL( ˆϑS)at a local minimum from Theorem E.1 attains a maximum atp=Nwith high probability in the limit
N, p→ ∞with fixed ratiop/N→γ.
Proof.The proof follows the steps of the proof of Theorem C.3. We start from the upper bound in Theorem E.1, which is
L( ˆϑS)≤ L′(S) + 1 N+ 1 α ξ2 max R λmax(Cf ( ˆϑS)) λmin( ˆHS( ˆϑS)) +O  1 N 2  .(E7)
We first turn our attention to the decomposition of ˆHS( ˆϑS)from Lemma D.1: ˆHS( ˆϑS) = ˆH o S( ˆϑS) + ˆH f S ( ˆϑS). Then, we apply
the other direction of the inequality in Assumption 6, which is
λmin

ˆHS( ˆϑS)

≥λ min

ˆH o S( ˆϑS)  +λ min  ˆH f S ( ˆϑS)  .(E8)
Again, specializing to the mean-squared error loss simplifies the expression for the outer-product Hessian, we have ˆH o S(ϑ) =
ˆC f S(ϑ). Substituting both this and the inequality from Assumption 6 into the upper bound, we obtain
L( ˆϑS)≤ L′(S) + 1 N+ 1 αξ2 maxRλmax(Cf ( ˆϑS)) λmin  ˆC f S( ˆϑS)  +λ min  ˆH f S ( ˆϑS)  +O  N −2 .(E9)
With Assumptions 4 and 4’, we can further replace the ˆϑS dependence by the value of the parameters at initializationϑ 0, for
some constantsA, B >0,
L( ˆϑS)≤ L′(S) + 1 N+ 1 αξ2 maxRBλmax(Cf (ϑ0)) Aλmin  ˆC f S(ϑ0)  +λ min  ˆH f S ( ˆϑS)  +O  N −2 .(E10)
Let us now consider the overparameterized regimep≥N. From Assumption 3 and Lemma D.12, for our choice of mean-
squared error loss, we have that ˆH f S ( ˆϑS) = 0. The denominator in the lower bound then becomes simplyAλ min

ˆC f S( ˆϑS)  .

20
100 200 300 400
Number of parameters
0.1
0.2
0.3
0.4
λmax(Hf )
(a)
N=21
N=30
N=39
N=48
200 400 600
Number of parameters
100
200
300
400Jacobian rank
(b)
200 400 600
Number of parameters
10□7
10□4
10□1
102
Min. non-zero eigenvalue
(c)
After training
Initialization
Figure F.1. Numerical verification of the assumptions underlying the double descent analysis for the MNIST-1D dataset, for different training
set sizesN. Vertical dashed lines indicate the predicted interpolation thresholdsp=N K. (a) Largest eigenvalue of the functional Hessian
ˆH f S ( ˆϑS)after training. In the underparameterized regimep < N K,λ max( ˆH f S ( ˆϑS))decreases aspapproaches interpolation, supporting
Assumption 2. (b) Rank of the sample Jacobian of the functionZ S( ˆϑS)after training. Forp≥N K, the rank saturates atN K, supporting
Assumption 3. (c) Smallest non-zero eigenvalue of the uncentered sample covariance matrix of function gradientsˆC f S at initialization and after
training, supporting Assumption 4. The shaded areas correspond to the standard deviation for ten independent experiment repetitions, each
using independently sampled training data.
Wielding Lemma D.11 we note thatλ min

ˆC f S( ˆϑS)  achieves a minimum atp=N, and hence it is an increasing function ofp
forp≥N. With this, we confirm that the upper bound ofL( ˆϑS)is decreasing in the overparameterized regime.
In the underparameterized regimep < N, the local minimumˆϑS is not necessarily a global minimum of the empirical risk, and
hence both summands in the denominator of the upper bound remain. In this case, we combine Assumption 2’ and Lemma D.11
to argue that, withp < N, both summands are decreasing functions ofp. Forλ min

ˆH f S ( ˆϑS)  , Assumption 2’ explicitly states
this fact; and forλ min

ˆC f S(ϑ0)  , it follows fromλ min  ˆC f S(ϑ0)  having a minimum atp=N. We thus confirm that the upper
bound ofL( ˆϑS)is increasing in the underparameterized regime near interpolation. The last two paragraphs combined complete
the proof: the upper bound ofL( ˆϑS)has a maximum atp=N.
Appendix F: Further empirical evidence of double descent in PQCs
Complimenting our main numerical findings reported in Fig. 1, we now turn our attention to a selection of the assumptions
we introduced for Theorem C.3 in Appendix C. We present our results in Fig. F.1, where we probe further the mechanism
behind the double descent peak. Here, we focus on the MNIST-1D dataset. By systematically testing for different assumptions,
we strengthen the evidence that the peak at interpolation in Fig. 1 is accurately captured by our main analytical contribution,
Theorem C.3.
• In Fig. F.1(a) we test Assumption 2: in the underparameterized regimep < N K, the largest eigenvalue of the functional
Hessian,λ max( ˆH f S ( ˆϑS)), decreases as the number of parameters approaches the interpolation threshold. This indicates
that the contribution of the functional Hessian becomes less dominant near interpolation, as required in the proof of the
double descent peak.
• In Fig. F.1(b) we test Assumption 3: we show that, oncep≥N K, the rank of the sample Jacobian of the functionZ S( ˆϑS)
saturates atN Kfor all training-set sizes considered. Thus, in the overparameterized regime, the Jacobian has full rank
with respect to theN Kscalar training constraints.
• In Fig. F.1(c) we test Assumption 4: we compare the smallest non-zero eigenvalue of the uncentered sample covariance
matrix of function gradients ˆC f S at initialization and after training, displaying a dip near the interpolation threshold.
Appendix G: Further details on the numerical experiments
In this section, we provide further implementation details for the numerical experiments presented in Figs. 1 and F.1. All
quantum circuit simulations were performed with thePennyLanesoftware library [57], and all experiments usen= 8qubits
andK= 8output dimensions. The circuit consists of an initial angle embedding of the classical input, followed byLdata

21
re-uploading layers. Each layer contains trainable single-qubit rotationsR X,R Z, andR Y on every qubit, followed by nearest-
neighborCZgates arranged in a ring. The input is then re-uploaded before the next trainable layer. The model output is
obtained by measuring Pauli-Xexpectation values on the firstKqubits and multiplying the resulting vector by the fixed scale
factorc= 150. Since each layer contains three trainable parameters per qubit, the total number of trainable parameters is
p= 3nL. In the experiments, the depth is varied asL= 2, . . . ,25, corresponding top= 48, . . . ,600trainable parameters. All
models are trained with the mean squared error loss using the Adam optimizer, and the training is performed for2500epochs.
For the MNIST-1D and Fashion MNIST classification tasks, we use8classes. The labels are encoded as one-hot vectors and
subsequently mapped from{0,1}to{−1,1}, so that the correct class has value+1and all other classes have value−1. This
allows the classification tasks to be trained using the same mean squared error objective as in the theoretical analysis. Classical
inputs are reduced to dimensiond=n= 8using principal component analysis, implemented withscikit-learn[58],
and then rescaled component-wise to the interval[−π/2, π/2]before being passed to the angle embedding. For the synthetic
regression task, inputs are sampled uniformly from[−π/2, π/2] 8, and targets are generated from a multidimensional linear
modely=XW+ζ, whereWis the all-ones matrix inR 8×8 andζis Gaussian noise with standard deviation0.5.
To scan across the interpolation threshold, we vary the number of training samples asN∈ {21,30,39,48}. SinceK= 8, the
corresponding interpolation thresholds arep=N K∈ {168,240,312,384}. For each value ofNand each circuit depth, the
test loss is evaluated on1000test samples. These values are chosen such that the interpolation thresholds coincide exactly with
parameter counts attainable by varying the number of data re-uploading layers. The results are averaged over10independent
repetitions, and shaded regions in the figures indicate the standard deviation over these repetitions. The code is publicly available
in Ref. [51].
Appendix H: Universality classes of double descent
The proof of Theorem C.3 establishes the double descent peak by relating the smallest non-zero eigenvalue of the empirical
covariance matrix of function gradients to the soft edge of the Mar ˇcenko–Pastur law. This naturally raises the question of how
much of the phenomenon depends on the specific Wishart ensemble arising from independent Gaussian data, and how much is
instead a manifestation of a broader random-matrix universality principle.
Viewed abstractly, the proof relies on only two ingredients. First, the smallest non-zero singular value of the empirical
Jacobian develops a soft edge at the interpolation threshold. Second, the associated singular vectors are sufficiently delocalized
so that generic data directions overlap with them in a statistically uniform way. The specific Gaussian assumptions merely
provide one convenient realization of these properties.
A natural question is to what extent the present analysis depends on the specific Wishart ensemble underlying the Marˇcenko–
Pastur law. From the perspective of the proof, the essential ingredient is not Gaussianity itself but rather the emergence of a soft
spectral edge governing the smallest non-zero singular value of the empirical covariance matrix. This suggests that analogous
double descent behavior may persist for considerably broader classes of covariance ensembles. Prominent examples include
correlated Wishart ensembles, random kernel matrices, and deformed covariance ensembles [59–61]. More generally, nonlinear
kernel models whose limiting spectral measures differ from the classical Mar ˇcenko–Pastur law may provide a mathematically
natural framework for extending the present analysis beyond linearized parameterizations [28, 60]. These observations suggest
that the mechanism underlying Theorem C.3 should be understood as a manifestation of a broader universality class rather than
of a single random matrix model.
Conjecture H.1(Universality of double descent).Consider the setting of Theorem C.3, replacing the Gaussian Wishart covari-
ance model by a random covariance ensemble whose smallest non-zero singular value exhibits universal soft-edge behavior and
whose singular vectors remain asymptotically delocalized. Then the lower bound on the expected risk exhibits an interpolation
peak at the corresponding critical aspect ratio, giving rise to double descent behavior.
Establishing the precise universality class governing double descent in parameterized quantum circuits, and identifying which
structural properties of the underlying random matrix ensemble are genuinely required, constitute interesting open problems.
