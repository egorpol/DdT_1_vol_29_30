# MEI Encoding and Publication Profile

This document records the technical publication profile for the complete work-level MEI files in this repository. It is intended for editors, maintainers, and validators; the main README remains a public overview of the corpus.

A reusable skeleton is available as [`templates/mei-header-template.xml`](templates/mei-header-template.xml). The Pisendel working file has carried the publication header since 2026-10-27; release fields (edition number, release date, versioned URI) are set at finalization.

## Schema profile

Publication files use the official MEI 5.1 Common Music Notation customization:

```xml
<?xml-model href="https://music-encoding.org/schema/5.1/mei-CMN.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="https://music-encoding.org/schema/5.1/mei-CMN.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>
<mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="5.1+CMN">
```

The XML model declarations and `mei/@meiversion` must identify the same MEI release and customization. The repository includes a pinned copy at [`schemas/mei-CMN-5.1.rng`](../schemas/mei-CMN-5.1.rng) for reproducible and offline validation. It is reference and validation infrastructure rather than edition content embedded in an MEI file.

A working file may declare `mei-all` until its publication header is applied, when the publication schema declarations above replace it; the Pisendel file declares them.

## Header model

The header distinguishes the encoded file, the historical source, the encoding process, the abstract musical work, and the file's revision history.

| Section | Purpose |
| --- | --- |
| `fileDesc/titleStmt` | Work title, composer, and responsibility for the digital file |
| `fileDesc/editionStmt` | Release designation and semantic version |
| `fileDesc/pubStmt` | Digital publisher, release date, canonical URI, and MEI-data license |
| `fileDesc/sourceDesc` | Bibliographic description, identifiers, location, page range, facsimile links, and image license |
| `encodingDesc/appInfo` | Significant software stages in the creation of the encoding |
| `encodingDesc/editorialDecl` | Correction policy, interventions, and facsimile conventions |
| `encodingDesc/projectDesc` | Project and funding context |
| `workList/work` | Stable work identifier, catalogue number, title, composer, key, and performing medium |
| `revisionDesc` | Meaningful lifecycle events, newest first |

