# AI Parsing Guidelines

This document explains how AI systems (LLMs, extraction pipelines, or parsing engines) should transform unstructured CV data into the **Barba-CV JSON format**.

Barba-CV is designed to act as the **deterministic structural layer** between probabilistic AI extraction and structured HR datasets.

---

# 1. Goal of AI parsing

The goal of an AI parser is to convert:

```
Unstructured CV (PDF / DOCX / HTML / text)
        ↓
AI extraction
        ↓
Barba-CV JSON structure
```

The parser should **map information into the Barba-CV structure without inventing data**.

Missing information should remain empty.

---

# 2. Never invent information

If a field cannot be extracted with confidence, it should be left empty.

Examples:

```
"date_of_birth": ""
"phone": ""
"organization": ""
```

AI systems **must not hallucinate information**.

---

# 3. Prefer structured extraction over free text

Whenever possible, the AI should structure information into the correct fields.

Example:

Instead of:

```
"profile_summary": "Worked at ACME as a software engineer from 2020 to 2023"
```

Use:

```
"experiences": [{
  "organization": "ACME",
  "role_title": "Software Engineer",
  "start_date": "2020",
  "end_date": "2023"
}]
```

---

# 4. Handling incomplete dates

Dates in CVs are highly variable.

Allowed examples:

```
"2020"
"Jan 2021"
"2021-2023"
"September 2019"
"Present"
```

Do not attempt to normalize aggressively.

Dates should remain **human readable**.

---

# 5. Experience extraction

Each professional role should become one element in `experiences`.

Example:

```
"experiences": [
  {
    "organization": "Example Company",
    "role_title": "Senior Engineer",
    "start_date": "2020",
    "end_date": "2023",
    "tasks": [],
    "achievements": []
  }
]
```

Descriptions should be split when possible:

* responsibilities → `tasks`
* measurable outcomes → `achievements`

---

# 6. Education extraction

Each education entry becomes one element in `education`.

Fields to extract when available:

* school
* degree
* field
* dates
* location

---

# 7. Skills classification

Skills should be categorized when possible:

```
"skills": {
  "it_skills": [],
  "hard_skills": [],
  "soft_skills": []
}
```

Guidelines:

| Category    | Meaning                            |
| ----------- | ---------------------------------- |
| it_skills   | programming, tools, software       |
| hard_skills | professional capabilities          |
| soft_skills | interpersonal or behavioral skills |

If classification is unclear, place the skill in `hard_skills`.

---

# 8. Position sought

The field `position_sought` describes the candidate's professional target.

Examples:

```
"position_sought": [
  "Full Stack Developer",
  "Python Expert"
]
```

If the CV includes a headline or title, it should be mapped here.

---

# 9. Languages

Languages should include:

```
{
  "language": "English",
  "level": "Fluent"
}
```

Levels remain **free text** to allow different conventions.

---

# 10. Certifications

Certifications should include issuer and dates when available.

Example:

```
{
  "name": "AWS Certified Solutions Architect",
  "issuer": "Amazon",
  "date_obtained": "2022"
}
```

---

# 11. Project achievements

Major projects or consulting missions can be extracted into `project_achievements`.

Example:

```
{
  "title": "ERP Implementation",
  "client": "Manufacturing Group",
  "role": "Project Manager",
  "period": "2021-2022"
}
```

---

# 12. Metadata population

The `meta` block contains operational information about parsing.

Typical fields include:

```
"meta": {
  "cv_uuid": "",
  "processor_engine": "",
  "ats_processed": false
}
```

AI systems should populate metadata only when known.

---

# 13. Extensions

Custom system information must be placed inside `extensions`.

Example:

```
"extensions": {
  "ats_id": "12345",
  "client_reference": "ABC"
}
```

This prevents breaking the core schema.

---

# 14. Output validation

After extraction, the generated JSON should:

1. validate against `barba-cv.schema.json`
2. contain only supported fields
3. respect the root CV structure

---

# Summary

AI parsing with Barba-CV follows a simple rule:

> Extract faithfully. Structure deterministically. Never invent data.

This ensures reliable CV parsing while keeping the schema compatible with real-world documents.
