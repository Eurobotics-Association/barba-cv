---
title: 1.3 field reference
layout: page
permalink: /docs/field-reference/
description: Field paths, types and meanings in the Barba-CV 1.3 standard.
---

# Barba-CV 1.3 field reference

**Latest release: Barba-CV 1.3 (2026-10-10).** The strict [JSON Schema]({{ '/schema/barba-cv-1.3.schema.json' | relative_url }}) is the machine-readable type contract. This page gives fictional example values and explains meaning and absence/empty/null handling. Examples illustrate types; they are not required defaults. Only `barba_cv_version` is required at the root. Within each skill item, only `name` is required. Every other listed property may be absent.

## Presence and empty values

- **Absent**: no value was supplied or the section is not relevant. Writers should generally omit unknown fields.
- **Empty text `""`**: explicitly present but no text recorded; accepted on text fields, though omit it when possible.
- **Empty array `[]`**: explicitly no recorded items. An empty historical array does not establish its item type.
- **Empty object `{}`**: a present structured section with no populated keys; accepted except a skill item, which requires a name.
- **`null`**: allowed only on the listed `meta` text/boolean/confidence fields. It is not a generic stand-in for missing data.
- Human-readable dates, locations, labels and levels have no imposed country format, date normalization, or controlled vocabulary. Preserve source wording.

## Fields

