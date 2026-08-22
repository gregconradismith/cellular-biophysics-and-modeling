# Codex Handoff

Date: 2026-08-22

Repo: `cellular-biophysics-and-modeling`

Branch: `main`

## 2026-08-22 Fall 2026 Launch Update

- Replaced the stale home-page status, "Next taught in Fall 2026," with the
  active course identification: `NSCI 351: Cellular Biophysics and Modeling`.
- Added the meeting schedule and location to the home page: Tuesdays and
  Thursdays, 2:00–3:20 p.m., Integrated Science Center, Room 0350.
- Updated the existing Fall 2026 status announcement with the same information
  and changed its displayed date to August 22, 2026.
- Added a separate `course_meeting` field to the home-page front matter so the
  logistical details render beneath the course status rather than as one long
  heading.
- Validation was limited to changed-file inspection, `git diff --check`, and
  Git state, as required by `AGENTS.md`; no local Jekyll build was run.
- Replaced all four unspecified calendar meetings with `TBD: Review and/or
  assessment.` and identified the November 24 lecture as a remote-instruction
  day.
- Added Fall 2026 syllabus logistics: NSCI 351; Tuesday/Thursday 2:00–3:20 p.m.
  in ISC 0350; instructor office ISC 0275; TA Sarah Sakly in ISC 0252; and TBD
  office hours for both instructor and TA. Replaced stale Blackboard/blog
  references with course-site terminology.

<!-- codex-transfer-snapshot:start -->
## 2026-06-22 Computer Transfer Snapshot

- Checked on 2026-06-22 from `/Users/greg/Git` before moving computers.
- Ran `git fetch --all --prune`; `main` is tracking `origin/main` unless this status says otherwise.
- Origin: `git@github.com:gregconradismith/cellular-biophysics-and-modeling.git`
- Latest commit at refresh time: `cbdd5ee 2026-06-22 15:46:36 -0400 Add curated material thumbnails`
- On the next machine, read `AGENTS.md` first, then this handoff.
- The working tree was clean before this handoff refresh; after committing the refresh, `git status --short --branch` should again show only the branch line.

Status before this handoff edit:

```bash
## main...origin/main
```
<!-- codex-transfer-snapshot:end -->

Latest pushed commit at handoff: `0072a34 Refine header buttons and philosophy quote`

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

## Recent Site Changes

- `0072a34 Refine header buttons and philosophy quote`
  - Made the top header navigation links read as compact buttons.
  - Increased the header brand text next to the cell image.
  - Changed the Course Philosophy quote to "One who chops their own firewood
    warms themselves twice." and centered the quote text.
- `1d31a06 Refine page alignment and notation`
  - Centered Lectures/Games content and button layouts.
  - Refined Calendar/Syllabus presentation and scientific notation styling.
- `17411de Center calendar headings`
  - Centered Calendar unit/week headings.

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
- Do not commit or push unless Greg asks. When he does, commit and push to
  `main`.
- When course-post review resumes, use `docs/HANDOFF.md` as the source of truth
  for the current batch and the A/B/C/D decision workflow.
- Keep source edits in Markdown and shared layouts rather than generated HTML.
- Avoid committing local noise such as `.DS_Store`, `_site/`, `.jekyll-cache/`,
  temporary exports, or unrelated generated artifacts.
- No local build was run for the latest handoff update.
