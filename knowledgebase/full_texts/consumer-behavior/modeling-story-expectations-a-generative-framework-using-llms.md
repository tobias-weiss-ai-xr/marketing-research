---
title: 'Modeling Story Expectations: A Generative Framework using LLMs'
url: https://arxiv.org/abs/2412.15239
category: consumer-behavior
subcategory: empirical
date: 2024-12
venue: ''
authors:
- Hortense Fong
- George Gui
- Bo Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2412.15239
pages: 45
chars: 113131
fetched_at: '2026-11-08T13:14:09+00:00'
kb_version: 1
---

# Modeling Story Expectations: A Generative Framework using LLMs

Modeling Story Expectations:
A Generative Framework using LLMs
Hortense Fong George Gui Bo Yang ∗
May 2026
Abstract
Consumers’ engagement with stories is shaped by their expectations about what will happen next, yet modeling
these forward-looking beliefs over unstructured narrative content has remained challenging. We develop a framework
that uses large language models to approximate consumers’ story expectations. Our method generates multiple
imagined story continuations from a pre-trained LLM and extracts interpretable, theory-motivated features from these
continuations, such as emotion and narrative path features. We propose two complementary validation procedures
suited to different data availability: a survey-based approach that compares LLM-derived expectations to human-
reported beliefs, and a rational-expectations approach that compares them to actual story outcomes. Applying the
framework to both survey data collected in a controlled lab setting and observational data from an online reading
platform, we find that LLM-derived expectations correlate with human-reported beliefs as well as actual story
continuations along all features studied. In both settings, forward-looking expectations are associated with reader
engagement above and beyond features of the content already consumed. Our framework provides a scalable method
for modeling consumer beliefs about narrative content, with implications for content creation, platform strategy, and
the study of narrative media.
∗Columbia Business School, Hortense Fong (hf2462@gsb.columbia.edu), George Gui (zg2467@gsb.columbia.edu), Bo Yang
(BYang30@gsb.columbia.edu). We thank researchers whose comments and suggestions have greatly improved the paper. We also thank Yut-
ing Deng, Raelynn Li, Riccardo Risi, Angela Qianya Wang, and Duoji Jiang for exceptional research assistance.
1
arXiv:2412.15239v4  [cs.CL]  13 Jul 2026

1 Introduction
Consumers around the world spend a large part of their free time consuming narrative media, whether in the form of TV
shows, films, books, podcasts, or narrative-driven social content. For example, U.S. consumers spend around 12 hours
a day consuming media, and at least half is on media typically presented in narrative (i.e., story) form. 1 Despite the
significant time allocation and size of the entertainment and media market, it is notoriously difficult for book publishers
and television and movie studios to predict what content will be successful (Waldfogel, 2018). We posit that part of
the challenge is that story engagement decisions depend in part on consumers’ expectations, which have historically
been challenging to elicit or model. This research develops a framework that leverages large language models (LLMs)
to model consumers’ forward-looking expectations for narrative content.
Modeling consumers’ forward-looking expectations allows us to explore audiences’ preferences over anticipated
content. How do consumers’ expectations affect engagement decisions? Why are some stories page turners? Why
do some stories generate a lot of buzz? These are questions of great interest to authors and screenwriters, as well
as publishers and platforms. For content creators, anticipating consumers’ expectations and knowing what affects
engagement can help creators design more engaging stories. For publishers and platforms, this information can help
improve marketing decisions, such as pricing and advertising.2
However, modeling consumers’ forward-looking expectations over narratives is challenging because expectations
are rarely observed, and approximating them typically requires surveys of the target audience or modeling assumptions.
Neither is straightforward in the context of stories. Surveying expectations along one or two dimensions is feasible, but
eliciting a full distribution of possibilities over how a story might unfold is cost-prohibitive. Modeling assumptions is
also difficult. In structured settings, empirical modelers often assume rational expectations and model beliefs about a
future low-dimensional outcome, such as next period’s price, as a conditional distribution given past low-dimensional
outcomes, such as past prices. For stories, the analogous move would require modeling how the distribution of possible
continuations, a high-dimensional object, depends on the story so far, which is also a high-dimensional object. There
is no obvious starting point for doing so.
To overcome these challenges, we introduce a novel framework that takes advantage of the vast knowledge base of
LLMs to model consumers’ expectations in stories. Our framework is made up of four components: story imagination,
feature extraction, validation, and analysis. In the story imagination component, we use a pre-trained LLM to generate
story continuations. Trained using the text of thousands of books,3 LLMs can predict many probable story continuations
from some initial text. For example, providing the LLM with the text from the first chapter, we can ask it to predict
the text of the next chapter. Furthermore, we can ask it to generate not just one continuation but a distribution of
continuations. The feature extraction component converts moments of this distribution into interpretable features
that are motivated by theories from narratology, psychology, and marketing. Our proposed method complements
1https://www.marketingcharts.com/television-236479
2For example, emotional state is known to moderate consumer response to ads (Goldberg and Gorn, 1987) and certain emotional states, such as
hope, dread, and fear, depend on consumer expectations.
3It is speculated that GPT-4 is trained on over 125,000 books. Source: https://aicopyright.substack.com/p/has-your-book-been-used-to-train
2

these theories and their associated feature-engineering approaches by examining not only how the original features
are associated with engagement, but also how expectations of those features help explain engagement. The validation
component assesses whether the previous two components can reasonably model consumers’ expectations. We propose
two validation procedures. The first is a standard survey-based approach that compares LLM-derived expectations
against human-reported beliefs. The second is a rational expectations-based approach that compares LLM-derived
expectations against actual story continuations. Finally, the analysis component presents a framework to interpret the
association between expectation and engagement, highlighting the challenge of studying it causally and the need for
extensive exploration of different story elements before making causal claims. The first three components are about
modeling expectations, while the fourth component generates a set of hypotheses attempting to link the narrative
features with engagement.
We apply our method to two complementary empirical settings using survey data and observational data. The
survey setting provides a controlled environment with cleaner data and direct measures of participants’ beliefs, allowing
us to validate whether our expectation-modeling procedure provides a reasonable proxy for consumers’ next-chapter
expectations. The observational setting captures real stories and organic engagement patterns, allowing us to assess
whether the procedure is consistent with rational expectations. We find that current LLMs provide imperfect but
informative proxies for consumers’ beliefs. LLM-derived expectations correlate with human-reported beliefs as well as
actual story continuations across all features studied. Forward-looking expectations are also associated with engagement
in both settings. In the survey, expected arousal predicts stated interest in continuing and the decision to read the next
chapter, whether expectations are elicited from readers or derived from imagined continuations. In the observational
data, LLM-derived expectations of all fifteen features we examine are significant predictors of the realized chapter
features, and expected valence, arousal, speed, and circuitousness are associated with voting and commenting rates.
Furthermore, we use LLM-derived expectations to assess the sensitivity of these focal relationships to other narrative
features, illustrating how the framework can sharpen subsequent causal questions and inform survey design.
The rest of the paper is organized as follows. Section 2 overviews the relevant literature we build from and
contribute to. Section 3 introduces the general framework, detailing our approach to modeling expectations in
unstructured narrative data. We then demonstrate our method using both survey and observational data in Sections
4 and 5, respectively. We discuss alternative ways to operationalize our framework in Section 6. Finally, we discuss
our main findings in Section 7 and conclude in Section 8. We hope that by addressing the challenges of modeling
expectations in unstructured narrative data, this paper can serve as a starting point for empirical researchers to explore
and formulate new hypotheses about how consumer beliefs drive their behavior in contexts involving stories.
2 Relevant Literature
This paper relates to three streams of literature: 1) narrative features, 2) consumers’ forward-looking expectations,
and 3) using large language models (LLMs) for market research. Researchers across marketing, narratology, computer
science, and psychology have made progress in extracting features from story text that predict narrative engagement
3

or success (Piper et al., 2021). However, these methods primarily describe content already consumed rather than what
readers expect will happen next. Much of this work focuses on emotion, building on the premise that entertainment is
fundamentally an emotional experience (Tan, 2008). Berger and Milkman (2012) demonstrate that positive emotions
and high-arousal emotions in news stories causally drive sharing behavior. Berger et al. (2023) extend this to sustained
attention, finding that the effects of emotional language on continued reading are driven by the degree to which discrete
emotions evoke arousal and uncertainty. Others find that the emotional flow of narratives predicts engagement and/or
success (Nabi and Green, 2015; Maharjan et al., 2018; Knight et al., 2024, 2025). Beyond emotion, researchers
have also extracted features related to semantic path (Toubia et al., 2021), story elements (Eliashberg et al., 2007;
Shachar et al., 2025), character types (Bamman et al., 2014), character traits (Toubia et al., 2019), and antecedents to
narrative transport (Van Laer et al., 2014). Our paper extends this literature by adding a forward-looking dimension:
modeling what readers expect will happen next, alongside what has already happened in the story. Our proposed
method complements existing feature construction methods by applying the feature extraction not only to the actual
story text, but also to imagined story continuations generated by a large language model.
This framework rests on the premise that what readers expect, not just what they have read, shapes engagement. In
economics and marketing, models of consumer decision-making recognize that consumers form beliefs about future
states from currently available information and act on those expectations. Friedman (1957) assumes that consumers
make consumption decisions based not only on current income but also on beliefs about future income. Manski (2004)
develops a framework for measuring expectations using surveys by eliciting subjective probability distributions, arguing
that such data can be used to validate assumptions models make about expectations. Extensive empirical research rests
on this assumption. Structural models have estimated dynamic behavior in domains including durable goods purchases
and dynamic pricing (Rust, 1987; Nair, 2007; Gowrisankaran and Rysman, 2012), consumer stockpiling (Hendel
and Nevo, 2006; Ching and Osborne, 2020), brand choice and learning under uncertainty (Erdem and Keane, 1996),
and agents’ strategic effort allocation (Misra and Nair, 2011). Together, this literature emphasizes that incorporating
expectations of future states is crucial for accurately modeling dynamic behavior.
Regarding forward-looking beliefs in the context of stories, Ely et al. (2015) write down a model of suspense and
surprise and derive the optimal information revelation strategy over time to maximize expected suspense or surprise.
Simonov et al. (2023) operationalize these ideas using structured game score data in an online streaming context,
demonstrating that suspense, but not surprise, about which team will win predicts viewing behavior. These empirical
approaches all require well-defined state spaces, leaving open how to model expectations over unstructured narrative
content, where the space of possible continuations is difficult to pre-specify. We extend the expectations framework to
unstructured narratives by generating belief distributions directly from narrative text.
Because LLMs were designed to generate probable text continuations conditional on partial input (Radford et al.,
2019), they offer a way to generate distributions of imagined continuations. However, their alignment with human
narrative expectations remains untested, and studies exploring whether LLMs can capture human beliefs, judgments,
and behaviors have produced mixed results. Even before modern LLMs, neural language models could generate
coherent story passages that humans preferred over baselines (Fan et al., 2018). However, it remains unclear whether
4

LLMs can capture how authors write. Tian et al. (2024) finds that narratives generated by GPT-4 lack tension and
are more positive than narratives generated by humans. The results are also mixed in other domains. Bybee (2023)
finds that LLMs can recover belief distributions over economic outcomes that closely match existing survey measures.
Halawi et al. (2024) find that LLMs are approaching human-level performance on forecasting tasks. Horton et al.
(2024) show that LLMs behave like humans in a number of economics experiments. Several studies find that LLMs
are useful for conducting market research (Brand et al., 2023; Li et al., 2024; Lee, 2024; Arora et al., 2025; Boughanmi
et al., 2025; Timoshenko et al., 2026). At the same time, Goli and Singh (2024) find that LLMs do not capture human
intertemporal preferences. Gao et al. (2025) find that LLMs do not exhibit human-like behaviors in the 11-20 money
request game. Peng et al. (2025) show that digital twins (LLM-based models of real individuals) generate answers
that only correlate weakly with human responses and demonstrate systematic bias. Overall, results on LLM-human
alignment are mixed, with agreement depending on task specificity and elicitation method. We contribute to this
literature by proposing two strategies to validate our framework for modeling story expectations. First, we propose a
rational expectations-based strategy,4 examining whether LLM-generated beliefs are, on average, unbiased predictors
of actual narrative text. Second, we compare LLM-derived expectations against human-reported beliefs collected
through survey. Bringing these three streams together creates a new opportunity for scalable market research on
creative content.
3 Method
Our approach leverages the ability of LLMs to approximate consumers’ forward-looking beliefs about stories. LLMs
are trained on enormous datasets encompassing diverse narratives across various genres, cultures, and time periods
(Radford et al., 2019). This expansive training allows them to capture complex patterns in storytelling that would
be difficult to model explicitly. In our context, this means the LLM can generate plausible story continuations that
reflect the nuanced ways in which narratives typically unfold, mirroring the expectations formed by consumers with
broad exposure to stories. We combine LLMs’ generative capabilities with theories from psychology, narratology, and
economics to extract interpretable features from the LLM-imagined story continuations.
We overview our proposed framework for modeling expectations in stories in Figure 1. The approach consists of
four main components: 1) imagined story generation, 2) feature extraction, 3) expectation validation, and 4) learning
how the features relate to engagement.
3.1 Imagined Story Continuation Generation
Our starting point is a piece of narrative content, such as the first few chapters of a book. LLMs are trained to predict
the next word given a set of preceding words. More specifically, language models estimate the conditional probability
of seeing word𝑤 𝑖, given all the previous words:𝑝(𝑤 𝑖|𝑤 1,...,𝑤 𝑖−1). We provide the LLM story text as input (e.g.,
chapters 1 through𝑡) and ask it to generate the next part of the story (e.g., chapter𝑡+1). Given the large amounts of story
4Rational expectations is the hypothesis that consumers’ subjective beliefs coincide, on average, with the true data-generating process.
5

