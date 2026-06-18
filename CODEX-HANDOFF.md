# Codex Handoff

Date: 2026-06-18

Repo: `cellular-biophysics-and-modeling`

Branch: `main`

Current Git status at handoff creation:

```bash
## main...origin/main
```

## Repository Role

This repository publishes the online materials for Cellular Biophysics and
Modeling:

https://gregconradismith.github.io/cellular-biophysics-and-modeling/

The editable source lives under `docs/`. GitHub Actions builds and deploys the
Jekyll site after changes are pushed to `main`.

## High-Value Context

- Read root `AGENTS.md` before editing. It says not to build or serve Jekyll
  locally unless Greg explicitly asks.
- `docs/HANDOFF.md` contains the detailed course-site continuation state,
  including the current post-review batch and Greg's preferred commit/push
  workflow.
- Course pages live in `docs/_materials/`.
- Course updates/posts live in `docs/_posts/`.
- Shared rendering is in `docs/_layouts/`.
- CSS, JavaScript, search data, and site assets live in `docs/assets/`.
- The GitHub Pages workflow is `.github/workflows/jekyll.yml`.
- Lecture previous/next navigation is centralized in
  `docs/_layouts/page.html` and uses `lecture_rank` front matter.

## Useful Commands

Check status:

```bash
git status --short --branch
```

Check whitespace in the scoped diff:

```bash
git diff --check
```

Inspect the GitHub Pages workflow:

```bash
sed -n '1,220p' .github/workflows/jekyll.yml
```

## Notes For The Next Codex

- Do not run a local Jekyll build or server unless Greg explicitly requests it.
- Normal validation is changed-file inspection plus Git state.
- After modifying this repo, commit and push to `main`.
- When course-post review resumes, use `docs/HANDOFF.md` as the source of truth
  for the current batch and the A/B/C/D decision workflow.
- Keep source edits in Markdown and shared layouts rather than generated HTML.
- Avoid committing local noise such as `.DS_Store`, `_site/`, `.jekyll-cache/`,
  temporary exports, or unrelated generated artifacts.
