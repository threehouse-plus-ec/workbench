# Workbench

Essay drafting and Breakwater analysis workspace for T(h)reehouse +EC.

**Endorsement Marker:** Local candidate framework — T(h)reehouse +EC stewardship. No external endorsement implied.

## How it works

Each topic lives in its own folder with three sub-layers:

```
topic-name/
├── breakwater/    ← Claim Analysis Ledger entries
├── references/    ← Source notes, evidence, data
└── essay/         ← Sail drafts, commentary
```

Every `.md` file in a topic folder is automatically rendered into a minimalist web page on push to `main`, published via GitHub Pages. The design follows the [T(h)reehouse +EC corporate design blueprint](https://github.com/threehouse-plus-ec/cd-rules).

## Mobile-first workflow

This repo is designed to work entirely from an iOS device:

1. Open the **GitHub mobile app** (or Working Copy)
2. Create or edit `.md` files directly
3. Commit to `main`
4. GitHub Actions builds and deploys automatically
5. View the rendered pages at the GitHub Pages URL

## Starting a new topic

Copy files from `_templates/` into a new topic folder:

```
my-new-topic/
├── breakwater/
│   └── CL-YYYY-NNN.md     (from breakwater-entry.md)
├── references/
│   └── ref-001.md          (from reference-note.md)
└── essay/
    └── draft.md            (from essay-draft.md)
```

## Methodology

See [BLUEPRINT.md](BLUEPRINT.md) for the Breakwater + Essay methodology.

## Corporate design

Assets are pulled from `threehouse-plus-ec/cd-rules` at build time (Model B: distributed copy with checksum). The build script fetches `tokens.css`, emblem SVGs, and wordmark SVGs from the cd-rules repo at the commit recorded in `assets/SOURCE.md`.

## Licence

Split architecture per the T(h)reehouse +EC blueprint:
- Page chrome, build scripts, CSS: MIT
- Authored content (essays, breakwater entries): CC BY-NC-SA 4.0

See per-folder LICENCE files.

---

*T(h)reehouse +EC. The emblem is the seed; the network is its recursive unfolding.*
