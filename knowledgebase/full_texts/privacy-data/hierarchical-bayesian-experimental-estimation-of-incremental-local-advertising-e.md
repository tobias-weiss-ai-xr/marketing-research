---
title: Hierarchical Bayesian Experimental Estimation of Incremental Local Advertising Effects with Secure
  Aggregation and Differential Privacy
url: https://doi.org/10.21203/rs.3.rs-11122128/v1
category: privacy-data
subcategory: empirical
date: 2026-09
venue: Research Square
authors:
- Que Yang
- Yukun Du
- Yuang Hu
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-11122128/latest.pdf
pages: 9
chars: 24850
fetched_at: '2026-11-08T17:46:27+00:00'
kb_version: 1
---

# Hierarchical Bayesian Experimental Estimation of Incremental Local Advertising Effects with Secure Aggregation and Differential Privacy

Hierarchical Bayesian Experimental Estimation of
Incremental Local Advertising Effects with Secure
Aggregation and Differential Privacy
Que Yang 
Carnegie Mellon University, Pittsburgh, 15213, United States
Yukun Du 
University of Chicago, Chicago, 60637, United States
Yuang Hu 
Carnegie Mellon University, Pittsburgh, PA 15213, United States
Research Article
Keywords: local business advertising, differential privacy, regional randomized experiments, hierarchical
Bayesian models, incremental conversions, advertising effectiveness measurement
Posted Date: September 23rd, 2026
DOI: https://doi.org/10.21203/rs.3.rs-11122128/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: The authors declare no competing interests.

Hierarchical Bayesian Experimental Estimation of Incremental Local Advertising
Effects with Secure Aggregation and Differential Privacy
Que Yang
 *
Carnegie Mellon University, Pittsburgh, 15213, United States, quey@alumni.cmu.edu
Yukun Du
University of Chicago, Chicago, 60637, United States, yukundu@uchicago.edu
Yuang Hu
Carnegie Mellon University, Pittsburgh, PA 15213, United States, yuangh@alumni.cmu.edu

Abstract
Local commercial advertising measurement on a U.S. digital media platform is comp utationally
constrained by sparse campaign -level conversions, the attribution bias of last -click rules, and privacy
restrictions that limit the availability of user-level behavioral data.A paired-area randomized experimental
framework was implemented for 1,860 local businesses across 12 U.S. states, covering  4,720 advertising
campaigns, 1.26 billion impressions, 19.4 million website visits, and 2.18 million purchase or appointment
records.The computational pipeline uses Z -score normalization, KD -tree candidate retrieval,
Mahalanobis-distance matching, and a SHA -256-derived random seed for paired -area assignment;
regional weekly records are then processed through secure aggregation and a Gaussian differential privacy
mechanism with ε = 2 and δ = 10⁻⁶. On the privacy -protected regional statistics, a hierarchical Bayesian
negative binomial inference module was constructed with business, industry, metrop olitan area, and ad
placement week modeled as four random-effect levels.The likelihood explicitly incorporates the recorded
privacy-noise variance, enabling the inference of incremental conversions and in cremental return on ad
spend without treating privacy -perturbed counts as noise -free observations.Experimental evaluation
showed that the proposed computational framework reduced the mean absolute err or of incremental
conversions from 71.4 for the standard difference -in-differences baseline to 43.6, achieved 91.2%
coverage for the 90% interval, and reduced the absolute error of incremental return on ad spend from 0.39
to 0.17.For campaigns with fewer than 500 conversions, hierarchical informatio n sharing reduced the
minimum detectable effect from 8.6 to 5.9 percentage points and the med ian posterior standard deviation
from 0.084 to 0.061; Gaussian privacy perturbation introduced an ad ditional error of 6.3 conversions,
while 83% of enterprise -level budget decisions remained unchanged.The resulting framework integrates
regional randomized co mputation, secure aggregation, differential privacy, hierarchical Bayesian
inference, and posterior decision rules into a privacy -preserving advertising measurement pipeline for
incremental-effect estimation and budget optimization.
CCS CONCEPTS:
Information systems~Information systems applications~Multimedia information sys tems~Multimedia
content creation
Keywords
local business advertising; differential privacy; regional randomized experiments; hierar chical Bayesian
models; incremental conversions; advertising effectiveness measurement
1 Introduction
Digital advertising is now a way for local businesses to reach people in the area, expan d their online
market, and spend marketing funds. Local restaurants, retailers, healthcare institutions and home -service
companies are generally characterised by low advertising investment, few conversion indicators and short
campaign cycles. The old model of last-click attribution cannot distinguish between ad-driven conversions
and organic demand, and thus often overstates the incremental effect. At the same time,  user -level
behavioural tracking is increasingly subject to privacy restrictions. Although sec ure aggregation and

