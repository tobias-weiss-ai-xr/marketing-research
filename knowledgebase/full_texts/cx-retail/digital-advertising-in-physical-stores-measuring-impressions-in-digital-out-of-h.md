---
title: 'Digital Advertising in Physical Stores: Measuring Impressions in Digital Out-of-Home Advertising'
url: https://doi.org/10.5281/zenodo.20144056
category: cx-retail
subcategory: case-study
date: 2026-02
venue: Zenodo (CERN European Organization for Nuclear Research)
authors:
- Karishma Verma
source: openalex-oa
pdf_url: https://ijisae.org/index.php/IJISAE/article/download/8232/7230
pages: 9
chars: 30830
fetched_at: '2026-11-08T17:22:33+00:00'
kb_version: 1
---

# Digital Advertising in Physical Stores: Measuring Impressions in Digital Out-of-Home Advertising

International Journal of
INTELLIGENT SYSTEMS AND APPLICATIONS IN
ENGINEERING
ISSN:2147-67992147-6799                                             www.ijisae.org Original Research Paper

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 688–697 |  688

Digital Advertising in Physical Stores: Measuring Impressions in
Digital Out-of-Home Advertising

Karishma Verma
Abstract: Digital Out-of-Home (DOOH) advertising combines multimedia display technology, computer vision, and real -
time audience profiling in retail and public environments. DOOH measurement does not follow the deterministic methodology
of online digital media measu rement. DOOH publisher measurements are based on probabilistic inference of sensor fusion,
geometry, and behavior rather than deterministic impressions. This paper provides a technical survey of DOOH impression
measurement methods. We focus on multimedia s ensing, real -time processing, and data -driven optimization in DOOH
systems. In this section we discuss four parts of the measurement pipeline. First, we consider traffic volume measurement
using optical and wireless traffic fingerprints, dwell time assessm ent using computer vision and projected ultrasonic waves,
demographic models using statistical classification, and opportunity -to-see (OTS) estimation using a mathematical model of
attention-weighted exposure probabilities. We also discuss how new technologies, such as state-of-the-art gaze estimation via
deep learning, mobile location analytics and programmatic advertising platforms, can assist in measuring and optimizing ad
campaigns. These challenges relate to environmental factors affecting sensor perfo rmance, noisy crowds, privacy-preserving
computation, and the lack of industry measurement standards. The paper suggests that the implementation of a transparent‚
auditable and standardized infrastructure for measuring impressions will allow strong‚ reliable and verifiable measurement. It
argues that this will enable the DOOH industry to flourish as a reliable data-driven medium.

Keywords: Digital Out -Of-Home Advertising, Impression Measurement, Opportunity -To-See, Audience Analytics,
Programmatic Advertising

1. Introduction
After rapid growth, Digital Out -of-Home has
become one of the most technologically advanced
advertising media. Static advertising on posters has
transitioned to screens in retail stores, transportation
hubs, and public spaces, where out -of-home media
owners wish to use real -time audience
measurements to target advertising to the right
viewer at the right moment. With the channel
maturing, the questions for the industry to answer
are how we accurately measure the audiences that
our screens can deliver․ Adver tising clients need
reliable, comparable, and standardized metrics
before they commit meaningful budgets to any
medium and‚ frankly, DOOH hasn't done that yet.
We review the state of the art in DOOH impression
measurement, covering sensing systems,
computational models, and challenges in this field.

1․1 DOOH as a Multimedia System
DOOH is a complex multimedia system of display
hardware, content supply networks, sensors, and
analytics. DOOH systems consist of (1) hardware
for displaying advertisements, such as LED
billboards and LCD screens at variable resolution
and viewing angles; (2) content management
systems that determine when ads are displayed; (3)
sensing hardware for detecting audiences; (4)
analytics pipelines for understanding sensor data;
and (5) programmatic systems for automated media
buying and optimization.
1․2 The impression measurement problem
The major overarching technical challenge is that
inference of exposure in a shared physical
environment differs from non -shared environments
like online advertising, where exposure can be
observed directly at the device. DOOH must infer
this exposure from  environmental sensors,
geometric models, and probabilistic attention
predictions.
Independent Researcher, USA

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 688–697 |  690

