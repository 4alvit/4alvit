# Security policy

The maintained scope is the default branch's profile content, validation scripts
and GitHub workflows. Linked software projects have separate security policies.
Updates are proposed through reviewed pull requests and the required CI gate.

Report a potential vulnerability privately using
[GitHub security reporting](https://github.com/4alvit/4alvit/security/advisories/new).
Include the affected commit, reproduction steps, likely impact and any suggested
mitigation. Do not include live credentials or private operational data. If the
private form is unavailable, open a minimal public issue requesting a private
reporting channel without disclosing the vulnerability details.

Maintainers aim to acknowledge a report within 14 days, confirm impact, and
coordinate a correction and disclosure with the reporter. This is a response
policy, not a claim about historical reports. Confirmed actionable scanner
findings receive a fix or a documented technical resolution; they are not hidden
by disabling the scanner.

Validation requires no production credentials and does not deploy or control
hardware. Workflow references must use immutable commits or image digests;
parser dependencies use checked hashes. Source parsing does not instantiate YAML
objects. Never add tokens, private keys or local device configuration to the repo.

The local validation commands do not implement cryptography. The shared client's
network `status` operation delegates to GitHub CLI; use the
[verified helper TLS profile](docs/HELPER_TLS_PROFILE.md) to retain certificate
verification and disable smaller keys for that operation.
