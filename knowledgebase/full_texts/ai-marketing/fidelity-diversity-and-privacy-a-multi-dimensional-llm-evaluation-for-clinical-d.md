---
title: 'Fidelity, Diversity, and Privacy: A Multi-Dimensional LLM Evaluation for Clinical Data Augmentation'
url: https://arxiv.org/abs/2604.27014
category: ai-marketing
subcategory: measurement
date: 2026-04
venue: ''
authors:
- Guillermo Iglesias
- Gema Bello-Orgaz
- María Navas-Loro
- Cristian Ramirez-Atencia
- Mercè Salvador Robert
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.27014
pages: 9
chars: 33720
fetched_at: '2026-11-08T13:28:06+00:00'
kb_version: 1
---

# Fidelity, Diversity, and Privacy: A Multi-Dimensional LLM Evaluation for Clinical Data Augmentation

Fidelity, Diversity, and Privacy: A Multi-Dimensional LLM Evaluation
for Clinical Data Augmentation
Guillermo Iglesias∗1, Gema Bello-Orgaz†1, María Navas-Loro‡1, Cristian Ramirez-Atencia§1, Mercè
Salvador Robert¶2, and Enrique Baca-Garcia‖3, 2, 4, 5, 6, 7, 8,
1Departamento de Sistemas Informáticos, Escuela Técnica Superior de Ingeniería de Sistemas
Informáticos, Universidad Politécnica de Madrid, Spain
2Department of Psychiatry, University Hospital Rey Juan Carlos, Mostoles, Spain
3Department of Psychiatry, University Hospital Jimenez Diaz Foundation, Madrid, Spain
4Department of Psychiatry, General Hospital of Villalba, Madrid, Spain
5Department of Psychiatry, University Hospital Infanta Elena, Valdemoro, Spain
6Department of Psychology, Universidad Catolica del Maule, Talca, Chile
7Department of Psychiatry, Madrid Autonomous University, Madrid, Spain
8CIBERSAM, ISCIII
Abstract
Thescarcityofhigh-qualityannotatedmedicaldata,particularlyinmentalhealth,posesasignificantbottleneckfortrainingro-
bustmachinelearningmodels. Privacyregulationsrestrictdatasharing,makingsyntheticdatagenerationapromisingalternative.
TheuseofLargeLanguageModels(LLMs)inadataaugmentationpipelinecouldbeleveragedasanalternativeinthisfield. Inthe
proposed methodology,DeepSeek-R1,OpenBioLLM-Llama3andQwen 3.5are used to generate synthetic mental health evalu-
ationreportsconditionedonspecificInternationalClassificationofDiseases,TenthRevision(ICD-10)codes. Becausenaivetext
generation can lead to mode collapse or privacy breaches (memorization), a comprehensive evaluation framework is introduced.
The generated diagnostic texts are assessed across three dimensions: semantic fidelity, lexical diversity, and privacy/plagiarism.
The results demonstrate that all models can generate clinically coherent, diverse, and privacy-safe synthetic reports, significantly
expanding the available training data for clinical natural language processing tasks without compromising patient confidentiality.
Keywords:LargeLanguageModels,DataAugmentation,SyntheticDataGeneration,PsychiatricReports,FewShotPrompt-
ing.
1 Introduction
The digitization of healthcare has led to an exponential increase in the volume of Electronic Health Records (EHRs), offering an
unprecedented opportunity for the application of Artificial Intelligence (AI) and Natural Language Processing (NLP) in clinical
decision support systems. Among clinical narratives, Mental Status Examination (MSE) reports are particularly rich in unstruc-
tured data, capturing psychological, cognitive, and behavioral assessments of patients. However, the development of robust AI
models for psychiatric and psychological domains is severely hindered by data scarcity. Strict data privacy regulations, such
as General Data Protection Regulation (GDPR) in Europe, and the highly sensitive nature of mental health records limit the
availability, sharing, and utilization of real patient data.
Toovercomethebarrierofdataaccess,syntheticdatagenerationthroughDataAugmentationhasemergedasahighlypromis-
ingparadigm. RecentadvancementsinLargeLanguageModels(LLMs)havedemonstratedremarkablecapabilitiesingenerating
coherent, domain-specific text. Despite this potential, generating synthetic medical reports that are both clinically accurate and
∗guillermo.iglesias@upm.es
†gema.borgaz@upm.es
‡m.navas@upm.es
§cristian.ramirez@upm.es
¶merce.salvador@salud.madrid.org
‖enrique.baca@uam.es
1
arXiv:2604.27014v1  [cs.LG]  29 Apr 2026