Figure 1: Overview of Proposed Method
Story Input
Story Text
LLM
Imagined
Continuations
Imagined Continuation 1
...
Imagined Continuation N
Feature
Extraction
Engagement
Validation
Based on Rational
Expectations or Survey
data used to train LLMs, there is alignment between their training data and the task of generating story continuations.
This approach aims to model the process of a representative consumer anticipating potential story developments.
We generate multiple imagined continuations of the story to approximate potential continuations an average
consumer might anticipate. We generate multiple continuations for two reasons. First, doing so allows us to obtain a
distribution of continuations, from which we can measure not only the mean but also higher-order moments. Second,
LLM text generation contains inherent noise, even when temperature is 0, 5 so averaging over multiple continuations
reduces LLM-generation noise. There are three key design choices in this step: the prompt, the temperature, and the
number of continuations. The prompt sets the context for the LLM. Our starting point will be to use a simple prompt:
System Prompt:“You are an average reader.”
User Prompt:“Continue this story with the next chapter: [story text]. Next chapter:”
where [story text] represents the chapters read so far. In this paper, we model beliefs over the next chapter𝑡+1. The
framework applies to continuations for any number of chapters after𝑡. Next, the temperature affects the creativity of
the generated text, and we use the default temperature of 1 to balance text diversity and coherence with the input text.6
Finally, we generate 50 imagined continuations per chapter. A sensitivity analysis in Appendix B shows that feature
distributions stabilize around this number.
The choices above define a baseline implementation of the method rather than a fixed recipe. The validation
procedures in Section 3.3 provide a principled way to refine each. With additional data such as survey responses, richer
prompts can also be developed and evaluated against the simple baseline. For example, prompts could condition on
reader characteristics to capture heterogeneous beliefs.
5https://martynassubonis.substack.com/p/zero-temperature-randomness-in-llms
6The temperature parameter scales the probabilities of the next word that the model can select from. A temperature of 0 generates more
deterministic output, while a temperature of 2.0 generates more unpredictable output. We found that high temperature values generate incoherent
text strings.
6

3.2 Feature Extraction
With multiple imagined story continuations per chapter, the next question is how to quantify and interpret the unstruc-
tured story text. We approach this question in two steps: 1) we extract from the text predefined features that have
been proposed in the literature to be associated with engagement or narrative success and 2) we calculate consumers’
expectations of those features. The core idea is that if consumers care about those features in the text they have already
consumed, then they may also care about those same features in what they believe is yet to come.
As discussed in Section 2, the literature has identified various sets of features based on existing text that are
associated with engagement or narrative success, such as emotion and semantic path. A key benefit of these features is
that they are relevant to a wide range of stories. However, researchers and practitioners interested in particular genres
could use more specific features with our framework. Let𝑖represent the focal book,𝑡the focal chapter,𝑛the imagined
continuation number with𝑁capturing the total number of imagined continuations per chapter. Let 𝑠𝑡𝑜𝑟𝑦 𝑛 𝑖,𝑡+1 be the
imagined continuation for the next chapter and𝑓the representation of a story that reflects existing theory as well as
a hypothesis that a researcher is interested in testing. For example, text emotion has been found to be associated with
virality (Berger and Milkman, 2012) and a researcher may want to study whether expectations of future emotion in
a story help generate word-of-mouth. The researcher would use𝑓to represent the consumed content and imagined
continuations as emotion features. We definee𝑧 𝑛 𝑖,𝑡+1 to be the extracted feature from imagined continuation𝑛(i.e.,
e𝑧𝑛 𝑖,𝑡+1 =𝑓( 𝑠𝑡𝑜𝑟𝑦 𝑛 𝑖,𝑡+1)) and𝑧 𝑖,𝑡 to be the extracted feature from chater𝑡.
To calculate the expectation of each feature for each chapter, we average the features extracted from the imagined
continuations. The expectation of feature𝑧is:
E𝑡 𝑛[e𝑧𝑛 𝑖,𝑡+1]= 1 𝑁 𝑁∑︁ 𝑛=1 e𝑧𝑛 𝑖,𝑡+1,
which represents the average expected future state of the narrative for feature𝑧.
Beyond the first moment, the framework can also be used to calculate other moments of interest, such as
variance Var𝑡 𝑛[e𝑧𝑛 𝑖,𝑡+1]= 1 𝑁−1 ˝𝑁 𝑛=1  e𝑧𝑛 𝑖,𝑡+1−E𝑡 𝑛[e𝑧𝑛 𝑖,𝑡+1] 2 , deviation Dev𝑡 𝑛[𝑧𝑖,𝑡,e𝑧𝑛 𝑖,𝑡]=𝑧 𝑖,𝑡−E 𝑡−1 𝑛 [e𝑧𝑛 𝑖,𝑡], interactions
E𝑡 𝑛[e𝑧𝑛 𝑖,𝑡+1e𝑥𝑛 𝑖,𝑡+1]= 1 𝑁 ˝𝑁 𝑛=1e𝑧𝑛 𝑖,𝑡+1e𝑥𝑛 𝑖,𝑡+1 , and suspense and surprise (Ely et al., 2015). For this paper we primarily focus
on empirically evaluating the first moment (i.e., expectation), and we discuss the challenges (Bisbee et al., 2024; Deng
et al., 2026) and opportunities to studying other moments in Section 4.3 and Appendix D.
3.3 Validation of Expectations
Our proposed framework for modeling story expectations is only useful insofar that the extracted features proxy
actual expectations. We propose two ways to validate our expectations modeling method: 1) using the actual story
continuations, which serve as another approximation of consumer expectations if we assume rational expectations,
and 2) a more standard approach using stated beliefs based on surveys with human respondents. These validation
approaches enable researchers to continuously validate new LLM models that may be used for story continuation
generation and feature extraction.
7

3.3.1 Assuming Rational Expectations
In the context of narratives, assuming rational expectations means assuming that consumers who understand how
writers typically craft stories form beliefs that align with the objective distribution of story continuations. Rational
expectations is an assumption commonly made in the structural dynamic discrete choice literature (Rust, 1987; Erdem
and Keane, 1996; Hitsch, 2006; Dub´e et al., 2010). Using the actual story continuations to proxy consumer expectations
is easy to implement but relies on rational expectations being a reasonable assumption.
We formalize this validation procedure below. Let𝑃(𝑠𝑡𝑜𝑟𝑦)be the probability distribution over all possible stories.
This distribution represents the space of narratively coherent and realistic stories that could potentially be created by
humans. Any actual story can be viewed as a single realization from the joint distribution:𝑠𝑡𝑜𝑟𝑦 𝑖∼𝑃(𝑠𝑡𝑜𝑟𝑦). From
the distribution of stories, we can derive a conditional distribution of stories that represents the probability distribution
of possible continuations given a specific narrative context (e.g., chapters 1 through𝑡in story𝑖). The actual next
chapter can be viewed as a single realization from the conditional distribution:𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡+1 ∼𝑃(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡+1|𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡)
where𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡 represents the content from chapters 1 through𝑡in story𝑖. Let𝐵(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡+1|𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡)represent
the representative consumer’s subjective belief distribution about the next chapter. Let 𝑠𝑡𝑜𝑟𝑦 𝑛 𝑖,𝑡+1 denote the𝑛th
imagined continuation (i.e., next chapter) generated by an LLM based on chapters 1 through𝑡of story𝑖. Our
method tries to approximate the subjective belief distribution, such that{𝑠𝑡𝑜𝑟𝑦 𝑛 𝑖,𝑡+1}𝑁 𝑛=1 forms an empirical distribution
ˆ𝐵(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡+1|𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡)for the next chapter.
Then, assuming rational expectations, consumers who understand how writers typically craft stories should form be-
liefs that align with the objective writer-generated distributions (i.e.,𝐵(𝑠𝑡𝑜𝑟𝑦𝑖,𝑡+1|𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡)=𝑃(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡+1|𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡)).
We assess whether the expectations implied by consumers’ subjective belief distribution ˆ𝐵(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡+1|𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡)align
with the expectations implied by the objective distribution𝑃(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡+1|𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡). We operationalize this by repre-
senting the actual chapter text and imagined continuations using𝑓and regressing the actual features𝑓(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡+1)on
the expected featuresE[𝑓( 𝑠𝑡𝑜𝑟𝑦𝑖,𝑡+1)|𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡]). For example, if we were interested in the expected valence of the
next chapter, we would extract the valence of the imagined and actual next chapters, and then regress each chapter’s
actual valence on its average LLM-based valence. An intercept of 0 and coefficient of 1 would suggest that the
expectation modeling method perfectly captures consumers’ expectations under the rational expectations assumption.
A statistically significant positive coefficient would indicate the method captures meaningful signal about consumers’
expectations. The same procedure can be used for the other moments of the feature distribution as well.
3.3.2 Survey
While the rational expectations-based validation approach is easy to implement and does not require additional data, it
relies on the assumption of rational expectations, which may not hold. The survey-based validation provides a direct
benchmark for the subjective belief distribution our method seeks to approximate. Although it requires costly data
collection, it avoids imposing the rational expectations assumption.
Without cost constraints, we would ideally ask survey respondents to write out their beliefs over possible story
continuations to obtain the joint distribution over story features that consumers care about. This would allow us to
8

understand consumer preferences over any given feature or combinations of features. However, a full distribution over
text is cost prohibitive, so we instead propose a validation procedure that focuses on theoretically motivated dimensions
and elicit belief distributions following Manski (2004).
As before,𝑓maps a story continuation to features of interest (e.g., valence). We define an outcome space for
each feature and elicit beliefs over that space. For concreteness, suppose feature𝑓induces a finite set of mutually
exclusive outcomesK 𝑓 ={1,...,𝐾 𝑓}. For example, valence can be characterized by five ordered bins, ranging from
very negative (1) to very positive (5). For each story context𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡 and feature𝑓, the survey asks respondents
to report a probability vectors 𝑖,𝑡+1,𝑓 ≡ 𝑠𝑖,𝑡+1,𝑓 (1),...,𝑠 𝑖,𝑡+1,𝑓 (𝐾𝑓), where𝑠 𝑖,𝑡+1,𝑓 (𝑘)is a respondent’s stated
probability that outcome𝑘will occur in the next chapter. We interpret the distribution ofs 𝑖,𝑡+1,𝑓 across all respondents
as an empirical proxy for the feature-level beliefs implied by𝐵(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡+1|𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡). As was done for the rational
expectations validation procedure, we assess alignment between survey beliefs and LLM-implied beliefs by regressing
survey respondents’ expectations on our LLM-generated expectationsE[𝑓( 𝑠𝑡𝑜𝑟𝑦𝑖,𝑡+1)|𝑠𝑡𝑜𝑟𝑦 𝑖,1:𝑡]. The same can be
done for other distribution moments too.
The two procedures provide a strategy for validating how well our belief approximation method captures consumers’
expectations about how stories continue. They can also help refine the choice over the prompt, temperature, and LLM
model.
3.4 Explaining Engagement
If the LLM-based framework generates valid expectations that approximate consumers’ expectations, we can then
use the LLM-derived expectations to better understand narrative engagement. To illustrate the value of modeling a
consumer’s foward-looking beliefs, consider a consumer reading chapter𝑡of book𝑖who decides whether to continue.
Let𝑈𝑖,𝑡 denote her expected utility from continuing past chapter𝑡that is determined by the story read so far𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡 .
Because𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡 is a high-dimensional text object, researchers typically need to choose a𝐾-dimensional feature set
f: Text→R 𝐾 that serves as asufficient representation(Veitch et al., 2020; Egami et al., 2022; Feder et al., 2022) of
the story: the consumer’s beliefs about the next chapter and her engagement decision depend on the chapter text only
through these features. Letz 𝑖,𝑡 =f(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡)denote the vector of realized features in the story up through chapter𝑡,
and let𝜶,𝜷∈R 𝐾 denote the corresponding coefficient vectors. Consider a linear expected utility model:7
𝑈𝑖,𝑡 =𝜶 ⊤z𝑖,𝑡 +𝜷 ⊤E  f( 𝑠𝑡𝑜𝑟𝑦𝑖,𝑡+1)

 f(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡)  +𝜀 𝑖,𝑡,(Expected Utility)
where𝜀 𝑖,𝑡 represents an idiosyncratic taste shock. The consumer’s expectation of next-chapter features depends on
the story so far, represented byf(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡), as well as how her beliefs form, summarized by a𝐾×𝐾matrixΓwhose
entries capture how the current story shapes her expectations about the the next chapter:
E

