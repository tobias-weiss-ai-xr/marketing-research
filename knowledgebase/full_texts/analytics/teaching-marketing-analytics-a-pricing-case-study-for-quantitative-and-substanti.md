---
title: 'Teaching marketing analytics: a pricing case study for quantitative and substantive marketing
  skills'
url: https://doi.org/10.1057/s41270-024-00313-2
category: analytics
subcategory: measurement
date: 2024-05
venue: Journal of Marketing Analytics
authors:
- Bernd Skiera
- Lukas Jürgensmeier
source: openalex-oa
pdf_url: https://www.econstor.eu/bitstream/10419/316666/1/41270_2024_Article_313.pdf
pages: 19
chars: 72281
fetched_at: '2026-11-08T13:40:39+00:00'
kb_version: 1
---

# Teaching marketing analytics: a pricing case study for quantitative and substantive marketing skills

Skiera, Bernd; Jürgensmeier, Lukas
Article  —  Published Version
Teaching marketing analytics: a pricing case study for
quantitative and substantive marketing skills
Journal of Marketing Analytics
Provided in Cooperation with:
Springer Nature
Suggested Citation: Skiera, Bernd; Jürgensmeier, Lukas (2024) : Teaching marketing analytics: a
pricing case study for quantitative and substantive marketing skills, Journal of Marketing Analytics,
ISSN 2050-3326, Palgrave Macmillan, London, Vol. 12, Iss. 2, pp. 209-226,
https://doi.org/10.1057/s41270-024-00313-2
This Version is available at:
https://hdl.handle.net/10419/316666
Standard-Nutzungsbedingungen:
Die Dokumente auf EconStor dürfen zu eigenen wissenschaftlichen
Zwecken und zum Privatgebrauch gespeichert und kopiert werden.
Sie dürfen die Dokumente nicht für öffentliche oder kommerzielle
Zwecke vervielfältigen, öffentlich ausstellen, öffentlich zugänglich
machen, vertreiben oder anderweitig nutzen.
Sofern die Verfasser die Dokumente unter Open-Content-Lizenzen
(insbesondere CC-Lizenzen) zur Verfügung gestellt haben sollten,
gelten abweichend von diesen Nutzungsbedingungen die in der dort
genannten Lizenz gewährten Nutzungsrechte.
Terms of use:
Documents in EconStor may be saved and copied for your personal
and scholarly purposes.
You are not to copy documents for public or commercial purposes, to
exhibit the documents publicly, to make them publicly available on the
internet, or to distribute or otherwise use the documents in public.
If the documents have been made available under an Open Content
Licence (especially Creative Commons Licences), you may exercise
further usage rights as specified in the indicated licence.
  http://creativecommons.org/licenses/by/4.0/

Vol.:(0123456789)
Journal of Marketing Analytics (2024) 12:209–226
https://doi.org/10.1057/s41270-024-00313-2
CASE STUDY
Teaching marketing analytics: a pricing case study for quantitative
and substantive marketing skills
Bernd Skiera1  · Lukas Jürgensmeier1
Revised: 27 March 2024 / Accepted: 28 March 2024 / Published online: 27 May 2024
© The Author(s) 2024
Abstract
This article describes a data-driven case study for teaching and assessing students’ skills in marketing analytics, specifically
in pricing. This case study combines teaching econometrics to analyze data and substantive marketing to derive managerial
insights. The econometric challenge requires students to set up and implement a regression analysis to derive the demand
function, detect multicollinearity, and select appropriate data visualizations. The substantive challenge requires deriving
optimal pricing decisions and understanding how the parameters of the demand function impact optimal prices and the
associated profit. We test the case study in a marketing analytics exam and discuss the performance of 134 students. Beyond
assessing student performance in an exam, the case study facilitates teaching through in-class group work or assignments.
Free of charge, under a liberal CC BY license, we encourage other educators to use the case study in their teaching. We
provide the necessary data and a sample solution using the statistical programming language R.
Keywords Marketing analytics · Pricing · Teaching · Education · Case study · Data science
Introduction
Marketing analytics, or data-driven marketing, enables
managers to make decisions based on insights from ana-
lyzing data rather than relying upon their intuition or past
experiences (Iacobucci et al. 2019). New technologies and
increasing data availability in marketing (Petrescu and
Krishen 2018; Van Auken 2015) enable the implementa-
tion of an evidence-based approach to marketing decision-
making that promises better and less risky decisions (Wedel
and Kannan 2016). For example, data-driven marketing uses
data to estimate demand functions depending on prices and
advertising budgets and derives optimal prices through profit
maximization.
Successful marketing analytics teaching requires that
future decision-makers, i.e., today’s marketing students,
learn (i) how to analyze data and (ii) how to turn the insights
from this analysis into marketing decisions.
Hence, such decisions require skills in econometrics and
marketing. However, many multivariate data analysis text-
books primarily cover theoretical aspects of data analysis
(e.g., Stock and Watson 2019; Wooldridge 2013), putting
less emphasis on turning the econometric insights into (opti-
mal) substantive decisions. In contrast, textbooks on sub-
stantive marketing topics focus on marketing management
and less on data analysis (e.g., Kotler et al. 2019).
In the vein of more specialized marketing analytics text-
books (e.g., Mizik and Hanssens 2018), this article aims to
bridge this gap between econometrics and substantive mar-
keting knowledge by suggesting a marketing analytics case
study that connects both skills.
This article aims to introduce and disseminate a market-
ing analytics case study that covers a fundamental task of
marketing—deriving optimal prices—and sets this deci-
sion into context with several other typical marketing ques-
tions: measurement of advertising effects, marketing mix
allocation, and performance-based compensation of sales
representatives.
By analyzing a simulated data set including sales,
prices, and other marketing mix variables, students
learn the theory and practical application of standard
 * Bernd Skiera
 skiera@wiwi.uni-frankfurt.de
 Lukas Jürgensmeier
 juergensmeier@wiwi.uni-frankfurt.de
1 Department of Marketing, Faculty of Economics
and Business, Goethe University Frankfurt,
Theodor-W.-Adorno-Platz 4, 60629 Frankfurt, Germany

