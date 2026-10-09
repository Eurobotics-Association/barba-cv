#!/usr/bin/env python3
"""Strict Barba-CV 1.3 validation and conservative historical-shape diagnostics."""
import argparse
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / 'schema/barba-cv-1.3.schema.json').read_text())
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = Draft202012Validator(SCHEMA)


def strict_errors(data):
    return sorted(VALIDATOR.iter_errors(data), key=lambda e: (list(map(str, e.path)), e.message))


def diagnostics(data):
    """Report clues, not historical schema conformance. Never modifies data."""
    if not isinstance(data, dict):
        return {'declared_version': None, 'strict_1_3_valid': False,
                'plausible_shapes': [], 'ambiguous': False,
                'observations': ['root must be an object']}
    observations = []
    declared = data.get('barba_cv_version')
    if declared is None:
        observations.append('missing version declaration does not prove 1.0')
    elif declared not in ('1.2', '1.3'):
        observations.append(f'unsupported declared version: {declared!r}')
    candidates = {'1.0 template shape', '1.2 template shape', '1.2 examples shape', '1.3 candidate shape'}
    if declared is not None:
        candidates.discard('1.0 template shape')
    if declared == '1.3':
        candidates.discard('1.2 template shape')
        candidates.discard('1.2 examples shape')
    if declared == '1.2':
        candidates.discard('1.3 candidate shape')
    if 'Middle_name' in data.get('personal_info', {}):
        candidates -= {'1.2 template shape', '1.2 examples shape', '1.3 candidate shape'}
        observations.append('personal_info.Middle_name is a 1.0 spelling')
    if 'parsing_errors' in data:
        candidates -= {'1.2 template shape', '1.2 examples shape', '1.3 candidate shape'}
        observations.append('root parsing_errors is a 1.0 placement')
    for i, entry in enumerate(data.get('education', []) if isinstance(data.get('education', []), list) else []):
        if not isinstance(entry, dict):
            observations.append(f'education[{i}] is not an object')
            continue
        loc = entry.get('school_location')
        if isinstance(loc, str):
            candidates -= {'1.2 template shape', '1.2 examples shape', '1.3 candidate shape'}
            observations.append(f'education[{i}].school_location is legacy text; splitting may lose meaning')
        elif isinstance(loc, dict):
            candidates.discard('1.0 template shape')
    skills = data.get('skills', {})
    if isinstance(skills, dict):
        for bucket in ('it_skills', 'hard_skills', 'soft_skills'):
            items = skills.get(bucket, [])
            if not isinstance(items, list):
                observations.append(f'skills.{bucket} is not an array')
                continue
            for i, item in enumerate(items):
                if isinstance(item, str):
                    candidates -= {'1.2 template shape', '1.3 candidate shape'}
                    observations.append(f'skills.{bucket}[{i}] is a legacy string; explicit name-only mapping is lossless')
                elif isinstance(item, dict):
                    candidates.discard('1.2 examples shape')
                else:
                    observations.append(f'skills.{bucket}[{i}] has unsupported item type')
    for key in ('project_achievements', 'projects_achievements_extracts'):
        projects = data.get(key, [])
        if key == 'projects_achievements_extracts' and key in data:
            candidates -= {'1.2 template shape', '1.2 examples shape', '1.3 candidate shape'}
            observations.append('projects_achievements_extracts is a 1.0 key')
        if not isinstance(projects, list):
            continue
        for i, item in enumerate(projects):
            if not isinstance(item, dict):
                continue
            period = item.get('period')
            if isinstance(period, str):
                candidates -= {'1.0 template shape', '1.2 examples shape', '1.3 candidate shape'}
                observations.append(f'{key}[{i}].period is free text; splitting may be ambiguous')
            elif isinstance(period, dict):
                candidates.discard('1.2 template shape')
    if isinstance(data.get('personal_info'), dict):
        links = data['personal_info'].get('links', {})
        if isinstance(links, dict) and 'X/twitter' in links:
            observations.append('legacy X/twitter present; map to twitter only if absent, otherwise report conflict')
            if 'twitter' in links:
                observations.append('X/twitter and twitter coexist: alias conflict requires review')
    errors = strict_errors(data)
    if errors:
        candidates.discard('1.3 candidate shape')
    if not candidates:
        observations.append('no known shape fits observed clues; historical checks are incomplete')
    return {'declared_version': declared, 'strict_1_3_valid': not errors,
            'plausible_shapes': sorted(candidates), 'ambiguous': len(candidates) > 1,
            'observations': observations,
            'strict_1_3_errors': [{'path': '/'.join(map(str, e.absolute_path)), 'message': e.message} for e in errors]}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('file', type=Path)
    ap.add_argument('--diagnose', action='store_true', help='show non-mutating structural clues; not historical conformance')
    args = ap.parse_args()
    try:
        data = json.loads(args.file.read_text())
    except (OSError, ValueError) as e:
        print(f'Could not read JSON: {e}', file=sys.stderr)
        return 2
    if args.diagnose:
        print(json.dumps(diagnostics(data), indent=2, ensure_ascii=False))
        return 0
    errors = strict_errors(data)
    if errors:
        for e in errors:
            print(f"/{'/'.join(map(str, e.absolute_path))}: {e.message}", file=sys.stderr)
        return 1
    print('Valid Barba-CV 1.3 candidate payload')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
