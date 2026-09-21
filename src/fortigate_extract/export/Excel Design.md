Below is the finalized design contract I would use for the exporter and frontend reporting layer.

# FortiGate Excel Schema and Derived Rules

## 1. Purpose

The workbook is a **FortiGate configuration inventory and migration-oriented report**.

The workbook must answer four questions quickly:

1. What is explicitly configured?
2. What does each object reference?
3. What is its logical/physical relationship?
4. What requires review before a future migration?

The workbook is **not**:

- a vendor-neutral IR;
- a target-vendor model;
- a FortiOS default calculator;
- a semantic repair layer;
- a replacement for `FGConfig`;
- a place to silently infer missing configuration.

The data flow remains:

```text
FortiGate CLI
→ Tokenizer
→ Parser
→ Command Evaluator
→ FGConfig
→ Relationships / Transforms
→ DerivedViews
→ Validation
→ Report Presentation
    ├── Excel
    └── Frontend
```

---

# 2. Data provenance rules

Every displayed value belongs to one of these classes:

| Class | Meaning |
|---|---|
| Source | Explicitly configured FortiGate source value |
| Derived | Calculated by an existing transform or relationship model |
| Analysis | Validation/review result |
| Source-only | Explicit CLI preserved without a dedicated typed model |
| Unknown | Cannot be determined safely |
| Effective | Only allowed when a current transform explicitly calculates it |

Missing source fields mean:

```text
not explicitly configured
```

They must remain blank.

Do not convert missing values into assumed FortiOS defaults.

---

# 3. Workbook visual design

Reuse the old workbook visual style.

## Sheet layout

```text
Row 1   Sheet title
Row 2   Note / navigation
Row 3   Column headers
Row 4+  Data
```

## Styling

```text
Title fill       dark navy
Column headers   teal
Normal rows      white
Alternate rows   very light grey
Derived fields   light teal
Review required  light yellow
Errors           light red
```

Recommended palette:

```text
Title       #17324D
Header      #0F766E
Alternate   #F8FAFC
Derived     #D7F0EC
Review      #FEF3C7
Error       #FEE2E2
Muted       #667085
```

All sheets should have:

- filters;
- frozen header row;
- wrapped cells;
- sensible widths;
- Summary backlink;
- no excessive decorative formatting.

Technical provenance columns such as:

```text
Source Explicit Fields
Additional Settings
```

should be placed at the far right and may be hidden by default.

---

# 4. Final workbook order

```text
Summary
Review Required

System Settings
DNS Settings
NTP Settings

Interfaces
Interface Secondary IPs
Zones

Addresses
Wildcard FQDN
Address Groups

Services
Service Groups

Policies

NAT Rules
IP Pools
Virtual IPs
VIP Real Servers
VIP Groups

Routes

VPN Tunnels
VPN Phase 2

DHCP Servers
DHCP IP Ranges
DHCP Reservations

SD-WAN
SD-WAN Zones
SD-WAN Members
SD-WAN Health Checks
SD-WAN Rules

SSL VPN Settings
SSL VPN Portals
SSL VPN Authentication Rules

Local Users
User Groups
User Group Matches
User Group Guests

Administrators
Admin Profiles
Admin Profile Permissions

IPS Sensors
IPS Sensor Entries
IPS Exempt IPs
Security Profiles

External Resources

Unresolved References
Unsupported
Source Inventory
FortiGate Source Configuration
Extraction Coverage
```

---

# 5. Sheets intentionally removed

Do not create dedicated workbook sheets for:

```text
Service Categories

Schedules
Schedule Groups

Traffic Shapers
Session Helpers

Routing Protocol Settings
BGP
OSPF
RIP
ISIS

SSL VPN Host Checks
SSL VPN Host Check Items

Authentication Settings
Authentication Schemes
Authentication Sequences

User Quarantine

ZTNA

Certificates

Proxy
Web Proxy

SSH Keys

Internet Service Definitions
Internet Service Additions
Internet Service Appends
Internet Service Extensions

Source Security Profile Settings

DoS Policies
DoS Anomalies
Firewall Sniffer
IPv6 EH Filter

LDAP Server Definitions
RADIUS Server Definitions
RADIUS Accounting Servers
TACACS+ Server Definitions
SAML Server Definitions
FSSO Server Definitions
FSSO AD Groups
FSSO Polling

unsupported SSL VPN landing/bookmark child sections
```

