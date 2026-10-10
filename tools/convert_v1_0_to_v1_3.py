#!/usr/bin/env python3
"""Explicitly convert supported, operator-identified 1.0-shaped CV data to 1.3.

This is a conservative data conversion, not proof that arbitrary undeclared JSON is
historical Barba-CV 1.0. It refuses fields that cannot be represented faithfully.
"""

import argparse
import json
from pathlib import Path

from normalize_legacy import normalize
from validate import strict_errors


def convert(data):
    """Return (new_payload_or_none, report) without changing the source object."""
    report = {'source_profile': 'operator-selected 1.0-shaped payload',
              'mappings': [], 'omitted_empty': [], 'blocked': []}
    if not isinstance(data, dict):
        report['blocked'].append('root is not an object')
        report['status'] = 'blocked'
        return None, report
    if 'barba_cv_version' in data:
        report['blocked'].append('input already declares a version; do not retag it as 1.0')
        report['status'] = 'blocked'
        return None, report

    out, notes = normalize(data)
    for note in notes:
        if note.startswith('mapped '):
            report['mappings'].append(note)
        else:
            report['blocked'].append(note)

    old_projects = 'projects_achievements_extracts'
    if old_projects in out:
        if 'project_achievements' in out:
            report['blocked'].append('both legacy and 1.3 project root keys coexist')
        elif not isinstance(out[old_projects], list):
            report['blocked'].append('legacy project root is not an array')
        else:
            out['project_achievements'] = out.pop(old_projects)
            report['mappings'].append('mapped projects_achievements_extracts to project_achievements')

    education = out.get('education', [])
    if isinstance(education, list):
        for i, item in enumerate(education):
            if not isinstance(item, dict) or 'school_location' not in item:
                continue
            location = item['school_location']
            if location == '':
                item.pop('school_location')
                report['omitted_empty'].append(f'education[{i}].school_location: empty legacy text')
            elif isinstance(location, str):
                report['blocked'].append(f'education[{i}].school_location: populated text needs a reviewed city/country mapping')

    projects = out.get('project_achievements', [])
    if isinstance(projects, list):
        for i, item in enumerate(projects):
            if not isinstance(item, dict) or 'synonyms' not in item:
                continue
            synonyms = item['synonyms']
            if synonyms == []:
                item.pop('synonyms')
                report['omitted_empty'].append(f'project_achievements[{i}].synonyms: empty legacy array')
            elif not isinstance(synonyms, dict):
                report['blocked'].append(f'project_achievements[{i}].synonyms: non-object content needs review')

    out['barba_cv_version'] = '1.3'
    for error in strict_errors(out):
        path = '/'.join(map(str, error.absolute_path)) or '<root>'
        report['blocked'].append(f'{path}: 1.3 {error.validator} validation failed')

    report['status'] = 'blocked' if report['blocked'] else 'converted'
    return (None if report['blocked'] else out), report


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source', type=Path, help='operator-identified 1.0-shaped JSON input')
    ap.add_argument('output', type=Path, help='new, validated 1.3 JSON output')
    ap.add_argument('--report', type=Path, help='optional new JSON mapping report')
    args = ap.parse_args()
    source = args.source.resolve()
    output = args.output.resolve()
    report_path = args.report.resolve() if args.report else None
    if source == output or (report_path and report_path in (source, output)):
        ap.error('source, output and report paths must differ')
    if args.output.exists() or (args.report and args.report.exists()):
        ap.error('output or report already exists; choose new paths')
    try:
        data = json.loads(args.source.read_text())
    except (OSError, ValueError) as exc:
        ap.error(f'could not read source JSON: {exc}')
    result, report = convert(data)
    report_json = json.dumps(report, indent=2, ensure_ascii=False) + '\n'
    if args.report:
        args.report.write_text(report_json)
    print(report_json, end='')
    if result is None:
        return 1
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
