from __future__ import annotations

from model.config import FGConfig
from model.policy import FGPolicy
from nodes import FortiGateConfigTree

from .common import (
    evaluate_edit,
    iter_section_edits,
    source_model_kwargs,
)


POLICY_LIST_ALIASES = {
    # Usually these can remain identical, but keeping this here makes
    # source→model naming differences explicit if needed later.
}


def extract_policies(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    """
    Extract `config firewall policy` objects.

    This function only constructs FortiGate source models.

    It does not:
        - derive NAT rules
        - resolve addresses/services
        - apply FortiOS defaults
        - infer NGFW behavior
        - infer central NAT behavior
        - validate cross-object references
    """

    section_path = "firewall policy"

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

        # FortiGate firewall-policy edit keys are policy IDs.
        try:
            attributes["policy_id"] = int(
                source.edit.name
            )
        except ValueError:
            attributes["raw_extra"]["unparsed_policy_id"] = (
                source.edit.name
            )

            # Skip model construction only if policy_id is mandatory.
            # Alternatively make policy_id optional in FGPolicy if you
            # explicitly want malformed objects preserved as typed models.
            continue

        config.policies.append(
            FGPolicy(**attributes)
        )