sufficiently diverse remains a complex challenge. Synthetic clinical text must faithfully reflect the semantic and linguistic prop-
erties of real reports associated with specific diagnoses, e.g. International Classification of Diseases, Tenth Revision (ICD-10)
codes[1], while strictly avoiding the memorization of original patient data, which would constitute a privacy violation. Fur-
thermore, models often suffer from mode collapse, producing repetitive text that lacks the natural variability of human-authored
clinical notes.
In this paper, a robust methodology for the targeted data augmentation of mental status evaluation reports using state-of-the-
art LLMs is presented. Specifically, we leverage and compare the performance ofDeepSeek-R1[2],OpenBioLLM-Llama3[3],
andQwen3.5[4] in generating synthetic clinical narratives conditioned on targeted ICD-10 codes. Using a proprietary database
ofrealmedicalevaluations,theapproachemploysafew-shotpromptingstrategy. Byprovidingthemodelswithacontextwindow
of𝑛= 10reference cases for a specific ICD-10 code, the LLMs are instructed to synthesize10novel, independent reports that
maintain diagnostic coherence with the underlying medical condition. The result is a set of 940 new synthetic reports.
A primary contribution of this work is the development and application of a comprehensive evaluation framework designed
to rigorously assess the quality of the synthetic medical data. Recognizing that standard generation metrics are insufficient for
clinical NLP, the generated reports are evaluated across three fundamental axes: domain fidelity (how closely the synthetic text
resembles the real distribution), lexical diversity (the variety and richness of the generated language), and plagiarism percentage
(based on the average distance between the original text and the generated synthetic text). This evaluation scheme analyzes both
raw plain text and dense semantic embeddings extracted via theall-MiniLM-L6-v2model.
Toachieveaholisticassessment,arobustbatteryofmetricsarecalculated,includingsemanticsimilaritymeasures(Maximum
Mean Discrepancy (MMD)[5], BERTScore[6], Sentence Mover’s Similarity (SMS)[7], Nearest Neighbor Distance (NND)[8]),
standard translation and n-gram overlap metrics (ROUGE-1, ROUGE-2, ROUGE-L[9], METEOR[10]) and diversity indicators
(Self-BLEU[11], Type-Token Ratio (TTR)[12]). Furthermore, this quantitative analysis is complemented by empirical evalua-
tions, specifically through the visual comparison of the original and synthetic embedding spaces using dimensionality reduction
techniques (Uniform Manifold Approximation and Projection (UMAP)[13] and t-distributed Stochastic Neighbor Embedding
(t-SNE)[14]), alongside frequent n-gram distribution analysis.
The remainder of this paper is structured as follows: Section 2 reviews related work in clinical synthetic data generation.
Section 3 details the methodology, including the data description, the LLM prompting strategy, the augmentation pipeline and
the evaluation framework. Section 4 discusses the results and comparative performance of the models. Section 5 contains the
conclusions of the research.
2 Related Work
Thechallenge posedby thescarcityof annotatedtextdatasets inNLP hasgivenrise toa diverseecosystemof dataaugmentation
techniquesdesigned toexpand trainingdatasetswithout theneed formanuallabeling. Earlystrategies focusedprimarily onrule-
basedmanipulations(suchastheEasyDataAugmentation(EDA)framework[15])orneuralnetwork-basedapproaches(applying
retranslation[16]or“Mixup”interpolation[17]). Althoughthesemethodsareeffectiveforgeneratinggeneralsynthetictext,they
often lack the contextual nuances required for specific applications in particular domains.
Intheclinicalsetting,thegenerationofsyntheticEHRdataisfurthercomplicatedbyGDPRregulationsandtheclinicalneed
to maintain diagnostic consistency. Unlike general text, clinical narratives must adhere to a structured medical logic; therefore,
specialized approaches in this specific field have incorporated medical ontologies to ensure that the generated symptoms are
accurate [18]. This requirement for accuracy has led to research on prompt engineering. For example, in the work by Moral-
González et al. [19], they demonstrated that providing detailed instructions,ranging from basic descriptions to comprehensive
clinical guidelines, to generate texts directly influences a model’s ability to maintain medical accuracy. Furthermore, hybrid
frameworks have emerged that combine the generative power of LLMs with traditional rule-based systems to address complex
challenges such as the classification of rare diseases [20].
The most recent research focuses on state-of-the-art reasoning models, which have a superior ability to capture the complex
reasoning found in a MSE. Frameworks such asAugGPThave demonstrated the potential of AI to reformulate clinical sets with
highsemanticfidelity[21],andotherrecentstudieshighlighthowLLMsareparticularlywell-suitedfortasksrequiringsignificant
reasoning effort, where the context between symptoms is as important as the symptoms themselves [22].
Building on this prior work, our study presents a specific methodology for improving the generation of synthetic text related
toclinicalreportsbyleveragingandcomparingtheperformanceofdifferentLLMs. Unlikeprevioushybridapproachesorsimple
reformulation, we employ a few-shot prompt strategy strictly governed by ICD-10 codes to ensure that the synthetic reports
maintain high diagnostic consistency. Furthermore, a key contribution of this research is the proposal of a multidimensional
evaluation framework for the generated texts, based on various metrics from the field of NLP. By integrating lexical, semantic,
andplagiarismindicatorsintothisevaluationframework,weprovidevalidationtoensurethatthegenerateddataarebothclinically
viable and privacy-safe.
2

