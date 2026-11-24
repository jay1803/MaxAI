---
summary: "Turning chat, email and stalled work into issues, with filters, watermarks and three outcomes."
---

# Intake

Intake turns signals into issues. It runs as one full daily sweep plus short
incremental windows during the workday.

## Sources

- **Chat**: direct and group messages to the owner, @mentions, new replies in
  threads the owner posted in recently, and items the owner saved for later.
- **Email**: mail to the owner, filtered by a sender gate.
- **Shared docs**: mentions and comments addressed to the owner.
- **Calendar**: deadline-bearing events and commitments to follow up (read
  only; intake never writes to the calendar).
- **Tracker issues**: comments on issues the owner is involved in.
- **Stalled issues**: Waiting past its follow-up date, In Review for more than
  two working days, Todo unchanged for seven days.
- **Rule changes**: decisions that change a project rule (pricing, eligibility,
  behavior, terms), collected separately and recorded in the project's rules
  document.

## Filters before judgment

Drop, before thinking about it:

- bots, automated notifications, newsletters, marketing;
- FYI messages and pure acknowledgements;
- email from senders who fail the gate: internal humans pass by default;
  external senders pass only with verified prior contact; no-reply and system
  senders never pass;
- anything already tracked (the duplicate check decides, not memory).

Then check each candidate against its raw source:

- Who is actually asking whom? A mention on a thread root does not make a
  later reply in that thread addressed to the owner.
- Whose words are these? A relayed view belongs to the person it came from.
- Is the decision settled? Read the whole thread; a later message may reverse
  the first reply.
- Is it still open? The owner may already have answered from another device.

## Three outcomes

Every candidate that survives gets exactly one outcome in the same run:

1. **Do it**: the work is whitelisted or already authorized. Do it, then show
   the owner the result.
2. **Needs the owner's judgment**: write a [decision card](decision-cards.md).
3. **Someone else owns it**: track it in Waiting with a follow-up date.

Agent-created issues never sit in Todo or Backlog without one of these.

## Watermarks

- Keep a covered-through time per source, not one global watermark.
- Never advance a source's watermark if that source was not fully read in this
  run.
- Do not use the creation time of the newest issue as a watermark: an issue
  may have come from a manual dispatch that skipped the sweep.

## Guard against duplicate runs

Scheduled runs can be dispatched twice. Before any shared write, check for a
sibling run of the same routine in the same window. If one is live, stop. If
one finished, verify its output read-only and do not repeat its writes.

## Coverage is not proof of absence

A search result is a candidate list, not the truth. Date filters in mail and
chat search drop items silently; chat search misses messages that channel
history returns. An empty result from a degraded source is reported as a
coverage gap, not as "nothing new".
