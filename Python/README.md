# 🐍 Python Method - Interactive Script Approach

> **Python script with interactive menu for selecting pre-commit checks**

The Python method uses a standalone Python script that lets you choose which validation checks to run. Perfect for flexibility and transparency about what's being validated.

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
You work more...
      ↓
Ready to push? Run checks:
python pre_commit_checks.py
      ↓
INTERACTIVE MENU APPEARS ⚡
  1. 🏗️  Terraform (fmt, validate, tflint)
  2. 📦 Node/React (format, lint, test)
  3. 🐍 Python (black, isort, pylint, pytest)
  4. 🐹 Go (fmt, vet, lint, test)
  5. 📝 Git (uncommitted changes)
  
  Select: 1,2  (choose which to run)
      ↓
SELECTED CHECKS RUN 🚀
  ✅ Terraform format check PASSED
  ✅ Terraform validate PASSED
  ✅ tflint PASSED
  ⏭️  Node/React skipped (not selected)
      ↓
📊 SUMMARY:
  ✅ Passed: 3
  ⏭️  Skipped: 2
  ❌ Failed: 0
      ↓
All pass → Ready to push!
git push origin feature/branch
```

### Key Features

✅ **Interactive Menu** - Choose exactly which checks you want  
✅ **Auto-Detection** - Detects your project type automatically  
✅ **Selective Execution** - Skip checks you don't need  
✅ **Clear Reporting** - See exactly what passed/failed/skipped  
✅ **Multiple Modes** - Interactive, all, or specific types  
✅ **No Git Hooks** - Manual run when you're ready  
✅ **Multi-Project** - Works for Terraform, Node, Python, Go  

---

## 📦 Prerequisites

### Python Version

```bash
python --version    # Should be 3.7 or higher
python3 --version   # Or use python3 explicitly
```

**If Python not installed:**

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip
```

**CentOS/RHEL:**
```bash
sudo yum install -y python3 python3-pip
```

**Windows:**
```powershell
choco install python
```

### Project Tools (Based on Project Type)

**For Terraform Projects:**
```bash
brew install terraform tflint
```

**For Node/React Projects:**
```bash
npm install  # Installs dependencies from package.json
```

**For Python Projects:**
```bash
pip install -r requirements.txt
pip install black isort pylint pytest
```

**For Go Projects:**
```bash
brew install go golangci-lint
```

### Verify Installation

```bash
python3 --version      # Python 3.7+
terraform --version    # (if using Terraform)
```

---

## 🚀 Installation (1 Minute)

### Step 1: Clone Your Project

```bash
git clone https://github.com/yourteam/your-project.git
cd your-project
```

### Step 2: Get the Script

Choose **Option A** (recommended) or **Option B**:

**Option A: Auto-Download**
```bash
# Download the script
curl -o pre_commit_checks.py https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/Python/pre_commit_checks.py

# Make executable
chmod +x pre_commit_checks.py
```

**Option B: Manual Copy**
1. Download from: https://github.com/sandya-portrfolio/pre-commit-rules/tree/main/Python
2. Copy `pre_commit_checks.py` to your project root
3. Run: `chmod +x pre_commit_checks.py`

### Step 3: Test the Script

```bash
python3 pre_commit_checks.py --help
```

**Expected Output:**
```
usage: pre_commit_checks.py [-h] [--all] [--terraform] [--node] [--python] [--go] [--git]

Run pre-commit checks with optional selection

optional arguments:
  -h, --help     show this help message and exit
  --all          Run all applicable checks without prompting
  --terraform    Run only Terraform checks
  --node         Run only Node/React checks
  --python       Run only Python checks
  --go           Run only Go checks
  --git          Run only Git checks
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

# Stage your changes
git add main.tf variables.tf
```

### 3. Commit Your Changes

```bash
git commit -m "Add new infrastructure resources"
```

### 4. Run Interactive Checks

