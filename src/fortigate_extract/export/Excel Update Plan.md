I inspected `feature/excel-report-v2` at commit `d53b10d799c7adf6b15766c6b916abafdda1a6bd`. No code was modified.

The main issue is that the branch is already moving toward the new design, but `excel_schema.py` still exposes many sheets and technical columns that the finalized design removes. `excel.py` also still contains old presentation behavior such as hierarchical interface names, combined service protocol/port fields, old policy/NAT names, and separate warning/source-detail sheets.

The design contract is clear that blanks mean “not explicitly configured,” derived/effective values require real upstream calculations, and Excel is presentation only. :chatgpt-content-reference{index="0"} The final workbook order is also explicitly constrained. :chatgpt-content-reference{index="1"}

## Phase 1: Replace the Excel schema contract

**Objective**

Make `excel_schema.py` exactly represent the final workbook instead of maintaining compatibility with the current oversized workbook.

**Files / locations**

- `src/fortigate_extract/export/excel_schema.py`
  - `OBJECT_TAIL`: lines 12–19
  - `CHILD_TAIL`: lines 21–26
  - `SOURCE_HEADERS`: lines 28–38
  - `SHEET_ORDER`: starts line 50
  - `SHEET_HEADERS`: starts line 202
  - `SOURCE_ONLY_SHEETS`: near the end of the file

**Required changes**

- Replace `SHEET_ORDER` with the exact final order from `Excel Design.md`.
- Remove all sheets not in that order.
- In particular remove dedicated sheets for:
  - `Address Group Tags`
  - `Service Categories`
  - `Schedules`
  - `Schedule Groups`
  - `Local-In Policies`
  - `Multicast Policies`
  - `Policy Routes`
  - `DHCP Exclude Ranges`
  - routing protocol/session TTL sheets
  - extra SD-WAN child sheets
  - SSL VPN host-check/bookmark/landing-page sheets
  - LDAP/RADIUS/TACACS/SAML/FSSO source-only sheets
  - authentication source-only sheets
  - Internet Service source-only sheets
  - DoS/sniffer/IPv6 EH sheets
  - `Warnings`
  - `Firewall Policy Source Settings`
  - `Interface Source Settings`
  - `Interface Nested Configuration`
- Move `NAT Rules` before `IP Pools`, matching the design.
- Stop using universal `OBJECT_TAIL` / `CHILD_TAIL` if they force columns onto sheets that should not contain them.
- Prefer exact per-sheet tuples for `SHEET_HEADERS`.

The current tails automatically inject:

```text
Extraction Status
Manual Review
Source Explicit Fields
Additional Settings
```

onto many sheets. The finalized design generally wants:

```text
Analysis Status
Review Reasons
```

plus `Source Explicit Fields` or `Additional Settings` only where explicitly specified.

- Replace the generic `SOURCE_HEADERS` use for the retained direct-source sheets:
  - `System Settings`
  - `DNS Settings`
  - `NTP Settings`
- Their schemas should match the compact source views in the design rather than the current generic `VDOM / Parent / Extraction Status / Manual Review` structure.
- Add schema metadata such as:
  - derived columns by sheet;
  - technical/provenance columns;
  - optionally columns hidden by default.

The design explicitly places `Source Explicit Fields` and `Additional Settings` at the far right and permits hiding them by default. :chatgpt-content-reference{index="2"}

**What not to change**

- No `FGConfig` changes.
- No parser/tokenizer changes.
- No source fields added just for Excel.
- No vendor-neutral model.
- No shared frontend/reporting layer yet.

**Risk**

The biggest compatibility break is sheet removal. Tests must check exact sheet order rather than simply checking that a few sheets exist.

**Validation**

Add an exact assertion:

```python
workbook.sheetnames == expected_sheet_order
```

and explicit absence checks for every removed category.

---

## Phase 2: Close the semantic gaps before Excel consumes the data

**Objective**

Ensure Excel only presents semantics that are already produced by transforms/relationships/validation.

