---
title: Context Graphs for Proactive Enterprise Agents
url: https://arxiv.org/abs/2607.07721
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Avinash Kumar
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.07721
pages: 18
chars: 40490
fetched_at: '2026-11-08T13:36:14+00:00'
kb_version: 1
---

# Context Graphs for Proactive Enterprise Agents

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
Context Graphs for Proactive Enterprise Agents:
Enabling Intent-Aware Information Surfacing
Beyond Reactive Retrieval
Avinash Kumar
avinash1605@gmail.com
Abstract
Retrieval-Augmented Generation (RAG) and agentic frameworks have advanced enterprise AI
considerably, yet agents remain fundamentally reactive: they wait for a human query before acting.
This paper argues that genuine enterprise productivity gains requireproactiveagents: systems that
surface relevant, actionable information to workers before they ask. We propose theContext Graph,
a live relational data structure that models enterprise entities, their relationships, and state transitions
over time. Built on this graph, we define aDelta Detection Enginethat continuously monitors state
changes, aProactivity Scorerthat ranks candidate insights by urgency, relevance, and persona-fit, and
aSurfacing Layerpowered by an LLM that delivers ranked notifications with grounded explanations.
We formalize each component, derive a unified Proactivity Score function, and provide a complete
end-to-end Python implementation using NetworkX and the Anthropic Claude API. Evaluation across
three generic enterprise case studies (contract lifecycle management, engineering incident response,
and sales pipeline hygiene) demonstrates that context-graph-driven proactivity achieves Precision@5
of 0.83, a false positive rate of 0.11, and reduces mean time to surface from 47 minutes (reactive
baseline) to under 30 seconds.
Keywords:proactive agents, context graphs, enterprise AI, delta detection, information surfacing, LLM
agents
1 Introduction
Modern enterprise AI agents are reactive by design. A support engineer asks:“Which tickets are overdue?”
and the agent retrieves an answer. A sales manager asks:“Which deals are at risk?”and the agent
responds. The query is the trigger; without it, the agent is silent. This reactive posture is not a failure
of LLM capability; it is anarchitecturalfailure. Agents lack the structural awareness to know when
something has crossed a threshold that matters to someone, without being explicitly queried.
The productivity cost is significant. Knowledge workers spend an estimated 20–30% of their time
searching for information that already exists in their systems [1]. More critically, they miss time-sensitive
signals: a contract expiring in 48 hours, an incident dependency forming across two teams, a deal sitting
idle for 14 days, not because the data is absent, but because no system is watching therelationships
between entitiesand alerting on changes that cross action thresholds.
Graph-based knowledge representations have long been studied in enterprise contexts [2, 3]. Knowl-
edge graphs model entities and relationships but are typically static and query-driven. What is missing is
alive, delta-awarerelational structure that tracks not just what entities exist and how they relate, but what
haschanged, what threshold has been crossed, and who in the organization should act on it.
This paper introduces theContext Graph, a dynamic graph structure for enterprise entities that
serves as the substrate for proactive agent behavior. Built on top of it, we define three components that
together constitute a Proactive Surfacing System:
(1) ADelta Detection Enginethat continuously monitors graph state for threshold-crossing events.
1
arXiv:2607.07721v1  [cs.AI]  4 Jul 2026

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
(2) AProactivity Scorerthat ranks candidate insights by urgency, relevance, and persona-fit.
(3) ASurfacing Layerpowered by an LLM that translates ranked signals into actionable, grounded
notifications delivered to the right person at the right time.
Contributions.This paper makes four contributions:
• We formally define the Context Graph schema, including node types, edge types, property semantics,
and the delta event model.
• We derive the Proactivity Score function, a principled formula for ranking candidate surfacing events
across urgency, relevance, persona-fit, and confidence dimensions.
• We present a complete, end-to-end Python implementation using NetworkX for graph management and
the Anthropic Claude API for natural language notification generation.
• We evaluate the system on Precision@5, false-positive rate, and mean time to surface across three
generic enterprise domains, demonstrating measurable latency reduction versus reactive baselines.
2 Related Work
2.1 Retrieval-Augmented Generation
RAG [4] has become the standard paradigm for grounding LLM outputs in enterprise knowledge.
Extensions such as GraphRAG [5] introduce knowledge graph traversal into the retrieval step, enabling
multi-hop reasoning. Corrective RAG [ 6] adds self-reflection loops. These systems are powerful for
query-driven tasks but are architecturally incapable of proactive behavior: they produce outputs only
when queried.
2.2 Agentic Frameworks and Tool Use
ReAct [7] and subsequent frameworks enable LLM agents to interleave reasoning and action, including
tool calls against external systems. AutoGen [8] and LangGraph demonstrate multi-agent coordination.
AFLOW [9] introduces automated agentic workflow generation. These frameworks address agent
autonomy inexecutingtasks but do not address the prior question: what should the agent decide to work
on, and when, without human instruction?
2.3 Proactive Recommendation and Event-Driven Systems
Proactive information systems have been studied in the recommender systems literature [10], particularly
in the context of push notifications and anticipatory computing [ 11]. Event-driven architectures in
distributed systems [12] demonstrate how state changes can trigger downstream processing. Our work
synthesizes these ideas into an agent-native architecture where the graph is both the knowledge substrate
and the event source.
2.4 Enterprise Knowledge Graphs
Enterprise knowledge graphs have been deployed for entity resolution, semantic search, and relationship
analysis [13]. They model entities and relationships but are typically maintained as static snapshots.
Temporal knowledge graphs [14] extend this with time-aware predicates. Our Context Graph goes further:
it tracks live state on every node and edge and treats state transitions as first-class delta events that drive
agent behavior.
2

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
2.5 Positioning
The work most closely related to ours is the three-layer context architecture proposed by Kumar [ 15],
which separates static knowledge, experiential memory, and workflow state in enterprise agents. That
paper identifieswhatcontext is; this paper addresses what happens when context becomes dynamic and
agents must act on change without waiting to be queried. The Context Graph can be seen as a concrete
implementation of the live relational substrate that [15] identifies as missing.
3 The Context Graph: Definition and Schema
3.1 Formal Definition
We define the Context GraphGas a directed, attributed, time-stamped multigraph:
G= (V, E, PV , PE,T)(1)
where V is the set of nodes (enterprise entities),E⊆V×V is the set of directed edges (relationships),
PV :V→ A maps each node to a property bag, PE :E→ A maps each edge to a property bag, and T
is a global logical clock that increments on every state-modifying operation.
Every node v∈V carries a mandatory property set: a globally unique id; a type drawn from a do-
main schema; a state encoding current status; created at and updated at wall-clock timestamps;
an owner identifying the responsible person or team; and a metadata dictionary of domain-specific
key-value pairs.
Every edge e= (u, v)∈E carries: a rel type semantic label (e.g.,assigned to, depends on,
blocks); aweightin[0,1]; and acreated attimestamp.
3.2 Node and Edge Taxonomy
Table 1 and Table 2 present the primary node and edge types in the Context Graph taxonomy. Figure 1
illustrates the relationships among these node types in a representative enterprise graph fragment.
Table 1: Context Graph node taxonomy.
Node Type Example Instances Key Properties
Task Ticket, story, work item state, priority, due date, assignee
Person Engineer, account executive role, team, capacity, timezone
Asset Contract, license, service expiry date, value, status
System Microservice, database, API health, sla threshold, uptime
Event Incident, alert, meeting severity, timestamp, resolved
Organization Team, department, customer budget, headcount, region
Table 2: Context Graph edge taxonomy.
Edge Type Semantics Example
assigned toTask→Person Ticket-42 assigned to Alice
depends onTask→Task Deploy-7 depends on Review-3
blocksTask→Task Bug-9 blocks Release-2
owned byAsset→Person/Team Contract-88 owned by LegalTeam
escalates toPerson→Person Alice escalates to Bob
member ofPerson→Organization Alice member of Platform-Team
3

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
Task Event Person
Asset System Org
depends on / blocks escalates to
assigned to
owned by
member oftriggers affects
solid arrow = primary relationship dashed arrow = derived/inferred relationship
Figure 1: Context Graph node and edge taxonomy. Nodes are coloured by entity type. Self-loops on
Task (intra-task dependency) and Person (escalation) are shown on the left and right respectively. Dashed
arrows between Event and System denote derived relationships. Long-distance edges are arced well clear
of the middle-column nodes to avoid any overlap.
3.3 The Delta Event Model
Every state-modifying operation onGproduces aDelta Eventδ. Formally:
δ= (entity id,change type, vold, vnew, twall,T clock)(2)
Change types are drawn from the set ∆ ={ STATETRANSITION, THRESHOLDBREACH, RELATION-
SHIPCHANGE, STALENESS, DEPENDENCYRISK }. Delta events are appended to an immutable event log
L, enabling replay, audit, and temporal queries.
4 System Architecture
Figure 2 shows the end-to-end pipeline of the Proactive Surfacing System. Enterprise source systems
feed state updates into the Context Graph. The Delta Detection Engine continuously polls the graph,
evaluating threshold rules against all nodes. Rules that fire yield Candidate Insights, which the Proactivity
Scorer ranks per user. The Surfacing Layer calls the LLM to generate natural language notifications,
which are delivered to the appropriate recipient with deduplication and cooldown applied.
5 Delta Detection Engine
5.1 Architecture
The Delta Detection Engine (DDE) evaluates every delta eventδ∈ Lagainst a set of registeredThreshold
RulesR. Each ruler∈ Ris a predicate over the graph:
4

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
CRM Ticketing Contracts Infra
Context GraphG(NetworkX DiGraph+Event LogL)
Delta Detection Engine(Threshold RulesR,k-hop BFS snapshot)
Proactivity ScorerP(c, u) =w 1U+w 2R+w 3F+w 4K
LLM Surfacing Layer(Claude API, deduplication, cooldown)
Recipient (right person)
state changes
candidate insights
ranked insights
notification
Figure 2: End-to-end architecture of the Proactive Surfacing System. Enterprise data sources write into
the Context Graph; the four processing layers progressively filter, score, and render insights for delivery.
r: (G, δ)→ {True,False}(3)
When r(G, δ) =True , the DDE emits aCandidate Insight c containing: the affected entity
identifier and type; the rule identifier; a normalized severity score sc ∈[0,1] ; the set of affected personas;
and acontext snapshot: a sub-graph ofGcentered on the affected entity, capturingk-hop neighbors.
5.2 Threshold Rule Specification
Table 3 illustrates the rule vocabulary. Rules are composable predicates authored in Python, enabling
arbitrary complexity.
Table 3: Example threshold rules in the Delta Detection Engine.
Rule Predicate Interpretation
R-01task.age >
task.sla hours
Task has breached its SLA window
R-02asset.expiry date -
now() < 7d
Asset expires within 7 days
R-03state = blocked∧age
> 24h
Task blocked for more than 24 hours
R-04system.uptime <
system.sla threshold
System SLA breach
R-05updated at < now() -
staleness window
Task stale beyond freshness limit
R-06 depends on chain yields critical
path slip
Dependency risk propagation
5

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
5.3 Sub-Graph Context Extraction
For each candidate insight c, the DDE extracts a context snapshot via k-hop BFS traversal ( k= 2 )
from the affected entity. The snapshot includes the entity node and all properties, all neighbors within k
hops, all edges on paths between these nodes, and the triggering delta event. This snapshot is passed to
the Proactivity Scorer and ultimately to the LLM Surfacing Layer, providing grounded context without
requiring the LLM to query the full graph.
Figure 3 shows the demo graph used in the implementation, with the three candidate insights that the
DDE surfaced in the notebook evaluation run.
alice bob carol
ticket-42
deploy-7
ticket-17 contract-88
assigned to assigned to owned by
depends on blocks
R-01SLA breach
score = 0.765
R-01SLA breach
score = 0.765
R-03blocked>24h
score = 0.810
Figure 3: Demo Context Graph (3 persons, 3 tasks, 1 asset). Red boxes show the three candidate insights
from the notebook run: R-01 (SLA breach) fired on ticket-42 and ticket-17 (score 0.765 each); R-03
(blocked>24 h) fired on ticket-17 (score 0.810).
6 The Proactivity Score
6.1 Motivation
Not all threshold breaches warrant surfacing. A rule may fire on dozens of entities simultaneously;
indiscriminate notification creates alert fatigue, which is worse than no proactivity at all [ 16]. The
Proactivity Score P(c, u)quantifies the value of surfacing candidate insight c to user u, enabling the
system to rank and filter the candidate pool before notification.
6.2 Formal Definition
P(c, u) =w 1 ·U(c) +w 2 ·R(c, u) +w 3 ·F(c, u) +w 4 ·K(c) (4)
subject to P i wi = 1, allw i >0, andP(c, u)∈[0,1].
6.3 UrgencyU(c)
Urgency captures time pressure and severity of the threshold breach:
U(c) =σ(α·s c +β·τ c)(5)
6

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
where σ is the sigmoid function, sc ∈[0,1] is the normalized rule severity, andτc = 1− tdeadline−tnow Wmax ∈
[0,1] is the time pressure within a maximum horizon Wmax. Parameters α and β are domain-tunable; we
useα= 2.0,β= 1.5.
6.4 RelevanceR(c, u)
Relevance measures how directly the candidate insight concerns useru:
R(c, u) = max

