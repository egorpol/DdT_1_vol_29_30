# Editorial policy and source register

This corpus is a corrected digital edition of the music printed in DdT, first series, volumes 29/30 (1907), edited by Arnold Schering. The edition preserves that source's musical presentation, including the cembalo staves as printed in DdT, while documenting substantive emendations. No other witness has been consulted yet. If one is, record it in `sourceDesc` with an exact locator and record what was actually consulted. Musical coherence supplies a rationale for a conjecture; source comparison establishes whether a reading is supported by a witness.

This policy was set on 2026-10-27, during page-level proofreading. Its adoption does not assert that any existing file already complies, or that every annotation has been revised.

## Sources and their roles

Use `src.ddt1907` for the 1907 DdT edition. It supplies the base score, its cembalo staves as printed, and the existing BSB facsimile/measure-zone mapping. Keep its full description and separate image-use statement in `sourceDesc`.

For individual corrections, cite the printed page and local musical location. Record what was actually consulted. Do not invent a second witness ID for material that has not been seen.

## Correction categories

Use the following distinctions consistently:

1. **OMR or conversion repair:** the encoding is brought into agreement with DdT. Routine repairs can be summarized in revision history and do not each need a published annotation. An ambiguous repair still warrants a local note.
2. **Source-supported emendation:** the encoded reading departs from DdT and is attested by an identified historical witness. Record both readings and the exact evidence location.
3. **Conjectural emendation:** the encoded reading departs from DdT on rhythmic, harmonic, contrapuntal, or other stated grounds without direct witness support. State the reasoning and uncertainty. Prefer the smallest justified intervention and retain a recoverable account of the printed reading.
4. **Retained source reading:** a noteworthy source feature or apparent anomaly is preserved deliberately. Record it when it could otherwise be mistaken for an encoding error. A checker warning may remain as a documented exception.
5. **Encoding note:** the musical reading is preserved but its technical representation, such as a cross-staff tie, needs explanation or has a known renderer limitation.
6. **Unresolved reading:** evidence is insufficient to choose confidently. Mark the uncertainty and record the available readings. Release review must explicitly address it; successful rhythm checks alone do not resolve it.

In particular, the cembalo staves as printed in DdT are source content for this edition. Who realized the figured bass in those staves is not established; do not attribute the realization to Schering. A change to those staves is a departure from DdT. Absence of a realization from an earlier partbook does not by itself support a particular corrected chord or rhythm.

## Recording decisions in MEI

Use one authoritative annotation in the MEI for each substantive decision, attached through `plist` (or an appropriate event pointer) to stable IDs. A corpus-wide list of emendations can be generated from these annotations; avoid manually maintaining a second list that can diverge.

Keep `type="editorial"` for compatibility. Adopt these project-specific `label` values for the categories above: `source-supported-emendation`, `conjectural-emendation`, `source-reading`, `encoding-note`, and `unresolved-reading`. An optional `omr-correction` label can identify a noteworthy recognition repair. These labels are CAMAT conventions, not MEI-defined controlled values.

For an emendation, the annotation must record:

- DdT's reading and the encoded replacement, with enough pitch/duration/context information to reconstruct the difference;
- a precise witness/page locator when a witness supports the change, or the conjectural rationale otherwise;
- the responsible editor through `resp` and any relevant uncertainty in the text;
- the affected event IDs and, when useful, a link to the corresponding source image/zone.

Use `annot/@source` only for sources that actually attest the reading in question. Use `ref/@target` inside the explanation to discuss contextual or contrasting evidence. Link `resp` to the actual responsible header declaration; do not infer the editor from who most recently saved the file. Review dates and review responsibility can be recorded in a meaningful revision entry.

The following illustration uses placeholder IDs and the template's generic `resp.editor`; the responsibility pointer must be replaced by the verified editor's declaration before application. It is a documentation example, not an applied correction or completed review:

```xml
<annot xml:id="editorial.example" type="editorial"
       label="conjectural-emendation"
       plist="#event.id.placeholder"
       resp="#resp.editor">
   <p>DdT prints this event as a dotted eighth note. The dot is omitted
      in the encoding to restore rhythmic consistency in this layer.
      This is a conjectural emendation of the cembalo staves as printed
      in DdT. No additional witness has been consulted for this reading.</p>
</annot>
```

Expand the rhythmic rationale with the actual beat/layer accounting during review. Do not introduce a spurious `source` pointer suggesting that an unconsulted print attests the replacement.

For a release designed to expose selectable alternatives, encode the original and corrected passages with `choice/sic/corr`, or use `app/lem/rdg` for source variants. That requires a documented default reading and tested selection in both the renderer and CAMAT. A corrected reading with complete, addressable annotations is the current lightweight policy. [MEI scholarly editing](https://music-encoding.org/guidelines/v5/content/scholarlyediting.html), [MEI annotation attributes](https://music-encoding.org/guidelines/v5/elements/annot.html).

## Staff layout and analytical views

Retain DdT's score layout, including the cembalo staves as printed (for example Pisendel: "Cembalo I." and "Cembalo II."; C. P. E. Bach: "Cembalo concertato." and "Cembalo ripieno."). Do not remove those staves merely because an earlier partbook transmits continuo only. Treat DdT as the source of that layout without assigning realization authorship more specifically than the evidence supports.

Per-work staff roles are declared when a work is combined. Store them in [`validation/works.json`](../validation/works.json) and [`validation/editorial-works.json`](../validation/editorial-works.json). Preserve source labels in the master when fidelity requires it; provide readable analytical names in the consumer/derived view.

Specify the selected view with each analysis: for example, the encoded instrumental parts alone, or DdT's complete texture including the cembalo staves. A selection of staves is still derived from this corrected DdT edition; it is not automatically an independent diplomatic transcription of earlier partbooks.

## Release review

Before finalization, review substantive annotations against the cited evidence, confirm responsibilities, and disclose retained anomalies or unresolved readings. Record the extent of source comparison accurately: consulting selected passages is different from collating every note. Independent review by a second editor is desirable for conjectural changes when available, but the header must record the review actually performed.

The MEI header carries a concise policy summary. This document carries the fuller corpus policy. Keep the two consistent, and record substantive policy changes with the next corpus/profile version.
