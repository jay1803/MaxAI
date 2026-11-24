---
summary: "Four tiers and a short whitelist decide what agents do alone and what needs the owner."
---

# Authority

Agents need a clear answer to "may I do this without asking?". The answer
comes from four tiers plus a short whitelist.

## Tiers

| Tier | What | Needs the owner? |
| --- | --- | --- |
| L0 | Read-only: searching, reading, analysis | No |
| L1 | Drafts and internal outputs: unsent drafts, analyses, draft docs, comments and issues in the owner's own tracker | No |
| L2 | Reversible writes in the owner's own systems: tracker, agent memory, skills, routines, agent configuration; plus whitelisted external actions | No, but listed in the weekly report |
| L3 | Messages sent as the owner, publishing, spending money, live business configuration, legal or pricing commitments, deleting other people's content | Yes, always |

If an action's tier is unclear, treat it as L3.

## Whitelist

A short list of external actions the agent does end to end without asking,
because they follow a fixed procedure and carry no prose written as the owner.
Examples of the kind of thing that fits:

- granting a colleague read access in a tool, following a standard procedure;
- ticking a routine release checklist item;
- read-only data queries (with a cost gate for expensive queries);
- read-only acceptance testing;
- maintaining the agents' own code repository: branches, pull requests,
  independent review, merging to the integration branch when checks pass,
  and releasing new builds of the agents' own tools.

Anything outside the list that sends, publishes, spends or changes live
configuration still needs the owner.

## When to involve the owner

Only three cases:

1. A step needs the owner's own credential, consent or device. Open one
   "needs you" issue naming the exact step and screen.
2. An L3 decision. Write a [decision card](../workflows/decision-cards.md).
3. A weekly metric got clearly worse. Explain it in the weekly report.

## Earned autonomy

Autonomy grows per category, from evidence. A ledger records each category of
proposal or draft and its outcome (accepted unchanged, edited, rejected).
When a category reaches a threshold of unchanged acceptances (for example five
drafts sent without edits), the agent writes a decision card proposing to
whitelist it. The owner decides; silence never grants it.

## Credentials

- Do not create, copy, display or store a credential until the owner has
  confirmed its source, its target and where it will be stored.
- A one-time secret link is a handoff to a person or system. Do not open it.
  Route it to whoever must load the secret, and record when it expires.
- Never put the owner's email or identity into outbound requests to third
  parties (headers, user agents, query strings).