| Path | Type | Example value | Meaning and 1.x note |
| --- | --- | --- | --- |
| `barba_cv_version` | literal `1.3` | `"1.3"` | Exact payload format declaration. |
| `personal_info` | object | `{"first_name":"Alex"}` | Candidate identity and contact details. |
| `personal_info.first_name` | string | `"Alex"` | Given name. |
| `personal_info.middle_name` | string | `"Jordan"` | Middle name; renamed from 1.0 `Middle_name`. |
| `personal_info.last_name` | string | `"Rivera"` | Family name. |
| `personal_info.date_of_birth` | string | `"1990"` | Birth date as supplied; no date format required. |
| `personal_info.driving_licenses` | array of string | `["B"]` | Licences stated by the source. |
| `personal_info.address` | object | `{"city":"Sample City"}` | Address. |
| `personal_info.address.street` | string | `"10 Example Road"` | Street address line. |
| `personal_info.address.street2` | string | `"Suite 2"` | Optional second address line; restored from 1.0. |
| `personal_info.address.postal_code` | string | `"A1 2BC"` | Postal code as text; no country format required. |
| `personal_info.address.city` | string | `"Sample City"` | Address city. |
| `personal_info.address.country` | string | `"Exampleland"` | Address country. |
| `personal_info.contact` | object | `{"email":"alex@example.org"}` | Contact. |
| `personal_info.contact.email` | string | `"alex@example.org"` | Email address as supplied. |
| `personal_info.contact.phone` | string | `"+1 555 0100"` | Telephone number as supplied. |
| `personal_info.links` | object | `{"website":"https://example.org"}` | Social links as supplied; do not fabricate URLs. |
| `personal_info.links.linkedin` | string | `"https://example.org/alex"` | LinkedIn link. |
| `personal_info.links.github` | string | `"https://example.org/code"` | GitHub link. |
| `personal_info.links.website` | string | `"https://example.org"` | Personal website. |
| `personal_info.links.twitter` | string | `"https://example.org/social"` | X/Twitter link; canonical name since 1.2. |
| `personal_info.links.instagram` | string | `"https://example.org/photos"` | Instagram link; restored from 1.0. |
| `personal_info.links.facebook` | string | `"https://example.org/profile"` | Facebook link; restored from 1.0. |
| `personal_info.links.other_socials` | array (item type open) | `[]` | Legacy list of other social links; item shape remains unspecified. |
| `profile_summary` | string | `"Builds accessible web tools."` | Source-backed summary, in human wording. |
| `position_sought` | array of string | `["Software engineer"]` | Desired roles or positioning statements. |
| `experiences` | array of object | `[{"organization":"Example Cooperative"}]` | Professional experience entries. |
| `experiences[]` | object | `{"organization":"Example Cooperative"}` | One professional experience entry; include only details supported by the source CV. |
| `experiences[].organization` | string | `"Example Cooperative"` | Employer or organization name. |
| `experiences[].role_title` | string | `"Software engineer"` | Role or job title. |
| `experiences[].location` | object | `{"city":"Sample City"}` | Work location when structured parts are known. |
| `experiences[].location.city` | string | `"Sample City"` | Work city. |
| `experiences[].location.country` | string | `"Exampleland"` | Work country. |
| `experiences[].start_date` | string | `"2021"` | Start wording from the source. |
| `experiences[].end_date` | string | `"Present"` | End wording from the source. |
| `experiences[].website` | string | `"https://example.org"` | Organization or role website. |
| `experiences[].logo` | string | `"https://example.org/logo.png"` | Logo reference if supplied. |
| `experiences[].tasks` | array of string | `["Built accessible interfaces."]` | Responsibilities or tasks, one text item each. |
| `experiences[].achievements` | array of string | `["Published a public guide."]` | Achievement statements, one text item each. |
| `education` | array of object | `[{"school":"Example College"}]` | Education entries. |
| `education[]` | object | `{"school":"Example College"}` | One education entry; preserve the institution and qualification wording supplied by the source. |
| `education[].school` | string | `"Example College"` | School or institution. |
| `education[].degree` | string | `"Diploma"` | Qualification or degree. |
| `education[].field` | string | `"Computer science"` | Field of study. |
| `education[].start_date` | string | `"2016"` | Start wording from the source. |
| `education[].end_date` | string | `"2019"` | End wording from the source. |
| `education[].website` | string | `"https://example.org/college"` | Institution website. |
| `education[].logo` | string | `"https://example.org/college.png"` | Logo reference if supplied. |
| `education[].school_location` | object | `{"city":"Sample City"}` | City/country object; older text cannot always be split. |
| `education[].school_location.city` | string | `"Sample City"` | School city. |
| `education[].school_location.country` | string | `"Exampleland"` | School country. |
| `skills` | object | `{"it_skills":[{"name":"Python"}]}` | Three established skill buckets. |
| `skills.it_skills` | array of object | `[{"name":"Python"}]` | IT-related skills. |
| `skills.it_skills[]` | object | `{"name":"Python"}` | Skill object; simple entries need only `name`. |
| `skills.it_skills[].name` | string | `"Python"` | Nonempty source skill label; required when item exists. |
| `skills.it_skills[].level` | string | `"Advanced"` | Source-backed human-readable proficiency; no fixed scale. |
| `skills.it_skills[].category` | string | `"Programming languages"` | Source-backed subcategory within the outer bucket. |
| `skills.it_skills[].keywords` | array of string | `["automation"]` | Source-backed related terms; no inferred aliases. |
| `skills.hard_skills` | array of object | `[{"name":"Technical writing"}]` | Other technical or domain skills. |
| `skills.hard_skills[]` | object | `{"name":"Technical writing"}` | Skill object; simple entries need only `name`. |
| `skills.hard_skills[].name` | string | `"Technical writing"` | Nonempty source skill label; required when item exists. |
| `skills.hard_skills[].level` | string | `"Advanced"` | Source-backed human-readable proficiency; no fixed scale. |
| `skills.hard_skills[].category` | string | `"Source category"` | Source-backed subcategory within the outer bucket. |
| `skills.hard_skills[].keywords` | array of string | `["automation"]` | Source-backed related terms; no inferred aliases. |
| `skills.soft_skills` | array of object | `[{"name":"Mentoring"}]` | Interpersonal or transferable skills. |
| `skills.soft_skills[]` | object | `{"name":"Mentoring"}` | Skill object; simple entries need only `name`. |
| `skills.soft_skills[].name` | string | `"Mentoring"` | Nonempty source skill label; required when item exists. |
| `skills.soft_skills[].level` | string | `"Advanced"` | Source-backed human-readable proficiency; no fixed scale. |
| `skills.soft_skills[].category` | string | `"Source category"` | Source-backed subcategory within the outer bucket. |
| `skills.soft_skills[].keywords` | array of string | `["automation"]` | Source-backed related terms; no inferred aliases. |
| `certifications` | array of object | `[{"name":"Example Certificate"}]` | Certifications or credentials stated in the source CV. |
| `certifications[]` | object | `{"name":"Example Certificate"}` | One certification or credential; fields may be absent when the source does not supply them. |
| `certifications[].name` | string | `"Example Certificate"` | Certification name. |
| `certifications[].issuer` | string | `"Example Institute"` | Issuing organization. |
| `certifications[].date_obtained` | string | `"2022"` | Date wording from the source. |
| `certifications[].expiry_date` | string | `"2027"` | Expiry wording from the source. |
| `certifications[].credential_id` | string | `"DEMO-123"` | Credential identifier. |
| `certifications[].credential_url` | string | `"https://example.org/credential"` | Credential URL. |
| `languages` | array of object | `[{"language":"French"}]` | Language entries. |
| `languages[]` | object | `{"language":"French"}` | One language spoken by the person, with optional source-backed proficiency and certificates. |
| `languages[].language` | string | `"French"` | Language name. |
| `languages[].level` | string | `"Fluent"` | Source-backed proficiency wording. |
| `languages[].certificates` | array (item type open) | `[]` | Legacy list of certificates; item shape remains unspecified. |
| `interests` | array of string | `["Cycling"]` | Personal interests or activities stated in the source CV; remains a root section. |
| `project_achievements` | array of object | `[{"title":"Public data guide"}]` | Projects or achievements described in the CV. |
| `project_achievements[]` | object | `{"title":"Public data guide"}` | One project or achievement entry described in the source CV. |
| `project_achievements[].id` | string | `"project-01"` | Project identifier if supplied. |
| `project_achievements[].service_type` | string | `"Documentation"` | Service or work type. |
| `project_achievements[].client` | string | `"Example Cooperative"` | Client or beneficiary. |
| `project_achievements[].title` | string | `"Public data guide"` | Project title. |
| `project_achievements[].period` | object | `{"start":"2022","end":"2023"}` | Human-readable start/end object; older free text may not split. |
| `project_achievements[].period.start` | string | `"2022"` | Start wording. |
| `project_achievements[].period.end` | string | `"2023"` | End wording. |
| `project_achievements[].role` | array of string | `["Author"]` | One or more role labels. |
| `project_achievements[].sectors` | array of string | `["Education"]` | One or more sector labels. |
| `project_achievements[].competencies` | array of string | `["Technical writing"]` | One or more competency labels. |
| `project_achievements[].keywords` | array of string | `["documentation"]` | One or more source-backed terms. |
| `project_achievements[].description` | string | `"Created a practical guide."` | Project description. |
| `project_achievements[].synonyms` | object | `{}` | Optional open object; internal structure is not standardized. Preserve supplied data. |
| `meta` | object | `{"parsing_errors":[]}` | Processing provenance and diagnostics, not biographical facts. |
| `meta.cv_uuid` | string or null | `"demo-001"` | System-assigned CV identifier, separate from the display title and original filename; UUID syntax is not currently enforced. |
| `meta.cv_title` | string or null | `"Alex Rivera CV"` | User-facing title or label for this CV, supplied by a user or producer; separate from its original filename and system identifier. |
| `meta.content_language` | nonempty string | `"en-GB"` | Likely predominant language of human-readable CV values, preferably a BCP 47 language tag; may be user- or parser-declared. It does not assert that every field has that language or translate values. Omit if unknown. |
| `meta.parsing_errors` | array of string | `[]` | Recorded extraction or mapping diagnostic messages; moved from the 1.0 root. Empty means no errors recorded, not guaranteed extraction accuracy. |
| `meta.ats_processed` | boolean or null | `null` | Whether ATS-oriented processing is known to have occurred. |
| `meta.processor_engine` | string or null | `"example-parser"` | Software or system that produced this structured CV, optionally including its version in the same value; this is the system parser/creator, not a human author. |
| `meta.parsed_at` | string or null | `"2026-10-10"` | Parse timestamp in source/system wording. |
| `meta.source_original_text` | string or null | `"Example source text"` | Original extracted text if retained. |
| `meta.source_ats_revised_text` | string or null | `"Example revised text"` | ATS-oriented revised text if retained. |
| `meta.original_filename` | string or null | `"example-cv.pdf"` | Filename of the document parsed to create this CV data; not the user-facing CV title or system identifier. |
| `meta.source_format` | string or null | `"pdf"` | Source file format. |
| `meta.ingested_at` | string or null | `"2026-10-10"` | Ingestion timestamp. |
| `meta.embedded_at` | string or null | `null` | Embedding timestamp. |
| `meta.extraction_confidence_overall` | number or null | `0.9` | Optional numeric confidence from 0 to 1. |
| `extensions` | object | `{"example.org.reference":"DEMO-001"}` | Adopter-specific data; unknown JSON values preserved on pass-through. |

## Version differences

The [compatibility guide]({{ '/docs/compatibility/' | relative_url }}) details 1.0/1.2 changes and conversion ambiguity. In particular, 1.3 skill items are objects, school locations are objects, project periods are objects, and project role/sectors/competencies/keywords are arrays of text. `synonyms` is an optional open object with no standardized internal keys or values. `other_socials[]` and `languages[].certificates[]` remain open because populated historical evidence does not establish an item contract.

`meta.content_language` differs from `languages[]`: the former describes the likely predominant language of the CV text, while the latter records languages spoken by the person. A renderer may use the content-language hint, but must not assume every field has the same language. `meta.processor_engine` is the one standard software parser/creator field; no separate `system_parser_creator` key is defined.

The standard describes CV data and processing metadata. A consuming application may impose stricter requirements but should identify those as its own profile.