f( 𝑠𝑡𝑜𝑟𝑦𝑖,𝑡+1)

 f(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡)  = Γz𝑖,𝑡.(Belief Formation)
7We adopt the linear form for clarity. It extends to nonlinear or dynamic utility, without changing the distinction between preferences over
realized and anticipated content.
9

The model implies several parameters of interest. To make them concrete, consider a representationf(𝑠𝑡𝑜𝑟𝑦 𝑖,𝑡)=
(𝑉𝑖,𝑡,𝐴𝑖,𝑡,𝜉𝑖,𝑡)⊤, where𝑉denotes valence,𝐴arousal, and𝜉collects all remaining elements of the story, and𝜶=
(𝛼𝑉,𝛼𝐴,𝛼𝜉)⊤,𝜷=(𝛽 𝑉,𝛽 𝐴,𝛽 𝜉)⊤, andΓ 𝑗,𝑘 denotes the entry of the belief-formation matrix giving the effect of
current feature𝑘on the expectation of next-chapter feature𝑗. Take emotional arousal, which captures how high or low
energy the chapter is, as the running example. Thetotal effect of current arousalon engagement bundles every channel
through which current arousal can move the consumer’s utility from continuing:
𝛿𝐴 =𝛼 𝐴 + (Γ⊤ 𝜷)𝐴=𝛼 𝐴|{z}
direct effect
+Γ 𝑉,𝐴 𝛽𝑉
|   {z   }
via expected valence
+Γ 𝐴,𝐴𝛽𝐴
|   {z   }
via expected arousal
+Γ 𝜉,𝐴 𝛽𝜉
|   {z   }
via expected𝜉
.
The first term is the direct effect: how much a high-arousal chapter raises engagement on its own. The remaining terms
run through belief formation: an arousing chapter shifts what the consumer expects to read next (the columnΓ ·,𝐴 ),
and she has preferences over each anticipated dimension (the entries of𝜷). Figure 2 illustrates the various channels
through which current arousal affects the consumer’s expected utility.𝛿𝐴 collapses these into a single number, mixing
structural preferences with belief formation. Thus, the total effect of current arousal is not a pure preference parameter.
It combines the consumer’s taste for current arousal with the way current arousal shifts expectations.
Figure 2: Unstructured Content and Expected Utility
Realized content Expected future content Expected utility
𝐴
𝑉
𝜉1
...
𝜉𝑛
E[𝐴]
E[𝑉]
E[𝜉 1]
...
E[𝜉𝑛]Survey/LLM
𝑈
Γ𝐴,𝐴
Γ𝑉,𝐴
Γ𝜉,𝐴
Γ𝑉,𝜉 1
𝛽𝐴
𝛽𝑉
𝛽𝜉
𝜶
Modeling expectations to recover𝛽𝐴 is valuable because preference over expectations are micro-founded economic
primitives that can generalize to cases when the belief formation process associated with a story changes. In many
applications, preferences over realized and anticipated content may be more portable than the belief-formation process
itself. For example, consumers’ beliefs may change as they gain genre familiarity. Without being able to measure or
approximateΓ, researchers cannot understand readers’ preferences over expectations.
Modeling expectations also delivers a prediction benefit by amplifying the value of existing theory. For example,
prior work suggests that valence and arousal are important drivers of engagement. If readers care about current valence
and arousal, they may also care about expected future valence and arousal. Including expected valence and arousal as
10

features therefore captures, indirectly, how other story dimensions𝜉feed into the consumer’s beliefs about what comes
next in terms of valence and arousal. We illustrate this idea in Figure 2. Expected next-chapter valence and arousal
depend on current𝜉through the off-diagonal entriesΓ 𝑉,𝜉 andΓ 𝐴,𝜉 . Although𝜉may itself be high-dimensional and
difficult to model explicitly, the LLM-generated continuations summarize its predictive content in part through expected
valence and arousal. Including expectations as features can therefore improve predictive power without requiring an
explicit model of every contributing𝜉dimension or sacrificing interpretability.
The model clarifies why estimating the effect of anticipated arousal is difficult even in a randomized experiment
due to the unstructured nature of the data (Wei and Malik, 2025). Suppose a researcher randomly assigns readers
to manipulated stories, elicits their expectations about next-chapter arousal, and measures subsequent engagement.
Random assignment makes exposure to the manipulated stories exogenous, but the manipulation may change many story
features at once. A regression of engagement on expected arousal alone therefore does not generally recover𝛽𝐴. Instead,
the coefficient on expected arousal reflects both the structural preference for anticipated arousal and bias from omitted
current and expected features that co-vary with expected arousal: plim ˆ𝑏=𝛽 𝐴+ ˝ 𝑋∈𝐴,𝑉,𝜉 𝛼𝑋𝜋𝑋+ ˝ 𝑋∈𝑉,𝜉 𝛽𝑋𝜋E𝑋,
where each𝜋𝑋 is the cross-story slope of feature𝑋on expected arousal. The estimated slope thus bundles the structural
preference𝛽 𝐴 with the effects of other story features that co-vary with expected arousal. Understanding these channels
requires measuring or approximating expected next-chapter content along multiple dimensions, which LLM-generated
continuations can provide at scale.
More generally, the coefficient on any feature in any specific representation is best read as a partial association,
holding the other included features fixed, which is how we are going to interpret the regression coefficients for the
remainder of the paper. While not causal, these coefficients can inform researchers on what additional data to collect
or analysis to conduct. When𝜉is correlated with the included current or expected features, that coefficient absorbs
the corresponding share of the𝜉effect as omitted-variable bias. Expanding the set of features included, whether
through richer feature extraction or additional survey items, both shrinks𝜉and closes one specific channel of bias on
the previously included coefficients.
4 Empirical Application with Survey Data
We first apply our proposed expectation-modeling approach in a controlled survey setting. This environment allows us
to directly elicit participants’ beliefs about upcoming story content, providing a ground-truth benchmark against which
to validate our LLM-based expectation measures. We also collect reader engagement to assess whether forward-looking
expectations are associated with it, and whether our modeled expectations can detect this relationship. A key benefit of
the controlled setting is that consumer selection is absent by design. In Section 5, we apply the method to observational
data to examine realistic engagement patterns but where such selection is present.
To illustrate our method, we focus on the emotion dimensions of valence and arousal encoded in the text (Russell,
1980).8 Valence captures how positive or negative a passage of text is and arousal captures how high or low energy.
8We distinguish between emotions expressed or encoded in the text and emotions felt by the reader. Mohammad and Turney (2013) find that the
11

These dimensions are well-defined psychological constructs, widely studied in narrative research (Berger et al., 2021;
Reagan et al., 2016; Knight et al., 2024), and consistently linked to engagement. Furthermore, forward-looking beliefs
are known to shape behavior through the anticipatory emotions they generate (Caplin and Leahy, 2001).
4.1 Survey Data
We recruit 263 participants via Prolific to read short stories and report their emotional beliefs and engagement. Each
participant reads two stories, each consisting of two chapters, yielding 1,052 participant-chapter observations. The
stories span five genres (fantasy, literary fiction, romance, science fiction, thriller), with 8 premises per genre for a total
of 40 unique story premises. An example of a premise used is: “Benor Vale, a former pilot, lives in exile on a dusty
moon and spends long evenings staring at the wreckage of his ship on the horizon.” Each premise has a common first
chapter and four second-chapter variants that differ in their emotional trajectory (positive/negative valence crossed with
high/low arousal), giving 160 unique story variants. This yields a total of 200 unique chapters (40 first chapters and
160 second chapters). We share the details of the procedure used to generate the chapters in Appendix A. Our goal was
to generate story text using a procedure that is easily reproducible and maximizes our ability to measure expectations
across the dimensions of valence and arousal.
After reading each chapter, participants report: (1) the valence and arousal of the text they just read (1–5 scale), (2)
their interest in continuing to read (1–5 scale), and (3) a probability distribution over expected valence and arousal for
the next chapter (allocating 100 points across five bins). Each unique chapter 1 and chapter 2 combination is read by
two to four participants. After the second chapter, participants additionally decide whether to read the third chapter.
Participants are told that the third chapter is entirely optional but that if they decide to read it that it will take one to
two more minutes. This binary decision serves as a revealed preference measure. We share additional survey details
in Appendix C.
4.2 Do Stated Expectations Predict Reader Engagement?
We use the survey responses to learn whether forward-looking beliefs are associated with engagement. We test this by
regressing reader stated interest to continue reading and their actual decision to continue reading on current valence
and arousal alongside the expectation, uncertainty, and/or deviation of valence and arousal.
We estimate the following model:
outcome𝑝𝑡 =x′ 𝑝𝑡 𝜷+𝛼 𝑝+𝜀 𝑝𝑡 (1)
where𝑝indexes participants and𝑡indexes chapters. The participant fixed effect𝛼 𝑝 absorbs unobserved individual
heterogeneity in response tendencies. Standard errors are two-way clustered at the participant and chapter level. We
measure stated interest in continuing to read after both chapters one and two, and therefore also include chapter number
fixed effects when the outcome is interest. We measure the binary decision to continue reading chapter three only
after chapter two, and therefore only include chapter two data when the outcome is the continue-to-read decision. We
former is associated with greater agreement between individuals and is therefore what we measure.
12

note that deviation can only be measured after chapter two because it requires the expectations generated after reading
chapter one.
The coefficients on the valence and arousal variables capture the association between a story’s emotional profile
and reader engagement. Because the emotional dimensions may covary with other story attributes, we do not interpret
the coefficients as isolated causal effects but instead as a combined association of the measured emotional profile and
any correlated story properties. Table 1 shows the results of regressing interest on the valence and arousal variables
collected for both chapters one and two. The stated expectations and uncertainty variables serve as direct measures of
consumers’ forward-looking beliefs. Adding expectations significantly improves the fit of the model. Stated arousal
expectations significantly predict interest in continuing to read. After controlling for the valence and arousal of the
chapter that they read (current valence and arousal), readers who anticipate more arousing continuations report greater
interest in continuing. Expected valence and uncertainty over valence and arousal, by contrast, are not significant
predictors of interest in our survey setting.
Table 1: Do Stated Expectations Predict Stated Interest?
DV: Stated Interest
Current V/A + Expectations + Exp + Uncertainty
(1) (2) (3)
Valence 0.020−0.005−0.005
(0.021) (0.026) (0.026)
Arousal 0.218 ∗∗∗ 0.120∗∗∗ 0.120∗∗∗
(0.026) (0.031) (0.032)
Expected valence 0.036 0.035
(0.050) (0.050)
Expected arousal 0.204 ∗∗∗ 0.206∗∗∗
(0.048) (0.049)
Uncertainty valence−0.008
(0.058)
Uncertainty arousal 0.036
(0.076)
Chapter number FE Yes Yes Yes
User FE Yes Yes Yes
𝐹(vs prev.) 3.32*** 0.04
Observations 1,052 1,052 1,052
R2 0.731 0.739 0.739
Adjusted R2 0.640 0.651 0.650
Note:Two-way clustered standard errors by user and chapter. ∗∗∗𝑝 <0.01; ∗∗𝑝 <0.05;
∗𝑝<0.1.
13

Table 2 reports results for the binary decision of continuing to read chapter three, which we interpret as a revealed-
preference measure. Because this was measured after chapter two, only chapter two data is used so the sample size
is reduced (N = 526). We estimate the model following equation 1 using a linear probability model. As with the
interest outcome, expected arousal predicts the decision to continue reading, while expected valence does not. Absolute
deviation and uncertainty also do not predict the decision to continue reading in this setting.
Table 2: Do Stated Expectations Predict Continue-to-Read Decision?
DV: Continue-to-Read
Current V/A + Expectations + Exp + Deviation + Exp + Dev + Unc
(1) (2) (3) (4)
Valence−0.0005−0.008−0.008−0.009
(0.015) (0.021) (0.021) (0.021)
Arousal 0.039 ∗∗ 0.006 0.005 0.0004
(0.015) (0.020) (0.022) (0.022)
Expected valence 0.015 0.014 0.013
(0.027) (0.027) (0.028)
Expected arousal 0.075 ∗∗ 0.072∗∗ 0.079∗∗
(0.030) (0.032) (0.032)
|Deviation|valence 0.020 0.011
(0.026) (0.028)
|Deviation|arousal−0.002−0.002
(0.026) (0.026)
Uncertainty valence 0.045
(0.048)
Uncertainty arousal 0.072
(0.059)
User FE Yes Yes Yes Yes
𝐹(vs prev.) 3.10** 0.28 2.00
Observations 526 526 526 526
R2 0.721 0.727 0.728 0.732
Adjusted R2 0.439 0.448 0.445 0.449
Note:Linear probability model. Two-way clustered standard errors by user and chapter. Ch2 only.|Deviation|=|actual
Ch2 V/A−Ch1 survey expectation|. ∗∗∗𝑝<0.01; ∗∗𝑝<0.05; ∗𝑝<0.1.
Altogether, the coefficients in Tables 1 and 2 suggest that consumers’ forward-looking expectations matter for
engagement. For both stated interest and decision to continue reading, the models including expectations show a
statistically significant improvement in fit.
14

