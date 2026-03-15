# 🧾 Barba‑CV

> **An open‑source industry specification for deterministic, machine‑readable CV data.**

Barba‑CV is an **open‑source specification** for representing CV / resume data in a **structured, deterministic, and machine‑readable JSON format** optimized for:

* 🤖 **AI processing**
* 📄 **ATS compatibility**
* 🔗 **interoperability between HR tools**
* 🧠 **machine learning & analytics**
* 🗂 **long‑term data portability**

The goal of this **open‑source project** is to provide a **simple, deterministic, and vendor‑neutral CV data standard** that can be used by:

* developers
* HR platforms
* recruiting software
* AI systems
* automation pipelines

---

# 🔮 Vision

As an **open‑source ecosystem**, Barba‑CV aims to become a **de‑facto open standard for structured CV data**, enabling a new generation of:

* AI‑native recruiting platforms
* interoperable HR systems
* portable career profiles
* automated talent analytics

The long‑term vision is a world where **career data is portable, structured, and interoperable across the entire HR ecosystem.**

---

# 🌍 The Industry Problem

Recruiters and HR systems process **millions of CVs every year**, yet the industry still relies on **unstructured documents**.

Even when CVs are provided as **PDF (the most common format used globally)**, they remain extremely difficult to process.

Typical problems include:

* multi‑column layouts
* custom typography
* graphics and icons
* tables used as layout systems
* inconsistent section naming
* different ordering of information

Two CVs containing the **exact same information** can look completely different.

For recruiters, this creates a real operational problem:

* reading large volumes of CVs becomes **mentally exhausting**
* information is **hard to locate quickly**
* comparisons between candidates become **inefficient**

For software systems the problem is even worse:

* parsing is unreliable
* information extraction becomes probabilistic
* ATS systems lose data
* automation pipelines become fragile

In other words:

> The industry stores critical career information inside **documents designed for visual presentation instead of structured data.**

---

# 🎯 The Barba‑CV Approach

Barba‑CV, as an **open‑source standard**, introduces a **deterministic JSON format** for CV data.

Instead of trying to analyse arbitrary document layouts, Barba‑CV defines a **normalized structure** that allows the industry to:

* extract CV data once
* store it in a structured format
* render it consistently
* analyse it reliably

This enables:

* ✅ deterministic data extraction
* ✅ standardized CV structure
* ✅ reliable ATS processing
* ✅ AI‑ready CV datasets
* ✅ long‑term candidate portability

## 🤖 Designed for AI and LLM Systems

Modern AI systems and LLMs are powerful at interpreting unstructured documents such as PDFs or Word files, but their outputs are often **non‑deterministic**. This means the same CV may be parsed slightly differently each time.

Barba‑CV templates provide the **deterministic missing piece** in this pipeline.

They allow AI systems to:

* convert messy, unorganized CV documents
* processed through **non‑deterministic AI / LLM systems**
* into a **strict, deterministic structured format**.

In practice the pipeline becomes:

```
Unstructured CV (PDF / DOCX)
        ↓
LLM / AI extraction
        ↓
Barba‑CV deterministic template
        ↓
Structured CV dataset
```

Barba‑CV is therefore **explicitly designed to help AI systems parse CVs into a structured template** that can be validated, stored, analysed, and rendered reliably.

Barba‑CV acts as a **canonical data layer for CV information**.

Documents (PDF, DOCX, HTML) then become **renderings of structured data**, not the source of truth.

---

# 💾 Storage Efficiency

Barba‑CV also improves how CV data is **stored and managed at scale**.

Because the format is structured JSON, CVs can be stored efficiently in modern databases such as **PostgreSQL JSONB**.

Benefits include:

* 📉 **Highly compressible storage** compared to PDF or DOCX
* 🗄 **Efficient indexing and querying** of candidate data
* ⚡ **fast search across millions of CVs**

Large HR platforms storing **hundreds of thousands or millions of CVs** can dramatically reduce storage usage.

Instead of storing heavy documents, they store **compressed structured career data**.

Documents then become **rendered views of that data**, generated when needed.

---

# 🎨 Rendering CVs in Any Format

A Barba‑CV profile is **layout‑agnostic**.

This means the same CV data can be rendered into **any format or layout** depending on the target use case.

Examples:

* 📄 PDF
* 🌐 HTML
* 📝 DOCX
* 📑 ATS‑optimized layouts
* 📊 AI‑optimized representations

Barba‑CV supports rendering through **Jinja2 templates**, enabling flexible generation of documents from structured CV data.

Examples:

* single‑column CVs optimized for ATS
* multi‑column CVs optimized for human reading
* compact recruiter views
* AI‑friendly machine representations

Typical rendering pipeline:

```
Barba‑CV JSON
     ↓
Jinja2 Template
     ↓
HTML / DOCX / PDF
```

This makes it possible to:

* standardize CV presentation
* generate multiple layouts from one dataset
* adapt rendering for AI or human consumption

---

# 🚀 Impact for the HR Industry

