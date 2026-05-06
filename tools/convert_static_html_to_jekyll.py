#!/usr/bin/env python3
"""One-time migration from generated HTML pages to editable Jekyll Markdown."""

from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MATERIALS = DOCS / "_materials"
POSTS = DOCS / "_posts"
SEARCH_INDEX = DOCS / "assets" / "search-index.json"


ARTICLE_RE = re.compile(
    r'<article class="content-page">.*?'
    r'<div class="page-kicker">(?P<kicker>.*?)</div>.*?'
    r"<h1>(?P<title>.*?)</h1>\s*"
    r'<div class="wp-content">\n(?P<body>.*?)\n      </div>\s*</article>',
    re.DOTALL,
)


def strip_tags(value: str) -> str:
    value = re.sub(r"(?is)<script.*?</script>", " ", value)
    value = re.sub(r"(?is)<style.*?</style>", " ", value)
    value = re.sub(r"(?s)<!--.*?-->", " ", value)
    value = re.sub(r"(?s)<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def yaml_scalar(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def html_to_markdown(value: str) -> str:
    value = re.sub(r"(?s)<!--\s*/?wp:.*?-->\s*", "", value).strip()
    if not value:
        return ""
    if re.search(r"(?is)<iframe\b", value):
        return value

    result = subprocess.run(
        ["pandoc", "--from=html", "--to=gfm+raw_html", "--wrap=none"],
        input=value,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        return value
    return result.stdout.strip()


def load_metadata() -> dict[str, dict[str, str]]:
    if not SEARCH_INDEX.exists():
        return {}
    try:
        entries = json.loads(SEARCH_INDEX.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return {entry["url"].strip("/"): entry for entry in entries}


def lecture_rank(slug: str) -> int | None:
    exact = re.fullmatch(r"lecture-(\d+)", slug)
    if exact:
        return int(exact.group(1)) * 10
    prefixed = re.match(r"lecture-(\d+)", slug)
    if prefixed:
        return int(prefixed.group(1)) * 10 + 1
    if re.fullmatch(r"lecture-x\d+", slug):
        return 900 + int(slug.rsplit("x", 1)[1])
    return None


def front_matter(fields: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if value is None:
            continue
        lines.append(f"{key}: {yaml_scalar(value)}")
    lines.append("---")
    return "\n".join(lines)


def extract(path: Path, kind: str, metadata: dict[str, dict[str, str]]) -> tuple[Path, str]:
    slug = path.parent.name
    raw = path.read_text(encoding="utf-8")
    match = ARTICLE_RE.search(raw)
    if not match:
        raise ValueError(f"Could not extract article content from {path}")

    title = strip_tags(match.group("title"))
    url = f"{'posts' if kind == 'post' else 'pages'}/{slug}"
    entry_meta = metadata.get(url, {})
    date = entry_meta.get("date") or date_from_kicker(match.group("kicker")) or "1970-01-01"
    body = html_to_markdown(match.group("body"))

    fields: dict[str, object] = {
        "title": title,
        "kind": kind,
        "date": date,
        "slug": slug,
        "permalink": f"/{url}/",
        "render_with_liquid": False,
    }

    rank = lecture_rank(slug)
    if rank is not None:
        fields["lecture_rank"] = rank

    if kind == "post":
        target = POSTS / f"{date}-{slug}.md"
    else:
        target = MATERIALS / f"{slug}.md"

    return target, f"{front_matter(fields)}\n\n{body}\n"


def date_from_kicker(value: str) -> str | None:
    text = strip_tags(value).replace("·", " ")
    match = re.search(r"([A-Z][a-z]{2})\s+(\d{1,2}),\s+(\d{4})", text)
    if not match:
        return None
    try:
        return datetime.strptime(match.group(0), "%b %d, %Y").strftime("%Y-%m-%d")
    except ValueError:
        return None


def main() -> None:
    metadata = load_metadata()
    converted: list[tuple[Path, str]] = []
    for path in sorted((DOCS / "pages").glob("*/index.html")):
        converted.append(extract(path, "page", metadata))
    for path in sorted((DOCS / "posts").glob("*/index.html")):
        converted.append(extract(path, "post", metadata))

    for directory in (DOCS / "pages", DOCS / "posts", MATERIALS, POSTS):
        if directory.exists():
            shutil.rmtree(directory)
    if (DOCS / "index.html").exists():
        (DOCS / "index.html").unlink()

    MATERIALS.mkdir(parents=True, exist_ok=True)
    POSTS.mkdir(parents=True, exist_ok=True)
    for target, content in converted:
        target.write_text(content, encoding="utf-8")

    print(f"Converted {len(converted)} generated HTML entries to Jekyll Markdown.")


if __name__ == "__main__":
    main()
