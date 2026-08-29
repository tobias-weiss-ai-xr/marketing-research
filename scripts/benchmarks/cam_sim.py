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

    def __init__(self, seed: Optional[int] = None):
        self.rng = np.random.RandomState(seed)
        self.scenario_counter = 0

    def _random_situation(self) -> SituationType:
        situations = list(SituationType)
        choice = self.rng.choice(len(situations), p=self.SITUATION_WEIGHTS)
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
        base_reward = self.BASE_REWARDS[(action.action_type, context.situation)]

        context_match = (action.action_type == IDEAL_ACTION[context.situation])
        context_bonus = 0.5 if context_match else -0.3

        optimal_bid = 1.0 * context.audience_intent_strength * context.channel_quality
        bid_ratio = action.bid / optimal_bid if optimal_bid > 0 else 0
        if 0.8 <= bid_ratio <= 1.2:
            bid_efficiency = 0.3
        elif 0.5 <= bid_ratio <= 1.5:
            bid_efficiency = 0.1
        else:
            bid_efficiency = -0.2

        competitive_factor = 1.0 - context.competitive_density * 0.5
        total_reward = (base_reward + context_bonus + bid_efficiency) * competitive_factor
        cost = self.ACTION_COSTS[action.channel] * action.bid
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

    def run_benchmark(self, agents: List[Agent], contexts: List[FullContext]) -> Dict[str, List[ActionResult]]:
        """Run every agent against the SAME context sequence (fair pairing)."""
        all_results = {}
        for agent in agents:
            agent.reset()
            results = []
            for context in contexts:
                action = agent.decide(context)
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
            }
        return metrics


AGENT_REGISTRY = {
    'baseline': BaselineAgent,
    'channel_only': ChannelOnly,
    'situation_only': SituationOnly,
    'noisy50': lambda: NoisyCAM(0.5, 'noisy50'),
    'noisy80': lambda: NoisyCAM(0.8, 'noisy80'),
    'cam_inferred': CAMInferred,
    'oracle': CAMOracle,
}

DEFAULT_AGENTS = ['baseline', 'channel_only', 'situation_only', 'noisy50', 'noisy80', 'cam_inferred', 'oracle']

METRIC_KEYS = ['context_match_rate', 'total_profit', 'roas_aggregate', 'profit_per_cost', 'avg_reward']


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

    metric_keys = [m for m in METRIC_KEYS if m != 'roas_aggregate'] + ['roas_aggregate']
    per_seed_values = {m: {n: [] for n in selected_names} for m in metric_keys}
    last_metrics = None
    sample_contexts = []

    for seed in seeds:
        # Seed BOTH the environment (numpy) and the agents (stdlib random).
        random.seed(seed)
        env = SimulationEnvironment(seed=seed)
        runner = BenchmarkRunner(env)

        # Generate the context sequence ONCE per seed -> every agent faces
        # identical scenarios (fair pairing).
        contexts = [env.generate_context() for _ in range(args.scenarios)]
        if not sample_contexts:
            sample_contexts = contexts[:10]

        agents = [AGENT_REGISTRY[n]() for n in selected_names]
        results = runner.run_benchmark(agents, contexts)
        metrics = runner.get_metrics(results)
        last_metrics = metrics

        for name in selected_names:
            for key in metric_keys:
                value = metrics[name][key]
                per_seed_values[key][name].append(value if value is not None else float('nan'))

    # Aggregate across seeds (nan-safe)
    aggregate = {}
    for name in selected_names:
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

    # Seed-level paired statistics: every agent vs baseline
    statistics = {}
    if 'baseline' in selected_names:
        for name in selected_names:
            if name == 'baseline':
                continue
            statistics[name] = {key: compute_statistics(per_seed_values[key]['baseline'],
                                                        per_seed_values[key][name])
                                for key in metric_keys}

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
        if not args.quiet:
            print(f"\n✅ Markdown report: {md_path}")

    if not args.quiet:
        print(f"✅ Results saved to: {output_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
