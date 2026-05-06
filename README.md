# Cellular Biophysics and Modeling - Online Materials

This repository now uses Jekyll so the course site can be edited as Markdown
instead of generated HTML.

## Editing

- Course pages live in `docs/_materials/`.
- Course updates live in `docs/_posts/`.
- Site layouts live in `docs/_layouts/`.
- CSS and JavaScript live in `docs/assets/`.
- Uploaded PDFs and media remain in `docs/wp-content/uploads/`.

Edit the Markdown files and push to `main`. The GitHub Actions workflow in
`.github/workflows/jekyll.yml` builds the Jekyll site and deploys it to GitHub
Pages.

## Local Preview

If Ruby dependencies are installed locally, preferably with Ruby 3.x:

```sh
cd docs
bundle config --local path vendor/bundle
bundle install
bundle exec jekyll serve
```

Then open the local URL printed by Jekyll.

## Migration Helper

`tools/convert_static_html_to_jekyll.py` was used for the one-time conversion
from the generated HTML export into Markdown source files.
