---
title: Brand Logos Recognition System Using Image Processing for Food and Beverage Brands
url: https://doi.org/10.36079/lamintang.jetas-0603.768
category: analytics
subcategory: empirical
date: 2024-12
venue: Journal of Engineering Technology and Applied Science (JETAS)
authors:
- A. Roslan
- Ahmad Fadli Saad
source: openalex-oa
pdf_url: https://lamintang.org/journal/index.php/jetas/article/download/768/527
pages: 11
chars: 37132
fetched_at: '2026-11-08T17:19:51+00:00'
kb_version: 1
---

# Brand Logos Recognition System Using Image Processing for Food and Beverage Brands

2024 | Journal of Engineering, Technology & Applied Science | Volume. 6 | Issue. 3 | 167-177

Journal of Engineering, Technology & Applied Science
p-ISSN: 2721-7949, e-ISSN: 2721-8090
Original Research Paper

Brand Logos Recognition System Using Image Processing for Food and
Beverage Brands

Aini Khadijah Mohamad Roslan1, Ahmad Fadli Saad1*

1 Computing Science Studies, College of Computing, Informatics and Media, Universiti
Teknologi MARA. Perak Branch, Tapah Campus. Perak, Malaysia.

Article History
Received:
17.11.2024

Revised:
04.12.2024

Accepted:
19.12.2024

*Corresponding Author:
Ahmad Fadli Saad
Email:
afadlis@uitm.edu.my

This is an open access article,
licensed under: CC–BY-SA

Abstract: This study investigates the development of a Brand Logo
Recognition (BLR) system employing Convolutional Neural Networks
(CNNs), specifically designed for the food and beverage industry in Ipoh.
Accurate logo recognition is vital for businesses to strengthen brand identity,
monitor consumer engagement, and mitigate the misuse of counterfeit logos.
Existing systems often encounter challenges related to variations in logo
design, image quality, and lighting conditions. To address these issues, the
research adopts a hybrid methodology that integrates the Machine Learning
Life Cycle and the Software Development Life Cycle (SDLC), utilizing an
iterative Agile development framework. The system incorporates CNN models
for feature extraction and classification, complemented by Single Shot
Detector (SSD) algorithms for object detection. A curated dataset of food and
beverage logos underwent preprocessing techniques, including resizing,
normalization, and augmentation, to enhance the model’s generalization
capabilities. Empirical results demonstrate high accuracy in detecting and
classifying logos across diverse conditions, underscoring the effectiveness of
the CNN-SSD architecture. The proposed system offers practical applications
for marketing analytics and consumer research, empowering local businesses
to refine branding strategies and improve customer engagement. Future
research directions include the exploration of multi-label classification, real-
time processing, and the integration of advanced methodologies, such as
generative adversarial networks (GANs), for counterfeit logo detection. This
study emphasizes the transformative potential of AI-driven logo recognition
systems in revolutionizing marketing practices and supporting small and
medium-sized enterprises (SMEs).

Keywords: Brand Logo Recognition, Convolutional Neural Networks, Deep
Learning, Image Processing, Machine Learning.

Aini Khadijah Mohamad Roslan, Ahmad Fadli Saad.
Brand Logos Recognition System Using Image Processing for Food and Beverage Brands.
Journal of Engineering, Technology & Applied Science, vol. 6, no. 3, pp. 167-177, December 2024. DOI: 10.36079/lamintang.jetas-0603.768

  168
