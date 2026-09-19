"""Evaluate FortiGate source commands in source order."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping

from .nodes import CommandNode, UnknownCommandNode
from .section_registry import SectionSpec


@dataclass(frozen=True, slots=True)
class CommandEvaluation:
    """
    Result of evaluating commands from one FortiGate source object.

    `attributes`
        Typed/declared source fields that can be passed to a FortiGate model.

    `explicit_fields`
        Fields explicitly configured by set/append and still effective after
        all commands have been evaluated.

    `unset_fields`
        Fields explicitly unset in the final source command sequence.

    `secret_fields_present`
        Secret fields that were configured. Secret values are never retained.

    `extra_settings`
        Explicit source fields not represented by the declared section schema,
        plus malformed values that could not be converted.
    """

    attributes: dict[str, Any] = field(default_factory=dict)
    explicit_fields: set[str] = field(default_factory=set)
    unset_fields: set[str] = field(default_factory=set)
    secret_fields_present: set[str] = field(default_factory=set)
    extra_settings: dict[str, Any] = field(default_factory=dict)


def normalize_key(key: str) -> str:
    """Convert FortiOS field spelling to Python model spelling."""

    normalized = key.replace("-", "_")

    if normalized == "threshold(default)":
        return "threshold_default"

    if normalized == "tacacs+_server":
        return "tacacs_server"

    return normalized


def _raw_value(
    values: list[str],
    *,
    scalar: bool = False,
) -> Any:
    """
    Preserve a source value without applying FortiOS semantics.

    Examples:
        []              -> True
        ["enable"]      -> "enable"
        ["a", "b"]      -> ["a", "b"]

    A declared scalar field joins multiple tokens because some FortiOS scalar
    values are represented by multiple lexical values.
    """

    if not values:
        return True

    if len(values) == 1:
        return values[0]

    if scalar:
        return " ".join(values)

    return list(values)


def _append_values(
    current: Any,
    values: list[Any],
) -> list[Any]:
    """Append values while tolerating a previously scalar value."""

    if current is None:
        return list(values)

    if isinstance(current, list):
        return [*current, *values]

    return [current, *values]


def _record_extra(
    extras: dict[str, Any],
    key: str,
    value: Any,
) -> None:
    """
    Preserve repeated unsupported values without destroying earlier evidence.
    """

    if key not in extras:
        extras[key] = value
        return

    current = extras[key]

    if not isinstance(current, list):
        current = [current]

    if isinstance(value, list):
        extras[key] = [*current, *value]
    else:
        extras[key] = [*current, value]


def evaluate_commands(
    commands: Iterable[CommandNode | UnknownCommandNode],
    *,
    list_fields: Iterable[str] = (),
    integer_fields: Iterable[str] = (),
    integer_list_fields: Iterable[str] = (),
    scalar_fields: Iterable[str] = (),
    secret_fields: Iterable[str] = (),
    initial: Mapping[str, Any] | None = None,
) -> CommandEvaluation:
    """
    Apply FortiGate set/append/unset operations in source order.

    This function performs only source-state evaluation and simple declared
    type conversion.

    It does not:
        - apply FortiOS defaults
        - resolve references
        - normalize vendor semantics
        - validate configuration
        - construct FortiGate models
    """

    list_fields = {normalize_key(key) for key in list_fields}
    integer_fields = {normalize_key(key) for key in integer_fields}
    integer_list_fields = {
        normalize_key(key)
        for key in integer_list_fields
    }
    scalar_fields = {normalize_key(key) for key in scalar_fields}
    secret_fields = {normalize_key(key) for key in secret_fields}

    declared_fields = (
        list_fields
        | integer_fields
        | integer_list_fields
        | scalar_fields
    )

    attributes: dict[str, Any] = dict(initial or {})
    extras: dict[str, Any] = {}

    explicit_fields: set[str] = set()
    unset_fields: set[str] = set()
    secret_fields_present: set[str] = set()

    for command in commands:
        if isinstance(command, UnknownCommandNode):
            _record_extra(
                extras,
                f"unknown_command:{command.keyword}",
                list(command.values),
            )
            continue

        key = normalize_key(command.key)
        operation = command.operation.lower()
        values = list(command.values)

        # --------------------------------------------------------------
        # Secret handling
        # --------------------------------------------------------------

        if key in secret_fields:
            attributes.pop(key, None)
            extras.pop(key, None)

            if operation == "unset":
                secret_fields_present.discard(key)
                explicit_fields.discard(key)
                unset_fields.add(key)

            elif operation in {"set", "append"}:
                secret_fields_present.add(key)
                explicit_fields.add(key)
                unset_fields.discard(key)

            else:
                _record_extra(
                    extras,
                    f"unsupported_operation:{operation}:{key}",
                    True,
                )

            continue

        # --------------------------------------------------------------
        # unset
        # --------------------------------------------------------------

        if operation == "unset":
            attributes.pop(key, None)
            extras.pop(key, None)
            extras.pop(f"unparsed_{key}", None)

            explicit_fields.discard(key)
            unset_fields.add(key)

            continue

        # --------------------------------------------------------------
        # Only set / append are evaluated
        # --------------------------------------------------------------

        if operation not in {"set", "append"}:
            _record_extra(
                extras,
                f"unsupported_operation:{operation}:{key}",
                values if values else True,
            )
            continue

        explicit_fields.add(key)
        unset_fields.discard(key)

        # --------------------------------------------------------------
        # Integer list
        # --------------------------------------------------------------

        if key in integer_list_fields:
            parsed: list[int] = []
            malformed: list[str] = []

            for value in values:
                try:
                    parsed.append(int(value))
                except (TypeError, ValueError):
                    malformed.append(str(value))

            if operation == "set":
                attributes[key] = parsed
            else:
                attributes[key] = _append_values(
                    attributes.get(key),
                    parsed,
                )

            if malformed:
                _record_extra(
                    extras,
                    f"unparsed_{key}",
                    malformed,
                )

            continue

        # --------------------------------------------------------------
        # Integer scalar
        # --------------------------------------------------------------

        if key in integer_fields:
            if operation == "append":
                _record_extra(
                    extras,
                    f"unsupported_append_{key}",
                    values if values else True,
                )
                continue

            if len(values) != 1:
                _record_extra(
                    extras,
                    f"unparsed_{key}",
                    _raw_value(values),
                )
                attributes.pop(key, None)
                continue

            try:
                attributes[key] = int(values[0])
            except (TypeError, ValueError):
                attributes.pop(key, None)

                _record_extra(
                    extras,
                    f"unparsed_{key}",
                    values[0],
                )

            continue

        # --------------------------------------------------------------
        # List
        # --------------------------------------------------------------

        if key in list_fields:
            if operation == "set":
                attributes[key] = list(values)
            else:
                attributes[key] = _append_values(
                    attributes.get(key),
                    values,
                )

            continue

        # --------------------------------------------------------------
        # Scalar
        # --------------------------------------------------------------

        if key in scalar_fields:
            if operation == "set":
                attributes[key] = _raw_value(
                    values,
                    scalar=True,
                )
            else:
                # Appending to a scalar has ambiguous semantics.
                _record_extra(
                    extras,
                    f"unsupported_append_{key}",
                    values if values else True,
                )

            continue

        # --------------------------------------------------------------
        # Unknown field
        # --------------------------------------------------------------

        value = _raw_value(values)

        if operation == "set":
            extras[key] = value

        else:
            extras[key] = _append_values(
                extras.get(key),
                values,
            )

    # Only declared fields belong in attributes.
    attributes = {
        key: value
        for key, value in attributes.items()
        if key in declared_fields or key in (initial or {})
    }

    return CommandEvaluation(
        attributes=attributes,
        explicit_fields=explicit_fields,
        unset_fields=unset_fields,
        secret_fields_present=secret_fields_present,
        extra_settings=extras,
    )


def evaluate_section_commands(
    commands: Iterable[CommandNode | UnknownCommandNode],
    spec: SectionSpec | None,
    *,
    initial: Mapping[str, Any] | None = None,
) -> CommandEvaluation:
    """Evaluate commands using a section registry specification."""

    if spec is None:
        return evaluate_commands(
            commands,
            initial=initial,
        )

    return evaluate_commands(
        commands,
        list_fields=spec.list_fields,
        integer_fields=spec.integer_fields,
        integer_list_fields=spec.integer_list_fields,
        scalar_fields=spec.scalar_fields,
        secret_fields=spec.secret_fields,
        initial=initial,
    )