# Contributing

This repository maintains the public GitHub profile and the scripts and workflows
which validate its source. The linked application repositories have their own
contribution and release policies.

Open an issue for an incorrect link, documentation problem or reproducible
validation defect. Include the command, operating system, Python version and a
minimal example; remove tokens, private URLs and personal configuration. Use
[SECURITY.md](SECURITY.md) for potential vulnerabilities.

Propose changes through a pull request. Keep links and project descriptions
accurate, explain the behavior change, and include a regression test for changed
validation behavior. Preserve copyright and license notices in vendored tooling.
Do not change the required gate or disable a scanner to hide a failure.

## Local validation

Use Python 3.12 or newer, Git, Bash, Node.js and actionlint 1.7.12. Set up a virtual
environment, then run:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --require-hashes --only-binary=:all: -r .github/requirements-workflow-contracts.txt -r .github/requirements-lint.txt
bash scripts/ci.sh
```

The local command checks Python for syntax/name/import errors (Ruff E9/F), then parses tracked and nonignored source/configuration files,
validates workflow semantics with actionlint, checks immutable action references
and consistent CodeQL releases, and runs the unittest regressions. YAML is parsed
without constructing tagged Python objects. CI separately runs CodeQL for both
Python and GitHub Actions and dependency review.

The scripts report paths and error locations without quoting source values.
No application is built or deployed here; successful syntax/contract checks do
not demonstrate behavior of the linked hardware or services. Git commits identify
profile and validator changes. This repository uses a validation-only policy and
has no application package release process.

See [validation interfaces](docs/VALIDATION_INTERFACE.md) for inputs, outputs,
exit statuses and the profile's continuous-delivery/source-identity model.
