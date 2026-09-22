# AGENTS.md

## Purpose

`fortigate-extract` is a FortiGate CLI extraction and Excel reporting tool.

Current pipeline:

```text
FortiGate CLI
→ Tokenizer
→ Parser
→ Command Evaluator
→ FGConfig
→ Relationships / Transforms
→ DerivedViews
→ Validation
→ Excel
```

There is no vendor-neutral IR.

## Core Rules

```text
Tokenizer
    syntax only

Parser
    structure only

Command Evaluator
    set / append / unset state
    primitive typing only

FGConfig / source models
    explicit FortiGate source data
    small migration-relevant fields
    raw_extra for preserved extras

Relationships
    references / topology
    do not mutate source models

Transforms
    FortiGate semantics
    normalization
    supported defaults / conversions
    derived report views

Validation
    detect and report only

Excel
    presentation only
```

## Source Data

`FGConfig` represents explicit source state.

A missing value means:

```text
not explicitly configured
```

Do not silently treat it as a FortiOS default.

Keep these distinct:

```text
explicit source
derived value
effective/default value
unknown value
```

Do not add source-model fields only to satisfy Excel.

Preserve useful unsupported settings through:

```text
raw_extra
Source Inventory
source appendix sheets
```

## Semantics

Do not put FortiGate semantics or defaults in:

```text
tokenizer
parser
command evaluator
Excel exporter
```

Cross-object meaning belongs in `relationships/`.

FortiGate defaults, normalization and conversions belong in `transform/` or dedicated FortiOS helpers.

## Excel

The original workbook is the content compatibility baseline, not an architecture to restore.

Use:

```text
keep useful original fields
+ add current source fields
+ add genuine derived fields
- old IR fields
- target-vendor fields
- redundant duplicates
- unsupported fake/effective fields
```

`Additional Settings` is for useful explicit source fields that do not justify permanent columns.

Only expose `Effective ...` fields when the current transform actually calculates them.

Do not duplicate `Original / Normalized` columns unless the values genuinely differ.

Interface hierarchy must come from the topology relationship model, not parser changes.

## Validation

Validation must not silently repair or mutate configuration.

Report problems with enough context to identify the affected object.

## Security

Never export or log actual secrets:

```text
passwords
PSKs
private keys
API keys
tokens
authentication secrets
key strings
```

Safe metadata such as `Password Configured = Yes` is allowed.

All raw/source-extra output must pass through the existing sanitization layer.

## Scope

Do not reintroduce unless explicitly requested:

```text
vendor-neutral IR
multi-vendor architecture
target-vendor generators
Terraform
SQLite / .fgreport
generic migration framework
```

## Change Discipline

Before editing:

1. inspect the actual current branch;
2. inspect existing paths, models and symbols;
3. do not guess names or APIs;
4. make the smallest coherent change;
5. avoid unrelated refactoring.

Prefer package-relative imports.

Do not restore old code just because the old Excel workbook contained fields produced by it.

## Testing

Test the affected path:

```text
source
→ parser
→ FGConfig
→ DerivedViews
→ validation
→ Excel
```

Important regressions:

```text
VDOM handling
nested config
unknown fields
reference resolution
interface topology
Excel compatibility
secret redaction
web preview
Excel download
```

Do not claim tests pass unless they were actually run.

## Reference

Use official Fortinet FortiOS CLI documentation as the primary semantic reference.

When behavior is unclear:

```text
preserve source
→ mark unknown/source-only
→ do not guess
```

Priority:

```text
correctness
→ source preservation
→ clear semantics
→ traceability
→ maintainability
```
