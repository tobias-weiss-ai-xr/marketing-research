---
title: 'Auditing Apple''s DifferentialPrivacy.framework: Implementation Bugs, Misconfigurations, and Practical
  Risks'
url: https://arxiv.org/abs/2605.21378
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Rishav Chourasia
- Ergute Bao
- Uzair Javaid
- Xiaokui Xiao
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.21378
pages: 19
chars: 98745
fetched_at: '2026-11-08T13:01:36+00:00'
kb_version: 1
---

# Auditing Apple's DifferentialPrivacy.framework: Implementation Bugs, Misconfigurations, and Practical Risks

Auditing Apple’s DifferentialPrivacy.framework: Implementation Bugs,
Misconfigurations, and Practical Risks
Rishav Chourasia ∗†, Ergute Bao ‡, Uzair Javaid †, Xiaokui Xiao ∗
∗National University of Singapore
†Betterdata.ai
‡Mohamed bin Zayed University of Artificial Intelligence
Email:{rishav, uzair}@betterdata.ai, baoergute8@gmail.com, xkxiao@nus.edu.sg
Abstract—Since 2016, Apple claims that the device analytics it
collects to improve user experience are protected by differential
privacy (DP). Running on over 2.35 billion Apple devices
today,1 their DP framework gathers a variety of sensitive data
ranging from contents of photos to COVID-19 vaccination
status. However, despite strong community interest, Apple
has not open-sourced its privatization algorithms, impeding
independent researchers from verifying its privacy claims and
testing for privacy violations. We perform a deep audit of
Apple’s client-side DP framework on macOS Sonoma 14.2
and Sequoia 15.6 by reverse engineering its native binaries
and building runtime interfaces to execute Apple’s deployed
mechanisms. Our audit covers nearly all deployed algorithms,
including Count Median Sketch (CMS) and Hadamard-CMS
from Apple’s white paper [1], and the Prio protocol for secure
aggregation (SecAgg), which Apple uses for learning iconic
scenes [2].
We report multiple issues. Every algorithm in Apple’s
framework that relies on floating-point noise fails to meet
its advertised DP and zero-knowledge (ZK) proof guarantees.
These violations happen because the DP framework uses in-
secure noise generators that are known to have floating-point
vulnerabilities since 2012. We also discover that the SecAgg
protocols in Apple’s DP framework are configured with local
DP disabled, uploading data without any local DP protection.
Our audit provides evidence of DP violations in 5 out of
9 audited mechanisms, impacting 87% of data collection in
macOS Sonoma and 68% in Sequoia. These vulnerabilities
are exploitable by any party with access to pre-aggregation
logs. We found instances on the open internet of leaked iPhone
logs that can be decoded to recover private information, such
as domains visited in Safari and emojis typed on the iPhone
keyboard. We responsibly disclosed these vulnerabilities to
Apple; the concerned mechanisms are now deprecated.
1. Introduction
Differentially private (DP) data collection has become a
popular method for gathering user insights. Its applications
1. Source: MacRumors report on Apple’s worldwide active device count.
range from enterprise use-cases like Google Trends [3],
Meta’s COVID-19 mobility reports [4], and Windows OS’s
analytics [5], to government tasks like the US Census Bu-
reau’s demographic data release [6]. The privacy-enhancing
computation market was valued at USD 5.2 billion in 2024.2
When used correctly, DP algorithms for data-aggregation
provide a mathematical guarantee that the contributing user’s
privacy remains protected. Such a guarantee is ensured by
deliberately introducing carefully-calibrated noise locally in
the device data before uploading it to the servers. Ap-
ple is arguably the industry leader in secure and privacy-
preserving data aggregation technology. Having announced
the adoption of DP as early as in 2016 for collecting device-
analytics in iOS 10 [7], the company demonstrated its strong
commitment with a white paper detailing its large-scale
architecture for its DP framework [1] in 2017. Since then,
Apple has secured numerous patents on distributed learning
and aggregate trend analysis with DP [8]–[15]. Apple has
also publicly emphasized its commitment to privacy through
marketing and research communications [16]–[19]. Today,
Apple’s DifferentialPrivacy.framework is present in every
device running Apple’s operating systems—iOS, iPadOS,
macOS, watchOS, tvOS, and visionOS. 3
Yet, unlike its competitors like Google, Apple has
not open-sourced its DifferentialPrivacy.framework. Conse-
quently, third party researchers have been prevented from
validating the correctness of Apple’s critical privacy algo-
rithms, leading privacy experts to question the real-world
effectiveness of the deployed techniques [20], [21]. This
lack of transparency hinders independent verification: as
with cryptographic primitives,differentially private algo-
rithms are difficult to implement correctly—there are many
examples of flawed implementations with subtle bugs that
do not meet their configured DP guarantees [22]–[26].
This paper presents anindependent, deep-dive privacy
audit of Apple’s DifferentialPrivacy.framework, focusing on
the versions deployed in macOS Sonoma 14.2 (released on
Dec 11, 2023) and Sequoia 15.6 (released on July 29, 2025).
2. Source: Privacy-enhancing computation market report.
3. Sources: public wiki, dyld header dumps, prior research, device ana-
lytics & Apple intelligence privacy policies, AppleTV user-guide and more.
arXiv:2605.21378v2  [cs.CR]  21 May 2026

Our work surgically deconstructs the black-box nature of
the framework by decompiling its native binaries to extract
Objective-C runtime headers. We then build custom executa-
bles that dynamically load the framework to execute Apple’s
native privatization algorithms, allowing us to perform a
combination of static analysis and runtime observation. This
goes beyond all prior analyses of Apple’s DP algorithms or
frameworks as by recovering executable interfaces to the
shipped binaries themselves, we audit the native outputs
on modern Apple OSs. Through this approach, we uncover
defects that lead to practically exploitable vulnerabilities in
several core privatization algorithms. We not only design
decoders that can de-noise and extract user information
from analytics data destined for Apple’s servers, but we
also demonstrate realistic exploits that external attackers
can mount on leaked data. We found numerous real-world
instances where these private device-analytics logs have
leaked onto the open internet—through user forums, social
media, and public code repositories like GitHub—exposing
private data through harmless-looking ciphertexts.
Our findings contradict Apple’s claims regarding the
privacy of collected device analytics through their DP
framework. Using state-of-the-art (SOTA) privacy auditing
techniques [27], [28], we providestatistically-significant
evidencethat Apple’s implementation of these critical mech-
anisms systematically violates their claimed differential pri-
vacy and zero-knowledge (ZK) proof guarantees. We find
floating-point vulnerabilities in Laplace and Gaussian pseu-
dorandom number generators (PRNGs) that are central to
several DP and secure aggregation (SecAgg) algorithms
actively used to collect device data for187out of276(i.e.,
≈68%) property keys in the macOS Sequoia 15.6 and160
out of185(i.e.,≈86%) keys in macOS Sonoma 14.2.
More concerningly, we find that Apple’s SecAgg proto-
cols arepurposely configured to not be differentially private.
AlthoughSecAgg is fully compatible with DP[29], [30] and
the implemented protocols do support DP with an optional
flag that can be enabled, our audit shows that the majority of
configurations do not enable this protection. We demonstrate
how any data collected this way can bereconstructed exactly
on a malicious Apple server(or by an external adversary, if
leaked). We also highlight that the design of Apple’s SecAgg
protocols break a core tenet of multiparty computation
(MPC) by sending all the cryptographic shares of users’
data to a single (potentially untrusted) leader server.
Finally, even for the few DP mechanisms that passed our
audit, we find their configured DP budgets are excessively
large, often exceedingε= 6. Such highεvalues signif-
icantly erode privacy; in the standard binary hypothesis-
testing interpretation of pure DP, anε= 6guarantee is weak
enough to allow membership inference success as high as
eε/(1 +eε)>99.75%[31]. Collectively, our findings reveal
that Apple’s implementation of differential privacy does not
fully match its public claims, raising questions about the
company’s commitment to the privacy of its users. Figure 1
shows the key-names of these collected data and the extent
of the violations per our audit on macOS Sonoma 14.2. We
detected most of these violations in Sequoia 15.6 as well.
Figure 1. Distribution of DP mechanisms identified within macOS Sonoma
14.2 (inner ring), paired with the specific property keys configured for data
collection using these mechanisms (outer ring). The gradient represents
the severity of the associated privacy violation. We quantify the severity
as the difference between the claimed DP upper bound (as per the ‘Pri-
vacyParameter’ attributes in the ‘com.apple.dprivacyd.keyproperties.plist’
configuration file) and the lower boundˆεlower on thetruedifferential privacy
parameter for which we have 95% confidence based on our auditing results.
Related Work.Some of our findings on implementation er-
rors are related to floating-point vulnerabilities in differential
privacy. Mironov [23] first demonstrated that the inverse-
sampling method for Laplace distributions introduces irreg-
ularities that break DP guarantees. Subsequent work [32]–
[34] uncovered similar vulnerabilities in various sampling
techniques for continuous distributions and developed pri-
vacy attacks. We specifically build upon the attacks proposed
by Mironov [23] and Jin et al. [32], extending their attack
principles to target the Gaussian and Laplace distribution
sampling methods used in Apple’s binaries.
To empirically validate our findings, we employdiffer-
ential privacy auditingtechniques, which estimate a mech-
anism’s DP constants by conducting membership inference
attacks [27], [35]–[38]. We use the Bayesian auditing ap-
proach by Zanella-B ´eguelin et al. [28], incorporating refine-
ments from Nasr et al. [39] to derive mechanism-specific
bounds on the true DP parameters of Apple’s mechanisms.
Our contribution is to operationalize these auditing tech-
niques for Apple’s closed-source implementations by reverse
engineering the framework, building executable interfaces,
and designing mechanism-specific attacks and log decoders

of real system outputs.
Prior analyses of Apple’s DP deployment address differ-
ent mechanisms and questions. Gadotti et al. [40] analyzed
practical leakage in Apple’s Count Mean Sketch using pool-
inference attacks derived from Apple’s published CMS de-
sign and parameters [1]. Tang et al. [41] offered an important
early study of Apple’s 2017 macOS 10.12 deployment, clar-
ifying the framework’s system design and privacy-budget
configuration and renewal policies. In contrast, we audit
Apple’s current DifferentialPrivacy.framework at the imple-
mentation level: we reverse engineer the shipped binaries,
construct executable interfaces to the deployed mechanisms,
and evaluate their native outputs across a much broader and
higher-budget deployment.
2. Preliminaries
LetM:X →Prob(Y)be a randomized algorithm that
takes as input a record from the data universeXand pro-
duces a random outcome in the output spaceY. In this paper,
Mis the device-side randomizer executed before any report
is uploaded to Apple, i.e., thelocaldifferential privacy (local
DP) setting. By contrast, incentral(orglobal) differential
privacy, a trusted curator first collects raw data and only
then releases a randomized aggregate or statistic [42], [43].
Differential privacy ensures privacy in the form ofplausible
deniability: an observer looking at an outcomeY∼ M(X)
is unable to accurately determine whether the input was
X=xor an alternateX=x ′.
Definition 2.1(Differential Privacy [44]).A mechanismM
is(ε, δ)-differentially private((ε, δ)-DP) if for allx, x′ ∈ X,
with the output distributionsM(x),M(x ′)denoted asP, Q
respectively, the following condition holds:
∀S⊂ Y:P(S)≤e ε ·Q(S) +δ.(1)
For the local-DP mechanisms studied here, this condition
compares the distributions of theuploaded reportproduced
on a single user’s device under two possible raw inputsx
andx ′. For smallϵandδ, withδ <10 −5 andϵ <1,
an(ϵ, δ)-DP guarantee implies minimal privacy risk: chang-
ing an individual’s data changes the outcome probability
by at most a factor ofe 1 ≈2.718with over99.999%
probability. Although each privatized sample carries limited
information, their aggregation permits learning population
statistics with meaningful accuracy. For example, estimating
the population mean 1 n Pn i=1 Xi under local(ε, δ)-DP for Xi ∈[0,1]yields an expected root-mean-square error of
O(
p
ln(1/δ)

ε√n)using the Gaussian mechanism [42]. To
contextualize this, even with(ε, δ) = (1,10 −5), aggregating
data from one million users incurs less than0.373%error,
despite each user’s submission having an expected root-
mean-square error of over373%.
Secure Aggregation.The objective ofsecure aggrega-
tionis to compute the global sumA= Pn i=1 M(Xi)
without revealing any individualM(X i)any more than
what could be inferred from the aggregateA. Achiev-
ing this requires extending the trust boundary beyond the
user’s device to a group ofmexternal servers, each as-
sumed to behonest but curious. In this setting, every user
splits their valueM(X i)intomcryptographic fragments
[M(Xi)]1,· · ·,[M(Xi)]m, sending one fragment to each
server. Each server locally aggregates its received secret-
shares as[A] j = Pn i=1[M(Xi)]j. When the servers jointly
combine their partial aggregates, the true sum is recovered
as Pm j=1[A]j =A, without exposing any individualM(X i).
Vanilla SecAgg protocols are susceptible to poisoning at-
tacks where one user can corrupt the aggregateAby sending
malicious shares to the servers. Verifiable SecAgg protocols
like Prio [29] provide robustness against such attacks by
requiring users to additionally send asecret-shared non-
interactive proof(SNIP), which is a zero-knowledge (ZK)
proof of correctness of their submitted data. The servers can
use these secret-shares of a SNIP to collaboratively check
the syntactic validity of a user’s submission, without ever
seeing their data in the clear.
SecAgg protocols exhibit a strong synergy with local DP
mechanisms: the aggregateAenjoys a considerably stronger
amplified DP guarantee than individualM(X i),provided
that we trust that at least one server remains honest[45].
Privacy Auditing.While DP provides a theoretical upper
bound on information leakage—typically derived through
formal mathematical analysis—these guarantees may fail
in practice if the analysis is flawed or the implementation
is buggy. Such discrepancies are not rare, and numerous
works have been devoted solely to uncovering analytical
or implementation errors in published mechanisms [22]–
[24], [26], [46]. To complement theoretical proofs,privacy
auditingtechniques have emerged as a practical means to
obtain empirical lower bounds on the true DP parameters.
By running privacy attacks on the implementation directly,
these audits can reveal when empirical lower bounds con-
tradict theoretical upper bounds, or otherwise assess the
tightness of existing analyses [27], [28], [34], [36]–[38]. We
describe the methodology used in this paper in Appendix B.
3. System Overview of Apple’s DP Framework
This section describes Apple’s client-side system archi-
tecture for collecting device analytics data using differential
privacy. Our analysis is based on an inspection of system
files, configurations, binaries, and logs from macOS Sonoma
14.2 (build 23C64) and Sequoia 15.6 (build 24G84).
Framework’s Workflow.At the heart of the architecture
is DifferentialPrivacy.framework, found within ‘/System/Li-
brary/PrivateFrameworks’, which is a bundle containing a
dynamic library(DYLIB) and its associated assets. This
library provides the full suite of DP and SecAgg function-
alities, accessible through its DPServer class, which runs as
a system daemon named ‘dprivacyd’.
Upon startup, the ‘dprivacyd’ system daemon initializes
several periodically scheduled background processes. These

