# 📚 Usage Examples

Real-world examples of working with GLOBAL_RULES.

---

## Example 1: New Developer Onboarding

Developer: Alice joining the team

```bash
# 1. Clone the project
git clone https://github.com/yourteam/scm-control-tower-spoke.git
cd scm-control-tower-spoke

# 2. First-time setup (one time)
make setup

# Output:
# 📦 Installing git hooks...
#   Installing pre-push hook... ✅ Installed
#   Installing pre-commit hook... ✅ Installed
# ✅ Setup complete!

# 3. Verify setup
make check-all

# Output:
# ✅ All validation checks PASSED!
#    Safe to push: git push origin <branch>

# 4. Ready to start coding!
# Alice can now work normally - rules auto-enforce
```

---

## Example 2: Before Pushing Code (Happy Path)

Developer: Bob making changes

```bash
# 1. Edit code
vim control-tower-agent-postgres.tf
vim variables.tf

# 2. Stage changes
git add control-tower-agent-postgres.tf variables.tf

# 3. Commit
git commit -m "Add PostgreSQL configuration for control-tower-agent"

# Pre-commit hook runs:
# ✓ Checks formatting - PASS
# ✓ Ready to commit

# 4. Before pushing - validation check
make check-all

# Output:
# ╔════════════════════════════════════════════════════╗
# ║ Running Pre-Push Validation Checks...              ║
# ╚════════════════════════════════════════════════════╝
#
# 📋 Terraform project detected
#
#   1️⃣  Checking terraform format...
#       ✅ Format check passed
#
#   2️⃣  Validating terraform syntax...
#       ✅ Validation passed
#
#   3️⃣  Running tflint linter...
#       ✅ Linting passed
#
# ╔════════════════════════════════════════════════════╗
# ║        ✅ All Checks PASSED - Push OK!            ║
# ╚════════════════════════════════════════════════════╝

# 5. Push safely
git push origin feature/postgres-config

# Pre-push hook runs one final check - everything passes
# Push succeeds ✅
```

---

## Example 3: Before Pushing Code (With Issues)

Developer: Carol with formatting problems

```bash
# 1. Edit code
vim control-tower-agent-cos.tf

# 2. Stage (without formatting)
git add control-tower-agent-cos.tf

# 3. Commit
git commit -m "Add COS bucket configuration"

# Pre-commit hook runs:
# ❌ Terraform formatting issues found
# Auto-fixing with: terraform fmt -recursive
# ✅ Formatting fixed!
# 📝 Please re-stage and commit

# 4. Re-stage
git add -A

# 5. Commit again
git commit -m "Add COS bucket configuration"

# Pre-commit hook runs:
# ✓ Format check - PASS
# ✓ Commit succeeds

# 6. Validation before push
make check-all

# Everything passes - safe to push
git push origin feature/cos-bucket
```

---

## Example 4: Fixing Validation Failures

Developer: Dave with validation errors

```bash
# 1. Made changes
vim main.tf

# 2. Staged and committed
git add main.tf
git commit -m "Update main configuration"

# 3. Before push - validation
make check-all

# Output:
# ❌ Validation failed!
# 
# terraform validate output:
# Error: Unsupported argument
#   on main.tf line 5:
#   5: invalid_argument = "value"
#
# This argument is not expected here.

# 4. Fix the issue
vim main.tf
# Remove the invalid_argument

# 5. Re-validate
make check-all

# ✅ All Checks PASSED

# 6. Push
git push origin feature/update-config
# Push succeeds ✅
```

---

## Example 5: Team-Wide Update

Scenario: New rule added to GLOBAL_RULES

```bash
# 1. Update in pre-commit-rules repo
cd ~/projects/pre-commit-rules
vim GLOBAL_RULES.md
# Add new rule #16
git push origin main

# 2. All projects can now get the update
cd ~/projects/scm-control-tower-spoke
make setup
# Downloads latest rules

# 3. New rule is now enforced
make check-all
# Uses new validation
```

---

## Example 6: Pull Request Workflow

Developer: Eve creating a PR

```bash
# 1. Create feature branch
git checkout -b feature/ATL-134-control-tower-agent

# 2. Make changes (multiple commits)
git add infrastructure.tf && git commit -m "Add infrastructure"
git add secrets.tf && git commit -m "Add secrets management"
git add ingress.tf && git commit -m "Add ingress configuration"

# Pre-commit hook runs on EVERY commit:
# ✓ Format check - all pass
# ✓ All commits succeed

# 3. Before final push - comprehensive check
make check-all

# Output: ✅ All Checks PASSED

# 4. Push to branch
git push origin feature/ATL-134-control-tower-agent

# Pre-push hook runs final validation:
# ✓ All checks pass
# ✓ Push succeeds

# 5. Create MR
# Pipeline CI/CD runs:
# ✓ terraform fmt
# ✓ terraform validate
# ✓ tflint
# ✓ gitleaks
# ✓ trivy
# All pass! ✅
```

---

## Example 7: Debugging Failed Checks

Developer: Frank wondering why push failed

```bash
# 1. Tries to push
git push origin feature/my-branch

# Pre-push hook output:
# ❌ Linting issues found!
# 
# tflint output:
# Warning: Module source "..." uses default branch (main)
# 
# 💡 Fix with tflint-ignore comment

# 2. Frank adds the fix
vim control-tower-agent-cos.tf

# Add before line 4:
# # tflint-ignore: terraform_module_pinned_source
#   source = "git@gitlab.com:..."

# 3. Re-check
make lint

# ✅ Linting passed

# 4. Push again
git push
# ✅ Succeeds
```

---

## Example 8: Different Project Type

Scenario: Using rules in a Python project

```bash
# 1. Clone Python project
git clone https://github.com/yourteam/python-service.git
cd python-service

# 2. Setup (but this is Python, not Terraform)
make setup

# Git hooks installed, but they look for .tf files
# For Python projects, you'd customize:
# - hooks check for *.py files
# - Use pylint, black, pytest instead

# 3. But the workflow is same
make check-all
git commit
git push
```

---

## Example 9: Emergency - Need to Bypass

Scenario: Production hotfix that must go through

```bash
# ⚠️ NOT RECOMMENDED - only for true emergencies

git push --no-verify

# This skips the pre-push hook
# Code goes directly to CI/CD validation
# Pipeline still catches issues

# But now:
# 1. Disable it again for future pushes
git config --local core.hooksPath .git/hooks

# 2. Fix the code later
# 3. Commit properly
```

---

## Example 10: Mentoring a Teammate

Scenario: Experienced dev helping new dev

```bash
# New dev: "My push is blocked - what do I do?"

# Experienced dev:
# "Run make check-all and fix any issues"
# 
# New dev runs:
make check-all

# Sees formatting issue
# Experienced dev says:
# "Run make fmt to fix it"

make fmt
make check-all

# Now passes
git push

# Success! ✅
```

---

## Takeaway

The workflow is consistent:

1. **Code** - Make changes
2. **Commit** - Pre-commit hook checks
3. **Validate** - `make check-all` before push
4. **Push** - Pre-push hook runs final check
5. **Pipeline** - CI/CD validates on the server

**All automatic. Zero manual steps.**

---

**Last Updated:** 2026-10-07