1. Introduction
Logos are a fundamental element of a brand's identity, serving as a visual representation of the brand
and its core values. Acting as crucial visual markers, logos significantly shape customers' perceptions,
influence decision-making, and strengthen relationships with brands [1]. A well-designed and
recognizable logo enhances brand awareness and fosters consumer loyalty, playing an essential role in
differentiating brands within highly competitive markets [2]. In the food and beverage industry, the
strategic deployment of logos has become increasingly important for building brand recognition and
driving consumer engagement. However, effective recognition and identification of logos are often
hindered by variations in design, image quality, and lighting conditions [3].
The advent of deep learning techniques has transformed the domain of image processing, providing
enhanced accuracy and resilience. Among these techniques, Convolutional Neural Networks (CNNs)
have demonstrated remarkable potential for applications such as logo recognition (LR) [4]. Traditional
LR systems, which rely on manual or semi-automated feature extraction methods, often struggle with
complex designs and variations, positioning deep learning-based approaches as a superior alternative.
These advanced systems enable businesses to gain valuable insights into brand recognition and
consumer loyalty, thereby refining their marketing strategies [5]. For example, accurate LR can help
organizations better understand consumer preferences, optimize product designs, and evaluate the
effectiveness of branding initiatives.
In the context of food and beverage brands, robust LR systems address several critical industry
challenges. These include detecting counterfeit logos, analyzing consumer behavior, and supporting
automated surveillance and fraud detection. Leveraging large datasets and advanced computational
tools, CNN-based LR systems have demonstrated notable improvements in recognition accuracy, even
for logos featuring intricate designs or diverse variations [6]. These advancements underscore the
transformative potential of AI-driven technologies to revolutionize marketing practices and enhance
customer satisfaction.
Ipoh, a town renowned for its vibrant food and beverage sector, provides an ideal setting for
examining the application of CNN-based logo recognition systems. The development of such systems
within this locale has the potential to support local businesses by optimizing branding strategies and
driving the broader adoption of advanced technologies among small and medium-sized enterprises
(SMEs). By employing deep learning methodologies, this research aims to create a Brand Logo
Recognition (BLR) system tailored to the specific needs of food and beverage brands in Ipoh, thereby
improving marketing efficiency and consumer engagement [3].
This article explores the capabilities of CNN-based BLR systems in addressing the challenges
associated with logo recognition, particularly within the food and beverage industry. It examines the
limitations of traditional methods, the advancements enabled by deep learning, and the practical
implications of implementing such systems in real-world contexts. By investigating these dimensions,
this study seeks to contribute to the expanding body of knowledge on AI-driven marketing tools and
their role in fostering innovation and growth in the business sector [7].

2. Introduction
2.1. Overview of Brands Marketing
Brand marketing, particularly logo recognition, holds substantial economic significance in the
contemporary business landscape [9]. It serves as a critical driver of business growth, facilitates the
development of consumer loyalty, and contributes to the establishment of a sustainable competitive
advantage. From an economic perspective, several aspects underscore the importance of brand
marketing with a specific focus on logo recognition [10]:
1) Differentiation and Competitive Advantage
Brand logo recognition plays a pivotal role in distinguishing companies from their
competitors. A distinctive and easily identifiable logo allows businesses to establish a unique
identity, effectively capturing consumer attention in a crowded marketplace. This
differentiation not only strengthens brand presence but also provides a competitive advantage
by fostering customer attraction and loyalty. Ultimately, a well-recognized logo contributes to
increased sales and revenue growth, reinforcing the company’s market position and long-term
success.
2) Brand Equity and Perceived Value
Brand logo recognition significantly contributes to the development of brand equity, an
intangible asset that encapsulates the value associated with a brand. A well-recognized and

Aini Khadijah Mohamad Roslan, Ahmad Fadli Saad.
Brand Logos Recognition System Using Image Processing for Food and Beverage Brands.
Journal of Engineering, Technology & Applied Science, vol. 6, no. 3, pp. 167-177, December 2024. DOI: 10.36079/lamintang.jetas-0603.768

  169
trusted logo fosters positive brand associations, instilling consumer confidence and
reinforcing perceptions of quality and reliability. As brand equity strengthens, the perceived
value of the brand increases, enabling businesses to command premium pricing for their
products or services. This heightened value translates into greater financial success,
positioning the brand for sustained growth and competitive advantage.
3) Consumer Trust and Loyalty:
Effective brand logo recognition plays a crucial role in cultivating consumer trust and
fostering brand loyalty. A recognizable and memorable logo generates a sense of familiarity
and reliability, which strengthens consumers’ emotional connections to the brand. When a
brand logo elicits positive perceptions, consumers are more inclined to exhibit loyalty,
resulting in repeat purchases and word-of-mouth advocacy. This loyal customer base not only
contributes to consistent revenue streams but also enhances the brand’s market reputation,
further solidifying its competitive position.

