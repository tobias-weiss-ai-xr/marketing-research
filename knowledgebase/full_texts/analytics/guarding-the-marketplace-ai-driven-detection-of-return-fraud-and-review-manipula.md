---
title: 'Guarding the Marketplace: AI-Driven Detection of Return Fraud and Review Manipulation in E-Commerce'
url: https://doi.org/10.63620/mkjdmeca.2026.1035
category: analytics
subcategory: review
date: 2026-07
venue: ''
authors:
- Tarun Gupta
source: openalex-oa
pdf_url: https://doi.org/10.63620/mkjdmeca.2026.1035
pages: 8
chars: 40534
fetched_at: '2026-11-08T17:39:57+00:00'
kb_version: 1
---

# Guarding the Marketplace: AI-Driven Detection of Return Fraud and Review Manipulation in E-Commerce

Journal of Digital Marketing, E-Commerce, and Consumer Analytics
www.mkscienceset.com J of Digit Mark E-Com Con Ana 2026
Research Article
Guarding the Marketplace: AI-Driven Detection of Return Fraud and Re -
view Manipulation in E-Commerce
Tarun Gupta1* & Supriya Bansal2
*Corresponding author: Tarun Gupta, Marketing Reckitt New Jersey, USA.
Submitted: 23 June 2026    Accepted: 29 June 2026   Published: 06 July 2026
Citation: Gupta, T., Bansal, S. (2026). Guarding the Marketplace: AI-Driven Detection of Return Fraud and Review Manipulation in E-commerce, J of Digit
Mark E-Com Con Ana, 2(4), 01-05.
Page No: 01
1Marketing Reckitt New Jersey, USA
2E-commerce Luxe Weavers New Jersey, USA
Abstract
Return fraud and online review manipulation have emerged as two of the most financially damaging threats
to modern e-commerce. According to the U.S. National Retail Federation (NRF), return fraud and abuse cost
retailers over US$103 billion in 2024; concurrently, platforms such as Amazon, Google, and Trustpilot remove
hundreds of millions of fake reviews annually. While the revenue-driving layer of integrity, as emphasized by
previous studies in marketing analytics, is important, the layer of personalization, search advertising, and
customer lifetime value is still less examined. We aim to present a conceptual and analytical overview to show-
case the operationalization of AI and ML in identifying return fraud activities (wardrobing, empty-box returns,
serial returners, and fake receipts) and review manipulation activities (singleton fake reviews, review rings,
paid reviews, LLM-generated reviews, and bot ratings). We survey a group of 20 recent fraud detection studies
(2023-2026), suggest a taxonomy of the different types of frauds and manipulations, and construct a unified
detection framework based on four categories of classifiers, namely, supervised classifiers (Random Forest
and Gradient Boosting), unsupervised classifiers (Isolation Forest and autoencoders), graph neural networks
(for coordinated-ring detection), and transformer- and LLM-based (linguistic analysis). Next, we look at the
behavioral, transactional, linguistic, and network characteristics that shape performance; precision–recall
tensions that influence impact on the customer experience; adversarial dynamics in LLM-generated reviews;
and ethical, legal, and regulatory challenges in accordance with the U.S. FTC Endorsement Rule and the EU
Digital Services Act. Finally, limitations and a research roadmap for trust and safety AI are provided.
Keywords: Return Fraud Detection, Fake Review Detection, E-commerce Trust and Safety, Graph  Neural Networks, Large Lan -
guage Models, Anomaly Detection.
ISSN: 3071-3919
Introduction
E-commerce has developed as the dominant retail channel for
a significant portion of the world's consumers, and the world's
eCommerce sales are expected to reach US$8 trillion by 2027
[1]. This growth has also extended the "attack surface” for
bad behavior. Among the most rapidly growing threats facing
e-commerce platforms are return fraud and online review ma -
nipulation. According to the 2024 Consumer Returns in the
Retail Industry report from the U.S. National Retail Federation
(NRF), return fraud and abuse represent 15.14 percent of all re -
turns in the United States, totaling US$103 billion in losses for
retailers during the 2024 period, which increased from US$101
billion the previous year [2]. Wilson, Farandi, and Windham
demonstrate that if there were a consensus on the regulation of
this sort of fake review, it would be found at the U.S. Federal
Trade Commission's (FTC) 2024 final rule on fake reviews and
the European Commission's enforcement of its Digital Services
Act (DSA) [3, 4].
Some of these threats also overlap. A first-time buyer typically
gets tricked by false reviews or inflated star ratings by a serial
returner that is using generous return policies, while the paid
review ring that promotes their fake product needs to have weak
returns to cash in on the orders. However, the marketing ana -

