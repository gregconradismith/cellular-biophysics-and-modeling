# Repository Instructions

This repository publishes a Jekyll static site from `docs/` via the GitHub
Actions workflow in `.github/workflows/jekyll.yml`.

Do not build or serve the Jekyll site locally unless the user explicitly asks
for a local build or preview. Normal validation for site edits should be limited
to inspecting changed files and checking Git state. The production build happens
when changes are pushed to `main`.

## Codex Coordination

At the start of work, read `.codex/handoff.md` and any other Markdown files in
`.codex/` that are relevant to the task. Before ending a session that made
meaningful progress, update `.codex/handoff.md` with the current state, changes,
verification, remaining work, and blockers. Record durable decisions in
`.codex/decisions.md` and concise activity history in `.codex/task-log.md` when
those files are useful.
