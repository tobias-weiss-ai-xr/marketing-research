---
title: 'SideKernel: A Usable microVM Sandbox for AI Coding Agents on macOS'
url: https://arxiv.org/abs/2610.02456
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Dimitrios Prasakis
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.02456
pages: 17
chars: 67700
fetched_at: '2026-11-08T13:24:25+00:00'
kb_version: 1
---

# SideKernel: A Usable microVM Sandbox for AI Coding Agents on macOS

SideKernel: A Usable microVM Sandbox for AI
Coding Agents on macOS
Dimitrios Prasakis
Georgia Institute of Technology
dimitrios.prasakis@gatech.edu
Abstract—AI coding agents are untrusted system components,
yet they require autonomy on the developer machines they run
on. This contradiction is a security problem. Sandboxes provide
an isolated environment, but for local macOS development, the
existing local, open-source options for AI coding agents are few
in number and cumbersome to use. I conducted a formative
online user survey which indicates that fewer than 40% of AI
coding agent users run their agents in a sandbox and identifies
the top usability barriers hindering AI coding agent sandbox
adoption. These findings are used to develop SideKernel: an open-
source, local, microVM-based macOS sandbox for AI coding
agents designed for usability. To evaluate SideKernel, I compiled
a list of sandboxes available on the market and filtered it
against five inclusion criteria. Then I performed a comparative
analysis between SideKernel and the sandboxes that satisfy these
criteria, across 23 capability tests derived from the usability
barriers revealed by the user survey. I discovered that only a
few sandboxes are similar to SideKernel, and that among those,
Docker Sandboxes and SideKernel score highest on capability
features related to usability. A secondary contribution of this
paper is a survey of the existing solution space for local, open-
source, microVM-based macOS sandboxes for AI coding agents.
Index Terms—AI agents, macOS, microVM, sandboxing, us-
able security.
I. INTRODUCTION
A. Motivation
AI agents are untrusted system components, and running
untrusted system components in a sandbox is a recommended
practice in systems security [1]. Over the past year 1, the
cybersecurity market has seen rapid development of AI agent
sandboxes [2–23]—many of which have gained popularity
but, anecdotally, see limited adoption with the majority of
AI coding agent users not running a sandbox (Section V).
The implication of this finding is that most users run AI
coding agents on their machines, with all the security risks
that this implies. For example, AI agents are vulnerable to
prompt injection attacks, tool misuse leading to remote code
execution, data exfiltration, and the installation of malware
through hallucinated package names [24, 25].
B. Isolation Primitives
The isolation primitives of sandboxes can be broadly clas-
sified based on where the security boundary lives [26]:
1Approximated from the date of the first public commit of most sandboxes
listed in Table I.
1)OS-isolation (Shared Kernel):Isolation primitives that
share the host’s kernel. For example, Linux Contain-
ers, bubblewrap (namespaces & cgroups), or kernel-
enforced security controls such as Linux Landlock, macOS
Seatbelt/sandbox-exec, and others.
2)Language-Specific Isolation:Isolation primitives where
the boundary lives inside a managed runtime provided
by the language. Examples include W ASM runtimes,
Chromium’s site isolation, and the JVM.
3)Virtualization (Separate Kernel):Each workload runs on
its own dedicated kernel, whether a full virtual machine
such as QEMU/KVM, VirtualBox, or Parallels, a unikernel
[27] or a microVM (i.e., a stripped-down guest running
a minimal Linux kernel) such as Firecracker or Kata
Containers.
C. Scope
Many of the AI coding agent sandboxes on the market use
isolation primitives that rely on a shared kernel. Container-
based isolation is weaker than microVM isolation [26]. This
claim is, however, not trivial to establish for other primitives
such as macOS Seatbelt, which on the one hand is a shared
kernel isolation primitive, but on the other hand is policy-
based and enforced at the kernel level. The right question to
ask is: under which threat model do I evaluate the security of
the two? This is a research question that deserves a study of
its own, and is out of scope for this paper. However, I state
in Section II-B the threat model under which SideKernel is
designed.
Moreover, security depends not only on the theoretical
guarantees of a technology, but also on the actual implemen-
tation of it. In this paper, I focus exclusively on microVM
sandboxes. The security argument is architectural: the host’s
kernel is not reachable, as the untrusted agent interacts with a
stripped-down microVM Linux kernel whose attack surface is
by definition reduced. A malicious agent or adversary would
have to escape the virtual machine monitor (VMM) to land
on the host. This is the isolation primitive that many cloud
providers use for untrusted code. For example, AWS uses
Firecracker microVMs for Lambda and Fargate [26], as do
the major commercial hosted AI agent sandboxing platforms
such as E2B and Vercel Sandbox [13, 28].
arXiv:2610.02456v1  [cs.CR]  1 Oct 2026

D. Research Question and Contributions
This paper addresses the following research question:
Which usability barriers hinder macOS developers’
adoption of AI coding agent sandboxes?
In order to answer this question, this paper makes three
contributions:
1)SideKernel:An implementation of a local, microVM-
based macOS sandbox for AI coding agents. SideKernel’s
core thesis is usable security: a sandbox that is secure, easy
to use, and built exclusively for AI coding agents.
2)An empirical account of sandbox usability issues:
Informal formative research via an online user Google
survey that hints at theUSABILITY BARRIERSthat AI
coding agent users face when using similar sandboxes.
This is a secondary contribution of this paper that ties to
the development of SideKernel; however, this study should
not be treated as statistically generalizable, but rather as an
informal signal. More on this in Section IX.
3)A comparative analysis of the existing sandbox market:
Summative research via a comparative analysis of SideK-
ernel against a list of similar sandboxing solutions on the
market. This is a secondary contribution of this paper that
discovers sandboxes similar to SideKernel and compares
them.
II. BACKGROUND
A. Terminal-Based vs. Programmatic AI Agents
AI coding agents are typically executed in the terminal
and require continuous human interaction. Examples include
Claude Code [29], Codex [30], and others. Programmable
software development kit (SDK) agents are typically executed
on a server, and require little to no human interaction. They
are programs interacting with MCP servers [31] or directly
with the application programming interfaces of LLM providers
or local models through their official SDKs. This distinction
matters because this paper is concerned only with AI coding
agents and their related sandboxes.
B. Threat Model
AI coding agents are untrusted system components and
they are executed directly on the host’s terminal. Therefore,
SideKernel’s threat model treats the agent itself as the adver-
sary. For example, an agent might be prompt-injected from
external sources, directly or indirectly, or might hallucinate
dangerously during its own inference. The reason the agent
turns hostile is immaterial to the threat model: the model
treats the threat actor as fully privileged (inside the sandbox)
regardless of cause.
To better study the attack surface of AI agents in the context
of sandboxing, I define two security boundaries, depicted in
Fig. 1:
Figure 1. North & South Security Boundaries
1) NORTHBOUNDARY: The north boundary encompasses
all communications that the agent inside the sandbox con-
ducts with machines other than the host or localhost. This
includes the internet, or other hosts in the same or external
networks. I refer to the communication channel from
the sandbox to the north boundary as NORTHBOUND
CHANNEL.
2) SOUTHBOUNDARY: The south boundary includes all
communications that the sandbox performs with the host.
Depending on the exact implementation of the sandbox,
that could be over virtual sockets, or networking protocols
such as SSH. I refer to the communication channel from
the sandbox to the host boundary as SOUTHBOUND
CHANNEL.
In this context, the south boundary exists toprotect the host
from malicious actions, for example installing malware, or
deleting or editing valuable files. The threat is unidirectional:
from the sandbox towards the host. The north boundary, in
turn,protects the datathat is mounted inside the sandbox
from exfiltration, for example a malicious agent sending all
the mounted data to an external source. It is equally concerned
withprotecting external entities from a local malicious
agent. In this context, the threat is bidirectional (from the
sandbox to the north boundary and vice versa).
A notable example is OpenAI’s autonomous AI agent sys-
tem inadvertently hacking Hugging Face through a sandbox
escape [32]. That very example, however, also shows the
complexity of the enterprise of sandboxing powerful agents.
OpenAI’s agent bypassed northbound security controls by dis-

