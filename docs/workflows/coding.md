# Agent-written code

Code the agents depend on (the relay, scripts, tooling) is maintained by the
agents themselves, under a fixed procedure that separates writing from
reviewing.

## Procedure

1. **Worktree**: create a separate Git worktree and branch for the change.
2. **Write**: run the coding agent non-interactively in that worktree with an
   implementer instruction set (read the repository rules, make the smallest
   change, run the checks).
3. **Freeze and review**: a second coding-agent run, read-only, reviews the
   frozen diff. It did not write the code and does not share the writer's
   context.
4. **Fix**: blocking findings are fixed and reviewed again.
5. **Merge**: the agent merges to the integration branch only when checks are
   green and the review has no blocking findings.
6. **Release** (for the agents' own tools): when the integration branch holds
   merged, reviewed changes with green checks, the agent promotes it, builds a
   release with notes, backs up the previous version and its data, checks for
   running sessions that an install would interrupt, installs the verified
   build, and reports.

If the coding agent is unavailable, the main agent may write the code itself,
but the independent review still runs, from a fresh session that did not
write it.

## Repository rules

Each repository has a root rules file (`AGENTS.md`) as the single index,
pointing to optional policies:

| Path | Holds |
| --- | --- |
| `.agents/policies/development.md` | Branches, pull requests, merge authority |
| `.agents/policies/coding.md` | Code and architecture conventions |
| `.agents/policies/validation.md` | Required checks |
| `.agents/policies/skills.md` | Repository-local skills |
| `.agents/policies/release.yaml` | Who may promote to production |
| `.agents/runbooks/release.md` | Release procedure |

Missing guidance never grants merge, release, deployment or deletion
authority. This repository itself follows the same layout.