Figure 1. Conceptual Map for Brand Logos

Brand logos are visual representations that encapsulate the essence and identity of a brand. These
carefully crafted symbols serve as powerful communication tools, embodying the personality, vision,
and values of the brand [11]. A brand logo functions as the face of the brand, acting as a visual cue
that instantly connects consumers to the brand’s products or services. An effective logo is easily
recognizable, memorable, and visually appealing, capturing consumer attention and leaving a lasting
impression. Through design elements such as typography, colors, shapes, and symbols, a logo conveys
critical information about the brand’s industry, target audience, and unique selling proposition.
A primary function of a brand logo is to facilitate brand recognition. A well-designed logo fosters
instant familiarity, enabling consumers to associate it with the brand’s offerings [12], [13]. Acting as
visual shorthand, the logo simplifies recall and differentiation from competitors. It serves as a visual
anchor that evokes positive associations and emotions tied to the brand.
Beyond recognition, a logo plays a central role in establishing a brand’s identity. It visually
represents the brand’s core values, positioning, and personality traits. For instance, a sleek and modern

Aini Khadijah Mohamad Roslan, Ahmad Fadli Saad.
Brand Logos Recognition System Using Image Processing for Food and Beverage Brands.
Journal of Engineering, Technology & Applied Science, vol. 6, no. 3, pp. 167-177, December 2024. DOI: 10.36079/lamintang.jetas-0603.768

  170
logo might signify innovation, while a warm and inviting design could convey trust and
approachability. These visual elements create a conduit for emotional connections between the brand
and its consumers.
Brand logos are integral to marketing and advertising strategies, prominently displayed across
various touchpoints, including product packaging, websites, social media profiles, advertisements, and
marketing collateral. Acting as a consistent visual thread, logos reinforce brand presence and enhance
recall in the minds of consumers [7].
Furthermore, a well-designed logo fosters trust and credibility by symbolizing professionalism,
reliability, and quality. It shapes consumer perceptions of the brand’s offerings and can inspire
confidence, encouraging consumers to choose the brand over its competitors.

2.2. Overview of Deep Learning and Neural Network and Image Recognition
This research focuses on the area of brand logo recognition through image recognition techniques.
Image recognition has become a widely explored domain in artificial intelligence (AI) research. Since
the advent of AI, many countries have invested significantly in advancing AI technologies, leading to
remarkable developments across various fields [11]. AI encompasses multiple approaches, including
machine learning and deep learning. For this research, we employ a machine learning-based approach
to detect and recognize brand logos as part of the image recognition process.
Image recognition serves diverse purposes and spans varying fields and complexities [12]. At its
core, image recognition involves identifying objects within an image and determining whether specific
objects are present. When integrated with AI, image recognition methods can analyze images more
comprehensively by identifying and deconstructing the objects within them. A practical example is
Google Lens, an application that utilizes image recognition technology. By analyzing captured
images, Google Lens identifies objects and provides accurate search results based on the image
content. This capability exemplifies the practical utility of AI-powered image recognition in everyday
applications.
Deep learning, a specialized branch of machine learning, has significantly advanced image
recognition. It trains artificial neural networks with multiple layers to learn from large datasets. These
neural networks, inspired by the biological structure of the human brain, consist of interconnected
artificial neurons organized into layers. Convolutional Neural Networks (CNNs), a specific type of
neural network, are particularly effective for image recognition tasks. They employ a distinct
architecture comprising convolutional layers, pooling layers, and fully connected layers to extract
features and classify images.
Training deep learning models for image recognition requires labeled datasets, enabling the
network to identify patterns and features by iteratively adjusting its internal parameters based on these
examples. Deep learning excels in automatic feature extraction and representation learning,
significantly reducing the need for manual feature engineering. Its hierarchical learning capabilities
allow for capturing intricate patterns and discriminative features, resulting in high accuracy and
performance.
Transfer learning is another valuable technique in deep learning, where pre-trained models, trained
on large-scale datasets, are fine-tuned for specific tasks. This method leverages the insights and
knowledge acquired from previous tasks, facilitating faster training and improved performance,
especially when working with limited labeled data [13].
Deep learning and neural networks have been applied across various domains, including medical
imaging, security systems, autonomous vehicles, and content-based image retrieval. These
technologies have revolutionized image recognition by enabling models to automatically learn and
extract features from raw image data, yielding precise and efficient predictions. In the context of brand
logo recognition, deep learning techniques hold immense potential for applications in marketing,
retail, and consumer behavior analysis. By leveraging image processing and deep learning, businesses
can enhance their understanding of branding strategies and consumer engagement, driving innovation
and competitive advantage.

