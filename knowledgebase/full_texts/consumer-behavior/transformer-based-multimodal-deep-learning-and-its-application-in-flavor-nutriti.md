---
title: Transformer-based multimodal deep learning and its application in flavor-nutrition synchronous
  evaluation
url: https://doi.org/10.1038/s41538-026-01186-8
category: consumer-behavior
subcategory: framework
date: 2026-09
venue: npj Science of Food
authors:
- Wenxi Qi
- Meiqi Ding
- Yi Zhang
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41538-026-01186-8_reference.pdf
pages: 20
chars: 121625
fetched_at: '2026-11-08T18:51:39+00:00'
kb_version: 1
---

# Transformer-based multimodal deep learning and its application in flavor-nutrition synchronous evaluation

npj | science of food Article
Published in partnership with Beijing Technology and Business U niversity & International Union of Food Science and Technology
Article in Press https://doi.org/10.1038/s41538-026-01186-8
Transformer-based multimodal deep
learning and its application in
ﬂavor-nutrition synchronous evaluation
Check for updates
Wenxi Qi1, Meiqi Ding1,Y iZ h a n g1,B oW a n g1 , Che Shen2 &D e n g y o n gL i u1
Flavor chemistry and nutritional quality are the core attributes determining the commercial value and
consumer acceptance of ready-to-eat meals. This study developed a Transformer-based multimodal
deep learning framework that integrates systematic ﬂavor chemistry pro ﬁles, physicochemical
nutrient indices, and visual features to achieve intelligent synchronous assessment of ﬂavor and
nutritional quality of ready-to-eat meals solely from product images. The model achieved 91.5%
classiﬁcation accuracy in distinguishing 32 ready-to-eat meal variants, comprising pork-, chicken-,
and beef-based meals, and demonstrated strong predictive performance for key nutrients, with
determination coefﬁcients (R2) of 0.86 for protein, 0.80 for fat, and 0.79 for carbohydrate after
weighted-Huber optimization, indicating high consistency with physicochemical measurements.
Systematic ﬂavor chemistry characterization via headspace solid-phase microextraction/gas
chromatography-mass spectrometry (HS-SPME/GC-MS) identi ﬁed 77 volatile ﬂavor compounds,
among which 22 key odor-active compounds with an odor activity value (OAV)≥ 1 were screened, with
aldehydes and spice-derived terpenes identiﬁed as major contributors to ﬂavor differentiation among
products. Consumer evaluation ( n = 100) revealed that ﬂavor attributes dominated purchase
decisions, and the model accurately identi ﬁed core ﬂavor descriptors of products. The proposed
model provides a rapid image-based approach for predicting ﬂavor-related attributes and nutritional
quality of ready-to-eat meals. In the future, the framework could serve as an AI-assisted quality-control
tool in centralized kitchens or ready-to-eat meal enterprises, while also being developed into a
consumer-oriented AI application for image-based estimation of macronutrients and calories and
personalized meal recommendations based on ﬂavor preferences and nutritional needs.
Traditional Chinese meat-based culi nary dishes are renowned for their
“color, aroma, taste, and shape ”1. With the acceleration of modern life,
dietary preferences have markedly shift e dt o w a r dc o n v e n ience, prioritizing
accessibility, minimal preparation time, and ease of consumption. This
trend has driven the rapid expansion of the ready-to-eat meal market2 and
encouraged the industrialized transformation of these traditional dishes into
ready-to-eat meals. Particularly, ready-to-eat meals, as frequently consumed
items, play a pivotal role in bridging food technology with daily diets and
hold a central position within the food industry3. In this study, ready-to-eat
meals are operationally deﬁned as standardized, fully cooked, frozen meat-
based meals that only require reheating before consumption, which are the
core products of the central kitchen industrialization model.
Flavor is the core sensory attribute that determines consumer accep-
tance and market competitiveness of r eady-to-eat meals, and systematic
characterization of ﬂavor chemistry proﬁl e si st h ec o r eb a s i sf o rq u a l i t y
standardization and industrial production of these products. Meanwhile,
the intrinsic correlation between ﬂavor chemistry characteristics and
nutritional quality of ready-to-eat meals, as well as the intelligent syn-
chronous evaluation of both attributes, have become a key research hotspot
in the ﬁeld of food ﬂavor chemistry.
However, the mass production of t hese products faces substantial
challenges. Conventional techniques like stir-frying and stewing alter the
sensory and nutritional properties of ingredients. This introduces com-
plexity to standardization and quality control4. Consequently, more rigor-
ous nutritional assessment is necessitated. Concurrently, while nutritional
1College of Food Science and Technology, Bohai University, Jinzhou, China.2Engineering Research Centre of Bio-process, Ministry of Education, Hefei University
of Technology, Hefei, China. e-mail: daqingwb@163.com; s837733211@163.com; jz_dyliu@126.com
npj Science of Food Article in Press
1234567890():,;
1234567890():,;

science is advancing toward precise d ietary assessment and personalized
nutrition5, current food quality evaluation methods still rely heavily on
traditional techniques. These are often too slow for modern industry
demands6, and the effectiveness of conventional nutrition labels in
improving public nutritional literacy remains uncertain7. These limitations
collectively underscore the need for more efﬁcient, accurate, and informa-
tive evaluation systems.
The emergence of artiﬁcial intelligence has catalyzed an iterative evo-
lution in nutritional assessment methodologies8. The integration of com-
puter vision with deep learning technologies has revolutionized food quality
evaluation by enabling rapid analysis9. While conventional convolutional
neural networks have demonstrated capabilities in feature extraction, they
often face limitations in handling complex food matrices and capturing
long-range dependencies10. The Transformer architecture, with its self-
attention mechanism and hierarchica l feature extraction capabilities,
represents a signi ﬁcant advancement in this domain. Transformers can
effectively capture both local textures and global visual cues, establishing
quantitative correlations between image attributes and nutritional
parameters11. However, correlating the visual characteristics of food images
with the ﬂavor, physical and chemical attributes of products to achieve
quantitative identiﬁcation is a challenge.
Existing image-based nutritional assessment studies mostly rely on
single visual modal data, which often struggle to fully characterize the
complex nutritional andﬂavor quality of ready-to-eat meals. For complex
ready-to-eat meals containing mixed meat ingredients, sauces, and side
ingredients, single-modal visual mode ls face inherent limitations. First,
machine vision in object recognition tasks is heavily affected by the inherent
complexity of food products, whi ch can lead to poor-quality image
acquisition12. In complex mixed meals, mutual occlusion between food
ingredients and interference from complex backgrounds severely com-
promise detection and analysis results 13. Furthermore, single-modal
machine vision is highly vulnerable to environmental factors; for instance,
shadows or uneven lighting can cause failures in extracting crucial internal
features of the food matrix14,15. Consequently, algorithms relying solely on
interpreting the macroscopic appearance, shape, and texture of food pro-
ducts are insuf ﬁcient for comprehensive quality and authenticity assess-
ments. However, for complex read y-to-eat meals containing mixed
ingredients, sauces, and diverse processing conditions, visual appearance
alone cannot adequately reﬂect intrinsic ﬂavor chemistry and nutritional
composition. Therefore, integratin g visual information with physico-
chemical andﬂavor-related data is necessary to achieve more reliable quality
evaluation.
Beyond ready-to-eat meals, intelligent food quality evaluation has been
increasingly applied to a broad range of food matrices. Computer vision,
hyperspectral imaging, and deep le arning models have been used for
freshness detection, maturity evaluation, defect recognition, quality grading,
and nutrition-related estimation in fruits, vegetables, cereal grains, and
mixed cooked foods. In parallel, electronic nose, electronic tongue, GC-MS,
and chemometric or machine learning approaches have been widely
adopted to characterize aroma, taste, authenticity, and quality differences in
dairy products, beverages, tea, coffee, cereal products, and fermented foods.
These studies demonstrate the feasibi lity of using image-based, sensor-
based, and data-driven strategies for rapid food quality assessment across
different food systems. However, most existing studies have focused on a
single food category or a single target attribute, such as freshness, ripeness,
adulteration, quality grade, calorie estimation, orﬂavor discrimination. Few
studies have simultaneously linked macroscopic visual characteristics with
systematic ﬂavor chemistry proﬁles and basic nutritional composition in
complex ready-to-eat meals. Therefore, the synchronous prediction ofﬂa-
vor chemistry attributes and nutri tional quality from product images
remains insufﬁciently explored, particularly for ready-to-eat meals con-
taining mixed ingredients, sauces, anddiverse thermal-processing histories.
Representative studies on image-based, sensor-based, and multimodal food
quality assessment in non-meat food systems are summarized in
Supplementary Table S1, highlighting their food matrices, analytical mod-
alities, target attributes, and relevance to the present study.
To address this gap, the integration of multimodal data, including
visual features, physicochemical indicators, andﬂavor characteristics, has
become a key development direction. Recent research emphasizes that food
should be evaluated as a complex system, where accurate assessment
requires decoding the interactions b etween molecular composition and
sensory perception 16. Consequently, data fusion strategies utilizing
advanced deep learning architectures are increasingly adopted for ﬂavor
data analysis17. For instance, the successful application of Transformer-
based models in mapping chemical structures to speciﬁct a s t ep r oﬁles has
proven the capability of self-attention mechanisms in handling high-
dimensional ﬂavor data 18. Furthermore, tailored AI methodologies,
including microbial resource exploration in fermented foods19 and graph-
based decision frameworks for targeted safety sampling20, demonstrate that
customized algorithms are essential for translating laboratory-scale analyses
into practical industrial applications21. From a broader food-technology
perspective, artiﬁcial intelligence and data-driven approaches are increas-
ingly being explored to address food-speci ﬁc analytical challenges and
expand the practical use of intel ligent evaluation technologies21.I nf o o d
companies, such approaches have the potential to support product devel-
opment and rapid quality evaluation by integrating imaging, physico-
chemical, and ﬂavor information through intelligent analytical models. In
this context, these technologies may also facilitate the connection between
industrial food evaluation and consumer-oriented applications.
Grounded in this perspective, this study focuses on 32 widely con-
sumed, ﬂavor-representative ready-to-eat meals. We developed a
Transformer-based deep learning framework that enables rapid image-
based prediction of nutritional andﬂavor attributes after being trained using
multimodal physicochemical andﬂavor-related information. To train and
validate this model, key product attributes, including physical properties,
basic nutrients, and ﬂavor proﬁles characterized by electronic nose, elec-
tronic tongue, and headspace sol id-phase microextraction/gas
chromatography-mass spectrometry (HS-SPME/GC-MS), were compre-
hensively quantiﬁed. This research aims to provide a practical, image-based
tool for nutritional andﬂavor quality control, thereby supporting standar-
dized production and consumer-oriented dietary choices.
The core innovations of this study are as follows: (i) A multi-task
Transformer framework integrating vis ual, physicochemical nutritional,
and systematic ﬂavor chemistry multimodal f eatures was constructed,
which realized synchronous evaluation ofﬂavor and nutritional quality of
ready-to-eat meals, and effectively compensated for the limitations of single-
modal models in the quality assessment of complex ready-to-eat meals; (ii)
The model realized rapid product classi ﬁcation, precise prediction of
nutritional components, and intelligent identiﬁcation of core ﬂavor chem-
istry attributes solely from product images, meeting the needs of on-line
monitoring of ﬂavor and nutritional quality in industrial production; (iii)
The intrinsic correlations between ﬂavor chemistry characteristics, nutri-
tional composition, and consumer s ensory preference of 32 mainstream
ready-to-eat meals in the Chinese mar ket were systematically revealed,
which not only provided data support for formula optimization and stan-
dardized production of products, b ut also offered new insights for
consumer-orientedﬂavor design in the ﬁeld of ﬂavor chemistry.
Results
Consumer sensory evaluation of the 32 products
This study analyzed sensory score data from 100 consumers regarding the
32 ready-to-eat meal samples and identi ﬁed a signi ﬁcant differentiation
trend in consumers’ purchase intentions (PI). Consumer purchase desire
and decision weight scores were shownin Fig. S1a, b, respectively. Products
with relatively high purchase intention scores included N1 (7.70 ± 1.03), N7
(7.75 ± 1.25), and N6 (7.20 ± 1.99). These products (e.g., N1 and N7) were
characterized by pronounced umami or spicy ﬂavor proﬁles. In contrast,
products with relatively low purchase intention scores, such as Z2
(1.70 ± 0.92), Z4 (1.95 ± 0.94), and J8 (2.00 ± 1.12), were often perceived as
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

