
**Rule:** ❌ Never push if local checks fail

**Why:** Prevents wasted pipeline time, keeps commit history clean, catches issues early

**Workflow:**
1. Make changes locally
2. Run all validation checks
3. Fix any issues found
4. Re-run checks until all pass ✅
5. THEN push to branch
6. Monitor pipeline until green

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

**These rules apply to:**
- All projects
- All repositories
- All accounts
- Across all sessions (even after sign-out)

**Always follow. No exceptions.**
