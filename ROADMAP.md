# Roadmap

## v0.1 Focus

The next release focuses on making the harness primitives more useful in real agent workflows.

## Planned Work

### Rate Limit Rails

GitHub issue: [#1](https://github.com/paopaonyapi-creator/nami-harness/issues/1)

Add a simple rate limit rail primitive for agent/action scoped execution limits.

### Budget Guard Brakes

GitHub issue: [#2](https://github.com/paopaonyapi-creator/nami-harness/issues/2)

Add a budget guard brake that can stop execution when a daily or per-run cost budget is exceeded.

### Stable Sensor Schema

GitHub issue: [#3](https://github.com/paopaonyapi-creator/nami-harness/issues/3)

Document and test a stable JSONL event schema with event type, timestamp, agent, action, correlation ID, status, and safe metadata.

### Hermes Integration Demo

GitHub issue: [#4](https://github.com/paopaonyapi-creator/nami-harness/issues/4)

Create a more complete demo showing how Hermes-style workers can be wrapped by `HarnessRuntime` in a production-like flow.

## Content Track

### Demo Video 01

GitHub issue: [#5](https://github.com/paopaonyapi-creator/nami-harness/issues/5)

Publish the first public demo explaining:

```text
Hermes = brain / agentic workforce
Nami Harness = rails / brakes / sensors / quality system
```

Script draft:

```text
docs/demo-video-01-script.md
```

## Current Release

```text
Repository: https://github.com/paopaonyapi-creator/nami-harness
Release: https://github.com/paopaonyapi-creator/nami-harness/releases/tag/v0.0.1
```