greasy or bland. The relatively low purchase intention for these products
may be associated with unfavorable sensory attributes, including excessive
greasiness or blandness. The PI scores are presented as mean ± standard
deviation (SD).
The instrumental color parameter a* (redness) of the products showed
as i g n iﬁcant positive correlation with consumers ’ purchase intention
(r = 0.52, P < 0.01). Notably, the color ratings for the highly preferred pro-
ducts N1 and Z9 exceeded 8.0, whereas those for the less favored products
Z2 and J8 generally fell below 7.5. This ﬁnding is consistent with previous
studies on the inﬂuence of visual cues on taste andﬂavor perception22.V i s u a l
characteristics inﬂuence taste expectations andﬂavor perception via sensory
mechanisms. Speciﬁcally, warm hues (e.g., red and orange) often evoke
associations with spicy and rich ﬂavors, while vibrant colors can heighten
the perceived ﬂavor intensity23.
A correlation analysis was conducted between consumers ’ sensory
scores of 32 products and the model’s nutritional component recognition
results to enhance the accuracy and practicality of the recommendation
system. For example, the color andﬂavor proﬁles of highly favored products
(e.g., N1 and N7) were translated into visual identiﬁcation markers to reﬁne
the model ’s selection criteria for “highly accepted” ready-to-eat meals.
Conversely, the oiliness or color imper fections of less desirable products
(e.g., Z2 and J8) were identiﬁed as crucial factors for the model’s feedback
mechanism, aiding consumers in avoiding products with subpar sensory
attributes.
pH value and color of different ready-to-eat meal categories
Table 1 displays the pH value and color index determination results of 32
product samples. Signi ﬁcant discrepancies in pH value and color were
observed among the three categories of ready-to-eat meals (P < 0.05). The
variations primarily arose from the inherent chemical characteristics of the
raw meat, the particular seasonings and spices employed in the processing
techniques, and the intricate chemic al transformations during thermal
processing4.
Signiﬁcant variations in pH values were observed among the 32 ready-
to-eat meals. Chicken-based ready-to-eat meals exhibited a pH range of 4.24
to 7.25. Notably, J5 had the highest pH value at 7.25 ± 0.01, whereas J12 had
the lowest at 4.24 ± 0.02. This wide pH range in chicken-based ready-to-eat
meals may be attributed to the use of alkaline pickling agents (e.g., sodium
Table 1 | Color difference measurement results and pH determination results for 32 ready-to-eat meals
Types of meat Sample L* a* b* pH
Chicken ready-to-eat meals J1 59.42 ± 1.74Aa 8.34 ± 0.27Bb 22.23 ± 1.76Aa 6.19 ± 0.01Ac
J2 56.66 ± 3.1Aab 7.51 ± 0.34Bbcd 19.05 ± 0.10Ac 5.27 ± 0.01 Ah
J3 52.08 ± 1.49Abcd 8.32 ± 0.58Bb 20.92 ± 0.57Aab 5.16 ± 0.03Ai
J4 46.49 ± 1.48Aef 8.16 ± 0.51Bbc 16.86 ± 0.91Ade 5.78 ± 0.01Ae
J5 48.07 ± 2.89Adef 6.61 ± 0.58Bbcd 17.06 ± 1.22Ade 7.25 ± 0.01Aa
J6 40.64 ± 1.50Ag 6.26 ± 0.56Bcd 14.05 ± 0.17Af 5.35 ± 0.01Ag
J7 40.39 ± 1.81Ag 6.11 ± 0.45Bd 14.45 ± 0.32Af 4.56 ± 0.02Ak
J8 47.65 ± 2.73Adef 14.25 ± 1.05Ba 19.66 ± 1.28Abc 5.93 ± 0.01Ad
J9 47.47 ± 2.39Adef 6.64 ± 0.65Bbcd 18.62 ± 1.60Acd 6.41 ± 0.01Ab
J10 43.22 ± 2.35Afg 6.30 ± 0.57Bbcd 15.56 ± 0.45Aef 5.08 ± 0.05Ag
J11 53.07 ± 0.55Abc 6.09 ± 0.56Bd 17.95 ± 0.48Acd 5.45 ± 0.01Af
J12 50.62 ± 2.87Acde 7.23 ± 0.36Bbcd 19.32 ± 1.37Abc 4.24 ± 0.02Al
Pork ready-to-eat meals Z1 34.03 ± 1.05Bf 7.55 ± 0.82Ad 13.17 ± 0.41Ag 5.59 ± 0.03Ad
Z2 49.99 ± 2.71Ba 9.44 ± 0.98Ac 21.19 ± 1.86Aa 4.47 ± 0.01Ai
Z3 42.75 ± 1.82Bc 8.70 ± 0.37Acd 18.34 ± 0.62Abc 4.47 ± 0.02Ai
Z4 39.78 ± 1.34Bd 9.35 ± 0.46Ac 17.77 ± 0.98Abcd 5.39 ± 0.03Ae
Z5 45.42 ± 1.82Bbc 8.79 ± 0.53Acd 19.04 ± 1.16Ab 6.22 ± 0.06Aa
Z6 37.23 ± 1.75Bde 9.96 ± 0.17Abc 15.92 ± 1.06Adef 4.72 ± 0.01 Ah
Z7 35.86 ± 0.54Bef 9.42 ± 0.46Ac 15.25 ± 0.28Aefg 4.52 ± 0.03Ai
Z8 47.30 ± 0.81Bb 12.26 ± 0.16Aa 21.58 ± 0.48Aa 4.76 ± 0.05 Ah
Z9 25.79 ± 0.98Bg 5.92 ± 0.38Ae 6.98 ± 0.53Ai 5.88 ± 0.03Ac
Z10 52.26 ± 2.06Ba 8.97 ± 0.51Acd 16.55 ± 1.80Acde 6.02 ± 0.01Ab
Z11 35.73 ± 1.16Bef 11.07 ± 3.10Aab 13.79 ± 1.14Afg 5.30 ± 0.06Af
Z12 33.10 ± 0.93Bf 11.35 ± 0.37Aa 9.72 ± 0.45 Ah 4.83 ± 0.04Ag
N1 40.13 ± 2.18Bab 6.79 ± 0.43Acd 11.09 ± 0.99Bd 6.66 ± 0.01Aa
N2 34.62 ± 2.24Bc 7.95 ± 3.06Abcd 13.45 ± 4.43Bbcd 5.12 ± 0.07Ae
N3 36.41 ± 1.07Bbc 6.82 ± 0.38Acd 12.53 ± 0.79Bcd 5.21 ± 0.01Ad
Beef ready-to-eat meals N4 42.34 ± 2.89Ba 9.91 ± 0.61Ab 16.65 ± 0.75Ba 5.21 ± 0.01Ad
N5 38.51 ± 0.40Babc 6.44 ± 0.59Ad 11.84 ± 0.20Bcd 5.94 ± 0.02Ac
N6 36.73 ± 2.27Bbc 9.38 ± 1.10Ab 15.53 ± 0.94Bab 6.05 ± 0.04Ab
N7 36.89 ± 1.96Bbc 8.97 ± 1.02Abc 13.08 ± 0.97Bbcd 4.48 ± 0.01Af
N8 42.20 ± 1.81Ba 14.47 ± 1.42Aa 14.68 ± 1.38Babc 4.25 ± 0.01Ag
Different lowercase letters within the same column indicate signi ﬁcant differences within groups ( P < 0.05). Different uppercase letters within the same column indicate signi ﬁcant differences between
groups (P < 0.05).
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

carbonate for meat tenderization) in high-pH samples, and acidic season-
ings (e.g., vinegar) in low-pH samples. For example, sodium carbonate may
have been employed in sample J5 while the addition of a substantial amount
of vinegar in sample J12 led to varying pH values. The overall acidic nature
of pork-based ready-to-eat meals aligns with the prevalent use of sweeteners
and acidulants in traditional culinary practices like ﬁsh-ﬂavored (a classic
Sichuan ﬂavor proﬁle utilizing pickled chilies, garlic, ginger, and vinegar,
without actual ﬁsh) and sweet and sour (dishes characterized by a sauce
made of sugar and vinegar) products. The pH values ranged from 4.47 to
6.22. Z5 exhibited the highest pH value at 6.22 ± 0.06, while Z2 and Z3 had a
relatively low pH of 4.47. Beef-basedready-to-eat meals showed a pH range
between 4.25 and 6.66. N1 had the highest pH value at 6.66 ± 0.01, whereas
N8 had the lowest at 4.25 ± 0.01. The lower pH values in most beef-based
ready-to-eat meals could be attributed to the use of vinegar, tomato sauce,
and other seasonings.
Beyond merely re ﬂecting differences in culinary formulations, the
observed pH variations may be asso ciated with lipid stability and ﬂavor
release across the ready-to-eat mealsamples. Lower pH conditions, mainly
related to the use of acidic seasonings, may promote lipid oxidation during
thermal processing and thereby contribute to the formation and release of
secondary lipid-derived volati le compounds, such as aldehydes 24,25.I n
addition, acidic conditions may in ﬂuence ﬂavor formation and release
pathways by affecting reactions such as the esteriﬁcation of organic acids
with alcohols, as well as Maillard-related reactions and lipid degradation26.
Therefore, the pH variations observed in these ready-to-eat meals may
contribute to differences in volatile ﬂavor proﬁles and oxidative stability,
although these associations should beinterpreted together with other for-
mulation and processing factors.
The color parameter analysis revealed a close association between L*
and the primary meat type, while the a* and b* values were predominantly
inﬂuenced by the Maillard reaction degree and spice additions27. Chicken-
based ready-to-eat meals exhibited the highest brightness values, ranging
from 40.39 to 59.42, with J1 displaying the highest brightness at 59.42 ± 1.74.
The higher L* i nc h i c k e nm e a ti sl i n k e dt oi t sl i g h t e rm y oﬁbrillary color28.
Pork-based ready-to-eat meals displayed a wide variation in brightness,
ranging from 25.79 to 52.26, with Z10 being the brightest and Z9 the dullest.
In contrast, beef-based ready-to-eatmeals generally had lower brightness
levels, ranging from 34.62 to 42.34, withN4 exhibiting the highest bright-
ness. The a* value was higher in pork-based ready-to-eat meals, with Z8
measuring 12.26 ± 0.16 and Z12 measuring 11.35 ± 0.37. The highest a *
value among chicken-based ready-t o-eat meals was observed in J8, at
14.25 ± 1.05. Among beef-based ready-to-eat meals, N8 showed the highest
a* value, at 14.47 ± 1.42. The b * values of beef-based ready-to-eat meals
were generally lower than those of chicken- and pork-based ready-to-eat
meals, with the highest value observed in N4 at 16.65 ± 0.75. By comparison,
J1 showed the highest b* value among chicken-based ready-to-eat meals,
reaching 22.23 ± 1.76, while Z8 showed the highest b* value among pork-
based ready-to-eat meals, reaching21.58 ± 0.48. Notably, when beef-based
ready-to-eat meals included vegetab le ingredients, their overall color
appeared darker, which may be associated with non-enzymatic browning of
vegetable components during thermal processing. This observation aligned
with previous research ﬁndings regarding changes in vegetable quality
during cooking29,30.
Determination of basic nutrients in different ready-to-eat meal
categories
The statistical analysis presented in Table2 revealed signiﬁcant differences
in the contents of protein, fat, moisture, ash, carbohydrate, and sodium
among the 32 product samples (P < 0.05).
The protein content of the 32 products ranged from 2.85 ± 0.11 g (J5)
to 15.32 ± 0.35 g (J3). Notably, the protein content of J3 and J6 was sig-
niﬁcantly higher than that of the other products (P < 0.05), while J5 and N7
exhibited signiﬁcantly lower protein levels. Among chicken-based ready-to-
eat meals, J3 had the highest protein value, whereas J5 had the lowest. In the
beef category, N2 and N3 showed relatively high protein contents of
11.50 ± 0.06 g and 11.58 ± 0.25 g, respectively. Among pork-based ready-to-
eat meals, Z7 had the highest protein content at 14.26 ± 1.09 g, while Z3 had
t h el o w e s ta t2 . 9 5±0 . 1 7g .T h ep r o t e i nc o n t e n to fp o r k - b a s e dr e a d y - t o - e a t
meals Z11 and Z12 was relatively prominent, potentially due to the use of
pig’s feet as raw material, which are rich in collagen. The fat content varied
signiﬁcantly across different ready-to- eat meal categories. Pork-based
ready-to-eat meals contained signiﬁcantly higher fat levels compared with
chicken- and beef-based ready-to-eat meals, while the overall fat content in
beef-based ready-to-eat meals remained relatively low.
The fat content of the products ranged from 2.27 ± 0.36 g (J3) to
32.58 ± 2.56 g (Z1). The fat content of Z1 and Z2 was signiﬁcantly greater
than that of the other products ( P < 0.05), while J3 and N7 displayed sig-
niﬁcantly lower fat content. High-fat products predominantly concentrated
in traditional braised products (e.g., slow-cooked pork belly in soy sauce and
caramelized sugar), aligning with the conventional recipes of Chinese cui-
sine that emphasize fatty meat as the primary ﬂavor. The use of lard in
products to enhanceﬂavor also contributed to an increase in fat content.
The carbohydrate content ranged from 2.43 ± 0.29 g (N3) to
13.32 ± 0.28 g (N6). Among chicken-based ready-to-eat meals, J12 con-
tained 11.82 ± 0.39 g of carbohydrate, while among pork-based ready-to-eat
meals, Z8 contained 12.96 ± 0.61 g. During the production of N4, sugar was
typically added for seasoning, which increased the carbohydrate content of
t h ep r o d u c t .I nt h eN 6s a m p l e ,p o t a t o e ss e r v e da ss i d ei n g r e d i e n t sa n d
constituted a substantial source of carbohydrates, resulting in relatively high
carbohydrate content.
The sodium content in the products ranged from 329.18 ± 5.27 mg
(Z3) to 1235.14 ± 4.22 mg (Z10). Sodium content in Z10 and
N4 signiﬁcantly exceeded that of other products (P < 0.05), while Z3 and
Z6 showed signiﬁcantly lower sodium levels. This suggests potential issues
with excessive seasoning in certain processed products. The extended
cooking time for soybeans and the richness of meat juice in pork knuckles
likely led to the high salt content in Z10.
Analysis of electronic noses and electronic tongues for different
ready-to-eat meals
The determination results of volatileﬂavor substances in 32 commercially
available ready-to-eat meals, as analyzed by the electronic nose, are pre-
sented in Fig. 1a–c. Analysis revealed that sensors such as W5S (nitrogen
oxides), W1W (sulﬁdes and pyrazines), W1S (methyl compounds), and
W2S (alcohols, aldehydes, and ketones) exhibited signiﬁcant responses. This
ﬁnding indicated substantial diffe rences in the abundances of nitrogen
oxides, sulﬁdes, hydrocarbons, and alcohol-aldehyde-ketone compounds
across various ready-to-eat meals. Notably, the response values of samples J1
and Z6 on the W5S sensor were highly pronounced. This prominence likely
resulted from the production of increased nitrogen oxides during the
thermal processing and seasoning of these two products, as such substances
are key contributors to the characteristicﬂavor of meat.
In contrast, sensors like W3S (long-chain alkanes), W6S (hydrides),
W1C (aromatic compounds), and W5C (alkenes and short-chain aromatic
substances) exhibited relatively mi nor response variations. The volatile
component proﬁles of diverse samples were depicted by color gradients,
mirroring the ﬂavor distinctions among various ready-to-eat meals. These
differences could stem from variations in the primary constituents and
processing methods of the samples31. For example, the response of beef-
based ready-to-eat meal N4 to the W3S sensor was slightly higher than that
of chicken-based ready-to-eat meal J 5, possibly attributed to the limited
production of ammonia and hydrocarbons resulting from protein degra-
dation in beef.
Principal component analysis (PCA) was performed on the electronic
nose response values of the 32 ready-to-eat meals. The PCA results are
s h o w ni nF i g .1g. The ﬁrst principal component (PC1) accounted for 59.8%
of the variance, while the second principal component (PC2) explained
26.6% of the variance. Together, thesetwo components contributed 86.4%,
effectively capturing the volatileﬂavor information of nearly all samples and
illustratingﬂavor distinctions among the various ready-to-eat meals. Beef-
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

