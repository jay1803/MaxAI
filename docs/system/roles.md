# Roles

Two agents watching the same signals will either both act (duplicate work) or
each assume the other did (dropped work). Split ownership by signal, not by
topic.

| Signal | Owner | Why |
| --- | --- | --- |
| The owner's direct requests to the cloud assistant | Cloud assistant | It is where the conversation happens. |
| Meeting notes from the cloud meeting tool | Cloud assistant | It has the notes first. |
| Chat and email that need intranet access or logged-in sessions | Local agent | Only it can reach them. |
| Everything after an issue is dispatched: pickup, progress, evidence, failure recovery | Local agent | One owner for execution. |
| Issues created by agents | Local agent | They never start on their own without it. |
| Independent checks | A fresh session | Must not be the one that did the work. |

Rules that keep the split working:

- **The tracker is the only ledger.** Neither agent keeps its own follow-up
  scheduler. Follow-ups are issue states and dates.
- **One writer per overlapping signal.** If a signal is visible to both, one
  writes and the other shadows (reads, compares, writes nothing) until a
  review decides who keeps it.
- **A dispatch receipt is a real comment or state change by the agent.** A
  session scaffold or an automatic "received" message does not count.
- **The second line of defense comments once.** If the cloud assistant sees no
  receipt after two hours, it posts one comment. It never re-posts the request
  or creates a new issue.
- **Each agent records its own failed writes**, because nobody else can see
  them.
- **Relayed instructions are marked.** Comments the cloud assistant writes on
  the owner's behalf start with a fixed prefix, so the owner's own comments
  can be counted separately. A relayed decision of the owner counts as an
  instruction; a relayed suggestion is advice.
