#!/usr/bin/env python3
"""CAM-Sim: Context-Aware Agentic Marketing Simulation Environment.

A synthetic marketing simulation for benchmarking Context-Aware Agentic Marketing
(CAM) frameworks. Enables reproducible evaluation of context-aware marketing
agents without requiring live ad spend or customer data.

Design notes (v0.3):
- Reproducibility: both the environment (numpy) and the agents (stdlib random)
  are seeded per run. Identical --seeds reproduce identical results.
- Fair pairing: scenarios are generated ONCE per seed and every agent acts on
  the SAME context sequence. This removes the scenario-draw confound and makes
  seed-level paired tests legitimate.
- Ablation ladder (the point of the benchmark): performance is measured as a
  function of context-awareness quality, not oracle-vs-random:
      baseline        random channel/action, fixed bid table (strawman floor)
      channel_only    optimal bidding, no situation knowledge
      situation_only  correct situation->action mapping, flat bidding
      noisy50/80      perceives true situation with probability p (graded SA)
      cam_inferred    infers situation from observable intent signal (no oracle)
      oracle          ground-truth situation access (upper bound, by design)

The oracle is labeled as an upper bound: it validates environment consistency,
NOT real-world performance. The informative comparisons are cam_inferred and
the noisy agents against each other (dose-response of situational awareness).

Usage:
    python3 scripts/benchmarks/cam_sim.py --scenarios 200 --seeds 1,2,3,4,5
    python3 scripts/benchmarks/cam_sim.py --agents baseline,cam_inferred,oracle --output-md results/cam_sim_results.md

Author: Tobias Weiss (2026)
"""

import argparse
import bisect
import json
import random
import sys
import scipy.stats
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
from pathlib import Path

import numpy as np

# Type aliases
ContextID = str
ActionID = int


class SituationType(Enum):
    """Situational archetypes from CAM framework."""
    EXPLORATION = "exploration"
    CONSIDERATION = "consideration"
    DECISION = "decision"
    CRISIS = "crisis"
    OPPORTUNITY = "opportunity"
    RETENTION = "retention"


class ChannelType(Enum):
    """Marketing channel types."""
    SEARCH = "search"
    SOCIAL = "social"
    DISPLAY = "display"
    EMAIL = "email"
    VIDEO = "video"


class ActionType(Enum):
    """Marketing action types."""
    EDUCATIONAL = "educational"
    COMPARISON = "comparison"
    PROMOTIONAL = "promotional"
    CRISIS_RESPONSE = "crisis_response"
    URGENT = "urgent"
    LOYALTY = "loyalty"


@dataclass
class ContextSignal:
    """A single context signal."""
    category: str
    name: str
    value: float | str | int
    confidence: float = 1.0
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


@dataclass
class FullContext:
    """Complete context state for a marketing moment."""
    context_id: ContextID
    timestamp: str
    signals: List[ContextSignal] = field(default_factory=list)
    situation: SituationType = SituationType.EXPLORATION
    audience_intent_strength: float = 0.5
    channel_quality: float = 0.7
    competitive_density: float = 0.3
    intent_vector: List[float] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            'context_id': self.context_id,
            'timestamp': self.timestamp,
            'situation': self.situation.value,
            'audience_intent_strength': self.audience_intent_strength,
            'channel_quality': self.channel_quality,
            'competitive_density': self.competitive_density,
            'intent_vector': self.intent_vector,
            'signals': [{'category': s.category, 'name': s.name, 'value': s.value,
                         'confidence': s.confidence, 'timestamp': s.timestamp}
                        for s in self.signals]
        }


@dataclass
class Action:
    """A marketing action."""
    action_id: ActionID
    action_type: ActionType
    channel: ChannelType
    bid: float = 0.0
    content: str = ""


@dataclass
class ActionResult:
    """Result of taking an action in a context."""
    context_id: ContextID
    action_id: ActionID
    action_type: ActionType
    reward: float
    cost: float
    long_term_value: float = 0.0
    context_match: bool = False
    latency_ms: float = 0.0
    skipped: bool = False  # action not executed (budget exhausted)

    @property
    def profit(self) -> float:
        """Net profit from action."""
        return self.reward + self.long_term_value - self.cost


# Shared situation->action / situation->channel mappings
IDEAL_ACTION = {
    SituationType.EXPLORATION: ActionType.EDUCATIONAL,
    SituationType.CONSIDERATION: ActionType.COMPARISON,
    SituationType.DECISION: ActionType.PROMOTIONAL,
    SituationType.CRISIS: ActionType.CRISIS_RESPONSE,
    SituationType.OPPORTUNITY: ActionType.URGENT,
    SituationType.RETENTION: ActionType.LOYALTY,
}

SITUATION_CHANNEL = {
    SituationType.EXPLORATION: ChannelType.SEARCH,
    SituationType.CONSIDERATION: ChannelType.SOCIAL,
    SituationType.DECISION: ChannelType.SEARCH,
    SituationType.CRISIS: ChannelType.SOCIAL,
    SituationType.OPPORTUNITY: ChannelType.DISPLAY,
    SituationType.RETENTION: ChannelType.EMAIL,
}


def infer_situation_from_intent(intent: float) -> SituationType:
    """Infer situation from the observable intent signal alone (no oracle).

    Deliberately imperfect: crisis (0.8±0.1) and opportunity (0.7±0.1) overlap
    with decision (0.9±0.1); retention (0.3±0.1) overlaps exploration. This
    models realistic classifier confusion on observable signals.
    """
    if intent < 0.35:
        return SituationType.EXPLORATION
    if intent < 0.65:
        return SituationType.CONSIDERATION
    if intent < 0.78:
        return SituationType.OPPORTUNITY
    return SituationType.DECISION


# ---------------------------------------------------------------------------
# Environment configurations (robustness presets)
#
# The situation->ideal-action LANGUAGE is held fixed across environments
# (IDEAL_ACTION / SITUATION_CHANNEL); what varies is the ECONOMICS: situation
# distribution, reward scale, media costs, and how strongly the environment
# pays for context-matching. This addresses reward-design circularity: if the
# headline findings replicate across presets, they are not artifacts of one
# hand-designed reward table.
# ---------------------------------------------------------------------------
ENVIRONMENT_PRESETS: Dict[str, dict] = {
    'default': {
        'situation_weights': [0.35, 0.30, 0.15, 0.05, 0.05, 0.10],
        'reward_scale': 1.0,
        'cost_multiplier': 1.0,
        'match_bonus': 0.5,       # reward added when action matches situation
        'match_penalty': -0.3,    # reward change when action mismatches
        'bid_eff_scale': 1.0,     # scales bid-efficiency adjustments (+.3/+.1/-.2)
        'competitive_scale': 0.5, # competitive discount factor
        'budget_per_episode': None,  # runner-level: media budget cap per episode
        'bid_return_alpha': None,    # env-level: concave returns to bid exponent
    },
    'uniform_situations': {
        'situation_weights': [1 / 6] * 6,
    },
    'decision_heavy': {
        'situation_weights': [0.15, 0.20, 0.35, 0.10, 0.10, 0.10],
    },
    'crisis_heavy': {
        'situation_weights': [0.15, 0.20, 0.15, 0.25, 0.10, 0.15],
    },
    'retention_heavy': {
        'situation_weights': [0.15, 0.15, 0.15, 0.05, 0.05, 0.45],
    },
    'high_costs': {
        'cost_multiplier': 2.0,   # expensive-media regime
    },
    'weak_signal_bonus': {
        'match_bonus': 0.25,
        'match_penalty': -0.15,
        'bid_eff_scale': 0.5,     # environment pays WEAKLY for context matching
    },
    'budget_constrained': {
        'budget_per_episode': 250.0,  # media budget cap per 200-action episode
    },
    'concave_returns': {
        'bid_return_alpha': 0.5,  # concave returns to bid: reward *= (bid/optimal)^0.5
    },
}


class Agent(ABC):
    """Abstract base class for marketing agents."""

    def __init__(self, name: str):
        self.name = name
        self.actions_taken: int = 0

    @abstractmethod
    def decide(self, context: FullContext) -> Action:
        """Make a decision given a context."""
        pass

    def reset(self):
        self.actions_taken = 0


