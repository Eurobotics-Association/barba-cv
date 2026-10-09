---
title: Roadmap
layout: page
---

> **Status (2026-10-10):** A 1.3 candidate contract, strict version-specific schema, guide and examples are available in this repository. No 1.3 release tag has been issued. The published 1.2 schema has unresolved references; see [version compatibility]({{ '/docs/compatibility/' | relative_url }}).

# Barba-CV Roadmap (Public Spec Repository)

This repository focuses on the **open Barba-CV specification**: schema, principles, and examples.

## Near-term priorities

1. Clarify schema semantics and field-level guidance
2. Expand representative example payloads
3. Improve versioning/changelog visibility for implementers
4. Publish a compliance validator specification

## Validator status

A public **compliance validator** is planned to help implementers verify whether payloads are Barba-CV compatible.

Current status:
- Strict 1.3 candidate validation is available via `schema/barba-cv-1.3.schema.json`; the published 1.2 schema has unresolved references
- Certification workflow and official validator process are not yet finalized in this repository

## Scope boundary

Barba-CV remains a **vendor-neutral standard**.

Parsing engines, normalization pipelines, and commercial processing services may use Barba-CV, but are intentionally out of scope for this repository.

A separate public service-layer repository exists at:
- https://github.com/lgb-sas/mcp-nantua
