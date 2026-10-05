# plan.md — Domain Setup Task

> **This is the first task for any new project.** Complete this task before
> any code tasks. The goal is to review the pre-filled domain files, answer
> the clarifying questions in SETUP.md, and customize them for your specific
> project.

---

## Task Description

Set up the domain documentation with project-specific rules and conventions.
The domain files come **pre-filled with working defaults** — your job is to
review them, answer the clarifying questions in `SETUP.md`, and fill in
project-specific details where indicated.

**Critical:** The domain is only ready to load into the system prompt when
this task completes with all clarifying questions answered and
`validate_domain.py` exiting with code 0.

### Goals

| ID     | Title                             | Description                                                                                                  |
| ------ | --------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **G1** | Review and customize domain files | Read each domain file, identify what needs project-specific customization, and fill in the details           |
| **G2** | Answer clarifying questions       | Answer all 7 clarifying questions in `SETUP.md` to gather project information                                |
| **G3** | Create project README.md          | Synthesize customized domain files and answers into a GitHub-style project README                            |
| **G4** | Research dependencies             | Research dependencies, patterns, and tools from authoritative documentation sources (latest stable versions) |
| **G5** | Validate and finalize             | Run `validate_domain.py`, confirm exit code 0, and update state.md                                           |

### Domain Rules Being Applied

- `docs/domain/conventions.md`: SDLC workflow conventions
- `docs/domain/constraints.md`: SDLC workflow constraints
- `docs/domain/DOMAIN.md`: SDLC workflow rules section

### Error Recovery Guide

| Symptom | Recovery |
|---|---|
| **validate_domain.py fails** | 1. Run it to see exact errors<br>2. Fix each error one at a time<br>3. Re-run until exit code 0 |
| **Unclear what to customize** | 1. Re-read the SETUP.md clarifying questions<br>2. Check which file section matches your question<br>3. If still unclear, ask the human for guidance |
| **Goal is too large for this task** | 1. Cite `conventions.md`'s "Task decomposition" capability<br>2. Propose splitting into a separate task with its own plan/context/goals/state |

### Quality Gates

- [ ] All 7 clarifying questions in SETUP.md have been answered
- [ ] Domain files have been reviewed and customized where needed
- [ ] `validate_domain.py` exits with code 0
- [ ] State.md updated after each step
- [ ] No goals left incomplete without a decision

---

## How to Recognize When a Goal Should Be Its Own Task

During this domain setup, you may encounter goals that are too large or complex
for a single task. Propose a split when:

1. **The goal spans multiple domains** — e.g., setting up both the build system
   and the testing framework. Split into "Build Setup" and "Test Setup" tasks.
2. **The goal requires significant research** — e.g., researching a new language
   or framework. Split into a "Research" task that produces reference documents.
3. **The goal is a prerequisite for other tasks** — e.g., domain setup must
   complete before code tasks can start. Make it a dependency.

In your plan.md, cite `conventions.md`'s "Task decomposition" capability and
propose the split as a separate task with its own domain-setup phase if needed.

---

## Approval

**Human reviewer:** _________________________

**Date:** _________________________

**Approved:** [ ] Yes  [ ] No (with comments: _____________)
