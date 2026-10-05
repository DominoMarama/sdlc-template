# capabilities.md — Agent Capabilities

## What the Agent Can Do

List the actions the agent is allowed to take without additional approval:

| Capability | Description |
|---|---|
| **Code generation** | Generate source files, configuration, tests, and documentation in your project's language |
| **Code review** | Review existing code against conventions; suggest improvements with citations |
| **CMake/package config** | Write build configuration and dependency entries (human runs the build) |
| **Task decomposition** | Break goals into independent, testable subtasks; identify when a goal should be its own task |
| **Deep-dive research** | Research dependencies and patterns from authoritative documentation sources (latest versions) |
| **GUI mockups** | Create wireframes and mockups for UI requirements before implementation |
| **State updates** | Update state.md after every step, not just at the end |
| **Validation** | Run validate_domain.py before and during tasks to verify domain integrity |

## What Agents Cannot Do (Without Explicit Approval)

| Action | Requires |
|---|---|
| Delete files or directories | Human approval |
| Push to remote repositories | Human approval |
| Modify DOMAIN.md or constraints | Human review |
| **Run build tools** | Human only — agent writes configuration; human executes builds |
| **Modify `scripts/validate_domain.py`** | Human authorization required — this is the validation guardrail itself |
| **Delete files or directories** | Human approval — agents may rename/move but not delete |
| **Modify DOMAIN.md** | Human review — agents propose changes; human approves and commits |
| **Change architecture/data models** | Decomposition + approval — agents propose; human reviews against domain rules |
| Change architecture/data models | Decomposition + approval |
| Add new dependencies | Human approval |
| Deploy to production | Human approval |

---

**Fill in the table above with your project-specific capabilities and
restrictions.** The agent will use this to know what it can do autonomously
and what requires your explicit approval.
