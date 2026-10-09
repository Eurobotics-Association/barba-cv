---
title: Skill objects
layout: page
permalink: /docs/skills/
description: How to represent names, levels, categories and keywords in Barba-CV 1.3.
---

# Skill objects in 1.3

Barba-CV groups skills in `skills.it_skills`, `skills.hard_skills`, and `skills.soft_skills`. Each populated 1.3 item is an object. The only required property is a nonempty `name`.

| Property | Type | Meaning | Example | If unavailable |
| --- | --- | --- | --- | --- |
| `name` | nonempty text | Skill label found in the source | `"Python"` | Do not emit an item. |
| `level` | text | Source's proficiency or experience wording; no standard scale | `"Advanced"`, `"3 years"` | Omit. Never infer from job title or tenure. |
| `category` | text | Source-backed grouping *inside* the chosen outer bucket | `"Programming languages"` | Omit. The outer bucket already groups the skill. |
| `keywords` | array of text | Source-backed related terms useful for discovery | `["automation"]` | Omit or use `[]` only when explicitly known empty. Do not invent synonyms. |

Use `{ "name": "SQL" }` when the source provides no further detail. If a CV says “Advanced Python (automation)”, an extraction system may write `{ "name": "Python", "level": "Advanced", "keywords": ["automation"] }`. Preserve original wording where interpretation is uncertain. The standard does not rank proficiency, require a controlled vocabulary, or infer relationships between skills.

Objects provide a place for detail that a string cannot hold. They also make later enrichment possible without changing the item type. The cost is a breaking change for readers that assume each skill item is a string. Historical strings remain valid historical evidence; a compatibility reader can read `"Python"` as a name-only skill, but a 1.3 writer emits the object. Never reduce an object with populated detail to a string without reporting the information loss.

The 1.0 original has empty arrays, so it cannot prove item type. A filled 1.0-shaped sample and repository examples show strings; the published 1.2 template shows objects. The choice for 1.3 is an explicit standard decision, not a claim that all legacy payloads used objects.
