# Getting started

You do not need the whole system on day one. This order gives value early and
adds each part only after the previous one works.

## Week 1: one ledger and one rules file

1. Pick one task tracker with an API and per-issue comments (this site uses
   Linear). Create one team for your own work.
2. Set up the workflow states from [Task tracker](system/task-tracker.md):
   Backlog, Todo, In Progress, Waiting, In Review, Done, Canceled, Duplicate.
3. Write a rules file for your agents, starting from the
   [agent rules template](starter-kit/agents-md.md). Fill in your authority
   tiers and your whitelist. Keep it short.
4. Do your work through issues: every ask you get becomes an issue, every
   agent turn ends in a "whose turn" state.

## Week 2: intake

5. Add a daily collector run that reads your chat and email for asks and
   creates or updates issues (see [Intake](workflows/intake.md)). Start with
   one source.
6. Add the duplicate check before every issue creation. Duplicates are the
   first thing that makes people stop trusting the ledger.

## Week 3: drafts and decisions

7. Turn on the drafts rule: agents prepare replies in place and never send.
   Track how much you edit each draft.
8. Introduce [decision cards](workflows/decision-cards.md) for choices that
   need you, with a default and a deadline.

## Week 4: checks and the loop

9. Add the [independent Done check](workflows/done-check.md).
10. Add the [reply watch](workflows/reply-watch.md) so agents pick up your
    answers without being mentioned.
11. Start the weekly [improvement loop](workflows/improvement-loop.md) and a
    change log for agent-made rule changes.

## What you need

- An agent that can run unattended on a schedule, read your chat and email,
  and call your tracker's API. A browser-based agent with your logged-in
  sessions is the simplest option.
- A coding agent for anything that changes code.
- A Git repository for the agents' rules, skills and memory, so every change
  is reviewable and reversible.

See [Tools](tools.md) for the specific stack and alternatives.
