# 🤖 Claude Method - Bash/Makefile Approach

> **Git hooks + Makefile automation for pre-commit checks**

The Claude method uses bash scripts and Makefile to automatically enforce development standards using git hooks that run before every commit and push.

---

## 📋 Table of Contents

1. [How It Works](#how-it-works)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Daily Workflow](#daily-workflow)
6. [Commands Reference](#commands-reference)
7. [Troubleshooting](#troubleshooting)

---

## 🔄 How It Works

### The Flow

```
Your Code Changes
      ↓
git add file.tf
      ↓
git commit -m "message"
      ↓
PRE-COMMIT HOOK AUTO-RUNS ⚡
  ✓ terraform fmt (auto-fix)
  ✓ Commit completes
      ↓
You work more...
      ↓
git push origin feature/branch
      ↓
PRE-PUSH HOOK AUTO-RUNS ⚡
  ✓ terraform fmt -check
  ✓ terraform validate
  ✓ tflint
  ✓ All checks pass → Push succeeds
  ✗ Any fail → Push blocked (fix and retry)
      ↓
GitHub Actions/Pipeline Runs
  ✓ Additional checks in CI/CD
```

### Key Features

✅ **Automatic Enforcement** - Checks run without you doing anything  
✅ **Fail Fast** - Catch errors locally before expensive CI/CD  
✅ **Auto-Fix** - Formatting issues fixed automatically  
✅ **Block Bad Pushes** - Won't let you push broken code  
✅ **Team Consistency** - Everyone follows same rules  

---

## 📦 Prerequisites (One Time Setup)

### Choose Your OS

**macOS:**
```bash
brew install terraform tflint make git
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y terraform tflint make git
```

**CentOS/RHEL:**
```bash
sudo yum install -y terraform tflint make git
```

**Windows (with Chocolatey):**
```powershell
choco install terraform tflint make git
```

### Verify Installation

```bash
terraform --version
tflint --version
make --version
git --version
```

---

## 🚀 Installation (2 Minutes)

### Step 1: Clone Your Project

```bash
git clone https://github.com/yourteam/your-project.git
cd your-project
```

### Step 2: Copy Files from Pre-Commit-Rules

Choose **Option A** (recommended) or **Option B**:

**Option A: Auto-Download**
```bash
# Download files directly
curl -o Makefile https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/Claude/Makefile
curl -o setup-git-hooks.sh https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/Claude/setup-git-hooks.sh
curl -o GLOBAL_RULES.md https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/GLOBAL_RULES.md
```

**Option B: Manual Copy**
1. Download from: https://github.com/sandya-portrfolio/pre-commit-rules/tree/main/Claude
2. Copy to your project root:
   - `Makefile`
   - `setup-git-hooks.sh`
   - `GLOBAL_RULES.md`

### Step 3: Make Script Executable

```bash
chmod +x setup-git-hooks.sh
```

### Step 4: Run Setup

```bash
make setup
```

**Expected Output:**
```
╔════════════════════════════════════════════════════╗
║         GLOBAL_RULES - Automated Setup            ║
╚════════════════════════════════════════════════════╝

📦 Installing git hooks...
  Installing pre-push hook... ✅ Installed
  Installing pre-commit hook... ✅ Installed

╔════════════════════════════════════════════════════╗
║              ✅ Setup Complete!                   ║
╚════════════════════════════════════════════════════╝
```

### Step 5: Verify Setup

```bash
make check-all
```

**Expected Output:**
```
✅ All validation checks PASSED!
   Safe to push: git push origin <branch>
```

---

## ⚡ Quick Start (First Task)

### 1. Start Your Work

```bash
# Pull latest
git pull origin main

# Create feature branch
git checkout -b feature/my-feature
```

### 2. Make Changes

```bash
# Edit your code
vim main.tf
vim variables.tf
vim provider.tf

# Stage changes
git add main.tf variables.tf provider.tf
```

### 3. Commit (Pre-Commit Hook Runs)

```bash
git commit -m "Add new infrastructure resources"

# OUTPUT:
# ✓ Pre-commit hook auto-runs
# ✓ terraform fmt auto-fixes if needed
# ✓ Commit completes successfully
```

### 4. Verify Before Push

```bash
# Run ALL checks
make check-all

# OUTPUT:
# ╔════════════════════════════════════════════════════╗
# ║     Running Pre-Push Validation Checks...         ║
# ╚════════════════════════════════════════════════════╝
#
# 📋 Terraform project detected
#   1️⃣  Checking terraform format...
#       ✅ Format check passed
#   2️⃣  Validating terraform syntax...
#       ✅ Validation passed
#   3️⃣  Running tflint linter...
#       ✅ Linting passed
#
# ╔════════════════════════════════════════════════════╗
# ║        ✅ All Checks PASSED - Push OK!            ║
# ╚════════════════════════════════════════════════════╝
```

### 5. Push to GitHub

```bash
git push origin feature/my-feature

# Pre-push hook runs one final check
# If pass → Push succeeds
# If fail → Push blocked (fix and retry)
```

### 6. Create Pull Request

```bash
# Go to GitHub and create MR/PR
# GitHub Actions will run additional checks
```

---

## 📅 Daily Workflow

### Before Each Commit

```bash
# Check what you changed
git status

# Stage files
git add file1.tf file2.tf

# Commit (hook auto-runs)
git commit -m "Clear message about changes"

# If hook fails:
# - Read error message
# - Fix the issue
# - Try commit again
```

### Before Each Push

```bash
# IMPORTANT: Run all checks
make check-all

# If any fail:
make fmt              # Auto-fix formatting
make validate         # Check syntax
make lint             # Run linter

# Re-check
make check-all

# Once all pass
git push origin <branch-name>
```

### If Checks Fail

```bash
# See what failed
make check-all

# Auto-fix formatting (most common issue)
terraform fmt -recursive

# If still failing, read error and fix code

# Re-check
make check-all

# Push when ready
git push origin <branch>
```

---

## 📋 Commands Reference

### Setup & Installation

```bash
# One-time setup (installs git hooks)
make setup

# Help - show all commands
make help
```

### Validation Commands (BEFORE PUSH)

```bash
# RUN THIS BEFORE EVERY PUSH ⭐
make check-all
# Runs: fmt-check, validate, lint (in order)
# Exit code 0 = safe to push
# Exit code 1 = fix errors first
```

### Individual Checks

```bash
# Check formatting (no changes)
make fmt-check
# Shows if files are not formatted
# Exit code 0 = formatted correctly
# Exit code 1 = needs formatting

# Auto-fix formatting (CHANGES FILES)
make fmt
# Automatically reformats all .tf files
# Use before git commit

# Validate syntax
make validate
# Checks Terraform configuration syntax
# Exit code 0 = valid
# Exit code 1 = syntax errors

# Run linter
make lint
# Runs tflint for best practices
# Exit code 0 = no issues
# Exit code 1 = linting issues found
```

### Maintenance

```bash
# Clean Terraform cache
make clean
# Removes: .terraform/, .terraform.lock.hcl, state files
# Use if having terraform init issues

# Show all available commands
make help
```

---

## 🔍 What Gets Checked

### Pre-Commit Hook
```bash
terraform fmt -recursive  # Auto-format code
```

### Pre-Push Hook
```bash
terraform fmt -check -recursive   # Check formatting
terraform validate                # Check syntax
tflint                           # Check best practices
```

### GitHub Actions (Pipeline)
```bash
Additional checks via CI/CD workflows
```

---

## 🐛 Troubleshooting

### ❌ "make: command not found"

**macOS:**
```bash
brew install make
```

**Linux:**
```bash
sudo apt-get install make
```

### ❌ "terraform fmt -check failed"

**Problem:** Files are not formatted correctly

**Solution:**
```bash
terraform fmt -recursive
make check-all
```

### ❌ "tflint not found"

**Problem:** tflint not installed

**Solution:**
```bash
brew install tflint        # macOS
sudo apt-get install tflint  # Linux
```

### ❌ "Pre-push hook not running"

**Problem:** Hook not installed properly

**Solution:**
```bash
make setup  # Reinstall hooks
```

### ❌ "terraform validate failed"

**Problem:** Syntax errors in code

**Solution:**
```bash
# Read error message
make validate

# Fix the error in your code
vim main.tf

# Re-check
make validate
```

### ❌ "terraform fmt -check failed after making changes"

**Problem:** New code needs formatting

**Solution:**
```bash
terraform fmt -recursive
make check-all
```

### ❌ "Pre-commit hook runs but doesn't auto-fix"

**Problem:** Hook installed but not executing auto-fix

**Solution:**
```bash
# Reinstall
make setup

# Manually run formatter
terraform fmt -recursive

# Try commit again
git commit -m "message"
```

### ❌ "Want to skip hooks?" (NOT RECOMMENDED)

```bash
# Force push bypassing all checks (DANGEROUS!)
git push --no-verify

# ⚠️ ONLY use for emergencies!
# This defeats the purpose of GLOBAL_RULES
```

---

## ✅ Checklist Before First Push

- [ ] Prerequisites installed (terraform, tflint, make)
- [ ] Setup completed (`make setup`)
- [ ] Setup verified (`make check-all` passes)
- [ ] Code changes made
- [ ] Pre-commit hook ran on `git commit`
- [ ] All checks pass (`make check-all`)
- [ ] Ready to push!

---

## 📞 Need Help?

See: **GLOBAL_RULES.md** - All 15 development rules  
See: **docs/TROUBLESHOOTING.md** - Common issues  
See: **docs/FAQ.md** - Frequently asked questions  

---

**Framework Repository:** https://github.com/sandya-portrfolio/pre-commit-rules