based ready-to-eat meal N1, pork-based ready-to-eat meals Z5 and Z11
were positioned on the positive half axis of PC1, displaying signi ﬁcant
positive correlations with sensorsW2S, W1W, W1S, and W5S. The volatile
ﬂavors of these products consist primarily of alcohols, aldehydes, ketones,
sulﬁdes, hydrocarbons, and nitrogen oxides. Pork-based ready-to-eat meals
Z8 and Z4, as well as beef-based ready-to-eat meal N4, were positioned in
the negative half of PC1 and exhibited close associations with sensors W6S
and W3S, suggesting a reliance on hydrogen and long-chain hydrocarbons
for theirﬂavor proﬁles. Various ready-to-eat meals occupied distinct regions
within the PCA space, with chicken-based ready-to-eat meals (e.g., J1 and
J5) predominantly clustered near the central axis of PC1, pork-based ready-
to-eat meals (e.g., Z5 and Z8) displaying a wide distribution range, and beef-
based ready-to-eat meals (e.g., N1 and N4) demonstrating polarization. The
PCA of the electronic nose effectively distinguished the three major types of
products: chicken, pork, and beef. The differences primarily arose from the
extent of fat oxidation in the raw meat, the types of spices incorporated in the
processing techniques, and variationsin the intensity of chemical reactions
like the Maillard reaction and lipid degradation during thermal processing.
The electronic tongue analysis indicated signiﬁcant variations in the
taste proﬁles of chicken-, pork-, and beef-b ased ready-to-eat meals. The
analysis in Fig. 1d–f demonstrated that sourness and umami exhibited the
most pronounced response intensity in the overall taste (P < 0.05). Samples
Z5, N6, and Z9 showed relatively high response values to sour taste. This
aligns with the typical preparation methods of such products, which fre-
quently incorporate acidic season ings like vinegar and tomato sauce.
Moreover, both Z9 and Z5 displayed noticeable umami characteristics. This
suggests a higher content of free amino acids (e.g., glutamic acid and aspartic
acid) in the raw meat or the addition of umami-rich ﬂavorings (e.g., soy
sauce and monosodium glutamate) during processing. The response values
of J5 in bitterness and its aftertaste channels differed signiﬁcantly from those
of other ready-to-eat meals ( P < 0.05), and the aftertaste response of
astringency exhibited a similar trend. This difference likely related to the
bitter components present in the speci ﬁc spices used during the J5 pre-
paration, such as pepper and star anise,or to the partial protein degradation
products resulting from prolonged stewing. In contrast, taste indicators such
as richness and astringency did not demonstrate systematic differences
Table 2 | Results of essential nutrient determination in 32 ready-to-eat meals
Abbreviation Protein (g/100 g) Fat (g/100 g) Moisture (g/100 g) Ash (g/100 g) Carbohydrates
(g/100 g)
Sodium (mg/100 g)
J1 5.36 ± 0.23Ag 8.97 ± 0.27Aef 72.09 ± 0.35 Be 2.14 ± 0.08 Ab 11.16 ± 0.17ABb 783.50 ± 5.38Ab
J2 4.65 ± 0.28 Ah 14.25 ± 0.31Ab 72.60 ± 0.42 Be 1.52 ± 0.06 Ag 6.46 ± 0.23ABf 477.44 ± 4.88Ak
J3 15.32 ± 0.35Aa 2.27 ± 0.36 Ah 76.15 ± 0.39 Bd 2.17 ± 0.07 Ac 3.86 ± 0.07ABgh 734.11 ± 4.22Ad
J4 7.80 ± 0.59Ae 8.68 ± 0.61Af 70.52 ± 0.72 Bf 2.61 ± 0.11 Aa 10.13 ± 0.67ABc 829.80 ± 5.55Aa
J5 2.85 ± 0.11Ai 12.29 ± 0.28Ac 79.05 ± 0.33 Bb 1.42 ± 0.05 Af 3.88 ± 0.28ABgh 568.92 ± 5.04Ai
J6 13.47 ± 0.11Ab 18.46 ± 0.40Aa 63.16 ± 0.38 Bh 2.08 ± 0.09 Ac 2.64 ± 0.20ABi 701.90 ± 2.14Ae
J7 12.63 ± 0.25Ac 11.63 ± 0.24Ad 70.13 ± 0.36 Bf 2.02 ± 0.08 Ad 3.45 ± 0.39ABh 646.66 ± 5.90Af
J8 5.62 ± 0.34Ag 18.90 ± 0.35Aa 66.11 ± 0.41 Bg 1.25 ± 0.06 Ah 7.40 ± 0.21ABe 406.34 ± 3.16Al
J9 4.10 ± 0.08 Ah 9.26 ± 0.06Ae 77.04 ± 0.22 Bc 2.10 ± 0.05 Ad 7.32 ± 0.07ABe 636.04 ± 5.79Ag
J10 4.52 ± 0.41 Ah 11.18 ± 0.14Ad 72.55 ± 0.52 Be 1.90 ± 0.09 Ae 9.56 ± 0.47ABd 580.95 ± 3.34 Ah
J11 10.44 ± 0.33Ad 2.72 ± 0.09 Ah 80.07 ± 0.38 Ba 2.31 ± 0.07 Ab 4.45 ± 0.30ABg 747.23 ± 5.96Ac
J12 7.22 ± 0.09Af 7.29 ± 0.08Ag 71.39 ± 0.45 Be 1.79 ± 0.06 Af 11.82 ± 0.39ABa 545.98 ± 5.08Aj
N1 3.71 ± 0.07Af 16.84 ± 0.33Aa 73.21 ± 0.39 Ae 2.30 ± 0.07 Ab 3.65 ± 0.14Bd 749.86 ± 6.81Ab
N2 11.50 ± 0.06Aa 7.41 ± 0.17Ad 73.65 ± 0.31 Ae 1.70 ± 0.05 Ad 5.44 ± 0.28Bc 466.66 ± 4.01Ae
N3 11.58 ± 0.25Aa 9.05 ± 0.15Ac 74.44 ± 0.37 Ad 2.20 ± 0.08 Ac 2.43 ± 0.29Be 671.23 ± 2.92Ad
N4 5.28 ± 0.03Ae 6.44 ± 0.18Ae 77.58 ± 0.32 Ac 2.78 ± 0.09 Aa 7.52 ± 0.13Bb 1025.28 ± 5.45Aa
N5 5.87 ± 0.32Ad 12.77 ± 0.60Ab 74.60 ± 0.51 Ae 1.59 ± 0.08 Ae 5.57 ± 0.33Bc 427.66 ± 3.95Af
N6 7.47 ± 0.23Ab 4.16 ± 0.14Ag 72.62 ± 0.36 Af 2.29 ± 0.07 Ab 13.32 ± 0.28Ba 746.37 ± 5.42Ab
N7 5.43 ± 0.08Ae 2.56 ± 0.11 Ah 82.48 ± 0.30 Aa 1.48 ± 0.04 Af 7.54 ± 0.11Bb 403.66 ± 3.72Ag
N8 6.40 ± 0.07Ac 5.15 ± 0.19Af 80.76 ± 0.28 Ab 2.20 ± 0.06 Ac 5.39 ± 0.09Bc 701.29 ± 1.23Ac
Z1 9.22 ± 0.12Be 32.58 ± 2.56Ba 46.40 ± 0.68 Ch 2.21 ± 0.13 Ad 9.21 ± 0.12Ad 731.85 ± 3.39Ae
Z2 7.65 ± 0.42Bf 13.62 ± 0.16Be 71.01 ± 0.51 Cb 2.10 ± 0.09 Ae 5.58 ± 0.28Ag 645.45 ± 3.73Af
Z3 2.95 ± 0.17Bi 18.45 ± 0.41Bc 71.96 ± 0.47 Ca 1.21 ± 0.05 Al 5.32 ± 0.20Ag 329.18 ± 5.27Ak
Z4 8.95 ± 0.19Be 15.42 ± 0.40Bd 63.34 ± 0.52 Ce 1.62 ± 0.07 Ah 10.24 ± 0.15Ac 446.59 ± 4.32Ai
Z5 4.72 ± 0.37Bh 18.42 ± 1.20Bc 69.72 ± 0.28 Cc 1.81 ± 0.10 Af 5.51 ± 0.12Ag 546.71 ± 3.11Ag
Z6 5.65 ± 0.27Bg 22.89 ± 0.68Bb 64.55 ± 0.75 Ce 1.36 ± 0.09 Ak 5.55 ± 0.45Ag 383.56 ± 4.23Aj
Z7 14.26 ± 1.09Ba 18.08 ± 0.54Bc 58.66 ± 1.22 Cg 2.74 ± 0.15 Ab 6.32 ± 0.13Af 951.86 ± 8.09Ab
Z8 11.41 ± 1.13Bd 8.36 ± 0.54Bg 65.60 ± 1.27 Cd 1.68 ± 0.11 Ag 12.96 ± 0.61Aa 452.90 ± 3.13Ai
Z9 12.55 ± 0.39Bc 19.43 ± 0.62Bc 60.36 ± 0.70 Cf 2.60 ± 0.12 Ac 5.26 ± 0.37Ag 898.15 ± 4.65Ad
Z10 13.19 ± 1.53Bbc 10.27 ± 0.71Bh 66.02 ± 1.64 Cd 2.89 ± 0.18 Aa 7.60 ± 0.59Ae 1235.14 ± 4.22Aa
Z11 13.62 ± 0.07Bab 7.38 ± 0.29Bg 63.15 ± 0.57 Ce 2.72 ± 0.10 Ab 12.65 ± 0.51Aa 924.39 ± 4.51Ac
Z12 13.32 ± 0.29Bbc 7.24 ± 0.45Bg 66.39 ± 0.58 Cd 1.73 ± 0.09 Ag 11.13 ± 0.64Ab 469.15 ± 3.52 Ah
For protein, fat, moisture, ash, and carbohydrates, percentage values are equivalent to g/100 g edible portion. Different lowercase letters within the same column indicate signi ﬁcant differences within
groups (P < 0.05). Different uppercase letters within the same column indicate signi ﬁcant differences between groups ( P < 0.05).
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

among various ready-to-eat meals, suggesting that these indicators were less
inﬂu e n c e db yt h et y p eo fr a wm e a ta n dm o r er e l i a n to nt h es e a s o n i n ga n d
cooking methods employed in speciﬁc recipes.
The PCA results are shown in Fig.1h. The two principal components,
PC1 and PC2, explained 83.6% of the total variance (PC1 = 65.4%, PC2 =
18.2%), effectively capturing the tas te characteristic information of the
sample. This ﬁnding provided an objective basis for evaluating the taste
quality of various ready-to-eat meals. Speciﬁcally, PC1 exhibited a positive
correlation with bitterness, saltiness, astringency, aftertaste astringency,
aftertaste bitterness, intensity, and umami, while showing a negative cor-
relation with sourness. PC2 exhibited positive correlations with sourness,
astringency, astringency aftertaste, and saltiness, while showing negative
correlations with umami, richness, bitterness, and bitter aftertaste. Spatially,
samples like Z11, J10, and N2 clustered along the negative axis of PC2,
Fig. 1 | Electronic nose and electronic tongue analysis results for 32 ready-to-eat meals. a –c Show the electronic nose responses of chicken, pork, and beef ready-to-eat
meals, respectively. d–f Show the electronic tongue responses of chicken, pork, and beef ready-to-eat meals, respectively. g, h Show the principal component analysis results
of the electronic nose and electronic tongue analyses, respectively.
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

aligning with umami attributes, indicating umami as a de ﬁning taste
characteristic. Conversely, samples such as J4, Z1, and J7 concentrated in the
positive axis of PC2, reﬂecting heightened acidity responses, consistent with
the prevalent use of acidic seasonings.Notably, chicken-based ready-to-eat
meal J5, distinguished by pronounced bitterness and bitter aftertaste,
positioned distinctly below the negative axis of PC1, segregating it from
other ready-to-eat meals.
GC-MS analysis results of 32 ready-to-eat meals
A total of 77 volatileﬂavor compounds, including 19 aldehydes, 9 alcohols, 6
ketones, 8 esters, 25 alkenes, and 10 other compounds, were identiﬁed in 32
commercially available ready-to- eat meals using HS-SPME/GC-MS.
Detailed information is provided in Tables S2–S4. Signiﬁcant variations in
compound levels were observed among the samples (P < 0.05), which aligns
with the ﬁndings of Shen et al. 32 that differences in volatile ﬂavors are
primarily inﬂuenced by the type of raw meat, processing techniques, and
seasoning additives. Figure 2a shows the hierarchical clustering and heat
map visualization of volatile com p o u n d si nr e a d y - t o - e a tm e a l s(n = 32). The
content and types of volatile compounds are shown in Fig.2b.
Aldehyde compounds, due to their low odor threshold, were identiﬁed
as the core components contributing to the characteristicﬂavor of ready-to-
eat meals. To further evaluate the key ﬂavor-active compounds, the odor
activity value (OAV) was calculated using the formula: OAV = C/T, where
C is the measured concentration of the compound (μg/kg), and T is the odor
threshold in water (μg/kg) retrieved from the literature. A total of 22 volatile
compounds achieved an OAV≥ 1 across speciﬁc ready-to-eat meal matri-
ces, supporting their roles as important ﬂavor contributors. These key
contributors showed substantial maximum OAVs, such as 18.7 for hexanal,
187.6 for (E,E)-2,4-decadienal, 42.1 for benzaldehyde, and 35.2 for linalool.
The continuous variations and clustering patterns of z-score-transformed
OAVs for these 22 coreﬂavor-contributing compounds across the 32 ready-
to-eat meals are further illustrated in Fig. 2c. These results indicate that
aldehydes and spice-derived terpenes are major contributors toﬂavor dif-
ferentiation. Theseﬂavor-active compounds, which were formed primarily
through the oxidative degradation of unsaturated fatty acids33 in raw meat
and the Strecker degradation of amino acids, exhibited distinct product-
speciﬁc distributions. For instance, the benzaldehyde content in sample Z9
reached 847.02 ± 36.13μg/kg, signiﬁcantly exceeding that of other samples;
the content of (E)-3,7-dimethyl-2,6-octadienal in sample Z6 measured
1373.5 ± 116.69μg/kg, which was speculated to relate to the oxidation of
unsaturated fatty acids in auxiliary ingredients such as sweet peppers. The
content of (E,E)-2,4-decadienal in sample Z9 was as high as
2551.42 ± 23.67μg/kg, which is a key marker compound for the “rich fat
aroma” of pork-based ready-to-eat me als, formed through the auto-
oxidation of linoleic acid. For n-hexanal, the highest content was detected in
pork sample Z9 (470.2 ± 7.63 μg/kg), followed by chicken sample J4
(380.58 ± 5.89μg/kg) and beef sample N2 (104.48 ± 7.31 μg/kg). This
compound, mainly gener ated through lipid oxidation, contributes to a
characteristic grassy aroma and was particularly abundant in Z9 and J4. The
concentrations of pentanal and 4-isopropylbenzaldehyde in beef-based
ready-to-eat meals were signi ﬁcantly higher than those in chicken- and
pork-based ready-to-eat meals, which may be attributed to the higher
proportion of saturated fatty acids in beef and the unique fat oxidation
pathway during thermal processing, consistent with the research results of
Dinh et al.34 on beef ﬂavor substances.
Alcohol compounds in the samples mainly originated from fat oxi-
dation and spice additives35. Among them, eucalyptol, 2,3-butanediol, n-
hexanol, and 1-octen-3-ol showed signiﬁcantly higher levels compared to
other alcohol compounds (P < 0.05). Speciﬁcally, Z6 recorded the highest
eucalyptol content at 281.52 ± 4.26μg/kg; sample J4 had the highest levels of
n-hexanol (544.32 ± 54.18 μg/kg) and 2,3-butanediol
(253818.07 ± 226.56μg/kg). The 1-octen-3-ol content in sample Z10 was
136.56 ± 5.25μg/kg, which is a key ﬂavor compound of pork, potentially
linked to the gradual oxidation of p ork knuckle fat during prolonged
stewing. For terpene alcohols from spices, sample N3 exhibited the highest
linalool content of 5838.18 ± 237.31μg/kg, while sample Z8 contained the
highest α-terpineol content at 581.26 ± 29.34μg/kg; these two compounds
mainly originate from spices such as star anise and cinnamon.
Although ketones and esters have lower concentrations compared to
aldehydes and alcohols, they play a crucial role in enhancing the ﬂavor
complexity ofthe products36. Ketone compounds primarily arise from lipid
oxidation, the Maillard reaction, and amino acid degradation37. The highest
content of methyl heptenone was found in sample J6, reaching
298.67 ± 7.74μg/kg; phenylbutanone was most abundant in pork sample
Z10 (143.75 ± 3.18μg/kg), followed by chicken sample J4 (79.26 ± 0.08μg/
kg), which may be attributed to variations in amino acid content among
different raw meats and differences in thermal processing temperatures38.
Sample J1 had the highest 3-heptanone content at 6.73 ± 0.17μg/kg.
For ester compounds, the levels of dimethyl phthalate, ethyl palmitate,
and terpinyl acetate were signiﬁcantly higher than other ester components
(P < 0.05). Speci ﬁcally, dimethyl phthalate content in J4 measured
617.80 ± 33.77μg/kg, ethyl palmitate content in Z5 peaked at
70.12 ± 2.37μg/kg, and terpinyl acetate content in Z8 reached the highest
level at 189.72 ± 15.78μg/kg. Ester compounds are mainly formed by the
esteriﬁcation of organic acids with alcohols39, and their higher content in
pork-based ready-to-eat meals is related to the abundant fatty acids in pork
raw materials and the wide use of acidic seasonings in processing39.
Alkenes and sulfur-containing compounds are the key characteristic
ﬂavor components of speci ﬁc products. The zingiberene content in J6
reached 1523.55 ± 71.34μg/kg, which originates from ginger and is the core
material of the “ginger aroma ” in J6 40. Z12 exhibited the highest
β-bisabolene content at 496.40 ± 34.98μg/kg, while sample Z8 contained
743.63 ± 49.76μg/kg of (D)-limonene, which mainly comes from spices like
dried tangerine peel and imparts a refreshing“citrus aroma” to the products.
Among phenolic ether compounds, sample Z12 exhibited signiﬁcant
levels of eugenol (18406.77 ± 493.23 μg/kg) and anethole
(45758.83 ± 3585.78μg/kg), both originating from cloves and fennel.
Sample J7 contained 224.53 ± 13.46 μg/kg of diallyl trisul ﬁde, a sulfur-
containing compound derived from garlic with a typical “garlic aroma”,
which is consistent with the ﬁndings by Qiao et al. (2025) 41 that sulfur-
containing compounds are the pivotalﬂavor components in garlic-infused
ready-to-eat products.
Transformer-driven intelligent synchronous evaluation
of ﬂavor chemistry characteristics and nutritional
quality
Feature extraction, nutrient estimation andﬂavor identiﬁcation
Based on the systematic characterization of ﬂavor chemistry proﬁles and
nutritional quality of ready-to-eat meals, this study constructed a multi-
modal Transformer deep learning fr amework to achieve rapid, non-
destructive synchronous evaluation of productﬂavor attributes and nutri-
tional quality solely from images, which provides a novel technical approach
for the application of artiﬁcial intelligence in theﬁeld ofﬂavor chemistry and
intelligent food quality control.
Industrialized ready-to-eat meals exhibited signiﬁcant variations in
shape due to diverse cooking methods, including braising, deep-frying, and
stewing, and often featured multiple ingredients stacked together42.S h a o
et al.43 noted that such complex forms were likely to induce systematic biases
in traditional nutrition prediction models. The Transformer, with its self-
attention mechanism and hierarchica l feature extraction capabilities,
effectively captured multi-scale features that ranged from local textures to
global forms10. It adapted to the morphological diversity of industrialized
products and provided a robust basis f or nutritional prediction through
feature representation. This observation is consistent with recent studies
suggesting that algorithms speciﬁcally optimized for food-related tasks may
provide advantages over generic image analysis models21. The hierarchical
feature extraction capability of Transformers allows the model to simulta-
neously capture low-level visual features (e.g., color, texture) and high-level
semantic features (e.g., ingredient distribution, cooking degree), which is
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

