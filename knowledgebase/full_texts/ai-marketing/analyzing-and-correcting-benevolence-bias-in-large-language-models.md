---
title: Analyzing and Correcting Benevolence Bias in Large Language Models
url: https://arxiv.org/abs/2608.24912
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Yuanzi Li
- Junhao Wang
- Minghui Liu
- Boyi Li
- Bingchen Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.24912
pages: 17
chars: 58969
fetched_at: '2026-11-08T13:33:40+00:00'
kb_version: 1
---

# Analyzing and Correcting Benevolence Bias in Large Language Models

Analyzing and Correcting Benevolence Bias in Large
Language Models
Yuanzi Li1, Junhao Wang 1, Minghui Liu 2, Boyi Li 1, Bingchen Chen 1, Zihang Tian 1,
Jingyu Zhao 3, Yuhan Wang 4, Lei Wang 1, Pei Wang 1, Jinchao Wu 1, Xu Chen 1,˚
1Gaoling School of Artificial Intelligence, Renmin University of China, Beijing, China
2School of Computer Science and Engineering, Sun Yat-sen University, Guangzhou, China
3School of Computer Science and Technology, Shandong University, Qingdao, China
4School of Mathematical Sciences, Peking University, Beijing, China
*Corresponding authors
Abstract
Large language models (LLMs) are increasingly used as stand-ins for human respondents,
from opinion polls and simulated survey participants to agent-based social simulations. These
uses rest on one assumption: that conditioning a model on who a person is yields answers
resembling those of real people from that group. Here we identify and measurebenevolence
bias, a small but consistent tendency for aligned LLMs to lean toward the kinder, safer, more
socially approved answer on value-laden survey questions. Across 18 widely used models, four
social-science datasets (ANES, GSS, WVS, and a cross-cultural prospect-theory replication) and
six psychological categories, we find that the bias is a stable model property, not a quirk of any
one system: it points the same way across models, grows with model size, and traces to the
post-training stage. Prompt language and framing change its size but never its direction, and a
“malicious persona” stress test shows a one-sided limit: aligned models struggle to play people
who are less kind, less prosocial or more harm-tolerant than average. The issue is thus not
only a shifted average, but a narrowed range of people the model can imitate. The bias sits
in the middle of the answer distribution rather than its tails, and survives changes in sampling
temperature and simple prompted reflection. The encouraging news is that it is easy to diagnose
and straightforward to fix: a light-touch contrastive calibration, which needs no retraining and
works on black-box APIs, brings all six categories back to the human baseline. Our results
give researchers a clear map of where aligned LLMs can already be trusted as human stand-ins,
where they need care, and a ready-to-use method for closing the gap.
Keywords:large language model, alignment, value representation, social simulation, survey
research
Introduction
Large language models (LLMs) are increasingly used as stand-ins for human respondents across
the social and behavioural sciences: to answer opinion polls, to simulate survey participants, to
populate agent-based models of social processes, and to supply synthetic samples where collecting
human data at scale is hard [1–4]. These uses promise faster, cheaper and larger studies, and they
rest on one idea: that asking a model to answer as a given kind of person yields answers resembling
what real people of that kind would say. Whether today’s aligned models live up to this idea, and
1
arXiv:2608.24912v1  [cs.HC]  26 Jul 2026

on which questions, has never been tested systematically. Answering that question is what turns
LLM-based simulation from a promising idea into a dependable method.
The question matters because the same models are also built for a different job: from chat
assistantstopolicytools, being“helpful” and“harmless” isacoredesigngoal. Reinforcementlearning
from human feedback [5–7], supervised instruction tuning [8], and constitutional or preference-
based safety training [9–12] all steer models toward answers that people find helpful, harmless
and agreeable, rewarding prosocial wording, caution around possible harm, and widely acceptable
choices [13, 14]. This mark points in the same direction as the categories along which value-laden
survey questions are scored [15, 16]. The training that makes models safer may therefore nudge
the whole distribution of their attitudes, not just sharpen it. If so, any conclusion drawn from a
synthetic sample inherits that nudge, and a researcher looking only at the model’s answers has no
way to notice. Seeing the nudge clearly and measuring it is the first step toward trusting these
tools.
Earlier work has assembled pieces of this picture: today’s models lean liberal on policy questions
and favour certain demographic profiles [17–20]; fine-tuning changes behaviour on contested topics
and value judgements [21–23]; persona conditioning moves answers in the right direction but does
not reliably reproduce the true distribution of a group [24–26]; aligned models drift toward answers
that match what the user seems to want [13, 14]; and theory suggests alignment objectives cannot
fully remove every unwanted behaviour [16]. What is still missing is a clear, category-by-category
map of this alignment-driven shift: which value categories are affected; how it changes with model
size and capability; whether prompt-level tools can move it; whether it belongs to the models or
to the datasets; and whether it is only a shift in the average, or also a shrinking of the range of
answers a model can produce. Without such a map, neither model builders nor downstream users
can check for this bias or reason about it.
Two things make this map especially timely. First, exactly this generation of aligned models is
being adopted at scale for synthetic samples and “silicon sample” experiments [2, 24, 26], so any value
shift is quietly passed along to a growing body of work. Second, established survey instruments such
as the World Values Survey [27], the General Social Survey [28], the American National Election
Studies [29] and cross-cultural prospect-theory replications [30] already provide a human reference,
and they cover exactly the value domains alignment is most likely to touch. Together these supply
both the motivation and the measuring stick.
Here we provide such a map across 18 widely used LLMs and four social-science datasets (ANES,
GSS, WVS, and a cross-cultural prospect-theory replication; Fig. 1a), with questions spanning four
social domains and six benevolence-bias categories (Fig. 1b,d,e). The six-category scheme splits
“benevolence” into separate strands: social-desirability self-presentation [31], harm aversion, proso-
cial motivation, benevolent interpretation, fairness optimism, and emotional softening (Fig. 1c).
Two simple metrics track the bias: the Benevolence Tendency Bias (BTB), the overall shift at the
population level, and the Benevolence Win Rate (BWR), the direction question by question. We
then study the bias at three points in the pipeline: at the model level, whether it is stable, how
it scales, and whether it traces to post-training; at the input level, whether it is just the default
assistant voice or a deeper prior carried across languages, framings and personas; and at the output
level, whether it lives only at the most likely answer or runs through the whole distribution, using
contrastive calibration first as a measuring tool and then as a practical fix.
Three findings map the shape of the bias and how to handle it. First, it points consistently one
way and lands hardest where alignment aims: 83 of 108 BTB cells are positive, 75 of 108 BWR
cells sit above the baseline, all 18 models shift positively on social desirability and 17 of 18 on
harm aversion; the bias grows with size in both Qwen families, is only weakly linked to capability
(R2“0.16), ranks models consistently across the three large surveys (Spearman’sρ0.54–0.63), and
2

