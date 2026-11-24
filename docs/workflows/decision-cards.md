# Decision cards

A decision card asks the owner for exactly one judgment, with everything
needed to answer in one click.

## Format

Title: `[Decision] <the question in one sentence>`. State In Review, label
`decision`, due date = deadline. The description has these fields, one per
line, in this order, so a script can read them:

```text
Question: what the owner must decide, in one sentence
Level: L1-L2 (internal, reversible) or L3 (external or irreversible)
Evidence: source links and the key facts
Recommendation: what the agent recommends and why
Default: the exact writes that happen if there is no reply by the deadline
          (for L3: "none, not carried out by silence")
Undo: how to reverse the default once carried out (required for L1-L2)
Deadline: YYYY-MM-DD
How to reply: pick an option in the session, or comment "agree" or your change
```

Rules:

- **Level** is L1-L2 only when every step of the default is L0 to L2. If
  unsure, L3. A card with no readable level is treated as L3.
- **Default** names the exact writes (which issues, which fields, which
  values). "Follow the recommendation" is not enough.
- **Deadline** defaults to three working days after creation.
- Do not write a card when there is no real preference question. Just do the
  work.

## One-click answers

After creating the card, the agent opens a session on it that shows the
question as two or three options, the recommendation first. Each option's
description states its concrete content. The owner clicks one; the session
continues with that choice, applies it exactly, reads back every write, posts
one comment whose first line says what was chosen, and sets the state.

A reply in a comment works the same way. The reply watch picks it up without a
mention.

## Silence default

Once a day, a check lists cards past their deadline:

- **L1-L2, no reply**: re-read the card and comments (a reply may just have
  landed), close any open question session, re-check that every step of the
  default is still L0 to L2, carry out exactly the default, read back every
  write, comment `[Silence default] carried out` with each write, the undo
  method and that the owner may reply at any time to reverse it. Add label
  `silence-default` and set Done.
- **Answered**: never run the default. If the owner asked a question instead
  of deciding, answer it and reset the deadline with a comment.
- **L3 past deadline**: leave it In Review and list it in the daily and weekly
  reports. Never carry it out.
- **Invalid**: fix the missing field; a new deadline counts from the fix.

A reply from the owner always wins, at any time, including after the default
ran: undo it, then apply the reply.