The service, policy, NAT, VPN, and topology transforms already cover most of the new design. Services must be split upstream, policy names normalized upstream, interface NAT resolved upstream, and VPN selectors normalized upstream. :chatgpt-content-reference{index="3"} :chatgpt-content-reference{index="4"}

### Service generated-state

**File**

- `src/fortigate_extract/transform/services.py`
  - `NormalizedService`: line 10
  - `transform_services()`: line 66
  - `_generated_name()`: line 335

**Existing logic**

The transform already:
- creates one service when there is one normalized result;
- generates numbered services for multiple results;
- creates the original name as a generated service group;
- resolves generated-name collisions deterministically.

**New logic**

Add explicit derived state to `NormalizedService`:

```text
generated = False
```

for a single retained source service, and:

```text
generated = True
```

for generated child services.

Do not infer `Generated` inside Excel from `name != source_name`.

`NormalizedServiceGroup.generated` already exists and should be reused.

### NAT ambiguity

**File**

- `src/fortigate_extract/transform/nat.py`
  - `NormalizedSourceNAT`: line 19
  - `_interface_nat()`: line 165

**Existing problem**

When multiple possible egress interfaces exist, `_interface_nat()` currently:
- derives addresses for each interface;
- adds an ambiguity issue;
- still returns those addresses.

The design requires:

```text
SNAT Address = blank
Analysis Status = REVIEW_REQUIRED
```

when runtime egress is ambiguous. :chatgpt-content-reference{index="5"}

**Required change**

When more than one possible egress interface remains:

- retain `egress_interfaces`;
- retain the ambiguity issue;
- return no `translated_addresses`.

Do not choose an address.

Dynamic DHCP/PPPoE handling is already correct and should remain unchanged.

### Broken references

**Files**

- `src/fortigate_extract/derived.py`
  - `DerivedViews`: line 33
  - `build_derived_views()`: line 49
- `src/fortigate_extract/validation/validator.py`
  - `validate_config()`: line 21
- `src/fortigate_extract/export/excel.py`
  - `_unresolved_reference_rows()`: line 2202

**Existing problem**

Excel currently calls `collect_broken_references()` itself.

That is relationship resolution inside the presentation layer.

**Required change**

Add the already-calculated broken-reference collection to `DerivedViews`.

Flow becomes:

```text
Relationships
→ DerivedViews.broken_references
→ Validation
→ Excel
```

Then:

- `validator.py` consumes `derived.broken_references`;
- `_unresolved_reference_rows()` only formats that collection.

No reference resolution should occur in `excel.py`.

### Load-balancing VIP validation

**Files**

- `src/fortigate_extract/validation/validator.py:21`
- reuse `FGVIP.realservers` from `src/fortigate_extract/model/vip.py:22`

Add validation only; do not repair the VIP.

For an explicitly configured VIP type of `load-balance` or `server-load-balance`, report `REVIEW_REQUIRED` when fewer than two usable configured backends are available.

FortiOS 7.4.6 explicitly distinguishes `static-nat`, `load-balance`, and `server-load-balance` VIP types. :chatgpt-content-reference{index="6"}

Count a backend only when the real-server entry contains an address/IP usable as an explicit configured target. Do not invent missing backends.

**What not to change**

- `src/fortigate_extract/model/*.py`, unless a field is genuinely required by FortiGate semantics independently of Excel.
- `src/fortigate_extract/transform/policies.py`: existing 32-character normalization is already appropriate.
- `src/fortigate_extract/transform/vpn.py`: current selector normalization already provides source/destination ranges.
- interface topology relationship logic.

---

## Phase 3: Rebuild the primary migration row mappings

**Objective**

Make the major sheets expose the exact design columns using existing source and derived data.

The interface, service, policy, NAT, VIP, route, and VPN schemas are explicitly defined in the design. :chatgpt-content-reference{index="7"} :chatgpt-content-reference{index="8"}

### Interfaces

**File**

