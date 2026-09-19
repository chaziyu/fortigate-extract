# AGENTS.md

## Project purpose

`fortigate-extract` extracts FortiGate configuration data into a structured FortiGate-specific model and exports it for review, primarily to Excel.

Current scope:

```text
FortiGate config file
→ parse
→ FortiGate model
→ validate
→ export
```

Do not introduce multi-vendor migration logic unless explicitly requested.

## Architecture rules

Follow these responsibilities strictly:

```text
Tokenizer   → syntax only
Parser      → structure + explicitly configured source data only
Model       → FortiGate-specific fields + raw extras
Validation  → references, consistency, unsupported values
Exporter    → presentation only
```

Do not place vendor semantics or inferred defaults in the tokenizer or structural parser.

## Parser rules

The parser must:

- preserve FortiGate hierarchy
- preserve explicit `config`, `edit`, `set`, `unset`, `append`, `select`, `next`, `end`
- preserve original values where practical
- preserve unknown settings instead of silently dropping them
- avoid guessing FortiOS defaults
- avoid converting data into vendor-neutral concepts
- fail visibly on malformed input

The parser should represent what the configuration says, not what it might mean on another firewall.

## FortiGate model rules

Models should remain close to FortiOS concepts.

Examples:

- interface
- zone
- address
- address group
- custom service
- service group
- schedule
- firewall policy
- VIP
- IP pool
- static route
- VPN
- security profile

Use typed fields only for data relevant to extraction and review.

Preserve unsupported or currently unused settings in `raw_extra` or equivalent storage.

Do not create a generic IR layer.

## Semantics and defaults

Do not inject undocumented defaults during parsing.

If FortiOS defaults or derived behavior are needed, handle them in a separate interpretation or validation step.

Keep these distinct:

```text
explicit source value
derived value
FortiOS default
unknown value
```

Never make them indistinguishable.

## Validation rules

Validation should detect, not silently fix.

Examples:

- missing address-group members
- missing service-group members
- invalid policy references
- missing interfaces or zones
- duplicate objects
- unsupported values
- malformed objects
- unresolved references

Return warnings or errors with enough context to identify the source object.

Do not mutate configuration data during validation unless explicitly required.

## Export rules

Exporters must not contain parsing or FortiGate semantic logic.

They should only convert validated model data into output formats.

Primary output:

```text
Excel workbook
```

Recommended worksheets:

- Summary
- Interfaces
- Zones
- Addresses
- Address Groups
- Services
- Service Groups
- Schedules
- Policies
- VIPs
- IP Pools
- Static Routes
- VPN
- Security Profiles
- Validation Issues

## Security rules

FortiGate configuration may contain sensitive data.

Never expose secrets in exported reports.

Redact or omit:

- passwords
- pre-shared keys
- API keys
- private keys
- SNMP communities
- authentication secrets
- tokens

Do not log sensitive values.

## Scope control

Do not add these unless explicitly requested:

- vendor-neutral IR
- other firewall vendors
- Terraform
- live API ingestion
- SSH collection
- deployment
- background jobs
- web authentication
- RBAC
- plugin systems
- generic multi-vendor registries

Prefer the smallest implementation that satisfies FortiGate extraction.

## Coding style

Before editing:

- inspect existing logic
- reuse existing FortiGate code where appropriate
- make the smallest required change
- avoid unrelated refactoring

Prefer:

- small modules
- explicit names
- typed models
- deterministic behavior
- clear error reporting

Avoid:

- hidden fallbacks
- implicit data loss
- large generic abstractions
- premature framework design

## Testing

Every supported FortiGate feature should have fixtures and tests.

Test at least:

```text
input config
→ parsed structure
→ FortiGate model
→ validation
→ exported values
```

Include tests for:

- quoted names
- spaces in values
- nested `config`
- empty sections
- duplicate entries
- unknown settings
- malformed blocks
- unresolved references
- VDOM-aware configuration where supported
- secret redaction

Do not claim tests passed unless they were actually run.

## Source of truth

Use official Fortinet FortiOS CLI documentation as the primary reference.

When behavior is unclear:

1. preserve the raw source
2. mark the behavior as unknown or unsupported
3. do not guess

Current implementation should prioritize **correct extraction over broad feature coverage**.