1․3 Multimedia Sensing Requirements
It is necessary to integrate multiple sensing
modalities:
● Sensing Layer:  Optical sensors, wireless
signal detectors, ultrasonic sensors
● Processing Layer: Computer vision, gaze
estimation, trajectory analysis, sensor fusion
● Analytics Layer:  Geometric modeling,
statistical inference, demographic profiling, real -
time optimization
1․4 Survey Methodology
We systematically reviewed 50+ papers from ACM
Digital Library, IEEE Xplore and advertising
research databases on computer vision, multimedia
systems, and audience analytics published between
2010 and 2026.

2. Defining Impressions in the DOOH Context
Before a measure can be evaluated, the concept it
attempts to measure must be defined. In online
advertising, there is a standard definition of an
impression based on ad delivery events. Since
DOOH does not have a direct equivalent to the
concept of a view able impression, it is particularly
important to have precise definitions. The
subheadings below discuss the definition of a
DOOH impression, the geometric requirements for
viewability of an impression, and the time
requirements for amassing impressions in  an
advertising loop.
2․1 Impression Definition
Formal Definition:  An impression is an event
during which an individual was present in the
viewable space of a digital display for the period of
time that an advertisement was delivered under
conditions sufficient to provide visual perception.
Characteristics:
● Probabilistic nature (inferred from sensors)
● Simultaneous exposure (multiple viewers)
● Environmental dependency (venue, crowd,
temporal factors)
● Attention uncertainty (presence ≠
attention)
● Controlled viewing contexts (public and
semi-public spaces)
2․2 Geometric Modeling
The impression requires the person to be in the
viewable zone, that is, a geometrically defined area
of physical space from which the screen is visible ‚
and, at the same time, legible. The viewable zone
needs to be defined in terms of the viewing distance,
the screen angle and possible occlusions. The model
consists of the following components:
● Viewing Distance:  1․5× to 10× screen
height (varies by content)
● Viewing Angle:  LCD ±60° horizontal,
±40° vertical; LED ±80° horizontal, ±60° vertical
● Occlusion Analysis:  architectural
structures, environmental objects, dynamic
occlusions
● Sightline Geometry:  Ray-tracing with
head height distributions (1․4-1․8m)
Mathematical Formulation:
V = {p ∈ ℝ³ : d_min ≤ ||p - s|| ≤ d_max‚ θ_h(p‚s) ≤
θ_h_max‚ θ_v(p‚s) ≤ θ_v_max‚ ¬occluded(p‚s)}
2․3 Opportunity-to-See versus Verified Exposure
Most DOOH audience measurement systems are
based on opportunity to see (OTS) methodology,
which measures the estimated number of persons
present within the effective viewing area of the
display that is in play mode at any point in time. It
measures the max imum possible exposure but does
not draw visual attention.
Attention-weighted OTS models modify OTS
estimates with attentional probabilities estimated
based on gaze estimation studies:
● Opportunity-to-See (OTS):  Total
potential audience who can see advertisement at any
one time
● Attention-Weighted OTS: OTS corrected
by attention correction factors (0․3 -0․7 depending
on venue).
● Verified Exposure:  use of eye -tracking,
gaze estimation or some other explicit measurement
of attention
● Relationship: Verified Exposure ≤
Attention-Weighted OTS ≤ Raw OTS

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 688–697 |  691

2․4 Role of Ad Play Duration and Loop
Frequency (Temporal Factors)
● Ad Play Duration: 5 to 30 seconds
● Typical Loop Cycle lengths range from 2
to 10 minutes
● De-duplication and Dwell Time
Interaction: When more than one loop exposure
Timing is also an important factor in measuring
DOOH impressions when the advertising displayed
on these screens is on a rotating schedule with ads
from multiple advertisers. The number of
impressions can be measured according to the length
of the advertis ement and the number of loops. The
frequency and de -duplication logic applied to an
impression figure should be published whenever
such a figure is presented.