traces to post-training. Second, it is not just a shifted average: a “malicious persona” stress test
can push models below their normal values on fairness optimism and emotional softening, but never
below the human baseline on social desirability, prosociality or harm aversion; on those axes the
models have lost some ability to imitate the less-benevolent end. Third, prompt-level tools change
its size but never its direction, whereas contrastive calibration at a moderate setting pulls all six
categories into a tight band around the human baseline. Alignment thus shifts, rather than merely
polishes, the value distribution of today’s models. That is encouraging news for practice: because
the shift is predictable and distributional, a light-touch correction with no retraining can bring
aligned LLMs back in line with the human reference, so they can be used responsibly as proxies for
human respondents.
Results
Model level
The bias is common but concentrated on a few dimensions.Across the four datasets
(ANES, GSS, WVS and PT), we compared 18 models against the human baseline (BTB“0,
BWR“0.5) on six bias dimensions (Table 1). Of the 108 BTB cells, 83 are positive; of the 108
BWR cells, 75 are above 0.5; the mean BTB is 0.027 and the mean BWR is 0.527. The bias thus
points the same way across models and dimensions, though it is moderate in size. It is largest
on social desirability, where every model is positive (mean BTB“0.059, mean BWR“0.565),
and harm aversion, where 17 of 18 are (mean BTB“0.066, mean BWR“0.569). Prosociality,
benevolent interpretation and fairness optimism are positive on average but smaller, and emotional
softening shows no clear shift (mean BTB“0.001, mean BWR“0.494). Individual models still
differ: GPT-4.1-mini, GPT-5-mini, Qwen3-32B, Qwen2.5-72B-Instruct and Llama-3.3-70B sit above
the baseline on almost every dimension, whereas Gemini3-Flash, DeepSeek-V4-Pro, Mimo-v2.5 and
Gemma-3-27B pair a strong social-desirability or harm-aversion shift with near-neutral or negative
values elsewhere. Benevolence bias is thus not a uniform push along every value axis, but a positive
shift focused on social approval, safety and harm avoidance.
The bias grows as models get larger.Within the Qwen3 family (0.6B, 1.7B, 4B, 8B, 14B and
32B), with datasets, prompting and scoring fixed, the mean BTB rises from close to the human
baseline at 0.6B to a clearly higher value at 32B, and the mean win rate moves from about chance to
well above 0.5 (Fig. 2a). Larger models therefore give benevolent answers more often. The growth
is uneven across categories (Fig. 2b): social-desirability and fairness-optimism bias grow fastest,
harm aversion turns from slightly negative in small models to positive in large ones, and the other
categories change less. The per-question distributions show the same pattern (Fig. 2c): as Qwen3
grows, the BTB distribution shifts right and develops a heavier positive tail, so the rising average
reflects a growing share of high-bias questions rather than a uniform push. The Qwen2.5 family
behaves similarly (Supplementary Information).
Turning on model reasoning reduces the bias.We then tested whether letting a model “think”
before answering changes the bias, using three families with a switchable thinking mode (GLM-5,
Qwen3-14B and DeepSeek-V4-Flash) and holding questions, scoring and dataset mix fixed. Per-
question BTB fell in all three models once thinking was on. For GLM-5, most points fall below the
identity line, across social desirability, harm aversion, fairness optimism and benevolent interpre-
tation (Fig. 2d). The category profile of Qwen3-14B pulls in toward the neutral centre, with the
biggest drops where the bias started strongest (Fig. 2e). The per-question distribution of DeepSeek-
V4-Flash shifts toward zero, with fewer strongly positive answers (Fig. 2f). The improvement is
partial: most categories keep a small positive residual, and no model fully matches the human
3

a
ExampleDefinitionCategory
How important are friends in
your life?
Models favor generosity and
cooperation over self-
interest more than real
humans do.
Prosocial
(PSB)
Do you consider thrift, such as
saving money and things, to be
an especially important quality
for children to learn at home?
Models prefer socially
acceptable, politically
correct responses,
suppressing realistic but
controversial views.
Social-
Desirability
(SDB)
Do you think we are spending
too much, too little, or about the
right amount on halting the
rising crime rate?
Models are overly risk-
averse, refusing actions with
even minimal harm potential
due to safety alignment.
Harm-
Aversion
(HAB)
Would you not like to have
people who speak a different
language as neighbors?
Models interpret ambiguous
situations charitably,
overlooking potential
malicious intent or negative
context.
Benevolent-
Interpretation
(BIB)
How satisfied are you with your
life as a whole these days?
Models soften negative
emotions, making
expressions of anger or
conflict more polite than
natural human reactions.
Emotional-
Softening
(ESB)
In your view, how often are
votes counted fairly in this
country’s elections?
Models overestimate social
fairness, institutional
trustworthiness, and the
likelihood of cooperation.
Fairness-
Optimism
(FOB)
cb
d
e
Stimulus Corpus
Construction
Cascaded Taxonomic
Annotation
Human
Simulation
LLMBias
Quantification
  




'!$#'%& #"%





  %&#$(






 %&#$( %&$ '& #"
%$%"
	



!$'
	


&



	
! !'

	



! #$"%$!
	



"!"
!$
#
	$







	
! !  !$

#! !%%!$
๭ 1: ࠎሙࡹܒაٳোุ༢b ađ ࠎሙੀӱۀফb Ֆჷეਘ९൬ࠢջႵࡎᆴڵᄛ֥໙जีཛđ ࡼఃٳ஥֞ഠ߶ਵთა೿ၩ
ொҵোљ֥ࠩ৳ٳোุ༢ᇏđႨႿՖ LLM ႄԛଆ୅ದো߭ճđѩაࣜဒྟದোཙႋٳ҃бࢠၛਈ߄ொҵbbđቋᇔЌ਽
֥ 406 ۱ࠎሙีཛᄝੂ۱೿ၩொҵোљᇏٳ֥҃ğ౔ഠ߶čPSBĎ aഠ߶௹ྸčSDBĎ aхݝčHABĎ a೿ၩࢳ൤čBIBĎ a
౦࿂ೈ߄čESBĎ܄ބ௜ুܴčFOBĎ bcđোљקၬࠣսіྟ໙जีཛđඪૼૄ۱ொҵົ؇෮ѽሚ֥ྛູౠཟbdđࠎሙ
ᄝ໓߄aᆟᇍaمੰ࠶ࣜބඹ۱ഠ߶ਵთᇏ֥ቆӮđཁൕٳ஥۲֞ਵთ֥ีཛඔਈაб২beđՖჷඔऌ֞ࠢਵთބொҵ
োљ֥Ԋࠒੀ๭đሹࢲ ANESaGSSaWVS ބ PT ีཛೂޅแԉቋᇔࠎሙٳোุ༢b
न RTB Ֆ 0.6B ൈ࣍ࢤದোࠎཌđഈശ֞ቋնܿଆൈ֥ૼཁۚࢠ౼ᆴč๭ 2aĎ b௜न഻ੱӯགྷཌྷ๝103
ࠖ݅đ Ֆቋཬܿଆൈ࣍රෛࠏඣ௜đ ၍֞׮32B ൈཁᇷۚႿ 0.5b ၹՎđ ۷ն֥Qwen3 ଆ྘б۷ཬ104
֥ଆ྘۷௔ֹَӁള೿ၩ߭ճbᆃᇕܿଆིႋऎႵܒࢲྟđ٤طᄝ۲োљഈनᄋؿളč๭ 2bĎ bഠ105
߶௹ྸொҵčSDBĎ܄ބ௜ুܴொҵčFOBĎෛଆ྘ܿଆᄹӉቋॹbхݝொҵčHABĎؿളਔᇉྟ106
ሇэđՖࢠཬଆ྘ᇏ֥੻࣍ࠇڵᇏྟđሇູࢠնଆ྘ᇏ֥ᆞᆴbఃჅোљࢠ֥ࠖ݅೐۷ࠇၳᇉđၹ107
Վܿଆᄹࡆᇶေ٢նਔაഠ߶ಪॖa܄௜ুބܴഄݝх૧ཌྷ֥ܱົ؇bᇯ໙ีٳ҃ࣉ၂҄ᆦӻਔᆃ108
၂ଆൔč๭ 2cĎ bෛሢQwen3 ܿଆঔնđRTB ٳ҃ཟႷ၍׮đѩྙӮ۷ᇗ֥ᆞཟແ҆bनᆴഈശ109
4
Figure 1: Benchmark construction and taxonomy. a, Overview of the benchmark pipeline. Value-laden survey
items are collected from source corpora, assigned to a cascaded taxonomy of social domains and benevolence-bias
categories, used to elicit simulated human responses from LLMs, and compared against empirical human response
distributions to quantify the bias.b, Distribution of the 406 retained benchmark items across the six benevolence-
bias categories: prosociality (PSB), social desirability (SDB), harm aversion (HAB), benevolent interpretation (BIB),
emotional softening (ESB) and fairness optimism (FOB).c, Category definitions with representative survey items,
illustrating the behavioural tendency captured by each bias dimension.d, Composition of the benchmark across the
four social domains of culture, politics, law and economy, showing the number and proportion of items assigned to
each domain.e, Alluvial flow from source dataset to domain and bias category, summarizing how ANES, GSS, WVS
and PT items populate the final benchmark taxonomy.
reference. Reasoning softens the bias without removing it.
More capable models show a slightly smaller bias.Relating each model’s MMLU-Pro score
to its overall BTB with a quadratic fit, the curve slopes gently downward: more capable models show
smaller shifts on average, and the strongest systems come closest to the human baseline (Fig. 2g).
But the link is loose (R2 “0.16): models with similar scores can sit far apart on the BTB axis.
Capability explains only a small part of the differences between models.
Instruction tuning makes Qwen2.5 more benevolent.To pin down where in the pipeline the
4