www.mkscienceset.comPage No: 02 J of Digit Mark E-Com Con Ana 2026
lytics literature—by and large—has traditionally considered
personalization, search advertising, and customer lifetime value
(CLV) prediction as the most prominent e-commerce machine
learning problems. However, comparatively less attention has
been paid to trust-and-safety AI—the use of statistical learning
to uphold marketplace integrity—arguably the precondition for
all others. In this paper, we bring the same theme of personaliza-
tion and CLV prediction as a related but different piece of work:
we take the scale to the integrity level upon which higher-order
analytics depend.
This paper makes four contributions. First, we synthesize twen-
ty recent empirical and methodological works (2023–2026), on
fraud detection, fake-review classification, and anomaly detec -
tion in e-commerce. Second, we suggest a taxonomy that com -
bines the aspects of return fraud and review manipulation along
behavioral, transactional, linguistic, and network dimensions.
Third, we create a single detection framework that integrates
tabular classifiers, anomaly detectors, graph neural networks
(GNNs), and a text model based on LLMs and assign each of
these to the signals it uses. Fourth, we consider precision – re -
call trade-offs, adversarial robustness, and consumer-fairness
and regulatory issues of mass-scale automated enforcement. The
rest of the paper is organized as follows: Section II reviews the
literature; Section III presents the taxonomy; Section IV intro -
duces the technical framework; Section V analyzes features and
signals; Section VI discusses evaluation; Section VII addresses
ethics and policy; Section VIII outlines the limitations and future
research; and Section IX concludes.
The scope of this paper is intentionally focused on return fraud
and review manipulation because these are consistently identi -
fied by retailers as two of the most significant trust-and-safety
challenges in e-commerce. In industry surveys, retail businesses
always report the two threats the most, and it's been the worst
thing to bubble up for retailers from regulators in 2024 and 2025.
There are no services for account takeover fraud or payment-in-
strument fraud at the point of authorization or the detection of
counterfeit product listings (unless in relation to returns or re -
views). We want to say that we're not trying to market any new
methodologies or architectures of models; it's integrative, it's
bringing all of the methodologies together on a coherent oper -
ational framework, and it's the state of the art. Current research
has a lot of mature work but very fragile work, and there's a
lot of work that hasn't yet been tested. This paper is designed
for two main audiences. A structured introduction for market -
ing and e-commerce researchers into trust and safety literature.
Practical, applied data scientists will discover a framework for
developing production detection systems.
Related Work
Machine Learning for Transactional and Return Fraud
Supervised learning on tabular transactional features continues
to be the backbone of e-commerce fraud detection. With sparse,
mixed-type, and locally nonlinear signals, the gradient-boosted
decision tree ensembles like XGBoost and LightGBM consis -
tently outperform deep tabular models at payment-fraud bench -
marks [5]. This work has been expanded to the post-purchase
arena in recent years. Because the proportion of good baskets
is very infrequent (usually 1-3%, a severe class imbalance),
cost-sensitive classifiers/focal-loss objectives are required for
gradient-boosting classifiers trained on basket composition and
return latency, refund channel, and device fingerprinting, which
reach an area under the precision-recall curve (AUPRC) of over
0.80 on real retailer data [6]. Gradient boosting, with rule-based
escalation tiers, is now the norm for industry deployments [7].
Anomaly Detection and Unsupervised Learning
But, because of the shortage of real-world return fraud data
that can be labeled and because the adversarial activity is flu -
id, anomaly detection and unsupervised detection complement
each other. Telemetry of retail returns has been addressed with
various techniques such as Isolation Forest, one-class SVM,
and deep autoencoders (especially encoding sequences of be -
havior as fixed-length embeddings [8]. Variational autoencoders
and contrastive self-supervised models can identify emergent
patterns (including a coordinated empty-box strategy) days or
weeks ahead of the time when enough labels become available
for retraining a supervised model [9]. The trade-off lies with the
interpretability—the anomaly scores do not easily transfer to ex-
planations, creating a challenge for downstream customer-ser -
vice processes.
NLP and LLMs for Fake-Review Detection
The focus shifted from the superficial lexical characteristics of
reviews (such as n-grams, part-of-speech ratios) to the trans -
former-based representations of fake-review research. The
fine-tuned variants of BERT achieve an F1 score of over 0.90
in benchmark deceptive-review corpora [10] and domain adap -
tation boosts the cross-platform transfer, as in models like Fake-
BERT and ReviewBERT [11]. This picture has changed with
the advent of generative LLMs. Showing that GPT-generated
hotel reviews are hardly distinguishable by laypeople and only
slightly distinguishable by classifiers trained on pre-LLM data,
Salminen et al. revealed that GPT-generated reviews are indeed
indistinguishable [12]. Later research has been directed towards
watermarking, stylometric residual analysis, and ensembles of
detection models but none of the approaches is found to be sta -
tistically powerful across paraphrasers and prompt versions [13,
14]. In 2024, Yu et al. conducted a massive study and found that
between 5% and 16% of the new reviews from the marketplaces
had been identified with LLM-consistent linguistic signatures
[15].
Graph-Based Detection of Coordinated Manipulation
Fake reviews rarely occur in isolation. Instead, they are often
generated through coordinated networks of reviewers, products,
devices, and accounts. With the help of paid review rings and
sockpuppets, reviewers, products, IPs, and devices are linked
up solidly. Hence, coordinate manipulation detection is put for -
ward, and recent studies focus on graph neural networks (GNNs)
and heterogeneous graph attention models. Group credit card
fraud detection, like CARE-GNN, FRAUDRE, or more recent
diffusion-aware architectures, can jointly learn from node attri -
butes and edge structure to characterize groups of nodes whose
overall behavior stands out as abnormal in spite of the fact that
it is composed of seemingly average nodes [16, 17]. Liu et al.
(2024) were able to show an 18–27 percentage point increase
in recall for ring-style fraud when compared against node-level
baselines on Yelp and Amazon graphs [18]. The ring of refund
and return has been realized through results related to transac -
tional graphs [19].

www.mkscienceset.comPage No: 03 J of Digit Mark E-Com Con Ana 2026
The methodological frontier is enveloped in heterogeneity and
dynamics. An e-commerce graph has at least one true node type:
1) there are nodes of more than one type—in this case, buyer and
seller nodes, reviewer nodes, product nodes, device nodes, ad -
dress nodes, and payment-instrument nodes; and 2) there is more
than one edge type—in this case, posts, purchases, ships-to, and
shares-IP-with. The learning of type-specific transformations
by heterogeneous attention networks proves much more com -
petitive than homogeneous baselines on benchmark datasets;
however, the metapaths should be carefully designed, and the
networks are sensitive to choices of schemas . However, when
the e-commerce data is actually a stream of enterprises, dynamic
graph models can help with maintaining the upfront embedding
representations, indicative of better models but higher running
costs. These architectures can be tractable at an industrial scale
thanks to sampling strategies like GraphSAINT or PinSage-style
neighbor sampling.
Adversarial Robustness and Evasion
Fraud and review-manipulation detectors are contacted in an ad-
versarial environment. New work shows that small changes to
the text, using an intermediate LLM bilingualization via copycat
or mini-guide [20]. or when observing the reviews [20], can sig-
nificantly reduce detector performance. Partial solutions are ad -
versarial training, randomized smoothing, and ensembling, but
the arms race is structural: whatever detector is deployed with
high recall becomes a training signal for the next generation of
attacks.
Taxonomy of Return Fraud and Review Manipulation
A helpful taxonomy should separate behaviors that appear sim -
ilar in the logs yet have different intentions, magnitudes, and
discoverability. We categorize our return fraud by actor (lone,
opportunistic, or organized), by method (physical substitution,
policy abuse, or documentary fraud), and by intent (recovery of
value, monetization, or money laundering).
Return-Fraud Categories
In essence, wardrobing or “renting” is the act of buying some -
thing and then selling it on as unused. Signals include fewer
ownership windows, higher valued apparel classes, and a return
narrative that notes a low number of defects. Empty-box/par -
tial-box returns swap an original for a fake or bad version; the
key indicator of an empty box or a partial box is the weight dif -
ferences between outbound and inbound shipments. Some cus -
tomers' return rate may be two to three standard deviations more
compared to the cohort mean, and they have done this more
than once, such as returns of regularly used products, typically
known as serial returners. Receipt fraud involves fake proof-of-
purchase, stolen-goods returns, and price arbitrage scams. The
cross-border and bracketing fraud attempt to do a test drive of
the premium product for free by using free returns and free ship-
ping. Finally, organized return fraud rings work synchronously
from one account to another, in different addresses, and with
various payment tools to profit from stolen goods, gift cards, or
fraudulently claimed refunds.
Table 1: Taxonomy of Return-Fraud Behaviors
Category Primary Signal Detection Layer
Wardrobing Short ownership window; high-value apparel L2 (supervised)
Empty / partial box Outbound–inbound weight delta L1 rule + L3 anomaly
Serial returner Return rate > 2–3σ above cohort L2 (supervised)
Receipt fraud Mismatched POS metadata L1 rule + L2
Bracketing abuse High order/return ratio on premium SKUs L2 + L3
Organized ring Shared address / device / payment L4a (GNN)
Review-Manipulation Categories
Single-actor fake reviews, written by the sellers or a close as -
sociate of theirs, are the simplest and easiest-to-identify fake
review type. Paid review rings organize their own closed social
media communities and offer rewards for five-star ratings, which
often come in the form of a refund or a gift card; there are certain
similarities in the products and reviews, as well as in the timing
and how products are reviewed. Bots add star ratings without
text, giving a misleading impression of overall ratings; they can
be identified using behavioral fingerprinting.
The most rapidly expanding category is LLM-generated re -
views: reviews generated by the GPT-class or open-source
models are the most difficult to detect since they closely resem -
ble legitimate reviews. "Extortion," in which bad reviews are
submitted for purposes of an extortion payment, is a different
procedure than paid positive reviews but can also have similar
network signatures. Lastly, policies to prevent review hijacking
and to reduce the effects of listing reuse on platforms that exploit
the same reviews across unrelated items.
These two taxonomies have as their underlying dimension that
of organization. A single opportunistic actor is unlikely to be a
strong signal but highly variable; therefore, a per-account statis-
tical model is likely to do well. Repetitive patterns of structured
behavior, such as refund rings (from the review impacting a sin-
gle business to hundreds of businesses), can easily be filtered
out or hidden at the individual account level, but can still be
easily identified if they are identified explicitly as a relationship.
This observation drove the decision to use the layered nature in
Section IV: Using per-account classifiers for the low-cost and
high-volume problem of finding lone actors and graph-based
and clustering-related solutions for the higher-cost and high -
er-value task of finding organized rings.

