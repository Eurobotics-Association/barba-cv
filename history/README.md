# Historical Barba-CV versions

This archive preserves the evidence for earlier versions of the open Barba-CV standard. Historical files remain available for reference, compatibility work and the development of version-aware validators. They are not silently rewritten when the standard evolves.

## Version inventory

| Version | Preserved artifact | Source and status |
| --- | --- | --- |
| 1.0 | [Original generic CV JSON template](1.0/Barba-cv-schema-1.0_generic-cv_json_template_20251203.json) | Supplied by Robert Vergnes on 2026-10-10 as the original 1.0 reference. Its filename carries the date 2025-12-03; that date is not independently verified as a release date. |
| 1.2 | [Published JSON Schema](1.2/barba-cv.schema.json) | Exact copy of `schema/barba-cv.schema.json` at release tag `v1.2`. Known incomplete validation definitions are preserved. |
| 1.2 | [Published generic CV JSON template](1.2/barba-cv.template.json) | Exact copy of `examples/barba-cv.template.json` at release tag `v1.2`. |

All three artifacts were archived on 2026-10-10. No 1.1 artifact or historical 1.0 release tag is asserted by this inventory. Further recovered sources should be added with their own provenance.

## Provenance

### Version 1.0

- Original filename: `Barba-cv-schema-1.0_generic-cv_json_template_20251203.json`.
- Source: original file supplied by the maintainer; version identification is based on that provenance and filename. The payload has no `barba_cv_version` field.
- Preserved size: 1,720 bytes. Its SHA-256 is recorded in [SHA256SUMS](SHA256SUMS).
- The original filename uses the word "schema". Technically, this artifact is a CV JSON template containing example empty values, not an executable JSON Schema validation document. It is evidence for the original data structure.
- Key spelling, casing and shape are preserved, including `Middle_name`, `street2`, `X/twitter`, a text `school_location`, `projects_achievements_extracts`, and root-level `parsing_errors`.
- Empty arrays do not establish the intended type of their future items. Additional representative 1.0 payloads may be needed to reconstruct validation rules accurately.

### Version 1.2

- Source release: [v1.2](https://github.com/Eurobotics-Association/barba-cv/releases/tag/v1.2).
- Source commit: `e00c9c781a20875e95a12d6faeb0bd0065cf58b9`.
- [Schema source](https://github.com/Eurobotics-Association/barba-cv/blob/e00c9c781a20875e95a12d6faeb0bd0065cf58b9/schema/barba-cv.schema.json), Git blob `89c15f41275bb070f54dbe87812c3f402168b2f0`.
- [Template source](https://github.com/Eurobotics-Association/barba-cv/blob/e00c9c781a20875e95a12d6faeb0bd0065cf58b9/examples/barba-cv.template.json), Git blob `a02d3b0f335aeddd084a0638b7b3a00f89faedfa`.
- Known limitations: the schema references eight missing `$defs` definitions; it does not declare `extensions` despite the template including it and the root forbidding additional properties. Its version field accepts any string. These defects have not been repaired in the archived copy.
- The published template and other example CVs also differ in some field types. Their compatibility must be reviewed before defining future validation or conversion rules.

## Integrity and future evolution

Run from the repository root:

```sh
sha256sum -c history/SHA256SUMS
```

The checksums cover the original bytes of the archived artifacts. They establish integrity, not semantic correctness or conformance.

Keep originals unchanged. Add corrections, derived validation schemas and new versions separately, documenting their relationship to these sources. Update this index and append checksums for newly archived artifacts. Do not use a newer schema to replace an older archived file or retag an existing release.

Preserve each current schema and template before an approved evolution replaces it, unless an identical version is already archived. Consumers should be able to retrieve an earlier reference without searching Git history. See [AGENTS.md](../AGENTS.md) for repository preservation instructions.
