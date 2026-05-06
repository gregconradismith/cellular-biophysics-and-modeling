# Cellular Biophysics and Modeling - Online Materials

This repository contains a WordPress export and a generated static version of the
course materials.

## Static site

Open `docs/index.html` in a browser to browse the presentable version of the
materials. The site includes:

- A course landing page
- Static pages for lectures, readings, slides, videos, syllabus, calendar, and
  other course materials
- A course updates archive generated from WordPress posts
- Lightweight filtering on the page and post index views

Media and PDF links still point to the original WordPress upload URLs; the export
contains references to those files, not the file contents themselves.

## Regenerate

```sh
sage -python tools/build_static_site.py
```

The generator reads `cellularbiophysicsandmodeling.WordPress.2026-05-05.xml` and
rewrites `docs/`.