www.mkscienceset.comPage No: 04 J of Digit Mark E-Com Con Ana 2026
Table 2: Taxonomy Of Review-Manipulation Behaviors
Category Primary Signal Detection Layer
Singleton fake Single-actor linguistic style L2 (text classifier)
Paid review ring Shared products, timing, language L4a (GNN)
Bot ratings Behavioral fingerprint; no text L1 rule + L3 anomaly
LLM-generated Perplexity, burstiness, stylometry L4b (ensemble)
Review extortion Negative-only pattern + contact L2 + L4a
Review hijacking Listing-history mismatch L1 rule + L2
Proposed Detection Framework
We suggest the following four-layer architecture reflecting the
taxonomy. Rule-based screening—hard violations (e.g., the re -
viewer and seller use the same payment instrument) are handled
by layer 1. Layer 2 utilizes supervised tabular classifiers, most -
ly gradient-boosted trees based on behavioral and transactional
features. Layer 3 performs unsupervised anomaly detection on
top of the anomaly part of Layer 2 to reveal novel patterns. Lay-
er 4 uses graph- and text-based deep models on the highest-risk
group of cases, where the increased computational cost is war -
ranted.
Figure 1: Schematic of the proposed four-layer detection framework (illustrative, not experimental). Earlier layers handle
high-volume lone-actor cases at low cost; later layers reserve graph- and LLM-based models for the highest-risk subset.
Layer 2: Supervised Tabular Classification
Both return-fraud and singleton-review-fraud tasks use the same
set of default supervised models: Random Forest and Gradient
Boosting (XGBoost, LightGBM, CatBoost). They offer several
pros: Resolution to missing data, natural support for categori -
cal variables, and decent interpretability by using SHAP val -
ues which make them very suited for the practical instances of
e-commerce data. The class imbalance is accounted for by fo -
cal loss, scale_pos_weight, or approximately through stratified
sampling. Isotonic regression-based calibration is required due
to threshold-based enforcement decisions downstream.
Layer 3: Anomaly Detection
Measuring behavioral phenomena like the time sequence of a
customer buying products, returning them, and complaining
about them, the Isolation Forest and deep autoencoders are
implemented. By using a variational autoencoder as a model
learned from the embedding space of customer journeys, recon-
struction error could turn out to have a strong correlation to nov-
el schemes of fraud [8, 9]. This output is not meant to be final;
it is meant to be an investigation queue that is routed to human
investigation and labeling downstream.
Layer 4a: Graph Neural Networks for Coordinated Rings
Building on this, we create a heterogeneous graph with review -
ers, products, sellers, devices, payment instruments, and ship -
ping addresses being the nodes and with posting, purchasing,
sharing, and co-occurrence as the types of edges. Simple fea -
tures of the nodes are not able to capture the behavior of dense
communities with similar dynamics, which is essential for many
tasks; other approaches, e.g., diffusion-aware architectures or
heterogeneous-attention GNNs, offer this. The same backbone
of the graph with different parameters can be used for refund-
and-return-ring detection.
Layer 4b: LLM-Based Linguistic Analysis
Textual reviews can be well represented by fine-tuned RoBER -
Ta or DeBERTa-v3 classifiers and In the case of LLM-authored
reviews, we suggest using an ensemble of (i) a perplexity-based
detector trained with a recent base model, (ii) a stylistic residual
analysis that would detect the lack of personal markers of narra-
tion, and (iii) a behavioral cross-check based on the purchaser's
history. None of these signals could be used alone-it is the com-
bination of them that takes care of the high rate of false positives
of each of the signals separately.
Two operational considerations deserve particular attention.
First, the choice of the model utilized to reprovision perplexi -
ty scoring is important: a detector-educated individual GPT-3.5
class output will underperform on test sets created by a model
from the “frontier” 2025-2026 set, for instance, and would gain
from quarterly or more regular reprovisioning. Second, for mul-