Figure 2. Overview of the design of DifferentialPrivacy.framework.
processes are essential for tasks like managing the privacy
budget, maintaining and cleaning up local storage, and
generating report logs. Once initialized, the server begins
listening for XPC (Cross-Process Communication) requests
from other applications that want to record analytics data.
It can record a variety of analytics data-types, including
strings, boolean values, and numerical data. To ensure data
integrity and security, the XPC listener only accepts con-
nections from applications holding a special entitlement
reserved exclusively for Apple’s own applications.
The ‘dprivacyd’ daemon relies on a set of hardcoded file
paths—stored within the DYLIB’s binary in the DPStrings
class—to locate key resources like the database maintaining
the DP ledger, the directory where reports are generated, and
configurations for privacy budget and algorithm parameters.
This configuration data governs the privatization process:
when an app requests to record data, ‘dprivacyd’ uses
these internal configs to determine the specific privatization
algorithm, its corresponding parameters, the amount to debit
in the DP ledger, whether the analytics report should be
queued locally or uploaded immediately, and other settings.
Figure 2 provides an overview of how the components of
this DP framework interact to collect device analytics data.
Privatization Algorithms.DifferentialPrivacy.framework
also contains the core implementations of Apple’s Local
DP mechanisms and secure aggregation protocols, including
Count Median Sketch [1], PI-RAPPOR [18], and Prio [29].
The ‘dprivacyd’ service uses these algorithms to privatize
the sensitive analytics data requested for upload by autho-
rized apps. Our analysis found 14 such algorithm fami-
lies in production on macOS Sonoma 14.2. Our DYLIB
hijack (described next) successfully interfaced with the
nine families that drive almost all active collections stud-
ied in this paper: NumberRandomizer, CMS, HCMS, PI-
RAPPOR, OneBitHistogram, Prio, Prio++, Prio++Metadata,
and Prio++Metrics. The remaining Sonoma families were
wrapper or specialized variants, including PrefixTree, BSSF-
PwOHE, and PrioCMS, that we did not observe driving
any active user-data collection in the analyzed deployment
(cf. blue wedges in Figure 1’s outer circle).
Following the upgrade to macOS Sequoia 15.6, some
historical mechanisms were replaced by newer algorithms
like Prio3 and PINE that according to Apple follow public
designs [30], [47], [48] (cf. Appendix A.1); our DYLIB hi-
jack worked for seven (7) of the 14 families there. Although
we did not instrument these two new client-side variants, the
same dynamic-loading methodology should extend to them.
DP Budget Ledger.All recorded values, the corre-
sponding algorithm parameters, and timestamps are locally
stored in an SQLite database named ‘DifferentialPrivacy-
ClassC.db’, found in ‘/private/var/db/DifferentialPrivacy/’.
This database also includes a table named ‘ZPRIVACYBUD-
GETRECORD’, which tracks the DP budget balance for
every configured property collected across the system.
Analytics Logs.The database directory also contains ‘Re-
ports/’ and ‘Retired/’ subdirectories where the analytics logs
are generated. Created by the report-generator periodic task,
these logs are plain text files with prefixes like ‘Dedisco’,
‘DifferentialPrivacy’, or ‘PrivacyPreservingMeasurements’.
In iOS and iPadOS, these staged reports can be viewed
by navigating to Settings⟩Privacy & Security⟩Analytics
& Improvements⟩Analytics Data. A subsequent report-
maintainer task periodically rotates these files into the ‘Re-
tired/’ subdirectory before deleting older records.
System Integrity Protection.We note that Apple en-
abledSystem Integrity Protection(SIP) on many associated
directories for its DP framework following the reverse-
engineering work by Tang et al. [41]. In order to examine
those paths, we had to disable SIP on our testing devices.
4. Hijacking DifferentialPrivacy.framework
Apple’s operating systems are built on a foundation of
bothpublic and private frameworks. Public frameworks,
such as MediaPlayer.framework and UIKit.framework, are
documented and supported for all third-party develop-
ers. Conversely, private frameworks like DifferentialPri-
vacy.framework are internal components reserved exclu-
sively for Apple’s own applications and system services.
Apple actively prevents third-party use of these internal
components through several mechanisms: refusing to re-
lease documentation, scanning App Store submissions for
linked private frameworks, and requiring special entitle-
ments within the application sandbox to access its resources.
To use a framework, an executable must be compiled
against its header files (with a .h extension), which declare
the available classes and functions within its DYLIB. Pro-
grams can incorporate these functionalities in two ways.
The first isdynamic linking, where the static linker includes
the library’s symbols as dependent libraries during compile
time. When the program launches, thedynamic link editor

1#import <Foundation/Foundation.h>
2#import "_DPNumberRandomizer.h" // Header extracted from ‘dyld_shared_cache’ using class-dump
3
4int main() {
5/ * Dynamically load the DP framework */
6NSString *path = @"/System/Library/PrivateFrameworks/DifferentialPrivacy.framework";
7NSBundle *framework = [[NSBundle alloc] initWithPath:path];
8[framework load];
9
10/ * Initialize and run DifferentialPrivacy.framework’s NumberRandomizer */
11double input = 0, epsilon = 1, range = 1;
12id mech = [[NSClassFromString(@"_DPNumberRandomizer") alloc] initWithRange:range epsilon:epsilon];
13NSLog(@"Sample: %@", [mech randomize:@(input)]);
14} // > gcc -framework Foundation laplace.m -o laplace
Figure 3. A program demonstrating how to dynamically load Apple’s DifferentialPrivacy.framework and access its NumberRandomizer functionality.
(ordyldfor short) handles the automatic loading and symbol
resolution of these shared libraries into memory. The second
and more flexible approach isdynamic loading, where the
static linker adds no dependency information. Instead, the
program code itself explicitly loads the library at runtime
(e.g., by calling theload()method) to resolve the necessary
symbols. Thedyldhandles both scenarios, ensuring depen-
dent libraries are loaded at launch and managing runtime
requests for dynamically loaded libraries. Crucially, as long
as the framework is properly linked or loaded, even a
third-party program can access and use the functionalities
implemented in Apple’s private frameworks.
Apple provides neither the documentation nor the header
files for its DifferentialPrivacy.framework. However, using
open-source tools such as class-dump and ipsw, we extract
the header files directly from the framework’s binary. 4 Re-
covered headers are available in the associated artifact [49].
We rely ondynamic loadingin our programs to interface
with DifferentialPrivacy.framework to avoid the complaints
by the static linker regarding unresolved external references
during compilation. This flexibility comes with a price as
errors due to incorrect declarations in the headers or missing
symbols may result in a runtime crash. We debug such
crashes by inspecting the relevant parts of the DYLIB’s
binary with decompiling software like Hopper, IDA Pro,
and Binary Ninja. Figure 3 illustrates an example program
that successfully executes the NumberRandomizer which
implements the Laplace mechanism. With some hit-and-
trial, we built an interface to run almost all privatization
mechanisms in DifferentialPrivacy.framework. We validated
recovered declarations against both binary evidence (e.g.,
constants, types/casts, selector usage, and branch structure)
and runtime behavior through executable instrumentation;
mismatches typically caused runtime failures that we iter-
atively resolved. This lets us instrument Apple’s shipped
implementations directly, enabling tight privacy audits and
practical reconstruction attacks from logs, as shown later.
4. All frameworks’ binaries used to be located inside respective subdirec-
tories in ‘/System/Library/’. However, since macOS Ventura 13, all system
binaries are consolidated into a single ‘dyld shared cache’ file. We extract
the DP framework’s binary from it using dyld-shared-cache-extractor.
LLM’s Aid in Binary Analysis.Analyzing decompiled
code can be challenging due to many reasons, like changes
in logic due to the optimizations made by the compiler
and the absence of meaningful function/variable names. To
understand some of the complex parts of the decompiled
binary, we sought assistance from Large Language Mod-
els (LLMs), specifically ChatGPT 4o and Gemini 2.5 Pro
models, in deciphering the underlying code. Concretely, we
used LLMs to help interpret decompiled Objective-C code:
we pasted a snippet from Hopper, IDA Pro, or Binary Ninja
together with our suspected functionality and asked for a
cleaner Objective-C or pseudocode rewrite. We treated these
outputs only as hypotheses. Any interpretation we relied on
had to match binary evidence such as constants, types/casts,
and branch logic, and also be consistent with runtime behav-
ior observed through our executable instrumentation. When
an LLM interpretation disagreed with this evidence, we
discarded it. When provided with accurate context regarding
a snippet’s suspected functionality, we found these LLMs’
interpretations to be helpful in our analysis.
Circumventing Apple’s Security.Our approach bypasses
the security boundary created by Apple’sSandboxand
Hardened Runtimefeatures that protect the ‘dprivacyd’
daemon. This is because the framework logic resides within
DifferentialPrivacy.framework’s binary, while ‘dprivacyd’ is
merely a service intended to act as its gatekeeper via the
XPC protocol. By employing dynamic loading to bring the
framework’s code directly into our application’s process
space, we eliminate the need to establish a secure XPC
connection with ‘dprivacyd’. Instead, our program directly
calls the privacy functions implemented within the frame-
work’s DYLIB, avoiding all the high-level security checks,
entitlements, and system service restrictions that would oth-
erwise be enforced against any third-party app attempting
to communicate with the protected daemon.
5. Threat Models and Attack Scenarios
Our analysis considers multiple threat models from the
perspectives of both Apple’s servers (assuming them to be
dishonest, collusive, and curious) and external adversaries.