If any of these appear explicitly in the FortiGate source, retain them through:

```text
Source Inventory
FortiGate Source Configuration
Unsupported
```

They are not discarded.

---

# 6. Summary

## Metadata

```text
Source File
Hostname
FortiOS Version            when explicitly available
VDOMs
Generated UTC
Validation Errors
Validation Warnings
```

## Inventory counts

```text
Interfaces
Zones
Addresses
Address Groups
Services
Service Groups
Policies
NAT Rules
IP Pools
Virtual IPs
Routes
VPN Tunnels
VPN Phase 2
DHCP Servers
SD-WAN Members
SSL VPN Portals
Local Users
Administrators
IPS Sensors
External Resources
Review Required
Unsupported Source Sections
```

## Migration indicators

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

These are derived/analysis indicators and must be clearly identified as such.

---

# 7. System Settings

This is a **direct explicit-source presentation**, not a typed `FGConfig` model.

Columns:

```text
Setting
Value
Source Path
Analysis Status
Review Reasons
```

Source paths:

```text
system global
system settings
```

Do not recreate old fields such as:

```text
Management IPv4 Address
Management Default Gateway
System Permitted IPs
Management Address Type
```

Interface management addressing belongs to Interfaces.

---

# 8. DNS Settings

Direct explicit-source view:

```text
Setting
Value
Source Path
Analysis Status
Review Reasons
```

Source:

```text
system dns
```

---

# 9. NTP Settings

Direct explicit-source view:

```text
Object
Setting
Value
Source Path
Analysis Status
Review Reasons
```

Sources:

```text
system ntp
system ntp ntpserver
```

---

# 10. Interfaces

This is a primary migration sheet.

## Visible columns

```text
Name
Alias
Type
Role
IP / Prefix
Secondary IPv4 Addresses
Addressing Mode
Management Access
VLAN ID
Parent Interface
Aggregate
Physical Interfaces
Topology Path
Zone
Members
Status
Description
VDOM
Topology Issues
Analysis Status
Review Reasons
```

## Technical columns

```text
Source Explicit Fields
Additional Settings
```

## Derived fields

```text
Aggregate
Physical Interfaces
Topology Path
Topology Issues
```

must come only from the interface topology relationship model.

Example:

```text
Name: vlan100
Parent Interface: agg1
Aggregate: agg1
Physical Interfaces: port1, port2
Topology Path: vlan100 → agg1
```

A tunnel or VLAN attached through an aggregate must resolve all the way to its physical members.

---

# 11. Interface Secondary IPs

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

---

# 12. Zones

```text
Name
Members
Intrazone
Description
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 13. Addresses

```text
Name
Type
Value
Address Family
Associated Interface
Allow Routing
Tags
Description
VDOM
Analysis Status
Review Reasons
Additional Settings
```

`Value` can represent:

```text
subnet
start-end
FQDN
wildcard
wildcard FQDN
```

depending on the explicit source object.

---

# 14. Wildcard FQDN

```text
Name
Wildcard FQDN
Description
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 15. Address Groups

```text
Name
Address Family
Group Type
Members
Exclusion Enabled
Exclude Members
Allow Routing
Tags
Description
VDOM
Analysis Status
Review Reasons
Additional Settings
```

A separate Address Group Tags sheet is unnecessary.

---

# 16. Services

Service Categories are removed.

Each normalized protocol/port combination becomes one migration service row.

## Columns

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

Do not combine:

```text
tcp/8080
```

into one field.

Use:

```text
Protocol          tcp
Destination Port  8080
```

---

# 17. Service normalization rule

Given:

```text
edit "DNS-Service"
    set tcp-portrange 53
    set udp-portrange 53 5353
next
```

derive:

```text
DNS-Service-1   tcp   53
DNS-Service-2   udp   53
DNS-Service-3   udp   5353
```

Then generate:

```text
Service Group: DNS-Service
Members:
  DNS-Service-1
  DNS-Service-2
  DNS-Service-3
```

Rules:

1. One normalized result:
   - retain original source service name;
   - do not generate a group.