2.3. Convolutional Neural Network Approaches
2.3.1. D-CNN
D-CNN or Dilated Convolutional Neural Network, refers to a specific architecture within
convolutional neural networks (CNNs) that integrates dilated convolutions. Dilated convolutions, also
known as atrous convolutions, involve introducing gaps or skips between the kernel elements during

Aini Khadijah Mohamad Roslan, Ahmad Fadli Saad.
Brand Logos Recognition System Using Image Processing for Food and Beverage Brands.
Journal of Engineering, Technology & Applied Science, vol. 6, no. 3, pp. 167-177, December 2024. DOI: 10.36079/lamintang.jetas-0603.768

  171
the convolution process. In contrast, a conventional convolution operation entails a kernel sliding over
the input image or feature map with a stride of 1, performing convolutions with neighboring pixels.
While this captures local information effectively, it may lead to a loss of spatial resolution as the
network depth increases [14].
Dilated convolutions mitigate this issue by inserting gaps between the kernel elements. By
applying a dilation factor greater than 1, such as 2 or 3, the receptive field of the convolution
operation is expanded without compromising spatial resolution. This mechanism enables the network
to capture both local and global contextual information. D-CNNs leverage dilated convolutions to
enhance the network's capacity to recognize larger contexts and long-range dependencies within the
input data. By employing dilated convolutions across multiple layers, D-CNNs can efficiently process
and extract features from images or sequences, facilitating the analysis of large receptive fields [15].
D-CNNs have proven effective in a wide range of computer vision tasks, including image
classification, object detection, semantic segmentation, and image generation. These networks exhibit
improved performance in capturing fine details, managing large-scale variations, and preserving
spatial information, outperforming traditional CNN architectures [15].

2.3.2. R-CNN
R-CNN, or Region-based Convolutional Neural Network, was introduced in 2014 and represents a
significant advancement in applying convolutional neural networks (CNNs) for object detection
research. The R-CNN architecture comprises three main modules: region proposal, feature extractor,
and classifier.
The region proposal module generates candidate bounding boxes, which are independent and
categorized into potential regions of interest. These candidate regions are then extracted for further
analysis. The feature extractor module utilizes a deep CNN, such as AlexNet, to extract features from
each candidate region. AlexNet, which won the ImageNet classification competition, is used to
generate a 4,096-element vector that characterizes the contents of the image. This vector is
subsequently input into a linear Support Vector Machine (SVM) for classification, with one SVM
trained for each known class [16]. This straightforward application of CNN effectively addresses
object localization and recognition tasks.
However, a major disadvantage of R-CNN is its slow processing speed, which hampers its
efficiency in image recognition tasks. To overcome this limitation, Fast R-CNN was developed to
address the speed issues associated with R-CNN. Fast R-CNN improves upon R-CNN in three key
areas. First, the output of the CNN is fully connected to a layer that generates two outputs: one for
class predictions via a softmax layer, and another for bounding box predictions via a linear regression
model [17]. This process is applied to each region of interest within an image multiple times,
improving both speed and accuracy.
In summary, R-CNN provides a simple yet effective solution for object localization and
recognition using CNN-based feature extraction, while Fast R-CNN optimizes the original
architecture by enhancing processing speed and classification efficiency. Figure 2.7 illustrates the Fast
R-CNN architecture and how the model operates on each candidate region.

Figure 2. R-CNN Works