class BaselineAgent(Agent):
    """Rule-based non-context-aware agent (strawman floor).

    Random channel, fixed per-channel action default, bid with ±20% noise
    around a fixed base. Uses stdlib random (seeded per run by the runner).
    """

    BASE_BIDS = {
        ChannelType.SEARCH: 1.50,
        ChannelType.SOCIAL: 1.00,
        ChannelType.DISPLAY: 0.80,
        ChannelType.EMAIL: 0.10,
        ChannelType.VIDEO: 2.00,
    }

    DEFAULT_ACTIONS = {
        ChannelType.SEARCH: ActionType.EDUCATIONAL,
        ChannelType.SOCIAL: ActionType.EDUCATIONAL,
        ChannelType.DISPLAY: ActionType.PROMOTIONAL,
        ChannelType.EMAIL: ActionType.LOYALTY,
        ChannelType.VIDEO: ActionType.PROMOTIONAL,
    }

    def __init__(self):
        super().__init__("baseline")

    def decide(self, context: FullContext) -> Action:
        self.actions_taken += 1
        channel = random.choice(list(ChannelType))
        bid = max(0.01, self.BASE_BIDS[channel] * random.uniform(0.8, 1.2))
        return Action(self.actions_taken, self.DEFAULT_ACTIONS[channel], channel, round(bid, 2))


class CAMOracle(Agent):
    """Full CAM implementation with ORACLE situation access (upper bound).

    Uses ground-truth situation label. This is NOT a realistic agent — it
    validates environment consistency and bounds achievable performance.
    """

    SITUATION_MULTIPLIERS = {
        SituationType.EXPLORATION: 0.8,
        SituationType.CONSIDERATION: 1.2,
        SituationType.DECISION: 1.8,
        SituationType.CRISIS: 2.0,
        SituationType.OPPORTUNITY: 1.5,
        SituationType.RETENTION: 1.0,
    }

    CHANNEL_QUALITY_ADJUSTMENTS = {0.0: 0.5, 0.3: 0.8, 0.5: 1.0, 0.7: 1.2, 0.9: 1.5, 1.0: 2.0}
    INTENT_ADJUSTMENTS = {0.0: 0.5, 0.25: 0.8, 0.5: 1.0, 0.75: 1.3, 1.0: 1.8}

    def __init__(self, name: str = "oracle"):
        super().__init__(name)

    def _interp(self, value: float, mapping: Dict[float, float]) -> float:
        keys = sorted(mapping.keys())
        for lo, hi in zip(keys, keys[1:]):
            if lo <= value <= hi:
                ratio = (value - lo) / (hi - lo) if hi > lo else 0.0
                return mapping[lo] + ratio * (mapping[hi] - mapping[lo])
        return mapping[keys[-1]]

    def _bid(self, situation: SituationType, context: FullContext) -> float:
        return (1.0
                * self.SITUATION_MULTIPLIERS[situation]
                * self._interp(context.channel_quality, self.CHANNEL_QUALITY_ADJUSTMENTS)
                * self._interp(context.audience_intent_strength, self.INTENT_ADJUSTMENTS))

    def decide(self, context: FullContext) -> Action:
        self.actions_taken += 1
        situation = context.situation  # oracle access
        action_type = IDEAL_ACTION[situation]
        channel = SITUATION_CHANNEL[situation]
        return Action(self.actions_taken, action_type, channel, round(self._bid(situation, context), 2))


class CAMInferred(Agent):
    """CAM agent that must INFER the situation from observable signals.

    Realistic Level-2 SA agent: classifies situation from audience intent
    strength (imperfect classifier via infer_situation_from_intent), then
    applies the same action mapping and bid logic as the oracle.
    """

    def __init__(self):
        super().__init__("cam_inferred")
        self._engine = CAMOracle("cam_inferred_engine")

    def decide(self, context: FullContext) -> Action:
        self.actions_taken += 1
        situation = infer_situation_from_intent(context.audience_intent_strength)
        action_type = IDEAL_ACTION[situation]
        channel = SITUATION_CHANNEL[situation]
        bid = self._engine._bid(situation, context)
        return Action(self.actions_taken, action_type, channel, round(bid, 2))


# ---------------------------------------------------------------------------
# Learned situation classifier (supervised, then deployed without oracle).
#
# Since audience intent is the ONLY situation-informative observable in the
# generator, the Bayes-optimal classifier on observable signals is an interval
# rule on intent. We therefore learn interval thresholds from a LABELED
# calibration sample (greedy top-down splitting, deterministic). This enables
# the F5 remedy test: recalibrate the classifier per situation distribution.
# ---------------------------------------------------------------------------

def fit_intent_classifier(samples, max_splits: int = 5):
    """Fit an interval classifier intent -> SituationType from labeled samples.

    Greedy top-down: repeatedly split the interval at the point that most
    reduces classification error, until max_splits splits. Deterministic.
    Returns (thresholds, interval_labels).
    """
    pts = sorted(samples, key=lambda t: t[0])

    def best_split(p):
        classes = {}
        for _, s in p:
            classes[s] = classes.get(s, 0) + 1
        total = len(p)
        e0 = total - max(classes.values())
        left = {}
        best_gain, best_j = 0.0, None
        for j in range(1, total):
            s = p[j - 1][1]
            left[s] = left.get(s, 0) + 1
            if p[j][0] == p[j - 1][0]:
                continue
            nl, nr = j, total - j
            ml = max(left.values())
            mr = max((n - left.get(c, 0) for c, n in classes.items()))
            gain = e0 - ((nl - ml) + (nr - mr))
            if gain > best_gain:
                best_gain, best_j = gain, j
        return best_gain, best_j

    intervals = [pts]
    while len(intervals) < max_splits + 1:
        cand = [(best_split(p), i) for i, p in enumerate(intervals) if len(p) >= 2]
        cand = [(g, j, i) for (g, j), i in cand if j is not None]
        if not cand:
            break
        gain, j, i = max(cand)
        if gain <= 0:
            break
        p = intervals[i]
        intervals[i:i + 1] = [p[:j], p[j:]]

    def majority(p):
        counts = {}
        for _, s in p:
            counts[s] = counts.get(s, 0) + 1
        return max(counts.items(), key=lambda kv: (kv[1], kv[0].value))[0]

    labels = [majority(p) for p in intervals]
    thresholds = [round((intervals[k - 1][-1][0] + intervals[k][0][0]) / 2, 4)
                  for k in range(1, len(intervals))]
    return thresholds, labels


def _fit_learner_for_config(config_overrides, calib_seed: int = 999_999, n: int = 2000,
                            label_noise: float = 0.0):
    """Draw a labeled calibration sample from the given env config and fit.

    label_noise: probability of flipping each label to a uniformly random
    OTHER situation (deployment realism: clean labels are an idealization;
    this parameterizes how fast the recalibration remedy degrades).
    """
    cfg = dict(ENVIRONMENT_PRESETS['default'])
    if config_overrides:
        cfg.update(config_overrides)
    env = SimulationEnvironment(seed=calib_seed, config=cfg)
    rng = np.random.RandomState(calib_seed + 1)
    all_situations = list(SituationType)
    samples = []
    for _ in range(n):
        c = env.generate_context()
        situation = c.situation
        if label_noise > 0 and rng.random_sample() < label_noise:
            choices = [s for s in all_situations if s != c.situation]
            situation = choices[rng.randint(len(choices))]
        samples.append((c.audience_intent_strength, situation))
    return fit_intent_classifier(samples)


_DEFAULT_LEARNER = None


def make_cam_learned() -> "CAMLearned":
    """Classifier fit ONCE on the default distribution (lazy, deterministic)."""
    global _DEFAULT_LEARNER
    if _DEFAULT_LEARNER is None:
        _DEFAULT_LEARNER = _fit_learner_for_config(None)
    return CAMLearned(*_DEFAULT_LEARNER, name="cam_learned")


