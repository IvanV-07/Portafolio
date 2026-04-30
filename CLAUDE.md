# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Static portfolio template for developers, built with [Reflex](https://reflex.dev) (Python framework that compiles to a Next.js frontend). Pinned to `reflex==0.4.5`. Designed to be exported as static HTML/CSS/JS and deployed to Vercel.

## Commands

Local development (run from repo root, where `rxconfig.py` lives):

```bash
pip install -r requirements.txt
reflex init        # only needed once, after a fresh clone
reflex run         # dev server at http://localhost:3000
```

Static export (what `build.sh` does for Vercel):

```bash
reflex export --frontend-only   # produces frontend.zip
unzip frontend.zip -d public    # Vercel serves from public/ (see vercel.json)
```

There is no test suite, linter, or formatter configured in this repo.

## Architecture

The Reflex app is the `portafolio` package; `rxconfig.py` declares `app_name="portafolio"` so Reflex looks for `portafolio/portafolio.py` as the entry point.

Data flow — content is data-driven, not hardcoded in components:

1. `assets/data/data.json` holds all portfolio content (use `data_template.json` as the schema reference).
2. [portafolio/data.py](portafolio/data.py) loads that JSON at import time and hydrates a tree of plain Python classes (`Data`, `Media`, `Technology`, `Info`, `Extra`). The path `assets/data/data.json` is opened relative to CWD, so commands must be run from the repo root.
3. [portafolio/portafolio.py](portafolio/portafolio.py) imports `data.data` once as `DATA` and passes slices of it (`DATA.about`, `DATA.experience`, ...) into view functions.

Layered UI structure:

- `portafolio/views/` — page sections (`header`, `about`, `tech_stack`, `info`, `extra`, `footer`). Each is a function returning an `rx.Component` that takes its data slice as an argument. The single `info()` view is reused for Experience, Projects, and Formación by passing different lists of `Info` objects plus a section title.
- `portafolio/components/` — small reusable building blocks (`card_detail`, `heading`, `icon_badge`, `icon_button`, `info_detail`, `media`) composed by the views.
- `portafolio/styles/styles.py` — central `MAX_WIDTH`, `EmSize`/`Size` enums, `BASE_STYLE`, and `STYLESHEETS` (Devicon CDN is loaded here for tech-stack icons).

Icon conventions (configured by editing `data.json`):

- General icons: [Lucide](https://lucide.dev/icons/) identifiers (used by `rx.icon`).
- Technology icons: [Devicon](https://devicon.dev/) identifiers (rendered as `<i class="devicon-...">` via the CDN stylesheet).

Theme: `rx.theme(...)` is configured inline in `portafolio.py`. To change it, uncomment `rx.theme_panel()` inside `index()`, run the dev server, pick a theme, click `Copy Theme`, and paste the values back into the `rx.theme(...)` call.

## Deployment

Vercel uses `@vercel/static-build` to run [build.sh](build.sh), which creates a venv, installs deps, runs `reflex export --frontend-only`, and unzips the output into `public/`. [vercel.json](vercel.json) then serves `public/` as static assets. `public/` is gitignored.
