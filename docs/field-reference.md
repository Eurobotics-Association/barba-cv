---
title: 1.3 field reference
layout: page
permalink: /docs/field-reference/
description: Field paths and data types in the Barba-CV 1.3 candidate standard.
---

# Barba-CV 1.3 field reference

**Status: candidate contract; no 1.3 release tag.** The strict [JSON Schema]({{ '/schema/barba-cv-1.3.schema.json' | relative_url }}) is the machine-readable type contract. This page explains meaning and absence/empty/null handling. Only `barba_cv_version` is required at the root. Within each skill item, only `name` is required. Every other listed property may be absent.

## Presence and empty values

- **Absent**: no value was supplied or the section is not relevant. Writers should generally omit unknown fields.
- **Empty text `""`**: explicitly present but no text recorded; accepted on text fields, though omit it when possible.
- **Empty array `[]`**: explicitly no recorded items. An empty historical array does not establish its item type.
- **Empty object `{}`**: a present structured section with no populated keys; accepted except a skill item, which requires a name.
- **`null`**: allowed only on the listed `meta` text/boolean/confidence fields. It is not a generic stand-in for missing data.
- Human-readable dates, locations, labels and levels have no imposed country format, date normalization, or controlled vocabulary. Preserve source wording.

## Fields

| Path | Type | Meaning and 1.x note |
| --- | --- | --- |
| `barba_cv_version` | literal `1.3` | Exact payload format declaration. |
| `personal_info` | object | Candidate identity and contact details. |
| `personal_info.first_name` | string | Given name. |
| `personal_info.middle_name` | string | Middle name; renamed from 1.0 `Middle_name`. |
| `personal_info.last_name` | string | Family name. |
| `personal_info.date_of_birth` | string | Birth date as supplied; no date format required. |
| `personal_info.driving_licenses` | array of string | Licences stated by the source. |
| `personal_info.address` | object | Address. |
| `personal_info.address.street` | string | Street address line. |
| `personal_info.address.street2` | string | Optional second address line; restored from 1.0. |
| `personal_info.address.postal_code` | string | Postal code as text; no country format required. |
| `personal_info.address.city` | string | Address city. |
| `personal_info.address.country` | string | Address country. |
| `personal_info.contact` | object | Contact. |
| `personal_info.contact.email` | string | Email address as supplied. |
| `personal_info.contact.phone` | string | Telephone number as supplied. |
| `personal_info.links` | object | Social links as supplied; do not fabricate URLs. |
| `personal_info.links.linkedin` | string | LinkedIn link. |
| `personal_info.links.github` | string | GitHub link. |
| `personal_info.links.website` | string | Personal website. |
| `personal_info.links.twitter` | string | X/Twitter link; canonical name since 1.2. |
| `personal_info.links.instagram` | string | Instagram link; restored from 1.0. |
| `personal_info.links.facebook` | string | Facebook link; restored from 1.0. |
| `personal_info.links.other_socials` | array (item type open) | Legacy list of other social links; item shape remains unspecified. |
| `profile_summary` | string | Source-backed summary, in human wording. |
| `position_sought` | array of string | Desired roles or positioning statements. |
| `experiences` | array of object | Professional experience entries. |
| `experiences[]` | object | Experiences[]. |
| `experiences[].organization` | string | Employer or organization name. |
| `experiences[].role_title` | string | Role or job title. |
| `experiences[].location` | object | Work location when structured parts are known. |
| `experiences[].location.city` | string | Work city. |
| `experiences[].location.country` | string | Work country. |
| `experiences[].start_date` | string | Start wording from the source. |
| `experiences[].end_date` | string | End wording from the source. |
| `experiences[].website` | string | Organization or role website. |
| `experiences[].logo` | string | Logo reference if supplied. |
| `experiences[].tasks` | array of string | Responsibilities or tasks, one text item each. |
| `experiences[].achievements` | array of string | Achievement statements, one text item each. |
| `education` | array of object | Education entries. |
| `education[]` | object | Education[]. |
| `education[].school` | string | School or institution. |
| `education[].degree` | string | Qualification or degree. |
| `education[].field` | string | Field of study. |
| `education[].start_date` | string | Start wording from the source. |
| `education[].end_date` | string | End wording from the source. |
| `education[].website` | string | Institution website. |
| `education[].logo` | string | Logo reference if supplied. |
| `education[].school_location` | object | City/country object; older text cannot always be split. |
| `education[].school_location.city` | string | School city. |
| `education[].school_location.country` | string | School country. |
| `skills` | object | Three established skill buckets. |
| `skills.it_skills` | array of object | IT-related skills. |
| `skills.it_skills[]` | object | Skill object; simple entries need only `name`. |
| `skills.it_skills[].name` | string | Nonempty source skill label; required when item exists. |
| `skills.it_skills[].level` | string | Source-backed human-readable proficiency; no fixed scale. |
| `skills.it_skills[].category` | string | Source-backed subcategory within the outer bucket. |
| `skills.it_skills[].keywords` | array of string | Source-backed related terms; no inferred aliases. |
| `skills.hard_skills` | array of object | Other technical or domain skills. |
| `skills.hard_skills[]` | object | Skill object; simple entries need only `name`. |
| `skills.hard_skills[].name` | string | Nonempty source skill label; required when item exists. |
| `skills.hard_skills[].level` | string | Source-backed human-readable proficiency; no fixed scale. |
| `skills.hard_skills[].category` | string | Source-backed subcategory within the outer bucket. |
| `skills.hard_skills[].keywords` | array of string | Source-backed related terms; no inferred aliases. |
| `skills.soft_skills` | array of object | Interpersonal or transferable skills. |
| `skills.soft_skills[]` | object | Skill object; simple entries need only `name`. |
| `skills.soft_skills[].name` | string | Nonempty source skill label; required when item exists. |
| `skills.soft_skills[].level` | string | Source-backed human-readable proficiency; no fixed scale. |
| `skills.soft_skills[].category` | string | Source-backed subcategory within the outer bucket. |
| `skills.soft_skills[].keywords` | array of string | Source-backed related terms; no inferred aliases. |
| `certifications` | array of object | Certification entries. |
| `certifications[]` | object | Certifications[]. |
| `certifications[].name` | string | Certification name. |
| `certifications[].issuer` | string | Issuing organization. |
| `certifications[].date_obtained` | string | Date wording from the source. |
| `certifications[].expiry_date` | string | Expiry wording from the source. |
| `certifications[].credential_id` | string | Credential identifier. |
| `certifications[].credential_url` | string | Credential URL. |
| `languages` | array of object | Language entries. |
| `languages[]` | object | Languages[]. |
| `languages[].language` | string | Language name. |
| `languages[].level` | string | Source-backed proficiency wording. |
| `languages[].certificates` | array (item type open) | Legacy list of certificates; item shape remains unspecified. |
| `interests` | array of string | Personal interests or activities. |
| `project_achievements` | array of object | Projects or achievements described in the CV. |
| `project_achievements[]` | object | Project achievements[]. |
| `project_achievements[].id` | string | Project identifier if supplied. |
| `project_achievements[].service_type` | string | Service or work type. |
| `project_achievements[].client` | string | Client or beneficiary. |
| `project_achievements[].title` | string | Project title. |
| `project_achievements[].period` | object | Human-readable start/end object; older free text may not split. |
| `project_achievements[].period.start` | string | Start wording. |
| `project_achievements[].period.end` | string | End wording. |
| `project_achievements[].role` | array of string | One or more role labels. |
| `project_achievements[].sectors` | array of string | One or more sector labels. |
| `project_achievements[].competencies` | array of string | One or more competency labels. |
| `project_achievements[].keywords` | array of string | One or more source-backed terms. |
| `project_achievements[].description` | string | Project description. |
| `project_achievements[].synonyms` | object | Optional open object; internal structure is not standardized. Preserve supplied data. |
| `meta` | object | Processing provenance and diagnostics, not biographical facts. |
| `meta.cv_uuid` | string or null | Processing-system CV identifier. |
| `meta.cv_title` | string or null | Display/export title. |
| `meta.parsing_errors` | array of string | Extraction/mapping issues; moved from 1.0 root. |
| `meta.ats_processed` | boolean or null | Whether ATS-oriented processing is known to have occurred. |
| `meta.processor_engine` | string or null | Processor identifier. |
| `meta.parsed_at` | string or null | Parse timestamp in source/system wording. |
| `meta.source_original_text` | string or null | Original extracted text if retained. |
| `meta.source_ats_revised_text` | string or null | ATS-oriented revised text if retained. |
| `meta.original_filename` | string or null | Original document filename. |
| `meta.source_format` | string or null | Source file format. |
| `meta.ingested_at` | string or null | Ingestion timestamp. |
| `meta.embedded_at` | string or null | Embedding timestamp. |
| `meta.extraction_confidence_overall` | number or null | Optional numeric confidence from 0 to 1. |
| `extensions` | object | Adopter-specific data; unknown JSON values preserved on pass-through. |

## Version differences

The [compatibility guide]({{ '/docs/compatibility/' | relative_url }}) details 1.0/1.2 changes and conversion ambiguity. In particular, 1.3 skill items are objects, school locations are objects, project periods are objects, and project role/sectors/competencies/keywords are arrays of text. `synonyms` is an optional open object with no standardized internal keys or values. `other_socials[]` and `languages[].certificates[]` remain open because populated historical evidence does not establish an item contract.

The standard describes CV data and processing metadata. A consuming application may impose stricter requirements but should identify those as its own profile.