covering and exploiting a chain of vulnerabilities to eventually
escape the sandbox and local networks and reach the internet.
The security controls of SideKernel address both bound-
aries, though not equally.
1) South Boundary Threat Model:On the south boundary,
the goal is protecting thehost’s runtimeand itsnon-mounted
filesystemfrom adversarial agents running inside the sandbox.
2) North Boundary Threat Model:On the north boundary,
the goal is preventingexfiltration of sandbox datato the
internet (or other external networks/endpoints), as well as
using the sandbox as alaunch pointfor outbound offensive
operations by a malicious agent.
III. RELATEDWORK
A. Existing Sandboxes
The current sandboxing market is dominated by sandboxes
that rely on OS-isolation or language-specific isolation. This
includes the native sandboxes of major frontier-model compa-
nies, for example, Claude Code [33], Codex [34], Gemini [35],
and Grok Build [36]—as well as well-known open-source tools
that depend on Seatbelt and Landlock, such as Nono [2], Agent
Safehouse [5], and more [8, 9, 11, 12].
Others use hardware-virtualized microVMs, but they are
SaaS products with no local deployment, indicatively E2B [13]
and Daytona [7]; are not open-source [22]; are general VM
runtimes rather than purpose-built agent sandboxes [37–39];
focus primarily on computer use [17]; or target mainly
programmable SDK agents or MCP gateways rather than
terminal-based coding agents [14, 20].
To the best of my knowledge, SmolVM [18], Microsand-
box [14], Shuru [15], and VibeBox [16] are the only open-
source, local, purpose-built for terminal-based AI coding
agents, hardware-virtualized with microVMs, and macOS-
native sandboxes on the market. I refer to these five properties
as theINCLUSION CRITERIA(IR-1–IR-5) and define and
discuss their importance in Section IV-B.
This is not an exhaustive survey of all the sandboxes on the
market. Rather, it aims to present an overview of the different
types of sandboxes that exist, but more importantly identify a
complete list of all the sandboxes similar 2 to SideKernel.
IV. METHODOLOGY
SideKernel’s prototype implementation is informed by two
studies:
1) Auser survey (formative research)[40, Ch. 3.1.1] con-
ducted prior to the development of SideKernel (complete
instrument in Table IX). The purpose of this formative
online user survey is twofold:
a) to inform the implementation of SideKernel
b) to motivate a comparative analysis of SideKernel
against other sandboxes on the market.
2) Acomparative analysis (summative research)[40,
Ch. 3.1.2] benchmarking the final SideKernel prototype
2What constitutes a similar sandbox is discussed in detail in Section IV-B.
Figure 2. SideKernel research methodology.
against other market sandboxes that satisfy a set of
inclusion criteria (Table I and Fig. 3). The analysis is run
on a set of well-defined capability tests (Section VII),
grounded on the usability signals of the user survey.
The depiction of the methodology for developing SideKer-
nel is shown in Fig. 2, where a feedback loop between the
results of the comparative-analysis and the continuous devel-
opment of SideKernel ensures that the software is constantly
improved, by addressing the findings and adding new tests.
The goal of this methodology is to allow me to evaluate and
improve SideKernel continuously.
A. User Survey Methodology
The user survey takes the form of an online Google Survey
that uses a mix of multiple-choice, multi-select, and free-text
questions, gathering empirical evidence from sandbox users
on whatUSABILITY BARRIERSthey faced while using similar
sandboxes.
The user survey is structured in three steps. First, filtering
out users that have never used an AI coding agent. Second,
categorizing the remaining users based on whether they are
current or former sandbox users. Third, through multiple-
choice, multi-select, and free-text questions, I gathered evi-
dence on what usability barriers they faced while using those
sandboxes.
Respondents were gathered via direct and targeted recruiting
[41, Ch. 2] specifically through my direct professional net-
work, Zurich’s JFloor startup community 3 and Georgia Tech’s
practicum course (CS-6727) online forum and user group &
3https://thejfloor.com/

Figure 3. Filtering process against inclusion criteria.
Georgia Tech’s Slack channels. It is important to note that this
is an informal Google Survey. I treat the results as anecdotal
signals rather than statistically generalizable results.
B. Comparative Analysis Methodology
The goal of the comparative analysis is to examine how well
the final SideKernel prototype addresses the usability barriers
identified from the user study relative to other sandboxes
currently on the market.
The comparative analysis begins with the compilation of a
list of all existing sandboxes that are similar to SideKernel. To
define what similarity means, I defined a set ofINCLUSION
CRITERIAthat I filter the list against. These are the following:
1) OPEN-SOURCE: The sandbox must be free to use, and
either open-source or source-available, to foster trust
through a publicly inspectable codebase.
2) LOCAL: The sandbox must execute in the user’s own
machine, rather than in a remote execution environment
such as a cloud or a virtual private server (VPS).
3) INTERACTIVE SHELL: The sandbox must provide an
interactive shell (e.g., bash) intended for operating CLI
coding agents such as Claude, Codex etc. This excludes
sandboxes thatonlyprovide SDK interfaces or computer-
use interfaces (GUI) for AI agents.
4) HARDWARE-VIRTUALIZATION(MICROVM): The sand-
box must use hardware virtualization as its isolation
boundary, and provide this virtualization performantly
through a stripped down kernel (microVM or unikernels).
This excludes platforms intended for full VM virtual-
ization, as performance is not a named but an implied
requirement.
5)MACOS SUPPORT: The sandbox must be able to run on
a macOS ARM machine.
Sandboxes that meet inclusion criteria two to five are
included in the comparative study. I did not filter on open-
source, because I did not want to exclude the major player,
Docker Sandboxes.
C. Deriving Tests from the Usability Barriers
The user survey, however, gives little information about the
detailed tests for each barrier. For example, the user study
suggests that sharing files between the host and the sandbox
is something users find cumbersome. But what exactly does
this mean? To the best of my knowledge, there is no prior
literature that studies these attributes in any greater detail for
sandboxes, beyond this study.
The selection of the tests for each usability barrier is done
so that as many possibilities as possible are covered—while
making reasonable assumptions. For example, in file sharing
(UB-1), I noticed that mounting is common across sandboxes,
but file sharing overSFTPorSSHis not; hence I created tech-
nical tests around mounting. Indicatively, assessing whether
CRUD operations work bidirectionally, if file-bit flags (r, w,
x) transfer, and more. Another example is image clipboard
sharing, a feature supported by coding agents such as Claude.
The multi-select and multiple-choice answers are then
grouped by frequency to identify the top usability barriers. For
example the answers “Initial installation / setup is too hard”
and “Had to set everything up from scratch (dotfiles, shell,
tools, logins)” are merged into one category “Environment
provisioning & Setup”.
The comparative analysis provides an overview of specific
usability capabilities within the confines of the tested usability
barriers, rather than a generalizable statement about which
sandbox is more useful.
D. Benchmark Construction
Each task is aCAPABILITY TESTwith a binary outcome,
testing whether an action related to a specific usability barrier
is feasible in a given sandbox. Success criteria for every ca-
pability test are fixed before the comparative analysis iteration
(evaluation) begins [40, §4.1].
A test passes if and only if the sandbox provides aBUILT-
IN MECHANISMfor the task. By built-in mechanism I refer to
a documented feature of the sandbox itself: one discoverable
through the tool’s official documentation or its own interface.
A test fails if the task is infeasible, or feasible only by working
around the sandbox—for example blocking network access to
a sandbox by explicitly and manually blocking the sandbox’s
networking on a host’s firewall. More specifically, the binary
outcomes of the capability tests are defined as follows:
•✓= a built-in mechanism for the task exists
•✗= no built-in mechanism exists
This evaluation rule is deliberately generous, and deliber-
ately blind to how easy or hard the built-in mechanism is to
use. Because I am both the tester and developer of SideKernel,
I had to find ways to reduce bias in my evaluation as much
as possible. One way to do this is to have a standardized
methodology to test the sandboxes. Had I also scored on
perceived effort, then every cell would encode a subjective
judgment of my own, and the comparison would not be