class CAMLearned(Agent):
    """CAM agent with a LEARNED situation classifier.

    Fit on a labeled calibration sample drawn from a (possibly different)
    situation distribution, then deployed without oracle access. Compared to
    `cam_inferred` (hand-set thresholds), this tests whether the F5 bias
    problem is an artifact of hand-tuning or intrinsic to distribution shift —
    and whether per-environment recalibration fixes it.
    """

    def __init__(self, thresholds, interval_labels, name: str = "cam_learned"):
        super().__init__(name)
        self.thresholds = list(thresholds)
        self.interval_labels = list(interval_labels)
        self._engine = CAMOracle(name + "_engine")

    def classify(self, intent: float) -> SituationType:
        idx = bisect.bisect_right(self.thresholds, intent)
        return self.interval_labels[idx]

    def decide(self, context: FullContext) -> Action:
        self.actions_taken += 1
        situation = self.classify(context.audience_intent_strength)
        action_type = IDEAL_ACTION[situation]
        channel = SITUATION_CHANNEL[situation]
        bid = self._engine._bid(situation, context)
        return Action(self.actions_taken, action_type, channel, round(bid, 2))


class NoisyCAM(Agent):
    """CAM agent with GRADED situational awareness.

    Perceives the true situation with probability p; otherwise acts on a
    random situation label. Bid logic always uses true context values.
    Models imperfect perception (Endsley Level-1 errors propagating upward).
    """

    def __init__(self, p_correct: float, label: str):
        super().__init__(label)
        self.p_correct = p_correct
        self._engine = CAMOracle(label + "_engine")

    def decide(self, context: FullContext) -> Action:
        self.actions_taken += 1
        if random.random() < self.p_correct:
            situation = context.situation
        else:
            situation = random.choice(list(SituationType))
        action_type = IDEAL_ACTION[situation]
        channel = SITUATION_CHANNEL[situation]
        bid = self._engine._bid(situation, context)
        return Action(self.actions_taken, action_type, channel, round(bid, 2))


class SituationOnly(Agent):
    """Ablation: correct situation->action mapping, FLAT bidding.

    Isolates the value of action-type matching from bid optimization.
    """

    def __init__(self):
        super().__init__("situation_only")

    def decide(self, context: FullContext) -> Action:
        self.actions_taken += 1
        situation = context.situation
        return Action(self.actions_taken, IDEAL_ACTION[situation],
                      SITUATION_CHANNEL[situation], 1.0)


class ChannelOnly(Agent):
    """Ablation: bid optimization WITHOUT situation knowledge.

    Random action type, situation-agnostic channel, but context-aware bidding
    (channel quality + intent adjustments). Isolates the value of bidding from
    action matching.
    """

    CHANNEL_QUALITY_ADJUSTMENTS = CAMOracle.CHANNEL_QUALITY_ADJUSTMENTS
    INTENT_ADJUSTMENTS = CAMOracle.INTENT_ADJUSTMENTS

    def __init__(self):
        super().__init__("channel_only")
        self._engine = CAMOracle("channel_only_engine")

    def decide(self, context: FullContext) -> Action:
        self.actions_taken += 1
        action_type = random.choice(list(ActionType))
        channel = random.choice(list(ChannelType))
        bid = (1.0
               * self._engine._interp(context.channel_quality, self.CHANNEL_QUALITY_ADJUSTMENTS)
               * self._engine._interp(context.audience_intent_strength, self.INTENT_ADJUSTMENTS))
        return Action(self.actions_taken, action_type, channel, round(bid, 2))


class SimulationEnvironment:
    """Synthetic marketing simulation environment."""

    ACTION_COSTS = {
        ChannelType.SEARCH: 1.20,
        ChannelType.SOCIAL: 0.80,
        ChannelType.DISPLAY: 0.60,
        ChannelType.EMAIL: 0.05,
        ChannelType.VIDEO: 2.50,
    }

    # explore, consider, decide, crisis, opportunity, retention
    SITUATION_WEIGHTS = [0.35, 0.30, 0.15, 0.05, 0.05, 0.10]

    BASE_REWARDS = {
        (ActionType.EDUCATIONAL, SituationType.EXPLORATION): 2.0,
        (ActionType.EDUCATIONAL, SituationType.CONSIDERATION): 1.5,
        (ActionType.EDUCATIONAL, SituationType.DECISION): 0.5,
        (ActionType.EDUCATIONAL, SituationType.CRISIS): 0.3,
        (ActionType.EDUCATIONAL, SituationType.OPPORTUNITY): 1.0,
        (ActionType.EDUCATIONAL, SituationType.RETENTION): 1.2,
        (ActionType.COMPARISON, SituationType.EXPLORATION): 0.8,
        (ActionType.COMPARISON, SituationType.CONSIDERATION): 2.5,
        (ActionType.COMPARISON, SituationType.DECISION): 1.8,
        (ActionType.COMPARISON, SituationType.CRISIS): 0.5,
        (ActionType.COMPARISON, SituationType.OPPORTUNITY): 1.2,
        (ActionType.COMPARISON, SituationType.RETENTION): 0.8,
        (ActionType.PROMOTIONAL, SituationType.EXPLORATION): 0.5,
        (ActionType.PROMOTIONAL, SituationType.CONSIDERATION): 1.5,
        (ActionType.PROMOTIONAL, SituationType.DECISION): 3.0,
        (ActionType.PROMOTIONAL, SituationType.CRISIS): 0.3,
        (ActionType.PROMOTIONAL, SituationType.OPPORTUNITY): 2.5,
        (ActionType.PROMOTIONAL, SituationType.RETENTION): 0.5,
        (ActionType.CRISIS_RESPONSE, SituationType.EXPLORATION): 0.1,
        (ActionType.CRISIS_RESPONSE, SituationType.CONSIDERATION): 0.3,
        (ActionType.CRISIS_RESPONSE, SituationType.DECISION): 0.5,
        (ActionType.CRISIS_RESPONSE, SituationType.CRISIS): 2.5,
        (ActionType.CRISIS_RESPONSE, SituationType.OPPORTUNITY): 0.2,
        (ActionType.CRISIS_RESPONSE, SituationType.RETENTION): 0.8,
        (ActionType.URGENT, SituationType.EXPLORATION): 0.5,
        (ActionType.URGENT, SituationType.CONSIDERATION): 1.2,
        (ActionType.URGENT, SituationType.DECISION): 2.0,
        (ActionType.URGENT, SituationType.CRISIS): 0.8,
        (ActionType.URGENT, SituationType.OPPORTUNITY): 2.8,
        (ActionType.URGENT, SituationType.RETENTION): 0.3,
        (ActionType.LOYALTY, SituationType.EXPLORATION): 0.3,
        (ActionType.LOYALTY, SituationType.CONSIDERATION): 0.5,
        (ActionType.LOYALTY, SituationType.DECISION): 0.2,
        (ActionType.LOYALTY, SituationType.CRISIS): 0.5,
        (ActionType.LOYALTY, SituationType.OPPORTUNITY): 0.3,
        (ActionType.LOYALTY, SituationType.RETENTION): 2.0,
    }

    def __init__(self, seed: Optional[int] = None, config: Optional[dict] = None):
        self.rng = np.random.RandomState(seed)
        self.scenario_counter = 0
        cfg = dict(ENVIRONMENT_PRESETS['default'])
        if config:
            unknown = set(config) - set(cfg)
            if unknown:
                raise ValueError(f"Unknown environment config keys: {unknown}")
            cfg.update(config)
        w = cfg['situation_weights']
        if abs(sum(w) - 1.0) > 1e-6:
            raise ValueError(f"situation_weights must sum to 1.0 (got {sum(w)})")
        if 'budget_per_episode' in cfg and (cfg['budget_per_episode'] is not None) and cfg['budget_per_episode'] <= 0:
            raise ValueError("budget_per_episode must be positive")
        a = cfg.get('bid_return_alpha')
        if a is not None and not (0.0 < a <= 2.0):
            raise ValueError("bid_return_alpha must be in (0, 2]")
        self.cfg = cfg
        self.situation_weights = list(w)
        self.action_costs = {ch: c * cfg['cost_multiplier']
                             for ch, c in self.ACTION_COSTS.items()}

    def _random_situation(self) -> SituationType:
        situations = list(SituationType)
        choice = self.rng.choice(len(situations), p=self.situation_weights)
        return situations[int(choice)]

    def _get_intent_strength(self, situation: SituationType) -> float:
        strengths = {
            SituationType.EXPLORATION: 0.2,
            SituationType.CONSIDERATION: 0.6,
            SituationType.DECISION: 0.9,
            SituationType.CRISIS: 0.8,
            SituationType.OPPORTUNITY: 0.7,
            SituationType.RETENTION: 0.3,
        }
        return max(0.0, min(1.0, strengths[situation] + self.rng.uniform(-0.1, 0.1)))

    def _generate_signals(self, situation: SituationType, intent: float) -> List[ContextSignal]:
        signals = []
        if situation in (SituationType.DECISION, SituationType.CRISIS):
            signals.append(ContextSignal("audience", "intent_strength", round(intent, 3), 0.9))
        signals.append(ContextSignal("channel", "quality_score", round(self.rng.uniform(0.5, 1.0), 2), 0.8))
        signals.append(ContextSignal("temporal", "time_of_day",
                                     self.rng.choice(["morning", "afternoon", "evening", "night"]), 1.0))
        signals.append(ContextSignal("situational", "device_type",
                                     self.rng.choice(["desktop", "mobile", "tablet"]), 0.95))
        return signals

    def generate_context(self) -> FullContext:
        """Generate a synthetic marketing context."""
        self.scenario_counter += 1
        situation = self._random_situation()
        intent = self._get_intent_strength(situation)
        return FullContext(
            context_id=f"ctx_{self.scenario_counter}",
            timestamp=datetime.utcnow().isoformat(),
            signals=self._generate_signals(situation, intent),
            situation=situation,
            audience_intent_strength=intent,
            channel_quality=float(self.rng.uniform(0.1, 1.0)),
            competitive_density=float(self.rng.uniform(0.0, 1.0)),
        )

    def evaluate_action(self, context: FullContext, action: Action) -> ActionResult:
        """Evaluate the result of taking an action in a context."""
        cfg = self.cfg
        base_reward = self.BASE_REWARDS[(action.action_type, context.situation)] * cfg['reward_scale']

        context_match = (action.action_type == IDEAL_ACTION[context.situation])
        context_bonus = cfg['match_bonus'] if context_match else cfg['match_penalty']

        optimal_bid = 1.0 * context.audience_intent_strength * context.channel_quality
        bid_ratio = action.bid / optimal_bid if optimal_bid > 0 else 0
        if 0.8 <= bid_ratio <= 1.2:
            bid_efficiency = 0.3
        elif 0.5 <= bid_ratio <= 1.5:
            bid_efficiency = 0.1
        else:
            bid_efficiency = -0.2
        bid_efficiency *= cfg['bid_eff_scale']

        competitive_factor = 1.0 - context.competitive_density * cfg['competitive_scale']
        total_reward = (base_reward + context_bonus + bid_efficiency) * competitive_factor

        # Optional concave returns to bid: reward scales sublinearly with the
        # bid relative to the clearing price, creating an interior optimal bid.
        alpha = cfg.get('bid_return_alpha')
        if alpha and optimal_bid > 0:
            ret_mult = max(0.0, min(2.0, (action.bid / optimal_bid) ** alpha))
            total_reward *= ret_mult

        cost = self.action_costs[action.channel] * action.bid
        long_term_value = total_reward * 0.2 * context.audience_intent_strength
        latency_ms = self.rng.uniform(50, 500)

        return ActionResult(
            context_id=context.context_id,
            action_id=action.action_id,
            action_type=action.action_type,
            reward=round(total_reward, 2),
            cost=round(cost, 2),
            long_term_value=round(long_term_value, 2),
            context_match=context_match,
            latency_ms=round(latency_ms, 1),
        )


