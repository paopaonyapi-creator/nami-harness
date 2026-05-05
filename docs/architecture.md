# Architecture

## Split of responsibilities

```text
Hermes = brain / agentic workforce
Nami Harness = rails / brakes / sensors / quality system
```

Hermes is allowed to think and act. Harness decides what actions are allowed, when execution must stop, what must be observed, and whether output is safe enough to ship.

## Hermes side

Hermes owns:

- Planning.
- Tool selection.
- Agent dispatch.
- Worker orchestration.
- Memory lookup.
- Task decomposition.
- Drafting outputs.

Hermes should not own final safety authority.

## Harness side

Nami Harness owns:

- **Rails**: who can do what, under which scope, with which quota.
- **Brakes**: kill switch, circuit breaker, budget stop, and cooldown.
- **Sensors**: trace events, audit records, health snapshots, and cost signals.
- **Quality**: validation gates, regression checks, replay, and release criteria.

## Control flow

```text
User / system request
  -> Hermes plans
  -> Harness rails authorize scope
  -> Hermes executes via workers
  -> Harness sensors record trace
  -> Harness brakes can stop execution
  -> Harness quality validates output
  -> result can be shipped
```

## Invariants

- No agent bypasses rails.
- No kill switch bypass exists.
- Every important action emits a sensor event.
- Output is not considered shippable until quality gates pass.
- Secrets are never logged in sensor payloads.
