# 📋 Global Rules & Pre-Commit Framework

> **Centralized automation framework for consistent development standards across all projects**

This repository contains **GLOBAL_RULES**, automation scripts, and CI/CD templates that ensure every developer, every machine, and every project follows the same quality standards.

**Choose Your Method:**
- 🤖 **Claude Method** - Automatic git hooks + Makefile (Set it and forget it)
- 🐍 **Python Method** - Interactive script with menu selection (Choose which checks)

---

## 🎯 What This Does

✅ **Enforces Rules Automatically** - Git hooks run checks before every commit & push  
✅ **Prevents Bad Commits** - Catches errors locally before they reach the pipeline  
✅ **Saves Pipeline Time** - No wasted CI/CD runs on code that won't pass  
✅ **Team Consistency** - Everyone follows same standards, no exceptions  
✅ **Works Everywhere** - Same rules on any laptop, any machine, any team member  

---

## 🚀 Choose Your Implementation Method

### 🤖 Claude Method (Automatic)

**Location:** `/Claude` folder  
**Best For:** Teams that want automatic enforcement with zero setup per commit  

```bash
cd Claude
make setup           # One-time setup
git commit -m "msg"  # Pre-commit hook auto-runs ✅
git push            # Pre-push hook auto-runs ✅
```

**What you get:**
- ✅ Automatic checks on every commit
- ✅ Checks on every push
- ✅ Auto-fix formatting
- ✅ Single setup command
- ✅ No thinking needed

**See:** [Claude/README.md](Claude/README.md) for complete guide

---

### 🐍 Python Method (Interactive)

**Location:** `/Python` folder  
**Best For:** Developers who want to choose which checks to run  

```bash
cd Python
python3 pre_commit_checks.py  # Interactive menu appears
# Select: 1,2,3 (choose your checks)
git push                      # Once checks pass
```

**What you get:**
- ✅ Interactive menu to select checks
- ✅ Run anytime, no git hooks
- ✅ Flexible, transparent control
- ✅ Perfect for learning
- ✅ Multi-project support

**See:** [Python/README.md](Python/README.md) for complete guide

---

## 📊 Comparison

| Feature | Claude | Python |
|---------|--------|--------|
| **Setup Time** | 2 min | 1 min |
| **Learning Curve** | Moderate | Easy |
| **Auto Enforcement** | ✅ Yes | ❌ Manual |
| **Interactive Menu** | ❌ No | ✅ Yes |
| **Flexible** | Moderate | ✅ High |
| **Best For** | Teams | Individuals |
| **Best For** | Consistency | Transparency |

**Choose Claude if:** Your team needs automatic enforcement  
**Choose Python if:** You want control and transparency  
**Use Both if:** Different projects have different needs

---

## 📚 Table of Contents

