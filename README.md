# MaxAI: how I work with AI agents

This repository documents how one person runs day-to-day product work with a
small team of AI agents: what the agents do on their own, what they hand back,
how work is tracked, and how the system improves itself every week.

The goal is replication. Everything here is written so that another person can
set up the same way of working with their own tools and accounts. Personal
data, employer data and anything that only works in one private setup are left
out on purpose.

The content is published as a website from `docs/` with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Until the site
is live, read the Markdown files directly, starting at
[`docs/index.md`](docs/index.md).

## Layout

| Path | What it holds |
| --- | --- |
| `docs/` | The website content. One page per topic. |
| `docs/system/` | The parts of the system: components, roles, authority, task tracker. |
| `docs/workflows/` | The recurring workflows, step by step. |
| `docs/knowledge/` | Memory, skills and writing rules. |
| `docs/starter-kit/` | Copy-ready templates: agent rules file, issue templates, routine prompts. |
| `scripts/check_public.py` | Public-safety check run on every pull request. |
| `mkdocs.yml` | Site configuration and navigation. |
| `AGENTS.md`, `.agents/` | Rules for agents that edit this repository. |

## Preview the site locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
```

## Contributing

All changes arrive as pull requests. Nobody commits to `main` directly.
See [CONTRIBUTING.md](CONTRIBUTING.md).
