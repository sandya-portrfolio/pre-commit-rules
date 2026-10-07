# ❓ Frequently Asked Questions

---

## Q: How often do rules change?

**A:** Rules are versioned in the repo. Current version: 1.0 (15 rules).

Updates are managed centrally. When you run `make setup`, you get the latest.

---

## Q: Do I need to setup for every project?

**A:** Yes, but it's just `make setup` (one time per project).

Each project needs its own hooks installed.

---

## Q: Can I work on multiple projects?

**A:** Absolutely! Each project has independent hooks.

Setup once per project, then work normally.

---

## Q: What if I'm on a new laptop?

**A:** Same process:
```bash
git clone <project>
make setup
```

Everything auto-installs.

---

## Q: Can teammates have different setups?

**A:** No - everyone uses same GLOBAL_RULES for consistency.

That's the whole point! One standard for all.

---

## Q: How do I update the rules?

**A:** Edit the pre-commit-rules repo:

1. Update GLOBAL_RULES.md
2. Push to main
3. Other projects auto-reference latest version
4. Next `make setup` gets the updates

---

## Q: Do hooks work offline?

**A:** Yes! All checks run locally:
- ✓ No internet needed
- ✓ No external services
- ✓ Fully local validation

---

## Q: Can I commit without running checks?

**A:** Not recommended, but possible:
```bash
git commit --no-verify
```

⚠️ This skips the pre-commit hook.

---

## Q: What if I disagree with a rule?

**A:** Propose changes!

1. Discuss with team
2. Update GLOBAL_RULES.md
3. Push to pre-commit-rules repo
4. All projects get the update

---

## Q: Do checks run on main/master?

**A:** No - pre-push hook skips checks on main/master.

This prevents blocking production pushes.

---

## Q: Can I disable a specific check?

**A:** Yes, but rarely:
```hcl
# tflint-ignore: rule_name
resource "..." { }
```

Use sparingly and with good reason.

---

## Q: What happens if a check fails?

**A:** Push is blocked.

You must fix locally and re-push.

---

## Q: How long does setup take?

**A:** 2 minutes:
```bash
make setup        # ~30 seconds
make check-all    # ~1 minute
```

Done!

---

## Q: Do pre-commit hooks slow down commits?

**A:** Minimal impact (~1 second):
- Just checks formatting
- Auto-fixes if possible
- Runs locally

---

## Q: Do pre-push hooks slow down pushes?

**A:** Minimal impact (~2-5 seconds):
- Checks format + syntax + linting
- Runs locally
- Catches errors before pipeline

Saves time overall by preventing pipeline failures.

---

## Q: What if CI/CD also runs these checks?

**A:** Good! Redundancy:
1. **Local** (pre-commit/push hooks) - catches errors early
2. **CI/CD** (GitHub Actions) - final gate

Two levels of protection.

---

## Q: Can I run checks without hooks?

**A:** Yes:
```bash
make check-all      # All checks
make fmt-check      # Just format
make validate       # Just validate
make lint           # Just linter
```

---

## Q: What's the difference between fmt and fmt-check?

**A:**
- `make fmt` - Auto-fixes formatting
- `make fmt-check` - Checks only (no changes)

Use `fmt-check` to verify, `fmt` to fix.

---

## Q: Where do hooks get installed?

**A:** `.git/hooks/` directory:
```bash
.git/hooks/pre-push      # Auto-runs before push
.git/hooks/pre-commit    # Auto-runs before commit
```

---

## Q: Can I manually run hooks?

**A:** Yes:
```bash
.git/hooks/pre-push
.git/hooks/pre-commit
```

Or use `make` commands instead.

---

## Q: How do I know setup worked?

**A:** Run this:
```bash
make check-all
```

Should see:
```
✅ All validation checks PASSED!
```

---

## Q: What if one team member's setup broke?

**A:** Reinstall:
```bash
make setup
make check-all
```

---

## Q: Is this compatible with my IDE?

**A:** Yes! Hooks run in git, IDE-independent.

Works with VS Code, IntelliJ, vim, etc.

---

## Q: Do I need to learn git hooks?

**A:** No! `make setup` handles everything.

Transparent automation - you just code normally.

---

## Q: Can I customize the checks?

**A:** Limited:
- Add tflint-ignore comments for exceptions
- Disable specific linting rules
- Override in special cases

But generally: follow the rules!

---

## Q: What if I forgot to run checks?

**A:** Pre-push hook catches it:
```bash
git push
# Hook runs, sees issues
# Push is blocked
# Fix locally
git push  # Retry
```

---

## Still have questions?

1. **Check README.md** - Full guide
2. **Check TROUBLESHOOTING.md** - Common issues
3. **Check GLOBAL_RULES.md** - All rules
4. **Ask your team lead**

---

**Last Updated:** 2026-10-07