class BenchmarkRunner:
    """Run benchmarks comparing different agents on SHARED context sequences."""

    def __init__(self, env: SimulationEnvironment):
        self.env = env
        self.contexts: List[FullContext] = []

    def run_benchmark(self, agents: List[Agent], contexts: List[FullContext],
                      budget: Optional[float] = None) -> Dict[str, List[ActionResult]]:
        """Run every agent against the SAME context sequence (fair pairing).

        If budget is set, an agent's cumulative spend is tracked per episode;
        once exhausted, further moments are SKIPPED (recorded as zero-value,
        non-matching results). Agents are budget-unaware — the constraint
        tests who spends efficiently, not who plans ahead.
        """
        all_results = {}
        for agent in agents:
            agent.reset()
            remaining = budget
            results = []
            for context in contexts:
                action = agent.decide(context)
                if remaining is not None:
                    est_cost = self.env.action_costs[action.channel] * action.bid
                    if est_cost > remaining + 1e-9:
                        results.append(ActionResult(
                            context_id=context.context_id,
                            action_id=action.action_id,
                            action_type=action.action_type,
                            reward=0.0, cost=0.0, long_term_value=0.0,
                            context_match=False, latency_ms=0.0, skipped=True))
                        continue
                    remaining -= est_cost
                results.append(self.env.evaluate_action(context, action))
            all_results[agent.name] = results
        return all_results

    @staticmethod
    def get_metrics(results: Dict[str, List[ActionResult]]) -> Dict[str, dict]:
        """Calculate evaluation metrics (aggregate ROAS, not per-action mean)."""
        metrics = {}
        for agent_name, agent_results in results.items():
            if not agent_results:
                continue
            total_actions = len(agent_results)
            total_cost = sum(r.cost for r in agent_results)
            total_reward = sum(r.reward for r in agent_results)
            total_ltv = sum(r.long_term_value for r in agent_results)
            total_profit = total_reward + total_ltv - total_cost
            context_match_rate = sum(1 for r in agent_results if r.context_match) / total_actions
            actions_skipped = sum(1 for r in agent_results if r.skipped)

            # Aggregate ROAS: total value returned per unit of spend. Guard
            # against near-zero spend instead of producing inf.
            roas = (total_reward + total_ltv) / total_cost if total_cost > 1e-9 else float('nan')

            metrics[agent_name] = {
                'total_actions': total_actions,
                'total_cost': round(total_cost, 2),
                'total_reward': round(total_reward, 2),
                'total_profit': round(total_profit, 2),
                'total_long_term_value': round(total_ltv, 2),
                'context_match_rate': round(context_match_rate * 100, 1),
                'roas_aggregate': round(roas, 3) if np.isfinite(roas) else None,
                'avg_cost': round(total_cost / total_actions, 2),
                'avg_reward': round(total_reward / total_actions, 3),
                'profit_per_cost': round(total_profit / total_cost, 3) if total_cost > 1e-9 else None,
                'actions_skipped': actions_skipped,
            }
        return metrics


class BidCalibratedAgent(Agent):
    """Oracle situation knowledge + bid calibrated to the environment MECHANISM.

    Unlike CAMOracle (hand-set bid multipliers), this agent knows the reward
    table, match bonus, cost table, competitive scale, and returns-to-bid
    curvature, and numerically maximizes expected profit per context (coarse
    grid + local refinement over the bid). It is the per-mechanism profit
    CEILING: it tests whether the F3 surprise (flat bidding beats heuristic
    bidding) survives when bidding is actually optimal, and whether the
    'oracle' was ever a real upper bound. Deterministic — no RNG draws, so
    appending it does not perturb the other agents' random streams.
    """

    def __init__(self, env: "SimulationEnvironment", name: str = 'bid_calibrated'):
        super().__init__(name)
        self.env = env
        self._counter = 0

    def _expected_profit(self, bid, intent, quality, channel_cost, comp, base, bonus):
        cfg = self.env.cfg
        optimal_bid = intent * quality
        ratio = bid / optimal_bid if optimal_bid > 0 else 0.0
        if 0.8 <= ratio <= 1.2:
            be = 0.3
        elif 0.5 <= ratio <= 1.5:
            be = 0.1
        else:
            be = -0.2
        be *= cfg['bid_eff_scale']
        total = (base + bonus + be) * comp
        alpha = cfg.get('bid_return_alpha')
        if alpha and optimal_bid > 0:
            total *= max(0.0, min(2.0, (bid / optimal_bid) ** alpha))
        # profit = reward + ltv - cost, with ltv = reward * 0.2 * intent
        return total * (1.0 + 0.2 * intent) - channel_cost * bid

    def decide(self, context: FullContext) -> Action:
        situation = context.situation
        action_type = IDEAL_ACTION[situation]
        channel = SITUATION_CHANNEL[situation]
        cfg = self.env.cfg
        base = self.env.BASE_REWARDS[(action_type, situation)] * cfg['reward_scale']
        bonus = cfg['match_bonus']  # always picks the ideal action -> always a match
        comp = 1.0 - context.competitive_density * cfg['competitive_scale']
        channel_cost = self.env.action_costs[channel]
        intent, quality = context.audience_intent_strength, context.channel_quality

        best_bid, best_val = 1.0, -float('inf')
        for i in range(1, 251):  # coarse grid: 0.02 .. 5.00
            bid = 0.02 * i
            v = self._expected_profit(bid, intent, quality, channel_cost, comp, base, bonus)
            if v > best_val:
                best_bid, best_val = bid, v
        lo = max(0.01, best_bid - 0.02)
        for i in range(1, 20):  # local refinement at 0.001 resolution
            bid = lo + 0.001 * i
            v = self._expected_profit(bid, intent, quality, channel_cost, comp, base, bonus)
            if v > best_val:
                best_bid, best_val = bid, v
        self._counter += 1
        return Action(action_id=f"a_{self.name}_{self._counter}", action_type=action_type,
                      channel=channel, bid=round(best_bid, 3))


