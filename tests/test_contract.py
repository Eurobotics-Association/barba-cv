import copy
import json
from pathlib import Path
import sys
import unittest

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from validate import diagnostics, strict_errors  # noqa: E402
from normalize_legacy import normalize  # noqa: E402


class ContractTests(unittest.TestCase):
    def test_archived_bytes(self):
        import subprocess
        result = subprocess.run(['sha256sum', '-c', 'history/SHA256SUMS'], cwd=ROOT,
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_schema_and_examples(self):
        schema = json.loads((ROOT / 'schema/barba-cv-1.3.schema.json').read_text())
        Draft202012Validator.check_schema(schema)
        self.assertNotIn('$ref', json.dumps(schema))
        for name in ('barba-cv-1.3.template.json', 'barba-cv-1.3.example.json'):
            data = json.loads((ROOT / 'examples' / name).read_text())
            self.assertEqual(strict_errors(data), [], name)

    def test_field_reference_examples(self):
        import re
        schema = json.loads((ROOT / 'schema/barba-cv-1.3.schema.json').read_text())
        reference = (ROOT / 'docs/field-reference.md').read_text()
        rows = re.findall(r'^\| \x60([^\x60]+)\x60 \| [^|]+ \| \x60(.*?)\x60 \|', reference, re.M)
        self.assertGreater(len(rows), 100)
        for path, raw in rows:
            node = schema
            for part in path.split('.'):
                is_item = part.endswith('[]')
                key = part[:-2] if is_item else part
                node = node['properties'][key]
                if is_item:
                    node = node['items']
            value = json.loads(raw)
            self.assertEqual(list(Draft202012Validator(node).iter_errors(value)), [], path)

    def test_inline_descriptions_match_field_reference(self):
        import re
        schema = json.loads((ROOT / 'schema/barba-cv-1.3.schema.json').read_text())
        reference = (ROOT / 'docs/field-reference.md').read_text()
        rows = re.findall(r'^\| `([^`]+)` \| [^|]+ \| `.*?` \| (.*?) \|$', reference, re.M)
        self.assertGreater(len(rows), 110)
        documented = {path for path, _ in rows}
        for path, meaning in rows:
            node = schema
            for part in path.split('.'):
                is_item = part.endswith('[]')
                node = node['properties'][part[:-2] if is_item else part]
                if is_item:
                    node = node['items']
            self.assertEqual(node.get('description'), meaning.strip(), path)
        self.assertTrue(schema.get('description'))

        def require_documented_properties(node, prefix=''):
            for key, child in node.get('properties', {}).items():
                path = f'{prefix}.{key}' if prefix else key
                self.assertIn(path, documented)
                self.assertTrue(child.get('description'), path)
                items = child.get('items')
                if isinstance(items, dict) and items.get('properties'):
                    item_path = path + '[]'
                    self.assertIn(item_path, documented)
                    self.assertTrue(items.get('description'), item_path)
                    require_documented_properties(items, item_path)
                require_documented_properties(child, path)

        require_documented_properties(schema)

    def test_metadata_and_retained_sections(self):
        schema = json.loads((ROOT / 'schema/barba-cv-1.3.schema.json').read_text())
        self.assertIn('certifications', schema['properties'])
        self.assertIn('interests', schema['properties'])
        self.assertNotIn('parsing_errors', schema['properties'])
        meta = schema['properties']['meta']['properties']
        self.assertIn('parsing_errors', meta)
        self.assertIn('processor_engine', meta)
        self.assertNotIn('system_parser_creator', meta)
        self.assertNotIn('created_by', meta)
        self.assertNotIn('content_language', schema['required'])
        payload = {'barba_cv_version': '1.3', 'certifications': [{'name': 'Example'}],
                   'interests': ['Cycling'], 'meta': {'content_language': 'en-GB',
                   'cv_title': 'Example CV', 'original_filename': 'source.pdf',
                   'cv_uuid': 'demo-001', 'processor_engine': 'example-parser 1.0',
                   'parsing_errors': []}}
        self.assertEqual(strict_errors(payload), [])
        payload['meta']['content_language'] = ''
        self.assertTrue(strict_errors(payload))
        payload['meta'].pop('content_language')
        self.assertEqual(strict_errors(payload), [])

    def test_skills_and_extensions(self):
        item = {'barba_cv_version': '1.3', 'skills': {'it_skills': [{'name': 'Python'}]},
                'extensions': {'vendor.example': {'unknown': [1, None, True]}}}
        self.assertEqual(strict_errors(item), [])
        item['skills']['it_skills'] = ['Python']
        self.assertTrue(strict_errors(item))
        item['skills']['it_skills'] = [{'name': 'Python', 'level': 'Advanced'}]
        self.assertEqual(strict_errors(item), [])
        item['skills']['it_skills'] = [{'name': ''}]
        self.assertTrue(strict_errors(item))

    def test_version_and_legacy_ambiguity(self):
        self.assertTrue(strict_errors({'barba_cv_version': '1.2'}))
        self.assertTrue(strict_errors({}))
        diagnosis = diagnostics({})
        self.assertTrue(diagnosis['ambiguous'])
        self.assertIsNone(diagnosis['declared_version'])
        legacy = {'skills': {'it_skills': ['Python']}}
        self.assertIn('1.0 template shape', diagnostics(legacy)['plausible_shapes'])
        self.assertNotIn('1.3 release shape', diagnostics(legacy)['plausible_shapes'])

    def test_alias_conflicts_and_nonmutation(self):
        original = {'personal_info': {'links': {'X/twitter': 'old', 'twitter': 'new'}},
                    'skills': {'it_skills': ['Python', {'name': 'SQL', 'level': 'Expert'}]}}
        before = copy.deepcopy(original)
        normalized, report = normalize(original)
        self.assertEqual(original, before)
        self.assertEqual(normalized['personal_info']['links'], before['personal_info']['links'])
        self.assertTrue(any('conflict' in line for line in report))
        self.assertEqual(normalized['skills']['it_skills'][0], {'name': 'Python'})
        self.assertEqual(normalized['skills']['it_skills'][1], before['skills']['it_skills'][1])
        self.assertEqual(original, before)
        self.assertEqual(diagnostics(original)['declared_version'], None)
        self.assertEqual(original, before)
        mapped, report = normalize({'personal_info': {'links': {'X/twitter': 'old'}}})
        self.assertEqual(mapped['personal_info']['links']['twitter'], 'old')
        self.assertNotIn('X/twitter', mapped['personal_info']['links'])

    def test_legacy_parsing_errors_mapping_and_conflicts(self):
        source = {'parsing_errors': ['Could not read a date'], 'interests': ['Cycling'],
                  'certifications': [{'name': 'Example'}]}
        before = copy.deepcopy(source)
        mapped, report = normalize(source)
        self.assertEqual(source, before)
        self.assertEqual(mapped['meta']['parsing_errors'], before['parsing_errors'])
        self.assertNotIn('parsing_errors', mapped)
        self.assertEqual(mapped['interests'], before['interests'])
        self.assertEqual(mapped['certifications'], before['certifications'])
        self.assertTrue(any('mapped root parsing_errors' in line for line in report))
        conflict = {'parsing_errors': ['old'], 'meta': {'parsing_errors': ['new']}}
        result, report = normalize(conflict)
        self.assertEqual(result, conflict)
        self.assertTrue(any('conflict' in line for line in report))
        malformed = {'parsing_errors': [{'message': 'old'}]}
        result, report = normalize(malformed)
        self.assertEqual(result, malformed)
        self.assertTrue(any('not an array of text' in line for line in report))

    def test_invalid_nested_types(self):
        bad = {'barba_cv_version': '1.3', 'education': [{'school_location': 'Paris'}]}
        self.assertTrue(strict_errors(bad))
        bad = {'barba_cv_version': '1.3', 'project_achievements': [{'period': '2020-2022'}]}
        self.assertTrue(strict_errors(bad))
        bad = {'barba_cv_version': '1.3', 'extensions': []}
        self.assertTrue(strict_errors(bad))
        bad = {'barba_cv_version': '1.3', 'unrecognized': 'value'}
        self.assertTrue(strict_errors(bad))


if __name__ == '__main__':
    unittest.main()