4.3 Survey Validation: Do LLM Expectations Approximate Human Beliefs?
We then validate whether the expectations implied by our LLM-generated continuations correlate with readers’ stated
expectations. To apply our expectation modeling framework, we generate 50 imagined continuations for each chapter
using GPT-4.1-mini9 (temperature = 1.0) and extract valence and arousal from each continuation as well as the original
story text (temperature = 0.0). Implementation details are in Appendix A. We compute LLM-based expectations as the
average valence and arousal across continuations.
Figure 3 shows the scatter plots of the survey measures against the LLM-based measures. For each chapter, we
regress survey-reported expected valence and arousal on LLM-derived expected valence and arousal. Table 3 reports
the regression results at the chapter level.
Figure 3: Survey Emotion vs. LLM-derived Emotion
Note: Each point is a unique chapter (𝑁=200).
The slopes in Table 3 are 0.57 for valence and 0.56 for arousal and both significantly positive, indicating that
LLM-derived expectations capture meaningful variation in human beliefs. The slopes are below 1, indicating that
LLM-based measures are imperfect but informative. The intercepts are positive (0.98 for valence, 1.44 for arousal),
indicating a level difference between the two measurement scales. Despite this approximation error, which can lead
to attenuation bias, the LLM expectations retain sufficient signal to predict reader interest, as we show below. This
validation holds across both chapters and all five genres, as shown in Figure D1 and Table D1 in Appendix D. The
relationship also survives controlling for current-chapter valence and arousal (Table D2 in Appendix D).
A well-known limitation of current off-the-shelf LLMs is that they tend to produce overly concentrated distributions
relative to humans (Bisbee et al., 2024; Deng et al., 2026). Our validation yields similar findings: when we regress survey
uncertainty on LLM-derived uncertainty for valence and arousal, the coefficients are small, statistically insignificant,
9Model version:gpt-4.1-mini-2025-04-14.
15

Table 3: LLM Expectations Predict Survey Expectations
Dependent variable:
Survey expected valence Survey expected arousal
(1) (2)
LLM expected valence 0.571 ∗∗∗
(0.053)
LLM expected arousal 0.563 ∗∗∗
(0.062)
Constant 0.977 ∗∗∗ 1.435∗∗∗
(0.200) (0.205)
Observations 200 200
R2 0.369 0.297
Adjusted R2 0.366 0.293
Note:∗∗∗𝑝<0.01; ∗∗𝑝<0.05; ∗𝑝<0.1.
and explain little of the variation in survey responses (Table D3 in Appendix D). Because of this limitation, this paper
focuses on expectations and leaves the modeling of uncertainty to future work.
4.4 Using LLM Expectations to Understand Reader Engagement
Having established that forward-looking expectations are associated with engagement, we ask whether LLM-derived
expectations can serve as a scalable proxy. We estimate parallel models replacing survey-elicited expectations with
LLM-based measures. Table 4 columns (3) and (4) show the results. We find that the modeled results parallel the
survey results. In both the survey and modeled data, current and expected valence do not significantly predict interest,
but current and expected arousal do. Furthermore, the coefficient magnitudes are comparable.
Table 5 reports the results of the binary decision to continue reading chapter three. As with the interest outcome,
expected arousal predicts the decision to continue reading in the survey (𝑝 <0.05) and modeled (𝑝 <0.10) specifica-
tions (columns 2 and 4), while expected valence does not. The coefficient magnitudes are comparable across the two
measurement approaches, reinforcing the conclusion that LLM-derived expectations can serve as a scalable proxy for
survey-elicited beliefs.
4.5 Application: Feature Exploration
Having validated the expectation framework on a predefined set of emotional dimensions, we next extend it to other
narrative dimensions. As discussed in Section 3.4, these approximations may be imperfect, but can nevertheless help
researchers refine their causal questions and interpret the empirical relationships they identify.
Causal questions about stories are difficult to study because narratives vary along many dimensions that often
move together. For example, changing a story to increase arousal rarely changes arousal alone, but typically changes
16

Table 4: LLM Expectations and Stated Interest
Survey Modeled
Current V/A + Expectations Current V/A + Expectations
(1) (2) (3) (4)
Valence 0.020 -0.005 0.012 0.022
(0.021) (0.027) (0.022) (0.026)
Arousal 0.218*** 0.120*** 0.160*** 0.118***
(0.026) (0.031) (0.024) (0.026)
Expected valence 0.036 -0.000
(0.050) (0.058)
Expected arousal 0.204*** 0.146**
(0.048) (0.071)
Chapter number FE Yes Yes Yes Yes
User FE Yes Yes Yes Yes
Observations 1,052 1,052 1,052 1,052
R2 0.731 0.739 0.713 0.715
Adjusted R2 0.640 0.651 0.616 0.618
Note:Two-way clustered standard errors by user and chapter.∗∗∗𝑝<0.01; ∗∗𝑝<0.05; ∗𝑝<0.1.
pacing and tension along with it. By approximating expectations along many dimensions at low cost, our framework
helps researchers assess whether these distinctions are empirically consequential and clarify which counterfactual their
estimates correspond to. Once the causal question is refined, researchers can more efficiently decide what additional
data to collect, based on how each approximated dimension correlates with the focal feature and outcome.
To illustrate, we use the imagined continuations to learn additional narrative dimensions that may be relevant for
reader engagement and extract them from both the actual text and imagined continuations. The features are narrative
tension, curiosity, emotional complexity, character agency, social conflict, resolution versus complication, cliffhanger
intensity, vividness, pacing, character relatability, and cognitive complexity (definitions in Appendix E.4). For each
dimension, we compute its expected value as the average rating across continuations, following the same procedure
used for valence and arousal. Although we do not have human survey responses against which to validate these
dimensions directly, we can validate them using the rational-expectations approach discussed in Section 5.2.
We then assess whether adding each dimension, one at a time, changes the valence and arousal coefficients reported
in Table 4. Figure 4 shows that the four coefficients respond differently to these additions. The current-chapter arousal
coefficient is stable and remains significant in nearly every specification, with the exceptions being pacing and tension.
By contrast, the expected-arousal coefficient is sensitive to the addition of tension, cliffhanger intensity, curiosity, and
emotional complexity. Current-chapter valence becomes significant after controlling for pacing, tension, cliffhanger,
and curiosity.
17

Table 5: LLM Expectations and Continue-to-Read Decision
Survey Modeled
Current V/A + Expectations Current V/A + Expectations
(1) (2) (3) (4)
Valence -0.000 -0.008 -0.005 -0.011
(0.015) (0.021) (0.014) (0.017)
Arousal 0.039** 0.006 0.025 0.013
(0.015) (0.020) (0.018) (0.020)
Expected valence 0.015 0.058
(0.027) (0.040)
Expected arousal 0.075** 0.077*
(0.030) (0.045)
User FE Yes Yes Yes Yes
Observations 526 526 526 526
R2 0.721 0.727 0.717 0.721
Adjusted R2 0.439 0.448 0.430 0.434
Note:Linear probability model. Two-way clustered standard errors by user and chapter. Ch 2 only.
∗∗∗𝑝<0.01; ∗∗𝑝<0.05; ∗𝑝<0.1.
For researchers studying valence and arousal, whether these additional dimensions should be measured depends
on the causal question. In particular, the researcher must decide whether a given dimension is a confounder to be held
fixed or a mediator that should be allowed to vary. Approximating and exploring these dimensions at low cost helps
identify which story elements to prioritize, because both the estimate and its interpretation can be sensitive to their
inclusion. For example, a researcher interested in the effect of expected arousal on engagement, regardless of what
drives that arousal, need not control for whether the story is at a cliffhanger. A researcher interested instead in the
component of expected arousal that arises from semantic content alone learns from this analysis that dimensions such
as cliffhanger intensity matter and should consider measuring them in a survey.
5 Empirical Application with Observational Data
Next, we apply our proposed framework to observational data from an online reading platform. This data set is noisier
and subject to reader self-selection of book choice and continued consumption, and so the empirical patterns may not
match those of the survey. However, the observational setting also offers several advantages over the survey setting.
First, the stories reflect realistic distributions of narrative content, making it possible to test the rational expectations
assumption described in Section 3.3. Second, the engagement measures capture revealed preferences through actual
reading, voting, and commenting behavior rather than stated intentions.
18

Figure 4: Sensitivity Analysis of V/A Coefficients
Note: Sensitivity of the validated coefficients to adding one narrative dimension at a time. The baseline specification regresses interest on current
and expected valence and arousal, with user and chapter-number fixed effects. Each row adds the realized and expected ratings of a single dimension
to that baseline.
5.1 Online Media Platform Data
We collect book text with chapter-by-chapter engagement from an online media platform where users read and write
stories. The content is posted chapter by chapter, and we observe the read count, vote count, and comment count
for each chapter, allowing us to calculate continue-to-read, vote-to-read, and comment-to-read rates. We focus on
the vote-to-read and comment-to-read rates as our primary engagement outcomes, and exclude the continue-to-read
rate because its data quality is compromised by chapter re-uploads, which reset the read count. Vote-to-read and
comment-to-read rates do not depend on chapter sequencing and are therefore less affected by chapter re-uploads.
For each book, we collect its title and description, creation date, language, whether the content is for mature
audiences, and writer-provided book tags (e.g., “school”, “drama”). For each chapter, we collect the text, title, date
written, comment count, vote count, and read count. We select books that have at least nine chapters and focus on the
first nine chapters so that we have a balanced dataset across books, which span a wide range of fiction genres.10
We usegpt-4o-mini-2024-07-18to generate the imagined story continuations. To alleviate the concern about
data leakage (i.e., the engagement metrics and actual story continuations being part of the training data), we only
include books published after the training data cutoff for the model. 11 This ensures that the content was not used to
train the LLM we use to generate the imagined stories. Since our proposed story imagination method relies critically
on the quality of the input text, we take several steps to clean the stories, as detailed in Web Appendix B. After cleaning,
we are left with 8,399 chapters across 937 books.
10We exclude nonfiction because rational expectations validation may be more likely to succeed in this setting and there is risk of data leakage.
11gpt-4o-mini-2024-07-18’s training data cutoff is October 2023, and all book chapters in our sample are published December 2023 or later.
19

5.1.1 Summary Statistics
Table 6 provides summary statistics of our dataset. Compared to more traditional books, which have on average 3,000
to 4,000 words per chapter, the chapters in our data are shorter with an average of 1,968 words. Readers can comment
throughout the text, and comments are consolidated at the end of the chapter. Readers can also vote to show their
support for a writer and can only vote once per chapter. Our outcome measures of interest are the comment-to-read
rate (comment count / read count of chapter) and vote-to-read rate (vote count / read count of chapter). Since the
engagement distributions are right-skewed, we winsorize the outcome measures at the 2.5th and 97.5th percentiles and
z-score them for the regression analysis.
Table 6: Summary Statistics
Measure Mean Std Dev Min P2.5 P97.5 Max
Number of words 1,968 1,453 200 393 6,139 13,882
Comment count 13 49 0 0 108 1,111
Vote count 31 157 0 0 171 5,338
Read count 900 4,559 1 12 5,338 245,187
Comment-to-read rate 0.06 0.27 0 0 0.46 6.50
Vote-to-read rate 0.06 0.08 0 0 0.28 1.00
5.2 Rational-Expectations Validation: Do LLM Expectations Approximate Actual Story
Features?
In addition to the emotion features used in the survey validation, this section includes semantic path features (speed,
volume, and circuitousness) and the narrative dimensions learned from the imagined continuations in Section 4.5. The
semantic path features can be applied to a wide range of stories and have been shown to predict narrative success
(Toubia et al., 2021). Speed captures how quickly the text moves from one idea to another, volume captures how much
conceptual ground it covers, and circuitousness captures how roundabout its trajectory is. Following Toubia et al.
(2021), we measure speed, volume, and circuitousness for each chapter and imagined continuation using their word
embeddings. Because speed and volume are highly correlated in our data (𝑟=0.997), we retain only speed in the
subsequent analysis.12 Additional implementation details are provided in Appendix E.
Following the rational-expectations validation procedure described in Section 3.3, we regress each chapter’s
realized feature value on the corresponding LLM-based expected value. Table 7 presents the results. All features
have positive, highly significant coefficients, indicating that LLM-generated expectations are informative predictors of
realized chapter content. However, as in the survey validation, the LLM-based expectation measures exhibit bias. The
emotion coefficients are similar across the survey and rational-expectations validation procedures: 0.69 versus 0.57
12Toubia et al. (2021) also report a high correlation between speed and volume,𝑟=0.88, in their analysis of TV dialogue.
20

