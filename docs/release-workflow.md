# CI and validation — 4alvit/4alvit

This repository publishes a GitHub profile and maintains its source-validation
scripts. It uses the `validation-only` mode in `.release-policy.json`; there is no
application package, firmware build or deployment workflow.

## Required checks

`quality-gate.yml` runs the callable validation workflows and produces the
required **CI gate** status on pull requests and merge-queue commits. Missing,
failed and skipped validation workflows fail the gate. The workflow contract job
also runs on every pull request and checks the declared validation graph,
timeouts, immutable action references and a consistent CodeQL release.

The callable workflows are:

- `validate.yml`: Python E9/F lint, source syntax, actionlint semantics and validator regressions.
- `codeql.yml`: separate Python and GitHub Actions analyses.
- `workflow-validation.yml`: actionlint checks for automation entry points.
- `dependency-review.yml`: pull-request dependency review.

The workflow contract regressions exercise mutable actions, reusable workflows,
Docker references and inconsistent CodeQL upload versions. Source-validator
regressions cover ignored files, symlinks, YAML tags and safe error messages.

## Local validation

Follow [Contributing](../CONTRIBUTING.md) to install Python 3.12+, the hash-locked
parser, Ruff and actionlint. Run `bash scripts/ci.sh` to execute the local checks. The
vendored client can also invoke the policy's local check command:

```sh
python3 scripts/release.py check
python3 scripts/release.py status
```

Local validation does not publish or deploy anything. It checks this repository's
profile and CI code, not the runtime behavior of the linked application projects.
Nightly runs repeat validation without publishing synthetic application releases.

## Maintaining shared tooling

The release client and workflow contracts are vendored from
[`victron-venus/venus-os-ci-toolkit`](https://github.com/victron-venus/venus-os-ci-toolkit).
Changes to shared behavior should also be submitted upstream and retain the local
regressions. The consumer-specific checks and documentation must continue to match
this repository's validation-only policy. Existing review and security rules
remain required; a successful local command does not replace them.
