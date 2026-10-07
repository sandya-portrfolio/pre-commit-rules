# 🔧 Troubleshooting Guide

Common issues and solutions.

---

## ❌ "Pre-push hook not running"

**Problem:** Hooks installed but not executing

**Solution:**
```bash
# Reinstall hooks
make setup

# Verify installation
ls -la .git/hooks/pre-push
ls -la .git/hooks/pre-commit

# Should show: -rwxr-xr-x (executable)
```

---

## ❌ "terraform fmt -check failed"

**Problem:** Code formatting doesn't match standards

**Solution:**
```bash
# Auto-fix formatting
terraform fmt -recursive

# Verify
make fmt-check

# Add and commit
git add -A
git commit -m "Fix terraform formatting"
git push
```

---

## ❌ "tflint not found"

**Problem:** TFLint not installed or not in PATH

**Solution:**

**macOS:**
```bash
brew install tflint
tflint --version  # Verify
```

**Ubuntu:**
```bash
sudo apt-get install tflint
tflint --version
```

**Windows:**
```powershell
choco install tflint
tflint --version
```

---

## ❌ "terraform validate failed"

**Problem:** Syntax errors in Terraform code

**Solution:**
```bash
# See detailed error
terraform validate

# Fix issues in your .tf files
# Then re-validate
terraform validate

# Once passes - try again
make check-all
```

---

## ❌ "git commit fails with formatting error"

**Problem:** Pre-commit hook detected formatting issues

**Solution:**
```bash
# Pre-commit hook output:
# ❌ Terraform formatting issues found
# Auto-fixing with: terraform fmt -recursive
# ✅ Formatting fixed!
# 📝 Please re-stage and commit

# Restage files
git add -A

# Commit again
git commit -m "Your message"
```

---

## ❌ "Pre-push blocks push"

**Problem:** Pre-push hook validation failed

**Solution:**
```bash
# Run checks locally
make check-all

# See which check failed and fix it
# Then try push again

# If still stuck:
terraform validate  # Check syntax
terraform fmt -recursive  # Fix formatting
tflint  # Check linting

# Re-run full check
make check-all

# Push when all pass
git push
```

---

## ✅ "Want to skip hooks?" (NOT RECOMMENDED)

**Emergency bypass:**
```bash
# Force push, bypassing ALL checks
git push --no-verify

# ⚠️ WARNING: This skips all validation
# Only use if absolutely necessary!
```

**Better: Fix the issue**
```bash
# See what failed
make check-all

# Fix it
terraform fmt -recursive

# Re-check
make check-all

# Now safe to push
git push
```

---

## ✅ "make command not found"

**Problem:** Make is not installed

**Solution:**

**macOS:**
```bash
brew install make
```

**Ubuntu:**
```bash
sudo apt-get install build-essential
```

**CentOS:**
```bash
sudo yum install make
```

---

## ✅ "Which files are actually checked?"

**Checked files:**
- All `.tf` files (Terraform)
- Formatted with `terraform fmt`
- Validated with `terraform validate`
- Linted with `tflint`

**Not checked:**
- `.tfvars` (Terraform variables)
- Other file types

---

## ✅ "Can I disable specific checks?"

**Yes, in your code:**

```hcl
# Disable specific tflint rule
# tflint-ignore: terraform_module_pinned_source
source = "git@gitlab.com:example/module.git?ref=main"

# But use sparingly!
```

---

## ✅ "Hooks work offline?"

**Yes!** All checks run locally:
- ✓ No internet needed
- ✓ No external services
- ✓ Completely local validation

---

## ✅ "How to get latest rules?"

**Auto-reference:**
```bash
# Rules auto-update from:
# https://github.com/sandya-portrfolio/pre-commit-rules

# To get latest in your project
make setup  # Reinstall
```

---

## ✅ "Setup failed - what's wrong?"

**Check prerequisites:**
```bash
# Terraform installed?
terraform --version

# TFLint installed?
tflint --version

# Git installed?
git --version

# In a git repo?
ls -la .git
```

**If any missing:**
```bash
# Install what's missing
brew install terraform tflint git

# Then retry setup
make setup
```

---

## ✅ "Multiple developers having same issue?"

**Likely cause:** Setup not run or hooks corrupted

**Solution for all:**
```bash
# Everyone runs:
make setup

# Verify:
make check-all
```

---

## Still Stuck?

1. **Read GLOBAL_RULES.md** - Understand the rules
2. **Read README.md** - Complete guide
3. **Check FAQ.md** - Common questions
4. **Run:** `make help` - See all commands

**Still need help?** Contact your team lead.

---

**Last Updated:** 2026-10-07
