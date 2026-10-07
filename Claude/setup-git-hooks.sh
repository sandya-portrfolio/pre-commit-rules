#!/bin/bash
# Automated git hooks setup script
# Run this once: chmod +x setup-git-hooks.sh && ./setup-git-hooks.sh
# Or use: make setup

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOOKS_DIR="$SCRIPT_DIR/.git/hooks"

echo "╔════════════════════════════════════════════════════╗"
echo "║         GLOBAL_RULES - Automated Setup            ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Check if .git directory exists
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository root directory"
    echo "   Please run this from your repo root"
    exit 1
fi

# Create hooks directory if it doesn't exist
mkdir -p "$HOOKS_DIR"

echo "📦 Installing git hooks..."
echo ""

# Create pre-push hook
echo "  Installing pre-push hook..."
cat > "$HOOKS_DIR/pre-push" << 'HOOK_EOF'
#!/bin/bash
# Pre-push hook - Enforces GLOBAL_RULE #5
# This automatically runs before every push

set -e

BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Don't run checks on main/master
if [[ "$BRANCH" == "main" || "$BRANCH" == "master" ]]; then
    echo "✅ Pushing to $BRANCH - skipping pre-push checks"
    exit 0
fi

echo "╔════════════════════════════════════════════════════╗"
echo "║     Running Pre-Push Validation Checks...         ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

FAILED=0

# Detect project type
if ls *.tf > /dev/null 2>&1 || [ -d "terraform" ]; then
    echo "📋 Terraform project detected"
    echo ""

    # Check formatting
    echo "  1️⃣  Checking terraform format..."
    if ! terraform fmt -check -recursive > /dev/null 2>&1; then
        echo "    ❌ Format issues found!"
        echo "    💡 Fix with: terraform fmt -recursive"
        FAILED=1
    else
        echo "    ✅ Format check passed"
    fi
    echo ""

    # Validate syntax
    echo "  2️⃣  Validating terraform syntax..."
    if ! terraform validate > /dev/null 2>&1; then
        echo "    ❌ Validation failed!"
        terraform validate
        FAILED=1
    else
        echo "    ✅ Validation passed"
    fi
    echo ""

    # Run tflint if available
    if command -v tflint &> /dev/null; then
        echo "  3️⃣  Running tflint linter..."
        if ! tflint > /dev/null 2>&1; then
            echo "    ❌ Linting issues found!"
            tflint
            FAILED=1
        else
            echo "    ✅ Linting passed"
        fi
    else
        echo "  3️⃣  tflint not installed - skipping"
        echo "    💡 Install with: brew install tflint"
    fi
    echo ""
fi

echo "╔════════════════════════════════════════════════════╗"
if [ $FAILED -eq 0 ]; then
    echo "║        ✅ All Checks PASSED - Push OK!          ║"
    echo "╚════════════════════════════════════════════════════╝"
    exit 0
else
    echo "║    ❌ Checks FAILED - Fix issues before push    ║"
    echo "╚════════════════════════════════════════════════════╝"
    echo ""
    echo "📖 See GLOBAL_RULES.md for details"
    exit 1
fi
HOOK_EOF

chmod +x "$HOOKS_DIR/pre-push"
echo "    ✅ Installed"
echo ""

# Create pre-commit hook
echo "  Installing pre-commit hook..."
cat > "$HOOKS_DIR/pre-commit" << 'HOOK_EOF'
#!/bin/bash
# Pre-commit hook - Prevents commits with formatting issues

if ls *.tf > /dev/null 2>&1 || [ -d "terraform" ]; then
    if ! terraform fmt -check -recursive > /dev/null 2>&1; then
        echo "❌ Terraform formatting issues found in staged files"
        echo ""
        echo "Auto-fixing with: terraform fmt -recursive"
        terraform fmt -recursive
        echo ""
        echo "✅ Formatting fixed!"
        echo "📝 Please re-stage and commit:"
        echo "   git add -A"
        echo "   git commit -m 'Your message'"
        exit 1
    fi
fi

exit 0
HOOK_EOF

chmod +x "$HOOKS_DIR/pre-commit"
echo "    ✅ Installed"
echo ""

echo "╔════════════════════════════════════════════════════╗"
echo "║              ✅ Setup Complete!                   ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""
echo "What's now enabled:"
echo "  ✓ Pre-commit checks (before committing)"
echo "  ✓ Pre-push checks (before pushing)"
echo "  ✓ Automatic validation on every push"
echo ""
echo "Next steps:"
echo "  1. Before each push, run: make check-all"
echo "  2. Or just push - hooks will auto-validate"
echo ""
echo "Documentation:"
echo "  See README.md for complete guide"
echo "  See GLOBAL_RULES.md for all project standards"
echo ""
