# Validation guidance

Run these checks before opening or updating a pull request, and report the
results in the pull request:

```bash
PRIVATE_TERMS_FILE=private-terms.txt python3 scripts/check_public.py
python3 scripts/check_lists.py
mkdocs build --strict
```

- `private-terms.txt` is a local, git-ignored list of private terms (one per
  line). In CI the same list comes from the `PRIVATE_TERMS` secret. Never
  commit it.
- `mkdocs build --strict` fails on broken internal links and pages missing
  from the navigation. Fix the cause; do not relax `strict`.
- `check_lists.py` fails on nested list items indented by fewer than four
  spaces. The parser would render them as extra items of the parent list.
- The `check` workflow runs all three checks on every pull request. Report a
  skipped or failed check as such.