critical for correlating visual appearance with both nutritional composition
and ﬂavor characteristics19.
In this study, the deep features extracted by the Transformer archi-
tecture, after dimensionality reduction via t-distributed stochastic neighbor
embedding (t-SNE), exhibited a distinct multi-cluster distribution in the
two-dimensional space. Figure3b shows that each ready-to-eat meal variant
is represented by a unique color, displaying relatively independent and
clearly delineated clusters in the feature space. This observation suggests that
the model effectively captured distinctive features among different products,
achieving high intra-class similarity and inter-class variation. Nonetheless,
there was some overlap among certai n products (e.g., J9, J10, and J11),
indicating potential similarities in the feature space and introducing
Fig. 2 | a Presents the hierarchical cluster analysis
and heatmap visualization of volatile compounds in
ready-to-eat meals ( n = 32). b Shows the content
and types of volatile compounds. c Presents the
heatmap visualization of z-score-transformed odor
activity values (OAVs) for 22 key odor-active com-
pounds across the 32 ready-to-eat meals.
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

uncertainty in classifying boundary samples. The overall distribution
demonstrated a “multi-centered and decentralized” pattern, highlighting
the diversity and speciﬁcity of the feature space and afﬁrming the model’s
reliability in estimating nutritional content.
The accuracy of nutrient component estimation was closely associated
with the model’s feature extraction capability44,45. The estimation results of
this model remained highly consistent with the measured physical and
chemical data. This result further supports the existence of meaningful
correlations among visual features, physicochemical properties, and nutri-
tional content.
Nutritional identiﬁcation involved a quantit ative mapping process
based on the physical and chemical laws of products. The results indicated a
high level of consistency among the three methods in estimating protein
content, demonstrating the effectiveness and stability of the model’so u t p u t
probability vector in inferring nutritional indicators. The model accuracy is
s h o w ni nF i g .S 2 .T h eo v e r a l lﬁndings revealed that the model not only
achieved precise product classiﬁcation, with an accuracy of 91.5% ± 1.2%,
but also yielded nutritional estimation results that were highly correlated
with physicochemical measurements, withR2 values of 0.86 for protein, 0.80
for fat, and 0.79 for carbohydrate.
The image recognition results are shown in Fig. 3c. The average fat
content of pork-based ready-to-eat meals exceeded that of chicken and beef,
with the model estimati ng higher fat values for them accordingly 46.T h e
deviation was minimal in high-fat samples like Z1 and Z2. Additionally, the
model could distinguish features of elevated carbohydrate content in pro-
ducts containing starchy side products like potatoes and lotus roots, as
evidenced by signiﬁcantly higher estimated values for J2 and N6 compared
to J3 products lacking starchy sides. Furthermore, the model demonstrated
the capability to identifyﬂavor descriptors accurately, capturing the distinct
ﬂavors of various products. For example, the J4 sample was labeled as
“spicy” because of its pronounced pungentﬂavor proﬁle, aligning with the
strong response of the W1W sensor in the electronic nose analysis to sulﬁde
and pyrazine compounds. The J6 sample was characterized by a “ginger
ﬂavor” label attributed to its zingiberene content of 1523.55 ± 71.34μg/kg.
Samples J1 and Z2 were labeled as “sweet and sour” due to their elevated
levels of acidic seasonings. These ﬂavor assignments were generally con-
sistent with the distribution patterns of the volatile compounds identiﬁed by
GC-MS analysis. The nutritional identiﬁcation results of the 32 products are
s h o w ni nT a b l e3.
External validation on the test set
To assess the model ’s generalizability and robustness in real-world sce-
narios, external validation was performed on the independent strati ﬁed
group test set (20% of the dataset, 384 images). For the classiﬁcation function
(distinguishing among 32 ready-to-eat meal variants), the model achieved
an accuracy of 91.5% ± 1.2%, with precision, recall, and F1-score averaging
0.92, 0.91, and 0.91, respectively. The confusion matrix showed that most
predictions were located on the diagona l, indicating generally stable dis-
crimination among the 32 ready-to-eat meal products. The remaining off-
diagonal errors were mainly concentrated among visually similar boundary
products rather than being evenly distributed across all classes. Repre-
sentative confusion occurred among samples with similar sauce color,
surface gloss, meat-cut morphology, and side-ingredient distribution, such
as J9, J10, and J11. These samples also showed partial overlaps in the t-SNE
feature space, suggesting that the misclassi ﬁcations were associated with
genuine visual similarity rather than random model failure. At the broader
meat-type level, the model maintained stable discriminative performance,
with classiﬁcation accuracies of 92.3% for pork, 91.0% for chicken, and
90.8% for beef.
For the nutritional regression task, predictions generated by the direct
nutrient-regression head were compared against the ground-truth physi-
cochemical measurements. The model yieldedR2 values of 0.86 for protein,
0.80 for fat, and 0.79 for carbohydrate, with mean absolute errors (MAEs) of
1.2 g/100 g, 1.5 g/100 g, and 1.47 g/100 g, respectively. The corresponding
root mean squared errors (RMSEs) were 1.5 g/100 g for protein, 2.0 g/100 g
Fig. 3 | a Illustrates the architecture of the Transformer-based model. b Presents the
t-SNE visualization of validation features for 32 ready-to-eat meals. c Shows the
image recognition results and Grad-CAM visualizations of 32 ready-to-eat meals
using the Transformer model.
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

for fat, and 1.93 g/100 g for carbohydrate. From an industrial perspective,
the observed MAEs of 1.2–1.5 g/100 g and RMSEs of 1.5–2.0 g/100 g indi-
cate that the proposed system can prov ide approximate nutritional esti-
mates with relatively limited abso lute deviations, supporting rapid
screening, batch-to-batch comparison, and preliminary quality control of
ready-to-eat meals. However, these error ranges should not be interpreted as
sufﬁcient for regulatory nutrition labeling or as a replacement for standar-
dized physicochemical measurements. Conﬁrmatory laboratory analysis
remains necessary when highly precise quantitative values are required.
These results indicate high predictiveconsistency, with deviations primarily
occurring in products with high variability in side ingredients (e.g., starchy
additions affecting carbohydrate estimates). The HM method showed the
highest robustness (lowest sensitivity to outliers), conﬁrming its utility for
mixed or anomalous samples.
Because carbohydrate estimation showed the largest baseline error
among the three macronutrients, the carbohydrate branch was further
optimized using weighted loss functions. Among the four loss settings,
Weighted-Huber ( λcarb = 1.50, δ = 1.00 g/100 g) achieved the best
validation performance under the predeﬁned model-selection criteria and
was therefore selected for ﬁnal evaluation on the held-out test set. On the
held-out test set, carbohydrate R2 increased from 0.720 to 0.793, MAE
decreased from 1.80 to 1.47 g/100 g, and RMSE decreased from 2.31 to
1.93 g/100 g, while classiﬁcation accuracy (91.50%), proteinR2 (0.860), and
fat R2 (0.799) remained essentially unchanged. Across ﬁve independent
runs, carbohydrateR2, MAE, and RMSE were 0.793 ± 0.003, 1.47 ± 0.02 g/
100 g, and 1.93 ± 0.02 g/100 g, respectively. The detailed comparison is
provided in Supplementary Table S11 and Fig.4.
Error stratiﬁcation further showed that starchy side dishes and thick-
ened sauces/soups were major sources of carbohydrate-prediction uncer-
tainty. Relative to the baseline model, the optimized model reduced MAE by
10.93% for normal meals, 26.56% for meals containing starchy side dishes,
and 28.58% for meals containing thickened sauces/soups. Samples con-
taining both starch-rich side dishes and thickened sauces remained the most
difﬁcult subgroup, with only a 7.85% MAE reduction and a residual MAE of
2.80 g/100 g. Starchy side dishes were deﬁned only when ingredient infor-
mation conﬁrmed discrete starch-rich ingredients such as potato or lotus
root, whereas thickened sauce/soup status was assigned only when the
ingredient label or production formu lation explicitly listed a starch or
thickening agent. The subgroup results are summarized in Supplementary
Table S12.
To evaluate the effectiveness of theproposed Transformer-based fra-
mework, a comparative analysis was conducted against several widely used
deep learning architectures, including ResNet-50, Ef ﬁcientNet-B0, and
Vision Transformer Base (ViT-Base), which are commonly used in image
classiﬁcation and nutrition estimation tasks. All models were trained and
evaluated using the same dataset, data split strategy, preprocessing proce-
dures, and evaluation metrics to ensure a fair comparison. The comparative
results are summarized in Table4.
The table illustrates that our model outperforms CNN baselines (e.g.,
ResNet-50 and Ef ﬁcientNet-B0) by 2 –3% in classi ﬁcation accuracy and
0.05–0.11 in R2 values, attributable to the Transformer ’s self-attention
mechanism, which captures long-range dependencies and global contexts
more effectively than local convolutions in CNNs. Although the classiﬁca-
tion accuracy of the proposed framework was slightly lower than that of the
standard ViT-Base model, it achieved consistently superior performance in
nutritional prediction tasks, yielding higherR2 values for protein, fat, and
carbohydrate estimation. This improvement can be attributed to the inte-
gration of physicochemical correlati ons, multimodal information, and
weighted algorithms, which mitigated classi ﬁcation uncertainty and
improved nutritional prediction. These advantages are particularly evident
in complex ready-to-eat meals with variable textures and ingredients, where
CNNs struggle with hierarchical feature extraction 10.H o w e v e r ,m i n o r
limitations include sensitivity to i mage overlaps in boundary cases, sug-
gesting potential enhancements via ensemble methods or larger datasets in
future work.
Practical deployment also requires consideration of model complexity,
training cost, and inference efﬁciency. The computationally intensive stage
of the proposed framework is ofﬂine model training, during which the ViT-
style Transformer encoder, physicochemical feature branch,ﬂavor feature
branch, and cross-attention fusion module learn the associations among
standardized product images, ph ysicochemical indicators, and ﬂavor
chemistry proﬁles. In the present implementation, the image branch uses
16 × 16 image patches, 768-dimensional embeddings, and 12 Transformer
encoder layers, while the physicochemical and ﬂavor branches use light-
weight fully connected encoders. Training was performed with a batch size
of 32 for a maximum of 50 epochs with early stopping, using AdamW
optimization, learning-rate warmup, and cosine decay. Thus, the major
computational cost is borne during model development and calibration
rather than during routine product scr eening. After training, practical
inference requires standardized image acquisition, image preprocessing,
and one forward pass through the trained network. This work ﬂow is
compatible with centrali zed-kitchen quality-control settings in which
imaging conditions can be ﬁxed. A limitation of the present study is that
Table 3 | Nutritional identi ﬁcation results of 32 ready-to-
eat meals
Abbreviation Protein
(g/
100 g)
Fat
(g/100 g)
Carbohydrates
(g/100 g)
Sodium
(mg/
100 g)
Energy
(kcal/
100 g)
J1 5 8 10 710 132.0
J2 5 13 6 435 161.0
J3 14 2 3 665 86.0
J4 8 9 10 755 153.0
J5 3 11 4 515 127.0
J6 13 17 3 635 217.0
J7 12 12 3 585 168.0
J8 6 18 7 370 214.0
J9 4 9 7 575 125.0
J10 5 11 9 525 155.0
J11 10 3 4 675 83.0
J12 7 7 11 495 135.0
N1 4 16 3 675 172.0
N2 11 7 5 425 127.0
N3 12 9 2 610 137.0
N4 5 6 7 930 102.0
N5 6 12 5 385 152.0
N6 7 4 12 675 112.0
N7 5 3 7 365 75.0
N8 6 5 5 635 89.0
Z1 9 30 9 665 342.0
Z2 8 13 5 585 169.0
Z3 3 18 5 300 194.0
Z4 9 15 10 405 211.0
Z5 5 18 5 495 202.0
Z6 6 22 5 348 242.0
Z7 14 17 6 865 233.0
Z8 11 8 12 410 164.0
Z9 12 19 5 815 239.0
Z10 13 10 7 1125 170.0
Z11 13 7 12 835 163.0
Z12 13 7 10 425 155.0
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

