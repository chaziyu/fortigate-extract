from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from command_evaluator import (
    CommandEvaluation,
    evaluate_section_commands,
)
from nodes import (
    ConfigNode,
    EditNode,
    FortiGateConfigTree,
)
from section_registry import get_section_spec


@dataclass(frozen=True, slots=True)
class SectionEdit:
    """
    One edit block plus its FortiGate execution context.
    """

    section_path: str
    edit: EditNode
    vdom: str = "root"


def evaluate_edit(
    section_path: str,
    edit: EditNode,
) -> CommandEvaluation:
    """
    Evaluate explicit commands from one edit block.

    No FortiGate defaults or cross-object semantics are applied here.
    """

    return evaluate_section_commands(
        edit.commands,
        get_section_spec(section_path),
    )


def source_model_kwargs(
    evaluation: CommandEvaluation,
    *,
    name: str | None = None,
    vdom: str | None = None,
) -> dict:
    """
    Convert command evaluation into common source-model fields.
    """

    values = dict(evaluation.attributes)

    if name is not None:
        values["name"] = name

    if vdom is not None:
        values["vdom"] = vdom

    values["raw_extra"] = dict(
        evaluation.extra_settings
    )

    values["explicit_fields"] = set(
        evaluation.explicit_fields
    )

    return values


def get_child_config(
    edit: EditNode,
    name: str,
) -> ConfigNode | None:
    for child in edit.children:
        if child.name == name:
            return child

    return None


def iter_section_edits(
    tree: FortiGateConfigTree,
    section_path: str,
) -> Iterator[SectionEdit]:
    """
    Find edit blocks for a section throughout the configuration.

    VDOM context is derived structurally instead of being maintained by
    mutable parser state.
    """

    def walk_config(
        node: ConfigNode,
        *,
        vdom: str,
    ) -> Iterator[SectionEdit]:
        if node.name == section_path:
            for edit in node.edits:
                yield SectionEdit(
                    section_path=section_path,
                    edit=edit,
                    vdom=vdom,
                )

        # Special structural treatment of:
        #
        # config vdom
        #     edit <vdom>
        #         config ...
        #
        if node.name == "vdom":
            for edit in node.edits:
                for child in edit.children:
                    yield from walk_config(
                        child,
                        vdom=edit.name,
                    )

            return

        for child in node.children:
            yield from walk_config(
                child,
                vdom=vdom,
            )

        for edit in node.edits:
            for child in edit.children:
                yield from walk_config(
                    child,
                    vdom=vdom,
                )

    for root in tree.configs:
        yield from walk_config(
            root,
            vdom="root",
        )