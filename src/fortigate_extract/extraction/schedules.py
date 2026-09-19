from __future__ import annotations

from model.config import FGConfig
from model.schedule import (
    FGScheduleGroup,
    FGScheduleOnetime,
    FGScheduleRecurring,
)
from nodes import FortiGateConfigTree

from .common import (
    evaluate_edit,
    iter_section_edits,
    source_model_kwargs,
)


def extract_schedules(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    _extract_onetime(tree, config)
    _extract_recurring(tree, config)
    _extract_groups(tree, config)


def _extract_onetime(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "firewall schedule onetime"

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

        config.schedules_onetime.append(
            FGScheduleOnetime(**attributes)
        )


def _extract_recurring(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "firewall schedule recurring"

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

        if "day" in attributes:
            attributes["days"] = attributes.pop(
                "day"
            )

        config.schedules_recurring.append(
            FGScheduleRecurring(**attributes)
        )


def _extract_groups(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "firewall schedule group"

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

        config.schedule_groups.append(
            FGScheduleGroup(**attributes)
        )