from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
from enum import Enum
from io import BytesIO
from pathlib import Path
from typing import Any, BinaryIO, Iterable, Mapping, Sequence

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

from ..config import ExtractionConfig
from ..derived import DerivedViews, build_derived_views
from ..extraction.result import ExtractionResult
from ..extraction.source_inventory import SourceObjectRecord
from ..relationships.references import collect_broken_references
from ..security.extraction import sanitize_source_attributes
from ..section_registry import registered_sections
from ..validation.models import ValidationIssue, ValidationResult
from .excel_schema import SHEET_HEADERS, SHEET_ORDER


_TITLE_FILL = PatternFill("solid", fgColor="173F3A")
_HEADER_FILL = PatternFill("solid", fgColor="1F5B52")
_TOPOLOGY_FILL = PatternFill("solid", fgColor="E8F3F0")
_REVIEW_FILL = PatternFill("solid", fgColor="FFF2CC")
_ERROR_FILL = PatternFill("solid", fgColor="FCE8E6")
_WARNING_FILL = PatternFill("solid", fgColor="FFF4E5")
_ALT_FILL = PatternFill("solid", fgColor="F7F9F8")
_WHITE_FONT = Font(color="FFFFFF", bold=True)
_TITLE_FONT = Font(color="FFFFFF", bold=True, size=14)
_HEADER_FONT = Font(color="FFFFFF", bold=True, size=10)
_MUTED_FONT = Font(color="66706D", italic=True, size=9)
_LINK_FONT = Font(color="0563C1", underline="single")
_THIN = Side(style="thin", color="D9E2DF")
_BORDER = Border(bottom=_THIN)

_OLD_CROSS_VENDOR_SHEETS = frozenset(
    {
        "Extraction Evidence",
        "Firewall Filters",
        "Checkpoint Access Rules",
        "Cisco ACP",
        "Default Security Rules",
        "PBF Rules",
        "NGFW Pre-Match Policies",
        "NGFW Security Policies",
        "Cisco PBR",
        "PAN SD-WAN Interface Profiles",
        "PAN SD-WAN Link Settings",
        "PAN SD-WAN Path Quality",
        "PAN SD-WAN Traffic Distribution",
        "PAN SD-WAN Rules",
    }
)

_EXTRA_SHEETS: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "Wildcard FQDN",
        (
            "Name",
            "Wildcard FQDN",
            "Description",
            "Source VDOM",
            "Extraction Status",
            "Manual Review",
            "Review Reasons",
            "Source Explicit Fields",
            "Additional Settings",
        ),
    ),
    (
        "DHCP Exclude Ranges",
        (
            "Server ID",
            "Interface",
            "Range ID",
            "Start IP",
            "End IP",
            "Lease Time",
            "VDOM",
            "Extraction Status",
            "Manual Review",
            "Review Reasons",
            "Source Explicit Fields",
            "Additional Settings",
        ),
    ),
    (
        "External Resources",
        (
            "Name",
            "Resource",
            "Type",
            "Refresh Rate",
            "Comments",
            "VDOM",
            "Extraction Status",
            "Manual Review",
            "Review Reasons",
            "Source Explicit Fields",
            "Additional Settings",
        ),
    ),
)

_EXTRA_COLUMNS: dict[str, tuple[str, ...]] = {
    "Interfaces": (
        "Relationship",
        "Topology Kind",
        "Aggregate",
        "Physical Interfaces",
        "Topology Issues",
        "Source Explicit Fields",
    ),
    "VPN Tunnels": (
        "Attached Interface",
        "Aggregate",
        "Resolved Physical Interfaces",
        "Topology Path",
        "Topology Issues",
        "Source Explicit Fields",
    ),
    "VPN Phase 2": (
        "Source Range",
        "Destination Range",
        "Source Explicit Fields",
    ),
    "SD-WAN Members": (
        "Resolved Physical Interfaces",
        "Aggregate",
        "Source Explicit Fields",
    ),
}

_SOURCE_PATHS_BY_SHEET: dict[str, tuple[str, ...]] = {
    "System Settings": ("system global", "system settings"),
    "DNS Settings": ("system dns",),
    "NTP Settings": ("system ntp", "system ntp ntpserver"),
    "Schedules": ("firewall schedule onetime", "firewall schedule recurring"),
    "Schedule Groups": ("firewall schedule group",),
    "Local-In Policies": ("firewall local-in-policy", "firewall local-in-policy6"),
    "Multicast Policies": ("firewall multicast-policy", "firewall multicast-policy6"),
    "Policy Routes": ("router policy", "router policy6"),
    "Session TTL Settings": ("system session-ttl",),
    "Session TTL Overrides": ("system session-ttl port",),
    "Routing Protocol Settings": (
        "router bgp",
        "router ospf",
        "router ospf6",
        "router rip",
        "router ripng",
        "router isis",
    ),
    "SSL VPN Portal Split DNS": ("vpn ssl web portal split-dns",),
    "SSL VPN Portal MAC Rules": ("vpn ssl web portal mac-addr-check-rule",),
    "SSL VPN Portal OS Checks": ("vpn ssl web portal os-check-list",),
    "SSL VPN Bookmark Groups": ("vpn ssl web portal bookmark-group",),
    "SSL VPN Bookmarks": ("vpn ssl web portal bookmark-group bookmarks",),
    "SSL VPN Bookmark Form Data": (
        "vpn ssl web portal bookmark-group bookmarks form-data",
    ),
    "SSL VPN Landing Pages": ("vpn ssl web portal landing-page",),
    "SSL VPN Landing Form Data": ("vpn ssl web portal landing-page form-data",),
    "LDAP Servers": ("user ldap",),
    "RADIUS Servers": ("user radius",),
    "RADIUS Accounting Servers": ("user radius accounting-server",),
    "TACACS+ Servers": ("user tacacs+",),
    "SAML Servers": ("user saml",),
    "FSSO Servers": ("user fsso",),
    "FSSO AD Groups": ("user adgrp",),
    "FSSO Polling": ("user fsso-polling",),
    "FortiTokens": ("user fortitoken",),
    "Authentication Schemes": ("authentication scheme",),
    "Authentication Rules": ("authentication rule",),
    "Authentication Sequences": ("authentication setting",),
    "Identity Server Endpoints": ("user security-exempt-list",),
    "SSL TLS Service Profiles": ("firewall ssl-server",),
    "Internet Service Definitions": ("firewall internet-service-definition",),
    "Internet Service Def Entries": ("firewall internet-service-definition entry",),
    "Internet Service Def Ports": (
        "firewall internet-service-definition entry port-range",
    ),
    "Custom Internet Services": ("firewall internet-service-custom",),
    "Custom IS Entries": ("firewall internet-service-custom entry",),
    "Custom IS Ports": ("firewall internet-service-custom entry port-range",),
    "Custom Internet Service Groups": ("firewall internet-service-custom-group",),
    "Internet Service Groups": ("firewall internet-service-group",),
    "IS Additions": ("firewall internet-service-addition",),
    "IS Addition Entries": ("firewall internet-service-addition entry",),
    "IS Addition Ports": ("firewall internet-service-addition entry port-range",),
    "IS Appends": ("firewall internet-service-append",),
    "IS Extensions": ("firewall internet-service-extension",),
    "IS Extension Disabled": ("firewall internet-service-extension disable-entry",),
    "IS Extension Entries": ("firewall internet-service-extension entry",),
    "IS Extension Ports": (
        "firewall internet-service-extension entry port-range",
        "firewall internet-service-extension disable-entry port-range",
    ),
    "Source Security Profile Setting": (
        "antivirus profile",
        "application list",
        "webfilter profile",
        "dnsfilter profile",
        "emailfilter profile",
        "firewall ssl-ssh-profile",
        "file-filter profile",
    ),
    "DoS Policies": ("firewall DoS-policy", "firewall DoS-policy6"),
    "DoS Anomalies": (
        "firewall DoS-policy anomaly",
        "firewall DoS-policy6 anomaly",
    ),
    "Firewall Sniffer": ("firewall sniffer",),
    "IPv6 EH Filter": ("firewall ipv6-eh-filter",),
}

_HEADER_ALIASES: dict[str, tuple[str, ...]] = {
    "Hostname": ("hostname",),
    "Timezone": ("timezone",),
    "Admin HTTPS Port": ("admin-sport", "admin-port"),
    "Primary DNS": ("primary",),
    "Secondary DNS": ("secondary",),
    "Role": ("role",),
    "Server Address": ("server",),
    "Authentication Type": ("authentication", "auth-type", "authmethod"),
    "Name": ("name",),
    "Description": ("description", "comments", "comment"),
    "Members": ("member", "members"),
    "Source Fabric Object": ("fabric-object",),
    "Source Color": ("color",),
    "Color": ("color",),
    "Status": ("status",),
    "Enabled": ("status",),
    "Source Interfaces": ("source-interface", "srcintf"),
    "Source Addresses": ("source-address", "srcaddr"),
    "Destination Addresses": ("destination-address", "dstaddr"),
    "Services": ("service",),
    "Interface": ("interface",),
    "Gateway": ("gateway",),
    "Source": ("source", "src"),
    "Destination": ("destination", "dst"),
    "Comment": ("comment", "comments"),
    "Comments": ("comments", "comment"),
    "Port": ("port",),
    "Protocol": ("protocol",),
    "Type": ("type",),
    "Minimum Protocol": ("ssl-min-proto-ver",),
    "Maximum Protocol": ("ssl-max-proto-ver",),
    "Server Certificate": ("servercert",),
    "Default Portal": ("default-portal",),
    "Tunnel IP Pools": ("tunnel-ip-pools",),
    "Source Explicit Fields": ("__explicit_fields__",),
}


