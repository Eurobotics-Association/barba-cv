---
title: Version and compatibility
layout: page
permalink: /docs/compatibility/
description: What Barba-CV 1.3 readers and writers can safely assume about legacy data.
---

# Version and compatibility

**Barba-CV v1.3 was released 2026-10-10.** The original 1.0 file is a template, not a validator. The published 1.2 schema has unresolved references and rejects its own template's `extensions`; it cannot certify nested 1.2 payloads. A payload's `barba_cv_version` is evidence of intent, not proof of structural conformance.

| Area | Historical evidence | 1.3 writer | Safe handling |
| --- | --- | --- | --- |
| Version | 1.0 original has none; 1.2 accepts any string in its defective schema | exact `"1.3"` | Validate structure independently; report missing, wrong or conflicting declarations. |
| Skills | 1.0 filled sample and later examples use strings; 1.2 template uses objects | name-bearing objects | Convert a string to a name-only object explicitly; never drop object detail on read or reverse conversion. |
| Education location | 1.0 template uses text; 1.2 template/examples use city/country object | city/country object | A free-text location may not split; retain source and report ambiguity. |
| Project dates and lists | 1.0 template/current examples show structured period and empty arrays; 1.2 template uses text | start/end object, arrays of text | Do not split arbitrary phrases or comma-separated values without source-backed mapping. |
| Project synonyms | 1.0 template/current examples use an empty object; 1.2 template uses text | optional open object | Internal keys and value shapes are unspecified; preserve supplied object data. Do not parse legacy text automatically. |
| Names and omitted fields | 1.0 `Middle_name`, `street2`, `instagram`, `facebook`, `X/twitter`, root `parsing_errors`, `projects_achievements_extracts` | 1.2 canonical names; optional restored ordinary fields | Map only unambiguous aliases; if both old and new keys contain values, report conflict and retain both in the source. Root `parsing_errors` maps to `meta.parsing_errors`; `certifications` and `interests` remain at the root. |
| Extensions | 1.2 template has an object, but published schema rejects it | optional open object | Preserve unknown JSON values on pass-through; core validation does not assign them application meaning. |

A compatibility reader may accept multiple historical shapes, but should label *which shape was observed*. Strict 1.3 output has one shape per defined field. A missing version does not establish 1.0; a sparse payload can match several known shapes. The diagnostic command intentionally reports that ambiguity. It is not a conversion command.

## Explicit, limited normalization helper

`python3 tools/normalize_legacy.py old.json normalized.json` writes a **new file** and leaves the declared version unchanged. It maps nonempty legacy skill strings to name-only objects, `Middle_name` to `middle_name`, and `X/twitter` to `twitter` when the destination key is absent. It also moves a root array of text `parsing_errors` to `meta.parsing_errors` when that destination is absent. If old and new aliases coexist, it retains both and reports a conflict; invalid error-list shapes are retained and reported. It does not split free-text dates, locations, project lists or synonyms; it does not turn a 1.0/1.2 payload into a certified 1.3 payload. Review the output and use strict validation before declaring 1.3.

## Conservative 1.0-shaped to 1.3 conversion

`python3 tools/convert_v1_0_to_v1_3.py old.json new.json --report mapping.json` writes a **new** 1.3 payload only when every included field validates against the 1.3 schema. It never edits the source. Select the input as a 1.0-shaped payload yourself: the missing version field alone does not prove its historical version. The report records mappings, empty values omitted, and blockers without repeating CV values.

The converter applies the alias and skill mappings above, moves `projects_achievements_extracts` to `project_achievements`, and adds `barba_cv_version: "1.3"`. It retains root `certifications` and `interests`, and moves root `parsing_errors` into `meta.parsing_errors`. It omits only an empty text `school_location` or an empty-array project `synonyms`, recording each omission. It does not infer `meta.content_language` or other metadata from the CV. A populated text school location, array/string project synonyms, duplicate old/new keys, unknown schema fields, or any other validation failure blocks output for manual review. A blocked run exits unsuccessfully and can still write its report.

The [fictional 1.0-shaped fixture]({{ '/examples/legacy/barba-cv-1.0-fictional.json' | relative_url }}) and [paired 1.3 fixture]({{ '/examples/barba-cv-1.3.from-legacy.example.json' | relative_url }}) show the complete supported conversion, including its [mapping report]({{ '/examples/legacy/barba-cv-1.0-to-1.3.report.json' | relative_url }}). Both are safe demonstration data, not an individual's CV or a certified original 1.0 release artifact. The 1.3 fixture is useful for renderer integration tests; a renderer's behavior still needs testing in its own project.

**Do not overwrite historical files or retag them.** Explicit conversions should produce a new payload, validate that payload, and report every source field that could not be represented without interpretation. For skills, `"Python"` → `{"name":"Python"}` retains the full source item; for `{"name":"Python","level":"Advanced"}` → `"Python"`, the level is lost, so that reduction is unsafe without a separate destination for the detail.
