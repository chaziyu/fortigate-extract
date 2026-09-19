# FortiGate Extract

A focused Python tool for extracting FortiGate configuration data into structured FortiGate-specific models and exporting the results for review.

The project currently focuses on **accurate FortiGate extraction**, not multi-vendor migration.

## Goal

```text
FortiGate configuration
→ parse
→ FortiGate model
→ validate
→ export
```

Primary output:

```text
Excel workbook
```

## Scope

Current scope includes FortiGate configuration extraction such as:

- System information
- Interfaces
- Zones
- Address objects
- Address groups
- Custom services
- Service groups
- Schedules
- Firewall policies
- VIPs
- IP pools
- Static routes
- VPN configuration
- Security profiles
- Reference and validation issues

Coverage will be added gradually.

## Architecture

The project follows these responsibilities:

```text
Tokenizer
→ syntax only

Parser
→ hierarchy and explicitly configured source data

FortiGate model
→ FortiGate-specific structured data

Validation
→ references, consistency, unsupported values

Exporter
→ output formatting only
```

The parser should preserve what exists in the source configuration.

It should not:

- convert data into a vendor-neutral IR
- infer target-vendor behavior
- silently insert FortiOS defaults
- silently discard unsupported settings

Unknown or currently unsupported settings should be preserved where practical.

## Example

Input:

```text
config firewall address
    edit "SERVER01"
        set subnet 10.10.10.5 255.255.255.255
        set comment "Production server"
    next
end
```

Structured result:

```text
FortiGateAddress
- name: SERVER01
- subnet: 10.10.10.5/32
- comment: Production server
```

The data can then be exported into an Excel worksheet for review.

## Excel output

The workbook may contain worksheets such as:

```text
Summary
Interfaces
Zones
Addresses
Address Groups
Services
Service Groups
Schedules
Policies
VIPs
IP Pools
Static Routes
VPN
Security Profiles
Validation Issues
```

The Excel output is intended for:

- configuration review
- migration preparation
- object inventory
- dependency checking
- identifying unsupported or unresolved configuration

## Validation

Validation should detect issues without silently modifying the source data.

Examples:

```text
Address group references missing address
Service group references missing service
Policy references unknown object
Policy references missing interface or zone
Duplicate object
Unsupported setting
Malformed configuration
```

Validation results should include enough source context to identify the affected object.

## Security

FortiGate configuration files may contain sensitive values.

Sensitive data should not be exported or logged.

Examples:

- passwords
- pre-shared keys
- API keys
- private keys
- SNMP communities
- authentication secrets
- tokens

Sensitive values should be redacted or omitted.

## Non-goals

The following are intentionally outside the current scope:

- Vendor-neutral IR
- Multi-vendor migration
- Terraform
- Live API ingestion
- SSH collection
- Automatic deployment
- Background job processing
- Web authentication
- RBAC
- Generic plugin systems
- Target firewall generation

These may be considered later if there is a clear requirement.

## Project structure

Example structure:

```text
fortigate-extract/
├── AGENTS.md
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── .gitattributes
│
├── documentation/
│
├── src/
│   └── fortigate_extract/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── web.py
│       │
│       ├── tokenizer.py
│       ├── nodes.py
│       ├── parser.py
│       ├── section_registry.py
│       ├── command_evaluator.py
│       │
│       ├── model/
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── interface.py
│       │   ├── zone.py
│       │   ├── address.py
│       │   ├── service.py
│       │   ├── policy.py
│       │   ├── ippol.py
│       │   ├── vip.py
│       │   ├── route_static.py
│       │   ├── vpn.py
│       │   ├── vpn_ssl.py
│       │   ├── dhcp.py
│       │   ├── sdwan.py
│       │   ├── user.py
│       │   ├── admin.py
│       │   ├── ips.py
│       │   └── security_profile.py
│       │
│       ├── extraction/
│       │   ├── __init__.py
│       │   ├── extractor.py
│       │   ├── result.py
│       │   ├── interfaces.py
│       │   ├── addresses.py
│       │   ├── services.py
│       │   ├── schedules.py
│       │   ├── policies.py
│       │   ├── nat.py
│       │   ├── routing.py
│       │   ├── vpn.py
│       │   └── security_profiles.py
│       │
│       ├── validation/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── references.py
│       │   ├── validators.py
│       │   └── coverage.py
│       │
│       ├── fortios/
│       │   ├── __init__.py
│       │   ├── predefined_services.py
│       │   ├── firewall_vip_746.py
│       │   └── firewall_ip_746.py
│       │
│       ├── security/
│       │   ├── __init__.py
│       │   ├── redaction.py
│       │   └── secrets.py
│       │
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── network.py
│       │   ├── mac.py
│       │   └── certificate.py
│       │
│       ├── export/
│       │   ├── __init__.py
│       │   └── excel.py
│       │
│       ├── templates/
│       └── static/
│
├── tests/
│   ├── fixtures/
│   ├── test_tokenizer.py
│   ├── test_parser.py
│   ├── test_extraction.py
│   ├── test_validation.py
│   └── test_export.py
│
└── examples/
```

## Development principles

The project prioritizes:

```text
Correctness
→ traceability
→ clear warnings
→ maintainability
→ broader coverage
```

When FortiGate behavior is unclear:

1. Preserve the original source data.
2. Mark it as unknown or unsupported.
3. Do not guess.

## Testing

Supported features should include fixtures and tests covering:

