# Independent Done check

Every issue an agent moves to Done is checked once by a session that did not
do the work. The checker judges the acceptance criteria against the real
outputs. It does not trust the executing session's summary.

## Contract for the executing session

- Before Done, post evidence: a link or ID for every output, and which
  acceptance item each one meets.
- Set Done through the agent's own identity, so the checker can tell
  agent-closed issues from owner-closed ones.

## Who checks, and when

- The daily agent check lists pending issues: closed by an agent, with no
  check comment after that close. A reopened and re-closed issue is checked
  again.
- It hands them to a fresh sub-session with no shared context (up to about ten
  issues per session). Never run the check inside the session that did the
  work.

## Checker procedure

1. Read the issue and find the acceptance criteria. If there are none, derive
   one to three from the ask and say so.
2. Read the comments only to collect pointers to outputs (URLs, commits, IDs).
   A claim like "done" or "verified" with no pointer is not evidence.
3. Open each output and check each criterion against it. For a criterion that
   can only be checked later, mark it pending.
4. Give a verdict per criterion: pass, fail, or cannot check (no read path).
   Overall: **pass** when every checkable criterion passes; **fail** when any
   fails or there are no pointers at all; **cannot check** when nothing could
   be read and nothing failed.
5. Post one top-level comment starting with `[Independent check] pass`,
   `fail` or `cannot check`, then one line per criterion with its evidence.
6. On fail: if an agent can fix the gap, set Todo and add `check-failed`; if
   only the owner can (a send, a credential, a decision), set In Review with
   the ask on the second line. Read the state back. Do nothing else: the
   checker does not fix, edit or message anyone.

## Fix loop

A fixed daily window works every open `check-failed` issue that an agent can
fix, posts new evidence and closes it again; the next daily check reviews it.
The weekly review reports coverage (target 100%) and the fail rate, and treats
each fail as a correction for the improvement loop.
