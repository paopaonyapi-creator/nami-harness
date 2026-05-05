import pytest

from nami_harness.exceptions import RailDenied
from nami_harness.rails import RailPolicy


def test_rail_policy_allows_known_agent_action() -> None:
    policy = RailPolicy(allowed_agents={"hermes"}, allowed_actions={"summarize"})

    policy.assert_allowed(agent="hermes", action="summarize")


def test_rail_policy_denies_unknown_agent() -> None:
    policy = RailPolicy(allowed_agents={"hermes"})

    with pytest.raises(RailDenied):
        policy.assert_allowed(agent="unknown", action="summarize")


def test_rail_policy_enforces_quota() -> None:
    policy = RailPolicy(max_daily_actions=1)

    policy.assert_allowed(agent="hermes", action="summarize")

    with pytest.raises(RailDenied):
        policy.assert_allowed(agent="hermes", action="summarize")