- `src/fortigate_extract/export/excel.py`
  - `_interface_rows()`: line 612
  - `_interface_secondary_rows()`: line 845
  - `_zone_rows()`: line 865
  - `_interface_source_values()`: line 2605
  - `_additional_source_settings()`: line 2688

Replace the current visual tree representation.

Current behavior adds:

```text
◆ agg1
├─ ● port1
└─ ▣ vlan100
```

and even inserts synthetic VPN rows into `Interfaces`.

The new sheet should have one row per real `FGInterface`, with plain `Name`.

Use:

- `Name` → source interface name
- `Alias`
- `Type`
- `Role`
- `IP / Prefix`
- `Secondary IPv4 Addresses`
- `Addressing Mode`
- `Management Access`
- `VLAN ID`
- `Parent Interface`
- `Members`
- `Status`
- `Description`
- `VDOM`

Use only `DerivedViews.topology` for:

- `Aggregate`
- `Physical Interfaces`
- `Topology Path`
- `Topology Issues`

Do not calculate hierarchy in Excel.

Remove visible:

- `Relationship`
- `Topology Kind`
- `DHCP Client`
- `PPPoE Mode`
- `PPPoE Username`
- IPv6 interface block
- `VRF`
- `MTU`
- link speed/duplex/media fields

Preserve omitted explicit settings through `Additional Settings` and source appendices.

Update `_interface_source_values()` so nested interface settings remain namespaced, for example:

```text
ipv6.ip6-address
```

Do not discard namespaced nested settings from `Additional Settings`.

Once the tree rendering is removed, delete `_interface_rank()` and `_topology_symbol()` if they have no remaining callers.

### Interface Secondary IPs

`_interface_secondary_rows():845`

Change to:

```text
Interface
ID
IP / Prefix
Management Access
HA Priority
Analysis Status
Review Reasons
Additional Settings
```

Use existing `FGInterfaceSecondaryIP.ha_priority`; no model change is needed.

### Zones / addresses / groups

Update:

- `_zone_rows():865`
- `_address_rows():884`
- `_wildcard_fqdn_rows():912`
- `_address_group_rows():928`

Main changes:

- remove source-only presentation columns such as `Zone Type`, `Source Path`, `Source Section`;
- rename `Configured Intrazone` → `Intrazone`;
- ensure `VDOM` is present where specified;
- remove `Address Group Tags` builder from workbook dispatch.

### Services

**Functions**

- `_service_rows()`: line 983
- `_service_group_rows()`: line 1017

Services must become:

```text
Name
Source Service
Protocol
Destination Port
Source Port
Protocol Number
ICMP Type
ICMP Code
Generated
Description
VDOM
Analysis Status
Review Reasons
```

Remove:

- `Category`
- `Configured Protocol`
- `Effective Protocol`
- combined `Protocol / Destination Port`
- `Source Protocol Number`
- `Source Port Constraint`

Do not recompute normalization here.

Service Groups:

```text
Name
Members
Generated
Description
VDOM
Analysis Status
Review Reasons
```

Use `NormalizedServiceGroup.generated`.

### Policies

**Function**

- `_policy_rows()`: line 1039

Replace current:

```text
Name
Normalized Name
```

with:

```text
Policy Name
Source Name
```

Rules:

- `Policy Name = normalized_name`
- if not truncated, `Source Name = blank`
- if truncated, `Source Name = original name`

The policy normalization transform already owns this behavior.

Remove visible IPv6-specific, internet-service, old NAT and duplicated source-profile columns.

Add:

```text
Status
SNAT Type
SNAT Address
IP Pool Name
DNS Filter
VDOM
```

Build a lookup of existing `context.derived.nat` results keyed by `(vdom, policy_id)` and only present those already-derived values.

`NAT Enabled` must continue to reflect explicit policy source state.

### NAT Rules

**Function**

- `_nat_rows()`: line 1211

Reduce to the design:

