# Improvement loop

The system changes itself every week, but every change is treated as a
hypothesis with a check date and an undo.

## Weekly review

1. **Metrics** for the last seven days, from a script over the tracker:
   - owner interventions per delivered result (the north-star metric);
   - proactive deliveries (results nobody asked for);
   - rework rate (issues reopened or failed checks);
   - orchestration overhead (owner comments that only steer agents);
   - execution failures (dropped runs, failed writes);
   - owner interventions inside the agents' own project (target zero);
   - draft quality: share sent unchanged, median draft-to-sent similarity.
   Correct keyword-based counts by hand and report raw and corrected numbers.
2. **Classify every correction** from the owner by root cause: missing
   context, wrong rule, tool failure, or wrong judgment.
3. **Fix the top causes**, at most three, each in exactly one place: a memory
   page, a skill or a template.
4. **Log each fix** in the change log (below), in the same commit.
5. **Check earlier changes** that are due: keep, revert, rewrite or defer
   (once) with one line of evidence. A revert happens in the same run.
6. **Report** as a project update: metrics next to last week's, causes,
   fixes, change-log results, autonomy changes, and anything the owner must
   decide.

## Change log

Every change an agent makes to its own rules, skills, routines, templates or
tracker settings gets one row:

| Column | Content |
| --- | --- |
| ID | Continuous number. Re-read the maximum right before appending; parallel sessions append too. |
| Date | Date of the change. |
| Change | What changed, where, and the commit or object ID. |
| Basis | The corrections or incidents that caused it. |
| Expected effect | One metric and its direction, observable within a week where possible. |
| Undo | The exact revert command or steps. Snapshot templates before editing them. |
| Check date | The first weekly review at least four days later. |
| Result | Empty until checked; then keep, reverted, rewritten or deferred. |

## Monthly workflow review

Once a month, review the workflow itself from purpose down: what each routine,
template and rule is for, who uses it, whether it is still needed, and what to
delete. Use the simplify-before-automate order.

## Research radar

Every two weeks, an agent researches new external methods for agent-run work
(products, papers, practices), checks each against the current system's
evidence, and proposes at most a few experiments, one per round.

## Experiments

Run one process experiment at a time, with a written hypothesis, a metric,
and a review date. Example: let the cloud assistant shadow a signal source for
a week and compare its coverage and latency before moving ownership.
