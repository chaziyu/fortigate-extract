from __future__ import annotations

from dataclasses import dataclass, field

from model.config import FGConfig
from model.policy import FGPolicy


@dataclass(slots=True)
class ExtractedNATRule:
    """
    Vendor-neutral-ish reporting view derived from FortiGate source objects.

    This is not a FortiGate source model.
    """

    rule_id: str
    name: str | None = None

    nat_type: str = "none"

    source_interfaces: list[str] = field(
        default_factory=list
    )

    destination_interfaces: list[str] = field(
        default_factory=list
    )

    original_source: list[str] = field(
        default_factory=list
    )

    original_destination: list[str] = field(
        default_factory=list
    )

    services: list[str] = field(
        default_factory=list
    )

    source_translation_mode: str | None = None

    translated_source: list[str] = field(
        default_factory=list
    )

    destination_translation_mode: str | None = None

    translated_destination: list[str] = field(
        default_factory=list
    )

    source_policy_id: int | None = None

    description: str | None = None

    review_reasons: list[str] = field(
        default_factory=list
    )


def extract_nat_views(
    config: FGConfig,
) -> list[ExtractedNATRule]:
    """
    Derive NAT report rows from already extracted FortiGate objects.

    Sources currently considered:
        - firewall policies
        - IP pools
        - VIPs
        - VIP groups

    No source models are created or mutated here.
    """

    pools = {
        pool.name: pool
        for pool in config.ip_pools
    }

    vips = {
        vip.name: vip
        for vip in config.vips
    }

    vip_groups = {
        group.name: group
        for group in config.vip_groups
    }

    result: list[ExtractedNATRule] = []

    for policy in config.policies:
        nat_rule = _derive_policy_nat(
            policy,
            pools=pools,
            vips=vips,
            vip_groups=vip_groups,
        )

        if nat_rule is not None:
            result.append(nat_rule)

    return result


def _derive_policy_nat(
    policy: FGPolicy,
    *,
    pools: dict,
    vips: dict,
    vip_groups: dict,
) -> ExtractedNATRule | None:
    """
    Derive one report NAT rule from a firewall policy when NAT behavior
    is explicitly present.
    """

    source_nat = policy.nat == "enable"

    destination_vips = [
        name
        for name in policy.dstaddr
        if name in vips
    ]

    destination_vip_groups = [
        name
        for name in policy.dstaddr
        if name in vip_groups
    ]

    destination_nat = bool(
        destination_vips
        or destination_vip_groups
    )

    if not source_nat and not destination_nat:
        return None

    rule = ExtractedNATRule(
        rule_id=f"policy-{policy.policy_id}",
        name=policy.name,
        source_policy_id=policy.policy_id,
        source_interfaces=list(policy.srcintf),
        destination_interfaces=list(policy.dstintf),
        original_source=list(policy.srcaddr),
        original_destination=list(policy.dstaddr),
        services=list(policy.service),
        description=policy.comments,
    )

    # --------------------------------------------------------------
    # Source NAT
    # --------------------------------------------------------------

    if source_nat:
        _apply_source_nat(
            rule,
            policy,
            pools,
        )

    # --------------------------------------------------------------
    # Destination NAT
    # --------------------------------------------------------------

    if destination_nat:
        _apply_destination_nat(
            rule,
            destination_vips,
            destination_vip_groups,
            vips,
            vip_groups,
        )

    # --------------------------------------------------------------
    # Overall classification
    # --------------------------------------------------------------

    if source_nat and destination_nat:
        rule.nat_type = "source-and-destination"

    elif source_nat:
        rule.nat_type = "source"

    elif destination_nat:
        rule.nat_type = "destination"

    return rule


def _apply_source_nat(
    rule: ExtractedNATRule,
    policy: FGPolicy,
    pools: dict,
) -> None:
    if policy.ippool == "enable":
        rule.source_translation_mode = "ip-pool"

        for pool_name in policy.poolname:
            pool = pools.get(pool_name)

            if pool is None:
                rule.review_reasons.append(
                    f"Unresolved IP pool reference "
                    f"{pool_name!r}."
                )
                continue

            rule.translated_source.extend(
                _pool_translation_values(pool)
            )

    else:
        # FortiGate policy NAT enabled without explicit IP pool.
        #
        # The actual effective semantics are FortiOS-specific and should
        # not be invented in the source model.
        rule.source_translation_mode = (
            "outgoing-interface-address"
        )


def _pool_translation_values(
    pool,
) -> list[str]:
    start = pool.startip
    end = pool.endip

    if start is None and end is None:
        return []

    if start and end and start != end:
        return [
            f"{start}-{end}",
        ]

    return [
        start or end,
    ]


def _apply_destination_nat(
    rule: ExtractedNATRule,
    vip_names: list[str],
    vip_group_names: list[str],
    vips: dict,
    vip_groups: dict,
) -> None:
    rule.destination_translation_mode = "vip"

    resolved_vips = list(vip_names)

    for group_name in vip_group_names:
        group = vip_groups[group_name]

        for member in group.members:
            if member in vips:
                resolved_vips.append(member)
            else:
                rule.review_reasons.append(
                    f"VIP group {group_name!r} references "
                    f"unresolved VIP {member!r}."
                )

    seen: set[str] = set()

    for vip_name in resolved_vips:
        if vip_name in seen:
            continue

        seen.add(vip_name)

        vip = vips[vip_name]

        translations = _vip_translation_values(
            vip
        )

        if translations:
            rule.translated_destination.extend(
                translations
            )
        else:
            rule.review_reasons.append(
                f"VIP {vip_name!r} has no typed mapped "
                "destination value."
            )


def _vip_translation_values(
    vip,
) -> list[str]:
    values: list[str] = []

    for value in vip.mappedip:
        if value:
            values.append(value)

    for value in vip.mapped_addr:
        if value:
            values.append(value)

    return values