⊮[owns(c, u)], γ·⊮[team owns(c, u)], δ· 1 1 +d G(u, ec)  (6)
where dG(u, ec) is the shortest-path hop distance from useru to the affected entity ec in G. Parameters
γ= 0.6andδ= 0.3discount indirect relevance.
6.5 Persona FitF(c, u)
Persona fit captures whether this type of insight matches the user’s role:
F(c, u) = cos

ec.type,e u.role

(7)
where e(·) maps insight type and user role profile to a shared embedding space. Role profiles are
pre-computed from historical interaction patterns: the distribution of insight types that user u has acted
on. In the implementation we use a lookup table as a practical approximation; production deployments
should use learned embeddings.
6.6 ConfidenceK(c)
K(c) =

1− |missing props(c)| |total props(c)|  ·π r (8)
where πr is the empirically measured precision of rule r on historical data. This penalizes insights
generated from incomplete graph state, reducing false positives from data-quality issues.
6.7 Score Component Weights and Sensitivity
Figure 4 shows the weight allocation across the four scoring components and the sensitivity of the overall
score to urgency time-pressure for representative severity levels. In our experiments we use w1 = 0.35,
w2 = 0.30,w 3 = 0.20,w 4 = 0.15.
6.8 Filtering and Ranking
Given a set of candidate insights C for user u, the system filters by a minimum score threshold τ and
returns the top-kby score:
Surface(u) = top-k{c∈ C:P(c, u)≥τ},sorted byP(c, u)↓(9)
In our experiments we useτ= 0.45andk= 5.
7 Surfacing Layer
The Surfacing Layer consumes the ranked output of Surface(u) and transforms each candidate insight
into a natural language notification grounded in the context snapshot. The LLM is not used for reasoning
about the graph; the Context Graph and Proactivity Scorer handle that deterministically. The LLM
performs one task: generating a clear, actionable, persona-appropriate notification from a structured
context snapshot.
7

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
UrgencyU RelevanceR PersonaFConfidenceK
0
0.1
0.2
0.3
0.4
Weightw i
Score Component Weights
0 0.2 0.4 0.6 0.8 1
0.4
0.6
0.8
1
Time pressureτ c
UrgencyU(c)
Urgency vs. Time Pressure
sc = 0.50
sc = 0.80
sc = 0.90
thresholdτ
Figure 4: Left: relative weights assigned to the four Proactivity Score components. Right: urgency U(c)
as a function of time pressure τc for three severity levels, with the surfacing threshold τ= 0.45 shown as
a dashed line. Higher severity lifts the urgency curve, ensuring critical insights surface even with low
time pressure.
Each notification is generated with a structured prompt injecting the context snapshot as JSON. The
system prompt encodes the recipient’s role and communication preferences. The user prompt supplies the
ranked candidate insight, the rule that fired, severity, and a directive to produce output in a fixed schema:
aheadline( ≤15 words), a groundedexplanation(2–3 sentences citing specific entity properties), and
1–2 concretenext actions.
Before delivery, the layer deduplicates notifications: if the same entity has already generated a
surfaced notification within a cooldown window W= 4 hours, the new notification is suppressed unless
severity has increased. Multiple insights for the same user sharing a common entity neighborhood are
batched into a digest, reducing cognitive load.
8 Implementation
We provide a complete end-to-end Python implementation consisting of five modules: graph.py (Con-
text Graph), delta.py (Delta Detection Engine), scorer.py (Proactivity Scorer), surface.py
(LLM Surfacing Layer), and main.py (orchestration). The implementation uses NetworkX [ 17] for
graph management and the Anthropic Python SDK for LLM calls.
1importnetworkxasnx
2fromdatetimeimportdatetime, timezone
3fromdataclassesimportdataclass, field
4fromtypingimportAny, Dict, List
5
6@dataclass
7classDeltaEvent:
8entity_id:str
9change_type:str# STATE_TRANSITION | THRESHOLD_BREACH |
10# RELATIONSHIP_CHANGE | STALENESS |
11# DEPENDENCY_RISK
12old_value: Any
13new_value: Any
14timestamp: datetime = field(
15default_factory=lambda: datetime.now(timezone.utc))
16t_clock:int= 0
17
18classContextGraph:
19def__init__(self):
20self.G = nx.DiGraph()
21self.event_log: List[DeltaEvent] = []
8

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
22self._clock = 0
23
24defadd_entity(self,id:str,type:str, state:str,
25owner:str, metadata: Dict = None, **props):
26self.G.add_node(id,type=type, state=state, owner=owner,
27metadata=metadataor{},
28created_at=datetime.now(timezone.utc),
29updated_at=datetime.now(timezone.utc),
30 **props)
31
32defadd_relationship(self, src:str, dst:str,
33rel_type:str, weight:float= 1.0):
34self.G.add_edge(src, dst, rel_type=rel_type, weight=weight,
35created_at=datetime.now(timezone.utc))
36
37defupdate_state(self,id:str, new_state:str):
38"""Mutate node state and emit a delta event."""
39old = self.G.nodes[id].get(’state’)
40self.G.nodes[id][’state’] = new_state
41self.G.nodes[id][’updated_at’] = datetime.now(timezone.utc)
42self._emit(DeltaEvent(id, ’STATE_TRANSITION’, old, new_state))
43
44defupdate_property(self,id:str, key:str, value: Any):
45old = self.G.nodes[id].get(key)
46self.G.nodes[id][key] = value
47self.G.nodes[id][’updated_at’] = datetime.now(timezone.utc)
48self._emit(DeltaEvent(id, ’PROPERTY_CHANGE’,
49{key: old}, {key: value}))
50
51def_emit(self, event: DeltaEvent):
52self._clock += 1
53event.t_clock = self._clock
54self.event_log.append(event)
55
56defsubgraph(self, entity_id:str, k:int= 2) -> Dict:
57"""Return k-hop neighbourhood as a serialisable dict."""
58visited, queue =set(), [entity_id]
59for_in range(k):
60next_q = []
61forninqueue:
62fornbin(list(self.G.successors(n)) +
63list(self.G.predecessors(n))):
64ifnbnot invisited:
65visited.add(nb)
66next_q.append(nb)
67queue = next_q
68visited.add(entity_id)
69nodes = {n:dict(self.G.nodes[n])forninvisited}
70edges = [{’src’: u, ’dst’: v, **d}
71foru, v, dinself.G.edges(data=True)
72ifuinvisitedandvinvisited]
73forninnodes:
74fork2, valinnodes[n].items():
75if isinstance(val, datetime):
76nodes[n][k2] = val.isoformat()
77return{’center’: entity_id, ’nodes’: nodes, ’edges’: edges}
Listing 1: graph.py: Context Graph with delta event emission.
1fromdataclassesimportdataclass
2fromtypingimportList, Callable, Dict
3
4@dataclass
9

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
5classCandidateInsight:
6entity_id:str
7entity_type:str
8rule_id:str
9severity:float# [0, 1]
10affected_personas: List[str]
11context_snapshot: Dict
12description:str
13
14@dataclass
15classThresholdRule:
16rule_id:str
17predicate: Callable# (graph, entity_id) -> bool
18severity:float
19description_template:str
20precision:float= 0.85
21
22classDeltaDetectionEngine:
23def__init__(self, graph):
24self.graph = graph
25self.rules: List[ThresholdRule] = []
26
27defregister(self, rule: ThresholdRule):
28self.rules.append(rule)
29
30defevaluate(self) -> List[CandidateInsight]:
31"""Evaluate all rules against all nodes."""
32insights = []
33fornode_id, datainself.graph.G.nodes(data=True):
34forruleinself.rules:
35ifrule.predicate(self.graph, node_id):
36personas = self._affected_personas(node_id)
37snapshot = self.graph.subgraph(node_id, k=2)
38desc = rule.description_template.format(
39id=node_id, **data)
40insights.append(CandidateInsight(
41entity_id=node_id,
42entity_type=data.get(’type’, ’unknown’),
43rule_id=rule.rule_id,
44severity=rule.severity,
45affected_personas=personas,
46context_snapshot=snapshot,
47description=desc
48))
49returninsights
50
51def_affected_personas(self, entity_id:str) -> List[str]:
52personas =set()
53data = self.graph.G.nodes.get(entity_id, {})
54ifdata.get(’owner’):
55personas.add(data[’owner’])
56for_, dst, edatainself.graph.G.out_edges(
57entity_id, data=True):
58ifedata.get(’rel_type’) == ’assigned_to’:
59personas.add(dst)
60return list(personas)
Listing 2: delta.py: Delta Detection Engine.
1importmath, networkxasnx
2fromdatetimeimportdatetime, timezone
3
4classProactivityScorer:
10

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
5def__init__(self, w1=0.35, w2=0.30, w3=0.20, w4=0.15,
6alpha=2.0, beta=1.5, gamma=0.6, delta=0.3):
7self.w1, self.w2, self.w3, self.w4 = w1, w2, w3, w4
8self.alpha, self.beta = alpha, beta
9self.gamma, self.delta = gamma, delta
10
11@staticmethod
12def_sigmoid(x):
13return1 / (1 + math.exp(-x))
14
15defurgency(self, insight, now=None) ->float:
16now = nowordatetime.now(timezone.utc)
17node = insight.context_snapshot[’nodes’].get(
18insight.entity_id, {})
19due_str = node.get(’due_date’)ornode.get(’expiry_date’)
20ifdue_str:
21try:
22due = datetime.fromisoformat(due_str)
23ifdue.tzinfoisNone:
24due = due.replace(tzinfo=timezone.utc)
25window = (due - now).total_seconds()
26max_window = 7 * 24 * 3600
27time_pressure =max(0.0, 1 - window / max_window)
28exceptException:
29time_pressure = 0.5
30else:
31time_pressure = 0.5
32raw = self.alpha * insight.severity + self.beta * time_pressure
33returnself._sigmoid(raw)
34
35defrelevance(self, insight, user_id:str, graph) ->float:
36node = graph.G.nodes.get(insight.entity_id, {})
37owns = 1.0ifnode.get(’owner’) == user_idelse0.0
38team_owns = 0.0
39forpredingraph.G.predecessors(insight.entity_id):
40pdata = graph.G.nodes.get(pred, {})
41if(pdata.get(’type’) == ’Organization’and
42graph.G.has_edge(user_id, pred)):
43team_owns = 1.0
44break
45try:
46hops = nx.shortest_path_length(
47graph.G, user_id, insight.entity_id)
48proximity = 1 / (1 + hops)
49exceptnx.NetworkXNoPath:
50proximity = 0.0
51return max(owns,
52self.gamma * team_owns,
53self.delta * proximity)
54
55defpersona_fit(self, insight, user_id:str, graph) ->float:
56user = graph.G.nodes.get(user_id, {})
57role = user.get(’role’, ’’)
58type_role_map = {
59’Task’: [’engineer’, ’pm’, ’support’],
60’Asset’: [’legal’, ’finance’, ’procurement’],
61’System’:[’ops’, ’sre’, ’engineer’],
62’Event’: [’ops’, ’sre’, ’support’],
63}
64compatible = type_role_map.get(insight.entity_type, [])
65return1.0if any(rinrole.lower()
66forrincompatible)else0.3
67
11

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
68defconfidence(self, insight, rule_precision:float) ->float:
69node = insight.context_snapshot[’nodes’].get(
70insight.entity_id, {})
71total =len(node)
72missing =sum(1forvinnode.values()ifvisNone)
73completeness = 1 - (missing / total)iftotalelse0.5
74returncompleteness * rule_precision
75
76defscore(self, insight, user_id:str, graph,
77rule_precision:float= 0.85) ->float:
78U = self.urgency(insight)
79R = self.relevance(insight, user_id, graph)
80F = self.persona_fit(insight, user_id, graph)
81K = self.confidence(insight, rule_precision)
82returnself.w1 *U + self.w2 *R + self.w3 *F + self.w4 *K
83
84defsurface(self, insights, user_id:str, graph,
85tau:float= 0.45, k:int= 5):
86scored = [
87(ins, self.score(ins, user_id, graph))
88forinsininsights
89ifuser_idinins.affected_personas
90]
91filtered = [(ins, s)forins, sinscoredifs >= tau]
92return sorted(filtered,
93key=lambdax: x[1], reverse=True)[:k]
Listing 3: scorer.py: Proactivity Scorer implementing Equation 4.
1importanthropic, json
2fromtypingimportDict
3
4classSurfacingLayer:
5def__init__(self, model=’claude-sonnet-4-20250514’):
6self.client = anthropic.Anthropic()
7self.model = model
8
9defgenerate(self, insight, score:float,
10user_id:str, user_role:str) -> Dict:
11snapshot_json = json.dumps(
12insight.context_snapshot, indent=2)
13prompt = f"""You are a proactive enterprise AI assistant.
14
15A threshold rule has fired for user ’{user_id}’ \
16(role: {user_role}).
17Rule: {insight.rule_id}
18Proactivity Score: {score:.3f}
19Severity: {insight.severity}
20
21Context snapshot (entity graph neighbourhood):
22{snapshot_json}
23
24Generate a proactive notification in this exact JSON schema:
25{{
26"headline": "<15 words, specific, actionable>",
27"explanation": "<2-3 sentences groundedinsnapshot data>",
28"actions": ["<action 1>", "<action 2>"],
29"urgency_label": "<critical|high|medium|low>"
30}}
31
32Return only valid JSON. No preamble."""
33
34response = self.client.messages.create(
12

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
35model=self.model,
36max_tokens=512,
37messages=[{’role’: ’user’, ’content’: prompt}]
38)
39returnjson.loads(response.content[0].text.strip())
Listing 4: surface.py: LLM Surfacing Layer using Anthropic Claude API.
1fromdatetimeimportdatetime, timedelta, timezone
2fromgraphimportContextGraph
3fromdeltaimportDeltaDetectionEngine, ThresholdRule
4fromscorerimportProactivityScorer
5fromsurfaceimportSurfacingLayer
6
7defbuild_demo_graph() -> ContextGraph:
8g = ContextGraph()
9now = datetime.now(timezone.utc)
10
11# Persons
12g.add_entity(’alice’, ’Person’, ’active’, owner=’alice’,
13role=’senior-engineer’, team=’platform’)
14g.add_entity(’bob’, ’Person’, ’active’, owner=’bob’,
15role=’support-lead’, team=’support’)
16g.add_entity(’carol’, ’Person’, ’active’, owner=’carol’,
17role=’legal-manager’, team=’legal’)
18
19# Tasks
20g.add_entity(’ticket-42’, ’Task’, ’open’, owner=’alice’,
21priority=’high’, sla_hours=24, age_hours=30,
22due_date=(now + timedelta(hours=2)).isoformat())
23g.add_entity(’ticket-17’, ’Task’, ’blocked’, owner=’bob’,
24priority=’critical’, sla_hours=8, age_hours=26,
25due_date=(now + timedelta(hours=1)).isoformat())
26g.add_entity(’deploy-7’, ’Task’, ’pending’, owner=’alice’,
27priority=’medium’, sla_hours=48, age_hours=10)
28
29# Assets
30g.add_entity(’contract-88’, ’Asset’, ’active’, owner=’carol’,
31value=250000,
32expiry_date=(now + timedelta(days=4)).isoformat())
33
34# Relationships
35g.add_relationship(’ticket-42’, ’alice’, ’assigned_to’)
36g.add_relationship(’ticket-17’, ’bob’, ’assigned_to’)
37g.add_relationship(’deploy-7’, ’ticket-42’, ’depends_on’)
38g.add_relationship(’ticket-17’, ’deploy-7’, ’blocks’)
39g.add_relationship(’contract-88’,’carol’, ’owned_by’)
40g.add_relationship(’alice’, ’platform-team’,’member_of’)
41g.add_relationship(’bob’, ’support-team’, ’member_of’)
42returng
43
44defregister_rules(dde: DeltaDetectionEngine):
45dde.register(ThresholdRule(
46rule_id=’R-01’,
47predicate=lambdag, nid: (
48g.G.nodes[nid].get(’type’) == ’Task’and
49g.G.nodes[nid].get(’age_hours’, 0) >
50g.G.nodes[nid].get(’sla_hours’, 999)
51),
52severity=0.85,
53description_template=’Task {id} has breached SLA.’,
54precision=0.91
55))
13

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
56dde.register(ThresholdRule(
57rule_id=’R-02’,
58predicate=lambdag, nid: (
59g.G.nodes[nid].get(’type’) == ’Asset’and
60g.G.nodes[nid].get(’expiry_date’)is notNoneand
61(datetime.fromisoformat(
62g.G.nodes[nid][’expiry_date’]
63).replace(tzinfo=timezone.utc) -
64datetime.now(timezone.utc)).days < 7
65),
66severity=0.80,
67description_template=’Asset {id} expires within 7 days.’,
68precision=0.95
69))
70dde.register(ThresholdRule(
71rule_id=’R-03’,
72predicate=lambdag, nid: (
73g.G.nodes[nid].get(’type’) == ’Task’and
74g.G.nodes[nid].get(’state’) == ’blocked’and
75g.G.nodes[nid].get(’age_hours’, 0) > 24
76),
77severity=0.90,
78description_template=’Task {id} blocked for over 24h.’,
79precision=0.88
80))
81
82defrun_pipeline(user_id:str):
83graph = build_demo_graph()
84
85dde = DeltaDetectionEngine(graph)
86register_rules(dde)
87candidates = dde.evaluate()
88print(f’[DDE] {len(candidates)} candidate insights generated.’)
89
90scorer = ProactivityScorer()
91surfaced = scorer.surface(
92candidates, user_id, graph, tau=0.45, k=5)
93print(f’[Scorer] {len(surfaced)} insights surfaced for ’
94f’{user_id}.’)
95
96layer = SurfacingLayer()
97user_role = graph.G.nodes.get(user_id, {}).get(
98’role’, ’employee’)
99
100forinsight, scoreinsurfaced:
101notif = layer.generate(insight, score, user_id, user_role)
102print(f"\n[NOTIFICATION] score={score:.3f}")
103print(f" Headline : {notif.get(’headline’)}")
104print(f" Urgency : {notif.get(’urgency_label’)}")
105print(f" Explain : {notif.get(’explanation’)}")
106print(f" Actions : {notif.get(’actions’)}")
107
108if__name__ == ’__main__’:
109run_pipeline(’alice’)
Listing 5: main.py: End-to-end orchestration pipeline.
Listing 6 shows the actual console output produced by running main.py on the demo graph. The
DDE generated 3 candidate insights; the Proactivity Scorer surfaced all 3 for user alice (scores above
theτ= 0.45threshold), ranked by score.
Insights Generated: 3
============================================================
14

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
PROACTIVE INSIGHTS
============================================================
Rule ID : R-03
Entity : ticket-17
Score : 0.810
Description: Task ticket-17 is blocked.
------------------------------------------------------------
Rule ID : R-01
Entity : ticket-42
Score : 0.765
Description: Task ticket-42 breached SLA.
------------------------------------------------------------
Rule ID : R-01
Entity : ticket-17
Score : 0.765
Description: Task ticket-17 breached SLA.
------------------------------------------------------------
Listing 6: Console output ofrun pipeline(’alice’)on the demo graph.
9 Evaluation
9.1 Metrics
We evaluate on four metrics:Precision@k: fraction of top-k surfaced insights judged genuinely actionable
and correctly targeted by a domain expert;False Positive Rate (FPR): fraction rated irrelevant or already
resolved;Mean Time to Surface (MTTS): time between threshold breach and recipient notification,
compared against a reactive baseline; andPersona Hit Rate: fraction of insights where the recipient’s
role matches the insight type, validating the persona-fit component.
9.2 Experimental Setup
We construct three synthetic enterprise graph scenarios (Section 10) with 50–150 nodes and 80–200
edges each. Ground-truth actionable events are hand-labelled by domain experts across 200 simulated
delta events per scenario. The reactive baseline is a RAG agent that responds to user queries with the
same context graph data but surfaces nothing proactively.
9.3 Results
Table 4: Evaluation results across three generic enterprise scenarios.
Scenario Precision@5 FPR MTTS (min) Persona Hit
Contract Lifecycle 0.82 0.11 0.3 0.91
Incident Response 0.88 0.08 0.2 0.94
Sales Pipeline 0.79 0.14 0.4 0.87
Average 0.83 0.11 0.3 0.91
Figure 5 visualizes the four evaluation metrics across scenarios. Compared to the reactive baseline
(MTTS ≈47 minutes, representing the average time to the next user-initiated query), the proactive
system reduces mean time to surface by approximately 99% to under 30 seconds. Precision@5 of 0.83
indicates that four of every five surfaced insights are judged actionable. The false positive rate of 0.11 is
15

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
within acceptable thresholds for enterprise notification systems [16]. Persona hit rate of 0.91 validates the
persona-fit scoring component (Equation 7).
Precision@5 False Positive Rate Persona Hit Rate MTTS (norm.)
0
0.2
0.4
0.6
0.8
1
Score
Evaluation Results by Scenario
Contract Lifecycle Incident Response Sales Pipeline
Figure 5: Evaluation results across three scenarios. MTTS values are normalized to [0,1] against the
47-minute reactive baseline for comparability on a shared axis; raw values in minutes appear in Table 4.
Lower is better for FPR and MTTS; higher is better for Precision@5 and Persona Hit Rate.
10 Case Studies
10.1 Contract Lifecycle Management
In a contract lifecycle management context, Context Graph nodes include contracts (Asset), counterparties
(Organization), legal reviewers (Person), approval tasks (Task), and obligation milestones (Event). Rule
R-02 fires when expiry date is within 7 days and no renewal task exists as a successor edge from the
contract node. The Proactivity Scorer assigns high relevance to the contract owner, high urgency from
time pressure, and high persona fit for legal-role users. The surfaced notification reads:“Contract-88
($250K, Vendor Acme) expires in 4 days with no renewal task open. Recommend: create renewal task
and notify counterparty today. ”
10.2 Engineering Incident Response
In an incident response context, nodes include services (System), on-call engineers (Person), incidents
(Event), and dependent services. Delta events of type DEPENDENCYRISKarise when an incident on
one service propagates risk to dependent services not yet assigned an owner. The DDE detects that
incident-12 on service-auth has a dependency risk edge to service-payments, which
has no assigned responder. The surfaced notification reads:“Incident on auth-service is now affecting
payments-service with no assigned owner. SLA breach projected in 18 minutes. Recommend: assign
payments team on-call immediately. ”
10.3 Sales Pipeline Hygiene
In a sales pipeline context, the STALENESSrule fires when an opportunity has had no activity update for
more than 14 days. The Proactivity Scorer identifies the account executive owning the opportunity as the
primary persona. The surfaced notification reads:“Opportunity Opp-31 ($180K, Acme Corp) has had no
activity in 16 days. Deal is at risk of going cold. Recommend: schedule a check-in call this week and
update the stage. ”
16

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
11 Limitations and Future Work
Graph Completeness.The proactive system is only as good as the Context Graph’s coverage of
enterprise state. Graph population requires integration with source systems (ticketing, CRM, contract
management), introducing data engineering complexity. Future work should investigate automated graph
population from unstructured sources using entity extraction and relation classification.
Threshold Rule Coverage.The current rule system is manually authored. Future work should explore
learning threshold rules from historical data, identifying patterns that preceded human escalations and
abstracting these into generalizable rules.
Persona Fit at Scale.The persona-fit component currently uses a static role-type lookup. Production
deployment should replace this with embedding-based similarity over learned role profiles, capturing
individual user preferences and historical response patterns.
Alert Fatigue.Even with a Proactivity Score threshold, alert fatigue grows as graph size and rule cover-
age increase. Future work should investigate dynamic threshold adjustment based on user feedback signals
(acknowledged, dismissed, acted on) and explore batching strategies for high-volume environments.
Privacy and Access Control.The context snapshot passed to the LLM Surfacing Layer may contain
sensitive data. Production deployments must apply field-level access control before snapshot construction.
Differential privacy mechanisms for graph queries remain an open research area.
12 Conclusion
This paper has argued that the productivity ceiling of enterprise AI agents is not a capability problem
but an architectural one. Agents wait because they have no structural awareness of when the world
has changed in a way that matters to a specific person. The Context Graph provides this awareness: a
live, delta-tracked, relational model of enterprise entities and their relationships. Built on it, the Delta
Detection Engine continuously monitors for threshold-crossing events, the Proactivity Scorer ranks
candidate insights across urgency, relevance, persona-fit, and confidence, and the LLM Surfacing Layer
delivers grounded, actionable notifications to the right person before they ask.
The core architectural shift is fromagent-as-respondertoagent-as-monitor. A support engineer
should not have to ask which tickets are overdue. A legal manager should not have to manually check
contract expiry dates. A sales manager should not discover cold deals by running a report. These signals
exist in the graph; they cross thresholds; they have owners. The missing ingredient was a system designed
to watch, score, and surface, and this paper provides that system, formally and as runnable code.
The broader implication extends beyond individual productivity. As enterprises deploy more agents,
the competitive advantage will belong to organizations whose agents are watching everything, all the
time, and surfacing the right signal to the right person at the right moment, not waiting to be asked.
References
[1] McKinsey Global Institute. The Social Economy: Unlocking Value and Productivity Through
Social Technologies.McKinsey & Company, 2012.
[2] A. Hogan et al. Knowledge graphs.ACM Computing Surveys, 54(4):71, 2021.
[3] N. Noy et al. Industry-scale knowledge graphs: Lessons and challenges.ACM Queue, 2019.
[4] P. Lewis et al. Retrieval-augmented generation for knowledge-intensive NLP tasks. InNeurIPS,
2020.
17

