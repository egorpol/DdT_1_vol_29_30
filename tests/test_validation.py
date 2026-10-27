from __future__ import annotations

import copy
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from validation.rules import edition_rows

M = 'http://www.music-encoding.org/ns/mei'
ID = '{http://www.w3.org/XML/1998/namespace}id'
PROFILE = json.loads((ROOT / 'validation/profile.json').read_text())
MANIFEST = json.loads((ROOT / 'validation/works.json').read_text())
FIXTURE = ROOT / 'tests/fixtures/publication_profile.mei'


def fixture_work():
    work = copy.deepcopy(MANIFEST['works'][0])
    work['printed_page_range'] = {'from': '1', 'to': '2'}
    work['staff_roles'] = {'1': 'violin', '2': 'continuo'}
    return work


@pytest.fixture
def score(tmp_path):
    work = fixture_work()
    path = tmp_path / work['file']
    path.parent.mkdir(parents=True)
    path.write_bytes(FIXTURE.read_bytes())
    tree = ET.parse(path)
    return tmp_path, path, tree, work


def save(path, tree):
    declarations = '\n'.join(line for line in path.read_text().splitlines() if line.startswith('<?xml-model'))
    path.write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + declarations + '\n' + ET.tostring(tree.getroot(), encoding='unicode'))


def checks(score, mode='review'):
    root, path, tree, work = score
    return {r['check'] for r in edition_rows(work, root_dir=root, profile=PROFILE, manifest=MANIFEST, mode=mode)}


def test_fixture_validates_against_schema():
    schema = etree.RelaxNG(etree.parse(str(ROOT / PROFILE['schema'])))
    assert schema.validate(etree.parse(str(FIXTURE)))


def test_fixture_is_clean_in_review(score):
    assert checks(score) == set()


def test_digital_license_scoped_to_pubstmt(score):
    _, path, tree, _ = score
    pub = tree.getroot().find(f'.//{{{M}}}pubStmt')
    pub.remove(pub.find(f'{{{M}}}availability'))
    assert tree.getroot().find(f'.//{{{M}}}sourceDesc//{{{M}}}availability') is not None
    save(path, tree)
    assert 'ddt.digital_license' in checks(score)


def test_exact_schema_declaration(score):
    _, path, _, _ = score
    path.write_text(path.read_text().replace('/schema/5.1/', '/schema/5.0/'))
    assert 'ddt.schema_declaration' in checks(score)


def test_release_events_and_review_blockers(score):
    _, path, tree, _ = score
    tree.getroot().find(f'.//{{{M}}}music//{{{M}}}note').attrib.pop(ID)
    save(path, tree)
    rules = checks(score, 'release')
    assert {'ddt.event_ids', 'ddt.editorial_review', 'ddt.release_version', 'ddt.filename'} <= rules


def test_incomplete_annotations(score):
    _, path, tree, _ = score
    annotation = tree.getroot().find(f'.//{{{M}}}annot')
    annotation.attrib.pop('plist', None)
    save(path, tree)
    assert 'ddt.annotation_fields' in checks(score)


def test_valid_conjecture_needs_no_attesting_source(score):
    _, path, tree, _ = score
    for annotation in tree.getroot().iter(f'{{{M}}}annot'):
        annotation.set('label', 'conjectural-emendation')
        annotation.set('resp', '#resp.editor')
        annotation.attrib.pop('source', None)
    save(path, tree)
    assert not {'ddt.annotation_fields', 'ddt.annotation_evidence', 'ddt.unresolved_reading'} & checks(score)


def test_publication_uri_and_version(score):
    _, path, tree, _ = score
    tree.getroot().find(f'.//{{{M}}}pubStmt/{{{M}}}identifier').text = 'https://example.org/wrong.mei'
    save(path, tree)
    assert 'ddt.publication_uri' in checks(score)
    assert 'ddt.release_version' in checks(score, 'release')