3. Core Measurement Techniques
Estimating the number of DOOH impressions
requires cross-aggregating many datasets across the
audience experience. There is no one dataset that
captures all of this information —traffic counts do
not capture dwell time, dwell time data does not
capture demo graphics, and neither of those can
confirm whether an ad was displayed or viewed.
Table 1 summarizes the components of a complete
measurement pipeline, the inputs they require, and
the limitations each has:

Component Data Input Primary Function Key Limitation
Traffic Volume Optical sensors, infrared counters, Wi-Fi/Bluetooth, ridership records Establishes raw audience count near display Accuracy degrades in high- density and variable lighting
Dwell Time Computer vision, ultrasonic sensors, device signals Estimates duration of presence in viewable zone Cannot confirm visual attention, only proximity
Opportunity-to-
See (OTS)
Traffic count, viewable zone
geometry, play window
Calculates maximum
potential exposure per ad
play
Overestimates actual
viewership; attention
unverified
Attention-
weighted OTS
OTS count, gaze probability
scores
Adjusts raw OTS by
empirical attention
probability
Gaze models vary in
accuracy across
environments
Demographic
Modeling
Panel surveys, census data,
behavioral segmentation
Estimates audience
composition by age,
gender, segment
Requires periodic
recalibration as
demographics shift
Loop Frequency
Adjustment
Ad play duration, loop cycle
length
Apportions audience
share per advertiser per
loop
De-duplication logic for
repeat exposures remains
unsettled
Programmatic
Integration
Real-time traffic feeds, audience
triggers
Activates delivery when
audience conditions are
met
Signal latency can misalign
delivery with audience
presence
Table 1: DOOH Impression Measurement Components and Their Functional Roles

3․1 Traffic Volume Estimation
Traffic volume is the basic layer of any impression
model and is a prerequisite for measuring dwell time
and attention around a given display. There are a
variety of sensing technologies that can be used for
this, each having advantages and disadvantages in
their application.
3․1․1 Optical Sensing
Optically based systems, which can provide spatial
data about the audience and are more widely

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 688–697 |  692

deployed in retail, are based on the following types
of sensors:
● PIR Sensors:  Economical, privacy -
maintaining, but low spatial resolution.
● Stereo Vision:  3D localization,
calibration-dependent, lighting-sensitive
● ToF Cameras:  640x480 pixels for real -
time 3D imaging with robustness
● LiDAR: high-resolution 3D point clouds,
high cost/high power
● Performance: detection varies from >95%
for sparse crowds to <70% for crowds with >1
person/m²

3․1․2 Wireless Detection
Detecting wireless signals can alternatively be used
for monitoring, where surveillance with a camera
device is not possible, or where privacy is a priority.
These technologies operate with varying degrees of
precision and scale:
● Wi-Fi Monitoring:  MAC address
detection, probe request frequency analysis
● BLE Beacons:  10-50 meter range․
Requires Bluetooth to be turned on.
● Cellular Analytics: Accuracy of hundreds
of meters, usually not for a single screen.
For retail outlets, traffic can vary by season, day of
week, and hour of the day. Daily averages can
induce large errors into impression estimates if
traffic is heavily concentrated in peak traffic periods
of the day.
3․2 Dwell Time Analysis
Dwell time is the amount of time a person's gaze is
held within the effective viewing area of a display
and is one of the most important factors of ad
detection and processing.
● CV-based tracking:  YOLO/Faster R -
CNN are DNNs used for pedestrian detection, while
SORT/DeepSORT/ByteTrack are multi -object
trackers used to maintain the identity across frames.
● Privacy-preserving: On-device
processing only sends aggregated statistics and does
not save identifiable images.
● Device-Based: Wi-Fi/BLE dwell
estimation with sampling intervals ranging from 1 to
5 minutes
These measurements create dwell time distributions
in the impression models, with more weight given to
those who spend more time in the viewable area.
3․3 Demographic Modeling
Presence measures like traffic and dwell time have
no demographic information, but this can be
modeled using external datasets about a location.
● CV-based classification (CNNs classify
age/gender from facial imagery with 80 -90%
benchmark accuracy) also faces bias/fairness
concerns.
● Panel-Based Modeling:  Survey panels
establish baseline demographics and extrapolate
them using statistical weighting and census/mobility
data. Calibration: Requires periodic recalibration
as demographics change.
3․4 OTS Calculation
The four components —traffic, dwell, viewability
geometry, and attention weighting —are turned into
an aggregated OTS number by applying the
following formula:
OTS = Traffic_Count × P(in_viewable_zone) ×
P(ad_playing | in_zone) × Attention_Weight
Attention weights between 0․3 and 0․7, based on
gaze data from retail stores and public places,
depend on factors such as the type of venue and the
placement of screens.

