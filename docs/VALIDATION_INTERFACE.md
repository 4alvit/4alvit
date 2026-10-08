# Profile validation interface

The deployed result is the README shown on the single `4alvit` GitHub profile.
GitHub displays changes from the default branch; there is no separately installed
application, firmware or reusable binary. The full Git commit ID identifies a
profile/source revision. Include `git rev-parse HEAD` in a bug report. The linked
projects have their own versions and release notes; a profile update is not a
release of those projects.

## Local commands

Install the tools listed in [Contributing](../CONTRIBUTING.md), then run from the
repository root:

- `bash scripts/ci.sh` checks Python errors, source syntax, workflow contracts and
  the unittest suite. It stops with a nonzero exit status on a failed check.
- `python3 scripts/validate-source.py` reads `.release-policy.json` and the Git
  tracked/nonignored files. It skips symlinks and optional `syntax_exclude`
  entries, parses Python/JSON/YAML, and invokes Bash/Node syntax checks plus
  actionlint. Success prints counts by extension. Errors identify the path and
  error location without quoting source values. YAML tags are parsed without
  constructing application objects or resolving includes.
- `python3 scripts/workflow_contracts.py` checks `.release-policy.json` against
  the workflows and reports contract errors with a nonzero exit status.
- `python3 -m unittest discover -s .github/workflow-tests -p 'test_*.py' -v` runs
  the source-parser and workflow-contract regressions without credentials.

These commands read repository files and run local tools. They do not run the
linked applications or demonstrate their operational safety.

## Shared helper

`scripts/release.py` is the shared toolkit client, used here with the checked-in
`validation-only` policy:

- `check` runs the policy's `local_checks` command (`bash scripts/ci.sh`).
- `status` invokes `gh run list` for this repository's `quality-gate.yml`, printing
  up to ten recent runs. This is the normal network operation; use the
  [helper TLS profile](HELPER_TLS_PROFILE.md) for the verified GitHub CLI runtime.
- `doctor` prints JSON identifying this repository, validation-only mode and
  `release_environment_required: false`. With this policy it needs no network.
- `--help` describes the shared parser. Its generic package/release commands are
  not supported delivery operations for this profile. Release dispatch rejects
  this policy; no packaging adapter or application version is configured.

Successful operations return zero. The client reports operational errors on
standard error as `release: ...` and returns one; invalid command syntax is
reported by argparse. Repository files are trusted local code: review a checkout
before running its scripts or policy commands.

This single-site profile is delivered continuously rather than through numbered
application releases. Pull requests describe the actual profile/validator change
and its impact. We do not create synthetic release packages or claim that a raw
Git log is a set of application release notes.
