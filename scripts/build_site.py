#!/usr/bin/env python3
"""Assemble the static web viewer for GitHub Pages.

Copies site/ (the viewer) and the assembled MEI files listed in
validation/editorial-works.json into OUT, and writes OUT/works.json, the index
the viewer's work selector reads: all seven works of the volume, those not yet
assembled without a score. The facsimile pages are not copied: the viewer loads
them from the BSB IIIF server. OUT is emptied first.

Standard library only.

Usage: python scripts/build_site.py [OUT]    (default: _site)
Preview: python -m http.server -d _site, then open http://localhost:8000/
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_FILES = ["index.html", "viewer.css", "viewer.js"]
WORK_LIST = "validation/editorial-works.json"
# The volume's works in printed order, as in the README's work table. The
# titles stand in for the MEI title, which stays the printed heading ("Concerto.")
# until a work's publication header is applied.
WORKS = [
    {"key": "pisendel_violin_concerto", "id": "pisendel", "label": "Pisendel",
     "composer": "Johann Georg Pisendel",
     "title": "Konzert für Violine und Streichorchester",
     "pages": {"from": "1", "to": "32"}},
    {"key": "hasse_flute_concerto", "id": "hasse", "label": "Hasse",
     "composer": "Johann Adolf Hasse",
     "title": "Konzert für Flöte, zwei Violinen, Viola und Bass",
     "pages": {"from": "33", "to": "61"}},
    {"key": "cpe_bach_keyboard_concerto", "id": "cpe_bach", "label": "C. P. E. Bach",
     "composer": "Carl Philipp Emanuel Bach",
     "title": "Concerto a Cembalo concertato, 2 Violini, Viola e Basso",
     "pages": {"from": "62", "to": "102"}},
    {"key": "telemann_violin_concerto", "id": "telemann", "label": "Telemann",
     "composer": "Georg Philipp Telemann",
     "title": "Konzert für Violine und Streichorchester, 2 Flöten, 2 Oboen, 2 Trompeten und Pauken",
     "pages": {"from": "103", "to": "195"}},
    {"key": "graupner_concerto_2_flutes_2_oboes", "id": "graupner", "label": "Graupner",
     "composer": "Christoph Graupner",
     "title": "Concerto a 2 Flauti traversieri, 2 Hautbois, 2 Violini, Viola e Cembalo",
     "pages": {"from": "196", "to": "220"}},
    {"key": "stoelzel_concerto_grosso_quattro_chori", "id": "stoelzel", "label": "Stölzel",
     "composer": "Gottfried Heinrich Stölzel",
     "title": "Concerto grosso a quattro Chori",
     "pages": {"from": "221", "to": "272"}},
    {"key": "hurlebusch_concerto_2_oboes_fagott_violin", "id": "hurlebusch", "label": "Hurlebusch",
     "composer": "Conrad Friedrich Hurlebusch",
     "title": "Konzert für 2 Oboen, Fagott, Solovioline und Streichorchester",
     "pages": {"from": "273", "to": "300"}},
]


def copy(source: Path, out: Path, target: str) -> None:
    destination = out / target
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    print(f"{source.relative_to(ROOT)} -> {target}")


def build(out: Path) -> dict:
    for name in SITE_FILES:
        copy(ROOT / "site" / name, out, name)

    listed = {w["key"]: w for w in json.loads((ROOT / WORK_LIST).read_text(encoding="utf-8"))["works"]}
    unknown = set(listed) - {w["key"] for w in WORKS}
    if unknown:
        raise SystemExit(f"{WORK_LIST}: {', '.join(sorted(unknown))} not in build_site.WORKS")
    works = []
    for entry in WORKS:
        work = {**entry, "catalogue": None, "status": "pending"}
        if entry["key"] in listed:
            item = listed[entry["key"]]
            if item["printed_page_range"] != entry["pages"]:
                raise SystemExit(f"{WORK_LIST}: {entry['key']} pages {item['printed_page_range']}, not {entry['pages']}")
            source = ROOT / item["file"]
            target = f"mei/{source.name}"
            copy(source, out, target)
            work.update({
                "catalogue": item["catalogue"],
                "status": item["editorial_status"],
                "mei": target,
                "source": item["file"],
                "report": item["file"].removesuffix(".mei") + "_consistency_report.csv",
            })
        works.append(work)

    index = {"works": works}
    (out / "works.json").write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"works.json: {len(works)} works, {sum('mei' in w for w in works)} with MEI")
    return index


def main() -> int:
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "_site").resolve()
    # OUT is emptied: inside the repository only _site may be used.
    if ROOT.is_relative_to(out) or (out.is_relative_to(ROOT) and not out.is_relative_to(ROOT / "_site")):
        print(f"refusing to empty {out}", file=sys.stderr)
        return 1
    if out.exists():
        shutil.rmtree(out)
    build(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