Reconstruction Attacks.In our primary threat model, we
assume that the adversary can access the privatized analytics
records generated on an Apple device. The adversary’s
objective is todecodemeaningful personal information from
these analytics records. The attacks are conducted in an
offline setting—without interacting with the users. To extract
personal data, the adversary exploits vulnerabilities in the
privatization algorithms used to generate the records. This
threat model applies in the following scenarios:
A)Apple’s servers.In its “Approach to Privacy” page,
Apple claims that personally identifiable information
(PII) is “removed from reports before they’re sent to
Apple or protected by [...] Differential Privacy.” We
examine this claim by testing whether the uploaded
records indeed provide sufficient privacy such that even
Apple cannot infer personal user information from the
collected data.
B)Third-party attackers.This scenario involves an ex-
ternal adversary who gains unauthorized access to an-
alytics logs originating from iPhones, iPads or other
Apple devices. This is a post-export threat model: we
do not assume that arbitrary third-party apps can bypass
Apple’s sandbox and read these files directly on-device.
Rather, the adversary gains access after user-exportable
diagnostics or staged analytics logs leave the device,
for example through log-stealer malwares, diagnostics
sharing or public leaks. Once this happens, the attack
is fully offline. In particular, we observed over fifty
publicly-posted instances of such logs on Apple’s of-
ficial forum, Pastebin, GitHub, Reddit, and even on
Instagram. (To avoid resurfacing potentially sensitive
user data, we omit direct URLs.) Unlike screenshots
or photos, these logs contain machine-readable encoded
measurements whose sensitivity is not obvious to users.
The ability to decode such logs presents a serious
privacy risk to unsuspecting users and is difficult for
Apple to mitigate, as these logs are already public.
Membership-Inference Attacks.In this threat model, the
attacker knows that the mechanism’s input is eitherx 0 or
x1 and seeks to determine which of the two was used
based on the observed output. By repeating this test across
many independent runs, where the input is randomly chosen
betweenx 0 andx 1, we measure the attacker’s prediction
accuracy to derive empirical lower-bound estimates on the
the true level of DP of the mechanism. We highlight that
this threat model is not intended to reflect a real-world
attack setting; rather, it provides a controlled experiment for
auditing the DP guarantees claimed by Apple’s framework.
6. Floating-Point Vulnerabilities
Many privatization algorithms in Apple’s DP framework
rely on continuous distributions as their core components.
However, thefinite-precisionof digital systems prevents
exact representation of continuous random variables. Stan-
dard numeric libraries like random.h in C++ and NumPy or
PyTorch in Python approximate these variables using IEEE
754 floating-point arithmetic, which introduces subtle irreg-
ularities. When used to generate noise in DP applications,
these imperfections can break the privacy guarantees [23].
As such, modern DP frameworks employ specialized, cryp-
tographically secure noise generation methods [50]–[52].
6.1. Laplace Mechanism
We find that the LaplaceNoiseGenerator in Apple’s DP
framework, used by their NumberRandomizer class imple-
menting the Laplace mechanism [53], employs the inverse
transform sampling method [54] as outlined in Algorithm 1.
This method leverages the property that any random variable
Ywith cumulative distribution function (CDF)F(t) =
Pr[Y≤t]can be generated from a uniformly distributed
random variableU∼[0,1]through the transformation
Y←F −1(U). This follows from the fact that for allt∈R,
Pr[F −1(U)≤t] = Pr[U≤F(t)] =F(t).(2)
Algorithm 1:inverse sampler forLap(λ)
Input:Scale parameterλ
Result:A single sampleY∼Lap(λ)
1uniformly sampleU∼[0,1]
2letF −1(u) := sign  1 2 −u  ·λln  1−2

u− 1 2


3Y←F −1(U)/ /F −1(·)is the inverse CDF ofLap(λ)
4Return:Y
Vulnerability.The framework implements the arithmetic in
Algorithm 1 using double-precision numbers. By the IEEE
standard, thisdoubledatatype allots 1 bit for sign, 52 bits
for the mantissa, and 11 bits for the exponent, and together
they can represent numbers of the following form.
Yin memory:s
sign
eeeeeeeeeee
exponentE
b51b50...b2b1b0
mantissa
Real value ofY: (−1) s

1 +
52X
i=1
b52−i ·2 −i
!
×2 E−1023
To produce a sampleY∼Lap(λ), the pseudorandom
generator first samples a random 32-bit unsigned integer
and divides it by its max value2 32 −1to get a double
Uin range[0,1]. Then, it computes its inverse CDF value
F −1(U)using floating-point arithmetic and returns it.
Back in 2012, Mironov [23] noted that the doubleU
produced this way does not have support over all the 64-
bit doubles in the range[0,1]. Furthemore, even if care
was taken to include all the doubles in the support ofU,
Mironov [23] noted that applying the inverse CDFF −1(·)
in floating-point arithmetic still results in plenty of double
values missing from the support ofY. As a result, when used
in a Laplace mechanismM Lap(x) =q(x) + Lap(∆ q/ε)to
privatize a queryq:X →[0,∆ q], this generator leads to
anε-DP violation: because certain double values can never

occur for one input but may appear for another, detecting
such aninfeasibleoutput providesincontrovertibleevidence
of which input was used (say, amongx 0 orx 1).
Membership-Inference Attack.Based on the discovered
floating-point vulnerability, we design an efficient attack
againstM Lap as implemented by Apple’s NumberRandom-
izer. Described in Algorithm 2, our attack tests for the
infeasibility of a candidate inputµgiven an outputYof
the mechanism.
Algorithm 2:ϕ Lap(Y;µ, λ): Isµinfeasible?
Input:Candidate meanµ, outputY, scaleλ
Result: TrueorFalse
1letF(y) := 1 2

1 + sign(y)·

1−e − |y| λ 
2letF −1(u) := sign  1 2 −u  ·λln  1−2

u− 1 2


3Return:µ+F −1(F(Y−µ))̸=Y
Mathematically, this algorithm should always return
Falseregardless of the choice ofµorY, becauseF −1(F(·))
is an identity function. However, floating-point arithmetic
changes this. If outputYwas not sampled fromµ+Lap(λ),
then there is a considerable chance (≈78%) that the condi-
tion in line 3 evaluates toTrue. This happens because the
outputYmight not be in the distribution ofµ+ Lap(λ).
That is, there might not be any doubleU∈[0,1]such
thatµ+F −1(U)precisely equalsY. To check for this,
Algorithm 2 streamlines the search by only testingU=
F(Y−µ), which yields a value closest toY. Conversely,
ifYwas in fact sampled fromµ+ Lap(λ), the test always
finds a match, i.e.,ϕ Lap(µ+ Lap(λ);µ, λ) =False.
Reconstruction Attack.The accuracy of our testϕ Lap is
88.2±1.02%regardless of the choice of DP parameter
ε, which is more than enough for a practical attack. But
we can also boost the accuracy to≈100%by drawing
multiple samplesY 1,· · ·, Ym from the Laplace mechanism
and testing whether any one of them is infeasible for a given
input, i.e. Wm i=1 ϕLap(Yi;µ, λ). At this accuracy level, we
can effectively reconstruct the input perfectly from the noisy
outputs. We find that with access to as few asm= 5samples
from NumberRandomizer with a DP guarantee ofε= 0.2
(i.e.,1-DP guarantee on composition) allows us to accurately
infer the collected property “com.apple.datatype.age” in the
range{0,1,· · ·,100}with90.4±0.91%probability.
Privacy Auditing Result.On running our DP audit (cf.
Algorithm 11 in Appendix B), we find that NumberRan-
domizer violates its DP guarantee. In Figure 4, we show
that our membership testϕ Lap achieves a false-negative rate
(FNR) of22.42±0.38%with a false-postive rate (FPR)
of0.00±0.02%, which constitutes statistically significant
evidence that the true DP parameter exceedsε lb = 5.69.
Given that we configured the mechanism’s parameters to
ε= 1and sensitivity∆ = 1, our audit confirms a DP
violation stemming from floating-point vulnerabilities.
5
 0 5
0.0
0.1
0.2
0.3
0.4
0.5Density / Normalized Frequency
Prediction Group
True Negative
False Positive
Lap(0,1) PDF
0 5
Prediction Group
True Positive
False Negative
Lap(1,1) PDF
 lb = 5.69 with 95% confidence (FPR = 0.00, FNR = 0.22)
Figure 4. Result of our audit on Apple’s NumberRandomizer with DP
parameter set toε= 1detects a DP violation. We run the mechanism
n= 1000times and use testϕ Lap(y;µ= 0, λ= 1)to predict whether
the input wasx 0 = 0orx 1 = 1. The audit used the familyF Lap of
Laplace mechanisms’ trade-offs (cf. Remark B.5) and the significance level
was set toγ= 0.05.
6.2. Gaussian Mechanism
One of Apple’s most widely used PRNGs in the frame-
work, GaussianPRNG, also suffers from floating-point vul-
nerabilities. It implements theMarsaglia polarmethod to
generate pairs of independent Gaussian samples as shown
in Algorithm 3. This method draws independent uniform
variable pairs(U 1, U2)∈[−1,1]from integer samples
V1, V2, untilR=U 2 1 +U 2 2 ≤1. Since points(U 1, U2)are
uniformly distributed within the unit circle, the normalized
vector( U1√ R , U2√ R )is uniformly distributed on the unit circle,
while the radius termρ=
p
−2 log(R)provides the correct
radial scaling for the bivariate normal distribution. Thus,
multiplying the two gives(Z 1, Z2) =

U1√
R ρ, U2√ R ρ  , whose
coordinates are independent standard normal variables.
Algorithm 3:marsaglia sampler forN(µ, σ 2)
Input:Random integersV 1, V2 ∈[−2 31,2 31 −1]
s.t.V 2 1 +V 2 2 ≤2 62 −1, meanµ, varianceσ 2
Result:Two samplesY 1, Y2 ∼ N(µ, σ2)
1R←(V 2 1 +V 2 2 )/(262 −1)
2U 1 ←V 1/(231 −1)andU 2 ←V 2/(231 −1)
3Z 1 ← U1√ R p −2 log(R)andZ 2 ← U2√ R p −2 log(R)
4Return:µ+σZ 1, µ+σZ2
Vulnerability.Similar to the Laplace noise generator,
Apple’s DP framework implements GaussianPRNG using
floating-point arithmetic, which we discover to be vulnerable
as well. Upon examining mechanisms like Prio++ and PINE,
which rely on GaussianPRNG to privatize numeric vectors,
we observe that both generated samples are always used
sequentially. We exploit this in Algorithm 4 by designing an
infeasibility test that determines whether a candidate mean
µis feasible for an output pair(Y 1, Y2).

Algorithm 4:ϕ Gauss(Y1, Y2;µ,σ2): Isµinfeasible?
Input:Candidate meanµ, output pair(Y 1, Y2),
varianceσ 2, testing windowk
Result: TrueorFalse
1Z 1 ←(Y 1 −µ)/σandZ 2 ←(Y 2 −µ)/σ
2R←exp

− Z2 1 +Z2 2 2 × (231−1)2 262−1 
3V 2 ←sign(Z 2)·int
q
R·(262−1)
|Z1/Z2|2+1

4V 1 ←sign(Z 1)·int

V2

 Z1 Z2

 
5forV ′ 1 ∈ {V1 −k,· · ·, V1 +k}do
6forV ′ 2 ∈ {V2 −k,· · ·, V2 +k}do
7Y ′ 1 , Y′ 2 ←marsaglia sampler(V ′ 1 , V′ 2 , µ, σ)
8ifY ′ 1 ̸=Y 1 orY ′ 2 ̸=Y 2 then
9Return: True
10Return: False
Membership-Inference Attack.The above test works like
the Laplace membership test: given a candidate meanµ
we try to recover the integer pair(V 1, V2)that would have
yielded the observed output(Y 1, Y2), then check whether the
polar sampler with those integers yields the same outputs.
Following the attack of Jin et al. [32], we recoverRas:
− Z 2 1 +Z 2 2
2 log(R) = V 2 1 +V 2 2 R(231 −1) 2 = 262 −1 (231 −1) 2
=⇒R= exp

− Z 2 1 +Z 2 2
2 × (231 −1) 2 262 −1 
In principle, testing whetherR·(2 62 −1) =V 2 1 +V 2 2 is
integer would suffice (the basis of Jin et al. [32]’s attack).
However, Apple’s implementation casts the 64-bit doubles
Y1, Y2 to 32-bit floats before returning, losing≈28bits of
precision. This makes attacks much harder: the reconstructed
Reffectively always integral and breaks that simple test.
To overcome this, we augment the attack. We also
use the ratioZ 1/Z2 =V 1/V2 alongside the reconstructed
Rto try and reconstruct(V 1, V2)as closely as possible.
Unfortunately because of the precision loss, many nearby
integer pairs can map to the same observed(Y 1, Y2). Our
attack focuses on thesize of this surrounding area—if the
candidateµis correct, this ambiguity region should be large.
Concretely, we test a windowV ′ 1 ∈ {V1 −k,· · ·V1 +k},
V ′ 2 ∈ {V2 −k,· · ·, V2 +k}and verify whether the Marsaglia
sampler with each(V ′ 1 , V′ 2 )reproduces(Y 1, Y2). If any
neighbour produces a different output, we markµas in-
feasible. With a window sizek= 80this test achieves an
FPR of0.00±0.00%and a TPR of0.25±0.03%, and an
overall balanced accuracy of50.12±0.02%.
As a final enhancement, we increase the attack’s effec-
tiveness by accumulating evidence across multiple Gaussian
sample pairs. Specifically, we used= 1,000samples
(Y1, Y2),· · ·,(Yd−1, Yd)to make a single prediction: a can-
2
 0 2
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40Density / Normalized Frequency
True Negative
False Positive
(0, 2) PDF
2
 0 2
