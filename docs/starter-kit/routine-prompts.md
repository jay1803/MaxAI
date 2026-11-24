# Routine prompts

Skeletons for the scheduled routines. Each routine runs in a fresh session,
so its prompt must be self-contained. Every prompt starts with the same
guard and ends with the same report line.

## Shared header and footer

```text
Start: if another run of this routine is live in the same window, stop. If one
finished, verify its output read-only and do not repeat its writes.
Follow the agent rules file. Do not send anything; drafts stay unsent.
Do not retry an external write whose outcome is unclear; read the target back.
State file: <path>. Keep it bounded: durable context, per-source watermarks,
and the two latest run entries.
...
Finish with one line:
ROUTINE_RESULT: {"status":"success|partial|blocked|failed","summary":"...","artifacts":[],"state_updates":{}}
```

## Daily intake (07:00)

```text
Run the task collector orchestrator over every source since each source's
covered-through time: chat, email (with the sender gate), shared-doc
mentions, calendar (read only), tracker comments, rule changes.
For each candidate: validate against the raw source, run the duplicate check,
then give it one outcome: do it, decision card, or track it.
Then run follow-up: prepare unsent drafts for replies and due nudges.
Advance a source's watermark only if it was fully read.
```

## Incremental loop (09:00, 13:00, 18:00 on workdays)

```text
Window = since the later of this loop's watermark and the daily intake's.
A. New signals: direct messages, mentions, replies in my recent threads,
   saved items; email that passes the sender gate; stalled issues.
B. Handle each with the three outcomes. Skip issues a live session is on.
C. (18:00) Day-end status pass on open issues.
D. (13:00) Fix every open check-failed issue an agent can fix.
```

## Reply watch (hourly)

See [Watching for replies](../workflows/reply-watch.md) for the steps:
delegation hygiene, new owner comments, action rules, resume dropped runs,
duplicate and orphan sweep.

## Recurring-issue watchdog (twice daily)

```text
List open recurring instances due in the last 2 days whose template is
delegated to an agent. Match by due date, never creation date. Run the
latest per template; mark older ones superseded; create a missing expected
instance once. Skip instances with a real agent answer or a live session.
```

## Repository sync (twice daily)

```text
In the agent repository: verify the remote and branch. Stage only legitimate
paths (never a blind add-all). Scan the staged diff for secrets, including
signed-URL parameters. Check per-file deletion counts for surprises. Commit,
merge the remote main, push. Never force-push, rebase or reset.
```
