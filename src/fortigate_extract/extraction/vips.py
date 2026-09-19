from __future__ import annotations

from model.config import FGConfig
from model.vip import (
    FGVIP,
    FGVIPGroup,
    FGVIPRealServer,
)
from nodes import FortiGateConfigTree

from .common import (
    evaluate_edit,
    get_child_config,
    iter_section_edits,
    source_model_kwargs,
)


def extract_vips(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    _extract_vips(tree, config)
    _extract_vip_groups(tree, config)


def _extract_vips(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "firewall vip"

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

        realservers = get_child_config(
            source.edit,
            "realservers",
        )

        attributes["realservers"] = (
            _extract_realservers(realservers)
            if realservers
            else []
        )

        config.vips.append(
            FGVIP(**attributes)
        )


def _extract_realservers(
    section,
) -> list[FGVIPRealServer]:
    result = []

    for edit in section.edits:
        evaluation = evaluate_edit(
            "firewall vip realservers",
            edit,
        )

        attributes = source_model_kwargs(
            evaluation,
        )

        try:
            attributes["id"] = int(edit.name)
        except ValueError:
            attributes["raw_extra"]["unparsed_id"] = (
                edit.name
            )

        result.append(
            FGVIPRealServer(**attributes)
        )

    return result


def _extract_vip_groups(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "firewall vipgrp"

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

        config.vip_groups.append(
            FGVIPGroup(**attributes)
        )