Table I
INCLUSION REQUIREMENTS AND ISOLATION CLASSIFICATION. IR-1:OPEN-SOURCE; IR-2:LOCAL EXECUTION; IR-3:INTERACTIVE SHELL FORCLI
AGENTS; IR-4:HARDWARE-VIRTUALIZED; IR-5:MACOS
Inclusion requirements Isolation
Sandbox IR-1 Source IR-2 Local IR-3 Shell IR-4 HW-virt. IR-5 macOS Isolation Mechanism(s) Class
nono✓ ✓ ✓ ✗ ✓ Seatbelt / Landlock Shared Kernel
Landrun ✓ ✓ ✓ ✗ ✗ Landlock Shared Kernel
Fence✓ ✓ ✓ ✗ ✓ Seatbelt / bubblewrap Shared Kernel
Daytona ✓a ✗ n/ab n/ab n/ab Shared Kernel / microVM Cont. / Sep. kernel
Yolobox✓ ✓ ✓ ✗ ✗ c Docker/Podman container Shared Kernel
AIO ✓ ✓ ✗ ✗ ✗c Docker container Shared Kernel
Deno✗ ✗n/a b n/ab n/ab microVM Sep. kernel
Capsule ✓ ✓ ✗ ✗ ✓ W ASM Runtime
pctx✓ ✓ ✗ ✗ ✓ Deno/V8 isolate; Podman Runtime / Cont.
E2B ✓ ✗ n/ab n/ab n/ab microVM Sep. kernel
Microsandbox✓ ✓ ✓ ✓ ✓ microVM Sep. kernel
Shuru ✓ ✓ ✓ ✓ ✓ microVM Sep. kernel
VibeBox✓ ✓ ✓ ✓ ✓ microVM Sep. kernel
CUA ✓ ✓ ✗d ✓ ✓ VM Sep. kernel
SmolVM✓ ✓ ✓ ✓ ✓ microVM Sep. kernel
Sprites ✗ ✗ n/ab n/ab n/ab microVM Sep. kernel
Arrakis✓ ✓ ✓ ✓ ✗ microVM Sep. kernel
OpenSandbox ✓ ✓ ✗ ✓e ✗c Container (opt. MicroVM) Shared Kernel
Docker Sbx✗ ✓ ✓ ✓ ✓ microVM Sep. kernel
CodeRunner ✓ ✓ ✗f ✓ ✓ microVM Sep. kernel
Agent Safehouse✓ ✓ ✓ ✗ ✓ Seatbelt Shared kernel
SideKernel ✓ ✓ ✓ ✓ ✓ microVM Sep. kernel
a Since June 2026, Daytona moved into private repositories.
b Not applicable: the sandbox executes on remote infrastructure rather than on the user’s machine (fails IR-2), so the remaining requirements, which concern
the local macOS execution environment, are not evaluated.
c Installable on macOS, but the sandbox does not virtualize natively: it executes only inside a Linux VM supplied by Docker Desktop, Colima, or Podman
machine.
d CUA is built for computer use. It is heavy (boots full macOS VMs) and has a different purpose (GUI, computer use) than SideKernel.
e Evaluated in its default configuration (shared host kernel).
f No native shell subcommand; interactive access uses the apple/container substrate.
reproducible by a reader. Restricting the binary outcome to
built-in capabilities makes the scores objective and auditable.
A valid counterargument to this methodology is that this
capability binary scoring measures exactly that: capability, not
usability. While this statement is true, there is a nuance: these
capabilities are sourced from the user study which identifies
which usability barriers hinder sandbox adoption.Therefore
they are capabilities related to usability barriers.
But this alone is not sufficient to demonstrate usability on
its own. Just because a sandbox has built-in capabilities to
perform some actions—even when those actions are related to
solving usability barriers—it does not mean that this built-in
mechanism is intuitive and frictionless. To counter this trans-
parently, I therefore recordfriction notesalongside the binary
outcomes. Friction notes never change a binary outcome. They
are reported per barrier in Section VII and carry the qualitative
descriptions that the binary outcome cannot, thus allowing the
reader to make a judgment of their own.
The sum of a sandbox’s binary outcomes forms itscapa-
bility score. It is a naive, unweighted sum in which every test
counts equally, although in practice not every task is equally
consequential. It is a signal rather than a definitive measure,
and it should be read together with the friction notes rather
than on its own.
E. Evaluation Protocol
In order to make the comparison standard and as thorough
as possible, I create a template directory that contains the
following structure and files:
sandbox-test-template/
|-- external-file.txt # host only file
|-- big-file.txt # 10 GB file
‘-- mount/ # mounted dir
|-- requirements.txt # contains numpy
|-- workspace-file.txt # CRUD, symlink
‘-- shell.sh # no exec-bit

This directory is deployed fresh for each new sandbox
evaluation.
These tests are extensive, but not exhaustive—and should
not be read as such. They are, however, a reasonable and
transparent indicator of how capable and usable different
sandboxes are in relation to the barriers the user survey
uncovered.
Another important aspect of this evaluation methodology
is that the iterative approach of SideKernel’s development
(Fig. 2) allows me to continuously create new tests or amend
existing ones while improving the product at the same time.
V. USERSURVEYRESULTS
A. Google Survey Report Analysis
Below I present the most frequently mentioned user survey
results that shaped my decisions on the development of the
prototype of SideKernel, as well as its evaluation. The com-
plete instrument and responses are reported in Appendix B.
The free-text responses are only analyzed and reported in
aggregate in this section.
•The Google survey gathered a total of 80 respondents.
•Out of the 80 respondents, 68 use AI coding agents (85%).
Respondents who do not use AI coding agents are filtered
out and not considered for the following results.
•60.3% of AI coding agent users are macOS users.
•Out of the 68 AI coding agent users, 86.8% use Claude
Code (59 respondents), 38.2% use Codex (26 respondents),
and 33.8% use Microsoft’s Copilot in agent mode (23
respondents). Cursor (19.1%, 13 respondents) and Gemini
CLI (14.7%, 10 respondents) follow, while every remaining
agent sits at or below 2.9%, making them individually
insignificant for the scope of SideKernel.
•Only 38.2% (26 users) of respondents are current sandbox
users, while 10.3% (7 users) are former sandbox users and
51.5% (35 users) have never used a sandbox.
•From the current sandbox users (26 in total), 34.6% (9
users) wrote that they face no significant difficulties.
•From the former and current sandbox users (33 in total), 8
wrote that getting ports / localhost / networking to work is
difficult, and that having to set everything up from scratch
(e.g., dotfiles, shell, tools, logins) is also difficult; 7 wrote
that sharing files between the sandbox and the host is hard
or slow. They are followed by 5 users noting that multi-
sandbox management is confusing and that initial setup
and installation was confusing.
•Notably, among the non-sandbox users, 60% answered that
they have never considered it and 25.7% that the security
benefit of using a sandbox did not seem worth the effort
for their use case.
The sample is highly technical, with one third working in
security and the vast majority being engineers. The dominance
Figure 4. Usability barriers reported by current and former sandbox users
(n= 33).
of Claude Code helped me scope down my practicum and
focus only on Claude Code. The count of 33 former and
current users is the group of interest for this study.
The free-text responses of current and former users around
what features or improvements an ideal sandboxing solution
would offer compared to their current or past setups focus
on a few main points. In aggregate users ask for ease of use
and “nearly invisible” sandboxes that require minimum effort
to manage and operate. Another cluster of users emphasizes
the importance of reproducible provisioning. That includes
features such as saving a working setup as a template and
flexibility to add tools. A notable response described a “golden
image” preloaded with tools; that gave me the idea for the
personalized image SideKernel implements today. Finally,
many comments note that granularity in the policies for the
security controls, as well as observability, is an important
attribute.
B. Usability Barriers
The usability barriers reported in the user survey are de-
picted in Fig. 4 and aggregated into the following three
categories:
1)Host–sandbox file sharing (UB-1):How cumbersome is
it to share files between the host and the sandbox? This
includes regular files, dotfiles and the clipboard.
2)Networking (e.g., ports, localhost, internet access) (UB-
2):How hard is it to get ports, localhost, and networking
to work correctly?
3)Environment provisioning (UB-3):Does the environment
(e.g., dotfiles, shell, tools, logins) have to be recreated
every time in the sandbox? This includes ease of first use,
custom Claude skill transfer, persisting configurations and
package installations across restarts—as well as the initial
setup of the sandboxes.
Beyond these three usability barriers, users also noted
usability issues regarding installation, multisandbox manage-
ment, reliability and performance. However, to keep imple-

