---
title: 'From Tools to Teacher-Built Teammates: No-Code Pedagogical Plugin Authoring with LearnAdapt Agentic
  Studio and PedOS 1.1 Lumina'
url: https://arxiv.org/abs/2607.09674
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Nizam Kadir
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.09674
pages: 3
chars: 5341
fetched_at: '2026-11-08T13:36:33+00:00'
kb_version: 1
---

# From Tools to Teacher-Built Teammates: No-Code Pedagogical Plugin Authoring with LearnAdapt Agentic Studio and PedOS 1.1 Lumina

From Tools to Teacher-Built Teammates:
No-Code Pedagogical Plugin Authoring with
LearnAdapt Agentic Studio and PedOS 1.1
Lumina
Nizam Kadir
Singapore University of Technology and Design
nizam_kadir@mymail.sutd.edu.sg
Abstract.Teachers and researchers need to adapt educational AI to lo-
calgoals,butmostsystemsremaindifficulttocustomizeorstudywithout
coding expertise. We present LearnAdapt Agentic Studio on PedOS 1.1
Lumina, a no-code authoring and governed runtime environment for edu-
cational AI plugins. A non-coder describes a desired learning interaction
in plain English; the system prepares a previewable plugin artifact, runs
safety checks, and supports submission for review. PedOS then deploys
approved plugins into a directory for installation. Crucially, telemetry
is strictly gated to authenticated users running approved plugins. The
demo shows the complete lifecycle from prompt to governed evidence
capture, shifting from fixed tools to teacher-built teammates.
Keywords:Educational AI·no-code authoring·agentic systems·plu-
gin ecosystem
Demo Link
https://www.youtube.com/watch?v=PjIRnAKUxWc
1 Motivation
The AIED 2026 theme raises a practical question: who shapes the AI teammate?
[1].Inmanydeployments,educatorsareunabletoauthorlearninginteractions[2]
or control evidence capture [3], remaining users of fixed systems [4]. LearnAdapt
addresses this by treating AI functionality as governable plugins. A non-coder
describes an activity in plain English, previews the plugin, and submits it for
review. After approval, it is distributed via PedOS 1.1 Lumina. This design en-
sures pedagogical utility, enforces safety reviews, and captures research evidence
through explicit, controlled telemetry pathways.
arXiv:2607.09674v1  [cs.CY]  5 Jun 2026

2 N. Kadir
2 System Presentation
LearnAdapt Agentic Studio and PedOS 1.1 Lumina form a no-code authoring
and governed runtime pipeline.
Agentic Studiois the creator interface where an educator’s prompt acts as
aclientbriefforanagentdevelopmentteam.Theworkflowbeginswithdetermin-
istic preflight checks, followed by specialized agents handling pedagogy, UX, and
architecture in parallel. Next, build and evidence design occur simultaneously,
culminating in QA, preview iteration, and release packaging. This multi-agent
pipeline generates runtime PHP/JS/CSS artifacts that execute securely via plat-
form routing. Direct access is blocked, and creators preview interactions before
admin review.
Fig. 1.The LearnAdapt Agentic Studio authoring interface. Educators describe the
desired learning interaction in plain English, and the agentic pipeline generates a de-
ployable, governable plugin through transparent build stages.
Security and reviewforms the governance layer. Validation includes PHP
syntax, API boundaries, and static application security testing (SAST). Admin

Teacher-Built Teammates with Agentic Studio and PedOS 3
approval re-runs these checks before deployment, using SAST scores alongside
policy status.
PedOS 1.1 Luminais the runtime layer. Approved plugins are versioned
and surfaced in the Plugin Directory for users to preview, install, and access.
Strict runtime safeguards isolate plugin execution to prevent platform-wide fail-
ures.
T elemetry gatinglinks interaction to evidence. Preview modes use mock
telemetry. Events are persisted only for authenticated users running active, in-
stalled plugins via approved endpoints.
3 Demonstrated Functionality
The demo presents a full plugin lifecycle. An educator prompts Agentic Studio
for a science retrieval-practice plugin. After previewing the generated artifact,
they submit it. An admin reviewer inspects the artifact, preview, SAST score,
and policy status, then approves it. The Plugin Directory displays the deployed
package, allowing learners to install and use it. The installed plugin emits teleme-
try only through approved endpoints. This demonstrates how educators can cre-
ate bounded, inspectable AI interactions (e.g., misconception probes). Teachers
define pedagogical intent; Agentic Studio handles technical production; PedOS
governs distribution and evidence capture.
4 Originality, Maturity, and Future Work
The main contribution combines no-code AI authoring with enforceable educa-
tional governance. LearnAdapt unites prompt-based creation, SAST validation,
admin review, deployment, and gated telemetry into one workflow. The system
is validated across production paths, demonstrating prompt intake to secure
telemetry persistence. While this submission does not claim learning gains, its
contribution is a working system for teacher-authored AI. Next steps include a
June 2026 co-design workshop to study teachers’ prioritized plugin categories
and evidence requirements.
References
1. Holmes, W., Bialik, M., Fadel, C.: Artificial intelligence in education. Center for
Curriculum Redesign (2019)
2. Molenaar, I.: Towards hybrid human-AI learning technologies. European Journal of
Education 57(4), 632–645 (2022)
3. UNESCO: Guidance for generative AI in education and research. UNESCO Digital
Library (2023)
4. Zawacki-Richter, O., Marín, V.I., Bond, M., Gouverneur, F.: Systematic review of
research on artificial intelligence applications in higher education–where are the
educators? International Journal of Educational Technology in Higher Education
16(1), 1–27 (2019)
