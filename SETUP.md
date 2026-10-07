# 🚀 Project Setup Guide - First Time

Complete step-by-step guide for setting up GLOBAL_RULES in any project.

---

## Prerequisites (One Time - Choose Your OS)

### macOS
```bash
brew install terraform tflint git
```

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install -y terraform tflint git
```

### CentOS/RHEL
```bash
sudo yum install -y terraform tflint git
```

### Windows (with Chocolatey)
```powershell
choco install terraform tflint git
```

---

## Setup Your Project (2 Minutes)

### Step 1: Clone Repository
```bash
git clone https://github.com/yourteam/your-project.git
cd your-project
```

### Step 2: Add Automation Files

**Option A: From this repo**
```bash
# Copy files from pre-commit-rules repo
curl -o Makefile https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/Makefile
curl -o setup-git-hooks.sh https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/setup-git-hooks.sh
curl -o GLOBAL_RULES.md https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/GLOBAL_RULES.md
curl -o README.md https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/README.md
```

**Option B: Manually**
```bash
# Copy these 4 files to your project root:
# 1. Makefile
# 2. setup-git-hooks.sh
# 3. GLOBAL_RULES.md
# 4. README.md
```

### Step 3: Setup Git Hooks (One Time Only!)
```bash
chmod +x setup-git-hooks.sh
make setup
```

Expected output:
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

### Step 4: Verify Setup
```bash
make check-all
```

Expected output:
```
✅ All validation checks PASSED!
   Safe to push: git push origin <branch>
```

---

## Daily Workflow

### Before Committing
```bash
# Make your changes
vim main.tf
vim variables.tf

# Stage changes
git add main.tf variables.tf

# Commit (pre-commit hook auto-runs)
git commit -m "Add control-tower-agent infrastructure"

# Pre-commit hook output:
# ✓ Pre-commit hook auto-checks
# ✓ Fixes formatting if needed
# ✓ Commit completes
```

### Before Pushing
```bash
# Run all validation checks
make check-all

# Expected:
# ╔════════════════════════════════════════╗
# ║   ✅ All Checks PASSED - Push OK!     ║
# ╚════════════════════════════════════════╝

# Now push safely
git push origin <branch-name>

# Pre-push hook auto-runs one final check
```

### If Checks Fail
```bash
# Auto-fix formatting
terraform fmt -recursive

# Re-check
make check-all

# If still failing - fix code issues
# Then re-check
make check-all

# Once all pass - push
git push origin <branch>
```

---

## Available Commands

```bash
# Setup (first time only)
make setup

# Before every push (IMPORTANT)
make check-all

# Individual commands
make fmt           # Auto-format code
make fmt-check     # Check format (no changes)
make validate      # Validate syntax
make lint          # Run linter
make clean         # Clean terraform cache

# Help
make help
```

---

## What Gets Checked

✅ **Terraform Formatting**
```bash
terraform fmt -check -recursive
```

✅ **Terraform Syntax**
```bash
terraform validate
```

✅ **Linting**
```bash
tflint
```

---

## Troubleshooting

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

**Solution:**
```bash
terraform fmt -recursive
make fmt-check  # Verify
```

### ❌ "tflint not found"

**Solution:**
```bash
brew install tflint
```

### ❌ "Pre-push hook not running"

**Solution:**
```bash
make setup  # Reinstall
```

### ✅ "Want to skip hooks?" (NOT RECOMMENDED)

```bash
# Force push bypassing all checks
git push --no-verify

# ⚠️ Only use for emergencies!
```

---

## GitHub CI/CD Workflows (Optional but Recommended)

Reusable workflow templates for any project type. Copy to your `.github/workflows/` directory.

### Available Workflow Templates

**Terraform Projects:**
```bash
curl -o .github/workflows/terraform-validate.yml \
  https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/.github/workflows/terraform-validate.yml
```
Checks: `terraform fmt`, `terraform validate`, `tflint`

**Node/React Projects:**
```bash
curl -o .github/workflows/node-ci.yml \
  https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/.github/workflows/node-ci.yml
```
Checks: format, lint, test, build

**Python Projects:**
```bash
curl -o .github/workflows/python-ci.yml \
  https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/.github/workflows/python-ci.yml
```
Checks: black, isort, pylint, pytest

**Go Projects:**
```bash
curl -o .github/workflows/go-ci.yml \
  https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/.github/workflows/go-ci.yml
```
Checks: gofmt, go vet, golangci-lint, tests

### Setup Workflows

**Step 1: Create directory**
```bash
mkdir -p .github/workflows
```

**Step 2: Copy templates** (choose for your project type)
```bash
# For Terraform
curl -o .github/workflows/terraform-validate.yml \
  https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/.github/workflows/terraform-validate.yml

# For Node/React
curl -o .github/workflows/node-ci.yml \
  https://raw.githubusercontent.com/sandya-portrfolio/pre-commit-rules/main/.github/workflows/node-ci.yml
```

**Step 3: Push to GitHub**
```bash
git add .github/
git commit -m "Add CI/CD workflows"
git push origin <branch>
```

**Step 4: Check GitHub**
Go to your repo → Actions tab → Workflows should run automatically on next push

---

## Documentation

| File | Purpose |
|------|---------|
| **README.md** | Complete guide & overview |
| **GLOBAL_RULES.md** | All 15 rules |
| **SETUP.md** | This file - team onboarding |
| **docs/TROUBLESHOOTING.md** | Common issues |
| **docs/FAQ.md** | Questions |
| **docs/EXAMPLES.md** | Usage examples |
| **.github/workflows/** | Reusable CI/CD templates |

---

## For Your Team

Share this with teammates:
```
https://github.com/sandya-portrfolio/pre-commit-rules
```

They can setup in **2 minutes:**
```bash
git clone <project>
cd <project>
make setup
```

---

## Next Steps

1. ✅ Setup complete
2. ✅ Read GLOBAL_RULES.md
3. ✅ Start developing (rules auto-enforce)
4. ✅ Before each push: `make check-all`

**You're ready!** 🚀
