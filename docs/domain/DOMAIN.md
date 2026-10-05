# DOMAIN.md — The Always-Present Knowledge Base

> **This is the constitution of your project.** Load this entire file into
> the system prompt or persistent vector store at session start. It never
> changes per task.

---

## 1. Capabilities

See `capabilities.md` for the full capability list. Key points:

- **Code Generation:** Generate source files, configuration, and tests
- **Code Review:** Review against conventions (naming, style, etc.)
- **Build Access:** Agent writes configuration; human runs the build. The
  agent may propose build changes but must not execute build tools.

### What Agents Cannot Do (Without Explicit Approval)

- Delete files or directories
- Push to remote repositories
- Modify DOMAIN.md or other domain-level docs without human review
- **Run build tools:** human only — agent writes configuration; human executes
  builds and verifies
- Change architecture/data models without decomposition

---

## 2. Conventions

See `conventions.md` for language-specific conventions.

---

## 3. Constraints

See `constraints.md` for the full constraint list. Key points:

### [Insert your key constraints here]

1. **[Your constraint 1]**
2. **[Your constraint 2]**
3. **[Your constraint 3]**

---

## 4. Terminology

See `terminology.md` for the glossary.

---

## 5. How to Use This Document

### For Agents

1. **Load DOMAIN.md at session start.** This is your single source of truth.
2. **Before every decision, check** the relevant section in DOMAIN.md.
3. **Never proceed without being able to cite** a domain rule that justifies
   your choice.
4. **Update state.md after every step**, not at the end.
5. **Remember: I write code, human builds.** Do not attempt to run the build.

### For Humans

### SDLC Workflow Rules (Domain Setup)

Before the domain is ready for use, complete the **domain-setup** task in
`docs/tasks/domain-setup/`. This task gathers project-specific information
and fills in the template placeholders. The domain is only loadable into the
system prompt after this task completes with zero placeholders remaining.

#### Domain Readiness Checklist

The domain is ready to load when all of the following are true:

- [ ] All `*.md` files have no `[FILL IN]`, `<!-- -->`, or similar placeholder markers
- [ ] `validate_domain.py` passes with exit code 0
- [ ] The domain-setup task has an approved plan and completed state
- [ ] No task goals reference "example" or template content

#### Important: No Placeholder Rules

Placeholder markers (e.g., `[FILL IN...]`, `<!-- TODO -->`) are **not** rules.
They are reminders to complete the domain setup. Never cite a placeholder as
a domain rule — this is a domain-level violation. If you encounter a placeholder,
the correct action is to create a domain-setup task to fill it in, not to
proceed with code that depends on it.

---

1. **Read DOMAIN.md before reviewing any plan.** It tells you what the agent
   is allowed to do and what rules it must follow.
2. **Approve plans by checking they reference domain rules.** If a plan doesn't
   cite DOMAIN.md, ask for the citation.
3. **Reject any plan that violates constraints.**
4. **Keep DOMAIN.md updated** whenever you change project conventions — this
   is the most important maintenance task.
