# Editorial Workflow

The principal editing unit is the complete work (concerto). Page-level MEI files are retained as source material, but progress and publication decisions are made at work level.

## Directory roles

- `29_30_instrumentalkonzerte_final/` contains the combined work-level MEI files and, beside each, its tracked `_consistency_report.csv` for contributors.
- `29_30_instrumentalkonzerte_deutscher_meister_bsb00023250/` contains the page-level OMR source files used during assembly.
- `docs/` contains editorial and technical documentation.
- `schemas/` holds the pinned MEI 5.1 CMN schema used for offline validation.

## Page-level proofreading

Students correct page files in [mei-friend](https://mei-friend.mdw.ac.at/) against the corresponding BSB page image and commit per measure or system. A work is assembled when its pages are proofread. Pages 00032, 00033 and 00052 (printed pp. 2, 3, 22) were re-encoded by Egor Polyakov from Dorico MusicXML and given IIIF facsimiles and measure zones (2026-09-01/02).

Page-level files point at IIIF images such as:

```text
https://api.digitale-sammlungen.de/iiif/image/v2/bsb00023250_<image>/full/4134,/0/default.jpg
```

## Work-level sequence

1. Assemble the relevant page-level source files into one complete work when no combined file exists.
2. Correct the notation against the DdT facsimile in mei-friend. Follow the [editorial policy](editorial-policy.md) and record substantive departures from DdT at the affected events.
3. Confirm that surfaces, measure zones, page breaks, and system breaks represent the source structure.
4. Apply the [MEI encoding and publication profile](mei-encoding-profile.md).
5. Refresh the consistency report beside the combined file after changes.
6. Review the resulting report and compare the rendered score with the facsimile.
7. Review the editorial annotations, confirm release metadata, remove the temporary `_corr` suffix, and update the publication URI together. Follow the release-identity rules in the [publication profile](mei-encoding-profile.md#release-identity-versions-and-citation).

## File naming

Work-level working files use a stem that already begins with the composer:

```text
29_30_instrumentalkonzerte_final/<stem>_corr.mei
```

`_corr` marks a working file. Final publication filenames omit that suffix: `<stem>.mei`. `meiHead/altId[@type='repository-stem']` equals the stem (without `_corr`). Examples: `pisendel_violin_concerto`, `hasse_flute_concerto`.

Page-level source filenames retain the BSB image identifier:

```text
bsb00023250_<image-number>_facs_zones.mei
```

In this digitization, printed score pages and BSB image numbers are offset by thirty: printed page 1 corresponds to image `00031`. Work-level surface numbering is independent and begins with `1`.

## Status vocabulary

- `pending`: no complete work-level MEI has been assembled.
- `combined`: source-page encodings have been assembled with linked facsimile surfaces.
- `corrected`: the musical text and facsimile references have been reviewed and local consistency checks completed.
- `finalized`: metadata, editorial review, validation, and publication naming are complete.

Update the work table in the main README when the work-level status changes. Page-by-page edit metadata is not used for the public status.

## Checks

The `_consistency_report.csv` beside a combined file lists CAMAT's consistency findings and is regenerated after changes. The scripted refresh and validation gate used in the sibling DdT 1 vol. 11 edition are to be ported later. The pinned MEI 5.1 CMN schema at [`schemas/mei-CMN-5.1.rng`](../schemas/mei-CMN-5.1.rng) keeps validation reproducible and offline once tooling is present.

An empty report means only that the implemented automated checks found no inconsistency. It cannot determine whether every pitch, rhythm, articulation, accidental, figured-bass symbol, or editorial reading agrees with the printed source.
