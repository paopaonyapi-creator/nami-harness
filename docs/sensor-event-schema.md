# Sensor Event Schema

## Version

```text
1.0
```

## Required fields

| Field | Type | Description |
| --- | --- | --- |
| `schema_version` | string | Sensor schema version. |
| `event_id` | string | Unique event identifier. |
| `timestamp` | string | UTC ISO-8601 timestamp. |
| `event_type` | string | Event name such as `harness.task.completed`. |
| `status` | string | `info`, `success`, or `error`. |
| `payload` | object | Event-specific payload. |
| `metadata` | object | Safe optional metadata. |

## Context fields

| Field | Type | Description |
| --- | --- | --- |
| `agent` | string or null | Agent name, when available. |
| `action` | string or null | Action name, when available. |
| `correlation_id` | string or null | Trace identifier shared by related events. |

## Runtime event types

```text
harness.task.requested
harness.task.started
harness.task.completed
harness.task.failed
```

## Safety rule

Sensor payloads must not include raw secrets, tokens, API keys, private logs, payment slips, or credential-bearing screenshots.

## Example

```json
{
  "action": "summarize",
  "agent": "hermes",
  "correlation_id": "trace-1",
  "event_id": "...",
  "event_type": "harness.task.completed",
  "metadata": {},
  "payload": {
    "action": "summarize",
    "agent": "hermes",
    "correlation_id": "trace-1",
    "output_keys": ["answer"]
  },
  "schema_version": "1.0",
  "status": "success",
  "timestamp": "2026-05-05T00:00:00+00:00"
}
```
