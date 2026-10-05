# G4 — Situational Awareness for Autonomous Marketing Agents
## Working Title: Context-Aware Agentic Marketing (CAM): A Framework for Situational Awareness in Autonomous Marketing Systems

> **File:** `g4_situational_awareness_framework.md`  
> **Status:** DRAFT (v0.2)  
> **Gap:** G4 (Situational Awareness for Autonomous Marketing Agents)  
> **Priority:** #1 (Weighted Score: 4.75/5.0)  
> **Lead Authors:** Tobias Weiss (proposed) + [TBD co-authors]  
> **Target Venues:** *Marketing Science*, *Journal of Marketing* (JM), RaAM 2027, MKTG Workshop  
> **Last Updated:** 2026-08-29  

---

## 🎯 Executive Summary

**Problem:** Agentic marketing systems can plan and execute, but **cannot understand marketing context** (audience situation, channel journey, moment-of-truth) — the corpus has **61 agentic papers** but **only 2** connect agentic with contextual understanding.

**Solution:** **Context-Aware Agentic Marketing (CAM)** — a framework that gives autonomous marketing agents **situational awareness** by:
1. **Sensing Layer** — real-time ingestion of multi-modal marketing context signals
2. **Context Model** — unified representation (JSON-schema + vector embeddings + graph models)
3. **Awareness Engine** — reasoning algorithms (neuro-symbolic hybrid: rules + ML classifiers)
4. **Action Layer** — context-conditioned marketing actions (messaging, bid adj., channel selection)

**Novelty:** First framework connecting **agentic AI** (corpus trend: 1.79x burst) with **marketing situational awareness** (corpus: 0 papers).

**Product Synergy:** Directly implements the **contextual-intelligence.org** product architecture.

---

## 📊 Corpus Evidence

### The Agentic Explosion
From `papers.yaml` (7,778 papers):
- **Agentic:** 61 papers total | **41 in 2024-2026** | **Burst: 1.79x** | **July 2026: 12 papers**
- **World Model:** 1 paper  
- **Simulation:** 48 papers  
- **Autonomous:** 53 papers  

### The Contextual Vacuum
| Keyword | Total | 2024-2026 | Combined with "agentic" |
|---------|-------|-----------|------------------------|
| contextual | 44 | 32 | **2** |
| context-aware | 3 | 2 | **0** |
| situational | 4 | 4 | **0** |
| intent | 823 | 598 | **0** |

**The intersection is essentially empty.**

### Cross-Cell White Space
- **analytics** + **contextual** + **agentic:** 0 papers
- **ai-marketing** + **agentic** + **framework:** 0 papers
- **omnichannel** + **agentic:** 0 papers

---

## Layer 2 Deep Dive: Context Model

### Purpose
Transform raw signals from Layer 1 into **structured, queryable, temporally-positive embedding** that represent.