Figure 5. SideKernel’s Architecture
mentation realistic within the time constraints of the practicum,
I only based my development and evaluation on the top three
most common usability barrier categories. For the evaluation,
each usability barrier category is broken down into capability
tests in Section VII.
VI. SIDEKERNEL
A. Architecture
A depiction of SideKernel’s architecture can be found in
Fig. 5. SideKernel consists of a virtual machine monitor
(VMM) written in Swift on top of Apple’s Virtualization
framework. It uses a stripped-down precompiled Linux kernel
by Kata Containers [42], over a curated Ubuntu root filesystem
built on first run, both pinned down to theirSHA256hashes.
Moreover, a core component of SideKernel is a minimal
zero-dependency Rust agent that runs as PID 1 inside the mi-
croVM. This Rust agent is responsible for mounting the host’s
filesystem using VirtioFS, and for automatic port detection &
forwarding. The Rust agent uses virtual sockets (vsock) for
communication with the host and exposes a pseudoterminal.
An important design decision is a small credential proxy
server on the host, outside the sandbox. It intercepts the agent’s
API requests and injects AI coding agent credentials, so that
no credentials are ever available inside the sandbox 4
B. Design Goals and Implementation
The user survey signals that usability issues constitute barri-
ers to adoption of sandboxes for AI coding agents. Therefore,
SideKernel is opinionated, and its design is guided by the
usability issues the survey identified. This opinionated design
means that the standard deny-all-by-default principle is applied
selectively rather than absolutely, in favor of usability.
4The only exception is the first authentication inside the sandbox, where
SideKernel reads the credentials and immediately deletes them from the
sandbox while storing them in the macOS Keychain.
Each design goal of SideKernel relates to a usability barrier
of Section V. The capabilities developed bind to a specific
usability barrier but some entail a deliberate risk acceptance,
as described in SideKernel’s threat model (Section II-B) and
summarized in Table II.
Table II also includes design goals not implemented for
this paper. These goals around credentials management, ob-
servability of agentic events inside the sandbox, visibility of
outbound connections, and more granular controls on the north
boundary were scoped down from the initial aspirations of the
practicum. Some of those features are present in other mature
products such as Docker Sandboxes [22].
The rest of this subsection describes the operation of SideK-
ernel in more detail.
1) Entering a sandbox:After installing SideKernel 5, a user
can enter the shell of SideKernel by typingsidekernel
(or the abbreviated aliassk). The command launches a new
ephemeral microVM in the background and the current direc-
tory of the host is automatically mounted to this microVM.
While this implicit mount looks contrary to standard security
practices, it is exactly what a Claude session (and other AI
coding agents) does on the host, so it matches what the
user expects. A user then can runclaudeinside SideKernel
to launch Claude Code, as the latest version of Claude is
preinstalled on the first launch. However, SideKernel also
provides a faster way to start Claude. That is, by running
sclaudedirectly on the host (which stands forSecure
ClaudeorSideKernel Claude).
2) Authentication:If Claude is already authenticated on the
host, running it inside SideKernel automatically provides an
authenticated session. When running Claude inside SideKernel
for the first time, SideKernel’s VMM reads Claude’s existing
credentials from the host’s macOS Keychain. This is only
possible after an explicit approval from the user. The macOS
Keychain access control prompt requests the user for their
password and permission to allow SideKernel to write to it. If
Claude is not authenticated on the host, authenticating Claude
in the sandbox also auto-authenticates Claude to the host. In
a nutshell, SideKernel’s and the host’s Claude share the same
authentication.
3) Sharing External Files:Host files and folders out-
side of the mounted directory can be requested frominside
SideKernel at runtime via an in-guest command,sk-drop
<host-path>, which, combined with explicit user approval
outside the sandbox, drops external files into SideKernel.
SideKernel includes preloaded instructions for Claude on how
to usesk-drop. Therefore, asking Claude for a macOS file,
or dragging and dropping a file into a Claude session is enough
to triggersk-dropand make the file available to the agent.
Moreover, the clipboard of the host is pastable into SideKernel.
For SideKernel’s Claude sessions particularly, images (e.g.
clipboard screenshots) are pastable into the SideKernel session
as well.
5Currently through a Makefile—in future work through brew or .dmg files

Table II
SIDEKERNEL DESIGN GOALS TRACED TO THE USABILITY BARRIERS OFSECTIONVAND THE BOUNDARIES OFSECTIONII-B
UB Boundary Design Goal Mechanism Implemented Risk Description
UB-1 South The current folder is the sandbox Implicit bidirectional current directory
mount withVirtioFS
✓The agent may read, edit or destroy
anything in the mounted directory
UB-1 South External (non-mounted) files or
directories reachable at runtime, with
explicit consent
Commandsk-dropwith host-side
approval. Drag and drop works into
SideKernel Claude’s sessions
✓ —
UB-1 South Copy and paste works between the
host and SideKernel’s Claude sessions
Bidirectional text (and image)
clipboard
✓—
UB-2 South Exposed sandbox ports are
automaticallyavailable on the host
SideKernel auto-detects and forwards
guest ports to127.0.0.1
✓ A malicious agent can open ports to
the host, exposing malicious services.
UB-2 North Block all internet/external traffic, while
the Claude agent still works
NAT kill-switch, Claude inference
endpoints allowlisted by default
✓—
UB-3 South SideKernel feels like a second PC (e.g.,
installed packages and configurations
persist across sandboxes)
Runtime OverlayFS persistence with a
personalized SideKernel image, using
the in-guestsavecommand
✓ —
UB-3 South One login authenticating on the Mac
orinside a sandbox authenticates both
The default Claude Code macOS
Keychain entry is shared between the
VMM of SideKernel (not the sandbox)
and the host
✓—
UB-3 South Claude credentials are never exposed
inside the sandbox
Credential proxy outside of the
sandbox
✓ —
UB-3 South Agent feels and behaves as configured
on the host
Automatic skill, agent and plugin
transfer
✓—
UB-3 South Arbitrary user secrets can be stored
outside the sandbox, and injected
securely
To be defined (Future Work,
Section X)
✗ —
UB-2 North The user can allowlist arbitrary
destinations while egress is otherwise
blocked
To be defined (Future Work,
Section X)
✗—
— — Agentic AI filesystem and process
events inside the sandbox are logged
To be defined (Future Work,
Section X)
✗ —
— North External endpoints the agent contacted
are logged
To be defined (Future Work,
Section X)
✗—
4) Ports and networking:In SideKernel port forwarding
is fully automatic. For example, running a Python server on
port 4000 inside the sandbox makes that port accessible on
the host without any extra steps or explicit port forwards. The
Rust agent detects newly opened ports, and SideKernel auto-
exposes them on the host’s loopback address.
5) Network (NAT) kill switch:SideKernel provides a net-
work kill switch for the northbound channel, controlled by
an in-guest command viask-net <on/off>. Turning the
kill switch on blocks all outbound traffic on the northbound
channel. The only exception is the official API endpoint of
Claude (api.anthropic.com), so that Claude can still
run inference. Turning the kill switch off restores traffic on
the northbound channel (this action requires explicit user
approval). This capability is coordinated by SideKernel’s Rust
agent in communication with SideKernel’s VMM.
6) Persistence and host parity:A user can use SideKernel
as they would use any machine, install packages or change
configurations, and then type the in-guest commandsavein-
side the sandbox. With save, a personalized image (an overlay
filesystem) persists those changes across restarts and across
sandboxes. Every time SideKernel is started or restarted, the
VMM spins up and down a new ephemeral microVM in the
background. Persisting this state gives the user a sense of
continuity. To facilitate environment set-up and provisioning
further, Claude’s skills, plugins and agents are automatically
copied in from the host before boot, so Claude in SideKernel
works as transparently as possible.
VII. EVALUATION: A COMPARATIVEANALYSIS
The evaluation of SideKernel takes the form of a compar-
ative analysis. First, I filter the list of discovered sandboxes
against the inclusion requirements two to five (IR-2 to IR-5) as
depicted in Fig. 3. IR-1 (Open-Source) is deliberately excluded
from the filtering. Restricting the study to open-source systems
would exclude Docker Sandboxes [22], which is freely avail-
able and maintained by a well-known and reputable company
in the systems industry.
The results of the first stage of the filtering process are
shown in detail in Table I. The sandboxes that pass the
inclusion criteria and filtering process are Docker Sandboxes,

