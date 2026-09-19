from __future__ import annotations

from model.config import FGConfig
from model.ip_pool import FGIPPool
from nodes import FortiGateConfigTree

from .common import (
    evaluate_edit,
    iter_section_edits,
    source_model_kwargs,
)


def extract_ip_pools(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "firewall ippool"

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

        config.ip_pools.append(
            FGIPPool(**attributes)
        )