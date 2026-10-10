#!/usr/bin/env python3
"""Explicit, non-destructive legacy alias/skill normalization; does not upgrade a payload version."""
import argparse
import copy
import json
from pathlib import Path


def normalize(data):
    out = copy.deepcopy(data)
    report = []
    if not isinstance(out, dict):
        return out, ['root is not an object']
    if 'parsing_errors' in out:
        legacy_errors = out['parsing_errors']
        meta = out.get('meta')
        if 'meta' in out and not isinstance(meta, dict):
            report.append('conflict: root parsing_errors cannot move because meta is not an object; retained source')
        elif isinstance(meta, dict) and 'parsing_errors' in meta:
            report.append('conflict: root and meta.parsing_errors coexist; retained both')
        elif not isinstance(legacy_errors, list) or not all(isinstance(item, str) for item in legacy_errors):
            report.append('root parsing_errors is not an array of text; retained source')
        else:
            if meta is None:
                meta = {}
                out['meta'] = meta
            meta['parsing_errors'] = out.pop('parsing_errors')
            report.append('mapped root parsing_errors to meta.parsing_errors')
    info = out.get('personal_info')
    if isinstance(info, dict):
        if 'Middle_name' in info:
            if 'middle_name' in info:
                report.append('conflict: personal_info.Middle_name and middle_name coexist; retained both')
            else:
                info['middle_name'] = info.pop('Middle_name')
                report.append('mapped personal_info.Middle_name to middle_name')
        links = info.get('links')
        if isinstance(links, dict) and 'X/twitter' in links:
            if 'twitter' in links:
                report.append('conflict: X/twitter and twitter coexist; retained both')
            else:
                links['twitter'] = links.pop('X/twitter')
                report.append('mapped personal_info.links.X/twitter to twitter')
    skills = out.get('skills')
    if isinstance(skills, dict):
        for bucket in ('it_skills', 'hard_skills', 'soft_skills'):
            items = skills.get(bucket)
            if not isinstance(items, list):
                continue
            for i, item in enumerate(items):
                if isinstance(item, str) and item:
                    items[i] = {'name': item}
                    report.append(f'mapped skills.{bucket}[{i}] string to name-only object')
                elif isinstance(item, str):
                    report.append(f'empty skills.{bucket}[{i}] string retained; cannot create a valid 1.3 skill')
    return out, report


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source', type=Path)
    ap.add_argument('output', type=Path)
    args = ap.parse_args()
    if args.source.resolve() == args.output.resolve():
        ap.error('output must differ from source')
    data = json.loads(args.source.read_text())
    result, report = normalize(data)
    if args.output.exists():
        ap.error('output exists; choose a new file')
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print('\n'.join(report) if report else 'No changes')
    print('Version declaration retained. Validate and review all other fields before emitting a 1.3 payload.')


if __name__ == '__main__':
    main()
