# Validation guidance

Run both checks before opening or updating a pull request, and report the
results in the pull request:

```bash
PRIVATE_TERMS_FILE=private-terms.txt python3 scripts/check_public.py
mkdocs build --strict
```

- `private-terms.txt` is a local, git-ignored list of private terms (one per
  line). In CI the same list comes from the `PRIVATE_TERMS` secret. Never
  commit it.
- `mkdocs build --strict` fails on broken internal links and pages missing
  from the navigation. Fix the cause; do not relax `strict`.
- The `check` workflow runs both checks on every pull request. Report a
  skipped or failed check as such.