2. More than one normalized result:
   - create numbered child services;
   - original source name becomes a generated service group.

3. Preserve:

```text
Source Service
Generated = Yes/No
```

for traceability.

4. Generated-name collisions must be handled deterministically.

---

# 18. Service Groups

```text
Name
Members
Generated
Description
VDOM
Analysis Status
Review Reasons
```

Both source FortiGate groups and generated groups appear here.

---

# 19. Policies

## Columns

```text
Rule #
Policy Name
Source Name
Source Interface
Source Addresses
Source Address Negate
Destination Interface
Destination Addresses
Destination Address Negate
Services
Service Negate
Action
Schedule
Status

NAT Enabled
SNAT Type
SNAT Address
IP Pool Name

VPN Tunnel

User Groups
Users

UTM Status
Security Profile Group
Antivirus
IPS Sensor
Web Filter
Application List
DNS Filter
SSL/SSH Profile

Log Setting
Comments
VDOM

Analysis Status
Review Reasons

Source Explicit Fields
Additional Settings
```

`Schedule` remains on the policy even though dedicated schedule sheets are removed.

---

# 20. Policy name rule

Migration policy names are limited to:

```text
32 characters
```

If source length is <= 32:

```text
Policy Name = source name
Source Name = blank
```

If source length is > 32:

```text
first 30 characters + "-L"
```

Example:

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789
↓
ABCDEFGHIJKLMNOPQRSTUVWXYZ1234-L
```

The final result must be 32 characters.

When truncation occurs:

```text
Source Name = original FortiGate policy name
Policy Name = migration-safe name
```

If two policies normalize to the same name:

```text
Analysis Status = REVIEW_REQUIRED
Review Reasons = Policy-name normalization collision
```

Do not silently invent another migration name.

---

# 21. NAT Rules

Derived from policies with source NAT enabled.

## Columns

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

## Rule A — IP pool NAT

When:

```text
ippool enabled
or
poolname explicitly configured
```

derive:

```text
SNAT Type = IP Pool
IP Pool Name = configured pool name(s)
SNAT Address = IP pool start/end address
```

Example:

```text
203.0.113.10
```

or:

```text
203.0.113.10-203.0.113.20
```

---

# 22. NAT Rule B — interface-address NAT

When NAT is enabled but no IP pool is used:

```text
resolve outgoing interface
→ obtain deterministic configured static IPv4
```

Then:

```text
SNAT Type = Interface Address
SNAT Address = interface IPv4 address
```

Do not derive an address when the interface uses:

```text
DHCP
PPPoE
```

or when multiple runtime egress paths make the result ambiguous.

Instead:

```text
SNAT Address = blank
Analysis Status = REVIEW_REQUIRED
```

with a reason.

---

# 23. IP Pools

```text
Name
Type
Start IP
End IP
Source Start IP
Source End IP
Start Port
End Port
Associated Interface
ARP Reply
ARP Interface
Permit Any Host
Excluded IPs
NAT64
Add NAT64 Route
Description
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 24. Virtual IPs

## Columns

```text
Name
Type
Status

External IP
External Address Objects
External Interface

Mapped IPs
Real Servers
Real Server Count

Port Forward
Protocol
External Port
Mapped Port

ARP Reply
NAT Source VIP

Services

Load Balance Method
Server Type
Monitors

Description
VDOM
Analysis Status
Review Reasons
Additional Settings
```

For load-balancing VIPs, never flatten the target to a single address.

Display every configured:

```text
mappedip
realserver
```

target.

If the source explicitly represents a load-balancing VIP but fewer than two usable backends are available:

```text
Analysis Status = REVIEW_REQUIRED
```

Do not derive interface attachment from external IP.

---

# 25. VIP Real Servers

```text
VIP Name
Server ID
IP
Address
Port
Status
Weight
Monitors
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 26. VIP Groups

```text
Name
Interface
Members
Comments
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 27. Routes

## Columns

```text
Route ID
Destination
Destination Address Object
Interface
Gateway
Distance
Priority
Status
SD-WAN Zone
Preferred Source
Source Prefix
Dynamic Gateway
Blackhole
Description
Address Family
VDOM
Analysis Status
Review Reasons
Additional Settings
```

Remove from the visible report:

