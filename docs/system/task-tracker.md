# Task tracker

The tracker is the single ledger. These conventions make its state mean the
same thing to the owner and to every agent. The examples use Linear; any
tracker with custom states, labels, parent issues, due dates, templates and an
API works.

## States mean "whose turn"

| State | Meaning | What the agent writes |
| --- | --- | --- |
| Backlog | Not planned. | Nothing required. |
| Todo | More agent work is queued. | The next step. |
| In Progress | An agent is working right now. Never a resting state. | Nothing; leave it before the turn ends. |
| Waiting | Sent to someone else; waiting for them. | The due date is the next follow-up date. |
| In Review | The owner must review, send or decide. | The first line of the comment says exactly what. |
| Done | Delivered and verifiable; nothing needed from the owner. | Evidence links for every output. |
| Canceled | Not doing it. | Why. |
| Duplicate | Same deliverable as another issue. | Link to the kept issue. |

Every agent turn on an issue ends in one of these states. An optional Blocked
state works too, but it must name what blocks it.

## Assignment

- Every issue is assigned to the owner, so the owner's views show everything.
- Every issue is delegated to the executing agent, so the relay knows which
  agent responds to comments.
- The identity that creates an issue matters if your relay ignores events the
  agent caused itself. Create through the owner's identity when the issue
  should start a session now; create through the agent's identity when it
  should not (decision cards, waiting items, backlog).

## Due dates

The owner reads a due date as a commitment. Use the due date only for:

- a hard external deadline (label it, for example `external ETA`);
- a Waiting issue's next follow-up date;
- a decision card's deadline.

Never write an agent's estimated completion date into the due date. Clear the
due date when the deliverable closes.

## One deliverable, one issue

Before creating any issue, run a duplicate check that searches open issues and
issues closed in the last two weeks, including their descriptions and
comments, for the same source link and the same objects. Outcomes:

- **Update**: the deliverable is already tracked. Comment there; create nothing.
- **Check**: similar issues exist. Read them; create only for a different
  deliverable, and link it.
- **Create**: nothing similar.

A new ask on a closed issue reopens or links that issue. A safety-net sweep
runs hourly, merges confirmed duplicates (newer one becomes Duplicate of the
older) and lists new issues with no parent.

## Every issue has a home

Set a parent on every new issue: the issue it follows up, or else the open
umbrella issue of the same workstream, or else create the umbrella when this is
the workstream's second step. "Related" links do not replace the parent. Only a
real one-off (an invoice, a system notice, a recurring instance) stays
standalone, with one line saying why.

## Deferred scope gets its own issue

When an agent leaves part of an issue for later, it creates an issue for that
part in the same turn, links it and names it in its comment. An issue with an
untracked deferred part cannot be Done. A next step of the same deliverable
(send a draft, wait for an owner, check later) is not deferred scope: it stays
on the same issue as its next state.

## Labels that drive automation

| Label | Use |
| --- | --- |
| `decision` | A decision card. |
| `needs-you` | A step only the owner can do (credential, consent, device). |
| `check-failed` | The independent check failed; an agent fixes it. |
| `silence-default` | A decision card was carried out by its silence default. |
| `rule-change` | A change to a project rule that must be recorded in its home doc. |
| `external ETA` | The due date is an external commitment. |

## Views

- **My turn**: In Review, plus anything labeled `decision` or `needs-you`.
  This is the owner's only queue.
- **Today / This week / This month**: by due date and cycle.
- **Weekly cycles**, Monday to Sunday. The weekly planner places issues in the
  cycle.
- **Auto-close**: Backlog and Todo issues untouched for three months are
  canceled automatically.

## Templates

Recurring work runs from issue templates (daily plan, weekly plan, daily agent
check, weekly review, skill review, monthly workflow review, research radar)
and one-off templates (decision card, chat task, project sync, correction
retro, workflow improvement). See [Issue templates](../starter-kit/issue-templates.md).

Recurring instances may be created days before they are due and may not start
an agent session by themselves. A watchdog routine runs each recurring
instance on its due date. See [Watching for replies](../workflows/reply-watch.md#recurring-issues).
