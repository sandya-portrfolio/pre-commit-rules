#!/usr/bin/env python3
"""
Pre-commit checks runner with interactive selection.

Usage:
    python pre_commit_checks.py              # Interactive mode (choose checks)
    python pre_commit_checks.py --all        # Run all applicable checks
    python pre_commit_checks.py --help       # Show help
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
from typing import List, Tuple, Dict


class ProjectDetector:
    """Detect project type based on files present."""

    @staticmethod
    def detect() -> List[str]:
        """Return list of detected project types."""
        project_types = []

        if Path("*.tf").glob("*.tf") or Path("provider.tf").exists():
            project_types.append("terraform")

        if Path("package.json").exists():
            project_types.append("node")

        if Path("requirements.txt").exists() or Path("setup.py").exists():
            project_types.append("python")

        if Path("go.mod").exists():
            project_types.append("go")

        return project_types


class CheckRunner:
    """Run various validation checks."""

    def __init__(self):
        self.passed = []
        self.failed = []
        self.skipped = []

    def run_command(self, cmd: str, description: str) -> bool:
        """Run a command and return True if successful."""
        print(f"\n  🔍 {description}...", end=" ", flush=True)
        try:
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=60
            )
            if result.returncode == 0:
                print("✅ PASSED")
                self.passed.append(description)
                return True
            else:
                print("❌ FAILED")
                if result.stderr:
                    print(f"     Error: {result.stderr[:100]}")
                self.failed.append(description)
                return False
        except subprocess.TimeoutExpired:
            print("⏱️  TIMEOUT")
            self.failed.append(f"{description} (timeout)")
            return False
        except Exception as e:
            print(f"❌ ERROR: {str(e)[:50]}")
            self.failed.append(f"{description} (error)")
            return False

    def terraform_checks(self) -> None:
        """Run Terraform checks."""
        print("\n📦 Terraform Checks:")
        self.run_command(
            "terraform fmt -check -recursive",
            "Terraform format check"
        )
        self.run_command(
            "terraform validate",
            "Terraform validate"
        )
        self.run_command(
            "tflint",
            "tflint linter"
        )

    def node_checks(self) -> None:
        """Run Node/React checks."""
        print("\n📦 Node/React Checks:")
        self.run_command(
            "npm run format --if-present",
            "Format check (prettier)"
        )
        self.run_command(
            "npm run lint --if-present",
            "Lint check (eslint)"
        )
        self.run_command(
            "npm test --if-present",
            "Test suite"
        )

    def python_checks(self) -> None:
        """Run Python checks."""
        print("\n📦 Python Checks:")
        self.run_command(
            "black --check .",
            "Format check (black)"
        )
        self.run_command(
            "isort --check-only .",
            "Import sort check (isort)"
        )
        self.run_command(
            "pylint --rcfile=.pylintrc **/*.py",
            "Lint check (pylint)"
        )
        self.run_command(
            "pytest",
            "Test suite (pytest)"
        )

    def go_checks(self) -> None:
        """Run Go checks."""
        print("\n📦 Go Checks:")
        self.run_command(
            "gofmt -l .",
            "Format check (gofmt)"
        )
        self.run_command(
            "go vet ./...",
            "Vet check (go vet)"
        )
        self.run_command(
            "golangci-lint run",
            "Lint check (golangci-lint)"
        )
        self.run_command(
            "go test -v ./...",
            "Test suite (go test)"
        )

    def git_checks(self) -> None:
        """Run git-related checks."""
        print("\n📦 Git Checks:")
        self.run_command(
            "git diff --exit-code",
            "Uncommitted changes check"
        )

    def report(self) -> bool:
        """Print summary and return True if all checks passed."""
        print("\n" + "=" * 60)
        print("📊 CHECK SUMMARY")
        print("=" * 60)

        if self.passed:
            print(f"\n✅ PASSED ({len(self.passed)}):")
            for check in self.passed:
                print(f"   ✓ {check}")

        if self.skipped:
            print(f"\n⏭️  SKIPPED ({len(self.skipped)}):")
            for check in self.skipped:
                print(f"   - {check}")

        if self.failed:
            print(f"\n❌ FAILED ({len(self.failed)}):")
            for check in self.failed:
                print(f"   ✗ {check}")

        print("\n" + "=" * 60)

        if self.failed:
            print("❌ SOME CHECKS FAILED - Fix errors and retry\n")
            return False
        else:
            print("✅ ALL CHECKS PASSED - Ready to push!\n")
            return True

    def skip(self, description: str) -> None:
        """Mark a check as skipped."""
        self.skipped.append(description)


def show_menu(options: Dict[str, str]) -> List[str]:
    """Show interactive menu and return selected options."""
    print("\n" + "=" * 60)
    print("🔍 PRE-COMMIT CHECKS - SELECT WHICH TO RUN")
    print("=" * 60 + "\n")

    selected = []
    for i, (key, description) in enumerate(options.items(), 1):
        print(f"{i}. {description}")

    print(f"\n{len(options) + 1}. Run ALL checks")
    print(f"{len(options) + 2}. Cancel\n")

    try:
        choice = input("Select checks (comma-separated, e.g., '1,2,3'): ").strip()

        if choice == str(len(options) + 2):
            print("\n❌ Cancelled\n")
            sys.exit(1)

        if choice == str(len(options) + 1):
            return list(options.keys())

        indices = [int(x.strip()) - 1 for x in choice.split(",")]
        keys = list(options.keys())
        selected = [keys[i] for i in indices if 0 <= i < len(keys)]

        if selected:
            print(f"\n✅ Selected: {', '.join(selected)}\n")
            return selected
        else:
            print("\n❌ Invalid selection\n")
            return show_menu(options)

    except (ValueError, IndexError):
        print("\n❌ Invalid input. Please enter numbers separated by commas.\n")
        return show_menu(options)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Run pre-commit checks with optional selection"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all applicable checks without prompting"
    )
    parser.add_argument(
        "--terraform",
        action="store_true",
        help="Run only Terraform checks"
    )
    parser.add_argument(
        "--node",
        action="store_true",
        help="Run only Node/React checks"
    )
    parser.add_argument(
        "--python",
        action="store_true",
        help="Run only Python checks"
    )
    parser.add_argument(
        "--go",
        action="store_true",
        help="Run only Go checks"
    )
    parser.add_argument(
        "--git",
        action="store_true",
        help="Run only Git checks"
    )

    args = parser.parse_args()

    # Detect project types
    detected = ProjectDetector.detect()
    runner = CheckRunner()

    # Determine which checks to run
    if args.terraform or args.node or args.python or args.go or args.git:
        # Specific checks requested
        if args.terraform:
            runner.terraform_checks()
        if args.node:
            runner.node_checks()
        if args.python:
            runner.python_checks()
        if args.go:
            runner.go_checks()
        if args.git:
            runner.git_checks()

    elif args.all:
        # Run all detected project types
        print(f"\n🔍 Detected project types: {', '.join(detected)}\n")
        if "terraform" in detected:
            runner.terraform_checks()
        if "node" in detected:
            runner.node_checks()
        if "python" in detected:
            runner.python_checks()
        if "go" in detected:
            runner.go_checks()
        runner.git_checks()

    else:
        # Interactive mode
        options = {}
        if "terraform" in detected:
            options["terraform"] = "🏗️  Terraform (fmt, validate, tflint)"
        if "node" in detected:
            options["node"] = "📦 Node/React (format, lint, test)"
        if "python" in detected:
            options["python"] = "🐍 Python (black, isort, pylint, pytest)"
        if "go" in detected:
            options["go"] = "🐹 Go (fmt, vet, lint, test)"

        options["git"] = "📝 Git (uncommitted changes)"

        if not options:
            print("\n⚠️  No supported project types detected\n")
            sys.exit(1)

        selected = show_menu(options)

        # Run selected checks
        for check_type in selected:
            if check_type == "terraform":
                runner.terraform_checks()
            elif check_type == "node":
                runner.node_checks()
            elif check_type == "python":
                runner.python_checks()
            elif check_type == "go":
                runner.go_checks()
            elif check_type == "git":
                runner.git_checks()

    # Print report and exit
    success = runner.report()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
