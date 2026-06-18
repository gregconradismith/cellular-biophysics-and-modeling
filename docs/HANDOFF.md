# Handoff

Repository path:

`/Users/gregconradismith/Library/CloudStorage/Dropbox/Main/Git/cellular-biophysics-and-modeling/docs`

This Jekyll site is published from `docs/` by the GitHub Actions workflow in `.github/workflows/jekyll.yml`.

Do not build or serve the site locally unless Greg explicitly asks. Normal validation is changed-file inspection plus `git status`. Production HTML is created by GitHub Actions after pushing to `main`.

## User Workflow Preference

- Commit and push to `main` after every modification.
- Explicitly say after each push: `I committed and pushed to main: <hash> <message>`.
- For post review, use batches of 3 with lettered options.
- Default posture for posts: delete stale logistics posts, but keep posts that could help this year's students after making them year/semester agnostic.

## Current Git State

As of this handoff, `main` was clean and even with `origin/main` before creating this file.

Most recent pushed commits:

- `9df5a3d Retain reusable dynamics resources`
- `b7c4625 Delete stale exam logistics posts`
- `7ea1cc6 Make reusable course guidance posts agnostic`
- `bf2d403 Delete stale introductory posts`
- `fb87093 Add course philosophy page`
- `7e5f1b0 Delete blog access and office hours posts`

## Completed Site Work

- Added Calendar page at `/pages/calendar/`.
- Organized menu as course pages and later added About and Philosophy.
- Created Fall 2026 calendar with every Tuesday/Thursday class date, weeks, units, no-class dates, and lectures in order.
- Updated Calendar formatting so dates and lectures are separate, week separators indicate weekends, and lecture number is a suffix/label as requested.
- Redesigned the home page:
  - Removed redundant top header on home.
  - Made a conventional banner from the main image.
  - Removed "View overview" and "Browse materials" buttons.
  - Added large centered buttons.
  - Added Recent posts list at bottom.
- Added About page and home button.
- Added Philosophy page and menu/home button:
  - URL: `https://gregconradismith.github.io/cellular-biophysics-and-modeling/pages/philosophy/`
  - Includes prominent firewood quote.
- Changed `Lecture X1` to `Lecture 22`.

## Post Review Status

The user has been reviewing stale posts in batches of 3. The current remaining posts are:

- `_posts/2025-09-05-questions-about-problem-set-1.md`
- `_posts/2025-09-05-will-exam-questions-be-similar-to-homework-questions.md`
- `_posts/2025-09-06-generative-ai-course-policy.md`
- `_posts/2025-10-16-rt-romeo-jt-juliet-dynamic-models-of-love-affairs.md`
- `_posts/2025-10-21-problem-set-3-is-due-thursday-october-23-helpful-videos.md`
- `_posts/2025-10-24-the-sign-of-beta-in-quadratic-formula.md`
- `_posts/2025-11-11-what-does-increased-iapp-raise-the-voltage-nullcline.md`
- `_posts/2025-11-12-important-currents.md`
- `_posts/2025-11-13-final-exam-example-questions.md`

Already made reusable:

- `2025-09-05-questions-about-problem-set-1.md`
- `2025-09-05-will-exam-questions-be-similar-to-homework-questions.md`
- `2025-09-06-generative-ai-course-policy.md`
- `2025-10-16-rt-romeo-jt-juliet-dynamic-models-of-love-affairs.md`
- `2025-10-21-problem-set-3-is-due-thursday-october-23-helpful-videos.md`

## Resume Point

The next unresolved batch was presented to Greg as:

A. Keep all three, lightly clean them into reusable concept posts.

B. Keep only the Iapp/nullcline post and beta-sign post; delete Important Currents.

C. Keep only the Iapp/nullcline post; delete the other two.

D. Delete all three.

Those three files are:

- `_posts/2025-10-24-the-sign-of-beta-in-quadratic-formula.md`
- `_posts/2025-11-11-what-does-increased-iapp-raise-the-voltage-nullcline.md`
- `_posts/2025-11-12-important-currents.md`

Greg has not answered that batch yet.

## Likely Next Step

Ask Greg to choose A/B/C/D for the batch above. After applying the decision:

1. Inspect changed files and `git status`.
2. Commit.
3. Push to `main`.
4. Say explicitly: `I committed and pushed to main: <hash> <message>`.
5. Present the next batch, which should include:
   - `_posts/2025-11-13-final-exam-example-questions.md`
   - Any remaining unreviewed posts, if there are enough for a batch.