def export_excel(
    *,
    extracted: ExtractionResult,
    validation: ValidationResult,
    output: BinaryIO | Path | str,
    config: ExtractionConfig | None = None,
    derived: DerivedViews | None = None,
    source_name: str | None = None,
) -> None:
    """
    Write the FortiGate Excel report.

    The original workbook remains the compatibility baseline for worksheet
    names/columns.  Cross-vendor target sheets and the obsolete Extraction
    Evidence sheet are excluded.  Current source/derived fields are added
    without turning Excel into a semantic layer.
    """

    del config  # reserved for future presentation-only export options

    derived = derived or build_derived_views(extracted.config)

    context = _ExcelContext(
        extracted=extracted,
        derived=derived,
        validation=validation,
        source_name=source_name,
    )

    workbook = _build_workbook(context)

    if isinstance(output, (str, Path)):
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        workbook.save(path)
        return

    workbook.save(output)


class _ExcelContext:
    def __init__(
        self,
        *,
        extracted: ExtractionResult,
        derived: DerivedViews,
        validation: ValidationResult,
        source_name: str | None,
    ) -> None:
        self.extracted = extracted
        self.config = extracted.config
        self.derived = derived
        self.validation = validation
        self.source_name = source_name or ""
        self.source_by_path: dict[str, list[SourceObjectRecord]] = defaultdict(list)

        for record in extracted.source_objects:
            self.source_by_path[record.source_path].append(record)

        self.issues_by_object: dict[tuple[str, str], list[ValidationIssue]] = defaultdict(list)

        for issue in validation.issues:
            if issue.object_name:
                self.issues_by_object[(issue.vdom, str(issue.object_name))].append(issue)

    def issues_for(
        self,
        *,
        vdom: str,
        names: Iterable[Any],
    ) -> list[ValidationIssue]:
        found: list[ValidationIssue] = []
        seen: set[tuple[str, str, str]] = set()

        for name in names:
            if name in (None, ""):
                continue

            for issue in self.issues_by_object.get((vdom, str(name)), ()):
                key = (issue.domain, issue.field or "", issue.message)
                if key in seen:
                    continue
                seen.add(key)
                found.append(issue)

        return found


def _build_workbook(context: _ExcelContext) -> Workbook:
    workbook = Workbook()
    workbook.remove(workbook.active)

    order = [
        name
        for name in SHEET_ORDER
        if name not in _OLD_CROSS_VENDOR_SHEETS
    ]

    extra_names = {name for name, _ in _EXTRA_SHEETS}

    if "Addresses" in order and "Wildcard FQDN" not in order:
        order.insert(order.index("Addresses") + 1, "Wildcard FQDN")

    if "DHCP IP Ranges" in order and "DHCP Exclude Ranges" not in order:
        order.insert(order.index("DHCP IP Ranges") + 1, "DHCP Exclude Ranges")

    validation_anchor = order.index("Dependency Registry") if "Dependency Registry" in order else len(order)
    if "External Resources" not in order:
        order.insert(validation_anchor, "External Resources")

    extra_headers = dict(_EXTRA_SHEETS)

    for sheet_name in order:
        if sheet_name == "Summary":
            _build_summary(workbook, context, order)
            continue

        headers = list(extra_headers.get(sheet_name, SHEET_HEADERS.get(sheet_name, ())))

        if not headers:
            headers = ["Name", "Extraction Status", "Additional Settings"]

        headers = [
            "Analysis Status" if header == "Migration Status" else header
            for header in headers
        ]

        for extra in _EXTRA_COLUMNS.get(sheet_name, ()):
            if extra not in headers:
                _insert_extra_header(headers, extra)

        rows = _rows_for_sheet(sheet_name, context, headers)
        _write_table_sheet(
            workbook,
            sheet_name,
            headers,
            rows,
            context=context,
        )

    return workbook


def _insert_extra_header(headers: list[str], header: str) -> None:
    if header in {
        "Relationship",
        "Topology Kind",
        "Aggregate",
        "Physical Interfaces",
        "Topology Issues",
    } and "Name" in headers:
        index = headers.index("Name") + 1
        while index < len(headers) and headers[index] in {
            "Relationship",
            "Topology Kind",
            "Aggregate",
            "Physical Interfaces",
            "Topology Issues",
        }:
            index += 1
        headers.insert(index, header)
        return

    headers.append(header)


def _rows_for_sheet(
    sheet_name: str,
    context: _ExcelContext,
    headers: Sequence[str],
) -> list[dict[str, Any]]:
    builders = {
        "Review Required": _review_rows,
        "Interfaces": _interface_rows,
        "Interface Secondary IPs": _interface_secondary_rows,
        "Zones": _zone_rows,
        "Addresses": _address_rows,
        "Wildcard FQDN": _wildcard_fqdn_rows,
        "Address Groups": _address_group_rows,
        "Address Group Tags": _address_group_tag_rows,
        "Service Categories": _service_category_rows,
        "Services": _service_rows,
        "Service Groups": _service_group_rows,
        "Policies": _policy_rows,
        "IP Pools": _ip_pool_rows,
        "Virtual IPs": _vip_rows,
        "VIP Real Servers": _vip_real_server_rows,
        "VIP Groups": _vip_group_rows,
        "NAT Rules": _nat_rows,
        "Routes": _route_rows,
        "VPN Tunnels": _vpn_phase1_rows,
        "VPN Phase 2": _vpn_phase2_rows,
        "DHCP Servers": _dhcp_server_rows,
        "DHCP IP Ranges": _dhcp_ip_range_rows,
        "DHCP Exclude Ranges": _dhcp_exclude_range_rows,
        "DHCP Reservations": _dhcp_reservation_rows,
        "SD-WAN": _sdwan_rows,
        "SD-WAN Zones": _sdwan_zone_rows,
        "SD-WAN Members": _sdwan_member_rows,
        "SD-WAN Health Checks": _sdwan_health_rows,
        "SD-WAN Rules": _sdwan_rule_rows,
        "SSL VPN Settings": _ssl_settings_rows,
        "SSL VPN Portals": _ssl_portal_rows,
        "SSL VPN Authentication Rules": _ssl_auth_rule_rows,
        "SSL VPN Host Checks": _ssl_host_check_rows,
        "SSL VPN Host Check Items": _ssl_host_check_item_rows,
        "Local Users": _local_user_rows,
        "User Groups": _user_group_rows,
        "User Group Matches": _user_group_match_rows,
        "User Group Guests": _user_group_guest_rows,
        "Administrators": _administrator_rows,
        "Admin Profiles": _admin_profile_rows,
        "Admin Profile Permissions": _admin_permission_rows,
        "IPS Sensors": _ips_sensor_rows,
        "IPS Sensor Entries": _ips_entry_rows,
        "IPS Exempt IPs": _ips_exempt_rows,
        "Security Profiles": _security_profile_rows,
        "External Resources": _external_resource_rows,
        "FortiGate Source Configuration": _source_configuration_rows,
        "Firewall Policy Source Settings": _policy_source_rows,
        "Interface Source Settings": _interface_source_rows,
        "Interface Nested Configuration": _interface_nested_rows,
        "Dependency Registry": _dependency_rows,
        "Unresolved References": _unresolved_reference_rows,
        "Warnings": _warning_rows,
        "Unsupported": _unsupported_rows,
        "Source Inventory": _source_inventory_rows,
        "Extraction Coverage": _coverage_rows,
    }

    builder = builders.get(sheet_name)

    if builder is not None:
        return builder(context, headers)

    return _generic_source_rows(sheet_name, context, headers)


