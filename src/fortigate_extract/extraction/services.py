from __future__ import annotations

from model.config import FGConfig
from model.service import (
    FGService,
    FGServiceCategory,
    FGServiceGroup,
)
from nodes import FortiGateConfigTree

from .common import (
    evaluate_edit,
    iter_section_edits,
    source_model_kwargs,
)


def extract_services(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    _extract_categories(tree, config)
    _extract_custom_services(tree, config)
    _extract_service_groups(tree, config)


def _extract_categories(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "firewall service category"

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

        config.service_categories.append(
            FGServiceCategory(**attributes)
        )


def _extract_custom_services(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "firewall service custom"

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

        config.services.append(
            FGService(**attributes)
        )


def _extract_service_groups(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "firewall service group"

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

        config.service_groups.append(
            FGServiceGroup(**attributes)
        )