210 B. Skiera, L. Jürgensmeier
econometric methods, such as the multivariate linear
regression, and use its results to determine optimal prices,
discuss advertising allocations to different marketing
channels, and estimate the impact of those marketing
decisions on sales and profit.
We assess the exercise’s efficacy as a 60-min final
exam by analyzing the performance of 134 students in an
undergraduate marketing analytics class. The results show
that the exercise results in approximately normally dis-
tributed student performance across all sub-exercises with
a mean close to half of the achievable points. Although
the exercise is very challenging to solve in 60 min, the
almost perfect solutions of a few students show that its
difficulty is well-calibrated.
On an individual sub-exercise level, our empirical
analysis shows that the sub-exercises vary in difficulty,
as reflected by the distribution of student performance.
These results indicate which sub-exercises confront stu-
dents with the biggest challenge and suggest where educa-
tors could focus their teaching efforts.
Our article first introduces the didactic setting, includ -
ing the case study’s pedagogical vision, learning goals,
structure, and theoretical background. After introducing
the context, we provide the full case study and detailed
solutions with a rubric that enables educators to use the
exercise as a case study, a (graded) assignment, or an
exam. The article proceeds with a discussion of the case
study’s implementation. Before concluding, we assess
and discuss the case study’s efficacy by presenting the
graded results from 134 exam submissions. We provide
data, simulation codes, exercise templates, and solutions
in the accompanying repository, https:// github. com/ lukas-
jue/ marke ting- analy tics- exerc ise.
Background of the case study
Description of pedagogical vision
We pursue the following two pedagogical aims with this
case study:
(a) equip students and future marketing managers with the
quantitative intuition and econometric toolkit to ana-
lyze marketing data, and
(b) enable students to use those quantitative skills to derive
better marketing decisions.
Fundamentally, we want students to understand in which
marketing setting which econometric method fits best. For
example, this case study does not ask students to “estimate
a linear regression and interpret its parameters” but instead
asks them to derive optimal prices based on the avail-
able data. Hence, students need to identify the appropriate
method themselves. Through this didactic approach, we aim
to prepare the students for their future work by simulating a
realistic working environment where part of the challenge
is identifying the path toward a solution.
Description of learning goals
Table 1 describes the learning goals of our case study, which
correspond to the two pedagogical aims stated above. In the
first column, we list the marketing learning goals, which
equip students with substantive marketing skills. The second
column describes the analytical or econometric techniques
students need to fulfill the corresponding marketing learn-
ing goal.
We structure the case study to achieve those stated learn-
ing goals through the following seven parts:
Table 1  Link between the Case Study’s Learning Goals in Marketing and Analytics
Marketing Analytics (Econometrics)
Understanding typical marketing data (here: sales and price data) Using a programming language to read, visualize, and model data
Estimating and interpreting parameters of a demand function from
sales and price data
Estimating and interpreting results of the (multivariate) linear regres-
sion
Understanding the relationship between a demand and a profit function Using the parameter estimates from the linear regression to describe the
demand function and set up the respective profit function
Setting the optimal price based on the demand function estimated
from sales and price data
Taking the first derivative of the profit function to derive its maximum
for identifying the optimal price
Understanding the impact of marketing mix variables (e.g., advertis-
ing) on the demand function and the corresponding optimal price
In linear regression, understanding how changing the value of an inde-
pendent variable impacts the dependent variable
Interpreting elasticities of demand and assessing their plausibility Understanding and computing the (price) elasticity of demand
Identifying and avoiding the impact of multicollinearity in marketing
variables on managerial decisions
Understanding the econometric problem and consequences of multicol-
linearity

211
Teaching marketing analytics: a pricing case study for quantitative and substantive marketing…
1. Starting with simple descriptive statistics and visualiza-
tions to understand the data and potential problems,
2. continuing with specifying the correct demand function
and modeling it through an appropriate multivariate lin-
ear regression,
3. using the regression results to compute price and adver-
tising budget elasticities of demand,
4. using the estimated demand function to derive optimal
prices,
5. estimating the impact of changes in the advertising
budget allocation on optimal prices,
6. using the econometric results to evaluate proposed mar-
keting budget allocations, and
7. assessing which performance characteristics of sales
representatives could justify different compensations for
individual salespersons based on their expected profit
(derived from the demand function).
This ordering follows a typical analytics workflow—from
descriptively analyzing the data to modeling and deciding
based on those results.
Considerations from the literature for successful
case study development
Because our case study should be suitable for both exams
and teaching, we consult the literature to derive characteris-
tics of a successful exam exercise and teaching case study,
respectively.
Characteristics of a successful exam exercise
One of the prominent theories in psychometrics and student
testing is the Item Response Theory. This framework aids
in constructing exams that accurately measure the latent
student ability. To achieve this aim, Item Response Theory
models students’ probability of correctly solving a sub-exer-
cise as a function of the exercise’s difficulty, among other
parameters (e.g., DeMars 2010). Constructing an exam with
sub-exercises of varying difficulty enables the educator to
differentiate between different levels of student ability.
Hence, in line with the requirements of Item Response
Theory, our exam aims to feature sub-exercises of varying
difficulty such that they can discriminate well between dif-
ferent levels of student performance.
Although assessing the exercise’s capability of measuring
the latent ability remains beyond this manuscript’s scope, we
posit that the full exam should be sufficiently difficult to dis-
tinguish between degrees of student performance granularly
but not too difficult such that the exercise lacks differential
power. Hence, the results of the exam should.
(a) yield an approximately normal distribution of achieved
points, thereby reflecting the assumed normal distribu-
tion of students’ abilities,
(b) with students’ performances covering the entire range
of possible outcomes.
While these two empirical characteristics refer to the full
set of sub-exercises, the exam should feature sub-exercises
from a broad range of difficulties. Hence, the exam results
should feature.
(c) sub-exercises with a comparatively high degree of cor-
rect submissions (i.e., relatively easy sub-exercises),
and
(d) exercises with a comparatively low degree of correct
submissions (i.e., relatively challenging sub-exercises).
Eventually, we test whether those requirements hold in an
exam setting in our empirical section. There, we present and
discuss the student performance distribution to our exercise
in an exam setting.
Additionally, we designed the exercise to feature high
construct validity (e.g., Peter 1981). Transferring the role
of construct validity in marketing research to an educational
setting, a successful marketing analytics exercise should
mirror the substantive marketing and analytics requirements
demanded in students’ future careers. Hence, the exercise
should reflect a typical marketing analytics task commonly
faced in practice and academia—thereby correctly assess-
ing students’ abilities in this field. We ensure this require-
ment through the topic choice (pricing) and the required
analytics techniques (data visualization, regressions, and
optimization).
Characteristics of a successful teaching case study
While the previous theoretical considerations apply primar-
ily to the exam setting, we also aim to provide a useful case
study for teaching purposes. Hence, the following theoretical
considerations inspired the development of the case study.
First, and congruent to exhibiting a high construct valid-
ity, a successful case study for teaching purposes should
exhibit constructive alignment (Biggs 1996). Hence, the
case study should mirror the course’s intended learning out-
comes. We designed the case study to feature high construc-
tive alignment with a typical marketing analytics course, as
reflected by the marketing and analytics learning goals in
Table 1.
Second, besides the case study mirroring the academic
course’s learning goals, it should also mirror what students
expect in the real world. Hence, the case study should be an
“authentic assessment,” meaning that students can expect

212 B. Skiera, L. Jürgensmeier
a similar case once they graduate and practice marketing
analytics (Montano et al., forthcoming).
Third, the case study should be sufficiently difficult to
provide ample learning opportunities. Hence, some of the
case study’s sub-exercises should be relatively challenging
even for exceptional students, enabling discussions in which
a teacher explains the underlying non-trivial approach to
solve the case study correctly.
After introducing the exercise’s pedagogical vision, learn-
ing goals, and theoretical background, we now introduce
the case study and provide detailed solutions, including a
grading rubric.
Description and solution of the case study
Your B2B firm sells an energy-efficient heater fan and has
divided the country into 100 comparable sales territories,
each staffed exclusively by a female sales representative. The
sales representatives differ according to their professional
experience (measured by the number of years they have been
in sales) and whether they have an engineering degree.
The management recently stated that 50% of the sales
representatives have at least five years of professional expe-
rience in sales, and at least one-third of the sales representa-
tives also have an engineering degree.
The firm’s management randomly varied the prices across
the sales territories.
In addition, the management commissioned an adver -
tising agency to support the sales representatives through
marketing and provided a dedicated budget. The agency
should use this marketing budget for telephone marketing
and social media marketing, with an approximately equal
allocation towards the two channels (i.e., 50% phone calls
and 50% social media marketing). So far, the firm’s manage-
ment has randomly varied the agency’s budget across the
sales territories.
The variable cost per unit of a heater fan is $200.
In the file data_sales.csv, you receive information
that helps you answer the questions. The data set includes
100 rows, each describing one of the 100 sales territories
with the following variables:
Table: Description of the data set data_sales.csv
Variable Description
quantity Number of sold heater fans in the respective
sales territory
price Price of the heater fan sold in the respective
sales territory
experience Number of years the sales representative has
been working in sales
Variable Description
engineer Binary variable indicating whether the sales
representative has an engineering degree
(= 1) or not (= 0)
gender Gender of the sales representative, female
(= 1) or other (= 0)
location Number of letters of the sales representa-
tive’s birthplace (e.g., 7 if the birthplace is
“Chicago”)
budget_agency Budget used by the advertising agency, which
is either spent for phone or social media
marketing, in $
budget_phone Budget used for telephone marketing, in $
budget_social_media Budget used for social media marketing, in $
(1): Exploratory data analysis
For each part of this first exercise, please answer the ques-
tion by analyzing the data set through one visualization and
one non-visual descriptive analysis.
We do not require custom labels for the visualizations.
(a)
Does the firm only employ female sales representatives?
(2 points).
Solution
df <- read.csv("data_sales.csv")
summary(df$gender)
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
##       1       1       1       1       1       1
barplot(table(df$gender), main = "Barplot of Gender"
b = "Number of Sales Territories")
Yes, because the summary statistics and the barplot show
that the data set only includes gender = 1, corresponding
to females.
(b)
Do the prices differ across sales territories? (2 points).