Aini Khadijah Mohamad Roslan, Ahmad Fadli Saad.
Brand Logos Recognition System Using Image Processing for Food and Beverage Brands.
Journal of Engineering, Technology & Applied Science, vol. 6, no. 3, pp. 167-177, December 2024. DOI: 10.36079/lamintang.jetas-0603.768

  172
The primary purpose of Fast R-CNN is to significantly accelerate training and improve prediction
accuracy compared to the original R-CNN technique. However, it still requires candidate regions
alongside the input image for processing. Building upon this foundation, the development of Faster R-
CNN further enhances both the speed of training and detection. This improvement is achieved through
the introduction of the Region Proposal Network (RPN), which efficiently generates and refines
region proposals during the training process [18]. Faster R-CNN comprises two key modules. The first
module is a deep convolutional network that generates region proposals. The second module uses
these proposed regions for detection through the Fast R-CNN detector [18]. By integrating region
proposal generation directly into the network, Faster R-CNN eliminates the need for external region
proposal algorithms, leading to a more streamlined and efficient object detection process

Figure 3. Fast-RCNN

In object detection, the entire system of Faster R-CNN is designed as a single, unified network. The
Region Proposal Network (RPN) module directs the Fast R-CNN module on where to focus, utilizing
the concept of 'attention' processes commonly seen in modern neural networks. For region proposal,
the network’s architecture and properties are crucial. Algorithms are developed to train both the RPN
and Fast R-CNN modules using shared features, ensuring seamless integration [18]. The region
proposal network works by taking an image of any size as input and producing rectangular object
proposals as output. This process is fully convolutional, with the key goal being to share computation
with the Fast R-CNN object detection module. A small network slides over the convolutional feature
map, which is the output of the final shared convolutional layer, to generate region proposals. This
smaller network processes the convolutional feature map to efficiently produce the proposals [18]. By
leveraging shared computations, Faster R-CNN improves both speed and performance in object
detection tasks.

3. Methodology
The methodology adopted in this research outlines a systematic approach for developing a brand logo
recognition system using image processing techniques and machine learning, specifically
Convolutional Neural Networks (CNN). The methodology is divided into three key phases:
3.1. Study of the Significance of Brand Logo Recognition Systems
This phase focuses on understanding the importance and potential applications of brand logo
recognition, including its relevance in marketing, consumer behavior analysis, and automated image
recognition tasks. This phase includes the following steps:
1) Defining the Problem Statement and Objectives: Establish the research area, significance, and
scope of the system while addressing target users and potential benefits.
2) Literature Review: Utilize open-source tools (e.g., Google Scholar) and software like
Mendeley to organize and study relevant academic works. Key focus areas include neural

Aini Khadijah Mohamad Roslan, Ahmad Fadli Saad.
Brand Logos Recognition System Using Image Processing for Food and Beverage Brands.
Journal of Engineering, Technology & Applied Science, vol. 6, no. 3, pp. 167-177, December 2024. DOI: 10.36079/lamintang.jetas-0603.768

  173
networks, image recognition techniques, and practical applications in food and beverage
sectors.
3) Preliminary Study: A survey is conducted to collect user feedback on the significance of logo
recognition systems. A structured questionnaire covers respondents’ experiences,
expectations, and understanding of machine learning concepts.
 Part A: Gathers demographic information (e.g., age, job, gender).
 Part B: Evaluates perceptions of logo recognition systems, including business and
consumer benefits.
 Part C: Assesses knowledge of machine learning among users.

3.2. Development of the Brand Logo Recognition System
In this phase, the logo recognition system is developed using CNN-based image processing
techniques. The system is trained on a dataset of brand logos to learn and identify distinct features
associated with different logos, optimizing the model for accurate and efficient recognition.

Figure 4. Hybrid Methodology – Machine Learning and SDLC