def test_versioned_uri_names_the_release_tag(score):
    root, path, tree, work = score
    manifest = {**MANIFEST, 'release_version': '9.9.9', 'immutable_git_ref': 'a' * 40}
    identifier = ET.SubElement(tree.getroot().find(f'.//{{{M}}}pubStmt'), f'{{{M}}}identifier', type='versioned-URI')
    def rules(uri):
        identifier.text = uri
        save(path, tree)
        return {r['check'] for r in edition_rows(work, root_dir=root, profile=PROFILE, manifest=manifest, mode='release')}
    base = PROFILE['public_base_url'].split('/blob/', 1)[0]
    assert 'ddt.immutable_uri' not in rules(f'{base}/blob/v9.9.9/{work["file"]}')
    # A commit URL cannot be inside the commit it names.
    assert 'ddt.immutable_uri' in rules(f'{base}/blob/{"a" * 40}/{work["file"]}')


def test_facsimile_topology(score):
    _, path, tree, _ = score
    topology = {'ddt.measure_zone', 'ddt.unused_measure_zone', 'ddt.shared_measure_zone', 'ddt.zone_bounds'}
    assert not topology & checks(score)
    first, second, third = list(tree.getroot().iter(f'{{{M}}}measure'))[:3]
    zone = next(z for z in tree.getroot().iter(f'{{{M}}}zone') if z.get(ID) == first.get('facs').removeprefix('#'))
    second.set('facs', first.get('facs'))
    third.attrib.pop('facs')
    zone.set('lrx', '99999')
    save(path, tree)
    assert topology <= checks(score)


def test_missing_selected_manifest_work(score):
    _, path, _, _ = score
    path.unlink()
    assert 'ddt.manifest_file' in checks(score)


def test_filename_rejects_composer_prefix(score):
    root, path, tree, work = score
    bad_name = 'buxtehude_' + work['key'] + '_corr.mei'
    bad = path.with_name(bad_name)
    path.rename(bad)
    work['file'] = str(Path(work['file']).with_name(bad_name))
    assert 'ddt.filename' in checks((root, bad, tree, work))


def test_filename_accepts_key_corr(score):
    assert 'ddt.filename' not in checks(score)


def test_catalogue_null_skips_check(score):
    _, path, tree, work = score
    assert work.get('catalogue') is None
    principal = tree.getroot().find(f'.//{{{M}}}workList/{{{M}}}work')
    # No catalogue identifier present; null catalogue must not flag.
    assert principal.find(f'{{{M}}}identifier') is None
    assert 'ddt.catalogue' not in checks(score)


def test_catalogue_type_derived_from_manifest(score):
    root, path, tree, work = score
    work['catalogue'] = 'TWV 51:D9'
    principal = tree.getroot().find(f'.//{{{M}}}workList/{{{M}}}work')
    ET.SubElement(principal, f'{{{M}}}identifier', type='TWV').text = 'TWV 51:D9'
    save(path, tree)
    assert 'ddt.catalogue' not in checks((root, path, tree, work))


def test_catalogue_wrong_type_is_flagged(score):
    root, path, tree, work = score
    work['catalogue'] = 'TWV 51:D9'
    # Wrong @type with the right text must still be flagged.
    principal = tree.getroot().find(f'.//{{{M}}}workList/{{{M}}}work')
    ET.SubElement(principal, f'{{{M}}}identifier', type='catalogue').text = 'TWV 51:D9'
    save(path, tree)
    assert 'ddt.catalogue' in checks((root, path, tree, work))


def test_skipped_required_pass_cannot_be_review_success(tmp_path):
    import importlib.util
    module_spec = importlib.util.spec_from_file_location('ddt_entry', ROOT / 'scripts/validate_corpus.py')
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    assert module.main(['--mode', 'review', '--skip-schematron', '--output-dir', str(tmp_path / 'run')]) == 1
    record = json.loads((tmp_path / 'run/run.json').read_text())
    assert record['mei_conformance'] == 'incomplete'
    assert record['ddt']['publication_acceptance'] == 'incomplete'


def test_empty_manifest_is_rejected(tmp_path):
    import importlib.util
    module_spec = importlib.util.spec_from_file_location('ddt_empty_entry', ROOT / 'scripts/validate_corpus.py')
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    empty = tmp_path / 'empty.json'
    empty.write_text('{"works": []}')
    with pytest.raises(SystemExit) as error:
        module.main(['--manifest', str(empty), '--output-dir', str(tmp_path / 'run')])
    assert error.value.code == 2