### Schema Definition (JSON)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CAM Context Model",
  "description": "Unified representation of marketing context for agentic systems",
  "type": "object",
  "required": ["metadata", "audience", "channel", "temporal", "situational", "social"],
  "properties": {
    "metadata": {
      "type": "object",
      "properties": {
        "context_id": {"type": "string", "format": "uuid"},
        "timestamp": {"type": "string", "format": "date-time"},
        "version": {"type": "string"},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1}
      }
    },
    "audience": {
      "type": "object",
      "properties": {
        "intent_vector": {
          "type": "array",
          "items": {"type": "number"},
          "minItems": 768,
          "maxItems": 1024,
          "description": "Intent embedding (text-embedding-3-small)"
        },
        "intent_segments": {
          "type": "array",
          "items": {"type": "string"},
          "description": "High-probability intent categories"
        },
        "behavior_graph": {
          "type": "object",
          "description": "Graph representation of user path",
          "properties": {
            "nodes": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {"type": "string"},
                  "type": {"enum": ["page_view", "content_engagement", "purchase", "support"]},
                  "timestamp": {"type": "string", "format": "date-time"}
                }
              }
            },
            "edges": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "from": {"type": "string"},
                  "to": {"type": "string"},
                  "weight": {"type": "number"}
                }
              }
            }
          }
        },
        "preferences": {
          "type": "object",
          "additionalProperties": {"type": "number"},
          "description": "Preference scores by category"
        }
      }
    },
    "channel": {
      "type": "object",
      "properties": {
        "platform": {"type": "string", "enum": ["email", "web", "mobile", "social", "search", "display"]},
        "inventory_level": {"type": "number", "minimum": 0, "maximum": 1},
        "competitive_density": {"type": "number", "minimum": 0},
        "placement_quality": {"type": "number", "minimum": 0, "maximum": 1},
        "auction_data": {
          "type": "object",
          "properties": {
            "current_bid": {"type": "number"},
            "floor_price": {"type": "number"},
            "competitors": {"type": "integer"}
          }
        }
      }
    },
    "temporal": {
      "type": "object",
      "properties": {
        "timestamp": {"type": "string", "format": "date-time"},
        "time_of_day": {"type": "string", "enum": ["morning", "afternoon", "evening", "night"]},
        "day_of_week": {"type": "string", "enum": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]},
        "seasonality_vector": {
          "type": "array",
          "items": {"type": "number"},
          "minItems": 12,
          "maxItems": 12
        },
        "holidays": {
          "type": "array",
          "items": {"type": "string"}
        }
      }
    },
    "situational": {
      "type": "object",
      "properties": {
        "device": {
          "type": "object",
          "properties": {
            "type": {"type": "string", "enum": ["desktop", "mobile", "tablet", "tv"]},
            "os": {"type": "string"},
            "browser": {"type": "string"}
          }
        },
        "location": {
          "type": "object",
          "properties": {
            "country": {"type": "string"},
            "region": {"type": "string"},
            "city": {"type": "string"},
            "coordinates": {
              "type": "array",
              "items": {"type": "number"},
              "minItems": 2,
              "maxItems": 2
            }
          }
        },
        "network": {
          "type": "object",
          "properties": {
            "speed": {"type": "string", "enum": ["slow", "medium", "fast"]},
            "connection_type": {"type": "string", "enum": ["wifi", "cellular", "wired"]}
          }
        },
        "environment": {
          "type": "object",
          "properties": {
            "weather": {"type": "string"},
            "temperature": {"type": "number"},
            "local_events": {
              "type": "array",
              "items": {"type": "string"}
            }
          }
        }
      }
    },
    "social": {
      "type": "object",
      "properties": {
        "sentiment_vector": {
          "type": "array",
          "items": {"type": "number"},
          "minItems": 768,
          "maxItems": 1024
        },
        "sentiment_polarity": {"type": "number", "minimum": -1, "maximum": 1},
        "trending_topics": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "topic": {"type": "string"},
              "score": {"type": "number"}
            }
          }
        }
      }
    },
    "market": {
      "type": "object",
      "properties": {
        "competitor_prices": {
          "type": "object",
          "additionalProperties": {"type": "number"}
        },
        "macro_indicators": {
          "type": "object",
          "properties": {
            "stock_index": {"type": "number"},
            "industry_growth": {"type": "number"}
          }
        }
      }
    }
  }
}
```

### Implementation Notes

#### Embedding Strategy
| Entity | Model | Dimensions | Use Case |
|--------|-------|------------|----------|
| Intent | text-embedding-3-small | 1024 | Semantic intent understanding |
| Audience Behavior | Node2Vec on behavior graph | 128 | Path similarity |
| Context | unified-context-embedder | 1024 | Holistic context similarity |

#### Storage & Versioning
- **Database:** PostgreSQL with pgvector extension for vector storage
- **Scheme:** Append-only context audit log with TTL
- **Privacy:** All embeddings are conclusion
- **Retention:**
  - Real-time context: 24 hours
  - Session context: 30 days
  - Historical patterns: indefinite

---

## Layer 3 Deep Dive: Awareness Engine

### Purpose
Evaluate context relevance and trigger adaptive agent behavior through reasoning.

### Architecture Overview

```
┌───────────────────────────────────────────────────────────────┐
│                        Awareness Engine                        │
├─────────────────┬─────────────────┬─────────────────┬─────────┤
│  Context Scorer │ Situation       │ Context          │ Action   │
│                 │ Classifier      │ Predictor       │ Mapper   │
│ (Rule-based +   │ (ML Classifier) │ (LSTM/           │ (Rules)  │
│  ML hybrid)     │                 │  Transformer)   │          │
└─────────────────┴─────────────────┴─────────────────┴─────────┘
                              │
                              ▼