4. Emerging technologies
Section 3 discusses the common audience metrics in
DOOH. The use of computer vision, mobile data and
the programmatic ad infrastructure, which is fast
evolving, brings rich promise for greater precision‚
granularity and real -time usage of audience data in
DOOH. This section reviews three developments
that are changing the technical capabilities of
measuring impressions in DOOH.
4.1 Computer Vision Systems
Computer vision is the most advanced technology
used to measure DOOH audience reach; since initial
implementations, the technology has included
behavioral analysis beyond mere detection. Deep
learning has improved the effectiveness and

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 688–697 |  693

efficiency of these systems in recent years, and edge
computing architectures have enabled large -scale,
privacy-friendly computer vision to be
implemented.
4.1.1 Deep Learning Detection
● YOLO: Real-time (30 –60 FPS), >90%
accuracy (YOLOv8)
● Faster R -CNN: Higher accuracy, lower
frame rates (5–15 FPS)
● RetinaNet: Balanced accuracy -speed for
crowded scenes
● Tracking: SORT (efficient), DeepSORT
(robust re-ID), ByteTrack (state-of-the-art)
4.1.2 Gaze Estimation
● Appearance-Based Models:  5–10°
angular accuracy from facial imagery
● Head Pose: Coarse gaze proxy (yaw, pitch,
roll)
● Attention Scoring:  Gaze direction +
viewing distance + dwell time + environmental
context
● Validation: Venue-specific calibration
with ground-truth eye-tracking required
4.1.3 Privacy-Preserving Computer Vision
Modern DOOH deployments use privacy -
preserving image processing techniques whereby
images are analyzed locally on -device and only
aggregated information is shared with backend
reporting systems.
● On-Device Processing:  Edge computing,
aggregate-only transmission
● Anonymization: Face blurring, pose -only
estimation, differential privacy
● Federated Learning: Distributed training
without centralizing raw video
4.2 Mobile Location Analytics
Mobile location analytics provides a strong
complementary source of audience intelligence,
enabling inference of human traffic around DOOH
displays beyond what static sensor networks
achieve.
4.2.1 Data Sources
● GPS: 5–10m outdoor, unavailable indoors
● Wi-Fi Positioning:  10–50m, requires
dense infrastructure
● Cellular: 100–1000m, broad coverage but
imprecise
● BLE Beacons:  1–10m, requires beacon
deployment
4.2.2 Applications
● Trajectory Mining:  Movement patterns,
traffic flows, dwell hotspots
● Visit Frequency:  Reach/frequency
estimation, new vs. returning visitors
● Catchment Analysis:  Geographic
distribution, geo-targeted campaigns
● Cross-Venue: Consumer journey patterns
(with privacy protections)
4.2.3 Limitations
● Sampling Bias:  5–20% population
coverage, requires statistical weighting
● Spatial Accuracy:  Indoor positioning
challenges
● Temporal Resolution:  1–5 minute
intervals limit precision
● Privacy: GDPR/CCPA compliance
requirements
4.3 Programmatic DOOH Platforms
Programmatic DOOH platforms ingest audience
measurement data into automated advertising
marketplaces, allowing advertisers to
programmatically target inventory based on
predicted audience profiles and near real -time
environmental conditions.
4.3.1 Architecture
● SSPs: Aggregate inventory, standardized
APIs
● DSPs: Programmatic bidding, targeting
criteria
● DMPs: Centralized audience data
● RTB: Auction-based buying, dynamic
pricing
4.3.2 Targeting
● Demographic: Delivery when audience
matches targets

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 688–697 |  694

