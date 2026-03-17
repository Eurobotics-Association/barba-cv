---
title: Design Principles
layout: page
description: Core Barba-CV design principles for deterministic CV schema structure, semantic flexibility, and interoperability across AI and ATS systems.
---

# Design Principles

Barba-CV is an open-source standard designed to represent CV / resume data in a way that is both **deterministic for systems** and **usable with real-world documents**.

Real-world CV data is heterogeneous: it may be incomplete, inconsistently structured, or only partially normalized. Barba-CV addresses this by enforcing a **deterministic structural model while preserving semantic flexibility**, allowing messy real-world career data to be captured and processed reliably.

---

## 1. Deterministic structure

The schema must define a stable and predictable structure so that:

* AI systems can map extracted information into known fields
* ATS and HR platforms can consume CV data consistently
* rendering engines can generate standardized layouts reliably
* developers can validate payloads programmatically

Barba-CV therefore defines a **canonical structural model** for CV data.

---

## 2. Semantic flexibility

While the structure must be deterministic, the content must remain flexible enough to reflect real CVs.

Examples:

* dates may be incomplete, localized, approximate, or narrative
* some fields may be missing entirely
* some values may already be normalized while others remain raw
* language levels, titles, and descriptions may vary significantly by country, profession, and context

Barba-CV is therefore designed to avoid over-constraining real-world data.

---

## 3. The CV stays at root

For backward compatibility and implementation simplicity, the CV payload remains at the root of the JSON object.

Barba-CV v1.2 introduces:

* `barba_cv_version`
* `meta`
* `extensions`

but keeps the main CV sections directly accessible at root.

This preserves continuity with Barba-CV v1 already in use.

---

## 4. Minimal mandatory fields

Barba-CV should remain compatible with partial parsing, incomplete source documents, and iterative enrichment workflows.

For this reason, the standard keeps **mandatory fields to a minimum**.

Implementers may enforce stricter requirements in their own pipelines, but the standard itself should remain broadly usable across many CV situations.

---

## 5. Data, not layout

Barba-CV stores **career data**, not document presentation.

The same Barba-CV payload should be renderable into different outputs:

* ATS-friendly single-column CVs
* recruiter-friendly multi-column CVs
* HTML pages
* DOCX documents
* PDFs
* AI-oriented text views

Document layout belongs to the rendering layer, not to the core data model.

---

## 6. AI-ready by design

Barba-CV is explicitly designed to help AI and LLM systems transform unstructured CVs into structured data.

The target workflow is:

```text
Unstructured CV (PDF / DOCX / text)
        ↓
AI / LLM extraction
        ↓
Barba-CV structured mapping
        ↓
Validated and reusable career dataset
```

Barba-CV provides the deterministic missing layer between probabilistic extraction systems and structured HR data.

---

## 7. ATS compatibility

The model must support ATS usage and standardized recruiter workflows.

This means Barba-CV should favor:

* clear sectioning
* predictable field names
* portable text content
* rendering into ATS-compatible layouts

Barba-CV is not tied to one ATS vendor, but it should remain easy to adapt to ATS expectations.

---

## 8. Separation of business content and processing metadata

The standard distinguishes between:

* **CV semantic content**
* **processing or operational metadata**

Examples of semantic content:

* personal information
* experience
* education
* skills
* certifications
* languages
* position sought

Examples of metadata:

* parser errors
* processor version
* original filename
* ingestion dates
* confidence score
* internal UUID
* export title

Operational metadata belongs in the `meta` block.

---

## 9. Controlled extensibility

The core standard should remain stable and interoperable.

At the same time, implementers may need additional fields for:

* ATS-specific identifiers
* MCP metadata
* billing or payment references
* internal workflow annotations
* vendor-specific integrations

For this reason, Barba-CV provides an `extensions` area rather than encouraging uncontrolled schema drift.

---

## 10. Human-readable and machine-usable

Barba-CV must remain understandable by:

* developers
* recruiters
* HR operations teams
* AI systems
* rendering engines

Field names, section boundaries, and documentation should remain clear enough for humans while staying predictable for machines.

---

## 11. Backward compatibility matters

Barba-CV v1 was already in operational use before the formal schema was introduced.

The evolution toward Barba-CV v1.2 therefore prioritizes:

* continuity of the root structure
* careful naming cleanup
* migration without unnecessary breakage
* compatibility across engine, API, and MCP layers

The standard should evolve deliberately, not disruptively.

---

## 12. Open-source and vendor-neutral

Barba-CV is an open-source, vendor-neutral standard.

It is designed so that:

* different developers can build validators, renderers, and APIs
* companies can adopt it without being locked into one provider
* the ecosystem can evolve through community and partner contributions

The standard must remain usable beyond any single implementation.

---

## 13. Keep the model compact

One of the main risks for any HR data standard is to become too large, too rigid, or too enterprise-heavy.

Barba-CV should avoid turning into a complex HR-XML-style structure.

Its strength comes from being:

* small enough to implement easily
* structured enough to validate reliably
* flexible enough for real CVs
* modern enough for AI pipelines

---

## Summary

Barba-CV is built on a simple principle:

> **Deterministic structure, semantic flexibility.**

This balance is what allows Barba-CV to serve as an open-source standard for AI parsing, ATS interoperability, HR workflows, and multi-format CV rendering.

## Related documentation

- [Documentation Hub](./index.md)
- [Visual Overview](./visual-overview.md)
- [Design Principles](./design-principles.md)
- [LLM Integration](./llm-integration.md)
- [AI Parsing Guidelines](./ai-parsing-guidelines.md)
