from dataclasses import dataclass, field

from .exceptions import RailDenied


@dataclass(frozen=True)
class RailDecision:
    allowed: bool
    reason: str


@dataclass
class RailPolicy:
    allowed_agents: set[str] = field(default_factory=set)
    allowed_actions: set[str] = field(default_factory=set)
    max_daily_actions: int | None = None
    _action_count: int = 0

    def check(self, *, agent: str, action: str) -> RailDecision:
        if self.allowed_agents and agent not in self.allowed_agents:
            return RailDecision(False, f"agent not allowed: {agent}")

        if self.allowed_actions and action not in self.allowed_actions:
            return RailDecision(False, f"action not allowed: {action}")

        if self.max_daily_actions is not None and self._action_count >= self.max_daily_actions:
            return RailDecision(False, "daily action quota exceeded")

        return RailDecision(True, "allowed")

    def assert_allowed(self, *, agent: str, action: str) -> None:
        decision = self.check(agent=agent, action=action)
        if not decision.allowed:
            raise RailDenied(decision.reason)
        self._action_count += 1
