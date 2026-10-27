from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def module():
    spec = importlib.util.spec_from_file_location('ddt_build_site', ROOT / 'scripts/build_site.py')
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_site_index_lists_every_work_and_copies_the_listed_files(tmp_path):
    out = tmp_path / '_site'
    index = module().build(out)
    works = index['works']
    assert [w['label'] for w in works] == [
        'Pisendel', 'Hasse', 'C. P. E. Bach', 'Telemann', 'Graupner', 'Stölzel', 'Hurlebusch',
    ]
    assert json.loads((out / 'works.json').read_text(encoding='utf-8')) == index
    listed = json.loads((ROOT / 'validation/editorial-works.json').read_text(encoding='utf-8'))['works']
    assert {w['key'] for w in works if 'mei' in w} == {w['key'] for w in listed}
    assert all(w['status'] == 'pending' for w in works if 'mei' not in w)
    assert next(w for w in works if w['id'] == 'pisendel')['status'] == 'combined'
    assert next(w for w in works if w['id'] == 'hasse')['status'] == 'combined'
    for work in works:
        if 'mei' in work:
            assert digest(out / work['mei']) == digest(ROOT / work['source'])
            assert (ROOT / work['report']).is_file()
    for name in ('index.html', 'viewer.css', 'viewer.js'):
        assert (out / name).read_bytes() == (ROOT / 'site' / name).read_bytes()


def test_build_refuses_to_empty_the_repository_or_its_folders(monkeypatch):
    m = module()
    def refuse(path):
        raise AssertionError(f'would delete {path}')
    monkeypatch.setattr(m.shutil, 'rmtree', refuse)
    for out in (ROOT, ROOT.parent, ROOT / 'site', ROOT / '29_30_instrumentalkonzerte_final'):
        monkeypatch.setattr('sys.argv', ['build_site.py', str(out)])
        assert m.main() == 1


def test_build_rejects_a_listed_work_it_does_not_know_or_whose_pages_differ(tmp_path, monkeypatch):
    m = module()
    works = list(m.WORKS)
    monkeypatch.setattr(m, 'WORKS', works[1:])
    with pytest.raises(SystemExit, match='pisendel_violin_concerto'):
        m.build(tmp_path / 'a')
    monkeypatch.setattr(m, 'WORKS', [{**works[0], 'pages': {'from': '1', 'to': '31'}}] + works[1:])
    with pytest.raises(SystemExit, match='pages'):
        m.build(tmp_path / 'b')
