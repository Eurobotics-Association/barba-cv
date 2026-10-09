# Agent instructions for Barba-CV

## Scope and design

- This repository maintains an open, generic CV data standard, its documentation, examples and version references.
- Keep the work focused on the standard. Do not introduce CV-selection applications, rendering systems or profession-specific models without an explicit request.
- Preserve the guiding principle: deterministic structure, semantic flexibility. Keep mandatory fields and constraints minimal; consuming applications may impose their own requirements.
- Do not impose country-specific address rules, require normalization of uncertain dates, or infer information absent from a source.
- `$defs` and `$ref` are optional schema-authoring mechanisms, not requirements of the CV payload or a reason to introduce new constraints. Agree on field semantics before choosing how to express them.
- `extensions` is intended to let adopters add their own keys without redefining the common standard. Document its optional nature and extension behavior; do not move standard career content there merely to avoid defining it.

## Preserve history

- Keep historical schemas, templates and version-specific examples discoverable under `history/<version>/`, with links from `history/README.md`.
- Preserve supplied originals and published artifacts byte-for-byte, including spelling, key casing, whitespace, empty values and known defects. Do not silently repair, reformat, rename or delete archived originals.
- Before replacing, renaming or removing a current schema or template during evolution, ensure its existing version is preserved in the archive with provenance and checksums. Check for an existing matching archive first.
- Never overwrite a historical version with a newer interpretation. Put corrected or derived validators in distinct files, document their origin and status, and retain the originals.
- For each archived artifact, record its source, version evidence, original filename or repository path, source commit/tag when known, archival date, SHA-256 and known limitations. Distinguish a CV JSON template from a formal JSON Schema validator document.
- Add newly recovered historical artifacts without replacing previous evidence. Record conflicting sources rather than choosing one silently. Do not invent missing versions or create historical release tags implying a release that cannot be verified.
- Do not delete historical release tags, rewrite published history, or remove archived artifacts unless the user explicitly requests that specific destructive action.
- Git history alone is not a substitute for the discoverable archive. Maintain `history/SHA256SUMS`; compare archived bytes against the original source and run `sha256sum -c history/SHA256SUMS` from the repository root after archive changes.

## Evolution and validation

- Base 1.x evolution on preserved 1.0 evidence, published 1.2 artifacts and explicitly agreed decisions. Do not treat a proposal as an approved field/type change.
- Explain each proposed rename, type change or restriction, its benefit and its effect on legacy consumers. Preserve source information and document any conversion ambiguity or loss.
- A declared `barba_cv_version` is evidence, not proof. Distinguish structural compatibility, declared-version conformance and conversion. Report ambiguous version matches honestly.
- Empty arrays in a historical template do not establish their item types. Seek representative data or document the uncertainty rather than inventing a rule.
- Historical artifacts may contain defects. Archiving or parsing them as JSON does not certify them as usable validators. Keep validation claims precise.

## Repository workflow

- Confirm the destination is `Eurobotics-Association/barba-cv` and the local checkout is `/home/rfv/Github_local/barba-cv` before changes.
- Use the GitHub plugin for all GitHub reads and writes. Do not use `git push`, `gh`, raw GitHub API requests or another GitHub client. Local-only Git operations are allowed.
- Check local changes and live GitHub state before editing; preserve unrelated work. Use a review branch and pull request for repository changes.
- Keep current schema, templates and documentation consistent when an evolution is approved. Publish stable version-specific references and document which versions developers can read or write.
- Do not modify unrelated repositories.
