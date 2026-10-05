#!/usr/bin/env python3
"""SDLC Domain Validator.

Validate that a project's domain documentation is properly set up and
current. This script checks the domain layer, problem layer, and detects
common violations before code is written.

Usage:
    python scripts/validate_domain.py [project_root]

Exit codes:
    0 — All checks passed
    1 — Errors found (review output)
    2 — Usage error
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Tuple, Dict, Any

# =============================================================================
# Configuration
# =============================================================================

DOMAIN_DIR = "docs/domain"
TASKS_DIR = "docs/tasks"

REQUIRED_DOMAIN_FILES = [
    "DOMAIN.md",
    "capabilities.md",
    "conventions.md",
    "constraints.md",
    "terminology.md",
]

REQUIRED_TASK_FILES = [
    "plan.md",
    "context.md",
    "goals.json",
    "state.md",
]

# =============================================================================
# Validators
# =============================================================================


def _path_ok(path: Path, msg: str) -> bool:
    """Print error and return False."""
    print(f"  ✗ {msg}", file=sys.stderr)
    return False


def _info(path: Path, msg: str):
    """Print info message."""
    print(f"  ✓ {msg}")


def check_domain_layer(project_root: Path) -> Tuple[int, List[str]]:
    """Validate the domain layer exists and is complete."""
    domain_dir = project_root / DOMAIN_DIR
    errors: List[str] = []

    if not domain_dir.exists():
        errors.append(f"Domain directory missing: {domain_dir}")
        return 2, errors

    _info(domain_dir, "Domain directory exists")

    # Check required files
    missing = []
    for fname in REQUIRED_DOMAIN_FILES:
        fpath = domain_dir / fname
        if not fpath.exists():
            missing.append(fname)
        else:
            # Check file is not empty
            if fpath.stat().st_size == 0:
                missing.append(fname + " (empty)")
            elif fpath.suffix == '.tpl':
                errors.append(
                    f"{fname} is still a .tpl placeholder — replace with actual content"
                )
            else:
                _info(fpath, f"present ({fpath.stat().st_size} bytes)")

    if missing:
        errors.append(f"Missing domain files: {', '.join(missing)}")

    # Check for leftover .tpl files
    tpl_files = [f for f in domain_dir.iterdir() if f.suffix == '.tpl']
    if tpl_files:
        names = [f.name for f in tpl_files]
        errors.append(f"Leftover .tpl placeholders: {', '.join(names)}")

    # Check DOMAIN.md has proper structure
    domain_md = domain_dir / "DOMAIN.md"
    if domain_md.exists():
        content = domain_md.read_text(encoding='utf-8')
        import re

        checks = [
            ("# DOMAIN.md", "^# DOMAIN.md"),
            ("## 1. Capabilities", r"^##\s*1\.\s*Capabilities"),
            ("## 2. Conventions", r"^##\s*2\.\s*Conventions"),
            ("## 3. Constraints", r"^##\s*3\.\s*Constraints"),
            ("## 4. Terminology", r"^##\s*4\.\s*Terminology"),
            ("## 5. How to Use", r"^##\s*5\.\s*How"),
        ]
        for name, regex_pattern in checks:
            if not re.search(regex_pattern, content, re.MULTILINE | re.DOTALL):
                errors.append(f"DOMAIN.md missing {name}")

    return 1 if errors else 0, errors


def check_problem_layer(project_root: Path) -> Tuple[int, List[str]]:
    """Validate problem layer structure for all tasks."""
    tasks_dir = project_root / TASKS_DIR
    errors: List[str] = []
    warnings: List[str] = []

    if not tasks_dir.exists():
        errors.append(f"Tasks directory missing: {tasks_dir}")
        return 2, errors

    _info(tasks_dir, "Tasks directory exists")

    task_ids = [d.name for d in tasks_dir.iterdir() if d.is_dir()]
    if not task_ids:
        warnings.append("No task folders found — expected at least one")

    for task_id in task_ids:
        task_dir = tasks_dir / task_id
        _info(task_dir, f"task folder exists")

        # Check required files
        missing = []
        for fname in REQUIRED_TASK_FILES:
            fpath = task_dir / fname
            if not fpath.exists():
                missing.append(fname)
            else:
                if fname == "goals.json":
                    # Validate JSON structure
                    try:
                        data = json.loads(fpath.read_text(encoding='utf-8'))
                        if "task_id" not in data:
                            errors.append(
                                f"{task_dir}/goals.json missing 'task_id' field"
                            )
                        if "goals" not in data or not isinstance(data["goals"], list):
                            errors.append(
                                f"{task_dir}/goals.json missing 'goals' array"
                            )
                        # Check each goal has required fields
                        for goal in data.get("goals", []):
                            if not isinstance(goal, dict):
                                errors.append(
                                    f"{task_dir}/goals.json: goal is not an object"
                                )
                                break
                            required_goal_fields = ["id", "title", "steps"]
                            for field in required_goal_fields:
                                if field not in goal:
                                    errors.append(
                                        f"{task_dir}/goals.json: goal missing '{field}'"
                                    )
                    except json.JSONDecodeError as e:
                        errors.append(f"{task_dir}/goals.json is not valid JSON: {e}")
                elif fname.endswith('.md'):
                    # Check markdown files are not empty
                    if fpath.stat().st_size == 0:
                        missing.append(fname + " (empty)")
                    _info(fpath, f"present")

        if missing:
            errors.append(f"{task_dir}/ missing: {', '.join(missing)}")

        # Check for .tpl placeholders
        tpl_files = [f for f in task_dir.iterdir() if f.suffix == '.tpl']
        if tpl_files:
            names = [f.name for f in tpl_files]
            errors.append(f"{task_dir}/ has leftover .tpl: {', '.join(names)}")

        # Domain bug prevention check
        plan_md = task_dir / "plan.md"
        state_md = task_dir / "state.md"
        context_md = task_dir / "context.md"
        if plan_md.exists() and not state_md.exists():
            errors.append(
                f"{task_dir}/: plan.md exists but state.md missing — "
                "coding without approved plan + state is a domain violation"
            )

    return 1 if errors else 0, errors


def check_consistency(project_root: Path) -> Tuple[int, List[str]]:
    """Check consistency between domain and problem layers."""
    domain_dir = project_root / DOMAIN_DIR
    tasks_dir = project_root / TASKS_DIR
    errors: List[str] = []

    # Check that DOMAIN.md references exist for all domain files
    domain_md = domain_dir / "DOMAIN.md"
    if domain_md.exists():
        content = domain_md.read_text(encoding='utf-8')
        for fname in REQUIRED_DOMAIN_FILES:
            if fname != "DOMAIN.md":
                fpath = domain_dir / fname
                if not fpath.exists():
                    errors.append(f"DOMAIN.md references {fname} but it doesn't exist")
                elif f"{fname}" not in content and f"`{fname}`" not in content:
                    errors.append(
                        f"DOMAIN.md has no reference to {fname} — should cite it"
                    )

    # Check that task plans reference domain rules
    for task_dir in tasks_dir.iterdir():
        if not task_dir.is_dir():
            continue
        plan_md = task_dir / "plan.md"
        if not plan_md.exists():
            continue

        content = plan_md.read_text(encoding='utf-8')
        # Check for domain rule citations
        if "DOMAIN.md" not in content and "domain" not in content.lower():
            errors.append(
                f"{task_dir}/plan.md does not reference DOMAIN.md — "
                "plans should cite domain rules"
            )

    return 1 if errors else 0, errors


def check_template_placeholders(project_root: Path) -> Tuple[int, List[str]]:    # Check that domain-setup task exists for new projects
    domain_setup_dir = project_root / TASKS_DIR / "domain-setup"
    if not domain_setup_dir.exists():
        errors.append(
            "domain-setup task missing — this is the first task for new "
            "projects; create it before loading the domain"
        )


    """Check for remaining .tpl placeholder files."""
    errors: List[str] = []

    # Walk entire project (excluding node_modules, .git, build dirs)
    excluded = {'node_modules', '.git', 'build', '_deps', 'venv', 'env'}

    for path in project_root.rglob("*"):
        if path.is_dir() and path.name in excluded:
            continue
        if path.suffix == '.tpl':
            rel = path.relative_to(project_root)
            errors.append(f"{rel} is a .tpl placeholder — replace with actual content")

    return 1 if errors else 0, errors

# =============================================================================
# Main
# =============================================================================


def main():
    if len(sys.argv) > 1:
        project_root = Path(sys.argv[1])
    else:
        # Default to current directory or parent sandbox
        possible = [Path("."), Path(os.path.expandvars('$SANDBOX'))]
        found = next((p for p in possible if p.exists()), None)
        if found is None:
            print("Usage: python validate_domain.py [project_root]", file=sys.stderr)
            sys.exit(2)
        project_root = found

    if not project_root.exists():
        print(f"Error: {project_root} does not exist", file=sys.stderr)
        sys.exit(2)

    print(f"Validating domain structure at: {project_root.resolve()}")
    print("=" * 60)

    all_errors: List[str] = []
    overall = 0

    # Run all checks
    name, errors = check_domain_layer(project_root)
    overall = max(overall, name)
    all_errors.extend(errors)

    name, errors = check_problem_layer(project_root)
    overall = max(overall, name)
    all_errors.extend(errors)

    name, errors = check_consistency(project_root)
    overall = max(overall, name)
    all_errors.extend(errors)

    name, errors = check_template_placeholders(project_root)
    overall = max(overall, name)
    all_errors.extend(errors)

    # Summary
    print("=" * 60)
    if overall == 0:
        print("✅ All domain checks passed!")
        print()
        print("Your domain documentation is properly set up. You can now proceed")
        print("with tasks, following the Domain/Task split.")
        sys.exit(0)
    else:
        print(f"❌ {len(all_errors)} error(s) found:")
        for err in all_errors:
            print(err)
        print()
        print("Fix these errors before proceeding. The agent must not write code")
        print("until the domain is properly set up.")
        sys.exit(1)


if __name__ == "__main__":
    main()