image acquisition was performed under standardized lighting conditions;
therefore, the robustness of the model under complex real-world illumi-
nation and severe occlusion has not yet been directly evaluated. Although
random brightness and contrast augmentation were applied during training
to simulate moderate environmental ﬂuctuations, this cannot fully repro-
duce uncontrolled real-world imaging conditions. For future industrial
deployment, a lightweight preprocessing pipeline could include automatic
white balance and color correction, image resizing, simple brightness/con-
trast normalization, and image-quality screening to identify severely
underexposed, overexposed, or occluding images before model inference.
Images that do not meet the prede ﬁned quality requirements could be
required. Future studies will further evaluate the proposed framework under
diverse lighting and occlusion conditions. Nevertheless, the current model
should be regarded as a decision-support tool for product comparison and
quality screening for the ready-to-ea t meal products investigated in this
study, rather than a complete replacement for reference physicochemical or
ﬂavor-chemistry analyses. The present lightweight experiments quantify
real-time inference on a desktop GPU and Jetson Orin Nano, while inde-
pendent production batches and longer-term ﬁeld deployment remain
necessary to assess operational robustness.
A dedicated lightweight experiment was therefore performed using
structured FFN-channel pruning followed by post-training quantization.
The 30% pruned INT8 con ﬁguration reduced model size from 366.84 to
72.32 MB (80.29% reduction) and reduced Jetson Orin Nano latency from
67.48 to 22.92 ms, corresponding to a 2.94-fold speed-up. Classi ﬁcation
accuracy decreased only from 91.50%to 90.85% (0.65 percentage points),
while the protein, fat, and carbohydrateR2 values remained 0.849, 0.788, and
0.775, respectively. Model-complexity and predictive-performance results
are reported in Supplementary Table S13, and platform-speciﬁcl a t e n c y / F P S
results are given in Supplementary Table S14. The size-latency trade-off and
the embedded deployment workﬂow are shown in Figs. 5 and 6.
To facilitate a clearer understandingo ft h ep o t e n t i a la p p l i c a t i o n so ft h e
proposed framework by the intended institutions and end users, its practical
use can be described in terms of two application scenarios. In centralized
kitchens or ready-to-eat meal enterprises, standardized meal images could
be acquired under controlled imaging conditions and analyzed using the
trained model to obtain product classi ﬁcation results, estimated macro-
nutrient contents, and ﬂavor-related information. These outputs could
assist production, quality-control, and product-development personnel in
product comparison, batch screening, preliminary quality assessment, and
formulation optimization. For future consumer-oriented applications, after
further validation under real-world imaging conditions, consumers could
capture meal images to obtain estimates of macronutrient composition and
corresponding caloric content. On th is basis, by further incorporating
individual preferences regarding meat type andﬂavor characteristics, as well
as nutritional requirements, the system could provide personalized ready-
to-eat meal recommendations. The present framework primarily provides a
technical basis for these potential applications, and further validation is still
required before routine deployment in real-world settings.
To further evaluate the practical relevance of the model for consumer-
oriented applications, a consumer satisfaction survey was conducted with
the 100 participants from the sensory evaluation experiment. First, con-
sumers completed personalized pref erence questionnaires. The ques-
tionnaire included meat-type preferences (chicken, pork, and beef),ﬂavor
preferences (such as spicy, sweet and sour, and ginger), as well as speciﬁc
requirements regarding nutritional indicators and caloric content. This
preference information was then used by the model to generate personalized
product recommendations. Finally, consumers evaluated their satisfaction
with the recommended products. Consumer ratings of 1 to 3 were con-
sidered unsatisfactory, 4 to 6 moderately satisfactory, and 7 to 9 highly
satisfactory.
The survey results are shown in Fig. S3. The overall satisfaction score of
consumers for the model recommendations reaches 8.0 out of 9, which
Fig. 4 | Effect of weighted loss functions on carbo-
hydrate prediction, showing MAE, RMSE, and car-
bohydrate R2 for the baseline and three weighted-
loss conﬁgurations.
Table 4 | Comparative performance of the proposed Transformer-based framework and baseline models on the present ready-
to-eat meal dataset
Model Architecture Classi ﬁcation Accuracy (%) Protein R2 Fat R2 Carbohydrate R2
ResNet-50 CNN 88.7 0.75 0.7 0.65
EfﬁcientNet-B0 CNN 89.4 0.78 0.72 0.68
ViT-Base Transformer 92.3 0.82 0.76 0.7
Proposed Transformer-based framework Transformer 91.5 0.86 0.8 0.79
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

belongs to the very satisﬁed level. In the detail dimension, the satisfaction
score for recommended products is 7.5 p oints, the satisfaction score for
nutritional indicators is 7.52 points, the satisfaction score for calories is 7.05
points, and the satisfaction score forﬂavor is 7.84 points. All indicators are
within a very satisfactory range. It is worth noting that theﬂavor satisfaction
score reached a high of 7.84 points, which veriﬁes the effectiveness of the
model in identifying theﬂavor labels of products. The model can accurately
identify labels such as“spicy” in J4,“ginger” in J6, and“sweet and sour” in J1
and Z2. This precise ﬂavor recognition ability directly translates into a
satisfactory experience for consumers.
A limitation of the present study is that the samples were restricted to
frozen ready-to-eat meals; therefore, the generalizability of the model to
shelf-stable and refrigerated ready-to-eat products has not yet been estab-
lished. Although three independent acquisition batches were included in the
present sample collection to account for potential batch-to-batch variability,
the current validation was not designed as an independent batch-level
external validation. Future studies willtherefore include independent pro-
duction batches, additional brands, andshelf-stable and refrigerated ready-
to-eat products to further evaluate the generalizability and robustness of the
proposed framework.
To verify the effectiveness of the proposed multi-modal feature fusion
framework, a comparative experiment was conducted between the multi-
modal fusion model and the single vi sual modal ViT model. The results
showed that the multi-modal fusion model improved the product classiﬁ-
cation accuracy by 3.14 percentage points compared with the single-modal
model, and the coefﬁcient of determination (R2)f o rp r o t e i n ,f a t ,a n dc a r -
bohydrate content prediction increased by 0.077, 0.087, and 0.129, respec-
tively. This result demonstrates tha t the fusion of physicochemical and
ﬂavor modal features effectively compensates for the limitations of single
visual modal data, improving the model’s prediction accuracy and robust-
ness for complex ready-to-eat meal matrices. Our approach aligns with the
paradigm that effective data fusion is critical for decoding the multi-layered
complexity of food systems16. Speciﬁcally, the use of cross-attention to link
visual features with ﬂavor chemistry validates recent consensus that mul-
timodal deep learning surpasses unimodal methods inﬂavor analysis17.T h e
high predictive consistency of our model mirrors the success of other
Fig. 5 |Model-size and Jetson Orin Nano latency trade-off after structured pruning and FP16/INT8 quantization, with classiﬁcation accuracy retained for each conﬁguration.
Fig. 6 | Lightweight compression and embedded deployment framework from of ﬂine model optimization/pruning/quantization to online Jetson Orin Nano inference and
task outputs.
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

specialized Transformers, which rely on self-attention to accurately map
complex chemical inputs to sensory labels18. Similar to recent applications of
AI in food science, including food safety monitoring and fermentation
research19,20, our framework demonstrates the potential of data-driven
methods for food quality evaluation.
To extendﬂavor prediction from qualitative descriptors to quantitative
chemical targets, a leakage-controlled regression experiment was added for
key volatile compounds. GC-MS concentrations and OAV-derived vari-
ables were excluded from all model inputs for this task, and concentration
targets were log10(C + 1)-transformed during training. Among eight
representative odor-active compounds,R2 values ranged from 0.639 for 1-
octen-3-ol to 0.769 for benzaldehyd e; detailed compound-level MAE,
RMSE, log-MAE, and log-RMSE values are reported in Supplementary
Table S15. These results demonstratethat the multimodal framework can
recover quantitative information for chemically distinct volatile com-
pounds, although predictive difﬁculty varied with concentration range and
compound-speciﬁc sensory/chemical characteristics.
A modality ablation experiment was additionally conducted using the
visual branch, physicochemical branch, and a leakage-controlled ﬂavor-
sensor branch consisting only of 10 electronic-nose responses and 7
electronic-tongue indicators. The full multimodal conﬁguration achieved
the highest classi ﬁcation accuracy (91.50%), protein R2 (0.859), fat R2
(0.799), carbohydrateR2 (0.793), and mean volatile-compoundR2 (0.707).
Removing either the physicochemical or ﬂavor-sensor branch reduced
performance, while the visual-only model yielded 88.37% accuracy and a
mean volatile R2 of 0.515. The complete ablation results are presented in
Supplementary Table S16, quantitatively conﬁrming that each input branch
contributes complementary information.
This study established a multimo dal Transformer framework that
integrates macroscopic visual features with underlying ﬂavor chemistry
attributes. The model uses a cross-attention mechanism to establish a deep
correlation between food appearance characteristics and intrinsic ﬂavor
substances. It integrates surface color features (L*,a *,b *), electronic nose-
derived volatile proﬁles, electronic tongue-derived taste matrices, and HS-
SPME/GC-MS-resolved absolute concentrations of core odor-active com-
pounds. By learning these multidimensional data, the model establishes a
quantitative mapping between the macr oscopic visual characteristics of
ready-to-eat meals and their intrinsic ﬂavor chemistry and nutritional
composition.
For the newly added volatile-com pound regression and associated
ablation experiments, however, GC-MS concentrations and OAV values
were used strictly as output targets/analytical references and were excluded
f r o mt h ei n p u tf e a t u r es p a c e .T h eﬂavor-sensor branch for these experi-
ments therefore contained only the 10 electronic-nose and 7 electronic-
tongue variables, preventing direct target leakage from GC-MS-derived
information.
This fused framework demonstrates the potential to support industrial
manufacturing and product development through data driven evaluation.
At the production level, image-driv en evaluation may help centralized
kitchens complement conventional nutrient testing or reduce reliance on
time-consuming and destructive analyses during routine quality screening.
Beyond nutritional monitoring, the m odel can also provide preliminary
prediction of ﬂavor attributes, offering a supportive tool for ﬂavor quality
assessment under standardized imaging conditions, which remains chal-
lenging in industrial food production19. When combined with automated
imaging devices, the system could support batch level or near real time
screening of macronutrient indicators and key ﬂavor characteristics in
centralized kitchen settings, thereby contributing toﬂavor standardization
of ready-to-eat meals21. At the product development level, the quantitative
correlations between cross modal features and measured outcomes may
support formulation optimization and objective evaluation ofﬂavor mod-
iﬁcations. As technology matures, these outputs may also be adapted for
retail or personalized dietary monitoring applications. By enabling nutri-
tional estimation from meal images, this framework may provide a useful
tool for tracking dietary patterns in speciﬁc populations and may facilitate
future integration between mass produced ready-to-eat meals and indivi-
dualized dietary management systems.
Methods
Materials
To ensure sample representativeness, this study selected 32 industrially
produced ready-to-eat meals based on integrated sales data analysis from
leading Chinese e-commerce and lifestyle platforms (Dianping, Meituan,
Ele.me, Taobao, JD.com) over a 6- month reference window (June to
December 2024). The 32 products with the highest composite sales scores
(incorporating monthly sales volume, customer review counts, and
platform-speciﬁc popularity rankings) were chosen to represent main-
stream best-selling products.
To account for potential batch-to-batch variability and improve the
robustness of the subsequent experimental results, after obtaining ethical
approval in May 2025, three independently packaged commercial units of
each of the 32 products were procured per batch across three independent
acquisition batches. All procured samples had production dates after Feb-
ruary 2025, yielding a total of 288 sample units for the full study. Imme-
diately following procurement, all samples were transported via a
continuous full cold chain maintained at−18 °C, hermetically sealed, and
stored in a −80 °C ultra-low temperature freezer until the pre-treatment
stage, with rigorous safeguards implemented throughout the entire process
to prevent repeated freeze-thaw cyc les of the samples. Corresponding
product names, abbreviations, and ful l details (including manufacturer,
ingredient list, production date, and shelf life) are listed in Table 5 and
Table S5, respectively.
The samples were limited to frozen ready-to-eat meals, thereby
excluding shelf-stable r eady-to-eat products, re frigerated ready-to-eat
items, and raw meat items. We acknowledge that the selected products
are complex ready-to-eat meals. To ensurethe feasibility and interpretability
of nutrient prediction across these het erogeneous matrices, a strict stan-
dardized protocol was applied: for physicochemical andﬂavor detection, all
samples were homogenized into a uniform analytical state. For image
acquisition, the intact product after reheating was used for shooting under
standardized conditions. This approach controls for the variability intro-
duced by complex food assemblies and allows the models to correlate visual
features with the average nutritiona l composition of the overall matrix.
Finally, products were categorized by primary meat type into three groups:
pork, chicken, and beef. The details of the instruments and equipment used
in the experiments are provided in Table S6. Information on the key
reagents employed is listed in Table S7.
Sample preparation
The 32 products were reheated using the manufacturer-recommended
water-bath method to simulate typi cal consumer preparation and stan-
dardize sample conditions prior to analysis. Immediately after sampling, the
products were cooled to room temperature, rapidly frozen, and stored under
vacuum at−80 °C until further analysis. Such ultra-low temperature frozen
storage can ensure the stability of meatquality, volatiles, and lipids, so as to
maintain sample stability prior to instrumental detection47. We recognize
that frozen storage may alter volatile proﬁles. To mitigate this effect, storage
time at −80 °C was minimized (less than 48 h for all samples), and a single,
consistent freeze‑thaw cycle was strictly maintained for all downstream
analyses. Furthermore, for GC ‑MS analysis, samples were homogenized
directly from the frozen state before headspace extraction to limit volatile
loss during thawing. This protocol w as designed to enable synchronous
evaluation of multiple attributes from the same batch of standardized
samples.
Consumer sensory evaluation
The study was conducted in a sensory laboratory designed in accordance
with ISO 8589:2007. A consumer cohort comprising 100 individuals (58
women and 42 men), aged between 18 and 40 years, was recruited. Detailed
demographic characteristics are summarized in Table S8. All participants
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

