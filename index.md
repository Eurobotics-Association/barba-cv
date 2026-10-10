---
title: Open CV data standard
layout: default
permalink: /
description: Barba-CV is an open JSON standard for structured, portable CV data across extraction and HR systems.
---
<div class="hero">
  <div class="shell hero-grid">
    <div class="hero-copy">
      <span class="eyebrow"><span class="status-dot"></span> Open standard · v1.3 released 2026-10-10</span>
      <h1>CV data that<br><em>moves with meaning.</em></h1>
      <p class="hero-lead">A clear JSON structure for resumes and CVs. Preserve what the source says, make it machine readable, and exchange it across tools.</p>
      <div class="hero-actions">
        <a class="button button-primary" href="{{ '/docs/getting-started/' | relative_url }}">Get started <span aria-hidden="true">→</span></a>
        <a class="button button-secondary" href="{{ '/docs/field-reference/' | relative_url }}">Explore the reference</a>
      </div>
      <p class="hero-note">Only the version is required. Add detail when the source supports it.</p>
    </div>
    <div class="code-panel" aria-label="Example Barba-CV JSON payload">
      <div class="code-top"><span class="code-dots" aria-hidden="true">● ● ●</span><span>barba-cv.json</span><span class="code-badge">1.3</span></div>
      <pre><code><span class="code-punctuation">{</span>
  <span class="code-key">"barba_cv_version"</span>: <span class="code-value">"1.3"</span>,
  <span class="code-key">"personal_info"</span>: <span class="code-punctuation">{</span>
    <span class="code-key">"first_name"</span>: <span class="code-value">"Alex"</span>
  <span class="code-punctuation">}</span>,
  <span class="code-key">"skills"</span>: <span class="code-punctuation">{</span>
    <span class="code-key">"it_skills"</span>: <span class="code-punctuation">[</span>
      <span class="code-punctuation">{</span><span class="code-key">"name"</span>: <span class="code-value">"Python"</span><span class="code-punctuation">}</span>
    <span class="code-punctuation">]</span>
  <span class="code-punctuation">}</span>
<span class="code-punctuation">}</span></code></pre>
      <div class="code-bottom"><span class="code-check" aria-hidden="true">✓</span> Simple by default. Structured when needed.</div>
    </div>
  </div>
</div>
<section class="intro-band">
  <div class="shell intro-grid">
    <div><span class="section-kicker">THE IDEA</span><h2>Structure without<br>flattening the story.</h2></div>
    <div><p>CVs vary in language, layout, and detail. Barba-CV gives each section a predictable place while letting names, dates, locations, and skill levels keep their source meaning.</p><a class="text-link" href="{{ '/design-principles/' | relative_url }}">Read the design principles <span aria-hidden="true">→</span></a></div>
  </div>
</section>
<section class="section shell" aria-labelledby="principles-title">
  <div class="section-heading"><span class="section-kicker">BUILT FOR REAL-WORLD DATA</span><h2 id="principles-title">One structure. Room for nuance.</h2><p>Use the common fields for CV content and an optional extension area for adopter-specific data.</p></div>
  <div class="feature-grid">
    <article class="feature-card"><div class="feature-icon">{ }</div><h3>Predictable shape</h3><p>Named sections for identity, experience, education, skills, projects, and more.</p></article>
    <article class="feature-card"><div class="feature-icon">◫</div><h3>Source fidelity</h3><p>Keep human wording where normalization would guess, including dates and proficiency.</p></article>
    <article class="feature-card"><div class="feature-icon">↗</div><h3>Portable by design</h3><p>Plain JSON and a versioned schema for independent tools and implementations.</p></article>
  </div>
</section>
<section class="section docs-section" aria-labelledby="docs-title"><div class="shell">
  <div class="section-heading"><span class="section-kicker">DOCUMENTATION</span><h2 id="docs-title">Find the right starting point.</h2></div>
  <div class="docs-grid">
    <a class="doc-card" href="{{ '/docs/getting-started/' | relative_url }}"><span>01 / START</span><h3>Get started</h3><p>Build a small valid payload and add fields as evidence allows.</p><b aria-hidden="true">↗</b></a>
    <a class="doc-card" href="{{ '/docs/field-reference/' | relative_url }}"><span>02 / CONTRACT</span><h3>Field reference</h3><p>Paths, types, optionality, empty values, and field meaning.</p><b aria-hidden="true">↗</b></a>
    <a class="doc-card" href="{{ '/docs/skills/' | relative_url }}"><span>03 / DEEP DIVE</span><h3>Skill objects</h3><p>When to use names, levels, categories, and keywords.</p><b aria-hidden="true">↗</b></a>
    <a class="doc-card" href="{{ '/docs/compatibility/' | relative_url }}"><span>04 / VERSIONS</span><h3>Compatibility</h3><p>Read historical shapes without silently discarding detail.</p><b aria-hidden="true">↗</b></a>
  </div>
</div></section>
<section class="section shell version-section"><div><span class="section-kicker">VERSION STATUS</span><h2>Clear history. Careful evolution.</h2><p>Latest release: <strong>Barba-CV v1.3 · 2026-10-10</strong>. The versioned schema, examples, and field guidance are available here. The 1.0 and published 1.2 originals remain preserved byte-for-byte.</p></div><div class="version-actions"><a class="button button-dark" href="{{ '/schema/barba-cv-1.3.schema.json' | relative_url }}">View 1.3 schema <span aria-hidden="true">↗</span></a><a class="text-link" href="https://github.com/Eurobotics-Association/barba-cv/releases/tag/v1.3">Read release notes <span aria-hidden="true">→</span></a></div></section>