True Positive
False Negative
(1/ d, 2) PDF
 lb = 15.60 with 95% confidence (FPR = 0.00, FNR = 0.28)
Figure 5. Result of our audit on Apple’s Prio++ algorithm, which uses
thed-dimensional Gaussian mechanism withd= 1,000andσ 2 = 1to
guarantee(4.377,10 −5)-DP. The audit was conducted using the described
membership test on inputs,x 0, x1, such thatq(x 0) = ⃗0andq(x 1) =
⃗1/∥⃗1∥. We ran the mechanismn= 1,000times and the audit used the
Gaussian trade-off familyF Gauss and a significance level ofγ= 0.05.
didate meanµ∈ {0,1/
√
d}is infeasible if
d/2_
i=1
ϕgauss(Y2i−1, Y2i;µ, σ2) =True.
Note that this construction effectively describes a mem-
bership inference attack against the Gaussian mechanism
Mgauss(x) =q(x) +N(0, σ 2Id), applied to vector-valued
queriesq:X →R d withL 2 sensitivity of∆ q = 1.
Privacy Auditing Result.We applied this membership test
to audit Apple’s Prio++, which internally uses Gaussian-
PRNG to implement the Gaussian mechanism (see Sec-
tion 7.3 for more details). As shown in Figure 5, our test
for distinguishing betweenq(x 0) = ⃗0andq(x 1) = ⃗1/∥⃗1∥
achieves an FNR of28.90±0.64%at0.10±0.06%FPR,
resulting in an overall accuracy of85.41±0.35%. Per
our audit, these results imply that the true DP parameters
exceedsε lb = 15.6forδ= 10 −5. This indicates a clear DP
violation since the mechanism was configured withσ 2 = 1
and∆ q = 1, which should guarantee(4.377,10 −5)-DP.
7. Problems with Apple’s Secure Aggregation
The protection offered by DP alone does not cover many
other properties that are needed to perform aggregation of
statistics across billions of devices securely. For instance,
DP analytics reports should be bothconfidentialto restrict
access only to authorized servers andverifiableto prevent
malicious clients from manipulating the aggregate. In 2023,
Apple announced in a research highlight [2] that it had
adopted Prio [29] protocol, combined with DP, to collect
annotation tags and location data from users’ photos for
features such as Memories and Places from iOS 17 onwards.
Consistent with this, we find that Apple’s DP framework
implements Prio and several internal variants, including