class BudgetPacedAgent(Agent):
    """Wrap any agent with a standard adtech EVEN-PACING rule: per moment, the
    bid may not exceed (remaining budget / remaining moments) / channel cost.

    Addresses the 'budget-unaware agents' limitation: the wrapped agent still
    decides channel and action exactly as before; only the bid is rationed so
    spend spreads across the episode instead of hitting a hard truncation
    cliff. Spend is estimated from the known cost table (cost = channel_cost
    x bid; the environment does not alter bids, so estimates are exact).
    """

    def __init__(self, inner: Agent, budget: float, n_moments: int, cost_table: dict):
        super().__init__(f"{inner.name}_paced")
        self.inner = inner
        self.budget = float(budget)
        self._n_moments = int(n_moments)
        self.cost_table = cost_table
        self.reset()

    def reset(self):
        super().reset()
        self.inner.reset()
        self.remaining = self.budget
        self.moments_left = self._n_moments

    def decide(self, context: FullContext) -> Action:
        action = self.inner.decide(context)
        cost_unit = self.cost_table[action.channel]
        if self.moments_left > 0 and self.remaining > 0 and cost_unit > 0:
            allowance = self.remaining / self.moments_left  # $ per moment
            max_bid = allowance / cost_unit
            bid = round(min(action.bid, max_bid), 3)
        else:
            bid = 0.0  # budget exhausted: zero-cost zero-reward residue
        self.remaining -= cost_unit * bid
        self.moments_left -= 1
        return Action(action_id=action.action_id, action_type=action.action_type,
                      channel=action.channel, bid=bid, content=action.content)


AGENT_REGISTRY = {
    'baseline': BaselineAgent,
    'channel_only': ChannelOnly,
    'situation_only': SituationOnly,
    'noisy50': lambda: NoisyCAM(0.5, 'noisy50'),
    'noisy80': lambda: NoisyCAM(0.8, 'noisy80'),
    'cam_inferred': CAMInferred,
    'cam_learned': make_cam_learned,
    'oracle': CAMOracle,
    # env-aware: run_env special-cases this name and constructs with the env
    'bid_calibrated': lambda: BidCalibratedAgent(SimulationEnvironment(seed=0)),
}

DEFAULT_AGENTS = ['baseline', 'channel_only', 'situation_only', 'noisy50', 'noisy80',
                  'cam_inferred', 'cam_learned', 'oracle', 'bid_calibrated']

METRIC_KEYS = ['context_match_rate', 'total_profit', 'roas_aggregate', 'profit_per_cost', 'avg_reward', 'actions_skipped']


def compute_statistics(values_a: list, values_b: list) -> Optional[dict]:
    """Paired seed-level comparison (b vs a): t-test, Cohen's d, 95% diff CI."""
    if not values_a or not values_b or len(values_a) != len(values_b) or len(values_a) < 2:
        return None

    a = np.asarray(values_a, dtype=float)
    b = np.asarray(values_b, dtype=float)
    finite = np.isfinite(a) & np.isfinite(b)
    a, b = a[finite], b[finite]
    if len(a) < 2:
        return None

    pooled_std = np.sqrt((a.var(ddof=1) + b.var(ddof=1)) / 2)
    cohens_d = float((b.mean() - a.mean()) / pooled_std) if pooled_std > 0 else None

    try:
        t_stat, p_value = scipy.stats.ttest_rel(a, b)
        t_stat, p_value = float(t_stat), float(p_value)
    except Exception:
        t_stat, p_value = None, None

    diff = b - a
    diff_mean = float(diff.mean())
    diff_se = float(diff.std(ddof=1) / np.sqrt(len(diff)))
    return {
        'mean_a': round(float(a.mean()), 4),
        'mean_b': round(float(b.mean()), 4),
        'effect_size_cohens_d': round(cohens_d, 4) if cohens_d is not None else None,
        't_stat': round(t_stat, 4) if t_stat is not None else None,
        'p_value': p_value,
        'significant_p_0_05': bool(p_value is not None and p_value < 0.05),
        'diff_mean': round(diff_mean, 4),
        'diff_ci_95': [round(diff_mean - 1.96 * diff_se, 4), round(diff_mean + 1.96 * diff_se, 4)],
        'n_pairs': int(len(a)),
    }


