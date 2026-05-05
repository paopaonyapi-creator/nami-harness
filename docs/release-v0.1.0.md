# Release v0.1.0

## Purpose

First practical roadmap release for Nami Harness after the v0.0.1 skeleton.

```text
Hermes = brain / agentic workforce
Nami Harness = rails / brakes / sensors / quality system
```

## Added

- `RateLimitRail` for agent/action scoped execution windows.
- `BudgetGuard` for per-run or daily cost stops.
- Stable sensor event schema fields.
- Sensor event schema documentation.
- Runtime budget guard integration.
- Hermes runtime pipeline example.
- Tests for rate limits, budget guards, sensor schema, and budget-aware runtime execution.

## Verification

```powershell
python -m pytest
python examples\hermes_worker_guard.py
python examples\hermes_runtime_pipeline.py
```

Expected result:

```text
22 passed
Hermes processed: summarize the service health report
Hermes routed and completed: summarize the agent health report
```

## Links

```text
Repository: https://github.com/paopaonyapi-creator/nami-harness
Release: https://github.com/paopaonyapi-creator/nami-harness/releases/tag/v0.1.0
Sensor schema: docs/sensor-event-schema.md
Hermes pipeline demo: examples/hermes_runtime_pipeline.py
```
