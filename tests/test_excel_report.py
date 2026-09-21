from __future__ import annotations

import io
import unittest

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

from fortigate_extract.config import ExtractionConfig
from fortigate_extract.derived import build_derived_views
from fortigate_extract.export import export_excel
from fortigate_extract.export.excel_schema import SHEET_HEADERS, SHEET_ORDER
from fortigate_extract.extraction.extractor import extract_fortigate_config
from fortigate_extract.parser import parse_fortigate_config
from fortigate_extract.validation.validator import validate_config


_SAMPLE_CONFIG = r"""
config system global
    set hostname "FG-TEST"
end

config system interface
    edit "wan-dhcp"
        set mode dhcp
    next
    edit "wan-pppoe"
        set mode pppoe
        set pppoe-username "source-user"
    next
    edit "port1"
        set ip 192.0.2.1 255.255.255.0
        set allowaccess ping https
        config secondaryip
            edit 1
                set ip 192.0.2.2 255.255.255.0
                set ha-priority 20
            next
        end
    next
    edit "port2"
    next
    edit "agg1"
        set type aggregate
        set member "port1" "port2"
    next
    edit "vlan100"
        set type vlan
        set interface "agg1"
        set vlanid 100
        set ip 10.100.0.1 255.255.255.0
        set ip6 2001:db8:100::1/64
    next
end

config firewall service custom
    edit "multi-port"
        set tcp-portrange 80 443
        set udp-portrange 53
    next
    edit "single-port"
        set protocol TCP
        set tcp-portrange 8443
    next
end

config firewall service group
    edit "web-services"
        set member "multi-port" "single-port"
    next
end

config firewall address
    edit "inside"
        set subnet 10.100.0.0 255.255.255.0
    next
end

config firewall ippool
    edit "pool1"
        set startip 198.51.100.10
        set endip 198.51.100.20
    next
end

config firewall vip
    edit "lb-vip"
        set type server-load-balance
        set extip 198.51.100.30
        set extintf "wan-dhcp"
        set ldb-method round-robin
        config realservers
            edit 1
                set ip 10.100.0.10
                set port 443
            next
            edit 2
                set ip 10.100.0.11
                set port 443
            next
        end
    next
end

config vpn ipsec phase1-interface
    edit "VPN-HQ"
        set interface "vlan100"
        set remote-gw 203.0.113.2
        set psksecret "do-not-export-this-secret"
    next
end

config vpn ipsec phase2-interface
    edit "VPN-subnet"
        set phase1name "VPN-HQ"
        set src-subnet 10.100.0.0 255.255.255.0
        set dst-subnet 10.200.0.0 255.255.255.0
    next
    edit "VPN-range"
        set phase1name "VPN-HQ"
        set src-start-ip 10.100.0.10
        set src-end-ip 10.100.0.20
        set dst-start-ip 10.200.0.10
        set dst-end-ip 10.200.0.20
    next
end

config firewall policy
    edit 1
        set name "A policy name that is deliberately much longer than thirty-two characters"
        set srcintf "vlan100"
        set dstintf "port1"
        set srcaddr "inside"
        set dstaddr "all"
        set service "web-services"
        set action accept
        set schedule always
        set nat enable
    next
    edit 2
        set name "Collision policy name with a shared long prefix A"
        set srcintf "vlan100"
        set dstintf "port1"
        set srcaddr "inside"
        set dstaddr "all"
        set service "multi-port"
        set action accept
        set schedule always
        set nat enable
        set ippool enable
        set poolname "pool1"
    next
    edit 3
        set name "Collision policy name with a shared long prefix B"
        set srcintf "vlan100"
        set dstintf "port1" "port2"
        set srcaddr "inside"
        set dstaddr "all"
        set service "multi-port"
        set action accept
        set schedule always
        set nat enable
    next
    edit 4
        set name "short policy"
    next
end

config firewall unsupported-section
    edit "source-only"
        set unsupported-setting "preserve-me"
    next
end

config user local
    edit "alice"
        set type password
        set passwd "another-do-not-export-secret"
    next
end
"""


