---
title: Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem
url: https://arxiv.org/abs/2608.05474
category: privacy-data
subcategory: framework
date: 2026-08
venue: arXiv (Cornell University)
authors:
- Jyotirmay Chauhan
- Kostas Solomos
- Mir Masood Ali
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.05474
pages: 19
chars: 118474
fetched_at: '2026-11-08T13:00:22+00:00'
kb_version: 1
---

# Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem

Exploring Privacy Leakage and Data Disclosure Violations in the
MacOS Application Ecosystem
Jyotirmay Chauhan
University of Illinois Chicago
Chicago, Illinois, USA
jchauh3@uic.edu
Kostas Solomos
Brandeis University
Waltham, Massachusetts, USA
solomos@brandeis.edu
Mir Masood Ali
University of Illinois Chicago
Chicago, Illinois, USA
mali92@uic.edu
Jason Polakis
University of Illinois Chicago
Chicago, Illinois, USA
polakis@uic.edu
Abstract
The systematic and excessive data collection practices of tech com-
panieshaverenderedonlineprivacybothanecessityandasought-
after commodity. However, while the privacy risks of the web, mo-
bile, and IoT ecosystems have been extensively examined, desk-
top environments have been largely overlooked. As desktop apps
continue to be widely used, they remain a critical yet understud-
ied dimension of user privacy. In this paper, we address this gap
by presenting the first, to our knowledge, comprehensive study
of the mechanisms designed to regulate and disclose data collec-
tion and sharing practices in the macOS ecosystem. We adopt an
app-development-centric view, and shed light on the interactions
between the various macOS mechanisms that mediate apps’ data
access. Driven by our findings, we develop NutriScan, an analy-
sis framework that incorporates both static and dynamic analysis
techniquestocreateaconsolidatedviewofmacOSapps’dataprac-
ticesanddisclosures.Weuseoursystemtodynamicallyanalyze1K
macOS apps, and find that 85% of them access user-data APIs with-
out disclosing it. 49.7% also exfiltrate data to advertising entities
and hosting providers, 12.5% of which do so without a correspond-
ing disclosure. We find that desktop apps are being leveraged by
onlinetrackerstoenrichuserprofilesanddevicefingerprints,thus
sheddingnewlightonthetruescopeoftheonlinetrackingecosys-
tem. Our analysis reveals how the macOS app ecosystem is com-
prised of disjoint mechanisms with divergent data abstractions,
thus increasing complexity for developers while also facilitating
undisclosed privacy-invasive practices. Accordingly, we propose a
seriesofmitigationsthataimtobothstreamlinethedatadisclosure
process for developers and improve Apple’s app vetting process.
ACM Reference Format:
Jyotirmay Chauhan, Kostas Solomos, Mir Masood Ali, and Jason Polakis.
2026. Exploring Privacy Leakage and Data Disclosure Violations in the
MacOS Application Ecosystem. In Proceedings of the 2026 ACM SIGSAC
Conference on Computer and Communications Security (CCS ’26), November
15–19, 2026, The Hague, Netherlands. ACM, New York, NY, USA,19 pages.
https://doi.org/10.1145/3830454.3832715
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense.
CCS ’26, The Hague, Netherlands
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2871-6/2026/11
https://doi.org/10.1145/3830454.3832715
1 Introduction
The proliferation of smartphones and Internet-connected devices
has resulted in users constantly interacting with devices that gen-
erate,store,andtransferaplethoraofprivatedata.Thisabundance
of data has given rise to surveillance capitalism [105], a complex
ecosystem powered by pervasive collection and opaque sharing
practices, where user data is brokered among corporations [37,
38]. The collected data enables the inference of sensitive andpro-
tected [57] user characteristics and behaviors [45, 88], highly effec-
tive advertising [59, 99] and misinformation campaigns [53].
Usershavesincegrownincreasinglyconcernedaboutprivacy[ 50,
95], calling for better technical and legislative measures [83]. Con-
sequently, there have been concerted efforts by browser and op-
erating system (OS) vendors for the deployment of more effective
anti-tracking and access control mechanisms, respectively [35, 65,
80].Atthesametime,OSvendorshavefocusedondeployingmech-
anisms that enable the disclosure of data practices in a more user-
friendly manner, as opposed to the confusinglegalese found in pri-
vacy policies. More specifically, Apple’s Privacy Nutrition Labels
and Google’s Data Safety Sections provide the means for app de-
velopers to inform users about the data they collect, whether they
share it with other parties, and how it is used [23, 64].
While the web, mobile, and IoT ecosystems have been exten-
sivelystudiedinregardtopotentialprivacyleakageandviolations[ 5,
7, 10, 36, 52, 66, 71, 77, 79, 84, 85, 92, 94, 98, 101], the desktop
ecosystem has been largely overlooked even though 61.5% of on-
line adults accessed the internet via desktop devices in Q3 2024,
including 72.7% in the United States [1]. This oversight could be
attributed to desktop apps not usually displaying ads and hence
not typically being associated with privacy leakage. Nonetheless,
it is currently unclear what role desktop apps play in the tracking
and advertising landscape. Desktops fundamentally allow broader
default access to user data, and macOS introduces a unique secu-
rity and permission architecture that differs from iOS. These dif-
ferences collectively motivate our study. Specifically, this includes
(i) understanding what access control and disclosure mechanisms
exist in a modern desktop OS, (ii) investigating whether desktop
apps employ tracking and fingerprinting techniques, and (iii) veri-
fying apps’ data practice disclosures.
In this paper, we fill this gap by presenting the first, to the best
of our knowledge, exploration of privacy leakage in desktop ap-
plications. We focus specifically on the macOS ecosystem, due to
arXiv:2608.05474v1  [cs.CR]  5 Aug 2026

CCS ’26, November 15–19, 2026, The Hague, Netherlands Jyotirmay Chauhan, Kostas Solomos, Mir Masood Ali, and Jason Polakis
usersperceivingitasamoreprivateoperatingsystemcomparedto
Windows [91], the presence of multiple OS-level security and pri-
vacy mechanisms [3], and Apple’s recent mandatory requirement
forappstoreleasePrivacyNutritionLabels[ 25].Tothatend,wede-
velop NutriScan, a novel framework that leverages both static and
dynamic analysis techniques to consolidate information across all
relevant application components. This includes analyzing bundle
components that define installation and run-time permissions for
data access and protected system resources, and dynamically in-
strumenting native APIs to identify what data and capabilities are
made available to the application. We also augment our analysis
with network traffic to identify what protected data is transferred
off the device. Finally, our system generates Nutrition Labels that
accurately capture app behavior, and flags inconsistencies in offi-
cial Nutrition Labels.
Overall, our experiments reveal a troubling pattern of overly
intrusive data collection practices alongside incomplete and incor-
rectdatadisclosures.Ourdatasuggeststhatprivacyscreeningpro-
cedures currently in place (if any) are insufficient, as developers
often fail to disclose what data is being collected and shared by
both first-party and third-party components, as reflected by the
inconsistencies captured by NutriScan. Specifically, we find that
only ∼ 15% of the tested apps correctly disclosed all data labels
associated with the sensitive data they accessed. Crucially, devel-
opers did not account for the data collected by embedded third-
party code in over 80% of the apps with manifest files. More im-
portantly, we found sensitive user data, and immutable user and
device identifiers being shared with advertising networks, includ-
ing Google and Facebook. As such, despite Apple’s recent market-
ing efforts showcasing privacy as a major selling point, we find
that even within their heavily guarded desktop environment, data
protection and disclosure mechanisms are currently insufficient,
necessitating a redesign of their mechanisms and a more stringent
vetting process.
In summary, our major research contributions are:
• We explore the mechanisms that govern data collection and
disclosure practices in the macOS ecosystem.
• WedevelopNutriScan,anoveldynamicanalysisframework
that comprehensively evaluates macOS applications for in-
completeorincorrectdatadisclosures.Wehaveopensourced
our system to enable developers to accurately report their
applications’ data practices. [47].
• We conduct the first study of tracking and fingerprinting in
desktop apps, and uncover the prevalence of inaccuracies
and omissions in macOS’ Privacy Nutrition Labels.
• We propose a unified data disclosure and verification pro-
cessformitigatingtheprivacyviolationsthatstemfromthe
complex and disjoint nature of macOS mechanisms.
2 Background and Threat Model
Here we provide background information on macOS and its app
ecosystem, which is pertinent to our work. Figure1 illustrates a
macOS application bundle and its components, resources, and as-
sociated metadata.
Main Code Frameworks Extensions &
Helpers
Executable
Components Info.plist
Manifest
Entitlements
Non-executable
Components
 Resources
 Property
Lists
Code Sign &
Notary
1 2 3
4 5 6
6A
6B
6C
Figure 1: Application bundle structure and components.
2.1 App Structure and Lifecycle.
macOS applications are built, distributed, and executed within Ap-
ple’secosystemthatintegratesdedicateddevelopmenttools,distri-
bution infrastructure, and runtime enforcement mechanisms. Ap-
ple provides developers withXcode, an Integrated Development
Environment (IDE), which includes interface design, coding, and
resource management, as well as integral tools for code signing
and configuration [33]. App developers produce their own first-
party code 1 and also include third-party SDKs 2 during the
development process. When an application is production-ready,
Xcode packages the contents into a structuredbundle, which de-
velopers can submit to the App Store [29].
Akeycomponent ofthe bundle isthe Information Property List
(Info.plist) 6A, which specifies app-related metadata, such as
thebundleID,versionnumber,supportedplatforms,URLschemes,
and document types [32]. Developers are also required to define
security and privacy-relevant declarations to access protected sys-
tem resources(e.g., camera, location).Entitlementsdefine the ca-
pabilitiesthattheapprequeststhatrequireelevatedprivileges[ 30] 6C.
SystemservicesusethemtogranttheappaccesstorestrictedAPIs
or privileged subsystems, such as iCloud storage, push notifica-
tions,orhardwaredevices.Anotherkeycomponentisthe Privacy
Manifest (.xcprivacy) 6B, a structured file declaring data prac-
tices for the app and embedded SDKs, using structured key val-
ues. Developers specify whether the app or an embedded SDK en-
gages in tracking, and enumerate the specific data types collected
(e.g., device identifiers, coarse location, phone number). Each data
item is individually labeled to indicate whether it is “linked” to the
userandannotatedwiththepurposesforwhichitiscollected,such
as analytics, app functionality, or advertising [24]. Xcode aggre-
gates these manifests into a single report at submission time [24].
Additionally,themacOSsecuritymodelverifiestheappatthree
distinct stages: (i) during the build via Xcode, (ii) during distribu-
tion through the App Store Connect submission and evaluation
system,and(iii)atruntimethroughsignatureandintegritychecks.
Each step corresponds to distinct cross-stage verification and en-
forcement checks applied to bundle components, including meta-
data that define the app’s identity and capabilities, declarations of
access to system resources, and disclosures of data collection prac-
tices.
2.1.1 è Build-time Verification. When developers build an app,
Xcode assembles the source code, static resources, and configura-
tion files into the bundle where different Apple mechanisms verify
theirvalidityandcorrectness.Specifically, Xcodevalidates Info.plist

Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem CCS ’26, November 15–19, 2026, The Hague, Netherlands
entriesstructurallyandsemantically 6A,ensuringthatdeclaredac-
cess to protected resources (e.g., camera, location) is present as re-
quired for runtime access. During development, a developer may
insert permission entries to theInfo.plist file and Xcode auto-
matically signs the binary with the necessary entitlements6C. It
also includes a CodeResources file containing the file hashes in
the bundle 4 and signs it to ensure the app’s integrity. When the
developer is ready to ship the app, they specify the team identifier,
which allows Xcode to sign the bundle with the Apple Develop-
ment certificate 5 , allowing the app to run on other systems.
2.1.2 Õ Submission & Compliance. UponsubmissiontotheApp
Store, Apple performs a combination of automated and manual re-
views to enforce platform-specific policies [26]. This process aims
to verify code-signing integrity, validate entitlements, and ensure
compliance with sandboxing requirements. Developers are also re-
quired to submit the app’s Nutrition Labels. The labels enumer-
ate the categories of data collected (e.g., contact information, lo-
cation, device identifiers), specify whether each category is associ-
ated with the user’s identity, and if they are used for tracking [21].
Labels are structured into three groups: (i)Data Linked to You
(information associated with a personal identity), (ii)Data Not
Linked to You (information purported to be anonymized), and
(iii) Data Used to Track You (information correlated across apps
or services). An example can be found in Figure9 (Appendix A).
2.1.3 Ń Runtime Validation. When the app first launches, the
systemvalidatesitsoriginandintegrity.Thisincludescode-signing
checksandteamidentifierchecks.Thecodeisalsocheckedformal-
ware signatures byGatekeeper and XProtect, Apple’s dedicated
verification systems [31]. At runtime, access to privacy-sensitive
resources(e.g.,camera,microphone)isverifiedbytheTransparency,
Consent,andControl( TCC)framework[ 20]whichcombineschecks
with user prompts, verifying property list files and the system’s
consent database before granting access.
2.1.4 ¿ Data Privacy Communication. Apple enforces a disclo-
suresystemthatseparatesreviewer-facinganduser-facingprivacy
information. Privacy Manifests provide machine-readable dec-
larations used during the App Store review6B, whilePrivacy Nu-
trition Labels present a simplified, human-readable summary
for users. These mechanisms operate independently, and Apple
does not perform consistency checks between them, which can re-
sult in conflicting or inaccurate disclosures. On iOS, developers
must specify predefined “required reason APIs” when accessing
fingerprinting-related interfaces [17]. This requirement does not
extend to macOS [24]. Instead, within the macOS ecosystem, App
Store disclosures coexist with broader system-level enforcement
mechanisms, resulting in a distinct enforcement environment.
2.2 macOS vs iOS.
Mobile operating systems have diverged considerably from tradi-
tionaldesktopoperatingsystems,especiallywithregardtoapplica-
tion isolation and data access control [41, 86, 89]. Here we provide
additional details about macOS and highlight some of the key dif-
ferences with iOS.
 App Sandbox. macOS implements a sandboxing system for
