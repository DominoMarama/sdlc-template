# context.md — Domain Setup Deep-Dive

> This file contains deep-dive references for the domain-setup task. It bridges
> the template structure with your project's specific needs.

---

## Relevant Domain Sections

| Section | Why It Matters |
|---|---|
| `docs/domain/conventions.md#sdlc-workflow-conventions` | Rules for how domain files are edited and what placeholders mean |
| `docs/domain/constraints.md#sdlc-workflow-constraints` | Non-negotiable SDLC rules that apply to domain setup itself |
| `docs/domain/DOMAIN.md#sdcl-workflow-rules` | The readiness checklist and placeholder warning |

## Key Concepts for This Task

### Concept 1: Placeholder Markers Are Not Rules

**Definition:** Text like `[FILL IN]`, `<!-- TODO -->`, `your rule here`, etc.
are reminders to complete the domain, not actual constraints.

**Why it matters for this task:** If you cite a placeholder as a rule, you're
citing nothing. The agent will behave incorrectly. This is explicitly forbidden
in `constraints.md`.

**Rule from DOMAIN.md:** "Placeholder markers in domain files are not rules."

### Concept 2: Domain Readiness = Zero Placeholders

**Definition:** The domain is only ready to load into the system prompt when
all placeholder markers have been replaced with actual content.

**Why it matters for this task:** Loading an incomplete domain into the
system prompt causes the agent to either ignore missing rules or hallucinate
content. The validate_domain.py script enforces this.

**Rule from DOMAIN.md:** "The domain is only loadable when the domain-setup
task completes with zero placeholders remaining."

### Concept 3: Deep-Dive Research from Authoritative Sources

**Definition:** When researching dependencies, patterns, or tools, use official
documentation (latest stable version) as the primary source, not blogs,
tutorials, or third-party articles.

**Why it matters for this task:** The domain documents should reflect current,
authoritative knowledge. Outdated or secondary sources lead to drift.

**Rule from conventions.md:** "Deep-dive research from authoritative sources."

## Decision Log

| Decision | Rationale | Domain Rule |
|---|---|---|
| **Complete domain-setup before any code** | Domain must be complete before agent can work correctly | DOMAIN.md readiness checklist |
| **Use validate_domain.py as the gate** | Automated check prevents incomplete domains from loading | constraints.md: placeholder-free requirement |
| **Split large goals into separate tasks** | Prevents task sprawl and ensures focused completion | conventions.md: task decomposition |

---

## Reference: Authoritative Documentation Sources

When researching for this task, prioritize these sources in order:

1. **Official language documentation** (e.g., docs.python.org, rust-lang.org)
2. **Official package documentation** (e.g., npmjs.com, pkg.go.dev)
3. **Official repository READMEs and docs folders**
4. **Official release notes/changelogs** (latest stable version)
5. **Official developer blogs** (only for announcements, not tutorials)

Avoid using blogs, tutorials, or third-party articles as primary sources for
domain rules — they may be outdated or incorrect.