possessed normal vision, had no history of food allergies or mental illness,
did not smoke, and female participants were not pregnant. To ensure a
consistent baseline state, evaluations were conducted after participants had
fasted and abstained from water for 1 h. Prior to the formal trial, all panelists
received standardized verbal and written instructions, including detailed
attribute deﬁnitions and a scale familiarization session, to ensure evaluation
accuracy and prevent subjective misinterpretation.
Samples (50 ± 0.5 g) were served on odorless, disposable white circular
plates (7 cm diameter), each coded with a random 3-digit number. Samples
were presented in a randomized and balanced order to ensure blind testing.
The sensory evaluations took place in individual sensory booths under
controlled conditions (temperature: 22 ± 1 °C, relative humidity: 50 ± 5%,
illumination: 500 lux). Evaluations were conducted in triplicate with 15-min
intervals. Panelists were instructed to cleanse their palates thoroughly using
puriﬁed water provided between samples48.
Participants assessed two primary metrics: (1) Purchase Intention (PI),
rated on a 9-point hedonic scale. To improve measurement accuracy, par-
ticipants were explicitly informed of the context: 1–4 points indicated low PI
(unlikely to purchase), 5–7 points indicated medium PI (likely to purchase),
and 8-9 points indicated high PI (very likely to purchase) 49. (2) Attribute
Importance, where participants rated the importance of aroma, taste, color,
and nutritional components on a 9-point scale (1–3: low importance; 4–6:
moderate; 7–9: high). Participants were guided to utilize the full scale range
by imagining real-life purchasing scenarios. Written informed consent was
obtained from all participants before participation, and all participants were
advised of their right to withdraw at any time without penalty50. The study
involving human participants was reviewed and approved by the Academic
Ethics Committee of Bohai University (approval No. 2025050501; date of
approval: May 5, 2025). The work was carried out in accordance with the
Declaration of Helsinki51.
Determination of pH and color parameters
The pH was measured using a calibrated pH meter (Five Easy Plus, Mettler
Toledo, Switzerland). The sample (20 g) was homogenized with 180 mL of
deionized water. The pH was measured after the mixture reached equili-
brium at an ambient temperature of 25 °C.
The surface color of the samples was measured using a CR-400
Chroma Meter (Konica Minolta Optical Co., Ltd). Based on the metho-
dology described by Ping et al.52 with minor modiﬁcations, the instrument
was calibrated against a standard white calibration plate before measure-
ment. The CR-400 employs a ﬁxed diffuse-illumination/0° viewing geo-
metry with the specular componen t included (SCI); therefore, SCI
Table 5 | Names and abbreviations of 32 ready-to-eat meals
Types of meat Product Name Abbreviation Descriptive English Name
Chicken ready-to-eat meals Sweet and sour chicken with pineapple J1 Deep-fried chicken chunks tossed in a sweet and tangy pineapple sauce
Stir-fried diced chicken with lotus root J2 Diced chicken quick-fried with crisp lotus root slices
Braised diced chicken in soy sauce J3 Chicken chunks slow-cooked in a savory soy-based sauce
Kung pao chicken J4 Spicy diced chicken stir-fried with peanuts, chili, and Sichuan peppercorns
Braised chicken with potatoes J5 Chicken chunks stewed with potatoes in a rich brown sauce
Chicken and mushroom stew J6 Slow-cooked chicken and wild mushrooms in a savory broth
Braised chicken in brown sauce J7 Chicken simmered in a caramelized soy sauce and spice mixture
Farmhouse-style chicken J8 Rustic braised chicken in a rich, savory homestyle sauce
Yu xiang shredded chicken J9 Shredded chicken in a classic Sichuan sweet, sour, and spicy garlic sauce
Slippery chicken slices in white sauce J10 Velvety chicken slices stir-fried in a mild, savory white sauce
Beijing style shredded chicken J11 Shredded chicken stir-fried in a sweet and savory fermented soybean paste
Chicken with wood ear & bamboo shoots J12 Stir-fried chicken with crunchy bamboo shoots and wood ear mushrooms
Pork ready-to-eat meals Stir-fried pork with chili peppers Z1 Sliced pork quick-fried with fresh spicy green chili peppers
Twice-cooked pork Z2 Sichuan-style boiled pork belly slices, stir-fried with spicy broad bean paste
Mu shu pork Z3 Stir-fried sliced pork with scrambled eggs and wood ear mushrooms
Pork and mushroom stir-fry Z4 Sliced pork stir-fried with savory edible mushrooms
Farmhouse stir-fried pork Z5 Rustic stir-fried pork slices with green chilies and garlic
Stir-fried pork with bell peppers Z6 Sliced pork sautéed with mild, crisp bell peppers
Stir-fried pork with bamboo shoots Z7 Pork slices quick-fried with tender bamboo shoots
Stir-fried pork with dried tofu Z8 Stir-fried pork strips mixed with ﬁrm, seasoned dried tofu slices
Hong shao rou Z9 Classic Chinese pork belly slow-braised in soy sauce and caramelized sugar
Braised pork hocks with soybeans Z10 Slow-stewed pork hocks with savory soybeans
Braised pork hocks Z11 Pork hocks slow-cooked in a traditional savory brown sauce
Red-braised pork hocks Z12 Pork hocks slowly braised to a reddish-brown color with soy sauce and sugar
Beef ready-to-eat meals Beef and carrot stew N1 Slow-cooked beef chunks simmered with sweet carrots
Beef curry N2 Tender beef pieces stewed in a rich, spiced curry sauce
Braised beef with bamboo shoots N3 Beef chunks braised in a savory sauce with crunchy bamboo shoots
Red-braised beef N4 Beef slowly stewed in a caramelized soy sauce and spice mixture
Clear-stewed beef with potatoes N5 Slow-cooked beef broth with tender potato chunks
Braised beef brisket with potatoes N6 Rich beef brisket chunks stewed with potatoes in a savory brown sauce
Spicy beef N7 Beef slices cooked in a ﬁery, chili-infused broth
Beef and vegetable hot pot N8 Sliced beef and assorted vegetables simmered in a savory broth
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

represents an inherent characteristic of the instrument’so p t i c a lg e o m e t r y
rather than a user-selectable measurement mode. Colorimetric values were
determined using the D65 standard illuminant. In the present study, the
measured L, a, and b * values were used as standardized instrumental
descriptors in the physicochemical feature branch of the multimodal model
rather than as direct surrogates for consumer visual perception. Visual
appearance and consumer perception were evaluated separately through the
image modality and consumer sensory evaluation, respectively. To mini-
mize environmental variation duringmeasurement, all measurements were
conducted under consistent indoor conditions, and the measuring aperture
was maintained perpendicular to and in full contact with the sample surface
to minimize interference from ambient light. After gently removing excess
surface moisture with ﬁlter paper, the lightness (L *), redness (a *), and
yellowness (b*) values were measured. Triplicate measurements were per-
formed at three positions near the center of each sample, and the mean
values were used for subsequent analysis.
Protein content determination
Protein content was determined using the Kjeldahl method as described by
Chang and Zhang 53, utilizing an automatic K jeldahl nitrogen analyzer
(K9840, Haineng, Jinan, China). The protein content was calculated based
on the titration volume of the sample (T s ,m L ) ,t h et i t r a t i o nv o l u m eo ft h e
blank (Tb, mL), the sample weight (ω, g), the concentration of the standard
HCl solution (0.1 mol/L), the molecular weight of nitrogen (14.01 g/mol),
and a conversion factor of 6.25.
Protein contentð%Þ¼ ð Ts /C0 TbÞ ×0 :1×1 4 :01 × 6:25 ω × 100% ð1Þ
Determination of fat content
The fat content was determined using a modi ﬁed version of the lipid
extraction method developed by Folch et al. 54. A quantity of 3.0 g of the
uniform sample was accurately weighed and placed in aﬁlter paper cylinder.
Petroleum ether (boiling range 30–60) in a volume of 150 mL was utilized as
the extraction solvent. The Soxhlet extraction apparatus (model: JB-SXT-02,
Shanghai Jiabang Electronics Co., Ltd) was employed for continuous reﬂux
extraction lasting 6 h. Subsequent to the extraction process, the solvent was
eliminated through rotary evaporation in a water bath at 60 °C. The
receiving bottle was then transferred to an oven at 105 °C and dried to
constant weight (approximately 1 h).The crude fat content was determined
by calculating the difference in mass of the receiving bottle before and after
extraction.
Determination of moisture content
According to the gravimetric method described by Chang and Zhang53,t h e
moisture content of the samples was determined by drying the samples in an
oven at 105 °C for 16–18 h to a constant weight. After drying, the samples
were cooled in a desiccator and weighed again. The moisture content was
then calculated using Eq. (2):
Hð%Þ¼ m0 /C0 m1 m0 × 100% ð2Þ
where m0 is the initial mass of the sample before drying (g), andm1i st h e
ﬁnal mass of the dried sample after reaching a constant weight (g).
Determination of ash content
The ash content of the ready-to-eat meals was determined using the dry
ashing method with reference to Perez and Andujar 55.B r i eﬂy, a speci ﬁc
amount of the homogenized sample was accurately weighed into a pre-dried
and pre-weighed crucible. The sample was then incinerated in a muf ﬂe
furnace at 550 °C until a white or light gray ash was obtained, indicating the
complete oxidation of all organic matter. After complete incineration, the
crucible containing the ash was transferred to a desiccator, cooled to room
temperature, and reweighed. The ash content was calculated using Eq. (3):
Að%Þ¼ m2 /C0 m0 m1 /C0 m0 × 100% ð3Þ
where m0 is the mass of the empty crucible (g),m1 is the initial mass of the
crucible containing the sample before ashing (g), andm2i st h eﬁnal mass of
the crucible containing the ash after cooling (g).
Determination of carbohydrate content
According to the method described by BeMiller56, total carbohydrates were
determined by difference (Eq.4):
Cð%Þ¼ 100 /C0ð H þ A þ P þ LÞð 4Þ
Where C is the total carbohydrate content, H is the moisture content, A is
the ash content, P is the crude protein content, and L is the crude fat content.
Determination of sodium content
The sodium content was determined according to the method of Corrêa
et al.57. Initially, 10.0 g of the sample was precisely weighed and ashed at
500 °C in a muf ﬂe furnace to eliminate the organic components while
preserving the inorganic elements. S ubsequently, the resulting ash was
dissolved in a concentrated acid solution. Upon complete dissolution, ﬁl-
tration was performed to eliminate any insoluble residues. Theﬁltrate was
diluted to 100 mL with deionized water, yielding the sodium test solution.
Sodium content analysis was carried out using aﬂame spectrophotometer
(Benfer BFC 150 model), using a 100 mmol/L sodium standard solution for
calibration. The outcomes were reported as grams of sodium per 100 g of
sample (mg/100 g), with all measurements performed with 4 technical
replicates for each independent sample unit.
All nutritional values (crude protein, fat, carbohydrate, sodium, and
energy) were calculated and are reported on a per 100-g edible portion basis.
Energy (kcal) was calculated using the Atwater general factors (4 kcal/g for
protein, 9 kcal/g for fat, 4 kcal/g for carbohydrate).
Determination of the electronic nose
An electronic nose system, out ﬁtted with 10 types of metal oxide semi-
conductor sensors (as detailed in TableS9), was used to analyze the volatile
compounds of the ready-to-eat meal samples. For analysis, a frozen sample
aliquot was taken from−80 °C storage and allowed to equilibrate to room
temperature. Subsequently, a 5 g portion of the thawed and homogenized
sample was placed in a 20 mL headspa ce vial and subjected to 30 min of
heating in a 50 °C water bath. The electronic nose settings were conﬁgured
as follows: cavity ﬂow rate of 200 mL/min, injection ﬂow rate of 200 mL/
min, test duration of 120 s, and collection duration of 108 s.
Determination of the electronic tongue
The taste proﬁle was analyzed using an electronic tongue system following
the procedure outlined by Zhu et al.58. Frozen sample aliquots were retrieved
from −80 °C storage and thawed at 4 °C. For analysis, 5.00 g of the thawed
and homogenized sample was blended with 100 mL of deionized water for
1 min. The mixture was centrifuged at 10,000 ×g and 4 °C for 10 min, and
the supernatant wasﬁltered through a 0.22μm membrane.
Prior to measurement, the sensor was calibrated and conditioned in a
c l e a ns o l u t i o n .A f t e rc l e a n i n g ,i tw a se q u i l i b r a t e di nt h es a m p l ef o r3 0 s
before a 30‑s measurement was taken. The sensor was then cleaned again
and transferred to a reference solution for aftertaste assessment. The
reference solution stabilized and cleansed the sensor, while the aftertaste step
simulated the lingering taste after s wallowing. Finally, the sensor signals
were converted into taste intensity va lues using dedicated taste analysis
software. Each sample was analyzed in four replicates.
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