Steps in system development, are:
1) Research Initiation
Define goals, objectives, and requirements for the software and machine learning components
in collaboration with stakeholders.
2) Data Acquisition and Preparation
Collect and preprocess a comprehensive dataset of food and beverage brand logos. Steps
include resizing, normalization, and augmentation.
3) Agile Iterations
Use iterative sprints for continuous software development, incorporating user stories and
prioritizing tasks.
4) Model Development
Train a CNN (e.g., ResNet or Inception) for logo classification and an SSD for object
detection. Optimize using transfer learning and iterative experimentation.
5) Integration and Testing
Combine machine learning models with software components, conducting unit and integration
testing.
6) User Feedback
Gather input to improve model accuracy and software functionality.
7) Deployment and Maintenance
Incrementally release the system, monitor performance, and make updates to improve
accuracy and address issues.

3.3. Construction of Algorithm for Brand Logo Recognition System
The algorithm construction process involves the following steps:
1) Dataset Collection
Acquire a labeled dataset of F&B brand logos.
2) Data Preprocessing
Resize, normalize, and augment images to enhance model generalization.

Aini Khadijah Mohamad Roslan, Ahmad Fadli Saad.
Brand Logos Recognition System Using Image Processing for Food and Beverage Brands.
Journal of Engineering, Technology & Applied Science, vol. 6, no. 3, pp. 167-177, December 2024. DOI: 10.36079/lamintang.jetas-0603.768

  174
3) Model Training
• Train a CNN model for feature extraction and classification.
• Use an SSD for logo detection to identify bounding boxes and classify detected regions.
4) Logo Detection and Recognition
Detect logos in input images using the SSD model, then classify detected regions with the
CNN model.
5) Post-Processing
Refine results with non-maximum suppression and confidence thresholds to reduce false
positives.
6) Evaluation
Assess model performance with metrics like precision, recall, and mean Average Precision
(mAP).
7) Iteration
Fine-tune hyperparameters and algorithms based on evaluation results.

Figure 5. Construction of the Algorithm

3.4. System Architecture
The system architecture combines components for preprocessing, deep learning, user interaction, and
data storage, as show in Figure 6.

Figure 6. The architecture of the Algorithm

This architecture enables the system to process input images, identify logos, and deliver results
efficiently. The system components are:
1) User Interface
Allows users to upload or capture images for recognition.
2) Image Processing Module
Standardizes image sizes, normalizes colors, and enhances quality.
3) Logo Recognition Algorithm
Utilizes CNN and SSD for detection and classification.
4) Brand Logo Database

Aini Khadijah Mohamad Roslan, Ahmad Fadli Saad.
Brand Logos Recognition System Using Image Processing for Food and Beverage Brands.
Journal of Engineering, Technology & Applied Science, vol. 6, no. 3, pp. 167-177, December 2024. DOI: 10.36079/lamintang.jetas-0603.768

  175
Stores logo information for verification and system improvement.
5) Integration Layer
Ensures smooth communication between components.

4. Finding and Discussion
4.1. Findings
The implementation of a CNN-based Brand Logo Recognition (BLR) system in this study yielded
several significant findings. First, the use of Convolutional Neural Networks (CNNs) demonstrated
remarkable accuracy and robustness in recognizing food and beverage brand logos across various
conditions, such as diverse lighting, image quality, and logo complexity. Training the CNN model on
a well-preprocessed dataset enhanced generalization, minimizing both false positives and false
negatives during logo recognition tasks.
Second, the study highlighted the critical role of integrating logo recognition algorithms with an
efficient image preprocessing pipeline. By normalizing colors, resizing images, and applying data
augmentation techniques, the system achieved consistent performance across a broad spectrum of
input variations. These preprocessing steps were essential in enhancing the CNN's feature extraction
capabilities, improving its overall performance.
Third, the deployment of the Single Shot Detector (SSD) in conjunction with CNNs for object
detection significantly improved the system's ability to accurately localize and classify logos. This
combination resulted in higher mean Average Precision (mAP) scores, effectively addressing
challenges associated with identifying logos that have similar features or complex designs.

