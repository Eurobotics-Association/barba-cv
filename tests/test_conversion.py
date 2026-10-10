"""Contract tests for a reviewable 1.0-shaped to 1.3 conversion."""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from convert_v1_0_to_v1_3 import convert  # noqa: E402
from validate import strict_errors  # noqa: E402


class ConversionTests(unittest.TestCase):
    def setUp(self):
        self.source = json.loads((ROOT / 'examples/legacy/barba-cv-1.0-fictional.json').read_text())

    def test_paired_fixture_is_exact_valid_conversion(self):
        before = copy.deepcopy(self.source)
        converted, report = convert(self.source)
        expected = json.loads((ROOT / 'examples/barba-cv-1.3.from-legacy.example.json').read_text())
        saved_report = json.loads((ROOT / 'examples/legacy/barba-cv-1.0-to-1.3.report.json').read_text())
        self.assertEqual(self.source, before)
        self.assertEqual(converted, expected)
        self.assertEqual(report, saved_report)
        self.assertEqual(report['status'], 'converted')
        self.assertEqual(strict_errors(converted), [])
        self.assertEqual(converted['certifications'], before['certifications'])
        self.assertEqual(converted['interests'], before['interests'])
        self.assertEqual(converted['meta']['parsing_errors'], before['parsing_errors'])
        self.assertNotIn('content_language', converted.get('meta', {}))

    def test_ambiguous_and_conflicting_data_blocks_conversion(self):
        alterations = (
            lambda d: d['education'][0].update(school_location='Unknown town'),
            lambda d: d['projects_achievements_extracts'][0].update(synonyms=['guide']),
            lambda d: d.update(project_achievements=[]),
            lambda d: d['personal_info'].update(middle_name='Conflicting'),
            lambda d: d['personal_info']['links'].update(twitter='https://example.org/other'),
            lambda d: d.update(meta={'parsing_errors': ['Other error']}),
            lambda d: d.update(meta=None),
            lambda d: d.update(unknown_legacy_field={'data': 1}),
            lambda d: d.update(barba_cv_version='1.0'),
        )
        for alter in alterations:
            with self.subTest(alter=alter):
                source = copy.deepcopy(self.source)
                alter(source)
                before = copy.deepcopy(source)
                converted, report = convert(source)
                self.assertIsNone(converted)
                self.assertEqual(report['status'], 'blocked')
                self.assertTrue(report['blocked'])
                self.assertEqual(source, before)

    def test_failed_cli_does_not_emit_a_converted_payload(self):
        source = copy.deepcopy(self.source)
        source['education'][0]['school_location'] = 'Unstructured location'
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            source_path = directory / 'source.json'
            output_path = directory / 'output.json'
            report_path = directory / 'report.json'
            source_path.write_text(json.dumps(source))
            run = subprocess.run([sys.executable, str(ROOT / 'tools/convert_v1_0_to_v1_3.py'),
                                  str(source_path), str(output_path), '--report', str(report_path)],
                                 text=True, capture_output=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertFalse(output_path.exists())
            self.assertEqual(json.loads(report_path.read_text())['status'], 'blocked')


if __name__ == '__main__':
    unittest.main()