Headspace solid-phase microextraction/gas chromatography-
mass spectrometry (HS-SPME/GC-MS) determination
Volatile compounds were analyzed by HS ‑SPME/GC‑MS (Shimadzu,
China) following Shen et al. (2024)32 with minor modiﬁcations. In line with
the sample‑handling protocol, 4 g of the frozen homogenate was weighed
directly into a 20 mL autosampler vial. A methanol solution of
2‑methyl‑3‑heptanone (internal standard, 1.68 ng/mL) was promptly
added, and the vial was sealed with a polytetraﬂuoroethylene septum. Vials
were placed in the autosampler, incubated at 55 °C for 15 min, and then
extracted by HS ‑SPME for 45 min using an 80 μmD V B / C‑WR/PDMS
ﬁber. After extraction, theﬁber was automatically injected into the GC inlet.
The GC inlet temperature was 250 °C, and desorption was performed
in splitless mode for 5 min. High‑purity helium (99.999%) was used as the
carrier gas at a constantﬂow of 1 mL/min. The oven temperature program
was as follows: hold at 35 °C for 3 min, increase to 120 °C at 5 °C/min, then
raise to 200 °C at 10 °C/min, and ﬁnally hold at 200 °C for 13 min. MS
d e t e c t i o ne m p l o y e da ne l e c t r o ni o n i z a t i o n( E I )s o u r c ea t7 0e V .B o t ht h ei o n
source and the transmission line were maintained at 200 °C, and mass
scanning was conducted within the range of 45–500 m/z.
Image acquisition and preprocessing
Images were acquired using an Apple iPhone 16 Pro Max smartphone,
featuring a 48-megapixel main camera for high-resolution images with
accurate color representation. Standardized indoor lighting was employed
during the collection process to maintain consistent lighting across all
sample images and minimize the impact of variables on image analysis
results. The photographs were taken at a 180° parallel angle relative to the
dish plane, with aﬁxed shooting distance of 30 cm from the sample surface.
The camera parameters were standardized as follows: f/1.78 aperture, 1/
120 s shutter speed, ISO 100, and 24 mm focal length. A ring LED soft light
(color temperature 5000 ± 50 K, illumination 500 ± 50 lux) was used to
avoid shadows and ensure consistent lighting across all images; 5000 K was
selected as it approximates natural daylight, minimizing color distortion for
accurate capture of product visual features (e.g., meat color, ingredient
texture), which simpliﬁes subsequent preprocessing and feature extraction.
During preprocessing, the raw images were initially converted in bat-
ches to the standard RGB format and uniformly resized to aﬁxed pixel size
to remove scale variations resultingfrom device settings. Automatic white
balance and color correction algorithms were then employed to improve
color consistency in the images, ensuring a more accurate representation of
the visual characteristics of the products.
A total of 1920 high-resolution RGB images were acquired for this
study. To improve the model ’s adaptability to real shooting conditions,
variations in image features resulting from environmentalﬂuctuations were
simulated, following the data augmentation approach in image preproces-
sing proposed by Wang et al. 59. To prevent leakage while retaining all 32
product classes in each partition, the image dataset was divided using a
stratiﬁed group split at the independent-package level. The development set
comprised 80% of the data and was further divided into training and vali-
dation subsets at a 90:10 ratio, giving approximate overall proportions of
72% training, 8% validation, and 20% test data. Images derived from the
same independent commercial package were assigned to only one subset.
All 32 ready-to-eat meal variants were represented in the training, valida-
tion, and test partitions. Z-score parameters, PCA transformations, and
other normalization statistics wereﬁtted using the training subset only.
Construction of image recognition model
Model architecture, core algorithms and training
This study constructed a multi-modal feature fusion multi-task deep
learning framework for the nutritional quality assessment of ready-to-eat
meals, which integrates three core modal branches: a visual feature branch
based on Vision Transformer (ViT), a physicochemical feature branch, and
a ﬂavor characteristic feature branch. The Transformer architecture dia-
gram of this study is shown in Fig.3a .T h ec o r eo b j e c t i v eo ft h i sf r a m e w o r ki s
to achieve deep complementary fusi on of heterogeneous features from
different modalities, and support multiple coordinated tasks:ﬁne-grained
classiﬁcation of 32 ready-to-eat meal variants, and quantitative prediction of
key nutritional components andﬂavor quality attributes.
For the physicochemical feature branch, eight physicochemical indi-
cators, including pH, color parameters L/a*/b*, protein, fat, carbohydrate,
and sodium content, were used as the original input features. A three-layer
fully connected network was used for feature encoding, producing a 128-
dimensional physicochemical feature vector. For the ﬂavor characteristic
feature branch, the response values of 10 electronic nose sensors, 7 taste
indicators of electronic tongue, and the relative content of 77 volatileﬂavor
compounds identiﬁed by GC-MS were used as the original input features.
After feature screening and dimensionality reduction by PCA, theﬁrst 20
principal components (cumulative variance contribution rate >90%) were
retained, and a 2-layer fully connected network was used for feature opti-
mization,ﬁnally outputting a 128-dimensionalﬂavor feature vector.
The complete image processing and feature encoding pipeline of the
model is as follows: First, the preprocessed input RGB images are divided
into a series of non-overlapping image patches with a size of 16×16 pixels.
All image patches are then ﬂattened and linearly projected into a 768-
dimensional embedding space, converting the two-dimensional image data
into a sequence structure that meets the input format requirements of the
Transformer encoder. To retain the spatial position information of each
patch in the original image, a learnable positional encoding vector is added
to each patch embedding vector before the sequence is fed into the encoder.
The feature sequence with posi tional encoding is input into
12 sequentially stacked Transformer encoder layers for deep hierarchical
feature extraction and optimization. Each encoder layer adopts the standard
structure of “residual connection + layer normalization”, and consists of
two core sub-modules: a Multi-Head Self-Attention (MHSA) module and a
Feed-Forward Network (FFN). Among them, the MHSA module calculates
the correlation weights between all positions in the feature sequence,
enabling the model to dynamically focus on key image regions highly cor-
related with nutritional quality assessment, including the microscopic tex-
ture of the meat matrix, the distribut ion state of fat particles, and the
compositional characteristics of dish auxiliary ingredients. The FFN module
performs high-order transformation and optimization on the extracted
deep visual features through two-lay er linear transformation with non-
linear activation, to further enhance the model ’s ability to capture subtle
feature differences in complex heterogeneous food matrices.
After deep feature extraction by the multi-layer Transformer encoder,
the model outputs a high-dimensional abstract feature representation cor-
responding to the input image. For the classi ﬁcation task of ready-to-eat
meals, a fully connected classiﬁcation head is added to theﬁnal output end of
the backbone network in this study. It maps the high-dimensional image
features to the class probability spacecorresponding to the 32 ready-to-eat
meal variants through linear transformation, andﬁnally generates the class
probability vectorPc(I) for c =0 –31, wherePc(I) is the predicted probability
that the input image I belongs to the c-th ready-to-eat meal variant.
After the independent feature extraction of the three modal branches
was completed, a cross-attention feature fusion module was constructed to
achieve deep fusion of heterogeneous features. The visual feature vector
output by ViT was used as the query vector, and the physicochemical feature
vector and ﬂavor feature vector were used as the key and value vectors
respectively. Through the multi-he ad cross-attention mechanism, the
model dynamically learned the correlation weights between visual features
and physicochemical/ﬂavor features, and realized the complementary
enhancement of multi-modal featur es. Finally, the fused multi-modal
comprehensive feature vector was input into the classi ﬁcation head and
regression head of the model, to complete the product classiﬁcation task and
nutritional component prediction task, respectively.
The classiﬁcation probability output of the model serves as the core
foundation for the quantitative estimation of nutritional components. To
convert the category probability vector into the speciﬁc predicted values of
three core nutritional components (pr otein, fat and carbohydrate), this
study designed three weighted nutritional estimation algorithms (Eqs.5–7)
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

with the physicochemically measured nutritional values of the 32 ready-to-
eat meal variants as the benchmark database. The core principle of the three
algorithms is that the nutritional content of the test sample can be estimated
by the probability-weighted average ofthe the nutritional benchmark value
associated with each product class, thereby achieving accurate prediction
from input images to nutritional indicators.
Weighted arithmetic mean (AM)
The ﬁnal predicted value of nutritionalcomponents was jointly calculated
by the multi-modal fusion feature similarity and the classi ﬁcation prob-
ability output by the model, and the calculation formula is as follows:
nj;AM ðIÞ¼
X31
c¼0
PcðIÞnc0 j ð5Þ
Where c is the total number of product classes,Pc(I) denotes the probability
that the input image I belongs to the c-th class, and nj,c represents the
measured value of thej-th nutritional indicator for products of classc .
Top-5 normalized arithmetic mean (Top-5 AM)
Among them, TOP-5 indicates the selection of the Top-5 product classes
with the highest predicted probabilities (if the number of categories is less
than 5, the actual number of categories C is taken).
nj; Top /C0 5 AMðIÞ¼
P5
c0¼1 nc0 j Pc0 ðIÞ P5
c0¼1Pc0 ðIÞ
ð6Þ
Weighted harmonic mean (HM) method
This algorithm adopts the weighted harmonic mean calculation framework,
which has higher robustness to outlier values, and is suitable for prediction
scenarios of samples with large diffe rences in nutritional composition
between categories. This algorithm only selects the top 5 categories with the
highest predicted probability (if the num b e ro fv a l i dc a t e g o r i e si sl e s st h a n5 ,
the actual number of categories C is used for calculation), and the calculation
f o r m u l ai sa sf o l l o w s :
nj; HMðIÞ¼
P5
c0¼1Pc0 ðIÞ P5
c0¼1
Pc ðIÞ
nc0 j
ð7Þ
These probability-based estimators were retained as auxiliary nutri-
tional estimation methods, whereas thedirect nutrient-regression head was
used for the regression-performance evaluation reported in terms of R2,
MAE, and RMSE.
For model training, we adopted a m ulti-task learning framework.
Cross-entropy loss was used for product classi ﬁcation, MSE loss was
retained for protein and fat regression, and a weighted Huber loss was
introduced for the carbohydrate branch. The total objective was
Ltotal ¼ LCE þ LMSE;protein þ LMSE;fatþ1:5LHuber;carbohydrate.T h eH u b e r
threshold wasδ¼1:0g=100g; because carbohydrate labels were standardized
during training, the implemented threshold wasδstd¼1:0=SDcarb;train.T h e
carbohydrate-loss weightλcarb and δ were selected using a validation-only
grid (λcarb¼1:00;1:25;1:50;2:00;δ¼0:50;1:00;1:50;2:00g=100g), prioritiz-
ing the lowest carbohydrate RMSE subject to ≤0.50-percentage-point
classiﬁcation-accuracy loss and ≤0.01 decreases in protein and fat R 2.
Training was performed using the AdamW optimizer with an initial
learning rate of 1×10-4. A linear learning rate warmup was set for the ﬁrst
10% of the training steps, followed by a cosine learning rate decay schedule.
Data augmentation strategies, including random horizontal ﬂips, random
rotations (within ±10°), and random b rightness/contrast adjustments
(range: 0.9–1.1), were applied to the training set to improve the model ’s
generalization ability. The training process used a batch size of 32, ran for a
maximum of 50 epochs, and adopted an early stopping strategy based on
validation loss to prevent model overﬁtting.
The complete training con ﬁguration is reported in Supplementary
Table S10. Images were resized to 224 × 224 pixels. The ViT branch used
16 × 16 patches, a 768-dimensional embedding, 12 encoder layers, 12
attention heads, a 3072-dimensional MLP, and dropout/attention-dropout
rates of 0.10. AdamW used β1 = 0.90, β2 = 0.999, ε =1×1 0 −8,a n dw e i g h t
decay = 0.05. Early stopping patience was 8 epochs. Five independent runs
used seeds 42, 3407, 2025, 7129, and 12345. The software environment was
Python 3.10.13, PyTorch 2.4.1, torchvision 0.19.1, and CUDA 12.1.
For model lightweighting, structured pruning was applied only to the
intermediate channels of the FFN blocks in each Transformer encoder, and
pruning ratios of 20% and 30% were evaluated. For each Linear(768,3072)
layer, output neurons were ranked by the L1 norm of their weights, and the
corresponding proportion of the lowest-ranked intermediate neurons was
removed together with the associatedinput channels of the following Linear
(3072,768) layer. Q/K/V projections, a ttention heads, patch embedding,
LayerNorm, the 768-dimensional embedding, and cross-attention output
dimensions were retained. The pruned model wasﬁne-tuned for 10 epochs
using AdamW with a learning rate of 1 × 10−5 and batch size 32.
Post-training INT8 quantization was performed using a 256-image
calibration subset sampled only from the training data withﬁxed seed 42;
validation and test images were excl uded. Calibration preprocessing was
identical to inference preprocessing, and the resulting INT8 scales wereﬁxed
before test evaluation. Inference benchmarking used batch size 1, 100 warm-
up runs, 1000 timed runs, and ﬁve independent repeats for each model/
hardware combination. CUDA synchronization was applied before and
after timed GPU inference. The deployment path was ONNX export fol-
lowed by TensorRT engine generation and execution on Jetson Orin Nano.
To interpret the model’s prediction results and clarify the spatial dis-
tribution of image features that affect the model ’s decision-making, we
employed Gradient-weighted Class Activation Mapping (Grad-CAM) to
generate visual explanations for themodel. This technique produces coarse
localization heatmaps, which highlight the key regions in the image (such as
marbled fat regions and speciﬁc texture patterns) that the model considers
most important for predicting nutritional properties, so as to provide an
intuitive insight into the internal reasoning process of the model.
Model training and evaluation wereperformed for 5 independent runs
with different random seeds under the ﬁxed stratiﬁed group split at the
independent-package level. All training hyperparameters remained con-
sistent across the 5 independent runs to ensure the controlled variable
principle. For the classi ﬁcation, nutrient-regression, and added volatile-
compound regression tasks, theﬁnal performance metrics are reported as
mean ± standard deviation derived from theﬁve independent experimental
runs, to fully reﬂect the stability and generalization ability of the model.
For quantitative volatile-compoundregression, GC-MS concentration
values were treated only as prediction targets. All 77 GC-MS concentration
variables and all OAV-derived variables were excluded from X. The per-
mitted inputs comprised visual features, physicochemical features, and 17
ﬂavor-sensor variables (10 electronic-nose responses and 7 electronic-
tongue indicators). Target concentrations were transformed as log10(C+
1) before regression. Any PCA or normalization used for this experiment
was ﬁtted exclusively on the training sub set. Technical repeats from the
same independent package were not allowed to cross training, validation,
and test partitions, and the test targets were not used for feature screening,
hyperparameter selection, or early stopping. Modality ablation compared
visual only, physicochemical+ ﬂavor-sensor, visual+ ﬂavor-sensor, visual
+ physicochemical, and the full visual+ physicochemical+ ﬂavor-sensor
conﬁguration.
External validation
To evaluate the model’s performance on unseen data, external validation
was conducted using the independent test set (20% of the dataset). Training,
validation, and test subsets were separated using the same strati ﬁed
independent-package grouping described above. The validation subset was
used only for early stopping, hyperpa rameter selection, and checkpoint
selection. The test subset was accessed only after the ﬁnal model
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

