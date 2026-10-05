# terminology.md — Glossary

> Replace this placeholder with your project's actual terminology.
> Use this to define key terms used throughout the domain documentation.

---

| Term | Definition |
|---|---|
| **Domain Layer** | The always-present knowledge base (`docs/domain/`). Contains conventions, constraints, and capabilities. Loaded once at session start. This is the project's constitution — stable across all tasks. |
| **Problem** | The task-specific instantiation (`docs/tasks/<task-id>/`). Contains goals, approved plan, and current state for this specific task. |
| **System Prompt** | The initial context injected at session start, containing the full DOMAIN.md. This is where agents always have access to project knowledge. |
| **Plan** | A sequence of steps the agent proposes to accomplish the task. Written in `plan.md`, approved by human before any code is written. |
| **State** | Current progress snapshot of the task. Written in `state.md`, updated after each step. |
| **Context** | Deep-dive reference into specific domain sections relevant to the current task. Written in `context.md`. |
| **Goal** | A decomposed, actionable subtask. Written in `goals.json`. Each goal is independent and testable. |
| **Invariant** | A rule that must always be true, regardless of task. |
| **Constraint** | A limitation or restriction that applies to the project. |
| **Capability** | Something the agent is allowed to do — not building.
| **Project Layer** | Task-agnostic knowledge between domain and problem (`docs/project/`). Accumulates research notes, UI mocks, class definitions, and quick references. Tasks cite and update it rather than re-discovering facts. |
| **Build Gate** | Human-only: agent writes configuration, human runs the build. |

---

**Add your project-specific terms to the table above.** These definitions
ensure that the agent and human share a common vocabulary when discussing
the project.
