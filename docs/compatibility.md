---
title: Version and compatibility
layout: page
permalink: /docs/compatibility/
description: What Barba-CV 1.3 readers and writers can safely assume about legacy data.
---

# Version and compatibility

**1.3 is a candidate contract, not a tagged release.** The original 1.0 file is a template, not a validator. The published 1.2 schema has unresolved references and rejects its own template's `extensions`; it cannot certify nested 1.2 payloads. A payload's `barba_cv_version` is evidence of intent, not proof of structural conformance.

| Area | Historical evidence | 1.3 writer | Safe handling |
| --- | --- | --- | --- |
| Version | 1.0 original has none; 1.2 accepts any string in its defective schema | exact `"1.3"` | Validate structure independently; report missing, wrong or conflicting declarations. |
| Skills | 1.0 filled sample and later examples use strings; 1.2 template uses objects | name-bearing objects | Convert a string to a name-only object explicitly; never drop object detail on read or reverse conversion. |
| Education location | 1.0 template uses text; 1.2 template/examples use city/country object | city/country object | A free-text location may not split; retain source and report ambiguity. |
| Project dates and lists | 1.0 template/current examples show structured period and empty arrays; 1.2 template uses text | start/end object, arrays of text | Do not split arbitrary phrases or comma-separated values without source-backed mapping. |
| Project synonyms | 1.0 template/current examples use an empty object; 1.2 template uses text | optional open object | Internal keys and value shapes are unspecified; preserve supplied object data. Do not parse legacy text automatically. |
| Names and omitted fields | 1.0 `Middle_name`, `street2`, `instagram`, `facebook`, `X/twitter`, root `parsing_errors`, `projects_achievements_extracts` | 1.2 canonical names; optional restored ordinary fields | Map only unambiguous aliases; if both old and new keys contain values, report conflict and retain both in the source. |
| Extensions | 1.2 template has an object, but published schema rejects it | optional open object | Preserve unknown JSON values on pass-through; core validation does not assign them application meaning. |

A compatibility reader may accept multiple historical shapes, but should label *which shape was observed*. Strict 1.3 output has one shape per defined field. A missing version does not establish 1.0; a sparse payload can match several known shapes. The diagnostic command intentionally reports that ambiguity. It is not a conversion command.

## Explicit, limited normalization helper

`python3 tools/normalize_legacy.py old.json normalized.json` writes a **new file** and leaves the declared version unchanged. It maps nonempty legacy skill strings to name-only objects, `Middle_name` to `middle_name`, and `X/twitter` to `twitter` when the destination key is absent. If old and new aliases coexist, it retains both and reports a conflict. It does not split free-text dates, locations, project lists or synonyms; it does not turn a 1.0/1.2 payload into a certified 1.3 payload. Review the output and use strict validation before declaring 1.3.

**Do not overwrite historical files or retag them.** Explicit conversions should produce a new payload, validate that payload, and report every source field that could not be represented without interpretation. For skills, `"Python"` → `{"name":"Python"}` retains the full source item; for `{"name":"Python","level":"Advanced"}` → `"Python"`, the level is lost, so that reduction is unsafe without a separate destination for the detail.
