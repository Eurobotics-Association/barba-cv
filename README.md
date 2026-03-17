# 🧾 Barba-CV

> **Open, vendor-neutral JSON standard for deterministic, machine-readable CV/resume data.**

Barba-CV is an **open-source specification** (not a parser service) that defines a normalized JSON format for CV/resume data so AI systems, ATSs, and HR software can exchange profiles reliably.

CV data is inherently heterogeneous—often incomplete, inconsistently structured, and partially normalized. The Barba-CV schema therefore enforces deterministic structure while preserving semantic flexibility, allowing real-world CV data to be represented without unrealistic constraints.

## Documentation

Full documentation is available at:

https://eurobotics-association.github.io/barba-cv/

---

## Why Barba-CV exists

Barba-CV exists to solve a fundamental problem in recruitment technology.

Recruitment systems receive thousands of CVs written in very different formats, layouts, and structures. Traditional CV parsing systems are fragile and frequently lose information when converting resumes into structured data.

Barba-CV introduces a deterministic JSON representation of CV data so that the information contained in a resume can be represented in a reliable and machine-readable format.

This enables:

• reliable CV parsing by AI systems
• interoperability between ATS platforms
• structured data exchange between HR systems
• processing of candidate profiles by autonomous AI agents

Barba-CV is designed to be both **deterministic and flexible**, allowing it to represent the wide diversity of CV structures while preserving the original information without hallucination or reinterpretation.

---

## Deterministic structure for AI and ATS systems

AI systems and LLM pipelines require deterministic structures to reliably extract and store information from unstructured CV text.

Barba-CV provides such a framework using JSON and JSON Schema.

Key design principles:

• deterministic structure for reliable parsing
• flexibility to represent different CV styles
• preservation of original information without hallucination
• compatibility with AI agent pipelines

The schema allows AI systems to map extracted CV text directly into structured JSON while keeping the original meaning intact.

---

## Efficient storage and interoperability

Using JSON (and JSONB in modern databases) provides several benefits:

• highly efficient storage of structured CV data
• easy exchange between systems
• compression and indexing in databases
• compatibility with modern APIs

This makes Barba-CV suitable for:

• AI pipelines
• HR platforms
• recruitment automation systems
• data warehouses

---

## Rendering and document generation

Barba-CV also enables deterministic rendering of CVs into different formats.

Because the data structure is standardized, it can easily be rendered using template engines such as Jinja into:

• HTML
• PDF
• DOCX

This allows organizations to generate CV formats adapted to their own branding or recruitment workflows while keeping a single structured representation of the candidate data.

---

<p align="center">
  <img src="https://raw.githubusercontent.com/Eurobotics-Association/barba-cv/96262ad2165e279f1f00697fd7c231a0ca3dedf6/logo/Barba-CV_transforming_resumes_seamlessly_v2_off_20260317.png" width="50%">
  <br>
  <em>Barba-CV transforms heterogeneous CVs into a standardized format.</em>
</p>

## What Barba-CV is / is not

**Barba-CV is:**
- ✅ an open, vendor-neutral **data standard**
- ✅ a deterministic **JSON schema** for CV structure
- ✅ a common target format for AI extraction pipelines and ATS interoperability

**Barba-CV is not:**
- ❌ a public parsing engine in this repository
- ❌ a full recruiting platform or paid processing service
- ❌ a replacement for service-layer projects

If you need API/service infrastructure around Barba-CV, see **MCP Nantua** (separate repository):
- https://github.com/lgb-sas/mcp-nantua

---

## Why this matters (AI + ATS + interoperability)

CVs are usually stored as PDFs or DOCX files designed for visual reading, not structured data. For software systems this creates recurring problems:
- inconsistent layouts and section names
- extraction variability across OCR/LLM pipelines
- fragile downstream matching and analytics
- poor cross-system portability

Barba-CV solves this by defining a deterministic JSON structure that becomes the **source of truth** for candidate data.

Typical pipeline:

```text
Unstructured CV (PDF/DOCX)
        ↓
AI/LLM extraction (probabilistic)
        ↓
Barba-CV schema mapping (deterministic)
        ↓
Validated, portable, queryable CV data
```

---

## Comparison with existing formats

Barba-CV addresses a similar problem space as **JSON Resume**, **HR-XML / HR-JSON**, and **Europass CV**, with a focused scope for deterministic CV data pipelines.