def _build_summary(
    workbook: Workbook,
    context: _ExcelContext,
    order: Sequence[str],
) -> None:
    sheet = workbook.create_sheet("Summary")
    sheet.sheet_view.showGridLines = False
    sheet.freeze_panes = "A5"

    sheet.merge_cells("A1:F1")
    sheet["A1"] = "FortiGate Configuration Report"
    sheet["A1"].fill = _TITLE_FILL
    sheet["A1"].font = Font(color="FFFFFF", bold=True, size=18)
    sheet["A1"].alignment = Alignment(vertical="center")
    sheet.row_dimensions[1].height = 30

    metadata = [
        ("Source file", context.source_name or "Not provided"),
        ("Generated UTC", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")),
        ("VDOMs", "\n".join(_vdoms(context)) or "root"),
        ("Validation errors", len(context.validation.errors)),
        ("Validation warnings", len(context.validation.warnings)),
    ]

    for row_number, (label, value) in enumerate(metadata, start=3):
        sheet.cell(row_number, 1, label).font = Font(bold=True, color="41504C")
        sheet.cell(row_number, 2, _excel_safe(value))
        sheet.cell(row_number, 2).alignment = Alignment(wrap_text=True, vertical="top")

    section_row = 10
    sheet.cell(section_row, 1, "Inventory")
    sheet.cell(section_row, 1).fill = _HEADER_FILL
    sheet.cell(section_row, 1).font = _WHITE_FONT
    sheet.merge_cells(start_row=section_row, start_column=1, end_row=section_row, end_column=3)

    counts = _inventory_counts(context)

    row_number = section_row + 1
    for label, count, target in counts:
        sheet.cell(row_number, 1, label)
        sheet.cell(row_number, 2, count)
        if target in order:
            cell = sheet.cell(row_number, 3, "Open sheet")
            cell.hyperlink = f"#'{target}'!A1"
            cell.font = _LINK_FONT
        row_number += 1

    nav_col = 5
    sheet.cell(3, nav_col, "Workbook navigation")
    sheet.cell(3, nav_col).fill = _HEADER_FILL
    sheet.cell(3, nav_col).font = _WHITE_FONT

    nav_row = 4
    for name in order:
        if name == "Summary":
            continue
        cell = sheet.cell(nav_row, nav_col, name)
        cell.hyperlink = f"#'{name}'!A1"
        cell.font = _LINK_FONT
        nav_row += 1

    sheet.column_dimensions["A"].width = 28
    sheet.column_dimensions["B"].width = 24
    sheet.column_dimensions["C"].width = 16
    sheet.column_dimensions["E"].width = 34


def _write_table_sheet(
    workbook: Workbook,
    sheet_name: str,
    headers: Sequence[str],
    rows: Sequence[Mapping[str, Any]],
    *,
    context: _ExcelContext,
) -> None:
    sheet = workbook.create_sheet(sheet_name)
    sheet.sheet_view.showGridLines = False
    sheet.sheet_view.zoomScale = 90

    max_col = max(len(headers), 1)
    sheet.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max_col)
    sheet.cell(1, 1, sheet_name)
    sheet.cell(1, 1).fill = _TITLE_FILL
    sheet.cell(1, 1).font = _TITLE_FONT
    sheet.cell(1, 1).alignment = Alignment(vertical="center")
    sheet.row_dimensions[1].height = 24

    if max_col > 1:
        sheet.merge_cells(
            start_row=2,
            start_column=1,
            end_row=2,
            end_column=max_col - 1,
        )
    note = sheet.cell(2, 1)
    note.value = _sheet_note(sheet_name, len(rows))
    note.font = _MUTED_FONT
    note.alignment = Alignment(wrap_text=True, vertical="top")

    for column, header in enumerate(headers, start=1):
        cell = sheet.cell(3, column, header)
        cell.fill = _HEADER_FILL
        cell.font = _HEADER_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        cell.border = _BORDER

        if sheet_name == "Interfaces" and header in {
            "Name",
            "Relationship",
            "Topology Kind",
            "Aggregate",
            "Physical Interfaces",
            "Topology Issues",
            "Parent / Underlay Interface",
            "Members",
        }:
            cell.fill = PatternFill("solid", fgColor="28786B")

    for index, row in enumerate(rows, start=4):
        for column, header in enumerate(headers, start=1):
            value = _excel_safe(row.get(header))
            cell = sheet.cell(index, column, value)
            cell.alignment = Alignment(wrap_text=True, vertical="top")

        if index % 2 == 1:
            for column in range(1, max_col + 1):
                sheet.cell(index, column).fill = _ALT_FILL

        outline = row.get("__outline_level__")
        if isinstance(outline, int) and outline > 0:
            sheet.row_dimensions[index].outlineLevel = min(outline, 7)

        if row.get("__review__"):
            for column in range(1, max_col + 1):
                if sheet.cell(index, column).fill == PatternFill():
                    sheet.cell(index, column).fill = _REVIEW_FILL

    if rows:
        sheet.auto_filter.ref = f"A3:{get_column_letter(max_col)}{len(rows) + 3}"

    sheet.freeze_panes = _freeze_pane(sheet_name, headers)
    _apply_widths(sheet, headers)
    _add_back_link(sheet)

    if sheet_name == "Review Required":
        _apply_review_colors(sheet, headers, len(rows))


def _add_back_link(sheet) -> None:
    if sheet.max_column <= 1:
        return

    cell = sheet.cell(2, sheet.max_column)
    cell.value = "Back to Summary"
    cell.hyperlink = "#'Summary'!A1"
    cell.font = _LINK_FONT
    cell.alignment = Alignment(horizontal="right")


def _apply_review_colors(sheet, headers: Sequence[str], row_count: int) -> None:
    if "Severity" not in headers:
        return

    severity_col = headers.index("Severity") + 1

    for row in range(4, row_count + 4):
        severity = str(sheet.cell(row, severity_col).value or "").lower()
        fill = _ERROR_FILL if severity == "error" else _WARNING_FILL

        for column in range(1, len(headers) + 1):
            sheet.cell(row, column).fill = fill


def _apply_widths(sheet, headers: Sequence[str]) -> None:
    for index, header in enumerate(headers, start=1):
        normalized = header.lower()

        if any(token in normalized for token in ("additional settings", "review reason", "raw capture", "notes")):
            width = 36
        elif any(token in normalized for token in ("description", "comment", "source path", "setting", "value")):
            width = 28
        elif any(token in normalized for token in ("members", "addresses", "interfaces", "services", "profiles", "references")):
            width = 26
        elif any(token in normalized for token in ("name", "object", "category", "status", "type")):
            width = 20
        elif "id" in normalized or "port" in normalized or "vlan" in normalized:
            width = 14
        else:
            width = 18

        sheet.column_dimensions[get_column_letter(index)].width = width


def _freeze_pane(sheet_name: str, headers: Sequence[str]) -> str:
    if sheet_name == "Interfaces":
        return "D4"
    if sheet_name == "Policies":
        return "D4"
    if len(headers) > 12:
        return "C4"
    return "A4"


def _sheet_note(sheet_name: str, row_count: int) -> str:
    if row_count:
        return (
            f"{row_count} record(s). Values are explicit FortiGate source data "
            "unless a column is clearly identified as derived/analysis output."
        )

    return (
        "No matching explicit FortiGate source records were extracted. "
        "The worksheet is retained for compatibility with the original workbook."
    )


def _inventory_counts(context: _ExcelContext) -> list[tuple[str, int, str]]:
    config = context.config
    return [
        ("Interfaces", len(config.interfaces), "Interfaces"),
        ("Zones", len(config.zones), "Zones"),
        ("Addresses", len(config.addresses), "Addresses"),
        ("Address Groups", len(config.address_groups), "Address Groups"),
        ("Services", len(context.derived.services.services), "Services"),
        ("Policies", len(config.policies), "Policies"),
        ("IP Pools", len(config.ip_pools), "IP Pools"),
        ("Virtual IPs", len(config.vips), "Virtual IPs"),
        ("Routes", len(config.static_routes), "Routes"),
        ("VPN Phase 1", len(config.ipsec_phase1), "VPN Tunnels"),
        ("VPN Phase 2", len(config.ipsec_phase2), "VPN Phase 2"),
        ("Local Users", len(config.local_users), "Local Users"),
        ("Validation Errors", len(context.validation.errors), "Review Required"),
        ("Validation Warnings", len(context.validation.warnings), "Review Required"),
    ]


def _vdoms(context: _ExcelContext) -> list[str]:
    values = {
        getattr(item, "vdom", "root")
        for collection_name in (
            "interfaces",
            "zones",
            "addresses",
            "policies",
            "static_routes",
            "ipsec_phase1",
        )
        for item in getattr(context.config, collection_name, ())
    }
    return sorted(values)


def _review_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    for issue in context.validation.issues:
        row = {
            "Severity": issue.severity.value,
            "Category": issue.domain,
            "Object": issue.object_name,
            "Issue / Review Reason": issue.message,
            "Status": "REVIEW_REQUIRED",
            "Source Sheet": _sheet_for_domain(issue.domain),
            "Source Row": None,
        }
        rows.append(row)

    return rows