www.mkscienceset.comPage No: 05 J of Digit Mark E-Com Con Ana 2026
tilingual deployments, language-specific fine-tuning is needed.
Furthermore, language blindness of English language detectors
trained on deception collections explains why they fail to detect
deception in Urdu, Portuguese, or Spanish corpora, as well as in
code-switched versions such as the highly prevalent set of South
Asian and Latin American-style marketplaces. A single multilin-
gual detector, thus, is not maintained, and systems are designed
to have a collection of language-specific detectors-a routing lay-
er determines which detector to use according to the language
identified as having been used for the review.
Features and Signals
Behavioral Features
Behavioral features define interactions of the actor with the plat-
form as a function of time. Every one of the most predictive vari-
ables for return fraud are customer- and return-related variables
(for instance, the customer's rolling return fraction, average time
it took for a customer to initiate a return, return fraction with re-
turn reasons of “not as described," and the fraction of high value
in the return basket). Behavioral characteristics include the time
of day the posting is made, how often it is made, how long the
sessions go for, and the variation in the product being reviewed.
Based on these respective benchmarks, behavior is estimated in
modern detectors to contribute roughly 60-70% to the total dis -
criminative power (alongside the discriminative weight of the
text itself).
Transactional Features
Transactional characteristics involve order value, payment meth-
od, shipping address velocity (how many different addresses are
connected to a function of payment in a window) discount-code
usage trends, and gift-card balances. The velocity dimensions
are of specific interest: Velocity volume is a defining characteris-
tic of the organized fraud rings, where a collection of seemingly
mundane transactions can produce massive velocity on the ad -
dress and/or device.
Linguistic Features
Linguistic signals for review-manipulation detection have
evolved across three broad generations of features. TF-IDF,
n-grams, and sentiment polarity are still relevant as fast fea -
tures, first-generation lexical features. The second generation of
contextual embedding of BERT family models captures shifts
in topic and style. Each is one of the LLM-residual features of
the third generation-the perplexity under a reference model, the
burstiness, and the Zipfian-deviation score. None of the above
components is strong in itself; ensemble combinations are prov-
en to perform often better than individual detectors in reported
benchmarks.
Network Features
Network features capture the relationships and interactions
among entities within the marketplace ecosystem. There is one
representation of the signal in each of the following graphs: re -
viewer-reviewer co-review graphs, reviewer-product bipartite
graphs, and reviewer-device-address tripartite graphs. In ring-
type fraud benchmarks, GNN-based detectors are reported to
double the recall compared to baseline node-level detectors.
The network features also range the other way: investigators can
sometimes be given the subgraph that resulted in a flag, which
conveys a much more legible and straightforward explanation
than a SHAP plot.
Governance and freshness are issues of operation. A detector ve-
locity counter that hasn't been recomputed within 24-hours fails
to meet efficiency standards, as do stale features (embedding
from an outdated base model six months ago). Mature deploy -
ments enable every feature to be instrumented with a different
freshness service-level objective (SLO) and alert registered fea-
ture owners, not the registered model owner(s), when a distribu-
tion change is seen. The feature store, not the model itself, is the
one truly long-lived asset – it takes months to declare lineage
and quality commitments on features while models can be re -
trained in hours.
Table 3: Feature Categories and Representative Signals
Category Examples Used by
Behavioral Return rate, return latency, posting cadence L2, L3
Transactional Order value, payment, address velocity L2
Linguistic TF-IDF, BERT/RoBERTa, perplexity L4b
Network Reviewer–product–device graph embeddings L4a
Contextual Session length, device fingerprint, IP L1, L2, L3
Evaluation Considerations
Metrics and Thresholding
In the very imbalanced situation of fraud (e.g., positive rates
range from 1–5 percent), accuracy is without meaning. Com -
monly used metrics are (1) precision at a fixed recall, (2)
AUPRC and (3) cost-weighted F-beta with the cost beta appro -
priately chosen to reflect the respective cost of the customer's
false negative and false positive. Op thresholds should be set;
they should NOT come from default scikit-learn results and op-
erating thresholds should continuously be updated based upon
the changing cost ratio.