```text
Rule #
Policy Name
Source Interface
Destination Interface
Source Addresses
Destination Addresses
Services
NAT Enabled
SNAT Type
SNAT Address
IP Pool Name
Egress Interfaces
VDOM
Analysis Status
Review Reasons
```

Remove:

- generic `Type`
- `Enabled`
- pool implementation detail columns
- source UUID/ID columns
- `Derived Issues`
- `Extraction Status`
- `Manual Review`

Convert transform identifiers for presentation only:

```text
ip_pool            → IP Pool
interface_address  → Interface Address
```

### Virtual IPs

**Functions**

- `_vip_rows()`: line 1130
- `_vip_real_server_rows()`: line 1164
- `_vip_group_rows()`: line 1196

Add:

```text
Real Servers
Real Server Count
```

`Real Servers` must include all configured backend targets, not a single flattened target.

Remove:

```text
Mapped Address
Source UUID
```

from the visible workbook.

Let validation supply review state for incomplete load-balancing backends.

### Routes

**Function**

- `_route_rows()`: line 1337

Remove visible `VRF`.

Keep the explicit VRF setting in `Additional Settings` and Source Inventory.

### VPN Tunnels

**Function**

- `_vpn_phase1_rows()`: line 1367

Rename/restructure to:

```text
Local Interface
Attached Physical Interfaces
Aggregate
Topology Path
Certificate
Description
```

Remove duplicate concepts:

```text
Interface
Attached Interface
Resolved Physical Interfaces
Certificates
Comments
```

Topology stays entirely sourced from `DerivedViews.topology`.

### VPN Phase 2

**Function**

- `_vpn_phase2_rows()`: line 1458

Expose:

```text
Source Range
Destination Range
Protocol
Source Port
Destination Port
Auto Negotiate
```

Use `DerivedViews.vpn` for the two ranges.

Do not expose source subnet/range components separately.

`protocol`, `src-port`, and `dst-port` are already preserved by the evaluator/`raw_extra`; do **not** add model fields merely to satisfy Excel. Add source-header aliases or a presentation lookup for those preserved fields.

---

## Phase 4: Align all remaining sheets and source appendices

**Objective**

Bring the rest of the workbook to exact schema parity and make provenance preservation reliable.

The remaining target sheets and their fields are defined from VIP Real Servers through Extraction Coverage. :chatgpt-content-reference{index="9"}

**Files / functions**

In `src/fortigate_extract/export/excel.py`:

- DHCP: `1528–1615`
- SD-WAN: `1616–1714`
- SSL VPN: `1715–1826`
- users: `1827–1922`
- administrators: `1923–1993`
- IPS/security: `1994–2100`
- external resources: `2101`
- source appendices: `2117–2300`
- `_model_rows()`: line 2440
- `_add_analysis_status()`: line 2510
- `_overlay_raw()`: line 2531

**Required changes**

- Remove `DHCP Exclude Ranges` from dispatch and workbook.
- Add `Analysis Status` / `Review Reasons` consistently to manual child-row builders that currently never call `_add_analysis_status()`.
- Rename:
  - SD-WAN `Resolved Physical Interfaces` → `Physical Interfaces`
  - user `Auth Timeout` → `Authentication Timeout`
- Remove SSL VPN portal host-check columns.
- Remove IPv6 source-address columns from SSL VPN Authentication Rules.
- Remove SMS-specific local-user columns from the primary sheet.
- Remove IPv6 trusted hosts from Administrators.
- Add missing `Application List` and `DNS Filter` to Security Profiles using fields already present in `FGProfileGroup`.
- Keep `File Filter`.

### Additional Settings preservation

Update `_model_rows()` and manual builders so `Additional Settings` does not mean only `raw_extra`.

It should contain:

```text
sanitized raw_extra
+
explicit typed source fields intentionally omitted from visible columns
```

Only include fields listed in the object's `explicit_fields`.

This is important for values such as:

- route `vrf`;
- omitted IPv6 fields;
- omitted local-user SMS settings;
- omitted administrator settings;
- other useful typed source values removed for workbook readability.

