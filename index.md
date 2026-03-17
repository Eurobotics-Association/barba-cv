---
layout: page
title: Home
permalink: /
---

<h1>
Barba-CV
<img src="logo/Barba-CV-Icon-Site-V1_off_20260220.png" width="60" style="vertical-align:middle;">
</h1>

Barba-CV is an open, vendor-neutral JSON specification for deterministic, machine-readable CV/resume data.

> “CV data is inherently heterogeneous—often incomplete, inconsistently structured, and partially normalized. The Barba-CV schema therefore enforces deterministic structure while preserving semantic flexibility, allowing real-world CV data to be represented without unrealistic constraints.”

<p align="center">
<img src="logo/Barba-CV_transforming_resumes_seamlessly_v2_off_20260317.png" width="600">
</p>

## Conceptual Pipeline

1. Unstructured CV (PDF/DOCX)
2. AI/LLM extraction (probabilistic)
3. Barba-CV schema mapping (deterministic)
4. Structured CV data for interoperability

## What it is / is not

**Barba-CV is:**
- an open, vendor-neutral data standard
- a deterministic JSON schema for CV structure
- a shared format for AI extraction pipelines and ATS interoperability

**Barba-CV is not:**
- a parser service in this repository
- a public API or SDK
- a replacement for separate service-layer projects

## Quick links

- [Schema (`schema/barba-cv.schema.json`)](https://github.com/Eurobotics-Association/barba-cv/blob/main/schema/barba-cv.schema.json)
- [Examples (`examples/`)](https://github.com/Eurobotics-Association/barba-cv/tree/main/examples)
- [Design principles](./design-principles/)
- [AI parsing guidance](./ai-parsing-guidance/)
- [Roadmap](./roadmap/)
- [Project origin](./origin/)
- [License (`LICENSE`)](https://github.com/Eurobotics-Association/barba-cv/blob/main/LICENSE)