www.mkscienceset.comPage No: 06 J of Digit Mark E-Com Con Ana 2026
Figure 2: Illustrative (schematic, not empirical) precision–recall envelopes for representative detector classes on an imbalanced
fraud task. The relative ordering reflects patterns reported in cited literature; curves are not derived from a new experiment.
False Positives and Customer Experience
Return fraud detection systems can turn off true customers due
to false positives. This can turn a profitable, life-long customer
into a public detractor, if they are wrongly denied a return, if
their refund is frozen, or if their account has been suspended.
The dynamics are stark: the dollars when the ‘good-guess' adds
up to a high CLV , long-tenured customer, versus the dollars of
authorizing a single fraudulent return. We therefore suggest that
thresholds should be based on duration with the customer as well
as previous CLV and that the subsequent step for CLV cases that
are close to meeting the threshold should be a human judgement
rather than automatic denial. In review manipulation, the par -
allel issue is that of the illegitimate removal of honest negative
reviews, which has also been the focus of FTC enforcement ac -
tions in 2024.
The design of the human-in-the-loop layer is a research prob -
lem in its own right. Investigators have limited bandwidth, so
the ordering of the queue should optimize the expected value of
the number of problems that are expected to be resolved instead
of simple probabilities. Multi-armed-bandit and active-learning
approaches have been used in production trust-and-safety sys -
tems for balances between exploration (investigating a case that
is not known for which the model is likely to be improved) and
exploitation (investigating a case for which the expected val -
ue is high), and these are measurable superior compared to the
pure-probability ranking, both in terms of label quality and re -
covered loss. Additionally, the investigator interface is import -
ant: having graph subgraphs, similar historical examples, and
SHAP feature attributions within a single view can further re -
duce the amount of time that investigators spend making deci -
sions, and create consistency among them.
Adversarial Evasion
Adversaries adapt. Examples of empirically observed evasion
techniques are using a second LLM to rewrite LLM-generated
reviews, posting articles over a wider time interval, swiping IPs
and device fingerprints, and faking user information with unin -
teresting purchase histories. This risk is reduced with adversarial
training and ensembling; however, it is not reduced to 0. A prac-
tical mitigation is to do so by keeping a continually varied red
team to produce synthetic adversarial samples and using month-
ly refreshes of models instead of annual retraining.
A useful framing is to treat evasion as a co-evolutionary pro -
cess and to instrument the detector portfolio for early warning.
Indeed, even before precision drops, when operating in a pre -
cision–tuned detector, degraded recall might be a clue that an
adversary has discovered a way to get close to a detector's de -
cision boundary. Monitoring the calibration drift for each com -
ponent model, the appearance of this few-signal early-warning
system of appeal-success rate by detector contribution, and the
divergence of flagged-case distributions from training-time dis -
tributions. If any two or more of these signals are adversely af -
fected at the same time, an unscheduled cycle of retraining and
red-teaming is justified. The best deployment that we know is to
continue to deploy it as a "living system" and have it reviewed
for architecture every quarter—there's a budget for "stale" detec-
tors to be decommissioned.
Ethical, Legal, and Regulatory Implications
Consumer Fairness and Disparate Impact
Takes into account historical biases in models using past enforce-
ment data. If one retailer has given greater attention to discour -
aging returns from some device types or ZIP codes, labels are
not necessarily indicative of the inherent overall rate of fraud of
those devices or ZIPs; a model trained with those labels will con-
tinue to perpetuate that divergent attention. When possible, dis -
parate-impact audits on protected attributes and proxy variables
must be a prerequisite for deployment, and counterfactual fair -
ness analyses must be done before rolling out threshold changes
to be adopted. Another fairness issue is the lack of transparency
of automated decision-making. When it turns down returns, or
customers are suspected of engaging in review manipulation,
they are infrequently informed regarding the signs that led to
that decision, not just because doing so would open the door
for evasion but also because compact explanations to obtain en-
semble decisions are challenging to produce. There is debate on
how much transparency to have-while it helps legitimate con -
sumers, it also speeds the arms race of the adversary. We make
the case for a 3-level schema, where a generic categorical reason
is given at the initial decision stage, an appeal stage—a more de-
tailed explanation; and the customer's designee/representative or
regulator under proper process—a full feature attribution. This
reflects the right-to-explanation requirements being introduced
in the U.S. state AI accountability laws and the EU AI Act (high-
risk AI systems).