● Behavioral: Inferred behaviors/interests
● Contextual: Weather, events, time, traffic
● Footfall: Volume threshold triggers
4.3.3 Optimization
● DCO: Real-time creative selection
● Pacing: Budget management, frequency
capping
● Feedback Loops:  Performance metrics
inform bidding
● Latency: 1–5 second signal -to-activation
delay
5. Challenges and Limitations of Current
Practices
Despite the technological advances described above,
DOOH impression measurement faces a number of
structural challenges. No technology so far has been
able to address these challenges across the entire
measurement process, from the initial collection of
raw sensor data through to the final impression
count. These challenges result in limited
comparability, reliability, and advertiser confidence
in current DOOH impression measures. Table 2
describes the origin of these challenges and their
impact on operations.

Challenge Primary Source Pipeline Stage Affected Operational Impact
Environmental
Variability
Screen placement, lighting,
occlusion, fixture layout
Traffic counting,
viewability
modeling
Inconsistent accuracy
across venue types
Crowd Flow Bias Channeling and clustering in high- density spaces Traffic volume estimation Systematic over- or undercount of audience
Sensor Degradation High pedestrian density, irregular flow, poor lighting Data acquisition Reduced detection reliability in real-world conditions
Privacy Regulation Data minimization laws, biometric inference restrictions Demographic modeling, location data use Reduced granularity of available audience signals
Re-identification
Risk
Anonymized data combined with
auxiliary sources All data layers Limits permissible data fusion and retention.
Absence of
Standards
No universal impression definition
or audit framework
Reporting and
comparison
Cross-publisher figures not
directly comparable
Methodological
Fragmentation
Varying viewability zones, dwell
thresholds, attention weights
Impression
calculation
Impression inflation
incentives without
transparency
Table 2: Challenges Affecting DOOH Impression Measurement Reliability

5․1 Environmental variability and
standardization issues
These unintended variances are not always
predictable, nor able to be controlled to mimic the
controlled environment of a lab or the standardized
rendering environment of a web browser, nor
eliminated. Sensor performance and viewability
modeling can differ from site to site across a media
owner's or venue's physical environments. Major
sources of environmental variability are:
● Lighting: Optical sensors are sensitive to
sunlight, shadows, and darkness.
● Architecture: Occlusions, reflections, and
ceiling height impact coverage.

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 688–697 |  695

● Screen position: Screen mounting height,
viewing angle, and distance to pedestrians can vary
tremendously.
● Crowd Density : Accurate for sparse
(>95% accuracy), not dense crowds (<70%
accuracy).
Standards that specify fixed viewability regions or
attention decay curves often rely on simplifying
assumptions that only hold in some environments,
and so viewability measurements should be based on
characteristics of the environment where they are
measured.
5․2 Statistical Uncertainty in High -Traffic
Environments
Even with well -calibrated sensors, the statistical
models that convert the raw number of detections to
an estimate of impressions have their own noise, and
this noise tends to increase in complex, high-density
scenes. Furthermore, real-world pedestrian behavior
violates the assumptions in most impression models.
● Non-Independent Movement:  Groups
and social forces violate the independence
assumption in pedestrian models.
● Channeling/Clustering: Self-
organization of pedestrians is observed in most
traffic simulations where pedestrians are treated as
individual particles.
● Dwell Time Distributions:  Heavy-tailed
distributions with high variance challenge simple
models.
● Temporal Patterns:  Strong
hourly/daily/weekly/seasonal patterns require
dynamic modeling.
If these impression models are not ground -truthed
against environment-specific pedestrian behavior, a
systematic overcount or undercount of advertising
exposure may occur.
5․3 Privacy Regulation and Data Constraints
However, the richest audience data (exact
geographical points, facial data, and biometric data)
is the most limited by the provisions of privacy law.
Privacy guardrails for collecting physical-world data
are becoming stricter as regulators begin to focus on
this area. This narrows the range of techniques and
data sources that can be used to estimate DOOH
audiences. Key regulatory frameworks include the
following, each with diverse impacts:
● GDPR: Lawful basis, data minimization,
purpose limitation, storage limitation, and right to
erasure.
● CCPA: Right to know, delete, and opt out
of data sale.
● Biometric Laws:  Illinois BIPA requires
consent and has strict liability.
● Impact: Limits facial recognition, location
tracking, and data retention.
The potential for re -identifying individuals from
nominally anonymized datasets combined with
other data sources highlights the need for a privacy-
by-design approach to all audience measurement
pipelines.
5․4 Absence of Industry-Wide Standards
Beyond these technical issues, there is a more
fundamental problem for addressing them: The
DOOH industry has not reached agreement on what
constitutes an impression, what the measurement
method should be, and how the methods should be
audited. The lack of standards creates challenges for
advertisers‚ publishers and the reputation of the
channel as a whole. Some of the more prominent
problems are
● Definitional Inconsistency:  Varying
definitions of impression, viewability, and attention
across providers.
● Methodological opacity:  Proprietary
algorithms restrict independent replication and
assessment.
● Inflation Incentives:  Commercial
interests prefer large impression numbers rather than
accurate measurement.
● Audit Challenges:  Independent
verification is difficult without agreed -upon
standards.
A similar industry -level consensus on definitions‚
calibration and auditing processes, which the MRC
performs for online ad publishers, would help
strengthen the long -term credibility of the DOOH
marketplace.

