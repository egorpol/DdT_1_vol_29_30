# DdT 1, Vol. 29/30: Instrumentalkonzerte deutscher Meister

Work-in-progress MEI corpus for *Instrumentalkonzerte deutscher Meister*, edited by Arnold Schering and published as volumes 29/30 of *Denkmaeler deutscher Tonkunst*, first series.

The corpus is currently at the initial page-level OMR stage. The repository contains single-page MEI files derived from the BSB digitization, with linked IIIF facsimile images and measure zones. Work-level MEI files have not yet been assembled.

The current MEI files are based on OMR data from the musiconn.scoresearch project. Editorial cleanup and correction are intended to be carried out in [mei-friend](https://mei-friend.mdw.ac.at/).

## Source

| Field | Description |
| --- | --- |
| Title | *Instrumentalkonzerte deutscher Meister. 29/30* |
| Preferred title | *Konzerte / Ausw.* |
| Composers represented | Johann Georg Pisendel; Johann Adolf Hasse; Carl Philipp Emanuel Bach; Georg Philipp Telemann; Christoph Graupner; Gottfried Heinrich Stoelzel; Konrad Friedrich Hurlebusch |
| Editor | Arnold Schering (GND: [118754688](https://d-nb.info/gnd/118754688)) |
| Publication | Leipzig: Breitkopf & Haertel, 1907 |
| Extent | LXXVIII, 300 pages |
| Holding institution | Bayerische Staatsbibliothek, Muenchen |
| Shelfmark | 2 Mus.pr. 3951-29/30 |
| BSB-ID | `991077497029707356` |
| BV number | `BV007816573` |
| WorldCat | [68616423](https://search.worldcat.org/title/68616423) |
| URN | [urn:nbn:de:bvb:12-bsb00023250-6](https://mdz-nbn-resolving.de/urn:nbn:de:bvb:12-bsb00023250-6) |
| Digital facsimile | <https://www.digitale-sammlungen.de/en/view/bsb00023250> |

## Repository Layout

```text
.
|-- README.md
`-- 29_30_instrumentalkonzerte_deutscher_meister_bsb00023250/
    |-- bsb00023250_00031_facs_zones.mei
    |-- bsb00023250_00034_facs_zones.mei
    `-- ...
```

The repository currently has one main MEI data directory:

- `29_30_instrumentalkonzerte_deutscher_meister_bsb00023250/` contains page-level OMR data derived from the BSB digitization.

The page-level OMR files follow this naming pattern:

```text
bsb00023250_<page-image-number>_facs_zones.mei
```

For example, `bsb00023250_00031_facs_zones.mei` points to the corresponding IIIF image:

```text
https://api.digitale-sammlungen.de/iiif/image/v2/bsb00023250_00031/full/4134,/0/default.jpg
```

## Planned Work-Level Files

The work-level files have not yet been assembled. The following table follows the source table of contents and can be used as the initial tracking plan.

| Composer | Work | First BSB image | Suggested MEI stem | Status |
| --- | --- | ---: | --- | --- |
| Johann Georg Pisendel | Konzert fuer Violine und Streichorchester | `00031` | `pisendel_violin_concerto` | pending |
| Johann Adolf Hasse | Konzert fuer Floete, zwei Violinen, Viola und Bass | `00063` | `hasse_flute_concerto` | pending |
| Carl Philipp Emanuel Bach | Concerto a Cembalo concertato, 2 Violini, Viola e Basso | `00092` | `cpe_bach_keyboard_concerto` | pending |
| Georg Philipp Telemann | Konzert fuer Violine und Streichorchester, 2 Floeten, 2 Oboen, 2 Trompeten und Pauken | `00133` | `telemann_violin_concerto` | pending |
| Christoph Graupner | Concerto a 2 Flauti traversieri, 2 Hautbois, 2 Violini, Viola e Cembalo | `00226` | `graupner_concerto_2_flutes_2_oboes` | pending |
| Gottfried Heinrich Stoelzel | Concerto grosso a quattro Chori | `00251` | `stoelzel_concerto_grosso_quattro_chori` | pending |
| Konrad Friedrich Hurlebusch | Konzert fuer 2 Oboen, Fagott, Solovioline und Streichorchester | `00303` | `hurlebusch_concerto_2_oboes_fagott_violin` | pending |

Status values for planned work-level files:

- `pending`: no work-level MEI file has been assembled yet.
- `combined`: page-level MEI files have been assembled into one work-level MEI file with linked facsimile surfaces.
- `corrected`: musical text and facsimile references have been corrected and local consistency checks have been reviewed.
- `finalized`: metadata/header, editorial review, validation, and repository naming are complete.

## MEI Header Policy

Final work-level files should carry a compact MEI header rather than the minimal OMR/transcoding header. The header should document the electronic MEI file, the historical source, the encoding process, the encoded work, and meaningful file revision history.

Modern project responsibility should be separated from historical source responsibility. Arnold Schering is the editor of the 1907 printed source and should be recorded in `sourceDesc`. The student or researcher who reads and corrects the OMR should be recorded in `titleStmt` using `respStmt`, with a responsibility such as `OMR correction and editorial review`.

Keep the header intentionally lean. Avoid `xml:id` values in the header unless another element references them. Do not duplicate the same responsibility in both `titleStmt` and `editionStmt`. Keep application metadata concise, and use `revisionDesc` only for meaningful lifecycle events such as assembly, correction, and finalization.

## Current Progress

Updated: 2026-07-01.

Current page status: 298 page-level MEI files are present, covering BSB image numbers `00031` through `00330`. Image numbers `00032` and `00033` are currently missing from that sequence. No page currently contains mei-friend edit metadata.

## Funding

Work on this corpus is funded by the German Research Foundation (DFG), program Library and Information Services - E-Research Technologies (LIS), grant PF 669/18-1.

## Citation

When citing this corpus, include both the encoded repository and the underlying source:

> Instrumentalkonzerte deutscher Meister. Edited by Arnold Schering. Leipzig: Breitkopf & Haertel, 1907. Digitized by Bayerische Staatsbibliothek, `bsb00023250`.

Digital facsimile: <https://www.digitale-sammlungen.de/en/view/bsb00023250>

## License

This repository does not yet include a top-level license file. Add one before publishing or distributing corrected MEI data.

The historical source is in the public domain, but reuse of the BSB facsimile images and metadata may be subject to the terms of the providing institution. The BSB IIIF manifest currently lists the digital facsimile license as [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Please consult the BSB record linked above for current reuse information.
