# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository overview
This is a simple, static GitHub Pages site (no build pipeline in-repo). The site is primarily a single HTML page styled by a small set of CSS files.

## Common commands
### Preview locally
Serve the repo root with any static file server.

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000/`.

### Tests / lint / build
There are no test, lint, or build scripts configured in this repository.

## High-level structure
### Content + page entrypoint
- `index.html`
  - The site’s main (and effectively only) page.
  - Includes the page header/content and an inline Google Analytics snippet near the bottom.

### Styling
- `stylesheets/stylesheet.css`: primary theme/layout.
- `stylesheets/github-dark.css`, `stylesheets/pygment_trac.css`: styling for code blocks/syntax highlighting.
- `stylesheets/print.css`: print styles.

### JavaScript
- `javascripts/main.js`: currently just a placeholder; there is no meaningful JS behavior wired up.

### Static assets
- `images/`: background and button/icon assets referenced by CSS.

### Legacy GitHub Pages generator metadata
- `params.json`: contains title/tagline/body and a note indicating it is used for “page regeneration” and should not be deleted.

## Notes / conventions
- Git editor preference: use `cursor` as the git editor when an interactive editor is needed (e.g., for commit messages or rebase).