┌───────────────────────────────────────────────────────────────┐
│                    Decision Output                              │
│  - Relevance Score (0-100)                                     │
│  - Situation Type (explore/consider/decide/crisis/opportunity) │
│  - Predicted Next Context                                      │
│  - Recommended Action Set                                      │
└───────────────────────────────────────────────────────────────┘
```

### Component 1: Context Scorer

**Purpose:** Calculate overall context relevance score.

#### Scoring Algorithm
```python
def calculate_context_relevance(context: ContextModel, target_action: Action) -> float:
    # Weights (tunable parameters)
    weights = {
        'intent_alignment': 0.35,
        'temporal_alignment': 0.20,
        'channel_compatibility': 0.20,
        'audience_readiness': 0.15,
        'competitive_context': 0.10
    }
    
    # Intent alignment: cosine similarity between action intent and audience intent
    intent_score = cosine_similarity(
        target_action.intent_embedding,
        context.audience.intent_vector
    )
    
    # Temporal alignment: is now within optimal window?
    temporal_score = temporal_compatibility(
        target_action.optimal_time_window,
        context.temporal
    )
    
    # Channel compatibility: rule-based + ML
    channel_score = channel_compatibility(
        target_action.required_channel_type,
        context.channel.platform,
        context.channel.placement_quality
    )
    
    # Audience readiness: intent strength above threshold?
    audience_score = audience_readiness(
        context.audience.intent_strength,
        target_action.required_intent_threshold
    )
    
    # Competitive context: adjust based on auction density
    competitive_score = competitive_adjustment(
        context.channel.competitive_density,
        target_action.competitive_strategy
    )
    
    # Weighted sum
    relevance = sum(weights[component] * score for component, score in 
                   [('intent_alignment', intent_score),
                    ('temporal_alignment', temporal_score),
                    ('channel_compatibility', channel_score),
                    ('audience_readiness', audience_score),
                    ('competitive_context', competitive_score)])
    
    return min(max(relevance, 0), 100)  # Clamp to 0-100
```

#### Rule Examples
```python
# Channel compatibility rules
CHANNEL_RULES = {
    ('video_ad', 'web'): 0.9,
    ('video_ad', 'mobile'): 0.7,
    ('video_ad', 'email'): 0.0,
    ('display_ad', 'web'): 0.8,
    ('display_ad', 'mobile'): 0.9,
    ('email_campaign', 'email'): 1.0,
    ('email_campaign', 'web'): 0.0
}

# Temporal compatibility rules
def temporal_compatibility(window, current_time):
    if current_time in window:
        return 1.0
    elif is_adjacent_to_window(current_time, window):
        return 0.5
    else:
        return 0.0
```

### Component 2: Situation Classifier

**Purpose:** Map current context to one of six situational archetypes.

#### Archetype Definitions
| Archetype | Definition | Context Indicators | Recommended Focus |
|-----------|------------|---------------------|-------------------|
| **Exploration** | Early research, low intent, high curiosity | Intent: research topics, Channel: search/educational, Temporal: early session | Educational content, Awareness |
| **Consideration** | Active evaluation, medium intent | Intent: comparison keywords, Channel: review sites, Temporal: mid session | Testimonials, Comparisons |
| **Decision** | Ready to purchase, high intent | Intent: pricing/buy keywords, Channel: product pages, Temporal: late session | Promotions, Urgency |
| **Crisis** | Negative sentiment, competitive threat | Intent: complaint keywords, Social: negative sentiment, Market: competitor mentions | Damage control, Support |
| **Opportunity** | Surge demand, trending alignment | Social: trending topics, Market: competitive wins, Temporal: peak timing | Aggressive bids, Trend-jacking |
| **Retention** | Post-purchase, loyalty signals | Intent: support/help keywords, Channel: customer portal, Temporal: post-purchase | Upsell, Loyalty, Support |

#### ML Classifier (Scikit-learn Implementation)
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

class SituationClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.feature_names = [
            'intent_research_score', 'intent_comparison_score', 'intent_purchase_score',
            'channel_educational', 'channel_review', 'channel_product',
            'session_depth', 'sentiment_score', 'competitor_mentions',
            'time_of_day_morning', 'time_of_day_afternoon'
        ]
    
    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)
        print(classification_report(y_test, self.model.predict(X_test)))
    
    def predict(self, context_features):
        return self.model.predict([context_features])[0]
    
    def save(self, path):
        joblib.dump(self.model, path)
    
    @classmethod
    def load(cls, path):
        instance = cls()
        instance.model = joblib.load(path)
        return instance
```

