"""FortiOS 7.4.6 firewall IP-pool semantics and validation.

This module contains FortiOS-specific knowledge that should not live in
the parser or source models:

    - documented/default effective values
    - documented enum/range constraints
    - source-value validation
    - effective-value calculation

Source models remain explicit-source-only. Documented FortiOS defaults
are applied here only when an effective view is required.
"""

from __future__ import annotations

from ipaddress import IPv4Address, IPv6Address
from typing import Any


# ----------------------------------------------------------------------
# IPv4 IP pools
# ----------------------------------------------------------------------

FORTIOS_746_IPPOOL_TYPES: frozenset[str] = frozenset(
    {
        "overload",
        "one-to-one",
        "fixed-port-range",
        "port-block-allocation",
        "cgn-resource-allocation",
    }
)


FORTIOS_746_IPPOOL_FIELDS: frozenset[str] = frozenset(
    {
        "add_nat64_route",
        "arp_intf",
        "arp_reply",
        "associated_interface",
        "block_size",
        "cgn_block_size",
        "cgn_client_endip",
        "cgn_client_ipv6shift",
        "cgn_client_startip",
        "cgn_fixedalloc",
        "cgn_overload",
        "cgn_port_end",
        "cgn_port_start",
        "cgn_spa",
        "comments",
        "endip",
        "endport",
        "exclude_ip",
        "nat64",
        "num_blocks_per_user",
        "pba_interim_log",
        "pba_timeout",
        "permit_any_host",
        "port_per_user",
        "source_endip",
        "source_startip",
        "startip",
        "startport",
        "subnet_broadcast_in_ippool",
        "type",
        "utilization_alarm_clear",
        "utilization_alarm_raise",
    }
)


FORTIOS_746_IPPOOL_INTEGER_RANGES: dict[str, tuple[int, int]] = {
    "block_size": (64, 4096),
    "cgn_block_size": (64, 4096),
    "cgn_client_ipv6shift": (0, 127),
    "cgn_port_start": (1024, 65535),
    "cgn_port_end": (1024, 65535),
    "endport": (5117, 65533),
    "num_blocks_per_user": (1, 128),
    "pba_timeout": (3, 86400),
    "startport": (5117, 65533),
    "utilization_alarm_clear": (40, 100),
    "utilization_alarm_raise": (50, 100),
}


FORTIOS_746_IPPOOL_ZERO_OR_RANGES: dict[str, tuple[int, int]] = {
    "pba_interim_log": (600, 86400),
    "port_per_user": (32, 60417),
}


FORTIOS_746_IPPOOL_DEFAULTS: dict[str, Any] = {
    "add_nat64_route": "enable",
    "arp_reply": "enable",
    "block_size": 128,
    "cgn_block_size": 128,
    "cgn_client_ipv6shift": 0,
    "cgn_fixedalloc": "disable",
    "cgn_overload": "disable",
    "cgn_port_start": 5117,
    "cgn_port_end": 65530,
    "cgn_spa": "disable",
    "endip": "0.0.0.0",
    "endport": 65533,
    "nat64": "disable",
    "num_blocks_per_user": 8,
    "pba_interim_log": 0,
    "pba_timeout": 30,
    "permit_any_host": "disable",
    "port_per_user": 0,
    "source_startip": "0.0.0.0",
    "source_endip": "0.0.0.0",
    "startip": "0.0.0.0",
    "startport": 5117,
    "subnet_broadcast_in_ippool": "enable",
    "type": "overload",
    "utilization_alarm_clear": 80,
    "utilization_alarm_raise": 100,
}


FORTIOS_ENABLE_DISABLE_FIELDS: frozenset[str] = frozenset(
    {
        "arp_reply",
        "permit_any_host",
        "nat64",
        "add_nat64_route",
        "subnet_broadcast_in_ippool",
        "cgn_fixedalloc",
        "cgn_overload",
        "cgn_spa",
    }
)


# ----------------------------------------------------------------------
# IPv6 IP pools
# ----------------------------------------------------------------------

FORTIOS_746_IPPOOL6_FIELDS: frozenset[str] = frozenset(
    {
        "add_nat46_route",
        "comments",
        "endip",
        "nat46",
        "startip",
    }
)


FORTIOS_746_IPPOOL6_DEFAULTS: dict[str, Any] = {
    "add_nat46_route": "enable",
    "endip": "::",
    "nat46": "disable",
    "startip": "::",
}