213
Teaching marketing analytics: a pricing case study for quantitative and substantive marketing…
Solution
summary(df$price)
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
##   209.4   271.1   301.4   300.4   329.6   369.4
hist(df$price, main = "Histogram of Price", xlab = "Price (in $)", ylab =
"Number of Sales Territories")
Yes, prices differ across sales territories. For example, the
summary statistics exhibit different values for the minimum
($209.4) and maximum ($369.4). Additionally, the histo-
gram shows that prices vary across sales territories.
(c)
Is the management’s statement regarding the professional
experience of their sales representatives correct? (2 points).
Solution
Statement to check: Median experience is 5 years
median(df$experience)
## [1] 4
boxplot(df$experience, main = "Boxplot of Experience", ylab = "Years")
No, because the summary statistics and the boxplot show
that the median of experience is 4. If management’s
statement (“50% of the sales representatives have at least
five years of professional experience in sales”) were true,
then the median of experience should be 5.
An alternative and equally correct solution is to count
the observations that have less than 5 years of experience:
table(df$experience)
##
##  0  1  2  3  4  5  6  7  8  9 10
##  2  9 12 20 19 20  7  6  3  1  1
sum(df$experience >= 5) / nrow(df)
## [1] 0.18
barplot(table(df$experience), main = "Barplot of Experience", xlab = "Year
s", ylab = "Number of Sales Territories")
(d)
Is the management’s statement regarding the background
of their sales representatives correct? (2 points).
Solution
Statement to check: At least one-third of sales representatives hold an engineering degree.
table(df$engineer)
##
##  No Yes
##  72  28
barplot(table(df$engineer), main = "Barplot of Engineering", ylab = "Numbe
r of Sales Territories")
Management’s statement is incorrect because we only
observe that 28% of sales representatives hold an engineer -
ing degree, not at least 33%.
(e)
Does the advertising agency’s budget differ across the
sales territories? (2 points).
28
72 + 28 = 0.28 < 1 3 ≈ 33% .

214 B. Skiera, L. Jürgensmeier
Solution
summary(df$budget_agency)
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
##     329     838    1030    1028    1199    2056
hist(df$budget_agency, main = "Histogram of Budget Agency", xlab = "Budget
in $", ylab = "Number of Sales Territories")
Yes, the budgets differ. The summary statistics outline
that the minimum budget across all sales territories is
329, and the maximum is 2,056. Additionally, the histo-
gram shows that the budget varies strongly across sales
territories.
(f)
Did the advertising agency achieve the aim of approxi-
mately equally allocating the budget to the two channels
(telephone and social media marketing)? (2 points).
Solution
cor(df$budget_phone, df$budget_social_media)
## [1] 0.9910698
plot(df$budget_social_media, df$budget_phone, main = "Scatterplot of Budge
ts", xlab = "Social Media ($)", ylab = "Telephone ($)")
Yes, all sales territories received almost equal tele-
phone and social media marketing budgets. This insight
is easiest to observe in the scatterplot. The visualization
displays the almost perfect linear relationship and shows
that the social media budget approximately equals the
telephone marketing budget. The correlation coefficient
is almost 1, and both budgets’ average values are also
almost equal.
Note: Displaying the individual distributions of the two
variables, e.g., via a histogram, is insufficient because a
similar distribution of two variables is a necessary but
not a sufficient condition for similar budgets in all sales
territories.
(g)
Were the sales representatives born in at least 8 differ -
ent cities? (2 points).
barplot(table(df$location), main = "Barplot of Location", xlab = "Number o
f Characters in City Name", ylab = "Number of Sales Territories")
Solution
nrow(table(df$location))
## [1] 11
Yes, because the data set includes 11 different values of
location, which implies that the sales representatives
were born in at least 11 cities.
Step Task Max. Points Achieved
Points
1-a Correct visualization (1 point),
correct non-visual descriptive
statistic (1 point)
2
1-b see above 2
1-c see above 2
1-d see above 2
1-e see above 2
1-f see above 2
1-g see above 2

215
Teaching marketing analytics: a pricing case study for quantitative and substantive marketing…
Exercise (2): Estimating a demand function
Estimate a linear demand function. Justify which variables
you include and which ones you ignore. Discuss the influ-
ence of price and professional experience on the quantity
and how confident you are about their influence. (14 points).
Solution
Step 1: Identify the variables to include in the linear
regression equation.
Include all variables except:
• gender, because it only has the value 1 and, thus, no
variation.
• location, because there is no plausible reason why
the character length of the sales representative’s city of
birth should impact sales.
• budget_phone and budget_social_media,
because
– the two variables are almost perfectly collinear
(50% share each and correlation is almost 1), and
– the sum of both variables is a linear combi-
nation corresponding to the third variable
budget_agency, leading to perfect multi-
collinearity: budget_agency = budget_
phone + budget_social_media.
Step 2: Use a linear regression to estimate the linear
demand function.
Most Suitable Model
reg_model_1 <- lm(quantity ~ price + experience + engineer + budget_agency
, data = df)
Acceptable Models
reg_model_2 <- lm(quantity ~ price + experience + engineer + budget_phone,
data = df)
reg_model_3 <- lm(quantity ~ price + experience + engineer + budget_social
_media, data = df)
library(stargazer)
stargazer(reg_model_1, reg_model_2, reg_model_3, type = "text", header = F
ALSE)
##
## ====================================================================
##                                        Dependent variable:
##                               --------------------------------------
##                                              quantity
##                                   (1)          (2)          (3)
## --------------------------------------------------------------------
## price                          -2.953***    -2.951***    -2.955***
##                                 (0.038)      (0.038)      (0.038)
##
## experience                      9.039***     9.061***     9.023***
##                                 (0.663)      (0.659)      (0.669)
##
## engineerYes                      0.954        1.012        0.860
##                                 (2.972)      (2.956)      (2.990)
##
## budget_agency                   0.023***
##                                 (0.004)
##
## budget_phone                                 0.046***
##                                              (0.009)
##
## budget_social_media                                       0.044***
##                                                           (0.009)
##
## Constant                      1,215.966*** 1,215.042*** 1,217.175***
##                                 (13.124)     (13.090)     (13.161)
##
## --------------------------------------------------------------------
## Observations                      100          100          100
## R2                               0.985        0.986        0.985
## Adjusted R2                      0.985        0.985        0.985
## Residual Std. Error (df = 95)    12.868       12.803       12.948
## F Statistic (df = 4; 95)      1,609.366*** 1,626.051*** 1,589.121***
## ====================================================================
## Note:                                    *p<0.1; **p<0.05; ***p<0.01
Incorrect Models
# Including two out of three variables `budget_agency`, `budget_phone`, an
d `budget_social_media`
reg_model_4 <- lm(quantity ~ price + experience + engineer + budget_phone
+ budget_social_media,
data = df)
# Including all three multicollinear independent variables `budget_agency`
, `budget_phone`, and `budget_social_media`
reg_model_5 <- lm(quantity ~ price + experience + engineer + budget_agency
+ budget_phone + budget_social_media,
data = df)
stargazer(reg_model_4, reg_model_5, type = "text", header = FALSE, column.
labels = c("(4)", "(5)"), model.numbers = FALSE)
##
## ==========================================================
##                                   Dependent variable:
##                               ----------------------------
##                                         quantity
##                                    (4)            (5)
## ----------------------------------------------------------
## price                           -2.948***      -2.948***
##                                  (0.038)        (0.038)
##
## experience                       9.177***      9.177***
##                                  (0.665)        (0.665)
##
## engineerYes                       0.943          0.943
##                                  (2.950)        (2.950)
##
## budget_agency                                   -0.076
##                                                 (0.064)
##
## budget_phone                      0.120*         0.196
##                                  (0.063)        (0.127)
##
## budget_social_media               -0.076
##                                  (0.064)
##
## Constant                       1,214.119***  1,214.119***
##                                  (13.085)      (13.085)
##
## ----------------------------------------------------------
## Observations                       100            100
## R2                                0.986          0.986
## Adjusted R2                       0.985          0.985
## Residual Std. Error (df = 94)     12.775        12.775
## F Statistic (df = 5; 94)       1,306.717***  1,306.717***
## ==========================================================
## Note:                          *p<0.1; **p<0.05; ***p<0.01

216 B. Skiera, L. Jürgensmeier
Conceptual notes concerning model selection:
When deciding on the appropriate model for this exercise,
students need to consider three crucial factors to ensure a
correct estimation:
• Correctly defining a demand function: the defined
regression equation must feature quantity as the depend-
ent variable. Additionally, price and experience must
serve as independent variables to determine how they
impact the quantity.
• Omitted variable bias: failing to control for a variable
that correlates with the dependent and other independ-
ent variable(s) leads to biased coefficient estimates. For
example, omitting experience or one of the advertis-
ing budget variables could bias the coefficient estimate of
price if the omitted variable(s) correlate with price
and the dependent variable.
  However, this exercise introduces the simplifying
assumption of randomly set prices, thereby ruling out
endogenous prices through omitted variable bias. Ran-
domizing prices might be challenging to implement in
firms outside of narrow A/B tests. If the educator decides
to omit randomization of prices as a simplifying element
of the exercise, students must discuss the impact of endo-
geneity on the coefficient estimation and potential rem-
edies.
• Multicollinearity: Including at least two independent
variables that strongly correlate with each other can bias
those variables’ coefficient estimates. If this correlation
is very high, estimated coefficients might exhibit oppos-
ing signs, even though the actual effects would be in the
same direction. In an extreme case, including at least two
perfectly collinear variables leads to perfect collinearity,
which makes the regression estimation impossible due to
a less-than-full rank of the design matrix of all independ-
ent variables.
Model selection:
Model 1 is the preferred model according to the justifica-
tion from Step 1. In the incorrect model 4, we see the effects
of collinearity between the two variables budget_phone
and budget_social_media (as observed through their
correlation, which is very close to 1) on the estimated coeffi-
cients. The coefficients in model 4 have different signs, even
though the overall effect (model 1) and the effect of each
variable alone in models 2 and 3 are positive. Additionally,
the sum of the coefficients of the variables budget_phone
and budget_social_media in model 4 is similar in
magnitude to the total effect, i.e., the coefficient of the vari-
able budget_agency in model 1.
Step 3: Interpretation of Model 1.
If the price increases by $1, the (expected) quantity
decreases by 2.954 units.
For each additional year of work experience, the
(expected) quantity increases by 9.034 units.
Both coefficients display p -values smaller than 1%.
Hence, we are very confident for both coefficients that we
can reject the null hypothesis that the coefficient is not dif-
ferent from zero. Formulated differently, we are confident
that the estimated effect differs from zero.
Step Task Max. Points Achieved
Points
2–1 Correct justification of
which dependent and
independent variables
to include in the linear
regression
6
(6 Points for the cor-
rect model. 1 point
deduction for each
incorrectly included
or excluded variable.
0.5 points deduction
if the correct decision
but not justified.)
2–2 Estimate regression with
lm() and print
summary()
2
2–3 Interpret the estimated
coefficient of price
correctly
3
(1.5 points for magni-
tude and statistical
significance, each)
2–4 Interpret the estimated
coefficient of expe-
rience correctly
3
(1.5 points for magni-
tude and statistical
significance, each)
Exercise (3): Compute advertising and price
elasticities of demand
Use your model to compute the price elasticity of demand
and the (advertising) budget elasticity of demand. Interpret
these elasticities and assess whether your computed elastici-
ties are consistent with economic intuition. (12 Points).
Solution
First, note that elasticities in a linear demand model are
not constant. Hence, the elasticity depends on the independ-
ent variable’s value. Students must pick a sensible value for
both variables to compute the elasticities (advertising budget
and price). A good choice would be to select the average
values.
elasticity_budget <- coefficients(reg_model_1)["budget_agency"] * mean(df$
budget_agency) / mean(df$quantity)
elasticity_budget
## budget_agency
##    0.05974684
elasticity_price <- coefficients(reg_model_1)["price"] * mean(df$price) /
mean(df$quantity)
elasticity_price
##     price
## -2.286785

217
Teaching marketing analytics: a pricing case study for quantitative and substantive marketing…
Interpretation of the elasticities:
At the average budget, a 1% increase in advertising budget
yields a 0.06% increase in demand. Thus, the value of the
advertising elasticity is 0.06. A positive advertising elastic-
ity makes economic sense because more advertising should
yield higher demand. The value is low but broadly in line
with findings from meta-analytical studies (e.g., Sethuraman
et al. 2011: 0.11).
At the average price, a 1% increase in price yields a 2.29%
decrease in demand. So, the value of the price elasticity is
− 2.29. The size of this value is plausible because a higher
price yields a lower demand. The value also aligns with find-
ings from meta-analytical studies (e.g., Tellis 1988: − 1.76;
Bijmolt et al. 2005: − 2.62).
Step Task Max.
Points
Achieved
Points
3–1 Mentioning that elasticities from a lin-
ear demand function are not constant
2
3–2 Sensible choice of values at which to
compute the elasticities (e.g., mean,
median, profit-maximizing value)
2
3–3 Correct computation of the two elas-
ticities
4
3–4 Correct interpretation of the two com-
puted elasticities
2
3–4 Correct evaluation of the two computed
elasticities’ plausibility
2
Exercise (4): Determine the optimal price
A sales representative with three years of professional expe-
rience and an engineering degree operates in a sales terri-
tory. In addition, the advertising agency spends a budget of
$2,000, allocating 50% to telephone and 50% to social media
marketing. Determine the optimal price in this setting and
explain the steps you take to arrive at your result. Assume
fixed costs of zero. What is the contribution margin per unit
and the firm’s profit? (20 points).
Solution
Step 1: Write the demand function with regression coef-
ficients from the most preferred model.
Notation ( equation/code):
• q/q: quantity sold
• qc/q_c: quantity sold without price term, constant
• p/p: price
• cv/c_v: variable costs
/uni0302.s1q = /uni0302.s1𝛽0 + /uni0302.s1𝛽1 ⋅ p + /uni0302.s1𝛽2 ⋅ experience
+ /uni0302.s1𝛽3 ⋅ engineer + /uni0302.s1𝛽4 ⋅ budget_agency
where /uni0302.s1q is the (expected value of) quantity.
/uni0302.s1qc is the expected quantity without considering the price
term:
Step 2: Compute /uni0302.s1qc , the expected quantity without the
impact of the price.
coef <- coefficients(reg_model_1)
q_c <- coef["(Intercept)"] + coef["experience"] * 3 + coef["engineerYes"]
* 1 + coef["budget_agency"] * 2000
Step 3: Set up the cost and profit functions.
Cost function
Profit function
Step 4: Take the first derivative of the profit function
with respect to p and set it equal to zero
Step 5: Rearrange the function to get the optimal price p∗
Step 6: Compute the optimal price by inserting the
computed values from the above steps.
c_v <- 200
p_star <- 0.5 * (c_v - (q_c / coef["price"]))
p_star
## (Intercept)
##     318.268
Step 7: Compute the profit contribution per unit.
profit_contribution_unit <- p_star - c_v
profit_contribution_unit
## (Intercept)
##     118.268
Step 8: Compute the (total) profit.
/uni0302.s1q = /uni0302.s1qc + /uni0302.s1𝛽1 ⋅ p
/uni0302.s1qc = /uni0302.s1𝛽0 + /uni0302.s1𝛽2 ⋅ experience + /uni0302.s1𝛽3 ⋅ engineer + /uni0302.s1𝛽4 ⋅ budget_agency
c/parenleft.s1/uni0302.s1q/parenright.s1 = cv ⋅ /uni0302.s1q = cv ⋅ /parenleft.s2 /uni0302.s1qc + /uni0302.s1𝛽1 ⋅ p /parenright.s2
𝜋 = p ⋅ /uni0302.s1q − c/parenleft.s1/uni0302.s1q/parenright.s1 = p ⋅ /parenleft.s2 /uni0302.s1qc + /uni0302.s1𝛽1 ⋅ p /parenright.s2 − /bracketleft.s2 cv ⋅ /parenleft.s2 /uni0302.s1qc + /uni0302.s1𝛽1 ⋅ p /parenright.s2/bracketright.s2
= p/uni0302.s1qc + p2 /uni0302.s1𝛽1 − cv/uni0302.s1qc − cv /uni0302.s1𝛽1p
𝜕𝜋
𝜕p = /uni0302.s1qc + 2p /uni0302.s1𝛽1 − cv /uni0302.s1𝛽1 = 0
p∗ = 1 2
/parenleft.s4
cv − /uni0302.s1qc /uni0302.s1𝛽1
/parenright.s4

218 B. Skiera, L. Jürgensmeier
q_star <- q_c + coef["price"] * p_star
profit_total <- q_star * profit_contribution_unit
The optimal price is $318.27. The profit contribution
per unit amounts to $118.27. The firm sells 349 units of
the heater fan, yielding a profit of $41,305.69.
Step Task Max.
Points
Achieved
Points
4–1 Description: Set up demand
function with regression
coefficients
2
4–2 Description: Constant demand
/uni0302.s1qc includes all terms from
the regression equation,
excluding the price term
2
4–3 Description: Set up the profit
function and insert the
demand function into the
profit function
2
4–4 Description: Take the first
derivative of the profit func-
tion with respect to p and set
it equal to zero
2
4–5 Description: Rearrange and
solve for the optimal price
p∗
2
4–6 State the correct formula for
the optimal price
2
4–7 Compute the expected quan-
tity (constant) without the
price term correctly
2
4–8 Compute the optimal price
correctly
2
4–9 Compute the profit contribu-
tion per unit correctly
2
4–10 Compute the firm’s profit
correctly
2
Exercise (5): Impact of changes on optimal prices
Answer the following two sub-questions by ticking the cor-
rect answer.
(a)
How does the optimal price change if a sales representa-
tive without an engineering degree works in the sales ter -
ritory instead of a sales representative with an engineering
degree? (2 points).
The optimal price…
• increases
• decreases
• remains about the same
• no statement possible
Solution
The optimal price remains about the same.
Explanation (not required):
Changes in the regression parameter of engineerYes
cause a parallel shift of the demand curve (upwards if pos-
itive, downwards if negative) or leave the demand curve
unaffected if it is statistically insignificantly different from
zero.
In our case, the parameter estimate of engineerYes
is statistically insignificantly different from zero. Hence, we
can expect that the demand curve does not change much,
implying that the optimal price remains the same.
The following computation of the optimal price for a sales
representative without an engineering degree supports this
claim:
q_c_no_engineer <- coef["(Intercept)"] + coef["experience"] * 3 + coef["bu
dget_agency"] * 2000
p_star_no_engineer <- 0.5 * (c_v - (q_c_no_engineer / coef["price"]))
compared to the optimal price with an engineering degree.
p_star
## (Intercept)
##     318.268
p_star_no_engineer
## (Intercept)
##    318.1064
p_star - p_star_no_engineer
## (Intercept)
##   0.1615698
The optimal price of a sales representative without an
engineering degree is $318.11, and with an engineering
degree is $318.27. The price difference is only $0.16.
Conclusion: The magnitude of the difference between
the two optimal prices is very small and statistically insig-
nificantly different from zero ( p > 0.1 ). Hence, the optimal
price remains about the same.
(b)
How does the optimal price change if a sales representa-
tive with only one year of professional experience works in
the sales territory instead of a sales representative with three
years of professional experience? (2 points).
The optimal price…
• increases
• decreases
• remains about the same
• no statement possible
Solution
The optimal price decreases.
Explanation (not required):

219
Teaching marketing analytics: a pricing case study for quantitative and substantive marketing…
Similar to the above exercise, we must consider how the
demand function changes. The demand function changes
significantly because the experience regression param-
eter is statistically significantly positive.
Hence, a decrease in the level of experience from 3 to 1
(= -2) years causes a parallel downward shift of the demand
function. This change leads to lower demand. Thus, the opti-
mal price decreases.
The following computation of the optimal price with one
year of experience supports this claim.
q_c_one_year_experience <- coef["(Intercept)"] + coef["experience"] * 1 +
coef["engineerYes"] * 1 +
  coef["budget_agency"] * 2000
p_star_one_year_experience <- 0.5 * (c_v - (q_c_one_year_experience / coef
["price"]))
compared with the optimal price with three years of
experience:
p_star
## (Intercept)
##     318.268
p_star_one_year_experience
## (Intercept)
##    315.2073
p_star_one_year_experience - p_star
## (Intercept)
##   -3.060719
The optimal price of a sales representative with a one-
year experience is $315.21, and with a three-year experi-
ence, $318.27. So, the price decreases ($-3.06).
Conclusion: the optimal price decreases by $-3.06, in line
with the expectation, because the coefficient on the variable
experience is statistically significantly different from
zero ( p < 0.01).
Step Task Max. Points Achieved Points
5-a Correct answer 2
5-b Correct answer 2
Exercise (6): Marketing budget allocation
The management wants to know whether it should spend the
marketing budget on telephone marketing or social media
marketing. Which recommendation can you give based on
your analyses? (2 points).
Solution
In this case, no recommendation is possible because the
firm always allocated 50% of the budget to telephone mar -
keting and 50% to social media marketing in each sales terri-
tory. Hence, the two budget variables, budget_phone and
budget_social_media, are almost perfectly collinear,
making the correct estimation of each variable’s effect on the
quantity sold impossible.
Step Task Max. Points Achieved Points
6 Correct answer 2
Exercise (7): Performance and compensation of sales
representatives
(a)
Do female sales representatives sell more than non-female
sales representatives? (2 points).
Answer this question based on your previous results.
Solution
No answer is possible because the data set only includes
female sales representatives.
(b)
Do business outcomes justify paying sales representa-
tives with an engineering degree a higher salary than those
without an engineering degree? (2 points).
Answer this question based on your previous results.
Solution
No, because the expected sold quantity does not differ
whether a person holds an engineering degree (see engi-
neerYes). While the estimated coefficient is positive, it is
not statistically significantly different from zero ( p > 0.1 ).
So, we do not expect a substantial increase in the quantity
sold that justifies a higher salary for sales representatives
with an engineering degree.
Decrease in estimated sales without an engineering
degree:
- coef["engineerYes"]
## engineerYes
##  -0.9542576
Decrease of profit:
- coef["engineerYes"] * profit_contribution_unit
## engineerYes
##   -112.8581
The profit decreases by $− 112.86. However, this effect
is very small compared to the profit of $41,305.69. Addi-
tionally, the coefficient estimate of engineerYes is not
statistically significantly different from zero ( p > 0.1).
(c)
Do business outcomes justify paying sales representatives
with more professional experience a higher salary than those
with less professional experience? (2 points).
Answer this question based on your previous results.

220 B. Skiera, L. Jürgensmeier
Solution
Yes, because the expected quantity increases by 9.04 units
for each additional year of experience. The profit contri-
bution per unit is $118.27, so 9.04 additionally sold units
increase the profit by $1,068.97 (= 9.04 * $118.27).
Additionally, the estimated coefficient on the variable
experience is statistically significantly different from
zero ( p < 0.01 ). So, we expect a substantial decrease in the
quantity sold that justifies a lower (higher) salary for sales
representatives with less (more) experience.
Step Task Max. Points Achieved
Points
7-a Correct answer, stating
that no conclusion is
possible
2
7-b Correct answer, including
stating that the coeffi-
cient is not statistically
significantly different
from zero
2
(0.5 points
deduction if
no level of
significance is
defined)
7-c Correct conclusion based
on regression estimates
2
Discussion of the case study’s
implementation
Description of target audience and requirements
Previous course requirements
The present case study aims at students starting from second-
year undergraduates with a basic understanding of statistics
and econometrics (e.g., through first-year statistics or econo-
metrics courses) and marketing (e.g., an introductory market-
ing course). Additionally, the case study requires the funda-
mental calculus skill of taking the first derivative of a profit
function and solving for the optimal price. Students typically
learn such skills in an introductory microeconomics course.
Software requirements
To complete this case study, students need to be familiar
with the R programming language (R Core Team 2023) or
another similar statistical programming language such as
Python or Stata. In our solution using R, we use “Base R,”
i.e., the core functionalities of the R language available with-
out installing additional packages.
The only exception used in the solution is the package
stargazer, which conveniently creates regression tables
for multiple model specifications (Hlavac 2022). Using this
package makes a quick model comparison feasible.
If educators focus less on the calculus requirement of the
optimal pricing decision, symbolic programming packages
could provide a shortcut, making the case study accessible
for students without taking the first derivative. One such
package is calculus (Guidotti 2022). For example, stu-
dents can take the first derivative of the profit function from
Exercise 4,
with the following R code:
library(calculus)
derivative(
f = "p * q_c + p^2 * b_1 - c_v * q_c - c_v * b_1 * p",
var = "p"
)
## [1] "q_c + 2 * p * b_1 - c_v * b_1"
Scope of the case study
In this case study, students learn to handle threats to a cor -
rect estimation of coefficient estimates in linear regression
analysis and understand how those apply when estimating
a demand function. This case study assesses three critical
factors when estimating a demand function:
• Correctly defining a demand function,
• considering omitted variable bias as one source for endo-
geneity,
• multicollinearity as a reason for biased coefficient esti-
mates.
Beyond ensuring that students select the correct variables
from the data set, we avoid assessing students’ comprehension
of endogeneity problems when estimating demand as a func-
tion of prices by outlining that management randomly sets
prices. Random variation enables us to estimate the causal
effect easily. While such a pricing setting can occur in the
context of A/B tests or larger experimental studies, it might
not be too realistic. However, this shortcut enables us to derive
an easier case study that focuses on data-driven pricing, i.e.,
turning statistical insights into pricing decisions. If the cor -
responding course discusses endogeneity in detail, educators
can drop the simplifying assumption of random prices.
While we do not focus on endogeneity, we assess stu-
dents’ understanding of another potential threat to the unbi-
ased identification of demand function parameters: multicol-
linearity. While students sometimes perceive the problem
and consequences of multicollinearity as theoretical and
𝜋 = p ⋅ ̂q − c(̂q)
= p ⋅ /parenleft.s1̂qc + ̂𝛽1 ⋅ p/parenright.s1 − /bracketleft.s1cv ⋅ /parenleft.s1̂qc + ̂𝛽1 ⋅ p/parenright.s1/bracketright.s1
= p̂qc + p2 ̂𝛽1 − cv ̂qc − cv ̂𝛽1p

221
Teaching marketing analytics: a pricing case study for quantitative and substantive marketing…
abstract, our setting outlines a marketing scenario that will
likely occur in practice.
Students must critically assess the included variables in
the data set and disregard a set of variables being highly
or even perfectly collinear to other potential independent
variables. However, a simple look at correlations between
independent variables is not enough in this setting—students
have to combine their econometric understanding of collin-
earity with economic intuition.
In our case, two advertising channels receive almost, but
not strictly equal, budgets. The sum of those two budgets
yields the total budget. Students must first identify that the for-
mer two variables add to the latter variable, thus facing perfect
collinearity when including all three variables. Secondly, stu-
dents should identify that the two budget variables correlate
highly but not perfectly. As highlighted in the incorrect model
specifications, this high correlation leads to severe multicol-
linearity—producing opposite-sign coefficient estimates for
the impact of advertising on sales—while the individual (and
correct) inclusion of only one budget variable always yields
a positive estimate. Third, students should understand why
multicollinearity occurs in many settings. For example, the
management’s request to split the budget 50:50 is a request
that could easily occur in a real-world setting.
Corresponding marketing analytics class
The preceding marketing analytics class teaches students
how to use a statistical programming language—in our
case, R, but software such as Python or Stata works equally
well—to analyze data and turn these results into marketing
decisions.
This class focuses on an experiential and active learning
approach that prioritizes students “getting their hands dirty.”
That means we provide ample time and case studies in class
for students to apply the econometric techniques themselves,
interpret the econometric results in a managerially relevant
way, and critically discuss the results in students’ small peer
groups and larger class conversations.
We structure the proposed case study and the associ-
ated marketing analytics class in a way that initially leads
students, most with only basic econometric or statistical
programming experience, to lose potentially existing fear
of statistics or programming quickly. Hence, we prioritize
interactive learning opportunities through in-class case stud-
ies with readily available teaching staff for questions. By
quickly and individually giving feedback, the instructors can
lead the student groups to quick results and instill a positive
“can do” mentality, which is critical for learning new quan-
titative techniques that students often perceive as difficult.
Discussion questions for educators
Table 2 provides educators with initial questions to lead a
classroom discussion about the case study. Those questions
should prompt the students to solve the case study success-
fully. In addition, the questions aim to induce students to
think about how and under which circumstances they can
transfer the case study’s methods to other scenarios.
Table 2  Teaching questions by topic
Topic Questions
Avoiding Endogeneous Prices • Discuss how random variation in prices across territories enables the firm to estimate the
optimal price
• What could be the problem if the prices are non-random?
• Discuss how different types of firms could vary their prices without alienating customers
but still being able to estimate the optimal price
Multicollinearity • What is multicollinearity, to which problem does it lead when estimating regressions, and
why and when could it occur?
• How do you avoid that your analysis suffers from multicollinearity?
Price and advertising elasticities of demand • Describe what price and advertising elasticities measure
• How do the values of the two elasticities differ?
• What are plausible ranges for the two elasticities’ values?
• How does knowing elasticities help with managerial decision-making?
• Particularly, how do those two elasticities contribute to optimal pricing?
Translating regression coefficients into elasticities • When using a linear regression model to estimate demand as a function of price, how can
we interpret the price coefficient?
• Which additional information do we need to translate this coefficient into the price elastic-
ity of demand?
• Does a higher (absolute) value of the price coefficient yield a higher or lower price elas-
ticity?

222 B. Skiera, L. Jürgensmeier
Application and results of the case study
as an exam exercise
Setup of the exam
We initially developed and applied the case study as a
computer-based final exam for second to third-year under -
graduate students in business and economics. The course
is a mandatory marketing analytics class for undergradu -
ates majoring in “Management and Marketing” at a large
public university. During the semester, students obtained
substantive marketing and analytics (econometrics) skills
corresponding to the learning goals in Table  1. The pre-
sented exercise matches some of a quantitative marketing
analyst’s most essential expected skills. Hence, we ensure
the constructive alignment of the exercise to what students
can expect once they graduate.
The final exam was administered in the year 2023 to 134
students at the end of the course. We used a computer class-
room with all necessary software pre-installed to ensure a
controlled exam setting and equal opportunity, irrespective
of student hardware. Consistent with the course’s learning
goals, we intended to avoid students having to memorize
easily accessible information, such as specific code snip-
pets or function names for statistical procedures. Hence, the
exam mode is “open book,” allowing students to reference
all physical and digital materials, such as pre-existing R
codes from the preceding class. Exam supervisors ensured
that no communication among students took place. Students
then had 60 min to solve the exam question. The exercise
discussed in this article was part of a 90-min exam that con-
tained an additional (smaller) exercise.
Demographic characteristics of the students
This subsection discusses which students took the exam.
The examination office strictly anonymizes student data, so
we only obtained a student identifier without the student’s
name or demographic characteristic. Hence, we cannot make
a precise statement about the demographics of students in
this exam cohort.
However, course evaluations (N = 24) taken before the
exam suggest that 50 – 60% of the students in the corre-
sponding class are female, and the age distribution centers
around 21 – 22 years. Approximately nine out of ten students
enroll in a business and economics undergraduate degree,
with the remainder taking the course as part of a business
minor in another degree, such as (business) pedagogy or
other social sciences. Students majoring in business and
economics have passed introductory statistics, mathemat-
ics, microeconomics, and marketing courses before being
able to enroll in this marketing analytics course and have
completed at least three semesters. Most students attended it
in their fourth or fifth semester of an undergraduate program
scheduled for completion in six semesters. Nevertheless, a
few students attended the course later than the fifth semester,
in line with the observation that many students require more
than six semesters to finish their studies.
Results of the exam
Figure 1 visualizes the distribution of achieved points from
the 134 exam submissions. The student performance approx-
imately follows a normal distribution around the mean
achieved points of 27.2 and a standard deviation of 11.1
points. The average student correctly solved 27.2/60 = 45.3%
of the exam. The minimum achieved points were 0 (some
students prefer to fail the exam instead of getting a bad pass-
ing grade, so there is an incentive to submit an empty solu-
tion). The best-performing student achieved 57.5 out of 60
points.
Figure  2 displays the distribution of the student per -
formance by sub-exercise. This visualization serves as a
proxy for a sub-exercise’s difficulty—the lower the share of
achieved points relative to the achievable points, the more
difficult the sub-exercise was to solve for the students.
Ranking the sub-exercises by this metric yields that
students performed best in Exercise 2, which estimated
a demand function through a regression. The most chal-
lenging was Exercise 6, which required students to decide
on the optimal budget allocation under multicollinearity.
However, the share of achieved points is only an imper -
fect measure of difficulty since all sub-exercises appeared
chronologically for all students. Hence, students might
have had less time to solve the sub-exercises towards the
end of the exam.
Fig. 1  Distribution of student performance for the exercise in an
exam setting (N = 134)

223
Teaching marketing analytics: a pricing case study for quantitative and substantive marketing…
Discussion of the applicability as an exam
and implications for other settings
The significant variation in Fig. 2’s distributions shows that
our case study’s sub-exercises exhibit various degrees of
difficulty, enabling the educator to assess students’ perfor -
mance very granularly.
Nevertheless, the comparatively low average number of
achieved points (27.2/60 = 45.3%) shows that it is challeng-
ing for the given student population to solve the full exer -
cise correctly in 60 min. Still, the occasional almost perfect
scores show that very strong students can solve the full exer-
cise correctly within 60 min. Hence, we conclude that the
exercise is well-calibrated to measure varying degrees of
student performance.
These results from using the exercise as an exam hold
implications for other settings earlier in the student’s learn-
ing journey, such as take-home or in-class case study
assignments.
First, students need sufficient time to work on the exer -
cises. Assuming a lower familiarity with the subject than
students writing an exam, we recommend that students
in a take-home case study or in-class group work have at
least 120 min to solve the case study as part of a learning
experience.
Second, the exam results show in which sub-exercises
students struggle to find the correct solution. Exercise 6
(marketing budget allocation under high multicollinearity)
and Exercise 4 (determining the optimal price) were the
most challenging parts of the case study. Hence, it might be
sensible for educators to spend most of their time discussing
those sub-exercises and the underlying concepts.
While our analysis shows the promise of the case study
in teaching and assessing marketing analytics, this analy -
sis cannot comment on whether this case study is optimal
such that it maximizes student learning. This article aims to
make this case study freely available to educators as a first
step in improving learning outcomes in marketing analytics.
Hence, we encourage further research comparing our case
study’s efficacy to other teaching and assessment approaches
in marketing analytics.
Fig. 2  Distribution of student performance by sub-exercise. Note: Due to the exam’s time constraints, the implemented exam consisted of all dis-
cussed sub-exercises except for Exercise 3 (Price Elasticity). Hence, we present the empirical results from all but this sub-exercise

224 B. Skiera, L. Jürgensmeier
Summary
This article described a case study to teach or assess mar -
keting analytics skills. The presented case study combines
substantive marketing skills with econometric methods,
conveying how data-driven marketing can create value for
firms and enable better decision-making. Through accessing
our open-source repository, marketing educators can use this
case study, its solution, and the accompanying data (acces-
sible via https:// github. com/ lukas- jue/ marke ting- analy tics-
exerc ise) as a template for in-class group work, homework,
or computer-based exams.
Appendix: Description of the case study
(excluding the solution)
Your B2B firm sells an energy-efficient heater fan and has
divided the country into 100 comparable sales territories,
each staffed exclusively by a female sales representative. The
sales representatives differ according to their professional
experience (measured by the number of years they have been
in sales) and whether they have an engineering degree.
The management recently stated that 50% of the sales
representatives have at least five years of professional expe-
rience in sales, and at least one-third of the sales representa-
tives also have an engineering degree.
The firm’s management randomly varied the prices across
the sales territories.
In addition, the management commissioned an adver -
tising agency to support the sales representatives through
marketing and provided a dedicated budget. The agency
should use this marketing budget for telephone marketing
and social media marketing, with an approximately equal
allocation towards the two channels (i.e., 50% phone calls
and 50% social media marketing). So far, the firm’s man-
agement has randomly varied the agency’s budget across
the sales territories.
The variable cost per unit of a heater fan is $200.
In the file data_sales.csv, you receive informa -
tion that helps you answer the questions. The data set
includes 100 rows, each describing one of the 100 sales
territories with the following variables:
Table: Description of the data set data_sales.csv
Variable Description
quantity Number of sold heater fans in the
respective sales territory
price Price of the heater fan sold in the
respective sales territory
Variable Description
experience Number of years the sales repre-
sentative has been working in
sales
engineer Binary variable indicating whether
the sales representative has an
engineering degree (= 1) or not
(= 0)
gender Gender of the sales representative,
female (= 1) or other (= 0)
location Number of letters of the sales rep-
resentative’s birthplace (e.g., 7 if
the birthplace is “Chicago”)
budget_agency Budget used by the advertising
agency, which is either spent for
phone or social media market-
ing, in $
budget_phone Budget used for telephone market-
ing, in $
budget_social_media Budget used for social media
marketing, in $
(1) Exploratory data analysis
For each part of this first exercise, please answer the
question by analyzing the data set through one visualiza-
tion and one non-visual descriptive analysis.
We do not require custom labels for the visualizations.
(a)
Does the firm only employ female sales representatives?
(2 points).
(b)
Do the prices differ across sales territories? (2 points).
(c)
Is the management’s statement regarding the profes-
sional experience of their sales representatives correct?
(2 points).
(d)
Is the management’s statement regarding the background
of their sales representatives correct? (2 points).
(e)
Does the advertising agency’s budget differ across the
sales territories? (2 points).
(f)
Did the advertising agency achieve the aim of approxi-
mately equally allocating the budget to the two channels
(telephone and social media marketing)? (2 points).
(g)
Were the sales representatives born in at least 8 different
cities? (2 points).
(2) Estimating a demand function
Estimate a linear demand function. Justify which vari-
ables you include and which ones you ignore. Discuss the
influence of price and professional experience on the quan-
tity and how confident you are about their influence. (14
points).

225
Teaching marketing analytics: a pricing case study for quantitative and substantive marketing…
(3) Compute advertising and price elasticities of demand
Use your model to compute the price elasticity of demand
and the (advertising) budget elasticity of demand. Interpret
these elasticities and assess whether your computed elastici-
ties are consistent with economic intuition. (12 Points).
(4) Determine the optimal price
A sales representative with three years of professional
experience and an engineering degree operates in a sales ter-
ritory. In addition, the advertising agency spends a budget of
$2,000, allocating 50% to telephone and 50% to social media
marketing. Determine the optimal price in this setting and
explain the steps you take to arrive at your result. Assume
fixed costs of zero. What is the contribution margin per unit
and the firm’s profit? (20 points).
(5) Impact of changes on optimal prices
Answer the following two sub-questions by ticking the
correct answer.
(a)
How does the optimal price change if a sales representa-
tive without an engineering degree works in the sales ter -
ritory instead of a sales representative with an engineering
degree? (2 points).
The optimal price…
• increases
• decreases
• remains about the same
• no statement possible
(b)
How does the optimal price change if a sales representa-
tive with only one year of professional experience works in
the sales territory instead of a sales representative with three
years of professional experience? (2 points).
The optimal price…
• increases
• decreases
• remains about the same
• no statement possible
(6) Marketing budget allocation
The management wants to know whether it should spend
the marketing budget on telephone marketing or social
media marketing. Which recommendation can you give
based on your analyses? (2 points).
(7) Performance and compensation of sales representatives
(a)
Do female sales representatives sell more than non-female
sales representatives? (2 points).
Answer this question based on your previous results.
(b)
Do business outcomes justify paying sales representa-
tives with an engineering degree a higher salary than those
without an engineering degree? (2 points).
Answer this question based on your previous results.
(c)
Do business outcomes justify paying sales representatives
with more professional experience a higher salary than those
with less professional experience? (2 points).
Answer this question based on your previous results.
Acknowledgements We thank Timo Müller-Tribbensee for valuable
comments on this case study.
Funding Open Access funding enabled and organized by Projekt
DEAL.
Data availability The authors provide the case study’s data, simulation
codes, exercise templates, and solutions in the accompanying GitHub
repository: https:// github. com/ lukas- jue/ marke ting- analy tics- exerc ise
Declarations
Conflict of interest On behalf of all authors, the corresponding author
states that there is no conflict of interest.
Open Access This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source,
provide a link to the Creative Commons licence, and indicate if changes
were made. The images or other third party material in this article are
included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in
the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will
need to obtain permission directly from the copyright holder. To view a
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
Biggs, John. 1996. Enhancing Teaching Through Constructive Align-
ment. Higher Education 32 (3): 347–364.
Bijmolt, Tammo H.A.., Harald J. Van Heerde, and Rik G.M.. Pieters.
2005. New Empirical Generalizations on the Determinants of
Price Elasticity. Journal of Marketing Research 42 (2): 141–156.
DeMars, Christine. 2010. Item Response Theory. Oxford: Oxford Uni-
versity Press.
Guidotti, Emanuele. 2022. calculus: High-Dimensional Numerical
and Symbolic Calculus in R. Journal of Statistical Software 104:
1–37.
Hlavac, Marek. 2022. stargazer: Well-Formatted Regression and Sum-
mary Statistics Tables. https:// cran.r- proje ct. org/ web/ packa ges/
starg azer/ index. html. Accessed 8 Nov 2023.
Iacobucci, Dawn, Maria Petrescu, Anjala Krishen, and Michael Ben-
dixen. 2019. The State of Marketing Analytics in Research and
Practice. Journal of Marketing Analytics 7 (3): 152–181.
Kotler, Philip, Gary Armstrong, Lloyd C. Harris, and Hongwei He.
2019. Principles of Marketing. London: Pearson.
Mizik, Natalie, and Dominique M. Hanssens. 2018. Handbook of
Marketing Analytics: Methods and Applications in Marketing

226 B. Skiera, L. Jürgensmeier
Management, Public Policy, and Litigation Support. Cheltenham:
Edward Elgar Publishing.
Montano, S., L. Gill-Simmen, D. Lee, L. Walsh, D. Duffy, and N.
Newman. forthcoming. Assessing Authentically—Learnings from
Marketing Educators. Journal of Marketing Management.
Peter, J. Paul. 1981. Construct Validity: A Review of Basic Issues
and Marketing Practices. Journal of Marketing Research 18 (2):
133–145.
Petrescu, Maria, and Anjala S. Krishen. 2018. Novel Retail Technolo-
gies and Marketing Analytics. Journal of Marketing Analytics 6
(3): 69–71.
R Core Team. 2023. R: A Language and Environment for Statistical
Computing. R Foundation for Statistical Computing, Vienna, Aus-
tria. https:// www.r- proje ct. org/. Accessed 10 Nov 2023.
Sethuraman, Raj, Gerard J. Tellis, and Richard A. Briesch. 2011.
How Well Does Advertising Work? Generalizations from Meta-
Analysis of Brand Advertising Elasticities. Journal of Marketing
Research 48 (3): 457–471.
Stock, James H., and Mark W. Watson. 2019. Introduction to Econo-
metrics. London: Pearson.
Tellis, Gerard J. 1988. Advertising Exposure, Loyalty, and Brand
Purchase: A Two-Stage Model of Choice. Journal of Marketing
Research 25 (2): 134–144.
Van Auken, Stuart. 2015. From Consumer Panels to Big Data: An
Overview on Marketing Data Development. Journal of Marketing
Analytics 3 (1): 38–45.
Wedel, Michel, and P.K. Kannan. 2016. Marketing Analytics for Data-
Rich Environments. Journal of Marketing 80 (6): 97–121.
Wooldridge, Jeffrey M. 2013. Introductory Econometrics: A Modern
Approach. Boston: Cengage Learning.
Publisher's Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional affiliations.
Bernd Skiera is a chaired professor of electronic commerce at Goethe
University Frankfurt, Germany and a Professorial Research Fellow at
Deakin University, Australia. His research interests are Marketing Ana-
lytics, Data-driven Marketing, Electronic Commerce, Online Advertis-
ing, Marketing Automation, and Consumer Privacy. Bernd Skiera’s
publications appeared in Marketing Science, Journal of Marketing
Research, Journal of Marketing, and Management Science. His articles
have received numerous awards, including the Sheth Foundation/Jour-
nal of Marketing Award for the best Journal of Marketing article with
long-term contributions and the AMA/Marketing Science Institute/H.
Paul Root Award. Through an ERC Advanced Grant, he and his group
currently conduct research on the economic consequences of online
consumer privacy.
Lukas Jürgensmeier is a Ph.D. student in Quantitative Marketing at
Goethe University Frankfurt. His research focuses on the interface
between Data Science and Marketing and applies econometric meth-
ods to novel data sources in the digital economy. Lukas Jürgensmeier
is the winner of the 2023 ISMS Dissertation Award for his disserta -
tion proposal “Measuring Fair Competition.” He currently serves as a
supervisory board member (previously executive board member) of
“TechAcademy,” an award-winning non-profit organization teaching
coding to students.
