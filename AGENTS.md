# Repository Instructions

This repository publishes a Jekyll static site from `docs/` via the GitHub
Actions workflow in `.github/workflows/jekyll.yml`.

Do not build or serve the Jekyll site locally unless the user explicitly asks
for a local build or preview. Normal validation for site edits should be limited
to inspecting changed files and checking Git state. The production build happens
when changes are pushed to `main`.
