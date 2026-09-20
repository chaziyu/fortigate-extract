from __future__ import annotations

from collections.abc import Iterator, Mapping
from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from ..command_evaluator import (
    CommandEvaluation,
    evaluate_commands,
)
from ..nodes import (
    ConfigNode,
    EditNode,
    FortiGateConfigTree,
)
from ..section_registry import get_section_spec


_SOURCE_KEY_OVERRIDES = {
    "tacacs+-server": "tacacs_server",
    "threshold(default)": "threshold_default",
}


@dataclass(frozen=True, slots=True)
class SectionEdit:
    """
    One edit block with its FortiGate source context.
    """

    section_path: str
    edit: EditNode
    vdom: str = "root"


def normalize_source_key(key: str) -> str:
    """
    Convert a raw FortiGate CLI field name to a Python field name.

    Normalization belongs at the extraction boundary.

    The tokenizer, parser, structural nodes, section registry, and command
    evaluator retain the original FortiGate CLI spelling.
    """

    if key in _SOURCE_KEY_OVERRIDES:
        return _SOURCE_KEY_OVERRIDES[key]

    return key.replace("-", "_")


def _model_field_name(
    source_key: str,
    field_map: Mapping[str, str],
) -> str:
    """
    Resolve one raw FortiGate source key to its target model field.

    `field_map` may reference either the raw CLI spelling or the normalized
    source spelling.

    Examples:
        member          -> members
        exclude-member  -> exclude_members
    """

    normalized = normalize_source_key(source_key)

    if source_key in field_map:
        return field_map[source_key]

    if normalized in field_map:
        return field_map[normalized]

    return normalized


def _record_raw_extra(
    raw_extra: dict[str, Any],
    key: str,
    value: Any,
) -> None:
    """
    Preserve source data without overwriting earlier evidence.

    Keys remain in original FortiGate CLI spelling whenever possible.
    """

    if key not in raw_extra:
        raw_extra[key] = value
        return

    current = raw_extra[key]

    if not isinstance(current, list):
        current = [current]

    if isinstance(value, list):
        raw_extra[key] = [
            *current,
            *value,
        ]
    else:
        raw_extra[key] = [
            *current,
            value,
        ]


def evaluate_edit(
    section_path: str,
    edit: EditNode,
) -> CommandEvaluation:
    """
    Evaluate explicit commands from one edit block.

    The section registry provides only primitive source-field shapes.

    This function does not:
        - normalize source keys
        - construct source models
        - apply FortiOS defaults
        - resolve references
        - derive topology
        - perform validation
    """

    spec = get_section_spec(section_path)

    if spec is None:
        return evaluate_commands(
            edit.commands,
        )

    return evaluate_commands(
        edit.commands,
        list_fields=spec.list_fields,
        integer_fields=spec.integer_fields,
        integer_list_fields=spec.integer_list_fields,
        scalar_fields=spec.scalar_fields,
    )


def source_model_kwargs(
    evaluation: CommandEvaluation,
    *,
    model_type: type[BaseModel],
    name: str | None = None,
    vdom: str | None = None,
    field_map: Mapping[str, str] | None = None,
) -> dict[str, Any]:
    """
    Convert evaluated source state into kwargs for one source model.

    Processing order:

        raw evaluated source field
        -> extraction-side key normalization
        -> optional domain field mapping
        -> model field, if supported
        -> raw_extra, if deliberately omitted from the small model

    Unsupported/untyped source data already present in
    `evaluation.untyped_values` is also retained in `raw_extra`.

    `field_map` handles domain-specific source-to-model naming.

    Example:

        field_map={
            "member": "members",
            "exclude_member": "exclude_members",
        }

    Raw-extra keys retain FortiGate CLI spelling.
    """

    field_map = dict(
        field_map or {}
    )

    model_fields = set(
        model_type.model_fields
    )

    values: dict[str, Any] = {}

    raw_extra: dict[str, Any] = dict(
        evaluation.untyped_values
    )

    explicit_fields: set[str] = set()

    # --------------------------------------------------------------
    # Evaluated declared source fields
    # --------------------------------------------------------------

    for source_key, value in evaluation.values.items():
        target_key = _model_field_name(
            source_key,
            field_map,
        )

        if target_key in model_fields:
            values[target_key] = value
            continue

        # The registry knows this field and the evaluator typed it,
        # but the deliberately small source model does not retain it.
        #
        # Preserve it rather than allowing Pydantic to silently drop it.
        _record_raw_extra(
            raw_extra,
            source_key,
            value,
        )

    # --------------------------------------------------------------
    # Explicit source-field tracking
    # --------------------------------------------------------------

    for source_key in evaluation.explicit_fields:
        target_key = _model_field_name(
            source_key,
            field_map,
        )

        if target_key in model_fields:
            explicit_fields.add(
                target_key
            )

    # --------------------------------------------------------------
    # Source object identity/context
    # --------------------------------------------------------------

    if name is not None:
        if "name" not in model_fields:
            raise ValueError(
                f"{model_type.__name__} does not define "
                f"a 'name' field"
            )

        values["name"] = name

    if vdom is not None:
        if "vdom" not in model_fields:
            raise ValueError(
                f"{model_type.__name__} does not define "
                f"a 'vdom' field"
            )

        values["vdom"] = vdom

    # --------------------------------------------------------------
    # Source-preservation metadata
    # --------------------------------------------------------------

    if raw_extra:
        if "raw_extra" not in model_fields:
            raise ValueError(
                f"{model_type.__name__} cannot preserve "
                f"raw source fields because it does not define "
                f"'raw_extra'"
            )

        values["raw_extra"] = raw_extra
    elif "raw_extra" in model_fields:
        values["raw_extra"] = {}

    if "explicit_fields" in model_fields:
        values["explicit_fields"] = explicit_fields

    return values


def get_child_config(
    edit: EditNode,
    name: str,
) -> ConfigNode | None:
    """
    Return the first direct child config with the requested structural name.
    """

    for child in edit.children:
        if child.name == name:
            return child

    return None


def iter_section_edits(
    tree: FortiGateConfigTree,
    section_path: str,
) -> Iterator[SectionEdit]:
    """
    Yield edit blocks belonging to the requested FortiGate section.

    VDOM context is derived from the structural tree rather than mutable
    parser state.
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

        # FortiGate VDOM structure:
        #
        # config vdom
        #     edit <vdom-name>
        #         config ...
        #         end
        #     next
        # end
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