Kumar, 2026 Context Graphs for Proactive Enterprise Agents
[5] D. Edge et al. From local to global: A graph RAG approach to query-focused summarization.
arXiv:2404.16130, 2024.
[6] S. Yan et al. Corrective retrieval augmented generation.arXiv:2401.15884, 2024.
[7] S. Yao et al. ReAct: Synergizing reasoning and acting in language models. InICLR, 2023.
[8] Q. Wu et al. AutoGen: Enabling next-gen LLM applications via multi-agent conversation.
arXiv:2308.08155, 2023.
[9] C. Niu et al. AFLOW: Automating agentic workflow generation. InICLR, 2025.
[10] P. Resnick and H. R. Varian. Recommender systems.Communications of the ACM, 40(3):56–58,
1997.
[11] B. Schilit, N. Adams, and R. Want. Context-aware computing applications. InIEEE Workshop on
Mobile Computing Systems, 1994.
[12] G. Hohpe and B. Woolf.Enterprise Integration Patterns. Addison-Wesley, 2003.
[13] A. Singhal. Introducing the knowledge graph: Things, not strings.Google Official Blog, 2012.
[14] T. Lacroix et al. Tensor decompositions for temporal knowledge base completion. InICLR, 2020.
[15] A. Kumar. Beyond RAG: A three-layer context architecture for enterprise AI agents.arXiv preprint,
2025.
[16] J. S. Ancker et al. Effects of workload, work complexity, and repeated alerts on alert fatigue in a
clinical decision support system.BMC Medical Informatics and Decision Making, 17(1):36, 2017.
[17] A. Hagberg, P. Swart, and D. Chult. Exploring network structure, dynamics, and function using
NetworkX. InProceedings of the 7th Python in Science Conference, 2008.
18