# ----------------------------------------------------------------------
# Generic helpers
# ----------------------------------------------------------------------

def _is_valid_ipv4(value: Any) -> bool:
    if value is None:
        return True

    try:
        IPv4Address(str(value))
        return True

    except ValueError:
        return False


def _is_valid_ipv6(value: Any) -> bool:
    if value is None:
        return True

    try:
        IPv6Address(str(value))
        return True

    except ValueError:
        return False


def _validate_integer_range(
    issues: list[str],
    *,
    field_name: str,
    value: Any,
    minimum: int,
    maximum: int,
) -> None:
    if value is None:
        return

    if not isinstance(value, int):
        issues.append(
            f"{field_name.replace('_', '-')} must be an integer."
        )
        return

    if not minimum <= value <= maximum:
        issues.append(
            f"{field_name.replace('_', '-')} value {value} is outside "
            f"FortiOS 7.4.6 range {minimum}-{maximum}."
        )


def _validate_zero_or_range(
    issues: list[str],
    *,
    field_name: str,
    value: Any,
    minimum: int,
    maximum: int,
) -> None:
    if value is None or value == 0:
        return

    if not isinstance(value, int):
        issues.append(
            f"{field_name.replace('_', '-')} must be an integer."
        )
        return

    if not minimum <= value <= maximum:
        issues.append(
            f"{field_name.replace('_', '-')} value {value} must be "
            f"0 or within {minimum}-{maximum}."
        )


def _effective_settings(
    item: Any,
    defaults: dict[str, Any],
) -> dict[str, Any]:
    """
    Return an effective FortiOS view without mutating the source model.

    Explicitly configured values win. Missing values use documented
    FortiOS 7.4.6 defaults.
    """

    explicit_fields = set(
        getattr(item, "explicit_fields", set())
    )

    result: dict[str, Any] = {}

    for field_name, default in defaults.items():
        if field_name in explicit_fields:
            result[field_name] = getattr(
                item,
                field_name,
                None,
            )
        else:
            result[field_name] = default

    return result


# ----------------------------------------------------------------------
# IPv4 validation
# ----------------------------------------------------------------------

def validate_ippool_746(
    pool: Any,
) -> list[str]:
    """Validate explicitly extracted IPv4 IP-pool source data."""

    issues: list[str] = []

    pool_type = getattr(pool, "type", None)

    if (
        pool_type is not None
        and pool_type not in FORTIOS_746_IPPOOL_TYPES
    ):
        issues.append(
            f"Unknown FortiOS IP-pool type {pool_type!r}."
        )

    for field_name, (
        minimum,
        maximum,
    ) in FORTIOS_746_IPPOOL_INTEGER_RANGES.items():
        _validate_integer_range(
            issues,
            field_name=field_name,
            value=getattr(pool, field_name, None),
            minimum=minimum,
            maximum=maximum,
        )

    for field_name, (
        minimum,
        maximum,
    ) in FORTIOS_746_IPPOOL_ZERO_OR_RANGES.items():
        _validate_zero_or_range(
            issues,
            field_name=field_name,
            value=getattr(pool, field_name, None),
            minimum=minimum,
            maximum=maximum,
        )

    # --------------------------------------------------------------
    # IPv4 fields
    # --------------------------------------------------------------

    ipv4_fields = (
        "startip",
        "endip",
        "source_startip",
        "source_endip",
        "cgn_client_startip",
        "cgn_client_endip",
    )

    for field_name in ipv4_fields:
        value = getattr(pool, field_name, None)

        if value is not None and not _is_valid_ipv4(value):
            issues.append(
                f"{field_name.replace('_', '-')} contains "
                f"invalid IPv4 address {value!r}."
            )

    for address in getattr(pool, "exclude_ip", []):
        if not _is_valid_ipv4(address):
            issues.append(
                f"exclude-ip contains invalid IPv4 "
                f"address {address!r}."
            )

    # --------------------------------------------------------------
    # Address ordering
    # --------------------------------------------------------------

    for start_field, end_field in (
        ("startip", "endip"),
        ("source_startip", "source_endip"),
        ("cgn_client_startip", "cgn_client_endip"),
    ):
        start = getattr(pool, start_field, None)
        end = getattr(pool, end_field, None)

        if (
            start is not None
            and end is not None
            and _is_valid_ipv4(start)
            and _is_valid_ipv4(end)
            and IPv4Address(start) > IPv4Address(end)
        ):
            issues.append(
                f"{start_field.replace('_', '-')} is greater than "
                f"{end_field.replace('_', '-')}."
            )

    # --------------------------------------------------------------
    # Port ordering
    # --------------------------------------------------------------

    for start_field, end_field in (
        ("startport", "endport"),
        ("cgn_port_start", "cgn_port_end"),
    ):
        start = getattr(pool, start_field, None)
        end = getattr(pool, end_field, None)

        if (
            isinstance(start, int)
            and isinstance(end, int)
            and start > end
        ):
            issues.append(
                f"{start_field.replace('_', '-')} is greater than "
                f"{end_field.replace('_', '-')}."
            )

    # --------------------------------------------------------------
    # enable / disable fields
    # --------------------------------------------------------------

    for field_name in FORTIOS_ENABLE_DISABLE_FIELDS:
        value = getattr(pool, field_name, None)

        if (
            value is not None
            and value not in {"enable", "disable"}
        ):
            issues.append(
                f"{field_name.replace('_', '-')} has invalid "
                f"FortiOS value {value!r}."
            )

    # --------------------------------------------------------------
    # Length constraints
    # --------------------------------------------------------------

    for field_name, maximum in (
        ("name", 79),
        ("comments", 255),
        ("associated_interface", 15),
        ("arp_intf", 15),
    ):
        value = getattr(pool, field_name, None)

        if (
            value is not None
            and len(str(value)) > maximum
        ):
            issues.append(
                f"{field_name.replace('_', '-')} exceeds "
                f"FortiOS 7.4.6 maximum length {maximum}."
            )

    # --------------------------------------------------------------
    # Parser conversion failures
    # --------------------------------------------------------------

    raw_extra = getattr(pool, "raw_extra", {})

    for key in sorted(raw_extra):
        if key.startswith("unparsed_"):
            issues.append(
                "Could not parse explicit source value for "
                f"{key.removeprefix('unparsed_').replace('_', '-')}."
            )

    return list(dict.fromkeys(issues))