4.2. Discussion
The findings of this study underscore the effectiveness of deep learning techniques, particularly
Convolutional Neural Networks (CNNs), in overcoming the limitations of traditional feature
extraction-based logo recognition systems. Traditional methods often face challenges when handling
variations in logo designs and environmental conditions. In contrast, CNN-based systems utilize deep
hierarchical representations, allowing for more accurate and robust logo detection across diverse
scenarios.
A key point of discussion is the practical application of the Brand Logo Recognition (BLR) system
for businesses in Ipoh. Local food and beverage enterprises can leverage this system to enhance brand
recognition, monitor customer engagement, and combat the spread of counterfeit logos. This
application not only supports marketing strategies but also helps protect brand integrity in a
competitive market.
The integration of an iterative Agile methodology during the development phase was crucial in
refining the BLR system. Continuous feedback from users enabled developers to improve model
accuracy and optimize the user interface. This iterative process highlights the importance of user-
centric approaches in creating AI-driven tools that are tailored to meet business needs.
Additionally, the research addressed challenges related to detecting counterfeit logos, which often
imitate genuine brand designs. To mitigate this, the system incorporated advanced post-processing
techniques such as non-maximum suppression and confidence thresholds. These measures effectively
reduced false detections, enhancing the reliability of the recognition outcomes.
The role of transfer learning in this study was pivotal. By leveraging pre-trained CNN models like
ResNet and fine-tuning them on the brand logo dataset, the system achieved optimal performance
without requiring substantial computational resources. This approach demonstrates the cost-
effectiveness and scalability of deep learning solutions, particularly beneficial for small and medium-
sized enterprises (SMEs) with limited resources.
Finally, the study highlights the broader potential of deploying such systems in industries beyond
food and beverages. Automated logo recognition can extend to sectors such as e-commerce,
advertising, and trademark infringement detection, thereby transforming traditional business practices.
The developed BLR system serves as a prototype for advancing AI applications in marketing and
branding. Although the system is specific to Ipoh's food and beverage industry, the methodology and
findings offer valuable insights for global applications. Future research could explore expanding the
system's capabilities to multi-label classification and real-time processing to enable wider adoption.

Aini Khadijah Mohamad Roslan, Ahmad Fadli Saad.
Brand Logos Recognition System Using Image Processing for Food and Beverage Brands.
Journal of Engineering, Technology & Applied Science, vol. 6, no. 3, pp. 167-177, December 2024. DOI: 10.36079/lamintang.jetas-0603.768

  176
5. Conclusion
This study successfully developed a CNN-based Brand Logo Recognition (BLR) system tailored to
the needs of the food and beverage industry, particularly in the context of Ipoh. The findings
demonstrated the effectiveness of Convolutional Neural Networks (CNNs) combined with Single Shot
Detector (SSD) algorithms in accurately detecting and classifying brand logos under diverse
conditions. Image preprocessing techniques, such as normalization, resizing, and augmentation,
played a crucial role in enhancing the model's generalization capabilities, while iterative feedback
through Agile methodology ensured that the system met user requirements. These results underscore
the value of integrating deep learning techniques with practical development approaches to address
real-world challenges in logo recognition.
The study also revealed the broader implications of deploying BLR systems for businesses. By
leveraging accurate logo detection, local food and beverage enterprises can strengthen their branding
strategies, monitor customer engagement, and prevent counterfeit logos from undermining their brand
integrity. The cost-effective application of transfer learning, using pre-trained CNN models like
ResNet, further highlights the feasibility of deploying advanced AI technologies in small and medium-
sized enterprises (SMEs). These findings emphasize the potential for AI-driven tools to transform
marketing practices, improve customer satisfaction, and safeguard brand identities across industries.
Future research should explore expanding the system's capabilities to address additional
challenges. Potential directions include incorporating multi-label classification for recognizing
multiple logos in a single image, improving real-time processing efficiency for broader applications,
and extending the system to other sectors such as e-commerce and trademark infringement detection.
Furthermore, integrating advanced techniques like generative adversarial networks (GANs) for
counterfeit logo detection and expanding datasets to include logos from diverse industries will further
enhance system accuracy and applicability. These advancements could pave the way for more
comprehensive and scalable solutions, benefiting businesses globally.