def _interface_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    config = context.config
    topology = {(item.vdom, item.name): item for item in context.derived.topology.interfaces}
    vpn_topology = {(item.vdom, item.name): item for item in context.derived.topology.vpns}
    interfaces = {(item.vdom, item.name): item for item in config.interfaces}

    zones_by_interface: dict[tuple[str, str], list[str]] = defaultdict(list)
    for zone in config.zones:
        for member in zone.members:
            zones_by_interface[(zone.vdom, member)].append(zone.name)

    aggregate_owner: dict[tuple[str, str], str] = {}
    for interface in config.interfaces:
        item = topology.get((interface.vdom, interface.name))
        if item and item.kind == "aggregate":
            for member in interface.members:
                aggregate_owner[(interface.vdom, member)] = interface.name

    child_map: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    for interface in config.interfaces:
        if interface.interface:
            child_map[(interface.vdom, interface.interface)].append((interface.vdom, interface.name))

    synthetic_vpns: dict[tuple[str, str], list[Any]] = defaultdict(list)
    for vpn in context.derived.topology.vpns:
        if (vpn.vdom, vpn.name) in interfaces:
            continue
        if vpn.attached_interface:
            synthetic_vpns[(vpn.vdom, vpn.attached_interface)].append(vpn)

    roots: list[tuple[str, str]] = []
    for key, interface in interfaces.items():
        if interface.interface:
            continue
        if key in aggregate_owner:
            continue
        roots.append(key)

    roots.sort(key=lambda key: (key[0], _interface_rank(topology.get(key)), key[1].lower()))
    rows: list[dict[str, Any]] = []
    visited: set[tuple[str, str]] = set()

    def emit_interface(
        key: tuple[str, str],
        *,
        prefix: str,
        connector: str,
        relation: str | None,
        depth: int,
    ) -> None:
        if key in visited:
            return

        visited.add(key)
        interface = interfaces[key]
        top = topology.get(key)
        kind = top.kind if top else (interface.type or "logical")
        symbol = _topology_symbol(kind, is_vpn=(key in vpn_topology))
        display_name = f"{prefix}{connector}{symbol} {interface.name}".rstrip()

        row = {
            "Name": display_name,
            "Relationship": relation or "—",
            "Topology Kind": "ipsec" if key in vpn_topology else kind,
            "Alias": interface.alias,
            "Zone": zones_by_interface.get(key, []),
            "IP / Prefix": interface.ip,
            "Interface Type": interface.type or ("ipsec" if key in vpn_topology else kind),
            "Role": interface.role,
            "Addressing Mode": interface.mode,
            "Management Access": interface.allowaccess,
            "VLAN ID": interface.vlanid,
            "Enabled": _enabled_text(interface.status),
            "Source VDOM": interface.vdom,
            "Description": interface.description,
            "VRF": interface.vrf,
            "Members": interface.members,
            "Parent / Underlay Interface": interface.interface,
            "Aggregate": top.aggregate if top else None,
            "Physical Interfaces": list(top.physical_interfaces) if top else [],
            "Topology Issues": list(top.issues) if top else [],
            "Source Explicit Fields": sorted(interface.explicit_fields),
            "Additional Settings": sanitize_source_attributes(interface.raw_extra),
            "__outline_level__": depth,
        }

        _add_analysis_status(
            row,
            context,
            vdom=interface.vdom,
            names=(interface.name,),
        )
        _overlay_raw(row, interface.raw_extra, headers)
        rows.append(row)

        children: list[tuple[str, str, str]] = []

        if kind == "aggregate":
            for member in interface.members:
                member_key = (interface.vdom, member)
                if member_key in interfaces:
                    children.append(("member", member, "member"))

        for child_key in child_map.get(key, ()):
            if child_key[1] in interface.members:
                continue
            children.append(("interface", child_key[1], "child"))

        for vpn in synthetic_vpns.get(key, ()):
            children.append(("vpn", vpn.name, "child"))

        children.sort(key=lambda item: (0 if item[2] == "member" else 1, item[1].lower()))

        for index, (child_type, name, relation_type) in enumerate(children):
            last = index == len(children) - 1
            branch = "└─ " if last else "├─ "
            next_prefix = prefix + ("   " if connector == "└─ " else "│  " if connector else "")

            if child_type in {"member", "interface"}:
                child_key = (interface.vdom, name)
                relation_text = (
                    f"Member of {interface.name}"
                    if relation_type == "member"
                    else f"Child of {interface.name}"
                )
                emit_interface(
                    child_key,
                    prefix=next_prefix,
                    connector=branch,
                    relation=relation_text,
                    depth=depth + 1,
                )
            else:
                vpn = next(
                    item
                    for item in synthetic_vpns[key]
                    if item.name == name
                )
                phase1 = next(
                    item
                    for item in config.ipsec_phase1
                    if item.vdom == vpn.vdom and item.name == vpn.name
                )
                vpn_row = {
                    "Name": f"{next_prefix}{branch}◈ {vpn.name}",
                    "Relationship": f"Child of {interface.name}",
                    "Topology Kind": "ipsec",
                    "Interface Type": "ipsec",
                    "Source VDOM": vpn.vdom,
                    "Description": phase1.comments,
                    "Parent / Underlay Interface": vpn.attached_interface,
                    "Aggregate": vpn.aggregate,
                    "Physical Interfaces": list(vpn.physical_interfaces),
                    "Topology Issues": list(vpn.issues),
                    "Source Explicit Fields": sorted(phase1.explicit_fields),
                    "Additional Settings": sanitize_source_attributes(phase1.raw_extra),
                    "__outline_level__": depth + 1,
                }
                _add_analysis_status(
                    vpn_row,
                    context,
                    vdom=vpn.vdom,
                    names=(vpn.name,),
                )
                rows.append(vpn_row)

    for root in roots:
        emit_interface(
            root,
            prefix="",
            connector="",
            relation=None,
            depth=0,
        )

    # Broken/cyclic/orphaned interfaces still need to be visible.
    for key in sorted(set(interfaces) - visited):
        emit_interface(
            key,
            prefix="",
            connector="",
            relation="Unresolved topology",
            depth=0,
        )

    return rows


