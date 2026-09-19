from __future__ import annotations

from model.config import FGConfig
from model.vpn import (
    FGIPsecPhase1,
    FGIPsecPhase2,
)
from nodes import FortiGateConfigTree

from .common import (
    evaluate_edit,
    iter_section_edits,
    source_model_kwargs,
)


def extract_vpn(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    _extract_phase1(tree, config)
    _extract_phase2(tree, config)


def _extract_phase1(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "vpn ipsec phase1-interface"

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

        # Secret values never enter the source model.
        attributes["psk_configured"] = any(
            key in evaluation.secret_fields_present
            for key in {
                "psksecret",
                "psksecret_remote",
            }
        )

        attributes["ppk_secret_configured"] = (
            "ppk_secret"
            in evaluation.secret_fields_present
        )

        attributes["auth_password_configured"] = (
            "authpasswd"
            in evaluation.secret_fields_present
        )

        attributes["group_authentication_secret_configured"] = (
            "group_authentication_secret"
            in evaluation.secret_fields_present
        )

        config.ipsec_phase1.append(
            FGIPsecPhase1(**attributes)
        )


def _extract_phase2(
    tree: FortiGateConfigTree,
    config: FGConfig,
) -> None:
    section_path = "vpn ipsec phase2-interface"

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

        config.ipsec_phase2.append(
            FGIPsecPhase2(**attributes)
        )