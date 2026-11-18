# Documentation

This repository publishes the `4alvit` GitHub profile page, together with the
validation that keeps the displayed result reproducible from tracked source.

## Validation

- [Profile validation interface](VALIDATION_INTERFACE.md) — the deployed result is the profile README, and the checks that gate it.
- [CI and release policy](CI_WORKFLOW.md) — the validation-only policy and what the Quality gate runs on each event.
- [CI orchestration](CI-ORCHESTRATION.md) — how the Quality gate and release pipeline split pull-request, merge-queue and default-branch work.
- [Profile helper TLS profile](HELPER_TLS_PROFILE.md) — the verified `gh` transport profile used by the shared status helper.

## Release records

- [CI and validation](release-workflow.md) — generated policy record for `4alvit/4alvit`.