1. [Quick Start](#quick-start)
2. [End-to-End Workflow](#end-to-end-workflow)
3. [Installation](#installation)
4. [Available Commands](#available-commands)
5. [Documentation](#documentation)
6. [Rules Overview](#rules-overview)
7. [Troubleshooting](#troubleshooting)

---

## 🚀 Quick Start

### For New Projects (2 minutes)

```bash
# 1. Clone your project
git clone https://github.com/yourteam/your-project.git
cd your-project

# 2. Add these files from this repo
curl -o README.md https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/README.md
curl -o Makefile https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/Makefile
curl -o setup-git-hooks.sh https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/setup-git-hooks.sh
curl -o GLOBAL_RULES.md https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/GLOBAL_RULES.md

# 3. Make setup script executable and run it
chmod +x setup-git-hooks.sh
make setup

# ✅ Done! Your project now enforces all rules automatically
```

### For Existing Projects

```bash
# Add to your repo root
cp Makefile your-project/
cp setup-git-hooks.sh your-project/
cp GLOBAL_RULES.md your-project/

# Setup
cd your-project
make setup
```

---

## 🔄 End-to-End Workflow

### **Phase 1: Initial Setup (First Time - 2 minutes)**

```bash
# Step 1: Clone repository
git clone https://github.com/yourteam/your-project.git
cd your-project

# Step 2: Add automation files
make setup

# Output:
# ╔════════════════════════════════════════════════════╗
# ║         GLOBAL_RULES - Automated Setup            ║
# ╚════════════════════════════════════════════════════╝
#
# 📦 Installing git hooks...
#   Installing pre-push hook... ✅ Installed
#   Installing pre-commit hook... ✅ Installed
#
# ╔════════════════════════════════════════════════════╗
# ║              ✅ Setup Complete!                   ║
# ╚════════════════════════════════════════════════════╝

# ✅ Git hooks now auto-check every commit & push
```

---

### **Phase 2: Daily Development (Every Time)**

#### **Step 1: Make Changes**
```bash
# Edit your code
vim main.tf
vim variables.tf

# Stage changes
git add main.tf variables.tf
```

#### **Step 2: Commit (Pre-Commit Hook Auto-Runs)**
```bash
git commit -m "Add control-tower-agent infrastructure"

# Output:
# ✓ Pre-commit hook runs automatically
# ✓ Checks formatting
# ✓ Auto-fixes if needed
# ✓ Commit completes
```

#### **Step 3: Validate Before Push**
```bash
# Run all validation checks
make check-all

# Output:
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

#### **Step 4: Push (Pre-Push Hook Auto-Runs)**
```bash
git push origin feature/my-feature

# Pre-push hook runs one final check
# If all pass → Push succeeds
# If any fail → Push blocked (fix first)
```

#### **Step 5: Pipeline Validation**
```
GitHub Actions / GitLab CI runs:
  ✓ terraform fmt check
  ✓ terraform validate
  ✓ tflint scan
  ✓ gitleaks scan
  ✓ trivy iac scan
  ✓ terraform plan

All automated. No manual steps.
```

---

## 💾 Installation

### Prerequisites (One Time)

```bash
# macOS
brew install terraform tflint git

# Ubuntu/Debian
sudo apt-get install terraform tflint git

# CentOS/RHEL
sudo yum install terraform tflint git

# Windows (with Chocolatey)
choco install terraform tflint git
```

### Setup in Your Project

```bash
# Clone from pre-commit-rules repo
git clone https://github.com/sandya-portrfolio/pre-commit-rules.git
cd pre-commit-rules

# OR manually add files to your project:
# 1. Copy Makefile
# 2. Copy setup-git-hooks.sh
# 3. Copy GLOBAL_RULES.md

# Then run:
make setup

# Verify:
make check-all
# Expected: ✅ All checks PASSED
```

---

## 📋 Available Commands

### Using Python Script (Recommended - Interactive)

```bash
# Interactive mode (choose which checks to run)
python pre_commit_checks.py

# Example menu:
# 1. 🏗️  Terraform (fmt, validate, tflint)
# 2. 📦 Node/React (format, lint, test)
# 3. 🐍 Python (black, isort, pylint, pytest)
# 4. 🐹 Go (fmt, vet, lint, test)
# 5. 📝 Git (uncommitted changes)
# 
# Select: 1,2  (runs Terraform + Node checks)
```

### Python Script Options

```bash
# Run all applicable checks
python pre_commit_checks.py --all

# Run specific check type
python pre_commit_checks.py --terraform    # Only Terraform
python pre_commit_checks.py --node         # Only Node/React
python pre_commit_checks.py --python       # Only Python
python pre_commit_checks.py --go           # Only Go
python pre_commit_checks.py --git          # Only Git checks

# Help
python pre_commit_checks.py --help
```

### Using Makefile (Traditional)

```bash
# Run ALL checks before push (recommended)
make check-all
# Runs: fmt-check, validate, lint

# Check code formatting
make fmt-check
# Shows if formatting issues exist (no changes)

# Auto-fix formatting
make fmt
# Automatically reformats code

# Validate syntax
make validate
# Checks Terraform syntax

# Run linter
make lint
# Runs tflint checks
```

### Setup & Maintenance

```bash
# Initial setup (one time)
make setup
# Installs git hooks

# Clean Terraform cache
make clean
# Removes .terraform/, .terraform.lock.hcl, state files

# Show all commands
make help
# Lists all available targets
```

---

## 🔄 GitHub CI/CD Workflows (Optional)

Reusable workflow templates for any project type. Automatically validate code on every push/PR.

### Available Templates

Copy any of these to your `.github/workflows/` directory:

```bash
# Terraform projects
curl -o .github/workflows/terraform-validate.yml \
  https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/.github/workflows/terraform-validate.yml

# Node/React projects
curl -o .github/workflows/node-ci.yml \
  https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/.github/workflows/node-ci.yml

# Python projects
curl -o .github/workflows/python-ci.yml \
  https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/.github/workflows/python-ci.yml

# Go projects
curl -o .github/workflows/go-ci.yml \
  https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/.github/workflows/go-ci.yml
```

### What They Check

| Workflow | Checks |
|----------|--------|
| **terraform-validate.yml** | `terraform fmt`, `terraform validate`, `tflint` |
| **node-ci.yml** | format, lint, test, build |
| **python-ci.yml** | black, isort, pylint, pytest |
| **go-ci.yml** | gofmt, go vet, golangci-lint, tests |

**See SETUP.md for complete workflow setup instructions.**

---

## 📖 Documentation

| File | Purpose |
|------|---------|
| **GLOBAL_RULES.md** | All 15 development rules (read this!) |
| **SETUP.md** | Step-by-step team onboarding guide |
| **docs/TROUBLESHOOTING.md** | Common issues & solutions |
| **docs/FAQ.md** | Frequently asked questions |
| **docs/EXAMPLES.md** | Real-world usage examples |
| **scripts/pre-push** | Auto-runs before every push |
| **scripts/pre-commit** | Auto-runs before every commit |
| **.github/workflows/** | Reusable CI/CD templates |

---

## 📜 Rules Overview

### **15 Global Rules for All Projects**

| # | Rule | Purpose |
|---|------|---------|
| 1 | Pull Before Starting Task | Sync with remote |
| 2 | Match Local With Remote | Keep in sync |
| 3 | Fresh Start For Each Task | No context drag |
| 4 | Simple & Concise Summaries | Clear communication |
| **5** | **All Checks Pass Before Push** | Quality gate |
| 6 | Push to Branch, Never to Main | Safety |
| 7 | Create MR (No Traces of Claude) | Clean history |
| 8 | Monitor Pipeline Autonomously | Continuous validation |
| 9 | Fix Errors Automatically | Self-healing |
| 10 | Don't Impact Existing Structure | Focused changes |
| 11 | Ask Before Destructive Changes | Approval required |
| 12 | Don't Assume Context | Fresh analysis |
| 13 | Rerun Stage If Runner Fails | Infrastructure resilience |
| 14 | Don't Remove Files To Fix Issues | Preserve code |
| 15 | Keep Repository Memory Persistent | Historical context |

**See GLOBAL_RULES.md for complete details.**

---

## 🔍 How It Works

### **Pre-Commit Hook** (Runs before every commit)

```bash
git commit -m "Your message"
    ↓
Pre-commit hook triggers:
  ✓ Checks formatting
  ✓ Auto-fixes if needed
  ✓ Allows commit if OK
  ✗ Blocks if serious issues
```

### **Pre-Push Hook** (Runs before every push)

```bash
git push origin <branch>
    ↓
Pre-push hook triggers:
  ✓ Checks formatting
  ✓ Validates syntax
  ✓ Runs linter (tflint)
  ✓ Allows push if all pass
  ✗ Blocks if any fail
```

### **CI/CD Pipeline** (Runs on GitHub/GitLab)

```
PR Created
    ↓
GitHub Actions / GitLab CI:
  ✓ terraform fmt check
  ✓ terraform validate
  ✓ tflint scan
  ✓ gitleaks scan
  ✓ trivy iac scan
  ✓ terraform plan
    ↓
  All Pass → Merge Ready
  Any Fail → Blocked
```

---

## ✅ What Gets Checked

### **Terraform Projects**

```bash
✓ Code Formatting
  → terraform fmt -check
  → Auto-fixable

✓ Syntax Validation
  → terraform validate
  → Catches errors early

✓ Code Linting
  → tflint
  → Best practices

✓ Security Scanning
  → gitleaks (secrets detection)
  → trivy (vulnerability scan)

✓ Infrastructure Validation
  → iac_scan (infrastructure as code)
  → terraform plan (dry-run)
```

---

## 🐛 Troubleshooting

### **Git Hooks Not Running?**

```bash
# Reinstall
make setup

# Verify
ls -la .git/hooks/pre-push
ls -la .git/hooks/pre-commit
```

### **Formatting Issues?**

```bash
# Auto-fix
terraform fmt -recursive

# Verify
make fmt-check
```

### **TFLint Not Found?**

```bash
# Install
brew install tflint

# Verify
tflint --version
```

### **Want to Bypass Hooks?** (Not Recommended)

```bash
# Force push (use only for emergencies)
git push --no-verify

# ⚠️ This bypasses ALL checks
```

**See docs/TROUBLESHOOTING.md for more issues.**

---

## 👥 For Your Team

### **Share This Link:**
```
https://github.com/sandya-portrfolio/pre-commit-rules
```

### **Team Members Setup (2 minutes):**

```bash
# 1. Clone project
git clone https://github.com/yourteam/your-project.git
cd your-project

# 2. Setup rules
make setup

# 3. Start working
# Rules auto-enforce on every commit/push
```

### **No Manual Steps Needed**

- Hooks auto-install
- Checks auto-run
- Errors auto-block
- Team stays aligned

---

## 📊 Benefits

| Benefit | Impact |
|---------|--------|
| **Catch Errors Early** | Before pipeline runs |
| **Save CI/CD Time** | 50% fewer failed runs |
| **Team Consistency** | Same standards everywhere |
| **Works Offline** | No internet needed |
| **Zero Setup Time** | `make setup` and done |
| **Easy to Update** | Central source of truth |

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-10-07 | Initial release with 15 global rules |

---

## 📞 Support

### **Quick Help**
```bash
# See all commands
make help

# View all rules
cat GLOBAL_RULES.md

# Read troubleshooting
cat docs/TROUBLESHOOTING.md
```

### **Common Issues**
See **docs/TROUBLESHOOTING.md**

### **Questions?**
See **docs/FAQ.md**

### **Examples**
See **docs/EXAMPLES.md**

---

## 📄 License

MIT License - Free to use and modify

---

## 🎯 Next Steps

1. **Read GLOBAL_RULES.md** - Understand all 15 rules
2. **Run make setup** - Install git hooks
3. **Run make check-all** - Verify everything works
4. **Start developing** - Rules auto-enforce

---

**Made for teams. Tested by teams. Used by teams.** ✨

Last Updated: 2026-10-07  
Maintained By: Your Team  
Status: Production Ready