class ExcelReportTest(unittest.TestCase):
    def _workbook(self, config_text: str = _SAMPLE_CONFIG):
        extracted = extract_fortigate_config(
            parse_fortigate_config(config_text),
            config=ExtractionConfig(),
        )
        derived = build_derived_views(extracted.config)
        validation = validate_config(extracted.config, derived=derived)
        output = io.BytesIO()
        export_excel(
            extracted=extracted,
            derived=derived,
            validation=validation,
            output=output,
            source_name="sample.conf",
        )
        output.seek(0)
        return load_workbook(output, data_only=False)

    @staticmethod
    def _rows(sheet):
        headers = [sheet.cell(3, column).value for column in range(1, sheet.max_column + 1)]
        return headers, list(sheet.iter_rows(min_row=4, values_only=True))

    def test_workbook_order_headers_and_removed_sheets(self):
        workbook = self._workbook()
        self.assertEqual(list(SHEET_ORDER), workbook.sheetnames)
        removed = {
            "Address Group Tags", "Schedules", "Schedule Groups", "Local-In Policies",
            "Multicast Policies", "Policy Routes", "DHCP Exclude Ranges", "Routing Protocol Settings",
            "Session TTL Settings", "Session TTL Overrides", "SD-WAN SLAs", "SD-WAN Duplication",
            "SD-WAN Neighbors", "SD-WAN Rule SLAs", "SSL VPN Host Checks", "SSL VPN Host Check Items",
            "SSL VPN Bookmark Groups", "SSL VPN Bookmarks", "LDAP Servers", "RADIUS Servers",
            "TACACS+ Servers", "SAML Servers", "FSSO Servers", "FortiTokens", "Authentication Rules",
            "Identity Server Endpoints", "Extraction Evidence", "Firewall Policy Source Settings",
            "Interface Source Settings", "Interface Nested Configuration",
        }
        self.assertTrue(removed.isdisjoint(workbook.sheetnames))
        for sheet_name in SHEET_ORDER:
            if sheet_name == "Summary":
                continue
            sheet = workbook[sheet_name]
            self.assertEqual(
                list(SHEET_HEADERS[sheet_name]),
                [sheet.cell(3, column).value for column in range(1, sheet.max_column + 1)],
                sheet_name,
            )

    def test_source_and_topology_contract(self):
        workbook = self._workbook()
        interfaces, rows = self._rows(workbook["Interfaces"])
        name = interfaces.index("Name")
        names = {row[name] for row in rows}
        self.assertEqual({"wan-dhcp", "wan-pppoe", "port1", "port2", "agg1", "vlan100"}, names)
        by_name = {row[name]: row for row in rows}
        self.assertEqual("dhcp", by_name["wan-dhcp"][interfaces.index("Addressing Mode")])
        self.assertIsNone(by_name["port2"][interfaces.index("Addressing Mode")])
        self.assertEqual("agg1", by_name["vlan100"][interfaces.index("Parent Interface")])
        self.assertEqual("port1\nport2", by_name["vlan100"][interfaces.index("Physical Interfaces")])
        self.assertNotIn("VPN-HQ", names)

        secondary, rows = self._rows(workbook["Interface Secondary IPs"])
        row = rows[0]
        self.assertEqual("192.0.2.2 255.255.255.0", row[secondary.index("IP / Prefix")])
        self.assertEqual(20, row[secondary.index("HA Priority")])

        summary = workbook["Summary"]
        summary_values = {summary.cell(row, 1).value: summary.cell(row, 2).value for row in range(1, summary.max_row + 1)}
        self.assertEqual("FG-TEST", summary_values["Hostname"])
        self.assertEqual("Yes", summary_values["IPv6 Explicit Configuration Present"])

    def test_semantics_and_source_preservation(self):
        workbook = self._workbook()
        services, rows = self._rows(workbook["Services"])
        service_rows = {row[services.index("Name")]: row for row in rows}
        generated = [row for row in rows if row[services.index("Source Service")] == "multi-port"]
        self.assertTrue(all(row[services.index("Generated")] == "Yes" for row in generated))
        self.assertIn("80", str(service_rows["multi-port-1"][services.index("Destination Port")]))

        groups, rows = self._rows(workbook["Service Groups"])
        group = {row[groups.index("Name")]: row for row in rows}
        self.assertEqual("Yes", group["multi-port"][groups.index("Generated")])
        self.assertEqual("No", group["web-services"][groups.index("Generated")])

        policies, rows = self._rows(workbook["Policies"])
        self.assertIsNotNone(rows[0][policies.index("Source Name")])
        self.assertTrue(rows[0][policies.index("Policy Name")].endswith("-L"))
        self.assertIsNotNone(rows[1][policies.index("Source Name")])
        self.assertIsNotNone(rows[2][policies.index("Source Name")])
        self.assertIsNone(rows[3][policies.index("Source Name")])
        self.assertEqual("pool1", rows[1][policies.index("IP Pool Name")])
        self.assertIsNone(rows[2][policies.index("SNAT Address")])

        nat, rows = self._rows(workbook["NAT Rules"])
        nat_by_rule = {row[nat.index("Rule #")]: row for row in rows}
        self.assertEqual("192.0.2.1", nat_by_rule[1][nat.index("SNAT Address")])
        self.assertEqual("198.51.100.10-198.51.100.20", nat_by_rule[2][nat.index("SNAT Address")])
        self.assertIsNone(nat_by_rule[3][nat.index("SNAT Address")])

        vips, rows = self._rows(workbook["Virtual IPs"])
        vip = next(row for row in rows if row[vips.index("Name")] == "lb-vip")
        self.assertEqual("round-robin", vip[vips.index("Load Balance Method")])
        self.assertEqual(2, vip[vips.index("Real Server Count")])

        phase2, rows = self._rows(workbook["VPN Phase 2"])
        by_name = {row[phase2.index("Name")]: row for row in rows}
        self.assertEqual("10.100.0.0-10.100.0.255", by_name["VPN-subnet"][phase2.index("Source Range")])
        self.assertEqual("10.100.0.10-10.100.0.20", by_name["VPN-range"][phase2.index("Source Range")])

        inventory_values = [cell.value for row in workbook["Source Inventory"].iter_rows() for cell in row]
        self.assertIn("2001:db8:100::1/64", inventory_values)
        self.assertIn("preserve-me", inventory_values)

    def test_presentation_and_review_contract(self):
        workbook = self._workbook()
        interfaces = workbook["Interfaces"]
        self.assertEqual("D4", interfaces.freeze_panes)
        self.assertEqual("17324D", interfaces["A1"].fill.fgColor.rgb[-6:])
        self.assertEqual("0F766E", interfaces["A3"].fill.fgColor.rgb[-6:])
        self.assertTrue(interfaces.column_dimensions["V"].hidden)
        self.assertTrue(interfaces.column_dimensions["W"].hidden)
        self.assertTrue(interfaces.auto_filter.ref.startswith("A3:"))
        self.assertEqual("#'Summary'!A1", interfaces[2][interfaces.max_column - 1].hyperlink.target)

        for sheet_name, headers in SHEET_HEADERS.items():
            if sheet_name == "Summary":
                continue
            sheet = workbook[sheet_name]
            for column, header in enumerate(headers, start=1):
                if header in {"Source Explicit Fields", "Additional Settings"}:
                    self.assertTrue(sheet.column_dimensions[get_column_letter(column)].hidden)

        review, rows = self._rows(workbook["Review Required"])
        for row in rows:
            self.assertTrue(row[review.index("VDOM")])
            self.assertTrue(row[review.index("Field")])

    def test_secrets_and_removed_legacy_target_columns(self):
        workbook = self._workbook()
        forbidden = {"do-not-export-this-secret", "another-do-not-export-secret"}
        for sheet in workbook.worksheets:
            for row in sheet.iter_rows():
                for cell in row:
                    self.assertTrue(not any(secret in str(cell.value) for secret in forbidden))

        system_headers, _ = self._rows(workbook["System Settings"])
        self.assertNotIn("Management IPv4 Address", system_headers)
        policy_headers, _ = self._rows(workbook["Policies"])
        self.assertNotIn("Source Address (Original)", policy_headers)
        pool_headers, _ = self._rows(workbook["IP Pools"])
        self.assertNotIn("Check Point Pool Object Type", pool_headers)
        security_headers, _ = self._rows(workbook["Security Profiles"])
        self.assertNotIn("WildFire", security_headers)


if __name__ == "__main__":
    unittest.main()