controlling applications’ behavior and capabilities within the sys-
tem. Sandboxed apps are restricted from accessing files owned by
other apps or the user, unless explicitly permitted (e.g., through
system file-selection dialogs). The sandbox is enforced by the ker-
nelusingtheMandatoryAccessControlFramework(MACF),which
checkspolicyviolationsatruntime.Sinceexecutingappsdistributed
outside the App Store is common practice in macOS, it provides
more granularity over specific rules and constraints, which can
be defined inside.sb files. Nonetheless, for convenience and stan-
dardization, Apple provides a default Sandboxing (App Sandbox ),
applied via the com.apple.security.app-sandbox entitlement,
which is mandatory for all apps downloaded via the App Store.
Apps distributed through other sources are not required to im-
port this entitlement. Furthermore, each sandboxed app contains
a filesystem hosted at/Library/Containers which mirrors a de-
fault user’s home directory structure (e.g.,Downloads, Desktop).
These directories are empty by default, and the app must request
permission via the TCC to obtain access. Similarly, access to net-
workingcapabilitiesandPhotosisalsorestrictedbyacombination
of entitlements and TCC-prompts.
The macOS and iOS sandboxes differ significantly in several
key aspects. While iOS enforces a stricter, more contained sand-
box model, macOS adopts a more flexible approach. Apps on iOS
execute in strictly isolated containers, while apps on macOS can
access standard user location and user-selected files. Developers
on macOS also have access to several entitlements that provide ex-
ceptions to the App Sandbox [18]. Notably, there is no equivalent
mechanism on iOS. These entitlements provide access to the main
filesystem( apple.security.temporary-exception.files.home-
relative-path)andtheIPCsystem( security.temporary-exception.mach-
register.global-name). Apps can use exception entitlements to
directly control the system via Apple Events, a macOS-specific au-
tomation feature. Finally, app sandboxing is not mandatory on ma-
cOS, while it is enforced for the App Store applications on iOS.
 System settings storage.UserDefaults(alsoreferredtoasNSUserDe-
faults) is a key-value storage mechanism for storing application
preferencesacrossrestartsandOSreboots[ 19].Itisanapp-specific
storage designed to record configuration data, such as UI prefer-
ences or language settings. For sandboxed apps, the UserDefaults
storeissavedunderthe Preferencessubdirectoryinsidetheapp’s
container. On both macOS and iOS, the UserDefaults file is pre-
populated with specific system-derived default values (e.g., locale-
related settings) required for the intended app functionality. No-
tably, Apple acknowledges that the contents of UserDefaults may
reveal environment-specific information that can be leveraged for
fingerprinting [19].
Summary.WhilemacOSandiOSshareseveralarchitecturaland
implementationfeaturesatboththesystemlevel(e.g.,kernel,XPC
Machmessaging,executableformat)andtheapplicationlevel(e.g.,
app bundles, entitlements, TCC permissions), they arefundamen-
tallydesignedarounddifferentsecuritymodels.iOSfollowsahighly
restrictive,closedecosystemmodel,inwhichAppleenforcesmanda-
tory code signing for all executable code and discourages applica-
tion distribution outside official channels. Permissions on iOS are
tightly constrained, and apps cannot access arbitrary filesystem

CCS ’26, November 15–19, 2026, The Hague, Netherlands Jyotirmay Chauhan, Kostas Solomos, Mir Masood Ali, and Jason Polakis
App Store
< / >
Developer
Documentation
APP
Package
Extraction
 App Store
Privacy Label 
Label Discrepancy
Report
Generated
Privacy Manifest
Extended
Fingerprint
Recognition
Extended Tracking
Report
Source
Analysis
Network
Proxy
UI
Automation
1    Apple
Resources     Bundled Developer Declarations2     Runtime Behavior Evaluation3
a   Execution Flow
Modiﬁcation
b   User Interaction
4
5
    Privacy Nutrition Label Analysis
    Extended Tracking Analysis 
Execution
Flow
Modiﬁcation
Privacy
Manifest
Permission
Management
Entitlements
   Generated
Privacy Labels
Figure 2: An overview of NutriScan’s components and workflow for evaluating macOS apps.
locations outside their containers without explicit user authoriza-
tion. Crucially, iOS does not expose a multi-user account model
and each app operates under a constrained single default user con-
text, reflecting its design as a single-user system.
In contrast, macOS is designed to support more flexible and cus-
tomizable workflows. It supports multiple user accounts and per-
mits application distribution outside the App Store, allowing users
todownloadandexecuteunsignedornon–AppStore–signedcode.
While macOS employs mechanisms such as Gatekeeper and nota-
rization to mitigate malware risk, these protections are not uni-
formly enforced across all execution paths, reflecting support for
a broader set of development and user workflows. As a result, ma-
cOS must address both privacy and system security threats. Apps
operate with broader privileges than on iOS, including access to
user-selected files, system automation interfaces, and native APIs
thatarenotavailableonthemobileplatform.Whilepriorworkhas
primarily focused on privacy label compliance in the iOS ecosys-
tem,macOSapplicationsoperateunderamorepermissivesecurity
model that both extends previously studied attack surfaces and en-
ables additional privacy-invasive risks.
2.3 Motivation and Threat Model.
Itisunclearwhatrole,ifany,desktopappsplaywithinthebroader
online tracking ecosystem. Moreover, several of their characteris-
tics are of particular interest when considering potential privacy
implications. First, they provide direct access to native APIs that
offeraplethoraofdevice-specificinformationandimmutableiden-
tifiers,whichcanbeusedbytrackerstoaugmentuserandbrowser-
fingerprint profiles. Second, users typically log into desktop apps,
thereby providing the identifier (i.e., email) necessary for linking
togethertheuser’svariousdevices[ 81,82].Theriskofcross-device
tracking is evident in FTC reports and prior studies that explored
how companies employ cross-device tracking techniques to cor-
relate different devices that belong to the same user [42, 48, 104].
Third, desktop apps can access other sensitive user data (e.g., ad-
dressbooks,photolibraries)whichcanenablediverseprivacy-invasive
inferences.WeprovideadetailedbreakdownofnativeAPIcapabil-
ities compared to browsers in AppendixB, highlighting how these
capabilities can be leveraged for extending fingerprinting beyond
the browser boundaries.
The privacy implications of these characteristics become even
more pronounced when considering our analysis of Apple’s data
access mechanisms. More specifically, while App Store reviewers
verify the contents of the consolidated app privacy report gener-
ated from individual privacy manifest files, they do not use this
information to verify the accuracy of the Privacy Nutrition Labels
shown to users. This is due to the privacy manifest itself lacking a
requirementforexplicitlydeclaringreasonsforaccessingsensitive
APIs (which can be used to fingerprint users, as we discuss in §4.3).
While no prior work has evaluated the accuracy and completeness
of macOS apps’ Privacy Nutrition Labels, studies have shown that
labels for mobile apps are inaccurate [36, 98], further motivating
our research.
In this study, we are interested in privacy-invasive practices by
first- and third-party code. We focus on a wide range of user and
device-specific data that can be obtained by apps through native
APIs, and misused for various scenarios. Indicatively, we highlight
the following scenarios that capture different privacy-invasive be-
haviors:(i)enrichingexistinguseradprofiles,(ii)correlatingdiffer-
ent devices operated by the same user, and (iii) deanonymizing an
active private browsing session – e.g., code byTracker is embed-
ded in the activeFOOBAR desktop app, while the user is also brows-
ing www.example.com (which includes aniframe from Tracker)
over incognito mode [96] in their browser, allowing Tracker to
deanonymize the private browsing session. Overall, we are inter-
estedincapturingprivacy-invasivepracticesthat are notaccurately
disclosed (or covered by) apps’ Privacy Nutrition Labels.
3 NutriScan: Design and Implementation
In this section, we detail the design and implementation of our
framework, NutriScan. Figure2 shows an overview of the frame-
work’s components and workflow, which we detail next.
1 Apple Resources. Apple lists and distributes bundled ma-
cOSappsviaitsAppStore( č),whichalsohostsappsforotherplat-
forms, including those aimed at iOS and iPadOS. Apple requires
that developers submitting to the App Store ensure that the Nutri-
tion Label and Privacy Manifest, among other declarations, reflect
the data collection practices relevant to the submitted version of
the app. To ensure the validity of our evaluation, we access app
bundles directly from the App Store, instead of using third-party
repositories.Wealsocollectthecorrespondinguser-facingPrivacy
Nutrition Labels that the developer has declared on the App Store.
2 Bundled Developer Declarations. Apps downloaded from
the App Store are bundled and structured in a standard format
(see §2). MacOS apps declare metadata relevant to the system by

Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem CCS ’26, November 15–19, 2026, The Hague, Netherlands
listing key-value pairs inInfo.plist, from which we extract the
app’s bundle identifier, version, and other metadata.
f Privacy Manifest. Apple holds developers accountable for
all of the code included in their app, including any third-party
SDKs they include [16]. However, the size and complex nature of
these third-party codebases make it difficult for developers to in-
dependently ensure accuracy and completeness. Apple, therefore,
mandates that third-party SDKs disclose their own data collection
practices via a key-value list in aprivacy manifest file, named
PrivacyInfo.xcprivacy.Whenbundlingtheapp,XCode( >=v15)
includes manifests from all third-party SDKs in the output. We ex-
tract and parse all available privacy manifest files, which we then
map to the corresponding entries in the Nutrition Labels.
To compare manifests with Nutrition Labels, we create a union
of all the manifest files present inside the app. This final file con-
tainsasupersetofall NSPrivacyCollectedDataTypevalueswhich
we then compare against the application’s Nutrition Labels. We
considerthepresenceofamanifest-declareddatatype(e.g., NSPri-
vacyCollectedDataTypeName) coupled with the absence of the
corresponding data item (e.g.,Name) from the Nutrition Labels as
a discrepancy/violation. We note that we only flag a discrepancy
when a Privacy Manifest item is found to be missing from the Nu-
trition Label, but not the other way around.
f Entitlements. While building the app, developers can add
Capabilitiestohelptheappaccesscertainsystemresources(e.g.,aut-
ofill, access to background tasks). The contents of these entitle-
ments help us evaluate a set of sensitive resources that the app
accesses, a subset of which maps to entries in the Nutrition Labels.
We parse Apple’s Documentation[30] and third-party sources [68]
to assemble a definitive list of entitlements. Since several entitle-
ments remain undocumented by Apple, we cannot guarantee com-
pleteness in our list of entitlements; however, our final list of en-
titlements was sufficiently complete to allow us to parseall of the
entitlements encountered when analyzing the apps in our dataset
(see §4). We also map entitlements to Nutrition Labels’ data items
such as name, physical address, coarse location etc. This mapping
was done independently by two researchers, who provided the
samemappingforover90%ofthecases.Forexample, ”com.apple.security.personal-
information.addressbook” was mapped toName, Physical Address .
In the few cases where there was disagreement, the final mapping
was resolved through mediation and discussion with a third re-
searcher. The full mapping can be found in AppendixC.
Using our mapping, we create an enriched profile for each app
and subsequently compare this against the label to the actual Nu-
trition Label to identify discrepancies. We further analyze the dis-
crepancies based on the individual data items. Each discrepancy
between the generated Label and what the app declared counts as
a single violation.
3 Runtime Behavior Analysis.Anapp’sruntimebehaviorpro-
videsreliableinsightsintoitsdatacollectionpractices.Wedevelop
a dynamic analysis approach that evaluates app behavior across
multiple dimensions.
a Execution Flow modification. We follow a two-pronged
approach for observing the app’s behavior upon execution: modi-
fying memory at runtime (required for Frida) and intercepting net-
work traffic via a proxy.
f API Hooking. Native API hooking is a technique often used
inreverseengineeringtoredirecttheflowoftheexecutionpointer.
We use Frida, a dynamic instrumentation tool that adopts atram-
poline code injection method, wherein it modifies the system’s ex-
ecution flow so that when a target function is called it redirects
the system to run custom code before returning to the target func-
tion [61, 62]. Frida does so by modifying the memory location of
a target function on the fly. We modify the flow of the target pro-
cess by adding logic within two event blocks; (a) code within an
onEnterblockthatexecutesbeforethetargetfunctionisexecuted,
and(b)codewithinan onLeaveblockthatexecutesafterthetarget
functionhasexecuted.Themodifiedfunctionreturnsacallback,in-
cluding a stacktrace of the current process, to the aforementioned
event blocks, which allows us to differentiate between first-party
and third-party execution.
Frida’s trampoline injection method adds overhead, especially
for frequently called functions. Prior work that analyzed the cost
of hooking system and function calls across platforms found that
Frida can add 128x physical memory overhead and 129x CPU User
Time while instrumenting macOS APIs [78]). To ensure that our
app instrumentation remains effective despite this overhead, we
balanceprogramexecutionwithlogging,bydetachinghooksfrom
atargetfunctionafterobserving10callstoit.Whilethismayresult
in our system missing certain details (e.g., an additional instance
of a third-party SDK calling a specific API that has already been
logged), it improves our system’s efficiency and reliability.
Reading and modifying processes on macOS requires access to
the task_for_pid Mach (IPC) call, which is denied by default by
System Integrity Protection (SIP, an XNU kernel extension). We
disableSIPonthetestdevicebybootingitintorecoverymode[ 15].
DisablingSIPcanbedetectedbyapps,whichcouldresultindecep-
tive apps changing their behavior to avoid detection. As such, our
findingsin§ 4presentalowerboundofprivacy-invasivebehaviors.
Network Proxy. Apart from recording relevant API access, we
inspect network traffic to detect the exfiltration of collected data.
We use the man-in-the-middle proxy (mitmproxy) [49], which re-
quires installing root certificates on the device so as to capture
all HTTP(S) and DNS requests sent from the evaluated app. Nu-
triScan parses the collected network traces to identify instances of
collected data being transferred, along with details of the domains
that receive it.
Wealsointegratecertificate-unpinningviatheSSLKillSwitch[ 54]
Frida script, which overrides SSL checking functions in several
popular libraries. This script is also injected before the entry point
of the executable allowing us to intercept TLS traffic from applica-
tionlaunch.AppsmayincludecustomizedSSLpinninglogicwhich
canbehardtogeneralizeandbypassthusleadingtoasubsetofnet-
work requests not being intercepted. This is a known challenge,
which has affected prior studies as well [98].
b User Interaction. UI automation is performed using a
heuristic-based approach via Apple’s Accessibility API. Our script
captures the app state as a nested tree data structure, where each
UI element forms a node. This tree is fetched after each interac-
tion; login pages and forms are detected via heuristics and popu-
latedwithsyntheticdata.Theinteractionscriptfollowsaweighted
semi-randomapproachtoselectinteractableelementsandexecute
the selected action.

