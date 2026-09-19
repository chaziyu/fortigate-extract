from __future__ import annotations

from model.config import FGConfig
from model.routing import FGStaticRoute
from nodes import FortiGateConfigTree

from .common import (
    evaluate_edit,
    iter_section_edits,
    source_model_kwargs,
)


def extract_routes(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    _extract_static_routes(
        tree,
        config,
        section_path="router static",
        address_family="ipv4",
    )

    # Add only if you support an IPv6 route model/report.
    # _extract_static_routes(
    #     tree,
    #     config,
    #     section_path="router static6",
    #     address_family="ipv6",
    # )


def _extract_static_routes(
    tree: FortiGateConfigTree,
    config: FGConfig,
    *,
    section_path: str,
    address_family: str,
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
            vdom=source.vdom,
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

        # Section identity is derived structural information,
        # not a FortiOS command field.
        attributes["address_family"] = address_family

        config.static_routes.append(
            FGStaticRoute(**attributes)
        )