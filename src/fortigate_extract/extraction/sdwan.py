from __future__ import annotations

from model.config import FGConfig
from model.sdwan import (
    FGSDWAN,
    FGSDWANHealthCheck,
    FGSDWANMember,
    FGSDWANService,
    FGSDWANZone,
)
from nodes import ConfigNode, FortiGateConfigTree

from .common import (
    evaluate_edit,
    iter_section_edits,
    source_model_kwargs,
)


def extract_sdwan(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    """
    Extract SD-WAN configuration per VDOM.

    One FGSDWAN aggregate is created for each VDOM where SD-WAN
    configuration is encountered.
    """

    sdwan_by_vdom: dict[str, FGSDWAN] = {}

    _extract_sdwan_root(
        tree,
        sdwan_by_vdom,
    )

    _extract_zones(
        tree,
        sdwan_by_vdom,
    )

    _extract_members(
        tree,
        sdwan_by_vdom,
    )

    _extract_health_checks(
        tree,
        sdwan_by_vdom,
    )

    _extract_services(
        tree,
        sdwan_by_vdom,
    )

    config.sdwans.extend(
        sdwan_by_vdom.values()
    )


def _get_sdwan(
    sdwan_by_vdom: dict[str, FGSDWAN],
    vdom: str,
) -> FGSDWAN:
    item = sdwan_by_vdom.get(vdom)

    if item is None:
        item = FGSDWAN(
            vdom=vdom,
        )
        sdwan_by_vdom[vdom] = item

    return item


def _extract_sdwan_root(
    tree: FortiGateConfigTree,
    sdwan_by_vdom: dict[str, FGSDWAN],
) -> None:
    """
    Extract commands directly under `config system sdwan`.

    This requires section-level command traversal rather than edit traversal.
    """

    for section, vdom in _iter_config_sections(
        tree,
        "system sdwan",
    ):
        evaluation = evaluate_edit_like_config(
            "system sdwan",
            section,
        )

        sdwan = _get_sdwan(
            sdwan_by_vdom,
            vdom,
        )

        for key, value in evaluation.attributes.items():
            if hasattr(sdwan, key):
                setattr(sdwan, key, value)
            else:
                sdwan.raw_extra[key] = value

        sdwan.explicit_fields.update(
            evaluation.explicit_fields
        )

        sdwan.raw_extra.update(
            evaluation.extra_settings
        )


def _extract_zones(
    tree: FortiGateConfigTree,
    sdwan_by_vdom: dict[str, FGSDWAN],
) -> None:
    section_path = "system sdwan zone"

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
        )

        _get_sdwan(
            sdwan_by_vdom,
            source.vdom,
        ).zones.append(
            FGSDWANZone(**attributes)
        )


def _extract_members(
    tree: FortiGateConfigTree,
    sdwan_by_vdom: dict[str, FGSDWAN],
) -> None:
    section_path = "system sdwan members"

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
        )

        try:
            attributes["seq_num"] = int(
                source.edit.name
            )
        except ValueError:
            attributes["raw_extra"]["unparsed_seq_num"] = (
                source.edit.name
            )
            continue

        _get_sdwan(
            sdwan_by_vdom,
            source.vdom,
        ).members.append(
            FGSDWANMember(**attributes)
        )


def _extract_health_checks(
    tree: FortiGateConfigTree,
    sdwan_by_vdom: dict[str, FGSDWAN],
) -> None:
    section_path = "system sdwan health-check"

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
        )

        _get_sdwan(
            sdwan_by_vdom,
            source.vdom,
        ).health_checks.append(
            FGSDWANHealthCheck(**attributes)
        )


def _extract_services(
    tree: FortiGateConfigTree,
    sdwan_by_vdom: dict[str, FGSDWAN],
) -> None:
    section_path = "system sdwan service"

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
        )

        try:
            attributes["id"] = int(
                source.edit.name
            )
        except ValueError:
            attributes["raw_extra"]["unparsed_id"] = (
                source.edit.name
            )
            continue

        _get_sdwan(
            sdwan_by_vdom,
            source.vdom,
        ).services.append(
            FGSDWANService(**attributes)
        )