Microsandbox, SmolVM, Shuru, VibeBox 6 and, of course,
SideKernel.
A. Comparative Analysis Process
I break down each usability barrier intoCAPABILITY TESTS:
A capability test is aspecific sequence of unit actions. Ex-
amples include (but are not limited to) running a host-side
command, opening a new terminal window, dragging a file
onto Claude’s session window, pasting text or an image to
the clipboard, entering a password etc. In Tables III, IV,
and V,T n refers to then-th capability test of each usability
barrier category. The capability tests are summarized under
each results table and are shown in detail in Appendix A. The
result of each capability test is then reported in two parts:
1) Thebinary outcomeof the capability test (mandatory)
2)Friction notesrecording qualitatively the ease-of-use of
passingmechanisms. (optional, where applicable)
In order to be as specific as possible in the qualitative
descriptions I define and use the following terms:
1)Native:The perceived user experience is exactly the same
as on a macOS machine, requiring no additional unit
actions
2)Frictionless:The perceived user experience is pleasant,
but not native-like, requiring one or two additional unit
actions
3)(With) friction:The perceived user experience is un-
pleasant, requiring three or more additional unit actions
B. UB-1: Host–Sandbox File Sharing
Table III summarizes the results of the capability tests for
UB-1. Out of the nine (9) total tests, SideKernel passes eight
(8), Docker Sandboxes passes six (6), and Microsandbox,
Shuru, and SmolVM pass five (5).
6VibeBox was included in the initial list for completeness. However it is
an unmaintained project (the first public commit to VibeBox was on Feb 7,
2026 and last commit on Feb 18, 2026) which has only one contributor, its
author. Moreover, after significant effort to install VibeBox on two separate
macOS machines (macOS Tahoe 26.2, M1 & M4 chips) I was unable to get a
working sandbox, despite following its README.md instructions. Therefore,
although the sandbox passes the inclusion criteria, it is currently not a suitable
candidate for evaluation.
Table III
UB-1 — HOST–SANDBOX FILE SHARING
Sandbox T1 T2 T3 T4 T5 T6 T7 T8 T9 Pass
Docker Sbx✓ ✓ ✗ ✓ ✗ ✗ ✓ ✓ ✓ 6
Microsandbox ✓ ✗ ✗ ✓ ✗ ✗ ✓ ✓ ✓ 5
Shuru✓ ✓ ✗ ✗ ✗ ✗ ✓ ✓ ✓ 5
SmolVM ✓ ✗ ✗ ✓ ✗ ✗ ✓ ✓ ✓ 5
VibeBox — — — — — — — — — —
SideKernel ✓ ✓ ✗ ✓ ✓ ✓ ✓ ✓ ✓ 8
T1 Mount read/create/delete, both directions
T2 Mount mode propagation, both directions
T3 Mount inode notification, host→sandbox
T4 Unmounted file transfer, host→sandbox
T5 Clipboard image, host→Claude in sandbox
T6 Clipboard text, Claude in sandbox→host
T7 Mount ownership propagation
T8 Symlink resolution
T9 Large file (10 GB) mount integrity
Friction Notes
Docker Sandboxes and SideKernel offer anativemounting
experience automounting the CWD. The rest of the sandboxes
require pre-launch mounts from the host causingfriction. In
Microsandbox and SmolVM, permission bits (r, w, x) do not
carry across the south boundary.
External file dropping (T4) is possiblewith frictionon
Docker Sandboxes, Microsandbox, and SmolVM via a host-
side command: the user must open a new terminal, recall the
sandbox name, discover the sandbox path for mounting the
file, and type/paste it. Each of these unit actions adds friction.
Indicatively, the host-side commands are:
# Mounting
shuru run --mount <HOST-PATH>:<SBX-PATH>
msb run ubuntu --mount-dir <HOST-PATH>:<SBX-PATH>
smolvm machine start --name <n> -v <HOST-PATH>:<SBX-PATH>
# Copying external files
sbx cp <FILE> <SBX-NAME>:<SBX-PATH>
msb copy <FILE> <SBX-NAME>
smolvm machine cp <FILE> <SBX-NAME>:<SBX-PATH>
SideKernel’s in-guest commandsk-drop <FILE>, as
well as the ability to drag and drop a file directly into
the Claude session (and Claude executessk-dropin the
background) isfrictionless: requiring one in-guest command
and approval on a macOS modal per external file.
A host Claude Code session allows pasting of both text
and images in interactive mode [43]. SideKernel is the only
sandbox to pass the clipboard tests (T5, T6), supportingnative-
likebidirectional text copy and paste, and unidirectional image
pasting from the host clipboard into the SideKernel sandbox.

C. UB-2: Networking, Ports & Localhost
Table IV summarizes the results of the capability tests
for UB-2. Out of the five (5) total tests, Docker Sandboxes
passes five (5), while Microsandbox, Shuru, SmolVM, and
SideKernel pass three (3).
Table IV
UB-2 — NETWORKING,PORTS&LOCALHOST
Sandbox T1 T2 T3 T4 T5 Pass
Docker Sbx✓ ✓ ✓ ✓ ✓ 5
Microsandbox ✗ ✓ ✗ ✓ ✓ 3
Shuru✗ ✓ ✗ ✓ ✓ 3
SmolVM ✗ ✓ ✗ ✓ ✓ 3
VibeBox — — — — — —
SideKernel ✓ ✓ ✗ ✓ ✗ 3
T1 Runtime port forwarding
T2 Restart port forwarding
T3 DNS connection URL logs visibility
T4 Egress control, blocking
T5 Egress control, allowlisting
Friction Notes
All candidate sandboxes provide some way of port-
forwarding, however they differ on the mechanism. SideKernel
providesnative-likeautomatic runtime port-forwarding with-
out any user interaction; Docker Sandboxes allowsfrictionless
manual runtime port forwarding through a host command.
Microsandbox, SmolVM and Shuru allow port-forwarding
but not on a running sandbox (T1). They require the ports
to be defined on the host before starting the sandbox, which
introducesfriction(especially if the developer does not know
in advance if and which ports they might need open and
exposed to the host). Indicatively, the commands are:
msb run ubuntu --port <HOST-PORT>:<SBX-PORT>
smolvm machine <run|create> --port <HOST>:<SBX-PORT>
shuru run -p <HOST-PORT>:<SBX-PORT> -- nginx
Docker Sandboxes is the only sandbox providing DNS
observability on the north boundary (T3). All sandboxes but
SideKernel provide granular north boundary security controls
blocking egress traffic with allowlists. SideKernel provides
an in-guest kill-switch without however the granularity other
sandboxes provide.
Notably, Docker Sandboxes’ allowlist is configurable
through the sandbox’s built-in TUI beyond declarative host
policies, making it easy to disallow or allow connections
during runtime. It continuously monitors DNS connections,
lists all the domains that the sandbox has communicated with,
and allows the allowlist to be toggled seamlessly through the
terminal interface (or new records to be added).
These observability and firewall features are additional
capabilities that are not normally present in the host; therefore,
describing friction for those is not applicable.
D. UB-3: Environment Provisioning & Setup
Table V summarizes the results of the capability tests for
UB-3. Out of the nine (9) total tests, Docker Sandboxes and
SideKernel pass eight (8), and SmolVM, Microsandbox and
Shuru pass four (4).
Table V
UB-3 — ENVIRONMENT PROVISIONING&SETUP
Sandbox T1 T2 T3 T4 T5 T6 T7 T8 T9 Pass
Docker Sbx✓ ✗ ✓ ✓ ✓ ✓ ✓ ✓ ✓ 8
Microsandbox ✗ ✗ ✓ ✓ ✓ ✓ ✗ ✗ ✗ 4
Shuru✗ ✗ ✓ ✓ ✓ ✓ ✗ ✗ ✗ 4
SmolVM ✗ ✗ ✓ ✓ ✓ ✓ ✗ ✗ ✗ 4
VibeBox — — — — — — — — — —
SideKernel ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✗ 8
T1 Agent preinstallation
T2 Credential inheritance
T3 Agent state persistence
T4 Configuration file persistence
T5 Package installation persistence
T6 Git state visibility
T7 Live checkpoint persistence
T8 Secret store, agent credentials
T9 Secret store, custom secrets
Friction notes.
Docker Sandboxes and SideKernel are the only two sand-
boxes that come with preinstalled agents (T1). However,
Docker Sandboxes supports many major agents including
Claude Code, Codex, Gemini CLI, GitHub Copilot, opencode
and more. SideKernel currently only supports Claude Code.
SideKernel is the only sandbox that shares agent authentication
with the host, providing africtionlessexperience on the first
run (entering the macOS password once on the Keychain’s
access control prompt).
Configuration and package installation persistence is feasi-
ble in all sandboxes, although in Shuru, Microsandbox, and
SmolVMwith friction. Docker Sandboxes and SideKernel
however persist changes that survive restarts at runtime in a
frictionlessmanner.
With regard to AI agent configuration, SideKernel is the
only sandbox that inherits Claude Code’s skills, plugins and
agents from the host providing anative-likeexperience. With
regard to credentials management, Docker Sandboxes is the
only sandbox with a built-in secret store for custom creden-
tials.
VIII. DISCUSSION
A. Interpreting the Aggregate Results
Across all 23 capability tests, Docker Sandboxes and SideK-
ernel pass 19 tests, SmolVM, Microsandbox and Shuru pass 12
tests. The combination of the aggregated test results with the
qualitative friction notes indicates that Docker Sandboxes and
SideKernel are the most usable sandboxes in the study (fol-
lowing the benchmark introduced in Section IV-D). However,
this is only true inside the confines of the usability barriers that
were tested and it is not a generalizable statement. It is also
worth noting that even among AI coding agent sandboxes, the
intended use varies. Docker Sandboxes, for example, is built
for enterprise deployments and multi-sandbox orchestration.