for valence and 0.62 versus 0.56 for arousal. This similarity suggests that rational-expectations validation performs
similarly to survey-based validation without requiring costly survey data.
Table 7: Validation based on Rational Expectations
Intercept𝛽R 2
Emotion
Valence 0.475 ∗∗∗ (0.045) 0.693 ∗∗∗ (0.012) 0.298
Arousal 1.424 ∗∗∗ (0.045) 0.615 ∗∗∗ (0.012) 0.232
Semantic Path
Semantic Speed -0.294 ∗∗∗ (0.019) 1.285 ∗∗∗ (0.021) 0.318
Semantic Circuitousness 0.015 ∗∗∗ (0.001) 0.435 ∗∗∗ (0.025) 0.035
Learned Features
Tension 1.346 ∗∗∗ (0.045) 0.670 ∗∗∗ (0.013) 0.253
Curiosity 1.606 ∗∗∗ (0.045) 0.607 ∗∗∗ (0.013) 0.210
Emotional Complexity 1.660 ∗∗∗ (0.051) 0.559 ∗∗∗ (0.014) 0.153
Character Agency 0.849 ∗∗∗ (0.079) 0.721 ∗∗∗ (0.021) 0.128
Social Conflict 1.321 ∗∗∗ (0.037) 0.669 ∗∗∗ (0.012) 0.260
Resolution 1.348 ∗∗∗ (0.044) 0.350 ∗∗∗ (0.018) 0.043
Cliffhanger 1.327 ∗∗∗ (0.054) 0.587 ∗∗∗ (0.017) 0.128
Vividness 1.940 ∗∗∗ (0.060) 0.456 ∗∗∗ (0.018) 0.073
Pacing 2.473 ∗∗∗ (0.066) 0.382 ∗∗∗ (0.018) 0.053
Relatability 0.218 ∗∗∗ (0.070) 0.925 ∗∗∗ (0.018) 0.240
Cognitive Complexity 1.465 ∗∗∗ (0.053) 0.623 ∗∗∗ (0.017) 0.135
Note:∗∗∗𝑝<0.01; ∗∗𝑝<0.05; ∗𝑝<0.1. N=8,399.
In addition, rational-expectations validation allows us to validate features that would be difficult to validate using
the survey-based strategy. In particular, it would be challenging to validate measures like interactions and covariances
using the survey because they require beliefs about the joint probability. In the survey, we do not measure consumers’
beliefs about the joint probability between valence and arousal because of the complexity of the task, which would
require assigning probabilities across 25 buckets. By assuming rational expectations, we can compare the pairwise
interactions of the features extracted from the imagined continuations with the pairwise interactions of the realized
chapters. Figure 5 plots the distribution of coefficients from regressing realized next-chapter pairwise interactions
on LLM-derived interactions. All of the𝛽coefficients are significantly positive and the median coefficient is 0.59,
suggesting our expectations modeling framework captures meaningful variation in human beliefs under the assumption
of rational expectations.
21

Figure 5: Interaction Coefficients
Note:Coefficient𝛽from𝑋 𝑡+1·𝑌𝑡+1∼E indirect[𝑋·𝑌] 𝑡 across all 105 pairs of the 15 features.𝛽=1 is the rational-expectations
target (dashed line). Median in red. All 105 coefficients are significant at𝑝<0.001.
5.3 Which Features Are Associated with Engagement?
Besides capturing realistic stories, the observational data capture real engagement patterns. Greater engagement in the
form of commenting and voting behavior is of interest to platforms, advertisers, and writers as these measures relate to
customer retention, ad effectiveness, and product feedback, respectively.
We regress each engagement measure on features of the actual text and expectations from the imagined continuations.
We also control for the log of first-chapter read count, which proxies for baseline book popularity, including factors
such as author fame and marketing effort. We control for word count because chapter length affects whether consumers
finish a given chapter, and include chapter-number fixed effects to absorb systematic differences in engagement across
chapter positions, such as reader attrition over the course of a book. Because these observational relationships may
reflect consumer heterogeneity and dynamic selection, we interpret the coefficients as platform-specific associations
rather than causal effects. Table 8 presents the regression results for each set of features separately. Expected valence,
arousal, speed, and circuitousness are all significantly associated with voting and commenting. More negative and
lower energy next-chapter expectations are associated with higher vote-to-read and comment-to-read rates. Higher
speed and lower circuitousness expectations are also associated with greater engagement. As with the survey data, we
observe that forward-looking expectations help predict engagement.
To illustrate how the method can help researchers better understand the relationship between the focal features and
engagement, Figure 6 shows how the current and expected valence and arousal coefficients change after including each
narrative dimension in the regression, one at a time. The robustness of expected arousal for comment-to-read suggests
22

Table 8: Which Features are Associated with Voting and Commenting?
Vote-to-Read Comment-to-Read
Current + Expectation Current + Expectation
Panel A. Emotion — Valence + Arousal, joint multivariate model
Valence, current -0.036 ∗∗∗ (0.012) 0.032 ∗∗ (0.015) -0.027 ∗∗ (0.012) 0.020 (0.015)
Valence, expectation — -0.123 ∗∗∗ (0.015) — -0.089 ∗∗∗ (0.016)
Arousal, current 0.013 (0.012) 0.017 (0.013) -0.020 (0.012) 0.009 (0.014)
Arousal, expectation — -0.045 ∗∗∗ (0.013) — -0.085 ∗∗∗ (0.014)
𝑅2 0.108 0.115 0.040 0.045
Adjusted𝑅 2 0.106 0.113 0.038 0.044
Panel B. Semantic Path — Speed + Circuitousness, joint multivariate model
Semantic Speed, current 0.023 (0.016) -0.026 (0.019) 0.084 ∗∗∗ (0.016) 0.010 (0.020)
Semantic Speed, expectation — 0.064 ∗∗∗ (0.014) — 0.095 ∗∗∗ (0.015)
Semantic Circuitousness, current -0.044 ∗∗∗ (0.011) -0.028 ∗∗ (0.011) -0.055 ∗∗∗ (0.011) -0.032 ∗∗∗ (0.012)
Semantic Circuitousness, expectation — -0.047 ∗∗∗ (0.011) — -0.063 ∗∗∗ (0.011)
𝑅2 0.108 0.111 0.044 0.051
Adjusted𝑅 2 0.106 0.110 0.043 0.050
Note: ∗∗∗𝑝<0.01; ∗∗𝑝<0.05; ∗𝑝<0.1. N = 8,399. Log first-chapter read count and word count included as controls. Chapter number FE
included.
that readers’ anticipation of emotional energy carries signal beyond what dimensions like tension and pacing capture.
The greater sensitivity of expected valence for comment-to-read, by contrast, indicates that this association may partly
operate through other narrative dimensions.13 As in Section 4.5, whether to treat these dimensions as confounders to
control for or as mediators to allow to vary depends on the researcher’s causal question. In this section, we analyze
the simplest set of current and forward-looking features, but there are many additional features, such as average past
emotion (e.g., average valence and arousal for chapters 1 to𝑡−1) and number of narrative reversals (Knight et al.,
2024), that future work could explore to further enrich our understanding of engagement.
6 Alternative Implementations
To model consumers’ forward-looking expectations, we have so far introduced and evaluated agenerativeimplementa-
tion, where we generate multiple imagined story continuations. We now discuss two alternative implementations that
can also operationalize our framework, and discuss the tradeoffs.
6.1 Direct Elicitation of Features from LLM
One possible implementation, which we calldirect elicitation, is to ask the LLM to assign probabilities to possible
outcomes for predefined features, mirroring how we elicit beliefs from survey respondents. Using this implementation,
13Web Appendix C provides the results for the semantic path features.
23

Figure 6: Sensitivity Analysis of V/A Coefficients for Observational Data
Note: Sensitivity of the emotion coefficients to adding one narrative dimension at a time. The baseline specification regresses each engagement ratio
on current and expected valence and arousal, with word count and log readership controls and chapter fixed effects. Each row adds the realized and
expected ratings of a single dimension to that baseline.
we extract emotion features and the 11 narrative dimensions from Section 4.5 for both the survey and observational
data. The prompt for the narrative dimensions is provided in Web Appendix A.
Direct elicitation and the generative implementation make different tradeoffs. Direct elicitation is less costly
because it does not require generating multiple continuations or extracting features from them. Because its output
structurally resembles survey responses, it may better match human-reported beliefs for well-studied features: in
the survey-validation comparison (Table 9),𝛽coefficients are closer to one and𝑅 2 values are higher than for the
generative method. Direct elicitation can therefore be well-suited when the research question targets a predefined set of
features and the goal is to approximate stated beliefs without exploring additional dimensions or checking sensitivity
to correlated ones.
In contrast, the generative implementation produces continuations as a byproduct of the procedure, which carry
several advantages. The continuations give writers a concrete view of what readers may anticipate, can be used to
identify additional features beyond those specified a priori (Section 4.5), and can serve as input to feature-extraction
methods that require text, such as Toubia et al. (2021). Because each continuation carries all features simultaneously, the
implementation also recovers the joint distribution across feature dimensions, something direct elicitation captures only
24

by separately eliciting probabilities over feature combinations, an exercise that becomes infeasible as the number of bins
grows. We find that the generative implementation more closely predicts realized story content for the observational
data. While direct elicitation provides a reasonable approximation of realized content, with positive and statistically
significant coefficients for nearly all of the expectations features (Table 10) and positive interaction coefficients with
a median of 0.63 (Figure 7), the LLM expectations derived from the generative implementation better explain the
variation of actual story continuations: Figure 8 shows that the generative𝑅 2 exceeds direct-elicitation𝑅 2 across all
features and feature pairs. Which implementation is preferable therefore depends on the research question.
Table 9: Direct Elicitation Expectations Predict Survey Expectations
Dependent variable:
Survey expected valence Survey expected arousal
(1) (2)
Direct-elicitation expected valence 0.787 ∗∗∗
(0.032)
Direct-elicitation expected arousal 0.773 ∗∗∗
(0.047)
Constant 0.908 ∗∗∗ 0.917∗∗∗
(0.092) (0.145)
Observations 200 200
R2 0.755 0.582
Adjusted R2 0.754 0.580
Note:∗∗∗𝑝<0.01; ∗∗𝑝<0.05; ∗𝑝<0.1.
Figure 7: Direct Elicitation Interaction Coefficients
Notes:All coefficients are significant at𝑝<0.001.
25

Table 10: Do Direct Elicitation Expectations Predict Actual Story Fea-
tures?
Intercept𝛽R 2
Emotion
Valence 0.915 ∗∗∗ (0.085) 0.808 ∗∗∗ (0.031) 0.075
Arousal 3.210 ∗∗∗ (0.094) 0.153 ∗∗∗ (0.030) 0.003
Learned Features
Tension 1.991 ∗∗∗ (0.145) 0.532 ∗∗∗ (0.044) 0.017
Curiosity 0.213 (0.161) 1.086 ∗∗∗ (0.050) 0.053
Emotional Complexity 2.385 ∗∗∗ (0.148) 0.397 ∗∗∗ (0.047) 0.009
Character Agency 1.281 ∗∗∗ (0.193) 0.732 ∗∗∗ (0.061) 0.017
Social Conflict -1.534 ∗∗∗ (0.163) 1.564 ∗∗∗ (0.053) 0.093
Resolution 2.743 ∗∗∗ (0.077) -0.183 ∗∗∗ (0.026) 0.006
Cliffhanger 0.448 ∗∗∗ (0.130) 0.884 ∗∗∗ (0.042) 0.051
Vividness 2.705 ∗∗∗ (0.193) 0.247 ∗∗∗ (0.063) 0.002
Pacing 2.180 ∗∗∗ (0.117) 0.550 ∗∗∗ (0.037) 0.025
Relatability 2.123 ∗∗∗ (0.161) 0.544 ∗∗∗ (0.051) 0.013
Cognitive Complexity 0.034 (0.153) 1.066 ∗∗∗ (0.049) 0.054
Note:∗∗∗𝑝<0.01; ∗∗𝑝<0.05; ∗𝑝<0.1. N = 8,399.
Figure 8: Comparison of𝑅 2 between Implementations (Generative𝑅 2 - Direct-elicitation𝑅 2)
(a)Δ𝑅 2 for Expectations
 (b)Δ𝑅 2 for Interactions
26

6.2 Embeddings as Features
We have so far focused on interpretable features because they are useful to content creators, platforms, and researchers
seeking to understand the drivers of engagement. The same framework can in principle be applied when stories are
represented using text embeddings rather than predefined interpretable features. The downside is that this approach
sacrifices interpretability, and its benefit depends on whether expectations over the embeddings capture meaningful
information. Web Appendix D implements this approach. In the survey data, the embedding-based expectation
components do not predict stated interest (Table D1), possibly due to the limited sample size relative to the number of
additional variables. In the observational data, by contrast, the embedding-based expectation components complement
the current-chapter components and improve prediction (Table D2).
7 Discussion
In both the survey and observational data, we find that LLM-generated story continuations correlate with consumers’
forward-looking expectations over interpretable dimensions and that these LLM-derived expectations are associated
with reader engagement. We discuss the key findings, implications, and limitations below.
The survey validation demonstrates that LLM-derived expectations correlate with human-reported beliefs over
story continuations along the dimensions of valence and arousal (Table 3). The slopes are attenuated relative to
unity, indicating that LLM expectations capture the direction and relative ordering of human beliefs but compress the
range. In the observational setting, the rational expectations validation confirms that LLM-generated expectations are
informative predictors of realized chapter content across all of the features we examine, which includes expectations
as well as interactions between pairs of features (Table 7). Together, these results suggest that LLMs trained on large
corpora of narrative text can serve as a reasonable starting point for modeling what readers anticipate.
We also find that forward-looking expectations are associated with engagement above and beyond the content
readers have already consumed. In the survey setting, expected arousal significantly predicts reader interest after
controlling for current valence and arousal (Table 1). In the observational setting, the expected emotion and semantic
path features predict voting and/or commenting behavior after controlling for their current measures (Table 8). We show
the sensitivity of the coefficients to controlling for the narrative dimensions identified using the generated continuations.
Our framework has several implications for research and practice. First, it provides a scalable method for empirically
modeling consumer beliefs over narrative content. Because the method can be applied to any text for which story
continuations can be generated, it extends the expectations literature beyond structured state spaces to the domain
of unstructured narratives. Researchers studying narrative engagement can use our approach to complement existing
feature extraction methods by adding a forward-looking dimension.
Second, the finding that expected features are associated with engagement has practical implications for content
creators and platforms. For content creators, our results suggest that what readers anticipate matters for engagement,
not just what they experience. Authors and screenwriters may benefit from considering how their narrative choices
shape reader expectations, such as how chapter endings signal the emotional trajectory or pacing of what is to come.
27

