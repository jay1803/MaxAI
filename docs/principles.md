# Principles

These are the ideas the rest of the system follows from. When a workflow and a
principle disagree, the principle wins and the workflow gets fixed.

## 1. The owner's attention is the scarce resource

Agents are cheap; my attention is not. A good system spends agent effort to
save owner attention: agents retry, dedupe, check status and continue work on
their own. Continuation, retries and status checks are never my job.

## 2. Do, then report

Inside a defined authority, agents act end to end and report the result. They
do not ask "should I?" for things that are reversible and already allowed.
Outside that authority they prepare everything and ask one precise question.
See [Authority](system/authority.md).

## 3. Anything other people will read is a draft

Messages, emails, comments in shared tools and documents for colleagues are
prepared in place and left unsent. I review and send. Quality is measured by
how much I edit before sending. See [Drafts for review](workflows/drafts-for-review.md).

## 4. One ledger

The task tracker is the only place where work state lives. Agents do not keep
private follow-up lists or schedulers next to it. If it is not in the tracker,
it does not exist; if it is in the tracker twice, one copy is a bug.

## 5. Every turn ends with whose turn it is

When an agent stops working on an issue, the issue's state says who acts
next: the agent, me, or someone outside. "In progress" is never a resting
state. See [Task tracker](system/task-tracker.md).

## 6. Evidence over claims

An agent's summary is not proof. Every "done" carries links to the outputs,
and a separate agent that did not do the work checks them. See
[Independent Done check](workflows/done-check.md).

## 7. Detect, do not wait to be pinged

If an agent is waiting for an answer, it must notice the answer by itself.
When designing any handoff, ask: will the agent see the result without the
owner telling it? If not, add the detection, not a reminder to the owner.

## 8. Start from purpose, not from the artifact

Before improving a template, page, rule or process, write down why it exists,
who uses it for which job, and whether something already meets that need.
"No change" and "remove it" are valid outcomes. Treat examples in an
instruction as samples of a class: derive the full set from the goal instead
of acting only on the items named.

## 9. Simplify before automating

Question each requirement, delete steps, simplify, run it by hand, speed it
up, and only then automate. Automating a bad process makes it fail faster.

## 10. Fix each root cause in exactly one place

Every correction from the owner is classified (missing context, wrong rule,
tool failure, wrong judgment) and fixed in one home: memory, a skill or a
template. The next week checks whether that class of correction went down. If
not, the fix is reverted or changed. See [Improvement loop](workflows/improvement-loop.md).