Do not include model defaults that were never explicit.

### Review Required

Update `_review_rows():594` to the exact schema:

```text
Severity
Category
Object
VDOM
Field
Issue / Review Reason
Source Sheet
```

Remove:

```text
Status
Source Row
```

Remove the separate `Warnings` sheet entirely.

### Unresolved References

`_unresolved_reference_rows():2202`

Use the precomputed relationship result from Phase 2.

Exact columns:

```text
Source VDOM
Source Type
Source Object
Field
Reference
Expected Type
Reason
```

Remove `Result`.

### Unsupported

`_unsupported_rows():2239`

Use:

```text
Section
Object Count
Status
Reason
Raw Capture Location
```

Remove:

```text
Item
Manual Review
Raw Capture
```

One architectural caveat exists in the design: the removed-sheet section says removed explicit configuration should remain available through `Unsupported`, while the later `Unsupported` definition says it represents source sections with no dedicated typed support.

Follow the project's provenance rule: **do not mark a typed section as `SOURCE_ONLY`.**

Therefore:

- genuinely untyped sections → `Unsupported`;
- typed but intentionally omitted primary sheets → Source Inventory + FortiGate Source Configuration + relevant object `Additional Settings`.

Do not misclassify typed source merely because its dedicated Excel sheet was removed.

### Source Inventory

`_source_inventory_rows():2260`

Exact columns:

```text
Domain
Scope Type
Scope Name
Source Path
Object Name
Setting
Value
Extraction Status
```

Remove `Manual Review`.

Keep only:

```text
TYPED
SOURCE_ONLY
```

for this provenance field.

### FortiGate Source Configuration

`_source_configuration_rows():2117`

Change to:

```text
Category
Source Path
Object
Parent / Subsection
Operation
Setting
Value
```

Remove:

```text
Source ID
Analysis Status
Manual Review
```

All values must continue through the existing secret sanitizer.

### Extraction Coverage

`_coverage_rows():2301`

The current fields already closely match the target.

Do not invent:

```text
Normalized Objects
Unresolved Dependencies
```

unless an upstream calculation actually exists.

---

## Phase 5: Rebuild Summary and workbook presentation

**Objective**

Match the new visual contract and make the first sheet useful for migration review.

### Summary

**File**

- `src/fortigate_extract/export/excel.py`
  - `_build_summary()`: line 340
  - `_inventory_counts()`: line 558
  - `_vdoms()`: line 578

Target metadata, counts, and indicators are explicitly listed in the design. :chatgpt-content-reference{index="10"}

Add metadata:

```text
Source File
Hostname
FortiOS Version
VDOMs
Generated UTC
Validation Errors
Validation Warnings
```

`Hostname` can be read from explicit `system global` source data without adding it to `FGConfig`.

Current `ExtractionResult` does not expose FortiOS version metadata. Do **not** add a source-model field or guess from defaults for this Excel task. Only populate the row if existing explicit extraction evidence becomes available; otherwise leave it blank.

Do not output `"Not provided"` for missing explicit configuration.

Inventory counts must include all design items, notably:

```text
Service Groups
NAT Rules
DHCP Servers
SD-WAN Members
SSL VPN Portals
Administrators
IPS Sensors
External Resources
Review Required
Unsupported Source Sections
```

Add migration indicators using only existing explicit/derived/validation evidence:

```text
IPv6 Explicit Configuration Present
Dynamic WAN Addressing Present
SD-WAN Present
Interface-NAT Ambiguities
Broken References
Policy Names Truncated
Policy Name Collisions
Topology Issues
```

These are analysis/derived indicators, not FortiOS defaults.

### Status simplification

**Function**

- `_add_analysis_status()`: line 2510

Stop injecting generic:

```text
Extraction Status = PARTIAL
Manual Review = Yes/No
Audit Note
```

into normal report rows.

Normal report analysis uses only:

```text
EXTRACTED
REVIEW_REQUIRED
SOURCE_ONLY
```