For platforms, the ability to extract expectation-based features at scale could inform recommendation systems, content
curation, and ad placement strategies.
Third, the sensitivity analysis of the coefficients to including additional content-based controls has important
implications for researchers seeking to study the causal effect of story features on outcomes of interest. Because story
features often move together, an estimate for any given feature depends on which other dimensions are held fixed.
Our framework helps researchers diagnose whether omitted dimensions are likely to change the interpretation of a
coefficient. LLM-based feature extraction can help refine the causal question before researchers commit to a particular
experimental or survey design.
Our approach has several limitations that present opportunities for future research. First, while our validation
results are encouraging, LLM-derived expectations are approximations. The attenuated survey-validation slopes
suggest that they compress the range of human beliefs, introducing measurement error that can attenuate downstream
regression coefficients. Future work could explore fine-tuning LLMs or calibrating the generated distributions to better
match human belief distributions. Second, our empirical results are associational rather than causal. The regression
coefficients capture the relationship between narrative features and engagement conditional on controls, but they
may reflect correlated story attributes rather than the isolated effect of any single dimension. Experimental designs
that manipulate reader expectations while holding actual content constant could help establish causal relationships.
Third, our current implementation focuses on textual narratives. Many forms of narrative media involve visual and
auditory elements that our text-based approach does not capture. For example, Manzoor and Malik (2023) use a
music generation model to quantify the unpredictability of music. As multimodal large language models continue
to develop, extending our framework to generate and analyze multimodal story continuations is a natural next step.
Finally, we model a representative consumer by treating the LLM as an average reader, but in practice, consumers
are heterogeneous in their narrative preferences and expectations. Readers with different genre expertise, cultural
backgrounds, or reading histories may form systematically different beliefs about how stories will unfold. Future work
could explore conditioning the LLM on reader-specific information or modeling heterogeneous expectations across
consumer segments.
8 Conclusion
This paper introduces a framework for modeling consumers’ forward-looking expectations in stories by using large
language models. By extracting features from these continuations, our method complements existing content analysis
techniques with a forward-looking dimension that captures what readers anticipate, not just what they have consumed.
We validate the approach using both survey-elicited beliefs and a rational expectations framework, finding that LLM-
derived expectations correlate with human beliefs and are informative predictors of realized story content across multiple
narrative dimensions. Applying the framework to both survey and observational data, we find that forward-looking
expectations are associated with reader engagement beyond what actual content features alone explain, suggesting that
a richer understanding of engagement requires modeling what readers expect.
28

We hope this framework serves as a starting point for empirical researchers interested in understanding how
consumer beliefs about unstructured narrative content shape behavior, with applications spanning content creation,
platform strategy, and the broader study of narrative media.
Funding and Competing Interests
All authors certify that they have no affiliations with or involvement in any organization or entity with any financial
interest or non-financial interest in the subject matter or materials discussed in this manuscript. The authors have no
funding to report.
References
Arora, N., Chakraborty, I., and Nishimura, Y. (2025). AI–human hybrids for marketing research: Leveraging large
language models (LLMs) as collaborators.Journal of Marketing, 89(2):43–70.
Bamman, D., Underwood, T., and Smith, N. A. (2014). A Bayesian mixed effects model of literary character. In
Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (ACL), pages 370–379.
Berger, J., Kim, Y. D., and Meyer, R. (2021). What makes content engaging? how emotional dynamics shape success.
Journal of Consumer Research, 48(2):235–250.
Berger, J. and Milkman, K. L. (2012). What makes online content viral?Journal of Marketing Research, 49(2):192–
205.
Berger, J., Moe, W. W., and Schweidel, D. A. (2023). What holds attention? linguistic drivers of engagement.Journal
of Marketing, 87(5):793–809.
Bisbee, J., Clinton, J. D., Dorff, C., Kenkel, B., and Larson, J. M. (2024). Synthetic replacements for human survey
data? the perils of large language models.Political Analysis, 32(4):401–416.
Boughanmi, K., Jedidi, K., and Jedidi, N. (2025). From reviews to actionable insights: An llm-based approach for
attribute and feature extraction.arXiv preprint arXiv:2510.16551.
Brand, J., Israeli, A., and Ngwe, D. (2023). Using LLMs for market research.Harvard Business School Marketing
Unit Working Paper, (23-062).
Bybee, L. (2023). Surveying generative ai’s economic expectations.arXiv preprint arXiv:2305.02823.
Caplin, A. and Leahy, J. (2001). Psychological expected utility theory and anticipatory feelings.Quarterly Journal of
Economics, 116(1):55–79.
29

Ching, A. T. and Osborne, M. (2020). Identification and estimation of forward-looking behavior: The case of consumer
stockpiling.Marketing Science, 39(4):707–726.
Deng, Y., Brucks, M., and Toubia, O. (2026). Examining and addressing barriers to diversity in llm-generated ideas.
arXiv preprint arXiv:2602.20408.
Dub´e, J.-P. H., Hitsch, G. J., and Chintagunta, P. K. (2010). Tipping and concentration in markets with indirect network
effects.Marketing Science, 29(2):216–249.
Egami, N., Fong, C. J., Grimmer, J., Roberts, M. E., and Stewart, B. M. (2022). How to make causal inferences using
texts.Science Advances, 8(42):eabg2652.
Eliashberg, J., Hui, S. K., and Zhang, Z. J. (2007). From story line to box office: A new approach for green-lighting
movie scripts.Management Science, 53(6):881–893.
Ely, J., Frankel, A., and Kamenica, E. (2015). Suspense and surprise.Journal of Political Economy, 123(1):215–260.
Erdem, T. and Keane, M. P. (1996). Decision-making under uncertainty: Capturing dynamic brand choice processes
in turbulent consumer goods markets.Marketing science, 15(1):1–20.
Fan, A., Lewis, M., and Dauphin, Y. (2018). Hierarchical neural story generation.arXiv preprint arXiv:1805.04833.
Feder, A., Keith, K. A., Manzoor, E., Pryzant, R., Sridhar, D., Wood-Doughty, Z., Eisenstein, J., Grimmer, J.,
Reichart, R., Roberts, M. E., et al. (2022). Causal inference in natural language processing: Estimation, prediction,
interpretation and beyond.Transactions of the Association for Computational Linguistics, 10:1138–1158.
Friedman, M. (1957). The permanent income hypothesis. InA theory of the consumption function, pages 20–37.
Princeton University Press.
Gao, Y., Lee, D., Burtch, G., and Fazelpour, S. (2025). Take caution in using llms as human surrogates.Proceedings
of the National Academy of Sciences, 122(24):e2501660122.
Goldberg, M. E. and Gorn, G. J. (1987). Happy and sad tv programs: How they affect reactions to commercials.
Journal of consumer research, 14(3):387–403.
Goli, A. and Singh, A. (2024). Frontiers: Can large language models capture human preferences?Marketing Science,
43(4):709–722.
Gowrisankaran, G. and Rysman, M. (2012). Dynamics of consumer demand for new durable goods.Journal of
Political Economy, 120(6):1173–1219.
Halawi, D., Zhang, F., Yueh-Han, C., and Steinhardt, J. (2024). Approaching human-level forecasting with language
models.arXiv preprint arXiv:2402.18563.
30

Hendel, I. and Nevo, A. (2006). Measuring the implications of sales and consumer inventory behavior.Econometrica,
74(6):1637–1673.
Hitsch, G. J. (2006). An empirical model of optimal dynamic product launch and exit under demand uncertainty.
Marketing Science, 25(1):25–50.
Horton, J. J., Filippas, A., and Manning, B. S. (2024). Large language models as simulated economic agents: What can
we learn from homo silicus? InProceedings of the 25th ACM Conference on Economics and Computation (EC).
Knight, S., Liu, L., and Kornish, L. J. (2025). Building persuasive stories with emotion sequences.Available at SSRN
5489708.
Knight, S., Rocklage, M. D., and Bart, Y. (2024). Narrative reversals and story success.Science Advances,
10(34):eadl2013.
Lee, K. (2024). Generative brand choice.
Li, P., Castelo, N., Katona, Z., and Sarvary, M. (2024). Frontiers: Determining the validity of large language models
for automated perceptual analysis.Marketing Science, 43(2):254–266.
Maharjan, S., Kar, S., Montes, M., Gonz´alez, F. A., and Solorio, T. (2018). Letting emotions flow: Success prediction
by modeling the flow of emotions in books. InProceedings of the 2018 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT), pages 259–265.
Manski, C. F. (2004). Measuring expectations.Econometrica, 72(5):1329–1376.
Manzoor, E. and Malik, N. (2023). Designing effective music excerpts.arXiv preprint arXiv:2309.14475.
Misra, S. and Nair, H. S. (2011). A structural model of sales-force compensation dynamics: Estimation and field
implementation.Quantitative Marketing and Economics, 9:211–257.
Mohammad, S. M. and Turney, P. D. (2013). Crowdsourcing a word–emotion association lexicon.Computational
intelligence, 29(3):436–465.
Nabi, R. L. and Green, M. C. (2015). The role of a narrative’s emotional flow in promoting persuasive outcomes.
Media Psychology, 18(2):137–162.
Nair, H. (2007). Intertemporal price discrimination with forward-looking consumers: Application to the US market
for console video-games.Quantitative Marketing and Economics, 5(3):239–292.
Peng, T., Gui, G., Brucks, M., Merlau, D. J., Jiarui Fan, G., Ben Sliman, M., Johnson, E. J., Althenayyan, A., Bellezza,
S., et al. (2025). Digital twins as funhouse mirrors: Five key distortions.arXiv preprint arXiv:2509.19088.
Piper, A., So, R. J., and Bamman, D. (2021). Narrative theory for computational narrative understanding. InProceedings
of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 298–311.
31

Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I. (2019). Language models are unsupervised
multitask learners. Technical report, OpenAI.
Reagan, A. J., Mitchell, L., Kiley, D., Danforth, C. M., and Dodds, P. S. (2016). The emotional arcs of stories are
dominated by six basic shapes.EPJ Data Science, 5(1):31.
Russell, J. A. (1980). A circumplex model of affect.Journal of personality and social psychology, 39(6):1161.
Rust, J. (1987). Optimal replacement of gmc bus engines: An empirical model of harold zurcher.Econometrica:
Journal of the Econometric Society, pages 999–1033.
Shachar, R., Muchnik, L., and Netzer, O. (2025). Sell me a story.SSRN Working Paper, (5236601).
Simonov, A., Ursu, R. M., and Zheng, C. (2023). Suspense and surprise in media product design: Evidence from
Twitch.tv.Journal of Marketing Research, 60(1):1–24.
Tan, E. S. (2008). Entertainment is emotion: The functional architecture of the entertainment experience.Media
Psychology, 11(1):28–51.
Tian, Y., Huang, T., Liu, M., Jiang, D., Spangher, A., Chen, M., May, J., and Peng, N. (2024). Are large language
models capable of generating human-level narratives? InProceedings of the 2024 Conference on Empirical Methods
in Natural Language Processing (EMNLP).
Timoshenko, A., Mao, C., and Hauser, J. R. (2026). Transforming the voice of the customer: Large language models
for identifying customer needs.
Toubia, O., Berger, J., and Eliashberg, J. (2021). How quantifying the shape of stories predicts their success.Proceedings
of the National Academy of Sciences, 118(26):e2011695118.
Toubia, O., Iyengar, G., Bunnell, R., and Lemaire, A. (2019). Extracting features of entertainment products: A guided
latent Dirichlet allocation approach informed by the psychology of media consumption.Journal of Marketing
Research, 56(1):18–36.
Van Laer, T., De Ruyter, K., Visconti, L. M., and Wetzels, M. (2014). The extended transportation-imagery model:
A meta-analysis of the antecedents and consequences of consumers’ narrative transportation.Journal of Consumer
Research, 40(5):797–817.
Veitch, V., Sridhar, D., and Blei, D. (2020). Adapting text embeddings for causal inference. InConference on
uncertainty in artificial intelligence, pages 919–928. PMLR.
Waldfogel, J. (2018).Digital Renaissance: What Data and Economics Tell Us about the Future of Popular Culture.
Princeton University Press.
Wei, Y. and Malik, N. (2025). Unstructured data, econometric models, and estimation bias.USC Marshall School of
Business Research Paper Sponsored by iORB.
32

