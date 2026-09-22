# FortiGate Extract

FortiGate CLI configuration extractor and Excel reporting tool.

The project parses FortiGate configuration backups into a small FortiGate-specific source model, builds derived review views, validates relationships, and produces a structured Excel workbook.

The current focus is **deep and reliable FortiGate extraction and analysis**. It is not a multi-vendor migration framework.

## Pipeline

```text
FortiGate CLI
    ↓
Tokenizer
    ↓
Parser
    ↓
Command Evaluator
    ↓
FGConfig
    ↓
Relationships / Transforms
    ↓
DerivedViews
    ↓
Validation
    ↓
Excel Report
```

The responsibility rule for the repository is:

```text
Tokenizer
    syntax only

Parser
    hierarchy / structure only

Command Evaluator
    explicit set / append / unset state + primitive typing

FortiGate Models
    small migration-relevant source fields + raw extras

Relationships
    cross-object references and topology

Transforms
    FortiGate semantics, normalization and derived views

Validation
    detect and report problems only

Excel Exporter
    presentation only
```

There is no vendor-neutral IR.

The central source object is `FGConfig`. Calculated report information is carried separately in `DerivedViews`.

> **FGConfig is explicit FortiGate source state. DerivedViews contains calculated report semantics. Excel presents both; it does not create semantics itself.**

---

## Quick Start

### Requirements

- Python 3.12 (the version exercised by CI)
- Windows for the bundled `run_excel_report.bat` launcher
- A UTF-8 FortiGate CLI backup by default

### Windows

Create a virtual environment and install dependencies:

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

Launch the local Excel report UI:

```bat
run_excel_report.bat
```

The local UI runs at:

```text
http://127.0.0.1:5000/
```

Workflow:

```text
Upload FortiGate configuration
→ Preview extracted inventory
→ Review validation counts
→ Download Excel report
```

Recommended filename extensions:

```text
.conf
.cfg
.txt
```

The browser file picker filters for these extensions. The server accepts any
non-empty filename containing a valid FortiGate CLI backup. Web uploads are
decoded as UTF-8 and limited to 32 MiB.

### CLI

The same extraction pipeline can be used without the web interface.

```bat
set PYTHONPATH=src

python -m fortigate_extract.main extract ^
    --input firewall.conf ^
    --output firewall_inventory.xlsx
```

Optional YAML extraction configuration:

```bat
python -m fortigate_extract.main extract ^
    --input firewall.conf ^
    --output firewall_inventory.xlsx ^
    --config extraction.yaml
```

Currently, only input encoding is an active YAML setting:

```yaml
encoding: utf-8
```

Other fields in the internal configuration model are not yet supported as
runtime controls and should not be relied on.

---

## Excel Report

The workbook is intended for:

- configuration review
- migration preparation
- firewall inventory
- topology review
- dependency checking
- identifying unresolved references
- identifying source-only or unsupported configuration

The original FortiGate inventory workbook is used as the **content and field compatibility baseline**, but the new exporter does not preserve obsolete architecture simply for compatibility.

The report follows this rule:

```text
Preserve useful original fields
+ add useful current source information
+ add current derived information
+ improve hierarchy and readability
- old vendor-neutral IR fields
- target-vendor artifacts
- redundant duplicate columns
- unsafe secret values
```

### Workbook organization

The workbook is broadly organized into:

```text
Overview
System
Network
Objects
Policies / NAT
Routing
SD-WAN
VPN
DHCP
SSL VPN
Identity / Authentication
Security
Source Appendix
Validation / Coverage
```

Every workbook follows a fixed schema. Important areas include:

- `Summary` and `Review Required`
- system, DNS, NTP settings, and nested NTP server objects
- interfaces, secondary IPs, zones, and topology
- addresses, services, policies, and NAT
- routes, VPN, DHCP, SD-WAN, and SSL VPN
- users, administrators, and security profiles
- unresolved references, unsupported coverage, and source inventory

The exact worksheet order is defined by
[`SHEET_ORDER`](src/fortigate_extract/export/excel_schema.py). Warnings are
reported through `Review Required` rather than a separate `Warnings` sheet.

Explicit configuration without a dedicated typed model is preserved as rows
in `FortiGate Source Inventory`, `Unsupported`, and `Extraction Coverage`.
Selected source-only sections may also have dedicated presentation worksheets
when that improves traceability; source evidence does not create worksheets
automatically by default.