#### Training Data Requirements
- Minimum: 1,000 labeled context examples per archetype
- Source: Historical campaign data with manual review
- Validation: 80/10/10 train/validation/test split

### Component 3: Context Predictor

**Purpose:** Predict future context states to enable pre-optimization.

#### Sequence Modeling Approach
```python
import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer

class ContextPredictor(nn.Module):
    def __init__(self, context_dim=1024, hidden_size=512, num_layers=2):
        super().__init__()
        # Use pre-trained model for context understanding
        self.encoder = AutoModel.from_pretrained('sentence-transformers/all-mpnet-base-v2')
        # LSTM for temporal prediction
        self.lstm = nn.LSTM(
            input_size=context_dim,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )
        # Predict next context embeddings
        self.predictor = nn.Linear(hidden_size, context_dim)
    
    def forward(self, context_sequence):
        # context_sequence: (batch, seq_len, context_dim)
        lstm_out, _ = self.lstm(context_sequence)
        next_context = self.predictor(lstm_out[:, -1, :])
        return next_context
```

#### Applications
1. **Pre-bid optimization:** Predict optimal bid before auction starts
2. **Content pre-fetch:** Load relevant content before it's needed
3. **Proactive engagement:** Initiate contact before user explicitly signals intent

### Component 4: Action Mapper

**Purpose:** Map situation types to optimal action sets.

#### Action-Situation Matrix

| Situation | Primary Actions | Budget Multiplier | Urgency Score | Creative Focus |
|-----------|----------------|-------------------|---------------|----------------|
| Exploration | Educational content, Broad targeting, A/B testing | 0.8x | Low | Awareness, Education |
| Consideration | Comparative content, Testimonials, Retargeting | 1.2x | Medium | Features, Benefits, ROI |
| Decision | Promotions, Urgency signals, Payment options | 1.8x | High | Offers, Urgency, Trust |
| Crisis | Damage control, Support escalation | 2.0x | Critical | Empathy, Resolution |
| Opportunity | Targeted surge, Competitive conquesting | 1.5x | High | Timeliness, Relevance |
| Retention | Loyalty rewards, Support outreach, Upsells | 1.0x | Medium | Value, Relationship |

#### Context Modulation Formula
```python
def calculate_action_parameters(situation, base_bid, max_budget):
    multipliers = {
        'exploration': 0.8,
        'consideration': 1.2,
        'decision': 1.8,
        'crisis': 2.0,
        'opportunity': 1.5,
        'retention': 1.0
    }
    
    urgency_scores = {
        'exploration': 0.2,
        'consideration': 0.5,
        'decision': 0.9,
        'crisis': 1.0,
        'opportunity': 0.8,
        'retention': 0.4
    }
    
    multiplier = multipliers.get(situation, 1.0)
    urgency = urgency_scores.get(situation, 0.5)
    
    final_bid = min(base_bid * multiplier, max_budget)
    
    return {
        'bid': final_bid,
        'urgency': urgency,
        'creative_type': get_creative_for_situation(situation)
    }
```

---

## 🎯 CAM Framework: The Four Layers

### Layer 1: Sensing Layer (Context Signal Ingestion)
**Purpose:** Real-time ingestion of multi-modal marketing context signals.

