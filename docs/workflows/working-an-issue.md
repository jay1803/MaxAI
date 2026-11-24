---
summary: "What an agent does from the start of a session until the issue says whose turn it is."
---

# Working an issue

What an agent does from the moment a session starts on an issue until the turn
ends.

## 1. Start

- Tag the session with the issue key, so other sessions can see who is working
  on what.
- Read the issue, all of its comments (sorted by time, not only the first
  page), linked sources and the parent issue.
- Check for other running sessions on the same issue. Several sessions on one
  issue are fine when they do different tasks. Stop only if one is doing the
  same task.
- If the request arrived late, or after an error notice, check whether the
  work is already delivered before doing it again.

## 2. Decide the outcome

- Inside authority (L0 to L2 or whitelisted): do it.
- Needs the owner's judgment: write a decision card.
- Will be read by other people: prepare a draft and stop.
- Someone else owns the next step: hand it over and set Waiting.

If the issue itself says "plan first", the first turn is the plan only.
Delegating such an issue to the agent is not approval of the plan.

## 3. Do the work

- Read the live state of the target right before every external write. A
  newer comment may have changed the scope minutes ago.
- After a write that reports an ambiguous error, read the target back before
  retrying. Blind retries create duplicates.
- Cite only what was read in this run. A fact from memory or an earlier
  session is labeled as unverified.
- Stay inside the scope the owner named. When the scope is unclear, say which
  reading was used.

## 4. Post evidence

Post one comment with the result and a link or ID for every output: the
comment, file and commit, document URL, routine ID, draft location. Say which
acceptance item each one meets. Read the comment back to confirm it landed.

Keep progress and retry noise out of the issue. The issue gets confirmed
results and real blockers.

## 5. End with whose turn

Set the state (see [Task tracker](../system/task-tracker.md)):

- Done: delivered and verifiable, nothing needed from the owner.
- In Review: the owner must review, send or decide; the first line says what.
- Waiting: handed to someone else; due date = next follow-up.
- Todo: more agent work queued; the next step is written down.

Before leaving, create an issue for any deferred part, and make sure no new
issue is a duplicate or an orphan.

## Starting other sessions

An agent can start a session on another issue through the relay (for example,
when it unblocks a waiting step). An issue that becomes ready is started by
the session that unblocked it, or done by that session if it is in scope.
