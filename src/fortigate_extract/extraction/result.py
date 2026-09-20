from __future__ import annotations

from dataclasses import dataclass

from ..model.source import FGConfig


@dataclass(slots=True)
class ExtractionResult:
    """Result of FortiGate source extraction."""

    config: FGConfig