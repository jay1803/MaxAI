# Development policy

This repository uses a single long-lived branch, `main`. There is no `develop`
branch.

- Start every change on a new branch from the latest `main`. Suggested names:
  `docs/<topic>`, `site/<topic>`, `chore/<topic>`.
- Open a pull request against `main`. Keep it to one topic where possible, and
  describe what changed in the way of working.
- Agents never merge, never push to `main`, and never enable auto-merge. The
  owner reviews and merges.
- Do not force-push a branch that someone else has reviewed. Add commits
  instead.
- Merging to `main` publishes the site through the `pages` workflow, so the
  owner's merge is the publish approval. Changing Pages settings or repository
  visibility still needs the owner's explicit approval.