```text
VRF
Device
Next Hop
Administrative Distance
Destination Prefix (Normalized)
Source Route ID
```

Explicit VRF source data remains preserved in source inventory / Additional Settings.

---

# 28. VPN Tunnels — IPsec Phase 1

```text
Name
Type
Local Interface
Attached Physical Interfaces
Aggregate
Topology Path

Remote Gateway IPv4
Remote Gateway DDNS

IKE Version
Authentication Method
Proposal
DH Groups
Key Lifetime
NAT Traversal
DPD

Local Gateway
Local ID
Peer ID
Certificate

Description
VDOM
Topology Issues
Analysis Status
Review Reasons
Additional Settings
```

Do not expose dedicated:

```text
Remote Gateway IPv6
Local Gateway IPv6
```

columns in the primary workbook.

Topology comes from `DerivedViews.topology`.

---

# 29. VPN Phase 2

## Columns

```text
Name
Phase 1
Proposal
PFS
DH Groups
Key Lifetime Seconds
Key Lifetime KB

Source Range
Destination Range

Protocol
Source Port
Destination Port
Auto Negotiate

Comments
VDOM
Analysis Status
Review Reasons
Additional Settings
```

Do not expose:

```text
Source Subnet
Destination Subnet
Source Range Start
Source Range End
Destination Range Start
Destination Range End
```

as separate visible columns.

Use the existing VPN transform to produce:

```text
start-end
```

Example:

```text
192.168.1.0-192.168.1.255
```

The transform may derive the range from:

```text
explicit start/end
subnet
resolvable address object
```

If it cannot be safely resolved:

```text
blank + REVIEW_REQUIRED
```

Do not invent a default selector.

---

# 30. DHCP Servers

```text
Server ID
Interface
Status
Server Type
IP Mode
Default Gateway
Netmask
Lease Time
DNS Service
DNS Server 1
DNS Server 2
DNS Server 3
DNS Server 4
Timezone Option
Timezone
Relay Agent
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 31. DHCP IP Ranges

```text
Server ID
Interface
Range ID
Start IP
End IP
Lease Time
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 32. DHCP Reservations

```text
Server ID
Interface
Reservation ID
IP Address
MAC Address
Description
Action
Type
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 33. SD-WAN

```text
Status
Load Balance Mode
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 34. SD-WAN Zones

```text
Zone Name
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 35. SD-WAN Members

```text
ID
Interface
Zone
Gateway
Source
Cost
Weight
Priority
Status

Aggregate
Physical Interfaces

VDOM
Analysis Status
Review Reasons
Additional Settings
```

Physical Interfaces comes from interface topology.

---

# 36. SD-WAN Health Checks

```text
Name
Server
Members
Protocol
Interval
Fail Time
Recovery Time
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 37. SD-WAN Rules

```text
ID
Name
Status
Mode
Source
Destination
Priority Members
Health Checks
Priority Zones
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 38. SSL VPN Settings

Keep only currently useful typed information:

```text
Status
Minimum Protocol
Maximum Protocol
Authentication Timeout
Idle Timeout
Port

DNS Server 1
DNS Server 2
Server Certificate

Source Interfaces
Source Addresses

Tunnel IP Pools
Default Portal

VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 39. SSL VPN Portals

```text
Name
Tunnel Mode
IPv6 Tunnel Mode
IP Pools
IPv6 Pools
Split Tunneling
Split Tunneling Routing Addresses
Limit User Logins
FortiClient Download
VDOM
Analysis Status
Review Reasons
Additional Settings
```

Host-check columns are omitted from the main report.

Their source configuration remains preserved.

---

# 40. SSL VPN Authentication Rules

```text
ID
Auth
Cipher
Client Certificate
Realm
Source Interfaces
Source Addresses
Source Address Negate
Users
User Peer
Groups
Portal
Analysis Status
Review Reasons
Additional Settings
```

---

# 41. Local Users

```text
Name
ID
Status
Type

Password Configured
Password Time

Two Factor
Two Factor Authentication
Two Factor Notification
FortiToken

Email

LDAP Server
RADIUS Server
TACACS+ Server

Authentication Timeout
Password Policy
Workstation
Username Sensitivity

PPK Identity
PPK Secret Configured

VDOM
Analysis Status
Review Reasons
Additional Settings
```

