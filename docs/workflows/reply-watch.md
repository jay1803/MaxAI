# Watching for replies

The owner should never have to mention an agent to make it notice an answer.
An hourly routine closes that gap.

## Reply watch (hourly)

1. If another run of the watch is live, stop. Read the watermark; the new
   watermark is the run start time.
2. **Delegation hygiene**: issues waiting on the owner or on others that have
   no agent delegate are given one, because the relay ignores undelegated
   issues.
3. List new comments by the owner (including relayed ones) since the
   watermark, excluding automatic session scaffolding.
4. A comment needs action if its issue is an agent-run project issue, a
   decision card, a "needs you" step, or In Review/Waiting with the latest
   agent comment asking the owner for something. Skip it if an agent already
   replied after it, or a running session is on that issue. If the comment
   mentions the agent, give the normal dispatch 30 minutes before treating it
   as dropped.
5. For each, do what the reply asks or implies: apply a decision, close a
   fulfilled "needs you" step, continue the work. Read back every write and
   post a short result comment.
6. **Resume dropped runs**: find dispatches that failed or stopped midway.
   Before resuming, check the issue and sibling sessions for a delivered
   result; if one exists, report its status instead of repeating the work.
7. **Duplicate and orphan sweep**: merge confirmed duplicates within the hour
   and give every new parentless issue a parent or a one-line reason.

## Before calling a request dropped

A session can start and answer inside the watch's gap. Re-read the comments
and the list of live sessions right before treating a request as dropped.

## Recurring issues

Recurring issue instances may be created long before they are due, and may
not start an agent session on their own (a session with no human creator can
be rejected by the relay). A watchdog routine runs twice a day:

1. List open recurring instances due in the last two days whose template is
   delegated to an agent. Match by due date, never by creation date.
2. If one template has several open instances, run the latest and mark the
   older ones as superseded.
3. If an expected instance is missing, create it once and record the miss.
4. Skip instances that already have a real agent answer or a live session.
5. Run each remaining instance, then post the result on it.