differential privacy can reduce the risk of individual data leakage, they add noise and weaken the statistical
identification capability for small -sample campaigns; thus, this paper selects the U.S. local business
advertising measurement scenario. A zip -code-level paired randomised experiment is employed as the
foundation for identification, and a Bayesian negative binomial estimation framework in corporating
secure aggregation, differential privacy noise correction and multi-layer parameter sharing is constructed.
We focus on the joint inference of incremental conversions, incremental retur n on ad spend (ROAS) and
budget allocation under privacy -disturbed conditions. By conducting model comparison, privacy -
sensitivity tests, and small -sample identification a nalysis, this paper verifies the applicability of the
framework in terms of estimation accuracy, interval calibration and decision stabilit y, and provides a
statistical basis for evaluating the effectiveness of local business advertising and optim ising lim ited
budgets in a privacy-preserving environment.
2 Analysis of Local Commercial Advertising Effectiveness Evaluation Under Privacy Constraints
Local advertising uses the postal area –week as the computational unit, with the advertising group
  and the control group   . The 4 -dimensional matching vector includes population size,
historical sales, industry category, and ad spend[1] . The event-level purchase or reservation count
exhibits a concentration of zero values, variance greater than the mean, and inter -week correlation, while
the secure aggregation interface can only return noisy statistics:
   (1)
 where  represent the company, matched region, and ad placement week, respectively;
is the accessible count;  is the potential conversion volume under the processing state; and
and   are the privacy noise and its variance, respectively.Thus, two measures — incremental
conversions and incremental returns on advertising — need to be determined over a four -level hierarchy
that includes companies, industries, metropolitan areas, and ad pl acement weeks, thus providing
constraints for subsequent paired sampling, noise correction, and stratification[2] .
3 Design of a Stratified Experimental Estimation Method for Incremental Advertising Effectiveness
Under Privacy Constraints
3.1 Advertising Effect Sampling Method Based on Paired Regional Randomized Experiments
The sampling module uses postal areas as randomization units and creates separate pools for each of
the nine ad categories, such as food and beverage. The three continuous va riables — population size,
historical sales, and advertising spending — are standardized with Z -scores, and industry categories are
defined as exact -match constraints; a KD -tree retrieves the top 5 candidates, and the top 1 is selected
according to Mahalanobis distance, so that the matching process can be completed  in 1: 1 without
substitution. The system extracts the 64-bit SHA-256 hash of the campaign ID as a random seed, assigning
  as the ad zone and   as the control zone.Only 5 fields are left in the sample table:
