# Release v0.0.1

## Purpose

First public skeleton of the Nami Harness OSS pillar.

```text
Hermes = brain / agentic workforce
Nami Harness = rails / brakes / sensors / quality system
```

## Included

- Rails policy allowlist and quota primitive.
- File kill switch.
- Circuit breaker.
- JSONL sensor events.
- Quality gate checks.
- Integrated `HarnessRuntime`.
- Example Hermes worker guard.
- Tests and GitHub Actions CI.

## Verification

```powershell
python -m pytest
```

Expected result:

```text
14 passed
```

## Publish checklist

- [ ] Create GitHub org or repo location.
- [ ] Initialize git repository.
- [ ] Commit v0.0.1 skeleton.
- [ ] Push to GitHub.
- [ ] Create tag `v0.0.1`.
- [ ] Add repo link to content plan.
- [ ] Record first demo video script.
