from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel


class ExtractionConfig(BaseModel):
    """
    Runtime configuration for FortiGate source extraction.

    This configuration controls input handling and extraction behavior only.
    Migration semantics, derived views, validation results, and report
    persistence are handled by their respective layers.
    """

    # Input handling.
    encoding: str = "utf-8"

    # Extraction behavior.
    preserve_unknown_sections: bool = True
    preserve_unknown_fields: bool = True
    include_source_metadata: bool = True

    # Validation behavior.
    validate_references: bool = True
    validate_required_fields: bool = True

    @classmethod
    def from_yaml(
        cls,
        filepath: str | Path,
    ) -> "ExtractionConfig":
        path = Path(filepath)

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = yaml.safe_load(file)

        return cls.model_validate(
            data or {}
        )