6․ Future Research Directions
As outlined in Section 5, the challenges described
above lead to a coherent research agenda for the
entire DOOH measurement domain such that the

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 688–697 |  696

road ahead to success requires the overall progress
in the different sensor and modeling approaches to
achieve privacy, accuracy, cross -channel
comparability and methodological transparency in
an integrated manner. Four research priorities are
defined below:
6․1 Privacy-Preserving Measurement
Given the tightening privacy regulations, the call is
for measurement architectures that can produce
audience estimates without relying on individual -
level data. Some technical approaches show
promise:
● Federated Learning:  Distributed ML
training without centralizing raw data.
● Differential Privacy:  Calibrated noise
prevents re-identification.
● Homomorphic encryption:  Computation
on encrypted data without decryption.
● Secure Multi-Party Computation:
Collaborative analytics without data sharing.
6․2 Attention Verification
The most compelling evidence for the effectiveness
of attention -based impressions versus more direct
presence-based impressions would be methods of
determining whether the person's gaze was truly
oriented towards the screen, but existing gaze
estimation methods are difficult to deploy reliably at
scale. Research priorities include:
● Scalable Eye -Tracking: Cost-effective,
scalable solution for  eye-tracking in retail
environments.
● Neurophysiological Signals:  EEG,
pupillometry, and cognitive engagement indicators.
● Implicit Interaction:  Touchscreen, QR
codes, and gesture recognition as engagement
proxies.
● Validation Studies:  Ground-truth
attention measurements to calibrate probabilistic
models.
6․3 Cross-Screen Attribution
As consumers move across physical and digital
spaces, connecting DOOH impressions to
downstream consumer actions has become critical to
understanding the full consumer journey. However,
establishing this link has posed a technical challenge
for the advertising industry. Key research challenges
include:
● Multi-Touch Attribution:  Linking
DOOH impressions to online/mobile conversions.
● Unified Measurement:  Combined
measurements for DOOH, mobile, desktop, and TV.
● Privacy-Preserving Linking:  Attribution
without individual-level tracking.
● Causal Inference:  Deals with
distinguishing correlation from causation in
exposure-outcome models.
6․4 Industry Standardization
However, technical innovation alone will not close
the measurement credibility gap for DOOH and
agreements around common definitions‚ audits and
transparency are necessary across the industry.
Standards initiatives have several purposes:
● Measurement Standards:  Industry-wide
definitions (IAB, MRC, DPAA frameworks).
● Audit Frameworks:  Independent
verification and certification programs.
● Transparency Requirements:
Methodology disclosure and accuracy reporting
obligations.
● Data Sharing:  Anonymized benchmark
datasets for research and calibration.

Conclusion
This paper has illustrated how the DOOH
advertising industry has a range of systems to
measure impressions that span computer vision,
multimedia systems, mobile computing and
advertising analytics. Key impression metrics, such
as traffic counting, dwell ti me, demographic
modeling and OTS calculation, can be combined to
create an audience profile for media planning and
programmatic campaign execution.
Improved computer vision, mobile location
analytics, and infrastructure for programmatic
advertising are increasing measurement accuracy
and narrowing the gap between estimated and actual
audience exposures. Remaining challenges include
variability in sens or performance due to
environmental factors, statistical and other
uncertainties in pedestrian modeling, privacy -

