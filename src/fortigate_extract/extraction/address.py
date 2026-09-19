from __future__ import annotations

from model.address import (
    FGAddress,
    FGAddressGroup,
    FGAddressGroupTaggingEntry,
    FGWildcardFQDN,
)
from model.config import FGConfig
from nodes import FortiGateConfigTree

from .common import (
    evaluate_edit,
    get_child_config,
    iter_section_edits,
    source_model_kwargs,
)


def extract_addresses(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    _extract_address_family(
        tree,
        config,
        section_path="firewall address",
    )

    _extract_address_family(
        tree,
        config,
        section_path="firewall address6",
    )

    _extract_address_groups(
        tree,
        config,
        section_path="firewall addrgrp",
    )

    _extract_address_groups(
        tree,
        config,
        section_path="firewall addrgrp6",
    )

    _extract_wildcard_fqdns(
        tree,
        config,
    )


def _extract_address_family(
    tree: FortiGateConfigTree,
    config: FGConfig,
    *,
    section_path: str,
) -> None:
    for source in iter_section_edits(
        tree,
        section_path,
    ):
        evaluation = evaluate_edit(
            section_path,
            source.edit,
        )

        attributes = source_model_kwargs(
            evaluation,
            name=source.edit.name,
            vdom=source.vdom,
        )

        # Address family is derived from source section,
        # not invented as a source CLI field.
        attributes["address_family"] = (
            "ipv6"
            if section_path.endswith("address6")
            else "ipv4"
        )

        config.addresses.append(
            FGAddress(**attributes)
        )


def _extract_address_groups(
    tree: FortiGateConfigTree,
    config: FGConfig,
    *,
    section_path: str,
) -> None:
    for source in iter_section_edits(
        tree,
        section_path,
    ):
        evaluation = evaluate_edit(
            section_path,
            source.edit,
        )

        attributes = source_model_kwargs(
            evaluation,
            name=source.edit.name,
            vdom=source.vdom,
        )

        if "member" in attributes:
            attributes["members"] = attributes.pop(
                "member"
            )

        if "exclude_member" in attributes:
            attributes["exclude_members"] = (
                attributes.pop("exclude_member")
            )

        tagging = get_child_config(
            source.edit,
            "tagging",
        )

        attributes["tagging"] = (
            _extract_group_tagging(
                tagging,
                section_path=section_path,
            )
            if tagging
            else []
        )

        config.address_groups.append(
            FGAddressGroup(**attributes)
        )


def _extract_group_tagging(
    section,
    *,
    section_path: str,
) -> list[FGAddressGroupTaggingEntry]:
    result = []

    tagging_path = f"{section_path} tagging"

    for edit in section.edits:
        evaluation = evaluate_edit(
            tagging_path,
            edit,
        )

        attributes = source_model_kwargs(
            evaluation,
            name=edit.name,
        )

        result.append(
            FGAddressGroupTaggingEntry(
                **attributes
            )
        )

    return result


def _extract_wildcard_fqdns(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "firewall wildcard-fqdn custom"

    for source in iter_section_edits(
        tree,
        section_path,
    ):
        evaluation = evaluate_edit(
            section_path,
            source.edit,
        )

        attributes = source_model_kwargs(
            evaluation,
            name=source.edit.name,
            vdom=source.vdom,
        )

        config.wildcard_fqdns.append(
            FGWildcardFQDN(**attributes)
        )