`Extraction Evidence` is intentionally not part of the standard workbook. Traceability is kept in the relevant object sheets, source appendix, validation sheets, and coverage sheets.

---

## Source Data vs Derived Data

### Source models

Source models represent explicitly configured FortiGate state.

For example:

```text
config firewall policy
    edit 10
        set srcintf "LAN"
        set dstintf "WAN"
        set action accept
    next
end
```

The source model stores what was explicitly configured.

A missing field means:

```text
not explicitly configured
```

It does **not** automatically mean a FortiOS default.

Typed models intentionally stay small. Explicit source settings that do not need a dedicated model field are preserved through `raw_extra` or generic source inventory where practical.

### Derived views

Derived information is built after source extraction.

Current derived areas include:

- interface topology
- VPN-to-interface topology
- normalized services
- normalized service groups
- source NAT views
- normalized policy names
- normalized VPN Phase 2 selectors
- reference resolution

Derived logic belongs in:

```text
relationships/
transform/
derived.py
```

It does not belong in the tokenizer, parser, or source models.

---

## Interface Topology

The Interfaces worksheet is topology-aware.

Example:

```text
◆ agg1
├─ ● port1       Member of agg1
├─ ● port2       Member of agg1
│
├─ ▣ vlan100     Child of agg1
│  └─ ◈ VPN-HQ   Child of vlan100
│
└─ ▣ vlan200     Child of agg1
```

Symbols:

```text
◆  aggregate / redundant interface
●  physical interface
▣  VLAN / logical child
◈  VPN / tunnel
◇  other logical interface
```

The hierarchy is derived from `relationships/interface_topology.py`; it is presentation metadata and does not modify source interface objects.

---

## Policy Reporting

The Policies worksheet should primarily expose useful FortiGate policy data plus current validation/analysis information.

The intended direction is:

```text
Policy identity
Match criteria
Action / NAT
Logging
Security profiles
Description / source metadata
Review status
```

Old workbook fields are not retained blindly.

In particular:

- redundant `Original` / `Normalized` duplicates should only remain when a current transform produces a genuinely different value;
- `Effective ...` fields should only exist when FortiGate effective semantics are actually calculated;
- old cross-vendor or target-vendor profile fields should not be part of the normal FortiGate policy report;
- uncommon explicit policy settings may remain in `Additional Settings` rather than becoming permanent first-class columns.

This keeps the policy report readable without losing explicit source configuration.

---

## Explicit Fields and Additional Settings

Two report concepts are important for traceability:

```text
Source Explicit Fields
Additional Settings
```

`Source Explicit Fields` records fields explicitly present in the FortiGate source.

`Additional Settings` contains safe preserved source values that are not represented by dedicated report columns.

Conceptually:

```text
raw_extra
    ↓
secret sanitization
    ↓
Additional Settings
```

This allows the typed source models to remain small without silently discarding useful source configuration.

---

## Source Inventory

Not every FortiGate section needs a first-class typed model.

Explicit configuration from advanced or currently unsupported sections can be preserved generically as source evidence.

Examples may include:

- routing protocol settings
- authentication-server configuration
- Internet Service definitions
- advanced SSL VPN child configuration
- DoS configuration
- other explicit FortiGate sections

These records can be surfaced through:

```text
FortiGate Source Inventory
Unsupported
Extraction Coverage
```

Generic source capture preserves explicit source state only. It does not insert FortiOS defaults or perform semantic conversion.

---

## Validation

Validation detects problems without silently changing source data.

Current validation covers areas such as:

- duplicate object definitions and ambiguous source identity
- broken object references
- missing interfaces
- missing addresses or address groups
- missing services or service groups
- topology issues
- service normalization issues
- NAT transformation issues
- policy issues
- VPN issues

Validation results feed report areas such as:

```text
Review Required
Unresolved References
Warnings
```

Preferred behavior:

```text
detect
→ explain
→ preserve source
```

not:

```text
detect
→ silently repair
```

---

## Security

FortiGate backups may contain credentials and other sensitive values.

Actual secret values must never be exported to Excel or written to logs.

Examples include:

- passwords
- pre-shared keys
- private keys
- API keys
- authentication secrets
- tokens
- key strings

Where useful, safe metadata may be exposed instead:

```text
Password Configured = Yes
PSK Configured = Yes
Credential Configured = Yes
```

Raw extras and generic source records pass through the same secret-sanitization rules before Excel export.

The bundled web launcher binds to `127.0.0.1`. Do not expose the development
server directly to untrusted networks.

---

## Project Structure

```text
src/fortigate_extract/
├── tokenizer.py / parser.py / command_evaluator.py
├── model/             FortiGate source models
├── extraction/        Domain extraction, source inventory, and metadata
├── relationships/     Reference resolution and interface topology
├── transform/         FortiGate normalization and derived semantics
├── validation/        Non-mutating validation
├── export/            Excel schema and workbook generation
├── fortios/           FortiOS-specific reference data
├── security/          Secret detection and sanitization
├── web.py             Web and desktop application entry points
├── web_report.py      Browser report serialization
├── templates/         Web UI templates
└── static/            Web UI assets
```

---

## Architecture Rules

### Tokenizer

Syntax only.

It recognizes FortiGate CLI constructs such as:

```text
config
edit
set
unset
append
next
end
comments
strings
unknown commands
```

It must not understand FortiGate object semantics.

### Parser

Structure only.

It builds:

```text
FortiGateConfigTree
ConfigNode
EditNode
CommandNode
UnknownCommandNode
CommentNode
```

It must not apply FortiOS defaults or create report objects.

### Command Evaluator

Evaluates explicit command state in source order:

```text
set
append
unset
```

It also performs primitive field typing according to `section_registry.py`.

### FortiGate Models

Represent small FortiGate-specific source concepts.

They contain migration/review-relevant typed fields, `explicit_fields`, and preserved `raw_extra`.

They are not a vendor-neutral IR.

### Relationships

Resolve cross-object meaning such as:

```text
VLAN → parent interface
aggregate → member interfaces
VPN → attached interface
policy → referenced objects
```

Relationships do not mutate source models.

### Transforms

Contain FortiGate semantics, normalization, defaults where explicitly supported, and report-oriented conversions.

Examples:

```text
service normalization
source NAT derivation
policy name normalization
VPN selector normalization
```

### Validation

Detects and reports problems.

It does not silently rewrite the configuration.

### Excel Exporter

Consumes:

```text
ExtractionResult / FGConfig
+
DerivedViews
+
ValidationResult
```

and produces the workbook.

The exporter is responsible for:

- worksheet selection
- column ordering
- formatting
- filters
- freeze panes
- hierarchy presentation
- workbook navigation
- review highlighting
- safe source presentation

It should not become a second FortiGate semantic engine.

---

## Testing

Run the current regression tests with:

```bat
set PYTHONPATH=src
python -m unittest discover -s tests -v
```

For pull requests, GitHub Actions uses Python 3.12, compiles `src` and `tests`,
and then runs the same test command.

Current regression coverage includes:

- parsing, source extraction, and source preservation
- relationships, topology, derived views, and validation
- Excel workbook structure and presentation
- secret-value leakage prevention
- web report rendering, preview, and Excel download

---

## Development Principles

Priority:

```text
correctness
→ explicit source preservation
→ clear semantics
→ traceability
→ maintainability
→ broader coverage
```

When FortiGate behavior is uncertain:

1. preserve the explicit source value;
2. do not invent a default;
3. do not guess target-vendor behavior;
4. keep unsupported source data visible through `Additional Settings` or source inventory where practical;
5. add semantics only when supported by FortiGate documentation or verified behavior.

---

## Non-Goals

The current project does not aim to provide:

- a vendor-neutral IR
- Cisco / Check Point / Juniper / PAN source parsers
- target-vendor configuration generators
- Terraform generation
- automatic firewall deployment
- SQLite report persistence
- `.fgreport` databases
- browser-side SQLite
- generic migration orchestration

These concerns should not be introduced into the tokenizer, parser, source models, or Excel exporter.

---

## Support and Licensing

Report defects through this repository's GitHub issue tracker. Use a minimal,
sanitized configuration sample and never attach production secrets.

This repository currently has no declared license. Add the intended `LICENSE`
file before presenting it as reusable or open-source software.

---

## Technical Reference

FortiGate semantics should be based on official Fortinet FortiOS CLI documentation and verified source behavior.

Version-specific behavior belongs in dedicated FortiOS semantic helpers rather than in the tokenizer, parser, or Excel exporter.
