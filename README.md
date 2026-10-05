# SDLC Domain Template

A reusable, language-agnostic template for setting up the **Domain/Problem**
documentation hierarchy used by agentic AI systems. Use it to prevent context
loss, keep agents aligned with your project rules, and maintain a consistent
SDLC across all tasks.

## The Problem: Agents Lose Context

Agentic AI systems work by injecting knowledge into a "system prompt." Over time,
as tasks accumulate, this prompt grows unwieldy, rules get mixed with task-specific
details, and agents start making decisions based on outdated or conflicting
information. The result: drift, inconsistent code, and surprises.

## The Solution: Three-Layer Documentation

This template implements a three-layer documentation structure:

```
┌─────────────────────────────────────────┐
│        DOMAIN LAYER (Always Present)    │
│  docs/domain/ — loaded once, never     │
│  changes per task                      │
│  • DOMAIN.md   — constitution          │
│  • capabilities.md  — agent powers    │
│  • conventions.md   — how you write  │
│  • constraints.md   — rules you follow│
│  • terminology.md   — glossary       │
└────────────┬────────────────────────────┘
             │ Loaded once, referenced always
             ▼
┌─────────────────────────────────────────┐
│      PROJECT LAYER (Task-Agnostic)      │
│  docs/project/ — grows over time       │
│  • research/     — research notes     │
│  • design/       — UI mocks, specs    │
│  • reference/    — class definitions  │
│  • architecture/ — system diagrams    │
└────────────┬────────────────────────────┘
             │ Tasks cite and update
             ▼
┌─────────────────────────────────────────┐
│       PROBLEM LAYER (Per Task)          │
│  docs/tasks/<task-id>/ — task-specific │
│  • plan.md      — agent proposes       │
│  • context.md   — deep-dive lookup    │
│  • goals.json   — structured steps    │
│  • state.md     — progress tracking   │
└─────────────────────────────────────────┘
```

**The domain layer is your constitution** — stable, always-present rules that
never change per task. **The project layer is your growing knowledge base** —
task-agnostic facts that accumulate so future tasks cite and update rather than
re-discover. **The problem layer is your execution log** — task-specific
instantiation that gets created, approved, and completed.

This three-layer separation prevents agents from mixing general knowledge with
task specifics, a common failure mode in agentic systems.

## Why Use This Template

| If you... | This template helps because... |
|---|---|
| Run agentic AI for C++ development | Pre-filled domain files come with SDL3/ImGui/C++20 conventions, memory safety rules, and CRT Debug Heap verification |
| Manage multiple projects | Each project gets its own domain — no cross-project contamination |
| Want reproducible builds | Dependency pinning with commit IDs, CPM.cmake management |
| Need human-in-the-loop control | Plan approval gate, build gate, and validation script prevent drift |
| Work with agents that lose context | The domain/problem split keeps the system prompt lean and consistent |

## Quick Start

```bash
# Clone the template
git clone https://github.com/your-org/sdlc-template.git my-project
cd my-project

# The domain files are pre-filled — review them and answer the clarifying
# questions in SETUP.md to customize for your project.

# Complete the domain-setup task, then start coding.
```

## File Structure

```
.
├── README.md                       # This file — SDLC concepts and overview
├── SETUP.md                        # Setup guide, deployment methods, clarifying questions
├── LICENSE                         # MIT License
├── docs/
│   ├── domain/                     # ← ALWAYS PRESENT (load once)
│   │   ├── DOMAIN.md               # Master domain document
│   │   ├── capabilities.md         # Agent capabilities
│   │   ├── conventions.md          # Naming, style, RAII, Doxygen
│   │   ├── constraints.md          # Memory safety, build rules, security
│   │   └── terminology.md          # Glossary with C++ terms
│   ├── project/                    # ← TASK-AGNOSTIC (grows over time)
│   │   ├── research/               # Research notes, quick references
│   │   ├── design/                 # UI mocks, architecture specs
│   │   ├── reference/              # Class definitions, API docs
│   │   └── architecture/           # System diagrams, data models
│   └── tasks/                      # ← TASK-SPECIFIC (per-request)
│       ├── TASK_TEMPLATE.md        # Template for new tasks
│       ├── example-task/           # Example: TDD RenderWindow + SDL3/ImGui
│       │   ├── plan.md
│       │   ├── context.md
│       │   ├── goals.json
│       │   └── state.md
│       └── initial-build/          # INITIAL-BUILD: scaffold verification
│           ├── plan.md
│           ├── context.md
│           ├── goals.json
│           └── state.md
├── cmake/
│   └── CPM.cmake                   # CPM dependency manager
├── cpm-packages.txt               # Pinned dependency versions
├── src/
│   └── main.cpp                    # Initial scaffold
├── tests/                         # Agent-written tests
├── CMakeLists.txt                 # Root CMake config
└── build/                         # Build output (git-ignored)
```

## The SDLC Cycle

```
  1. SPEC (Domain docs)      ← Written once, referenced always
         │
         ▼
  2. PLAN (Agent proposes)   ← Human approves BEFORE code
         │
         ▼
  3. CODE (Agent implements) ← Smart pointers, RAII, Doxygen
         │
         ▼
  4. CMAKE (Agent configures)← Human reviews
         │
         ▼
  5. BUILD (HUMAN ONLY)      ← Human runs cmake/build/verify
         │
         ▼
  6. VERIFY (Human + gtest)  ← Does code match spec? Memory safe?
         │
         ▼
  7. UPDATE DOCS             ← Updated WITH code, not after
```

## Key Rules

1. **DOMAIN.md is the constitution** — agents reference it for every C++ decision.
2. **No plan approval → no code** — the human-in-the-loop gate prevents drift.
3. **Agent writes code, human builds** — never run cmake with build tools.
4. **No raw `new`/`delete`** — smart pointers and RAII are non-negotiable.
5. **SDL3 static build only** — `SDL_BUNDLE_STATIC_RUNTIME ON`, no DLLs.
6. **If you can't cite a domain rule, don't proceed.**

## Glossary

| Term | Meaning |
|---|---|
| **Domain Layer** | Always-present knowledge base: C++ conventions, SDL3/ImGui setup, constraints |
| **Project Layer** | Task-agnostic knowledge: research notes, UI mocks, class definitions, quick references |
| **Problem** | Task-specific instantiation: goals, inputs, approved plan, overrides |
| **System Prompt** | Where the domain layer lives — injected once at session start |
| **Plan Approval** | Human review step where the problem layer is validated against the domain |
| **Deep Dive** | On-demand lookup of specific domain sections when uncertain |
| **Build Gate** | Human-only: agent writes CMakeLists.txt, human runs cmake/build |

## License

MIT — see [LICENSE](LICENSE) for details.

---

**Developed and maintained in `unsloth-tmp/sdlc-template`.** The domain files
come pre-filled with working defaults; customize them via the setup process
described in [SETUP.md](SETUP.md).
