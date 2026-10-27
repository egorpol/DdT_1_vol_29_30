# Changelog

All notable changes to this edition are recorded here. Version numbers will follow the [encoding profile](docs/mei-encoding-profile.md#release-identity-versions-and-citation) once a release is prepared: patch releases for compatible corrections or metadata fixes that keep event IDs, minor releases for added works or coverage, and major releases for changes to event identity, segmentation or analytical interpretation. Musical corrections are listed even when the version step is small.

## [Unreleased]

### Added

- Validation layer ported from DdT 1 vol. 11: `scripts/validate_corpus.py`, editorial-report refresh, CAMAT update helper, `validation/` profile and work lists (Pisendel), pytest suite with a synthetic publication-profile fixture, CI review gate, and the corpus-check / facsimile-viewer notebooks. Pins CAMAT 0.2.7.
- Pisendel, Konzert für Violine und Streichorchester (`pisendel_violin_concerto`), assembled by Egor Polyakov on 2026-09-02 from the 32 page files (commit `dd634c6`): one `mdiv`, 480 measures, 32 facsimile surfaces with measure zones. Francy Häring corrected the page files (July–September 2026) and continued correcting in the combined file until 2026-10-07. Status `combined`; the consistency report, regenerated with CAMAT 0.2.7 on 2026-10-27, has 120 rows (the previous hand-made report had 206). The file still carries the minimal OMR/transcoding header.
- Pages 00032, 00033 and 00052 (printed pp. 2, 3, 22) re-encoded by Egor Polyakov from Dorico MusicXML and given IIIF facsimiles and measure zones (2026-09-01/02).
- Documentation and license layer: README restructure, `docs/editorial-workflow.md`, `docs/editorial-policy.md`, `docs/mei-encoding-profile.md`, `docs/templates/mei-header-template.xml`, pinned `schemas/mei-CMN-5.1.rng`, `LICENSE.md` with `LICENSES/`, and `CITATION.cff`.

### Fixed

- Pisendel m. 37 (p. 4): restored the 3/4 meter of the Vivace after the common-time Andante (mm. 27–36); without it mm. 37–173 were read as 4/4 and CAMAT 0.2.7 reported 924 underfull layers (`64ee4df`).
