---
summary: "Reusable procedures in folders. When to create one, how families work, and the weekly review."
---

# Skills

A skill is a reusable procedure in a folder: a `SKILL.md` with a name, a
description that says when to use it, and the steps, plus optional scripts,
references and templates. Agents load a skill only when its description
matches the task.

## Skill families

Most skills stand alone. When one job is really several kinds of expertise, it
is split into a family with consistent names (`Family: Role`), one
responsibility per member. Families used in this system:

| Family | Members (roles) |
| --- | --- |
| Task Collector | Orchestrator; one collector per source (chat, email, calendar, docs mentions, tracker, rule changes) |
| Task Assistant | Organizer (sole writer of the tracker), Follow Up (drafts and nudges), Planner, Calendar (time blocks on request only) |
| Project | Init (idea to proposal), Bet (go or no-go), Setup (full plan), Delivery Plan, Entry Page, Sources, Update, Rule Change |
| Research | Orchestrator plus specialists: question framing, decision model, hypothesis map, evidence plan, desk research, data analysis, causal analysis, forecasting, user study, synthesis, independent review |
| Docs | Writers for leadership requests, progress updates, results and annual reviews, plus a reviewer |
| Growth | Experiment design, experiment metrics |

Plus single skills for recurring jobs: acceptance testing, simplify before
automate, skill review, learning from external content, giving more context
on a task, meeting preparation, and similar.

## When to create a skill

1. Run the first two steps of simplify-before-automate first: question the
   requirement and delete what is not needed. Many candidate skills disappear
   here.
2. Create a skill when the same procedure has been done by hand at least twice
   and will recur.
3. Prefer updating an existing skill to creating a new one.
4. A periodic freeze (no new skills for a few weeks, only updates, merges and
   retirements) keeps the set from sprawling.

## Writing a skill

- The description carries the trigger phrases, in the languages the owner
  uses. If the description does not match, the skill never loads.
- The body is procedure: steps, checks, failure handling. No history, no
  narrative.
- Shareable skills name no colleagues and no personal paths.
- Validate the frontmatter after every edit.

## Weekly skill review

1. Window: the last seven days of sessions.
2. Evidence: corrections, repeated manual steps, skills that loaded but were
   not followed, skills that never loaded.
3. Judge each candidate: create, update, merge, split, retire, or nothing.
4. Execute every item: repoint references when content moves; before
   retiring, check every routine and skill that links the old one.
5. Log one change-log row per item.
6. Report on the issue and sync the repository.