Shuru is intended to be used as a Claude skill invoked by an
AI agent running on the host, self-isolating its tool runs inside
the sandbox. SideKernel attempts to replicate as closely as
possible the experience a user has on the host, from inside a
microVM. Last but not least, Microsandbox and SmolVM are
hybrid sandboxes, focusing primarily on SDK programmable
agents and providing CLI features as a sidecar rather than as
their main design.
B. Comparison with Docker Sandboxes
SideKernel provides a few features bound to usability bar-
riers of the user study that no other sandbox does:frictionless
external file drops through an in-guest command or drag
and drop into Claude, automatic port forwarding of newly
opened ports inside the sandbox, bidirectional clipboard ca-
pabilities inside Claude sessions (e.g., pasting images), and
synchronized authentication with the host. These are small
but not insignificant contributions to the current market of
sandboxes. Moreover, I intend to open-source SideKernel, a
fact differentiating it from the free but closed-source Docker
Sandboxes.
That said, Docker Sandboxes is an undeniably more feature-
rich sandbox, including advanced observability and auditing
capabilities, governance and granular policies, a versatile ter-
minal user interface, easy multi-sandbox management features,
mature credential management, and others that were out of
scope for this study. However, within the confines of the
usability barriers that the user study discovered, I conclude
Docker Sandboxes and SideKernel are the most capable
sandboxes in regard to usability features—something which a
reader can evaluate through the capability tests and the friction
notes.
C. Real-World Considerations
•SideKernel is designed for single macOS machines, but
tested only on M1 and M4 chips and only on the latest
Tahoe 26.2 OS version. It might still include undetected
bugs and rough edges.
•The security of SideKernel is implied from an architec-
tural perspective, but the implementation has not under-
gone a formal security review.
•SideKernel is not yet notarized (and it is self-signed). It
currently has no observability out of the box.
•SideKernel currently provides no enterprise features,
including logging, declarative policies and centralized
governance capabilities.
IX. LIMITATIONS ANDTHREATS TOVALIDITY
Below I describe all the limitations and threats to the validity
of the evaluation and development of SideKernel. The majority
of those limitations are attributed to the time constraints of
the practicum (which required scoping down), and single-
evaluator bias.
•Evaluator bias.The comparative analysis unavoidably
introduces bias, because the developer is also the evaluator.
Although I took every reasonable measure to reduce it (e.g.
fixed success criteria, binary outcomes based on built-in
capabilities, auditable tests, standardized and transparent
friction notes), a better methodology would involve multi-
ple users, something, however, practically infeasible within
the practicum’s timeline.
•User survey instrument bias.The user survey instru-
ment is designed by the developer. Many of the survey’s
questions are multiple-choice or multi-select format. This
anchors respondents towards the pre-formulated options,
which introduces bias. I mitigate this by providing a
free-text “Other” option on closed questions, as well as
enriching the instrument with open free-text questions.
While this likely reduces the instrument bias, it does not
eliminate it.
•Sampling bias.The online survey’s sample tilts towards
a security-aware audience. Real-world AI coding agent
sandbox adoption is therefore probably significantly lower
than the 38.2% that the study records.
•Sample size.While the sample (N = 80 respondents; 33
current or former sandbox users) is likely sufficient for
formative/directional signals, it is low. The results were
used for informed development decisions and a framework
for the comparative analysis, rather than statistically gen-
eralizable data.
•Informal study status.The formative user survey was
conducted as informal practicum research and did not
undergo a formal Georgia Tech IRB review. The study is
not designed to produce generalizable knowledge but rather
its results are interpreted as signals for the development and
evaluation of SideKernel, rather than rigorous academic
data.
•Usability is measured indirectly.The tests measure how
well a sandbox addresses the survey’s usability barriers,
not usability in any general sense.
•Binary scoring without gradation.The binary score of
the capability tests is blind to friction. While I remediate
this with qualitative notes on friction, it does not eliminate
the fact that the score itself does not weigh the very
nuances that describe usability.
•Binary scoring without weights.The binary score of the
capability tests does not consider which capabilities are
important for the users in practice. The scores are naive,

in the sense that the binary outcomes are unweighted.
Therefore, the results are approximations.
•Platform constraints.SideKernel is a Linux microVM on
top of macOS. It therefore cannot offer capabilities that
Seatbelt-based sandboxes can. For example, it is unsuit-
able for testing native macOS SwiftUI applications, and
certain macOS terminal commands are unavailable inside
SideKernel.
•Scoping constraints.SideKernel is a microVM sandbox.
Sandboxes based on other isolation primitives such as
macOS Seatbelt might also provide sufficient security
guarantees—depending on the use case and threat model.
SideKernel is not evaluated against such sandboxes which
were deliberately left out of scope to keep the project
manageable within the time constraints of the practicum.
X. FUTUREWORK
The comparative analysis exposed areas for improvement
in SideKernel, in particular capabilities that similar sandboxes
already implement. Future work will include replacing the
NAT kill-switch with a full network proxy server that provides
granular allowlisting. Such a network proxy will also allow
implementation of DNS observability. On the south boundary,
the remaining work is a secure generic credential management
store, beyond Claude’s credentials. Finally, SideKernel will
support more major agents (in a similar way to how Claude
Code is currently integrated), including Codex, Microsoft
Copilot and others.
XI. CONCLUSION
SideKernel constitutes a capable local microVM sandbox
for AI coding agents that addresses many of the usability
barriers reported in the user study. It is currently the only local
microVM sandbox that solves the bidirectional clipboard issue
in Claude Code, provides automatic runtime port forwarding,
integrates Claude Code’s native macOS Keychain authenti-
cation seamlessly, and transfers the host’s Claude skills and
agents into the sandbox automatically. Moreover, it provides
a frictionless way to drop external files into the sandbox, and
eases environment provisioning through a personalized image.
Another highly capable microVM sandbox in the context of
the usability barriers addressed is Docker Sandboxes. It is the
only sandbox that allows or blocks DNS requests through a
TUI, provides custom credential management, preinstalls most
major AI coding agents, and offers observability on top.
Microsandbox, Shuru and SmolVM follow, with more lim-
ited AI coding agent capabilities.
I attribute this to the fact that there has been little serious
effort in the industry focused on AI coding agents for local ma-
cOS environments. The arms race pushes sandboxes towards
autonomous programmable SDK agents, leaving coding agents
as an afterthought, despite this being a demonstrably real
security problem. This part of the industry is still young and
rapidly developing. The fact that an infrastructure company as
big as Docker did not release sbx until January 30, 2026 [22]
further strengthens this claim, and justifies the development of
SideKernel.
A personal note: I already use SideKernel daily. I now
develop SideKernel inside of SideKernel!

