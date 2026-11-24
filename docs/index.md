# How I work with AI agents

I am one person doing product work. Most of the doing is done by AI agents:
they collect what people ask of me, do the work they are allowed to do, prepare
drafts for what they are not, and bring me only the decisions that need me.
This site describes that system so that you can build the same thing with your
own tools.

## The model in one paragraph

Every piece of work is an issue in one task tracker. Agents find new work in
chat, email and stalled issues several times a day, and create or update
issues for it. For each issue an agent either does the work end to end (when
the action is inside its authority), writes a decision card for me (when my
judgment is needed), or tracks it (when someone else owns it). Anything other
people will read is left as an unsent draft for me. Every issue ends each turn
in a state that says whose turn it is. A separate agent checks every issue an
agent closed. Once a week the agents read my corrections, find the root cause
of each one, and fix it in exactly one place.

```mermaid
flowchart TB
  S[Signals: chat, email, meetings, stalled issues] --> C[Collector agents]
  C --> T[(Task tracker: one issue per deliverable)]
  T --> E[Executing agent]
  E -->|inside authority| D[Done + evidence]
  E -->|needs judgment| K[Decision card for the owner]
  E -->|others will read it| R[Unsent draft for the owner]
  D --> V[Independent check by a fresh agent]
  K --> O((Owner))
  R --> O
  O -->|reply, click, edit| T
  V --> W[Weekly review of corrections]
  W -->|one fix per root cause| Rules[Rules, skills, templates]
  Rules --> E
```

## What to read

- [Principles](principles.md): the few ideas everything else follows from.
- [Getting started](getting-started.md): the smallest version you can run this
  week.
- [System](system/index.md): components, roles, authority tiers and the task
  tracker setup.
- [Workflows](workflows/index.md): intake, execution, decisions, drafts,
  checks, planning and the improvement loop.
- [Knowledge](knowledge/index.md): how agents remember, how skills are made,
  and the writing rules.
- [Templates](starter-kit/index.md): files you can copy.
- [Lessons learned](lessons.md): failure modes that each cost real time.

## The measure of success

The main metric is **my interventions per delivered result**: how many times I
had to step in (correct, retry, remind, re-explain) for each thing the agents
delivered. It is read together with the number of results the agents
delivered on their own initiative, so that doing less never counts as
progress.
