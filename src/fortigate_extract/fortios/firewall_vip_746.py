"""FortiOS 7.4.6 firewall VIP semantics and validation.

This module contains FortiOS-specific knowledge for `config firewall vip`:

    - reviewed source-field contract
    - documented effective defaults
    - source-accounting validation

It does not construct models, resolve references, or perform target-vendor
conversion.
"""

from __future__ import annotations

from typing import Any


FORTIOS_746_VIP_FIELDS: frozenset[str] = frozenset(
    {
        "add_nat46_route",
        "arp_reply",
        "color",
        "comment",
        "dns_mapping_ttl",
        "extaddr",
        "extintf",
        "extip",
        "extport",
        "gratuitous_arp_interval",
        "gslb_domain_name",
        "gslb_hostname",
        "h2_support",
        "h3_support",
        "http_cookie_age",
        "http_cookie_domain",
        "http_cookie_domain_from_host",
        "http_cookie_generation",
        "http_cookie_path",
        "http_cookie_share",
        "http_ip_header",
        "http_ip_header_name",
        "http_multiplex",
        "http_multiplex_max_concurrent_request",
        "http_multiplex_max_request",
        "http_multiplex_ttl",
        "http_redirect",
        "https_cookie_secure",
        "id",
        "ipv6_mappedip",
        "ipv6_mappedport",
        "ldb_method",
        "mapped_addr",
        "mappedip",
        "mappedport",
        "max_embryonic_connections",
        "monitor",
        "nat_source_vip",
        "nat44",
        "nat46",
        "one_click_gslb_server",
        "outlook_web_access",
        "persistence",
        "portforward",
        "portmapping_type",
        "protocol",
        "server_type",
        "service",
        "src_filter",
        "src_vip_filter",
        "srcintf_filter",
        "ssl_accept_ffdhe_groups",
        "ssl_algorithm",
        "ssl_certificate",
        "ssl_client_fallback",
        "ssl_client_rekey_count",
        "ssl_client_renegotiation",
        "ssl_client_session_state_max",
        "ssl_client_session_state_timeout",
        "ssl_client_session_state_type",
        "ssl_dh_bits",
        "ssl_hpkp",
        "ssl_hpkp_age",
        "ssl_hpkp_backup",
        "ssl_hpkp_include_subdomains",
        "ssl_hpkp_primary",
        "ssl_hpkp_report_uri",
        "ssl_hsts",
        "ssl_hsts_age",
        "ssl_hsts_include_subdomains",
        "ssl_http_location_conversion",
        "ssl_http_match_host",
        "ssl_max_version",
        "ssl_min_version",
        "ssl_mode",
        "ssl_pfs",
        "ssl_send_empty_frags",
        "ssl_server_algorithm",
        "ssl_server_max_version",
        "ssl_server_min_version",
        "ssl_server_renegotiation",
        "ssl_server_session_state_max",
        "ssl_server_session_state_timeout",
        "ssl_server_session_state_type",
        "status",
        "type",
        "uuid",
        "weblogic_server",
        "websphere_server",
    }
)


FORTIOS_746_VIP_NESTED_SECTIONS: frozenset[str] = frozenset(
    {
        "gslb-public-ips",
        "quic",
        "realservers",
        "ssl-cipher-suites",
        "ssl-server-cipher-suites",
    }
)


FORTIOS_746_VIP_DEFAULTS: dict[str, Any] = {
    "add_nat46_route": "enable",
    "arp_reply": "enable",
    "extintf": "any",
    "nat44": "enable",
    "nat46": "disable",
    "portforward": "disable",
    "portmapping_type": "1-to-1",
    "protocol": "tcp",
    "status": "enable",
    "type": "static-nat",
}


def effective_vip_settings_746(
    vip: Any,
) -> dict[str, Any]:
    """
    Return documented FortiOS 7.4.6 effective VIP values.

    The source model is not modified. Explicitly configured values win;
    missing values use the documented FortiOS defaults.
    """

    explicit_fields = set(
        getattr(vip, "explicit_fields", set())
    )

    result: dict[str, Any] = {}

    for field_name, default in FORTIOS_746_VIP_DEFAULTS.items():
        if field_name in explicit_fields:
            result[field_name] = getattr(
                vip,
                field_name,
                None,
            )
        else:
            result[field_name] = default

    return result


def validate_vip_746(
    vip: Any,
) -> list[str]:
    """
    Validate extracted VIP source accounting against the reviewed
    FortiOS 7.4.6 field contract.

    This intentionally does not attempt to validate every possible enum
    or feature combination.
    """

    issues: list[str] = []

    explicit_fields = set(
        getattr(vip, "explicit_fields", set())
    )

    raw_extra = dict(
        getattr(vip, "raw_extra", {}) or {}
    )

    # --------------------------------------------------------------
    # Explicit fields outside the reviewed 7.4.6 contract
    # --------------------------------------------------------------

    for field_name in sorted(
        explicit_fields - FORTIOS_746_VIP_FIELDS
    ):
        issues.append(
            f"VIP field "
            f"{field_name.replace('_', '-')!r} "
            f"is outside the reviewed FortiOS 7.4.6 field contract."
        )

    # --------------------------------------------------------------
    # Raw / untyped fields
    # --------------------------------------------------------------

    for key in sorted(raw_extra):
        if key.startswith("unparsed_"):
            issues.append(
                "Could not parse explicit VIP source value for "
                f"{key.removeprefix('unparsed_').replace('_', '-')}."
            )
            continue

        if key in FORTIOS_746_VIP_FIELDS:
            issues.append(
                f"FortiOS 7.4.6 VIP field "
                f"{key.replace('_', '-')!r} "
                "was preserved in raw_extra because it is not yet "
                "represented by the typed VIP model."
            )

    return list(dict.fromkeys(issues))