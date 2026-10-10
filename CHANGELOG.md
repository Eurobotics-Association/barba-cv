# Changelog

## [v1.3] — 2026-10-10

Barba-CV 1.3 is the latest release of the open CV data standard. The [versioned JSON Schema](schema/barba-cv-1.3.schema.json), [field reference](docs/field-reference.md), [getting-started guide](docs/getting-started.md), and [compatibility guide](docs/compatibility.md) define this release. The release tag records its exact Git commit and publication timestamp.

- Added a strict 1.3 validator with an exact `barba_cv_version` declaration and optional, open `extensions`.
- Standardized skill items as objects with a required nonempty `name` and optional `level`, `category`, and `keywords`; source-backed detail can be preserved.
- Clarified structured education locations and project fields, while documenting cases where older free text cannot be converted without interpretation.
- Kept `certifications` and `interests` at the root; placed extraction diagnostics in `meta.parsing_errors` and provided a conflict-aware legacy mapping helper.
- Clarified `cv_title`, `cv_uuid`, `original_filename`, and the single software parser/creator field `processor_engine`; added optional `meta.content_language` for the likely predominant language of human-readable CV values.
- Added inline schema descriptions, a populated fictional example, field guidance, version-aware diagnostics, and historical provenance.

Only `barba_cv_version` is required at the root. The 1.0 template and published 1.2 artifacts remain unchanged in [`history/`](history/). The published 1.2 schema contains unresolved references; use the versioned 1.3 schema for strict 1.3 validation. Historical input requires explicit review before it can be emitted as a conforming 1.3 payload.

The SchemaStore catalog entry still points to the unversioned 1.2 schema. Its update is planned separately; use the 1.3 URL above until then.

## [v1.2] — 2026-03-17

Initial public Barba-CV release. The exact published schema and template are preserved in [`history/1.2/`](history/1.2/).

[v1.3]: https://github.com/Eurobotics-Association/barba-cv/releases/tag/v1.3
[v1.2]: https://github.com/Eurobotics-Association/barba-cv/releases/tag/v1.2