```bash
python3 pre_commit_checks.py
```

**You'll see:**
```
============================================================
🔍 PRE-COMMIT CHECKS - SELECT WHICH TO RUN
============================================================

1. 🏗️  Terraform (fmt, validate, tflint)
2. 📦 Node/React (format, lint, test)
3. 🐍 Python (black, isort, pylint, pytest)
4. 🐹 Go (fmt, vet, lint, test)
5. 📝 Git (uncommitted changes)

6. Run ALL checks
7. Cancel

Select checks (comma-separated, e.g., '1,2,3'): 
```

### 5. Select Your Checks

```bash
# Enter: 1,5
# This runs Terraform + Git checks
```

### 6. View Results

```bash
============================================================
📊 CHECK SUMMARY
============================================================

✅ PASSED (3):
   ✓ Terraform format check
   ✓ Terraform validate
   ✓ tflint linter

⏭️  SKIPPED (2):
   - Node/React checks
   - Python checks

❌ FAILED (0):

============================================================
✅ ALL CHECKS PASSED - Ready to push!
```

### 7. Push to GitHub

```bash
git push origin feature/my-feature
```

---

## 📅 Daily Workflow

### Before Each Commit

```bash
# Make your changes
vim main.tf

# Stage changes
git add main.tf

# Commit
git commit -m "Clear message"
```

### Before Each Push

```bash
# Run checks INTERACTIVELY
python3 pre_commit_checks.py

# OR run all checks (no menu)
python3 pre_commit_checks.py --all

# OR run specific type only
python3 pre_commit_checks.py --terraform

# If any fail:
# - Read error message
# - Fix the issue
# - Run checks again

# Once all pass
git push origin <branch-name>
```

### If Checks Fail

**Example: Terraform format failed**
```bash
# Run checks
python3 pre_commit_checks.py --all

# See the error:
# ❌ Terraform format check FAILED

# Auto-fix
terraform fmt -recursive

# Re-check
python3 pre_commit_checks.py --terraform

# If still failing, fix code manually and retry
```

---

## 📋 Commands Reference

### Interactive Mode (Recommended)

```bash
# Interactive menu - choose checks
python3 pre_commit_checks.py

# Select from menu:
# 1. Terraform
# 2. Node/React
# 3. Python
# 4. Go
# 5. Git
# 6. All
# 7. Cancel
```

### Run All Checks

```bash
# Auto-detect project type and run all applicable
python3 pre_commit_checks.py --all
```

### Run Specific Project Type

```bash
# Terraform only
python3 pre_commit_checks.py --terraform

# Node/React only
python3 pre_commit_checks.py --node

# Python only
python3 pre_commit_checks.py --python

# Go only
python3 pre_commit_checks.py --go

# Git only
python3 pre_commit_checks.py --git
```

### Run Multiple Types

```bash
# Terraform + Node
python3 pre_commit_checks.py --terraform --node

# Python + Go
python3 pre_commit_checks.py --python --go

# All three
python3 pre_commit_checks.py --terraform --python --go
```

### Help & Documentation

```bash
# Show help
python3 pre_commit_checks.py --help
```

---

## 🔍 What Gets Checked

### Terraform Checks
```
✓ terraform fmt -check -recursive   (formatting)
✓ terraform validate                (syntax)
✓ tflint                            (best practices)
```

### Node/React Checks
```
✓ npm run format                    (prettier)
✓ npm run lint                      (eslint)
✓ npm test                          (jest tests)
```

### Python Checks
```
✓ black --check .                   (formatting)
✓ isort --check-only .              (import sorting)
✓ pylint                            (linting)
✓ pytest                            (tests)
```

### Go Checks
```
✓ gofmt -l .                        (formatting)
✓ go vet ./...                      (static analysis)
✓ golangci-lint run                 (linting)
✓ go test -v ./...                  (tests)
```