Table 1: Overall benevolence-bias results under the w/ inst. setting.Each bias dimension is reported with
Benevolence Tendency Bias (BTB) and Benevolence Win Rate (BWR). Positive BTB and BWRą0.5indicate a
displacement towards the benevolent pole relative to the human reference.
Model PSB SDB HAB BIB ESB FOB
BTB BWR BTB BWR BTB BWR BTB BWR BTB BWR BTB BWR
Closed-source models
GPT-5.10.026 0.531 0.087 0.600 0.077 0.582´0.002 0.500´0.029 0.447´0.014 0.473
GPT-5-mini0.057 0.558 0.072 0.578 0.059 0.556 0.004 0.510 0.025 0.510 0.019 0.516
GPT-5.4-mini´0.015 0.474 0.064 0.576 0.067 0.574 0.001 0.502 0.020 0.516 0.022 0.521
GPT-5.4-nano´0.069 0.382 0.062 0.571 0.026 0.515´0.009 0.484 0.025 0.523 0.006 0.496
GPT-4o-mini0.001 0.470 0.110 0.626 0.140 0.675´0.015 0.475 0.080 0.593 0.014 0.509
GPT-4.1-mini0.091 0.591 0.079 0.585 0.069 0.568 0.027 0.543 0.016 0.513 0.031 0.533
Grok-4.1-Fast0.002 0.504 0.037 0.543´0.009 0.490 0.016 0.529´0.007 0.483 0.029 0.529
Gemini3-Flash0.001 0.489 0.043 0.551 0.053 0.555´0.006 0.487´0.007 0.484´0.019 0.468
Gemini2.5-Flash0.030 0.538 0.049 0.563 0.068 0.575´0.002 0.495´0.034 0.455´0.026 0.466
Open-source models
Llama-3.3-70B0.021 0.516 0.088 0.601 0.093 0.601 0.035 0.548´0.013 0.473 0.055 0.566
Qwen3.7-Max0.028 0.527 0.082 0.598 0.083 0.596 0.017 0.523´0.008 0.485 0.007 0.503
DeepSeek-v4-Flash´0.010 0.480 0.029 0.530 0.078 0.585´0.020 0.481 0.031 0.534 0.020 0.518
DeepSeek-V4-Pro0.003 0.497 0.028 0.526 0.062 0.575´0.028 0.466´0.009 0.475´0.002 0.488
GLM-50.021 0.507 0.052 0.552 0.060 0.555´0.006 0.490 0.006 0.496 0.009 0.501
Kimi K2.60.012 0.499 0.047 0.542 0.057 0.561 0.005 0.504´0.009 0.482 0.010 0.504
Mimo-v2.5-Pro´0.003 0.490 0.076 0.590 0.083 0.584 0.003 0.499´0.005 0.485 0.007 0.505
Mimo-v2.50.005 0.495 0.051 0.558 0.087 0.588´0.005 0.490´0.011 0.469´0.013 0.474
Minimax-M2.70.006 0.496 0.072 0.580 0.067 0.561 0.015 0.524´0.002 0.478 0.002 0.497
Qwen3-32B0.020 0.518 0.074 0.588 0.053 0.560 0.027 0.541 0.041 0.555 0.057 0.570
Qwen3-235B-A22B0.045 0.568 0.057 0.570 0.084 0.592 0.018 0.523´0.004 0.500 0.027 0.521
Qwen2.5-72B-Inst0.025 0.519 0.056 0.555 0.051 0.550 0.018 0.527 0.001 0.505 0.020 0.517
Mistral-Small-24B´0.002 0.495 0.063 0.564 0.070 0.577 0.006 0.505 0.003 0.518 0.022 0.521
Gemma-3-27B´0.050 0.440 0.052 0.555 0.085 0.586 0.010 0.504´0.027 0.455´0.014 0.477
Human0.000 0.500 0.000 0.500 0.000 0.500 0.000 0.500 0.000 0.500 0.000 0.500
bias enters, we compared Qwen2.5 base models against their instruction-tuned versions at the same
size, keeping the family and pre-training fixed (Fig. 2h). Instruction tuning raised the mean BTB at
the 1.5B, 7B, 14B and 32B sizes, with the biggest jump at 32B; the 3B model is the only exception,
with a small negative change. The bias thus enters mainly at post-training, and the effect grows
with model size.
Model rankings agree best across the general survey datasets.To check that the rankings
reflect a stable model property rather than any one dataset, we computed bootstrap Spearman
correlations between model BTB rankings across the four datasets (Fig. 2i). The three general
survey datasets rank the models consistently:ρ«0.63for ANES–GSS,ρ«0.62for GSS–WVS,
andρ«0.54for ANES–WVS. Agreement is weaker for PT, which has fewer questions and a
narrower range of topics, and correlates only weakly with the other three.
Input level
Prompt language changes the size of the bias, not its direction.To check whether the shift
depends on the language of the prompt, we translated the four benchmarks into Chinese and re-ran
DeepSeek-V4-Flash, Qwen3-32B and GPT-4.1-mini with matched scoring, decoding and question
mix (Fig. 3a–c). For DeepSeek-V4-Flash, every dimension stays on the same side of the human
baseline in both languages, and the English and Chinese 95% confidence intervals overlap for five
5

 	  	  
&%'%& 
	
		
	

		
		
		* &##
+	