def write_markdown_report(path: Path, seeds: List[int], scenarios: int,
                          aggregate: Dict[str, dict], statistics: Dict[str, dict]) -> None:
    """Generate a markdown results report from actual run output."""
    lines = [
        "# CAM-Sim Results (auto-generated)",
        "",
        f"Generated: {datetime.utcnow().isoformat()}  ",
        f"Seeds: {seeds}  |  Scenarios per seed: {scenarios}  ",
        "Reproducible: environment (numpy) and agents (stdlib random) both seeded per run.",
        "",
        "## Design",
        "",
        "Every agent acts on the SAME context sequence per seed (fair pairing).",
        "Ablation ladder measures performance as a function of context-awareness quality.",
        "`oracle` has ground-truth situation access — an upper bound by design, not a realistic agent.",
        "",
        "## Aggregate results (mean across seeds)",
        "",
        "| Agent | Context match % | Total profit | ROAS (agg.) | Profit/cost | Avg reward |",
        "|-------|-----------------|--------------|-------------|-------------|------------|",
    ]
    for name in aggregate:
        a = aggregate[name]
        roas = f"{a['roas_aggregate_mean']:.3f}" if a.get('roas_aggregate_mean') is not None else "n/a"
        lines.append(
            f"| {name} | {a['context_match_rate_mean']:.1f} | {a['total_profit_mean']:+.2f} "
            f"| {roas} | {a['profit_per_cost_mean']:+.3f} | {a['avg_reward_mean']:.3f} |"
        )
    lines += ["", "## Paired seed-level statistics vs baseline", ""]
    for name, stats in statistics.items():
        if name == 'baseline':
            continue
        lines.append(f"### {name} vs baseline")
        lines.append("")
        lines.append("| Metric | diff (mean) | 95% CI | t | p | Cohen's d | n | sig? |")
        lines.append("|--------|-------------|--------|---|---|-----------|---|------|")
        for metric, st in stats.items():
            if st is None:
                lines.append(f"| {metric} | — | — | — | — | — | — | n/a |")
                continue
            p_str = f"{st['p_value']:.2e}" if st['p_value'] is not None else "n/a"
            d_str = f"{st['effect_size_cohens_d']:.2f}" if st['effect_size_cohens_d'] is not None else "n/a"
            t_str = f"{st['t_stat']:.2f}" if st['t_stat'] is not None else "n/a"
            sig = "yes" if st['significant_p_0_05'] else "no"
            ci = f"[{st['diff_ci_95'][0]:+.3f}, {st['diff_ci_95'][1]:+.3f}]"
            lines.append(
                f"| {metric} | {st['diff_mean']:+.3f} | {ci} | {t_str} | {p_str} | {d_str} | {st['n_pairs']} | {sig} |"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def aggregate_seeds(per_seed_values, agent_names, metric_keys):
    """Aggregate per-seed metric lists into means/SDs/95% CIs (nan-safe)."""
    aggregate = {}
    for name in agent_names:
        agg = {}
        for key in metric_keys:
            arr = np.asarray(per_seed_values[key][name], dtype=float)
            finite = arr[np.isfinite(arr)]
            agg[key + '_mean'] = round(float(finite.mean()), 4) if len(finite) else None
            agg[key + '_std'] = round(float(finite.std(ddof=1)), 4) if len(finite) > 1 else None
            if len(finite) > 1:
                se = finite.std(ddof=1) / np.sqrt(len(finite))
                agg[key + '_ci95'] = [round(float(finite.mean() - 1.96 * se), 4),
                                      round(float(finite.mean() + 1.96 * se), 4)]
        aggregate[name] = agg
    return aggregate


def stats_vs_baseline(per_seed_values, agent_names, metric_keys):
    """Seed-level paired statistics vs baseline for every other agent."""
    statistics = {}
    if 'baseline' in agent_names:
        for name in agent_names:
            if name == 'baseline':
                continue
            statistics[name] = {key: compute_statistics(per_seed_values[key]['baseline'],
                                                        per_seed_values[key][name])
                                for key in metric_keys}
    return statistics


def run_env(env_config, seeds, scenarios, agent_names, capture_sample=False, extra_agent_factory=None):
    """Run all agents across seeds within ONE environment configuration.

    env_config=None means the default preset. extra_agent_factory (optional)
    appends one additional per-config agent (e.g. a recalibrated classifier).
    Returns (aggregate, statistics, per_seed_values, last_metrics, sample_contexts).
    """
    metric_keys = list(METRIC_KEYS)
    per_seed_values = {m: {n: [] for n in agent_names} for m in metric_keys}
    last_metrics = None
    sample_contexts = []
    for seed in seeds:
        # Seed BOTH the environment (numpy) and the agents (stdlib random).
        random.seed(seed)
        env = SimulationEnvironment(seed=seed, config=env_config)
        runner = BenchmarkRunner(env)

        # Generate the context sequence ONCE per seed -> every agent faces
        # identical scenarios (fair pairing).
        contexts = [env.generate_context() for _ in range(scenarios)]
        if capture_sample and not sample_contexts:
            sample_contexts = contexts[:10]

        agents = []
        for n in agent_names:
            if n == 'bid_calibrated':
                agents.append(BidCalibratedAgent(env))
            else:
                agents.append(AGENT_REGISTRY[n]())
        if extra_agent_factory is not None:
            agents.append(extra_agent_factory())
        budget = env.cfg.get('budget_per_episode')
        results = runner.run_benchmark(agents, contexts, budget=budget)
        metrics = runner.get_metrics(results)
        last_metrics = metrics

        for name in metrics:
            if name not in per_seed_values[metric_keys[0]]:
                for k in metric_keys:
                    per_seed_values[k][name] = []
            for key in metric_keys:
                value = metrics[name][key]
                per_seed_values[key][name].append(value if value is not None else float('nan'))

    all_names = list(per_seed_values[next(iter(per_seed_values))].keys())
    return (aggregate_seeds(per_seed_values, all_names, metric_keys),
            stats_vs_baseline(per_seed_values, all_names, metric_keys),
            per_seed_values, last_metrics, sample_contexts)


def run_alpha_sweep(seeds, scenarios, quiet=False, alphas=(0.0, 0.25, 0.5, 0.75, 1.0, 1.5)):
    """F8 follow-up: locate WHERE the F3 reversal starts as returns-to-bid vary.

    alpha=0.0 means no concavity (default economics). Agents: the
    bidding-relevant subset. Answers two questions: (1) at which curvature
    does calibrated bidding overtake flat bidding, and (2) does
    bid_calibrated (the true mechanism-aware ceiling) dominate everywhere —
    i.e. was the hand-set 'oracle' ever a real upper bound?
    """
    agent_names = ['baseline', 'situation_only', 'oracle', 'bid_calibrated']
    rows = []
    for alpha in alphas:
        cfg = {'bid_return_alpha': alpha} if alpha > 0 else None
        aggregate, _, per_seed, _, _ = run_env(cfg, seeds, scenarios, agent_names)
        profits = {n: aggregate[n]['total_profit_mean'] for n in agent_names}
        so = per_seed['total_profit']['situation_only']
        orc = per_seed['total_profit']['oracle']
        bc = per_seed['total_profit']['bid_calibrated']
        row = {
            'alpha': alpha,
            'profits': profits,
            'situation_vs_oracle': compute_statistics(orc, so),
            'situation_vs_calibrated': compute_statistics(bc, so),
            'oracle_vs_calibrated': compute_statistics(bc, orc),
        }
        rows.append(row)
        if not quiet:
            print(f"  alpha={alpha:<5} situation_only {profits['situation_only']:>+9.2f}   "
                  f"oracle {profits['oracle']:>+9.2f}   bid_calibrated {profits['bid_calibrated']:>+9.2f}")
    return rows


def run_label_noise_study(seeds, scenarios, quiet=False,
                          envs=('crisis_heavy', 'retention_heavy', 'uniform_situations'),
                          epsilons=(0.0, 0.05, 0.1, 0.2, 0.3)):
    """Deployment-realism check for the F6 remedy: recalibration trained on
    NOISY labels (each label flipped to a random other situation with prob
    epsilon). How fast does the remedy degrade as labeling quality drops?
    """
    rows = []
    for env_name in envs:
        overrides = dict(ENVIRONMENT_PRESETS[env_name])
        for eps in epsilons:
            th, lb = _fit_learner_for_config(overrides, label_noise=eps)
            factory = lambda th=th, lb=lb: CAMLearned(th, lb, name='cam_recalibrated')
            aggregate, _, _, _, _ = run_env(overrides, seeds, scenarios,
                                            ['noisy50'],
                                            extra_agent_factory=factory)
            rec = aggregate['cam_recalibrated']
            row = {'env': env_name, 'epsilon': eps,
                   'match_rate': rec['context_match_rate_mean'],
                   'profit': rec['total_profit_mean'],
                   'profit_ci95': rec['total_profit_ci95'],
                   'thresholds': th}
            rows.append(row)
            if not quiet:
                print(f"  {env_name:<18} eps={eps:<5} recal match {rec['context_match_rate_mean']:5.1f}%  "
                      f"profit {rec['total_profit_mean']:>+8.2f}")
    return rows


def run_budget_pacing_study(seeds, scenarios, quiet=False):
    """Limitation 'budget-unaware agents': does a standard EVEN-PACING rule
    (bid <= remaining/moments_left, per channel cost) change the conclusions
    under budget_constrained? Same wrapping logic for baseline, situation_only
    and oracle; each paced agent is paired against its unpaced twin.
    """
    overrides = dict(ENVIRONMENT_PRESETS['budget_constrained'])
    budget = overrides['budget_per_episode']
    names = ['baseline', 'situation_only', 'oracle']
    metric_keys = list(METRIC_KEYS)
    all_names = names + [f'{n}_paced' for n in names]
    per_seed_values = {m: {n: [] for n in all_names} for m in metric_keys}
    for seed in seeds:
        random.seed(seed)
        env = SimulationEnvironment(seed=seed, config=overrides)
        runner = BenchmarkRunner(env)
        contexts = [env.generate_context() for _ in range(scenarios)]
        agents = [AGENT_REGISTRY[n]() for n in names]
        agents += [BudgetPacedAgent(AGENT_REGISTRY[n](), budget, scenarios, env.action_costs)
                   for n in names]
        results = runner.run_benchmark(agents, contexts, budget=budget)
        metrics = runner.get_metrics(results)
        for n in all_names:
            for key in metric_keys:
                per_seed_values[key][n].append(metrics[n][key])
    aggregate = aggregate_seeds(per_seed_values, all_names, metric_keys)
    if not quiet:
        for n in all_names:
            a = aggregate[n]
            print(f"  {n:<20} profit {a['total_profit_mean']:>+9.2f}  "
                  f"skipped {a['actions_skipped_mean']:5.1f}")
    return aggregate


def check_ladder(profits: Dict[str, float], inferred_key: str = 'cam_inferred') -> Optional[bool]:
    """H4 dose-response by label ordering: noisy50 < <inferred_key> < noisy80 < oracle."""
    needed = ['noisy50', inferred_key, 'noisy80', 'oracle']
    if not all(a in profits and profits[a] is not None for a in needed):
        return None
    return profits['noisy50'] < profits[inferred_key] < profits['noisy80'] < profits['oracle']


def check_recal_healthy(profits: Dict[str, float]) -> Optional[bool]:
    """Recalibration remedy (F5): recal classifier must beat unbiased 50% noise.

    (Deliberately NOT a strict ladder check: a recalibrated classifier with
    >80% accuracy SHOULD exceed noisy80 — performance must follow perception
    quality, which the Spearman dose-response check below measures properly.)
    """
    if not all(a in profits and profits[a] is not None for a in ('cam_recalibrated', 'noisy50')):
        return None
    return profits['cam_recalibrated'] > profits['noisy50']


def dose_response_spearman(aggregate: Dict[str, dict]):
    """Agent-level dose-response: Spearman(match rate, profit) across agents.

    The proper H4 test: profit must increase with ACTUAL perception quality,
    regardless of agent labels.
    """
    xs, ys = [], []
    for v in aggregate.values():
        m, p = v.get('context_match_rate_mean'), v.get('total_profit_mean')
        if m is not None and p is not None and np.isfinite(m) and np.isfinite(p):
            xs.append(m)
            ys.append(p)
    if len(xs) < 3:
        return None, None
    rho, pval = scipy.stats.spearmanr(xs, ys)
    return float(rho), float(pval)


def check_f3(profits: Dict[str, float]) -> Optional[bool]:
    """F3: flat-bid perfect matching beats the oracle's context-inflated bidding."""
    if not all(a in profits and profits[a] is not None for a in ('situation_only', 'oracle')):
        return None
    return profits['situation_only'] > profits['oracle']


def run_robustness_sweep(seeds, scenarios, agent_names, quiet=False):
    """Run the ablation ladder across ALL environment presets."""
    rows = []
    if not quiet:
        print("\n" + "=" * 78)
        print(f"ROBUSTNESS SWEEP: {len(ENVIRONMENT_PRESETS)} environments x {len(seeds)} seeds")
        print("=" * 78)
    for env_name, overrides in ENVIRONMENT_PRESETS.items():
        cfg = dict(ENVIRONMENT_PRESETS['default'])
        cfg.update(overrides)
        # Per-environment RECALIBRATED classifier: fit on a labeled calibration
        # sample drawn from THIS distribution (F5 remedy test).
        th, lb = _fit_learner_for_config(overrides)
        extra_factory = lambda: CAMLearned(th, lb, name='cam_recalibrated')  # noqa: E731
        aggregate, _, per_seed, _, _ = run_env(cfg, seeds, scenarios, agent_names,
                                               extra_agent_factory=extra_factory)
        profits = {n: aggregate[n]['total_profit_mean'] for n in aggregate}
        rho, rho_p = dose_response_spearman(aggregate)
        # F3 needs a REAL test, not just a point-estimate comparison:
        # paired seed-level situation_only vs oracle (both exist in all runs).
        f3_stats = None
        if 'situation_only' in per_seed['total_profit'] and 'oracle' in per_seed['total_profit']:
            f3_stats = compute_statistics(per_seed['total_profit']['oracle'],
                                          per_seed['total_profit']['situation_only'])
        # Per-seed Spearman rho across agents (paired design: 50 replicates
        # of a 9-agent ranking) -> mean + 95% CI, instead of a single
        # pseudo-inferential p-value on non-independent agents.
        agent_list = list(aggregate.keys())
        seed_rhos = []
        n_seeds = len(per_seed['total_profit'][agent_list[0]])
        for i in range(n_seeds):
            xs = [per_seed['context_match_rate'][n][i] for n in agent_list]
            ys = [per_seed['total_profit'][n][i] for n in agent_list]
            if all(np.isfinite(xs)) and all(np.isfinite(ys)):
                seed_rhos.append(scipy.stats.spearmanr(xs, ys)[0])
        rho_seed_mean = float(np.mean(seed_rhos)) if seed_rhos else None
        rho_seed_ci = ([round(float(np.percentile(seed_rhos, 2.5)), 4),
                        round(float(np.percentile(seed_rhos, 97.5)), 4)]
                       if len(seed_rhos) > 1 else None)
        row = {
            'env': env_name,
            'config_overrides': {k: v for k, v in cfg.items() if k not in ('situation_weights',)},
            'situation_weights': [round(w, 4) for w in cfg['situation_weights']],
            'profits': profits,
            'ladder_ok': check_ladder(profits, 'cam_inferred'),
            'recal_healthy': check_recal_healthy(profits),
            'f3_ok': check_f3(profits),
            'f3_paired': f3_stats,
            'dose_response_spearman_rho': round(rho, 4) if rho is not None else None,
            'dose_response_spearman_p': rho_p,
            'rho_per_seed_mean': round(rho_seed_mean, 4) if rho_seed_mean is not None else None,
            'rho_per_seed_ci95': rho_seed_ci,
            'recal_thresholds': th,
            'hand_thresholds': [0.35, 0.65, 0.78],
        }
        rows.append(row)
        if not quiet:
            ladder = 'OK  ' if row['ladder_ok'] else 'FAIL'
            recal = 'OK  ' if row['recal_healthy'] else 'FAIL'
            f3 = 'OK  ' if row['f3_ok'] else 'FAIL'
            print(f"  {env_name:<20} situation_only {profits['situation_only']:>+9.2f}   "
                  f"oracle {profits['oracle']:>+9.2f}   "
                  f"baseline {profits['baseline']:>+9.2f}   "
                  f"hand={ladder} recal={recal}  F3={f3}  rho={row['dose_response_spearman_rho']}" +
                  (f"  F3-p={row['f3_paired']['p_value']:.1e}" if f3_stats else ""))
    return rows


def write_robustness_md(path: Path, seeds: List[int], scenarios: int, rows: List[dict]) -> None:
    """Write a robustness report from actual sweep output."""
    agents = list(rows[0]['profits'].keys()) if rows else []
    lines = [
        "# CAM-Sim Robustness Sweep (auto-generated)",
        "",
        f"Generated: {datetime.utcnow().isoformat()}  ",
        f"Environments: {[r['env'] for r in rows]}  |  Seeds: {len(seeds)}  |  Scenarios/seed: {scenarios}",
        "",
        "Situation->action language held fixed; ECONOMICS vary (situation distribution,",
        "reward scale, media costs, budget caps, bid-return curvature, context-payoff strength).",
        "cam_recalibrated = classifier fit per environment on a labeled calibration sample.",
        "",
        "| Environment | " + " | ".join(agents) + " | ladder (hand) | recal>noisy50 | F3 OK | rho(match,profit) |",
        "|-------------|" + "|".join(["--------"] * len(agents)) + "|------|------|------|------|",
    ]
    for r in rows:
        cells = " | ".join(f"{r['profits'].get(a, float('nan')):+.1f}" for a in agents)
        lh = "yes" if r['ladder_ok'] else "**NO**"
        lr = "yes" if r['recal_healthy'] else "**NO**"
        fp = r.get('f3_paired')
        if r['f3_ok']:
            f3 = f"yes (p={fp['p_value']:.0e})" if fp else "yes"
        else:
            f3 = f"**NO** (p={fp['p_value']:.0e})" if fp else "**NO**"
        rho = r.get('dose_response_spearman_rho')
        rho_s = f"{rho:.2f}" if rho is not None else "n/a"
        lines.append(f"| {r['env']} | {cells} | {lh} | {lr} | {f3} | {rho_s} |")
    lines += [
        "",
        "ladder (hand) = noisy50 < cam_inferred < noisy80 < oracle (H4, label ordering);",
        "recal>noisy50 = per-env recalibrated classifier beats unbiased 50% perception (F5 remedy);",
        "F3 = situation_only > oracle (action selection dominates bid modulation);",
        "rho = Spearman(context match rate, profit) across agents — the label-free dose-response test.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="CAM-Sim: Context-Aware Agentic Marketing Simulation"
    )
    parser.add_argument("--scenarios", "-n", type=int, default=200,
                        help="Number of scenarios per seed (default: 200)")
    parser.add_argument("--agents", "-a", type=str, default=",".join(DEFAULT_AGENTS),
                        help=f"Comma-separated agents (default: {','.join(DEFAULT_AGENTS)})")
    parser.add_argument("--seeds", "-S", type=str, default="1,2,3,4,5",
                        help="Comma-separated seed list (default: 1,2,3,4,5)")
    parser.add_argument("--output", "-o", type=str, default="results/cam_sim_results.json",
                        help="JSON output path")
    parser.add_argument("--output-md", type=str, default=None,
                        help="Markdown report output path (e.g. results/cam_sim_results.md)")
    parser.add_argument("--robustness", "-R", action="store_true",
                        help="Run the ablation across ALL environment presets (robustness sweep)")
    parser.add_argument("--alpha-sweep", action="store_true",
                        help="F8 stress test: vary returns-to-bid curvature alpha and locate the F3 reversal")
    parser.add_argument("--label-noise", action="store_true",
                        help="Stress test: recalibration with noisy calibration labels (deployment realism)")
    parser.add_argument("--budget-pacing", action="store_true",
                        help="Stress test: even-pacing wrappers under budget_constrained (budget-awareness)")
    parser.add_argument("--quiet", "-q", action="store_true")

    args = parser.parse_args()

    seeds = [int(s.strip()) for s in args.seeds.split(',') if s.strip()]
    selected_names = [n.strip() for n in args.agents.split(',') if n.strip() in AGENT_REGISTRY]
    if not selected_names:
        print(f"No valid agents selected. Available: {', '.join(AGENT_REGISTRY)}")
        sys.exit(1)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not args.quiet:
        print(f"Running CAM-Sim: {args.scenarios} scenarios x {len(seeds)} seeds")
        print(f"Agents: {selected_names}")
        print(f"Seeds: {seeds}")
        print()

    aggregate, statistics, per_seed_values, last_metrics, sample_contexts = run_env(
        None, seeds, args.scenarios, selected_names, capture_sample=True)

    # ---- Robustness sweep (optional) ----
    robustness_rows = None
    if args.robustness:
        robustness_rows = run_robustness_sweep(seeds, args.scenarios, selected_names,
                                               quiet=args.quiet)

    # ---- Stress tests (optional) ----
    alpha_rows = label_rows = pacing_aggregate = None
    if args.alpha_sweep:
        if not args.quiet:
            print("\nALPHA SWEEP (returns-to-bid curvature; alpha=0 = default economics)")
        alpha_rows = run_alpha_sweep(seeds, args.scenarios, quiet=args.quiet)
    if args.label_noise:
        if not args.quiet:
            print("\nLABEL-NOISE STUDY (recalibration under imperfect labeling)")
        label_rows = run_label_noise_study(seeds, args.scenarios, quiet=args.quiet)
    if args.budget_pacing:
        if not args.quiet:
            print("\nBUDGET PACING STUDY (even-pacing wrappers, budget_constrained env)")
        pacing_aggregate = run_budget_pacing_study(seeds, args.scenarios, quiet=args.quiet)

    # ---- Print ----
    if not args.quiet:
        print("=" * 78)
        print("CAM-Sim Multi-Seed Results (ablation ladder)")
        print("=" * 78)
        for name in selected_names:
            agg = aggregate[name]
            print(f"\n  {name:<15} match {agg['context_match_rate_mean']:>6.1f}%  "
                  f"profit {agg['total_profit_mean']:>+9.2f}  "
                  f"ROAS {agg['roas_aggregate_mean'] if agg['roas_aggregate_mean'] is not None else 'n/a':>7}  "
                  f"p/c {agg['profit_per_cost_mean']:>+.3f}")

        if statistics:
            print("\n" + "=" * 78)
            print("PAIRED SEED-LEVEL STATS vs BASELINE")
            print("=" * 78)
            for name, stats in statistics.items():
                st = stats['total_profit']
                if st is None:
                    continue
                sig = "yes" if st['significant_p_0_05'] else "NO"
                print(f"\n  {name:<15} profit diff {st['diff_mean']:>+8.2f} "
                      f"(CI {st['diff_ci_95'][0]:+.1f}..{st['diff_ci_95'][1]:+.1f})  "
                      f"p={st['p_value']:.2e}  d={st['effect_size_cohens_d'] if st['effect_size_cohens_d'] is not None else 'n/a'}  "
                      f"sig={sig}")

    # ---- Save JSON ----
    output_data = {
        'timestamp': datetime.utcnow().isoformat(),
        'scenarios_per_seed': args.scenarios,
        'seeds': seeds,
        'agents': selected_names,
        'design': 'shared-context-sequence-per-seed; both RNGs seeded; oracle=labeled upper bound',
        'aggregate_across_seeds': aggregate,
        'statistics_vs_baseline': statistics,
        'robustness_sweep': robustness_rows,
        'alpha_sweep': alpha_rows,
        'label_noise': label_rows,
        'budget_pacing': pacing_aggregate,
        'last_seed_metrics': last_metrics,
        'sample_contexts': [c.to_dict() for c in sample_contexts],
    }
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)

    # ---- Save Markdown ----
    if args.output_md:
        md_path = Path(args.output_md)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        write_markdown_report(md_path, seeds, args.scenarios, aggregate, statistics)
        if robustness_rows is not None:
            rb_path = md_path.with_name(md_path.stem + '_robustness.md')
            write_robustness_md(rb_path, seeds, args.scenarios, robustness_rows)
            if not args.quiet:
                print(f"✅ Robustness report: {rb_path}")
        stress_lines = []
        if alpha_rows is not None:
            stress_lines += [
                "", "## Alpha sweep: where does the F3 reversal start?", "",
                "alpha = returns-to-bid exponent (0 = no concavity = default economics).", "",
                "| alpha | baseline | situation_only | oracle | bid_calibrated | F3 (sit>oracle) p | sit-vs-calib p |",
                "|-------|----------|----------------|--------|----------------|-------------------|----------------|",
            ]
            for r in alpha_rows:
                p = r['profits']
                stress_lines.append(
                    f"| {r['alpha']} | {p['baseline']:+.1f} | {p['situation_only']:+.1f} | "
                    f"{p['oracle']:+.1f} | {p['bid_calibrated']:+.1f} | "
                    f"{r['situation_vs_oracle']['p_value']:.1e} | "
                    f"{r['situation_vs_calibrated']['p_value']:.1e} |")
            stress_lines += ["", f"(auto-generated from {len(seeds)} seeds x {args.scenarios} scenarios)", ""]
        if label_rows is not None:
            stress_lines += [
                "", "## Label-noise study: recalibration under imperfect labeling", "",
                "| env | epsilon | recal match % | recal profit | noisy50 (ref) |",
                "|-----|---------|---------------|--------------|----------------|",
            ]
            for r in label_rows:
                stress_lines.append(
                    f"| {r['env']} | {r['epsilon']} | {r['match_rate']:.1f} | "
                    f"{r['profit']:+.1f} | see robustness table |")
            stress_lines += [""]
        if pacing_aggregate is not None:
            stress_lines += [
                "", "## Budget pacing: even-pacing wrappers under budget_constrained", "",
                "| agent | profit | skipped/200 |",
                "|-------|--------|-------------|",
            ]
            for n, a in pacing_aggregate.items():
                stress_lines.append(
                    f"| {n} | {a['total_profit_mean']:+.1f} | {a['actions_skipped_mean']:.1f} |")
            stress_lines += [""]
        if stress_lines:
            with open(md_path, 'a', encoding='utf-8') as f:
                f.write("\n".join(stress_lines))
            if not args.quiet:
                print(f"✅ Stress-test sections appended: {md_path}")
        if not args.quiet:
            print(f"\n✅ Markdown report: {md_path}")

    if not args.quiet:
        print(f"✅ Results saved to: {output_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