Never export actual:

```text
password
PPK secret
token secret
```

values.

---

# 42. User Groups

```text
Name
ID
Group Type
Members
Match Count
Authentication Timeout
Auth Concurrent Override
Auth Concurrent Value
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 43. User Group Matches

```text
User Group
Match ID
Server Name
Group Name
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 44. User Group Guests

```text
User Group
Guest ID
Name
User ID
Email
Mobile Phone
Expiration
Sponsor
Comment
Password Configured
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 45. Administrators

```text
Name
Access Profile
VDOMs

IPv4 Trusted Hosts

Two Factor
Two Factor Authentication
Two Factor Notification

Remote Auth
Remote Group

Credential Configured
FortiToken

Guest User Groups
Schedule

Peer Auth
Peer Group

SSH Certificate

Analysis Status
Review Reasons
Additional Settings
```

Actual passwords, private keys and SSH key contents must never appear.

---

# 46. Admin Profiles

```text
Name
Analysis Status
Review Reasons
Additional Settings
```

---

# 47. Admin Profile Permissions

```text
Profile
Permission Group
Setting
Value
Analysis Status
Review Reasons
Additional Settings
```

---

# 48. IPS Sensors

```text
Name
Description
Block Malicious URL
Scan Botnet Connections
Extended Log
Replacement Message Group
Entry Count
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 49. IPS Sensor Entries

Use one column per concept.

```text
Sensor
Entry ID
Signature IDs
CVEs
Applications
OS
Protocols
Severities
Location

Default Action
Default Status
Action
Status

Log
Log Packet
Log Attack Context

Rate Count
Rate Duration
Rate Mode
Rate Track

Quarantine
Quarantine Expiry
Quarantine Log

Vulnerability Types

VDOM
Analysis Status
Review Reasons
Additional Settings
```

No duplicate singular/plural aliases.

---

# 50. IPS Exempt IPs

```text
Sensor
Entry ID
Exempt IP ID
Source IP
Destination IP
VDOM
Analysis Status
Review Reasons
Additional Settings
```

---

# 51. Security Profiles

Use FortiGate fields only.

```text
Name
Antivirus
IPS Sensor
Application List
Web Filter
DNS Filter
File Filter
SSL/SSH Profile
VDOM
Analysis Status
Review Reasons
Additional Settings
```

Do not include:

```text
Anti-Spyware
WildFire
target-vendor profile concepts
```

---

# 52. External Resources

The existing typed model supports the required fields directly.

```text
Name
Resource
Type
Refresh Rate
Comments
VDOM
Analysis Status
Review Reasons
Additional Settings
```

Corresponding FortiGate values:

```text
resource
type
comments
refresh-rate
```

---

# 53. Unresolved References

```text
Source VDOM
Source Type
Source Object
Field
Reference
Expected Type
Reason
```

Only unresolved relationships appear here.

Do not create a duplicate Dependency Registry sheet.

---

# 54. Unsupported

One row per source section without dedicated typed support:

```text
Section
Object Count
Status
Reason
Raw Capture Location
```

Example:

```text
user ldap
3
SOURCE_ONLY
No dedicated typed FortiGate model
Source Inventory
```

---

# 55. Source Inventory

This is the primary source-preservation appendix.

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

Values must be sanitized.

Statuses:

```text
TYPED
SOURCE_ONLY
```

---

# 56. FortiGate Source Configuration

Command-level appendix:

```text
Category
Source Path
Object
Parent / Subsection
Operation
Setting
Value
```

Secrets must be sanitized before reaching Excel.

---

# 57. Extraction Coverage

```text
Source Section
Found
Source Objects
Parsed Objects
Status
Semantic Level
Parser Handler
Line Start
Line End
Semantic Unknowns
Notes
```

Do not include fake fields such as:

```text
Normalized Objects
Unresolved Dependencies
```

unless real current calculations exist.

---

# 58. IPv6 final rule

Do **not** remove IPv6 from extraction, source models, or source inventory.

Remove most IPv6-specific columns from the primary migration workbook.

The main workbook should be IPv4-focused for readability.

Retain IPv6 where it is naturally useful, for example:

