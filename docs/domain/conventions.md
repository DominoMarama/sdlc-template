# conventions.md — Language-Specific Conventions

> These are default conventions that apply to all projects using this
> template. Fill in project-specific conventions below.

---

## SDLC Workflow Conventions

| Aspect | Rule |
|---|---|
| **Domain files are never edited in-place** | Agents create task-specific docs; they do not modify DOMAIN.md or other domain files without human review |
| **Placeholder markers are not rules** | `[FILL IN]`, `<!-- TODO -->`, etc. are reminders, not constraints. Never cite them |
| **Domain-setup task comes first** | For new projects, complete the domain-setup task before any code tasks |
| **Deep-dive research from authoritative sources** | When researching dependencies or patterns, use official documentation (latest stable version) as the primary source |
| **GUI mockups before implementation** | For UI requirements, create wireframes/mockups in the plan phase before writing code |
| **Task splitting recognized during planning** | If a goal is large, complex, or spans multiple domains, propose it as a separate task with its own domain setup |

## Naming Conventions

| Element | Rule | Example |
|---|---|---|
| **File naming** | lowercase-with-dashes for directories; snake_case for files | `user_service.py`, `auth_controller/` |
| **Function naming** | snake_case, imperative mood | `calculate_total()`, `validate_input()` |
| **Class naming** | PascalCase | `UserService`, `AuthController` |
| **Variable naming** | snake_case for locals; camelCase for parameters | `total_amount`, `user_id` |
| **Constant naming** | UPPER_SNAKE_CASE | `MAX_RETRIES`, `API_VERSION` |
| **Error names** | `Err<Name>` or `<Name>Error` | `ErrNotFound`, `ValidationError` |

## Code Style

| Aspect | Rule |
|---|---|
| **Indentation** | e.g., 2 spaces, no tabs |
| **Line length** | e.g., max 100 characters |
| **Trailing commas** | e.g., always in multi-line structures |
| **Import organization** | e.g., standard library → third-party → local |
| **Comment style** | e.g., inline `#`, docstrings for functions |
| **Blank lines** | e.g., one blank line between logical blocks |

## Error Handling

| Pattern | Rule |
|---|---|
| **Error types** | e.g., define specific exception classes |
| **Error messages** | e.g., include context, never bare `Exception` |
| **Retry logic** | e.g., max 3 retries with exponential backoff |
| **Logging** | e.g., use structured logging with levels |

## Testing Conventions

| Aspect | Rule |
|---|---|
| **Test file naming** | e.g., `test_<module>.py` |
| **Test function naming** | e.g., `test_<action>_<condition>()` |
| **Test organization** | e.g., setup/teardown in fixtures |
| **Coverage target** | e.g., 80% minimum |

## File Organization

| Directory | Purpose |
|---|---|
| `src/` | Source code |
| `tests/` | Test suite |
| `config/` | Configuration files |
| `docs/` | Documentation (domain + tasks) |
| `scripts/` | Build/maintenance scripts |

---

**Replace this entire file with your project's actual conventions.** The
agent will use this as its style guide for all code generation.
