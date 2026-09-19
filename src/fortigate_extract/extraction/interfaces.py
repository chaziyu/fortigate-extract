from __future__ import annotations

from model.interface import (
    FGInterface,
    FGInterfaceSecondaryIP,
)
from model.config import FGConfig
from nodes import FortiGateConfigTree

from .common import (
    evaluate_edit,
    get_child_config,
    iter_section_edits,
    source_model_kwargs,
)


def extract_interfaces(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    for source in iter_section_edits(
        tree,
        "system interface",
    ):
        evaluation = evaluate_edit(
            "system interface",
            source.edit,
        )

        attributes = source_model_kwargs(
            evaluation,
            name=source.edit.name,
            vdom=source.vdom,
        )

        # Source CLI:
        #     set member ...
        #
        # Source model:
        #     members: list[str]
        if "member" in attributes:
            attributes["members"] = attributes.pop(
                "member"
            )

        secondary_config = get_child_config(
            source.edit,
            "secondaryip",
        )

        attributes["secondary_ips"] = (
            _extract_secondary_ips(
                secondary_config,
            )
            if secondary_config
            else []
        )

        config.interfaces.append(
            FGInterface(**attributes)
        )


def _extract_secondary_ips(
    section,
) -> list[FGInterfaceSecondaryIP]:
    result: list[FGInterfaceSecondaryIP] = []

    for edit in section.edits:
        evaluation = evaluate_edit(
            "system interface secondaryip",
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
            FGInterfaceSecondaryIP(**attributes)
        )

    return result