APPENDIXA
FULLTASKDEFINITIONS
This appendix gives the complete definition of every task referenced in Section VII. Each task is a capability test with a
binary outcome, scored according to the criteria in Section IV-D.
Table VI: UB-1 — Host–sandbox file sharing: full task definitions
ID Name Definition
T1 MOUNTCRUD,BOTH DIRECTIONS Read, create and delete the mount dir filemount/workspace-file.txtand validate
bidirectionally all actions.
T2MOUNT MODE PROPAGATION,
BOTH DIRECTIONS
Runchmod 777 mount/shell.sh. Test that all the permission bits (r, w, x) carry across.
T3 MOUNT INODE NOTIFICATION,
HOST→SANDBOX
Runinotifywaitonworkspace-file.txtinside the sandbox, then edit the file on the
host. Test that the notification fired.
T4UNMOUNTED FILE TRANSFER,
HOST→SANDBOX
Test whether<HOST-PATH>/external-file.txtcan be accessed and read inside the
sandbox, without host-side commands, without sandbox restart, and with explicit approval. a
T5 CLIPBOARD IMAGE,HOST→
CLAUDE IN SANDBOX
Copy an image to the host clipboard. Test that it pastes into the Claude session inside the
sandbox.
T6CLIPBOARD TEXT,SANDBOX→
HOST
Copy text from the Claude session inside the sandbox. Test that it pastes on the host.
T7 MOUNT OWNERSHIP PROPAGATION Createmount/sandbox-created.txtinside the sandbox. Test thatls -lon the host
shows the host user as owner.
T8SYMLINK RESOLUTIONCreate a symlink inmount/toworkspace-file.txt. Test that it resolves.
T9 LARGE FILE MOUNT INTEGRITY Mount the zero-filled10GB <HOST-PATH>/big-file.txtto the sandbox. Check that it
mounts successfully and that themd5summatches the one on the host.
a The goal is to let the user read any external file easily and securely. Easily means from inside the sandbox through a built-in
mechanism, without sandbox restarts or host-side commands; securely means with explicit user approval.
Table VII: UB-2 — Networking, ports & localhost: full task definitions
ID Name Definition
T1RUNTIME PORT FORWARDINGRunpython3 -m "http.server" 5000inside the sandbox. Configure port forwarding
without restarting the sandbox for 5000. Test thatcurl localhost:5000is reachable from
the host.
T2 RESTART PORT FORWARDING Runpython3 -m "http.server" 6000inside the sandbox. Test thatcurl
localhost:6000is reachable from the host after explicitly configuring port forwarding.
T3DNSCONNECTIONURLLOGS
VISIBLE
Provides a DNS network log panel listing the websites connected to.
T4 EGRESS CONTROL,BLOCKING Test that blocking outbound internet access is feasible with a built-in sandbox mechanism
enforced by the hypervisor. Run the sandbox and block all traffic.
T5EGRESS CONTROL,ALLOWLISTINGIf blocking outbound internet access is feasible, test whether allowlisting is feasible natively,
enforced by the hypervisor. Run the sandbox and allowlistcurl https://example.com.
Table VIII: UB-3 — Environment provisioning & setup: full task definitions. For each
task, the tester checkpoints the sandbox (if applicable)
ID Name Definition
T1AGENT PREINSTALLATIONTest thatclaude -versionsucceeds on first boot, without the tester installing it manually.
T2 CREDENTIAL INHERITANCE Ensure Claude is authenticated on the host. Test that the agent completes a prompt–response
round-trip inside the sandbox without the tester performing a login in the sandbox.
T3AGENT STATE PERSISTENCERestart the sandbox. Test that Claude is still present and authenticated.

Table VIII (continued)
ID Name Definition
T4 CONFIGURATION FILE
PERSISTENCE
Define aliasprint_hiin the sandbox shell rc, and restart it. Test thatprint_hiresolves.
T5PACKAGE INSTALLATION
PERSISTENCE
Runpip install -r requirements.txt, and restart it. Test thatpython -c
"import numpy"exits successfully.
T6 GIT STATE VISIBILITY Rungit init .on the host and create a new file calledgit.txt. Enter the sandbox and
rungit diff .. Test whethergit.txtappears on the diff.
T7LIVE CHECKPOINT PERSISTENCETest whether the sandbox supportslive checkpoints. A live checkpoint saves therunning disk
stateof a sandbox, including installed packages and configuration changes. Runapt-get
install nmap, checkpoint and restart the sandbox, then verify whethernmapis still installed.
T8 SECRET STORE,AGENT
CREDENTIALS
Test whether the sandbox provides a designated secret store (e.g., macOS Keychain) for Claude
credentials (OAuth/API Keys).
T9SECRET STORE,CUSTOM SECRETSTest whether the sandbox provides a designated secret store (e.g., macOS Keychain) for
arbitrary custom secrets.
APPENDIXB
GOOGLESURVEYRESULTS
Table IX reports the complete survey results. Questions are presented for the relevant corresponding groups, for example,
sandboxing tools previously used are over the group of former users. Reasons for never using a sandbox are over the group
of non-users etc. For brevity, I omit free-text responses/options that were only selected by a single respondent.
Table IX: Complete Google Survey results
Question / Response n %
Q1. Do you currently use AI coding agents? (N= 80)
Yes 68 85.0
No 12 15.0
Q2. Professional role (n= 68)
Cybersecurity (Engineering, OffSec etc) 23 33.8
Software developer or engineer 14 20.6
Platform engineer 10 14.7
Technical manager or product owner 8 11.8
Hobbyist developer 4 5.9
Student 4 5.9
Data/AI engineer or scientist 3 4.4
Other (e.g., founder) 2 2.9
Q3. AI coding agents used (multi-select,n= 68)
Claude Code 59 86.8
OpenAI Codex 26 38.2
GitHub Copilot (agent mode/chat, not just inline suggestions) 23 33.8
Cursor 13 19.1
Gemini CLI 10 14.7
opencode 2 2.9
Q4. Operating systems used (multi-select,n= 68)
macOS 41 60.3
Linux 37 54.4
Windows 22 32.4
Windows (in WSL) 13 19.1
Q5. Have you used an isolation environment for AI coding agents? (n= 68)
Yes, I currently use one 26 38.2
Yes, but I stopped using it 7 10.3
No, I have never used one 35 51.5
Q6. Sandboxing tools in use (multi-select, current users,n= 26)
Docker Sandboxes 12 46.2
Full VM (UTM, Parallels, Lima etc.) 9 34.6
continued on next page

Table IX (continued)
Question / Response n %
Nono.sh 7 26.9
Separate machine dedicated for AI (e.g., Mac Mini) 2 7.7
Q7/Q10. Barriers experienced (multi-select, current + former users,n= 33)
No significant difficulties † 9 n/a
Had to set everything up from scratch (dotfiles, shell, tools, logins) 8 24.2
Getting ports / localhost / networking to work is difficult 8 24.2
Sharing files between sandbox and host is hard or slow 7 21.2
Security benefit not worth the effort ‡ 6 n/a
Managing multiple sandboxes is confusing 5 15.2
Initial installation / setup is too hard 5 15.2
It is slow, or slows down my machine 4 12.1
The sandbox itself crashes or breaks 3 9.1
OS mismatch (e.g., macOS host, Linux-only sandbox) 3 9.1
Usual host tools do not work inside the sandbox 2 6.1
Q9. Sandboxing tools previously used (multi-select, former users,n= 7)
Docker Sandbox 3 42.9
Full VM (UTM, Parallels, Lima etc.) 2 28.6
Microsandbox 1 14.3
Separate machine dedicated for AI (e.g., Mac Mini) 1 14.3
OrbStack 1 14.3
OpenHands with Docker 1 14.3
Q12. Reasons for never using a sandbox (multi-select,n= 35)
I have never considered it 21 60.0
I am not aware of any good options 11 31.4
The security benefit does not seem worth the effort for my use case 9 25.7
The built-in sandboxing in my coding agent is sufficient 7 20.0
I looked into it, but it seemed too difficult 4 11.4
† Offered to current users only; not applicable to the combined percentage base.
‡ Offered to former users only; not applicable to the combined percentage base.