Prio++, Prio3Sum [55], and PINE [30]. In this section, we
first outline the design and security guarantees of the orig-
inal Prio [29], and then examine Apple’s implementation,
highlighting key deviations that weakens their privacy.
7.1. The Original Prio
Prio [29] is a multiparty computation protocol forsecure
aggregation, which enables a group of servers to compute an
aggregate valueA= P i Yi, without learning any individual
client submissionY i =M(X i), whereX i is the client’s
private data andMprivatizes it locally. Prio’s client-side
protocol operates as follows.
ClientC i
Xi ←Private Data
Yi ← M(Xi)/ /DP mechanism
([Yi]1, . . . ,[Yi]m)←SecretShares(Y i;m)
([πi]1, . . . ,[πi]m)←SNIPs(Y i;m)/ /ZK proof
forj= 1..mdo
pkj ←ServerS j
msg(j) i ←Enc(([Y i]j,[π i]j);pk j)
Sendmsg (j) i to ServerS j
Each clientC i randomly splitsY i intomsecret shares
[Yi]1, . . . ,[Yi]m over a finite fieldFsuch that their aggregate
equalsY i. Alongside the secret shares ofY i, the clients also
create secret shares of a proof of correctnessπ i forY i. Each
pair of shares are sent to a distinct server after encryption
with its public key. Prio’s server-side operates as follows.
ServerS j
skj,pk j ←$ KGen/ /Public keypk j is shared with clients
[A]j ←[0]/ /Initialized with0in the fieldF
fori= 1..ndo
msg(j) i ←C i
([Yi]j,[π i]j)←Dec(msg (j) i ;sk j)
ifVerify([Y i]j,[π i]j;S 1 · · ·, Sm)then
[A]j ←[A] j + [Yi]j
publish[A] j
Each server locally sums the decrypted shares it receives to
obtain[A] j = P i[Yi]j. The global aggregate is recovered by
combining these partial sums as:A= Pm j=1[A]j = P i Yi.
This design ensures that as long asat least one server
remains honest, the others, even if colluding with a subset
of clients, cannot reconstruct any individualY i. In addition
to being confidential, the client submissions through Prio
are alsoverifiable. The second set of secret-shares serve as
a ZK mechanism that allows servers to collectively verify
the correctness of each client’s submission, ensuring that
malformed or adversarial inputs can be filtered, without even
knowing the underlying values.
7.2. Apple’s implementation of Prio
The core security for MPC protocols like Prio funda-
mentally relies on the decentralized control of the servers
performing data aggregation. When all servers are operated
by the same entity in a closed-source cloud environment,
the security assumption relies on operational independence
between servers; from the client vantage, we cannot attest
to that separation. In our analysis, we find that Apple’s
Prio implementation splits each client’s data (Y i =M(X i))
into only two secret shares (m= 2) but transmits both
to the same server endpoint, designated as the “leader.”
Although the shares are encrypted under distinct public keys,
nominally assigning one to the “leader” and other to a
“helper”, there is no external means to verify the intended
separation of decryption capabilities is upheld by Apple,
effectively weakening Prio’s SecAgg guarantees.
Secondly, Apple’s research highlight [2] states that it
employs Prio withε-DP to collect encoded photos attributes,
such as approximate location and scene contents, for training
models that identify iconic scenes. Consistent with this de-
scription, thekeyproperties.plistconfiguration file in macOS
lists numerous properties, including “InsightsIconicScenes”,
“InsightsSafari”, “KeyboardTextInput”, and “ENDiagnosed-
VaccineStatus”, as being collected via Prio. To provideε-DP,
we find that Prio employs thesymmetric one-hot-encoding
mechanismM symOHE, as described in Algorithm 5.
Algorithm 5:M symOHE [45, Algorithm 3]
Input:Data elementX∈ {1,· · ·, d}, parameterε
Result:Bit StringY∈ {0,1} d
1InitializeV, Y← {0} d
2V[X]←1/ /EncodeXas a one-hot vectorV
3fori∈ {1,· · ·, d}do
4Y[i]←
(
V[i]with probability eε eε+1
1−V[i]otherwise
5Return:Y
Algorithm 5 satisfiesε-DP locally,but under the deletion
adjacency model. In this model, the output distribution of
MsymOHE on a data pointXis compared against a refer-
ence distributionBernoulli( eε eε+1 )d, which corresponds to the case where nothing was sent. However, in the standard
replacement adjacency model[45], the same mechanism
only achieves a much worse privacy of2ε-DP.
A closer examination of the configuration files reveals
a concerning inconsistency in how privacy budgets are de-
fined. While most mechanisms specifyεunder the replace-
ment adjacency model, Prio appears to report its guarantees
under the weaker deletion adjacency model. To verify this,
we conducted a privacy audit with a membership test in
which an adversary attempts to distinguish whether the input
Xwas1or2. As shown in Figure 6, the observed success
indicates that the actual privacy loss, i.e., theεperceived by
an adversary, is nearly twice the value configured for Prio.

0.0 0.2 0.4 0.6 0.8 1.0
FPR (T ype I Error)
0.0
0.2
0.4
0.6
0.8
1.0FNR (T ype II Error)
(0.05, 0.44)
1-DP region (Pr[ 1] 1.2 × 10 10)
1.91-DP region (Pr[ 1.91] 0.05)
 lb = 1.91 with 95% confidence
Figure 6. Illustration of our privacy audit on Apple’s Prio implementa-
tion with its DP parameter set toε= 1. The protocol was executed
500times, with the inputXselected randomly from{1,2}. We then
decoded the shares([Y] 1,[Y] 2)to reconstruct the randomized2-bit vector,
Y∈ {0,1}2. Our membership test predictedX= 1if the first bit ofY
was set, and asX= 2otherwise.
Third, the configured privacy budgets for Prio are excep-
tionally large, ranging fromε= 6toε= 8. At such levels,
a one-hot vectorVwith dimensionality as high asd= 10 4
is almost identical to its privatized outputY: they differ by
at most 30 bits with87.57%probability whenε= 6, and by
no more than 5 bits with87.64%probability whenε= 8.
In other words, with such large budgets, a malicious Apple
server can reconstruct sensitive data, such as domains visited
on Safari or contents of pictures in the Photos app, from the
collected device analytics with only asmall margin of error.
Finally, these privacy concerns extends beyond Apple
servers with our discovery ofunencrypted Prio client-shares
publicly available on the internet. These analytics logs con-
tain raw secret-share data that can be decoded and recom-
bined to recover the original private records. Such logs allow
for direct reconstruction of sensitive user by an external
attacker, effectively sidestepping the privacy protections that
Apple’s system tries to provide. Figure 7 shows an example
of this on logs captured from our test iPhone device.
7.3. Apple’s Prio++ and PINE Variants
The original Prio protocol [29] was designed for ver-
ifiable and secure aggregation ofdiscretedata types. Its
SNIP proof system for bound verification scales efficiently
only for integral inputs, specifically, when the arithmetic
circuit representing the proofπinvolves far fewer mul-
tiplications than the size of the underlying fieldF. Con-
sequently, it integrates naturally with discrete DP mecha-
nisms likeM symOHE. To extend its security principles to
continuous domains in a computationally efficient manner,
researchers at Apple have proposed protocols such asSecure
Summation(SS) [56] andPINE[30], which enable verifica-
tion that each client’s contribution has a bounded Euclidean
norm. We find implementations of these mechanisms in the
DP framework as Prio++ and PINE, respectively.
Design of Prio++.Like Prio, Apple’s Prio++ is designed
to securely aggregate analytics data. However, unlike Prio,
which operates on bit sequences, Prio++ handles float vec-
tors. As a result, Prio++ employs a different mechanism for
privatization (i.e., DP guarantee) and for correctness-proof
generation (i.e., ZK guarantee). Specifically, Prio++ takes
a float vectorX∈R d as input and applies the Gaussian
mechanism to privatize it, generatingY=M Gauss(x) =
X/max(1,∥X∥) +N( ⃗0, σ2Id). The inputYis then split
into two secret shares by adding another layer of Gaussian
noise with a distinct variance parameterσ 2 SS as described
in Algorithm 6.
Algorithm 6:SecretShares(Y)used in Prio++
Input:DataY∈R d, secret sharing varianceσ 2 SS
Result:Leader and helper shares[Y] 1,[Y] 2
1seed← $ SGen/ /Generate a random seed
2V∼ N( ⃗0, σ2 SSId)/ /By calling GaussianPRNG(seed; d)
3([Y] 1,[Y] 2)←(Y−V,seed)
4Return:[Y] 1,[Y] 2
This additional noise layer serves two purposes. First,
the noise layer generates two secret shares,[Y i]1 and[Y i]2,
for distribution to the leader and helper server respectively.
After securely aggregating their shares[A] j = P i[Yi]j from
all clients, the servers combine their shares to recover the
aggregateA= [A] 1 + [A]2 = P i Yi, effectively “peeling
off” the second layer of added noise.
Second, it enables integrity verification usingdifferen-
tially zero-knowledge(DZK) proofs, a relaxation of standard
ZK proofs introduced in [56]. With the two shares,[Y i]1 and
[Yi]2, servers can probabilistically verify that∥Y i∥ ≤ρfor
someρ>1before accepting a client’s submission, with-
out revealing excessive information to each other (see [56,
Algorithm 3] for verification details).
Violation of DZK.The floating-point vulnerabilities found
in GaussianPRNG—which we showed in Section 6.2 cause
the Gaussian mechanism used in Prio++ to violate its DP
guarantees—also affect the SecretShares(Y)function (in
Algorithm 6). Because it uses the same flawed PRNG
to generate shares, the resulting leader’s share,[Y] 1 =
Y− N( ⃗0, σ2 SSId), is not nearly as indistinguishable to
N(⃗0, σ2 SSId)as necessary for the DZK property to hold. This
DZK failure is a direct consequence of the shared vulnera-
bility, and we demonstrate it using a membership-inference
attack like the one in Section 6.2. This vulnerability also
affects the DZK property of Prio++Metrics.
7.4. Apple Disables DP in SecAgg Protocols
By design, secure aggregation is intended to serve as an
additional layer of securityon top of the local DP applied
to the device analytics—for sufficiently smallε, this local
ε-DP guarantee is amplified to(O(εlog(1/δ)/ √n), δ)-DP
centrally when aggregating submissions fromnusers [45].

TABLE 1. SUMMARY OF DISCOVERED ISSUES INSECAGG PROTOCOLS
Protocol DP Mech. PRNG for SecretShares ZK(✓/✗)
Violates DP under the replacement adjacency model
PrioM symOHE PrioSeedablePRNG ZK✓
Violates DP due to floating-point vulnerabilities
Prio++M Gauss GaussianPRNG DZK✗
Does not implement DP
Prio++MetadataNonePrioSeedablePRNG ZK✓
Prio++MetricsNoneGaussianPRNG DZK✗
An intention to use this synergy is evident in Apple’s
implementations as all three protocols—Prio, Prio++, and
PINE—include options to enable local DP, either through a
dpflag or directly through a configurationmetadata.
However, we discovered that these protocols arecon-
figured to disable the DP layerfor the vast majority of
collected analytics data. Furthermore, we discover that sub-
variants such as Prio++Metadata and Prio++Metrics are
essentially wrappers around Prio and Prio++ thathard-code
DP to be disabled. This means that data collected under
these variantslacks local differential privacy guarantees.
Our DP audit confirmed this alarming operation as our mem-
bership inference attacks achieved a100%accuracy rate.
Furthermore, Apple’s response to our report acknowledges
that these protocolsintentionally lackDP guarantees (cf.
Appendix A.4). In total, we find that at least40%of the col-
lected data in Sonoma 14.2 and37%in Sequoia 15.6, includ-
ing sensitive properties like “QuickTypeDESPlugin.LSTM”,
“NightangleTraining”, “Siri.GlobalSpeechNNLM”, and “In-
telligencePlatform”, are collected with DP disabled.
7.5. Decoding Prio and Prio++ Logs in iPhones
Apple’s 2017 white paper introducing its DP frame-
work [1] stated that analytics logs generated by the system
would be visible on iOS under Settings⟩Privacy & Security
⟩Analytics & Improvements⟩Analytics Data. Our inves-
tigation finds this to beonly partially truein 2025; over
68%of the collected properties in macOS Sonoma 14.2 are
configured with ‘DirectUpload=true’, meaning they are
transmitted directly to Apple’s servers without generating
any local logs. Nevertheless, we confirmed that a subset
of analytics data continues to be logged locally; over three
months of observation on an iPhone 12 running iOS 18.1.1,
we repeatedly found analytics entries prefixed with ‘Priva-
cyPreservingMeasurements’, as shown in Figure 7.
Examining these logs, ‘share1’ and ‘share2’ attributes
stand out. Our analysis of the SecretShares(Y)implemen-
tation in both protocols reveals that these fields directly
contain theleaderandhelpersecret shares inplaintext—
without any encryption applied. Combined with the ‘algo-
rithmParameters’ attribute present in the same logs, these
three fields are sufficient to fully decode and reconstruct the
original private data.
Specifically, Prio employs a SecretShares(Y)function
similar to Algorithm 6, but replaces GaussianPRNG with
PrioSeedablePRNG and appends a ZK proof, as described
Figure 7. Decoding analytics data from our test iPhone device. The logs
reveal unencrypted ‘share1’ and ‘share2’ fields (representing the secret
shares[Y] 1 and[Y] 2) of the differentially private measurementYuploaded
to Apple’s servers. These plaintext logs allow direct decoding ofY, as
shown on the right. Furthermore, the logs indicate the original OHE of
Xhad a dimensionality of9, privatized withε= 6, leading to a97.80%
chance that the decodedYequals the originalX.
in Algorithm 7. To reconstruct the original data, we in-
Algorithm 7:SecretShares(Y)used in Prio
Input:DataY∈ {0,1} d
Result:Leader and Helper shares[Y] 1,[Y] 2
1seed← $ SGen/ /Generate a random seed
2V∼[0,2 32 −1]/ /By calling PrioSeedablePRNG(seed; d)
3[Y] 1 ←(Y−V,SNIP(Y,seed))/ /share1
4[Y] 2 ←seed/ /share2
5Return:[Y] 1,[Y] 2
vert Algorithm 6 and Algorithm 7 by computingY←
[Y] 1 +PRNG([Y] 2)wherePRNGis PrioSeedablePRNG for
Prio (and its child Prio++Metadata), and GaussianPRNG for
Prio++ (and Prio++Metrics). For Prio, the addition is per-
formed in the finite fieldFover ‘uint32’, while for Prio++,
it is computed in ‘float32’. We verified that this decoding
process works across all four Prio variants, enabling nearly
full recovery of the underlying private data directly from the
analytics logs generated in our test iPhone device, as shown
in Figure 7.
8. Use of Large DP Parameters
We also audit several other DP mechanisms within
Apple’s framework that sample from discrete distributions.
Such mechanisms are simpler to implement with PRNGs
and less likely to violate differential privacy in practice.
While our audit did not find any DP violations, we highlight
that their configured privacy budgets are large relative to
common practice and can weaken privacy.
8.1. Count Sketch Mechanisms
Apple’s 2017 white paper proposed the Count Me-
dian Sketch (CMS) and Hadamard Count Median Sketch

(HCMS) algorithms [1], which we find directly implemented
within the DP framework. These algorithms operate by
collecting randomized encodings of count data from the
users to estimate the frequencies of a set of known elements,
such as emojis used in QuickType and web domains visited
on Safari. At the server, these encodings are then aggregated
into acount-sketch matrix, which can then be queried to
extract a privacy-preserving approximate count of all the
elements. Algorithm 8 and Algorithm 9 detail the client-
side part of the CMS and HCMS algorithms respectively.
Algorithm 8:M client-CMS [1, Algorithm 2]
Input:Data elementX, parameterε, bit countd,
hash countk
Result:BitsY∈ {0,1} d, hash indexj
1Uniformly samplej∼[k]
2Initialize vectorV← {0} d
3SetV[Hash j(x) modd]←1
4fori∈ {1,· · ·, d}do
5Y[i]←
(
V[i]with probability eε/2 eε/2+1
1−V[i]otherwise
6Return:Y, indexj
The mechanismM client-CMS works by hashing the input
Xinto one ofdpossible buckets using a random hash
functionHash j, implemented asSHA256(j∥x)in the DP
framework, to create a one-hot vectorV. This vector is then
privatized withε-DP by randomly flipping its bits and then
sent to the server along with the hash function indexj.
Algorithm 9:M client-HCMS [1, Algorithm 6]
Input:Data elementX, parameterε, bit countd,
hash countk
Result:BitY∈ {−1,1}, hash indexj, bit indexl
1Uniformly samplej∼[k]
2Initialize vectorV← {0} d
3SetV[Hash(j, x) modd]←1
4TransformU←H d ×V/ /H d is the Hadamard matrix
5Uniformly samplel∼[d]
6SetY←
(
Ul with probability eε eε+1
−Ul otherwise
7Return:Y, indexj, indexl
TheM client-HCMS is similar toM client-CMS, except it
compresses the one-hot vectorVby multiplying it with the
Hadamard matrixH d and then randomly selecting an index
l∈[d]of the transformed vectorUto privatize withε-DP
and send to the server, along with the indiceslandj.
Decoder forM client-CMS andM client-HCMS.We found sev-
eral leaked logs from Apple’s CMS and HCMS mechanisms,
containing keynames like “keyboard.Emoji.en US” or “Pod-
castTopic.en US” that describe the type of recorded data. To
Figure 8. Illustration of our decoder for Apple’s Count Median Sketch
(Mclient-CMS). Our decoder’s functionality is demonstrated by a test case:
the emoji “
 ” is privatized usingM client-CMS with a privacy budget of
ε= 6. We then attempt to identify the original emoji from a predefined
set of 152 most popular emojis. The decoder successfully narrows down
this set to 5 potential emojis, accurately including the true input.
avoid any risk of exposing real user data, we demonstrate
our decoders on outputs that we generated ourselves using
custom executables that callM client-CMS andM client-HCMS
mechanisms within Apple’s DP framework (see Figure 8).
Our decoding approach requires a candidate setGof
plausible values for the private dataX(a set that, in prin-
ciple, could be formulated for any given log based on its
keyname). For a given hash indexjand corrresponding
output vectorY, we consider a guessg∈Gplausible
if hasing it yields an index whose bit inYis set, i.e.,
Y[Hash j(g) modd] = 1. The rationale behind this is that
whenε≥4, there is at least an88.08%probability that the
true bit in the one-hot vectorVremains unflipped in the
privatized outputY. Hence, anyg∈Gthat maps to a set
bit inYis a plausible candidate for the original value ofX.
ForM client-HCMS, we apply a similar decoding process
that accounts for the Hadamard transformation. Specifically,
for an observation(Y, j, l)fromM client-HCMS, we markg∈
Gas plausible if hasing it withHash j yields a transformed
vector whose bit at indexlmatches the observed outputY,
i.e.,OHE(l) ⊤ ×H d ×OHE(Hash j(g) modd) =Y.

Figure 9. Sample record generated by Count Median Sketch that appears
in [1, Figure 3]. Running our decoder on it after padding “...” with0s on
the same list of 152 emojis as in Figure 8 results in a unique match: “
 ”.
Reconstruction Attack.We find that our strategy is quite
effective in decoding the output ofM client-CMS, especially
when provided with a descent set of guessesGfor the
targetX, as illustrated in Figure 8. When we tested
our decoder on outputs generated from our executable—
configured to mimic the leaked logs with the keyname
“keyboard.Emoji.en US” and withε= 6budget—it fre-
quently returned just a single matching emoji. Moreover,
when we ran the decoder on the partial CMS sample from
Apple’s white paper (cf. Figure 9), it returned a unique
match: “
 ”. Given that the paper itself reports “
 ” as the
overwhelmingly most popular emoji in the English locale
(see [1, Figure 5]), this provides strong evidence that our
reconstruction was successful, illustrating the privacy risks.
Privacy Auditing Result.We conducted a DP audit of
Mclient-CMS andM client-HCMS using a membership test
grounded in our decoding strategy. In this setup, the adver-
sary predicts the input asx 1 =“
 ” if the alternative guess
x0 =“
 ” fails to decode to the mechanism’s output. Each
mechanism was executedn= 1000times withε= 4, ran-
domly selecting betweenx 0 andx 1 in each run. From these
experiments, we obtained95%-confidence lower bounds of
εlb = 2.86forM client-CMS andε lb = 3.66forM client-HCMS
(see Algorithm 11), confirming that both adhere to their
stated privacy parameters. However, the membership infer-
ence attacks achieved high success rates—83.80% accuracy
(FPR2.65%, TPR70.73%) forM client-CMS and71.30%ac-
curacy (FPR0.41%, TPR44.01%) forM client-HCMS. These
results show that, even with a correct implementation, a
privacy budget ofε= 4, which Apple used from 2017 to
2022 for collecting sensitive data (see Appendix A.6), was
far too large to provide meaningful privacy protection.
8.2. PI-RAPPOR Mechanism
Another mechanism that we audit is PI-RAPPOR. Intro-
duced in [18, Algorithm 3], this mechanism is configured
with constants0< α 0 < α1 <1, number of classesk,
and a primepsuch thatα 0p∈N, and satisfiesε-DP in
the standard replacement model forε= log α1(1−α0) α0(1−α1). The
output of this mechanism is a pair of coefficients,(ϕ 0, ϕ1),
that is transmitted to the servers. For brevity, we omit the
description of this mechanism, referring the reader to [18,
Section 4.1] for the details of its design.
We observe that the implementation of PI-RAPPOR
closely aligns with its specification in [18, Algorithm 3].
Its constructor takes the same four initialization parameters,
which we set tok= 2,α 0 = 0.000335,α 1 = 0.999665,
andp= 2971, yieldingε-DP withε= 8. These val-
ues correspond exactly to those used in macOS Sonoma
14.2 for collecting analytics data associated with keys like
“systemsettings.SearchTerm”, “networking.IPPrefix”, “key-
board.WordUnigram”, and others.
To decode an output(ϕ 0, ϕ1), we employ the built-in
decode()method provided in the DP framework. Using this
decoder as the membership test for our privacy auditing
(via Algorithm 11), we evaluated PI-RAPPOR on inputs
x0 = 0andx 1 = 1acrossn= 1,000runs, obtaining a
95%-confidence lower bound ofε lb = 5.51. Although our
audit does not indicate any DP violation, we note that the
configured privacy budget ofε= 8is nonetheless far too
large to provide sufficient protection, as our membership
inference attack still achieved a striking98.43%accuracy.
8.3. OneBitHistogram Mechanism
The final mechanism we audit in Apple’s DP framework
is OneBitHistogram, which also seems to be designed for
the frequency estimation task. Although we could not find
any public information from Apple on its design, OneBitHis-
togram seems to be a variant of the Randomized Response
mechanism that resembles [43, Algorithm 1]. Based on our
inspection of the binary, we describe it in Algorithm 10.
Algorithm 10:OneBitHistogram
Input:Data elementX, parameterε, bit countd
Result:BitY∈ {0,1}, bit indexl
1Uniformly sample indexl∼[d]
2Create keyk←SHA256(X)
3EncryptV←AES128(l;k)
4Y←
(
V[l]with probability eε eε+1
1−V[l]otherwise
5Return:BitY, bit indexl
We do not know why Algorithm 10 was designed in its
presented form, nor how Apple’s servers aggregate the data
it produces. Nevertheless, given its output(Y, l), we can
test whether a guessg∈Gfor the true data elementXis
plausible by checking whetherAES128(l;SHA256(g))[l] =
Y. Using this membership test to distinguish between the
guessesG={“
 ”,“
 ”}, we audit the DP of the OneBitHis-
togram mechanism (via Algorithm 11 in Appendix B). With
n= 1,000runs, we obtain a 95%-confidence lower bound
ofε lb = 0.86, when the mechanism was configured to
satisfy1-DP. While we did not detect any violations of
DP, our membership attack achieves an accuracy of72.10%
(FPR28.92%, TPR73.08%), which is strikingly close to
the theoretical bounde ε/(eε + 1)≈73.11%forε= 1.
9. Countermeasures and Discussion
Our audit of Apple’s DifferentialPrivacy.framework re-
veals a significant gap between the company’s public com-

mitment to privacy and the technical reality of its imple-
mentation. The vulnerabilities we uncovered—ranging from
flawed noising mechanisms to insecure multiparty compu-
tation protocols and excessively weak privacy parameters—
undermine the very guarantees that differential privacy is
meant to provide. These findings not only impact user
privacy on potentially billions of devices but also highlight
systemic issues in deploying privacy-enhancing technologies
at scale without sufficient transparency. Here, we propose
concrete countermeasures to address the identified flaws and
discuss the broader implications for Apple and the industry.
9.1. Mitigating Implementation Vulnerabilities
The vulnerabilities detailed in this paper are not theoret-
ical; they are practical flaws with tangible impacts on user
privacy. Fortunately, they are also rectifiable. We propose
the following technical countermeasures.
Secure Noise Generation.The use of floating-point arith-
metic for generating noise from continuous distributions like
Laplace and Gaussian is a well-documented anti-pattern in
DP implementation [23], [32], [34]. We recommend that
Apple deprecates its current noise generation mechanisms
based on inverse transform and the Marsaglia polar methods.
Instead, it should adopt SOTA, secure techniques designed
to be resilient against floating-point attacks. Options include
switching to discrete versions of these distributions (e.g., the
Discrete Laplace or Discrete Gaussian distributions [57])
or employing a secure noise library or other provably safe
methods [50]–[52]. This would directly remediate the flaws
found in NumberRandomizer and Prio++.
Re-Architecting Secure Aggregation Protocols.Our anal-
ysis shows that Apple’s implementation of the Prio [29]-
based secure aggregation protocol has several issues that
weaken the privacy it provides to its users. We provide the
following recommendations to address them:
1)A Public Server.A SecAgg protocol’s security guar-
antee is predicated on the operational independence
of the servers aggregating the secret shares. Sending
both shares to a single endpoint falls outside standard
threat-model assumptions about independently oper-
ated servers. To rectify this, the system should be re-
designed to send shares totwo or more logically and
physically separate servers. Critically, to ensure public
trust, one of these aggregation servers should be a
publicly auditable entity, allowing external parties to
verify that the protocol is being followed correctly.
2)Always use DP.All data transmitted, including meta-
data and performance metrics, should be considered po-
tentially sensitive. Protocols like Prio++Metadata and
Prio++Metrics currently transmit information without
any DP noise, relying only on SecAgg for protection,
which is problematic. All components of an analytics
data should be protected with a formal differential
privacy guarantee, ensuring that no part of the collected
data can be used to compromise user privacy.
3)Cryptographically secure PRNGs.The random num-
bers used to generate the shares must come from
a cryptographically-secure PRNGs. Re-using the vul-
nerable floating-point-based GaussianPRNG for secret
sharing, as is done in Prio++, Prio++Metrics and PINE,
should be avoided.
4)Encrypted Logs.The current practice of exposing
private record payloads in user-exportable diagnostics
is a critical vulnerability, especially once such logs
leave the device. The surrounding metadata can remain
available for debugging, but sensitive payload fields
such as secret shares and encoded measurements should
be encrypted whenever reports are staged for export or
user sharing.
5)Preventing Side-channel Attacks.The very act of
generating a report or uploading analytics data can leak
information, such as how often a user engages with a
particular app. To curb this, the frequency and timing
of report generation must be randomized with a DP
mechanism to obscure the underlying activity patterns.
Tighter Privacy Budgeting.Even a perfectly implemented
DP algorithm can offer negligible privacy if configured with
a large privacy budgetε. Apple should conduct a thorough
review of the privacy budgets assigned to all the collected
properties. Any property with anεvalue high enough to
permit trivial membership inference (e.g.,ε >4) should
be considered effectively non-private. These budgets must
be drastically lowered or their use explicitly justified with
clear, user-facing consent. Additionally, the ambiguity we
observed in the privacy budget for Prio—where the con-
figuredεappears to correspond to a2εloss when doing
membership inference—highlights the need for clear and
consistent definitions of neighbouring relationship in privacy
guarantees across all mechanisms.
9.2. Transparency and Verifiability
While technical fixes are essential, our findings point to
a deeper, more structural problem: the opacity of Apple’s
privacy engineering. Relying on “security through obscu-
rity” is a fragile strategy, especially for primitives like
DP where subtle implementation errors can silently break
privacy guarantees. Our DP audit validates long-held con-
cerns from the privacy community regarding Apple’s closed-
source approach [20], [21]. Slogans like “what happens
on your iPhone, stays on your iPhone” ring hollow if the
mechanisms ensuring this are difficult to verify and, as we
have shown with our privacy audits, riddled with flaws.
The most effective measure to restore trust on its pri-
vacy features istransparency. We recommend that Apple
open-source, or publish a verifiable specification of, the
DifferentialPrivacy.framework library. Doing so would al-
low for public verification from independent researchers and
security experts, fostering a collaborative environment to
identify and fix vulnerabilities before they can be exploited.

