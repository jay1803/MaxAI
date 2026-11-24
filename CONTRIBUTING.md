# Contributing

## How a change lands

1. Create a branch from `main`.
2. Make the change. Keep one topic per pull request when possible. Every
   page starts with a `summary:` line in its front matter; the home page and
   the page header show it.
3. Run the checks:

   ```bash
   python3 scripts/check_public.py
   .venv/bin/mkdocs build --strict
   ```

4. Open a pull request against `main`. Fill in the template checklist.
5. The owner reviews and merges. Agents never merge in this repository.
   Merging publishes: the `pages` workflow deploys `main` to the site.

Every update to the way of working is a new pull request, so the pull request
history doubles as the change history of the method. Add a line to
[`docs/changelog.md`](docs/changelog.md) in the same pull request.

## What may appear here

This repository is meant to become public. Write only what another person can
reuse. Do not include:

- names, handles, emails, phone numbers or photos of the owner or anyone else;
- employer names, product names, customers, partners, prices, metrics or plans;
- internal URLs, workspace names, channel names, user IDs, issue keys or
  database IDs from any real system;
- credentials, tokens, signed URLs or local file paths from a real machine;
- quotes from private conversations, even anonymized ones, when the content
  itself is internal.

Use neutral placeholders instead: `the owner`, `a colleague`, `PROJ-123`,
`<team>`, `<channel>`, `example.com`.

Public product names of tools (Linear, Slack, Git, GitHub, Claude Code,
ChatGPT and similar) are fine.

## The public-safety check

`scripts/check_public.py` scans tracked text files for generic leak patterns
(emails, tokens, signed URLs, local paths, chat-tool user IDs, UUIDs, real issue
keys). It also reads an optional private term list:

- locally from the file named in `PRIVATE_TERMS_FILE`, one term per line;
- in CI from the `PRIVATE_TERMS` repository secret, one term per line.

The private term list never goes into the repository, because the list itself
would be a leak. A failing check blocks the pull request.