3 Methodology
3.1 Clinical Dataset
The foundation of this research is a proprietary clinical dataset comprising25,803real medical reports. These records were
systematically extracted from the psychiatric and psychological emergency clinic of Fundación Jiménez Díaz (Grupo Quirón
Salud - Madrid, Spain). Using data from a real-world emergency clinical setting is highly advantageous, as it faithfully captures
the linguistic nuances, urgency, and unstructured nature typical of frontline mental health assessments.
Each record in the dataset contains a free-text MSE narrative detailing the patient’s diagnostic evaluation. Given the highly
descriptivenatureofpsychiatricassessments,thereportsexhibitsignificantvariationinlengthanddetail. Onaverage,textlengths
are48.3characters,withaminimumof2andamaximumof2,560characters,reflectingahighlyheterogeneouscorpusthatranges
from concise emergency summaries to extensive clinical histories.
Crucially for the augmentation task, each report is annotated with one or more diagnostic codes corresponding to the ICD-
10. The dataset is formulated as a multi-label classification problem, where a single report may be assigned multiple concurrent
diagnoses, capturing clinical comorbidities.
In total, the dataset encompasses a label space of94distinct ICD-10 categories. An analysis of the label distribution of the
datasetrevealsastrongprevalenceoftheICD-10’F’chapter,specificallyMental,BehavioralandNeurodevelopmentaldisorders.
Thisincludes,butisnotlimitedto,mood(affective)disorders(e.g.,F30-F39suchasBipolardisordersandDepressiveepisodes),
anxiety, dissociative, stress-related, and somatoform disorders (e.g., F40-F48), as well as mental and behavioral disorders due to
psychoactivesubstanceuse(e.g.,F10-F19). Thepresenceofthese94specificdiagnosticlabelsservesastheconditioningground
truth for the targeted synthetic data generation process performed by the LLMs.
3.2 Prompt Engineering and LLM Setup
To carry out the targeted data augmentation, we evaluated three state-of-the-art LLMs:DeepSeek-r1:32b,OpenBioLLM-Lla
ma3-70b.i1-q4_k_m.gguf, andQwen3.5:35b-a3b-q8_0. The selection of these specific medium-sized models, alongside
the use of quantized versions (such as the 4-bit and 8-bit quantizations forOpenBioLLM-Llama3andQwen3.5, respectively), is
a strategic decision to balance advanced natural language understanding and clinical domain knowledge with the constraints of
privacy concerns in the medical field.
Our generative approach relies on a meticulously designed few-shot prompting strategy to instruct the models to synthesize
realistic, medically accurate Spanish clinical narratives. By providing in-context learning examples, the models are guided to
emulate the specific linguistic style, length, and terminology of the original emergency department reports.
The prompt architecture is modularly divided into a system prompt and a structured user query, as detailed below.
System Prompt: The models are initially contextualized through a system prompt that defines their persona and output con-
straints. TheLLMisinstructedtoactasaspecializedmedicalassistanttaskedwithgeneratingbriefclinicaldiagnosesinSpanish.
Crucially,tofacilitateautomatedparsinginthedatapipeline,thesystempromptenforcesastrictstructuralconstraint,mandating
thattheoutputmustbeexclusivelyavalid,correctlyclosedJSONobjectwithoutanyconversationalfillerormarkdownformatting.
system_prompt
Eres un a s i s t e n t e medico e s p e c i a l i z a d o en generar
d i a g n o s t i c o s cl in ico s breves en espanol .
D evu el ve u n i c a m e n t e un JSON ** valido y cerrado
c o r r e c t a m e n t e ** ( todas las llaves deben estar
b a l a n c e a d a s ) .
No i nc lu ya s co mi lla s triples ni texto a d i c i o n a l .
El JSON debe tener esta e s t r u c t u r a exacta :
{
" d i a g n o s t i c o s ": [" D i a g n o s t i c o A " , " D i a g n o s t i c o B
" , ...]
}
system_prompt (English translation)
You are a medical a s s i s t a n t s p e c i a l i z e d in g e n e r a t i n g
brief c li ni ca l d i a g n o s e s in Spanish .
Return only a ** valid and p ro pe rl y closed ** JSON ( all
curly braces must be bal an ce d ) .
Do not include triple quotes or a d d i t i o n a l text .
The JSON must have this exact s t r u c t u r e :
{
" d i a g n o s i s ": [" D i a g n o s i s A " , " D i a g n o s i s B " , ...]
}
User Query Structure:The main prompt delivered to the model is dynamically constructed for each target diagnostic label
using three main components:
1.Context Initialization(start_prompt): This introductory segment informs the model that it will be provided with an
ICD-10 code and a set of associated real clinical examples.
3

start_prompt
A c o n t i n u a c i o n tienes i n f o r m a c i o n sobre una
et iq ue ta CIE -10 y ej em pl os de d i a g n o s t i c o s
a s o c i a d o s :
start_prompt (English translation)
Below is i n f o r m a t i o n about a CIE -10 code and
e xam pl es of a s s o c i a t e d d i a g n o s e s :
2.Few-Shot Examples(example_prompt): For each augmentation cycle, the prompt iterates over𝑛= 10real reference
cases extracted from our proprietary database. Each example injected into the prompt specifies the ICD-10 codes, the de-
scriptivenameofthelabel,andtheverbatimtextoftheclinicalreport. Thisgroundsthemodelintheactualdistributionof
the data.
example_prompt
- Codigos CIE -10 a s o c i a d o s al ejemplo : { code }
- Nombre de la et iq uet a : { c o d e _ n a m e }
- D i a g n o s t i c o de ejemplo : { example }
example_prompt (English translation)
- ICD -10 codes a s s o c i a t e d with the example : { code
}
- Label name : { c o d e _ n a m e }
- Example d i a g n o s i s : { example }
wherecodeis the corresponding ICD-10 code,code_nameis the description of the code andexampleis one random
example from the real dataset.
3.Task Formulation(end_prompt): Thefinalsegmentsynthesizestheobjective. Itexplicitlyinstructsthemodeltogenerate
a precise number of new, distinct clinical diagnoses corresponding to the target ICD-10 code. It reiterates the strict JSON
formatting requirement, mapping each new case to its generated diagnostic text.
end_prompt
Tu tarea es generar e x a c t a m e n t e { n } d i a g n o s t i c o s
cl in ic os nuevos , d i s t i n t o s de los anteriores , que
c o r r e s p o n d a n a la e ti que ta { code } -{ c o d e _ n a m e }.
De vu el ve la r e s p u e s t a como un JSON con esta
e s t r u c t u r a exacta :
{
" caso 1": {
"[ l i s t a _ c o d i g o s ]":" D i a g n o s t i c o 1"
} ,
" caso 2": {
"[ l i s t a _ c o d i g o s ]":" D i a g n o s t i c o 2"
} ,
...
}
Debe ser JSON valido , sin ningun texto a d i c i o n a l .
end_prompt (English translation)
Your task is to ge ne ra te exactly { n } new cli ni ca l
diagnoses , d is ti nc t from the p re vio us ones , that
c o r r e s p o n d to the label { code } -{ c o d e _ n a m e }.
Return the r es po nse as JSON with this exact
s t r u c t u r e :
{
" case 1": {
"[ c o d e _ l i s t ]":" D i a g n o s i s 1"
} ,
" case 2": {
"[ c o d e _ l i s t ]":" D i a g n o s i s 2"
} ,
...
}
It must be valid JSON , with no a d d i t i o n a l text .
In theend_prompt,nis the number of diagnosis to generate in each LLM call,codeis the corresponding ICD-10 code to
generate andcode_nameis the description of the code.
Bystructuringtheinputinthismodularfashion,weensurethattheLLMsaredeeplycontextualizedbyrealdiagnosticnuances
whilebeingheavilyconstrainedintheiroutputformat,therebymaximizingtheefficiencyandreliabilityoftheautomatedsynthetic
data generation pipeline.
3.3 Inference and Generation Pipeline
To generate synthetic data, we implemented an automated iterative processing workflow. The inference process is systematically
structured to cover the entire spectrum of ICD-10 codes present in the dataset.
For each ICD-10 code processed, the generation algorithm selects𝑚= 10real clinical cases that have been previously
reviewed and validated. These10cases are dynamically integrated into the prompt via theexample_promptcomponent, estab-
lishingarobustfew-shotlearningparadigm. Byprovidingthisnumberofexamples,themodelhassufficientlexicalandstructural
variability to understand the nuances of the specific disorder without exceeding the context window.
4

After presenting the examples, an inference call is made to the LLM, with the instruction to generate𝑛= 10new and unique
synthetic diagnoses for a target code. This10 input examples for 10 output diagnosesloop is repeated for each ICD-10 code and
for each of the models (DeepSeek-R1,OpenBioLLMLlama3, andQwen 3.5).
SinceLLMscangenerateadditionalconversationaltext(format hallucinations)despitetheinstructionsinthesystemprompt,
thepipelineincludesacriticalpost-processingstep. Therawresponsereturnedbythemodelisanalyzedusingregularexpressions
to locate and extract only the block of text enclosed in curly braces, ensuring that the underlying JSON object is captured.
3.4 Evaluation Framework
Toassessthequality,utility,andsafetyofthegeneratedsyntheticclinicalreports,weimplementedamulti-dimensionalevaluation
scheme. Relying on standard n-gram overlap metrics is often inadequate for clinical NLP, as medical text requires adherence to
domain knowledge. Thus, our evaluation framework is divided into three core dimensions: Semantic Fidelity, Lexical Diversity
and Novelty, and Privacy and Plagiarism Analysis. Both raw plain texts and dense semantic embeddings, extracted via the
all-MiniLM-L6-v2sentence transformer, were utilized to compute the metrics.
3.4.1 Semantic Fidelity
This dimension evaluates how closely the synthetic diagnoses resemble the real clinical reports in terms of meaning, contextual
structure, and overall domain distribution.
•Maximum Mean Discrepancy (MMD)[5]:This statistical measure evaluates domain fidelity by calculating the distance
between the embedding distributions of the real and synthetic reports. A lower MMD indicates that the LLM has success-
fully approximated the true data manifold of the original psychiatric emergency records.
•BERTScore[6]:This metric leverages pre-trained language models to compute token-level semantic similarity (reporting
Precision, Recall, and F1-score) between generated texts and reference cases. It is particularly valuable for capturing deep
contextual equivalence rather than relying on exact word matches.
•SMS[7]:Adapting the concept of Word Mover’s Distance, SMS evaluates the continuous semantic representation at the
sentence level, assessing the distance required to align the synthetic text’s meaning with the original clinical reports.
•N-gram Overlap Metrics (ROUGE[9] & METEOR[10]):We compute standard machine translation metrics (ROUGE-
1, ROUGE-2, ROUGE-L, and METEOR) to measure surface-level linguistic alignment. These metrics quantify how well
standard clinical phrasing, terminology, and syntax are preserved in the augmented data.
Additionally, an empirical visual assessment was carried out. To qualitatively validate the distributional alignment, we apply
dimensionalityreductionalgorithms,specificallyUMAP[13]andt-SNE[14]toprojectthehigh-dimensionalall-MiniLM-L6-v2
embeddings into a 2D space. This visual comparison provides immediate insight into the structural overlap between the real and
synthetic cohorts.
3.4.2 Lexical Diversity
A common failure mode in generative models, particularly when conditioned on specific prompts, ismode collapse, where the
model produces highly repetitive, template-like text. This subsection measures the linguistic richness and natural variance of the
augmented corpus.
•Self-BLEU[11]:BLEUscoremeasuresinternaldiversityofeachgeneratedsyntheticreportagainsttherestofthegenerated
set. A lower Self-BLEU score is highly desirable, as it indicates minimal internal repetition and confirms that the model is
generating novel phrasing rather than defaulting to a standard output.
•Type-Token Ratio (TTR)[12]:measuresthevocabularyrichnessofthesyntheticcorpusbycalculatingtheratioofunique
words(types)tothetotalnumberofwords(tokens). AhigherTTRreflectsavaried,expansive,andnaturalclinicallexicon.
3.4.3 Privacy/Plagiarism Preservation
Given the highly sensitive nature of MSE reports, generating synthetic data must strictly avoid memorizing and regurgitating the
few-shot reference examples. Such memorization would constitute a critical privacy breach, defeating the purpose of synthetic
data generation.
5

•NND[8]:For every synthetic report, we calculate the cosine distance to its closest real report in the semantic embedding
space. While the average NND serves as a proxy for structural similarity. The greater this distance, the more it indicates
that the generation of new data that is almost identical to the original is being avoided.
•Plagiarism Rate:This metric measures the proportion of synthetic reports that are excessively similar to real reports,
thereby indicating potential data leakage. It is computed as the percentage of synthetic texts whose NND to a real patient
record falls below a predefined distance threshold in the normalized embedding space. A synthetic report is considered
plagiarized if its NND satisfies𝑑 <0.05.
3.5 Experimental setup
Experiments and tests were conducted on two 48 GB Nvidia Quadro RTX 8000 GPUs and an Intel Xeon Bronze 3206R CPU
@ 1.90GHz. To download and infer data with LLMs the Ollama package version 0.17.7 was used. All source code is open and
accessible at https://------1.
The experiments performed for data augmentation inference took 4 hours, 30 minutes and 21 seconds, and the evaluation of
the results required 27 minutes and 9 seconds.
4 Results and Discussion
Toevaluatetheefficacyoftheproposeddataaugmentationpipeline,weconductedacomparativeanalysisofthesyntheticclinical
recordsgeneratedbyDeepSeek-R1,OpenBioLLM-Llama3,andQwen 3.5. Table1summarizestheperformanceofeachmodel
across our predefined metrics, encompassing semantic fidelity, lexical diversity, and privacy/plagiarism preservation.
Model Name MMD▾ BERTScore F1▴ SMS▾Rouge-1▾Rouge-2▾Rouge-L▾
DeepSeek-R1:32b 0.012 0.6900.514 0.074 0.005 0.068
OpenBioLLM-Llama3:70b 0.027 0.6860.4310.064 0.007 0.059
Qwen 3.5:35b 0.015 0.689 0.5000.059 0.003 0.057
Dimension Semantic fidelity
Model Name METEOR▾ Self BLEU▾TTR▴ NND▴Plagiarism Rate▾
DeepSeek-R1:32b 0.056 0.134 0.986 0.186 0.060
OpenBioLLM-Llama3:70b 0.040 0.234 0.978 0.203 0.100
Qwen 3.5:35b 0.053 0.120 0.991 0.232 0.023
Dimension Semantic fidelity Lexical diversity Privacy/Plagiarism preservation
Table 1: Synthetic text metrics forDeepSeek-R1,OpenBioLLM-Llama3andQwen 3.5.▴denotes that the higher the metric,
the better; whereas▾denotes that the lower the metric, the better.
4.1 Semantic Fidelity
In terms of overall domain adaptation, MMD results reveal thatDeepSeek-R1achieved the lowest divergence (0.012) between
the synthetic and real distributions. This indicates a superior ability to capture the underlying data manifold of real psychiatric
reports.
When evaluating deep semantic equivalence at the sentence and token levels, the Average BERTScore F1 and Average SMS
providedconsistentinsights.DeepSeek-R1alsoyieldedthehighestAverageBERTScoreF1of0.690whereasOpenBioLLM-Llama3
gotthebestAverageSMSresultswith0.431,demonstratingthatthegeneratednarrativesnotonlymatchedtheclinicalvocabulary
but also maintained the nuanced contextual meaning of the targeted ICD-10 diagnoses.
Surface-levellinguisticoverlapwasassessedusingROUGE(1,2,andL)andMETEORmetrics. Whilethesemetricspenalize
deviationsfromexactphrasing,whichissomewhatexpectedandevendesiredinsyntheticgenerationtoensurenovelty,theresults
were distributed across models.Qwen 3.5:35bdemonstrated the highest novelty in terms of ROUGE, achieving a ROUGE-L
of 0.057, whileOpenBioLLMLlama3:70bmaintained the highest baseline structural fidelity with a METEOR score of 0.040.
1Code repository will be available at article’s acceptance
6

That said, all the models have similar performance in semantic fidelity, suggesting a high similarity between the original and
the synthetic texts.
Figure 1 shows an empirical visual assessment using t-SNE and UMAP over the text embeddings. As can be seen, the
probabilitydistributionofrealandsyntheticdataisthesame,suggestingthattherearenovisibledifferencesbetweenbothsources
of data.
Figure 1: Latent representation of real and synthetic texts using the embeddings produced withall-MiniLM-L6-v2sentence
transformer. Dimensionality reduction was performed using a) t-SNE and b) UMAP.⦁shows real data,⦁shows synthetic data
generatedwithDeepSeek-R1,⦁showssyntheticdatageneratedwithOpenBioLLM-Llama3and⦁showssyntheticdatagenerated
withQwen 3.5.
4.2 Lexical Diversity
Acriticalsuccessfactorinclinicaldataaugmentationisthegenerationofaheterogeneouscorpus. OuranalysisofTTRandSelf-
BLEU highlights significant differences in how the models handled vocabulary variance.Qwen 3.5demonstrated the highest
vocabulary richness with a TTR of 0.991, producing a highly varied lexicon of medical terminology. The other models have
similar performance in terms of TTR.
Qwen 3.5successfullymitigatedmodecollapse, recordingthelowestSelf-BLEUscore(0.120). AlowSelf-BLEUconfirms
that the model generated distinct, independent reports for each iteration rather than converging on a single, repetitive diagnostic
template. Incontrast,OpenBioLLM-Llama3exhibitedahigherSelf-BLEU(0.234),indicatingaslighttendencytowardstructural
repetition across its generated outputs.
4.3 Privacy/Plagiarism Preservation
To ensure that the few-shot prompting did not result in the memorization and regurgitation of real patient data, we analyzed the
NNDintheembeddingspace. AllthreemodelsmaintainedanAverageNNDwellaboveourstrictplagiarismthreshold(𝑑 <0.05).
Specifically,Qwen 3.5exhibited an Average NND of 0.232 and the lowest percentage (2,3%) of cases with𝑑 <0.05. The
distances achieved confirm that while the models learned the semantic distribution of the specific ICD-10 codes, they generated
genuinelysyntheticandnovelpatienthistories,therebysuccessfullypreservingpatientprivacyandpassingthedataleakageaudit.
5 Conclusion
The scarcity of high-quality, annotated clinical data, with strict privacy regulations, remains a fundamental bottleneck in the
development of NLP systems for mental health. In this paper, we proposed and evaluated a comprehensive data augmentation
methodology utilizing state-of-the-art LLMs (DeepSeek-R1,OpenBioLLM-Llama3, andQwen 3.5) to generate synthetic MSE
reports conditioned on specific ICD-10 codes.
7

