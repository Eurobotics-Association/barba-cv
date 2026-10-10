---
title: Get started with 1.3
layout: page
permalink: /docs/getting-started/
description: Build and validate a Barba-CV 1.3 JSON payload.
---

# Get started with Barba-CV 1.3

**Latest release: [Barba-CV v1.3](https://github.com/Eurobotics-Association/barba-cv/releases/tag/v1.3), published 2026-10-10.** The [published 1.2 artifacts]({{ '/history/' | relative_url }}) remain available unchanged. Use the versioned 1.3 schema path for strict 1.3 validation.

## 1. Start small

Only `barba_cv_version` is required. Add CV sections as the source supports them:

```json
{
  "barba_cv_version": "1.3",
  "personal_info": {"first_name": "Alex", "last_name": "Rivera"},
  "skills": {"it_skills": [{"name": "Python"}]}
}
```

A more detailed, entirely fictional [example]({{ '/examples/barba-cv-1.3.example.json' | relative_url }}) and an [empty-section template]({{ '/examples/barba-cv-1.3.template.json' | relative_url }}) are available. Template placeholders are not mandatory payload fields. Do not copy empty skill objects merely to fill the template.

## 2. Add skill detail only from evidence

A skill item is an object with a nonempty `name`. `level`, `category`, and `keywords` are optional. Keep the human wording of a proficiency level; no numeric scale or taxonomy is required. `category` refines the outer `it_skills`, `hard_skills`, or `soft_skills` bucket. `keywords` holds source-backed related labels or search terms, not invented aliases. If evidence supplies only a name, write only `name`.

```json
{"it_skills": [
  {"name": "SQL"},
  {"name": "Python", "level": "Advanced", "category": "Programming languages", "keywords": ["automation"]}
]}
```

Historical string items such as `"SQL"` can be represented **losslessly** as `{"name":"SQL"}` in an explicit conversion. An older consumer that expects strings will need an update to read 1.3 skill items; projecting an enriched object back to a string discards detail and must not happen silently.

## 3. Validate the right version

Use [the 1.3 JSON Schema]({{ '/schema/barba-cv-1.3.schema.json' | relative_url }}) for strict 1.3 payload validation. For a local Python check, install the development dependency with `python3 -m pip install -r requirements-dev.txt`, then run:

```sh
python3 tools/validate.py examples/barba-cv-1.3.example.json
python3 tools/validate.py --diagnose path/to/cv.json
```

Strict mode requires the exact `"1.3"` declaration. Diagnostic mode reports the declaration separately from observed structural clues; it does not alter the input or certify historical 1.0/1.2 conformance. The [field reference]({{ '/docs/field-reference/' | relative_url }}) and [compatibility guide]({{ '/docs/compatibility/' | relative_url }}) describe every field and migration uncertainty.

## 4. Preserve source meaning

Keep dates, names, levels and locations as supplied. Omit unknown fields rather than guessing. Empty text means a known field has no value recorded; `[]` is an explicitly empty list; `null` is allowed only where the schema lists it. `extensions` is optional adopter-specific data; preserve unknown extension values on pass-through. Do not place standard CV information there to avoid the common fields.

## 5. Record optional processing context

`meta.cv_title` is a user-facing label for this CV. It is separate from `meta.original_filename`, the name of the document parsed, and `meta.cv_uuid`, an identifier assigned by a system. `meta.processor_engine` identifies the software or system that produced the structured CV; it is also the system parser/creator field. If useful, include that software's version in the same value. These fields are optional.

`meta.content_language` is the likely predominant language of the human-readable CV values. Prefer a language tag such as `en` or `en-GB`; omit it when unknown. It may reflect a user's declaration or a parser's assessment. It differs from root `languages`, which records languages spoken by the person. The hint does not guarantee that every field is in the same language and does not request translation.

```json
{
  "barba_cv_version": "1.3",
  "meta": {
    "cv_uuid": "demo-001",
    "cv_title": "Alex Rivera Software Engineer CV",
    "content_language": "en",
    "original_filename": "alex-rivera-source.pdf",
    "processor_engine": "example-parser 1.0",
    "parsed_at": "2026-10-10T09:00:00Z",
    "parsing_errors": []
  }
}
```

`parsing_errors: []` means no diagnostics were recorded, not that extraction was proven perfect. The original 1.0 placement was at the root; 1.3 stores it under `meta`. Root `certifications` and `interests` remain available for ordinary CV content.