def effective_ippool_settings(
    pool: Any,
) -> dict[str, Any]:
    """
    Return documented FortiOS 7.4.6 effective IP-pool settings.

    The source model itself is not modified.
    """

    return _effective_settings(
        pool,
        FORTIOS_746_IPPOOL_DEFAULTS,
    )


# ----------------------------------------------------------------------
# IPv6 validation
# ----------------------------------------------------------------------

def validate_ippool6_746(
    pool: Any,
) -> list[str]:
    """Validate explicitly extracted IPv6 IP-pool source data."""

    issues: list[str] = []

    for field_name in (
        "startip",
        "endip",
    ):
        value = getattr(pool, field_name, None)

        if (
            value is not None
            and not _is_valid_ipv6(value)
        ):
            issues.append(
                f"{field_name} contains invalid IPv6 "
                f"address {value!r}."
            )

    for field_name in (
        "nat46",
        "add_nat46_route",
    ):
        value = getattr(pool, field_name, None)

        if (
            value is not None
            and value not in {"enable", "disable"}
        ):
            issues.append(
                f"{field_name.replace('_', '-')} has invalid "
                f"FortiOS value {value!r}."
            )

    start = getattr(pool, "startip", None)
    end = getattr(pool, "endip", None)

    if (
        start is not None
        and end is not None
        and _is_valid_ipv6(start)
        and _is_valid_ipv6(end)
        and IPv6Address(start) > IPv6Address(end)
    ):
        issues.append(
            "startip is greater than endip."
        )

    for field_name, maximum in (
        ("name", 79),
        ("comments", 255),
    ):
        value = getattr(pool, field_name, None)

        if (
            value is not None
            and len(str(value)) > maximum
        ):
            issues.append(
                f"{field_name} exceeds FortiOS 7.4.6 "
                f"maximum length {maximum}."
            )

    raw_extra = getattr(pool, "raw_extra", {})

    for key in sorted(raw_extra):
        if key.startswith("unparsed_"):
            issues.append(
                "Could not parse explicit source value for "
                f"{key.removeprefix('unparsed_').replace('_', '-')}."
            )

    return list(dict.fromkeys(issues))


def effective_ippool6_settings(
    pool: Any,
) -> dict[str, Any]:
    """Return documented FortiOS 7.4.6 effective IPv6 IP-pool settings."""

    return _effective_settings(
        pool,
        FORTIOS_746_IPPOOL6_DEFAULTS,
    )