| Format | Primary focus | Main limitation | Barba-CV angle |
|---|---|---|---|
| JSON Resume | Lightweight developer resume JSON | Less oriented to AI extraction + ATS normalization workflows | Deterministic schema targeting AI/ATS interoperability |
| HR-XML / HR-JSON | Broad enterprise HR data exchange | Often heavier to implement for CV-first pipelines | Developer-friendly CV-focused JSON structure |
| Europass CV | Standardized profile presentation in EU context | Less flexible for cross-platform technical pipeline integration | Vendor-neutral structured format for interoperable CV data |

Barba-CV emphasizes deterministic structured CV data, compatibility with AI extraction mapping, ATS interoperability, and a schema-first developer workflow.

## Rendering

Barba-CV defines the structured data layer of a CV. Presentation formats are generated by external rendering systems.

Possible outputs include:
- PDF
- HTML
- DOCX

Conceptual pipeline:

```text
Barba-CV JSON
     ↓
Template
     ↓
PDF / HTML / DOCX
```

This repository does not include rendering tools.

## Storage and analytics

Because Barba-CV payloads are structured JSON, they can be stored and queried in systems such as:
- PostgreSQL JSONB
- document databases
- analytics platforms

This supports use cases like structured search, candidate analytics, machine learning datasets, and large-scale CV databases.

---

## Quick navigation

- **Schema:** [`schema/barba-cv.schema.json`](schema/barba-cv.schema.json)
- **Examples:** [`examples/`](examples)
- **Design principles:** [`docs/design-principles.md`](docs/design-principles.md)
- **AI mapping guidance:** [`docs/ai-parsing-guidelines.md`](docs/ai-parsing-guidelines.md)
- **Roadmap / validator status:** [`docs/roadmap.md`](docs/roadmap.md)
- **License:** [`LICENSE`](LICENSE)

---

## Repository contents

```text
barba-cv/
├── schema/
│   └── barba-cv.schema.json
├── examples/
│   ├── barba-cv.template.json
│   ├── Clara_Delaunay_International_Internship_20260316.json
│   ├── Marc_Valentin_Customer_Service_Manager_20260316.json
│   └── Nassim_Karoubi_Business_Development_Internship_20260316.json
├── docs/
│   ├── ai-parsing-guidelines.md
│   ├── design-principles.md
│   ├── genesis.md
│   └── roadmap.md
├── logo/
├── LICENSE
└── README.md
```

---

## Specification scope

The schema defines normalized CV sections such as:
- personal information
- profile summary and target position
- work experiences and education
- skills, certifications, languages, interests
- project achievements
- processing metadata (`meta`) and controlled extensions (`extensions`)

Barba-CV is intended to serve as a **normalized data layer for CV/resume interoperability**. Different renderers and services can be built on top of it.

---

## Example payloads

Start with:
- template: [`examples/barba-cv.template.json`](examples/barba-cv.template.json)
- internship profile: [`examples/Clara_Delaunay_International_Internship_20260316.json`](examples/Clara_Delaunay_International_Internship_20260316.json)
- management profile: [`examples/Marc_Valentin_Customer_Service_Manager_20260316.json`](examples/Marc_Valentin_Customer_Service_Manager_20260316.json)
- business development profile: [`examples/Nassim_Karoubi_Business_Development_Internship_20260316.json`](examples/Nassim_Karoubi_Business_Development_Internship_20260316.json)

Recommended next additions (incremental):
- a **senior technical profile** example (engineering-heavy vocabulary)
- a **career-switch profile** example (non-linear timeline)

---

## Versioning and compatibility

- The format version is carried by `barba_cv_version` in each payload.
- Schema evolution is managed conservatively to keep interoperability high.
- Compatibility labels and formal certification tooling are documented and evolving.

See: [`docs/roadmap.md`](docs/roadmap.md)

---

## License and trademark

- License: Apache-2.0 (`LICENSE`)
- Trademark notice: “Barba-CV” is maintained by Eurobotics; naming use must not imply false endorsement.

---

## Contributing

Contributions are welcome for:
- schema clarity
- documentation
- examples
- interoperability guidance

For major specification changes, open an issue first to discuss scope and compatibility impact.


---

## Project origin

See [`docs/genesis.md`](docs/genesis.md) for background on how the Barba-CV specification emerged.
