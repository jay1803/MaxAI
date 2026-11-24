---
summary: "The recurring procedures in the order work moves through them, and a typical weekday."
---

# Workflows

The recurring procedures, in the order work moves through them.

| Workflow | When it runs | What it produces |
| --- | --- | --- |
| [Intake](intake.md) | Daily full sweep plus three windows on workdays | New or updated issues |
| [Working an issue](working-an-issue.md) | Whenever an issue is dispatched | A result, a draft, or a decision card |
| [Decision cards](decision-cards.md) | When the owner's judgment is needed | One clickable question with a default |
| [Drafts for review](drafts-for-review.md) | Whenever others will read the output | An unsent draft in place |
| [Independent Done check](done-check.md) | Daily | A pass or fail verdict on each agent-closed issue |
| [Watching for replies](reply-watch.md) | Hourly | Answers picked up without pings; dropped runs resumed |
| [Planning](planning.md) | Daily, weekly, quarterly | Priorities and focus |
| [Agent-written code](coding.md) | Any code change | A reviewed, merged change |
| [Improvement loop](improvement-loop.md) | Weekly and monthly | One fix per root cause, with a check date |

## A typical weekday

| Time | What runs |
| --- | --- |
| 07:00 | Full daily intake sweep over every source since the last run. |
| 09:00 | Intake window: new signals and stalled issues. Daily agent check (Done checks, due decision cards). |
| 09:30 | Recurring-issue watchdog runs instances due today. |
| Hourly, 08:00 to 23:00 | Reply watch. |
| 13:00 | Intake window plus fixing issues that failed their check. Agent repo sync. |
| 15:30 | Watchdog retry. |
| 18:00 | Intake window plus a day-end status pass. |
| 01:00 | Agent repo sync. |
| Monday | Weekly review and weekly plan. |
| Sunday | Skill review. |
| 1st of the month | Monthly workflow review. |