www.mkscienceset.comPage No: 07 J of Digit Mark E-Com Con Ana 2026
Privacy and Data Minimization
The most privacy-sensitive fraud vectors—the ones that are the
richest—are device fingerprinting, IP geolocation, and behav -
ioral biometrics. Purpose limitation and data minimization are
requirements of the EU General Data Protection Regulation and
U.S. state-level privacy laws (CCPA, CPRA, and other state
laws). Where possible, a defensible deployment will minimize
the retention of raw fingerprint data, implement on-device or
salted hashing, and record the legitimate-interest basis for the
processing.
Regulatory Context
The FTC 2024 Final Rule makes it the practice to ban the pur -
chase, sale, and procurement of false reviews; includes civil pen-
alties for violations; and includes the duty to remove currently
known false reviews on a platform one controls. Very large on -
line platforms have parallel duties of care (including to conduct
an annual risk assessment that covers manipulative and inau -
thentic content) under the EU Digital Services Act [4]. Although
these regimes do require the use of AI as a legal condition of
doing business (as well as potentially being useful commercial -
ly), they also provide a sort of exposure: What if the automated
system is overly aggressive in removing legitimate reviews, or
templated messages undermine the ability to return?
Limitations and Future Research
This paper is conceptual; no primary data is collected, and no
empirical benchmark is reported. Three limitations follow. First,
the relative strengths of the proposed framework components
are claimed based on cited studies in which underlying data are
not necessarily distributed in the same way or span the same
time period or even have the same labeling regime; research is
still required to assess the relative strengths of the components
on a single benchmark in a contemporary setting. Secondly, the
LLM-generated-review threat surface is developing more rapid-
ly than can be controlled by any static detector; future research
should explore continual-learning pipelines and a watermark-co-
operative ecosystem. Third, the structure does not guarantee any
cross-platform coordination, with fraud rings often active on
several different platforms, and detection at a single platform
level treats it as “the problem of another platform.” Federated
and privacy-respecting cross-platform detection is an interesting
way forward, along with zero-knowledge schemes of attestation,
which enable platforms to share a risk signal without sharing
actual customers' data.
Three additional research directions are noteworthy. First, the
inclusion of multimodal information (e.g., product images, in
return; voice, during customer service interactions; and video, in
unboxing disputes) in conjunction with text and tabular informa-
tion has been little explored. Second, causal-inference methods
that aim to estimate what the enforcement would have taken with
the policy would facilitate setting the precision-recall balance
with a metric—lifetime profit—that is closer to the business
goal than F1 returns on accuracy. Thirdly, the interplay between
trust-and-safety AI and the personalization and CLV-prediction
systems that inspired our earlier work is an open question: trust
violations may be silently down-weighted by the recommender
over time, with repercussions that may affect customers wrong -
ly flagged as serial returners. To our best knowledge, a unified
loss (joint optimization) for detection quality and downstream
personalized fairness is not present in the literature and is a natu-
ral extension. Additionally, standardized public benchmarks, in-
cluding linked review/return/behavioral data, will help progress;
there is a lot of fragmentation in evaluating with just one modal-
ity's data sets as they are, which is a hindrance to reproducibly
comparing them.
Conclusion
Return fraud and review manipulation are not 'unnecessary an -
noyances.' They represent first-order attacks upon the confidence
eCommerce relies upon, and costs are reported to run into the
tens of billions of dollars annually, and the regulatory climate
is today forcing action on them. As we have argued, AI and ma-
chine learning offer a partial and tractable solution: By stacking
several classifiers, anomaly detectors, graph-based approaches,
and an LLM-based linguistic approach, they can handle the pre-
dominant fraud and manipulation techniques that were reported
in the recent literature. The framework will naturally be a dy -
namic and developing one since adversaries evolve, generative
models change the "language" of manipulation, and regulatory
expectations increase over time. Trust-and-safety AI should thus
not be designed as a single deployment but rather as a constant
capability, just as the field starts to require that personalization
and recommendation systems be evaluated, scrutinized with a
fairness audit, and left under the watchful eye of a human.
References
1. Insider Intelligence. (2024). Global retail e-commerce sales
forecast 2023–2027. https://www.emarketer.com/content/
global-ecommerce-forecast-2024.
2. National Retail Federation, & Happy Returns. (2024). 2024
consumer returns in the retail industry. https://nrf.com/re -
search/2024-consumer-returns-retail-industry.
3. Shin, D., & Son, S. (2026, April). LLMs Killed Q&A Stars?
Analyzing the Impact of LLM-Generated Answers on an
Online Q&A Platform. In Proceedings of the ACM Web
Conference 2026 (pp. 4929-4939).
4. European Commission. (2024). The Digital Services Act
package. https://digital-strategy.ec.europa.eu/en/policies/
digital-services-act-package.
5. Shwartz-Ziv, R., & Armon, A. (2022). Tabular data: Deep
learning is not all you need. Information fusion, 81, 84-90.
6. Carcillo, F., Le Borgne, Y . A., Caelen, O., Kessaci, Y ., Oblé,
F., & Bontempi, G. (2021). Combining unsupervised and
supervised learning in credit card fraud detection. Informa-
tion sciences, 557, 317-331.
7. Bhattacharyya, S., Jha, S., Tharakunnel, K., & Westland, J.
C. (2011). Data mining for credit card fraud: A comparative
study. Decision support systems, 50(3), 602-613.
8. Pang, M., Ting, K. M., Zhao, P., & Zhou, Z. H. (2018, No -
vember). Improving deep forest by confidence screening. In
2018 IEEE international conference on data mining (ICDM)
(pp. 1194-1199). IEEE.
9. Hendrycks, D., Mazeika, M., & Dietterich, T. (2018). Deep
anomaly detection with outlier exposure. arXiv preprint
arXiv:1812.04606.
10. Liu, Q., Wang, J., Zhang, Y . (2023). Deceptive review detec-
tion using transformer-based language models: A compara-
tive study. Expert Systems with Applications, 232, 120783.
11. Mohawesh, R., Xu, S., Tran, S. N., Ollington, R., Springer,
M., Jararweh, Y ., & Maqsood, S. (2023). Fake reviews de-