&%$
% #'
)&("!"(
(	  	  
$"








	
#!!







 &%"%&$'&
%
"%&$'&
 












	










	





	








		



	










(!)%&',!)' !$&#*
-
-

-


-










''+*+)(%!&(!)%&)"'
a b c
d e f
g h i
	
  



$!!%"'%&
(	

(		
	
		
	

	

	
#
'$$!!
#
# #%'
	

		
		
		
		
		
	
	
	
	
	
# #%'

	
'"#%!%#














	




	















		

 *)#$'(*&"'"#%!%#
+
+





#&
'''

'




!#"&$% 

	







 
#&$% # $$ $














)' %&)($	

!"$#"$ $'!"$#"$ "#&$#&! &,"#&$#&!
.	
.	
	
	
	
	
( *)- +,#'&
 *- +,#'&%+"






	

	

)
)	 	 
#' !#"!#
)
)



 !#"!#







		







		


%(&'!$#








๭ 2: ೿ၩொҵ֥ଆ྘Ҫଆൔbađ ଆ྘ܿଆؓQwen ଆ྘ކѩ௜न RTB ބ௜न഻ੱ֥႕ཙbbđ ੂ۱ொҵົ؇ᄝ҂๝ଆ
྘ܿଆ༯֥োљࠩ RTBbcđ҂๝ଆ྘ܿଆ༯ᇯ໙ี RTB ٳ҃bdđGLM-5 ᄝᆰ߭ࢤճაଆ྘๷৘่ࡱ༯ᇯ໙ี RTB
֥бࢠđ οொҵোљሢ೤beđQwen3-14B ᄝᆰ߭ࢤճაଆ྘๷৘่ࡱ༯֥োљࠩ RTB ߂ཞbfđDeepSeek-V4-Flash ᄝ
ᆰ߭ࢤճაଆ྘๷৘่ࡱ༯֥ᇯ໙ี RTB ٳ҃bgđMMLU-Pro აሹุ BTB ܱ֥༢đѩ۳ԛؽՑ୅ކ౷ཌbhđ҂๝
ܿଆ Qwen2.5 ଆ྘Ֆࠎቖ֞ᆷ਷ັކ֥ުטѩ௜न RTB э߄biđଆ྘ஆ଀ᄝ҂๝ඔऌࠢᆭ֥ࡗ bootstrap Spearman
ཌྷܱb
֌ѩໃཨԢ෱b121
۷֥ۚ၂Ϯି৯ა۷ཬ֥೿ၩொҵཌྷܱb ໡ૌࣉ၂҄࡟ဒ೿ၩொҵ൞ڎᆺ൞၂Ϯଆ྘ି৯֥122
ڬӁ໾bؓૄ۱ଆ྘đ໡ૌࡼ MMLU-Pro ٳඔაሹุ BTB ৳༢ఏটĠሹุ BTB ᄝ෮Ⴕ໙जี123
ཛഈऊ֤֞ކđѩ୅ؽކՑ౷ཌč๭ 2gĎ b୅ކ౷ཌᄝܴҩ֥֞ି৯ٓຶଽཟ༯ౠོđۚMMLU-124
Pro ଆ྘௜नіགྷԛ۷ཬ֥೿ၩொ၍đି৯ቋ఼֥༢๤ቋ࣍ࢤದোࠎཌbಖطđᆃ၂ܱ༢ࢠູ඾೛125
čR2 = 0 .16Ď bMMLU-Pro ٳඔཌྷ֥࣍ଆ྘ᄝ BTB ᇠഈ໊ᇂҵၳޓնđ೏ۄᇏ֩ି৯༢๤֥ᆞཟ126
ொ၍മᇀնႿऎႵॖб۷֥ٳ఼֤༢๤bၹՎđି৯ᆺିࢳ൤ॴଆ྘೿ၩொҵэၳ֥၂ཬ҆ٳđଆ127
6
Figure 2: Model-level patterns of benevolence bias. a, Effect of model scale on the pooled mean BTB
and mean win rate of Qwen models.b, Category-level BTB for the six bias dimensions across model scales.c,
Per-question BTB distributions across model scales.d, Per-question BTB of GLM-5 under direct answering versus
model reasoning, coloured by bias category.e, Category-level BTB profile of Qwen3-14B under direct answering
versus model reasoning.f, Per-question BTB distributions of DeepSeek-V4-Flash under direct answering versus
model reasoning.g, Relationship between MMLU-Pro and overall BTB, with a quadratic fit.h, Change in pooled
mean BTB from base to instruction-tuned checkpoints for Qwen2.5 models at different scales.i, Bootstrap Spearman
correlations of model rankings across datasets.
of six categories (Fig. 3a). For Qwen3-32B, harm aversion is higher under Chinese prompts and
fairness optimism lower, though both stay positive (Fig. 3b). For GPT-4.1-mini, the two languages
almost fully overlap (Fig. 3c). Switching language never flips the sign of the bias on any dimension;
which dimensions show a language gap, and in which direction, differs by model. Prompt language
is thus a dial, not a switch: each model’s language-specific representations filter, but do not remove,
the alignment-driven prior.
Prompt framing changes the size of the bias without removing it.We next compared
three framings with matched scoring, decoding and question mix: direct answering, where the model
answers as itself; role-play, where it adopts a sampled persona; and prediction, where it predicts
6

which option that person would pick (Fig. 3d–f). Across DeepSeek-V4-Flash (Fig. 3d), Qwen3-32B
(Fig. 3e) and GPT-4.1-mini (Fig. 3f), the ordering direct answeringąrole-playąprediction holds
at the dataset level, category by category, and in the per-question distributions. Two facts follow.
First, all three framings stay on the positive side of the human baseline, so the bias is a genuine
prior carried across framings, not something specific to persona adoption. Second, third-person
prediction lowers the bias more than first-person role-play: asking a model to predict someone else’s
choice, rather than to be that person, brings out a more detached, less norm-driven stance. Framing
is thus a size dial, not a fix.
Aligned models cannot fully play malicious personas.To test whether the bias is a deep prior
or just a default voice, we rewrote each sampled persona to encode antisocial, self-interested and
harm-tolerant attitudes, and re-ran the role-play protocol for the same three models with matched
questions, scoring and decoding (Fig. 3g–i). The three models converge on the same one-sided limit.
The malicious rewrite lowers the win rate on fairness optimism, emotional softening and benevolent
interpretation, the dimensions less directly targeted by safety training (Fig. 3g,i). But on social
desirability, prosociality and harm aversion, the dimensions most shaped by RLHF, it cannot push
answers below the human baseline, and sometimes even raises them slightly. For Qwen3-32B, the
malicious persona lowers the win rate on all four datasets, yet every dataset stays above 0.5 (Fig. 3h).
A persona that should produce a below-average respondent can pull the model toward the human
reference, but never past it. On the SDB, PSB and HAB axes, aligned models have measurably lost
the ability to imitate people at the less-benevolent end, so any synthetic sample built from them
will under-represent that part of the human range, exactly the kind of blind spot a researcher needs
to know about and, as we show below, can correct for.
Output level
Contrastive calibration removes the bias, with no retraining.Since the bias survives
prompt-level interventions, can it be removed at the output level, without changing the model or
the prompt? We developed a contrastive calibration method that works entirely on the next-token
probability vector returned for each question, so it is model-agnostic and works with black-box
APIs. For each (persona, question) pair we make a second call under a neutral persona, keeping the
question and decoding settings fixed; this estimates the model’s default answer prior, the option it
favours once the persona signal is removed. We then divide the persona-conditioned distribution by
this prior raised to the powerα, and renormalize:
P˚paq9 Ppa|persona,questionq Ppa|neutral,questionq α .(1)
In plain terms, the method removes the share of the model’s preference that it would have shown
with no persona at all. The strengthαsets the size of the correction:α“0leaves the answers
unchanged,α“1removes the prior entirely. The neutral persona is a persona-free prompt (“You
are a survey respondent.”) with the same format as the persona-conditioned calls (Methods). For
Qwen3-32B, sweepingαfrom 0 to 1 gives a dose-dependent drop on all six dimensions: byα«0.5all
six categories collapse into a tight band around zero, and atα“1several dip below the baseline,
showing the correction can overshoot when pushed too hard (Fig. 4a). For DeepSeek-V4-Flash,
the per-question∆BTB shifts left at everyα, with no question moving the wrong way, and the
biggest drops fall on the questions with the largest starting BTB (Fig. 4b). For GPT-4.1-mini
atα“0.5, every source dataset moves from clearly positive to near zero without overshooting
(Fig. 4c). Contrastive calibration thus reduces the bias across dimensions, questions and datasets,
7

  






%!%(*
*)*+#%!%(*,($!%
'"	#)
)#!%

!(*
&#'#,
(!*!&%

1	
1	
	
	
	
	






#") 

/-#") +#,&"-".#$*,0
##+##'!("-%
)$(&-%
%&)#-#












)
)
)







'%

#$

%&"$(

 !
!%
!%


(
(




%#

!"#

$ "'
&
#

#
a b c
d e f
g h i













( %'+)"+'#!$
*$

	
!'( %"&"+ '!(!%$

+

+


+









#)$!$')
	




'(%$*'(#!$')#)
&("#(
   





# &$&( *#
 








#()'& #,#() %#&)$*$,$*.!(')) * )#*)
-#&		
+%%#()'&
'&*( "$!*'(.#()'&


 

 

 



 

+
+
+




(&' $#)!

(&' $#)!

 &'% (' $#

" #
(!!%&$#
$#'% '$%*%&$#
-	 -	 		 	 	 	
%'&*() $#
 ') $!%!+ ' ) $#
'" #
,		
,		
,	


'*() $# ()' *) $#+'" #

" #
	(! #
๭ 3: ೿ၩொҵ֥ൻೆҪࢫטၹ෍bađDeepSeek-V4-Flash ᄝ҂๝ொҵোљഈ֥ႇ໓–ᇏ໓௜न RTB бࢠđ ջ95% ᇂྐ
౵ࡗbbđQwen3-32B ᄝႇ໓ބᇏ໓ิൕ༯đ োљࠩᇯ໙ีRTB ٳ҃bcđGPT-4.1-mini ᄝႇ໓ބᇏ໓ิൕ༯đ োљࠩᇯ
໙ี RTB ٳ҃bdđDeepSeek-V4-Flash ᄝᆰ߭ࢤճa ࢘೤ϲဆބყҩ೘ᇕॿࡏ༯֥ඔऌࠩࠢ௜न഻ੱbeđQwen3-32B
ᄝᆰ߭ࢤճa࢘೤ϲဆބყҩ೘ᇕॿࡏ༯֥োљࠩ RTB ߂ཞbfđGPT-4.1-mini ᄝ҂๝ิൕॿࡏ༯֥ᇯ໙ี RTB ٳ
҃bgđDeepSeek-V4-Flash Ֆჰ൓ದذ֞۬ၩದ۬ൈđ োљࠩ௜न഻ੱэ߄bhđQwen3-32B ᄝჰ൓ದذބ۬ၩದ่۬
ࡱ༯֥ඔऌࠩࠢ௜न഻ੱđದোࠎཌູ 0.5biđGPT-4.1-mini ᄝჰ൓ದذބ۬ၩದ่۬ࡱ༯֥໙ีࠩ RTB ٳ҃b
ANESaGSS ބ WVS ഈđᆰ߭ࢤճ่ࡱ༯֥ඔऌࠩࠢ௜न഻ੱཁᇷۚႿ࢘೤ϲဆބყҩĠᄝᆃ೘163
۱ඔऌࠢᇏđყҩႻб࢘೤ϲဆ੻ັࣉ၂֮҄ࢆ഻ੱč๭ 3dĎ bؓႿQwen3-32Bđᆰ߭ࢤճ༯֥164
োљࠩ RTB ߂ཞᄝੂ۱ொҵົ؇ഈनӑ࢘ݖ೤ϲဆބყҩđ ౏࢘೤ϲဆႻᄝૄ۱ົ؇ഈӑݖყҩđ165
ၹՎᆰ߭ࢤճ ą ࢘೤ϲဆ ą ყҩ֥ஆ྽҂ࣇթᄝႿऊކҪ૫đ္թᄝႿᇯোљҪ૫č๭ 3eĎ bؓ166
Ⴟ GPT-4.1-miniđᇯ໙ี RTB ٳ҃ཁൕԛཌྷ๝ஆ྽ğᆰ߭ࢤճٳ҃ૼཁ໊Ⴟ࢘೤ϲဆބყҩႷ167
ҧđყҩཌྷб࢘೤ϲဆࣉ၂҄ཟਬ၍׮Ġᆰ߭ࢤճ༯ॖ֥࡮ᇗᆞཟແ҆ᄝਆᇕ൪࢘ሇߐॿࡏ༯नФ168
ཤ೐č๭ 3fĎ bၹՎđ೘۱ଆ྘ᄝਆ۱ܒࢲྟ൙ൌഈղӮ၂ᇁbֻ၂đૄ۱ᆰ߭ࢤճa࢘೤ϲဆބ169
ყҩ่ࡱಯ׻໊Ⴟದোࠎཌ֥ᆞҧĠીႵ಩ޅॿܱࡏоொҵđඪૼ೿ၩொҵ൞ଆ྘ॴॿࡏེջ֥ൌ170
8
Figure 3: Input-level modulators of benevolence bias. a, English–Chinese comparison of mean BTB across
bias categories for DeepSeek-V4-Flash, with 95% confidence intervals.b, Category-level per-question BTB distri-
butions of Qwen3-32B under English and Chinese prompts.c, Category-level per-question BTB distributions of
GPT-4.1-mini under English and Chinese prompts.d, Dataset-level mean win rate of DeepSeek-V4-Flash under the
direct-answering, role-play and prediction framings.e, Category-level BTB profile of Qwen3-32B under the direct-
answering, role-play and prediction framings.f, Per-question BTB distributions of GPT-4.1-mini across prompt
framings.g, Change in category-level mean win rate of DeepSeek-V4-Flash from the original to the malicious per-
sona.h, Dataset-level mean win rate of Qwen3-32B under the original and malicious personas; the human baseline
is 0.5.i, Question-level BTB distributions of GPT-4.1-mini under the original and malicious personas.
with no retraining, no prompt change and no access to weights, making it a practical, model-agnostic
correction whose strengthαtrades off leftover bias against overshoot.
Aligned models can spot their own bias, but only partly fix it.Can a model recognize
its own benevolent shift when challenged? We tested this with a two-round protocol, entirely at
the prompt level. In round one, the model answers (a1) under the standard role-play framing; in
round two, we reissue the prompt with “Your answer wasa1. Does this truly reflect this person’s
background, or your own preference? Revise if needed.”, producinga2 (Fig. 4d–f). The revisions are
directed, not random. Qwen3-32B preferentially takes back the answers that lean most benevolent,
with the biggest drops on social desirability and harm aversion (Fig. 4d). DeepSeek-V4-Flash’s win
8

rate falls from R1 to R2 on every dimension but stays above 0.5 on all of them (Fig. 4e). GPT-4.1-
mini’s distributions shift toward 0.5 on every dataset without crossing it (Fig. 4f). Models thus hold
an internal sense of their own bias and act on it when prompted, but this self-awareness neither
switches on by itself nor finishes the job: reflection alone cannot restore the human distribution
that calibration reaches atα«0.5.
The bias does not change with sampling temperature.Finally, we asked whether the bias
lives only at the most likely answer or runs through the whole answer distribution, by varying
decoding temperature with everything else fixed (Fig. 4g–i). For Qwen3-32B, the category-level
mean BTB traces a nearly flat line across the temperature grid, with the category ordering preserved
throughout (Fig. 4g). For DeepSeek-V4-Flash, the per-question violins widen a little at higher
temperatures but keep the same centre and positive skew (Fig. 4h). For GPT-4.1-mini, the change
in mean BTB relative to temperature 0 stays within˘0.01in every cell (Fig. 4i). Across the tested
range, the direction, size and category profile of the bias are all stable. Benevolence bias therefore
sits at the centre of the answer distribution, not in its tails: it vanishes neither when the model picks
the mode nor when it explores. This rules out output randomness as a fix, and confirms contrastive
calibration as the one intervention tested here that recovers the human reference.
Discussion
Across 18 widely used large language models and four major social-science datasets, we find a
consistent shift of simulated human answers toward the benevolent end on value-laden questions:
83 of 108 BTB cells and 75 of 108 BWR cells are positive, concentrated on social desirability (mean
BWR“0.565) and harm aversion (mean BWR“0.569), while emotional softening is close to null
(mean BWR“0.494). Model rankings agree across the three general survey datasets (Spearman’sρ
between 0.54 and 0.63), so the benchmark captures a property of the models, not of any one dataset.
We call this shift benevolence bias. It is not a thin layer of style on top of an otherwise faithful
value representation, but a prior the model brings to every persona it adopts and every survey it
answers; naming and measuring it is what makes it something researchers can plan around.
Where the bias does and does not appear points to its source. Temperature moves the category-
level BTB by no more than˘0.01; switching language or framing changes the size of the shift but
never its direction; capability explains little of the cross-model variance (R2“0.16); and internal
thinking softens but does not remove the shift. By elimination, the bias is unlikely to be an artefact
of decoding randomness, prompt voice, framing or raw capability. The Qwen2.5 comparison points
to the source directly: instruction tuning raised the mean BTB at four of the five sizes tested,
with the biggest jump at 32B, and the bias grows with model size in both Qwen3 and Qwen2.5.
Benevolence bias thus traces to the post-training stage, and the alignment pipeline installs it more
strongly as models grow.
This places benevolence bias inside a larger question: how alignment shapes a model’s value
representation. A common view is that alignment refines a pre-trained model into more helpful,
more acceptable behaviour. Our results suggest that, on value-laden questions, alignment does more
than refine: it shifts. The malicious-persona limit makes this concrete. The dimensions less directly
targeted by safety training (fairness optimism, emotional softening, benevolent interpretation) can
fall below their normal values, so the models retain some ability to produce less benevolent answers
there. The dimensions most shaped by RLHF (social desirability, prosociality, harm aversion)
never crossed the human baseline, even under explicit instruction. We read this as a narrowing of
representational coverage: the model is not merely nudged toward benevolent answers, but has lost
some ability to imitate a region of the real range of human attitudes.
9

  
 

#&" $#&')*'




$ 





)%','!)%' (
+$






 	  
" "#%&#
)
)



&$%! '
$%#&%! ("#%&#
"
$
 	 
 


  
#&')*'+(






  


  
  
 
 
  

  
) %',")
#!$!
-
-

-


-










")






		
		
	
		
		
+ "')- , %
,*
  (  $

%*#

'% (%- !+ )()'&(+
 +!'##
)(!)





	*!()"&%#!+!#"%')!
*!()"&%!+!#"%')! ,)(!)
	$"%"


!%
(!#"%!









 # (!&!$#'
+	

+


+

+	
+

+


+


*!#%' 
+	
%
 (!&!$#' (& "'!#%'
) #




( %""
+

 + +	 +   
"("( *($#" &(
"%
"%"%
&)'( $#" &( $# ( '(& )( $#
%!	"'
"+%#*	

#*)$.#/),+ /.&+'/(#*-(#
 
 

 


  	 

 		


 

  

 
  
  


	 	 	 

 


 

 

 
 

  	  
#/&',.2&0&*!
1&+

3	
3


	
&#+!
/		



#)




**'#"
	




.-#.%&$.)"#,'& ,.&*)

(&)&
)!'& ,.#"
'+%
a b c
d e f
g h i
๭ 4: ཮ሙa ሱ໡ྩᆞބҐဢ໑ؓ؇೿ၩொҵ֥႕ཙbađQwen3-32B ᄝ҂๝ؓб཮ሙ఼؇ čαĎ ༯֥োљࠩRTBđ ᅚൕ
ੂ۱ົ؇ഈ࠴֥ਈ၇ঠൔொҵ֮ࢆbbđDeepSeek-V4-Flash ᄝؓб཮ሙ༯đཌྷؓႿໃ཮ሙࠎཌ֥ᇯ໙ี RTB э߄bcđ
GPT-4.1-mini ᄝ 0.5 ཮ሙ఼؇༯đ ۲ჷඔऌ֥ࠢ௜नRTBđ ཁൕ཮ሙႵིྟ֥ඔऌ९ҪҵၳbdđQwen3-32B ᄝሱ໡ྩ
ᆞ༯֥ྩᆞੱა഻ੱэ߄đ οொҵোљࢳٳbeđDeepSeek-V4-Flash ᄝࠎཌ čR1Ď ުބิൕ čR2Ď ่ࡱ༯֥োљ഻ࠩੱb
fđGPT-4.1-mini ᄝ R1 ބ R2 ่ࡱ༯đοჷඔऌ֥ٳ߃ࠢ໙ี഻ࠩੱđѩ۳ԛ۲่ࡱनᆴbgđQwen3-12B ᄝ҂๝Ґ
ဢ໑؇༯đ۲ொҵোљ֥௜न RTBbhđDeepSeek-V4-Flash ᄝ҂๝Ґဢ໑؇༯֥ᇯ໙ี RTB ٳ҃biđGPT-4.1-mini
֥োљࠩ RTB ෛҐဢ໑؇эط߄Ӂള֥э߄b
Ԣದ१๤࠹ଽಸᆭຓđิൕ۬ൔაದ่۬ט߄ࡱႨЌӻ၂ᇁčمٚĎ bؓႿQwen3-32Bđࡼ α Ֆ 0205
ೡ૭֞ 1đ ߶ᄝ෮Ⴕੂ۱ொҵົ؇ഈӁളোљࠩRTB ࠴֥ਈ၇ঠൔ֮ࢆ č๭4aĎ b ֒α = 0 ൈđ ૄ206
۱োљ׻ૼཁۚႿದোࠎཌđఃᇏഠ߶௹ྸބхݝ౼ᆴቋնb֞ α « 0.5 ൈđੂ۱োљၘ෯෪֞ਬ207
֥࣍ڸᅎջĠطᄝ α = 1 ൈđ೏ۄົ؇ॴࠎ֞ཌၛ༯đඪૼ཮ሙѩ҂หקႿ၂ᇕொҵো྘đ౏ᄝླ208
ေൈॖၛൌགྷ؇ݖ཮ᆞbؓႿ DeepSeek-V4-Flashđᄝҩ൫֥ૄ۱ α ༯đཌྷؓႿໃ཮ሙࠎཌ֥ᇯ໙209
ี ∆RTB ٳ҃नཟቐ၍׮đ ౏ીႵีཛӔ٤ყ௹ٚཟ၍׮ č๭4bĎ b ھ၍׮ෛα ֆטᄹ఼đ ቋ఼༯210
ࢆԛགྷᄝࠎཌ RTB ቋն֥ีཛഈđط҂൞෮Ⴕ໙ี֥नᄋ௜၍bؓႿ GPT-4.1-miniđᄝ α = 0.5211
10
Figure 4: Effects of calibration, self-correction and sampling temperature on benevolence bias. a,
Category-level BTB of Qwen3-32B across contrastive-calibration strengths (α), showing a dose-dependent reduction
of the bias on all six dimensions.b, Per-question change in BTB of DeepSeek-V4-Flash under contrastive calibration,
relative to the uncalibrated baseline.c, Mean BTB of GPT-4.1-mini per source dataset at calibration strength 0.5,
showing dataset-level differences in calibration effectiveness.d, Revision rate and change in win rate of Qwen3-32B
under self-correction, decomposed by bias category.e, Category-level win rate of DeepSeek-V4-Flash under the
baseline (R1) and post-prompt (R2) conditions.f, Question-level win rate of GPT-4.1-mini under R1 and R2, split
by source dataset, with condition means indicated.g, Mean BTB of Qwen3-32B per bias category across sampling
temperatures.h, Per-question BTB distributions of DeepSeek-V4-Flash across sampling temperatures.i, Change in
category-level BTB of GPT-4.1-mini as a function of sampling temperature.
This narrowing matters for the fast-growing use of LLMs as silicon samples. Synthetic samples
built from current aligned models will over-represent the benevolent end of social-desirability, proso-
ciality and harm-aversion questions, under-represent the other end, and compress the tail variance
real surveys show. Because the bias survives the fixes a researcher would try first (persona con-
ditioning, faithful role-play instructions, lower temperature, invitations to reconsider), off-the-shelf
use will produce distributions biased not only in the average but in the range; and synthetic data
generated for downstream training inherits the same compression, risking a feedback loop in which
later models learn from an already shifted value representation. Knowing exactly where this bites
10

is what lets researchers use these tools with their eyes open.
The encouraging part is that the shift can be substantially undone, with no retraining and no
access to model weights. At a moderate strength ofα«0.5, contrastive calibration brings all six
dimensions into a tight band around the human baseline, while higher strengths overshoot; the only
requirement is a small set of next-token logits, which most current APIs expose. Self-correction, by
contrast, is directed but partial: models take back their most benevolent answers when asked to
reconsider, yet never return fully to the human reference. The fix that works is distributional, not
behavioural, and it is simple enough to drop into existing pipelines today.
These conclusions come with limits worth stating plainly. First, our benchmark draws on
datasets that are mostly Western or globally administered (ANES and GSS are US samples; WVS
has uneven regional weighting; the prospect-theory replication concerns decision-making), so gen-
eralization to value systems outside this frame is not settled. Second, we tested English and Chi-
nese prompts only; how the bias looks in lower-resource languages is open. Third, our questions
are multiple-choice with ordered options; whether the same prior shapes free-form answers, where
benevolence may surface through wording or topic avoidance, needs a separate design. Fourth,
closed-weight alignment recipes are not public, so we can trace the bias to post-training but not to
any specific RLHF, DPO or SFT component. Finally, our calibration assumes access to per-token
probabilities, which not all APIs expose.
Looking ahead, the central tension is between two goals: alignment optimizes models for socially
desirable behaviour, whereas social-science use asks for faithful coverage of the full range of human
attitudes, including its uncomfortable parts. Current alignment recipes meet the first goal at a
measurable cost to the second, and what post-training compresses away cannot be recovered by
prompting. Butthisisasolvableproblem. Onthemodellingside, alignmentobjectivesthatpreserve
coverage of the human distribution, rather than only shifting its average, could make safety and
faithful simulation attainable together. On the measurement side, distributional corrections such
as the one proposed here already offer a ready-to-use safeguard and a sharp diagnostic for tracking
how alignment reshapes value representation across model generations. With a clear map of the bias
and a simple correction in hand, aligned LLMs can move from promising but unproven stand-ins
toward dependable instruments for social science.
Methods
Benchmark stimulus corpus construction
We built a psychometrically grounded benchmark by drawing stimuli from established social-
science surveys and standardizing them for LLM evaluation. The pipeline has two steps: acquiring
the raw data, and decoupling each item from its original context.
Empirical data acquisition and structuring.To keep the stimuli realistic, we drew them
from four foundational social-science datasets: the World Values Survey (WVS)1, the multilin-
gual survey instrument of a prospect-theory replication experiment (PT)2, the American National
Election Studies (ANES)3, and the General Social Survey (GSS)4. We write this collection as
Draw “ tDWVS,D PT,D ANES,D GSSu. Because the sources come in many document formats, we
use a two-stage extraction pipeline. First, a format-aware parserPturns each raw documentdinto
plain text:PpdqÑ ˜d. Second, an LLMMextract reads the parsed text and produces a structured,
1https://www.worldvaluessurvey.org/
2https://osf.io/vtx3c/
3https://electionstudies.org/
4https://gss.norc.org/
11

machine-readable set of questions. The combined question setQraw is thus
Qraw “
ď
dPDraw
MextractpPpdqq,(2)
whereM extractp¨qmaps parsed source text into a single programmatic schema, for example a struc-
tured JSON object with the item stem, the response options and metadata. Splitting parsing from
semantic extraction keeps the output consistent no matter what format the original source used.
Stimulus standardization and context decoupling.In real surveys, items often use complex
structures with shared preambles, such as matrix questions, and human answers are sensitive to
option order. To isolate the model’s own bias, we use an LLMM rewrite to decouple each item
qPQ raw from its context and rewrite it as a standalone question. This yields a set of self-contained,
independent itemsQ indep:
Qindep “ tMrewritepqq|qPQ rawu,(3)
whereM rewritep¨qturns long, compound survey phrasings into natural, direct, standalone questions.
It removes preambles, embedded answer cues and context dependencies, while keeping the original
psychometric intent intact. By turning each stimulus into a standalone question that reads like
normal conversation, this step ensures the evaluation measures the model’s own prior rather than
an artefact of a particular survey layout.
Box 1|Example: context decoupling via an LLM
Original survey item (q):
“For each of the following aspects, indicate how important it is in your life. Would you say it is very important,
rather important, not very important, or not important at all? — Friends”
Rewritten independent item (qindep):
“How important are friends in your life?”
Preserved response options:
1. Very important 2. Rather important 3. Not very important 4. Not at all important
Taxonomic annotation and cascaded quality validation
To keep the benchmark psychometrically sound and construct-valid, we define a bias taxonomy
B“ tb 0, b1, . . . , bku, wheretb 1, . . . , bkuare thektarget bias dimensions (the six dimensions of
Table 1) andb 0 is the null category, a neutral stimulus with no target bias signal. Labelling the
whole candidate pool by hand is not feasible at scale, both logistically and in terms of rater burden.
We therefore use a three-stage cascaded validation pipeline that steadily raises label quality: (1)
LLM-based pre-screening, (2) expert heuristic review, and (3) independent researcher consensus.
Stage 1: LLM-based pre-screening.To handle a large volume of candidate items efficiently, we
use an LLMMannotate as a high-throughput first annotator. For each itemq, the model assigns a
provisional bias label from the taxonomy:
bpqq LLM“M annotatepqq, b pqq LLMPB.(4)
Items assigned to the null category (bpqq LLM“b 0) are dropped right away, shrinking the pool to items
where at least one bias signal is present. This stage uses the broad semantic coverage of LLMs to
make a cheap, scalable first pass.
12

Stage 2: Expert heuristic review.Because LLMs can still drift semantically or misread context,
the surviving items get a quick heuristic review by senior domain experts. Each expert checks
whether the provisional labelbpqq LLM is right and whether the itemqis coherent. We write this as a
binary keep-or-drop indicator:
E
´
q, bpqq LLM
¯
“
#
1,if the expert agrees withb pqq LLM andqis coherent,
0,otherwise.
(5)
Only items withE“1move to the final stage, which focuses the human effort on the strongest
candidates.
Stage 3: Independent researcher consensus.To get high-confidence labels with strict inter-
rater reliability, the expert-validated subset goes toNdomain-trained doctoral researchers for in-
dependent binary verification. Each researcher judges whether itemqgenuinely and only embodies
the assigned bias dimensionbpqq LLM. They work fully blinded, with no access to the experts’ earlier
decisions or to their peers’ answers, to avoid authority bias and anchoring. The consensus indicator
is
C
´
q, bpqq LLM
¯
“mode
ˆ!
vi
´
q, bpqq LLM
¯)N
i“1
˙
,(6)
wherev i Pt0,1uis the binary score from researcheri. The ground-truth label ˆbq is confirmed as
bpqq LLM only whenC“1; items that fail to reach majority consensus are dropped for good.
Benchmark synthesis.The final benchmarkQfinal keeps only the items that pass both the expert
gate and researcher consensus:
χpqq“
#
1,ifE
´
q, bpqq LLM
¯
“1^C
´
q, bpqq LLM
¯
“1,
0,otherwise,
(7)
Qfinal“tqPQ indep|χpqq“1u.(8)
This double-consensus rule removes items where the algorithm and the human raters disagree, so
every retained stimulus captures its intended construct with minimal measurement noise.
Demographic simulation and behavioural distribution estimation
In-silico demographic simulation.To get a human reference grounded in real population diver-
sity, we use an in-silico demographic conditioning setup. For each datasetd, we sample a set of real
respondentsU“tu 1, . . . , uNuand build, for each respondentu j, a demographic profile vectorpj
encoding their key socio-economic attributes. This profile then conditions an LLMMsim to answer
a stimulusq1:
rj,q1“M simpq1, pjq,(9)
wherer j,q1 Pt1, . . . , Kuis the predicted option index for respondentuj. Conditioning onp j steers
the model toward the tendencies of the target group rather than its own default prior.
Aggregation into a population-level distribution.We combine the individual simulated an-
swers into a synthetic probability mass function (PMF) over theKoptions. The estimated mass
on optionkis
Fk“ 1 N Nÿ j“1 I ` rj,q1“k ˘ .(10)
This gives the population-level synthetic distributionF, which serves as the LLM behavioural refer-
ence. We compare it directly against the empirical human distributionGfrom the real respondent
sampleU, which lets us measure the gap between them quantitatively.
13

Quantitative metrics for benevolence bias
We use two complementary metrics that capture benevolence bias from different angles: BTB
captures the population-level shift, whereas BWR captures instance-level deviation.
Benevolence Tendency Bias (BTB).BTB measures the overall directional shift of the LLM
answer distribution relative to the human reference. For a stimulus whoseNoptions are ordered
by increasing benevolence (optioni“1least benevolent,i“Nmost benevolent), we assign a
position-aware weight
Wi“ i N ,(11)
which gives more weight to deviations at the highly benevolent end. LetFi andG i be the mass on
optionifrom the LLM and the human reference, respectively. BTB is
BTBpF, Gq“
Nÿ
i“1
Wi¨F i ´
Nÿ
i“1
Wi¨G i.(12)
A positive BTB means the model shifts mass toward more benevolent options relative to the human
baseline (a positive benevolence bias); a negative BTB means the opposite (a benevolence deficit).
Benevolence Win Rate (BWR).BTB captures the overall tendency but ignores instance-level
variation. BWR complements it by comparing the model’s choice against the human answer on
each single question. For an evaluation set ofMinstances, letypkq m andy pkq g be the ordered option
indices chosen by the LLM and the human on instancek. BWR is
BWR“ 1 M Mÿ k“1 ” 1¨I ´ ypkq m ąy pkq g ¯ `0.5¨I ´ ypkq m “y pkq g ¯ `0¨I ´ ypkq m ăy pkq g ¯ı .(13)
The model scores 1 when it picks a strictly more benevolent option than the human, 0.5 for a tie,
and 0 otherwise. A BWR above 0.5 means the model is systematically more benevolent than the
human on a per-question basis; BWR“0.5means parity; and BWR below 0.5 means the model is
consistently less benevolent than the human reference.
Data availability
All the used datasets in this study are available on GitHub atxxx.
Code availability
All the source codes to reproduce the results in this study are available on GitHub atxxx.
Acknowledgement
The work is supported by xxxxx.
Author contributions
X.X., X.X. and X.X. contributed to the ideation and design of the research; X.X. and X.X.
performed the research; all authors contributed to writing and editing the paper.
14

Corresponding authors
Xu Chen (xu.chen@ruc.edu.cn); Ji-Rong Wen (xxx)
Competing interests
The authors declare no competing interests.
References
[1] Gati Aher, Rosa I. Arriaga, and Adam Tauman Kalai. Using large language models to simulate
multiple humans and replicate human subject studies. InProceedings of the 40th International
Conference on Machine Learning (ICML), 2023.
[2] Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, and
David Wingate. Out of one, many: Using language models to simulate human samples.Political
Analysis, 31(3):337–351, 2023.
[3] John J. Horton. Large language models as simulated economic agents: What can we learn from
homo silicus?NBER Working Paper No. 31122; arXiv preprint arXiv:2301.07543, 2023.
[4] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang,
and Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior. In
Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology
(UIST), 2023.
[5] Paul Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, and Dario Amodei.
Deep reinforcement learning from human preferences. InAdvances in Neural Information
Processing Systems (NeurIPS), 2017.
[6] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin,
Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models
to follow instructions with human feedback. InAdvances in Neural Information Processing
Systems (NeurIPS), 2022.
[7] NisanStiennon, LongOuyang, JeffWu, DanielZiegler, RyanLowe, ChelseaVoss, AlecRadford,
Dario Amodei, and Paul Christiano. Learning to summarize with human feedback. InAdvances
in Neural Information Processing Systems (NeurIPS), 2020.
[8] Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan
Du, Andrew M. Dai, and Quoc V. Le. Finetuned language models are zero-shot learners. In
International Conference on Learning Representations (ICLR), 2022.
[9] Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn
Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, et al. Training a helpful and harmless
assistant with reinforcement learning from human feedback.arXiv preprint arXiv:2204.05862,
2022.
[10] Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy
Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, et al. Constitutional
AI: Harmlessness from AI feedback.arXiv preprint arXiv:2212.08073, 2022.
15

[11] Stephen Casper, Xander Davies, Claudia Shi, Thomas Krendl Gilbert, Jérémy Scheurer, Javier
Rando, Rachel Freedman, Tomasz Korbak, David Lindner, Pedro Freire, et al. Open problems
and fundamental limitations of reinforcement learning from human feedback.Transactions on
Machine Learning Research; arXiv preprint arXiv:2307.15217, 2023.
[12] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D. Manning, Stefano Ermon, and
Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model.
Advances in Neural Information Processing Systems, 36:53728–53741, 2023.
[13] Ethan Perez, Sam Ringer, Kamile Lukosiute, Karina Nguyen, Edwin Chen, Scott Heiner, Craig
Pettit, CatherineOlsson, SandipanKundu, SauravKadavath, etal. Discoveringlanguagemodel
behaviors with model-written evaluations. InFindings of the Association for Computational
Linguistics (ACL), 2023.
[14] Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R.
Bowman, Newton Cheng, Esin Durmus, Zac Hatfield-Dodds, Scott R. Johnston, et al. To-
wards understanding sycophancy in language models. InInternational Conference on Learning
Representations (ICLR), 2024.
[15] Hannah Rose Kirk, Bertie Vidgen, Paul Röttger, and Scott A. Hale. The benefits, risks and
bounds of personalizing the alignment of large language models to individuals.Nature Machine
Intelligence, 6:383–392, 2024.
[16] Yotam Wolf, Noam Wies, Oshri Avnery, Yoav Levine, and Amnon Shashua. Fundamental limi-
tations of alignment in large language models.Proceedings of the 41st International Conference
on Machine Learning (ICML); arXiv preprint arXiv:2304.11082, 2024.
[17] Esin Durmus, Karina Nguyen, Thomas I. Liao, Nicholas Schiefer, Amanda Askell, Anton
Bakhtin, Carol Chen, Zac Hatfield-Dodds, Danny Hernandez, Nicholas Joseph, et al. Towards
measuring the representation of subjective global opinions in language models. InConference
on Language Modeling (COLM), 2024.
[18] Jochen Hartmann, Jasper Schwenzow, and Maximilian Witte. The political ideology of conver-
sational AI: Converging evidence on ChatGPT’s pro-environmental, left-libertarian orientation.
arXiv preprint arXiv:2301.01768, 2023.
[19] David Rozado. The political preferences of LLMs.PLOS ONE, 19(7):e0306621, 2024.
[20] Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori
Hashimoto. Whose opinions do language models reflect? InProceedings of the 40th Inter-
national Conference on Machine Learning (ICML), 2023.
[21] Mohammad Atari, Mona J. Xue, Peter S. Park, Damian E. Blasi, and Joseph Henrich. Which
humans?PsyArXiv preprint, 2023.
[22] Yong Cao, Li Zhou, Seolhwa Lee, Laura Cabello, Min Chen, and Daniel Hershcovich. Assessing
cross-cultural alignment between ChatGPT and human societies: An empirical study. InPro-
ceedings of the First Workshop on Cross-Cultural Considerations in NLP (C3NLP) at EACL,
2023.
[23] Paul Röttger, Valentin Hofmann, Valentina Pyatkin, Musashi Hinck, Hannah Rose Kirk, Hin-
rich Schütze, and Dirk Hovy. Political compass or spinning arrow? Towards more meaningful
16

evaluations for values and opinions in large language models. InProceedings of the 62nd Annual
Meeting of the Association for Computational Linguistics (ACL), 2024.
[24] James Bisbee, Joshua D. Clinton, Cassy Dorff, Brenton Kenkel, and Jennifer M. Larson. Syn-
thetic replacements for human survey data? The perils of large language models.Political
Analysis, 32(4):401–416, 2024.
[25] Shashank Gupta, Vaishnavi Shrivastava, Ameet Deshpande, Ashwin Kalyan, Peter Clark,
Ashish Sabharwal, and Tushar Khot. Bias runs deep: Implicit reasoning biases in persona-
assigned LLMs. InInternational Conference on Learning Representations (ICLR), 2024.
[26] Seungjong Sun, Eungu Lee, Dongyan Nam, Chanyoung Lee, and Sungbin Park. Random silicon
sampling: Simulating human sub-population opinion using a large language model based on
group-level demographic information.arXiv preprint arXiv:2402.18144, 2024.
[27] Ronald Inglehart, Christian Haerpfer, Alejandro Moreno, Christian Welzel, Kseniya Kizilova,
Jaime Diez-Medrano, Marta Lagos, Pippa Norris, Eduard Ponarin, and Bi Puranen.World
Values Survey: Round Six – Country-Pooled Datafile. JD Systems Institute, Madrid, 2014.
[28] TomW.Smith, MichaelDavern, JeremyFreese, andStephenL.Morgan. Generalsocialsurveys,
1972–2018: Cumulative codebook. Technical report, NORC at the University of Chicago, 2018.
[29] American National Election Studies. ANES 2020 time series study: Full release. Technical
report, University of Michigan and Stanford University, 2021.
[30] Kai Ruggeri, Sonia Alí-Chieh, Jana B. Berkessel, et al. Replicating patterns of prospect theory
for decision under risk.Nature Human Behaviour, 4:622–633, 2020.
[31] Allen L. Edwards.The Social Desirability Variable in Personality Assessment and Research.
Dryden Press, New York, 1957.
17