def _interface_secondary_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for interface in context.config.interfaces:
        for item in interface.secondary_ips:
            row = {
                "Interface": interface.name,
                "Secondary IP Status": "Configured",
                "Source ID": item.id,
                "Source IP": item.ip,
                "IP / Prefix": item.ip,
                "Management Access": item.allowaccess,
                "Extraction Status": "EXTRACTED",
                "Manual Review": "No",
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _zone_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for item in context.config.zones:
        row = {
            "VDOM": item.vdom,
            "Name": item.name,
            "Zone Type": "zone",
            "Members": item.members,
            "Description": item.description,
            "Configured Intrazone": item.intrazone,
            "Source Path": "system zone",
            "Additional Settings": sanitize_source_attributes(item.raw_extra),
        }
        _add_analysis_status(row, context, vdom=item.vdom, names=(item.name,))
        _overlay_raw(row, item.raw_extra, headers)
        rows.append(row)
    return rows


def _address_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for item in context.config.addresses:
        value = item.subnet or (
            f"{item.start_ip}-{item.end_ip}" if item.start_ip and item.end_ip else None
        ) or item.fqdn or item.wildcard or item.wildcard_fqdn
        row = {
            "Name": item.name,
            "Type": item.type,
            "Value": value,
            "Address Family": item.address_family,
            "Associated Interface": item.associated_interface,
            "Allow Routing": item.allow_routing,
            "Tags": [
                tag
                for entry in item.tagging
                for tag in entry.tags
            ],
            "Description": item.comment,
            "Source Section": "firewall address6" if item.address_family == "ipv6" else "firewall address",
            "Additional Settings": sanitize_source_attributes(item.raw_extra),
        }
        _add_analysis_status(row, context, vdom=item.vdom, names=(item.name,))
        _overlay_raw(row, item.raw_extra, headers)
        rows.append(row)
    return rows


def _wildcard_fqdn_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for item in context.config.wildcard_fqdns:
        row = {
            "Name": item.name,
            "Wildcard FQDN": item.wildcard_fqdn,
            "Description": item.comment,
            "Source VDOM": item.vdom,
            "Source Explicit Fields": sorted(item.explicit_fields),
            "Additional Settings": sanitize_source_attributes(item.raw_extra),
        }
        _add_analysis_status(row, context, vdom=item.vdom, names=(item.name,))
        rows.append(row)
    return rows


def _address_group_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for item in context.config.address_groups:
        row = {
            "Name": item.name,
            "Members": item.members,
            "Address Family": _address_group_family(item.raw_extra),
            "Exclusion Enabled": item.exclude,
            "Exclude Members": item.exclude_members,
            "Description": item.comment,
            "Allow Routing": item.allow_routing,
            "Source Category": item.category,
            "Group Type": item.type,
            "Tags": [tag for entry in item.tagging for tag in entry.tags],
            "Additional Settings": sanitize_source_attributes(item.raw_extra),
        }
        _add_analysis_status(row, context, vdom=item.vdom, names=(item.name,))
        _overlay_raw(row, item.raw_extra, headers)
        rows.append(row)
    return rows


def _address_group_tag_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for group in context.config.address_groups:
        for tag in group.tagging:
            rows.append(
                {
                    "Group Name": group.name,
                    "Address Family": _address_group_family(group.raw_extra),
                    "Tag Entry": tag.name,
                    "Category": tag.category,
                    "Tags": tag.tags,
                    "Extraction Status": "EXTRACTED",
                    "Manual Review": "No",
                    "Additional Settings": sanitize_source_attributes(tag.raw_extra),
                }
            )
    return rows


def _service_category_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for item in context.config.service_categories:
        row = {
            "Name": item.name,
            "Description": item.comment,
            "Extraction Status": "EXTRACTED",
            "Additional Settings": sanitize_source_attributes(item.raw_extra),
        }
        _overlay_raw(row, item.raw_extra, headers)
        rows.append(row)
    return rows


def _service_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    source = {(item.vdom, item.name): item for item in context.config.services}
    rows = []
    for item in context.derived.services.services:
        source_item = source.get((item.vdom, item.source_name or item.name))
        row = {
            "Name": item.name,
            "Category": getattr(source_item, "category", None),
            "Configured Protocol": getattr(source_item, "protocol", None),
            "Effective Protocol": item.protocol,
            "Protocol / Destination Port": (
                f"{item.protocol}/{item.port}" if item.port else item.protocol
            ),
            "Description": item.comment,
            "Source Protocol Number": item.protocol_number,
            "Source Port Constraint": item.source_port,
            "Additional Settings": (
                sanitize_source_attributes(source_item.raw_extra)
                if source_item is not None
                else {}
            ),
        }
        _add_analysis_status(
            row,
            context,
            vdom=item.vdom,
            names=(item.source_name, item.name),
        )
        if source_item is not None:
            _overlay_raw(row, source_item.raw_extra, headers)
        rows.append(row)
    return rows


def _service_group_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    source = {(item.vdom, item.name): item for item in context.config.service_groups}
    rows = []
    for item in context.derived.services.groups:
        source_item = source.get((item.vdom, item.name))
        row = {
            "Name": item.name,
            "Members": list(item.members),
            "Description": item.comment,
            "Additional Settings": (
                sanitize_source_attributes(source_item.raw_extra)
                if source_item is not None
                else {}
            ),
        }
        _add_analysis_status(row, context, vdom=item.vdom, names=(item.name,))
        if source_item is not None:
            _overlay_raw(row, source_item.raw_extra, headers)
        rows.append(row)
    return rows


def _policy_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    normalized = {
        (item.vdom, item.policy_id): item
        for item in context.derived.policy_names
    }
    rows = []
    for item in context.config.policies:
        name_info = normalized.get((item.vdom, item.policy_id))
        row = {
            "Rule #": item.policy_id,
            "Name": item.name,
            "Source Interface": item.srcintf,
            "Source Address (Normalized)": item.srcaddr,
            "Destination Interface": item.dstintf,
            "Destination Address (Normalized)": item.dstaddr,
            "Service (Normalized)": item.service,
            "Action (Normalized)": item.action,
            "Schedule (Normalized)": item.schedule,
            "NAT Enabled": _enabled_text(item.nat),
            "Effective UTM Status": item.utm_status,
            "Disabled": _disabled_text(item.status),
            "Source Policy ID": item.policy_id,
            "Source Address (Original)": item.srcaddr,
            "Source Address Negate": item.srcaddr_negate,
            "Source IPv6 Address": item.srcaddr6,
            "Source IPv6 Address Negate": item.srcaddr6_negate,
            "Destination Address (Original)": item.dstaddr,
            "Destination Address Negate": item.dstaddr_negate,
            "Destination IPv6 Address": item.dstaddr6,
            "Destination IPv6 Address Negate": item.dstaddr6_negate,
            "User Groups": item.groups,
            "Users": item.users,
            "Service (Original)": item.service,
            "Service Negate": item.service_negate,
            "Action (Original)": item.action,
            "Schedule (Original)": item.schedule,
            "VPN Tunnel": item.vpntunnel,
            "UTM Status": item.utm_status,
            "IP Pool Enabled": _enabled_text(item.ippool),
            "NAT Pool": item.poolname,
            "NAT Pool IPv6": item.poolname6,
            "Internet Service Status": item.internet_service,
            "Internet Services": item.internet_service_name,
            "Security Profile Group": item.profile_group,
            "Antivirus": item.av_profile,
            "IPS Sensor": item.ips_sensor,
            "Web Filter": item.webfilter_profile,
            "Application List": item.application_list,
            "SSL/SSH Profile": item.ssl_ssh_profile,
            "Source Profile Type": item.profile_type,
            "Source Profile Group": item.profile_group,
            "Log Setting": item.logtraffic,
            "Comments": item.comments,
            "Additional Settings": sanitize_source_attributes(item.raw_extra),
        }
        if name_info is not None:
            row["Normalized Name"] = name_info.normalized_name
        _add_analysis_status(
            row,
            context,
            vdom=item.vdom,
            names=(item.name, item.policy_id),
        )
        _overlay_raw(row, item.raw_extra, headers)
        rows.append(row)
    return rows


def _ip_pool_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.ip_pools,
        headers,
        {
            "Name": "name",
            "Type": "type",
            "Start IP": "startip",
            "End IP": "endip",
            "Source Start IP": "source_startip",
            "Source End IP": "source_endip",
            "Start Port": "startport",
            "End Port": "endport",
            "Associated Interface": "associated_interface",
            "ARP Reply": "arp_reply",
            "ARP Interface": "arp_intf",
            "Permit Any Host": "permit_any_host",
            "Excluded IPs": "exclude_ip",
            "NAT64": "nat64",
            "Add NAT64 Route": "add_nat64_route",
            "Comments": "comments",
        },
    )


def _vip_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.vips,
        headers,
        {
            "Name": "name",
            "Type": "type",
            "Status": "status",
            "External IP": "extip",
            "External Address Objects": "extaddr",
            "External Interface": "extintf",
            "Mapped IPs": "mappedip",
            "Mapped Address": "mapped_addr",
            "Port Forward": "portforward",
            "Protocol": "protocol",
            "External Port": "extport",
            "Mapped Port": "mappedport",
            "ARP Reply": "arp_reply",
            "NAT Source VIP": "nat_source_vip",
            "Service": "service",
            "Load Balance Method": "ldb_method",
            "Server Type": "server_type",
            "Monitor": "monitor",
            "Comment": "comment",
            "Source UUID": "uuid",
        },
    )


def _vip_real_server_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for vip in context.config.vips:
        for item in vip.realservers:
            row = {
                "VIP Name": vip.name,
                "Server ID": item.id,
                "IP": item.ip,
                "Address": item.address,
                "Port": item.port,
                "Status": item.status,
                "Weight": item.weight,
                "Monitor": item.monitor,
                "VDOM": vip.vdom,
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _vip_group_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.vip_groups,
        headers,
        {
            "Name": "name",
            "Interface": "interface",
            "Members": "members",
            "Comments": "comments",
            "Source UUID": "uuid",
        },
    )


def _nat_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for item in context.derived.nat:
        row = {
            "Policy ID": item.policy_id,
            "Policy Name": item.policy_name,
            "Translation Type": item.translation_type,
            "Pool Names": list(item.pool_names),
            "Translated Addresses": list(item.translated_addresses),
            "Egress Interfaces": list(item.egress_interfaces),
            "Issues": list(item.issues),
            "VDOM": item.vdom,
        }
        _add_analysis_status(
            row,
            context,
            vdom=item.vdom,
            names=(item.policy_name, item.policy_id),
            extra_reasons=item.issues,
        )
        rows.append(row)
    return rows


def _route_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.static_routes,
        headers,
        {
            "Route ID": "seq_num",
            "Destination": "dst",
            "Destination Address Object": "dstaddr",
            "Device": "device",
            "Gateway": "gateway",
            "Distance": "distance",
            "Priority": "priority",
            "Status": "status",
            "SD-WAN Zone": "sdwan_zone",
            "Preferred Source": "preferred_source",
            "Source": "src",
            "Dynamic Gateway": "dynamic_gateway",
            "Blackhole": "blackhole",
            "Comment": "comment",
            "Address Family": "address_family",
            "VDOM": "vdom",
            "VRF": "vrf",
        },
    )


def _vpn_phase1_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    topology = {(item.vdom, item.name): item for item in context.derived.topology.vpns}
    rows = []
    for item in context.config.ipsec_phase1:
        top = topology.get((item.vdom, item.name))
        row = {
            "Name": item.name,
            "Interface": item.interface,
            "Remote Gateway IPv4": item.remote_gw,
            "Remote Gateway DDNS": item.remotegw_ddns,
            "Type": item.type,
            "IKE Version": item.ike_version,
            "Authentication Method": item.authmethod,
            "Proposal": item.proposal,
            "DH Groups": item.dhgrp,
            "Key Lifetime": item.keylife,
            "NAT Traversal": item.nattraversal,
            "DPD": item.dpd,
            "Local Gateway": item.local_gw,
            "Local ID": item.localid,
            "Peer ID": item.peerid,
            "Certificate": item.certificate,
            "Comments": item.comments,
            "VDOM": item.vdom,
            "Attached Interface": top.attached_interface if top else item.interface,
            "Aggregate": top.aggregate if top else None,
            "Resolved Physical Interfaces": list(top.physical_interfaces) if top else [],
            "Topology Path": list(top.path) if top else [],
            "Topology Issues": list(top.issues) if top else [],
            "Source Explicit Fields": sorted(item.explicit_fields),
            "Additional Settings": sanitize_source_attributes(item.raw_extra),
        }
        _add_analysis_status(
            row,
            context,
            vdom=item.vdom,
            names=(item.name,),
            extra_reasons=(top.issues if top else ()),
        )
        _overlay_raw(row, item.raw_extra, headers)
        rows.append(row)
    return rows


