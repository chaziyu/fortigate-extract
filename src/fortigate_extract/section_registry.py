"""Declarative FortiGate section field metadata."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


@dataclass(frozen=True, slots=True)
class SectionSpec:
    """
    Primitive source-field behavior for one FortiGate config section.

    This registry describes only how explicit CLI values should be
    represented before FortiGate semantic extraction.

    It does not:
        - construct models
        - apply FortiOS defaults
        - resolve references
        - perform validation
        - know Excel/report destinations
    """

    source_path: str

    list_fields: frozenset[str] = field(
        default_factory=frozenset
    )

    integer_fields: frozenset[str] = field(
        default_factory=frozenset
    )

    integer_list_fields: frozenset[str] = field(
        default_factory=frozenset
    )

    scalar_fields: frozenset[str] = field(
        default_factory=frozenset
    )

    secret_fields: frozenset[str] = field(
        default_factory=frozenset
    )


SECTION_REGISTRY: dict[str, SectionSpec] = {}


def _fields(*names: str) -> frozenset[str]:
    return frozenset(names)


def register_section(spec: SectionSpec) -> None:
    """Register one immutable section specification."""

    categories = {
        "list_fields": spec.list_fields,
        "integer_fields": spec.integer_fields,
        "integer_list_fields": spec.integer_list_fields,
        "scalar_fields": spec.scalar_fields,
    }

    names = list(categories)

    for index, left_name in enumerate(names):
        for right_name in names[index + 1:]:
            overlap = (
                categories[left_name]
                & categories[right_name]
            )

            if overlap:
                raise ValueError(
                    f"{spec.source_path!r}: "
                    f"fields {sorted(overlap)!r} appear in both "
                    f"{left_name} and {right_name}"
                )

    SECTION_REGISTRY[spec.source_path] = spec


def get_section_spec(
    source_path: str,
) -> SectionSpec | None:
    return SECTION_REGISTRY.get(source_path)


def is_registered_section(
    source_path: str,
) -> bool:
    return source_path in SECTION_REGISTRY


def registered_sections() -> tuple[str, ...]:
    return tuple(sorted(SECTION_REGISTRY))


# ----------------------------------------------------------------------
# Interfaces / zones
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="system interface",
        list_fields=_fields(
            "allowaccess",
            "member",
            "dhcp_relay_ip",
            "fail_alert_interfaces",
            "fail_detect_option",
            "dns_server_protocol",
            "security_groups",
        ),
        integer_fields=_fields(
            "vlanid",
            "vrf",
            "mtu",
            "tcp_mss",
            "distance",
            "priority",
            "ha_priority",
            "min_links",
            "weight",
            "snmp_index",
            "link_up_delay",
            "link_down_delay",
            "dhcp_renew_time",
            "lacp_select_timeout",
            "bandwidth",
        ),
        scalar_fields=_fields(
            "type",
            "mode",
            "ip",
            "interface",
            "alias",
            "description",
            "status",
            "role",
            "defaultgw",
            "lacp_mode",
            "lacp_speed",
            "aggregate_type",
            "management_ip",
        ),
        secret_fields=_fields(
            "password",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system interface secondaryip",
        integer_fields=_fields(
            "id",
            "ha_priority",
        ),
        scalar_fields=_fields(
            "ip",
            "allowaccess",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system zone",
        list_fields=_fields(
            "interface",
        ),
        scalar_fields=_fields(
            "description",
            "intrazone",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system zone tagging",
        list_fields=_fields(
            "tags",
        ),
        scalar_fields=_fields(
            "category",
        ),
    )
)


# ----------------------------------------------------------------------
# Addresses
# ----------------------------------------------------------------------

ADDRESS_SCALAR_FIELDS = _fields(
    "type",
    "subnet",
    "start_ip",
    "end_ip",
    "fqdn",
    "wildcard",
    "wildcard_fqdn",
    "associated_interface",
    "allow_routing",
    "comment",
)

register_section(
    SectionSpec(
        source_path="firewall address",
        integer_fields=_fields(
            "cache_ttl",
            "route_tag",
            "color",
        ),
        scalar_fields=ADDRESS_SCALAR_FIELDS,
    )
)

register_section(
    SectionSpec(
        source_path="firewall address6",
        integer_fields=_fields(
            "cache_ttl",
            "route_tag",
            "color",
        ),
        scalar_fields=_fields(
            "type",
            "ip6",
            "start_ip",
            "end_ip",
            "fqdn",
            "associated_interface",
            "allow_routing",
            "comment",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall address tagging",
        list_fields=_fields(
            "tags",
        ),
        scalar_fields=_fields(
            "category",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall addrgrp",
        list_fields=_fields(
            "member",
            "exclude_member",
        ),
        integer_fields=_fields(
            "color",
        ),
        scalar_fields=_fields(
            "exclude",
            "comment",
            "type",
            "category",
            "allow_routing",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall addrgrp6",
        list_fields=_fields(
            "member",
            "exclude_member",
        ),
        integer_fields=_fields(
            "color",
        ),
        scalar_fields=_fields(
            "exclude",
            "comment",
            "type",
            "category",
            "allow_routing",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall addrgrp tagging",
        list_fields=_fields(
            "tags",
        ),
        scalar_fields=_fields(
            "category",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall wildcard-fqdn custom",
        scalar_fields=_fields(
            "wildcard_fqdn",
            "comment",
        ),
    )
)


# ----------------------------------------------------------------------
# Services
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="firewall service category",
        scalar_fields=_fields(
            "comment",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall service custom",
        integer_fields=_fields(
            "protocol_number",
            "icmptype",
            "icmpcode",
            "session_ttl",
        ),
        scalar_fields=_fields(
            "category",
            "protocol",
            "tcp_portrange",
            "udp_portrange",
            "sctp_portrange",
            "proxy",
            "comment",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall service group",
        list_fields=_fields(
            "member",
        ),
        scalar_fields=_fields(
            "proxy",
            "comment",
        ),
    )
)


# ----------------------------------------------------------------------
# Schedules
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="firewall schedule onetime",
        integer_fields=_fields(
            "expiration_days",
        ),
        scalar_fields=_fields(
            "start",
            "end",
            "start_utc",
            "end_utc",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall schedule recurring",
        list_fields=_fields(
            "day",
        ),
        scalar_fields=_fields(
            "start",
            "end",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall schedule group",
        list_fields=_fields(
            "member",
        ),
    )
)


# ----------------------------------------------------------------------
# Firewall policy
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="firewall policy",
        list_fields=_fields(
            "srcintf",
            "dstintf",
            "srcaddr",
            "dstaddr",
            "srcaddr6",
            "dstaddr6",
            "service",
            "groups",
            "users",
            "poolname",
            "poolname6",
            "internet_service_name",
            "internet_service_group",
            "internet_service_custom",
            "internet_service_custom_group",
            "internet_service_src_name",
            "internet_service_src_group",
            "internet_service_src_custom",
            "internet_service_src_custom_group",
            "internet_service6_name",
            "internet_service6_group",
            "internet_service6_custom",
            "internet_service6_custom_group",
            "internet_service6_src_name",
            "internet_service6_src_group",
            "internet_service6_src_custom",
            "internet_service6_src_custom_group",
        ),
        integer_fields=_fields(
            "policyid",
            "session_ttl",
        ),
        scalar_fields=_fields(
            "name",
            "status",
            "action",
            "schedule",
            "nat",
            "ippool",
            "srcaddr_negate",
            "dstaddr_negate",
            "srcaddr6_negate",
            "dstaddr6_negate",
            "service_negate",
            "internet_service",
            "internet_service_src",
            "utm_status",
            "inspection_mode",
            "profile_type",
            "profile_group",
            "av_profile",
            "ips_sensor",
            "application_list",
            "webfilter_profile",
            "dnsfilter_profile",
            "ssl_ssh_profile",
            "logtraffic",
            "comments",
        ),
    )
)


# ----------------------------------------------------------------------
# NAT / VIP
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="firewall ippool",
        list_fields=_fields(
            "exclude_ip",
        ),
        integer_fields=_fields(
            "startport",
            "endport",
            "block_size",
            "port_per_user",
        ),
        scalar_fields=_fields(
            "type",
            "startip",
            "endip",
            "source_startip",
            "source_endip",
            "associated_interface",
            "arp_reply",
            "arp_intf",
            "permit_any_host",
            "nat64",
            "add_nat64_route",
            "comments",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall vip",
        list_fields=_fields(
            "extaddr",
            "mappedip",
            "mapped_addr",
            "monitor",
            "service",
        ),
        scalar_fields=_fields(
            "uuid",
            "status",
            "type",
            "extip",
            "extintf",
            "portforward",
            "protocol",
            "extport",
            "mappedport",
            "arp_reply",
            "nat_source_vip",
            "ldb_method",
            "server_type",
            "comment",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall vip realservers",
        list_fields=_fields(
            "monitor",
        ),
        integer_fields=_fields(
            "id",
            "port",
            "weight",
        ),
        scalar_fields=_fields(
            "ip",
            "address",
            "status",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="firewall vipgrp",
        list_fields=_fields(
            "member",
        ),
        scalar_fields=_fields(
            "uuid",
            "interface",
            "comments",
        ),
    )
)


# ----------------------------------------------------------------------
# Routing
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="router static",
        list_fields=_fields(
            "sdwan_zone",
        ),
        integer_fields=_fields(
            "distance",
            "priority",
            "vrf",
            "tag",
        ),
        scalar_fields=_fields(
            "dst",
            "dstaddr",
            "device",
            "gateway",
            "dynamic_gateway",
            "src",
            "preferred_source",
            "status",
            "blackhole",
            "comment",
        ),
    )
)


# ----------------------------------------------------------------------
# IPsec
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="vpn ipsec phase1-interface",
        list_fields=_fields(
            "proposal",
            "dhgrp",
            "certificate",
        ),
        integer_fields=_fields(
            "keylife",
            "distance",
            "priority",
        ),
        scalar_fields=_fields(
            "type",
            "interface",
            "local_gw",
            "remote_gw",
            "remotegw_ddns",
            "ike_version",
            "authmethod",
            "nattraversal",
            "dpd",
            "localid",
            "peerid",
            "comments",
        ),
        secret_fields=_fields(
            "psksecret",
            "psksecret_remote",
            "ppk_secret",
            "authpasswd",
            "group_authentication_secret",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="vpn ipsec phase2-interface",
        list_fields=_fields(
            "proposal",
            "dhgrp",
            "src_name",
            "dst_name",
        ),
        integer_fields=_fields(
            "keylifeseconds",
            "keylifekbs",
            "protocol",
            "src_port",
            "dst_port",
        ),
        scalar_fields=_fields(
            "phase1name",
            "pfs",
            "src_addr_type",
            "src_subnet",
            "src_start_ip",
            "src_end_ip",
            "dst_addr_type",
            "dst_subnet",
            "dst_start_ip",
            "dst_end_ip",
            "replay",
            "auto_negotiate",
            "comments",
        ),
    )
)


# ----------------------------------------------------------------------
# DHCP
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="system dhcp server",
        integer_fields=_fields(
            "lease_time",
        ),
        scalar_fields=_fields(
            "status",
            "interface",
            "server_type",
            "ip_mode",
            "default_gateway",
            "netmask",
            "dns_service",
            "dns_server1",
            "dns_server2",
            "dns_server3",
            "dns_server4",
            "timezone_option",
            "timezone",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system dhcp server ip-range",
        integer_fields=_fields(
            "id",
            "lease_time",
        ),
        scalar_fields=_fields(
            "start_ip",
            "end_ip",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system dhcp server exclude-range",
        integer_fields=_fields(
            "id",
        ),
        scalar_fields=_fields(
            "start_ip",
            "end_ip",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system dhcp server reserved-address",
        integer_fields=_fields(
            "id",
        ),
        scalar_fields=_fields(
            "ip",
            "mac",
            "description",
            "action",
            "type",
        ),
    )
)


# ----------------------------------------------------------------------
# SD-WAN
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="system sdwan",
        scalar_fields=_fields(
            "status",
            "load_balance_mode",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system sdwan zone",
        integer_fields=_fields(
            "minimum_sla_meet_members",
        ),
        scalar_fields=_fields(
            "advpn_health_check",
            "advpn_select",
            "service_sla_tie_break",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system sdwan members",
        integer_fields=_fields(
            "seq_num",
            "priority",
            "cost",
            "weight",
        ),
        scalar_fields=_fields(
            "interface",
            "zone",
            "gateway",
            "source",
            "status",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system sdwan health-check",
        list_fields=_fields(
            "members",
            "server",
        ),
        integer_fields=_fields(
            "interval",
            "failtime",
            "recoverytime",
        ),
        scalar_fields=_fields(
            "protocol",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system sdwan service",
        list_fields=_fields(
            "src",
            "dst",
            "service",
            "priority_members",
            "priority_zone",
            "health_check",
        ),
        integer_fields=_fields(
            "id",
        ),
        scalar_fields=_fields(
            "name",
            "mode",
            "status",
        ),
    )
)


# ----------------------------------------------------------------------
# SSL VPN
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="vpn ssl settings",
        list_fields=_fields(
            "source_interface",
            "source_address",
            "source_address6",
            "tunnel_ip_pools",
            "tunnel_ipv6_pools",
        ),
        integer_fields=_fields(
            "auth_timeout",
            "idle_timeout",
            "port",
        ),
        scalar_fields=_fields(
            "status",
            "ssl_min_proto_ver",
            "ssl_max_proto_ver",
            "dns_server1",
            "dns_server2",
            "servercert",
            "default_portal",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="vpn ssl web portal",
        list_fields=_fields(
            "ip_pools",
            "ipv6_pools",
            "split_tunneling_routing_address",
            "ipv6_split_tunneling_routing_address",
            "host_check_policy",
        ),
        scalar_fields=_fields(
            "tunnel_mode",
            "ipv6_tunnel_mode",
            "split_tunneling",
            "ipv6_split_tunneling",
            "limit_user_logins",
            "forticlient_download",
            "web_mode",
            "host_check",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="vpn ssl web host-check-software",
        scalar_fields=_fields(
            "guid",
            "type",
            "os_type",
            "version",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="vpn ssl web host-check-software check-item-list",
        integer_fields=_fields(
            "id",
        ),
        list_fields=_fields(
            "md5s",
        ),
        scalar_fields=_fields(
            "action",
            "type",
            "target",
            "version",
        ),
    )
)


# ----------------------------------------------------------------------
# Users
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="user local",
        integer_fields=_fields(
            "id",
        ),
        scalar_fields=_fields(
            "status",
            "type",
            "passwd_time",
            "passwd_policy",
            "ldap_server",
            "radius_server",
            "tacacs_server",
            "two_factor",
            "two_factor_authentication",
            "two_factor_notification",
            "fortitoken",
            "email_to",
            "sms_phone",
            "sms_server",
            "sms_custom_server",
            "workstation",
            "username_sensitivity",
        ),
        secret_fields=_fields(
            "passwd",
            "ppk_secret",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="user group",
        list_fields=_fields(
            "member",
        ),
        integer_fields=_fields(
            "id",
            "authtimeout",
            "auth_concurrent_value",
        ),
        scalar_fields=_fields(
            "group_type",
            "auth_concurrent_override",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="user group match",
        integer_fields=_fields(
            "id",
        ),
        scalar_fields=_fields(
            "server_name",
            "group_name",
        ),
    )
)


# ----------------------------------------------------------------------
# Administrators
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="system admin",
        list_fields=_fields(
            "vdom",
        ),
        scalar_fields=_fields(
            "accprofile",
            "trusthost1",
            "trusthost2",
            "trusthost3",
            "trusthost4",
            "trusthost5",
            "trusthost6",
            "trusthost7",
            "trusthost8",
            "trusthost9",
            "trusthost10",
            "ip6_trusthost1",
            "ip6_trusthost2",
            "ip6_trusthost3",
            "ip6_trusthost4",
            "ip6_trusthost5",
            "ip6_trusthost6",
            "ip6_trusthost7",
            "ip6_trusthost8",
            "ip6_trusthost9",
            "ip6_trusthost10",
            "two_factor",
            "two_factor_authentication",
            "two_factor_notification",
            "fortitoken",
            "email_to",
            "sms_phone",
            "remote_auth",
            "remote_group",
            "peer_auth",
            "peer_group",
            "schedule",
            "comments",
        ),
        secret_fields=_fields(
            "password",
            "ssh_public_key1",
            "ssh_public_key2",
            "ssh_public_key3",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="system accprofile",
        integer_fields=_fields(
            "admintimeout",
        ),
        scalar_fields=_fields(
            "authgrp",
            "ftviewgrp",
            "fwgrp",
            "loggrp",
            "netgrp",
            "secfabgrp",
            "sysgrp",
            "utmgrp",
            "vpngrp",
            "wanoptgrp",
            "wifi",
            "scope",
            "cli_config",
            "cli_diagnose",
            "cli_exec",
            "cli_get",
            "cli_show",
            "admintimeout_override",
            "comments",
        ),
    )
)


# ----------------------------------------------------------------------
# IPS
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="ips sensor",
        scalar_fields=_fields(
            "comment",
            "block_malicious_url",
            "scan_botnet_connections",
            "extended_log",
            "replacemsg_group",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="ips sensor entries",
        list_fields=_fields(
            "rule",
            "cve",
            "application",
            "os",
            "protocol",
            "severity",
            "location",
            "vuln_type",
        ),
        integer_fields=_fields(
            "id",
            "rate_count",
            "rate_duration",
        ),
        scalar_fields=_fields(
            "action",
            "default_action",
            "default_status",
            "status",
            "log",
            "log_packet",
            "log_attack_context",
            "quarantine",
            "quarantine_expiry",
            "quarantine_log",
            "rate_mode",
            "rate_track",
            "last_modified",
        ),
    )
)

register_section(
    SectionSpec(
        source_path="ips sensor entries exempt-ip",
        integer_fields=_fields(
            "id",
        ),
        scalar_fields=_fields(
            "src_ip",
            "dst_ip",
        ),
    )
)


# ----------------------------------------------------------------------
# Security profile groups
# ----------------------------------------------------------------------

register_section(
    SectionSpec(
        source_path="firewall profile-group",
        scalar_fields=_fields(
            "application_list",
            "av_profile",
            "casb_profile",
            "cifs_profile",
            "diameter_filter_profile",
            "dlp_profile",
            "dnsfilter_profile",
            "emailfilter_profile",
            "file_filter_profile",
            "icap_profile",
            "ips_sensor",
            "ips_voip_filter",
            "profile_protocol_options",
            "sctp_filter_profile",
            "ssh_filter_profile",
            "ssl_ssh_profile",
            "videofilter_profile",
            "virtual_patch_profile",
            "voip_profile",
            "waf_profile",
            "webfilter_profile",
        ),
    )
)


# ----------------------------------------------------------------------
# Diagnostics
# ----------------------------------------------------------------------

def get_section_capability(
    source_path: str,
    encountered_fields: Iterable[str] = (),
) -> dict[str, object]:
    """
    Describe how much of one section is currently declared.

    Useful for diagnostics/tests, not normal extraction behavior.
    """

    spec = get_section_spec(source_path)

    encountered = {
        field.replace("-", "_")
        for field in encountered_fields
    }

    if spec is None:
        return {
            "source_path": source_path,
            "registered": False,
            "known_fields": [],
            "unknown_fields": sorted(encountered),
        }

    known = (
        spec.list_fields
        | spec.integer_fields
        | spec.integer_list_fields
        | spec.scalar_fields
        | spec.secret_fields
    )

    return {
        "source_path": source_path,
        "registered": True,
        "known_fields": sorted(known),
        "unknown_fields": sorted(
            encountered - known
        ),
    }