# Contributing to Barba-CV

Thank you for your interest in improving the Barba-CV standard.

Barba-CV is an open JSON standard designed to represent CV and resume data in a deterministic and machine-readable format.

## Types of contributions

We welcome contributions such as:

• improvements to the JSON schema
• additional example CV files
• documentation improvements
• integration guidance for AI systems and ATS platforms

## Schema changes

Changes to the schema should be proposed via pull requests and must include:

• a clear explanation of the change
• updates to documentation if necessary
• updated example JSON files if the schema structure changes

Schema evolution should maintain backward compatibility whenever possible.

Use a version-specific schema path for each released contract. Give every defined field a concise JSON Schema `description` that matches the [field reference](docs/field-reference.md), and update the example and compatibility guidance when semantics change. Preserve earlier published artifacts under [`history/`](history/README.md).

Before opening a pull request, run:

```sh
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
sha256sum -c history/SHA256SUMS
```

The GitHub pull-request check runs the contract tests and validates the released 1.3 example and template.

## Discussions

Major changes to the standard should first be discussed in GitHub issues before submitting a pull request.