ACKNOWLEDGMENT
I co-developed the SideKernel codebase with AI (Claude,
Anthropic). I also used AI to refine the grammar and phrasing
of this paper, to generate the LaTeX code for tables and the
draw.io code for diagrams, and to review the manuscript for
factual errors. AI was used in a supporting capacity throughout
every task, but the substance of the work is my own, including
but not limited to the text of this paper, design decisions, threat
model, methodology, instrument design, content of the tables
and diagrams, evaluation, analysis, research, and conclusions.
REFERENCES
[1] M. Christodorescu, E. Fernandes, A. Hooda, S. Jha,
J. Rehberger, K. Chaudhuri, X. Fu, K. Shams, G. Amir,
J. Choi, S. Choudhary, N. Palumbo, A. Labunets,
and N. V . Pandya, “Agent security is a systems
problem,” 2026. [Online]. Available: https://arxiv.org/
abs/2605.18991
[2] Always Further, Inc., “nono sandbox documentation,”
2026, accessed: Jun. 28, 2026. [Online]. Available:
https://nono.sh/os-sandbox
[3] Zouuup, “landrun: Run Any Linux Process in
a Secure, Unprivileged Landlock Sandbox,” 2026,
accessed: Jul. 25, 2026. [Online]. Available:
https://github.com/Zouuup/landrun
[4] Fence, “Fence Documentation,” 2026, accessed: Jun. 28,
2026. [Online]. Available: https://fencesandbox.com/docs
[5] Agent Safehouse, “Agent Safehouse Documentation,”
2026, accessed: Jul. 25, 2026. [Online]. Available:
https://github.com/eugene1g/agent-safehouse
[6] L. Meng, H. Feng, I. Shumailov, and E. Fernandes,
“ceLLMate: Sandboxing browser AI agents,” 2025.
[Online]. Available: https://arxiv.org/abs/2512.12594
[7] Daytona Platforms, Inc., “Daytona Documentation,”
2026, accessed: Jun. 28, 2026. [Online]. Available:
https://www.daytona.io/docs/en/sandboxes/
[8] F. Taylor, “Yolobox,” 2026, accessed: Jun. 28, 2026.
[Online]. Available: https://yolobox.dev/
[9] Agent Infra, “AIO Sandbox Documentation,” 2026,
accessed: Jul. 25, 2026. [Online]. Available: https:
//github.com/agent-infra/sandbox
[10] Deno Land, Inc., “Deno Sandbox Documentation,”
2026, accessed: Jun. 28, 2026. [Online]. Available:
https://docs.deno.com/sandbox/
[11] Bots Garden, “Capsule,” 2025, accessed: Jun.
28, 2026. [Online]. Available: https://github.com/
bots-garden/capsule
[12] Port of Context, “pctx,” 2026, accessed: Jun. 28, 2026.
[Online]. Available: https://github.com/portofcontext/
pctx
[13] E2B, “E2B Documentation,” 2026, accessed: Jun. 28,
2026. [Online]. Available: https://e2b.dev/docs
[14] Super Rad Company, “Microsandbox Documentation,”
2026, accessed: Jun. 28, 2026. [Online]. Available: https:
//docs.microsandbox.dev/getting-started/introduction
[15] Shuru, “Shuru Sandbox Documentation,” 2026, accessed:
Jun. 28, 2026. [Online]. Available: https://github.com/
shuru-project/shuru
[16] VibeBox, “VibeBox Documentation,” 2026, accessed:
Jun. 28, 2026. [Online]. Available: https://github.com/
robcholz/vibebox
[17] Cua, “Cua Documentation,” 2026, accessed: Jun. 28,
2026. [Online]. Available: https://github.com/trycua/cua
[18] Smol Machines, “smolvm: Portable, Lightweight, Self-
Contained Virtual Machine,” 2026, accessed: Jul.
25, 2026. [Online]. Available: https://github.com/
smol-machines/smolvm
[19] Fly.io, “Sprites: Stateful Sandbox Environments,” 2026,
accessed: Jul. 25, 2026. [Online]. Available: https:
//sprites.dev/
[20] A. Bhardwaj, “Arrakis,” 2025, accessed: Jun. 28, 2026.
[Online]. Available: https://github.com/abshkbh/arrakis
[21] OpenSandbox, “OpenSandbox Documentation,” 2026,
accessed: Jul. 25, 2026. [Online]. Available: https:
//github.com/opensandbox-group/OpenSandbox
[22] Docker, Inc., “Docker Sandboxes (sbx) Documentation,”
2026, accessed: Jun. 28, 2026. [Online]. Available:
https://docs.docker.com/ai/sandboxes/
[23] InstaVM, “CodeRunner Documentation,” 2026,
accessed: Jun. 28, 2026. [Online]. Available:
https://instavm.io/docs/quickstart
[24] OW ASP GenAI Security Project, “Agentic AI — threats
and mitigations,” OW ASP Agentic Security Initiative,
Tech. Rep. Version 1.1, Dec. 2025, accessed: Jun. 28,
2026. [Online]. Available: https://genai.owasp.org/
[25] J. Spracklen, R. Wijewickrama, A. H. M. N. Sakib,
A. Maiti, B. Viswanath, and M. Jadliwala, “We have a
package for you! A comprehensive analysis of package
hallucinations by code generating LLMs,” inProceed-
ings of the 34th USENIX Security Symposium (USENIX
Security 25). Seattle, W A, USA: USENIX Association,
2025.
[26] A. Agache, M. Brooker, A. Florescu, A. Iordache,
A. Liguori, R. Neugebauer, P. Piwonka, and D.-M. Popa,
“Firecracker: Lightweight virtualization for serverless
applications,” inProceedings of the 17th USENIX Sympo-
sium on Networked Systems Design and Implementation
(NSDI 20). USENIX Association, 2020, pp. 419–434.
[27] S. Kuenzer, V .-A. B ˘adoiu, H. Lefeuvre, S. Santhanam,
A. Jung, G. Gain, C. Soldani, C. Lupu, ¸ S. Teodor-
escu, C. R ˘aducanu, C. Banu, L. Mathy, R. Deaconescu,
C. Raiciu, and F. Huici, “Unikraft: Fast, specialized
unikernels the easy way,” inProceedings of the Sixteenth
European Conference on Computer Systems, New York,
NY , USA, 2021, pp. 376–394.
[28] Vercel, “Vercel Sandbox,” 2026, accessed: Jul. 25, 2026.
[Online]. Available: https://vercel.com/docs/sandbox
[29] Anthropic, “Claude Code: Overview,” 2026, accessed:
Jul. 25, 2026. [Online]. Available: https://code.claude.
com/docs/en/overview
[30] OpenAI, “ChatGPT and Codex Documentation:

Overview,” 2026, accessed: Jul. 25, 2026. [Online].
Available: https://learn.chatgpt.com/docs
[31] Anthropic, “Introducing the Model Context Protocol,”
Nov. 2024. [Online]. Available: https://www.anthropic.
com/news/model-context-protocol
[32] OpenAI, “OpenAI and Hugging Face partner
to address security incident during model
evaluation,” Jul. 2026, accessed: Jul. 28,
2026. [Online]. Available: https://openai.com/index/
hugging-face-model-evaluation-security-incident/
[33] Anthropic, “Making Claude Code More Secure and
Autonomous with Sandboxing,” 2026, accessed: Jun. 28,
2026. [Online]. Available: https://www.anthropic.com/
engineering/claude-code-sandboxing
[34] OpenAI, “Codex Sandboxing,” 2026, accessed: Jun.
28, 2026. [Online]. Available: https://developers.openai.
com/codex/concepts/sandboxing
[35] Google, “Sandboxing in Gemini CLI,” 2026, accessed:
Jun. 28, 2026. [Online]. Available: https://geminicli.
com/docs/cli/sandbox/
[36] xAI, “Enterprise Deployments, Grok Build,” 2026,
accessed: Jun. 28, 2026. [Online]. Available: https:
//docs.x.ai/build/enterprise
[37] Lima Project, “Lima,” 2026, accessed: Jun. 28, 2026.
[Online]. Available: https://lima-vm.io/docs/
[38] Apple, “container,” 2026, accessed: Jun. 28, 2026.
[Online]. Available: https://github.com/apple/container
[39] Orbital Labs, LLC, “OrbStack Documentation,” 2026,
accessed: Jun. 28, 2026. [Online]. Available: https:
//docs.orbstack.dev/
[40] W. Albert and T. S. Tullis,Measuring the User Experi-
ence: Collecting, Analyzing, and Presenting UX Metrics,
3rd ed. Cambridge, MA, USA: Morgan Kaufmann,
2022.
[41] W. Albert, T. S. Tullis, and D. Tedesco,Beyond the Us-
ability Lab: Conducting Large-Scale Online User Expe-
rience Studies. Boston, MA, USA: Morgan Kaufmann,
2010.
[42] OpenInfra Foundation, “Kata Containers,” 2026,
accessed: Jul. 31, 2026. [Online]. Available:
https://katacontainers.io/
[43] Anthropic, “Interactive Mode — Claude Code Documen-
tation,” 2026, accessed: Jul. 29, 2026. [Online]. Avail-
able: https://code.claude.com/docs/en/interactive-mode