conﬁguration had beenﬁxed. No images or technical repeats from the same
independent package were allowed to cross partitions. The same grouping
strategy was maintained across the ﬁve independent runs, with the pre-
deﬁned random seeds reported in Supplementary Table S10. This validation
assessed the classi ﬁcation and nutritional-estimation functions of the
model: (1) classiﬁcation among 32 ready-to-eat meal variants, measured by
accuracy, precision, recall, F1-score, and confusion matrix; and (2) nutri-
tional estimation (protein, fat, and carbohydrate content), evaluated using
coefﬁcient of determination (R2), MAE, and RMSE. The test set predictions
were compared against ground-truthproduct labels and measured physi-
cochemical values (nutritional comp onents). This external validation
ensured the model’s robustness and generalizability beyond the training
data, simulating real-world application scenarios.
Data analysis
All statistical analyses were performed using IBM SPSS Statistics (Version
26.0, IBM Corp., Armonk, NY, USA). For physicochemical property and
electronic sensory (e-nose, e-tongue) analyses, the experimental unit was an
independent commercial package of ready-to-eat meal, with 9 replicates set
for each product. All instrumental measurements were performed in
quadruplicate for each replicate, and the ﬁnal value was calculated as the
mean of the quadruplicate technical tests. For consumer sensory evaluation,
the experimental unit was the rating from an individual participant, with
each product evaluated in 3 independent sessions.
Prior to statistical analysis, the normality and homogeneity of variance
of all datasets were veriﬁed using the Shapiro-Wilk test and Levene’st e s t ,
respectively. Signiﬁcant differences in physicochemical and sensory attri-
butes among the 32 products were assessed by one-way ANOVA with
product type as theﬁx e df a c t o r ,f o l l o w e db yT u k e y’s HSD post-hoc test for
pairwise comparisons. The thr eshold for statistical signi ﬁcance was set
at P < 0.05.
Data visualization was performed using Origin Pro 2022b (OriginLab
I n c . ,N o r t h a m p t o n ,M A ,U S A ) .H e a t map construction and Pearson cor-
relation analysis were conducted using TBtools (Version 2.098). All vari-
ables were Z-score normalized prior to correlation analysis, and no
multiple-testing correction was applied for the exploratory analyses.
For the deep learning model evaluation, the independent held-out test
set (20% of the total image dataset) was used. Model performance was
evaluated for classiﬁcation and nutrient regression: (1) classiﬁcation among
32 ready-to-eat meal variants, with assessment metrics including accuracy,
precision, recall, and F1-score; (2) regression task for protein, fat, and car-
bohydrate content estimation, with evaluation metrics including the coef-
ﬁcient of determination (R2), MAE, and RMSE.
The added volatile-compound regression task was evaluated usingR2,
M A E ,R M S E ,l o g - M A E ,a n dl o g - R M S E .For the modality ablation analysis,
the same ﬁxed split and evaluation protocol were applied to all branch
combinations so that changes in performance reﬂected the contribution of
the removed modality rather than differences in data partitioning.
Data availability
The datasets generated and/or analyzed during the current study are not
publicly available due to con ﬁdentiality restrictions, institutional data-
management requirements, and participant privacy and ethical restrictions,
but are available from the corresponding author on reasonable request,
subject to applicable institutional and ethical requirements. The complete
model hyperparameters are reported in Supplementary Table S10.
Code availability
The custom code used for model training, model evaluation, and data
analysis in this study is not publicly available due to institutional data
management considerations, but is available from the corresponding author
on reasonable request.
Received: 6 March 2026; Accepted: 20 September 2026;
References
1. Wang, Z. et al. Decoding the ﬂavor of traditional Chinese stir-fried pork
cuisine: development of a sensory wheel and exploration of the
relationship between sensory attributes and aroma compounds.Food
Res. Int. 214, 116650 (2025).
2. Jia, Y. et al. Innovations and challenges in the production of prepared
dishes based on central kitchen engineering: a review and future
perspectives. Innov. Food Sci. Emerg. Technol. 91, 103521 (2024).
3. Lin, H. et al. Water-oil displacement in prefried potatoes during
freezing-thawing and reheating: a simulation of the industrial prepared
dishes supply chain. Food Chem. 490, 145111 (2025).
4. Khalid, W. et al. Dynamic alterations in protein, sensory, chemical, and
oxidative properties occurring in meat during thermal and non-
thermal processing techniques: a comprehensive review. Front. Nutr.
9, 1057457 (2023).
5. Feng, Y. et al. Large-scale image classi ﬁcation and nutrient estimation
for Chinese dishes. J. Agric. Food Res. 19, 101733 (2025).
6. Fridolfsson, J., Sjöberg, E., Thiwang, M. & Pettersson, S. Performance
evaluation of 3 large language models for nutritional content
estimation from food images. Curr. Dev. Nutr. 9, 107556 (2025).
7. González, A., Ojedo, F., Ruiz, I. & de Brugada, I. The effect of nutritional
labels on the facilitation of food image detection. Food Qual. Prefer.
130, 105547 (2025).
8. Tsolakidis, D., Gymnopoulos, L. P. & Dimitropoulos, K. Arti ﬁcial
intelligence and machine learning technologies for personalized
nutrition: a review. Informatics 11, 62 (2024).
9. Wang, X. et al. Enhancing optical non-destructive methods for food
quality and safety assessments with machine learning techniques: a
survey. J. Agric. Food Res. 19, 101734 (2025).
10. Wang, H. et al. Nutritional composition analysis in food images: an
innovative Swin Transformer approach. Front. Nutr. 11, 1454466
(2024).
11. Li, M. et al. Deep learning-based multimodal fusion for quality
prediction of chili paste using hyperspectral imaging and near-infrared
spectroscopy. Food Chem. 493, 145712 (2025).
12. Kaushal, S. et al. Computer vision and deep learning-based
approaches for detection of food nutrients/nutrition: new insights and
advances. Trends Food Sci. Technol. 146, 104408 (2024).
13. Shen, C. et al. Machine vision combined with deep learning-based
approaches for food authentication: an integrative review and new
insights. Compr. Rev. Food Sci. Food Saf. 23, e70054 (2024).
14. Meenu, M. et al. A concise review on food quality assessment using
digital image processing. Trends Food Sci. Technol. 118, 106–124
(2021).
15. Patel, K. K., Kar, A., Jha, S. N. & Khan, M. A. Machine vision system: a
tool for quality inspection of food and agricultural products. J. Food
Sci. Technol. 49, 123–141 (2012).
16. Ke, Q., Zhang, J., Huang, X., Kou, X. & Zhang, D. Machine learning
unveils three layers of food complexity. npj Sci. Food 10, 87 (2026).
17. Yuan, J. et al. A review of deep learning models for food ﬂavor data
analysis. J. Future Foods 6, 533–544 (2026).
18. Zimmermann, Y., Sieben, L., Seng, H., Pestlin, P. & Görlich, F. A
chemical language model for molecular taste prediction.npj Sci. Food
9, 122 (2025).
19. Shi, P. et al. AI-driven exploration of microbial resources in fermented
foods. Trends Food Sci. Technol. 167, 105450 (2026).
20. Yu, J. et al. A food safety targeted sampling decision-making method
based on association rule mining and GNNs. npj Sci. Food 9, 132
(2025).
21. Zhang, D. Practical guide for food scientists to build AI: data,
algorithms, and applications. Food Chem. 499, 147281 (2026).
22. Motoki, K., Spence, C. & Velasco, C. When visual cues inﬂuence taste/
ﬂavour perception: a systematic review. Food Qual. Prefer. 111,
104996 (2023).
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

23. Harris, N. M., Lindeman, R. W., Bah, C. S. F., Gerhard, D. & Hoermann,
S. Eliciting real cravings with virtual food: using immersive
technologies to explore the effects of food stimuli in virtual reality.
Front. Psychol. 14, 956585 (2023).
24. Cavalcante, C. L., Gonza, M. M. C., Lopes, B. G. & Contreras-Castillo,
C. J. Impact of ultimate pH on oxidative stability and warmed-over
ﬂavor in aged beef after grilling and reheating. Int. J. Gastron. Food
Sci. 40, 101140 (2025).
25. Ou, Q., Zhang, Y., Wang, L., Xiong, Y. L. & Chen, J. Flavor formation,
deterioration and preservation in ready-to-eat spiced braised meat
products: a comprehensive review. Trends Food Sci. Technol. 173,
105762 (2026).
26. Liang, E. et al. Effect of salt on volatile ﬂavor substances in meat
products: a review. LWT 238, 118857 (2025).
27. Delgado-Andrade, C., Seiquer, I., Haro, A., Castellano, R. & Navarro,
M. P. Development of the Maillard reaction in foods cooked by
different techniques. Intake of Maillard-derived compounds. Food
Chem. 122, 145–153 (2010).
28. Swatland, H. J. How pH causes paleness or darkness in chicken
breast meat. Meat Sci. 80, 396–400 (2008).
29. Yang, Y., Achaerandio, I. & Pujolà, M. Effect of the intensity of cooking
methods on the nutritional and physical properties of potato tubers.
Food Chem. 197, 1301–1310 (2016).
30. Li, J., Han, D., Huang, F. & Zhang, C. Effect of reheating methods on
eating quality, oxidation andﬂavor characteristics of braised beef with
potatoes product. Int. J. Gastron. Food Sci. 31, 100659 (2023).
31. Yao, Y. et al. Formation of characteristic aroma in traditional livestock
and poultry meat products and strategies of aroma control and
standardization for industrial cooking.Trends Food Sci. Technol.163,
105208 (2025).
32. Shen, C. et al. Characterization of lamb shashliks with different
roasting methods by intelligent sensory technologies and GC-MS to
simulate human multi-sensation: based on multimodal deep learning.
Food Chem. 440, 138265 (2024).
33. Jiang, H. et al. Variation of volatile ﬂavor substances in salt-baked
chicken during processing. Food Chem. X 24, 101846 (2024).
34. Dinh, T. T. N., To, K. V. & Schilling, M. W. Fatty acid composition of
meat animals as ﬂavor precursors. Meat Muscle Biol. 5,1 –16 (2021).
35. Wang, X. et al. Changes of lipid oxidation, volatile and taste-active
compounds during pan-heating of pork belly. Food Res. Int. 172,
113106 (2023).
36. Guichard, E. Interactions between ﬂavor compounds and food
ingredients and their inﬂuence on ﬂavor perception. Food Rev. Int. 18,
49–70 (2002).
37. Zhao, J. et al. Formation mechanism of aroma compounds in a
glutathione-glucose reaction with fat or oxidized fat.Food Chem. 270,
436–444 (2019).
38. Gómez, I., Ibañez, F. C. & Beriain, M. J. Physicochemical and sensory
properties of sous vide meat and meat analog products marinated and
cooked at different temperature-time combinations.Int. J. Food Prop.
22, 1693–1708 (2019).
39. Wang, P. et al. Changes in ﬂavour characteristics and bacterial
diversity during the traditional fermentation of Chinese rice wines from
Shaoxing region. Food Control 44,5 8–63 (2014).
40. Xu, D. et al. Changes in volatile ﬂavor compounds and metabolites
during processing of ginger milk curd from buffalo milk by GC-IMS
and LC-MS. Food Res. Int. 209, 116230 (2025).
41. Qiao, X. et al. Research on the migration mechanism of volatile
substances from garlic in light soy sauce. LWT 228, 118144 (2025).
42. Jiang, S., Min, W., Liu, L. & Luo, Z. Multi-scale multi-view deep feature
aggregation for food recognition. IEEE Trans. Image Process. 29,
265–276 (2020).
43. Shao, W. et al. Vision-based food nutrition estimation via RGB-D
fusion network. Food Chem. 424, 136309 (2023).
44. Ma, P. et al. Image-based nutrient estimation for Chinese dishes using
deep learning. Food Res. Int. 147, 110437 (2021).
45. Ma, P., Lau, C. P., Yu, N., Li, A. & Sheng, J. Application of deep
learning for image-based Chinese market food nutrients estimation.
Food Chem. 373, 130994 (2022).
46. Uttaro, B. & Zawadski, S. Prediction of pork belly fatness from the
intact primal cut. Food Control 21, 1394–1401 (2010).
47. Bi, J. et al. Accurate evaluation of the lipid characteristics and ﬂavor of
abdominal muscle resulting from different cooking processes using
lipidomics and GC-IMS analysis. Food Chem. X 27, 102353 (2025).
48. Lyu, C., Forde, C. G. & Stieger, M. Effect of oral burn on dynamic taste,
ﬂavor and mouthfeel perception of tomato soups, curried rice and
beef patties. Food Qual. Prefer. 115, 105109 (2024).
49. Lyford, C. P. et al. Is willingness to pay (WTP) for beef quality grades
affected by consumer demographics and meat consumption
preferences? Australas. Agribus. Rev. 18,1 –18 (2010).
50. Zellner, D. A., Loss, C. R., Zearfoss, J. & Remolina, S. It tastes as good
as it looks! The effect of food presentation on liking for the ﬂavor of
food. Appetite 77,3 1–35 (2014).
51. World Medical Association. World Medical Association Declaration of
Helsinki: ethical principles for medical research involving human
subjects. JAMA 310, 2191–2194 (2013).
52. Ping, C. et al. Identi ﬁcation of characteristic ﬂavor quality of ceramic-
pot sealed meat after reheating based on HS-GC-IMS, bionic sensory
combined chemometrics. Food Chem. X 23, 101640 (2024).
53. Chang, S. K. C. & Zhang, Y. Protein analysis. in Food Analysis315–331
(ed. Nielsen, S. S.) (Springer International Publishing, 2017).
54. Folch, J., Lees, M. & Sloane Stanley, G. H. A simple method for the
isolation and puriﬁcation of total lipides from animal tissues. J. Biol.
Chem. 226, 497–509 (1957).
55. Perez, D. & Andujar, G. Determination of ash content in meat products.
Meat Sci. 5, 165–170 (1981).
56. BeMiller, J. N. Carbohydrate analysis. in Food Analysis 147-177 (ed.
Nielsen, S. S.) (Springer US, 2010).
57. Corrêa, P. F., da Silva, C. F., Ferreira, J. P. & Guerra, J. M. C.
Vegetable-based frankfurter sausage production by different
emulsion gels and assessment of physical-chemical, microbiological
and nutritional properties. Food Chem. Adv. 3, 100354 (2023).
58. Zhu, D. et al. Collaborative analysis on difference of apple fruits ﬂavour
using electronic nose and electronic tongue. Sci. Hortic. 260, 108879
(2020).
59. Wang, T. et al. Multimodal nondestructive testing of tender coconut
water quality using spectroscopy, computer vision, and deep
learning. Food Control 180, 111660 (2026).
Acknowledgements
This work was supported by the Liaoning Revitalization Talents Program
(Grant No. XLYC2502022).
Author contributions
Wenxi Qi: Data curation, methodology, writing—original draft, writing—
review and editing. Meiqi Ding: Formal analysis, supervision. Yi Zhang:
Formal analysis, supervision. Bo Wang: Formal analysis, supervision, writing
—review and editing, supervision. Che Shen: Formal analysis, methodology,
writing—review and editing. Dengyong Liu: Writing—review and editing,
supervision and funding acquisition.
Competing interests
The authors declare no competing interests.
Additional information
Supplementary informationThe online version contains
supplementary material available at
https://doi.org/10.1038/s41538-026-01186-8.
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press

Correspondenceand requests for materials should be addressed to
Bo Wang, Che Shen or Dengyong Liu.
Reprints and permissions informationis available at
http://www.nature.com/reprints
Publisher’s noteSpringer Nature remains neutral with regard to jurisdictional
claims in published maps and institutional afﬁliations.
Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and
reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if you modi ﬁed the licensed material. You
do not have permission under this licence to share adapted material
derived from this article or parts of it. The images or other third party
material in this article are included in the article's Creative Commons
licence, unless indicated otherwise in a credit line to the material. If material
is not included in the article's Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted use,
you will need to obtain permission directly from the copyright holder. To
view a copy of this licence, visit http://creativecommons.org/licenses/by-
nc-nd/4.0/.
© The Author(s) 2026
This Article in Press is shared early to give you faster access to new research.
It is citable and carries a permanent DOI. Theﬁnal edited version will replace it
automatically.
https://doi.org/10.1038/s41538-026-01186-8 Article
npj Science of Food Article in Press