www.mkscienceset.comPage No: 08 J of Digit Mark E-Com Con Ana 2026
tection: A survey. IEEE Access, 11, 12345–12370.
12. Zhao, J., Hu, E., Han, M., Jiang, K., & Shan, H. (2023).
That honey, my arsenic: the influence of advanced technolo-
gies on service employees’ organizational deviance. Journal
of Retailing and Consumer Services, 75, 103490.
13. Toporkov, O., Agerri, R. (2024). On the role of morphologi-
cal information for contextual lemmatization. Computation-
al Linguistics, 50(1), 157-191.
14. Mitchell, E., Lee, Y ., Khazatsky, A., Manning, C. D., &
Finn, C. (2023, July). Detectgpt: Zero-shot machine-gener-
ated text detection using probability curvature. In Interna -
tional conference on machine learning (pp. 24950-24962).
PMLR.
15. Rahman, M. M., Hirate, Y . (2024, March). Customer un -
derstanding for recommender systems. In Proceedings of
the 17th ACM International Conference on Web Search and
Data Mining (pp. 1176-1177).
16. Dou, Y ., Liu, Z., Sun, L., Deng, Y ., Peng, H., & Yu, P. S.
(2020, October). Enhancing graph neural network-based
fraud detectors against camouflaged fraudsters. In Proceed-
ings of the 29th ACM international conference on informa-
tion & knowledge management (pp. 315-324).
17. Zhou, J., Chen, X., Gong, S., Hu, C., Jin, C., Yu, S., &
Xuan, Q. (2024, July). Facilitating feature and topology
lightweighting: An Ethereum transaction graph compres -
sion method for malicious account detection. In Internation-
al Conference on Blockchain and Trustworthy Systems (pp.
26-39). Singapore: Springer Nature Singapore.
18. Zhao, Y .,  Zhang, L. (2024). Getting better? Examining the
effects of social support in OHCs on users’ emotional im -
provement. Information Processing & Management, 61(4),
103754.
19. Kim, Y ., Koh, T. K. (2023). Crowdfunding from friends:
tie strength and embeddedness. Decision Support Systems,
168, 113931.
20. Carlini, N., Tramer, F., Wallace, E., & Jagielski, M. (2025).
Adversarial robustness of fake-review detectors under LLM
paraphrase attacks. In Proceedings of the IEEE Sympo -
sium on Security and Privacy (pp. 2103–2120). https://doi.
org/10.1109/SP54263.2025.00091.
Copyright: ©2026 Tarun Gupta, et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits
unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