International Journal of Intelligent Systems and Applications in Engineering                      IJISAE, 2026, 14(1s), 688–697 |  697

preserving computation, and development of
common market metrics.
It includes areas such as privacy -preserving
measurement methodologies, attention verification
tools, cross -screen attribution, and standardization
efforts. A transparent, auditable, and standardized
impression measurement infrastructure is important
for enabling the sustainable development of DOOH
as a reliable data -driven advertising channel. The
depth and quality of the channel's advance will also
rely on the strength and openness of its measurement
infrastructure as much as on the enhancement of
screen and creative capabilities.

References
[1] Michel Wedel and Rick Pieters, Visual
Marketing: From Attention to Action. New York,
NY, USA: Routledge, 2015. [Online]. Available:
https://repo.darmajaya.ac.id/5815/1/Michel%20We
del%2C%20Rik%20Pieters%20-
%20Visual%20Marketing_%20From%20Attention
%20to%20Action%20%28Marketing%20and%20
Consumer%20Psychology%29-
Lawrence%20Erlbaum%20%282007%29.pdf
[2] Yu Zheng, "Trajectory data mining: An
overview," ACM Transactions on Intelligent
Systems and Technology, vol. 6, no. 3, pp. 1 –41,
May 2015. [Online]. Available:
https://dl.acm.org/doi/epdf/10.1145/2743025
[3] Dirk Helbing and P´eter Moln´ar, "Social force
model for pedestrian dynamics," Arvix, vol. 51, no.
5, pp. 4282 –4286, May 1998. [Online]. Available:
https://arxiv.org/pdf/cond-mat/9805244
[4] Arvind Narayanan and Vitaly Shmatikov,
"Robust de-anonymization of large sparse datasets,"
[Online]. Available:
https://www.cs.cornell.edu/~shmat/shmat_oak08ne
tflix.pdf
[5] Richard Szeliski, Computer Vision: Algorithms
and Applications, 2nd ed. Cham, Switzerland:
Springer, 2010. [Online]. Available:
https://eclass.hmu.gr/modules/document/file.php/T
M152/Books/Computer%20Vision%3A%20Algori
thms%20and%20Applications%20-
%20Szeliski.pdf
[6] Xucong Zhang, et al., "Appearance -based gaze
estimation in the wild." [Online]. Available:
https://openaccess.thecvf.com/content_cvpr_2015/
papers/Zhang_Appearance-
Based_Gaze_Estimation_2015_CVPR_paper.pdf
[7] J. K. Aggarwal And M. S. Ryoo, "Human
Activity Analysis: A Review," Acm Computing
Surveys, Vol. 43, No. 3, Pp. 1 –43, Apr. 2011.
[Online]. Available:
Https://Dl.Acm.Org/Doi/Epdf/10.1145/1922649.19
22653
[8] Andrea Hess, et al., "Data -driven Human
Mobility Modeling: A Survey and Engineering
Guidance for Mobile Networking," ACM
Computing Surveys Volume 48, Issue 3 Feb 2016.
[Online]. Available:
https://dl.acm.org/doi/epdf/10.1145/2840722
[9] Ayman Farahat and Michael Bailey, "How
effective is targeted advertising?" in Proc. 21st Int.
World Wide Web Conf. (WWW), Lyon, France,
2012, pp. 111 –120. [Online]. Available:
https://dl.acm.org/doi/epdf/10.1145/2187836.21878
52
[10] Virginio Cantoni, et al., "Challenges for data
mining in distributed sensor networks for real -time
human detection and tracking," in Proc. 18th Int.
Conf. Pattern Recognition (ICPR), Hong Kong,
China, 2006, vol. 1, pp. 1162 –1167. [Online].
Available: https://scispace.com/pdf/challenges-for-
data-mining-in-distributed-sensor-networks-
3it58v2v2r.pdf