To overcome the limitations of standard text generation metrics, we introduced a rigorous, multi-dimensional evaluation
framework that assesses the generated data across semantic fidelity, lexical diversity, and privacy preservation. Our comparative
analysis yielded promising results: all evaluated models demonstrated a strong capacity to approximate the semantic distribution
of real clinical records. Specifically,DeepSeek-R1showed the highest domain semantic fidelity, achieving the lowest MMD
(0.012) and the highest BERTScore F1 (0.690). Conversely,OpenBioLLM-Llama3provided the best alignment in continuous
sentence representation (Average SMS of 0.431) and the lowest surface-level overlap (METEOR of 0.040), although it exhibited
slightly higher ROUGE scores compared toQwen 3.5. On the other hand,Qwen 3.5excelled in producing the most lexically
diverse text, successfully mitigating mode collapse with the lowest Self-BLEU score (0.120) and the highest TTR (0.991).
Crucially, our privacy auditing confirmed that the applied few-shot prompting strategy did not trigger the memorization of
original patient data. All models maintained an Average NND well above the strict plagiarism threshold (𝑑 <0.05), ensuring
that the synthetic narratives are genuinely novel and safely preserve patient confidentiality.
Thesefindingsdemonstratethattargeteddataaugmentationviamedium-sized,quantizedLLMsisahighlyviable,secure,and
efficientsolutionforexpandingclinicaldata. Futureworkwillfocusonintegratingthesyntheticcorpusintodownstreamclinical
classification tasks to quantify the performance gains achieved by training predictive models on augmented data. Additionally,
expanding the generation pipeline to cover other specialized medical domains could further validate the generalization of this
framework.
A Acknowledgements
ThisstudyissupportedbytheDirecciónGeneraldeInvestigacióneInnovaciónTecnológicadelaComunidaddeMadrid(Orden
3177/2024) through the I+D Technological activities program (TEC-2024/COM-224).
This research was supported by CIBER -Consorcio Centro de Investigación Biomédica en Red- (CB/07/09/0025), the Insti-
tuto de Salud Carlos III with the support of the European Regional Development Fund (ISCIII PI23/00614; PMP24/00026), by
Fundació la Marató de TV3 (202226-31) and by CaixaResearch Health 2023 LCF/PR/HR23/52430033.
References
[1] World Health Organization. International Statistical Classification of Diseases and Related Health Problems (ICD-10).
vol. 1. 5th ed. Geneva: World Health Organization; 2016. Available from: https://icd.who.int/browse10/2016/en.
[2] DeepSeek-AI. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. arXiv preprint
arXiv:250112948. 2025. Available from: https://arxiv.org/abs/2501.12948.
[3] AnkitPalMS.OpenBioLLMs: AdvancingOpen-SourceLargeLanguageModelsforHealthcareandLifeSciences.Hugging
Face; 2024. https://huggingface.co/aaditya/OpenBioLLM-Llama3-70B.
[4] Qwen Team. Qwen3.5: Towards Native Multimodal Agents; 2026. Available from: https://qwen.ai/blog?id=qwen3.5.
[5] Gretton A, Borgwardt KM, Rasch MJ, Schölkopf B, Smola A. A kernel two-sample test. The journal of machine learning
research. 2012;13(1):723-73.
[6] Zhang T, Kishore V, Wu F, Weinberger KQ, Artzi Y. Bertscore: Evaluating text generation with bert. arXiv preprint
arXiv:190409675. 2019.
[7] Clark E, Celikyilmaz A, Smith NA. Sentence mover’s similarity: Automatic evaluation for multi-sentence texts. In: Pro-
ceedings of the 57th annual meeting of the association for computational linguistics; 2019. p. 2748-60.
[8] Clark PJ, Evans FC. Distance to nearest neighbor as a measure of spatial relationships in populations. Ecology.
1954;35(4):445-53.
[9] Lin CY. Rouge: A package for automatic evaluation of summaries. In: Text summarization branches out; 2004. p. 74-81.
[10] Banerjee S, Lavie A. METEOR: An automatic metric for MT evaluation with improved correlation with human judg-
ments. In: Proceedings of the acl workshop on intrinsic and extrinsic evaluation measures for machine translation and/or
summarization; 2005. p. 65-72.
[11] Zhu Y, Lu S, Zheng L, Guo J, Zhang W, Wang J, et al. Texygen: A benchmarking platform for text generation models. In:
The 41st international ACM SIGIR conference on research & development in information retrieval; 2018. p. 1097-100.
8