#### Signal Categories
| Category | Signals | Sources | Frequency | Latency Budget |
|----------|---------|---------|-----------|----------------|
| **Audience** | Demographics, past behavior, interest graph, current session intent | CDP, DMP, CRM, Web Analytics | Event-stream | <100ms |
| **Channel** | Platform state, inventory levels, competitive landscape, ad placement quality | DSPs, SSPs, Ad Servers | Event-stream | <500ms |
| **Temporal** | Time of day, day of week, seasonality, holidays, trends | Calendar APIs, Trend APIs | Batch + Event | <1s |
| **Situational** | Device type, location, network speed, surrounding content, weather | Device APIs, Contextual DSPs | Event-stream | <100ms |
| **Social** | Social sentiment, trending topics, peer activity, influencer mentions | Social APIs, News Feeds | Event-stream | <1s |
| **Market** | Competitor prices, macroeconomic indicators, industry news | Market Data Feeds | Batch | <5min |

#### Key Design Principles
- **Multi-modal fusion:** Combine structured (CRM) + unstructured (social text) + sensor (device) data
- **Privacy-first:** All signals are **non-PII** or pseudonymous; no identity-based targeting required
- **Real-time capability:** Sub-second latency for audience/situational signals  
- **Fallback to batch:** Market/temporal signals can be higher-latency

---

### Layer 2: Context Model (Unified Representation)
**Purpose:** Transform raw signals into a structured, queryable context representation.

#### Core Entities
See **Layer 2 Deep Dive** above for complete JSON schema, embedding strategy, and storage implementation.

---

### Layer 3: Awareness Engine (Context Reasoning)
**Purpose:** Reasoning module that evaluates context relevance and triggers adaptive agent behavior.

#### Core Capabilities
See **Layer 3 Deep Dive** above for:
- Context Scorer (rule-based + ML hybrid)
- Situation Classifier (6 archetypes, RandomForest implementation)
- Context Predictor (LSTM-based sequence modeling)
- Action Mapper (situation-to-action mapping)

---

## 🎯 CAM Maturity Model

### Level 0: Unaware Agents
- **Description:** Traditional rule-based marketing automation
- **Context Awareness:** None  
- **Examples:** Basic email drip campaigns, static retargeting

### Level 1: Signal-Aware Agents
- **Description:** Can ingest basic signals (time, channel, simple demographics)
- **Context Awareness:** Basic signal detection
- **Examples:** Time-of-day ad scheduling, device-based bidding

### Level 2: Context-Aware Agents (Current State of Art)
- **Description:** Can understand and act on specific context dimensions
- **Context Awareness:** Partial, siloed understanding
- **Examples:** Weather-triggered ads, location-based offers

### Level 3: Context-Aware Agents (CAM Target)
- **Description:** Unified context understanding across all dimensions
- **Context Awareness:** Holistic situational awareness
- **Examples:** This framework's implementation

### Level 4: Context-Predictive Agents
- **Description:** Can predict future context states and pre-optimize
- **Context Awareness:** Temporal forecasting
- **Examples:** Future-state marketing

---

## 🧪 Evaluation Framework

### Metrics
| Category | Metric | Definition | Target |
|----------|--------|------------|--------|
| **Context Accuracy** | Context Match Rate | % actions correctly matched to context | >90% |
| **Business Impact** | Lift over Baseline | % improvement vs non-context-aware | +15-30% |
| **Computational** | Latency | Time from signal to action | <500ms |
| **Reliability** | Uptime | System availability | >99.5% |
| **Privacy** | PII Exposure | % of decisions using PII | 0% |

### Benchmarks
| Benchmark Name | Description | Dataset Size | Metric |
|----------------|-------------|--------------|--------|
| CAM-Sim | Synthetic marketing simulation environment | 10K scenarios | Context Match Rate |
| Real-World A/B | Production A/B tests vs baseline | TBD | Lift over Baseline |
| Context Robustness | Performance under adversarial context | 1K edge cases | Context Accuracy |

---

## 📋 Roadmap