### Git Checks
```
✓ git diff --exit-code              (uncommitted changes)
```

---

## 🐛 Troubleshooting

### ❌ "python3: command not found"

**Problem:** Python not installed

**Solution:**
```bash
# macOS
brew install python3

# Ubuntu
sudo apt-get install python3

# Check version
python3 --version
```

### ❌ "ModuleNotFoundError"

**Problem:** Python module missing

**Solution:**
```bash
# Most checks are built-in, but ensure tools are installed:
terraform --version
tflint --version
npm --version  # for Node projects
pip3 --version  # for Python projects
```

### ❌ "No supported project types detected"

**Problem:** Script can't find project files

**Solution:**
```bash
# Ensure you're in the project root directory
pwd
ls -la

# Should see: Makefile, package.json, *.tf, etc.
```

### ❌ "Terraform format check FAILED"

**Problem:** Code needs formatting

**Solution:**
```bash
# Auto-fix
terraform fmt -recursive

# Re-run checks
python3 pre_commit_checks.py --terraform
```

### ❌ "tflint not found"

**Problem:** tflint not installed

**Solution:**
```bash
# macOS
brew install tflint

# Ubuntu
sudo apt-get install tflint

# Verify
tflint --version
```

### ❌ "npm test failed"

**Problem:** Test suite failing (Node project)

**Solution:**
```bash
# Install dependencies first
npm install

# Run tests
npm test

# Fix failing tests

# Re-run checks
python3 pre_commit_checks.py --node
```

### ❌ "PermissionError when running script"

**Problem:** Script not executable

**Solution:**
```bash
chmod +x pre_commit_checks.py
python3 pre_commit_checks.py
```

### ❌ "Script hangs/takes too long"

**Problem:** A check is timing out

**Solution:**
```bash
# Run checks with timeout
# Kill stuck process (Ctrl+C)

# Try running specific checks instead
python3 pre_commit_checks.py --terraform

# Check if specific tool is slow
terraform validate
tflint
```

### ❌ "Selection menu not appearing"

**Problem:** Non-interactive mode

**Solution:**
```bash
# Make sure you're running interactively
python3 pre_commit_checks.py

# Not:
python3 pre_commit_checks.py < input.txt

# If redirected, use --all or --terraform flags instead
python3 pre_commit_checks.py --all
```

---

## 🔧 Customization

### Run as Git Hook (Optional)

**To run automatically before push**, create `.git/hooks/pre-push`:

```bash
#!/bin/bash
python3 pre_commit_checks.py --all
exit $?
```

Then make it executable:
```bash
chmod +x .git/hooks/pre-push
```

### Integrate with CI/CD

**GitHub Actions example:**
```yaml
name: Pre-commit Checks
on: [pull_request, push]
jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: python pre_commit_checks.py --all
```

---

## ✅ Checklist Before First Push

- [ ] Python 3.7+ installed
- [ ] Project tools installed (terraform, tflint, etc.)
- [ ] Script downloaded and executable
- [ ] Code changes made and committed
- [ ] Script runs without errors
- [ ] All selected checks pass
- [ ] Ready to push!

---

## 📚 Comparison: Python vs Claude Method

| Feature | Python | Claude |
|---------|--------|--------|
| **Setup Time** | 1 minute | 2 minutes |
| **User Choice** | Interactive menu | Automatic |
| **Manual Runs** | Yes, anytime | Via `make` |
| **Auto on Commit** | Optional hook | Yes, always |
| **Flexibility** | Very high | Moderate |
| **Learning Curve** | Easy | Moderate |
| **Best For** | Selective checks | Consistency |

---

## 📞 Need Help?

See: **GLOBAL_RULES.md** - All 15 development rules  
See: **docs/TROUBLESHOOTING.md** - Common issues  
See: **docs/FAQ.md** - Frequently asked questions  

---

**Framework Repository:** https://github.com/sandya-portrfolio/pre-commit-rules