A Appendix: Story Stimuli Generation for Survey
The goal of the story stimuli generation procedure is to produce stimuli that are representative across genres and exhibit
sufficient variation in valence and arousal for our validation tests. We generate the stimuli in three stages.
Stage 1: Premise and first-chapter generation.We generate 500 one-sentence story premises (100 per genre:
fantasy, literary fiction, romance, science fiction, thriller) usinggpt-5.4-mini-2026-03-17(temperature 1) with
the system prompt“You are a fiction author writing short three-chapter stories.”For each premise, we generate a
first chapter of approximately 250 words using the same model:“Write Chapter 1 of a three-chapter story. Each
chapter should be around 250 words. Chapter 1 should establish the characters, setting, and central conflict. Premise:
[premise text]. Write Chapter 1 now.”
Stage 2: Premise selection.We select 40 premises (8 per genre) from the 500 candidates to maximize diversity in
expected valence and arousal. For each candidate, we generate 50 imagined continuations usinggpt-4.1-mini-2025
-04-14(temperature 1) given its lower cost and extract valence and arousal from each continuation (temperature 0).
We compute expected valence and arousal as the average across continuations and select premises using inverse-density
sampling in this two-dimensional space.
Stage 3: Chapters 2 and 3 generation with emotional conditioning.For each selected premise, we generate four
second- and third-chapter variants using GPT-4.1-mini (temperature = 1.0). The four variants correspond to a 2×2
factorial design crossing valence (positive vs. negative) and arousal (high vs. low energy). We append the following
emotional tone instructions to the generation prompt. The valence instructions read:“Words can be positive or
negative. For example, very positive words include ‘vacation’ and ‘happiness,’ while very negative words include
‘torture’ and ‘mourn.’ Write in a [positive/negative] way.”The arousal instructions read:“Words can be low or high
energy. For example, very high energy words include ‘scare’ and ‘exciting,’ while very low energy words include
‘calm’ and ‘dull.’ Write in a [high-energy/low-energy] way.”The full user prompt for chapters 2 and 3 is:“Here is
Chapter 1 of a story: [Ch1 text]. Write Chapter 2 and Chapter 3, continuing from Chapter 1. Each chapter should be
around 250 words. Chapter 3 should provide a resolution to the story’s central conflict. [tone instructions]. Write the
chapters now.”
This yields 160 unique story variants (40 premises×4 conditions) and 200 unique chapters (40 shared first chapters
plus 160 second chapters).
B Appendix: Sensitivity of Number of Imagined Continuations
This section presents the sensitivity analysis for the number of imagined continuations𝑁. In our main analysis, we
set𝑁=50 imagined continuations per chapter. To ensure that our results are robust to this choice, we examine how
expected valence and arousal and the semantic path features stabilize as𝑁increases.
33

B.1 Bootstrap Procedure
To determine the number of imagined continuations needed, we conduct a bootstrap resampling analysis on a pilot
sample of approximately 367 chapters from the observational data. We examine the emotion and semantic path
features. We assume 100 imagined continuations is sufficient to recover the ground truth and compute the ground-truth
estimates using all 100 available imagined continuations for each chapter𝑐: Expectation 𝑐 = 1 𝐾 ˝𝐾 𝑘=1𝑧𝑘 𝑐, where𝑧 𝑘 𝑐 is
the feature value extracted from the𝑘th imagined continuation of chapter𝑐. We then simulate the scenario of having
only𝑁imagined continuations. For each𝑁∈{1,2,...,100}, we run𝐵=1,000 bootstrap iterations with replacement.
Across the𝐵iterations, we compute the bias (average deviation from ground truth) and the bootstrap standard deviation
(estimation noise) for the expectation estimates.
B.2 Reliability Ratio
To formalize the precision of the expectation estimate at a given𝑁, we compute a reliability ratio that quantifies the
fraction of observed chapter-to-chapter variance in the expectation that is true signal versus sampling noise. Let𝜎 2 𝐵
denote the between-chapter variance of the true chapter-level expectations (i.e., the signal), and let ¯𝜎 2 𝑊 denote the
average within-chapter variance across imagined continuations (i.e., the noise source). When using only𝑁imagined
continuations per chapter, the noise variance injected into each chapter’s expectation estimate is ¯𝜎 2 𝑊/𝑁, and the
reliability ratio is𝜌(𝑁)=
𝜎2 𝐵
𝜎2 𝐵+¯𝜎2 𝑊/𝑁 . A reliability of𝜌=0.9 indicates that 90% of the observed chapter-to-chapter
variance in the expectation estimate is true signal. By the classical measurement error attenuation result, OLS regression
coefficients using this feature are attenuated by a factor of approximately𝜌(i.e., ˆ𝛽≈𝜌·𝛽). Higher reliability implies
less bias in downstream regressions.
B.3 Results
At𝑁=50, all five features achieve a reliability ratio above 0.90, with valence reaching approximately 0.99 and
circuitousness at approximately 0.90. The marginal improvement from𝑁=50 to𝑁=100 is negligible, adding only
about 0.01 to the reliability across features. Both the bootstrap standard deviation and bias stabilize well before𝑁=50,
indicating that additional imagined continuations beyond this point yield diminishing returns.
C Appendix: Survey Details
This appendix provides details of the survey instrument used in the survey validation study. Participants were recruited
to complete a study about story beliefs. After providing informed consent, participants read two short stories, each
presented over multiple chapters. For each story, participants first read Chapter 1 and then answered questions about
the emotional content of the chapter, their interest in continuing, and their beliefs about the emotional content of the
next chapter. Participants then read Chapter 2 and answered analogous questions. Finally, participants were given the
option to read Chapter 3, which provides a revealed-preference measure of continued engagement.
34

Realized Chapter Ratings.After each chapter, participants were asked to rate its valence and arousal. For valence,
participants saw the following explanation: “Words can be characterized as being different levels of negative or positive.
For example, very negative words include “torture” and “mourn,” neutral words include “vertical” and “beaver,” and
very positive words include “vacation” and “happiness.”” They were then asked: “Where on the very negative to very
positive spectrum do you think the words in the chapter are?” Responses were given on a 1–5 scale.
For arousal, participants saw the following explanation: “In addition to being negative or positive, words can also
be characterized as being low or high energy. For example, very low energy words include “calm” and “dull,” medium
energy words include “relationship” and “religion,” while very high energy words include “scare” and “exciting.””
They were then asked: “Where on the very low energy to very high energy spectrum do you think the words in the
chapter are?” Responses were given on a 1–5 scale.
Stated Interest.After each of the first two chapters, participants were asked: “How interested are you in continuing
to read the next chapter?” Responses were given on a 1–5 scale.
Beliefs About Next-Chapter Valence and Arousal.Participants were asked to assign probabilities to possible
valence levels of the next chapter: “Based on the chapter you just read, what do you think is the likelihood that the text
of the next chapter will be very negative or very positive? Please assign a percentage to each. The total must sum to
100%. ” They then assigned percentages across the following categories: very negative, somewhat negative, neutral,
somewhat positive, and very positive.
Participants were also asked to assign probabilities to possible arousal levels of the next chapter: “Based on the
chapter you just read, what do you think is the likelihood that the text of the next chapter will be very low energy or
very high energy? Please assign a percentage to each. The total must sum to 100%.” They then assigned percentages
across the following categories: very low energy, somewhat low energy, medium energy, somewhat high energy, and
very high energy.
Revealed Preference for Continuing.After completing the Chapter 2 questions, participants were told that reading
the final chapter was optional: “The next chapter is the final chapter of this story and reading it is optional for this
survey. If you decide to read the final chapter, it will take 1–2 minutes and we will ask you one additional question. If
you decide not to read the final chapter, you will continue to the next story.” Participants were then asked: “Would you
like to read the next chapter?” The response options were “No” and “Yes.”
D Appendix: Survey Validation Robustness Checks
We conduct a number of robustness checks for the main findings obtained from the survey data. First, we show that the
positive relationship between stated expectations and LLM-derived expectations hold across all five genres captured in
the survey data in Figure D1 and Table D1.
35

Figure D1: LLM Expectations and Survey Expectations Across Genres
Table D1: LLM-Derived Expectations Approximate
Survey-Elicited Expectations Across Genres
Expected Valence Expected Arousal
ˆ𝛽 𝑅 2 ˆ𝛽 𝑅 2 𝑁
All genres0.571 ∗∗∗ 0.369 0.563 ∗∗∗ 0.297 200
fantasy 0.638 ∗∗∗ 0.321 0.622 ∗∗ 0.214 40
literary 0.598 ∗∗∗ 0.522 0.488 ∗∗ 0.228 40
romance 0.673 ∗∗∗ 0.476 0.589 ∗∗∗ 0.311 40
scifi 0.384 ∗ 0.143 0.708 ∗∗∗ 0.300 40
thriller 0.565 ∗∗∗ 0.403 0.543 ∗∗∗ 0.429 40
Note:∗∗∗𝑝<0.01; ∗∗𝑝<0.05; ∗𝑝<0.1.
In Table D2, we add controls for LLM-rated current valence and arousal. Adding these variables reduces the slopes
(from 0.57 to 0.26 for valence; from 0.56 to 0.32 for arousal), consistent with the expectations being partly informed
by the current chapter’s emotional content. Crucially, both slopes remain strongly significant (𝑝 <0.001), confirming
that the LLM expectations capture forward-looking beliefs beyond what current chapter features explain.
Consistent with the literature that has found that off-the-shelf LLMs tend to produce overly concentrated distributions
relative to humans (Bisbee et al., 2024; Deng et al., 2026), we find that the LLM-derived uncertainty measures for
valence and arousal have lower variance than the equivalent based on human response. To further assess whether
LLM-derived uncertainty can proxy human uncertainty, we regress survey uncertainty on LLM-derived uncertainty for
valence and arousal. Table D3 presents the regression coefficients. We find that the coefficients are small in magnitude,
36

Table D2: Validation Survives Controlling for Current Valence and
Arousal
Survey expected valence Survey expected arousal
Baseline + Controls Baseline + Controls
(1) (2) (3) (4)
LLM expected valence 0.571*** 0.255***
(0.053) (0.039)
LLM expected arousal 0.563*** 0.322***
(0.062) (0.052)
Current valence 0.371*** 0.090***
(0.022) (0.022)
Current arousal 0.053** 0.315***
(0.021) (0.027)
Observations 200 200 200 200
R2 0.369 0.755 0.297 0.619
Adjusted R2 0.366 0.752 0.293 0.613
Note:∗∗∗𝑝<0.01; ∗∗𝑝<0.05; ∗𝑝<0.1.
statistically insignificant, and explain little of the variation in survey responses. Therefore, the distribution of imagined
continuations we generated cannot approximate the human stated uncertainty.
Table D3: LLM-derived Uncertainty and Survey-derived Uncertainty
Dependent variable:
Survey uncertainty valence Survey uncertainty arousal
(1) (2)
LLM uncertainty valence 0.142
(0.146)
LLM uncertainty arousal 0.077
(0.259)
Constant 0.799 ∗∗∗ 0.664∗∗∗
(0.051) (0.056)
Observations 200 200
R2 0.005 0.0004
Adjusted R2 −0.0003−0.005
Note:∗∗∗𝑝 <0.01;∗∗𝑝 <0.05;∗𝑝 <0.1.
37

E Feature Extraction Implementation Details
This appendix provides implementation details for the imagination generation and feature extraction procedures
described in Section 3.
E.1 Imagination Generation
We generate imagined story continuations usinggpt-4o-mini-2024-07-18. For each chapter𝑡in book𝑖, we provide
the full text of chapters 1 through𝑡as context and prompt the model to generate the next chapter using the prompt
described in Section 3.
We generate𝑁=50 continuations per chapter using OpenAI’snparameter, which produces all continuations in
a single API call with identical context. The generation parameters are: temperature=1.0, top p=1.0, frequency
penalty=0.0, and presence penalty=0.0. Each continuation can be up to 16,000 tokens. The context window
accommodates up to 90,000 words of preceding chapter text; when the preceding text exceeds this limit, we truncate
from the beginning, starting from the first complete sentence after the truncation point.
E.2 Emotion Features: Valence and Arousal
We extract valence and arousal from each chapter and imagined continuation usinggpt-4.1-mini-2025-04-14
(temperature 0). The model receives the chapter text and returns integer ratings for each dimension on a 1–5 scale.
The prompt is as follows:
System prompt:“Rate the overall emotional tone of the following text on two dimensions:
1. Valence (1–5): how negative vs positive (1 = very negative, 5 = very positive)
2. Arousal (1–5): how calm vs intense (1 = very calm, 5 = very intense)
Respond ONLY with a JSON object:{“valence”:⟨int⟩, “arousal”:⟨int⟩}”
User prompt:[chapter text]
The model returns a JSON object with two integer fields. Valence captures how negative (1) versus positive (5) the
overall emotional tone of the chapter is. Arousal captures how calm (1) versus intense (5) the emotional energy is. We
apply this extraction to both the actual chapter text and each of the𝑁imagined continuations independently.
E.3 Semantic Path Features
We measure the speed, volume, and circuitousness of each chapter and imagined continuation following the approach
proposed by Toubia et al. (2021). These measures capture the dynamics of narrative content within a chapter by
analyzing the trajectory of text embeddings.
To operationalize, we embed story text usingtext-embedding-3-large, which produces 3,072-dimensional
embedding vectors. We pass the original chapter text as written, truncating any segment that exceeds 8,000 tokens
38