| Q | Deliverable | Output | Success Criteria |
|---|-------------|--------|-------------------|
| **Q3 2026** | Framework Paper (this doc → publication) | Journal submission | Accepted to Tier-1 conference/journal |
| **Q4 2026** | CAM-Sim Benchmark | Open-source sim + leaderboard | 5+ external submissions |
| **Q1 2027** | Level 3 Prototype | Production-ready implementation | 500ms latency, 95% context accuracy |
| **Q2 2027** | Real-world Validation | A/B test results | +20% lift on pilot campaigns |

---

## 🔗 Relationship to Other Gaps

| Gap | Synergy with G4 | How G4 Informs/Enables |
|-----|----------------|------------------------|
| **G1** | Foundational | G4 provides operational definition of contextual intelligence for marketing; G1 provides the theoretical framework that G4 instantiates |
| **G2** | Validation | G4's prototypes can be used to test measurement instruments; G2 provides survey-based validation of G4's constructs |
| **G3** | Evidence | G4's A/B testing framework directly supports context-aware vs identity-based targeting experiments |
| **G5** | Integration | G4's situational awareness model can subsume omnichannel fusion as a context signal category |
| **G6** | Domain Specialization | G4 can be specifically adapted for B2B contexts (firmographics, buying committees, longer cycles) |

---

## 🛡️ Haaglund Differentiation

**Haaglund (2025):** Contextual intelligence: leveraging AI for targeted marketing (Umea, CS/NLP)
- **Domain:** CS/NLP (Computing Science)
- **Focus:** Opinion-unit extraction, aspect-based sentiment, media-context effects on ad perception
- **Contribution:** Technical foundation for understanding text-side advertising context
- **Limitation:** Does NOT address agentic systems, does NOT define marketing construct

**This Work (G4 CAM):**
- **Domain:** Marketing (with AI/CS methods)
- **Focus:** Agentic situational awareness - how AI agents understand and act on marketing context
- **Contribution:** Operational framework for context-aware agents, bridging Haaglund's NLP foundation with marketing strategy
- **Citation Strategy:** Explicitly cite Haaglund as technical prior art for context representation, then extend

**Differentiation Statement:**
> While Haaglund (2025) provides the NLP foundation for understanding advertising context within text, our work extends this to full agentic situational awareness - how autonomous marketing agents sense, reason about, and act on across all dimensions of marketing context, not just textual advertising context.

---

## 💡 Next Steps

- [x] Flesh out Layer 2 (Context Model) with JSON schema + embedding strategy
- [x] Flesh out Layer 3 (Awareness Engine) with algorithms + code snippets
- [ ] Develop CAM-Sim benchmark environment and synthetic data generation
- [ ] Draft journal submission (target: Marketing Science special issue on AI)
- [ ] Prototype Level 2→3 implementation using existing corpus data

---

## 📚 References (from corpus)

To be populated from papers.yaml:
- All 61 agentic papers
- All 44 contextual papers  
- Intent modeling papers (top 50)
- Omnichannel papers (top 20)
- B2B marketing AI papers (top 15)

---

## 📊 Appendix: Corpus Signal Deep-Dive

### Agentic Papers Over Time
```
2025-02: 1  | 2025-11: 1  | 2025-12: 1
2026-01: 2  | 2026-03: 3  | 2026-04: 7
2026-05: 4  | 2026-06: 6  | 2026-07: 12
2026-08: 4 (to date)
```
**Exponential growth trajectory confirmed.**

### Contextual Papers Distribution
- ai-marketing: 22
- digital-marketing: 8
- analytics: 5
- privacy-data: 3
- b2b: 2
- others: 4

**50% in AI-marketing category; none in agentic categories.**

### Zero-Intersection Confirmation
The only 2 papers that mention both agentic and context are:
1. From Personalisation to Agentic Campaigns: Modern Marketing Techniques Using Artificial Intelligence in the Indian Context (2026-07)
2. I hope we don't do to trust what advertising has done to love (2026-04)

Both are **superficial mentions** - no academic paper builds the bridge.

---

*This document is the starting point for the G4 deliverable. Status: deep-dive v0.2*