CCS ’26, November 15–19, 2026, The Hague, Netherlands Jyotirmay Chauhan, Kostas Solomos, Mir Masood Ali, and Jason Polakis
The tool identifies elements such as Text fields and generates
random text of varying lengths to fill them. The tool can also pro-
vide apps with inputs from the filesystem via Apple’s Finder App
(filepicker), such as picking a media file for a media player or spec-
ifying the output directory. Our navigation flow covers a wide
range of user interactions, so that our tool can navigate an app
more effectively than basic monkey testing [58].
f Permissions. Apple enforces runtime checks on sensitive
resources like the camera, microphone, and filesystem. In such sit-
uations, macOS prompts the user to provide explicit permissions.
Once granted (or denied), the system records this choice in a user-
specific database that it queries during future attempts. We en-
sured that all user permission prompts that pop-up during inter-
action are accepted. This has two benefits: (i) it ensures that our
tool’s interaction with the app remains uninterrupted, and (ii) it
allows us to capture all observed permission prompts by accessing
the app’s permission database at the end of its interaction session.
4 Privacy Nutrition Label Analysis. Subsequently, NutriScan
collects the logs generated during the app’s execution and com-
pares them against the app’s Nutrition Labels. We consider four
perspectives (marked withf in Figure2) to an app’s data collec-
tionpractices.Weindependentlyconsidereachsourceanddevelop
unique mappings between its taxonomy and the taxonomy used
by Apple’s Nutrition Labels. We first map API calls to the data
types which should be declared. Then for each API call made by
the app, we add the mapped labels to create anaccurate Nutrition
Label, which is the union of all unique data labels. NutriScan then
compares the results of the mappings against the actual Nutrition
Labels obtained from the App Store, and flags any discrepancies.
5 Extended Tracking Analysis. While Nutrition Labels pro-
vide an overview of the app’s data collection, they do not accu-
rately capture its tracking capabilities, as theydo not account for
device fingerprinting (in online tracking this is typically achieved
through browser fingerprinting [73]). This relies on collecting a
widerangeofdevicecharacteristicslikethescreenresolution,model,
OS version, GPU vendor, etc. Individual attributes are not unique
but can provide a high-entropy identifier when combined. To ac-
count for such practices, we created a table of attributes using Ma-
cOS’s system_profiler and the test user profile, and mapped it
to individual data items likeuser id and device id. We also
included coarser device attributes not covered explicitly by Nutri-
tion Label. Our system searches for these attributes in the network
traffic. This is a well-established strategy for identifying apps exfil-
trating data of interest; we adapted hashing and encoding tech-
niques from prior work [56, 87]. We consider multiple hashing
(e.g.,MD2/4/5,SHA1/224/256/384/512,MMH3)andencoding(e.g.,Base16/32/58/64,
gzip, LZ-string) functions. For each identifier of interest, we pre-
computed a pool of potentialmulti-layered hashed and encoded
values, which we search for in captured traffic including the Re-
quest URL, the body ofPOST requests, and response bodies.
4 Experimental Measurements
In this section, we provide the first measurement study on privacy
violations in the macOS desktop environment. We demonstrate
our system’s capabilities in detecting application-component dis-
crepancies in bundle-level declarations (§4.1), identifying Nutri-
tion Label violations via data exfiltration through application be-
havior (§4.2), and also extend our analysis to device-based finger-
printing capabilities in macOS applications (§4.3).
Experimental Setup. We use an M4 Macbook Air to run our
experiments, and create a fresh Apple account to download apps
onto the device from the official Apple App Store. To collect repre-
sentative data, each app is individually executed for∼5 minutes, a
threshold selected after exploratory analysis showed no additional
violations beyond this point. This is also consistent with prior re-
search on mobile dynamic analysis [36, 98] (nonetheless, we note
that our results represent a lower bound, which could be further
amplified with longer exercise times). For apps requiring an ac-
count, a single account was created while all other aspects of the
app interaction, such as logging in and UI clicking, are automated.
After completing the dynamic analysis, all callback logs are auto-
matically processed to generate accurate Nutrition Label for each
applicationandtoproduceanaggregatereportincludingtheviola-
tions and discrepancies detected by NutriScan across our dataset.
Dataset. While Google provides detailed ranking and popular-
ity metrics across app stores (e.g., Google Play Store, Chrome Ex-
tension Store), the Apple App store does not disclose specific sta-
tistics or a single global ranking for macOS or iOS apps. Instead, it
publishes category-specific lists of popular apps that are updated
based on proprietary metrics, including recent download activity.
Since download statistics are not publicly available, we use the
number of user ratings as an indicator of application popularity.
To construct our dataset, we initially assembled a list of all app
URLs via the sitemap[28] of Apple’s website, which we used to
scrape their app webpages. Interestingly, upon closer inspection,
we found that Apple’s sitemap only includes iOS and iPad apps
while excluding macOS apps. Moreover, when a particular macOS
app also has an iPad or iOS version, the app’s metrics (such as its
rating or number of ratings) correspond to the iPad or iOS version
instead of the macOS version. The macOS version’s ratings, which
often differ significantly from the iOS or iPad version, are only
available within the dedicated App Store application.
To enhance our dataset, we leveraged AppFigures [11], a popu-
larappanalyticsplatform.Wescrapedthetop250rankedMacapps
foreachofthe20differentcategories,mergedthemandfilteredfor
appswhichweredesignedformacOS.Foreachselectedapp,wead-
ditionallyscrapedtheirappstorewebpagetocollecttheuserrating
counts.Thisresultedinover1,800+apps,rangingfromhighlypop-
ularappssuchasMicrosoftWord(1.7Mratings)tosmallerandless
popularapplicationssuchastheVisioFileEditor(1rating).Wesub-
sequently excluded 350 applications that employed anti-analysis
techniques, which prevented dynamic instrumentation via Frida.
Accordingly, our final dataset (referred to asTotalApp) consists of
two different subsets: (i) 500 popular apps based on the number of
userratings( TopApp),and(ii)500appsrandomlyselectedfromthe
remainder of the collected apps (RandomApp). TopAppspans a wide
range of categories, including Productivity (17%) Utilities (15%),
Games(5.7%),PhotoandVideo(8.7%),Business(5.9%)Music(6.9%)
and Health & Fitness (2.7%) among others. Similarly,RandomApp
includes applications from categories such as Productivity (3.3%),
Utilities (5.7%), Developer Tools (10%), Graphics & Design (8.1%),

Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem CCS ’26, November 15–19, 2026, The Hague, Netherlands
Education (5.5%) and Business (5.9%) among other categories. For
each app in the dataset, our system parses theInfo.plist to ex-
tract the bundle identifier, and to also retrieve each application’s
informationandnutritionlabelvaluesviaiTunes’spublic API[ 34].
We also detected that 14.9% of the applications restricted function-
ality by requiring an account, for which we manually registered a
dedicated test account. In addition, 47 applications in our dataset
offered a free trial associated with our Apple account, which we
activated during dynamic analysis [46].
Attribution. As part of our analysis, we are interested in at-
tributing data access and potential discrepancies to first- or third-
party code. We define first-party origin to include both applica-
tion developer provided components and Apple-provided system
libraries and frameworks bundled with macOS, as these are re-
quired dependencies for all applications. Any other origin is classi-
fiedasthird-party.ForPrivacyManifests,eachfileispresentinside
a parent folder which contains the name of the associated frame-
work or the SDK. Since native macOS components do not define
manifest files, we use the location of the manifest file in the app
bundle to determine whether it is first party or third party.
Regarding API hooking and backtrace attribution, our system
captures the sequence of binaries, dynamic libraries and frame-
worksinvolvedineachfunctioncall.ThesetypicallyincludeApple
frameworks and system libraries (e.g., UIKit [14], CFNetwork [12],
libsystem_pthread.dylib, and libobjc.A.dylib), the applica-
tion’scorebinary(e.g.,VPNUnlimited[ 69]),orthird-partylibraries
and frameworks (e.g., FirebaseCore or FirebaseCrashlytics [60]).
First-party binaries are identified by matching the binary name to
the application name.
The primary challenge in this process, is to identify the native
framework and SDKs, since there is not available documentation
for all system components. To address this, we curated a reference
listusingacombinationofopen-sourceGitHubrepositories[ 6,93],
search engines, and macOS system file listings. Any frameworks,
SDKs, or binaries not identified as first-party or native Apple com-
ponents are classified as third-party.
4.1 Bundle-Declared Privacy Capabilities
Inthefirststageofouranalysis,weanalyzeeachapplication’sbun-
dle to collect its declared privacy capabilities. We extract the set
of permissions specified in itsEntitlements and parse the asso-
ciated Privacy Manifest to determine the declared data-access
requirements. Both entitlements and manifests specify these per-
missionsdifferently(section 2).Whilemanifestscontaindeveloper
disclosuresaboutthedatacollected(similartoNutritionLabel),en-
titlements are more granular and directly affect the app’s runtime
privileges.Declarationsarethencomparedagainstthecorrespond-
ing Nutrition Labels to identify missing data items, i.e.,discrep-
ancies.
Entitlements. All 1,000 applications analyzed by NutriScan de-
clareatleastoneentitlement,consistentwithApple’sdevelopment
model, which requires applications to be code-signed with a ded-
icated entitlement (e.g., com.apple.security.app-sandbox) for
effective distribution [27]. We identified entitlement discrepancies
in 82.8% of the applications (n=828), where applications declared
Table 1: Distribution of apps with discrepancies between
their declared entitlements and corresponding Nutrition La-
bel data types. (For more details see Table 6, Appendix.)
Entitlement Discr. (%) Top. (%) Random. (%)
com.apple.security
files.user-selected.read-only 95% 94.1% 95.7%
personal-information.location 93.6% 93.8% 93.4%
personal-information.addressbook 93.8% 93.9% 92.8%
files.downloads.read-write 92.3% 93.8% 89.6%
personal-information.photos-library 90.8% 90% 92.1%
files.downloads.read-only 88.8% 66.6% 100%
files.user-selected.read-write 90.7% 87.7% 94.5%
device.microphone 89.4% 88.2% 90.4%
assets.pictures.read-write 87.1% 89.4% 83.3%
personal-information.calendars 86.6% 84.7% 92.3%
device.audio-input 86.1% 87.6% 84.5%
device.camera 84.5% 84.5% 84.4%
assets.pictures.read-only 80.9% 75% 100%
temporary-exception.files.home-relative-path.read-only 68.7% 61.5% 100%
com.apple.developer
healthkit 100% 100% 100%
healthkit.access 100% 100% 100%
ubiquity-kvstore-identifier 93.6% 90.5% 100%
networking.networkextension 90.3% 89.4% 91.6%
ubiquity-container-identifiers 90.7% 87.1% 97.3%
in-app-payments 66.6% 50% 100%
game-center 65% 66.6% 64%
financekit 50% 50% N.A.
com.apple
mail 100% 100% 100%
accounts.appleaccount.fullaccess 100% N.A. 100%
at least one entitlement that grants access to data not disclosed in
their Nutrition Labels.
Table 1 presents the proportion of apps where a declared en-
titlement’s data type is absent from the Nutrition Label. We find
that the majority of apps exhibit high omission rates across all en-
titlements,withseveralreaching100%,indicatingthatnoappscon-
tainingthatentitlementdeclaredtheassociateddataaccessintheir
Nutrition Labels. In thecom.apple.security namespace discrep-
ancies span both file operations and user data access. The highest
omission rates occur for personal-information.addressbook,
files.user-selected.read-only, andpersonal-information.
location. The com.apple.developer namespace exhibits a sim-
ilar omission pattern, with complete omissions for sensitive APIs,
including health data and contact information.
Moreover, Apple-related integrations (e.g.,mail, and appleac-
count.fullaccess lack any corresponding disclosure in the Nu-
trition Label, indicating that omissions persist even for capabili-
ties tied to highly sensitive, platform-level services. Notably, we
found that Apple’s own Swift Playground application doesn’t de-
clare thefullaccess entitlement, an Apple-exclusive entitlement
with complete access to the user’s iCloud, Mail, etc. These omis-
sions have a direct and significant impact on user privacy, as users
are not aware of the data access capabilities they grant to applica-
tions at installation time.
We also compare data labels which are tied to explicit user con-
sent[20]againstdatalabelswhicharenot.AsFigure 3shows,enti-
tlement violations rate remained high in both cases. Sensitive Info
(Health Data), Emails and Text Messages, and Credit Info exhibit
100% discrepancy, as none of the apps declared the appropriate en-
titlements in their Nutrition Label.

CCS ’26, November 15–19, 2026, The Hague, Netherlands Jyotirmay Chauhan, Kostas Solomos, Mir Masood Ali, and Jason Polakis
 0
 20
 40
 60
 80
 100
Emails Or Text Messages
Sensitive Info
Credit Info
Other User Content
User Id
Payment Info
Name
Purchase History
Email Address
Physical AddressPhotos Or Videos
Audio Data
Precise LocationCoarse Location
Disclosure-only Runtime Permission
Discrepancy Rate (%)
Figure 3: Discrepancy rates between declared entitlements
and Nutrition Labels data types, grouped by disclosure-only
access and TCC-protected runtime permissions.
 0
 20
 40
 60
Other Diagnostic Data
Other Data TypesPerformance Data
Device Id
Purchase History
User Id
Crash Data
Product Interaction
Coarse LocationOther Usage Data Email Address
Name
Phone Number
Customer SupportPhotos Or Videos
Search History
Other User Content
Other User Contact Info
Audio Data
Other Financial Info
Advertising Data
Contacts
Health
Privacy Manifests (%)
Figure 4: Discrepancies across Nutrition Label data types
and privacy manifests.
Privacy Manifests. While entitlements declare system-level
capabilities, privacy manifests disclose data collection at the SDK
level. We extracted 588 privacy manifests in total from our dataset.
Of these, 67 (11.3%) applications included a first-party or app-wide
manifest, which is generated during the build process, while the
majority (88.6%) originated from third-party providers.
Over 70% of all apps with Privacy Manifests (n=588) did not de-
clareany CollectedDataTypes.Amongtheremainingapps(n=168),
135 (80.3%) apps declaredCollectedDataTypes in their manifests
thatwereabsentfromthecorrespondingNutritionLabels.Overall,
discrepancies were detected in 92.3% of the first-party manifests
(n=12) and in 78.2% (n=122) of the third-party manifests. The dis-
crepancies typically involved fields such as Other Diagnostic Data,
Device ID, and sensitive fields like Coarse Location and Email Ad-
dress.
While entitlements allow an app to access specific data types,
manifests disclose the type of data being collected. Each violation
in privacy manifests amounts to a data label being collected with-
out a corresponding disclosure. Figure4 illustrates the discrepan-
cies between privacy manifests and the corresponding Nutrition
Labels. The highest affected type is Other Diagnostic Data, where
37.5% of manifest declarations lack a matching Nutrition Label en-
try. This label represents coarse devices attributes (chipset model,
OSversions)andsoftwaretelemetry(networkorGPUperformance).
This is a catch-all category for “purposes of measuring technical
diagnostics related to the app” [21]. Additionally, Nutrition Label
omissions were detected for Other Data Types (20.2%), Device ID
(12.5%), and Purchase History (9.5%).
Manifest files in SDKs are intended for developers when inte-
grating third-party components into their applications. The high
rate of discrepancies detected by NutriScan indicates that devel-
opers often overlook these files. This may be due to various fac-
tors, such as a lack of awareness of Privacy Manifests or confusion
caused by Nutrition Labels [76]. Prior work has also reported that
developers can be confused or misunderstand the scope of permis-
sionsrequestedby third-partylibraries[ 90].Othercases mayexist
duetodeveloperscollectingdatafordebuggingand,thus,consider-
ing that data collected for testing purposes does not need to be dis-
closed. Finally, discrepancies could also reflect intentional under-
disclosure, as work has found that permission abuse can lead to
app removal by users [40].
Privacy Disclosure Inconsistencies. Overall, the divergence
between Nutrition Labels and bundle declarations reveals system-
atic omissions. This misalignment enables applications to collect
user and device data without accurate disclosure, thereby prevent-
ing users from understanding the apps’ privacy practices. The con-
sistently high omission rates across major functionalities reveal a
structuralweaknessinmacOS’sverificationprocess,whichdetects
thepresenceofaNutritionLabelbutdoesnotverifyitsconsistency
with declared capabilities. Given the scale and compliance obliga-
tions of major third-party services, these omissions demonstrate
that the misalignment extends beyond application developers and
furtherweakensthereliabilityofApple’sprivacylabelmechanism.
4.2 Behavior-based Violations
Next, we analyze application runtime behavior to detectprivacy
violations, defined as cases in which an app accesses or transmits
user or device data without a corresponding Nutrition Label dec-
laration. We compare their data flows to declared capabilities, to
detect non-disclosed data collection and transmission, and reveal
behavior-based inconsistencies beyond the bundle-level analysis.
Runtime Traces. We applied our dynamic analysis pipeline
(§3)to TotalApp,collectingexecutiontraces,nativeandthird-party
APIcalls,andassociateddata.NutriScanthenmapstheruntimebe-
haviorstotheircorrespondingNutritionLabelcategories,allowing
the direct comparison to their reported disclosures. We evaluated
appdevelopers’adherencetoAppStorerequirementsfordeclaring
data collection practices to end users, by comparing the Nutrition
Labels with the data collection observed through the hooking of
Native API Calls. To quantify the extent ofnon-compliance we cal-
culate the following metric:
Non-compliance = 1 − 𝐴∩𝐵 𝐵
A:= Set of Data Types declared within Nutrition Labels.
B:= Set of Data Types observed from Native API Calls.
Figure 5 illustrates the distribution ofnon-compliance for the apps
inourdataset. Eachundeclareddatatype (e.g.,NameorUser ID)is

Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem CCS ’26, November 15–19, 2026, The Hague, Netherlands
 0
 20
 40
 60
 80
 100
 10  20  30  40  50  60  70  80  90  100
TotalApp RandomApp TopApp
Non-compliance (%)
Number of Apps (%)
Figure 5: Degree of Nutrition Labels non-compliance across
evaluated applications.
 0
 20
 40
 60
 80
 100
Coarse Location
NameUser IdDevice Id
Advertising Data
Payment Info
Credit Info
Physical AddressPhone Number Other User ContentPhotos Or Videos
Audio Data
Precise LocationEmail AddressBrowsing History
Apps (%)
Figure 6: Distribution of violations by Nutrition Data Labels.
counted as a single violation, regardless of whether it is accessed
by one or multiple API calls.
Approximately 15% of the apps were fully consistent with their
Nutrition Labels, achieving complete compliance and accurate pri-
vacy disclosure. Prominent apps among these include Microsoft
Excel, One note and Outlook. While these apps collect sensitive
identifierslikeDeviceID,Emailaddress,CoarseLocationandCon-
tact Data, they accurately disclose it in their Nutrition Label. Nev-
ertheless, the fact that only 15% of the apps achieving full com-
pliance is a concerning finding and comparable to the extent of
non-compliance reported for mobile apps [36].
Moreover, 60% of the apps omitted half the data types that they
collect from their Nutrition Labels, and approximately 38% did not
declare any of the data types, resulting in total non-compliance.
Whilemostofthesecasesarelesspopularapps,thepopularLetsVPN
app [4]1 declares in its Nutrition Label that “No Data is Collected“.
To make matters worse, LetsVPN’s privacy policy [74] which is
publicly available in the app’s App Store page, states that the app
collects Device ID, Purchase Information among other data types.
Under Apple’s Nutrition Label guidelines, this type of data collec-
tion is required to be disclosed. NutriScan further detected that
1While the Apple App Store does not provide download numbers, indicatively,
LetsVPN has 5M+ downloads in the Android Play Store.
 0
 20
 40
 60
 80
 100
Audio Data
Precise LocationAdvertising DataPhysical AddressPhone NumberPhotos Or VideosOther User Content Email Address
Device Id
Browsing HistoryCoarse Location
Payment Info
Credit Info
NameUser Id
1st-party 3rd-party
Violation Origin(%)
Figure 7: Breakdown of violations by attribution to first or
third party.
LetsVPN accesses User ID, Device ID, and Coarse Location at run-
time,indicatingadiscrepancybetweendeclaredandobserveddata
practices. In contrast, we find that widely used apps (e.g., What-
sApp) are more likely to provide accurate Nutrition Labels.
Notably, we detect substantial variance in the non-compliance
rate between TopApp and RandomApp. A larger fraction of apps in
therandomlyselecteddatasetarenon-compliantcomparedtopop-
ular apps. Nearly 45% of apps in the random dataset are fully non-
compliant compared to 30% for popular apps. One potential fac-
tor contributing to the higher non-compliance among less popu-
lar applications is differences in available resources. Popular appli-
cations are typically developed by larger organizations with dedi-
cated teams, which allows higher attention to privacy compliance
compared to less popular applications. Our results demonstrate
thatruntimebehaviorsdivergesignificantlyfromdeclaredprivacy
practices, indicating that Apple’s disclosure mechanism is neither
effectively enforced nor consistently adopted by developers.
Data type Violations. To quantify the impact of runtime behav-
iors on the accuracy of Nutrition Labels, we mapped omitted data
typesforeachappandmeasuredtheirprevalence.AsshowninFig-
ure 6, the most frequently undisclosed item was Coarse Location,
detected in approximately 70% of the apps and primarily exposed
through Apple’sNSUserDefaults API, which exposes the nearest
major city. This value is set by macOS when selecting the system’s
timezone. Other categories of PII, including Name (30.1%), User ID
(24.5%), and Device ID (18%), were also frequently collected with-
out disclosure.
Since apps access combinations of identifiers and data in paral-
lel, violations do not occur independently. The most common com-
bination involved was User ID, Name, and Coarse Location, while
another frequent pattern involved simultaneous collection of De-
viceIDandCoarseLocation.Theseoverlappingviolationsincrease
privacy risks as they can be leveraged to cross-link user identities
across devices and online contexts.
Violation Origin. We further attribute API accesses to first- or
third-party based on the Frida backtrace. This backtrace captures
the stack at the time of execution, and maps the memory locations

CCS ’26, November 15–19, 2026, The Hague, Netherlands Jyotirmay Chauhan, Kostas Solomos, Mir Masood Ali, and Jason Polakis
 0
 50
 100
 150
 200
 250
 300
Google
Amazon Web Services
Revenue Cat
MicrosoftAmplitude
Functional Software
FastlyMeta
MixPanelCloudflareSmartbearAkamai Other
Apps (#)
Figure 8: Top third-party entities present in apps.
to the relevant code that resulted in the call. To associate undis-
closed data access to the originating party, we apply the attribu-
tion process described previously. Each mismatch between an API
call and data label item is considered a separate violation.
As shown in Figure7, the majority of violations originates from
first-party behaviors. This finding contrasts with prior findings for
Android applications, where the majority of the violations were
attributedtothird-partycode[ 36].Inmoredetail,formultipledata
types (e.g., Audio Data, Precise Location, Browsing History) the
majority of violations was attributed to the first-party. In contrast,
identifiers such as User ID, Device ID, and Name are more evenly
collected by both parties, with up to 40% of violations linked to
external SDKs and libraries.
We detect a high number of first-party Nutrition Label viola-
tions,incontrasttoprivacymanifestswherethird-partyviolations
dominate. This discrepancy is driven from the broader availability
of third-party manifests, which results in a higher share of viola-
tions originating from external SDKs. Notably, one-third of apps
exhibits third-party Nutrition Label violations, a proportion com-
parabletothosewiththird-partymanifestviolations.Overall,both
first- and third-party origins contribute to privacy violations, al-
though this distinction is less pronounced in the manifest analysis.
Third-Party Entities.Whiledetectingundeclaredaccessatrun-
time establishes that apps collect sensitive data without disclosure,
it does not determine whether data is directly exfiltrated beyond
theapplicationboundaries.ToassesswhetherAPIaccessalsoleads
to data leakage, we analyze the network traffic generated during
the app’s execution and categorize the prevalence of third-party
domainsbeingcontacted.Figure 8illustratesthedistributionofen-
titiescontactedbyallappsacrossthedataset.Eachdomainwascat-
egorizedusingtheTrackerDB[ 63]andDisconnecttrackerlists[ 55],
and then mapped to their parent service provider based on the
eTLD+1. The most common services originate from Google, reflect-
ing their major roles as SDK and service providers. Amazon Web
Services is also prevalent, operating primarily as a hosting infras-
tructure. The “Other” category captures a long tail of third-party
domains, each associated with a smaller number of apps. We note
that these patterns mirror those measured on web and mobile plat-
forms, where tracking/analytics/infrastructure is concentrated to
a limited number of major providers [51].
Data Exfiltration. We next assess whether the captures network
communications, transmits sensitive user or device data. In total,
497 applications transmitted user and device information over the
network. Among these, 204 applications transmitted identifiers ex-
plicitly protected by the Nutrition Labels, and 62 of those did not
disclose the corresponding data types. The remaining apps trans-
mitted coarser, fingerprint-related attributes, such as kernel or OS
version, Mac model identifier, and screen resolution. Table2 re-
ports the breakdown of undisclosed data types collected, and the
topdomainsreceivingthedata.Acrossalldatatypes,themostcom-
monlycontactedentitieswereGoogle( googleapis.com, 1e100.net),
Amazon( amazonaws.com, cloudfront.net),andFacebook( fbcdn.net,
facebook.com). These entities primarily provide advertising, ana-
lytics, or infrastructure services, highlighting the privacy implica-
tions of undisclosed data transmission by desktop apps.
4.3 Extended Fingerprinting Analysis
In the final part of our study, we present a taxonomy of all device
identifiers we encountered during our analysis. This analysis is in-
dependentofthecurrentdesignofNutritionLabelsandinstead,we
consider all device identifier and related attributes transmitted off-
device. We analyze their prevalence in app network traffic and cat-
egorize them by the type of information they reveal, demonstrat-
ing how third parties can leverage them for augmenting device
fingerprinting. The identifier list was generated via thesystem_-
profiler command on macOS, which provides a highly detailed
technical overview of a device’s hardware capabilities.
Table 3 lists the identifiers detected, representative values, and
theirprevalenceacrossapps.Severaldevice-specificidentifiers(e.g., Sys-
tem Version and Kernel Version) are disclosed by default through
Apple’s networking stack, as they are embedded in the user-agent
stringautomaticallygeneratedby CFNetwork,thedefaultnetwork-
ing library [12]. Interestingly, the version value increments with
each operating system update (e.g., macOS 15.6, Darwin 24.5.0),
allowing trackers to classify the devices by patch level. This leak-
ageextendsthefingerprintingsurfacebeyondApple’sdeclared De-
vice ID category, introducing a persistent, fine-grained feature
for tracking. Additional identifiers expose detailed device charac-
teristics and configuration information. TheModel Identifier
directly encodes hardware specifications; for example,Mac16,12
denotes the 13-inch MacBook Air with an M4 chipset [13]. We de-
tected this identifier in the network traffic of 222 apps (44%), repre-
senting a significant fraction of our dataset. Apps also transmitted
screen resolutions attributes that are considered as high-entropy
for fingerprinting within browsers [102]. While native resolution
can also be inferred from the model identifier, the HiDPI value
varies with user configuration, introducing a distinct fingerprint-
ing modality that expands the range of device-specific attributes
availabletothirdparties.Furthermore,identifiersexposedthrough
Apple’s Graphics API, Metal [2], also introduce an independent
hardware feature, further enriching the fingerprinting surface. Fi-
nally, we detected a specific combination of identifiers (“Darwin
12.3.0”,“15.3.2”,“M4”,“<REDACTED_CITY>”)in72apps’network
traffic, directly revealing the device and execution environment.
Summary.Ouranalysishighlightsthevariousshortcomingsin
the current design of Apple Nutrition Labels. In its current state,

Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem CCS ’26, November 15–19, 2026, The Hague, Netherlands
Table 2: Applications exfiltrating sensitive data in violation
of Nutrition Label, and the corresponding third-party do-
mains.
Data Type Apps Domains
cloudfront.net, akamaitechnologies.com,Name 44 fbcdn.net, amazonaws.com, 1e100.net
Coarse 124 googleapis.com, 1e100.net, Location amazonaws.com, facebook.com, braze.com
User ID 10 cloudfront.net, amazonaws.com, 1e100.net
Device ID 16 google.com, unity3d.com, icandesignapp.com
Email 7 1e100.net, amazonaws.com
Table 3: Access of fingerprintable device attributes.
Device Attribute Description Apps
System Version macOS 15.3.2 362
Kernel Version Darwin 24.3.0 408
Chipset Model Apple M4 241
Location Redacted 145
Model Identifier Mac16,12 222
Resolution(HiDPI) 1470 x 956 Retina 145
Email Redacted 24
Display Type Liquid Retina XDR Display 147
Name Redacted 59
User Name Redacted 59
Boot Volume Macintosh HD 78
Hardware UUID Redacted 21
Metal Support Metal 3 54
Computer Name Redacted’s MacBook Pro 53
Bus Built-In 18
Serial Number (system) Redacted 11
Hardware AirPort 21
Domain Name 10.0.5.1 3
MAC Address Redacted 6
IPv4 Addresses 10.0.5.14 2
the Nutrition Label framework is insufficient for both developers
and end users. Developers must navigate the complex compliance
system encompassing entitlements, privacy manifests, and Nutri-
tion Labels. In addition, the lack of Nutrition Label verification
during App submission also means that users encounter incom-
pleteorincorrectlabels,underminingtheirtrustinthesystem.Fur-
thermore, given the proliferation of device fingerprinting for user
tracking and risk-based authentication, and the extent of device-
identifier exfiltration detected by NutriScan, the absence of a ded-
icated fingerprinting category in Nutrition Labels is a significant
oversight. While Apple has acknowledged the fingerprinting po-
tential of certain system APIs[22] and requires developers to dis-
close why they are used, this disclosure is relegated to the privacy
manifests which most end users will neither read nor encounter. A
ground-upredesignofNutritionLabelsthatfocusesonsimplifying
Apple’s data collection nomenclature, and extending it to include
device fingerprinting, will provide a more comprehensive and im-
pactful privacy disclosure mechanism.
5 Mitigating Disclosure Discrepancies
A key takeaway from our measurement study and data analysis is
that disclosures cannot rely on developer self-reporting, and effec-
tive mitigations require replacing this implicit-trust-based model
with centralized verification. NutriScan demonstrates that auto-
mated analysis can generatereliable and accurate disclosures by
cross-referencing bundle components. These audits can be inte-
grated directly into build and deployment pipelines. For instance,
Nutrition Labels can be pre-populated from SDK manifests embed-
dedintheapp,reducingredundancyandminimizingomissions. Xcode
alreadyhastheabilitytocombineallthird-partymanifestfilesinto
anapp-widemanifestfile.Yet,developersarecurrentlyrequiredto
manually fill out Nutrition Labels.
Platform changes. At the platform level, enforcement must
combine static and dynamic validation. The submission pipeline
should incorporate automated cross-checks between Nutrition La-
bels, entitlements, and manifests, rejecting apps with inconsistent
disclosures. Nutrition Labels can be partially auto-generated from
bundle artifacts (e.g., SDK manifests) at build time, ensuring that
developer-supplied disclosures cannot fall below a verified base-
line. XcodeshouldpartiallyautofilltheNutritionLabelcomponent,
and interface with App Store Connect to ensure the presence of
baseline disclosures during submission. Finally, runtime enforce-
ment should be extended to detect undeclared access to protected
APIs. These measures must be integrated by Apple across deploy-
ment and runtime mechanisms to replace the current fragmented
model.
Unified Disclosure and Verification. Apple uses a combination
of property list declarations and user-enforced runtime permis-
sionstoregulateaccesstosensitivedata,whileotherprivacy-related
declarations(e.g.,nutritionlabels)remainunverified.Thisfragmented
approach creates opportunities for inconsistencies and omissions.
We provide an example that illustrates the problematic nature
of the current design: imagine a developer that wants to create an
app that can record videos. The app would need to use multiple
Native APIs in their code;AVCaptureSession begins an event dur-
ing which the user takes a picture. Since Apple considers access to
this functionality sensitive, the developer would need to request
the user for aruntime permission to access the camera via a differ-
ent object,AVCaptureDevice, whose propertyrequestAccess, is
used to trigger a system prompt that is displayed to the user. How-
ever,whenmacOSobservesthisAPIcall,itlooksforanentryinthe
Entitlements file, com.apple.security.device.camera, which is
a static declaration from the developer that the app will access the
camera. In the absence of this entitlement, the developer’s code )
will not prompt the user and hence will not receive device permis-
sions. Additionally, if the developer wants to list their app on the
AppStore,theyneedtocreatea privacy manifest file,andincludea
key, NSPrivacyCollectedDataTypePhotosorVideos, along with
details about how the data is used and handled by the app. While
the manifest entry does not affect runtime enforcement, it is used
by App Store reviewers to approve the app for listing. Finally, the
developer must also declare thePhotos & Videos type in the Nu-
trition Label, under the categoryUser Content , to inform users
thattheappaccessestheirphotosorvideos.Listing 1(AppendixE)
provides an example snippet of Swift code a developer might use
for this workflow.
The developer in this example creates redundant declarations,
eachofwhichusesdifferentterminology.Alternatively,Applecould
consolidatethesecomponentsintoasingledeclarationthatisused

CCS ’26, November 15–19, 2026, The Hague, Netherlands Jyotirmay Chauhan, Kostas Solomos, Mir Masood Ali, and Jason Polakis
for both enforcement and user disclosure. The developer could de-
clare in a single file that the app accesses the camera to record
videos, and this declaration would be used by the OS to enforce ac-
cessrestrictions,byAppStorereviewerstoapprovetheappforlist-
ing, and by users to understand the app’s data collection practices.
Considering Xcode’s existing capabilities to populate and consol-
idate entitlements and privacy manifest files, we propose that a
similar approach should consolidate all data access into a single
declaration. We provide an example declaration in AppendixE for
this specific example, illustrating our proposed unified approach.
This strategy would streamline the disclosure process for develop-
ers by eliminating redundancy, minimizing accidental omissions,
and enhancing the reliability of disclosures, while also facilitating
a platform-level automated verification process.
6 Discussion and Limitations
WhileNutriScanextensivelyevaluatestheruntimebehaviorofma-
cOSapps,itsanalysishasthefollowinglimitations.NutriScanuses
a custom UI-exercising tool to interact with apps, but these inter-
actions are not comprehensive, i.e., we do not evaluateall possi-
ble app states or user inputs. As such, our system may miss cer-
tain privacy-invasive behaviors and disclosure violations. More-
over,ouranalysisdependsontaxonomicalandfunctionaloverlaps
with Nutrition Labels which can only partially be addressed via
Entitlements and Runtime Permissions. Due to the nature of our
classification and the absence of platform documentation, a subset
ofAPIscouldnotbereliablyclassifiedintospecificlabelcategories.
Ourresults,therefore,offera lower bound ofdatacollection,which
may be even more extensive than what our study demonstrates.
Finally, NutriScan reports on observed data collection but cannot
determine the purpose or use of the collected data, nor can it iden-
tify backend handling practices (e.g., anonymization). These are
important for a complete assessment of app privacy, but can only
be performed in collaboration with app and SDK developers.
7 Related Work
Herewediscusspertinentpriorwork,focusingmainlyonresearch
addressing privacy labels, and desktop platforms.
Privacy Nutrition Labels. Kelley et al. [70] first proposed the
idea of creating a nutrition label for apps similar to the mandated
Food Nutrition labels governed by the FDA. A privacy nutrition
label was designed as a simple and universal disclosure that would
accurately indicate the app’s data collection practices. This would
allow a user to understand the data they were sharing and dictate
theirdecisionsaboutusinganapp.Theideagainedtraction,which
led Apple and subsequently Google to implement a version of this
nutrition label calling them App Nutrition Labels [25] and Data
Safety Labels [64], respectively. While initially introduced for iOS,
Apple recently rolled out Nutrition Labels for macOS and made it
mandatory for developers to include one for their desktop apps.
Subsequently, several dimensions of Nutrition Labels have been
studied, including usability from the end-user perspective [103],
developer challenges [75], and large-scale analyses [76].
Closer to our work are studies focusing on compliance. Ali et
al. [8] compared labels with privacy policies and found significant
divergences across iOS apps. Kollnig et al. [72] demonstrated that
iOSappsusedfingerprinting-derivedidentifiersfortracking,found
evidence of Apple engaging in tracking, and detected that discrep-
ancies were widespread in less popular apps, a finding also ver-
ified by our research. Arkalakis et al. [36] conducted a dynamic
analysis of Android apps to analyze their data collection practices.
That study also correlated apps’ dynamic behavior, including API
accesses and network traffic, with the apps’ Data Safety Section.
Their research uncovered a high degree of non-compliance with
the apps’ stated data disclosure policies. While that study follows
a similar methodology (albeit in a vastly different software ecosys-
tem), it focuses on apps’ dynamic behavior depending on users’
runtime consent. On the other hand, our research focuses on the
unique aspects of the macOS ecosystem, including identifying sys-
temresourcesthatarenotsufficientlytrackedthroughentitlements,
TCCandGatekeeper,yetcanbeleveragedbytrackersforuniquely
identifying users. Another relevant study [98] examined iOS apps’
compliancewiththeirNutritionLabelsusingdynamicanalysisand
network interception. Their dynamic analysis system, Lalaine, de-
tected67%ofappstobenon-compliantcomparedtoour85%.Their
findings are consistent with ours in identifying User ID, Device
ID and Location data as the most frequent non-compliant cate-
gories. NutriScan analyzes additional app and system level compo-
nents, including privacy manifests, entitlements, and fingerprint-
able identifiers, thus offering a more comprehensive assessment of
privacy violations.
Desktop Apps. Recent research on desktop apps has focused on
thesecuritypropertiesofcross-platformapps.Carettonideveloped
a static analysis tool, Electronegativity, that identifies potential se-
curity vulnerabilities in Electron apps [44]. Xiao et al. [97] found
concerningsecuritypracticesadoptedby640appswhenevaluated
with Electronegativity. They then developed a dynamic analysis
tooltoevaluateElectronappsandidentifysensitivedataflowsthat
can be exploited to perform Remote Code Execution (RCE) attacks.
Similarly, Ali et al. [9] proposed a dynamic analysis tool, Inspec-
tron, that runs apps against an instrumented Electron framework
and monitors their runtime behavior to identify potential secu-
rity vulnerabilities. Jin et al. [67] developed a framework that uses
a DOM-tree-based analysis to evaluate and identify unintended
modificationsinElectronapps.YangandYue[ 100]comparedtrack-
ing practices between mobile and desktop environments; however,
forthedesktopcomponentoftheirresearch,theystudiedwebsites
that offer a desktop version of their webpage, they did not study
dedicated desktop applications. Blochberger et al. [39] compared
the deployment and configuration of sandboxing within macOS
applications installed through Apple’s official store to that of ap-
plications retrieved from a third-party app store and found that
89% of apps distributed through the third-party app store did not
use sandboxing, thereby exposing users to risk.
Summary. To the best of our knowledge, no prior work has sys-
tematicallyinvestigatedhowtrackingandfingerprintingtechniques
are deployed within desktop apps. This lack of attention is no-
table given the research on tracking in web and mobile ecosys-
tems, leaving a gap in our understanding of privacy risks in desk-
top environments. By presenting the first empirical exploration
of privacy-invasive practices in a desktop platform, our study di-
rectly addresses this gap and helps complete the broader picture

Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem CCS ’26, November 15–19, 2026, The Hague, Netherlands
of online tracking across different platforms. In addition, we con-
duct the first systematic evaluation of macOS apps’ compliance
with their reported Privacy Nutrition Labels. This dual contribu-
tion allows us to assess not only the presence of tracking and fin-
gerprinting behaviors, but also the extent to which apps adhere
to their self-disclosed data practices. Taken together, our findings
provide a more comprehensive picture of the shortcomings and
challenges associated with both data access control mechanisms
and data practice disclosure frameworks in one of the most widely
used desktop operating systems.
8 Conclusion
Usershavebecomeconsiderablymoreaware,andconcerned,about
online tracking and other forms of privacy loss, and a rich body
of academic research has explored multiple dimensions of privacy
loss within the web, mobile, and smart device ecosystems. How-
ever, despite the continuing widespread use of desktops, no prior
research has explored how desktop apps can impact users’ privacy.
To address that gap, we conducted the first, to our knowledge, sys-
tematicevaluationofdatapracticesandviolationsbydesktopapps.
We focused on macOS, due to its general perception as a more se-
cure and private OS compared to Windows, as well as its recent
adoption of Privacy Nutrition Labels. To that end, we developed
NutriScan, an analysis framework and pipeline that consolidates
diverse data sources by statically analyzing app components and
dynamically instrumenting and exercising app. Using our system
we were able to detect privacy violations and disclosure discrepan-
cies across a wide selection of popular apps. Our in-depth analysis
of these violations, reveals that known tracking entities often sur-
reptitiously exfiltrate unique user and device identifiers that can
deanonymizeconcurrentprivatebrowsingsessions,andothersen-
sitive data that can be used to significantly enrich user’s profiles.
Our research calls for more streamlined nutrition-label creation
mechanisms, and improved vetting processes within Apple’s App
store,tomitigatethesignificantprivacyriskposedbymacOSapps.
Acknowledgments
We would like to thank the anonymous reviewers and shepherd
for their valuable feedback. This work was supported by the Na-
tional Science Foundation under grants CNS-2211574 and CNS-
2143363.Anyopinions,findings,conclusions,orrecommendations
expressed herein are those of the authors, and do not necessarily
reflect those of the NSF.
Ethical Considerations
We conducted this research with strict adherence to ethical guide-
lines, and upheld principles in accordance with the Menlo report.
Purpose and Impact of Research.Theprimarygoalofthiswork
is to understand the data collection practices of desktop applica-
tions and their resulting implications for the privacy ofend users.
We show that desktop environments provide rich data collection
capabilities, but offer few guidelines to assist app developers. Our
findings can inform the design of more effective privacy controls
and tools for desktop environments, as well as guide future re-
search in this space.
Beneficence.Ateverystepofthisresearchproject,weproactively
evaluated our findings and its impact on all stakeholders involved,
including Apple (especially, reviewers of apps on the App Store),
app developers, developers of third-party SDKs,andimportantly, end
users. We highlight their interactions with various studied compo-
nents in Table4 in the Appendix. Below, we outline the specific
considerations and impact on each stakeholder.
Apple. We gathered our dataset of apps from the official Apple
AppStore.Wefetchedindividualappbundlesandassociatedmeta-
data one at a time, ensuring that our requests did not overwhelm
the App Store infrastructure. Our work demonstrates shortcom-
ings in the App Store’s review process and highlights a need for
more comprehensive verification of submissions.
App Developers. All apps and associated metadata that we ana-
lyzed in this study are publicly available on the Apple App Store.
Our research highlights that developers are held responsible for a
large array of app components in their app, each of which have
partially overlapping semantics and share functional similarities
with each other. Our findings show that these components can re-
sult in inconsistent privacy practices, and can lead to developers
including conflicting privacy declarations for end users to view on
the App Store.
Third-party SDK Developers. Our analysis highlights the privacy
practicesofapps,withallincludedSDKs,asawhole.Werecognize
that developers of third-party SDKs have limited control over how
their SDKs are incorporated within apps, and that the SDKs’ data
collectionpracticescanvarybasedonfeaturesaccessedbytheapp
itself (i.e., corresponding Native API calls). We clarify in §2 that
the responsibility for accuracy of submissions lays with the app
developers, and point out that SDK developers can ease the pro-
cess by providing their own privacy manifest files. Our proposed
system can help SDK developers understand the real-world use of
their SDKs, and better support their clients (i.e., app developers)
through enhanced documentation and support with communicat-
ing privacy practices.
End Users.Theprivacyimplicationsofourworkprimarilyaffect
end users that download and use apps from the App Store. Our
findings show that end users that rely on the Privacy Nutrition
Labels on the App Store can be misinformed of an app’s actual be-
havior once downloaded. Our work aims to raise awareness about
these issues and provide insights into how apps collect and use
data, thereby empowering end users to make informed decisions
about their privacy.
Respect for persons. We note that our research does not directly
involve human subjects and informed consent procedures are not
applicabletoourresearch.Ourworkdoesnotcauseanyadditional
risk to end users, developers, or Apple itself. Our work informs
users,researchers,andregulatorstherebyimprovingtransparency
and accountability. The study relies exclusively on empirical mea-
surementofapplicationbehaviorandanalysisofpubliclyavailable
disclosures, without interacting with end users or collecting per-
sonal data. While our results may reflect negatively on certain ap-
plications or platform practices, we believe that responsible dis-
closure of measurement-based evidence serves the public inter-
est and aligns with established norms in security and privacy re-
search. Overall, the expected benefits of increasing awareness and
enabling better-informed decisions about privacy risks outweigh

CCS ’26, November 15–19, 2026, The Hague, Netherlands Jyotirmay Chauhan, Kostas Solomos, Mir Masood Ali, and Jason Polakis
any minimal potential downsides, justifying the ethical conduct of
this research.
Responsible Disclosure. Upon completion of our analysis, we
provided Apple a detailed description of our findings, including
a list of the apps with discrepancies in their data practice disclo-
sures. We have received notification that our reported issues were
reproduced and are currently being investigated.
Open Science
Topromotetransparencyandto facilitate futureresearch,wehave
made research artifacts available on Github [47].
References
[1] [n.d.]. DATAREPORTAL - Digital 2025: device trends for 2025.https://datare
portal.com/reports/digital-2025-sub-section-device-trends
[2] [n.d.]. Metal Overview. https://developer.apple.com/metal/
[3] 2024. Apple Platform Security.https://help.apple.com/pdf/security/en_US/ap
ple-platform-security-guide.pdf
[4] Letsgo Network Incorporated. 2011. LetsVPN MacOS Store.https://apps.apple
.com/us/app/letsvpn/id1481327306?mt=12.
[5] Gunes Acar, Marc Juarez, Nick Nikiforakis, Claudia Diaz, Seda Gürses, Frank
Piessens, and Bart Preneel. 2013. FPDetective: dusting the web for fingerprint-
ers. InProceedings of the 2013 ACM SIGSAC conference on Computer & commu-
nications security. 1129–1140.
[6] alexey-lysiuk. 2021. macos-sdk. https://github.com/alexey-lysiuk/macos-
sdk/tree/main/MacOSX10.15.sdk.
[7] Muhammad Ali, Angelica Goetzen, Alan Mislove, Elissa M Redmiles, and Piotr
Sapiezynski. 2023. Problematic advertising and its disparate exposure on Face-
book. In32nd USENIX Security Symposium (USENIX Security 23) . 5665–5682.
[8] Mir Masood Ali, David G. Balash, Monica Kodwani, Chris Kanich, and Adam J.
Aviv. 2024. Honesty is the Best Policy: On the Accuracy of Apple Privacy La-
bels Compared to Apps’ Privacy Policies. InProceedings on Privacy Enhancing
Technologies Symposium, Vol. 2024. Bristol, UK, 142–166.doi:10.56553/popets-
2024-0111
[9] Mir Masood Ali, Mohammad Ghasemisharif, Chris Kanich, and Jason Polakis.
2024. Rise of Inspectron: Automated Black-box Auditing of Cross-platform
Electron Apps. In33rd USENIX Security Symposium (USENIX Security 24) . 775–
792.
[10] Gianluca Anselmi, Yash Vekaria, Alexander D’Souza, Patricia Callejo,
AnnaMariaMandalari,andZubairShafiq.2024. WatchingTVwiththesecond-
party: a first look at automatic content recognition tracking in smart TVs. In
Proceedings of the 2024 ACM on Internet Measurement Conference . 622–634.
[11] Appfigures. 2025. Top Ranked Mac App Store Apps.https://appfigures.com/t
op-apps/mac-app-store/united-states/top-overall .
[12] Apple. 2025. CFNetwork.https://developer.apple.com/documentation/cfnetw
ork.
[13] Apple. 2025. Identify your MacBook Pro model - Apple Support.https://supp
ort.apple.com/en-us/108052.
[14] Apple. 2025. UIKit.https://developer.apple.com/documentation/uikit.
[15] Apple Developer. 2025. Disabling and Enabling System Integrity Protection.
https://developer.apple.com/documentation/security/disabling-and-enabling-
system-integrity-protection.
[16] AppleDeveloper.2025. Third-partySDKRequirements-Support:PrivacyMan-
ifests. https://developer.apple.com/support/third-party-SDK-requirements.
[17] Apple Developer Documentation. 2023. Required reason APIs.https://develo
per.apple.com/documentation/bundleresources/privacy_manifest_files/descr
ibing_use_of_required_reason_api.
[18] Apple Developer Documentation. 2023. Sandbox Exceptions.https://develope
r.apple.com/library/archive/documentation/Miscellaneous/Reference/Entitl
ementKeyReference/Chapters/AppSandboxTemporaryExceptionEntitlements.
html.
[19] apple developer documentation. 2026. nsuserdefaults.https://developer.apple.
com/documentation/foundation/userdefaults.
[20] Apple Inc. [n.d.]. PrivacyPreferencesPolicyControl. https://developer.apple.
com/documentation/devicemanagement/privacypreferencespolicycontrol.
[21] Apple Inc. 2020. App Privacy Details on the App Store.https://developer.appl
e.com/app-store/app-privacy-details.
[22] AppleInc.2024. DescribinguseofrequiredreasonAPI. https://developer.apple.
com/documentation/bundleresources/describing-use-of-required-reason-api .
[23] Apple Inc. 2024. Privacy updates for App Store submissions.https://develope
r.apple.com/news/?id=3d8a9yyh.
[24] Apple Inc. 2025. Adding a Privacy Manifest to Your App or Third-Party SDK.
https://developer.apple.com/documentation/bundleresources/privacy-
manifest-files.
[25] Apple Inc. 2025. App privacy details on the App Store.https://developer.appl
e.com/app-store/app-privacy-details/.
[26] Apple Inc. 2025. App Review Guidelines.https://developer.apple.com/app-
store/review/guidelines/.
[27] Apple Inc. 2025. App Sandbox.https://developer.apple.com/documentation/se
curity/app-sandbox.
[28] Apple Inc. 2025. App’s Sitemap.https://apps.apple.com/robots.txt.
[29] Apple Inc. 2025. Bundle: A representation of the code and resources stored in
a bundle directory on disk.https://developer.apple.com/documentation/foun
dation/bundle.
[30] Apple Inc. 2025. Entitlements.https://developer.apple.com/documentation/bu
ndleresources/entitlements.
[31] Apple Inc. 2025. Gatekeeper and runtime protection in macOS.https://suppor
t.apple.com/guide/security/gatekeeper-and-runtime-protection-sec5599b66df
/web.
[32] Apple Inc. 2025. Information Property List.https://developer.apple.com/docu
mentation/bundleresources/information-property-list.
[33] Apple Inc. 2025. Xcode.https://developer.apple.com/xcode/.
[34] Apple Inc. 2026. iTunes Search API.https://performance-partners.apple.com
/search-api.
[35] Apple WebKit Team. 2020. Tracking Prevention in WebKit.https://webkit.org
/tracking-prevention/.
[36] IoannisArkalakis,MichalisDiamantaris,SerafeimMoustakas,SotirisIoannidis,
Jason Polakis, and Panagiotis Ilia. 2024. Abandon All Hope Ye Who Enter Here:
A Dynamic, Longitudinal Investigation of Android’s Data Safety Section. In
33rd USENIX Security Symposium (USENIX Security 24) . 5645–5662.
[37] MuhammadAhmadBashir,SajjadArshad,WilliamRobertson,andChristoWil-
son.2016. TracingInformationFlowsBetweenAdExchangesUsingRetargeted
Ads. In 25th USENIX Security Symposium (USENIX Security 16) . USENIX Asso-
ciation, Austin, TX, 481–496.https://www.usenix.org/conference/usenixsecu
rity16/technical-sessions/presentation/bashir
[38] Muhammad Ahmad Bashir and Christo Wilson. 2018. Diffusion of User Track-
ing Data in the Online Advertising Ecosystem.Proceedings on Privacy Enhanc-
ing Technologies (PoPETS) 2018, 4 (July 2018).
[39] Maximilian Blochberger, Jakob Rieck, Christian Burkert, Tobias Mueller, and
HannesFederrath.2019. Stateofthesandbox:InvestigatingmacOSapplication
security. InProceedings of the 18th ACM Workshop on Privacy in the Electronic
Society. 150–161.
[40] Bram Bonné, Sai Teja Peddinti, Igor Bilogrevic, and Nina Taft. 2017. Exploring
decisionmaking with {Android’s}runtimepermission dialogs using in-context
surveys. InThirteenth Symposium on Usable Privacy and Security (SOUPS 2017) .
195–210.
[41] ReinhardtABotha,StevenMFurnell,andNathanLClarke.2009. Fromdesktop
to mobile: Examining the security experience. Computers & Security 28, 3-4
(2009), 130–137.
[42] JustinBrookman,PhoebeRouge,AaronAlva,andChristinaYeung.2017. Cross-
device tracking: Measurement and disclosures.Proceedings on Privacy Enhanc-
ing Technologies (2017).
[43] Bytedance Pte. Ltd. 2025. CapCut - video editor.https://apps.apple.com/us/ap
p/capcut-video-editor/id1500855883.
[44] LucaCarettoni.2017. Electronegativity-AStudyofElectronSecurity. Blackhat
(July 2017). https://infocondb.org/con/black-hat/black-hat-usa-2017/electro
negativity-a-study-of-electron-security
[45] Claude Castelluccia, Mohamed-Ali Kaafar, and Minh-Dung Tran. 2012. Be-
trayed by your ads! Reconstructing user profiles from targeted ads. InInter-
national symposium on privacy enhancing technologies symposium. Springer, 1–
17.
[46] Geoff Charles. 2024. What Is a Virtual Credit Card & How Do They Work?
https://ramp.com/blog/virtual-credit-card-guide
[47] Jyotirmay Chauhan. [n.d.]. NutriScan.https://github.com/jchauhn/Nutriscan-
CCS-26.
[48] Federal Trade Commission et al. 2017. Cross-Device Tracking: A Federal Trade
Commission Staff Report (2017). (2017).
[49] Aldo Cortesi, Maximilian Hils, and Thomas Kriechbaumer. 2025. mitmproxy -
an interactive HTTPS proxy.https://www.mitmproxy.org/.
[50] Rachel Cummings, Gabriel Kaptchuk, and Elissa M Redmiles. 2021. ” i need
a better description”: An investigation into user expectations for differential
privacy. In Proceedings of the 2021 ACM SIGSAC Conference on Computer and
Communications Security. 3037–3052.
[51] Savino Dambra, Iskander Sanchez-Rola, Leyla Bilge, and Davide Balzarotti.
2022. When Sally met trackers: Web tracking from the users’ perspective. In
31st USENIX Security Symposium (USENIX Security 22) . 2189–2206.
[52] Anupam Das, Nikita Borisov, and Matthew Caesar. 2016. Tracking Mobile Web
Users Through Motion Sensors: Attacks and Defenses.. InNDSS.
[53] Jessica Dawson. 2021. Microtargeting as information warfare.The Cyber De-
fense Review 6, 1 (2021), 63–80.

Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem CCS ’26, November 15–19, 2026, The Hague, Netherlands
[54] Alban Diquet. 2025. SSL Kill Switch 2.https://github.com/nabla-c0d3/ssl-kill-
switch2.
[55] DisconnectTrackerList.2022. CanonicalrepositoryfortheDisconnectservices
file. https://github.com/disconnectme/disconnect-tracking-protection/blob/
master/services.json.
[56] Steven Englehardt, Jeffrey Han, and Arvind Narayanan. 2018. I never signed
up for this! Privacy implications of email tracking. In Proceedings on Pri-
vacy Enhancing Technologies Symposium, Vol. 2018. Barcelona, Spain, 109–126.
doi:10.1515/popets-2018-0006
[57] Equity and Human Rights Commission. 2021. Protected characteristics.
https://www.equalityhumanrights.com/equality/equality-act-2010/protected-
characteristics.
[58] Exforsys. 2011. What is Monkey Testing – IT Training and Consulting – Ex-
forsys. https://www.exforsys.com/tutorials/testing-types/monkey-
testing.html
[59] Ayman Farahat and Michael C. Bailey. 2012. How effective is targeted adver-
tising?. In Proceedings of the 21st International Conference on World Wide Web
(WWW ’12).
[60] Firebase(Google). 2025. Firebase SDK for Apple App Development.https://gi
thub.com/firebase/firebase-ios-sdk.git.
[61] Frida. 2015. The Engineering behind Reverse Engineering.Open Source Devel-
opers’ Conference (OSDC) (Oct. 2015). https://frida.re/slides/osdc-2015-the-
engineering-behind-the-reverse-engineering.pdf
[62] Frida Project. [n.d.]. Frida. Dynamic instrumentation toolkit for developers,
reverse-engineers, and security researchers.https://github.com/frida/frida.
[63] Ghostery. 2025. TrackerDB.https://github.com/ghostery/trackerdb.
[64] Google LLC. 2022. Provide information for Google Play’s Data safety section.
https://support.google.com/googleplay/android-developer/answer/10787469?
hl=en.
[65] Google LLC. 2023. Privacy Sandbox.https://privacysandbox.com/.
[66] UmarIqbal,PounehNikkhahBahrami,RahmadiTrimananda,HaoCui,Alexan-
der Gamero-Garrido, Daniel J Dubois, David Choffnes, Athina Markopoulou,
Franziska Roesner, and Zubair Shafiq. 2023. Tracking, profiling, and ad target-
ing in the Alexa echo smart speaker ecosystem. InProceedings of the 2023 ACM
on Internet Measurement Conference. 569–583.
[67] Zihao Jin, Shuo Chen, Yang Chen, Haixin Duan, Jianjun Chen, and Jianping
Wu. 2023. A Security Study about Electron Applications and a Programming
Methodology to Tame DOM Functionalities. InNDSS.
[68] Jonathan Levin Morpheus. 2025. OSX iOS Entitlement Database.https://newo
sxbook.com/ent.php.
[69] KEEPSOLID INC. 2025. VPN Unlimited.https://apps.apple.com/us/app/vpn-
unlimited-for-mac/id727593140?mt=12.
[70] Patrick Gage Kelley, Joanna Bresee, Lorrie Faith Cranor, and Robert W. Reeder.
2009. A “Nutrition Label” for Privacy. InProceedings of the 5th Symposium on
Usable Privacy and Security (SOUPS ’09).AssociationforComputingMachinery,
New York, NY, USA, 1–12.doi:10.1145/1572532.1572538
[71] Konrad Kollnig, Pierre Dewitte, Max Van Kleek, Ge Wang, Daniel Omeiza, He-
lena Webb, and Nigel Shadbolt. 2021. A fait accompli? an empirical study into
theabsenceofconsentto {Third-Party}trackinginandroidapps.In Seventeenth
Symposium on Usable Privacy and Security (SOUPS 2021) . 181–196.
[72] Konrad Kollnig, Anastasia Shuba, Max Van Kleek, Reuben Binns, and Nigel
Shadbolt. 2022. Goodbye Tracking? Impact of IOS App Tracking Transparency
and Privacy Labels. In 2022 ACM Conference on Fairness, Accountability, and
Transparency(Seoul,RepublicofKorea) (FAccT ’22).AssociationforComputing
Machinery, New York, NY, USA, 508–520.doi:10.1145/3531146.3533116
[73] Pierre Laperdrix, Nataliia Bielova, Benoit Baudry, and Gildas Avoine. 2020.
Browser fingerprinting: A survey. ACM Transactions on the Web (TWEB) 14,
2 (2020), 1–33.
[74] Letsgo Network Incorporated. 2011. LetsVPN Privacy Policy.https://letsvpn.
world/privacy.
[75] Tianshi Li, Kayla Reiman, Yuvraj Agarwal, Lorrie Faith Cranor, and Jason I.
Hong. 2022. Understanding Challenges for Developers to Create Accurate
Privacy Nutrition Labels. In Proceedings of the 2022 CHI Conference on Hu-
man Factors in Computing Systems (New Orleans, LA, USA) (CHI ’22). Asso-
ciation for Computing Machinery, New York, NY, USA, Article 588, 24 pages.
doi:10.1145/3491102.3502012
[76] Yucheng Li, Deyuan Chen, Tianshi Li, Yuvraj Agarwal, Lorrie Faith Cranor,
and Jason I. Hong. 2022. Understanding iOS Privacy Nutrition Labels: An Ex-
ploratory Large-Scale Analysis of App Store Data. InExtended Abstracts of the
2022 CHI Conference on Human Factors in Computing Systems (New Orleans,
LA, USA)(CHI EA ’22). Association for Computing Machinery, New York, NY,
USA, Article 356, 7 pages.doi:10.1145/3491101.3519739
[77] Thomas Linden, Rishabh Khandelwal, Hamza Harkous, and Kassem Fawaz.
[n.d.]. The Privacy Policy Landscape After the GDPR.Proceedings on Privacy
Enhancing Technologies 2020 ([n.d.]).
[78] Juan Lopez, Leonardo Babun, Hidayet Aksu, and A. Selcuk Uluagac. 2017. A
SurveyonFunctionandSystemCallHookingApproaches. Journal of Hardware
and Systems Security 1, 2 (June 2017), 114–136.doi:10.1007/s41635-017-0013-2
[79] Francesco Marcantoni, Michalis Diamantaris, Sotiris Ioannidis, and Jason Po-
lakis. 2019. A Large-scale Study on the Risks of the HTML5 WebAPIfor Mobile
Sensor-based Attacks. In30th International World Wide Web Conference, WWW
’19. ACM.
[80] MozillaCorporation.2019. EnhancedTrackingProtectioninFirefox. https://su
pport.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop .
[81] Evan Neufeld. 2017. Cross-device and cross-channel identity measurement is-
sues and guidelines: How advertisers can maximize the impact of an identity-
based brand campaign.Journal of Advertising Research 57, 1 (2017), 109–118.
[82] ChangSeok Oh, Chris Kanich, Damon McCoy, and Paul Pearce. 2022. Cart-
ology: Intercepting Targeted Advertising via Ad Network Identity Entangle-
ment. In Proceedings of the 2022 ACM SIGSAC Conference on Computer and
Communications Security (Los Angeles, CA, USA) (CCS ’22). Association for
Computing Machinery, New York, NY, USA, 2401–2414.doi:10.1145/3548606.
3560641
[83] Angelisa C. Plane, Elissa M. Redmiles, Michelle L. Mazurek, and Michael Carl
Tschantz. 2017. Exploring User Perceptions of Discrimination in Online Tar-
geted Advertising. In 26th USENIX Security Symposium (USENIX Security 17) .
USENIX Association, Vancouver, BC, 935–951.https://www.usenix.org/confe
rence/usenixsecurity17/technical-sessions/presentation/plane
[84] Jingjing Ren, Martina Lindorfer, Daniel J Dubois, Ashwin Rao, David Choffnes,
and Narseo Vallina-Rodriguez. 2018. A longitudinal study of pii leaks across
android app versions. InNetwork and Distributed System Security Symposium
(NDSS), Vol. 10.
[85] Jingjing Ren, Ashwin Rao, Martina Lindorfer, Arnaud Legout, and David
Choffnes.2016. ReCon:RevealingandControllingPIILeaksinMobileNetwork
Traffic.In Proceedings of the 14th Annual International Conference on Mobile Sys-
tems, Applications, and Services (MobiSys ’16) .
[86] Franziska Roesner, Tadayoshi Kohno, Alexander Moshchuk, Bryan Parno, He-
len J Wang, and Crispin Cowan. 2012. User-driven access control: Rethinking
permission granting in modern operating systems. In2012 IEEE Symposium on
Security and Privacy. IEEE, 224–238.
[87] Asuman Senol, Gunes Acar, Mathias Humbert, and Frederik Zuiderveen Bor-
gesius. 2022. Leaky Forms: A Study of Email and Password Exfiltration Before
Form Submission. In 31st USENIX Security Symposium (USENIX Security 22) .
USENIX Association, Boston, MA, 1813–1830.https://www.usenix.org/confe
rence/usenixsecurity22/presentation/senol
[88] Till Speicher, Muhammad Ali, Giridhari Venkatadri, Filipe Nunes Ribeiro,
George Arvanitakis, Fabrício Benevenuto, Krishna P. Gummadi, Patrick
Loiseau, and Alan Mislove. 2018. Potential for Discrimination in Online Tar-
geted Advertising. InProceedings of the 1st Conference on Fairness, Accountabil-
ity and Transparency, Vol. 81.
[89] Chad Spensky, Jeffrey Stewart, Arkady Yerukhimovich, Richard Shay, Ari Tra-
chtenberg, Rick Housley, and Robert K Cunningham. 2016. Sok: Privacy on
mobile devices–it’s complicated.Proceedings on privacy enhancing technologies
(2016).
[90] MohammadTahaei,RubaAbu-Salma,andAwaisRashid.2023. Stuckintheper-
missions with you: Developer & end-user perspectives on app permissions &
theirprivacyramifications.In Proceedings of the 2023 CHI Conference on Human
Factors in Computing Systems. 1–24.
[91] Cem Topcuoglu, Andrea Martinez, Abbas Acar, Selcuk Uluagac, and Engin
Kirda. 2024. MacOS versus Microsoft Windows: A Study on the Cybersecurity
andPrivacyUserPerceptionofTwoPopularOperatingSystems.In Symposium
on Usable Security and Privacy (USEC) 2024 .
[92] Imdad Ullah, Roksana Boreli, and Salil S Kanhere. 2023. Privacy in targeted
advertising on mobile devices: a survey.International Journal of Information
Security 22, 3 (2023), 647–678.
[93] w0lfschild. 2025. macOS headers.https://github.com/w0lfschild/macOS_head
ers.
[94] Zhaohui Wang, Bo Luo, and Fengjun Li. 2025. PrivacyGuard: Exploring Hid-
den Cross-App Privacy Leakage Threats In IoT Apps.Proceedings on Privacy
Enhancing Technologies (2025).
[95] Primal Wijesekera, Arjun Baokar, Lynn Tsai, Joel Reardon, Serge Egelman,
David Wagner, and Konstantin Beznosov. 2017. The feasibility of dynamically
granted permissions: Aligning mobile privacy with user preferences. In2017
IEEE Symposium on Security and Privacy (SP) . IEEE, 1077–1093.
[96] Yuxi Wu, Panya Gupta, Miranda Wei, Yasemin Acar, Sascha Fahl, and Blase Ur.
[n.d.]. Your Secrets Are Safe: How Browsers’ Explanations Impact Misconcep-
tionsAboutPrivateBrowsingMode.In Proceedings of the 2018 World Wide Web
Conference (WWW ’18). 217–226.
[97] Feng Xiao, Zheng Yang, Joey Allen, Guangliang Yang, Grant Williams, and
WenkeLee.2022. Understandingand mitigatingremotecodeexecution vulner-
abilities in cross-platform ecosystem. InProceedings of the 2022 ACM SIGSAC
Conference on Computer and Communications Security . 2975–2988.
[98] Yue Xiao, Zhengyi Li, Yue Qin, Xiaolong Bai, Jiale Guan, Xiaojing Liao, and
Luyi Xing. 2023. Lalaine: measuring and characterizing non-compliance of
apple privacy labels. InProceedings of the 32nd USENIX Conference on Security
Symposium (Anaheim, CA, USA)(SEC ’23). USENIX Association, USA, Article

CCS ’26, November 15–19, 2026, The Hague, Netherlands Jyotirmay Chauhan, Kostas Solomos, Mir Masood Ali, and Jason Polakis
Figure 9: The Privacy Nutrition Label of CapCut.
62, 18 pages.
[99] Jun Yan, Ning Liu, Gang Wang, Wen Zhang, Yun Jiang, and Zheng Chen. 2009.
How much can behavioral targeting help online advertising?. InProceedings of
the 18th International Conference on World Wide Web (WWW ’09) .
[100] Zhiju Yang and Chuan Yue. 2020. A comparative measurement study of web
tracking on mobile and desktop environments.Proceedings on Privacy Enhanc-
ing Technologies 2020, 2 (2020).
[101] Eric Zeng, Tadayoshi Kohno, and Franziska Roesner. 2021. What makes a “bad”
ad? user perceptions of problematic online advertising. InProceedings of the
2021 CHI Conference on Human Factors in Computing Systems . 1–24.
[102] Desheng Zhang, Jianhui Zhang, Youjun Bu, Bo Chen, Chongxin Sun, and
Tianyu Wang. 2022. A Survey of Browser Fingerprint Research and Ap-
plication. Wireless Communications and Mobile Computing 2022, 1 (2022),
3363335. arXiv: https://onlinelibrary.wiley.com/doi/pdf/10.1155/2022/3363335
doi:10.1155/2022/3363335
[103] Shikun Zhang, Yuanyuan Feng, Yaxing Yao, Lorrie Faith Cranor, and Norman
Sadeh. 2022. How usable are ios app privacy labels?Proceedings on Privacy
Enhancing Technologies (2022).
[104] Sebastian Zimmeck, Jie S Li, Hyungtae Kim, Steven M Bellovin, and Tony Je-
bara.2017. Aprivacyanalysisofcross-devicetracking.In 26th USENIX Security
Symposium (USENIX Security 17). 1391–1408.
[105] Shoshana Zuboff. 2023. The age of surveillance capitalism. In Social theory
re-wired. Routledge, 203–213.
A Privacy Nutrition Example
Figure9illustratestheNutritionLabelofapopularvideoapp,Cap-
Cut [43]. The app declares the collection of device identifiers, user
content,andinteractiondata,andclassifiesthemas“LinkedtoYou”
or “Used to Track you”. While this separation increases disclosure
granularity, users face challenges interpreting such information
without familiarity with Apple’s labeling system, highlighting a
broaderlimitationofthislabellingapproach[ 103].However,while
a simpler label listing only the collected data items may be easier
to interpret, it might not accurately capture applications’ data col-
lection practices [76].
B macOS Privacy Mechanisms
Table 4 provides a taxonomy of macOS privacy components and
disclosure mechanisms, evaluated across four dimensions: (i) over-
lapintaxonomyandfunctionality,(ii)datacollectionandhandling
practices, (iii) tracking and fingerprinting surfaces, and (iv) access
and interaction by different entities (e.g., developers, reviewers,
users).
Privacy Labels are user-facing disclosures that report data collec-
tion categories and stated purposes. They rely on the same taxon-
omyasmanifestsandpermissions,sincedevelopersgeneratethem
based on bundle-defined components. During the app’s lifecycle,
theAppStoreverifiestheirpresencethroughinternalchecks,with-
outhowever,verifyingtheiraccuracy.Asouranalysisdemonstrated,
labels remain developer-declared rather than system-enforced or
validated. Even if they demonstrate the intended practices, they
provide no information about fingerprinting vectors or runtime
behavior.
Privacy Manifests are developer-supplied metadata files embed-
ded in macOS app bundles and SDKs. They adopt identical data-
type taxonomy as Nutrition Label and require structured declara-
tions of collected data, stated purposes, and externally accessed
trackingdomains(e.g., NSPrivacyTrackingDomains).Duringapp’s
submission, Apple’s review pipeline processes manifests to gener-
ate the corresponding Nutrition Labels. However, manifests are
solely developer-declarative, since they capture developer-stated
practices. Similar to Nutrition Labels they do not specify the appli-
cation’s tracking purposes or runtime functionality.
Entitlements are the primary access control mechanism on ma-
cOS. They are embedded in the app bundle’s.entitlements file
and define the system services and resources an application can
access (e.g., push notifications). Entitlements are enforced by ma-
cOS at runtime, controlling the app’s effective permissions during
execution.
Permissions are enforced by macOS at runtime when an applica-
tion requests access to protected resources such as the camera, mi-
crophone, or location. Permissions provide the interface through
which users must grant or deny access to sensitive components.
They are enforced at runtime and directly tied to application be-
havior once access is requested. By design, they do not provide
information about how resources are used once access has been
granted.
Native API Calls are used by applications to deliver their func-
tionality. They are widely accessible by both the application de-
veloper, and also the third-party SDKs. The APIs invoked during
runtime not only reflect the data uses declared by the application,
and also expose additional invocations that may be exploited for
tracking or other invasive practices. This runtime information can
only be obtained through dynamic analysis, which requires addi-
tional effort for execution monitoring and attribution.
Overall, each mechanism contributes a complementary view of
applicationbehavior,butnoneprovidesanaccuraterepresentation
of privacy practices. Moreover, there is no centralized validation
mechanism (e.g., the Mac App Store) to enforce consistency. Our
analysis demonstrates the fundamental limitations of the current
validation process, while our system performedend-to-end analy-
sis to detect inconsistencies in disclosure practices.
C NutriScan: Nutrition Label to Entitlement
mapping
Table 5 maps Nutrition Label categories to the entitlements and
APIs that provide access to the corresponding data. We note that
this information does not appear in Apple’s documentation and
was constructed from official references during our analysis. As
shown in §4, individual label categories correspond to diverse en-
titlementsandAPIs.Forexample, user id isreportedunderApple
account and Game Center entitlements and is accessible through
host and device APIs. Multiple categories, including advertising
data, performance data, and crash data, have no associated entitle-
mentandcanonlybeaccessedthroughAPIs.Thismappingdemon-
strates that the Nutrition Label taxonomy is technically grounded

Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem CCS ’26, November 15–19, 2026, The Hague, Netherlands
Table 4: Overview of privacy-relevant components studied in this work with insights into their relationships and attributes.
Overlap (| / F = complete/partial Taxonomy Overlap,Ū / x = complete/partial Functionality Overlap) shows the relationship
between components. Data Collection & Handling ( î = Data Linking or Anonymization, Ď = Purpose, ͜ = Data Types or
Categories) indicates the app’s data collection practices that can be gathered from analyzing the component. User Tracking
& Fingerprinting (Á = Apple’s pre-defined Sensitive APIs, ́ = Extended Fingerprinting) indicates the app’s privacy-invasive
practices that can be gathered from analyzing the component. Access & Interaction ( ̲ = Creation, ¬ = Verification, ¿ =
Observation) shows how each entity accesses the corresponding component.
Component
Overlap Data User Access & Interaction

ȷ ɚ Ù ĸ Collection Tracking & App SDK App Store End & Handling Fingerprinting Developer Developer Reviewer User

Privacy Label | Ū F x î Ď ͜ ̲ ¿ ¿
ȷ Privacy Manifest | Ū | Ū x x F x î Ď ͜ Á ̲ ̲ ¬
ɚ Entitlements x x | Ū F x F x ͜ Á ̲ ¬
Ù Permissions x x F x | Ū F x ͜ Á ̲ ¬ĸNative API Calls x x F Ū F Ū | Ū ͜ Á ́ ̲ ̲
var isAuthorized : Bool {
get async {
let status = AVCaptureDevice . authorizationStatus (
for : . video )
// Determine if the user previously authorized
camera access .
var isAuthorized = status == . a u t h o r i z e d
// If the system hasn 't determined the user 's
authorization status ,
// explicitly prompt them for approval .
i f status == . notDetermined {
isAuthorized = await AVCaptureDevice .
requestAccess ( for : . video )
} r e t u r n isAuthorized } }
func setUpCaptureSession () async {
// Check for camera authorization .
guard await isAuthorized e l s e { r e t u r n }
// Create the capture session .
let captureSession = AVCaptureSession ()
// Find the default video device .
guard let videoDevice = AVCaptureDevice . default ( for :
. video ) e l s e { r e t u r n }
do {
// Wrap the video device in a capture device input
.
let videoInput = try AVCaptureDeviceInput ( device :
videoDevice )
// If the input can be added , add it to the
session .
i f captureSession . canAddInput ( videoInput ) {
captureSession . addInput ( videoInput )
} } c a t c h {
// Configuration failed . Handle error . }}
Listing 1: Example Swift code to capture a video on macOS.
in concrete entitlements and APIs. However, the absence of corre-
sponding documentation and guidelines leads to developer confu-
sion, resulting in the Nutrition Label violations and discrepancies,
as our analysis demonstrated.
D Entitlement oriented Discrepancies
Table 6 expands Table1 (§4.1) with the entitlement-to-Nutrition
LabelmappingandtheNutritionLabeldatatypestheycorrespond
"Camera " : {
" Data Type " : { " Video " : true } ,
" Purpose " : { "App Functionality " : true } ,
" Handling " : { " Anonymization " : false } ,
" User Permission " : {
" Required " : true , " Status " : . notdetermined } ,
"API Access " : [
" AVCaptureSession " ,
" AVCaptureDevice " ,
" AVCaptureVideoDataOutput " ] }
Listing 2: Example unified declaration for camera access.
to. As our analysis highlights, multiple entitlements map to differ-
ent and diverse Nutrition Label categories. For example,appleac-
count.fullaccessmapstouseranddeviceidentifiers,contactde-
tails, communications, and payment information. The largest dis-
crepancies occur for Identifiers, Name and Contact Information,
Photos or Videos, Health, and Financial Information, which are
frequently omitted even though the entitlements indicate access.
Overall, this result demonstrates that the impact of discrepancies
is greater when entitlements map to multiple Nutrition Label cat-
egories are omited.
E Unified Privacy Declaration
InListing 1weincludeasnippetofexampleSwiftcodethatadevel-
oper may use to capture enable a user to capture video using the
device camera. The code checks for camera access authorization,
requests access if not determined, and sets up a capture session if
authorized, before creating a recording session.
Listing 2 demonstrates how how multiple fragmented disclo-
sures, that are currently spread across entitlements, privacy man-
ifests, and user-facing labels, can be merged into a single, unified
declaration.Adeveloper,mayspecifythedatatypecollected(video),
it’s purpose (functionality), the handling practice (no anonymiza-
tion) and other metadata about howAPIs are invoked. This unified
structure allows the same declaration to serve simultaneously for
OS-level enforcement, App Store review, and user transparency.

CCS ’26, November 15–19, 2026, The Hague, Netherlands Jyotirmay Chauhan, Kostas Solomos, Mir Masood Ali, and Jason Polakis
Table 5: Nutrition Label to Entitlement and API mapping
Label Entitlement API
user id accounts.appleaccount.fullaccess, developer.game-center,
developer.ubiquity-kvstore-identifier, developer.upi-device-
validation
gethostname, hostinfo, NSUserName, NSHomeDirectory, NSFileManager,
NSHost, IOBluetoothDevice, NSAppleScript, NSTask, UIDevice
email address accounts.appleaccount.fullaccess, developer.mail-client, mail ABCopyArrayOfAllPeople, ABGetSharedAddressBook, ABAddressBook,
CNContactSaveRequest, CNContactStore, NSAppleScript, CNContact-
FetchRequest
phone number accounts.appleaccount.fullaccess, private.contactsui ABCopyArrayOfAllPeople, ABGetSharedAddressBook, ABAddressBook,
CNContactSaveRequest, CNContactStore, EKEventStore, NSAppleScript,
CNContactFetchRequest
name accounts.appleaccount.fullaccess, private.contactsui, security.personal-information.addressbook,
security.temporary-exception.files.home-relative-path.read-
only
ABCopyArrayOfAllPeople, ABGetSharedAddressBook, NSUserName,
NSHomeDirectory, NSHost,
ABAddressBook, CNContactSaveRequest, CNContactStore, EKEventStore,
NSAppleScript, CNContactFetchRequest
physical address accounts.appleaccount.fullaccess, private.contactsui,
security.personal-information.addressbook
ABCopyArrayOfAllPeople, ABGetSharedAddressBook, ABAddressBook,
CNContactSaveRequest, CNContactStore, EKEventStore, NSAppleScript,
PKPaymentRequest, CNContactFetchRequest
other user content developer.contacts.notes, developer.ubiquity-container-
identifiers, developer.ubiquity-kvstore-identifier,
developer.user-management, security.files.downloads.read-
only, security.files.downloads.read-write, security.files.user-
selected.read-only, security.files.user-selected.read-write,
security.personal-information.calendars
LSSharedFileListCopySnapshot, EKEventStore, NSAppleScript
browsing history developer.web-browser LSSharedFileListCopySnapshot, NSAppleScript
device id accounts.appleaccount.fullaccess, developer.device-
information.user-assigned-device-name, security.temporary-
exception.files.home-relative-path.read-only
AudioDeviceID, DCDevice, AVCaptureDevice, CWInterface, NSAppleScript,
NSTask, UIDevice
precise location developer.location.push, security.personal-
information.location
CLLocationManager, LocationManagerDelegate, NSAppleScript
coarse location developer.location.push, devel-
oper.networking.networkextension, security.personal-
information.location
CLLocationManager, LocationManagerDelegate, NSUserDefaults, NSTime-
Zone, NSAppleScript
payment info accounts.appleaccount.fullaccess, developer.financekit,
developer.in-app-payments
PKPaymentRecurringRequest, PKPayment, SKMutablePayment, NSApple-
Script, PKPaymentRequest
credit info
accounts.appleaccount.fullaccess
PKPaymentRecurringRequest, PKPayment, SKMutablePayment, NSApple-
Script, PKPaymentRequest
emails or text messages accounts.appleaccount.fullaccess, developer.mail-client, mail MEMessage, MSConversation, MEMessageState, NSAppleScript
performance data MXCellularConditionMetric, MXCPUMetrics, MXGPUMetrics, NSApple-
Script, MXAppLaunchDiagnostic, MXAppExitMetric, MXNetworkTransfer-
Metric, MXCPUExceptionDiagnostic, MXDiskIOMetric, MXMemoryMetric,
MXDisplayMetric
advertising data ASIdentifierManager, NSAppleScript, SKAdNetwork
photos or videos security.assets.pictures.read-only,security.assets.pictures.read-
write, security.device.camera, security.personal-
information.photos-library
AVCaptureSession, NSAppleScript, PHFetchResultChangeDetails, PH-
FetchResult
audio data security.device.audio-input, security.device.microphone AVCaptureSession, NSAppleScript, PHFetchResultChangeDetails, PH-
FetchResult
purchase history developer.in-app-payments NSAppleScript
product interaction NSAppleScript
crash data NSAppleScript, MXAppLaunchDiagnostic, MXAppExitMetric, MXCPUEx-
ceptionDiagnostic, MXDiskIOMetric, MXMemoryMetric, MXDisplayMetric
customer support NSAppleScript
other financial info developer.financekit NSAppleScript
gameplay content NSAppleScript
sensitive info developer.healthkit.access, developer.healthkit NSAppleScript

Exploring Privacy Leakage and Data Disclosure Violations in the MacOS Application Ecosystem CCS ’26, November 15–19, 2026, The Hague, Netherlands
Table 6: Distribution of apps with discrepancies between declared entitlements and corresponding Nutrition Label data types.
Entitlement # TotalApp (%) # TopApp (%) # Rand.App (%) Label Data Type
com.apple.security
files.user-selected.read-only 95% 94.1% 95.7% Other User Content
personal-information.location 93.6% 93.8% 93.4% Precise Location, Coarse Location
personal-information.addressbook 93.8% 93.9% 92.8% Name, Physical Address
files.downloads.read-write 92.3% 93.8% 89.6% Other User Content
personal-information.photos-library 90.8% 90% 92.1% Photos or Videos
files.downloads.read-only 88.8% 66.6% 100% Other User Content
files.user-selected.read-write 90.7% 87.7% 94.5% Other User Content
device.microphone 89.4% 88.2% 90.4% Audio Data
assets.pictures.read-write 87.1% 89.4% 83.3% Photos or Videos
personal-information.calendars 86.6% 84.7% 92.3% Other User Content
device.audio-input 86.1% 87.6% 84.5% Audio Data
device.camera 84.5% 84.5% 84.4% Photos or Videos
assets.pictures.read-only 80.9% 75% 100% Photos or Videos
temporary-exception.files.home-
relative-path.read-only
68.7% 61.5% 100% Device ID, Name
com.apple.developer
healthkit 100% 100% 100% Health, Sensitive Info
healthkit.access 100% 100% 100% Health, Sensitive Info
ubiquity-kvstore-identifier 93.6% 90.5% 100% Other User Content
networking.networkextension 90.3% 89.4% 91.6% Coarse Location
ubiquity-container-identifiers 90.7% 87.1% 97.3% Other User Content
in-app-payments 66.6% 50% 100% Payment Info, Purchase History
game-center 65% 66.6% 64% User ID
financekit 50% 50% N.A. Payment Info, Other Financial Info
com.apple
mail 100% 100% 100% Email Address, Emails or Text Mes-
sages
accounts.appleaccount.fullaccess 100% N.A. 100% User ID, Device ID, Phone Number,
Name,PhysicalAddress,EmailsorText
Messages, Payment Info, Credit Info,
Health, Fitness