References
[1]  C. W. Park, B. J. Jaworski, and D. J.  MacInnis, “Strategic brand concept-image management,”
Journal of Marketing, vol. 50, no. 4, pp. 135-145, 2013.
[2] C. Kohli, and R. Suri, “Branding consumer goods: Insights from theory and practice,” Journal of
Consumer Marketing, vol. 19, no. 1, pp. 52-63, 2002.
[3] M. A. Shakir, H. Saleh, and Z. Ali, “Logo and trademark recognition using deep learning
techniques,” Journal of Visual Communication and Image Representation , vol. 55, pp. 62-69,
2018.
[4] F. Sahel, S. Ahmed, and S. Latif, “Deep learning for logo recognition: Challenges and
opportunities,” International Journal of Computer Vision, vol. 129, no. 3, pp. 712-726, 2021.
[5] X. Zou, H. Chen, and W. Li, “Counterfeit logo detection in social media using neural networks,”
IEEE Transactions on Multimedia, vol. 25, pp. 1091-1102, 2023.
[6]  F. Sahel, S. Ahmed, and S. Latif, “Logo recognition using CNN-based image processing
techniques,” Image and Vision Computing, vol. 89, pp. 52-63, 2021.
[7] H. Kaur, and K. Kaur, “Connecting the dots between brand logo and brand image,” Asia-Pacific
Journal of Business Administration, vol. 11, no. 1, pp. 68–87, 2019.
[8] C. Kohli, and R. Suri, “Creating effective logos: Insights from theory and practice,” Business
Horizons, vol. 45, no. 3, pp. 58–64, 2002.
[9] C. W. Park, A. B. Eisingerich, G. Pol, and J. W. Park, “The role of brand logos in firm
performance,” Journal of Business Research, vol. 66, no. 2, pp. 80–187, 2013.
[10] S. Sahel, M. Alsahafi, M. Alghamdi, and T. Alsubait, “Logo Detection Using Deep Learning
with Pretrained CNN Models,” In Technology & Applied Science Research, vol. 11, no. 1, 2021.
[11] L. Liang, S. Z. Abidin, N. Shaari, and L. Jing, “Logo Impact on Consumer’s Perception, Attitude,
Brand Image and Purchase Intention: A 5 Years Systematic Review,” International Journal of
Academic Research in Business and Social Sciences, vol. 14, no. 3, 2024.
[12] A. Svyrydov, H. Kuchuk, O. Tsiapa, Improving efficienty of image recognition process:
Approach and case study SO 2018 IEEE 9th International Conference on Dependable Systems,
Services and Technologies (DESSERT), LA English, 2018.

Aini Khadijah Mohamad Roslan, Ahmad Fadli Saad.
Brand Logos Recognition System Using Image Processing for Food and Beverage Brands.
Journal of Engineering, Technology & Applied Science, vol. 6, no. 3, pp. 167-177, December 2024. DOI: 10.36079/lamintang.jetas-0603.768

  177
[13] A. Kaluthantrige, J. Feng, and J. Gil-Fernández, “CNN-based Image Processing algorithm for
autonomous optical navigation of Hera mission to the binary asteroid Didymos,” Acta
Astronautica. 2023.
[14] N. Herencsar, Linear Blocks Following Recent Trends In Analog Circuit Design , Thesis, Institute
of Electrical and Electronics Engineers: Brno, 2015.
[15] C. Agarwal, P. Itondia, and A. Mishra, “A novel DCNN-ELM hybrid framework for face mask
detection,” Intelligent Systems with Applications, 17. 2023.
[16] L. Bombonato, G. Camara-Chavez, and P. Silva, “Real-Time Single-Shot Brand Logo
Recognition. Proceedings - 30th Conference on Graphics, Patterns and Images,” SIBGRAPI pp.
134-140, 2017.
[17] J. Sanghvi, J. Rathod, S. Nemade, H. Panchal, and A. Pavate, “Logo Detection Using Machine
Learning Algorithm: A Survey. 2023 4th International Conference on Communication Systems,
Computing and IT Applications,” CSCITA, 2023
[18] S. Ren, K. He, R. Girshick, and J. Sun, “Faster R-CNN: Towards Real-Time Object Detection
with Region Proposal Networks,” IEEE Transactions on Pattern Analysis and Machine
Intelligence, vol. 39, pp. 1137-1149, 2017.