def _vpn_phase2_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    normalized = {(item.vdom, item.name): item for item in context.derived.vpn.phase2}
    rows = []
    for item in context.config.ipsec_phase2:
        norm = normalized.get((item.vdom, item.name))
        row = {
            "Name": item.name,
            "Phase 1": item.phase1name,
            "Proposal": item.proposal,
            "PFS": item.pfs,
            "DH Groups": item.dhgrp,
            "Keylife Seconds": item.keylifeseconds,
            "Keylife KB": item.keylifekbs,
            "Source Range": norm.source_range if norm else None,
            "Destination Range": norm.destination_range if norm else None,
            "Source Address Type": item.src_addr_type,
            "Source Subnet": item.src_subnet,
            "Source Range Start": item.src_start_ip,
            "Source Range End": item.src_end_ip,
            "Destination Address Type": item.dst_addr_type,
            "Destination Subnet": item.dst_subnet,
            "Destination Range Start": item.dst_start_ip,
            "Destination Range End": item.dst_end_ip,
            "VDOM": item.vdom,
            "Comments": item.comments,
            "Source Explicit Fields": sorted(item.explicit_fields),
            "Additional Settings": sanitize_source_attributes(item.raw_extra),
        }
        _add_analysis_status(row, context, vdom=item.vdom, names=(item.name,))
        _overlay_raw(row, item.raw_extra, headers)
        rows.append(row)
    return rows


def _dhcp_server_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.dhcp_servers,
        headers,
        {
            "Server ID": "id",
            "Interface": "interface",
            "Status": "status",
            "Server Type": "server_type",
            "IP Mode": "ip_mode",
            "Default Gateway": "default_gateway",
            "Netmask": "netmask",
            "Lease Time": "lease_time",
            "DNS Service": "dns_service",
            "DNS Server 1": "dns_server1",
            "DNS Server 2": "dns_server2",
            "DNS Server 3": "dns_server3",
            "DNS Server 4": "dns_server4",
            "Timezone Option": "timezone_option",
            "Timezone": "timezone",
            "Relay Agent": "relay_agent",
            "VDOM": "vdom",
        },
    )


def _dhcp_ip_range_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _dhcp_child_rows(context, headers, "ip_ranges")


def _dhcp_exclude_range_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _dhcp_child_rows(context, headers, "exclude_ranges")