[12] Templin MC. Certain language skills in children; their development and interrelationships. University of Minnesota Press;
1957.
[13] McInnes L, Healy J, Melville J. Umap: Uniform manifold approximation and projection for dimension reduction. arXiv
preprint arXiv:180203426. 2018.
[14] Van der Maaten L, Hinton G. Visualizing data using t-SNE. Journal of machine learning research. 2008;9(11).
[15] Wei J, Zou K. EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks. In:
Proceedings of EMNLP-IJCNLP; 2019. p. 6382-8.
[16] Shorten C, Khoshgoftaar TM, Furht B. Text data augmentation for deep learning. Journal of big Data. 2021;8(1):101.
[17] Guo H, Mao Y, Zhang R. Augmenting data with mixup for sentence classification: An empirical study. arXiv preprint
arXiv:190508941. 2021.
[18] SpasicI,NenadicG.Clinicaltextdatainmachinelearning: systematicreview.JMIRmedicalinformatics.2020;8(3):e17984.
[19] del Moral-González R, Gómez-Adorno H, Ramos-Flores O. Comparative analysis of generative LLMs for labeling entities
in clinical notes. Genomics & Informatics. 2025;23(1):3.
[20] LyuQ,etal.Ahybridframeworkwithlargelanguagemodelsforrarediseasephenotyping.JournalofBiomedicalInformatics
/ PMC. 2023.
[21] Dai H, Liu Z, Liao W, Huang X, Cao Y, Wu Z, et al. Auggpt: Leveraging chatgpt for text data augmentation. IEEE
Transactions on Big Data. 2025;11(3):907-18.
[22] ChaiY,XieH,QinJS. Textdataaugmentationforlargelanguagemodels: Acomprehensivesurveyofmethods,challenges,
and opportunities. Artificial Intelligence Review. 2026;59(1):35.
9