```text
Address Family
IPv6 Pools where already part of an SSL VPN portal
IPv6 Tunnel Mode where explicitly configured
```

Do not expose huge blocks such as:

```text
IPv6 Send Advertisement
IPv6 Manage Flag
IPv6 Other Flag
IPv6 Reachable Time
IPv6 Retransmit Time
DHCPv6 Prefix Hint
DHCPv6 Relay fields
...
```

in the main Interfaces sheet.

Instead derive:

```text
IPv6 Explicit Configuration Present = Yes/No
```

for Summary.

If IPv6 exists, preserve the complete explicit configuration in:

```text
Source Inventory
FortiGate Source Configuration
Additional Settings
```

This keeps the workbook readable without destroying migration evidence.

---

# 59. Analysis status

Use only:

```text
EXTRACTED
REVIEW_REQUIRED
SOURCE_ONLY
```

### EXTRACTED

Structured output exists and no relevant issue was found.

### REVIEW_REQUIRED

Examples:

```text
broken reference
ambiguous interface NAT
dynamic NAT interface
topology cycle
missing aggregate member
VPN selector cannot be normalized
policy-name collision
load-balancing VIP with suspicious/incomplete backend data
```

### SOURCE_ONLY

Explicit FortiGate source exists but there is no dedicated typed model.

Validation must not mutate the data.

---

# 60. Review Required sheet

Consolidate validation findings into:

```text
Severity
Category
Object
VDOM
Field
Issue / Review Reason
Source Sheet
```

This replaces unnecessary separate warning/report sheets.

---

# 61. Missing/default rules

Blank means:

```text
not explicitly configured
```

Do not output:

```text
Disabled
No
0
default
any
```

merely because FortiOS might behave that way by default.

A `Yes/No` value is allowed only when:

1. the underlying source field was explicitly present; or
2. a documented current transform genuinely calculates that state.

---

# 62. Effective field rule

Only use a column beginning with:

```text
Effective ...
```

when the current transform actually computes it.

Example allowed:

```text
Configured Protocol
Effective Protocol
```

because the service transform genuinely expands/calculates the protocol representation.

Do not create:

```text
Effective UTM Status
Effective Management Address
Effective Gateway
```

without a real transform.

---

# 63. Original / normalized rule

Do not keep generic pairs such as:

```text
Source Address (Original)
Source Address (Normalized)

Action (Original)
Action (Normalized)
```

when the values do not genuinely differ.

Keep both only for real migration transformations.

Examples:

```text
Source Name
Policy Name
```

is valid when the policy name was truncated.

Likewise:

```text
Source Service
Generated Service
```

is valid because service expansion actually changes representation.

---

# 64. Secret handling

Never export:

```text
password
passwd
PSK
private key
API key
token
authentication secret
PPK secret
```

Safe metadata includes:

```text
Password Configured = Yes
Credential Configured = Yes
PPK Secret Configured = Yes
```

Raw appendix views must pass through the same secret sanitization rules.

---

# 65. Presentation versus semantics

Excel may:

```text
rename headers
order columns
format values
join list values for display
apply colors
hide technical columns
show derived fields already calculated upstream
```

Excel must not:

```text
resolve references
calculate topology
split services
normalize VPN selectors
choose NAT addresses
truncate policy names
apply FortiOS defaults
repair source data
```

Those belong in Relationships / Transforms / Validation.

---

# 66. Shared frontend/reporting recommendation

The eventual frontend and Excel should consume the same transient report view:

```text
FGConfig
+ DerivedViews
+ Validation
        ↓
ReportSection / presentation rows
       ↙                    ↘
Frontend JSON              Excel
```

This presentation layer is not another IR.

It should contain only:

```text
section metadata
columns
already-calculated source/derived values
analysis state
```

No semantic configuration should be stored there.

---

# 67. Final design principle

The primary workbook should be:

```text
compact
migration-oriented
traceable
source-faithful
relationship-aware
easy to scan
```

The main report should contain only useful migration information.

Everything else remains safely available through:

```text
Additional Settings
Source Inventory
FortiGate Source Configuration
Unsupported
```

This preserves source fidelity without allowing raw FortiGate complexity to overwhelm the primary workbook.

This is the schema I would treat as the baseline before implementing the new shared reporting layer and simplifying `excel.py`.