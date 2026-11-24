---
summary: "The current stack, the job each tool does, and what any replacement needs."
---

# Tools

The method matters more than the tools. This is the current stack, the job
each tool does, and what to look for if you use something else.

| Job | Tool used | What any replacement needs |
| --- | --- | --- |
| Task tracker and agent conversation | [Linear](https://linear.app) | Custom states, labels, parent issues, templates and recurring issues, an API, and agent sessions or webhooks on comments |
| Local agent | Aside, a browser-based agent | Runs on your machine with your logged-in sessions; scheduled routines; sub-sessions; file system and shell access |
| Coding agent | Claude Code | Non-interactive mode, a read-only (plan) mode for reviews, works in Git worktrees |
| Cloud assistant | [ChatGPT](https://chatgpt.com) | Connectors to your tracker and chat, scheduled checks, can write and read back |
| Relay | A small self-built app | Turns tracker events into agent sessions; ignores events the agent caused itself; lets agents start sessions on other issues and show options for one-click answers |
| Team chat | Slack | API access for history, drafts and saved items |
| Email and calendar | Gmail, Google Calendar | Search, drafts; calendar read only for intake |
| Shared documents | Notion | Pages and comments colleagues can open |
| Agent repository | Git and GitHub | Private repository for rules, skills, memory; pull requests for code |
| Password manager | Any, with browser autofill | Agents use autofill; they never read or store secrets |

## Where each kind of content lives

| Content | Home | Why |
| --- | --- | --- |
| What the owner must do, and work state | Tracker | The single ledger; the owner's own workspace |
| Anything colleagues must read or confirm | Shared docs | Colleagues usually cannot open the owner's tracker |
| Project rules (decided facts such as eligibility or terms) | A rules database in shared docs, with a change log | One home per rule; changes are traceable |
| Agent rules, skills, memory, routines | Agent repository | Versioned, reviewable, reversible |
| Drafts | In place, in the tool they will be sent from | The owner edits and sends where the message lives |

## Notes

- Prefer APIs over clicking through a UI for reads. Use the UI for drafts the
  owner will open, so they appear where the owner expects them.
- Check that a newly connected tool actually authorizes with one call before
  relying on it; fall back to a working path instead of retrying a broken one.
- A stateless model call can return a detailed, plausible answer without
  having run any query. Re-verify numbers from a second, independent run, and
  compute totals with an explicit query.