```text
input config
→ parsed structure
→ FortiGate model
→ validation
→ exported values
```

Important cases include:

- quoted object names
- nested `config` blocks
- empty sections
- duplicate entries
- unknown settings
- malformed configuration
- unresolved references
- VDOM-aware configuration
- sensitive-value redaction

## High Level View

At a high level, the program should now work like this:

```text
FortiGate config file
        ↓
tokenizer.py
        ↓
parser.py
        ↓
nodes.py structural tree
        ↓
section_registry.py + command_evaluator.py
        ↓
extraction/<domain>.py
        ↓
model/<domain>.py
        ↓
relationship / derived extraction
        ↓
validation/
        ↓
Excel export
```

### 1. Tokenizer

`tokenizer.py` reads raw FortiGate CLI text and converts it into simple syntax tokens:

```text
config
edit
set
unset
append
next
end
string
comment
```

It should not know what an IP address, service, interface, or policy means.

Example:

```text
set subnet 10.0.0.0 255.255.255.0
```

becomes roughly:

```text
SET
STRING subnet
STRING 10.0.0.0
STRING 255.255.255.0
```

### 2. Parser

`parser.py` consumes those tokens and builds the source structure only.

Example:

```text
config firewall address
    edit "LAN"
        set subnet 10.0.0.0 255.255.255.0
    next
end
```

becomes:

```text
ConfigNode("firewall address")
└── EditNode("LAN")
    └── CommandNode(
            operation="set",
            key="subnet",
            values=[...]
        )
```

The parser still does not construct `FGAddress`.

### 3. Structural nodes

`nodes.py` stores the syntax tree:

```text
FortiGateConfigTree
ConfigNode
EditNode
CommandNode
UnknownCommandNode
CommentNode
```

This is the authoritative representation of what was structurally present in the source configuration.

### 4. Section registry

`section_registry.py` tells the evaluator how basic fields behave.

For example:

```python
"firewall policy":
    srcintf -> list
    dstintf -> list
    session_ttl -> integer
    action -> scalar
```

It does not construct models or apply FortiOS defaults.

### 5. Command evaluator

`command_evaluator.py` evaluates commands inside one object in source order:

```text
set
append
unset
```

For example:

```text
set member A B
append member C
unset comment
```

produces explicit source state roughly like:

```python
attributes = {
    "member": ["A", "B", "C"],
}

explicit_fields = {
    "member",
}

unset_fields = {
    "comment",
}
```

Unknown fields go into:

```python
raw_extra
```

Secret values are discarded, with only presence tracked.

### 6. Domain extraction

Now the files in `extraction/` interpret FortiGate sections.

For example:

```text
extraction/addresses.py
    firewall address
    firewall addrgrp
        ↓
    FGAddress
    FGAddressGroup
```

```text
extraction/vpn.py
    phase1-interface
    phase2-interface
        ↓
    FGIPsecPhase1
    FGIPsecPhase2
```

```text
extraction/routing.py
    router static
        ↓
    FGStaticRoute
```

This is where source syntax gets mapped into the small FortiGate-specific models.

### 7. Source models

The `model/` folder represents explicit FortiGate source concepts:

```text
FGInterface
FGAddress
FGService
FGPolicy
FGIPPool
FGVIP
FGStaticRoute
FGIPsecPhase1
FGIPsecPhase2
...
```

Important rule:

```text
None
= not explicitly configured
```

Do not insert FortiOS defaults into these models.

### 8. FortiOS semantic helpers

Files under:

```text
fortios/
```

contain vendor knowledge such as:

```text
firewall_ip_746.py
firewall_vip_746.py
predefined_services.py
```

They handle things like:

```text
documented FortiOS defaults
valid ranges
predefined objects
version-specific semantics
```

For example:

```python
effective_vip_settings_746(vip)
```

may derive an effective default without modifying `FGVIP`.

### 9. Relationship and derived extraction

After all source objects exist, resolve cross-object relationships.

Examples:

```text
VLAN → parent interface
Phase2 → Phase1
Phase1 → interface
policy → addresses
policy → services
policy → schedule
policy → IP pool
policy destination → VIP
SD-WAN member → interface
```

Derived report data also happens here.

For example:

```text
FGPolicy
FGIPPool
FGVIP
FGVIPGroup
    ↓
extraction/nat.py
    ↓
ExtractedNATRule
```

`ExtractedNATRule` is a report view, not a FortiGate source object.

### 10. Validation

`validation/` checks things such as:

```text
unresolved references
invalid addresses
invalid ranges
malformed IDs
unsupported explicit settings
missing required relationships
```

It should detect problems, not silently repair them.

### 11. Excel exporter

Finally:

```text
FGConfig
+ derived report views
+ validation results
        ↓
Excel workbook
```

The exporter should mainly format data into sheets.

It should not contain FortiGate parsing or semantic logic.

So the overall responsibility is:

```text
Tokenizer
    syntax

Parser
    structure

Command evaluator
    explicit command state

Extraction
    FortiGate source semantics

Models
    FortiGate objects

FortiOS helpers
    defaults / vendor rules

Relationships
    cross-object meaning

Validation
    detect problems

Exporter
    presentation
```

That separation is the main design goal of the refactor.

## Reference

The primary technical reference is the official Fortinet FortiOS CLI documentation.

Current work should focus on **deep and reliable FortiGate extraction before adding migration or other vendors**.
```