def _dhcp_reservation_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for server in context.config.dhcp_servers:
        for item in server.reserved_addresses:
            row = {
                "Server ID": server.id,
                "Interface": server.interface,
                "Reservation ID": item.id,
                "IP Address": item.ip,
                "MAC Address": item.mac,
                "Description": item.description,
                "Action": item.action,
                "Type": item.type,
                "VDOM": server.vdom,
                "Extraction Status": "EXTRACTED",
                "Source Explicit Fields": sorted(item.explicit_fields),
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _dhcp_child_rows(
    context: _ExcelContext,
    headers: Sequence[str],
    attribute: str,
) -> list[dict[str, Any]]:
    rows = []
    for server in context.config.dhcp_servers:
        for item in getattr(server, attribute):
            row = {
                "Server ID": server.id,
                "Interface": server.interface,
                "Range ID": item.id,
                "Source ID": item.id,
                "Start IP": item.start_ip,
                "End IP": item.end_ip,
                "Lease Time": item.lease_time,
                "VDOM": server.vdom,
                "Extraction Status": "EXTRACTED",
                "Manual Review": "No",
                "Source Explicit Fields": sorted(item.explicit_fields),
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _sdwan_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for item in context.config.sdwans:
        row = {
            "Status": item.status,
            "Load Balance Mode": item.load_balance_mode,
            "Extraction Status": "EXTRACTED",
            "Manual Review": "No",
            "Additional Settings": sanitize_source_attributes(item.raw_extra),
            "VDOM": item.vdom,
        }
        _overlay_raw(row, item.raw_extra, headers)
        rows.append(row)
    return rows


def _sdwan_zone_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for sdwan in context.config.sdwans:
        for item in sdwan.zones:
            row = {
                "Zone Name": item.name,
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
                "VDOM": sdwan.vdom,
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _sdwan_member_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    topology = {(item.vdom, item.name): item for item in context.derived.topology.interfaces}
    rows = []
    for sdwan in context.config.sdwans:
        for item in sdwan.members:
            top = topology.get((sdwan.vdom, item.interface or ""))
            row = {
                "ID": item.seq_num,
                "Interface": item.interface,
                "Zone": item.zone,
                "Gateway": item.gateway,
                "Source": item.source,
                "Cost": item.cost,
                "Weight": item.weight,
                "Priority": item.priority,
                "Status": item.status,
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
                "VDOM": sdwan.vdom,
                "Resolved Physical Interfaces": list(top.physical_interfaces) if top else [],
                "Aggregate": top.aggregate if top else None,
                "Source Explicit Fields": sorted(item.explicit_fields),
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _sdwan_health_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for sdwan in context.config.sdwans:
        for item in sdwan.health_checks:
            row = {
                "Name": item.name,
                "Server": item.server,
                "Members": item.members,
                "Protocol": item.protocol,
                "Interval": item.interval,
                "Fail Time": item.failtime,
                "Recovery Time": item.recoverytime,
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
                "VDOM": sdwan.vdom,
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _sdwan_rule_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for sdwan in context.config.sdwans:
        for item in sdwan.services:
            row = {
                "ID": item.id,
                "Name": item.name,
                "Status": item.status,
                "Mode": item.mode,
                "Source": item.src,
                "Destination": item.dst,
                "Priority Members": item.priority_members,
                "Health Checks": item.health_check,
                "Priority Zones": item.priority_zone,
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
                "VDOM": sdwan.vdom,
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _ssl_settings_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.ssl_vpn_settings,
        headers,
        {
            "Status": "status",
            "Minimum Protocol": "ssl_min_proto_ver",
            "Maximum Protocol": "ssl_max_proto_ver",
            "Authentication Timeout": "auth_timeout",
            "Idle Timeout": "idle_timeout",
            "Port": "port",
            "DNS Server 1": "dns_server1",
            "DNS Server 2": "dns_server2",
            "Server Certificate": "servercert",
            "Source Interfaces": "source_interface",
            "Source Addresses": "source_address",
            "Tunnel IP Pools": "tunnel_ip_pools",
            "Default Portal": "default_portal",
            "VDOM": "vdom",
        },
    )


def _ssl_portal_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.ssl_vpn_portals,
        headers,
        {
            "Name": "name",
            "Tunnel Mode": "tunnel_mode",
            "IPv6 Tunnel Mode": "ipv6_tunnel_mode",
            "IP Pools": "ip_pools",
            "IPv6 Pools": "ipv6_pools",
            "Split Tunneling": "split_tunneling",
            "Limit User Logins": "limit_user_logins",
            "FortiClient Download": "forticlient_download",
            "Host Check": "host_check",
            "Host Check Policies": "host_check_policy",
            "Split Tunneling Routing Addresses": "split_tunneling_routing_address",
            "VDOM": "vdom",
        },
    )


def _ssl_auth_rule_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for settings in context.config.ssl_vpn_settings:
        for item in settings.authentication_rules:
            row = {
                "ID": item.id,
                "Auth": item.auth,
                "Cipher": item.cipher,
                "Client Certificate": item.client_cert,
                "Realm": item.realm,
                "Source Interfaces": item.source_interface,
                "Source Addresses": item.source_address,
                "Source Address Negate": item.source_address_negate,
                "IPv6 Source Addresses": item.source_address6,
                "IPv6 Source Address Negate": item.source_address6_negate,
                "Users": item.users,
                "User Peer": item.user_peer,
                "Groups": item.groups,
                "Portal": item.portal,
                "Extraction Status": "EXTRACTED",
                "Manual Review": "No",
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _ssl_host_check_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.ssl_vpn_host_check_software,
        headers,
        {
            "Name": "name",
            "Type": "type",
            "OS Type": "os_type",
            "Version": "version",
            "GUID": "guid",
            "Check Item Count": lambda item: len(item.check_items),
            "VDOM": "vdom",
        },
    )


def _ssl_host_check_item_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for software in context.config.ssl_vpn_host_check_software:
        for item in software.check_items:
            row = {
                "Host Check": software.name,
                "ID": item.id,
                "Action": item.action,
                "Type": item.type,
                "Target": item.target,
                "MD5s": item.md5s,
                "Version": item.version,
                "Extraction Status": "EXTRACTED",
                "Manual Review": "No",
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _local_user_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(context, context.config.local_users, headers, {})


def _user_group_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.user_groups,
        headers,
        {
            "Name": "name",
            "Members": "members",
            "Group Type": "group_type",
            "ID": "id",
            "VDOM": "vdom",
        },
    )


def _user_group_match_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for group in context.config.user_groups:
        for item in group.matches:
            row = {
                "User Group": group.name,
                "Match ID": item.id,
                "Server Name": item.server_name,
                "Group Name": item.group_name,
                "VDOM": group.vdom,
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _user_group_guest_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for group in context.config.user_groups:
        for item in group.guests:
            row = {
                "User Group": group.name,
                "Guest ID": item.id,
                "Name": item.name,
                "User ID": item.user_id,
                "Email": item.email,
                "Mobile Phone": item.mobile_phone,
                "Expiration": item.expiration,
                "Sponsor": item.sponsor,
                "Comment": item.comment,
                "Password Configured": item.password_configured,
                "VDOM": group.vdom,
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _administrator_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(context, context.config.administrators, headers, {})


def _admin_profile_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(context, context.config.admin_profiles, headers, {})


def _admin_permission_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for profile in context.config.admin_profiles:
        for kind, permission in (
            ("Firewall", profile.firewall_permission),
            ("Log", profile.log_permission),
            ("Network", profile.network_permission),
            ("System", profile.system_permission),
            ("UTM", profile.utm_permission),
        ):
            if permission is None:
                continue
            values = permission.model_dump(mode="python", exclude={"raw_extra", "explicit_fields"})
            for setting, value in values.items():
                if value in (None, "", [], {}):
                    continue
                rows.append(
                    {
                        "Profile": profile.name,
                        "Permission Group": kind,
                        "Setting": setting,
                        "Value": value,
                        "Extraction Status": "EXTRACTED",
                        "Additional Settings": sanitize_source_attributes(permission.raw_extra),
                    }
                )
    return rows


def _ips_sensor_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(context, context.config.ips_sensors, headers, {})


def _ips_entry_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for sensor in context.config.ips_sensors:
        for item in sensor.entries:
            row = {
                "Sensor": sensor.name,
                "Entry ID": item.id,
                "Rule": item.rule,
                "CVE": item.cve,
                "Application": item.application,
                "OS": item.os,
                "Protocol": item.protocol,
                "Severity": item.severity,
                "Location": item.location,
                "Default Action": item.default_action,
                "Default Status": item.default_status,
                "Action": item.action,
                "Status": item.status,
                "Log": item.log,
                "VDOM": sensor.vdom,
                "Additional Settings": sanitize_source_attributes(item.raw_extra),
            }
            _overlay_raw(row, item.raw_extra, headers)
            rows.append(row)
    return rows


def _ips_exempt_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for sensor in context.config.ips_sensors:
        for entry in sensor.entries:
            for item in entry.exempt_ips:
                rows.append(
                    {
                        "Sensor": sensor.name,
                        "Entry ID": entry.id,
                        "Exempt IP ID": item.id,
                        "Source IP": item.src_ip,
                        "Destination IP": item.dst_ip,
                        "VDOM": sensor.vdom,
                        "Additional Settings": sanitize_source_attributes(item.raw_extra),
                    }
                )
    return rows


def _security_profile_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.profile_groups,
        headers,
        {
            "Name": "name",
            "Antivirus": "av_profile",
            "Vulnerability": "ips_sensor",
            "URL Filtering": "webfilter_profile",
            "SSL Decryption": "ssl_ssh_profile",
            "Description": None,
            "VDOM": "vdom",
        },
    )


def _external_resource_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    return _model_rows(
        context,
        context.config.external_resources,
        headers,
        {
            "Name": "name",
            "Resource": "resource",
            "Type": "type",
            "Refresh Rate": "refresh_rate",
            "Comments": "comments",
            "VDOM": "vdom",
        },
    )


def _source_configuration_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for record in context.extracted.source_objects:
        for command in record.commands:
            rows.append(
                {
                    "Category": _source_category(record.source_path),
                    "Source Path": record.source_path,
                    "Object": record.object_name,
                    "Source ID": record.object_name,
                    "Parent / Subsection": list(record.parent_objects),
                    "Operation": command.operation,
                    "Setting": command.key,
                    "Value": list(command.values),
                    "Analysis Status": "SOURCE",
                    "Manual Review": "No",
                }
            )
    return rows


def _policy_source_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    policy_names = {str(item.policy_id): item.name for item in context.config.policies if item.policy_id is not None}
    for record in context.source_by_path.get("firewall policy", ()):
        for command in record.commands:
            rows.append(
                {
                    "Source Policy ID": record.object_name,
                    "Policy Name": policy_names.get(str(record.object_name), ""),
                    "Operation": command.operation,
                    "Setting": command.key,
                    "Ordered Source Values": list(command.values),
                }
            )
    return rows


def _interface_source_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for record in context.source_by_path.get("system interface", ()):
        for command in record.commands:
            rows.append(
                {
                    "Interface": record.object_name,
                    "Source Vendor": "FortiGate",
                    "Setting": command.key,
                    "Value": list(command.values),
                    "Extraction Status": "EXTRACTED",
                }
            )
    return rows


def _interface_nested_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for record in context.extracted.source_objects:
        if not record.source_path.startswith("system interface "):
            continue
        interface = record.parent_objects[0] if record.parent_objects else None
        for command in record.commands:
            rows.append(
                {
                    "Interface": interface,
                    "Config Path": record.source_path,
                    "Node Type": "edit" if record.object_name is not None else "config",
                    "Object / Edit": record.object_name,
                    "Operation": command.operation,
                    "Setting": command.key,
                    "Value": list(command.values),
                    "Extraction Status": "EXTRACTED",
                    "Manual Review": "No",
                }
            )
    return rows


def _dependency_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    # The old IR dependency engine is intentionally not restored.  Present the
    # current FortiGate reference failures in the same audit-friendly columns.
    return _unresolved_reference_rows(context, headers)


def _unresolved_reference_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for item in collect_broken_references(context.config, index=context.derived.references):
        rows.append(
            {
                "Source VDOM": item.source_vdom,
                "Source Type": item.source_kind,
                "Source Object": item.source_name,
                "Field": item.source_field,
                "Reference": item.reference,
                "Expected Type": [kind.value for kind in item.expected_kinds],
                "Result": "UNRESOLVED",
                "Normalization Status": "UNRESOLVED",
                "Reason": "Reference could not be resolved in the same VDOM.",
            }
        )
    return rows


def _warning_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    for index, issue in enumerate(context.validation.warnings, start=1):
        rows.append(
            {
                "ID": index,
                "Category": issue.domain,
                "Confidence": "VALIDATION",
                "Message": issue.message,
            }
        )
    return rows


def _unsupported_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    registered = set(registered_sections())
    counts: dict[str, int] = defaultdict(int)

    for record in context.extracted.source_objects:
        if record.source_path not in registered:
            counts[record.source_path] += 1

    return [
        {
            "Section": path,
            "Item": count,
            "Status": "SOURCE_ONLY",
            "Reason": "No dedicated typed FortiGate model is currently defined for this source section.",
            "Manual Review": "No",
            "Raw Capture": "Preserved in Source Inventory / FortiGate Source Configuration",
        }
        for path, count in sorted(counts.items())
    ]


def _source_inventory_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    rows = []
    registered = set(registered_sections())

    for record in context.extracted.source_objects:
        safe_values = sanitize_source_attributes(record.values)
        if not safe_values:
            rows.append(
                {
                    "Vendor": "FortiGate",
                    "Domain": _source_category(record.source_path),
                    "Scope Type": "Object" if record.object_name is not None else "Config",
                    "Scope Name": record.object_name,
                    "Source Path": record.source_path,
                    "Object Name": record.object_name,
                    "Extraction Status": (
                        "TYPED" if record.source_path in registered else "SOURCE_ONLY"
                    ),
                    "Manual Review": "No",
                }
            )
            continue

        for setting, value in safe_values.items():
            rows.append(
                {
                    "Vendor": "FortiGate",
                    "Domain": _source_category(record.source_path),
                    "Scope Type": "Object" if record.object_name is not None else "Config",
                    "Scope Name": record.object_name,
                    "Source Path": record.source_path,
                    "Object Name": record.object_name,
                    "Setting": setting,
                    "Value": value,
                    "Extraction Status": (
                        "TYPED" if record.source_path in registered else "SOURCE_ONLY"
                    ),
                    "Manual Review": "No",
                }
            )
    return rows


def _coverage_rows(context: _ExcelContext, headers: Sequence[str]) -> list[dict[str, Any]]:
    registered = set(registered_sections())
    records_by_path = context.source_by_path
    rows = []

    for path in sorted(records_by_path):
        records = records_by_path[path]
        rows.append(
            {
                "Source Section": path,
                "Found": "Yes",
                "Source Objects": len(records),
                "Parsed Objects": len(records),
                "Normalized Objects": None,
                "Status": "TYPED" if path in registered else "SOURCE_ONLY",
                "Semantic Level": "typed-source" if path in registered else "raw-source",
                "Parser Handler": "command evaluator",
                "Line Start": min(
                    (record.start_line_number for record in records if record.start_line_number is not None),
                    default=None,
                ),
                "Line End": max(
                    (record.end_line_number for record in records if record.end_line_number is not None),
                    default=None,
                ),
                "Semantic Unknowns": 0 if path in registered else len(records),
                "Unresolved Dependencies": None,
                "Notes": (
                    "Typed primitive source extraction available."
                    if path in registered
                    else "Explicit source retained generically; no dedicated source model yet."
                ),
            }
        )

    return rows


def _generic_source_rows(
    sheet_name: str,
    context: _ExcelContext,
    headers: Sequence[str],
) -> list[dict[str, Any]]:
    paths = _SOURCE_PATHS_BY_SHEET.get(sheet_name, ())

    if not paths:
        return []

    rows: list[dict[str, Any]] = []

    for path in paths:
        for record in context.source_by_path.get(path, ()):
            rows.append(_generic_record_row(record, context, headers))

    return rows


def _generic_record_row(
    record: SourceObjectRecord,
    context: _ExcelContext,
    headers: Sequence[str],
) -> dict[str, Any]:
    values = sanitize_source_attributes(record.values)
    row: dict[str, Any] = {
        "Name": record.object_name,
        "Source Context": record.vdom,
        "Source VDOM": record.vdom,
        "VDOM": record.vdom,
        "Source Path": record.source_path,
        "Object / Instance": record.object_name,
        "Object": record.object_name,
        "ID": record.object_name,
        "Source ID": record.object_name,
        "Parent / Subsection": list(record.parent_objects),
        "Source Explicit Fields": list(record.explicit_fields),
        "Extraction Status": "EXTRACTED",
        "Analysis Status": "EXTRACTED",
        "Manual Review": "No",
    }

    consumed: set[str] = set()

    for header in headers:
        if header in row:
            continue
        value, source_key = _lookup_source_header(header, values)
        if source_key is not None:
            row[header] = value
            consumed.add(source_key)

    extra = {
        key: value
        for key, value in values.items()
        if key not in consumed
    }

    if "Additional Settings" in headers:
        row["Additional Settings"] = extra

    _add_analysis_status(
        row,
        context,
        vdom=record.vdom,
        names=(record.object_name,),
    )

    return row


def _model_rows(
    context: _ExcelContext,
    objects: Iterable[Any],
    headers: Sequence[str],
    mapping: Mapping[str, str | None | Any],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    for item in objects:
        data = item.model_dump(mode="python")
        row: dict[str, Any] = {}

        for header, attribute in mapping.items():
            if callable(attribute):
                row[header] = attribute(item)
            elif attribute:
                row[header] = data.get(attribute)

        # Populate obvious old workbook columns from model field names.
        for header in headers:
            if header in row:
                continue

            key = _header_to_model_key(header)
            if key in data:
                row[header] = data[key]

        raw_extra = sanitize_source_attributes(data.get("raw_extra", {}))
        _overlay_raw(row, raw_extra, headers)

        if "Source Explicit Fields" in headers:
            row["Source Explicit Fields"] = sorted(data.get("explicit_fields", []))

        if "Typed Source Fields" in headers:
            row["Typed Source Fields"] = sorted(data.get("explicit_fields", []))

        if "Additional Settings" in headers:
            row["Additional Settings"] = raw_extra

        vdom = str(data.get("vdom") or "global")
        name = (
            data.get("name")
            or data.get("policy_id")
            or data.get("seq_num")
            or data.get("id")
        )
        _add_analysis_status(row, context, vdom=vdom, names=(name,))

        rows.append(row)

    return rows


def _add_analysis_status(
    row: dict[str, Any],
    context: _ExcelContext,
    *,
    vdom: str,
    names: Iterable[Any],
    extra_reasons: Iterable[str] = (),
) -> None:
    issues = context.issues_for(vdom=vdom, names=names)
    reasons = [issue.message for issue in issues]
    reasons.extend(str(reason) for reason in extra_reasons if reason)
    reasons = list(dict.fromkeys(reasons))

    row["Analysis Status"] = "REVIEW_REQUIRED" if reasons else "EXTRACTED"
    row["Extraction Status"] = "PARTIAL" if reasons else "EXTRACTED"
    row["Manual Review"] = "Yes" if reasons else "No"
    row["Review Reasons"] = reasons
    row["Audit Note"] = reasons
    row["__review__"] = bool(reasons)


def _overlay_raw(
    row: dict[str, Any],
    raw: Mapping[str, Any],
    headers: Sequence[str],
) -> None:
    safe = sanitize_source_attributes(raw)

    for header in headers:
        if row.get(header) not in (None, "", [], {}):
            continue

        value, _ = _lookup_source_header(header, safe)
        if value not in (None, "", [], {}):
            row[header] = value


def _lookup_source_header(
    header: str,
    values: Mapping[str, Any],
) -> tuple[Any, str | None]:
    normalized_values = {
        _normalize_key(key): (key, value)
        for key, value in values.items()
    }

    candidates = list(_HEADER_ALIASES.get(header, ()))
    candidates.extend(_header_candidates(header))

    for candidate in candidates:
        normalized = _normalize_key(candidate)
        if normalized in normalized_values:
            source_key, value = normalized_values[normalized]
            return value, source_key

    return None, None


def _header_candidates(header: str) -> list[str]:
    value = header.lower()
    replacements = {
        " / ": " ",
        "/": " ",
        "(": " ",
        ")": " ",
        "#": " number ",
        "+": " ",
        ":": " ",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)

    words = [
        word
        for word in value.replace("_", " ").replace("-", " ").split()
        if word not in {
            "source",
            "configured",
            "effective",
            "original",
            "normalized",
            "setting",
            "settings",
            "explicit",
            "additional",
        }
    ]

    if not words:
        return []

    joined = "-".join(words)
    return [joined, "_".join(words), words[-1]]


def _header_to_model_key(header: str) -> str:
    return "_".join(
        word
        for word in _header_candidates(header)[:1][0].replace("-", " ").split()
    ) if _header_candidates(header) else ""


def _normalize_key(value: Any) -> str:
    return str(value).strip().lower().replace("-", "_").replace(" ", "_")


def _enabled_text(value: Any) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"enable", "enabled", "up", "yes", "true", "1"}:
        return "Yes"
    if normalized in {"disable", "disabled", "down", "no", "false", "0"}:
        return "No"
    return str(value)


def _disabled_text(value: Any) -> str | None:
    enabled = _enabled_text(value)
    if enabled == "Yes":
        return "No"
    if enabled == "No":
        return "Yes"
    return None


def _interface_rank(item: Any) -> int:
    kind = getattr(item, "kind", "")
    return {
        "aggregate": 0,
        "physical": 1,
        "vlan": 2,
        "tunnel": 3,
        "logical": 4,
    }.get(kind, 5)


def _topology_symbol(kind: str, *, is_vpn: bool = False) -> str:
    if is_vpn or kind == "tunnel":
        return "◈"
    if kind == "aggregate":
        return "◆"
    if kind == "vlan":
        return "▣"
    if kind == "physical":
        return "●"
    return "◇"


def _address_group_family(raw_extra: Mapping[str, Any]) -> str | None:
    source_section = str(raw_extra.get("source_section") or "")
    if "addrgrp6" in source_section:
        return "ipv6"
    return None


def _source_category(path: str) -> str:
    parts = path.split()
    return " ".join(parts[:2]) if len(parts) >= 2 else path


def _sheet_for_domain(domain: str) -> str:
    return {
        "interface": "Interfaces",
        "interface_topology": "Interfaces",
        "zone": "Zones",
        "address": "Addresses",
        "address_group": "Address Groups",
        "service": "Services",
        "service_group": "Service Groups",
        "policy": "Policies",
        "nat": "NAT Rules",
        "vip": "Virtual IPs",
        "vip_group": "VIP Groups",
        "ip_pool": "IP Pools",
        "ipsec_phase1": "VPN Tunnels",
        "vpn_topology": "VPN Tunnels",
        "vpn_phase2": "VPN Phase 2",
        "static_route": "Routes",
        "user_group": "User Groups",
        "ips_sensor": "IPS Sensors",
    }.get(domain, "Source Inventory")


def _excel_safe(value: Any) -> Any:
    value = _plain_value(value)

    if isinstance(value, str) and value.startswith(("=", "+", "-", "@")):
        return "'" + value

    return value


def _plain_value(value: Any) -> Any:
    if value is None:
        return None

    if isinstance(value, Enum):
        return value.value

    if is_dataclass(value):
        return _plain_value(asdict(value))

    if isinstance(value, Mapping):
        return "\n".join(
            f"{key} = {_plain_value(item)}"
            for key, item in value.items()
        )

    if isinstance(value, (list, tuple, set, frozenset)):
        return "\n".join(
            str(_plain_value(item))
            for item in value
            if item not in (None, "", [], {})
        )

    if isinstance(value, bool):
        return "Yes" if value else "No"

    if isinstance(value, (str, int, float)):
        return value

    return str(value)
