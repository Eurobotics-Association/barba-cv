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
        self.assertNotIn('1.3 candidate shape', diagnostics(legacy)['plausible_shapes'])

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
