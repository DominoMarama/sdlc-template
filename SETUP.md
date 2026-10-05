# SDLC Domain Template

A language-agnostic template for setting up the Domain/Problem documentation
structure used by this agent system. Clone this repository as a new project
root (preferred) or copy its `docs/` contents into an existing project. The
domain files come pre-filled with working defaults; answer the clarifying
questions to customize them for your project.

## What This Is

This template provides the skeleton for three layers of documentation:

```
┌─────────────────────────────────────────┐
│         DOMAIN LAYER (Always Present)   │
│                                        │
│  capabilities.md   ← What you can do    │
│  conventions.md    ← How you write     │
│  constraints.md    ← Rules you follow  │
│  terminology.md    ← Glossary          │
│  DOMAIN.md         ← Your constitution │
└───────────────┬─────────────────────────┘
                │ Loaded once, referenced always
                ▼
┌─────────────────────────────────────────┐
│      PROJECT LAYER (Task-Agnostic)      │
│                                        │
│  research/    ← Research notes         │
│  design/      ← UI mocks, specs        │
│  reference/   ← Class definitions      │
│  architecture/← System diagrams        │
└───────────────┬─────────────────────────┘
                │ Tasks cite and update
                ▼
┌─────────────────────────────────────────┐
│        PROBLEM LAYER (Per Task)         │
│                                        │
│  plan.md      ← Agent proposes → Human approves
│  context.md   ← Deep-dive into domain    │
│  goals.json   ← Structured decomposition │
│  state.md     ← Progress snapshot       │
└─────────────────────────────────────────┘
```

## Quick Start

This template provides two ways to set up a new project:

### Method A: Clone as Project Root (Preferred)

Clone the template repository and use it directly as your project root. The
domain files (`docs/domain/`) and validation script (`scripts/`) are already
in place:

```bash
git clone https://github.com/your-org/sdlc-template.git my-project
cd my-project
```

### Method B: Copy Contents into Existing Project

Clone the template to a temporary location, then copy its `docs/` and
`scripts/` contents into your existing project:

```bash
git clone https://github.com/your-org/sdlc-template.git /tmp/sdlc-template-source
cd my-existing-project
cp -r /tmp/sdlc-template-source/docs/* docs/
cp -r /tmp/sdlc-template-source/scripts/ scripts/
```

After either method, continue with the remaining steps:

1. **Review** the domain files in `docs/domain/` — they come pre-filled
   with working defaults, no placeholders.

2. **Answer** the clarifying questions in this README to fill in the
   blanks appropriately for your project.

3. **Complete the domain-setup task** in `docs/tasks/domain-setup/`. This
   is the first task for any new project. The domain is only loadable when
   this task completes with zero placeholders remaining.

4. **Create** the project layer: `docs/project/` with research/, design/,
   reference/, architecture/ subdirectories. Tasks will populate these as they go
   with task-agnostic knowledge (research notes, UI mocks, class definitions).

5. **Load** the completed DOMAIN.md into your agent's system prompt at
   session start. The domain must pass validate_domain.py (exit code 0)
   before loading.

## Clarifying Questions

Before you finalize the domain, answer these questions for your project:

### 1. What is your project?

What language/paradigm does it use? This determines what goes into
`capabilities.md` and `conventions.md`.

### 2. What are your non-negotiable constraints?

List rules that must always be true, regardless of task. Examples:
- No external dependencies without approval
- All functions must have unit tests
- Linting/formatting with specific toolchain

Write these in `constraints.md`.

### 3. What is your sandbox's build access policy?

Specify whether agents can run build tools, and if so, which ones. Update
`docs/domain/DOMAIN.md` (section "What Agents Cannot Do") and
`docs/domain/capabilities.md` (the "Run build tools" row). Examples:

- "Agents cannot run any build tools — human runs all builds"
- "Agents can run `go build` but not `docker build`"
- "Agents can configure build files; human runs the build"
- "Agents can run `npm ci` and `npm run build`"

### 4. What capabilities should the agent have?

What is the agent allowed to do? Examples:
- Code generation in your language
- Writing tests
- Refactoring
- No database changes
- No deployment scripts

Write these in `capabilities.md`.

### 5. What naming/convention rules apply?

File naming, function naming, import organization, comment style,
error handling pattern — put these in `conventions.md`.

### 6. What does "done" look like for your project?

Define success criteria so the agent and human can agree on when a
task is complete. This goes in each task's `goals.json`.

### 7. What version control system do you use?

Specify your VCS and any repository conventions. Examples:
- "Git, with commits reviewed before push"
- "Git with conventional commit messages"
- "No remote repo yet — local development only"
- "Git with protected main branch, PR required"

Update `constraints.md` (dependency rules, push policies) and
`conventions.md` (commit message format, branching strategy) as needed.

## File-by-File Guide

All domain files are pre-filled with working defaults. Review them and fill
in project-specific details where indicated.

### DOMAIN.md

The constitution of your project. Already includes:
- Capabilities (code generation, review, configuration)
- Conventions (naming, SDLC workflow)
- Constraints (dependencies, build rules, security)
- Terminology (domain/problem/system prompt/plan/state/goal/etc.)

Fill in additional project-specific constraints and conventions as needed.

### capabilities.md

List what the agent is allowed to do: code generation, refactoring,
test writing, configuration, etc. Also list what it cannot do
without explicit approval.

### conventions.md

Language-specific conventions: naming, formatting, error handling,
logging, testing patterns, file organization.

### constraints.md

Non-negotiable rules: memory safety, dependency policies, build
requirements, security rules, etc.

### terminology.md

Glossary of key terms used in your project domain.

### Task Folder Structure (docs/tasks/<task-id>/)

For each task, create these files:

| File | Purpose |
|---|---|
| `plan.md` | Agent proposes steps → Human approves |
| `context.md` | Deep-dive into relevant domain sections |
| `goals.json` | Structured, testable subtasks |
| `state.md` | Progress snapshot, updated after each step |

## Workflow Summary

1. **Before any code:** Create plan.md + context.md + goals.json
2. **Human reviews** plan against DOMAIN.md constraints
3. **Human approves** → agent executes
4. **Agent updates state.md** after every step
5. **Human builds/verifies** — agent cannot build

## Adapting from This Template

This template is designed to be cloned as a new project (Method A) or
copied into an existing project (Method B). The domain files come
pre-filled with working defaults — review them and answer the clarifying
questions to customize for your specific project. No placeholder renaming
or file creation is needed.

The template itself contains no language-specific code or dependencies.
All project-specific conventions, constraints, and capabilities are filled
in during setup. The pre-filled files provide a clean, neutral starting
point that you adapt to your own technology stack.
