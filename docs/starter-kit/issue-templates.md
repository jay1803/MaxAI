---
summary: "Decision card, chat task, plans, daily check, weekly review and the other templates that drive the loop."
---

# Issue templates

Each template below is the description of a tracker issue template. Recurring
ones are run by the watchdog on their due date.

## Decision card

See [Decision cards](../workflows/decision-cards.md) for the rules.

```text
Title: [Decision] <one-sentence question>
Labels: decision        State: In Review        Due: <deadline>

Question:
Level: L1-L2 | L3
Evidence:
Recommendation:
Default:
Undo:
Deadline: YYYY-MM-DD
How to reply: pick an option in the session, or comment "agree" or your change
```

## Chat task

Created by the owner with one link to a chat message the owner wants handled.

```text
Title: Chat task
Source: <message link>

Agent: if the ask is simple and inside authority (an access grant, a
lookup), do it now. Otherwise work out the context, rewrite this issue's title
and description, link related issues, and leave any reply as an unsent draft
in the chat tool. I send replies myself.
```

## Daily plan and weekly plan

```text
Title: Daily plan | Weekly plan
Agent: run the planner in daily | weekly mode. Planning issues get no
priority and no due date.
```

## Daily agent check (recurring, daily)

```text
Title: Agent daily check
Steps:
0. Independent Done check: list agent-closed issues without a check comment
   and hand them to a fresh session.
1. Decision cards past their deadline: carry out L1-L2 silence defaults;
   list L3 ones.
2. Stalled issues: Waiting past follow-up, In Review over 2 working days,
   Todo unchanged for 7 days. Act or ask.
3. Report: one comment with what was done and anything I must decide.
```

## Weekly review (recurring, Mondays)

```text
Title: Agent weekly review
Steps: metrics for the last 7 days; classify my corrections by root cause;
fix at most 3 causes, each in one place; log each fix; check due change-log
rows (keep / revert / rewrite / defer); post a project update.
```

## Skill review (recurring, weekly)

```text
Title: Skill review
Steps: evidence from the week's sessions; decide create / update / merge /
split / retire for each candidate; execute; log; report; sync the repository.
```

## Monthly workflow review (recurring, 1st of the month)

```text
Title: Monthly workflow review
For each routine, template and rule: why it exists, who uses it for what,
whether something else already covers it, and what to delete or simplify.
```

## Research radar (recurring, every 2 weeks)

```text
Title: Research radar
Find new external methods for agent-run work. Check each against our own
evidence. Propose at most a few experiments, one per round.
```

## Correction retro

```text
Title: Correction retro: <what went wrong>
What I corrected:
Root cause: missing context | wrong rule | tool failure | wrong judgment
The one place to fix it:
Expected effect and check date:
Undo:
```

## Workflow improvement

```text
Title: Workflow improvement: <topic>
Purpose: why this workflow exists
Users and jobs: who uses it for what, with evidence
What already meets the need:
Smallest change (or "no change" / "remove it"):
```

## Project sync (recurring, weekly per project)

```text
Title: Project sync: <project>
Bring the project's entry page current: what happened since the last update
(dated), what is next (dated), and a short metrics snapshot if relevant.
Post a status update with a health value.
```