10. LLM Usage Considerations
We leveraged LLMs, specifically ChatGPT 4o and Gem-
ini 2.5 Pro models, in understanding complex sections of the
decompiled binary. These LLMs were also used for editorial
purposes in this manuscript, and all outputs were inspected
by the authors to ensure accuracy and originality.
11. Ethics Considerations
All experiments illustrated in this work used only the
author-controlled test devices and synthetic inputs. Through-
out the duration of this study, no third-party user data was
collected, retained, or analyzed.
The objective of our ethical reverse-engineering efforts
was to responsibly disclose any vulnerabilities we identify
to Apple directly. We did so on August 13, 2025, submit-
ting an early draft of this work, accompanying proof-of-
concept exploits, and references to publicly exposed logs
that appeared susceptible to data extraction attacks. Apple
responded promptly the following day, requesting clarifica-
tion on our publication timeline. By August 29, 2025, the
company confirmed in its disclosure correspondence with
us that the reported vulnerabilities were reproducible and
stated that fixes were planned for release in fall 2025.
However, two months later, Apple reclassified the vul-
nerabilities as “expected behaviour” and closed the report on
October 7, 2025. Appendix A summarizes Apple’s official
response that we received at the time of closure of our
vulnerability report, and explains its relation to our results.
Acknowledgments
This research is supported by the Ministry of Education,
Singapore, under an AcRF Tier 2 Grant (MOE-000761-01),
and by a gift grant from Google.
References
[1] Differential Privacy Team, Apple Inc., “Learning with
privacy at scale,”Apple Machine Learning Research, 2017.
[Online]. Available: https://docs-assets.developer.apple.com/ml-
research/papers/learning-with-privacy-at-scale.pdf
[2] A. M. L. Research, “Scenes: Differential privacy,” https:
//machinelearning.apple.com/research/scenes-differential-privacy,
2024, accessed: 2024-10-07.
[3] B. Zhang, V . Doroshenko, P. Kairouz, T. Steinke, A. Thakurta, Z. Ma,
E. Cohen, H. Apte, and J. Spacek, “Differentially private stream
processing at scale,”arXiv preprint arXiv:2303.18086, 2023.
[4] K. Jin and L. McGorman, “Data for good: New tools to help health
researchers track and combat covid-19,” 2020. [Online]. Available:
https://about.fb.com/news/2020/04/data-for-good/
[5] B. Ding, J. Kulkarni, and S. Yekhanin, “Collecting telemetry data pri-
vately,”Advances in Neural Information Processing Systems, vol. 30,
2017.
[6] J. M. Abowd, “The US Census Bureau adopts differential privacy,”
inProceedings of the 24th ACM SIGKDD international conference
on knowledge discovery & data mining, 2018, pp. 2867–2867.
[7] WWDC 2016b, “WWDC 2016 Keynote,” June 2016. [Online].
Available: https://youtu.be/n5jXg NNiCA?t=6112
[8] A. Bhowmick, A. H. Vyrros, and U. S. Vaishampayan, “Differential
privacy using a count mean sketch,” Dec. 6 2018, US Patent App.
15/805,591.
[9] A. Bhowmick, A. H. Vyrros, and R. M. Rogers, “Privatized machine
learning using generative adversarial networks,” Aug. 8 2019, US
Patent App. 15/892,246.
[10] A. Bhowmick, J. Duchi, J. Freudiger, G. Kapoor, and R. M. Rogers,
“Private federated learning with protection against reconstruction,”
May 21 2024, US Patent 11,989,634.
[11] A. Bhowmick, R. M. Rogers, U. S. Vaishampayan, and A. H. Vyrros,
“Distributed labeling for supervised learning,” Jul. 25 2023, US Patent
11,710,035.
[12] A. G. Thakurta, A. H. Vyrros, U. S. Vaishampayan, G. Kapoor,
J. Freudinger, V . V . Prakash, A. Legendre, and S. Duplinsky, “Emoji
frequency detection and deep link frequency,” Jul. 11 2017, US Patent
9,705,908.
[13] A. G. Thakurta, A. H. Vyrros, U. S. Vaishampayan, G. Kapoor,
J. Freudiger, V . R. Sridhar, and D. Davidson, “Learning new words,”
Mar. 14 2017, US Patent 9,594,741.
[14] E. D. Friedman, R. K. Kumar, and L. Winstrom, “Differential pri-
vacy for message text content mining,” Sep. 15 2020, US Patent
10,778,633.
[15] Y . L. Sierra, A. G. Thakurta, U. S. Vaishampayan, J. C. Hurley, K. F.
Mowery, and M. Brouwer, “Efficient implementation for differential
privacy using cryptographic functions,” Mar. 12 2019, US Patent
10,229,282.
[16] “Understanding aggregate trends for apple intelligence using
differential privacy,” 2025, accessed: 2025-04-22. [Online]. Avail-
able: https://machinelearning.apple.com/research/differential-privacy-
aggregate-trends
[17] K. Chadha, J. Chen, J. Duchi, V . Feldman, H. Hashemi, O. Javidbakht,
A. McMillan, and K. Talwar, “Differentially private heavy hitter
detection using federated analytics,” in2024 IEEE Conference on
Secure and Trustworthy Machine Learning (SaTML). IEEE, 2024,
pp. 512–533.
[18] V . Feldman and K. Talwar, “Lossless compression of efficient private
local randomizers,” inInternational Conference on Machine Learn-
ing. PMLR, 2021, pp. 3208–3219.
[19] V . Feldman, J. Nelson, H. Nguyen, and K. Talwar, “Private frequency
estimation via projective geometry,” inInternational Conference on
Machine Learning. PMLR, 2022, pp. 6418–6433.
[20] B. Cyphers, “Differential privacy, part 3: Extraordinary claims
require extraordinary scrutiny,”Access Now, November 2017.
[Online]. Available: https://www.accessnow.org/differential-privacy-
part-3-extraordinary-claims-require-extraordinary-scrutiny/
[21] A. H. N. Forum, “Apple’s emphasis on differential privacy,” 2016,
accessed: 2024-11-27. [Online]. Available: https://news.ycombinator.
com/item?id=11903127
[22] S. Casacuberta, M. Shoemate, S. Vadhan, and C. Wagaman,
“Widespread underestimation of sensitivity in differentially private
libraries and how to fix it,” inProceedings of the 2022 ACM SIGSAC
Conference on Computer and Communications Security, 2022, pp.
471–484.
[23] I. Mironov, “On significance of the least significant bits for differential
privacy,” inProceedings of the 2012 ACM conference on Computer
and communications security, 2012, pp. 650–661.
[24] C. J. Lebeda, M. Regehr, G. Kamath, and T. Steinke, “Avoiding
pitfalls for privacy accounting of subsampled mechanisms under
composition,”arXiv preprint arXiv:2405.20769, 2024.
[25] F. Tramer, A. Terzis, T. Steinke, S. Song, M. Jagielski, and N. Carlini,
“Debugging differential privacy: A case study for privacy auditing,”
arXiv preprint arXiv:2202.12219, 2022.