As an **open‑source HR data standard**, Barba‑CV helps **rationalize the entire CV lifecycle**.

For HR organizations this means:

* 📉 **reduced storage costs** when managing large CV databases
* ⚡ **faster candidate search and filtering**
* 📑 **consistent CV layouts for recruiters**
* 🤖 **AI‑ready datasets for talent analysis**
* 🔎 **better candidate comparison**

For recruiters:

* CVs become **easier and faster to read**
* candidate information becomes **consistent across profiles**

For HR platforms:

* parsing becomes **deterministic instead of probabilistic**
* systems become **simpler and more reliable**

For candidates:

* career data becomes **portable and reusable across platforms**

Ultimately, Barba‑CV helps the industry:

> **identify the right candidates faster by transforming CVs into structured data instead of visual documents.**

---

# 📦 Repository contents

```
barba-cv/

schema/
  barba-cv.schema.json

examples/
  simple-example.json
  multi-experience-example.json

tools/
  validator/
  cli/

docs/
  design-principles.md
  ats-compatibility.md

CHANGELOG.md
VERSIONING.md
BARBA-CV_SPEC_VERSION
LICENSE
TRADEMARKS.md
COMPATIBILITY.md
```

---

# 📐 Specification

The core of Barba‑CV is the JSON schema located in:

```
schema/barba-cv.schema.json
```

This schema defines standardized fields such as:

* 👤 candidate identity
* 🎓 education
* 💼 work experience
* 🧠 skills
* 📜 certifications
* 🧾 publications
* 🧩 additional structured sections

The schema follows **semantic versioning**.

Current version is defined in:

```
BARBA-CV_SPEC_VERSION
```

---

# 🧪 Compatibility levels

The Barba‑CV ecosystem defines several levels of compatibility.

| Label                      | Meaning                                    |
| -------------------------- | ------------------------------------------ |
| 🟢 Barba‑CV Compatible     | Generates valid JSON respecting the schema |
| 🟡 Barba‑CV Certified      | Validated by official validation tools     |
| 🔵 Official Implementation | Maintained by the Barba‑CV maintainers     |

Details are defined in:

```
COMPATIBILITY.md
```

---

# 🤝 Entitled partners

The Barba‑CV specification can be implemented by **any developer or company**.

However, some partners build **reference implementations or official services** around the standard.

Current entitled partners:

* **mcp‑nantua** — API gateway and service layer implementing the Barba‑CV processing ecosystem

More information:

[https://github.com/lgb-sas/mcp-nantua](https://github.com/lgb-sas/mcp-nantua)

---

# 📜 License

Barba‑CV is released as an **open‑source standard** and this project is licensed under the **Apache License 2.0**.

This allows:

* commercial usage
* SaaS implementations
* forks and improvements

while providing **patent protection for contributors**.

See:

```
LICENSE
```

---

# ™ Trademark

"Barba‑CV" is a trademark of **Eurobotics**.

Forks of this repository may not use the name "Barba‑CV" in a way that implies endorsement, certification, or official compatibility unless explicitly approved by the maintainers.

See:

```
TRADEMARKS.md
```

---

# 🚀 Contributing

We welcome contributions that improve:

* schema clarity
* validation tools
* documentation
* interoperability

Please open an issue before proposing **major changes to the specification**.

---

# 🏛 Maintainers

Barba‑CV is maintained by **Eurobotics** with contributions from the community.

---

# 🌱 Genesis of the Barba‑CV Project

Barba‑CV emerged from **real operational problems observed in the HR and consulting industry**.

In **mid‑2025**, Robert Vergnes (President of **Eurobotics.org**) was involved in multiple industrial and consulting projects where discussions with executives from **large industrial companies, consulting firms, and HR teams** repeatedly highlighted the same issue:

> Managing CVs at scale was becoming increasingly painful for both organizations and candidates.

Several recurring problems were identified:

* organizations managing **thousands of candidate CVs** struggled with inconsistent formats
* recruiters had to review **large volumes of visually different documents**, slowing down evaluation
* candidates found it difficult to **maintain and update their own CVs across multiple systems**
* HR IT systems were forced to parse **documents designed for visual presentation rather than structured data**

Despite the existence of ATS platforms and HR software, the underlying data problem remained unresolved.

CVs were still fundamentally **documents instead of structured career records**.

During the summer of 2025, many CV formats and HR systems were reviewed. The conclusion was simple:

> The industry needed a **small standardized database structure for each CV**.

Rather than inventing a complex system, the project chose a pragmatic approach:

* represent CV data as **structured JSON**
* define a **deterministic schema**
* allow any platform to **store, render, or analyse the data consistently**

By **September 2025**, the first **Barba‑CV JSON template** was created.

Since then, the project has continued to evolve through experimentation, implementation, and feedback from recruiters, engineers, and industry partners.

---

# 📬 Contacts

**Eurobotics.org**
Non‑Profit Organisation — Loi 1901
[contact@eurobotics.org](mailto:contact@eurobotics.org)
Compiègne | France

---