The distinction between this analysis status and Source Inventory's `TYPED/SOURCE_ONLY` provenance must remain clear. :chatgpt-content-reference{index="11"}

### Missing/default behavior

Audit every row builder for synthesized defaults.

Blank must continue to mean:

```text
not explicitly configured
```

No automatic:

```text
No
Disabled
0
default
any
```

unless the source explicitly provided it or a real current transform calculates it. :chatgpt-content-reference{index="12"}

### Styling

**File locations**

- style constants: `excel.py:20–38`
- `_write_table_sheet()`: line 407
- `_apply_review_colors()`: line 498
- `_apply_widths()`: line 512
- `_freeze_pane()`: line 532

Change palette to:

```text
Title       #17324D
Header      #0F766E
Alternate   #F8FAFC
Derived     #D7F0EC
Review      #FEF3C7
Error       #FEE2E2
Muted       #667085
```

Use precedence:

```text
error/review
> derived field
> alternate row
> normal row
```

Apply light teal to genuine derived data columns using schema metadata rather than a special `Interfaces` hard-coded header set.

Default-hide technical columns:

```text
Source Explicit Fields
Additional Settings
```

where present.

Keep:

- row 1 title;
- row 2 note/backlink;
- row 3 headers;
- row 4+ data;
- filters;
- wrapped cells;
- frozen headers;
- Summary backlink.

The design explicitly separates source/derived/analysis data and prohibits Excel from resolving topology, normalizing VPN selectors, selecting NAT addresses, splitting services, or truncating policy names itself. :chatgpt-content-reference{index="13"}

---

## Phase 6: Replace the Excel regression tests with the new contract

**Files**

- `tests/test_excel_report.py`
  - fixture: lines 16–50
  - workbook contract/topology: line 82
  - secret test: line 194
  - legacy column test: line 220
  - target-vendor test: line 314
- `tests/test_web_ui.py`
  - Excel endpoint regression: around lines 117–140

**Required test changes**

Expand `_SAMPLE_CONFIG` or create focused fixtures for:

- hostname;
- secondary IP + HA priority;
- VLAN → aggregate → physical topology;
- explicit IPv6 source evidence;
- DHCP/PPPoE interface;
- multi-port service normalization;
- generated service group;
- long policy name;
- policy-name collision;
- IP-pool NAT;
- deterministic interface-address NAT;
- ambiguous interface NAT;
- load-balancing VIP;
- VPN Phase 2 subnet/range normalization;
- unknown/source-only section;
- secrets.

Assert:

- exact workbook sheet order;
- every removed sheet is absent;
- exact header order for every retained sheet;
- plain interface names;
- topology data comes from dedicated columns;
- generated services/groups are marked correctly;
- policy `Source Name` is blank unless truncation happened;
- ambiguous NAT has blank `SNAT Address`;
- removed typed settings survive in `Additional Settings` or appendices;
- no missing source field is converted into a default;
- `Review Required` contains VDOM and Field;
- technical columns are hidden where intended;
- palette/freeze/filter/backlink behavior;
- actual secrets never occur anywhere in the workbook.

Keep the current web endpoint regression because `/api/extract/excel` still needs to produce a valid `.xlsx`. No web API contract change should be necessary.

Run at minimum:

```text
python -m unittest tests.test_excel_report tests.test_web_ui
python -m unittest discover -s tests
```

Do not claim passing validation until these commands are actually run.

### Scope boundary

This change should **not** implement the proposed shared `ReportSection` frontend/Excel layer yet. `Excel Design.md` describes that as a later recommendation; this task should first make the existing exporter conform to the finalized schema. :chatgpt-content-reference{index="14"}

The dependency order should therefore be:

```text
schema contract
→ missing transform/relationship/validation outputs
→ Excel row mappings
→ source-preservation appendices
→ summary + styling
→ regression tests
```

That keeps the change aligned with the current pipeline rather than moving semantics back into Excel.