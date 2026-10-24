# Codex Handoff

Date: 2026-08-22

Repo: `cellular-biophysics-and-modeling`

Branch: `main`

## Blackboard Course

- Fall 2026 NSCI 351 Blackboard Ultra course:
  <https://blackboard.wm.edu/ultra/courses/_40085_1/outline>
- Blackboard course identifier: `_40085_1`.
- The canonical entry point requires the `/outline` suffix. The shorter course
  URL did not open the authenticated course correctly in the built-in browser.
- Use the Blackboard course as the roster-aware notification layer for
  announcements published on the public course website. A preferred workflow
  is to publish the full post on the website, then create a concise Blackboard
  announcement with the essential information, a link to the website post,
  and an email copy to course members.
- The user handles W&M authentication and MFA. Before Codex posts an
  announcement or sends an email copy, request confirmation at the final
  submission step.

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

## 2026-10-10 Evergreen Resource Review

- Greg requested a review and recommendations, not implementation, to make the public site a semester-independent resource organized by lecture.
- Reviewed the live public home page, local materials/layouts/posts, and authenticated Fall 2026 Blackboard outline and lecture documents 1–21.
- Recommend removing public announcements and calendar/course logistics, preserving reusable concept posts within lectures, replacing year-based resource sections with topic-based sections, and consolidating empty/duplicate indexes.
- Blackboard includes additional resources absent from public source: Lecture 4 GHK spreadsheets and supplemental readings; Lecture 7 Cervera reading; Lecture 9 browser HH simulations; Lecture 11 recording, Van der Pol examples, and updated pplane links.
- Main lecture topics agree through 21; the separate Slides index is stale, older year-based materials belong to different topic numbers, and public Lecture 22 (basal ganglia) is additional.
- Blackboard homework answer documents and exam practice resources require a resource mapping. Homework 4 answers, later homework, and lectures 15–21 are currently hidden; visibility must not be mistaken for public redistribution permission.
- Existing private GitHub companion links require separate repository access; prefer publisher/DOI/open versions plus clearly labeled restricted Blackboard links where appropriate.
- Review was of document contents and attachment labels, not a binary-file or redistribution-rights audit. No public website or Blackboard content changed. No local Jekyll build run.
- Next step: agree on structure, then inventory and map each reusable Blackboard resource to its evergreen lecture and confirm public versus restricted hosting.

## 2026-10-10 Evergreen collection implementation

- User authorized the reorganization and explicitly declined compatibility for old bookmarks. Deleted calendars, announcement posts/index, syllabus logistics, office-hours page, and empty indexes without redirects.
- Added common resource navigation, 22 topic-labeled lectures in three substantive units, practice/solutions index, models/games page, bibliography, and evergreen About/study guidance.
- Retained reusable post content within relevant lectures and topic-matched supplementary material. Added public Blackboard-linked tutorials/simulators. The inspected Unit 2 whiteboard is hosted as a public repository image, explicitly authorized by the user after automatic review initially rejected copying it.
- Cataloged released Blackboard lecture documents 1–14; linked homework 1–4, solutions 1–3, and practice exams. Hidden future assessments/solutions were not newly exposed. Restricted PDFs remain in the private companion with access labels; publication exclusions unchanged.
- Validation: YAML front matter and data JSON parse, 22 lectures present, local page/asset links resolve, and git diff --check passes. No local Jekyll build performed. Production deployment is checked after push.

## 2026-10-10 Remove Blackboard-dependent resources

- User requested About first in navigation and removal of every link/section requiring Blackboard access.
- Reordered shared navigation; removed lecture file catalogs, homework/solution links, practice-exam sections, their data/includes, and Blackboard-specific access prose. Practice retains interactive tools and references to supplementary lecture exercises.
- Private GitHub PDF companion and publisher/library links are retained: these do not require Blackboard. The public Unit 2 whiteboard remains hosted in this repository.
- Validation: source inspection, link/reference search, YAML/JSON parsing, and git diff --check; no local Jekyll build. Commit/push and production build verification follow.

## 2026-10-15 Morris–Lecar simulator link

- Added the public Morris–Lecar Simulator to the Models & Games page button list (`docs/_materials/games.md`), originally linking to the standalone app (repository identifier `gregconradismith/morris-lecar-simulator`; source commit `eea0175ccea0322eb775d388e1f50ad2160a7b1b`). The current destination is https://gregconradismith.github.io/simulations/morris-lecar-simulator/.
- Validation: inspected the scoped source diff and ran `git diff --check`; no local Jekyll build, following `AGENTS.md`. Publication uses the existing GitHub Actions workflow after pushing main.


## 2026-10-24 Academic simulation destinations

- Updated all seven standalone simulation links in `docs/_materials/games.md` and `docs/_materials/practice.md` to the verified copies under the academic site’s `/simulations/` directory: PolyQual, current–voltage relations, voltage clamp, and Morris–Lecar.
- Preserved the historical Morris–Lecar addition above with a non-hyperlinked repository identifier and immutable source commit; its live destination now points to the academic copy.
- Read repository instructions and inspected Markdown/HTML and existing deployment generation. No local Jekyll build or server per AGENTS.md. `git diff --check` passed; deployment and public link checks follow the authorized main push.
