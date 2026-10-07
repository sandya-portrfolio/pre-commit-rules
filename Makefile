.PHONY: validate fmt lint check-all setup clean help

# Setup git hooks (one time)
setup:
	@echo "📦 Setting up git hooks for this project..."
	@chmod +x setup-git-hooks.sh
	@./setup-git-hooks.sh
	@echo "✅ Setup complete! Rules are now enforced."

# Format code
fmt:
	@echo "📝 Formatting Terraform..."
	@terraform fmt -recursive

# Check formatting (without modifying)
fmt-check:
	@echo "📝 Checking Terraform format..."
	@terraform fmt -check

# Validate syntax
validate:
	@echo "✓ Validating Terraform syntax..."
	@terraform validate

# Run linter
lint:
	@echo "🔍 Running tflint..."
	@tflint

# Run ALL checks (GLOBAL_RULE #5)
check-all: fmt-check validate lint
	@echo ""
	@echo "✅ All validation checks PASSED!"
	@echo "   Safe to push: git push origin <branch>"

# Clean terraform cache
clean:
	@echo "🧹 Cleaning Terraform cache..."
	@rm -rf .terraform/ .terraform.lock.hcl terraform.tfstate*
	@echo "✅ Clean complete"

# Show help
help:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "GLOBAL_RULES Automation - Available Commands"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo ""
	@echo "First time setup:"
	@echo "  make setup      - Install git hooks (one time)"
	@echo ""
	@echo "Before every push:"
	@echo "  make check-all  - Run ALL validation checks"
	@echo ""
	@echo "Individual checks:"
	@echo "  make fmt        - Format Terraform code"
	@echo "  make fmt-check  - Check format (no changes)"
	@echo "  make validate   - Validate Terraform syntax"
	@echo "  make lint       - Run tflint checks"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean      - Clean Terraform cache"
	@echo ""
	@echo "Documentation:"
	@echo "  See README.md for complete guide"
	@echo "  See GLOBAL_RULES.md for all project standards"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
