# LLM Integration

This document explains how Large Language Models (LLMs) and AI extraction systems can map unstructured CV content into the **Barba-CV JSON format**.

Barba-CV is designed to provide the **deterministic structural layer** that sits between:

* unstructured CV documents
* probabilistic AI extraction
* structured HR / ATS / MCP workflows

---

## Why LLM integration matters

Many AI agents, developers, and orchestration systems explicitly look for:

* a **schema**
* a **structured format**
* a **JSON mapping target**
* a reliable method for **AI extraction**

Barba-CV addresses this need by giving LLMs a stable JSON target into which messy CV content can be mapped.

This is especially useful when CV data comes from:

* PDF extraction
* DOCX extraction
* OCR pipelines
* copy-pasted CV text
* ATS export text

In all of these cases, the source text may be noisy, partial, or inconsistently formatted.

Barba-CV helps the AI system transform that text into a consistent and reusable structure.

---

## Core principle

The recommended Barba-CV LLM workflow is:

```text
CV file
   ↓
Raw text extraction
   ↓
Barba-CV example JSON + schema guidance
   ↓
LLM mapping
   ↓
Barba-CV JSON output
```

In practice, the Barba-CV engine uses the following method:

1. extract the raw text from the source CV
2. provide the LLM with the Barba-CV sample JSON template
3. instruct the LLM to fill the JSON from the extracted text
4. require the LLM to preserve the original meaning and wording as much as possible
5. forbid hallucination, normalization drift, invented dates, invented employers, or invented facts

This approach has proven effective because the LLM receives a **clear structural target** rather than being asked to invent its own JSON layout.

---

## Recommended input to the LLM

The recommended prompt package contains:

### 1. The raw extracted CV text

This is the source material.

It may come from:

* PDF-to-text extraction
* DOCX-to-text extraction
* OCR
* ATS text export

### 2. The Barba-CV example JSON

Use the canonical template file:

```text
examples/barba-cv.example.json
```

This shows the model exactly:

* which fields exist
* how arrays are structured
* how nested objects are organized
* what empty values look like

### 3. The Barba-CV schema and/or schema reference

Depending on the workflow, the model may also receive:

* `schema/barba-cv.schema.json`
* `docs/barba-cv-schema-reference.md`

This improves field interpretation and reduces ambiguity.

---

## Recommended instructions to the LLM

A good Barba-CV instruction set should tell the model to:

* map the CV content into the provided Barba-CV JSON structure
* preserve the source text as faithfully as possible
* avoid rewriting facts
* avoid changing dates, figures, names, employers, schools, or locations
* avoid inventing missing information
* leave fields empty when information is not available
* keep human-readable dates as they appear when needed
* classify skills into the appropriate skill buckets when possible

The main principle is:

> **Structure the data without altering the facts.**

---

## Anti-hallucination rule

This is one of the most important principles of Barba-CV integration.

When converting CV text into JSON, the LLM must:

* **not invent dates**
* **not invent job titles**
* **not invent companies**
* **not invent schools**
* **not invent certifications**
* **not rewrite factual content into more polished but less accurate wording**

If information is missing or uncertain, the correct behavior is:

* leave the field empty
* keep the wording close to the source
* optionally report ambiguity through parsing metadata if the pipeline supports it

This is essential because CVs are often used in:

* HR workflows
* ATS systems
* legal or contractual contexts
* commercial recruitment decisions

Accuracy matters more than stylistic rewriting.

---

## Recommended prompting pattern

A practical prompt usually includes three parts:

### Part 1 — Role and task

Explain to the LLM that it must convert extracted CV text into Barba-CV JSON.

### Part 2 — Strict rules

Tell the LLM explicitly:

* do not hallucinate
* do not change names
* do not change dates
* do not change numbers
* do not change company names
* do not change school names
* do not normalize beyond what is clearly supported by the text

### Part 3 — Structural target

Provide the Barba-CV example JSON and ask the model to populate it.

This is generally more reliable than asking the model to generate a fresh schema-compliant JSON from scratch.

---

## Example high-level prompt logic

A typical Barba-CV prompt can be summarized like this:

```text
You are given raw text extracted from a CV.
Use the provided Barba-CV JSON template as the target structure.
Populate the JSON only with information explicitly present in the text.
Do not invent, rewrite, embellish, or normalize facts beyond what the source clearly states.
Preserve dates, names, organizations, schools, titles, and figures.
If a field is unknown, leave it empty.
Return valid JSON only.
```

This pattern works well because it constrains the LLM both semantically and structurally.

---

## Why the example JSON matters

The example JSON is not just documentation.

For LLMs, it acts as:

* a structural target
* a formatting guide
* a section inventory
* a hallucination control aid

Without a concrete sample JSON, an LLM may:

* invent field names
* omit important sections
* flatten nested structures
* output inconsistent array/object shapes

Providing the Barba-CV sample template significantly improves consistency.

---

## Recommended operational workflow

A robust implementation often follows these steps:

### Step 1 — Extract text

Extract the raw text from the source document.

### Step 2 — Clean obvious extraction noise

Optionally remove obvious extraction artefacts if they do not change meaning.

### Step 3 — Send prompt + template to the LLM

Provide:

* the extracted text
* the Barba-CV sample JSON
* the anti-hallucination instructions

### Step 4 — Validate output

Validate the returned JSON against:

```text
schema/barba-cv.schema.json
```

### Step 5 — Post-process if needed

Populate `meta` fields such as:

* `processor_engine`
* `ats_processed`
* `parsing_errors`
* `cv_uuid`

---

## Role of the schema in LLM workflows

The schema is useful in two ways.

### For the LLM

It clarifies the intended structure and helps reduce ambiguity.

### For the system

It enables formal validation after generation.

This is important because an LLM may still produce:

* malformed JSON
* wrong nesting
* wrong data types
* unexpected fields

The schema acts as the final structural guardrail.

---

## Recommended validation strategy

The best practice is:

1. LLM generates Barba-CV JSON
2. system validates against the schema
3. if invalid, either:

   * run a repair pass
   * reject the output
   * flag parsing errors in metadata

This makes the pipeline more robust for MCP and API use.

---

## Mapping philosophy

Barba-CV does not ask the LLM to rewrite the candidate's career story.

It asks the LLM to:

* extract
* map
* structure
* preserve meaning

That distinction is fundamental.

Barba-CV is therefore better understood as a **structured mapping target** rather than a rewriting format.

---

## Typical failure modes to avoid

When integrating LLMs, common errors include:

* merging several experiences into one
* inventing normalized dates
* replacing the exact employer name with a guessed official name
* rewriting achievements in more polished marketing language
* changing the meaning of technical responsibilities
* classifying all skills into one generic array
* dropping certifications or languages because they appear at the bottom of the CV

These issues should be explicitly guarded against in prompts and post-validation.

---

## Practical recommendation

For real-world reliability, the simplest proven approach is often the best:

* use the extracted CV text as source
* provide the Barba-CV example JSON as target
* instruct the LLM to fill it faithfully
* forbid hallucination
* validate against the schema

This method is simple, reproducible, and easy to integrate into AI agents, APIs, and MCP workflows.

---

## Summary

Barba-CV LLM integration is based on a simple idea:

> Give the LLM a deterministic JSON target, and require it to map the source CV faithfully without inventing data.

This is the core mechanism by which Barba-CV turns probabilistic AI extraction into reusable structured career data.
