---
name: global-work-rules
description: Global rules for ALL projects - applies to every account and repo
metadata: 
  type: feedback
  version: 1.0
  lastUpdated: 2026-10-07
---

# GLOBAL RULES - ALL PROJECTS

These rules apply to **EVERY project and account**. Follow consistently across all work.

---

## 1. PULL BEFORE STARTING ANY TASK

**Always:**
```bash
git pull origin main  # or current branch
```

**Why:** Sync with remote before touching anything. Don't assume local is current.

**When:** Start of every new task/change.

---

## 2. MATCH LOCAL WITH REMOTE REPO

**Don't ignore remote changes.** 
- Pull latest
- Check what changed remotely
- Sync before starting work
- Never work assuming only local state matters

---

## 3. FRESH START FOR EACH TASK

**Don't drag previous task context into new tasks.**
- If different repo/project → treat as fresh
- Don't assume previous patterns apply
- Read requirements carefully
- Check current state, don't assume

---

## 4. SIMPLE & CONCISE SUMMARIES

**After completing work:**
- What changed (1-2 sentences max)
- What to expect next
- No long explanations unless asked

Example:
```
✅ Added control-tower-agent infrastructure for all environments (dev/qa/prod).
Ready for pipeline validation - MR #18.
```

---

## 5. ALL CHECKS MUST PASS LOCALLY BEFORE PUSH

**Before every push, run ALL validation checks:**
```bash
# Terraform/IaC projects:
terraform fmt -check      # Check formatting
terraform validate        # Check syntax/config
terraform plan           # Plan for all environments (dev, qa, prod)
tflint                   # Lint check

# Other projects:
# Use project's linter, formatter, test, and build commands
```

**Rule:** ❌ Never push if local checks fail

**Why:** Prevents wasted pipeline time, keeps commit history clean, catches issues early, validates infrastructure changes won't fail

**Workflow:**
1. Make changes locally
2. Run all validation checks (including terraform plan for all environments)
3. Fix any issues found
4. Re-run checks until all pass ✅
5. THEN push to branch
6. Monitor pipeline until green

**For Terraform Multi-Environment:**
- Run `terraform validate` with each tfvars file
- Run `terraform plan -var-file=conf/dev.tfvars`
- Run `terraform plan -var-file=conf/qa.tfvars`
- Run `terraform plan -var-file=conf/prod.tfvars`
- Ensure all 3 environments plan successfully

---

## 6. PUSH TO BRANCH, NEVER TO MAIN

**Rule:**
- Create feature branch
- Push to branch
- Create MR
- Only push to main if explicitly told "push to main"

**Example:** ✅ `git push origin feature/ATL-134` but ❌ `git push origin main`

---

## 7. CREATE MR (NO TRACES OF CLAUDE)

**When creating MR:**
- Don't add "Created by Claude" or similar
- Don't leave bot signatures
- Make it look human-authored
- No traces that Claude did the work

---

## 8. MONITOR PIPELINE AUTONOMOUSLY

**After creating MR:**
- Monitor pipeline automatically
- Fix errors without asking
- Don't wait for user approval
- User won't be available for monitoring
- Push fixes to branch immediately

---

## 9. FIX ERRORS AUTOMATICALLY

**Pipeline failures:**
- Identify error
- Fix locally
- Validate
- Push fix
- Watch pipeline again
- Repeat until green ✅

**No need for user approval** - just fix and move forward.

---

## 10. DONT IMPACT EXISTING STRUCTURE

**When making changes:**
- Only change what's needed
- Don't refactor unless asked
- Don't reorganize files
- Don't "improve" existing code
- Minimal, focused changes only

---

## 11. ASK BEFORE DESTRUCTIVE CHANGES

**If your change would:**
- Delete files
- Remove code
- Change existing resources
- Modify infrastructure
- Impact existing services

**Then:** Ask for approval BEFORE pushing.

**Example:**
- ❌ Delete postgres.tf → Ask first
- ❌ Remove security group → Ask first  
- ✅ Add new service file → Just do it
- ✅ Update config → Just do it

---

## 12. DONT ASSUME CONTEXT

**For each new task:**
- Read requirements carefully
- Don't drag assumptions from previous tasks
- Check current state independently
- Verify before acting

---

## 13. RERUN STAGE IF RUNNER FAILS

**Pipeline stage failures:**
- If error is **runner/infrastructure failure** (not code issue)
  - Example: "runner timed out", "docker pull failed", "node unavailable"
  - Action: Rerun that stage automatically
  - No need to fix code, just retry

**When NOT to rerun:**
- Code errors (terraform validate failed, syntax error, etc.)
- Fix the code issue instead, then rerun

**How to rerun:**
- Use GitLab UI or API to retry the failed job
- Don't ask for approval - just do it
- Monitor until it passes or fails with real error

---

## 14. DON'T REMOVE FILES/RESOURCES TO FIX ISSUES

**When fixing failures:**
- ❌ Don't delete files to fix linting/validation errors
- ❌ Don't remove resources just to pass checks
- ✅ Refactor/update instead of removing
- ✅ Ask before removing anything significant

**Why:**
- Removing files affects OTHER environments
- Breaks existing infrastructure in other contexts
- Can impact resources that depend on what you removed
- Future requirements may need what you deleted

**Examples:**
- ❌ Remove AWS provider variables to fix unused variable warning
- ✅ Keep variables, comment them if truly unused, or find where they should be used
- ❌ Delete security group because it shows warnings
- ✅ Fix the security group configuration instead

**Rule:** If your fix involves REMOVING code/files/resources → **Ask approval first.**

---

## 15. KEEP REPOSITORY MEMORY PERSISTENT

**Memory management:**
- Save repository-based memory (not session-based)
- Don't delete old requirements/rules because new task came in
- Keep historical context - future work may need it
- Memory persists across projects/days/sessions

**Update memory when:**
- New repository pattern discovered
- New rule needed
- Old rule proves wrong → update, don't delete
- Requirements change → document the change, keep history

---

## Summary

| Rule | Focus | Action |
|------|-------|--------|
| 1-4 | Workflow Basics | Start clean, communicate clearly |
| **5** | **Quality Gate** | **Check locally before push** |
| 6-9 | Pipeline Safety | Use branches, monitor, fix issues |
| 10-12 | Focused Changes | Minimal, intentional, verified |
| 13-15 | Resilience & Memory | Retry infrastructure issues, preserve context |

---

## How to Follow These Rules

### Daily Checklist

- [ ] Pull latest before starting
- [ ] Make focused, minimal changes
- [ ] Run all validation checks locally
- [ ] Push only when checks pass
- [ ] Monitor pipeline automatically
- [ ] Fix errors as they appear

### Before Every Push

```bash
# 1. Validate locally
make check-all

# 2. If any fail
terraform fmt -recursive  # Fix formatting
make check-all           # Re-validate

# 3. When all pass
git push origin <branch>
```

### If Pipeline Fails

```bash
# 1. Check error (not runner failure)
git pull origin <branch>

# 2. Fix locally
make check-all
# Fix any issues
make check-all  # Verify

# 3. Push fix
git push origin <branch>

# 4. Monitor pipeline again
```

---

## Rules Applied To

- ✅ All projects
- ✅ All repositories
- ✅ All accounts
- ✅ All environments (dev, qa, prod)
- ✅ Across all sessions (even after sign-out)

**Always follow. No exceptions.**

---

**Version:** 1.0  
**Last Updated:** 2026-10-07  
**Maintained By:** Your Team