Enterprise ID, Campaign ID, Area ID, Week ID, and Processing Flag. To avoid  duplication of locations
and cross regions, a regional hash index is used [3]. In order to v isually illustrate the differences between
the different types of advertisements, Figure 1 illustrates nine typical advertising ima ges. Subsequent
counts are aggregated by region and week in the Security Aggregation module.
1=Z 0=Z
0NY
) , 0 ( ~ , ) (~ 2 DP  N Z Y Yipt ipt ipt ipt ipt+ =
t p i、 、 iptY~
) (ipt iptZ Y ipt
2
DP
1=pZ 0=pZ

Figure 1: Examples of 9 Categories of Local Commercial Advertisements
3.2 Method for Generating Differential Privacy Statistics Based on Secure Aggregation
A three level index is set up for outgoing records according to treatm ent group, post area p, and
placement week t. The local nodes encode impressions, visits,  conversions, and ad spend into 64, 4
dimensional fixed point vectors, and perform L2 contribution truncation at the user – week level [4]. A
256-bit key is used by each node to negotiate and produce paired masks, the sum of which is expressed as:
   (2)
where s  is the regional weekly aggregation vector,  is the number of shards participating in
the calculation,  is the sum of truncated contributions within shard  , and  is the random mask
shared by shards   and   ; positive and negative masks cancel each other out during summation,
preventing the server from reading data from individual shards. After ag gregation is complete, statistics
are published using a Gaussian mechanism:
   (3)
where  is the noisy output,  is the Gaussian noise,  is the upper bound on user contribution
sensitivity,  is the 4×4 identity matrix,  is the noise multiplier, and  and  are the privacy budget
and failure probability, respectively.The system uses a Rényi differential privacy co unter to accumulate
weekly queries, constraining the total budget to ε = 2 and δ = 10 − 6, while preserving C, σ, and the noise
covariance. The negative noise value is not truncated so that the full error distribution is reproduced in the
probability function [5].
3.3 Hierarchical Bayesian Estimation Model Incorporating Privacy-Preserving Noise Correction
The model reads the noisy conversion volume  and the noise variance  from the output, sets
  
=  
      − + = K k k k k k kpt pt 1 m m a s    
pts K
kpta k km
k 

    ) / 25 . 1 ln( 2), I , 0 ( ~ , s s~ 4 2 2  + =C Npt pt pt pt
pts~ pt C
4I   
iptY~ 2 ptw

the unperturbed count  as a discrete latent variable, and constructs a negative binomial count layer and
a Gaussian privacy observation layer:
   (4)
where  represent the company, matched region, and campaign week, respectively;  is
the latent conversion mean;  is a discrete parameter; and  ;  are read from
the differential privacy metadata. The count mean adopts a 4-level hierarchical structure:
   (5)
In this model,   represents the exposure bias term,   represents the population intercept,
 represents the treatment label,  represents the population advertising effect,  represents
the firm-level random slope, and  and  represent the standardized covariates and their coefficients,
respectively;  andst` denote the random intercepts for firm, industry, metropolitan area,
and advertising week, respectively. Let ; the remaining random effects follow a zero-
mean normal prior, with standard deviations following a half -t prior.The model uses decentralized
parameters and NUTS sampling, runs 4 chains, with 4,000 iterations per chain  and a warm-up of the first
2,000 iterations; the target acceptance rate is set to 0.90. From the same posterior sample, co unterfactual
conversion volumes are generated by setting  and  , respectively, to compute incremental
conversions and the probability of budget decisions[6] .
3.4 A Method for Evaluating Advertising Decisions Based on Posterior Inference
Using 8,000 sets of posterior samples retained from four NUTS chains, and holding the firm, region,
week, and covariates constant, we set the treatment variable to  and  , respectively. We
then use two-stage vectorization inference to generate the latent mean conversions for the advertising and
natural states. The firm-level evaluation metric is defined as:
   (6)
where  is the a posteriori sample index;  and  represent the two latent means for
firm   in region   and week   ;   is the local increment;   is the cumulative incremental
conversions;  is the conversion value;  is the ad spend; and  is the incremental return on ad
spend. Budget actions are determined by minimizing a posteriori risk:
   (7)
where   ,   include four actions: increase, maintain, reduce, and stop, and   is the
budget misallocation loss function. The decision engine outputs the 5th, 5 0th, and 95th percentile at the
same time; the budget is increased when the posterior probability of the return is  not less than 0.90, and
the 90 per cent confidence limit is  greater than 0; when the probability is between 0.60 and 0.90, it
decreases when the probability is less than 0.60, and stops when the probability is not lower than 0.90 [7].
Figure 2 illustrates the execution process of posterior reasoning, counterfactual generation, risk assessment,
and action output.
iptY
) , ( ~~), , NB( ~ 2 pt ipt ipt ipt ipt iptw Y N Y Y Y 
t p i、 、 ipt
 / = ) Var(2 ipt ipt ipt+μ μY 2 ptw
t i m i h i ipt p i ipt ipts w v u Z b (αEμ + + + + x + ) + + log = log) ( ) ( T  +
iptE α
 1 , 0pZ  ib
iptx 
) ( ) (i m i h iw v u、 、
)Σ(0,～) ( 2 T b i iN ,b u
1=pZ 0=pZ
1=pZ 0=pZ
i
t p
s
ipt ipts
i
t p
s
ipt
s
i
s
ipt
s
ipt
s
ipt
AR  = =  − = ,
) (
) (
,
) ( ) ( ) ( ) ( ) (, ), 0 ( ) 1 (      
s ) 1 () (s ipt ) 0 () (s ipt
i p t ) (s ipt ) (s i
ipt iA ) (s iR
( )
=
  =
S
s
s
i
s
iA ai R a LSa 1 ) ( ) (, ,1max arg
8000=S A ()L

Figure 2: Process for Evaluating Incremental Advertising Effectiveness and Budget Decision-Making
Based on Posterior Inference
4 Experimental Results and Analysis
4.1 Construction of the Experimental Dataset and Setting of Evaluation Metrics
The experimental data come from 1,860 local businesses in the 12 U.S. states, and  these four
industries are: food service, retail, healthcare and home repair. A total of 4,720 advertising campaigns have
been run, with 1.26 billion impressions, 19.4 million  website visits and 2.18 million purchase or
appointment records. On average, each business has about 2.54 campaigns, and each campaign has around
266,900 impressions, 4,110 visits and 462 conversions. The con version rate of impressions to visits was
1.54%, and the conversion rate of visits to purchases or appointments was 11.24%. The data had a small
sample size at the campaign level and cross -industry imbalances. All records were grouped by company
ID to prevent leakage of activities from the same company  across sets, and independent regional
experiments were used as the basis for effect calibration; weekly regional statistics were gen erated using
a Gaussian differential privacy mechanism with ε=2 and δ=10⁻⁶. Evaluation metrics included the mean
absolute error (MAE) of incremental conversions, 90% posterior interval cover age, absolute error in
incremental return on ad spend, minimum detectable effect (MDE), median posterior  standard deviation,
additional error from privacy noise, and budget decision consistency rate. For the small -sample analysis,
MDE was evaluated for campaigns with fewer than 500 observed conversions us ing the 8,000 retained
posterior draws. The detectable-effect threshold was determined from the posterior distribution under the
same positive-effect criterion used for posterior decision inference, so that MDE and posterior uncertainty
were evaluated on a common probabilistic scale [8].
4.2 Comparison of Performance Between the Stratified Bayesian Model and Baseline Methods
Using the same weekly statistics for paired regions and enterprise-level data segmentation, we tested
the standard double-difference model and the stratified Bayesian negative binomial model proposed in this
paper, with incremental conversions measured in independent regional experiments as the reference. The
results show that the mean absolute error (MAE) of incremental conversions dec reased from 71.4 for the
standard difference -in-differences model to 43.6 for the hierarchical Bayesian model, an absolut e
reduction of 27.8 and a relative reduction of 38.9% . The absolute error in incremental return on ad spend
decreased from 0.39 to 0.17, corresponding to a 56.4% reduction. T hese point -error measures were
considered jointly with posterior dispersion in the small -sample analysis rather than being interpreted
independently, allowing the reduction in estimation error to be assessed together with the ch ange in
posterior uncertainty; and the 90% confidence interval coverage rate of the model in this paper is 91. 2%,
which is 1.2 percentage points lower than the theoretical uncovered level of 10.0 %. The above results
show that four-level parameter sharing across enterprises, industries, metropolitan areas and ad placement
weeks can reduce the estimation variance of sparse events, and the negative binomial likelihood effectively

handles the highly discrete nature of conversion counts [9-10]. Specific results are as follows: Table 1
Table 1: Comparison of Estimation Performance Between the Hierarchical Bayesian Model and the
Baseline Method
 Evaluation Metrics  Reference Method or Nominal Value  Model in This Paper  Absolute Change Relative Change
 Conversion Increment
MAE/Iteration
 71.4 (standard double
difference)  43.6  −27.8  −38.9%
 Absolute error in incremental
return on ad spend
 0.39 (ordinary double
difference)  0.17  −0.22  −56.4%
 90% Confidence Interval
Coverage / %  90.0 (nominal level)  91.2
 +1.2
percentage
points
 —
4.3 Analysis of the Impact of Differential Privacy Mechanisms on Estimation Performance
We compared the results of the regional weekly statistics for 4,720 advertising  campaigns under
conditions without privacy perturbation and those with Gaussian differential privacy (ε=2, δ=10⁻⁶). Given
the privacy constraints, the model's incremental conve rsion MAE was 43.6 times, and an additional error
of 6.3 times was added due to privacy noise; without noise, the MAE was 37.3 times. After adding the
privacy mechanism, the error increased by 16.9% compared with the no -noise case, but it was still lower
than the 71.4 times obtained by a standard double-difference model. In terms of budget output, 83% of the
companies kept their original budget retention or adjustment decisions, and only 17% changed their actions;
thus, the noise variance correction in the likelihood function did not directly alter the advertising effect
parameters. Both the increase in error and the stability of the decision can  be shown in Figure 3: the left
side shows the change in error from 37.3 to 43.6, and the right side s hows that 83 % of the companies
maintained their conclusion while only 17% changed it. Therefore, we will now investigate the problem
of privacy noise amplification in low-conversion campaigns.

Figure 3: Impact of the differential privacy mechanism on incremental estimation error and budget
decision stability
4.4 Analysis of Small-Sample Ad Campaign Performance Identification and Budget Optimization
For advertising campaigns with fewer than 500 conversions in the observ ation period, the non -
hierarchical and hierarchical estimators were evaluated on the same campaign subset, paired  regional
weekly statistics, covariates, differential -privacy setting of  ε=2 and δ=10⁻⁶, and posterior evaluation

procedure. The comparison therefore changed the hierarchical informatio n-sharing component while
holding the underlying observations and privacy conditions fixed, avoid ing differences in sample
composition from affecting the MDE comparison.Under this match ed evaluation setting, the MDE
decreased from 8.6 percentage points without hierarchical information sharing  to 5.9 percentage points
with hierarchical sharing, corresponding to an absolute reduction of 2.7 p ercentage points and a relative
reduction of 31.4%. Because both estimators were evaluated on the same low -conversion campaigns and
privacy-protected regional statistics, the reduction reflects the change in the information-sharing structure
rather than a change in campaign composition or privacy budget.The median posterior standard deviation
decreased from 0.084 to 0.061, an absolute reduction of 0.023 an d a relative reduction of 27.4%. In
variance terms, the corresponding squared posterior dispersion decreased  from 0.00706 to 0.00372, a
reduction of approximately 47.3%. Together with the reduction in MDE from 8.6 to 5.9 percentage points,
this result indicates that hierarchical information sharing reduced posterior dispers ion without obtaining
the lower uncertainty by imposing a higher detectable -effect threshold. The result therefore characterizes
the error –variance trade -off as a simultaneous improvement in small -sample detection sensitivity and
posterior concentration.  Budget optimisation no longer relies on a single -point estimate; instead, the
posterior median, 5th and 95th percentiles, and the probability of achieving return targets are fed into four
action classifiers—increase, maintain, reduce, and stop —to reduce budget misallocation in small-sample
campaigns caused by short -term conversion spikes. Figure 4 jointly presents the change in MDE and
posterior uncertainty: hierarchical information sharing reduced the MDE from 8.6 to 5.9 percentage points
while reducing the median posterior standard deviation from 0.084 to 0.061,  providing a joint view of
detection sensitivity and posterior dispersion under the same small-sample setting.

Figure 4: Comparison of Performance Identification Capabilities and Posterior Uncertainty in Small-
Sample Advertising Campaigns
5. Conclusions
Evaluating the effectiveness of local commercial advertising under privacy constrain ts requires
striking a balance among data availability, statistical reliability, and individual privacy protection. Based
on a hierarchical Bayesian estimation framework th at incorporates regional randomized experiments,
secure aggregation mechanisms, and fusion noise correction, this method achieves stable identification of
incremental effects in scenarios with small sample sizes and highly discrete conversion s, and further
supports budget adjustment decisions through posterior inference.This m ethod overcomes the reliance of
traditional attribution models on user-level behavioral data, providing an interpretable statistical approach
to ad measurement in privacy-protected environments. However, the regional randomized design remains
limited by external market changes, cross -regional spillover effects, and scalability across industry

heterogeneity. Future research could incorporate dynamic experimental data over lon ger time periods,
introduce time -varying causal structures, and employ multi -source privacy -preserving computation
mechanisms to further enhance the adaptability and decisio n accuracy of incremental ad effect
identification in complex market environments.
References
[1] Barrientos A F, Williams A R, Snoke J, et al. A feasibility study of differentially private summary
statistics and regression analyses with evaluations on administrative and survey data[J].  Journal of the
American Statistical Association, 2024, 119(545): 52-65.
[2] Zhang Y , Xu Q, Tang N, et al. Differentially private data release for mixed-type data via latent
factor models[J]. Journal of Machine Learning Research, 2024, 25(116): 1-37.
[3] Samartsidis P, Seaman S R, Harrison A, et al. A Bayesian multivariate factor analysis model for
causal inference using time-series observational data on mixed outcomes[J]. Biostatistics, 2024, 25(3):
867-884.
[4] Ye T, Westling T, Page L, et al. Nonparametric identification of causal effects in clustered
observational studies with differential selection[J]. Journal of the Royal Statistical Society Ser ies A:
Statistics in Society, 2024, 187(4): 1013-1036.
[5] Guo Q, Barrientos A F, Peña V . Differentially private methods for compositional data[J]. Journal
of Computational and Graphical Statistics, 2025, 34(3): 848-858.
[6] Imbens G, Kallus N, Mao X, et al. Long-term causal inference under persistent confounding via
data combination[J]. Journal of the Royal Statistical Society Series B: Statistical Methodology,  2025,
87(2): 362-388.
[7] Kallus N, Mao X. On the role of surrogates in the efficient estimation of treatment effects  with
limited outcome data[J]. Journal of the Royal Statistical Society Series B: Statistical Methodology, 2025,
87(2): 480-509.
[8] Yu P, Jiang Y , Su Z, et al. Differentially Private Bayesian Envelope Regression via Sufficient
Statistic Perturbation[J]. Journal of Data Science, 2026, 24(1): 187.
[9] Runge J, Pauwels K. Open -source media and marketing mix modeling: Practice -oriented
overview, challenges, opportunities[J]. Customer Needs and Solutions, 2026, 13(1): 3.
[10] Luo J, Qin H, Xu Z. Differential privacy statistical inference for a directed network model with
covariates[J]. Journal of Systems Science and Complexity, 2026, 39(3): 1285-1305.