to stay within the model’s 8,192-token context limit. Each chapter is divided into𝑇=20 equal-sized segments by
splitting its text into𝑇consecutive spans of equal word count. We embed each chunk’s text directly, obtaining one
3,072-dimensional vector per chunk. We then use these embeddings to compute speed, volume, and circuitousness.
E.4 11 Narrative Features
We extract eleven narrative dimensions (narrative tension, curiosity, emotional complexity, character agency, social
conflict, resolution, cliffhanger intensity, narrative vividness, pacing, character relatability, cognitive complexity) using
gpt-5.4-nano-2026-03-17(temperature 0). The dimensions are defined based on the following text:
Narrative tension / Stakes (1–5):1 = nothing at stake, no consequences, 2 = low stakes, minor concerns, 3
= moderate stakes, 4 = high stakes, significant consequences for characters, 5 = extreme stakes, life-changing or
life-threatening.
Curiosity / Information gaps (1–5):1 = everything is explained, no unanswered questions, 2 = minor open
questions, 3 = some curiosity-provoking elements, 4 = significant unanswered questions or mysteries, 5 = major
information gaps that demand resolution.
Emotional complexity (1–5):1 = simple, single emotion dominates clearly, 2 = mostly one emotion with slight
nuance, 3 = mixed emotions, some tension between feelings, 4 = complex emotional layering, conflicting feelings, 5 =
deeply complex, multiple conflicting emotions intertwined.
Character agency (1–5):1 = characters are entirely passive, things happen to them, 2 = mostly reactive, limited
initiative, 3 = moderate agency, some active choices, 4 = characters actively drive the plot through their decisions, 5 =
strong agency, characters’ choices are the primary plot engine.
Social conflict (1–5):1 = no interpersonal tension, harmonious relationships, 2 = minor disagreements or mild
tension, 3 = moderate interpersonal conflict, 4 = significant relational tension, confrontation, or betrayal, 5 = intense
social conflict, deep interpersonal rupture.
Resolution vs. Complication (1–5):1 = fully resolves existing plot threads, provides closure, 2 = mostly resolves
with minor new elements, 3 = balanced — resolves some threads while introducing others, 4 = mostly introduces new
complications or questions, 5 = purely complicating — opens new threads without resolving any.
Cliffhanger intensity (1–5):1 = fully resolved ending, no open questions, 2 = mostly resolved, minor loose ends,
3 = some unresolved tension or open questions, 4 = significant unresolved tension or a question that demands the next
chapter, 5 = major cliffhanger — the chapter ends at a critical moment of suspense.
Narrative vividness (1–5):1 = abstract, tell-not-show, minimal sensory detail, 2 = some concrete details but
mostly summary, 3 = moderate sensory detail and scene-setting, 4 = vivid and immersive, strong sensory language, 5
= extremely vivid, deeply immersive, rich sensory and emotional detail.
Pacing (1–5):1 = very slow, contemplative, mostly internal reflection, 2 = slow, unhurried, deliberate unfolding,
3 = moderate pace, balanced action and reflection, 4 = fast-paced, events progress quickly, 5 = very fast, rapid-fire
events, high urgency.
Character relatability (1–5):1 = characters feel distant, generic, or hard to empathize with, 2 = somewhat flat
39

characters with limited emotional depth, 3 = moderately relatable, some emotional resonance, 4 = relatable characters
with clear motivations and emotional depth, 5 = deeply relatable, strong emotional connection, compelling inner life.
Cognitive complexity (1–5):1 = simple, straightforward, no ambiguity, 2 = mostly straightforward with minor
complexity, 3 = moderate complexity, some ambiguity or layering, 4 = complex, requires attention, plot twists or moral
ambiguity, 5 = very complex, multiple layers of meaning, significant ambiguity.
40

A Web Appendix: Extraction of 11 Narrative Dimensions
A.1 Extraction of 11 Narrative Dimensions
We extract eleven narrative dimensions (narrative tension, curiosity, emotional complexity, character agency, social
conflict, resolution, cliffhanger intensity, narrative vividness, pacing, character relatability, cognitive complexity) using
gpt-5.4-nano-2026-03-17(temperature 0). The prompts for the generative and direct-elicitation implementations
share the same system-prompt structure and differ only in the task they pose and the response format they request.
Generative implementation.The prompt asks the model toratethe most recent chapter it has been shown. That
chapter is either the actual chapter or one imagined continuation, presented in an identical format so that the model
cannot tell the two apart. For each dimension, it returns a single integer rating on a 1–5 scale. Applying this prompt to
the imagined continuations of a chapter and averaging the ratings yields the expected feature value, while applying it
to the actual chapter yields the realized value.
Direct elicitation.The prompt asks the model topredictthe next, unread chapter from the chapters read so far. For
each dimension, it directly returns a five-bin probability distribution (five percentages, one per rating level, summing
to 100).
The system prompt has three components: a general instruction (which differs by implementation), the feature
definitions (shared across both implementations), and an output specification (which differs by implementation). We
first give the shared feature description, then the complete system prompt and user prompt for each implementation.
A.1.1 Shared Feature Description
Both variants use the same feature definitions (Appendix E.4).
A.1.2 Generative Implementation and Actual Content
This variant rates a single chapter, either the actual chapter𝑡or one imagined continuation of it, on each of the eleven
dimensions, given the preceding chapters as context.
System prompt.The system prompt concatenates the general instruction, the shared feature description, and the
output specification:
You are an average reader. You have been reading a story chapter by chapter. The chapters you have
read so far include those in<preceding chapters as context>and<latest chapter to rate>,
and the chapter to rate appears in<latest chapter to rate>. What is your rating for each of the eleven
dimensions defined below for the chapter in<latest chapter to rate>?
[shared feature description]
Provide your ratings for the chapter in<latest chapter to rate>. For each dimension, return a single
integer between 1 (lowest) and 5 (highest) that represents your rating for the chapter in<latestchapter to rate>.
41

Respond ONLY with a JSON object. Each key maps to a single integer:{"tension": <int>,
"curiosity": <int>, ..., "cog complexity": <int>}.
User prompt.
<preceding chapters as context>
[text of chapters 1 through𝑡−1]
</preceding chapters as context>
Rate the latest chapter:
<latest chapter to rate>
[text of the actual chapter𝑡or one imagined continuation]
</latest chapter to rate>
A.1.3 Direct Elicitation
This variant predicts the next, unread chapter, returning for each of the eleven dimensions a probability distribution
over the 1–5 rating scale.
System prompt.The system prompt concatenates the general instruction, the shared feature description, and the
output specification:
You are an average reader. You have been reading a story chapter by chapter. The chapters you have read
so far appear in the user message. What is your belief for each of the eleven dimensions defined below for
the NEXT chapter?
[shared feature description]
Provide your beliefs for the NEXT chapter, which you have not yet read. For each dimension, return five
integers that represent the chance of each rating happening in the next chapter — these are PERCENTAGES,
not ratings, that must sum to 100. The five elements correspond to rating 1 (first element) through rating 5
(last element). Example for one dimension: [10, 30, 30, 20, 10] means 10% chance the next chapter rates
1, 30% chance it rates 2, 30% chance it rates 3, 20% chance it rates 4, 10% chance it rates 5. The five
percentages must sum to 100 (10 + 30 + 30 + 20 + 10 = 100). Respond ONLY with a JSON object. Each
key maps to an array of five percentages summing to 100, ordered from rating 1 to rating 5:{"tension":
[p1, p2, p3, p4, p5], ..., "cog complexity": [p1, p2, p3, p4, p5]}.
User prompt.
<story so far>
[text of chapters 1 through𝑡]
</story so far>
42

B Web Appendix: Data Preprocessing for Observational Data
We preprocess the observational data at the text, chapter, and book levels. At the text level, we remove non-story
material such as trailing author notes, HTML tags, HTML entities, and emojis. At the chapter level, we distinguish
plot-related story chapters from contextual material, such as prologues, character lists, author notes, and other non-plot
text. Contextual chapters are retained when useful for generating imagined continuations, but are excluded from feature
extraction and analysis. We also exclude chapters that are too short, extreme length outliers, non-English, explicit,
incoherent as narrative text, associated with zero reads, or linked to invalid engagement records. To avoid overlap with
the model’s training data, we exclude chapters created before December 1, 2023.
At the book level, we remove books that are marked as mature or contain explicit-content keywords in their metadata.
We also require books to have sufficient readership (first-chapter read count>50), have at least 10 plot-related story
chapters after filtering, and plausible chapter length. For analysis, we retain the first 9 plot-related chapters of each
eligible book. We further exclude books that are predominantly non-English or have average chapter lengths that are
unusually short or long, which often indicate non-narrative content or entire books uploaded as single chapters.
C Web Appendix: Sensitivity of Semantic Path Features
Figure C1: Semantic Speed and Circuitousness Coefficient Sensitivity
Note: Sensitivity of the semantic path coefficients to adding one narrative dimension at a time. The baseline specification regresses each engagement
ratio on current and expected speed and circuitousness, with word count and log readership controls and chapter fixed effects. Each row adds the
realized and expected ratings of a single dimension to that baseline. The dot is the partial coefficient, the whisker its 95% confidence interval
(two-way clustered by user and chapter), and the dashed red line highlights the baseline estimate.𝑁=8,399.
43

D Web Appendix : Embedding PCA Implementation Details
We embed each actual chapter and each imagined continuation withtext-embedding-3-large, which maps a passage
of text to a 3,072-dimensional vector. Because this dimensionality is far larger than the number of stories in either
empirical setting, we do not use the raw embeddings as regressors; instead we reduce them with principal component
analysis (PCA). We apply PCA separately within each empirical setting, the survey data and the observational data, and
in each case we fit the PCA on the embeddings of theactualchapter text only since the actual text should capture the
variation in dimensions that stories differ over. To choose how many components to retain, we inspect the scree plot of
eigenvalues and retain the number of dimensions up till elbow - 1. The elbow plot suggests retaining five components
for the survey data and three components for the observational data.
Table D1: Which Embedding Components Are Associated with Survey Stated Interest?
DV: Stated Interest
(1) Current PCs (2)+Expectations
Coef. SE Coef. SE
PC 1−1.292 ∗∗ (0.562)−1.454 ∗∗ (0.590)
PC 2 0.336 (0.485) 0.355 (0.640)
PC 3−0.670 ∗∗ (0.270)−0.591 (0.393)
PC 4 0.536 (0.396)−0.092 (0.606)
PC 5 0.903 ∗∗ (0.446) 1.194 (0.751)
Expected PC 1 0.054 (1.021)
Expected PC 2 0.028 (0.897)
Expected PC 3−0.570 (1.141)
Expected PC 4 0.951 (0.848)
Expected PC 5−0.328 (0.908)
Chapter number FE Yes Yes
User FE Yes Yes
Observations 1,052 1,052
R2 0.723 0.724
Adjusted R2 0.628 0.627
Note:Two-way clustered standard errors for user and
chapter.∗∗∗𝑝 <0.01;∗∗𝑝 <0.05;∗𝑝 <0.1.
44

Table D2: Which Embedding Components Are Associated with Voting and Commenting?
Vote-to-Read Comment-to-Read
Baseline+Expectations Baseline+Expectations
Coef. SE Coef. SE Coef. SE Coef. SE
Embedding Principal Components
PC 1−0.117 ∗∗∗ (0.011) −0.112 ∗∗∗ (0.029) −0.091 ∗∗∗ (0.012) −0.038(0.030)
PC 2 0.075 ∗∗∗ (0.010)0.207 ∗∗∗ (0.035) −0.043 ∗∗∗ (0.011)0.026(0.037)
PC 3−0.121 ∗∗∗ (0.012) −0.053 ∗∗∗ (0.019) −0.047 ∗∗∗ (0.013) −0.029(0.020)
Expected PC 1−0.108 ∗∗∗ (0.031) −0.107 ∗∗∗ (0.032)
Expected PC 2−0.165 ∗∗∗ (0.036) −0.089 ∗∗ (0.037)
Expected PC 3−0.148 ∗∗∗ (0.020) −0.069 ∗∗∗ (0.021)
Chapter Number FE Yes Yes Yes Yes
Observations 8,399 8,399 8,399 8,399
R2 0.1293 0.1371 0.0478 0.0501
Adjusted R2 0.1279 0.1355 0.0463 0.0483
𝐹(vs baseline) 25.30 ∗∗∗ 6.82∗∗∗
Note:∗∗∗𝑝 <0.01;∗∗𝑝 <0.05;∗𝑝 <0.1. Log first-chapter read count and word count controlled.
45
