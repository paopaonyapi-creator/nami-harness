# Nami Harness

Nami Harness is the safety and quality layer for agentic systems.

## Core model

```text
Hermes = brain / agentic workforce
Harness Engineering = rails / brakes / sensors / quality system
```

Hermes decides, plans, delegates, and runs agentic labor. Nami Harness constrains, observes, and validates that labor before it can damage systems, budgets, users, or reputation.

## Layers

- **Rails**: route permissions, scope boundaries, quotas, and policy decisions.
- **Brakes**: kill switches, circuit breakers, cooldowns, and hard stops.
- **Sensors**: traces, events, costs, health, and audit records.
- **Quality**: checks, replay, evals, regressions, and release gates.

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]
pytest
```

## Minimal example

```python
from nami_harness.quality import QualityGate, require_non_empty
from nami_harness.rails import RailPolicy
from nami_harness.runtime import HarnessContext, HarnessRuntime
from nami_harness.sensors import JsonlSensor

policy = RailPolicy(allowed_agents={"hermes"}, allowed_actions={"summarize"})
gate = QualityGate([require_non_empty("answer")])
sensor = JsonlSensor("events.jsonl")
runtime = HarnessRuntime(rails=policy, quality=gate, sensor=sensor)

result = runtime.run(
    HarnessContext(agent="hermes", action="summarize"),
    {"input": "hello"},
    lambda payload: {"answer": payload["input"].upper()},
)

print(result.output)
```

## Status

Version `0.0.1` is the first open-source skeleton for the Harness Engineering pillar.