[26] M. Lyu, D. Su, and N. Li, “Understanding the sparse vector tech-
nique for differential privacy,”Proceedings of the VLDB Endowment,
vol. 10, no. 6, pp. 637–648, 2017.
[27] Z. Ding, Y . Wang, G. Wang, D. Zhang, and D. Kifer, “Detecting
violations of differential privacy,” inProceedings of the 2018 ACM
SIGSAC Conference on Computer and Communications Security,
2018, pp. 475–489.
[28] S. Zanella-Beguelin, L. Wutschitz, S. Tople, A. Salem, V . R ¨uhle,
A. Paverd, M. Naseri, B. K ¨opf, and D. Jones, “Bayesian estima-
tion of differential privacy,” inInternational Conference on Machine
Learning. PMLR, 2023, pp. 40 624–40 636.
[29] H. Corrigan-Gibbs and D. Boneh, “Prio: Private, robust, and scalable
computation of aggregate statistics,” in14th USENIX symposium on
networked systems design and implementation (NSDI 17), 2017, pp.
259–282.
[30] G. N. Rothblum, E. Omri, J. Chen, and K. Talwar, “{PINE}: Efficient
verification of a euclidean norm bound of a{Secret-Shared}vector,”
in33rd USENIX Security Symposium (USENIX Security 24), 2024,
pp. 6975–6992.
[31] P. Kairouz, S. Oh, and P. Viswanath, “The composition theorem for
differential privacy,” inInternational conference on machine learning.
PMLR, 2015, pp. 1376–1385.
[32] J. Jin, E. McMurtry, B. I. Rubinstein, and O. Ohrimenko, “Are we
there yet? Timing and floating-point attacks on differential privacy
systems,” in2022 IEEE Symposium on security and privacy (SP).
IEEE, 2022, pp. 473–488.
[33] S. Haney, D. Desfontaines, L. Hartman, R. Shrestha, and M. Hay,
“Precision-based attacks and interval refining: How to break,
then fix, differential privacy on finite computers,”arXiv preprint
arXiv:2207.13793, 2022.
[34] J. Lokna, A. Paradis, D. I. Dimitrov, and M. Vechev, “Group and
Attack: Auditing differential privacy,” inProceedings of the 2023
ACM SIGSAC Conference on Computer and Communications Secu-
rity, 2023, pp. 1905–1918.
[35] A. C. Gilbert and A. McMillan, “Property testing for differential pri-
vacy,” in2018 56th Annual Allerton Conference on Communication,
Control, and Computing (Allerton). IEEE, 2018, pp. 249–258.
[36] B. Bichsel, S. Steffen, I. Bogunovic, and M. Vechev, “DP-Sniper:
Black-box discovery of differential privacy violations using classi-
fiers,” in2021 IEEE Symposium on Security and Privacy (SP). IEEE,
2021, pp. 391–409.
[37] T. Steinke, M. Nasr, and M. Jagielski, “Privacy auditing with one (1)
training run,”Advances in Neural Information Processing Systems,
vol. 36, 2024.
[38] S. Mahloujifar, L. Melis, and K. Chaudhuri, “Auditingf-differential
privacy in one run,”arXiv preprint arXiv:2410.22235, 2024.
[39] M. Nasr, J. Hayes, T. Steinke, B. Balle, F. Tram `er, M. Jagielski,
N. Carlini, and A. Terzis, “Tight auditing of differentially private
machine learning,” in32nd USENIX Security Symposium (USENIX
Security 23), 2023, pp. 1631–1648.
[40] A. Gadotti, F. Houssiau, M. S. M. S. Annamalai, and Y .-A. de Mon-
tjoye, “Pool inference attacks on local differential privacy: Quantify-
ing the privacy guarantees of apple’s count mean sketch in practice,”
in31st USENIX Security Symposium (USENIX Security 22), 2022,
pp. 501–518.
[41] J. Tang, A. Korolova, X. Bai, X. Wang, and X. Wang, “Privacy loss
in Apple’s implementation of differential privacy on macOS 10.12,”
arXiv preprint arXiv:1709.02753, 2017.
[42] C. Dwork, A. Rothet al., “The algorithmic foundations of differential
privacy,”Foundations and trends® in theoretical computer science,
vol. 9, no. 3–4, pp. 211–407, 2014.
[43] R. Bassily and A. Smith, “Local, private, efficient protocols for
succinct histograms,” inProceedings of the forty-seventh annual ACM
symposium on Theory of computing, 2015, pp. 127–135.
[44] C. Dwork, “Differential privacy,” inInternational colloquium on
automata, languages, and programming. Springer, 2006, pp. 1–12.
[45] A. McMillan, O. Javidbakht, K. Talwar, E. Briggs, M. Chatzidakis,
J. Chen, J. Duchi, V . Feldman, Y . Goren, M. Hesseet al., “Pri-
vate federated statistics in an interactive setting,”arXiv preprint
arXiv:2211.10082, 2022.
[46] Y . Chen and A. Machanavajjhala, “On the privacy properties
of variants on the Sparse Vector Technique,”arXiv preprint
arXiv:1508.07306, 2015.
[47] R. Barnes, D. Cook, C. Patton, and P. Schoppmann, “Verifiable
Distributed Aggregation Functions,” Internet Engineering Task
Force, Internet-Draft draft-irtf-cfrg-vdaf-17, Oct. 2025, work in
Progress. [Online]. Available: https://datatracker.ietf.org/doc/draft-
irtf-cfrg-vdaf/17/
[48] T. Geoghegan, C. Patton, B. Pitman, E. Rescorla, and C. A.
Wood, “Distributed Aggregation Protocol for Privacy Preserving
Measurement,” Internet Engineering Task Force, Internet-Draft draft-
ietf-ppm-dap-16, Sep. 2025, work in Progress. [Online]. Available:
https://datatracker.ietf.org/doc/draft-ietf-ppm-dap/16/
[49] “Anonymous artifact for auditing apple’s differentialpri-
vacy.framework,” https://anonymous.4open.science/r/ios17-dyld-
headers-DifferentialPrivacy-E187/, 2025, anonymous research
artifact containing recovered headers and supporting code.
[50] G. D. P. Team, “Secure noise generation,” June 2020.
[Online]. Available: https://github.com/google/differential-privacy/
blob/main/common docs/Secure Noise Generation.pdf
[51] N. Holohan, S. Braghin, and M. Suliman, “Securing floating-point
arithmetic for noise addition,” inProceedings of the 2024 on ACM
SIGSAC Conference on Computer and Communications Security,
2024, pp. 1954–1966.
[52] H. Keller, H. M ¨ollering, T. Schneider, O. Tkachenko, and L. Zhao,
“Secure noise sampling for DP in MPC with finite precision,” in
Proceedings of the 19th International Conference on Availability,
Reliability and Security, 2024, pp. 1–12.
[53] C. Dwork, F. McSherry, K. Nissim, and A. Smith, “Calibrating noise
to sensitivity in private data analysis,” inTheory of cryptography
conference. Springer, 2006, pp. 265–284.
[54] J. E. Gentle,Random number generation and Monte Carlo methods.
Springer, 2003.
[55] S. Wang and C. Patton, “Task Binding and In-Band Provisioning for
DAP,” Internet Engineering Task Force, Internet-Draft draft-ietf-ppm-
dap-taskprov-03, Sep. 2025, work in Progress. [Online]. Available:
https://datatracker.ietf.org/doc/draft-ietf-ppm-dap-taskprov/03/
[56] K. Talwar, “Differential secrecy for distributed data and applications
to robust differentially secure vector summation,”arXiv preprint
arXiv:2202.10618, 2022.
[57] C. L. Canonne, G. Kamath, and T. Steinke, “The discrete gaussian
for differential privacy,”Advances in Neural Information Processing
Systems, vol. 33, pp. 15 676–15 688, 2020.
[58] C. Dwork, N. Kohli, and D. Mulligan, “Differential privacy in prac-
tice: Expose your epsilons!”Journal of Privacy and Confidentiality,
vol. 9, no. 2, 2019.
[59] L. Wasserman and S. Zhou, “A statistical framework for differential
privacy,”Journal of the American Statistical Association, vol. 105,
no. 489, pp. 375–389, 2010.
[60] J. Dong, A. Roth, and W. J. Su, “Gaussian differential privacy,”arXiv
preprint arXiv:1905.02383, 2019.
Appendix A.
Apple’s Response and Relation to Our Results
This appendix summarizes Apple’s response to our dis-
closure and explains how they relate to the results that we

report. We note that all results in the paper concern the
client-side, pre-aggregationbehavior of the mechanisms as
shipped in macOS Sonoma 14.2 and Sequoia 15.6. We did
not instrument or evaluate Apple’s server-side systems.
A.1. Deployment Status and Versions
Apple states that several mechanisms that we exam-
ined (e.g., the Laplace sampler in NumberRandomizer,
GaussianPRNG-based Prio++ paths, and CMS/HCMS vari-
ants) have beendeprecatedand that newer deployments use
PINE that implements open protocol designs likeVerifi-
able Distributed Aggregation Functions(VDAF) [47] and
Distribution Aggregation Protocol(DAP) [48]. Our results
therefore pertain to the client code and configurations as
shipped in macOS Sonoma 14.2 and Sequoia 15.6, in which
many of the now-deprecated mechanisms were still in active
use.
A.2. Floating-Point Sampling and PINE
Apple states that PINE converts outputs to integers
before secret sharing. Our audits and reconstruction tests
target the Laplace and Gaussian pathways that we executed
via dynamic loading; we report violations for NumberRan-
domizer and for the Gaussian pathway used by Prio++.
Although we found that PINE’s addNoiseToData() method
also uses the vulnerable GaussianPRNG, we did not evaluate
its randomizeFloatVector() method and therefore do not
make claims about its privacy or confidentiality guarantees.
A.3. Leader/Helper Separation
Apple states that the leader forwards one share to a
distinct helper holding a different key. From the client side,
we observe uploads of two ciphertexts to a leader endpoint;
we cannot externally attest to operational non-collusion
or infrastructure separation – this is a trust assumption
not auditable from the client vantage. Our findings about
pre-aggregationrisk are unaffected.
A.4. Configurations Collected Without Local DP
Apple confirms that certain variants (e.g., PINEMeta-
data and PINEMetrics) are collectedwithoutlocal DP and
rely on secure aggregation. Our results likewise found
local-DP-off configurations (previously Prio++Metadata and
Prio++Metrics) and showed perfect membership inference
pre-aggregation under those settings. We describe these
precisely as “configured with local DP disabled” and retain
the analysis of risk to any party that obtains client-side logs.
A.5. Plaintext Logs and Reconstruction Risks
Apple notes that on-device analytics logs are plaintext
and argues access requires an unlocked device; logs in transit
are encrypted. Our result targets a different, post-export
threat model: we do not claim that arbitrary third-party
apps can read these files directly on-device under Apple’s
sandbox. Rather, any party (not necessarily Apple) that ob-
tains pre-aggregation logs (e.g., via user export, diagnostics
sharing, or online leaks) can reconstruct measurements from
‘share1’, ‘share2’, and recorded parameters. This doesnot
imply that Apple’s servers see decrypted per-user data; it
shows pre-aggregation exposure to parties with log access.
A.6. Count–Sketch Mechanisms
Apple reports that Count-sketching mechanisms have
been deprecated and have not used for data collections since
2022. Matching this, we did find CMS/HCMS mechanisms
missing in the DP framework shipped on macOS Sequoia
15.6 (but were present in Sonoma 14.2). We keep our results
for these mechanisms ashistoricalto illustrate how largeε
materially weakens privacy, because other deployers may
still use these designs. Our decoders and audits demonstrate
the methodology without relying on third-party logs.
A.7. Adjacency Models and Shuffling
Apple emphasizes privacy amplification by shuffling,
justifying the use of large Local DP budgets. Our audits
estimatelocal, pre-shuffleprivacy (the view observable at
the client and in the logs). Shuffling can strengthen central
DP at the aggregate, but it does not mitigatelog-leakrisk
because an attacker holding pre-aggregation logs sees the
local outputs before shuffling.
Apple also emphasizes deletion adjacency model as
being widely trusted and used in the industry. Our analysis
highlights the inconsistency in how adjacency is applied:
whereas the other mechanisms we audited interpret their
‘PrivacyParameter’ in the configuration under replacement
adjacency, Prio interprets it under deletion adjacency.
A.8. Zero-Knowledge Proofs
Apple states that PINE’s zero-knowledge proofs are
unaffected. We make no claim about PINE’s ZK proofs.
Our DZK-related finding pertains to Prio++, where the same
floating-point issue that affects the Gaussian mechanism also
impacts the SecretShares generator and thereby the indistin-
guishability requirement used in its DZK verification.
Appendix B.
Our DP Auditing Framework
We consider a mechanismM:X →Prob(Y)that takes
as input a record from the data universeXand produces a
random outcome in the output spaceY.
Definition B.1(Differential Privacy [58]).An mechanism
Mis(ε, δ)-differentially private((ε, δ)-DP) if for allx, x′ ∈
X, with the output distributionsM(x),M(x ′)denoted as
P, Qrespectively, the following condition holds:
∀S⊂ Y:P(S)≤e ε ·Q(S) +δ.(3)

A practical interpretation of DP guarantees is to see them
as constraints on ahypothesis test—lety∈ Ybe an output
obtained by running the mechanismMon eitherxor its
neighbourx ′, then any membership testϕ:Y → {0,1}to
distinguish between thenullandalternatehypothesis:
H0 :ycame fromM(x), H 1 :ycame fromM(x ′),
cannot simultaneously have a lowfalse alarm rateα ϕ (i.e.,
Type-I error or False Positive Rate or FPR) and a lowmissed
detection rateβ ϕ (i.e. Type-II error or False Negative Rate
or FNR) [31], [59]. More precisely,(ε, δ)-DP implies that
for all testsϕ, the inequality1−β ϕ ≤e εαϕ +δholds. The
work in [60] formalize this hypothesis testing interpretation
as the following differential privacy definition.
Definition B.2(f-differential privacy [60]).A mechanism
Misf-differentially private(f-DP) if for allx, x ′ ∈ X,
with the output distributionsM(x),M(x ′)denoted asP, Q
respectively, the following condition holds:
∀α∈[0,1] :T P∥Q (α)≥f(α),(4)
whereT P∥Q is thetrade-off functiondefined as
TP∥Q (α) := inf ϕ:Y→{0,1} {βϕ :α ϕ ≤α},(5)
withα ϕ :=E P [ϕ], andβ ϕ := 1−E Q [ϕ].
We say that a trade-off curvef 1 is dominated byf 2
(denotedf 1 ≼f 2), if:
∀α∈[0,1] :f 1(α)≥f 2(α).(6)
An(ε, δ)-DP guarantee can be equivalently stated in
terms of thef-DP guarantee.
Proposition B.1((ε, δ)-DP tof-DP [60]).A mechanism is
(ε, δ)-DP if and only if it isf ε,δ-DP , where
fε,δ(α) := max{0,1−δ−e εα, e−ε(1−δ−α)}.(7)
And, anf-DP guarantee and the curve comprising of all
(ε, δ)-DP guarantees are linked viaconvex-conjugatation.
Proposition B.2(f-DP to(ε, δ)-DP [60]).A mechanism is
f-DP if and only if it is(ε, δ f (ε))-DP for allε≥0, where
δf (ε) := sup
α∈[0,1]
1−α·e ε −f(α).(8)
More importantly, dominance in trade-off functionsf
directly translates to dominance in theirδ f (ε)curves.
Proposition B.3( [60, Lemma B.2]).If trade-off functions
f1, f2 satisfyf 1 ≼f 2, thenδ f (ε)≤δ f (ε)for allε≥0.
A DP guarantee is an upper bounds that is established
in theory, typically by means of a pen-and-paper proof.
However, these guarantees can fail in practiceif the analysis
is incorrect or there are bugs in the implementation. Unfor-
tunately, such mistakes are not uncommon and many papers
are written to exclusively point out these mistakes [22]–
[24], [26], [46]. Privacy auditing techniques provide an
empirically lower boundon the DP parameters by testing
the implementation, which can help in detecting bugs or an-
alytical errors when the lower and upper bounds contradict
each other, or help assess the tightness of the upper-bounds
otherwise [27], [28], [34], [36]–[38].
In the following definition, we introduce the workflow
for auditing DP adopted in this paper. Our framing here is
derived from a compilation of existing auditing techniques,
taking inspiration from [27], [36], [36], [37], and formalizes
the high-level principle for estimating an empirical lower
bound on the privacy description of a mechanism.
Definition B.3(f-DP Auditor).Anf-DP auditor(A,R f )
is a hypothesis test to determine whether the null-hypothesis
“mechanismMisf-DP” holds or not. It eitherREJECTs
the null-hypothesis with a p-value at mostγorFAILS TO
REJECTit, as follows:
1) Auditor executesMin a controlled environment to
collect certain statisticsA(M)∈Ω.
2) Auditor thenREJECTSifA(M)lies in the rejection
setR f (γ)⊂Ωof extreme values that rarely occur
(probability less thanγ) underf-DP . Otherwise, the
auditorFAILS TO REJECT.
Formally, anf-DP auditor(A,R f )is such that for all
mechanismsM:X → Yand significance levelsγ∈[0,1],
Misf-DP=⇒P[A(M)∈ R f (γ)]≤γ.(9)
In other words, anf-DP auditor(A,R f )has only
a small probability (≤γ) of incorrectly flagging anf-
DP mechanismMas violatingf-DP. Crutially, this false-
rejection probabilityγcan be controlled by adjusting the
size of the rejection setR f (γ). Moreover, since(ε, δ)-DP is
equivalent tof ε,δ-DP (cf. Proposition B.1), anf-DP auditor
can also be used to audit(ε, δ)-DP guarantees.
Definition B.3 provides a unifying perspective on the
DP auditing techniques in the literature, which differ only
in the attack statistic they evaluate (A(M)) and in how they
construct the corresponding rejection region (R f (γ)).
Steinke et al. [37] show that a DP auditor can be
leveraged to compute a high-confidence lower bound on the
true DP characteristic of a mechanismM. The following
proposition restates the statement in [37, Lemma 4.7] but
molded forf-DP auditing instead of(ε, δ)-DP auditing.
Proposition B.4( [37, Lemma 4.7]).For each mechanism
M, letf M ∈ Fbe the truef-DP guarantee it satisfies
within a trade-off function familyF. Let(A,R)be anf-
DP auditor for allf∈ F. Further suppose that iff 1 ≼f 2
withinF, then the rejection setR f1 (γ)⊃ Rf2 (γ). Then,
for allMand allγ >0,
P

fM ≽f lb ≥1−γ,(10)
where the trade-off curvef lb is defined as
f lb := sup{f∈ F:A(M)∈ Rf (γ)}.(11)
The idea expressed in Proposition B.4 turns a hypothesis
test forf-DP, for which we can control the p-valueγby
adjusting the size of rejection setR f (γ)(see Eqn. (9)), into

anf-DP lower bound estimatorthat searches a classFfor a
maximal trade-off curvef lb that has at least1−γprobability
of being rejected by the auditor. In other words, the trade-
off curvef lb serves as a high-probability lower bound on
the unknownf M-DP guarantee thatMtruly satisfies.
The choice of the trade-off familyFdetermines the
shape of the lower boundf lb that we get on auditing. If
we do not know anything about the mechanismM, it is
reasonable to use the familyF ε :={f ε,δ :ε≥0}or
Fδ :={f ε,δ :δ∈[0,1]}denoting the trade-off curves
corresponding to(ε, δ)-DP for fixedεor fixedδrespectively.
However, Nasr et al. [39] points out that typical trade-off
curves of many mechanisms are considerably distinct from
theF ε orF δ family, which causes lower bound estimates
from these families to underestimate the truef-DP guaran-
tee of such mechanisms. If we know what mechanism we
are auditing, e.g. Gaussian or Laplace mechanisms, we can
restrict the audit to the respective family of trade-off curves,
such as Gaussian familyF Gauss or Laplace familyF Lap, to
get the tighter lower-bound estimatef lb on the truef-DP
guaranteef M ∈ FthatMsatisfies.
Remark B.5.The Gaussian and Laplace family of trade-off
curves are defined respectively as
FGauss :={T N(0,1)∥N(µ,1) |µ≥0},(12)
FLap :={T Lap(0,1)∥Lap(µ,1) |µ≥0}.(13)
The duality between trade-off curvesf(α)curve and
δf (ε)-curve in Proposition B.2 and the dominance relation-
ship in Proposition B.3 converts anf-DP lower bound into
an(ε, δ)-DP lower bound.
fM ≽f lb =⇒ ∀ε≥0 :δ fM (ε)≥δ f lb (ε).(14)
Essentially, if we have a lower bound curvef lb for the
realf-DP guarantee of a mechanismM, it means we can
confidently say thatMisnot(ε, δ f lb (ε))-DP for anyε≥0.
Alternatively, we can say thatMisnot(ε f lb (δ), δ)-DP for
anyδ∈[0,1], whereε f lb (δ)is theright inverse functionof
δf lb (ε), defined as
εf lb (δ) := inf{ε≥0 :δ f lb (ε)≤δ}.(15)
Bayesian DP Auditor.For auditing a mechanismM:X →
Y, we design amembership inference attackϕ:Y → {0,1}
to infer whetherMwas ran on an inputx 0 orx 1 and
empirically estimate its FPRαandβ. This is done by
runningMmultiple times on a random choice ofx 0 orx 1
and using the attackϕto predict the choice made for each
run, which gives us a confusion matrix(TN,FP,FN,TP).
Zanella-B´eguelin et al. [28] note that if the real false positive
rate isα, then the number of false positives (FP) observed
across allN := FP + TNtrials (where the true input was
x0) follows a binomial distribution:
FP|α,N∼Binomial(N, α).(16)
Similarly, if the real false negative rate isβ, then the number
of false negatives (FN) observed across allP := FN + TP
trials (where the true input wasx 1) follows:
FN|β,P∼Binomial(P, β).(17)
Therefore, by assuming the realα, βto be distributed ac-
cording to the Beta distributionα, β∼Beta( 1/2,1/2), which
is thenon-informative conjugate priorfor the Binomial
distributions above, the Bayes rule allows them to model
the posterior distribution of(α, β)given the attack statistics
(TP,FP,FN,TN)as follows:
α|FP,TN∼Beta( 1/2+ FP, 1/2+ TN),(18)
β|FN,TP∼Beta( 1/2+ FN, 1/2+ TP).(19)
By definition, ifMisf-DP then all membership attacks
must have FPRαand FNRβthat satisfyf(α)≤β≤
1−f(1−α). Consequently, the probabilityp(f)thatM
satisfiesf-DP for a candidate trade-off curvefon observing
the attack statisticsA(M) := (TP,FP,FN,TN)is
p(f) =P
α|FP,TN
β|FN,TP
[f(α)≤β≤1−f(1−α)].(20)
So if we define our rejection set as
Rf (γ) :={(TP,FP,FN,TN) :p(f)≤γ},(21)
then for all significance levelγ∈[0,1],
Misf-DP=⇒P[M(A)∈ R f (γ)]≤γ.(22)
In other words, the(A,R f )defined above describes anf-
DP auditor. Algorithm 11 describes this auditing approach.
Algorithm 11:(ε, δ)-DP Estimator [28]
Input:MechanismM, trade-off familyF,
significance thresholdγ, target deltaδ,
number of mechanism runsn
Result:ε lb s.t.P  Mis not(ε lb, δ)-DP  ≥1−γ
1initializex 0, x1 ∈ Xand membership testϕ
2uniformly sampleS← $ {0,1} n
3foriin1,· · ·, ndo
4Y i ← M(xSi )// run mechanism
5T i ←ϕ(Y i)// run membership test
/* compute statsA(M) := (TN,FP,FN,TP) */
6A(M)←ConfusionMatrix(S, T)
/* formulate rejection setR f (γ) */
7R f (γ) :={(TP,FP,FN,TN) :p(f)≤γ}
/* findf lb to REJECT withγsignificance */
8f lb ←sup{f∈ F:A(M)∈ R f (γ)}
/* find correspondingε lb forδto REJECT */
9δ f lb (ε) := supα∈[0,1] 1−α·e ε −f lb(α)
10ε lb ←inf{ε≥0 :δ f lb (ε)≤δ}
11Return:ε lb
