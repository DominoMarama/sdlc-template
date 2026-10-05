# constraints.md — Non-Negotiable Constraints

> These are rules that MUST always be true, regardless of the task. Fill in
> additional project-specific constraints below. The SDLC workflow itself
> imposes these default constraints:

---

## SDLC Workflow Constraints

| Rule                                                                | Rationale                                                                                     |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **No code without approved plan + context + goals**                 | Domain bug prevention — prevents drift and ensures every change is intentional and documented |
| **Agents cannot modify DOMAIN.md without human review**             | The domain is the constitution; changes must be deliberate                                    |
| **Agents cannot modify validate_domain.py without human authorization** | The validation script defines what a properly set-up domain looks like; changing it could allow incomplete domains to pass validation, defeating the guardrail's purpose.
| **Agents cannot run build tools**                                   | Human verifies builds; agents write configuration only                                        |
| **Placeholder markers in domain files are not rules**               | `[FILL IN]`, `<!-- TODO -->`, etc. are reminders, not constraints. Never cite them as rules   |
| **Domain must be placeholder-free before loading to system prompt** | Incomplete domains lead to incorrect agent behavior                                           |

## Memory & Resource Safety

| Rule | Rationale |
|---|---|
| **No unmanaged resources** | All resources (files, handles, connections) must have a clear owner and cleanup path |
| **All file handles must be closed** | Use context managers or RAII; never rely on OS cleanup |
| **No raw pointer arithmetic** | Use safe abstractions; the language's safety features are part of the contract |

## Dependency Rules

| Rule                                                    | Rationale                                                                               |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **All dependencies via package manager**                | No manual downloads or inline code; everything goes through the declared package system |
| **Pin versions to specific commits or tagged releases** | Reproducible builds; avoid "it worked on my machine" drift                              |
| **No dev dependencies in production builds**            | Development tools should never ship with released artifacts                             |

## Build Rules

| Rule | Rationale |
|---|---|
| **Reproducible builds required** | Same source + same environment = same binary; no timestamps or random values in output |
| **Static analysis before commit** | Lint, type check, and format checks must pass before code is committed |
| **CI must pass all tests** | No merge without green CI; tests are the gate, not the human |

## Security Rules

| Rule | Rationale |
|---|---|
| **No hardcoded secrets** | Use environment variables or secret management; never commit API keys or tokens |
| **Input validation on all boundaries** | All user input must be validated and sanitized before processing |
| **Use parameterized queries only** | Prevent SQL injection; never concatenate user input into queries |

## [Add more constraint categories as needed]

| Rule | Rationale |
|---|---|
| **[Your rule]** | e.g., **[Your reason specific to your project]** |

---

**These default constraints apply to all projects using this template.** Add
project-specific rules to the tables above. The SDLC workflow constraints are
non-negotiable and cannot be removed.