The structure follows the [MEI metadata guidelines](https://music-encoding.org/guidelines/v5/content/metadata.html). Give each cited source, work, and responsibility statement a stable `xml:id`. Musical events require IDs under the event-identity rule below; optional header prose does not need an ID on every element.

## Title and edition statement

Use the work title alone in `titleStmt/title`, for example:

```xml
<title>Konzert für Violine und Streichorchester</title>
```

The phrase “digital MEI edition” is edition information, not part of the displayed work title. Record it in `editionStmt`, for example:

```xml
<edition n="1.0.0">First digital edition</edition>
```

This example describes an actual first release. Before that release, use a truthful working-edition designation and a documented development version, such as `0.1.0`; do not treat the template's `1.0.0` as evidence that a release has occurred. After a release, working files may retain the last published edition statement while recording subsequent work in `revisionDesc`.

No corpus-wide first-page heading (`pgHead`) decision exists yet. The first-page heading is decided per work at finalization. Keep the authority-linked `composer/persName` in `meiHead`; a page heading does not replace source or work metadata.

## Responsibilities and revisions

Separate modern digital responsibilities from the editorship of the 1907 source. Arnold Schering belongs in `sourceDesc`; contributors responsible for assembly, correction, review, or metadata belong in `titleStmt/respStmt`, with a responsibility such as `OMR correction and editorial review`.

Keep the header intentionally lean. Avoid `xml:id` values in the header unless another element references them. Do not duplicate the same responsibility in both `titleStmt` and `editionStmt`. Keep application metadata concise.

Use `revisionDesc` for significant work-level events such as assembly, completion of correction, application of the publication profile, and release. Each `change/@resp` should point to the relevant `respStmt/@xml:id`. Dates and responsibilities must describe actual work and should be confirmed before publication.

## Source and licensing

The base edition is DdT 1907 (`xml:id="src.ddt1907"`). No other witness has been consulted yet; if one is, describe it in `sourceDesc` with an exact locator. The source register and citation rules are in [editorial-policy.md](editorial-policy.md).

The MEI data and the BSB facsimile are separate resources and require separate rights statements:

- Record the repository's MEI-data license (CC BY 4.0) in `pubStmt/availability`.
- Record the facsimile provider and image-use terms (BSB, CC BY-NC-SA 4.0) inside the bibliographic source description.
- Retain the BSB URN, local identifiers, holding institution, shelfmark, digital record, IIIF manifest, and printed page range.
- An additional witness need not have a public image URL or IIIF manifest to be a valid bibliographic source. Never use a catalogue search page as a `graphic/@target` or invent an IIIF canvas URL.

## Editorial text and source relationships

This is a corrected digital edition based on DdT 1907. It is not an unaltered diplomatic transcription. The [editorial policy](editorial-policy.md) distinguishes OMR repairs, source-supported emendations, conjectural emendations, retained source readings, and encoding comments.

The concise `encodingDesc/editorialDecl` in each published MEI must summarize that policy and identify significant exceptions. Each substantive departure from DdT must have an addressable editorial annotation recording the source reading, encoded reading, evidence/reason, and responsible editor. Keep `annot/@type="editorial"`; the policy defines `@label` categories without changing that existing convention. An annotation's `@source` identifies evidence that actually attests a reading.

Retain DdT's printed staff arrangement and the cembalo staves as printed. Per-work staff roles are declared when a work is combined. State the relationship in the header and provide a documented staff-to-role mapping for analysis. Source-faithful score labels may remain as printed; analytical labels can be maintained in a corpus manifest or derived view. Do not introduce visible labels solely to compensate for a parser limitation without an explicit editorial decision.

## Event identity

All notes (including chord tones), chords, rests, spaces, full-measure rest/space events, measures, layers, staves, and independently addressable control events such as ties, slurs, figured-bass events, tempo marks, and annotations must have persistent `xml:id` values in release files. Extend this set explicitly when the corpus uses additional event types. An ID is required for an event that CAMAT exposes for selection or annotation even when the MEI schema makes it optional.

Preserve existing IDs across correction, formatting, and release renaming. IDs are unique within each XML document; the cross-corpus address is the stable file identifier plus `#xml-id`. A bare `#id` in a finalized file must resolve in that file. Cross-page fragments may be tolerated during assembly, but a similarly named ID in a different standalone release file does not resolve a broken local reference.

## Work declarations

Each complete file declares one principal `work` with a stable `xml:id`. Its `mdiv/@decls` points to that work. Record a normalized title, composer authority record, and performing medium when known. Catalogue numbers such as TWV, Wq/H or GWV are recorded only when verified against a catalogue; never guessed.

The legacy `altId` type name `repository-stem` denotes a stable local edition key. In this repository the stem already begins with the composer, so `altId[@type='repository-stem']` equals the stem (for example `pisendel_violin_concerto`). It deliberately omits the temporary `_corr` suffix. Preserve existing local keys; map them explicitly to files as described below.

## Release identity, versions, and citation

Keep three identities distinct: the musical work (catalogue number when verified), the local encoded-edition key (`pisendel_violin_concerto`), and the versioned published file.

- For this repository, the final filename is `<stem>.mei`; the working filename is `<stem>_corr.mei`, both under `29_30_instrumentalkonzerte_final/`. Record an explicit manifest mapping if a future exception is needed.
- `pubStmt/identifier[@type='URI']` identifies the current publicly accessible file. While a file is a working edition it may point to its existing `_corr` path. When releasing it, update this URI and remove `_corr` together. Do not install a guessed future URL in a working header.
- Record an immutable version URL as a separate `identifier[@type='versioned-URI']` only when preparing an actual release. It names the release tag, for example `…/blob/v1.0.0/<file>`. A commit URL cannot work, because the file would have to contain the commit that contains it, so the commit goes in the manifest's `immutable_git_ref` instead. Commit the final files, commit the manifest with that commit's SHA, tag the manifest commit locally, run release mode, and push the tag only once it passes. Release mode checks that the tag and the commit both carry the working files' exact bytes.
- Use a single corpus release number for the set of files shipped together and record it in each included file's `edition/@n`. The publication date is the actual release date; editing dates belong in `revisionDesc`. Corrected releases receive a new version rather than silently replacing an archived dataset.
- Define version changes in the release notes: patch for compatible corrections or metadata fixes with preserved event identity; minor for added works or compatible new coverage; major for incompatible identity, segmentation, or analytical-interpretation changes. Disclose musical corrections in the notes even when the version increment is small.
- Publish `CITATION.cff` with each release. The corpus release manifest is [`validation/works.json`](../validation/works.json) (see [`validation/README.md`](../validation/README.md)). The manifest should identify the corpus/profile version, local edition key, catalogue number when known, final relative file path, per-file SHA-256, source IDs/page ranges, staff roles, editorial status, and the validation-run reference. Hash the final MEI files after their metadata is set; keep those hashes in the manifest, not recursively inside the files being hashed.
- Add an archival DOI or other persistent release identifier once it has been issued. Cite that specific release for reproducible research, retaining the repository URL for current development. Do not fabricate a DOI, archive record, release date, or editor sign-off to fill a template.

The manifest documents which works are included and which remain in progress. A corpus release need not imply that every working file in the repository is finalized. No release has been published yet.

## Facsimile and page boundaries

Use the following conventions consistently:

- Each source page is represented by one `surface` with a `graphic` and measure zones.
- For BSB surfaces, `surface/@corresp` points to the exact IIIF Presentation canvas; `graphic/@target` points to the requested image resource.
- Every measure points to its measure zone through `measure/@facs`.
- Every measure zone is referenced by exactly one measure and lies within its surface's `@ulx`/`@uly`/`@lrx`/`@lry` bounds.
- Use one numbered `pb` for the first encoded content on every surface.
- Use `sb` for the remaining original system boundaries on that surface.
- `surface/@n` and `pb/@n` form a work-local sequence beginning with `1`.
- Record the original printed range in `sourceDesc/biblScope`; do not overload the local page sequence with printed pagination.

These topology rules describe the base-edition facsimile. A supplementary witness may be cited by part and printed page/folio without introducing a second competing page-break sequence. If supplementary images are later provided, keep their source identity and locations distinct from the base-edition `measure/@facs` mapping.

IIIF is not required by MEI: `graphic/@target` can point to an ordinary image URI, including a resolvable relative path in an image bundle. Test the chosen serving method with the intended viewer. Do not create public image pointers until the files and their redistribution terms are available.

## Publication validation

Before changing a work's status to `finalized`, confirm all of the following:

1. The file is well-formed XML and passes both RELAX NG and the embedded MEI 5.1 CMN Schematron rules. Presence of an XML model declaration is not proof that its rules ran.
2. Required event IDs are present, all `xml:id` values are unique within the file, and local references resolve, including `resp`, `source`, and `decls`.
3. Every measure has one valid facsimile zone and the zone is on the active surface.
4. Surface and `pb` sequences agree, with one `pb` per surface.
5. Work declarations, responsibilities, editorial annotations, dates, identifiers, source range, staff roles, final filename, and publication URIs have been reviewed. File-level license checks must inspect `fileDesc/pubStmt/availability` specifically; an image license does not satisfy that requirement.
6. Verovio renders the complete file without warning or error logs.
7. The notation has been compared visually with the facsimile; an empty automated report does not establish musical accuracy.
8. The validation record identifies executed, skipped, and failed checks, the schema/profile and tool versions, and input hashes. A missing validator or disabled pass must not be reported as a pass. Any accepted source anomaly or tool limitation has an explicit rationale; substantive unresolved readings remain visible.

The validation tooling in [`validation/`](../validation/README.md) checks these publication requirements; its README lists which checks run in review and in release mode. Existing combined files may still carry a minimal OMR/transcoding header until their publication headers are applied; the review gate reports those gaps without rewriting MEI.
