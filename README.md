# DdT 1, Vol. 29/30 — Instrumentalkonzerte deutscher Meister

This repository contains a work-in-progress scholarly MEI edition of *Instrumentalkonzerte deutscher Meister*, edited by Arnold Schering and published in 1907 as volumes 29/30 of the first series of *Denkmäler deutscher Tonkunst*.

The edition began with page-level optical music recognition (OMR) data from [musiconn.scoresearch](https://www.musiconn.de/services/musiconnscoresearch), which is being corrected against the [Bayerische Staatsbibliothek digital facsimile](https://www.digitale-sammlungen.de/en/view/bsb00023250). Editorial work is carried out with [mei-friend](https://mei-friend.mdw.ac.at/). The corpus is at the proofreading stage: 300 page-level files cover the full score, and one work (Pisendel) has been assembled.

## Edition at a glance

|                     |                                                              |
| ------------------- | ------------------------------------------------------------ |
| Contents            | Seven concertos by seven composers                           |
| Encoding            | MEI 5.1; work files target the Common Music Notation customization at finalization |
| Editorial unit      | One MEI file per complete work                               |
| Facsimile alignment | IIIF-linked surfaces with measure-level zones                |
| Current state       | Pisendel combined; page-level proofreading under way for Hasse and C. P. E. Bach; the others pending |

## Source edition

| Field                 | Description                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------- |
| Title                 | *Instrumentalkonzerte deutscher Meister*                                                            |
| Series                | *Denkmäler deutscher Tonkunst*, first series, vols. 29/30                                           |
| Editor                | Arnold Schering ([GND 118754688](https://d-nb.info/gnd/118754688))                                  |
| Publication           | Leipzig: Breitkopf & Härtel, 1907                                                                   |
| Extent               | LXXVIII, 300 pages                                                                                  |
| Holding institution   | Bayerische Staatsbibliothek, München                                                                |
| Shelfmark             | 2 Mus.pr. 3951-29/30                                                                                |
| BSB identifier        | `991077497029707356`                                                                                |
| BV number             | `BV007816573`                                                                                       |
| WorldCat              | [OCLC 68616423](https://search.worldcat.org/title/68616423)                                         |
| Persistent identifier | [urn:nbn:de:bvb:12-bsb00023250-6](https://mdz-nbn-resolving.de/urn:nbn:de:bvb:12-bsb00023250-6)    |
| Digital facsimile     | [Bayerische Staatsbibliothek](https://www.digitale-sammlungen.de/en/view/bsb00023250)               |
| IIIF manifest         | [bsb00023250](https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb00023250/manifest)         |
| Facsimile license     | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)                               |
| Composers             | [Johann Georg Pisendel](https://d-nb.info/gnd/11946912X) (11946912X); [Johann Adolf Hasse](https://d-nb.info/gnd/118546651) (118546651); [Carl Philipp Emanuel Bach](https://d-nb.info/gnd/118505505) (118505505); [Georg Philipp Telemann](https://d-nb.info/gnd/11862119X) (11862119X); [Christoph Graupner](https://d-nb.info/gnd/118718517) (118718517); [Gottfried Heinrich Stölzel](https://d-nb.info/gnd/118618458) (118618458); [Conrad Friedrich Hurlebusch](https://d-nb.info/gnd/118708236) (118708236) |

Printed page = BSB image number − 30 (image 00031 is printed p. 1). The digitization's front matter is on images 00001–00030.

## Corpus contents

The status describes the complete work-level file, not the presence or edit history of its individual source pages.

| Composer | Work | Printed pages | BSB images | MEI stem | Status | Proofreading |
| --- | --- | --- | --- | --- | --- | --- |
| Johann Georg Pisendel | Konzert für Violine und Streichorchester | 1–32 | 00031–00062 | `pisendel_violin_concerto` | combined | Francy Häring |
| Johann Adolf Hasse | Konzert für Flöte, zwei Violinen, Viola und Bass | 33–61 | 00063–00091 | `hasse_flute_concerto` | pending | Jingyu Tu |
| Carl Philipp Emanuel Bach | Concerto a Cembalo concertato, 2 Violini, Viola e Basso | 62–102 | 00092–00132 | `cpe_bach_keyboard_concerto` | pending | Lea Meret Beck |
| Georg Philipp Telemann | Konzert für Violine und Streichorchester, 2 Flöten, 2 Oboen, 2 Trompeten und Pauken | 103–195 | 00133–00225 | `telemann_violin_concerto` | pending | — |
| Christoph Graupner | Concerto a 2 Flauti traversieri, 2 Hautbois, 2 Violini, Viola e Cembalo | 196–220 | 00226–00250 | `graupner_concerto_2_flutes_2_oboes` | pending | You Zhou |
| Gottfried Heinrich Stölzel | Concerto grosso a quattro Chori | 221–272 | 00251–00302 | `stoelzel_concerto_grosso_quattro_chori` | pending | — |
| Conrad Friedrich Hurlebusch | Konzert für 2 Oboen, Fagott, Solovioline und Streichorchester | 273–300 | 00303–00330 | `hurlebusch_concerto_2_oboes_fagott_violin` | pending | — |

Status terms are used as follows:

- `pending`: no complete work-level MEI has been assembled.
- `combined`: source-page encodings have been assembled with linked facsimile surfaces.
- `corrected`: the musical text and facsimile references have been reviewed and local consistency checks completed.
- `finalized`: metadata, editorial review, validation, and publication naming are complete.

The Proofreading column names who is correcting the page-level files for that work (or has done so). It does not by itself change the work-level status.

Pisendel was assembled by Egor Polyakov on 2026-09-02 from the 32 page files (commit `dd634c6`): one `mdiv`, 480 measures, 32 facsimile surfaces with measure zones. Francy Häring corrected the page files (July–September 2026) and continued correcting in the combined file until 2026-10-07. Work-level correction is not complete; its consistency report, regenerated with CAMAT 0.2.7 on 2026-10-27, has 120 rows. The file still carries the minimal OMR/transcoding header; the publication header is applied at finalization.

## Repository contents

- [`29_30_instrumentalkonzerte_final/`](29_30_instrumentalkonzerte_final/) contains the combined work-level editions. A temporary `_corr` filename suffix indicates a file still undergoing editorial work. Beside each assembled score is its tracked `_consistency_report.csv`.
- [`29_30_instrumentalkonzerte_deutscher_meister_bsb00023250/`](29_30_instrumentalkonzerte_deutscher_meister_bsb00023250/) preserves the page-level OMR source material. Page files are named `bsb00023250_<image-number>_facs_zones.mei` and point at IIIF images such as `https://api.digitale-sammlungen.de/iiif/image/v2/bsb00023250_<image>/full/4134,/0/default.jpg`.
- [`docs/mei-encoding-profile.md`](docs/mei-encoding-profile.md) documents the publication header, facsimile conventions, and validation profile.
- [`docs/editorial-workflow.md`](docs/editorial-workflow.md) records file naming, work-level statuses, and the correction sequence.
- [`docs/editorial-policy.md`](docs/editorial-policy.md) defines source relationships, correction categories and responsibility.
- [`validation/README.md`](validation/README.md) explains the checks, reports and release gate, and separates shared CAMAT checks from this edition's publication rules.
- [`docs/templates/mei-header-template.xml`](docs/templates/mei-header-template.xml) is the reusable publication header skeleton.
- [`schemas/mei-CMN-5.1.rng`](schemas/mei-CMN-5.1.rng) is the pinned MEI 5.1 CMN schema for offline validation.
- [`scripts/`](scripts/), [`tests/`](tests/), [`mei_corpus_checks.ipynb`](mei_corpus_checks.ipynb) and [`mei_facsimile_viewer.ipynb`](mei_facsimile_viewer.ipynb) are the local validation and inspection tools (ported from DdT 1 vol. 11).
- [`site/`](site/) is the web viewer (ported from DdT 1 vol. 11): each assembled score rendered with Verovio page by page beside its BSB facsimile page, measure zones linked both ways, with its editorial notes; the works not yet assembled are listed as pending. `python scripts/build_site.py` assembles it in `_site/` (preview with `python -m http.server -d _site`); GitHub Pages publishes it from `main` at https://egorpol.github.io/DdT_1_vol_29_30/ (for example [Pisendel, measure 37](https://egorpol.github.io/DdT_1_vol_29_30/#pisendel/37)). `python scripts/check_site.py _site <shot-dir>` opens every page of every work in headless Chromium and reports rendered measures that don't match their facsimile zones, empty facsimiles, measure boxes beyond their staves and console errors; set `SITE_URL` to check a published copy instead of a local server. It needs Playwright with Chromium (`pip install playwright && playwright install chromium`), which `requirements.txt` and CI leave out.
- [`CHANGELOG.md`](CHANGELOG.md) records notable changes; [`CITATION.cff`](CITATION.cff) holds citation metadata.

## Check and inspect locally

Use Python 3.11 or newer and the same environment for these commands and the notebooks. With a neighboring CAMAT checkout:

```sh
python scripts/update_camat.py --dry-run
python scripts/update_camat.py
python scripts/validate_corpus.py --mode review --verovio --camat-parse
python scripts/refresh_editorial_reports.py
```

For a standalone clone without a neighboring CAMAT checkout,
`python -m pip install -r requirements.txt` installs the tested versions
(Python 3.12 or newer), including CAMAT 0.2.7 from PyPI; `python scripts/update_camat.py --git-ref v0.2.7`
installs the same CAMAT from Git and records the resolved code. CAMAT 0.2.7's
duration checks also cover measures marked `metcon="false"`, as future committed
reports will; CAMAT 0.2.1–0.2.6 skip them.

Install libxml2's `xmllint` separately. Open
[`mei_corpus_checks.ipynb`](mei_corpus_checks.ipynb) for the same general + DdT
checks and [`mei_facsimile_viewer.ipynb`](mei_facsimile_viewer.ipynb) for source
inspection. Dependency updates are explicit, separate operations; validation
records the actual CAMAT version/revision/source hashes.

The publication work list selects Pisendel. A separate review-only
[editorial work list](validation/editorial-works.json) covers the same assembled
score for shared reports; publication candidates still require explicit review.
Official IIIF Schematron warnings remain pending publication review. See
[the tool guide](validation/README.md) for all options, reports, scope and
release gates.

## Editorial approach

This is a corrected digital edition based on DdT 1907, retaining its staff layout and the cembalo staves as printed in DdT. OMR repairs, source-supported emendations, conjectural emendations and encoding notes are distinguished in the [editorial policy](docs/editorial-policy.md). Substantive departures from DdT are documented in the MEI. Each measure is linked to a zone on the corresponding facsimile surface, allowing the encoded notation and source image to be inspected together.

The MEI 5.1 CMN publication profile is the target for finalizing work-level files. Detailed implementation guidance is kept in the [MEI encoding profile](docs/mei-encoding-profile.md).

## Contributors

When a work is finalized, its MEI header records these responsibilities in `titleStmt/respStmt`. MEI encoding and work-level assembly: CAMAT.

| Contributor    | Page-level OMR correction                         | Work-level correction                          |
| -------------- | ------------------------------------------------- | ---------------------------------------------- |
| Lea Meret Beck | C. P. E. Bach (in progress)                       | —                                              |
| Francy Häring  | Pisendel                                          | Pisendel (through 2026-10-07)                  |
| Egor Polyakov  | pages 2, 3, 22 (Dorico re-encoding)               | Pisendel assembly                              |
| Jingyu Tu      | Hasse (in progress)                               | —                                              |
| You Zhou       | Graupner (p. 196 so far)                          | —                                              |

## Funding

Work on this corpus is funded by the German Research Foundation (DFG), programme Library and Information Services — E-Research Technologies (LIS), grant PF 669/18-1.

## Citation

Cite this repository as a work in progress, and cite the underlying source edition separately. The same metadata are in [`CITATION.cff`](CITATION.cff); the [changelog](CHANGELOG.md) lists notable changes.

> Polyakov, Egor, Lea Meret Beck, Francy Häring, Jingyu Tu, and You Zhou. *DdT 1, Vol. 29/30 — Instrumentalkonzerte deutscher Meister*. Work in progress. CAMAT Corpus Editions. https://github.com/egorpol/DdT_1_vol_29_30.

> *Instrumentalkonzerte deutscher Meister*. Edited by Arnold Schering. Leipzig: Breitkopf & Härtel, 1907. Digitized by the Bayerische Staatsbibliothek as `bsb00023250`.

## License

MEI data and documentation are released under [CC BY 4.0](LICENSES/CC-BY-4.0.txt); project-authored code under the [MIT License](LICENSES/MIT.txt). See [`LICENSE.md`](LICENSE.md) for the split and for third-party material. The unchanged official MEI schema retains its upstream Educational Community License 2.0 notice.

Third-party facsimile images are separate from the MEI-data license. The BSB digitization is offered under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The MEI files link to these images on the BSB IIIF server; this repository does not copy them.
